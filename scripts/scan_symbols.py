#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scan_symbols.py — ตัวตรวจสัญลักษณ์ต้องห้ามของ math-bank
=========================================================

⚠️ เวอร์ชัน 1 มีช่องโหว่: walker ไม่ลง `imageSpec` (ค่าเป็น dict)
   ⇒ ป้ายกำกับในรูปที่เด็ก "เห็นด้วยตา" ไม่เคยถูกตรวจเลย
   ⇒ ทีมพอร์ทัลจับได้ 31 ก.ค. 2569 (⊄ ใน chap-02-logic-q46)

เวอร์ชัน 2.0 แก้สองอย่าง:
  1. walker ลงทุกชั้น ทั้ง dict และ list — `imageSpec` รวมอยู่ด้วย
  2. มี CANARY SELF-TEST: ฝังข้อล่อที่มีสัญลักษณ์ต้องห้ามใน `imageSpec`
     แล้วบังคับให้ตัวตรวจต้องจับได้ก่อน จึงจะยอมรายงานผลของจริง
     ⛔ ถ้าจับข้อล่อไม่ได้ = ออกด้วยรหัส 2 (ด่านแดง) ไม่ใช่ "ผ่านเพราะไม่เจออะไร"

     เหตุผล (กฎ B8): "0 จุด" อาจแปลว่าสะอาดจริง หรือแปลว่าไม่ได้ตรวจ
     สองอย่างนี้หน้าตาเหมือนกันทุกประการ — canary คือสิ่งเดียวที่แยกมันออก

เวอร์ชัน 2.1 (ตามที่ทีมพอร์ทัลขอ 31 ก.ค. 2569) แก้อีกสี่อย่าง:
  3. โหมด diff-scoped (`--since` / `--changed` / `--changed-ids`)
     BLOCK นับเฉพาะข้อที่ "เปลี่ยนจริงในรอบนี้" · ของเก่าลงชั้น LEGACY
     ⇒ ต่อ CI ได้โดยไม่แดงทุก push จากหนี้เก่า 45 ข้อ
     เหตุผล: ด่านที่แดงตลอดเวลา ทุกคนจะเรียนรู้ที่จะกดข้าม — แย่กว่าไม่มีด่าน
  4. CANARY ของโหมด diff เอง — 4 ตัว บวก anti-canary 2 ตัว
     กันกรณีที่ `--changed` กลายเป็น "ไม่จับอะไรเลย" แล้วไม่มีใครรู้
  5. SCANNER_VERSION เป็นตัวแปรที่หัวไฟล์ (พอร์ทัลใช้ตรวจ drift ด้วย เวอร์ชัน+md5)
  6. ฝั่ง BLOCK มี ratchet เทียบ `block_questions_legacy` ⇒ โหมดทั้งคลังออก 0 ได้

รหัสออก:
    0 = ผ่าน
    1 = ด่านแดงจากเนื้อหา (BLOCK ใหม่ / WARN โต / LEGACY โต)
    2 = ด่านแดงจากตัวตรวจเอง (canary ล้ม — ผลสแกนเชื่อไม่ได้)

การใช้:
    # ทั้งคลัง + ratchet — ใช้ฝั่งพอร์ทัลตอน sync
    python scripts/scan_symbols.py data/sets --baseline docs/warn-baseline.json

    # เฉพาะของที่เปลี่ยนในคอมมิตล่าสุด — ใช้ฝั่ง CI ของ math-bank
    python scripts/scan_symbols.py data/sets --since HEAD~1 --baseline docs/warn-baseline.json

    # ระบุไฟล์เอง (เช่นจาก git diff --name-only ของ CI)
    python scripts/scan_symbols.py data/sets --changed data/sets/gen-chap-01-set.json --base HEAD~1

    # ระบุรหัสข้อเอง (ไม่ต้องมี git — ใช้ตรวจซ้ำด้วยมือ)
    python scripts/scan_symbols.py data/sets --changed-ids gen-chap-01-set-q273,chap-02-logic-q46
"""
import json, os, sys, argparse, subprocess

SCANNER_VERSION = '2.1'
SCANNER_DATE = '2026-07-31'

# ─────────────────────────────────────────────────────────────
# นิยามกฎ
# ─────────────────────────────────────────────────────────────

# ⛔ ห้ามทุกที่ ทุกฟิลด์ — ไม่มีข้อยกเว้น
UNICODE_BANNED = ['⊃', '⊇', '⊆', '⊊', '⊋', '⊅', '⊈', '⊉', '∁', '∖']
MACRO_BANNED = [r'\setminus', r'\backslash', r'\subseteq', r'\subsetneq',
                r'\nsubseteq', r'\supset', r'\supseteq', r'\supsetneq']

# ✅ อนุญาต (หลักสูตรไทยใช้จริง) — ระบุไว้เพื่อไม่ให้ใครเผลอเติมลง BANNED
UNICODE_ALLOWED = ['⊂', '⊄']

# ⚠️ ยกเว้นเฉพาะ "ไฟล์ข้อสอบจริง" และเฉพาะกฎสัญลักษณ์คณิตเท่านั้น
#    ⛔ ไม่ยกเว้นกฎ escape เกินชั้น และ [IMAGE:n] — สองอันนั้นคือความผิดตอนพิมพ์เข้าคลัง
MACRO_REALEXAM_ONLY = [r'\mathbb{I}']

# แมโครที่เด็กอ่านไม่ออกถ้าเจอในโจทย์ — BLOCK ฝั่งโจทย์ / WARN ฝั่งเฉลย
TIERED = [r'\operatorname', r'\lfloor', r'\dbinom', r'\mathrm',
          r'\binom', r'\bmod', r'\lceil', r'\pmod', r'\rfloor', r'\rceil']

# ฟิลด์ที่เด็กเห็นทันทีตอนทำข้อ (imageSpec = ป้ายกำกับที่วาดลง SVG)
STUDENT_NOW = ('question', 'choices', 'imageSpec')
STUDENT_LATER = ('explanation',)

# ⛔ ฟิลด์ที่ห้ามแตะเด็ดขาด — ยูนิโคดในนี้คือ "รายการคำตอบที่ยอมรับ"
#    ถ้าลบทิ้ง ระบบตรวจคำตอบจะพังเงียบ ๆ (เด็กพิมพ์ ∅ แล้วถูกตอบว่าผิด)
FIELDS_NEVER_TOUCH = ('accept',)


def is_real_exam(filename):
    """ข้อสอบจริง = ทุกไฟล์ที่ไม่ได้ขึ้นต้นด้วย chap- / gen-chap-
    ผูกกับ 'ไฟล์' ไม่ใช่ 'รหัสข้อ' — ไม่งั้นข้อสอบจริงข้อใหม่จะแดงทั้งที่ถูก"""
    return not os.path.basename(filename).startswith(('chap-', 'gen-chap-'))


def walk(v):
    """เดินทุกสตริงในโครงสร้าง — ลง dict ด้วย ⇒ imageSpec ถูกตรวจ
    🔴 บั๊กเดิมอยู่ตรงนี้: v เป็น dict แล้วไม่ทำอะไรต่อ"""
    if isinstance(v, str):
        yield v
    elif isinstance(v, list):
        for x in v:
            yield from walk(x)
    elif isinstance(v, dict):
        for x in v.values():
            yield from walk(x)


def scan_question(q, filename):
    """คืนลิสต์ของ (ระดับ, สัญลักษณ์, ฟิลด์, จำนวน) ที่พบ — ระดับดิบ ยังไม่คิดเรื่อง diff"""
    found = []
    realexam = is_real_exam(filename)

    for field, val in q.items():
        if field in FIELDS_NEVER_TOUCH:
            continue
        strings = list(walk(val))
        if not strings:
            continue

        for sym in UNICODE_BANNED + MACRO_BANNED:
            n = sum(s.count(sym) for s in strings)
            if n:
                found.append(('BLOCK', sym, field, n))

        if not realexam:
            for sym in MACRO_REALEXAM_ONLY:
                n = sum(s.count(sym) for s in strings)
                if n:
                    found.append(('BLOCK', sym, field, n))

        for sym in TIERED:
            n = sum(s.count(sym) for s in strings)
            if not n:
                continue
            if field in STUDENT_NOW:
                found.append(('BLOCK', sym, field, n))
            elif field in STUDENT_LATER:
                found.append(('WARN', sym, field, n))
    return found


# ─────────────────────────────────────────────────────────────
# โหมด diff-scoped
# ─────────────────────────────────────────────────────────────
# ⚠️ ของเก่าไม่ได้ถูกโยนเข้ากอง WARN ตรง ๆ แม้พอร์ทัลจะเขียนไว้แบบนั้น
#    เพราะเส้นฐาน WARN = 444 ข้อ วัดจาก TIERED-ใน-explanation ล้วน ๆ
#    ถ้าเทของเก่า 45 ข้อลงไปปน ยอดจะเป็น ~489 > 444 ⇒ ratchet แดงทันที
#    ⇒ แยกเป็นชั้น LEGACY ของตัวเอง มี ratchet ของตัวเอง (block_questions_legacy)
#    ผลลัพธ์เชิงพฤติกรรมเหมือนที่ตกลงกัน: ไม่ทำให้ด่านแดง แต่ถูกนับและพิมพ์ทุกรอบ

def question_fingerprint(q):
    """ลายนิ้วมือของข้อ — ใช้เทียบว่า 'เปลี่ยนจริงไหม' ไม่ใช่แค่ไฟล์ถูกแตะ"""
    return json.dumps(q, sort_keys=True, ensure_ascii=False)


def diff_ids(old_data, new_data):
    """คืนเซตรหัสข้อที่ 'เพิ่มใหม่ หรือ แก้เนื้อใน' — ข้อที่ถูกลบไม่นับ (ไม่มีให้ตรวจแล้ว)
    old_data = None ⇒ ไฟล์ใหม่ทั้งไฟล์ ⇒ ทุกข้อนับว่าเปลี่ยน"""
    old = {}
    if old_data:
        for q in old_data.get('questions', []):
            old[q.get('id')] = question_fingerprint(q)
    ids = set()
    for q in (new_data or {}).get('questions', []):
        qid = q.get('id')
        if old.get(qid) != question_fingerprint(q):
            ids.add(qid)
    return ids


def git_out(args, cwd):
    """เรียก git แบบไม่ระเบิด — คืน None ถ้าไม่มี git / คำสั่งล้ม"""
    try:
        r = subprocess.run(['git'] + args, cwd=cwd, capture_output=True,
                           text=True, timeout=120)
    except Exception:
        return None
    return r.stdout if r.returncode == 0 else None


def repo_root(path):
    out = git_out(['rev-parse', '--show-toplevel'], path)
    return out.strip() if out else None


def collect_changed_ids(sets_dir, since_ref, changed_files, base_ref):
    """คืน (เซตรหัสข้อที่เปลี่ยน, คำอธิบายขอบเขต, รายการเตือน)"""
    warnings = []
    root = repo_root(sets_dir)
    if not root:
        return None, None, ['ไม่ได้อยู่ใน git repo — โหมด diff ใช้ไม่ได้']

    rel_sets = os.path.relpath(os.path.abspath(sets_dir), root)

    if since_ref:
        ref = since_ref
        out = git_out(['diff', '--name-only', ref, '--', rel_sets], root)
        if out is None:
            return None, None, [f'git diff --name-only {ref} ล้มเหลว (คอมมิตไม่มีจริง?)']
        files = [ln for ln in out.splitlines() if ln.strip().endswith('.json')]
        scope = f'--since {ref}'
    else:
        ref = base_ref
        files = []
        for f in changed_files:
            p = os.path.relpath(os.path.abspath(f), root)
            if p.endswith('.json'):
                files.append(p)
            else:
                warnings.append(f'ข้าม (ไม่ใช่ .json): {f}')
        scope = f'--changed {len(files)} ไฟล์ (เทียบกับ {ref})'

    ids = set()
    for relpath in files:
        newp = os.path.join(root, relpath)
        if not os.path.exists(newp):
            continue                       # ไฟล์ถูกลบทั้งไฟล์ — ไม่มีข้อให้ตรวจ
        with open(newp, encoding='utf-8') as f:
            new_data = json.load(f)
        blob = git_out(['show', f'{ref}:{relpath}'], root)
        if blob is None:
            old_data = None                # ไฟล์ใหม่ ⇒ ทุกข้อในไฟล์นับว่าเปลี่ยน
            warnings.append(f'ไฟล์ใหม่ (ไม่มีใน {ref}) ⇒ นับทุกข้อ: {relpath}')
        else:
            try:
                old_data = json.loads(blob)
            except json.JSONDecodeError:
                old_data = None
                warnings.append(f'อ่านฉบับเก่าไม่ได้ ⇒ นับทุกข้อ: {relpath}')
        ids |= diff_ids(old_data, new_data)
    return ids, scope, warnings


# ─────────────────────────────────────────────────────────────
# คำตัดสิน — แยกเป็นฟังก์ชันบริสุทธิ์เพื่อให้ canary ทดสอบได้
# ─────────────────────────────────────────────────────────────
def verdict(block_q, standing_q, warn_q, base, diff_mode):
    """คืน (แดงไหม, เหตุผล[])
    base = dict จาก warn-baseline.json หรือ None

    🔴 หลักสำคัญ: โหมดทั้งคลัง BLOCK **คือ** หนี้เก่า ไม่ใช่ของใหม่
       ถ้าปล่อยให้ 'มี BLOCK = แดง' ด่านจะแดงทุก push ตลอดกาล
       แล้วทุกคนจะเรียนรู้ที่จะกดข้ามด่าน — แย่กว่าไม่มีด่าน
       ⇒ โหมดทั้งคลังตัดสินด้วย ratchet เท่านั้น
       ⇒ 'ของใหม่ต้องเป็นศูนย์' บังคับในโหมด diff ซึ่งเป็นที่ที่ 'ใหม่' มีความหมาย"""
    red, why = False, []
    if base:
        if 'warn_questions' in base and warn_q > base['warn_questions']:
            red = True
            why.append(f"WARN โตขึ้น {warn_q - base['warn_questions']} ข้อ")
        if 'block_questions_legacy' in base and standing_q > base['block_questions_legacy']:
            red = True
            why.append(f"หนี้เก่า BLOCK โตขึ้น {standing_q - base['block_questions_legacy']} ข้อ")
    if diff_mode:
        if block_q:
            red = True
            why.append(f"มี BLOCK ใหม่ในของที่เปลี่ยนรอบนี้ {block_q} ข้อ")
    elif not base and block_q:
        # ไม่มีเส้นฐานให้เทียบ ⇒ กลับไปพฤติกรรมเดิม: มี BLOCK = แดง
        red = True
        why.append(f"มี BLOCK {block_q} ข้อ และไม่มีเส้นฐานให้เทียบ")
    return red, why


# ─────────────────────────────────────────────────────────────
# CANARY — ข้อพิสูจน์ว่าตัวตรวจ "มีของให้จับแล้วจับได้จริง"
# ─────────────────────────────────────────────────────────────
CANARIES = [
    # (ชื่อกับดัก, ข้อล่อ, สัญลักษณ์ที่ต้องจับได้)
    ("⊆ ซ่อนใน imageSpec.labels (บั๊กจริงที่พอร์ทัลจับได้ 31 ก.ค. 69)",
     {"id": "CANARY-1", "question": "สะอาด",
      "imageSpec": {"type": "venn-diagram", "labels": ["A ⊆ B"]}}, "⊆"),
    ("⊇ ซ่อนลึก 3 ชั้นใน imageSpec",
     {"id": "CANARY-2", "question": "สะอาด",
      "imageSpec": {"type": "venn", "sets": [{"note": {"txt": "X ⊇ Y"}}]}}, "⊇"),
    ("\\setminus ซ่อนใน imageSpec",
     {"id": "CANARY-3", "question": "สะอาด",
      "imageSpec": {"caption": r"$A \setminus B$"}}, r"\setminus"),
    ("∖ ยูนิโคดใน notes (ฟิลด์ที่เด็กไม่เห็นแต่ติดไปกับ bank.json)",
     {"id": "CANARY-4", "question": "สะอาด", "notes": "A∖B"}, "∖"),
    ("\\lfloor ในโจทย์ = ต้อง BLOCK",
     {"id": "CANARY-5", "question": r"หาค่า $\lfloor x \rfloor$"}, r"\lfloor"),
]

ANTI_CANARIES = [
    # ของที่ "ต้องไม่จับ" — กันตัวตรวจดุเกินจนคนปิดทิ้ง
    ("⊂ ที่หลักสูตรไทยใช้จริง",
     {"id": "OK-1", "question": "$A \\subset B$ และ A ⊂ B"}),
    ("⊄ คู่ของ ⊂",
     {"id": "OK-2", "imageSpec": {"labels": ["A ⊄ B"]}}),
    ("accept ที่มียูนิโคด ⛔ ห้ามแตะ",
     {"id": "OK-3", "accept": ["เซตว่าง", "∅", "X = ∅"]}),
    ("\\lfloor ในเฉลย = WARN ไม่ใช่ BLOCK",
     {"id": "OK-4", "explanation": r"ได้ $\lfloor 7/2 \rfloor = 3$"}),
]

# ข้อล่อสำหรับโหมด diff — เนื้อเดียวกันเป๊ะ ต่างกันแค่ "อยู่ใน diff ไหม"
_DIRTY = {"id": "DIFF-BAIT", "question": "สะอาด",
          "imageSpec": {"labels": ["A ⊆ B"]}}

# ชุดข้อมูลจำลองสำหรับทดสอบตัวหาข้อที่เปลี่ยน
_OLD_SET = {"questions": [
    {"id": "Q-SAME", "question": "เหมือนเดิมทุกตัวอักษร"},
    {"id": "Q-EDIT", "question": "ก่อนแก้"},
    {"id": "Q-GONE", "question": "ข้อนี้จะถูกลบ"},
]}
_NEW_SET = {"questions": [
    {"id": "Q-SAME", "question": "เหมือนเดิมทุกตัวอักษร"},
    {"id": "Q-EDIT", "question": "หลังแก้"},
    {"id": "Q-NEW", "question": "ข้อใหม่"},
]}


def classify(raw_hits, qid, changed_ids):
    """แปลงระดับดิบเป็นระดับสุดท้าย
    changed_ids = None ⇒ โหมดทั้งคลัง (BLOCK คือ BLOCK)
    changed_ids = เซต   ⇒ โหมด diff: BLOCK ที่ id ไม่อยู่ในเซต ลดชั้นเป็น LEGACY"""
    out = []
    for level, sym, field, n in raw_hits:
        if level == 'BLOCK' and changed_ids is not None and qid not in changed_ids:
            out.append(('LEGACY', sym, field, n))
        else:
            out.append((level, sym, field, n))
    return out


def _levels(q, changed_ids):
    raw = scan_question(q, 'gen-chap-99-canary.json')
    return set(h[0] for h in classify(raw, q.get('id'), changed_ids))


def run_canary():
    ok = True
    print("─" * 62)
    print(f"CANARY SELF-TEST v{SCANNER_VERSION} — ข้อพิสูจน์ว่ามีของให้จับแล้วจับได้")
    print("─" * 62)
    for name, q, sym in CANARIES:
        hits = scan_question(q, 'gen-chap-99-canary.json')
        caught = any(h[1] == sym for h in hits)
        print(f"  {'✅' if caught else '🔴 จับไม่ได้'}  {name}")
        if not caught:
            ok = False
    for name, q in ANTI_CANARIES:
        hits = [h for h in scan_question(q, 'gen-chap-99-canary.json') if h[0] == 'BLOCK']
        clean = not hits
        print(f"  {'✅' if clean else '🔴 จับเกิน: ' + str(hits)}  (ต้องไม่จับ) {name}")
        if not clean:
            ok = False

    # ── ด่านของโหมด diff เอง ──────────────────────────────────
    # ⚠️ ความเสี่ยงของโหมดนี้คือ "ไม่จับอะไรเลย" ซึ่งหน้าตาเหมือน "สะอาด"
    print("  ── โหมด diff ──")
    diff_checks = [
        ("ข้อสกปรกที่ 'อยู่ใน diff' ⇒ ต้อง BLOCK",
         'BLOCK' in _levels(_DIRTY, {'DIFF-BAIT'})),
        ("ข้อสกปรกที่ 'อยู่ในคลังแต่ไม่อยู่ใน diff' ⇒ ต้องไม่ BLOCK",
         'BLOCK' not in _levels(_DIRTY, {'ข้ออื่น'})),
        ("…แต่ต้องไม่หายเงียบ — ต้องโผล่เป็น LEGACY",
         'LEGACY' in _levels(_DIRTY, {'ข้ออื่น'})),
        ("โหมดทั้งคลัง (ไม่มี diff) ข้อเดียวกันต้องกลับเป็น BLOCK",
         'BLOCK' in _levels(_DIRTY, None)),
        ("ตัวหาข้อที่เปลี่ยนต้องได้ {Q-EDIT, Q-NEW} เป๊ะ",
         diff_ids(_OLD_SET, _NEW_SET) == {'Q-EDIT', 'Q-NEW'}),
        ("(ต้องไม่จับ) ข้อที่ไม่ได้แตะเลยต้องไม่อยู่ในผลลัพธ์",
         'Q-SAME' not in diff_ids(_OLD_SET, _NEW_SET)),
        ("(ต้องไม่จับ) ข้อที่ถูกลบต้องไม่อยู่ในผลลัพธ์",
         'Q-GONE' not in diff_ids(_OLD_SET, _NEW_SET)),
        ("ไฟล์ใหม่ทั้งไฟล์ ⇒ ทุกข้อนับว่าเปลี่ยน",
         diff_ids(None, _NEW_SET) == {'Q-SAME', 'Q-EDIT', 'Q-NEW'}),
    ]
    B = {'warn_questions': 444, 'block_questions_legacy': 45}
    diff_checks += [
        ("── คำตัดสิน ── ทั้งคลัง หนี้เก่าเท่าเดิม ⇒ ต้องผ่าน (ไม่ใช่แดงตลอดกาล)",
         verdict(45, 45, 444, B, False)[0] is False),
        ("ทั้งคลัง หนี้เก่าโตเป็น 46 ⇒ ต้องแดง",
         verdict(46, 46, 444, B, False)[0] is True),
        ("ทั้งคลัง WARN โตเป็น 445 ⇒ ต้องแดง",
         verdict(45, 45, 445, B, False)[0] is True),
        ("โหมด diff ไม่มีของใหม่ หนี้เก่าเท่าเดิม ⇒ ต้องผ่าน",
         verdict(0, 45, 444, B, True)[0] is False),
        ("โหมด diff มีของใหม่ 1 ข้อ ⇒ ต้องแดง แม้ ratchet จะผ่าน",
         verdict(1, 45, 444, B, True)[0] is True),
        ("ทั้งคลัง ไม่มีเส้นฐาน ⇒ มี BLOCK = แดง (พฤติกรรมเดิม)",
         verdict(45, 45, 444, None, False)[0] is True),
    ]
    for name, passed in diff_checks:
        print(f"  {'✅' if passed else '🔴 ล้ม'}  {name}")
        if not passed:
            ok = False
    print()
    return ok


# ─────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(
        description=f'scan_symbols.py v{SCANNER_VERSION} ({SCANNER_DATE})')
    ap.add_argument('sets_dir', nargs='?', default='data/sets')
    ap.add_argument('--baseline', help='ไฟล์เส้นฐาน ratchet (WARN + LEGACY)')
    ap.add_argument('--write-baseline', action='store_true')
    ap.add_argument('--since', metavar='REF',
                    help='โหมด diff: ตรวจเฉพาะข้อที่เปลี่ยนตั้งแต่คอมมิต REF')
    ap.add_argument('--changed', nargs='+', metavar='FILE',
                    help='โหมด diff: ระบุไฟล์ชุดที่เปลี่ยนเอง (เช่นจาก git diff --name-only)')
    ap.add_argument('--base', metavar='REF', default='HEAD',
                    help='ฉบับเก่าที่ใช้เทียบในโหมด --changed (ปริยาย HEAD)')
    ap.add_argument('--changed-ids', metavar='ID,ID,…',
                    help='โหมด diff แบบไม่ต้องมี git: ระบุรหัสข้อที่เปลี่ยนเอง')
    ap.add_argument('--version', action='store_true')
    args = ap.parse_args()

    if args.version:
        print(SCANNER_VERSION)
        return

    print(f"scan_symbols.py v{SCANNER_VERSION} ({SCANNER_DATE})")

    # ⛔ ด่านแรก — canary ต้องผ่านก่อน ไม่งั้นผลของจริงเชื่อไม่ได้
    if not run_canary():
        print("🔴 CANARY ล้มเหลว — ตัวตรวจมองไม่เห็นของที่ต้องเห็น")
        print("   ผลสแกนของจริงเชื่อไม่ได้ ⇒ ด่านแดง (ไม่ใช่ 'ผ่านเพราะไม่เจออะไร')")
        sys.exit(2)

    # ── ตัดสินขอบเขต BLOCK ────────────────────────────────────
    changed_ids, scope = None, 'ทั้งคลัง'
    n_modes = sum(bool(x) for x in (args.since, args.changed, args.changed_ids))
    if n_modes > 1:
        print("🔴 เลือกโหมด diff ได้ทีละแบบเท่านั้น (--since / --changed / --changed-ids)")
        sys.exit(2)
    if args.changed_ids:
        changed_ids = set(x.strip() for x in args.changed_ids.split(',') if x.strip())
        scope = f'--changed-ids {len(changed_ids)} ข้อ'
    elif args.since or args.changed:
        changed_ids, scope, warn_msgs = collect_changed_ids(
            args.sets_dir, args.since, args.changed or [], args.base)
        for m in warn_msgs:
            print(f"  ⚠️ {m}")
        if changed_ids is None:
            # ⛔ ไม่เดา — ถ้าหาขอบเขต diff ไม่ได้ ห้ามเงียบแล้วผ่าน
            print("🔴 กำหนดขอบเขต diff ไม่ได้ ⇒ ด่านแดง (ห้ามตีความว่า 'ไม่มีอะไรเปลี่ยน')")
            sys.exit(2)
        print(f"  ขอบเขต diff: {scope} ⇒ {len(changed_ids)} ข้อที่เปลี่ยนจริง")

    blocks, warns, legacy = [], [], []
    nq = 0
    for fn in sorted(os.listdir(args.sets_dir)):
        if not fn.endswith('.json'):
            continue
        path = os.path.join(args.sets_dir, fn)
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        for q in data.get('questions', []):
            nq += 1
            qid = q.get('id')
            raw = scan_question(q, fn)
            for level, sym, field, n in classify(raw, qid, changed_ids):
                rec = (fn, qid, sym, field, n)
                {'BLOCK': blocks, 'WARN': warns, 'LEGACY': legacy}[level].append(rec)

    def nqs(recs):
        return len(set(r[1] for r in recs))

    print("─" * 62)
    print(f"สแกน {nq:,} ข้อ · walker ลง imageSpec แล้ว · ขอบเขต BLOCK = {scope}")
    print("─" * 62)
    tag = "ของใหม่ในรอบนี้ — ต้องเป็น 0" if changed_ids is not None else "ทั้งคลัง = หนี้เก่า"
    print(f"  BLOCK  : {len(blocks)} จุด / {nqs(blocks)} ข้อ   ({tag})")
    print(f"  LEGACY : {len(legacy)} จุด / {nqs(legacy)} ข้อ   (หนี้เก่าที่ยังค้าง — ห้ามโต)")
    print(f"  WARN   : {len(warns)} จุด / {nqs(warns)} ข้อ")

    for r in blocks[:40]:
        print(f"    🔴 {r[1]:28} {r[2]:14} ใน `{r[3]}` ×{r[4]}")
    if len(blocks) > 40:
        print(f"    … อีก {len(blocks)-40} จุด")

    warn_q, legacy_q, block_q = nqs(warns), nqs(legacy), nqs(blocks)
    # ในโหมดทั้งคลัง ไม่มีชั้น LEGACY แยก — หนี้เก่าคือ BLOCK ทั้งก้อน
    standing = legacy_q if changed_ids is not None else block_q

    if args.write_baseline and args.baseline:
        # เก็บคีย์อธิบาย (_comment/_method/…) ของเดิมไว้ — ไม่ล้างคำอธิบายทิ้ง
        out = {}
        if os.path.exists(args.baseline):
            out = json.load(open(args.baseline, encoding='utf-8'))
        out.update({'warn_questions': warn_q,
                    'warn_occurrences': len(warns),
                    'block_questions_legacy': standing})
        with open(args.baseline, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f"\n  เขียนเส้นฐานแล้ว: WARN {warn_q} ข้อ · LEGACY {standing} ข้อ")
        sys.exit(0)

    diff_mode = changed_ids is not None
    base = None
    if args.baseline and os.path.exists(args.baseline):
        base = json.load(open(args.baseline, encoding='utf-8'))
        for label, cur, key in (('WARN  ', warn_q, 'warn_questions'),
                                ('หนี้เก่า', standing, 'block_questions_legacy')):
            if key not in base:
                continue
            b = base[key]
            print(f"\n  RATCHET {label}: เส้นฐาน {b} → ปัจจุบัน {cur}", end=' ')
            print("🔴 โตขึ้น %d ข้อ" % (cur - b) if cur > b else
                  ("✅ ลดลง %d ข้อ" % (b - cur) if cur < b else "✅ เท่าเดิม"))

    # 📌 พิมพ์ยอดหนี้เก่าทุกรอบ ไม่ให้ลืม (ข้อเรียกร้องของพอร์ทัล)
    print(f"\n  📌 ยอด BLOCK เก่าที่ยังค้างทั้งคลัง: {standing} ข้อ — ยังไม่ได้แก้ ไม่ใช่ไม่มี")

    red, why = verdict(block_q, standing, warn_q, base, diff_mode)
    for w in why:
        print(f"  🔴 {w}")
    print(f"\n  ⇒ {'🔴 ไม่ผ่าน' if red else '✅ ผ่าน'}")
    sys.exit(1 if red else 0)


if __name__ == '__main__':
    main()

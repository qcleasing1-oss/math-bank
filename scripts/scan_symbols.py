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

เวอร์ชัน 2.2 (ตามที่ทีมพอร์ทัลขอ 31 ก.ค. 2569 — ข้อเดียวของรอบ) แก้อีกอย่างเดียว:
  7. เส้นฐานที่ "ขาดคีย์ที่ต้องใช้ / อ่านไม่ได้ / ไม่ใช่ dict / ค่าไม่ใช่ int"
     ⇒ exit 2 = ตัวตรวจใช้ไม่ได้ (ของเดิมข้ามเงียบ ๆ แล้วรายงานว่าผ่าน)
     เหตุ: sync สคริปต์กับเส้นฐานไม่ครบคู่ = เคสที่เกิดง่ายที่สุดในทางปฏิบัติ
     ⇒ กลไกนี้บังคับกฎ "sync เป็นคู่เสมอ" โดยไม่ต้องพึ่งวินัยคน

เวอร์ชัน 2.3 (ตามที่ทีมพอร์ทัลขอ 31 ก.ค. 2569) แก้อีกสองอย่าง:
  8. ทิศทางของรุ่นเป็น "ไม่สมมาตร" — เทียบเชิงตัวเลข ไม่ใช่ !=
     เส้นฐาน "ใหม่กว่า" สคริปต์ ⇒ exit 2 (สคริปต์ไม่รู้จักคีย์ที่รุ่นหลังเพิ่ม
     ⇒ อาจไม่ได้ตรวจชั้นนั้นเลยแล้วรายงานว่าผ่าน)
     เส้นฐาน "เก่ากว่า" ⇒ เตือนเฉย ๆ (สคริปต์รู้เองว่าต้องใช้คีย์อะไร ขาดจริงก็แดงอยู่แล้ว)
     ประทับที่อ่านเป็นเลขรุ่นไม่ได้ ⇒ exit 2 เพราะ "เทียบไม่ได้" ไม่เท่ากับ "เทียบแล้วผ่าน"
  9. --write-baseline ปฏิเสธการเขียนทับเมื่อยอดค้างโต (exit 2)
     ต้องประกาศเจตนาด้วย --accept-debt-increase '<เหตุผล>' และเหตุผลถูกเขียนลงเส้นฐาน
     เหตุ: คนที่จะละเมิดกฎนี้คือคนที่กำลังรีบและด่านกำลังแดง — คนที่จะอ่านจดหมายเก่าน้อยที่สุด
     ⇒ กติกาที่อยู่ในไฟล์จะยังอยู่ ตอนที่ทุกคนจำไม่ได้แล้ว
     (ซ่อมเส้นฐานที่พัง และยอดที่ลดลง ยังเขียนได้ตามปกติโดยไม่ต้องใช้ธง)

รหัสออก:
    0 = ผ่าน
    1 = ด่านแดงจากเนื้อหา (BLOCK ใหม่ / WARN โต / LEGACY โต)
    2 = ด่านแดงจากตัวตรวจเอง — ผลสแกนเชื่อไม่ได้
        (canary ล้ม · ขอบเขต diff ระบุไม่ได้ · สองโหมดพร้อมกัน · เส้นฐานใช้ไม่ได้
         · เส้นฐานใหม่กว่าสคริปต์ · สั่งเขียนเส้นฐานตอนยอดโตโดยไม่ประกาศเจตนา)

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
import datetime as _dt

SCANNER_VERSION = '2.4'
SCANNER_DATE = '2026-08-01'

# คีย์ที่สคริปต์รุ่นนี้ "ใช้ตัดสินจริง" — ขาดข้อใดข้อหนึ่ง = ตัวตรวจใช้ไม่ได้ (exit 2)
# 🔴 ไม่ใช่ 'ข้ามไปเงียบ ๆ' เพราะ "ไม่ได้ตรวจ" กับ "ตรวจแล้วสะอาด" ต้องไม่ให้ผลเหมือนกัน
#    (ข้อเรียกร้องพอร์ทัลรอบ 9 · รูปแบบเดียวกับกฎ B8 ข้อ 1)
#    เคสจริงที่กลัว: sync scan_symbols.py ไปไฟล์เดียว ลืม warn-baseline.json
# หมายเหตุ: warn_occurrences ไม่อยู่ในรายการนี้ เพราะสคริปต์ไม่ได้ใช้ตัดสิน (ไว้ดูแนวโน้มเท่านั้น)
REQUIRED_BASELINE_KEYS = ('warn_questions', 'block_questions_legacy')

# สภาพของเส้นฐาน "เดิม" ตอนจะเขียนทับ มี 3 แบบ ไม่ใช่ 2 — และต่างกันมาก
#   None       = ยังไม่เคยมีไฟล์เลย  ⇒ การตั้งต้นครั้งแรก ไม่มีอะไรให้ฟอก
#   UNREADABLE = มีไฟล์ แต่อ่านไม่ได้/ไม่ใช่ dict ⇒ เคยมีเลขอยู่ แล้วเลขนั้นหายไป
#   dict       = อ่านได้ (แต่คีย์ข้างในอาจยังพังเป็นราย ๆ)
UNREADABLE = object()

# "ฉบับก่อนหน้าของข้อนี้อ่านไม่ได้" — ต่างจาก "ฉบับก่อนหน้าสะอาด" คนละเรื่องกัน
# 🔴 ใช้กับชั้นแยกหนี้ ทำเกิด/ไปปลุก: เทียบไม่ได้ ⇒ ต้องพิมพ์ว่าระบุไม่ได้ ⛔ ห้ามพิมพ์ 0
UNKNOWN_PREV = object()


def parse_version(s):
    """แปลง '2.3' → (2, 3) เพื่อเทียบ "ทิศทาง" ของรุ่นเชิงตัวเลข — คืน None ถ้าอ่านไม่ได้

    ⚠️ ห้ามเทียบเป็นสตริง: ตามลำดับพจนานุกรม '2.10' < '2.9' ซึ่งกลับทิศกับความจริง
       (พอร์ทัลรอบ 10 ระบุชัดว่า "เทียบแบบตัวเลข ไม่ใช่ !=")
    """
    if not isinstance(s, str):
        return None
    parts = s.strip().split('.')
    if not parts or not all(p.isdigit() for p in parts):
        return None
    return tuple(int(p) for p in parts)

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

# ✅ โทเคนที่ยกเว้นจากชั้น TIERED "แบบเป๊ะทั้งตัว" (มติครู 1 ส.ค. 69)
#    \operatorname{Im} · \operatorname{Re} = สัญกรณ์มาตรฐานของจำนวนเชิงซ้อน
#    ที่ข้อสอบจริงใช้อยู่แล้ว ⇒ ถ้าไม่ยกเว้น ข้อพวกนี้จะแดงทุกครั้งที่ใครไปแตะ
#    = หนี้ที่ล้างไม่ได้ตลอดกาล แล้วสุดท้ายคนจะเรียนรู้ที่จะกดข้ามด่าน
#
# ⛔ ห้ามยกเว้น \operatorname ทั้งแมโครเด็ดขาด
#    ทั้งคลังมี \operatorname ในขอบเขต BLOCK 21 ข้อ · เป็น Im/Re เพียง 2 ชื่อ
#    ถ้ายกเว้นทั้งตัว อีก 19 ข้อ (cis, sgn, adj, proj, …) จะหลุดไปเงียบ ๆ
#    ⇒ ยกเว้น "สตริงเต็มโทเคนรวมวงเล็บปิด" เท่านั้น
#       ⇒ \operatorname{Imaginary} ไม่เข้าเงื่อนไข เพราะ } ไม่ได้อยู่หลัง Im
MACRO_EXEMPT_EXACT = [r'\operatorname{Im}', r'\operatorname{Re}']


def mask_exempt(s):
    """กลบโทเคนที่ยกเว้นด้วยตัวเติมความยาวเท่าเดิมที่ไม่มี \\ และไม่มี { }

    ทำไมต้องกลบแทนที่จะลบ: ความยาวเท่าเดิม ⇒ ไม่มีสตริงสองข้างมาต่อกัน
    จนเกิดโทเคนใหม่โดยบังเอิญ
    ⚠️ ใช้เฉพาะในลูป TIERED เท่านั้น — ⛔ ห้ามใช้กับ UNICODE_BANNED/MACRO_BANNED
       (ของต้องห้ามยังต้องถูกจับแม้จะอยู่ในสตริงเดียวกับ Im/Re)
    """
    for tok in MACRO_EXEMPT_EXACT:
        if tok in s:
            s = s.replace(tok, 'x' * len(tok))
    return s

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

        # 🔴 กลบไวต์ลิสต์ "ก่อนนับชั้น TIERED เท่านั้น"
        #    ของต้องห้ามข้างบนนับจาก strings ตัวจริงไปแล้ว ⇒ ไม่มีทางหลุดตามไปด้วย
        masked = [mask_exempt(s) for s in strings]
        for sym in TIERED:
            n = sum(s.count(sym) for s in masked)
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


def split_debt(new_hits, old_hits):
    """แยกหนี้ BLOCK ของ "ข้อหนึ่งข้อ" ออกเป็นสองถัง — คืน (ทำเกิด[], ไปปลุก[])

    ทั้งสองถังเป็นลิสต์ของ (สัญลักษณ์, ฟิลด์, จำนวนจุด)

    🔴 เหตุผลที่ต้องแยก (พอร์ทัลรอบ 13 ข้อ 5):
       "ปัญหาไม่ใช่ 'แดง' ปัญหาคือ 'แดงแล้วไม่รู้ว่าแดงเพราะใคร'"
       ขอบเขตยังเป็นรายข้อเหมือนเดิม (ไม่ลงไปเป็นรายฟิลด์ เพราะรายฟิลด์
       เปิดทางให้แก้ข้อที่มีหนี้โดยไม่เคยเห็นหนี้) — เปลี่ยนแค่ "ถ้อยคำที่รายงาน"

    ⚠️ ชั้นนี้ ⛔ ไม่ทำให้ด่านอ่อนลง: ข้อที่มีแต่หนี้ "ไปปลุก" ก็ยังแดงเหมือนเดิม
       (แตะแล้วต้องล้าง) — verdict() ไม่ถูกแก้เลยด้วยเหตุผลนี้

    old_hits = None ⇒ ฉบับก่อนหน้าไม่มีข้อนี้ ⇒ ทุกจุดคือ "ทำเกิด"
               (เหมือนกับกรณีฉบับเก่ามีข้อนี้แต่สะอาด — ซึ่งถูกต้อง)
    ⛔ "ฉบับก่อนหน้าอ่านไม่ได้" ห้ามส่งเข้ามาที่นี่ — ผู้เรียกต้องกันไว้เป็น UNKNOWN_PREV
    """
    old = {}
    if old_hits:
        for level, sym, field, cnt in old_hits:
            if level == 'BLOCK':
                old[(sym, field)] = old.get((sym, field), 0) + cnt
    made, woke = [], []
    for level, sym, field, cnt in (new_hits or []):
        if level != 'BLOCK':
            continue
        k = (sym, field)
        was = old.get(k, 0)
        keep = min(cnt, was)
        old[k] = was - keep            # กันนับซ้ำเมื่อคีย์เดียวกันโผล่หลายรายการ
        if keep:
            woke.append((sym, field, keep))
        if cnt - keep:
            made.append((sym, field, cnt - keep))
    return made, woke


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
    """คืน (เซตรหัสข้อที่เปลี่ยน, คำอธิบายขอบเขต, รายการเตือน, รอยเดิมรายข้อ)

    รอยเดิมรายข้อ = dict rหัสข้อ → ผลของ scan_question บน "ฉบับก่อนหน้า"
      · ไม่มีคีย์      ⇒ ฉบับก่อนหน้าไม่มีข้อนี้ (ข้อใหม่/ไฟล์ใหม่) ⇒ ทุกจุดคือของใหม่
      · UNKNOWN_PREV  ⇒ ฉบับก่อนหน้าอ่านไม่ได้ ⇒ ⛔ ระบุไม่ได้ ห้ามนับเป็นศูนย์
    """
    warnings = []
    root = repo_root(sets_dir)
    if not root:
        return None, None, ['ไม่ได้อยู่ใน git repo — โหมด diff ใช้ไม่ได้'], None

    rel_sets = os.path.relpath(os.path.abspath(sets_dir), root)

    if since_ref:
        ref = since_ref
        out = git_out(['diff', '--name-only', ref, '--', rel_sets], root)
        if out is None:
            return None, None, [f'git diff --name-only {ref} ล้มเหลว (คอมมิตไม่มีจริง?)'], None
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

    ids, prev = set(), {}
    for relpath in files:
        newp = os.path.join(root, relpath)
        if not os.path.exists(newp):
            continue                       # ไฟล์ถูกลบทั้งไฟล์ — ไม่มีข้อให้ตรวจ
        with open(newp, encoding='utf-8') as f:
            new_data = json.load(f)
        base_fn = os.path.basename(relpath)   # ⚠️ ต้องเป็นชื่อไฟล์ล้วน
        #                                        ไม่งั้น is_real_exam() อ่านผิดเพราะมี data/sets/ นำหน้า
        blob = git_out(['show', f'{ref}:{relpath}'], root)
        unreadable = False
        if blob is None:
            old_data = None                # ไฟล์ใหม่ ⇒ ทุกข้อในไฟล์นับว่าเปลี่ยน
            warnings.append(f'ไฟล์ใหม่ (ไม่มีใน {ref}) ⇒ นับทุกข้อ: {relpath}')
        else:
            try:
                old_data = json.loads(blob)
            except json.JSONDecodeError:
                old_data = None
                unreadable = True
                warnings.append(f'อ่านฉบับเก่าไม่ได้ ⇒ นับทุกข้อ: {relpath}')
        # 🔴 เก็บ "รอยเดิม" ไว้ตอนที่ยังถือ blob อยู่ในมือ — ใช้แยก ทำเกิด/ไปปลุก
        if unreadable:
            for q in new_data.get('questions', []):
                prev[q.get('id')] = UNKNOWN_PREV
        elif old_data:
            for q in old_data.get('questions', []):
                prev[q.get('id')] = scan_question(q, base_fn)
        ids |= diff_ids(old_data, new_data)
    return ids, scope, warnings, prev


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


def check_baseline(base, path='<เส้นฐาน>'):
    """ตรวจว่าเส้นฐาน "ใช้ตัดสินได้จริง" ไหม — คืน (ใช้ได้ไหม, เหตุผลตาย[], ข้อสังเกต[])

    🔴 หลักสำคัญ (พอร์ทัลรอบ 9): ห้ามคืน 'ผ่าน' เพียงเพราะ *ไม่มีคีย์ให้เทียบ*
       ของเดิมเขียน `if key not in base: continue` ⇒ เส้นฐานที่ขาดคีย์จะ
       'ไม่พัง แต่ก็ไม่ตรวจ' แล้วรายงานว่าผ่าน — หน้าตาเหมือนตรวจแล้วสะอาดเป๊ะ
    base = None ⇒ ผู้ใช้ไม่ได้ระบุ --baseline เลย = คนละกรณี ไม่ใช่เส้นฐานพัง"""
    if base is None:
        return True, [], []
    if not isinstance(base, dict):
        return False, [f"{path} ไม่ใช่วัตถุ JSON (พบชนิด {type(base).__name__})"], []

    notes = []
    # ── ทิศทางของรุ่น "ไม่สมมาตร" (พอร์ทัลรอบ 10 ข้อ 2) ──────────────────
    #   สคริปต์ใหม่ + เส้นฐานเก่า = ปลอดภัย — สคริปต์รู้เองว่าต้องใช้คีย์อะไร
    #                                 ถ้าขาดจริงจะแดงที่ด่านคีย์อยู่แล้ว ⇒ เตือนพอ
    #   สคริปต์เก่า + เส้นฐานใหม่ = อันตราย — สคริปต์ไม่รู้จักคีย์ที่รุ่นหลังเพิ่มมา
    #                                 ⇒ อาจ "ไม่ได้ตรวจชั้นนั้น" เงียบ ๆ แล้วรายงานว่าผ่าน
    stamp = base.get('_scannerVersion')
    mine = parse_version(SCANNER_VERSION)
    if stamp is None:
        # ไม่มีประทับ = เส้นฐานรุ่นก่อนที่จะเริ่มประทับ ⇒ เป็น "เก่ากว่า" เสมอ
        # (ทุกรุ่นตั้งแต่ 2.1 เขียนประทับให้อัตโนมัติ ⇒ ของใหม่จะมีประทับแน่นอน)
        notes.append("⚠️ เส้นฐานไม่มีประทับ _scannerVersion — ถือว่าเก่ากว่าสคริปต์"
                     " · ควร sync ใหม่ให้เป็นคู่ (ยังไม่ทำให้แดง)")
    else:
        theirs = parse_version(stamp)
        if theirs is None:
            # 🔴 "เทียบไม่ได้" ≠ "เทียบแล้วไม่เจอปัญหา" — กับดักข้อ 6
            #    ถ้าปล่อยเป็นแค่คำเตือน = เราไม่ได้ตรวจทิศทางเลย แต่รายงานเหมือนตรวจแล้ว
            return False, [
                f"{path} ประทับ _scannerVersion = {stamp!r} อ่านเป็นเลขรุ่นไม่ได้",
                "⇒ ตัดสินไม่ได้ว่าเส้นฐานใหม่กว่าสคริปต์หรือไม่ ⇒ ไม่ถือว่าผ่าน",
            ], notes
        if theirs > mine:
            return False, [
                f"{path} ประทับ v{stamp} · สคริปต์เป็น v{SCANNER_VERSION}",
                "เส้นฐานรุ่นใหม่กว่าสคริปต์ — สคริปต์รุ่นนี้อาจไม่รู้จักคีย์ที่เพิ่มมา"
                " ⇒ อัปเดตสคริปต์ก่อน",
            ], notes
        if theirs < mine:
            notes.append(f"⚠️ เส้นฐานประทับ v{stamp} เก่ากว่าสคริปต์ v{SCANNER_VERSION}"
                         " — ควร sync ใหม่ให้เป็นคู่ (ยังไม่ทำให้แดง)")

    missing = [k for k in REQUIRED_BASELINE_KEYS if k not in base]
    if missing:
        return False, [
            f"{path} ขาดคีย์ที่ v{SCANNER_VERSION} ต้องใช้: {', '.join(missing)}",
            "⇒ sync scan_symbols.py กับ warn-baseline.json ใหม่ให้เป็น 'คู่เดียวกัน' — ห้าม sync ไฟล์เดียว",
        ], notes

    # ⚠️ กับดักชนิดข้อมูล: bool เป็นลูกของ int ใน Python ⇒ 444 > True ไม่ error
    #    ถ้าไม่กันไว้ เส้นฐานที่เพี้ยนเป็น true/false จะ 'เทียบผ่าน' อย่างเงียบ ๆ
    bad = [k for k in REQUIRED_BASELINE_KEYS
           if isinstance(base[k], bool) or not isinstance(base[k], int)]
    if bad:
        return False, [
            f"{path} คีย์ {', '.join(bad)} ไม่ใช่จำนวนเต็ม ⇒ เทียบ ratchet ไม่ได้",
        ], notes
    return True, [], notes


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
    # ── ด่านคุมไวต์ลิสต์ Im/Re (มติครู 1 ส.ค. 69) ─────────────────
    #    ทั้งสามข้อนี้คือข้อพิสูจน์ว่า "ยกเว้นเฉพาะโทเคน" ไม่ใช่ "ยกเว้นทั้งแมโคร"
    (r"\operatorname{cis} ในโจทย์ = ยังต้อง BLOCK (⛔ ห้ามยกเว้น \operatorname ทั้งตัว)",
     {"id": "CANARY-6", "question": r"เขียน $\operatorname{cis}\theta$ ในรูป…"},
     r"\operatorname"),
    (r"\operatorname{Imaginary} = ต้องไม่หลุดเพราะ 'ขึ้นต้นเหมือน Im'",
     {"id": "CANARY-7", "question": r"$\operatorname{Imaginary}(z)$"}, r"\operatorname"),
    (r"\operatorname{Im} ปนกับ ⊆ ในสตริงเดียวกัน ⇒ ⊆ ต้องยังถูกจับ",
     {"id": "CANARY-8", "question": r"$\operatorname{Im}(z)$ และ $A ⊆ B$"}, "⊆"),
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
    (r"\operatorname{Im} ในโจทย์ = สัญกรณ์มาตรฐานจำนวนเชิงซ้อน (มติครู 1 ส.ค. 69)",
     {"id": "OK-5", "question": r"หาค่า $\operatorname{Im}(z)$ เมื่อ $z = 3+4i$"}),
    (r"\operatorname{Re} ในโจทย์",
     {"id": "OK-6", "choices": [r"$\operatorname{Re}(z) = 3$"]}),
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


# ─────────────────────────────────────────────────────────────
# ด่านของ "ชั้นถ้อยคำใหม่" เอง — พอร์ทัลรอบ 13 ข้อ 5
#   "ถ้อยคำชั้นใหม่ต้องมีด่านคุม ⇒ ใส่บั๊กที่สลับสองถัง แล้วนับด่านที่ล้ม ต้อง > 0"
#   ⚠️ เคสที่ "สมมาตร" (ทำเกิด 0 · ไปปลุก 0) จับการสลับถังไม่ได้เลย
#      ⇒ ต้องมีเคสอสมมาตรอย่างน้อยหนึ่ง ไม่งั้นฮาร์เนสนี้เป็นแค่พิธีกรรม
# ─────────────────────────────────────────────────────────────
_B = 'BLOCK'
SPLIT_CASES = [
    ("ฉบับเก่าสะอาด → รอบนี้มี 1 จุด ⇒ ทำเกิด 1 · ไปปลุก 0  (เคสอสมมาตร)",
     [(_B, '⊆', 'question', 1)], [], [('⊆', 'question', 1)], []),
    ("ฉบับเก่าไม่มีข้อนี้เลย (old=None) ⇒ ทุกจุดคือทำเกิด",
     [(_B, '⊆', 'question', 2)], None, [('⊆', 'question', 2)], []),
    ("เก่า 1 · ใหม่ 1 จุดเดียวกัน ⇒ ทำเกิด 0 · ไปปลุก 1",
     [(_B, '⊆', 'question', 1)], [(_B, '⊆', 'question', 1)],
     [], [('⊆', 'question', 1)]),
    ("เก่า 1 · ใหม่ 3 ⇒ ทำเกิด 2 · ไปปลุก 1  (เฉพาะส่วนเกินที่เป็นของใหม่)",
     [(_B, '⊆', 'question', 3)], [(_B, '⊆', 'question', 1)],
     [('⊆', 'question', 2)], [('⊆', 'question', 1)]),
    ("เก่า 2 · ใหม่เหลือ 1 ⇒ ทำเกิด 0 · ไปปลุก 1  (หนี้ลดลงไม่ใช่ของใหม่)",
     [(_B, '⊆', 'question', 1)], [(_B, '⊆', 'question', 2)],
     [], [('⊆', 'question', 1)]),
    ("ย้ายหนี้ข้ามฟิลด์ question → choices ⇒ นับเป็นทำเกิด (ถังผูกกับฟิลด์ด้วย)",
     [(_B, '⊆', 'choices', 1)], [(_B, '⊆', 'question', 1)],
     [('⊆', 'choices', 1)], []),
    ("WARN ไม่เข้าถังไหนเลย — สองถังนี้เป็นเรื่องของ BLOCK เท่านั้น",
     [('WARN', r'\lfloor', 'explanation', 3)], [], [], []),
]


def _mut_swap(new_hits, old_hits):
    """บั๊กจำลอง ① สลับสองถัง — ของใหม่ถูกรายงานว่าเป็นหนี้เก่า"""
    m, w = split_debt(new_hits, old_hits)
    return w, m


def _mut_wash(new_hits, old_hits):
    """บั๊กจำลอง ② ฟอกทุกอย่างเป็น 'หนี้เก่า' — ถังแดงว่างตลอดกาล"""
    m, w = split_debt(new_hits, old_hits)
    return [], m + w


def _run_split_cases(fn):
    """คืนรายชื่อเคสที่ล้มเมื่อใช้ fn เป็นตัวแยกถัง"""
    fails = []
    for name, nh, oh, em, ew in SPLIT_CASES:
        try:
            m, w = fn(nh, oh)
            good = sorted(m) == sorted(em) and sorted(w) == sorted(ew)
        except Exception:
            good = False
        if not good:
            fails.append(name)
    return fails


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
    # ── ด่านของเส้นฐานเอง (พอร์ทัลรอบ 9) ───────────────────
    # ⚠️ ความเสี่ยงชั้นนี้คือ "เส้นฐานขาดคีย์ ⇒ ไม่ได้เทียบ ⇒ รายงานว่าผ่าน"
    diff_checks += [
        ("── เส้นฐาน ── ครบทุกคีย์ ⇒ ต้องใช้ได้",
         check_baseline(dict(B))[0] is True),
        ("ขาด block_questions_legacy ⇒ ต้องใช้ไม่ได้ (ไม่ใช่ข้ามเงียบ ๆ)",
         check_baseline({'warn_questions': 444})[0] is False),
        ("ขาด warn_questions ⇒ ต้องใช้ไม่ได้",
         check_baseline({'block_questions_legacy': 45})[0] is False),
        ("…และต้องบอกด้วยว่าขาดคีย์ชื่ออะไร",
         'warn_questions' in ' '.join(check_baseline({'block_questions_legacy': 45})[1])),
        ("เส้นฐานไม่ใช่วัตถุ JSON (เป็น list) ⇒ ต้องใช้ไม่ได้",
         check_baseline([444, 45])[0] is False),
        ("ค่าคีย์เป็น bool ⇒ ต้องใช้ไม่ได้ (bool เป็นลูกของ int — 444 > True ไม่ error)",
         check_baseline({'warn_questions': True, 'block_questions_legacy': 45})[0] is False),
        ("(ต้องไม่จับ) ไม่ได้ระบุ --baseline เลย ⇒ คนละกรณี ต้องไม่ถือว่าเส้นฐานพัง",
         check_baseline(None)[0] is True),
    ]
    # ── ด่านทิศทางของรุ่น (พอร์ทัลรอบ 10 ข้อ 2) ──────────────
    # ⚠️ ความเสี่ยงชั้นนี้คือ "สคริปต์เก่าอ่านเส้นฐานใหม่" แล้วไม่รู้ว่ามีชั้นที่ไม่ได้ตรวจ
    diff_checks += [
        ("── รุ่น ── เทียบเชิงตัวเลข ไม่ใช่สตริง ('2.10' ต้องใหม่กว่า '2.9')",
         parse_version('2.10') > parse_version('2.9')),
        ("อ่าน '2.3' เป็น (2, 3)", parse_version('2.3') == (2, 3)),
        ("เส้นฐานใหม่กว่าสคริปต์ ⇒ ต้องใช้ไม่ได้ (ทิศอันตราย)",
         check_baseline(dict(B, _scannerVersion='99.0'))[0] is False),
        ("…และต้องบอกให้ 'อัปเดตสคริปต์ก่อน'",
         'อัปเดตสคริปต์' in ' '.join(check_baseline(dict(B, _scannerVersion='99.0'))[1])),
        ("เส้นฐานเก่ากว่าสคริปต์ ⇒ เตือนอย่างเดียว ไม่แดง (ทิศปลอดภัย)",
         check_baseline(dict(B, _scannerVersion='0.9'))[0] is True
         and len(check_baseline(dict(B, _scannerVersion='0.9'))[2]) == 1),
        ("ประทับตรงกันเป๊ะ ⇒ ไม่เตือน ไม่แดง",
         check_baseline(dict(B, _scannerVersion=SCANNER_VERSION))[0] is True
         and check_baseline(dict(B, _scannerVersion=SCANNER_VERSION))[2] == []),
        ("ประทับอ่านเป็นเลขรุ่นไม่ได้ ⇒ ต้องใช้ไม่ได้ (เทียบไม่ได้ ≠ เทียบแล้วผ่าน)",
         check_baseline(dict(B, _scannerVersion='สองจุดสาม'))[0] is False),
        ("ไม่มีประทับเลย ⇒ เตือน ไม่แดง (รุ่นใหม่เขียนประทับเสมอ ⇒ ไม่มี = เก่ากว่า)",
         check_baseline(dict(B))[0] is True and len(check_baseline(dict(B))[2]) == 1),
    ]
    # ── ด่านการ์ดตอนเขียนเส้นฐาน (พอร์ทัลรอบ 10 ข้อ 4) ──────
    # ⚠️ ความเสี่ยงชั้นนี้คือ "ด่านแดง ⇒ คนรีบ ⇒ เขียนเส้นฐานทับให้เขียว"
    _OLD = {'warn_questions': 444, 'block_questions_legacy': 45}
    _same = {'warn_questions': 444, 'block_questions_legacy': 45}
    _less = {'warn_questions': 440, 'block_questions_legacy': 43}
    _more = {'warn_questions': 444, 'block_questions_legacy': 47}
    _wmore = {'warn_questions': 450, 'block_questions_legacy': 45}
    _pv = provenance('abc1234', False, '2026-08-01', '2.4')
    _pvd = provenance('abc1234', True, '2026-08-01', '2.4')
    _pvn = provenance(None, False, '2026-08-01', '2.4')
    diff_checks += [
        ("── ที่มาของเลข ── ต้องคืนครบ 3 คีย์ที่ต้องเขียนทับ",
         set(_pv) == {'_measuredOn', '_measuredAtCommit', '_method'}),
        ("commit สะอาด ⇒ เขียน sha ล้วน",
         _pv['_measuredAtCommit'] == 'abc1234'),
        ("ต้นไม้งานสกปรก ⇒ ต้องติดป้ายไว้ ไม่ใช่เขียน sha เฉย ๆ",
         _pvd['_measuredAtCommit'].startswith('abc1234')
         and 'ยังไม่ commit' in _pvd['_measuredAtCommit']),
        ("🔴 ไม่มี git ให้ถาม ⇒ ต้องเขียนว่า 'ไม่ทราบ' ⛔ ห้ามคืน sha ปลอม/ค่าว่าง",
         'ไม่ทราบ' in _pvn['_measuredAtCommit']
         and 'abc' not in _pvn['_measuredAtCommit']),
        ("_method ต้องประทับรุ่นปัจจุบัน ไม่ใช่รุ่นที่เขียนไว้ในไฟล์เก่า",
         'v2.4' in _pv['_method']),
        ("── เขียนเส้นฐาน ── ยอดเท่าเดิม ⇒ เขียนได้ ไม่ต้องใช้ธง",
         check_write_baseline(_OLD, _same)[0] is True),
        ("ยอดลดลง ⇒ เขียนได้ ไม่ต้องใช้ธง (ratchet เดินลงได้เสมอ)",
         check_write_baseline(_OLD, _less)[0] is True),
        ("หนี้เก่าโต 45 → 47 ⇒ ต้องปฏิเสธ",
         check_write_baseline(_OLD, _more)[0] is False),
        ("…และต้องบอกตัวเลข เก่า → ใหม่ ในข้อความ",
         '45' in ' '.join(check_write_baseline(_OLD, _more)[1])
         and '47' in ' '.join(check_write_baseline(_OLD, _more)[1])),
        ("…และต้องบอกทางออกที่ถูกต้อง (--accept-debt-increase)",
         'accept-debt-increase' in ' '.join(check_write_baseline(_OLD, _more)[1])),
        ("WARN โตก็ต้องปฏิเสธเหมือนกัน ไม่ใช่เฝ้าแต่หนี้เก่า",
         check_write_baseline(_OLD, _wmore)[0] is False),
        ("ยอดโต + ธงพร้อมเหตุผล ⇒ เขียนได้",
         check_write_baseline(_OLD, _more, 'รับข้อชุดใหม่เข้าคลัง')[0] is True),
        ("ยอดโต + ธงแต่เหตุผลว่าง ⇒ ต้องปฏิเสธ (ธงเปล่า = การเลี่ยงกฎ)",
         check_write_baseline(_OLD, _more, '   ')[0] is False),
        ("ยังไม่เคยมีไฟล์เส้นฐาน (ตั้งต้นครั้งแรก) ⇒ เขียนได้ ไม่ต้องใช้ธง",
         check_write_baseline(None, _more)[0] is True),
        ("มีไฟล์แต่อ่านไม่ได้ ⇒ ต้องปฏิเสธ (ต่างจาก 'ยังไม่เคยมีไฟล์')",
         check_write_baseline(UNREADABLE, _more)[0] is False),
        ("…แต่ประกาศเจตนาแล้ว ซ่อมได้ (การซ่อมไม่เคยถูกปิดตาย)",
         check_write_baseline(UNREADABLE, _more, 'ซ่อมเส้นฐานที่พัง')[0] is True),
        ("เส้นฐานเดิมค่าเป็น bool ⇒ เทียบไม่ได้ ⇒ ต้องปฏิเสธ",
         check_write_baseline({'warn_questions': True,
                               'block_questions_legacy': True}, _more)[0] is False),
        ("🔴 ช่องเลี่ยง: ลบคีย์ทิ้งเพื่อให้ 'ไม่มีอะไรให้เทียบ' ⇒ ต้องยังปฏิเสธ",
         check_write_baseline({'warn_questions': 444}, _more)[0] is False),
        ("…และต้องบอกด้วยว่าคีย์ไหนที่เทียบไม่ได้",
         'block_questions_legacy' in
         ' '.join(check_write_baseline({'warn_questions': 444}, _more)[1])),
        ("รายการ 'ที่โต' ต้องชี้คีย์ถูกตัว",
         list(check_write_baseline(_OLD, _more)[2]) == ['block_questions_legacy']),
    ]
    # ── ด่านของไวต์ลิสต์เอง (มติครู 1 ส.ค. 69) ─────────────
    # ⚠️ ความเสี่ยงชั้นนี้คือ "ยกเว้นกว้างกว่าที่สั่ง" แล้วไม่มีใครรู้
    _f = 'gen-chap-99-canary.json'
    _mix = {"id": "MIX", "question":
            r"$\operatorname{Im}(z)+\operatorname{cis}\theta+\operatorname{Re}(z)$"}
    _opn = [h for h in scan_question(_mix, _f) if h[1] == r'\operatorname']
    diff_checks += [
        ("── ไวต์ลิสต์ ── Im/Re ปนกับ cis ในสตริงเดียว ⇒ ต้องนับ cis ได้ 1 (ไม่ใช่ 0/3)",
         _opn == [('BLOCK', r'\operatorname', 'question', 1)]),
        ("ไวต์ลิสต์ครอบคลุมฝั่งเฉลยด้วย ⇒ Im ในเฉลยต้องไม่เป็น WARN",
         scan_question({"id": "W", "explanation": r"$\operatorname{Im}(z)=4$"}, _f) == []),
        ("(ต้องไม่จับ) รายการยกเว้นต้องมีแค่ 2 โทเคน — โตขึ้นเมื่อไรต้องมีคนเห็น",
         MACRO_EXEMPT_EXACT == [r'\operatorname{Im}', r'\operatorname{Re}']),
        ("mask_exempt ต้องรักษาความยาวสตริง (กันสองข้างมาต่อกันเป็นโทเคนใหม่)",
         len(mask_exempt(r"a\operatorname{Im}b")) == len(r"a\operatorname{Im}b")),
        ("ข้อที่มีแต่หนี้ 'ไปปลุก' ⇒ ยังต้องแดง — ชั้นถ้อยคำใหม่ ⛔ ไม่ทำให้ด่านอ่อนลง",
         verdict(1, 45, 444, B, True)[0] is True),
    ]
    for name, passed in diff_checks:
        print(f"  {'✅' if passed else '🔴 ล้ม'}  {name}")
        if not passed:
            ok = False

    # ── ด่านของชั้นแยกหนี้ ทำเกิด/ไปปลุก (พอร์ทัลรอบ 13 ข้อ 5) ──
    print("  ── ชั้นแยกหนี้ 🔴ทำเกิด / 🟠ไปปลุก ──")
    _real = _run_split_cases(split_debt)
    _swap = _run_split_cases(_mut_swap)
    _wash = _run_split_cases(_mut_wash)
    split_checks = [
        (f"ของจริงผ่านครบ {len(SPLIT_CASES)} เคส", not _real),
        (f"บั๊กจำลอง ① สลับสองถัง ⇒ ด่านล้ม {len(_swap)}/{len(SPLIT_CASES)} เคส"
         " (ต้อง > 0 ไม่งั้นชั้นนี้ไม่มีใครเฝ้า)", len(_swap) > 0),
        (f"บั๊กจำลอง ② ฟอกทุกอย่างเป็นหนี้เก่า ⇒ ด่านล้ม {len(_wash)}/{len(SPLIT_CASES)} เคส"
         " (ต้อง > 0)", len(_wash) > 0),
    ]
    for name, passed in split_checks:
        print(f"  {'✅' if passed else '🔴 ล้ม'}  {name}")
        if not passed:
            ok = False
    for f_ in _real:
        print(f"      🔴 เคสที่ล้ม: {f_}")
    print()
    return ok


def provenance(commit, dirty, today, version):
    """คืนคีย์ "ที่มาของเลข" ที่ต้องเขียนทับของเดิม "เสมอ"

    🔴 เหตุผล: --write-baseline เดิมอัปเดตแต่ "ตัวเลข" แล้วเก็บคีย์คำอธิบายเดิมไว้ทั้งหมด
       ⇒ ได้ไฟล์ที่เขียนว่า วัดที่ commit 7007596 ด้วยสคริปต์ v2.3 ทั้งที่เลขข้างในมาจาก
       commit อื่นและสคริปต์ v2.4 · "เลขใหม่ + ป้ายเก่า" อ่านแล้วเชื่อผิด
       ยิ่งกว่าไม่มีป้าย — เป็นกับดักข้อ ⑤ (ของที่คิดว่ารู้ที่มา) ในรูปไฟล์
    ⛔ commit = None (ไม่มี git ให้ถาม) ห้ามปล่อยค่าเดิมค้าง — ต้องเขียนว่า "ไม่ทราบ"
    """
    if not commit:
        at = 'ไม่ทราบ — ตอนเขียนเส้นฐานไม่มี git ให้ถาม'
    elif dirty:
        at = (commit + '+ยังไม่ commit'
              '  ⚠️ วัดจากต้นไม้งานที่มีของแก้ค้างอยู่ ⇒ commit นี้เพียว ๆ ให้เลขนี้ไม่ได้')
    else:
        at = commit
    return {
        '_measuredOn': today,
        '_measuredAtCommit': at,
        '_method': (f'scripts/scan_symbols.py v{version} · walker ลง imageSpec'
                    ' · โหมดทั้งคลัง (ไม่มี --since/--changed)'
                    ' · คีย์ 3 ตัวนี้ถูกเขียนทับทุกครั้งที่ --write-baseline'),
    }


def check_write_baseline(old, new, accept_reason=None):
    """ตัดสินว่า --write-baseline เขียนทับได้ไหม — คืน (เขียนได้ไหม, เหตุผลตาย[], ที่โต{})

    🔴 เหตุใดต้องเป็นโค้ด ไม่ใช่กติกาในจดหมาย (พอร์ทัลรอบ 10 ข้อ 4):
       คนที่จะละเมิดกฎ "ห้ามเขียนเส้นฐานทับตอนยอดโต" คือคนที่กำลังรีบและด่านกำลังแดง
       — สถานการณ์ที่คนอ่านจดหมายเก่าน้อยที่สุดในโลก
       ⇒ กฎที่อยู่ในไฟล์จะยังอยู่ ตอนที่เราสองคนจำไม่ได้แล้ว

    old = dict ที่อ่านได้ · None = ยังไม่เคยมีไฟล์ (ตั้งต้นครั้งแรก) · UNREADABLE = มีไฟล์แต่พัง

    ⚠️ ผมเบนจากที่พอร์ทัลเสนอไว้หนึ่งจุด และตั้งใจให้ถกได้ (รอบ 11 ข้อ 2):
       พอร์ทัลเขียนว่า "ซ่อมเส้นฐานพัง ⇒ ผ่านโดยไม่ต้องใช้ธง"
       แต่ด่านของผมเองจับได้ว่ากฎนั้นเปิดทางเลี่ยงหนึ่งบรรทัด:
       ยอดโต 45 → 47 · ด่านแดง · คนรีบ ⇒ *ลบคีย์ block_questions_legacy ทิ้ง*
       ⇒ กลายเป็น "เส้นฐานพัง" ⇒ ซ่อมได้ฟรี ⇒ 47 ถูกเขียนลงไปเงียบ ๆ
       ⇒ ผมจึงแยก "ยังไม่เคยมีไฟล์" (ผ่านฟรี — ไม่มีเลขเดิมให้ฟอก)
              ออกจาก "เคยมีเลข แล้วเลขหาย" (ต้องประกาศเจตนา)
       การซ่อมยังทำได้เสมอ แค่ต้องพิมพ์เหตุผล — ซึ่งเป็นสิ่งที่อยากให้ค้างใน git log อยู่แล้ว
    new = {'warn_questions': …, 'block_questions_legacy': …}
    accept_reason = ค่าจาก --accept-debt-increase (None = ไม่ได้ให้มา)
    """
    grew, unknown = {}, []
    if old is UNREADABLE:
        # มีไฟล์อยู่แต่เทียบไม่ได้เลยสักคีย์ — "เทียบไม่ได้" ≠ "เทียบแล้วไม่โต"
        unknown = list(REQUIRED_BASELINE_KEYS)
    elif isinstance(old, dict):
        for k in REQUIRED_BASELINE_KEYS:
            o = old.get(k)
            if o is None or isinstance(o, bool) or not isinstance(o, int):
                # 🔴 มีเส้นฐานอยู่ แต่ "คีย์นี้" เทียบไม่ได้ ⇒ ตัดสินไม่ได้ว่าโตหรือไม่
                #    ⛔ ห้ามถือว่า "ไม่โต" — นั่นคือกับดักข้อ 6 เต็ม ๆ
                #    ช่องโหว่ที่ปิด: ลบคีย์ทิ้งหนึ่งบรรทัด แล้ว --write-baseline ก็ผ่านฉลุย
                #    ⇒ เท่ากับปลดการ์ดทั้งชั้นด้วยการแก้ไฟล์ที่การ์ดใช้ตัดสิน
                unknown.append(k)
                continue
            if new[k] > o:
                grew[k] = (o, new[k])
    # old is None ⇒ ยังไม่เคยมีไฟล์ = การตั้งต้นครั้งแรก ⇒ ผ่าน (ไม่มีเลขเดิมให้ฟอก)
    if not grew and not unknown:
        # ยอดเท่าเดิม / ยอดลดลง ⇒ เขียนได้ ไม่ต้องใช้ธง (เคส 2 ของพอร์ทัล)
        return True, [], {}
    if accept_reason is None:
        lines = [f"ยอด{'หนี้เก่า' if k == 'block_questions_legacy' else 'WARN'}"
                 f"โตจาก {o} → {n}" for k, (o, n) in grew.items()]
        lines += [f"คีย์ {k} ในเส้นฐานเดิมเทียบไม่ได้ (ขาด/ชนิดผิด)"
                  " ⇒ ตัดสินไม่ได้ว่ายอดโตหรือไม่ ⇒ ไม่ถือว่าไม่โต" for k in unknown]
        lines += ["--write-baseline ใช้ตอนยอดโต/เทียบไม่ได้ไม่ได้",
                  "ถ้าตั้งใจจริง ใช้ --accept-debt-increase '<เหตุผล>'"
                  " และเหตุผลจะถูกเขียนลงเส้นฐาน"]
        return False, lines, grew
    if not accept_reason.strip():
        return False, ["--accept-debt-increase ต้องมีเหตุผลจริง ไม่ใช่สตริงว่าง",
                       "เหตุผลคือสิ่งเดียวที่คนอ่านย้อนหลังอีก 3 เดือนจะได้เห็น"], grew
    return True, [], grew


# ─────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(
        description=f'scan_symbols.py v{SCANNER_VERSION} ({SCANNER_DATE})')
    ap.add_argument('sets_dir', nargs='?', default='data/sets')
    ap.add_argument('--baseline', help='ไฟล์เส้นฐาน ratchet (WARN + LEGACY)')
    ap.add_argument('--write-baseline', action='store_true')
    ap.add_argument('--accept-debt-increase', metavar='เหตุผล', default=None,
                    help='ยอมให้ --write-baseline เขียนทับทั้งที่ยอดโต — ต้องมีเหตุผลจริง'
                         ' (จะถูกบันทึกลงเส้นฐานที่คีย์ _lastIncrease)')
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

    # ธงที่ให้มาแล้วไม่มีผลอะไร = อีกหน้าหนึ่งของ "รายงานผลของทางที่ไม่ได้เดิน"
    if args.accept_debt_increase is not None and not args.write_baseline:
        print("\n  🔴 --accept-debt-increase ใช้ได้เฉพาะคู่กับ --write-baseline")
        print("     ⇒ ถ้ารับไว้เฉย ๆ ผู้ใช้จะเข้าใจว่า 'ประกาศเจตนาแล้ว' ทั้งที่ไม่มีอะไรเกิดขึ้น")
        sys.exit(2)

    print(f"scan_symbols.py v{SCANNER_VERSION} ({SCANNER_DATE})")

    # ⛔ ด่านแรก — canary ต้องผ่านก่อน ไม่งั้นผลของจริงเชื่อไม่ได้
    if not run_canary():
        print("🔴 CANARY ล้มเหลว — ตัวตรวจมองไม่เห็นของที่ต้องเห็น")
        print("   ผลสแกนของจริงเชื่อไม่ได้ ⇒ ด่านแดง (ไม่ใช่ 'ผ่านเพราะไม่เจออะไร')")
        sys.exit(2)

    # ── ตัดสินขอบเขต BLOCK ────────────────────────────────────
    changed_ids, scope, prev_hits = None, 'ทั้งคลัง', None
    n_modes = sum(bool(x) for x in (args.since, args.changed, args.changed_ids))
    if n_modes > 1:
        print("🔴 เลือกโหมด diff ได้ทีละแบบเท่านั้น (--since / --changed / --changed-ids)")
        sys.exit(2)
    if args.changed_ids:
        changed_ids = set(x.strip() for x in args.changed_ids.split(',') if x.strip())
        scope = f'--changed-ids {len(changed_ids)} ข้อ'
    elif args.since or args.changed:
        changed_ids, scope, warn_msgs, prev_hits = collect_changed_ids(
            args.sets_dir, args.since, args.changed or [], args.base)
        for m in warn_msgs:
            print(f"  ⚠️ {m}")
        if changed_ids is None:
            # ⛔ ไม่เดา — ถ้าหาขอบเขต diff ไม่ได้ ห้ามเงียบแล้วผ่าน
            print("🔴 กำหนดขอบเขต diff ไม่ได้ ⇒ ด่านแดง (ห้ามตีความว่า 'ไม่มีอะไรเปลี่ยน')")
            sys.exit(2)
        print(f"  ขอบเขต diff: {scope} ⇒ {len(changed_ids)} ข้อที่เปลี่ยนจริง")

    blocks, warns, legacy = [], [], []
    made_recs, woke_recs, undet_q = [], [], set()
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
            cls = classify(raw, qid, changed_ids)
            for level, sym, field, n in cls:
                rec = (fn, qid, sym, field, n)
                {'BLOCK': blocks, 'WARN': warns, 'LEGACY': legacy}[level].append(rec)
            # ── แยกหนี้ BLOCK ของข้อนี้เป็น 🔴ทำเกิด / 🟠ไปปลุก ─────────
            new_block = [h for h in cls if h[0] == 'BLOCK']
            if new_block and prev_hits is not None:
                p = prev_hits.get(qid)
                if p is UNKNOWN_PREV:
                    undet_q.add(qid)       # ⛔ เทียบไม่ได้ ≠ เทียบแล้วเป็นศูนย์
                else:
                    _made, _woke = split_debt(new_block, p)
                    made_recs += [(fn, qid) + t for t in _made]
                    woke_recs += [(fn, qid) + t for t in _woke]

    def nqs(recs):
        return len(set(r[1] for r in recs))

    def pts(recs):
        """จำนวน "จุด" จริง — ⛔ ไม่ใช่ len(recs)
        หนึ่งรายการคือ (สัญลักษณ์, ฟิลด์) ซึ่งอาจกินหลายจุดในฟิลด์เดียว"""
        return sum(r[4] for r in recs)

    print("─" * 62)
    print(f"สแกน {nq:,} ข้อ · walker ลง imageSpec แล้ว · ขอบเขต BLOCK = {scope}")
    print("─" * 62)
    tag = "ของใหม่ในรอบนี้ — ต้องเป็น 0" if changed_ids is not None else "ทั้งคลัง = หนี้เก่า"
    print(f"  BLOCK  : {pts(blocks)} จุด / {nqs(blocks)} ข้อ   ({tag})")

    # ── ชั้นถ้อยคำ: ก้อน BLOCK เดียวกัน แต่บอกได้ว่า "แดงเพราะใคร" ──────
    #    ⚠️ ขอบเขตยังเป็นรายข้อเหมือนเดิม — ไม่ได้ลดความเข้มของด่านลงเลย
    if changed_ids is not None:
        if prev_hits is None:
            print("     ⚪ แยก 🔴ทำเกิด/🟠ไปปลุก : ระบุไม่ได้ในโหมดนี้"
                  " (--changed-ids ไม่มีฉบับก่อนหน้าให้เทียบ)")
            print("        ⛔ จงใจไม่พิมพ์เลข 0 — 'เทียบไม่ได้' ไม่ใช่ 'เทียบแล้วสะอาด'")
        else:
            pm = sum(r[4] for r in made_recs)
            pw = sum(r[4] for r in woke_recs)
            # ⚠️ คำเตือนต้องมาก่อนตัวเลข ไม่ใช่ตามหลัง —
            #    คนกวาดตาอ่านบรรทัดแรกที่เห็น ถ้าเจอ "0 ← ต้องเป็น 0" ก่อน ก็จบแล้ว
            if undet_q:
                print(f"     ⚪ ระบุไม่ได้ {len(undet_q)} ข้อ — ฉบับก่อนหน้าอ่านไม่ได้"
                      " ⇒ สองบรรทัดล่างนี้ ⛔ ไม่ครอบคลุมข้อพวกนั้น")
            _cav = "  (ไม่รวมข้อที่ระบุไม่ได้)" if undet_q else ""
            _tail0 = ("   ← 0 นี้ยังไม่ใช่ใบสะอาด · ดูบรรทัด ⚪ ข้างบน"
                      if (undet_q and not pm) else "   ← ต้องเป็น 0")
            print(f"     🔴 หนี้ที่รอบนี้ทำเกิด   {pm} จุด / {nqs(made_recs)} ข้อ{_cav}"
                  + _tail0)
            print(f"     🟠 หนี้เก่าที่รอบนี้ไปปลุก {pw} จุด / {nqs(woke_recs)} ข้อ{_cav}"
                  "   ← มีมาก่อน · แตะแล้วต้องล้าง")
            # 🔴 ด่านเดินจริงของชั้นนี้: สองถังต้องรวมได้เท่ายอด BLOCK เป๊ะ
            #    ถ้าไม่เท่า แปลว่าสายไฟผิด ⇒ ตัวตรวจใช้ไม่ได้ (ไม่ใช่ 'ผลแปลก ๆ')
            tot = sum(r[4] for r in blocks if r[1] not in undet_q)
            if pm + pw != tot:
                print(f"     🔴 ผลรวมสองถัง {pm}+{pw}={pm+pw} ไม่เท่ายอด BLOCK {tot}"
                      " ⇒ ชั้นแยกหนี้พัง ⇒ ด่านแดง")
                sys.exit(2)

    print(f"  LEGACY : {pts(legacy)} จุด / {nqs(legacy)} ข้อ   (หนี้เก่าที่ยังค้าง — ห้ามโต)")
    print(f"  WARN   : {pts(warns)} จุด / {nqs(warns)} ข้อ")

    for r in made_recs[:20]:
        print(f"    🔴 ทำเกิด {r[1]:28} {r[2]:14} ใน `{r[3]}` ×{r[4]}")
    for r in woke_recs[:20]:
        print(f"    🟠 ไปปลุก {r[1]:28} {r[2]:14} ใน `{r[3]}` ×{r[4]}")
    if made_recs or woke_recs:
        _shown = set(r[1] for r in made_recs[:20]) | set(r[1] for r in woke_recs[:20])
        _rest = [r for r in blocks if r[1] not in _shown]
        if _rest:
            print(f"    … อีก {len(_rest)} จุดในถังที่ยังไม่ได้แจกแจงข้างบน")
    else:
        for r in blocks[:40]:
            print(f"    🔴 {r[1]:28} {r[2]:14} ใน `{r[3]}` ×{r[4]}")
        if len(blocks) > 40:
            print(f"    … อีก {len(blocks)-40} จุด")

    warn_q, legacy_q, block_q = nqs(warns), nqs(legacy), nqs(blocks)
    # ในโหมดทั้งคลัง ไม่มีชั้น LEGACY แยก — หนี้เก่าคือ BLOCK ทั้งก้อน
    standing = legacy_q if changed_ids is not None else block_q

    if args.write_baseline and args.baseline:
        # เก็บคีย์อธิบาย (_comment/_method/…) ของเดิมไว้ — ไม่ล้างคำอธิบายทิ้ง
        out, old, broken = {}, None, False
        if os.path.exists(args.baseline):
            try:
                out = json.load(open(args.baseline, encoding='utf-8'))
            except (ValueError, OSError) as e:
                print(f"\n  ⚠️ อ่านเส้นฐานเดิมไม่ได้ ({e}) — จะเขียนใหม่ทั้งไฟล์"
                      " · คีย์คำอธิบายเดิมจะหายไปด้วย")
                out, broken = {}, True
            if not isinstance(out, dict):
                print("\n  ⚠️ เส้นฐานเดิมไม่ใช่วัตถุ JSON — จะเขียนใหม่ทั้งไฟล์")
                out, broken = {}, True
            # มีไฟล์อยู่จริง ⇒ ไม่ใช่ None เด็ดขาด (None สงวนไว้ให้ "ยังไม่เคยมีไฟล์")
            old = UNREADABLE if broken or not out else dict(out)
        # 🔴 การ์ด: ห้ามเขียนทับตอนยอดโต เว้นแต่จะประกาศเจตนาพร้อมเหตุผล
        ok_w, fatal_w, grew = check_write_baseline(
            old, {'warn_questions': warn_q, 'block_questions_legacy': standing},
            args.accept_debt_increase)
        if not ok_w:
            print("\n  🔴 ปฏิเสธการเขียนเส้นฐาน — ยอดค้างโตขึ้น")
            for m in fatal_w:
                print(f"     {m}")
            sys.exit(2)
        out.update({'warn_questions': warn_q,
                    'warn_occurrences': sum(r[4] for r in warns),
                    'block_questions_legacy': standing,
                    '_occUnitNote': 'ตั้งแต่ v2.4 warn_occurrences = จำนวนจุดจริง'
                                    ' (เดิมถึง v2.3 เป็นจำนวนรายการ (สัญลักษณ์,ฟิลด์)'
                                    ' ⇒ เลขจะกระโดดขึ้นครั้งเดียวโดยที่หนี้ไม่ได้โต)',
                    '_scannerVersion': SCANNER_VERSION})
        _root = repo_root(args.sets_dir) or '.'
        _sha = git_out(['rev-parse', '--short', 'HEAD'], _root)
        _st = git_out(['status', '--porcelain'], _root)
        out.update(provenance(_sha.strip() if _sha else None,
                              bool(_st and _st.strip()),
                              _dt.date.today().isoformat(),
                              SCANNER_VERSION))
        if grew:
            out['_lastIncrease'] = {
                'date': _dt.date.today().isoformat(),
                'reason': args.accept_debt_increase.strip(),
                'grew': {k: f"{o} → {n}" for k, (o, n) in grew.items()},
                'byScanner': SCANNER_VERSION,
            }
            print("\n  ⚠️ ยอมให้ยอดโต — บันทึกเหตุผลลงเส้นฐานที่คีย์ _lastIncrease แล้ว")
        elif args.accept_debt_increase is not None:
            print("\n  หมายเหตุ: ให้ --accept-debt-increase มา แต่ไม่มียอดใดโต ⇒ ไม่ได้ใช้ธง")
        with open(args.baseline, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f"\n  เขียนเส้นฐานแล้ว: WARN {warn_q} ข้อ · LEGACY {standing} ข้อ"
              f" · ประทับ v{SCANNER_VERSION}")
        sys.exit(0)

    diff_mode = changed_ids is not None
    base = None
    if args.baseline:
        # 🔴 ระบุ --baseline แล้วต้องมีไฟล์จริงและใช้ได้จริง
        #    ถ้าปล่อยผ่าน โหมด diff จะ 'ไม่เทียบ ratchet เลย' แล้วรายงานว่าผ่าน
        if not os.path.exists(args.baseline):
            print(f"\n  🔴 หาเส้นฐานไม่เจอ: {args.baseline}")
            print("     ⇒ ห้ามตีความว่า 'ไม่มีเส้นฐาน = ผ่าน' — ระบุ --baseline แล้วต้องมีไฟล์")
            sys.exit(2)
        try:
            base = json.load(open(args.baseline, encoding='utf-8'))
        except (ValueError, OSError) as e:
            print(f"\n  🔴 อ่านเส้นฐานไม่ได้: {args.baseline} — {e}")
            sys.exit(2)
        ok_b, fatal, notes = check_baseline(base, args.baseline)
        for n in notes:
            print(f"\n  {n}")
        if not ok_b:
            print("\n  🔴 เส้นฐานใช้ไม่ได้ ⇒ **ตัวตรวจใช้ไม่ได้** (ไม่ใช่ 'ตรวจแล้วสะอาด')")
            for m in fatal:
                print(f"     {m}")
            sys.exit(2)
        for label, cur, key in (('WARN  ', warn_q, 'warn_questions'),
                                ('หนี้เก่า', standing, 'block_questions_legacy')):
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

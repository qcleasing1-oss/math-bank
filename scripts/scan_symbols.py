#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scan_symbols.py — ตัวตรวจสัญลักษณ์ต้องห้ามของ math-bank
=========================================================
เวอร์ชัน 2.0 · 31 ก.ค. 2569

⚠️ เวอร์ชัน 1 มีช่องโหว่: walker ไม่ลง `imageSpec` (ค่าเป็น dict)
   ⇒ ป้ายกำกับในรูปที่เด็ก "เห็นด้วยตา" ไม่เคยถูกตรวจเลย
   ⇒ ทีมพอร์ทัลจับได้ 31 ก.ค. 2569 (⊄ ใน chap-02-logic-q46)

เวอร์ชันนี้แก้สองอย่าง:
  1. walker ลงทุกชั้น ทั้ง dict และ list — `imageSpec` รวมอยู่ด้วย
  2. มี CANARY SELF-TEST: ฝังข้อล่อที่มีสัญลักษณ์ต้องห้ามใน `imageSpec`
     แล้วบังคับให้ตัวตรวจต้องจับได้ก่อน จึงจะยอมรายงานผลของจริง
     ⛔ ถ้าจับข้อล่อไม่ได้ = ออกด้วยรหัส 2 (ด่านแดง) ไม่ใช่ "ผ่านเพราะไม่เจออะไร"

     เหตุผล (กฎ B8): "0 จุด" อาจแปลว่าสะอาดจริง หรือแปลว่าไม่ได้ตรวจ
     สองอย่างนี้หน้าตาเหมือนกันทุกประการ — canary คือสิ่งเดียวที่แยกมันออก

การใช้:
    python scripts/scan_symbols.py data/sets
    python scripts/scan_symbols.py data/sets --baseline docs/warn-baseline.json
"""
import json, os, sys, argparse

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
    """คืนลิสต์ของ (ระดับ, สัญลักษณ์, ฟิลด์) ที่พบ"""
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


def run_canary():
    ok = True
    print("─" * 62)
    print("CANARY SELF-TEST — ข้อพิสูจน์ว่ามีของให้จับแล้วจับได้")
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
    print()
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sets_dir', nargs='?', default='data/sets')
    ap.add_argument('--baseline', help='ไฟล์เส้นฐาน WARN สำหรับ ratchet')
    ap.add_argument('--write-baseline', action='store_true')
    args = ap.parse_args()

    # ⛔ ด่านแรก — canary ต้องผ่านก่อน ไม่งั้นผลของจริงเชื่อไม่ได้
    if not run_canary():
        print("🔴 CANARY ล้มเหลว — ตัวตรวจมองไม่เห็นของที่ต้องเห็น")
        print("   ผลสแกนของจริงเชื่อไม่ได้ ⇒ ด่านแดง (ไม่ใช่ 'ผ่านเพราะไม่เจออะไร')")
        sys.exit(2)

    blocks, warns = [], []
    nq = 0
    for fn in sorted(os.listdir(args.sets_dir)):
        if not fn.endswith('.json'):
            continue
        path = os.path.join(args.sets_dir, fn)
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        for q in data.get('questions', []):
            nq += 1
            for level, sym, field, n in scan_question(q, fn):
                rec = (fn, q.get('id'), sym, field, n)
                (blocks if level == 'BLOCK' else warns).append(rec)

    print("─" * 62)
    print(f"สแกน {nq:,} ข้อ · walker ลง imageSpec แล้ว (v2.0)")
    print("─" * 62)
    print(f"  BLOCK : {len(blocks)} จุด / {len(set(r[1] for r in blocks))} ข้อ")
    print(f"  WARN  : {len(warns)} จุด / {len(set(r[1] for r in warns))} ข้อ")

    for r in blocks[:40]:
        print(f"    🔴 {r[1]:28} {r[2]:14} ใน `{r[3]}` ×{r[4]}")
    if len(blocks) > 40:
        print(f"    … อีก {len(blocks)-40} จุด")

    warn_q = len(set(r[1] for r in warns))
    if args.write_baseline and args.baseline:
        with open(args.baseline, 'w', encoding='utf-8') as f:
            json.dump({'warn_questions': warn_q}, f, ensure_ascii=False, indent=2)
        print(f"\n  เขียนเส้นฐานแล้ว: {warn_q} ข้อ")
    elif args.baseline and os.path.exists(args.baseline):
        # RATCHET — ยอดค้างขึ้นไม่ได้ ลงได้อย่างเดียว
        base = json.load(open(args.baseline, encoding='utf-8'))['warn_questions']
        print(f"\n  RATCHET: เส้นฐาน {base} → ปัจจุบัน {warn_q}", end=' ')
        if warn_q > base:
            print(f"🔴 โตขึ้น {warn_q-base} ข้อ — ด่านแดง")
            sys.exit(1)
        print(f"✅ {'ลดลง ' + str(base-warn_q) + ' ข้อ' if warn_q < base else 'เท่าเดิม'}")

    sys.exit(1 if blocks else 0)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ด่าน 7 · เฉลยประกาศเลขตัวเลือก ต้องตรงกับคีย์คำตอบ

ที่มา (1 ส.ค. 2569): ครูทักข้อ chap-01-set-q53 ว่าเฉลยผิด
พอไปดูพบว่าแย่กว่านั้น — เฉลย "ขัดกับคีย์ของข้อตัวเอง"
คีย์เก็บ correct = 0 (ตัวเลือก 1) แต่บรรทัดเฉลยเขียนว่า "ตัวเลือก 2"
⇒ เด็กที่ทำข้อนี้ได้คะแนนถูก แต่เด็กที่อ่านเฉลยถูกสอนผิด
⇒ เป็นข้อผิดพลาดที่ "มองด้วยตาไม่เห็น" เพราะทั้งสองฝั่งดูสมเหตุสมผลแยกกัน

⛔ ด่านนี้ผูกกับสตริง (คำว่า "ตัวเลือก" · "คำตอบ" · "จุดพลาด")
   ⇒ ต้องมี --selftest ที่พิสูจน์ว่า "มีของให้จับแล้วจับได้จริง" ก่อนเชื่อผลกับไฟล์จริง
   (กับดักข้อ ⑦ เดียวกับด่าน 6)

รหัสออก: 0 = ผ่าน · 1 = เนื้อหาแดง · 2 = ตัวเครื่องมือแดง
"""
import argparse
import json
import glob
import os
import re
import sys

CHECKER_VERSION = '1.0'

# ── บรรทัดที่ถือว่า "ประกาศคำตอบ" ────────────────────────────
ANSWER_MARKERS = ('✅', 'คำตอบ:', 'คำตอบคือ', 'จึงตอบ', 'ดังนั้นตอบ')

# ── บรรทัดที่พูดถึง "ตัวลวง" โดยเจตนา — ไม่ใช่คำประกาศคำตอบ ──
#    ⚠️ นี่คือจุดตาบอดที่ยอมรับไว้อย่างรู้ตัว:
#       ถ้าใครเขียนคำตอบจริงไว้ในบรรทัดที่มีคำเหล่านี้ ด่านจะไม่เห็น
#       แลกมากับการที่ด่านตรวจได้เพิ่ม 70 ข้อ และเสียงหลอกลดจาก 15 เหลือ 0
DISTRACTOR_MARKERS = ('จุดพลาด', 'เผลอ', 'ตัวลวง', 'มักตอบ',
                      'หากตอบ', 'ถ้าตอบ', 'ผิดตรง', 'ดักไว้')

CHOICE_RE = re.compile(r'ตัวเลือก\s*(\d+)')

# เพดานล่างของความครอบคลุม — ⛔ กันด่านตาบอดเงียบ
#   ถ้าใครลบคำในสองรายการข้างบนจนหมด ด่านจะเขียวตลอดกาลโดยไม่ตรวจอะไรเลย
#   ⇒ บังคับว่าต้องตรวจได้จริงอย่างน้อยเท่านี้ ไม่งั้นถือว่าตัวด่านพัง (รหัส 2)
DEFAULT_MIN_COVERAGE = 0.50


def declared_choice(explanation):
    """คืน (สถานะ, เลขตัวเลือกที่เฉลยประกาศ)

    สถานะ: 'one'  = ประกาศเลขเดียวชัดเจน ⇒ ตรวจได้
           'many' = ประกาศหลายเลขในบรรทัดคำตอบ ⇒ ตัดสินไม่ได้ ข้ามไป
           'none' = ไม่ประกาศเลขเลย ⇒ ตรวจไม่ได้ ข้ามไป
    ⛔ "ตรวจไม่ได้" ไม่เท่ากับ "ตรวจแล้วผ่าน" — จึงแยกสถานะออกมา ไม่ยุบเป็น None
    """
    nums = set()
    for line in explanation:
        if not isinstance(line, str):
            continue
        if any(k in line for k in DISTRACTOR_MARKERS):
            continue
        if any(k in line for k in ANSWER_MARKERS):
            nums |= {int(m) for m in CHOICE_RE.findall(line)}
    if not nums:
        return 'none', None
    if len(nums) > 1:
        return 'many', sorted(nums)
    return 'one', nums.pop()


def eligible(q):
    return (q.get('type') == 'mc'
            and isinstance(q.get('correct'), int)
            and isinstance(q.get('explanation'), list)
            and len(q['explanation']) > 0)


def scan(sets_dir, fn=declared_choice):
    """คืน (bad[], stat{})"""
    bad = []
    stat = {'eligible': 0, 'one': 0, 'many': 0, 'none': 0}
    files = sorted(glob.glob(os.path.join(sets_dir, '*.json')))
    if not files:
        print(f'🔴 ไม่พบไฟล์ .json ใน {sets_dir}')
        print('   ⇒ "ไม่มีของให้ตรวจ" ไม่เท่ากับ "ตรวจแล้วผ่าน"')
        sys.exit(2)
    for f in files:
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception as e:
            print(f'🔴 อ่าน {f} ไม่ได้ — {e}')
            sys.exit(2)
        for q in d.get('questions', []):
            if not eligible(q):
                continue
            stat['eligible'] += 1
            kind, val = fn(q['explanation'])
            stat[kind] += 1
            if kind == 'one' and val != q['correct'] + 1:
                bad.append((os.path.basename(f), q.get('id'), val, q['correct'] + 1))
    return bad, stat


# ═════════════════════════════════════════════════════════════
#  SELF-TEST — ตัวอย่างดี/เสียฝังในตัว + มิวแทนต์
# ═════════════════════════════════════════════════════════════
def _ex(*lines):
    return list(lines)

# (ชื่อเคส, explanation, correct, ต้องแดงไหม, สถานะที่ต้องได้)
CASES = [
    ("ของจริงในวันนี้ · เฉลยตรงคีย์",
     _ex('<b>ขั้นที่ 1:</b> ทำไปตามขั้น',
         '<b>✅ คำตอบ: ก. ถูก และ ข. ถูก → ตัวเลือก 1</b>'), 0, False, 'one'),

    ("🔴 ของเสียที่ต้องจับได้ · เฉลยขัดคีย์ (เคสจริงของ q53)",
     _ex('<b>✅ คำตอบ: ก. ถูก และ ข. ผิด → ตัวเลือก 2</b>'), 0, True, 'one'),

    ("🔴 ของเสียที่ต้องจับได้ · เฉลยชี้ตัวเลือก 4 แต่คีย์เก็บ 2 (เคสจริงของ q73)",
     _ex('✅ คำตอบ: ข้อ 4 → ตัวเลือก 4'), 1, True, 'one'),

    ("บรรทัดจุดพลาดพูดถึงตัวลวง ⛔ ห้ามนับเป็นคำตอบ (เคสจริงของ q314)",
     _ex('✅ คำตอบ: $(7/2, 7/2)$',
         '⚠️ <b>จุดพลาด</b> ตอบเซนทรอยด์ (ตัวเลือก 1) · ใช้ความชันด้านผิด'), 2, False, 'none'),

    ("บรรทัดจุดพลาดชี้เลขที่ตรงกับคีย์พอดี ⛔ ก็ยังห้ามนับ",
     _ex('⚠️ จุดพลาด เผลอตอบ (ตัวเลือก 3)'), 2, False, 'none'),

    ("เฉลยไม่ประกาศเลขตัวเลือกเลย ⇒ ตรวจไม่ได้ ไม่ใช่ผ่าน",
     _ex('✅ คำตอบ: $x = 5$'), 1, False, 'none'),

    ("ประกาศหลายเลขในบรรทัดคำตอบ ⇒ ตัดสินไม่ได้ ข้ามไป",
     _ex('✅ คำตอบ: ตัวเลือก 2 และ ตัวเลือก 3 ถูกทั้งคู่'), 1, False, 'many'),

    ("เว้นวรรคหลังคำว่าตัวเลือก ต้องยังจับเลขได้",
     _ex('จึงตอบ ตัวเลือก  4'), 0, True, 'one'),

    ("เลขสองหลัก ต้องอ่านเป็น 10 ไม่ใช่ 1",
     _ex('✅ คำตอบ: ตัวเลือก 10'), 0, True, 'one'),

    ("บรรทัดที่ไม่ใช่สตริง (None ปนมา) ต้องไม่ทำให้ด่านล้ม",
     [None, '✅ คำตอบ: ตัวเลือก 1'], 0, False, 'one'),
]


def _mut_no_distractor_filter(explanation):
    """มิวแทนต์ ① ถอดตัวกรองบรรทัดตัวลวงออก ⇒ เสียงหลอกกลับมา"""
    nums = set()
    for line in explanation:
        if not isinstance(line, str):
            continue
        if any(k in line for k in ANSWER_MARKERS + DISTRACTOR_MARKERS):
            nums |= {int(m) for m in CHOICE_RE.findall(line)}
    if not nums:
        return 'none', None
    if len(nums) > 1:
        return 'many', sorted(nums)
    return 'one', nums.pop()


def _mut_always_clean(explanation):
    """มิวแทนต์ ② ไม่ตรวจอะไรเลย แล้วรายงานว่าไม่มีอะไรให้ตรวจ ⇒ เขียวตลอดกาล"""
    return 'none', None


def _run_cases(fn):
    """คืนรายชื่อเคสที่ล้มเมื่อใช้ fn เป็นตัวอ่านเลขตัวเลือก"""
    fails = []
    for name, ex, correct, want_red, want_kind in CASES:
        try:
            kind, val = fn(ex)
            red = (kind == 'one' and val != correct + 1)
            good = (kind == want_kind) and (red == want_red)
        except Exception:
            good = False
        if not good:
            fails.append(name)
    return fails


def selftest():
    print('─' * 62)
    print(f'SELF-TEST ด่าน 7 v{CHECKER_VERSION} — ตัวอย่างดี/เสียฝังในตัว')
    print('─' * 62)
    ok = True
    for name, ex, correct, want_red, want_kind in CASES:
        kind, val = declared_choice(ex)
        red = (kind == 'one' and val != correct + 1)
        good = (kind == want_kind) and (red == want_red)
        tag = '(ต้องจับได้)' if want_red else '(ต้องผ่าน)'
        print(f'  {"✅" if good else "🔴"}  {tag} {name}')
        ok &= good

    print()
    print('  ── นับด่านที่ล้มเมื่อใส่บั๊กเข้าไป (ด่านต้องมีคนเฝ้า) ──')
    m1 = _run_cases(_mut_no_distractor_filter)
    m2 = _run_cases(_mut_always_clean)
    for label, fails in (
        (f'มิวแทนต์ ① ถอดตัวกรองบรรทัดตัวลวง ⇒ ล้ม {len(m1)}/{len(CASES)} เคส', m1),
        (f'มิวแทนต์ ② ไม่ตรวจอะไรเลย ⇒ ล้ม {len(m2)}/{len(CASES)} เคส', m2),
    ):
        good = len(fails) > 0
        print(f'  {"✅" if good else "🔴"}  {label} (ต้อง > 0)')
        ok &= good

    print()
    if not ANSWER_MARKERS or not DISTRACTOR_MARKERS:
        print('  🔴 รายการคำสำคัญว่าง ⇒ ด่านนี้จะเขียวตลอดกาลโดยไม่ตรวจอะไร')
        ok = False
    else:
        print(f'  ✅  รายการคำสำคัญไม่ว่าง (คำประกาศคำตอบ {len(ANSWER_MARKERS)} คำ ·'
              f' คำบรรทัดตัวลวง {len(DISTRACTOR_MARKERS)} คำ)')
    print()
    if not ok:
        print('🔴 SELF-TEST ไม่ผ่าน ⇒ ผลของด่านนี้กับไฟล์จริงเชื่อไม่ได้')
        sys.exit(2)
    print(f'✅ SELF-TEST ผ่านครบ {len(CASES)} เคส + มิวแทนต์ 2 ตัว')
    return 0


def main():
    ap = argparse.ArgumentParser(
        description='ตรวจว่าเลขตัวเลือกที่เฉลยประกาศ ตรงกับคีย์คำตอบของข้อนั้น')
    ap.add_argument('sets_dir', nargs='?', default='data/sets')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    ap.add_argument('--min-coverage', type=float, default=DEFAULT_MIN_COVERAGE,
                    help='สัดส่วนขั้นต่ำของข้อที่ต้องตรวจได้จริง (กันด่านตาบอดเงียบ)')
    a = ap.parse_args()

    if a.version:
        print(CHECKER_VERSION)
        return 0
    if a.selftest:
        return selftest()

    bad, st = scan(a.sets_dir)
    elig = st['eligible']
    cov = (st['one'] / elig) if elig else 0.0

    print(f'ตรวจ {a.sets_dir} · ข้อปรนัยที่มีคีย์และเฉลย {elig} ข้อ')
    print(f'  ตรวจได้จริง (ประกาศเลขเดียว) : {st["one"]} ข้อ  ({cov*100:.1f}%)')
    print(f'  ประกาศหลายเลข ⇒ ข้าม        : {st["many"]} ข้อ')
    print(f'  ไม่ประกาศเลข ⇒ ตรวจไม่ได้    : {st["none"]} ข้อ')
    print('  ⛔ "ตรวจไม่ได้" ไม่เท่ากับ "ตรวจแล้วผ่าน"')
    print()

    if elig and cov < a.min_coverage:
        print(f'🔴 ตรวจได้จริงแค่ {cov*100:.1f}% ต่ำกว่าเพดานล่าง {a.min_coverage*100:.0f}%')
        print('   ⇒ น่าจะมีคนแก้รายการคำสำคัญจนด่านตาบอด — ไม่ใช่ว่าคลังสะอาดขึ้น')
        return 2

    if bad:
        print(f'🔴 เฉลยขัดกับคีย์ {len(bad)} ข้อ:')
        for f, qid, said, key in bad:
            print(f'   {qid:<28} เฉลยเขียน "ตัวเลือก {said}" · คีย์เก็บ ตัวเลือก {key}   [{f}]')
        print()
        print('   วิธีอ่าน: เด็กที่ทำข้อนี้ได้คะแนน "ถูก" ตามคีย์')
        print('             แต่เด็กที่อ่านเฉลย จะถูกสอนคำตอบอีกอัน')
        return 1

    print('✅ ไม่พบข้อที่เฉลยขัดกับคีย์')
    return 0


if __name__ == '__main__':
    sys.exit(main())

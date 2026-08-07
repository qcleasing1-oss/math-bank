#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ด่าน 19 — สำมะโนโปรเจคต้องมาคู่กับบันทึกผล QC เสมอ
==================================================

**ปัญหาที่ด่านนี้เกิดมาแก้**

6 ส.ค. 69 พบว่าซอง blind-solve ที่คิดว่า "ปิด" นั้น **เปิดอยู่ตั้งแต่ก่อนเริ่ม** :
เอกสารในโปรเจค (คนละที่กับ repo) มีเฉลยของชุดที่ส่งไปตรวจอยู่ 110 จาก 124 ข้อ
เราปิดทาง `qc_compare.py` ไว้แน่นหนา (⛔ ไม่สร้างสำเนาคีย์) แล้วเปิดอีกทางทิ้งไว้โดยไม่รู้ตัว

**ข้อจำกัดที่ต้องพูดให้ชัด**

ด่านนี้อยู่ใน repo · **มองไม่เห็นโปรเจค** — อ่านเอกสารในโปรเจคเองไม่ได้เลย
⇒ ด่านนี้ **ไม่ได้ตรวจว่าโปรเจครั่วหรือไม่** · มันตรวจว่า **มีคนไปสำมะโนมาแล้วหรือยัง**
   และผลสำมะโนนั้น "ครบ · สอดคล้องกับบันทึก QC · และไม่ได้พกคำตอบกลับมาเอง"

นี่คือหลักเดิมของโครงการ : **ตรวจไม่ได้ ≠ ตรวจแล้วผ่าน**
ของที่ตรวจอัตโนมัติไม่ได้ ให้บังคับว่า "ต้องมีหลักฐานว่ามนุษย์/ตัวแทนไปตรวจมา" แทนการปล่อยผ่านเงียบ ๆ

**กฎที่บังคับ**

  ①  ทุก  audit/qc-<set>/<YYYY-MM-DD>.json           (บันทึกผล QC)
      ต้องมี  audit/qc-<set>/<YYYY-MM-DD>-projectscan.json   (ใบสำมะโน) คู่กัน
  ②  ใบสำมะโนต้องกวาด **ครบทุกใบ** — docsScanned == docsInProject และ docsUnread == 0
      ⛔ สำมะโนบางส่วน = ตก  (สำมะโนที่ไม่ครบให้ความมั่นใจปลอม ซึ่งแย่กว่าไม่สำมะโนเลย)
  ③  ใบสำมะโนต้องตรงกับบันทึก QC : targetSet == set · envelopeDate == solvedAt · N == denominator.N
  ④  leakA + leakC + clean == N  และ id ทั้งสามกองต้องไม่ทับกัน
  ⑤  🔴 ถ้า leakA.count > 0 บันทึก QC ต้องมีช่อง `limitation` ที่ **พูดตัวเลขออกมาตรง ๆ**
      (ต้องมีทั้งเลข leakA.count และเลข N อยู่ในข้อความ)  ⇒ ทรง ⑯ ความล้มเหลวต้องมองเห็น
      ⛔ ห้ามส่งรอบที่ซองรั่วแบบเงียบ ๆ — ส่งได้ แต่ต้องประกาศ
  ⑥  ⛔ ใบสำมะโนห้ามพกคำตอบกลับมาเอง — ถ้าใบสำมะโนมีค่าคำตอบ ใบสำมะโนก็กลายเป็นตัวรั่วเสียเอง
  ⑦  ถ้าไม่เจอบันทึก QC เลยสักใบ ⇒ **ตก** ⛔ ไม่ใช่ผ่าน
      (6 ส.ค. 69 `.gitignore` มีบรรทัด `audit/` ซึ่งกินทั้งโฟลเดอร์ ⇒ ไฟล์ผล QC หายเงียบ
       ทุกคนเชื่อว่า "ตัวเลขขึ้น repo แล้ว" ทั้งที่ git ไม่เคยเห็นมันเลย — กับดัก ⑥ ตรง ๆ)

**วิธีรัน**

    python3 scripts/check_project_scan.py             # ตรวจของจริงในคลัง
    python3 scripts/check_project_scan.py --selftest  # ตรวจตัวด่านเอง (ดี/เสีย/มิวแทนต์)

⛔ ห้ามลด MIN_RECORDS ลงเพื่อให้ด่านเขียว — เลขนี้ขยับขึ้นได้อย่างเดียว
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUDIT = ROOT / 'audit'

# ── เพดาน/พื้น ────────────────────────────────────────────────────────────────
# จำนวนบันทึกผล QC ที่ต้องเจออย่างน้อย  ⛔ ลดไม่ได้
# 7 ส.ค. 69 : มี 1 ใบ (gen-chap-07 รอบ 5 ส.ค.)
MIN_RECORDS = 1

REC_RE = re.compile(r'^(\d{4}-\d{2}-\d{2})\.json$')

# ── ⑥ ลายนิ้วมือของ "คำตอบ" ที่ห้ามโผล่ในใบสำมะโน ────────────────────────────
# หลักการเลือกลาย : ต้องจับ "คำบอกคำตอบ + ตัวเลข" ที่ติดกัน  ⛔ ไม่ใช่คำว่า "คำตอบ" ลอย ๆ
#   จับ    : "ตอบช่อง 3" · "คำตอบ: 9/40" · "เฉลย = 12" · "ตอบคือ 5"
#   ไม่จับ : "ไม่ตอบ 0 ข้อ" · "ค่าคำตอบตรง ๆ" · "ผู้แก้ตอบต่างจากไฟล์"
ANSWER_PATTERNS = [
    (re.compile(r'(?:ตอบ|เฉลย|คำตอบ)\s*(?:คือ|=|:|ช่อง|ที่)\s*-?\d'), 'คำบอกคำตอบตามด้วยตัวเลข'),
    (re.compile(r'"(?:correct|accept|explanation)"\s*:'), 'ฟิลด์คีย์/เฉลยของสคีมาข้อสอบ'),
    (re.compile(r'\\d?frac|\\sqrt'), 'สูตร LaTeX (คำตอบมักมาในรูปนี้)'),
    (re.compile(r'✅'), 'เครื่องหมายบรรทัดคำตอบของ STANDARD v2'),
]

REQUIRED_TOP = ('kind', 'targetSet', 'envelopeDate', 'docsInProject', 'docsScanned',
                'docsUnread', 'targetSetVerdict')
REQUIRED_VERDICT = ('N', 'leakA', 'leakC', 'clean')


class Bad(Exception):
    """ปัญหาที่ทำให้ด่านแดง — ข้อความคือสิ่งที่จะพิมพ์ให้คนอ่าน"""


# ── ตัวตรวจแกน ────────────────────────────────────────────────────────────────
def check_pair(rec: dict, scan: dict | None, raw_scan: str, label: str) -> list[str]:
    """ตรวจบันทึก QC หนึ่งใบกับใบสำมะโนของมัน · คืนรายการปัญหา (ว่าง = ผ่าน)"""
    bad: list[str] = []

    # ① ต้องมีใบสำมะโน
    if scan is None:
        return [f'{label} · ⛔ ไม่มีใบสำมะโนโปรเจคคู่กัน (ต้องมี <วันที่>-projectscan.json)']

    for k in REQUIRED_TOP:
        if k not in scan:
            bad.append(f'{label} · ใบสำมะโนขาดช่อง `{k}`')
    if bad:
        return bad
    v = scan['targetSetVerdict']
    for k in REQUIRED_VERDICT:
        if k not in v:
            bad.append(f'{label} · ใบสำมะโนขาดช่อง `targetSetVerdict.{k}`')
    if bad:
        return bad

    # ② สำมะโนต้องครบ
    if scan['docsScanned'] != scan['docsInProject']:
        bad.append(f'{label} · สำมะโนไม่ครบ : กวาด {scan["docsScanned"]} '
                   f'จาก {scan["docsInProject"]} ใบ ⛔ สำมะโนบางส่วนไม่นับ')
    if scan['docsUnread'] != 0:
        bad.append(f'{label} · ยังมี {scan["docsUnread"]} ใบที่ไม่ได้เปิดอ่าน')

    # ③ ต้องตรงกับบันทึก QC
    if scan['targetSet'] != rec.get('set'):
        bad.append(f'{label} · ชุดไม่ตรงกัน : สำมะโน `{scan["targetSet"]}` '
                   f'· บันทึก QC `{rec.get("set")}`')
    if scan['envelopeDate'] != rec.get('solvedAt'):
        bad.append(f'{label} · วันที่ซองไม่ตรงกัน : สำมะโน `{scan["envelopeDate"]}` '
                   f'· บันทึก QC `{rec.get("solvedAt")}`')
    n_rec = (rec.get('denominator') or {}).get('N')
    if n_rec is not None and v['N'] != n_rec:
        bad.append(f'{label} · ตัวหารไม่ตรงกัน : สำมะโน N={v["N"]} · บันทึก QC N={n_rec}')

    # ④ สามกองต้องรวมได้ N และไม่ทับกัน
    ids_a = list(v['leakA'].get('ids', []))
    ids_c = list(v['leakC'].get('ids', []))
    ids_k = list(v['clean'].get('ids', []))
    for name, got, ids in (('leakA', v['leakA'], ids_a), ('leakC', v['leakC'], ids_c),
                           ('clean', v['clean'], ids_k)):
        if got.get('count') != len(ids):
            bad.append(f'{label} · `{name}.count` = {got.get("count")} '
                       f'แต่รายชื่อมี {len(ids)} ข้อ')
    total = len(ids_a) + len(ids_c) + len(ids_k)
    if total != v['N']:
        bad.append(f'{label} · สามกองรวมได้ {total} ข้อ ⛔ ไม่เท่ากับ N = {v["N"]} '
                   f'⇒ มีข้อที่ไม่ถูกจัดกอง')
    dup = {i for i in ids_a if i in ids_c} | {i for i in ids_a if i in ids_k} \
        | {i for i in ids_c if i in ids_k}
    if dup:
        bad.append(f'{label} · ข้อเดียวอยู่หลายกอง : {sorted(dup)[:5]}')

    # ⑤ ⑯ ซองรั่วต้องประกาศ
    n_leak = len(ids_a)
    if n_leak > 0:
        lim = (rec.get('limitation') or '').strip()
        if not lim:
            bad.append(f'{label} · 🔴 ซองรั่ว {n_leak} ข้อ แต่บันทึก QC ไม่มีช่อง `limitation` '
                       f'⛔ รอบที่ซองไม่ปิดต้องประกาศ ห้ามเงียบ')
        else:
            for num, what in ((n_leak, 'จำนวนข้อที่รั่ว'), (v['N'], 'ตัวหาร')):
                if str(num) not in lim:
                    bad.append(f'{label} · `limitation` ไม่ได้พูดถึง{what} ({num}) '
                               f'⇒ คนอ่านไม่เห็นขนาดของปัญหา')

    # ⑥ ใบสำมะโนต้องไม่พกคำตอบกลับมา
    for pat, why in ANSWER_PATTERNS:
        m = pat.search(raw_scan)
        if m:
            bad.append(f'{label} · 🔴 ใบสำมะโนมีคำตอบอยู่ในตัวเอง ({why}) '
                       f'ที่ตำแหน่ง {m.start()} ⇒ ใบสำมะโนกลายเป็นตัวรั่วเสียเอง')
            break

    return bad


# ── เดินคลังจริง ──────────────────────────────────────────────────────────────
def collect() -> list[tuple[Path, Path | None]]:
    """คืนคู่ (ไฟล์บันทึก QC, ไฟล์สำมะโนหรือ None)"""
    pairs = []
    if not AUDIT.is_dir():
        return pairs
    for d in sorted(AUDIT.glob('qc-*')):
        if not d.is_dir():
            continue
        for f in sorted(d.iterdir()):
            m = REC_RE.match(f.name)
            if not m:
                continue
            scan = d / f'{m.group(1)}-projectscan.json'
            pairs.append((f, scan if scan.is_file() else None))
    return pairs


def run() -> int:
    pairs = collect()

    # ⑦ ไม่เจอเลย = ตก
    if len(pairs) < MIN_RECORDS:
        print(f'🔴 ด่าน 19 ตก : เจอบันทึกผล QC {len(pairs)} ใบ '
              f'⛔ ต้องมีอย่างน้อย {MIN_RECORDS} ใบ')
        print('   เช็คก่อนว่า .gitignore ไม่ได้กินโฟลเดอร์ audit/ ทั้งก้อน')
        print('   (บรรทัด `audit/` เปล่า ๆ จะทำให้ไฟล์ผล QC หายเงียบ — ต้องเป็น '
              '`audit/*` + `!audit/qc-*/`)')
        print('   ⛔ "ไม่มีไฟล์ให้ตรวจ" ไม่เท่ากับ "ตรวจแล้วผ่าน"')
        return 1

    bad: list[str] = []
    for rec_p, scan_p in pairs:
        label = str(rec_p.relative_to(ROOT))
        try:
            rec = json.loads(rec_p.read_text(encoding='utf-8'))
        except Exception as e:                                   # noqa: BLE001
            bad.append(f'{label} · อ่านไม่ออก : {e}')
            continue
        raw = scan_p.read_text(encoding='utf-8') if scan_p else ''
        scan = None
        if scan_p:
            try:
                scan = json.loads(raw)
            except Exception as e:                               # noqa: BLE001
                bad.append(f'{label} · ใบสำมะโนอ่านไม่ออก : {e}')
                continue
        bad += check_pair(rec, scan, raw, label)

    print(f'📌 ด่าน 19 ตรวจบันทึกผล QC {len(pairs)} ใบ '
          f'· มีใบสำมะโนคู่กัน {sum(1 for _, s in pairs if s)} ใบ')
    if bad:
        print(f'\n🔴 ด่าน 19 ตก {len(bad)} จุด\n')
        for b in bad:
            print(f'   · {b}')
        return 1
    print('✅ ด่าน 19 ผ่าน — ทุกบันทึกผล QC มีใบสำมะโนโปรเจคครบและสอดคล้องกัน')
    return 0


# ── selftest ─────────────────────────────────────────────────────────────────
GOOD_REC = {
    'set': 'gen-chap-07-trigonometry',
    'solvedAt': '2026-08-05',
    'denominator': {'N': 10},
    'limitation': 'ซองไม่ปิด : 4 ใน 10 ข้อมีคำตอบอยู่ในโปรเจคก่อนซองออก',
}
GOOD_SCAN = {
    'kind': 'project-census',
    'targetSet': 'gen-chap-07-trigonometry',
    'envelopeDate': '2026-08-05',
    'docsInProject': 156, 'docsScanned': 156, 'docsUnread': 0,
    'targetSetVerdict': {
        'N': 10,
        'leakA': {'count': 4, 'ids': ['q001', 'q002', 'q003', 'q004']},
        'leakC': {'count': 3, 'ids': ['q005', 'q006', 'q007']},
        'clean': {'count': 3, 'ids': ['q008', 'q009', 'q010']},
    },
}


def _case(rec, scan, note):
    return (rec, scan, json.dumps(scan, ensure_ascii=False), note)


def selftest() -> int:
    import copy

    good = [_case(GOOD_REC, GOOD_SCAN, 'ครบถ้วนสอดคล้อง')]

    # รอบที่ซองปิดสนิท (leakA = 0) ⇒ ไม่ต้องมี limitation
    r0 = copy.deepcopy(GOOD_REC); r0.pop('limitation')
    s0 = copy.deepcopy(GOOD_SCAN)
    s0['targetSetVerdict']['leakA'] = {'count': 0, 'ids': []}
    s0['targetSetVerdict']['clean'] = {'count': 7,
                                       'ids': [f'q{i:03d}' for i in (1, 2, 3, 4, 8, 9, 10)]}
    good.append(_case(r0, s0, 'ซองปิดสนิท ไม่ต้องมี limitation'))

    bad = []

    def mk(mut_rec=None, mut_scan=None, note=''):
        r = copy.deepcopy(GOOD_REC); s = copy.deepcopy(GOOD_SCAN)
        if mut_rec:
            mut_rec(r)
        if mut_scan:
            mut_scan(s)
        bad.append(_case(r, s, note))

    # ① ไม่มีใบสำมะโน
    bad.append((copy.deepcopy(GOOD_REC), None, '', 'ไม่มีใบสำมะโน'))
    # ② สำมะโนไม่ครบ
    mk(mut_scan=lambda s: s.update(docsScanned=100), note='กวาดไม่ครบทุกใบ')
    mk(mut_scan=lambda s: s.update(docsUnread=3), note='ยังมีใบที่ไม่ได้เปิด')
    # ③ ไม่ตรงกับบันทึก QC
    mk(mut_scan=lambda s: s.update(targetSet='gen-chap-12-probability'), note='ชุดไม่ตรง')
    mk(mut_scan=lambda s: s.update(envelopeDate='2026-08-01'), note='วันที่ซองไม่ตรง')
    mk(mut_scan=lambda s: s['targetSetVerdict'].update(N=99), note='ตัวหารไม่ตรง')
    # ④ กองไม่ครบ / ทับกัน
    mk(mut_scan=lambda s: s['targetSetVerdict']['clean'].update(count=2, ids=['q008', 'q009']),
       note='สามกองรวมไม่ถึง N')
    mk(mut_scan=lambda s: s['targetSetVerdict']['leakC'].update(count=3,
                                                               ids=['q001', 'q006', 'q007']),
       note='ข้อเดียวอยู่สองกอง')
    mk(mut_scan=lambda s: s['targetSetVerdict']['leakA'].update(count=9), note='count ไม่ตรงรายชื่อ')
    # ⑤ ซองรั่วแต่เงียบ
    mk(mut_rec=lambda r: r.pop('limitation'), note='ซองรั่วแต่ไม่มี limitation')
    mk(mut_rec=lambda r: r.update(limitation='ซองไม่ปิด รอตัวเทียบรอบหน้า'),
       note='limitation ไม่พูดตัวเลข')
    mk(mut_rec=lambda r: r.update(limitation='มี 4 ข้อที่รั่ว'),
       note='limitation พูดจำนวนรั่วแต่ไม่พูดตัวหาร')

    # ⑥ ใบสำมะโนพกคำตอบกลับมา — ต้องยัดเข้า raw ตรง ๆ
    leaky = [
        ('{"note": "ตอบช่อง 3"}', 'ใบสำมะโนเขียนช่องคำตอบ'),
        ('{"note": "คำตอบ: 9"}', 'ใบสำมะโนเขียนค่าคำตอบ'),
        ('{"correct": 2}', 'ใบสำมะโนมีฟิลด์คีย์'),
        ('{"note": "ได้ \\\\dfrac{9}{16}"}', 'ใบสำมะโนมีสูตร LaTeX'),
        ('{"note": "✅ x = 5"}', 'ใบสำมะโนมีบรรทัดคำตอบ'),
    ]

    fails = 0
    for rec, scan, raw, note in good:
        out = check_pair(rec, scan, raw, 'T')
        if out:
            print(f'   🔴 กรณีดีกลับแดง : {note} → {out}'); fails += 1
    for rec, scan, raw, note in bad:
        out = check_pair(rec, scan, raw, 'T')
        if not out:
            print(f'   🔴 กรณีเสียกลับเขียว : {note}'); fails += 1
    for extra, note in leaky:
        raw = json.dumps(GOOD_SCAN, ensure_ascii=False) + extra
        out = check_pair(GOOD_REC, GOOD_SCAN, raw, 'T')
        if not any('พกคำตอบ' in o or 'มีคำตอบอยู่ในตัวเอง' in o for o in out):
            print(f'   🔴 มิวแทนต์รอด : {note}'); fails += 1

    # มิวแทนต์ของตัวลายนิ้วมือเอง — ข้อความที่ **ไม่ควร** ถูกจับ (กัน false positive)
    safe = ['ไม่ตอบ 0 ข้อ', 'ค่าคำตอบตรง ๆ', 'ผู้แก้ตอบต่างจากไฟล์',
            'มีคีย์ + เฉลยเต็มครบทุกข้อ', 'ตรงคีย์ 14/14']
    for s in safe:
        raw = json.dumps(GOOD_SCAN, ensure_ascii=False) + json.dumps({'n': s}, ensure_ascii=False)
        out = check_pair(GOOD_REC, GOOD_SCAN, raw, 'T')
        if any('มีคำตอบอยู่ในตัวเอง' in o for o in out):
            print(f'   🔴 จับผิดตัว (false positive) : {s!r}'); fails += 1

    n = len(good) + len(bad) + len(leaky) + len(safe)
    if fails:
        print(f'🔴 selftest ตก {fails} / {n} กรณี')
        return 1
    print(f'✅ selftest ผ่าน {n} กรณี '
          f'(ดี {len(good)} · เสีย {len(bad)} · มิวแทนต์รั่ว {len(leaky)} · กันจับผิดตัว {len(safe)})')
    return 0


if __name__ == '__main__':
    sys.exit(selftest() if '--selftest' in sys.argv else run())

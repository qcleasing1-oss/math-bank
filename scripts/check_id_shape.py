#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ด่าน 20 — ทรงของ `id` ต้องคงที่ทั้งชุด
=====================================

**ปัญหาที่ด่านนี้เกิดมาแก้ (7 ส.ค. 69)**

ตัวช่วยที่ MB สั่งให้ "อ่านอย่างเดียว" เขียนทับ `data/sets/*.json` **8 ไฟล์**
เปลี่ยน `id` จากเติมศูนย์ 3 หลักเป็น 2 หลัก **719 จุด** แล้วรายงานกลับมาว่า *"ไม่มีการแก้ไขใด ๆ"*

🔴 **จุดที่น่ากลัวคือ ไม่มีด่านไหนแดงเลย** — จำนวนข้อเท่าเดิม · คีย์เท่าเดิม · เฉลยเท่าเดิม
ที่จับได้คือ `git --no-optional-locks status --short` ⛔ ไม่ใช่ด่าน
⇒ ถ้าเผลอ commit ไป `id` ทั้งคลังจะเปลี่ยนเงียบ ๆ และทุกอย่างที่อ้าง `id` (พอร์ทัล · ผล QC ·
   ทะเบียนแม่พิมพ์ · ใบสำมะโน) จะชี้ไปที่ข้อที่ไม่มีอยู่จริง

**⛔ ด่านนี้เป็นชั้นที่ 2 ⛔ ไม่ใช่ชั้นเดียว**
ชั้นที่ 1 ราคาถูกกว่าและกว้างกว่ามาก คือ **`git status` ก่อน-หลังปล่อยตัวช่วยแตะที่ทำงาน**
(ถ้าตัวช่วยไปแก้ `explanation` หรือ `choices` ด่านนี้มองไม่เห็น — มติร่วม E→MB #28 §6ⓐ)

**กฎที่บังคับ**

  ①  `id` ต้องขึ้นต้นด้วย `<setId>-`
  ②  ส่วนท้ายต้องเป็น `<คำนำหน้าเป็นตัวอักษร><ตัวเลข>` เท่านั้น
  ③  ตัวเลขใน `id` ต้องเท่ากับ `questionNumber`
  ④  🔑 **เติมศูนย์กว้างเดียวต่อชุด** — ทุก `id` ต้องเท่ากับ `str(questionNumber).zfill(P)`
      โดย `P` เป็นค่าเดียวของทั้งชุด  ⇒ **นี่คือกฎที่จับอุบัติเหตุ 7 ส.ค. ได้**
      (กว้าง 2 แปลว่า q01…q99 แล้วต่อ q100 ⇒ ⛔ "หลักไม่เท่ากัน" ไม่ใช่ความผิด)
  ⑤  คำนำหน้าเดียวต่อชุด
  ⑥  `id` ห้ามซ้ำกันทั้งคลัง
  ⑦  ทุกข้อในไฟล์เดียวกันต้องมี `setId` เดียวกัน และตรงกับ `setId` บนสุด (ถ้ามี)
  ⑧  ไฟล์ต้องมี `setId` บนสุด

**⛔ ของเก่าที่ยังผิดอยู่ — pin ไว้เป็นรายชื่อ ⛔ ไม่ใช่ตัวเลข**

รายการยกเว้นด้านล่างเป็น **ชื่อเฉพาะเจาะจง** ⇒ ถ้ามีชุดใหม่ผิดแบบเดียวกัน **ด่านแดงทันที**
⛔ ห้ามเติมชื่อใหม่ลงรายการเพื่อให้ด่านเขียว — รายการนี้ย่อได้อย่างเดียว
(ทรงเดียวกับด่าน 10 "รายการอนุญาตห้ามโตเงียบ ๆ")

**วิธีรัน**

    python3 scripts/check_id_shape.py             # ตรวจของจริงในคลัง
    python3 scripts/check_id_shape.py --selftest  # ตรวจตัวด่านเอง (ดี/เสีย/มิวแทนต์)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SETS = ROOT / 'data' / 'sets'

SUFFIX = re.compile(r'^([A-Za-z]*)(\d+)$')

# ── 🔑 ตารางประกาศทรง `id` ต่อชุด — `setId: (คำนำหน้า, ความกว้างเติมศูนย์)` ────
#
#    🔴 **ตารางนี้คือหัวใจของด่าน 20** — ถ้าปล่อยให้ด่านเดาความกว้างจากข้อมูลเอง
#       การเขียนทับ "ทั้งชุดพร้อมกัน" (ซึ่งคืออุบัติเหตุ 7 ส.ค. 69 เป๊ะ ๆ) จะดู**ถูกต้อง**
#       เพราะชุดที่ถูกแก้ยกชุดก็ยัง "สม่ำเสมอ" อยู่ดี ⇒ **ทรงต้องถูกประกาศ ⛔ ไม่ใช่ถูกเดา**
#
#    ความกว้าง 0 = ไม่เติมศูนย์ · 2 = q01…q99 แล้วต่อ q100 · 3 = q001…q999
#    ⛔ แก้ตัวเลขในตารางนี้ = เปลี่ยน id ของทั้งชุด ⇒ ต้องเห็นใน diff และต้องตั้งใจ
#    ⇒ ชุดใหม่ที่ยังไม่อยู่ในตาราง ⇒ **ด่านแดง** (บังคับให้ประกาศ ⛔ ไม่ปล่อยผ่านเงียบ)
SHAPE: dict[str, tuple] = {
    'alvl1-2566-03'                                   : ('q', 2),
    'alvl1-2567-03'                                   : ('q', 2),
    'alvl1-2568-03-v2'                                : ('q', 2),
    'alvl1-2569-03'                                   : ('q', 2),
    'chap-01-set'                                     : ('q', 2),
    'chap-02-logic'                                   : ('q', 2),
    'chap-03-realnumber'                              : ('q', 2),
    'chap-04-coord'                                   : ('q', 2),
    'chap-05-function'                                : ('q', 2),
    'chap-06-matrix'                                  : ('q', 2),
    'chap-07-trigonometry'                            : ('q', 2),
    'chap-08-explog'                                  : ('q', 2),
    'chap-09-vector'                                  : ('q', 2),
    'chap-10-complex'                                 : ('q', 2),
    'chap-11-sequence'                                : ('q', 2),
    'chap-12-probability'                             : ('q', 2),
    'chap-13-calculus'                                : ('q', 2),
    'chap-14-infiniteseries'                          : ('q', 2),
    'chap-15-statistics'                              : ('q', 2),
    'gen-chap-01-set'                                 : ('q', 3),
    'gen-chap-02-logic'                               : ({'P', 'q'}, 3),
    'gen-chap-03-real'                                : ('q', 3),
    'gen-chap-04-coord'                               : ('q', 3),
    'gen-chap-05-function'                            : ('q', 3),
    'gen-chap-07-trigonometry'                        : ('q', 3),
    'gen-chap-09-vector'                              : ('q', 3),
    'gen-chap-12-probability'                         : ('rv', 3),
    'gen-chap-18-interest-and-value-of-money'         : ('q', 2),
    'pat1-2552-03'                                    : ('q', 2),
    'pat1-2552-07'                                    : ('q', 2),
    'pat1-2552-10'                                    : ('q', 2),
    'pat1-2553-03'                                    : ('q', 2),
    'pat1-2553-07'                                    : ('q', 2),
    'pat1-2553-10'                                    : ('q', 2),
    'pat1-2554-03'                                    : ('q', 2),
    'pat1-2554-12'                                    : ('q', 2),
    'pat1-2555-03'                                    : ('q', 2),
    'pat1-2555-10'                                    : ('q', 2),
    'pat1-2556-03'                                    : ('q', 2),
    'pat1-2557-03'                                    : ('q', 2),
    'pat1-2557-04'                                    : ('q', 2),
    'pat1-2557-11'                                    : ('q', 2),
    'pat1-2558-03'                                    : ('q', 2),
    'pat1-2558-10'                                    : ('q', 2),
    'pat1-2559-03'                                    : ('q', 2),
    'pat1-2559-10'                                    : ('q', 2),
    'pat1-2560-03'                                    : ('q', 2),
    'pat1-2561-02'                                    : ('q', 2),
    'pat1-2562-02'                                    : ('q', 2),
    'pat1-2563-02'                                    : ('q', 2),
    'pat1-2564-03'                                    : ('q', 2),
    'pat1-2565-03'                                    : ('q', 2),
    'samn-2555-01'                                    : ('q', 2),
    'samn-2556-01'                                    : ('q', 2),
    'samn-2557-01'                                    : ('q', 2),
    'samn-2558-01'                                    : ('q', 2),
    'samn-2558-12'                                    : ('q', 2),
    'samn-2559-12'                                    : ('q', 2),
    'samn-2561-03'                                    : ('q', 2),
    'samn-2562-03'                                    : ('q', 2),
    'samn-2563-03'                                    : ('q', 2),
    'samn-2564-04'                                    : ('q', 2),
    'samn-2565-03'                                    : ('q', 2),
}


# ── พื้นจำนวนไฟล์ ⛔ ลดไม่ได้ (กับดัก ⑥ : "ไม่มีไฟล์ให้ตรวจ" ≠ "ตรวจแล้วผ่าน") ──
MIN_FILES = 60          # 7 ส.ค. 69 : data/sets มี 63 ไฟล์

# ── ⑧ ไฟล์เก่าที่ยังไม่มี setId บนสุด — pin ด้วยชื่อ ⛔ ไม่ใช่ตัวเลข ──────────
NO_TOP_SETID = {
    'pat1-2553-10.json': 'ไฟล์รุ่นเก่า เป็น {"questions": [...]} ล้วน · setId รายข้อถูกต้องครบ',
    'pat1-2558-10.json': 'ไฟล์รุ่นเก่า เป็น {"questions": [...]} ล้วน · setId รายข้อถูกต้องครบ',
    'pat1-2559-03.json': 'ไฟล์รุ่นเก่า เป็น {"questions": [...]} ล้วน · setId รายข้อถูกต้องครบ',
    'pat1-2560-03.json': 'ไฟล์รุ่นเก่า เป็น {"questions": [...]} ล้วน · setId รายข้อถูกต้องครบ',
}



class Finding(str):
    pass


def load(path: Path):
    d = json.loads(path.read_text(encoding='utf-8'))
    if isinstance(d, dict):
        return d.get('questions', []), d.get('setId')
    return d, None


def check_file(name: str, questions: list, top_setid: str | None,
               shape: dict | None = None) -> list[str]:
    """ตรวจไฟล์เดียว · คืนรายการปัญหา (ว่าง = ผ่าน)"""
    bad: list[str] = []
    if not questions:
        return [f'{name} · ไม่มีข้อเลย']

    # ⑧ setId บนสุด
    if top_setid is None and name not in NO_TOP_SETID:
        bad.append(f'{name} · ⛔ ไม่มี `setId` บนสุด (ถ้าตั้งใจ ให้ pin ชื่อไฟล์ในตัวด่าน)')

    # ⑦ setId รายข้อต้องเป็นค่าเดียว
    sids = {q.get('setId') for q in questions}
    if len(sids) > 1:
        bad.append(f'{name} · ไฟล์เดียวมี `setId` หลายค่า: {sorted(map(str, sids))[:3]}')
        return bad
    sid = sids.pop()
    if sid is None:
        bad.append(f'{name} · ข้อไม่มี `setId`')
        return bad
    if top_setid is not None and sid != top_setid:
        bad.append(f'{name} · `setId` บนสุด ({top_setid}) ≠ ของข้อ ({sid})')

    prefixes: set[str] = set()
    pads: dict[int, list[str]] = {}

    for q in questions:
        qid = q.get('id')
        if not isinstance(qid, str):
            bad.append(f'{name} · มีข้อที่ `id` ไม่ใช่สตริง'); continue

        # ① ขึ้นต้นด้วย setId
        if not qid.startswith(sid + '-'):
            bad.append(f'{name} · `{qid}` ⛔ ไม่ขึ้นต้นด้วย `{sid}-`'); continue

        # ② ทรงส่วนท้าย
        m = SUFFIX.match(qid[len(sid) + 1:])
        if not m:
            bad.append(f'{name} · `{qid}` ส่วนท้ายไม่ใช่ <ตัวอักษร><ตัวเลข>'); continue
        pref, digits = m.group(1), m.group(2)
        prefixes.add(pref)

        # ③ ตัวเลขต้องเท่ากับ questionNumber
        qn = q.get('questionNumber')
        if qn is not None and int(digits) != qn:
            bad.append(f'{name} · `{qid}` เลขใน id = {int(digits)} '
                       f'แต่ `questionNumber` = {qn}')
            continue

        # ④ เก็บความกว้างที่ใช้จริง (เฉพาะข้อที่เลขสั้นกว่าสตริง ⇒ บอกความกว้างได้)
        n = int(digits)
        pads.setdefault(len(digits) if len(digits) > len(str(n)) else 0, []).append(qid)

    # 🔑 ทรงต้องถูก "ประกาศ" ⛔ ไม่ใช่ถูกเดาจากข้อมูล
    shape = SHAPE if shape is None else shape
    if sid not in shape:
        bad.append(f'{name} · ชุด `{sid}` ยังไม่ได้ประกาศทรง `id` ในตาราง SHAPE '
                   f'⇒ เพิ่มบรรทัด {sid!r}: (<คำนำหน้า>, <ความกว้าง>) ก่อน '
                   f'⛔ ด่านนี้ไม่เดาทรงให้')
        return bad
    want_pref, want_pad = shape[sid]
    ok_pref = {want_pref} if isinstance(want_pref, str) else set(want_pref)

    # ⑤ คำนำหน้าต้องอยู่ในที่ประกาศไว้
    extra = prefixes - ok_pref
    if extra:
        bad.append(f'{name} · ชุดนี้ใช้คำนำหน้า {sorted(extra)} ที่ไม่ได้ประกาศไว้ '
                   f'(ประกาศไว้ = {sorted(ok_pref)})')

    # ④ 🔑 เติมศูนย์ต้องตรงกับที่ประกาศ — กฎที่จับอุบัติเหตุ 7 ส.ค. 69
    shown = 0
    for q in questions:
        qid, qn = q.get('id'), q.get('questionNumber')
        if not isinstance(qid, str) or qn is None or not qid.startswith(sid + '-'):
            continue
        m = SUFFIX.match(qid[len(sid) + 1:])
        if not m:
            continue
        want = str(qn).zfill(want_pad) if want_pad else str(qn)
        if m.group(2) != want:
            bad.append(f'{name} · `{qid}` ควรเป็น `{sid}-{m.group(1)}{want}` '
                       f'(ชุดนี้ประกาศเติมศูนย์กว้าง {want_pad or "ไม่เติม"})')
            shown += 1
            if shown >= 2:
                bad.append(f'{name} · … ยังมีอีก ⇒ ทั้งชุดถูกเปลี่ยนทรงหรือเปล่า')
                break
    return bad


def run() -> int:
    if not SETS.is_dir():
        print(f'🔴 ด่าน 20 ตก : ไม่มีโฟลเดอร์ {SETS}')
        return 2
    files = sorted(SETS.glob('*.json'))
    if len(files) < MIN_FILES:
        print(f'🔴 ด่าน 20 ตก : เจอไฟล์ชุด {len(files)} ไฟล์ ⛔ ต้องมีอย่างน้อย {MIN_FILES}')
        print('   ⛔ "ไม่มีไฟล์ให้ตรวจ" ไม่เท่ากับ "ตรวจแล้วผ่าน" (กับดัก ⑥)')
        return 1

    bad: list[str] = []
    seen: dict[str, str] = {}
    total = 0
    for f in files:
        try:
            qs, top = load(f)
        except Exception as e:                                    # noqa: BLE001
            bad.append(f'{f.name} · อ่านไม่ออก : {e}'); continue
        total += len(qs)
        bad += check_file(f.name, qs, top)
        # ⑥ id ห้ามซ้ำทั้งคลัง
        for q in qs:
            qid = q.get('id')
            if isinstance(qid, str):
                if qid in seen:
                    bad.append(f'{f.name} · `{qid}` ซ้ำกับใน {seen[qid]}')
                seen[qid] = f.name

    print(f'📌 ด่าน 20 ตรวจ {len(files)} ชุด · {total:,} ข้อ '
          f'· ประกาศทรงไว้ {len(SHAPE)} ชุด · ยกเว้น setId บนสุด {len(NO_TOP_SETID)} ไฟล์'
          )
    if bad:
        print(f'\n🔴 ด่าน 20 ตก {len(bad)} จุด\n')
        for b in bad[:40]:
            print(f'   · {b}')
        if len(bad) > 40:
            print(f'   … และอีก {len(bad) - 40} จุด')
        return 1
    print('✅ ด่าน 20 ผ่าน — ทรง `id` คงที่ทุกชุด และไม่มี id ซ้ำ')
    return 0


# ── selftest ─────────────────────────────────────────────────────────────────
def _set(sid='gen-x3', pad=3, n=4, pref='q', start=1):
    return [{'id': f'{sid}-{pref}{str(i).zfill(pad)}', 'setId': sid, 'questionNumber': i}
            for i in range(start, start + n)]


TEST_SHAPE = {
    'gen-x3': ('q', 3), 'gen-x2': ('q', 2), 'gen-x0': ('q', 0),
    'gen-chap-02-logic': ({'q', 'P'}, 3),
}


def selftest() -> int:
    fails = 0

    def good(qs, top, note):
        nonlocal fails
        out = check_file('T.json', qs, top, TEST_SHAPE)
        if out:
            print(f'   🔴 กรณีดีกลับแดง : {note} → {out}'); fails += 1

    def bad(qs, top, note, want=None):
        nonlocal fails
        out = check_file('T.json', qs, top, TEST_SHAPE)
        if not out:
            print(f'   🔴 กรณีเสียกลับเขียว : {note}'); fails += 1
        elif want and not any(want in o for o in out):
            print(f'   🔴 จับได้แต่เหตุผลผิด : {note} → {out}'); fails += 1

    # ── กรณีดี ────────────────────────────────────────────────────────────
    good(_set('gen-x3', 3), 'gen-x3', 'เติมศูนย์ 3 หลักตามที่ประกาศ')
    good(_set('gen-x2', 2), 'gen-x2', 'เติมศูนย์ 2 หลักตามที่ประกาศ')
    good(_set('gen-x2', 2, n=4, start=98), 'gen-x2', 'กว้าง 2 แล้วข้ามไป 3 หลัก (q99 → q100)')
    good(_set('gen-x0', 0), 'gen-x0', 'ชุดที่ประกาศว่าไม่เติมศูนย์')

    # ── กรณีเสีย ──────────────────────────────────────────────────────────
    bad(_set('gen-x3', 3), None, 'ไม่มี setId บนสุด และไม่ได้ pin', 'ไม่มี `setId` บนสุด')
    bad(_set('gen-new', 3), 'gen-new', 'ชุดใหม่ที่ยังไม่ประกาศทรง', 'ยังไม่ได้ประกาศทรง')

    # 🔑 มิวแทนต์ของอุบัติเหตุ 7 ส.ค. 69 — เปลี่ยนความกว้าง 3 → 2 **ทั้งชุดพร้อมกัน**
    #    (ฉบับที่เดาทรงจากข้อมูลเองจะปล่อยผ่าน เพราะชุดที่ถูกแก้ยกชุดก็ยัง "สม่ำเสมอ")
    q = _set('gen-x3', 3)
    for it in q:
        it['id'] = f"gen-x3-q{str(it['questionNumber']).zfill(2)}"
    bad(q, 'gen-x3', '🔑 ทั้งชุดถูกเปลี่ยนจากกว้าง 3 เป็นกว้าง 2 (อุบัติเหตุ 7 ส.ค. 69)', 'ควรเป็น')

    q = _set('gen-x3', 3); q[2]['id'] = 'gen-x3-q3'
    bad(q, 'gen-x3', 'บางข้อกว้างไม่เท่าที่ประกาศ', 'ควรเป็น')

    q = _set('gen-x3', 3); q[1]['questionNumber'] = 99
    bad(q, 'gen-x3', 'เลขใน id ไม่ตรง questionNumber', '`questionNumber`')

    q = _set('gen-x3', 3); q[0]['id'] = 'gen-y-q001'
    bad(q, 'gen-x3', 'id ชี้ไปชุดอื่น', 'ไม่ขึ้นต้นด้วย')

    q = _set('gen-x3', 3); q[0]['id'] = 'gen-x3-q001b'
    bad(q, 'gen-x3', 'ส่วนท้ายมีตัวอักษรต่อท้ายตัวเลข', 'ส่วนท้าย')

    q = _set('gen-x3', 3); q[3]['id'] = 'gen-x3-P004'
    bad(q, 'gen-x3', 'คำนำหน้าที่ไม่ได้ประกาศ', 'ไม่ได้ประกาศไว้')

    bad(_set('gen-x3', 3), 'gen-other', 'setId บนสุดไม่ตรงกับของข้อ', 'บนสุด')

    q = _set('gen-x3', 3); q[0]['setId'] = 'gen-z'
    bad(q, None, 'setId รายข้อมีหลายค่า', 'หลายค่า')

    # ── กันจับผิดตัว : ชุดที่ประกาศคำนำหน้าปนไว้ ต้องยังเขียว ───────────────
    sid = 'gen-chap-02-logic'
    q = [{'id': f'{sid}-q{i:03d}', 'setId': sid, 'questionNumber': i} for i in (1, 2)]
    q += [{'id': f'{sid}-P{i:03d}', 'setId': sid, 'questionNumber': i} for i in (281, 282)]
    good(q, sid, 'ชุดที่ประกาศคำนำหน้าปนไว้ ต้องไม่แดง')

    n = 15
    if fails:
        print(f'🔴 selftest ตก {fails} / ~{n} กรณี')
        return 1
    print(f'✅ selftest ผ่าน ~{n} กรณี '
          '(ดี 5 · เสีย 10 · รวมมิวแทนต์ของอุบัติเหตุ 7 ส.ค. 69 ที่ฉบับ "เดาทรงเอง" ปล่อยผ่าน)')
    return 0


if __name__ == '__main__':
    sys.exit(selftest() if '--selftest' in sys.argv else run())

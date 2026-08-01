#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ด่าน 9 · ธง flawedSource ต้องมีหลักฐาน ไม่ใช่แค่มีธง

ที่มา (1 ส.ค. 2569 · มติครูข้อ 3 ในจดหมายพอร์ทัล E→MB #02):
  ข้อ chap-15-statistics-q73 เคยมีคำว่า “เฉลยทางการ=ข้อ4” อยู่ในช่อง notes
  โดย **ไม่มีที่มา** — ไม่มีใครรู้ว่าเอามาจากไหน ตรวจสอบย้อนไม่ได้ แก้ต่อไม่ได้
  ⇒ ตกลงกันว่าต่อไปข้อที่ “ตัวโจทย์เองมีปัญหา” ต้องติดธงเป็นโครงสร้าง
     ไม่ใช่ประโยคลอย ๆ ในช่องข้อความ

  🔴 หัวใจของด่านนี้อยู่ที่คำเดียว: **evidence ห้ามว่าง**
     พอร์ทัลเขียนไว้ตรง ๆ ว่า ธงที่ยอมให้ evidence ว่างได้ = สร้างรูเดิมขึ้นมาใหม่
     ⇒ ด่านนี้จึงไม่ได้ตรวจแค่ว่า “มีคีย์ครบไหม” แต่ตรวจว่า
        ของที่ใส่มานั้น **เป็นหลักฐานจริงหรือแค่ขีดกลาง**

โครงที่บังคับ (สเปกขั้นต่ำจากพอร์ทัล — ห้ามขาด ห้ามเกิน):
  {
    "kind":      หนึ่งใน 4 ค่าที่กำหนดไว้เท่านั้น ⛔ ไม่ใช่สตริงอิสระ
    "note":      ปัญหาคืออะไร (ภาษาคน)
    "evidence":  ที่มาของหลักฐาน ⛔ ห้ามว่าง ⛔ ห้ามเป็นขีดกลาง
    "decidedAt": วันที่ตัดสิน + ใครตัดสิน
  }

🔴 เส้นแบ่งที่ต้องอ่านก่อนติดธงทุกครั้ง (พอร์ทัลรอบ 16 ข้อ 6):
   flawedSource = “แก้ไม่ได้”  ⛔ ไม่ใช่ “ยังไม่ได้แก้”

   ✅ ติดธงได้:  ตัวโจทย์/ตัวเลือกของ **ข้อสอบจริง** มีปัญหาในตัวมันเอง
                (ตอบถูกหลายข้อ · ไม่มีข้อถูก · กำกวม · ข้อเท็จจริงล้าสมัย)
                — ของพวกนี้แก้ไม่ได้เพราะแก้แล้วมันจะไม่ใช่ข้อสอบจริงอีกต่อไป
   ⛔ ห้ามติดธง: เฉลยยังไม่ดี · หมุดรูปยังไม่ครบ · สัญลักษณ์ยังไม่ได้แปลง ·
                คำอธิบายยังไม่ได้เขียน — **ทั้งหมดนี้เป็นของเรา และแก้ได้**
                ⇒ ติดธงให้ของพวกนี้ = เปลี่ยน “หนี้ที่ต้องใช้” ให้กลายเป็น “ข้อยกเว้นถาวร”

   ⚠️ ทำไมต้องเขียนไว้ในโค้ดไม่ใช่ในจดหมาย: วันที่คนจะติดธงผิด คือวันที่ด่านกำลังแดง
      และเขากำลังรีบ — เป็นวันที่เขาอ่านจดหมายเก่าน้อยที่สุด

⛔ ด่านนี้ไม่แตะฟิลด์ accept และไม่แก้ไฟล์ใด ๆ — อ่านอย่างเดียว

⚠️ ข้อจำกัดที่รู้ตัว (เขียนไว้ให้พอร์ทัลเถียงได้):
   ด่านนี้ตัดสิน “รูปร่างของหลักฐาน” ไม่ได้ตัดสิน “หลักฐานนั้นจริงไหม”
   คนที่ตั้งใจโกงยังพิมพ์ประโยคยาว ๆ ที่ไม่มีอยู่จริงได้
   สิ่งที่ด่านนี้กันได้จริงคือ **การเผลอ** — ปล่อยว่าง ใส่ขีดกลาง ใส่ "ยังไม่ระบุ"
   ซึ่งเป็นวิธีที่รูเดิมของ q73 เกิดขึ้นจริง ๆ

รหัสออก: 0 = ผ่าน · 1 = เนื้อหาแดง · 2 = ตัวเครื่องมือแดง
"""
import argparse
import datetime
import glob
import json
import os
import re
import sys

CHECKER_VERSION = '1.1'

FIELD = 'flawedSource'

# 🔴 เส้นแบ่งที่ต้องพิมพ์ "ทุกรอบ" ไม่ใช่เขียนไว้ในหัวไฟล์เฉย ๆ
#    เหตุผล: หัวไฟล์มีคนอ่านตอนแก้โค้ด · log ของ CI มีคนอ่านตอนติดธง
#    ⇒ ข้อความต้องไปโผล่ตรงที่คนกำลังจะตัดสินใจ ไม่ใช่ตรงที่เราเขียนมันไว้
BOUNDARY = (
    '  ┌─ เส้นแบ่งของธงนี้ ───────────────────────────────────────\n'
    '  │ flawedSource = “แก้ไม่ได้” ⛔ ไม่ใช่ “ยังไม่ได้แก้”\n'
    '  │   ✅ โจทย์/ตัวเลือกของข้อสอบจริงที่มีปัญหาในตัวมันเอง\n'
    '  │   ⛔ เฉลย · หมุดรูป · สัญลักษณ์ — ของเราทั้งนั้น แก้ได้ ⇒ ห้ามติดธง\n'
    '  └──────────────────────────────────────────────────────────'
)

# ── 4 ค่าที่พอร์ทัลกำหนด ⛔ ไม่ใช่สตริงอิสระ ────────────────
#    การเพิ่มค่าที่ 5 = เปลี่ยนกติการ่วม ต้องเป็นมติร่วม ไม่ใช่แก้เงียบ ๆ
#    ⚠️ การ "ปักหมุด" ค่าชุดนี้ไว้ในไฟล์เดียวกับที่ใช้มัน คือกับดัก ⑧ อีกหน้าหนึ่ง
#       (กฎที่คุมรอยต่อของรุ่น ไม่ควรอยู่ในรุ่นใดรุ่นหนึ่ง)
#       ⇒ ตัวคุมจริงอยู่ที่ด่าน 10 ใน guards.yml ซึ่งเทียบรายการนี้ที่ HEAD กับที่ฐาน
#          ถ้ารายการโตขึ้นโดยไม่ประกาศในข้อความ commit = แดง
ALLOWED_KINDS = (
    'multiple-correct',   # โจทย์มีคำตอบถูกมากกว่า 1 ข้อ
    'no-correct',         # โจทย์ไม่มีตัวเลือกไหนถูกเลย
    'ambiguous',          # ถ้อยคำอ่านได้ 2 ทาง ตัดสินไม่ขาด
    'outdated-fact',      # เคยถูกในยุคนั้น แต่ข้อเท็จจริงเปลี่ยนไปแล้ว
)

REQUIRED_KEYS = ('kind', 'note', 'evidence', 'decidedAt')

# ⛔ ห้ามมีคีย์นอกรายการ — เพราะคีย์ที่พิมพ์ผิด (evidences / evidenceX)
#    จะกลายเป็น "ไม่มี evidence" แบบเงียบ ๆ ถ้าไม่ตรวจ
ALLOWED_KEYS = set(REQUIRED_KEYS)

# ── กันช่อง evidence ที่ "ไม่ว่างแต่ไม่ใช่หลักฐาน" ───────────
MIN_LEN = {'note': 20, 'evidence': 20}

PLACEHOLDERS = {
    '-', '—', '–', '.', '..', '...', '?', '??',
    'n/a', 'na', 'nil', 'none', 'tbd', 'todo', 'xxx',
    'ไม่มี', 'ไม่ระบุ', 'ไม่ทราบ', 'ดูเฉลย', 'ตามเฉลย', 'ตามที่ครูบอก',
}

# ประโยคที่ "ประกาศว่ายังไม่มีหลักฐาน" — ยาวพอผ่านเกณฑ์ความยาวได้ แต่ไม่ใช่หลักฐาน
PLACEHOLDER_PREFIX = ('ยังไม่', 'รอตรวจ', 'รอหา', 'ไม่แน่ใจ', 'จำได้ว่า', 'น่าจะ')

# ── decidedAt = วันที่จริง + คนตัดสิน ───────────────────────
#    รูปแบบ: "YYYY-MM-DD · ใครก็ตามที่ตัดสิน"
DECIDED_RE = re.compile(r'^(\d{4})-(\d{2})-(\d{2})\s*·\s*(\S.*)$')

# ⚠️ ช่วงปีนี้มีไว้ดัก พ.ศ. โดยเฉพาะ — คลังนี้เขียน พ.ศ. ในเนื้อหาทุกที่
#    ถ้าใครเผลอพิมพ์ 2569-08-01 ลงช่องนี้ ต้องแดง ไม่ใช่ผ่านเงียบ ๆ
YEAR_MIN, YEAR_MAX = 2000, 2099

# ── ชื่อคีย์ที่ "เกือบใช่" ───────────────────────────────────
#    กับดัก ⑥: ของที่คิดว่ายังไม่มี ต้องไปดูก่อน
#    ถ้าใครสะกดชื่อฟิลด์ผิด ด่านนี้จะเขียวตลอดกาลโดยไม่เจออะไรเลย
NEAR_MISS_KEYS = (
    'flawedsource', 'flawed_source', 'flawSource', 'flawedSources',
    'flawedsources', 'FlawedSource', 'flawed-source', 'flawedSrc',
)


def check_one(fs):
    """ตรวจ 1 ธง — คืนรายการปัญหา [(รหัส, ข้อความ)] · ว่าง = ผ่าน

    ⛔ คืน "รหัสปัญหา" ไม่ใช่แค่ข้อความ เพราะ self-test ต้องพิสูจน์ได้ว่า
       เคสหนึ่ง ๆ แดง **ด้วยเหตุผลที่ตั้งใจ** ไม่ใช่บังเอิญแดงด้วยเหตุอื่น
       (กับดัก ⑦ข ที่พอร์ทัลเสนอมาในจดหมาย E→MB #02)
    """
    p = []
    if not isinstance(fs, dict):
        return [('not-dict', f'{FIELD} ต้องเป็นวัตถุ (dict) ไม่ใช่ {type(fs).__name__}')]

    for k in sorted(set(fs) - ALLOWED_KEYS):
        p.append(('unknown-key:' + k,
                  f'คีย์แปลกปลอม “{k}” — ถ้าตั้งใจเพิ่มช่องใหม่ ต้องไปเพิ่มใน '
                  f'ALLOWED_KEYS ของด่าน 9 ด้วย (ตั้งใจให้ต้องแตะสองที่)'))

    for k in REQUIRED_KEYS:
        if k not in fs:
            p.append(('missing:' + k, f'ขาดช่อง “{k}”'))

    # ── kind ──
    if 'kind' in fs:
        v = fs['kind']
        if not isinstance(v, str):
            p.append(('not-string:kind', 'kind ต้องเป็นสตริง'))
        elif v not in ALLOWED_KINDS:
            p.append(('kind-not-allowed',
                      f'kind = “{v}” ไม่อยู่ใน 4 ค่าที่ตกลงกัน '
                      f'({" · ".join(ALLOWED_KINDS)}) ⛔ ไม่ใช่สตริงอิสระ'))

    # ── note / evidence ──
    for k in ('note', 'evidence'):
        if k not in fs:
            continue
        v = fs[k]
        if not isinstance(v, str):
            p.append(('not-string:' + k, f'{k} ต้องเป็นสตริง'))
            continue
        s = v.strip()
        if not s:
            p.append(('empty:' + k,
                      f'{k} ว่าง ⛔ ธงที่ยอมให้ {k} ว่าง = สร้างรูเดิมของ q73 ขึ้นมาใหม่'))
            continue
        low = s.casefold()
        if low in PLACEHOLDERS or low.startswith(PLACEHOLDER_PREFIX):
            p.append(('placeholder:' + k,
                      f'{k} = “{s[:30]}” เป็นคำแทนที่ ไม่ใช่หลักฐาน'))
            continue
        if len(s) < MIN_LEN[k]:
            p.append(('too-short:' + k,
                      f'{k} ยาว {len(s)} ตัวอักษร — ต่ำกว่าเกณฑ์ {MIN_LEN[k]} '
                      f'(ที่มาจริงไม่มีทางสั้นกว่านี้)'))

    # ── decidedAt ──
    if 'decidedAt' in fs:
        v = fs['decidedAt']
        if not isinstance(v, str):
            p.append(('not-string:decidedAt', 'decidedAt ต้องเป็นสตริง'))
        else:
            m = DECIDED_RE.match(v.strip())
            if not m:
                p.append(('decidedAt-format',
                          f'decidedAt = “{v}” ต้องเป็น "YYYY-MM-DD · ใครตัดสิน" '
                          f'— วันที่อย่างเดียวตอบไม่ได้ว่าใครรับผิดชอบ'))
            else:
                y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
                if not (YEAR_MIN <= y <= YEAR_MAX):
                    p.append(('decidedAt-year-range',
                              f'ปี {y} อยู่นอกช่วง {YEAR_MIN}–{YEAR_MAX} '
                              f'— ช่องนี้ใช้ ค.ศ. (เผลอพิมพ์ พ.ศ. หรือเปล่า)'))
                else:
                    try:
                        datetime.date(y, mo, d)
                    except ValueError:
                        p.append(('decidedAt-not-a-date',
                                  f'“{m.group(0)[:10]}” ไม่ใช่วันที่ที่มีอยู่จริง'))
    return p


# ═════════════════════════════════════════════════════════════
#  SELF-TEST — ตัวอย่างดี/เสียฝังในตัว + มิวแทนต์
# ═════════════════════════════════════════════════════════════
GOOD = {
    'kind': 'multiple-correct',
    'note': 'ตัวเลือก 2 และตัวเลือก 4 ผิดทั้งคู่ ทำให้ข้อนี้มีข้อความผิด 2 ข้อ',
    'evidence': 'ลำดับปีสำมะโนของสำนักงานสถิติแห่งชาติ — สำมะโนอุตสาหกรรม 2507 · 2540 · 2550',
    'decidedAt': '2026-08-01 · ครู QC',
}


def _g(**over):
    """สำเนาของดี แล้วทับเฉพาะช่องที่ระบุ (None = ลบช่องนั้นทิ้ง)"""
    d = dict(GOOD)
    for k, v in over.items():
        if v is None:
            d.pop(k, None)
        else:
            d[k] = v
    return d


# (ชื่อเคส, ธง, ต้องผ่านไหม, รหัสปัญหาที่ต้องเจอ)
#  ⛔ ระบุ "รหัสที่ต้องเจอ" ทุกเคสที่ต้องแดง — ไม่ใช่แค่ "แดงก็พอ"
#     เพราะแดงด้วยเหตุผลอื่นคือด่านที่หลอกตัวเอง (กับดัก ⑦ข)
CASES = [
    ("ธงของ q73 ครบถ้วน ⇒ ต้องผ่าน", GOOD, True, None),

    ("kind อีกค่าที่อนุญาต (no-correct) ⇒ ต้องผ่าน",
     _g(kind='no-correct'), True, None),

    ("มีช่องว่างหัวท้าย ⇒ ยังต้องผ่าน (ไม่จู้จี้เกินเหตุ)",
     _g(evidence='  ' + GOOD['evidence'] + '  '), True, None),

    ("🔴 evidence ว่าง — รูเดิมของ q73 ⇒ ต้องแดง",
     _g(evidence=''), False, 'empty:evidence'),

    ("🔴 evidence เป็นขีดกลาง ⇒ ต้องแดง (ไม่ว่าง แต่ไม่ใช่หลักฐาน)",
     _g(evidence='-'), False, 'placeholder:evidence'),

    ("🔴 evidence = “ยังไม่ได้ตรวจสอบที่มาของข้อมูลชุดนี้” ⇒ ต้องแดง (ยาวพอ แต่ประกาศเองว่าไม่มี)",
     _g(evidence='ยังไม่ได้ตรวจสอบที่มาของข้อมูลชุดนี้'), False, 'placeholder:evidence'),

    ("🔴 evidence สั้นเกินจะเป็นที่มา ⇒ ต้องแดง",
     _g(evidence='ครูบอก'), False, 'too-short:evidence'),

    ("🔴 kind เป็นสตริงอิสระภาษาไทย ⇒ ต้องแดง",
     _g(kind='เฉลยมีปัญหา'), False, 'kind-not-allowed'),

    ("🔴 kind สะกดเกือบถูก (เว้นวรรคแทนขีด) ⇒ ต้องแดง",
     _g(kind='multiple correct'), False, 'kind-not-allowed'),

    ("🔴 ขาดช่อง note ⇒ ต้องแดง",
     _g(note=None), False, 'missing:note'),

    ("🔴 คีย์พิมพ์ผิดเป็น evidences ⇒ ต้องแดงที่ 'คีย์แปลกปลอม'",
     _g(evidence=None, evidences=GOOD['evidence']), False, 'unknown-key:evidences'),

    ("🔴 คีย์พิมพ์ผิดเป็น evidences ⇒ และต้องแดงที่ 'ขาด evidence' ด้วย",
     _g(evidence=None, evidences=GOOD['evidence']), False, 'missing:evidence'),

    ("🔴 decidedAt มีแต่วันที่ ไม่มีคนตัดสิน ⇒ ต้องแดง",
     _g(decidedAt='2026-08-01'), False, 'decidedAt-format'),

    ("🔴 decidedAt เป็น พ.ศ. ⇒ ต้องแดง (คลังนี้เขียน พ.ศ. ทุกที่ จะเผลอแน่)",
     _g(decidedAt='2569-08-01 · ครู QC'), False, 'decidedAt-year-range'),

    ("🔴 decidedAt วันที่ไม่มีอยู่จริง (30 ก.พ.) ⇒ ต้องแดง",
     _g(decidedAt='2026-02-30 · ครู QC'), False, 'decidedAt-not-a-date'),

    ("🔴 note มีคีย์อยู่แต่ค่าเป็น null ⇒ ต้องแดงที่ 'ไม่ใช่สตริง' ไม่ใช่ล้มทั้งด่าน",
     dict(GOOD, note=None), False, 'not-string:note'),

    ("🔴 ธงเป็นสตริงทั้งก้อน ⇒ ต้องแดงที่ 'ไม่ใช่ dict'",
     'ข้อนี้เฉลยมีปัญหา', False, 'not-dict'),

    ("🔴 ธงเป็นลิสต์ ⇒ ต้องแดงที่ 'ไม่ใช่ dict'",
     [GOOD], False, 'not-dict'),

    ("🔴 ธงว่างเปล่า ⇒ ต้องแดงครบทั้ง 4 ช่อง",
     {}, False, 'missing:evidence'),
]


def _mut_evidence_optional(fs):
    """มิวแทนต์ ① ยอมให้ evidence ว่าง ⇒ รูเดิมของ q73 กลับมาทั้งดุ้น"""
    return [(c, m) for c, m in check_one(fs)
            if not c.startswith(('empty:evidence', 'placeholder:evidence',
                                 'too-short:evidence'))]


def _mut_kind_free_string(fs):
    """มิวแทนต์ ② ให้ kind เป็นสตริงอิสระ ⇒ รายการ 4 ค่ากลายเป็นคำแนะนำ"""
    return [(c, m) for c, m in check_one(fs) if c != 'kind-not-allowed']


def _mut_allow_unknown_keys(fs):
    """มิวแทนต์ ③ ปล่อยคีย์แปลกปลอม ⇒ evidences ที่พิมพ์ผิดจะเงียบ"""
    return [(c, m) for c, m in check_one(fs) if not c.startswith('unknown-key:')]


def _mut_shape_only(fs):
    """มิวแทนต์ ④ ตรวจแค่ว่า 'มีคีย์ครบ' ⇒ ธงมีรูปร่างถูก แต่ข้างในเป็นขีดกลางได้"""
    if not isinstance(fs, dict):
        return [('not-dict', '')]
    return [('missing:' + k, '') for k in REQUIRED_KEYS if k not in fs]


def _mut_always_ok(fs):
    """มิวแทนต์ ⑤ ไม่ตรวจอะไรเลย ⇒ กติกากลับไปอยู่แต่ในจดหมาย"""
    return []


def _run_cases(fn):
    """คืนรายชื่อเคสที่ล้มเมื่อใช้ fn เป็นตัวตรวจ"""
    fails = []
    for name, fs, want_ok, want_code in CASES:
        try:
            codes = [c for c, _ in fn(fs)]
            good = (len(codes) == 0) == want_ok
            if good and want_code is not None:
                good = want_code in codes
        except Exception:
            good = False
        if not good:
            fails.append(name)
    return fails


def selftest():
    print('─' * 62)
    print(f'SELF-TEST ด่าน 9 v{CHECKER_VERSION} — ธง {FIELD} ต้องมีหลักฐาน')
    print('─' * 62)
    ok = True

    print(f'  รายการ kind ที่อนุญาต ({len(ALLOWED_KINDS)} ค่า): '
          + ' · '.join(ALLOWED_KINDS))
    print('  (พิมพ์ออกมาทุกรอบ เพื่อให้การขยายรายการนี้เห็นได้ใน log ของ CI)')
    print(BOUNDARY)
    print()

    for name, fs, want_ok, want_code in CASES:
        codes = [c for c, _ in check_one(fs)]
        good = (len(codes) == 0) == want_ok
        why = ''
        if good and want_code is not None:
            good = want_code in codes
            if not good:
                why = f'   ← แดงจริง แต่ด้วยรหัส {codes} ไม่ใช่ {want_code}'
        print(f'  {"✅" if good else "🔴"}  {name}{why}')
        ok &= good

    print()
    print('  ── ใส่บั๊กเข้าไปแล้วด่านต้องล้ม (ด่านต้องมีคนเฝ้า) ──')
    print('     ⑦ข: แดงแล้วยังต้องถามต่อว่า “แดงเพราะเคสที่ตั้งใจหรือเปล่า”')
    for label, fails in (
        ('① ยอมให้ evidence ว่าง/เป็นขีดกลาง', _run_cases(_mut_evidence_optional)),
        ('② ให้ kind เป็นสตริงอิสระ',           _run_cases(_mut_kind_free_string)),
        ('③ ปล่อยคีย์แปลกปลอม',                _run_cases(_mut_allow_unknown_keys)),
        ('④ ตรวจแค่ “มีคีย์ครบ”',              _run_cases(_mut_shape_only)),
        ('⑤ ไม่ตรวจอะไรเลย',                   _run_cases(_mut_always_ok)),
    ):
        good = len(fails) > 0
        print(f'  {"✅" if good else "🔴"}  มิวแทนต์ {label} ⇒ ล้ม {len(fails)}/{len(CASES)} เคส')
        for f in fails[:2]:
            print(f'         ↳ จับได้ที่: {f}')
        ok &= good

    print()
    # ── ตรวจตัวรายการค่าคงที่เอง — กันด่านตาบอดเงียบ ──
    if not ALLOWED_KINDS or not REQUIRED_KEYS or not PLACEHOLDERS:
        print('  🔴 รายการค่าคงที่ว่าง ⇒ ด่านนี้จะเขียวตลอดกาลโดยไม่ตรวจอะไร')
        ok = False
    else:
        print(f'  ✅  รายการค่าคงที่ไม่ว่าง (kind {len(ALLOWED_KINDS)} · '
              f'ช่องบังคับ {len(REQUIRED_KEYS)} · คำแทนที่ {len(PLACEHOLDERS)})')

    print()
    if not ok:
        print('🔴 SELF-TEST ไม่ผ่าน ⇒ ผลของด่านนี้กับไฟล์จริงเชื่อไม่ได้')
        return 2
    print(f'✅ SELF-TEST ผ่านครบ {len(CASES)} เคส + มิวแทนต์ 5 ตัว')
    return 0


def scan(sets_dir):
    """คืน (bad[], near[], n_flag, n_q)"""
    bad, near = [], []
    n_flag = n_q = 0
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
        b = os.path.basename(f)
        for q in d.get('questions', []):
            if not isinstance(q, dict):
                continue
            n_q += 1
            qid = q.get('id', '(ไม่มี id)')
            for k in NEAR_MISS_KEYS:
                if k in q:
                    near.append((b, qid, k))
            if FIELD in q:
                n_flag += 1
                for code, msg in check_one(q[FIELD]):
                    bad.append((b, qid, code, msg))
    return bad, near, n_flag, n_q


def main():
    ap = argparse.ArgumentParser(
        description='ตรวจว่าธง flawedSource ทุกอันมีหลักฐานจริง ไม่ใช่แค่มีธง')
    ap.add_argument('sets_dir', nargs='?', default='data/sets')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    a = ap.parse_args()

    if a.version:
        print(CHECKER_VERSION)
        return 0
    if a.selftest:
        return selftest()

    bad, near, n_flag, n_q = scan(a.sets_dir)

    print(f'ตรวจ {a.sets_dir} · {n_q} ข้อ · ติดธง {FIELD} ทั้งหมด {n_flag} ข้อ')
    print(f'  รายการ kind ที่อนุญาต: ' + ' · '.join(ALLOWED_KINDS))
    print(BOUNDARY)
    print()

    if near:
        print(f'🔴 พบชื่อฟิลด์ที่ “เกือบใช่” {len(near)} จุด — ธงที่สะกดผิดคือธงที่ไม่มีใครตรวจ:')
        for b, qid, k in near[:20]:
            print(f'   {b} · {qid} · คีย์ “{k}” ⇒ ต้องเป็น “{FIELD}”')
        print()

    if bad:
        print(f'🔴 ธง {FIELD} ที่ไม่ผ่าน {len(bad)} จุด:')
        cur = None
        for b, qid, code, msg in bad:
            if qid != cur:
                print(f'   ── {b} · {qid}')
                cur = qid
            print(f'      [{code}] {msg}')
        print()
        print('วิธีแก้: เติมให้ครบตามโครงนี้')
        print('  "flawedSource": {')
        print('    "kind": "multiple-correct",        ⛔ หนึ่งใน '
              + ' · '.join(ALLOWED_KINDS))
        print('    "note": "ปัญหาของข้อนี้คืออะไร",')
        print('    "evidence": "ที่มาที่ตรวจย้อนได้",  ⛔ ห้ามว่าง ห้ามเป็นขีดกลาง')
        print('    "decidedAt": "2026-08-01 · ครู QC"')
        print('  }')
        return 1

    if near:
        return 1

    print(f'✅ ธง {FIELD} ทุกอันมีครบทั้ง 4 ช่อง และ evidence ไม่ว่าง')
    if n_flag == 0:
        print('   (รอบนี้ยังไม่มีข้อไหนติดธง — ด่านนี้จึงยังไม่ได้ตรวจอะไรจริง ๆ')
        print('    แต่ตัวดักชื่อฟิลด์ที่สะกดผิดทำงานแล้ว จึงไม่ใช่ความเขียวแบบตาบอด)')
    return 0


if __name__ == '__main__':
    # ⛔ ต้องเป็น sys.exit(main()) — บั๊กจริง 1 ส.ค. 69 ในไฟล์พี่น้องกัน:
    #    เขียน main() เฉย ๆ แล้วรหัสออกถูกกลืน เชลล์เห็น 0 ทั้งที่ตั้งใจคืน 2
    sys.exit(main())

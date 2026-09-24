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

v1.1 (1 ส.ค. 69) — ชั้นบังคับตามขอบเขต diff (มติพอร์ทัล E→MB #02 ข้อ 2)
  พอร์ทัลรับทางเลือก (ก) "ปล่อยหนี้เก่าไว้ที่ 66.3% + บังคับเฉพาะข้อที่แต่งใหม่"
  พร้อมเงื่อนไขว่า **ต้องเป็นด่านจริง ไม่ใช่ข้อตกลงในจดหมาย**
  ⇒ โหมด --enforce-declared: ข้อที่ "เปลี่ยนในรอบนี้" ต้องประกาศเลขตัวเลือกได้
     ข้อเก่าไม่แดง · ข้อใหม่ที่ไม่ประกาศ = แดง
  ⛔ ด่านนี้ (ด่าน 8) ไม่ตัดสินเรื่อง "เฉลยขัดคีย์" — นั่นเป็นงานของด่าน 7
     แยกกันเพื่อให้ตอบได้ทันทีว่า "แดงเพราะด่านไหน" (บทเรียนข้อ ๘ ของรอบ 14)
  ⛔ รายชื่อ "ข้อที่เปลี่ยนรอบนี้" ไม่ได้คำนวณในไฟล์นี้ — รับมาจาก
     scan_symbols.py --print-changed-ids เพื่อให้มีที่เดียวที่ตอบคำถามนี้

v1.4 (23 ก.ย. 69) — ㉝ อ่าน "ข้อ N" ในบรรทัดคำตอบเป็นคำประกาศด้วย
  มติครู 23 ก.ย. ③ (ใบ 400) · regex ㉝ MB-v1 (ใบ 397 §4 · E วัดซ้ำตรงทุกช่องในใบ 398 §1)
  ที่มา: เฉลยจำนวนมากสรุปว่า "✅ คำตอบ: ข้อ 4" โดยไม่มีคำว่า "ตัวเลือก"
         ⇒ v1.3 นับเป็น 'none' ⇒ ด่าน 7 มองไม่เห็น ทั้งที่เฉลยประกาศชัด
  ข้อบังคับ (สองเลนตกลงกันแล้ว):
    · หน่วย = บรรทัด เหมือนเดิม ⛔ ห้ามอ่านทั้งก้อน (ชุดทดสอบใบ 391 §2 เฝ้าไว้)
    · (ข) บรรทัดที่มี "ตัวเลือก N" ⇒ ตัวเลือกชนะ ⛔ ไม่อ่าน "ข้อ" ในบรรทัดนั้น
    · (ก) "ข้อ N" ที่ N > จำนวนตัวเลือก ⇒ ⛔ ไม่อ่าน
    · (ค) หลายเลข ⇒ 'many' เหมือนเดิม
    · ⛔ ไม่ตัดแท็ก HTML ก่อนอ่าน — `<` ในสูตรทำให้ `<[^>]+>` กลืน "ตัวเลือก N" (ใบ 398 §3)
  ⬜ ยังไม่ใส่ (ฉ) "โจทย์ที่พูดถึงข้อสอบ ⇒ ไม่อ่าน" (8 ข้อทั้งคลัง · ใส่แล้วหนี้ขึ้น ≤ 8)
  positive control (กฎ ⑪): ปิด ALT_RE ⇒ ต้องได้ one 3,012 · many 42 · none 1,382
                          = v1.3 ทุกช่อง บนฐาน b8d0344 (มิวแทนต์ ⑦ ในตัวนี้คือโค้ดชุดนั้น)

รหัสออก: 0 = ผ่าน · 1 = เนื้อหาแดง · 2 = ตัวเครื่องมือแดง
"""
import argparse
import json
import glob
import os
import re
import sys

CHECKER_VERSION = '1.4'

# ── เพดานหนี้ "ตรวจไม่ได้" — ratchet เดียว ⛔ ไม่ใช่สองตัว ─────────────
#
# 🔴 ทำไมเป็นเลขตัวเดียว ไม่ใช่ "หลายเลข 42" กับ "ไม่ประกาศ 1,382" แยกกัน:
#    ถ้าเฝ้าแยกสองถัง คนแก้ย้ายหนี้ข้ามถังได้ฟรี — แก้ข้อ "ไม่ประกาศ" ให้กลายเป็น
#    "ประกาศหลายเลข" แล้วถังหนึ่งลด อีกถังโต ⇒ ทั้งสองด่านเขียว ทั้งที่ยังตรวจไม่ได้เหมือนเดิม
#    ⇒ ของที่เราสนใจจริงคือ "จำนวนข้อที่ด่าน 7 มองไม่เห็น" ซึ่งเป็นผลบวกของสองถัง
#
# ⚠️ เลข 1,424 นี้ ⛔ ไม่ใช่เป้าหมาย — เป็น "ที่ที่เรายืนอยู่วันนี้" (1 ส.ค. 69 · 538d4d4)
#    42 + 1,382 = 1,424 จากข้อปรนัยที่มีคีย์และเฉลย 4,221 ข้อ
#    ทุกครั้งที่ยอดลดลงจริง ให้ปรับเพดานลงตาม ⇒ ratchet เดินลงทางเดียว
#
# 🆕 v1.4 (23 ก.ย. 69 · ㉝ · มติครู ③): 1,424 → 1,097
#    ⬤ วัดบนฐาน b8d0344: one 3,339 · many 67 · none 1,030 ⇒ หนี้ 1,097 · ตัวหาร 4,436 · แดง 0
#    ⛔ หนี้ลดเพราะ "ด่านมองเห็นมากขึ้น" ⛔ ไม่ใช่เพราะมีคนเติมบรรทัดสรุป — สองอย่างนี้ห้ามปนกัน
#    ⇒ ratchet เดินลงทางเดียวเหมือนเดิม ⛔ ห้ามขยับขึ้น
MAX_UNDECLARED = 1097

# ── ⑨ ตัวหาร: "หนี้ 1,424" จากคลัง 4,221 ข้อ ต่างจาก "หนี้ 1,424" จากคลัง 1,500 ข้อ ──
# ถ้าไฟล์ชุดหายไปครึ่งคลัง หนี้จะ "ลดลง" เอง แล้วด่านนี้จะเขียว ⇒ ต้องมีพื้นของตัวหาร
MIN_ELIGIBLE = 4000

# ── บรรทัดที่ถือว่า "ประกาศคำตอบ" ────────────────────────────
ANSWER_MARKERS = ('✅', 'คำตอบ:', 'คำตอบคือ', 'จึงตอบ', 'ดังนั้นตอบ')

# ── บรรทัดที่พูดถึง "ตัวลวง" โดยเจตนา — ไม่ใช่คำประกาศคำตอบ ──
#    ⚠️ นี่คือจุดตาบอดที่ยอมรับไว้อย่างรู้ตัว:
#       ถ้าใครเขียนคำตอบจริงไว้ในบรรทัดที่มีคำเหล่านี้ ด่านจะไม่เห็น
#       แลกมากับการที่ด่านตรวจได้เพิ่ม 70 ข้อ และเสียงหลอกลดจาก 15 เหลือ 0
DISTRACTOR_MARKERS = ('จุดพลาด', 'เผลอ', 'ตัวลวง', 'มักตอบ',
                      'หากตอบ', 'ถ้าตอบ', 'ผิดตรง', 'ดักไว้')

CHOICE_RE = re.compile(r'ตัวเลือก\s*(\d+)')

# 🆕 v1.4 ㉝ — "ข้อ N" ในบรรทัดคำตอบ (อ่านเฉพาะบรรทัดที่ไม่มี "ตัวเลือก N")
#    lookahead ปิดช่วงแบบ "ข้อ 1-4" / "ข้อ 1–4" ⛔ ไม่ให้อ่านเป็นคำประกาศ
#    ⚠️ รู้ไว้ 2 ข้อ (MB ใบ 403):
#       ① lookahead ⛔ ไม่ได้ปิด "ข้อ 50%" — ตัวที่ปิดคือกฎ (ก) N > จำนวนตัวเลือก
#       ② ช่วงเลขสองหลัก "ข้อ 12-14" จะถูกย้อนรอยจนอ่านได้ "1"
#          ⬤ วัดบนฐาน b8d0344: กระทบ 0 บรรทัด · 0 ข้อ ⇒ คงไว้ตาม MB-v1 ที่ครูเคาะ ⛔ ไม่แก้เงียบ
ALT_RE = re.compile(r'ข้อ\s*(\d+)(?!\s*[%–\-]\s*\d)')

# เพดานล่างของความครอบคลุม — ⛔ กันด่านตาบอดเงียบ
#   ถ้าใครลบคำในสองรายการข้างบนจนหมด ด่านจะเขียวตลอดกาลโดยไม่ตรวจอะไรเลย
#   ⇒ บังคับว่าต้องตรวจได้จริงอย่างน้อยเท่านี้ ไม่งั้นถือว่าตัวด่านพัง (รหัส 2)
DEFAULT_MIN_COVERAGE = 0.50


def declared_choice(explanation, n_choices=None):
    """คืน (สถานะ, เลขตัวเลือกที่เฉลยประกาศ)

    สถานะ: 'one'  = ประกาศเลขเดียวชัดเจน ⇒ ตรวจได้
           'many' = ประกาศหลายเลขในบรรทัดคำตอบ ⇒ ตัดสินไม่ได้ ข้ามไป
           'none' = ไม่ประกาศเลขเลย ⇒ ตรวจไม่ได้ ข้ามไป
    ⛔ "ตรวจไม่ได้" ไม่เท่ากับ "ตรวจแล้วผ่าน" — จึงแยกสถานะออกมา ไม่ยุบเป็น None

    n_choices (v1.4) = จำนวนตัวเลือกของข้อ · None ⇒ ไม่กรองด้วยกฎ (ก)
    """
    nums = set()
    for line in explanation:
        if not isinstance(line, str):
            continue
        if any(k in line for k in DISTRACTOR_MARKERS):
            continue
        if not any(k in line for k in ANSWER_MARKERS):
            continue
        c = {int(m) for m in CHOICE_RE.findall(line)}
        if c:                              # (ข) ตัวเลือกชนะ ⛔ ไม่อ่าน "ข้อ" ในบรรทัดนี้
            nums |= c
            continue
        nums |= {int(m) for m in ALT_RE.findall(line)            # 🆕 v1.4 ㉝
                 if not n_choices or int(m) <= n_choices}        # (ก) N > จำนวนตัวเลือก ⇒ ⛔ ไม่อ่าน
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


def is_blind(q):
    """ข้อที่ "มีคีย์และมีเฉลย" แต่ด่านนี้มองไม่เห็นเพราะไม่ใช่ปรนัย

    ⛔ นี่ไม่ใช่ข้อบกพร่องของข้อ — เป็นข้อบกพร่องของ *ตัวด่าน* ที่ต้องประกาศทุกครั้ง
       (จดหมายพอร์ทัล E→MB #22 ข้อ ③ สั่งไว้)
    """
    return (not eligible(q)
            and q.get('type') != 'mc'
            and q.get('correct') not in (None, '')
            and isinstance(q.get('explanation'), list)
            and len(q['explanation']) > 0)


def scan(sets_dir, fn=declared_choice):
    """คืน (bad[], stat{}, recs[])

    recs = [(ชื่อไฟล์, รหัสข้อ, สถานะ)] ของทุกข้อที่เข้าข่ายตรวจ
           ⇒ ชั้นบังคับ (v1.1) ใช้รายการนี้ ไม่ต้องเดินไฟล์ซ้ำ
    """
    bad = []
    recs = []
    # 🔴 'blind' = ข้อที่ "มีคีย์และมีเฉลย" แต่ eligible() ไม่รับ เพราะไม่ใช่ปรนัย
    #    ⇒ ข้อชนิด fill ทุกข้อในคลัง ตกอยู่ในถังนี้ทั้งหมด
    #    ⛔ ห้ามยุบเข้ากับ 'none' — "ไม่เคยถูกมอง" ต่างจาก "มองแล้วอ่านค่าไม่ได้"
    stat = {'eligible': 0, 'one': 0, 'many': 0, 'none': 0, 'blind': 0}
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
                if is_blind(q):
                    stat['blind'] += 1
                continue
            stat['eligible'] += 1
            ch = q.get('choices')
            kind, val = fn(q['explanation'], len(ch) if isinstance(ch, list) else None)
            stat[kind] += 1
            recs.append((os.path.basename(f), q.get('id'), kind))
            if kind == 'one' and val != q['correct'] + 1:
                bad.append((os.path.basename(f), q.get('id'), val, q['correct'] + 1))
    return bad, stat, recs


# ── ชั้นบังคับ v1.1 ──────────────────────────────────────────
def enforce_verdict(recs, scope_ids):
    """คืนรายการข้อที่ต้องแดงเพราะ "เปลี่ยนในรอบนี้แต่ประกาศเลขตัวเลือกไม่ได้"

    scope_ids = None      ⇒ บังคับทั้งคลัง (ใช้ตรวจด้วยมือ — วันนี้จะแดงเป็นพันข้อ)
    scope_ids = เซตว่าง   ⇒ รอบนี้ไม่มีข้อไหนเปลี่ยน ⇒ ไม่มีอะไรให้บังคับ
    ⛔ เซตว่าง กับ None ต้องไม่ยุบเป็นค่าเดียวกัน
       "ไม่มีข้อเปลี่ยน" ≠ "ไม่ได้จำกัดขอบเขต" (กับดัก ⑥)
    ⛔ 'many' ก็ต้องแดง — เพราะจุดประสงค์คือ "ตรวจได้จริง" ไม่ใช่ "มีคำว่าตัวเลือก"
    """
    out = []
    for fname, qid, kind in recs:
        if scope_ids is not None and qid not in scope_ids:
            continue
        if kind != 'one':
            out.append((fname, qid, kind))
    return out


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


# 🆕 v1.4 ㉝ — (ชื่อเคส, explanation, จำนวนตัวเลือก, correct, ต้องแดงไหม, สถานะที่ต้องได้)
#  ⛔ แยกจาก CASES เพราะต้องพกจำนวนตัวเลือก (กฎ (ก)) · ทุกเคสมีมิวแทนต์เฝ้า ⑦–⑪
ALT_CASES = [
    ("㉝ บรรทัดคำตอบเขียน 'ข้อ N' ตรงคีย์ ⇒ ตรวจได้ (ทรงของ gen-chap-02-logic-q246)",
     _ex('✅ คำตอบ: ข้อ 4 คือ $(p\\wedge r)\\vee q$'), 4, 3, False, 'one'),

    ("🔴 ㉝ ของเสียที่ต้องจับได้ · 'ข้อ W' ≠ คีย์ ⇒ ต้องแดง (ใบ 400 §2 ②)",
     _ex('<b>✅ คำตอบ ข้อ 2</b>'), 4, 0, True, 'one'),

    ("㉝ (ข) มี 'ตัวเลือก N' ในบรรทัดเดียวกัน ⇒ ตัวเลือกชนะ ⛔ ไม่อ่าน 'ข้อ'",
     _ex('✅ คำตอบ: ตัวเลือก 2 (แทนค่าในข้อ 3 แล้วไม่จริง)'), 4, 1, False, 'one'),

    ("㉝ (ก) 'ข้อ N' ที่ N เกินจำนวนตัวเลือก ⇒ ⛔ ไม่อ่าน",
     _ex('✅ คำตอบ: ผ่านเงื่อนไขข้อ 12 ของโจทย์'), 4, 0, False, 'none'),

    ("㉝ ช่วง 'ข้อ 1–4' / 'ข้อ 1-4' ⛔ ไม่ใช่คำประกาศ",
     _ex('✅ คำตอบ: ตรวจครบข้อ 1–4 แล้ว ได้ $x=2$',
         '✅ คำตอบ: ข้อ 1-4 ใช้ได้ทุกข้อ'), 4, 1, False, 'none'),

    ("㉝ หน่วย = บรรทัด · 'ข้อ N' ในบรรทัดที่ไม่มีคำประกาศ ⛔ ห้ามนับ (ด่านกันการอ่านทั้งก้อน · ใบ 391 §2)",
     _ex('<b>✔ ตรวจคำตอบ</b>',
         'ข้อ 2 ผิดเพราะแทนค่าแล้วไม่จริง',
         '<b>✅ คำตอบ: ข้อ 4</b>'), 4, 3, False, 'one'),

    ("㉝ บรรทัดตัวลวงที่มี 'ข้อ N' และคำประกาศปนอยู่ ⛔ ห้ามนับ",
     _ex('✅ คำตอบ: ข้อ 1',
         '⚠️ จุดพลาด: มักตอบข้อ 3 เพราะคิดว่าคำตอบคือค่าบวก'), 4, 0, False, 'one'),

    ("㉝ หลายเลขในบรรทัดคำตอบ ⇒ 'many' (ตัดสินไม่ได้)",
     _ex('✅ คำตอบ: ข้อ 1 และ ข้อ 3 ถูก'), 4, 0, False, 'many'),

    ("㉝ ไม่รู้จำนวนตัวเลือก (None) ⇒ ไม่กรองด้วยกฎ (ก) แต่ยังอ่านได้",
     _ex('✅ คำตอบ: ข้อ 2'), None, 1, False, 'one'),
]


# (ชื่อเคส, recs, scope, รหัสข้อที่ต้องแดง)
#  ⛔ ตั้งใจใช้รหัสข้อชุดใหม่ที่ไม่ทับกับ CASES ข้างบน — กับดัก ⑦ข ของพอร์ทัล:
#     มิวแทนต์ที่ทับกับตัวอย่างเดิม จะทำให้ด่านแดงด้วยเหตุผลผิดตัว
ENFORCE_CASES = [
    ("ข้อที่เปลี่ยนรอบนี้ ไม่ประกาศเลข ⇒ ต้องแดง",
     [('f.json', 'NEW-1', 'none')], {'NEW-1'}, ['NEW-1']),

    ("ข้อเก่าที่ไม่ได้แตะ ไม่ประกาศเลข ⇒ ต้องไม่แดง (ไม่ไล่เก็บหนี้เก่า)",
     [('f.json', 'OLD-1', 'none')], {'NEW-1'}, []),

    ("ข้อที่เปลี่ยนรอบนี้ ประกาศเลขเดียว ⇒ ต้องไม่แดง",
     [('f.json', 'NEW-1', 'one')], {'NEW-1'}, []),

    ("ข้อที่เปลี่ยนรอบนี้ ประกาศหลายเลข ⇒ ต้องแดง (ตรวจไม่ได้ = ยังไม่ผ่าน)",
     [('f.json', 'NEW-2', 'many')], {'NEW-2'}, ['NEW-2']),

    ("ปนกัน — ต้องแดงเฉพาะข้อที่อยู่ในขอบเขต",
     [('f.json', 'OLD-1', 'none'), ('f.json', 'NEW-1', 'none'),
      ('f.json', 'NEW-2', 'one')], {'NEW-1', 'NEW-2'}, ['NEW-1']),

    ("รอบนี้ไม่มีข้อไหนเปลี่ยน (เซตว่าง) ⇒ ไม่มีอะไรให้บังคับ",
     [('f.json', 'OLD-1', 'none'), ('f.json', 'OLD-2', 'many')], set(), []),

    ("🔴 ขอบเขต None = ทั้งคลัง ⛔ ต้องไม่ยุบรวมกับเซตว่าง",
     [('f.json', 'OLD-1', 'none'), ('f.json', 'OLD-2', 'many')], None,
     ['OLD-1', 'OLD-2']),

    ("รหัสข้อในขอบเขตที่ไม่มีอยู่ในคลัง (ข้อถูกลบ/เปลี่ยนชื่อ) ⇒ ต้องไม่ล้ม",
     [('f.json', 'NEW-1', 'one')], {'NEW-1', 'GHOST-9'}, []),
]


# (ชื่อเคส, ข้อ, ต้องนับเป็น "ตาบอด" ไหม)
#  ⛔ ถ้าใครแก้ eligible() ให้รับทุกชนิด ตัวเลขตาบอดจะกลายเป็น 0
#     แล้วบรรทัดที่พอร์ทัลสั่งไว้จะ "พิมพ์ออกมาแต่โกหก" ⇒ ต้องมีเคสเฝ้า
BLIND_CASES = [
    ("ข้อ fill ที่มีคีย์และเฉลย ⇒ ตาบอด (นี่คือเหตุผลที่ต้องมีด่าน 17)",
     {'type': 'fill', 'correct': '9/40', 'explanation': ['✅ คำตอบ']}, True),
    ("ข้อปรนัยปกติ ⇒ ไม่ใช่ตาบอด (ด่านนี้มองเห็นอยู่แล้ว)",
     {'type': 'mc', 'correct': 0, 'explanation': ['✅ ตัวเลือก 1']}, False),
    ("ข้อ fill ที่ไม่มีเฉลย ⇒ ไม่นับ (ไม่มีของให้ด่านไหนตรวจตั้งแต่แรก)",
     {'type': 'fill', 'correct': '5', 'explanation': []}, False),
    ("ข้อ fill ที่ไม่มีคีย์ ⇒ ไม่นับ",
     {'type': 'fill', 'explanation': ['✅ คำตอบ']}, False),
    ("ข้อปรนัยที่คีย์ไม่ใช่จำนวนเต็ม ⇒ ไม่ใช่ 'ตาบอดเพราะชนิด' ⛔ ห้ามนับรวม",
     {'type': 'mc', 'correct': 'ก', 'explanation': ['✅ ตัวเลือก 1']}, False),
]


def _mut_blind_always_zero(q):
    """⑥ รายงานว่าไม่มีข้อตาบอดเลย ⇒ บรรทัดที่พอร์ทัลสั่งกลายเป็นคำโกหก"""
    return False


def _run_blind_cases(fn):
    fails = []
    for name, q, want in BLIND_CASES:
        try:
            good = bool(fn(q)) == want
        except Exception:
            good = False
        if not good:
            fails.append(name)
    return fails


def _mut_ignore_scope(recs, scope_ids):
    """มิวแทนต์ ③ ลืมขอบเขต ⇒ ไล่เก็บหนี้เก่าทั้งคลัง (ด่านจะแดงตลอดกาล)"""
    return [(f, q, k) for f, q, k in recs if k != 'one']


def _mut_many_is_ok(recs, scope_ids):
    """มิวแทนต์ ④ ถือว่า 'ประกาศหลายเลข' ใช้ได้ ⇒ ช่องเลี่ยงที่เขียนง่ายมาก"""
    out = []
    for f, q, k in recs:
        if scope_ids is not None and q not in scope_ids:
            continue
        if k == 'none':
            out.append((f, q, k))
    return out


def _mut_never_red(recs, scope_ids):
    """มิวแทนต์ ⑤ ไม่บังคับอะไรเลย ⇒ กติกากลับไปอยู่แต่ในจดหมาย"""
    return []


def _run_enforce_cases(fn):
    """คืนรายชื่อเคสที่ล้มเมื่อใช้ fn เป็นตัวตัดสินชั้นบังคับ"""
    fails = []
    for name, recs, scope, want in ENFORCE_CASES:
        try:
            got = sorted(q for _, q, _ in fn(recs, scope))
            good = got == sorted(want)
        except Exception:
            good = False
        if not good:
            fails.append(name)
    return fails


def _mut_no_distractor_filter(explanation, n_choices=None):
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


def _mut_always_clean(explanation, n_choices=None):
    """มิวแทนต์ ② ไม่ตรวจอะไรเลย แล้วรายงานว่าไม่มีอะไรให้ตรวจ ⇒ เขียวตลอดกาล"""
    return 'none', None


# ── 🆕 v1.4 มิวแทนต์ของ ㉝ — แต่ละตัวถอดข้อบังคับออกหนึ่งข้อ ─────────────
def _alt_variant(explanation, n_choices, *, alt_re=ALT_RE, use_alt=True,
                 nfilter=True, choice_wins=True):
    nums = set()
    for line in explanation:
        if not isinstance(line, str):
            continue
        if any(k in line for k in DISTRACTOR_MARKERS):
            continue
        if not any(k in line for k in ANSWER_MARKERS):
            continue
        c = {int(m) for m in CHOICE_RE.findall(line)}
        nums |= c
        if c and choice_wins:
            continue
        if use_alt:
            nums |= {int(m) for m in alt_re.findall(line)
                     if not (nfilter and n_choices) or int(m) <= n_choices}
    if not nums:
        return 'none', None
    if len(nums) > 1:
        return 'many', sorted(nums)
    return 'one', nums.pop()


def _mut_no_alt(explanation, n_choices=None):
    """⑦ ถอด ㉝ ทิ้ง = พฤติกรรม v1.3 ⇒ ใช้เป็น positive control กับคลังจริงด้วย (กฎ ⑪)"""
    return _alt_variant(explanation, n_choices, use_alt=False)


def _mut_no_nchoice_filter(explanation, n_choices=None):
    """⑧ ถอดกฎ (ก) ⇒ "ข้อ 12" ถูกอ่านเป็นคำประกาศ"""
    return _alt_variant(explanation, n_choices, nfilter=False)


def _mut_alt_with_choice(explanation, n_choices=None):
    """⑨ ถอดกฎ (ข) ⇒ อ่าน "ข้อ" ปนกับ "ตัวเลือก" ในบรรทัดเดียวกัน"""
    return _alt_variant(explanation, n_choices, choice_wins=False)


_ALT_NO_RANGE = re.compile(r'ข้อ\s*(\d+)')


def _mut_no_range_guard(explanation, n_choices=None):
    """⑩ ถอด lookahead ⇒ ช่วง "ข้อ 1–4" ถูกอ่านเป็นเลข 1"""
    return _alt_variant(explanation, n_choices, alt_re=_ALT_NO_RANGE)


def _mut_whole_block(explanation, n_choices=None):
    """⑪ อ่านทั้งก้อนแทนทีละบรรทัด (ทรงที่ชุดทดสอบใบ 391 §2 เฝ้าไว้)"""
    lines = [x for x in explanation if isinstance(x, str)
             and not any(k in x for k in DISTRACTOR_MARKERS)]
    if not any(any(k in x for k in ANSWER_MARKERS) for x in lines):
        return 'none', None
    return _alt_variant(['✅ ' + ' '.join(lines)], n_choices)


def _run_alt_cases(fn):
    """คืนรายชื่อเคส ㉝ ที่ล้มเมื่อใช้ fn เป็นตัวอ่าน"""
    fails = []
    for name, ex, n, correct, want_red, want_kind in ALT_CASES:
        try:
            kind, val = fn(ex, n)
            red = (kind == 'one' and val != correct + 1)
            good = (kind == want_kind) and (red == want_red)
        except Exception:
            good = False
        if not good:
            fails.append(name)
    return fails


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
    print('  ── 🆕 ㉝ อ่าน "ข้อ N" ในบรรทัดคำตอบ (v1.4 · มติครู 23 ก.ย. ③) ──')
    for name, ex, n, correct, want_red, want_kind in ALT_CASES:
        kind, val = declared_choice(ex, n)
        red = (kind == 'one' and val != correct + 1)
        good = (kind == want_kind) and (red == want_red)
        tag = '(ต้องจับได้)' if want_red else '(ต้องผ่าน)'
        print(f'  {"✅" if good else "🔴"}  {tag} {name}')
        ok &= good
    good = not _run_cases(declared_choice)
    print(f'  {"✅" if good else "🔴"}  เคสเดิมของ v1.3 ทั้ง {len(CASES)} เคส ยังผ่านเมื่อเปิด ㉝')
    ok &= good
    print('  ── มิวแทนต์ของ ㉝ — และ "ถูกจับด้วยเคสไหน" ──')
    for label, fn in (
        ('⑦ ถอด ㉝ ทิ้ง (= v1.3)',              _mut_no_alt),
        ('⑧ ถอดกฎ (ก) N > จำนวนตัวเลือก',       _mut_no_nchoice_filter),
        ('⑨ ถอดกฎ (ข) ตัวเลือกชนะ',              _mut_alt_with_choice),
        ('⑩ ถอด lookahead กันช่วง "ข้อ 1–4"',    _mut_no_range_guard),
        ('⑪ อ่านทั้งก้อนแทนทีละบรรทัด',           _mut_whole_block),
    ):
        fails = _run_alt_cases(fn)
        good = len(fails) > 0
        print(f'  {"✅" if good else "🔴"}  มิวแทนต์ {label} ⇒ ล้ม {len(fails)}/{len(ALT_CASES)} เคส')
        for f in fails[:2]:
            print(f'         ↳ จับได้ที่: {f}')
        ok &= good

    print()
    print('  ── ชั้นบังคับตามขอบเขต diff (v1.1) ──')
    for name, recs, scope, want in ENFORCE_CASES:
        got = sorted(q for _, q, _ in enforce_verdict(recs, scope))
        good = got == sorted(want)
        print(f'  {"✅" if good else "🔴"}  {name}')
        ok &= good

    print()
    print('  ── ตัวนับ "ตาบอด" (บรรทัดที่พอร์ทัลสั่งไว้ E→MB #22) ──')
    for name, q, want in BLIND_CASES:
        good = bool(is_blind(q)) == want
        print(f'  {"✅" if good else "🔴"}  {name}')
        ok &= good
    mb = _run_blind_cases(_mut_blind_always_zero)
    good = len(mb) > 0
    print(f'  {"✅" if good else "🔴"}  มิวแทนต์ ⑥ รายงานตาบอด = 0 เสมอ'
          f' ⇒ ล้ม {len(mb)}/{len(BLIND_CASES)} เคส (ต้อง > 0)')
    ok &= good

    print()
    print('  ── มิวแทนต์ของชั้นบังคับ — และ "ถูกจับด้วยเคสไหน" ──')
    print('     (พอร์ทัลเสนอกับดัก ⑦ข: แดงแล้วยังต้องถามว่าแดงเพราะเคสที่ตั้งใจหรือเปล่า)')
    for label, fails in (
        ('③ ลืมขอบเขต ⇒ ไล่เก็บหนี้เก่า', _run_enforce_cases(_mut_ignore_scope)),
        ('④ ยอมรับ "ประกาศหลายเลข"',      _run_enforce_cases(_mut_many_is_ok)),
        ('⑤ ไม่บังคับอะไรเลย',            _run_enforce_cases(_mut_never_red)),
    ):
        good = len(fails) > 0
        print(f'  {"✅" if good else "🔴"}  มิวแทนต์ {label} ⇒ ล้ม {len(fails)}/{len(ENFORCE_CASES)} เคส')
        for f in fails[:2]:
            print(f'         ↳ จับได้ที่: {f}')
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
    print(f'✅ SELF-TEST ผ่านครบ {len(CASES)} + {len(ALT_CASES)} + {len(ENFORCE_CASES)}'
          f' + {len(BLIND_CASES)} เคส + มิวแทนต์ 11 ตัว')
    return 0


def main():
    ap = argparse.ArgumentParser(
        description='ตรวจว่าเลขตัวเลือกที่เฉลยประกาศ ตรงกับคีย์คำตอบของข้อนั้น')
    ap.add_argument('sets_dir', nargs='?', default='data/sets')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    ap.add_argument('--min-coverage', type=float, default=DEFAULT_MIN_COVERAGE,
                    help='สัดส่วนขั้นต่ำของข้อที่ต้องตรวจได้จริง (กันด่านตาบอดเงียบ)')
    ap.add_argument('--max-undeclared', type=int, default=MAX_UNDECLARED, metavar='N',
                    help=f'เพดานหนี้ "ตรวจไม่ได้" = หลายเลข + ไม่ประกาศ (ปริยาย {MAX_UNDECLARED})'
                         ' — ratchet เดินลงทางเดียว')
    ap.add_argument('--min-eligible', type=int, default=MIN_ELIGIBLE, metavar='N',
                    help=f'พื้นตัวหาร (กับดัก ⑨) — ต่ำกว่านี้ ⇒ รหัส 2 (ปริยาย {MIN_ELIGIBLE})'
                         ' · 0 = ปิด ใช้เฉพาะตอนตรวจโฟลเดอร์ย่อย')
    ap.add_argument('--enforce-declared', action='store_true',
                    help='โหมดด่าน 8: บังคับว่าข้อที่เปลี่ยนรอบนี้ต้องประกาศเลขตัวเลือกได้')
    ap.add_argument('--changed-ids', default=None, metavar='ID,ID,…',
                    help='ขอบเขตของ --enforce-declared'
                         ' (รับจาก scan_symbols.py --print-changed-ids)'
                         ' ⛔ ไม่ระบุธงนี้เลย = ทั้งคลัง · ระบุเป็นค่าว่าง = รอบนี้ไม่มีข้อเปลี่ยน')
    a = ap.parse_args()

    if a.version:
        print(CHECKER_VERSION)
        return 0
    if a.selftest:
        return selftest()

    if a.changed_ids is not None and not a.enforce_declared:
        print('🔴 --changed-ids ใช้ได้เฉพาะคู่กับ --enforce-declared')
        print('   ⇒ ถ้ารับไว้เฉย ๆ จะเข้าใจว่า "จำกัดขอบเขตแล้ว" ทั้งที่ไม่มีอะไรเกิดขึ้น')
        return 2

    bad, st, recs = scan(a.sets_dir)
    elig = st['eligible']
    cov = (st['one'] / elig) if elig else 0.0

    debt = st['many'] + st['none']

    print(f'ตรวจ {a.sets_dir} · ข้อปรนัยที่มีคีย์และเฉลย {elig} ข้อ')
    # 🔴 บรรทัดเดียว 4 เลข — ตกลงกับพอร์ทัล (รอบ 15) ว่าเลขทุกตัวต้อง "มากับตัวหาร"
    #    ⛔ ห้ามพิมพ์ % ลอย ๆ โดยไม่มีตัวส่วน · ⛔ ห้ามพิมพ์หนี้โดยไม่มีเพดาน
    print(f'  ตรวจได้ {st["one"]:,} / {elig:,} ({cov*100:.1f}%)'
          f'  ·  ประกาศหลายเลข {st["many"]:,}'
          f'  ·  ไม่ประกาศ {st["none"]:,}'
          f'  ·  รวมหนี้ {debt:,} (เพดาน {a.max_undeclared:,})')
    print('  ⛔ "ตรวจไม่ได้" ไม่เท่ากับ "ตรวจแล้วผ่าน" — หนี้ทั้ง 2 ถังคือข้อที่ด่าน 7 มองไม่เห็น')

    # ── 📌 บรรทัดตาบอด — พอร์ทัลสั่งไว้ในจดหมาย E→MB #22 ⛔ ห้ามละ ──────
    #    เหตุผล: ด่านนี้รับเฉพาะ type == 'mc' ⇒ ข้อ fill ไม่เคยถูกมองเลยสักข้อ
    #    ถ้ารายงานแต่ "ตรวจได้ 2,797/4,221" คนอ่านจะเข้าใจว่าตัวหารคือทั้งคลัง
    #    ⇒ ต้องประกาศ "ตาบอดกี่ข้อ" ทุกครั้ง แม้วันที่ตัวเลขจะเป็นศูนย์
    #    ⛔ ห้ามลบบรรทัดนี้ตอนที่ด่าน 17 เขียว — ด่าน 17 ไม่ได้ทำให้ด่าน 7 มองเห็น fill
    total = elig + st['blind']
    pct = (st['blind'] / total * 100) if total else 0.0
    print(f'📌 ด่าน 7 ตรวจได้ {st["one"]:,}/{elig:,} ข้อ (mc เท่านั้น)'
          f' · ตาบอด {st["blind"]:,} ข้อ = {pct:.1f}%')
    print(f'   ตัวหารของ "ตาบอด" = ข้อที่มีคีย์และมีเฉลยทั้งหมด {total:,} ข้อ'
          ' (ปรนัย + เติมคำ)')
    if st['blind']:
        print('   ⇒ ข้อที่ตาบอดตรงนี้ เป็นงานของ ด่าน 17 (scripts/check_fill_answer.py)')
    print()

    # ── ⑨ พื้นตัวหาร — ต้องมาก่อนคำตัดสินทุกอัน ────────────────────
    if a.min_eligible and elig < a.min_eligible:
        print(f'🔴 ข้อที่ตรวจได้มีแค่ {elig:,} — ต่ำกว่าพื้น {a.min_eligible:,}')
        print('   ⇒ หนี้ที่ "ลดลง" รอบนี้อาจเป็นเพราะไฟล์ชุดหายไป ไม่ใช่เพราะมีคนแก้')
        print('   ⛔ ผลรอบนี้ใช้อ้างอิงไม่ได้ (ตั้งใจตรวจโฟลเดอร์ย่อย ⇒ --min-eligible 0)')
        return 2

    # ── ratchet เดียวของหนี้ "ตรวจไม่ได้" ───────────────────────────
    if debt > a.max_undeclared:
        print(f'🔴 หนี้ "ตรวจไม่ได้" โตขึ้น {a.max_undeclared:,} → {debt:,}'
              f' (+{debt - a.max_undeclared:,})')
        print('   ⇒ มีข้อใหม่ที่ไม่ได้เขียนบรรทัดสรุป "→ ตัวเลือก N" ท้ายเฉลย')
        print('   วิธีแก้: เติมบรรทัดนั้นในข้อที่เพิ่ง/เพิ่งแก้ ⛔ ไม่ใช่ขยับเพดาน')
        print(f'   ถ้ายอดโตเพราะเพิ่มข้อชุดใหญ่จริง ⇒ แก้ MAX_UNDECLARED พร้อมเหตุผลในคอมมิต')
        return 1
    if debt < a.max_undeclared:
        print(f'  🟢 หนี้ลดลงจริง {a.max_undeclared:,} → {debt:,}'
              f' ⇒ ปรับ MAX_UNDECLARED ลงเป็น {debt:,} ได้แล้ว (ratchet เดินลงทางเดียว)')
        print()

    # ── โหมดด่าน 8 — บังคับเฉพาะของใหม่ ──────────────────────
    if a.enforce_declared:
        if a.changed_ids is None:
            scope = None
            print('  ขอบเขต: ทั้งคลัง (ไม่ได้ระบุ --changed-ids)')
        else:
            scope = set(x.strip() for x in a.changed_ids.split(',') if x.strip())
            print(f'  ขอบเขต: ข้อที่เปลี่ยนรอบนี้ {len(scope)} ข้อ')
            ghosts = scope - {q for _, q, _ in recs}
            if ghosts:
                print(f'  🟠 มี {len(ghosts)} รหัสในขอบเขตที่ไม่ใช่ข้อปรนัยที่ตรวจได้'
                      ' (ข้อเติมคำ/ถูกลบ/ไม่มีคีย์) ⇒ ไม่บังคับ')
        need = enforce_verdict(recs, scope)
        print(f'  ⛔ ด่านนี้ไม่ตัดสินเรื่อง "เฉลยขัดคีย์" — นั่นเป็นงานของด่าน 7')
        print()
        if need:
            print(f'🔴 ข้อที่เปลี่ยนรอบนี้แต่ประกาศเลขตัวเลือกไม่ได้ {len(need)} ข้อ:')
            for f, qid, kind in need:
                why = ('ไม่ประกาศเลขตัวเลือกเลย' if kind == 'none'
                       else 'ประกาศหลายเลขในบรรทัดคำตอบ ⇒ ตัดสินไม่ได้')
                print(f'   {qid:<28} {why}   [{f}]')
            print()
            print('   วิธีแก้: เติมบรรทัดสรุปท้ายเฉลยให้ชัด เช่น')
            print('           <b>✅ คำตอบ: … → ตัวเลือก 3</b>')
            print('   เหตุผล: ข้อที่ไม่ประกาศเลข ด่าน 7 มองไม่เห็นตลอดไป')
            print('           ⇒ ถ้าปล่อยให้ของใหม่ไม่ประกาศ ตัวเลขครอบคลุมจะไม่มีวันโต')
            return 1
        print('✅ ข้อที่เปลี่ยนรอบนี้ ประกาศเลขตัวเลือกได้ครบทุกข้อ')
        return 0

    if elig and cov < a.min_coverage:
        print(f'🔴 ตรวจได้จริงแค่ {cov*100:.1f}% ต่ำกว่าเพดานล่าง {a.min_coverage*100:.0f}%')
        print('   ⇒ น่าจะมีคนแก้รายการคำสำคัญจนด่านตาบอด — ไม่ใช่ว่าคลังสะอาดขึ้น')
        return 2

    if bad:
        print(f'🔴 เฉลยขัดกับคีย์ {len(bad)} ข้อ:')
        for f, qid, said, key in bad:
            print(f'   {qid:<28} เฉลยประกาศเลข {said} ("ตัวเลือก N" หรือ "ข้อ N")'
                  f' · คีย์เก็บ ตัวเลือก {key}   [{f}]')
        print()
        print('   วิธีอ่าน: เด็กที่ทำข้อนี้ได้คะแนน "ถูก" ตามคีย์')
        print('             แต่เด็กที่อ่านเฉลย จะถูกสอนคำตอบอีกอัน')
        return 1

    print('✅ ไม่พบข้อที่เฉลยขัดกับคีย์')
    return 0


if __name__ == '__main__':
    sys.exit(main())

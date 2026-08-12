#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ด่าน 10 · รายการ "สิ่งที่อนุญาต" ต้องไม่โตขึ้นเงียบ ๆ

ที่มา (1 ส.ค. 2569 · จดหมายพอร์ทัล E→MB #02 ตอบข้อ M7 / กับดัก ⑧):
  ด่าน 6 มี ALLOWED_PATHS = ['data/bank.json'] และ "หมุดปักค่า" (CONFIG_PIN)
  อยู่ในไฟล์เดียวกัน — ซึ่งเป็นกับดัก ⑧ เต็ม ๆ:
      🔴 กฎที่บังคับ "รอยต่อระหว่างรุ่น" ไปอยู่ในรุ่นใดรุ่นหนึ่งไม่ได้
         เพราะคนที่แก้รายการ ก็แก้หมุดในบรรทัดถัดไปได้พร้อมกัน
  พอร์ทัลจึงเสนอ (และรับมาทำ) ว่า ตัวเทียบต้องอยู่ "นอกทั้งสองรุ่น" = อยู่ที่ CI
  ⇒ เทียบรายการที่ HEAD กับที่ฐาน (HEAD~1 / event.before / PR base)
     ถ้ารายการ **โตขึ้น** ⇒ แดง เว้นแต่ข้อความ commit ในช่วงนั้นประกาศไว้ว่า
         ALLOWED_PATHS+: <เหตุผล>

  ⚠️ ข้อจำกัดที่พอร์ทัลรับรู้แล้วและยอมรับ:
     คนที่ตั้งใจเลี่ยง ก็พิมพ์บรรทัดประกาศนั้นเองได้ ด่านนี้ไม่ได้กันคนโกง
     สิ่งที่กันได้คือ **การขยายสิทธิ์แบบไม่มีใครสังเกต** — บังคับให้การขยาย
     ต้องทิ้งประโยคไว้ในประวัติ git ที่ค้นย้อนได้

⛔ อ่านไฟล์เป็น "ข้อความล้วน" เท่านั้น — ห้าม import สคริปต์ที่กำลังตรวจ
   (กฎเดียวกับด่าน 2 · ถ้า import ไฟล์ที่พัง ตัวด่านจะพังตามไปด้วย
    แล้วจะแยกไม่ออกว่า "ของพัง" หรือ "ด่านพัง")

รหัสออก: 0 = ผ่าน · 1 = เนื้อหาแดง · 2 = ตัวเครื่องมือแดง / เทียบไม่ได้
"""
import argparse
import ast
import re
import subprocess
import sys

CHECKER_VERSION = '1.2'

# (ไฟล์, ชื่อตัวแปร) ที่ต้องเฝ้า — เพิ่มได้ แต่การเพิ่ม "รายการที่เฝ้า" ไม่อันตราย
# อันตรายคือการเพิ่ม "สมาชิกในรายการที่ถูกเฝ้า" ซึ่งคือสิ่งที่ด่านนี้จับ
WATCHED = [
    ('scripts/check_bot_add.py', 'ALLOWED_PATHS'),
    ('scripts/check_flawed_source.py', 'ALLOWED_KINDS'),
    # 🔴 WORD_BANNED เป็น dict {คำ: เหตุผล} ไม่ใช่ลิสต์ — ด่านนี้เฝ้า "คีย์"
    #    เหตุผลที่ต้องเฝ้า: มันคือรายการเดียวในคลังที่ "เติมคำเดียว = คลังแดงทั้งคลัง"
    #    (เติม 'cis' ลงไปคำเดียว ⇒ แดง 435 จุดในวินาทีเดียว)
    ('scripts/scan_symbols.py', 'WORD_BANNED'),
    # 🔴 NOT_IN_CI = รายการ "ตัวตรวจที่ตั้งใจไม่ให้ CI เรียก" ของด่าน 11
    #    เฝ้าเพราะมันคือ **รายการปิดด่านที่ถูกกติกา** — ทุกชื่อที่เพิ่มเข้าไป
    #    คือด่านหนึ่งด่านที่หลุดจากกฎ ⑦ก อย่างถาวร
    #    ⇒ ตอนออกแบบข้อยกเว้นนี้เขียนไว้เองว่า "รายการนี้ถูกด่าน 10 เฝ้าไว้"
    #      ถ้าไม่ลงทะเบียนตรงนี้ ประโยคนั้นก็เป็นแค่คอมเมนต์ (⑦ก ซ้อนตัวเอง)
    #    ⚠️ เฝ้า "คีย์" ⇒ แก้ถ้อยคำของเหตุผลไม่นับเป็นการขยายสิทธิ์
    #       ส่วนความยาวขั้นต่ำของเหตุผล ด่าน 11 บังคับเองอยู่แล้ว
    ('scripts/check_exit_codes.py', 'NOT_IN_CI'),
    # 🔴 ALLOW_BARE = รายการ "หมุดรูปเปล่าที่ยอมให้ค้างไว้" ของด่าน 14
    #    เพิ่ม 3 ส.ค. 69 (ซองหมุดรูป 3 จุด) — และเพิ่มตอนที่รายการนี้ **ว่างพอดี**
    #
    #    ⚠️ ทำไมต้องเฝ้ารายการที่ว่าง — เหตุผลตรงข้ามกับสัญชาตญาณ
    #      รายการว่างคือรายการที่ "โตกลับ" ได้เงียบที่สุด: เติมบรรทัดเดียวลงไป
    #      ด่าน 14 ก็ยังเขียวเหมือนเดิมทุกตัวอักษร เพราะหมุดเปล่านั้นมีใบอนุญาตแล้ว
    #      ⇒ ตอนที่รายการว่าง คือตอนที่ต้องมีตัวเฝ้าขาขึ้นมากที่สุด ⛔ ไม่ใช่น้อยที่สุด
    #
    #    ⚠️ ก่อนหน้านี้ ด่าน 14 **เขียนในคอมเมนต์ของตัวเองว่าถูกด่าน 10 เฝ้าอยู่**
    #      ทั้งที่ไม่เคยลงทะเบียนที่นี่เลย (⑦ก ซ้อนตัวเองรอบสอง — รอบแรกคือ
    #      NOT_IN_CI ข้างบน) ⇒ v1.2 ของด่าน 14 ถอนคำอ้างนั้น
    #      และ **บรรทัดนี้** คือสิ่งที่ทำให้คำอ้างกลายเป็นเรื่องจริงที่ตรวจสอบได้
    #
    #    ⚠️ เฝ้า "คีย์" ⇒ แก้ถ้อยคำของเหตุผลไม่นับเป็นการขยายสิทธิ์
    #       ความยาวขั้นต่ำของเหตุผล (MIN_REASON = 40) ด่าน 14 บังคับเองอยู่แล้ว
    #    ⚠️ ขาลง (3 → 0 ในซองนี้) ⛔ ไม่แดง ตามกติกาของ growth_verdict —
    #       "ลดสิทธิ์ไม่ต้องขออนุญาต" ส่วนขาลงอีกแบบ (รายการค้างโดยไม่มีหมุดเปล่า
    #       รองรับแล้ว = แดง) ด่าน 14 บังคับเองในตัว
    ('scripts/check_image_markers.py', 'ALLOW_BARE'),
    # 🔴 KNOWN_DUPES = หมุด "ข้อที่ตัวเลือกซ้ำกันและยอมให้ค้างไว้" ของด่าน 15
    #    เพิ่ม 9 ส.ค. 69 พร้อมกับตัวด่านเอง (คำเคาะ E→MB #61 §2 · ทาง ค)
    #
    #    ⚠️ ทำไมต้องเฝ้า — เพราะรายการนี้คือ **ราคาทั้งหมดของทาง ค**
    #      ทาง ค เลือกให้ด่านเขียววันแรกโดยยกเว้น 2 ข้อที่มีชื่อ แทนที่จะปล่อยแดง
    #      (แดงไม่มีกำหนด ⇒ ⑯ ⇒ และเพราะ guards.yml เป็นใบเดียว จะพาด่านอีก 19 ใบตายด้วย)
    #      ⇒ ⇒ สิ่งเดียวที่กันไม่ให้ "ทาง ค" กลายเป็น "ที่ทิ้งขยะที่ถูกกฎ"
    #           คือ **การเติมชื่อที่สามต้องประกาศในข้อความคอมมิต**
    #      ⇒ ถ้าบรรทัดนี้หายไป ด่าน 15 จะยังเขียวอยู่ทุกวัน แต่รายการยกเว้นจะโตได้เงียบ ๆ
    #
    #    ⚠️ เฝ้า "คีย์" (= รหัสข้อ) ⇒ แก้ถ้อยคำของ why/until ⛔ ไม่นับเป็นการขยายสิทธิ์
    #       ความยาวขั้นต่ำของเหตุผล (MIN_REASON = 40) และการมี until ด่าน 15 บังคับเองในตัว
    #    ⚠️ ขาลง ⛔ ไม่แดง — และด่าน 15 บังคับขาลงเองอยู่แล้ว:
    #       หมุดที่ไม่มีของรองรับ (ข้อหาย/ไม่ซ้ำแล้ว) ⇒ ด่าน 15 แดงจนกว่าจะถอนหมุด
    #    🔴 v1.2 ของด่าน 15 · เฝ้า **KNOWN_DUPE_IDS** (รายการแบน) ⛔ ไม่ใช่ KNOWN_DUPES
    #       เหตุ: `KNOWN_DUPES` มีป้ายชนิด (`: dict[str, dict]`) และเป็น dict ซ้อนชั้น
    #             ⇒ parse_list ของด่านนี้อ่านไม่ออกทั้งสองเหตุ ⇒ เฝ้าไม่ได้จริง
    #       ⇒ ด่าน 15 มี selftest เรียก parse_list ตัวจริงมารันพิสูจน์ว่าอ่านออก (⑱ข)
    #         และบังคับให้รายการแบนตรงกับหมุดจริงเสมอ (㉒)
    ('scripts/check_duplicate_choices.py', 'KNOWN_DUPE_IDS'),
    # 🔴 PINNED = รายการ "ป้ายเลขกำพร้าที่อ่านแล้วและตัดสินแล้ว" ของด่าน 16
    #    เพิ่ม 3 ส.ค. 69 พร้อมกับตัวด่าน 16 เอง — ⛔ ไม่ใช่ตามหลัง
    #
    #    ⚠️ ลงทะเบียน **ในซองเดียวกับที่สร้างด่าน 16** โดยตั้งใจ
    #      ด่าน 16 เขียนในหัวไฟล์ของตัวเองว่า "รายการนี้ถูกด่าน 10 เฝ้าขาขึ้นอยู่"
    #      ถ้าเลื่อนบรรทัดนี้ไปซองหน้า ประโยคนั้นจะเป็นคำอ้างลอย ๆ ไปหนึ่งซอง
    #      = กับดัก ⑦ก รอบที่สาม (สองรอบแรก: NOT_IN_CI และ ALLOW_BARE ข้างบน
    #      ซึ่งทั้งคู่เคยเขียนคำอ้างไว้ก่อนแล้วค่อยมาลงทะเบียนทีหลัง)
    #      ⇒ กฎที่ถอดออกมา: **คำอ้างกับการลงทะเบียน ต้องเดินทางในซองเดียวกัน**
    #
    #    ⚠️ รอบแรกจะพิมพ์ 🟠 "ไฟล์นี้ไม่เคยมีในประวัติก่อนหน้า ⇒ ยังไม่มีของให้เทียบ"
    #      ⛔ นั่นไม่ใช่เขียว มันคือบันทึกว่า "รอบนี้ยังไม่ได้เฝ้า" — เฝ้าจริงรอบหน้า
    #
    #    ⚠️ เฝ้า "คีย์" (id ของข้อ) ⇒ แก้ถ้อยคำของเหตุผล หรือแก้ชุดป้ายที่ประกาศไว้
    #       ไม่นับเป็นการขยายสิทธิ์ที่นี่ — แต่ **ด่าน 16 จับเองสองทาง**:
    #       ชุดป้ายที่ไม่ตรงกับของจริง = แดง · บรรทัดที่ไม่มีธงรองรับแล้ว = แดง
    #       ⇒ สองด่านนี้แบ่งงานกัน ⛔ ไม่ได้ตรวจซ้ำกัน
    #    ⚠️ ขาลง (เช่นวันที่แก้ 22.5 → 62 แล้วลบบรรทัด pat1-2560-03-q35 ทิ้ง)
    #       ⛔ ไม่แดงที่นี่ ตามกติกา "ลดสิทธิ์ไม่ต้องขออนุญาต" — และ ⛔ ไม่ต้องแดง
    #       เพราะถ้าลบบรรทัดโดยที่ยังไม่ได้แก้ข้อมูล ด่าน 16 จะแดงทันทีอยู่แล้ว
    ('scripts/check_orphan_labels.py', 'PINNED'),
    # 🔴 NOTES_REF_DEBT = หนี้ "ข้อที่ `notes` อ้างเอกสารที่หาไม่พบ" ของด่าน 21
    #    เพิ่ม 13 ส.ค. 69 **ในคอมมิตเดียวกับที่สร้างด่าน 21** ⛔ ไม่ใช่ตามหลัง
    #    ⇒ ตามกฎที่ ALLOW_BARE/PINNED ถอดออกมาแล้ว: **คำอ้างกับการลงทะเบียน ต้องเดินทางในซองเดียวกัน**
    #
    #    ⚠️ ทำไมอยู่ใน WATCHED ⛔ ไม่ใช่ FROZEN — และนี่คือเส้นแบ่งที่ควรจำ:
    #       `BLIND_CENSUS` (FROZEN) = **สำมะโนที่มีวันที่** ⇒ "เคยขาด" ⛔ ไม่มีวันเป็นเท็จ ⇒ ย่อไม่ได้
    #       `NOTES_REF_DEBT` (ที่นี่) = **หนี้ที่ต้องหมดไป**  ⇒ ย่อ = ใช้หนี้ ⇒ ต้องย่อได้ฟรี
    #       ⇒ ⇒ เอาสองอย่างนี้ไปไว้ทรงเดียวกัน = ⑪ (ยุบสองสิ่งที่ต่างกันให้ใช้กฎเดียว)
    #
    #    ⚠️ และการย่อมันเงียบ ๆ **ทำไม่ได้อยู่แล้ว** — ด่าน 21 บังคับขาลงเองในตัว (กฎ ②):
    #       ถอนหมุดโดยที่ `notes` ยังอ้างของที่ไม่มี ⇒ กฎ ① แดงทันที
    #       ⇒ WATCHED ที่นี่จึงเฝ้า **ขาขึ้น** อย่างเดียวก็พอ — ⛔ ไม่ใช่ความหละหลวม
    #
    #    ⚠️ ที่ต้องเฝ้าขาขึ้นจริง ๆ คือ **ก้อนแต่งใหม่**: ก้อน b20/b21 พลาดทั้งก้อน
    #       โดยที่ ⛔ ไม่มีใครเห็นมาสามเดือน ⇒ ก้อนถัดไปที่พลาดแบบเดียวกัน
    #       จะต้องเขียน `NOTES_REF_DEBT+:` ในข้อความคอมมิต = มีคนต้องพิมพ์เหตุผลด้วยมือ
    ('scripts/check_notes_refs.py', 'NOTES_REF_DEBT'),
]

# ═══════════════════════════════════════════════════════════════
#  FROZEN — รายการที่เป็น "ข้อเท็จจริงที่มีวันที่" ⛔ ไม่ใช่ "สภาพปัจจุบัน"
# ═══════════════════════════════════════════════════════════════
#
# 🔴 **ต่างจาก WATCHED ที่ *ทิศทาง* ⛔ ไม่ใช่ที่ความเข้มงวด**
#      WATCHED เฝ้า **ขาขึ้น** — "ขยายสิทธิ์ต้องขออนุญาต · ลดสิทธิ์ไม่ต้องขอ"
#      FROZEN  เฝ้า **สองขา** — เพราะรายการพวกนี้ ⛔ ไม่ใช่สิทธิ์ มันคือ **บันทึกสำมะโน**
#                               ⇒ การลบชื่อออก = **การลบหลักฐาน** ⛔ ไม่ใช่การลดสิทธิ์
#
# ⬤ **ที่มา (10 ส.ค. 69 · MB วัดจริง ⛔ ไม่ใช่การคาดเดา):**
#    ด่าน 15 มี selftest ⑲ ที่ตรวจว่า "รหัสข้อทั้ง 9 ของสำมะโนตาบอด อยู่ในหัวไฟล์"
#    🔴 ย่อรายการจาก 9 ชื่อเหลือ 1 ชื่อ ⇒ selftest **ยังผ่านครบ 28/28 เคส**
#       และย่อหัวไฟล์ตามไปด้วย ⇒ **ยังผ่านอีก**
#    ⇒ ⇒ เคสนั้นเฝ้า **"ความสอดคล้องภายในไฟล์"** ⛔ ไม่ได้เฝ้า **"ความครบ"**
#         เพราะสองข้างที่มันเทียบอยู่ใน **ไฟล์เดียวกัน** ⇒ แก้พร้อมกันก็ผ่าน
#    ⇒ ⇒ ⇒ 🔑 สิ่งที่ขาดคือ **หลักยึดที่อยู่นอกไฟล์** — และ `git` คือหลักยึดนั้น
#            (ด่านนี้อ่านค่าที่คอมมิตฐานอยู่แล้ว ⇒ เครื่องมือมีอยู่แล้ว ขาดแค่ทิศทาง)
#
# ⚠️ **การประกาศ:** เติม ⇒ `VAR+: <เหตุผล>` · ลบ ⇒ `VAR-: <เหตุผล>` ในข้อความคอมมิต
FROZEN = [
    # 🔴 BLIND_CENSUS = สำมะโน "ข้อที่ต้นฉบับมี 5 ตัวเลือกแต่คลังเก็บ 4" ของด่าน 15
    #    พบ 9 ข้อ เมื่อ 10 ส.ค. 69 (E เปิด PDF · E→MB #63 §3)
    #    ⇒ วันที่ข้อไหนถูกซ่อม **ให้ทำเครื่องหมายในหัวไฟล์ ⛔ ไม่ใช่ลบชื่อออก**
    #      เพราะ "เคยขาด" เป็นข้อเท็จจริงที่ ⛔ ไม่มีวันเป็นเท็จ (กฎห้ามลบบันทึกเก่า)
    ('scripts/check_duplicate_choices.py', 'BLIND_CENSUS'),
]

MIN_REASON_LEN = 8


def parse_list(text, var):
    """อ่านค่ารายการของตัวแปร จากไฟล์ในรูป "ข้อความล้วน"

    คืน (สถานะ, ค่า)
      'ok'         → ลิสต์ของสตริง (ถ้าค่าเป็น dict จะคืน "คีย์" — ดูหมายเหตุล่าง)
      'absent'     → ไม่มีตัวแปรนี้ในไฟล์ (หรือถูกคอมเมนต์ไว้)
      'multi'      → มีการประกาศตัวแปรนี้มากกว่า 1 ที่ ⇒ ตัดสินไม่ได้
      'unparsable' → เจอแล้วแต่อ่านค่าไม่ออก
    ⛔ 'absent' ไม่ใช่ 'ลิสต์ว่าง' — "ไม่มีให้เทียบ" ต่างจาก "เทียบแล้วไม่มีอะไร"
       (กับดัก ⑥ · เป็นเหตุผลเดียวกับที่ scan_symbols แยก UNKNOWN_PREV ออกมา)

    🔴 รองรับ dict ตั้งแต่ v1.1 — และนี่ไม่ใช่เรื่องความสะดวก:
       WORD_BANNED ของ scan_symbols เป็น dict {คำ: เหตุผล} โดยเจตนา (เหตุผลต้องมาพร้อมคำ)
       ถ้า parse_list อ่าน dict ไม่ได้ ด่านนี้จะคืน 'unparsable' ทุกครั้ง ⇒ แดงค้างถาวร
       ⇒ คนแก้จะถอดมันออกจาก WATCHED แล้วรายการที่อันตรายที่สุดจะไม่มีใครเฝ้าเลย
       (กับดัก ⑦ข: ด่านที่แดงตลอดเวลา มีค่าเท่ากับด่านที่ถูกปิด)

    ⚠️ ขอบเขตที่ยอมรับไว้: เขียนแบบง่าย ๆ `\{[^}]*\}` ⇒ ถ้าเหตุผลมี } อยู่ข้างใน
       จะอ่านไม่ออก ⇒ คืน 'unparsable' = แดง ⛔ ไม่ใช่ "อ่านได้บางส่วน"
       เลือกทางนี้เพราะ "แดงแล้วมีคนมาดู" ปลอดภัยกว่า "อ่านได้ครึ่งเดียวแล้วเงียบ"
    """
    # ^ ต้นบรรทัด ⇒ บรรทัดที่ถูกคอมเมนต์ (#) จะไม่เข้าเงื่อนไข — ตั้งใจ
    pat = re.compile(r'(?m)^[ \t]*' + re.escape(var)
                     + r'\s*=\s*(\[[^\]]*\]|\([^)]*\)|\{[^}]*\})')
    ms = pat.findall(text)
    if not ms:
        return 'absent', None
    if len(ms) > 1:
        return 'multi', None
    try:
        v = ast.literal_eval(ms[0])
    except Exception:
        return 'unparsable', None
    if isinstance(v, dict):
        # ⛔ เฝ้า "คีย์" เท่านั้น — การแก้ถ้อยคำของเหตุผลไม่ใช่การขยายสิทธิ์
        return 'ok', list(v.keys())
    if isinstance(v, set):
        # เรียงให้ผลคงที่ — เซตไม่มีลำดับ แต่ผู้เรียกเทียบสมาชิก ไม่ใช่ลำดับอยู่แล้ว
        return 'ok', sorted(v)
    if not isinstance(v, (list, tuple)):
        return 'unparsable', None
    return 'ok', list(v)


def declared(messages, var, sign='+'):
    """ข้อความ commit ในช่วงนี้ ประกาศการขยายรายการนี้ไว้หรือยัง

    รูปแบบที่รับ:  <ชื่อตัวแปร>+: <เหตุผล>   (การเติม)
                   <ชื่อตัวแปร>-: <เหตุผล>   (การลบ · ใช้กับ FROZEN เท่านั้น)
    ⛔ ต้องระบุ "ชื่อตัวแปร" ให้ตรง — ประกาศตัวแปรอื่นไม่นับ
    ⛔ ต้องมีเหตุผลจริง — เครื่องหมายโคลอนลอย ๆ ไม่นับ
    ⛔ เครื่องหมายต้องตรงทิศ — ประกาศ "เติม" ⛔ ไม่ครอบการ "ลบ"
    """
    pat = re.compile(re.escape(var) + re.escape(sign) + r':[ \t]*(\S[^\n]*)')
    for m in messages:
        if not isinstance(m, str):
            continue
        g = pat.search(m)
        if g and len(g.group(1).strip()) >= MIN_REASON_LEN:
            return True
    return False


def growth_verdict(prev, now, messages, var):
    """คืนรายการปัญหา [(รหัส, ข้อความ)] · ว่าง = ผ่าน

    prev / now = ลิสต์สมาชิก หรือ None (= ไม่มีตัวแปรนั้น ณ จุดนั้น)
    ⛔ เทียบด้วย "สมาชิก" ไม่ใช่ "จำนวน" และไม่ใช่ "สตริงทั้งก้อน"
       — เอาออก 1 ใส่เข้า 1 จำนวนเท่าเดิม แต่สิทธิ์เปลี่ยน ⇒ ต้องแดง
    ⛔ รายการที่ "หดลง" ไม่แดง — ลดสิทธิ์ไม่ต้องขออนุญาต
    """
    if now is None:
        return [('var-gone',
                 f'ไม่พบตัวแปร {var} ที่ HEAD แล้ว — ถ้าเปลี่ยนชื่อ ด่านนี้จะตาบอดทันที '
                 f'⇒ ต้องแก้รายการ WATCHED ของด่าน 10 ให้ตรงกันก่อน')]
    base = [] if prev is None else prev
    added = [x for x in now if x not in base]
    if not added:
        return []
    if declared(messages, var):
        return []
    return [('undeclared-growth',
             f'{var} โตขึ้น {len(added)} รายการ ({" · ".join(map(str, added))}) '
             f'โดยไม่มีบรรทัดประกาศในข้อความ commit ช่วงนี้ '
             f'⇒ เขียน "{var}+: <เหตุผล>" (อย่างน้อย {MIN_REASON_LEN} ตัวอักษร) '
             f'ในข้อความ commit')]


def frozen_verdict(prev, now, messages, var):
    """เหมือน growth_verdict แต่ **เฝ้าสองขา** — ใช้กับรายการใน FROZEN

    🔑 เหตุผลที่ขาลงต้องแดงด้วย:
       รายการใน FROZEN ⛔ ไม่ใช่ "สิทธิ์" มันคือ **สำมะโนที่มีวันที่**
       ⇒ การลบชื่อออกคือการทำให้คำประกาศ **ครบน้อยลง** โดยที่ทุกด่านยังเขียว
       ⇒ ⇒ นี่คือรูที่ selftest ในไฟล์เดียวกันจับไม่ได้โดยหลักการ
            (สองข้างที่มันเทียบอยู่ในไฟล์เดียวกัน ⇒ แก้พร้อมกันก็ผ่าน)
    """
    if now is None:
        return [('var-gone',
                 f'ไม่พบตัวแปร {var} ที่ HEAD แล้ว — สำมะโนที่หายไปทั้งก้อน '
                 f'⛔ ไม่ใช่ "ไม่มีอะไรให้เฝ้า" ⇒ ต้องแก้รายการ FROZEN ให้ตรงกันก่อน')]
    base = [] if prev is None else prev
    added = [x for x in now if x not in base]
    removed = [x for x in base if x not in now]
    bad = []
    if added and not declared(messages, var, '+'):
        bad.append(('undeclared-growth',
                    f'{var} โตขึ้น {len(added)} รายการ ({" · ".join(map(str, added))}) '
                    f'โดยไม่มีบรรทัดประกาศ ⇒ เขียน "{var}+: <เหตุผล>" '
                    f'(อย่างน้อย {MIN_REASON_LEN} ตัวอักษร) ในข้อความ commit'))
    if removed and not declared(messages, var, '-'):
        bad.append(('undeclared-shrink',
                    f'🔴 {var} **ถูกลบออก** {len(removed)} รายการ '
                    f'({" · ".join(map(str, removed))}) โดยไม่มีบรรทัดประกาศ '
                    f'⇒ รายการนี้เป็น **สำมะโนที่มีวันที่** — การลบชื่อ = การลบหลักฐาน '
                    f'⇒ ถ้าตั้งใจจริง เขียน "{var}-: <เหตุผล>" ในข้อความ commit '
                    f'(ปกติแล้วสิ่งที่ควรทำคือ **ทำเครื่องหมายว่าซ่อมแล้ว ⛔ ไม่ใช่ลบชื่อ**)'))
    return bad


def head_status_verdict(st):
    """สถานะที่อ่านได้ **ที่ HEAD** ⇒ เดินต่อได้ไหม · คืน None = ได้ · str = เหตุผลที่ต้องแดง

    🔴 v1.2 · เคสที่ v1.1 ปล่อยผ่าน: **'absent'**
       v1.1 ดักแค่ ('multi', 'unparsable') ⇒ 'absent' ไหลผ่านไปเป็น v_now = None เงียบ ๆ
       ⇒ ถ้าไฟล์นั้นเพิ่งเกิด (how == 'never') ด่านจะพิมพ์ 🟠 "0 รายการ · รอบหน้าจะเฝ้าได้จริง"
         ⇒ ⇒ **เป็นเท็จ** — รอบหน้าจะได้ 'var-gone' แดง ⛔ ไม่ใช่ "เฝ้าได้จริง"
       ⇒ ⇒ ⇒ นี่คือรูที่ทำให้ `KNOWN_DUPES: dict[str, dict] = {…}` ของด่าน 15 v1.0
              ผ่านไปได้ทั้งที่ตัวอ่าน **มองไม่เห็นตัวแปรนั้นเลย** (5ffc3a4 · 9 ส.ค. 69)
       🔑 "อ่านไม่ออก" ยังส่งเสียง · **"ไม่มีอยู่" เงียบ** — และเงียบคือสิ่งที่อันตรายกว่า
    """
    if st == 'ok':
        return None
    if st == 'absent':
        return ('absent ⇒ ตัวอ่านของด่านนี้ ⛔ มองไม่เห็นตัวแปรที่สั่งให้เฝ้า '
                '(ป้ายชนิด `: dict[...]` · dict ซ้อนชั้น · เปลี่ยนชื่อ) '
                '⛔ นี่ ⛔ ไม่ใช่ "รายการว่าง" — เป็น "เฝ้าไม่ได้" '
                '⇒ 〔52〕 : 🟠 ที่ไม่มีวันเป็น 🟢 ต้องแดงเดี๋ยวนี้')
    return (f'{st} ⇒ ตัดสินไม่ได้ · ⛔ ตัดสินไม่ได้ต้องแดงแบบเครื่องมือ ⛔ ไม่ใช่ปล่อยผ่าน')


# ═════════════════════════════════════════════════════════════
#  SELF-TEST
# ═════════════════════════════════════════════════════════════
SRC_OK = """
import os
ALLOWED_PATHS = ['data/bank.json']
X = 1
"""

SRC_MULTILINE = """
ALLOWED_KINDS = (
    'multiple-correct',
    'no-correct',
)
"""

SRC_COMMENTED = """
# ALLOWED_PATHS = ['data/bank.json', 'data/secret.json']
ALLOWED_PATHS = ['data/bank.json']
"""

SRC_ONLY_COMMENT = """
# ALLOWED_PATHS = ['data/bank.json']
"""

SRC_TWICE = """
ALLOWED_PATHS = ['data/bank.json']
ALLOWED_PATHS = ['data/bank.json', 'data/anything.json']
"""

SRC_WEIRD = """
ALLOWED_PATHS = [os.environ['X']]
"""

# ── ของจริงจาก scan_symbols.py: dict {คำ: เหตุผล} หลายบรรทัด + สตริงต่อกันเอง ──
SRC_DICT = """
MIN_WORD_REASON = 20

WORD_BANNED = {
    'cosec': 'สัญกรณ์เก่าของโคซีแคนต์ — ใช้ csc เท่านั้น '
             '· แปลงทั้งคลังแล้ว 12 ข้อ/57 จุด',
}
"""

SRC_DICT_EMPTY = """
WORD_BANNED = {}
"""

# 🔴 เหตุผลที่มี } อยู่ข้างใน ⇒ regex ตัดกลางคัน ⇒ ต้อง unparsable (แดง)
#    ⛔ ห้ามอ่านได้ครึ่งเดียวแล้วรายงานว่า ok
SRC_DICT_BRACE = """
WORD_BANNED = {
    'cosec': 'เขียน \\text{x} แบบนี้ไม่ได้',
}
"""

# (ชื่อเคส, ข้อความไฟล์, ตัวแปร, สถานะที่ต้องได้, ค่าที่ต้องได้)
PARSE_CASES = [
    ("ลิสต์บรรทัดเดียว", SRC_OK, 'ALLOWED_PATHS', 'ok', ['data/bank.json']),
    ("ทูเปิลหลายบรรทัด", SRC_MULTILINE, 'ALLOWED_KINDS', 'ok',
     ['multiple-correct', 'no-correct']),
    ("🔴 บรรทัดที่ถูกคอมเมนต์ ⛔ ห้ามนับ (ไม่งั้นเอาของจริงไปซ่อนใต้ # ได้)",
     SRC_COMMENTED, 'ALLOWED_PATHS', 'ok', ['data/bank.json']),
    ("มีแต่บรรทัดคอมเมนต์ ⇒ ถือว่าไม่มีตัวแปร",
     SRC_ONLY_COMMENT, 'ALLOWED_PATHS', 'absent', None),
    ("ไม่มีตัวแปรนี้เลย ⇒ absent ⛔ ไม่ใช่ลิสต์ว่าง",
     SRC_OK, 'ALLOWED_KINDS', 'absent', None),
    ("🔴 ประกาศ 2 ที่ ⇒ ตัดสินไม่ได้ ⛔ ห้ามหยิบอันสุดท้ายมาเงียบ ๆ",
     SRC_TWICE, 'ALLOWED_PATHS', 'multi', None),
    ("🔴 ค่าไม่ใช่ค่าคงที่ ⇒ อ่านไม่ออก ⛔ ห้ามเดา",
     SRC_WEIRD, 'ALLOWED_PATHS', 'unparsable', None),
    # ── ชั้น dict (v1.1) — WORD_BANNED ของ scan_symbols ───────────────
    ("dict {คำ: เหตุผล} หลายบรรทัด ⇒ ต้องได้ 'คีย์' (ก่อน v1.1 ได้ unparsable)",
     SRC_DICT, 'WORD_BANNED', 'ok', ['cosec']),
    ("dict ว่าง ⇒ ok + ลิสต์ว่าง ⛔ ไม่ใช่ absent (ประกาศไว้แล้วแต่ไม่มีสมาชิก)",
     SRC_DICT_EMPTY, 'WORD_BANNED', 'ok', []),
    ("🔴 เหตุผลมี } ข้างใน ⇒ unparsable = แดง ⛔ ห้ามอ่านครึ่งเดียวแล้วบอกว่า ok",
     SRC_DICT_BRACE, 'WORD_BANNED', 'unparsable', None),
    ("ตัวแปร dict ที่ไม่มีในไฟล์ ⇒ absent เหมือนเดิม",
     SRC_OK, 'WORD_BANNED', 'absent', None),
]

V = 'ALLOWED_PATHS'
OK_MSG = [f'แก้ด่าน 6\n\n{V}+: เพิ่มไฟล์ผลรวมชุดใหม่ตามมติครู 1 ส.ค.']

# (ชื่อเคส, prev, now, ข้อความ commit, รหัสที่ต้องเจอ | None = ต้องผ่าน)
#  ⛔ ใช้ชื่อไฟล์สมมติชุดใหม่ (aaa/bbb) ไม่ทับกับตัวอย่างจริงข้างบน — กับดัก ⑦ข
GROW_CASES = [
    ("ไม่มีอะไรเปลี่ยน ⇒ ผ่าน", ['aaa'], ['aaa'], [''], None),

    ("รายการหดลง ⇒ ผ่าน (ลดสิทธิ์ไม่ต้องขอ)", ['aaa', 'bbb'], ['aaa'], [''], None),

    ("สลับลำดับเฉย ๆ ⇒ ผ่าน (เทียบสมาชิก ไม่ใช่ลำดับ)",
     ['aaa', 'bbb'], ['bbb', 'aaa'], [''], None),

    ("🔴 เพิ่ม 1 รายการ ไม่ประกาศ ⇒ แดง", ['aaa'], ['aaa', 'bbb'], [''],
     'undeclared-growth'),

    ("เพิ่ม 1 รายการ + ประกาศครบ ⇒ ผ่าน", ['aaa'], ['aaa', 'bbb'], OK_MSG, None),

    ("🔴 ประกาศแต่ไม่ให้เหตุผล (โคลอนลอย ๆ) ⇒ แดง",
     ['aaa'], ['aaa', 'bbb'], [f'{V}+:   '], 'undeclared-growth'),

    ("🔴 ประกาศชื่อตัวแปรอื่น ⇒ แดง (ประกาศผิดช่องไม่นับ)",
     ['aaa'], ['aaa', 'bbb'], ['ALLOWED_KINDS+: เพิ่มชนิดใหม่ตามมติ'],
     'undeclared-growth'),

    ("ประกาศอยู่ในข้อความ commit ที่ 2 จาก 3 ⇒ ผ่าน",
     ['aaa'], ['aaa', 'bbb'], ['ปรับ log', OK_MSG[0], 'แก้คำผิด'], None),

    ("🔴 เอาออก 1 ใส่เข้า 1 (จำนวนเท่าเดิม) ⇒ ยังต้องแดง",
     ['aaa', 'bbb'], ['aaa', 'ccc'], [''], 'undeclared-growth'),

    ("🔴 ฐานไม่มีตัวแปรนี้ (ไฟล์เพิ่งเกิด) ⇒ ทั้งก้อนคือของใหม่ ⇒ แดง",
     None, ['aaa'], [''], 'undeclared-growth'),

    ("ฐานไม่มีตัวแปร แต่ที่ HEAD ก็ยังว่าง ⇒ ผ่าน", None, [], [''], None),

    ("🔴 ตัวแปรหายไปจาก HEAD (เปลี่ยนชื่อหนีด่าน) ⇒ แดง",
     ['aaa'], None, OK_MSG, 'var-gone'),

    ("สมาชิกซ้ำในตัวเอง ⇒ ไม่ถือว่าโต", ['aaa'], ['aaa', 'aaa'], [''], None),

    ("🔴 ข้อความ commit เป็น None ปนมา ⇒ ต้องไม่ล้ม และยังแดงตามเดิม",
     ['aaa'], ['aaa', 'bbb'], [None, ''], 'undeclared-growth'),
]


# 🧊 v1.2 · เคสของ FROZEN — เฝ้า **สองขา**
FROZEN_CASES = [
    ("ไม่มีอะไรเปลี่ยน ⇒ ผ่าน", ['aaa', 'bbb'], ['aaa', 'bbb'], [''], None),

    ("🔴 **ย่อรายการโดยไม่ประกาศ ⇒ แดง** (นี่คือรูที่ selftest ในไฟล์เดียวจับไม่ได้)",
     ['aaa', 'bbb'], ['aaa'], [''], 'undeclared-shrink'),

    ("ย่อรายการ + ประกาศ `-:` ครบ ⇒ ผ่าน",
     ['aaa', 'bbb'], ['aaa'], [f'{V}-: ซ่อมข้อนั้นครบแล้วจึงถอนชื่อออกตามมติครู'], None),

    ("🔴 ย่อรายการ แต่ประกาศผิดทิศ (`+:` แทน `-:`) ⇒ ยังแดง",
     ['aaa', 'bbb'], ['aaa'], OK_MSG, 'undeclared-shrink'),

    ("🔴 ย่อ + ประกาศ `-:` แต่ไม่ให้เหตุผล ⇒ แดง",
     ['aaa', 'bbb'], ['aaa'], [f'{V}-:   '], 'undeclared-shrink'),

    ("🔴 เติมโดยไม่ประกาศ ⇒ แดง (ขาขึ้นยังบังคับเหมือนเดิม)",
     ['aaa'], ['aaa', 'bbb'], [''], 'undeclared-growth'),

    ("🔴 เอาออก 1 ใส่เข้า 1 ⇒ ต้องแดง **ทั้งสองรหัส** (จับได้ที่ shrink)",
     ['aaa', 'bbb'], ['aaa', 'ccc'], [''], 'undeclared-shrink'),

    ("🔴 สำมะโนหายทั้งก้อนจาก HEAD ⇒ แดง",
     ['aaa'], None, [f'{V}-: ลบทิ้งทั้งก้อน'], 'var-gone'),

    ("สลับลำดับเฉย ๆ ⇒ ผ่าน", ['aaa', 'bbb'], ['bbb', 'aaa'], [''], None),
]

# 🔴 v1.2 · สถานะที่อ่านได้ที่ HEAD — เคสที่ v1.1 ปล่อยผ่านคือ 'absent'
HEAD_STATUS_CASES = [
    ('ok',         False, "อ่านออก ⇒ เดินต่อได้"),
    ('absent',     True,  "🔴 **ไม่พบตัวแปรเลย ⇒ ต้องแดง** (v1.1 ปล่อยผ่าน — รูของ 5ffc3a4)"),
    ('multi',      True,  "🔴 เจอหลายที่ ⇒ ตัดสินไม่ได้ ⇒ แดง"),
    ('unparsable', True,  "🔴 อ่านไม่ออก ⇒ ตัดสินไม่ได้ ⇒ แดง"),
]


def _mut_shrink_is_free(prev, now, messages, var):
    """🧬 มิวแทนต์: 'ย่อรายการไม่ต้องขออนุญาต' — คือพฤติกรรมของ growth_verdict เป๊ะ
       ⇒ ถ้าเคสของ FROZEN ⛔ ไม่ล้มกับมิวแทนต์ตัวนี้ แปลว่า FROZEN ⛔ ไม่ต่างจาก WATCHED"""
    return growth_verdict(prev, now, messages, var)


def _mut_absent_is_ok(st):
    """🧬 มิวแทนต์: กลับไปเป็น v1.1 — ดักแค่ multi/unparsable"""
    return None if st in ('ok', 'absent') else 'x'


def _mut_compare_len(prev, now, messages, var):
    """มิวแทนต์ ① เทียบด้วยจำนวนสมาชิก ⇒ สลับเข้า-ออกเท่ากันจะรอด"""
    if now is None:
        return [('var-gone', '')]
    base = [] if prev is None else prev
    if len(now) <= len(base) or declared(messages, var):
        return []
    return [('undeclared-growth', '')]


def _mut_any_plus(prev, now, messages, var):
    """มิวแทนต์ ② เห็น "+:" ที่ไหนก็ถือว่าประกาศแล้ว ⇒ ประกาศผิดช่องก็ผ่าน"""
    if now is None:
        return [('var-gone', '')]
    base = [] if prev is None else prev
    added = [x for x in now if x not in base]
    if not added:
        return []
    if any(isinstance(m, str) and '+:' in m for m in messages):
        return []
    return [('undeclared-growth', '')]


def _mut_ignore_var_gone(prev, now, messages, var):
    """มิวแทนต์ ③ ตัวแปรหายไปก็ถือว่าไม่มีอะไรโต ⇒ เปลี่ยนชื่อหนีด่านได้"""
    if now is None:
        return []
    return growth_verdict(prev, now, messages, var)


def _mut_never_red(prev, now, messages, var):
    """มิวแทนต์ ④ ไม่แดงเลย ⇒ กติกากลับไปอยู่แต่ในจดหมาย"""
    return []


def _mut_prev_absent_is_free(prev, now, messages, var):
    """มิวแทนต์ ⑤ ฐานไม่มีตัวแปร = ปล่อยผ่าน ⇒ สร้างไฟล์ใหม่แล้วใส่อะไรก็ได้"""
    if prev is None:
        return []
    return growth_verdict(prev, now, messages, var)


def _run_grow(fn):
    fails = []
    for name, prev, now, msgs, want in GROW_CASES:
        try:
            codes = [c for c, _ in fn(prev, now, msgs, V)]
            good = (codes == []) if want is None else (want in codes)
        except Exception:
            good = False
        if not good:
            fails.append(name)
    return fails


def selftest():
    print('─' * 62)
    print(f'SELF-TEST ด่าน 10 v{CHECKER_VERSION} — รายการที่อนุญาตต้องไม่โตเงียบ ๆ')
    print('─' * 62)
    ok = True

    print('  รายการที่เฝ้าอยู่:')
    for f, v in WATCHED:
        print(f'     {f} · {v}')
    print('  สำมะโนที่เฝ้าสองขา (FROZEN):')
    for f, v in FROZEN:
        print(f'     🧊 {f} · {v}')
    print()

    print('  ── อ่านค่ารายการจากไฟล์ (ข้อความล้วน ⛔ ไม่ import) ──')
    for name, src, var, want_st, want_v in PARSE_CASES:
        st, v = parse_list(src, var)
        good = (st == want_st) and (v == want_v)
        why = '' if good else f'   ← ได้ ({st}, {v})'
        print(f'  {"✅" if good else "🔴"}  {name}{why}')
        ok &= good

    print()
    print('  ── ตัดสินว่า "โตขึ้นโดยไม่ประกาศ" หรือไม่ ──')
    for name, prev, now, msgs, want in GROW_CASES:
        codes = [c for c, _ in growth_verdict(prev, now, msgs, V)]
        good = (codes == []) if want is None else (want in codes)
        why = '' if good else f'   ← ได้ {codes} ต้องการ {want}'
        print(f'  {"✅" if good else "🔴"}  {name}{why}')
        ok &= good

    print()
    print('  ── 🧊 v1.2 · สำมะโน (FROZEN) ต้องเฝ้า **สองขา** ──')
    for name, prev, now, msgs, want in FROZEN_CASES:
        codes = [c for c, _ in frozen_verdict(prev, now, msgs, V)]
        good = (codes == []) if want is None else (want in codes)
        why = '' if good else f'   ← ได้ {codes} ต้องการ {want}'
        print(f'  {"✅" if good else "🔴"}  {name}{why}')
        ok &= good

    print()
    print('  ── 🔴 v1.2 · สถานะที่อ่านได้ "ที่ HEAD" ต้องตัดสินถูกทุกค่า ──')
    for st, want_red, name in HEAD_STATUS_CASES:
        got_red = head_status_verdict(st) is not None
        good = got_red == want_red
        print(f'  {"✅" if good else "🔴"}  [{st}] {name}')
        ok &= good

    print()
    print('  ── ใส่บั๊กเข้าไปแล้วด่านต้องล้ม ──')
    print('     ⑦ข: แดงแล้วยังต้องถามต่อว่า “แดงเพราะเคสที่ตั้งใจหรือเปล่า”')
    for label, fails in (
        ('① เทียบด้วยจำนวนสมาชิก',        _run_grow(_mut_compare_len)),
        ('② เห็น "+:" ที่ไหนก็ผ่าน',       _run_grow(_mut_any_plus)),
        ('③ ตัวแปรหายไปก็ไม่ว่า',          _run_grow(_mut_ignore_var_gone)),
        ('④ ไม่แดงเลย',                    _run_grow(_mut_never_red)),
        ('⑤ ฐานไม่มีตัวแปร = ปล่อยผ่าน',   _run_grow(_mut_prev_absent_is_free)),
        ('🧊⑥ v1.2 · FROZEN ใช้กติกาขาขึ้นอย่างเดียว (= ย่อได้ฟรี)',
         [n for n, pv, nw, ms, wt in FROZEN_CASES
          if not (([c for c, _ in _mut_shrink_is_free(pv, nw, ms, V)] == [])
                  if wt is None else
                  (wt in [c for c, _ in _mut_shrink_is_free(pv, nw, ms, V)]))]),
        ('🔴⑦ v1.2 · absent ที่ HEAD = ปล่อยผ่าน (พฤติกรรมของ v1.1)',
         [n for st, wr, n in HEAD_STATUS_CASES
          if ((_mut_absent_is_ok(st) is not None) != wr)]),
    ):
        good = len(fails) > 0
        print(f'  {"✅" if good else "🔴"}  มิวแทนต์ {label} ⇒ ล้ม {len(fails)}/{len(GROW_CASES)} เคส')
        for f in fails[:2]:
            print(f'         ↳ จับได้ที่: {f}')
        ok &= good

    print()
    if not WATCHED:
        print('  🔴 รายการ WATCHED ว่าง ⇒ ด่านนี้จะเขียวตลอดกาลโดยไม่เฝ้าอะไร')
        ok = False
    else:
        print(f'  ✅  รายการ WATCHED ไม่ว่าง ({len(WATCHED)} รายการ)')
    if not FROZEN:
        print('  🔴 รายการ FROZEN ว่าง ⇒ ขาลงของสำมะโน ⛔ ไม่มีใครเฝ้า')
        ok = False
    else:
        print(f'  ✅  รายการ FROZEN ไม่ว่าง ({len(FROZEN)} รายการ)')

    print()
    if not ok:
        print('🔴 SELF-TEST ไม่ผ่าน ⇒ ผลของด่านนี้กับของจริงเชื่อไม่ได้')
        return 2
    print(f'✅ SELF-TEST ผ่านครบ {len(PARSE_CASES)} + {len(GROW_CASES)} '
          f'+ {len(FROZEN_CASES)} 🧊 + {len(HEAD_STATUS_CASES)} เคส + มิวแทนต์ 7 ตัว')
    return 0


# ── ฝั่งที่คุยกับ git ──────────────────────────────────────────
def git(*a):
    """คืน (สำเร็จไหม, ข้อความ) — ⛔ ห้ามกลืนรหัสออกของ git"""
    try:
        r = subprocess.run(('git',) + a, capture_output=True, text=True)
    except Exception as e:
        return False, str(e)
    if r.returncode != 0:
        return False, (r.stderr or '').strip()
    return True, r.stdout


def read_at_base(path, base):
    """หาค่า "ก่อนหน้า" ของไฟล์ที่เฝ้าอยู่ — คืน (สถานะ, ข้อความไฟล์, คอมมิตที่ใช้)

      'ok'       → ไฟล์มีอยู่ที่คอมมิตฐานตรง ๆ
      'historic' → ไฟล์ไม่มีที่ฐาน แต่เคยมีในประวัติ ⇒ ใช้ครั้งล่าสุดที่ยังมี
      'never'    → ไม่เคยมีไฟล์นี้ในประวัติเลย ⇒ ไม่มีของให้เทียบจริง ๆ

    🔴 ทำไมต้องมี 'historic':
       ถ้าเทียบเฉพาะที่คอมมิตฐาน คนที่อยากขยายสิทธิ์เงียบ ๆ แค่
       "ลบไฟล์ทิ้งแล้วสร้างใหม่ในคอมมิตเดียว" ก็ทำให้ด่านนี้เห็นเป็น
       "ไฟล์ใหม่ ไม่มีของเทียบ" ได้ทันที ⇒ ช่องโหว่ที่เขียนได้ใน 1 บรรทัด
       ⇒ ต้องไล่ย้อนประวัติหาเวอร์ชันล่าสุดที่ยังมีตัวไฟล์อยู่
    """
    ok, txt = git('show', f'{base}:{path}')
    if ok:
        return 'ok', txt, base
    ok2, out = git('rev-list', base, '--', path)
    if ok2:
        for sha in out.split()[:20]:
            ok3, txt3 = git('show', f'{sha}:{path}')
            if ok3:
                return 'historic', txt3, sha
    return 'never', None, None


def main():
    ap = argparse.ArgumentParser(
        description='ตรวจว่ารายการ "สิ่งที่อนุญาต" ไม่โตขึ้นโดยไม่ประกาศ')
    ap.add_argument('--base', default=None,
                    help='คอมมิตฐานที่จะเทียบด้วย (ถ้าไม่ระบุ ใช้ HEAD~1)')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    a = ap.parse_args()

    if a.version:
        print(CHECKER_VERSION)
        return 0
    if a.selftest:
        return selftest()

    base = a.base or 'HEAD~1'
    okb, _ = git('rev-parse', '--verify', base + '^{commit}')
    if not okb:
        print(f'🔴 หาคอมมิตฐาน "{base}" ไม่เจอ ⇒ เทียบไม่ได้')
        print('   ⛔ "เทียบไม่ได้" ไม่เท่ากับ "เทียบแล้วผ่าน"')
        print('   (ถ้าเป็นคอมมิตแรกของ repo หรือ checkout ตื้น ให้ตั้ง fetch-depth: 0)')
        return 2

    okm, msgs_raw = git('log', '--format=%B%x00', f'{base}..HEAD')
    if not okm:
        print(f'🔴 อ่านข้อความ commit ช่วง {base}..HEAD ไม่ได้')
        return 2
    messages = [m for m in msgs_raw.split('\x00') if m.strip()]
    if not messages:
        # ช่วงว่าง (เช่น HEAD = base) — ยังต้องอ่านข้อความของ HEAD เอง
        _, m1 = git('log', '-1', '--format=%B', 'HEAD')
        messages = [m1]

    print(f'ด่าน 10 v{CHECKER_VERSION} · เทียบ {base} → HEAD '
          f'· ข้อความ commit ในช่วง {len(messages)} ก้อน'
          f' · เฝ้า {len(WATCHED)} ขาขึ้น + {len(FROZEN)} 🧊 สองขา')
    print()

    red = 0
    for path, var, kind in ([(f, v, 'watched') for f, v in WATCHED]
                            + [(f, v, 'frozen') for f, v in FROZEN]):
        tag = '🧊' if kind == 'frozen' else ''
        # ── ค่า "ตอนนี้" อ่านจากไฟล์ที่จะถูกใช้จริง (working tree ของ CI) ──
        try:
            now_txt = open(path, encoding='utf-8').read()
        except Exception as e:
            print(f'🔴 อ่าน {path} ไม่ได้ — {e}')
            return 2
        st_now, v_now = parse_list(now_txt, var)
        # 🔴 v1.2 · ดักทุกสถานะที่ ⛔ ไม่ใช่ 'ok' — รวม 'absent' ที่ v1.1 ปล่อยผ่าน
        why = head_status_verdict(st_now)
        if why:
            print(f'🔴 {path} · {var} → {why}')
            return 2

        # ── ค่า "ที่ฐาน" อ่านจาก git โดยตรง ──
        how, prev_txt, at = read_at_base(path, base)
        if how == 'never':
            n = len(v_now or [])
            print(f'🟠 {path} · {var} {tag}— ไฟล์นี้ไม่เคยมีในประวัติก่อนหน้า '
                  f'({n} รายการ) ⇒ รอบนี้ยังไม่มีของให้เทียบ')
            # 🔑 〔52〕 · สถานะที่ไม่ใช่เขียว **ต้องประกาศเงื่อนไขที่จะทำให้มันเขียว**
            #    ประโยคข้างล่างเขียนได้เฉพาะเมื่อ st_now == 'ok' ซึ่งบังคับไว้ข้างบนแล้ว
            #    ⇒ ⇒ **ตัวประโยคเองคือด่าน** — ⛔ ไม่ต้องมีใครมาเฝ้าประโยคอีกชั้น
            print(f'     ⛔ "ยังไม่ได้เทียบ" ⛔ ไม่ใช่ "เทียบแล้วผ่าน"')
            print(f'     ✅ และรอบหน้าจะเฝ้าได้จริง **เพราะตัวอ่านอ่านตัวแปรนี้ออกแล้ว '
                  f'(สถานะ ok · {n} รายการ)** — ถ้าอ่านไม่ออก ด่านนี้แดงไปตั้งแต่บรรทัดบนแล้ว')
            continue
        if how == 'historic':
            print(f'🟠 {path} · {var} — ไฟล์ไม่มีที่คอมมิตฐาน '
                  f'⇒ ย้อนไปใช้ครั้งล่าสุดที่ยังมี ({at[:7]}) '
                  f'(กันวิธีลบทิ้งแล้วสร้างใหม่เพื่อล้างของเทียบ)')
        st_prev, v_prev = parse_list(prev_txt, var)
        if st_prev in ('multi', 'unparsable'):
            print(f'🔴 {path} · {var} ที่ฐานอ่านไม่ออก ({st_prev}) ⇒ เทียบไม่ได้')
            return 2

        probs = (frozen_verdict if kind == 'frozen' else growth_verdict)(
            v_prev, v_now, messages, var)
        shown_prev = '(ไม่มีที่ฐาน)' if v_prev is None else str(v_prev)
        shown_now = '(หายไปแล้ว)' if v_now is None else str(v_now)
        if probs:
            red += 1
            print(f'🔴 {path} · {var}')
            print(f'     ฐาน   : {shown_prev}')
            print(f'     HEAD  : {shown_now}')
            for code, msg in probs:
                print(f'     [{code}] {msg}')
        else:
            n = len(v_now or [])
            note = ('⛔ ไม่เปลี่ยนโดยไม่ประกาศ (เฝ้าสองขา)' if kind == 'frozen'
                    else 'ไม่โตขึ้นโดยไม่ประกาศ')
            print(f'✅ {path} · {var} {tag}— {n} รายการ {note}')
    print()
    if red:
        print(f'🔴 มี {red} รายการที่เปลี่ยนโดยไม่ประกาศ')
        return 1
    print(f'✅ ไม่มีรายการอนุญาตใดโตขึ้นโดยไม่ประกาศ '
          f'({len(WATCHED)} ขาขึ้น) · และ ⛔ ไม่มีสำมะโนใดถูกย่อโดยไม่ประกาศ '
          f'({len(FROZEN)} 🧊 สองขา)')
    return 0


if __name__ == '__main__':
    sys.exit(main())

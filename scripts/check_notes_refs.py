#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ด่าน 21 — `notes` ห้ามอ้างเอกสารที่ไม่มีอยู่
=============================================

**ปัญหาที่ด่านนี้เกิดมาแก้ (13 ส.ค. 69)**

ฟิลด์ `notes` ของข้อสอบเป็นที่เก็บ **หลักฐานว่าข้อนั้นถูกตรวจแล้วอย่างไร**
ธรรมเนียมที่ใช้กันมาตั้งแต่ก้อน b3 คือเขียนชื่อสคริปต์ที่ใช้ตรวจลงไปตรง ๆ เช่น
*"probe collide_b19.py: the pair (…) crossed with (…)"*

🔴 **แต่ชื่อที่เขียนไว้ ⛔ ไม่มีใครเคยตรวจว่ามันชี้ไปที่ของที่มีอยู่จริง**
   ⇒ วันที่สคริปต์ตัวนั้น ⛔ ไม่ถูก commit ขึ้นมาด้วย **บรรทัดหลักฐานยังอยู่เหมือนเดิมทุกตัวอักษร**
   ⇒ ⇒ ข้อนั้นยัง "มีหลักฐาน" ในสายตาคนอ่าน แต่ **⛔ ไม่มีใครเปิดดูได้อีกแล้ว**

⬤ **MB วัดเอง 13 ส.ค. 69 · คอมมิตฐาน `0b9f323` — เจอของจริง 27 ข้อ:**

     ก้อน b10 ..... 1 ข้ออ้าง collide · ชื่อที่ ⛔ ไม่มี **0**
     ก้อน b11 ..... 8 ข้อ ................. **0**
     ก้อน b15 ..... 2 ข้อ ................. **0**
     ก้อน b16 ..... 6 ข้อ ................. **0**
     ก้อน b17 ..... 5 ข้อ ................. **0**
     ก้อน b18 .... 12 ข้อ ................. **0**
     ก้อน b19 .... 42 ข้อ ................. **0**
     ก้อน b20 .... 35 ข้อ ................. 🔴 **35 (ทุกข้อ)**
     ก้อน b21 ..... 8 ข้อ ................. 🔴 **8 (ทุกข้อ)**
     ก้อน b23 .... 20 ข้อ ................. 🔴 **20 (ทุกข้อ) — เพิ่ม 22 ส.ค. 69**

   ⇒ ⇒ **b20 กับ b21 ⛔ ไม่ใช่ "พลาดบางข้อ" — มันพลาด *ทั้งก้อน* และเป็นสองก้อนเดียวที่พลาด**
   ⇒ ⇒ **b23 พลาดทั้งก้อนซ้ำอีกรอบ (22 ส.ค. 69)** — ทรงเดียวกับ b20/b21 เป๊ะ: `notes` ทุกข้ออ้าง
      `verify_b23.py` (ตัวตรวจฐานตอนแต่งข้อครั้งแรก 13 ส.ค.) และบางข้ออ้าง `collide_b23.py` /
      `stems_b23.py` เพิ่ม — **⛔ ไม่ใช่คนละเรื่องกับ `b23/verify_tri3.py`** ซึ่งเป็นตัวตรวจ
      ชั้นประยุกต์ 3-tier ที่เพิ่มทีหลังและมากับซองส่งมอบจริง (13 ส.ค.) จึง commit เข้าคลัง
      พร้อมกันได้ ⇒ ไม่ต้องปักหมุด — สองไฟล์นี้ทำหน้าที่คนละอย่าง แค่ชื่อคล้ายกัน

**🔑 ชื่อที่ ⛔ ไม่มีอยู่จริง — ยืนยันแล้วอย่างน้อย 2 ขาอิสระทุกชื่อ**

     collide_b20.py · collide_b20b.py · collide_b21.py · collide_b21b.py
     b20/w711/v130_131.py
     collide_b23.py · stems_b23.py · verify_b23.py   ← เพิ่ม 22 ส.ค. 69 (ก้อน b23)

     ขา ① `git log --all --diff-filter=A -- '*<ชื่อ>'` ⇒ **⛔ ไม่เคยถูก add เลยสักคอมมิตในประวัติทั้งหมด**
          ⇒ ⇒ นี่ ⛔ ไม่ใช่ "ของที่ถูกลบทีหลัง" — มัน ⛔ ไม่เคยขึ้น git
     ขา ② สำเนาทำงานบนดิสก์ครู `…\\math-bank\\tools\\authoring\\k2\\` (MB อ่านรายการเอง 13 ส.ค. ·
          ยืนยันซ้ำ 22 ส.ค.) ⇒ มี `collide_b3…b19` และ `collide_b22.py` ครบ ·
          **⛔ ไม่มีของ b20 / b21 / b23 เลยสักตัว**
     ขา ③ (b20/b21 เท่านั้น) ซองส่งมอบ `…\\_delivery-ก้อน20-21\\tools-b20-b21.tar.gz` (62 รายการ · MB แตกอ่านเอง)
          ⇒ **⛔ ไม่มีคำว่า `collide` เลยสักบรรทัด**

   ⇒ ⇒ ⇒ **สรุปที่พูดได้:** สิ่งที่ `notes` อ้างถึง **⛔ ไม่มีอยู่ในที่ที่เอื้อมถึงได้ทั้งสามที่**

**⛔ สิ่งที่ด่านนี้ ⛔ ไม่ได้พูด — ⛔ ห้ามอ่านเกิน**

  ⛔ ⛔ **ด่านนี้ ⛔ ไม่ได้บอกว่า "การกวาดหาการชนของ b20/b21 ⛔ ไม่เคยรัน"**
     สคริปต์อาจเคยมีอยู่จริงในรอบแต่ง แล้วหายไปพร้อมกับที่ทำงานของรอบนั้น
  ⛔ ⛔ **และ ⛔ ไม่ได้บอกว่าตัวลวงของ 27 ข้อนั้นผิด**
  ✅ สิ่งที่พูดได้มีอย่างเดียว: **หลักฐานที่ถูกอ้าง ⛔ ไม่สามารถเปิดดูหรือรันซ้ำได้**
     ⇒ ตัวเลข *"Collision sweep on 6417 items"* ที่ `notes` ของ q130 เขียนไว้
       ⛔ ไม่มีใครทำซ้ำได้ ⇒ มันเป็น **คำบอกเล่า** ⛔ ไม่ใช่ **การวัด** (㉚)

**กฎที่บังคับ**

  ①  `notes` ของข้อใดอ้างชื่อไฟล์ **ในคลัง** ที่หาไม่พบ ⇒ 🔴 แดง
      เว้นแต่ `id` ของข้อนั้นถูกปักหมุดไว้ใน `NOTES_REF_DEBT`
  ②  🔑 **หมุดที่ไม่มีของรองรับแล้ว ⇒ แดง** (ข้อหาย · `notes` เลิกอ้าง · ไฟล์ถูก commit เข้ามาแล้ว)
      ⇒ รายการนี้ **ย่อได้อย่างเดียว** — ทรงเดียวกับ `KNOWN_DUPE_IDS` ของด่าน 15
      ⇒ ⇒ และการย่อมัน **ต้องมาคู่กับการแก้ของจริง** ⛔ ย่อเปล่า ๆ ⛔ ไม่ได้
  ③  ตัวหารเป็นศูนย์ ⇒ แดง ("เขียวเพราะไม่ได้ตรวจอะไร" ต้องไม่หน้าตาเหมือน "เขียวเพราะสะอาด")
  ④  ชื่อไฟล์ **นอกคลัง** (PDF ต้นฉบับบนดิสก์ครู) ⇒ **พิมพ์รายงาน ⛔ ไม่ตัดสิน** (ดูจุดบอด)

**🔴 เขตอ้างอิง (㊾) — นิยามไว้ตั้งแต่วันเขียน ⛔ ไม่ปล่อยให้ความเงียบแปลว่าครอบคลุม**

  ที่อ่าน  : ฟิลด์ชื่อ `notes` ที่มีค่าเป็น **สตริง** เท่านั้น
  ขอบเขต  : `data/sets/*.json` = **ชั้นที่บังคับ**  ·  `data/_archive/*.json` = **ชั้นที่รายงาน**
             (⛔ ไม่บังคับ `_archive` — บทที่ปลดหลักสูตรแล้ว ⛔ ไม่ควรทำให้ CI แดง · ทรงเดียวกับด่าน 14)
  ⛔ ไม่อ่าน: `data/bank.json` (ของที่ถูกสร้าง ⇒ ซ้ำกับ `data/sets`) · ซอร์สใน `scripts/` · เอกสารใน `docs/`

  **เกณฑ์ว่า "ชี้ถึง"** — ชื่อจะถือว่าหาเจอ ถ้า **ข้อใดข้อหนึ่ง** จริง:
      (ก) path ตรงตัวจากรากคลังมีอยู่จริง            เช่น `tools/authoring/k2/molds.py`
      (ข) **ชื่อท้าย** ของมันมีอยู่ที่ใดก็ได้ในคลัง    เช่น `verify_b19.py`
  ⇒ เกณฑ์ (ข) **ใจกว้างโดยตั้งใจ** เพราะธรรมเนียมใน `notes` เขียนเป็นชื่อเปล่า ⛔ ไม่ใช่ path เต็ม
  ⇒ ⇒ **ราคาที่จ่ายให้ความใจกว้างนี้:** ถ้ามีไฟล์ชื่อพ้องกันคนละโฟลเดอร์ ด่านนี้จะปล่อยผ่าน
       ⇒ ⇒ ด่านนี้จับ **"⛔ ไม่มีของชื่อนี้เลย"** ⛔ ไม่ได้จับ **"ชี้ผิดตัว"** — คนละคำถาม คนละด่าน

**🔴 จุดบอดที่ด่านนี้ประกาศเอง ⛔ ไม่รอให้คนอื่นมาค้นพบ**

  ① **ชื่อไฟล์นอกคลังตรวจไม่ได้เลย** — `'13 แคลคูลัส โจทย์.pdf'` และ `'15 สถิติ เฉลย.pdf'`
     อยู่บนดิสก์ครู ⇒ CI มองไม่เห็น ⇒ ด่านนี้ **พิมพ์อย่างเดียว ⛔ ไม่ตัดสิน**
     ⇒ "เขียว" ของด่านนี้ ⛔ ไม่ใช่หลักฐานว่า PDF ที่ถูกอ้างมีอยู่
  ② **ด่านนี้อ่านแต่ *ชื่อ* ⛔ ไม่อ่าน *เนื้อ*** — ไฟล์ที่มีอยู่แต่เนื้อในไม่เกี่ยวกับข้อที่อ้าง
     จะผ่านฉลุย ⇒ นี่คือ **㊾ ที่ยังเปิดอยู่** และด่านนี้ ⛔ ไม่ปิดมัน
  ③ **ด่านนี้เห็นเฉพาะการอ้างที่ *มีนามสกุลไฟล์*** — ประโยคอย่าง "ตรวจด้วยตัวกวาดของก้อน 20"
     ⛔ ไม่มีนามสกุล ⇒ ด่านนี้มองไม่เห็น ⇒ **การเลี่ยงด่านนี้ทำได้ด้วยการเลิกเขียนชื่อไฟล์**
     ⇒ ⇒ 🔑 นั่นแปลว่า **ตัวเลข 27 เป็น "พื้น" ⛔ ไม่ใช่ "จำนวน"** (〔52〕)

**⛔ รายการ `NOTES_REF_DEBT` ถูกด่าน 10 เฝ้าอยู่**
  ลงทะเบียนไว้ใน `WATCHED` ของ `scripts/check_config_growth.py`
  ⇒ เติมชื่อเข้ามาเงียบ ๆ ⛔ ไม่ได้ — ต้องประกาศในข้อความคอมมิตว่า `NOTES_REF_DEBT+: <เหตุผล>`
  ⇒ **เลือก WATCHED ⛔ ไม่ใช่ FROZEN โดยตั้งใจ** — ต่างจาก `BLIND_CENSUS` ของด่าน 15:
       `BLIND_CENSUS` = **สำมะโนที่มีวันที่** ⇒ ย่อไม่ได้ ⇒ FROZEN (เฝ้าสองขา)
       `NOTES_REF_DEBT` = **หนี้ที่ต้องหมดไป**  ⇒ ย่อ = ใช้หนี้ ⇒ WATCHED (เฝ้าขาขึ้น)
     และการย่อมันเงียบ ๆ **ทำไม่ได้อยู่แล้ว** เพราะกฎ ② บังคับให้หมุดต้องมีของรองรับ
     ⇒ ⇒ หมุดที่ถูกถอนโดยที่ `notes` ยังอ้างของที่ไม่มี ⇒ **กฎ ① แดงทันที**

รหัสออก: 0 = ผ่าน · 1 = เนื้อหาแดง · 2 = ตัวเครื่องมือแดง
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

CHECKER_VERSION = '1.0'

DEFAULT_SCAN = Path('data/sets')
ARCHIVE_SCAN = Path('data/_archive')
REPO_ROOT = Path('.')
GROWTH_GUARD = 'scripts/check_config_growth.py'

# ── ตัวจับชื่อไฟล์ ────────────────────────────────────────────────────────────
#
# 🔴 **บทเรียนที่ต้องอยู่ตรงนี้ ⛔ ไม่ใช่ในจดหมาย — MB เจอกับตัวเอง 13 ส.ค. 69**
#
#    รุ่นแรกของตัวกวาดนี้เขียนว่า `[\w.]+\.pdf` แล้ว **อ่านชื่อไฟล์ไทยขาดกลางคำ**
#    เพราะ `์` (thanthakhat · U+0E4C) เป็น Unicode category **Mn** (เครื่องหมายไม่กินที่)
#    ⇒ `'์'.isalnum()` เป็น **False** ⇒ `\w` ของไพทอน **⛔ ไม่ครอบมัน**
#    ⇒ ⇒ `โจทย์.pdf` จึงถูกตัดหัวเหลือ `.pdf` แล้วหลุดตัวกรองไปเงียบ ๆ
#    ⇒ ⇒ ⇒ **ตัวกวาดรายงานว่า "เจอ 2 ข้อ" ทั้งที่ของจริงมี 4** — และมัน ⛔ ไม่แดง มันแค่ *นับขาด*
#
#    🔑 กฎที่ได้ และใช้ได้กับทุกด่านในคลังนี้:
#       **regex ที่ต้องกวาดข้อความไทย ⛔ ห้ามใช้ `\w` เป็นตัวแทน "ตัวอักษร"**
#       ให้เขียนช่วง `฀-๿` ตรง ๆ (คลุมทั้งพยัญชนะ สระ วรรณยุกต์ และเครื่องหมาย)
#    ⇒ มี selftest ⑤ / ⑥ เฝ้าไว้ ⛔ ไม่ปล่อยให้เป็นแค่คอมเมนต์ (⑦ก)
THAI = '฀-๿'

# ชั้น ก · ชื่อ**นอกคลัง** — มีอักษรไทย + นามสกุลเอกสาร ⇒ ของบนดิสก์ครู ⇒ ⛔ ไม่ตัดสิน
#   อนุญาตช่องว่างในกลุ่มนี้เท่านั้น เพราะชื่อจริงเป็นแบบ '13 แคลคูลัส โจทย์.pdf'
RE_EXTERNAL = re.compile(
    '[' + THAI + '][' + THAI + r'\w .\-]*\.(?:pdf|docx?|xlsx?)', re.IGNORECASE)

# ชั้น ข/ค · path **ในคลัง** — ASCII ล้วน ⛔ ไม่มีช่องว่าง
#   🔴 **⛔ ห้ามอนุญาตช่องว่างในกลุ่มนี้** — MB ลองแล้ว 13 ส.ค. 69 และมันกลืนทั้งประโยค
#      ได้ของปลอมออกมาว่า `'5/2. The independent route was … in b20/w711/v130_131.py'`
#      ⇒ ⇒ ตัวจับที่ใจกว้างเกินไป **สร้างชื่อไฟล์ที่ ⛔ ไม่มีใครเคยเขียน** แล้วรายงานว่ามันหาย
RE_REPO = re.compile(
    r'(?<![\w/.\-])((?:[A-Za-z0-9_\-.]+/)*[A-Za-z0-9_\-.]+'
    r'\.(?:md|json|py|js|html|yml|yaml|csv|txt|zip))(?![\w])')

# ── 🔴 หนี้ที่มีชื่อ — 27 ข้อ วัดเมื่อ 13 ส.ค. 2569 · คอมมิตฐาน 0b9f323 ──────────
#
# ⛔ **นี่คือ "หนี้ที่ต้องหมดไป" ⛔ ไม่ใช่ "สำมะโนที่มีวันที่"**
#    ⇒ วันที่ข้อไหนถูกแก้ (notes เลิกอ้างของที่ไม่มี · หรือไฟล์ถูก commit เข้ามาจริง)
#      **ให้ถอนชื่อออกจากรายการนี้** ⛔ ไม่ใช่ทำเครื่องหมายทิ้งไว้
#    ⇒ ⇒ ต่างจาก `BLIND_CENSUS` ของด่าน 15 ตรงนี้ — เหตุผลเต็มอยู่ในหัวไฟล์
#
# ⛔ ลิสต์แบน ⛔ ไม่มีป้ายชนิด ⛔ ไม่ซ้อนชั้น — ไม่งั้นตัวอ่านของด่าน 10 อ่านไม่ออก
#    (รูนี้เคยกัดด่าน 15 v1.0 มาแล้วจริง ๆ ⇒ ⛔ ไม่ใช่ความระวังเปล่า ๆ)
NOTES_REF_DEBT = [
    'gen-chap-07-trigonometry-q125',
    'gen-chap-07-trigonometry-q126',
    'gen-chap-07-trigonometry-q128',
    'gen-chap-07-trigonometry-q129',
    'gen-chap-07-trigonometry-q130',
    'gen-chap-07-trigonometry-q131',
    'gen-chap-07-trigonometry-q132',
    'gen-chap-07-trigonometry-q133',
    'gen-chap-07-trigonometry-q134',
    'gen-chap-07-trigonometry-q135',
    'gen-chap-07-trigonometry-q136',
    'gen-chap-07-trigonometry-q137',
    'gen-chap-07-trigonometry-q138',
    'gen-chap-07-trigonometry-q139',
    'gen-chap-07-trigonometry-q140',
    'gen-chap-07-trigonometry-q141',
    'gen-chap-07-trigonometry-q142',
    'gen-chap-07-trigonometry-q143',
    'gen-chap-07-trigonometry-q144',
    'gen-chap-07-trigonometry-q146',
    'gen-chap-07-trigonometry-q149',
    'gen-chap-07-trigonometry-q151',
    'gen-chap-07-trigonometry-q153',
    'gen-chap-07-trigonometry-q156',
    'gen-chap-07-trigonometry-q158',
    'gen-chap-07-trigonometry-q161',
    'gen-chap-07-trigonometry-q164',
    # 🆕 22 ส.ค. 2569 · ก้อน 23 (q165–q184) — commit ที่เพิ่มบล็อกนี้เดินคู่กับ
    #    `NOTES_REF_DEBT+:` ในข้อความ commit (บังคับโดยด่าน 10)
    #    รูปเดียวกับ b20/b21 เป๊ะ: ทุกข้อ notes อ้าง `verify_b23.py` (ตัวตรวจฐานตอนแต่งข้อ
    #    ครั้งแรก 13 ส.ค.) และบางข้ออ้าง `collide_b23.py` / `stems_b23.py` เพิ่ม — ทั้งสามชื่อ
    #    ⛔ ไม่เคยถูก commit หรือส่งมอบเป็นไฟล์เลย (ต่างจาก `b23/verify_tri3.py` ซึ่งเป็นคนละ
    #    ตัวคนละหน้าที่ — ตรวจเฉพาะชั้นประยุกต์ 3-tier ที่เพิ่มทีหลัง — และมากับซองจริง จึง
    #    commit เข้าคลังพร้อมกันได้ ⇒ ไม่ต้องปักหมุด) — ยืนยัน 2 ขา: ① `git log --all
    #    --diff-filter=A -- '*verify_b23.py' '*collide_b23.py' '*stems_b23.py'` ไม่เจอเลย
    #    ② ค้นดิสก์ครูทั้งโฟลเดอร์ที่เชื่อมได้ (`_delivery-qc`, `math-bank/tools/authoring/k2`,
    #    `สื่อการสอน`) ไม่เจอเช่นกัน
    'gen-chap-07-trigonometry-q165',
    'gen-chap-07-trigonometry-q166',
    'gen-chap-07-trigonometry-q167',
    'gen-chap-07-trigonometry-q168',
    'gen-chap-07-trigonometry-q169',
    'gen-chap-07-trigonometry-q170',
    'gen-chap-07-trigonometry-q171',
    'gen-chap-07-trigonometry-q172',
    'gen-chap-07-trigonometry-q173',
    'gen-chap-07-trigonometry-q174',
    'gen-chap-07-trigonometry-q175',
    'gen-chap-07-trigonometry-q176',
    'gen-chap-07-trigonometry-q177',
    'gen-chap-07-trigonometry-q178',
    'gen-chap-07-trigonometry-q179',
    'gen-chap-07-trigonometry-q180',
    'gen-chap-07-trigonometry-q181',
    'gen-chap-07-trigonometry-q182',
    'gen-chap-07-trigonometry-q183',
    'gen-chap-07-trigonometry-q184',
]

# 🔑 ชื่อที่หายไป — เก็บเป็น **ข้อมูล** เพื่อให้ selftest ยืนบนข้อมูล ⛔ ไม่ยืนบนถ้อยคำ
#    (บทเรียน ② ของด่าน 15 v1.3: ตรึงถ้อยคำ = ลงโทษการแก้ให้ถูก)
MISSING_NAMES = [
    'collide_b20.py',
    'collide_b20b.py',
    'collide_b21.py',
    'collide_b21b.py',
    'b20/w711/v130_131.py',
    # 🆕 22 ส.ค. 2569 · ก้อน 23 — ดูเหตุผลที่ NOTES_REF_DEBT ด้านบน
    'collide_b23.py',
    'stems_b23.py',
    'verify_b23.py',
]

# ── 🧬 ฟิกซ์เจอร์สังเคราะห์ของ selftest ────────────────────────────────────────
#
# 🔑 **เหตุผลที่มันต้องมีอยู่ แม้รายการหนี้จะยาว 27 บรรทัดวันนี้** (บทเรียน ① ด่าน 15 v1.3)
#    มิวแทนต์ที่สร้างจากรายการจริง จะกลายเป็นลิสต์ว่างในวันที่หนี้ถูกใช้หมด
#    (= วันที่งานสำเร็จ) ⇒ เคส "ต้องแดง" จะเขียวเงียบ ๆ
#    ⇒ ⇒ **ชุดทดสอบต้องเป็นเจ้าของวัตถุทดสอบของตัวเอง**
# ⛔ รหัสข้อขึ้นต้น 'chap-00-' ซึ่ง ⛔ ไม่มีอยู่จริงในคลัง ⇒ ⛔ ไม่มีวันชนของจริง
FIX_ID = 'chap-00-fixture-q01'
FIX_CLEAN_ID = 'chap-00-fixture-q02'
FIX_MISSING = 'ghost_probe_zz9.py'      # ⛔ ⛔ ไม่มีวันมีไฟล์ชื่อนี้ในคลัง
FIX_PRESENT = 'build_bank.py'           # มีจริงใน scripts/ ⇒ ใช้ทดสอบขา "ต้องเงียบ"
FIX_DEBT = [FIX_ID]


# ── ชั้นอ่านไฟล์ ──────────────────────────────────────────────────────────────
def iter_notes(paths):
    """คืน (ไฟล์, id ของข้อ, ข้อความ notes) ทีละตัว

    ⛔ เดินทั้งต้นไม้ ⛔ ไม่สมมติว่า notes อยู่ชั้นบนสุดของข้อ
       (บางชุดเก็บ notes ซ้อนอยู่ในบล็อกย่อย ⇒ การสมมติทรงคือการนับขาดเงียบ ๆ)
    """
    out = []

    def walk(node, qid, fname):
        if isinstance(node, dict):
            if isinstance(node.get('id'), str):
                qid = node['id']
            for key, val in node.items():
                if key == 'notes' and isinstance(val, str):
                    out.append((fname, qid, val))
                walk(val, qid, fname)
        elif isinstance(node, list):
            for val in node:
                walk(val, qid, fname)

    for p in paths:
        try:
            data = json.loads(Path(p).read_text(encoding='utf-8'))
        except Exception as exc:                       # noqa: BLE001
            raise RuntimeError(f'อ่าน {p} ไม่ได้: {exc}') from exc
        walk(data, None, str(p))
    return out


def repo_index(root=REPO_ROOT):
    """ดัชนีของไฟล์ทุกตัวในคลัง — เก็บทั้ง path เต็มและชื่อท้าย (ดูเกณฑ์ (ก)/(ข) ในหัวไฟล์)"""
    names = set()
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d != '.git']
        for f in files:
            rel = os.path.relpath(os.path.join(base, f), root)
            names.add(rel.replace(os.sep, '/'))
            names.add(f)
    return names


def refs_in(text):
    """แยกการอ้างในข้อความเดียว ⇒ (ชื่อนอกคลัง, ชื่อในคลัง)"""
    external = sorted({m.strip() for m in RE_EXTERNAL.findall(text)})
    inrepo = sorted(set(RE_REPO.findall(text)))
    return external, inrepo


def resolve(name, index):
    """เกณฑ์ (ก) path ตรงตัว หรือ (ข) ชื่อท้ายมีอยู่ที่ใดก็ได้"""
    return name in index or os.path.basename(name) in index


def scan(paths, index):
    """คืน (ตัวหาร, ข้อที่อ้างของหาย, ชื่อนอกคลัง)

    ตัวหาร = จำนวนฟิลด์ notes ที่เป็นสตริง (⛔ ไม่ใช่จำนวนข้อ — ประกาศหน่วยไว้ที่นี่)
    """
    divisor = 0
    broken = {}
    external = {}
    for fname, qid, text in iter_notes(paths):
        divisor += 1
        ext, inrepo = refs_in(text)
        for e in ext:
            external.setdefault(e, set()).add(qid)
        missing = [n for n in inrepo if not resolve(n, index)]
        if missing and qid:
            broken.setdefault(qid, set()).update(missing)
    return divisor, {k: sorted(v) for k, v in broken.items()}, external


def verdict(divisor, broken, debt):
    """คืน (รายการแดง, รายการบรรทัดที่ต้องพิมพ์เสมอ)

    🔑 พิมพ์รายการหมุด **ในรอบที่เขียวด้วย** (เงื่อนไข E→MB #61 §2)
       ⇒ "เขียว" ของด่านนี้แปลว่า *⛔ ไม่มีการอ้างของหาย นอกจากรายการที่พิมพ์อยู่ตรงนี้*
    """
    red = []
    lines = []
    if divisor <= 0:
        red.append(('empty-divisor',
                    '🔴 ตัวหารเป็นศูนย์ — ⛔ ไม่พบฟิลด์ notes เลยสักตัว '
                    '⇒ "เขียว" รอบนี้ ⛔ ไม่ได้แปลว่าสะอาด มันแปลว่า ⛔ ไม่ได้ตรวจอะไร'))

    pinned = set(debt)
    for qid in sorted(broken):
        if qid not in pinned:
            red.append(('unpinned-missing-ref',
                        f'🔴 {qid} · `notes` อ้างของที่หาไม่พบ: '
                        f'{" · ".join(broken[qid])} ⇒ ⛔ ไม่ได้ปักหมุดไว้'))

    # กฎ ② — หมุดที่ไม่มีของรองรับ
    for qid in sorted(pinned):
        if qid not in broken:
            red.append(('pin-without-backing',
                        f'🔴 หมุด {qid} ⛔ ไม่มีของรองรับแล้ว '
                        '(ข้อหาย · notes เลิกอ้าง · หรือไฟล์ถูก commit เข้ามาแล้ว) '
                        '⇒ ถอนชื่อออกจาก NOTES_REF_DEBT'))

    for qid in sorted(pinned & set(broken)):
        lines.append(f'  📌 {qid} → {" · ".join(broken[qid])}')
    return red, lines


# ── ชั้นทดสอบตัวเอง ───────────────────────────────────────────────────────────
def selftest():                                        # noqa: C901
    src = Path(__file__).read_text(encoding='utf-8')
    passed = []
    failed = []

    def say(tag, desc, cond):
        (passed if cond else failed).append(f'{tag} {desc}')

    idx = repo_index()

    # ── ① ชั้นแยกการอ้าง
    say('①', 'ชื่อในคลังธรรมดา ⇒ จับได้',
        refs_in('probe verify_b19.py ran clean')[1] == ['verify_b19.py'])
    say('②', 'path มีโฟลเดอร์ ⇒ จับทั้ง path ⛔ ไม่ตัดเหลือชื่อท้าย',
        refs_in('see b20/w711/v130_131.py here')[1] == ['b20/w711/v130_131.py'])
    say('③', '(ต้องไม่จับ) ข้อความไม่มีนามสกุลไฟล์ ⇒ เงียบ',
        refs_in('ตรวจด้วยตัวกวาดของก้อน 20 แล้ว')[1] == [])
    say('④', '🔴 ตัวจับในคลังต้อง ⛔ ไม่กลืนช่องว่าง '
             '(รุ่นที่กลืน สร้างชื่อไฟล์ที่ ⛔ ไม่มีใครเขียนขึ้นมาเอง)',
        refs_in('answer is 5/2. checked in b20/w711/v130_131.py')[1]
        == ['b20/w711/v130_131.py'])

    # ── ② 🔴 ขาไทย — บทเรียนที่ด่านนี้เกิดมาพร้อมกับมัน
    say('⑤', '🔴 ชื่อไฟล์ไทยที่ลงท้ายด้วย ์ ต้องถูกจับเป็น "นอกคลัง" ครบคำ '
             '(`\\w` ของไพทอน ⛔ ไม่ครอบ U+0E4C ⇒ รุ่นแรกอ่านขาด)',
        refs_in("E เปิด '13 แคลคูลัส โจทย์.pdf' หน้า 26")[0] == ['แคลคูลัส โจทย์.pdf'])
    say('⑥', '🧬 และตัวอักษรตัวนั้นต้อง ⛔ ไม่ใช่ \\w จริง ๆ '
             '⇒ ถ้าวันหนึ่งไพทอนเปลี่ยนนิยาม เคสนี้จะเตือนก่อน',
        re.fullmatch(r'\w', '์') is None)
    say('⑦', 'ชื่อไทยต้อง ⛔ ไม่ถูกนับเป็น "ในคลัง" (ไม่งั้นด่านจะแดงเพราะของบนดิสก์ครู)',
        refs_in("'15 สถิติ เฉลย.pdf'")[1] == [])

    # ── ③ ชั้นชี้ถึง
    say('⑧', 'เกณฑ์ (ข) ชื่อท้ายที่มีอยู่จริง ⇒ ถือว่าชี้ถึง',
        resolve(FIX_PRESENT, idx))
    say('⑨', 'ชื่อที่ ⛔ ไม่มีในคลัง ⇒ ชี้ไม่ถึง', not resolve(FIX_MISSING, idx))
    say('⑩', 'เกณฑ์ (ก) path ตรงตัวจากรากคลัง ⇒ ชี้ถึง',
        resolve('scripts/check_notes_refs.py', idx))

    # ── ④ ชั้นคำตัดสิน · ยืนบนฟิกซ์เจอร์ของตัวเอง ⛔ ไม่ยืมรายการจริง
    fix_broken = {FIX_ID: [FIX_MISSING]}
    say('⑪', 'ของหายที่ปักหมุดไว้ ⇒ เขียว',
        verdict(1, fix_broken, FIX_DEBT)[0] == [])
    say('⑫', '🧬 ของหายที่ ⛔ ไม่ได้ปักหมุด ⇒ ต้องแดง',
        any(c == 'unpinned-missing-ref' for c, _ in verdict(1, fix_broken, [])[0]))
    say('⑬', '🧬 กฎ ② หมุดที่ไม่มีของรองรับ ⇒ ต้องแดง',
        any(c == 'pin-without-backing' for c, _ in verdict(1, {}, FIX_DEBT)[0]))
    say('⑭', '🧬 ตัวหารศูนย์ ⇒ ต้องแดง แม้ ⛔ ไม่มีของหายเลย',
        any(c == 'empty-divisor' for c, _ in verdict(0, {}, [])[0]))
    say('⑮', 'หมุดที่มีของรองรับ ต้องได้บรรทัดพิมพ์ 1 บรรทัด (เขียวก็ต้องพิมพ์)',
        len(verdict(1, fix_broken, FIX_DEBT)[1]) == 1)
    say('⑯', '🧬 ฟิกซ์เจอร์ที่ ⛔ ไม่ถูกมิวเทต ต้องเขียว '
             '(คู่บังคับของ ⑫⑬ — ไม่งั้น "แดงเสมอ" จะดูเหมือนผ่าน)',
        verdict(2, {FIX_ID: [FIX_MISSING]}, FIX_DEBT)[0] == []
        and verdict(2, {}, [])[0] == [])

    # ── ⑤ ชั้นของจริง
    real = sorted(str(p) for p in DEFAULT_SCAN.glob('*.json'))
    divisor, broken, external = scan(real, idx)
    say('⑰', f'ตัวหารของจริงต้องไม่เป็นศูนย์ (วัดได้ {divisor})', divisor > 0)
    say('⑱', f'ของจริงพบข้ออ้างของหาย {len(broken)} ข้อ · '
             f'ปักหมุดไว้ {len(NOTES_REF_DEBT)} ข้อ ⇒ ต้องเขียว',
        verdict(divisor, broken, NOTES_REF_DEBT)[0] == [])
    say('⑲', 'รายการหนี้ต้อง ⛔ ไม่มีชื่อซ้ำ (ชื่อซ้ำ = ตัวหารเฟ้อโดยไม่มีใครเห็น)',
        len(set(NOTES_REF_DEBT)) == len(NOTES_REF_DEBT))
    say('⑳', 'หัวไฟล์ต้องประกาศ **รายชื่อไฟล์ที่หาย** ครบทุกตัว '
             '⛔ ยืนบนข้อมูล ⛔ ไม่ยืนบนถ้อยคำ',
        all(n in __doc__ for n in MISSING_NAMES))
    say('㉑', '🔑 รายชื่อที่หายในหัวไฟล์ ต้องเป็นชุดเดียวกับที่ *วัดได้จากคลังจริง* '
              '⇒ หัวไฟล์โกหกไม่ได้',
        set(MISSING_NAMES) == {n for v in broken.values() for n in v})
    say('㉒', 'ทุกข้อในรายการหนี้ ต้องมีอยู่ในผลวัดจริง (⛔ ไม่มีหมุดลอย)',
        set(NOTES_REF_DEBT) == set(broken))

    # ── ⑥ ชั้นลงทะเบียนกับด่าน 10 — **ยาที่อยู่นอกไฟล์นี้**
    reg = Path(GROWTH_GUARD).read_text(encoding='utf-8')
    # ⛔ ต่อ needle ตอนรัน ⛔ ไม่เขียนเป็นสตริงตรง ๆ (㊾ — ไม่งั้นด่านอื่นที่กวาดซอร์สจะจับใบนี้เอง)
    #    และต่อจาก **path จริงของไฟล์นี้** ⇒ วันที่ไฟล์ถูกย้าย/เปลี่ยนชื่อ เคสนี้จะแดง
    #    ซึ่ง **ถูกต้อง** — เพราะทะเบียนของด่าน 10 ต้องถูกแก้ตามในคอมมิตเดียวกัน
    needle = "'scripts/" + os.path.basename(__file__) + "', 'NOTES_REF_DEBT'"
    say('㉓', '🔑 รายการหนี้ต้องลงทะเบียนใน WATCHED ของด่าน 10 '
              '(ไฟล์เป็นพยานของความครบของตัวเองไม่ได้ ⇒ หลักยึดต้องอยู่นอกไฟล์)',
        needle in reg)
    say('㉔', '…และต้องอยู่ใน **WATCHED** ⛔ ไม่ใช่ FROZEN '
              '(หนี้ต้องย่อได้ · สำมะโนต้องย่อไม่ได้ — คนละทรง)',
        needle in reg
        and reg.index('WATCHED = [') < reg.index(needle)
        and (('FROZEN = [' not in reg) or reg.index(needle) < reg.index('FROZEN = [')))

    mod = _load_growth()
    if mod is None:
        say('㉕', 'โหลดตัวอ่านของด่าน 10 มารันจริงได้', False)
    else:
        status, got = mod.parse_list(src, 'NOTES_REF_DEBT')
        say('㉕', '🔑 ตัวอ่านของด่าน 10 ต้องอ่าน NOTES_REF_DEBT ออก**จริง** '
                  '⛔ ไม่ใช่แค่มีชื่ออยู่ในทะเบียน (รูนี้เคยเปิดอยู่จริงในด่าน 10)',
            status == 'ok' and sorted(got or []) == sorted(NOTES_REF_DEBT))
        say('㉖', '🧬 และด่าน 10 ต้องแดงจริงถ้ารายการโตโดยไม่ประกาศ',
            any(c == 'undeclared-growth' for c, _ in mod.growth_verdict(
                NOTES_REF_DEBT, NOTES_REF_DEBT + ['chap-00-fixture-q99'],
                [''], 'NOTES_REF_DEBT')))
        say('㉗', '…และต้องเงียบเมื่อประกาศถูกต้อง (ไม่งั้นด่านที่แดงเสมอ = ด่านที่ถูกปิด)',
            mod.growth_verdict(
                NOTES_REF_DEBT, NOTES_REF_DEBT + ['chap-00-fixture-q99'],
                ['NOTES_REF_DEBT+: ก้อนใหม่อ้างสคริปต์ที่ยังไม่ commit'],
                'NOTES_REF_DEBT') == [])

    # ── ⑦ ชั้นประกาศจุดบอด
    say('㉘', 'หัวไฟล์ต้องประกาศว่าชื่อ**นอกคลัง**ตรวจไม่ได้ '
              '⇒ ยืนบนข้อมูล: ชื่อนอกคลังที่วัดได้จริงต้องไม่เป็นศูนย์',
        len(external) > 0)
    say('㉙', 'ชื่อนอกคลังต้อง ⛔ ไม่มีวันทำให้แดง (แม้จะหาไฟล์ไม่เจอ)',
        verdict(1, {}, [])[0] == [])
    say('㉚', 'ด่านนี้ต้องประกาศเองว่า 27 เป็น "พื้น" ⛔ ไม่ใช่ "จำนวน"',
        'พื้น' in __doc__ and '〔52〕' in __doc__)

    print(f'ด่าน 21 · check_notes_refs v{CHECKER_VERSION} — self-test')
    for line in passed:
        print(f'  ✅ {line}')
    for line in failed:
        print(f'  ❌ {line}')
    # ⛔ ห้ามพิมพ์เลขที่เขียนด้วยมือ — นับเอง (㉚ ของทะเบียน)
    print(f'  ── ผ่าน {len(passed)} · ล้ม {len(failed)} · รวม {len(passed) + len(failed)} เคส')
    return 0 if not failed else 1


def _load_growth():
    """โหลด check_config_growth.py มาเป็นโมดูล เพื่อ **เรียกตัวอ่านของจริง** มาพิสูจน์"""
    import importlib.util
    try:
        spec = importlib.util.spec_from_file_location('_cg', GROWTH_GUARD)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except Exception:                                  # noqa: BLE001
        return None


# ── ชั้นรัน ───────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(
        description='ด่าน 21 — notes ห้ามอ้างเอกสารที่ไม่มีอยู่')
    ap.add_argument('root', nargs='?', default=str(DEFAULT_SCAN),
                    help='โฟลเดอร์ที่บังคับ (ปริยาย data/sets)')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    args = ap.parse_args()

    if args.version:
        print(CHECKER_VERSION)
        return 0
    if args.selftest:
        return selftest()

    root = Path(args.root)
    if not root.is_dir():
        print(f'🔴 ⛔ ไม่พบโฟลเดอร์ {root}', file=sys.stderr)
        return 2

    try:
        index = repo_index()
        paths = sorted(str(p) for p in root.glob('*.json'))
        divisor, broken, external = scan(paths, index)
    except RuntimeError as exc:
        print(f'🔴 {exc}', file=sys.stderr)
        return 2

    print(f'ด่าน 21 · check_notes_refs v{CHECKER_VERSION}')
    print(f'  ⑨ ตัวหาร: ฟิลด์ `notes` ที่เป็นสตริง = {divisor} '
          f'จาก {len(paths)} ไฟล์ใน {root}  ⬤ ชั้นที่**บังคับ**')

    # ชั้นที่รายงานอย่างเดียว — _archive
    if ARCHIVE_SCAN.is_dir():
        apaths = sorted(str(p) for p in ARCHIVE_SCAN.glob('*.json'))
        if apaths:
            ad, ab, _ = scan(apaths, index)
            print(f'  ⑪ ชั้นที่**รายงาน**: {ARCHIVE_SCAN} — notes {ad} ตัว · '
                  f'ข้อที่อ้างของหาย {len(ab)} ข้อ  ⛔ ไม่มีผลต่อรหัสออก')
            for qid in sorted(ab):
                print(f'       ⚠️ {qid} → {" · ".join(ab[qid])}')

    print(f'  🔒 ชื่อ**นอกคลัง** (ดิสก์ครู) {len(external)} ชื่อ — ⛔ ด่านนี้ไม่ตัดสิน:')
    for name in sorted(external):
        print(f'       📄 {name} ← {len(external[name])} ข้อ')

    red, pin_lines = verdict(divisor, broken, NOTES_REF_DEBT)

    print(f'  📌 หนี้ที่ปักหมุดไว้ {len(NOTES_REF_DEBT)} ข้อ '
          f'(พิมพ์ทุกรอบ ⛔ ไม่ใช่เฉพาะรอบที่แดง):')
    for line in pin_lines:
        print(line)

    if red:
        print()
        for _, msg in red:
            print(f'  {msg}')
        print(f'\n🔴 ด่าน 21 แดง — {len(red)} เรื่อง')
        return 1

    print('\n✅ ด่าน 21 เขียว — ⛔ ไม่มีการอ้างเอกสารที่หาไม่พบ '
          'นอกเหนือจากรายการหนี้ที่พิมพ์ไว้ข้างบน')
    return 0


if __name__ == '__main__':
    sys.exit(main())

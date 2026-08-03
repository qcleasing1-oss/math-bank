#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_image_markers.py — ด่าน "หมุดรูปต้องชี้รูปที่มีจริง"
==============================================================================

⚠️ ที่มาของไฟล์นี้ (2 ส.ค. 2569)

   หมุด `[IMAGE:n]` ในเฉลย ⛔ ไม่ใช่ป้ายกำกับ — มันคือ **คำสั่งย้ายรูป**
   (viewer/admin.html ~1918–1930): รูปที่ถูกหมุดเรียก จะไปโผล่ตรงหมุด
   และรูปที่ **ไม่มีหมุดเรียก** จะไปโผล่ **พร้อมโจทย์**
   ⇒ หมุดที่หายไป 1 ตัว = รูปเฉลยเด้งไปอยู่หน้าโจทย์ = เด็กเห็นคำตอบก่อนทำ

   ระหว่างวัด "รัศมีของปัญหารูปบอกคำตอบ" ให้ทีมพอร์ทัล พบว่า
   **254 ข้อ จาก 2,150 ข้อที่มีรูป มีคำตอบพิมพ์อยู่บนตัวรูป**
   ⇒ สำหรับ 254 ข้อนี้ "หมุดทำงานถูก" คือสิ่งเดียวที่กั้นเด็กจากคำตอบ
     ไม่มีชั้นป้องกันอื่นเลย ⇒ ความถูกต้องของหมุดต้องมีด่าน ไม่ใช่ความระมัดระวัง

   และพบว่ามีหมุดอยู่รูปแบบหนึ่งที่ **อ่านได้สองความหมายพร้อมกัน**:
   หมุดเปล่า `[IMAGE]` (ไม่มี `:n`)
      · viewer/admin.html และ viewer/export.js ใช้ /\\[IMAGE(?::(\\d+))?\\]/g
        ⇒ **จับได้** แล้วแปลว่าดัชนี 0 ⇒ รูปอยู่ในเฉลย
      · ตัวอ่านที่ใช้รูปแบบเข้ม /\\[IMAGE:(\\d+)\\]/ (เช่นที่ทีมพอร์ทัลใช้อยู่ช่วงหนึ่ง)
        ⇒ **จับไม่ได้เลย** ⇒ ข้อนั้นถูกอ่านว่า "ไม่มีหมุด" ⇒ รูปไปอยู่หน้าโจทย์
   ⇒ ข้อมูลชุดเดียวกัน ให้ผลตรงข้ามกันสุดขั้วกับผู้อ่านสองราย
     และ **ไม่มีฝ่ายไหนผิด** — นี่คือความกำกวมของตัวข้อมูลเอง
   (นี่คือที่มาของตัวเลข 204 vs 201 และ 106 vs 103 ในสำมะโนบทบาทรูป)

──────────────────────────────────────────────────────────────────────────────
ข้อตกลงรหัสออก (ตามข้อตกลงกลางของคลัง: 0 ผ่าน · 1 เนื้อหาแดง · 2 เครื่องมือแดง)

    0 = หมุดทุกตัวในตัวหารชี้รูปที่มีจริง และหมุดเปล่าตรงกับรายการอนุญาตเป๊ะ
    1 = ตัดสินได้ว่าผิด ได้แก่
        · หมุดเปล่าโผล่ในข้อที่ไม่ได้อยู่ในรายการอนุญาต (ความกำกวมกำลังลาม)
        · ข้อในรายการอนุญาต **ไม่มีหมุดเปล่าแล้ว** (รายการค้าง)
          ⇒ "พิสูจน์ว่าไม่เพิ่ม" ≠ "พิสูจน์ว่าไม่ลด" (กับดัก ⑩)
             รายการที่ลดแล้วไม่มีใครบังคับให้ลบ จะกลายเป็นใบอนุญาตถาวรของของที่ไม่มีอยู่
        · จำนวนจุด/ฟิลด์ของข้อในรายการไม่ตรงกับที่ประกาศไว้
        · หมุดชี้ดัชนีเกินจำนวนรูปที่ข้อนั้นมี  (`[IMAGE:3]` แต่มีรูป 2 รูป)
        · มีหมุดแต่ข้อนั้นไม่มี imageSpec เลย
        · ข้อความที่ "เกือบเป็นหมุด" แต่ไม่มีตัวอ่านรายไหนจับได้
          (`[image]` · `[IMAGE ]` · `[ IMAGE:1 ]`) ⇒ รูปหายเงียบ
    2 = ตัดสินไม่ได้ ได้แก่
        · ไม่มีโฟลเดอร์ data/sets · ไม่มีไฟล์ .json · ไม่มีข้อเลย  ← ตัวหารเป็นศูนย์ (⑨)
        · ไฟล์ชุดอ่านไม่ได้ / ไม่ใช่ JSON / ไม่มีลิสต์ questions
          ⇒ ด่านนี้ไม่ประกาศว่าเนื้อหาผิด เพราะมัน **วัดไม่ได้** ต่างหาก
        · รายการอนุญาตในไฟล์นี้เองผิดรูป (เหตุผลสั้น/ไม่ครบช่อง)
        · **ของล่อของกฎใดกฎหนึ่งไม่ทำงาน** (v1.1) ⇒ เลข "จับ N" ของกฎนั้นอ่านไม่ได้
          ⇒ ของที่อ่านไม่ได้ ⛔ ไม่ใช่ของที่ผ่าน

⛔ "ตรวจไม่ได้" ไม่เท่ากับ "ตรวจแล้วผ่าน"

──────────────────────────────────────────────────────────────────────────────
⑨ ตัวหารที่ด่านนี้บังคับ — ประกาศไว้ ⛔ ห้ามให้ความเงียบแปลว่าครอบคลุม

   คลังที่บังคับ = **ไฟล์ `data/sets/*.json` เท่านั้น** (กับดัก ⑪)
     เหตุผล: data/bank.json เป็น **ของที่ถูกสร้าง** ไม่ใช่ของที่คนแก้
     ⇒ ตั้งด่านที่ของที่ถูกสร้าง = จับได้ช้ากว่าหนึ่งรุ่นเสมอ และแก้ที่นั่นไม่ได้

   สิ่งที่จงใจอยู่ **นอก** ตัวหาร (วัดแล้ว ณ bb32125 ⇒ พิมพ์ให้เห็น ไม่ตัดเงียบ):
     · data/manifest.json — 4 จุด แต่เป็น **ข้อความบันทึกงาน** ที่พูดถึงหมุด
       ("แทรก [IMAGE] marker ที่ขาด 9 ข้อ") ⛔ ไม่ใช่หมุดที่ตัวอ่านจะเจอ
       เพราะไม่ได้อยู่ในฟิลด์ของข้อ ⇒ ถ้านับ จะเป็นแดงปลอมถาวร
     · data/_archive/*.json — 46 จุด · บท 16 ปลดจากหลักสูตรแล้ว ไม่ถูกเสิร์ฟให้ใคร
     · viewer/*.js|html และ docs/*.md — เป็นซอร์สกับเอกสารที่ **อธิบาย** รูปแบบหมุด
       ด่านที่จับเอกสารของตัวเอง คือด่านที่จะโดนถอดทิ้ง
   ⇒ ตัวเลขนอกตัวหารถูกพิมพ์ทุกครั้ง แต่ ⛔ ไม่มีผลต่อรหัสออก

   ภายในข้อหนึ่ง ๆ: อ่านทุกฟิลด์ **ยกเว้น `imageSpec`**
     เหตุผล: ข้อความในสเปกรูปคือของที่ถูกวาดลงบนรูป ไม่ใช่ตำแหน่งวางรูป

──────────────────────────────────────────────────────────────────────────────
🔴 ขอบเขตที่ด่านนี้ ⛔ ตัดสินไม่ได้ (ประกาศไว้ ไม่ให้เขียวถูกอ่านเกินจริง)

   · "ข้อนี้ **ควร** มีหมุดไหม" — ตัดสินไม่ได้จากข้อมูล ต้องอ่านเฉลยด้วยคน
     ⇒ นั่นคืองาน C1 (เติมหมุดย้อนหลัง) ไม่ใช่ด่านนี้
   · "รูปนี้บอกคำตอบไหม" — คนละด่าน คนละตัวหาร (⑨)
   · หมุดที่อยู่ในข้อที่ไม่มี id ⇒ ใส่รายการอนุญาตไม่ได้ ⇒ ถ้ามีหมุดเปล่าก็แดง

──────────────────────────────────────────────────────────────────────────────
⑦ข ระวัง "เขียวเพราะไม่มีของให้จับ":
   กฎ ข/ค/ง ปัจจุบันจับได้ 0 จุดทั้งสิ้น (วัดที่ bb32125: เกินดัชนี 0 · กำพร้า 0 ·
   เกือบเป็นหมุด 0) ⇒ เขียวของสามกฎนี้ **ไม่ใช่หลักฐานว่ากฎทำงาน**

   🔴 v1.1 (3 ส.ค. 69 · เงื่อนไขจากทีมพอร์ทัล E→MB #11 §3)
      เดิม "แต่ละกฎยิงจริง" ถูกพิสูจน์ใน `--selftest` เท่านั้น ⇒ คนที่อ่าน**รายงานของ
      การรันจริง** ยังแยกไม่ออกว่า `จับ 0` แปลว่า "สะอาด" หรือ "กฎตาย"
      ⇒ ตั้งแต่ v1.1 **ทุกกฎมีของล่อของตัวเอง และของล่อถูกยิงทุกครั้งที่รันจริง**
        รายงานพิมพ์แยกกฎ:  `กฎ ข · … : จับ 0 ข้อ · ของล่อ 3/3 ✅`
        ⇒ เลข 0 อ่านได้ เพราะบรรทัดเดียวกันมีหลักฐานว่ากฎยังยิงเป็น
      ⛔ ห้ามพิมพ์รวมเป็น "จับ 0 ทั้งหมด" — 0 ที่ไม่มีของล่อกำกับ คือ 0 ที่อ่านไม่ได้
      ⛔ ห้ามให้ `ของล่อ 0/0` พิมพ์ ✅ — กฎที่ไม่มีของล่อ = รหัส 2
      ของล่อมีสองขั้วเสมอ: **ของล่อบวก** (ของเสียที่กฎต้องจับ) และ **ของล่อลบ**
      (ของสะอาดที่หน้าตาใกล้เคียง ที่กฎต้อง**ไม่**จับ) ⇒ กันทั้ง "กฎตาย" และ "กฎยิงมั่ว"

การใช้:
    python scripts/check_image_markers.py            # ตรวจคลังจริง (รากคือ .)
    python scripts/check_image_markers.py --root .   # ระบุรากเอง
    python scripts/check_image_markers.py --selftest # ด่านของตัวด่านเอง
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile

CHECKER_VERSION = '1.1'

SETS_DIR = os.path.join('data', 'sets')

# ── รูปแบบหมุด ────────────────────────────────────────────────────────────────
# ⚠️ ตัวนี้ต้องเป็น "ไบต์ต่อไบต์" เดียวกับที่ viewer/admin.html ใช้
#    ⛔ ห้ามทำให้เข้มขึ้นเพื่อให้ด่านเงียบ — เข้มขึ้นเมื่อไร ด่านจะเลิกเห็นหมุดเปล่า
#      ซึ่งเป็นของชิ้นเดียวที่ด่านนี้ตั้งขึ้นมาเพื่อจับ
MARK = re.compile(r'\[IMAGE(?::(\d+))?\]')
BARE = re.compile(r'\[IMAGE\]')

# "เกือบเป็นหมุด" — ผ่อนช่องว่างและตัวพิมพ์เล็ก แล้วค่อยหักตัวที่ถูกต้องออก
# ⛔ ห้ามผ่อนจนจับ `[IMG]` หรือ `(IMAGE)` — ของพวกนั้นไม่มีใครตั้งใจให้เป็นหมุด
NEAR = re.compile(r'\[\s*image\s*(?::\s*\d+\s*)?\]', re.I)

# ── ชั้นของฟิลด์ (กับดัก ⑪ — ฟิลด์ที่เด็กเห็น ต่างจากฟิลด์บันทึกงาน) ──────────
# ⚠️ ชั้นนี้ใช้ "รายงาน" ⛔ ไม่ใช้ "ตัดสิน"
#    เหตุผล: วัดแล้ว หมุดเปล่าทั้ง 3 จุดอยู่ใน explanation (ชั้นเด็กเห็น) ทั้งหมด
#    ⇒ ถ้าวันหนึ่งมีหมุดโผล่ในฟิลด์บันทึกงาน นั่นเป็นของใหม่ที่ต้องมีคนมอง
#      ⇒ ให้เห็นในรายงานทันที ⛔ ไม่ใช่ปล่อยผ่านเพราะ "ไม่ใช่ฟิลด์ที่เด็กเห็น"
STUDENT_FIELDS = ('question', 'explanation', 'choices', 'hint', 'accept',
                  'correct', 'answer')
BOOK_FIELDS = ('notes', 'sourceTag', 'tags', 'flawedSource', 'patchLog',
               'review', 'comment', 'level', 'score')


def field_layer(top):
    if top in STUDENT_FIELDS:
        return 'เด็กเห็น'
    if top in BOOK_FIELDS:
        return 'บันทึกงาน'
    return 'ไม่จัดชั้น'


# ─────────────────────────────────────────────────────────────
# รายการอนุญาต — หมุดเปล่าที่ "มีอยู่ก่อนตั้งด่าน" และยังแก้ไม่ได้
#
# 🔴 นี่คือรายการ **ชั่วคราว** ปลายทางคือว่าง
#    ทางแก้จริงคือเปลี่ยน `[IMAGE]` เป็น `[IMAGE:0]` ทั้ง 3 จุด (ความหมายไม่เปลี่ยน
#    สำหรับ admin.html แต่ความกำกวมกับตัวอ่านเข้มหายไป)
#    ⛔ ยังทำไม่ได้ตอนนี้ เพราะ 2 ใน 3 อยู่ในชุดข้อสอบจริง (สามัญ 2555 / 2558)
#      ซึ่งมีมติว่า "แตะชุดข้อสอบจริง ต้องขออนุมัติแยกใบ ⛔ ห้ามทำเงียบ ๆ"
#
# ⚠️ รายการนี้ถูก ด่าน 10 (รายการอนุญาตห้ามโตเงียบ ๆ) เฝ้าอยู่ ⇒ โตเมื่อไรต้องประกาศ
#    และด่านนี้เองบังคับ **ขาลง** ด้วย: รายการที่ค้าง = แดง (กับดัก ⑩)
#
# รูปแบบ: id -> (ฟิลด์ชั้นบนสุดที่หมุดอยู่, จำนวนจุดในข้อนั้น, เหตุผล)
# ─────────────────────────────────────────────────────────────
ALLOW_BARE = {
    'samn-2555-01-q12': (
        'explanation', 1,
        'ชุดข้อสอบจริง (วิชาสามัญ 2555) — การแก้ตัวอักษรในชุดข้อสอบจริงต้องมีใบอนุมัติแยก'
        ' ตามมติ 1 ส.ค. 69 ⛔ ห้ามแก้เงียบ ๆ · ทางแก้ที่เตรียมไว้: [IMAGE] -> [IMAGE:0]'),
    'samn-2558-01-q27': (
        'explanation', 1,
        'ชุดข้อสอบจริง (วิชาสามัญ 2558) — เหตุผลเดียวกับ samn-2555-01-q12'
        ' · ทางแก้ที่เตรียมไว้: [IMAGE] -> [IMAGE:0]'),
    'chap-07-trigonometry-q22': (
        'explanation', 1,
        'ชุดแต่งเอง แก้ได้ทันที แต่จงใจรวมไปกับอีก 2 ข้อในใบเดียว'
        ' เพราะแก้ทีละข้อจะทำให้รายการนี้ไม่มีวันว่าง และไม่มีใครเห็นว่ามันควรว่าง'),
}
MIN_REASON = 40


def check_allowlist(table=None):
    """รายการอนุญาตต้องอ่านได้จริง — คืน (ผ่านไหม, ปัญหา[])

    ⛔ รายการที่ผิดรูป = ด่านที่ตัดสินด้วยของที่อ่านไม่ออก ⇒ ต้องเป็นรหัส 2
       ไม่ใช่รหัส 1 (ของที่ถูกตรวจไม่ได้ผิดอะไร — เครื่องมือต่างหากที่พัง)
    """
    t = ALLOW_BARE if table is None else table
    bad = []
    if not isinstance(t, dict):
        return False, ['ALLOW_BARE ต้องเป็น dict {id: (ฟิลด์, จำนวน, เหตุผล)}']
    for k, v in t.items():
        if not (isinstance(v, tuple) and len(v) == 3):
            bad.append('%s: ต้องเป็น (ฟิลด์, จำนวน, เหตุผล) 3 ช่อง' % k)
            continue
        fld, cnt, why = v
        if not isinstance(fld, str) or not fld:
            bad.append('%s: ช่องฟิลด์ว่าง' % k)
        if not isinstance(cnt, int) or isinstance(cnt, bool) or cnt < 1:
            bad.append('%s: จำนวนจุดต้องเป็นจำนวนเต็ม >= 1' % k)
        if not isinstance(why, str) or len(why.strip()) < MIN_REASON:
            bad.append('%s: เหตุผลสั้นกว่า %d ตัวอักษร — ใบอนุญาตที่ไม่มีเหตุผล'
                       ' คือการปิดด่านที่หน้าตาเหมือนการประกาศ' % (k, MIN_REASON))
    return not bad, bad


# ─────────────────────────────────────────────────────────────
# ส่วนวัด — ฟังก์ชันบริสุทธิ์ ทดสอบได้โดยไม่ต้องมีคลัง
# ─────────────────────────────────────────────────────────────
def walk_strings(value, path, out):
    """เก็บ (เส้นทางฟิลด์, สตริง) ทุกตัวที่อยู่ใต้ value

    ⛔ ต้องลงทั้ง dict และ list — กับดัก ④ (walker ที่ไม่ลง dict) เคยกัดมาแล้ว
    """
    if isinstance(value, str):
        out.append((path, value))
    elif isinstance(value, dict):
        for k, v in value.items():
            walk_strings(v, '%s.%s' % (path, k) if path else str(k), out)
    elif isinstance(value, list):
        for i, v in enumerate(value):
            walk_strings(v, '%s[%d]' % (path, i), out)
    return out


def n_figures(spec):
    """จำนวนรูปที่ข้อนี้มี — สเปกมี 3 ทรง: dict / list ของ dict / list ซ้อน list"""
    if isinstance(spec, dict):
        return 1
    if isinstance(spec, list):
        return len(spec)
    return 0


def scan_question(q):
    """วัดข้อเดียว — คืน dict ของสิ่งที่พบ ⛔ ยังไม่ตัดสินอะไร

    คืน: id, nfig, indices(set), bare[(path,layer,ctx)], near[(path,ข้อความ)],
         n_str, n_char
    """
    qid = q.get('id')
    nfig = n_figures(q.get('imageSpec'))
    indices, bare, near = set(), [], []
    n_str = n_char = 0
    for k, v in q.items():
        if k == 'imageSpec':          # ⛔ ข้อความบนรูป ไม่ใช่ตำแหน่งวางรูป
            continue
        for path, s in walk_strings(v, str(k), []):
            n_str += 1
            n_char += len(s)
            for m in MARK.finditer(s):
                indices.add(int(m.group(1)) if m.group(1) else 0)
            top = path.split('.')[0].split('[')[0]
            for m in BARE.finditer(s):
                a = max(0, m.start() - 40)
                b = min(len(s), m.end() + 40)
                bare.append((path, field_layer(top), s[a:b].replace('\n', ' ')))
            for m in NEAR.finditer(s):
                txt = m.group(0)
                if MARK.fullmatch(txt):
                    continue          # `[IMAGE]` และ `[IMAGE:3]` ถูกต้องอยู่แล้ว
                near.append((path, txt))
    return {'id': qid, 'nfig': nfig, 'indices': indices, 'bare': bare,
            'near': near, 'n_str': n_str, 'n_char': n_char}


def scan_questions(questions, setname='<mem>'):
    """วัดทั้งชุด — คืน (สรุปตัวหาร, findings[])

    findings แต่ละตัว: (ชนิด, setname, qid, รายละเอียด)
    ชนิด: 'bare' · 'oor' (ชี้เกินดัชนี) · 'orphan' (มีหมุดแต่ไม่มีรูป) · 'near'
    """
    div = {'q': 0, 'str': 0, 'char': 0, 'marked': 0, 'withfig': 0}
    found = []
    per_q_bare = {}
    for q in questions:
        r = scan_question(q)
        div['q'] += 1
        div['str'] += r['n_str']
        div['char'] += r['n_char']
        if r['indices']:
            div['marked'] += 1
        if r['nfig']:
            div['withfig'] += 1
        qid = r['id'] or '<ไม่มี id>'
        if r['bare']:
            per_q_bare[qid] = (setname, r['bare'])
        for path, txt in r['near']:
            found.append(('near', setname, qid,
                          'ข้อความ %r ที่ %s — ⛔ ไม่มีตัวอ่านรายไหนจับได้'
                          ' ⇒ รูปจะหายเงียบ' % (txt, path)))
        if r['indices'] and r['nfig'] == 0:
            found.append(('orphan', setname, qid,
                          'มีหมุด %s แต่ข้อนี้ไม่มี imageSpec เลย'
                          % sorted(r['indices'])))
        elif r['indices'] and max(r['indices']) >= r['nfig']:
            found.append(('oor', setname, qid,
                          'หมุด %s แต่มีรูปแค่ %d รูป (ดัชนีสูงสุดที่ใช้ได้คือ %d)'
                          % (sorted(r['indices']), r['nfig'], r['nfig'] - 1)))
    return div, found, per_q_bare


def verdict_bare(per_q_bare, allow):
    """เทียบหมุดเปล่าที่พบ กับรายการอนุญาต — สองทางเสมอ (กับดัก ⑩)

    คืน problems[] (ว่าง = ตรงกันเป๊ะ)
    """
    problems = []
    for qid, (setname, hits) in sorted(per_q_bare.items()):
        if qid not in allow:
            problems.append(
                '🔴 หมุดเปล่าในข้อที่ไม่ได้อยู่ในรายการอนุญาต: %s (%s) %d จุด'
                ' — ชั้น %s' % (qid, setname, len(hits),
                                '/'.join(sorted({h[1] for h in hits}))))
            continue
        fld, cnt, _ = allow[qid]
        tops = sorted({h[0].split('.')[0].split('[')[0] for h in hits})
        if len(hits) != cnt:
            problems.append('🔴 %s: รายการอนุญาตประกาศ %d จุด แต่พบ %d จุด'
                            % (qid, cnt, len(hits)))
        if tops != [fld]:
            problems.append('🔴 %s: รายการอนุญาตประกาศฟิลด์ %r แต่พบที่ %s'
                            % (qid, fld, tops))
    for qid in sorted(allow):
        if qid not in per_q_bare:
            problems.append(
                '🔴 รายการอนุญาตค้าง: %s ไม่มีหมุดเปล่าแล้ว'
                ' ⇒ ต้องลบบรรทัดนี้ออกจาก ALLOW_BARE ในคอมมิตเดียวกับที่แก้ข้อมูล'
                ' ("พิสูจน์ว่าไม่เพิ่ม" ≠ "พิสูจน์ว่าไม่ลด")' % qid)
    return problems


# ─────────────────────────────────────────────────────────────
# ของล่อประจำกฎ (v1.1) — ⛔ ไม่ใช่ self-test มันถูกยิงทุกครั้งที่รันจริง
#
# 🔴 เหตุผลที่ต้องอยู่ในเส้นทางการรันจริง ไม่ใช่ใน --selftest:
#    รายงานของการรันจริงคือสิ่งที่คนอ่าน แล้วตัดสินใจว่า "ผ่าน"
#    ถ้าหลักฐานว่ากฎยังยิงเป็น อยู่คนละคำสั่งกับรายงาน ⇒ คนอ่านรายงานไม่มีหลักฐานนั้น
#    ⇒ `จับ 0` จะถูกอ่านว่า "สะอาด" ทั้งที่อาจแปลว่า "กฎตาย" (B8 ข้อ 1)
#
# รูปแบบ: รหัสกฎ -> [(ชื่อ, 'ยิง'|'เงียบ', ข้อ[], รายการอนุญาตที่ใช้ (เฉพาะกฎ ก))]
#   'ยิง'   = ของล่อบวก — ของเสียที่กฎนี้ **ต้อง** จับ  ⇒ กัน "กฎตาย"
#   'เงียบ' = ของล่อลบ  — ของสะอาดหน้าตาใกล้เคียงที่กฎนี้ **ต้องไม่** จับ ⇒ กัน "กฎยิงมั่ว"
# ⛔ ของล่อทุกตัวเป็นของในหน่วยความจำล้วน — ห้ามแตะคลังจริงหรือรายการอนุญาตจริง
# ─────────────────────────────────────────────────────────────
def _q(qid, **kw):
    q = {'id': qid, 'question': 'โจทย์', 'explanation': ['ขั้นที่ 1']}
    q.update(kw)
    return q


DECOY_RULES = ('ก', 'ข', 'ค', 'ง')
DECOY_KIND = {'ข': 'oor', 'ค': 'orphan', 'ง': 'near'}   # กฎ ก ตัดสินด้วย verdict_bare

# 🔴 หมุดปักจำนวนของล่อขั้นต่ำ (กับดัก ⑩ อีกครั้ง)
#    ของล่อที่ "ผ่านหมด" พิสูจน์แค่ว่าของล่อ **ที่เหลืออยู่** ยังผ่าน
#    ⛔ ไม่ได้พิสูจน์ว่าไม่มีใครถอดของล่อออกเงียบ ๆ — `ของล่อ 2/2 ✅` ที่เคยเป็น 3/3
#      อ่านเหมือนเดิมทุกตัวอักษร ⇒ จำนวนต้องถูกปักไว้ ไม่ใช่นับจากของที่เหลือ
DECOY_MIN = {'ก': 3, 'ข': 3, 'ค': 3, 'ง': 4}

_DECOY_ALLOW_STALE = {
    'ล่อ-ค้าง': ('explanation', 1,
                 'รายการอนุญาตของล่อ — ใช้พิสูจน์ขาลงของกฎ ก (⑩) ว่ายังบังคับอยู่จริง'),
}

DECOYS = {
    'ก': [
        ('หมุดเปล่าในข้อที่ไม่มีใบอนุญาต ⇒ ต้องแดง', 'ยิง',
         [_q('ล่อ-ก1', explanation=['[IMAGE]'], imageSpec={'type': 't'})], None),
        ('ใบอนุญาตค้างโดยไม่มีหมุดเปล่าแล้ว ⇒ ต้องแดง (⑩ ขาลง)', 'ยิง',
         [_q('ล่อ-ก2', explanation=['[IMAGE:0]'], imageSpec={'type': 't'})],
         _DECOY_ALLOW_STALE),
        ('`[IMAGE:0]` ดัชนีชัดเจน ⛔ ไม่ใช่หมุดเปล่า ⇒ ต้องเงียบ', 'เงียบ',
         [_q('ล่อ-ก3', explanation=['[IMAGE:0]'], imageSpec={'type': 't'})], None),
    ],
    'ข': [
        ('`[IMAGE:3]` แต่มีรูป 2 รูป ⇒ ต้องแดง', 'ยิง',
         [_q('ล่อ-ข1', explanation=['[IMAGE:0]', '[IMAGE:3]'],
             imageSpec=[{'type': 't'}, {'type': 't'}])], None),
        ('`[IMAGE:1]` กับรูป 2 รูป (ดัชนีสูงสุดพอดี) ⇒ ต้องเงียบ', 'เงียบ',
         [_q('ล่อ-ข2', explanation=['[IMAGE:1]'],
             imageSpec=[{'type': 't'}, {'type': 't'}])], None),
        ('`[IMAGE:0]` กับรูปเดี่ยวแบบ dict ⇒ ต้องเงียบ', 'เงียบ',
         [_q('ล่อ-ข3', explanation=['[IMAGE:0]'], imageSpec={'type': 't'})], None),
    ],
    'ค': [
        ('มีหมุดแต่ไม่มี imageSpec เลย ⇒ ต้องแดง', 'ยิง',
         [_q('ล่อ-ค1', explanation=['[IMAGE:1]'])], None),
        ('ไม่มีหมุดและไม่มีรูป (ข้อธรรมดา) ⇒ ต้องเงียบ', 'เงียบ',
         [_q('ล่อ-ค2', explanation=['ไม่มีรูปในข้อนี้'])], None),
        ('มีหมุดและมีรูปครบ ⇒ ต้องเงียบ', 'เงียบ',
         [_q('ล่อ-ค3', explanation=['[IMAGE:0]'], imageSpec={'type': 't'})], None),
    ],
    'ง': [
        ('`[image]` ตัวพิมพ์เล็ก ⇒ ต้องแดง', 'ยิง',
         [_q('ล่อ-ง1', explanation=['[image]'], imageSpec={'type': 't'})], None),
        ('`[ IMAGE:1 ]` มีช่องว่างใน ⇒ ต้องแดง', 'ยิง',
         [_q('ล่อ-ง2', explanation=['[ IMAGE:1 ]'],
             imageSpec=[{'type': 't'}, {'type': 't'}])], None),
        ('`[IMAGE:1]` ที่ถูกต้อง ⇒ ต้องเงียบ', 'เงียบ',
         [_q('ล่อ-ง3', explanation=['[IMAGE:1]'],
             imageSpec=[{'type': 't'}, {'type': 't'}])], None),
        ('`[IMG]` ⛔ ไม่มีใครตั้งใจให้เป็นหมุด ⇒ ต้องเงียบ (กันตัวจับหลวมเกิน)', 'เงียบ',
         [_q('ล่อ-ง4', explanation=['[IMG] และ (IMAGE)'], imageSpec={'type': 't'})],
         None),
    ],
}


def run_decoys(decoys=None, scan=None, verdict=None):
    """ยิงของล่อของทุกกฎ — คืน {รหัสกฎ: (ผ่าน, ทั้งหมด, ปัญหา[])}

    ⛔ กฎที่ไม่มีของล่อ = ปัญหา ไม่ใช่ 0/0 ✅
       (0/0 ที่พิมพ์ ✅ คือคำโกหกที่หน้าตาเหมือนหลักฐาน)
    """
    table = DECOYS if decoys is None else decoys
    scan = scan_questions if scan is None else scan
    verdict = verdict_bare if verdict is None else verdict
    out = {}
    for rule in DECOY_RULES:
        cases = list(table.get(rule) or [])
        probs, npass = [], 0
        if not cases:
            probs.append('🔴 กฎ %s ไม่มีของล่อเลย ⇒ เลข "จับ N" ของกฎนี้อ่านไม่ได้'
                         ' ว่าเป็นความสะอาดหรือความตายของกฎ' % rule)
        else:
            # ⑩ ขาลง: "ของล่อผ่านหมด" พิสูจน์แค่ของล่อ **ที่ยังเหลืออยู่**
            #    ⇒ จำนวนต้องเทียบกับหมุดที่ปักไว้ ไม่ใช่กับจำนวนที่เหลือ
            floor = DECOY_MIN.get(rule, 1)
            if len(cases) < floor:
                probs.append('🔴 กฎ %s มีของล่อ %d ตัว แต่หมุด DECOY_MIN ปักไว้ %d'
                             ' ⇒ **ของล่อถูกถอดออกเงียบ ๆ (⑩)**'
                             ' ⇒ เลข "จับ" ของกฎนี้อ่านไม่ได้' % (rule, len(cases), floor))
            # สองขั้ว: ถ้ามีแต่ของล่อบวก จะจับ "กฎยิงมั่ว" ไม่ได้
            #          ถ้ามีแต่ของล่อลบ จะจับ "กฎตาย" ไม่ได้
            wants = {w for _, w, _, _ in cases}
            if wants != {'ยิง', 'เงียบ'}:
                probs.append('🔴 กฎ %s ของล่อมีขั้วเดียว (%s) ⇒ จับได้แค่ด้านเดียว'
                             ' ⇒ เลข "จับ" ของกฎนี้อ่านไม่ได้'
                             % (rule, '/'.join(sorted(wants)) or 'ไม่มี'))
        for name, want, qs, allow in cases:
            try:
                _, found, bare = scan(qs, '<ของล่อ>')
                if rule == 'ก':
                    fired = bool(verdict(bare, allow or {}))
                else:
                    fired = any(f[0] == DECOY_KIND[rule] for f in found)
            except Exception as e:                       # noqa: BLE001
                probs.append('🔴 กฎ %s · ของล่อระเบิด: %s — %s' % (rule, name, e))
                continue
            if fired == (want == 'ยิง'):
                npass += 1
            elif want == 'ยิง':
                probs.append('🔴 กฎ %s ไม่ยิงใส่ของล่อ: %s'
                             ' ⇒ **กฎตาย** ⇒ เลข "จับ" ของกฎนี้อ่านไม่ได้' % (rule, name))
            else:
                probs.append('🔴 กฎ %s ยิงใส่ของสะอาด: %s'
                             ' ⇒ **กฎยิงมั่ว** ⇒ เลข "จับ" ของกฎนี้เชื่อไม่ได้'
                             % (rule, name))
        out[rule] = (npass, len(cases), probs)
    return out


def decoy_tag(res, rule):
    """ข้อความท้ายบรรทัดของกฎ — `ของล่อ 3/3 ✅` หรือ `ของล่อ 2/3 ⛔`"""
    npass, total, probs = res.get(rule, (0, 0, ['ไม่ได้ยิงของล่อของกฎนี้']))
    ok = (total > 0 and npass == total and not probs)
    return 'ของล่อ %d/%d %s' % (npass, total, '✅' if ok else '⛔')


# ─────────────────────────────────────────────────────────────
# ส่วนอ่านคลัง
# ─────────────────────────────────────────────────────────────
def load_sets(root):
    """อ่าน data/sets/*.json — คืน (รายการ (ชื่อ, questions), เหตุผลที่ตัดสินไม่ได้)

    ⛔ ไฟล์ที่อ่านไม่ออกแม้แต่ไฟล์เดียว ⇒ ตัดสินไม่ได้ทั้งด่าน
       เพราะหมุดที่หายไปอาจอยู่ในไฟล์นั้นพอดี — "อ่านไม่ได้" ไม่ใช่ "ไม่มี"
    """
    d = os.path.join(root, SETS_DIR)
    if not os.path.isdir(d):
        return None, 'ไม่มีโฟลเดอร์ %s' % d
    names = sorted(f for f in os.listdir(d) if f.endswith('.json'))
    if not names:
        return None, 'ไม่มีไฟล์ .json ใน %s — ตัวหารเป็นศูนย์' % d
    out = []
    for f in names:
        p = os.path.join(d, f)
        try:
            with open(p, encoding='utf-8') as fh:
                data = json.load(fh)
        except Exception as e:                      # noqa: BLE001
            return None, 'อ่าน %s ไม่ได้: %s' % (p, e)
        qs = data.get('questions') if isinstance(data, dict) else data
        if not isinstance(qs, list):
            return None, '%s ไม่มีลิสต์ questions' % p
        out.append((f, qs))
    if not any(qs for _, qs in out):
        return None, 'ไฟล์ชุดมี แต่ไม่มีข้อเลย — ตัวหารเป็นศูนย์'
    return out, None


# นอกตัวหาร — พิมพ์ให้เห็น ⛔ ไม่มีผลต่อรหัสออก (ดูเหตุผลในหัวไฟล์)
OUTSIDE = [
    (os.path.join('data', 'manifest.json'), 'ข้อความบันทึกงานที่พูดถึงหมุด'),
    (os.path.join('data', 'bank.json'), 'ของที่ถูกสร้าง ไม่ใช่ของที่คนแก้'),
    (os.path.join('data', '_archive'), 'บท 16 ปลดจากหลักสูตรแล้ว'),
]


def count_outside(root):
    """นับหมุดเปล่านอกตัวหาร — เพื่อไม่ให้ "3 จุด" ถูกอ่านว่า "3 จุดทั้งคลัง" (⑨)"""
    rows = []
    for rel, why in OUTSIDE:
        p = os.path.join(root, rel)
        n, ok = 0, False
        try:
            if os.path.isdir(p):
                for f in sorted(os.listdir(p)):
                    if f.endswith('.json'):
                        with open(os.path.join(p, f), encoding='utf-8') as fh:
                            n += len(BARE.findall(fh.read()))
                ok = True
            elif os.path.isfile(p):
                with open(p, encoding='utf-8') as fh:
                    n = len(BARE.findall(fh.read()))
                ok = True
        except Exception:                            # noqa: BLE001
            ok = False
        rows.append((rel, why, n if ok else None))
    return rows


def head_sha(root):
    """SHA ปัจจุบัน — ใช้ "ผูกรายงานกับของจริง" เท่านั้น

    ⛔ ด่านนี้ **ไม่มีฐาน** — มันตรวจสภาพปัจจุบันของไฟล์ที่กำลังจะเข้าคลัง
       จึงอ่าน working tree โดยตั้งใจ และไม่มีการใช้คำว่า "ฐาน" ที่ไหนเลย
       (กฎ "พูดคำว่าฐานต้องพิมพ์ SHA และอ่านด้วย git show" ใช้กับด่านที่เทียบรุ่น)
    """
    try:
        sha = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=root,
                             capture_output=True, text=True, timeout=20)
        dirty = subprocess.run(['git', 'status', '--porcelain', '--', SETS_DIR],
                               cwd=root, capture_output=True, text=True, timeout=20)
        if sha.returncode != 0:
            return '(เรียก git ไม่ได้)'
        tag = sha.stdout.strip()
        if dirty.stdout.strip():
            tag += ' + %s ยังไม่ commit %d ไฟล์' % (
                SETS_DIR, len(dirty.stdout.strip().splitlines()))
        return tag
    except Exception:                                # noqa: BLE001
        return '(เรียก git ไม่ได้)'


def run(root, decoys=None, scan=None, verdict=None):
    """ตรวจคลังจริง — คืน (รหัสออก, บรรทัดรายงาน[])

    scan/verdict/decoys รับเข้ามาได้เพื่อให้ self-test ฉีด "ตัวจับที่พัง" เข้าไป
    แล้วพิสูจน์ว่าของล่อจับความพังนั้นได้จริง ⛔ ไม่ใช่เชื่อว่าจับได้
    """
    _scan = scan_questions if scan is None else scan
    _verdict = verdict_bare if verdict is None else verdict
    lines = []
    ok, bad = check_allowlist()
    if not ok:
        lines.append('🔴 รายการอนุญาตในตัวด่านเองผิดรูป ⇒ ตัดสินไม่ได้')
        lines += ['   ' + b for b in bad]
        return 2, lines

    sets, why = load_sets(root)
    if sets is None:
        lines.append('🟠 ตัดสินไม่ได้: %s' % why)
        lines.append('   ⛔ "ตรวจไม่ได้" ไม่เท่ากับ "ตรวจแล้วผ่าน"')
        return 2, lines

    # ของล่อถูกยิงก่อนอ่านผลจริง — เพื่อให้ทุกบรรทัดของกฎมีหลักฐานกำกับ
    dres = run_decoys(decoys, _scan, _verdict)
    dprobs = [p for r in DECOY_RULES for p in dres.get(r, (0, 0, []))[2]]

    div = {'q': 0, 'str': 0, 'char': 0, 'marked': 0, 'withfig': 0}
    found, per_q_bare = [], {}
    for name, qs in sets:
        d, f, b = _scan(qs, name)
        for k in div:
            div[k] += d[k]
        found += f
        per_q_bare.update(b)

    lines.append('check_image_markers v%s · ที่ %s' % (CHECKER_VERSION, head_sha(root)))
    lines.append('⑨ ตัวหาร (คลังที่บังคับ = %s): ไฟล์ชุด %d · ข้อ %d · ข้อที่มีรูป %d'
                 ' · ข้อที่มีหมุด %d · สตริง %d · อักษร %d'
                 % (SETS_DIR, len(sets), div['q'], div['withfig'], div['marked'],
                    div['str'], div['char']))
    for rel, why2, n in count_outside(root):
        lines.append('   นอกตัวหาร: %-22s %s จุด (%s) ⛔ ไม่มีผลต่อรหัสออก'
                     % (rel, '?' if n is None else n, why2))

    problems = _verdict(per_q_bare, ALLOW_BARE)
    kinds = {'oor': [], 'orphan': [], 'near': []}
    for kind, setname, qid, detail in found:
        kinds[kind].append('🔴 %s (%s): %s' % (qid, setname, detail))

    n_bare_pts = sum(len(h) for _, h in per_q_bare.values())
    lines.append('')
    lines.append('รายงานแยกกฎ — เลข "จับ" ทุกตัวมีของล่อกำกับ ⇒ 0 อ่านได้ว่าสะอาด'
                 ' ⛔ ไม่ใช่กฎตาย')
    lines.append('กฎ ก · หมุดเปล่า `[IMAGE]`      : จับ %d จุด ใน %d ข้อ · %s'
                 ' · รายการอนุญาต %d ข้อ'
                 % (n_bare_pts, len(per_q_bare), decoy_tag(dres, 'ก'),
                    len(ALLOW_BARE)))
    lines.append('กฎ ข · หมุดชี้เกินจำนวนรูป      : จับ %d ข้อ · %s'
                 % (len(kinds['oor']), decoy_tag(dres, 'ข')))
    lines.append('กฎ ค · มีหมุดแต่ไม่มีรูป        : จับ %d ข้อ · %s'
                 % (len(kinds['orphan']), decoy_tag(dres, 'ค')))
    lines.append('กฎ ง · ข้อความที่เกือบเป็นหมุด   : จับ %d จุด · %s'
                 % (len(kinds['near']), decoy_tag(dres, 'ง')))

    for qid, (setname, hits) in sorted(per_q_bare.items()):
        mark = '✅ อยู่ในรายการอนุญาต' if qid in ALLOW_BARE else '🔴 ไม่ได้รับอนุญาต'
        lines.append('   %s %-28s (%s) %d จุด · ชั้น %s'
                     % (mark, qid, setname, len(hits),
                        '/'.join(sorted({h[1] for h in hits}))))

    # เครื่องมือแดงมาก่อนเนื้อหาแดงเสมอ — ถ้ากฎตาย เลขเนื้อหาของกฎนั้นไม่มีความหมาย
    if dprobs:
        lines.append('')
        lines += dprobs
        lines.append('')
        lines.append('⇒ รหัส 2 · ของล่อของกฎข้างต้นไม่ทำงาน ⇒ **ตัดสินไม่ได้**')
        lines.append('   ⛔ ห้ามอ่านเลข "จับ" ของกฎที่ของล่อตก — 0 ของมันแปลไม่ได้')
        return 2, lines

    allbad = problems + kinds['oor'] + kinds['orphan'] + kinds['near']
    if allbad:
        lines.append('')
        lines += allbad
        lines.append('')
        lines.append('⇒ รหัส 1 · แก้ที่ %s แล้วรันใหม่' % SETS_DIR)
        return 1, lines
    lines.append('')
    lines.append('✅ หมุดทุกตัวชี้รูปที่มีจริง และหมุดเปล่าตรงกับรายการอนุญาตเป๊ะ')
    return 0, lines


# ─────────────────────────────────────────────────────────────
# self-test — ⛔ ด่านของตัวด่านเอง ห้ามพึ่งคลังจริง
#   (`_q` ย้ายขึ้นไปอยู่กับตาราง DECOYS แล้ว เพราะของล่อต้องใช้ตอน import)
# ─────────────────────────────────────────────────────────────
def _scan_dead(questions, setname='<mem>'):
    """ตัวจับที่ "กฎตาย" — ไม่เคยคืน finding เลย ⇒ ของล่อบวกต้องตก

    นี่คือความพังที่อันตรายที่สุดของด่านนี้: มันทำให้รายงาน "จับ 0 ทุกกฎ"
    ซึ่งหน้าตาเหมือนคลังสะอาดเป๊ะ
    """
    return ({'q': len(questions), 'str': 0, 'char': 0, 'marked': 0,
             'withfig': 0}, [], {})


def _scan_loud(questions, setname='<mem>'):
    """ตัวจับที่ "ยิงมั่ว" — คืนทุกชนิดเสมอ ⇒ ของล่อลบต้องตก"""
    qid = (questions[0].get('id') if questions else None) or 'x'
    found = [(k, setname, qid, 'มั่ว') for k in ('oor', 'orphan', 'near')]
    return ({'q': len(questions), 'str': 0, 'char': 0, 'marked': 0,
             'withfig': 0}, found,
            {qid: (setname, [('explanation', 'เด็กเห็น', '[IMAGE]')])})


def _write_repo(root, files):
    d = os.path.join(root, SETS_DIR)
    os.makedirs(d, exist_ok=True)
    for name, payload in files.items():
        with open(os.path.join(d, name), 'w', encoding='utf-8') as fh:
            if isinstance(payload, str):
                fh.write(payload)                      # JSON เสียโดยตั้งใจ
            else:
                json.dump(payload, fh, ensure_ascii=False)
    return root


def selftest():
    fails = []

    def eq(name, got, want):
        if got != want:
            fails.append('%s: ได้ %r ควรได้ %r' % (name, got, want))

    ALLOW3 = {
        'a-q1': ('explanation', 1, 'เหตุผลยาวพอสำหรับการทดสอบด่านของตัวด่านเอง'
                                   ' ที่ต้องยาวกว่าเกณฑ์ขั้นต่ำจริง ๆ'),
    }

    # ① ตรงกับรายการอนุญาตพอดี ⇒ ไม่มีปัญหา
    qs = [_q('a-q1', explanation=['x', '[IMAGE]'], imageSpec={'type': 't'})]
    _, found, bare = scan_questions(qs, 's')
    eq('① ไม่มี finding ชนิดอื่น', found, [])
    eq('① เทียบรายการอนุญาตแล้วสะอาด', verdict_bare(bare, ALLOW3), [])

    # ② ข้อใหม่มีหมุดเปล่า ⇒ ต้องมีปัญหา
    qs = [_q('a-q1', explanation=['[IMAGE]'], imageSpec={'type': 't'}),
          _q('a-q9', explanation=['[IMAGE]'], imageSpec={'type': 't'})]
    _, _, bare = scan_questions(qs, 's')
    p = verdict_bare(bare, ALLOW3)
    eq('② จับข้อใหม่ได้ 1 ปัญหา', len(p), 1)
    eq('② ปัญหาชี้ที่ a-q9', 'a-q9' in p[0], True)

    # ③ รายการอนุญาตค้าง (⑩) ⇒ ต้องแดง ⛔ ไม่ใช่ผ่านเงียบ
    qs = [_q('a-q1', explanation=['[IMAGE:0]'], imageSpec={'type': 't'})]
    _, _, bare = scan_questions(qs, 's')
    p = verdict_bare(bare, ALLOW3)
    eq('③ จับรายการค้างได้', len(p), 1)
    eq('③ ข้อความบอกให้ลบรายการ', 'รายการอนุญาตค้าง' in p[0], True)

    # ④ จำนวนจุดไม่ตรงที่ประกาศ
    qs = [_q('a-q1', explanation=['[IMAGE]', '[IMAGE]'], imageSpec={'type': 't'})]
    _, _, bare = scan_questions(qs, 's')
    p = verdict_bare(bare, ALLOW3)
    eq('④ จับจำนวนจุดไม่ตรง', len(p) == 1 and 'พบ 2 จุด' in p[0], True)

    # ⑤ หมุดเปล่าย้ายฟิลด์ (explanation -> notes)
    qs = [_q('a-q1', explanation=['x'], notes='[IMAGE]', imageSpec={'type': 't'})]
    _, _, bare = scan_questions(qs, 's')
    p = verdict_bare(bare, ALLOW3)
    eq('⑤ จับการย้ายฟิลด์', len(p) == 1 and "'notes'" in p[0], True)
    eq('⑤ รายงานชั้นฟิลด์ถูก', bare['a-q1'][1][0][1], 'บันทึกงาน')

    # ⑥ `[IMAGE:0]` ⛔ ไม่ใช่หมุดเปล่า
    qs = [_q('b-q1', explanation=['[IMAGE:0]'], imageSpec={'type': 't'})]
    _, found, bare = scan_questions(qs, 's')
    eq('⑥ ดัชนีชัดเจนไม่ถือเป็นหมุดเปล่า', bare, {})
    eq('⑥ และไม่เป็น finding อื่น', found, [])

    # ⑦ หมุดใน imageSpec ⛔ ไม่นับ
    qs = [_q('b-q2', explanation=['x'],
             imageSpec={'type': 't', 'label': 'ดู [IMAGE] ประกอบ'})]
    _, found, bare = scan_questions(qs, 's')
    eq('⑦ ไม่นับหมุดในสเปกรูป', (bare, found), ({}, []))

    # ⑧ หมุดชี้เกินจำนวนรูป
    qs = [_q('b-q3', explanation=['[IMAGE:0]', '[IMAGE:3]'],
             imageSpec=[{'type': 't'}, {'type': 't'}])]
    _, found, _ = scan_questions(qs, 's')
    eq('⑧ จับหมุดเกินดัชนี', [f[0] for f in found], ['oor'])

    # ⑨ มีหมุดแต่ไม่มีรูป
    qs = [_q('b-q4', explanation=['[IMAGE:1]'])]
    _, found, _ = scan_questions(qs, 's')
    eq('⑨ จับหมุดกำพร้า', [f[0] for f in found], ['orphan'])

    # ⑩ เกือบเป็นหมุด — ทั้งตัวพิมพ์เล็กและช่องว่าง
    for txt in ['[image]', '[IMAGE ]', '[ IMAGE:1 ]', '[Image:2]']:
        qs = [_q('b-q5', explanation=[txt], imageSpec={'type': 't'})]
        _, found, bare = scan_questions(qs, 's')
        eq('⑩ จับ %r' % txt, [f[0] for f in found], ['near'])
        eq('⑩ %r ไม่ถูกนับเป็นหมุดเปล่า' % txt, bare, {})

    # ⑩ข ข้อความปกติที่มีคำว่า image ⛔ ต้องไม่แดง
    qs = [_q('b-q6', explanation=['ดูรูป [IMAGE:1] และ [IMAGE:2] ประกอบ (image map)'],
             imageSpec=[{'a': 1}, {'b': 2}, {'c': 3}])]
    _, found, bare = scan_questions(qs, 's')
    eq('⑩ข ไม่มีแดงปลอม', (found, bare), ([], {}))

    # ⑪ ตัวหารเป็นศูนย์ ⇒ รหัส 2 (ทั้งไม่มีโฟลเดอร์ · ไม่มีไฟล์ · ไม่มีข้อ)
    with tempfile.TemporaryDirectory() as t:
        eq('⑪ ไม่มีโฟลเดอร์ ⇒ 2', run(t)[0], 2)
        os.makedirs(os.path.join(t, SETS_DIR))
        eq('⑪ ไม่มีไฟล์ .json ⇒ 2', run(t)[0], 2)
        _write_repo(t, {'a.json': {'questions': []}})
        eq('⑪ ไม่มีข้อเลย ⇒ 2', run(t)[0], 2)

    # ⑫ JSON เสีย ⇒ 2 ⛔ ไม่ใช่ 1
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': '{ ไม่ใช่ JSON'})
        code, out = run(t)
        eq('⑫ JSON เสีย ⇒ 2', code, 2)
        eq('⑫ พิมพ์ว่าตัดสินไม่ได้', any('ตัดสินไม่ได้' in x for x in out), True)

    # ⑬ รายการอนุญาตผิดรูป ⇒ 2
    ok, bad = check_allowlist({'x': ('explanation', 1, 'สั้น')})
    eq('⑬ เหตุผลสั้น ⇒ ไม่ผ่าน', (ok, len(bad)), (False, 1))
    ok, _ = check_allowlist({'x': ('explanation', 0, 'เหตุผลยาวพอสมควรสำหรับการทดสอบ'
                                                    ' ที่ยาวเกินสี่สิบตัวอักษรแน่นอน')})
    eq('⑬ จำนวน 0 ⇒ ไม่ผ่าน', ok, False)
    ok, _ = check_allowlist(ALLOW_BARE)
    eq('⑬ รายการจริงในไฟล์นี้ต้องผ่าน', ok, True)

    # ⑭ ตัวหารต้องถูกพิมพ์จริง ⛔ ไม่ใช่รายงานที่ซ่อนว่าตรวจอะไรไปกี่ชิ้น
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [
            _q('z-q1', explanation=['[IMAGE:0]'], imageSpec={'t': 1})]}})
        code, out = run(t)
        txt = '\n'.join(out)
        eq('⑭ ข้อมูลสะอาด + รายการอนุญาตค้าง 3 ข้อ ⇒ 1', code, 1)
        eq('⑭ พิมพ์ตัวหาร', '⑨ ตัวหาร' in txt and 'ข้อ 1' in txt, True)
        eq('⑭ พิมพ์ทั้งสี่กฎ',
           all(k in txt for k in ['กฎ ก', 'กฎ ข', 'กฎ ค', 'กฎ ง']), True)

    # ⑮ e2e — รันเป็นโปรเซสจริง อ่านรหัสที่ "เชลล์เห็น" (กับดัก ⑦ก)
    #    ⛔ ไม่ใช่เรียก run() ในโปรเซสเดียวกัน: return 1 ที่ไม่ได้ต่อกับ sys.exit
    #      จะทำให้เชลล์เห็น 0 และไม่มีเทสต์ในโปรเซสเดียวกันตัวไหนจับได้เลย
    here = os.path.abspath(__file__)
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [
            _q('z-q1', explanation=['[IMAGE:1]'])]}})     # หมุดกำพร้า ⇒ 1
        r = subprocess.run([sys.executable, here, '--root', t],
                           capture_output=True, text=True)
        eq('⑮ e2e เนื้อหาแดง ⇒ เชลล์เห็น 1', r.returncode, 1)
    with tempfile.TemporaryDirectory() as t:
        r = subprocess.run([sys.executable, here, '--root', t],
                           capture_output=True, text=True)
        eq('⑮ e2e ตัดสินไม่ได้ ⇒ เชลล์เห็น 2', r.returncode, 2)

    # ⑯ ของล่อชุดจริงในไฟล์นี้ต้องผ่านครบทุกกฎ และต้องมีสองขั้วครบทุกกฎ
    res = run_decoys()
    for r in DECOY_RULES:
        npass, total, probs = res[r]
        eq('⑯ กฎ %s ของล่อผ่านครบ' % r, (npass, total > 0, probs), (total, True, []))
        wants = {w for _, w, _, _ in DECOYS[r]}
        eq('⑯ กฎ %s มีของล่อทั้งบวกและลบ' % r, wants, {'ยิง', 'เงียบ'})
        eq('⑯ กฎ %s ป้ายเป็น ✅' % r, decoy_tag(res, r).endswith('✅'), True)

    # ⑰ รายงานของ "การรันจริง" ต้องพิมพ์ของล่อแยกกฎ ⛔ ไม่ใช่มีแต่ใน --selftest
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [
            _q('z-q1', explanation=['[IMAGE:0]'], imageSpec={'t': 1})]}})
        txt = '\n'.join(run(t)[1])
        for r in DECOY_RULES:
            eq('⑰ บรรทัดกฎ %s มีทั้ง "จับ" และ "ของล่อ …/… ✅"' % r,
               any(x.startswith('กฎ %s ' % r) and 'จับ' in x
                   and ('ของล่อ %d/%d ✅' % (res[r][1], res[r][1])) in x
                   for x in run(t)[1]), True)
        eq('⑰ ⛔ ไม่มีการพิมพ์รวมแบบไม่มีของล่อกำกับ', 'ของล่อ 0/0' in txt, False)

    # ⑱ ตัวจับตาย (จับ 0 ทุกกฎ) ⇒ ต้องเป็นรหัส 2 ⛔ ไม่ใช่ 0 ที่ดูเหมือนคลังสะอาด
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [_q('z-q1')]}})
        code, out = run(t, scan=_scan_dead)
        txt = '\n'.join(out)
        eq('⑱ กฎตาย ⇒ 2', code, 2)
        eq('⑱ รายงานบอกว่ากฎตาย', 'กฎตาย' in txt, True)
        eq('⑱ กฎที่ของล่อตกต้องไม่ติดป้าย ✅',
           any(x.startswith('กฎ ก ') and '⛔' in x for x in out), True)

    # ⑲ ตัวจับยิงมั่ว ⇒ ต้องเป็นรหัส 2 เช่นกัน (เลขที่จับได้เชื่อไม่ได้)
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [_q('z-q1')]}})
        code, out = run(t, scan=_scan_loud)
        eq('⑲ ยิงมั่ว ⇒ 2', code, 2)
        eq('⑲ รายงานบอกว่ายิงมั่ว',
           any('กฎยิงมั่ว' in x for x in out), True)

    # ⑳ กฎที่ไม่มีของล่อ ⇒ 2 และ ⛔ ห้ามพิมพ์ `0/0 ✅`
    empty = {r: [] for r in DECOY_RULES}
    eq('⑳ ป้ายของ 0/0 ต้องเป็น ⛔', decoy_tag(run_decoys(empty), 'ก'),
       'ของล่อ 0/0 ⛔')
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [_q('z-q1')]}})
        code, out = run(t, decoys=empty)
        eq('⑳ ไม่มีของล่อ ⇒ 2', code, 2)
        eq('⑳ รายงานบอกว่าอ่านเลขไม่ได้',
           any('อ่านไม่ได้' in x for x in out), True)

    # ㉑ ถอดของล่อออกเงียบ ๆ ⇒ ต้องเป็นรหัส 2
    #    (⑩ ขาลง — `ของล่อ 2/2 ✅` ที่เคยเป็น 3/3 อ่านเหมือนเดิมทุกตัวอักษร)
    for r in DECOY_RULES:
        eq('㉑ หมุด DECOY_MIN กฎ %s ไม่เกินของล่อจริง' % r,
           DECOY_MIN[r] <= len(DECOYS[r]), True)
        eq('㉑ หมุด DECOY_MIN กฎ %s ไม่ต่ำกว่า 3' % r, DECOY_MIN[r] >= 3, True)
    thin = {r: list(DECOYS[r]) for r in DECOY_RULES}
    thin['ข'] = thin['ข'][:-1]                    # ถอดออก 1 ตัว (3 → 2)
    res_thin = run_decoys(thin)
    eq('㉑ กฎที่โดนถอดต้องติด ⛔', decoy_tag(res_thin, 'ข'), 'ของล่อ 2/2 ⛔')
    eq('㉑ กฎอื่นไม่โดนหางเลข', decoy_tag(res_thin, 'ค').endswith('✅'), True)
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [_q('z-q1')]}})
        code, out = run(t, decoys=thin)
        eq('㉑ ถอดของล่อ ⇒ 2', code, 2)
        eq('㉑ รายงานบอกว่าถูกถอดออกเงียบ ๆ',
           any('ถอดออกเงียบ ๆ' in x for x in out), True)

    # ㉑ข ของล่อขั้วเดียว ⇒ ต้องเป็นรหัส 2 เช่นกัน
    onepol = {r: [c for c in DECOYS[r] if c[1] == 'ยิง'] + [
        c for c in DECOYS[r] if c[1] == 'ยิง'][:1] for r in DECOY_RULES}
    onepol = {r: (v * 2)[:max(DECOY_MIN[r], len(v))] for r, v in onepol.items()}
    res_one = run_decoys(onepol)
    eq('㉑ข ขั้วเดียวต้องติด ⛔', decoy_tag(res_one, 'ข').endswith('⛔'), True)
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [_q('z-q1')]}})
        code, out = run(t, decoys=onepol)
        eq('㉑ข ขั้วเดียว ⇒ 2', code, 2)
        eq('㉑ข รายงานบอกว่าขั้วเดียว',
           any('ขั้วเดียว' in x for x in out), True)

    print('self-test ของ check_image_markers v%s — %d เคส'
          % (CHECKER_VERSION, 21))
    if fails:
        print('🔴 ตก %d ข้อ:' % len(fails))
        for f in fails:
            print('   ' + f)
        return 2                    # ตัวด่านเองพัง = เครื่องมือแดง ⛔ ไม่ใช่เนื้อหาแดง
    print('✅ ผ่านทุกเคส')
    return 0


def main():
    ap = argparse.ArgumentParser(
        description='ตรวจว่าหมุดรูป [IMAGE:n] ใน data/sets ชี้รูปที่มีจริง')
    ap.add_argument('--root', default='.', help='รากของคลัง (ค่าเริ่มต้น .)')
    ap.add_argument('--selftest', action='store_true', help='ตรวจตัวด่านเอง')
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    code, lines = run(a.root)
    for x in lines:
        print(x)
    return code


if __name__ == '__main__':
    sys.exit(main())

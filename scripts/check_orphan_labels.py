#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ด่าน 16 · ตัวเลขที่เขียนอยู่บนรูป ต้องมีที่มาในข้อเดียวกัน

──────────────────────────────────────────────────────────────────────────────
ที่มา (กับดัก ⑳ · 3 ส.ค. 2569)

  ระหว่างไล่อ่านรูปของ C1 เจอรูปของ `pat1-2560-03-q35` เขียนค่ากลางของเส้นโค้ง
  ปกติไว้ว่า **22.5** ทั้งที่ค่าเฉลี่ยของข้อนั้นคือ **62** (เฉลยคำนวณได้ 62 เอง
  ในบรรทัดที่ 29 และ 36) ⇒ ตัวเลข 22.5 **ไม่มีที่มาจากข้อนี้เลยแม้แต่ที่เดียว**

  บทเรียนที่ถอดออกมาเป็นกฎ:
     🔴 ตัวเลขในรูปที่ไม่โผล่ในตัวหนังสือของข้อเดียวกัน
        = รูปนั้นอาจไม่ใช่ของข้อนี้ (ลอกมาจากข้ออื่นแล้วลืมแก้)

  ⛔ นี่ ⛔ ไม่ใช่ ด่านที่บอกว่า "รูปวาดถูกไหม" — ด่านนี้ตัดสินได้แค่เรื่องเดียว:
     ป้ายตัวเลขนั้น **มีที่มา** ในข้อเดียวกันหรือไม่

──────────────────────────────────────────────────────────────────────────────
㉑ ตัวเลขที่ต้องประกาศ (ด่านที่เขียนจากเคสเดียว มักไม่จับเคสนั้น)

  · **ตัวหาร** : ข้อที่มี `imageSpec` ใน `data/sets/*.json` = **2,150 ข้อ**
                 (วัดที่ 1876dfb + 3 ไฟล์ของซองหมุดรูป 3 จุด)
  · **แดงวันแรก** : **0** — ไม่ใช่เพราะไม่มีของ แต่เพราะของที่มี **2 ข้อ**
                 ถูกปักไว้ในรายการ PINNED ข้างล่างพร้อมเหตุผลทั้งคู่
  · **ผลกับเคสต้นเรื่อง** : `pat1-2560-03-q35` **ยังติดธง** และถูกปักไว้
                 ⇒ ด่านนี้จับเคสที่ทำให้มันเกิดได้จริง ⛔ ไม่ใช่ด่านที่เขียนแล้วเงียบ

──────────────────────────────────────────────────────────────────────────────
🔴 ขอบเขตที่ด่านนี้ ⛔ ตัดสินไม่ได้ (ประกาศไว้ ไม่ให้เขียวถูกอ่านเกินจริง)

  ด่านนี้ **นับน้อยกว่าความจริงโดยตั้งใจ** สองชั้น — วัดผลของทั้งสองชั้นไว้แล้ว:

  ① เพดาน |ค่า| > 10 (`CUTOFF`)
     เลขแกน/ขีดสเกล (`0 1 2 5 10`) ไม่มีทางโผล่ในโจทย์ ⇒ ถ้าไม่ตัด จะแดงปลอมถาวร
     **วัดแล้ว:** ถ้าถอดเพดานออก ธงขึ้นเป็น **11 ข้อ** ซึ่ง **9 ข้อเป็นแดงปลอม**
     (`0.71 · 0.1 · ±1.73 · 0.6826 · -6 · 10 · -1 · 6 · 1.5` — เลขแกนล้วน)
     ⇒ เพดานนี้แลก "จับได้น้อยลง" กับ "เลขที่จับได้ทุกตัวมีความหมาย"

  ② เทียบแบบ "สตริงย่อย" (`'62' in ข้อความทั้งก้อน`)
     ⇒ ป้าย `22` จะเงียบทันทีถ้าในข้อมีคำว่า `220` หรือ `0.22` อยู่ที่ไหนก็ได้
     ตัวอย่างจริงที่โดน: `samn-2565-03-q30` มีป้าย 8 ตัว ติดธงแค่ 3
     ⇒ **เขียวของด่านนี้ไม่ใช่หลักฐานว่าไม่มีป้ายกำพร้า** เป็นแค่หลักฐานว่า
       ไม่มีป้ายกำพร้า **ชนิดที่ตรงไปตรงมาที่สุด** ที่ไม่ได้ถูกปักไว้

  ③ อ่านเฉพาะคีย์ `text` / `label` / `caption` ใน `imageSpec`
     ตัวเลขที่เป็น **พิกัด** (`x`, `y`, `value`, `zPosition`) ⛔ ไม่นับเป็นป้าย
     เพราะมันคือ "ตำแหน่ง" ไม่ใช่ "ข้อความที่เด็กอ่าน"

  ④ "รูปนี้เป็นของข้อนี้จริงไหม" — ตัดสินไม่ได้จากข้อมูล ต้องมีคนอ่าน
     ด่านนี้ยกธงให้คนไปอ่าน ⛔ ไม่ได้ตัดสินแทน

──────────────────────────────────────────────────────────────────────────────
⑦ข ระวัง "เขียวเพราะไม่มีของให้จับ"

  ด่านนี้เกิดมาพร้อมสถานะ "จับได้ 2 · ปักไว้ 2 · แดง 0" ⇒ รายงานของมันเป็นศูนย์
  ตั้งแต่วันแรก ⇒ **ของล่อประจำกฎคือสิ่งเดียวที่ทำให้ศูนย์นั้นอ่านได้**
  ของล่อถูกยิงทุกครั้งที่รันจริง ⛔ ไม่ใช่เฉพาะใน `--selftest`
    รายงานพิมพ์แยกกฎ:  `กฎ ก · … : จับ 2 ข้อ · ของล่อ 4/4 ✅`
  ⛔ ห้ามให้ `ของล่อ 0/0` พิมพ์ ✅ — กฎที่ไม่มีของล่อ = รหัส 2

⑩ รายการ PINNED ถูกบังคับ **สองทาง**
  · มีธงที่ไม่ได้ปัก      ⇒ แดง (ของใหม่โผล่)
  · ปักไว้แต่ไม่มีธงแล้ว ⇒ แดง (แก้ข้อมูลแล้วต้องลบบรรทัดที่ปักในคอมมิตเดียวกัน)
  · ปักไว้แต่ชุดป้ายเปลี่ยน ⇒ แดง (แก้ครึ่งเดียวแล้วรายการเดิมยังอ่านเหมือนเดิม)

การใช้:
    python scripts/check_orphan_labels.py            # ตรวจคลังจริง (รากคือ .)
    python scripts/check_orphan_labels.py --root .   # ระบุรากเอง
    python scripts/check_orphan_labels.py --selftest # ด่านของตัวด่านเอง

รหัสออก: 0 = ผ่าน · 1 = เนื้อหาแดง · 2 = ตัวเครื่องมือแดง / ตัดสินไม่ได้
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile

CHECKER_VERSION = '1.0'

SETS_DIR = os.path.join('data', 'sets')

# ── อะไรนับเป็น "ป้าย" ────────────────────────────────────────────────────────
# ⛔ ห้ามเติม 'value' / 'x' / 'y' / 'z' ลงไป — พวกนั้นคือพิกัด ไม่ใช่ข้อความ
#    (ถ้าเติม ด่านจะแดงปลอมทุกข้อที่มีจุดพิกัดเกิน 10)
LABEL_KEYS = ('text', 'label', 'caption')

# ตัวเลขล้วน — รับจุดทศนิยมและลูกน้ำหลักพัน ⛔ ไม่รับ LaTeX หรือหน่วย
#
# ⚠️ เขียนผิดมาก่อนแล้วครั้งหนึ่ง — บันทึกไว้ให้คนถัดไป:
#    รุ่นแรกเขียน `^-?\d{1,3}(?:,\d{3})*(?:\.\d+)?$` ซึ่งอ่านเผิน ๆ เหมือนถูก
#    แต่ `\d{1,3}` + `(?:,\d{3})*` แปลว่า **เลข 4 หลักที่ไม่มีลูกน้ำ ไม่ match**
#    ⇒ ป้าย `4321` / `9999` เงียบสนิท ⇒ ของล่อของกฎ ก ตายไป 1 ตัวโดยไม่มีใครรู้
#    (ของล่อจับได้ตอน --selftest ครั้งแรก — นี่คือเหตุผลที่ต้องมีของล่อ)
#    ⇒ ต้องแยกสองทางชัด ๆ: "มีลูกน้ำแบบหลักพัน" หรือ "ไม่มีลูกน้ำเลย"
NUM = re.compile(r'^-?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?$')

# เพดาน: ป้ายที่ |ค่า| <= CUTOFF ไม่ตัดสิน (ดูเหตุผลข้อ ① ในหัวไฟล์)
CUTOFF = 10

# ── เนื้อข้อที่ใช้เป็น "ที่มา" ────────────────────────────────────────────────
# กับดัก ⑪ — ฟิลด์ที่เด็กเห็น ต่างจากฟิลด์บันทึกงาน
# ⛔ `notes` / `patchLog` / `review` ⛔ ไม่นับเป็นที่มา ตั้งใจ:
#    บันทึกงานที่เผอิญพิมพ์เลขนั้นไว้ ("แก้ป้าย 22.5") จะทำให้ด่านเงียบทันที
#    ⇒ ที่มาของตัวเลขต้องเป็นของที่ **เด็กอ่านได้** เท่านั้น
BODY_FIELDS = ('question', 'explanation', 'choices', 'correct', 'answer',
               'accept', 'hint', 'tables')

MIN_REASON = 40


# ─────────────────────────────────────────────────────────────
# รายการที่ปักไว้ — ธงที่รู้แล้ว มีคนอ่านแล้ว และตัดสินแล้วว่าจะทำอย่างไร
#
# ⛔ นี่ ⛔ ไม่ใช่ "รายการยกเว้น" — มันคือ **รายการที่ต้องตรงเป๊ะ**
#    ธงที่ไม่อยู่ในนี้ = แดง · บรรทัดในนี้ที่ไม่มีธงแล้ว = แดงเช่นกัน (⑩ สองทาง)
#
# รูปแบบ: id -> (ชุดป้ายที่ต้องเจอ (tuple เรียงแล้ว), เหตุผล)
# ⛔ ห้ามเติมบรรทัดที่นี่เพื่อให้ด่านเงียบ — เติมได้เมื่อ "อ่านแล้วและตัดสินแล้ว"
#    และรายการนี้ถูก ด่าน 10 (check_config_growth) เฝ้าขาขึ้นอยู่
# ─────────────────────────────────────────────────────────────
PINNED = {
    'pat1-2560-03-q35': (
        ('22.5',),
        'เคสต้นเรื่องของกับดัก ⑳ — ป้ายค่ากลางของเส้นโค้งปกติเขียนว่า 22.5 '
        'แต่ค่าเฉลี่ยของข้อนี้คือ 62 (เฉลยคำนวณเองในบรรทัด 29 และ 36) '
        '⇒ เป็นป้ายที่ลอกมาจากข้ออื่น ใบแก้เขียนไว้แล้ว (22.5 → 62 · 2 จุด) '
        'แต่ ⛔ ยังไม่มีลายเซ็นครูสำหรับการแตะชุดข้อสอบจริง PAT1 '
        '⇒ ค้างไว้โดยรู้ตัว ไม่ใช่โดยลืม · ลบบรรทัดนี้ในคอมมิตเดียวกับที่แก้ข้อมูล'
    ),
    'samn-2565-03-q30': (
        ('16', '28', '40'),
        'อ่านแล้ว — ไม่ใช่ของเสีย: เป็นแผนภูมิแท่งส่วนประกอบ 100% ที่ตัวเลข '
        'ร้อยละบนแท่ง **คือข้อมูลที่โจทย์ตั้งใจให้อ่านจากรูป** '
        '(โจทย์เขียนเองว่า "เขียนแผนภูมิ ... ดังรูป") ⇒ ป้ายที่ไม่โผล่ในตัวหนังสือ '
        'คือลักษณะปกติของข้อชนิดนี้ ⛔ ไม่ใช่ความผิดพลาด '
        '· หมายเหตุ: ป้ายอีก 5 ตัว (22·36·14·34·10) เงียบเพราะเทียบแบบสตริงย่อย '
        'ไปชนเลขอื่นในเฉลย — เป็นตัวอย่างของข้อจำกัด ② ที่ประกาศไว้ในหัวไฟล์'
    ),
}


def check_pins(table=None):
    """รายการที่ปักไว้ต้องอ่านได้จริง — คืน (ผ่านไหม, ปัญหา[])

    ⛔ รายการผิดรูป = ด่านที่ตัดสินด้วยของที่อ่านไม่ออก ⇒ รหัส 2 ไม่ใช่ 1
    """
    t = PINNED if table is None else table
    bad = []
    if not isinstance(t, dict):
        return False, ['PINNED ต้องเป็น dict {id: (ชุดป้าย, เหตุผล)}']
    for k, v in t.items():
        if not (isinstance(v, tuple) and len(v) == 2):
            bad.append('%s: ต้องเป็น (ชุดป้าย, เหตุผล) 2 ช่อง' % k)
            continue
        labs, why = v
        if not (isinstance(labs, tuple) and labs
                and all(isinstance(x, str) and x for x in labs)):
            bad.append('%s: ชุดป้ายต้องเป็น tuple ของสตริงที่ไม่ว่าง' % k)
        elif list(labs) != sorted(labs):
            bad.append('%s: ชุดป้ายต้องเรียงแล้ว — ลำดับที่ไม่คงที่'
                       ' ทำให้ diff ของรายการนี้อ่านไม่ได้' % k)
        if not isinstance(why, str) or len(why.strip()) < MIN_REASON:
            bad.append('%s: เหตุผลสั้นกว่า %d ตัวอักษร — บรรทัดที่ปักไว้'
                       'โดยไม่มีเหตุผล คือการปิดด่านที่หน้าตาเหมือนการประกาศ'
                       % (k, MIN_REASON))
    return not bad, bad


# ─────────────────────────────────────────────────────────────
# ส่วนวัด — ฟังก์ชันบริสุทธิ์ ทดสอบได้โดยไม่ต้องมีคลัง
# ─────────────────────────────────────────────────────────────
def walk_labels(value, out, key=None):
    """เก็บสตริงทุกตัวที่อยู่ใต้คีย์ใน LABEL_KEYS

    ⛔ ต้องลงทั้ง dict และ list — กับดัก ④ (walker ที่ไม่ลง dict) เคยกัดมาแล้ว
    ⛔ และต้องลงต่อ **แม้เจอคีย์ที่ตรงแล้ว** ถ้าค่าไม่ใช่สตริง
       (`labels: [{text: ...}]` — คีย์ `labels` ไม่ตรง แต่ข้างในมี `text`)
    """
    if isinstance(value, str):
        if key in LABEL_KEYS:
            out.append(value)
    elif isinstance(value, dict):
        for k, v in value.items():
            walk_labels(v, out, k)
    elif isinstance(value, list):
        for v in value:
            walk_labels(v, out, key)
    return out


def body_text(q):
    """ข้อความของข้อนี้ที่ใช้เป็น "ที่มา" — ⛔ ไม่รวม imageSpec และฟิลด์บันทึกงาน"""
    return json.dumps([q.get(k) for k in BODY_FIELDS], ensure_ascii=False)


def orphan_labels(q):
    """คืน (มี imageSpec ไหม, ชุดป้ายกำพร้าที่เรียงแล้ว)"""
    spec = q.get('imageSpec')
    if not spec:
        return False, ()
    labs = walk_labels(spec, [])
    body = body_text(q)
    body_nc = body.replace(',', '')
    miss = set()
    for raw in labs:
        t = raw.strip()
        if not NUM.match(t):
            continue
        if abs(float(t.replace(',', ''))) <= CUTOFF:
            continue
        if t in body:
            continue
        if t.replace(',', '') in body_nc:
            continue
        miss.add(t)
    return True, tuple(sorted(miss))


def scan_questions(questions, setname='<mem>'):
    """วัดทั้งชุด — คืน (สรุปตัวหาร, per_q {qid: (setname, ชุดป้าย)})"""
    div = {'q': 0, 'withfig': 0, 'lab': 0, 'num': 0}
    per_q = {}
    for q in questions:
        div['q'] += 1
        spec = q.get('imageSpec')
        if spec:
            labs = walk_labels(spec, [])
            div['lab'] += len(labs)
            div['num'] += sum(1 for x in labs if NUM.match(x.strip()))
        hasfig, miss = orphan_labels(q)
        if hasfig:
            div['withfig'] += 1
        if miss:
            per_q[q.get('id') or '<ไม่มี id>'] = (setname, miss)
    return div, per_q


def verdict_labels(per_q, pinned):
    """เทียบธงที่พบ กับรายการที่ปักไว้ — สองทางเสมอ (กับดัก ⑩)

    คืน problems[] (ว่าง = ตรงกันเป๊ะ)
    """
    problems = []
    for qid, (setname, labs) in sorted(per_q.items()):
        if qid not in pinned:
            problems.append(
                '🔴 ป้ายเลขที่ไม่มีที่มาในข้อ และไม่ได้ถูกปักไว้: %s (%s) — %s'
                ' ⇒ ไปอ่านรูปข้อนี้ก่อนว่ารูปเป็นของข้อนี้จริงไหม'
                % (qid, setname, ' · '.join(labs)))
            continue
        want, _ = pinned[qid]
        if tuple(labs) != tuple(want):
            problems.append(
                '🔴 %s: รายการปักไว้ประกาศป้าย %s แต่พบ %s'
                ' ⇒ ของเปลี่ยนไปแล้วแต่บรรทัดที่ปักยังอ่านเหมือนเดิม'
                % (qid, ' · '.join(want), ' · '.join(labs)))
    for qid in sorted(pinned):
        if qid not in per_q:
            problems.append(
                '🔴 รายการปักค้าง: %s ไม่มีป้ายกำพร้าแล้ว'
                ' ⇒ ต้องลบบรรทัดนี้ออกจาก PINNED ในคอมมิตเดียวกับที่แก้ข้อมูล'
                ' ("พิสูจน์ว่าไม่เพิ่ม" ≠ "พิสูจน์ว่าไม่ลด")' % qid)
    return problems


# ─────────────────────────────────────────────────────────────
# ของล่อประจำกฎ — ⛔ ไม่ใช่ self-test มันถูกยิงทุกครั้งที่รันจริง
#
# 🔴 เหตุผลที่ต้องอยู่ในเส้นทางการรันจริง:
#    รายงานของการรันจริงคือสิ่งที่คนอ่านแล้วตัดสินว่า "ผ่าน"
#    ถ้าหลักฐานว่ากฎยังยิงเป็น อยู่คนละคำสั่งกับรายงาน ⇒ คนอ่านไม่มีหลักฐานนั้น
#
# รูปแบบ: รหัสกฎ -> [(ชื่อ, 'ยิง'|'เงียบ', ข้อ[], รายการที่ปักไว้ (เฉพาะกฎ ข))]
# ⛔ ของล่อทุกตัวเป็นของในหน่วยความจำล้วน — ห้ามแตะคลังจริงหรือรายการ PINNED จริง
# ─────────────────────────────────────────────────────────────
def _q(qid, **kw):
    q = {'id': qid, 'question': 'โจทย์', 'explanation': ['ขั้นที่ 1']}
    q.update(kw)
    return q


DECOY_RULES = ('ก', 'ข')

# 🔴 หมุดปักจำนวนของล่อขั้นต่ำ (กับดัก ⑩ อีกครั้ง)
#    `ของล่อ 3/3 ✅` ที่เคยเป็น 4/4 อ่านเหมือนเดิมทุกตัวอักษร
#    ⇒ หมุดต้องเท่ากับจำนวนจริง ⛔ ไม่ใช่ "ต่ำกว่าไว้ก่อนกันเหนียว"
#      หมุดที่ตั้งต่ำกว่าของจริง = ช่องให้ถอดของล่อออกได้ฟรีตามส่วนต่าง
DECOY_MIN = {'ก': 7, 'ข': 5}

_PIN_STALE = {
    'ล่อ-ค้าง': (('99',),
                 'รายการปักของล่อ — ใช้พิสูจน์ขาลงของกฎ ข (⑩) ว่ายังบังคับอยู่จริง'),
}
_PIN_OK = {
    'ล่อ-ข3': (('4321',),
               'รายการปักของล่อ — ใช้พิสูจน์ว่าธงที่ตรงกับที่ปักไว้ต้องเงียบสนิท'),
}
_PIN_WRONG = {
    'ล่อ-ข4': (('1234',),
               'รายการปักของล่อ — ใช้พิสูจน์ว่าชุดป้ายที่เปลี่ยนไปต้องแดง'),
}

DECOYS = {
    # กฎ ก — ตัวจับ: ป้ายเลขที่ไม่มีที่มาในเนื้อข้อ
    'ก': [
        ('ป้าย 22.5 ที่ไม่โผล่ในเนื้อข้อ ⇒ ต้องแดง', 'ยิง',
         [_q('ล่อ-ก1', imageSpec={'labels': [{'text': '22.5'}]})], None),
        ('ป้ายอยู่ลึกใต้ list ซ้อน dict ⇒ ต้องยังจับได้ (กับดัก ④)', 'ยิง',
         [_q('ล่อ-ก2', imageSpec={'curves': [{'labels': [{'text': '9999'}]}]})],
         None),
        ('ป้าย 22.5 ที่โจทย์พูดถึงจริง ⇒ ต้องเงียบ', 'เงียบ',
         [_q('ล่อ-ก3', question='ค่าเฉลี่ยคือ $22.5$',
             imageSpec={'labels': [{'text': '22.5'}]})], None),
        ('ป้ายเลขแกนเล็ก ๆ (|ค่า| <= 10) ⇒ ต้องเงียบตามเพดานที่ประกาศไว้', 'เงียบ',
         [_q('ล่อ-ก4', imageSpec={'labels': [{'text': '5'}]})], None),
        ('ป้ายที่ไม่ใช่ตัวเลข ⇒ ต้องเงียบ', 'เงียบ',
         [_q('ล่อ-ก5', imageSpec={'labels': [{'text': 'ทรงขากระบอก'}]})], None),
        ('พิกัดตัวเลขใหญ่ในคีย์ที่ไม่ใช่ป้าย ⇒ ต้องเงียบ', 'เงียบ',
         [_q('ล่อ-ก6', imageSpec={'points': [{'x': 5000, 'y': 8000}]})], None),
        ('ป้ายมีลูกน้ำหลักพัน แต่เนื้อข้อเขียนไม่มีลูกน้ำ ⇒ ต้องเงียบ', 'เงียบ',
         [_q('ล่อ-ก7', question='ทั้งหมด $1200$ ตัว',
             imageSpec={'labels': [{'text': '1,200'}]})], None),
    ],
    # กฎ ข — ตัวตัดสิน: รายการที่ปักไว้ต้องตรงเป๊ะ สองทาง
    'ข': [
        ('มีธงแต่ไม่มีบรรทัดที่ปักไว้ ⇒ ต้องแดง', 'ยิง',
         [_q('ล่อ-ข1', imageSpec={'labels': [{'text': '4321'}]})], None),
        ('ปักไว้แต่ไม่มีธงแล้ว ⇒ ต้องแดง (⑩ ขาลง)', 'ยิง',
         [_q('ล่อ-ข2', imageSpec={'labels': [{'text': '7'}]})], _PIN_STALE),
        ('ปักไว้แต่ชุดป้ายเปลี่ยนไป ⇒ ต้องแดง', 'ยิง',
         [_q('ล่อ-ข4', imageSpec={'labels': [{'text': '4321'}]})], _PIN_WRONG),
        ('ธงตรงกับที่ปักไว้เป๊ะ ⇒ ต้องเงียบ', 'เงียบ',
         [_q('ล่อ-ข3', imageSpec={'labels': [{'text': '4321'}]})], _PIN_OK),
        ('ไม่มีธงและไม่มีบรรทัดที่ปักไว้ ⇒ ต้องเงียบ', 'เงียบ',
         [_q('ล่อ-ข5', imageSpec={'labels': [{'text': '7'}]})], None),
    ],
}


def run_decoys(decoys=None, scan=None, verdict=None):
    """ยิงของล่อของทุกกฎ — คืน {รหัสกฎ: (ผ่าน, ทั้งหมด, ปัญหา[])}

    ⛔ กฎที่ไม่มีของล่อ = ปัญหา ไม่ใช่ 0/0 ✅
    """
    table = DECOYS if decoys is None else decoys
    scan = scan_questions if scan is None else scan
    verdict = verdict_labels if verdict is None else verdict
    out = {}
    for rule in DECOY_RULES:
        cases = list(table.get(rule) or [])
        probs, npass = [], 0
        if not cases:
            probs.append('🔴 กฎ %s ไม่มีของล่อเลย ⇒ เลข "จับ N" ของกฎนี้อ่านไม่ได้'
                         ' ว่าเป็นความสะอาดหรือความตายของกฎ' % rule)
        else:
            # ⑩ ขาลง: "ของล่อผ่านหมด" พิสูจน์แค่ของล่อ **ที่ยังเหลืออยู่**
            floor = DECOY_MIN.get(rule, 1)
            if len(cases) < floor:
                probs.append('🔴 กฎ %s มีของล่อ %d ตัว แต่หมุด DECOY_MIN ปักไว้ %d'
                             ' ⇒ **ของล่อถูกถอดออกเงียบ ๆ (⑩)**'
                             ' ⇒ เลข "จับ" ของกฎนี้อ่านไม่ได้'
                             % (rule, len(cases), floor))
            wants = {w for _, w, _, _ in cases}
            if wants != {'ยิง', 'เงียบ'}:
                probs.append('🔴 กฎ %s ของล่อมีขั้วเดียว (%s) ⇒ จับได้แค่ด้านเดียว'
                             ' ⇒ เลข "จับ" ของกฎนี้อ่านไม่ได้'
                             % (rule, '/'.join(sorted(wants)) or 'ไม่มี'))
        for name, want, qs, pin in cases:
            try:
                _, per_q = scan(qs, '<ของล่อ>')
                if rule == 'ก':
                    fired = bool(per_q)
                else:
                    fired = bool(verdict(per_q, pin or {}))
            except Exception as e:                       # noqa: BLE001
                probs.append('🔴 กฎ %s · ของล่อระเบิด: %s — %s' % (rule, name, e))
                continue
            if fired == (want == 'ยิง'):
                npass += 1
            elif want == 'ยิง':
                probs.append('🔴 กฎ %s ไม่ยิงใส่ของล่อ: %s'
                             ' ⇒ **กฎตาย** ⇒ เลข "จับ" ของกฎนี้อ่านไม่ได้'
                             % (rule, name))
            else:
                probs.append('🔴 กฎ %s ยิงใส่ของสะอาด: %s'
                             ' ⇒ **กฎยิงมั่ว** ⇒ เลข "จับ" ของกฎนี้เชื่อไม่ได้'
                             % (rule, name))
        out[rule] = (npass, len(cases), probs)
    return out


def decoy_tag(res, rule):
    npass, total, probs = res.get(rule, (0, 0, ['ไม่มีข้อมูล']))
    # ⛔ 0/0 ห้ามเป็น ✅ — 0/0 ที่พิมพ์ ✅ คือคำโกหกที่หน้าตาเหมือนหลักฐาน
    ok = (not probs) and total > 0 and npass == total
    return 'ของล่อ %d/%d %s' % (npass, total, '✅' if ok else '⛔')


# ─────────────────────────────────────────────────────────────
# เส้นทางการรันจริง
# ─────────────────────────────────────────────────────────────
def load_sets(root):
    """อ่าน data/sets/*.json — คืน (รายการ (ชื่อ, questions), เหตุผลที่ตัดสินไม่ได้)

    ⛔ ไฟล์ที่อ่านไม่ออกแม้แต่ไฟล์เดียว ⇒ ตัดสินไม่ได้ทั้งด่าน
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


def head_sha(root):
    """SHA ปัจจุบัน — ผูกรายงานกับของจริง ⛔ ด่านนี้ไม่มีฐาน อ่าน working tree"""
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
    _verdict = verdict_labels if verdict is None else verdict
    lines = []
    ok, bad = check_pins()
    if not ok:
        lines.append('🔴 รายการที่ปักไว้ในตัวด่านเองผิดรูป ⇒ ตัดสินไม่ได้')
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

    div = {'q': 0, 'withfig': 0, 'lab': 0, 'num': 0}
    per_q = {}
    for name, qs in sets:
        d, pq = _scan(qs, name)
        for k in div:
            div[k] += d[k]
        per_q.update(pq)

    lines.append('check_orphan_labels v%s · ที่ %s'
                 % (CHECKER_VERSION, head_sha(root)))
    lines.append('⑨ ตัวหาร (คลังที่บังคับ = %s): ไฟล์ชุด %d · ข้อ %d'
                 ' · **ข้อที่มีรูป %d** · ป้ายในรูป %d · ป้ายที่เป็นตัวเลขล้วน %d'
                 % (SETS_DIR, len(sets), div['q'], div['withfig'],
                    div['lab'], div['num']))
    lines.append('   ตัวหารของด่านนี้คือ "ข้อที่มีรูป" ⛔ ไม่ใช่ "ข้อทั้งหมด"'
                 ' — ข้อที่ไม่มีรูป ด่านนี้ไม่มีอะไรจะพูดถึง')
    lines.append('   เพดานที่ประกาศไว้: ป้ายที่ |ค่า| <= %d ⛔ ไม่ตัดสิน'
                 ' (ถอดเพดานออกจะได้ธง 11 ข้อ ซึ่ง 9 ข้อเป็นแดงปลอม)' % CUTOFF)

    problems = _verdict(per_q, PINNED)

    lines.append('')
    lines.append('รายงานแยกกฎ — เลข "จับ" ทุกตัวมีของล่อกำกับ ⇒ 0 อ่านได้ว่าสะอาด'
                 ' ⛔ ไม่ใช่กฎตาย')
    lines.append('กฎ ก · ป้ายเลขที่ไม่มีที่มาในข้อ : จับ %d ข้อ · %s'
                 % (len(per_q), decoy_tag(dres, 'ก')))
    lines.append('กฎ ข · รายการที่ปักไว้ต้องตรงเป๊ะ : ไม่ตรง %d จุด · %s'
                 ' · รายการที่ปักไว้ %d ข้อ'
                 % (len(problems), decoy_tag(dres, 'ข'), len(PINNED)))

    for qid, (setname, labs) in sorted(per_q.items()):
        mark = '✅ ปักไว้แล้ว' if qid in PINNED else '🔴 ยังไม่ได้ปัก'
        lines.append('   %s %-24s (%s) ป้าย: %s'
                     % (mark, qid, setname, ' · '.join(labs)))

    # เครื่องมือแดงมาก่อนเนื้อหาแดงเสมอ — ถ้ากฎตาย เลขเนื้อหาของกฎนั้นไม่มีความหมาย
    if dprobs:
        lines.append('')
        lines += dprobs
        lines.append('')
        lines.append('⇒ รหัส 2 · ของล่อของกฎข้างต้นไม่ทำงาน ⇒ **ตัดสินไม่ได้**')
        lines.append('   ⛔ ห้ามอ่านเลข "จับ" ของกฎที่ของล่อตก — 0 ของมันแปลไม่ได้')
        return 2, lines

    if problems:
        lines.append('')
        lines += problems
        lines.append('')
        lines.append('⇒ รหัส 1 · แก้ที่ %s หรือปักบรรทัดพร้อมเหตุผล'
                     ' แล้วรันใหม่' % SETS_DIR)
        return 1, lines
    lines.append('')
    lines.append('✅ ป้ายเลขที่ไม่มีที่มา ตรงกับรายการที่ปักไว้เป๊ะ'
                 ' (จับ %d · ปักไว้ %d)' % (len(per_q), len(PINNED)))
    return 0, lines


# ─────────────────────────────────────────────────────────────
# self-test — ⛔ ด่านของตัวด่านเอง ห้ามพึ่งคลังจริง
# ─────────────────────────────────────────────────────────────
def _scan_dead(questions, setname='<mem>'):
    """ตัวจับตาย — วัดตัวหารได้ แต่ไม่เคยเจออะไร"""
    div, _ = scan_questions(questions, setname)
    return div, {}


def _scan_loud(questions, setname='<mem>'):
    """ตัวจับยิงมั่ว — ยกธงทุกข้อที่มีรูป"""
    div, _ = scan_questions(questions, setname)
    return div, {(q.get('id') or '?'): (setname, ('9999',))
                 for q in questions if q.get('imageSpec')}


def _write_repo(root, files):
    d = os.path.join(root, SETS_DIR)
    os.makedirs(d, exist_ok=True)
    for name, payload in files.items():
        with open(os.path.join(d, name), 'w', encoding='utf-8') as fh:
            if isinstance(payload, str):
                fh.write(payload)
            else:
                json.dump(payload, fh, ensure_ascii=False)


def selftest():
    fails = []

    def eq(name, got, want):
        if got != want:
            fails.append('%s: ได้ %r ควรได้ %r' % (name, got, want))

    # ① ป้ายที่ไม่มีที่มา ⇒ ติดธง
    eq('① ป้ายกำพร้า', orphan_labels(
        _q('a', imageSpec={'labels': [{'text': '22.5'}]})), (True, ('22.5',)))
    # ② ป้ายที่มีที่มาในโจทย์ ⇒ เงียบ
    eq('② ป้ายมีที่มา', orphan_labels(
        _q('a', question='$22.5$', imageSpec={'labels': [{'text': '22.5'}]})),
        (True, ()))
    # ③ เพดาน — |ค่า| <= CUTOFF ⛔ ไม่ตัดสิน
    eq('③ เลขแกนเล็ก', orphan_labels(
        _q('a', imageSpec={'labels': [{'text': '10'}]})), (True, ()))
    eq('③ เกินเพดานนิดเดียวยังจับ', orphan_labels(
        _q('a', imageSpec={'labels': [{'text': '10.5'}]})), (True, ('10.5',)))
    # ④ ไม่มีรูป ⇒ ไม่อยู่ในตัวหาร (กับดัก ⑥ — "ไม่มีของ" ≠ "ตรวจแล้วสะอาด")
    eq('④ ไม่มี imageSpec ⇒ นอกตัวหาร', orphan_labels(_q('a')), (False, ()))
    # ⑤ walker ต้องลงทั้ง dict และ list (กับดัก ④)
    eq('⑤ ป้ายซ่อนลึก', orphan_labels(
        _q('a', imageSpec={'curves': [{'labels': [{'text': '4321'}]}]})),
        (True, ('4321',)))
    eq('⑤ imageSpec เป็น list ของ dict', orphan_labels(
        _q('a', imageSpec=[{'label': '4321'}, {'caption': '8765'}])),
        (True, ('4321', '8765')))
    # ⑥ คีย์ที่ไม่ใช่ป้าย ⛔ ห้ามนับ (ไม่งั้นพิกัดทุกจุดจะกลายเป็นธง)
    eq('⑥ พิกัดไม่ใช่ป้าย', orphan_labels(
        _q('a', imageSpec={'points': [{'x': 5000, 'y': 8000}]})), (True, ()))
    eq('⑥ ค่าตัวเลข (ไม่ใช่สตริง) ใต้คีย์ป้าย ⛔ ไม่นับ', orphan_labels(
        _q('a', imageSpec={'segments': [{'label': 4321, 'value': 4321}]})),
        (True, ()))
    # ⑦ ลูกน้ำหลักพัน — ต้องเทียบได้ทั้งสองแบบ
    eq('⑦ ป้ายมีลูกน้ำ เนื้อข้อไม่มี', orphan_labels(
        _q('a', question='$1200$', imageSpec={'labels': [{'text': '1,200'}]})),
        (True, ()))
    eq('⑦ ป้ายไม่มีลูกน้ำ เนื้อข้อมี', orphan_labels(
        _q('a', question='$1,200$', imageSpec={'labels': [{'text': '1200'}]})),
        (True, ()))
    # ⑧ ที่มาต้องเป็นฟิลด์ที่เด็กเห็น ⛔ ไม่ใช่บันทึกงาน (กับดัก ⑪)
    eq('⑧ notes ⛔ ไม่นับเป็นที่มา', orphan_labels(
        _q('a', notes='เคยแก้ป้าย 22.5 ไว้',
           imageSpec={'labels': [{'text': '22.5'}]})), (True, ('22.5',)))
    eq('⑧ tables นับเป็นที่มา', orphan_labels(
        _q('a', tables=[{'rows': [['22.5']]}],
           imageSpec={'labels': [{'text': '22.5'}]})), (True, ()))
    # ⑨ ตัวเลขติดลบ / ไม่ใช่ตัวเลข
    eq('⑨ ป้ายติดลบเกินเพดาน', orphan_labels(
        _q('a', imageSpec={'labels': [{'text': '-62'}]})), (True, ('-62',)))
    eq('⑨ ป้ายที่มีหน่วยปน ⛔ ไม่ตัดสิน', orphan_labels(
        _q('a', imageSpec={'labels': [{'text': '62 ซม.'}]})), (True, ()))

    # ⑩ รายการที่ปักไว้ — สองทาง
    eq('⑩ ตรงเป๊ะ ⇒ ไม่มีปัญหา',
       verdict_labels({'a': ('s', ('62',))}, {'a': (('62',), 'x' * 50)}), [])
    eq('⑩ มีธงแต่ไม่ได้ปัก ⇒ 1 ปัญหา',
       len(verdict_labels({'a': ('s', ('62',))}, {})), 1)
    eq('⑩ ปักแต่ไม่มีธงแล้ว ⇒ 1 ปัญหา',
       len(verdict_labels({}, {'a': (('62',), 'x' * 50)})), 1)
    eq('⑩ ชุดป้ายเปลี่ยน ⇒ 1 ปัญหา',
       len(verdict_labels({'a': ('s', ('62', '99'))}, {'a': (('62',), 'x' * 50)})),
       1)

    # ⑪ รายการที่ปักไว้ผิดรูป ⇒ ตัวเครื่องมือแดง
    eq('⑪ เหตุผลสั้น ⇒ ไม่ผ่าน',
       check_pins({'x': (('62',), 'สั้น')})[0], False)
    eq('⑪ ชุดป้ายไม่เรียง ⇒ ไม่ผ่าน',
       check_pins({'x': (('99', '62'), 'x' * 50)})[0], False)
    eq('⑪ ชุดป้ายว่าง ⇒ ไม่ผ่าน', check_pins({'x': ((), 'x' * 50)})[0], False)
    eq('⑪ ไม่ใช่ dict ⇒ ไม่ผ่าน', check_pins([])[0], False)
    ok, _ = check_pins(PINNED)
    eq('⑪ รายการจริงในไฟล์นี้ต้องผ่าน', ok, True)

    # ⑫ คลังว่าง / JSON เสีย ⇒ 2 ⛔ ไม่ใช่ 0
    with tempfile.TemporaryDirectory() as t:
        code, out = run(t)
        eq('⑫ ไม่มีโฟลเดอร์ชุด ⇒ 2', code, 2)
        eq('⑫ พิมพ์ว่าตัดสินไม่ได้', any('ตัดสินไม่ได้' in x for x in out), True)
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': '{ ไม่ใช่ JSON'})
        eq('⑫ JSON เสีย ⇒ 2', run(t)[0], 2)

    # ⑬ ตัวหารต้องถูกพิมพ์จริง ⛔ ไม่ใช่รายงานที่ซ่อนว่าตรวจอะไรไปกี่ชิ้น
    #
    # ⚠️ คลังจำลองในเคสนี้ **ไม่มี** ข้อที่ปักไว้ทั้งสองข้อของคลังจริง
    #    ⇒ ถ้าปล่อยให้ PINNED จริงมีผล ขาลงของกฎ ข จะยิง (รายการปักค้าง 2 บรรทัด)
    #      แล้วเคสนี้จะได้ 1 ทั้งที่กำลังทดสอบเรื่อง "พิมพ์ตัวหาร" คนละเรื่องกัน
    #    ⇒ สลับรายการปักเป็นว่างชั่วคราว แล้วคืนค่าใน finally
    #    ⛔ ห้ามแก้ด้วยการเติมข้อ pat1-2560-03-q35 ปลอมลงคลังจำลอง —
    #      นั่นคือการผูก self-test กับเนื้อหาของคลังจริง (กับดัก ⑰)
    #
    # 🔴 ผลพลอยได้ที่ตั้งใจ: ตอนนี้ค่าที่ "พิมพ์" (0) ต่างจากค่าจริงในไฟล์ (2)
    #    ⇒ ถ้าใครฮาร์ดโค้ดเลขรายการที่ปักไว้ลงในข้อความรายงาน เคสนี้จะจับได้
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [
            _q('z-q1', imageSpec={'labels': [{'text': '5'}]}),
            _q('z-q2')]}})
        _real_pin = globals()['PINNED']
        globals()['PINNED'] = {}
        try:
            code, out = run(t)
        finally:
            globals()['PINNED'] = _real_pin
        txt = '\n'.join(out)
        eq('⑬ ข้อมูลสะอาด + รายการปักว่าง ⇒ 0', code, 0)
        eq('⑬ พิมพ์ตัวหารเป็น "ข้อที่มีรูป" ไม่ใช่ "ข้อทั้งหมด"',
           'ข้อ 2' in txt and 'ข้อที่มีรูป 1' in txt, True)
        eq('⑬ พิมพ์ทั้งสองกฎ', all(k in txt for k in ['กฎ ก', 'กฎ ข']), True)
        eq('⑬ พิมพ์จำนวนรายการที่ปักไว้ตามของที่ใช้จริงตอนรัน ⛔ ไม่ใช่ค่าคงที่',
           'รายการที่ปักไว้ 0 ข้อ' in txt, True)
        eq('⑬ คืนค่ารายการจริงแล้ว', PINNED is _real_pin, True)
        eq('⑬ รายการจริงยังมี 2 บรรทัด ⇒ 0 ข้างบนมาจากตัวแปรสด', len(PINNED), 2)

    # ⑭ ธงใหม่ที่ไม่ได้ปัก ⇒ 1 (เนื้อหาแดง)
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [
            _q('z-q9', imageSpec={'labels': [{'text': '4321'}]})]}})
        code, out = run(t)
        eq('⑭ ธงที่ไม่ได้ปัก ⇒ 1', code, 1)
        eq('⑭ รายงานชี้ข้อที่ต้องไปอ่าน',
           any('z-q9' in x and 'ยังไม่ได้ปัก' in x for x in out), True)

    # ⑮ ขาลงที่ระดับ run() — รายการปักค้างโดยไม่มีธงแล้ว ⇒ 1
    #    ⛔ ห้ามฉีดผ่าน verdict= เพราะตัวเดียวกันถูกใช้ยิงของล่อของกฎ ข ด้วย
    #      ⇒ สลับตัวแปรระดับโมดูลชั่วคราวแทน แล้วคืนค่าใน finally
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [_q('z-q1')]}})
        _real_pin = globals()['PINNED']
        globals()['PINNED'] = dict(_PIN_STALE)
        try:
            code, out = run(t)
        finally:
            globals()['PINNED'] = _real_pin
        eq('⑮ รายการปักค้าง ⇒ 1', code, 1)
        eq('⑮ รายงานสั่งให้ลบบรรทัดที่ค้าง',
           any('รายการปักค้าง' in x for x in out), True)
        eq('⑮ คืนค่ารายการจริงแล้ว', PINNED is _real_pin, True)

    # ⑯ e2e — รันเป็นโปรเซสจริง อ่านรหัสที่ "เชลล์เห็น" (กับดัก ⑦ก)
    here = os.path.abspath(__file__)
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [
            _q('z-q9', imageSpec={'labels': [{'text': '4321'}]})]}})
        r = subprocess.run([sys.executable, here, '--root', t],
                           capture_output=True, text=True)
        eq('⑯ e2e เนื้อหาแดง ⇒ เชลล์เห็น 1', r.returncode, 1)
    with tempfile.TemporaryDirectory() as t:
        r = subprocess.run([sys.executable, here, '--root', t],
                           capture_output=True, text=True)
        eq('⑯ e2e ตัดสินไม่ได้ ⇒ เชลล์เห็น 2', r.returncode, 2)

    # ⑰ ของล่อชุดจริงในไฟล์นี้ต้องผ่านครบทุกกฎ และต้องมีสองขั้วครบทุกกฎ
    res = run_decoys()
    for r in DECOY_RULES:
        npass, total, probs = res[r]
        eq('⑰ กฎ %s ของล่อผ่านครบ' % r, (npass, total > 0, probs), (total, True, []))
        wants = {w for _, w, _, _ in DECOYS[r]}
        eq('⑰ กฎ %s มีของล่อทั้งบวกและลบ' % r, wants, {'ยิง', 'เงียบ'})
        eq('⑰ กฎ %s ป้ายเป็น ✅' % r, decoy_tag(res, r).endswith('✅'), True)

    # ⑱ รายงานของ "การรันจริง" ต้องพิมพ์ของล่อแยกกฎ ⛔ ไม่ใช่มีแต่ใน --selftest
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [_q('z-q1')]}})
        out = run(t)[1]
        txt = '\n'.join(out)
        for r in DECOY_RULES:
            eq('⑱ บรรทัดกฎ %s มีทั้ง "จับ/ไม่ตรง" และ "ของล่อ …/… ✅"' % r,
               any(x.startswith('กฎ %s ' % r)
                   and ('ของล่อ %d/%d ✅' % (res[r][1], res[r][1])) in x
                   for x in out), True)
        eq('⑱ ⛔ ไม่มีการพิมพ์รวมแบบไม่มีของล่อกำกับ', 'ของล่อ 0/0' in txt, False)

    # ⑲ ตัวจับตาย (จับ 0 ทุกกฎ) ⇒ ต้องเป็นรหัส 2 ⛔ ไม่ใช่ 0 ที่ดูเหมือนคลังสะอาด
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [_q('z-q1')]}})
        code, out = run(t, scan=_scan_dead)
        eq('⑲ กฎตาย ⇒ 2', code, 2)
        eq('⑲ รายงานบอกว่ากฎตาย', any('กฎตาย' in x for x in out), True)
        eq('⑲ กฎที่ของล่อตกต้องไม่ติดป้าย ✅',
           any(x.startswith('กฎ ก ') and '⛔' in x for x in out), True)

    # ⑳ ตัวจับยิงมั่ว ⇒ ต้องเป็นรหัส 2 เช่นกัน (เลขที่จับได้เชื่อไม่ได้)
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [_q('z-q1')]}})
        code, out = run(t, scan=_scan_loud)
        eq('⑳ ยิงมั่ว ⇒ 2', code, 2)
        eq('⑳ รายงานบอกว่ายิงมั่ว', any('กฎยิงมั่ว' in x for x in out), True)

    # ㉑ กฎที่ไม่มีของล่อ ⇒ 2 และ ⛔ ห้ามพิมพ์ `0/0 ✅`
    empty = {r: [] for r in DECOY_RULES}
    eq('㉑ ป้ายของ 0/0 ต้องเป็น ⛔', decoy_tag(run_decoys(empty), 'ก'),
       'ของล่อ 0/0 ⛔')
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [_q('z-q1')]}})
        code, out = run(t, decoys=empty)
        eq('㉑ ไม่มีของล่อ ⇒ 2', code, 2)
        eq('㉑ รายงานบอกว่าอ่านเลขไม่ได้',
           any('อ่านไม่ได้' in x for x in out), True)

    # ㉒ ถอดของล่อออกเงียบ ๆ / ของล่อขั้วเดียว ⇒ ต้องเป็นรหัส 2
    for r in DECOY_RULES:
        eq('㉒ หมุด DECOY_MIN กฎ %s ไม่เกินของล่อจริง' % r,
           DECOY_MIN[r] <= len(DECOYS[r]), True)
        eq('㉒ หมุด DECOY_MIN กฎ %s ไม่ต่ำกว่า 3' % r, DECOY_MIN[r] >= 3, True)
    thin = {r: list(DECOYS[r]) for r in DECOY_RULES}
    thin['ก'] = thin['ก'][:-1]
    eq('㉒ กฎที่โดนถอดต้องติด ⛔', decoy_tag(run_decoys(thin), 'ก').endswith('⛔'),
       True)
    eq('㉒ กฎอื่นไม่โดนหางเลข', decoy_tag(run_decoys(thin), 'ข').endswith('✅'),
       True)
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [_q('z-q1')]}})
        code, out = run(t, decoys=thin)
        eq('㉒ ถอดของล่อ ⇒ 2', code, 2)
        eq('㉒ รายงานบอกว่าถูกถอดออกเงียบ ๆ',
           any('ถอดออกเงียบ ๆ' in x for x in out), True)
    onepol = {r: [c for c in DECOYS[r] if c[1] == 'ยิง'] for r in DECOY_RULES}
    onepol = {r: (v * 4)[:max(DECOY_MIN[r], len(v))] for r, v in onepol.items()}
    eq('㉒ข ขั้วเดียวต้องติด ⛔',
       decoy_tag(run_decoys(onepol), 'ก').endswith('⛔'), True)
    with tempfile.TemporaryDirectory() as t:
        _write_repo(t, {'a.json': {'questions': [_q('z-q1')]}})
        code, out = run(t, decoys=onepol)
        eq('㉒ข ขั้วเดียว ⇒ 2', code, 2)
        eq('㉒ข รายงานบอกว่าขั้วเดียว', any('ขั้วเดียว' in x for x in out), True)

    print('self-test ของ check_orphan_labels v%s — %d เคส'
          % (CHECKER_VERSION, 22))
    if fails:
        print('🔴 ตก %d ข้อ:' % len(fails))
        for f in fails:
            print('   ' + f)
        return 2                    # ตัวด่านเองพัง = เครื่องมือแดง ⛔ ไม่ใช่เนื้อหาแดง
    print('✅ ผ่านทุกเคส')
    return 0


def main():
    ap = argparse.ArgumentParser(
        description='ตรวจว่าตัวเลขบนรูปมีที่มาในเนื้อข้อเดียวกัน')
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

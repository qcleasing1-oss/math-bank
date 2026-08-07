#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ด่าน 17 · เฉลยข้อ **เติมคำ (fill)** ต้องประกาศค่าที่ตรงกับคีย์
ด่าน 18 · ช่องคำตอบต้องรับคีย์ของตัวเอง (correct ต้องอยู่ใน accept)

ที่มา (5 ส.ค. 2569 · จดหมายพอร์ทัล E→MB #22 ข้อ ③):
    ด่าน 7 (check_answer_claim.py) มีเงื่อนไข eligible() ว่า `q['type'] == 'mc'`
    ⇒ ข้อชนิด `fill` **ไม่เคยถูกด่าน 7 มองเห็นเลยสักข้อ**
    ตราบใดที่ในคลังมี fill อยู่ไม่กี่ข้อ เรื่องนี้เป็นหนี้เล็ก
    แต่ก้อน 19 เปิดชนิด fill เป็นครั้งแรกในสายงานแต่งใหม่ (6 ข้อ)
    และโควตาก้อน 20 สั่ง fill ≥ 8 ⇒ หนี้กำลังจะโตเร็วกว่าที่ด่านจะตามทัน
    ⇒ พอร์ทัลสั่ง: **ทำด่านคู่ขนานก่อนแต่งก้อน 20** ⛔ ไม่ใช่ "ทำทีหลังเมื่อ fill เยอะพอ"

⛔ ทำไมเป็นไฟล์แยก ไม่ใช่แก้ eligible() ของด่าน 7 ให้รับ fill ด้วย
   เพราะของที่ตรวจคนละอย่างกัน :
     ด่าน 7  ตรวจ "เลขตัวเลือก" — ตัวเลขเล็ก ๆ 1-4 อ่านจากคำว่า "ตัวเลือก N"
     ด่าน 17 ตรวจ "ค่าคำตอบ"   — เศษส่วน ทศนิยม เลขติดลบ หน่วยพันบาท ฯลฯ
   ถ้ายัดสองเรื่องลงฟังก์ชันเดียว วันที่ด่านแดงจะตอบไม่ได้ว่า "แดงเพราะเรื่องไหน"
   (บทเรียนข้อ ๘ ของรอบ 14 — เหตุผลเดียวกับที่ด่าน 8 แยกจากด่าน 7)

⛔ ทำไม "คัดลอก" รายการคำสำคัญมาจากด่าน 7 แทนที่จะ import
   ถ้า import ⇒ วันที่ใครแก้รายการของด่าน 7 จนตาบอด ด่าน 17 จะตาบอดตามเงียบ ๆ
   ⇒ ถือสำเนาของตัวเอง + มีตัวตรวจ "สองฝั่งยังตรงกันไหม" ใน --selftest
      (อ่านไฟล์พี่น้องเป็น**ข้อความล้วน** ⛔ ไม่ import — กับดัก ⑦ เดียวกับด่าน 2)

⛔ จุดตาบอดที่ยอมรับไว้อย่างรู้ตัว — เขียนไว้ตรงนี้เพื่อไม่ให้ใครเข้าใจผิดภายหลัง
   ① ด่านนี้ใช้เกณฑ์ "**ค่าของคีย์ต้องปรากฏ**ในบรรทัดคำตอบ" ⛔ ไม่ใช่ "บรรทัดคำตอบมีค่าเดียว"
      เพราะบรรทัด ✅ ของข้อ fill มีเลขอื่นปนได้ตามธรรมชาติ (สูตร · หน่วย · ตัวประกอบ)
      ⇒ ข้อที่คีย์ไปตรงกับ "เลขระหว่างทาง" โดยบังเอิญ ด่านนี้จะไม่จับ
   ② ตรวจเฉพาะข้อที่ **คีย์เป็นจำนวนเดี่ยว** · คีย์ที่เป็นสูตร/ข้อความ = นอกขอบเขต
      ⛔ "นอกขอบเขต" ไม่เท่ากับ "ตรวจแล้วผ่าน" — จึงนับแยกถังและมีเพดาน

รหัสออก: 0 = ผ่าน · 1 = เนื้อหาแดง · 2 = ตัวเครื่องมือแดง
"""
import argparse
import glob
import json
import os
import re
import sys
from fractions import Fraction

CHECKER_VERSION = '1.0'

# ── บรรทัดที่ถือว่า "ประกาศคำตอบ" — สำเนาจากด่าน 7 (ดูเหตุผลหัวไฟล์) ──
ANSWER_MARKERS = ('✅', 'คำตอบ:', 'คำตอบคือ', 'จึงตอบ', 'ดังนั้นตอบ')

# ── บรรทัดที่พูดถึงตัวลวง/กับดัก โดยเจตนา — ไม่ใช่คำประกาศคำตอบ ──
#    เท่ากับของด่าน 7 ทุกคำ + 'กับดัก' ซึ่งพบเฉพาะในเฉลยข้อ fill
SKIP_MARKERS = ('จุดพลาด', 'เผลอ', 'ตัวลวง', 'มักตอบ',
                'หากตอบ', 'ถ้าตอบ', 'ผิดตรง', 'ดักไว้', 'กับดัก')

# ── ความคลาดเคลื่อนสัมพัทธ์ที่ยอมให้ ────────────────────────────────
#    เฉลยเขียน 0.8959 ขณะที่คีย์เก็บ 0.89585 = การปัดที่ถูกต้อง ⛔ ไม่ใช่ความผิด
#    ⚠️ ตั้งหลวมกว่านี้เมื่อไหร่ = ยอมให้ "เฉลยผิดนิดหน่อย" ผ่านด่าน
TOL = Fraction(1, 200)          # 0.5%

# ── เส้นแบ่ง "ปัดเลข" กับ "คนละหน่วย" ในรายการเฝ้าดูของ accept ────────
#    0.33 แทน 1/3 · 3.9 แทน 3.95 = ปัดเลข ⇒ น่าเบื่อ นับรวมพอ
#    0.1587 แทน 15.87 (0.01×) · -5.6 แทน 5.6 (-1×) = คนละหน่วย ⇒ ต้องอ่านทีละอัน
ROUND_TOL = Fraction(1, 50)     # 2%

# ── เพดานหนี้ · ratchet เดินลงทางเดียว ───────────────────────────────
#    ⚠️ เลขเหล่านี้ ⛔ ไม่ใช่เป้าหมาย — เป็น "ที่ที่เรายืนอยู่วันนี้"
#    (6 ส.ค. 69 · วัดด้วยด่านตัวนี้เอง ⛔ ไม่ได้ยกมาจากสคริปต์สอบเทียบตัวก่อน
#     เพราะตัวนั้นนิยาม "ข้อที่เข้าข่าย" ไม่เหมือนกัน — 1,991 vs 2,069)
#    ทุกครั้งที่ยอดลดจริง ให้ปรับลงตาม ⛔ ห้ามขยับขึ้นโดยไม่มีเหตุผลในคอมมิต
MAX_NO_VALUE = 15        # เฉลยไม่ประกาศค่าเลย ⇒ ด่าน 17 มองไม่เห็น
#   🔻 7 ส.ค. 69 : 19 → 15  (แก้ gen-chap-18 q09/q23/q44/q45 ให้บรรทัด ✅ พกค่าคำตอบมาด้วย)
#      ⛔ เพดานขยับลงได้อย่างเดียว
MAX_OUT_OF_SCOPE = 332   # คีย์ไม่ใช่จำนวนเดี่ยว (สูตร/ข้อความ/หลายค่า)
MAX_NO_ACCEPT = 1117     # ไม่มีสนาม accept เลย ⇒ ด่าน 18 มองไม่เห็น
MAX_KEY_NOT_IN_ACCEPT = 81

# ── ⑨ พื้นตัวหาร — กันยอดหนี้ "ลดลง" เพราะไฟล์ชุดหายไป ────────────
#    วันนี้เข้าข่าย 2,069 ข้อ ⇒ ตั้งพื้นไว้ 1,950 (≈94%) เท่าสัดส่วนเดียวกับด่าน 7
MIN_ELIGIBLE = 1950

# ── เพดานล่างของความครอบคลุม — กันด่านตาบอดเงียบ ─────────────────
#    ถ้าใครลบคำใน ANSWER_MARKERS จนหมด ด่านจะเขียวตลอดกาลโดยไม่ตรวจอะไร
DEFAULT_MIN_COVERAGE = 0.50


# ═════════════════════════════════════════════════════════════
#  ตัวอ่านค่าจากข้อความคณิตศาสตร์
# ═════════════════════════════════════════════════════════════
DASHES = ('\u2212', '\u2013', '\u2014', '\u2043')   # − – — ⁃  ⇒ ทั้งหมดคือลบ
FR = re.compile(r'(-?)\s*\\frac\{\s*(-?\d+(?:\.\d+)?)\s*\}\{\s*(-?\d+(?:\.\d+)?)\s*\}')
SL = re.compile(r'(-?\d+(?:\.\d+)?)\s*/\s*(-?\d+(?:\.\d+)?)')
PL = re.compile(r'-?\d+(?:\.\d+)?')


def clean(s):
    """ทำข้อความให้เป็นรูปเดียวก่อนอ่านค่า

    ⚠️ ทุกบรรทัดในนี้มาจาก false positive จริงที่เจอตอนสอบเทียบกับคลังทั้งใบ
       ⛔ อย่าลบบรรทัดไหนออกโดยไม่รันสอบเทียบใหม่
    """
    t = str(s)
    for d in DASHES:
        t = t.replace(d, '-')
    for junk in ('{,}', '\\,', '\\;', '\\!', '\\ ', '~'):
        t = t.replace(junk, '')
    for f in ('\\dfrac', '\\tfrac', '\\cfrac'):
        t = t.replace(f, '\\frac')
    t = re.sub(r'(?<=\d),(?=\d{3}(?!\d))', '', t)          # 2,625 ⇒ 2625
    t = re.sub(r'\\frac\s*(\d)\s*(\d)(?!\d)', r'\\frac{\1}{\2}', t)   # \frac72
    t = re.sub(r'\\frac\s*\{([^{}]*)\}\s*(\d)(?!\d)', r'\\frac{\1}{\2}', t)
    t = re.sub(r'\\frac\s*(\d)\s*\{([^{}]*)\}', r'\\frac{\1}{\2}', t)
    return t


def vals(text):
    """คืน (รายการค่าที่อ่านได้, เศษข้อความที่เหลือหลังคาดทับตัวเลขออกหมด)

    ⛔ ต้องกวาดสามรอบและ "คาดทับ" ของที่จับได้ทิ้ง ไม่ใช่กวาดพร้อมกัน
       เหตุผล: $-\\frac{1}{8}$ มีเครื่องหมายลบอยู่ **นอก** วงเล็บของเศษส่วน
       ถ้าปล่อยให้ตัวจับเลขล้วนเห็น 1 กับ 8 ก่อน จะได้ค่าผิดสองค่าแทนค่าถูกค่าเดียว
    """
    t = clean(text)
    out = []

    def eat(rx, conv):
        nonlocal t
        buf, pos = [], 0
        for m in rx.finditer(t):
            try:
                v = conv(m)
            except (ZeroDivisionError, ValueError, ArithmeticError):
                continue
            out.append(v)
            buf.append(t[pos:m.start()])
            buf.append(' ' * (m.end() - m.start()))
            pos = m.end()
        buf.append(t[pos:])
        t = ''.join(buf)

    eat(FR, lambda m: (Fraction(m.group(2)) / Fraction(m.group(3)))
        * (-1 if m.group(1) == '-' else 1))
    eat(SL, lambda m: Fraction(m.group(1)) / Fraction(m.group(2)))
    eat(PL, lambda m: Fraction(m.group(0)))
    return out, t


def single(key):
    """คืน (สถานะ, ค่า) ของ **คีย์**

    'num'   = คีย์เป็นจำนวนเดี่ยวล้วน ⇒ ด่านนี้ตรวจได้
    'other' = คีย์เป็นสูตร/ข้อความ/หลายค่า ⇒ **นอกขอบเขต** ⛔ ไม่ใช่ผ่าน
    """
    if key is None:
        return 'other', None
    if isinstance(key, (int, float)) and not isinstance(key, bool):
        return 'num', Fraction(str(key))
    v, res = vals(str(key))
    for junk in ('$', '\\', '{', '}', ' ', '\t'):
        res = res.replace(junk, '')
    if len(v) == 1 and not res:
        return 'num', v[0]
    return 'other', None


def near(a, b, tol=TOL):
    """เท่ากันภายในความคลาดเคลื่อนสัมพัทธ์ (0 เทียบกับ 0 ต้องเป๊ะ)"""
    if a == b:
        return True
    scale = max(abs(a), abs(b))
    if scale == 0:
        return False
    return abs(a - b) / scale <= tol


def declared_value(explanation, key):
    """คืนสถานะของ "บรรทัดคำตอบ" เทียบกับคีย์

    'hit'  = บรรทัดคำตอบมีค่าที่ตรงกับคีย์  ⇒ ผ่าน
    'miss' = บรรทัดคำตอบประกาศค่า แต่ไม่มีค่าไหนตรงคีย์เลย ⇒ 🔴 เฉลยขัดกับคีย์
    'none' = บรรทัดคำตอบไม่มีค่าเป็นตัวเลขเลย ⇒ ตรวจไม่ได้ ⛔ ไม่ใช่ผ่าน
    """
    seen = []
    for line in explanation:
        if not isinstance(line, str):
            continue
        if any(k in line for k in SKIP_MARKERS):
            continue
        if not any(k in line for k in ANSWER_MARKERS):
            continue
        v, _ = vals(line)
        seen.extend(v)
    if not seen:
        return 'none', None
    for v in seen:
        if near(v, key):
            return 'hit', v
    return 'miss', seen


def eligible(q):
    return (q.get('type') == 'fill'
            and q.get('correct') not in (None, '')
            and isinstance(q.get('explanation'), list)
            and len(q['explanation']) > 0)


# ═════════════════════════════════════════════════════════════
#  ด่าน 18 · ช่องคำตอบต้องรับคีย์ของตัวเอง
# ═════════════════════════════════════════════════════════════
def accept_verdict(q):
    """คืน (สถานะ, รายละเอียด)

    'no-field'  = ไม่มีสนาม accept ⇒ ด่าน 18 มองไม่เห็น (หนี้)
    'bad-type'  = มีสนามแต่ไม่ใช่ list ที่ไม่ว่าง ⇒ 🔴
    'dup'       = มีค่าซ้ำใน accept ⇒ 🔴 (สัญญาณว่าแก้มือชนกัน)
    'missing'   = accept ไม่รับคีย์ของตัวเอง ⇒ 🔴 เด็กตอบตามเฉลยแล้วถูกตัดผิด
    'ok'        = รับคีย์
    ⛔ เทียบด้วย "ค่า" ไม่ใช่สตริง — คลังเก่ามีทั้ง correct เป็น int และ str
    """
    if 'accept' not in q:
        return 'no-field', None
    acc = q.get('accept')
    if not isinstance(acc, list) or not acc:
        return 'bad-type', repr(acc)
    if len(set(map(str, acc))) != len(acc):
        return 'dup', acc
    st, key = single(q.get('correct'))
    if st != 'num':
        # คีย์เป็นข้อความ ⇒ เทียบแบบสตริงตรงตัวเท่านั้น
        return ('ok', None) if str(q['correct']).strip() in [str(a).strip() for a in acc] \
            else ('missing', acc)
    for a in acc:
        sa, va = single(a)
        if sa == 'num' and near(va, key):
            return 'ok', None
        if str(a).strip() == str(q['correct']).strip():
            return 'ok', None
    return 'missing', acc


def accept_offbeat(q):
    """คืนรายการ accept ที่ค่าห่างจากคีย์ — ⛔ ไม่ใช่คำตัดสิน เป็นรายการให้คนอ่าน

    ส่วนใหญ่คือ "รับอีกหน่วยหนึ่ง" ที่ตั้งใจ (ร้อยละ vs สัดส่วน · บาท vs พันบาท)
    ⛔ ด่านนี้ **ไม่ตัดสิน** ว่าถูกหรือผิด เพราะเป็นดุลพินิจของครู ไม่ใช่ของเครื่อง
       แต่ต้อง "มองเห็น" ⇒ พิมพ์ออกมาทุกครั้ง
    """
    acc = q.get('accept')
    if not isinstance(acc, list):
        return []
    st, key = single(q.get('correct'))
    if st != 'num' or key == 0:
        return []
    out = []
    for a in acc:
        sa, va = single(a)
        if sa != 'num' or near(va, key):
            continue
        ratio = va / key if key != 0 else None
        out.append((a, ratio))
    return out


def scan(sets_dir):
    stat = {'eligible': 0, 'hit': 0, 'miss': 0, 'none': 0, 'out': 0,
            'no-field': 0, 'bad-type': 0, 'dup': 0, 'missing': 0, 'ok': 0}
    red_answer, red_accept, offbeat, recs = [], [], [], []
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
        base = os.path.basename(f)
        for q in d.get('questions', []):
            if not eligible(q):
                continue
            stat['eligible'] += 1
            qid = q.get('id')

            st, key = single(q.get('correct'))
            if st != 'num':
                stat['out'] += 1
                kind = 'out'
            else:
                kind, got = declared_value(q['explanation'], key)
                stat[kind] += 1
                if kind == 'miss':
                    red_answer.append((base, qid, q.get('correct'), got))

            av, detail = accept_verdict(q)
            stat[av] += 1
            if av in ('bad-type', 'dup', 'missing'):
                red_accept.append((base, qid, av, q.get('correct'), detail))
            for a, ratio in accept_offbeat(q):
                offbeat.append((base, qid, q.get('correct'), a, ratio))

            recs.append((base, qid, kind, av))
    return stat, red_answer, red_accept, offbeat, recs


# ── ชั้นบังคับตามขอบเขต diff (แบบเดียวกับด่าน 8) ──────────────
def enforce_verdict(recs, scope_ids):
    """ข้อที่ "เปลี่ยนรอบนี้" ต้องตรวจได้จริง ⛔ ไม่ไล่เก็บหนี้เก่า

    scope_ids = None    ⇒ ทั้งคลัง · เซตว่าง ⇒ รอบนี้ไม่มีข้อเปลี่ยน
    ⛔ None กับเซตว่าง ต้องไม่ยุบเป็นค่าเดียวกัน (กับดัก ⑥)
    """
    out = []
    for base, qid, kind, av in recs:
        if scope_ids is not None and qid not in scope_ids:
            continue
        if kind != 'hit':
            out.append((base, qid, 'answer:' + kind))
        elif av != 'ok':
            out.append((base, qid, 'accept:' + av))
    return out


# ═════════════════════════════════════════════════════════════
#  SELF-TEST
# ═════════════════════════════════════════════════════════════
# (ชื่อเคส, explanation, correct, สถานะที่ต้องได้)
CASES = [
    ("เฉลยประกาศค่าตรงคีย์ (เศษส่วน dfrac)",
     ['✅ <b>คำตอบ</b> $\\dfrac{9}{40}$'], '9/40', 'hit'),

    ("🔴 ของเสียที่ต้องจับได้ · เฉลยประกาศค่าอื่น",
     ['✅ <b>คำตอบ</b> $\\dfrac{9}{41}$'], '9/40', 'miss'),

    ("🔴 เคสจริง q157 · โจทย์ถามสองอย่าง เฉลยประกาศแค่สูตร ไม่ประกาศค่า",
     ['✅ คำตอบ: $f^{-1}(x) = \\dfrac{1}{2}\\ln\\dfrac{1+x}{1-x}$'], '0.89585', 'miss'),

    ("q157 ฉบับแก้แล้ว · เติมค่าเข้าไป ⇒ ต้องผ่าน",
     ['✅ คำตอบ: $f^{-1}(x) = \\dfrac{1}{2}\\ln\\dfrac{1+x}{1-x}$ '
      'และ $f^{-1}\\left(\\dfrac{5}{7}\\right) \\approx 0.89585$'], '0.89585', 'hit'),

    ("ทศนิยมปัดแล้ว 0.8959 กับคีย์ 0.89585 ⇒ ยังถือว่าตรง",
     ['✅ คำตอบ $0.8959$'], '0.89585', 'hit'),

    ("ปัดสามหลัก 33.3 กับคีย์ 33.33 ⇒ ยังถือว่าตรง",
     ['✅ คำตอบ $33.3$'], '33.33', 'hit'),

    ("🔴 คลาดไป 5% ($0.85$ กับคีย์ $0.89585$) ⇒ ต้องแดง ไม่ใช่ 'ปัดเลข'",
     ['✅ คำตอบ $0.85$'], '0.89585', 'miss'),

    ("เครื่องหมายลบอยู่นอกเศษส่วน $-\\dfrac{1}{8}$ ต้องอ่านเป็น -1/8",
     ['✅ <b>คำตอบ</b> $-\\dfrac{1}{8}$'], '-1/8', 'hit'),

    ("🔴 สลับเครื่องหมาย · เฉลย +1/8 คีย์ -1/8 ⇒ ต้องจับได้",
     ['✅ <b>คำตอบ</b> $\\dfrac{1}{8}$'], '-1/8', 'miss'),

    ("ขีดยูนิโคด − (U+2212) ต้องอ่านเป็นลบเหมือน -",
     ['✅ <b>คำตอบ</b> $\u22125.6$'], '-5.6', 'hit'),

    ("เลขคั่นหลักพัน 705{,}100 ต้องอ่านเป็น 705100 ไม่ใช่ 705 กับ 100",
     ['✅ <b>คำตอบ</b> $705{,}100$'], '705100', 'hit'),

    ("เศษส่วนไม่มีวงเล็บ \\dfrac72 ต้องอ่านเป็น 3.5",
     ['✅ <b>คำตอบ</b> $\\dfrac72$'], '3.5', 'hit'),

    ("บรรทัดจุดพลาดมีค่าที่ตรงคีย์พอดี ⛔ ห้ามนับเป็นคำประกาศคำตอบ",
     ['⚠️ <b>จุดพลาด</b> เผลอตอบ $7$'], '7', 'none'),

    ("บรรทัด 'กับดัก' ก็ต้องข้าม (คำที่พบเฉพาะเฉลย fill)",
     ['💡 กับดักของข้อนี้คือตอบ $12$'], '12', 'none'),

    ("เฉลยมีเลขระหว่างทางปนในบรรทัดคำตอบ แต่คีย์อยู่ด้วย ⇒ ผ่าน",
     ['✅ คำตอบ: แทน $n=4$ ได้ $S_4 = 30$'], '30', 'hit'),

    ("เฉลยไม่ประกาศตัวเลขเลย ⇒ ตรวจไม่ได้ ไม่ใช่ผ่าน",
     ['✅ คำตอบ: ค่าคงตัวที่หาได้ข้างต้น'], '5', 'none'),

    ("บรรทัดที่ไม่ใช่สตริง (None ปนมา) ต้องไม่ทำให้ด่านล้ม",
     [None, '✅ คำตอบ $5$'], '5', 'hit'),

    ("ไม่มีบรรทัดไหนเข้าข่ายคำประกาศคำตอบเลย ⇒ none",
     ['<b>ขั้นที่ 1:</b> ทำไปตามขั้น $5$'], '5', 'none'),
]

# (ชื่อเคส, ข้อ, สถานะ accept ที่ต้องได้)
ACCEPT_CASES = [
    ("accept รับคีย์ตรงตัว", {'correct': '9/40', 'accept': ['9/40', '0.225']}, 'ok'),
    ("accept รับคีย์คนละรูปแต่ค่าเดียวกัน",
     {'correct': '0.225', 'accept': ['\\dfrac{9}{40}']}, 'ok'),
    ("🔴 เคสจริง q49 · accept ไม่มีคีย์ของตัวเอง",
     {'correct': 57, 'accept': ['60']}, 'missing'),
    ("q49 ฉบับแก้แล้ว · correct เป็น int กับ accept เป็นสตริง ต้องเทียบด้วยค่า",
     {'correct': 57, 'accept': ['57']}, 'ok'),
    ("🔴 accept มีค่าซ้ำ", {'correct': '5', 'accept': ['5', '5']}, 'dup'),
    ("🔴 accept เป็นลิสต์ว่าง", {'correct': '5', 'accept': []}, 'bad-type'),
    ("🔴 accept ไม่ใช่ลิสต์", {'correct': '5', 'accept': '5'}, 'bad-type'),
    ("ไม่มีสนาม accept ⇒ หนี้ ⛔ ไม่ใช่แดง", {'correct': '5'}, 'no-field'),
    ("คีย์เป็นข้อความ ⇒ เทียบสตริงตรงตัว",
     {'correct': 'x=2', 'accept': ['x=2']}, 'ok'),
]

ENFORCE_CASES = [
    ("ข้อที่เปลี่ยนรอบนี้ เฉลยไม่ประกาศค่า ⇒ ต้องแดง",
     [('f', 'NEW-1', 'none', 'ok')], {'NEW-1'}, ['NEW-1']),
    ("ข้อเก่าที่ไม่ได้แตะ ⇒ ต้องไม่แดง (ไม่ไล่เก็บหนี้เก่า)",
     [('f', 'OLD-1', 'none', 'no-field')], {'NEW-1'}, []),
    ("ข้อที่เปลี่ยนรอบนี้ ครบทั้งสองฝั่ง ⇒ ต้องไม่แดง",
     [('f', 'NEW-1', 'hit', 'ok')], {'NEW-1'}, []),
    ("ข้อที่เปลี่ยนรอบนี้ เฉลยตรงแต่ไม่มี accept ⇒ ต้องแดง",
     [('f', 'NEW-2', 'hit', 'no-field')], {'NEW-2'}, ['NEW-2']),
    ("ข้อที่เปลี่ยนรอบนี้ คีย์นอกขอบเขต ⇒ ต้องแดง (ตรวจไม่ได้ = ยังไม่ผ่าน)",
     [('f', 'NEW-3', 'out', 'ok')], {'NEW-3'}, ['NEW-3']),
    ("รอบนี้ไม่มีข้อไหนเปลี่ยน (เซตว่าง) ⇒ ไม่มีอะไรให้บังคับ",
     [('f', 'OLD-1', 'none', 'no-field')], set(), []),
    ("🔴 ขอบเขต None = ทั้งคลัง ⛔ ต้องไม่ยุบรวมกับเซตว่าง",
     [('f', 'OLD-1', 'none', 'no-field')], None, ['OLD-1']),
    ("รหัสในขอบเขตที่ไม่มีในคลัง (ข้อถูกลบ) ⇒ ต้องไม่ล้ม",
     [('f', 'NEW-1', 'hit', 'ok')], {'NEW-1', 'GHOST-9'}, []),
]


# ── มิวแทนต์ ────────────────────────────────────────────────
def _mut_no_skip_filter(explanation, key):
    """① ถอดตัวกรองบรรทัดตัวลวง/กับดัก ⇒ เสียงหลอกกลับมา"""
    seen = []
    for line in explanation:
        if isinstance(line, str) and any(k in line for k in ANSWER_MARKERS):
            seen.extend(vals(line)[0])
        elif isinstance(line, str) and any(k in line for k in SKIP_MARKERS):
            seen.extend(vals(line)[0])
    if not seen:
        return 'none', None
    return ('hit', key) if any(near(v, key) for v in seen) else ('miss', seen)


def _mut_always_none(explanation, key):
    """② ไม่ตรวจอะไรเลย แล้วรายงานว่าไม่มีของให้ตรวจ ⇒ เขียวตลอดกาล"""
    return 'none', None


def _mut_string_equal(explanation, key):
    """③ เทียบด้วยสตริงแทนค่า ⇒ 9/40 กับ 0.225 จะกลายเป็นคนละคำตอบ"""
    for line in explanation:
        if isinstance(line, str) and any(k in line for k in ANSWER_MARKERS):
            if str(key) in line:
                return 'hit', key
    return 'none', None


def _mut_no_masking(explanation, key):
    """④ ไม่คาดทับ — กวาดเลขล้วนอย่างเดียว ⇒ -\\dfrac{1}{8} อ่านเป็น 1 กับ 8"""
    seen = []
    for line in explanation:
        if not isinstance(line, str):
            continue
        if any(k in line for k in SKIP_MARKERS):
            continue
        if any(k in line for k in ANSWER_MARKERS):
            seen += [Fraction(x) for x in PL.findall(clean(line))]
    if not seen:
        return 'none', None
    return ('hit', key) if any(near(v, key) for v in seen) else ('miss', seen)


def _mut_accept_string_only(q):
    """⑤ ด่าน 18 เทียบสตริงล้วน ⇒ correct=57 (int) กับ accept=['57'] จะกลายเป็นแดง"""
    if 'accept' not in q:
        return 'no-field', None
    acc = q.get('accept')
    if not isinstance(acc, list) or not acc:
        return 'bad-type', repr(acc)
    if len(set(map(str, acc))) != len(acc):
        return 'dup', acc
    return ('ok', None) if q.get('correct') in acc else ('missing', acc)


def _mut_accept_never_red(q):
    """⑥ ด่าน 18 ไม่ตัดสินอะไรเลย"""
    return 'ok', None


def _mut_enforce_ignore_scope(recs, scope_ids):
    """⑦ ลืมขอบเขต ⇒ ไล่เก็บหนี้เก่าทั้งคลัง (ด่านจะแดงตลอดกาล)"""
    return [(b, q, k) for b, q, k, a in recs if k != 'hit' or a != 'ok']


def _mut_enforce_never_red(recs, scope_ids):
    """⑧ ไม่บังคับอะไรเลย ⇒ กติกากลับไปอยู่แต่ในจดหมาย"""
    return []


def _run_cases(fn):
    fails = []
    for name, ex, correct, want in CASES:
        try:
            st, key = single(correct)
            kind, _ = fn(ex, key) if st == 'num' else ('out', None)
            good = (kind == want)
        except Exception:
            good = False
        if not good:
            fails.append(name)
    return fails


def _run_accept_cases(fn):
    fails = []
    for name, q, want in ACCEPT_CASES:
        try:
            good = fn(q)[0] == want
        except Exception:
            good = False
        if not good:
            fails.append(name)
    return fails


def _run_enforce_cases(fn):
    fails = []
    for name, recs, scope, want in ENFORCE_CASES:
        try:
            good = sorted(q for _, q, _ in fn(recs, scope)) == sorted(want)
        except Exception:
            good = False
        if not good:
            fails.append(name)
    return fails


SIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'check_answer_claim.py')


def _sibling_markers():
    """อ่านรายการคำสำคัญของด่าน 7 แบบ **ข้อความล้วน** ⛔ ไม่ import

    เหตุผล: ถ้าตัวสคริปต์พี่น้องเพี้ยน ด่านที่พึ่งตรรกะของมันก็เพี้ยนตาม
            ด่านต้องตอบได้แม้ของที่อ้างอิงจะพัง (กับดัก ⑦ เดียวกับด่าน 2)
    """
    if not os.path.exists(SIB):
        return None, None
    src = open(SIB, encoding='utf-8').read()

    def grab(name):
        m = re.search(name + r'\s*=\s*\(([^)]*)\)', src, re.S)
        if not m:
            return None
        return tuple(re.findall(r"'([^']*)'", m.group(1)))
    return grab('ANSWER_MARKERS'), grab('DISTRACTOR_MARKERS')


def selftest():
    print('─' * 66)
    print(f'SELF-TEST ด่าน 17+18 v{CHECKER_VERSION} — ตัวอย่างดี/เสียฝังในตัว')
    print('─' * 66)
    ok = True

    print('  ── ด่าน 17 · เฉลยประกาศค่าตรงคีย์ ──')
    for name, ex, correct, want in CASES:
        st, key = single(correct)
        kind, _ = declared_value(ex, key) if st == 'num' else ('out', None)
        good = (kind == want)
        print(f'  {"✅" if good else "🔴"}  [{kind:<4}] {name}')
        ok &= good

    print()
    print('  ── ด่าน 18 · ช่องคำตอบต้องรับคีย์ ──')
    for name, q, want in ACCEPT_CASES:
        got = accept_verdict(q)[0]
        good = (got == want)
        print(f'  {"✅" if good else "🔴"}  [{got:<8}] {name}')
        ok &= good

    print()
    print('  ── ชั้นบังคับตามขอบเขต diff ──')
    for name, recs, scope, want in ENFORCE_CASES:
        got = sorted(q for _, q, _ in enforce_verdict(recs, scope))
        good = got == sorted(want)
        print(f'  {"✅" if good else "🔴"}  {name}')
        ok &= good

    print()
    print('  ── นับด่านที่ล้มเมื่อใส่บั๊กเข้าไป (ด่านต้องมีคนเฝ้า) ──')
    print('     ⛔ แดงเฉย ๆ ไม่พอ — ต้องบอกได้ว่า "แดงเพราะเคสไหน" (กับดัก ⑦ข)')
    for label, fails, total in (
        ('① ถอดตัวกรองบรรทัดตัวลวง', _run_cases(_mut_no_skip_filter), len(CASES)),
        ('② ไม่ตรวจอะไรเลย', _run_cases(_mut_always_none), len(CASES)),
        ('③ เทียบด้วยสตริงแทนค่า', _run_cases(_mut_string_equal), len(CASES)),
        ('④ ไม่คาดทับ กวาดเลขล้วน', _run_cases(_mut_no_masking), len(CASES)),
        ('⑤ ด่าน 18 เทียบสตริงล้วน', _run_accept_cases(_mut_accept_string_only),
         len(ACCEPT_CASES)),
        ('⑥ ด่าน 18 ไม่ตัดสินอะไร', _run_accept_cases(_mut_accept_never_red),
         len(ACCEPT_CASES)),
        ('⑦ ชั้นบังคับลืมขอบเขต', _run_enforce_cases(_mut_enforce_ignore_scope),
         len(ENFORCE_CASES)),
        ('⑧ ชั้นบังคับไม่แดงเลย', _run_enforce_cases(_mut_enforce_never_red),
         len(ENFORCE_CASES)),
    ):
        good = len(fails) > 0
        print(f'  {"✅" if good else "🔴"}  มิวแทนต์ {label} ⇒ ล้ม {len(fails)}/{total} เคส')
        for f in fails[:2]:
            print(f'         ↳ จับได้ที่: {f}')
        ok &= good

    print()
    print('  ── รายการคำสำคัญยังตรงกับด่าน 7 ไหม (อ่านไฟล์พี่น้องเป็นข้อความล้วน) ──')
    sib_ans, sib_skip = _sibling_markers()
    if sib_ans is None:
        print(f'  🔴 อ่านรายการคำสำคัญจาก {SIB} ไม่ได้')
        print('     ⇒ "เทียบไม่ได้" ไม่เท่ากับ "เทียบแล้วตรง"')
        ok = False
    else:
        good = (sib_ans == ANSWER_MARKERS)
        print(f'  {"✅" if good else "🔴"}  คำประกาศคำตอบตรงกันทั้ง {len(ANSWER_MARKERS)} คำ')
        if not good:
            print(f'         ด่าน 7  : {sib_ans}')
            print(f'         ด่าน 17 : {ANSWER_MARKERS}')
            print('         ⇒ สองด่านเข้าใจคำว่า "บรรทัดคำตอบ" ไม่ตรงกันแล้ว')
        ok &= good
        extra = set(SKIP_MARKERS) - set(sib_skip or ())
        lack = set(sib_skip or ()) - set(SKIP_MARKERS)
        good2 = not lack
        print(f'  {"✅" if good2 else "🔴"}  คำบรรทัดตัวลวงของด่าน 7 มีครบในด่าน 17'
              f' (ด่าน 17 มีเพิ่ม {sorted(extra)})')
        if lack:
            print(f'         ขาด: {sorted(lack)}')
        ok &= good2

    print()
    if not ANSWER_MARKERS or not SKIP_MARKERS:
        print('  🔴 รายการคำสำคัญว่าง ⇒ ด่านนี้จะเขียวตลอดกาลโดยไม่ตรวจอะไร')
        ok = False
    else:
        print(f'  ✅  รายการคำสำคัญไม่ว่าง (ประกาศคำตอบ {len(ANSWER_MARKERS)} คำ ·'
              f' ข้ามบรรทัด {len(SKIP_MARKERS)} คำ)')
    print()
    if not ok:
        print('🔴 SELF-TEST ไม่ผ่าน ⇒ ผลของด่านนี้กับไฟล์จริงเชื่อไม่ได้')
        sys.exit(2)
    print(f'✅ SELF-TEST ผ่านครบ {len(CASES)} + {len(ACCEPT_CASES)} + {len(ENFORCE_CASES)}'
          f' เคส + มิวแทนต์ 8 ตัว + ตัวเทียบคำสำคัญกับด่าน 7')
    return 0


def main():
    ap = argparse.ArgumentParser(
        description='ด่าน 17/18 — เฉลยข้อ fill ต้องประกาศค่าตรงคีย์ และ accept ต้องรับคีย์')
    ap.add_argument('sets_dir', nargs='?', default='data/sets')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    ap.add_argument('--min-coverage', type=float, default=DEFAULT_MIN_COVERAGE)
    ap.add_argument('--min-eligible', type=int, default=MIN_ELIGIBLE, metavar='N',
                    help=f'พื้นตัวหาร (กับดัก ⑨) — ต่ำกว่านี้ ⇒ รหัส 2 (ปริยาย {MIN_ELIGIBLE})'
                         ' · 0 = ปิด ใช้เฉพาะตอนตรวจโฟลเดอร์ย่อย')
    ap.add_argument('--max-no-value', type=int, default=MAX_NO_VALUE)
    ap.add_argument('--max-out-of-scope', type=int, default=MAX_OUT_OF_SCOPE)
    ap.add_argument('--max-no-accept', type=int, default=MAX_NO_ACCEPT)
    ap.add_argument('--max-key-not-in-accept', type=int, default=MAX_KEY_NOT_IN_ACCEPT)
    ap.add_argument('--enforce-declared', action='store_true',
                    help='บังคับว่าข้อ fill ที่เปลี่ยนรอบนี้ ต้องตรวจได้ทั้งสองฝั่ง')
    ap.add_argument('--changed-ids', default=None, metavar='ID,ID,…',
                    help='ขอบเขตของ --enforce-declared'
                         ' ⛔ ไม่ระบุธงนี้เลย = ทั้งคลัง · ระบุเป็นค่าว่าง = รอบนี้ไม่มีข้อเปลี่ยน')
    a = ap.parse_args()

    if a.version:
        print(CHECKER_VERSION)
        return 0
    if a.selftest:
        return selftest()
    if a.changed_ids is not None and not a.enforce_declared:
        print('🔴 --changed-ids ใช้ได้เฉพาะคู่กับ --enforce-declared')
        return 2

    st, red_answer, red_accept, offbeat, recs = scan(a.sets_dir)
    elig = st['eligible']
    checkable = st['hit'] + st['miss'] + st['none']
    cov = (st['hit'] + st['miss']) / elig if elig else 0.0

    print(f'ตรวจ {a.sets_dir} · ข้อ **เติมคำ (fill)** ที่มีคีย์และเฉลย {elig:,} ข้อ')
    print(f'  ด่าน 17 ตรวจได้ {st["hit"] + st["miss"]:,} / {elig:,} ({cov * 100:.1f}%)'
          f'  ·  เฉลยไม่ประกาศค่า {st["none"]:,} (เพดาน {a.max_no_value:,})'
          f'  ·  คีย์ไม่ใช่จำนวนเดี่ยว {st["out"]:,} (เพดาน {a.max_out_of_scope:,})')
    print(f'  ด่าน 18 ตรวจได้ {elig - st["no-field"]:,} / {elig:,}'
          f'  ·  ไม่มีสนาม accept {st["no-field"]:,} (เพดาน {a.max_no_accept:,})'
          f'  ·  accept ไม่รับคีย์ {st["missing"]:,} (เพดาน {a.max_key_not_in_accept:,})')
    print('  ⛔ "ตรวจไม่ได้" ไม่เท่ากับ "ตรวจแล้วผ่าน" — ทุกถังหนี้คือข้อที่ด่านมองไม่เห็น')
    print()

    if a.min_eligible and elig < a.min_eligible:
        print(f'🔴 ข้อ fill ที่ตรวจได้มีแค่ {elig:,} — ต่ำกว่าพื้น {a.min_eligible:,}')
        print('   ⇒ หนี้ที่ "ลดลง" รอบนี้อาจเป็นเพราะไฟล์ชุดหายไป ไม่ใช่เพราะมีคนแก้')
        print('   ⛔ ผลรอบนี้ใช้อ้างอิงไม่ได้ (ตั้งใจตรวจโฟลเดอร์ย่อย ⇒ --min-eligible 0)')
        return 2

    if elig and cov < a.min_coverage:
        print(f'🔴 ด่าน 17 ตรวจได้จริงแค่ {cov * 100:.1f}% ต่ำกว่าเพดานล่าง'
              f' {a.min_coverage * 100:.0f}%')
        print('   ⇒ น่าจะมีคนแก้รายการคำสำคัญจนด่านตาบอด — ไม่ใช่ว่าคลังสะอาดขึ้น')
        return 2

    rc = 0
    for label, got, cap, flag in (
        ('เฉลยไม่ประกาศค่า', st['none'], a.max_no_value, '--max-no-value'),
        ('คีย์ไม่ใช่จำนวนเดี่ยว', st['out'], a.max_out_of_scope, '--max-out-of-scope'),
        ('ไม่มีสนาม accept', st['no-field'], a.max_no_accept, '--max-no-accept'),
        ('accept ไม่รับคีย์', st['missing'], a.max_key_not_in_accept,
         '--max-key-not-in-accept'),
    ):
        if got > cap:
            print(f'🔴 หนี้ "{label}" โตขึ้น {cap:,} → {got:,} (+{got - cap:,})')
            print(f'   วิธีแก้: แก้ที่ข้อ ⛔ ไม่ใช่ขยับเพดาน ({flag})')
            rc = 1
        elif got < cap:
            print(f'  🟢 หนี้ "{label}" ลดลงจริง {cap:,} → {got:,}'
                  f' ⇒ ปรับเพดานลงเป็น {got:,} ได้แล้ว (ratchet เดินลงทางเดียว)')

    unit = [r for r in offbeat
            if r[4] is None or abs(r[4] - 1) > ROUND_TOL]
    rounded = len(offbeat) - len(unit)
    if offbeat:
        print()
        print(f'🟠 accept ที่ค่าไม่เท่าคีย์ {len(offbeat)} รายการ'
              f' — เป็นการปัดเลข {rounded} · คนละหน่วย/เครื่องหมาย {len(unit)}')
        print('   ⛔ ด่านนี้ **ไม่ตัดสิน** เพราะ "รับอีกหน่วยหนึ่ง" เป็นดุลพินิจของครู'
              ' ไม่ใช่ของเครื่อง')
        print('   แต่ต้องมองเห็น ⇒ ครูอ่านแล้วเคาะเองว่าอันไหนตั้งใจ อันไหนหลุด')
        for base, qid, key, a_, ratio in unit:
            r = f'{float(ratio):g}×' if ratio is not None else '?'
            print(f'   {qid:<44} คีย์ {key!r:<12} รับ {a_!r:<12} ({r})   [{base}]')

    if red_answer:
        print()
        print(f'🔴 เฉลยขัดกับคีย์ {len(red_answer)} ข้อ:')
        for base, qid, key, got in red_answer:
            g = ', '.join(str(x) for x in (got or [])[:4])
            print(f'   {qid:<44} คีย์ {key!r} · บรรทัดคำตอบมีแต่ {g}   [{base}]')
        print()
        print('   วิธีอ่าน: เด็กที่ตอบตามคีย์ได้คะแนน "ถูก"')
        print('             แต่เด็กที่อ่านเฉลย จะถูกสอนค่าอีกอัน')
        rc = 1

    hard = [r for r in red_accept if r[2] in ('bad-type', 'dup')]
    if hard:
        print()
        print(f'🔴 สนาม accept ผิดรูป {len(hard)} ข้อ:')
        for base, qid, av, key, detail in hard:
            why = {'bad-type': 'accept ต้องเป็นลิสต์ที่ไม่ว่าง',
                   'dup': 'accept มีค่าซ้ำ'}[av]
            print(f'   {qid:<44} {why} — {detail!r}   [{base}]')
        rc = 1

    if a.enforce_declared:
        print()
        if a.changed_ids is None:
            scope = None
            print('  ขอบเขต: ทั้งคลัง (ไม่ได้ระบุ --changed-ids)')
        else:
            scope = set(x.strip() for x in a.changed_ids.split(',') if x.strip())
            print(f'  ขอบเขต: ข้อที่เปลี่ยนรอบนี้ {len(scope)} ข้อ')
            ghosts = scope - {q for _, q, _, _ in recs}
            if ghosts:
                print(f'  🟠 มี {len(ghosts)} รหัสในขอบเขตที่ไม่ใช่ข้อ fill ที่ตรวจได้'
                      ' (ข้อปรนัย/ถูกลบ/ไม่มีคีย์) ⇒ ไม่บังคับ')
        need = enforce_verdict(recs, scope)
        if need:
            print()
            print(f'🔴 ข้อ fill ที่เปลี่ยนรอบนี้แต่ยังตรวจไม่ได้ {len(need)} ข้อ:')
            for base, qid, why in need:
                print(f'   {qid:<44} {why}   [{base}]')
            print()
            print('   วิธีแก้: เขียนค่าคำตอบเป็นตัวเลขในบรรทัด ✅ · และใส่ accept ที่รับคีย์')
            rc = 1
        else:
            print('✅ ข้อ fill ที่เปลี่ยนรอบนี้ ตรวจได้ครบทั้งสองฝั่ง')

    print()
    if rc == 0:
        print('✅ ไม่พบข้อ fill ที่เฉลยขัดกับคีย์ และไม่มีสนาม accept ผิดรูป')
    return rc


if __name__ == '__main__':
    sys.exit(main())

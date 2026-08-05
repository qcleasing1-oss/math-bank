# -*- coding: utf-8 -*-
"""ก้อน 19 · 20 ข้อ (q105-q124) · ก้อนแรกของชุดที่มีข้อชนิด fill

ระดับมาจาก grade_b19.py (คิดคะแนน rubric ก่อน ⛔ ไม่ใช่เลือกระดับแล้วย้อนหาคะแนน):
  q105 7.1+7.4   ง่าย     F1 C0 P1 T0 L0 =  2   fill
  q106 7.1       ปานกลาง  F2 C1 P2 T1 L1 =  7
  q107 7.1       ปานกลาง  F2 C1 P2 T1 L1 =  7
  q108 7.1       ยาก      F2 C1 P3 T2 L1 =  9
  q109 7.1+7.6   ยาก      F3 C2 P3 T2 L1 = 11   fill
  q110 7.1       ปานกลาง  F2 C1 P2 T1 L1 =  7
  q111 7.1+7.5   ยาก      F3 C2 P3 T2 L1 = 11
  q112 7.1       ยาก      F2 C1 P3 T2 L1 =  9   fill
  q113 7.11      ง่าย     F1 C0 P1 T0 L0 =  2   fill
  q114 7.11      ปานกลาง  F2 C1 P2 T1 L0 =  6
  q115 7.11      ปานกลาง  F2 C1 P2 T1 L0 =  6
  q116 7.11      ปานกลาง  F2 C1 P2 T1 L0 =  6
  q117 7.11+7.1  ยากมาก   F3 C2 P3 T3 L1 = 12
  q118 7.11+7.1  ปานกลาง  F2 C1 P2 T2 L0 =  7
  q119 7.11      ยาก      F2 C2 P2 T2 L0 =  8
  q120 7.3       ง่าย     F1 C0 P1 T0 L0 =  2   fill
  q121 7.3       ง่าย     F1 C0 P1 T0 L0 =  2
  q122 7.3       ง่าย     F1 C0 P1 T0 L0 =  2
  q123 7.3       ยากมาก   F3 C2 P3 T3 L1 = 12
  q124 7.3       ยาก      F2 C1 P2 T2 L1 =  8   fill
ช่องคำตอบของ 14 ข้อปรนัย: 4, 1, 4, 4, 1, 2, 2, 1, 2, 3, 4, 4, 4, 1
  (ทุกช่องถูกบังคับด้วยกฎเรียงตัวเลือกจากน้อยไปมาก ⛔ ไม่ได้เลือกเอง)
  ⇒ สะสมทั้งชุด 29 / 31 / 30 / 28 จากข้อปรนัย 118 ข้อ
sympy: verify_b19.py ผ่านทุกบรรทัด (124 บรรทัด) ✅
แม่พิมพ์: molds.py ❌ 0 คู่ · แผนก้อน 19 ไม่เพิ่มคู่ WATCH ใหม่แม้แต่คู่เดียว
ด่าน ④: crossnew_b19.py รายงานครบ 190 คู่ · ตก 0 คู่

🔑 ด่านกันของลอย: ไฟล์นี้เทียบ stem/choices/correct/accept ของทุกข้อกับ stems_b19.py
   ซึ่งเป็นฉบับที่ผ่าน sympy และผ่านด่านชั้นแรกมาแล้ว ⇒ ถ้าผู้แต่งเผลอแก้ตัวเลขในเฉลย
   ไฟล์นี้จะหยุดทันที ⛔ ไม่ปล่อยให้ของสองฝั่งลอยจากกัน
"""
import json, io, os, sys, collections

sys.path.insert(0, '/home/claude/k2')
from stems_b19 import STEMS

OUT = '/home/claude/k2/out'
os.makedirs(OUT, exist_ok=True)
SRC = 'แต่งใหม่ v2 · แข่งขัน · 2569'
SET = 'gen-chap-07-trigonometry'
Q = []
SPEC = {s[0]: s for s in STEMS}


def _guard(n, st, level, stem, kind):
    assert n in SPEC, 'ข้อ %d ไม่มีในสเปก' % n
    s = SPEC[n]
    assert s[1] == st, 'q%03d subTopics ไม่ตรงสเปก: %r vs %r' % (n, st, s[1])
    assert s[2] == level, 'q%03d ระดับไม่ตรงสเปก: %r vs %r' % (n, level, s[2])
    assert s[3] == kind, 'q%03d ชนิดไม่ตรงสเปก: %r vs %r' % (n, kind, s[3])
    assert s[4] == stem, 'q%03d ตัวโจทย์ไม่ตรงสเปกทุกตัวอักษร' % n
    return s


def add(n, st, level, stem, choices, correct, expl, notes):
    s = _guard(n, st, level, stem, 'mc')
    assert s[5] == choices, 'q%03d ตัวเลือกไม่ตรงสเปก' % n
    assert s[6] == correct, 'q%03d correct ไม่ตรงสเปก: %r vs %r' % (n, correct, s[6])
    Q.append(collections.OrderedDict([
        ('id', '%s-q%03d' % (SET, n)), ('setId', SET), ('questionNumber', n),
        ('topics', ['7']), ('subTopics', st), ('difficulty', level),
        ('type', 'mc'), ('question', stem), ('choices', choices),
        ('hasImage', False), ('sourceTag', SRC), ('correct', correct),
        ('explanation', expl), ('notes', notes),
    ]))
    print('q%03d ok (mc · ช่อง %d)' % (n, correct + 1))


def add_fill(n, st, level, stem, correct, accept, expl, notes):
    s = _guard(n, st, level, stem, 'fill')
    assert s[6] == correct, 'q%03d correct ไม่ตรงสเปก: %r vs %r' % (n, correct, s[6])
    assert s[7] == accept, 'q%03d accept ไม่ตรงสเปก' % n
    assert isinstance(correct, str), 'q%03d ข้อ fill ต้องมี correct เป็นสตริง' % n
    Q.append(collections.OrderedDict([
        ('id', '%s-q%03d' % (SET, n)), ('setId', SET), ('questionNumber', n),
        ('topics', ['7']), ('subTopics', st), ('difficulty', level),
        ('type', 'fill'), ('question', stem),
        ('hasImage', False), ('sourceTag', SRC), ('correct', correct),
        ('accept', accept), ('explanation', expl), ('notes', notes),
    ]))
    print('q%03d ok (fill · คำตอบ %s)' % (n, correct))


# เนื้อข้อแยกเป็นไฟล์ละข้อใน parts_b19/ เพื่อเลี่ยงการเขียนไฟล์ยาวรวดเดียว (กันงานพัง)
for _n in range(105, 125):
    _p = '/home/claude/k2/parts_b19/q%03d.py' % _n
    exec(compile(io.open(_p, encoding='utf-8').read(), _p, 'exec'), globals())

assert len(Q) == 20, 'ได้ %d ข้อ ต้องได้ 20' % len(Q)
data = collections.OrderedDict([('setId', SET), ('questions', Q)])
FN = 'k2-ก้อน19-20ข้อ-7.1-7.11-7.3.json'
path = os.path.join(OUT, FN)
txt = json.dumps(data, ensure_ascii=False, indent=2)
io.open(path, 'w', encoding='utf-8', newline='\n').write(txt)
print('เขียน', os.path.basename(path), '·', len(txt.encode()), 'B ·', len(Q), 'ข้อ')

# -*- coding: utf-8 -*-
"""ก้อน 18 · ก้อนแรกที่ขยายเป็น 10 ข้อ ตามคำสั่ง ② ของจดหมาย E→MB #20 · (q095-q104)

ระดับมาจาก grade_b18.py (คิดคะแนน rubric ก่อน ⛔ ไม่ใช่เลือกระดับแล้วย้อนหาคะแนน):
  q095 7.11        ง่าย     F1 C0 P1 T0 L0 = 2
  q096 7.4         ง่าย     F1 C0 P1 T0 L0 = 2
  q097 7.5+7.2     ปานกลาง  F2 C1 P2 T1 L0 = 6
  q098 7.10+7.1    ปานกลาง  F2 C1 P2 T1 L1 = 7
  q099 7.6+7.2     ปานกลาง  F2 C1 P2 T1 L0 = 6
  q100 7.4         ปานกลาง  F2 C1 P2 T1 L0 = 6
  q101 7.1+7.2     ปานกลาง  F2 C1 P2 T1 L0 = 6
  q102 7.7         ปานกลาง  F2 C1 P2 T1 L0 = 6
  q103 7.7+7.5     ยาก      F3 C2 P2 T2 L0 = 9
  q104 7.10+7.9    ยากมาก   F3 C2 P3 T2 L2 = 12
ช่องคำตอบ: 3, 1, 2, 2, 3, 2, 1, 3, 1, 4   (แก้ 2026-08-05 · บรรทัดเดิมพิมพ์ผิด 3 ตัว)
  (ทุกช่องถูกบังคับด้วยกฎเรียงตัวเลือก ⛔ ไม่ได้เลือกเอง)
sympy: verify_b18.py ผ่านทุกบรรทัด ✅
แม่พิมพ์: molds.py ❌ 0 คู่ · กวาดชนครบ 8 รอบ (collide_b18a..h)
"""
import json, io, os, collections

OUT = '/home/claude/k2/out'
os.makedirs(OUT, exist_ok=True)
SRC = 'แต่งใหม่ v2 · แข่งขัน · 2569'
SET = 'gen-chap-07-trigonometry'
Q = []


def add(n, st, level, stem, choices, correct, expl, notes):
    Q.append(collections.OrderedDict([
        ('id', '%s-q%03d' % (SET, n)), ('setId', SET), ('questionNumber', n),
        ('topics', ['7']), ('subTopics', st), ('difficulty', level),
        ('type', 'mc'), ('question', stem), ('choices', choices),
        ('hasImage', False), ('sourceTag', SRC), ('correct', correct),
        ('explanation', expl), ('notes', notes),
    ]))
    print('q%03d ok' % n)


# เนื้อข้อแยกเป็นไฟล์ละข้อใน parts_b18/ เพื่อเลี่ยงการเขียนไฟล์ยาวรวดเดียว (กันงานพัง)
for _n in range(95, 105):
    _p = '/home/claude/k2/parts_b18/q%03d.py' % _n
    exec(compile(io.open(_p, encoding='utf-8').read(), _p, 'exec'), globals())

data = collections.OrderedDict([('setId', SET), ('questions', Q)])
FN = 'k2-ก้อน18-10ข้อ-7.11-7.4-7.5-7.10-7.6-7.1-7.7-7.9.json'
path = os.path.join(OUT, FN)
txt = json.dumps(data, ensure_ascii=False, indent=2)
io.open(path, 'w', encoding='utf-8', newline='\n').write(txt)
print('เขียน', os.path.basename(path), '·', len(txt.encode()), 'B ·', len(Q), 'ข้อ')

# -*- coding: utf-8 -*-
"""ก้อน 13 · 7.9 กฎของโคไซน์ (สามด้าน · จุดกึ่งกลาง · ลำดับเรขาคณิต)
   + 7.1 นิพจน์มุมพิเศษ + 7.10 เสาธงในภาพสามมิติ · 5 ข้อ (q070-q074)

ระดับมาจาก grade_b13.py (คิดคะแนน rubric ก่อน ⛔ ไม่ใช่เลือกระดับแล้วย้อนหาคะแนน):
  q070 ง่าย 2 · q071 ง่าย 2 · q072 ปานกลาง 4 · q073 ยาก 9 · q074 ยากมาก 12
  หลังก้อน 13 : 74 ข้อ — ง่าย 24.3 · ปานกลาง 33.8 · ยาก 24.3 · ยากมาก 17.6
  (ห่างเป้าสุด 2.6 จุด ⇒ อยู่ในกรอบ ±3 ทั้งสี่แถบ ✅)
ช่องคำตอบ: 1, 4, 1, 3, 2 (สะสมเป็น 18/19/19/18 จาก 74 ข้อ — สเปรดสูงสุด 1 ช่อง)
  บันทึกการตัดสิน: โน้ตก้อน 12 สั่งให้เอียงมาช่อง 1 (ตอนนั้นช่อง 1 ต่ำสุดที่ 16)
  ถ้าเอา q073 ไปช่อง 1 ด้วยจะได้ 19/19/18/18 ซึ่งสเปรดเท่ากันแต่กระจุก 3 ใน 5 ข้อ
  ที่ช่องเดียว ⇒ เลือกช่อง 3 ให้ในก้อนกระจายดีกว่า โดยสเปรดสะสมยังเท่าเดิม
sympy: verify_b13.py ผ่านทุกจุด (ทุกข้อมีเส้นทางที่สองที่เป็นอิสระจริง
  + ตัวลวงทุกตัวคำนวณจากเส้นทางพลาดที่ตั้งชื่อไว้ + มี guard กันตัวลวงเสื่อม)
แม่พิมพ์: molds.py ❌ 0 คู่ · ไม่มีคู่ WATCH ใหม่ (WATCH-A คง 3 · WATCH-B คง 8)
โพรบชน: 14 รอบ (collide_b13 ... b13p) — ฆ่าแบบร่างไป 26 แม่พิมพ์
  ⚠️ ในนั้นมีการชนกับ "ข้อของเราเอง" 5 ครั้ง (q047 · q053 · q050 · q034)
  ⇒ พื้นที่แม่พิมพ์ของบท 7 เริ่มตึงจริง — บันทึกไว้ใน CHANGELOG เพื่อรายงานครู
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


# เนื้อข้อแยกเป็นไฟล์ละข้อใน parts_b13/ เพื่อเลี่ยงการเขียนไฟล์ยาวรวดเดียว (กันงานพัง)
for _n in range(70, 75):
    _p = '/home/claude/k2/parts_b13/q%03d.py' % _n
    exec(compile(io.open(_p, encoding='utf-8').read(), _p, 'exec'), globals())

data = collections.OrderedDict([('setId', SET), ('questions', Q)])
FN = 'k2-ก้อน13-5ข้อ-7.9-7.1-7.10-สามด้าน-มุมพิเศษ-จุดกึ่งกลาง-เสาธงสามมิติ-ลำดับเรขาคณิต.json'
path = os.path.join(OUT, FN)
txt = json.dumps(data, ensure_ascii=False, indent=2)
io.open(path, 'w', encoding='utf-8', newline='\n').write(txt)
print('เขียน', os.path.basename(path), '·', len(txt.encode()), 'B ·', len(Q), 'ข้อ')

# -*- coding: utf-8 -*-
"""ก้อน 15 · 7.6 ย้อนมุมสองเท่า + 7.8 ผลบวกค่าหลักของ arc + 7.5×7.1 ถอดมุมจาก tan ผลบวก
   + 7.4×7.7 เอกลักษณ์คอนจูเกต sec-tan + 7.9×7.11 สามเหลี่ยมแนบวงกลม→ความยาวส่วนโค้ง
   · 5 ข้อ (q080-q084)

ระดับมาจาก grade_b15.py (คิดคะแนน rubric ก่อน ⛔ ไม่ใช่เลือกระดับแล้วย้อนหาคะแนน):
  q080 ง่าย 2 · q081 ง่าย 2 · q082 ปานกลาง 5 · q083 ยาก 8 · q084 ยากมาก 12 (T=3)
  หลังก้อน 15 : 84 ข้อ — ง่าย 23.8 · ปานกลาง 34.5 · ยาก 23.8 · ยากมาก 17.9
  (ห่างเป้าสุด 2.9 จุด ⇒ อยู่ในกรอบ ±3 ทั้งสี่แถบ ✅)
  📌 ทำตามคำเตือนท้าย build_b14.py : ก้อนนี้มี "ง่ายจริง" 2 ข้อ (q080 q081) ดึงแถบ ง่าย กลับขึ้น
  📌 และมี "ยากมาก" 1 ข้อ (q084) ตามคำสั่ง ④ ของจดหมาย E→MB #19
     ("ยากมาก" เป็นผลผลิตของวิธีแต่ง ⛔ ไม่ใช่คุณสมบัติของบท)
  ⭐ บันทึกความซื่อสัตย์ : q084 ฉบับแรกให้คะแนนตรงไปตรงมาแล้วได้ 10 ⇒ ยาก
     ⛔ ไม่ดัน L หรือ T ขึ้นเพื่อให้เข้าแผน — แต่ **ออกแบบโจทย์ใหม่ให้ยากขึ้นจริง**
     โดยซ่อนมุม A ไว้หลังพื้นที่ ⇒ เกิดสองกิ่ง (π/3 กับ 2π/3) ที่ต้องตัดด้วยเงื่อนไข BC < AB
ช่องคำตอบ: 1, 3, 2, 4, 4 (สะสมเป็น 21/21/21/21 จาก 84 ข้อ — สเปรด 0 ช่อง ✅)
sympy: verify_b15.py ผ่าน 52 จุด · ล้ม 0 จุด
  (ทุกข้อมีเส้นทางที่สองที่เป็นอิสระจริง + ตัวลวงทุกตัวคำนวณจากเส้นทางพลาดที่ตั้งชื่อไว้)
แม่พิมพ์: molds.py ❌ 0 คู่ · โพรบชน 5 รอบ (collide_b15 … b15e)
  ⚠️ รอบ b15d ฆ่าแบบร่าง q084 เดิม (มุมเงยสองจุดสังเกต — แม่พิมพ์อิ่มตัวแล้ว 8 ข้อ)
  เพื่อนบ้านใกล้สุดของฉบับใหม่คือ chap-07-trigonometry-q122 และ q069 ของเราเอง — ทั้งคู่ไม่ชน
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


# เนื้อข้อแยกเป็นไฟล์ละข้อใน parts_b15/ เพื่อเลี่ยงการเขียนไฟล์ยาวรวดเดียว (กันงานพัง)
for _n in range(80, 85):
    _p = '/home/claude/k2/parts_b15/q%03d.py' % _n
    exec(compile(io.open(_p, encoding='utf-8').read(), _p, 'exec'), globals())

data = collections.OrderedDict([('setId', SET), ('questions', Q)])
FN = 'k2-ก้อน15-5ข้อ-7.6-7.8-7.5-7.4-7.9-7.11-ย้อนมุมสองเท่า-ผลบวกอาร์ค-คอนจูเกต-ส่วนโค้ง.json'
path = os.path.join(OUT, FN)
txt = json.dumps(data, ensure_ascii=False, indent=2)
io.open(path, 'w', encoding='utf-8', newline='\n').write(txt)
print('เขียน', os.path.basename(path), '·', len(txt.encode()), 'B ·', len(Q), 'ข้อ')

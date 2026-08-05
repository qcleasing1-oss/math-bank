# -*- coding: utf-8 -*-
"""ก้อน 17 · 7.6 ยุบ cos²-sin² · 7.4 นิพจน์ตรรกยะตรีโกณ
   + 7.11×7.1 ถังทรงกระบอกนอนราบ (เซกเมนต์วงกลม)
   + 7.10×7.9 เงาเสาทอดขึ้นพื้นลาด
   + 7.11×7.1 ม้วนเซกเตอร์เป็นกรวย
   · 5 ข้อ (q090-q094)

ระดับมาจาก grade_b17.py (คิดคะแนน rubric ก่อน ⛔ ไม่ใช่เลือกระดับแล้วย้อนหาคะแนน):
  q090 ง่าย 2 · q091 ง่าย 2 · q092 ยาก 11 · q093 ยาก 9 · q094 ยากมาก 12 (F=3,T=2)
  หลังก้อน 17 : 94 ข้อ — ง่าย 24.5 · ปานกลาง 33.0 · ยาก 24.5 · ยากมาก 18.1
  ⚠️ "ยากมาก" หลุดกรอบ +3.1 pp ⇒ ส่งเรื่องให้ครูเคาะใน CHANGELOG (ไม่ตัดข้อทิ้งเอง)
  📌 มี "ยากมาก" 1 ข้อ (q094) ตามคำสั่ง ④ ของจดหมาย E→MB #19
  ⭐ บันทึกความซื่อสัตย์ 3 จุด :
     q091 คง P=1 ตามบรรทัดฐาน q087 (บวกกับลบเป็นก้าวคู่ขนานชนิดเดียวกัน ไม่ใช่สองเวที)
     q092 ได้ 11 ไม่ถึง 12 ⇒ ปล่อยเป็น "ยาก" ⛔ ไม่ดันมิติใดให้ถึงยากมาก
     q093 คง L=1 ตามบรรทัดฐาน q077/q089 (ระนาบเดียว ⇒ 1 · สามมิติเท่านั้นถึงให้ 2)
  ⭐ ก้อนแรกที่ใช้ "แต่งขนาน" ตามมติครู (q091-q094 แต่งพร้อมกัน 4 ตัวช่วย · q090 แต่งเอง)
     ⇒ ด่านทั้งสาม (check_k2 · daan7 · audit44) สำคัญกว่าปกติ เพราะสำนวนมาจากหลายมือ
ช่องคำตอบ: 3, 3, 2, 3, 1 (ทุกช่องถูกบังคับด้วยกฎเรียงตัวเลือก ⛔ ไม่ได้เลือกเอง)
  สะสมเป็น 22/25/26/21 จาก 94 ข้อ
sympy: verify_b17.py ผ่านทุกบรรทัด ✅
  (q091 มีบรรทัดพิสูจน์ว่า "ตัดพจน์ที่สองทิ้งคู่กัน" ให้ cot ไม่ใช่ 1 ⇒ ตัวลวงมีที่มาจริง)
แม่พิมพ์: molds.py ❌ 0 คู่ ทั้งที่ 89 และ 94 ข้อ · WATCH เท่าเดิมทุกคู่ (ไม่มีญาติใหม่)
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


# เนื้อข้อแยกเป็นไฟล์ละข้อใน parts_b17/ เพื่อเลี่ยงการเขียนไฟล์ยาวรวดเดียว (กันงานพัง)
for _n in range(90, 95):
    _p = '/home/claude/k2/parts_b17/q%03d.py' % _n
    exec(compile(io.open(_p, encoding='utf-8').read(), _p, 'exec'), globals())

data = collections.OrderedDict([('setId', SET), ('questions', Q)])
FN = 'k2-ก้อน17-5ข้อ-7.6-7.4-7.11-7.1-7.10-7.9-ถังนอนราบ-เงาบนลาด-ม้วนกรวย.json'
path = os.path.join(OUT, FN)
txt = json.dumps(data, ensure_ascii=False, indent=2)
io.open(path, 'w', encoding='utf-8', newline='\n').write(txt)
print('เขียน', os.path.basename(path), '·', len(txt.encode()), 'B ·', len(Q), 'ข้อ')

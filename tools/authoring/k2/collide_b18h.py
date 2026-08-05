# -*- coding: utf-8 -*-
"""กวาดชนก้อน 18 · รอบ 8 — ปิดจุดบอด "คลาสอักขระ" ของโพรบ U1b

🔴 จุดบอดชั้นที่สองของโพรบตัวเอง (ต่อจากบทเรียน "ทิศเดียว" ของรอบ 7)
   U1b รอบ 7 เขียนว่า (\\sin|\\cos|...)\\s*\\?[a-zA-Z\\]{1,8} ... ⇒ ได้ 0 ข้อ
   แต่ของจริงมี : chap-07-trigonometry-q137
     "ถ้า $\\tan 20^\\circ = M$ แล้ว จงหาค่าของ $\\sin 70^\\circ \\cot 200^\\circ \\sec 290^\\circ$"
   คือ **ผลคูณของฟังก์ชันตรีโกณสามตัวติดกัน** เต็ม ๆ — แต่หลุด เพราะอาร์กิวเมนต์เป็น "ตัวเลข"
   ไม่ใช่ตัวอักษร ([a-zA-Z\\] ไม่รับ 7,0)
   ⭐ กฎใหม่ข้อที่สองของโพรบ : คลาสอักขระของอาร์กิวเมนต์ต้องรับทั้ง
      ตัวอักษร · ตัวเลข · \\dfrac · ^\\circ · วงเล็บ เสมอ ⇒ ใช้ [^\\\\$]{0,14} แทน

รอบนี้ยิงเพื่อตัดสินว่า U1 (ง่าย 7.4 · รูปอย่างง่ายของ sin t sec t cot t) รอดหรือตาย
  W1a ผลคูณตรีโกณสามตัวติดกัน — อาร์กิวเมนต์รูปแบบใดก็ได้
  W1b คำสั่ง "รูปอย่างง่าย/เท่ากับข้อใด" ที่ตัวโจทย์ **ไม่มีเงื่อนไขนำหน้า** (ไม่มี กำหนดให้/ถ้า)
      ⇒ นับเฉพาะข้อ "ยุบนิพจน์เปล่า" ซึ่งเป็นแม่พิมพ์เดียวกับ U1 จริง ๆ
  W1c เฉลยที่เดินทาง "แปลงทุกตัวเป็น sin/cos แล้วตัดกัน" จนเหลือค่าคงที่ 1
"""
import io, json, glob, re

items = []
for p in sorted(glob.glob('/tmp/mb27/data/sets/*.json') +
                glob.glob('/home/claude/k1/out/*.json') +
                glob.glob('/home/claude/k2/out/*.json')):
    d = json.load(io.open(p, encoding='utf-8'))
    for q in d.get('questions', []):
        q['_src'] = p.split('/')[-1].replace('.json', '')
        items.append(q)


def txt(q):
    parts = [q.get('question') or '']
    parts += [str(c) for c in (q.get('choices') or [])]
    ex = q.get('explanation') or ''
    parts += ex if isinstance(ex, list) else [str(ex)]
    return '\n'.join(parts)


def scan(label, pattern, qonly=False, show=8, flags=0):
    rx = re.compile(pattern, flags)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-32s %-8s %-12s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:110]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

FN = r'\\(?:sin|cos|tan|cot|sec|csc)'
ARG = r'[^\\$]{0,16}'

scan('W1a  ผลคูณตรีโกณสามตัวติดกัน (อาร์กิวเมนต์รูปแบบใดก็ได้)',
     FN + ARG + FN + ARG + FN, qonly=True, show=14)
scan('W1b  โจทย์ยุบนิพจน์เปล่า (ไม่มี กำหนดให้/ถ้า/เมื่อ นำหน้า)',
     r'^(?!.*(กำหนดให้|ถ้า|เมื่อ|โดยที่))[\s\S]{0,200}(รูปอย่างง่าย|ตรงกับข้อใด|เท่ากับข้อใด)',
     qonly=True, show=20)
scan('W1c  เฉลยยุบเหลือค่าคงที่ 1 จากผลคูณตรีโกณ',
     r'(รูปอย่างง่าย|ยุบ|ตัดกัน)[\s\S]{0,120}=\s*1\s*$', show=12, flags=re.M)

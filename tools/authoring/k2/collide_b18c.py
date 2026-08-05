# -*- coding: utf-8 -*-
"""กวาดชนก้อน 18 · รอบ 3 — ปิดสามช่องที่ยังว่าง (ง่าย 1 · ปานกลาง 2)

⛔ ที่ตายเพิ่มในรอบ 2
   Q2  (ง่าย 7.8 · tan(arccos 3/5)) — ชน chap-07-trigonometry-q77 เต็มสามส่วน
       (theta = sin(arctan 120/119) · ง่าย · 7.8/7.1) ⇒ G · A · M ตรงกันหมด
       ⭐ ข้อสรุปสำคัญ : 7.8 "บาง" เฉพาะในชุดของเรา (6 ข้อ) แต่ **คลังเดิมอัดแน่น**
          ⇒ ตัวเลขหัวข้อย่อยของเราไม่ใช่ตัวชี้ว่ามีที่ว่าง ต้องดูคลังเดิมเสมอ
   Q5  regex "จั่ว" ให้ผลลวง — ไปแมตช์ "สามเหลี่ยมหน้าจั่ว" (isosceles) 25 ข้อ
       ⇒ ต้องใช้ (?<!หน้า)จั่ว และแยกคำว่า หลังคา ออกมากวาดเดี่ยว

✅ ที่ผ่านแล้วในรอบ 1-2 (7 ข้อ)
   q095 ง่าย 7.7 · tan x = -1 ⇒ คำตอบมากที่สุด        (P1a=0 · P1b=0)
   q097 ปกลาง 7.5 · สองอัตราส่วน+สองจตุภาค ⇒ sin(A+B) (P3b=0 · P3a 2 ข้อคนละแม่พิมพ์)
   q100 ปกลาง 7.4 · sin/(1-cot) + cos/(1-tan)         (P6c=0 · P6e 1 ข้อเป็นผลคูณ ไม่ใช่ผลบวก)
   q101 ปกลาง 7.1 · 3sin=2cos + จตุภาค 3 ⇒ csc        (P7c=0 · P7d 1 ข้อเป็น 2sin^2=3cos)
   q102 ปกลาง 7.7 · 2cos^2x-3cosx+1=0 ⇒ นับคำตอบ      (P8c=0 · P8d=0)
   q103 ยาก  7.7 · sin3x = cos2x ⇒ คำตอบบวกน้อยสุด    (P9a=0 · P9c=0)
   q104 ยากมาก 7.10 · บอลลูนเชือกสองเส้น (สามมิติ)     (P10d=0 · P10f=0)

ตัวแทนที่ยิงรอบนี้ (ต้องได้ ง่าย 1 · ปานกลาง 2)
  R1 ง่าย  7.8  · โดเมนของ y = arcsin(3x - 1)
  R2 ปกลาง 7.10 · หลังคาทรงจั่ว (ไม่มีผู้สังเกต ไม่มีมุมเงย) ⇒ ความยาวจันทัน
  R3 ปกลาง 7.6  · sin2t/(1 + cos2t) เมื่อให้ tan t ⇒ ยุบเป็น tan t
  R4 ปกลาง 7.11 · (สำรอง) ใบพัด/เข็มนาฬิกากวาดพื้นที่
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

# ── R1 · โดเมนของ arcsin ที่อาร์กิวเมนต์เป็นเชิงเส้น ────────────────────────
scan('R1a  คำถามถามโดเมนของฟังก์ชันผกผันตรีโกณ',
     r'โดเมน[\s\S]{0,120}(arcsin|arccos|arctan|\\sin\^\{-1\}|\\cos\^\{-1\})|'
     r'(arcsin|arccos|arctan)[\s\S]{0,120}โดเมน', qonly=True)
scan('R1b  คำถามมี arcsin/arccos ของนิพจน์เชิงเส้น ax+b',
     r'(arcsin|arccos)\s*\\?(left)?\(?\s*\{?\s*\d?\s*x\s*[-+]\s*\d', qonly=True)
scan('R1c  คำถามถามช่วงของ x ที่ทำให้หาค่าได้', r'หาค่าได้|นิยามได้|มีความหมาย', qonly=True, show=10)

# ── R2 · หลังคาทรงจั่ว (แก้ false positive หน้าจั่ว) ───────────────────────
scan('R2a  คำว่า หลังคา (คำเดี่ยว)', r'หลังคา', show=12)
scan('R2b  คำว่า จั่ว ที่ไม่ใช่ สามเหลี่ยมหน้าจั่ว', r'(?<!หน้า)จั่ว')
scan('R2c  คำว่า จันทัน / อกไก่ / สันหลังคา', r'จันทัน|อกไก่|สันหลังคา')

# ── R3 · sin2t/(1+cos2t) ⇒ tan t ───────────────────────────────────────────
scan('R3a  นิพจน์ sin2x ส่วน 1+cos2x (ทุกแบบเขียน)',
     r'\\d?frac\{\\sin\s*2[\s\S]{0,12}\}\{\s*1\s*\+\s*\\cos\s*2|'
     r'\\sin\s*2\s*\\?[a-z]+\s*/\s*\(?\s*1\s*\+\s*\\cos\s*2')
scan('R3b  คำถามมี 1 + cos 2 อะไรสักอย่าง', r'1\s*\+\s*\\cos\s*2', qonly=True, show=10)
scan('R3c  คำถามมี 1 - cos 2 อะไรสักอย่าง', r'1\s*-\s*\\cos\s*2', qonly=True, show=10)

# ── R4 · (สำรอง) ใบพัด / พื้นที่ที่เข็มกวาด ────────────────────────────────
scan('R4a  คำว่า ใบพัด / กังหัน / พัดลม', r'ใบพัด|กังหัน|พัดลม')
scan('R4b  คำว่า กวาดพื้นที่ / พื้นที่ที่เข็มกวาด', r'กวาด')

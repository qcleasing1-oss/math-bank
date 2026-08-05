# -*- coding: utf-8 -*-
"""กวาดชนก้อน 18 · รอบ 6 (รอบปิด) — ยืนยันสองข้อสุดท้ายก่อนลง PLAN

⛔ ที่ตายในรอบ 5
   S5 (ง่าย 7.1 · ให้ tan มุมแหลม ⇒ sin + cos) — ชน gen-chap-07-trigonometry-q011 **ของเราเอง**
      q011 : "A เป็นมุมแหลม tan A = 5/12 ค่าของ sin A + cos A" ⇒ G · A · M ตรงกันทั้งสามส่วน
      (ทะเบียน q011 = G-ANGLE-ACUTE-RATIO / A-EXPR-VALUE / M-REF-TRIANGLE)
   S4 (ง่าย 7.9 · สองด้าน+มุมระหว่าง ⇒ พื้นที่สามเหลี่ยม) — ชน q061 ของเราเอง
      q061 = G-TRI-SAS-OBTUSE / A-AREA / M-AREA-HALF-AB-SIN ⇒ A ตรง · M ตรง (⚠️ WATCH-A ทันที)
      + คลังเดิมมี 19 ข้อที่เฉลยใช้สูตร 1/2 ab sin C

✅ ทางออกที่เจอ : ใช้ "ช่องว่างในตาราง (สิ่งที่ให้ × สิ่งที่ถาม)" ของหัวข้อ 7.11
   ของเดิมในชุดเรา  q030 ให้ (r, มุม) ⇒ พื้นที่ · q031 ให้ (r, พื้นที่) ⇒ เส้นรอบรูป
                    q032 วงซ้อน ⇒ ส่วนโค้ง · q033 ลูกตุ้ม ⇒ ส่วนโค้ง
                    q034 ให้ (เส้นรอบรูป, พื้นที่) ⇒ ผลบวกพารามิเตอร์ · q060 ให้ (r, ส่วนโค้ง) ⇒ มุม
   ⇒ **ช่องที่ยังว่างจริงคือ "ให้ (ส่วนโค้ง, มุม) ⇒ หารัศมี"** — ไม่มีข้อไหนถามรัศมีเลยทั้งชุด

ตัวแทนที่ยิงรอบนี้ (รอบสุดท้าย)
  T1 ง่าย   7.11 · ให้ความยาวส่วนโค้ง + มุมที่จุดศูนย์กลางเป็นเรเดียน ⇒ หารัศมี
  T2 ปกลาง 7.10 · หลังคาทรงจั่วของโรงเก็บของ ⇒ พื้นที่แผ่นมุงสองผืน
     (⛔ เปลี่ยนจาก "พื้นที่หน้าจั่ว" เพราะ A-AREA + M-AREA-HALF-AB-SIN ชน q061)
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

# ── T1 · ถามรัศมี โดยให้ส่วนโค้งกับมุม ─────────────────────────────────────
scan('T1a  คำถามถามหารัศมี (ทุกบริบท)',
     r'รัศมี[\s\S]{0,30}(ยาวเท่าใด|เท่ากับข้อใด|ยาวกี่|เป็นเท่าใด)|หารัศมี|รัศมีของวงกลม[\s\S]{0,20}(คือ|เท่ากับ)',
     qonly=True, show=12)
scan('T1b  คำถามมีทั้ง ส่วนโค้ง และ เรเดียน', r'ส่วนโค้ง[\s\S]{0,200}เรเดียน|เรเดียน[\s\S]{0,200}ส่วนโค้ง',
     qonly=True, show=12)

# ── T2 · หลังคาทรงจั่ว ⇒ พื้นที่แผ่นมุง ────────────────────────────────────
scan('T2a  คำว่า แผ่นมุง / กระเบื้อง / สังกะสี / เมทัลชีท', r'แผ่นมุง|กระเบื้อง|สังกะสี|เมทัลชีท|มุงหลังคา')
scan('T2b  คำว่า โรงเก็บของ / โรงเรือน / โกดัง / เพิง', r'โรงเก็บของ|โรงเรือน|โกดัง|เพิง')
scan('T2c  คำถามถามพื้นที่ผิว/พื้นที่ที่ต้องใช้วัสดุ',
     r'พื้นที่[\s\S]{0,30}(ผิว|ที่ต้องใช้|ทั้งหมดของ)', qonly=True, show=12)

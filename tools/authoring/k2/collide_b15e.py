# -*- coding: utf-8 -*-
"""กวาดชนก้อน 15 · รอบ 5 — เฉพาะ q084 ฉบับแก้ (ไม่กรองบท)

เหตุ: q084 ฉบับแรก (ให้ b c และมุม A = 60 องศา ⇒ ส่วนโค้ง) ให้คะแนน rubric ตรง ๆ ได้
      F3 C2 P2 T2 L1 = 10 ⇒ "ยาก" ไม่ถึง "ยากมาก" ⛔ ไม่ยอมปั๊ม L หรือ T ให้ตรงแผน
      ⇒ ออกแบบใหม่ให้ "ยากขึ้นจริง" : ไม่ให้มุม A มาตรง ๆ แต่ให้ "พื้นที่" แทน
         ⇒ sin A = sqrt3/2 ⇒ A มีสองค่าในสามเหลี่ยม (60 กับ 120 องศา) ⇒ แตกกิ่งจริง
         ⇒ ต้องคำนวณ BC ทั้งสองกิ่งก่อน จึงใช้เงื่อนไข BC < AB คัดกิ่งได้
รอบนี้จึงต้องกวาดแม่พิมพ์ "ให้พื้นที่แล้วถอยกลับหามุม (กรณีกำกวม)" ใหม่ทั้งหมด
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


def scan(label, pattern, qonly=False, show=12, flags=0):
    rx = re.compile(pattern, flags)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-32s %-8s %-12s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:104]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

scan('N1 · โจทย์ให้ "พื้นที่ของรูปสามเหลี่ยม" เป็นข้อมูลตั้งต้น (ไม่ใช่สิ่งที่ถาม)',
     r'พื้นที่(ของรูป|รูป)?สามเหลี่ยม[^?]{0,40}(เท่ากับ|เป็น|คือ)\s*\$', qonly=True)

scan('N2 · พื้นที่สามเหลี่ยม + ส่วนโค้ง/เซกเตอร์ ในข้อเดียวกัน',
     r'พื้นที่.{0,700}(ความยาวส่วนโค้ง|เซกเตอร์)|(ความยาวส่วนโค้ง|เซกเตอร์).{0,700}พื้นที่',
     flags=re.S)

scan('N3 · กรณีกำกวมของมุม (sin ให้สองมุม) แล้วมีเงื่อนไขคัดกิ่ง',
     r'(มุมแหลม|มุมป้าน).{0,300}(สองค่า|สองกรณี|สองมุม)|'
     r'(สองค่า|สองกรณี|สองมุม).{0,300}(มุมแหลม|มุมป้าน)', flags=re.S)

scan('N4 · โจทย์เอ่ย "แนบในวงกลม / วงกลมล้อมรอบ" ทุกที่',
     r'แนบในวงกลม|วงกลมล้อมรอบ|บรรจุในวงกลม|รัศมีของวงกลมที่ล้อมรอบ|วงกลมแนบนอก')

scan('N5 · "ส่วนโค้ง BC ที่ไม่มีจุด A" หรือถ้อยคำระบุส่วนโค้งด้วยจุดยอด',
     r'ส่วนโค้ง\s*\$?[A-Z]\$?\s*\$?[A-Z]\$?|ส่วนโค้งที่ไม่มีจุด|ส่วนโค้งเล็ก|ส่วนโค้งใหญ่')

scan('N6 · เงื่อนไขเปรียบเทียบด้าน (BC < AB แบบตัวอักษรสามตัว) ในคำถาม',
     r'\$?[A-Z]{2}\$?\s*<\s*\$?[A-Z]{2}|[A-Z]{2}\s*มีความยาวน้อยกว่า', qonly=True)

scan('N7 · ให้สองด้าน + พื้นที่ แล้วถอยกลับหามุมระหว่างสองด้านนั้น',
     r'\\dfrac\{1\}\{2\}\s*\\?c?d?o?t?\s*[a-z0-9]{1,3}\s*\\?c?d?o?t?\s*[a-z0-9]{1,3}\s*\\sin|'
     r'พื้นที่.{0,120}\\dfrac\{1\}\{2\}.{0,60}\\sin', flags=re.S)

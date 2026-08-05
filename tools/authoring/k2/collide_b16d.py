# -*- coding: utf-8 -*-
"""กวาดชนก้อน 16 · รอบ 4 — ยังเติมช่อง "ยาก" ไม่ได้

ผลรอบ 3 (out_b16c.txt) ตัดสินไปแล้ว
  ⛔ U5 (cos 20 + cos 100 + cos 140 ⇒ 0) ถูกฆ่า — pat1-2557-11-q32 คือ
     cos 15 + cos 87 + cos 159 + cos 231 + cos 303 (ห้ามุมห่างกัน 72 องศา ⇒ 0)
     M เดียวกันเป๊ะ (ผลบวกโคไซน์ของมุมที่กระจายเท่ากันรอบวงกลม) และ A เดียวกัน (หาค่านิพจน์)
     ซ้ำยังมี pat1-2555-10-q08 (ก) cos(pi/5) + cos(3pi/5) + cos(pi) = 1/2 อีกตัว
  ⛔ U7 (คาบของ sin^4 x + cos^4 x) ถูกฆ่า — q055 ของเราเองคือ
     "sin^4 x + cos^4 x = a + b cos 4x หา a, b" ⇒ G ตรงเป๊ะ · M ตรงเป๊ะ (ยุบเป็น 3/4 + (1/4)cos 4x)
     ต่างแค่ A ⇒ WATCH-B ที่ชิดเกินไป
  ⛔ U8 (ตึกสองหลัง มุมก้มไปโคน + มุมเงยไปยอด) ถูกฆ่า — chap-07-q203 คือ
     "จากฐานตึกมุมเงยเสา 60 · จากยอดตึกสูง 60 ฟุต มุมเงยเสา 30" ⇒ แม่พิมพ์เดียวกัน
     และ pat1-2564-03-q22 · chap-07-q101 · q204 · q205 เต็มพื้นที่นี้อยู่แล้ว
  ⚠️ U10 (tan A + tan B + tan C = tan A tan B tan C) — U10a = 0 แต่ต้องยืนยันกับ
     q001 ของเราเอง (ยากมาก · 7.5/7.4 · มุมภายในสามเหลี่ยมกับ tan) และ chap-07-q164
     ⇒ รอบนี้พิมพ์เนื้อสองข้อนั้นออกมาเต็ม ๆ เพื่อชี้ขาด

แบบร่างที่ยิงรอบนี้ (ทั้งหมดเล็งช่อง "ยาก")
  V1 7.6+7.9  · ความยาวเส้นแบ่งครึ่งมุมในสามเหลี่ยม (ใช้การแบ่งพื้นที่ ⇒ 2bc cos(A/2)/(b+c))
  V2 7.7+7.2  · จำนวนคำตอบของสมการตรีโกณในช่วงยาว (เช่น [0, 10pi]) ⛔ ไม่ใช่ผลบวกคำตอบ
  V3 7.8      · เซตคำตอบของ "อสมการ" ที่มี arccos/arcsin (ไม่ใช่การหาค่านิพจน์)
  V4 7.10+7.11· ล้อ/รอกหมุน ⇒ ระยะทางที่เคลื่อนที่จากมุมที่หมุน (s = r·theta ประยุกต์)
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

BY = {q['id']: q for q in items}


def txt(q):
    parts = [q.get('question') or '']
    parts += [str(c) for c in (q.get('choices') or [])]
    ex = q.get('explanation') or ''
    parts += ex if isinstance(ex, list) else [str(ex)]
    return '\n'.join(parts)


def scan(label, pattern, qonly=False, show=10, flags=0):
    rx = re.compile(pattern, flags)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-32s %-8s %-12s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:120]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# ── ชี้ขาด U10 : พิมพ์เนื้อ q001 และ q164 เต็ม ────────────────────────────────
for _id in ('gen-chap-07-trigonometry-q001', 'chap-07-trigonometry-q164'):
    q = BY.get(_id)
    print()
    print('== เนื้อเต็ม %s ==' % _id)
    if not q:
        print('   (ไม่พบ)')
        continue
    print('   โจทย์:', (q.get('question') or '')[:700])
    for i, c in enumerate(q.get('choices') or []):
        print('   ตัวเลือก %d: %s' % (i + 1, str(c)[:180]))
    print('   correct =', q.get('correct'))

# ── V1 · ความยาวเส้นแบ่งครึ่งมุม ─────────────────────────────────────────────
scan('V1a · คำว่า "แบ่งครึ่งมุม/เส้นแบ่งครึ่ง/bisect"',
     r'แบ่งครึ่งมุม|เส้นแบ่งครึ่ง|แบ่งมุม[^\n]{0,10}ออกเป็นสองส่วนเท่า', show=25)
scan('V1b · คำว่า "เส้นมัธยฐาน/มัธยฐานของสามเหลี่ยม"',
     r'มัธยฐาน', show=25)
scan('V1c · คำว่า "จุด D บนด้าน BC" (เส้นเชียนภายในสามเหลี่ยม)',
     r'จุด\s*\$?D\$?\s*(อยู่)?บนด้าน|บนด้าน\s*\$?BC\$?', show=25)
scan('V1d · คำถามมีครึ่งมุม A/2 หรือ theta/2 ร่วมกับสามเหลี่ยม',
     r'\\dfrac\{A\}\{2\}|\\frac\{A\}\{2\}|\\dfrac\{\\theta\}\{2\}', qonly=True, show=20)

# ── V2 · จำนวนคำตอบในช่วงยาว ────────────────────────────────────────────────
scan('V2a · คำถามถาม "จำนวนคำตอบ/มีกี่คำตอบ/จำนวนสมาชิกของเซตคำตอบ"',
     r'จำนวนคำตอบ|มีกี่คำตอบ|จำนวนสมาชิกของเซตคำตอบ|กี่จำนวน[^\n]{0,30}สอดคล้องกับสมการ',
     qonly=True, show=30)
scan('V2b · ช่วงที่ยาวกว่า 2pi ในคำถาม (4pi, 6pi, 8pi, 10pi)',
     r'\b(4|6|8|10|12)\\pi\b', qonly=True, show=25)

# ── V3 · อสมการที่มีฟังก์ชันผกผัน ───────────────────────────────────────────
scan('V3a · คำว่า "อสมการ" ร่วมกับ arc',
     r'อสมการ[^\n]{0,120}(arc|\^\{-1\})|( arc|\^\{-1\})[^\n]{0,120}อสมการ', show=25)
scan('V3b · ทุกข้อในคลังที่คำถามมี arcsin/arccos/arctan (นับรวม)',
     r'\\arcsin|\\arccos|\\arctan|\\sin\^\{-1\}|\\cos\^\{-1\}|\\tan\^\{-1\}',
     qonly=True, show=8)
scan('V3c · เครื่องหมายอสมการอยู่ในสมการเดียวกับ arc',
     r'(arcsin|arccos|arctan)[^$]{0,60}(\\le|\\ge|<|>)', qonly=True, show=25)

# ── V4 · ล้อ/รอกหมุน ⇒ ระยะทาง ──────────────────────────────────────────────
scan('V4a · คำว่า "ล้อ/รอก/สายพาน/เฟือง"', r'ล้อ|รอก|สายพาน|เฟือง', show=25)
scan('V4b · คำว่า "รอบต่อนาที/หมุนครบ...รอบ"',
     r'รอบต่อนาที|หมุนครบ|หมุนไป[^\n]{0,20}รอบ|จำนวนรอบ', show=25)
scan('V4c · คำว่า "ความยาวส่วนโค้ง" ทั้งคลัง', r'ความยาวส่วนโค้ง|ความยาวของส่วนโค้ง', show=30)

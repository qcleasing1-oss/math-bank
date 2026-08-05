# -*- coding: utf-8 -*-
"""กวาดรอบสี่ของก้อน 12 — เฉพาะสองข้อที่ต้องออกแบบใหม่

รอบสามจับการชนได้สองจุด และทั้งสองจุดชนกับ "ข้อที่เราแต่งเอง" ไม่ใช่ของในคลัง
  ⛔ q065 ฉบับแรก (ให้ด้าน ⇒ ถาม sec A − tan A)
     ชนกับ gen-chap-07-trigonometry-q007 ซึ่งเป็นข้อเดียวกันกลับทิศ
     ("มุม C ฉาก ถ้า sec A − tan A = 1/3 แล้ว sin A") ⇒ G กับ M ตรงกัน ⇒ ทิ้ง
  ⛔ q068 ฉบับแรก (ให้ค่าสูงสุด-ต่ำสุด-คาบ ⇒ ถาม a+b+c)
     ชนกับ gen-chap-07-trigonometry-q009 ตรงตัว ("f(x) = a sin(bx) + c ... ค่าสูงสุด...") ⇒ ทิ้ง
  บทเรียน: โพรบรอบ 1–2 ที่กรอง only7 ด้วย regex คนละสำนวน **มองไม่เห็นข้อของเราเอง**
           ⇒ รอบยิงตรงต่อข้อ (ไม่กรองบท) เป็นด่านที่ขาดไม่ได้

ฉบับแทน
  q065 ใหม่ · 7.1 ง่าย  : สามเหลี่ยมมุมฉาก 9-12-15 ⇒ ถาม (sin A + cos A)/tan A
  q068 ใหม่ · 7.10 ปานกลาง : ระยะทางบนผิวโลกตามเส้นเมริเดียนเดียวกัน (ละติจูดต่างกัน)
       (T3 ในรอบสองให้ผล 0 ข้อ — รอบนี้กวาดซ้ำด้วยถ้อยคำของข้อจริง)
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
    for r in (q.get('rows') or []):
        parts += [str(r.get('text', '')), str(r.get('why', ''))]
    return '\n'.join(parts)


def scan(label, pattern, qonly=False, show=8):
    rx = re.compile(pattern)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-30s %-8s %-12s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:105]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# ── q065 ใหม่ ────────────────────────────────────────────────────────────────
scan('q065-A · นิพจน์ (sin + cos) หารด้วย tan (หรือคูณ)',
     r'\(\s*\\sin[^)]{0,30}?\+\s*\\cos[^)]{0,30}?\)[\s\S]{0,40}?\\tan|'
     r'\\dfrac\{\\sin[\s\S]{0,60}?\+\s*\\cos[\s\S]{0,60}?\}\{\\tan')
scan('q065-B · สามเหลี่ยมมุมฉากด้าน 9-12-15 (หรือ 3-4-5 ขยาย)',
     r'9[\s\S]{0,50}?12[\s\S]{0,50}?15|12[\s\S]{0,50}?9[\s\S]{0,50}?15', qonly=True)
scan('q065-C · "มุมฉาก" + ให้ด้านประกอบมุมฉากสองด้านเป็นตัวเลข',
     r'มุมฉาก[\s\S]{0,180}?ยาว\s*\$?\d+[\s\S]{0,120}?ยาว\s*\$?\d+', qonly=True)

# ── q068 ใหม่ ────────────────────────────────────────────────────────────────
scan('q068-A · โลก/ทรงกลม + ละติจูด + ระยะตามผิว',
     r'ละติจูด|ลองจิจูด|เมริเดียน|ผิวโลก|รัศมีของโลก|โลกเป็นทรงกลม|6,?400')
scan('q068-B · ส่วนโค้งของวงกลมใหญ่ที่รัศมีเป็นหลักพัน',
     r'รัศมี[\s\S]{0,40}?\d{3,}[\s\S]{0,120}?(?:ส่วนโค้ง|ระยะทาง)', qonly=True)
scan('q068-C · แปลงองศาเป็นเรเดียนแล้วหาความยาวส่วนโค้ง (ยืนยันแม่พิมพ์ที่มีอยู่)',
     r'ความยาวส่วนโค้ง|ส่วนโค้งยาว|ยาวของส่วนโค้ง', show=14)

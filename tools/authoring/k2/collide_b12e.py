# -*- coding: utf-8 -*-
"""กวาดรอบห้า — เฉพาะ q068 ฉบับที่สาม และยืนยัน q065 ฉบับที่สอง

รอบสี่ให้ผล
  q065-A นิพจน์ (sin+cos)/tan = 0 ✅
  q065-C "มุมฉาก + ให้ด้านเป็นตัวเลข" = 2 ข้อ
        ⚠️ gen-chap-07-trigonometry-q010 (ให้ด้านตรงข้ามมุมฉาก 25 + ด้านประกอบ 7 ⇒ ถาม tan B)
           ⇒ G ต่าง (ฉากบวกประกอบ vs ประกอบสองด้าน) · A ต่าง (อัตราส่วนเดี่ยว vs นิพจน์ประกอบ)
           ⇒ ต่างกัน 2 ใน 3 แกน ⇒ ผ่านกฎเหล็ก 5 · ไม่ใช่ ❌ และไม่ใช่ WATCH-A
  q068-A ละติจูด/ผิวโลก = 3 ข้อ แต่ทั้งสามเป็นบท 18 ดอกเบี้ย (regex ไปโดนเลขเงิน) ⇒ ว่างจริง
  q068-C ความยาวส่วนโค้ง = 21 ข้อ ⇒ แม่พิมพ์ "แปลงองศาแล้ว s = r·theta" อิ่มแล้ว
        ⚠️ q033 ลูกตุ้ม (ก้าน 45 ซม. · มุม 24 องศา ⇒ ระยะโค้ง) มี A กับ M ตรงกับ q068 ฉบับสอง
           ⇒ ฉบับสอง (สองเมืองบนเมริเดียนเดียวกัน) จะเป็น WATCH-A ⇒ เปลี่ยนเป็นฉบับสาม

ฉบับสามของ q068 · 7.10/7.11 : สองเมืองบน **เส้นละติจูดเดียวกัน** (วงกลมเล็ก)
  ต้องหารัศมีของวงกลมละติจูดก่อน (R cos(phi)) แล้วจึงใช้ s = r·theta
  ⇒ M ใหม่จริง ไม่มีในคลัง ⇒ ต้องกวาดยืนยัน
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


def scan(label, pattern, qonly=False, show=10):
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

scan('q068-D · วงกลมที่เกิดจากระนาบตัดทรงกลม (วงกลมเล็ก/วงกลมใหญ่)',
     r'ระนาบ[\s\S]{0,60}?ตัด[\s\S]{0,60}?(?:ทรงกลม|ผิวโลก|ทรงกลมรัศมี)|'
     r'วงกลมเล็ก|วงกลมใหญ่ของทรงกลม|ตัดทรงกลม')

scan('q068-E · รัศมีที่ต้องฉายลงมาด้วย cos ก่อนใช้ s = r·theta',
     r'(?:R|รัศมี)\s*\\?c?o?s?[\s\S]{0,40}?\\cos[\s\S]{0,120}?(?:ส่วนโค้ง|ความยาวโค้ง|ระยะทางตาม)')

scan('q068-F · ทรงกลม + ระยะทางบนผิว (คำใดก็ได้)',
     r'ทรงกลม[\s\S]{0,200}?(?:ระยะทาง|ระยะห่าง)', qonly=True)

scan('q068-G · โจทย์ที่พูดถึง "แกนหมุน/ขั้วโลก/ศูนย์สูตร"',
     r'ขั้วโลก|ศูนย์สูตร|แกนโลก|แกนหมุน')

scan('q065-D · ยืนยันอีกครั้ง : ถามนิพจน์ที่รวม sin กับ cos แล้วหารด้วย tan',
     r'\\dfrac\{\\sin\s*A\s*\+\s*\\cos\s*A\}|'
     r'\(\\sin[^)]{0,20}\+\\cos[^)]{0,20}\)[\s\S]{0,30}\\tan|'
     r'\\sin\s*A\s*\+\s*\\cos\s*A[\s\S]{0,60}?\\tan\s*A')

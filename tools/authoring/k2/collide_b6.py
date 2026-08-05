# -*- coding: utf-8 -*-
"""STEP H (ทำก่อนแต่ง) · ก้อน 6 · 7.2 + 7.3 · กวาดคลัง + ข้อใหม่ของเราเอง
ตรวจ 5 แม่พิมพ์ที่ตั้งใจจะใช้ ว่าชนของเดิมหรือไม่ · เกณฑ์ ต่างอย่างน้อย 2 ใน 3 แกน"""
import glob, json, re, io

QS = []
for fp in sorted(glob.glob('/tmp/mb27/data/sets/*.json')):
    d = json.load(io.open(fp, encoding='utf-8'))
    for q in d.get('questions', []):
        QS.append(('คลัง', q))
for fp in sorted(glob.glob('/home/claude/k1/out/*.json')) + \
          sorted(glob.glob('/home/claude/k2/out/*.json')):
    d = json.load(io.open(fp, encoding='utf-8'))
    for q in d.get('questions', []):
        QS.append(('ใหม่', q))
print('ฐานเทียบ:', len(QS), 'ข้อ (คลัง + ที่เราแต่งไปแล้ว)')


def stem(q):
    s = q.get('question')
    if isinstance(s, list):
        s = ' '.join(x for x in s if isinstance(x, str))
    return (s or '').replace('\n', ' ')


PROBES = [
    ('q035 · จุดปลายส่วนโค้ง/มุมในตำแหน่งมาตรฐาน อยู่บนเส้นตรงที่กำหนด',
     r'(อยู่บนเส้นตรง|บนเส้นตรง|เส้นตรง)[^.]{0,60}(ผ่านจุดกำเนิด|=\s*0)|'
     r'ด้านสิ้นสุด[^.]{0,60}เส้นตรง|แขนของมุม[^.]{0,60}เส้นตรง'),
    ('q035b · โจทย์ที่ให้เงื่อนไขจตุภาคแล้วถาม sin ลบ cos',
     r'\\sin\s*\\?theta\s*-\s*\\cos|\\sin\s*A\s*-\s*\\cos\s*A|'
     r'\\sin\\theta\s*-\s*\\cos\\theta'),
    ('q036 · สูตรมุมสัมพันธ์ (pi ลบ theta / pi ส่วน 2 บวก theta / 2pi ลบ theta)',
     r'\\sin\s*\(\s*\\pi\s*-|\\cos\s*\(\s*\\pi\s*\+|'
     r'\\tan\s*\(\s*2\s*\\pi\s*-|\\sin\s*\(\s*\\dfrac\{3\\pi\}\{2\}|'
     r'\\cos\s*\(\s*\\dfrac\{\\pi\}\{2\}\s*\+'),
    ('q036b · คำว่า มุมสัมพันธ์ / ลดทอนมุม',
     r'มุมสัมพันธ์|ลดทอนมุม|มุมอ้างอิง'),
    ('q037 · นับจำนวนจำนวนเต็ม n ที่มุม n pi ส่วน k ตกในจตุภาคหนึ่ง',
     r'จำนวนเต็ม\s*\$?n[^.]{0,120}จตุภาค|จตุภาค[^.]{0,120}จำนวนเต็ม\s*\$?n|'
     r'มีจำนวนเต็ม[^.]{0,80}กี่จำนวน[^.]{0,80}จตุภาค'),
    ('q037b · โจทย์นับจำนวนที่ใช้ช่วง 1 ถึง 100 กับมุมเป็นพหุคูณของ pi ส่วน 6',
     r'\\dfrac\{n\\pi\}\{6\}|\\dfrac\{n\\pi\}\{4\}|\\dfrac\{n\\pi\}\{3\}|n\\pi\s*/\s*6'),
    ('q038 · พิสัย/ค่าสูงสุดของเศษส่วนที่มีตรีโกณอยู่ในตัวส่วน',
     r'\\dfrac\{\s*\d+\s*\}\{[^}]{0,30}\\(sin|cos)|'
     r'\\dfrac\{1\}\{[^}]{0,30}\\(sin|cos)'),
    ('q038b · คำว่า พิสัย / เรนจ์ ของฟังก์ชันตรีโกณ',
     r'พิสัยของ[^.]{0,60}(\\sin|\\cos|\\tan|ตรีโกณ)'),
    ('q039 · กราฟสองกราฟตัดกัน (sin 2x กับ cos x)',
     r'กราฟ[^.]{0,80}ตัดกัน|ตัดกัน[^.]{0,80}กราฟ|จุดตัดของกราฟ'),
    ('q039b · sin 2x เท่ากับ cos x (ทุกสำนวน)',
     r'\\sin\s*2x\s*=\s*\\cos\s*x|\\cos\s*x\s*=\s*\\sin\s*2x|'
     r'\\sin\s*2\\theta\s*=\s*\\cos\\theta'),
    ('รวม · คำว่า จุดปลายส่วนโค้ง',
     r'จุดปลายส่วนโค้ง'),
    ('รวม · คำว่า วงกลมหนึ่งหน่วย',
     r'วงกลมหนึ่งหน่วย'),
]

for title, pat in PROBES:
    rx = re.compile(pat)
    hits = [(src, q) for src, q in QS if rx.search(stem(q))]
    print()
    print('=' * 78)
    print(title, ' ⇒ ', len(hits), 'ข้อ')
    print('=' * 78)
    for src, q in hits[:14]:
        print('  [%s]' % src, q.get('id'), '|', q.get('difficulty'),
              '|', q.get('subTopics'))
        print('      ', stem(q)[:165])
    if len(hits) > 14:
        print('   … อีก', len(hits) - 14, 'ข้อ')

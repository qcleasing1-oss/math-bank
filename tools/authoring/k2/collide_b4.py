# -*- coding: utf-8 -*-
"""STEP H · ก้อน 4 (7.3) · กวาดทั้งคลัง + ข้อใหม่ของเราเอง
หาแม่พิมพ์ใกล้เคียงของ q025-q029 · เกณฑ์: ต้องต่างอย่างน้อย 2 ใน 3 แกน"""
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
    ('q025 · ถามคาบของฟังก์ชัน',
     r'คาบ'),
    ('q025b · คาบของ "ผลบวก" ของสองพจน์ตรีโกณ',
     r'(\\sin|\\cos|\\tan)[^=]{0,40}\+[^=]{0,40}(\\sin|\\cos|\\tan)[^.]{0,120}คาบ|'
     r'คาบ[^.]{0,120}(\\sin|\\cos)[^=]{0,40}\+[^=]{0,40}(\\sin|\\cos)'),
    ('q026 · การแปลงกราฟ (เลื่อน/ยืด) ของกราฟตรีโกณ',
     r'(เลื่อน|ยืด|หด|สะท้อน)[^.]{0,120}กราฟ[^.]{0,120}(\\sin|\\cos|\\tan)|'
     r'กราฟ[^.]{0,120}(\\sin|\\cos|\\tan)[^.]{0,120}(เลื่อนไป|ยืดใน|หดใน)'),
    ('q026b · คำว่า "ยืดในแนวตั้ง/แนวนอน"',
     r'ยืดในแนว|หดในแนว|ยืดตามแนว'),
    ('q027 · สร้างฟังก์ชันจากค่าสูงสุด-ต่ำสุด-คาบ (a sin(bx+c)+d)',
     r'a\s*\\sin\s*\(\s*b|A\s*\\sin\s*\(\s*B|'
     r'ค่าสูงสุด[^.]{0,120}ค่าต่ำสุด[^.]{0,120}คาบ|'
     r'คาบ[^.]{0,120}ค่าสูงสุด[^.]{0,120}ค่าต่ำสุด'),
    ('q027b · ถามค่าของฟังก์ชันที่จุดหนึ่งหลังหาสัมประสิทธิ์',
     r'แอมพลิจูด[^.]{0,160}คาบ[^.]{0,160}(f\(|ค่าของ)'),
    ('q028 · โดเมนของรากที่สองที่มีตรีโกณอยู่ข้างใน',
     r'\\sqrt\{[^}]{0,40}(\\cos|\\sin|\\tan)|'
     r'โดเมน[^.]{0,120}(\\cos|\\sin|\\tan)'),
    ('q028b · ถามความยาวรวมของช่วง',
     r'ความยาว[^.]{0,60}ช่วง|ผลรวมความยาว'),
    ('q029 · ผลบวกของค่าสัมบูรณ์ของ sin หลายพจน์',
     r'\|\s*\\sin[^|]{0,40}\|[^.]{0,60}\+[^.]{0,60}\|\s*\\sin|'
     r'\\left\|\s*\\sin[^|]{0,60}\+[^.]{0,80}\\left\|\s*\\sin'),
    ('q029b · มุมเลื่อน 2π/3 · 4π/3 (สามพจน์เว้นระยะเท่ากัน)',
     r'\\dfrac\{2\\pi\}\{3\}[^.]{0,160}\\dfrac\{4\\pi\}\{3\}|'
     r'x\s*\+\s*\\dfrac\{2\\pi\}\{3\}'),
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

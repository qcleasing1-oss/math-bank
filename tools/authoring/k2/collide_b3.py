# -*- coding: utf-8 -*-
"""STEP H · ก้อน 3 (7.2) · กวาดทั้งคลัง 6,313 ข้อ + 19 ข้อใหม่ของเราเอง
หาแม่พิมพ์ใกล้เคียงของ q020-q024 · เกณฑ์: ต้องต่างอย่างน้อย 2 ใน 3 แกน"""
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
    ('q020 · ค่าตรีโกณของมุมที่เกิน 2π (โคเทอร์มินัล)',
     r'\\(sin|cos|tan)\s*\\?d?frac\{\s*(1[3-9]|[2-9][0-9])\s*\\?p?i?'
     r'|\\(sin|cos|tan)\s*\\dfrac\{(1[3-9]|[2-9][0-9])\\pi\}'),
    ('q020b · เศษส่วน π ที่ตัวเศษ ≥ 13 (ต้องลดรอบก่อน)',
     r'\\dfrac\{\s*(1[3-9]|[2-9][0-9])\\pi\s*\}\{\s*[236]\s*\}'),
    ('q021 · ให้พิกัดจุดปลายส่วนโค้ง แล้วถามค่าฟังก์ชัน',
     r'จุดปลายส่วนโค้ง.{0,160}\(\s*-?\\?d?frac|จุดปลายส่วนโค้ง.{0,120}คือจุด'),
    ('q021b · สูตรลดทอนแบบ sin(θ+π) / cos(-θ)',
     r'\\sin\s*\(\s*\\theta\s*\+\s*\\pi|\\cos\s*\(\s*-\s*\\theta'),
    ('q022 · ให้ tan แล้วมีเงื่อนไขเครื่องหมาย/จตุภาค',
     r'\\tan\s*\\?t?h?e?t?a?\s*=.{0,60}(sin|\\sin)\s*\\theta\s*<|'
     r'(<\s*\\theta\s*<).{0,40}\\tan\s*\\theta\s*='),
    ('q022b · ถามค่า k(sinθ + cosθ) แบบคูณตัวส่วนออก',
     r'2[05]\s*\\?l?e?f?t?\(\s*\\sin|\\sin\s*\\theta\s*\+\s*\\cos\s*\\theta'),
    ('q023 · ระยะทางแนวเส้นตรง / คอร์ด จากจุด (1, 0)',
     r'\(\s*1\s*,\s*0\s*\).{0,120}(ระยะ|ห่าง|คอร์ด)|'
     r'(ระยะ|ห่าง|คอร์ด).{0,120}\(\s*1\s*,\s*0\s*\)'),
    ('q024 · ภาพสะท้อน / สมมาตร ของจุดปลายส่วนโค้ง',
     r'จุดปลายส่วนโค้ง.{0,120}(สะท้อน|สมมาตร)|'
     r'(สะท้อน|สมมาตร).{0,120}จุดปลายส่วนโค้ง'),
    ('q024b · เทียบมุม θ กับ 3θ/5θ บนวงกลมหนึ่งหน่วย',
     r'วงกลมหนึ่งหน่วย.{0,200}5\s*\\theta|5\\theta.{0,200}วงกลมหนึ่งหน่วย'),
]

for title, pat in PROBES:
    rx = re.compile(pat)
    hits = [(src, q) for src, q in QS if rx.search(stem(q))]
    print()
    print('=' * 78)
    print(title, ' ⇒ ', len(hits), 'ข้อ')
    print('=' * 78)
    for src, q in hits[:12]:
        print('  [%s]' % src, q.get('id'), '|', q.get('difficulty'),
              '|', q.get('subTopics'))
        print('      ', stem(q)[:170])
    if len(hits) > 12:
        print('   … อีก', len(hits) - 12, 'ข้อ')

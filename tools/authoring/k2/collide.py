# -*- coding: utf-8 -*-
"""STEP H · เช็คไม่ซ้ำ 2-ใน-3 · กวาดทั้งคลัง 6,313 ข้อ หาแม่พิมพ์ใกล้เคียงของ 5 ข้อใหม่"""
import glob, json, re, io

QS = []
for fp in sorted(glob.glob('/tmp/mb25/data/sets/*.json')):
    d = json.load(io.open(fp, encoding='utf-8'))
    for q in d.get('questions', []):
        QS.append((fp.split('/')[-1], q))
print('รวมข้อในคลัง:', len(QS))


def stem(q):
    s = q.get('question')
    if isinstance(s, list):
        s = ' '.join(x for x in s if isinstance(x, str))
    return s or ''


PROBES = [
    ('E-1 · สามเหลี่ยมมุมฉาก ให้ด้าน ⇒ หาอัตราส่วนตรีโกณ',
     r'มุมฉาก'),
    ('E-1b · สามเหลี่ยม 7-24-25',
     r'(7\s*,\s*24|24\s*,\s*25|\b25\b.*\b7\b|\b7\b.*\b24\b)'),
    ('E-2 · ให้ tan ของมุมแหลม ⇒ หา sin+cos',
     r'\\tan\s*A?\s*(=|\}\s*=).{0,20}(แหลม|มุมแหลม)|แหลม.{0,60}\\tan'),
    ('E-2b · หา sin+cos (ผลบวกของสองฟังก์ชัน)',
     r'\\sin\s*[A-Za-z\\][^+]{0,12}\+\s*\\cos'),
    ('E-3 · ค่าตรีโกณของมุมพิเศษ 120/135 (องศา)',
     r'(120|135)\^\\circ'),
    ('E-3b · tan + cot ของมุมองศา',
     r'\\tan.{0,40}\\cot|\\cot.{0,40}\\tan'),
    ('E-4 · ค่าต่ำสุด/สูงสุดของ a ± b cos(cx)',
     r'(ต่ำสุด|สูงสุด|น้อยที่สุด|มากที่สุด).{0,80}\\cos|\\cos.{0,60}(ต่ำสุด|สูงสุด|น้อยที่สุด|มากที่สุด)'),
    ('E-5 · sinθcosθ = k ⇒ (sin+cos)²',
     r'\\sin\s*\\theta\s*\\cos\s*\\theta|\\sin\s*\\theta\\cos\s*\\theta'),
    ('E-5b · (sin+cos)² หรือ sin+cos กำลังสอง',
     r'\(\s*\\sin[^)]{0,25}\+\s*\\cos[^)]{0,15}\)\s*\^\s*\{?2'),
]

for title, pat in PROBES:
    rx = re.compile(pat)
    hits = []
    for fn, q in QS:
        if rx.search(stem(q)):
            hits.append((fn, q.get('id'), q.get('difficulty'), q.get('subTopics'), stem(q)[:150]))
    print()
    print('=' * 78)
    print(title, ' ⇒ ', len(hits), 'ข้อ')
    print('=' * 78)
    for h in hits[:14]:
        print('  ', h[1], '|', h[2], '|', h[3], '|', h[4].replace('\n', ' '))
    if len(hits) > 14:
        print('   … อีก', len(hits) - 14, 'ข้อ')

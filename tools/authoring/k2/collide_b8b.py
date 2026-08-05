# -*- coding: utf-8 -*-
"""STEP H รอบสอง · ก้อน 8 ฉบับออกแบบใหม่ · 5 แม่พิมพ์ใหม่หลังจากของเดิมตายหมด 5 อัน
กวาดคลัง 6,313 + ที่เราแต่งเอง 44 = 6,357 ข้อ"""
import glob, json, re, io

QS = []
for fp in sorted(glob.glob('/tmp/mb27/data/sets/*.json')):
    for q in json.load(io.open(fp, encoding='utf-8')).get('questions', []):
        QS.append(('คลัง', q))
for fp in sorted(glob.glob('/home/claude/k1/out/*.json')) + \
          sorted(glob.glob('/home/claude/k2/out/*.json')):
    for q in json.load(io.open(fp, encoding='utf-8')).get('questions', []):
        QS.append(('ใหม่', q))
print('ฐานเทียบ:', len(QS), 'ข้อ')


def stem(q):
    s = q.get('question')
    if isinstance(s, list):
        s = ' '.join(x for x in s if isinstance(x, str))
    return (s or '').replace('\n', ' ')


def full(q):
    """โจทย์ + ตัวเลือก + เฉลย · ใช้ตอนอยากรู้ว่าเครื่องมือนี้เคยถูกใช้ที่ไหนบ้าง"""
    parts = [stem(q)]
    for c in q.get('choices') or []:
        if isinstance(c, str):
            parts.append(c)
    e = q.get('explanation')
    if isinstance(e, list):
        parts += [x for x in e if isinstance(x, str)]
    elif isinstance(e, str):
        parts.append(e)
    return ' '.join(parts)


PROBES = [
    # ── q045 · 7.2 · เครื่องหมายของอัตราส่วนสองตัว ⇒ จุดปลายส่วนโค้งอยู่จตุภาคใด ──
    ('q045 · เงื่อนไขเครื่องหมาย (ผลคูณ/ผลหารของอัตราส่วน) แล้วถามจตุภาค',
     r'(\\sin|\\cos|\\tan|\\cot|\\sec|\\csc)[^.]{0,40}(<\s*0|>\s*0)[^.]{0,120}จตุภาค|'
     r'จตุภาค[^.]{0,120}(<\s*0|>\s*0)', 'stem'),
    ('q045b · คำว่า จตุภาค ในบทที่ 7 เท่านั้น', r'จตุภาค', 'chap7'),
    ('q045c · เครื่องหมายบวก/ลบ ของอัตราส่วนเป็นหัวใจของข้อ',
     r'เครื่องหมายของ\s*(\\sin|\\cos|\\tan|ค่า)|มีเครื่องหมายเป็นลบ|เป็นจำนวนลบ[^.]{0,30}\\', 'stem'),

    # ── q046 · เรียงลำดับค่าตรีโกณของมุมเรเดียนที่ไม่ใช่มุมมาตรฐาน ──
    ('q046 · เรียงลำดับค่าจากน้อยไปมาก / เปรียบเทียบขนาดของค่าตรีโกณ',
     r'เรียงลำดับ|จากน้อยไปมาก|จากมากไปน้อย|ข้อใดมีค่ามากที่สุด|ข้อใดมีค่าน้อยที่สุด|'
     r'ค่าใดมากที่สุด|เรียงจาก', 'stem'),
    ('q046b · sin/cos/tan ของ 1 หรือ 2 หรือ 3 เรเดียน (ไม่มีองศา ไม่มี pi)',
     r'\\(sin|cos|tan)\s*\{?\s*[123]\s*\}?(?!\^)(?![0-9])', 'stem'),
    ('q046c · คำว่า เรเดียน ในบทที่ 7', r'เรเดียน', 'chap7'),

    # ── q047 · อสมการตรีโกณ ⇒ ความยาวรวมของเซตคำตอบ ──
    ('q047 · อสมการตรีโกณ (มีเครื่องหมาย < > ≤ ≥ คร่อมฟังก์ชันตรีโกณ)',
     r'(\\sin|\\cos|\\tan)[^.$]{0,30}(\\le|\\ge|<|>)\s*\\?d?frac|'
     r'(\\le|\\ge|<|>)\s*(\\sin|\\cos|\\tan)\s*\d?\s*x|'
     r'(\\sin|\\cos|\\tan)\s*\d?\s*x\s*(\\le|\\ge|<|>)', 'stem'),
    ('q047b · ความยาวรวม/ผลรวมความยาวของช่วงคำตอบ',
     r'ความยาวรวม|ผลรวมของความยาว|ความยาวของช่วง|ความยาวทั้งหมดของ', 'stem'),
    ('q047c · เซตคำตอบของอสมการ', r'เซตคำตอบของอสมการ|คำตอบของอสมการ', 'stem'),

    # ── q048 · ช่วงที่ฟังก์ชันตรีโกณเป็นฟังก์ชันเพิ่ม/ลด ──
    ('q048 · ฟังก์ชันเพิ่ม / ฟังก์ชันลด',
     r'ฟังก์ชันเพิ่ม|ฟังก์ชันลด|เพิ่มขึ้นบนช่วง|ลดลงบนช่วง|มีค่าเพิ่มขึ้น|มีค่าลดลง', 'stem'),
    ('q048b · ฟังก์ชันเพิ่ม/ลด ที่ไหนก็ได้ในคลัง (ดูว่าบทอื่นใช้เยอะไหม)',
     r'ฟังก์ชันเพิ่ม|ฟังก์ชันลด', 'stem-all'),

    # ── q049 · จำนวนรอบของกราฟในช่วงที่กำหนด ⇒ ถอดค่าคงตัว b ──
    ('q049 · จำนวนรอบ / ครบรอบ ของกราฟตรีโกณ',
     r'ครบ\s*\d*\s*รอบ|จำนวนรอบ|กี่รอบ|รอบพอดี', 'stem'),
    ('q049b · หาค่าคงตัว b ใน sin bx / cos bx',
     r'y\s*=\s*\\?[a-z]*\s*\\(sin|cos)\s*b\s*x|\\(sin|cos)\s*\(\s*b\s*x', 'stem'),
    ('q049c · คำว่า คาบ ในบทที่ 7 (ดูความหนาแน่น)', r'คาบ', 'chap7'),
]

for title, pat, mode in PROBES:
    rx = re.compile(pat)
    if mode == 'chap7':
        pool = [(s, q) for s, q in QS
                if any(str(t).startswith('7.') for t in (q.get('subTopics') or []))]
    else:
        pool = QS
    txt = full if mode == 'full' else stem
    hits = [(s, q) for s, q in pool if rx.search(txt(q))]
    print()
    print('=' * 78)
    print(title, ' ⇒ ', len(hits), 'ข้อ', '(จากพูล %d)' % len(pool))
    print('=' * 78)
    for s, q in hits[:10]:
        print('  [%s]' % s, q.get('id'), '|', q.get('difficulty'), '|', q.get('subTopics'))
        print('      ', stem(q)[:160])
    if len(hits) > 10:
        print('   … อีก', len(hits) - 10, 'ข้อ')

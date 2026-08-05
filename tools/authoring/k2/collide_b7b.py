# -*- coding: utf-8 -*-
"""STEP H รอบสอง · ก้อน 7 · หลังเปลี่ยนแม่พิมพ์ q040 (ชนกับ q009 ของเราเอง)
และหลังปรับ q042 (ถาม sin) กับ q044 (ถามค่าต่ำสุด)"""
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
print('ฐานเทียบ:', len(QS), 'ข้อ')


def stem(q):
    s = q.get('question')
    if isinstance(s, list):
        s = ' '.join(x for x in s if isinstance(x, str))
    return (s or '').replace('\n', ' ')


PROBES = [
    ('q040 ใหม่ · คาบของ ผลบวก ของฟังก์ชันตรีโกณสองพจน์',
     r'\\sin[^=]{0,25}\+\s*\\cos[^.]{0,60}คาบ|คาบ[^.]{0,60}\\sin[^=]{0,25}\+\s*\\cos'),
    ('q040 ใหม่ · คำว่า คาบ (ทุกสำนวน) ในบท 7 ของคลังและของใหม่',
     r'คาบ'),
    ('q040 ใหม่ · อาร์กิวเมนต์รูป x ส่วน 2 หรือ x ส่วน 3 ในฟังก์ชันตรีโกณ',
     r'\\sin\s*\\dfrac\{x\}\{[23]\}|\\cos\s*\\dfrac\{x\}\{[23]\}|'
     r'\\sin\\dfrac\{x\}\{[23]\}|\\cos\\dfrac\{x\}\{[23]\}'),
    ('q042 ปรับ · ถามค่า sin theta จากเงื่อนไขเชิงเส้นของ sin กับ cos',
     r'3\\sin[^.]{0,30}4\\cos|4\\cos[^.]{0,30}3\\sin'),
    ('q044 ปรับ · ค่าต่ำสุดของนิพจน์ที่มี sin กำลังสอง',
     r'ค่าต่ำสุด[^.]{0,80}\\sin|\\sin\^\{?2\}?[^.]{0,60}ค่าต่ำสุด'),
    ('q044 ปรับ · รูป sin^2 x ลบ k sin x บวก c',
     r'\\sin\^\{?2\}?\s*x\s*-\s*\d*\\sin\s*x'),
    ('q041 · ส่วนโค้งยาวหลายร้อยหน่วย (เลขมากกว่าสองหลัก) บนวงกลมหนึ่งหน่วย',
     r'ยาว\s*\$?\d{3,}|\$\d{3,}\$\s*หน่วย'),
]

for title, pat in PROBES:
    rx = re.compile(pat)
    hits = [(src, q) for src, q in QS if rx.search(stem(q))]
    ch7 = [(s, q) for s, q in hits if '7' in (q.get('topics') or []) or
           any(str(t).startswith('7.') for t in (q.get('subTopics') or []))]
    print()
    print('=' * 78)
    print(title, ' ⇒ ', len(hits), 'ข้อ (เฉพาะบท 7 =', len(ch7), 'ข้อ)')
    print('=' * 78)
    for src, q in (ch7 if len(hits) > 20 else hits)[:14]:
        print('  [%s]' % src, q.get('id'), '|', q.get('difficulty'), '|', q.get('subTopics'))
        print('      ', stem(q)[:160])

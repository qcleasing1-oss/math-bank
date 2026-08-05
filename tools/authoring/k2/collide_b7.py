# -*- coding: utf-8 -*-
"""STEP H (ทำก่อนแต่ง) · ก้อน 7 · 7.2 + 7.3 · กวาดคลัง + ข้อใหม่ของเราเอง
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
    ('q040 · ถอดค่าคงตัว a b c จากค่าสูงสุด/ค่าต่ำสุด/คาบ ของกราฟไซน์',
     r'(ค่าสูงสุด|ค่าต่ำสุด)[^.]{0,120}คาบ|คาบ[^.]{0,120}(ค่าสูงสุด|ค่าต่ำสุด)'),
    ('q040b · คำว่า แอมพลิจูด',
     r'แอมพลิจูด|amplitude'),
    ('q040c · รูปแบบ a sin(bx) + c ที่ต้องหาค่าคงตัว',
     r'a\\sin|a\s*\\sin\s*\(\s*b|\\sin\s*\(\s*bx'),
    ('q041 · ส่วนโค้งยาวตามที่กำหนด แล้วถามว่าจุดปลายอยู่จตุภาคใด',
     r'อยู่ในจตุภาคใด|ตกอยู่ในจตุภาคใด|อยู่จตุภาคที่เท่าใด'),
    ('q041b · ส่วนโค้งยาว … หน่วย บนวงกลมหนึ่งหน่วย',
     r'ส่วนโค้งยาว|ความยาวส่วนโค้ง[^.]{0,40}หน่วย[^.]{0,40}วงกลมหนึ่งหน่วย|'
     r'วัดจากจุด\s*\$?\(1\s*,\s*0\)'),
    ('q042 · เงื่อนไข 3 sin + 4 cos = 5 (หรือ a sin + b cos = c ที่แตะขอบ)',
     r'3\\sin[^.]{0,30}4\\cos|4\\cos[^.]{0,30}3\\sin|'
     r'\\sin\\theta\s*\+\s*\d*\\cos\\theta\s*='),
    ('q043 · จำนวนคำตอบ/จำนวนจุดตัด ของสมการที่ต้องนับด้วยกราฟ',
     r'จำนวนคำตอบของสมการ|มีคำตอบกี่จำนวน|ตัดกันกี่จุด|กี่จุด[^.]{0,40}ตัดกัน'),
    ('q043b · สมการรูป ตรีโกณ = เส้นตรงเอียง (x ส่วนคงที่)',
     r'\\sin\s*x\s*=\s*\\dfrac\{x\}|\\cos\s*x\s*=\s*\\dfrac\{x\}|'
     r'=\s*\\dfrac\{x\}\{\d+\}'),
    ('q044 · ฟังก์ชันกำลังสองในตัวแปร sin (พาราโบลาซ่อนรูป)',
     r'\\sin\^\{?2\}?\s*x[^.]{0,40}\\sin\s*x|\\sin\^2x[^.]{0,40}\\sin\s*x'),
    ('q044b · ค่าสูงสุด/ต่ำสุดของนิพจน์ที่มี sin กำลังสอง',
     r'(ค่าสูงสุด|ค่าต่ำสุด)[^.]{0,60}\\sin\^\{?2\}?'),
    ('รวม · คำว่า จุดปลายส่วนโค้ง',
     r'จุดปลายส่วนโค้ง'),
    ('รวม · คำว่า คาบ ของฟังก์ชัน',
     r'คาบของฟังก์ชัน|คาบเท่ากับ|หาคาบ'),
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
        print('      ', stem(q)[:165])
    if len(hits) > 12:
        print('   … อีก', len(hits) - 12, 'ข้อ')

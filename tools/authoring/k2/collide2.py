# -*- coding: utf-8 -*-
"""STEP H รอบสอง · เจาะเฉพาะสองข้อที่ยังเสี่ยงชน: E-1 (อัตราส่วนในสามเหลี่ยมมุมฉาก) · E-4 (ค่าสุดขีดของ a+b cos)"""
import glob, json, re, io

QS = []
for fp in sorted(glob.glob('/tmp/mb25/data/sets/*.json')):
    d = json.load(io.open(fp, encoding='utf-8'))
    for q in d.get('questions', []):
        QS.append((fp.split('/')[-1], q))


def stem(q):
    s = q.get('question')
    if isinstance(s, list):
        s = ' '.join(x for x in s if isinstance(x, str))
    return s or ''


def show(title, pred, limit=20):
    hits = [(fn, q) for fn, q in QS if pred(fn, q)]
    print()
    print('=' * 78)
    print(title, '⇒', len(hits), 'ข้อ')
    print('=' * 78)
    for fn, q in hits[:limit]:
        print('  ', q.get('id'), '|', q.get('difficulty'), '|', q.get('subTopics'))
        print('     ', stem(q)[:230].replace('\n', ' '))
        ch = q.get('choices')
        if isinstance(ch, list):
            print('      ตัวเลือก:', ' / '.join(str(c)[:34] for c in ch))
    if len(hits) > limit:
        print('   … อีก', len(hits) - limit, 'ข้อ')


# ── E-1 : ข้อที่อยู่ในบท 7 และพูดถึงสามเหลี่ยมมุมฉาก + ถามอัตราส่วนตรีโกณตรง ๆ
rx1 = re.compile(r'มุมฉาก')
rx2 = re.compile(r'\\(tan|sin|cos|cot|sec|csc)')
show('E-1 · ข้อในบท 7 ที่มี "มุมฉาก" และสัญลักษณ์ตรีโกณ',
     lambda fn, q: fn.endswith('trigonometry.json') and rx1.search(stem(q)) and rx2.search(stem(q)))

# ── E-1 : ข้อที่ให้ความยาวด้านสองด้านแล้วถามอัตราส่วน (คีย์เวิร์ดความยาว)
rx3 = re.compile(r'(สามเหลี่ยม|รูปสามเหลี่ยม).{0,120}(ยาว|=)\s*\$?\d')
show('E-1b · บท 7 · สามเหลี่ยม + ให้ความยาวเป็นตัวเลข',
     lambda fn, q: fn.endswith('trigonometry.json') and rx3.search(stem(q))
     and q.get('difficulty') in ('ง่าย', 'ปานกลาง'), limit=14)

# ── E-4 : ทุกข้อในคลังที่ถามค่าสุดขีดของฟังก์ชันตรีโกณล้วน
rx4 = re.compile(r'(ค่าสูงสุด|ค่าต่ำสุด|มากที่สุด|น้อยที่สุด|สูงสุด|ต่ำสุด|แอมพลิจูด|พิสัย)')
rx5 = re.compile(r'\\(sin|cos)')
show('E-4 · ทั้งคลัง · ถามค่าสุดขีด/แอมพลิจูด ของฟังก์ชัน sin/cos',
     lambda fn, q: rx4.search(stem(q)) and rx5.search(stem(q))
     and any(str(s).startswith('7.') for s in (q.get('subTopics') or [])), limit=25)

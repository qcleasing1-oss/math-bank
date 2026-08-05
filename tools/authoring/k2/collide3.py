# -*- coding: utf-8 -*-
"""STEP H · ก้อน 2 · กวาดทั้งคลัง 6,313 ข้อ หาแม่พิมพ์ใกล้เคียงของ E-6 … E-10"""
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


def show(title, pred, limit=12):
    hits = [(fn, q) for fn, q in QS if pred(fn, q)]
    print()
    print('=' * 78)
    print(title, '⇒', len(hits), 'ข้อ')
    print('=' * 78)
    for fn, q in hits[:limit]:
        print('  ', q.get('id'), '|', q.get('difficulty'), '|', q.get('subTopics'))
        print('     ', stem(q)[:200].replace('\n', ' '))
    if len(hits) > limit:
        print('   … อีก', len(hits) - limit, 'ข้อ')


TRIG = re.compile(r'\\(sin|cos|tan|cot|sec|csc)')
SEV = lambda q: any(str(s).startswith('7.') for s in (q.get('subTopics') or []))

# E-6 · ให้ด้านหนึ่ง + อัตราส่วน ⇒ หาความยาวอีกด้าน
show('E-6 · ทั้งคลัง · "ยาว...หน่วย" + สามเหลี่ยม + tan/sin/cos ในโจทย์ (ป้าย 7.*)',
     lambda fn, q: SEV(q) and re.search(r'สามเหลี่ยม', stem(q))
     and re.search(r'ยาว', stem(q)) and TRIG.search(stem(q)))

# E-7 · sin A cos B − cos A sin B (ทรงสูตรผลต่างมุมแบบ "จำสูตรย้อนกลับ")
show('E-7 · ทั้งคลัง · ทรง sinAcosB ± cosAsinB',
     lambda fn, q: re.search(r'\\sin[^+\-]{0,25}\\cos[^+\-]{0,10}[+\-][^+\-]{0,10}\\cos[^+\-]{0,25}\\sin',
                             stem(q)))
show('E-7b · ทั้งคลัง · มุม 75° หรือ 15° ในโจทย์ (ป้าย 7.*)',
     lambda fn, q: SEV(q) and re.search(r'(75|15)\^\\circ', stem(q)))

# E-8 · tan 2θ
show('E-8 · ทั้งคลัง · มี \\tan 2 (มุมสองเท่าของ tan)',
     lambda fn, q: re.search(r'\\tan\s*(2|\{2)', stem(q)))
show('E-8b · ทั้งคลัง · กำหนด tanθ = ตัวเลข (ป้าย 7.*)',
     lambda fn, q: SEV(q) and re.search(r'\\tan\s*\\?[A-Za-z]*\s*(\\theta)?\s*=\s*\$?\-?\d', stem(q)))

# E-9 · สมการตรีโกณคำตอบเดียวในช่วงควอดรันต์แรก
show('E-9 · ทั้งคลัง · สมการทรง 2cos x = √3 / 2sin x = √3 (สัมประสิทธิ์ 2 หน้าฟังก์ชัน)',
     lambda fn, q: re.search(r'2\s*\\(sin|cos|tan)\s*\\?[a-zA-Z]', stem(q)))
show('E-9b · ทั้งคลัง · สมการตรีโกณที่จำกัดช่วง 0° ถึง 90°',
     lambda fn, q: SEV(q) and re.search(r'0\^\\circ.{0,40}90\^\\circ', stem(q)))

# E-10 · กฎไซน์จากสองมุมกับหนึ่งด้าน
show('E-10 · ทั้งคลัง · ให้สองมุม (30/45/60/105/120) + ด้านหนึ่ง ⇒ หาอีกด้าน',
     lambda fn, q: SEV(q) and len(re.findall(r'\d+\^\\circ', stem(q))) >= 2
     and re.search(r'สามเหลี่ยม', stem(q)))

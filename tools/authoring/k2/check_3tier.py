# -*- coding: utf-8 -*-
"""check_3tier.py — ด่านตรวจโครงเฉลย 3 ชั้น (q165–q184)

⛔ ด่านนี้ต้องล้มเองได้ — มี selftest ที่ป้อนของเสียเข้าไปแล้วต้องจับได้ทุกกรณี
   (บทเรียนจากด่าน 10 ที่ลงทะเบียนไว้แต่ไม่เคยทำงานจริง)
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'out', 'k2-ก้อน23-20ข้อ-q165-q184.json')
DST = os.path.join(ROOT, 'out', 'k2-เฉลย3ชั้น-q165-q184-20ข้อ.json')

BANNED = [
    (r'\\frac\b', r'\frac (ต้องใช้ \dfrac)'),
    ('√', 'อักขระ √ ดิบ (ต้องใช้ \\sqrt)'),
    (r'\\subseteq', r'\subseteq'),
    (r'\\phi\b', r'\phi'),
    (r'\\"', 'เครื่องหมายคำพูดหนี'),
    ('ดังรูป', 'คำว่า ดังรูป'),
    ('จากรูป', 'คำว่า จากรูป'),
    ('ตัวเลือกที่', 'สำนวน "ตัวเลือกที่ N"'),
    (r'<b>[^<]*<b>', '<b> ซ้อน <b>'),
]
DEG_RAW = re.compile(r'(?<!\^\\circ)°')
H_RE = re.compile(r'^<b>【 แบบที่ (\d) ▸ (พื้นฐาน \(ละเอียด\)|พื้นฐาน \(กระชับ\)|⚡ ประยุกต์) · (.+) 】</b>$')


def blocks(ex):
    """แยก explanation เป็น (หัวร่วม, [(เลข, ชนิด, ชื่อ, บรรทัด)...], หาง)"""
    hi = [i for i, l in enumerate(ex) if l.startswith('<b>【')]
    ti = next(i for i, l in enumerate(ex) if l.startswith('✔ <b>ตรวจคำตอบ'))
    out = []
    for k, i in enumerate(hi):
        j = hi[k + 1] if k + 1 < len(hi) else ti
        m = H_RE.match(ex[i])
        if not m:
            return ex[:hi[0]], None, ex[ti:], f'หัวผิดรูป: {ex[i][:90]}'
        out.append((int(m.group(1)), m.group(2), m.group(3), ex[i:j]))
    return ex[:hi[0]], out, ex[ti:], None


def check_one(q, src):
    e = []
    qid = q['id'][-4:]
    ex = q['explanation']
    head, bl, tail, err = blocks(ex)
    if err:
        return [f'{qid}: {err}']

    # ── 1. หัวร่วม
    if sum(l.startswith('📐 <b>โจทย์กำหนด</b>') for l in head) != 1:
        e.append('หัวร่วมต้องมี 📐 โจทย์กำหนด พอดี 1 บรรทัด')
    if sum(l.startswith('🎯 <b>เป้าหมาย</b>') for l in head) != 1:
        e.append('หัวร่วมต้องมี 🎯 เป้าหมาย พอดี 1 บรรทัด')
    if any(l.startswith('📚') for l in head):
        e.append('📚 ต้องอยู่ใน "แบบที่ 1" ไม่ใช่หัวร่วม')

    # ── 2. จำนวนและลำดับของแบบ
    if len(bl) not in (2, 3):
        e.append(f'ต้องมี 2 หรือ 3 แบบ พบ {len(bl)}')
    want = [(1, 'พื้นฐาน (ละเอียด)'), (2, 'พื้นฐาน (กระชับ)'), (3, '⚡ ประยุกต์')]
    for k, (n, kind, name, body) in enumerate(bl):
        if (n, kind) != want[k]:
            e.append(f'แบบลำดับที่ {k+1} ควรเป็น {want[k]} แต่พบ ({n}, {kind})')

    # ── 3. ①② ต้องชื่อวิธีเดียวกันเป๊ะ · ③ ต้องต่าง
    if len(bl) >= 2 and bl[0][2] != bl[1][2]:
        e.append(f'ชื่อวิธีของแบบที่ 1 กับ 2 ไม่ตรงกัน:\n      ① {bl[0][2]}\n      ② {bl[1][2]}')
    if len(bl) == 3 and bl[2][2] == bl[0][2]:
        e.append('แบบที่ 3 ใช้ชื่อวิธีเดียวกับแบบที่ 1 — ไม่ใช่วิธีใหม่')

    # ── 4. ชื่อวิธีต้องมีภาษาอังกฤษในวงเล็บ (กฎที่ครูสั่ง)
    for n, kind, name, body in bl:
        if not re.search(r'\([a-zA-Z][^)]*\)\s*$', name):
            e.append(f'แบบที่ {n}: ชื่อวิธีไม่มีภาษาอังกฤษปิดท้ายในวงเล็บ — {name[:60]}')
        if len(f'<b>【 แบบที่ {n} ▸ {kind} · {name} 】</b>') > 115:
            e.append(f'แบบที่ {n}: หัวยาวเกิน 115 ตัวอักษร')

    # ── 5. เนื้อในแต่ละแบบ
    b1 = bl[0][3]
    if sum(l.startswith('📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>') for l in b1) != 1:
        e.append('แบบที่ 1 ต้องมี 📚 ความรู้พื้นฐานที่ต้องใช้ พอดี 1 บรรทัด')
    if not any(l.startswith('<b>ขั้นที่') for l in b1):
        e.append('แบบที่ 1 ไม่มีบรรทัด "ขั้นที่"')
    b2 = bl[1][3]
    if any(l.startswith('📚') for l in b2):
        e.append('แบบที่ 2 (กระชับ) ต้องไม่มีก้อน 📚')
    if sum(l.startswith('<b>ขั้นที่') for l in b2) < 2:
        e.append('แบบที่ 2 ต้องมีอย่างน้อย 2 ขั้น')
    if len(''.join(b2)) >= len(''.join(b1)):
        e.append('แบบที่ 2 ไม่สั้นกว่าแบบที่ 1 — ผิดนิยาม "กระชับ"')
    if len(bl) == 3:
        b3 = bl[2][3]
        if not any(l.startswith('<b>ข้อต่าง:</b>') for l in b3):
            e.append('แบบที่ 3 ต้องปิดด้วยบรรทัด "ข้อต่าง:"')
        if any(l.startswith('📚') for l in b3):
            e.append('แบบที่ 3 ต้องไม่มีก้อน 📚')
        if len(''.join(b3)) >= len(''.join(b1)):
            e.append('แบบที่ 3 ไม่สั้นกว่าแบบที่ 1')

    # ── 6. หาง
    for pat, label in (('✔ <b>ตรวจคำตอบ', '✔ ตรวจคำตอบ'), ('✅ <b>คำตอบ</b>', '✅ คำตอบ'),
                       ('💡 <b>เทคนิค</b>', '💡 เทคนิค'), ('⚠️ <b>จุดพลาด</b>', '⚠️ จุดพลาด')):
        if sum(l.startswith(pat) for l in tail) != 1:
            e.append(f'หางต้องมี {label} พอดี 1 บรรทัด')

    # ── 7. คำว่า "ตัวเลือก"
    n_ch = ''.join(ex).count('ตัวเลือก')
    if q['type'] == 'mc' and n_ch != 1:
        e.append(f'ข้อชนิด mc ต้องมีคำว่า "ตัวเลือก" ครั้งเดียว (บรรทัด ✅) พบ {n_ch}')
    if q['type'] == 'fill' and n_ch != 0:
        e.append(f'ข้อชนิดเติมคำตอบต้องไม่มีคำว่า "ตัวเลือก" พบ {n_ch}')

    # ── 8. อักขระต้องห้าม + สมดุลแท็ก
    for i, l in enumerate(ex):
        for pat, label in BANNED:
            if re.search(pat, l):
                e.append(f'บรรทัด {i}: พบ {label}')
        if DEG_RAW.search(l):
            e.append(f'บรรทัด {i}: พบ ° ดิบ')
        if l.count('<b>') != l.count('</b>'):
            e.append(f'บรรทัด {i}: แท็ก <b> ไม่สมดุล')
        if l.count('$') % 2:
            e.append(f'บรรทัด {i}: $ ไม่เป็นคู่')

    # ── 9. ⛔ ห้ามแตะโจทย์
    for f in ('question', 'choices', 'correct', 'accept', 'difficulty', 'subTopics', 'type'):
        if q.get(f) != src.get(f):
            e.append(f'ฟิลด์ {f} ถูกแก้ — ผิดกฎเหล็ก ห้ามแตะข้อสอบเดิม')

    return [f'{qid}: {x}' for x in e]


# ═══════════════════ selftest — ด่านต้องจับของเสียได้จริง ═══════════════════
def selftest():
    base = {
        'id': 'x-q999', 'type': 'mc', 'question': 'q', 'choices': ['a', 'b'],
        'correct': 0, 'accept': None, 'difficulty': 'ง่าย', 'subTopics': ['7.1'],
        'explanation': [
            '📐 <b>โจทย์กำหนด</b>', '• อะไรสักอย่าง', '🎯 <b>เป้าหมาย</b> หาอะไรสักอย่าง',
            '<b>【 แบบที่ 1 ▸ พื้นฐาน (ละเอียด) · วิธีเอ (method a) 】</b>',
            '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>', '• สูตร', '<b>ขั้นที่ 1 · ทำ</b>', 'ยาว ๆ ' * 40,
            '<b>【 แบบที่ 2 ▸ พื้นฐาน (กระชับ) · วิธีเอ (method a) 】</b>',
            '<b>ขั้นที่ 1:</b> ทำ', '<b>ขั้นที่ 2:</b> จบ',
            '<b>【 แบบที่ 3 ▸ ⚡ ประยุกต์ · วิธีบี (method b) 】</b>',
            '<b>ขั้นที่ 1:</b> ลัด', '<b>ข้อต่าง:</b> สั้นกว่า',
            '✔ <b>ตรวจคำตอบ (วิธีอิสระ)</b>', 'ตรวจ',
            '✅ <b>คำตอบ</b> ได้ → <b>ตัวเลือก 1</b>',
            '💡 <b>เทคนิค</b>', 'เทคนิค', '⚠️ <b>จุดพลาด</b>', 'พลาด',
        ],
    }
    import copy
    ok = check_one(copy.deepcopy(base), base)
    assert not ok, f'selftest: ของดีต้องผ่าน แต่ได้ {ok}'

    cases = [
        ('②ชื่อไม่ตรง ①', 8, lambda d: d['explanation'].__setitem__(
            8, '<b>【 แบบที่ 2 ▸ พื้นฐาน (กระชับ) · วิธีซี (method c) 】</b>')),
        ('③ชื่อซ้ำ ①', 11, lambda d: d['explanation'].__setitem__(
            11, '<b>【 แบบที่ 3 ▸ ⚡ ประยุกต์ · วิธีเอ (method a) 】</b>')),
        ('ชื่อไม่มีอังกฤษ', 3, lambda d: (
            d['explanation'].__setitem__(3, '<b>【 แบบที่ 1 ▸ พื้นฐาน (ละเอียด) · วิธีเอ 】</b>'),
            d['explanation'].__setitem__(8, '<b>【 แบบที่ 2 ▸ พื้นฐาน (กระชับ) · วิธีเอ 】</b>'))),
        ('③ไม่มีข้อต่าง', 13, lambda d: d['explanation'].__setitem__(13, 'จบเฉย ๆ')),
        ('②มีก้อน 📚', 9, lambda d: d['explanation'].insert(9, '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>')),
        # ⛔ อย่าตัดแบบที่ 1 ให้สั้นลงเพื่อทดสอบ — ต้อง "ทำแบบที่ 2 ให้ยาว" ถึงจะวัดสิ่งที่ตั้งใจวัด
        ('②ไม่สั้นกว่า ①', 10, lambda d: d['explanation'].insert(10, 'ยืดยาว ' * 80)),
        (r'ใช้ \frac', 6, lambda d: d['explanation'].__setitem__(6, r'<b>ขั้นที่ 1 · $\frac{1}{2}$</b>')),
        ('° ดิบ', 6, lambda d: d['explanation'].__setitem__(6, '<b>ขั้นที่ 1 · มุม 30°</b>')),
        ('$ ไม่เป็นคู่', 6, lambda d: d['explanation'].__setitem__(6, '<b>ขั้นที่ 1 · $x</b>')),
        ('คำว่า ตัวเลือก เกิน', 6, lambda d: d['explanation'].__setitem__(6, '<b>ขั้นที่ 1 · ดูตัวเลือก</b>')),
        ('แตะ correct', 0, lambda d: d.__setitem__('correct', 1)),
        ('แตะ question', 0, lambda d: d.__setitem__('question', 'อื่น')),
        ('📚 อยู่หัวร่วม', 0, lambda d: d['explanation'].insert(0, '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>')),
        ('หางไม่มี 💡', 0, lambda d: d['explanation'].remove('💡 <b>เทคนิค</b>')),
        ('สลับลำดับแบบ', 0, lambda d: d['explanation'].__setitem__(
            3, '<b>【 แบบที่ 2 ▸ พื้นฐาน (กระชับ) · วิธีเอ (method a) 】</b>')),
    ]
    bad = []
    for name, _, mut in cases:
        d = copy.deepcopy(base)
        mut(d)
        if not check_one(d, base):
            bad.append(name)
    if bad:
        print('🔴 selftest ตก — ด่านมองไม่เห็นของเสียเหล่านี้:')
        for b in bad:
            print('   ✗', b)
        sys.exit(1)
    print(f'✅ selftest ผ่าน {len(cases)}/{len(cases)} · ด่านจับของเสียได้ทุกกรณี')


if __name__ == '__main__':
    selftest()
    src = {q['id'][-4:]: q for q in json.load(open(SRC, encoding='utf-8'))['questions']}
    dst = json.load(open(DST, encoding='utf-8'))['questions']
    errs = []
    for q in dst:
        errs += check_one(q, src[q['id'][-4:]])
    print()
    if errs:
        for x in errs:
            print('  ✗', x)
        print(f'\n🔴 ตก {len(errs)} จุด')
        sys.exit(1)
    n3 = sum(1 for q in dst if any('แบบที่ 3' in l for l in q['explanation']))
    print(f'✅ ผ่านครบ {len(dst)}/20 ข้อ · 3 แบบ {n3} ข้อ · 2 แบบ {len(dst) - n3} ข้อ')

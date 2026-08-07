# -*- coding: utf-8 -*-
"""รวมไฟล์ข้อเดี่ยวของก้อน 20 เป็นไฟล์สเตจใน /home/claude/k2/out/

⛔ ยึด stems_b20.py เป็นความจริง — _guard() เทียบทุกสนามทีละตัวอักษร
   ถ้าผู้แต่งเผลอแก้โจทย์/ตัวเลือก/คำตอบ จะหยุดทันที ⛔ ไม่เขียนไฟล์ผิดออกไป
📌 รูปแบบผลผลิตต้องเหมือน build_b19.py ทุกประการ เพราะ bootstrap.sh
   สร้างไฟล์นี้กลับมาใหม่ทุกครั้ง แล้ว regen_check ต้องได้ผลตรงทุกไบต์
"""
import io, json, os, collections, sys

sys.path.insert(0, '/home/claude/k2')
from stems_b20 import STEMS

OUT = '/home/claude/k2/out'
os.makedirs(OUT, exist_ok=True)
SRC = 'แต่งใหม่ v2 · แข่งขัน · 2569'
SET = 'gen-chap-07-trigonometry'
Q = []
SPEC = {s[0]: s for s in STEMS}


def _guard(n, st, level, stem, kind):
    assert n in SPEC, 'ข้อ %d ไม่มีในสเปก' % n
    s = SPEC[n]
    assert s[1] == st, 'q%03d subTopics ไม่ตรงสเปก: %r vs %r' % (n, st, s[1])
    assert s[2] == level, 'q%03d ระดับไม่ตรงสเปก: %r vs %r' % (n, level, s[2])
    assert s[3] == kind, 'q%03d ชนิดไม่ตรงสเปก: %r vs %r' % (n, kind, s[3])
    assert s[4] == stem, 'q%03d ตัวโจทย์ไม่ตรงสเปกทุกตัวอักษร' % n
    return s


def add(n, st, level, stem, choices, correct, expl, notes):
    s = _guard(n, st, level, stem, 'mc')
    assert s[5] == choices, 'q%03d ตัวเลือกไม่ตรงสเปก' % n
    assert s[6] == correct, 'q%03d correct ไม่ตรงสเปก: %r vs %r' % (n, correct, s[6])
    Q.append(collections.OrderedDict([
        ('id', '%s-q%03d' % (SET, n)), ('setId', SET), ('questionNumber', n),
        ('topics', ['7']), ('subTopics', st), ('difficulty', level),
        ('type', 'mc'), ('question', stem), ('choices', choices),
        ('hasImage', False), ('sourceTag', SRC), ('correct', correct),
        ('explanation', expl), ('notes', notes),
    ]))
    print('q%03d ok (mc · ช่อง %d)' % (n, correct + 1))


def add_fill(n, st, level, stem, correct, accept, expl, notes):
    s = _guard(n, st, level, stem, 'fill')
    assert s[6] == correct, 'q%03d correct ไม่ตรงสเปก: %r vs %r' % (n, correct, s[6])
    assert s[7] == accept, 'q%03d accept ไม่ตรงสเปก' % n
    assert isinstance(correct, str), 'q%03d ข้อ fill ต้องมี correct เป็นสตริง' % n
    Q.append(collections.OrderedDict([
        ('id', '%s-q%03d' % (SET, n)), ('setId', SET), ('questionNumber', n),
        ('topics', ['7']), ('subTopics', st), ('difficulty', level),
        ('type', 'fill'), ('question', stem),
        ('hasImage', False), ('sourceTag', SRC), ('correct', correct),
        ('accept', accept), ('explanation', expl), ('notes', notes),
    ]))
    print('q%03d ok (fill · คำตอบ %s)' % (n, correct))


for _n in range(125, 145):
    _p = '/home/claude/k2/parts_b20/q%03d.py' % _n
    exec(compile(io.open(_p, encoding='utf-8').read(), _p, 'exec'), globals())

assert len(Q) == 20, 'ได้ %d ข้อ ต้องได้ 20' % len(Q)
Q.sort(key=lambda z: z['questionNumber'])
data = collections.OrderedDict([('setId', SET), ('questions', Q)])
FN = 'k2-ก้อน20-20ข้อ-7.1-7.11-7.2-7.3-7.4.json'
path = os.path.join(OUT, FN)
txt = json.dumps(data, ensure_ascii=False, indent=2)
io.open(path, 'w', encoding='utf-8', newline='\n').write(txt)
print('เขียน', os.path.basename(path), '·', len(txt.encode()), 'B ·', len(Q), 'ข้อ')

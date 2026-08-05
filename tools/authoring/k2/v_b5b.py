# -*- coding: utf-8 -*-
"""STEP D เพิ่มเติม · q033 ปรับรัศมีเป็น 45 ซม. เพื่อเลี่ยงเลขชนกับวิธีตรวจอิสระ"""
from sympy import *
ok = []
def chk(tag, got, want, note=''):
    good = simplify(got - want) == 0
    ok.append(good)
    print(('  ✅ ' if good else '  ❌ ') + tag, '=', got, '|' if note else '', note)
def chkbool(tag, cond, note=''):
    ok.append(bool(cond)); print(('  ✅ ' if cond else '  ❌ ') + tag, '|' if note else '', note)

print('B5-4 rev (q033) · ลูกตุ้มก้านยาว 45 ซม. กวาด 24 องศา')
th = 24*pi/180
chk('แปลง 24 องศาเป็นเรเดียน', th, 2*pi/15)
chk('คำตอบ · s = r theta', 45*th, 6*pi)
chk('ตัวลวง A · ใช้ครึ่งมุม 12 องศา', 45*(12*pi/180), 3*pi)
chk('ตัวลวง B · พื้นที่เซกเตอร์แทนความยาวส่วนโค้ง', Rational(1,2)*45**2*th, 135*pi)
chk('ตัวลวง C · ไม่แปลงหน่วย 45 x 24', Integer(45*24), Integer(1080))
chk('ตรวจอิสระ · (24/360) x 2 pi r', Rational(24,360)*2*pi*45, 6*pi)
chk('เส้นรอบวงเต็มวง 2 pi r', 2*pi*45, 90*pi, 'ต้องไม่เท่ากับตัวลวงตัวใด')
chkbool('เส้นรอบวง 90pi ไม่ชนตัวเลือกใดเลย',
        len({3*pi, 6*pi, 135*pi, Integer(1080), 90*pi}) == 5)
chkbool('เรียงน้อยไปมาก 3pi < 6pi < 135pi < 1080',
        float(3*pi) < float(6*pi) < float(135*pi) < 1080)
chkbool('ตัวลวงต่างกันหมด', len({3*pi, 6*pi, 135*pi, Integer(1080)}) == 4)
print(); print('='*60); print('ผ่าน %d / %d' % (sum(1 for v in ok if v), len(ok)))

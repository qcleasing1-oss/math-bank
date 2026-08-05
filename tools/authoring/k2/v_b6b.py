# -*- coding: utf-8 -*-
"""STEP E (รอบแก้) · ก้อน 6 · ตรวจ “เส้นทางตัวลวง” ของ q036 ใหม่ทั้งสามเส้น
เหตุ: ตอนร่างครั้งแรกอ้างว่า tan θ มาจาก “ไม่เปลี่ยนชนิดและไม่ใส่เครื่องหมายเลย”
      แต่คำนวณจริงเส้นนั้นได้ tan^2 θ ⇒ ต้องหาเส้นทางที่ให้ tan θ จริง ๆ ก่อนเขียนเฉลย"""
from sympy import *

ok = []


def chk(tag, got, want, note=''):
    good = simplify(got - want) == 0
    ok.append(good)
    print(('  ✅ ' if good else '  ❌ ') + tag, '=', simplify(got), '|' if note else '', note)


th = symbols('theta')
S, C, T = sin(th), cos(th), tan(th)

print('q036 · ค่าจริงของแต่ละตัวประกอบ (ยืนยันด้วย sympy อีกครั้ง)')
chk('sin(pi - th)', simplify(sin(pi - th)), S)
chk('cos(pi/2 + th)', simplify(cos(pi / 2 + th)), -S)
chk('tan(2pi - th)', simplify(tan(2 * pi - th)), -T)
chk('cos(pi + th)', simplify(cos(pi + th)), -C)
chk('sin(3pi/2 - th)', simplify(sin(3 * pi / 2 - th)), -C)

print()
print('q036 · คำตอบจริง')
E = (sin(pi - th) * cos(pi / 2 + th) * tan(2 * pi - th)) / \
    (cos(pi + th) * sin(3 * pi / 2 - th))
chk('คำตอบ · นิพจน์เต็ม', E, T**3)

print()
print('q036 · เส้นทางตัวลวงที่แก้ใหม่')
# ตัวลวง A · ไม่เปลี่ยน “ชนิด” ที่ฐาน pi/2 และ 3pi/2 แต่ใส่เครื่องหมายถูกทั้งหมด
A = (S * (-C) * (-T)) / ((-C) * (-S))
chk('ตัวลวง A · ไม่เปลี่ยนชนิดที่ฐาน pi/2 และ 3pi/2 (เครื่องหมายถูก)', A, T,
    'ต้องได้ tan θ')
# ตัวลวง B · เปลี่ยนชนิดที่ pi/2 ถูก แต่ลืมเปลี่ยนชนิดที่ 3pi/2
B = (S * (-S) * (-T)) / ((-C) * (-S))
chk('ตัวลวง B · ลืมเปลี่ยนชนิดเฉพาะที่ฐาน 3pi/2', B, T**2, 'ต้องได้ tan^2 θ')
# ตัวลวง C · ทุกอย่างถูก ยกเว้นคิดว่า tan(2pi - th) = + tan th
Cc = (S * (-S) * (T)) / ((-C) * (-C))
chk('ตัวลวง C · พลาดเครื่องหมายจุดเดียวที่ tan(2pi - th)', Cc, -T**3,
    'ต้องได้ -tan^3 θ')

print()
print('q036 · ตัวเลือกทั้งสี่ต้องไม่ซ้ำกันเมื่อแทนมุมจริง th = pi/3')
vals = [T.subs(th, pi / 3), (T**2).subs(th, pi / 3),
        (-T**3).subs(th, pi / 3), (T**3).subs(th, pi / 3)]
print('   ', [simplify(v) for v in vals])
ok.append(len(set([simplify(v) for v in vals])) == 4)
print(('  ✅ ' if ok[-1] else '  ❌ ') + 'ตัวเลือกสี่ตัวต่างกันจริง')

print()
print('q036 · ตรวจอิสระด้วยการแทนมุมจริง th = pi/3')
v = simplify(E.subs(th, pi / 3))
chk('แทน th = pi/3 ในนิพจน์เต็ม', v, 3 * sqrt(3))
chk('เทียบกับ tan^3(pi/3)', (T**3).subs(th, pi / 3), 3 * sqrt(3))
num = simplify(sin(pi - th).subs(th, pi / 3) * cos(pi / 2 + th).subs(th, pi / 3) *
               tan(2 * pi - th).subs(th, pi / 3))
den = simplify(cos(pi + th).subs(th, pi / 3) * sin(3 * pi / 2 - th).subs(th, pi / 3))
chk('เศษที่ th = pi/3', num, 3 * sqrt(3) / 4)
chk('ส่วนที่ th = pi/3', den, Rational(1, 4))

print()
print('=' * 60)
print('ผ่าน %d / %d' % (sum(1 for v in ok if v), len(ok)))

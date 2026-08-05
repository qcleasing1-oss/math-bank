# -*- coding: utf-8 -*-
"""STEP D รอบแก้ · ก้อน 7 · แก้จุดที่ตัวตรวจเองบกพร่อง 3 จุด
 (1) q040 การสแกนคาบไปแตะขอบ 12pi เอง  (2)(3) q042 sympy ไม่ยุบ sin(2 atan(1/3)) ให้"""
from sympy import *
import math

ok = []


def chk(tag, cond, extra=''):
    ok.append(bool(cond))
    print(('  OK  ' if cond else '  FAIL') + ' | ' + tag + (' | ' + str(extra) if extra else ''))


x, th = symbols('x theta', real=True)

print('q040 · ยืนยันว่า 12pi คือคาบที่เล็กที่สุดจริง (ตัดย่านรอบ 12pi ออกจากการสแกน)')
ff = lambda t: math.sin(t / 2) + math.cos(t / 3)
XS = [i * 0.137 for i in range(1, 80)]
TWELVE = 12 * math.pi
best, bestT = 9e9, None
for k in range(1, 8000):
    T = TWELVE * k / 8000.0
    if T > TWELVE - 0.5:          # ตัดย่านที่ชิดคาบจริง ออกจากการสแกน
        break
    dev = max(abs(ff(t + T) - ff(t)) for t in XS)
    if dev < best:
        best, bestT = dev, T
chk('ทุก T ใน (0, 12pi - 0.5) ไม่เป็นคาบ', best > 0.05,
    'เบี่ยงเบนต่ำสุด %.4f ที่ T = %.4f' % (best, bestT))

print('   พิสูจน์เชิงสัญลักษณ์ · T ต้องเป็นคาบของทั้งสองพจน์พร้อมกัน')
T = symbols('T', positive=True)
# ถ้า f(x+T) = f(x) ทุก x แล้วแทน x และ x + 12pi/... ใช้วิธีตรง: แยกพจน์ด้วยความเป็นอิสระเชิงเส้น
# ตรวจว่า T ที่เป็นพหุคูณร่วมของ 4pi และ 6pi ตัวเล็กสุดคือ 12pi
cands = [Rational(a, 1) * 4 for a in range(1, 10)]        # T = 4pi * a
hits = [a for a in range(1, 10) if (4 * a) % 6 == 0]
chk('พหุคูณร่วมบวกที่น้อยที่สุดของ 4pi กับ 6pi คือ 12pi', hits[0] * 4 == 12, hits)
for Tv, name in [(2 * pi, '2pi'), (3 * pi, '3pi'), (4 * pi, '4pi'), (6 * pi, '6pi'),
                 (8 * pi, '8pi'), (9 * pi, '9pi'), (10 * pi, '10pi'), (11 * pi, '11pi')]:
    f = sin(x / 2) + cos(x / 3)
    d = simplify(f.subs(x, x + Tv) - f)
    chk('T = %s ไม่เป็นคาบ' % name, d != 0)

print()
print('q042 · ยุบค่า sin และ cos ของคำตอบที่ sympy คืนมาในรูป atan')
sols = solveset(Eq(3 * sin(th) + 4 * cos(th), 5), th, S.Reals)
print('   solveset ⇒', sols)
s0 = 2 * atan(Rational(1, 3))
sv = nsimplify(simplify(sin(s0)), rational=True)
cv = nsimplify(simplify(cos(s0)), rational=True)
print('   sin(2 atan(1/3)) =', sv, ' | cos(2 atan(1/3)) =', cv)
chk('sin(theta) = 3/5', sv == Rational(3, 5), sv)
chk('cos(theta) = 4/5', cv == Rational(4, 5), cv)
chk('ตรวจอิสระเชิงตัวเลข · sin = 0.6', abs(float(sin(s0)) - 0.6) < 1e-12, float(sin(s0)))
chk('ตรวจอิสระเชิงตัวเลข · cos = 0.8', abs(float(cos(s0)) - 0.8) < 1e-12, float(cos(s0)))
chk('แทนกลับสมการเดิมได้ 5 พอดี',
    simplify(3 * sin(s0) + 4 * cos(s0) - 5) == 0)
print('   คำตอบทั่วไปคือ theta = 2 atan(1/3) + 2k pi ซึ่งให้ sin เท่ากันทุก k')
for k in range(-3, 4):
    v = nsimplify(simplify(sin(s0 + 2 * k * pi)), rational=True)
    ok.append(v == Rational(3, 5))
chk('ทุก k ใน -3..3 ให้ sin(theta) = 3/5 เท่ากันหมด', all(ok[-7:]))
# ตรวจว่าไม่มีคำตอบอื่นในหนึ่งรอบเลย ด้วยการสแกนตัวเลข
gg = lambda t: 3 * math.sin(t) + 4 * math.cos(t) - 5
near = [i * 1e-5 for i in range(0, 628319) if abs(gg(i * 1e-5)) < 1e-3]
chk('สแกนหนึ่งรอบ · จุดที่ใกล้สอดคล้องสมการเกาะกลุ่มเดียว',
    max(near) - min(near) < 0.1, 'ช่วง %.5f ถึง %.5f' % (min(near), max(near)))
chk('จุดกึ่งกลางของกลุ่มนั้นคือ 2 atan(1/3) = %.6f' % float(s0),
    abs((max(near) + min(near)) / 2 - float(s0)) < 1e-3)

print()
print('=' * 70)
print('ผ่าน %d / %d' % (sum(1 for v in ok if v), len(ok)))

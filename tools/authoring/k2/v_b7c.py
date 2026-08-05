# -*- coding: utf-8 -*-
"""STEP D รอบแก้ที่สอง · แก้ตัวตรวจอีกสองจุด
 (1) q040 การสแกนไปแตะย่าน T ใกล้ศูนย์ ซึ่งไม่ใช่คาบ แต่ผลต่างเล็กตามธรรมชาติ
 (2) q042 ต้องบังคับให้ sympy ยุบ sin(atan(3/4)) ด้วย expand_trig ไม่ใช่ simplify เปล่า"""
from sympy import *
import math

ok = []


def chk(tag, cond, extra=''):
    ok.append(bool(cond))
    print(('  OK  ' if cond else '  FAIL') + ' | ' + tag + (' | ' + str(extra) if extra else ''))


x, th = symbols('x theta', real=True)

print('q040 · สแกน T ใน [0.5 , 12pi - 0.5] (ตัดทั้งย่านใกล้ศูนย์และย่านใกล้ 12pi)')
ff = lambda t: math.sin(t / 2) + math.cos(t / 3)
XS = [i * 0.137 for i in range(1, 120)]
TWELVE = 12 * math.pi
best, bestT = 9e9, None
k = 0
while True:
    T = 0.5 + k * 0.002
    if T > TWELVE - 0.5:
        break
    dev = max(abs(ff(t + T) - ff(t)) for t in XS)
    if dev < best:
        best, bestT = dev, T
    k += 1
chk('ไม่มี T ใดใน [0.5 , 12pi-0.5] ที่เป็นคาบ', best > 0.2,
    'เบี่ยงเบนต่ำสุด %.4f ที่ T = %.4f' % (best, bestT))
chk('ที่ T = 12pi พอดี ผลต่างเป็นศูนย์เชิงตัวเลข',
    max(abs(ff(t + TWELVE) - ff(t)) for t in XS) < 1e-9)
chk('ที่ T เล็ก ๆ (0.01) ไม่เป็นคาบ แม้ผลต่างจะเล็ก',
    0 < max(abs(ff(t + 0.01) - ff(t)) for t in XS) < 0.02,
    '%.5f' % max(abs(ff(t + 0.01) - ff(t)) for t in XS))

print()
print('q042 · ยุบ sin(atan(3/4)) และ cos(atan(3/4)) ให้เป็นเศษส่วน')
a = atan(Rational(3, 4))
sv = simplify(expand_trig(sin(a)))
cv = simplify(expand_trig(cos(a)))
print('   sin(atan(3/4)) =', sv, '| cos(atan(3/4)) =', cv)
chk('sin(theta) = 3/5', sv == Rational(3, 5), sv)
chk('cos(theta) = 4/5', cv == Rational(4, 5), cv)
chk('tan(theta) = 3/4', simplify(tan(a)) == Rational(3, 4))
chk('แทนกลับ 3 sin + 4 cos = 5', simplify(3 * sv + 4 * cv - 5) == 0)
good = []
for kk in range(-3, 4):
    v = simplify(expand_trig(sin(a + 2 * kk * pi)))
    good.append(v == Rational(3, 5))
chk('คำตอบทั่วไป theta = atan(3/4) + 2k pi ให้ sin = 3/5 ทุก k', all(good), good)
sset = solveset(Eq(3 * sin(th) + 4 * cos(th), 5), th, S.Reals)
chk('solveset คืนคำตอบเป็นตระกูลเดียว (ไม่มีสองตระกูล) ⇒ sin ไม่กำกวม',
    isinstance(sset, ImageSet), sset)

print()
print('=' * 70)
print('ผ่าน %d / %d' % (sum(1 for v in ok if v), len(ok)))

# -*- coding: utf-8 -*-
"""STEP D + E · ก้อน 7 · q040-q044 · ตรวจคำตอบและเส้นทางตัวลวงทุกเส้นด้วย sympy/ตัวเลข"""
from sympy import *
import math

ok = []


def chk(tag, cond, extra=''):
    ok.append(bool(cond))
    print(('  OK  ' if cond else '  FAIL') + ' | ' + tag + (' | ' + str(extra) if extra else ''))


x, th, u = symbols('x theta u', real=True)

print('=' * 74)
print('q040 · คาบของ f(x) = sin(x/2) + cos(x/3)')
print('=' * 74)
f = sin(x / 2) + cos(x / 3)
chk('คาบของ sin(x/2) = 4pi', simplify(periodicity(sin(x / 2), x) - 4 * pi) == 0,
    periodicity(sin(x / 2), x))
chk('คาบของ cos(x/3) = 6pi', simplify(periodicity(cos(x / 3), x) - 6 * pi) == 0,
    periodicity(cos(x / 3), x))
chk('f(x + 12pi) = f(x) ทุก x', simplify(f.subs(x, x + 12 * pi) - f) == 0)
for T, name in [(4 * pi, '4pi'), (6 * pi, '6pi'), (10 * pi, '10pi')]:
    d = simplify(f.subs(x, x + T) - f)
    chk('T = %s ใช้ไม่ได้ (ผลต่างไม่เป็นศูนย์)' % name, d != 0, 'ผลต่าง = %s' % d)

ff = lambda t: math.sin(t / 2) + math.cos(t / 3)
XS = [i * 0.137 for i in range(1, 400)]
best, bestT = 9e9, None
Ts = [k * 12 * math.pi / 4000 for k in range(1, 4000)]   # T ใน (0, 12pi) ไม่รวมปลาย
for T in Ts:
    dev = max(abs(ff(t + T) - ff(t)) for t in XS[:60])
    if dev < best:
        best, bestT = dev, T
chk('ไม่มี T ใด ๆ ใน (0, 12pi) ที่ทำให้ f เป็นคาบ', best > 0.05,
    'ค่าเบี่ยงเบนต่ำสุดที่พบ = %.4f ที่ T = %.4f' % (best, bestT))
chk('ตรวจอิสระ · f(0) = f(12pi) และ f(1) = f(1+12pi) เชิงตัวเลข',
    abs(ff(0) - ff(12 * math.pi)) < 1e-9 and abs(ff(1) - ff(1 + 12 * math.pi)) < 1e-9)
chk('ตัวเลือกสี่ตัวต่างกัน', len({4, 6, 10, 12}) == 4)

print()
print('=' * 74)
print('q041 · ส่วนโค้งยาว 670 หน่วย วัดทวนเข็มจากจุด (1, 0) บนวงกลมหนึ่งหน่วย')
print('=' * 74)
L = 670
TAU = 2 * math.pi
k = int(L // TAU)
r = L - k * TAU
print('   จำนวนรอบเต็ม =', k, '| มุมเหลือ = %.6f เรเดียน = %.6f pi' % (r, r / math.pi))
chk('มุมเหลืออยู่ระหว่าง pi กับ 3pi/2 ⇒ จตุภาคที่ 3',
    math.pi < r < 1.5 * math.pi, '%.4f' % r)
chk('ห่างขอบจตุภาคอย่างน้อย 0.5 เรเดียน (ทนต่อการปัด pi)',
    min(r - math.pi, 1.5 * math.pi - r) > 0.5,
    'ห่าง %.4f' % min(r - math.pi, 1.5 * math.pi - r))
r314 = L - int(L // (2 * 3.14)) * (2 * 3.14)
chk('ใช้ pi = 3.14 หยาบ ๆ ก็ยังได้จตุภาค 3', 3.14 < r314 < 1.5 * 3.14, '%.4f' % r314)
chk('ตรวจอิสระ · sin ลบ และ cos ลบ (เครื่องหมายของจตุภาค 3)',
    math.sin(L) < 0 and math.cos(L) < 0,
    'sin = %.4f , cos = %.4f' % (math.sin(L), math.cos(L)))
# เส้นทางตัวลวง
d = L % 360
chk('ตัวลวง · คิดว่า 670 เป็นองศา ⇒ 310 องศา ⇒ จตุภาค 4', 270 < d < 360, '%.1f องศา' % d)
cw = (-r) % TAU
chk('ตัวลวง · วัดตามเข็มนาฬิกา ⇒ จตุภาค 2', math.pi / 2 < cw < math.pi, '%.4f' % cw)
mp = L % math.pi
chk('ตัวลวง · ลบด้วย pi แทน 2pi (คิดว่าครบรอบคือ pi) ⇒ จตุภาค 1',
    0 < mp < math.pi / 2, '%.4f' % mp)

print()
print('=' * 74)
print('q042 · 3 sin(theta) + 4 cos(theta) = 5 ⇒ หา sin(theta)')
print('=' * 74)
sols = solve(Eq(3 * sin(th) + 4 * cos(th), 5), th)
print('   sympy solve ⇒', sols)
vals = sorted({simplify(sin(s)) for s in sols})
chk('คำตอบของ sin(theta) มีค่าเดียวคือ 3/5', vals == [Rational(3, 5)], vals)
cvals = sorted({simplify(cos(s)) for s in sols})
chk('cos(theta) = 4/5', cvals == [Rational(4, 5)], cvals)
c = symbols('c', real=True)
poly = expand((5 - 4 * c)**2 - 9 * (1 - c**2))
chk('แทน sin = (5-4c)/3 ลง sin^2 + cos^2 = 1 ได้ 25c^2 - 40c + 16 = 0',
    simplify(poly - (25 * c**2 - 40 * c + 16)) == 0, factor(poly))
chk('พหุนามเป็นกำลังสองสมบูรณ์ (5c-4)^2 ⇒ รากซ้ำ ⇒ theta ไม่กำกวม',
    factor(poly) == (5 * c - 4)**2, factor(poly))
s_ = symbols('s', real=True)
poly2 = expand((5 - 3 * s_)**2 - 16 * (1 - s_**2))
chk('ตรวจอิสระ · แก้ในตัวแปร sin ได้ 25s^2 - 30s + 9 = (5s-3)^2',
    factor(poly2) == (5 * s_ - 3)**2, factor(poly2))
chk('ตรวจอิสระ · แทนกลับ 3(3/5) + 4(4/5) = 5',
    simplify(3 * Rational(3, 5) + 4 * Rational(4, 5)) == 5)
chk('ตัวลวง · ตอบ cos แทน sin ⇒ 4/5', Rational(4, 5) != Rational(3, 5))
chk('ตัวลวง · ตอบ tan = sin/cos ⇒ 3/4',
    simplify(Rational(3, 5) / Rational(4, 5)) == Rational(3, 4))
chk('ตัวลวง · ตอบ cot = cos/sin ⇒ 4/3',
    simplify(Rational(4, 5) / Rational(3, 5)) == Rational(4, 3))
chk('ตัวเลือกสี่ตัวต่างกันจริง',
    len({Rational(3, 5), Rational(3, 4), Rational(4, 5), Rational(4, 3)}) == 4)

print()
print('=' * 74)
print('q043 · จำนวนคำตอบของสมการ sin x = x/10')
print('=' * 74)
g = lambda t: math.sin(t) - t / 10.0
roots = []
N = 2000000
lo, hi = -11.0, 11.0
prev_t, prev_v = lo, g(lo)
for i in range(1, N + 1):
    t = lo + (hi - lo) * i / N
    v = g(t)
    if v == 0.0:
        roots.append(t)
    elif prev_v * v < 0:
        a, b = prev_t, t
        for _ in range(80):
            m = (a + b) / 2
            if g(a) * g(m) <= 0:
                b = m
            else:
                a = m
        roots.append((a + b) / 2)
    prev_t, prev_v = t, v
roots = sorted(roots)
merged = []
for rr in roots:
    if not merged or abs(rr - merged[-1]) > 1e-6:
        merged.append(rr)
print('   รากที่พบ:', ['%.6f' % rr for rr in merged])
chk('มีคำตอบทั้งหมด 7 จำนวน', len(merged) == 7, len(merged))
chk('ทุกรากอยู่ในช่วง [-10, 10] (ขอบเขตจาก |sin x| <= 1)',
    all(abs(rr) <= 10 + 1e-9 for rr in merged))
chk('รากสมมาตรรอบศูนย์ (ฟังก์ชันคี่)',
    all(abs(merged[i] + merged[-1 - i]) < 1e-6 for i in range(len(merged))))
chk('มีรากที่ x = 0', any(abs(rr) < 1e-9 for rr in merged))
pos = [rr for rr in merged if rr > 1e-9]
chk('รากบวกมี 3 จำนวน', len(pos) == 3, ['%.4f' % v for v in pos])
chk('รากบวกหนึ่งตัวอยู่ใน (0, pi)',
    len([v for v in pos if 0 < v < math.pi]) == 1)
chk('ไม่มีรากใน (pi, 2pi) เพราะ sin ติดลบแต่เส้นตรงเป็นบวก',
    len([v for v in pos if math.pi < v < 2 * math.pi]) == 0)
chk('มีรากสองตัวใน (2pi, 3pi)',
    len([v for v in pos if 2 * math.pi < v < 3 * math.pi]) == 2)
chk('ไม่มีรากใน (3pi, 10] เพราะ sin ติดลบ',
    len([v for v in pos if 3 * math.pi < v <= 10]) == 0)
chk('ตัวลวง 3 · นับเฉพาะช่วง [-pi, pi]',
    len([rr for rr in merged if abs(rr) <= math.pi]) == 3)
chk('ตัวลวง 9 · ถ้าเข้าใจผิดว่าลูกคลื่นทุกลูกใน [-10,10] ตัดลูกละ 2 จุด บวกรากศูนย์ ⇒ 9',
    2 * 4 + 1 == 9)
chk('ตัวลวง 5 · ถ้าเข้าใจผิดว่าลูกคลื่นตัดลูกละ 1 จุด (บวก/ลบ อย่างละ 2) บวกรากศูนย์ ⇒ 5',
    2 * 2 + 1 == 5)

print()
print('=' * 74)
print('q044 · ค่าต่ำสุดของ f(x) = sin^2 x - 4 sin x + 3')
print('=' * 74)
F = u**2 - 4 * u + 3
chk('จัดรูปกำลังสองสมบูรณ์ได้ (u-2)^2 - 1', simplify(F - ((u - 2)**2 - 1)) == 0)
chk('จุดยอดอยู่ที่ u = 2 ซึ่งอยู่นอกช่วง [-1, 1]', 2 > 1)
chk('f ลดลงตลอดช่วง [-1, 1] (อนุพันธ์ 2u-4 < 0)',
    all((2 * v - 4) < 0 for v in [-1, 0, 1]))
chk('ค่าต่ำสุดที่ u = 1 คือ 0', F.subs(u, 1) == 0, F.subs(u, 1))
chk('ค่าสูงสุดที่ u = -1 คือ 8', F.subs(u, -1) == 8, F.subs(u, -1))
mm = minimum(sin(x)**2 - 4 * sin(x) + 3, x, S.Reals)
chk('sympy minimum บนจำนวนจริงทั้งหมด = 0', simplify(mm) == 0, mm)
MM = maximum(sin(x)**2 - 4 * sin(x) + 3, x, S.Reals)
chk('sympy maximum บนจำนวนจริงทั้งหมด = 8', simplify(MM) == 8, MM)
gg = lambda t: math.sin(t)**2 - 4 * math.sin(t) + 3
mn = min(gg(i * 0.0001) for i in range(0, 100000))
chk('สแกนเชิงตัวเลขบน [0, 10] ได้ค่าต่ำสุด ~ 0', abs(mn - 0) < 1e-6, '%.8f' % mn)
chk('ตัวลวง -1 · ใช้ค่าจุดยอดโดยลืมว่า |sin x| <= 1', F.subs(u, 2) == -1)
chk('ตัวลวง 3 · แทน sin x = 0', F.subs(u, 0) == 3)
chk('ตัวลวง 8 · ตอบค่าสูงสุดแทนค่าต่ำสุด (u = -1)', F.subs(u, -1) == 8)
chk('ตัวเลือกสี่ตัวต่างกันจริง', len({-1, 0, 3, 8}) == 4)

print()
print('=' * 74)
print('ผ่าน %d / %d' % (sum(1 for v in ok if v), len(ok)))
print('=' * 74)

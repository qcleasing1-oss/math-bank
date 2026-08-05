# -*- coding: utf-8 -*-
"""ตรวจก้อน 9 (q050-q054) ด้วย sympy · ทุกคำตอบและทุกตัวลวงต้องผ่านก่อนเขียนไฟล์

⛔ ห้ามข้าม (กฎเหล็กข้อ 1) · ตัวลวงทุกตัวต้องคำนวณจากเส้นทางผิดจริง ไม่ใช่เลขใกล้เคียง
"""
import sympy as sp

ok = fail = 0


def chk(label, got, want):
    global ok, fail
    g = sp.simplify(got - want)
    good = (g == 0)
    print('%-4s %-64s %s' % ('✅' if good else '❌', label, sp.srepr(sp.nsimplify(got))[:0] or sp.simplify(got)))
    if good:
        ok += 1
    else:
        fail += 1
        print('     ⛔ ควรได้ %s' % want)


def chkb(label, cond):
    global ok, fail
    print('%-4s %s' % ('✅' if cond else '❌', label))
    if cond:
        ok += 1
    else:
        fail += 1


x, t = sp.symbols('x t', real=True)
pi = sp.pi

print('═' * 78)
print('q050 · f(x) = (arcsin x)^2 + (arccos x)^2 บน [-1, 1] · ถามผลต่าง max - min')
print('═' * 78)
f = sp.asin(x) ** 2 + sp.acos(x) ** 2

# แทน u = arcsin x  ⇒ arccos x = pi/2 - u และ u วิ่งบน [-pi/2, pi/2]
u = sp.symbols('u', real=True)
g = u ** 2 + (pi / 2 - u) ** 2
chk('ยุบเป็นพหุนามกำลังสองใน u ได้ 2u^2 - pi*u + pi^2/4',
    sp.expand(g), sp.expand(2 * u ** 2 - pi * u + pi ** 2 / 4))
# ยืนยันว่าการแทนนี้ถูกจริงทุกจุด (ไม่ใช่แค่เชิงสัญลักษณ์)
import random
random.seed(9)
bad = [v for v in [-1, -0.7, -0.3, 0, 0.25, 0.6, 0.9, 1] + [random.uniform(-1, 1) for _ in range(40)]
       if abs(float(f.subs(x, v)) - float(g.subs(u, sp.asin(v)))) > 1e-12]
chkb('แทน u = arcsin x แล้วค่าตรงกันทุกจุดที่สุ่มมา 48 จุด', not bad)

vertex = sp.solve(sp.diff(g, u), u)[0]
chk('จุดยอดของพาราโบลาอยู่ที่ u = pi/4', vertex, pi / 4)
chkb('จุดยอดอยู่ในช่วง [-pi/2, pi/2] จริง ⇒ ใช้เป็นค่าต่ำสุดได้', -pi / 2 <= vertex <= pi / 2)

fmin = sp.simplify(g.subs(u, pi / 4))
fmax = sp.Max(sp.simplify(g.subs(u, -pi / 2)), sp.simplify(g.subs(u, pi / 2)))
chk('ค่าต่ำสุด = pi^2/8', fmin, pi ** 2 / 8)
chk('ค่าสูงสุด = 5pi^2/4 (ที่ปลาย u = -pi/2 คือ x = -1)', fmax, 5 * pi ** 2 / 4)
chk('f(-1) = 5pi^2/4', f.subs(x, -1), 5 * pi ** 2 / 4)
chk('f(1)  = pi^2/4', f.subs(x, 1), pi ** 2 / 4)
chk('f(sqrt2/2) = pi^2/8', sp.simplify(f.subs(x, sp.sqrt(2) / 2)), pi ** 2 / 8)
chk('คำตอบ · ผลต่าง max - min = 9pi^2/8', sp.simplify(fmax - fmin), 9 * pi ** 2 / 8)

# ยืนยันสุดขีดด้วยการกวาดตัวเลข (วิธีอิสระ)
vals = [float(f.subs(x, -1 + 2 * i / 4000)) for i in range(4001)]
chkb('กวาดตัวเลข 4001 จุด: ต่ำสุด ≈ pi^2/8', abs(min(vals) - float(pi ** 2 / 8)) < 1e-6)
chkb('กวาดตัวเลข 4001 จุด: สูงสุด ≈ 5pi^2/4', abs(max(vals) - float(5 * pi ** 2 / 4)) < 1e-9)

print('-- ตัวลวง q050 --')
chk('ตัวลวง ก · เชื่อว่า (arcsin)^2+(arccos)^2 = (arcsin+arccos)^2 = pi^2/4 คงที่ ⇒ ผลต่าง 0',
    sp.simplify((pi / 2) ** 2 - (pi / 2) ** 2), sp.Integer(0))
chk('ตัวลวง ข · จำเรนจ์ arcsin ผิดเป็น [0, pi/2] ⇒ สูงสุด pi^2/4 ⇒ ผลต่าง pi^2/8',
    sp.simplify(pi ** 2 / 4 - pi ** 2 / 8), pi ** 2 / 8)
chk('ตัวลวง ค · ดูแต่ปลายช่วง ไม่ดูจุดยอด ⇒ 5pi^2/4 - pi^2/4 = pi^2',
    sp.simplify(5 * pi ** 2 / 4 - pi ** 2 / 4), pi ** 2)
chkb('ตัวเลือกทั้งสี่ไม่ซ้ำค่ากัน',
     len({sp.nsimplify(v) for v in [0, pi ** 2 / 8, pi ** 2, 9 * pi ** 2 / 8]}) == 4)

print()
print('═' * 78)
print('q051 · เรียงลำดับค่าของสี่ปริมาณที่มี arc (สามอันต้องพับเข้าช่วงหลัก)')
print('═' * 78)
a = sp.asin(sp.sin(5 * pi / 6))
b = sp.acos(sp.cos(-pi / 3))
c = sp.atan(sp.tan(3 * pi / 4))
d = sp.acos(sp.Rational(-1, 2))
chk('a = arcsin(sin 5pi/6) = pi/6', a, pi / 6)
chk('b = arccos(cos(-pi/3)) = pi/3', b, pi / 3)
chk('c = arctan(tan 3pi/4) = -pi/4', c, -pi / 4)
chk('d = arccos(-1/2) = 2pi/3', d, 2 * pi / 3)
order = sorted([('a', a), ('b', b), ('c', c), ('d', d)], key=lambda p: float(p[1]))
chkb('คำตอบ · เรียงจากน้อยไปมากได้ c < a < b < d',
     [p[0] for p in order] == ['c', 'a', 'b', 'd'])
# ค่าที่ "ข้างใน" จริง ๆ ต้องอยู่นอกช่วงหลัก มิฉะนั้นข้อนี้ไม่มีกับดัก
chkb('5pi/6 อยู่นอกเรนจ์ของ arcsin ⇒ ต้องพับจริง', not (-pi / 2 <= 5 * pi / 6 <= pi / 2))
chkb('-pi/3 อยู่นอกเรนจ์ของ arccos ⇒ ต้องพับจริง', not (0 <= -pi / 3 <= pi))
chkb('3pi/4 อยู่นอกเรนจ์ของ arctan ⇒ ต้องพับจริง', not (-pi / 2 < 3 * pi / 4 < pi / 2))
print('-- ตัวลวง q051 --')
naive = sorted([('a', 5 * pi / 6), ('b', -pi / 3), ('c', 3 * pi / 4), ('d', 2 * pi / 3)],
               key=lambda p: float(p[1]))
chkb('ตัวลวง ก · เชื่อว่า arc ล้างฟังก์ชันข้างในทิ้งได้เลย ⇒ b < d < c < a',
     [p[0] for p in naive] == ['b', 'd', 'c', 'a'])
e2 = sorted([('a', pi / 6), ('b', pi / 3), ('c', 3 * pi / 4), ('d', 2 * pi / 3)],
            key=lambda p: float(p[1]))
chkb('ตัวลวง ข · ใช้เรนจ์ arctan ผิดเป็น (0, pi) ⇒ a < b < d < c',
     [p[0] for p in e2] == ['a', 'b', 'd', 'c'])
e3 = sorted([('a', pi / 6), ('b', -pi / 3), ('c', -pi / 4), ('d', 2 * pi / 3)],
            key=lambda p: float(p[1]))
chkb('ตัวลวง ค · คิดว่า arccos คืนค่าลบตามมุมลบข้างใน ⇒ b < c < a < d',
     [p[0] for p in e3] == ['b', 'c', 'a', 'd'])

print()
print('═' * 78)
print('q052 · โดเมนของ f(x) = arcsin(x^2 - 2x)')
print('═' * 78)
inner = x ** 2 - 2 * x
sol = (sp.solveset(inner >= -1, x, sp.S.Reals)
       .intersect(sp.solveset(inner <= 1, x, sp.S.Reals)))
print('   sympy ให้โดเมน =', sol)
chkb('คำตอบ · โดเมน = [1-sqrt2, 1+sqrt2]',
     sol == sp.Interval(1 - sp.sqrt(2), 1 + sp.sqrt(2)))
chkb('ด้านล่าง x^2-2x >= -1 เป็นจริงทุกจำนวนจริง (เพราะ (x-1)^2 >= 0)',
     sp.solveset(inner + 1 >= 0, x, sp.S.Reals) == sp.S.Reals)
chkb('x = 1 อยู่ในโดเมน (จุดที่ (x-1)^2 = 0 พอดี — ห้ามตัดทิ้ง)',
     (1 - sp.sqrt(2) <= 1) and (1 <= 1 + sp.sqrt(2)) and abs(float(inner.subs(x, 1))) <= 1)
chk('ที่ x = 1 ได้ arcsin(-1) = -pi/2 (นิยามได้จริง)', sp.asin(inner.subs(x, 1)), -pi / 2)
chk('ที่ปลาย x = 1+sqrt2 ได้ x^2-2x = 1', sp.simplify(inner.subs(x, 1 + sp.sqrt(2))), sp.Integer(1))
chk('ที่ปลาย x = 1-sqrt2 ได้ x^2-2x = 1', sp.simplify(inner.subs(x, 1 - sp.sqrt(2))), sp.Integer(1))
print('-- ตัวลวง q052 --')
chkb('ตัวลวง ก · [-1, 1] · ยกโดเมนของ arcsin มาเป็นโดเมนของ f เลย · x=-1 ต้องหลุดจริง',
     abs(float(inner.subs(x, -1))) > 1)
chkb('ตัวลวง ข · ตัด x=1 ทิ้งเพราะแก้ (x-1)^2 > 0 แบบเข้ม ⇒ โดเมนขาดหนึ่งจุด',
     abs(float(inner.subs(x, 1))) <= 1)
chkb('ตัวลวง ค · แก้อสมการกลับข้างเป็น x^2-2x-1 >= 0 ⇒ ได้ส่วนนอกช่วง',
     sp.solveset(inner - 1 >= 0, x, sp.S.Reals) ==
     sp.Union(sp.Interval(-sp.oo, 1 - sp.sqrt(2)), sp.Interval(1 + sp.sqrt(2), sp.oo)))

print()
print('═' * 78)
print('q053 · มุม A = 30 องศา · CA = 8 · BC = k · หา k จำนวนเต็มบวกที่สร้างได้สองรูป ⇒ ผลบวก k')
print('═' * 78)
A = pi / 6
bb = sp.Integer(8)                      # b = CA ตรงข้ามมุม B · a = BC = k ตรงข้ามมุม A
h = sp.simplify(bb * sp.sin(A))
chk('ความสูงจาก C ลงฐาน AB คือ h = b sin A = 4', h, sp.Integer(4))

cc = sp.symbols('c', positive=True)


def ntri(kval):
    """นับรูปสามเหลี่ยมจริง ๆ จากจำนวนรากบวกของสมการกฎโคไซน์ c^2 - 2b cosA c + (b^2 - a^2) = 0"""
    poly = sp.Eq(sp.Integer(kval) ** 2, bb ** 2 + cc ** 2 - 2 * bb * cc * sp.cos(A))
    rs = sp.solve(poly, cc)
    rs = [sp.simplify(r) for r in rs if r.is_real and float(r) > 0]
    return len({sp.nsimplify(r) for r in rs})


table = {k: ntri(k) for k in range(1, 13)}
print('   k : จำนวนรูป =', table)
two = sorted(k for k, n in table.items() if n == 2)
chkb('กวาด k = 1..12 แล้วได้สองรูปเฉพาะ k = 5, 6, 7', two == [5, 6, 7])
chkb('k = 1, 2, 3 สร้างไม่ได้เลย (สั้นกว่าความสูง h = 4)',
     all(table[k] == 0 for k in (1, 2, 3)))
chkb('k = 4 ได้รูปเดียว (a = h พอดี ⇒ มุม B เป็นมุมฉาก รากซ้ำ)', table[4] == 1)
chkb('k = 8 ได้รูปเดียว (a = b ⇒ รูปหน้าจั่ว · อีกรากคือ c = 0 ใช้ไม่ได้)', table[8] == 1)
chkb('k = 9, 10, 11, 12 ได้รูปเดียวทุกค่า (a > b)',
     all(table[k] == 1 for k in (9, 10, 11, 12)))
chkb('เงื่อนไขเชิงทฤษฎี h < a < b ⇔ 4 < k < 8 ตรงกับผลกวาดทุกค่า',
     [k for k in range(1, 13) if 4 < k < 8] == two)
chk('คำตอบ · ผลบวกของ k ทั้งหมด = 5 + 6 + 7 = 18', sp.Integer(sum(two)), sp.Integer(18))

# ตรวจซ้ำเชิงเรขา: k = 6 ต้องได้ AB สองค่าที่ต่างกันจริง และคืนค่า BC = 6 ทั้งคู่
rs6 = sorted([sp.simplify(r) for r in
              sp.solve(sp.Eq(sp.Integer(6) ** 2, bb ** 2 + cc ** 2 - 2 * bb * cc * sp.cos(A)), cc)],
             key=lambda r: float(r))
chkb('k = 6 ให้ AB สองค่าที่ต่างกันจริง', len(rs6) == 2 and float(rs6[1] - rs6[0]) > 1e-9)
for r in rs6:
    chk('ตรวจย้อน k = 6 · รูปที่ AB = %.6f ให้ BC = 6 จริง' % float(r),
        sp.simplify(sp.sqrt(bb ** 2 + r ** 2 - 2 * bb * r * sp.cos(A))), sp.Integer(6))
    chkb('อสมการสามเหลี่ยมของรูปที่ AB = %.6f' % float(r),
         float(r) + 6 > 8 and float(r) + 8 > 6 and 14 > float(r))
sinB6 = sp.simplify(bb * sp.sin(A) / sp.Integer(6))
chk('sin B = 2/3 เท่ากันทั้งสองรูปเมื่อ k = 6', sinB6, sp.Rational(2, 3))
B1 = sp.asin(sinB6)
chkb('มุม B สองค่าคือ B1 (แหลม) กับ pi - B1 (ป้าน) และรวมกับ A แล้วยังน้อยกว่า pi ทั้งคู่',
     float(A + B1) < float(pi) and float(A + (pi - B1)) < float(pi))
print('-- ตัวลวง q053 --')
chkb('ตัวลวง ก · นับ k = 8 เข้าไปด้วย (คิดว่า a = b ก็ยังกำกวม) ⇒ 5+6+7+8 = 26',
     sum(two) + 8 == 26 and table[8] == 1)
chkb('ตัวลวง ข · นับ k = 4 เข้าไปด้วย (คิดว่าจุดสัมผัสให้สองรูป) ⇒ 4+5+6+7 = 22',
     sum(two) + 4 == 22 and table[4] == 1)
chkb('ตัวลวง ค · ตอบ “จำนวนค่าของ k” แทนผลบวก ⇒ 3', len(two) == 3)
chkb('ตัวเลือกทั้งสี่ไม่ซ้ำค่ากัน', len({3, 22, 26, 18}) == 4)

print()
print('═' * 78)
print('q054 · สี่เหลี่ยม ABCD · AB=3 BC=5 CD=2 DA=3 · มุม ABC + มุม ADC = 180 ⇒ พื้นที่')
print('═' * 78)
AB, BC, CD, DA = sp.Integer(3), sp.Integer(5), sp.Integer(2), sp.Integer(3)
Bang = sp.symbols('B', positive=True)
cB = sp.symbols('cB', real=True)
# AC^2 จากสามเหลี่ยม ABC และจากสามเหลี่ยม ACD (โดย cos D = -cos B)
lhs = AB ** 2 + BC ** 2 - 2 * AB * BC * cB
rhs = CD ** 2 + DA ** 2 - 2 * CD * DA * (-cB)
solB = sp.solve(sp.Eq(lhs, rhs), cB)
chkb('แก้ได้ค่าเดียว', len(solB) == 1)
chk('cos B = 1/2 ⇒ มุม B = 60 องศา', solB[0], sp.Rational(1, 2))
cBv = solB[0]
AC2 = sp.simplify(lhs.subs(cB, cBv))
chk('AC^2 = 19 (คิดจากสามเหลี่ยม ABC)', AC2, sp.Integer(19))
chk('AC^2 = 19 (คิดจากสามเหลี่ยม ACD ด้วย cos D = -1/2)',
    sp.simplify(rhs.subs(cB, cBv)), sp.Integer(19))
sB = sp.sqrt(1 - cBv ** 2)
area = sp.simplify(sp.Rational(1, 2) * AB * BC * sB + sp.Rational(1, 2) * CD * DA * sB)
chk('คำตอบ · พื้นที่ = 21sqrt3/4', area, 21 * sp.sqrt(3) / 4)
# วิธีอิสระ: สูตรพรหมคุปต์ (ใช้ได้เพราะมุมตรงข้ามรวม 180 ⇒ แนบในวงกลม)
s = sp.Rational(AB + BC + CD + DA, 2)
brahma = sp.sqrt((s - AB) * (s - BC) * (s - CD) * (s - DA))
chk('ตรวจอิสระด้วยสูตรพรหมคุปต์ได้ค่าเดียวกัน', sp.simplify(brahma - area), sp.Integer(0))
chkb('รูปสามเหลี่ยม ABC ใช้ได้จริง (อสมการสามเหลี่ยม)',
     3 + 5 > float(sp.sqrt(19)) and 3 + float(sp.sqrt(19)) > 5 and 5 + float(sp.sqrt(19)) > 3)
chkb('รูปสามเหลี่ยม ACD ใช้ได้จริง (อสมการสามเหลี่ยม)',
     2 + 3 > float(sp.sqrt(19)) and 2 + float(sp.sqrt(19)) > 3 and 3 + float(sp.sqrt(19)) > 2)
chkb('มุม D = 120 องศา (จาก cos D = -1/2)', sp.acos(-cBv) == 2 * pi / 3)
print('-- ตัวลวง q054 --')
chk('ตัวลวง ก · คิดพื้นที่แค่สามเหลี่ยม ACD = 3sqrt3/2',
    sp.simplify(sp.Rational(1, 2) * CD * DA * sB), 3 * sp.sqrt(3) / 2)
chk('ตัวลวง ข · คิดพื้นที่แค่สามเหลี่ยม ABC = 15sqrt3/4',
    sp.simplify(sp.Rational(1, 2) * AB * BC * sB), 15 * sp.sqrt(3) / 4)
chk('ตัวลวง ค · ลืมครึ่งในสูตรพื้นที่ ⇒ 21sqrt3/2',
    sp.simplify(AB * BC * sB + CD * DA * sB), 21 * sp.sqrt(3) / 2)
chkb('ตัวเลือกทั้งสี่ไม่ซ้ำค่ากัน',
     len({sp.nsimplify(v) for v in [3 * sp.sqrt(3) / 2, 15 * sp.sqrt(3) / 4,
                                    21 * sp.sqrt(3) / 4, 21 * sp.sqrt(3) / 2]}) == 4)

print()
print('═' * 78)
print('รวม ✅ %d จุด · ❌ %d จุด' % (ok, fail))
print('═' * 78)
raise SystemExit(1 if fail else 0)

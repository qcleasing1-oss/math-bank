# -*- coding: utf-8 -*-
"""STEP D · sympy verify ของ 3 ข้อระดับ ปานกลาง (7.1 · 7.2 · 7.3)
ทุกตัวลวงต้องคำนวณจากเส้นทางพลาดจริง ⛔ ห้ามเดาเลขใกล้เคียง"""
import sympy as sp

print('=' * 74)
print('M-1 · 7.1 · sec θ − tan θ = 1/3 , θ แหลม  ⇒  sin θ = ?')
print('=' * 74)
th = sp.symbols('theta', positive=True)
eq = sp.Eq(sp.sec(th) - sp.tan(th), sp.Rational(1, 3))
sols = sp.solve(eq, th)
print('solve ตรง ๆ :', sols)
for s in sols:
    sv = complex(sp.N(s))
    assert abs(sv.imag) < 1e-12, sv           # รูปที่ sympy คืนมาเป็น log เชิงซ้อน แต่ค่าจริงเป็นจำนวนจริง
    r = sv.real
    print('   θ ≈', r, 'rad = ', r * 180 / 3.141592653589793, '°',
          '· sin ≈', sp.N(sp.sin(s)), '· cos ≈', sp.N(sp.cos(s)),
          '· tan ≈', sp.N(sp.tan(s)))
    print('   θ = atan(4/3) ?', abs(r - float(sp.atan(sp.Rational(4, 3)))) < 1e-12)
print('ตรวจย้อน sec−tan ที่ sinθ=4/5, cosθ=3/5 :',
      sp.simplify(1 / sp.Rational(3, 5) - sp.Rational(4, 5) / sp.Rational(3, 5)))

# เส้นทางที่ 1 (เส้นทางหลักในเฉลย) — คอนจูเกต
s_, c_ = sp.symbols('s c', real=True)
sec_, tan_ = 1 / c_, s_ / c_
prod = sp.simplify((sec_ - tan_) * (sec_ + tan_))
print('\n(sec−tan)(sec+tan) = sec²−tan² =', sp.simplify(prod.subs(c_**2, 1 - s_**2)))
print('  ⇒ sec+tan = 3 · sec−tan = 1/3  ⇒ sec = 5/3 , tan = 4/3')
print('  cos = 3/5 ⇒ sin = sqrt(1−9/25) =', sp.sqrt(1 - sp.Rational(9, 25)))

# เส้นทางที่ 2 (ตัวตรวจอิสระ) — ยกกำลังสอง แล้วต้องตัดรากแปลกปลอม
S = sp.symbols('S', real=True)
quad = sp.expand((3 * (1 - S))**2 - (1 - S**2))
print('\nยกกำลังสองจาก 3(1−sin) = cos  ⇒', sp.factor(quad), '= 0')
print('  ราก:', sp.solve(sp.Eq(quad, 0), S))
for r in sp.solve(sp.Eq(quad, 0), S):
    ok = sp.simplify(3 * (1 - r) - sp.sqrt(1 - r**2))
    print('   S =', r, '· ตรวจย้อน 3(1−S) − cos =', ok,
          '⇒', 'ใช้ได้' if ok == 0 else 'รากแปลกปลอม')
print('  S = 1 ⇒ cos = 0 ⇒ sec/tan ไม่นิยาม ⇒ ตัดทิ้ง (ขั้นแยกกรณีจริง)')

print('\nค่าตัวลวงที่คำนวณได้จริง:')
print('   sin = 4/5 ✅  · cos = 3/5 (ตอบโคไซน์)  · cot = 3/4 (กลับส่วนของ tan)  · sec = 5/3 (ตอบซีแคนต์)')
vals = [sp.Rational(3, 5), sp.Rational(3, 4), sp.Rational(4, 5), sp.Rational(5, 3)]
print('   เรียงจากน้อยไปมาก:', vals, '⇒ ดัชนีคำตอบ', vals.index(sp.Rational(4, 5)))
assert vals == sorted(vals) and len(set(vals)) == 4

print()
print('=' * 74)
print('M-2 · 7.2 · ปลายส่วนโค้ง θ = (−5/13, −12/13) ⇒ ปลายส่วนโค้ง π/2 − θ = ?')
print('=' * 74)
c0, s0 = sp.Rational(-5, 13), sp.Rational(-12, 13)
print('cos θ =', c0, '· sin θ =', s0, '· ตรวจ cos²+sin² =', sp.simplify(c0**2 + s0**2))
t = sp.symbols('t', real=True)
th0 = sp.atan2(s0, c0)
print('θ ≈', float(th0 % (2 * sp.pi)), 'rad · จตุภาคที่ 3 ✓')


def endpoint(expr):
    return (sp.simplify(sp.cos(expr)), sp.simplify(sp.sin(expr)))


for name, ex in [('π/2 − θ  ✅ คำตอบ', sp.pi / 2 - th0),
                 ('−θ        (สะท้อนแกน x)', -th0),
                 ('θ + π     (จุดตรงข้าม)', th0 + sp.pi),
                 ('θ − π/2   (สลับพิกัดผิดเครื่องหมาย)', th0 - sp.pi / 2)]:
    x, y = endpoint(ex)
    print('  %-28s ⇒ (%s , %s)' % (name, sp.nsimplify(x, rational=True), sp.nsimplify(y, rational=True)))

print('\nเอกลักษณ์ที่ใช้: cos(π/2−θ) = sin θ · sin(π/2−θ) = cos θ')
print('  ตรวจเชิงสัญลักษณ์:', sp.simplify(sp.cos(sp.pi / 2 - t) - sp.sin(t)) == 0,
      sp.simplify(sp.sin(sp.pi / 2 - t) - sp.cos(t)) == 0)
pts = [(sp.Rational(-12, 13), sp.Rational(-5, 13)),    # ✅ π/2 − θ
       (sp.Rational(-12, 13), sp.Rational(5, 13)),     # θ − π/2  (สลับลำดับการลบ)
       (sp.Rational(-5, 13), sp.Rational(12, 13)),     # −θ       (สะท้อนแกน x)
       (sp.Rational(5, 13), sp.Rational(12, 13))]      # θ + π    (จุดตรงข้าม)
print('  เรียงตาม (x, y) จากน้อยไปมาก:', pts, '⇒ ดัชนีคำตอบ 0')
assert pts == sorted(pts) and len(set(pts)) == 4
for p in pts:
    assert sp.simplify(p[0]**2 + p[1]**2) == 1, p
print('  ทุกตัวเลือกอยู่บนวงกลมหนึ่งหน่วยจริง ⇒ ไม่มีตัวลวงที่ถูกตัดทิ้งได้ฟรี ✓')

print()
print('=' * 74)
print('M-3 · 7.3 · f(x) = a sin(bx) + c , a>0 , b>0 , max 7 , min −1 , คาบ 2π/3 ⇒ f(π/12)')
print('=' * 74)
a, b, c = sp.symbols('a b c', positive=True)
sol = sp.solve([sp.Eq(a + c, 7), sp.Eq(-a + c, -1), sp.Eq(2 * sp.pi / b, 2 * sp.pi / 3)], [a, b, c], dict=True)
print('แก้ระบบได้:', sol)
A, B, C = sol[0][a], sol[0][b], sol[0][c]
f = A * sp.sin(B * sp.symbols('x')) + C
print('f(x) =', f)
X = sp.symbols('x')
fx = A * sp.sin(B * X) + C
print('  ตรวจ max =', sp.maximum(fx, X), '· min =', sp.minimum(fx, X),
      '· คาบ =', sp.periodicity(fx, X))
ans = sp.simplify(fx.subs(X, sp.pi / 12))
print('f(π/12) = 4 sin(π/4) + 3 =', ans, '≈', float(ans))

print('\nค่าตัวลวงที่คำนวณได้จริง:')
d1 = sp.simplify(A * sp.sin(B * sp.pi / 12))                    # ลืมบวก c
d2 = sp.simplify(A * sp.Rational(1, 2) + C)                     # จำ sin(π/4) = 1/2
d3 = sp.simplify(2 * A * sp.sin(B * sp.pi / 12) + C)            # ไม่หารสองตอนหาแอมพลิจูด (a = 8)
print('  ลืมบวกค่าคงที่ c        ⇒', d1, '≈', float(d1))
print('  ใช้ sin(π/4) = 1/2      ⇒', d2, '≈', float(d2))
print('  a = max−min = 8 (ไม่หาร2) ⇒', d3, '≈', float(d3))
cand = [d1, d2, ans, d3]
print('  เรียงจากน้อยไปมาก:', cand, '⇒ ดัชนีคำตอบ', cand.index(ans))
assert [float(v) for v in cand] == sorted(float(v) for v in cand)
assert len({sp.simplify(v) for v in cand}) == 4

print('\n  ตรวจอิสระ: จุดกึ่งกลาง c = (max+min)/2 =', (7 + (-1)) / 2,
      '· แอมพลิจูด a = (max−min)/2 =', (7 - (-1)) / 2,
      '· b = 2π/คาบ =', sp.simplify(2 * sp.pi / (2 * sp.pi / 3)))
print('  bx ที่ x = π/12 คือ 3·π/12 = π/4 ✓ ·  sin(π/4) =', sp.sin(sp.pi / 4))
print()
print('✅ ผ่านทั้งสามข้อ')

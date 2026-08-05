# -*- coding: utf-8 -*-
"""STEP D · sympy verify ของ 5 ข้อระดับ ง่าย ก้อน 1 (7.1 ×2 · 7.2 · 7.3 · 7.4)
ทุกตัวลวงต้องคำนวณจากเส้นทางพลาดจริง ⛔ ห้ามเดาเลขใกล้เคียง
ทุกข้อต้องมีการตรวจ 'สมมติฐานเป็นไปได้จริง' (บทเรียนจาก q140)"""
import sympy as sp

R = sp.Rational
ok_all = []

# ======================================================================
print('=' * 74)
print('E-1 · 7.1 · สามเหลี่ยม ABC มุม C = 90° , AB = 25 , BC = 7  ⇒  tan B = ?')
print('=' * 74)
AB, BC = 25, 7                      # AB = ด้านตรงข้ามมุมฉาก (ตรงข้ามมุม C)
AC = sp.sqrt(AB**2 - BC**2)
print('ตรวจความเป็นไปได้: BC < AB ?', BC < AB, '· AC =', AC, '(ต้องเป็นจำนวนเต็มบวก)')
assert AC == 24 and AC > 0
print('  สามเหลี่ยม 7-24-25 :', 7**2 + 24**2 == 25**2)

# มุม B อยู่ที่จุด B ⇒ ด้านตรงข้าม = AC = 24 · ด้านประชิด (ที่ไม่ใช่ด้านตรงข้ามมุมฉาก) = BC = 7
tanB = R(AC, BC)
sinB = R(AC, AB)
cosB = R(BC, AB)
print('  sin B =', sinB, '· cos B =', cosB, '· tan B =', tanB)
print('  ตรวจ sin²+cos² =', sp.simplify(sinB**2 + cosB**2), '· sin/cos =', sp.simplify(sinB / cosB))
assert sp.simplify(sinB**2 + cosB**2) == 1
assert sp.simplify(sinB / cosB - tanB) == 0

# ตรวจอิสระด้วยมุมจริง
Bang = sp.atan(tanB)
print('  ตรวจอิสระ: B = atan(24/7) ≈', float(Bang * 180 / sp.pi), '° · sin B ≈', float(sp.sin(Bang)),
      '(ควรเท่ากับ', float(sinB), ')')
assert abs(float(sp.sin(Bang)) - float(sinB)) < 1e-12

print('\nตัวลวงจากเส้นทางพลาดจริง:')
d_sinA = R(BC, AB)        # 7/25  = sin B? ไม่ใช่ — คือ cos B (สับ sin/cos ของมุม B)
d_swap = R(BC, AC)        # 7/24  = สลับข้าม/ชิด (ตอบ cot B)
d_hyp = R(AC, AB)         # 24/25 = ใช้ด้านตรงข้ามมุมฉากเป็นตัวส่วน (ได้ sin B)
print('  7/25  = ใช้ 7 เป็นตัวเศษ 25 เป็นตัวส่วน (ที่จริงคือ cos B)     ⇒', d_sinA)
print('  7/24  = สลับข้าม/ชิด (ที่จริงคือ cot B)                        ⇒', d_swap)
print('  24/25 = เอาด้านตรงข้ามมุมฉากมาเป็นตัวส่วน (ที่จริงคือ sin B)   ⇒', d_hyp)
vals = [d_sinA, d_swap, d_hyp, tanB]
print('  เรียงจากน้อยไปมาก:', vals, '⇒ ดัชนีคำตอบ', vals.index(tanB))
assert vals == sorted(vals) and len(set(vals)) == 4
ok_all.append(('E-1', vals.index(tanB)))

# ======================================================================
print()
print('=' * 74)
print('E-2 · 7.1 · A เป็นมุมแหลม , tan A = 5/12  ⇒  sin A + cos A = ?')
print('=' * 74)
opp, adj = 5, 12
hyp = sp.sqrt(opp**2 + adj**2)
print('ตรวจความเป็นไปได้: tan A = 5/12 > 0 และ A แหลม ⇒ มีจริงเสมอ · hyp =', hyp)
assert hyp == 13
sinA, cosA = R(opp, hyp), R(adj, hyp)
ans = sp.simplify(sinA + cosA)
print('  sin A =', sinA, '· cos A =', cosA, '· ผลบวก =', ans)
assert sp.simplify(sinA**2 + cosA**2) == 1

# ตรวจอิสระ: (sinA+cosA)² = 1 + 2 sinA cosA
lhs = sp.simplify(ans**2)
rhs = sp.simplify(1 + 2 * sinA * cosA)
print('  ตรวจอิสระ (วิธียกกำลังสอง): (s+c)² =', lhs, '· 1+2sc =', rhs, '· ตรงกัน:', lhs == rhs)
assert lhs == rhs
Aang = sp.atan(R(5, 12))
print('  ตรวจเชิงตัวเลข: A ≈', float(Aang * 180 / sp.pi), '° · sin+cos ≈',
      float(sp.sin(Aang) + sp.cos(Aang)), 'vs', float(ans))
assert abs(float(sp.sin(Aang) + sp.cos(Aang)) - float(ans)) < 1e-12

print('\nตัวลวงจากเส้นทางพลาดจริง:')
d_prod = sp.simplify(sinA * cosA)      # 60/169 ตอบผลคูณแทนผลบวก
d_diff = sp.simplify(cosA - sinA)      # 7/13  ตอบผลต่าง
d_wrong_hyp = R(17, 12)                # เข้าใจผิดว่า 12 คือด้านตรงข้ามมุมฉาก ⇒ (5+12)/12
print('  ตอบผลคูณ sinA·cosA                      ⇒', d_prod)
print('  ตอบผลต่าง cosA − sinA                   ⇒', d_diff)
print('  คิดว่า 12 คือด้านตรงข้ามมุมฉาก ⇒ (5+12)/12 ⇒', d_wrong_hyp)
vals2 = [d_prod, d_diff, ans, d_wrong_hyp]
print('  ค่าโดยประมาณ:', [float(v) for v in vals2])
print('  เรียงจากน้อยไปมาก:', vals2, '⇒ ดัชนีคำตอบ', vals2.index(ans))
assert vals2 == sorted(vals2, key=float) and len(set(vals2)) == 4
assert [float(v) for v in vals2] == sorted(float(v) for v in vals2)
ok_all.append(('E-2', vals2.index(ans)))

# ======================================================================
print()
print('=' * 74)
print('E-3 · 7.2 · tan 120° + cot 135° = ?')
print('=' * 74)
a1 = sp.tan(sp.rad(120))
a2 = sp.cot(sp.rad(135))
print('  tan 120° =', sp.simplify(a1), '· cot 135° =', sp.simplify(a2))
ans3 = sp.simplify(a1 + a2)
print('  ผลบวก =', ans3, '≈', float(ans3))
assert sp.simplify(ans3 - (-sp.sqrt(3) - 1)) == 0

# ตรวจอิสระ: ใช้มุมอ้างอิง + เครื่องหมายควอดรันต์
print('  ตรวจอิสระ (มุมอ้างอิง): 120° อยู่ควอดรันต์ 2 ⇒ tan ลบ · มุมอ้างอิง 60° ⇒ tan = ',
      sp.tan(sp.rad(60)), '⇒ tan120 = -√3')
print('                          135° อยู่ควอดรันต์ 2 ⇒ cot ลบ · มุมอ้างอิง 45° ⇒ cot = ',
      sp.cot(sp.rad(45)), '⇒ cot135 = -1')
assert sp.simplify(sp.tan(sp.rad(120)) + sp.sqrt(3)) == 0
assert sp.simplify(sp.cot(sp.rad(135)) + 1) == 0

print('\nตัวลวงจากเส้นทางพลาดจริง:')
t1 = sp.simplify(sp.sqrt(3) + 1)        # ลืมเครื่องหมายควอดรันต์ทั้งสองพจน์
t2 = sp.simplify(1 - sp.sqrt(3))        # ผิดเครื่องหมายเฉพาะ cot (−√3 + 1)
t3 = sp.simplify(sp.sqrt(3) - 1)        # ผิดเครื่องหมายเฉพาะ tan (+√3 − 1)
print('  ลืมเครื่องหมายควอดรันต์ทั้งคู่ ⇒ √3 + 1   =', t1, '≈', float(t1))
print('  ผิดเครื่องหมายเฉพาะ cot      ⇒ −√3 + 1  =', t2, '≈', float(t2))
print('  ผิดเครื่องหมายเฉพาะ tan      ⇒ √3 − 1   =', t3, '≈', float(t3))
vals3 = [ans3, t2, t3, t1]
print('  ค่าโดยประมาณ:', [float(v) for v in vals3])
assert [float(v) for v in vals3] == sorted(float(v) for v in vals3)
assert len({sp.simplify(v) for v in vals3}) == 4
print('  เรียงจากน้อยไปมาก ⇒ ดัชนีคำตอบ 0')
ok_all.append(('E-3', 0))

# ======================================================================
print()
print('=' * 74)
print('E-4 · 7.3 · f(x) = 4 − 5cos(3x)  ⇒  ค่าต่ำสุดที่เป็นไปได้ของ f = ?')
print('=' * 74)
X = sp.symbols('x', real=True)
f = 4 - 5 * sp.cos(3 * X)
mn = sp.minimum(f, X)
mx = sp.maximum(f, X)
print('  sympy: min =', mn, '· max =', mx, '· คาบ =', sp.periodicity(f, X))
assert mn == -1 and mx == 9

# ตรวจอิสระ: ต่ำสุดเกิดเมื่อ cos3x = +1 (เพราะสัมประสิทธิ์ติดลบ)
x0 = 0
print('  ตรวจอิสระ: cos(3x) = 1 ที่ x = 0 ⇒ f(0) =', f.subs(X, 0))
assert f.subs(X, 0) == -1
print('              cos(3x) = −1 ที่ x = π/3 ⇒ f(π/3) =', sp.simplify(f.subs(X, sp.pi / 3)))
assert sp.simplify(f.subs(X, sp.pi / 3)) == 9

print('\nตัวลวงจากเส้นทางพลาดจริง:')
print('  −5 = ลืมค่าคงที่ 4 (ตอบแค่ −|a|)')
print('   4 = ใช้ cos 3x = 0')
print('   9 = ตอบค่าสูงสุด (สับสนเพราะสัมประสิทธิ์ติดลบ)')
vals4 = [sp.Integer(-5), sp.Integer(-1), sp.Integer(4), sp.Integer(9)]
assert vals4 == sorted(vals4) and len(set(vals4)) == 4
print('  เรียงจากน้อยไปมาก:', vals4, '⇒ ดัชนีคำตอบ', vals4.index(sp.Integer(-1)))
ok_all.append(('E-4', vals4.index(sp.Integer(-1))))

# ======================================================================
print()
print('=' * 74)
print('E-5 · 7.4 · sinθ cosθ = 1/4  ⇒  (sinθ + cosθ)² = ?')
print('=' * 74)
# 🔴 บทเรียน q140: ต้องพิสูจน์ว่าสมมติฐานเป็นไปได้จริงก่อน
th = sp.symbols('theta', real=True)
print('ตรวจความเป็นไปได้ของสมมติฐาน:')
print('  sinθcosθ = (1/2)sin2θ ⇒ sin2θ = 1/2 · ช่วงค่าของ sin2θ = [−1, 1] ⇒ 1/2 อยู่ในช่วง ✓')
sols = sp.solve(sp.Eq(sp.sin(2 * th), R(1, 2)), th)
print('  ราก:', sols)
assert len(sols) > 0
theta0 = sp.rad(15)
chk = sp.simplify(sp.sin(theta0) * sp.cos(theta0))
print('  ตรวจด้วย θ = 15° : sinθcosθ =', chk, '≈', float(chk))
assert sp.simplify(chk - R(1, 4)) == 0

ans5 = sp.simplify(1 + 2 * R(1, 4))
print('\n  (s+c)² = s² + 2sc + c² = 1 + 2(1/4) =', ans5)
# ตรวจอิสระด้วยค่าจริงที่ θ = 15°
ind = sp.simplify((sp.sin(theta0) + sp.cos(theta0))**2)
print('  ตรวจอิสระที่ θ = 15° : (sin+cos)² =', ind, '=', sp.nsimplify(sp.expand(ind)), '≈', float(ind))
assert sp.simplify(ind - R(3, 2)) == 0
# และเชิงสัญลักษณ์
sym = sp.simplify(sp.expand((sp.sin(th) + sp.cos(th))**2) - 1 - 2 * sp.sin(th) * sp.cos(th))
print('  ตรวจเชิงสัญลักษณ์: (s+c)² − 1 − 2sc =', sym)
assert sym == 0

print('\nตัวลวงจากเส้นทางพลาดจริง:')
print('  1/2 = ตอบ 2 sinθcosθ (คือ sin2θ) แทนที่จะเป็น (s+c)²')
print('  1   = ลืมพจน์กลาง 2sc (เหลือแค่ s²+c²)')
print('  5/4 = ลืมคูณ 2 ที่พจน์กลาง (1 + 1/4)')
vals5 = [R(1, 2), sp.Integer(1), R(5, 4), R(3, 2)]
assert vals5 == sorted(vals5) and len(set(vals5)) == 4
print('  เรียงจากน้อยไปมาก:', vals5, '⇒ ดัชนีคำตอบ', vals5.index(R(3, 2)))
ok_all.append(('E-5', vals5.index(R(3, 2))))

# ======================================================================
print()
print('=' * 74)
print('สรุปดัชนีคำตอบ (0-based) และหมายเลขตัวเลือก (1-based)')
print('=' * 74)
for name, idx in ok_all:
    print('  %s : correct = %d  ⇒  ตัวเลือก %d' % (name, idx, idx + 1))
print('\n✅ ผ่านครบทั้ง 5 ข้อ')

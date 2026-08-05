# -*- coding: utf-8 -*-
"""STEP D · ตรวจคำตอบเชิงสัญลักษณ์ · ก้าว 2 ง่าย ก้อน 2 (E-6 … E-10)
   ทุกข้อ: (1) เดินเส้นทางหลัก (2) เดินเส้นทางอิสระอีกทาง (3) คำนวณตัวลวงจากเส้นทางพลาดที่ตั้งชื่อได้
   (4) ยืนยันว่าลิสต์ตัวเลือกเรียงจากน้อยไปมากและไม่ซ้ำ"""
import sympy as sp
from sympy import Rational as R

D = sp.pi / 180
ok = 0


def ascending(vals, label):
    nums = [sp.nsimplify(v) for v in vals]
    fl = [float(sp.N(v)) for v in nums]
    assert fl == sorted(fl), (label, fl)
    assert len(set(fl)) == len(fl), (label, fl)
    print('   ตัวเลือกเรียงน้อย→มาก และไม่ซ้ำ ✓', [str(sp.nsimplify(v)) for v in nums])


# ─────────────────────────────────────────────────────────────── E-6 · 7.1
print('E-6 · 7.1 · สามเหลี่ยมมุมฉากที่ C · AC = 12 · tan A = 3/4 ⇒ BC')
# มุม A อยู่ที่จุดยอด A · ด้านตรงข้าม A คือ BC · ด้านประชิด A (ที่ไม่ใช่ด้านตรงข้ามมุมฉาก) คือ AC
AC = 12
tanA = R(3, 4)
BC = tanA * AC
print('   หลัก   : tan A = BC/AC ⇒ BC = 12 · 3/4 =', BC)
assert BC == 9
# วิธีอิสระ: สามเหลี่ยมคล้าย 3-4-5 · ตัวคูณ k = 12/4 = 3
k = R(AC, 4)
BC2, AB2 = 3 * k, 5 * k
print('   อิสระ  : รูปคล้าย 3-4-5 · k = 12/4 =', k, '⇒ BC =', BC2, ', AB =', AB2)
assert BC2 == BC == 9 and AB2 == 15
assert sp.simplify(BC2**2 + AC**2 - AB2**2) == 0          # พีทาโกรัสยืนยัน
# ตัวลวง
d_inv = R(4, 3) * AC                     # กลับอัตราส่วน AC/BC = 3/4
d_hyp = AB2                              # ตอบด้านตรงข้ามมุมฉากแทนด้าน BC
d_both = sp.sqrt(AC**2 + d_inv**2)       # กลับอัตราส่วนแล้วยังตอบด้านตรงข้ามมุมฉาก
print('   ตัวลวง : กลับอัตราส่วน =', d_inv, '· ตอบด้าน AB =', d_hyp, '· กลับ+ตอบ AB =', d_both)
assert d_inv == 16 and d_hyp == 15 and d_both == 20
ascending([BC, d_hyp, d_inv, d_both], 'E-6')
print('   correct index =', 0, '⇒ ตัวเลือก 1')
ok += 1

# ─────────────────────────────────────────────────────────────── E-7 · 7.5
print()
print('E-7 · 7.5 · sin75°cos15° − cos75°sin15°')
expr = sp.sin(75 * D) * sp.cos(15 * D) - sp.cos(75 * D) * sp.sin(15 * D)
main = sp.simplify(expr)
print('   หลัก   : สูตรผลต่างมุม ⇒ sin(75° − 15°) = sin 60° =', main)
assert sp.simplify(main - sp.sqrt(3) / 2) == 0
# วิธีอิสระ: แทนค่าจริงของแต่ละพจน์แล้วบวกลบตรง ๆ (ไม่ใช้สูตรผลต่างมุมเลย)
indep = sp.nsimplify(sp.expand(sp.simplify(
    sp.sin(75 * D)) * sp.simplify(sp.cos(15 * D))
    - sp.simplify(sp.cos(75 * D)) * sp.simplify(sp.sin(15 * D))))
print('   อิสระ  : แทนค่ารากที่สองของแต่ละมุมแล้วคูณ-ลบตรง ๆ ⇒', sp.simplify(indep))
assert sp.simplify(indep - sp.sqrt(3) / 2) == 0
assert abs(float(sp.N(main)) - 0.8660254037844386) < 1e-12
# ตัวลวง
d_sum = sp.simplify(sp.sin(90 * D))      # จำสูตรผิดเป็นผลบวกมุม
d_cos = sp.simplify(sp.cos(60 * D))      # จำสูตรผิดเป็นสูตรของ cos
d_tab = sp.simplify(sp.sin(45 * D))      # ได้ 60° ถูก แต่เปิดตารางมุมพิเศษสลับแถว
print('   ตัวลวง : ใช้สูตรผลบวก ⇒ sin90° =', d_sum,
      '· ใช้สูตรของ cos ⇒ cos60° =', d_cos,
      '· จำค่ามุมพิเศษสลับ ⇒ sin45° =', d_tab)
assert d_sum == 1 and d_cos == R(1, 2) and sp.simplify(d_tab - sp.sqrt(2) / 2) == 0
ascending([d_cos, d_tab, main, d_sum], 'E-7')
print('   correct index =', 2, '⇒ ตัวเลือก 3')
ok += 1

# ─────────────────────────────────────────────────────────────── E-8 · 7.6
print()
print('E-8 · 7.6 · tanθ = 4 · θ แหลม ⇒ tan 2θ')
print('   ⚠️ เลี่ยงพื้นผิว tanθ = 2 / 3 เพราะ samn-2559-12-q03 (ง่าย) ใช้ tanA = 2, tanB = 3 อยู่แล้ว')
th = sp.atan(4)
assert 0 < float(sp.N(th)) < float(sp.N(sp.pi / 2))
main8 = sp.nsimplify(sp.simplify(sp.expand_trig(sp.tan(2 * th))))
print('   หลัก   : tan2θ = 2tanθ/(1 − tan²θ) = 8/(1 − 16) =', main8)
assert main8 == R(-8, 15)
# วิธีอิสระ: สร้าง sin θ, cos θ จากสามเหลี่ยม 1-4-√17 แล้วใช้ sin2θ/cos2θ
s_, c_ = 4 / sp.sqrt(17), 1 / sp.sqrt(17)
assert sp.simplify(s_**2 + c_**2 - 1) == 0
s2, c2 = sp.simplify(2 * s_ * c_), sp.simplify(c_**2 - s_**2)
indep8 = sp.nsimplify(sp.simplify(s2 / c2))
print('   อิสระ  : สามเหลี่ยม 1-4-√17 ⇒ sin2θ =', s2, ', cos2θ =', c2, '⇒ tan2θ =', indep8)
assert indep8 == R(-8, 15)
assert s2 == R(8, 17) and c2 == R(-15, 17)      # ตกลงที่สามเหลี่ยมมุมฉาก 8-15-17 พอดี
deg2 = float(sp.N(2 * th * 180 / sp.pi))
print('   ตรวจซ้ำ: 2θ =', deg2, 'องศา ⇒ อยู่ควอดรันต์ 2 ⇒ tan ต้องเป็นลบ ✓')
assert 90 < deg2 < 180
d8a = sp.nsimplify(sp.simplify(2 * sp.tan(th)))   # คิดว่า tan2θ = 2tanθ
d8b = R(2 * 4, 4**2 - 1)                          # กลับเครื่องหมายตัวส่วน
d8c = R(2 * 4, 1 + 4**2)                          # ใช้ 1 + tan²θ เป็นตัวส่วน
print('   ตัวลวง : 2tanθ =', d8a, '· ตัวส่วนเป็น tan²θ − 1 ⇒', d8b,
      '· ตัวส่วนเป็น 1 + tan²θ ⇒', d8c)
assert d8a == 8 and d8b == R(8, 15) and d8c == R(8, 17)
ascending([main8, d8c, d8b, d8a], 'E-8')
print('   correct index =', 0, '⇒ ตัวเลือก 1')
ok += 1

# ─────────────────────────────────────────────────────────────── E-9 · 7.7
print()
print('E-9 · 7.7 · 2cos x = √3 · 0° ≤ x < 90° ⇒ x')
x = sp.Symbol('x', real=True)
sols = sp.solveset(sp.Eq(2 * sp.cos(x), sp.sqrt(3)), x,
                   domain=sp.Interval.Ropen(0, sp.pi / 2))
sols = list(sols)
print('   หลัก   : cos x = √3/2 · คำตอบในช่วง [0°, 90°) =',
      [str(sp.N(v * 180 / sp.pi)) + '°' for v in sols])
assert len(sols) == 1, sols                            # ⚠️ ต้องมีคำตอบเดียว ⇒ C = 0 จริง
assert sp.simplify(sols[0] - sp.pi / 6) == 0
# วิธีอิสระ: แทน x = 30° กลับเข้าสมการเดิม + ยืนยันว่า cos ลดทางเดียวบน [0°,90°) ⇒ ไม่มีคำตอบอื่น
lhs = sp.simplify(2 * sp.cos(30 * D))
print('   อิสระ  : แทน x = 30° ⇒ 2cos30° =', lhs, '= √3 ✓ · และ cos ลดทางเดียวบน [0°,90°) ⇒ คำตอบเดียว')
assert sp.simplify(lhs - sp.sqrt(3)) == 0
assert sp.simplify(sp.diff(sp.cos(x), x).subs(x, sp.pi / 4)) < 0
# ตัวลวง
d9a = 15    # อ่าน 2cos x เป็น cos 2x ⇒ 2x = 30° ⇒ x = 15°
d9b = 45    # จำ √3/2 สลับกับ √2/2
d9c = 60    # เปิดตารางผิดแถว ใช้ sin x = √3/2 แทน cos x = √3/2
for ang, why in [(d9a, 'cos2x'), (d9b, '√2/2'), (d9c, 'sin แทน cos')]:
    assert sp.simplify(2 * sp.cos(ang * D) - sp.sqrt(3)) != 0, ang
print('   ตัวลวง : 15° (อ่านเป็น cos2x) · 45° (จำ √3/2 สลับ √2/2) · 60° (ใช้แถว sin แทน cos)')
print('   ยืนยันว่าทั้งสามไม่ใช่คำตอบ: 2cos15° =', float(sp.N(2 * sp.cos(d9a * D))),
      '· 2cos45° =', float(sp.N(2 * sp.cos(d9b * D))),
      '· 2cos60° =', float(sp.N(2 * sp.cos(d9c * D))), '(√3 =', float(sp.N(sp.sqrt(3))), ')')
ascending([15, 30, 45, 60], 'E-9')
print('   correct index =', 1, '⇒ ตัวเลือก 2')
ok += 1

# ─────────────────────────────────────────────────────────────── E-10 · 7.9
print()
print('E-10 · 7.9 · A = 30° · C = 105° · a = 8 ⇒ b')
print('   ⚠️ ให้มุม A กับ C (ไม่ใช่ A กับ B) เพื่อบังคับให้ต้องหามุม B ก่อน')
print('      และเพื่อให้ต่างพื้นผิวจาก chap-07-trigonometry-q109 ที่ให้สองมุมที่ต้องใช้มาตรง ๆ')
a = 8
A_, C_ = 30, 105
B_ = 180 - A_ - C_
print('   ขั้นแรก : B = 180° −', A_, '° −', C_, '° =', B_, '°')
assert B_ == 45
main10 = sp.simplify(a * sp.sin(B_ * D) / sp.sin(A_ * D))
print('   หลัก   : b = a·sinB/sinA = 8·(√2/2)/(1/2) =', main10)
assert sp.simplify(main10 - 8 * sp.sqrt(2)) == 0
# วิธีอิสระ: เดินผ่านด้าน c เป็นตัวกลาง (ไม่ใช้ความสัมพันธ์ a↔b โดยตรงเลย)
c = sp.simplify(a * sp.sin(C_ * D) / sp.sin(A_ * D))
b_via_c = sp.simplify(sp.expand(c * sp.sin(B_ * D) / sp.sin(C_ * D)))
print('   อิสระ  : c =', c, '⇒ b = c·sinB/sinC =', b_via_c)
assert sp.simplify(b_via_c - 8 * sp.sqrt(2)) == 0
# ตรวจอีกชั้นด้วยกฎโคไซน์: b² = a² + c² − 2ac cos B
lhs = sp.simplify(a**2 + c**2 - 2 * a * c * sp.cos(B_ * D))
print('   ตรวจซ้ำ: กฎโคไซน์ a² + c² − 2ac·cosB =', sp.simplify(lhs), '= (8√2)² =', 128)
assert sp.simplify(lhs - 128) == 0
print('   ตรวจรูป: มุม B > มุม A ⇒ ด้าน b ต้องยาวกว่า a = 8 ·  b =', float(sp.N(main10)), '> 8 ✓')
assert float(sp.N(main10)) > a
d10a = sp.simplify(a * sp.sin(A_ * D) / sp.sin(B_ * D))   # กลับอัตราส่วน
d10b = sp.simplify(sp.expand(c))                          # ใช้ sinC แทน sinB ⇒ ได้ด้าน c
d10c = R(a * B_, A_)                                      # เทียบสัดส่วนด้วยขนาดมุมแทนไซน์
print('   ตัวลวง : กลับอัตราส่วน ⇒', d10a, '· ใช้ sinC แทน sinB (ได้ด้าน c) ⇒', d10b,
      '· เทียบสัดส่วนด้วยขนาดมุม 8·45/30 ⇒', d10c)
assert sp.simplify(d10a - 4 * sp.sqrt(2)) == 0
assert sp.simplify(d10b - (4 * sp.sqrt(2) + 4 * sp.sqrt(6))) == 0
assert d10c == 12
ascending([d10a, main10, d10c, d10b], 'E-10')
print('   correct index =', 1, '⇒ ตัวเลือก 2')
ok += 1

print()
print('✅ ผ่านครบทั้ง', ok, 'ข้อ')

# -*- coding: utf-8 -*-
import io
p = '/home/claude/k2/v_easy2.py'
s = io.open(p, encoding='utf-8').read()

M8, M9 = '# ─────────────────────────────────────────────────────────────── E-8 · 7.6', \
         '# ─────────────────────────────────────────────────────────────── E-9 · 7.7'
M10, END = '# ─────────────────────────────────────────────────────────────── E-10 · 7.9', \
           "print()\nprint('✅ ผ่านครบทั้ง'"

NEW8 = M8 + r'''
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

'''

NEW10 = M10 + r'''
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

'''

i8, i9 = s.index(M8), s.index(M9)
s = s[:i8] + NEW8 + s[i9:]
i10, iend = s.index(M10), s.index(END)
s = s[:i10] + NEW10 + s[iend:]
io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('patched')

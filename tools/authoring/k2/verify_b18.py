# -*- coding: utf-8 -*-
"""STEP D · ตรวจคำตอบ + ตัวลวงทั้ง 10 ข้อของก้อน 18 ด้วย sympy (ห้ามข้าม · กฎเหล็ก 1)"""
import sympy as sp

x, t, th = sp.symbols('x t theta', real=True)
ok = True


def chk(tag, got, want):
    global ok
    g = sp.nsimplify(sp.simplify(got))
    w = sp.nsimplify(sp.simplify(want))
    good = sp.simplify(g - w) == 0
    ok = ok and good
    print(('  ✅ ' if good else '  ❌ ') + tag + '  ได้ ' + str(g) + '  ต้องการ ' + str(w))


print('q095 · ให้ส่วนโค้ง s = 10pi/3 และมุม 5pi/9 เรเดียน ⇒ หารัศมี')
s095, a095 = sp.Rational(10, 3) * sp.pi, sp.Rational(5, 9) * sp.pi
chk('คำตอบ r = s/theta', s095 / a095, 6)
chk('ลวง1 กลับเศษส่วน theta/s', a095 / s095, sp.Rational(1, 6))
chk('ลวง2 ใช้สูตรพื้นที่ r=sqrt(2s/theta)', sp.sqrt(2 * s095 / a095), 2 * sp.sqrt(3))
chk('ลวง3 จำผิดว่า s=r*theta/2 ⇒ r=2s/theta', 2 * s095 / a095, 12)

print('q096 · รูปอย่างง่ายของ sin(t)sec(t)cot(t)')
chk('คำตอบ', sp.sin(t) * sp.sec(t) * sp.cot(t), 1)
chk('ลวง1 ใช้ sec=1/sin ⇒ เหลือ cot', sp.sin(t) * (1 / sp.sin(t)) * sp.cot(t), sp.cot(t))
chk('ลวง2 คิดว่า sec กับ cot เป็นส่วนกลับกัน ⇒ เหลือ sin', sp.sin(t) * 1, sp.sin(t))
chk('ลวง3 พลิก cot เป็น sin/cos', sp.sin(t) * sp.sec(t) * (sp.sin(t) / sp.cos(t)), sp.tan(t) ** 2)

print('q097 · sin A = 3/5 (จตุภาค 2) · cos B = -12/13 (จตุภาค 3) ⇒ sin(A+B)')
sA, cA = sp.Rational(3, 5), sp.Rational(-4, 5)
cB, sB = sp.Rational(-12, 13), sp.Rational(-5, 13)
chk('ตรวจ A อยู่จตุภาค 2', sA ** 2 + cA ** 2, 1)
chk('ตรวจ B อยู่จตุภาค 3', sB ** 2 + cB ** 2, 1)
chk('คำตอบ sin(A+B)', sA * cB + cA * sB, sp.Rational(-16, 65))
chk('ลวง1 ทิ้งเครื่องหมายจตุภาคทั้งหมด', sp.Rational(3, 5) * sp.Rational(12, 13)
    + sp.Rational(4, 5) * sp.Rational(5, 13), sp.Rational(56, 65))
chk('ลวง2 ใช้สูตร cos(A+B) แทน', cA * cB - sA * sB, sp.Rational(63, 65))
chk('ลวง3 ให้ sin B เป็นบวก', sA * cB + cA * sp.Rational(5, 13), sp.Rational(-56, 65))

print('q098 · หลังคาจั่ว ยาว 20 · ฐาน 12 · จันทันทำมุม 30 องศา ⇒ พื้นที่แผ่นมุงสองผืน')
raf = 6 / sp.cos(sp.rad(30))
chk('จันทัน = 6/cos30', raf, 4 * sp.sqrt(3))
chk('คำตอบ 2*20*จันทัน', 2 * 20 * raf, 160 * sp.sqrt(3))
chk('ลวง1 นับผืนเดียว', 20 * raf, 80 * sp.sqrt(3))
chk('ลวง2 ใช้ tan30 แทน cos30 ในตัวส่วน', 2 * 20 * (6 / sp.tan(sp.rad(30))), 240 * sp.sqrt(3))
chk('ลวง3 ใช้ฐานเต็ม 12 แทนครึ่งฐาน', 2 * 20 * (12 / sp.cos(sp.rad(30))), 320 * sp.sqrt(3))

print('q099 · sin t = -3/5 · จตุภาค 3 ⇒ sin(2t)/(1+cos(2t))')
st, ct = sp.Rational(-3, 5), sp.Rational(-4, 5)
chk('ตรวจจตุภาค 3', st ** 2 + ct ** 2, 1)
val = (2 * st * ct) / (1 + (2 * ct ** 2 - 1))
chk('คำตอบ = tan t', val, sp.Rational(3, 4))
chk('ลวง1 ใช้ cos t = 4/5', (2 * st * sp.Rational(4, 5)) / (2 * sp.Rational(4, 5) ** 2),
    sp.Rational(-3, 4))
chk('ลวง2 ตอบ cot t', ct / st, sp.Rational(4, 3))
chk('ลวง3 cot t ที่เครื่องหมายพลาด', -ct / -(-st), sp.Rational(-4, 3))
chk('เอกลักษณ์ทั่วไป sin2t/(1+cos2t) = tan t',
    sp.simplify(sp.sin(2 * t) / (1 + sp.cos(2 * t)) - sp.tan(t)), 0)

print('q100 · sin/(1-cot) + cos/(1-tan)')
e100 = sp.sin(th) / (1 - sp.cot(th)) + sp.cos(th) / (1 - sp.tan(th))
chk('คำตอบ = sin + cos', sp.simplify(e100 - (sp.sin(th) + sp.cos(th))), 0)
chk('ลวง3 ตัวส่วนร่วมผิด ⇒ 1/(sin-cos)',
    (sp.sin(th) ** 2 + sp.cos(th) ** 2) / (sp.sin(th) - sp.cos(th)),
    1 / (sp.sin(th) - sp.cos(th)))
for v in [sp.Rational(3, 10), sp.Rational(9, 10), sp.Rational(23, 10)]:
    chk('เช็คเชิงตัวเลขที่ theta=' + str(v),
        e100.subs(th, v) - (sp.sin(v) + sp.cos(v)), 0)

print('q101 · 3 sin th = 2 cos th · จตุภาค 3 ⇒ csc th')
s101 = -2 / sp.sqrt(13)
c101 = -3 / sp.sqrt(13)
chk('ตรวจสมการ', 3 * s101 - 2 * c101, 0)
chk('ตรวจบนวงกลมหนึ่งหน่วย', s101 ** 2 + c101 ** 2, 1)
chk('คำตอบ csc', 1 / s101, -sp.sqrt(13) / 2)
chk('ลวง1 ลืมเครื่องหมายจตุภาค', 1 / (2 / sp.sqrt(13)), sp.sqrt(13) / 2)
chk('ลวง2 ตอบ sec', 1 / c101, -sp.sqrt(13) / 3)
chk('ลวง3 ตอบ cot', c101 / s101, sp.Rational(3, 2))

print('q102 · 2cos^2 x - 3cos x + 1 = 0 · 0 <= x < 2pi ⇒ นับคำตอบ')
sol = sp.solveset(2 * sp.cos(x) ** 2 - 3 * sp.cos(x) + 1, x,
                  sp.Interval.Ropen(0, 2 * sp.pi))
print('   คำตอบจริง :', sol)
chk('จำนวนคำตอบ', len(sol), 3)
chk('ลวง1 ทิ้งราก cos=1', len(sp.solveset(sp.cos(x) - sp.Rational(1, 2), x,
                                          sp.Interval.Ropen(0, 2 * sp.pi))), 2)

print('q103 · sin 3x = cos 2x ⇒ คำตอบบวกน้อยที่สุด')
chk('ตรวจ x=pi/10 เป็นคำตอบ',
    sp.sin(3 * sp.pi / 10) - sp.cos(2 * sp.pi / 10), 0)
cand = sp.solveset(sp.sin(3 * x) - sp.cos(2 * x), x, sp.Interval.open(0, sp.pi))
print('   คำตอบใน (0, pi) :', cand)
# ⚠️ sympy คืนรากในรูป atan(...) ที่ simplify ยุบไม่ลง ⇒ เทียบเชิงตัวเลขความละเอียดสูงแทน
lo = min(cand, key=lambda e: sp.N(e, 40))
print('   รากน้อยสุด (ตัวเลข 40 หลัก) :', sp.N(lo, 40))
same = abs(sp.N(lo - sp.pi / 10, 40)) < sp.Float('1e-35')
ok = ok and bool(same)
print(('  ✅ ' if same else '  ❌ ') + 'ค่าน้อยสุดที่เป็นบวก = pi/10  (pi/10 = '
      + str(sp.N(sp.pi / 10, 40)) + ')')
# ยืนยันอีกทางหนึ่ง : g(x) = sin3x - cos2x ไม่เปลี่ยนเครื่องหมายเลยใน (0, pi/10)
g = sp.lambdify(x, sp.sin(3 * x) - sp.cos(2 * x), 'math')
vals = [g(k * float(sp.pi / 10) / 4000.0) for k in range(1, 4000)]
nz = all(v < 0 for v in vals)
ok = ok and nz
print(('  ✅ ' if nz else '  ❌ ') + 'ไม่มีคำตอบใดใน (0, pi/10) — g(x) < 0 ตลอด 3999 จุด '
      + '(g ต่ำสุด ' + ('%.6f' % min(vals)) + ' · สูงสุด ' + ('%.6f' % max(vals)) + ')')
for bad, why in [(sp.pi / 6, 'ลวง1 แยกตัวประกอบพหุนามผิดได้ sin x = 1/2'),
                 (sp.pi / 5, 'ลวง2 ใช้ผลบวกมุม = pi แทน pi/2'),
                 (sp.pi / 2, 'ลวง3 ใช้เฉพาะวงศ์ที่สอง')]:
    r = sp.simplify(sp.sin(3 * bad) - sp.cos(2 * bad))
    print(('  ✅ ' if (r != 0 or bad == sp.pi / 2) else '  ❌ ') + why
          + '  ค่าต่าง = ' + str(r))
chk('ยืนยันว่า pi/2 เป็นคำตอบจริงแต่ไม่ใช่ตัวน้อยสุด',
    sp.sin(3 * sp.pi / 2) - sp.cos(sp.pi), 0)

print('q104 · บอลลูน เชือก 40 ม. ทำมุม 30 องศา · เชือกอีกเส้นทำมุม 45 องศา · มุม AOB = 150 องศา')
h = 40 * sp.sin(sp.rad(30))
OA = 40 * sp.cos(sp.rad(30))
OB = h / sp.tan(sp.rad(45))
chk('ความสูง h', h, 20)
chk('OA', OA, 20 * sp.sqrt(3))
chk('OB', OB, 20)
AB2 = OA ** 2 + OB ** 2 - 2 * OA * OB * sp.cos(sp.rad(150))
chk('AB^2', AB2, 2800)
chk('คำตอบ AB', sp.sqrt(AB2), 20 * sp.sqrt(7))
chk('ลวง1 ใช้ cos150 เป็นบวก', sp.sqrt(OA ** 2 + OB ** 2 - 2 * OA * OB * sp.sqrt(3) / 2), 20)
chk('ลวง2 ตอบ OA แทน AB', OA, 20 * sp.sqrt(3))
chk('ลวง3 คิดว่ามุม AOB เป็นมุมฉาก', sp.sqrt(OA ** 2 + OB ** 2), 40)

print()
print('สรุปก้อน 18 :', 'ผ่านทุกข้อ ✅' if ok else 'มีข้อผิด ❌')

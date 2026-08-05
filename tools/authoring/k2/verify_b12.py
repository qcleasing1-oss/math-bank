# -*- coding: utf-8 -*-
"""STEP D · ตรวจคำตอบก้อน 12 ด้วย sympy — ทุกข้อต้องมี "เส้นทางที่สอง" ที่เป็นอิสระจากเส้นทางแรก
กฎเหล็กข้อ 1 : ห้ามเชื่อการคำนวณมือ · ทุกตัวลวงต้องคำนวณด้วยเครื่องเช่นกัน (กฎเหล็กข้อ 2)
"""
import sympy as sp

ok = True


def chk(tag, got, want, note=''):
    global ok
    good = sp.simplify(sp.nsimplify(got) - sp.nsimplify(want)) == 0
    ok &= good
    print('   %-52s %-22s %s %s' % (tag, str(got), 'ตรง' if good else '❌ ไม่ตรง', note))


# ══════════════════════════════════════════════════════════════════════════════
print('q065 · สามเหลี่ยมมุมฉาก มุม C ฉาก · BC = 9 · CA = 12 ⇒ (sin A + cos A)/tan A')
a, b = sp.Integer(9), sp.Integer(12)          # a = BC ตรงข้ามมุม A · b = CA ตรงข้ามมุม B
c = sp.sqrt(a**2 + b**2)
chk('ด้านตรงข้ามมุมฉาก c', c, 15)
sinA, cosA, tanA = a / c, b / c, a / b
E1 = (sinA + cosA) / tanA
chk('เส้นทางที่ 1 · จากอัตราส่วนด้าน', E1, sp.Rational(28, 15))

# เส้นทางที่ 2 · หามุม A จริงก่อน แล้วค่อยแทนในนิพจน์ตรีโกณ (อิสระจากเส้นทางแรก)
A = sp.atan(sp.Rational(9, 12))
E2 = (sp.sin(A) + sp.cos(A)) / sp.tan(A)
chk('เส้นทางที่ 2 · ผ่านมุม A = atan(3/4)', sp.nsimplify(sp.N(E2, 50), rational=True), sp.Rational(28, 15))

chk('ตัวลวง · คิดอัตราส่วนของมุม B แทนมุม A', (sinA + cosA) / sp.Rational(12, 9), sp.Rational(21, 20))
sinB, cosB, tanB = b / c, a / c, b / a
chk('ตัวลวง · ยืนยันว่าเส้นทางมุม B ให้ค่าเดียวกัน', (sinB + cosB) / tanB, sp.Rational(21, 20))
chk('ตัวลวง · เอา tan A ไปหารเฉพาะพจน์แรก', sinA / tanA + cosA, sp.Rational(8, 5))
chk('ตัวลวง · หลงว่า sin A + cos A = 1', 1 / tanA, sp.Rational(4, 3))
# ⛔ ตัวลวงต้องรอดจากขอบเขตสามัญสำนึก : sin A + cos A > 1 และ tan A = 3/4 < 1
#    ⇒ ค่าจริงต้องมากกว่า 1/tan A = 4/3 ⇒ ตัวลวงที่ดีต้องไม่ถูกตัดทิ้งพร้อมกันทั้งชุด
print('   %-52s %s' % ('ตัวลวง 8/5 รอดจากขอบเขต > 4/3 (ไม่ให้ข้อกลายเป็นข้อเดา)',
      'ตรง' if sp.Rational(8, 5) > sp.Rational(4, 3) else '❌ ไม่ตรง'))
ok &= sp.Rational(8, 5) > sp.Rational(4, 3)

# ══════════════════════════════════════════════════════════════════════════════
print()
print('q066 · รอกสองตัวเชื่อมด้วยสายพาน · รัศมี 12 กับ 30 ซม. · ตัวเล็ก 150 รอบ/นาที')
r1, r2, n1 = sp.Integer(12), sp.Integer(30), sp.Integer(150)
chk('เส้นทางที่ 1 · v เท่ากัน ⇒ n2 = n1·r1/r2', n1 * r1 / r2, 60)

# เส้นทางที่ 2 · นับความยาวสายพานที่เคลื่อนไปใน 1 นาที แล้วหารด้วยเส้นรอบวงตัวใหญ่
belt = n1 * 2 * sp.pi * r1
chk('เส้นทางที่ 2 · ความยาวสายพานต่อนาที / เส้นรอบวงใหญ่', sp.simplify(belt / (2 * sp.pi * r2)), 60)

chk('ตัวลวง · กลับอัตราส่วน n1·r2/r1', n1 * r2 / r1, 375)
chk('ตัวลวง · คิดว่ารอบต่อนาทีเท่ากัน', n1, 150)
chk('ตัวลวง · ใช้อัตราส่วนกำลังสอง (พื้นที่)', n1 * (r1 / r2)**2, 24)

# ══════════════════════════════════════════════════════════════════════════════
print()
print('q067 · จำนวนเต็ม n ที่ทำให้ arccos((n+4)/6) นิยามได้')
n = sp.Symbol('n', integer=True)
sol = sp.solve([sp.Ge((n + 4) / 6, -1), sp.Le((n + 4) / 6, 1)], n)
print('   ผลจาก sympy :', sol)
cnt1 = len([k for k in range(-10, 3)])
chk('เส้นทางที่ 1 · −10 ≤ n ≤ 2', cnt1, 13)

# เส้นทางที่ 2 · ไล่ยิงทีละจำนวนในช่วงกว้าง แล้วนับจริง (ไม่พึ่งการแก้อสมการ)
cnt2 = sum(1 for k in range(-200, 201) if abs(sp.Rational(k + 4, 6)) <= 1)
chk('เส้นทางที่ 2 · ไล่นับ n ตั้งแต่ −200 ถึง 200', cnt2, 13)

chk('ตัวลวง · ลืมคูณ 6 (−1 ≤ n+4 ≤ 1)',
    sum(1 for k in range(-200, 201) if -1 <= k + 4 <= 1), 3)
chk('ตัวลวง · คิดว่าโดเมนคือ [0, 1]',
    sum(1 for k in range(-200, 201) if 0 <= sp.Rational(k + 4, 6) <= 1), 7)
chk('ตัวลวง · นับพลาดหนึ่ง (2 − (−10))', 2 - (-10), 12)

# ══════════════════════════════════════════════════════════════════════════════
print()
print('q068 · สองเมืองบนเส้นละติจูด 60° เหนือ · ลองจิจูดต่างกัน 45° · R = 6400 กม.')
R, phi, dlam = sp.Integer(6400), sp.rad(60), sp.rad(45)
rlat = R * sp.cos(phi)
chk('รัศมีของวงกลมละติจูด R·cos 60°', rlat, 3200)
chk('เส้นทางที่ 1 · s = r·theta', sp.simplify(rlat * dlam), 800 * sp.pi)

# เส้นทางที่ 2 · วางพิกัดสามมิติจริง แล้ววัดระยะจากแกนโลกด้วย sqrt(x^2 + y^2)
lam = sp.Symbol('lam')
x = R * sp.cos(phi) * sp.cos(lam)
y = R * sp.cos(phi) * sp.sin(lam)
z = R * sp.sin(phi)
chk('เส้นทางที่ 2a · จุดอยู่บนผิวโลกจริง (x²+y²+z² = R²)', sp.simplify(x**2 + y**2 + z**2), R**2)
axis = sp.simplify(sp.sqrt(x**2 + y**2))
chk('เส้นทางที่ 2b · ระยะจากแกนโลก', axis, 3200)
chk('เส้นทางที่ 2c · s = (ระยะจากแกน)·(มุมลองจิจูด)', sp.simplify(axis * dlam), 800 * sp.pi)

chk('ตัวลวง · ใช้ R = 6400 ตรง ๆ (ลืม cos 60°)', sp.simplify(R * dlam), 1600 * sp.pi)
chk('ตัวลวง · ใช้ sin 60° แทน cos 60°', sp.simplify(R * sp.sin(phi) * dlam), 800 * sp.sqrt(3) * sp.pi)
chk('ตัวลวง · แปลง 45° เป็นเรเดียนด้วย 360 แทน 180', sp.simplify(rlat * sp.pi * 45 / 360), 400 * sp.pi)

# ══════════════════════════════════════════════════════════════════════════════
print()
print('q069 · สามเหลี่ยม ABC · a = 6 · A = pi/3 ⇒ ช่วงของเส้นรอบรูป P')
B = sp.Symbol('B', positive=True)
aa, AA = sp.Integer(6), sp.pi / 3
twoR = sp.simplify(aa / sp.sin(AA))
chk('2R = a/sin A', twoR, 4 * sp.sqrt(3))
CC = sp.pi - AA - B
bb, cc = twoR * sp.sin(B), twoR * sp.sin(CC)
P1 = sp.simplify(aa + bb + cc)
P2 = 6 + 12 * sp.cos(B - sp.pi / 3)
chk('เส้นทางที่ 1 · ยุบผลบวกเป็นผลคูณ ⇒ P = 6 + 12cos(B − pi/3)',
    sp.simplify(sp.expand_trig(P1 - P2)), 0)

# เส้นทางที่ 2 · ไล่ยิงตัวเลขบนช่วง B ที่เป็นไปได้ทั้งช่วง (ไม่พึ่งสูตรผลบวกเป็นผลคูณ)
vals = [sp.N(P1.subs(B, sp.Rational(k, 2000) * sp.Rational(2, 3) * sp.pi), 30)
        for k in range(1, 2000)]
lo, hi = min(vals), max(vals)
print('   เส้นทางที่ 2 · ไล่ยิง 1999 จุด : ต่ำสุดที่พบ %s · สูงสุดที่พบ %s' % (sp.N(lo, 12), sp.N(hi, 12)))
print('   %-52s %s' % ('ค่าที่พบทั้งหมดอยู่ใน (12, 18]',
      'ตรง' if all(sp.N(v) > 12 and sp.N(v) <= 18 + sp.Rational(1, 10**20) for v in vals) else '❌ ไม่ตรง'))
ok &= all(sp.N(v) > 12 for v in vals)

chk('ปลายบน · แตะได้จริงที่ B = pi/3 (สามเหลี่ยมด้านเท่า)', sp.simplify(P1.subs(B, sp.pi / 3)), 18)
lim_lo = sp.limit(P1, B, 0, '+')
chk('ปลายล่าง · ลิมิตเมื่อ B → 0+ (สามเหลี่ยมแฟบ ⇒ แตะไม่ได้)', sp.simplify(lim_lo), 12)
lim_hi = sp.limit(P1, B, sp.Rational(2, 3) * sp.pi, '-')
chk('ปลายล่างอีกฝั่ง · ลิมิตเมื่อ B → 2pi/3−', sp.simplify(lim_hi), 12)

print()
print('=' * 78)
print('สรุปก้อน 12 :', 'ผ่านทุกข้อ ✅' if ok else '❌ มีจุดไม่ตรง — ห้ามแต่งต่อ')

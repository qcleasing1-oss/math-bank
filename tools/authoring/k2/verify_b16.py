# -*- coding: utf-8 -*-
"""ตรวจคำตอบก้อน 16 (q085-q089) ด้วย sympy — กฎเหล็กข้อ 1 ห้ามข้าม

ทุกข้อต้องผ่านสองชั้น
  ชั้น 1  คำนวณเชิงสัญลักษณ์ตามเส้นทางเฉลย
  ชั้น 2  ตรวจซ้ำด้วยวิธีอิสระ (ตัวเลข/เรขาคณิต/สุ่มค่า) ที่ไม่ใช้สูตรเดิม
และตัวลวงทุกตัวต้องคำนวณจาก "เส้นทางพลาด" ที่ตั้งชื่อได้ ไม่ใช่เลขสุ่ม
"""
import sympy as sp

ok = True


def chk(label, got, want, tol=None):
    global ok
    if tol is None:
        good = sp.simplify(got - want) == 0
    else:
        good = abs(float(got) - float(want)) < tol
    print(('  ✅ ' if good else '  ❌ ') + label + '   ได้ %s · คาด %s' % (got, want))
    if not good:
        ok = False


pi = sp.pi

# ═══════════════════════════════════════════════════════════════════════════
print('== q085 · เรนจ์ของ f(x) = 3 arccos x - pi/2 ==')
x = sp.Symbol('x', real=True)
f = 3 * sp.acos(x) - pi / 2

# ชั้น 1 · arccos มีเรนจ์ [0, pi] และ 3u - pi/2 เป็นฟังก์ชันเพิ่มใน u
lo1 = f.subs(x, 1)      # acos(1) = 0
hi1 = f.subs(x, -1)     # acos(-1) = pi
chk('ค่าต่ำสุด (ที่ x = 1)', sp.simplify(lo1), -pi / 2)
chk('ค่าสูงสุด (ที่ x = -1)', sp.simplify(hi1), 5 * pi / 2)

# ชั้น 2 · วิธีอิสระ : กวาดค่า f บน [-1, 1] แบบตัวเลข แล้วดู min/max จริง
vals = [float(f.subs(x, sp.Rational(k, 400))) for k in range(-400, 401)]
chk('กวาดตัวเลข · min', sp.Float(min(vals)), sp.Float(float(-pi / 2)), tol=1e-9)
chk('กวาดตัวเลข · max', sp.Float(max(vals)), sp.Float(float(5 * pi / 2)), tol=1e-9)
# ชั้น 2b · ต่อเนื่องบน [-1,1] ⇒ เรนจ์เป็นช่วงปิดทั้งช่วง (ตรวจว่าค่ากลางถูกชน)
mid = f.subs(x, 0)
chk('f(0) อยู่กลางช่วงจริง', sp.simplify(mid), pi)

# ตัวลวง
d_asin = [3 * (-pi / 2) - pi / 2, 3 * (pi / 2) - pi / 2]   # ใช้เรนจ์ของ arcsin ผิดตัว
chk('ตัวลวง A (ใช้เรนจ์ arcsin) ปลายซ้าย', sp.simplify(d_asin[0]), -2 * pi)
chk('ตัวลวง A ปลายขวา', sp.simplify(d_asin[1]), pi)
d_no3 = [0 - pi / 2, pi - pi / 2]                          # ลืมคูณ 3
chk('ตัวลวง B (ลืมคูณ 3) ปลายขวา', sp.simplify(d_no3[1]), pi / 2)
# ตัวลวง C = [0, pi] คือเรนจ์ของ arccos ล้วน ๆ (ลืมทั้งคูณและลบ)

# ═══════════════════════════════════════════════════════════════════════════
print()
print('== q086 · ระยะระหว่างปลายเข็มนาฬิกา เวลา 4 นาฬิกาตรง ==')
h, m = sp.Integer(3), sp.Integer(5)          # เข็มสั้น 3 ซม. · เข็มยาว 5 ซม.
theta = 4 * sp.Rational(360, 12) * pi / 180  # 4 ช่วงชั่วโมง ช่วงละ 30 องศา
chk('มุมระหว่างเข็ม', sp.simplify(theta), 2 * pi / 3)

# ชั้น 1 · กฎโคไซน์
d2 = h**2 + m**2 - 2 * h * m * sp.cos(theta)
chk('d^2 จากกฎโคไซน์', sp.simplify(d2), sp.Integer(49))
chk('d', sp.sqrt(sp.simplify(d2)), sp.Integer(7))

# ชั้น 2 · วิธีอิสระ : วางพิกัดจริงบนหน้าปัด แล้วใช้ระยะระหว่างจุด
#   เข็มยาวชี้เลข 12 (มุม 90 องศาจากแกน x) · เข็มสั้นชี้เลข 4 (90 - 120 = -30 องศา)
Pm = (m * sp.cos(pi / 2), m * sp.sin(pi / 2))
Ph = (h * sp.cos(-pi / 6), h * sp.sin(-pi / 6))
dist = sp.sqrt((Pm[0] - Ph[0])**2 + (Pm[1] - Ph[1])**2)
chk('ระยะจากพิกัดจริง (วิธีอิสระ)', sp.simplify(dist), sp.Integer(7))

# ตัวลวง
chk('ตัวลวง A (เซ็น cos ผิด ⇒ ใช้ +1/2)', sp.sqrt(h**2 + m**2 - 2 * h * m * sp.Rational(1, 2)),
    sp.sqrt(19))
chk('ตัวลวง B (คิดว่ามุมฉาก ⇒ พีทาโกรัส)', sp.sqrt(h**2 + m**2), sp.sqrt(34))
chk('ตัวลวง C (บวกความยาวเข็ม)', h + m, sp.Integer(8))
print('  ลำดับจากน้อยไปมาก :', [float(v) for v in
      (sp.sqrt(19), sp.sqrt(34), sp.Integer(7), sp.Integer(8))])

# ═══════════════════════════════════════════════════════════════════════════
print()
print('== q087 · cos(A+B) = 3/5 · cos(A-B) = 4/5 ⇒ tan A tan B ==')
S, D = sp.Rational(3, 5), sp.Rational(4, 5)

# ชั้น 1 · บวก-ลบสองสมการเพื่อแยก cosAcosB กับ sinAsinB
cc = (D + S) / 2
ss = (D - S) / 2
chk('cos A cos B', cc, sp.Rational(7, 10))
chk('sin A sin B', ss, sp.Rational(1, 10))
chk('tan A tan B', sp.simplify(ss / cc), sp.Rational(1, 7))

# ชั้น 2 · วิธีอิสระ : หามุม A, B จริงเชิงตัวเลขแล้วคูณ tan ตรง ๆ
AB = sp.acos(S)      # A + B
AmB = sp.acos(D)     # A - B
A = sp.simplify((AB + AmB) / 2)
B = sp.simplify((AB - AmB) / 2)
chk('มุมจริง ⇒ tan A · tan B (วิธีอิสระ)',
    sp.Float(float(sp.tan(A) * sp.tan(B))), sp.Float(1.0 / 7), tol=1e-12)
chk('ตรวจย้อน cos(A+B)', sp.Float(float(sp.cos(A + B))), sp.Float(0.6), tol=1e-12)
chk('ตรวจย้อน cos(A-B)', sp.Float(float(sp.cos(A - B))), sp.Float(0.8), tol=1e-12)

# ชั้น 2b · พยานเชิงสัญลักษณ์ : A = pi/4 และ B = arctan(1/7) สอดคล้องกับโจทย์ทั้งสองเงื่อนไข
Aw, Bw = pi / 4, sp.atan(sp.Rational(1, 7))
chk('พยาน · cos(A+B) = 3/5', sp.simplify(sp.cos(Aw + Bw)), sp.Rational(3, 5))
chk('พยาน · cos(A-B) = 4/5', sp.simplify(sp.cos(Aw - Bw)), sp.Rational(4, 5))
chk('พยาน · tan A tan B', sp.simplify(sp.tan(Aw) * sp.tan(Bw)), sp.Rational(1, 7))

# ตัวลวง
chk('ตัวลวง A (จำสูตรสลับเครื่องหมาย ⇒ ss = -1/10)', sp.Rational(-1, 10) / cc,
    sp.Rational(-1, 7))
chk('ตัวลวง B (หารกลับหัว)', sp.simplify(cc / ss), sp.Integer(7))
chk('ตัวลวง C (ลบสองสมการแล้วตอบเลย)', D - S, sp.Rational(1, 5))

# ═══════════════════════════════════════════════════════════════════════════
print()
print('== q088 · ความยาวเส้นแบ่งครึ่งมุม AD · AB=10 · AC=15 · A=pi/3 ==')
c_, b_, A_ = sp.Integer(10), sp.Integer(15), pi / 3

# ชั้น 1 · แบ่งพื้นที่ : [ABD] + [ACD] = [ABC]
t = sp.Symbol('t', positive=True)
eq = sp.Eq(sp.Rational(1, 2) * c_ * t * sp.sin(A_ / 2)
           + sp.Rational(1, 2) * b_ * t * sp.sin(A_ / 2),
           sp.Rational(1, 2) * b_ * c_ * sp.sin(A_))
AD = sp.simplify(sp.solve(eq, t)[0])
chk('AD จากการแบ่งพื้นที่', AD, 6 * sp.sqrt(3))
chk('AD ตรงกับสูตร 2bc cos(A/2)/(b+c)',
    sp.simplify(2 * b_ * c_ * sp.cos(A_ / 2) / (b_ + c_)), 6 * sp.sqrt(3))

# ชั้น 2 · วิธีอิสระ : พิกัดจริง · A ที่จุดกำเนิด · AB บนแกน x · หา D จากอัตราส่วน BD:DC = c:b
Apt = sp.Matrix([0, 0])
Bpt = sp.Matrix([c_, 0])
Cpt = sp.Matrix([b_ * sp.cos(A_), b_ * sp.sin(A_)])
Dpt = (b_ * Bpt + c_ * Cpt) / (b_ + c_)          # ทฤษฎีบทเส้นแบ่งครึ่งมุม BD:DC = AB:AC
AD2 = sp.simplify(sp.sqrt((Dpt - Apt).dot(Dpt - Apt)))
chk('AD จากพิกัดจริง (วิธีอิสระ)', AD2, 6 * sp.sqrt(3))
# ตรวจว่า AD แบ่งมุมครึ่งจริง
ang_BAD = sp.acos(sp.simplify((Bpt.dot(Dpt)) / (Bpt.norm() * Dpt.norm())))
chk('มุม BAD = A/2 จริง', sp.simplify(ang_BAD), pi / 6)

BC = sp.sqrt(b_**2 + c_**2 - 2 * b_ * c_ * sp.cos(A_))
chk('BC (ใช้เป็นตัวลวง)', sp.simplify(BC), 5 * sp.sqrt(7))

# ตัวลวง
chk('ตัวลวง A (ใช้มุมเต็ม A ในรูปย่อยทั้งสอง ⇒ t(b+c) = bc)',
    sp.simplify(b_ * c_ / (b_ + c_)), sp.Integer(6))
chk('ตัวลวง B (ทิ้ง cos(A/2) ⇒ 2bc/(b+c))',
    sp.simplify(2 * b_ * c_ / (b_ + c_)), sp.Integer(12))
print('  ลำดับจากน้อยไปมาก :', [float(v) for v in
      (sp.Integer(6), 6 * sp.sqrt(3), sp.Integer(12), 5 * sp.sqrt(7))])

# ═══════════════════════════════════════════════════════════════════════════
print()
print('== q089 · แพะผูกเชือกที่มุมโรงเรือน 6 x 4 · เชือก 7 ==')
L, p, q = sp.Integer(7), sp.Integer(6), sp.Integer(4)
chk('เชือกสั้นกว่าผลรวมสองด้าน (พันไม่ครบรอบ)', sp.Integer(1 if L < p + q else 0), sp.Integer(1))
chk('เชือกที่เหลือหลังพันมุมด้านยาว', L - p, sp.Integer(1))
chk('เชือกที่เหลือหลังพันมุมด้านสั้น', L - q, sp.Integer(3))
chk('ไม่ซ้อนกัน : (L-p) < q', sp.Integer(1 if (L - p) < q else 0), sp.Integer(1))
chk('ไม่ซ้อนกัน : (L-q) < p', sp.Integer(1 if (L - q) < p else 0), sp.Integer(1))

# ชั้น 1 · สามเซกเตอร์
main = sp.Rational(3, 4) * pi * L**2
w1 = sp.Rational(1, 4) * pi * (L - p)**2
w2 = sp.Rational(1, 4) * pi * (L - q)**2
total = sp.simplify(main + w1 + w2)
chk('พื้นที่รวม', total, 157 * pi / 4)

# ชั้น 2 · วิธีอิสระ : มอนติคาร์โลบนกริดละเอียด (ระยะทางเดินอ้อมมุมจริง)
import math
BX, BY = 6.0, 4.0          # โรงเรือนกินพื้นที่ [0,6] x [0,4] · แพะผูกที่ (0,0)


def reachable(px, py, rope=7.0):
    inside = (0.0 < px < BX) and (0.0 < py < BY)
    if inside:
        return False
    d = math.hypot(px, py)
    if px >= 0.0 and py >= 0.0 and (px > BX or py > BY or px == 0.0 or py == 0.0):
        pass
    # เส้นตรงจากมุม (0,0) ถูกกั้นไหม : ถูกกั้นเมื่อจุดอยู่ใน "เงา" ของสี่เหลี่ยม
    blocked = (px > 0.0 and py > 0.0) and (px < BX or py < BY)
    if not blocked:
        return d <= rope
    # ต้องอ้อมมุมใดมุมหนึ่ง
    if py <= BY:                      # อ้อมมุม (BX, 0) ตามด้านยาว
        return BX + math.hypot(px - BX, py) <= rope
    return BY + math.hypot(px, py - BY)  <= rope


N, R = 1400, 7.5
cell = (2 * R / N) ** 2
cnt = 0
for i in range(N):
    px = -R + (i + 0.5) * 2 * R / N
    for j in range(N):
        py = -R + (j + 0.5) * 2 * R / N
        if reachable(px, py):
            cnt += 1
approx = cnt * cell
chk('มอนติคาร์โล/กริด (วิธีอิสระ)', sp.Float(approx), sp.Float(float(157 * math.pi / 4)),
    tol=0.05)

# ตัวลวง
chk('ตัวลวง A (ลืมเชือกพันมุม)', sp.simplify(main), 147 * pi / 4)
chk('ตัวลวง B (ใช้ครึ่งวงกลมที่มุมที่พัน)',
    sp.simplify(main + sp.Rational(1, 2) * pi * ((L - p)**2 + (L - q)**2)), 167 * pi / 4)
chk('ตัวลวง C (คิดเป็นวงกลมเต็ม ลืมว่าโรงเรือนกั้น)', sp.simplify(pi * L**2), 49 * pi)
print('  ลำดับจากน้อยไปมาก :', [float(v) for v in
      (147 * pi / 4, 157 * pi / 4, 167 * pi / 4, 49 * pi)])

print()
print('ผลรวม :', '✅ ผ่านทุกข้อ' if ok else '❌ มีข้อไม่ผ่าน')
raise SystemExit(0 if ok else 1)

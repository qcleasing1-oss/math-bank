# -*- coding: utf-8 -*-
"""STEP D · ตรวจคำตอบและตัวลวงของก้อน 13 (q070–q074) ด้วย sympy

กฎเหล็กข้อ 1 : ห้ามเชื่อการคำนวณมือ ทุกค่าต้อง verify เชิงสัญลักษณ์
กฎเหล็กข้อ 2 : ตัวลวงทุกตัวต้องคำนวณจาก "เส้นทางพลาดจริง" ไม่ใช่เลขใกล้เคียง
บทเรียนก้อน 12 : ต้องมีด่านกัน "ตัวลวงตายยกแผง" (estimation-degenerate)
                 — ถ้าขอบเขตสามัญสำนึกอันเดียวฆ่าตัวลวงได้หมด ข้อนั้นกลายเป็นข้อเดา
"""
import sympy as sp

ok = True


def chk(tag, got, want, note=''):
    global ok
    good = sp.simplify(sp.nsimplify(got) - sp.nsimplify(want)) == 0
    ok &= good
    print('   %-52s %-24s %s %s' % (tag, str(got), 'ตรง' if good else '❌ ไม่ตรง', note))


def guard(tag, cond, why):
    global ok
    ok &= bool(cond)
    print('   %-52s %s   %s' % (tag, 'ผ่าน' if cond else '❌ ตก', why))


# ══════════════════════════════════════════════════════════════════════════════
print()
print('q070 · ง่าย · 7.9 · ด้าน 3, 5, 7 ⇒ cos ของมุมตรงข้ามด้านยาวที่สุด')
a, b, c = sp.Integer(3), sp.Integer(5), sp.Integer(7)
cosC = (a**2 + b**2 - c**2) / (2 * a * b)
chk('คำตอบ · cos C = (3^2+5^2-7^2)/(2*3*5)', cosC, sp.Rational(-1, 2))
# เส้นทางอิสระ : สร้างสามเหลี่ยมด้วยพิกัดแล้วใช้ผลคูณจุด
C_ = sp.acos(cosC)
chk('ตรวจอิสระ · มุม C จาก acos', sp.deg(C_), 120)
chk('ตรวจอิสระ · c^2 = a^2+b^2-2ab cos C', a**2 + b**2 - 2 * a * b * sp.cos(C_), 49)
# ตัวลวง
chk('ลวง ② +1/2 · ลืมเครื่องหมายลบ (49-9-25)/30', (c**2 - a**2 - b**2) / (2 * a * b),
    sp.Rational(1, 2))
chk('ลวง ③ 11/14 · cos ของมุมตรงข้ามด้าน 5 แทน', (a**2 + c**2 - b**2) / (2 * a * c),
    sp.Rational(11, 14))
chk('ลวง ④ 13/14 · cos ของมุมตรงข้ามด้าน 3 แทน', (b**2 + c**2 - a**2) / (2 * b * c),
    sp.Rational(13, 14))
guard('ด่านกันข้อเดา · มีตัวลวงบวกอยู่ 3 ตัว',
      len([v for v in [sp.Rational(1, 2), sp.Rational(11, 14), sp.Rational(13, 14)] if v > 0]) == 3,
      'เครื่องหมายลบไม่ใช่ตัวคัดทิ้งอัตโนมัติ เพราะเด็กต้องรู้ว่ามุมป้านก่อน')
guard('สามเหลี่ยมมีจริง (3+5>7)', 3 + 5 > 7, 'อสมการสามเหลี่ยม')

# ══════════════════════════════════════════════════════════════════════════════
print()
print('q071 · ง่าย · 7.1 · (sin^2(pi/6) + tan^2(pi/3)) / cos^2(pi/4)')
E = (sp.sin(sp.pi / 6)**2 + sp.tan(sp.pi / 3)**2) / sp.cos(sp.pi / 4)**2
chk('คำตอบ · ค่าของนิพจน์', sp.simplify(E), sp.Rational(13, 2))
chk('ตรวจอิสระ · แทนค่าเป็นทศนิยม', sp.nsimplify(sp.N(E, 20), rational=True), sp.Rational(13, 2))
chk('ลวง ① 7 · ลืมยกกำลังสองของ sin(pi/6) (ใช้ 1/2 แทน 1/4)',
    (sp.sin(sp.pi / 6) + sp.tan(sp.pi / 3)**2) / sp.cos(sp.pi / 4)**2, 7)
chk('ลวง ② 7/6 · สลับ tan(pi/3) เป็น tan(pi/6)',
    (sp.sin(sp.pi / 6)**2 + sp.tan(sp.pi / 6)**2) / sp.cos(sp.pi / 4)**2, sp.Rational(7, 6))
chk('ลวง ③ 13/8 · คูณด้วย cos^2(pi/4) แทนการหาร',
    (sp.sin(sp.pi / 6)**2 + sp.tan(sp.pi / 3)**2) * sp.cos(sp.pi / 4)**2, sp.Rational(13, 8))

# ══════════════════════════════════════════════════════════════════════════════
print()
print('q072 · ปานกลาง · 7.9 · AB=5 · AC=6 · A=2pi/3 · M กึ่งกลาง AC ⇒ BM')
AB, AC, A = sp.Integer(5), sp.Integer(6), sp.Rational(2, 3) * sp.pi
AM = AC / 2
BM2 = AB**2 + AM**2 - 2 * AB * AM * sp.cos(A)
chk('คำตอบ · BM', sp.sqrt(sp.simplify(BM2)), 7)
# เส้นทางอิสระ : วางพิกัด A ที่จุดกำเนิด
Ax, Ay = 0, 0
Bx, By = AB, 0
Cx, Cy = AC * sp.cos(A), AC * sp.sin(A)
Mx, My = Cx / 2, Cy / 2
chk('ตรวจอิสระ · ระยะทางเชิงพิกัด', sp.sqrt(sp.simplify((Bx - Mx)**2 + (By - My)**2)), 7)
chk('ลวง ② sqrt(19) · ใช้ cos A = +1/2', sp.sqrt(AB**2 + AM**2 - 2 * AB * AM * sp.Rational(1, 2)),
    sp.sqrt(19))
chk('ลวง ③ sqrt(34) · ตัดพจน์ -2ab cos A ทิ้ง (คิดว่ามุมฉาก)', sp.sqrt(AB**2 + AM**2), sp.sqrt(34))
chk('ลวง ④ sqrt(91) · ลืมจุดกึ่งกลาง ใช้ AC เต็ม ⇒ ได้ BC',
    sp.sqrt(sp.simplify(AB**2 + AC**2 - 2 * AB * AC * sp.cos(A))), sp.sqrt(91))
guard('ด่านกันข้อเดา · BM ต้องน้อยกว่า BC', 7 < sp.sqrt(91),
      'sqrt(91) = 9.54 ⇒ ตัวลวงตัวใหญ่ยังสมเหตุสมผล ไม่ถูกตัดด้วยสายตา')
guard('ด่านกันข้อเดา · ตัวลวงทั้งสามอยู่ในช่วง (2, 10)',
      all(2 < sp.N(v) < 10 for v in [sp.sqrt(19), sp.sqrt(34), sp.sqrt(91)]),
      'ไม่มีตัวไหนถูกขอบเขตสามัญสำนึกฆ่าทิ้ง')

# ══════════════════════════════════════════════════════════════════════════════
print()
print('q073 · ยาก · 7.10 · เสาตั้งฉากพื้นที่ O · มุม AOB ฉาก · เงย 45 กับ 30 · AB = 24')
h = sp.symbols('h', positive=True)
OA = h / sp.tan(sp.rad(45))
OB = h / sp.tan(sp.rad(30))
sol = sp.solve(sp.Eq(OA**2 + OB**2, 24**2), h)
chk('คำตอบ · ความสูงเสา h', sol[0], 12)
# เส้นทางอิสระ : วางพิกัดสามมิติ O = (0,0,0) · A บนแกน x · B บนแกน y · P = (0,0,h)
hv = sp.Integer(12)
Ap = sp.Matrix([hv, 0, 0])
Bp = sp.Matrix([0, hv * sp.sqrt(3), 0])
Pp = sp.Matrix([0, 0, hv])
chk('ตรวจอิสระ · |AB| เชิงพิกัด', (Ap - Bp).norm(), 24)
chk('ตรวจอิสระ · มุมเงยจาก A', sp.deg(sp.atan(hv / Ap.norm())), 45)
chk('ตรวจอิสระ · มุมเงยจาก B', sp.deg(sp.atan(hv / Bp.norm())), 30)
chk('ตรวจอิสระ · มุม AOB เป็นมุมฉาก (ผลคูณจุด)', Ap.dot(Bp), 0)
chk('ลวง ① 12sqrt3 · สลับอัตราส่วน ใช้ OB = h tan30',
    sp.solve(sp.Eq(h**2 + (h / sp.sqrt(3))**2, 24**2), h)[0], 12 * sp.sqrt(3))
chk('ลวง ② 12sqrt2 · ใช้พีทาโกรัสผิดข้าง OB^2 = OA^2 + AB^2',
    sp.solve(sp.Eq(3 * h**2, h**2 + 24**2), h)[0], 12 * sp.sqrt(2))
chk('ลวง ④ 12(sqrt3-1) · คิดว่า A, O, B อยู่ในแนวเส้นตรง ⇒ OA + OB = AB',
    sp.simplify(sp.solve(sp.Eq(h + h * sp.sqrt(3), 24), h)[0]), 12 * sp.sqrt(3) - 12)
guard('ด่านกันข้อเดา · ตัวลวงทุกตัวยังน้อยกว่า AB = 24',
      all(sp.N(v) < 24 for v in [12 * sp.sqrt(3), 12 * sp.sqrt(2), 12 * sp.sqrt(3) - 12]),
      'ขอบเขต h < AB ฆ่าตัวลวงไม่ได้สักตัว ⇒ ต้องคำนวณจริงถึงจะตอบได้')
guard('ด่านกันข้อเดา · ค่าทั้งสี่ต่างกันจริง',
      len(set([sp.N(v, 12) for v in [12, 12 * sp.sqrt(3), 12 * sp.sqrt(2),
                                     12 * sp.sqrt(3) - 12]])) == 4, 'ไม่มีคู่ที่เท่ากัน')

# ══════════════════════════════════════════════════════════════════════════════
print()
print('q074 · ยากมาก · 7.9 · a, b, c เป็นลำดับเรขาคณิต ⇒ เซตของขนาดมุม B')
r = sp.symbols('r', positive=True)
aa, bb, cc = sp.Integer(1), r, r**2          # ด้าน a, b, c เป็นลำดับเรขาคณิตอัตราส่วน r
cosB = sp.simplify((aa**2 + cc**2 - bb**2) / (2 * aa * cc))
chk('รูปทั่วไปของ cos B', cosB, (1 + r**4 - r**2) / (2 * r**2))
chk('เขียนใหม่เป็น (u-1)/2 เมื่อ u = r^2 + 1/r^2',
    sp.simplify(cosB - ((r**2 + 1 / r**2) - 1) / 2), 0)
chk('ค่าต่ำสุดของ cos B ที่ r = 1 (AM-GM ให้ u >= 2)', cosB.subs(r, 1), sp.Rational(1, 2))
guard('AM-GM · u = r^2 + 1/r^2 - 2 = (r - 1/r)^2 >= 0',
      sp.simplify(r**2 + 1 / r**2 - 2 - (r - 1 / r)**2) == 0, 'เท่ากันเมื่อ r = 1 เท่านั้น')
# ขอบเขตบนของ B มาจากอสมการสามเหลี่ยม 1 + r > r^2 (กรณี r >= 1)
phi = (1 + sp.sqrt(5)) / 2
chk('รากบวกของ r^2 - r - 1 = 0 (ขอบของอสมการสามเหลี่ยม)', sp.solve(r**2 - r - 1, r)[-1], phi)
chk('ที่ r -> phi · u = r^2 + 1/r^2 เข้าสู่ 3', sp.simplify((phi**2 + 1 / phi**2)), 3)
chk('⇒ cos B -> (3-1)/2 = 1 ⇒ B -> 0', sp.simplify((phi**2 + 1 / phi**2 - 1) / 2), 1)
guard('ช่วงของ r ที่อสมการสามเหลี่ยมเป็นจริง = ช่วงที่ u < 3 พอดี',
      sp.simplify(sp.solve(r**4 - 3 * r**2 + 1, r)[-1] - phi) == 0,
      'r^4-3r^2+1 = 0 มีรากบวกใหญ่สุด = phi ⇒ สองเงื่อนไขให้ช่วงเดียวกัน ⇒ B ได้ครบ (0, pi/3]')
chk('B สูงสุด = arccos(1/2)', sp.deg(sp.acos(sp.Rational(1, 2))), 60)
# ตรวจเชิงตัวเลข : กวาด r แล้วดูว่ามุม B ไม่เคยเกิน pi/3 และเข้าใกล้ 0 ได้
vals = []
for k in range(1, 400):
    rv = sp.Rational(k, 200)                       # r = 0.005 … 1.995
    if not (1 + rv > rv**2 and 1 + rv**2 > rv and rv + rv**2 > 1):
        continue
    cb = sp.N((1 + rv**4 - rv**2) / (2 * rv**2))
    vals.append(sp.N(sp.acos(cb)))
guard('กวาดตัวเลข · ไม่มี r ใดให้ B > pi/3', max(vals) <= sp.N(sp.pi / 3) + sp.Rational(1, 10**9),
      'ค่าสูงสุดที่กวาดได้ = %.6f (pi/3 = %.6f)' % (float(max(vals)), float(sp.N(sp.pi / 3))))
guard('กวาดตัวเลข · B แตะ pi/3 ได้จริงที่ r = 1',
      abs(sp.N(sp.acos(sp.Rational(1, 2))) - sp.N(sp.pi / 3)) < 1e-12, 'สามเหลี่ยมด้านเท่า')
# ⚠️ กวาดแบบขั้นละ 0.005 เข้าไม่ถึงขอบ r -> phi ⇒ ต้องยิงตรงเข้าหาขอบเพื่อยืนยันว่าช่วงเปิดจริง
tail = []
for e in range(2, 9):
    rv = sp.nsimplify(phi) - sp.Rational(1, 10**e)
    assert 1 + rv > rv**2                                   # ยังเป็นสามเหลี่ยมอยู่
    tail.append(sp.N(sp.acos(sp.N((1 + rv**4 - rv**2) / (2 * rv**2), 40)), 40))
guard('ยิงตรงที่ขอบ · r -> phi^- แล้ว B -> 0 (ช่วงเปิดข้างล่างจริง)',
      min(tail) < sp.Rational(1, 1000) and all(tail[i] > tail[i + 1] for i in range(len(tail) - 1)),
      'B ที่ r = phi - 1e-8 ได้ %.3e และลดลงเรื่อย ๆ ⇒ ไม่มีค่าต่ำสุด' % float(min(tail)))
guard('ด่านกันข้อเดา · ตัวลวง (0, pi/2] ไม่ถูกตัดด้วยสายตา',
      sp.N(sp.pi / 3) < sp.N(sp.pi / 2),
      'เด็กที่สรุปแค่ว่า b ไม่ใช่ด้านยาวสุด ⇒ B ไม่ใช่มุมป้าน จะได้ตัวนี้')

print()
print('=' * 78)
print('ผลรวม :', 'ผ่านทุกจุด ✅' if ok else '❌ มีจุดไม่ตรง — ห้ามแต่งต่อ')
print('=' * 78)

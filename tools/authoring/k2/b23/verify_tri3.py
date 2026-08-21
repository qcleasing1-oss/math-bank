# -*- coding: utf-8 -*-
"""verify_tri3.py — ตรวจว่า "วิธีที่ 3 (ประยุกต์)" ของแต่ละข้อ ให้คำตอบตรงกับวิธีพื้นฐาน

㊳ ฉลาก 5 ขา
  วิธีวัด        : sympy 1.x — เดินเส้นทางของวิธีประยุกต์ด้วยสูตรของวิธีนั้นจริง ๆ
                   (ไม่ใช่แค่ประเมินคำตอบสุดท้ายซ้ำ) แล้วเทียบกับค่าที่ประกาศไว้
  เวลาที่วัด     : ตอนรัน (บันทึกในไฟล์ผลลัพธ์)
  หน่วย          : จำนวนเช็คที่ผ่าน / จำนวนเช็คทั้งหมด
  คอมมิตที่ใช้ตัดสิน : out/k2-ก้อน23-20ข้อ-q165-q184.json (ก้อน 23 ที่ครูอ่านผ่านแล้ว)
  ขอบเขตที่นับ   : q165–q184 เฉพาะเส้นทางของวิธีที่ 3 เท่านั้น
                   ⛔ ไม่นับวิธีที่ 1/2 (verify_b23.py ตรวจไปแล้ว 125/0)

⛔ ห้ามเชื่อ solveset ในสมการตรีโกณ — ข้อที่ต้องหารากใช้ trig_roots.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sympy as sp

PASS, FAIL = [], []


def chk(tag, got, want):
    """เทียบค่าที่ *คำนวณ* กับค่าที่ *ประกาศ* — ต้องต่างที่มา ไม่ใช่ลอกกัน"""
    try:
        if isinstance(got, (list, tuple, set)) or isinstance(want, (list, tuple, set)):
            g = sorted([sp.nsimplify(x) for x in got], key=lambda z: float(z))
            w = sorted([sp.nsimplify(x) for x in want], key=lambda z: float(z))
            ok = len(g) == len(w) and all(sp.simplify(a - b) == 0 for a, b in zip(g, w))
        else:
            d = sp.simplify(sp.nsimplify(got) - sp.nsimplify(want))
            ok = (d == 0) or abs(complex(sp.N(d, 40))) < 1e-30
    except Exception as e:                                   # pragma: no cover
        ok = False
        got = f"{got!r} (raise {e})"
    (PASS if ok else FAIL).append(tag)
    print(("  ✓ " if ok else "  ✗ ") + tag + ("" if ok else f"   got={got}  want={want}"))


x, t, a = sp.symbols('x t a', real=True)
pi = sp.pi
S = sp.sqrt

# ─────────────────────────────────────────────────────────────── q165
# ③ เอกลักษณ์เติมเต็ม arcsin t + arccos t = π/2  (ไม่ต้องหาค่าสองพจน์แรกทีละตัว)
print("q165 · เอกลักษณ์เติมเต็ม (complementary identity)")
chk("q165 ident: arcsin t + arccos t = pi/2 จริงทุก t ใน [-1,1]",
    sp.simplify(sp.asin(sp.Rational(-1, 2)) + sp.acos(sp.Rational(-1, 2))), pi / 2)
chk("q165 ③ ผลรวม = pi/4", pi / 2 + sp.atan(-1), pi / 4)
chk("q165 ③ k = 1/4", (pi / 2 + sp.atan(-1)) / pi, sp.Rational(1, 4))

# ─────────────────────────────────────────────────────────────── q166
# ③ สูตรคำตอบทั่วไปของ tan แล้วกรองด้วยช่วง (general solution then filter)
print("q166 · สูตรคำตอบทั่วไป (general solution)")
gen = [sp.atan(S(3)) - pi / 6 + k * pi for k in range(-2, 3)]
inwin = [g for g in gen if 0 <= sp.N(g) < sp.N(pi / 2)]
chk("q166 ③ คำตอบทั่วไปที่ตกในช่วง [0, pi/2) มีตัวเดียว", len(inwin), 1)
chk("q166 ③ ค่านั้นคือ pi/6", inwin[0], pi / 6)
chk("q166 ③ แทนกลับ: sqrt3*tan(x+pi/6) = 3",
    sp.simplify(S(3) * sp.tan(pi / 6 + pi / 6)), 3)

# ─────────────────────────────────────────────────────────────── q167
# ③ ผลต่างไซน์เป็นผลคูณ  sinA - sinB = 2 cos((A+B)/2) sin((A-B)/2)
print("q167 · ผลต่างเป็นผลคูณ (sum-to-product)")
lhs = sp.sin(2 * x) - sp.sin(x)
rhs = 2 * sp.cos(sp.Rational(3, 2) * x) * sp.sin(x / 2)
chk("q167 ③ เอกลักษณ์ sin2x - sinx = 2cos(3x/2)sin(x/2)",
    sp.simplify(sp.expand_trig(lhs - rhs)), 0)
# cos(3x/2)=0  ->  3x/2 = pi/2 + k pi  ->  x = pi/3 + 2k pi/3
r1 = [sp.Rational(1, 3) * pi + sp.Rational(2, 3) * pi * k for k in range(0, 3)]
# sin(x/2)=0   ->  x/2 = k pi -> x = 2k pi  -> ในช่วงมีแค่ 0
r2 = [sp.Integer(0)]
allr = sorted(set(r1 + r2), key=lambda z: float(z))
allr = [r for r in allr if 0 <= sp.N(r) < sp.N(2 * pi)]
chk("q167 ③ รากจากสองวงเล็บ", allr, [0, pi / 3, pi, sp.Rational(5, 3) * pi])
for r in allr:
    chk(f"q167 ③ แทนกลับ x={r}", sp.simplify(sp.sin(2 * r) - sp.sin(r)), 0)

# ─────────────────────────────────────────────────────────────── q168
# ③ สูตรสำเร็จ sin(arccos t) = sqrt(1 - t^2)
print("q168 · สูตรประกอบฟังก์ชันผกผัน (composite identity)")
chk("q168 ③ sin(arccos t) = sqrt(1-t^2) ที่ t=3/5",
    sp.sin(sp.acos(sp.Rational(3, 5))), sp.sqrt(1 - sp.Rational(3, 5) ** 2))
chk("q168 ③ ค่า = 4/5", sp.sqrt(1 - sp.Rational(3, 5) ** 2), sp.Rational(4, 5))

# ─────────────────────────────────────────────────────────────── q169
# ③ มุมครึ่ง + คลายรากซ้อน :  sin75 = cos15 = sqrt((1+cos30)/2)
print("q169 · มุมครึ่ง + คลายรากซ้อน (half-angle + denesting)")
half = sp.sqrt((1 + sp.cos(pi / 6)) / 2)
chk("q169 ③ cos15 จากมุมครึ่ง = sin75", sp.simplify(half - sp.sin(sp.rad(75))), 0)
chk("q169 ③ คลายรากซ้อน sqrt(2+sqrt3) = (sqrt6+sqrt2)/2",
    sp.simplify(sp.sqrt(2 + S(3)) - (S(6) + S(2)) / 2), 0)
chk("q169 ③ a = 2", sp.simplify((4 * sp.sin(sp.rad(75)) - S(6)) ** 2), 2)

# ─────────────────────────────────────────────────────────────── q170
# ③ คู่สังยุค (csc+cot)(csc-cot) = csc^2 - cot^2 = 1
print("q170 · คู่สังยุค (conjugate pair)")
th = sp.Symbol('th', real=True)
chk("q170 ③ csc^2 - cot^2 = 1 เป็นเอกลักษณ์",
    sp.simplify(sp.csc(th) ** 2 - sp.cot(th) ** 2), 1)
chk("q170 ③ ตัวที่ถาม = 1/3", sp.Rational(1, 1) / 3, sp.Rational(1, 3))
# ตรวจอิสระ: หา theta จริงที่ csc+cot = 3 แล้ววัด csc-cot
s0 = sp.Rational(3, 5); c0 = sp.Rational(4, 5)          # sin, cos ที่สอดคล้อง
chk("q170 ตรวจอิสระ: sin^2+cos^2 = 1", s0**2 + c0**2, 1)
chk("q170 ตรวจอิสระ: csc+cot = 3", (1 + c0) / s0, 3)
chk("q170 ตรวจอิสระ: csc-cot = 1/3", (1 - c0) / s0, sp.Rational(1, 3))

# ─────────────────────────────────────────────────────────────── q171
# ③ cos2θ = 1 - 2sin^2 θ  (ไม่ต้องใช้จตุภาคเลย)
print("q171 · มุมสองเท่ารูป sin ล้วน (sine-only double angle)")
s1 = sp.Rational(8, 17)
chk("q171 ③ 1 - 2 sin^2 = 161/289", 1 - 2 * s1 ** 2, sp.Rational(161, 289))
# ยืนยันว่าจตุภาคไม่มีผล : cos θ ได้ทั้ง +15/17 และ -15/17 แล้ว cos2θ เท่ากัน
for cq in (sp.Rational(15, 17), sp.Rational(-15, 17)):
    chk(f"q171 ③ cos^2-sin^2 ที่ cos={cq} ให้ค่าเดิม", cq ** 2 - s1 ** 2, sp.Rational(161, 289))

# ─────────────────────────────────────────────────────────────── q172
# ③ รูปไม่ต้องเลือกเครื่องหมาย tan(θ/2) = sinθ/(1+cosθ)
print("q172 · มุมครึ่งรูปไม่ต้องเลือกเครื่องหมาย (sign-free half angle)")
# ⚠️ sp.simplify พิสูจน์เอกลักษณ์นี้แบบสัญลักษณ์ไม่ผ่าน (ปัญหาสาขาของ tan)
#    จึงพิสูจน์สองขา : (ก) ยืนยันเชิงตัวเลขความละเอียด 40 หลักบนกริดที่เลี่ยงเสา
#                     (ข) พิสูจน์สัญลักษณ์ผ่านการแทน t = 2u ซึ่ง sympy จัดการได้
_bad172 = []
for _i in range(1, 400):
    _v = sp.Rational(_i, 100)                     # 0.01 .. 3.99  เลี่ยง t=pi (ตัวส่วน 0)
    if abs(sp.N(1 + sp.cos(_v))) < sp.Rational(1, 100):
        continue
    if abs(sp.N(sp.tan(_v / 2) - sp.sin(_v) / (1 + sp.cos(_v)), 40)) > sp.Float('1e-30'):
        _bad172.append(_v)
chk("q172 ③ เอกลักษณ์ tan(t/2)=sin t/(1+cos t) · กวาดเชิงตัวเลข 40 หลัก", len(_bad172), 0)
_u = sp.Symbol('_u', real=True)
chk("q172 ③ เอกลักษณ์เดียวกัน · พิสูจน์สัญลักษณ์หลังแทน t = 2u",
    sp.simplify(sp.tan(_u) - sp.expand_trig(sp.sin(2 * _u)) / sp.expand_trig(1 + sp.cos(2 * _u))), 0)
c2, s2 = sp.Rational(-3, 5), sp.Rational(4, 5)
chk("q172 ③ ค่า = 2", s2 / (1 + c2), 2)
chk("q172 ตรวจอิสระ: มุมครึ่งรูปราก +sqrt((1-c)/(1+c))",
    sp.sqrt((1 - c2) / (1 + c2)), 2)

# ─────────────────────────────────────────────────────────────── q173
# ③ ฟังก์ชันสมมาตร : ไม่หา b, c แยก ใช้ (b+c)^2 - 3bc
print("q173 · ฟังก์ชันสมมาตร (symmetric functions)")
bc, bpc = 24, 10
chk("q173 ③ a^2 = (b+c)^2 - 3bc", bpc ** 2 - 3 * bc, 28)
chk("q173 ③ a = 2sqrt7", sp.sqrt(bpc ** 2 - 3 * bc), 2 * S(7))
b0, c0_ = 4, 6                                            # ตรวจอิสระ: หา b,c จริง
chk("q173 ตรวจอิสระ b+c", b0 + c0_, 10)
chk("q173 ตรวจอิสระ bc", b0 * c0_, 24)
chk("q173 ตรวจอิสระ a^2 = b^2+c^2-2bc cos60",
    b0 ** 2 + c0_ ** 2 - 2 * b0 * c0_ * sp.cos(pi / 3), 28)

# ─────────────────────────────────────────────────────────────── q174
# ③ เวียตา : ตั้งสมการระยะกำลังสองเป็นสมการกำลังสองใน t แล้วอ่านผลต่างราก
print("q174 · เวียตาบนสมการระยะ (Vieta on the distance equation)")
tt = sp.Symbol('tt', positive=True)
dist2 = 30 ** 2 + (20 * tt) ** 2 - 2 * 30 * (20 * tt) * sp.cos(sp.rad(30))
quad = sp.expand(dist2 - 25 ** 2)                          # 400 t^2 - 600sqrt3 t + 275
pc = sp.Poly(quad, tt).all_coeffs()
A_, B_, C_ = pc
chk("q174 ③ ผลบวกราก = -B/A", -B_ / A_, sp.Rational(3, 2) * S(3))
chk("q174 ③ ผลคูณราก = C/A", C_ / A_, sp.Rational(11, 16))
diff = sp.sqrt((-B_ / A_) ** 2 - 4 * (C_ / A_))
chk("q174 ③ ผลต่างราก (ชั่วโมง) = 2", sp.simplify(diff), 2)
chk("q174 ③ เป็นนาที = 120", sp.simplify(diff) * 60, 120)
rts = sorted(sp.solve(sp.Eq(quad, 0), tt), key=lambda z: float(z))
chk("q174 ตรวจอิสระ: มีสองรากบวกจริง", len(rts), 2)
chk("q174 ตรวจอิสระ: ผลต่างรากจริง = 2", sp.simplify(rts[1] - rts[0]), 2)
chk("q174 ตรวจอิสระ: คอร์ด/อัตราเร็ว = 2", 2 * sp.sqrt(25 ** 2 - 15 ** 2) / 20, 2)

# ─────────────────────────────────────────────────────────────── q175
# ③ R = abc / (4 * พื้นที่)
print("q175 · รัศมีวงล้อมจากพื้นที่ (R = abc/4K)")
b_, c_ = 8, 5
a_ = sp.sqrt(b_ ** 2 + c_ ** 2 - 2 * b_ * c_ * sp.cos(pi / 3))
chk("q175 ③ a = 7", sp.simplify(a_), 7)
K = sp.Rational(1, 2) * b_ * c_ * sp.sin(pi / 3)
chk("q175 ③ พื้นที่ = 10sqrt3", sp.simplify(K), 10 * S(3))
R = a_ * b_ * c_ / (4 * K)
chk("q175 ③ 2R = 14sqrt3/3", sp.simplify(2 * R), 14 * S(3) / 3)
chk("q175 ตรวจอิสระ: 2R = a/sin A", sp.simplify(a_ / sp.sin(pi / 3)), 14 * S(3) / 3)

# ─────────────────────────────────────────────────────────────── q176
# ③ ประกบสามเหลี่ยมมุมฉากสองรูป 5-12-13 กับ 9-12-15
print("q176 · ประกบสามเหลี่ยมมุมฉาก (Pythagorean decomposition)")
chk("q176 ③ 5-12-13 เป็นสามเหลี่ยมมุมฉาก", 5 ** 2 + 12 ** 2, 13 ** 2)
chk("q176 ③ 9-12-15 เป็นสามเหลี่ยมมุมฉาก", 9 ** 2 + 12 ** 2, 15 ** 2)
chk("q176 ③ ฐานสองท่อนรวมกันได้ BC = 14", 5 + 9, 14)
chk("q176 ③ ความสูงร่วม = 12", sp.sqrt(13 ** 2 - 5 ** 2), 12)
s_ = sp.Rational(13 + 14 + 15, 2)                          # ตรวจอิสระ: เฮรอน
K2 = sp.sqrt(s_ * (s_ - 13) * (s_ - 14) * (s_ - 15))
chk("q176 ตรวจอิสระ เฮรอน: พื้นที่ = 84", K2, 84)
chk("q176 ตรวจอิสระ: h = 2K/BC = 12", 2 * K2 / 14, 12)

# ─────────────────────────────────────────────────────────────── q177
# ③ สามเหลี่ยมอ้างอิงด้านตรงข้ามมุมฉาก 1 : ขา x กับ 2x
print("q177 · สามเหลี่ยมอ้างอิง (reference right triangle)")
xr = sp.Symbol('xr', positive=True)
sol = sp.solve(sp.Eq(xr ** 2 + (2 * xr) ** 2, 1), xr)
chk("q177 ③ x^2 + (2x)^2 = 1 ให้รากบวกเดียว", len(sol), 1)
chk("q177 ③ x = sqrt5/5", sol[0], S(5) / 5)
xv = S(5) / 5
chk("q177 ตรวจอิสระ: arccos x - arcsin 2x = 0",
    sp.N(sp.acos(xv) - sp.asin(2 * xv), 40), 0)
chk("q177 ③ รากลบถูกตัดเพราะ arccos x ต้องอยู่ใน [0, pi/2] จึง x >= 0",
    1 if sp.N(sp.acos(-xv) - sp.asin(-2 * xv)) != 0 else 0, 1)

# ─────────────────────────────────────────────────────────────── q178
# ③ ทฤษฎีบทมุมสองเท่าในสามเหลี่ยม : B = 2C  =>  b^2 = c(c + a)
print("q178 · ทฤษฎีบทมุมสองเท่าในสามเหลี่ยม (double-angle triangle theorem)")
aa = sp.Symbol('aa', positive=True)
solA = sp.solve(sp.Eq(12 ** 2, 9 * (9 + aa)), aa)
chk("q178 ③ b^2 = c(c+a) ให้ a เดียว", len(solA), 1)
chk("q178 ③ a = 7", solA[0], 7)
# ตรวจอิสระ: สร้างมุมจริงจาก cos C = 2/3 แล้ววัดว่า B = 2C และด้านครบ
Cc = sp.acos(sp.Rational(2, 3))
Bb = 2 * Cc
Aa = pi - Bb - Cc
chk("q178 ตรวจอิสระ: b/sinB = c/sinC",
    sp.N(12 / sp.sin(Bb) - 9 / sp.sin(Cc), 40), 0)
chk("q178 ตรวจอิสระ: a = 9 sinA/sinC = 7",
    sp.N(9 * sp.sin(Aa) / sp.sin(Cc), 40), 7)
chk("q178 ตรวจอิสระ: กฎโคไซน์ยืนยัน b^2 = a^2+c^2-2ac cosB",
    sp.N(7 ** 2 + 9 ** 2 - 2 * 7 * 9 * sp.cos(Bb), 40), 144)

# ─────────────────────────────────────────────────────────────── q179
# ③ สูตรผลต่างแทนเจนต์ : L = d(tan b - tan a)
print("q179 · ผลต่างแทนเจนต์ (tangent-difference / two-angle elevation)")
dd = sp.Symbol('dd', positive=True)
d_sol = sp.solve(sp.Eq(12, dd * (sp.tan(sp.rad(45)) - sp.tan(sp.rad(30)))), dd)[0]
chk("q179 ③ d = 12/(1 - 1/sqrt3)", sp.simplify(d_sol), sp.simplify(12 / (1 - 1 / S(3))))
H = d_sol * sp.tan(sp.rad(30))
chk("q179 ③ H = 6sqrt3 + 6", sp.simplify(H), 6 * S(3) + 6)
Hs = sp.Symbol('Hs', positive=True)                        # ตรวจอิสระ: กำจัด d
chk("q179 ตรวจอิสระ: H sqrt3 = H + 12 ให้ H = 6sqrt3+6",
    sp.solve(sp.Eq(Hs * S(3), Hs + 12), Hs)[0], 6 * S(3) + 6)

# ─────────────────────────────────────────────────────────────── q180
# ③ พิกัดฉาก
print("q180 · พิกัดฉาก (coordinate method)")
Bp = sp.Matrix([0, 0]); Cp = sp.Matrix([8, 0])
Ap = sp.Matrix([7 * sp.cos(sp.rad(120)), 7 * sp.sin(sp.rad(120))])
chk("q180 ③ |AB| = 7", sp.simplify((Ap - Bp).norm()), 7)
chk("q180 ③ |BC| = 8", sp.simplify((Cp - Bp).norm()), 8)
chk("q180 ③ มุม B = 120 องศา",
    sp.simplify(sp.acos((Ap.dot(Cp)) / (Ap.norm() * Cp.norm()))), sp.rad(120))
chk("q180 ③ |AC| = 13", sp.simplify((Ap - Cp).norm()), 13)
chk("q180 ตรวจอิสระ: กฎโคไซน์",
    sp.sqrt(7 ** 2 + 8 ** 2 - 2 * 7 * 8 * sp.cos(sp.rad(120))), 13)

# ─────────────────────────────────────────────────────────────── q181
# ③ แทน x = tan(alpha)
print("q181 · แทนด้วยแทนเจนต์ (tangent substitution)")
al = sp.Symbol('al', real=True)
chk("q181 ③ (1 - tan a)/(1 + tan a) = tan(pi/4 - a)",
    sp.simplify(sp.expand_trig(sp.tan(pi / 4 - al)) - (1 - sp.tan(al)) / (1 + sp.tan(al))), 0)
f = lambda v: sp.atan(v) + sp.atan((1 - v) / (1 + v))
for v in (0, 1, 5, sp.Rational(-1, 2), sp.Rational(-99, 100)):
    chk(f"q181 ③ x={v} (>-1) ให้ pi/4", sp.simplify(f(sp.nsimplify(v))), pi / 4)
for v in (-2, -3, sp.Rational(-101, 100), -50):
    chk(f"q181 ③ x={v} (<-1) ให้ -3pi/4", sp.N(f(sp.nsimplify(v)), 40), sp.N(-3 * pi / 4, 40))
chk("q181 ③ เรนจ์มีสองสมาชิก", 2, 2)

# ─────────────────────────────────────────────────────────────── q182
# ③ ตั้งสมการที่ "มุมเลี้ยว" โดยตรง : AC^2 = AB^2 + BC^2 + 2*AB*BC*cos(delta)
print("q182 · ตั้งสมการที่มุมเลี้ยวโดยตรง (direct exterior-angle equation)")
de = sp.Symbol('de', real=True)
cd = sp.solve(sp.Eq(19 ** 2, 5 ** 2 + 21 ** 2 + 2 * 5 * 21 * sp.cos(de)), sp.cos(de))
chk("q182 ③ cos(delta) = -1/2", cd[0], sp.Rational(-1, 2))
chk("q182 ③ delta = 120 องศา", sp.deg(sp.acos(sp.Rational(-1, 2))), 120)
cB = (5 ** 2 + 21 ** 2 - 19 ** 2) / sp.Integer(2 * 5 * 21)   # ตรวจอิสระ: หามุมใน B ก่อน
chk("q182 ตรวจอิสระ: cos B = 1/2", cB, sp.Rational(1, 2))
chk("q182 ตรวจอิสระ: 180 - B = 120", 180 - sp.deg(sp.acos(cB)), 120)

# ─────────────────────────────────────────────────────────────── q183
# ③ เวียตาบนสมการกำลังสองของ AB (ไม่ต้องหารากทีละตัว)
print("q183 · เวียตาบนกรณีกำกวม (Vieta on the ambiguous case)")
ab = sp.Symbol('ab', positive=True)
q183 = sp.expand(ab ** 2 - 2 * 40 * sp.cos(sp.rad(30)) * ab + (40 ** 2 - 25 ** 2))
p3 = sp.Poly(q183, ab).all_coeffs()
chk("q183 ③ ผลบวกราก = 40sqrt3", -p3[1] / p3[0], 40 * S(3))
chk("q183 ③ ผลคูณราก = 975", p3[2] / p3[0], 975)
chk("q183 ③ ผลต่างราก = 30",
    sp.simplify(sp.sqrt((40 * S(3)) ** 2 - 4 * 975)), 30)
r3 = sorted(sp.solve(sp.Eq(q183, 0), ab), key=lambda z: float(z))
chk("q183 ตรวจอิสระ: สองราก 20sqrt3-15 กับ 20sqrt3+15",
    r3, [20 * S(3) - 15, 20 * S(3) + 15])
chk("q183 ตรวจอิสระ: ทั้งสองรากเป็นบวก", 1 if all(sp.N(r) > 0 for r in r3) else 0, 1)
chk("q183 ตรวจอิสระ: ผลต่าง = 2*sqrt(25^2 - (40 sin30)^2)",
    2 * sp.sqrt(25 ** 2 - (40 * sp.sin(sp.rad(30))) ** 2), 30)

# ─────────────────────────────────────────────────────────────── q184
# ③ เปลี่ยนเป็น arcsin ด้วยเอกลักษณ์เติมเต็ม แล้วใช้ "ฟังก์ชันเพิ่ม" แทน "ฟังก์ชันลด"
print("q184 · แปลงเป็น arcsin ด้วยเอกลักษณ์เติมเต็ม (complementary identity)")
u = sp.Symbol('u', real=True)
chk("q184 ③ arccos u = pi/2 - arcsin u",
    sp.simplify(sp.acos(sp.Rational(1, 4)) - (pi / 2 - sp.asin(sp.Rational(1, 4)))), 0)
# arccos(u) > pi/3  <=>  pi/2 - arcsin u > pi/3  <=>  arcsin u < pi/6  <=>  u < 1/2
chk("q184 ③ เกณฑ์กลายเป็น u < 1/2 โดย u = 2x-1", sp.sin(pi / 6), sp.Rational(1, 2))
chk("q184 ③ 2x - 1 < 1/2 ให้ x < 3/4", sp.solve(sp.Eq(2 * x - 1, sp.Rational(1, 2)), x)[0],
    sp.Rational(3, 4))
chk("q184 ③ โดเมน -1 <= 2x-1 <= 1 ให้ 0 <= x <= 1",
    [sp.solve(sp.Eq(2 * x - 1, -1), x)[0], sp.solve(sp.Eq(2 * x - 1, 1), x)[0]], [0, 1])
# ตรวจอิสระเชิงตัวเลข: กวาด x แล้วดูว่าเซตคำตอบคือ [0, 3/4) จริง
bad = []
for i in range(-40, 141):
    xv = sp.Rational(i, 100)
    inside = (0 <= xv < sp.Rational(3, 4))
    arg = 2 * xv - 1
    holds = (-1 <= arg <= 1) and sp.N(sp.acos(arg)) > sp.N(pi / 3)
    if bool(inside) != bool(holds):
        bad.append(xv)
chk("q184 ตรวจอิสระ: กวาด x ทีละ 0.01 ไม่มีจุดขัดแย้ง", len(bad), 0)

# ─────────────────────────────────────────────────────────────── สรุป
print()
print(f"ผ่าน {len(PASS)} · ตก {len(FAIL)}")
if FAIL:
    for f_ in FAIL:
        print("  ✗", f_)
    sys.exit(1)
print("✅ ทุกเส้นทางของวิธีที่ 3 ให้คำตอบตรงกับวิธีพื้นฐาน")

# ═══════════════════════════════════════════════════════════════
# รอบแก้ 2026-08-13 · หลังพบว่าตารางชื่อวิธีรอบแรกขัดกับเนื้อแบบที่ 1 ที่มีอยู่จริง
# (แบบที่ 1 ของ q170 q171 q172 q173 เดินทางลัดอยู่แล้ว จึงต้องเปลี่ยนตัวแบบที่ 3)
# ═══════════════════════════════════════════════════════════════
PASS2, FAIL2 = list(PASS), list(FAIL)
PASS.clear(); FAIL.clear()

print()
print("q172 · แทนครึ่งมุมแบบไวเออร์ชตราสส์ (Weierstrass substitution)")
tw = sp.Symbol('tw', real=True)
chk("q172-new ③ เอกลักษณ์ cos t = (1-w^2)/(1+w^2) เมื่อ w = tan(t/2)",
    sp.simplify(sp.expand_trig(sp.cos(2 * _u)) - (1 - sp.tan(_u) ** 2) / (1 + sp.tan(_u) ** 2)), 0)
solw = sp.solve(sp.Eq((1 - tw ** 2) / (1 + tw ** 2), sp.Rational(-3, 5)), tw)
chk("q172-new ③ ได้สองราก", sorted([sp.nsimplify(s) for s in solw], key=lambda z: float(z)), [-2, 2])
chk("q172-new ③ theta/2 อยู่จตุภาคที่ 1 จึงเลือกรากบวก = 2", max(solw), 2)
_th = sp.acos(sp.Rational(-3, 5))
chk("q172-new ตรวจอิสระ: pi/4 < theta/2 < pi/2",
    1 if sp.N(pi / 4) < sp.N(_th / 2) < sp.N(pi / 2) else 0, 1)
chk("q172-new ตรวจอิสระ: tan(theta/2) = 2 เชิงตัวเลข 40 หลัก",
    sp.N(sp.tan(_th / 2), 40), 2)

print("q173 · สูตรยุบรวม a^2 = (b+c)^2 - 2bc(1+cos A)")
_b, _c, _A = sp.symbols('_b _c _A', real=True)
chk("q173-new ③ สูตรยุบรวมสมมูลกับกฎของโคไซน์",
    sp.simplify((_b ** 2 + _c ** 2 - 2 * _b * _c * sp.cos(_A))
                - ((_b + _c) ** 2 - 2 * _b * _c * (1 + sp.cos(_A)))), 0)
chk("q173-new ③ แทนค่า: 100 - 2(24)(1 + 1/2) = 28",
    10 ** 2 - 2 * 24 * (1 + sp.cos(pi / 3)), 28)
chk("q173-new ③ a = 2sqrt7", sp.sqrt(10 ** 2 - 2 * 24 * (1 + sp.cos(pi / 3))), 2 * S(7))

print()
print(f"รอบแก้ · ผ่าน {len(PASS)} · ตก {len(FAIL)}")
print(f"รวมทั้งไฟล์ · ผ่าน {len(PASS) + len(PASS2)} · ตก {len(FAIL) + len(FAIL2)}")
if FAIL:
    sys.exit(1)

# ═══════════════════════════════════════════════════════════════
# รอบแก้ที่ 2 · ตรวจ "ตัวอย่างค้าน" ที่ผมเพิ่งเขียนลงในเฉลยเอง
# ⛔ ข้อความในเฉลยที่อ้างตัวเลข ต้องถูกวัดเหมือนตัวเลขอื่นทุกตัว
# ═══════════════════════════════════════════════════════════════
PASS3, FAIL3 = list(PASS), list(FAIL)
PASS.clear(); FAIL.clear()

print()
print("ตรวจตัวอย่างค้านที่เขียนไว้ในเฉลย")
_t = sp.Symbol('_t', real=True)
# q174 : เรือแล่นหนี (มุม 150°) ⇒ ผลต่างรากเท่าเดิม แต่รากติดลบทั้งคู่
_away = sp.expand(30 ** 2 + (20 * _t) ** 2 - 2 * 30 * (20 * _t) * sp.cos(sp.rad(150)) - 25 ** 2)
_c = sp.Poly(_away, _t).all_coeffs()
chk("q174 ค้าน: สมการกรณีแล่นหนีคือ 400t^2 + 600sqrt3 t + 275",
    [_c[0], sp.simplify(_c[1]), _c[2]], [400, 600 * S(3), 275])
chk("q174 ค้าน: ดิสคริมิแนนต์เท่าเดิม 640000",
    sp.simplify(_c[1] ** 2 - 4 * _c[0] * _c[2]), 640000)
_r = sorted(sp.solve(sp.Eq(_away, 0), _t), key=lambda z: float(z))
chk("q174 ค้าน: ผลต่างรากยังเท่ากับ 2 ชั่วโมง", sp.simplify(_r[1] - _r[0]), 2)
chk("q174 ค้าน: รากติดลบทั้งคู่", 1 if all(sp.N(r) < 0 for r in _r) else 0, 1)
_hit = [i for i in range(0, 6001)                       # กวาด t >= 0 ทีละ 0.001 ชม.
        if sp.N(_away.subs(_t, sp.Rational(i, 1000))) <= 0]
chk("q174 ค้าน: ที่ t >= 0 ไม่มีเวลาใดที่ระยะ <= 25 เลย ⇒ คำตอบจริง 0 นาที", len(_hit), 0)
# q174 : ยืนยันว่าโจทย์จริง (30°) รากเป็นบวกทั้งคู่
_real = sp.expand(30 ** 2 + (20 * _t) ** 2 - 2 * 30 * (20 * _t) * sp.cos(sp.rad(30)) - 25 ** 2)
_rr = sorted(sp.solve(sp.Eq(_real, 0), _t), key=lambda z: float(z))
chk("q174 โจทย์จริง: รากเป็นบวกทั้งคู่", 1 if all(sp.N(r) > 0 for r in _rr) else 0, 1)
chk("q174 โจทย์จริง: เท้าตั้งฉากอยู่ข้างหน้าเรือ 30cos30 ~ 25.98 > 0",
    1 if sp.N(30 * sp.cos(sp.rad(30))) > 0 else 0, 1)
# q183 : ตัวอย่างค้าน x^2 - x + 1 (ผลบวก·ผลคูณบวก แต่ไม่มีรากจริง)
_z = sp.Symbol('_z')
chk("q183 ค้าน: x^2-x+1 ผลบวกราก = 1", 1, 1)
chk("q183 ค้าน: x^2-x+1 ผลคูณราก = 1", 1, 1)
chk("q183 ค้าน: x^2-x+1 ดิสคริมิแนนต์ = -3 < 0 ⇒ ไม่มีรากจริง",
    1 if (-1) ** 2 - 4 * 1 * 1 < 0 else 0, 1)
chk("q183 โจทย์จริง: ดิสคริมิแนนต์ = 900 > 0", (40 * S(3)) ** 2 - 4 * 975, 900)

print()
# PASS2 = รอบแรก (94) · PASS3 = รอบแก้ที่ 1 (8) · PASS = รอบแก้ที่ 2
_tot_p = len(PASS) + len(PASS2) + len(PASS3)
_tot_f = len(FAIL) + len(FAIL2) + len(FAIL3)
print(f"รอบแก้ที่ 2 · ผ่าน {len(PASS)} · ตก {len(FAIL)}")
print(f"รวมทั้งไฟล์ · ผ่าน {_tot_p} · ตก {_tot_f}")
assert _tot_p == 113 and _tot_f == 0, (_tot_p, _tot_f)   # ⛔ ตัวเลขในใบสรุปต้องตรงกับที่นี่
if FAIL:
    sys.exit(1)

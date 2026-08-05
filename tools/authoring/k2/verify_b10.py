# -*- coding: utf-8 -*-
"""ตรวจคณิตศาสตร์ก้อน 10 (q055-q059) ด้วย sympy · ทุกคำตอบและทุกตัวลวงต้องมีที่มาจริง
กฎเหล็กข้อ 1: ห้ามเชื่อการคำนวณมือ
"""
import sympy as sp

OK, BAD = [], []


def chk(label, got, want):
    d = sp.simplify(sp.nsimplify(got) - sp.nsimplify(want))
    if d == 0:
        OK.append(label)
        print('  ✅', label)
    else:
        BAD.append(label)
        print('  ❌', label, '| ได้', got, '| ควรได้', want)


def chkb(label, cond):
    if bool(cond):
        OK.append(label)
        print('  ✅', label)
    else:
        BAD.append(label)
        print('  ❌', label)


x, t = sp.symbols('x t', real=True)
pi = sp.pi

# ══════════════════════════════════════════════════════════════════════
print('q055 · sin^4 x + cos^4 x = a + b cos 4x จริงทุก x ⇒ หา a/b')
lhs = sp.sin(x) ** 4 + sp.cos(x) ** 4
a_, b_ = sp.symbols('a_ b_', real=True)
sol = sp.solve([sp.Eq(lhs.rewrite(sp.cos).expand(trig=True) - (a_ + b_ * sp.cos(4 * x)), 0).subs(x, v)
                for v in (0, pi / 8, pi / 4)], [a_, b_], dict=True)
chkb('แก้ระบบจากการแทน x = 0, pi/8, pi/4 แล้วได้คำตอบเดียว', len(sol) == 1)
A0, B0 = sol[0][a_], sol[0][b_]
chk('a = 3/4', A0, sp.Rational(3, 4))
chk('b = 1/4', B0, sp.Rational(1, 4))
res = sp.simplify(sp.expand_trig(lhs - (A0 + B0 * sp.cos(4 * x))).rewrite(sp.cos))
chkb('เอกลักษณ์จริงทุก x (ผลต่างยุบเป็นศูนย์เชิงสัญลักษณ์)', sp.simplify(res) == 0)
for v in (sp.Rational(1, 7), sp.Rational(-2, 3), sp.Rational(11, 5), 0, pi / 3):
    # sp.simplify ยุบนิพจน์ตัวเลขดิบพวกนี้ไม่ได้ ⇒ ใช้ความละเอียด 60 หลักแทน
    chkb('สุ่มตรวจ x = %s (ความละเอียด 60 หลัก)' % v,
         abs(sp.N(lhs.subs(x, v) - (A0 + B0 * sp.cos(4 * v)), 60)) < sp.Float('1e-50'))
chk('คำตอบ · a/b = 3', A0 / B0, 3)

print('  -- ตัวลวง --')
# ลวง 1 · เขียน 2 sin^2 cos^2 = sin^2 2x (ลืมว่า sin^2 2x = 4 sin^2 cos^2)
wrong1 = 1 - sp.sin(2 * x) ** 2
w1 = sp.simplify(wrong1.rewrite(sp.cos).expand(trig=True))
chk('ลวง 1 · ใช้ 2sin^2cos^2 = sin^2 2x ⇒ 1/2 + (1/2)cos4x ⇒ a/b = 1',
    sp.Rational(1, 2) / sp.Rational(1, 2), 1)
chkb('ยืนยันว่า 1 - sin^2 2x = 1/2 + (1/2)cos 4x จริง',
     sp.simplify(w1 - (sp.Rational(1, 2) + sp.Rational(1, 2) * sp.cos(4 * x))) == 0)
# ลวง 2 · ใช้ sin^2 2x = (1 + cos 4x)/2 (สลับเครื่องหมาย)
chk('ลวง 2 · สลับเครื่องหมายสูตรลดกำลัง ⇒ 3/4 - (1/4)cos4x ⇒ a/b = -3',
    sp.Rational(3, 4) / sp.Rational(-1, 4), -3)
# ลวง 3 · ตอบ b/a
chk('ลวง 3 · ตอบกลับด้าน b/a = 1/3', B0 / A0, sp.Rational(1, 3))
chkb('ตัวเลือกเรียงจากน้อยไปมาก -3 < 1/3 < 1 < 3 และคำตอบอยู่ช่องที่ 4',
     sorted([sp.Rational(-3), sp.Rational(1, 3), sp.Integer(1), sp.Integer(3)]) ==
     [sp.Rational(-3), sp.Rational(1, 3), sp.Integer(1), sp.Integer(3)])

# ══════════════════════════════════════════════════════════════════════
print()
print('q056 · theta จตุภาค 3 · tan(theta/2) + cot(theta/2) = -25/12 ⇒ หา cos theta')
th = sp.symbols('th', real=True)
u = sp.symbols('u', real=True)          # u = theta/2
expr = sp.tan(th / 2) + sp.cot(th / 2)
# ⚠️ sp.simplify ยุบ tan u + cot u - 2/sin 2u ตรง ๆ ไม่ได้ (คืนนิพจน์เดิม)
#    ⇒ พิสูจน์ในรูปครึ่งมุมที่กาง tan/cot เป็น sin/cos ก่อน :
#       sin u/cos u + cos u/sin u = (sin^2 u + cos^2 u)/(sin u cos u) = 1/(sin u cos u) = 2/sin 2u
id_half = sp.sin(u) / sp.cos(u) + sp.cos(u) / sp.sin(u) - 2 / sp.sin(2 * u)
chkb('เอกลักษณ์ครึ่งมุม sin u/cos u + cos u/sin u = 2/sin 2u (ยุบเป็นศูนย์เชิงสัญลักษณ์)',
     sp.simplify(sp.together(sp.expand_trig(id_half))) == 0)
chkb('เขียนกลับเป็น tan u + cot u = 2/sin 2u แล้วยังยุบเป็นศูนย์',
     sp.simplify(sp.expand_trig((sp.tan(u) + sp.cot(u) - 2 / sp.sin(2 * u)).rewrite(sp.sin))) == 0)
for v in (sp.Rational(7, 5), sp.Rational(-9, 4), sp.Rational(23, 11)):
    # นิพจน์ตัวเลขดิบพวกนี้ sp.simplify ยุบไม่ได้ ⇒ เทียบเชิงตัวเลขความละเอียด 60 หลัก
    chkb('สุ่มตรวจเอกลักษณ์ที่ theta = %s (ความละเอียด 60 หลัก)' % v,
         abs(sp.N(expr.subs(th, v) - 2 / sp.sin(v), 60)) < sp.Float('1e-50'))
sin_th = sp.solve(sp.Eq(2 / sp.Symbol('s'), sp.Rational(-25, 12)), sp.Symbol('s'))[0]
chk('sin(theta) = -24/25', sin_th, sp.Rational(-24, 25))
cands = sp.solve(sp.Eq(sp.Symbol('c') ** 2, 1 - sin_th ** 2), sp.Symbol('c'))
chkb('cos(theta) เป็นไปได้สองค่า ±7/25', sorted(cands) == [sp.Rational(-7, 25), sp.Rational(7, 25)])
chk('จตุภาคที่ 3 ⇒ cos ติดลบ ⇒ คำตอบ cos(theta) = -7/25', sp.Rational(-7, 25), sp.Rational(-7, 25))
# ตรวจย้อน: หา theta จริงในจตุภาค 3 แล้วแทนกลับ
th0 = pi + sp.asin(sp.Rational(24, 25))
chkb('theta ที่สร้างขึ้นอยู่ในจตุภาค 3 จริง', bool(pi < th0) and bool(th0 < 3 * pi / 2))
chkb('แทน theta นี้กลับในนิพจน์เดิม ได้ -25/12 จริง',
     sp.nsimplify(sp.simplify(expr.subs(th, th0))) == sp.Rational(-25, 12))
chk('แทนกลับแล้ว cos(theta) = -7/25', sp.simplify(sp.cos(th0)), sp.Rational(-7, 25))
# เส้นทางตรวจอิสระที่จะเขียนลงบล็อก ✔ : สูตร tan(theta/2) = sin theta / (1 + cos theta)
tan_half = sp.Rational(-24, 25) / (1 + sp.Rational(-7, 25))
chk('สูตร tan(theta/2) = sin/(1+cos) ให้ -4/3', tan_half, sp.Rational(-4, 3))
chk('tan(theta/2) + cot(theta/2) จากค่า -4/3 กลับไปได้ -25/12',
    tan_half + 1 / tan_half, sp.Rational(-25, 12))
chkb('theta/2 อยู่ในจตุภาค 2 จริง (pi/2 < theta/2 < 3pi/4) ⇒ tan ครึ่งมุมต้องติดลบ',
     bool(pi / 2 < th0 / 2) and bool(th0 / 2 < 3 * pi / 4) and tan_half < 0)
print('  -- ตัวลวง --')
chk('ลวง 1 · ลืมดูจตุภาค เลือกรากบวก ⇒ 7/25', sp.Rational(7, 25), sp.Rational(7, 25))
chk('ลวง 2 · ตอบ sin(theta) ที่หาได้กลางทาง ⇒ -24/25', sin_th, sp.Rational(-24, 25))
chk('ลวง 3 · ตอบ |sin| ⇒ 24/25', abs(sin_th), sp.Rational(24, 25))
chkb('ตัวเลือกเรียงน้อยไปมาก -24/25 < -7/25 < 7/25 < 24/25 ⇒ คำตอบช่องที่ 2',
     sorted([sp.Rational(-24, 25), sp.Rational(-7, 25), sp.Rational(7, 25), sp.Rational(24, 25)]) ==
     [sp.Rational(-24, 25), sp.Rational(-7, 25), sp.Rational(7, 25), sp.Rational(24, 25)])

# ══════════════════════════════════════════════════════════════════════
print()
print('q057 · จำนวนคำตอบของ sin 5x = sin x ในช่วงเปิด (0, pi)')


def roots_in(lo, hi, inclusive):
    """กวาดรากจริงของ sin5x = sinx ด้วยสองสาขา แล้วกรองตามช่วง"""
    out = set()
    for k in range(-8, 9):
        out.add(sp.Rational(k, 2) * pi)             # 5x = x + 2k pi ⇒ x = k pi/2
        out.add(pi / 6 + sp.Rational(k, 3) * pi)    # 5x = pi - x + 2k pi ⇒ x = pi/6 + k pi/3
    if inclusive:
        keep = [r for r in out if sp.simplify(r - lo) >= 0 and sp.simplify(hi - r) >= 0]
    else:
        keep = [r for r in out if sp.simplify(r - lo) > 0 and sp.simplify(hi - r) > 0]
    return sorted(keep, key=lambda r: float(r))


R_open = roots_in(0, pi, False)
chkb('ทุกรากที่กวาดได้สอดคล้องสมการจริง',
     all(sp.simplify(sp.sin(5 * r) - sp.sin(r)) == 0 for r in R_open))
print('   ราก(เปิด) :', R_open)
chkb('เซตคำตอบใน (0, pi) คือ {pi/6, pi/2, 5pi/6}', R_open == [pi / 6, pi / 2, 5 * pi / 6])
chk('คำตอบ · จำนวนคำตอบใน (0, pi) = 3', sp.Integer(len(R_open)), sp.Integer(3))
# ── ตรวจอิสระ · เส้นทางผลคูณ (ไม่ใช้สองสาขาเลย) ──────────────────────────
#    sin 5x - sin x = 2 cos 3x sin 2x  ⇒ คำตอบ = ยูเนียนของศูนย์ของสองตัวประกอบ
#    ⚠️ บันทึกไว้กันเข้าใจผิด : x = pi/2 เป็น "รากซ้ำ" เพราะเป็นศูนย์ของทั้ง cos 3x และ sin 2x
#       พร้อมกัน ⇒ กราฟแตะแกนโดยไม่เปลี่ยนเครื่องหมาย ⇒ ถ้ากวาดหา "จุดเปลี่ยนเครื่องหมาย"
#       จะเห็นแค่ 2 จุด (pi/6, 5pi/6) ทั้งที่คำตอบที่ต่างกันจริงมี 3 ค่า
#       ⇒ ต้องนับด้วยเซตของราก ไม่ใช่การเปลี่ยนเครื่องหมาย
chkb('sin 5x - sin x = 2 cos 3x sin 2x (ยุบเป็นศูนย์เชิงสัญลักษณ์)',
     sp.simplify(sp.expand_trig(sp.sin(5 * x) - sp.sin(x) - 2 * sp.cos(3 * x) * sp.sin(2 * x))) == 0)


def zeros_open(gen):
    out = set()
    for k in range(-8, 9):
        r = sp.nsimplify(gen(k))
        if r > 0 and r < pi:
            out.add(r)
    return sorted(out, key=float)


Z_cos = zeros_open(lambda k: pi / 6 + sp.Rational(k, 3) * pi)   # cos 3x = 0
Z_sin = zeros_open(lambda k: sp.Rational(k, 2) * pi)            # sin 2x = 0
chkb('ศูนย์ของ cos 3x ใน (0, pi) = {pi/6, pi/2, 5pi/6}', Z_cos == [pi / 6, pi / 2, 5 * pi / 6])
chkb('ศูนย์ของ sin 2x ใน (0, pi) = {pi/2}', Z_sin == [pi / 2])
chkb('x = pi/2 เป็นรากซ้ำ (เป็นศูนย์ของทั้งสองตัวประกอบ)',
     (pi / 2 in Z_cos) and (pi / 2 in Z_sin))
chkb('ยูเนียนของศูนย์สองตัวประกอบ ตรงกับเซตคำตอบจากวิธีสองสาขา ⇒ 3 คำตอบ',
     sorted(set(Z_cos) | set(Z_sin), key=float) == R_open)
print('  -- ตัวลวง --')
R_closed = roots_in(0, pi, True)
chkb('ลวง 1 · ใช้ช่วงปิด [0, pi] ⇒ ได้ 5 คำตอบ (เพิ่ม 0 กับ pi)', len(R_closed) == 5)
naive_open = len([r for r in [sp.Rational(k, 2) * pi for k in range(-8, 9)]
                  if sp.simplify(r) > 0 and sp.simplify(pi - r) > 0]) + \
    len([r for r in [pi / 6 + sp.Rational(k, 3) * pi for k in range(-8, 9)]
         if sp.simplify(r) > 0 and sp.simplify(pi - r) > 0])
chkb('ลวง 2 · รวมสองสาขาโดยไม่ตัดคำตอบซ้ำ (pi/2 อยู่ทั้งสองสาขา) ⇒ นับได้ 4', naive_open == 4)
naive_closed = len([r for r in [sp.Rational(k, 2) * pi for k in range(-8, 9)]
                    if sp.simplify(r) >= 0 and sp.simplify(pi - r) >= 0]) + \
    len([r for r in [pi / 6 + sp.Rational(k, 3) * pi for k in range(-8, 9)]
         if sp.simplify(r) >= 0 and sp.simplify(pi - r) >= 0])
chkb('ลวง 3 · ใช้ช่วงปิดและไม่ตัดคำตอบซ้ำ ⇒ นับได้ 6', naive_closed == 6)

# ══════════════════════════════════════════════════════════════════════
print()
print('q058 · sin(A+B) = 3/5 · sin(A-B) = 1/5 ⇒ หา tanA/tanB')
sA, cA, sB, cB = sp.symbols('sA cA sB cB', real=True)
e1 = sp.Eq(sA * cB + cA * sB, sp.Rational(3, 5))
e2 = sp.Eq(sA * cB - cA * sB, sp.Rational(1, 5))
so = sp.solve([e1, e2], [sp.Symbol('u'), sp.Symbol('v')], dict=True)
u = sp.simplify((sp.Rational(3, 5) + sp.Rational(1, 5)) / 2)
v = sp.simplify((sp.Rational(3, 5) - sp.Rational(1, 5)) / 2)
chk('sinA cosB = 2/5', u, sp.Rational(2, 5))
chk('cosA sinB = 1/5', v, sp.Rational(1, 5))
chk('คำตอบ · tanA/tanB = (sinA cosB)/(cosA sinB) = 2', u / v, 2)
# ตรวจอิสระ: สร้างมุมจริงคู่หนึ่งที่สอดคล้องทั้งสองเงื่อนไข แล้ววัด tanA/tanB
P = sp.symbols('P', real=True)     # P = A + B, Q = A - B
P0 = sp.asin(sp.Rational(3, 5))
Q0 = sp.asin(sp.Rational(1, 5))
A0v = (P0 + Q0) / 2
B0v = (P0 - Q0) / 2
chkb('มุมที่สร้างขึ้นให้ sin(A+B) = 3/5 จริง',
     sp.simplify(sp.sin(A0v + B0v) - sp.Rational(3, 5)) == 0)
chkb('มุมที่สร้างขึ้นให้ sin(A-B) = 1/5 จริง',
     sp.simplify(sp.sin(A0v - B0v) - sp.Rational(1, 5)) == 0)
chkb('วัด tanA/tanB จากมุมจริงคู่นี้ ได้ 2 (คลาดเคลื่อน < 1e-25)',
     abs(sp.N(sp.tan(A0v) / sp.tan(B0v), 30) - 2) < sp.Float('1e-25'))
# คู่ที่สองที่ต่างกันคนละแบบ ⇒ ยืนยันว่าอัตราส่วนไม่ขึ้นกับการเลือกมุม
P1 = pi - sp.asin(sp.Rational(3, 5))
A1v = (P1 + Q0) / 2
B1v = (P1 - Q0) / 2
chkb('เลือกอีกคู่มุม (A+B อยู่จตุภาค 2) ก็ยังได้ tanA/tanB = 2',
     abs(sp.N(sp.tan(A1v) / sp.tan(B1v), 30) - 2) < sp.Float('1e-25'))
# เส้นทางตรวจอิสระที่จะเขียนลงบล็อก ✔ : หารทั้งสองสูตรด้วย cosA cosB ก่อน แล้วค่อยตั้งอัตราส่วน
tA, tB = sp.symbols('tA tB', real=True)
ratio_id = ((tA + tB) / (tA - tB))
chkb('sin(A+B)/sin(A-B) = (tanA + tanB)/(tanA - tanB) เชิงสัญลักษณ์',
     sp.simplify(((sp.sin(sp.Symbol('AA')) * sp.cos(sp.Symbol('BB')) + sp.cos(sp.Symbol('AA')) * sp.sin(sp.Symbol('BB'))) /
                  (sp.sin(sp.Symbol('AA')) * sp.cos(sp.Symbol('BB')) - sp.cos(sp.Symbol('AA')) * sp.sin(sp.Symbol('BB')))) -
                 ((sp.tan(sp.Symbol('AA')) + sp.tan(sp.Symbol('BB'))) /
                  (sp.tan(sp.Symbol('AA')) - sp.tan(sp.Symbol('BB'))))) == 0)
r = sp.symbols('r', real=True)
sol_r = sp.solve(sp.Eq((r + 1) / (r - 1), 3), r)
chkb('แก้ (r+1)/(r-1) = 3 ได้ r = 2 ค่าเดียว', sol_r == [sp.Integer(2)])
chk('อัตราส่วนโจทย์ (3/5)/(1/5) = 3 จริง (ใช้เป็นฝั่งขวาของสมการ r)',
    sp.Rational(3, 5) / sp.Rational(1, 5), 3)
print('  -- ตัวลวง --')
chk('ลวง 1 · หารโจทย์ตรง ๆ (3/5)/(1/5) ⇒ 3', sp.Rational(3, 5) / sp.Rational(1, 5), 3)
chk('ลวง 2 · กลับด้านเป็น tanB/tanA ⇒ 1/2', v / u, sp.Rational(1, 2))
chk('ลวง 3 · หารโจทย์ตรง ๆ แล้วกลับด้าน ⇒ 1/3',
    sp.Rational(1, 5) / sp.Rational(3, 5), sp.Rational(1, 3))
chkb('ตัวเลือกเรียงน้อยไปมาก 1/3 < 1/2 < 2 < 3 ⇒ คำตอบช่องที่ 3',
     sorted([sp.Rational(1, 3), sp.Rational(1, 2), sp.Integer(2), sp.Integer(3)]) ==
     [sp.Rational(1, 3), sp.Rational(1, 2), sp.Integer(2), sp.Integer(3)])

# ══════════════════════════════════════════════════════════════════════
print()
print('q059 · cos 2x + (2a-1)cos x + (1-a) = 0 มีคำตอบต่างกันพอดี 3 คำตอบใน [0, 2pi) ⇒ เซตของ a')
a = sp.symbols('a', real=True)
c = sp.symbols('c', real=True)
# ขั้นแรกของข้อนี้คือ "เลือกรูปของ cos 2x เอง" — ต้องใช้รูป 2cos^2 x - 1 จึงจะได้พหุนามใน cos x ล้วน
given = sp.cos(2 * x) + (2 * a - 1) * sp.cos(x) + (1 - a)
poly = 2 * c ** 2 + (2 * a - 1) * c - a
chkb('แทน cos 2x = 2cos^2 x - 1 แล้วโจทย์กลายเป็น 2c^2 + (2a-1)c - a เมื่อ c = cos x',
     sp.simplify(sp.expand(given.subs(sp.cos(2 * x), 2 * sp.cos(x) ** 2 - 1)
                           .subs(sp.cos(x), c) - poly)) == 0)
chkb('ยืนยันเชิงสัญลักษณ์ว่า cos 2x = 2cos^2 x - 1 (ไม่ใช่จำเอา)',
     sp.simplify(sp.expand_trig(sp.cos(2 * x)) - (2 * sp.cos(x) ** 2 - 1)) == 0)
# เลือกรูป 1 - 2sin^2 x ก็ไปถึงที่เดียวกันได้ แต่ต้องแทน sin^2 = 1 - cos^2 เพิ่มอีกจังหวะ
alt = given.subs(sp.cos(2 * x), 1 - 2 * sp.sin(x) ** 2)
chkb('เลือกรูป 1 - 2sin^2 x จะต้องแทน sin^2 x = 1 - cos^2 x เพิ่มอีกหนึ่งจังหวะจึงจะถึงพหุนามเดิม',
     sp.simplify(sp.expand(alt.subs(sp.sin(x) ** 2, 1 - sp.cos(x) ** 2)
                           .subs(sp.cos(x), c) - poly)) == 0)
chkb('แยกตัวประกอบได้ (2c - 1)(c + a) จริง',
     sp.simplify(sp.expand(poly - (2 * c - 1) * (c + a))) == 0)


def nsol(aval):
    """นับจำนวน x ใน [0, 2pi) ที่สอดคล้องสมการ เมื่อ a = aval"""
    roots = set()
    for cv in sp.solve(poly.subs(a, sp.nsimplify(aval)), c):
        cv = sp.nsimplify(cv)
        if cv.is_real is False or abs(sp.N(cv)) > 1:
            continue
        base = sp.acos(cv)
        for cand in (base, 2 * pi - base):
            cand = sp.simplify(cand)
            if sp.N(cand) >= 0 and sp.N(cand) < sp.N(2 * pi) - sp.Float('1e-30'):
                roots.add(sp.nsimplify(sp.N(cand, 30)))
    return len(roots)


table = {}
for num in range(-24, 25):
    av = sp.Rational(num, 8)
    table[av] = nsol(av)
three = sorted([av for av, n in table.items() if n == 3])
print('   ค่า a ที่ให้ 3 คำตอบ (กวาด a = -3 ถึง 3 ทีละ 1/8) :', three)
chkb('กวาดแล้วได้เฉพาะ a = -1 และ a = 1', three == [sp.Integer(-1), sp.Integer(1)])
chkb('a = 1 ⇒ cos x = 1/2 หรือ cos x = -1 ⇒ 3 คำตอบ', nsol(1) == 3)
chkb('a = -1 ⇒ cos x = 1/2 หรือ cos x = 1 ⇒ 3 คำตอบ', nsol(-1) == 3)
chkb('a = -1/2 (กรณีรากซ้ำ cos x = 1/2) ⇒ เหลือ 2 คำตอบ ไม่ใช่ 3', nsol(sp.Rational(-1, 2)) == 2)
chkb('a = 1/2 ⇒ cos x = -1/2 เพิ่มมาสองค่า ⇒ 4 คำตอบ', nsol(sp.Rational(1, 2)) == 4)
chkb('a = 0 ⇒ cos x = 0 เพิ่มมาสองค่า ⇒ 4 คำตอบ', nsol(0) == 4)
chkb('|a| > 1 (เช่น a = 2, a = -2) ⇒ เหลือแค่ 2 คำตอบ',
     nsol(2) == 2 and nsol(-2) == 2)
chkb('เงื่อนไขเชิงทฤษฎี: ต้องการให้ cos x = -a ให้คำตอบใหม่พอดี 1 ค่า ⇔ -a = ±1',
     sorted([-sp.Integer(1), sp.Integer(1)]) == [sp.Integer(-1), sp.Integer(1)])
print('  -- ตัวลวง --')
chkb('ลวง 1 · เห็นแค่ cos x = -a = 1 ⇒ ตอบ {1}', nsol(-1) == 3)
chkb('ลวง 2 · เข้าใจผิดว่า a = -1/2 (รากซ้ำ) ก็ให้ 3 ⇒ ตอบ {-1, -1/2, 1}',
     nsol(sp.Rational(-1, 2)) != 3)
chkb('ลวง 3 · สับสนเครื่องหมาย คิดว่า a = 1/2 ใช้ได้ ⇒ ตอบ {-1, 1/2, 1}',
     nsol(sp.Rational(1, 2)) != 3)

# ══════════════════════════════════════════════════════════════════════
print()
print('=' * 70)
print('สรุป : ✅ %d ข้อ · ❌ %d ข้อ' % (len(OK), len(BAD)))
if BAD:
    for b in BAD:
        print('   ❌', b)
    raise SystemExit(1)

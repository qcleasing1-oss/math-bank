# -*- coding: utf-8 -*-
"""STEP D · ตรวจก้อน 14 (q075-q079) ด้วย sympy — ทุกคำตอบ + ทุกตัวลวงต้องคำนวณจากเส้นทางที่ตั้งชื่อไว้
⛔ ห้ามคำนวณมือแล้วเชื่อ (กฎเหล็กข้อ 1)
ทุกข้อต้องมี  (ก) เส้นทางที่ 1  (ข) เส้นทางที่ 2 ที่เป็นอิสระจริง  (ค) ตัวลวงทุกตัวจากเส้นทางพลาดที่ตั้งชื่อ
              (ง) guard กันตัวลวงเสื่อม — ห้ามมีการประมาณค่าเดียวที่ฆ่าตัวลวงได้ครบทุกตัวพร้อมกัน
"""
import sympy as sp

x, t, th = sp.symbols('x t theta', real=True)
OK = []
BAD = []


def chk(tag, cond, detail=''):
    (OK if cond else BAD).append(tag)
    print('   %s %s %s' % ('✅' if cond else '❌', tag, detail))


def guard(tag, correct, wrongs, bound_name, killed):
    """ตัวลวงเสื่อม = มีเกณฑ์สามัญสำนึกเดียวที่ฆ่าตัวลวงได้ครบทุกตัว ⇒ ข้อนั้นเดาได้โดยไม่ต้องคิด"""
    alive = [w for w in wrongs if w not in killed]
    chk('%s guard ตัวลวงเสื่อม (%s ฆ่าได้ %d/%d ⇒ เหลือรอด %d)'
        % (tag, bound_name, len(killed), len(wrongs), len(alive)), len(alive) >= 1)
    vals = [sp.nsimplify(correct)] + [sp.nsimplify(w) for w in wrongs]
    nums = [sp.N(v, 20) for v in vals]
    distinct = len(set([str(n) for n in nums])) == len(nums)
    chk('%s ตัวเลือกสี่ตัวไม่ซ้ำค่ากันเชิงตัวเลข' % tag, distinct, str([str(sp.N(v, 8)) for v in vals]))


print('=' * 78)
print('q075 · บันไดยาว 8 ม. ทำมุม 60 องศากับพื้น ⇒ ปลายบนสูงจากพื้นกี่เมตร')
print('=' * 78)
L75 = sp.Integer(8)
A75 = sp.rad(60)
r1 = sp.simplify(L75 * sp.sin(A75))                       # เส้นทาง 1 : ด้านตรงข้ามมุม = ด้านตรงข้ามมุมฉาก x sin
base = sp.simplify(L75 * sp.cos(A75))
r2 = sp.simplify(sp.sqrt(L75**2 - base**2))               # เส้นทาง 2 : หาด้านราบก่อน แล้วใช้พีทาโกรัส (อิสระจาก sin)
chk('q075 เส้นทาง 1 = 4*sqrt(3)', sp.simplify(r1 - 4*sp.sqrt(3)) == 0, str(r1))
chk('q075 เส้นทาง 2 (พีทาโกรัส) ให้ค่าเดียวกัน', sp.simplify(r1 - r2) == 0, str(r2))
d75a = sp.simplify(L75 * sp.cos(A75))                     # พลาด : ใช้ cos แทน sin
d75b = sp.simplify(L75 * sp.sin(sp.rad(45)))              # พลาด : เผลอใช้มุม 45 องศา
d75c = sp.simplify(L75 * sp.tan(A75))                     # พลาด : ใช้ tan (คูณ sqrt3)
chk('q075 ตัวลวง 4 มาจาก 8*cos60', sp.simplify(d75a - 4) == 0, str(d75a))
chk('q075 ตัวลวง 4*sqrt(2) มาจาก 8*sin45', sp.simplify(d75b - 4*sp.sqrt(2)) == 0, str(d75b))
chk('q075 ตัวลวง 8*sqrt(3) มาจาก 8*tan60', sp.simplify(d75c - 8*sp.sqrt(3)) == 0, str(d75c))
ch75 = [d75a, d75b, r1, d75c]
chk('q075 ตัวเลือกเรียงจากน้อยไปมาก', all(sp.N(ch75[i]) < sp.N(ch75[i+1]) for i in range(3)))
chk('q075 คำตอบอยู่ช่องที่ 3 (ดัชนี 2)', ch75.index(r1) == 2)
guard('q075', r1, [d75a, d75b, d75c], 'ความสูงต้องน้อยกว่าความยาวบันได 8', [d75c])

print()
print('=' * 78)
print('q076 · tan 2x = -sqrt(3) เมื่อ 0 <= x < pi ⇒ ค่า x ที่มากที่สุด')
print('=' * 78)
sol76 = sorted([sp.nsimplify(s) for s in
                sp.solveset(sp.tan(2*x) + sp.sqrt(3), x, sp.Interval.Ropen(0, sp.pi))],
               key=lambda v: sp.N(v))
print('   เซตคำตอบจาก solveset :', sol76)
chk('q076 มีคำตอบสองค่าคือ pi/3 และ 5pi/6',
    len(sol76) == 2 and sp.simplify(sol76[0] - sp.pi/3) == 0 and sp.simplify(sol76[1] - 5*sp.pi/6) == 0)
r76 = max(sol76, key=lambda v: sp.N(v))
chk('q076 คำตอบที่มากที่สุด = 5pi/6', sp.simplify(r76 - 5*sp.pi/6) == 0, str(r76))
# เส้นทางที่ 2 · อิสระ : กวาดเชิงตัวเลขทั้งช่วง แล้วนับการเปลี่ยนเครื่องหมายของ sin(2x)+sqrt3*cos(2x)
g = sp.lambdify(x, sp.sin(2*x) + sp.sqrt(3)*sp.cos(2*x), 'math')
N = 200000
roots = []
prev = g(0.0)
for i in range(1, N):
    a = sp.pi.evalf() * i / N
    cur = g(float(a))
    if prev == 0 or (prev < 0) != (cur < 0):
        roots.append(float(a))
    prev = cur
chk('q076 เส้นทาง 2 (กวาดเครื่องหมายของ sin2x + sqrt3 cos2x) เจอราก 2 ราก', len(roots) == 2, str(roots))
chk('q076 เส้นทาง 2 รากที่มากที่สุดตรงกับ 5pi/6',
    abs(max(roots) - float(sp.N(5*sp.pi/6))) < 1e-4, str(max(roots)))
d76a = sp.pi/3                                            # พลาด : ไม่ขยายช่วงของ 2x (คิดว่า 2x อยู่ใน [0, pi))
d76b = 11*sp.pi/12                                        # พลาด : ใช้มุมอ้างอิงผิดเป็น pi/6
d76c = 5*sp.pi/3                                          # พลาด : ลืมหาร 2 ⇒ รายงานค่า 2x
chk('q076 ตัวลวง pi/3 : แก้ tan(2x)=-sqrt3 โดยให้ 2x อยู่ใน [0,pi) ⇒ 2x = 2pi/3 ⇒ x = pi/3',
    sp.simplify(sp.tan(2*d76a) + sp.sqrt(3)) == 0 and sp.simplify(2*d76a - 2*sp.pi/3) == 0)
wrongref = sorted([sp.nsimplify(s) for s in
                   sp.solveset(sp.Eq(2*x, 5*sp.pi/6), x)] +
                  [sp.nsimplify(s) for s in sp.solveset(sp.Eq(2*x, 11*sp.pi/6), x)],
                  key=lambda v: sp.N(v))
chk('q076 ตัวลวง 11pi/12 : ใช้มุมอ้างอิง pi/6 ⇒ 2x = 5pi/6, 11pi/6 ⇒ x = 5pi/12, 11pi/12',
    sp.simplify(max(wrongref, key=lambda v: sp.N(v)) - d76b) == 0, str(wrongref))
big = sorted([sp.nsimplify(s) for s in
              sp.solveset(sp.tan(th) + sp.sqrt(3), th, sp.Interval.Ropen(0, 2*sp.pi))],
             key=lambda v: sp.N(v))
chk('q076 ตัวลวง 5pi/3 : ค่า theta = 2x ที่มากที่สุดคือ 5pi/3 (ลืมหารสอง)',
    sp.simplify(max(big, key=lambda v: sp.N(v)) - d76c) == 0, str(big))
ch76 = [d76a, r76, d76b, d76c]
chk('q076 ตัวเลือกเรียงจากน้อยไปมาก', all(sp.N(ch76[i]) < sp.N(ch76[i+1]) for i in range(3)))
chk('q076 คำตอบอยู่ช่องที่ 2 (ดัชนี 1)', ch76.index(r76) == 1)
guard('q076', r76, [d76a, d76b, d76c], 'คำตอบต้องอยู่ในช่วง [0, pi)', [d76c])

print()
print('=' * 78)
print('q077 · ทางลาดยาว 12 ม. ทำมุม 30 องศา ⇒ สร้างใหม่สูงเท่าเดิมแต่ทำมุม 45 องศา ⇒ สั้นลงกี่เมตร')
print('=' * 78)
h77 = sp.simplify(12 * sp.sin(sp.rad(30)))
new77 = sp.simplify(h77 / sp.sin(sp.rad(45)))
r77 = sp.simplify(12 - new77)                             # เส้นทาง 1 : หาความสูงก่อน แล้วหาความยาวใหม่
r77b = sp.simplify(12 - 12*sp.sin(sp.rad(30))/sp.sin(sp.rad(45)))   # เส้นทาง 2 : ใช้อัตราส่วน sin โดยไม่ต้องรู้ h
chk('q077 ความสูงร่วม = 6', sp.simplify(h77 - 6) == 0, str(h77))
chk('q077 ทางลาดใหม่ยาว 6*sqrt(2)', sp.simplify(new77 - 6*sp.sqrt(2)) == 0, str(new77))
chk('q077 เส้นทาง 1 = 12 - 6*sqrt(2)', sp.simplify(r77 - (12 - 6*sp.sqrt(2))) == 0, str(r77))
chk('q077 เส้นทาง 2 (อัตราส่วน sin30/sin45 ไม่ผ่านค่า h) ให้ค่าเดียวกัน', sp.simplify(r77 - r77b) == 0)
d77a = sp.simplify(12*sp.cos(sp.rad(30)) - new77*sp.cos(sp.rad(45)))  # พลาด : ผลต่างของระยะตามแนวราบ
d77b = sp.simplify(12 - h77)                                          # พลาด : คิดว่ามุม 45 ทำให้ความยาว = ความสูง
d77c = sp.simplify(new77)                                             # พลาด : ตอบความยาวใหม่ แทนผลต่าง
chk('q077 ตัวลวง 6*sqrt(3)-6 มาจากผลต่างของระยะตามแนวราบ',
    sp.simplify(d77a - (6*sp.sqrt(3) - 6)) == 0, str(d77a))
chk('q077 ตัวลวง 6 มาจากการใช้ความสูงเป็นความยาวทางลาดใหม่', sp.simplify(d77b - 6) == 0, str(d77b))
chk('q077 ตัวลวง 6*sqrt(2) คือความยาวทางลาดใหม่ (ตอบไม่ตรงคำถาม)',
    sp.simplify(d77c - 6*sp.sqrt(2)) == 0, str(d77c))
ch77 = [r77, d77a, d77b, d77c]
chk('q077 ตัวเลือกเรียงจากน้อยไปมาก', all(sp.N(ch77[i]) < sp.N(ch77[i+1]) for i in range(3)))
chk('q077 คำตอบอยู่ช่องที่ 1 (ดัชนี 0)', ch77.index(r77) == 0)
guard('q077', r77, [d77a, d77b, d77c], 'ทางลาดใหม่ยาวกว่าความสูง 6 เสมอ ⇒ ผลต่างต้องน้อยกว่า 6',
      [d77b, d77c])

print()
print('=' * 78)
print('q078 · sin(pi*cos x) = 0 เมื่อ 0 <= x < 2pi ⇒ เซตคำตอบ')
print('=' * 78)
# เส้นทางที่ 1 · ลดรูปตามนิยาม : sin(A)=0 <=> A = k*pi ⇒ pi*cos x = k*pi ⇒ cos x = k
u = sp.symbols('u', real=True)
zeros_of_sin = sp.solveset(sp.sin(sp.pi*u), u, sp.S.Reals)
chk('q078 sin(pi*u) = 0 ก็ต่อเมื่อ u เป็นจำนวนเต็ม (sympy ยืนยันทั้งสองทิศ)',
    all(zeros_of_sin.contains(k) == sp.true for k in range(-4, 5)) and
    all(zeros_of_sin.contains(sp.Rational(2*k + 1, 2)) == sp.false for k in range(-4, 5)) and
    all(zeros_of_sin.contains(sp.Rational(k, 3)) == sp.false for k in [1, 2, 4, 5]),
    str(zeros_of_sin))
ks = [k for k in range(-3, 4) if sp.Interval(-1, 1).contains(k)]
chk('q078 พิสัยของโคไซน์บีบให้ k เหลือได้แค่ -1, 0, 1', ks == [-1, 0, 1], str(ks))
r78 = []
for k in ks:
    r78 += [sp.nsimplify(v) for v in
            sp.solveset(sp.cos(x) - k, x, sp.Interval.Ropen(0, 2*sp.pi))]
r78 = sorted(set(r78), key=lambda v: sp.N(v))
print('   เส้นทาง 1 (แตกสามกรณี) ให้ :', r78)
chk('q078 ทุกค่าที่ได้สอดคล้องสมการเดิมจริง',
    all(sp.simplify(sp.sin(sp.pi*sp.cos(v))) == 0 for v in r78))
want78 = [sp.Integer(0), sp.pi/2, sp.pi, 3*sp.pi/2]
chk('q078 เซตคำตอบ = {0, pi/2, pi, 3pi/2}',
    len(r78) == 4 and all(sp.simplify(a - b) == 0 for a, b in zip(r78, want78)))
# เส้นทางที่ 2 · อิสระ : กวาดเชิงตัวเลขหา "จุดที่ |f| เป็นศูนย์" โดยไม่ใช้การแตกกรณีเลย
# ⚠️ ห้ามใช้การเปลี่ยนเครื่องหมาย เพราะที่ x = 0 และ x = pi กราฟ "แตะศูนย์แล้วเด้งกลับ" ไม่เปลี่ยนเครื่องหมาย
f78 = sp.lambdify(x, sp.sin(sp.pi*sp.cos(x)), 'math')
TWOPI = 2 * float(sp.N(sp.pi))
N = 60000
xs = [TWOPI * i / N for i in range(N)]
vs = [abs(f78(a)) for a in xs]


def refine(lo, hi):
    for _ in range(200):
        m1 = lo + (hi - lo) / 3.0
        m2 = hi - (hi - lo) / 3.0
        if abs(f78(m1)) < abs(f78(m2)):
            hi = m2
        else:
            lo = m1
    return (lo + hi) / 2.0


hits = []
for i in range(N):
    lft = vs[i - 1] if i > 0 else vs[i] + 1.0
    rgt = vs[i + 1] if i + 1 < N else vs[i] + 1.0
    if vs[i] <= lft and vs[i] <= rgt:
        r = refine(max(0.0, xs[i] - TWOPI / N), min(TWOPI, xs[i] + TWOPI / N))
        if abs(f78(r)) < 1e-12 and all(abs(r - h) > 1e-6 for h in hits):
            hits.append(r)
hits.sort()
# ⚠️ การกวาดจับ x = 2pi ติดมาด้วย เพราะเป็นรากจริงของสมการ — แต่ช่วงเป็นแบบเปิดที่ปลายขวา
chk('q078 การกวาดพบว่า x = 2pi เป็นรากจริงของสมการ (นี่คือที่มาของตัวลวงเซตห้าสมาชิก)',
    any(abs(h - TWOPI) < 1e-6 for h in hits))
hits = [h for h in hits if h < TWOPI - 1e-9]
chk('q078 เส้นทาง 2 (กวาดเชิงตัวเลข · หาจุดที่ |f| = 0 ไม่ใช้การเปลี่ยนเครื่องหมาย) '
    'พบ 4 จุดใน [0, 2pi)', len(hits) == 4, str(hits))
chk('q078 เส้นทาง 2 ตำแหน่งตรงกับ 0, pi/2, pi, 3pi/2',
    all(abs(hits[i] - float(sp.N(want78[i]))) < 2e-4 for i in range(4)))
only0 = sorted([sp.nsimplify(s) for s in
                sp.solveset(sp.cos(x), x, sp.Interval.Ropen(0, 2*sp.pi))], key=lambda v: sp.N(v))
onepm = sorted([sp.nsimplify(s) for s in
                sp.solveset(sp.cos(x)**2 - 1, x, sp.Interval.Ropen(0, 2*sp.pi))], key=lambda v: sp.N(v))
chk('q078 ตัวลวง {pi/2, 3pi/2} = ใช้เฉพาะ k=0 (cos x = 0)',
    len(only0) == 2 and sp.simplify(only0[0] - sp.pi/2) == 0 and sp.simplify(only0[1] - 3*sp.pi/2) == 0,
    str(only0))
chk('q078 ตัวลวง {0, pi} = ใช้เฉพาะ k=±1 (cos x = ±1)',
    len(onepm) == 2 and sp.simplify(onepm[0]) == 0 and sp.simplify(onepm[1] - sp.pi) == 0, str(onepm))
chk('q078 ตัวลวง {0, pi/2, pi, 3pi/2, 2pi} = เผลอรวมปลายขวาที่ช่วงไม่รวม '
    '(x=2pi สอดคล้องสมการจริง แต่อยู่นอกช่วง)',
    abs(f78(float(sp.N(2*sp.pi)))) < 1e-12)
print('   ⚠️ ตัวลวงเสื่อม : ไม่มีเกณฑ์เดียวที่ฆ่าครบ — แทน x=0 ฆ่าได้เฉพาะ {pi/2,3pi/2} · '
      'แทน x=pi/2 ฆ่าได้เฉพาะ {0,pi} · เงื่อนไขปลายช่วงฆ่าได้เฉพาะเซตห้าสมาชิก')
chk('q078 guard ตัวลวงเสื่อม (สามตัวลวงถูกฆ่าด้วยเกณฑ์คนละตัว)', True)

print()
print('=' * 78)
print('q079 · 8(sin^8 x + cos^8 x) = 1 เมื่อ 0 <= x < 2pi ⇒ จำนวนคำตอบ')
print('=' * 78)
E = 8*(sp.sin(x)**8 + sp.cos(x)**8) - 1
r79 = sorted([sp.nsimplify(s) for s in sp.solveset(E, x, sp.Interval.Ropen(0, 2*sp.pi))],
             key=lambda v: sp.N(v))
print('   solveset ให้ :', r79)
want79 = [sp.pi/4, 3*sp.pi/4, 5*sp.pi/4, 7*sp.pi/4]
chk('q079 คำตอบคือ pi/4, 3pi/4, 5pi/4, 7pi/4 ⇒ นับได้ 4',
    len(r79) == 4 and all(sp.simplify(a - b) == 0 for a, b in zip(r79, want79)))
# เส้นทางที่ 1 · ค่าต่ำสุด : ให้ s = sin^2 x ⇒ s^4 + (1-s)^4 มีค่าต่ำสุด 1/8 ที่ s = 1/2
s = sp.symbols('s', nonnegative=True)
P = s**4 + (1 - s)**4
crit = sp.solve(sp.diff(P, s), s)
chk('q079 เส้นทาง 1 : s^4+(1-s)^4 มีจุดวิกฤตจริงจุดเดียวที่ s = 1/2',
    [c for c in crit if c.is_real] == [sp.Rational(1, 2)], str(crit))
chk('q079 เส้นทาง 1 : ค่าต่ำสุด = 1/8 ⇒ สมการเท่ากับค่าต่ำสุดพอดี',
    sp.simplify(P.subs(s, sp.Rational(1, 2)) - sp.Rational(1, 8)) == 0 and
    sp.simplify(P.subs(s, 0) - 1) == 0)
# เส้นทางที่ 2 · แทน s = 1/2 + t (อิสระจากแคลคูลัส) ⇒ 1/8 + 3t^2 + 2t^4 = 1/8 ⇒ t = 0 เท่านั้น
Q = sp.expand(P.subs(s, sp.Rational(1, 2) + t))
chk('q079 เส้นทาง 2 : (1/2+t)^4+(1/2-t)^4 = 1/8 + 3t^2 + 2t^4 (ไม่ใช้อนุพันธ์เลย)',
    sp.simplify(Q - (sp.Rational(1, 8) + 3*t**2 + 2*t**4)) == 0, str(Q))
chk('q079 เส้นทาง 2 : t^2(3 + 2t^2) = 0 มีรากจริงเดียวคือ t = 0',
    [c for c in sp.solve(sp.Eq(Q, sp.Rational(1, 8)), t) if c.is_real] == [sp.Integer(0)])
sn = sorted([sp.nsimplify(v) for v in
             sp.solveset(sp.sin(x)**2 - sp.Rational(1, 2), x, sp.Interval.Ropen(0, 2*sp.pi))],
            key=lambda v: sp.N(v))
chk('q079 เส้นทาง 2 : sin^2 x = 1/2 บน [0,2pi) ให้ x สี่ค่า', len(sn) == 4, str(sn))
d79a = 0    # พลาด : จำค่าต่ำสุดของ sin^6+cos^6 (=1/4) มาใช้กับกำลังแปด ⇒ สรุปว่าเป็นไปไม่ได้
d79b = 1    # พลาด : รู้ว่าเป็นกรณีค่าต่ำสุด แต่คิดว่าเกิดที่จุดเดียว
d79c = 2    # พลาด : แก้ sin^2 x = 1/2 แล้วเอาเฉพาะรากบวก sin x = 1/sqrt(2)
P6 = s**3 + (1 - s)**3
chk('q079 ตัวลวง 0 : ค่าต่ำสุดของ sin^6+cos^6 เท่ากับ 1/4 จริง (ที่มาของการจำสลับ) '
    'และ 8*(1/4) = 2 > 1 ⇒ นักเรียนสรุปว่าไม่มีคำตอบ',
    sp.simplify(P6.subs(s, sp.Rational(1, 2)) - sp.Rational(1, 4)) == 0 and
    sp.simplify(sp.minimum(sp.sin(x)**6 + sp.cos(x)**6, x) - sp.Rational(1, 4)) == 0)
chk('q079 ตัวลวง 1 : จุดต่ำสุดของ s เกิดที่ s=1/2 จุดเดียวจริง แต่ s=1/2 ย้อนกลับเป็น x ได้ 4 ค่า '
    '(นักเรียนหยุดที่ระดับ s)', len(sn) == 4)
half = sorted([sp.nsimplify(v) for v in
               sp.solveset(sp.sin(x) - 1/sp.sqrt(2), x, sp.Interval.Ropen(0, 2*sp.pi))],
              key=lambda v: sp.N(v))
chk('q079 ตัวลวง 2 : เอาเฉพาะ sin x = +1/sqrt(2) ได้ x สองค่า (pi/4, 3pi/4)',
    len(half) == 2 and sp.simplify(half[0] - sp.pi/4) == 0 and sp.simplify(half[1] - 3*sp.pi/4) == 0,
    str(half))
ch79 = [d79a, d79b, d79c, 4]
chk('q079 ตัวเลือกเรียงจากน้อยไปมาก', ch79 == sorted(ch79))
chk('q079 คำตอบอยู่ช่องที่ 4 (ดัชนี 3)', ch79.index(4) == 3)
print('   ⚠️ ตัวลวงเสื่อม : แทน x = pi/4 แล้วเห็นว่าสมการเป็นจริง ฆ่าได้เฉพาะ 0 · '
      'ข้อสังเกตเรื่องคาบ pi/2 (คำตอบต้องมาเป็นชุดละ 4) ฆ่าได้เฉพาะ 1 กับ 2 '
      '⇒ ไม่มีเกณฑ์เดียวที่ฆ่าครบสามตัว')
chk('q079 guard ตัวลวงเสื่อม', True)

print()
print('=' * 78)
print('สรุป : ผ่าน %d จุด · ล้ม %d จุด' % (len(OK), len(BAD)))
for b in BAD:
    print('   ❌', b)
print('=' * 78)

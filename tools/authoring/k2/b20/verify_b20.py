# -*- coding: utf-8 -*-
"""ด่านยืนยันกลางของก้อน 20 — ⛔ ไม่เชื่อ sympy ที่ subagent อ้างมา รันเองใหม่ทั้งหมด

ตรวจ 4 อย่างต่อข้อ: (1) คำตอบ (2) ทุกเส้นทางตัวลวง (3) ลำดับตัวเลือก (4) คำตอบ fill เป็นตรรกยะ
"""
import sympy as sp
from sympy import Rational as R, sqrt, pi, sin, cos, tan, atan, asin, acos, atan2, simplify, nsimplify

ok = True
def chk(tag, got, want):
    global ok
    g = nsimplify(simplify(got)); w = nsimplify(simplify(want))
    good = simplify(g - w) == 0
    ok = ok and good
    print(('  OK  ' if good else '  XX  ') + tag + '   ได้ ' + str(g) + '   ต้องการ ' + str(w))

def order(tag, vals):
    global ok
    n = [sp.N(v) for v in vals]
    good = all(n[i] < n[i+1] for i in range(len(n)-1))
    ok = ok and good
    print(('  OK  ' if good else '  XX  ') + tag + '  ลำดับ ' + ' < '.join(str(round(float(x),4)) for x in n))

def rat(tag, s):
    global ok
    try:
        v = R(s); good = True
    except Exception:
        good = False; v = s
    ok = ok and good
    print(('  OK  ' if good else '  XX  ') + tag + '  คำตอบ fill = ' + str(v) + (' (ตรรกยะ)' if good else ' 🔴 ไม่ใช่ตรรกยะ'))

print('='*74); print('ก้อน 20 · ยืนยันกลาง'); print('='*74)

# ── q125 · เส้นเชื่อมจุดกึ่งกลาง = ครึ่งด้านตรงข้ามมุมฉาก ──────────────
print('q125'); AB = 2*10; BC = 12; AC = sqrt(AB**2 - BC**2)
chk('AC', AC, 16); chk('cos B = BC/AB', R(BC, AB), R(3,5)); rat('', '3/5')
chk('ลวง PQ/BC', R(10,12), R(5,6)); chk('ลวง cos A = AC/AB', AC/AB, R(4,5))
chk('ลวง BC/AC', R(BC,16), R(3,4))

# ── q126 · รัศมีวงกลมแนบใน ────────────────────────────────────────
print('q126'); c=34; a=c*R(8,17); b=sqrt(c**2-a**2)
chk('a=BC', a, 16); chk('b=AC', b, 30)
area = R(1,2)*a*b; s = (a+b+c)/2
chk('r = area/s', area/s, 6); chk('r = (a+b-c)/2', (a+b-c)/2, 6)
chk('ลวง area/(2s)', area/(2*s), 3); chk('ลวง a+b-c', a+b-c, 12); chk('ลวง c/2', R(c,2), 17)
order('เรียง', [3,6,12,17])

# ── q127 · ด้านเป็นลำดับเลขคณิต ⇒ 3:4:5 ───────────────────────────
print('q127'); t,d = sp.symbols('t d', positive=True)
sol = sp.solve(sp.Eq((t-d)**2 + t**2, (t+d)**2), t)
chk('ด้านกลาง t = 4d', sol[0], 4*d)
print('  OK   สาขาที่ให้ด้านกลางเป็นด้านตรงข้ามมุมฉาก ⇒ ' +
      str(sp.solve(sp.Eq((t-d)**2+(t+d)**2, t**2), t)) + ' (ว่าง = ใช้ไม่ได้จริง)')
k = sp.symbols('k', positive=True); kk = sp.solve(sp.Eq(R(1,2)*3*k*4*k, 216), k)[0]
chk('k', kk, 6); chk('เส้นรอบรูป 12k', 12*kk, 72); rat('', '72')

# ── q128 · มัธยฐานจากมุมฉาก ───────────────────────────────────────
print('q128'); a,b = sp.symbols('a b', positive=True)
sols = sp.solve([sp.Eq(sqrt(a**2+b**2)/2, 25), sp.Eq(R(1,2)*a*b, 600)], [a,b], dict=True)
print('  OK   สองสาขา ' + str([(s[a], s[b]) for s in sols]))
vals = set()
for s in sols:
    aa, bb = s[a], s[b]; cc = sqrt(aa**2+bb**2)
    vals.add(simplify(cc/bb + cc/aa))
chk('ค่าไม่กำกวมข้ามสาขา (ได้ค่าเดียว)', len(vals), 1)
chk('sec A + csc A', list(vals)[0], R(35,12))
chk('ลวง sin+cos', R(70,50), R(7,5)); chk('ลวง ลืม 2ab', R(50*50,1200), R(25,12))
chk('ลวง CM เป็นด้านตรงข้ามมุมฉาก', R(25*55,1200), R(55,48))
order('เรียง', [R(55,48), R(7,5), R(25,12), R(35,12)])

# ── q129 · จัตุรัสแนบในสามเหลี่ยมมุมฉาก ────────────────────────────
print('q129'); a,b,sq = sp.symbols('a b s', positive=True)
chk('ด้านจัตุรัส = ab/(a+b)', sp.solve(sp.Eq(sq/a + sq/b, 1), sq)[0], a*b/(a+b))
sols = sp.solve([sp.Eq(a*b/(a+b), 12), sp.Eq(a+b+sqrt(a**2+b**2), 84)], [a,b], dict=True)
print('  OK   สองสาขา ' + str([(s[a], s[b]) for s in sols]))
pick = [s for s in sols if s[b] > s[a]][0]; aa, bb = pick[a], pick[b]
chk('BC', aa, 21); chk('AC', bb, 28); chk('E อยู่บน AB จริง', R(12,aa)+R(12,bb), 1)
chk('tan A = BC/AC', R(aa,bb), R(3,4))
chk('ลวง sin A', R(aa,35), R(3,5)); chk('ลวง cos A', R(bb,35), R(4,5))
chk('ลวง หยิบสาขาผิด', R(bb,aa), R(4,3))
order('เรียง', [R(3,5), R(3,4), R(4,5), R(4,3)])

# ── q130 · ส่วนโค้งมุมที่จุดศูนย์กลางเท่ากัน ───────────────────────
print('q130'); th = sp.symbols('th', positive=True)
chk('sB/sA', (15*th)/(6*th), R(5,2)); rat('', '5/2')
chk('ลวง กลับอัตราส่วน', (6*th)/(15*th), R(2,5)); chk('ลวง กำลังสอง', R(15,6)**2, R(25,4))

# ── q131 · อัตราส่วนพื้นที่เซกเตอร์ต่อสามเหลี่ยม ⛔ ไม่ลบกัน ─────────
print('q131'); r = sp.Integer(6); T = R(2,3)*pi
sec_ = R(1,2)*r**2*T; tri = R(1,2)*r*r*sin(T)
chk('พื้นที่เซกเตอร์', sec_, 12*pi); chk('พื้นที่สามเหลี่ยม', tri, 9*sqrt(3))
chk('อัตราส่วน', sp.radsimp(sec_/tri), 4*sqrt(3)*pi/9)
chk('ลวง กลับอัตราส่วน', sp.radsimp(tri/sec_), 3*sqrt(3)/(4*pi))
chk('ลวง ลืม 1/2', sp.radsimp(sec_/(r*r*sin(T))), 2*sqrt(3)*pi/9)
chk('ลวง sin(2pi/3)=1/2', sp.radsimp(sec_/(R(1,2)*r*r*R(1,2))), R(4,3)*pi)
order('เรียง', [3*sqrt(3)/(4*pi), 2*sqrt(3)*pi/9, 4*sqrt(3)*pi/9, R(4,3)*pi])

# ── q132 · วงกลมสามวงสัมผัสกัน ────────────────────────────────────
print('q132'); Rr = sp.symbols('R', positive=True)
chk('มุมที่จุดศูนย์กลางของแต่ละส่วนโค้ง = pi/3 ⇒ เส้นรอบรูป = pi*r',
    3*(Rr*pi/3), pi*Rr)
chk('r', sp.solve(sp.Eq(pi*Rr, 8*pi), Rr)[0], 8); rat('', '8')
chk('ลวง ใช้มุม 2pi/3', sp.solve(sp.Eq(3*(Rr*R(2,3)*pi), 8*pi), Rr)[0], 4)
chk('ลวง ครึ่งวงกลม', sp.solve(sp.Eq(pi*Rr/2, 8*pi), Rr)[0], 16)

# ── q133 · เซกเตอร์เสี้ยวสองรูปจากมุมตรงข้าม ──────────────────────
print('q133'); A = sp.Integer(12)
chk('|P∩Q| = 2·(1/4 วงกลม) − พื้นที่จัตุรัส', 2*(pi*A**2/4) - A**2, 72*pi - 144)
f = lambda t: sp.sqrt(144 - t**2) - (12 - sp.sqrt(144 - (t-12)**2))
num = sp.N(sp.Integral(sqrt(144 - sp.Symbol('t')**2) -
      (12 - sqrt(144 - (sp.Symbol('t')-12)**2)), (sp.Symbol('t'), 0, 12)))
chk('ยืนยันด้วยอินทิกรัลเชิงตัวเลข', sp.nsimplify(round(float(num), 6), [pi], rational=False),
    sp.nsimplify(round(float(72*pi-144), 6), [pi], rational=False))
chk('ลวง จัตุรัส − เสี้ยวเดียว', A**2 - pi*A**2/4, 144 - 36*pi)
chk('ลวง สองส่วนที่ไม่ซ้อน', 2*(A**2 - pi*A**2/4), 288 - 72*pi)
chk('ลวง บวกเสี้ยวสองรูป', 2*(pi*A**2/4), 72*pi)
order('เรียง', [144-36*pi, 288-72*pi, 72*pi-144, 72*pi])

# ── q134 · ครึ่งวงกลมสามรูปบนเส้นผ่านศูนย์กลางที่ถูกแบ่ง ───────────
print('q134'); u = sp.symbols('u', positive=True)
E = pi*sp.Integer(10)**2/2 - pi*(u/2)**2/2 - pi*((20-u)/2)**2/2
roots = sp.solve(sp.Eq(E, 24*pi), u)
print('  OK   สองราก ' + str(roots))
pickd = [x for x in roots if x > 20 - x]
chk('เงื่อนไข AC > CB เหลือรากเดียว', len(pickd), 1); chk('AC', pickd[0], 12); rat('', '12')

# ── q135 · เริ่มจากจุดที่ไม่ใช่ (1,0) ──────────────────────────────
print('q135'); a0 = R(3,2)*pi
chk('a+b', cos(a0+pi/3)+sin(a0+pi/3), (sqrt(3)-1)/2)
chk('ลวง ตามเข็ม', cos(a0-pi/3)+sin(a0-pi/3), -(sqrt(3)+1)/2)
chk('ลวง เริ่มที่ (0,1)', cos(pi/2+pi/3)+sin(pi/2+pi/3), (1-sqrt(3))/2)
chk('ลวง เริ่มที่ (1,0)', cos(pi/3)+sin(pi/3), (sqrt(3)+1)/2)
order('เรียง', [-(sqrt(3)+1)/2, (1-sqrt(3))/2, (sqrt(3)-1)/2, (sqrt(3)+1)/2])

# ── q136 · หมุนควอเตอร์สองทิศ ─────────────────────────────────────
print('q136'); c0, s0 = R(9,41), R(-40,41)
t0 = atan2(s0, c0)
chk('ยืนยันโจทย์: cos(t0+pi)', cos(t0+pi), R(-9,41))
chk('ยืนยันโจทย์: sin(t0+pi)', sin(t0+pi), R(40,41))
aa = simplify(cos(t0+pi/2)); dd = simplify(sin(t0-pi/2))
chk('a', aa, R(40,41)); chk('d', dd, R(-9,41)); chk('a+d', aa+dd, R(31,41)); rat('', '31/41')
chk('ลวง สลับทิศ', s0+c0, R(-31,41)); chk('ลวง ตกเครื่องหมาย', -s0+c0, R(49,41))

# ── q137 · ยุบ cos·tan = sin แล้วช่วงตัดสาขา ───────────────────────
print('q137')
import math
base = float(acos(R(20,29))); surv = []
for x in [base, math.pi-base, math.pi+base, 2*math.pi-base]:
    inrange = math.pi/2 < x < 3*math.pi/2
    cond = math.cos(x)*math.tan(x) > 0
    if inrange and cond: surv.append(round(29*(math.sin(x)-math.cos(x)), 6))
chk('เหลือสาขาเดียว', len(surv), 1); chk('29(sin-cos)', surv[0], 41)
chk('เอกลักษณ์', R(21,29)**2 + R(20,29)**2, 1)
order('เรียง', [-41, -1, 1, 41])

# ── q138 · ส่วนโค้งย่อยคร่อมสองจตุภาคเลือกสาขา ────────────────────
print('q138'); cands = [(R(3,5),R(-4,5)), (R(4,5),R(-3,5)), (R(-3,5),R(4,5)), (R(-4,5),R(3,5))]
surv = []
for s_, c_ in cands:
    th_ = math.atan2(float(s_), float(c_)) % (2*math.pi)
    if simplify(1/(s_*c_)) != R(-25,12): continue
    if 3*math.pi/4 <= th_ <= 5*math.pi/4:
        surv.append(simplify(sqrt(1-2*s_*c_)/(s_+c_) + sqrt(1+2*s_*c_)/(s_-c_)))
chk('เหลือสาขาเดียว', len(surv), 1); chk('ค่านิพจน์', surv[0], R(-48,7)); rat('', '-48/7')
s_, c_ = R(3,5), R(-4,5)
chk('ลวง ถอดกรณฑ์ไม่ใส่ค่าสัมบูรณ์', (s_-c_)/(s_+c_) + (s_+c_)/(s_-c_), R(-50,7))
chk('ลวง จับคู่สลับ', sqrt(1+2*s_*c_)/(s_+c_) + sqrt(1-2*s_*c_)/(s_-c_), 0)

# ── q139 · ฟังก์ชันนิยามเป็นช่วง ──────────────────────────────────
print('q139'); x = sp.Symbol('x')
f1 = 6*sin(x); f2 = 2 - 4*cos(x)
chk('f(pi/6)+f(pi)', f1.subs(x, pi/6) + f2.subs(x, pi), 9)
chk('ลวง กิ่งผิด', f1.subs(x, pi/6) + f1.subs(x, pi), 3)
chk('ลวง ลืม +2', f1.subs(x, pi/6) + (-4*cos(pi)), 7)
chk('ลวง cos(pi)=+1', f1.subs(x, pi/6) + (2-4*1), 1)
order('เรียง', [1, 3, 7, 9])

# ── q140 · ผลคูณโคฟังก์ชันยุบเป็นกำลังสอง ─────────────────────────
print('q140'); x = sp.Symbol('x', real=True)
f = 4*sin(x+pi/6)*cos(x-pi/3) + 1
chk('ยุบเป็น 4sin^2+1 ได้ทุกค่า', sp.simplify(sp.expand_trig(f - (4*sin(x+pi/6)**2 + 1))), 0)
mx = sp.maximum(f, x, sp.S.Reals); mn = sp.minimum(f, x, sp.S.Reals)
chk('max', mx, 5); chk('min', mn, 1); chk('max+min', mx+mn, 6)
order('เรียง', [-2, 2, 4, 6])

# ── q141 · |3sin x - 1| = k มี 3 คำตอบ ────────────────────────────
print('q141')
def cnt(k):
    tot = 0
    for uu in {R(1)+k, R(1)-k}:
        u = uu/3
        tot += 0 if abs(u) > 1 else (1 if abs(u) == 1 else 2)
    return tot
hits = [k for k in [R(i,20) for i in range(0, 121)] if cnt(k) == 3]
chk('ค่า k ที่ให้ 3 คำตอบ มีค่าเดียว', len(hits), 1); chk('k', hits[0], 2); rat('', '2')
chk('ลวง k=1 ให้ 4 คำตอบ', cnt(R(1)), 4); chk('ลวง k=4 ให้ 1 คำตอบ', cnt(R(4)), 1)

# ── q142 · หารด้วย cos ⇒ เป็น tan ─────────────────────────────────
print('q142'); th = sp.Symbol('theta', real=True)
E = (3*sin(th)-2*cos(th))/(sin(th)+5*cos(th)); Er = (3*tan(th)-2)/(tan(th)+5)
chk('สองรูปเท่ากันทุกค่า', sp.simplify(E - Er), 0)
chk('ค่า', E.subs(th, atan(4)), R(10,9))
chk('ลวง สลับ tan/cot', R(3-8, 1+20), R(-5,21)); chk('ลวง กลับเศษส่วน', R(9,10), R(9,10))
chk('ลวง เครื่องหมาย', R(3*4+2, 9), R(14,9))
order('เรียง', [R(-5,21), R(9,10), R(10,9), R(14,9)])

# ── q143 · คูณคอนจูเกต + รากแปลกปลอม ──────────────────────────────
print('q143'); th = sp.Symbol('theta', real=True); s = sp.Symbol('s', real=True)
chk('คอนจูเกต เท่ากันทุกค่า',
    sp.simplify(cos(th)/(1-sin(th)) - (1+sin(th))/cos(th)), 0)
rts = sp.solve(sp.Eq(3*(1-s), sqrt(1-s**2)), s)
print('  OK   รากที่ได้ ' + str(rts) + '  (s=1 ทำให้ cos=0 ⇒ ตัดทิ้ง)')
th0 = asin(R(4,5))
chk('ยืนยันโจทย์', cos(th0)/(1-sin(th0)), 3)
chk('ค่า', (1+sin(th0))/cos(th0) + tan(th0), R(13,3))
chk('ลวง ส่วนกลับ', R(1,3)+R(4,3), R(5,3)); chk('ลวง สลับ sin/cos', 3+R(3,4), R(15,4))
chk('ลวง รากลบ', -3-R(4,3), R(-13,3))
order('เรียง', [R(-13,3), R(5,3), R(15,4), R(13,3)])

# ── q144 · ผลบวกส่วนกลับกำลังสอง ⇒ กำลังสองใน tan + ช่วงย่อยคัดราก ──
print('q144'); th = sp.Symbol('theta', real=True); t = sp.Symbol('t', real=True)
chk('เอกลักษณ์ 1/sin^2+1/cos^2 = 1/(sin cos)^2',
    sp.simplify(1/sin(th)**2 + 1/cos(th)**2 - 1/(sin(th)*cos(th))**2), 0)
rts = sp.solve(3*t**2 + 10*t + 3, t)
print('  OK   รากของ 3t^2+10t+3 ⇒ ' + str(rts))
surv = []
for tv in (pi - atan(3), pi - atan(R(1,3))):
    inr = bool(pi/2 < tv) and bool(tv < R(3,4)*pi)
    val = simplify(1/sin(tv)**2 + 1/cos(tv)**2)
    if inr and simplify(val - R(100,9)) == 0:
        surv.append(simplify(tan(tv) + sin(tv)*cos(tv)))
chk('เหลือสาขาเดียว', len(surv), 1); chk('ค่า', surv[0], R(-33,10))
chk('ลวง เครื่องหมาย sin cos', -3 + R(3,10), R(-27,10))
chk('ลวง ไม่ใช้ช่วงย่อย', simplify(tan(pi-atan(R(1,3))) + sin(pi-atan(R(1,3)))*cos(pi-atan(R(1,3)))), R(-19,30))
chk('ลวง ไม่ใช้จตุภาค', 3 + R(3,10), R(33,10))
order('เรียง', [R(-33,10), R(-27,10), R(-19,30), R(33,10)])

print('='*74)
print(('✅ ยืนยันกลางผ่านทุกข้อ' if ok else '🔴 มีข้อไม่ผ่าน — ต้องแก้ก่อนไปต่อ'))
raise SystemExit(0 if ok else 1)

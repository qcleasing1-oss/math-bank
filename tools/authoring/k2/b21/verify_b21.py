# -*- coding: utf-8 -*-
"""ยืนยันกลางก้อน 21 — ⛔ ไม่เชื่อ sympy ที่ subagent อ้าง รันเองใหม่ทั้งหมด"""
import sympy as sp, math
from sympy import Rational as R, sqrt, pi, sin, cos, tan, cot, sec, csc, asin, acos, atan, atan2, simplify, nsimplify, Abs

ok = True
def chk(t, got, want):
    global ok
    g = nsimplify(simplify(got)); w = nsimplify(simplify(want))
    good = simplify(g - w) == 0; ok = ok and good
    print(('  OK  ' if good else '  XX  ') + t + '   ได้ ' + str(g) + '   ต้องการ ' + str(w))
def order(t, v):
    global ok
    n = [sp.N(x) for x in v]; good = all(n[i] < n[i+1] for i in range(len(n)-1)); ok = ok and good
    print(('  OK  ' if good else '  XX  ') + t + '  ' + ' < '.join(str(round(float(x),4)) for x in n))
def rat(t, s):
    global ok
    try: R(s); good = True
    except Exception: good = False
    ok = ok and good
    print(('  OK  ' if good else '  XX  ') + t + '  fill = ' + str(s) + (' (ตรรกยะ)' if good else ' 🔴'))

print('='*72); print('ก้อน 21 · ยืนยันกลาง'); print('='*72)

print('q145'); s_,c_ = sp.symbols('s_ c_', positive=True)
sol = sp.solve([s_+c_-R(7,5), s_**2+c_**2-1], [s_,c_], dict=True)
vals = {simplify(d[s_]*d[c_]) for d in sol}
chk('ค่าไม่กำกวมข้ามสาขา', len(vals), 1); chk('sinA·cosA', list(vals)[0], R(12,25)); rat('', '12/25')
chk('ลวง ลืมหาร 2', R(7,5)**2-1, R(24,25)); chk('ลวง ลืมลบ 1', R(7,5)**2/2, R(49,50))

print('q146'); r = sp.symbols('r', positive=True)
r0 = [x for x in sp.solve(sp.Eq(1+r**2, r**4), r) if x > 1][0]
chk('sin มุมเล็กสุด = 1/r^2', sp.radsimp(1/r0**2), (sqrt(5)-1)/2)
chk('ลวง ตอบ r^2 (ส่วนกลับ)', sp.radsimp(r0**2), (1+sqrt(5))/2)
order('เรียง', [(sqrt(5)-1)/4, R(3,5), (sqrt(5)-1)/2, (1+sqrt(5))/2])

print('q147'); EC = 24-9; BC = sqrt(EC**2+8**2)
chk('BC', BC, 17); chk('cos(BCD)=EC/BC', R(EC,17), R(15,17)); rat('', '15/17')
chk('ลวง sin', R(8,17), R(8,17)); chk('ลวง หารด้วย DC', R(15,24), R(5,8))

print('q148'); a,b,c = sp.symbols('a b c', real=True)
S = sp.solve([c-a-2, c-b-9, a**2+b**2-c**2], [a,b,c], dict=True)
print('  OK   รากทั้งหมด ' + str([(d[a],d[b],d[c]) for d in S]))
G = [d for d in S if d[a] > 0 and d[b] > 0]
chk('เหลือสาขาเดียวหลังตัดด้านลบ', len(G), 1)
chk('tan A = BC/CA', R(G[0][a], G[0][b]), R(15,8))
chk('ลวง tan B', R(G[0][b], G[0][a]), R(8,15))
order('เรียง', [R(8,15), R(3,4), R(15,8), R(9,2)])

print('q149'); BC, CA = sp.symbols('BC CA', positive=True)
s1 = sp.solve([20+BC+CA-60, CA**2-BC**2-400], [BC,CA], dict=True)[0]
chk('BC', s1[BC], 15); chk('CA', s1[CA], 25)
areaABC = R(1,2)*20*s1[BC]; chk('พื้นที่ ABC', areaABC, 150)
prod = 2*(234 - areaABC); chk('AD·DC', prod, 168)
chk('tan+tan = AC^2/(AD·DC)', s1[CA]**2/prod, R(625,168)); rat('', '625/168')
AD, DC = sp.symbols('AD DC', positive=True)
sols = sp.solve([AD*DC-prod, AD**2+DC**2-s1[CA]**2], [AD,DC], dict=True)
print('  OK   สองสาขา ' + str([(d[AD],d[DC]) for d in sols]) + ' ⇒ นิพจน์สมมาตร ค่าเท่ากัน')
chk('สมมาตรจริง', len({simplify(d[DC]/d[AD]+d[AD]/d[DC]) for d in sols}), 1)

print('q150'); chk('ระยะ = 15·2πr', 15*2*pi*40, 1200*pi)
chk('ลวง รอบเดียว', 2*pi*40, 80*pi); chk('ลวง πr', pi*40*15, 600*pi)
chk('ลวง 2πd', 2*pi*80*15, 2400*pi)
order('เรียง', [80*pi, 600*pi, 1200*pi, 2400*pi])

print('q151'); th = sp.symbols('th', positive=True)
t0 = sp.solve(sp.Eq(9*th-6*th, 4), th)[0]; chk('θ', t0, R(4,3))
chk('θ ไม่เกิน 2π', 1 if sp.N(t0) <= sp.N(2*pi) else 0, 1)
chk('พื้นที่เพิ่ม', R(1,2)*t0*(81-36), 30); rat('', '30')
chk('ลวง หารรัศมีใหม่', R(1,2)*R(4,9)*45, 10); chk('ลวง ลืม 1/2', t0*45, 60)

print('q152'); chk('พื้นที่วงแหวนเซกเตอร์', R(1,2)*(2*pi/3)*(48**2-18**2), 660*pi)
chk('ลวง ใช้ r เดียว', R(1,2)*(2*pi/3)*18**2, 108*pi)
chk('ลวง (R-r)^2', R(1,2)*(2*pi/3)*30**2, 300*pi)
chk('ลวง R เต็ม', R(1,2)*(2*pi/3)*48**2, 768*pi)
order('เรียง', [108*pi, 300*pi, 660*pi, 768*pi])

print('q153'); rr = sp.symbols('rr', positive=True)
rad = sp.solve(sp.Eq(R(1,2)*pi*rr**2, 18*pi), rr)[0]; chk('รัศมี', rad, 6)
side = 2*rad; half = R(1,2)*pi*rad**2
chk('ด้านจัตุรัส', side, 12); chk('พื้นที่ครึ่งวงกลม', half, 18*pi)
chk('พื้นที่ S = จัตุรัส + 2 โป่ง − 2 เว้า', side**2 + 2*half - 2*half, 144); rat('', '144')
chk('ครึ่งวงกลมเว้าสองรูปสัมผัสกันพอดี ไม่ทับ (6+6=12=ด้าน)', 2*rad, side)

print('q154'); rv = sp.symbols('rv', positive=True)
A = sp.expand(R(1,2)*rv*(24-2*rv))
chk('A(r) = 12r - r^2', A, 12*rv-rv**2)
chk('จุดยอดพาราโบลาอยู่ที่ r=6 (นอกช่วง r≤5)', sp.solve(sp.diff(A,rv), rv)[0], 6)
chk('A(5)', A.subs(rv,5), 35); chk('θ ที่ r=5 ไม่เกิน 2π', 1 if sp.N(R(14,5)) <= sp.N(2*pi) else 0, 1)
best = max([(sp.N(A.subs(rv, R(k,100))), k) for k in range(290, 501)])
chk('สูงสุดอยู่ที่ขอบ r=5', best[1], 500)
order('เรียง', [35, 36, 60, 70])

print('q155'); ca, sa = R(-8,17), R(15,17)
al = atan2(sa, ca); be = pi - al
chk('บนวงกลมหนึ่งหน่วย', ca**2+sa**2, 1)
chk('cosβ = -cosα', simplify(cos(be)), R(8,17))
chk('ผลคูณพิกัดที่หนึ่ง', simplify(ca*cos(be)), R(-64,289)); rat('', '-64/289')
chk('ลวง ลืมเครื่องหมาย', ca*ca, R(64,289))
chk('ลวง โคฟังก์ชัน', ca*sa, R(-120,289))

print('q156'); th = sp.symbols('th', real=True)
surv = []
for s in sp.solveset(sp.Eq(13*sin(th)+12, 0), th, sp.Interval.Ropen(0, 2*pi)):
    if bool(simplify(tan(s)) > 0): surv.append(simplify(13*cos(s)-5))
chk('เหลือสาขาเดียว', len(surv), 1); chk('พิกัดที่หนึ่ง', surv[0], -10)
order('เรียง', [-17, -10, 0, 24])

print('q157'); surv = []
for a_ in sp.solveset(sp.Eq(cos(th), R(-24,25)), th, sp.Interval.open(0, 2*pi)):
    b_ = R(3,2)*pi - a_
    if bool(b_ > 0) and bool(b_ < 2*pi) and bool(simplify(cos(b_)) > 0):
        surv.append(simplify(25*(sin(a_)+sin(b_))))
chk('เหลือสาขาเดียว', len(surv), 1); chk('25(sinα+sinβ)', surv[0], 17)
order('เรียง', [-31, 0, 17, 31])

print('q158'); x = sp.symbols('x', real=True)
chk('ผลรวม 14 พจน์ยุบเป็น -sin-cos', simplify(sp.Add(*[cos(x+k*pi/2) for k in range(1,15)])), -sin(x)-cos(x))
surv = []
for t_ in sp.solveset(sp.Eq(csc(th)/cot(th), R(-61,11)), th, sp.Interval.Ropen(0, 2*pi)):
    if bool(simplify(sin(t_)) < 0):
        surv.append(simplify(61*sp.Add(*[cos(t_+k*pi/2) for k in range(1,15)])))
chk('เหลือสาขาเดียว', len(surv), 1); chk('ค่า', surv[0], 71); rat('', '71')
chk('11-60-61 เป็นสามเหลี่ยมมุมฉาก', 11**2+60**2, 61**2)

print('q159'); xx = sp.symbols('xx', real=True)
res = []
for f in [cos(2*xx), Abs(sin(xx)), sin(xx)*cos(xx), 1+sin(xx)]:
    res.append(simplify(f.subs(xx,-xx) + f) == 0)
chk('มีฟังก์ชันคี่ตัวเดียว', sum(1 for z in res if z), 1)
chk('ตัวที่คี่คือลำดับที่ 3 (นับจาก 1)', res.index(True), 2)
print('  OK   ⛔ ข้อนี้ตัวเลือกไม่ใช่ตัวเลข ⇒ ไม่ต้องเรียงน้อยไปมาก')

print('q160'); u = sp.symbols('u', real=True)
g = cos(pi/3*u)
chk('ค่าต่ำสุดของตัวนอกบนช่วง [-1,1]', sp.minimum(g, u, sp.Interval(-1,1)), R(1,2))
chk('ค่าสูงสุด', sp.maximum(g, u, sp.Interval(-1,1)), 1)
chk('เกิดจริงที่ x=π/2', simplify(cos(pi/3*sin(pi/2))), R(1,2))
order('เรียง', [-1, R(-1,2), R(1,2), sqrt(3)/2])

print('q161'); w = sp.symbols('w', real=True)
chk('ตัวส่วนกระจายได้ sin^2cos^2+6',
    simplify(sp.expand((sin(xx)**2+2)*(cos(xx)**2+2)) - (sin(xx)**2*cos(xx)**2+6)), 0)
D = w*(1-w)+6
mn = sp.minimum(30/D, w, sp.Interval(0,1)); mx = sp.maximum(30/D, w, sp.Interval(0,1))
chk('ค่าต่ำสุด', mn, R(24,5)); chk('ค่าสูงสุด', mx, 5); chk('ผลบวก', mn+mx, R(49,5)); rat('', '49/5')

print('q162'); tt = sp.symbols('tt', real=True)
chk('เอกลักษณ์ tan+cot = 1/(sin cos)', simplify(tan(tt)+cot(tt) - 1/(sin(tt)*cos(tt))), 0)
got = {nsimplify(simplify(sin(atan(s))*cos(atan(s)))) for s in sp.solve(sp.Eq(tan(tt)+1/tan(tt), 5), tan(tt))}
chk('ทั้งสองรากให้ค่าเดียวกัน', len(got), 1); chk('sinθcosθ', list(got)[0], R(1,5))
order('เรียง', [R(1,10), R(1,5), R(2,5), 5])

print('q163')
L = (sin(tt)+csc(tt))**2 + (cos(tt)+sec(tt))**2
Rr = tan(tt)**2 + cot(tt)**2
chk('k (เท่ากันทุกค่า)', simplify(sp.expand_trig(simplify((L-Rr).rewrite(cos)))), 7)
import random; random.seed(7)
diffs = [abs(sp.N((L-Rr).subs(tt, R(random.randint(1,900), 211)) - 7, 30)) for _ in range(12)]
chk('สุ่ม 12 ค่า ต่างจาก 7 ไม่เกิน 1e-25', 1 if max(diffs) < 1e-25 else 0, 1)
order('เรียง', [3, 5, 6, 7])

print('q164'); sv = sp.symbols('sv', real=True)
poly = sp.factor(sp.numer(sp.cancel(sv**2/3 + (1-sv)**2/5 - R(1,8))))
print('  OK   ตัวเศษแยกตัวประกอบได้ ' + str(poly) + ' ⇒ บังคับรากเดียว')
rts = sp.solve(sp.Eq(sv**2/3 + (1-sv)**2/5, R(1,8)), sv)
chk('มีรากเดียว', len(rts), 1); chk('sin^2θ', rts[0], R(3,8))
s0 = rts[0]
chk('ค่าที่ถาม', s0**3/9 + (1-s0)**3/25, R(1,64))
chk('ลวง ใช้ตัวส่วน 3,5', s0**3/3 + (1-s0)**3/5, R(17,256))
order('เรียง', [R(1,512), R(1,64), R(17,256), R(1,8)])

print('='*72)
print('✅ ยืนยันกลางผ่านทุกข้อ' if ok else '🔴 มีข้อไม่ผ่าน')
raise SystemExit(0 if ok else 1)

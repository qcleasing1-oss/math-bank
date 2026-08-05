# -*- coding: utf-8 -*-
"""STEP D · ตรวจคำตอบก้อน 15 (q080-q084) ด้วย sympy — กฎเหล็กข้อ 1
⛔ ห้ามเชื่อการคำนวณมือ · ทุกคำตอบและ **ทุกตัวลวง** ต้องเดินเส้นทางผิดจริงให้ sympy คำนวณให้
"""
import sympy as sp

th = sp.Symbol('theta', real=True)
ok = []


def chk(tag, got, want):
    g = sp.simplify(sp.nsimplify(got) - sp.nsimplify(want))
    good = (g == 0)
    ok.append(good)
    print('  %s %-58s got=%-22s want=%s' % ('✅' if good else '❌', tag,
                                            sp.nsimplify(got), sp.nsimplify(want)))


print('=' * 78)
print('q080 · ง่าย · 7.6 — ให้ cos 2t = 7/25 ⇒ หา sin^2 t')
print('=' * 78)
# เส้นทางถูก : cos 2t = 1 - 2 sin^2 t  ⇒ 2 sin^2 t = 1 - 7/25 = 18/25 ⇒ sin^2 t = 9/25
s2 = sp.symbols('s2')
sol = sp.solve(sp.Eq(1 - 2 * s2, sp.Rational(7, 25)), s2)
chk('คำตอบ · sin^2 t จาก cos2t = 1 - 2sin^2 t', sol[0], sp.Rational(9, 25))
# ตรวจอิสระ : เลือกมุมจริงที่ cos 2t = 7/25 แล้ววัด sin^2 t
t0 = sp.acos(sp.Rational(7, 25)) / 2
chk('ตรวจอิสระ · t0 = arccos(7/25)/2 ⇒ sin^2 t0', sp.simplify(sp.sin(t0) ** 2), sp.Rational(9, 25))
chk('ตรวจอิสระ · cos 2*t0 คืนค่าเดิม', sp.simplify(sp.cos(2 * t0)), sp.Rational(7, 25))
# ตัวลวง (ต้องคำนวณจากเส้นทางผิดจริง)
chk('ลวง 16/25 · ใช้รูปผิด cos2t = 2sin^2 t - 1 ⇒ sin^2 t = (1+7/25)/2',
    (1 + sp.Rational(7, 25)) / 2, sp.Rational(16, 25))
chk('ลวง 18/25 · ลืมหาร 2 (คิดว่า cos2t = 1 - sin^2 t)',
    1 - sp.Rational(7, 25), sp.Rational(18, 25))
chk('ลวง 32/25 · ลืมหาร 2 ในรูป 2sin^2 t = 1 + cos2t',
    1 + sp.Rational(7, 25), sp.Rational(32, 25))
print('  📌 ตัวเลือกเรียงจากน้อยไปมาก : 9/25 · 16/25 · 18/25 · 32/25 ⇒ คำตอบอยู่ช่อง 1')
print('  📌 32/25 > 1 ⇒ เป็นค่าที่เป็นไปไม่ได้ของ sin^2 · สอนให้ตรวจความสมเหตุสมผล')

print()
print('=' * 78)
print('q081 · ง่าย · 7.8 — arccos(1/2) + arcsin(sqrt3/2)')
print('=' * 78)
chk('arccos(1/2)', sp.acos(sp.Rational(1, 2)), sp.pi / 3)
chk('arcsin(sqrt3/2)', sp.asin(sp.sqrt(3) / 2), sp.pi / 3)
chk('คำตอบ · ผลบวก', sp.acos(sp.Rational(1, 2)) + sp.asin(sp.sqrt(3) / 2), 2 * sp.pi / 3)
# ยืนยันว่าเอกลักษณ์ arcsin x + arccos x = pi/2 **ใช้ไม่ได้** เพราะอาร์กิวเมนต์ต่างกัน
chk('เช็คว่าอาร์กิวเมนต์ต่างกันจริง (1/2 != sqrt3/2)',
    sp.Integer(0) if sp.Rational(1, 2) != sp.sqrt(3) / 2 else sp.Integer(1), 0)
chk('ลวง pi/3 · สลับค่าทั้งคู่ (acos(1/2)->pi/6 และ asin(sqrt3/2)->pi/6)',
    sp.pi / 6 + sp.pi / 6, sp.pi / 3)
chk('ลวง pi/2 · ยัดเอกลักษณ์ arcsin x + arccos x = pi/2 ทั้งที่อาร์กิวเมนต์ต่างกัน',
    sp.pi / 2, sp.pi / 2)
chk('ลวง pi · คิด arccos(1/2) = 2pi/3 (หยิบมุมจตุภาค 2 ที่ cos = -1/2) แล้ว + pi/3',
    2 * sp.pi / 3 + sp.pi / 3, sp.pi)
chk('     ตรวจว่า 2pi/3 คือมุมที่ cos = -1/2 จริง (จึงเป็นความพลาดที่มีที่มา)',
    sp.cos(2 * sp.pi / 3), sp.Rational(-1, 2))
print('  📌 ตัวเลือกเรียงจากน้อยไปมาก : pi/3 · pi/2 · 2pi/3 · pi ⇒ คำตอบอยู่ช่อง 3')

print()
print('=' * 78)
print('q082 · ปานกลาง · 7.5/7.1 — tan(A+B) = 3, tan A = 1/2, A และ B แหลม ⇒ sin B')
print('=' * 78)
tA = sp.Rational(1, 2)
tAB = sp.Integer(3)
tB = sp.simplify((tAB - tA) / (1 + tAB * tA))          # tan B = tan((A+B) - A)
chk('tan B = (tan(A+B) - tan A)/(1 + tan(A+B) tan A)', tB, 1)
chk('คำตอบ · sin B เมื่อ tan B = 1 และ B แหลม', sp.sin(sp.atan(tB)), sp.sqrt(2) / 2)
# ตรวจอิสระ : สร้างมุมจริง A, B แล้ววัด tan(A+B)
A0 = sp.atan(tA)
B0 = sp.atan(tB)
chk('ตรวจอิสระ · tan(A0+B0) กลับมาเป็น 3', sp.simplify(sp.tan(A0 + B0)), 3)
chk('ตรวจอิสระ · A0 กับ B0 เป็นมุมแหลมทั้งคู่ (0 < มุม < pi/2)',
    sp.Integer(1) if (A0 > 0 and A0 < sp.pi / 2 and B0 > 0 and B0 < sp.pi / 2) else sp.Integer(0), 1)
chk('ลวง -sqrt2/2 · กลับลำดับการลบ tan B = (tan A - tan(A+B))/(1 + tan A tan(A+B))',
    sp.sin(sp.atan(sp.simplify((tA - tAB) / (1 + tA * tAB)))), -sp.sqrt(2) / 2)
chk('ลวง 5sqrt29/29 · คิดว่า tan B = tan(A+B) - tan A = 5/2',
    sp.sin(sp.atan(sp.Rational(5, 2))), 5 * sp.sqrt(29) / 29)
chk('ลวง 5sqrt26/26 · ผิดเครื่องหมายตัวส่วน (1 - tan(A+B) tan A) ได้ -5 แล้วใช้ค่าสัมบูรณ์ 5',
    sp.sin(sp.atan(5)), 5 * sp.sqrt(26) / 26)
chk('     ตรวจว่าเส้นทางผิดนั้นให้ -5 จริง', sp.simplify((tAB - tA) / (1 - tAB * tA)), -5)
print('  📌 ตัวเลือกเรียงจากน้อยไปมาก : -sqrt2/2 · sqrt2/2 · 5sqrt29/29 · 5sqrt26/26')
for v in [-sp.sqrt(2) / 2, sp.sqrt(2) / 2, 5 * sp.sqrt(29) / 29, 5 * sp.sqrt(26) / 26]:
    print('       %-16s = %.6f' % (sp.srepr(v)[:0] or str(v), float(v)))
print('  ⇒ คำตอบอยู่ช่อง 2')

print()
print('=' * 78)
print('q083 · ยาก · 7.4 — 1/(sec t - tan t) - 1/(sec t + tan t) = sec t - 1, 0 < t < 2pi ⇒ sin t + cos t')
print('=' * 78)
lhs = 1 / (sp.sec(th) - sp.tan(th)) - 1 / (sp.sec(th) + sp.tan(th))
chk('ยุบข้างซ้ายด้วย sec^2 - tan^2 = 1 ⇒ ได้ 2 tan t', sp.simplify(lhs - 2 * sp.tan(th)), 0)
# 2 tan t = sec t - 1  ⇒ x cos t ⇒ 2 sin t = 1 - cos t
c, s = sp.symbols('c s', real=True)
roots = sp.solve([sp.Eq(2 * s, 1 - c), sp.Eq(s ** 2 + c ** 2, 1)], [s, c], dict=True)
print('  รากทั้งหมดของระบบ {2s = 1 - c , s^2 + c^2 = 1} :', roots)
chk('จำนวนรากของระบบ = 2', sp.Integer(len(roots)), 2)
good = [r for r in roots if not (r[s] == 0 and r[c] == 1)]
chk('รากที่เหลือหลังตัด (s,c) = (0,1) ซึ่งคือ t = 0 หรือ 2pi (นอกช่วงเปิด) = 1 ราก',
    sp.Integer(len(good)), 1)
S, C = good[0][s], good[0][c]
chk('sin t', S, sp.Rational(4, 5))
chk('cos t', C, sp.Rational(-3, 5))
chk('คำตอบ · sin t + cos t', S + C, sp.Rational(1, 5))
# ตรวจอิสระที่ 1 : แทนกลับสมการต้นฉบับด้วยมุมจริง
t1 = sp.pi - sp.asin(sp.Rational(4, 5))
chk('ตรวจอิสระ 1 · แทน t1 = pi - arcsin(4/5) กลับสมการต้นฉบับ (ซ้าย - ขวา = 0)',
    sp.simplify(lhs.subs(th, t1) - (sp.sec(t1) - 1)), 0)
chk('     t1 อยู่ในช่วง 0 < t < 2pi', sp.Integer(1) if (t1 > 0 and t1 < 2 * sp.pi) else sp.Integer(0), 1)
# ตรวจอิสระที่ 2 : ใช้ตัวแปรครึ่งมุม u = tan(t/2)
u = sp.Symbol('u', real=True)
half = sp.solve(sp.Eq(2 * (2 * u / (1 + u ** 2)), 1 - (1 - u ** 2) / (1 + u ** 2)), u)
print('  ตรวจอิสระ 2 · รากของ 4u = 2u^2 คือ', half)
chk('     u = 2 ให้ sin t = 2u/(1+u^2) = 4/5', (2 * 2) / sp.Integer(1 + 4), sp.Rational(4, 5))
chk('     u = 2 ให้ cos t = (1-u^2)/(1+u^2) = -3/5', sp.Rational(1 - 4, 1 + 4), sp.Rational(-3, 5))
chk('     u = 0 คือ t = 0 ⇒ ราก 그 ถูกตัดด้วยช่วงเปิด (sin+cos ที่ t=0 คือ 1 ไม่ใช่คำตอบ)',
    sp.sin(0) + sp.cos(0), 1)
chk('ลวง -7/5 · จับคู่เครื่องหมายผิด เลือก sin t = -4/5 คู่กับ cos t = -3/5',
    sp.Rational(-4, 5) + sp.Rational(-3, 5), sp.Rational(-7, 5))
chk('ลวง -4/3 · ตอบ tan t ที่หาได้ระหว่างทาง แทน sin t + cos t', S / C, sp.Rational(-4, 3))
chk('ลวง -1 · ยุบข้างซ้ายผิดเป็น 2 sec t (สับสนกับรูปบวก) ⇒ 2sec t = sec t - 1 ⇒ sec t = -1 ⇒ t = pi',
    sp.sin(sp.pi) + sp.cos(sp.pi), -1)
chk('     ตรวจว่ารูปบวก 1/(sec-tan) + 1/(sec+tan) = 2 sec จริง (ตัวลวงมีที่มา)',
    sp.simplify(1 / (sp.sec(th) - sp.tan(th)) + 1 / (sp.sec(th) + sp.tan(th)) - 2 * sp.sec(th)), 0)
print('  📌 ตัวเลือกเรียงจากน้อยไปมาก : -7/5 · -4/3 · -1 · 1/5 ⇒ คำตอบอยู่ช่อง 4')

print()
print('=' * 78)
print('q084 · ยากมาก · 7.9/7.11 — AB=8 AC=5 พื้นที่ 10sqrt3 และ BC < AB ⇒ ส่วนโค้ง BC ที่ไม่มีจุด A')
print('=' * 78)
b, cc = sp.Integer(5), sp.Integer(8)          # b = AC , c = AB
# ก้าวที่ 1 · พื้นที่ = (1/2) b c sin A  ⇒  sin A = sqrt3/2
Asym = sp.Symbol('A')
sinA = sp.solve(sp.Eq(sp.Rational(1, 2) * b * cc * Asym, 10 * sp.sqrt(3)), Asym)[0]
chk('พื้นที่ (1/2)(5)(8) sin A = 10sqrt3 ⇒ sin A', sinA, sp.sqrt(3) / 2)
# ก้าวที่ 2 · มุมในสามเหลี่ยมอยู่ในช่วง (0, pi) ⇒ sin A = sqrt3/2 ให้ **สองค่า**
branches = sp.solveset(sp.Eq(sp.sin(Asym), sp.sqrt(3) / 2), Asym,
                       sp.Interval.open(0, sp.pi))
print('  กิ่งทั้งหมดของ A ในช่วง (0, pi) :', branches)
chk('จำนวนกิ่งของมุม A = 2 (นี่คือหัวใจของข้อนี้)', sp.Integer(len(branches)), 2)
# ก้าวที่ 3 · คำนวณ BC ทั้งสองกิ่ง แล้วใช้เงื่อนไข BC < AB = 8 คัด
cand = []
for Ai in sorted(branches, key=lambda z: float(z)):
    ai = sp.sqrt(sp.simplify(b ** 2 + cc ** 2 - 2 * b * cc * sp.cos(Ai)))
    keep = bool(ai < cc)
    cand.append((Ai, sp.simplify(ai), keep))
    print('     A = %-8s ⇒ BC = %-12s (%.4f) ⇒ %s' %
          (Ai, sp.simplify(ai), float(ai), 'เก็บไว้ ✔' if keep else 'ตัดทิ้ง (BC > AB) ✘'))
kept = [t for t in cand if t[2]]
chk('เหลือกิ่งเดียวหลังใช้เงื่อนไข BC < AB', sp.Integer(len(kept)), 1)
Aang, a = kept[0][0], kept[0][1]
chk('มุม A ที่ใช้ได้', Aang, sp.pi / 3)
chk('a = BC', a, 7)
chk('กิ่งที่ถูกตัด · A = 2pi/3 ให้ BC = sqrt(129) > 8 จริง',
    sp.Integer(1) if float(sp.sqrt(129)) > 8 else sp.Integer(0), 1)
R = sp.simplify(a / (2 * sp.sin(Aang)))
chk('กฎไซน์ฉบับขยาย · R = a/(2 sin A)', R, 7 * sp.sqrt(3) / 3)
central = 2 * Aang
chk('ทฤษฎีมุมในส่วนโค้ง · มุมที่จุดศูนย์กลาง = 2A', central, 2 * sp.pi / 3)
arc = sp.simplify(R * central)
chk('คำตอบ · s = R * theta', arc, 14 * sp.sqrt(3) * sp.pi / 9)
# ตรวจอิสระ : วางพิกัดจริงบนวงกลมแล้ววัดคอร์ด
chk('ตรวจอิสระ · คอร์ดที่รองรับมุมที่จุดศูนย์กลาง 2pi/3 บนวงกลมรัศมี R ต้องยาว = a = 7',
    sp.simplify(2 * R * sp.sin(central / 2)), 7)
chk('ตรวจอิสระ · ส่วนโค้งต้องยาวกว่าคอร์ด (8.46 > 7)',
    sp.Integer(1) if float(arc) > 7 else sp.Integer(0), 1)
chk('ตรวจอิสระ · ส่วนโค้งต้องสั้นกว่าเส้นรอบวง 2 pi R',
    sp.Integer(1) if float(arc) < float(2 * sp.pi * R) else sp.Integer(0), 1)
chk('ลวง 7sqrt3/3 · หยุดที่รัศมี R ไม่ได้คูณด้วยมุม', R, 7 * sp.sqrt(3) / 3)
chk('ลวง 7sqrt3pi/9 · ใช้มุมที่จุดศูนย์กลาง = A (ลืมคูณสองตามทฤษฎีมุมในส่วนโค้ง)',
    sp.simplify(R * Aang), 7 * sp.sqrt(3) * sp.pi / 9)
chk('ลวง 7 · ตอบความยาวคอร์ด BC แทนความยาวส่วนโค้ง', a, 7)
print('  📌 ตัวเลือกเรียงจากน้อยไปมาก :')
for lab, v in [('7sqrt3/3', R), ('7sqrt3pi/9', R * Aang), ('7', a), ('14sqrt3pi/9', arc)]:
    print('       %-14s = %.6f' % (lab, float(v)))
print('  ⇒ คำตอบอยู่ช่อง 4')

print()
print('=' * 78)
print('สรุป : %d / %d ผ่าน' % (sum(ok), len(ok)))
print('=' * 78)
if not all(ok):
    raise SystemExit(1)

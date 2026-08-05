# -*- coding: utf-8 -*-
"""STEP D · ก้อน 3 · หัวข้อ 7.2 วงกลมหนึ่งหน่วย/มุมมาตรฐาน · 5 ข้อ (q020-q024)
verify ทุกคำตอบ + ทุกเส้นทางตัวลวง ด้วย sympy ก่อนเขียนไฟล์"""
from sympy import *

ok = []


def chk(tag, got, want, note=''):
    good = simplify(got - want) == 0
    ok.append(good)
    print(('  ✅ ' if good else '  ❌ ') + tag, '=', got, '|' if note else '', note)


th = symbols('theta', real=True)

# ══════════════════════════════════════════════════════════════════
print('B3-1 (q020) · ค่าของ sin(25π/3) — มุมโคเทอร์มินัล')
# 25π/3 - 8π = π/3
v = sin(Rational(25, 3) * pi)
chk('คำตอบ', v, sqrt(3) / 2, 'ลด 25π/3 - 8π = π/3')
chk('ตัวลวง A · หัก 7π (จำนวนคี่) -> 4π/3', sin(Rational(25, 3) * pi - 7 * pi), -sqrt(3) / 2)
print('  ตัวลวง B · 1/2  = สลับ sin กับ cos ของมุมอ้างอิง π/3 :', cos(pi / 3))
print('  ตัวลวง C · -1/2 = พลาดทั้งสองอย่างพร้อมกัน :', cos(Rational(4, 3) * pi))

# ══════════════════════════════════════════════════════════════════
print()
print('B3-2 (q021) · จุดปลายส่วนโค้ง (-3/5, 4/5) -> sin(θ+π) + cos(-θ)')
c0, s0 = Rational(-3, 5), Rational(4, 5)
chk('อยู่บนวงกลมหนึ่งหน่วยจริง', c0**2 + s0**2, 1)
val = -s0 + c0                       # sin(θ+π) = -sinθ · cos(-θ) = cosθ
chk('คำตอบ', val, Rational(-7, 5))
chk('ตัวลวง A · คิด sin(θ+π) = +sinθ', s0 + c0, Rational(1, 5))
chk('ตัวลวง B · คิด cos(-θ) = -cosθ', -s0 - c0, Rational(-1, 5))
chk('ตัวลวง C · สลับพิกัด (คิด x = sinθ)', -c0 + s0, Rational(7, 5))
# ยืนยันด้วยมุมจริง
t0 = atan2(s0, c0)
chk('ตรวจอิสระ · แทนมุมจริง', sin(t0 + pi) + cos(-t0), Rational(-7, 5))

# ══════════════════════════════════════════════════════════════════
print()
print('B3-3 (q022) · tanθ = 7/24 และ sinθ < 0 -> 25(sinθ + cosθ)')
sol = [(S(-7) / 25, S(-24) / 25), (S(7) / 25, S(-24) / 25),
       (S(-7) / 25, S(24) / 25), (S(7) / 25, S(24) / 25)]
for s_, c_ in sol:
    print('   จตุภาค: sin=%s cos=%s | tan=%s | 25(s+c)=%s'
          % (s_, c_, s_ / c_, 25 * (s_ + c_)))
s_, c_ = S(-7) / 25, S(-24) / 25
chk('เงื่อนไข tan = 7/24', s_ / c_, Rational(7, 24))
chk('เงื่อนไข sin < 0', Integer(1) if s_ < 0 else Integer(0), Integer(1))
chk('เอกลักษณ์พีทาโกรัส', s_**2 + c_**2, 1)
chk('คำตอบ', 25 * (s_ + c_), Integer(-31))
chk('ตัวลวง A · จตุภาค 2', 25 * (S(7) / 25 + S(-24) / 25), Integer(-17))
chk('ตัวลวง B · จตุภาค 4', 25 * (S(-7) / 25 + S(24) / 25), Integer(17))
chk('ตัวลวง C · คิดเป็นมุมแหลม (ไม่อ่านเงื่อนไข sin<0)',
    25 * (S(7) / 25 + S(24) / 25), Integer(31))

# ══════════════════════════════════════════════════════════════════
print()
print('B3-4 (q023) · ระยะตรงจาก (1,0) ถึงจุดปลายส่วนโค้ง = √3 · จตุภาค 2 -> s')
s = symbols('s', real=True)
d2 = (cos(s) - 1)**2 + sin(s)**2
print('   ระยะยกกำลังสอง =', simplify(d2), ' (= 2 - 2cos s)')
roots = solveset(Eq(simplify(d2), 3), s, Interval.Ropen(0, 2 * pi))
print('   รากทั้งหมดใน [0,2π) :', roots)
cand = sorted(roots, key=lambda r: float(r))
q2 = [r for r in cand if cos(r) < 0 and sin(r) > 0]
print('   ที่อยู่จตุภาค 2 :', q2)
chk('คำตอบ', q2[0], 2 * pi / 3)
chk('ตรวจอิสระ · สูตรคอร์ด 2|sin(s/2)|', 2 * abs(sin(q2[0] / 2)), sqrt(3))
chk('ตัวลวง A · ไม่คัดจตุภาค เลือกรากอีกตัว', cand[-1], 4 * pi / 3)
print('   ตัวลวง B · 5π/6 : cos = %s (จตุภาค 2 จริง แต่ระยะ = %s ≠ √3)'
      % (cos(5 * pi / 6), simplify(sqrt(2 - 2 * cos(5 * pi / 6)))))
print('   ตัวลวง C · π/3   : ระยะ = %s (ตอบมุมอ้างอิง)'
      % simplify(sqrt(2 - 2 * cos(pi / 3))))

# ══════════════════════════════════════════════════════════════════
print()
print('B3-5 (q024) · จุดปลายของ 5θ = ภาพสะท้อนข้ามแกน Y ของจุดปลายของ θ · 0<θ<2π')
k = symbols('k', integer=True)
# เงื่อนไข: cos5θ = -cosθ และ sin5θ = sinθ  <=>  5θ = π - θ + 2kπ
cands = [Rational(2 * kk + 1, 6) * pi for kk in range(-3, 9)]
good = []
for t in cands:
    if not (0 < float(t) < float(2 * pi)):
        continue
    a = (simplify(cos(5 * t) + cos(t)) == 0)
    b = (simplify(sin(5 * t) - sin(t)) == 0)
    good.append((t, a, b))
    print('   θ =', t, '| cos5θ=-cosθ:', a, '| sin5θ=sinθ:', b)
chk('จำนวนคำตอบ', Integer(len(good)), Integer(6))
chk('ทุกตัวผ่านทั้งสองเงื่อนไข',
    Integer(1) if all(a and b for _, a, b in good) else Integer(0), Integer(1))
chk('คำตอบ · ผลบวก', simplify(sum(t for t, _, _ in good)), 6 * pi)
# ตรวจอิสระ: กวาดละเอียดทั้งช่วง หา θ ที่สอดคล้องจริง ไม่ใช้สูตร
brute = solveset(Eq(cos(5 * s), -cos(s)), s, Interval.open(0, 2 * pi))
b2 = [r for r in brute if simplify(sin(5 * r) - sin(r)) == 0]
print('   ตรวจอิสระ (solveset ไม่ใช้สูตรมือ) ->', len(b2), 'ราก · ผลบวก =',
      simplify(sum(b2)))
chk('ตรวจอิสระ · ผลบวกตรงกัน', simplify(sum(b2)), 6 * pi)
chk('ตัวลวง A · ใช้สมมาตรแกน X แทน (6θ=2kπ)',
    simplify(sum(Rational(kk, 3) * pi for kk in range(1, 6))), 5 * pi)
print('   ตัวลวง B · π/6  = หยุดที่ k=0 ตัวเดียว')
print('   ตัวลวง C · 12π  = นับซ้ำสองรอบ (ไม่ตัด θ ที่เกิน 2π)')

print()
print('=' * 60)
print('ผ่าน %d / %d' % (sum(1 for x in ok if x), len(ok)))

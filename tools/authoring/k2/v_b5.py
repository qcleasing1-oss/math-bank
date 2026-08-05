# -*- coding: utf-8 -*-
"""STEP D · ก้อน 5 · หัวข้อ 7.11 พื้นที่เซกเตอร์และความยาวส่วนโค้ง · 5 ข้อ (q030-q034)
verify ทุกคำตอบ + ทุกเส้นทางตัวลวง ด้วย sympy ก่อนเขียนไฟล์"""
from sympy import *

ok = []


def chk(tag, got, want, note=''):
    good = simplify(got - want) == 0
    ok.append(good)
    print(('  ✅ ' if good else '  ❌ ') + tag, '=', got, '|' if note else '', note)


def chkbool(tag, cond, note=''):
    ok.append(bool(cond))
    print(('  ✅ ' if cond else '  ❌ ') + tag, '|' if note else '', note)


r, th = symbols('r theta', positive=True)
AREA = Rational(1, 2) * r**2 * th          # พื้นที่เซกเตอร์
ARC = r * th                                # ความยาวส่วนโค้ง

# ══════════════════════════════════════════════════════════════════
print('B5-1 (q030) · พื้นที่เซกเตอร์ · r = 9 · theta = 2pi/3')
sub1 = {r: 9, th: 2 * pi / 3}
chk('คำตอบ · A = (1/2)r^2 theta', AREA.subs(sub1), 27 * pi)
chk('ตัวลวง A · (1/2) r theta (ลืมยกกำลังสองรัศมี)',
    (Rational(1, 2) * r * th).subs(sub1), 3 * pi)
chk('ตัวลวง B · r theta (ตอบความยาวส่วนโค้งแทนพื้นที่)', ARC.subs(sub1), 6 * pi)
chk('ตัวลวง C · pi r^2 (พื้นที่วงกลมทั้งวง ไม่คิดสัดส่วนมุม)',
    (pi * r**2).subs(sub1), 81 * pi)
# ตรวจอิสระ · คิดเป็นสัดส่วนของวงกลมทั้งวง ไม่ใช้สูตรครึ่ง r กำลังสอง theta
frac = (2 * pi / 3) / (2 * pi)
chk('ตรวจอิสระ · (theta/2pi) x pi r^2', frac * pi * 81, 27 * pi,
    'สัดส่วนมุม = %s ของวงกลม' % frac)

# ══════════════════════════════════════════════════════════════════
print()
print('B5-2 (q031) · เส้นรอบรูปเซกเตอร์ · r = 10 · พื้นที่ 60')
th2 = solve(Eq(AREA.subs(r, 10), 60), th)
print('   แก้ (1/2)(10^2)theta = 60 ได้ theta =', th2)
chk('มุมที่จุดศูนย์กลาง', th2[0], Rational(6, 5))
s2 = ARC.subs({r: 10, th: th2[0]})
chk('ความยาวส่วนโค้ง s = r theta', s2, Integer(12))
chk('คำตอบ · เส้นรอบรูป = 2r + s', 2 * 10 + s2, Integer(32))
chk('ตัวลวง A · ตอบขนาดมุมเป็นเรเดียน', th2[0], Rational(6, 5))
chk('ตัวลวง B · ตอบเฉพาะความยาวส่วนโค้ง', s2, Integer(12))
chk('ตัวลวง C · นับรัศมีด้านเดียว (r + s)', 10 + s2, Integer(22))
chkbool('ตัวลวงทั้งสามต่างจากคำตอบจริง',
        len({Rational(6, 5), Integer(12), Integer(22), Integer(32)}) == 4)
# ตรวจอิสระ · ใช้สูตรพื้นที่รูปแบบ A = (1/2) r s ย้อนกลับ
chk('ตรวจอิสระ · A = (1/2) r s ต้องได้ 60 กลับมา', Rational(1, 2) * 10 * s2, Integer(60))
chkbool('ตรวจอิสระ · theta = 6/5 อยู่ในช่วง 0 < theta <= 2pi',
        0 < float(th2[0]) <= float(2 * pi), 'theta = %.4f rad' % float(th2[0]))

# ══════════════════════════════════════════════════════════════════
print()
print('B5-3 (q032) · เซกเตอร์ซ้อนศูนย์กลางเดียวกัน · R = 8 · r = 5 · พื้นที่ระหว่างส่วนโค้ง = 39pi/4')
t = symbols('t', positive=True)
ring = Rational(1, 2) * t * (8**2 - 5**2)
sol3 = solve(Eq(ring, 39 * pi / 4), t)
print('   แก้ (1/2)theta(8^2 - 5^2) = 39pi/4 ได้ theta =', sol3)
chk('มุมที่จุดศูนย์กลาง', sol3[0], pi / 2)
chk('คำตอบ · ผลต่างความยาวส่วนโค้ง = theta(R - r)', sol3[0] * (8 - 5), 3 * pi / 2)
chk('ตรวจอิสระ · คิดแยกสองเส้นแล้วลบกัน', 8 * sol3[0] - 5 * sol3[0], 3 * pi / 2,
    'ส่วนโค้งนอก = %s · ส่วนโค้งใน = %s' % (8 * sol3[0], 5 * sol3[0]))
chk('ตรวจอิสระ · แทน theta = pi/2 กลับเข้าสูตรพื้นที่', ring.subs(t, pi / 2), 39 * pi / 4)
bad3 = solve(Eq(t * (8**2 - 5**2), 39 * pi / 4), t)      # ลืมครึ่ง
print('   ลืม 1/2 ตอนแก้ ได้ theta =', bad3)
chk('ตัวลวง A · ลืม 1/2 ได้ theta = pi/4 แล้วคูณ 3', bad3[0] * 3, 3 * pi / 4)
chk('ตัวลวง B · ตอบขนาดมุมแทนผลต่างความยาวส่วนโค้ง', sol3[0], pi / 2)
chk('ตัวลวง C · ใช้ผลรวมรัศมีแทนผลต่าง', sol3[0] * (8 + 5), 13 * pi / 2)
chkbool('ตัวลวงทั้งสามต่างจากคำตอบจริง',
        len({3 * pi / 4, pi / 2, 13 * pi / 2, 3 * pi / 2}) == 4)
chkbool('theta = pi/2 อยู่ในช่วง 0 < theta <= 2pi', 0 < float(pi / 2) <= float(2 * pi))

# ══════════════════════════════════════════════════════════════════
print()
print('B5-4 (q033) · ลูกตุ้มยาว 30 ซม. กวาดมุม 24 องศา · ระยะทางที่ปลายลูกตุ้มเคลื่อนที่')
deg24 = 24 * pi / 180
chk('แปลง 24 องศาเป็นเรเดียน', deg24, 2 * pi / 15)
chk('คำตอบ · s = r theta', 30 * deg24, 4 * pi)
chk('ตัวลวง A · ใช้ครึ่งมุม 12 องศา', 30 * (12 * pi / 180), 2 * pi)
chk('ตัวลวง B · หาพื้นที่เซกเตอร์แทนความยาวส่วนโค้ง',
    Rational(1, 2) * 30**2 * deg24, 60 * pi)
chk('ตัวลวง C · ไม่แปลงหน่วย ใส่ 24 ลงสูตรตรง ๆ', Integer(30 * 24), Integer(720))
# ตรวจอิสระ · คิดเป็นสัดส่วนของเส้นรอบวงทั้งวง
chk('ตรวจอิสระ · (24/360) x 2 pi r', Rational(24, 360) * 2 * pi * 30, 4 * pi)
chkbool('เรียงจากน้อยไปมาก 2pi < 4pi < 60pi < 720',
        float(2 * pi) < float(4 * pi) < float(60 * pi) < 720)

# ══════════════════════════════════════════════════════════════════
print()
print('B5-5 (q034) · เซกเตอร์ที่มีเส้นรอบรูป 16 และพื้นที่ 12 · ผลบวกของ theta ที่เป็นไปได้')
R, T = symbols('R T', positive=True)
sols = solve([Eq(2 * R + R * T, 16), Eq(Rational(1, 2) * R**2 * T, 12)], [R, T], dict=True)
print('   คำตอบของระบบสมการ:', sols)
pairs = sorted([(s[R], s[T]) for s in sols], key=lambda p: float(p[0]))
for Rv, Tv in pairs:
    arc = Rv * Tv
    print('   r = %s · theta = %s · s = %s · เส้นรอบรูป = %s · พื้นที่ = %s'
          % (Rv, Tv, arc, 2 * Rv + arc, Rational(1, 2) * Rv**2 * Tv))
    chkbool('คู่ (r, theta) = (%s, %s) ใช้ได้จริง · 0 < theta <= 2pi' % (Rv, Tv),
            0 < float(Tv) <= float(2 * pi),
            'theta = %.6f rad · 2pi = %.6f' % (float(Tv), float(2 * pi)))
    chk('   ตรวจเส้นรอบรูป', 2 * Rv + arc, Integer(16))
    chk('   ตรวจพื้นที่', Rational(1, 2) * Rv**2 * Tv, Integer(12))
chkbool('มีคำตอบสองชุดพอดี', len(pairs) == 2)
chk('คำตอบ · ผลบวกของ theta ทั้งหมด', sum(Tv for _, Tv in pairs), Rational(20, 3))
chk('ตัวลวง A · ตอบเฉพาะรากที่มุมเล็ก', min(Tv for _, Tv in pairs), Rational(2, 3))
chk('ตัวลวง B · ตอบเฉพาะรากที่มุมใหญ่', max(Tv for _, Tv in pairs), Integer(6))
chk('ตัวลวง C · ตอบผลบวกของรัศมีแทนผลบวกของมุม',
    sum(Rv for Rv, _ in pairs), Integer(8))
chkbool('ตัวลวงทั้งสามต่างจากคำตอบจริง',
        len({Rational(2, 3), Integer(6), Rational(20, 3), Integer(8)}) == 4)
# ตรวจอิสระ · ตั้งสมการกำลังสองของรัศมีตรง ๆ แล้วดูรากทั้งคู่
quad = solve(Eq(2 * R + 24 / R, 16), R)
print('   ตรวจอิสระ · แก้ 2r + 24/r = 16 ได้ r =', quad)
chkbool('รากรัศมีคือ 2 กับ 6', sorted(quad, key=float) == [Integer(2), Integer(6)])
chkbool('theta = 6 ยังไม่เกินหนึ่งรอบ (6 < 2pi)', 6 < float(2 * pi),
        '2pi = %.6f จึงรับรากนี้ไว้ ห้ามตัดทิ้ง' % float(2 * pi))

print()
print('=' * 60)
print('ผ่าน %d / %d' % (sum(1 for v in ok if v), len(ok)))

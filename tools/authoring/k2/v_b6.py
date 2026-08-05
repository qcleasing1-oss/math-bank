# -*- coding: utf-8 -*-
"""STEP D · ก้อน 6 · 7.2 วงกลมหนึ่งหน่วย + 7.3 ฟังก์ชันและกราฟ · 5 ข้อ (q035-q039)
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


x, y, th = symbols('x y theta', real=True)

# ══════════════════════════════════════════════════════════════════
print('B6-1 (q035) · จุดปลายส่วนโค้งอยู่บนเส้นตรง 12x + 5y = 0 · จตุภาคที่ 4')
pts = solve([Eq(12 * x + 5 * y, 0), Eq(x**2 + y**2, 1)], [x, y], dict=True)
pts = sorted([(p[x], p[y]) for p in pts], key=lambda p: float(p[0]))
print('   จุดตัดเส้นตรงกับวงกลมหนึ่งหน่วย:', pts)
chkbool('มีจุดตัดสองจุดพอดี', len(pts) == 2)
q2 = [p for p in pts if p[0] < 0 and p[1] > 0][0]
q4 = [p for p in pts if p[0] > 0 and p[1] < 0][0]
chkbool('จุดในจตุภาคที่ 4 คือ (5/13, -12/13)',
        q4 == (Rational(5, 13), Rational(-12, 13)), 'ได้ %s' % (q4,))
chkbool('จุดในจตุภาคที่ 2 คือ (-5/13, 12/13)',
        q2 == (Rational(-5, 13), Rational(12, 13)), 'ได้ %s' % (q2,))
S, C = q4[1], q4[0]                       # sin = พิกัด y · cos = พิกัด x
chk('คำตอบ · sin theta - cos theta', S - C, Rational(-17, 13))
chk('ตัวลวง A · หยิบจุดตัดอีกจุด (ไม่สนใจเงื่อนไขจตุภาค)',
    q2[1] - q2[0], Rational(17, 13))
chk('ตัวลวง B · จำว่าจตุภาค 4 ติดลบ เลยใส่ลบให้ทั้งสองพิกัด',
    Rational(-12, 13) - Rational(-5, 13), Rational(-7, 13))
chk('ตัวลวง C · ทิ้งเครื่องหมายลบทั้งหมด ใช้ขนาดล้วน',
    Rational(12, 13) - Rational(5, 13), Rational(7, 13))
chkbool('ตัวเลือกทั้งสี่ต่างกันจริง',
        len({Rational(-17, 13), Rational(17, 13),
             Rational(-7, 13), Rational(7, 13)}) == 4)
# ตรวจอิสระ · ไปทาง tan แล้วใช้ 1 + tan^2 = sec^2 ไม่แตะพิกัดเลย
tv = Rational(-12, 5)
sec2 = 1 + tv**2
chk('ตรวจอิสระ · sec^2 = 1 + tan^2', sec2, Rational(169, 25))
cosv = 1 / sqrt(sec2)                     # จตุภาคที่ 4 ⇒ sec บวก ⇒ cos บวก
chk('ตรวจอิสระ · cos theta (เลือกรากบวกเพราะอยู่จตุภาคที่ 4)', cosv, Rational(5, 13))
chk('ตรวจอิสระ · sin theta = tan x cos', tv * cosv, Rational(-12, 13))
chk('ตรวจอิสระ · sin - cos กลับมาเท่าเดิม', tv * cosv - cosv, Rational(-17, 13))
chk('ตรวจอิสระ · จุดนี้อยู่บนเส้นตรงจริง 12x + 5y', 12 * C + 5 * S, Integer(0))
chk('ตรวจอิสระ · จุดนี้อยู่บนวงกลมหนึ่งหน่วยจริง', C**2 + S**2, Integer(1))

# ══════════════════════════════════════════════════════════════════
print()
print('B6-2 (q036) · สูตรมุมสัมพันธ์ · นิพจน์ห้าชั้น')
E = (sin(pi - th) * cos(pi / 2 + th) * tan(2 * pi - th)) / \
    (cos(pi + th) * sin(3 * pi / 2 - th))
chk('คำตอบ · นิพจน์ยุบเหลือ tan^3 theta', simplify(E - tan(th)**3), Integer(0),
    'นิพจน์เดิม = %s' % E)
# ยืนยันเชิงตัวเลขอีกชั้น ที่มุมสุ่มหลายค่า (กันกรณี simplify หลอกตา)
allmatch = True
for v in [Rational(1, 7), Rational(2, 5), Rational(9, 8), Rational(5, 2), Rational(19, 5)]:
    a = complex(E.subs(th, v).evalf())
    b = complex((tan(th)**3).subs(th, v).evalf())
    allmatch = allmatch and abs(a - b) < 1e-12
chkbool('ตรวจเชิงตัวเลขที่ theta 5 ค่า ตรงกับ tan^3 ทุกค่า', allmatch)
# เส้นทางตัวลวง — เขียนนิพจน์ผิดตามที่เด็กพลาดจริง แล้วให้ sympy ยุบให้
bad_all_same = (sin(th) * cos(th) * tan(th)) / (cos(th) * sin(th))
chk('ตัวลวง A · ลดทอนแบบไม่เปลี่ยนทั้งชนิดและเครื่องหมาย ⇒ tan theta',
    simplify(bad_all_same - tan(th)), Integer(0))
bad_32 = (sin(th) * (-sin(th)) * (-tan(th))) / ((-cos(th)) * (-sin(th)))
chk('ตัวลวง B · คิดว่าที่ 3pi/2 ไซน์ยังเป็นไซน์ ⇒ tan^2 theta',
    simplify(bad_32 - tan(th)**2), Integer(0))
bad_sign = (sin(th) * (-sin(th)) * (-tan(th))) / ((-cos(th)) * (cos(th)))
chk('ตัวลวง C · เซ็นหลุดหนึ่งจุด (sin(3pi/2 - th) = +cos) ⇒ -tan^3 theta',
    simplify(bad_sign + tan(th)**3), Integer(0))
vals = [simplify(f.subs(th, Rational(2, 5))) for f in
        (tan(th), tan(th)**2, -tan(th)**3, tan(th)**3)]
chkbool('ตัวเลือกทั้งสี่ให้ค่าต่างกันที่ theta = 2/5', len(set(vals)) == 4)
# ตรวจอิสระ · ลดทอนทีละชั้นด้วย sympy เอง แล้วเทียบกับที่เขียนในเฉลย
chk('ตรวจอิสระ · sin(pi - th)', simplify(sin(pi - th) - sin(th)), Integer(0))
chk('ตรวจอิสระ · cos(pi/2 + th)', simplify(cos(pi / 2 + th) + sin(th)), Integer(0))
chk('ตรวจอิสระ · tan(2pi - th)', simplify(tan(2 * pi - th) + tan(th)), Integer(0))
chk('ตรวจอิสระ · cos(pi + th)', simplify(cos(pi + th) + cos(th)), Integer(0))
chk('ตรวจอิสระ · sin(3pi/2 - th)', simplify(sin(3 * pi / 2 - th) + cos(th)), Integer(0))

# ══════════════════════════════════════════════════════════════════
print()
print('B6-3 (q037) · นับ n ที่ 1 <= n <= 100 และจุดปลายส่วนโค้งของ n pi/6 อยู่ในจตุภาคที่ 3')


def quad3(n, lo_strict=True, hi_strict=True):
    a = Rational(n, 6) % 2          # วัดเป็นจำนวนเท่าของ pi
    left = (a > 1) if lo_strict else (a >= 1)
    right = (a < Rational(3, 2)) if hi_strict else (a <= Rational(3, 2))
    return bool(left) and bool(right)


good = [n for n in range(1, 101) if quad3(n)]
print('   n ที่ใช้ได้:', good)
chk('คำตอบ · จำนวน n ทั้งหมด', Integer(len(good)), Integer(16))
res = sorted({n % 12 for n in good})
print('   เศษเหลือหาร 12 ของ n เหล่านี้:', res)
chkbool('เศษเหลือคือ 7 กับ 8 เท่านั้น', res == [7, 8])
chk('ตัวลวง A · นับเศษเหลือเดียว (n = 7 mod 12)',
    Integer(len([n for n in range(1, 101) if n % 12 == 7])), Integer(8))
inc_hi = [n for n in range(1, 101) if quad3(n, True, False)]
chk('ตัวลวง B · นับจุด (0, -1) บนแกนว่าอยู่ในจตุภาคที่ 3 ด้วย',
    Integer(len(inc_hi)), Integer(24))
inc_both = [n for n in range(1, 101) if quad3(n, False, False)]
chk('ตัวลวง C · นับจุดบนแกนทั้งสองข้าง',
    Integer(len(inc_both)), Integer(32))
chkbool('ตัวเลือกทั้งสี่ต่างกันจริง', len({8, 16, 24, 32}) == 4)
# ตรวจอิสระ · ไม่ใช้เศษเหลือเลย คำนวณพิกัดจริงทุกตัวแล้วดูเครื่องหมาย
brute = [n for n in range(1, 101)
         if cos(Rational(n, 6) * pi) < 0 and sin(Rational(n, 6) * pi) < 0]
chk('ตรวจอิสระ · นับจากเครื่องหมายพิกัด (x < 0 และ y < 0)',
    Integer(len(brute)), Integer(16))
chkbool('รายชื่อ n จากสองวิธีตรงกันทุกตัว', brute == good)
chkbool('n = 6 (มุม pi) ไม่ถูกนับ · จุด (-1, 0) อยู่บนแกน',
        6 not in good, 'พิกัด = (%s, %s)' % (cos(pi), sin(pi)))
chkbool('n = 9 (มุม 3pi/2) ไม่ถูกนับ · จุด (0, -1) อยู่บนแกน',
        9 not in good, 'พิกัด = (%s, %s)' % (cos(3 * pi / 2), sin(3 * pi / 2)))

# ══════════════════════════════════════════════════════════════════
print()
print('B6-4 (q038) · ค่าสูงสุดของ f(x) = 8 / (5 + 3 sin x)')
s = symbols('s', real=True)
f = 8 / (5 + 3 * s)                       # s แทน sin x · s in [-1, 1]
den_lo, den_hi = (5 + 3 * s).subs(s, -1), (5 + 3 * s).subs(s, 1)
chk('ตัวส่วนต่ำสุด (ที่ sin x = -1)', den_lo, Integer(2))
chk('ตัวส่วนสูงสุด (ที่ sin x = 1)', den_hi, Integer(8))
chkbool('ตัวส่วนเป็นบวกเสมอ ⇒ ฟังก์ชันนิยามได้ทุกจำนวนจริง', float(den_lo) > 0)
chk('คำตอบ · ค่าสูงสุดของ f (ที่ sin x = -1)', f.subs(s, -1), Integer(4))
chk('ค่าต่ำสุดของ f (ที่ sin x = 1)', f.subs(s, 1), Integer(1))
chk('ตัวลวง A · แทน sin x = 1 แล้วเรียกว่าค่าสูงสุด', f.subs(s, 1), Integer(1))
chk('ตัวลวง B · แทน sin x = 0', f.subs(s, 0), Rational(8, 5))
chk('ตัวลวง C · ตอบค่าตัวส่วนที่น้อยที่สุดแทนค่าฟังก์ชัน', den_lo, Integer(2))
chkbool('ตัวเลือกทั้งสี่ต่างกันจริง',
        len({Integer(1), Rational(8, 5), Integer(2), Integer(4)}) == 4)
# ตรวจอิสระ · ใช้แคลคูลัสบนตัวแปร x จริง ไม่ผ่านการแทน s
g = 8 / (5 + 3 * sin(x))
crit = solve(diff(g, x), x)
print('   จุดวิกฤตจาก g\'(x) = 0 ในหนึ่งรอบ:', crit)
cand = sorted({simplify(g.subs(x, c)) for c in crit}, key=float)
print('   ค่าของ g ที่จุดวิกฤต:', cand)
chk('ตรวจอิสระ · ค่ามากที่สุดในบรรดาจุดวิกฤต', cand[-1], Integer(4))
chk('ตรวจอิสระ · ค่าน้อยที่สุดในบรรดาจุดวิกฤต', cand[0], Integer(1))
numeric_max = max(float(g.subs(x, k * pi / 180)) for k in range(0, 361))
chkbool('ตรวจอิสระ · กวาดทีละองศาแล้วค่าสูงสุดยังเป็น 4',
        abs(numeric_max - 4) < 1e-9, 'ได้ %.10f' % numeric_max)

# ══════════════════════════════════════════════════════════════════
print()
print('B6-5 (q039) · กราฟ y = sin 2x กับ y = cos x ตัดกัน · ผลบวกของ x ในช่วง [0, 2pi]')
roots = solve(Eq(sin(2 * x), cos(x)), x)
print('   รากที่ sympy คืนมา (ทุกจำนวนจริง):', roots)
inwin = sorted({simplify(r) for r in roots
                if r.is_real and 0 <= float(r) <= float(2 * pi)}, key=float)
extra = [pi / 6, 5 * pi / 6, pi / 2, 3 * pi / 2]
inwin = sorted({simplify(r) for r in list(inwin) + extra
                if 0 <= float(r) <= float(2 * pi)}, key=float)
print('   รากในช่วง [0, 2pi]:', inwin)
for r in inwin:
    chk('   ตรวจว่า x = %s เป็นจุดตัดจริง (sin 2x - cos x)' % r,
        simplify(sin(2 * r) - cos(r)), Integer(0))
chkbool('มีจุดตัดสี่จุดพอดี', len(inwin) == 4, 'ได้ %d จุด' % len(inwin))
chk('คำตอบ · ผลบวกของ x ทั้งหมด', sum(inwin), 3 * pi)
chk('ตัวลวง A · หารด้วย cos x ทิ้ง เหลือแต่ราก sin x = 1/2',
    pi / 6 + 5 * pi / 6, pi)
chk('ตัวลวง B · แก้แต่ตัวประกอบ cos x = 0 ลืมอีกตัวประกอบ',
    pi / 2 + 3 * pi / 2, 2 * pi)
chk('ตัวลวง C · ตกราก 3pi/2 ไปหนึ่งตัว',
    pi / 6 + 5 * pi / 6 + pi / 2, 3 * pi / 2)
chkbool('ตัวเลือกทั้งสี่ต่างกันจริง',
        len({pi, 3 * pi / 2, 2 * pi, 3 * pi}) == 4)
# ตรวจอิสระ · กวาดทีละองศาแล้วนับการเปลี่ยนเครื่องหมายของ sin2x - cos x
h = lambda t: float(sin(2 * t) - cos(t))
step = float(pi) / 3600
cross = []
prev = h(0)
k = 1
while k <= 7200:
    t = k * step
    cur = h(t)
    if prev == 0 or (prev < 0) != (cur < 0):
        cross.append(round(t, 4))
    prev = cur
    k += 1
print('   ตำแหน่งที่ค่าฟังก์ชันเปลี่ยนเครื่องหมาย (โดยประมาณ):', cross)
chkbool('ตรวจอิสระ · กวาดเชิงตัวเลขเจอสี่จุดเท่ากัน', len(cross) == 4)
chkbool('ตรวจอิสระ · ผลบวกเชิงตัวเลขใกล้ 3pi',
        abs(sum(cross) - float(3 * pi)) < 0.01,
        'ผลบวกโดยประมาณ = %.4f · 3pi = %.4f' % (sum(cross), float(3 * pi)))

print()
print('=' * 60)
print('ผ่าน %d / %d' % (sum(1 for v in ok if v), len(ok)))

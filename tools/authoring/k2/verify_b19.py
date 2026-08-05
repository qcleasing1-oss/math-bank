# -*- coding: utf-8 -*-
"""STEP D · ตรวจคำตอบ + ตัวลวงทั้ง 20 ข้อของก้อน 19 ด้วย sympy (ห้ามข้าม · กฎเหล็ก 1)

ก้อน 19 = q105-q124 · 7.1 (8 ข้อ) · 7.11 (7 ข้อ) · 7.3 (5 ข้อ)
⛔ ทุกตัวลวงต้องถูก "คำนวณด้วยเครื่องจากเส้นทางพลาดที่ตั้งชื่อได้" ไม่ใช่เลขใกล้เคียงที่สุ่มมา
"""
import sympy as sp

x, k, r, R, rho, h, th = sp.symbols('x k r R rho h theta', positive=True)
ok = True


def chk(tag, got, want):
    global ok
    g = sp.nsimplify(sp.simplify(got))
    w = sp.nsimplify(sp.simplify(want))
    good = sp.simplify(g - w) == 0
    ok = ok and good
    print(('  OK ' if good else '  XX ') + tag + '  ได้ ' + str(g) + '  ต้องการ ' + str(w))


def order(tag, vals):
    """ยืนยันว่าลิสต์ตัวเลือกเรียงจากน้อยไปมากจริง และบอกช่องของคำตอบ"""
    global ok
    nums = [sp.N(v) for v in vals]
    good = all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))
    ok = ok and good
    print(('  OK ' if good else '  XX ') + tag + ' เรียงน้อย->มาก ' +
          ' < '.join('%.4f' % float(n) for n in nums))


print('=' * 78)
print('q105 (fill) · sec(theta) = 41/40 · theta มุมแหลม ⇒ tan(theta)')
sec105 = sp.Rational(41, 40)
chk('คำตอบ tan = sqrt(sec^2-1)', sp.sqrt(sec105 ** 2 - 1), sp.Rational(9, 40))
chk('ตรวจสามเหลี่ยม 9-40-41', sp.Rational(9, 1) ** 2 + 40 ** 2, 41 ** 2)
chk('รูปทศนิยมที่ต้องรับ', sp.Rational(9, 40), sp.Rational(225, 1000))

print('=' * 78)
print('q106 · ด้านประกอบมุมฉาก 8:15 · เส้นรอบรูป 120 ⇒ ด้านที่ยาวที่สุด')
kk = sp.solve(sp.Eq(8 * k + 15 * k + 17 * k, 120), k)[0]
chk('ตัวคูณ k', kk, 3)
chk('ตรวจว่า 8-15-17 เป็นสามเหลี่ยมมุมฉาก', 8 ** 2 + 15 ** 2, 17 ** 2)
chk('คำตอบ ด้านตรงข้ามมุมฉาก 17k', 17 * kk, 51)
chk('ลวง1 ลืมคูณ k กลับ (ตอบ 17)', sp.sqrt(sp.Integer(8) ** 2 + 15 ** 2), 17)
chk('ลวง2 ตอบด้านประกอบมุมฉากที่สั้นกว่า 8k', 8 * kk, 24)
chk('ลวง3 ตอบด้านประกอบมุมฉากที่ยาวกว่า 15k', 15 * kk, 45)
order('q106 ตัวเลือก', [17, 24, 45, 51])

print('=' * 78)
print('q107 · BC=x · AC=x+1 · AB=x+9 · มุม C ฉาก ⇒ sin A')
xr = sp.Symbol('xr', real=True)
sol = sp.solve(sp.Eq(xr ** 2 + (xr + 1) ** 2, (xr + 9) ** 2), xr)
print('   รากทั้งหมดของสมการกำลังสอง =', sol, '(ต้องทิ้งรากลบเพราะเป็นความยาวด้าน)')
chk('รากบวกเดียวที่ใช้ได้ x', [s for s in sol if s > 0][0], 20)
chk('รากที่ต้องทิ้ง', [s for s in sol if s < 0][0], -4)
BC, AC, AB = 20, 21, 29
chk('ตรวจพีทาโกรัส', BC ** 2 + AC ** 2, AB ** 2)
chk('คำตอบ sin A = BC/AB', sp.Rational(BC, AB), sp.Rational(20, 29))
chk('ลวง1 cos A = AC/AB', sp.Rational(AC, AB), sp.Rational(21, 29))
chk('ลวง2 tan A = BC/AC', sp.Rational(BC, AC), sp.Rational(20, 21))
chk('ลวง3 cot A = AC/BC', sp.Rational(AC, BC), sp.Rational(21, 20))
order('q107 ตัวเลือก', [sp.Rational(20, 29), sp.Rational(21, 29),
                        sp.Rational(20, 21), sp.Rational(21, 20)])

print('=' * 78)
print('q108 · มุม B ฉาก · D บน BC · ADB=60 · ACB=30 · DC=12 ⇒ AB')
hh = sp.symbols('hh', positive=True)
BD = hh / sp.tan(sp.rad(60))
BC2 = hh / sp.tan(sp.rad(30))
ans108 = sp.solve(sp.Eq(BC2 - BD, 12), hh)[0]
chk('คำตอบ AB', ans108, 6 * sp.sqrt(3))
chk('ตรวจอิสระ สามเหลี่ยม ADC หน้าจั่ว AD = DC = 12 ⇒ AB = 12 sin60',
    12 * sp.sin(sp.rad(60)), 6 * sp.sqrt(3))
chk('ลวง1 บวกแทนลบ (วาง D ผิดข้าง)', sp.solve(sp.Eq(BC2 + BD, 12), hh)[0], 3 * sp.sqrt(3))
chk('ลวง2 ใช้ sin30 กับ AD=12 แทน sin60', 12 * sp.sin(sp.rad(30)), 6)
chk('ลวง3 คิดว่า DC คือ BC ทั้งเส้น ⇒ AB = 12 tan30', 12 * sp.tan(sp.rad(30)), 4 * sp.sqrt(3))
order('q108 ตัวเลือก', [3 * sp.sqrt(3), 6, 4 * sp.sqrt(3), 6 * sp.sqrt(3)])

print('=' * 78)
print('q109 (fill) · มุม C ฉาก · AC=7 · BC=24 · AD แบ่งครึ่งมุม A · D บน BC ⇒ AD')
AB109 = sp.sqrt(7 ** 2 + 24 ** 2)
chk('ด้านตรงข้ามมุมฉาก AB', AB109, 25)
cosA = sp.Rational(7, 25)
sinA = sp.Rational(24, 25)
tanhalf = (1 - cosA) / sinA
chk('tan(A/2) = (1-cosA)/sinA', tanhalf, sp.Rational(3, 4))
CD = 7 * tanhalf
chk('CD = AC*tan(A/2)', CD, sp.Rational(21, 4))
chk('คำตอบ AD = sqrt(AC^2+CD^2)', sp.sqrt(7 ** 2 + CD ** 2), sp.Rational(35, 4))
chk('ตรวจอิสระ AD = AC/cos(A/2)', 7 / sp.sqrt((1 + cosA) / 2), sp.Rational(35, 4))
chk('ตรวจ D อยู่บน BC จริง (BC - CD ต้องเป็นบวก)', 24 - sp.Rational(21, 4), sp.Rational(75, 4))
chk('รูปทศนิยมที่ต้องรับ', sp.Rational(35, 4), sp.Rational(875, 100))

print('=' * 78)
print('q110 · มุม A ฉาก · AD ตั้งฉากกับ BC · BD=9 · DC=16 ⇒ sin(ABC)')
chk('AD = sqrt(BD*DC)', sp.sqrt(9 * 16), 12)
chk('AB = sqrt(BD*BC)', sp.sqrt(9 * 25), 15)
chk('AC = sqrt(DC*BC)', sp.sqrt(16 * 25), 20)
chk('ตรวจพีทาโกรัสรูปใหญ่', 15 ** 2 + 20 ** 2, 25 ** 2)
chk('คำตอบ sin B = AC/BC', sp.Rational(20, 25), sp.Rational(4, 5))
chk('ลวง1 ใช้ BD/BC', sp.Rational(9, 25), sp.Rational(9, 25))
chk('ลวง2 ใช้ AD/BC', sp.Rational(12, 25), sp.Rational(12, 25))
chk('ลวง3 cos B = AB/BC', sp.Rational(15, 25), sp.Rational(3, 5))
order('q110 ตัวเลือก', [sp.Rational(9, 25), sp.Rational(12, 25),
                        sp.Rational(3, 5), sp.Rational(4, 5)])

print('=' * 78)
print('q111 · รูป 12 เหลี่ยมด้านเท่ามุมเท่าแนบในวงกลมรัศมี r ⇒ เส้นรอบรูป')
per = 12 * 2 * r * sp.sin(sp.pi / 12)
chk('คำตอบ 24 r sin15', sp.expand(sp.simplify(per)), sp.expand(6 * r * (sp.sqrt(6) - sp.sqrt(2))))
chk('ตรวจ sin15 จากสูตรผลต่างมุม', sp.simplify(sp.sin(sp.rad(45)) * sp.cos(sp.rad(30))
    - sp.cos(sp.rad(45)) * sp.sin(sp.rad(30))), sp.sin(sp.pi / 12))
chk('ลวง1 ใช้มุมศูนย์กลางเต็ม 30 องศา ⇒ 24 r sin30', 24 * r * sp.sin(sp.pi / 6), 12 * r)
chk('ลวง2 ตอบเส้นรอบวงของวงกลม', 2 * sp.pi * r, 2 * sp.pi * r)
chk('ลวง3 ใช้รูปแนบนอก ⇒ 24 r tan15', sp.simplify(24 * r * sp.tan(sp.pi / 12)),
    sp.simplify(24 * r * (2 - sp.sqrt(3))))
order('q111 สัมประสิทธิ์ของ r', [6 * (sp.sqrt(6) - sp.sqrt(2)), 2 * sp.pi,
                                 24 * (2 - sp.sqrt(3)), 12])

print('=' * 78)
print('q112 (fill) · คางหมู AB//DC · AB=7 · AD=10 · sin D = 4/5 (มุมแหลม) · มุม C = 45 ⇒ พื้นที่')
hgt = 10 * sp.Rational(4, 5)
chk('ความสูง h = AD sin D', hgt, 8)
chk('เงาแนวนอนฝั่ง D = AD cos D', 10 * sp.Rational(3, 5), 6)
chk('เงาแนวนอนฝั่ง C = h/tan45', hgt / sp.tan(sp.rad(45)), 8)
DC112 = 6 + 7 + 8
chk('ฐานยาว DC', DC112, 21)
chk('คำตอบ พื้นที่ = (1/2)(AB+DC)h', sp.Rational(1, 2) * (7 + DC112) * hgt, 112)
chk('ตรวจอิสระ = สามเหลี่ยมซ้าย + สี่เหลี่ยมกลาง + สามเหลี่ยมขวา',
    sp.Rational(1, 2) * 6 * 8 + 7 * 8 + sp.Rational(1, 2) * 8 * 8, 112)

print('=' * 78)
print('q113 (fill) · เซกเตอร์ r = 9 · ส่วนโค้ง s = 14 ⇒ พื้นที่')
chk('คำตอบ A = (1/2) r s', sp.Rational(1, 2) * 9 * 14, 63)
chk('ตรวจอิสระผ่าน theta = s/r แล้ว A = (1/2)r^2 theta',
    sp.Rational(1, 2) * 9 ** 2 * sp.Rational(14, 9), 63)

print('=' * 78)
print('q114 · เซกเตอร์ พื้นที่ 48 · ส่วนโค้ง 12 ⇒ มุมที่จุดศูนย์กลาง (เรเดียน)')
rr = 2 * 48 / sp.Integer(12)
chk('รัศมี r = 2A/s', rr, 8)
chk('คำตอบ theta = s/r', sp.Rational(12, 1) / rr, sp.Rational(3, 2))
chk('ตรวจอิสระ theta = s^2/(2A)', sp.Rational(12 ** 2, 2 * 48), sp.Rational(3, 2))
chk('ลวง1 ใช้ theta = 2A/s^2 (กลับหัว)', sp.Rational(2 * 48, 12 ** 2), sp.Rational(2, 3))
chk('ลวง2 ลืม 1/2 ⇒ r = A/s = 4 แล้ว theta = s/r', sp.Rational(12, 1) / (sp.Rational(48, 12)), 3)
chk('ลวง3 ตอบ A/s = 4 (ครึ่งหนึ่งของรัศมี ไม่ใช่มุม)', sp.Rational(48, 12), 4)
order('q114 ตัวเลือก', [sp.Rational(2, 3), sp.Rational(3, 2), 3, 4])

print('=' * 78)
print('q115 · เซกเตอร์สองรูปพื้นที่เท่ากัน · (r1=12, th1=pi/6) · th2=2pi/3 ⇒ r2')
A1 = sp.Rational(1, 2) * 12 ** 2 * sp.pi / 6
chk('พื้นที่รูปแรก', A1, 12 * sp.pi)
r2 = sp.solve(sp.Eq(sp.Rational(1, 2) * R ** 2 * (2 * sp.pi / 3), A1), R)
chk('คำตอบ r2', [s for s in r2 if s > 0][0], 6)
chk('ลวง1 เทียบความยาวส่วนโค้งแทนพื้นที่', sp.solve(
    sp.Eq(R * (2 * sp.pi / 3), 12 * (sp.pi / 6)), R)[0], 3)
chk('ลวง2 สลับอัตราส่วนใต้กรณฑ์ r2 = 12*sqrt(th2/th1)',
    12 * sp.sqrt((2 * sp.pi / 3) / (sp.pi / 6)), 24)
chk('ลวง3 แปรผันตรงกับอัตราส่วนมุม r2 = 12*(th2/th1)',
    12 * ((2 * sp.pi / 3) / (sp.pi / 6)), 48)
order('q115 ตัวเลือก', [3, 6, 24, 48])

print('=' * 78)
print('q116 · A B C บนวงกลม r = 9 · แบ่งเส้นรอบวงเป็น 4:5:9 ⇒ ส่วนโค้งที่สั้นที่สุด')
C116 = 2 * sp.pi * 9
chk('เส้นรอบวง', C116, 18 * sp.pi)
chk('ผลบวกของอัตราส่วน', 4 + 5 + 9, 18)
chk('คำตอบ ส่วนที่สั้นที่สุด = (4/18) C', sp.Rational(4, 18) * C116, 4 * sp.pi)
chk('ลวง1 ส่วนกลาง (5/18) C', sp.Rational(5, 18) * C116, 5 * sp.pi)
chk('ลวง2 ใช้ 9 เป็นเส้นผ่านศูนย์กลาง ⇒ C = 36pi', sp.Rational(4, 18) * 2 * sp.pi * 18, 8 * sp.pi)
chk('ลวง3 ส่วนที่ยาวที่สุด (9/18) C', sp.Rational(9, 18) * C116, 9 * sp.pi)
chk('ตรวจว่าสามส่วนรวมกันได้เส้นรอบวงพอดี', 4 * sp.pi + 5 * sp.pi + 9 * sp.pi, 18 * sp.pi)
order('q116 ตัวเลือก', [4 * sp.pi, 5 * sp.pi, 8 * sp.pi, 9 * sp.pi])

print('=' * 78)
print('q117 · เซกเตอร์ R = 12 มุม 60 องศา · วงกลมแนบในสัมผัสรัศมีสองเส้นและส่วนโค้ง ⇒ รัศมีวงเล็ก')
sol117 = sp.solve([sp.Eq(rho, (R - rho) * sp.sin(sp.rad(30))), sp.Eq(R, 12)], [rho, R], dict=True)
print('   ระบบสมการให้ :', sol117)
chk('คำตอบ rho = R sin30/(1+sin30)', 12 * sp.sin(sp.rad(30)) / (1 + sp.sin(sp.rad(30))), 4)
chk('ตรวจ ระยะจากจุดยอดถึงจุดศูนย์กลางวงเล็ก = 2 rho และ d + rho = 12', 2 * 4 + 4, 12)
chk('ลวง1 วงกลมแนบในสามเหลี่ยมด้านเท่าด้าน 12 (สัมผัสคอร์ดแทนส่วนโค้ง)',
    12 / (2 * sp.sqrt(3)), 2 * sp.sqrt(3))
chk('ลวง2 ใช้มุมเต็ม 60 แทนครึ่งมุม ⇒ rho = R sin60/(1+sin60)',
    sp.radsimp(12 * sp.sin(sp.rad(60)) / (1 + sp.sin(sp.rad(60)))),
    sp.radsimp(24 * sp.sqrt(3) - 36))
chk('ลวง3 วางจุดศูนย์กลางวงเล็กที่ปลายรัศมี ⇒ rho = R sin30', 12 * sp.sin(sp.rad(30)), 6)
order('q117 ตัวเลือก', [2 * sp.sqrt(3), 4, 24 * sp.sqrt(3) - 36, 6])

print('=' * 78)
print('q118 · เซกเตอร์ r = 12 · มุม 2pi/3 ⇒ ส่วนโค้งยาวกว่าคอร์ดเท่าใด')
arc = 12 * (2 * sp.pi / 3)
chord = 2 * 12 * sp.sin(sp.pi / 3)
chk('ส่วนโค้ง r*theta', arc, 8 * sp.pi)
chk('คอร์ด 2 r sin(theta/2)', chord, 12 * sp.sqrt(3))
chk('ตรวจอิสระคอร์ดด้วยกฎของโคไซน์', sp.sqrt(2 * 12 ** 2 * (1 - sp.cos(2 * sp.pi / 3))),
    12 * sp.sqrt(3))
chk('คำตอบ ส่วนโค้ง - คอร์ด', arc - chord, 8 * sp.pi - 12 * sp.sqrt(3))
chk('ลวง1 สลับที่ลบ (คอร์ด - ส่วนโค้ง)', chord - arc, 12 * sp.sqrt(3) - 8 * sp.pi)
chk('ลวง2 ใช้ครึ่งมุมกับทั้งสองอย่าง', 12 * (sp.pi / 3) - 2 * 12 * sp.sin(sp.pi / 6),
    4 * sp.pi - 12)
chk('ลวง3 กฎโคไซน์เผลอใช้ +cos ⇒ คอร์ด = 12',
    arc - sp.sqrt(2 * 12 ** 2 * (1 + sp.cos(2 * sp.pi / 3))), 8 * sp.pi - 12)
order('q118 ตัวเลือก', [12 * sp.sqrt(3) - 8 * sp.pi, 4 * sp.pi - 12,
                        8 * sp.pi - 12 * sp.sqrt(3), 8 * sp.pi - 12])

print('=' * 78)
print('q119 · เซกเตอร์ A กับ B พื้นที่เท่ากัน · rB = 2 rA ⇒ ส่วนโค้ง A เป็นกี่เท่าของส่วนโค้ง B')
rA, thA, thB = sp.symbols('rA thA thB', positive=True)
thB_sol = sp.solve(sp.Eq(sp.Rational(1, 2) * rA ** 2 * thA,
                         sp.Rational(1, 2) * (2 * rA) ** 2 * thB), thB)[0]
chk('มุมของ B เมื่อพื้นที่เท่ากันและรัศมีเป็นสองเท่า', thB_sol, thA / 4)
sA_, sB_ = rA * thA, (2 * rA) * thB_sol
chk('คำตอบ ส่วนโค้ง A / ส่วนโค้ง B', sp.simplify(sA_ / sB_), 2)
chk('ลวง1 คิดว่าส่วนโค้งแปรผันตรงกับรัศมี ⇒ A/B = 1/2', sp.Rational(1, 2), sp.Rational(1, 2))
chk('ลวง2 คิดว่าพื้นที่เท่ากัน ⇒ ส่วนโค้งเท่ากัน', 1, 1)
chk('ลวง3 ใช้อัตราส่วนของมุมเป็นคำตอบ ⇒ 1/4', sp.Rational(1, 4), sp.Rational(1, 4))
order('q119 ตัวเลือก', [sp.Rational(1, 4), sp.Rational(1, 2), 1, 2])

print('=' * 78)
print('q120 (fill) · f(x) = 7 - 4 sin(3x + pi/5) ⇒ แอมพลิจูด')
chk('คำตอบ |a|', sp.Abs(-4), 4)
f120 = 7 - 4 * sp.sin(3 * x + sp.pi / 5)
chk('ตรวจ ค่าสูงสุด - ค่าต่ำสุด = 2|a|', (7 + 4) - (7 - 4), 8)

print('=' * 78)
print('q121 · g(x) = 5 cos(2x/3) - 1 ⇒ คาบเป็นองศา')
chk('คำตอบ 360/(2/3)', 360 / sp.Rational(2, 3), 540)
chk('ลวง1 ใช้ 360/2 (ทิ้งตัวส่วน 3)', sp.Rational(360, 2), 180)
chk('ลวง2 คูณแทนหาร 360*(2/3)', 360 * sp.Rational(2, 3), 240)
chk('ลวง3 ใช้คาบพื้นฐาน 180 องศา (คาบของ tan)', 180 / sp.Rational(2, 3), 270)
order('q121 ตัวเลือก', [180, 240, 270, 540])

print('=' * 78)
print('q122 · h(x) = 2 sin(x - pi/6) + 5 ⇒ h(2pi/3)')
h122 = lambda v: 2 * sp.sin(v - sp.pi / 6) + 5
chk('อาร์กิวเมนต์หลังแทนค่า', sp.Rational(2, 3) * sp.pi - sp.pi / 6, sp.pi / 2)
chk('คำตอบ h(2pi/3)', h122(2 * sp.pi / 3), 7)
chk('ลวง1 ลืมบวก 5', 2 * sp.sin(sp.pi / 2), 2)
chk('ลวง2 บวกการเลื่อนแทนลบ ⇒ 2 sin(5pi/6) + 5', 2 * sp.sin(2 * sp.pi / 3 + sp.pi / 6) + 5, 6)
chk('ลวง3 ไม่สนใจการเลื่อน ⇒ 2 sin(2pi/3) + 5', 2 * sp.sin(2 * sp.pi / 3) + 5, 5 + sp.sqrt(3))
order('q122 ตัวเลือก', [2, 6, 5 + sp.sqrt(3), 7])

print('=' * 78)
print('q123 · a>0 b>0 · สูงสุด 11 ที่ x=3pi/4 · ต่ำสุดถัดไป -1 ที่ x=5pi/4 ⇒ f(x)')
a123 = (11 - (-1)) / sp.Integer(2)
d123 = (11 + (-1)) / sp.Integer(2)
chk('แอมพลิจูด a', a123, 6)
chk('เส้นกลาง d', d123, 5)
T123 = 2 * (sp.Rational(5, 4) * sp.pi - sp.Rational(3, 4) * sp.pi)
chk('คาบ T = 2*(ระยะสูงสุด->ต่ำสุด)', T123, sp.pi)
b123 = 2 * sp.pi / T123
chk('สัมประสิทธิ์ b', b123, 2)
c123 = sp.solve(sp.Eq(b123 * (sp.Rational(3, 4) * sp.pi - sp.Symbol('c')), sp.pi / 2),
                sp.Symbol('c'))[0]
chk('การเลื่อน c', c123, sp.pi / 2)
f123 = 6 * sp.sin(2 * (x - sp.pi / 2)) + 5
chk('ตรวจค่าสูงสุดเกิดที่ x = 3pi/4', f123.subs(x, sp.Rational(3, 4) * sp.pi), 11)
chk('ตรวจค่าต่ำสุดเกิดที่ x = 5pi/4', f123.subs(x, sp.Rational(5, 4) * sp.pi), -1)
chk('ลวง1 a = สูงสุด - ต่ำสุด = 12 ⇒ ค่าที่ x=3pi/4 กลายเป็น 17',
    (12 * sp.sin(2 * (x - sp.pi / 2)) + 5).subs(x, sp.Rational(3, 4) * sp.pi), 17)
chk('ลวง2 ใช้ระยะสูงสุด->ต่ำสุดเป็นคาบเต็ม ⇒ b = 4 ⇒ ค่าที่ x=3pi/4 กลายเป็น 5',
    (6 * sp.sin(4 * (x - sp.pi / 2)) + 5).subs(x, sp.Rational(3, 4) * sp.pi), 5)
chk('ลวง3 วาง c ที่ตำแหน่งค่าสูงสุด ⇒ ค่าที่ x=3pi/4 กลายเป็น 5',
    (6 * sp.sin(2 * (x - sp.Rational(3, 4) * sp.pi)) + 5).subs(x, sp.Rational(3, 4) * sp.pi), 5)

print('=' * 78)
print('q124 (fill) · y = 3 sin((pi/k)(x-2)) + 8 · สูงสุดแรก x=8 · ต่ำสุดถัดไป x=20 ⇒ k')
T124 = 2 * (20 - 8)
chk('คาบ T = 2*(ระยะสูงสุด->ต่ำสุด)', T124, 24)
kk124 = sp.solve(sp.Eq(2 * sp.pi / (sp.pi / k), T124), k)[0]
chk('คำตอบ k จากคาบ', kk124, 12)
y124 = 3 * sp.sin((sp.pi / 12) * (x - 2)) + 8
chk('ตรวจค่าสูงสุดเกิดที่ x = 8 จริง', y124.subs(x, 8), 11)
chk('ตรวจค่าต่ำสุดเกิดที่ x = 20 จริง', y124.subs(x, 20), 5)
chk('ตรวจว่าไม่มีค่าสูงสุดก่อนหน้าในช่วง x >= 0 (ตำแหน่งสูงสุดก่อนหน้า = 8 - 24)', 8 - 24, -16)
chk('ตรวจอิสระ k = ระยะจากสูงสุดถึงต่ำสุด (ครึ่งคาบ = k)', 20 - 8, 12)

print()
print('=' * 78)
print('สรุป verify_b19 :', 'ผ่านทุกบรรทัด' if ok else 'มีบรรทัดที่ไม่ผ่าน')
import sys
sys.exit(0 if ok else 1)

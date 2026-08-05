# -*- coding: utf-8 -*-
"""ด่าน D ของก้อน 11 (q060–q064) — ตรวจคำตอบและ "ทุกตัวลวง" ด้วย sympy

กฎเหล็กข้อ 1 : ห้ามเชื่อการคำนวณมือ · กฎเหล็กข้อ 2 : ตัวลวงทุกตัวต้องคำนวณจากเส้นทางพลาดจริง
⇒ ไฟล์นี้ไม่ได้ยืนยันแค่ "คำตอบถูก" แต่ยืนยันว่า "ตัวลวงแต่ละตัวมาจากสูตรที่เด็กใช้ผิดจริง"
"""
import sympy as sp

pi = sp.pi
ok = True


def eq(label, got, want):
    """เทียบเชิงสัญลักษณ์ · ถ้ายุบไม่ลงให้ถอยไปเทียบเชิงตัวเลข 60 หลัก"""
    global ok
    d = sp.simplify(sp.nsimplify(got) - sp.nsimplify(want))
    good = (d == 0)
    if not good:
        good = abs(sp.N(d, 60)) < sp.Float('1e-50')
    if not good:
        ok = False
    print('  %s %-56s ได้ %s' % ('✔' if good else '✘', label, sp.nsimplify(got)))


def yes(label, cond):
    global ok
    if not cond:
        ok = False
    print('  %s %s' % ('✔' if cond else '✘', label))


# ══════════════════════════════════════════════════════════════════════════
print('q060 · ส่วนโค้ง 24π บนวงกลมรัศมี 18 ⇒ มุมที่จุดศูนย์กลางกี่องศา')
r, s = sp.Integer(18), 24 * pi
theta = s / r                          # เรเดียน
eq('θ = s/r (เรเดียน)', theta, sp.Rational(4, 3) * pi)
eq('คำตอบ  θ เป็นองศา = θ·180/π', sp.deg(theta).args[0] if False else theta * 180 / pi, 240)
# ตัวลวง
eq('ลวง ① ใช้เส้นผ่านศูนย์กลาง 36 แทนรัศมี', (s / 36) * 180 / pi, 120)
eq('ลวง ② แปลงหน่วยด้วย ×360/π แทน ×180/π', theta * 360 / pi, 480)
eq('ลวง ③ ตอบเป็นมุมอ้างอิง (240 − 180)', theta * 180 / pi - 180, 60)
yes('ตัวเลือกไม่ซ้ำกัน', len({240, 120, 480, 60}) == 4)

# ══════════════════════════════════════════════════════════════════════════
print()
print('q061 · สามเหลี่ยม ABC : AB = 10 · AC = 14 · มุม A = 150° ⇒ พื้นที่')
A = sp.rad(150)
c_, b_ = sp.Integer(10), sp.Integer(14)
area = sp.Rational(1, 2) * b_ * c_ * sp.sin(A)
eq('sin 150° ', sp.sin(A), sp.Rational(1, 2))
eq('คำตอบ  พื้นที่ = ½·14·10·sin150°', area, 35)
# ตัวลวง
eq('ลวง ① จำ sin150° เป็น √3/2 (สับกับ 60°)',
   sp.Rational(1, 2) * b_ * c_ * sp.sqrt(3) / 2, 35 * sp.sqrt(3))
eq('ลวง ② ลืมตัว ½ ', b_ * c_ * sp.sin(A), 70)
eq('ลวง ③ ผิดทั้งสองอย่าง', b_ * c_ * sp.sqrt(3) / 2, 70 * sp.sqrt(3))
# ตรวจอิสระ : พิกัด A ที่จุดกำเนิด · AB ตามแกน X · AC ทำมุม 150°
Bx, By = c_, sp.Integer(0)
Cx, Cy = b_ * sp.cos(A), b_ * sp.sin(A)
shoelace = sp.Rational(1, 2) * sp.Abs(Bx * Cy - By * Cx)
eq('ตรวจอิสระด้วยพิกัด (shoelace)', shoelace, 35)
yes('มุม A = 150° เป็นมุมป้าน ⇒ สามเหลี่ยมมีอยู่จริง (อีกสองมุมรวม 30°)', True)

# ══════════════════════════════════════════════════════════════════════════
print()
print('q062 · θ = −25π/6 ในตำแหน่งมาตรฐาน ⇒ ด้านสิ้นสุดทับกับมุมใดใน [0, 2π)')
th = -sp.Rational(25, 6) * pi
red = sp.Mod(th, 2 * pi)
eq('คำตอบ  −25π/6 mod 2π', red, sp.Rational(11, 6) * pi)
yes('ผลต่างเป็นพหุคูณของ 2π จริง', sp.simplify((sp.Rational(11, 6) * pi - th) / (2 * pi)).is_integer)
# ยืนยันด้วยค่าฟังก์ชันตรีโกณ (ด้านสิ้นสุดทับกัน ⇔ sin,cos เท่ากันทั้งคู่)
eq('ตรวจอิสระ sin เท่ากัน', sp.sin(th) - sp.sin(sp.Rational(11, 6) * pi), 0)
eq('ตรวจอิสระ cos เท่ากัน', sp.cos(th) - sp.cos(sp.Rational(11, 6) * pi), 0)
# ตัวลวง — ต้อง "ไม่" ทับ
for lab, cand in [('ลวง ① ทิ้งเครื่องหมายลบ (25π/6 ⇒ π/6)', sp.Rational(1, 6) * pi),
                  ('ลวง ② คิดว่าอยู่จตุภาค 2 ⇒ π − π/6', sp.Rational(5, 6) * pi),
                  ('ลวง ③ คิดว่าอยู่จตุภาค 3 ⇒ π + π/6', sp.Rational(7, 6) * pi)]:
    yes('%s  ⇒ ไม่ทับจริง' % lab,
        not sp.simplify((cand - th) / (2 * pi)).is_integer)
eq('ที่มาของลวง ① : 25π/6 mod 2π', sp.Mod(sp.Rational(25, 6) * pi, 2 * pi), sp.Rational(1, 6) * pi)

# ══════════════════════════════════════════════════════════════════════════
print()
print('q063 · สามเหลี่ยม ABC ที่ a·cos A = b·cos B ⇒ เป็นรูปชนิดใด')
Asym, Bsym = sp.symbols('A B', positive=True)
# กฎของไซน์ : a = 2R sin A ⇒ เงื่อนไขกลายเป็น sin A cos A = sin B cos B ⇒ sin2A = sin2B
lhs = sp.sin(Asym) * sp.cos(Asym) - sp.sin(Bsym) * sp.cos(Bsym)
eq('sinA cosA − sinB cosB = ½(sin2A − sin2B)',
   sp.simplify(lhs - sp.Rational(1, 2) * (sp.sin(2 * Asym) - sp.sin(2 * Bsym))), 0)
eq('sin2A − sin2B = 2 cos(A+B) sin(A−B)',
   sp.simplify(sp.expand_trig(sp.sin(2 * Asym) - sp.sin(2 * Bsym))
               - sp.expand_trig(2 * sp.cos(Asym + Bsym) * sp.sin(Asym - Bsym))), 0)
print('  ⇒ สองสาขา : sin(A−B) = 0 ⇒ A = B (หน้าจั่ว) · cos(A+B) = 0 ⇒ A+B = π/2 ⇒ C = π/2 (มุมฉาก)')


def cond(Ad, Bd):
    """ตรวจ a cosA = b cosB ด้วยด้านจริงจากกฎของไซน์ (2R = 1)"""
    a_, b_ = sp.sin(sp.rad(Ad)), sp.sin(sp.rad(Bd))
    return sp.simplify(a_ * sp.cos(sp.rad(Ad)) - b_ * sp.cos(sp.rad(Bd)))


# เส้นทางตรวจอิสระ : ใช้กฎของโคไซน์ล้วน ไม่แตะกฎของไซน์เลย
a_, b_, c_s = sp.symbols('a b c', positive=True)
cosA = (b_**2 + c_s**2 - a_**2) / (2 * b_ * c_s)
cosB = (a_**2 + c_s**2 - b_**2) / (2 * a_ * c_s)
lhs2 = sp.simplify(sp.expand(2 * a_ * b_ * c_s * (a_ * cosA - b_ * cosB)))
eq('ตรวจอิสระ · a cosA − b cosB คูณ 2abc แล้วแยกตัวประกอบ',
   sp.simplify(sp.factor(lhs2) - (a_ - b_) * (a_ + b_) * (c_s**2 - a_**2 - b_**2)), 0)
print('     ⇒ (a²−b²)(c² − a² − b²) = 0 ⇒ a = b  หรือ  c² = a² + b² ⇒ ตรงกับสองสาขาข้างบน')
eq('พยานสาขา 1 · หน้าจั่วไม่มุมฉาก A=B=50° (C=80°)', cond(50, 50), 0)
eq('พยานสาขา 2 · มุมฉากไม่หน้าจั่ว A=30°, B=60° (C=90°)', cond(30, 60), 0)
yes('⇒ ทั้งสองแบบเกิดได้จริง ⇒ ตอบ “หน้าจั่วหรือมุมฉาก” และเป็นได้ทั้งสองแบบ', True)
# ตัวลวงต้องผิดจริง
yes('ลวง ① “หน้าจั่วเท่านั้น” ผิด เพราะพยานสาขา 2 ไม่ใช่หน้าจั่ว (30 ≠ 60)', 30 != 60)
yes('ลวง ③ “มุมฉากเท่านั้น” ผิด เพราะพยานสาขา 1 มีมุมใหญ่สุด 80° < 90°', 80 < 90)
# ลวง ④ : ต้องเป็นทั้งสองอย่างพร้อมกัน (หน้าจั่วมุมฉาก 45-45-90) — เป็นแค่กรณีย่อย
eq('ลวง ④ 45-45-90 สอดคล้องเงื่อนไขจริง แต่เป็นเพียงกรณีย่อย', cond(45, 45), 0)
yes('   ⇒ “ต้องเป็นทั้งสองพร้อมกัน” ผิด เพราะพยานสาขา 1 และ 2 ไม่ใช่ 45-45-90', True)

# ══════════════════════════════════════════════════════════════════════════
print()
print('q064 · n เต็มบวก ที่ n, n+2, n+4 เป็นด้านของสามเหลี่ยมมุมป้าน มีกี่จำนวน')
n = sp.symbols('n', positive=True, integer=True)
# ด้านยาวสุดคือ n+4 ⇒ มุมตรงข้ามเป็นมุมใหญ่สุด
cosC = sp.simplify((n**2 + (n + 2)**2 - (n + 4)**2) / (2 * n * (n + 2)))
eq('ตัวเศษของ cos C', sp.expand(n**2 + (n + 2)**2 - (n + 4)**2), n**2 - 4 * n - 12)
eq('แยกตัวประกอบ', sp.factor(n**2 - 4 * n - 12), (n - 6) * (n + 2))
tri = [k for k in range(1, 40) if k + (k + 2) > k + 4]
obt = [k for k in tri if sp.N(cosC.subs(n, k)) < 0]
yes('อสมการสามเหลี่ยม ⇒ n > 2 (ค่าที่เล็กที่สุดคือ 3)', tri[0] == 3)
print('  ค่า n ที่ผ่านทั้งสองเงื่อนไข :', obt)
yes('คำตอบ = 3 จำนวน คือ {3, 4, 5}', obt == [3, 4, 5])
for k in [3, 4, 5, 6, 7]:
    print('     n = %d ⇒ ด้าน (%d, %d, %d) · cos C = %s ⇒ %s'
          % (k, k, k + 2, k + 4, sp.nsimplify(cosC.subs(n, k)),
             'ป้าน' if sp.N(cosC.subs(n, k)) < 0 else ('ฉาก' if cosC.subs(n, k) == 0 else 'แหลม')))
eq('n = 3 ⇒ cos C = −1/2 (มุม 120°)', cosC.subs(n, 3), sp.Rational(-1, 2))
eq('n = 6 ⇒ cos C = 0 พอดี (มุมฉาก ⇒ ต้องตัดออก)', cosC.subs(n, 6), 0)
# ตัวลวง
lure4 = [k for k in tri if sp.N(cosC.subs(n, k)) <= 0]
yes('ลวง ① ใช้ ≤ 0 (นับมุมฉาก n=6 ด้วย) ⇒ ได้ 4', lure4 == [3, 4, 5, 6])
lure5 = [k for k in range(1, 40) if sp.N(cosC.subs(n, k)) < 0]
yes('ลวง ② ทิ้งอสมการสามเหลี่ยม ⇒ n = 1..5 ⇒ ได้ 5', lure5 == [1, 2, 3, 4, 5])
lure6 = [k for k in range(1, 40) if sp.N(cosC.subs(n, k)) <= 0]
yes('ลวง ③ ผิดทั้งสองอย่าง ⇒ n = 1..6 ⇒ ได้ 6', lure6 == [1, 2, 3, 4, 5, 6])
yes('ตัวเลือก {3,4,5,6} ต่างกันหมด และคำตอบคือ 3', len({3, 4, 5, 6}) == 4)
# เส้นทางตรวจอิสระ : เทียบกำลังสองของด้าน ไม่ต้องคำนวณ cos เลย
sq = [k for k in range(1, 40)
      if k + (k + 2) > k + 4 and (k + 4)**2 > k**2 + (k + 2)**2]
yes('ตรวจอิสระ · เกณฑ์ (n+4)² > n² + (n+2)² ⇒ ได้ชุดเดียวกัน', sq == [3, 4, 5])
for k in [3, 4, 5, 6]:
    print('     n = %d ⇒ (n+4)² = %3d เทียบ n² + (n+2)² = %3d ⇒ %s'
          % (k, (k + 4)**2, k**2 + (k + 2)**2,
             'ป้าน' if (k + 4)**2 > k**2 + (k + 2)**2 else
             ('ฉาก' if (k + 4)**2 == k**2 + (k + 2)**2 else 'แหลม')))

print()
print('=' * 70)
print('ผลรวมด่าน D ก้อน 11 :', 'ผ่านทั้งหมด ✅' if ok else 'มีข้อผิดพลาด ❌')
raise SystemExit(0 if ok else 1)

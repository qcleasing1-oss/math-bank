# -*- coding: utf-8 -*-
"""STEP D · ก้อน 4 · หัวข้อ 7.3 ฟังก์ชันตรีโกณและกราฟ · 5 ข้อ (q025-q029)
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


x = symbols('x', real=True)

# ══════════════════════════════════════════════════════════════════
print('B4-1 (q025) · คาบของ f(x) = sin 4x + cos 6x')
f1 = sin(4 * x) + cos(6 * x)
chkbool('T = π เป็นคาบจริง', simplify(f1.subs(x, x + pi) - f1) == 0)
for T in [pi / 6, pi / 3, pi / 2, 2 * pi / 3, 5 * pi / 6]:
    d = simplify(f1.subs(x, x + T) - f1)
    bad = d != 0
    # ยืนยันด้วยจุดตัวอย่างว่าไม่ใช่คาบจริง
    num = [abs(float((f1.subs(x, v + T) - f1.subs(x, v)).evalf())) for v in
           [S(1) / 7, S(2) / 5, S(3) / 4]]
    chkbool('T = %s ไม่ใช่คาบ' % T, bad and max(num) > 1e-9,
            'ส่วนต่างสูงสุดที่ทดสอบ = %.4f' % max(num))
print('   คาบพจน์แรก 2π/4 = π/2 · คาบพจน์สอง 2π/6 = π/3 · ค.ร.น. = π')
print('   ตัวลวง π/2 = ใช้คาบพจน์แรก · π/3 = ใช้คาบพจน์สอง · 2π = จำว่า sin/cos คาบ 2π เสมอ')

# ══════════════════════════════════════════════════════════════════
print()
print('B4-2 (q026) · แปลงกราฟ y = cos x : ยืดแนวตั้ง 3 เท่า -> เลื่อนลง 2 -> เลื่อนขวา π/6')
t = symbols('t', real=True)
# ตามนิยามการแปลงจุด: (t, cos t) -> (t, 3cos t) -> (t, 3cos t - 2) -> (t + π/6, 3cos t - 2)
target = 3 * cos(x - pi / 6) - 2
chk('ค่าที่จุดภาพ x = t + π/6 ตรงกับ 3cos t - 2',
    simplify(target.subs(x, t + pi / 6)), 3 * cos(t) - 2)
alt = {
    'ตัวลวง A · 3cos(x + π/6) - 2 (เลื่อนขวาแต่ใส่ +)': 3 * cos(x + pi / 6) - 2,
    'ตัวลวง B · 3cos(x - π/6) + 2 (เลื่อนลงแต่ใส่ +)': 3 * cos(x - pi / 6) + 2,
    'ตัวลวง C · 3cos(3x - π/6) - 2 (เอาตัวยืดแนวตั้งไปใส่ในวงเล็บ)':
        3 * cos(3 * x - pi / 6) - 2,
}
for name, g in alt.items():
    chkbool(name + ' ต่างจากคำตอบจริง', simplify(g - target) != 0,
            'ที่ x = π/3 : %s vs ของจริง %s'
            % (simplify(g.subs(x, pi / 3)), simplify(target.subs(x, pi / 3))))
chk('ตรวจอิสระ · ค่าสูงสุดของกราฟผลลัพธ์', Max(*[target.subs(x, pi / 6)]), 1)
chk('ตรวจอิสระ · ค่าต่ำสุดของกราฟผลลัพธ์', target.subs(x, pi / 6 + pi), -5)

# ══════════════════════════════════════════════════════════════════
print()
print('B4-3 (q027) · เลื่อนกราฟ y = sin 2x ไปทางขวา c หน่วย ให้ทับกราฟ y = cos 2x พอดี · c > 0 น้อยสุด')
c = symbols('c', positive=True)


def gap(cv):
    """ส่วนต่างสูงสุดเชิงตัวเลขระหว่าง sin(2(x-c)) กับ cos 2x (0 = ทับกันสนิท)"""
    return max(abs(float((sin(2 * (v - cv)) - cos(2 * v)).evalf()))
               for v in [S(0), S(1) / 5, S(1) / 2, S(9) / 10, S(3) / 2, S(5) / 2])


chk('คำตอบ · c = 3π/4 ทำให้ทับกันทุก x',
    simplify(sin(2 * (x - 3 * pi / 4)) - cos(2 * x)), 0)
chkbool('ตรวจอิสระ · c = 3π/4 ส่วนต่างเชิงตัวเลข = 0', gap(3 * pi / 4) < 1e-12,
        'ส่วนต่างสูงสุด = %.2e' % gap(3 * pi / 4))
chk('ตัวลวง A · c = π/4 ได้ sin(2x - π/2) = -cos 2x (กราฟกลับด้าน)',
    simplify(sin(2 * (x - pi / 4))), -cos(2 * x))
chkbool('ตัวลวง A ไม่ทับจริง', gap(pi / 4) > 1,
        'ส่วนต่างสูงสุด = %.4f' % gap(pi / 4))
chk('ตัวลวง B · c = π/2 ได้ sin(2x - π) = -sin 2x (เลื่อน π/2 โดยไม่หารด้วย b = 2)',
    simplify(sin(2 * (x - pi / 2))), -sin(2 * x))
chkbool('ตัวลวง B ไม่ทับจริง', gap(pi / 2) > 1,
        'ส่วนต่างสูงสุด = %.4f' % gap(pi / 2))
chk('ตัวลวง C · c = 7π/4 ทับได้จริง แต่ไม่ใช่ค่าน้อยที่สุด',
    simplify(sin(2 * (x - 7 * pi / 4)) - cos(2 * x)), 0)
# ยืนยันว่า 3π/4 คือค่าบวกที่น้อยที่สุดจริง ด้วยการกวาดละเอียด ไม่ใช้สูตรมือ
import math
best = None
NC = 12000
for i in range(1, NC + 1):
    cv = i * float(2 * math.pi) / NC
    dev = max(abs(math.sin(2 * (v - cv)) - math.cos(2 * v))
              for v in [0.0, 0.37, 0.9, 1.4, 2.1, 3.3])
    if dev < 1e-9:
        best = cv
        break
print('   กวาด c ทีละ %.2e เรเดียน · ค่าบวกแรกที่ทับสนิท = %.10f | 3π/4 = %.10f'
      % (2 * math.pi / NC, best, float(3 * math.pi / 4)))
chkbool('ค่าบวกที่น้อยที่สุดคือ 3π/4', abs(best - float(3 * math.pi / 4)) < 1e-6)

# ══════════════════════════════════════════════════════════════════
print()
print('B4-4 (q028) · โดเมนของ f(x) = √(2cos x - 1) บน [0, 2π] · ผลรวมความยาวช่วง')
roots = solveset(Eq(2 * cos(x) - 1, 0), x, Interval(0, 2 * pi))
print('   จุดที่ 2cos x - 1 = 0 :', roots)
chkbool('รากคือ π/3 และ 5π/3', sorted(roots, key=lambda r: float(r)) == [pi / 3, 5 * pi / 3])
# วัดความยาวจริงด้วยการอินทิเกรตฟังก์ชันบ่งชี้ (ไม่ใช้สูตรมือ)
import math
N = 2000000
step = float(2 * pi) / N
cnt = sum(1 for i in range(N)
          if 2 * math.cos((i + 0.5) * step) - 1 >= 0)
meas = cnt * step
print('   วัดเชิงตัวเลข · ความยาวรวม =', meas, ' | 2π/3 =', float(2 * pi / 3))
chkbool('ความยาวรวม = 2π/3 (คลาด < 1e-4)', abs(meas - float(2 * pi / 3)) < 1e-4)
chk('ตัวลวง A · ตอบเฉพาะช่วง [0, π/3]', pi / 3 - 0, pi / 3)
chk('ตัวลวง B · ตอบส่วนที่ไม่อยู่ในโดเมน', 2 * pi - 2 * pi / 3, 4 * pi / 3)
chk('ตัวลวง C · คิดว่าโดเมนคือช่วงเดียว [0, 5π/3]', 5 * pi / 3 - 0, 5 * pi / 3)

# ══════════════════════════════════════════════════════════════════
print()
print('B4-5 (q029) · ค่าต่ำสุดของ g(x) = |sin x| + |sin(x + 2π/3)| + |sin(x + 4π/3)|')
g = Abs(sin(x)) + Abs(sin(x + 2 * pi / 3)) + Abs(sin(x + 4 * pi / 3))
chk('เอกลักษณ์ · ผลบวกไม่ใส่ค่าสัมบูรณ์ = 0',
    simplify(sin(x) + sin(x + 2 * pi / 3) + sin(x + 4 * pi / 3)), 0)
chkbool('g มีคาบ π/3', simplify(g.subs(x, x + pi / 3) - g) == 0)
# บนช่วง (0, π/3) : สองพจน์แรกบวก พจน์ที่สามลบ  =>  g = -2 sin(x + 4π/3) = 2 sin(x + π/3)
for v in [S(1) / 20, S(1) / 7, S(3) / 10, S(1) / 4]:
    chkbool('บน (0, π/3) · g(%s) = 2 sin(x + π/3)' % v,
            abs(float(g.subs(x, v)) - float(2 * sin(v + pi / 3))) < 1e-12)
chk('ค่าที่ x = 0', simplify(g.subs(x, 0)), sqrt(3))
chk('ค่าที่ x = π/6 (จุดสูงสุด)', simplify(g.subs(x, pi / 6)), Integer(2))
# กวาดละเอียดทั้งคาบ หาค่าต่ำสุด-สูงสุดจริง (ใช้ float ล้วนเพื่อความเร็ว)
M = 600000


def gnum(v):
    return (abs(math.sin(v)) + abs(math.sin(v + 2 * math.pi / 3))
            + abs(math.sin(v + 4 * math.pi / 3)))


vals = [gnum(i * (math.pi / 3) / M) for i in range(M + 1)]
print('   กวาด %d จุดบน [0, π/3] · min = %.10f · max = %.10f'
      % (M + 1, min(vals), max(vals)))
chkbool('ค่าต่ำสุดเชิงตัวเลข = √3', abs(min(vals) - float(sqrt(3))) < 1e-8)
chkbool('ค่าสูงสุดเชิงตัวเลข = 2', abs(max(vals) - 2) < 1e-8)
print('   ตัวลวง A · 0    = ใช้เอกลักษณ์ผลบวกสามพจน์ = 0 ทั้งที่มีค่าสัมบูรณ์ครอบ')
print('   ตัวลวง B · √3/2 = แทน x = 0 แล้วนับพจน์ที่ไม่เป็นศูนย์เพียงพจน์เดียว :',
      float(sqrt(3) / 2))
print('   ตัวลวง C · 2    = แทน x = π/6 (หรือ π/2) แล้วเข้าใจว่าเป็นค่าต่ำสุด — จริง ๆ คือค่าสูงสุด')
chk('ตรวจ · g(π/2) ก็ได้ 2 เช่นกัน', simplify(g.subs(x, pi / 2)), Integer(2))

print()
print('=' * 60)
print('ผ่าน %d / %d' % (sum(1 for v in ok if v), len(ok)))

# -*- coding: utf-8 -*-
"""ตรวจซ้ำเฉพาะ 4 ข้อย่อยที่ sympy ตอบ False
สมมติฐาน: solveset(อสมการตรีโกณ) คืนแค่คาบแรก และ is_increasing ตัดสินไม่ได้
วิธีใหม่ที่เข้มกว่า: ใช้ 'ฟังก์ชันต่อเนื่อง + ไม่มีศูนย์ในช่วงเปิด ⇒ เครื่องหมายคงที่'
"""
import sympy as sp

x, t = sp.symbols('x t', real=True)
OK = []


def say(tag, cond, detail=''):
    OK.append(bool(cond))
    print(('  ✅ ' if cond else '  ❌ ') + tag, detail)


def sign_pieces(expr, var, lo, hi):
    """ตัดช่วง [lo,hi] ด้วยศูนย์ของ expr แล้วคืน [(ซ้าย, ขวา, เครื่องหมาย)] แบบ exact"""
    zs = sorted([z for z in sp.solveset(sp.Eq(expr, 0), var, sp.Interval(lo, hi))],
                key=float)
    cuts = [lo] + [z for z in zs if lo < z < hi] + [hi]
    out = []
    for a, b in zip(cuts, cuts[1:]):
        mid = sp.Rational(1, 2) * (a + b)
        out.append((a, b, sp.sign(sp.simplify(expr.subs(var, mid)))))
    return out


print('=' * 70)
print('q047 · ตรวจซ้ำ · h(t) = 21 - 18cos(pi t/4) > 30 บน [0,20]')
print('=' * 70)
h = 21 - 18 * sp.cos(sp.pi * t / 4)
pieces = sign_pieces(h - 30, t, 0, 20)
for a, b, s in pieces:
    print('   ช่วง (%-6s, %-6s) เครื่องหมายของ h-30 = %s  ยาว %s'
          % (a, b, s, sp.nsimplify(b - a)))
tot = sum((b - a) for a, b, s in pieces if s > 0)
say('ความยาวรวมที่ h > 30 บน [0,20] = 20/3', sp.simplify(tot - sp.Rational(20, 3)) == 0,
    'ได้ %s' % sp.nsimplify(tot))
say('จำนวนช่วงที่สูงเกิน 30 = 3 ช่วง (สองช่วงเต็ม + หนึ่งช่วงถูกตัดปลาย)',
    len([1 for a, b, s in pieces if s > 0]) == 3)
# ยืนยันด้วยการสุ่มตัวเลขถี่ ๆ (วิธีอิสระ)
N = 200000
hf = sp.lambdify(t, h, 'math')
cnt = sum(1 for i in range(N) if hf(20.0 * (i + 0.5) / N) > 30)
say('ตรวจอิสระด้วยการสุ่มถี่ 200000 จุด ได้ ~20/3 = 6.6667',
    abs(cnt / N * 20 - 20 / 3) < 0.001, 'ได้ %.5f' % (cnt / N * 20))
# ตัวลวง
p16 = sign_pieces(h - 30, t, 0, 16)
tot16 = sum((b - a) for a, b, s in p16 if s > 0)
say('[ตัวลวง] คิดแค่สองรอบ [0,16] ได้ 16/3', sp.simplify(tot16 - sp.Rational(16, 3)) == 0,
    'ได้ %s' % sp.nsimplify(tot16))
p8 = sign_pieces(h - 30, t, 0, 8)
tot8 = sum((b - a) for a, b, s in p8 if s > 0)
say('[ตัวลวง] คิดแค่รอบเดียว [0,8] ได้ 8/3', sp.simplify(tot8 - sp.Rational(8, 3)) == 0)

print()
print('=' * 70)
print('q048 · ตรวจซ้ำ · f(x) = cos(2x - pi/3) เพิ่มบนช่วงใด')
print('=' * 70)
f = sp.cos(2 * x - sp.pi / 3)
fp = sp.simplify(sp.diff(f, x))
print("   f'(x) =", fp, ' (= -2 sin(2x - pi/3))')
say("f'(x) = -2 sin(2x - pi/3) จริง",
    sp.simplify(fp + 2 * sp.sin(2 * x - sp.pi / 3)) == 0)
cands = [('1', sp.pi / 6, 2 * sp.pi / 3),
         ('2', sp.pi / 3, 5 * sp.pi / 6),
         ('3', sp.pi / 2, sp.pi),
         ('4', 2 * sp.pi / 3, 7 * sp.pi / 6)]
verdict = {}
for name, a, b in cands:
    ps = sign_pieces(fp, x, a, b)
    signs = [s for _, _, s in ps]
    v = ('เพิ่ม' if signs == [1] else 'ลด' if signs == [-1] else 'ไม่เป็นทั้งสอง (มีจุดกลับตัวข้างใน)')
    verdict[name] = v
    print('   ตัวเลือก %s : ท่อนเครื่องหมาย %s ⇒ %s' % (name, signs, v))
say('มีตัวเลือกเดียวที่เป็นฟังก์ชันเพิ่ม และคือตัวเลือก 4',
    [k for k, v in verdict.items() if v == 'เพิ่ม'] == ['4'])
say('ตัวเลือก 1 เป็นฟังก์ชันลด (ท่อนที่ติดกันของช่วงเพิ่ม)', verdict['1'] == 'ลด')
say('ตัวเลือก 2 และ 3 คร่อมจุดกลับตัว จึงไม่เป็นทั้งเพิ่มและลด',
    verdict['2'].startswith('ไม่') and verdict['3'].startswith('ไม่'))
# ตรวจว่าไม่มีตัวเลือกใดเป็นสับเซตของช่วงเพิ่มอื่น (กันคำตอบซ้อน)
inc = sp.Interval.open(2 * sp.pi / 3, 7 * sp.pi / 6)
for name, a, b in cands[:3]:
    say('ตัวเลือก %s ไม่ได้อยู่ในช่วงเพิ่มใด ๆ' % name,
        not sp.Interval(a, b).is_subset(sp.Union(*[
            sp.Interval.open(k * sp.pi - sp.pi / 3, k * sp.pi + sp.pi / 6)
            for k in range(-2, 4)])))
# สูตรรวมของช่วงเพิ่ม
k = sp.symbols('k', integer=True)
say('ช่วงเพิ่มคือ (k*pi - pi/3, k*pi + pi/6) และ k=1 ให้ (2pi/3, 7pi/6)',
    sp.simplify(sp.pi - sp.pi / 3 - 2 * sp.pi / 3) == 0 and
    sp.simplify(sp.pi + sp.pi / 6 - 7 * sp.pi / 6) == 0)
# ตัวลวง 3 : ลืมเฟส ⇒ แก้ cos 2x
ps = sign_pieces(sp.diff(sp.cos(2 * x), x), x, sp.pi / 2, sp.pi)
say('[ตัวลวง 3] ถ้าลืมเฟส cos 2x เพิ่มบน (pi/2, pi) จริง',
    [s for _, _, s in ps] == [1], [s for _, _, s in ps])

print()
print('=' * 70)
print('ผลรวมรอบตรวจซ้ำ: ผ่าน %d / %d ข้อย่อย' % (sum(OK), len(OK)))
print('=' * 70)

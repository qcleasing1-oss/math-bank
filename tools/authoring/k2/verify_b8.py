# -*- coding: utf-8 -*-
"""STEP D · ตรวจคำตอบและตัวลวงของก้อน 8 ด้วย sympy (กฎเหล็กข้อ 1 · ห้ามข้าม)"""
import sympy as sp

x, t, th = sp.symbols('x t theta', real=True)
OK = []


def say(tag, cond, detail=''):
    OK.append(bool(cond))
    print(('  ✅ ' if cond else '  ❌ ') + tag, detail)


def sign_pieces(expr, var, lo, hi):
    """ตัดช่วง [lo,hi] ด้วยศูนย์ของ expr แล้วคืน [(ซ้าย, ขวา, เครื่องหมาย)] แบบ exact

    ⚠️ ทำไมต้องมีฟังก์ชันนี้ (บันทึกไว้กันคนหลังหลงทาง · 5 ส.ค. 69)
    รอบแรกใช้ `solveset(อสมการตรีโกณ, ช่วง)` กับ `sp.is_increasing` ตรง ๆ แล้วได้ False
    4 จุด ทั้งที่โจทย์ถูก — เพราะ
      · solveset ของอสมการตรีโกณบนช่วงจำกัด คืน **แค่คาบแรก** (q047 ได้ 8/3 แทน 20/3)
      · is_increasing ตัดสินฟังก์ชันตรีโกณที่มีเฟสไม่ได้ คืน False ทั้งที่เพิ่มจริง (q048)
    วิธีนี้ใช้ทฤษฎีบทค่าระหว่างกลางแทน: ฟังก์ชันต่อเนื่อง ถ้าไม่มีศูนย์ในช่วงเปิด
    ⇒ เครื่องหมายคงที่ทั้งช่วง ⇒ ดูเครื่องหมายที่จุดกึ่งกลางจุดเดียวก็พอ (exact ไม่ใช่ตัวเลข)
    """
    zs = sorted([z for z in sp.solveset(sp.Eq(expr, 0), var, sp.Interval(lo, hi))],
                key=float)
    cuts = [lo] + [z for z in zs if lo < z < hi] + [hi]
    out = []
    for a, b in zip(cuts, cuts[1:]):
        mid = sp.Rational(1, 2) * (a + b)
        out.append((a, b, sp.sign(sp.simplify(expr.subs(var, mid)))))
    return out


# ═══════════════════════════════════════════════════════════ q045
print('═' * 70)
print('q045 · sin*tan > 0 และ cos*cot < 0 ⇒ จตุภาคใด')
print('═' * 70)
# ตัวแทนมุมของแต่ละจตุภาค
reps = {1: sp.pi / 6, 2: 2 * sp.pi / 3, 3: 7 * sp.pi / 6, 4: 5 * sp.pi / 3}
good = []
for q, a in reps.items():
    c1 = sp.simplify(sp.sin(a) * sp.tan(a)) > 0
    c2 = sp.simplify(sp.cos(a) * sp.cot(a)) < 0
    print('   จตุภาค %d : sin*tan = %s (>0? %s) · cos*cot = %s (<0? %s)'
          % (q, sp.nsimplify(sp.sin(a) * sp.tan(a)), bool(c1),
             sp.nsimplify(sp.cos(a) * sp.cot(a)), bool(c2)))
    if bool(c1) and bool(c2):
        good.append(q)
say('มีจตุภาคเดียวที่สอดคล้องทั้งสองเงื่อนไข และคือจตุภาคที่ 4', good == [4], good)
# ยืนยันรูปพีชคณิต: sin*tan = sin^2/cos ⇒ เครื่องหมายตาม cos ; cos*cot = cos^2/sin ⇒ ตามsin
say('sin*tan = sin^2/cos จริง',
    sp.simplify(sp.sin(th) * sp.tan(th) - sp.sin(th) ** 2 / sp.cos(th)) == 0)
say('cos*cot = cos^2/sin จริง',
    sp.simplify(sp.cos(th) * sp.cot(th) - sp.cos(th) ** 2 / sp.sin(th)) == 0)

# ═══════════════════════════════════════════════════════════ q046
print()
print('═' * 70)
print('q046 · เรียงลำดับ sin 2 · cos 2 · tan 2 · cot 2 (เรเดียน) จากน้อยไปมาก')
print('═' * 70)
s2, c2v, t2, k2 = sp.sin(2), sp.cos(2), sp.tan(2), sp.cot(2)
print('   sin 2 = %.6f · cos 2 = %.6f · tan 2 = %.6f · cot 2 = %.6f'
      % (float(s2), float(c2v), float(t2), float(k2)))
say('ลำดับที่ถูกคือ tan 2 < cot 2 < cos 2 < sin 2',
    float(t2) < float(k2) < float(c2v) < float(s2))
# ── เหตุผลที่ใช้ในเฉลย ต้องไม่พึ่งเครื่องคิดเลขเลย ──
say('[ขั้น 1] pi/2 < 2 < 3pi/4 ⇒ 2 เรเดียนอยู่จตุภาคที่ 2',
    float(sp.pi / 2) < 2 < float(3 * sp.pi / 4))
say('[ขั้น 1] จึง sin 2 > 0 และอีกสามตัวเป็นลบ',
    float(s2) > 0 and float(c2v) < 0 and float(t2) < 0 and float(k2) < 0)
say('[ขั้น 2] มุมอ้างอิง pi - 2 มากกว่า pi/4 ⇒ |tan 2| > 1 ⇒ tan 2 < -1',
    float(sp.pi - 2) > float(sp.pi / 4) and float(t2) < -1)
say('[ขั้น 3] tan 2 · cot 2 = 1 ⇒ |cot 2| < 1 ⇒ -1 < cot 2 < 0',
    sp.simplify(sp.tan(2) * sp.cot(2) - 1) == 0 and -1 < float(k2) < 0)
say('[ขั้น 3] จึงสรุป tan 2 < -1 < cot 2 ได้โดยไม่ต้องคิดเลข', float(t2) < -1 < float(k2))
say('[ขั้น 4] 0 < sin 2 < 1 (เพราะ 2 ไม่ใช่ pi/2)', 0 < float(s2) < 1)
say('[ขั้น 4] cot 2 = cos 2 / sin 2 · หารจำนวนลบด้วยค่าใน (0,1) ⇒ ยิ่งลบ ⇒ cot 2 < cos 2',
    sp.simplify(sp.cot(2) - sp.cos(2) / sp.sin(2)) == 0 and float(k2) < float(c2v))
# ตรวจอิสระ: ผลต่าง cos 2 - cot 2 = cos 2 (1 - 1/sin 2) ต้องเป็นบวก
diff = sp.simplify(sp.cos(2) - sp.cot(2))
say('ตรวจอิสระ · cos 2 - cot 2 = cos2(1 - 1/sin2) > 0', float(diff) > 0,
    '%.6f' % float(diff))
# ตัวลวง (i) หน่วยผิด: มองเป็น 2 องศา
d = sp.pi / 90
print('   [ตัวลวงหน่วยผิด] sin2 = %.5f · tan2 = %.5f · cos2 = %.5f · cot2 = %.5f (องศา)'
      % (float(sp.sin(d)), float(sp.tan(d)), float(sp.cos(d)), float(sp.cot(d))))
say('[ตัวลวง 4] ถ้าอ่านเป็นองศาจะได้ sin < tan < cos < cot จริง',
    float(sp.sin(d)) < float(sp.tan(d)) < float(sp.cos(d)) < float(sp.cot(d)))
say('[ตัวลวง 2] สลับ cot กับ cos (เทียบสองตัวลบผิดทาง) ⇒ ไม่ใช่ลำดับจริง',
    not (float(t2) < float(c2v) < float(k2) < float(s2)))
say('[ตัวลวง 3] คิดว่า |cot 2| > |tan 2| ⇒ ไม่ใช่ลำดับจริง',
    not (float(k2) < float(t2) < float(c2v) < float(s2)))

# ═══════════════════════════════════════════════════════════ q047
print()
print('═' * 70)
print('q047 · ชิงช้าสวรรค์ · เด็กต้องสร้าง h(t) เอง แล้วหาเวลาที่สูงเกิน 30 ม. ใน [0,15]')
# 🔴 แก้ขอบเวลา 20 → 15 (5 ส.ค. 69) — ฉบับ [0,20] ใช้ไม่ได้เพราะ 20 เป็นจำนวนเต็มเท่าของ
#    ครึ่งคาบพอดี ⇒ การเทียบบัญญัติไตรยางศ์แบบมักง่าย (1/3 ของ 20 = 20/3) บังเอิญได้คำตอบถูก
#    ⇒ กับดัก "ไม่ครบรอบ" ตายทันที และข้อจะง่ายกว่าที่ตั้งใจ
#    ที่ [0,15] : คำตอบจริง 16/3 ≈ 5.33 แต่บัญญัติไตรยางศ์ให้ 5 ⇒ กับดักกลับมามีชีวิต
print('═' * 70)
# ── ขั้นสร้างแบบจำลอง (ส่วนที่ทำให้ข้อนี้ขึ้นเป็นยากมาก) ──
# รัศมี 18 · จุดต่ำสุดสูงจากพื้น 3 ม. ⇒ ศูนย์กลางสูง 3 + 18 = 21
# ครบรอบ 8 นาที ⇒ สัมประสิทธิ์ = 2pi/8 = pi/4 · เริ่มที่จุดต่ำสุด ⇒ ใช้ -cos
h = 21 - 18 * sp.cos(sp.pi * t / 4)
say('ศูนย์กลางวงล้อสูงจากพื้น 3 + 18 = 21 เมตร', 3 + 18 == 21)
say('ครบรอบ 8 นาที ⇒ สัมประสิทธิ์หน้า t คือ 2pi/8 = pi/4',
    sp.simplify(2 * sp.pi / 8 - sp.pi / 4) == 0)
say('เริ่มจับเวลาที่จุดต่ำสุด ⇒ h(0) = 3', h.subs(t, 0) == 3)
say('ครึ่งรอบ (t = 4) อยู่จุดสูงสุด ⇒ h(4) = 39', h.subs(t, 4) == 39)
say('ความสูงสูงสุด 39 · ต่ำสุด 3', (sp.maximum(h, t, sp.S.Reals) == 39)
    and (sp.minimum(h, t, sp.S.Reals) == 3))
say('คาบเท่ากับ 8 นาที', sp.periodicity(h, t) == 8)
say('15 นาที = 1.875 รอบ (ไม่ครบจำนวนเต็มรอบ และไม่ครบครึ่งรอบ — นี่คือกับดักของข้อ)',
    sp.Rational(15, 8) == sp.Rational(15, 8) and sp.Rational(15, 4) != sp.floor(sp.Rational(15, 4)))
sol = sp.solveset(sp.Eq(h, 30), t, sp.Interval(0, 15))
print('   จุดที่ h = 30 ในช่วง [0,15] :', sorted(sol, key=float))
want = [sp.Rational(8, 3), sp.Rational(16, 3), sp.Rational(32, 3), sp.Rational(40, 3)]
say('รากตรงกับ 8/3, 16/3, 32/3, 40/3 (56/3 ≈ 18.67 หลุดออกนอก 15 แล้ว)',
    sorted(sol, key=float) == want)
say('รากถัดไปคือ 56/3 ซึ่งมากกว่า 15 จริง', sp.Rational(56, 3) > 15)
pieces = sign_pieces(h - 30, t, 0, 15)
for a, b, s in pieces:
    print('   ช่วง (%-6s, %-6s) เครื่องหมาย h-30 = %+d  ยาว %s'
          % (a, b, s, sp.nsimplify(b - a)))
tot = sum((b - a) for a, b, s in pieces if s > 0)
say('ความยาวรวมที่ h > 30 บน [0,15] = 16/3 นาที',
    sp.simplify(tot - sp.Rational(16, 3)) == 0, 'ได้ %s' % sp.nsimplify(tot))
say('แบ่งเป็น 2 ช่วงเต็ม (ช่วงที่สามเริ่ม 56/3 ซึ่งเลย 15 ไปแล้ว)',
    len([1 for a, b, s in pieces if s > 0]) == 2)
# ตรวจอิสระด้วยวิธีเชิงตัวเลข (คนละวิธีกับข้างบน)
hf = sp.lambdify(t, h, 'math')
N = 400000
frac = sum(1 for i in range(N) if hf(15.0 * (i + 0.5) / N) > 30) / N * 15
say('ตรวจอิสระด้วยการสุ่มถี่ 400000 จุด ได้ ~5.3333', abs(frac - 16 / 3) < 1e-3,
    'ได้ %.5f' % frac)
tot8 = sum((b - a) for a, b, s in sign_pieces(h - 30, t, 0, 8) if s > 0)
say('[ตัวลวง 1] คิดรอบเดียว [0,8] ได้ 8/3', sp.simplify(tot8 - sp.Rational(8, 3)) == 0)
# ── กับดักหลัก: เทียบบัญญัติไตรยางศ์ 1/3 ของ 15 = 5 ──
say('[ตัวลวง 2] สัดส่วนของคาบที่อยู่สูงเกิน 30 คือ 1/3 พอดี',
    sp.simplify(sp.Rational(8, 3) / 8 - sp.Rational(1, 3)) == 0)
say('[ตัวลวง 2] บัญญัติไตรยางศ์ 1/3 x 15 = 5 ซึ่ง "ไม่เท่ากับ" 16/3 ⇒ กับดักมีชีวิตจริง',
    sp.Rational(15, 3) != sp.Rational(16, 3))
say('[ตัวลวง 3] นับช่วงที่สามด้วยทั้งที่เลย 15 ⇒ 3 x 8/3 = 8', 3 * sp.Rational(8, 3) == 8)
# ── หลักฐานว่าความผิดพลาดเรื่องเฟสให้ค่าคนละตัว (เก็บไว้เขียนใน จุดพลาด ไม่ใช้เป็นตัวเลือก) ──
hp = 21 + 18 * sp.cos(sp.pi * t / 4)
totp = sum((b - a) for a, b, s in sign_pieces(hp - 30, t, 0, 15) if s > 0)
say('[หลักฐาน] ถ้าใช้เฟสผิด (เริ่มที่จุดสูงสุด) จะได้ 13/3 ซึ่งไม่ตรงกับตัวเลือกใดเลย',
    sp.simplify(totp - sp.Rational(13, 3)) == 0, 'ได้ %s' % sp.nsimplify(totp))
say('[กันคำตอบซ้ำ] ตัวเลือกทั้งสี่ 8/3, 5, 16/3, 8 ต่างกันหมด',
    len({sp.Rational(8, 3), sp.Rational(5), sp.Rational(16, 3), sp.Rational(8)}) == 4)

# ═══════════════════════════════════════════════════════════ q048
print()
print('═' * 70)
print('q048 · f(x) = cos(2x - pi/3) เป็นฟังก์ชันเพิ่มบนช่วงใด')
print('═' * 70)
f = sp.cos(2 * x - sp.pi / 3)
fp = sp.diff(f, x)
print('   f\'(x) =', sp.simplify(fp))
say("f'(x) = -2 sin(2x - pi/3) จริง",
    sp.simplify(fp + 2 * sp.sin(2 * x - sp.pi / 3)) == 0)
cands = [('1', sp.pi / 6, 2 * sp.pi / 3),
         ('2', sp.pi / 3, 5 * sp.pi / 6),
         ('3', sp.pi / 2, sp.pi),
         ('4', 2 * sp.pi / 3, 7 * sp.pi / 6)]
verdict = {}
for name, a, b in cands:
    signs = [s for _, _, s in sign_pieces(fp, x, a, b)]
    verdict[name] = ('เพิ่ม' if signs == [1] else 'ลด' if signs == [-1]
                     else 'ไม่เป็นทั้งสอง (คร่อมจุดกลับตัว)')
    print('   ตัวเลือก %s : ท่อนเครื่องหมายของ f\' = %-9s ⇒ %s'
          % (name, signs, verdict[name]))
say('มีช่วงเดียวที่เป็นฟังก์ชันเพิ่ม และคือตัวเลือก 4',
    [k for k, v in verdict.items() if v == 'เพิ่ม'] == ['4'])
say('[ตัวลวง 1] (pi/6, 2pi/3) เป็นฟังก์ชันลดจริง', verdict['1'] == 'ลด')
say('[ตัวลวง 2] มาจากลบ pi/3 แทนบวก : (pi-pi/3)/2 = pi/3 และ (2pi-pi/3)/2 = 5pi/6',
    sp.simplify((sp.pi - sp.pi / 3) / 2 - sp.pi / 3) == 0 and
    sp.simplify((2 * sp.pi - sp.pi / 3) / 2 - 5 * sp.pi / 6) == 0)
say('[ตัวลวง 2 และ 3] คร่อมจุดกลับตัว จึงไม่เป็นทั้งเพิ่มและลด',
    verdict['2'].startswith('ไม่') and verdict['3'].startswith('ไม่'))
say('[ตัวลวง 3] มาจากลืมเฟส : cos 2x เพิ่มบน (pi/2, pi) จริง',
    [s for _, _, s in sign_pieces(sp.diff(sp.cos(2 * x), x), x,
                                  sp.pi / 2, sp.pi)] == [1])
# ⛔ กันคำตอบซ้อน: ตัวลวงต้องไม่เป็นสับเซตของช่วงเพิ่มใด ๆ (เคยพลาดตอนออกแบบ)
INC = sp.Union(*[sp.Interval.open(k * sp.pi - sp.pi / 3, k * sp.pi + sp.pi / 6)
                 for k in range(-2, 4)])
for name, a, b in cands[:3]:
    say('ตัวลวง %s ไม่ได้อยู่ในช่วงเพิ่มใด ๆ (ไม่มีคำตอบซ้อน)' % name,
        not sp.Interval(a, b).is_subset(INC))
say('สูตรรวมช่วงเพิ่ม (k*pi - pi/3, k*pi + pi/6) · k = 1 ให้ (2pi/3, 7pi/6)',
    sp.simplify(sp.pi - sp.pi / 3 - 2 * sp.pi / 3) == 0 and
    sp.simplify(sp.pi + sp.pi / 6 - 7 * sp.pi / 6) == 0)

# ═══════════════════════════════════════════════════════════ q049
print()
print('═' * 70)
print('q049 · f(x) = cos(bx) ตัดแกน X 7 จุด บน [0, pi] ⇒ f(pi/3) + f(pi/4)')
print('═' * 70)
cnt = {}
for b in range(1, 11):
    z = sp.solveset(sp.cos(b * x), x, sp.Interval(0, sp.pi))
    cnt[b] = len(z)
print('   จำนวนจุดตัดแกน X ต่อค่า b :', cnt)
say('จำนวนจุดตัด = b ทุกค่า', all(cnt[b] == b for b in cnt))
say('7 จุด ⇒ b = 7 เพียงค่าเดียว', [b for b in cnt if cnt[b] == 7] == [7])
val = sp.cos(7 * sp.pi / 3) + sp.cos(7 * sp.pi / 4)
say('f(pi/3) + f(pi/4) = (1 + sqrt2)/2',
    sp.simplify(val - (1 + sp.sqrt(2)) / 2) == 0, sp.nsimplify(val))
say('cos(7pi/3) = 1/2', sp.cos(7 * sp.pi / 3) == sp.Rational(1, 2))
say('cos(7pi/4) = sqrt2/2', sp.simplify(sp.cos(7 * sp.pi / 4) - sp.sqrt(2) / 2) == 0)
v6 = sp.cos(6 * sp.pi / 3) + sp.cos(6 * sp.pi / 4)
v8 = sp.cos(8 * sp.pi / 3) + sp.cos(8 * sp.pi / 4)
say('[ตัวลวง b=6] ได้ 1', sp.simplify(v6 - 1) == 0, v6)
say('[ตัวลวง b=8] ได้ 1/2', sp.simplify(v8 - sp.Rational(1, 2)) == 0, v8)
say('[ตัวลวงเครื่องหมาย] 1/2 - sqrt2/2 = (1-sqrt2)/2',
    sp.simplify(sp.Rational(1, 2) - sp.sqrt(2) / 2 - (1 - sp.sqrt(2)) / 2) == 0)
say('ตัวเลือกทั้งสี่เรียงจากน้อยไปมาก และคำตอบอยู่ช่องที่ 4',
    float((1 - sp.sqrt(2)) / 2) < 0.5 < 1 < float((1 + sp.sqrt(2)) / 2))

print()
print('═' * 70)
print('ผลรวม: ผ่าน %d / %d ข้อย่อย' % (sum(OK), len(OK)))
print('═' * 70)

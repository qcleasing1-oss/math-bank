#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ตัวหารากสมการตรีโกณที่ ⛔ ไม่พึ่ง solveset — เครื่องมือผู้แต่ง (ก้อน 23+)

🔴 **ทำไมต้องมีไฟล์นี้ — เจอของจริง 13 ส.ค. 69 ⛔ ไม่ใช่ความระวังเปล่า ๆ**

    HANDOFF §③ค เขียนไว้นานแล้วว่า *"⛔ ห้ามเชื่อ `solveset` ในสมการตรีโกณ"*
    แต่ ⛔ ไม่เคยมีใครบันทึก **เคสจริง** ไว้ข้าง ๆ กฎ ⇒ มันเป็นคำเตือนที่พิสูจน์ไม่ได้

    ⬤ เคสที่เจอ (ระหว่างออกแบบข้อ q167) :

        sp.solveset(2*sin(x)**2 - sin(x) - 1, x, Interval.Ropen(0, 2*pi))
        ⇒ **{pi/2}**            ← 1 คำตอบ

        ของจริง: (2 sin x + 1)(sin x − 1) = 0 ⇒ sin x = −1/2 หรือ sin x = 1
        ⇒ **{pi/2, 7pi/6, 11pi/6}**   ← **3 คำตอบ**

    ⇒ ⇒ 🔴 **solveset นับขาด 2 จาก 3** และมัน ⛔ ไม่ error ⛔ ไม่เตือน — มันคืนเซตที่ดูปกติ
    ⇒ ⇒ ⇒ ถ้าผู้แต่งเชื่อมัน จะได้ข้อที่ถามว่า "มีกี่คำตอบ" แล้ว**เฉลยผิดตั้งแต่ต้น**
           และ ⛔ ไม่มีด่านไหนในคลังจับได้ เพราะด่านอ่าน JSON ⛔ ไม่ได้แก้สมการ

**วิธีที่ไฟล์นี้ใช้แทน — สองขาที่ต้องบรรจบกัน (⑨)**

    ขา ① กวาดเชิงตัวเลข : แบ่งช่วงละเอียด หาที่ฟังก์ชันเปลี่ยนเครื่องหมาย แล้ว bisection
         ⇒ **⛔ ไม่พึ่งพีชคณิตเชิงสัญลักษณ์เลย** ⇒ ⛔ ไม่มีทางพลาดแบบเดียวกับ solveset
    ขา ② ยืนยันเชิงสัญลักษณ์ : แทนรากที่ขัดเป็นค่าตรงแบบ (เช่น 7*pi/6) กลับเข้าสมการเดิม
         แล้ว `simplify` ต้องได้ 0 เป๊ะ ⇒ กันรากปลอมจากความคลาดเคลื่อนเชิงตัวเลข

    ⇒ **รายงานทั้งสองขาเสมอ + เทียบกับ solveset ให้เห็นด้วย**
      ถ้าสองขาของเราตรงกันแต่ solveset ต่าง ⇒ พิมพ์ 🔴 บอกตรง ๆ ⛔ ไม่กลืนเงียบ

🔒 **จุดบอดที่ไฟล์นี้ประกาศเอง**
    ① รากที่ฟังก์ชัน **แตะศูนย์แล้วเด้งกลับ** (รากคู่ · ⛔ ไม่เปลี่ยนเครื่องหมาย) ขา ① มองไม่เห็น
       ⇒ จึงมีขา ③ : สแกนหาจุดที่ |f| เล็กมากแต่ ⛔ ไม่เปลี่ยนเครื่องหมาย แล้ว **เตือน**
    ② ช่วงที่มี asymptote (tan · sec) — การเปลี่ยนเครื่องหมายข้าม asymptote ⛔ ไม่ใช่ราก
       ⇒ กรอง: ราก r ต้องมี |f(r)| < TOL_F จริง ⛔ ไม่ใช่แค่เครื่องหมายพลิก
    ③ ไฟล์นี้ตอบ **"รากในช่วงที่ระบุ"** เท่านั้น ⛔ ไม่ตอบคำตอบทั่วไป (general solution)

รหัสออก: 0 = ผ่าน · 1 = พบความไม่ตรงกัน · 2 = ตัวเครื่องมือแดง
"""
import sys

import numpy as np
import sympy as sp

VERSION = '1.0'
TOL_F = 1e-6          # |f(r)| ต้องเล็กกว่านี้จึงนับเป็นรากจริง (กัน asymptote)
TOL_DUP = 1e-7        # รากสองตัวใกล้กว่านี้ = ตัวเดียวกัน
GRID = 200001         # ความละเอียดของการกวาด


def roots_numeric(expr, var, lo, hi, grid=GRID):
    """ขา ① — กวาดเชิงตัวเลขบน [lo, hi) · ⛔ ไม่พึ่ง solveset"""
    f = sp.lambdify(var, expr, 'numpy')
    xs = np.linspace(float(lo), float(hi), grid)
    with np.errstate(all='ignore'):
        ys = np.asarray(f(xs), dtype=float)
    found, touch = [], []
    for i in range(len(xs) - 1):
        a, b = ys[i], ys[i + 1]
        if not (np.isfinite(a) and np.isfinite(b)):
            continue
        if a == 0.0:
            found.append(xs[i])
        elif a * b < 0:
            lo_i, hi_i = xs[i], xs[i + 1]
            for _ in range(100):
                mid = (lo_i + hi_i) / 2
                fm = float(f(mid))
                if not np.isfinite(fm):
                    break
                if float(f(lo_i)) * fm <= 0:
                    hi_i = mid
                else:
                    lo_i = mid
            found.append((lo_i + hi_i) / 2)
    # ขา ③ — รากคู่ที่ ⛔ ไม่เปลี่ยนเครื่องหมาย
    for i in range(1, len(xs) - 1):
        if np.isfinite(ys[i]) and abs(ys[i]) < 1e-4:
            if ys[i - 1] * ys[i + 1] > 0 and abs(ys[i]) < abs(ys[i - 1]) and abs(ys[i]) < abs(ys[i + 1]):
                touch.append(xs[i])
    out = []
    for r in found:
        if r >= float(hi) - 1e-9 or r < float(lo) - 1e-12:
            continue
        try:
            if abs(float(f(r))) > TOL_F:      # กัน asymptote
                continue
        except Exception:                      # noqa: BLE001
            continue
        if not any(abs(r - s) < TOL_DUP for s in out):
            out.append(r)
    return sorted(out), sorted(touch)


def snap(r, base=sp.pi, maxden=60):
    """ขัดรากเชิงตัวเลขให้เป็นค่าตรงแบบ k·pi (ถ้าทำได้)"""
    q = sp.nsimplify(sp.Rational(str(round(r / float(base), 12))), rational=True).limit_denominator(maxden)
    cand = q * base
    return cand if abs(float(cand) - r) < 1e-8 else None


def verify(expr, var, lo, hi, label=''):
    """คืน (รากที่ยืนยันแล้ว, รายงานเป็นข้อความ, ตรงกับ solveset ไหม)"""
    lines = []
    num, touch = roots_numeric(expr, var, lo, hi)
    exact, unresolved = [], []
    for r in num:
        s = snap(r)
        if s is not None and sp.simplify(expr.subs(var, s)) == 0:
            exact.append(s)                                   # ขา ②
        else:
            unresolved.append(r)

    try:
        ss = sp.solveset(expr, var, sp.Interval.Ropen(lo, hi))
        n_ss = len(ss) if isinstance(ss, sp.FiniteSet) else None
    except Exception:                                          # noqa: BLE001
        n_ss = None

    lines.append('  %s' % (label or sp.srepr(expr)[:60]))
    lines.append('    ขา ① กวาดเชิงตัวเลข : %d ราก' % len(num))
    lines.append('    ขา ② ยืนยันสัญลักษณ์ : %d ราก%s'
                 % (len(exact), (' · ขัดเป็นค่าตรงแบบไม่ได้ %d' % len(unresolved)) if unresolved else ''))
    if exact:
        lines.append('         ' + ' · '.join(str(e) for e in exact))
    if touch:
        lines.append('    ⚠️ ขา ③ พบจุดที่ |f| เล็กมากแต่ ⛔ ไม่เปลี่ยนเครื่องหมาย %d จุด '
                     '⇒ อาจเป็นรากคู่ ให้ตรวจมือ' % len(touch))
    agree = (n_ss == len(num))
    if n_ss is None:
        lines.append('    solveset : ตอบไม่ได้/ไม่ใช่เซตจำกัด ⇒ ⛔ ใช้เทียบไม่ได้')
    elif agree:
        lines.append('    solveset : %d ราก ✅ ตรงกัน' % n_ss)
    else:
        lines.append('    solveset : %d ราก 🔴 **⛔ ไม่ตรง — เชื่อขา ①②** '
                     '(เคสแบบนี้เกิดจริงแล้ว ดูหัวไฟล์)' % n_ss)
    return exact, '\n'.join(lines), agree


def selftest():
    x = sp.symbols('x', real=True)
    lo, hi = 0, 2 * sp.pi
    passed, failed = [], []

    def say(tag, desc, cond):
        (passed if cond else failed).append('%s %s' % (tag, desc))

    # ① เคสต้นเรื่อง — ตัวที่ solveset พลาดจริง
    e = 2 * sp.sin(x) ** 2 - sp.sin(x) - 1
    r, _, agree = verify(e, x, lo, hi)
    say('①', '🔴 เคสต้นเรื่อง 2sin²x−sinx−1 ⇒ ต้องได้ **3 ราก**', len(r) == 3)
    say('②', '…และต้องเป็น π/2 · 7π/6 · 11π/6 เป๊ะ',
        set(r) == {sp.pi / 2, 7 * sp.pi / 6, 11 * sp.pi / 6})
    say('③', '🧬 …และต้องรายงานว่า solveset ⛔ ไม่ตรง (ไม่งั้นเครื่องมือนี้ไม่มีเหตุผลจะมีอยู่)',
        agree is False)

    # ④ เคสที่ solveset ถูก — ต้อง ⛔ ไม่แดงมั่ว
    r2, _, agree2 = verify(sp.sin(2 * x) - sp.sin(x), x, lo, hi)
    say('④', 'sin2x=sinx ⇒ 4 ราก · และ solveset ต้องตรง (คู่บังคับของ ③)',
        len(r2) == 4 and agree2 is True)

    # ⑤ รากคู่ — ขา ① มองไม่เห็น ต้องมีขา ③ เตือน
    _, rep, _ = verify((sp.sin(x) - 1) ** 2, x, lo, hi)
    say('⑤', '🔒 รากคู่ (sinx−1)² ⇒ ต้องเตือนว่ามีจุดแตะศูนย์ (จุดบอดที่ประกาศเอง)',
        'ขา ③' in rep)

    # ⑥ asymptote ต้องไม่ถูกนับเป็นราก
    r3, _, _ = verify(sp.tan(x) - 1, x, 0, sp.pi)
    say('⑥', '🔒 tan x = 1 บน [0,π) ⇒ ต้องได้ π/4 ตัวเดียว (⛔ ไม่นับ asymptote ที่ π/2)',
        r3 == [sp.pi / 4])

    # ⑦ ⛔ ไม่มีราก ⇒ ต้องคืนว่าง ⛔ ไม่ใช่พัง
    r4, _, _ = verify(sp.sin(x) - 2, x, lo, hi)
    say('⑦', 'sin x = 2 ⇒ ⛔ ไม่มีราก ⇒ คืนลิสต์ว่าง', r4 == [])

    print('trig_roots v%s — self-test' % VERSION)
    for line in passed:
        print('  ✅ ' + line)
    for line in failed:
        print('  ❌ ' + line)
    print('  ── ผ่าน %d · ล้ม %d · รวม %d เคส' % (len(passed), len(failed), len(passed) + len(failed)))
    return 0 if not failed else 1


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    print('ใช้: python trig_roots.py --selftest   หรือ import verify() ไปใช้ตอนแต่งข้อ')
    sys.exit(0)

# -*- coding: utf-8 -*-
"""STEP D · sympy verify · 3 ข้อระดับ ยาก (H-1 7.4 · H-2 7.7 · H-3 7.9)"""
import sympy as sp

print("="*70)
print("H-1 · 7.4 · tanθ+cotθ = -5/2 , 0<θ<π  ⇒  sin³θ - cos³θ = ?")
print("="*70)

th = sp.symbols('theta', real=True)
# 1) หา sinθcosθ
sc = sp.symbols('sc', real=True)
# tan+cot = 1/(s c)
sol_sc = sp.solve(sp.Eq(1/sc, sp.Rational(-5,2)), sc)
print("sinθcosθ =", sol_sc)
SC = sol_sc[0]
assert SC == sp.Rational(-2,5)

# 2) (s-c)^2 = 1 - 2sc
d2 = 1 - 2*SC
print("(s-c)^2 = 1-2sc =", d2, "=", sp.nsimplify(d2))
d = sp.sqrt(d2)
print("s-c = +sqrt =", sp.simplify(d), "=", sp.radsimp(d))

# 3) s^3-c^3 = (s-c)(1+sc)
ans = sp.simplify(d*(1+SC))
print("s³-c³ = (s-c)(s²+sc+c²) = (s-c)(1+sc) =", sp.radsimp(sp.simplify(ans)))
target = sp.Rational(9,25)*sp.sqrt(5)
print("เทียบกับ 9√5/25 :", sp.simplify(ans - target) == 0)
assert sp.simplify(ans - target) == 0

# 4) หา θ จริง ๆ ทั้งหมดใน (0,π) แล้วเช็คตรง ๆ
print("-"*70)
print("ตรวจด้วยรากจริงทุกตัวใน (0,π):")
eq = sp.Eq(sp.tan(th)+sp.cot(th), sp.Rational(-5,2))
# แก้ผ่าน s = sinθ
s = sp.symbols('s', positive=True)   # 0<θ<π ⇒ sinθ>0
# sc = -2/5, c = -2/(5s), s²+c²=1
cand = sp.solve([sp.Eq(s**2 + (sp.Rational(-2,5)/s)**2, 1)], [s], dict=True)
roots = []
for r in cand:
    sv = sp.simplify(r[s])
    if sv.is_real and sv > 0:
        cv = sp.simplify(sp.Rational(-2,5)/sv)
        roots.append((sv, cv))
for sv, cv in roots:
    chk_pyth = sp.simplify(sv**2+cv**2-1)
    chk_eq   = sp.simplify(sv/cv + cv/sv + sp.Rational(5,2))
    val      = sp.radsimp(sp.simplify(sv**3-cv**3))
    plus     = sp.radsimp(sp.simplify(sv**3+cv**3))
    print("  s=%-22s c=%-22s  s²+c²-1=%s  eq=%s" %
          (sp.nsimplify(sv), sp.nsimplify(cv), chk_pyth, chk_eq))
    print("     s³-c³ = %-16s   s³+c³ = %s   (s+c = %s)" %
          (val, plus, sp.radsimp(sp.simplify(sv+cv))))
    assert chk_pyth == 0 and chk_eq == 0
    assert sp.simplify(val - target) == 0
print("⇒ s³-c³ เท่ากันทุกราก = 9√5/25 ✓   ⇒ s³+c³ ไม่เท่ากัน (กำกวมจริง) ✓")

# 5) ตัวลวง
print("-"*70)
print("ตัวลวง:")
print("  เครื่องหมาย s-c ผิด        ⇒", sp.radsimp(sp.simplify(-d*(1+SC))))
print("  ใช้ (s-c)(1-sc) สลับสูตร    ⇒", sp.radsimp(sp.simplify(d*(1-SC))))
sp1 = sp.sqrt(sp.Rational(1,5))
print("  ตอบ s³+c³ โดยเลือก s+c=+1/√5 ⇒", sp.radsimp(sp.simplify(sp1*(1-SC))))

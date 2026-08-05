# -*- coding: utf-8 -*-
import sympy as sp

print("="*70)
print("H-3 · 7.9 · ด้านเป็นจำนวนเต็มบวกเรียงติดกัน · มุมใหญ่สุด = 2 เท่ามุมเล็กสุด ⇒ cos(มุมใหญ่)")
print("="*70)
n = sp.symbols('n', positive=True)
a, b, c = n, n+1, n+2          # a เล็กสุด ตรงข้ามมุม A เล็กสุด · c ใหญ่สุด ตรงข้ามมุม C ใหญ่สุด

# กฎของไซน์ + C = 2A  ⇒  c/sin2A = a/sinA ⇒ c/(2 sinA cosA) = a/sinA ⇒ cosA = c/(2a)
cosA_sine = sp.simplify(c/(2*a))
print("จากกฎของไซน์  cos A = c/(2a) =", cosA_sine)

# กฎของโคไซน์  cos A = (b²+c²-a²)/(2bc)
cosA_cos = sp.simplify((b**2+c**2-a**2)/(2*b*c))
print("จากกฎของโคไซน์ cos A = (b²+c²-a²)/(2bc) =", sp.factor(sp.simplify(cosA_cos)))

sols = sp.solve(sp.Eq(cosA_sine, cosA_cos), n)
print("แก้สมการ ⇒ n =", sols)
N = [s for s in sols if s.is_real and s > 0]
print("รากที่ใช้ได้ (n>0 และทำให้เป็นสามเหลี่ยม) :", N)
assert 4 in [sp.nsimplify(v) for v in N]

print("-"*70)
A_, B_, C_ = 4, 5, 6
cosC = sp.Rational(A_**2 + B_**2 - C_**2, 2*A_*B_)
cosA = sp.Rational(B_**2 + C_**2 - A_**2, 2*B_*C_)
cosB = sp.Rational(A_**2 + C_**2 - B_**2, 2*A_*C_)
print("ด้าน 4,5,6 :  cos A =", cosA, " cos B =", cosB, " cos C =", cosC)
print("cos(2A) =", sp.simplify(2*cosA**2-1), " ⇒ เท่ากับ cos C ?", sp.simplify(2*cosA**2-1-cosC)==0)
assert sp.simplify(2*cosA**2 - 1 - cosC) == 0
degA = sp.deg(sp.acos(cosA)).evalf()
degB = sp.deg(sp.acos(cosB)).evalf()
degC = sp.deg(sp.acos(cosC)).evalf()
print("มุม (องศา) A=%.4f  B=%.4f  C=%.4f   ผลรวม=%.6f   C/A=%.10f"
      % (degA, degB, degC, degA+degB+degC, degC/degA))
assert abs(float(degA+degB+degC) - 180) < 1e-9
assert abs(float(degC/degA) - 2) < 1e-12

print("-"*70)
print("ตรวจว่าไม่มีสามเหลี่ยมด้านเรียงติดกันชุดอื่นที่ C=2A (กวาด n=1..400):")
hits = []
for nv in range(1, 401):
    A2, B2, C2 = nv, nv+1, nv+2
    if A2 + B2 <= C2:            # อสมการสามเหลี่ยม
        continue
    cA = sp.Rational(B2**2 + C2**2 - A2**2, 2*B2*C2)
    cC = sp.Rational(A2**2 + B2**2 - C2**2, 2*A2*B2)
    if sp.simplify(2*cA**2 - 1 - cC) == 0:
        hits.append(nv)
print("  พบที่ n =", hits, "⇒ เดียวจริง ✓")
assert hits == [4]

print("-"*70)
print("ตัวลวง:")
print("  ตอบ cos ของมุมเล็กสุด (A) ⇒", cosA)
print("  ตอบ cos ของมุมกลาง  (B) ⇒", cosB)
print("  เครื่องหมายผิดในกฎของโคไซน์ (a²+b²+c² สลับ) ⇒", -cosC)
vals = [cosC, cosA, cosB, -cosC]
print("  ทั้งสี่ค่าไม่ซ้ำกัน :", len(set(vals)) == 4, sorted(vals))
assert len(set(vals)) == 4

print("-"*70)
print("✔ ทางตรวจอิสระ · กฎของไซน์ล้วน:  a/sinA = c/sinC, C=2A")
Aang = sp.acos(cosA)
print("   a/sin A =", (4/sp.sin(Aang)).evalf(), "  c/sin 2A =", (6/sp.sin(2*Aang)).evalf(),
      "  b/sin B =", (5/sp.sin(sp.acos(cosB))).evalf())

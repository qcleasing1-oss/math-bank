# -*- coding: utf-8 -*-
import sympy as sp

print("="*70)
print("H-2 · 7.7 · cos²x + (2k+1)sin x = k²+k+1 มีคำตอบจริง ⇒ ผลบวก k ทั้งหมด")
print("="*70)
x, k, s = sp.symbols('x k s', real=True)

expr = sp.cos(x)**2 + (2*k+1)*sp.sin(x) - (k**2+k+1)
sub  = sp.expand(expr.rewrite(sp.sin).subs(sp.sin(x), s))
print("แทน cos²x = 1-s² ⇒", sp.factor(sp.expand(1-s**2 + (2*k+1)*s - (k**2+k+1))))
quad = sp.expand(s**2 - (2*k+1)*s + (k**2+k))
print("คูณ -1 ⇒", quad, "  แยกตัวประกอบ ⇒", sp.factor(quad))
assert sp.factor(quad) == (s-k)*(s-k-1)

# ตรวจว่าสมการเดิมสมมูลกันจริง
chk = sp.simplify(sp.expand(-(quad).subs(s, sp.sin(x))) - sp.expand(expr))
print("สมมูลกับสมการเดิม (ผลต่าง=0):", chk == 0)
assert chk == 0

print("-"*70)
ok = []
for kv in range(-6, 7):
    r1_ok = -1 <= kv <= 1
    r2_ok = -1 <= kv+1 <= 1
    if r1_ok or r2_ok:
        ok.append(kv)
        # ยืนยันด้วยการหา x จริง
        roots = [v for v in (kv, kv+1) if -1 <= v <= 1]
        xs = [sp.asin(sp.Integer(v)) for v in roots]
        vals = [sp.simplify(expr.subs({k: kv, x: xx})) for xx in xs]
        print("  k=%2d  ราก s ที่ใช้ได้ %-10s  แทนกลับสมการเดิม ⇒ %s"
              % (kv, roots, vals))
        assert all(v == 0 for v in vals)
print("k ที่เป็นไปได้ =", ok, " ผลบวก =", sum(ok))
assert ok == [-2,-1,0,1] and sum(ok) == -2

print("-"*70)
print("ตัวลวง:")
a = [kv for kv in range(-6,7) if -1 <= kv <= 1];        print("  ใช้เฉพาะราก s=k        ⇒", a, "ผลบวก", sum(a))
b = [kv for kv in range(-6,7) if (-1<=kv<=1) and (-1<=kv+1<=1)]; print("  อินเตอร์เซกชัน (ทั้งสองราก) ⇒", b, "ผลบวก", sum(b))
c = [kv for kv in range(-6,7) if (-1<=kv<=1) or (-1<=kv-1<=1)];  print("  แยกตัวประกอบผิดเป็น k,k-1 ⇒", c, "ผลบวก", sum(c))
assert sum(a)==0 and sum(b)==-1 and sum(c)==2

# ยืนยันว่า k=-2 และ k=1 ใช้ได้จริงแบบตัวเลข (ปลายทาง)
print("-"*70)
for kv in (-2, 1):
    roots = [v for v in (kv, kv+1) if -1 <= v <= 1]
    print("  k=%d ⇒ sin x = %s ⇒ มี x จริง ✓" % (kv, roots))
for kv in (-3, 2):
    roots = [v for v in (kv, kv+1) if -1 <= v <= 1]
    print("  k=%d ⇒ ราก s ที่ใช้ได้ %s ⇒ ไม่มีคำตอบ ✓" % (kv, roots))
    assert roots == []

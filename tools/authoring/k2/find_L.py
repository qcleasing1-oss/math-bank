# -*- coding: utf-8 -*-
"""ค้นหาความยาวส่วนโค้ง L ที่ทำให้เส้นทางพลาดสี่เส้นตกคนละจตุภาค (q041)"""
import math
TAU = 2 * math.pi

def quad_rad(a):
    a = a % TAU
    if 0 < a < math.pi / 2: return 1
    if math.pi / 2 < a < math.pi: return 2
    if math.pi < a < 3 * math.pi / 2: return 3
    if 3 * math.pi / 2 < a < TAU: return 4
    return 0

def quad_deg(d):
    d = d % 360
    if 0 < d < 90: return 1
    if 90 < d < 180: return 2
    if 180 < d < 270: return 3
    if 270 < d < 360: return 4
    return 0

def margin_rad(a):
    a = a % TAU
    return min(abs(a - k * math.pi / 2) for k in range(5))

def margin_deg(d):
    d = d % 360
    return min(abs(d - k * 90) for k in range(5))

cands = []
for L in range(100, 3001, 10):
    r = L % TAU
    if quad_rad(r) != 3:              # คำตอบถูก ต้องอยู่จตุภาค 3
        continue
    if quad_deg(L) != 4:              # เส้นทางพลาด คิดว่าเป็นองศา
        continue
    if quad_rad(-r) != 2:             # เส้นทางพลาด วัดตามเข็ม
        continue
    if quad_rad(L % math.pi) != 1:    # เส้นทางพลาด ลบด้วย pi
        continue
    mr, md, mp = margin_rad(r), margin_deg(L), margin_rad(L % math.pi)
    if mr < 0.20 or md < 8 or mp < 0.20:
        continue
    cands.append((L, r, L % TAU, L % 360, L % math.pi, mr, md, mp))

print('พบ', len(cands), 'ตัวเลือก')
for L, r, a, d, p, mr, md, mp in cands[:40]:
    print('L=%5d | mod 2pi = %.4f (จตุภาค 3, ห่างขอบ %.2f) | mod 360 = %6.2f องศา (จตุภาค 4, ห่าง %.1f) | mod pi = %.4f (จตุภาค 1, ห่าง %.2f) | รอบ = %d'
          % (L, a, mr, d, md, p, mp, int(L // TAU)))

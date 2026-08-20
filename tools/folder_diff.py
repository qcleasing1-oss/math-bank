#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""folder_diff.py — เทียบสองโฟลเดอร์ว่าตรงกันไหม (เช่น math-portal กับ math-bank)
ใช้: python folder_diff.py "A:\...\สื่อการสอน" "A:\...\math-bank" [--ext .json .js .html] [--out folder_diff.csv]
"""
import os, hashlib, csv, argparse

def walk(root, exts):
    out = {}
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in ('.git', 'node_modules', '__pycache__', '_snapshots')]
        for f in fn:
            if exts and os.path.splitext(f)[1].lower() not in exts: continue
            p = os.path.join(dp, f)
            try: h = hashlib.md5(open(p, 'rb').read()).hexdigest()
            except Exception: continue
            out[os.path.relpath(p, root).replace('\\', '/')] = (h, os.path.getsize(p))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('a'); ap.add_argument('b')
    ap.add_argument('--ext', nargs='*', default=[])
    ap.add_argument('--out', default='folder_diff.csv')
    x = ap.parse_args()
    exts = {e.lower() if e.startswith('.') else '.' + e.lower() for e in x.ext}
    A, B = walk(x.a, exts), walk(x.b, exts)
    rows = []
    for k in sorted(set(A) | set(B)):
        if k in A and k not in B: rows.append([k, 'มีเฉพาะฝั่ง A', A[k][1], ''])
        elif k in B and k not in A: rows.append([k, 'มีเฉพาะฝั่ง B', '', B[k][1]])
        elif A[k][0] != B[k][0]: rows.append([k, '🔴 เนื้อไม่ตรงกัน', A[k][1], B[k][1]])
    with open(x.out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f); w.writerow(['ไฟล์', 'สถานะ', 'ขนาดฝั่ง A', 'ขนาดฝั่ง B']); w.writerows(rows)
    same = len(set(A) & set(B)) - sum(1 for r in rows if r[1].startswith('🔴'))
    print(f'A: {len(A):,} ไฟล์ · B: {len(B):,} ไฟล์ · ตรงกัน {same:,} · ต่าง {len(rows):,}')
    for r in rows[:15]: print(f'  {r[1]}  {r[0]}')
    if len(rows) > 15: print(f'  … อีก {len(rows)-15} รายการใน {x.out}')
    print(f'✅ {x.out}')

if __name__ == '__main__': main()

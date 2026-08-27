#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""snapshot.py — สำรองคลัง+ผลงานเป็น zip พร้อมลายนิ้วมือ md5 (กันงานหาย)
ใช้: python snapshot.py [--src data _t1run\results tools] [--out _snapshots]
เก็บไฟล์ snapshot_YYYYMMDD-HHMM.zip + .md5.txt · เก็บย้อนหลังกี่ชุดกำหนดด้วย --keep
"""
import os, sys, glob, zipfile, hashlib, argparse, datetime

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', nargs='*', default=['data', os.path.join('_t1run', 'results'), 'tools'])
    ap.add_argument('--out', default='_snapshots')
    ap.add_argument('--keep', type=int, default=7)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M')
    zp = os.path.join(a.out, f'snapshot_{stamp}.zip')
    lines, n, tot = [], 0, 0
    with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
        for s in a.src:
            files = [s] if os.path.isfile(s) else glob.glob(os.path.join(s, '**', '*'), recursive=True)
            for f in files:
                if not os.path.isfile(f): continue
                h = hashlib.md5(open(f, 'rb').read()).hexdigest()
                z.write(f, f); lines.append(f'{h}  {f}'); n += 1; tot += os.path.getsize(f)
    open(zp[:-4] + '.md5.txt', 'w', encoding='utf-8').write('\n'.join(lines))
    old = sorted(glob.glob(os.path.join(a.out, 'snapshot_*.zip')))[:-a.keep]
    for f in old:
        os.remove(f)
        if os.path.exists(f[:-4] + '.md5.txt'): os.remove(f[:-4] + '.md5.txt')
    print(f'✅ {zp} · {n:,} ไฟล์ · ต้นฉบับรวม {tot/1048576:.1f} MB · zip {os.path.getsize(zp)/1048576:.1f} MB')
    print(f'   ลายนิ้วมือ: {zp[:-4]}.md5.txt' + (f' · ลบชุดเก่า {len(old)} ชุด' if old else ''))

if __name__ == '__main__': main()

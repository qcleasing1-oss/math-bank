# -*- coding: utf-8 -*-
"""เก็บไฟล์ผล t1 จาก Downloads → _t1run/results แล้ว merge + สร้าง progress.html ให้ครบในคำสั่งเดียว
⛔ ไม่ลบอะไรทั้งสิ้น · ถ้าไฟล์ชื่อซ้ำจะไม่ทับ แต่เติมท้ายว่า -dup"""
import os, sys, json, shutil, subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
DL   = pathlib.Path(os.path.expanduser('~')) / 'Downloads'
RES  = ROOT / '_t1run' / 'results'
RES.mkdir(parents=True, exist_ok=True)

moved, skipped = [], []
import datetime, itertools
cands = sorted(itertools.chain(DL.glob('t1_*.json'), DL.glob('out*.json')))
for p in cands:
    try:                                     # ตรวจว่าเป็น JSON ที่อ่านได้ก่อนย้ายเสมอ
        n = len(json.load(open(p, encoding='utf-8-sig')))
    except Exception as e:
        skipped.append(f"{p.name} — อ่านไม่ได้ ({type(e).__name__}) ⇒ ไม่ย้าย"); continue
    name = p.name
    if not name.startswith('t1_'):
        ts = datetime.datetime.fromtimestamp(p.stat().st_mtime).strftime('%Y%m%d-%H%M')
        name = f't1_{ts}.json'
        print(f"   ↻ เปลี่ยนชื่อ {p.name} → {name} (ใช้เวลาแก้ไขไฟล์เป็นตราเวลา)")
    dst = RES / name
    if dst.exists(): dst = RES / (p.stem + '-dup' + p.suffix)
    shutil.move(str(p), str(dst)); moved.append(f"{dst.name} · {n} ข้อ")

print("=" * 60)
print(f"① เก็บไฟล์จาก Downloads : ย้ายได้ {len(moved)} ไฟล์")
for m in moved:   print("   +", m)
for s in skipped: print("   🔴", s)
if not moved and not skipped:
    print("   (ไม่พบไฟล์ t1_*.json ใน Downloads — ถ้าเพิ่งกดโหลด ลองรันซ้ำอีกที)")

def run(label, args):
    print("\n" + "=" * 60); print(label)
    subprocess.run([sys.executable] + args, cwd=str(ROOT))

run("② รวมเป็น MASTER", ['tools/merge_master.py'])
run("③ สร้างหน้าความคืบหน้า", [
    'tools/progress.py',
    '--bank', 'data/bank.json', '--manifest', 'data/manifest.json',
    '--done', '_t1run/results', '--queue', '_t1run/QUEUE_ปัจจุบัน.json',
    '--master', '_t1run/results/t1_MASTER.json', '--out', '_t1run/progress.html',
    '--rounds', '16:08,18:08,20:08,22:08,00:08,02:08,04:08,06:08'])
print("\n" + "=" * 60)
print("เสร็จแล้ว — เปิด  _t1run\\progress.html  ได้เลย")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""merge_master.py — รวมไฟล์ผลทุกไฟล์เป็น MASTER เดียว ตัดข้อซ้ำ เลือกฉบับที่ดีที่สุด
ใช้: python merge_master.py [--done _t1run\\results] [--bank data\\bank.json] [--out _t1run\\results\\t1_MASTER.json]
     [--choices _t1run\\choice_*.json] [--dry-run]
เกณฑ์เลือกฉบับ: (1) คำตอบตรงเฉลย (2) ขั้นตอน+กับดักมากกว่า (3) ยาวกว่า

🔴 ชั้นคำเคาะครู (เพิ่ม 24 ส.ค. 2569 — หลังเหตุการณ์ที่คำเคาะ 25 ข้อถูกกลืนเงียบ)
   เกณฑ์อัตโนมัติข้างบนใช้ "ขั้นเยอะ = ดีกว่า" — แต่ตอนครูเลือกจริง 95 ข้อ ครูเลือก
   ฉบับที่ **สั้นลง 13 · เท่าเดิม 9 · ยาวขึ้น 3** (สั้น : ยาว ≈ 4 : 1)
   ⇒ เกณฑ์เครื่องสวนทางกับคำเคาะครู ⇒ ทุกครั้งที่ merge วิ่ง คำเคาะจะถูกลบทิ้ง
   ⇒ ⇒ คำเคาะครูจึงต้องเป็น **ชั้นทับสุดท้าย** และเวลาทับต้อง **พิมพ์บอก ⛔ ห้ามเงียบ**
"""
import json, os, re, glob, argparse, hashlib

def S(v): return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))
def norm(x):
    t = re.sub(r'\\left|\\right|\\text|\\mathrm', '', S(x)).replace('dfrac', 'frac').replace('tfrac', 'frac')
    return re.sub(r'[\s$\\{}()\[\],"\']', '', t)

# 🔑 ลายนิ้วมือของ "ฉบับ" — ต้องตรงกับที่เครื่องมือเลือกรุ่นใช้ (เลือกรุ่นt1.html)
#    ⛔ ห้ามเปลี่ยนสูตรนี้ ถ้าเปลี่ยน คำเคาะเก่าทั้งหมดจะหาที่ลงไม่เจอ
def vhash(r):
    return hashlib.md5(json.dumps(r, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()[:8]

def load_choices(patterns):
    """อ่านไฟล์คำเคาะครูทุกไฟล์ที่เข้าเงื่อนไข → {id: hash} · ไฟล์ใหม่กว่าทับไฟล์เก่ากว่า"""
    files = []
    for p in patterns:
        files += [p] if os.path.isfile(p) else glob.glob(p)
    files = sorted(set(files), key=lambda f: os.path.getmtime(f))
    out, src = {}, {}
    for f in files:
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception as e:
            print(f'   ⚠️ อ่านไฟล์คำเคาะไม่ได้: {f} — {e}'); continue
        if not isinstance(d, dict):
            print(f'   ⚠️ ไฟล์คำเคาะรูปแบบไม่ถูก (ต้องเป็น {{id: hash}}): {f}'); continue
        for k, v in d.items():
            if isinstance(v, str): out[k] = v; src[k] = os.path.basename(f)
    return out, src, files

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--done', nargs='*', default=[os.path.join('_t1run', 'results')])
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--out', default=os.path.join('_t1run', 'results', 't1_MASTER.json'))
    ap.add_argument('--choices', nargs='*', default=[os.path.join('_t1run', 'choice_*.json')],
                    help='ไฟล์คำเคาะครู {id: hash} · ใส่ค่าว่างเพื่อปิดชั้นนี้')
    ap.add_argument('--dry-run', action='store_true', help='คำนวณและรายงาน แต่ ⛔ ไม่เขียนไฟล์')
    a = ap.parse_args()
    key = {}
    if os.path.exists(a.bank):
        for q in load_bank(a.bank):
            c = q.get('correct')
            key[q['id']] = q['choices'][c] if isinstance(c, int) and q.get('choices') else S(c)
    files = []
    for p in a.done:
        files += [p] if os.path.isfile(p) else glob.glob(os.path.join(p, '**', '*.json'), recursive=True)
    files = [f for f in files if os.path.abspath(f) != os.path.abspath(a.out)]
    vers, nfile, nrec = {}, 0, 0
    for f in sorted(files):
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        if not (isinstance(d, list) and d and isinstance(d[0], dict) and 'steps' in d[0]): continue
        nfile += 1
        for r in d:
            nrec += 1; vers.setdefault(r['id'], []).append(r)
    def hit(r):
        k = norm(key.get(r['id'], ''))
        blob = norm(S(r['steps'][-1].get('eq') or '')) + norm(S(r.get('verify', {}).get('result') or ''))
        return bool(k) and (k in blob or (blob and blob in k))
    def score(r): return (1 if hit(r) else 0, len(r.get('steps', [])) + len(r.get('traps', [])), len(S(r)))
    chosen = {i: max(v, key=score) for i, v in vers.items()}

    # ---------- 🔴 ชั้นคำเคาะครู — ทับหลังสุด และรายงานทุกครั้ง ----------
    ch, csrc, cfiles = load_choices([p for p in a.choices if p])
    applied, same, notfound, noid = [], [], [], []
    for i, h in ch.items():
        if i not in vers: noid.append(i); continue
        m = [r for r in vers[i] if vhash(r) == h]
        if not m: notfound.append(i); continue
        if vhash(chosen[i]) == h: same.append(i)
        else: chosen[i] = m[0]; applied.append(i)

    best = list(chosen.values())
    dup = nrec - len(best)
    if not a.dry_run:
        os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
        json.dump(best, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(('🧪 ทดลอง (⛔ ไม่เขียนไฟล์) ' if a.dry_run else '✅ ') + a.out)
    print(f'   อ่าน {nfile} ไฟล์ · {nrec:,} ฉบับ ⇒ id ไม่ซ้ำ {len(best):,} ข้อ · ตัดฉบับซ้ำทิ้ง {dup:,}')
    if key: print(f'   ฉบับที่เลือกแล้วตรงเฉลย {sum(1 for r in best if hit(r)):,} / {len(best):,}')

    # ---------- รายงานชั้นคำเคาะ ⛔ ห้ามเงียบไม่ว่ากรณีใด ----------
    print('   ── ชั้นคำเคาะครู ──')
    if not cfiles:
        print('   ⚠️ ⛔ ไม่พบไฟล์คำเคาะเลย — MASTER นี้ใช้เกณฑ์เครื่องล้วน')
        print('      (เกณฑ์เครื่อง = "ขั้นเยอะกว่าชนะ" ซึ่งสวนทางกับที่ครูเลือกจริง 4 ต่อ 1)')
    else:
        print(f'   อ่านคำเคาะ {len(cfiles)} ไฟล์: ' + ' · '.join(os.path.basename(f) for f in cfiles))
        print(f'   คำเคาะทั้งหมด {len(ch)} ข้อ ⇒ ทับจริง {len(applied)} · ตรงกับเครื่องอยู่แล้ว {len(same)}')
        if applied:
            print('   🔧 ข้อที่คำเคาะครูทับเกณฑ์เครื่อง:')
            for i in sorted(applied):
                print(f'      {i} → {ch[i]}  (จาก {csrc[i]})')
        if notfound:
            print(f'   🔴 {len(notfound)} ข้อ — คำเคาะชี้ไปที่ฉบับที่ **หาไม่เจอในไฟล์ผล** ⇒ ใช้ของเครื่องแทน:')
            for i in sorted(notfound): print(f'      {i} → {ch[i]}')
            print('      ⇒ แปลว่าไฟล์ผลต้นทางหายไป หรือสูตรลายนิ้วมือเปลี่ยน — ตรวจก่อนเชื่อ MASTER นี้')
        if noid:
            print(f'   ⚠️ {len(noid)} ข้อ — คำเคาะมี id ที่ ⛔ ไม่มีในไฟล์ผลเลย: {sorted(noid)[:10]}')
    if not a.dry_run and (notfound or noid):
        print('   🔴 เขียนไฟล์แล้ว แต่ **มีคำเคาะที่ทำตามไม่ได้** — อย่าเพิ่งถือว่า MASTER นี้ตรงใจครู')

if __name__ == '__main__': main()

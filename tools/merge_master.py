#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""merge_master.py — รวมไฟล์ผลทุกไฟล์เป็น MASTER เดียว ตัดข้อซ้ำ เลือกฉบับที่ดีที่สุด
ใช้: python merge_master.py [--done _t1run\results] [--bank data\bank.json] [--out _t1run\results\t1_MASTER.json]
เกณฑ์เลือกฉบับ: (1) คำตอบตรงเฉลย (2) ขั้นตอน+กับดักมากกว่า (3) ยาวกว่า
"""
import json, os, re, glob, argparse

def S(v): return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))
def norm(x):
    t = re.sub(r'\\left|\\right|\\text|\\mathrm', '', S(x)).replace('dfrac', 'frac').replace('tfrac', 'frac')
    return re.sub(r'[\s$\\{}()\[\],"\']', '', t)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--done', nargs='*', default=[os.path.join('_t1run', 'results')])
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--out', default=os.path.join('_t1run', 'results', 't1_MASTER.json'))
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
    best = [max(v, key=score) for v in vers.values()]
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    json.dump(best, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    dup = nrec - len(best)
    print(f'✅ {a.out}')
    print(f'   อ่าน {nfile} ไฟล์ · {nrec:,} ฉบับ ⇒ id ไม่ซ้ำ {len(best):,} ข้อ · ตัดฉบับซ้ำทิ้ง {dup:,}')
    if key: print(f'   ฉบับที่เลือกแล้วตรงเฉลย {sum(1 for r in best if hit(r)):,} / {len(best):,}')

if __name__ == '__main__': main()

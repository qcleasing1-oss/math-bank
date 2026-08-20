#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""id_registry.py — ดูเลข id ที่ว่าง/เลขถัดไปของแต่ละชุด (กันตั้งชื่อชนกันตอนเพิ่มโจทย์ใหม่)
ใช้: python id_registry.py [--set alvl1-2566-03] [--out id_registry.csv]
"""
import json, os, re, csv, argparse, collections
def load_bank(p):
    d=json.load(open(p,encoding='utf-8'))
    return d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,list) and v and isinstance(v[0],dict))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bank',default=os.path.join('data','bank.json'))
    ap.add_argument('--set'); ap.add_argument('--out',default='id_registry.csv')
    a=ap.parse_args()
    items=load_bank(a.bank)
    g=collections.defaultdict(list)
    for q in items:
        sid=q.get('setId') or re.sub(r'-q\d+[a-z]?$','',q['id'])
        m=re.search(r'-q(\d+)',q['id'])
        g[sid].append(int(m.group(1)) if m else None)
    rows=[]
    for sid,nums in sorted(g.items()):
        ns=sorted(n for n in nums if n is not None)
        if not ns: rows.append([sid,len(nums),'','','']); continue
        gaps=[n for n in range(1,max(ns)) if n not in set(ns)]
        rows.append([sid,len(nums),min(ns),max(ns),
                     f'{sid}-q{max(ns)+1}',' '.join(str(x) for x in gaps[:20])+(' …' if len(gaps)>20 else '')])
    with open(a.out,'w',newline='',encoding='utf-8-sig') as f:
        w=csv.writer(f); w.writerow(['ชุด','จำนวนข้อ','เลขต่ำสุด','เลขสูงสุด','id ถัดไปที่ควรใช้','เลขที่ว่างอยู่']); w.writerows(rows)
    if a.set:
        for r in rows:
            if r[0]==a.set: print(f'ชุด {r[0]} · {r[1]} ข้อ · เลข {r[2]}–{r[3]} · **id ถัดไป = {r[4]}** · ว่าง: {r[5] or "—"}')
    print(f'✅ {a.out} · {len(rows)} ชุด')
if __name__=='__main__': main()

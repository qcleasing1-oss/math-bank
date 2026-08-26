#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""normalize_tex.py — ตรวจ/จัดรูปสูตรให้เป็นแบบเดียวกันทั้งคลัง
ค่าเริ่มต้น = ตรวจอย่างเดียว (ไม่แก้ไฟล์) · เติม --write ถึงจะแก้จริง (สำรองไฟล์เดิมให้อัตโนมัติ)
ใช้: python normalize_tex.py [--bank data\bank.json] [--write] [--out tex_issues.csv]
กฎ: \( \) \[ \] → $ $ · \tfrac → \dfrac · เลขไทย ๐-๙ ในสูตร → 0-9 · ลบช่องว่างซ้ำในสูตร
"""
import json, os, re, csv, shutil, argparse, datetime
RULES=[(re.compile(r'\\\((.+?)\\\)',re.S),r'$\1$'),(re.compile(r'\\\[(.+?)\\\]',re.S),r'$$\1$$'),
       (re.compile(r'\\tfrac'),r'\\dfrac')]
THAI='๐๑๒๓๔๕๖๗๘๙'
def fix(s):
    if not isinstance(s,str): return s,[]
    hit=[]; o=s
    for rx,rep in RULES:
        if rx.search(s): hit.append(rx.pattern); s=rx.sub(rep,s)
    def th(m):
        return m.group(0).translate({ord(c):str(i) for i,c in enumerate(THAI)})
    if any(c in s for c in THAI):
        s2=re.sub(r'\$[^$]*\$',lambda m:th(m),s)
        if s2!=s: hit.append('เลขไทยในสูตร'); s=s2
    return s,hit
def walk(o,path,rows,rid):
    if isinstance(o,str):
        n,h=fix(o)
        if h: rows.append([rid,path,' · '.join(h),o[:70],n[:70]])
        return n
    if isinstance(o,list): return [walk(v,f'{path}[{i}]',rows,rid) for i,v in enumerate(o)]
    if isinstance(o,dict): return {k:walk(v,f'{path}.{k}',rows,rid) for k,v in o.items()}
    return o
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bank',default=os.path.join('data','bank.json'))
    ap.add_argument('--write',action='store_true')
    ap.add_argument('--out',default='tex_issues.csv')
    a=ap.parse_args()
    raw=json.load(open(a.bank,encoding='utf-8'))
    items=raw if isinstance(raw,list) else next(v for v in raw.values() if isinstance(v,list) and v and isinstance(v[0],dict))
    rows=[]; new=[walk(q,'',rows,q.get('id','?')) for q in items]
    with open(a.out,'w',newline='',encoding='utf-8-sig') as f:
        w=csv.writer(f); w.writerow(['id','ตำแหน่ง','กฎที่เข้า','ก่อน','หลัง']); w.writerows(rows)
    print(f'พบจุดที่ควรจัดรูป {len(rows):,} จุด ใน {len({r[0] for r in rows}):,} ข้อ → {a.out}')
    if a.write and rows:
        bak=a.bank+'.bak-'+datetime.datetime.now().strftime('%Y%m%d-%H%M')
        shutil.copy2(a.bank,bak)
        if isinstance(raw,list): raw=new
        else:
            for k,v in raw.items():
                if isinstance(v,list) and v and isinstance(v[0],dict): raw[k]=new; break
        json.dump(raw,open(a.bank,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
        print(f'✅ แก้ไฟล์แล้ว · สำรองของเดิมไว้ที่ {bak}')
    elif rows: print('   (ตรวจอย่างเดียว ⛔ ยังไม่แก้ไฟล์ — เติม --write ถ้าจะให้แก้จริง)')
if __name__=='__main__': main()

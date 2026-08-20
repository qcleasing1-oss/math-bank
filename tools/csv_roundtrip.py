#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""csv_roundtrip.py — คลัง JSON ↔ CSV (แก้ใน Excel แล้วนำกลับ)
ออก:  python csv_roundtrip.py export --bank data\bank.json --csv bank_edit.csv [--topic 7]
เข้า: python csv_roundtrip.py import --bank data\bank.json --csv bank_edit.csv   (สำรองไฟล์เดิมอัตโนมัติ)
⚠️ นำกลับจะอัปเดตเฉพาะช่องที่อยู่ใน CSV และเฉพาะ id ที่มีอยู่แล้ว ⛔ ไม่สร้างข้อใหม่ ⛔ ไม่ลบข้อ
"""
import json, os, csv, shutil, argparse, datetime
COLS=['id','setId','topic','difficulty','type','hasImage','correct','question','choices']
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('mode',choices=['export','import'])
    ap.add_argument('--bank',default=os.path.join('data','bank.json'))
    ap.add_argument('--csv',default='bank_edit.csv'); ap.add_argument('--topic',nargs='*')
    a=ap.parse_args()
    raw=json.load(open(a.bank,encoding='utf-8'))
    islist=isinstance(raw,list)
    key=None if islist else next(k for k,v in raw.items() if isinstance(v,list) and v and isinstance(v[0],dict))
    items=raw if islist else raw[key]
    if a.mode=='export':
        sel=[q for q in items if not a.topic or set(a.topic)&{str(t) for t in (q.get('topics') or [q.get('topic')])}]
        with open(a.csv,'w',newline='',encoding='utf-8-sig') as f:
            w=csv.writer(f); w.writerow(COLS)
            for q in sel:
                w.writerow([q.get('id',''),q.get('setId',''),q.get('topic',''),q.get('difficulty',''),q.get('type',''),
                            1 if q.get('hasImage') else 0,q.get('correct',''),q.get('question',''),
                            ' ||| '.join(str(c) for c in (q.get('choices') or []))])
        print(f'✅ ออก {a.csv} · {len(sel):,} แถว · แก้ใน Excel ได้ (ตัวเลือกคั่นด้วย " ||| ")')
    else:
        by={q['id']:q for q in items}; n=0; miss=0
        for r in csv.DictReader(open(a.csv,encoding='utf-8-sig')):
            q=by.get(r['id'])
            if not q: miss+=1; continue
            ch=[c.strip() for c in (r.get('choices') or '').split('|||') if c.strip()]
            new={'setId':r.get('setId') or q.get('setId'),'topic':r.get('topic') or q.get('topic'),
                 'difficulty':r.get('difficulty') or q.get('difficulty'),'type':r.get('type') or q.get('type'),
                 'hasImage':str(r.get('hasImage','0')).strip() in ('1','True','true','ใช่'),
                 'question':r.get('question') or q.get('question')}
            if r.get('correct','').strip().isdigit(): new['correct']=int(r['correct'])
            if ch: new['choices']=ch
            if any(q.get(k)!=v for k,v in new.items()): n+=1
            q.update(new)
        bak=a.bank+'.bak-'+datetime.datetime.now().strftime('%Y%m%d-%H%M'); shutil.copy2(a.bank,bak)
        json.dump(raw,open(a.bank,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
        print(f'✅ นำกลับแล้ว · แก้จริง {n:,} ข้อ · ไม่พบ id ในคลัง {miss:,} แถว · สำรองเดิมที่ {bak}')
if __name__=='__main__': main()

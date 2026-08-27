#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""item_analysis.py — วิเคราะห์ข้อสอบจากคำตอบนักเรียน (ค่าความยาก p · อำนาจจำแนก r · ตัวลวงที่ไม่มีใครเลือก)
รูปแบบไฟล์คำตอบ (CSV · หัวตารางต้องมีชื่อนี้):
    student,id,answer            ← answer = เลขตัวเลือกที่เลือก (1,2,3,…)
ใช้: python item_analysis.py --responses คำตอบ.csv [--bank data\bank.json] [--out item_analysis.csv]
⛔ ไฟล์นี้อยู่บนเครื่องครู ⛔ ไม่ส่งออกไปไหน · ใส่ชื่อเล่น/เลขที่แทนชื่อจริงก็ได้
"""
import json, os, csv, argparse, collections
def load_bank(p):
    d=json.load(open(p,encoding='utf-8'))
    return d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,list) and v and isinstance(v[0],dict))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--responses',required=True); ap.add_argument('--bank',default=os.path.join('data','bank.json'))
    ap.add_argument('--out',default='item_analysis.csv')
    a=ap.parse_args()
    key={}; nch={}
    if os.path.exists(a.bank):
        for q in load_bank(a.bank):
            if isinstance(q.get('correct'),int): key[q['id']]=q['correct']+1; nch[q['id']]=len(q.get('choices') or [])
    resp=list(csv.DictReader(open(a.responses,encoding='utf-8-sig')))
    if not resp: print('🔴 ไฟล์คำตอบว่าง'); return
    by=collections.defaultdict(dict)
    for r in resp:
        try: by[r['student']][r['id']]=int(str(r['answer']).strip())
        except Exception: continue
    ids=sorted({r['id'] for r in resp})
    unknown=[i for i in ids if i not in key]
    score={s:sum(1 for i,v in d.items() if key.get(i)==v) for s,d in by.items()}
    order=sorted(score,key=lambda s:-score[s]); k=max(1,round(len(order)*0.27))
    hi,lo=set(order[:k]),set(order[-k:])
    rows=[]
    for i in ids:
        ans=[d[i] for d in by.values() if i in d]
        if not ans: continue
        c=key.get(i); n=len(ans)
        p=sum(1 for v in ans if v==c)/n if c else None
        ph=sum(1 for s in hi if by[s].get(i)==c)/max(1,len(hi)) if c else 0
        pl=sum(1 for s in lo if by[s].get(i)==c)/max(1,len(lo)) if c else 0
        r=ph-pl if c else None
        dist=collections.Counter(ans)
        dead=[str(x) for x in range(1,(nch.get(i) or max(dist))+1) if x!=c and dist.get(x,0)==0]
        note=[]
        if p is not None:
            if p>=0.85: note.append('ง่ายมาก')
            elif p<=0.25: note.append('🔴 ยากผิดปกติ/อาจโจทย์มีปัญหา')
            if r is not None and r<0.1: note.append('🔴 อำนาจจำแนกต่ำ — เด็กเก่งกับเด็กอ่อนตอบพอกัน')
            if dead: note.append('ตัวลวงไม่มีใครเลือก: '+','.join(dead))
        rows.append([i,n,'' if p is None else f'{p:.2f}','' if r is None else f'{r:.2f}',c or '',
                     ' '.join(f'{x}:{dist.get(x,0)}' for x in sorted(dist)),' · '.join(note)])
    rows.sort(key=lambda x:(x[2] or '9'))
    with open(a.out,'w',newline='',encoding='utf-8-sig') as f:
        w=csv.writer(f); w.writerow(['id','จำนวนคนตอบ','ค่าความยาก p','อำนาจจำแนก r','เฉลย','คนเลือกแต่ละตัว','ข้อสังเกต']); w.writerows(rows)
    avg=sum(score.values())/len(score)
    print(f'นักเรียน {len(by)} คน · ข้อสอบ {len(ids)} ข้อ · คะแนนเฉลี่ย {avg:.1f}/{len(ids)}')
    print(f'ข้อที่ควรดู: ยากผิดปกติ {sum(1 for r in rows if "ยากผิดปกติ" in r[6])} · อำนาจจำแนกต่ำ {sum(1 for r in rows if "อำนาจจำแนกต่ำ" in r[6])}')
    if unknown: print(f'⚠️ ไม่พบเฉลยในคลัง {len(unknown)} ข้อ: {unknown[:5]}')
    print(f'✅ {a.out}')
if __name__=='__main__': main()

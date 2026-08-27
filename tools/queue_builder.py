#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""queue_builder.py — สร้างคิวงานเฉลย = คลัง − DONE  (ค่า token = 0)
ใช้:  python queue_builder.py --bank data\bank.json --done _t1run\results --out QUEUE_input.json
      [--topic 7] [--difficulty ยาก] [--limit 200] [--skip-image]
กติกาในตัว (POSTMORTEM §4):
  · DONE นับจากไฟล์ผลจริงทุกไฟล์ ⛔ ไม่เชื่อทะเบียนใด ๆ
  · นับจำนวนก่อนเขียนเสมอ · ถ้าคิวใหม่ว่าง = หยุด ⛔ ไม่เขียนทับ
  · เขียน DONE.json ทุกครั้งโดยไม่มีเงื่อนไข
"""
import json, os, re, sys, argparse, glob

def S(v): return v if isinstance(v,str) else json.dumps(v,ensure_ascii=False)

def load_bank(p):
    d=json.load(open(p,encoding='utf-8'))
    if isinstance(d,list): return d
    return next(v for v in d.values() if isinstance(v,list) and v and isinstance(v[0],dict))

def done_ids(paths):
    ids=set(); files=0
    for p in paths:
        cand=[p] if os.path.isfile(p) else glob.glob(os.path.join(p,'*.json'))
        for f in cand:
            try: d=json.load(open(f,encoding='utf-8'))
            except Exception: continue
            if isinstance(d,list) and d and isinstance(d[0],dict) and 'steps' in d[0]:
                ids.update(x['id'] for x in d if 'id' in x); files+=1
    return ids, files

def hint(expl, cap=700):
    if not expl: return ''
    expl = S(expl)
    out=[]
    m=re.search(r'✅\s*คำตอบ[:：]?(.{0,120}?)(?=</b>|\n)',expl,re.S)
    if m: out.append('คำตอบเดิม: '+re.sub(r'<[^>]+>','',m.group(1)).strip()[:100])
    for pat in [r'💡\s*เทคนิคที่ใช้[:：]?(.{0,400}?)(?=<b>|⚠️|$)', r'⚠️\s*จุดที่เด็กมักผิด[:：]?(.{0,400}?)(?=<b>|$)']:
        m=re.search(pat,expl,re.S)
        if m: out.append(re.sub(r'<[^>]+>','',m.group(1)).strip()[:300])
    return ' · '.join(x for x in out if x)[:cap]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bank',default=os.path.join('data','bank.json'))
    ap.add_argument('--done',nargs='*',default=[os.path.join('_t1run','results')])
    ap.add_argument('--out',default='QUEUE_input.json')
    ap.add_argument('--topic'); ap.add_argument('--difficulty')
    ap.add_argument('--limit',type=int); ap.add_argument('--skip-image',action='store_true')
    a=ap.parse_args()
    items=load_bank(a.bank); dn,nf=done_ids(a.done)
    print(f'คลัง {len(items)} ข้อ · DONE {len(dn)} ข้อ (จาก {nf} ไฟล์ผลจริง)')
    rest=[q for q in items if q.get('id') not in dn]
    if a.topic:
        t=str(a.topic); rest=[q for q in rest if t in [str(x) for x in (q.get('topics') or [q.get('topic')])]]
    if a.difficulty: rest=[q for q in rest if q.get('difficulty')==a.difficulty]
    if a.skip_image: rest=[q for q in rest if not q.get('hasImage')]
    print(f'เหลือหลังกรอง {len(rest)} ข้อ')
    if a.limit: rest=rest[:a.limit]
    lean=[{'id':q['id'],'topics':q.get('topics') or [q.get('topic')],'subTopics':q.get('subTopics'),
           'difficulty':q.get('difficulty'),'type':q.get('type'),'question':q.get('question'),
           'choices':q.get('choices'),'correct':q.get('correct'),'hasImage':bool(q.get('hasImage')),
           'hint':hint(q.get('explanation'))} for q in rest]
    if not lean:
        print('🔴 คิวใหม่ว่าง — หยุด ⛔ ไม่เขียนทับไฟล์เดิม'); sys.exit(1)
    json.dump(lean,open(a.out,'w',encoding='utf-8'),ensure_ascii=False)
    json.dump(sorted(dn),open('DONE.json','w',encoding='utf-8'),ensure_ascii=False)
    back=json.load(open(a.out,encoding='utf-8'))
    print(f'✅ เขียน {a.out} = {len(back)} ข้อ (อ่านกลับมานับแล้ว) · DONE.json = {len(dn)} id')
    print(f'   มีรูป {sum(1 for x in back if x["hasImage"])} · ไม่มีรูป {sum(1 for x in back if not x["hasImage"])}')

if __name__=='__main__': main()

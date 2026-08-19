#!/usr/bin/env python3
"""ด่านตรวจผลผลิต t1 ตามสเปก §5 — รันตอนครูกลับ
ใช้:  python3 check_t1.py <โฟลเดอร์ผลลัพธ์> <โฟลเดอร์ pack>
ออก: สรุปบนจอ + report.csv (ข้อไหนตก ตกด่านไหน)
"""
import json,re,sys,os,glob,csv
OUT=sys.argv[1] if len(sys.argv)>1 else 'out'
PK =sys.argv[2] if len(sys.argv)>2 else '.'
NEED=['id','v','kb_ref','given','goal','steps','verify','technique','traps','hints']
def norm(x):
    t = re.sub(r'\\left|\\right', '', str(x))
    t = t.replace('dfrac','frac').replace('tfrac','frac')
    return re.sub(r'[\s$\\{}()\[\]]', '', t)

src={}
for f in glob.glob(os.path.join(PK,'pack_*.json')):
    for q in json.load(open(f,encoding='utf-8')): src[q['id']]=q
rows=[];ok=0;tot=0
for f in sorted(glob.glob(os.path.join(OUT,'*.json'))):
    for d in (json.load(open(f,encoding='utf-8')) if f.endswith('.json') else []):
        if isinstance(d,str): continue
        tot+=1; s=json.dumps(d,ensure_ascii=False); q=src.get(d.get('id'),{}); bad=[]
        if not all(k in d for k in NEED): bad.append('ฟิลด์ขาด:'+','.join(k for k in NEED if k not in d))
        if 'ความรู้พื้นฐาน' in s: bad.append('มีบล็อก kb หลุด')
        if '\\(' in s or '\\[' in s: bad.append('LaTeX ผิดรูปแบบ')
        body=' '.join(d.get('given',[]))+str(d.get('goal',''))+json.dumps(d.get('steps',[]),ensure_ascii=False)
        if body.count('$')%2: bad.append('$ ไม่เป็นคู่')
        n=len(re.sub(r'[{}\[\]",]','',s))
        if not (2500<=n<=9000): bad.append('ความยาว %d'%n)
        ch=q.get('choices')
        if ch and q.get('correct') is not None:
            cor=norm(ch[q['correct']])
            last=json.dumps(d.get('steps',[])[-1:],ensure_ascii=False)+json.dumps(d.get('verify',{}),ensure_ascii=False)
            if cor and cor not in norm(last): bad.append('คำตอบไม่ตรง correct')
            dis=[norm(c) for i,c in enumerate(ch) if i!=q['correct']]
            got=[norm(t.get('got','')) for t in d.get('traps',[])]
            m=sum(1 for g in got if g in dis)
            if got and m==0: bad.append('traps ไม่ตรงตัวลวงเลย')
        if not bad: ok+=1
        rows.append({'id':d.get('id'),'ผ่าน':'✅' if not bad else '🔴','ปัญหา':' · '.join(bad),'ตัวอักษร':n})
print('ตรวจ {:,} ข้อ · ผ่าน {:,} ({:.0f}%) · ตก {:,}'.format(tot,ok,ok*100/max(tot,1),tot-ok))
c=collections=__import__('collections').Counter()
for r in rows:
    for b in r['ปัญหา'].split(' · '):
        if b: c[b.split(':')[0]]+=1
for k,v in c.most_common(): print('   {:>5}  {}'.format(v,k))
with open('report.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=['id','ผ่าน','ปัญหา','ตัวอักษร']); w.writeheader(); w.writerows(rows)
print('เขียน report.csv แล้ว')

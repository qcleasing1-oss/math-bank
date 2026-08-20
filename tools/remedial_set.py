#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""remedial_set.py — ใบงานซ่อมเสริมจากข้อที่เด็กพลาด (รายห้อง หรือ ราย 1 คน)
ใช้: python remedial_set.py --responses คำตอบ.csv [--student "เลขที่ 12"] [--n 10] [--out remedial.html]
เลือกหัวข้อย่อยที่พลาดบ่อยที่สุด แล้วดึงโจทย์ระดับง่าย-ปานกลางในหัวข้อเดียวกันมาให้ฝึกใหม่
"""
import json, os, csv, random, argparse, collections, html, datetime
def S(v): return v if isinstance(v,str) else json.dumps(v,ensure_ascii=False)
def load_bank(p):
    d=json.load(open(p,encoding='utf-8'))
    return d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,list) and v and isinstance(v[0],dict))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--responses',required=True); ap.add_argument('--bank',default=os.path.join('data','bank.json'))
    ap.add_argument('--manifest',default=os.path.join('data','manifest.json'))
    ap.add_argument('--student'); ap.add_argument('--n',type=int,default=10)
    ap.add_argument('--seed',type=int,default=None); ap.add_argument('--out',default='remedial.html')
    a=ap.parse_args()
    rnd=random.Random(a.seed)
    bank={q['id']:q for q in load_bank(a.bank)}
    sn={}
    try: sn=json.load(open(a.manifest,encoding='utf-8')).get('subTopicNames',{})
    except Exception: pass
    miss=collections.Counter(); who=set()
    for r in csv.DictReader(open(a.responses,encoding='utf-8-sig')):
        if a.student and r.get('student')!=a.student: continue
        who.add(r.get('student'))
        q=bank.get(r['id'])
        if not q or not isinstance(q.get('correct'),int): continue
        try: v=int(str(r['answer']).strip())
        except Exception: continue
        if v!=q['correct']+1:
            for s in (q.get('subTopics') or []): miss[s]+=1
    if not miss: print('🔴 ไม่พบข้อที่ตอบผิด (หรือไม่พบนักเรียนคนนี้)'); return
    used={r['id'] for r in csv.DictReader(open(a.responses,encoding='utf-8-sig'))}
    picks=[]
    for s,_ in miss.most_common():
        pool=[q for q in bank.values() if s in (q.get('subTopics') or []) and q['id'] not in used
              and q.get('difficulty') in ('ง่าย','ปานกลาง') and q.get('choices')]
        rnd.shuffle(pool)
        for q in pool[:max(1,a.n//max(1,len(miss)))]:
            if len(picks)<a.n: picks.append((s,q))
        if len(picks)>=a.n: break
    ts=datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    body=''.join(f"<li><div class=st>{html.escape(sn.get(s,s))}</div><div class=q>{html.escape(S(q['question']))}</div>"
                 f"<ol class=c>{''.join(f'<li>{html.escape(S(c))}</li>' for c in q['choices'])}</ol>"
                 f"<div class=a>เฉลย: ข้อ {q['correct']+1} <span class=i>({html.escape(q['id'])})</span></div></li>" for s,q in picks)
    top=' · '.join(f'{html.escape(sn.get(s,s))} ({n})' for s,n in miss.most_common(5))
    open(a.out,'w',encoding='utf-8').write(f"""<!doctype html><html lang=th><meta charset=utf-8><title>ใบงานซ่อมเสริม</title>
<script>window.MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}}}};</script>
<script id=MathJax-script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>body{{font-family:'Segoe UI',Tahoma,sans-serif;max-width:800px;margin:0 auto;padding:24px 20px 60px;color:#111}}
h1{{font-size:20px;margin-bottom:2px}} .sub{{color:#666;font-size:12px;margin-bottom:16px}}
ol{{padding-left:22px}} ol>li{{margin-bottom:15px}} .st{{font-size:11.5px;color:#b8763e}}
.q{{margin:3px 0}} ol.c{{padding-left:24px;margin:4px 0}}
.a{{font-size:12px;color:#2f6b3d;margin-top:4px}} .i{{color:#aaa}} @media print{{.a{{display:none}}}}</style>
<h1>ใบงานซ่อมเสริม{(' — '+html.escape(a.student)) if a.student else ' — ทั้งห้อง'}</h1>
<div class=sub>สร้างเมื่อ {ts} · จากคำตอบของ {len(who)} คน · หัวข้อที่พลาดบ่อย: {top}<br>
ชื่อ ______________________ ชั้น ______ เลขที่ ____</div>
<ol>{body}</ol></html>""")
    print(f'✅ {a.out} · {len(picks)} ข้อ · หัวข้อที่พลาดบ่อยสุด: {miss.most_common(3)}')
if __name__=='__main__': main()

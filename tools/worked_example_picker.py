#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""worked_example_picker.py — เลือกตัวอย่างสอนหน้าห้อง หัวข้อย่อยละ 1-3 ข้อ (เอาฉบับที่อธิบายครบสุด)
ใช้: python worked_example_picker.py [--per 2] [--topic 7] [--out _t1run\examples.html]
"""
import json, os, glob, argparse, collections, html, datetime
def S(v): return v if isinstance(v,str) else json.dumps(v,ensure_ascii=False)
def load_bank(p):
    d=json.load(open(p,encoding='utf-8'))
    return d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,list) and v and isinstance(v[0],dict))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bank',default=os.path.join('data','bank.json'))
    ap.add_argument('--manifest',default=os.path.join('data','manifest.json'))
    ap.add_argument('--done',nargs='*',default=[os.path.join('_t1run','results')])
    ap.add_argument('--per',type=int,default=2); ap.add_argument('--topic',nargs='*')
    ap.add_argument('--out',default=os.path.join('_t1run','examples.html'))
    a=ap.parse_args()
    bank={q['id']:q for q in load_bank(a.bank)}
    mf={}
    try: mf=json.load(open(a.manifest,encoding='utf-8'))
    except Exception: pass
    tn,sn=mf.get('topicNames',{}),mf.get('subTopicNames',{})
    recs={}
    for p in a.done:
        for f in ([p] if os.path.isfile(p) else glob.glob(os.path.join(p,'**','*.json'),recursive=True)):
            try: d=json.load(open(f,encoding='utf-8'))
            except Exception: continue
            if isinstance(d,list) and d and isinstance(d[0],dict) and 'steps' in d[0]:
                for r in d: recs[r['id']]=r
    bysub=collections.defaultdict(list)
    for i,r in recs.items():
        q=bank.get(i,{})
        if a.topic and not set(a.topic)&{str(t) for t in (q.get('topics') or [q.get('topic')])}: continue
        for s in (q.get('subTopics') or ['(ไม่มีป้าย)']): bysub[s].append(r)
    def score(r): return (len(r.get('steps',[])), len(r.get('traps',[])), len(S(r)))
    secs=[]; n=0
    for s in sorted(bysub,key=lambda x:[int(p) if str(p).isdigit() else 0 for p in str(x).split('.')]):
        best=sorted(bysub[s],key=score,reverse=True)[:a.per]; n+=len(best)
        t=str(s).split('.')[0]
        cards=[]
        for r in best:
            q=bank.get(r['id'],{})
            steps=''.join(f"<li><b>{html.escape(st.get('title',''))}</b>"
                          f"{'<div class=w>'+html.escape(st.get('eq') or '')+'</div>' if st.get('eq') else ''}</li>"
                          for st in r.get('steps',[]))
            cards.append(f"<div class=card><div class=meta>{html.escape(r['id'])} · {html.escape(q.get('difficulty',''))}</div>"
                         f"<div class=q>{html.escape(S(q.get('question','')))}</div><ol class=s>{steps}</ol>"
                         f"<div class=tech>{html.escape(' · '.join(r.get('technique',[])[:2]))}</div></div>")
        secs.append(f"<h2>{html.escape(sn.get(s,str(s)))} <span class=c>{html.escape(tn.get(t,t))} · {len(bysub[s])} ข้อในกลุ่มนี้</span></h2>"+''.join(cards))
    ts=datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    open(a.out,'w',encoding='utf-8').write(f"""<!doctype html><html lang=th><meta charset=utf-8><title>ตัวอย่างสอนหน้าห้อง</title>
<script>window.MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}}}};</script>
<script id=MathJax-script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>body{{font-family:'Segoe UI',Tahoma,sans-serif;max-width:880px;margin:0 auto;padding:26px 18px 60px;background:#faf8f5;color:#2b2b2b}}
h1{{font-size:22px;margin:0 0 4px}} .sub{{color:#8a8078;font-size:13px;margin-bottom:18px}}
h2{{font-size:15px;margin:24px 0 8px}} .c{{font-size:11.5px;color:#8a8078;font-weight:400}}
.card{{background:#fff;border:1px solid #eae4dc;border-radius:10px;padding:13px 15px;margin-bottom:9px}}
.meta{{font-size:11px;color:#a09488}} .q{{font-size:13.5px;margin:5px 0 7px}}
ol.s{{padding-left:20px;margin:0;font-size:13px}} ol.s li{{margin:3px 0}} .w{{color:#8a5a2b}}
.tech{{font-size:12px;color:#6b6259;margin-top:6px;border-top:1px dashed #eee;padding-top:5px}}
@media print{{.card{{break-inside:avoid}}}}</style>
<h1>ตัวอย่างสอนหน้าห้อง — หัวข้อย่อยละ {a.per} ข้อ</h1>
<div class=sub>สร้างเมื่อ {ts} · เลือกฉบับที่ขั้นตอน/กับดักครบที่สุด · รวม {n} ตัวอย่าง</div>{''.join(secs)}</html>""")
    print(f'✅ {a.out} · {n} ตัวอย่าง จาก {len(bysub)} หัวข้อย่อย')
if __name__=='__main__': main()

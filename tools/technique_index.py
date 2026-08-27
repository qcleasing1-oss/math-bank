#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""technique_index.py — คลังเทคนิคจากเฉลย จัดตามบท/หัวข้อย่อย (ใช้เปิดคาบสอน)
ใช้: python technique_index.py [--out _t1run\technique_index.html] [--csv _t1run\technique_index.csv]
"""
import json, os, re, glob, csv, argparse, collections, html, datetime
def S(v): return v if isinstance(v,str) else json.dumps(v,ensure_ascii=False)
def load_bank(p):
    d=json.load(open(p,encoding='utf-8'))
    return d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,list) and v and isinstance(v[0],dict))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bank',default=os.path.join('data','bank.json'))
    ap.add_argument('--manifest',default=os.path.join('data','manifest.json'))
    ap.add_argument('--done',nargs='*',default=[os.path.join('_t1run','results')])
    ap.add_argument('--out',default=os.path.join('_t1run','technique_index.html'))
    ap.add_argument('--csv',default=os.path.join('_t1run','technique_index.csv'))
    a=ap.parse_args()
    topic={}; 
    if os.path.exists(a.bank):
        for q in load_bank(a.bank): topic[q['id']]=str((q.get('topics') or [q.get('topic')])[0])
    names={}
    try: names=json.load(open(a.manifest,encoding='utf-8')).get('topicNames',{})
    except Exception: pass
    files=[]
    for p in a.done: files+=[p] if os.path.isfile(p) else glob.glob(os.path.join(p,'**','*.json'),recursive=True)
    seen=set(); reg=collections.defaultdict(dict); rows=[]
    for f in sorted(files):
        try: d=json.load(open(f,encoding='utf-8'))
        except Exception: continue
        if not(isinstance(d,list) and d and isinstance(d[0],dict) and 'steps' in d[0]): continue
        for r in d:
            if r['id'] in seen: continue
            seen.add(r['id']); t=topic.get(r['id'],'?')
            for tx in r.get('technique',[]):
                tx=(tx or '').strip()
                if len(tx)<12: continue
                k=re.sub(r'\s+','',tx)[:60]
                e=reg[t].setdefault(k,{'text':tx,'n':0,'ids':[]}); e['n']+=1
                if len(e['ids'])<5: e['ids'].append(r['id'])
                rows.append([names.get(t,t),r['id'],tx])
    with open(a.csv,'w',newline='',encoding='utf-8-sig') as f:
        w=csv.writer(f); w.writerow(['บท','id','เทคนิค']); w.writerows(rows)
    secs=[]
    for t,d in sorted(reg.items(),key=lambda kv:-len(kv[1])):
        lst=sorted(d.values(),key=lambda e:-e['n'])
        secs.append(f"<h2>{html.escape(names.get(t,t))} <span class=c>{len(lst)} เทคนิค</span></h2><ul>"+
            ''.join(f"<li>{html.escape(e['text'])}<span class=m>พบ {e['n']} ครั้ง · {html.escape(', '.join(e['ids']))}</span></li>" for e in lst)+"</ul>")
    ts=datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    open(a.out,'w',encoding='utf-8').write(f"""<!doctype html><html lang=th><meta charset=utf-8><title>คลังเทคนิค</title>
<style>body{{font-family:'Segoe UI',Tahoma,sans-serif;max-width:900px;margin:0 auto;padding:26px 18px 60px;background:#faf8f5;color:#2b2b2b}}
h1{{font-size:22px;margin:0 0 4px}} .sub{{color:#8a8078;font-size:13px;margin-bottom:18px}}
h2{{font-size:16px;margin:24px 0 8px;border-bottom:2px solid #eae4dc;padding-bottom:5px}} .c{{font-size:12px;color:#8a8078;font-weight:400}}
ul{{list-style:none;padding:0}} li{{background:#fff;border:1px solid #eae4dc;border-radius:8px;padding:9px 12px;margin-bottom:6px;font-size:13.5px}}
.m{{display:block;font-size:11px;color:#a09488;margin-top:4px}} @media print{{.m{{display:none}}}}</style>
<h1>คลังเทคนิค — จากเฉลยที่ทำแล้ว</h1><div class=sub>สร้างเมื่อ {ts} · จากเฉลย {len(seen):,} ข้อ · เทคนิคซ้ำถูกยุบ</div>
{''.join(secs)}</html>""")
    print(f'✅ {a.out} + {a.csv} · จากเฉลย {len(seen):,} ข้อ · {sum(len(d) for d in reg.values()):,} เทคนิคไม่ซ้ำ')
if __name__=='__main__': main()

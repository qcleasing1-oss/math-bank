#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""stats.py — สร้าง dashboard.html ความคืบหน้าเฉลยละเอียด (ค่า token = 0)
ใช้:  python stats.py --bank data\bank.json --manifest data\manifest.json --done _t1run\results --out dashboard.html
"""
import json, os, re, argparse, glob, collections, html, datetime

def S(v): return v if isinstance(v,str) else json.dumps(v,ensure_ascii=False)
IMG=re.compile(r'\[IMAGE[:\]]',re.I)
FIG=re.compile(r'ดูรูป|ดูตาราง|จากรูป|ตามรูป|รูปประกอบ|ตารางประกอบ|จากตาราง|ดังรูป|ดังตาราง')

def load_bank(p):
    d=json.load(open(p,encoding='utf-8'))
    return d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,list) and v and isinstance(v[0],dict))

def done_ids(paths):
    ids=set()
    for p in paths:
        for f in ([p] if os.path.isfile(p) else glob.glob(os.path.join(p,'*.json'))):
            try: d=json.load(open(f,encoding='utf-8'))
            except Exception: continue
            if isinstance(d,list) and d and isinstance(d[0],dict) and 'steps' in d[0]:
                ids.update(x['id'] for x in d if 'id' in x)
    return ids

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bank',default=os.path.join('data','bank.json'))
    ap.add_argument('--manifest',default=os.path.join('data','manifest.json'))
    ap.add_argument('--done',nargs='*',default=[os.path.join('_t1run','results')])
    ap.add_argument('--out',default='dashboard.html')
    a=ap.parse_args()
    items=load_bank(a.bank); dn=done_ids(a.done)
    names={}
    try: names=json.load(open(a.manifest,encoding='utf-8')).get('topicNames',{})
    except Exception: pass
    chap=collections.defaultdict(lambda:{'n':0,'d':0,'img':0})
    diff=collections.defaultdict(lambda:{'n':0,'d':0})
    ansimg=figmiss=flagged=0
    for q in items:
        i=q.get('id'); isdone=i in dn
        for t in (q.get('topics') or [q.get('topic')]):
            k=str(t); chap[k]['n']+=1; chap[k]['d']+=isdone
            if q.get('hasImage'): chap[k]['img']+=1
        dl=q.get('difficulty') or '(ไม่มีป้าย)'
        diff[dl]['n']+=1; diff[dl]['d']+=isdone
        if q.get('hasImage'): flagged+=1
        if IMG.search(S(q.get('explanation') or '')): ansimg+=1
        if (not q.get('hasImage')) and FIG.search(S(q.get('question') or '')): figmiss+=1
    tot=len(items); done=len(dn & {q.get('id') for q in items}); rest=tot-done
    pct=done/tot*100 if tot else 0
    rows=[]
    for k,v in sorted(chap.items(), key=lambda x:-x[1]['n']):
        p=v['d']/v['n']*100 if v['n'] else 0
        rows.append(f"<tr><td class=c>{html.escape(names.get(k,k))}</td><td class=n>{v['n']}</td>"
                    f"<td class=n>{v['d']}</td><td class=n>{v['n']-v['d']}</td><td class=n>{v['img']}</td>"
                    f"<td class=bar><div class=track><div class=fill style='width:{p:.1f}%'></div></div><span>{p:.0f}%</span></td></tr>")
    drows=''.join(f"<tr><td class=c>{html.escape(k)}</td><td class=n>{v['n']}</td><td class=n>{v['d']}</td>"
                  f"<td class=n>{v['n']-v['d']}</td><td class=n>{v['d']/v['n']*100 if v['n'] else 0:.0f}%</td></tr>"
                  for k,v in sorted(diff.items(), key=lambda x:-x[1]['n']))
    ts=datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    doc=f"""<!doctype html><html lang=th><meta charset=utf-8>
<title>ความคืบหน้าเฉลยละเอียด t1</title>
<style>
body{{font-family:'Segoe UI',Tahoma,sans-serif;margin:0;background:#faf8f5;color:#2b2b2b}}
.wrap{{max-width:1000px;margin:0 auto;padding:28px 20px 60px}}
h1{{font-size:22px;margin:0 0 4px}} .sub{{color:#8a8078;font-size:13px;margin-bottom:22px}}
.kpi{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:26px}}
.card{{flex:1;min-width:150px;background:#fff;border:1px solid #eae4dc;border-radius:10px;padding:14px 16px}}
.card .v{{font-size:26px;font-weight:600}} .card .l{{font-size:12px;color:#8a8078;margin-top:2px}}
table{{width:100%;border-collapse:collapse;background:#fff;border:1px solid #eae4dc;border-radius:10px;overflow:hidden;margin-bottom:26px}}
th,td{{padding:8px 12px;font-size:13px;border-bottom:1px solid #f2ede6;text-align:left}}
th{{background:#f6f1ea;font-weight:600;font-size:12px;color:#6b6259}}
td.n{{text-align:right;font-variant-numeric:tabular-nums;width:70px}}
td.bar{{width:180px}} .track{{display:inline-block;width:120px;height:8px;background:#efe9e1;border-radius:4px;vertical-align:middle}}
.fill{{height:8px;background:#b8763e;border-radius:4px}} td.bar span{{font-size:12px;color:#8a8078;margin-left:8px}}
h2{{font-size:15px;margin:0 0 10px}} .warn{{background:#fff6ef;border-color:#f0d9c4}}
</style><div class=wrap>
<h1>ความคืบหน้าเฉลยละเอียด t1</h1>
<div class=sub>สร้างจากไฟล์จริงเมื่อ {ts} · ตัวหาร = คลัง {tot} ข้อ · ⛔ ค่า token = 0</div>
<div class=kpi>
 <div class=card><div class=v>{tot:,}</div><div class=l>ข้อทั้งคลัง</div></div>
 <div class=card><div class=v>{done:,}</div><div class=l>มีเฉลยละเอียดแล้ว</div></div>
 <div class=card><div class=v>{rest:,}</div><div class=l>เหลือ</div></div>
 <div class=card><div class=v>{pct:.1f}%</div><div class=l>คืบหน้า</div></div>
</div>
<div class=kpi>
 <div class="card warn"><div class=v>{flagged:,}</div><div class=l>ข้อที่ติดธง hasImage</div></div>
 <div class="card warn"><div class=v>{ansimg:,}</div><div class=l>รูปอยู่ฝั่งเฉลย 🔴 เสี่ยงเฉลยรั่ว</div></div>
 <div class="card warn"><div class=v>{figmiss:,}</div><div class=l>โจทย์อ้างรูป/ตาราง แต่ไม่มีรูป 🔴 ต้องใช้ตาคน</div></div>
</div>
<h2>ตามบท</h2>
<table><tr><th>บท</th><th class=n>ทั้งหมด</th><th class=n>ทำแล้ว</th><th class=n>เหลือ</th><th class=n>มีรูป</th><th>คืบหน้า</th></tr>{''.join(rows)}</table>
<h2>ตามความยาก</h2>
<table><tr><th>ระดับ</th><th class=n>ทั้งหมด</th><th class=n>ทำแล้ว</th><th class=n>เหลือ</th><th class=n>%</th></tr>{drows}</table>
</div></html>"""
    open(a.out,'w',encoding='utf-8').write(doc)
    print(f'✅ {a.out} · คลัง {tot} · ทำแล้ว {done} ({pct:.1f}%) · เหลือ {rest}')
    print(f'   ธงมีรูป {flagged} · รูปฝั่งเฉลย {ansimg} · โจทย์อ้างรูปแต่ไม่มีรูป {figmiss}')

if __name__=='__main__': main()

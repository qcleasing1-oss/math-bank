#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""subtopic_map.py — แผนที่หัวข้อย่อย: บทไหนหัวข้อไหนมีโจทย์กี่ข้อ · ทำเฉลยแล้วกี่ข้อ · หัวข้อไหนว่าง
ใช้: python subtopic_map.py [--bank data\bank.json] [--manifest data\manifest.json] [--done _t1run\results] [--out subtopic_map.html]
"""
import json, os, glob, argparse, collections, html, datetime

def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))
def done_ids(paths):
    ids = set()
    for p in paths:
        for f in ([p] if os.path.isfile(p) else glob.glob(os.path.join(p, '**', '*.json'), recursive=True)):
            try: d = json.load(open(f, encoding='utf-8'))
            except Exception: continue
            if isinstance(d, list) and d and isinstance(d[0], dict) and 'steps' in d[0]:
                ids.update(x['id'] for x in d if 'id' in x)
    return ids

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--manifest', default=os.path.join('data', 'manifest.json'))
    ap.add_argument('--done', nargs='*', default=[os.path.join('_t1run', 'results')])
    ap.add_argument('--out', default='subtopic_map.html')
    a = ap.parse_args()
    items = load_bank(a.bank); dn = done_ids(a.done)
    mf = {}
    try: mf = json.load(open(a.manifest, encoding='utf-8'))
    except Exception: pass
    tn, sn = mf.get('topicNames', {}), mf.get('subTopicNames', {})
    dep = set(mf.get('deprecatedSubTopics', []))
    cnt = collections.Counter(); cdone = collections.Counter()
    for q in items:
        for s in (q.get('subTopics') or ['(ไม่มีป้าย)']):
            cnt[s] += 1
            if q['id'] in dn: cdone[s] += 1
    allsub = set(sn) | set(cnt)
    bytopic = collections.defaultdict(list)
    for s in allsub:
        t = str(s).split('.')[0]
        bytopic[t].append(s)
    secs = []; empty = 0
    for t in sorted(bytopic, key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else 0)):
        rows = []
        for s in sorted(bytopic[t], key=lambda x: [int(p) if p.isdigit() else 0 for p in str(x).split('.')]):
            n, d = cnt.get(s, 0), cdone.get(s, 0)
            if n == 0: empty += 1
            cls = 'z' if n == 0 else ('f' if d == n else ('p' if d else ''))
            tag = ' <span class=dep>เลิกใช้</span>' if s in dep else ''
            rows.append(f"<tr class={cls}><td>{html.escape(str(s))}</td><td>{html.escape(sn.get(s, '—'))}{tag}</td>"
                        f"<td class=n>{n}</td><td class=n>{d}</td><td class=n>{n-d}</td></tr>")
        secs.append(f"<h2>{html.escape(tn.get(t, t))} <span class=c>{len(rows)} หัวข้อย่อย</span></h2>"
                    f"<table><tr><th>รหัส</th><th>หัวข้อย่อย</th><th class=n>โจทย์</th><th class=n>มีเฉลย</th><th class=n>เหลือ</th></tr>{''.join(rows)}</table>")
    ts = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    doc = f"""<!doctype html><html lang=th><meta charset=utf-8><title>แผนที่หัวข้อย่อย</title>
<style>body{{font-family:'Segoe UI',Tahoma,sans-serif;max-width:900px;margin:0 auto;padding:26px 18px 60px;background:#faf8f5;color:#2b2b2b}}
h1{{font-size:22px;margin:0 0 4px}} .sub{{color:#8a8078;font-size:13px;margin-bottom:18px}}
h2{{font-size:15px;margin:24px 0 7px}} .c{{font-size:12px;color:#8a8078;font-weight:400}}
table{{width:100%;border-collapse:collapse;background:#fff;border:1px solid #eae4dc;border-radius:9px;overflow:hidden}}
th,td{{padding:6px 10px;font-size:13px;border-bottom:1px solid #f2ede6;text-align:left}} th{{background:#f6f1ea;font-size:12px;color:#6b6259}}
td.n{{text-align:right;width:70px;font-variant-numeric:tabular-nums}}
tr.z{{background:#fff5f5}} tr.z td:first-child{{color:#c04a4a}} tr.f{{background:#f2f9f3}} tr.p{{background:#fffaf2}}
.dep{{font-size:10px;background:#eee;padding:1px 5px;border-radius:4px;color:#888}}</style>
<h1>แผนที่หัวข้อย่อย — มีโจทย์ครบทุกหัวข้อไหม</h1>
<div class=sub>สร้างเมื่อ {ts} · 🟥 แดง = ยังไม่มีโจทย์เลย ({empty} หัวข้อ) · 🟩 เขียว = มีเฉลยครบ · 🟨 เหลือง = ทำไปบ้าง</div>
{''.join(secs)}</html>"""
    open(a.out, 'w', encoding='utf-8').write(doc)
    print(f'✅ {a.out} · หัวข้อย่อยทั้งหมด {len(allsub)} · ยังไม่มีโจทย์เลย {empty} หัวข้อ')

if __name__ == '__main__': main()

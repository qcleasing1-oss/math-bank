#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""trap_registry.py — ดึง "กับดักที่เด็กมักพลาด" จากเฉลย t1 → ทะเบียนกับดักรายบท/รายหัวข้อย่อย
ใช้: python trap_registry.py [--done _t1run\results] [--bank data\bank.json] [--manifest data\manifest.json]
                              [--out trap_registry.html] [--csv trap_registry.csv]
"""
import json, os, re, glob, csv, argparse, collections, html, datetime

def S(v): return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--done', nargs='*', default=[os.path.join('_t1run', 'results')])
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--manifest', default=os.path.join('data', 'manifest.json'))
    ap.add_argument('--out', default='trap_registry.html')
    ap.add_argument('--csv', default='trap_registry.csv')
    a = ap.parse_args()
    topic, sub = {}, {}
    if os.path.exists(a.bank):
        for q in load_bank(a.bank):
            topic[q['id']] = str((q.get('topics') or [q.get('topic')])[0])
            sub[q['id']] = ' '.join(q.get('subTopics') or [])
    names, subnames = {}, {}
    try:
        mf = json.load(open(a.manifest, encoding='utf-8'))
        names = mf.get('topicNames', {}); subnames = mf.get('subTopicNames', {})
    except Exception: pass
    files = []
    for p in a.done:
        files += [p] if os.path.isfile(p) else glob.glob(os.path.join(p, '**', '*.json'), recursive=True)
    seen = set(); reg = collections.defaultdict(list); rows = []
    for f in sorted(files):
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        if not (isinstance(d, list) and d and isinstance(d[0], dict) and 'steps' in d[0]): continue
        for r in d:
            if r['id'] in seen: continue
            seen.add(r['id'])
            t = topic.get(r['id'], '?')
            for tr in r.get('traps', []):
                why = (tr.get('why') or '').strip()
                if len(why) < 12: continue
                got = (tr.get('got') or '').strip()
                caught = (tr.get('caught_by') or '').strip()
                reg[t].append({'id': r['id'], 'why': why, 'got': got, 'caught': caught, 'sub': sub.get(r['id'], '')})
                rows.append([names.get(t, t), r['id'], ' '.join(subnames.get(s, s) for s in sub.get(r['id'], '').split() if s), got, why, caught])
    with open(a.csv, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f); w.writerow(['บท', 'id', 'หัวข้อย่อย', 'เด็กตอบผิดเป็น', 'เพราะอะไร', 'จับได้ด้วย']); w.writerows(rows)
    ts = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    secs = []
    for t, lst in sorted(reg.items(), key=lambda kv: -len(kv[1])):
        secs.append(f"<h2>{html.escape(names.get(t, t))} <span class=c>{len(lst)} กับดัก</span></h2><ul>" +
                    ''.join(f"<li><div class=w>{html.escape(e['why'])}</div>"
                            f"<div class=m>ตอบผิดเป็น: <code>{html.escape(e['got'][:80])}</code> · จับได้ด้วย: {html.escape(e['caught'][:90])} · <span class=i>{html.escape(e['id'])}</span></div></li>"
                            for e in lst) + "</ul>")
    doc = f"""<!doctype html><html lang=th><meta charset=utf-8><title>ทะเบียนกับดักรายบท</title>
<style>body{{font-family:'Segoe UI',Tahoma,sans-serif;max-width:920px;margin:0 auto;padding:26px 18px 60px;background:#faf8f5;color:#2b2b2b}}
h1{{font-size:22px;margin:0 0 4px}} .sub{{color:#8a8078;font-size:13px;margin-bottom:20px}}
h2{{font-size:16px;margin:26px 0 8px;border-bottom:2px solid #eae4dc;padding-bottom:5px}} .c{{font-size:12px;color:#8a8078;font-weight:400}}
ul{{list-style:none;padding:0;margin:0}} li{{background:#fff;border:1px solid #eae4dc;border-radius:8px;padding:10px 13px;margin-bottom:7px}}
.w{{font-size:13.5px}} .m{{font-size:11.5px;color:#8a8078;margin-top:5px}} code{{background:#f6f1ea;padding:1px 5px;border-radius:4px}}
.i{{color:#b8763e}} @media print{{body{{background:#fff}} .i{{display:none}} li{{break-inside:avoid}}}}</style>
<h1>ทะเบียนกับดัก — เด็กมักพลาดตรงไหน</h1>
<div class=sub>สร้างเมื่อ {ts} · จากเฉลย {len(seen):,} ข้อ · รวม {len(rows):,} กับดัก · ใช้เปิดคาบสอนหรือเตือนก่อนสอบ</div>
{''.join(secs)}</html>"""
    open(a.out, 'w', encoding='utf-8').write(doc)
    print(f'✅ {a.out} + {a.csv} · จากเฉลย {len(seen):,} ข้อ · {len(rows):,} กับดัก ใน {len(reg)} บท')

if __name__ == '__main__': main()

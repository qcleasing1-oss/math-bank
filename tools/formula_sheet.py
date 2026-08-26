#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""formula_sheet.py — ดึงสูตรจากเฉลย t1 ที่ทำแล้ว → ใบสรุปสูตรรายบท (HTML เปิดอ่าน/สั่งพิมพ์ได้)
ใช้: python formula_sheet.py [--done _t1run\results] [--bank data\bank.json] [--manifest data\manifest.json] [--out formula_sheet.html]
"""
import json, os, re, glob, argparse, collections, html, datetime

def S(v): return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))
def key(t):
    return re.sub(r'\s+', '', re.sub(r'\\left|\\right', '', S(t))).replace('dfrac', 'frac')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--done', nargs='*', default=[os.path.join('_t1run', 'results')])
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--manifest', default=os.path.join('data', 'manifest.json'))
    ap.add_argument('--out', default='formula_sheet.html')
    ap.add_argument('--min', type=int, default=1, help='แสดงเฉพาะสูตรที่พบอย่างน้อยกี่ครั้ง')
    a = ap.parse_args()
    topic = {}
    if os.path.exists(a.bank):
        for q in load_bank(a.bank):
            topic[q['id']] = str((q.get('topics') or [q.get('topic')])[0])
    names = {}
    try: names = json.load(open(a.manifest, encoding='utf-8')).get('topicNames', {})
    except Exception: pass
    files = []
    for p in a.done:
        files += [p] if os.path.isfile(p) else glob.glob(os.path.join(p, '**', '*.json'), recursive=True)
    seen, bank = set(), collections.defaultdict(dict)
    for f in sorted(files):
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        if not (isinstance(d, list) and d and isinstance(d[0], dict) and 'steps' in d[0]): continue
        for r in d:
            if r['id'] in seen: continue
            seen.add(r['id'])
            t = topic.get(r['id'], '?')
            for st in r.get('steps', []):
                fo = (st.get('formula') or '').strip()
                if not fo or len(fo) < 6: continue
                k = key(fo)
                e = bank[t].setdefault(k, {'text': fo, 'n': 0, 'ids': []})
                e['n'] += 1
                if len(e['ids']) < 6: e['ids'].append(r['id'])
    ts = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    secs = []
    for t, d in sorted(bank.items(), key=lambda kv: -len(kv[1])):
        rows = [e for e in sorted(d.values(), key=lambda e: -e['n']) if e['n'] >= a.min]
        if not rows: continue
        secs.append(f"<h2>{html.escape(names.get(t, t))} <span class=c>{len(rows)} สูตร</span></h2><ul>" +
                    ''.join(f"<li><span class=f>{html.escape(e['text'])}</span>"
                            f"<span class=m>พบ {e['n']} ครั้ง · {html.escape(', '.join(e['ids']))}</span></li>" for e in rows) + "</ul>")
    doc = f"""<!doctype html><html lang=th><meta charset=utf-8><title>ใบสรุปสูตรรายบท</title>
<script>window.MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}}}};</script>
<script id=MathJax-script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>body{{font-family:'Segoe UI',Tahoma,sans-serif;max-width:900px;margin:0 auto;padding:26px 18px 60px;background:#faf8f5;color:#2b2b2b}}
h1{{font-size:22px;margin:0 0 4px}} .sub{{color:#8a8078;font-size:13px;margin-bottom:20px}}
h2{{font-size:16px;margin:26px 0 8px;border-bottom:2px solid #eae4dc;padding-bottom:5px}}
.c{{font-size:12px;color:#8a8078;font-weight:400}}
ul{{list-style:none;padding:0;margin:0}} li{{background:#fff;border:1px solid #eae4dc;border-radius:8px;padding:9px 12px;margin-bottom:6px}}
.f{{display:block;font-size:14px}} .m{{display:block;font-size:11px;color:#a09488;margin-top:4px}}
@media print{{body{{background:#fff}} .m{{display:none}} li{{break-inside:avoid}}}}</style>
<h1>ใบสรุปสูตร — จากเฉลยละเอียดที่ทำแล้ว</h1>
<div class=sub>สร้างเมื่อ {ts} · จากเฉลย {len(seen):,} ข้อ · สูตรซ้ำถูกยุบเป็นบรรทัดเดียว · กด Ctrl+P เพื่อพิมพ์</div>
{''.join(secs)}</html>"""
    open(a.out, 'w', encoding='utf-8').write(doc)
    print(f'✅ {a.out} · จากเฉลย {len(seen):,} ข้อ · {sum(len(d) for d in bank.values()):,} สูตรไม่ซ้ำ ใน {len(bank)} บท')
    print('   ⚠️ ไฟล์นี้เรียกฟอนต์สูตรจากอินเทอร์เน็ต (MathJax) — เปิดตอนออนไลน์จะเห็นสูตรสวย')

if __name__ == '__main__': main()

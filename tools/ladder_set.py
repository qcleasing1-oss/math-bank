#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ladder_set.py — ชุดฝึกไล่ระดับในหัวข้อเดียวกัน (ง่าย → ปานกลาง → ยาก) สำหรับเด็กที่ตามไม่ทัน
ใช้: python ladder_set.py --topic 7 [--subtopic 7.9] [--pattern 3,4,2] [--out _t1run\ladder.html]
pattern = จำนวนข้อ ง่าย,ปานกลาง,ยาก (ค่าเริ่มต้น 3,4,2)
"""
import json, os, random, argparse, datetime, html

def S(v): return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--manifest', default=os.path.join('data', 'manifest.json'))
    ap.add_argument('--topic', nargs='*', required=True)
    ap.add_argument('--subtopic', nargs='*')
    ap.add_argument('--pattern', default='3,4,2')
    ap.add_argument('--seed', type=int, default=None)
    ap.add_argument('--skip-image', action='store_true')
    ap.add_argument('--out', default=os.path.join('_t1run', 'ladder.html'))
    a = ap.parse_args()
    rnd = random.Random(a.seed)
    items = load_bank(a.bank)
    names = {}
    try: names = json.load(open(a.manifest, encoding='utf-8')).get('topicNames', {})
    except Exception: pass
    want = dict(zip(['ง่าย', 'ปานกลาง', 'ยาก'], [int(x) for x in a.pattern.split(',')]))
    pool = {k: [] for k in want}
    for q in items:
        if not q.get('choices'): continue
        if a.skip_image and q.get('hasImage'): continue
        if not set(a.topic) & {str(t) for t in (q.get('topics') or [q.get('topic')])}: continue
        if a.subtopic and not set(a.subtopic) & set(q.get('subTopics') or []): continue
        d = q.get('difficulty')
        if d in pool: pool[d].append(q)
        elif d == 'ยากมาก': pool['ยาก'].append(q)
    secs, n = [], 0
    for lvl, k in want.items():
        got = rnd.sample(pool[lvl], min(k, len(pool[lvl])))
        n += len(got)
        if len(got) < k: print(f'⚠️ ระดับ{lvl} มีให้เลือกแค่ {len(pool[lvl])} ข้อ (ขอ {k})')
        secs.append(f"<h2>ระดับ {html.escape(lvl)} <span class=c>{len(got)} ข้อ</span></h2><ol class=q>" +
                    ''.join(f"<li><div class=t>{html.escape(S(q['question']))}</div><ol class=c>" +
                            ''.join(f"<li>{html.escape(S(c))}</li>" for c in q['choices']) +
                            f"</ol><div class=a>เฉลย: ข้อ {q['correct']+1} <span class=i>({html.escape(q['id'])})</span></div></li>"
                            for q in got) + "</ol>")
    ts = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    doc = f"""<!doctype html><html lang=th><meta charset=utf-8><title>ชุดฝึกไล่ระดับ</title>
<script>window.MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}}}};</script>
<script id=MathJax-script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>body{{font-family:'Segoe UI',Tahoma,sans-serif;max-width:800px;margin:0 auto;padding:24px 20px 60px;color:#111}}
h1{{font-size:20px;margin-bottom:2px}} .sub{{color:#666;font-size:12px;margin-bottom:16px}}
h2{{font-size:16px;margin:26px 0 8px;border-bottom:2px solid #eee;padding-bottom:5px}} .c{{font-size:12px;color:#888;font-weight:400}}
ol.q{{padding-left:22px}} ol.q>li{{margin-bottom:15px}} ol.c{{padding-left:24px;margin:4px 0}}
.a{{font-size:12px;color:#2f6b3d;margin-top:4px}} .i{{color:#aaa}}
@media print{{.a{{display:none}}}}</style>
<h1>ชุดฝึกไล่ระดับ — {html.escape(' · '.join(names.get(t, t) for t in a.topic))}</h1>
<div class=sub>สร้างเมื่อ {ts} · รวม {n} ข้อ · เรียงจากง่ายไปยาก · พิมพ์ด้วย Ctrl+P (เฉลยจะไม่ติดไปกับกระดาษ)</div>
{''.join(secs)}</html>"""
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    open(a.out, 'w', encoding='utf-8').write(doc)
    print(f'✅ {a.out} · รวม {n} ข้อ')

if __name__ == '__main__': main()

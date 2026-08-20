#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""exam_builder.py — ออกข้อสอบจากคลังตามพิมพ์เขียว + สลับชุด ก-ง + เฉลย + กระดาษคำตอบ
ใช้ (ตัวอย่าง):
  python exam_builder.py --topic 7 --n 20 --difficulty ปานกลาง ยาก --variants 2 --title "สอบกลางภาค ตรีโกณ"
ออก: _t1run\exams\<ชื่อ>_<เวลา>.html (ข้อสอบทุกชุด + เฉลย + กระดาษคำตอบ · กด Ctrl+P พิมพ์)
     และจำ id ที่เคยออกไว้ใน _t1run\exams\history.json ⇒ ครั้งหน้าจะไม่ออกซ้ำ (ปิดด้วย --allow-repeat)
"""
import json, os, re, random, argparse, datetime, html

def S(v): return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))
LET = 'กขคง จฉชญ'.replace(' ', '')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--manifest', default=os.path.join('data', 'manifest.json'))
    ap.add_argument('--topic', nargs='*', help='เลขบท เช่น 7 หรือ 7 8')
    ap.add_argument('--subtopic', nargs='*', help='รหัสหัวข้อย่อย เช่น 7.9')
    ap.add_argument('--difficulty', nargs='*', help='ง่าย ปานกลาง ยาก ยากมาก')
    ap.add_argument('--n', type=int, default=20)
    ap.add_argument('--variants', type=int, default=1, help='จำนวนชุดสลับ (ก ข ค ง)')
    ap.add_argument('--title', default='แบบทดสอบ')
    ap.add_argument('--seed', type=int, default=None)
    ap.add_argument('--skip-image', action='store_true')
    ap.add_argument('--allow-repeat', action='store_true')
    ap.add_argument('--outdir', default=os.path.join('_t1run', 'exams'))
    a = ap.parse_args()
    rnd = random.Random(a.seed)
    items = load_bank(a.bank)
    names = {}
    try: names = json.load(open(a.manifest, encoding='utf-8')).get('topicNames', {})
    except Exception: pass
    os.makedirs(a.outdir, exist_ok=True)
    hp = os.path.join(a.outdir, 'history.json')
    hist = set(json.load(open(hp, encoding='utf-8'))) if os.path.exists(hp) else set()
    pool = []
    for q in items:
        if not q.get('choices') or not isinstance(q.get('correct'), int): continue
        if a.skip_image and q.get('hasImage'): continue
        tp = [str(t) for t in (q.get('topics') or [q.get('topic')])]
        if a.topic and not set(a.topic) & set(tp): continue
        if a.subtopic and not set(a.subtopic) & set(q.get('subTopics') or []): continue
        if a.difficulty and q.get('difficulty') not in a.difficulty: continue
        if not a.allow_repeat and q['id'] in hist: continue
        pool.append(q)
    if len(pool) < a.n:
        print(f'⚠️ มีข้อให้เลือกแค่ {len(pool)} ข้อ (ขอ {a.n}) — จะออกเท่าที่มี')
    picked = rnd.sample(pool, min(a.n, len(pool)))
    if not picked: print('🔴 ไม่มีข้อที่ตรงเงื่อนไขเลย — ลองผ่อนตัวกรอง'); return
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M')
    papers = []
    for v in range(a.variants):
        qs = picked[:]
        if v: rnd.shuffle(qs)
        rows = []
        for i, q in enumerate(qs, 1):
            ch = list(enumerate(q['choices']))
            if v: rnd.shuffle(ch)
            cor = next(k for k, (oi, _) in enumerate(ch) if oi == q['correct'])
            rows.append({'n': i, 'id': q['id'], 'q': S(q['question']),
                         'ch': [S(c) for _, c in ch], 'cor': cor, 'd': q.get('difficulty', '')})
        papers.append({'v': LET[v] if v < len(LET) else str(v + 1), 'rows': rows})
    def qhtml(p):
        out = [f"<h2 class=pg>{html.escape(a.title)} — ชุด {p['v']}</h2><ol class=q>"]
        for r in p['rows']:
            out.append(f"<li><div class=t>{html.escape(r['q'])}</div><ol class=c type=1>" +
                       ''.join(f"<li>{html.escape(c)}</li>" for c in r['ch']) + "</ol></li>")
        return ''.join(out) + '</ol>'
    def key(p):
        return (f"<h2 class=pg>เฉลย — ชุด {p['v']}</h2><table class=k><tr>" +
                ''.join(f"<td>{r['n']}. <b>{r['cor']+1}</b></td>" + ("</tr><tr>" if r['n'] % 10 == 0 else '')
                        for r in p['rows']) + "</tr></table>" +
                "<div class=idl>" + ' · '.join(f"{r['n']}:{html.escape(r['id'])}" for r in p['rows']) + "</div>")
    def sheet(p):
        cells = ''.join(f"<tr><td class=no>{r['n']}</td>" + ''.join(f"<td class=b>{k+1}</td>" for k in range(len(r['ch']))) + "</tr>"
                        for r in p['rows'])
        return f"<h2 class=pg>กระดาษคำตอบ — ชุด {p['v']}</h2><div class=nm>ชื่อ ______________________ ชั้น ______ เลขที่ ____</div><table class=s>{cells}</table>"
    doc = f"""<!doctype html><html lang=th><meta charset=utf-8><title>{html.escape(a.title)}</title>
<script>window.MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}}}};</script>
<script id=MathJax-script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>body{{font-family:'Segoe UI',Tahoma,sans-serif;max-width:820px;margin:0 auto;padding:24px 20px 60px;color:#111}}
h1{{font-size:20px}} h2.pg{{font-size:17px;margin-top:36px;border-top:2px solid #ddd;padding-top:14px;page-break-before:always}}
h2.pg:first-of-type{{page-break-before:auto;border-top:none}}
ol.q{{padding-left:22px}} ol.q>li{{margin-bottom:14px}} .t{{margin-bottom:5px}}
ol.c{{padding-left:24px;margin:4px 0}} ol.c>li{{margin:2px 0}}
table.k td{{padding:3px 9px;font-size:14px}} .idl{{font-size:10px;color:#888;margin-top:10px;word-break:break-all}}
table.s{{border-collapse:collapse;margin-top:8px}} table.s td{{border:1px solid #bbb;padding:4px 10px;text-align:center;font-size:13px}}
td.no{{background:#f2f2f2;font-weight:600}} td.b{{color:#bbb}} .nm{{margin:10px 0;font-size:14px}}
.meta{{color:#666;font-size:12px;margin-bottom:10px}}
@media print{{.meta{{display:none}} .idl{{display:none}}}}</style>
<h1>{html.escape(a.title)}</h1>
<div class=meta>สร้างเมื่อ {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')} · {len(picked)} ข้อ · {a.variants} ชุด ·
เงื่อนไข: บท {','.join(names.get(t,t) for t in (a.topic or [])) or 'ทุกบท'} · ความยาก {' '.join(a.difficulty or ['ทุกระดับ'])}
{' · ข้ามข้อที่มีรูป' if a.skip_image else ''} · กด Ctrl+P เพื่อพิมพ์ (เฉลยและ id จะไม่ติดไปกับกระดาษข้อสอบ)</div>
{''.join(qhtml(p) for p in papers)}
{''.join(key(p) for p in papers)}
{''.join(sheet(p) for p in papers)}
</html>"""
    fn = os.path.join(a.outdir, f"{re.sub(r'[^ก-๙a-zA-Z0-9]+', '_', a.title)}_{stamp}.html")
    open(fn, 'w', encoding='utf-8').write(doc)
    if not a.allow_repeat:
        hist |= {q['id'] for q in picked}
        json.dump(sorted(hist), open(hp, 'w', encoding='utf-8'), ensure_ascii=False)
    json.dump([{'v': p['v'], 'ids': [r['id'] for r in p['rows']], 'key': [r['cor'] + 1 for r in p['rows']]} for p in papers],
              open(fn[:-5] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'✅ {fn}')
    print(f'   {len(picked)} ข้อ · {a.variants} ชุด · จำ id ไว้แล้ว {len(hist):,} ข้อ (ครั้งหน้าไม่ออกซ้ำ)')

if __name__ == '__main__': main()

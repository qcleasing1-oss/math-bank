# -*- coding: utf-8 -*-
"""mk_preview_3tier.py — สร้างหน้า PREVIEW ให้ครูประเมินเฉลย 3 ชั้น

จุดประสงค์ของหน้านี้คือ "ให้ครูตัดสินได้ว่ารูปแบบนี้ดีกับเด็กแค่ไหน"
จึงต้องอ่านแบบเดียวกันรวดเดียวทั้ง 20 ข้อได้ → มีปุ่มเปิดเฉพาะแบบที่ 1 / 2 / 3
"""
import json, os, re, html, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'b23'))
from methods import M

SRC = os.path.join(ROOT, 'out', 'k2-เฉลย3ชั้น-q165-q184-20ข้อ.json')
DST = os.path.join(ROOT, 'deliver', 'PREVIEW-เฉลย3ชั้น-q165-q184.html')

H_RE = re.compile(r'^<b>【 แบบที่ (\d) ▸ ([^·]+) · (.+) 】</b>$')
TIER_CSS = {1: 't1', 2: 't2', 3: 't3'}
TIER_LABEL = {1: 'แบบที่ 1 · พื้นฐาน (ละเอียด) · เด็กอ่อน',
              2: 'แบบที่ 2 · พื้นฐาน (กระชับ) · เด็กปานกลางถึงเก่ง',
              3: 'แบบที่ 3 · ⚡ ประยุกต์ · เด็กเก่ง'}

CSS = """
body{font-family:'Sarabun',system-ui,sans-serif;max-width:920px;margin:0 auto;padding:14px;background:#f6f7f9;color:#1b1b1b}
h2{margin:8px 0} .lede{background:#fff;border:1px solid #e0e0e0;border-radius:10px;padding:14px 18px;line-height:1.8}
.bar{position:sticky;top:0;z-index:9;background:#1b2a3a;color:#fff;padding:10px 12px;border-radius:10px;margin:12px 0;
     display:flex;gap:8px;flex-wrap:wrap;align-items:center;box-shadow:0 2px 8px rgba(0,0,0,.2)}
.bar b{margin-right:6px}
button{font:inherit;font-size:.88em;border:0;border-radius:16px;padding:6px 14px;cursor:pointer;background:#e9eef4;color:#1b2a3a}
button:hover{background:#fff}
button.on{outline:2px solid #ffd54f}
.card{background:#fff;border:1px solid #e0e0e0;border-radius:10px;padding:14px 18px;margin:16px 0;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.head{display:flex;gap:9px;align-items:center;margin-bottom:8px;flex-wrap:wrap}
.no{font-weight:700;font-size:1.06em} code{background:#f0f0f0;padding:2px 6px;border-radius:4px;font-size:.82em}
.chip{border-radius:12px;padding:2px 10px;font-size:.78em;background:#eceff1}
.d-ง่าย{background:#c8e6c9}.d-ปานกลาง{background:#fff3c4}.d-ยาก{background:#ffd6c4}.d-ยากมาก{background:#f3c4c4}
.chip.n3{background:#ddd0f5}.chip.n2{background:#ffe0b2}
.q{margin:8px 0;line-height:1.75;font-size:1.02em}
ol.ch{line-height:1.95} ol.ch li.ok{background:#e6f6e6;border-radius:6px;padding:2px 8px;font-weight:600}
.fillans{background:#e6f6e6;border-radius:6px;padding:6px 10px;display:inline-block;margin:6px 0}
.shared{background:#fbfcfd;border-left:3px solid #b0bec5;padding:8px 12px;margin:10px 0;line-height:1.85}
details.tier{border-radius:9px;margin:9px 0;border:1px solid #ddd;overflow:hidden}
details.tier>summary{cursor:pointer;padding:9px 13px;font-weight:600;list-style:none;display:flex;
                     justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap}
details.tier>summary::-webkit-details-marker{display:none}
.t1>summary{background:#e8f5e9;border-left:5px solid #43a047}
.t2>summary{background:#e3f2fd;border-left:5px solid #1e88e5}
.t3>summary{background:#f3e5f5;border-left:5px solid #8e24aa}
.mname{font-weight:400;font-size:.93em;opacity:.9}
.len{font-size:.78em;background:#fff;border-radius:10px;padding:2px 9px;opacity:.85;white-space:nowrap}
.body{padding:10px 14px;line-height:1.85}
.tail{background:#fffdf5;border-left:3px solid #ffb300;padding:9px 13px;margin-top:10px;line-height:1.85}
.no3{background:#fff3e0;border-left:4px solid #fb8c00;padding:9px 13px;margin:9px 0;line-height:1.8;font-size:.94em}
.toc{background:#fff;border:1px solid #e0e0e0;border-radius:10px;padding:12px 16px;line-height:2}
.toc a{text-decoration:none;color:#1b2a3a;border-bottom:1px dotted #999}
@media(max-width:600px){body{padding:8px}.card{padding:11px 12px}.body{padding:8px 10px}}
"""

JS = """
function only(n){
  document.querySelectorAll('details.tier').forEach(function(d){
    d.open = (n===0) ? true : (n===-1 ? false : d.classList.contains('t'+n));
  });
  document.querySelectorAll('.bar button').forEach(function(b){b.classList.remove('on');});
  var id = {0:'bAll','-1':'bNone',1:'b1',2:'b2',3:'b3'}[n];
  var el = document.getElementById(id); if(el) el.classList.add('on');
}
"""


def esc(s):
    return html.escape(s, quote=False)


def main():
    d = json.load(open(SRC, encoding='utf-8'))
    qs = d['questions']
    n3 = sum(1 for q in qs if any(l.startswith('<b>【 แบบที่ 3') for l in q['explanation']))

    P = ['<!doctype html><html lang="th"><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         '<title>PREVIEW · เฉลย 3 ชั้น · q165–q184</title>',
         '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">',
         '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>',
         '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"'
         ' onload="renderMathInElement(document.body,{delimiters:[{left:\'$\',right:\'$\',display:false}],'
         'throwOnError:false})"></script>',
         f'<style>{CSS}</style><script>{JS}</script></head><body>',
         '<h2>PREVIEW · เฉลย 3 ชั้น · ตรีโกณมิติ q165–q184 (20 ข้อ)</h2>',
         '<div class="lede">'
         '<b>สิ่งที่ครูสั่ง</b> — ทำเฉลยทั้ง 3 แบบใน 1 ข้อ ถ้าข้อไหนไม่มีประยุกต์ก็ทำ 2 แบบ<br>'
         '<b>ที่ทำมา</b> — 20 ข้อที่เพิ่งแต่งใหม่ (ก้อน 23) · '
         f'มีครบ 3 แบบ <b>{n3}</b> ข้อ · มี 2 แบบ <b>{20 - n3}</b> ข้อ<br>'
         '<b>🔴 กติกาที่ยึด</b> — แบบที่ 1 กับแบบที่ 2 เป็น <b>วิธีเดียวกัน</b> ต่างกันแค่ความละเอียด '
         'จึงใช้ <b>ชื่อวิธีเดียวกันเป๊ะ</b> · แบบที่ 3 ต้องเป็นวิธีคนละวิธีจริง '
         '⛔ ถ้าวิธีที่สองเป็นแค่วิธีเดิมที่เขียนสั้นลง หรือยาวกว่าเดิม จะไม่นับเป็นประยุกต์ และทำแค่ 2 แบบ<br>'
         '<b>ชื่อวิธี</b> — ไทยนำ อังกฤษในวงเล็บ ตามที่ครูสั่ง · หัว 【 】 ยาวไม่เกิน 109 ตัวอักษร '
         '(ของเดิมยาวถึง 383)<br>'
         '<b>ตรวจแล้ว</b> — เส้นทางของแบบที่ 3 ทุกข้อผ่าน sympy 102 เช็ก ตก 0 · '
         'ด่านโครงสร้าง 20/20 · selftest ของด่านเอง 15/15<br>'
         '<b>⛔ ไม่ได้แตะ</b> โจทย์ ตัวเลือก เฉลย หรือคำตอบที่รับได้ ของข้อใดเลย</div>',
         '<div class="bar"><b>อ่านทีละแบบ:</b>'
         '<button id="b1" onclick="only(1)">เฉพาะแบบที่ 1 · เด็กอ่อน</button>'
         '<button id="b2" onclick="only(2)">เฉพาะแบบที่ 2 · ปานกลาง</button>'
         '<button id="b3" onclick="only(3)">เฉพาะแบบที่ 3 · ⚡ ประยุกต์</button>'
         '<button id="bAll" onclick="only(0)">เปิดทั้งหมด</button>'
         '<button id="bNone" onclick="only(-1)">ปิดทั้งหมด</button></div>']

    toc = []
    for i, q in enumerate(qs, 1):
        qid = q['id'][-4:]
        has3 = any(l.startswith('<b>【 แบบที่ 3') for l in q['explanation'])
        toc.append(f'<a href="#{qid}">{i}. {qid}</a> {"🟪" if has3 else "🟧"}')
    P.append('<div class="toc"><b>สารบัญ</b> · 🟪 = มี 3 แบบ · 🟧 = มี 2 แบบ<br>' +
             ' &nbsp;·&nbsp; '.join(toc) + '</div>')

    for i, q in enumerate(qs, 1):
        qid = q['id'][-4:]
        ex = q['explanation']
        hi = [k for k, l in enumerate(ex) if l.startswith('<b>【')]
        ti = next(k for k, l in enumerate(ex) if l.startswith('✔ <b>ตรวจคำตอบ'))
        shared, tail = ex[:hi[0]], ex[ti:]
        has3 = len(hi) == 3

        P.append(f'<section class="card" id="{qid}"><div class="head">'
                 f'<span class="no">ข้อ {i}</span><code>{esc(q["id"])}</code>'
                 f'<span class="chip d-{q["difficulty"]}">{q["difficulty"]}</span>'
                 f'<span class="chip">{q["type"]}</span>'
                 f'<span class="chip">{" · ".join(q["subTopics"])}</span>'
                 f'<span class="chip {"n3" if has3 else "n2"}">{"3 แบบ" if has3 else "2 แบบ"}</span>'
                 f'</div>')
        P.append(f'<div class="q">{q["question"]}</div>')
        if q['type'] == 'mc':
            P.append('<ol class="ch">' + ''.join(
                f'<li class="{"ok" if k == q["correct"] else ""}">{c}</li>'
                for k, c in enumerate(q['choices'])) + '</ol>')
        else:
            P.append(f'<div class="fillans">ตอบ: <b>{esc(str(q["correct"]))}</b></div>')

        P.append('<div class="shared">' + '<br>\n'.join(shared) + '</div>')

        for k, s in enumerate(hi):
            e_ = hi[k + 1] if k + 1 < len(hi) else ti
            m = H_RE.match(ex[s])
            n = int(m.group(1))
            body = ex[s + 1:e_]
            nch = sum(len(x) for x in body)
            P.append(f'<details class="tier {TIER_CSS[n]}"><summary>'
                     f'<span>{TIER_LABEL[n]}<br><span class="mname">{m.group(3)}</span></span>'
                     f'<span class="len">{nch:,} ตัวอักษร</span></summary>'
                     f'<div class="body">' + '<br>\n'.join(body) + '</div></details>')

        if not has3:
            why = M[qid][3] or ''
            P.append(f'<div class="no3"><b>🟧 ข้อนี้ทำ 2 แบบ · เหตุผล</b><br>{why}</div>')

        P.append('<div class="tail">' + '<br>\n'.join(tail) + '</div></section>')

    P.append('<script>only(0)</script></body></html>')
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, 'w', encoding='utf-8').write('\n'.join(P))
    print(f'เขียน {DST}  ({os.path.getsize(DST):,} ไบต์)')


if __name__ == '__main__':
    main()

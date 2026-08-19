#!/usr/bin/env python3
"""แปลงผลลัพธ์ t1 (JSON) → HTML ตามรูปแบบที่ครูอนุมัติ
ใช้: python3 render_t1.py <ไฟล์ผลลัพธ์.json> <pack ที่มีโจทย์> <out.html>"""
import json,sys,html
res=json.load(open(sys.argv[1],encoding='utf-8'))
src={q['id']:q for q in json.load(open(sys.argv[2],encoding='utf-8'))}
CSS="""body{margin:0;background:#eef2f5;font-family:'Sarabun','Noto Sans Thai',system-ui,sans-serif;line-height:1.85;font-size:17px;color:#1f2933}
.p{max-width:740px;margin:0 auto;padding:16px 14px 60px}
.card{background:#fff;border:1px solid #dfe6ec;border-radius:14px;padding:20px 22px;margin-bottom:18px}
.qh{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:10px;font-size:.8em;color:#5b6b7a}
.qh b{font-size:1.3em;color:#1f2933}
.pill{background:#eef2f5;border-radius:12px;padding:2px 10px}
.qt{background:#f7fafc;border-left:4px solid #1b6fb8;padding:12px 14px;border-radius:0 8px 8px 0;margin:0 0 10px}
.ch{list-style:none;padding:0;margin:0 0 14px;font-size:.95em}
.ch li{padding:5px 10px;border:1px solid #eef3f7;border-radius:8px;margin:4px 0}
.ch li.ok{background:#eef7ee;border-color:#a5d6a7;font-weight:600}
.band{margin:20px 0 8px;font-size:.76em;letter-spacing:.08em;color:#8a99a8;border-top:1px solid #dfe6ec;padding-top:8px}
.goal{background:#eef7ee;border-left:4px solid #66bb6a;padding:10px 14px;border-radius:0 8px 8px 0;margin:0 0 10px}
details{border:1px solid #dfe6ec;border-radius:10px;margin:8px 0;background:#fff}
summary{cursor:pointer;list-style:none;padding:10px 14px;font-weight:600;font-size:.97em}
summary::-webkit-details-marker{display:none} summary::before{content:"▸ ";color:#1b6fb8}
details[open]>summary::before{content:"▾ "}
.bd{padding:12px 15px;border-top:1px solid #eef3f7}
ul.l{list-style:none;margin:4px 0;padding:0} ul.l>li{position:relative;padding-left:16px;margin:6px 0}
ul.l>li::before{content:"•";position:absolute;left:2px;color:#1b6fb8;font-weight:700}
.imp{border-left:3px solid #c9d6e2;padding:2px 0 2px 12px;margin:5px 0;color:#41505e;font-size:.95em}
.eq{margin:9px 0;padding:10px 12px;background:#f7fafc;border-radius:8px;text-align:center;overflow-x:auto}
ol.st{list-style:none;counter-reset:s;padding:0;margin:0}
ol.st>li{counter-increment:s;position:relative;padding:2px 0 2px 40px;margin:0 0 18px}
ol.st>li::before{content:counter(s);position:absolute;left:0;top:3px;width:27px;height:27px;border-radius:50%;background:#1b6fb8;color:#fff;font-size:.82em;font-weight:700;display:flex;align-items:center;justify-content:center}
ol.st>li::after{content:"";position:absolute;left:13px;top:34px;bottom:-14px;width:2px;background:#dfe6ec}
ol.st>li:last-child::after{display:none}
.stt{font-weight:600;margin:0 0 5px} .lbl{font-size:.76em;background:#eef2f5;color:#5b6b7a;border-radius:4px;padding:1px 7px;margin-right:5px}
.why{background:#fffaf0;border-left:3px solid #ffcc80;padding:7px 11px;border-radius:0 6px 6px 0;margin:6px 0;font-size:.95em;color:#6d4b12}
.ck{background:#f2faf3;border-left:3px solid #a5d6a7;border-radius:0 6px 6px 0;padding:7px 11px;margin:6px 0;font-size:.93em}
table.tr{width:100%;border-collapse:collapse;font-size:.9em}
table.tr th{background:#f7fafc;text-align:left;padding:7px 9px;border-bottom:2px solid #dfe6ec;font-size:.88em;color:#5b6b7a}
table.tr td{padding:8px 9px;border-bottom:1px solid #eef3f7;vertical-align:top}
table.tr td:first-child{white-space:nowrap;font-weight:600}
.hint{border-top:1px dashed #ffd9a0;padding:8px 2px;font-size:.94em}
.hw{border:1px solid #ffd9a0;background:#fffbf3;border-radius:12px;padding:10px 14px;margin:14px 0}
.kb{font-size:.8em;color:#1565c0;background:#e3f2fd;border-radius:10px;padding:2px 10px;display:inline-block;margin:6px 0}"""
import re as _re
def esc(x):
    t=html.escape(str(x),quote=False)
    t=_re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    return t
def ul(items): return '<ul class="l">'+''.join('<li>%s</li>'%esc(i) for i in items)+'</ul>' if items else ''
out=[]
for d in res:
    q=src.get(d.get('id'),{})
    ch=q.get('choices') or []
    chh=''.join('<li class="%s">%s %s</li>'%('ok' if i==q.get('correct') else '','กขคงจ'[i] if i<5 else '',esc(c)) for i,c in enumerate(ch))
    steps=''
    for s in d.get('steps',[]):
        steps+='<li><p class="stt">%s</p>'%esc(s.get('title',''))
        if s.get('formula'): steps+='<div><span class="lbl">สูตรที่ใช้</span>%s</div>'%esc(s['formula'])
        if s.get('why'): steps+='<div class="why"><b>ทำไม</b> %s</div>'%esc(s['why'])
        steps+=ul(s.get('work',[]))
        if s.get('eq'): steps+='<div class="eq">%s</div>'%esc(s['eq'])
        if s.get('check'): steps+='<div class="ck">%s</div>'%esc(s['check'])
        steps+='</li>'
    traps=''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>'%(esc(t.get('got','')),esc(t.get('why','')),esc(t.get('caught_by',''))) for t in d.get('traps',[]))
    hints=''.join('<details class="hint"><summary>ใบ้ที่ %d</summary><div class="bd">%s</div></details>'%(i+1,esc(h)) for i,h in enumerate(d.get('hints',[])))
    v=d.get('verify',{})
    out.append(f"""<div class="card">
<div class="qh"><b>{esc(d.get('id'))}</b><span class="pill">{esc(q.get('difficulty',''))}</span><span class="pill">{esc(q.get('type',''))}</span></div>
<div class="qt">{esc(q.get('question',''))}</div><ul class="ch">{chh}</ul>
<div class="band">ก่อนลงมือ</div>
<div class="goal"><b>🎯 เป้าหมาย</b> {esc(d.get('goal',''))}</div>
<div class="kb">📚 ความรู้พื้นฐาน: การ์ด {esc(' · '.join(d.get('kb_ref',[])))} <i>(เสียบทีหลัง)</i></div>
<details><summary>📐 โจทย์กำหนด</summary><div class="bd">{ul(d.get('given',[]))}</div></details>
<div class="hw"><b>💡 ติดตรงไหน — เปิดทีละใบ้</b>{hints}</div>
<details open><summary>📖 วิธีทำ</summary><div class="bd"><ol class="st">{steps}</ol></div></details>
<div class="band">หลังทำเสร็จ</div>
<details><summary>✔️ ตรวจคำตอบด้วยวิธีอิสระ</summary><div class="bd"><div class="imp">{esc(v.get('how',''))}</div>{ul(v.get('lines',[]))}<div class="ck">{esc(v.get('result',''))}</div></div></details>
<details><summary>💡 เทคนิค</summary><div class="bd">{ul(d.get('technique',[]))}</div></details>
<details><summary>⚠️ จุดพลาด ({len(d.get('traps',[]))} เส้นทาง)</summary><div class="bd"><table class="tr"><thead><tr><th>ได้คำตอบ</th><th>เพราะพลาดตรงไหน</th><th>ด่านที่จับได้</th></tr></thead><tbody>{traps}</tbody></table></div></details>
</div>""")
open(sys.argv[3],'w',encoding='utf-8').write(f"""<!DOCTYPE html><html lang="th"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>ตัวอย่าง t1</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css"><style>{CSS}</style></head>
<body><div class="p"><div style="background:#12212f;color:#fff;padding:12px 16px;border-radius:0 0 10px 10px;margin:0 -14px 16px">
<b>ตัวอย่างผลผลิต t1</b><div style="font-size:.78em;color:#9fb6c9">สร้างจาก JSON ตามสเปก · ⛔ ยังไม่มีบล็อกความรู้พื้นฐาน (รอการ์ด)</div></div>
{''.join(out)}</div>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script>document.addEventListener('DOMContentLoaded',()=>renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}],throwOnError:false}}));</script>
</body></html>""")
print("เขียน",sys.argv[3])

# -*- coding: utf-8 -*-
"""สร้างไฟล์ HTML ให้ครูตรวจ — รวมทุกข้อที่แต่งไปแล้วจาก k1/out + k2/out ไว้ที่เดียว

ทุกข้อในรอบนี้ hasImage = false ⇒ ไม่ต้องใช้ renderers.js เลย
(กฎ: ⛔ ไม่ใช้ renderer ที่ยังไม่ deploy)

สิ่งที่ครูต้องเห็นครบในไฟล์เดียว
  · โจทย์ · ตัวเลือกทั้งสี่ (ตัวถูกไฮไลต์) · เฉลยเต็มตามรูปแบบ STANDARD v2
  · ป้ายระดับความยาก · หัวข้อย่อย · ช่องคำตอบ · แผนที่กับดัก (notes)
  · ตัวกรองด้านบน กดเลือกดูเฉพาะระดับ/หัวข้อย่อยที่อยากตรวจได้
  · ปุ่มพับเฉลย เผื่อครูอยากลองทำเองก่อนดูเฉลย
"""
import io, json, glob, os, html, re, sys

SRC = ['/home/claude/k1/out/*.json', '/home/claude/k2/out/*.json']
OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/k2/ตรวจข้อสอบตรีโกณ.html'

# ── รวบรวมทุกข้อ เรียงตาม questionNumber ──────────────────────────────
items = []
for pat in SRC:
    for p in sorted(glob.glob(pat)):
        if os.path.basename(p).startswith('_'):
            continue
        d = json.load(io.open(p, encoding='utf-8'))
        for q in d['questions']:
            q['_file'] = os.path.basename(p)
            items.append(q)
items.sort(key=lambda q: q['questionNumber'])


def esc_keep_b(t):
    """หนีอักขระ HTML แต่คง <b> ไว้ เพราะรูปแบบ STANDARD v2 ใช้ <b> เป็นหัวบล็อก"""
    if isinstance(t, list):
        t = '\n'.join(t)
    t = html.escape(t, quote=False)
    t = t.replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>')
    return t.replace('\n', '<br>')


LV = ['ง่าย', 'ปานกลาง', 'ยาก', 'ยากมาก']
LVCLS = {'ง่าย': 'lv1', 'ปานกลาง': 'lv2', 'ยาก': 'lv3', 'ยากมาก': 'lv4'}
subs = sorted({s for q in items for s in q['subTopics']},
              key=lambda s: [int(x) for x in s.split('.')])

cnt_lv = {l: sum(1 for q in items if q['difficulty'] == l) for l in LV}
cnt_ch = {c: sum(1 for q in items if q['correct'] == c - 1) for c in (1, 2, 3, 4)}

CSS = """
*{box-sizing:border-box}
body{font-family:'Sarabun','Noto Sans Thai',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
     margin:0;background:#f4f5f7;color:#1a1a1a;line-height:1.75}
header{position:sticky;top:0;z-index:20;background:#1f2a44;color:#fff;padding:14px 22px 12px;
       box-shadow:0 2px 10px rgba(0,0,0,.18)}
header h1{margin:0 0 4px;font-size:19px;font-weight:700}
.sum{font-size:13px;opacity:.9}
.bar{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px;align-items:center}
.bar b{font-size:12px;opacity:.75;margin-right:2px;font-weight:600}
.chip{border:1px solid rgba(255,255,255,.4);background:transparent;color:#fff;border-radius:999px;
      padding:3px 11px;font-size:12.5px;cursor:pointer;font-family:inherit}
.chip.on{background:#fff;color:#1f2a44;border-color:#fff;font-weight:700}
.wrap{max-width:1000px;margin:0 auto;padding:18px 16px 80px}
.card{background:#fff;border-radius:12px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,.09);
      overflow:hidden;border:1px solid #e3e5ea}
.hd{display:flex;flex-wrap:wrap;gap:7px;align-items:center;padding:11px 16px;
    background:#fafbfc;border-bottom:1px solid #eceef2}
.no{font-weight:800;font-size:16px;color:#1f2a44;margin-right:3px}
.tag{font-size:11.5px;padding:2px 9px;border-radius:999px;background:#eef1f6;color:#41506b;font-weight:600}
.lv1{background:#e3f5e8;color:#1d6b33}.lv2{background:#e6effb;color:#1d4f96}
.lv3{background:#fdefe0;color:#9a5410}.lv4{background:#fce4e4;color:#a32222}
.ans{background:#1f2a44;color:#fff}
.q{padding:15px 18px 4px;font-size:16.5px}
.ch{list-style:none;margin:6px 0 12px;padding:0 18px}
.ch li{border:1px solid #e0e3e9;border-radius:9px;padding:8px 13px;margin:6px 0;background:#fff;
       display:flex;gap:9px;align-items:flex-start}
.ch li.ok{border-color:#2e9e4f;background:#f2fbf5}
.k{font-weight:800;color:#7b8598;min-width:20px}
.ch li.ok .k{color:#2e9e4f}
.tick{margin-left:auto;color:#2e9e4f;font-weight:800}
.exbtn{margin:0 18px 14px;border:1px solid #ccd2dd;background:#fff;border-radius:8px;
       padding:6px 14px;font-size:13.5px;cursor:pointer;font-family:inherit;color:#33415c;font-weight:600}
.exbtn:hover{background:#f3f5f9}
.ex{margin:0 18px 16px;padding:14px 16px;background:#fbfcfd;border:1px solid #e6e9ef;
    border-left:4px solid #1f2a44;border-radius:8px;font-size:15px}
.nt{margin:0 18px 16px;padding:11px 14px;background:#fff9ec;border:1px solid #f0e3c4;
    border-radius:8px;font-size:12.5px;color:#6a5525;line-height:1.65;word-break:break-word}
.nt b{color:#4a3a12}
.hide{display:none}
#empty{text-align:center;color:#7b8598;padding:50px;font-size:15px}
"""

JS = """
function apply(){
  var lv=[].slice.call(document.querySelectorAll('.f-lv.on')).map(function(e){return e.dataset.v});
  var st=[].slice.call(document.querySelectorAll('.f-st.on')).map(function(e){return e.dataset.v});
  var an=[].slice.call(document.querySelectorAll('.f-an.on')).map(function(e){return e.dataset.v});
  var n=0;
  [].slice.call(document.querySelectorAll('.card')).forEach(function(c){
    var okL=!lv.length||lv.indexOf(c.dataset.lv)>=0;
    var okS=!st.length||st.some(function(s){return c.dataset.st.split(',').indexOf(s)>=0});
    var okA=!an.length||an.indexOf(c.dataset.an)>=0;
    var show=okL&&okS&&okA;
    c.classList.toggle('hide',!show); if(show)n++;
  });
  document.getElementById('n').textContent=n;
  document.getElementById('empty').classList.toggle('hide',n>0);
}
document.addEventListener('click',function(e){
  var t=e.target;
  if(t.classList.contains('chip')){t.classList.toggle('on');apply();}
  if(t.classList.contains('exbtn')){
    var b=document.getElementById(t.dataset.t);
    var open=b.classList.toggle('hide');
    t.textContent=open?'▸ ดูเฉลยเต็ม':'▾ พับเฉลย';
  }
  if(t.id==='allex'){
    var any=!!document.querySelector('.ex.hide');
    [].slice.call(document.querySelectorAll('.ex')).forEach(function(b){b.classList.toggle('hide',!any)});
    [].slice.call(document.querySelectorAll('.exbtn')).forEach(function(b){
      b.textContent=any?'▾ พับเฉลย':'▸ ดูเฉลยเต็ม'});
    t.textContent=any?'พับเฉลยทั้งหมด':'กางเฉลยทั้งหมด';
  }
  if(t.id==='clr'){
    [].slice.call(document.querySelectorAll('.chip.on')).forEach(function(c){c.classList.remove('on')});
    apply();
  }
});
"""

o = []
o.append('<!doctype html><html lang="th"><head><meta charset="utf-8">')
o.append('<meta name="viewport" content="width=device-width,initial-scale=1">')
o.append('<title>ตรวจข้อสอบตรีโกณมิติ · %d ข้อ</title>' % len(items))
o.append('<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;800&display=swap" rel="stylesheet">')
# ⭐ ฝัง MathJax ลงในไฟล์เลย (ฉบับ SVG ไม่ต้องโหลดฟอนต์เพิ่ม)
# ⇒ ครูเปิดไฟล์ได้แม้ไม่มีเน็ต และไม่ต้องพึ่ง CDN ที่บางเครือข่ายบล็อก
MJ = '/home/claude/k2/node_modules/mathjax/es5/tex-svg.js'
o.append('<script>window.MathJax={tex:{inlineMath:[["$","$"]],displayMath:[["$$","$$"]]},'
         'svg:{fontCache:"global"},'
         'options:{skipHtmlTags:["script","noscript","style","textarea"]}};</script>')
o.append('<script>%s</script>' % io.open(MJ, encoding='utf-8').read())
o.append('<style>%s</style></head><body>' % CSS)

o.append('<header><h1>ตรวจข้อสอบตรีโกณมิติ (บทที่ 7) · แต่งใหม่</h1>')
o.append('<div class="sum">แสดงอยู่ <b id="n">%d</b> จาก %d ข้อ &nbsp;·&nbsp; %s '
         '&nbsp;·&nbsp; ช่องคำตอบ %s</div>'
         % (len(items), len(items),
            ' · '.join('%s %d' % (l, cnt_lv[l]) for l in LV),
            '/'.join(str(cnt_ch[c]) for c in (1, 2, 3, 4))))
o.append('<div class="bar"><b>ระดับ</b>')
for l in LV:
    o.append('<button class="chip f-lv" data-v="%s">%s (%d)</button>' % (l, l, cnt_lv[l]))
o.append('</div><div class="bar"><b>หัวข้อย่อย</b>')
for s in subs:
    c = sum(1 for q in items if s in q['subTopics'])
    o.append('<button class="chip f-st" data-v="%s">%s (%d)</button>' % (s, s, c))
o.append('</div><div class="bar"><b>ช่องคำตอบ</b>')
for c in (1, 2, 3, 4):
    o.append('<button class="chip f-an" data-v="%d">%d (%d)</button>' % (c, c, cnt_ch[c]))
o.append('<button class="chip" id="clr">ล้างตัวกรอง</button>')
o.append('<button class="chip" id="allex">กางเฉลยทั้งหมด</button>')
o.append('</div></header><div class="wrap">')

for k, q in enumerate(items):
    n = q['questionNumber']
    o.append('<div class="card" data-lv="%s" data-st="%s" data-an="%d">'
             % (q['difficulty'], ','.join(q['subTopics']), q['correct'] + 1))
    o.append('<div class="hd"><span class="no">ข้อ %d</span>' % n)
    o.append('<span class="tag %s">%s</span>' % (LVCLS[q['difficulty']], q['difficulty']))
    for s in q['subTopics']:
        o.append('<span class="tag">%s</span>' % s)
    o.append('<span class="tag ans">เฉลย ตัวเลือก %d</span>' % (q['correct'] + 1))
    o.append('<span class="tag">%s</span></div>' % html.escape(q['id']))

    o.append('<div class="q">%s</div>' % esc_keep_b(q['question']))
    o.append('<ul class="ch">')
    for j, c in enumerate(q['choices']):
        ok = ' ok' if j == q['correct'] else ''
        tick = '<span class="tick">✓ เฉลย</span>' if j == q['correct'] else ''
        o.append('<li class="%s"><span class="k">%d.</span><span>%s</span>%s</li>'
                 % (ok.strip(), j + 1, esc_keep_b(c), tick))
    o.append('</ul>')

    o.append('<button class="exbtn" data-t="ex%d">▸ ดูเฉลยเต็ม</button>' % k)
    o.append('<div class="ex hide" id="ex%d">%s</div>' % (k, esc_keep_b(q['explanation'])))
    if q.get('notes'):
        o.append('<div class="nt"><b>บันทึกผู้แต่ง (แผนที่กับดัก · การตรวจสอบ · เหตุผลไม่ซ้ำของเก่า)</b><br>%s</div>'
                 % esc_keep_b(q['notes']))
    o.append('</div>')

o.append('<div id="empty" class="hide">ไม่มีข้อที่ตรงกับตัวกรอง</div>')
o.append('</div><script>%s</script></body></html>' % JS)

doc = '\n'.join(o)
io.open(OUT, 'w', encoding='utf-8', newline='\n').write(doc)
print('เขียน %s · %d ข้อ · %d B' % (os.path.basename(OUT), len(items), len(doc.encode('utf-8'))))

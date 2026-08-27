#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""reveal_viewer.py — หน้าเปิดเฉลยทีละขั้น (ใช้สอนหน้าห้อง / ให้เด็กลองก่อนดูเฉลย)
ใช้: python reveal_viewer.py [--master _t1run\results\t1_MASTER.json] [--bank data\bank.json] [--out _t1run\reveal.html] [--limit 400]
"""
import json, os, argparse, datetime, html

def S(v): return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--master', default=os.path.join('_t1run', 'results', 't1_MASTER.json'))
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--out', default=os.path.join('_t1run', 'reveal.html'))
    ap.add_argument('--limit', type=int, default=400)
    a = ap.parse_args()
    recs = json.load(open(a.master, encoding='utf-8'))[:a.limit]
    bank = {q['id']: q for q in load_bank(a.bank)} if os.path.exists(a.bank) else {}
    data = []
    for r in recs:
        q = bank.get(r['id'], {})
        data.append({'id': r['id'], 'set': q.get('setId', ''), 'd': q.get('difficulty', ''),
                     'q': S(q.get('question', '')), 'ch': [S(c) for c in (q.get('choices') or [])],
                     'cor': q.get('correct'), 'goal': r.get('goal', ''),
                     'steps': [{'t': s.get('title', ''), 'f': s.get('formula') or '', 'w': s.get('work') or [],
                                'e': s.get('eq') or '', 'y': s.get('why') or ''} for s in r.get('steps', [])],
                     'hints': r.get('hints', []), 'traps': [{'g': t.get('got', ''), 'w': t.get('why', '')} for t in r.get('traps', [])]})
    ts = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    doc = """<!doctype html><html lang=th><meta charset=utf-8><title>เฉลยเปิดทีละขั้น</title>
<script>window.MathJax={tex:{inlineMath:[['$','$']],displayMath:[['$$','$$']]}};</script>
<script id=MathJax-script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>body{font-family:'Segoe UI',Tahoma,sans-serif;max-width:860px;margin:0 auto;padding:22px 18px 70px;background:#faf8f5;color:#2b2b2b}
h1{font-size:21px;margin:0 0 3px} .sub{color:#8a8078;font-size:12px;margin-bottom:16px}
select,input,button{font:inherit;padding:7px 11px;border:1px solid #ddd5cb;border-radius:7px;background:#fff}
button{cursor:pointer;background:#b8763e;color:#fff;border-color:#b8763e}
.box{background:#fff;border:1px solid #eae4dc;border-radius:11px;padding:18px 20px;margin-top:14px}
.q{font-size:15px;margin-bottom:10px} ol.c{padding-left:22px} ol.c li{margin:3px 0}
.step{border-left:3px solid #e5d9c8;padding:8px 0 8px 14px;margin:12px 0;display:none}
.step.on{display:block} .st{font-weight:600;font-size:14px} .why{color:#8a8078;font-size:12.5px;margin:3px 0}
.work div{margin:2px 0} .eq{background:#f6f1ea;padding:5px 9px;border-radius:6px;display:inline-block;margin-top:5px}
.meta{font-size:12px;color:#8a8078}.hint{background:#fffaf0;border:1px solid #f0e2c8;border-radius:8px;padding:9px 12px;margin-top:10px;font-size:13px;display:none}
.trap{background:#fff4f4;border:1px solid #f2d6d6;border-radius:8px;padding:9px 12px;margin-top:8px;font-size:13px;display:none}
.row{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}</style>
<h1>เฉลยเปิดทีละขั้น</h1><div class=sub>สร้างเมื่อ __TS__ · __N__ ข้อ · ให้เด็กลองก่อน แล้วค่อยกดเปิดทีละขั้น</div>
<div class=row><input id=f placeholder="ค้นหา id / ชุด…" style="width:220px"><select id=sel></select></div>
<div class=box id=card></div>
<script>
const D=__DATA__; let i=0, shown=0;
const esc=s=>String(s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
function fill(){const sel=document.getElementById('sel'),f=document.getElementById('f').value.toLowerCase();
 const list=D.map((d,k)=>[d,k]).filter(([d])=>!f||(d.id+' '+d.set).toLowerCase().includes(f));
 sel.innerHTML=list.map(([d,k])=>`<option value="${k}">${esc(d.id)} · ${esc(d.d)}</option>`).join('');
 if(list.length){i=list[0][1];draw();}}
function draw(){const d=D[i];shown=0;
 document.getElementById('card').innerHTML=`<div class=meta>${esc(d.id)} · ${esc(d.set)} · ${esc(d.d)}</div>
 <div class=q>${esc(d.q)}</div>${d.ch.length?'<ol class=c>'+d.ch.map(c=>`<li>${esc(c)}</li>`).join('')+'</ol>':''}
 <div class=row><button data-act=next>เปิดขั้นถัดไป ▸</button><button data-act=all>เปิดทั้งหมด</button>
 <button data-act=hint>ใบ้</button><button data-act=trap>กับดัก</button><button data-act=reset>ซ่อนใหม่</button></div>
 <div class=meta style="margin-top:10px">เป้าหมาย: ${esc(d.goal)}</div>
 ${d.steps.map((s,n)=>`<div class=step id=s${n}><div class=st>ขั้นที่ ${n+1} · ${esc(s.t)}</div>
   ${s.y?`<div class=why>${esc(s.y)}</div>`:''}${s.f?`<div>${esc(s.f)}</div>`:''}
   <div class=work>${(s.w||[]).map(w=>`<div>${esc(w)}</div>`).join('')}</div>
   ${s.e?`<div class=eq>${esc(s.e)}</div>`:''}</div>`).join('')}
 <div class=hint id=hint><b>คำใบ้</b><ul>${d.hints.map(h=>`<li>${esc(h)}</li>`).join('')}</ul></div>
 <div class=trap id=trap><b>กับดักที่เด็กมักพลาด</b><ul>${d.traps.map(t=>`<li><code>${esc(t.g)}</code> — ${esc(t.w)}</li>`).join('')}</ul></div>`;
 mj();}
function rvNext(){const s=document.getElementById('s'+shown);if(s){s.classList.add('on');shown++;mj(s);}}
function rvAll(){document.querySelectorAll('.step').forEach(s=>s.classList.add('on'));shown=(D[i].steps||[]).length;mj();}
function rvReset(){document.querySelectorAll('.step').forEach(s=>s.classList.remove('on'));shown=0;document.getElementById('hint').style.display='none';document.getElementById('trap').style.display='none';}
function rvHint(){const h=document.getElementById('hint');h.style.display=h.style.display==='block'?'none':'block';mj(h);}
function rvTrap(){const h=document.getElementById('trap');h.style.display=h.style.display==='block'?'none':'block';mj(h);}
document.getElementById('sel').onchange=e=>{i=+e.target.value;draw()};
const ACT={next:rvNext,all:rvAll,hint:rvHint,trap:rvTrap,reset:rvReset};
document.getElementById('card').addEventListener('click',e=>{const b=e.target.closest('button[data-act]');if(b&&ACT[b.dataset.act])ACT[b.dataset.act]();});
function mj(el){try{if(window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise(el?[el]:undefined).catch(()=>{});}catch(_){}}
document.getElementById('f').oninput=fill; fill();
</script></html>"""
    doc = doc.replace('__TS__', ts).replace('__N__', str(len(data))).replace('__DATA__', json.dumps(data, ensure_ascii=False))
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    open(a.out, 'w', encoding='utf-8').write(doc)
    print(f'✅ {a.out} · {len(data):,} ข้อ (จำกัดด้วย --limit เพื่อไม่ให้ไฟล์ใหญ่เกิน)')

if __name__ == '__main__': main()

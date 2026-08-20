#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""progress.py v2 — สร้าง progress.html
   ความคืบหน้ารายชุด/รายข้อ/รายบท + กราฟรายวันที่อ่านออก + แถบ "วันนี้" + กางเฉลยได้ในหน้าเดียว

ใช้ (บนเครื่องครู · ค่า token = 0):
  python tools\\progress.py --bank data\\bank.json --manifest data\\manifest.json ^
      --done _t1run\\results --queue _t1run\\QUEUE_ปัจจุบัน.json ^
      --master _t1run\\results\\t1_MASTER_486.json --out _t1run\\progress.html

ตัวเลือกที่เพิ่มใน v2:
  --master FILE      ไฟล์เฉลยรวม ⇒ ฝังเฉลยลงหน้า กดกางได้ (ไม่ใส่ = หน้าเบา ไม่มีเฉลย)
  --no-solutions     บังคับไม่ฝังเฉลย แม้จะส่ง --master มา
  --days N           กราฟรายวันย้อนหลังกี่วัน (ค่าเริ่ม 21)
  --target N         เส้นเพดานต่อวันในกราฟ (ค่าเริ่ม 80 = มติครู #7 · ใส่ 0 เพื่อไม่วาด)
  --rounds "09:08,12:08,15:08,18:08"   เวลารอบอัตโนมัติ ⇒ ใช้คำนวณ "รอบถัดไป"
"""
import json, os, re, glob, argparse, collections, datetime

TH_DAY = ['จ.', 'อ.', 'พ.', 'พฤ.', 'ศ.', 'ส.', 'อา.']

# ⏱ เวลาทุกจุดในหน้านี้ = ICT เสมอ ⛔ ไม่ขึ้นกับโซนเวลาของเครื่องที่รัน
# (รันผ่านสะพาน = เครื่อง Linux เป็น UTC · รันบน Windows ของครู = ICT อยู่แล้ว — สูตรนี้ถูกทั้งสองทาง)
ICT = datetime.timezone(datetime.timedelta(hours=7))
def now_ict():
    return datetime.datetime.now(ICT)
def ts_ict(epoch):
    return datetime.datetime.fromtimestamp(epoch, ICT)


def S(v):
    return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)


def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(
        v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))


STAMP = re.compile(r'(20\d{6})-(\d{4})')


def scan_done(paths):
    """คืน (done, rounds)
       done   = {id: {'when': 'YYYY-MM-DD HH:MM', 'approx': 0/1}}
       rounds = [{'when':…, 'file':…, 'ids':[…], 'approx':0/1}]  เรียงตามเวลา
       กติกาป้าย: ไฟล์ที่ชื่อมี stamp (t1_YYYYMMDD-HHMM.json) = เวลาจริงของรอบ ⇒ approx = 0
                  ไฟล์รวม (t1_MASTER_*.json ฯลฯ) ไม่มี stamp ⇒ ใช้เวลาแก้ไขไฟล์ ⇒ approx = 1
       ข้อที่โผล่ในไฟล์รอบจริง จะไม่ถูกไฟล์รวมแย่งวันที่ (ยึดเวลาจริงเสมอ แล้วจึงยึดเวลาที่เก่าที่สุด)
    """
    files = []
    for p in paths:
        if os.path.isfile(p):
            files.append(p)
        else:
            files += glob.glob(os.path.join(p, '**', '*.json'), recursive=True)

    stamped, rolled = [], []
    for f in sorted(files):
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        if not (isinstance(d, list) and d and isinstance(d[0], dict) and 'steps' in d[0]):
            continue
        ids = [r.get('id') for r in d if r.get('id')]
        m = STAMP.search(os.path.basename(f))
        if m:
            when = f'{m.group(1)[:4]}-{m.group(1)[4:6]}-{m.group(1)[6:]} {m.group(2)[:2]}:{m.group(2)[2:]}'
            stamped.append({'when': when, 'file': os.path.basename(f), 'ids': ids, 'approx': 0})
        else:
            when = ts_ict(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
            rolled.append({'when': when, 'file': os.path.basename(f), 'ids': ids, 'approx': 1})

    done = {}
    for r in sorted(stamped, key=lambda x: x['when']):          # เวลาจริงมาก่อนเสมอ
        for i in r['ids']:
            if i not in done or r['when'] < done[i]['when']:
                done[i] = {'when': r['when'], 'approx': 0}
    for r in sorted(rolled, key=lambda x: x['when']):           # ไฟล์รวมเติมเฉพาะข้อที่ยังไม่มีวันที่จริง
        for i in r['ids']:
            if i not in done:
                done[i] = {'when': r['when'], 'approx': 1}

    rounds = []
    seen = set()
    for r in sorted(stamped + rolled, key=lambda x: (x['approx'], x['when'])):
        fresh = [i for i in r['ids'] if i not in seen]
        seen.update(fresh)
        if fresh:
            rounds.append({'when': r['when'], 'file': r['file'], 'ids': fresh,
                           'n': len(fresh), 'approx': r['approx']})
    rounds.sort(key=lambda x: x['when'])
    return done, rounds


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--manifest', default=os.path.join('data', 'manifest.json'))
    ap.add_argument('--done', nargs='*', default=[os.path.join('_t1run', 'results')])
    ap.add_argument('--queue', default=os.path.join('_t1run', 'QUEUE_now.json'))
    ap.add_argument('--master', default='')
    ap.add_argument('--no-solutions', action='store_true')
    ap.add_argument('--days', type=int, default=21)
    ap.add_argument('--target', type=int, default=80)
    ap.add_argument('--rounds', default='09:08,12:08,15:08,18:08')
    ap.add_argument('--out', default='progress.html')
    a = ap.parse_args()

    items = load_bank(a.bank)
    done, rounds = scan_done(a.done)

    names = {}
    try:
        names = json.load(open(a.manifest, encoding='utf-8')).get('topicNames', {})
    except Exception:
        pass

    queue_ids, queue_order, queue_when = set(), {}, ''
    if os.path.exists(a.queue):
        try:
            q = json.load(open(a.queue, encoding='utf-8'))
            for n, x in enumerate(q):
                queue_ids.add(x['id'])
                queue_order[x['id']] = n
            queue_when = ts_ict(os.path.getmtime(a.queue)).strftime('%d/%m/%Y %H:%M')
        except Exception:
            pass

    # ---------- เฉลย ----------
    sols, sol_note = {}, ''
    if a.master and not a.no_solutions and os.path.exists(a.master):
        bank_by_id = {x['id']: x for x in items}
        try:
            recs = json.load(open(a.master, encoding='utf-8'))
            for r in recs:
                i = r.get('id')
                if not i:
                    continue
                q = bank_by_id.get(i, {})
                sols[i] = {
                    'q': S(q.get('question', '')),
                    'ch': [S(c) for c in (q.get('choices') or [])],
                    'cor': q.get('correct'),
                    'goal': r.get('goal', ''),
                    'given': r.get('given') or [],
                    'steps': [{'t': s.get('title', ''), 'f': s.get('formula') or '',
                               'y': s.get('why') or '', 'w': s.get('work') or [],
                               'e': s.get('eq') or '', 'c': s.get('check') or ''}
                              for s in (r.get('steps') or [])],
                    'ver': (r.get('verify') or {}).get('result', '') if isinstance(r.get('verify'), dict) else S(r.get('verify') or ''),
                    'tech': r.get('technique') or [],
                    'hints': r.get('hints') or [],
                    'traps': [{'g': t.get('got', ''), 'y': t.get('why', '')}
                              for t in (r.get('traps') or [])],
                }
            sol_note = f'ฝังเฉลย {len(sols):,} ข้อจาก {os.path.basename(a.master)}'
        except Exception as e:
            sol_note = f'⚠️ อ่านไฟล์เฉลยไม่ได้: {e}'
    elif a.master and a.no_solutions:
        sol_note = 'ปิดการฝังเฉลยด้วย --no-solutions'
    elif a.master:
        sol_note = f'⚠️ ไม่พบไฟล์เฉลย {a.master}'
    else:
        sol_note = 'ไม่ได้ส่ง --master ⇒ หน้านี้ไม่มีเฉลย'

    # ---------- จัดกลุ่มเป็นชุด ----------
    sets = collections.defaultdict(list)
    for x in items:
        sid = x.get('setId') or re.sub(r'-q\d+[a-z]?$', '', x.get('id', ''))
        sets[sid].append(x)

    data = []
    for sid, rows in sorted(sets.items()):
        tps = collections.Counter()
        qs = []
        for x in rows:
            for t in (x.get('topics') or [x.get('topic')]):
                tps[str(t)] += 1
            i = x['id']
            st = 'done' if i in done else ('queue' if i in queue_ids else 'todo')
            qs.append({'id': i, 'n': str(x.get('questionNumber') or ''),
                       'd': x.get('difficulty') or '',
                       'sub': ' '.join(x.get('subTopics') or []),
                       'img': 1 if x.get('hasImage') else 0,
                       'st': st,
                       'when': done.get(i, {}).get('when', ''),
                       'ap': done.get(i, {}).get('approx', 0),
                       'sol': 1 if i in sols else 0,
                       'ord': queue_order.get(i, -1)})
        qs.sort(key=lambda r: (len(str(r['n'])), str(r['n'])))
        nd = sum(1 for r in qs if r['st'] == 'done')
        nq = sum(1 for r in qs if r['st'] == 'queue')
        last = max([r['when'] for r in qs if r['when']] or [''])
        tp_names = [names.get(t, t) for t, _ in tps.most_common()]
        data.append({'set': sid, 'chap': ' · '.join(tp_names[:3]), 'tps': tp_names,
                     'n': len(qs), 'done': nd, 'queue': nq, 'last': last, 'items': qs})

    tot = len(items)
    nd = sum(1 for x in items if x['id'] in done)
    inq = sum(1 for x in items if x['id'] in queue_ids and x['id'] not in done)

    # ---------- กราฟรายวัน (เติมวันที่ว่างให้ครบ) ----------
    byday = collections.Counter()
    byday_ap = collections.Counter()
    for i, v in done.items():
        d = v['when'][:10]
        byday[d] += 1
        if v['approx']:
            byday_ap[d] += 1
    today = now_ict().date()
    days = []
    if byday:
        first = min(datetime.date.fromisoformat(d) for d in byday)
        start = max(first, today - datetime.timedelta(days=a.days - 1))
        d = start
        while d <= today:
            k = d.isoformat()
            days.append({'d': k, 'lab': f'{d.day:02d}/{d.month:02d}', 'dow': TH_DAY[d.weekday()],
                         'c': byday.get(k, 0), 'ap': byday_ap.get(k, 0),
                         'today': 1 if d == today else 0})
            d += datetime.timedelta(days=1)

    # ---------- วันนี้ ----------
    tkey = today.isoformat()
    today_rounds = [r for r in rounds if r['when'][:10] == tkey]
    today_n = sum(r['n'] for r in today_rounds)

    nxt_all = sorted([r for s in data for r in s['items'] if r['st'] == 'queue'],
                     key=lambda r: r['ord'])
    now = now_ict()
    round_times = [t.strip() for t in a.rounds.split(',') if t.strip()]
    next_round = ''
    for t in round_times:
        try:
            hh, mm = [int(z) for z in t.split(':')]
        except Exception:
            continue
        cand = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
        if cand > now:
            next_round = cand.strftime('%d/%m %H:%M')
            break
    if not next_round and round_times:
        try:
            hh, mm = [int(z) for z in round_times[0].split(':')]
            next_round = (now + datetime.timedelta(days=1)).replace(
                hour=hh, minute=mm, second=0, microsecond=0).strftime('%d/%m %H:%M')
        except Exception:
            pass

    ts = now.strftime('%d/%m/%Y %H:%M')
    today_lab = f'{TH_DAY[today.weekday()]} {today.day:02d}/{today.month:02d}/{today.year}'

    def J(o):
        return json.dumps(o, ensure_ascii=False).replace('</', '<\\/')

    doc = r"""<!doctype html><html lang=th><meta charset=utf-8>
<title>ความคืบหน้าเฉลยละเอียด t1</title>
<script>window.MathJax={tex:{inlineMath:[['$','$']],displayMath:[['$$','$$']]},options:{skipHtmlTags:['script','noscript','style','textarea','pre']}};</script>
<script id=MathJax-script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
*{box-sizing:border-box} body{font-family:'Segoe UI',Tahoma,sans-serif;margin:0;background:#faf8f5;color:#2b2b2b}
.wrap{max-width:1180px;margin:0 auto;padding:26px 18px 90px}
h1{font-size:22px;margin:0 0 4px} .sub{color:#8a8078;font-size:13px;margin-bottom:20px;line-height:1.6}
h2{font-size:15px;margin:26px 0 10px}
.kpi{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:8px}
.card{flex:1;min-width:140px;background:#fff;border:1px solid #eae4dc;border-radius:10px;padding:13px 15px}
.card .v{font-size:25px;font-weight:600} .card .l{font-size:12px;color:#8a8078;margin-top:2px}
.bar{background:#fff;border:1px solid #eae4dc;border-radius:10px;padding:14px 16px;margin-bottom:8px}
input,select,button{font:inherit;padding:7px 10px;border:1px solid #ddd5cb;border-radius:7px;background:#fff}
input{width:250px} button{cursor:pointer}
button.p{background:#b8763e;color:#fff;border-color:#b8763e}
button.s{background:#fff;color:#8a5a2e;border-color:#e0cdb4}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #eae4dc;border-radius:10px;overflow:hidden}
th,td{padding:8px 11px;font-size:13px;border-bottom:1px solid #f2ede6;text-align:left;vertical-align:top}
th{background:#f6f1ea;font-weight:600;font-size:12px;color:#6b6259}
td.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
tr.s{cursor:pointer} tr.s:hover{background:#fdfaf6}
.track{display:inline-block;width:96px;height:8px;background:#efe9e1;border-radius:4px;vertical-align:middle}
.fill{height:8px;background:#b8763e;border-radius:4px} .pct{font-size:12px;color:#8a8078;margin-left:7px}
.det{display:none;background:#fdfbf8} .det td{padding:10px 14px}
.q{display:inline-block;margin:2px;padding:3px 7px;border-radius:6px;font-size:12px;border:1px solid transparent;white-space:nowrap}
.done{background:#e8f3ea;border-color:#cfe4d3;color:#2f6b3d}
.queue{background:#fff2e2;border-color:#f0dcc0;color:#9a5b17}
.todo{background:#f4f1ed;border-color:#e7e1d8;color:#8a8078}
.q.pick{cursor:pointer} .q.pick:hover{filter:brightness(.97)}
.q.on{outline:2px solid #b8763e;outline-offset:1px;font-weight:600}
.tag{font-size:9px;border:1px solid currentColor;border-radius:3px;padding:0 3px;margin-left:4px;opacity:.75;vertical-align:1px}
.legend{font-size:12px;color:#8a8078;margin:6px 0 14px;line-height:2}
/* ---- กราฟรายวัน ---- */
.chartbox{overflow-x:auto;padding-bottom:2px}
.plot{display:flex;gap:7px;align-items:flex-end;height:150px;position:relative;padding-top:16px}
.col{display:flex;flex-direction:column;justify-content:flex-end;align-items:center;width:42px;min-width:42px;height:100%}
.col .v{font-size:11px;color:#6b6259;margin-bottom:3px;font-variant-numeric:tabular-nums}
.col .b{width:28px;background:#b8763e;border-radius:4px 4px 0 0;min-height:2px}
.col .b.z{background:#ece5dc}
.col .b.ap{background:repeating-linear-gradient(45deg,#d3a877,#d3a877 4px,#e3c6a4 4px,#e3c6a4 8px)}
.xaxis{display:flex;gap:7px;border-top:1px solid #e9e1d6;padding-top:5px}
.xaxis div{width:42px;min-width:42px;text-align:center;font-size:10px;color:#8a8078;line-height:1.35}
.xaxis div.today{color:#b8763e;font-weight:700}
.tline{position:absolute;left:0;right:0;border-top:1px dashed #cbb9a0}
.tline span{position:absolute;right:0;top:-15px;font-size:10px}
.tline span{color:#a8998a;background:#fff;padding:0 4px}
/* ---- วันนี้ ---- */
.today{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:10px}
.tbox{flex:1;min-width:190px;border:1px solid #eee7dd;border-radius:9px;padding:11px 13px;background:#fdfbf8}
.tbox .h{font-size:12px;color:#8a8078;margin-bottom:4px}
.tbox .v{font-size:19px;font-weight:600}
.rt{font-size:12.5px;margin:4px 0;color:#4a443e}
.rt b{font-variant-numeric:tabular-nums}
/* ---- ห้องอ่านเฉลย ---- */
#reader{display:none}
.rbar{position:sticky;top:0;z-index:5;background:#fff8ef;border:1px solid #f0e0c8;border-radius:9px;
      padding:9px 12px;display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:10px}
.rbar .c{font-size:13px;color:#8a5a2e;font-weight:600}
details.sol{background:#fff;border:1px solid #eae4dc;border-radius:10px;margin-bottom:9px}
details.sol>summary{cursor:pointer;padding:10px 14px;font-size:13.5px;list-style:none}
details.sol>summary::-webkit-details-marker{display:none}
details.sol>summary:before{content:'▸ ';color:#b8763e}
details.sol[open]>summary:before{content:'▾ '}
details.sol[open]>summary{border-bottom:1px solid #f2ede6;background:#fdfbf8}
.solbody{padding:12px 16px 16px}
.qtext{font-size:14.5px;margin-bottom:8px;line-height:1.7}
ol.ch{padding-left:22px;margin:6px 0} ol.ch li{margin:3px 0}
ol.ch li.cor{background:#e8f3ea;border-radius:5px;padding:1px 5px}
.step{border-left:3px solid #e5d9c8;padding:7px 0 7px 13px;margin:11px 0}
.st{font-weight:600;font-size:13.5px} .why{color:#8a8078;font-size:12.5px;margin:3px 0}
.work div{margin:2px 0;font-size:13px}
.eq{background:#f6f1ea;padding:5px 9px;border-radius:6px;display:inline-block;margin-top:5px}
.meta{font-size:12px;color:#8a8078}
.hint,.trap{border-radius:8px;padding:9px 12px;margin-top:9px;font-size:13px}
.hint{background:#fffaf0;border:1px solid #f0e2c8} .trap{background:#fff4f4;border:1px solid #f2d6d6}
.hint ul,.trap ul{margin:5px 0 0;padding-left:20px}
.nosol{color:#8a8078;font-size:12.5px}
</style><div class=wrap>
<h1>ความคืบหน้าเฉลยละเอียด t1</h1>
<div class=sub>สร้างจากไฟล์จริงเมื่อ <b>__TS__ ICT</b> · ไฟล์คิวอัปเดตล่าสุด <b>__QWHEN__ ICT</b> · __SOLNOTE__
<br>คลิกแถวชุดเพื่อกางรายข้อ · คลิก<b>เลขข้อสีเขียว</b>เพื่อเลือกเข้าห้องอ่านเฉลย · ⛔ ค่า token = 0 (ไฟล์นี้ทำงานในเครื่อง)</div>

<div class=kpi>
 <div class=card><div class=v>__TOT__</div><div class=l>ข้อทั้งคลัง</div></div>
 <div class=card><div class=v>__ND__</div><div class=l>ทำเสร็จแล้ว</div></div>
 <div class=card><div class=v>__INQ__</div><div class=l>อยู่ในคิว (รอทำ)</div></div>
 <div class=card><div class=v>__REST__</div><div class=l>ยังไม่เข้าคิว</div></div>
 <div class=card><div class=v>__PCT__%</div><div class=l>คืบหน้า</div></div>
</div>

<h2>📆 วันนี้ · __TODAYLAB__</h2>
<div class=bar>
 <div class=today>
  <div class=tbox><div class=h>เสร็จวันนี้</div><div class=v id=tdn>—</div></div>
  <div class=tbox><div class=h>รอบของวันนี้</div><div class=v id=tdr>—</div></div>
  <div class=tbox><div class=h>รอบถัดไป (ตามตารางเวลา)</div><div class=v id=tdnext>—</div></div>
  <div class=tbox><div class=h>เหลือในคิว</div><div class=v id=tdq>—</div></div>
 </div>
 <div id=todaylist></div>
 <div style="margin-top:12px"><b style="font-size:13px">▶️ รอบถัดไปจะหยิบ 20 ข้อนี้</b>
   <span class=meta>(เรียงตามลำดับคิวจริง · ป้ายนี้มีอายุเท่าไฟล์คิว: __QWHEN__)</span></div>
 <div id=next20 style="margin-top:5px"></div>
 <div style="margin-top:12px"><b style="font-size:13px">⏭ หลังจากนั้นอีก 20 ข้อ</b></div>
 <div id=next40 style="margin-top:5px"></div>
</div>

<h2>📅 เสร็จวันละกี่ข้อ</h2>
<div class=bar>
 <div class=chartbox>
  <div class=plot id=plot></div>
  <div class=xaxis id=xaxis></div>
 </div>
 <div class=legend style="margin:10px 0 0">
   <span style="display:inline-block;width:12px;height:9px;background:#b8763e;border-radius:2px"></span> วันที่รู้เวลารอบจริง ·
   <span style="display:inline-block;width:12px;height:9px;background:repeating-linear-gradient(45deg,#d3a877,#d3a877 4px,#e3c6a4 4px,#e3c6a4 8px);border-radius:2px"></span>
   ⬜ ประมาณจากเวลาแก้ไขไฟล์รวม (ไฟล์นั้นไม่มีเวลารอบในชื่อ) · เส้นประ = เพดาน __TARGET__ ข้อ/วัน
 </div>
</div>

<h2>📖 ห้องอ่านเฉลย</h2>
<div id=reader>
 <div class=rbar>
  <span class=c id=rc>เลือกแล้ว 0 ข้อ</span>
  <button class=p data-r=open>กางทั้งหมด</button>
  <button class=s data-r=close>พับทั้งหมด</button>
  <button class=s data-r=clear>ล้างที่เลือก</button>
 </div>
 <div id=rlist></div>
</div>
<div class=bar id=readerhint>ยังไม่ได้เลือกข้อไหน — คลิกเลขข้อ<span class="q done" style="margin:0 3px">สีเขียว</span>ในตารางข้างล่าง
 หรือกดปุ่ม <b>📖 เลือกทั้งชุด</b> ในแถวที่กางอยู่ · หรือใช้ <b>เลือกทั้งหมดที่กรองอยู่</b> เพื่อเลือกทั้งบท</div>

<h2>📚 รายชุด</h2>
<div class=bar>
 <input id=f placeholder="ค้นหาชื่อชุด / บท / เลขข้อ…">
 <select id=g>
  <option value=all>ทุกชุด</option>
  <option value=part>เฉพาะที่ทำไปบ้างแล้ว</option>
  <option value=full>เฉพาะที่เสร็จครบ</option>
  <option value=none>เฉพาะที่ยังไม่เริ่ม</option>
  <option value=queue>เฉพาะที่มีอยู่ในคิวตอนนี้</option>
 </select>
 <select id=ch><option value="">ทุกบท</option></select>
 <button class=s data-r=selall>เลือกทั้งหมดที่กรองอยู่ (เฉพาะข้อที่เสร็จ)</button>
 <span class=meta id=cnt></span>
</div>
<div class=legend>สีของเลขข้อ: <span class="q done">เสร็จแล้ว</span> <span class="q queue">อยู่ในคิว</span>
 <span class="q todo">ยังไม่ทำ</span> · <span class="q todo">12<span class=tag>รูป</span></span> = ข้อที่ติดธงว่ามีรูป
 · <span class="q done">7<span class=tag>?</span></span> = วันที่เป็นค่าประมาณ</div>
<table id=t><thead><tr><th>ชุด</th><th>บทหลัก</th><th class=n>ทั้งหมด</th><th class=n>เสร็จ</th>
 <th class=n>ในคิว</th><th>คืบหน้า</th><th>เสร็จล่าสุด</th></tr></thead><tbody id=tb></tbody></table>
</div>
<script id=SOLDATA type="application/json">__SOLS__</script>
<script>
const DATA=__DATA__, DAYS=__DAYS__, ROUNDS=__ROUNDS__, TODAY=__TODAYJS__, TARGET=__TARGET__;
const NEXTQ=__NEXTQ__, NEXTROUND=__NEXTROUND__, INQ=__INQN__;
let SOL=null;
function sol(){ if(SOL===null){ try{SOL=JSON.parse(document.getElementById('SOLDATA').textContent||'{}');}
  catch(e){SOL={};} } return SOL; }
const esc=s=>String(s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const mj=el=>{try{if(window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise(el?[el]:undefined).catch(()=>{});}catch(_){}};

/* ---------- เลขข้อ ---------- */
function chip(r){
  const tags=(r.img?'<span class=tag>รูป</span>':'')+(r.ap?'<span class=tag>?</span>':'');
  const pick=(r.st==='done'&&r.sol)?' pick':'';
  const on=SELECTED.has(r.id)?' on':'';
  const tip=r.id+(r.when?' · เสร็จ '+r.when+(r.ap?' (ประมาณ)':''):'')+(r.sub?' · '+r.sub:'')+' · '+r.d
    +(pick?' · คลิกเพื่ออ่านเฉลย':'');
  return `<span class="q ${r.st}${pick}${on}" data-id="${esc(r.id)}" title="${esc(tip)}">${esc(r.n||r.id)}${tags}</span>`;
}

/* ---------- กราฟรายวัน ---------- */
(function(){
  const mx=Math.max(1,...DAYS.map(d=>d.c)), H=118;
  document.getElementById('plot').innerHTML=DAYS.map(d=>{
    const h=d.c?Math.max(3,Math.round(d.c/mx*H)):2;
    const cls=d.c?(d.ap>=d.c?'b ap':'b'):'b z';
    return `<div class=col title="${d.d} · ${d.c} ข้อ${d.ap?' (ประมาณ '+d.ap+')':''}">
      <div class=v>${d.c||''}${d.ap?'<sup style="color:#a8998a">'+d.ap+'?</sup>':''}</div>
      <div class="${cls}" style="height:${h}px"></div></div>`;}).join('')
    +(TARGET>0&&TARGET<=mx?`<div class=tline style="bottom:${Math.round(TARGET/mx*H)}px">
      <span>เพดาน ${TARGET}/วัน</span></div>`:'');
  document.getElementById('xaxis').innerHTML=DAYS.map(d=>
    `<div class="${d.today?'today':''}">${d.lab}<br>${d.dow}</div>`).join('');
  const box=document.querySelector('.chartbox'); box.scrollLeft=box.scrollWidth;
})();

/* ---------- วันนี้ ---------- */
(function(){
  const tr=ROUNDS.filter(r=>r.when.slice(0,10)===TODAY);
  const real=tr.filter(r=>!r.approx), ap=tr.filter(r=>r.approx);
  const n=real.reduce((s,r)=>s+r.n,0), na=ap.reduce((s,r)=>s+r.n,0);
  document.getElementById('tdn').innerHTML=n+' ข้อ'+(na?` <span class=meta style="font-size:12px">+${na} จากไฟล์รวม (เวลาประมาณ)</span>`:'');
  document.getElementById('tdr').innerHTML=real.length+' รอบ'+(ap.length?` <span class=meta style="font-size:12px">+${ap.length} ไฟล์รวม</span>`:'');
  document.getElementById('tdnext').textContent=NEXTROUND||'—';
  document.getElementById('tdq').textContent=INQ.toLocaleString()+' ข้อ';
  document.getElementById('todaylist').innerHTML = tr.length
    ? tr.map((r,k)=>`<div class=rt>🕐 <b>${r.when.slice(11)}</b> น. · <b>${r.n}</b> ข้อ
        <span class=meta>· ${esc(r.file)}${r.approx?' · ⬜ เวลาโดยประมาณ':''}</span>
        <button class="s" style="padding:2px 8px;font-size:12px" data-rd="${k}">ดูรายชื่อ</button>
        <div id=rd${k} style="display:none;margin:5px 0 9px">${r.ids.map(i=>`<span class="q done" data-id="${esc(i)}">${esc(i)}</span>`).join(' ')}</div></div>`).join('')
    : '<div class=rt style="color:#8a8078">⬜ ยังไม่มีรอบของวันนี้ในโฟลเดอร์ผล — ถ้ารอบเพิ่งจบ ให้รันสคริปต์นี้ใหม่อีกครั้ง</div>';
  document.getElementById('todaylist').addEventListener('click',e=>{
    const b=e.target.closest('button[data-rd]'); if(!b)return;
    const d=document.getElementById('rd'+b.dataset.rd);
    d.style.display=d.style.display==='none'?'block':'none';});
  document.getElementById('next20').innerHTML=NEXTQ.slice(0,20).map(r=>
    `<span class="q queue" title="${esc(r.id)}">${esc(r.id)}</span>`).join(' ')||'<span class=meta>⬜ ไม่พบไฟล์คิว</span>';
  document.getElementById('next40').innerHTML=NEXTQ.slice(20,40).map(r=>
    `<span class="q queue" title="${esc(r.id)}">${esc(r.id)}</span>`).join(' ')||'<span class=meta>—</span>';
})();

/* ---------- ห้องอ่านเฉลย ---------- */
const SELECTED=new Set();
function solHTML(id){
  const d=sol()[id];
  if(!d) return `<div class=nosol>⬜ ไม่มีเฉลยของข้อนี้ในไฟล์ที่ฝังมา</div>`;
  const ch=d.ch&&d.ch.length?`<ol class=ch>${d.ch.map((c,k)=>
      `<li class="${(typeof d.cor==='number'&&k===d.cor)?'cor':''}">${esc(c)}</li>`).join('')}</ol>`:'';
  const given=(d.given&&d.given.length)?`<div class=meta style="margin:6px 0">โจทย์ให้: ${d.given.map(esc).join(' · ')}</div>`:'';
  return `<div class=solbody>
   <div class=qtext>${esc(d.q)}</div>${ch}${given}
   <div class=meta style="margin:8px 0 2px">🎯 เป้าหมาย: ${esc(d.goal)}</div>
   ${(d.tech&&d.tech.length)?`<div class=meta>เทคนิค: ${d.tech.map(esc).join(' · ')}</div>`:''}
   ${d.steps.map((s,n)=>`<div class=step><div class=st>ขั้นที่ ${n+1} · ${esc(s.t)}</div>
     ${s.y?`<div class=why>${esc(s.y)}</div>`:''}${s.f?`<div>${esc(s.f)}</div>`:''}
     <div class=work>${(s.w||[]).map(w=>`<div>${esc(w)}</div>`).join('')}</div>
     ${s.e?`<div class=eq>${esc(s.e)}</div>`:''}
     ${s.c?`<div class=why>✔ ${esc(s.c)}</div>`:''}</div>`).join('')}
   ${d.ver?`<div class=eq style="margin-top:8px">✅ ${esc(d.ver)}</div>`:''}
   ${(d.hints&&d.hints.length)?`<div class=hint><b>คำใบ้ 4 ระดับ</b><ul>${d.hints.map(h=>`<li>${esc(h)}</li>`).join('')}</ul></div>`:''}
   ${(d.traps&&d.traps.length)?`<div class=trap><b>กับดัก</b><ul>${d.traps.map(t=>`<li><code>${esc(t.g)}</code> — ${esc(t.y)}</li>`).join('')}</ul></div>`:''}
  </div>`;
}
function renderReader(){
  const ids=[...SELECTED];
  document.getElementById('rc').textContent='เลือกแล้ว '+ids.length+' ข้อ';
  document.getElementById('reader').style.display=ids.length?'block':'none';
  document.getElementById('readerhint').style.display=ids.length?'none':'block';
  if(!ids.length){document.getElementById('rlist').innerHTML='';return;}
  const meta={}; DATA.forEach(s=>s.items.forEach(r=>{if(SELECTED.has(r.id))meta[r.id]={set:s.set,chap:s.chap,r:r};}));
  document.getElementById('rlist').innerHTML=ids.map(id=>{
    const m=meta[id]||{set:'',chap:'',r:{}};
    return `<details class=sol data-sid="${esc(id)}"><summary><b>${esc(id)}</b>
      <span class=meta>· ${esc(m.set)} · ${esc(m.chap)} · ${esc(m.r.d||'')}${m.r.when?' · เสร็จ '+esc(m.r.when):''}</span></summary>
      <div class=slot></div></details>`;}).join('');
  document.querySelectorAll('details.sol').forEach(el=>{
    el.addEventListener('toggle',()=>{
      if(el.open&&!el.dataset.filled){el.querySelector('.slot').innerHTML=solHTML(el.dataset.sid);
        el.dataset.filled='1';mj(el);}});});
}
function toggle(id){ if(SELECTED.has(id))SELECTED.delete(id); else SELECTED.add(id);
  renderReader(); paintChips(); }
function paintChips(){ document.querySelectorAll('.q.pick').forEach(el=>
  el.classList.toggle('on',SELECTED.has(el.dataset.id))); }

/* ---------- ตารางรายชุด ---------- */
(function(){const all=new Set(); DATA.forEach(s=>s.tps.forEach(t=>all.add(t)));
  document.getElementById('ch').innerHTML='<option value="">ทุกบท</option>'+
    [...all].sort().map(t=>`<option value="${esc(t)}">${esc(t)}</option>`).join('');})();

function filtered(){
  const f=document.getElementById('f').value.trim().toLowerCase(),
        g=document.getElementById('g').value, c=document.getElementById('ch').value;
  return DATA.filter(s=>{
    if(g==='part'&&!(s.done>0&&s.done<s.n))return false;
    if(g==='full'&&s.done!==s.n)return false;
    if(g==='none'&&s.done!==0)return false;
    if(g==='queue'&&s.queue===0)return false;
    if(c&&!s.tps.includes(c))return false;
    if(!f)return true;
    return (s.set+' '+s.chap).toLowerCase().includes(f)||s.items.some(r=>r.id.toLowerCase().includes(f));
  });
}
function render(){
  const rows=filtered();
  document.getElementById('cnt').textContent=
    `${rows.length} ชุด · เสร็จแล้วในกลุ่มนี้ ${rows.reduce((a,s)=>a+s.done,0).toLocaleString()} ข้อ`;
  document.getElementById('tb').innerHTML=rows.map((s,i)=>{
    const p=s.n?s.done/s.n*100:0;
    return `<tr class=s data-i="${i}"><td><b>${esc(s.set)}</b></td><td>${esc(s.chap)}</td>
    <td class=n>${s.n}</td><td class=n>${s.done}</td><td class=n>${s.queue||''}</td>
    <td><span class=track><span class=fill style="width:${p.toFixed(1)}%;display:block"></span></span><span class=pct>${p.toFixed(0)}%</span></td>
    <td>${esc(s.last||'—')}</td></tr>
    <tr class=det><td colspan=7>
      ${s.done?`<div style="margin-bottom:7px"><button class=s data-set="${esc(s.set)}" data-act=add>📖 เลือกทั้งชุด (${s.done} ข้อ)</button>
        <button class=s data-set="${esc(s.set)}" data-act=del>เอาชุดนี้ออก</button></div>`:''}
      ${s.items.map(chip).join(' ')}</td></tr>`;}).join('');
  document.querySelectorAll('tr.s').forEach(tr=>tr.onclick=()=>{
    const d=tr.nextElementSibling; d.style.display=d.style.display==='table-row'?'none':'table-row';});
  paintChips();
}
document.getElementById('tb').addEventListener('click',e=>{
  const b=e.target.closest('button[data-set]');
  if(b){ e.stopPropagation();
    const s=DATA.find(x=>x.set===b.dataset.set); if(!s)return;
    s.items.filter(r=>r.st==='done'&&r.sol).forEach(r=>
      b.dataset.act==='add'?SELECTED.add(r.id):SELECTED.delete(r.id));
    renderReader(); paintChips(); return; }
  const c=e.target.closest('.q.pick');
  if(c){ e.stopPropagation(); toggle(c.dataset.id); }
});
document.getElementById('todaylist').addEventListener('click',e=>{
  const c=e.target.closest('.q[data-id]'); if(c&&sol()[c.dataset.id])toggle(c.dataset.id);});
document.querySelector('.rbar').addEventListener('click',e=>{
  const b=e.target.closest('button[data-r]'); if(!b)return;
  if(b.dataset.r==='open')document.querySelectorAll('details.sol').forEach(d=>d.open=true);
  if(b.dataset.r==='close')document.querySelectorAll('details.sol').forEach(d=>d.open=false);
  if(b.dataset.r==='clear'){SELECTED.clear();renderReader();paintChips();}});
document.querySelector('button[data-r=selall]').addEventListener('click',()=>{
  let n=0; filtered().forEach(s=>s.items.forEach(r=>{if(r.st==='done'&&r.sol){SELECTED.add(r.id);n++;}}));
  if(n>300&&!confirm('เลือก '+n+' ข้อ — หน้าอาจหนักสักหน่อย ไปต่อไหม?')){return;}
  renderReader(); paintChips();});
document.getElementById('f').oninput=render;
document.getElementById('g').onchange=render;
document.getElementById('ch').onchange=render;
render(); renderReader();
setTimeout(()=>{ if(!(window.MathJax&&MathJax.typesetPromise)){
  const d=document.createElement('div'); d.className='bar';
  d.style.cssText='background:#fffaf0;border-color:#f0e2c8;font-size:12.5px;color:#8a5a2e';
  d.innerHTML='⬜ โหลดตัวจัดสูตร (MathJax) ไม่ได้ — น่าจะไม่ได้ต่อเน็ต ⇒ สูตรจะแสดงเป็นข้อความดิบแบบ $...$ ⛔ ไม่ใช่ข้อมูลเสีย';
  document.querySelector('.wrap').insertBefore(d,document.querySelector('.kpi'));}},4000);
</script></html>"""

    doc = (doc.replace('__TS__', ts)
              .replace('__QWHEN__', queue_when or '⬜ ไม่พบไฟล์คิว')
              .replace('__SOLNOTE__', sol_note)
              .replace('__TODAYLAB__', today_lab)
              .replace('__TOT__', f'{tot:,}').replace('__ND__', f'{nd:,}')
              .replace('__INQN__', str(inq))
              .replace('__INQ__', f'{inq:,}')
              .replace('__REST__', f'{tot-nd-inq:,}')
              .replace('__PCT__', f'{nd/tot*100:.1f}' if tot else '0')
              .replace('__TARGET__', str(a.target))
              .replace('__TODAYJS__', J(tkey))
              .replace('__NEXTROUND__', J(next_round))
              .replace('__DAYS__', J(days))
              .replace('__ROUNDS__', J([{'when': r['when'], 'file': r['file'], 'n': r['n'],
                                         'approx': r['approx'], 'ids': r['ids']} for r in rounds]))
              .replace('__NEXTQ__', J([{'id': r['id']} for r in nxt_all[:40]]))
              .replace('__SOLS__', J(sols) if sols else '{}')
              .replace('__DATA__', J(data)))

    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    open(a.out, 'w', encoding='utf-8').write(doc)
    size = os.path.getsize(a.out)
    print(f'✅ {a.out}  ({size/1048576:.2f} MB)')
    print(f'   คลัง {tot:,} · เสร็จ {nd:,} ({nd/tot*100:.1f}%) · ในคิว {inq:,} · ยังไม่เข้าคิว {tot-nd-inq:,}')
    print(f'   ชุด {len(data)} · เริ่มแล้ว {sum(1 for s in data if s["done"])} · เสร็จครบ {sum(1 for s in data if s["done"]==s["n"])}')
    print(f'   เฉลยที่ฝัง {len(sols):,} ข้อ · {sol_note}')
    real_rounds = [r for r in today_rounds if not r['approx']]
    ap_rounds = [r for r in today_rounds if r['approx']]
    print(f'   วันนี้ {tkey}: {sum(r["n"] for r in real_rounds)} ข้อ จาก {len(real_rounds)} รอบจริง' +
          (f' ({", ".join(r["when"][11:] for r in real_rounds)})' if real_rounds else '') +
          (f'  ·  +{sum(r["n"] for r in ap_rounds)} ข้อจากไฟล์รวม ⬜ เวลาประมาณ' if ap_rounds else ''))
    if days:
        print('   รายวัน: ' + ' · '.join(f'{d["lab"]}={d["c"]}' for d in days[-7:]))


if __name__ == '__main__':
    main()

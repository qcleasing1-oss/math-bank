#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ตัวเดินงาน t1 — ใช้ในทุกรอบที่งานตามเวลาปลุก
  python3 runner.py status
  python3 runner.py next 10        -> เขียน current_batch.json + พิมพ์โจทย์ที่ต้องทำ
  python3 runner.py commit out.json -> ตรวจ 6 ด่าน + บันทึก + เลื่อน cursor
"""
import json, re, sys, os, datetime, glob

D = os.path.dirname(os.path.abspath(__file__))
Q = os.path.join(D, 'queue.json')
L = os.path.join(D, 'ledger.json')
OUT = os.path.join(D, 'out')
os.makedirs(OUT, exist_ok=True)

def ict():
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=7)).strftime('%Y-%m-%d %H:%M ICT')

def load_q():
    return json.load(open(Q, encoding='utf-8'))

def load_l():
    if os.path.exists(L):
        return json.load(open(L, encoding='utf-8'))
    return {'cursor': 0, 'done': 0, 'passed': 0, 'failed': 0, 'seq': 0, 'batches': []}

def save_l(l):
    json.dump(l, open(L, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

NEED = ['id','v','kb_ref','given','goal','steps','verify','technique','traps','hints']
def norm(x):
    t = re.sub(r'\\left|\\right', '', str(x))
    t = t.replace('dfrac','frac').replace('tfrac','frac')
    return re.sub(r'[\s$\\{}()\[\]]', '', t)


def gates(d, q):
    s = json.dumps(d, ensure_ascii=False); bad = []
    if not all(k in d for k in NEED):
        bad.append('ฟิลด์ขาด:' + ','.join(k for k in NEED if k not in d))
    if 'ความรู้พื้นฐาน' in s: bad.append('มีบล็อก kb หลุด')
    if '\\(' in s or '\\[' in s: bad.append('LaTeX ผิดรูปแบบ')
    body = ' '.join(d.get('given', [])) + str(d.get('goal','')) + json.dumps(d.get('steps',[]), ensure_ascii=False)
    if body.count('$') % 2: bad.append('$ ไม่เป็นคู่')
    n = len(re.sub(r'[{}\[\]",]', '', s))
    if not (2500 <= n <= 9000): bad.append('ความยาว %d' % n)
    ch = q.get('choices'); cor_i = q.get('correct')
    if ch and cor_i is not None and isinstance(cor_i, int) and 0 <= cor_i < len(ch):
        cor = norm(ch[cor_i])
        last = json.dumps(d.get('steps', [])[-1:], ensure_ascii=False) + json.dumps(d.get('verify', {}), ensure_ascii=False)
        if cor and cor not in norm(last): bad.append('คำตอบไม่ตรง correct')
        dis = [norm(c) for i, c in enumerate(ch) if i != cor_i]
        got = [norm(t.get('got','')) for t in d.get('traps', [])]
        if got and sum(1 for g in got if g in dis) == 0: bad.append('traps ไม่ตรงตัวลวงเลย')
    return bad, n

def cmd_requeue():
    l = load_l(); miss = l.get('missing', []) + [r for r in l.get('rejected_ids', [])]
    if not miss:
        print('ไม่มีข้อค้าง'); return
    qs = load_q(); have = {q['id'] for q in qs}
    src = {q['id']: q for q in qs}
    add = [src[i] for i in dict.fromkeys(miss) if i in src]
    qs += add
    json.dump(qs, open(Q,'w',encoding='utf-8'), ensure_ascii=False)
    l['missing'] = []; l['rejected_ids'] = []; save_l(l)
    print('ต่อท้ายคิวอีก %d ข้อ · คิวรวม %d' % (len(add), len(qs)))

def cmd_status():
    qs = load_q(); l = load_l()
    print('คิวทั้งหมด %d ข้อ · ทำแล้ว %d · ผ่าน %d · ตก %d · ค้าง %d · cursor=%d'
          % (len(qs), l['done'], l['passed'], l['failed'],
             len(l.get('missing',[]))+len(l.get('rejected_ids',[])), l['cursor']))
    if l['cursor'] < len(qs):
        nx = qs[l['cursor']]
        print('ข้อถัดไป: %s (%s)' % (nx['id'], (nx.get('topics') or ['?'])[0]))
    else:
        print('🎉 คิวหมดแล้ว')
    for b in l['batches'][-5:]:
        print('  รอบ %-4d %s  ผ่าน %d/%d' % (b['seq'], b['at'], b['pass'], b['pass'] + b['fail']))

def cmd_next(n):
    qs = load_q(); l = load_l(); c = l['cursor']
    batch = qs[c:c+n]
    if not batch:
        print('CURSOR_END'); return
    json.dump(batch, open(os.path.join(D,'current_batch.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=1)
    print('รอบที่ %d · ข้อ %d-%d จาก %d' % (l['seq']+1, c+1, c+len(batch), len(qs)))
    print(json.dumps(batch, ensure_ascii=False, indent=1))

def cmd_split(k):
    b = json.load(open(os.path.join(D,'current_batch.json'), encoding='utf-8'))
    step = (len(b)+k-1)//k; made=[]
    for i in range(k):
        part = b[i*step:(i+1)*step]
        if not part: continue
        fp = os.path.join(D, 'slice_%d.json' % (i+1))
        json.dump(part, open(fp,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
        made.append('%s (%d ข้อ: %s)' % (fp, len(part), ', '.join(q['id'] for q in part)))
    for m in made: print(m)

def cmd_merge(paths):
    allr=[]
    for p in paths:
        if not os.path.exists(p):
            print('⚠️ ไม่พบ', p); continue
        r=json.load(open(p,encoding='utf-8'))
        allr += r if isinstance(r,list) else [r]
    json.dump(allr, open(os.path.join(D,'merged.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=1)
    print('รวมได้ %d ข้อ -> merged.json' % len(allr))

def cmd_commit(path):
    qs = load_q(); l = load_l()
    src = {q['id']: q for q in qs}
    recs = json.load(open(path, encoding='utf-8'))
    if isinstance(recs, dict): recs = [recs]
    l['seq'] += 1; seq = l['seq']
    keep, rej = [], []
    for d in recs:
        q = src.get(d.get('id'), {})
        bad, n = gates(d, q)
        if bad:
            rej.append({'id': d.get('id'), 'ปัญหา': ' · '.join(bad), 'ตัวอักษร': n})
            l.setdefault('rejected_ids', []).append(d.get('id'))
        else: keep.append(d)
    fp = os.path.join(OUT, 't1_%04d.json' % seq)
    json.dump(keep, open(fp,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
    if rej:
        json.dump(rej, open(os.path.join(OUT,'reject_%04d.json'%seq),'w',encoding='utf-8'), ensure_ascii=False, indent=1)
    cb = json.load(open(os.path.join(D,'current_batch.json'), encoding='utf-8'))
    bs = len(cb)
    produced = {d.get('id') for d in recs}
    missing = [q['id'] for q in cb if q['id'] not in produced]
    if missing:
        l.setdefault('missing', []).extend(missing)
    l['cursor'] += bs; l['done'] += bs; l['passed'] += len(keep); l['failed'] += len(rej)
    l['batches'].append({'seq': seq, 'at': ict(), 'pass': len(keep), 'fail': len(rej),
                         'ids': [d.get('id') for d in recs]})
    save_l(l)
    print('รอบ %d · ผ่าน %d · ตก %d · ไม่ได้ส่งมา %d · เขียน %s' % (seq, len(keep), len(rej), len(missing), fp))
    for r in rej: print('   🔴 %s — %s' % (r['id'], r['ปัญหา']))
    print('คืบหน้ารวม %d/%d (%.1f%%)' % (l['done'], len(qs), l['done']*100.0/len(qs)))
    print('DOC_PATH=claude/t1-out/batch_%04d.json' % seq)
    print('LOCAL=%s' % fp)

if __name__ == '__main__':
    a = sys.argv[1:] or ['status']
    if a[0] == 'status': cmd_status()
    elif a[0] == 'next': cmd_next(int(a[1]) if len(a) > 1 else 10)
    elif a[0] == 'requeue': cmd_requeue()
    elif a[0] == 'split': cmd_split(int(a[1]) if len(a)>1 else 4)
    elif a[0] == 'merge': cmd_merge(a[1:])
    elif a[0] == 'commit': cmd_commit(a[1])
    else: print('ไม่รู้จักคำสั่ง', a[0])

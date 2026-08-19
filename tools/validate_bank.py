#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_bank.py — ตรวจคลังข้อสอบทั้งใบ (ค่า token = 0 · รันบนเครื่องครู)
ใช้:  python validate_bank.py [path\to\bank.json] [-o report]
ออก:  report_summary.txt · report_issues.csv
"""
import json, sys, os, re, csv, collections

DEF = os.path.join('data', 'bank.json')
IMG = re.compile(r'\[IMAGE[:\]]', re.I)
FIGWORD = re.compile(r'ดูรูป|ดูตาราง|จากรูป|ตามรูป|รูปประกอบ|ตารางประกอบ|จากตาราง|ดังรูป|ดังตาราง')

def S(v):
    return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)

def load(p):
    d = json.load(open(p, encoding='utf-8'))
    if isinstance(d, list): return d, {}
    meta = {k: v for k, v in d.items() if isinstance(v, (int, str))}
    items = next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))
    return items, meta

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    path = args[0] if args else DEF
    out = 'report'
    if '-o' in sys.argv: out = sys.argv[sys.argv.index('-o') + 1]
    items, meta = load(path)
    n = len(items)
    rows = []           # (id, ระดับ, เรื่อง, รายละเอียด)
    ids = collections.Counter(q.get('id') for q in items)
    for i, c in ids.items():
        if c > 1: rows.append((i, 'ผิด', 'id ซ้ำ', f'พบ {c} ครั้ง'))
    bychap = collections.Counter(); bydiff = collections.Counter()
    multi = []; noimg_but_figword = []; imgflag_nomarker = []; ansimg = []
    for q in items:
        qid = q.get('id', '?')
        tps = q.get('topics') if isinstance(q.get('topics'), list) else ([q.get('topic')] if q.get('topic') else [])
        for t in tps: bychap[t] += 1
        if len(tps) > 1: multi.append(qid)
        d = q.get('difficulty'); bydiff[d] += 1
        if not d: rows.append((qid, 'ผิด', 'ไม่มีป้ายความยาก', ''))
        ch = q.get('choices'); cor = q.get('correct')
        if q.get('type') != 'fill':
            if not ch: rows.append((qid, 'ผิด', 'ไม่มีตัวเลือก', ''))
            elif isinstance(cor, int) and not (0 <= cor < len(ch)):
                rows.append((qid, 'ผิด', 'correct เกินช่วง', f'correct={cor} · ตัวเลือก {len(ch)}'))
            elif isinstance(ch, list) and len(set(map(S, ch))) < len(ch):
                rows.append((qid, 'เตือน', 'ตัวเลือกซ้ำกันเอง', ''))
        qs = S(q.get('question') or '') + S(q.get('choices') or '')
        es = S(q.get('explanation') or '')
        fl = bool(q.get('hasImage'))
        if IMG.search(es): ansimg.append(qid)
        if fl and not (IMG.search(qs) or IMG.search(es)): imgflag_nomarker.append(qid)
        if (not fl) and FIGWORD.search(qs):
            noimg_but_figword.append(qid)
            rows.append((qid, 'ผิด', 'โจทย์อ้างรูป/ตาราง แต่ hasImage=false', FIGWORD.search(qs).group(0)))
        if fl and IMG.search(es) and not IMG.search(qs):
            rows.append((qid, 'เตือน', 'รูปอยู่ฝั่งเฉลย ⛔ ไม่ใช่ฝั่งโจทย์', 'เสี่ยงเฉลยรั่วถ้าดึงเฉลยเก่ามาใช้'))
    sum_chap = sum(bychap.values())
    L = []
    L.append('=== validate_bank.py · รายงานคลังข้อสอบ ===')
    L.append(f'ไฟล์: {path}')
    if meta: L.append('meta: ' + ' · '.join(f'{k}={v}' for k, v in meta.items()))
    L.append('')
    L.append(f'ยอดระเบียนจริง (ตัวหาร)        = {n}')
    L.append(f'ยอดถ้านับตามบท (topics)        = {sum_chap}   ← ต่าง {sum_chap-n} เพราะข้อติดหลายบทถูกนับซ้ำ')
    L.append(f'ข้อที่ติดมากกว่า 1 บท           = {len(multi)}')
    L.append(f'ยอดตามความยาก                  = {sum(bydiff.values())}  ' + ' · '.join(f'{k}:{v}' for k, v in bydiff.most_common()))
    L.append('')
    L.append(f'ธง hasImage = true             = {sum(1 for q in items if q.get("hasImage"))}')
    L.append(f'  ในนั้น marker รูปอยู่ฝั่งเฉลย    = {len(ansimg)}   🔴 เสี่ยงเฉลยรั่ว')
    L.append(f'  ธงติดแต่ไม่มี marker ที่ไหนเลย  = {len(imgflag_nomarker)}   ⬜ รูปอยู่ไหนไม่รู้')
    L.append(f'🔴 โจทย์อ้าง "ดูรูป/ดูตาราง" แต่ hasImage=false = {len(noimg_but_figword)}  ← ต้องใช้ตาคน')
    L.append('')
    lv = collections.Counter(r[1] for r in rows)
    L.append(f'รวมประเด็นที่พบ = {len(rows)}  (' + ' · '.join(f'{k}:{v}' for k, v in lv.items()) + ')')
    L.append('')
    L.append('--- 10 บทที่มีข้อมากที่สุด ---')
    for t, c in bychap.most_common(10): L.append(f'  {c:5d}  {t}')
    txt = '\n'.join(L)
    open(out + '_summary.txt', 'w', encoding='utf-8').write(txt)
    with open(out + '_issues.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f); w.writerow(['id', 'ระดับ', 'เรื่อง', 'รายละเอียด']); w.writerows(rows)
    print(txt)
    print(f'\n📄 เขียนแล้ว: {out}_summary.txt · {out}_issues.csv ({len(rows)} แถว)')

if __name__ == '__main__':
    main()

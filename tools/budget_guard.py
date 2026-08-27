#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""budget_guard.py — เฝ้าผลงานรายรอบ: ได้ของใหม่กี่ข้อ · ซ้ำไหม · ใช้งบไปเท่าไร
ใช้: python budget_guard.py [--done _t1run\results] [--log _t1run\budget_log.csv] [--per-item-token 2800]
ทุกครั้งที่รัน จะบันทึก 1 แถวลง log และเตือนถ้า "ได้ของใหม่ 0" หรือ "พบฉบับซ้ำ"
"""
import json, os, glob, csv, argparse, datetime, collections

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--done', nargs='*', default=[os.path.join('_t1run', 'results')])
    ap.add_argument('--log', default=os.path.join('_t1run', 'budget_log.csv'))
    ap.add_argument('--per-item-token', type=int, default=2800)
    ap.add_argument('--exclude', default='MASTER,ALL,pilot', help='ข้ามไฟล์ที่ชื่อมีคำเหล่านี้ (คั่นด้วย ,) — กันนับซ้ำจากไฟล์รวม')
    a = ap.parse_args()
    files = []
    for p in a.done:
        files += [p] if os.path.isfile(p) else glob.glob(os.path.join(p, '**', '*.json'), recursive=True)
    skip = [w for w in a.exclude.split(',') if w]
    files = [f for f in files if not any(w.lower() in os.path.basename(f).lower() for w in skip)]
    cnt = collections.Counter(); nrec = 0; chars = 0
    for f in sorted(files):
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        if not (isinstance(d, list) and d and isinstance(d[0], dict) and 'steps' in d[0]): continue
        for r in d:
            cnt[r['id']] += 1; nrec += 1; chars += len(json.dumps(r, ensure_ascii=False))
    uniq = len(cnt); dup = nrec - uniq
    prev = 0
    if os.path.exists(a.log):
        try: prev = int(list(csv.DictReader(open(a.log, encoding='utf-8-sig')))[-1]['id_ไม่ซ้ำสะสม'])
        except Exception: prev = 0
    newly = uniq - prev
    est = nrec * a.per_item_token
    row = [datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), nrec, uniq, dup, newly, f'{est:,}', f'{chars:,}']
    head = ['เวลา', 'ฉบับทั้งหมด', 'id_ไม่ซ้ำสะสม', 'ฉบับซ้ำ', 'ใหม่ตั้งแต่ครั้งก่อน', 'ประมาณ_token_ที่ใช้', 'อักษรรวม']
    new_file = not os.path.exists(a.log)
    with open(a.log, 'a', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        if new_file: w.writerow(head)
        w.writerow(row)
    print(f'ฉบับทั้งหมด {nrec:,} · id ไม่ซ้ำ {uniq:,} · ฉบับซ้ำ {dup:,} · ใหม่ตั้งแต่ครั้งก่อน {newly:,}')
    print(f'ประมาณ token ที่จ่ายไปกับทั้งหมด ~{est:,} (ที่ {a.per_item_token:,}/ฉบับ)')
    bad = False
    if dup: print(f'🔴 พบฉบับซ้ำ {dup:,} — แปลว่ามีรอบที่ทำข้อเดิมซ้ำ ให้ตรวจ DONE.json ทันที'); bad = True
    if prev and newly == 0: print('🔴 ได้ของใหม่ 0 ตั้งแต่ครั้งก่อน — ให้หยุดงานอัตโนมัติแล้วตรวจคิว'); bad = True
    if not bad: print('✅ ปกติ — ไม่มีฉบับซ้ำ และมีของใหม่เพิ่ม')
    print(f'📄 บันทึกลง {a.log}')

if __name__ == '__main__': main()

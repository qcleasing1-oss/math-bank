#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""status_md.py — สรุปสถานะโปรเจคเป็นไฟล์เดียว ใช้เปิดแชทใหม่โดยไม่ต้องเล่าประวัติซ้ำ (ประหยัด token ตรง ๆ)
ใช้: python status_md.py [--out STATUS.md]
"""
import json, os, re, glob, argparse, collections, datetime

def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--done', nargs='*', default=[os.path.join('_t1run', 'results')])
    ap.add_argument('--queue', default=os.path.join('_t1run', 'QUEUE_now.json'))
    ap.add_argument('--out', default='STATUS.md')
    a = ap.parse_args()
    items = load_bank(a.bank) if os.path.exists(a.bank) else []
    dn, files, last = set(), 0, ''
    for p in a.done:
        for f in ([p] if os.path.isfile(p) else glob.glob(os.path.join(p, '**', '*.json'), recursive=True)):
            try: d = json.load(open(f, encoding='utf-8'))
            except Exception: continue
            if isinstance(d, list) and d and isinstance(d[0], dict) and 'steps' in d[0]:
                files += 1; dn |= {x['id'] for x in d if 'id' in x}
                m = re.search(r'(20\d{6})-(\d{4})', os.path.basename(f))
                if m: last = max(last, f'{m.group(1)} {m.group(2)}')
    nq = 0
    if os.path.exists(a.queue):
        try: nq = len(json.load(open(a.queue, encoding='utf-8')))
        except Exception: pass
    byset = collections.Counter(); dset = collections.Counter()
    for q in items:
        s = q.get('setId', '?'); byset[s] += 1
        if q['id'] in dn: dset[s] += 1
    started = [(s, dset[s], byset[s]) for s in byset if dset[s]]
    started.sort(key=lambda r: -(r[1] / r[2]))
    ts = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    L = [f'# STATUS — คลังข้อสอบ/เฉลยละเอียด (สร้างอัตโนมัติ {ts})', '',
         '> ไฟล์นี้สร้างจากไฟล์จริงด้วย `python tools\\status_md.py` — เปิดแชทใหม่ให้ AI อ่านไฟล์นี้ไฟล์เดียวพอ', '',
         '## ตัวเลขหลัก', '',
         f'- คลังทั้งหมด: **{len(items):,} ข้อ**',
         f'- มีเฉลยละเอียด t1 แล้ว: **{len(dn):,} ข้อ** ({len(dn)/max(1,len(items))*100:.1f}%) จากไฟล์ผล {files} ไฟล์',
         f'- เหลือ: **{len(items)-len(dn):,} ข้อ** · อยู่ในคิวตอนนี้: **{nq:,} ข้อ**',
         f'- รอบล่าสุดที่มีผล: **{last or "—"}**', '',
         '## ชุดที่เริ่มแล้ว (เรียงตาม % คืบหน้า)', '',
         '| ชุด | เสร็จ/ทั้งหมด | % |', '|---|---|---|']
    for s, d, n in started[:25]:
        L.append(f'| `{s}` | {d}/{n} | {d/n*100:.0f}% |')
    if len(started) > 25: L.append(f'| … อีก {len(started)-25} ชุด | | |')
    L += ['', '## ไฟล์สำคัญ', '',
          '- คลังต้นฉบับ: `data/bank.json` · สารบัญบท/หัวข้อย่อย: `data/manifest.json`',
          '- ผลเฉลยรายรอบ: `_t1run/results/` · ไฟล์รวม: `_t1run/results/t1_MASTER.json`',
          '- เครื่องมือทั้งหมด + วิธีใช้: `tools/README-เครื่องมือ.md`',
          '- หน้าติดตามงาน: `_t1run/progress.html`', '',
          '## กติกาที่ผูกไว้ (ห้ามลืม)', '',
          '1. ⛔ ห้ามเริ่มงานทิ้งไว้ ก่อนรัน 2 รอบต่อหน้าครูและพิสูจน์ว่ารอบ 2 หยิบคนละข้อ',
          '2. คิว = คลัง − DONE เสมอ · หดคิวทุกรอบไม่มีเงื่อนไข',
          '3. รอบไหนได้ของใหม่ 0 ⇒ หยุดทั้งชุดแล้วแจ้ง',
          '4. ⛔ ห้ามแต่งข้อมูลที่โจทย์ไม่ได้ให้ (เช่นสร้างตารางเอง) — ให้ข้ามแล้วจดถามครู',
          '5. ⛔ ห้ามรายงานตัวเลขจากสคริปต์ที่ยังไม่ได้เปิดดูตัวอย่างจริง ≥ 3 ตัวอย่าง']
    open(a.out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(f'✅ {a.out} · คลัง {len(items):,} · เสร็จ {len(dn):,} · ชุดที่เริ่มแล้ว {len(started)}')

if __name__ == '__main__': main()

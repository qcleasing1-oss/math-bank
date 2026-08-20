#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""token_estimate.py — ประเมินราคาก่อนสั่งงาน (ดูราคาก่อนจ่าย)
ใช้: python token_estimate.py --items 500            # จะทำอีก 500 ข้อ ราคาเท่าไร
     python token_estimate.py --rest                 # ทำให้ครบทั้งคลังราคาเท่าไร
ฐานราคา = วัดจากเฉลยที่ทำเสร็จแล้วจริง ⛔ ไม่ใช่ตัวเลขที่แต่งขึ้น
"""
import json, os, glob, argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--done', nargs='*', default=[os.path.join('_t1run', 'results')])
    ap.add_argument('--items', type=int)
    ap.add_argument('--rest', action='store_true')
    ap.add_argument('--per-round', type=int, default=40)
    a = ap.parse_args()
    recs = {}
    for p in a.done:
        for f in ([p] if os.path.isfile(p) else glob.glob(os.path.join(p, '**', '*.json'), recursive=True)):
            try: d = json.load(open(f, encoding='utf-8'))
            except Exception: continue
            if isinstance(d, list) and d and isinstance(d[0], dict) and 'steps' in d[0]:
                for r in d: recs[r['id']] = r
    if not recs: print('🔴 ยังไม่มีเฉลยให้ใช้เป็นฐานวัด'); return
    chars = [len(json.dumps(r, ensure_ascii=False)) for r in recs.values()]
    avg = sum(chars) / len(chars)
    th = sum(sum(1 for c in json.dumps(r, ensure_ascii=False) if '\u0e00' <= c <= '\u0e7f') for r in recs.values()) / sum(chars)
    lo_per = avg * (th / 2.0 + (1 - th) / 4.0)
    hi_per = avg * (th / 1.0 + (1 - th) / 2.5)
    n = a.items
    if a.rest:
        d = json.load(open(a.bank, encoding='utf-8'))
        items = d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))
        n = len(items) - len(recs)
    if not n: print('ระบุ --items <จำนวน> หรือ --rest'); return
    print(f'ฐานวัดจากของจริง {len(recs):,} ข้อ · เฉลี่ย {avg:,.0f} อักษร/ข้อ (อักษรไทย {th*100:.0f}%)')
    print(f'ประมาณ {lo_per:,.0f}–{hi_per:,.0f} output token ต่อ 1 ข้อ')
    print(f'\nถ้าทำอีก {n:,} ข้อ:')
    print(f'  ≈ {n*lo_per/1e6:.1f} – {n*hi_per/1e6:.1f} ล้าน output token')
    print(f'  ≈ {-(-n//a.per_round):,} รอบ (รอบละ {a.per_round} ข้อ) · รอบละ ~{a.per_round*lo_per/1000:,.0f}–{a.per_round*hi_per/1000:,.0f}k token')
    print('\n⚠️ ⛔ ไม่รวม input token ที่ทุกรอบต้องอ่านคิว+สเปกใหม่ ⇒ ของจริงสูงกว่านี้')
    print('   วิธีได้ตัวเลขจริงของบัญชีตัวเอง: จดเลข % ในหน้า Usage ก่อน/หลังรัน 2 รอบ แล้วเทียบ')

if __name__ == '__main__': main()

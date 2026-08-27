#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""old_vs_new.py — เทียบ "เฉลยเก่าในคลัง" vs "เฉลย t1 ใหม่" vs "เฉลยจริง (correct)" ทั้งคลัง
ใช้: python old_vs_new.py [--bank data\bank.json] [--done _t1run\results] [--out old_vs_new.csv]
ออก: CSV ต่อ 1 ข้อ — ตรงเฉลยไหม (เก่า/ใหม่) · ธงที่ควรให้ตาคนดู   ค่า token = 0
⚠️ ตัวเทียบเป็นการจับข้อความ ⇒ อาจมีสัญญาณลวง — ให้ใช้เป็น "รายการที่ต้องเปิดดู" ⛔ ไม่ใช่คำตัดสิน
"""
import json, os, re, glob, csv, argparse

def S(v): return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))
def norm(x):
    t = re.sub(r'\\left|\\right|\\text|\\mathrm|<[^>]+>', '', S(x)).replace('dfrac', 'frac').replace('tfrac', 'frac')
    return re.sub(r'[\s$\\{}()\[\],"\']', '', t)
def pick(blob, q):
    """เดาว่า 'ตอบข้อไหน' จากข้อความ — คืน index หรือ None"""
    ch = q.get('choices') or []
    nb = norm(blob)
    for i, c in enumerate(ch):
        n = norm(c)
        if n and len(n) > 3 and n in nb: return i
    m = re.search(r'(?:ตัวเลือกที่|ตัวเลือก|ข้อที่|ข้อ)\s*([1-9])', S(blob))
    if m: return int(m.group(1)) - 1
    for i, c in enumerate(ch):
        n = norm(c)
        if n and n in nb: return i
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--done', nargs='*', default=[os.path.join('_t1run', 'results')])
    ap.add_argument('--out', default='old_vs_new.csv')
    ap.add_argument('--all', action='store_true', help='รวมกลุ่ม 🟡 (เฉลยเก่าไม่ตรง) ซึ่งสัญญาณลวงเยอะ')
    a = ap.parse_args()
    bank = {q['id']: q for q in load_bank(a.bank)}
    new = {}
    files = []
    for p in a.done:
        files += [p] if os.path.isfile(p) else glob.glob(os.path.join(p, '**', '*.json'), recursive=True)
    for f in sorted(files):
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        if isinstance(d, list) and d and isinstance(d[0], dict) and 'steps' in d[0]:
            for r in d: new[r['id']] = r
    rows = []; flag = 0
    for i, q in bank.items():
        cor = q.get('correct')
        if not isinstance(cor, int): continue
        old_pick = pick(q.get('explanation') or '', q)
        n = new.get(i)
        new_pick = pick(S(n['steps'][-1].get('eq') if n else '') + S(n.get('verify', {}) if n else ''), q) if n else None
        f_old = '' if old_pick is None else ('ตรง' if old_pick == cor else 'ไม่ตรง')
        f_new = '' if new_pick is None else ('ตรง' if new_pick == cor else 'ไม่ตรง')
        note = []
        if f_old == 'ไม่ตรง' and f_new == 'ไม่ตรง': note.append('🔴 ทั้งเก่าและใหม่ไม่ตรงเฉลย — เฉลยในคลังอาจผิด')
        elif f_new == 'ไม่ตรง': note.append('🟠 เฉลยใหม่ไม่ตรง')
        elif f_old == 'ไม่ตรง': note.append('🟡 เฉลยเก่าไม่ตรง (ใหม่ตรง)')
        if not note: continue
        if note[0].startswith('🟡') and not a.all: continue
        flag += 1
        rows.append([i, q.get('setId', ''), q.get('difficulty', ''), 'ใช่' if n else '', f_old, f_new, ' · '.join(note),
                     S(q.get('question'))[:120].replace('\n', ' ')])
    with open(a.out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f); w.writerow(['id', 'ชุด', 'ความยาก', 'มีเฉลยใหม่แล้ว', 'เฉลยเก่า', 'เฉลยใหม่', 'ธง', 'โจทย์ 120 อักษรแรก']); w.writerows(rows)
    print(f'✅ {a.out} · ตรวจ {len(bank):,} ข้อ · มีเฉลยใหม่ {len(new):,} · ธงที่ต้องเปิดดู {flag:,} แถว')
    print('   (ค่าเริ่มต้นแสดงเฉพาะ 🔴 ทั้งเก่าและใหม่ไม่ตรง กับ 🟠 เฉลยใหม่ไม่ตรง · เติม --all เพื่อดู 🟡 ด้วย)')
    print('   ⚠️ เป็นรายการให้เปิดดู ⛔ ไม่ใช่คำตัดสิน — ตัวเทียบจับข้อความ อาจมีสัญญาณลวง')

if __name__ == '__main__': main()

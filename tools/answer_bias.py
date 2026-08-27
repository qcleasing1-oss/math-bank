#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""answer_bias.py — ตรวจอคติของเฉลย: เฉลยกระจุกอยู่ตัวเลือกไหน · ตัวลวงยาวผิดปกติจนชี้เฉลย
ใช้: python answer_bias.py [--bank data\bank.json] [--out answer_bias.csv]
"""
import json, os, csv, argparse, collections

def S(v): return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--out', default='answer_bias.csv')
    a = ap.parse_args()
    items = load_bank(a.bank)
    pos = collections.defaultdict(collections.Counter); byset = collections.defaultdict(collections.Counter)
    rows = []; longest = 0
    for q in items:
        ch = q.get('choices') or []; c = q.get('correct')
        if not ch or not isinstance(c, int) or not (0 <= c < len(ch)): continue
        pos[len(ch)][c + 1] += 1; byset[q.get('setId', '')][c + 1] += 1
        L = [len(S(x)) for x in ch]
        if L[c] == max(L) and max(L) > 1.35 * (sum(L) - L[c]) / max(1, len(L) - 1):
            longest += 1
            rows.append([q['id'], q.get('setId', ''), c + 1, L[c], f'{(sum(L)-L[c])/max(1,len(L)-1):.0f}',
                         'เฉลยยาวกว่าตัวลวงมาก — เดาได้จากความยาว'])
    tot = sum(sum(c.values()) for c in pos.values())
    print(f'ตรวจ {tot:,} ข้อที่เป็นปรนัย')
    print('ตำแหน่งเฉลย (แยกตามจำนวนตัวเลือก — เทียบข้ามกลุ่มไม่ได้):')
    for nc in sorted(pos):
        c = pos[nc]; t = sum(c.values()); exp = t / nc
        sk = max(abs(c.get(k, 0) - exp) for k in range(1, nc + 1)) / exp * 100
        dist = ' · '.join(f'ข้อ {k}: {c.get(k,0)} ({c.get(k,0)/t*100:.0f}%)' for k in range(1, nc + 1))
        verdict = '✅ สมดุล' if sk < 25 else '🔴 กระจุกผิดปกติ'
        print(f'  แบบ {nc} ตัวเลือก ({t:,} ข้อ): {dist}  ⇒ เบี่ยงสูงสุด {sk:.0f}% {verdict}')
        if sk >= 25: rows.append([f'(ทั้งคลัง) ข้อแบบ {nc} ตัวเลือก', '', '', '', '', f'ตำแหน่งเฉลยเบี่ยง {sk:.0f}%'])
    bad = [(s, c) for s, c in byset.items() if sum(c.values()) >= 20 and max(c.values()) / sum(c.values()) > 0.45]
    for s, c in bad:
        t = sum(c.values()); k, v = c.most_common(1)[0]
        rows.append([f'(ทั้งชุด) {s}', s, k, '', '', f'ชุดนี้เฉลยเป็นข้อ {k} ถึง {v}/{t} = {v/t*100:.0f}%'])
        print(f'🔴 ชุด {s}: เฉลยเป็นข้อ {k} ถึง {v}/{t} ({v/t*100:.0f}%)')
    with open(a.out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f); w.writerow(['id/ชุด', 'ชุด', 'ตำแหน่งเฉลย', 'ยาว(เฉลย)', 'ยาวเฉลี่ย(ตัวลวง)', 'ข้อสังเกต']); w.writerows(rows)
    print(f'✅ {a.out} · ข้อที่เฉลยยาวจนเดาได้ {longest:,} ข้อ · ชุดที่เฉลยกระจุก {len(bad)} ชุด')

if __name__ == '__main__': main()

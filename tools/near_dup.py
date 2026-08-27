#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""near_dup.py — หาโจทย์ซ้ำ/คล้ายกันเองในคลัง (ไม่ใช้ AI · ใช้ลายนิ้วมือข้อความ)
ใช้: python near_dup.py [--bank data\bank.json] [--out near_dup.csv] [--th 0.82] [--same-topic]
th = ความคล้ายขั้นต่ำ 0-1 (0.82 = คล้ายมาก)
"""
import json, os, re, csv, argparse, collections

def S(v): return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))
def norm(t):
    t = re.sub(r'\[IMAGE[^\]]*\]|<[^>]+>', ' ', S(t))
    t = re.sub(r'\\left|\\right|\\dfrac|\\frac|\\text\{[^}]*\}', ' ', t)
    return re.sub(r'\s+', '', re.sub(r'[^\w฀-๿]+', ' ', t))
def shingles(t, k=6):
    return {t[i:i+k] for i in range(0, max(1, len(t)-k+1))}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--out', default='near_dup.csv')
    ap.add_argument('--th', type=float, default=0.82)
    ap.add_argument('--same-topic', action='store_true', help='เทียบเฉพาะข้อที่อยู่บทเดียวกัน (เร็วกว่ามาก)')
    a = ap.parse_args()
    items = load_bank(a.bank)
    recs = []
    for q in items:
        t = norm(q.get('question'))
        if len(t) < 25: continue
        recs.append({'id': q['id'], 'set': q.get('setId', ''), 'topic': str((q.get('topics') or [q.get('topic')])[0]),
                     't': t, 'sh': shingles(t), 'q': S(q.get('question'))[:110].replace('\n', ' ')})
    # ทำดัชนีจากชิ้นข้อความ เพื่อไม่ต้องเทียบทุกคู่ (6,477² = 21 ล้านคู่)
    idx = collections.defaultdict(list)
    for i, r in enumerate(recs):
        for s in list(r['sh'])[:60]: idx[s].append(i)
    seen, rows = set(), []
    for i, r in enumerate(recs):
        cand = collections.Counter()
        for s in list(r['sh'])[:60]:
            for j in idx[s]:
                if j > i: cand[j] += 1
        for j, c in cand.items():
            if c < 8: continue
            o = recs[j]
            if a.same_topic and o['topic'] != r['topic']: continue
            inter = len(r['sh'] & o['sh']); union = len(r['sh'] | o['sh'])
            sim = inter / union if union else 0
            if sim >= a.th and (i, j) not in seen:
                seen.add((i, j))
                rows.append([f'{sim:.3f}', r['id'], o['id'], r['set'], o['set'],
                             'บทเดียวกัน' if r['topic'] == o['topic'] else 'คนละบท', r['q'], o['q']])
    rows.sort(key=lambda x: -float(x[0]))
    with open(a.out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f); w.writerow(['ความคล้าย', 'id_A', 'id_B', 'ชุด_A', 'ชุด_B', 'บท', 'โจทย์_A', 'โจทย์_B']); w.writerows(rows)
    print(f'✅ {a.out} · เทียบ {len(recs):,} ข้อ · พบคู่ที่คล้ายกัน ≥ {a.th} = {len(rows):,} คู่')
    print('   ⚠️ คู่ที่คล้ายไม่ได้แปลว่าซ้ำเสมอ — โจทย์คนละปีอาจเปลี่ยนแค่ตัวเลข ⇒ ให้เปิดดูก่อนตัดสิน')

if __name__ == '__main__': main()

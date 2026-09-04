#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""answer_bias.py v2.0 — ตรวจอคติของเฉลย · สามแขน สามหน่วย ⛔ ห้ามยุบเป็นเลขเดียว

ใช้: python tools/answer_bias.py --out <ที่เก็บ.csv> [--bank data/bank.json]
     python tools/answer_bias.py --out out/ab.csv --set gen-chap-07-trigonometry --since-question 185
     python tools/answer_bias.py --out out/ab.csv --set gen-chap-07-trigonometry --tail 60

🔑 สามแขน — **หน่วยต่างกัน ตัวหารต่างกัน** (มติ ใบ 130 §4 · ใบ 131 §4 · ครูเคาะ 4 ก.ย. 69):
     แขน ก   ต่อ **ชุด** ทั้งชุด            > 45%          ⇒ เตือน   (เดิม ⛔ ไม่แตะเกณฑ์)
     แขน ข   ต่อ **ก้อนที่เพิ่งเติม**        > 40%          ⇒ เตือน
     แขน ข2  ต่อ **หน้าต่าง 10 ข้อติดกัน**   >= 5 ต่อ index ⇒ เตือน  (กฎใบ 127 ตรงตัว ⛔ ไม่แปลงเป็น %)

🔴 ทำไมต้องมีสามแขน — วัดจริงกับก้อน q185-q244 ของชุดตรีโกณ (4 ก.ย. 69):
     แขน ก อ่านชุด 244 ข้อ ⇒ 75/216 = 34.7% ⇒ **เขียว** (ต่ำกว่า 45%)
     แขน ข อ่านก้อน 60 ข้อ ⇒ 29/60  = 48.3% ⇒ แดง
     แขน ข2 อ่านทีละ 10   ⇒ **5 จาก 6 ก้อนย่อยแดง** · หน้าต่างเลื่อนแดง 33/51 · แย่สุด 7/10
   ⇒ ⇒ ยิ่งตัวหารใหญ่ ความเบี่ยงยิ่งถูกเจือจาง ⇒ "เทของเบี่ยงลงถังที่ใหญ่กว่า" (ใบ 129)
      และเกณฑ์ 40% ต่อก้อน 60 ข้อ ยอมได้ถึง 24/60 ⇒ แขน ข อย่างเดียวยังหลวมกว่ากฎใบ 127

⛔ ค่าปริยายของ --out ถูกถอดออกแล้ว (ครูเคาะ 4 ก.ย. 69 · ใบ 131 §7):
   ของเดิม default 'answer_bias.csv' ⇒ เขียนลงโฟลเดอร์ที่บังเอิญยืนอยู่ = รากโปรเจคของครู

รหัสออก: 0 = ผ่าน/เตือน (ค่าปริยาย) · 1 = แดง เมื่อสั่ง --enforce · 2 = เครื่องมือ/ข้อมูลเทียบไม่ได้
⛔ ค่าปริยาย ⛔ ไม่ตั้ง 1 โดยตั้งใจ — รอบแรกให้ครูเห็นตัวเลขทั้งคลังก่อน (คำขอ E ใบ 132 §4)
"""
import argparse
import collections
import csv
import json
import os
import re
import sys

VERSION = '2.4'
SET_MAX = 0.45          # แขน ก · ต่อชุด
SET_MIN_N = 20          # แขน ก · ตัวหารขั้นต่ำที่ยอมตัดสิน
CHUNK_MAX = 0.40        # แขน ข · ต่อก้อนที่เพิ่งเติม
WINDOW = 10             # แขน ข2 · ความกว้างหน้าต่าง (กฎใบ 127)
WINDOW_MAX = 4          # แขน ข2 · ยอมได้ไม่เกิน 4 ต่อ index ⇒ 5 ขึ้นไป = แดง


def pb_tail(ps, x):
    r"""P(ผลรวมของ Bernoulli ที่ความน่าจะเป็นไม่เท่ากัน >= x) — Poisson-binomial แบบตรง (DP)

    🔑 ทำไมต้องมี (ใบ 136 §5 ของ E): ชุดที่ **จำนวนตัวเลือกคละ** (4 กับ 5 ปนกัน)
       ถ้าเลือก k ตัวเดียวมาแทนทั้งชุด ผลต่างกันได้ 80 เท่า (max vs พบบ่อยสุด)
       ⇒ ⛔ ไม่ต้องเลือก k เลย — ใส่ 1/k ของข้อนั้น ๆ เข้าไปตรง ๆ
    """
    if x <= 0:
        return 1.0
    dist = [1.0]
    for q in ps:
        nxt = [0.0] * (len(dist) + 1)
        for i, w in enumerate(dist):
            nxt[i] += w * (1 - q)
            nxt[i + 1] += w * q
        dist = nxt
    if x > len(dist) - 1:
        return 0.0
    return sum(dist[x:])


def p_index_ge(n, k, thr):
    r"""P(index ที่ระบุไว้ล่วงหน้า ถูกเลือก >= thr ครั้ง ใน n ข้อ ที่มี k ตัวเลือก สุ่มสม่ำเสมอ)"""
    from math import comb
    q = 1.0 / k
    return sum(comb(n, i) * q ** i * (1 - q) ** (n - i) for i in range(thr, n + 1))


def fmt_p(p):
    r"""พิมพ์ค่า p ให้อ่านออกเสมอ — ⛔ ห้ามพิมพ์ 0.00% ให้ค่าที่เล็กมากหายไป"""
    if p is None:
        return 'n/a'
    if p >= 0.001:
        return '%.2f%%' % (p * 100)
    return '%.1e' % p


def binom_tail(m, p, x):
    r"""P(X >= x) เมื่อ X ~ Binomial(m, p)"""
    from math import comb
    if x <= 0:
        return 1.0
    return sum(comb(m, i) * p ** i * (1 - p) ** (m - i) for i in range(x, m + 1))


def longest_run(seq):
    r"""คืน (ความยาวช่วงที่ค่าเท่ากันติดกันยาวสุด, ค่านั้น, ตำแหน่งเริ่ม)"""
    best = (0, None, 0)
    cur = 1
    for i in range(1, len(seq) + 1):
        if i < len(seq) and seq[i] == seq[i - 1]:
            cur += 1
        else:
            if cur > best[0]:
                best = (cur, seq[i - 1], i - cur)
            cur = 1
    return best


def arm_b2b(chunkvals, kmode):
    r"""แขน ข2ข · ก้อนย่อย 10 ข้อที่กระจุกที่ **index เดียวกัน** — คืน (จำนวนก้อน, index, ก้อนที่โดน, p)

    🔑 ทำไมต้องเป็น "index เดียวกัน" (ข้อเสนอ E ใบ 134 §2):
       กระจุกที่ index กระจาย = ความบังเอิญ · กระจุกที่ index เดิมทุกก้อน = **ลายนิ้วมือของนิสัยการแต่ง**
       ⬤ ก้อน 60 ข้อของ MB: index ใดก็ได้ >= 5 ใน 5/6 ก้อน = 1.29%
          แต่ index เดิมทุกก้อน = 0.0016% (คูณ 4 index = 0.0065%) ⇒ ต่างกัน ~200 เท่า
    """
    chunks = [chunkvals[i:i + WINDOW] for i in range(0, len(chunkvals), WINDOW)]
    chunks = [c for c in chunks if len(c) == WINDOW]
    m = len(chunks)
    if m == 0:
        return 0, None, 0, None
    hits = collections.Counter()
    for c in chunks:
        cc = collections.Counter(c)
        for idx, v in cc.items():
            if v > WINDOW_MAX:
                hits[idx] += 1
    if not hits:
        return m, None, 0, 1.0
    idx, x = hits.most_common(1)[0]
    p_one = p_index_ge(WINDOW, kmode, WINDOW_MAX + 1)
    p = min(1.0, binom_tail(m, p_one, x) * kmode)      # คูณ kmode = เผื่อว่าเลือก index ไหนก็ได้
    return m, idx, x, p


def arm_b3(vals, kmode):
    r"""แขน ข3 · ช่วงเฉลยเดียวกันติดกันยาวสุด — คืน (ยาว, index, ตำแหน่งเริ่ม, p)"""
    L, idx, start = longest_run(vals)
    n = len(vals)
    if L < 2 or n < 2:
        return L, idx, start, 1.0
    # P(มีช่วงยาว >= L ที่ไหนสักแห่ง) ≈ (n - L + 1) · k · (1/k)^L   (ขอบบน ⇒ เข้าข้างการ "ไม่แดง")
    p = min(1.0, (n - L + 1) * kmode * (1.0 / kmode) ** L)
    return L, idx, start, p


P_RED = 0.001      # 🔴 แดง · ปิดกั้น              (มติครู 4 ก.ย. 69 · ใบ 138 §4)
P_AMBER = 0.01     # 🟠 รอคนเซ็น · ⛔ ไม่ปิดกั้น แต่ ⛔ ไม่ใช่ "ผ่าน"
PERM_N = 20000     # จำนวนรอบสลับของ permutation test
PERM_SEED = 20260904
PERM_SCREEN = 0.01 # รันสลับเฉพาะชุดที่ null-A ต่ำกว่านี้ (ประหยัดเวลา · ประกาศไว้ ⛔ ไม่ซ่อน)
PERM_MAX = 200000  # เพดานรอบเมื่อค่าตกใกล้เส้นแบ่ง (E ใบ 140 §4)


def wilson(k, n, z=1.96):
    r"""ช่วงความเชื่อมั่น 95% ของสัดส่วน (Wilson) — ⛔ ไม่ใช้ normal approx เพราะ k เล็กมาก"""
    import math
    if n == 0:
        return (0.0, 1.0)
    ph = k / n
    d = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / d
    h = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def near_edge(p):
    r"""ค่านี้ตกใกล้เส้นแบ่งจนจำนวนรอบตัดสินแทนข้อมูลไหม (E ใบ 140 §4)"""
    if p is None:
        return False
    return any(0.3 * t < p < 3 * t for t in (P_RED, P_AMBER))


def fmt_perm_full(p, k, n):
    r"""พิมพ์ p จาก permutation พร้อมของที่ทำให้แปลได้: จำนวนครั้งจริง · N · ช่วง 95%"""
    if p is None:
        return 'n/a'
    if k == 0:
        return '< %s (เจอ 0/%s ⇒ **ขอบบน** ⛔ ไม่ใช่ค่าที่วัดได้)' % (fmt_p(1.0 / (n + 1)), format(n, ','))
    lo, hi = wilson(k, n)
    return '%s (เจอ %s/%s · ช่วง 95%% [%s, %s])' % (fmt_p(p), format(k, ','), format(n, ','),
                                                    fmt_p(lo), fmt_p(hi))



def tier(p):
    r"""สามชั้นตามมติครู 4 ก.ย. 69 — ชั้นกลางคือ **รอคนเซ็น** ⛔ ไม่ใช่ ผ่าน"""
    if p is None:
        return '⬜ วัดไม่ได้'
    if p < P_RED:
        return '🔴 แดง · ปิดกั้น'
    if p < P_AMBER:
        return '🟠 รอคนเซ็น'
    return '✅ ผ่าน'


def fmt_perm(p, n=PERM_N):
    r"""ค่า p จาก permutation ที่ชนพื้น = **ขอบบน** ⛔ ไม่ใช่ค่าที่วัดได้ ⇒ ต้องพิมพ์ < ให้เห็น"""
    floor = 1.0 / (n + 1)
    return ('< ' + fmt_p(floor)) if p is not None and p <= floor + 1e-15 else fmt_p(p)


def perm_null(vals, idx_block, obs_blocks, run_len, n_iter=PERM_N, seed=PERM_SEED):
    r"""null-B แบบ permutation — สลับลำดับเฉลยทั้งชุด **คงจำนวนของแต่ละ index ไว้เท่าเดิม**

    🔑 ใช้เมื่อ **หน่วยที่ถูกตัดสินคือทั้งชุด** ⇒ ⛔ ไม่มี "ส่วนที่เหลือ" ให้อ้างอิง (E ใบ 138 §1)
       คำถามที่มันตอบ: "การ *จัดเรียง* กระจุกเกินบังเอิญไหม" ⛔ ไม่ใช่ "ชุดนี้เอียงไหม"
       (ความเอียงถูกคงไว้ในทุกการสลับ ⇒ ถูกหักออกจากคำถามโดยอัตโนมัติ)
    ⛔ ค่าที่ได้เป็นค่าประมาณจากการสุ่ม ⇒ พิมพ์จำนวนรอบติดไปด้วยเสมอ
    """
    import random
    rnd = random.Random(seed)
    arr = list(vals)
    hit_b = hit_r = 0
    for _ in range(n_iter):
        rnd.shuffle(arr)
        if obs_blocks is not None:
            b = sum(1 for i in range(0, len(arr) - WINDOW + 1, WINDOW)
                    if arr[i:i + WINDOW].count(idx_block) > WINDOW_MAX)
            if b >= obs_blocks:
                hit_b += 1
        if run_len:
            L, _v, _st = longest_run(arr)
            if L >= run_len:
                hit_r += 1
    pb = (hit_b + 1) / (n_iter + 1) if obs_blocks is not None else None
    pr = (hit_r + 1) / (n_iter + 1) if run_len else None
    return pb, pr, hit_b, hit_r, n_iter


def perm_refine(vals, idx_block, obs_blocks, run_len):
    r"""สลับ แล้ว **รันซ้ำรอบ 10 เท่า** ถ้าค่าตกใกล้เส้นแบ่ง (E ใบ 140 §4)

    เหตุ: p = 8.5e-04 ที่ 20,000 รอบ = "เจอ 17 ครั้ง" ⇒ ช่วง 95% คร่อมเกณฑ์ 0.001
       ⇒ ชั้นของมันถูกตัดสินโดย **จำนวนรอบที่เราเลือก** ⛔ ไม่ใช่โดยข้อมูล
    """
    n = PERM_N
    while True:
        pb, pr, kb, kr, _ = perm_null(vals, idx_block, obs_blocks, run_len, n_iter=n)
        if n >= PERM_MAX or not (near_edge(pb) or near_edge(pr)):
            return pb, pr, kb, kr, n
        n = min(n * 10, PERM_MAX)
MIN_REF = 30       # ตัวหารขั้นต่ำของ "แหล่งอ้างอิง" ที่จะใช้คิด null แบบ conditioned


def blocks_of(seq, width):
    r"""ตัดเป็นบล็อกเต็มความกว้างเท่านั้น — เศษท้ายทิ้ง ⛔ ไม่นับครึ่งบล็อก"""
    out = [seq[i:i + width] for i in range(0, len(seq), width)]
    return [b for b in out if len(b) == width]


def arm_b2b_v2(blocks, ref_rate, idx_list):
    r"""ข2ข v2 — คืน dict ของทั้งสอง null (ใบ 136 §3 ของ E · ใบ 135 §3 ของ MB)

    blocks   : รายการบล็อก · แต่ละบล็อกเป็น [(index เฉลย, จำนวนตัวเลือกของข้อนั้น), ...]
    ref_rate : {index: อัตราจริงของแหล่งอ้างอิง} — ใช้เป็น null แบบ conditioned
               ⛔ แหล่งอ้างอิงต้อง **ไม่ใช่ตัวก้อนเอง** ไม่งั้นเป็นการวัดตัวเองด้วยตัวเอง
    🔑 null สองแบบตอบคนละคำถาม:
       1/k        ⇒ "เอียงไหม" (แขน ข ตอบอยู่แล้ว ⇒ ข2ข จะยิงซ้ำ — E ใบ 136 §3)
       ref_rate   ⇒ "กระจุกเป็นบล็อก **เกินกว่าที่ความเอียงอธิบายได้** ไหม" ⇒ ของจริงที่ ข2ข ควรถาม
    """
    m = len(blocks)
    if m == 0:
        return None
    best = None
    for idx in idx_list:
        x = sum(1 for b in blocks if sum(1 for v, k in b if v == idx) > WINDOW_MAX)
        if x == 0:
            continue
        pu = [pb_tail([1.0 / k for v, k in b], WINDOW_MAX + 1) for b in blocks]
        r = ref_rate.get(idx)
        pc = None if r is None else [pb_tail([r] * len(b), WINDOW_MAX + 1) for b in blocks]
        p_uni = min(1.0, pb_tail(pu, x) * len(idx_list))
        p_con = None if pc is None else min(1.0, pb_tail(pc, x) * len(idx_list))
        cand = (idx, x, m, p_uni, p_con)
        # 🔴 4 ก.ย. 69 · แก้บั๊กที่เจอตอนไล่ gen-chap-02-logic:
        #    เลือก index ด้วย "p ที่เล็กสุด" ⇒ ได้ index ที่กระจุก **น้อยกว่า** เพราะ p ของตัวจริง
        #    ถูก clamp ที่ 1.0 ไปแล้ว ⇒ เทียบกันไม่ได้ (1.0 vs 0.81 ⇒ แพ้ทั้งที่ x = 15 vs 5)
        #    ⇒ เลือกด้วย **จำนวนบล็อกที่กระจุก (x)** ซึ่งเป็นของที่วัดตรง ⛔ ไม่ผ่านการ clamp
        key = (x, -(p_con if p_con is not None else p_uni))
        bkey = None if best is None else (best[1], -(best[4] if best[4] is not None else best[3]))
        if bkey is None or key > bkey:
            best = cand
    return best


def S(v):
    return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)


def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(
        v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))


def qnum(qid):
    r"""เลขท้าย id — ใช้เรียงลำดับ "ของที่เพิ่งเติม" ⛔ ไม่ใช้ mtime (mtime ในคลังนี้โกหกได้)"""
    m = re.search(r'(\d+)$', str(qid))
    return int(m.group(1)) if m else None


def windows_over(seq, width, cap):
    r"""คืน (จำนวนหน้าต่างทั้งหมด, จำนวนที่เกิน, (ตำแหน่ง, สูงสุด, index) ของหน้าต่างแย่สุด)"""
    if len(seq) < width:
        return 0, 0, None
    total = over = 0
    worst = None
    for i in range(len(seq) - width + 1):
        c = collections.Counter(seq[i:i + width])
        k, v = c.most_common(1)[0]
        total += 1
        if v > cap:
            over += 1
        if worst is None or v > worst[1]:
            worst = (i, v, k)
    return total, over, worst


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--out', required=True,
                    help='ที่เก็บ CSV — บังคับ ⛔ ไม่มีค่าปริยาย (ครูเคาะ 4 ก.ย. 69)')
    ap.add_argument('--set', dest='setid', default=None, help='จำกัดแขน ข/ข2 ไว้ที่ชุดเดียว')
    ap.add_argument('--since-question', type=int, default=None,
                    help='ก้อน = ข้อที่เลขท้าย id >= ค่านี้ (ต้องใช้คู่กับ --set)')
    ap.add_argument('--tail', type=int, default=None,
                    help='ก้อน = N ข้อท้ายสุดของชุด (ต้องใช้คู่กับ --set)')
    ap.add_argument('--enforce', action='store_true', help='ให้ผลที่แดงคืนรหัส 1')
    ap.add_argument('--version', action='store_true')
    a = ap.parse_args()
    if a.version:
        print(VERSION)
        return 0
    if (a.since_question is not None or a.tail is not None) and not a.setid:
        print('🔴 --since-question / --tail ต้องใช้คู่กับ --set')
        print('   เหตุ: เลขท้าย id เริ่มใหม่ในทุกชุด ⇒ ข้ามชุดแล้ว "ก้อน" ไม่มีความหมาย')
        return 2
    outdir = os.path.dirname(a.out)
    if outdir and not os.path.isdir(outdir):
        os.makedirs(outdir, exist_ok=True)

    items = load_bank(a.bank)
    pos = collections.defaultdict(collections.Counter)
    byset = collections.defaultdict(collections.Counter)
    order = collections.defaultdict(list)      # setId -> [(เลขข้อ, index เฉลย, id)]
    rows = []
    longest = 0
    for q in items:
        ch = q.get('choices') or []
        c = q.get('correct')
        if not ch or not isinstance(c, int) or not (0 <= c < len(ch)):
            continue
        sid = q.get('setId', '')
        pos[len(ch)][c + 1] += 1
        byset[sid][c + 1] += 1
        order[sid].append((qnum(q.get('id')), c + 1, q.get('id'), len(ch)))
        L = [len(S(x)) for x in ch]
        if L[c] == max(L) and max(L) > 1.35 * (sum(L) - L[c]) / max(1, len(L) - 1):
            longest += 1
            rows.append([q['id'], sid, c + 1, L[c],
                         f'{(sum(L)-L[c])/max(1,len(L)-1):.0f}',
                         'เฉลยยาวกว่าตัวลวงมาก — เดาได้จากความยาว'])

    tot = sum(sum(c.values()) for c in pos.values())
    print(f'answer_bias v{VERSION} · คลัง {a.bank}')
    print(f'ตรวจ {tot:,} ข้อที่เป็นปรนัย')
    print('ตำแหน่งเฉลย (แยกตามจำนวนตัวเลือก — เทียบข้ามกลุ่มไม่ได้):')
    for nc in sorted(pos):
        c = pos[nc]
        t = sum(c.values())
        exp = t / nc
        sk = max(abs(c.get(k, 0) - exp) for k in range(1, nc + 1)) / exp * 100
        dist = ' · '.join(f'ข้อ {k}: {c.get(k,0)} ({c.get(k,0)/t*100:.0f}%)' for k in range(1, nc + 1))
        verdict = '✅ สมดุล' if sk < 25 else '🔴 กระจุกผิดปกติ'
        print(f'  แบบ {nc} ตัวเลือก ({t:,} ข้อ): {dist}  ⇒ เบี่ยงสูงสุด {sk:.0f}% {verdict}')
        if sk >= 25:
            rows.append([f'(ทั้งคลัง) ข้อแบบ {nc} ตัวเลือก', '', '', '', '', f'ตำแหน่งเฉลยเบี่ยง {sk:.0f}%'])

    # ── แขน ก · ต่อชุด ────────────────────────────────────────────────
    print()
    print(f'แขน ก · ต่อชุดทั้งชุด (เกณฑ์ > {SET_MAX*100:.0f}% · ตัวหารขั้นต่ำ {SET_MIN_N} ข้อ)'
          f' — ตัวหาร: {len(byset)} ชุด')
    bad = [(s, c) for s, c in byset.items()
           if sum(c.values()) >= SET_MIN_N and max(c.values()) / sum(c.values()) > SET_MAX]
    for s, c in bad:
        t = sum(c.values())
        k, v = c.most_common(1)[0]
        rows.append([f'(ทั้งชุด) {s}', s, k, '', '', f'ชุดนี้เฉลยเป็นข้อ {k} ถึง {v}/{t} = {v/t*100:.0f}%'])
        print(f'🔴 ชุด {s}: เฉลยเป็นข้อ {k} ถึง {v}/{t} ({v/t*100:.0f}%)')
    if not bad:
        print('  ✅ ⛔ ไม่มีชุดไหนเกินเกณฑ์แขน ก')

    # ── แขน ข · ต่อก้อนที่เพิ่งเติม ────────────────────────────────────
    chunk = None
    chunk_red = False
    if a.setid:
        seq = sorted((x for x in order.get(a.setid, []) if x[0] is not None), key=lambda x: x[0])
        if not seq:
            print(f'🔴 ไม่พบข้อปรนัยที่อ่านเลขท้าย id ได้ในชุด {a.setid} ⇒ เทียบไม่ได้')
            return 2
        if a.since_question is not None:
            chunk = [x for x in seq if x[0] >= a.since_question]
            label = f'{a.setid} · ข้อที่เลขท้าย >= {a.since_question}'
        elif a.tail is not None:
            chunk = seq[-a.tail:]
            label = f'{a.setid} · {a.tail} ข้อท้ายสุด'
        else:
            chunk = seq
            label = f'{a.setid} · ทั้งชุด'
        n = len(chunk)
        kmode = collections.Counter(x[3] for x in chunk).most_common(1)[0][0]
        cc = collections.Counter(x[1] for x in chunk)
        k, v = cc.most_common(1)[0]
        print()
        print(f'แขน ข · ก้อนที่เพิ่งเติม (เกณฑ์ > {CHUNK_MAX*100:.0f}%) — ก้อน: {label}')
        print(f'  ตัวหาร {n} ข้อปรนัย (q{chunk[0][0]}-q{chunk[-1][0]}) ·'
              f' การกระจาย: ' + ' · '.join(f'ข้อ {i}: {cc.get(i,0)}' for i in sorted(cc)))
        if v / n > CHUNK_MAX:
            chunk_red = True
            print(f'  🔴 สูงสุด {v}/{n} ที่ข้อ {k} = {v/n*100:.1f}% ⇒ เกินเพดาน {CHUNK_MAX*100:.0f}%')
            rows.append([f'(ก้อน) {label}', a.setid, k, '', '', f'ก้อนนี้เฉลยเป็นข้อ {k} ถึง {v}/{n} = {v/n*100:.1f}%'])
        else:
            print(f'  ✅ สูงสุด {v}/{n} ที่ข้อ {k} = {v/n*100:.1f}%')

    # ── แขน ข2 · หน้าต่าง 10 ข้อติดกัน ────────────────────────────────
    print()
    print(f'แขน ข2 · หน้าต่าง {WINDOW} ข้อติดกัน (แดงเมื่อ >= {WINDOW_MAX+1} ต่อ index — กฎใบ 127 ตรงตัว)')
    win_red = False
    if chunk is not None:
        seqv = [x[1] for x in chunk]
        total_w, over_w, worst = windows_over(seqv, WINDOW, WINDOW_MAX)
        if total_w == 0:
            print(f'  ⬜ ก้อนมี {len(seqv)} ข้อ < {WINDOW} ⇒ วัดหน้าต่างไม่ได้ ⛔ ไม่ใช่ "ผ่าน"')
        else:
            mark = '🔴' if over_w else '✅'
            print(f'  {mark} หน้าต่างที่เกิน {over_w}/{total_w} หน้าต่าง ·'
                  f' แย่สุด {worst[1]}/{WINDOW} ที่ข้อ {worst[2]} (เริ่มลำดับที่ {worst[0]+1})')
            for st in range(0, len(seqv), WINDOW):
                blk = seqv[st:st + WINDOW]
                cb = collections.Counter(blk)
                kk, vv = cb.most_common(1)[0]
                flag = '🔴' if vv > WINDOW_MAX else '✅'
                print(f'     ก้อนย่อย {st//WINDOW+1} (q{chunk[st][0]}-q{chunk[min(st+WINDOW-1,len(chunk)-1)][0]}) :'
                      f' สูงสุด {vv}/{len(blk)} ที่ข้อ {kk}  {flag}')
            if over_w:
                rows.append([f'(หน้าต่าง) {a.setid}', a.setid, worst[2], '', '',
                             f'หน้าต่าง {WINDOW} ข้อ เกินเกณฑ์ {over_w}/{total_w} · แย่สุด {worst[1]}/{WINDOW}'])
            print(f'  🟠 แขน ข2 = **เตือนเท่านั้น** ⛔ ไม่ทำให้แดง'
                  f' (ก้อนสุ่มล้วนแดงเอง {p_index_ge(WINDOW, kmode, WINDOW_MAX+1)*kmode*100:.0f}%'
                  f' เมื่อมี {kmode} ตัวเลือก) — ครูเคาะ 4 ก.ย. 69''')
        # ── แขน ข2ข v2 · null สองแบบ (ใบ 136 §3) ────────────────────
        blocks = blocks_of([(x[1], x[3]) for x in chunk], WINDOW)
        rest = [x for x in seq if x[0] < (chunk[0][0])]
        if len(rest) >= MIN_REF:
            ref_src, ref_pool = f'ส่วนที่เหลือของชุด {len(rest)} ข้อ (⛔ ไม่ใช่ก้อนเอง)', rest
        else:
            ref_src, ref_pool = f'ทั้งชุด {len(seq)} ข้อ (⚠️ รวมก้อนเอง — ส่วนที่เหลือมีแค่ {len(rest)} ข้อ < {MIN_REF})', seq
        rc = collections.Counter(x[1] for x in ref_pool)
        rtot = sum(rc.values())
        ref_rate = {i: rc[i] / rtot for i in rc}
        idx_list = sorted({x[1] for x in chunk} | set(rc))
        print()
        print(f'แขน ข2ข · ก้อนย่อย {WINDOW} ข้อ ที่กระจุกที่ **index เดียวกัน** (แดงเมื่อ p < {P_RED})')
        print(f'  ตัวหาร {len(blocks)} บล็อกเต็ม · null-A = 1/k ต่อข้อ (Poisson-binomial ⇒ ⛔ ไม่ต้องเลือก k)')
        print(f'  null-B = อัตราจริงของแหล่งอ้างอิง: {ref_src}')
        res = arm_b2b_v2(blocks, ref_rate, idx_list)
        if not blocks:
            print(f'  ⬜ ก้อนสั้นกว่า {WINDOW} ข้อ ⇒ วัดไม่ได้ ⛔ ไม่ใช่ "ผ่าน"')
        elif res is None:
            print(f'  ✅ ⛔ ไม่มีบล็อกไหนกระจุกเกิน {WINDOW_MAX}')
        else:
            idx, x, m, p_uni, p_con = res
            rr = ref_rate.get(idx)
            print(f'  ข้อ {idx} กระจุกใน {x}/{m} บล็อก')
            print(f'     null-A (1/k)        ⇒ p = {fmt_p(p_uni)}  · Bonferroni x{len(idx_list)}')
            print(f'     null-B (อัตราจริง {rr*100:.1f}% ของ{ref_src.split(" ")[0]}) ⇒ p = {fmt_p(p_con)}'
                  f'  · Bonferroni x{len(idx_list)}')
            print(f'     ⇒ {tier(p_con)} — ตัดสินด้วย **null-B** (สามชั้น · มติครู 4 ก.ย. 69 · ใบ 138 §4)')
            if p_con is not None and P_RED <= p_con < P_AMBER:
                print('     📌 ชั้น 🟠 = **รอคนเซ็น** ⛔ ไม่ใช่ "ผ่าน" — ต้องมีคนรับก่อนของเข้าคลัง')
            if p_con is not None and p_con < P_RED:
                win_red = True
                rows.append([f'(ข2ข) {a.setid}', a.setid, idx, '', '',
                             f'กระจุกที่ข้อ {idx} ใน {x}/{m} บล็อก · p(null-B)={p_con:.2e} · null-B={rr:.3f}'])
            elif p_uni < P_RED:
                print(f'     📌 null-A แดงแต่ null-B ไม่แดง ⇒ **ความกระจุกอธิบายได้ด้วยความเอียงของชุด**'
                      f' ⇒ เรื่องนี้เป็นของ **แขน ข** ⛔ ไม่ใช่ของ ข2ข')
        # ── แขน ข3 · ช่วงติดกัน (null สองแบบเช่นกัน) ─────────────────
        vals = [x[1] for x in chunk]
        ks = [x[3] for x in chunk]
        L3, i3, st3 = longest_run(vals)
        nrun = len(vals) - L3 + 1 if L3 else 0
        pu3 = min(1.0, nrun * sum((1.0 / k) ** L3 for k in set(ks)) ) if L3 >= 2 else 1.0
        rr3 = ref_rate.get(i3, 0)
        pc3 = min(1.0, nrun * (rr3 ** L3) * len(idx_list)) if L3 >= 2 else 1.0
        mark3 = '🔴' if pc3 < P_RED else ('🟠' if L3 >= 5 else '✅')
        print(f'แขน ข3 · ช่วงเฉลยเดียวกันติดกันยาวสุด = {mark3} {L3} ข้อ ที่ข้อ {i3}'
              f' (เริ่มลำดับที่ {st3+1} จาก {len(vals)} ข้อ)')
        print(f'     null-A ⇒ p = {fmt_p(pu3)} · null-B (อัตราจริง {rr3*100:.1f}%) ⇒ p = {fmt_p(pc3)}')
        if pc3 < P_RED:
            win_red = True
            rows.append([f'(ข3) {a.setid}', a.setid, i3, '', '',
                         f'เฉลยข้อ {i3} ติดกัน {L3} ข้อ · p(null-B)={pc3:.2e}'])
    else:
        # ⛔ กวาดทั้งคลังเพื่อ "ดูขนาดของปัญหา" ก่อน ⛔ ไม่ตัดสิน (คำขอ E ใบ 132 §4)
        hits = []
        measurable = 0
        for s, lst in byset.items():
            seq = sorted((x for x in order[s] if x[0] is not None), key=lambda x: x[0])
            seqv = [x[1] for x in seq]
            total_w, over_w, worst = windows_over(seqv, WINDOW, WINDOW_MAX)
            if total_w == 0:
                continue
            measurable += 1
            if over_w:
                hits.append((over_w, total_w, worst[1], s))
        hits.sort(reverse=True)
        print(f'  ตัวหาร: {measurable} ชุดที่ยาวพอจะวัดหน้าต่างได้ (จาก {len(byset)} ชุด)')
        print(f'  ชุดที่มีหน้าต่างเกินเกณฑ์อย่างน้อย 1 บาน = {len(hits)}/{measurable} ชุด')
        for over_w, total_w, wv, s in hits[:10]:
            print(f'     {s}: เกิน {over_w}/{total_w} หน้าต่าง · แย่สุด {wv}/{WINDOW}')
        if len(hits) > 10:
            print(f'     … อีก {len(hits)-10} ชุด (อยู่ใน CSV)')
        for over_w, total_w, wv, s in hits:
            rows.append([f'(หน้าต่าง) {s}', s, '', '', '',
                         f'หน้าต่าง {WINDOW} ข้อ เกินเกณฑ์ {over_w}/{total_w} · แย่สุด {wv}/{WINDOW}'])
        print('  📌 แขน ข2 ⛔ ไม่ตัดสินอะไร — หน้าต่างซ้อนกัน ⇒ ชุดยาวเจอเกินอย่างน้อย 1 บานเกือบแน่นอน'
              ' โดยความบังเอิญ (E ใบ 132 §4 · MB ใบ 133 §4)')
        # ── ข2ข + ข3 ทั้งคลัง · null-B = **permutation** (ใบ 138 §1 ของ E) ──
        print()
        print(f'แขน ข2ข + ข3 · ทั้งคลัง — สามชั้น: 🔴 p<{P_RED} · 🟠 p<{P_AMBER} (รอคนเซ็น) · ✅ p>={P_AMBER}')
        print(f'  null-A = 1/k ต่อข้อ (Poisson-binomial) ⇒ ใช้ **คัดกรอง** เท่านั้น (เกณฑ์คัดกรอง p<{PERM_SCREEN})')
        print(f'  null-B = permutation เริ่ม {PERM_N:,} รอบ (ซ้ำ x10 ถึง {PERM_MAX:,} ถ้าตกใกล้เส้นแบ่ง) · seed {PERM_SEED}')
        print('  🔑 ที่นี่ ⛔ ไม่มี "ส่วนที่เหลือ" ให้อ้างอิง เพราะหน่วยที่ถูกตัดสิน = ทั้งชุด')
        red, amber, screened = [], [], 0
        for s_, lst in byset.items():
            seq = sorted((x for x in order[s_] if x[0] is not None), key=lambda x: x[0])
            vals = [x[1] for x in seq]
            ks = [x[3] for x in seq]
            if len(vals) < WINDOW:
                continue
            rc = collections.Counter(vals)
            idx_list = sorted(rc)
            blocks = blocks_of(list(zip(vals, ks)), WINDOW)
            res = arm_b2b_v2(blocks, {i: rc[i] / len(vals) for i in rc}, idx_list)
            L3, i3, st3 = longest_run(vals)
            pu3 = min(1.0, (len(vals) - L3 + 1) * sum((1.0 / k) ** L3 for k in set(ks))) if L3 >= 2 else 1.0
            need_b = res is not None and res[3] < PERM_SCREEN
            need_r = pu3 < PERM_SCREEN
            if not (need_b or need_r):
                continue
            screened += 1
            pb, pr, kb, kr, nused = perm_refine(vals, res[0] if need_b else None,
                                                res[1] if need_b else None, L3 if need_r else 0)
            if nused > PERM_N:
                print('     🔁 ค่าตกใกล้เส้นแบ่ง ⇒ รันซ้ำ %s รอบ (จาก %s)'
                      % (format(nused, ','), format(PERM_N, ',')))
            if need_b:
                t = tier(pb)
                line = (f'{s_}: ข้อ {res[0]} กระจุกใน {res[1]}/{res[2]} บล็อก'
                        f' · null-A p={fmt_p(res[3])} · **null-B(perm) p={fmt_perm_full(pb, kb, nused)}** ⇒ {t}')
                (red if pb < P_RED else amber if pb < P_AMBER else []).append(('ข2ข', s_, line))
                print(f'     {t} · {line}')
                rows.append([f'(ข2ข) {s_}', s_, res[0], '', '',
                             f'{res[1]}/{res[2]} บล็อก · p={pb:.2e} · เจอ {kb}/{nused} · {t}'])
            if need_r:
                t = tier(pr)
                line = (f'{s_}: เฉลยข้อ {i3} ติดกัน {L3} ข้อ (จาก {len(vals)} ข้อปรนัย)'
                        f' · null-A p={fmt_p(pu3)} · **null-B(perm) p={fmt_perm_full(pr, kr, nused)}** ⇒ {t}')
                (red if pr < P_RED else amber if pr < P_AMBER else []).append(('ข3', s_, line))
                print(f'     {t} · {line}')
                rows.append([f'(ข3) {s_}', s_, i3, '', '',
                             f'ติดกัน {L3} ข้อ · p={pr:.2e} · เจอ {kr}/{nused} · {t}'])
        print(f'  ⑨ ตัวหาร: ชุดที่ผ่านการคัดกรองไปทำ permutation = {screened} ชุด'
              f' · 🔴 แดง {len(red)} · 🟠 รอคนเซ็น {len(amber)}')
        if amber:
            print('  📌 ชั้น 🟠 ⛔ ไม่ใช่ "ผ่าน" — ต้องมีคนเซ็นรับก่อน · ถ้าชั้นนี้บวมจนไม่มีใครเซ็นไหว'
                  ' แปลว่าเกณฑ์ผิด ⛔ ไม่ใช่คนขี้เกียจ (E ใบ 138 §4)')
        if red:
            win_red = True

    with open(a.out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(['id/ชุด', 'ชุด', 'ตำแหน่งเฉลย', 'ยาว(เฉลย)', 'ยาวเฉลี่ย(ตัวลวง)', 'ข้อสังเกต'])
        w.writerows(rows)
    print()
    print(f'✅ {a.out} · ข้อที่เฉลยยาวจนเดาได้ {longest:,} ข้อ · ชุดที่เฉลยกระจุก (แขน ก) {len(bad)} ชุด')
    red = bool(bad) or chunk_red or win_red
    if red and a.enforce:
        print('⇒ 🔴 --enforce ⇒ รหัสออก 1')
        return 1
    if red:
        print('⇒ 🟠 โหมดเตือน (ค่าปริยาย) ⇒ รหัสออก 0 · เปิดแดงด้วย --enforce เมื่อครูเคาะ')
    return 0


if __name__ == '__main__':
    sys.exit(main())

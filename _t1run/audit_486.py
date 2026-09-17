# -*- coding: utf-8 -*-
"""
audit_486.py -- ตรวจซ้ำระเบียนที่ merge_master บอกว่า "ไม่ตรงเฉลย"
ด้วย normalizer ตัวเต็ม (ชุดเดียวกับที่ run.py gate ใช้ตอนผลิต)

อ่านอย่างเดียว ⛔ ไม่เขียนทับไฟล์ใด ๆ  (เขียนแค่รายงานผลตามที่สั่งด้วย --out)

ผลลัพธ์แบ่ง 3 กลุ่ม
  A) ด่านอ่อน   - merge_master ไม่ match แต่ normalizer เต็มเจอ  => เฉลยถูก
  B) ต้องดูตา   - ทั้งสองด่านไม่ match => อาจเฉลยผิดจริง หรือรูปแบบแปลก
  C) ไม่มีคีย์   - บทที่ correct เป็น None/ว่าง => เทียบไม่ได้ตั้งแต่ต้น
"""
import argparse, json, os, re, sys, unicodedata

# ---------------- raw_text: เดินเก็บสตริงเอง ⛔ ห้าม json.dumps ----------------
def raw_text(x, out=None):
    if out is None: out = []
    if isinstance(x, str): out.append(x)
    elif isinstance(x, dict):
        for v in x.values(): raw_text(v, out)
    elif isinstance(x, (list, tuple)):
        for v in x: raw_text(v, out)
    elif x is not None: out.append(str(x))
    return out

def S(x): return " ".join(raw_text(x))

# ---------------- normalize ----------------
SUP = {'\u00b2':'^2','\u00b3':'^3','\u00b9':'^1','\u2070':'^0','\u2074':'^4','\u2075':'^5',
       '\u2076':'^6','\u2077':'^7','\u2078':'^8','\u2079':'^9','\u207b':'^-'}
SUB = {'\u2080':'_0','\u2081':'_1','\u2082':'_2','\u2083':'_3','\u2084':'_4','\u2085':'_5',
       '\u2086':'_6','\u2087':'_7','\u2088':'_8','\u2089':'_9'}
UNI2TOK = {'\u00b1':'pm','\u221a':'sqrt','\u221e':'infty','\u2264':'le','\u2265':'ge',
           '\u2260':'ne','\u222a':'cup','\u2229':'cap','\u2205':'varnothing','\u2208':'in'}
LAT2TOK = {r'\pm':'pm', r'\sqrt':'sqrt', r'\infty':'infty', r'\le':'le', r'\leq':'le',
           r'\ge':'ge', r'\geq':'ge', r'\ne':'ne', r'\neq':'ne', r'\cup':'cup',
           r'\cap':'cap', r'\varnothing':'varnothing', r'\emptyset':'varnothing', r'\in':'in',
           # 🔴 ขาดไปตอนแรก เจอจากการสุ่มตรวจจริง: \lt \gt ทำให้ "-5\lt c\lt5" ไม่ match "-5 < c < 5"
           r'\lt':'<', r'\gt':'>', r'\cdot':'*', r'\times':'*', r'\div':'/', r'\%':'%'}
DECOR = ['\u0304','\u0305','\u20d7']
KILL = [r'\left', r'\right', r'\,', r'\!', r'\;', r'\:', r'\displaystyle',
        r'\overline', r'\bar', r'\vec', r'\mathbf', r'\boldsymbol', r'\text', r'\mathrm']

def _bracify(s):
    # \frac25 -> \frac{2}{5} ; \frac2{5} ; \frac{2}5
    s = re.sub(r'\\frac\s*(\d)\s*(\d)', r'\\frac{\1}{\2}', s)
    s = re.sub(r'\\frac\s*(\d)\s*\{', r'\\frac{\1}{', s)
    s = re.sub(r'\\frac\s*\{([^{}]*)\}\s*(\d)', r'\\frac{\1}{\2}', s)
    return s

def _frac_to_div(s):
    """\frac{A}{B} -> (A)/(B) แบบนับวงเล็บให้สมดุล ทำซ้ำจนไม่เหลือ"""
    for _ in range(12):
        i = s.find(r'\frac{')
        if i < 0: break
        j = i + 6; depth = 1
        while j < len(s) and depth:
            if s[j] == '{': depth += 1
            elif s[j] == '}': depth -= 1
            j += 1
        if depth: break
        A = s[i+6:j-1]
        if j >= len(s) or s[j] != '{': break
        k = j + 1; depth = 1
        while k < len(s) and depth:
            if s[k] == '{': depth += 1
            elif s[k] == '}': depth -= 1
            k += 1
        if depth: break
        B = s[j+1:k-1]
        s = s[:i] + '(' + A + ')/(' + B + ')' + s[k:]
    return s

def normalize(s):
    if not isinstance(s, str): s = str(s)
    for a, b in SUP.items(): s = s.replace(a, b)
    for a, b in SUB.items(): s = s.replace(a, b)
    s = unicodedata.normalize('NFKC', s)
    # แยกตัวประกอบออกก่อน แล้วค่อยทิ้งมาครอน/ลูกศรเวกเตอร์ (ū ที่ NFKC ประกอบแล้วก็โดน)
    s = unicodedata.normalize('NFD', s)
    for d in DECOR: s = s.replace(d, '')
    s = unicodedata.normalize('NFC', s)
    # 🔴 คั่นหลักพันแบบ LaTeX: 27{,}846 / 27{\,}846 / 27\,846  -> 27846
    #    ต้องทำก่อนตัดปีกกา ไม่งั้นเหลือ "27,846" แล้วกฎตัดคอมมาจับไม่ได้ (เจอจากการสุ่มตรวจจริง)
    s = re.sub(r'(?<=\d)\{\s*\\?[,.]?\s*\}(?=\d)', '', s)
    s = re.sub(r'(?<=\d)\\[,;:!](?=\d)', '', s)
    # 🔴 ต้องทิ้งคำสั่งจัดรูปก่อน map \le/\ge  ไม่งั้น \le ไปกิน \left จนเหลือ "left"
    for k in KILL: s = s.replace(k, '')
    s = s.replace(r'\dfrac', r'\frac').replace(r'\tfrac', r'\frac')
    s = _bracify(s)
    s = _frac_to_div(s)
    s = re.sub(r'\\sqrt\s*\{([^{}]*)\}', r'sqrt\1', s)
    s = re.sub(r'\bsqrt\s*\(([^()]*)\)', r'sqrt\1', s)
    # เรียงจากยาวไปสั้น + ต้องไม่มีตัวอักษรตามหลัง กัน \le กิน \leftarrow ฯลฯ
    for a in sorted(LAT2TOK, key=len, reverse=True):
        s = re.sub(re.escape(a) + r'(?![A-Za-z])', LAT2TOK[a], s)
    for a, b in UNI2TOK.items(): s = s.replace(a, b)
    s = s.replace('\u2212', '-').replace('\u2013', '-').replace('\u2014', '-')
    s = s.replace('\u00d7', '*').replace('\u00f7', '/').replace('\u22c5', '*')
    s = s.replace(r'\imath', 'i').replace(r'\jmath', 'j')
    s = re.sub(r'\\lvert|\\rvert|\\vert|\\mid', '|', s)
    # 🔴 ต้องตัดช่องว่างก่อนกฎคอมมา ไม่งั้น "{0, 2, 7, 8}" -> "0,2,7,8"
    #    แต่ "{0,2,7,8}" -> "0278"  => คีย์กับเฉลยกลายเป็นคนละอย่างทั้งที่เหมือนกัน (เจอจากการสุ่มตรวจจริง)
    s = re.sub(r'\s', '', s)
    s = re.sub(r'(?<=\d),(?=\d)', '', s)      # 16,232 -> 16232
    s = re.sub(r'[\$\{\}\(\)\[\]]', '', s)
    s = s.replace('\\', '')                    # ทิ้งแบ็กสแลชที่เหลือเป็นขั้นสุดท้าย
    return s.lower()

# ---------------- ตัวเทียบ ----------------
def contains(hay, needle):
    """มี digit-boundary guard กันเลขสั้น match มั่วในเลขยาว"""
    if not needle: return False
    if needle[0].isdigit() or needle[-1].isdigit():
        pat = re.escape(needle)
        if needle[0].isdigit():  pat = r'(?<![0-9.])' + pat
        if needle[-1].isdigit(): pat = pat + r'(?![0-9.])'
        return re.search(pat, hay) is not None
    return needle in hay

def frac_alts(raw):
    """สร้างรูปเทียบเท่าของคำตอบ: เศษส่วน / ทศนิยม / ตัดเครื่องหมาย ±"""
    outs = set()
    r = str(raw).strip()
    outs.add(r)
    outs.add(r.lstrip('+-').lstrip('\u00b1'))
    m = re.fullmatch(r'\s*(-?\d+)\s*/\s*(\d+)\s*', r)
    if m:
        n, d = int(m.group(1)), int(m.group(2))
        outs.add(f'{n}/{d}'); outs.add(rf'\frac{{{n}}}{{{d}}}'); outs.add(rf'\dfrac{{{n}}}{{{d}}}')
        if d: outs.add(f'{n/d:.6f}'.rstrip('0').rstrip('.'))
        if n < 0: outs.add(f'-{abs(n)}/{d}')
    try:
        f = float(r)
        if f == int(f): outs.add(str(int(f)))
        outs.add(f'{f:.6f}'.rstrip('0').rstrip('.'))
    except Exception:
        pass
    return {x for x in outs if str(x).strip()}

SPLIT = re.compile(r'[;:,]|หรือ|และ|\bor\b|\band\b')
def segments(raw):
    return [p.strip() for p in SPLIT.split(str(raw)) if p and p.strip()]

def join_norm(*objs):
    """🔴 normalize ทีละชิ้นแล้วค่อยต่อด้วย '|'
    ถ้า normalize ก้อนรวมทีเดียว ช่องว่างระหว่างช่องจะหายไป ทำให้เลขท้ายช่องหนึ่ง
    ไปติดกับเลขต้นอีกช่อง แล้ว digit-guard เข้าใจผิดว่าเป็นเลขยาวตัวเดียว
    (เจอจากการสุ่มตรวจจริง: $\\dfrac{3}{2}$ ไม่ match ทั้งที่เฉลยเขียนไว้ชัด ๆ)"""
    parts = []
    for o in objs: parts.extend(raw_text(o))
    return '|' + '|'.join(normalize(p) for p in parts if p is not None) + '|'

def build_hay(rec):
    steps = rec.get('steps') or []
    tail = steps[-2:] if isinstance(steps, list) else []
    return join_norm(tail, rec.get('verify'))

def hay_weak(rec):
    """เลียนแบบ hit() ของ merge_master: eq ขั้นท้าย + verify.result เท่านั้น"""
    steps = rec.get('steps') or []
    eq = ''
    if isinstance(steps, list) and steps and isinstance(steps[-1], dict):
        eq = S(steps[-1].get('eq') or '')
    v = rec.get('verify')
    res = S(v.get('result') or '') if isinstance(v, dict) else ''
    return normalize(eq) + normalize(res)

def check_full(rec, q):
    """คืน (ผ่านไหม, ทางที่ผ่าน)"""
    hay = build_hay(rec)
    if not hay: return False, 'ไม่มีเนื้อให้เทียบ'
    correct = q.get('correct'); choices = q.get('choices')
    # ---------- ข้อ fill ----------
    if not choices:
        if correct is None or str(correct).strip() == '': return None, 'ไม่มีคีย์'
        for alt in frac_alts(correct):
            if contains(hay, normalize(alt)): return True, 'fill: ค่าคำตอบปรากฏ'
        segs = segments(correct)
        if len(segs) > 1:
            okc = sum(1 for s in segs if any(contains(hay, normalize(a)) for a in frac_alts(s)))
            if okc == len(segs): return True, 'fill: ครบทุกเซกเมนต์'
            if okc / len(segs) >= 0.8: return True, f'fill: เจอ {okc}/{len(segs)} เซกเมนต์ (>=80%)'
        th = re.findall(r'[\u0e00-\u0e7f]{6,}', str(correct))
        if th and all(normalize(t) in hay for t in th): return True, 'fill: วลีไทยครบ'
        return False, 'fill: ไม่เจอค่าคำตอบ'
    # ---------- ข้อเลือกตอบ ----------
    try: ci = int(correct)
    except Exception: return None, 'ไม่มีคีย์'
    if not (0 <= ci < len(choices)): return None, 'คีย์ชี้นอกช่วงตัวเลือก'
    ctext = choices[ci]
    if contains(hay, normalize(ctext)): return True, 'mc: ข้อความตัวเลือกทั้งก้อน'
    segs = re.findall(r'\$([^$]+)\$', str(ctext))
    if segs and all(contains(hay, normalize(s)) for s in segs): return True, 'mc: ชิ้น $...$ ครบ'
    for pat in (rf'ตอบข้อ{ci+1}', rf'ข้อที่{ci+1}', rf'ตัวเลือกที่{ci+1}', rf'ตัวเลือก{ci+1}',
                rf'index={ci}', rf'index:{ci}'):
        if normalize(pat) in hay: return True, f'mc: ชี้หมายเลขตัวเลือก {ci+1}'
    toks = [t for t in re.split(r'[^0-9a-z\u0e00-\u0e7f]+', normalize(ctext)) if len(t) >= 2]
    if toks:
        r = sum(1 for t in toks if t in hay) / len(toks)
        if r >= 0.8: return True, f'mc: โทเคนตรง {r:.0%}'
    # ตัวเลือกที่ต่างกันแค่ "ป้าย" ท้าย -> ตัด prefix/suffix ร่วมแล้วเทียบเศษ
    if len(choices) > 1:
        others = [normalize(c) for k, c in enumerate(choices) if k != ci]
        me = normalize(ctext)
        pre = os.path.commonprefix([me] + others)
        suf = os.path.commonprefix([me[::-1]] + [o[::-1] for o in others])[::-1]
        core = me[len(pre):len(me)-len(suf)] if len(pre)+len(suf) < len(me) else ''
        if len(core) >= 2 and contains(hay, core): return True, 'mc: เศษที่ต่างจากตัวเลือกอื่น'
    return False, 'mc: ไม่เจอคำตอบ'

# ---------------- main ----------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--master', default=os.path.join('_t1run', 'results', 't1_MASTER.json'))
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--out', default=os.path.join('_t1run', 'audit_486_report.json'))
    ap.add_argument('--show', type=int, default=25)
    a = ap.parse_args()

    bank = json.load(open(a.bank, encoding='utf-8'))
    qs = bank['questions'] if isinstance(bank, dict) and 'questions' in bank else bank
    Q = {q['id']: q for q in qs}
    d = json.load(open(a.master, encoding='utf-8'))
    recs = d if isinstance(d, list) else (d.get('items') or d.get('records') or list(d.values()))
    recs = [r for r in recs if isinstance(r, dict) and 'id' in r]
    print(f"MASTER {len(recs)} ระเบียน | คลัง {len(Q)} ข้อ")

    weak_fail, nokey = [], []
    for r in recs:
        q = Q.get(r['id'])
        if not q: continue
        k = q.get('correct')
        if k is None or str(k).strip() == '':
            nokey.append(r['id']); continue
        kk = normalize(str(k)); blob = hay_weak(r)
        if not (kk and (kk in blob or (blob and blob in kk))):
            weak_fail.append(r['id'])

    print(f"\nด่านอ่อน (แบบ merge_master) ไม่ match : {len(weak_fail)} ข้อ")
    print(f"ไม่มีคีย์คำตอบในคลัง                    : {len(nokey)} ข้อ")

    byid = {r['id']: r for r in recs}
    A, B, C = [], [], []
    for i in weak_fail:
        ok, why = check_full(byid[i], Q[i])
        (A if ok else (C if ok is None else B)).append((i, why))

    print("\n" + "=" * 62)
    print(f"A) ด่านอ่อนล้วน ๆ (normalizer เต็มเจอคำตอบ) : {len(A)} ข้อ")
    print(f"B) ต้องดูด้วยตา (ทั้งสองด่านไม่เจอ)          : {len(B)} ข้อ")
    print(f"C) เทียบไม่ได้ (คีย์มีปัญหา)                  : {len(C)} ข้อ")
    print("=" * 62)

    from collections import Counter
    if A:
        print("\nทางที่ normalizer เต็มใช้กู้ได้:")
        for w, n in Counter(w for _, w in A).most_common(): print(f"   {n:5d}  {w}")
    if B:
        print(f"\n🔎 กลุ่ม B — {min(a.show,len(B))} ตัวอย่างแรก:")
        for i, w in B[:a.show]:
            q = Q[i]
            print(f"   {i:34s} type={q.get('type'):5s} correct={repr(q.get('correct'))[:34]}")
        print("\nกลุ่ม B แยกตามบท:")
        for p, n in Counter(re.sub(r'-(q|rv)\d+$', '', i) for i, _ in B).most_common(12):
            print(f"   {n:5d}  {p}")

    json.dump({'weak_fail': len(weak_fail),
               'A_gate_weak': [i for i, _ in A],
               'B_need_eyes': [{'id': i, 'why': w, 'type': Q[i].get('type'),
                                'correct': Q[i].get('correct')} for i, w in B],
               'C_no_key': [i for i, _ in C]},
              open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"\nรายงานเต็ม: {a.out}")

if __name__ == '__main__':
    main()

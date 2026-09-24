#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""merge_master.py — รวมไฟล์ผลทุกไฟล์เป็น MASTER เดียว ตัดข้อซ้ำ เลือกฉบับที่ดีที่สุด
ใช้: python merge_master.py [--done _t1run\\results] [--bank data\\bank.json] [--out _t1run\\results\\t1_MASTER.json]
     [--choices _t1run\\choice_*.json] [--dry-run]
เกณฑ์เลือกฉบับ: (1) คำตอบตรงเฉลย (2) ขั้นตอน+กับดักมากกว่า (3) ยาวกว่า

🔴 ชั้นคำเคาะครู (เพิ่ม 24 ส.ค. 2569 — หลังเหตุการณ์ที่คำเคาะ 25 ข้อถูกกลืนเงียบ)
   เกณฑ์อัตโนมัติข้างบนใช้ "ขั้นเยอะ = ดีกว่า" — แต่ตอนครูเลือกจริง 95 ข้อ ครูเลือก
   ฉบับที่ **สั้นลง 13 · เท่าเดิม 9 · ยาวขึ้น 3** (สั้น : ยาว ≈ 4 : 1)
   ⇒ เกณฑ์เครื่องสวนทางกับคำเคาะครู ⇒ ทุกครั้งที่ merge วิ่ง คำเคาะจะถูกลบทิ้ง
   ⇒ ⇒ คำเคาะครูจึงต้องเป็น **ชั้นทับสุดท้าย** และเวลาทับต้อง **พิมพ์บอก ⛔ ห้ามเงียบ**

🖼 ชั้นหมุดรูป (overlay) — v2 · 24 ก.ย. 2569 · มติครู ⑪ ก (ใบ 405 · 408) · MB ใบ 411
   เดิม: ถ้าใส่ [IMAGE:n] ลง t1_MASTER.json ตรง ๆ ⇒ merge รอบหน้าสร้าง MASTER ใหม่จากไฟล์ผลดิบ ⇒ หมุดหายเงียบ
   ⇒ หมุดเก็บแยกที่ _t1run/imagepins/*.json แล้ว merge ใส่ทับ **หลังชั้นคำเคาะครู** ทุกรอบ
   รูปแบบ (ไฟล์ละหลายข้อ · id ห้ามซ้ำข้ามไฟล์ · คีย์ขึ้นต้นด้วย _ = หมายเหตุ ไม่อ่าน):
     {"<id>": {"v": "<ลายนิ้วมือ 8 ตัวของฉบับ t1 ที่เลือก ก่อนใส่หมุด>",
               "pins": [{"step": 2, "img": 0, "at": "end"}]}          ← ขั้นที่ 2 (นับจาก 1) · รูป imageSpec ตัวที่ 0 · ท้ายขั้น (หรือ "start")
      "<id>": {"v": "...", "none": "เหตุผลที่เฉลยข้อนี้ไม่ต้องมีรูป"}}
   ใส่ยังไง: เติม "[IMAGE:n]" เป็นแถวใหม่ใน steps[k].work + ติดป้าย record["imgpins"] = {v, src, pins|none}
   ⛔ ห้ามทับเงียบ: ฉบับ t1 เปลี่ยน (v ไม่ตรง) · ขั้น/รูปที่ชี้ไม่มีจริง · id ไม่มีใน MASTER · ซ้ำกับหมุดที่มีในไฟล์ผลดิบ
      ⇒ ⛔ ไม่ใส่ข้อนั้น + พิมพ์รายชื่อ + รหัสออก 1
   กันหมุดไหลกลับ (⑦): ฉบับในไฟล์อินพุตที่มีป้าย "imgpins" (เช่น snapshot t1_MASTER_*.json ที่เซฟหลังใส่หมุด) ⇒ ⛔ ไม่นับเป็นฉบับ
   หลังเขียน MASTER ⇒ สร้าง _t1run/t1_index.json ใหม่ทันที (build_t1_index · มติ ⑮) ⇒ วิวเวอร์ไม่ค้าง
   รหัสออก: 0 = ผ่าน · 1 = มีหมุดที่ทำตามไม่ได้ · 2 = อ่านไฟล์หมุด/สร้าง index ไม่ได้
"""
import json, os, re, glob, argparse, hashlib, copy, sys

def S(v): return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
def load_bank(p):
    d = json.load(open(p, encoding='utf-8'))
    return d if isinstance(d, list) else next(v for v in d.values() if isinstance(v, list) and v and isinstance(v[0], dict))
def norm(x):
    t = re.sub(r'\\left|\\right|\\text|\\mathrm', '', S(x)).replace('dfrac', 'frac').replace('tfrac', 'frac')
    return re.sub(r'[\s$\\{}()\[\],"\']', '', t)

# 🔑 ลายนิ้วมือของ "ฉบับ" — ต้องตรงกับที่เครื่องมือเลือกรุ่นใช้ (เลือกรุ่นt1.html)
#    ⛔ ห้ามเปลี่ยนสูตรนี้ ถ้าเปลี่ยน คำเคาะเก่าทั้งหมดจะหาที่ลงไม่เจอ
def vhash(r):
    return hashlib.md5(json.dumps(r, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()[:8]

def load_choices(patterns):
    """อ่านไฟล์คำเคาะครูทุกไฟล์ที่เข้าเงื่อนไข → {id: hash} · ไฟล์ใหม่กว่าทับไฟล์เก่ากว่า"""
    files = []
    for p in patterns:
        files += [p] if os.path.isfile(p) else glob.glob(p)
    files = sorted(set(files), key=lambda f: os.path.getmtime(f))
    out, src = {}, {}
    for f in files:
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception as e:
            print(f'   ⚠️ อ่านไฟล์คำเคาะไม่ได้: {f} — {e}'); continue
        if not isinstance(d, dict):
            print(f'   ⚠️ ไฟล์คำเคาะรูปแบบไม่ถูก (ต้องเป็น {{id: hash}}): {f}'); continue
        for k, v in d.items():
            if isinstance(v, str): out[k] = v; src[k] = os.path.basename(f)
    return out, src, files

# ---------- 🖼 ชั้นหมุดรูป (⑪) ----------
PIN_RE = re.compile(r'\[IMAGE:(\d+)\]')

def load_pins(pdir):
    """อ่าน <pdir>/*.json → ({id: entry}, {id: ไฟล์}, [ไฟล์], [ข้อผิดพลาด]) · id ซ้ำข้ามไฟล์ = ข้อผิดพลาด ⛔ ไม่ทับกันเงียบ"""
    files = sorted(glob.glob(os.path.join(pdir, '*.json'))) if pdir and os.path.isdir(pdir) else []
    out, src, errs = {}, {}, []
    for f in files:
        b = os.path.basename(f)
        try:
            with open(f, encoding='utf-8') as fh: d = json.load(fh)
        except Exception as e:
            errs.append(f'อ่าน {b} ไม่ได้ — {e}'); continue
        if not isinstance(d, dict):
            errs.append(f'{b} ต้องเป็น {{id: entry}}'); continue
        for k, v in d.items():
            if k.startswith('_'): continue
            if k in out:
                errs.append(f'id ซ้ำข้ามไฟล์: {k} ({src[k]} · {b})'); continue
            out[k] = v; src[k] = b
    return out, src, files, errs

def _entry_errs(e, r, nimg_i):
    """ตรวจ entry หนึ่งข้อกับ record ที่เลือก · คืนรายการปัญหา (ว่าง = ใส่ได้)"""
    if not isinstance(e, dict): return ['entry ต้องเป็น object']
    has_p, has_n = 'pins' in e, 'none' in e
    if has_p == has_n: return ['ต้องมี "pins" หรือ "none" อย่างใดอย่างหนึ่ง']
    if has_n:
        return [] if isinstance(e['none'], str) and e['none'].strip() else ['"none" ต้องเป็นเหตุผลที่ไม่ว่าง']
    ps = e['pins']
    if not isinstance(ps, list) or not ps: return ['"pins" ต้องเป็น list ที่ไม่ว่าง']
    steps = r.get('steps') if isinstance(r.get('steps'), list) else []
    out, seen = [], set()
    for p in ps:
        if not isinstance(p, dict): out.append('หมุดต้องเป็น object'); continue
        k, n, at = p.get('step'), p.get('img'), p.get('at', 'end')
        if not isinstance(k, int) or isinstance(k, bool) or not 1 <= k <= len(steps) or not isinstance(steps[k - 1], dict):
            out.append(f'ขั้น {k} ไม่มีจริง (ฉบับนี้มี {len(steps)} ขั้น)')
        if not isinstance(n, int) or isinstance(n, bool) or n < 0 or (nimg_i is not None and n >= nimg_i):
            out.append(f'รูป {n} ไม่มีจริง (imageSpec ของข้อนี้มี {nimg_i if nimg_i is not None else "?"} รูป)')
        if at not in ('end', 'start'): out.append(f'"at" = {at!r} (ใช้ได้แค่ end / start)')
        if n in seen: out.append(f'รูป {n} ถูกปักซ้ำในข้อเดียวกัน')
        seen.add(n)
        if isinstance(n, int) and f'[IMAGE:{n}]' in S(r): out.append(f'[IMAGE:{n}] มีอยู่แล้วในเฉลย t1 (จากไฟล์ผลดิบ) ⇒ ซ้ำ')
    return out

def apply_pins(chosen, pins, psrc, nimg):
    """ใส่หมุดทับลงฉบับที่เลือก (ทำสำเนาก่อน ⛔ ไม่แตะของในไฟล์ผลดิบ) · คืนรายงาน"""
    rep = {'pins': [], 'none': [], 'stale': [], 'noid': [], 'bad': []}
    for i in sorted(pins):
        e = pins[i]
        if i not in chosen: rep['noid'].append(i); continue
        r = chosen[i]
        want, got = (e.get('v') if isinstance(e, dict) else None), vhash(r)
        if want != got: rep['stale'].append((i, want, got)); continue
        if nimg is not None and i not in nimg and isinstance(e, dict) and 'pins' in e:
            rep['bad'].append((i, ['ข้อนี้ไม่มี imageSpec ในคลัง ⇒ ห้ามมีหมุด'])); continue
        errs = _entry_errs(e, r, None if nimg is None else nimg.get(i))
        if errs: rep['bad'].append((i, errs)); continue
        r = copy.deepcopy(r)
        meta = {'v': got, 'src': psrc.get(i, '')}
        if 'none' in e:
            meta['none'] = e['none']; rep['none'].append(i)
        else:
            for p in e['pins']:
                s = r['steps'][p['step'] - 1]
                w = s.get('work')
                w = [] if w is None else (list(w) if isinstance(w, list) else [w])
                tag = f"[IMAGE:{p['img']}]"
                s['work'] = [tag] + w if p.get('at') == 'start' else w + [tag]
            meta['pins'] = [{'step': p['step'], 'img': p['img'], 'at': p.get('at', 'end')} for p in e['pins']]
            rep['pins'].append(i)
        r['imgpins'] = meta
        chosen[i] = r
    return rep

def write_index(best, out):
    """สร้าง t1_index.json จาก MASTER ที่เพิ่งเขียน (มติ ⑮) · ใช้โค้ดเดียวกับ tools/build_t1_index.py"""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import build_t1_index as bti
    body = bti.dump(bti.build(best))
    tmp = out + '.tmp'
    with open(tmp, 'wb') as f: f.write(body)
    os.replace(tmp, out)
    return len(body), hashlib.md5(body).hexdigest()[:8]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--done', nargs='*', default=[os.path.join('_t1run', 'results')])
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--out', default=os.path.join('_t1run', 'results', 't1_MASTER.json'))
    ap.add_argument('--choices', nargs='*', default=[os.path.join('_t1run', 'choice_*.json')],
                    help='ไฟล์คำเคาะครู {id: hash} · ใส่ค่าว่างเพื่อปิดชั้นนี้')
    ap.add_argument('--dry-run', action='store_true', help='คำนวณและรายงาน แต่ ⛔ ไม่เขียนไฟล์')
    ap.add_argument('--sets-manifest', default=os.path.join('data', 'manifest.json'),
                    help='ต้นทางธง flawedSource (อ่านจาก data/sets ตาม manifest ⛔ ไม่ใช่ bank.json ที่บอทสร้าง) · ใส่ค่าว่างเพื่อปิดตัวกรอง')
    ap.add_argument('--pins', default=os.path.join('_t1run', 'imagepins'),
                    help='โฟลเดอร์ไฟล์หมุดรูป (⑪) · ใส่ค่าว่างเพื่อปิดชั้นนี้')
    ap.add_argument('--index', default=os.path.join('_t1run', 't1_index.json'),
                    help='สร้าง index ของวิวเวอร์ต่อท้าย (⑮) · ใส่ค่าว่างเพื่อไม่สร้าง')
    a = ap.parse_args()
    key = {}
    if os.path.exists(a.bank):
        for q in load_bank(a.bank):
            c = q.get('correct')
            key[q['id']] = q['choices'][c] if isinstance(c, int) and q.get('choices') else S(c)

    # ---------- 🔴 ตัวกรอง "ข้อสอบออกผิด" (มติครูอ๊อฟ 17–18 ก.ย. 2569 · ใบ 375/376/377/379) ----------
    #   ข้อที่มีธง flawedSource **และ** ไม่มีคีย์ (correct is None) = โจทย์ผิด ⇒ ⛔ ไม่เข้า MASTER
    #   อ่านธงจาก data/sets ตาม manifest (ต้นทางจริง) ⛔ ไม่อ่านจาก bank.json — bank.json เป็นของที่บอทสร้าง
    #   ถ้าครูยังไม่ Pull หลังบอท rebuild ธงใหม่จะยังไม่อยู่ใน bank ⇒ ตัวกรองจะผ่านเงียบ (ใบ 376 §1 · E แก้ใน 377 §③)
    #   ทรงเดียวกับ _t1run/drop_flawed_from_master.py (G2) ⇒ ตัวกรอง 2 ตัวตอบตรงกันเสมอ
    #   ⛔ ไม่ฝังเลขคาดหวัง (เช่น "ต้องได้ 10") — เลขนั้นเปลี่ยนทุกครั้งที่ครูเคาะข้อใหม่ · พิมพ์จำนวน+รายชื่อให้คนเทียบแทน
    flawed_nokey, flawed_keyed, sets_seen = {}, [], 0
    nimg = {}   # 🖼 id → จำนวนรูปใน imageSpec (ใช้ตรวจหมุด ⑪)
    if a.sets_manifest and os.path.exists(a.sets_manifest):
        sets_d = os.path.join(os.path.dirname(a.sets_manifest), 'sets')
        try:
            man = json.load(open(a.sets_manifest, encoding='utf-8'))
            for sid in man.get('sets', []):
                p = os.path.join(sets_d, sid + '.json')
                if not os.path.exists(p): continue
                sets_seen += 1
                for q in json.load(open(p, encoding='utf-8')).get('questions', []):
                    sp_ = q.get('imageSpec')
                    if sp_: nimg[q['id']] = len(sp_) if isinstance(sp_, list) else 1
                    fs_ = q.get('flawedSource')
                    if not fs_: continue
                    if q.get('correct') is None: flawed_nokey[q['id']] = fs_.get('kind') if isinstance(fs_, dict) else str(fs_)
                    else: flawed_keyed.append(q['id'])
        except Exception as e:
            print(f'   ⚠️ อ่าน manifest/sets ไม่ได้: {e} — ตัวกรองข้อสอบออกผิด ⛔ ไม่ทำงานรอบนี้')
    files = []
    for p in a.done:
        files += [p] if os.path.isfile(p) else glob.glob(os.path.join(p, '**', '*.json'), recursive=True)
    files = [f for f in files if os.path.abspath(f) != os.path.abspath(a.out)]
    vers, nfile, nrec = {}, 0, 0
    fedback = 0   # 🖼 ⑦ ฉบับที่มีป้าย imgpins ติดมา (ไหลกลับจาก snapshot) ⇒ ไม่นับ
    for f in sorted(files):
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        if not (isinstance(d, list) and d and isinstance(d[0], dict) and 'steps' in d[0]): continue
        nfile += 1
        for r in d:
            if isinstance(r, dict) and 'imgpins' in r: fedback += 1; continue
            nrec += 1; vers.setdefault(r['id'], []).append(r)
    def hit(r):
        k = norm(key.get(r['id'], ''))
        blob = norm(S(r['steps'][-1].get('eq') or '')) + norm(S(r.get('verify', {}).get('result') or ''))
        return bool(k) and (k in blob or (blob and blob in k))
    def score(r): return (1 if hit(r) else 0, len(r.get('steps', [])) + len(r.get('traps', [])), len(S(r)))
    chosen = {i: max(v, key=score) for i, v in vers.items()}

    # ---------- ตัดข้อสอบออกผิดออกก่อนชั้นคำเคาะ (คำเคาะที่ชี้ id ที่ถูกตัด จะไปโผล่ในถัง noid ⇒ ไม่เงียบ) ----------
    dropped = sorted(i for i in chosen if i in flawed_nokey)
    for i in dropped:
        del chosen[i]; vers.pop(i, None)

    # ---------- 🔴 ชั้นคำเคาะครู — ทับหลังสุด และรายงานทุกครั้ง ----------
    ch, csrc, cfiles = load_choices([p for p in a.choices if p])
    applied, same, notfound, noid = [], [], [], []
    for i, h in ch.items():
        if i not in vers: noid.append(i); continue
        m = [r for r in vers[i] if vhash(r) == h]
        if not m: notfound.append(i); continue
        if vhash(chosen[i]) == h: same.append(i)
        else: chosen[i] = m[0]; applied.append(i)

    # ---------- 🖼 ชั้นหมุดรูป (⑪) — ทับหลังชั้นคำเคาะครู · รายงานทุกครั้ง ----------
    raw_pinned = {i for i, r in chosen.items() if PIN_RE.search(S(r))}
    if a.pins:
        pins, psrc, pfiles, perrs = load_pins(a.pins)
    else:
        pins, psrc, pfiles, perrs = {}, {}, [], []
    prep = apply_pins(chosen, pins, psrc, nimg if sets_seen else None)

    best = list(chosen.values())
    dup = nrec - len(best)
    if not a.dry_run:
        os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
        # newline='\n' (มติครูอ๊อฟ 18 ก.ย. 2569 ข้อ ③): เดิมเปิด 'w' ไม่ระบุ ⇒ Windows เขียน CRLF ⇒ md5 บนดิสก์ ≠ blob ใน git (.gitattributes eol=lf)
        #   ⚠️ รอบ merge แรกหลังแพตช์นี้ md5 ของ MASTER เปลี่ยนทั้งไฟล์แม้เนื้อเท่าเดิม (ใบ 377 §③ · 378 §1)
        json.dump(best, open(a.out, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
    print(('🧪 ทดลอง (⛔ ไม่เขียนไฟล์) ' if a.dry_run else '✅ ') + a.out)
    print(f'   อ่าน {nfile} ไฟล์ · {nrec:,} ฉบับ ⇒ id ไม่ซ้ำ {len(best):,} ข้อ · ตัดฉบับซ้ำทิ้ง {dup:,}')
    if key: print(f'   ฉบับที่เลือกแล้วตรงเฉลย {sum(1 for r in best if hit(r)):,} / {len(best):,}')

    # ---------- รายงานตัวกรองข้อสอบออกผิด ⛔ ห้ามเงียบ ----------
    print('   ── ตัวกรองข้อสอบออกผิด (ธง flawedSource + ไม่มีคีย์ · อ่านจาก data/sets) ──')
    if not a.sets_manifest:
        print('   ⚠️ ⛔ ปิดตัวกรอง (--sets-manifest ว่าง) — MASTER นี้อาจมีข้อโจทย์ผิดปน')
    elif not sets_seen:
        print(f'   ⚠️ ⛔ ไม่ได้อ่านชุดใดเลย ({a.sets_manifest}) — ตัวกรองไม่ทำงาน · ตรวจพาธ/manifest ก่อนเชื่อ MASTER นี้')
    else:
        print(f'   อ่าน {sets_seen} ชุด · ธง+ไม่มีคีย์ในคลัง {len(flawed_nokey)} ข้อ ⇒ ตัดออกจาก MASTER รอบนี้ {len(dropped)} ข้อ'
              f' · ธง+มีคีย์ (คงไว้) {len(flawed_keyed)} ข้อ')
        for i in dropped: print(f'      ✂️ {i}  ({flawed_nokey[i]})')
        if not flawed_nokey:
            print('   ⚠️ คลังไม่มีข้อ "ธง+ไม่มีคีย์" เลย — ผิดจากที่ครูเคาะไว้ (17 ก.ย. 69 มี 10 ข้อ) ⇒ ตรวจว่า data/sets ครบไหม')

    # ---------- รายงานชั้นคำเคาะ ⛔ ห้ามเงียบไม่ว่ากรณีใด ----------
    print('   ── ชั้นคำเคาะครู ──')
    if not cfiles:
        print('   ⚠️ ⛔ ไม่พบไฟล์คำเคาะเลย — MASTER นี้ใช้เกณฑ์เครื่องล้วน')
        print('      (เกณฑ์เครื่อง = "ขั้นเยอะกว่าชนะ" ซึ่งสวนทางกับที่ครูเลือกจริง 4 ต่อ 1)')
    else:
        print(f'   อ่านคำเคาะ {len(cfiles)} ไฟล์: ' + ' · '.join(os.path.basename(f) for f in cfiles))
        print(f'   คำเคาะทั้งหมด {len(ch)} ข้อ ⇒ ทับจริง {len(applied)} · ตรงกับเครื่องอยู่แล้ว {len(same)}')
        if applied:
            print('   🔧 ข้อที่คำเคาะครูทับเกณฑ์เครื่อง:')
            for i in sorted(applied):
                print(f'      {i} → {ch[i]}  (จาก {csrc[i]})')
        if notfound:
            print(f'   🔴 {len(notfound)} ข้อ — คำเคาะชี้ไปที่ฉบับที่ **หาไม่เจอในไฟล์ผล** ⇒ ใช้ของเครื่องแทน:')
            for i in sorted(notfound): print(f'      {i} → {ch[i]}')
            print('      ⇒ แปลว่าไฟล์ผลต้นทางหายไป หรือสูตรลายนิ้วมือเปลี่ยน — ตรวจก่อนเชื่อ MASTER นี้')
        if noid:
            print(f'   ⚠️ {len(noid)} ข้อ — คำเคาะมี id ที่ ⛔ ไม่มีในไฟล์ผลเลย: {sorted(noid)[:10]}')
    if not a.dry_run and (notfound or noid):
        print('   🔴 เขียนไฟล์แล้ว แต่ **มีคำเคาะที่ทำตามไม่ได้** — อย่าเพิ่งถือว่า MASTER นี้ตรงใจครู')

    # ---------- 🖼 รายงานชั้นหมุดรูป ⛔ ห้ามเงียบ ----------
    rc = 0
    print('   ── ชั้นหมุดรูป (⑪ · overlay) ──')
    if fedback:
        print(f'   🛡 ตัดฉบับที่มีป้าย imgpins ติดมาจากไฟล์อินพุต {fedback:,} ฉบับ (กันหมุดไหลกลับทาง snapshot · ⑦)')
    if not a.pins:
        print('   ⚠️ ⛔ ปิดชั้นหมุด (--pins ว่าง) — หมุดที่ปักไว้จะไม่อยู่ใน MASTER นี้')
    else:
        print(f'   อ่านไฟล์หมุด {len(pfiles)} ไฟล์ ({a.pins}) · {len(pins):,} ข้อ'
              + ((': ' + ' · '.join(os.path.basename(f) for f in pfiles)) if pfiles else ''))
        print(f'   ⇒ ใส่หมุด {len(prep["pins"]):,} ข้อ · ระบุไม่ต้องมีรูป {len(prep["none"]):,} ข้อ'
              f' · ฉบับเปลี่ยน {len(prep["stale"])} · ชี้ผิด {len(prep["bad"])} · ไม่มีใน MASTER {len(prep["noid"])}')
        for e in perrs: print(f'   🔴 {e}')
        for i, want, got in prep['stale']:
            print(f'   🔴 ฉบับเปลี่ยน {i}: หมุดผูกกับ {want} แต่ merge เลือก {got} ⇒ ⛔ ไม่ใส่ · ต้องตรวจตำแหน่งใหม่')
        for i, errs in prep['bad']:
            print(f'   🔴 ชี้ผิด {i}: ' + ' · '.join(errs))
        for i in prep['noid']:
            print(f'   🔴 ไม่มีใน MASTER: {i} (ถูกตัดเป็นข้อสอบออกผิด หรือ id พิมพ์ผิด)')
        if perrs or prep['stale'] or prep['bad'] or prep['noid']:
            rc = 1
    if sets_seen:
        scope = {i for i in chosen if i in nimg}
        done = raw_pinned | set(prep['pins']) | set(prep['none'])
        extra = sorted(i for i in (raw_pinned | set(prep['pins'])) if i not in nimg)
        print(f'   ขอบเขต (ข้อใน MASTER ที่คลังมี imageSpec) {len(scope):,} ข้อ ⇒ หมุดจากไฟล์ผลดิบ {len(raw_pinned & scope):,}'
              f' · หมุด overlay {len(set(prep["pins"]) & scope):,} · ระบุไม่ต้องมีรูป {len(set(prep["none"]) & scope):,}'
              f' · ⬜ ยังไม่ตัดสิน {len(scope - done):,}')
        if extra:
            print(f'   🔴 มีหมุดในข้อที่คลังไม่มี imageSpec {len(extra)} ข้อ: {extra[:10]}'); rc = 1
    else:
        print('   ⚠️ ไม่ได้อ่าน data/sets ⇒ ตรวจเลขรูปและขอบเขตไม่ได้')

    # ---------- index ของวิวเวอร์ (⑮) ----------
    if not a.dry_run and a.index:
        try:
            n, h = write_index(best, a.index)
            print(f'   🗂 สร้าง {a.index} ใหม่ · {n:,} B · md5 {h} · {len(best):,} ข้อ (วิวเวอร์เห็น MASTER ฉบับนี้)')
        except Exception as e:
            print(f'   🔴 สร้าง {a.index} ไม่ได้ — {e} ⇒ วิวเวอร์จะแสดงของเก่า · รัน python tools/build_t1_index.py เอง')
            rc = 2
    elif not a.dry_run:
        print('   ⚠️ ไม่ได้สร้าง index (--index ว่าง) ⇒ วิวเวอร์อาจค้าง · รัน python tools/build_t1_index.py')
    if rc == 1:
        print('   🔴 มีหมุดที่ทำตามไม่ได้ (รายการข้างบน) ⇒ รหัสออก 1')
    return rc

if __name__ == '__main__': sys.exit(main())

# -*- coding: utf-8 -*-
"""
apply_nokey_keys.py -- ใส่คีย์คำตอบให้ข้อที่ `correct` เป็น null ในคลัง

ที่มาของคีย์
    ตัวแก้อิสระ 5 ตัว (blind solver) แก้โจทย์เองโดย ⛔ ไม่เห็นเฉลย t1
    แล้วนำผลมาเทียบกับข้อสรุปของเฉลย t1 ที่เขียนไว้ก่อนหน้า
    ใส่เฉพาะข้อที่ "สองทางอิสระตรงกัน" เท่านั้น

ค่าปริยาย = DRY RUN (ไม่เขียนอะไรเลย)  ต้องใส่ --apply ถึงจะเขียนจริง

ด่านกันพลาด
    - สำรอง data/bank.json เป็น .bak-keys-<YYYYmmdd-HHMM> ก่อนเสมอ
    - เขียนไฟล์ชั่วคราวแล้วตรวจก่อนทับ:
        * จำนวนข้อในคลังต้องเท่าเดิม
        * ข้อที่ไม่อยู่ในรายการต้องไม่เปลี่ยนแม้แต่ตัวอักษรเดียว
        * ข้อที่แก้ ต้องเปลี่ยนเฉพาะช่อง `correct` เท่านั้น
        * ⛔ ห้ามทับข้อที่ `correct` เดิม "ไม่ว่าง" (กันเขียนทับคีย์ที่มีอยู่แล้ว)
        * ข้อ mc: ดัชนีต้องอยู่ในช่วง 0..len(choices)-1
      ไม่ผ่านข้อใดข้อหนึ่ง ⇒ ยกเลิก ไม่ทับ

วิธีใช้
    python _t1run\\apply_nokey_keys.py                 <- ดูก่อน
    python _t1run\\apply_nokey_keys.py --apply         <- เขียนจริง
"""
import argparse, datetime, json, os, shutil, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bank', default=os.path.join('data', 'bank.json'))
    ap.add_argument('--keys', default=os.path.join('_t1run', 'PROPOSED_KEYS.json'))
    ap.add_argument('--apply', action='store_true')
    a = ap.parse_args()

    for p in (a.bank, a.keys):
        if not os.path.isfile(p):
            print(f"ไม่พบไฟล์: {p}"); sys.exit(1)

    keys = json.load(open(a.keys, encoding='utf-8'))
    raw = open(a.bank, encoding='utf-8').read()
    bank = json.loads(raw)
    wrapped = isinstance(bank, dict) and 'questions' in bank
    qs = bank['questions'] if wrapped else bank
    byid = {q['id']: q for q in qs}

    print(f"คลัง: {os.path.abspath(a.bank)}  ({len(qs)} ข้อ)")
    print(f"คีย์ที่เสนอ: {len(keys)} ข้อ")
    print(f"โหมด: {'APPLY (เขียนจริง)' if a.apply else 'DRY RUN (ไม่เขียน)'}")
    print("-" * 70)

    plan, skip = [], []
    for k in keys:
        i = k['id']; q = byid.get(i)
        if q is None:
            skip.append((i, 'ไม่พบ id นี้ในคลัง')); continue
        cur = q.get('correct')
        if cur is not None and str(cur).strip() != '':
            skip.append((i, f'มีคีย์อยู่แล้ว ({cur!r}) ⛔ ไม่ทับ')); continue
        val = k['proposed_correct']
        if q.get('choices'):
            try: val = int(val)
            except Exception:
                skip.append((i, f'เป็นข้อเลือกตอบแต่คีย์ไม่ใช่ตัวเลข: {val!r}')); continue
            if not (0 <= val < len(q['choices'])):
                skip.append((i, f'ดัชนี {val} อยู่นอกช่วง 0..{len(q["choices"])-1}')); continue
        else:
            val = str(val)
        plan.append((i, cur, val, k.get('confidence', '?')))

    for i, cur, val, conf in plan:
        note = '  ⚠️ confidence=medium' if conf == 'medium' else ''
        print(f"  {i:32s} null -> {str(val):12s}{note}")
    if skip:
        print("\n  ข้ามไม่แก้:")
        for i, why in skip: print(f"    {i:32s} {why}")

    print("-" * 70)
    print(f"จะแก้ {len(plan)} ข้อ · ข้าม {len(skip)} ข้อ")
    if not a.apply:
        print("DRY RUN -- ยังไม่เขียน  ใส่ --apply เพื่อแก้จริง")
        return
    if not plan:
        print("ไม่มีอะไรต้องแก้"); return

    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M')
    bak = f"{a.bank}.bak-keys-{stamp}"
    shutil.copy2(a.bank, bak)

    before = {q['id']: json.dumps(q, ensure_ascii=False, sort_keys=True) for q in qs}
    changed = {i for i, _, _, _ in plan}
    for i, _, val, _ in plan:
        byid[i]['correct'] = val

    tmp = a.bank + '.tmp-keys'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(bank, f, ensure_ascii=False, indent=1)

    # ---------- ด่านตรวจซ้ำก่อนทับของจริง ----------
    chk = json.loads(open(tmp, encoding='utf-8').read())
    cqs = chk['questions'] if (isinstance(chk, dict) and 'questions' in chk) else chk
    errs = []
    if len(cqs) != len(qs): errs.append(f"จำนวนข้อเปลี่ยน {len(qs)} -> {len(cqs)}")
    cby = {q['id']: q for q in cqs}
    for i, s in before.items():
        n = cby.get(i)
        if n is None: errs.append(f"{i}: หายไปจากคลัง"); continue
        if i in changed:
            old = json.loads(s); new = dict(n)
            if old.get('correct') not in (None, ''): errs.append(f"{i}: ของเดิมไม่ได้ว่าง")
            o2 = {k: v for k, v in old.items() if k != 'correct'}
            n2 = {k: v for k, v in new.items() if k != 'correct'}
            if o2 != n2: errs.append(f"{i}: มีช่องอื่นนอกจาก correct เปลี่ยนไปด้วย")
        else:
            if json.dumps(n, ensure_ascii=False, sort_keys=True) != s:
                errs.append(f"{i}: ข้อที่ไม่ควรถูกแตะ กลับเปลี่ยนไป")
    if errs:
        os.remove(tmp)
        print("\n[ไม่ผ่านด่านตรวจ] ยกเลิก ไม่เขียนทับคลัง")
        for e in errs[:10]: print("    !", e)
        print(f"    (สำรองไว้ที่ {os.path.basename(bak)} -- ลบทิ้งได้)")
        sys.exit(2)

    os.replace(tmp, a.bank)
    print(f"\n[เขียนแล้ว] แก้ {len(plan)} ข้อ  (สำรอง: {os.path.basename(bak)})")
    left = sum(1 for q in cqs if q.get('correct') is None or str(q.get('correct')).strip() == '')
    print(f"ตรวจซ้ำ: ข้อที่ยังไม่มีคีย์ในคลัง เหลือ {left} ข้อ")

if __name__ == '__main__':
    main()

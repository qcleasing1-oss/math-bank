# -*- coding: utf-8 -*-
"""
fix_verify_shape.py  --  ซ่อมระเบียนผลลัพธ์ t1 ที่ช่อง verify เป็น "สตริง" แทนที่จะเป็น dict

อาการที่ซ่อม
    merge_master.py ล้มด้วย AttributeError: 'str' object has no attribute 'get'
    ที่บรรทัด  r.get('verify', {}).get('result')
    เพราะบางระเบียน worker เขียน verify เป็นข้อความยาว ๆ แทนที่จะเป็น {how, lines, result}

วิธีซ่อม (ไม่ทำข้อมูลหาย)
    verify: "<ข้อความ>"  ->  {"how": "<ข้อความ>", "lines": [], "result": "<ข้อความ>"}
    เก็บข้อความเดิมไว้ทั้งใน how และ result
    ใส่ไว้ใน result ด้วยเพราะ merge_master ใช้ result ไปเทียบกับคีย์คำตอบ
    ถ้าตัดทิ้ง ระเบียนนั้นจะถูกให้คะแนนต่ำกว่าความจริง

ค่าปริยาย = DRY RUN (ไม่เขียนอะไรเลย)  ต้องใส่ --apply ถึงจะเขียนจริง
เขียนจริงจะสำรองไฟล์เดิมเป็น <ชื่อไฟล์>.bak-verifyfix-<YYYYmmdd-HHMM> ก่อนเสมอ
หลังเขียนมีด่านตรวจซ้ำ: จำนวนระเบียนต้องเท่าเดิม / ระเบียนอื่นต้องไม่เปลี่ยนแม้แต่ตัวเดียว / ต้องไม่เหลือ verify ที่เป็นสตริง

วิธีใช้
    python _t1run\\fix_verify_shape.py                 <- ดูก่อนว่าจะแก้อะไรบ้าง
    python _t1run\\fix_verify_shape.py --apply         <- แก้จริง
"""
import argparse, datetime, glob, json, os, shutil, sys

def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def is_result_list(d):
    return isinstance(d, list) and d and isinstance(d[0], dict) and 'steps' in d[0]

def fix_record(rec):
    """คืน (ระเบียนใหม่, แก้ไหม)"""
    v = rec.get('verify')
    if v is None or isinstance(v, dict):
        return rec, False
    if not isinstance(v, str):
        return rec, False
    new = dict(rec)
    new['verify'] = {"how": v, "lines": [], "result": v}
    return new, True

def scan(folder):
    hits = []
    for path in sorted(glob.glob(os.path.join(folder, 't1_*.json'))):
        base = os.path.basename(path)
        if base.startswith('t1_MASTER_'):
            continue
        try:
            d = load(path)
        except Exception as e:
            print(f"  [ข้าม] {base} -- อ่าน JSON ไม่ได้: {e}")
            continue
        if not is_result_list(d):
            continue
        bad = [r.get('id') for r in d
               if isinstance(r, dict) and isinstance(r.get('verify'), str)]
        if bad:
            hits.append((path, base, d, bad))
    return hits

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', default=os.path.join('_t1run', 'results'),
                    help='โฟลเดอร์ไฟล์ผล (ปริยาย _t1run/results)')
    ap.add_argument('--apply', action='store_true', help='เขียนจริง (ไม่ใส่ = ดูอย่างเดียว)')
    a = ap.parse_args()

    folder = a.dir
    if not os.path.isdir(folder):
        print(f"ไม่พบโฟลเดอร์: {folder}")
        sys.exit(1)

    print(f"โฟลเดอร์ที่ตรวจ: {os.path.abspath(folder)}")
    print(f"โหมด: {'APPLY (เขียนจริง)' if a.apply else 'DRY RUN (ไม่เขียน)'}")
    print("-" * 66)

    hits = scan(folder)
    total = sum(len(b) for _, _, _, b in hits)
    if not hits:
        print("ไม่พบระเบียนที่ verify เป็นสตริง -- ไม่มีอะไรต้องแก้")
        return

    print(f"พบ {total} ระเบียน ใน {len(hits)} ไฟล์:")
    for _, base, _, bad in hits:
        print(f"  {base}  ({len(bad)} ระเบียน)")
        for i in bad:
            print(f"      - {i}")
    print("-" * 66)

    if not a.apply:
        print("DRY RUN -- ยังไม่เขียนอะไร  ใส่ --apply เพื่อแก้จริง")
        return

    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M')
    for path, base, d, bad in hits:
        bak = f"{path}.bak-verifyfix-{stamp}"
        shutil.copy2(path, bak)

        out, nfix = [], 0
        for r in d:
            nr, changed = fix_record(r) if isinstance(r, dict) else (r, False)
            nfix += 1 if changed else 0
            out.append(nr)

        tmp = path + '.tmp-verifyfix'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=1)

        # ---------- ด่านตรวจซ้ำก่อนทับของจริง ----------
        chk = load(tmp)
        errs = []
        if len(chk) != len(d):
            errs.append(f"จำนวนระเบียนเปลี่ยน {len(d)} -> {len(chk)}")
        if any(isinstance(r.get('verify'), str) for r in chk if isinstance(r, dict)):
            errs.append("ยังเหลือ verify ที่เป็นสตริง")
        if nfix != len(bad):
            errs.append(f"แก้ได้ {nfix} ระเบียน แต่ควรเป็น {len(bad)}")
        badset = set(bad)
        for old, new in zip(d, chk):
            if not isinstance(old, dict):
                continue
            if old.get('id') in badset:
                v = new.get('verify')
                if not (isinstance(v, dict) and v.get('result') == old.get('verify')
                        and v.get('how') == old.get('verify')):
                    errs.append(f"{old.get('id')}: ซ่อมแล้วเนื้อไม่ตรงต้นฉบับ")
            else:
                if old != new:
                    errs.append(f"{old.get('id')}: ระเบียนที่ไม่ควรถูกแตะ กลับเปลี่ยนไป")

        if errs:
            os.remove(tmp)
            print(f"[ไม่ผ่านด่านตรวจ] {base} -- ยกเลิก ไม่เขียนทับ")
            for e in errs[:10]:
                print("    !", e)
            print(f"    (สำรองไว้แล้วที่ {os.path.basename(bak)} -- ลบทิ้งได้)")
            continue

        os.replace(tmp, path)
        print(f"[แก้แล้ว] {base}  {nfix} ระเบียน  (สำรอง: {os.path.basename(bak)})")

    print("-" * 66)
    left = sum(len(b) for _, _, _, b in scan(folder))
    print(f"ตรวจซ้ำทั้งโฟลเดอร์: เหลือระเบียนที่ verify เป็นสตริง = {left}")
    print("เสร็จแล้วรัน:  python tools\\merge_master.py")

if __name__ == '__main__':
    main()

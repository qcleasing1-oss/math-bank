# -*- coding: utf-8 -*-
"""
แก้คลัง bank.json ตามที่ครูเคาะ 10 ก.ย. 2569 — 3 ข้อ
วิธีรัน (ในโฟลเดอร์ math-bank):   python "แก้คลัง-3ข้อ-ครูเคาะ10กย-v1.0-ครูรันเอง.py"
⛔ สำรองไฟล์ให้อัตโนมัติก่อนแก้เสมอ · ⛔ ถ้าค่าปัจจุบันไม่ตรงที่คาด จะไม่แก้ข้อนั้นและรายงานออกมา
⛔ สคริปต์นี้ ⛔ ไม่แตะ git — ครูเป็นคนคอมมิตเอง
"""
import json, shutil, os, sys, io

BANK = os.path.join("data", "bank.json")
BACKUP = os.path.join("data", "bank.json.bak-2026-09-10-ก่อนแก้3ข้อ")

if not os.path.exists(BANK):
    sys.exit("⛔ ไม่พบ %s — ต้องรันในโฟลเดอร์ math-bank" % BANK)

shutil.copy2(BANK, BACKUP)
print("⬤ สำรองแล้ว:", BACKUP, "(%d ไบต์)" % os.path.getsize(BACKUP))

with io.open(BANK, encoding="utf-8") as f:
    bank = json.load(f)
qs = {q["id"]: q for q in bank["questions"]}
changed, skipped = [], []

# ── ① chap-02-logic-q37 : ครูเคาะทาง ก — เหตุขัดแย้งกันเอง = สมเหตุสมผล ⇒ คำตอบคือตัวเลือกแรก
q = qs.get("chap-02-logic-q37")
if q is None:
    skipped.append("chap-02-logic-q37 · ⛔ ไม่พบ id นี้ในคลัง")
elif q.get("correct") != 2:
    skipped.append("chap-02-logic-q37 · ค่าปัจจุบัน correct=%r ⛔ ไม่ใช่ 2 ตามที่คาด ⇒ ไม่แก้" % q.get("correct"))
else:
    q["correct"] = 0
    q["notes"] = (q.get("notes", "") + " | มติครู 10 ก.ย. 69: เหตุขัดแย้งกันเอง ⇒ การอ้างเหตุผลสมเหตุสมผล (vacuously valid) ⇒ ก. และ ข. สมเหตุสมผล").strip(" |")
    changed.append("chap-02-logic-q37 · correct 2 → 0 (ก. และ ข. สมเหตุสมผล)")

# ── ② chap-10-complex-q81 : ตัวโจทย์ตกขีดบน (สังยุค) ที่ตัวส่วน ⇒ เติมกลับ · correct=7 เดิมถูกแล้ว
q = qs.get("chap-10-complex-q81")
if q is None:
    skipped.append("chap-10-complex-q81 · ⛔ ไม่พบ id นี้ในคลัง")
else:
    old = q.get("question", "")
    OLD_SUB, NEW_SUB = "(3 + 4i)}{1 + i}", "(3 + 4i)}{\\overline{1 + i}}"
    if "\\overline{1 + i}" in old:
        skipped.append("chap-10-complex-q81 · มีขีดบนอยู่แล้ว ⇒ ไม่แก้ซ้ำ")
    elif old.count(OLD_SUB) != 1:
        skipped.append("chap-10-complex-q81 · หาข้อความ %r ไม่เจอ/เจอมากกว่า 1 ครั้ง (เจอ %d) ⇒ ไม่แก้ · ข้อความจริงคือ: %s"
                       % (OLD_SUB, old.count(OLD_SUB), old))
    elif q.get("correct") != 7:
        skipped.append("chap-10-complex-q81 · correct=%r ⛔ ไม่ใช่ 7 ตามที่คาด ⇒ ไม่แก้" % q.get("correct"))
    else:
        q["question"] = old.replace(OLD_SUB, NEW_SUB)
        q["notes"] = (q.get("notes", "") + " | 10 ก.ย. 69: เติมขีดบน (สังยุค) ที่ตัวส่วนตามต้นฉบับโควตา มช. 2541 ⇒ z = -1+7i ⇒ ส่วนจินตภาพ 7 ตรงกับ correct เดิม").strip(" |")
        changed.append("chap-10-complex-q81 · เติม \\overline ที่ตัวส่วน (correct=7 คงเดิม)")

# ── ③ pat1-2555-10-q15 : ข้อมูลในโจทย์ขัดแย้งกันเอง (ละเมิดโคชี–ชวาร์ซ) ⇒ ขึ้นทะเบียนว่าต้นฉบับผิด
q = qs.get("pat1-2555-10-q15")
if q is None:
    skipped.append("pat1-2555-10-q15 · ⛔ ไม่พบ id นี้ในคลัง")
elif q.get("flawedSource") is True:
    skipped.append("pat1-2555-10-q15 · ขึ้นทะเบียน flawedSource ไว้แล้ว ⇒ ไม่แก้ซ้ำ")
else:
    q["flawedSource"] = True
    q["notes"] = (q.get("notes", "") + " | มติครู 10 ก.ย. 69: ข้อสอบต้นฉบับออกผิด — จากเงื่อนไขได้ |u|=4, |v|=√2, u·v=-6 "
                  "แต่โคชี–ชวาร์ซบังคับ |u·v| ≤ 4√2 ≈ 5.657 ⇒ cos(u,v) = -1.06 นอกช่วง [-1,1] ⇒ เวกเตอร์ชุดนี้ไม่มีจริง "
                  "⇒ ตัดออกจากคิว t1 ⛔ ไม่ทำเฉลย").strip(" |")
    changed.append("pat1-2555-10-q15 · ตั้ง flawedSource = true (ตัดออกจากคิว t1 อัตโนมัติ)")

if not changed:
    print("\n⛔ ไม่ได้แก้อะไรเลย — ลบไฟล์สำรองทิ้งได้")
else:
    with io.open(BANK, "w", encoding="utf-8") as f:
        json.dump(bank, f, ensure_ascii=False, indent=1)
    print("\n⬤ เขียน %s แล้ว (%d ไบต์)" % (BANK, os.path.getsize(BANK)))

print("\n=== แก้แล้ว %d ข้อ ===" % len(changed))
for c in changed: print("  ✅", c)
print("=== ไม่ได้แก้ %d ข้อ ===" % len(skipped))
for s in skipped: print("  ⚠️", s)

# ── ตรวจซ้ำโดยอ่านไฟล์ที่เขียนไปแล้วกลับขึ้นมาใหม่
if changed:
    with io.open(BANK, encoding="utf-8") as f:
        again = {q["id"]: q for q in json.load(f)["questions"]}
    print("\n=== ยืนยันจากไฟล์ที่เขียนแล้ว ===")
    for i in ("chap-02-logic-q37", "chap-10-complex-q81", "pat1-2555-10-q15"):
        r = again.get(i, {})
        print("  %-26s correct=%-5r flawedSource=%r" % (i, r.get("correct"), r.get("flawedSource", False)))
    print("  chap-10-complex-q81 มีขีดบนแล้ว:", "\\overline{1 + i}" in again.get("chap-10-complex-q81", {}).get("question", ""))
    print("\n📌 ขั้นถัดไปของครู: ตรวจ 3 บรรทัดข้างบนให้ตรง แล้วค่อย git commit — ⛔ สคริปต์นี้ไม่แตะ git")

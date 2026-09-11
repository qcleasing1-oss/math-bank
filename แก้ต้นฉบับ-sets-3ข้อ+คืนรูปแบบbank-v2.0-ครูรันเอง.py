# -*- coding: utf-8 -*-
"""
v2.0 — แก้ที่ต้นฉบับ data/sets/*.json (ของจริง) + คืนรูปแบบเดิมให้ data/bank.json
วิธีรัน (ในโฟลเดอร์ math-bank):  python "แก้ต้นฉบับ-sets-3ข้อ+คืนรูปแบบbank-v2.0-ครูรันเอง.py"

ทำ 4 อย่าง:
 ① หาว่า 3 id อยู่ในไฟล์ sets ไหน  ② สำรอง + แก้ที่ sets  ③ เขียน bank.json ใหม่ด้วย "รูปแบบเดิม"
 ④ ตรวจซ้ำจากไฟล์ที่เขียนแล้ว + บอกขนาดเทียบกับไฟล์สำรอง
⛔ ไม่แตะ git · ⛔ ถ้าค่าปัจจุบันไม่ตรงที่คาด จะข้ามข้อนั้นแล้วรายงาน
"""
import json, shutil, os, sys, io, glob, re

BANK   = os.path.join("data", "bank.json")
BACKUP = os.path.join("data", "bank.json.bak-2026-09-10-ก่อนแก้3ข้อ")
SETS   = os.path.join("data", "sets")

if not os.path.isdir(SETS):
    sys.exit("⛔ ไม่พบโฟลเดอร์ %s — ต้องรันในโฟลเดอร์ math-bank" % SETS)

TARGETS = ["chap-02-logic-q37", "chap-10-complex-q81", "pat1-2555-10-q15"]

# ── ตรวจรูปแบบการเว้นวรรคของไฟล์สำรอง (ของเดิมก่อนผมแก้)
def detect_indent(path):
    with io.open(path, encoding="utf-8") as f:
        head = f.read(4000)
    m = re.search(r"\{\r?\n(\s*)\"", head)
    if not m:
        return None, head[:80]
    pad = m.group(1)
    if "\t" in pad:
        return "\t", head[:80]
    return len(pad), head[:80]

orig_indent = None
if os.path.exists(BACKUP):
    orig_indent, sample = detect_indent(BACKUP)
    cur_indent, _ = detect_indent(BANK)
    print("⬤ รูปแบบเดิม (จากไฟล์สำรอง) indent = %r · ตอนนี้ = %r" % (orig_indent, cur_indent))
else:
    print("⚠️ ไม่พบไฟล์สำรอง %s ⇒ จะไม่ยุ่งกับรูปแบบของ bank.json" % BACKUP)

# ── ① หา id ใน sets
found = {}
setfiles = sorted(glob.glob(os.path.join(SETS, "*.json")))
print("\n=== ① ค้น 3 id ใน %d ไฟล์ของ data/sets ===" % len(setfiles))
for p in setfiles:
    try:
        with io.open(p, encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print("  ⚠️ อ่านไม่ได้:", p, e); continue
    items = data.get("questions", data) if isinstance(data, dict) else data
    if not isinstance(items, list):
        continue
    for q in items:
        if isinstance(q, dict) and q.get("id") in TARGETS:
            found.setdefault(q["id"], []).append(p)
for t in TARGETS:
    print("  %-26s → %s" % (t, found.get(t) or "⛔ ไม่พบในไฟล์ sets ไหนเลย"))

# ── ② แก้ที่ sets
changed, skipped = [], []

def patch_q(q, which):
    if which == "chap-02-logic-q37":
        if q.get("correct") == 0:
            return None, "correct=0 อยู่แล้ว ⇒ ไม่แก้ซ้ำ"
        if q.get("correct") != 2:
            return None, "correct=%r ⛔ ไม่ใช่ 2 ตามที่คาด ⇒ ไม่แก้" % q.get("correct")
        q["correct"] = 0
        q["notes"] = (q.get("notes","") + " | มติครู 10 ก.ย. 69: เหตุขัดแย้งกันเอง ⇒ สมเหตุสมผล (vacuously valid) ⇒ ก. และ ข. สมเหตุสมผล").strip(" |")
        return "correct 2 → 0", None
    if which == "chap-10-complex-q81":
        old = q.get("question","")
        if "\\overline{1 + i}" in old:
            return None, "มีขีดบนอยู่แล้ว ⇒ ไม่แก้ซ้ำ"
        OLD, NEW = "(3 + 4i)}{1 + i}", "(3 + 4i)}{\\overline{1 + i}}"
        if old.count(OLD) != 1:
            return None, "หา %r ไม่เจอ/ไม่ยูนีก (เจอ %d) · ข้อความจริง: %s" % (OLD, old.count(OLD), old[:160])
        if q.get("correct") != 7:
            return None, "correct=%r ⛔ ไม่ใช่ 7 ⇒ ไม่แก้" % q.get("correct")
        q["question"] = old.replace(OLD, NEW)
        q["notes"] = (q.get("notes","") + " | 10 ก.ย. 69: เติมขีดบน (สังยุค) ที่ตัวส่วนตามต้นฉบับโควตา มช. 2541 ⇒ z=-1+7i ⇒ ส่วนจินตภาพ 7 ตรงกับ correct เดิม").strip(" |")
        return "เติม \\overline ที่ตัวส่วน", None
    if which == "pat1-2555-10-q15":
        if q.get("flawedSource") is True:
            return None, "flawedSource=true อยู่แล้ว ⇒ ไม่แก้ซ้ำ"
        q["flawedSource"] = True
        q["notes"] = (q.get("notes","") + " | มติครู 10 ก.ย. 69: ต้นฉบับออกผิด — |u|=4, |v|=√2, u·v=-6 แต่โคชี–ชวาร์ซบังคับ |u·v| ≤ 4√2 ≈ 5.657 ⇒ cos = -1.06 นอกช่วง [-1,1] ⇒ เวกเตอร์ชุดนี้ไม่มีจริง ⇒ ตัดออกจากคิว t1").strip(" |")
        return "ตั้ง flawedSource = true", None
    return None, "⛔ ไม่รู้จัก id นี้"

print("\n=== ② แก้ที่ไฟล์ sets ===")
for t in TARGETS:
    for p in found.get(t, []):
        with io.open(p, encoding="utf-8") as f:
            raw = f.read()
        data = json.loads(raw)
        items = data.get("questions", data) if isinstance(data, dict) else data
        target = next(q for q in items if q.get("id") == t)
        ind, _ = detect_indent(p)
        ok, why = patch_q(target, t)
        if ok is None:
            skipped.append("%s (%s) · %s" % (t, os.path.basename(p), why)); continue
        bak = p + ".bak-2026-09-10"
        if not os.path.exists(bak):
            shutil.copy2(p, bak)
        with io.open(p, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=(ind if isinstance(ind,(int,str)) else 1))
            f.write("\n" if raw.endswith("\n") else "")
        changed.append("%s (%s) · %s" % (t, os.path.basename(p), ok))

for c in changed: print("  ✅", c)
for s in skipped: print("  ⚠️", s)

# ── ③ เขียน bank.json ใหม่ด้วยรูปแบบเดิม
print("\n=== ③ คืนรูปแบบเดิมให้ bank.json ===")
if orig_indent is None:
    print("  ⚠️ ข้าม — ไม่รู้รูปแบบเดิม")
else:
    with io.open(BANK, encoding="utf-8") as f:
        bank = json.load(f)
    with io.open(BACKUP, encoding="utf-8") as f:
        tail_nl = f.read()[-1:] == "\n"
    with io.open(BANK, "w", encoding="utf-8") as f:
        json.dump(bank, f, ensure_ascii=False, indent=orig_indent)
        if tail_nl: f.write("\n")
    a, b = os.path.getsize(BACKUP), os.path.getsize(BANK)
    print("  ไฟล์สำรอง %d ไบต์ · เขียนใหม่ %d ไบต์ · ต่างกัน %+d" % (a, b, b-a))
    print("  ⬤ ถ้าต่างกันหลักไม่กี่ร้อยไบต์ = รูปแบบตรงแล้ว (ส่วนต่างคือเนื้อ notes ที่เพิ่ม)")
    print("  ⚠️ ถ้ายังต่างกันเป็นล้านไบต์ ⇒ บอกผม อย่าเพิ่ง commit")

# ── ④ ตรวจซ้ำ
print("\n=== ④ ตรวจซ้ำจากไฟล์ที่เขียนแล้ว ===")
with io.open(BANK, encoding="utf-8") as f:
    again = {q["id"]: q for q in json.load(f)["questions"]}
for t in TARGETS:
    r = again.get(t, {})
    print("  bank.json  %-26s correct=%-6r flawedSource=%r" % (t, r.get("correct"), r.get("flawedSource", False)))
for t in TARGETS:
    for p in found.get(t, []):
        with io.open(p, encoding="utf-8") as f:
            d = json.load(f)
        items = d.get("questions", d) if isinstance(d, dict) else d
        r = next((q for q in items if q.get("id")==t), {})
        print("  sets/%-22s %-26s correct=%-6r flawedSource=%r" % (os.path.basename(p), t, r.get("correct"), r.get("flawedSource", False)))
print("\n  chap-10-complex-q81 ใน bank มีขีดบน:", "\\overline{1 + i}" in again.get("chap-10-complex-q81", {}).get("question",""))

print("\n📌 ขั้นถัดไป: ถ้าโปรเจคมีตัว build ที่สร้าง bank.json จาก sets ⇒ รัน build แล้วเทียบว่าตรงกัน · แล้วค่อย git commit")

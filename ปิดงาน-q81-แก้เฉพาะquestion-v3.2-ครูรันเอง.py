# -*- coding: utf-8 -*-
"""
v3.2 — ปิดงาน chap-10-complex-q81 : แก้ "เฉพาะช่อง question" เท่านั้น
⛔ ไม่แตะช่อง explanation เด็ดขาด — เฉลยเก่าเดินตามโจทย์แบบไม่มีขีดบน ถ้าแทนที่ตรง ๆ จะได้เฉลยครึ่ง ๆ กลาง ๆ
   (v3.1 พบว่าเฉลยเก่าเขียน  z = 2(3+4i)/(1+i) = (6+8i)/(1+i)  ⇒ ได้ 7+i ⇒ ส่วนจินตภาพ 1 ⛔ ไม่ใช่ 7)

วิธีรัน (ในโฟลเดอร์ math-bank):
   python "ปิดงาน-q81-แก้เฉพาะquestion-v3.2-ครูรันเอง.py"            ← ดูก่อน + พิมพ์เฉลยเก่าเต็ม
   python "ปิดงาน-q81-แก้เฉพาะquestion-v3.2-ครูรันเอง.py" --apply    ← แก้ช่อง question
⛔ ไม่แตะ git · สำรองอัตโนมัติ
"""
import os, sys, io, json, shutil

APPLY = "--apply" in sys.argv
BANK  = os.path.join("data", "bank.json")
QID   = "chap-10-complex-q81"
OLD   = "(3 + 4i)}{1 + i}"
NEW_RAW = "(3 + 4i)}{\\\\overline{1 + i}}"
NEW_STR = "(3 + 4i)}{\\overline{1 + i}}"

print("โหมด:", "🔴 แก้จริง (--apply)" if APPLY else "🟢 ดูอย่างเดียว")

with io.open(BANK, "r", encoding="utf-8", newline="") as f:
    txt = f.read()

i = txt.find('"%s"' % QID)
if i < 0: sys.exit("⛔ ไม่พบ %s" % QID)
j = txt.find('"id"', i + len(QID) + 2)
if j < 0: j = len(txt)

# ── หา span ของช่อง "question" ในบล็อกนี้ (นับ escape ให้ถูก)
qk = txt.find('"question"', i, j)
if qk < 0: sys.exit("⛔ ไม่พบช่อง question ในบล็อก q81")
s = txt.find('"', txt.find(":", qk) ) + 1      # เปิดค่าสตริง
p = s
while p < j:
    if txt[p] == "\\": p += 2; continue
    if txt[p] == '"': break
    p += 1
qspan = (s, p)
qval = txt[s:p]
print("\n=== ช่อง question (ยาว %d ตัวอักษร) ===" % len(qval))
print("  ", qval[:300])
print("   พบ %r ในช่องนี้ %d จุด" % (OLD, qval.count(OLD)))

if APPLY:
    if NEW_RAW in qval:
        print("\n⬤ ช่อง question มีขีดบนอยู่แล้ว ⇒ ไม่แก้ซ้ำ")
    elif qval.count(OLD) != 1:
        print("\n⛔ ไม่ยูนีกในช่อง question (เจอ %d) ⇒ ไม่แก้" % qval.count(OLD))
    else:
        bak = BANK + ".bak-v32"
        if not os.path.exists(bak): shutil.copy2(BANK, bak)
        size0 = os.path.getsize(BANK)
        txt = txt[:s] + qval.replace(OLD, NEW_RAW, 1) + txt[p:]
        with io.open(BANK, "w", encoding="utf-8", newline="") as f:
            f.write(txt)
        size1 = os.path.getsize(BANK)
        print("\n✅ แก้ช่อง question แล้ว · ขนาด %d → %d (%+d ไบต์)" % (size0, size1, size1 - size0))

# ── พิมพ์เฉลยเก่าเต็ม ๆ ให้ครูตัดสิน
with io.open(BANK, encoding="utf-8") as f:
    bank = json.load(f)
q = {x["id"]: x for x in bank["questions"]}[QID]
print("\n=== ตรวจซ้ำ ===")
print("  จำนวนข้อในคลัง:", len(bank["questions"]), "(ต้องเป็น 6557)")
print("  correct =", q.get("correct"), "(ต้องเป็น 7)")
print("  ช่อง question มีขีดบน:", NEW_STR in q.get("question",""))
print("  ช่อง explanation มีข้อความเก่า:", OLD in q.get("explanation",""))

exp = q.get("explanation", "")
print("\n=== 🔴 เฉลยเก่าของ q81 (เต็ม %d ตัวอักษร) — ครูอ่านแล้วเคาะว่าจะเอายังไง ===" % len(exp))
import re
print(re.sub(r"<[^>]+>", "", exp).replace("\n\n", "\n").strip()[:2500])
print("\n📌 ทางเลือก: ก) ปล่อยไว้ รอเฉลยละเอียด t1 มาแทน · ข) ให้ E ร่างเฉลยเก่าใหม่ให้ตรงกับโจทย์ที่มีขีดบน · ค) ลบเฉลยเก่าทิ้ง")

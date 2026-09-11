# -*- coding: utf-8 -*-
"""
v3.1 — ปิดงานข้อ chap-10-complex-q81 (ขีดบนที่ตัวส่วน)
เหตุ: v3.0 เจอข้อความ '(3 + 4i)}{1 + i}' 2 ครั้งในไฟล์ ⇒ การ์ดสั่งข้าม (ถูกแล้ว)
v3.1 ทำ 2 รอบ:
   รอบ A (ดูอย่างเดียว) : พิมพ์ให้ดูว่า 2 จุดนั้นอยู่ช่องไหน พร้อมข้อความรอบ ๆ  ⛔ ไม่แก้อะไร
   รอบ B (แก้)          : รันซ้ำด้วย  --apply  ⇒ แก้เฉพาะจุดที่อยู่ในบล็อกของ q81 เท่านั้น

วิธีรัน (ในโฟลเดอร์ math-bank):
   python "ปิดงาน-q81-ขีดบน-v3.1-ครูรันเอง.py"            ← ดูก่อน
   python "ปิดงาน-q81-ขีดบน-v3.1-ครูรันเอง.py" --apply    ← แก้จริง
⛔ ไม่ re-serialize bank.json (ผ่าที่ตัวข้อความ) · ⛔ ไม่แตะ git · สำรองให้อัตโนมัติตอน --apply
"""
import os, sys, io, json, shutil

APPLY  = "--apply" in sys.argv
BANK   = os.path.join("data", "bank.json")
SETFILE= os.path.join("data", "sets", "chap-10-complex.json")
QID    = "chap-10-complex-q81"
OLD    = "(3 + 4i)}{1 + i}"
NEW_RAW= "(3 + 4i)}{\\\\overline{1 + i}}"   # ในไฟล์ JSON ดิบ (แบ็กสแลชคู่)
NEW_STR= "(3 + 4i)}{\\overline{1 + i}}"     # ในสตริงที่ถอดแล้ว

print("โหมด:", "🔴 แก้จริง (--apply)" if APPLY else "🟢 ดูอย่างเดียว")

# ═══════ ส่วนที่ 1 : bank.json (ผ่าที่ตัวข้อความ) ═══════
with io.open(BANK, "r", encoding="utf-8", newline="") as f:
    txt = f.read()

key = '"%s"' % QID
i = txt.find(key)
if i < 0:
    sys.exit("⛔ ไม่พบ %s ใน bank.json" % QID)
j = txt.find('"id"', i + len(key))
if j < 0: j = len(txt)
print("\n=== bank.json : บล็อกของ %s ยาว %d ตัวอักษร ===" % (QID, j - i))

pos, hits = 0, []
while True:
    k = txt.find(OLD, pos)
    if k < 0: break
    hits.append(k); pos = k + 1
print("พบข้อความ %r ทั้งไฟล์ %d จุด:" % (OLD, len(hits)))
for n, k in enumerate(hits, 1):
    inside = (i <= k < j)
    # เดาชื่อช่องจากคีย์ล่าสุดก่อนตำแหน่งนั้น
    field = "?"
    for cand in ('"question"', '"explanation"', '"choices"', '"notes"', '"hint"'):
        c = txt.rfind(cand, 0, k)
        if c > 0 and (field == "?" or c > txt.rfind('"%s"' % field.strip('"'), 0, k)):
            field = cand
    print("  จุดที่ %d · ตำแหน่ง %d · อยู่ในบล็อก q81: %s · ช่อง %s" % (n, k, "ใช่" if inside else "⛔ ไม่ใช่", field))
    print("     …%s…" % txt[max(0, k-90):k+70].replace("\r", "").replace("\n", " ⏎ "))

in_block = [k for k in hits if i <= k < j]
print("\n⇒ อยู่ในบล็อกของ q81 จำนวน %d จุด · อยู่นอกบล็อก %d จุด" % (len(in_block), len(hits) - len(in_block)))
if len(hits) - len(in_block) > 0:
    print("  ⚠️ มีจุดนอกบล็อก ⇒ ⛔ v3.1 จะไม่แตะจุดนั้นเด็ดขาด (เป็นของข้ออื่น)")

if APPLY and in_block:
    bak = BANK + ".bak-v31"
    if not os.path.exists(bak): shutil.copy2(BANK, bak)
    size0 = os.path.getsize(BANK)
    seg = txt[i:j].replace(OLD, NEW_RAW)
    txt = txt[:i] + seg + txt[j:]
    with io.open(BANK, "w", encoding="utf-8", newline="") as f:
        f.write(txt)
    size1 = os.path.getsize(BANK)
    print("\n✅ bank.json แก้ %d จุดในบล็อก q81 · ขนาด %d → %d (%+d ไบต์)" % (len(in_block), size0, size1, size1 - size0))

# ═══════ ส่วนที่ 2 : data/sets/chap-10-complex.json (ต้นฉบับจริง) ═══════
print("\n=== ต้นฉบับ %s ===" % SETFILE)
if not os.path.exists(SETFILE):
    print("  ⛔ ไม่พบไฟล์")
else:
    with io.open(SETFILE, encoding="utf-8") as f:
        data = json.load(f)
    items = data.get("questions", data) if isinstance(data, dict) else data
    q = next((x for x in items if x.get("id") == QID), None)
    if q is None:
        print("  ⛔ ไม่พบ", QID)
    else:
        todo = [k for k, v in q.items() if isinstance(v, str) and OLD in v]
        done = [k for k, v in q.items() if isinstance(v, str) and NEW_STR in v]
        print("  ช่องที่ยังตกขีดบน:", todo or "⬤ ไม่มีแล้ว")
        print("  ช่องที่มีขีดบนแล้ว:", done or "—")
        if APPLY and todo:
            bak = SETFILE + ".bak-v31"
            if not os.path.exists(bak): shutil.copy2(SETFILE, bak)
            for k in todo:
                q[k] = q[k].replace(OLD, NEW_STR)
            with io.open(SETFILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write("\n")
            print("  ✅ แก้ช่อง %s แล้ว" % ", ".join(todo))

# ═══════ ตรวจซ้ำ ═══════
print("\n=== ตรวจซ้ำ ===")
with io.open(BANK, encoding="utf-8") as f:
    bank = json.load(f)
qs = {x["id"]: x for x in bank["questions"]}
r = qs.get(QID, {})
print("  จำนวนข้อในคลัง:", len(bank["questions"]), "(ต้องเป็น 6557)")
print("  correct =", r.get("correct"), "(ต้องเป็น 7)")
for k, v in r.items():
    if isinstance(v, str) and ("overline" in v or OLD in v):
        print("  ช่อง %-12s : %s" % (k, "⬤ มีขีดบน" if NEW_STR in v else "⛔ ยังตก"))
print("\n📌 %s" % ("ถ้าเขียวหมด ⇒ commit ได้" if APPLY else "ดูรายการข้างบนแล้วถ้าถูกต้อง ⇒ รันซ้ำด้วย --apply"))

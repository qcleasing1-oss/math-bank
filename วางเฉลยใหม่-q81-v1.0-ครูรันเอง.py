# -*- coding: utf-8 -*-
"""
วางเฉลยใหม่ของ chap-10-complex-q81 (ทาง ข ที่ครูเคาะ 10 ก.ย.)
เฉลยเก่าเดินตามโจทย์แบบไม่มีขีดบน ⇒ ได้ z = 7+i ⇒ ส่วนจินตภาพ 1 ⛔ ไม่ตรงคีย์ 7
เฉลยใหม่เดินตามต้นฉบับ (มีขีดบน) ⇒ z = -1+7i ⇒ ส่วนจินตภาพ 7 ✅ ตรงคีย์

วิธีรัน (ในโฟลเดอร์ math-bank):
   python "วางเฉลยใหม่-q81-v1.0-ครูรันเอง.py"           ← ดูเฉลยใหม่ก่อน ⛔ ไม่แก้
   python "วางเฉลยใหม่-q81-v1.0-ครูรันเอง.py" --apply   ← วางจริง (bank.json + data/sets)
⛔ bank.json ใช้การผ่าที่ตัวข้อความ ⛔ ไม่ re-serialize ทั้งไฟล์ · สำรองอัตโนมัติ · ⛔ ไม่แตะ git
"""
import os, sys, io, json, shutil

APPLY  = "--apply" in sys.argv
BANK   = os.path.join("data", "bank.json")
SETF   = os.path.join("data", "sets", "chap-10-complex.json")
QID    = "chap-10-complex-q81"

NEW = [
 "<b>📐 ความรู้พื้นฐาน</b>",
 "$\\begin{aligned} |\\sqrt{4i}| &= \\sqrt{|4i|} \\\\ &= \\sqrt4 \\\\ &= 2 \\end{aligned}$",
 "ขีดบนคือสังยุค: $\\overline{a+bi} = a-bi$ ⇒ $\\overline{1+i} = 1-i$",
 "",
 "<b>🎯 เป้าหมาย</b> หา $z$ แล้วอ่านค่าส่วนจินตภาพ",
 "",
 "<b>【 พื้นฐาน · จัดรูปแล้วหารจำนวนเชิงซ้อน (simplify then complex division) 】</b>",
 "",
 "<b>ขั้นที่ 1:</b> $|\\sqrt{4i}| = 2$ และ $\\overline{1+i} = 1-i$ → $z = \\dfrac{2(3+4i)}{1-i} = \\dfrac{6+8i}{1-i}$",
 "<b>ขั้นที่ 2:</b> คูณสังยุคของตัวส่วน $(1+i)$ ทั้งเศษและส่วน: $\\dfrac{(6+8i)(1+i)}{(1-i)(1+i)} = \\dfrac{6+6i+8i+8i^2}{2} = \\dfrac{-2+14i}{2} = -1+7i$",
 "<b>ขั้นที่ 3:</b> $z = -1+7i$ → ส่วนจริง $= -1$ , ส่วนจินตภาพ $= 7$",
 "",
 "<b>✔ ตรวจคำตอบ</b> แทนกลับ: $(-1+7i)(1-i) = -1+i+7i-7i^2 = 6+8i$ ✓ ตรงกับตัวเศษ $2(3+4i)$",
 "",
 "✅ คำตอบ: ส่วนจินตภาพของ $z$ เท่ากับ $7$",
 "",
 "<b>💡 เทคนิคที่ใช้</b> $|\\sqrt{4i}| = \\sqrt{|4i|}$ — ขนาดของรากเท่ากับรากของขนาด",
 "<b>⚠️ จุดที่เด็กมักผิด</b> มองข้ามขีดบนที่ตัวส่วน แล้วหารด้วย $1+i$ ⇒ ได้ $z = 7+i$ ⇒ ตอบ $1$ ซึ่งผิด",
 "หรือสับสนส่วนจริงกับส่วนจินตภาพ (ข้อนี้ส่วนจริงเป็นลบ ส่วนจินตภาพเป็นบวก)",
 "หรือคิด $|\\sqrt{4i}|$ ผิดเป็น $4$"
]

print("=== เฉลยใหม่ %d ชิ้น ===" % len(NEW))
for n, s in enumerate(NEW): print(" [%02d] %s" % (n, s))
if not APPLY:
    print("\n📌 ถ้าถูกต้อง ⇒ รันซ้ำด้วย --apply")
    sys.exit(0)

# ═══ bank.json : ผ่าเฉพาะอาเรย์ explanation ของ q81 ═══
with io.open(BANK, "r", encoding="utf-8", newline="") as f:
    txt = f.read()
i = txt.find('"%s"' % QID)
if i < 0: sys.exit("⛔ ไม่พบ %s" % QID)
j = txt.find('"id"', i + len(QID) + 2)
if j < 0: j = len(txt)
k = txt.find('"explanation"', i, j)
if k < 0: sys.exit("⛔ ไม่พบช่อง explanation ในบล็อก q81")
s = txt.find("[", k)
# ไล่หาวงเล็บปิดคู่ของมัน โดยข้ามข้อความในเครื่องหมายคำพูด
p, depth, instr = s, 0, False
while p < j:
    ch = txt[p]
    if instr:
        if ch == "\\": p += 2; continue
        if ch == '"': instr = False
    else:
        if ch == '"': instr = True
        elif ch == "[": depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0: break
    p += 1
if depth != 0: sys.exit("⛔ หาวงเล็บปิดของ explanation ไม่เจอ ⇒ ไม่แก้")
line_start = txt.rfind("\n", 0, k) + 1
base = txt[line_start:k]                      # ระยะย่อหน้าของบรรทัด "explanation"
body = json.dumps(NEW, ensure_ascii=False, indent=2)
body = "\n".join((base + ln) if n else ln for n, ln in enumerate(body.split("\n")))
bak = BANK + ".bak-เฉลยq81"
if not os.path.exists(bak): shutil.copy2(BANK, bak)
size0 = os.path.getsize(BANK)
txt = txt[:s] + body + txt[p+1:]
with io.open(BANK, "w", encoding="utf-8", newline="") as f:
    f.write(txt)
print("\n✅ bank.json · ขนาด %d → %d (%+d ไบต์)" % (size0, os.path.getsize(BANK), os.path.getsize(BANK) - size0))

# ═══ data/sets (ต้นฉบับ) ═══
with io.open(SETF, encoding="utf-8") as f:
    data = json.load(f)
items = data.get("questions", data) if isinstance(data, dict) else data
q = next((x for x in items if x.get("id") == QID), None)
if q is None:
    print("⛔ ไม่พบ q81 ใน", SETF)
else:
    bak2 = SETF + ".bak-เฉลยq81"
    if not os.path.exists(bak2): shutil.copy2(SETF, bak2)
    q["explanation"] = NEW
    q["notes"] = (q.get("notes", "") + " | 10 ก.ย. 69: เขียนเฉลยใหม่ — เฉลยเดิมเดินตามโจทย์ที่ตกขีดบน ได้ z=7+i ⇒ ส่วนจินตภาพ 1 ⛔ ไม่ตรงคีย์ 7 · ฉบับใหม่ใช้ \\overline{1+i}=1-i ⇒ z=-1+7i ⇒ 7 ✅").strip(" |")
    with io.open(SETF, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2); f.write("\n")
    print("✅ %s เขียนแล้ว" % SETF)

# ═══ ตรวจซ้ำ ═══
with io.open(BANK, encoding="utf-8") as f:
    bank = json.load(f)
r = {x["id"]: x for x in bank["questions"]}[QID]
print("\n=== ตรวจซ้ำ ===")
print("  จำนวนข้อในคลัง:", len(bank["questions"]), "(ต้องเป็น 6557)")
print("  correct =", r.get("correct"), "· ชนิด explanation =", type(r.get("explanation")).__name__,
      "· จำนวนชิ้น =", len(r.get("explanation") or []))
print("  question มีขีดบน:", "\\overline{1 + i}" in r.get("question", ""))
joined = " ".join(x for x in r["explanation"] if isinstance(x, str))
print("  เฉลยใหม่มี '-1+7i':", "-1+7i" in joined.replace(" ", ""))
print("  เฉลยใหม่ยังมี '7+i' แบบเดิมไหม (ควรมีเฉพาะในบรรทัดจุดที่เด็กมักผิด):", joined.count("7+i"))

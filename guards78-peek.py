# -*- coding: utf-8 -*-
"""
ดูกติกาด่าน 7 และ 8 · v1.0 · ครูรันเอง
--------------------------------------
⛔ สคริปต์นี้ "อ่านอย่างเดียว" — ไม่แก้ ไม่ย้าย ไม่ลบไฟล์ใด ๆ ทั้งสิ้น
⛔ ไม่แตะ git
จุดประสงค์: ดึงกติกาจริงของด่าน 7/8 ออกมาให้ E อ่าน จะได้ไม่ต้องเดา

ใช้:  cd A:\โปรเจคสอนคณิตศาสตร์\math-bank
      python guards78-peek.py

ผลลัพธ์: ไฟล์  _guards78-rules-for-E.txt  ในโฟลเดอร์ math-bank
         (ครูเปิดแล้ว copy ทั้งไฟล์ส่งให้ผมในแชท)
"""
import os, re, sys, io

ROOT = os.getcwd()
OUT  = os.path.join(ROOT, "_guards78-rules-for-E.txt")
YML  = os.path.join(ROOT, ".github", "workflows", "guards.yml")

buf = io.StringIO()
def p(s=""):
    print(s)
    buf.write(s + "\n")

p("=" * 70)
p("กติกาด่าน 7 / 8  ·  ดึงจาก repo จริง  ·  อ่านอย่างเดียว")
p("โฟลเดอร์ที่รัน: " + ROOT)
p("=" * 70)

if not os.path.isfile(YML):
    p("⛔ ไม่พบ " + YML)
    p("   ครูรันสคริปต์นี้ในโฟลเดอร์ math-bank หรือยังครับ")
    sys.exit(1)

raw = open(YML, "rb").read().decode("utf-8", "replace")
lines = raw.split("\n")

# ---------- 1) ตัดเฉพาะ step ที่ชื่อมี "ด่าน 7" / "ด่าน 8" ----------
p("\n[1] ขั้นตอนใน guards.yml ที่ชื่อมี 'ด่าน 7' หรือ 'ด่าน 8'")
p("-" * 70)

step_starts = [i for i, L in enumerate(lines) if re.match(r"^\s*-\s+name:", L)]
step_starts.append(len(lines))

scripts_found = set()
for k in range(len(step_starts) - 1):
    a, b = step_starts[k], step_starts[k + 1]
    head = lines[a]
    if ("ด่าน 7" in head) or ("ด่าน 8" in head):
        p("")
        for L in lines[a:b]:
            p("    " + L.rstrip())
        blob = "\n".join(lines[a:b])
        for m in re.finditer(r"[\w\-/\\\.]+\.py", blob):
            scripts_found.add(m.group(0).replace("\\", "/"))

if not scripts_found:
    p("\n⚠️ ไม่พบชื่อไฟล์ .py ในสองขั้นตอนนี้ — อาจเป็นสคริปต์ฝังใน yml")

# ---------- 2) cat สคริปต์ที่อ้างถึง ----------
p("\n\n[2] เนื้อในสคริปต์ที่ด่าน 7/8 เรียกใช้")
p("-" * 70)

for rel in sorted(scripts_found):
    path = os.path.join(ROOT, rel.replace("/", os.sep))
    p("\n### ไฟล์: " + rel)
    if not os.path.isfile(path):
        p("    (ไม่พบไฟล์นี้ในเครื่อง)")
        continue
    src = open(path, "rb").read().decode("utf-8", "replace")
    p("    ขนาด %d ไบต์ · %d บรรทัด" % (len(src.encode("utf-8")), src.count("\n") + 1))
    p("    " + "-" * 60)
    for i, L in enumerate(src.split("\n"), 1):
        p("    %4d | %s" % (i, L.rstrip()))

# ---------- 3) ค่าเพดาน ----------
p("\n\n[3] บรรทัดที่มีคำว่า MAX_UNDECLARED / เพดาน (ทั้ง repo, เฉพาะ .py และ .yml)")
p("-" * 70)
hits = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "__pycache__")]
    for fn in filenames:
        if not fn.endswith((".py", ".yml", ".yaml")):
            continue
        fp = os.path.join(dirpath, fn)
        try:
            t = open(fp, "rb").read().decode("utf-8", "replace")
        except Exception:
            continue
        if "MAX_UNDECLARED" in t or "เพดาน" in t:
            for i, L in enumerate(t.split("\n"), 1):
                if "MAX_UNDECLARED" in L or "เพดาน" in L:
                    p("  %s:%d | %s" % (os.path.relpath(fp, ROOT), i, L.strip()))
                    hits += 1
if hits == 0:
    p("  (ไม่พบ)")

p("\n" + "=" * 70)
p("จบ · เขียนผลลงไฟล์: " + OUT)
p("=" * 70)

with open(OUT, "wb") as f:
    f.write(buf.getvalue().encode("utf-8"))

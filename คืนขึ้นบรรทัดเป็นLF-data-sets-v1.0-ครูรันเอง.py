# -*- coding: utf-8 -*-
"""
คืนขึ้นบรรทัดของไฟล์ใน data\\sets ให้เป็น LF ตามที่ repo สั่งไว้   (v1.0 · ครูรันเอง)
==============================================================================
ที่มา (ใบ 368 ของ CC · ⬤ วัดจากชั้น git):
    git ls-files --eol data/sets  →  62 ไฟล์ = i/lf ทั้งหมด · attr text eol=lf
    working tree                  →  w/lf 59 · w/crlf 3
  ⇒ **ใน repo ทุกไฟล์เป็น LF อยู่แล้ว** · CRLF มีเฉพาะสำเนาบนดิสก์เครื่องนี้ 3 ไฟล์
  ⇒ `.gitattributes` (7 ส.ค.) สั่ง `*.json text eol=lf` ⇒ CRLF บนดิสก์คือ **ของแปลกปลอม**

🪞 E ยอมรับ: เมื่อ 11 ก.ย. E ประกาศว่า "ต้องรักษา CRLF ไว้" — ผิดที่เหตุผล
   (git กลืน \\r ทิ้งตอน add อยู่แล้ว ความเสียหายต่อ repo = 0)
   เหตุผลที่ยังยืน = สคริปต์ต้องไม่เปลี่ยนสิ่งที่ไม่ได้สั่งให้เปลี่ยน
   สคริปต์ตัวนี้ต่างออกไป: **สั่งให้เปลี่ยนโดยตรง และรายงานทุกตัวเลข**

สิ่งที่ทำ : แปลง CRLF → LF เฉพาะไฟล์ที่ยังมี CRLF ใน data\\sets (+ data\\bank.json ถ้ามี)
สิ่งที่ ⛔ ไม่ทำ : ไม่แตะเนื้อ JSON · ไม่ re-serialize · ไม่ยุ่ง git · ไม่ลบไฟล์
         ⛔ ข้ามไฟล์สำรอง .bak-* ทุกตัว (ปล่อยไว้เป็นหลักฐานเดิม)

ด่านตรวจ : JSON ต้อง parse ได้ทั้งก่อนและหลัง · จำนวนข้อต้องเท่าเดิม
         ขนาดที่หายต้องเท่ากับจำนวน CRLF พอดี ⛔ ถ้าไม่ตรง = ยกเลิกไฟล์นั้น

ใช้งาน
    python "คืนขึ้นบรรทัดเป็นLF-data-sets-v1.0-ครูรันเอง.py"           ← ดูอย่างเดียว
    python "คืนขึ้นบรรทัดเป็นLF-data-sets-v1.0-ครูรันเอง.py" --apply   ← เขียนจริง
"""
import hashlib, json, os, shutil, sys

ROOT  = os.path.dirname(os.path.abspath(__file__))
SETS  = os.path.join(ROOT, "data", "sets")
BANK  = os.path.join(ROOT, "data", "bank.json")
APPLY = "--apply" in sys.argv


def md5(b):
    return hashlib.md5(b).hexdigest().upper()[:8]


def nq(raw):
    d = json.loads(raw.decode("utf-8"))
    qs = d["questions"] if isinstance(d, dict) and "questions" in d else d
    return len(qs)


targets = []
if os.path.isdir(SETS):
    for fn in sorted(os.listdir(SETS)):
        if fn.endswith(".json") and ".bak" not in fn:
            targets.append(os.path.join(SETS, fn))
if os.path.exists(BANK):
    targets.append(BANK)

print("=" * 74)
print("คืนขึ้นบรรทัดเป็น LF  %s" % ("(เขียนจริง)" if APPLY else "(dry-run — ยังไม่เขียน)"))
print("=" * 74)
print("⬤ ไฟล์ที่ตรวจ: %d (ข้ามไฟล์สำรอง .bak-* ทั้งหมด)" % len(targets))

hits, clean, fail = [], 0, 0
for p in targets:
    raw = open(p, "rb").read()
    crlf = raw.count(b"\r\n")
    cr = raw.count(b"\r")
    if crlf == 0 and cr == 0:
        clean += 1
        continue
    name = os.path.relpath(p, ROOT)
    if cr != crlf:
        print("  ⚠️ %s : มี \\r เดี่ยว %d ตัวที่ไม่ได้คู่กับ \\n ⇒ ⛔ ข้าม ให้ครูดูเอง" % (name, cr - crlf))
        fail += 1
        continue
    hits.append((p, name, raw, crlf))

print("-" * 74)
print("⬤ เป็น LF อยู่แล้ว: %d ไฟล์" % clean)
print("🔧 ต้องแปลง: %d ไฟล์" % len(hits))
if fail:
    print("⚠️ ข้าม: %d ไฟล์" % fail)

for p, name, raw, crlf in hits:
    try:
        n0 = nq(raw)
    except Exception as e:
        print("  ⛔ %s : JSON เดิมอ่านไม่ออก (%s) ⇒ ข้าม" % (name, e))
        continue
    new = raw.replace(b"\r\n", b"\n")
    drop = len(raw) - len(new)
    ok_size = (drop == crlf)
    try:
        n1 = nq(new)
    except Exception as e:
        print("  ⛔ %s : แปลงแล้ว JSON พัง (%s) ⇒ ข้าม" % (name, e))
        continue
    print("-" * 74)
    print("  %s" % name)
    print("    ขนาด   : %d → %d  (−%d)   %s" % (len(raw), len(new), drop,
          "✅ เท่ากับจำนวน CRLF พอดี" if ok_size else "⛔ ไม่ตรงกับ CRLF %d — ข้าม" % crlf))
    print("    CRLF   : %d → %d" % (crlf, new.count(b"\r\n")))
    print("    จำนวนข้อ: %d → %d   %s" % (n0, n1, "✅" if n0 == n1 else "⛔ ไม่เท่า — ข้าม"))
    print("    md5    : %s → %s" % (md5(raw), md5(new)))
    if not (ok_size and n0 == n1):
        continue
    if not APPLY:
        print("    (dry-run — ยังไม่เขียน)")
        continue
    bak = p + ".bak-ก่อนคืนLF"
    if not os.path.exists(bak):
        shutil.copy2(p, bak)
    with open(p, "wb") as f:
        f.write(new)
    chk = open(p, "rb").read()
    print("    ✅ เขียนแล้ว · ตรวจซ้ำ: ขนาด %d · CRLF %d · จำนวนข้อ %d · md5 %s"
          % (len(chk), chk.count(b"\r\n"), nq(chk), md5(chk)))

print("-" * 74)
if APPLY:
    print("เสร็จ · ⛔ สคริปต์นี้ไม่ได้แตะ git")
    print("🔔 ขั้นถัดไป: git status ควรยังสะอาด (index เป็น LF อยู่แล้ว)")
    print("   ถ้า git ขึ้นว่าไฟล์เปลี่ยน = ผิดคาด ให้หยุดแล้วบอก E")
else:
    print("ถ้าถูกต้องแล้ว สั่งซ้ำด้วย --apply เพื่อเขียนจริง")
print("=" * 74)

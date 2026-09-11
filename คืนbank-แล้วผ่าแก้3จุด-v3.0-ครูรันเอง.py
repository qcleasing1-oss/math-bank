# -*- coding: utf-8 -*-
"""
v3.0 — คืน data/bank.json จากไฟล์สำรองให้ "ตรงทุกไบต์" แล้วผ่าแก้เฉพาะ 3 จุดในตัวข้อความ
⇒ ⛔ ไม่ re-serialize ทั้งไฟล์ ⇒ git เห็นแค่ 3 บรรทัด · ขนาดต่างจากเดิมไม่กี่สิบไบต์

วิธีรัน (ในโฟลเดอร์ math-bank):  python "คืนbank-แล้วผ่าแก้3จุด-v3.0-ครูรันเอง.py"
⛔ ไม่แตะ data/sets (v2 แก้ถูกแล้ว) · ⛔ ไม่แตะ git
"""
import os, sys, io, json, hashlib, shutil

BANK   = os.path.join("data", "bank.json")
BACKUP = os.path.join("data", "bank.json.bak-2026-09-10-ก่อนแก้3ข้อ")

def md5(p, chunk=1 << 20):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()

if not os.path.exists(BACKUP):
    sys.exit("⛔ ไม่พบไฟล์สำรอง %s — หยุดไว้ก่อน อย่าทำอะไรต่อ" % BACKUP)

print("① คืนไฟล์จากสำรอง (ไบนารี ⇒ ตรงทุกไบต์)")
shutil.copyfile(BACKUP, BANK)          # copyfile = คัดลอกเนื้อดิบ ⛔ ไม่แปลงบรรทัด
m_bak, m_now = md5(BACKUP), md5(BANK)
print("   md5 สำรอง = %s" % m_bak[:8])
print("   md5 ปัจจุบัน = %s  ⇒ %s" % (m_now[:8], "⬤ ตรงกันทุกไบต์" if m_bak == m_now else "⛔ ไม่ตรง — หยุด!"))
if m_bak != m_now:
    sys.exit(1)
size0 = os.path.getsize(BANK)

# อ่านเป็น "ไบต์" แล้วถอดเป็นข้อความโดยไม่แปลงบรรทัด
with io.open(BANK, "r", encoding="utf-8", newline="") as f:
    txt = f.read()
print("   อ่านเข้ามา %d ตัวอักษร · %d ไบต์บนดิสก์" % (len(txt), size0))

edits, problems = [], []

def window(text, qid):
    """ตัดช่วงข้อความของข้อนั้น: ตั้งแต่ "id": "<qid>" ถึง "id": ตัวถัดไป"""
    key = '"%s"' % qid
    i = text.find(key)
    if i < 0: return None, None
    j = text.find('"id"', i + len(key))
    if j < 0: j = len(text)
    return i, j

# ── จุดที่ 1 : chap-02-logic-q37  correct 2 → 0
i, j = window(txt, "chap-02-logic-q37")
if i is None:
    problems.append("chap-02-logic-q37 · ⛔ ไม่พบ id ในไฟล์")
else:
    seg = txt[i:j]
    if '"correct": 0' in seg:
        problems.append("chap-02-logic-q37 · correct=0 อยู่แล้ว ⇒ ข้าม")
    elif seg.count('"correct": 2') != 1:
        problems.append('chap-02-logic-q37 · หา \'"correct": 2\' ไม่เจอ/ไม่ยูนีก (เจอ %d) ⇒ ข้าม' % seg.count('"correct": 2'))
    else:
        txt = txt[:i] + seg.replace('"correct": 2', '"correct": 0', 1) + txt[j:]
        edits.append("chap-02-logic-q37 · correct 2 → 0")

# ── จุดที่ 2 : chap-10-complex-q81  เติมขีดบนที่ตัวส่วน
OLD = "(3 + 4i)}{1 + i}"
NEW = "(3 + 4i)}{\\\\overline{1 + i}}"     # ในไฟล์ JSON แบ็กสแลชเขียนเป็นคู่
if "\\\\overline{1 + i}" in txt:
    problems.append("chap-10-complex-q81 · มีขีดบนอยู่แล้ว ⇒ ข้าม")
elif txt.count(OLD) != 1:
    problems.append("chap-10-complex-q81 · เจอ %r %d ครั้ง (ต้องเจอ 1) ⇒ ข้าม" % (OLD, txt.count(OLD)))
else:
    txt = txt.replace(OLD, NEW, 1)
    edits.append("chap-10-complex-q81 · เติม \\overline ที่ตัวส่วน")

# ── จุดที่ 3 : pat1-2555-10-q15  เพิ่ม "flawedSource": true
i, j = window(txt, "pat1-2555-10-q15")
if i is None:
    problems.append("pat1-2555-10-q15 · ⛔ ไม่พบ id ในไฟล์")
elif '"flawedSource"' in txt[i:j]:
    problems.append("pat1-2555-10-q15 · มี flawedSource อยู่แล้ว ⇒ ข้าม")
else:
    line_end = txt.find("\n", i)                       # ท้ายบรรทัด "id": "pat1-2555-10-q15",
    nxt = txt.find("\n", line_end + 1)
    indent = ""
    for ch in txt[line_end + 1:nxt]:
        if ch in " \t": indent += ch
        else: break
    nl = "\r\n" if txt[line_end - 1:line_end + 1] == "\r\n" or "\r\n" in txt[:2000] else "\n"
    txt = txt[:line_end + 1] + indent + '"flawedSource": true,' + nl + txt[line_end + 1:]
    edits.append('pat1-2555-10-q15 · เพิ่ม "flawedSource": true')

print("\n② ผลการผ่าแก้")
for e in edits: print("   ✅", e)
for p in problems: print("   ⚠️", p)

if not edits:
    print("\n⛔ ไม่ได้แก้อะไร — bank.json เท่ากับไฟล์สำรองทุกไบต์")
    sys.exit(0)

with io.open(BANK, "w", encoding="utf-8", newline="") as f:   # newline="" = ⛔ ไม่แปลงบรรทัด
    f.write(txt)
size1 = os.path.getsize(BANK)
print("\n③ ขนาดไฟล์  เดิม %d → ใหม่ %d  ⇒ ต่างกัน %+d ไบต์" % (size0, size1, size1 - size0))
print("   ⬤ ควรต่างไม่เกินราว ๆ 30–60 ไบต์ (แก้เลข 1 ตัว + เติมข้อความสั้น 2 จุด)")
if abs(size1 - size0) > 500:
    print("   ⛔ ต่างเกินคาด — บอก E ก่อน commit")

print("\n④ ตรวจซ้ำ: อ่าน JSON กลับขึ้นมาทั้งไฟล์ (ถ้าพังจะ error ตรงนี้)")
with io.open(BANK, encoding="utf-8") as f:
    bank = json.load(f)
qs = {q["id"]: q for q in bank["questions"]}
print("   จำนวนข้อในคลัง:", len(bank["questions"]), "(ต้องเป็น 6557)")
for t in ("chap-02-logic-q37", "chap-10-complex-q81", "pat1-2555-10-q15"):
    r = qs.get(t, {})
    print("   %-26s correct=%-6r flawedSource=%r" % (t, r.get("correct"), r.get("flawedSource", False)))
print("   chap-10-complex-q81 มีขีดบน:", "\\overline{1 + i}" in qs.get("chap-10-complex-q81", {}).get("question", ""))
print("\n📌 ถ้าทั้ง 4 ขั้นเขียว ⇒ git diff จะเห็นแค่ 3 บรรทัดใน bank.json + 3 ไฟล์ใน data/sets ⇒ commit ได้")

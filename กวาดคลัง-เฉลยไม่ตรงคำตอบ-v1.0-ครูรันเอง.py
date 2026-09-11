# -*- coding: utf-8 -*-
"""
v1.0 — ① ดึงเฉลยเก่าของ chap-10-complex-q81 ออกมาเป็นไฟล์ (ให้ E ร่างใหม่)
        ② กวาดทั้งคลังหาข้อที่ "ผลลัพธ์สุดท้ายในเฉลย ไม่ตรงกับ correct"
วิธีรัน (ในโฟลเดอร์ math-bank):  python "กวาดคลัง-เฉลยไม่ตรงคำตอบ-v1.0-ครูรันเอง.py"
⛔ อ่านอย่างเดียว ⛔ ไม่แก้ bank.json ⛔ ไม่แตะ git
ผลออกที่โฟลเดอร์ _t1run\audit\
"""
import os, io, json, re, csv, sys

BANK = os.path.join("data", "bank.json")
OUT  = os.path.join("_t1run", "audit")
os.makedirs(OUT, exist_ok=True)

with io.open(BANK, encoding="utf-8") as f:
    bank = json.load(f)
qs = bank["questions"]
print("⬤ อ่านคลัง %d ข้อ" % len(qs))

# ── ① ดึงเฉลยเก่าของ q81
q81 = next((q for q in qs if q.get("id") == "chap-10-complex-q81"), None)
if q81:
    p = os.path.join(OUT, "q81_ทั้งข้อ.json")
    with io.open(p, "w", encoding="utf-8") as f:
        json.dump(q81, f, ensure_ascii=False, indent=2)
    print("① เขียน", p, "(%d ไบต์)" % os.path.getsize(p))
    print("   ชนิดของช่อง explanation:", type(q81.get("explanation")).__name__,
          "· จำนวนชิ้น:", len(q81.get("explanation") or []))

# ── ② กวาดคลัง
def raw_text(o, acc=None):
    """เก็บสตริงจริงทั้งหมดจาก dict/list ⛔ ห้ามใช้ json.dumps (มันทำ \\ เป็น \\\\)"""
    if acc is None: acc = []
    if isinstance(o, str): acc.append(o)
    elif isinstance(o, dict):
        for v in o.values(): raw_text(v, acc)
    elif isinstance(o, list):
        for v in o: raw_text(v, acc)
    return acc

TAG = re.compile(r"<[^>]+>")
def norm(s):
    s = TAG.sub(" ", s)
    s = s.replace("\\left", "").replace("\\right", "").replace("\\,", "").replace("\;", "")
    s = s.replace("\\dfrac", "\\frac").replace("\\tfrac", "\\frac")
    s = s.replace("$", "").replace("{", "").replace("}", "")
    s = s.replace("(", "").replace(")", "").replace(",", "")
    return re.sub(r"\s+", "", s)

def num_in(hay, needle):
    """หาเลขโดยกันไม่ให้ 7 ไปแมตช์กลาง 17 หรือ 70"""
    return re.search(r"(?<![0-9.])" + re.escape(needle) + r"(?![0-9.])", hay) is not None

rows, counts = [], {"ตรวจได้": 0, "ข้าม": 0, "ไม่เจอคำตอบเลย": 0, "เจอแต่ไม่ได้อยู่ท้ายเฉลย": 0}
for q in qs:
    try:
        exp = q.get("explanation")
        cor = q.get("correct")
        if not exp or cor is None or q.get("retired"):
            counts["ข้าม"] += 1; continue
        parts = raw_text(exp)
        if not parts:
            counts["ข้าม"] += 1; continue
        whole = norm(" ".join(parts))
        tail  = norm(" ".join(parts[-3:]))[-900:]

        typ = q.get("type")
        ch  = q.get("choices")
        if isinstance(ch, list) and ch and isinstance(cor, int) and 0 <= cor < len(ch):
            expected = ch[cor]; kind = "mc"
        else:
            expected = str(cor); kind = "fill"
        exp_n = norm(str(expected))
        if not exp_n or len(exp_n) < 1:
            counts["ข้าม"] += 1; continue

        if kind == "fill" and re.fullmatch(r"-?[0-9.]+", exp_n):
            hit_all, hit_tail = num_in(whole, exp_n), num_in(tail, exp_n)
        else:
            hit_all, hit_tail = (exp_n in whole), (exp_n in tail)

        counts["ตรวจได้"] += 1
        if not hit_all:
            counts["ไม่เจอคำตอบเลย"] += 1
            rows.append([q["id"], q.get("setId",""), typ, repr(cor), str(expected)[:80], "ไม่เจอเลย",
                         len(parts), "🔴 คำตอบไม่ปรากฏในเฉลยเลย"])
        elif not hit_tail:
            counts["เจอแต่ไม่ได้อยู่ท้ายเฉลย"] += 1
            rows.append([q["id"], q.get("setId",""), typ, repr(cor), str(expected)[:80], "เจอแต่ไม่อยู่ท้าย",
                         len(parts), "🟡 อาจเป็นการเอ่ยกลางทาง ⛔ ไม่ใช่ผลสรุป"])
    except Exception as e:
        counts["ข้าม"] += 1
        rows.append([q.get("id","?"), q.get("setId",""), q.get("type",""), "", "", "ตรวจไม่ได้", 0, "⚠️ %s" % e])

csvp = os.path.join(OUT, "audit_เฉลยไม่ตรงคำตอบ_2026-09-10.csv")
with io.open(csvp, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id","setId","type","correct","คำตอบที่คาด","ผลตรวจ","จำนวนชิ้นเฉลย","หมายเหตุ"])
    w.writerows(rows)

print("\n② ผลกวาด")
for k, v in counts.items(): print("   %-24s %d" % (k, v))
print("   เขียนรายงาน:", csvp, "(%d แถว)" % len(rows))

from collections import Counter
c = Counter(r[1] for r in rows if r[5] == "ไม่เจอเลย")
print("\n   🔴 กลุ่ม 'ไม่เจอคำตอบเลย' แยกตามชุด (10 อันดับแรก):")
for k, v in c.most_common(10): print("      %-28s %d" % (k or "-", v))
print("\n📌 ส่งไฟล์ CSV กับ q81_ทั้งข้อ.json ให้ E — E จะคัดตัวจริงออกจากตัวหลอกให้")

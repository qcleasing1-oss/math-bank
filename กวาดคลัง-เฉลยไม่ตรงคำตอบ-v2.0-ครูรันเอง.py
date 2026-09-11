# -*- coding: utf-8 -*-
"""
กวาดคลัง: เฉลยชี้คำตอบคนละอันกับ `correct` หรือไม่   (v2.0 · ครูรันเอง)
============================================================================
🪞 ทำไมต้องมี v2.0 — v1.0 และ v1.1 ของผมเชื่อไม่ได้ทั้งคู่
   v1.0 ได้ 787 · v1.1 ได้ 469 · ผมสุ่มเปิด 3 ข้อแรกของ v1.1 ปรากฏว่า
   **ถูกทั้ง 3 ข้อ** (alvl1-2566-03-q02/q04/q08 เฉลยชี้ตัวเลือก 4/5/1
   ตรงกับ correct = 3/4/0 เป๊ะ) ⇒ 469 คือสัญญาณเท็จเกือบทั้งกอง
   สาเหตุ: v1.1 ตัด "220 ตัวอักษรท้ายสุด" ซึ่งไปตกที่ท่อน
   «⚠️ จุดที่เด็กมักผิด» ⛔ ไม่ใช่ท่อน «✅ คำตอบ»

v2.0 เปลี่ยนวิธีทั้งหมด — เลิกเดาจากหาง ใช้การเทียบเลขตัวเลือกตรง ๆ
   1) หาชิ้นเฉลยที่เป็น "บรรทัดคำตอบ" จริง ๆ (มี ✅ หรือ «คำตอบ:») — เอาชิ้นท้ายสุด
   2) ข้อ mc : อ่านเลขหลังคำว่า ตัวเลือก / ข้อ / ตัวเลือกที่ ในบรรทัดนั้น
              แล้วเทียบกับ correct+1 (คลังนี้เก็บ correct แบบเริ่มที่ 0)
              ⇒ ตรง = 🟢 · ไม่ตรง = 🔴 **ขัดกันจริง** (ชนิดเดียวกับ q37 ที่ครูเคาะ)
   3) ข้อ fill: เทียบค่า correct หลายรูป (เศษส่วน · ทศนิยม · \\frac · \\dfrac)
   4) ไม่มีบรรทัดคำตอบให้ตรวจ = ⚪ ⛔ ไม่นับเป็นของเสีย

⚖️ 🔴 ของ v2.0 = "เฉลยบอกตัวเลือก A แต่คลังเก็บ B" ซึ่งอย่างใดอย่างหนึ่งผิดแน่นอน
    ⛔ ไม่ใช่ "เครื่องมือหาไม่เจอ" แบบสองรุ่นก่อน

ใช้งาน
    python "กวาดคลัง-เฉลยไม่ตรงคำตอบ-v2.0-ครูรันเอง.py"

⛔ อ่านอย่างเดียว · ⛔ ไม่แก้ไฟล์ใด · ⛔ ไม่ยุ่ง git · ข้ามข้อที่ติด flawedSource
"""
import csv, io, json, os, re, sys
from fractions import Fraction

ROOT   = os.path.dirname(os.path.abspath(__file__))
SETS   = os.path.join(ROOT, "data", "sets")
OUTDIR = os.path.join(ROOT, "_t1run", "audit")
OUT    = os.path.join(OUTDIR, "audit_v20_เฉลยชี้คนละข้อ.csv")

ANSLINE = re.compile(r"✅|คำตอบ\s*[:：]")
PICK    = re.compile(r"(?:ตัวเลือกที่|ตัวเลือก|ข้อที่|ข้อ)\s*(?:ที่\s*)?(\d+)")
TAG     = re.compile(r"<[^>]+>")


def flat(x):
    """แปลง explanation (list / str / dict ซ้อน) เป็นรายการข้อความ"""
    if isinstance(x, str):
        return [x]
    if isinstance(x, list):
        out = []
        for i in x:
            out.extend(flat(i))
        return out
    if isinstance(x, dict):
        out = []
        for v in x.values():
            out.extend(flat(v))
        return out
    return []


def plain(s):
    return TAG.sub("", s)


def variants(v):
    """รูปเขียนที่เป็นไปได้ของคำตอบข้อเติมคำ"""
    out = set()
    s = str(v).strip()
    if not s:
        return out
    out.add(s)
    out.add(s.replace(" ", ""))
    m = re.fullmatch(r"(-?\d+)\s*/\s*(\d+)", s)
    if m:
        a, b = m.group(1), m.group(2)
        out.add("%s/%s" % (a, b))
        out.add(r"\frac{%s}{%s}" % (a, b))
        out.add(r"\dfrac{%s}{%s}" % (a, b))
        try:
            out.add("%g" % (int(a) / int(b)))
        except Exception:
            pass
    try:
        f = Fraction(s)
        if f.denominator != 1:
            out.add("%d/%d" % (f.numerator, f.denominator))
            out.add(r"\frac{%d}{%d}" % (f.numerator, f.denominator))
            out.add(r"\dfrac{%d}{%d}" % (f.numerator, f.denominator))
            out.add("%g" % float(f))
        else:
            out.add(str(f.numerator))
    except Exception:
        pass
    try:
        fl = float(s)
        out.add("%g" % fl)
        if abs(fl - round(fl)) < 1e-12:
            out.add(str(int(round(fl))))
    except Exception:
        pass
    return {x for x in out if x}


print("=" * 70)
print("กวาดคลัง v2.0 — เฉลยชี้คำตอบคนละอันกับ correct หรือไม่")
print("=" * 70)

green = red = amber = white = skip = 0
oob = []          # correct เกินจำนวนตัวเลือก
rows = []
nf = ntot = 0
for fn in sorted(os.listdir(SETS)):
    if not fn.endswith(".json"):
        continue
    nf += 1
    d = json.loads(open(os.path.join(SETS, fn), "rb").read().decode("utf-8"))
    qs = d["questions"] if isinstance(d, dict) and "questions" in d else d
    for q in qs:
        if not isinstance(q, dict):
            continue
        ntot += 1
        qid = q.get("id")
        setid = q.get("setId") or fn[:-5]
        if q.get("flawedSource"):
            skip += 1
            continue
        cor = q.get("correct")
        if cor is None:
            skip += 1
            continue
        items = flat(q.get("explanation"))
        if not items:
            skip += 1
            continue
        cand = [plain(e) for e in items if ANSLINE.search(e)]
        if not cand:
            white += 1
            rows.append([qid, setid, q.get("type"), cor, "", "⚪ ไม่มีบรรทัดคำตอบ", ""])
            continue
        line = cand[-1]
        typ = q.get("type")
        if typ == "mc" and isinstance(cor, int) and not isinstance(cor, bool):
            ch = q.get("choices") or []
            if ch and cor >= len(ch):
                oob.append(qid)
            want = cor + 1
            nums = [int(x) for x in PICK.findall(line)]
            if nums:
                if want in nums:
                    green += 1
                else:
                    red += 1
                    rows.append([qid, setid, typ, cor,
                                 "เฉลยชี้ตัวเลือก %s แต่คลังเก็บ %d" % ("/".join(map(str, nums)), want),
                                 "🔴 ขัดกัน", line[:200]])
            else:
                txt = plain(ch[cor]) if ch and cor < len(ch) else ""
                key = re.sub(r"\s+", "", txt)[:24]
                if key and key in re.sub(r"\s+", "", line):
                    green += 1
                else:
                    amber += 1
                    rows.append([qid, setid, typ, cor, "บรรทัดคำตอบไม่ระบุเลขตัวเลือก",
                                 "🟠 ตรวจด้วยตา", line[:200]])
        else:
            vs = variants(cor)
            flatline = line.replace(" ", "")
            if any(v.replace(" ", "") in flatline for v in vs):
                green += 1
            else:
                amber += 1
                rows.append([qid, setid, typ, cor, "ไม่พบค่า %s ในบรรทัดคำตอบ" % cor,
                             "🟠 ตรวจด้วยตา", line[:200]])

print("⬤ อ่านคลังจากต้นฉบับ %d ไฟล์ · %d ข้อ" % (nf, ntot))
print("-" * 70)
print("🟢 เฉลยตรงกับ correct              : %5d" % green)
print("🔴 **เฉลยชี้คนละข้อกับคลัง**       : %5d   ⇒ ต้องเคาะทุกข้อ (ทรงเดียวกับ q37)" % red)
print("🟠 บรรทัดคำตอบมี แต่เทียบไม่ลงตัว  : %5d   ⇒ ตรวจด้วยตา" % amber)
print("⚪ ไม่มีบรรทัดคำตอบให้ตรวจ         : %5d   ⛔ ไม่ใช่ของเสีย" % white)
print("   ข้าม (flawedSource / correct ว่าง / ไม่มีเฉลย): %d" % skip)
if oob:
    print("-" * 70)
    print("⚠️ correct เกินจำนวนตัวเลือก %d ข้อ: %s" % (len(oob), ", ".join(oob[:10])))

if not os.path.isdir(OUTDIR):
    os.makedirs(OUTDIR)
with io.open(OUT, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "ชุด", "type", "correct", "เหตุผล", "ธง", "บรรทัดคำตอบในเฉลย (200 ตัว)"])
    w.writerows(sorted(rows, key=lambda r: (r[5], r[0])))
print("-" * 70)
print("CSV: %s  (%d แถว)" % (OUT, len(rows)))
print("📌 ส่งภาพผลรันนี้ให้ E พอ ⛔ ครูไม่ต้องเปิด CSV เอง")
print("=" * 70)

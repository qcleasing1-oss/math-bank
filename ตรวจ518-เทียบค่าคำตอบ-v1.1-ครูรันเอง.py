# -*- coding: utf-8 -*-
"""
ตรวจกอง 🟠 518 ข้อ — เทียบ "ค่า" ในบรรทัดคำตอบ กับตัวเลือก/คำตอบที่คลังเก็บ
(v1.1 · ครูรันเอง)
============================================================================
กอง 🟠 จาก `กวาดคลัง v2.0` คือข้อที่ **มีบรรทัด «✅ คำตอบ» แต่เทียบไม่ลงตัว**
แยกได้ 2 ทรง
  • mc 254 ข้อ  — บรรทัดคำตอบเขียนเป็น "ค่า" ⛔ ไม่ได้บอกเลขข้อ
      เช่น «✅ คำตอบ: $f'(x)=h(x)$»
  • fill 264 ข้อ — คลังเก็บ correct เป็นข้อความธรรมดา แต่เฉลยเขียนเป็น LaTeX
      เช่น correct = `x^3 - (3/2)x^2` · เฉลย = «$f(x)=x^3-\\dfrac{3}{2}x^2-x+\\dfrac{3}{2}$»
  ⇒ ทั้งสองทรง "ไม่ใช่ของเสีย" แต่เครื่องรุ่นก่อนอ่านไม่ออก

v1.0 เพิ่มตัวแปลงรูป LaTeX ให้เทียบได้:
   \\dfrac{a}{b} · \\frac{a}{b}  →  a/b      |  \\sim → ~   |  \\varnothing → ∅
   ตัด $ \\left \\right \\displaystyle \\, \; \\! วงเล็บ ช่องว่าง แท็ก html ทิ้ง
แล้วอ่าน "บล็อกคำตอบ" = ชิ้น «✅ คำตอบ» + อีก 2 ชิ้นถัดไป (เผื่อค่าไปอยู่บรรทัดล่าง)

ผลลัพธ์
   🟢 ค่าตรงกับที่คลังเก็บ            ⇒ ปลอดภัย ปิดได้
   🔴 ค่าตรงกับ "ตัวเลือกอื่น"        ⇒ ของเสียจริง ต้องเคาะ
   ⚪ เทียบไม่ได้                     ⇒ ต้องใช้ตาครู

ใช้งาน
    python "ตรวจ518-เทียบค่าคำตอบ-v1.0-ครูรันเอง.py"

⛔ อ่านอย่างเดียว · ⛔ ไม่แก้ไฟล์ใด · ⛔ ไม่ยุ่ง git
"""
import csv, io, json, os, re

ROOT   = os.path.dirname(os.path.abspath(__file__))
SETS   = os.path.join(ROOT, "data", "sets")
OUTDIR = os.path.join(ROOT, "_t1run", "audit")
OUT    = os.path.join(OUTDIR, "audit_v31_กอง518.csv")
SRC    = os.path.join(OUTDIR, "audit_v20_เฉลยชี้คนละข้อ.csv")   # ผลของ v2.0 — ใช้เลือกเฉพาะกอง 🟠

TAG     = re.compile(r"<[^>]+>")
ANSLINE = re.compile(r"✅|คำตอบ\s*[:：]")
PICK    = re.compile(r"(?:ตัวเลือกที่|ตัวเลือก|ข้อที่|ข้อ)\s*(\d+)")
FRAC2   = re.compile(r"\\[dt]?frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}")
FRAC1   = re.compile(r"\\[dt]?frac\s*(-?\d)\s*(-?\d)")
SQRTB   = re.compile(r"\\sqrt\s*\{([^{}]*)\}")
SQRTN   = re.compile(r"\\sqrt\s*")
WRAP    = re.compile(r"\\(mathbb|mathcal|mathrm|text|operatorname)\s*\{([^{}]*)\}")

# ⛔ ลำดับสำคัญ: ตัวยาวต้องมาก่อน ไม่งั้น \infty จะโดน \in กินกลายเป็น "∈fty"
SYM = [("\\infty", "∞"), ("\\varnothing", "∅"), ("\\emptyset", "∅"),
       ("\\subseteq", "⊆"), ("\\subset", "⊂"), ("\\times", "×"),
       ("\\cdot", "·"), ("\\cup", "∪"), ("\\cap", "∩"),
       ("\\sim", "~"), ("\\pm", "±"), ("\\mp", "∓"),
       ("\\leq", "≤"), ("\\geq", "≥"), ("\\neq", "≠"),
       ("\\in", "∈"), ("√", "sqrt")]


def norm(s):
    """ทำ LaTeX กับข้อความธรรมดาให้อยู่รูปเดียวกันเพื่อเทียบค่า"""
    s = TAG.sub("", str(s))
    for _ in range(4):
        t = WRAP.sub(r"\2", s)
        t = SQRTB.sub(r"sqrt(\1)", t)
        t = FRAC2.sub(r"(\1)/(\2)", t)
        t = FRAC1.sub(r"\1/\2", t)
        if t == s:
            break
        s = t
    s = SQRTN.sub("sqrt", s)
    for a, b in SYM:
        s = s.replace(a, b)
    s = re.sub(r"\\[,;!:\s]", "", s)
    s = re.sub(r"[\\$\s()\u200b]", "", s)
    return s.lower()


def flat(x):
    if isinstance(x, str):
        return [x]
    if isinstance(x, list):
        r = []
        for i in x:
            r.extend(flat(i))
        return r
    return []


print("=" * 72)
print("ตรวจกอง 🟠 — เทียบค่าในบรรทัดคำตอบกับคลัง")
print("=" * 72)

if not os.path.exists(SRC):
    raise SystemExit("⛔ ไม่เจอ %s — ต้องรัน 'กวาดคลัง-เฉลยไม่ตรงคำตอบ-v2.0' ก่อน" % SRC)
TARGET = set()
with io.open(SRC, encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        if (row.get("ธง") or "").startswith("🟠"):
            TARGET.add(row["id"])
print("⬤ รับกอง 🟠 จาก v2.0 มา %d ข้อ" % len(TARGET))

g = r = w = 0
rows = []
nq = 0
for fn in sorted(os.listdir(SETS)):
    if not fn.endswith(".json"):
        continue
    d = json.loads(open(os.path.join(SETS, fn), "rb").read().decode("utf-8"))
    qs = d["questions"] if isinstance(d, dict) and "questions" in d else d
    for q in qs:
        if not isinstance(q, dict) or q.get("id") not in TARGET:
            continue
        c = q.get("correct")
        if c is None:
            continue
        items = flat(q.get("explanation"))
        if not items:
            continue
        idxs = [i for i, e in enumerate(items) if ANSLINE.search(e)]
        if not idxs:
            continue
        i = idxs[-1]
        line = TAG.sub("", items[i])
        typ = q.get("type")
        ch = q.get("choices") or []
        # ข้อที่ v2.0 ตัดสินไปแล้ว (มีเลขข้อในบรรทัด) ⇒ ข้าม
        if typ == "mc" and isinstance(c, int) and PICK.search(line):
            continue
        block = norm(" ".join(TAG.sub("", e) for e in items[i:i + 3]))
        setid = q.get("setId") or fn[:-5]
        if typ == "mc" and isinstance(c, int) and not isinstance(c, bool) and ch and 0 <= c < len(ch):
            hits = []
            for k, x in enumerate(ch):
                nx = norm(x)
                if len(nx) >= 3 and nx in block:
                    hits.append(k)
            if hits == [c]:
                g += 1
            elif hits and c not in hits:
                r += 1
                rows.append([q["id"], setid, typ, c, "🔴 ค่าตรงกับตัวเลือกอื่น",
                             "เฉลยไปตรงกับข้อ %s" % ",".join(str(k + 1) for k in hits), line[:150]])
            elif c in hits:
                g += 1
            else:
                w += 1
                rows.append([q["id"], setid, typ, c, "⚪ เทียบไม่ได้", "", line[:150]])
        else:
            nc = norm(c)
            if len(nc) >= 1 and nc in block:
                g += 1
            else:
                w += 1
                rows.append([q["id"], setid, typ, c, "⚪ เทียบไม่ได้", "", line[:150]])

tot = g + r + w
print("⬤ ตรวจได้ %d จาก %d ข้อ" % (tot, len(TARGET)))
print("-" * 72)
print("🟢 ค่าตรงกับที่คลังเก็บ        : %4d   ⇒ ปลอดภัย ปิดได้เลย" % g)
print("🔴 ค่าตรงกับตัวเลือกอื่น       : %4d   ⇒ ของเสียจริง ต้องเคาะ" % r)
print("⚪ เทียบไม่ได้                 : %4d   ⇒ ต้องใช้ตาครู" % w)
if r:
    print("-" * 72)
    print("🔴 รายชื่อ:")
    for x in rows:
        if x[4].startswith("🔴"):
            print("   %-26s correct=%-4s %s" % (x[0], x[3], x[5]))

if not os.path.isdir(OUTDIR):
    os.makedirs(OUTDIR)
with io.open(OUT, "w", encoding="utf-8-sig", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["id", "ชุด", "type", "correct", "ธง", "หมายเหตุ", "บรรทัดคำตอบ"])
    wr.writerows(sorted(rows, key=lambda x: (x[4], x[0])))
print("-" * 72)
print("CSV: %s  (%d แถว)" % (OUT, len(rows)))
print("📌 ส่งภาพผลรันนี้ให้ E พอ ⛔ ครูไม่ต้องเปิด CSV เอง")
print("=" * 72)

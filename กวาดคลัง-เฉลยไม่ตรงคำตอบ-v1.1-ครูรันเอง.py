# -*- coding: utf-8 -*-
"""
v1.1 — กวาดคลังหาข้อที่ "ผลสรุปในเฉลย ไม่ตรงกับ correct"
🪞 v1.0 ให้ตัวเลขเฟ้อ (787 / 4,333) เพราะ 3 จุด — v1.1 แก้ครบ:
   ① ท่อนสรุปไม่ใช่ "3 ชิ้นสุดท้าย" — เฉลยจบด้วยบล็อกเทคนิค/จุดที่เด็กมักผิด
      ⇒ v1.1 หาบล็อกที่มีคำว่า "คำตอบ / ✅ / ตอบ" แล้วใช้ตั้งแต่ตรงนั้นเป็นท่อนสรุป
   ② เศษส่วน: คีย์เก็บ "12/25" แต่เฉลยเขียน \\dfrac{12}{25} ⇒ ต้องเทียบรูปเทียบเท่า + ทศนิยม
   ③ ปรนัย: เฉลยมักเขียน "ตอบข้อ 3" ⛔ ไม่ยกข้อความตัวเลือกมาทั้งประโยค ⇒ ต้องรับรูปนี้ด้วย
วิธีรัน (ในโฟลเดอร์ math-bank):  python "กวาดคลัง-เฉลยไม่ตรงคำตอบ-v1.1-ครูรันเอง.py"
⛔ อ่านอย่างเดียว · ผลออกที่ _t1run\audit\
"""
import os, io, json, re, csv
from collections import Counter
from fractions import Fraction

BANK = os.path.join("data", "bank.json")
OUT  = os.path.join("_t1run", "audit")
os.makedirs(OUT, exist_ok=True)
with io.open(BANK, encoding="utf-8") as f:
    bank = json.load(f)
qs = bank["questions"]
print("⬤ อ่านคลัง %d ข้อ" % len(qs))

def raw_text(o, acc=None):
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
    for a in ("\\left", "\\right", "\\,", "\;", "\\!", "\\ ", "\\displaystyle"):
        s = s.replace(a, "")
    s = s.replace("\\dfrac", "\\frac").replace("\\tfrac", "\\frac")
    s = s.replace("$", "").replace("{", "").replace("}", "")
    s = s.replace("(", "").replace(")", "").replace(",", "")
    s = s.replace("−", "-").replace("–", "-")
    return re.sub(r"\s+", "", s)

def needles(expected):
    """สร้างรูปเทียบเท่าของคำตอบ 1 ค่า"""
    out, e = set(), norm(str(expected))
    if not e: return out
    out.add(e)
    m = re.fullmatch(r"(-?)(\d+)/(\d+)", e)
    if m:
        sg, a, b = m.group(1), m.group(2), m.group(3)
        out.add("%s\\frac%s%s" % (sg, a, b))
        out.add("\\frac%s%s%s" % (sg, a, b))
        try:
            v = float(Fraction(int(a), int(b))) * (-1 if sg else 1)
            for d in (2, 3, 4):
                out.add(("%%.%df" % d) % v)
            out.add(repr(round(v, 6)).rstrip("0").rstrip("."))
        except Exception: pass
    m = re.fullmatch(r"(-?)\\frac(\d+)(\d+)", e)
    if m: out.add("%s%s/%s" % (m.group(1), m.group(2), m.group(3)))
    return {x for x in out if x}

def num_ok(hay, nd):
    if re.fullmatch(r"-?[\d.]+", nd):
        return re.search(r"(?<![0-9.])" + re.escape(nd) + r"(?![0-9.])", hay) is not None
    return nd in hay

ANS = re.compile(r"(คำตอบ|✅|ตอบ|สรุป|ANSWER)")
def tail_of(parts):
    """ท่อนสรุป = ตั้งแต่ชิ้นที่พูดถึงคำตอบเป็นต้นไป · ไม่เจอ ⇒ 6 ชิ้นท้าย"""
    idx = [n for n, s in enumerate(parts) if ANS.search(s)]
    if idx: return " ".join(parts[min(idx):])
    return " ".join(parts[-6:])

rows, cnt = [], Counter()
for q in qs:
    try:
        exp, cor = q.get("explanation"), q.get("correct")
        if not exp or cor is None or q.get("retired") or q.get("flawedSource"):
            cnt["ข้าม"] += 1; continue
        parts = [p for p in raw_text(exp) if p and p.strip()]
        if not parts: cnt["ข้าม"] += 1; continue
        whole, tail = norm(" ".join(parts)), norm(tail_of(parts))

        ch = q.get("choices")
        is_mc = isinstance(ch, list) and ch and isinstance(cor, int) and 0 <= cor < len(ch)
        nds = needles(ch[cor] if is_mc else cor)
        if is_mc:            # รับรูป "ตอบข้อ N" ด้วย
            n = cor + 1
            for pat in ("ตอบข้อ%d" % n, "ข้อ%d" % n, "ตัวเลือกที่%d" % n, "ข้อที่%d" % n):
                nds.add(norm(pat))
        if not nds: cnt["ข้าม"] += 1; continue

        cnt["ตรวจได้"] += 1
        hit_tail  = any(num_ok(tail, nd)  for nd in nds)
        hit_whole = any(num_ok(whole, nd) for nd in nds)
        if hit_tail: continue
        lvl = "🔴 ไม่เจอเลย" if not hit_whole else "🟡 เจอกลางทางแต่ไม่อยู่ท่อนสรุป"
        cnt[lvl] += 1
        rows.append([q["id"], q.get("setId",""), q.get("type",""), repr(cor),
                     str(ch[cor] if is_mc else cor)[:70], lvl, len(parts),
                     norm(tail_of(parts))[-220:]])
    except Exception as e:
        cnt["ตรวจไม่ได้"] += 1
        rows.append([q.get("id","?"), q.get("setId",""), q.get("type",""), "", "", "⚠️ error", 0, str(e)[:120]])

rows.sort(key=lambda r: (r[5] != "🔴 ไม่เจอเลย", r[1], r[0]))
p = os.path.join(OUT, "audit_v11_เฉลยไม่ตรงคำตอบ.csv")
with io.open(p, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id","setId","type","correct","คำตอบที่คาด","ระดับ","ชิ้นเฉลย","ท่อนสรุป(ตัดมา 220 ตัวท้าย)"])
    w.writerows(rows)

print("\n=== ผลกวาด v1.1 ===")
for k, v in cnt.most_common(): print("   %-34s %d" % (k, v))
print("   เขียนรายงาน:", p, "(%d แถว)" % len(rows))
red = [r for r in rows if r[5].startswith("🔴")]
print("\n   🔴 แยกตามชุด (10 อันดับแรก):")
for k, v in Counter(r[1] for r in red).most_common(10): print("      %-30s %d" % (k or "-", v))
print("\n📌 ส่งไฟล์ CSV ให้ E — E จะสุ่มตรวจแล้วบอกว่าเหลือของจริงกี่ข้อ")

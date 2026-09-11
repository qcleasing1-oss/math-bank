# -*- coding: utf-8 -*-
"""
พิสูจน์: เฉลย t1 ของ 776 ข้อนั้น "เคยเห็นตาราง/รูป" หรือไม่  (v1.2 · ครูรันเอง)
------------------------------------------------------------------------------
v1.0 ตอบได้แค่ว่า "มีข้อที่มีตาราง/รูป และ t1 ทำไปแล้ว 776 ข้อ"
     ⛔ ยังไม่ได้พิสูจน์ว่าเฉลยพวกนั้นมั่วจริงหรือไม่

v1.1 พิสูจน์ด้วยหลักฐานในตัวเฉลยเอง:
     ดึง "ตัวเลขเฉพาะ" ออกจากตาราง/แผนภูมิของแต่ละข้อ (เช่น 24.0, 39.5, 70.3, 22, 36 …)
     แล้วดูว่าตัวเลขพวกนั้นโผล่ในเนื้อเฉลยของ t1 กี่ตัว
       • พบ 0%        → 🔴 t1 ไม่เคยเห็นตาราง/รูปแน่นอน  ⇒ เฉลยใช้ไม่ได้
       • พบ 1–49%     → 🟠 น่าสงสัยมาก
       • พบ ≥ 50%     → 🟢 น่าจะเห็น (หรือเดาถูก) ⇒ ผ่านชั้นนี้ไปก่อน

⬤ ที่รู้แน่แล้ว: ระเบียนที่ป้อน t1 ทุกยุค ⛔ ไม่มีช่อง tables และ ⛔ ไม่มีช่อง imageSpec
   (pack_*.json เก่า: id·topics·subTopics·difficulty·type·question·choices·correct·hasImage·old)
   (POOL-0xx.json ใหม่: id·type·difficulty·hasImage·hint·topics·subTopics·correct·choices·question)

ใช้งาน
    python "พิสูจน์-t1เห็นตารางไหม-v1.1-ครูรันเอง.py"

⛔ อ่านอย่างเดียว · ⛔ ไม่แก้ไฟล์ใด · ⛔ ไม่ยุ่ง git
⛔ ไม่โหลด t1_MASTER 51MB เข้าแรมทั้งก้อน — อ่านทีละระเบียน
"""
import codecs, csv, io, json, os, re, sys

ROOT   = os.path.dirname(os.path.abspath(__file__))
SETS   = os.path.join(ROOT, "data", "sets")
MASTER = os.path.join(ROOT, "_t1run", "results", "t1_MASTER.json")
OUTDIR = os.path.join(ROOT, "_t1run", "audit")
OUT    = os.path.join(OUTDIR, "audit_t1_พิสูจน์เห็นตารางไหม_v12.csv")

NUM = re.compile(r"\d+(?:\.\d+)?")

# คีย์ที่เป็น "ขนาด/พิกัดวาดรูป" ⛔ ไม่ใช่เนื้อหาโจทย์ — ตัดทิ้ง ไม่เอามานับ
LAYOUT = set("""width height viewBox x y x1 y1 x2 y2 cx cy r rx ry dx dy
fontSize font_size strokeWidth stroke_width padding margin offset opacity
size gap radius dpi scale tickStep step lineWidth angle rotate zIndex
top left right bottom""".split())


def walk(o, key=None, out=None):
    """เก็บ 'ตัวเลขเนื้อหา' จากตาราง/สเปกรูป แบบไล่ทุกชั้น ⛔ ข้ามคีย์ที่เป็นขนาด/พิกัด"""
    if out is None:
        out = []
    if key in LAYOUT:
        return out
    if isinstance(o, dict):
        for k, v in o.items():
            walk(v, k, out)
    elif isinstance(o, list):
        for v in o:
            walk(v, key, out)
    elif isinstance(o, str):
        out.extend(NUM.findall(o))          # ข้อความ/ป้าย = เนื้อหาเสมอ
    elif isinstance(o, (int, float)) and not isinstance(o, bool):
        out.append(("%g" % o) if isinstance(o, float) else str(o))
    return out


def tokens_from(q):
    """ตัวเลขเฉพาะที่ 'ต้องมี' ถ้าเฉลยได้เห็นตาราง/รูปจริง"""
    raw = walk(q.get("tables")) + walk(q.get("imageSpec"))
    uniq = []
    for t in raw:
        if len(t) >= 2 and t not in uniq:   # ยาว >= 2 ตัว กันเลข 0-9 ที่เจอได้ทั่วไป
            uniq.append(t)
    return uniq


print("=" * 68)
print("พิสูจน์ว่าเฉลย t1 เคยเห็นตาราง/รูปหรือไม่")
print("=" * 68)

need, meta, nonum = {}, {}, set()
nf = 0
for fn in sorted(os.listdir(SETS)):
    if not fn.endswith(".json"):
        continue
    nf += 1
    d = json.loads(open(os.path.join(SETS, fn), "rb").read().decode("utf-8"))
    qs = d["questions"] if isinstance(d, dict) and "questions" in d else d
    for q in qs:
        if not isinstance(q, dict):
            continue
        if not (q.get("tables") or q.get("imageSpec")):
            continue
        qid = q.get("id")
        tk = tokens_from(q)
        if not tk:
            nonum.add(qid)          # ตารางไม่มีตัวเลข (เช่น T/F) ⇒ พิสูจน์ด้วยเลขไม่ได้
            continue
        need[qid] = tk
        qtext = q.get("question") or ""
        inq = sum(1 for t in tk if t in qtext)
        meta[qid] = dict(
            setId=q.get("setId") or fn[:-5],
            kind="ตาราง" if q.get("tables") else "รูป",
            typ=q.get("type"),
            correct=q.get("correct"),
            inq=inq,
        )
print("① sets %d ไฟล์ · ข้อที่มีตาราง/รูป และดึงตัวเลขอ้างอิงได้: %d ข้อ" % (nf, len(need)))
print("   (อีก %d ข้อ ตาราง/รูปไม่มีตัวเลข เช่น T/F ⇒ พิสูจน์ด้วยวิธีนี้ไม่ได้)" % len(nonum))
nonum_hit = set()

# ── streaming: ดึงทีละระเบียนจาก t1_MASTER ────────────────────────
if not os.path.exists(MASTER):
    sys.exit("⛔ ไม่เจอ %s" % MASTER)
size = os.path.getsize(MASTER)
dec = codecs.getincrementaldecoder("utf-8")()
depth = 0
in_str = False
esc = False
buf = []
seen = {}
read = 0
with open(MASTER, "rb") as f:
    while True:
        raw = f.read(2 * 1024 * 1024)
        if not raw:
            break
        read += len(raw)
        for ch in dec.decode(raw):
            if depth > 0:
                buf.append(ch)
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
                continue
            if ch == '"':
                in_str = True
            elif ch == "{":
                if depth == 0:
                    buf = ["{"]
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    try:
                        rec = json.loads("".join(buf))
                    except Exception:
                        buf = []
                        continue
                    buf = []
                    qid = rec.get("id") if isinstance(rec, dict) else None
                    if qid in nonum:
                        nonum_hit.add(qid)
                    if qid in need and qid not in seen:
                        text = json.dumps(rec, ensure_ascii=False)
                        toks = need[qid]
                        found = [t for t in toks if t in text]
                        seen[qid] = (len(toks), len(found),
                                     [t for t in toks if t not in found][:6],
                                     (rec.get("given") or "")[:120] if isinstance(rec.get("given"), str) else "")
        sys.stdout.write("\r② อ่าน t1_MASTER ... %d%%  (จับคู่ได้ %d ข้อ)" % (read * 100 // size, len(seen)))
        sys.stdout.flush()
print("\r② t1_MASTER: จับคู่ข้อที่มีตาราง/รูปได้ %d ข้อ                    " % len(seen))

red = amber = green = blue = 0
rows = []
for qid, (n, k, miss, given) in sorted(seen.items()):
    pct = (k * 100 // n) if n else 0
    m = meta[qid]
    qpct = (m["inq"] * 100 // n) if n else 0
    if qpct >= 80:
        flag = "🔵 โจทย์มีเลขครบ"      # ตัวเลขอยู่ในเนื้อโจทย์อยู่แล้ว ⇒ ตารางหายก็ไม่กระทบ
        blue += 1
    elif pct == 0:
        flag = "🔴 ไม่เคยเห็น"
        red += 1
    elif pct < 50:
        flag = "🟠 น่าสงสัย"
        amber += 1
    else:
        flag = "🟢 น่าจะเห็น"
        green += 1
    rows.append([qid, m["setId"], m["kind"], m["typ"],
                 "" if m["correct"] is None else m["correct"],
                 n, k, "%d%%" % pct, "%d%%" % qpct, flag, " ".join(miss), given])

print("-" * 68)
print("③ ผลพิสูจน์ (จาก %d ข้อ)" % len(seen))
print("   🔵 โจทย์บรรยายตัวเลขครบอยู่แล้ว      : %4d ข้อ  ⇒ ตารางหายก็ไม่กระทบ ปลอดภัย" % blue)
print("   🔴 ไม่พบตัวเลขจากตาราง/รูปเลย        : %4d ข้อ  ⇒ เฉลยใช้ไม่ได้ ต้องทำใหม่" % red)
print("   🟠 พบบางส่วน (< 50%%)                 : %4d ข้อ  ⇒ ต้องดูด้วยตา" % amber)
print("   🟢 พบ ≥ 50%%                          : %4d ข้อ  ⇒ ผ่านชั้นนี้" % green)
print("   ⚪ ตารางไม่มีตัวเลข และ t1 ทำไปแล้ว   : %4d ข้อ  ⇒ ต้องดูด้วยตา (เช่น chap-02-logic-q99)" % len(nonum_hit))

if not os.path.isdir(OUTDIR):
    os.makedirs(OUTDIR)
with io.open(OUT, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "ชุด", "ชนิด", "type", "correct",
                "เลขที่ต้องมี", "เลขที่พบในเฉลย", "ร้อยละในเฉลย", "ร้อยละในโจทย์", "ธง",
                "ตัวอย่างเลขที่หาย", "given 120 ตัวอักษร"])
    w.writerows(rows)
print("-" * 68)
print("④ CSV: %s" % OUT)
print("   %d แถว · ส่งภาพผลรันนี้ให้ E พอ ⛔ ครูไม่ต้องเปิด CSV เอง" % len(rows))
print("=" * 68)

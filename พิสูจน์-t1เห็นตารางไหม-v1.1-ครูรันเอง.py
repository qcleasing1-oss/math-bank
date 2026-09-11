# -*- coding: utf-8 -*-
"""
พิสูจน์: เฉลย t1 ของ 776 ข้อนั้น "เคยเห็นตาราง/รูป" หรือไม่  (v1.1 · ครูรันเอง)
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
OUT    = os.path.join(OUTDIR, "audit_t1_พิสูจน์เห็นตารางไหม.csv")

NUM = re.compile(r"\d+(?:\.\d+)?")


def tokens_from(q):
    """ตัวเลขเฉพาะที่ 'ต้องมี' ถ้าเฉลยได้เห็นตาราง/รูปจริง"""
    out = []
    for t in (q.get("tables") or []):
        if not isinstance(t, dict):
            continue
        for row in (t.get("rows") or []):
            for cell in row:
                for m in NUM.findall(str(cell)):
                    out.append(m)
    spec = q.get("imageSpec")
    if isinstance(spec, dict):
        for cat in (spec.get("categories") or []):
            for seg in (cat.get("segments") or []):
                v = seg.get("label", seg.get("value"))
                for m in NUM.findall(str(v)):
                    out.append(m)
        for k in ("points", "values", "data", "bars"):
            v = spec.get(k)
            if isinstance(v, list):
                for m in NUM.findall(json.dumps(v, ensure_ascii=False)):
                    out.append(m)
    # เก็บเฉพาะเลขที่ "เฉพาะพอ" — ยาว ≥ 2 ตัวอักษร กันเลข 0-9 ที่เจอได้ทั่วไป
    uniq = []
    for t in out:
        if len(t) >= 2 and t not in uniq:
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
        meta[qid] = dict(
            setId=q.get("setId") or fn[:-5],
            kind="ตาราง" if q.get("tables") else "รูป",
            typ=q.get("type"),
            correct=q.get("correct"),
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

red = amber = green = 0
rows = []
for qid, (n, k, miss, given) in sorted(seen.items()):
    pct = (k * 100 // n) if n else 0
    flag = "🔴 ไม่เคยเห็น" if pct == 0 else ("🟠 น่าสงสัย" if pct < 50 else "🟢 น่าจะเห็น")
    if pct == 0:
        red += 1
    elif pct < 50:
        amber += 1
    else:
        green += 1
    m = meta[qid]
    rows.append([qid, m["setId"], m["kind"], m["typ"],
                 "" if m["correct"] is None else m["correct"],
                 n, k, "%d%%" % pct, flag, " ".join(miss), given])

print("-" * 68)
print("③ ผลพิสูจน์ (จาก %d ข้อ)" % len(seen))
print("   🔴 ไม่พบตัวเลขจากตาราง/รูปเลย        : %4d ข้อ  ⇒ เฉลยใช้ไม่ได้ ต้องทำใหม่" % red)
print("   🟠 พบบางส่วน (< 50%%)                 : %4d ข้อ  ⇒ ต้องดูด้วยตา" % amber)
print("   🟢 พบ ≥ 50%%                          : %4d ข้อ  ⇒ ผ่านชั้นนี้" % green)
print("   ⚪ ตารางไม่มีตัวเลข และ t1 ทำไปแล้ว   : %4d ข้อ  ⇒ ต้องดูด้วยตา (เช่น chap-02-logic-q99)" % len(nonum_hit))

if not os.path.isdir(OUTDIR):
    os.makedirs(OUTDIR)
with io.open(OUT, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "ชุด", "ชนิด", "type", "correct",
                "เลขที่ต้องมี", "เลขที่พบ", "ร้อยละ", "ธง",
                "ตัวอย่างเลขที่หาย", "given 120 ตัวอักษร"])
    w.writerows(rows)
print("-" * 68)
print("④ CSV: %s" % OUT)
print("   %d แถว · ส่งภาพผลรันนี้ให้ E พอ ⛔ ครูไม่ต้องเปิด CSV เอง" % len(rows))
print("=" * 68)

# -*- coding: utf-8 -*-
"""
ตรวจ: t1 ทำเฉลยข้อที่ "มีตาราง / มีรูป" ไปกี่ข้อ โดยที่ไม่เคยเห็นตารางหรือรูปนั้นเลย
(v1.0 · ครูรันเอง)
----------------------------------------------------------------------------
ที่มา : ครูจับได้ว่า chap-02-logic-q99 มีตารางอยู่ในคลังจริง ๆ (เห็นในหน้า viewer)
        แต่ t1 รายงานว่า "โจทย์อ้างตารางที่ไม่มี" ⇒ ตารางไม่ได้หายจากคลัง
        แต่ **หายตอนสร้าง POOL ส่งให้ t1** เพราะระเบียนที่ส่งมีแค่ 10 ช่อง
        (id · type · difficulty · hasImage · hint · topics · subTopics · correct · choices · question)
        ⛔ ไม่มีช่อง `tables` และ ⛔ ไม่มีช่อง `imageSpec`

สคริปต์นี้ตอบคำถามเดียว: **ของจริงมีกี่ข้อ**

วิธี (ออกแบบให้กินแรมน้อย ⛔ ไม่โหลด bank.json 37MB เข้าแรม)
  1) ไล่อ่าน data\\sets\\*.json ทีละไฟล์ → เก็บ id ที่มี `tables` หรือ `imageSpec`
  2) ไล่อ่าน _t1run\\results\\t1_MASTER.json แบบทีละก้อน (streaming) → เก็บ id ที่ t1 ทำไปแล้ว
  3) ตัดกัน → ออก CSV

ใช้งาน
    python "ตรวจ-t1-ข้อที่มีตารางหรือรูป-v1.0-ครูรันเอง.py"

⛔ อ่านอย่างเดียว ไม่เขียนทับไฟล์ใด · ⛔ ไม่ยุ่ง git · ผลออกที่ _t1run\\audit\\
"""
import csv, io, json, os, re, sys

ROOT   = os.path.dirname(os.path.abspath(__file__))
SETS   = os.path.join(ROOT, "data", "sets")
MASTER = os.path.join(ROOT, "_t1run", "results", "t1_MASTER.json")
OUTDIR = os.path.join(ROOT, "_t1run", "audit")
OUT    = os.path.join(OUTDIR, "audit_t1_ตารางหรือรูปไม่ถึงt1.csv")

ID_RE = re.compile(r'"((?:[a-z0-9]+-)+q\d+)"')

print("=" * 66)
print("ตรวจข้อที่มีตาราง/รูป แต่ t1 ไม่เคยเห็น")
print("=" * 66)

# ── 1) กวาดต้นฉบับ sets ───────────────────────────────────────────
if not os.path.isdir(SETS):
    sys.exit("⛔ ไม่เจอโฟลเดอร์ %s" % SETS)

info = {}          # id -> dict(has_tables, has_image, setId, type, correct, qhead)
n_files = 0
for fn in sorted(os.listdir(SETS)):
    if not fn.endswith(".json"):
        continue                      # ข้ามไฟล์สำรอง .bak-*
    p = os.path.join(SETS, fn)
    try:
        d = json.loads(open(p, "rb").read().decode("utf-8"))
    except Exception as e:
        print("  ⚠️ อ่านไม่ได้ %s : %s" % (fn, e))
        continue
    n_files += 1
    qs = d["questions"] if isinstance(d, dict) and "questions" in d else d
    for q in qs:
        if not isinstance(q, dict):
            continue
        ht = bool(q.get("tables"))
        hi = bool(q.get("imageSpec")) or bool(q.get("hasImage"))
        if not (ht or hi):
            continue
        qid = q.get("id")
        if not qid:
            continue
        head = (q.get("question") or "").replace("\n", " ")[:110]
        info[qid] = dict(
            setId=q.get("setId") or fn[:-5],
            typ=q.get("type"),
            tables="มี" if ht else "",
            image="มี" if hi else "",
            correct=q.get("correct"),
            head=head,
        )
print("① ไฟล์ต้นฉบับที่อ่าน: %d ไฟล์" % n_files)
print("   ข้อที่มี tables หรือ imageSpec/hasImage: %d ข้อ" % len(info))
n_tab = sum(1 for v in info.values() if v["tables"])
n_img = sum(1 for v in info.values() if v["image"])
print("     • มีตาราง (tables)      : %d" % n_tab)
print("     • มีรูป (imageSpec/hasImage): %d" % n_img)

# ── 2) กวาด t1_MASTER แบบ streaming ───────────────────────────────
if not os.path.exists(MASTER):
    sys.exit("⛔ ไม่เจอ %s" % MASTER)
done = set()
size = os.path.getsize(MASTER)
with open(MASTER, "rb") as f:
    tail = b""
    read = 0
    while True:
        chunk = f.read(4 * 1024 * 1024)
        if not chunk:
            break
        read += len(chunk)
        buf = (tail + chunk).decode("utf-8", "ignore")
        for m in ID_RE.finditer(buf):
            done.add(m.group(1))
        tail = chunk[-200:]
        sys.stdout.write("\r② อ่าน t1_MASTER.json ... %d%%" % (read * 100 // size))
        sys.stdout.flush()
print("\r② t1_MASTER.json: เจอ id ที่ t1 แตะแล้ว %d ข้อ            " % len(done))

# ── 3) ตัดกัน ─────────────────────────────────────────────────────
hit = sorted(qid for qid in info if qid in done)
print("-" * 66)
print("③ 🔴 ข้อที่ **มีตาราง/รูปในคลัง** และ **t1 ทำเฉลยไปแล้ว** = %d ข้อ" % len(hit))
print("   (เฉลยพวกนี้เขียนขึ้นโดยไม่เคยเห็นตาราง/รูป ⇒ ต้องตรวจซ้ำทุกข้อ)")
not_done = len(info) - len(hit)
print("   ข้อที่มีตาราง/รูปแต่ t1 ยังไม่แตะ = %d ข้อ (ปลอดภัย)" % not_done)

by_set = {}
for qid in hit:
    by_set[info[qid]["setId"]] = by_set.get(info[qid]["setId"], 0) + 1
print("-" * 66)
print("   แยกตามชุด (มากไปน้อย):")
for s, c in sorted(by_set.items(), key=lambda x: -x[1])[:20]:
    print("     %-28s %4d" % (s, c))

# ── 4) เขียน CSV ──────────────────────────────────────────────────
if not os.path.isdir(OUTDIR):
    os.makedirs(OUTDIR)
with io.open(OUT, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "ชุด", "ชนิด", "มีตาราง", "มีรูป", "correct", "หัวโจทย์ 110 ตัวอักษร"])
    for qid in hit:
        v = info[qid]
        w.writerow([qid, v["setId"], v["typ"], v["tables"], v["image"],
                    "" if v["correct"] is None else v["correct"], v["head"]])
print("-" * 66)
print("④ CSV: %s" % OUT)
print("   %d แถว · ส่งภาพผลรันนี้ให้ E พอ ⛔ ครูไม่ต้องเปิด CSV เอง" % len(hit))
print("=" * 66)

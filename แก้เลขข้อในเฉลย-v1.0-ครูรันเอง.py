# -*- coding: utf-8 -*-
"""
แก้ "เลขข้อ" ที่พิมพ์ผิดในบรรทัดคำตอบ   (v1.0 · ครูรันเอง)
===========================================================================
อาการ : ค่าคำตอบในเฉลย **ถูก** แต่เลขข้อที่พิมพ์กำกับ **ผิด**
        เด็กอ่านบรรทัดสุดท้ายแล้วไปฝนผิดข้อ
  • gen-chap-04-coord   พิมพ์ "ข้อ 1" ตายตัวทุกข้อ
  • gen-chap-02-logic   พิมพ์เลขแบบเริ่มที่ 0 ("ข้อ 0") ขณะที่หน้าเว็บนับ 1–4
  • gen-chap-05-function / gen-chap-03-real   เลขไม่ตรงทั้งฐาน 0 และฐาน 1
  (ตัวอย่างที่ครูจับได้เอง: gen-chap-03-real-q393 ติ๊กถูกข้อ 4 แต่เฉลยพิมพ์ "ข้อ 1")

สิ่งที่สคริปต์นี้ทำ  = เขียนตัวเลขนั้นใหม่เป็น `correct + 1` เท่านั้น
สิ่งที่สคริปต์นี้ ⛔ ไม่ทำ = ไม่แตะเนื้อเฉลย · ไม่แตะ correct · ไม่แตะโจทย์/ตัวเลือก

🔒 ด่านความปลอดภัย (ข้อไหนไม่ผ่าน = ข้าม แล้วรายงานให้ครูดูเอง)
   1. ต้องเป็น mc และ correct เป็นจำนวนเต็มในช่วงตัวเลือก
   2. ต้องมีบรรทัด «✅ คำตอบ» ชัดเจน
   3. **ค่าของตัวเลือกที่คลังเก็บ ต้องปรากฏในเนื้อเฉลย** (ยืนยันว่าคณิตศาสตร์ถูก)
   4. ในบรรทัดนั้นต้องมีรูปแบบ "ข้อ N / ตัวเลือก N" เพียงแห่งเดียว
   5. ถ้า ⛔ ไม่ผ่านข้อใด → ข้าม (เช่น chap-02-logic-q37 ที่เฉลยผิดจริง จะไม่ถูกแตะ)

⛔ ผ่าตัดข้อความแบบไบนารี — CRLF ไม่หาย · ไฟล์ไม่ถูก re-serialize · ขนาดขยับแค่หลักไบต์
⛔ ไม่ยุ่ง git · ไม่ลบไฟล์ · สำรอง .bak-เลขข้อ ก่อนเขียนเสมอ

ใช้งาน
    python "แก้เลขข้อในเฉลย-v1.0-ครูรันเอง.py"            ← ดูอย่างเดียว (dry-run)
    python "แก้เลขข้อในเฉลย-v1.0-ครูรันเอง.py" --apply    ← เขียนจริง
"""
import io, json, os, re, shutil, sys

ROOT  = os.path.dirname(os.path.abspath(__file__))
SETS  = os.path.join(ROOT, "data", "sets")
BANK  = os.path.join(ROOT, "data", "bank.json")
APPLY = "--apply" in sys.argv

TAG     = re.compile(r"<[^>]+>")
ANSLINE = re.compile(r"✅|คำตอบ\s*[:：]")
PICK    = re.compile(r"(ตัวเลือกที่|ตัวเลือก|ข้อที่|ข้อ)(\s*)(\d+)")


def norm(s):
    return re.sub(r"[\s\\$,]", "", TAG.sub("", str(s)))


def flat(x):
    if isinstance(x, str):
        return [x]
    if isinstance(x, list):
        r = []
        for i in x:
            r.extend(flat(i))
        return r
    return []


def plan_for(q):
    """คืน (ข้อความเก่า, ข้อความใหม่, เหตุผล) หรือ (None, None, เหตุผลที่ข้าม)"""
    if q.get("type") != "mc":
        return None, None, "ไม่ใช่ mc"
    c = q.get("correct")
    ch = q.get("choices") or []
    if not isinstance(c, int) or isinstance(c, bool) or not ch or c >= len(ch) or c < 0:
        return None, None, "correct ใช้ไม่ได้"
    items = q.get("explanation")
    if not isinstance(items, list):
        return None, None, "explanation ไม่ใช่ list"
    idxs = [i for i, e in enumerate(items) if isinstance(e, str) and ANSLINE.search(e)]
    if not idxs:
        return None, None, "ไม่มีบรรทัดคำตอบ"
    i = idxs[-1]
    line = items[i]
    ms = list(PICK.finditer(TAG.sub("", line)))
    if len(ms) != 1:
        return None, None, ("ไม่มีเลขข้อในบรรทัดคำตอบ" if not ms else "มีเลขข้อหลายแห่ง")
    said = int(ms[0].group(3))
    want = c + 1
    if said == want:
        return None, None, "เลขถูกอยู่แล้ว"
    # ด่าน 3 — ค่าของตัวเลือกที่คลังเก็บต้องอยู่ในเนื้อเฉลย
    blob = norm(" ".join(TAG.sub("", e) for e in flat(items)))
    tgt = norm(ch[c])
    ok = len(tgt) >= 3 and (tgt in blob or (len(tgt) > 6 and tgt[: int(len(tgt) * 0.75)] in blob))
    if not ok:
        return None, None, "⛔ ยืนยันค่าคำตอบในเฉลยไม่ได้ — ต้องให้ครูดูเอง"
    # แทนที่เฉพาะตัวเลขตัวนั้น โดยนับตำแหน่งบนข้อความจริง (ที่ยังมีแท็ก)
    hits = list(PICK.finditer(line))
    if len(hits) != 1:
        return None, None, "ตำแหน่งเลขข้อไม่ชัด"
    h = hits[0]
    new = line[: h.start(3)] + str(want) + line[h.end(3):]
    return line, new, "ข้อ %d → ข้อ %d" % (said, want)


def span_of_expl(raw, qid):
    needle = '"%s"' % qid
    if raw.count(needle) != 1:
        return None
    i = raw.find(needle)
    j = raw.find('"explanation"', i)
    if j < 0:
        return None
    k = raw.find("[", j)
    depth, p, ins, esc = 0, k, False, False
    while p < len(raw):
        ch = raw[p]
        if ins:
            if esc:      esc = False
            elif ch == "\\": esc = True
            elif ch == '"': ins = False
        else:
            if ch == '"': ins = True
            elif ch in "[{": depth += 1
            elif ch in "]}":
                depth -= 1
                if depth == 0:
                    return k, p + 1
        p += 1
    return None


def apply_edits(path, plans, label):
    """plans = [(qid, old, new)] — ผ่าตัดทีละจุดแล้วเขียนครั้งเดียว"""
    if not os.path.exists(path):
        print("  ⛔ ไม่เจอไฟล์: %s" % path)
        return 0
    raw = open(path, "rb").read().decode("utf-8")
    crlf_before = raw.count("\r\n")
    edits, miss = [], []
    for qid, old, new in plans:
        sp = span_of_expl(raw, qid)
        if not sp:
            miss.append((qid, "หา explanation ไม่เจอ/ id ซ้ำ"))
            continue
        a, b = sp
        enc_old = json.dumps(old, ensure_ascii=False)
        seg = raw[a:b]
        if seg.count(enc_old) != 1:
            miss.append((qid, "หาบรรทัดคำตอบในไฟล์ไม่เจอ (%d ครั้ง)" % seg.count(enc_old)))
            continue
        off = a + seg.find(enc_old)
        edits.append((off, off + len(enc_old), json.dumps(new, ensure_ascii=False)))
    edits.sort()
    print("  %s : แก้ได้ %d จุด · ข้าม %d" % (label, len(edits), len(miss)))
    for qid, why in miss[:8]:
        print("      ⚠️ %s — %s" % (qid, why))
    if not APPLY or not edits:
        return len(edits)
    bak = path + ".bak-เลขข้อ"
    if not os.path.exists(bak):
        shutil.copy2(path, bak)
    out, prev = [], 0
    for a, b, t in edits:
        out.append(raw[prev:a]); out.append(t); prev = b
    out.append(raw[prev:])
    res = "".join(out)
    before = os.path.getsize(path)
    with open(path, "wb") as f:
        f.write(res.encode("utf-8"))
    after = os.path.getsize(path)
    print("      ✅ เขียนแล้ว %d → %d (%+d ไบต์) · CRLF %d → %d %s"
          % (before, after, after - before, crlf_before, res.count("\r\n"),
             "✅" if crlf_before == res.count("\r\n") else "⛔ ผิดปกติ"))
    return len(edits)


print("=" * 72)
print("แก้เลขข้อในบรรทัดคำตอบ  %s" % ("(เขียนจริง)" if APPLY else "(dry-run — ยังไม่เขียน)"))
print("=" * 72)

allplans, skipped = {}, []
nq = 0
for fn in sorted(os.listdir(SETS)):
    if not fn.endswith(".json"):
        continue
    d = json.loads(open(os.path.join(SETS, fn), "rb").read().decode("utf-8"))
    qs = d["questions"] if isinstance(d, dict) and "questions" in d else d
    plans = []
    for q in qs:
        if not isinstance(q, dict):
            continue
        nq += 1
        old, new, why = plan_for(q)
        if old is None:
            if why.startswith("⛔"):
                skipped.append((q.get("id"), why))
            continue
        plans.append((q["id"], old, new))
    if plans:
        allplans[fn] = plans

total = sum(len(v) for v in allplans.values())
print("⬤ อ่านคลัง %d ข้อ · เจอข้อที่ต้องแก้เลข %d ข้อ" % (nq, total))
for fn, v in sorted(allplans.items(), key=lambda x: -len(x[1])):
    print("     %-30s %3d" % (fn[:-5], len(v)))
if skipped:
    print("-" * 72)
    print("🔔 ข้ามให้ครูดูเอง %d ข้อ (ยืนยันค่าคำตอบไม่ได้):" % len(skipped))
    for qid, why in skipped:
        print("     %s" % qid)

print("-" * 72)
print("1) data\\sets\\*.json")
for fn, v in sorted(allplans.items()):
    apply_edits(os.path.join(SETS, fn), v, "sets\\" + fn)
print("-" * 72)
print("2) data\\bank.json")
flatplans = [p for v in allplans.values() for p in v]
apply_edits(BANK, flatplans, "bank.json")

if APPLY:
    print("-" * 72)
    print("=== ตรวจซ้ำ ===")
    bad = 0
    for fn, v in allplans.items():
        d = json.loads(open(os.path.join(SETS, fn), "rb").read().decode("utf-8"))
        qs = {q["id"]: q for q in (d["questions"] if isinstance(d, dict) else d)}
        for qid, old, new in v:
            o, n, why = plan_for(qs[qid])
            if o is not None:
                bad += 1
                print("   ⛔ %s ยังไม่ถูก (%s)" % (qid, why))
    print("   ข้อที่ยังเหลือปัญหา: %d (ต้องเป็น 0)" % bad)
    if os.path.exists(BANK):
        d = json.loads(open(BANK, "rb").read().decode("utf-8"))
        qs = d["questions"] if isinstance(d, dict) and "questions" in d else d
        print("   จำนวนข้อใน bank.json: %d" % len(qs))
    print("-" * 72)
    print("⛔ สคริปต์นี้ไม่ได้แตะ git — ครู commit เองเมื่อพร้อม")
else:
    print("-" * 72)
    print("ถ้าถูกต้องแล้ว สั่งซ้ำด้วย --apply เพื่อเขียนจริง")
print("=" * 72)

# -*- coding: utf-8 -*-
"""
แก้ธง flawedSource ให้ตรงสเปกของด่าน 9   (v1.0 · ครูรันเอง)
============================================================================
🪞 E ยอมรับ: E เขียน "flawedSource": true (bool) ทั้ง 4 ข้อ
   แต่ repo บังคับให้เป็น **วัตถุ (dict) 4 ช่อง** — ด่าน 9 เตือนมาตั้งแต่
   commit เมื่อคืน (405f434) แต่ไม่มีใครในเลนเปิดดู GitHub Actions เลย

สเปกที่ด่าน 9 ระบุ (จากล็อกของด่านเอง):
   "flawedSource": {
     "kind":      หนึ่งใน multiple-correct · no-correct · ambiguous · outdated-fact
     "note":      ปัญหาของข้อนี้คืออะไร            ⛔ ห้ามขาด
     "evidence":  ที่มาที่ตรวจย้อนได้               ⛔ ห้ามว่าง ห้ามสั้น ห้ามเป็นขีดกลาง
     "decidedAt": "YYYY-MM-DD · ชื่อคนตัดสิน"      ⛔ ต้องเป็น ค.ศ. และต้องมีคนตัดสิน
   }

ทั้ง 4 ข้อเป็น kind = "no-correct" (ไม่มีตัวเลือก/คำตอบใดถูก)

⛔ ผ่าตัดข้อความแบบไบนารี · ⛔ ไม่แตะเนื้ออื่น · ⛔ ไม่ยุ่ง git
สำรอง .bak-ธงdict ก่อนเขียนเสมอ · แก้ทั้ง data\\sets และ data\\bank.json

ใช้งาน
    python "แก้ธงflawedSource-ให้ตรงสเปกด่าน9-v1.0-ครูรันเอง.py"           ← ดู + อ่านเนื้อธง
    python "แก้ธงflawedSource-ให้ตรงสเปกด่าน9-v1.0-ครูรันเอง.py" --apply
"""
import json, os, shutil, sys

ROOT  = os.path.dirname(os.path.abspath(__file__))
SETS  = os.path.join(ROOT, "data", "sets")
BANK  = os.path.join(ROOT, "data", "bank.json")
APPLY = "--apply" in sys.argv

FLAGS = {
"pat1-2555-10-q15": ("pat1-2555-10.json", {
  "kind": "no-correct",
  "note": "โจทย์กำหนดผลคูณจุดเกินขอบเขตที่เวกเตอร์ขนาดนั้นเป็นไปได้ ⇒ ไม่มีเวกเตอร์คู่ใดสอดคล้องกับเงื่อนไข จึงไม่มีคำตอบ",
  "evidence": "ใบเคาะครู 10 ก.ย. 2569 · อสมการโคชี–ชวาร์ซ |u·v| ≤ |u||v| = 4 × √2 ≈ 5.657 แต่โจทย์กำหนด u·v = −6 ซึ่งเกินขอบเขต ⇒ โคไซน์ระหว่างเวกเตอร์ ≈ −1.06 เป็นไปไม่ได้",
  "decidedAt": "2026-09-10 · ครู QC",
}),
"pat1-2552-10-q17": ("pat1-2552-10.json", {
  "kind": "no-correct",
  "note": "คำตอบที่ถูกต้องตามโจทย์ไม่ปรากฏในตัวเลือกใดเลย",
  "evidence": "เฉลยทางการระบุว่า «ตอบ ไม่มีข้อถูก» · P(E) = (C(9,4) + C(3,1)·C(9,3)) / C(12,4) = (126 + 252)/495 = 378/495 = 42/55 ซึ่งไม่ตรงกับตัวเลือกทั้งสี่ (1/3 · 1/4 · 14/99 · 14/55) · E คำนวณอิสระได้เลขเดียวกับเฉลยทางการ 12 ก.ย. 2569",
  "decidedAt": "2026-09-12 · ครู QC",
}),
"pat1-2558-10-q37": ("pat1-2558-10.json", {
  "kind": "no-correct",
  "note": "เงื่อนไขในโจทย์ขัดแย้งกันเอง ⇒ ไม่มีลำดับเลขคณิตใดสอดคล้องได้ทั้งหมด",
  "evidence": "เฉลยทางการระบุว่า «โจทย์ผิด» · ผลบวกพจน์คู่ − ผลบวกพจน์คี่ = 25d = 0 ⇒ d = 0 ⇒ ทุกพจน์เท่ากัน · ถ้ายึด a100 = 200 ผลบวกพจน์คี่จะเป็น 5000 ซึ่งขัดกับ 1275 ที่โจทย์กำหนด · E ยืนยันความขัดแย้งเดียวกันด้วยเส้นทางคำนวณอิสระ 12 ก.ย. 2569",
  "decidedAt": "2026-09-12 · ครู QC",
}),
"chap-14-infiniteseries-q43": ("chap-14-infiniteseries.json", {
  "kind": "no-correct",
  "note": "ปริพันธ์ที่ใช้นิยาม a_n ลู่ออกทุกค่า n ⇒ นิยาม a_n ไม่ได้ ⇒ อนุกรมในโจทย์ไม่นิยาม จึงไม่มีตัวเลือกใดถูก",
  "evidence": "E ตรวจ 12 ก.ย. 2569 · a_n = ปริพันธ์ของ x^(−2n) จาก 0 ถึง 2 เป็นปริพันธ์ไม่ตรงแบบที่ปลายล่าง และเลขชี้กำลัง 2n ≥ 2 > 1 ⇒ ลิมิตเมื่อ x→0+ ไม่มีค่า · เฉลยทางการ Entrance 2538 ให้ 2/3 ซึ่งได้จากการถือว่า F(0) = 0 ทั้งที่ F(0) ไม่มีค่า · notes เดิมของคลังบันทึกให้ยึดเฉลยทางการ ครูเคาะใหม่ 12 ก.ย. 2569 ให้ยึดความถูกต้องทางคณิตศาสตร์",
  "decidedAt": "2026-09-12 · ครู QC",
}),
}

OLD = '"flawedSource": true,'


def step_of(raw):
    """ระยะย่อหน้าต่อชั้นของไฟล์นี้ (นับจาก explanation กับชิ้นแรกในนั้น)"""
    j = raw.find('"explanation"')
    if j < 0:
        return 2
    ls = raw.rfind("\n", 0, j) + 1
    key_ind = len(raw[ls:j]) - len(raw[ls:j].lstrip(" "))
    key_ind = j - ls
    k = raw.find("[", j)
    n = raw.find("\n", k)
    p, item_ind = n + 1, 0
    while p < len(raw) and raw[p] == " ":
        item_ind += 1
        p += 1
    d = item_ind - key_ind
    return d if 1 <= d <= 8 else 2


def render(obj, ind, step, nl):
    pad, pad2 = " " * ind, " " * (ind + step)
    lines = ['"flawedSource": {']
    keys = ["kind", "note", "evidence", "decidedAt"]
    for i, k in enumerate(keys):
        comma = "," if i < len(keys) - 1 else ""
        lines.append(pad2 + json.dumps(k, ensure_ascii=False) + ": "
                     + json.dumps(obj[k], ensure_ascii=False) + comma)
    lines.append(pad + "},")
    return (nl + pad).join([lines[0]]) + nl + (nl).join(lines[1:])


def run(path, label):
    if not os.path.exists(path):
        print("  ⛔ ไม่เจอไฟล์: %s" % label)
        return
    raw = open(path, "rb").read().decode("utf-8")
    crlf0 = raw.count("\r\n")
    nl = "\r\n" if crlf0 else "\n"
    step = step_of(raw)
    edits = []
    print("  %s   (ย่อหน้าต่อชั้น = %d)" % (label, step))
    for qid, (fn, obj) in FLAGS.items():
        if os.path.basename(path) not in (fn, "bank.json"):
            continue
        key = '"%s"' % qid
        if raw.count(key) != 1:
            continue
        i = raw.find(key)
        # หา "flawedSource": true, ที่อยู่ในข้อนี้ (ภายใน 4000 อักขระถัดไป)
        j = raw.find(OLD, i, i + 4000)
        if j < 0:
            if '"flawedSource": {' in raw[i:i + 4000]:
                print("     %-28s ⏭ เป็น dict อยู่แล้ว" % qid)
            else:
                print("     %-28s ⛔ หาธงไม่เจอ" % qid)
            continue
        ls = raw.rfind("\n", 0, j) + 1
        ind = j - ls
        edits.append((j, j + len(OLD), render(obj, ind, step, nl)))
        print("     %-28s · true → dict 4 ช่อง" % qid)
    if not edits:
        print("     (ไม่มีอะไรต้องแก้)")
        return
    if not APPLY:
        print("     (dry-run — %d จุด ยังไม่เขียน)" % len(edits))
        return
    bak = path + ".bak-ธงdict"
    if not os.path.exists(bak):
        shutil.copy2(path, bak)
    edits.sort()
    out, prev = [], 0
    for s, e, t in edits:
        out.append(raw[prev:s]); out.append(t); prev = e
    out.append(raw[prev:])
    res = "".join(out)
    before = os.path.getsize(path)
    open(path, "wb").write(res.encode("utf-8"))
    after = os.path.getsize(path)
    # ⚠️ สคริปต์นี้ "เพิ่มบรรทัด" ⇒ จำนวน CRLF ต้องโตขึ้นตามบรรทัดที่เพิ่ม (ไม่ใช่คงที่)
    # ด่านที่ถูกต้องคือ: ต้องไม่มี \r เดี่ยว ๆ ที่ไม่ได้คู่กับ \n
    lone0 = raw.count("\r") - crlf0
    lone1 = res.count("\r") - res.count("\r\n")
    print("     ✅ เขียนแล้ว %d → %d (%+d) · บรรทัด %d → %d · \\r เดี่ยว %d → %d %s"
          % (before, after, after - before,
             raw.count("\n"), res.count("\n"), lone0, lone1,
             "✅" if lone1 == lone0 == 0 else "⛔"))


print("=" * 78)
print("แก้ธง flawedSource ให้เป็นวัตถุตามสเปกด่าน 9  %s"
      % ("(เขียนจริง)" if APPLY else "(dry-run)"))
print("=" * 78)
if not APPLY:
    print("📖 เนื้อธงที่จะเขียน — ครูอ่านก่อนสั่ง --apply")
    for qid, (_, o) in FLAGS.items():
        print("-" * 78)
        print("  %s" % qid)
        for k in ("kind", "note", "evidence", "decidedAt"):
            print("    %-10s %s" % (k, o[k]))
    print("=" * 78)

for fn in sorted(set(f for f, _ in FLAGS.values())):
    run(os.path.join(SETS, fn), "data\\sets\\" + fn)
print("-" * 78)
run(BANK, "data\\bank.json")

if APPLY:
    print("-" * 78)
    print("=== ตรวจซ้ำ ===")
    for fn in sorted(set(f for f, _ in FLAGS.values())) + ["bank.json"]:
        p = BANK if fn == "bank.json" else os.path.join(SETS, fn)
        if not os.path.exists(p):
            continue
        d = json.loads(open(p, "rb").read().decode("utf-8"))
        qs = d["questions"] if isinstance(d, dict) and "questions" in d else d
        idx = {q["id"]: q for q in qs if isinstance(q, dict)}
        print("  %s · %d ข้อ" % (fn, len(qs)))
        for qid in FLAGS:
            if qid in idx:
                fsrc = idx[qid].get("flawedSource")
                ok = isinstance(fsrc, dict) and set(fsrc) == {"kind", "note", "evidence", "decidedAt"}
                print("     %-28s %s · kind=%s · evidence %d ตัวอักษร"
                      % (qid, "✅ dict ครบ 4 ช่อง" if ok else "⛔ ยังไม่ถูก",
                         (fsrc or {}).get("kind"), len((fsrc or {}).get("evidence") or "")))
    print("-" * 78)
    print("⛔ สคริปต์นี้ไม่ได้แตะ git — ครู commit เองเมื่อพร้อม")
else:
    print("-" * 78)
    print("ถ้าเนื้อธงถูกต้องแล้ว สั่งซ้ำด้วย --apply")
print("=" * 78)

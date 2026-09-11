# -*- coding: utf-8 -*-
"""
ติดธงข้อสอบบกพร่อง 3 ข้อ (มติครู 12 ก.ย. 69)   (v1.0 · ครูรันเอง)
==========================================================================
① pat1-2552-10-q17   หลอดไฟ 12 หลอด ชำรุด 3 หยิบ 4 · P(ชำรุดไม่เกิน 1)
     คำตอบจริง 378/495 = 42/55 ⛔ ไม่มีในตัวเลือกใดเลย
     ⬤ เฉลยทางการ: "ตอบ ไม่มีข้อถูก"  ⇒ ติด flawedSource
     (correct = null อยู่แล้ว · เฉลยในคลังเขียนไว้ถูกแล้ว ⇒ ⛔ ไม่แตะเฉลย)

② pat1-2558-10-q37   ลำดับเลขคณิต ผลบวกคี่ = ผลบวกคู่ = 1275 และ a100 = 200
     25d = 0 ⇒ d = 0 ⇒ ทุกพจน์เท่ากัน ⇒ ขัดกับเงื่อนไข
     ⬤ เฉลยทางการ: "โจทย์ผิด"  ⇒ ติด flawedSource
     (correct = null อยู่แล้ว · เฉลยในคลังเขียนไว้ถูกแล้ว ⇒ ⛔ ไม่แตะเฉลย)

③ chap-14-infiniteseries-q43   a_n = ∫₀² x^(-2n) dx
     ที่ x→0⁺ ได้ x^(-2n) → ∞ และ 2n ≥ 2 > 1 ⇒ ปริพันธ์ลู่ออกทุก n ⇒ a_n ไม่มีค่า
     ⚠️ ข้อนี้ต่างจาก 2 ข้อบน: **เฉลยทางการ Entrance 2538 ให้ 2/3**
        และคลังเคยบันทึกใน notes ว่าให้ยึดเฉลยทางการ (ดู REVIEW-LOG)
     ⚖️ ครูเคาะใหม่ 12 ก.ย. 69 = ยึดความถูกต้องทางคณิตศาสตร์ ⇒ ทำ 3 อย่าง:
        flawedSource: true · correct 1 → null · วางเฉลยใหม่ (อธิบายทั้งการลู่ออก
        และที่มาของ 2/3) · notes เดิมเก็บไว้ครบ + ต่อท้ายด้วยมติใหม่

⛔ ผ่าตัดข้อความแบบไบนารี — ขึ้นบรรทัดเดิมของแต่ละไฟล์ไม่ขยับ · ⛔ ไม่ re-serialize
⛔ ไม่ยุ่ง git · ⛔ ไม่ลบไฟล์ · สำรอง .bak-ธงบกพร่อง ก่อนเขียนเสมอ
แก้ทั้ง data\\bank.json และ data\\sets\\*.json ให้ตรงกัน

ใช้งาน
    python "ติดธงข้อสอบบกพร่อง-3ข้อ-v1.0-ครูรันเอง.py"           ← ดูอย่างเดียว
    python "ติดธงข้อสอบบกพร่อง-3ข้อ-v1.0-ครูรันเอง.py" --apply   ← เขียนจริง
"""
import io, json, os, shutil, sys

ROOT  = os.path.dirname(os.path.abspath(__file__))
SETS  = os.path.join(ROOT, "data", "sets")
BANK  = os.path.join(ROOT, "data", "bank.json")
APPLY = "--apply" in sys.argv

Q43 = "chap-14-infiniteseries-q43"
TARGETS = [
    ("pat1-2552-10-q17",  "pat1-2552-10.json"),
    ("pat1-2558-10-q37",  "pat1-2558-10.json"),
    (Q43,                 "chap-14-infiniteseries.json"),
]

NEW_EXPL_Q43 = [
"<b>📐 ความรู้พื้นฐาน</b>",
"<b>ปริพันธ์ไม่ตรงแบบ (improper integral)</b> ถ้าฟังก์ชันระเบิดที่ปลายช่วง ⛔ แทนค่าปลายตรง ๆ ไม่ได้ ต้องคิดเป็นลิมิต",
"$\\displaystyle\\int_{0}^{b}x^{-p}\\,dx$ <b>ลู่เข้า</b> ก็ต่อเมื่อ $p<1$ เท่านั้น",
"สูตรปริพันธ์กำลัง: $\\displaystyle\\int x^{p}\\,dx=\\dfrac{x^{p+1}}{p+1}+C$ (เมื่อ $p\\neq -1$)",
"ผลบวกอนุกรมเรขาคณิตอนันต์: $\\displaystyle\\sum_{n=1}^{\\infty}ar^{n-1}=\\dfrac{a}{1-r}$ เมื่อ $|r|<1$",
"",
"<b>🎯 เป้าหมาย</b> ตรวจก่อนว่า $a_n$ <b>มีค่าจริงหรือไม่</b> แล้วจึงค่อยหาผลบวกอนุกรม",
"",
"<b>【 ขั้นที่ 1 ▸ ตรวจว่า $a_n$ หาค่าได้ไหม 】</b>",
"$a_n=\\displaystyle\\int_{0}^{2}x^{-2n}\\,dx$ เมื่อ $n$ เป็นจำนวนเต็มบวก ⇒ เลขชี้กำลัง $-2n\\le -2$",
"ที่ $x\\to 0^{+}$ ได้ $x^{-2n}\\to +\\infty$ ⇒ เป็น<b>ปริพันธ์ไม่ตรงแบบที่ปลายล่าง</b>",
"ต้องคิดเป็นลิมิต: $\\displaystyle\\lim_{t\\to 0^{+}}\\int_{t}^{2}x^{-2n}\\,dx=\\lim_{t\\to 0^{+}}\\dfrac{2^{\\,1-2n}-t^{\\,1-2n}}{1-2n}$",
"เพราะ $1-2n<0$ จึงได้ $t^{\\,1-2n}\\to +\\infty$ เมื่อ $t\\to 0^{+}$",
"⇒ <b>ลิมิตไม่มีค่า ⇒ $a_n$ ลู่ออกทุก $n$</b> ⇒ อนุกรม $\\displaystyle\\sum_{n=1}^{\\infty}(1-2n)a_n$ จึง<b>ไม่นิยาม</b>",
"",
"<b>✅ คำตอบ: ไม่มีคำตอบ — โจทย์ข้อนี้บกพร่อง</b> (⚖️ มติครู 12 ก.ย. 69)",
"",
"<b>【 ขั้นที่ 2 ▸ แล้ว $\\dfrac{2}{3}$ ในเฉลยทางการมาจากไหน 】</b>",
"ถ้า <b>ข้าม</b> การตรวจปลายล่าง แล้วแทนค่าตรง ๆ โดยถือว่า $F(0)=0$ จะได้",
"$a_n \\approx \\dfrac{2^{\\,1-2n}}{1-2n}$ ⇒ $(1-2n)a_n=2^{\\,1-2n}=2\\cdot 4^{-n}$",
"$\\displaystyle\\sum_{n=1}^{\\infty}2\\cdot 4^{-n}=2\\cdot\\dfrac{\\frac{1}{4}}{1-\\frac{1}{4}}=2\\cdot\\dfrac{1}{3}=\\dfrac{2}{3}$",
"⇒ นี่คือที่มาของตัวเลือก 2 — ⛔ แต่ขั้นตอน “ถือว่า $F(0)=0$” ใช้ไม่ได้ เพราะ $F(0)$ <b>ไม่มีค่า</b>",
"",
"<b>🪞 บันทึกการตัดสิน</b> เฉลยทางการ Entrance 2538 ให้ $\\dfrac{2}{3}$ · คลังเคยบันทึกไว้ให้ยึดเฉลยทางการ · ⚖️ ครูเคาะใหม่ 12 ก.ย. 69 ให้ยึดความถูกต้องทางคณิตศาสตร์ ⇒ ติดธง <b>flawedSource</b>",
"",
"<b>💡 เทคนิคที่ใช้</b> เจอ $\\displaystyle\\int_{0}^{b}x^{-p}\\,dx$ ให้ดูเลขชี้กำลังก่อนเสมอ — $p\\ge 1$ เมื่อไร ปริพันธ์ลู่ออกทันที",
"",
"<b>⚠️ จุดที่เด็กมักผิด</b> แทนขอบล่าง $x=0$ ลงในสูตร $\\dfrac{x^{\\,1-2n}}{1-2n}$ แล้วได้ $0$ ทั้งที่ $0$ ยกกำลังจำนวนลบ<b>ไม่มีค่า</b>",
]

NOTE_ADD = " | ⚖️ มติครู 12 ก.ย. 69: ยึดความถูกต้องทางคณิตศาสตร์ — ปริพันธ์ลู่ออกทุก n ⇒ ติด flawedSource, correct=null, วางเฉลยใหม่ (ที่มาของ 2/3 อธิบายไว้ในเฉลยแล้ว)"


def obj_span(raw, qid):
    """ช่วง { ... } ของข้อ qid"""
    needle = '"%s"' % qid
    if raw.count(needle) != 1:
        raise RuntimeError("เจอ %s %d ครั้ง (ต้องเป็น 1)" % (needle, raw.count(needle)))
    i = raw.find(needle)
    s = raw.rfind("{", max(0, i - 400), i)
    if s < 0:
        raise RuntimeError("หา { เปิดข้อไม่เจอ")
    depth, p, ins, esc = 0, s, False, False
    while p < len(raw):
        c = raw[p]
        if ins:
            if esc:      esc = False
            elif c == "\\": esc = True
            elif c == '"': ins = False
        else:
            if c == '"': ins = True
            elif c in "[{": depth += 1
            elif c in "]}":
                depth -= 1
                if depth == 0:
                    return s, p + 1
        p += 1
    raise RuntimeError("หา } ปิดข้อไม่เจอ")


def expl_span(raw, a, b):
    j = raw.find('"explanation"', a, b)
    if j < 0:
        raise RuntimeError("ไม่เจอ explanation")
    k = raw.find("[", j)
    depth, p, ins, esc = 0, k, False, False
    while p < b:
        c = raw[p]
        if ins:
            if esc:      esc = False
            elif c == "\\": esc = True
            elif c == '"': ins = False
        else:
            if c == '"': ins = True
            elif c in "[{": depth += 1
            elif c in "]}":
                depth -= 1
                if depth == 0:
                    return k, p + 1
        p += 1
    raise RuntimeError("หา ] ปิด explanation ไม่เจอ")


def render(old, items):
    ascii_only = all(ord(c) < 128 for c in old)
    nl = "\r\n" if "\r\n" in old else "\n"
    body = old[1:]
    n = body.find("\n")
    if n < 0:
        return json.dumps(items, ensure_ascii=ascii_only)
    ind, p = "", n + 1
    while p < len(body) and body[p] == " ":
        ind += " "
        p += 1
    tail = old[:-1].rstrip(" ")
    close = old[len(tail):-1]
    parts = [json.dumps(s, ensure_ascii=ascii_only) for s in items]
    return "[" + nl + ("," + nl).join(ind + x for x in parts) + nl + close + "]"


def plan(raw, qid):
    """คืน list ของ (start, end, newtext, คำอธิบาย)"""
    a, b = obj_span(raw, qid)
    seg = raw[a:b]
    out = []
    # ── 1) flawedSource
    if '"flawedSource"' in seg:
        out.append(("SKIP", "มี flawedSource อยู่แล้ว"))
    else:
        idkey = '"%s"' % qid
        ipos = a + seg.find(idkey)
        eol = raw.find("\n", ipos)
        line_start = raw.rfind("\n", a, ipos) + 1
        indent = ""
        for ch in raw[line_start:ipos]:
            if ch == " ":
                indent += " "
            else:
                break
        nl = "\r\n" if raw[eol - 1:eol + 1] == "\r\n" or raw[max(0, eol - 1)] == "\r" else "\n"
        ins = ('\r\n' if raw[eol-1] == '\r' else '\n') + indent + '"flawedSource": true,'
        out.append((eol if raw[eol-1] != '\r' else eol - 1, eol if raw[eol-1] != '\r' else eol - 1,
                    ins, 'เติม "flawedSource": true'))
    # ── 2) เฉพาะ q43
    if qid == Q43:
        old_c = '"correct": 1,'
        if seg.count(old_c) == 1:
            p0 = a + seg.find(old_c)
            out.append((p0, p0 + len(old_c), '"correct": null,', 'correct 1 → null'))
        elif '"correct": null,' in seg:
            out.append(("SKIP", "correct = null อยู่แล้ว"))
        else:
            raise RuntimeError("หา correct ของ q43 ไม่เจอ/ไม่ชัด")
        k0, k1 = expl_span(raw, a, b)
        old_e = raw[k0:k1]
        n_old = len(json.loads(old_e))
        out.append((k0, k1, render(old_e, NEW_EXPL_Q43),
                    "เฉลย %d → %d ชิ้น" % (n_old, len(NEW_EXPL_Q43))))
        q = json.loads(raw[a:b])
        nt = q.get("notes")
        if isinstance(nt, str) and NOTE_ADD.strip()[:20] not in nt:
            enc_old = json.dumps(nt, ensure_ascii=False)
            if seg.count(enc_old) == 1:
                p0 = a + seg.find(enc_old)
                out.append((p0, p0 + len(enc_old),
                            json.dumps(nt + NOTE_ADD, ensure_ascii=False), "ต่อท้าย notes (เก็บของเดิมครบ)"))
    return out


def run(path, label):
    if not os.path.exists(path):
        print("  ⛔ ไม่เจอไฟล์: %s" % label)
        return
    raw = open(path, "rb").read().decode("utf-8")
    crlf0 = raw.count("\r\n")
    edits = []
    print("  %s" % label)
    for qid, fn in TARGETS:
        if fn not in os.path.basename(path) and os.path.basename(path) != "bank.json":
            continue
        if '"%s"' % qid not in raw:
            continue
        for e in plan(raw, qid):
            if e[0] == "SKIP":
                print("     %-28s ⏭ %s" % (qid, e[1]))
            else:
                print("     %-28s · %s" % (qid, e[3]))
                edits.append(e[:3])
    if not edits:
        print("     (ไม่มีอะไรต้องแก้)")
        return
    if not APPLY:
        print("     (dry-run — %d จุด ยังไม่เขียน)" % len(edits))
        return
    bak = path + ".bak-ธงบกพร่อง"
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
    print("     ✅ เขียนแล้ว %d → %d (%+d ไบต์) · CRLF %d → %d %s"
          % (before, after, after - before, crlf0, res.count("\r\n"),
             "✅" if crlf0 == res.count("\r\n") else "⛔"))


print("=" * 74)
print("ติดธงข้อสอบบกพร่อง 3 ข้อ  %s" % ("(เขียนจริง)" if APPLY else "(dry-run)"))
print("=" * 74)
files = sorted(set(fn for _, fn in TARGETS))
for fn in files:
    run(os.path.join(SETS, fn), "data\\sets\\" + fn)
print("-" * 74)
run(BANK, "data\\bank.json")

if APPLY:
    print("-" * 74)
    print("=== ตรวจซ้ำ ===")
    for fn in files + ["bank.json"]:
        p = BANK if fn == "bank.json" else os.path.join(SETS, fn)
        if not os.path.exists(p):
            continue
        d = json.loads(open(p, "rb").read().decode("utf-8"))
        qs = d["questions"] if isinstance(d, dict) and "questions" in d else d
        idx = {q["id"]: q for q in qs if isinstance(q, dict)}
        print("  %s · %d ข้อ" % (fn, len(qs)))
        for qid, _ in TARGETS:
            if qid in idx:
                q = idx[qid]
                extra = ""
                if qid == Q43:
                    extra = " · ชิ้นเฉลย %d · notes %d ตัวอักษร" % (len(q["explanation"]), len(q.get("notes") or ""))
                print("     %-28s flawedSource=%s · correct=%r%s"
                      % (qid, q.get("flawedSource"), q.get("correct"), extra))
    print("-" * 74)
    print("⛔ สคริปต์นี้ไม่ได้แตะ git — ครู commit เองเมื่อพร้อม")
else:
    print("-" * 74)
    print("ถ้าถูกต้องแล้ว สั่งซ้ำด้วย --apply เพื่อเขียนจริง")
print("=" * 74)

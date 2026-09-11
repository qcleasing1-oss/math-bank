# -*- coding: utf-8 -*-
"""
fix-declare-choice-gen07.py  ·  v1.0  ·  ครูรันเอง
=================================================
เติม " → <b>ตัวเลือก N</b>" ต่อท้ายบรรทัด "✅ คำตอบ" (รูปแบบเดียวกับข้ออื่นในไฟล์เดียวกัน)
ให้ข้อ gen-chap-07-trigonometry-q185..q244 (60 ข้อ)

ทำไม: ด่าน 7 (scripts/check_answer_claim.py) อ่านเลขตัวเลือกจากบรรทัดคำตอบ
      ด้วย CHOICE_RE = r'ตัวเลือก\\s*(\\d+)'   60 ข้อนี้ไม่มีเลข ⇒ "ไม่ประกาศ"
      ⇒ หนี้ 1,424 → 1,484 (+60)  ⇒ ด่าน 7/8 แดง

⛔ ไม่แตะ git   ⛔ ไม่ลบ/ไม่ย้าย/ไม่ rename ไฟล์ใด
⛔ ปริยาย = ซ้อมเปล่า (dry-run) · ต้องใส่ --apply ถึงจะเขียนจริง
✅ สำรองอัตโนมัติเป็น .bak-declare60 ก่อนเขียน

ใช้:  cd A:\\โปรเจคสอนคณิตศาสตร์\\math-bank
      python fix-declare-choice-gen07.py            (ซ้อมเปล่า)
      python fix-declare-choice-gen07.py --apply    (เขียนจริง)
"""
import os, sys, json, re, shutil

APPLY = "--apply" in sys.argv
FILES = [os.path.join("data", "sets", "gen-chap-07-trigonometry.json"),
         os.path.join("data", "bank.json")]

ANSWER_MARKERS     = ('✅', 'คำตอบ:', 'คำตอบคือ', 'จึงตอบ', 'ดังนั้นตอบ')
DISTRACTOR_MARKERS = ('จุดพลาด', 'เผลอ', 'ตัวลวง', 'มักตอบ',
                      'หากตอบ', 'ถ้าตอบ', 'ผิดตรง', 'ดักไว้')
CHOICE_RE = re.compile(r'ตัวเลือก\s*(\d+)')


def declared(expl):
    """คัดลอกตรรกะของด่าน 7 มาทั้งดุ้น ⛔ ห้ามเดา"""
    nums = set()
    for line in expl:
        if not isinstance(line, str):
            continue
        if any(k in line for k in DISTRACTOR_MARKERS):
            continue
        if any(k in line for k in ANSWER_MARKERS):
            nums |= {int(x) for x in CHOICE_RE.findall(line)}
    if not nums:
        return 'none'
    return 'many' if len(nums) > 1 else 'one'


def norm(s):
    s = re.sub(r'<[^>]+>', '', str(s))
    return re.sub(r'[\s\\,;$]', '', s)


def obj_span(raw, pos):
    """จาก pos (ตำแหน่งของ \"id\") ถอยหาปีกกาเปิด แล้วเดินหาปีกกาปิดที่คู่กัน"""
    i = raw.rfind('{', 0, pos)
    depth, j, instr, esc = 0, i, False, False
    while j < len(raw):
        c = raw[j]
        if instr:
            if esc:            esc = False
            elif c == '\\':    esc = True
            elif c == '"':     instr = False
        else:
            if   c == '"': instr = True
            elif c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    return i, j + 1
        j += 1
    raise ValueError("หาปีกกาปิดไม่เจอ")


def str_span(raw, start):
    """คืน (ต้น, ท้าย) ของสตริง JSON ที่เริ่มด้วย \" ที่ตำแหน่ง start"""
    j, esc = start + 1, False
    while j < len(raw):
        c = raw[j]
        if esc:          esc = False
        elif c == '\\':  esc = True
        elif c == '"':   return start, j
        j += 1
    raise ValueError("หาปลายสตริงไม่เจอ")


# ---------- 1) หาเป้าหมายจากไฟล์ sets (แหล่งความจริง) ----------
src = FILES[0]
if not os.path.isfile(src):
    print("⛔ ไม่พบ " + src + " — ครูรันในโฟลเดอร์ math-bank หรือยังครับ")
    sys.exit(1)

doc = json.load(open(src, encoding='utf-8'))
qs  = doc['questions'] if isinstance(doc, dict) and 'questions' in doc else doc

targets = {}       # id -> เลขตัวเลือก (1-based)
skipped = []
for q in qs:
    if q.get('type') != 'mc' or not isinstance(q.get('correct'), int):
        continue
    ex = q.get('explanation')
    if not isinstance(ex, list) or not ex:
        continue
    if declared(ex) != 'none':
        continue
    ticks = [i for i, L in enumerate(ex) if isinstance(L, str) and '✅' in L]
    if len(ticks) != 1:
        skipped.append((q['id'], "บรรทัด ✅ มี %d บรรทัด" % len(ticks))); continue
    # 🔒 ด่านความปลอดภัย: ข้อความในบรรทัด ✅ ต้องตรงกับ choices[correct]
    if norm(q['choices'][q['correct']]) not in norm(ex[ticks[0]]):
        skipped.append((q['id'], "บรรทัด ✅ ไม่ตรงกับตัวเลือกที่เป็นคำตอบ")); continue
    targets[q['id']] = q['correct'] + 1

print("=" * 70)
print("โหมด: " + ("✍️  เขียนจริง (--apply)" if APPLY else "🔍 ซ้อมเปล่า (ยังไม่เขียน)"))
print("เป้าหมาย %d ข้อ · ข้าม %d ข้อ" % (len(targets), len(skipped)))
for s in skipped:
    print("   ⏭️  %s — %s" % s)
if not targets:
    print("ไม่มีอะไรต้องแก้"); sys.exit(0)
ks = sorted(targets)
print("   ตั้งแต่ %s ถึง %s" % (ks[0], ks[-1]))
print("=" * 70)

# ---------- 2) แก้ทีละไฟล์ แบบไบนารี ----------
for path in FILES:
    if not os.path.isfile(path):
        print("\n⚠️  ข้าม (ไม่พบไฟล์): " + path); continue

    raw  = open(path, 'rb').read().decode('utf-8')
    b0   = len(raw.encode('utf-8'))
    lone0 = raw.count('\r') - raw.count('\r\n')
    out, hit, miss = raw, 0, []

    for qid in sorted(targets, reverse=True):     # ⬅️ ท้ายไปต้น: ตำแหน่งไม่เลื่อน
        n = targets[qid]
        mm = re.search(r'"id"\s*:\s*"' + re.escape(qid) + r'"', out)
        if not mm:
            miss.append(qid); continue
        a, b = obj_span(out, mm.start())
        seg  = out[a:b]
        if seg.count('✅') != 1:
            miss.append(qid + " (✅ ไม่ใช่ 1 ตัวในข้อนี้)"); continue
        t  = seg.index('✅')
        s0 = seg.rfind('"', 0, t)
        _, s1 = str_span(seg, s0)
        if 'ตัวเลือก' in seg[s0:s1]:
            miss.append(qid + " (บรรทัด ✅ มีคำว่าตัวเลือกอยู่แล้ว)"); continue
        newseg = seg[:s1] + (" → <b>ตัวเลือก %d</b>" % n) + seg[s1:]
        out = out[:a] + newseg + out[b:]
        hit += 1

    b1    = len(out.encode('utf-8'))
    lone1 = out.count('\r') - out.count('\r\n')

    print("\n📄 %s" % path)
    print("   แก้สำเร็จ %d ข้อ · พลาด %d" % (hit, len(miss)))
    for x in miss[:10]:
        print("      ⛔ " + x)
    print("   ไบต์ %d → %d (%+d) · \\r เดี่ยว %d → %d" % (b0, b1, b1 - b0, lone0, lone1))

    # ---------- 3) ด่านตรวจก่อนเขียน ----------
    ok = True
    if lone1 != lone0:
        print("   ⛔ จำนวน \\r เดี่ยวเปลี่ยน — ยกเลิกไฟล์นี้"); ok = False
    try:
        d2 = json.loads(out)
    except Exception as e:
        print("   ⛔ JSON พังหลังแก้: %s — ยกเลิกไฟล์นี้" % e); ok = False; d2 = None
    if d2 is not None:
        q2 = d2['questions'] if isinstance(d2, dict) and 'questions' in d2 else d2
        idx = {q.get('id'): q for q in q2}
        bad = []
        for qid, n in targets.items():
            q = idx.get(qid)
            if q is None:
                continue
            st = declared(q['explanation'])
            if st != 'one' or CHOICE_RE.findall(
                    [L for L in q['explanation'] if '✅' in L][0]) != [str(n)]:
                bad.append((qid, st))
        if bad:
            print("   ⛔ ตรวจซ้ำไม่ผ่าน %d ข้อ: %s — ยกเลิกไฟล์นี้" % (len(bad), bad[:5])); ok = False
        else:
            print("   ✅ ตรวจซ้ำ: ทุกข้อกลายเป็น 'ประกาศเลขเดียว' ตรงกับคีย์")
        if len(q2) != len(qs) and path == src:
            print("   ⛔ จำนวนข้อเปลี่ยน — ยกเลิกไฟล์นี้"); ok = False

    if not ok:
        print("   ⏭️  ไม่เขียนไฟล์นี้"); continue
    if not APPLY:
        print("   🔍 ซ้อมเปล่า — ยังไม่เขียน"); continue

    bak = path + ".bak-declare60"
    if not os.path.exists(bak):
        shutil.copy2(path, bak)
        print("   💾 สำรองไว้ที่ " + os.path.basename(bak))
    with open(path, 'wb') as f:
        f.write(out.encode('utf-8'))
    print("   ✍️  เขียนแล้ว")

print("\n" + "=" * 70)
print("เสร็จ" + ("" if APPLY else "  ·  ยังไม่ได้เขียนอะไร — ใส่ --apply เมื่อพร้อม"))
print("=" * 70)

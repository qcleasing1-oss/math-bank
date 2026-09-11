# -*- coding: utf-8 -*-
"""
วางเฉลยใหม่ chap-02-logic-q37  (v1.0 · ครูรันเอง)
------------------------------------------------
ทำไม : ครูเคาะแล้วว่าคำตอบคือ ตัวเลือก 1 "ก. และ ข. สมเหตุสมผล"
       ฟิลด์ correct แก้ไปแล้ว (= 0) แต่ "เฉลย" ยังเป็นของเก่าที่เดินไปหาตัวเลือก 3
       สคริปต์นี้วางเฉลยชุดใหม่ 44 ชิ้นแทนของเก่าทั้งก้อน

แก้ 2 ไฟล์ให้ตรงกัน
  1) data\\bank.json                    (ไฟล์ที่ generate ออกมา)
  2) data\\sets\\chap-02-logic.json     (ต้นฉบับ)

วิธีแก้ = ผ่าตัดข้อความเฉพาะช่วง "explanation": [ ... ] ของข้อนี้เท่านั้น
          ⛔ ไม่ re-serialize ทั้งไฟล์ → รูปแบบ/ขนาดไฟล์ส่วนอื่นไม่ขยับแม้แต่ไบต์เดียว

ใช้งาน
    python "วางเฉลยใหม่-q37-v1.0-ครูรันเอง.py"           ← ดูอย่างเดียว (dry-run)
    python "วางเฉลยใหม่-q37-v1.0-ครูรันเอง.py" --apply   ← เขียนจริง (สำรองไฟล์ให้อัตโนมัติ)

⛔ ไม่ยุ่งกับ git · ⛔ ไม่ลบไฟล์ใด · สำรองเป็น .bak-เฉลยq37 ก่อนเขียนเสมอ
"""
import io, json, os, shutil, sys

QID  = "chap-02-logic-q37"
ROOT = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(ROOT, "data", "bank.json")
SETS = os.path.join(ROOT, "data", "sets", "chap-02-logic.json")
APPLY = "--apply" in sys.argv

# ────────────────────────────────────────────────────────────────
# เฉลยชุดใหม่
# ────────────────────────────────────────────────────────────────
NEW = [
"<b>📐 ความรู้พื้นฐาน</b>",
"การอ้างเหตุผล <b>สมเหตุสมผล</b> เมื่อ (เหตุทุกข้อรวมกัน) $\\to$ (ผล) เป็น <b>สัจนิรันดร์</b>",
"พูดอีกอย่าง: <b>ไม่มีกรณีใดเลย</b> ที่เหตุจริงครบทุกข้อพร้อมกัน แล้วผลเท็จ",
"<b>⭐ กรณีพิเศษที่ต้องจำ</b> ถ้าเหตุ <b>ขัดแย้งกันเอง</b> (เป็นเท็จทุกกรณี) จะไม่มีกรณีที่เหตุจริงพร้อมกันเลย → เท็จ $\\to$ อะไรก็ได้ $=$ จริง → <b>สมเหตุสมผลเสมอ</b> ไม่ว่าผลจะเป็นอะไร",
"กฎที่ใช้: Modus Ponens · contrapositive $A \\to B \\equiv \\sim B \\to \\sim A$ · การกระจายนิเสธ $\\sim(r \\vee s) \\equiv \\sim r \\wedge \\sim s$ · กฎตัดออก",
"",
"<b>🎯 เป้าหมาย</b> ตรวจ ก. และ ข. ว่าสมเหตุสมผลหรือไม่ แล้วเลือกตัวเลือกที่ตรงกัน",
"",
"<b>【 วิธีที่ 1 ▸ พื้นฐาน · สมมติเหตุจริงพร้อมกัน แล้วลากไปหาผล 】</b>",
"<b>ขั้นที่ 1: ตรวจ ก.</b> เหตุ $(1)\\,q \\to \\sim r$, $(2)\\,q$, $(3)\\,r$ ; ผล $p$",
"สมมติเหตุทั้งสามข้อจริงพร้อมกัน",
"จาก (1) กับ (2) ด้วย Modus Ponens ได้ $\\sim r$ จริง คือ $r$ <b>เท็จ</b>",
"แต่ (3) บอกว่า $r$ <b>จริง</b> → เหตุขัดแย้งกันเอง ✗",
"แปลว่า <b>ไม่มีกรณีใดเลย</b> ที่เหตุจริงครบทั้งสามข้อ → เงื่อนไข (เหตุ) $\\to p$ มีส่วนหน้าเท็จเสมอ → เป็นจริงทุกกรณี คือ <b>สัจนิรันดร์</b>",
"→ <b>ก. สมเหตุสมผล</b>",
"",
"<b>ขั้นที่ 2: ตรวจ ข.</b> เหตุ $(1)\\,(p \\wedge q) \\to r$, $(2)\\,\\sim(r \\vee s)$, $(3)\\,p$ ; ผล $\\sim q$",
"จาก (2) กระจายนิเสธได้ $\\sim r \\wedge \\sim s$ ดังนั้น $\\sim r$ จริง คือ $r$ เท็จ",
"จาก (1) เขียน contrapositive ได้ $\\sim r \\to \\sim(p \\wedge q)$",
"นำ $\\sim r$ (จริง) เข้า Modus Ponens ได้ $\\sim(p \\wedge q)$ จริง คือ $\\sim p \\vee \\sim q$ จริง",
"จาก (3) $p$ จริง คือ $\\sim p$ เท็จ → ด้วยกฎตัดออก ได้ $\\sim q$ จริง",
"ตรงกับผลที่โจทย์ให้ → <b>ข. สมเหตุสมผล</b>",
"",
"<b>【 วิธีที่ 2 ▸ ⚡ ประยุกต์ · สมมติผลเท็จแล้วหาข้อขัดแย้ง 】</b>",
"หลักการ: ถ้าสมมติ “เหตุจริงทุกข้อ + ผลเท็จ” แล้ว <b>ชนความขัดแย้งเสมอ</b> → สมเหตุสมผล",
"<b>ขั้นที่ 1: ก. สมมติผลเท็จ</b> ให้ $p =$ เท็จ และเหตุจริงครบสามข้อ",
"• เหตุ (2) $q =$ จริง รวมกับเหตุ (1) $q \\to \\sim r$ ได้ $r =$ เท็จ",
"• แต่เหตุ (3) บอก $r =$ จริง — ขัดแย้ง ✗ (ชนตั้งแต่ยังไม่ได้ใช้ค่า $p$ ด้วยซ้ำ)",
"• สร้างกรณี “เหตุจริง + ผลเท็จ” ไม่ได้เลย → <b>ก. สมเหตุสมผล</b>",
"<b>ขั้นที่ 2: ข. สมมติผลเท็จ</b> ให้ $\\sim q =$ เท็จ คือ $q =$ จริง",
"• เหตุ (3) $p =$ จริง → $p \\wedge q =$ จริง",
"• เหตุ (2) $\\sim(r \\vee s)$ จริง → $r =$ เท็จ, $s =$ เท็จ",
"• เหตุ (1) $(p \\wedge q) \\to r =$ จริง$\\to$เท็จ $=$ เท็จ — ขัดแย้งกับที่ให้เหตุจริง ✗ → <b>ข. สมเหตุสมผล</b>",
"<b>ข้อต่าง:</b> วิธีที่ 1 ดูก่อนว่าเหตุจริงพร้อมกันได้ไหม · วิธีที่ 2 บังคับให้ผลเท็จแล้วดูว่าชนขัดแย้งไหม — สองวิธีให้คำตอบตรงกัน",
"",
"<b>✔ ตรวจคำตอบ:</b> ก. สมเหตุสมผล และ ข. สมเหตุสมผล → ตรงกับตัวเลือก “ก. และ ข. สมเหตุสมผล”",
"",
"<b>✅ คำตอบ: ก. และ ข. สมเหตุสมผล → ตัวเลือก 1</b>",
"",
"<b>💡 เทคนิคที่ใช้</b> เจอชุดเหตุที่ขัดแย้งกันเอง ให้ตอบ <b>สมเหตุสมผล</b> ได้ทันที ไม่ต้องสนใจว่าผลเขียนว่าอะไร",
"ข้อ ข. ใช้ <b>กระจายนิเสธ</b> + <b>contrapositive</b> + <b>กฎตัดออก</b> ต่อกันจนได้ $\\sim q$",
"",
"<b>⚠️ จุดที่เด็กมักผิด</b> ข้อ ก. เห็นว่าตัวแปร $p$ ในผล <b>ไม่ปรากฏในเหตุเลย</b> แล้วรีบสรุปว่า “ลากไปไม่ถึง $p$ ⇒ ไม่สมเหตุสมผล” ⇒ ไปตอบตัวเลือก 3 ซึ่ง <b>ผิด</b>",
"เกณฑ์ตัดสินคือ “มีกรณีที่เหตุจริงครบแล้วผลเท็จหรือไม่” ไม่ใช่ “ลากจากเหตุไปถึงผลได้หรือไม่” — เมื่อเหตุขัดแย้งกันเอง กรณีนั้นไม่มีอยู่จริง จึงสมเหตุสมผล",
]

# ────────────────────────────────────────────────────────────────
def find_expl_span(raw, qid):
    """คืน (start, end) ของช่วง [ ... ] ที่เป็น explanation ของข้อ qid"""
    needle = '"%s"' % qid
    hits = raw.count(needle)
    if hits != 1:
        raise RuntimeError("เจอ %s ในไฟล์ %d ครั้ง (ต้องเป็น 1 ครั้ง) — หยุดเพื่อความปลอดภัย" % (needle, hits))
    i = raw.find(needle)
    j = raw.find('"explanation"', i)
    if j < 0:
        raise RuntimeError("ไม่เจอคีย์ explanation หลัง id")
    k = raw.find('[', j)
    if k < 0:
        raise RuntimeError("ไม่เจอ [ หลัง explanation")
    # เดินหาวงเล็บปิดที่คู่กัน โดยข้ามอักขระที่อยู่ในสตริงและ escape
    depth, p, in_str, esc = 0, k, False, False
    while p < len(raw):
        c = raw[p]
        if in_str:
            if esc:            esc = False
            elif c == '\\':    esc = True
            elif c == '"':     in_str = False
        else:
            if   c == '"':     in_str = True
            elif c in '[{':    depth += 1
            elif c in ']}':
                depth -= 1
                if depth == 0:
                    return k, p + 1
        p += 1
    raise RuntimeError("หา ] ปิดไม่เจอ")


def render(old_span, items):
    """สร้างข้อความ [ ... ] ชุดใหม่ โดยลอกรูปแบบเว้นวรรค/ย่อหน้า/ชนิดขึ้นบรรทัดจากของเก่า"""
    ascii_only = all(ord(ch) < 128 for ch in old_span)
    nlchar = '\r\n' if '\r\n' in old_span else '\n'      # ⛔ ไฟล์ชุดนี้เป็น CRLF ห้ามแปลงเป็น LF
    body = old_span[1:]
    nl = body.find('\n')
    if nl < 0:                       # ของเก่าเขียนติดกันบรรทัดเดียว
        return json.dumps(items, ensure_ascii=ascii_only)
    item_ind = ''
    p = nl + 1
    while p < len(body) and body[p] == ' ':
        item_ind += ' '
        p += 1
    tail = old_span[:-1].rstrip(' ')
    close_ind = old_span[len(tail):-1]
    parts = [json.dumps(s, ensure_ascii=ascii_only) for s in items]
    return '[' + nlchar + (',' + nlchar).join(item_ind + x for x in parts) + nlchar + close_ind + ']'


def patch(path, label):
    if not os.path.exists(path):
        print("  ⛔ ไม่เจอไฟล์: %s" % path)
        return False
    raw = open(path, 'rb').read().decode('utf-8')   # ⛔ ไบนารี — ไม่ให้ python แปลง CRLF
    a, b = find_expl_span(raw, QID)
    old = raw[a:b]
    new = render(old, NEW)
    before = os.path.getsize(path)
    print("  %s" % label)
    print("    ชิ้นเฉลยเดิม: %d ชิ้น" % len(json.loads(old)))
    print("    ชิ้นเฉลยใหม่: %d ชิ้น" % len(NEW))
    print("    ช่วงที่จะทับ: %d → %d ไบต์(อักขระ)" % (len(old), len(new)))
    if not APPLY:
        print("    (dry-run — ยังไม่เขียน)")
        return True
    bak = path + ".bak-เฉลยq37"
    if not os.path.exists(bak):
        shutil.copy2(path, bak)
        print("    สำรองไว้ที่: %s" % os.path.basename(bak))
    out = raw[:a] + new + raw[b:]
    with open(path, 'wb') as f:
        f.write(out.encode('utf-8'))
    after = os.path.getsize(path)
    print("    ✅ เขียนแล้ว · ขนาด %d → %d (%+d ไบต์)" % (before, after, after - before))
    return True


def verify(path, label, expect_total=None):
    rawb = open(path, 'rb').read()
    d = json.loads(rawb.decode('utf-8'))
    qs = d['questions'] if isinstance(d, dict) else d
    q = [x for x in qs if x.get('id') == QID][0]
    print("  %s" % label)
    print("    ขึ้นบรรทัดแบบ CRLF: %d บรรทัด · LF ทั้งหมด: %d (สองเลขต้องเท่ากัน)" % (rawb.count(b"\r\n"), rawb.count(b"\n")))
    print("    จำนวนข้อในไฟล์: %d%s" % (len(qs), ("  (ต้องเป็น %d)" % expect_total) if expect_total else ""))
    print("    correct = %r · ตัวเลือกที่ชี้ = %r" % (q.get('correct'), q['choices'][q['correct']]))
    print("    ชนิด explanation = %s · จำนวนชิ้น = %d" % (type(q['explanation']).__name__, len(q['explanation'])))
    txt = "\n".join(q['explanation'])
    print("    เฉลยใหม่ชี้ 'ตัวเลือก 1'      : %s" % ('ตัวเลือก 1' in txt))
    print("    ยังหลงเหลือ 'ตัวเลือก 3' ไหม : %d ครั้ง (ควรมี 1 = บรรทัดจุดที่เด็กมักผิด)" % txt.count('ตัวเลือก 3'))
    print("    ยังมีคำว่า 'ก. ไม่สมเหตุสมผล' ไหม : %d ครั้ง (ควรเป็น 0)" % txt.count('ก. ไม่สมเหตุสมผล'))


print("=" * 62)
print("วางเฉลยใหม่ %s  %s" % (QID, "(เขียนจริง)" if APPLY else "(dry-run)"))
print("=" * 62)
ok1 = patch(BANK, "1) data\\bank.json")
ok2 = patch(SETS, "2) data\\sets\\chap-02-logic.json")

if APPLY and ok1 and ok2:
    print("-" * 62)
    print("=== ตรวจซ้ำ ===")
    verify(BANK, "1) data\\bank.json", 6557)
    verify(SETS, "2) data\\sets\\chap-02-logic.json", 128)
    print("-" * 62)
    print("เสร็จ · ⛔ สคริปต์นี้ไม่ได้แตะ git — ครู commit เองเมื่อพร้อม")
elif not APPLY:
    print("-" * 62)
    print("ถ้าถูกต้องแล้ว สั่งซ้ำด้วย --apply เพื่อเขียนจริง")

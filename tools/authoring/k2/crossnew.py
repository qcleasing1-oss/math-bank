# -*- coding: utf-8 -*-
"""ด่าน ④ · เทียบ "ข้อใหม่กับข้อใหม่กันเอง" หลัง merge — เงื่อนไขของครูในจดหมาย E→MB #20

    “ข้อที่แต่งขนานมองไม่เห็นกัน ⇒ อาจซ้ำกันเอง … ต้องเทียบข้อใหม่กันเองหลัง merge ด้วย
     (ตัวหาร = จำนวนคู่ในก้อนนั้น)”

ก้อน 18 มี 10 ข้อ ⇒ ตัวหาร = C(10,2) = 45 คู่ · ต้องรายงานครบทั้ง 45 คู่ ⛔ ไม่ใช่สุ่มดู

⚠️ ทำไมด่านนี้ไม่ซ้ำซ้อนกับ molds.py
   molds.py เทียบ "สามส่วนของแม่พิมพ์" ที่ผมเขียนเอง ⇒ ถ้าผมตั้งชื่อสองข้อต่างกันทั้งที่
   มันเหมือนกัน ด่านนั้นจะเขียวโดยที่ของจริงซ้ำ (กับดัก B8 รูปหนึ่ง)
   ด่านนี้จึงกวาด **ของจริงในไฟล์** แทน 4 ชั้นที่ผมโกงไม่ได้:
     ชั้น 1  แม่พิมพ์สามส่วน (เทียบกับ PLAN ของ molds.py)
     ชั้น 2  คำตอบที่ถูกต้อง — ค่าซ้ำกันเองในก้อนเดียวกัน
     ชั้น 3  ตัวเลือกทั้งใบ — ชุดตัวเลือกทับกันกี่ตัว
     ชั้น 4  คำนามฉากหลัง + สูตรหลักที่โผล่ในโจทย์ (กวาดจากตัวอักษรจริง)
"""
import io, json, re, itertools, importlib.util

FILE = ('/home/claude/k2/out/'
        'k2-ก้อน18-10ข้อ-7.11-7.4-7.5-7.10-7.6-7.1-7.7-7.9.json')

d = json.load(io.open(FILE, encoding='utf-8'))
qs = d['questions']
N = len(qs)
PAIRS = N * (N - 1) // 2
print('ก้อน 18 · %d ข้อ ⇒ ตัวหาร = C(%d,2) = %d คู่' % (N, N, PAIRS))

# ── ชั้น 1 · ดึง PLAN ของ molds.py มาใช้ตรง ๆ (ไม่คัดลอกมือ กันคัดลอกผิด) ──────
spec = importlib.util.spec_from_file_location('molds_src', '/home/claude/k2/molds.py')
src = io.open('/home/claude/k2/molds.py', encoding='utf-8').read()
ns = {}
exec(compile(src.split('def audit(')[0], 'molds_head', 'exec'), ns)
PLAN = ns['PLAN']

# ── ชั้น 4 · คำที่ใช้เป็นลายนิ้วมือของ "ฉากหลัง" และ "เครื่องมือ" ─────────────
# 🔴 บทเรียนรอบนี้ (ข้อค้นพบที่ 5 ของโครงการ) : ภาษาไทยไม่มีช่องว่างระหว่างคำ
#    ⇒ คำสั้น 2 พยางค์ในรายการนี้จะไป **ชนกลางคำอื่น** แล้วรายงานเท็จ
#    ของจริงที่เจอ : 'ล้อ' ไปชนใน "สอดคล้อง" ⇒ q101 ↔ q103 ขึ้น ⚠️ ฉากหลังร่วม
#    ทั้งที่ทั้งสองข้อเป็นสมการล้วน ไม่มีฉากหลังเลยสักข้อ
#    ⇒ กฎ : คำนามฉากหลังต้องเขียนให้ยาวพอจนไม่เป็นสตริงย่อยของคำอื่น
#      (ถ้าเลี่ยงไม่ได้ ให้ใส่คำขยายประกบ เช่น 'ล้อรถ' 'ล้อจักรยาน' แทน 'ล้อ')
BG = ['หลังคา', 'จั่ว', 'บอลลูน', 'เชือก', 'ล้อรถ', 'ล้อจักรยาน', 'ชิงช้า', 'บันได',
      'เสาธง', 'ตึก', 'สะพาน', 'ภูเขา', 'เรือ', 'เครื่องบิน', 'ว่าว', 'ต้นไม้',
      'หอคอย', 'รางน้ำ', 'พัดลม', 'จานดาวเทียม', 'ถัง', 'กรวย', 'ทางลาด', 'เงา',
      'นาฬิกา', 'แพะ', 'ลูกตุ้ม']
TOOL = ['กฎของโคไซน์', 'กฎของไซน์', 'มุมสองเท่า', 'ครึ่งมุม', 'ผลบวกมุม', 'ผลต่างมุม',
        'วงกลมหนึ่งหน่วย', 'เซกเตอร์', 'ส่วนโค้ง', 'พีทาโกรัส', 'เอกลักษณ์',
        'ผกผัน', 'จตุภาค', 'มุมอ้างอิง', 'สมการตรีโกณ', 'โคฟังก์ชัน']


def bag(q):
    stem = q['question']
    return (set(w for w in BG if w in stem), set(w for w in TOOL if w in stem))


def norm(c):
    """ตัดมาร์กอัปออก เหลือแก่นค่าไว้เทียบ"""
    s = re.sub(r'\$|\\left|\\right|\\,|\\;|\s+', '', str(c))
    s = s.replace('\\dfrac', '\\frac')
    return s


rows = []
bad = 0
for a, b in itertools.combinations(range(N), 2):
    qa, qb = qs[a], qs[b]
    ka = 'q%03d' % qa['questionNumber']
    kb = 'q%03d' % qb['questionNumber']
    ga, aa, ma = PLAN[ka]
    gb, ab, mb = PLAN[kb]
    same3 = (ga == gb) + (aa == ab) + (ma == mb)

    ansa = norm(qa['choices'][qa['correct']])
    ansb = norm(qb['choices'][qb['correct']])
    ans_same = ansa == ansb

    seta = set(norm(c) for c in qa['choices'])
    setb = set(norm(c) for c in qb['choices'])
    overlap = len(seta & setb)

    bga, ta = bag(qa)
    bgb, tb = bag(qb)
    bg_share = bga & bgb
    tool_share = ta & tb

    # เกณฑ์ตก : แม่พิมพ์ตรงสามส่วน  หรือ  ฉากหลังเดียวกัน+เครื่องมือเดียวกัน
    #           หรือ  ชุดตัวเลือกทับกัน >= 3 ตัว
    flag = ''
    if same3 == 3:
        flag = '❌ แม่พิมพ์ตรงสามส่วน'
    elif bg_share and tool_share:
        flag = '❌ ฉากหลัง+เครื่องมือเดียวกัน (%s · %s)' % (
            '/'.join(sorted(bg_share)), '/'.join(sorted(tool_share)))
    elif overlap >= 3:
        flag = '❌ ชุดตัวเลือกทับกัน %d ตัว' % overlap
    elif same3 == 2:
        flag = '⚠️ แม่พิมพ์ตรง 2/3 ส่วน'
    elif ans_same:
        flag = '⚠️ คำตอบถูกมีค่าเท่ากัน (%s)' % ansa
    elif overlap:
        flag = '⚠️ ตัวเลือกทับ %d ตัว' % overlap
    elif bg_share:
        flag = '⚠️ ฉากหลังร่วม (%s)' % '/'.join(sorted(bg_share))
    elif tool_share:
        flag = '⚠️ เครื่องมือร่วม (%s)' % '/'.join(sorted(tool_share))
    if flag.startswith('❌'):
        bad += 1
    rows.append((ka, kb, same3, overlap, flag))

print()
print('%-6s %-6s %-5s %-5s %s' % ('ข้อ A', 'ข้อ B', 'G/A/M', 'ตัวเลือกทับ', 'ผล'))
print('-' * 78)
for ka, kb, s3, ov, flag in rows:
    print('%-6s %-6s %-7s %-9s %s' % (ka, kb, '%d/3' % s3, '%d ตัว' % ov,
                                      flag or '✅ ผ่าน'))
print('-' * 78)
print('รายงานครบ %d คู่ จากตัวหาร %d ⇒ %s'
      % (len(rows), PAIRS, 'ครบ ✅' if len(rows) == PAIRS else 'ไม่ครบ ❌'))
print('คู่ที่ตก ❌ = %d คู่ ⇒ %s' % (bad, 'ผ่านด่าน ④ ✅' if bad == 0 else 'ต้องแก้ ❌'))

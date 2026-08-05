# -*- coding: utf-8 -*-
"""ด่าน ④ ก้อน 19 · เทียบ "ข้อใหม่กับข้อใหม่กันเอง" ครบทุกคู่ — ตัวหาร = C(20,2) = 190 คู่

⛔ รุ่นนี้อ่านจาก stems_b19.py (โจทย์ + คำตอบ ล้วน ๆ) ⇒ เป็นด่าน**ชั้นแรก** ทำงานได้ก่อนเขียนเฉลย
   ตามคำสั่ง ① ของครู : กวาดด่านให้จบก่อน แล้วค่อยเขียนเฉลยเฉพาะข้อที่รอด

สี่ชั้นเหมือนเดิม (ของจริงในไฟล์ ⛔ ไม่ใช่ป้ายที่ผมเขียนเอง ยกเว้นชั้น 1) :
  ชั้น 1  แม่พิมพ์สามส่วน (ดึง PLAN จาก molds.py ตรง ๆ ไม่คัดลอกมือ)
  ชั้น 2  คำตอบที่ถูกต้อง — ค่าซ้ำกันเองในก้อนเดียวกัน
  ชั้น 3  ตัวเลือกทั้งใบ — ชุดตัวเลือกทับกันกี่ตัว (ข้อ fill ไม่มีตัวเลือก ⇒ นับเป็น 0)
  ชั้น 4  คำนามฉากหลัง + สูตรหลักที่โผล่ในโจทย์ (กวาดจากตัวอักษรจริง)

🔴 กฎคำสั้น (บทเรียนข้อค้นพบที่ 5) : คำนามฉากหลังต้องยาวพอจนไม่เป็นสตริงย่อยของคำอื่น
"""
import io, re, itertools, sys

sys.path.insert(0, '/home/claude/k2')
from stems_b19 import STEMS

src = io.open('/home/claude/k2/molds.py', encoding='utf-8').read()
ns = {}
exec(compile(src.split('def audit(')[0], 'molds_head', 'exec'), ns)
PLAN = ns['PLAN']

N = len(STEMS)
PAIRS = N * (N - 1) // 2
print('ก้อน 19 · %d ข้อ ⇒ ตัวหาร = C(%d,2) = %d คู่' % (N, N, PAIRS))

BG = ['หลังคา', 'จั่ว', 'บอลลูน', 'เชือก', 'ล้อรถ', 'ล้อจักรยาน', 'ชิงช้า', 'บันได',
      'เสาธง', 'ตึก', 'สะพาน', 'ภูเขา', 'เรือ', 'เครื่องบิน', 'ว่าว', 'ต้นไม้',
      'หอคอย', 'รางน้ำ', 'พัดลม', 'จานดาวเทียม', 'ถังน้ำ', 'กรวย', 'ทางลาด', 'เงา',
      'นาฬิกา', 'แพะ', 'ลูกตุ้ม', 'ถนน', 'อาคาร', 'เสาไฟ']
TOOL = ['กฎของโคไซน์', 'กฎของไซน์', 'มุมสองเท่า', 'ครึ่งมุม', 'ผลบวกมุม', 'ผลต่างมุม',
        'วงกลมหนึ่งหน่วย', 'เซกเตอร์', 'ส่วนโค้ง', 'พีทาโกรัส', 'เอกลักษณ์',
        'ผกผัน', 'จตุภาค', 'มุมอ้างอิง', 'สมการตรีโกณ', 'โคฟังก์ชัน',
        'มุมฉาก', 'คางหมู', 'แอมพลิจูด', 'คาบ', 'เส้นรอบรูป', 'คอร์ด', 'แนบใน']


def bag(stem):
    return (set(w for w in BG if w in stem), set(w for w in TOOL if w in stem))


def norm(c):
    s = re.sub(r'\$|\\left|\\right|\\big|\\,|\\;|\s+', '', str(c))
    return s.replace('\\dfrac', '\\frac')


rows, bad = [], 0
for a, b in itertools.combinations(range(N), 2):
    na, sta, lva, tya, stema, cha, cora, acca = STEMS[a]
    nb, stb, lvb, tyb, stemb, chb, corb, accb = STEMS[b]
    ka, kb = 'q%03d' % na, 'q%03d' % nb
    ga, aa, ma = PLAN[ka]
    gb, ab, mb = PLAN[kb]
    same3 = (ga == gb) + (aa == ab) + (ma == mb)

    ansa = norm(cha[cora]) if tya == 'mc' else norm(cora)
    ansb = norm(chb[corb]) if tyb == 'mc' else norm(corb)
    ans_same = ansa == ansb

    seta = set(norm(c) for c in (cha or []))
    setb = set(norm(c) for c in (chb or []))
    overlap = len(seta & setb)

    bga, ta = bag(stema)
    bgb, tb = bag(stemb)
    bg_share, tool_share = bga & bgb, ta & tb

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
print('%-6s %-6s %-7s %-11s %s' % ('ข้อ A', 'ข้อ B', 'G/A/M', 'ตัวเลือกทับ', 'ผล'))
print('-' * 78)
for ka, kb, s3, ov, flag in rows:
    print('%-6s %-6s %-7s %-11s %s' % (ka, kb, '%d/3' % s3, '%d ตัว' % ov, flag or '✅ ผ่าน'))
print('-' * 78)
print('รายงานครบ %d คู่ จากตัวหาร %d ⇒ %s'
      % (len(rows), PAIRS, 'ครบ ✅' if len(rows) == PAIRS else 'ไม่ครบ ❌'))
print('คู่ที่ตก ❌ = %d คู่ ⇒ %s' % (bad, 'ผ่านด่าน ④ ✅' if bad == 0 else 'ต้องแก้ ❌'))
print()
print('สรุปคู่ที่ขึ้น ⚠️ (ต้องตรวจด้วยตา) :')
w = [r for r in rows if r[4].startswith('⚠️')]
for ka, kb, s3, ov, flag in w:
    print('   %s ↔ %s   %s' % (ka, kb, flag))
print('   รวม %d คู่' % len(w))
sys.exit(1 if bad else 0)

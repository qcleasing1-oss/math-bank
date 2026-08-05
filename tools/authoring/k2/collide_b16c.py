# -*- coding: utf-8 -*-
"""กวาดชนก้อน 16 · รอบ 3 — เติมช่อง "ยาก" ที่ยังว่าง

ผลรอบ 2 (out_b16b.txt) ตัดสินไปแล้ว
  ✅ S3 (ให้ cos(A+B), cos(A-B) ⇒ tan A tan B) = ว่าง
     S3a ชนเดียวคือ chap-07-trigonometry-q108 ซึ่งเป็นโจทย์สามเหลี่ยม G ต่าง · S3b = 0
  ✅ T1 (ผูกเชือกมุมอาคาร ⇒ พื้นที่เล็มหญ้า) = ว่าง — T1a 7 ข้อไม่เกี่ยว · T1b 1 ข้อไม่เกี่ยว · T1c 0
  ⛔ S18 (สองพาหนะคนละทิศ ⇒ ระยะห่าง) ถูกฆ่า — chap-07-trigonometry-q222 ตรงทั้ง G · A · M
  ⛔ T2 (วงกลมสองวงตัดกัน ⇒ พื้นที่ซ้อน) ถูกฆ่า — chap-07-trigonometry-q211 ตรงตัว
  ⚠️ S9 (มุมเงยจากพื้นเอียง) แออัด — "มุมเงย" 12 ข้อทั้งคลัง (รวม q003 q073 ของเราเอง)
     และ "มุมเงยสองจุดสังเกต" อยู่ในบัญชีแม่พิมพ์อิ่มตัวแล้ว ⇒ พักไว้ ไม่ใช้ในก้อนนี้

สเลตก้อน 16 ตอนนี้
  ง่าย    = R1  · 7.8      · เรนจ์ของ a·arccos x + b
  ปกลาง 1 = R2  · 7.10+7.9 · ระยะระหว่างปลายเข็มนาฬิกา (กฎโคไซน์)
  ปกลาง 2 = S3  · 7.5+7.4  · cos(A+B), cos(A-B) ⇒ tan A tan B
  ยากมาก  = T1  · 7.11     · เชือกที่มุมอาคาร ⇒ พื้นที่เล็มหญ้า (สามเซกเตอร์)
  ยาก     = ??? ← รอบนี้ยิงสี่แบบร่าง

แบบร่างที่ยิงรอบนี้
  U5  ยาก 7.5+7.2  · cos 20 + cos 100 + cos 140 (สามมุมห่างกัน 120 องศา ⇒ 0)
  U7  ยาก 7.3+7.6  · คาบของ f(x) = sin^4 x + cos^4 x (ยุบเป็น 3/4 + (1/4)cos 4x ⇒ pi/2)
      ⚠️ เสี่ยง WATCH-B กับ q055 ของเราเอง (ใช้ sin^4 + cos^4 = a) — ต้องดูให้ชัด
  U8  ยาก 7.10     · ตึกสองหลัง มุมก้มไปโคน + มุมเงยไปยอด ⇒ ความสูงตึกที่สอง
  U10 ยาก 7.5+7.4  · A+B+C = pi ⇒ tan A + tan B + tan C = tan A tan B tan C

⛔ แม่พิมพ์อิ่มตัว ห้ามแตะ: ผลบวกคำตอบสมการตรีโกณ (77) · ผลคูณโคไซน์ยุบมุมสองเท่า (12) ·
   a sin x + b cos x = c แบบมุมช่วย (80) · คิดค่านิพจน์ arc ซ้อน (19) · ผลบวก arctan (14) ·
   สมการ arcsin+arccos · มุมเงยสองจุดสังเกต (8) · sin x + cos x = ค่าคงที่ (25) ·
   มุมสองเท่าไปข้างหน้า (25)
"""
import io, json, glob, re

items = []
for p in sorted(glob.glob('/tmp/mb27/data/sets/*.json') +
                glob.glob('/home/claude/k1/out/*.json') +
                glob.glob('/home/claude/k2/out/*.json')):
    d = json.load(io.open(p, encoding='utf-8'))
    for q in d.get('questions', []):
        q['_src'] = p.split('/')[-1].replace('.json', '')
        items.append(q)


def txt(q):
    parts = [q.get('question') or '']
    parts += [str(c) for c in (q.get('choices') or [])]
    ex = q.get('explanation') or ''
    parts += ex if isinstance(ex, list) else [str(ex)]
    return '\n'.join(parts)


def scan(label, pattern, qonly=False, show=10, flags=0):
    rx = re.compile(pattern, flags)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-32s %-8s %-12s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:120]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# ── U5 · ผลบวกโคไซน์สามมุมห่างกัน 120 องศา ────────────────────────────────────
scan('U5a · คำถามมีผลบวกโคไซน์ตั้งแต่สามพจน์',
     r'\\cos[^$]{0,25}\+[^$]{0,25}\\cos[^$]{0,25}\+[^$]{0,25}\\cos', qonly=True, show=20)
scan('U5b · คำถามมีผลบวกไซน์ตั้งแต่สามพจน์',
     r'\\sin[^$]{0,25}\+[^$]{0,25}\\sin[^$]{0,25}\+[^$]{0,25}\\sin', qonly=True, show=20)
scan('U5c · เลข 20 กับ 140 องศาปรากฏร่วมกัน',
     r'20\^\{\\circ\}[^$]{0,60}140\^\{\\circ\}|140\^\{\\circ\}[^$]{0,60}20\^\{\\circ\}',
     show=20)
scan('U5d · คำว่า "ห่างกัน 120" หรือ "แบ่งวงกลมสามส่วนเท่ากัน"',
     r'120\^\{\\circ\}|\\frac\{2\\pi\}\{3\}|\\dfrac\{2\\pi\}\{3\}', qonly=True, show=20)

# ── U7 · คาบของ sin^4 + cos^4 ────────────────────────────────────────────────
scan('U7a · คำถามถาม "คาบ" ของฟังก์ชัน', r'คาบ', qonly=True, show=30)
scan('U7b · นิพจน์ sin^4 หรือ cos^4 ทั้งคลัง',
     r'\\sin\^\{?4\}?|\\cos\^\{?4\}?', show=25)
scan('U7c · คำว่า "แอมพลิจูด" ทั้งคลัง', r'แอมพลิจูด', show=25)

# ── U8 · ตึกสองหลัง มุมก้ม+มุมเงย ────────────────────────────────────────────
scan('U8a · คำว่า "ตึก/อาคาร/ดาดฟ้า/ยอดตึก"', r'ตึก|อาคาร|ดาดฟ้า', show=25)
scan('U8b · มุมก้มและมุมเงยอยู่ในข้อเดียวกัน',
     r'มุมก้ม[^\n]{0,200}มุมเงย|มุมเงย[^\n]{0,200}มุมก้ม', show=20)

# ── U10 · เอกลักษณ์ tan A + tan B + tan C ในสามเหลี่ยม ───────────────────────
scan('U10a · คำถามมี tan A + tan B (ผลบวก tan ของมุมสามเหลี่ยม)',
     r'\\tan\s*A\s*\+\s*\\tan\s*B|\\tan\s*x\s*\+\s*\\tan\s*y|'
     r'\\tan\s*\\alpha\s*\+\s*\\tan\s*\\beta', qonly=True, show=20)
scan('U10b · คำว่า "มุมภายในของสามเหลี่ยม" ร่วมกับ tan',
     r'มุมภายใน[^\n]{0,120}\\tan|\\tan[^\n]{0,120}มุมภายใน', show=20)
scan('U10c · A + B + C = pi หรือ 180 องศา ในคำถาม',
     r'A\s*\+\s*B\s*\+\s*C\s*=|\\alpha\s*\+\s*\\beta\s*\+\s*\\gamma\s*=', qonly=True, show=20)

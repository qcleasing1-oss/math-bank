# -*- coding: utf-8 -*-
"""กวาดชนก้อน 18 · รอบ 7 — ซ่อมจุดบอดของโพรบเอง + ตัวแทนช่อง "ง่าย" ตัวที่สาม

🔴 บทเรียนใหม่ที่แพงที่สุดของก้อนนี้ — **โพรบทิศทางเดียวมองไม่เห็นประโยคที่สลับลำดับคำ**
   P1a รอบ 1 เขียนว่า  r'tan.*(มากที่สุด|มากสุด|สูงสุด)'  ⇒ ได้ 0 ข้อ ⇒ ปล่อยผ่าน
   แต่ของจริงมีอยู่ : gen-chap-07-trigonometry-q076 **ของเราเอง**
     "ค่าของ $x$ ที่มากที่สุดซึ่งสอดคล้องกับสมการ $\\tan 2x = -\\sqrt{3}$ เมื่อ $0 \\le x < \\pi$"
   คำว่า "มากที่สุด" มา **ก่อน** คำว่า tan ⇒ regex ทิศเดียวไม่จับ
   ⇒ q095 (tan x = -1 ⇒ คำตอบมากที่สุด) ตาย : A-MAX-SOLUTION ตรงกับ q076 และแม่พิมพ์
     ก็คือ q076 แบบถอดตัวคูณหน้า x ออก ⇒ ต่างกันแกนเดียว (ตัวเลข) ผิดกฎเหล็ก 5 ที่ต้องต่าง 2 ใน 3
   ⭐ กฎใหม่ที่ต้องใช้ทุกโพรบต่อจากนี้ : ถ้าโพรบเป็นคู่คำ ให้เขียนสองทิศเสมอ
      A[\\s\\S]{0,N}B|B[\\s\\S]{0,N}A  ⛔ ห้ามเขียนทิศเดียว

⇒ ต้องยิงซ้ำ P8 (q102 นับจำนวนคำตอบ) ด้วย เพราะภาษาไทยนิยมพูด
   "จำนวนคำตอบของสมการ ... เท่ากับเท่าใด" คือวางคำถามไว้ "หน้า" สมการ

ตัวแทนที่ยิงรอบนี้
  U1 ง่าย 7.4 · รูปอย่างง่ายของ sin(t) sec(t) cot(t)  (แทนช่อง ง่าย ที่ q095 ตายไป)
  V1 (ยิงซ้ำ) q102 · 2cos^2 x - 3cos x + 1 = 0 ⇒ จำนวนคำตอบ — คราวนี้กวาดสองทิศ
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


def scan(label, pattern, qonly=False, show=8, flags=0):
    rx = re.compile(pattern, flags)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-32s %-8s %-12s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:110]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# ── U1 · ผลคูณ sin sec cot ⇒ ยุบเป็น 1 ─────────────────────────────────────
scan('U1a  คำถามมีทั้ง sec และ cot (สองทิศ)',
     r'\\sec[\s\S]{0,80}\\cot|\\cot[\s\S]{0,80}\\sec', qonly=True, show=12)
scan('U1b  คำถามเป็นผลคูณของฟังก์ชันตรีโกณสามตัวติดกัน',
     r'(\\sin|\\cos|\\tan|\\cot|\\sec|\\csc)\s*\\?[a-zA-Z\\]{1,8}\s*\\?[\s\\cdot]{0,8}'
     r'(\\sin|\\cos|\\tan|\\cot|\\sec|\\csc)\s*\\?[a-zA-Z\\]{1,8}\s*\\?[\s\\cdot]{0,8}'
     r'(\\sin|\\cos|\\tan|\\cot|\\sec|\\csc)', qonly=True, show=12)
scan('U1c  คำถามถามว่านิพจน์ตรงกับข้อใด/เท่ากับข้อใด แบบไม่มีเงื่อนไข (สองทิศ)',
     r'(ตรงกับข้อใด|เท่ากับข้อใด)[\s\S]{0,80}(\\sec|\\csc|\\cot)|'
     r'(\\sec|\\csc|\\cot)[\s\S]{0,120}(ตรงกับข้อใด|เท่ากับข้อใด)', qonly=True, show=12)

# ── V1 · ยิงซ้ำ q102 สองทิศ ────────────────────────────────────────────────
scan('V1a  คำถามนับคำตอบ + มี cos ยกกำลังสอง (สองทิศ)',
     r'(จำนวนคำตอบ|กี่คำตอบ|มีคำตอบกี่|กี่จำนวน)[\s\S]{0,220}\\cos\^|'
     r'\\cos\^[\s\S]{0,220}(จำนวนคำตอบ|กี่คำตอบ|มีคำตอบกี่|กี่จำนวน)', qonly=True, show=14)
scan('V1b  สมการกำลังสองในโคไซน์ที่แยกตัวประกอบได้ (ทุกลำดับคำ)',
     r'2\s*\\cos\^\{?2\}?|\\cos\^\{?2\}?\s*x\s*-\s*3', qonly=True, show=14)

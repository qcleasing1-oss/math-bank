# -*- coding: utf-8 -*-
"""กวาดชนก้อน 18 · รอบ 2 — ยิงตัวแทน 3 แบบที่ตายในรอบ 1 + รัดโพรบที่กว้างเกินไป

⛔ ที่ตายในรอบ 1
   P2  (ง่าย 7.8 · arcsin(sin 5pi/6)) — **ตายทันที** ชนกับ gen-chap-07-trigonometry-q051
       ของเราเองแบบคำต่อคำ (q051 ให้ a = arcsin(sin 5pi/6) ตรงตัว)
       ⇒ บทเรียนเดิมจากก้อน 17 ซ้ำรอยอีกครั้ง : ข้อ "ง่าย" มีพื้นที่เดินน้อย ชนของตัวเองง่ายที่สุด
   P4  (ปกลาง 7.6 · ให้ cos theta + จตุภาค ⇒ tan(theta/2)) — ชน chap-07-trigonometry-q161
       (ให้ tan theta + ช่วง ⇒ ค่าที่เป็นไปได้ของ tan(theta/2)) ⇒ G คล้าย · A ตรง · M ตรง
   P5  (ปกลาง 7.10 · เสาอากาศบนดาดฟ้า มุมเงยสองค่า) — แม่พิมพ์ "มุมเงยสองค่า" มีของแล้ว 5 ข้อ
       และ chap-07-trigonometry-q203 (จากฐานตึกกับจากยอดตึก) เป็นตัวเดียวกันแบบกลับด้าน
       ⇒ ทิ้งทั้งช่อง ไม่ใช้แม่พิมพ์มุมเงยในก้อนนี้เลย

ตัวแทนที่ยิงรอบนี้
  Q2 ง่าย   7.8  · tan(arccos(3/5)) ⇒ สามเหลี่ยมอ้างอิงจากค่าอาร์คตัวเดียว
  Q2' ง่าย  7.8  · (สำรอง) arccos(-1/2) - arcsin(-1/2) ⇒ ค่าหลักล้วน
  Q4 ปกลาง  7.8  · sin(2 arctan(1/3)) ⇒ สามเหลี่ยมอ้างอิงแล้วเข้าสูตรมุมสองเท่า
  Q5 ปกลาง  7.10 · หลังคาทรงจั่ว (ไม่มีผู้สังเกต ไม่มีมุมเงย) ⇒ ความยาวจันทัน + ความสูงสัน

โพรบที่ต้องรัดให้แคบลงจากรอบ 1
  P6 (47 ข้อจากคำกว้าง) · P7b (13 ข้อจากคำว่า csc) · P8b (103 ข้อจากคำว่าจำนวนคำตอบ)
  P9b (8 ข้อ) · P10a (21 ข้อจากคำว่าว่าว/ลูกโป่ง)
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

# ── Q2 · ฟังก์ชันตรีโกณครอบอาร์คตัวเดียว (สามเหลี่ยมอ้างอิง) ────────────────
scan('Q2a  คำถามมี tan/sin/cos ครอบ arc ตัวเดียว',
     r'\\(sin|cos|tan|cot|sec|csc)\s*\\?(left)?\s*\(\s*\\?(arcsin|arccos|arctan|operatorname\{arc)', qonly=True)
scan('Q2b  คำถามมี arc ของเศษส่วน 3/5 หรือ 4/5 หรือ 5/13',
     r'(arcsin|arccos|arctan)[\s\S]{0,30}(3\}\{5|4\}\{5|5\}\{13|12\}\{13)', qonly=True)
scan("Q2'  คำถามเป็นผลต่างของค่าหลักสองตัวล้วน ๆ",
     r'\\arccos[\s\S]{0,40}-\s*\\arcsin|\\arcsin[\s\S]{0,40}-\s*\\arccos', qonly=True)

# ── Q4 · สูตรมุมสองเท่าซ้อนบนอาร์ค ─────────────────────────────────────────
scan('Q4a  คำถามมี 2 arctan / 2 arcsin / 2 arccos (มุมสองเท่าของอาร์ค)',
     r'2\s*\\?(arctan|arcsin|arccos)|\\?(sin|cos|tan)\s*\\?(left)?\(\s*2\s*\\?(arctan|arcsin|arccos)', qonly=True)
scan('Q4b  คำถามมี arctan ของ 1/3 หรือ 1/2 หรือ 1/7',
     r'arctan[\s\S]{0,25}(1\}\{3|1\}\{2|1\}\{7)', qonly=True)

# ── Q5 · หลังคาทรงจั่ว (ไม่มีมุมเงย) ───────────────────────────────────────
scan('Q5a  คำว่า หลังคา / จั่ว / จันทัน / สันหลังคา', r'หลังคา|จั่ว|จันทัน|อกไก่')
scan('Q5b  คำว่า กระเช้า / เคเบิล / รอกลาก (บริบทสำรอง)', r'กระเช้า|เคเบิล|ลวดสลิง')

# ── P6 (รัด) · sin/(1-cot) + cos/(1-tan) ──────────────────────────────────
scan('P6c  คำถามมีทั้ง cot และ tan อยู่ในตัวส่วน',
     r'\{\s*1\s*-\s*\\cot[\s\S]{0,80}\{\s*1\s*-\s*\\tan|\{\s*1\s*-\s*\\tan[\s\S]{0,80}\{\s*1\s*-\s*\\cot', qonly=True)
scan('P6d  คำถามที่คำตอบยุบเป็น sin + cos', r'ยุบ|รูปอย่างง่าย|เท่ากับข้อใด[\s\S]{0,10}$',
     qonly=True, show=0)
scan('P6e  คำถามมีคำว่า 1-\\cot ในคำถามล้วน', r'1\s*-\s*\\cot', qonly=True)

# ── P7 (รัด) · หา csc จากสมการเชิงเส้นของ sin กับ cos ──────────────────────
scan('P7c  คำถามถาม csc และมีคำว่าจตุภาค', r'\\csc[\s\S]{0,200}จตุภาค|จตุภาค[\s\S]{0,200}\\csc', qonly=True)
scan('P7d  คำถามมีสมการ a sin = b cos ทุกแบบเขียน',
     r'\\sin\s*\\?[a-zA-Z\\]{1,10}\s*=\s*\d*\s*\\cos|\d\s*\\sin[\s\S]{0,12}=\s*\d\s*\\cos', qonly=True)

# ── P8 (รัด) · สมการกำลังสองใน cos ⇒ นับคำตอบ ──────────────────────────────
scan('P8c  คำถามมี cos^2 x และ cos x และถามจำนวนคำตอบ',
     r'\\cos\^\{?2\}?[\s\S]{0,60}\\cos[\s\S]{0,120}(จำนวนคำตอบ|กี่คำตอบ|มีคำตอบกี่)', qonly=True)
scan('P8d  คำถามมี 2\\cos^2 หรือ 2\\sin^2 พร้อมพจน์เชิงเส้น',
     r'2\\cos\^\{?2\}?\s*x\s*[-+]\s*\d\s*\\cos|2\\sin\^\{?2\}?\s*x\s*[-+]\s*\d\s*\\sin', qonly=True)

# ── P9 (รัด) · sin 3x = cos 2x ─────────────────────────────────────────────
scan('P9c  คำถามมี sin หรือ cos ของ 3x กับ 2x ในสมการเดียว',
     r'(\\sin|\\cos)\s*3\s*x[\s\S]{0,20}=[\s\S]{0,20}(\\sin|\\cos)\s*2\s*x|'
     r'(\\sin|\\cos)\s*2\s*x[\s\S]{0,20}=[\s\S]{0,20}(\\sin|\\cos)\s*3\s*x', qonly=True)
scan('P9d  คำถามถามคำตอบที่น้อยที่สุด', r'น้อยที่สุด', qonly=True, show=12)

# ── P10 (รัด) · บอลลูนผูกเชือกสองเส้นลงหมุดบนพื้น (สามมิติ) ─────────────────
scan('P10d บอลลูน/ลูกโป่งในคำถามจริง ๆ', r'บอลลูน|ลูกโป่ง', qonly=True)
scan('P10e วัตถุลอยอยู่เหนือจุดหนึ่ง + จุดบนพื้นสองจุด',
     r'(เหนือจุด|ลอยอยู่เหนือ|อยู่เหนือ)[\s\S]{0,200}(สองจุด|จุด\s*[AB][\s\S]{0,60}จุด\s*[AB])', qonly=True)
scan('P10f คำถามมีเชือกสองเส้น', r'เชือกสองเส้น|เชือก\s*2\s*เส้น|สายสองเส้น', qonly=True)

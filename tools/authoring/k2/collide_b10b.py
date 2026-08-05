# -*- coding: utf-8 -*-
"""กวาดรอบสอง — เจาะแม่พิมพ์ที่ตัดสินใจแล้วของก้อน 10 (หลังรอบแรกตัดทิ้งไป 3 อัน)

รอบแรกบอกอะไร
  ⛔ "ผลบวกของคำตอบ" ของสมการตรีโกณ อิ่มตัว (77 ข้อ · ในบท 7 เองมี q169, gen-q039, gen-q005)
  ⛔ ผลคูณโคไซน์ยุบด้วยมุมสองเท่า อิ่มตัว (pat1-2554-12-q31, chap-07-q43)
  ⛔ a sin x + b cos x = c แบบมุมช่วย อิ่มตัว (80 ข้อ · gen-q042 เป็นของเราเอง)
  ⇒ เปลี่ยนไปใช้ "คำถาม" ที่คลังยังไม่เคยถาม
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
    for r in (q.get('rows') or []):
        parts += [str(r.get('text', '')), str(r.get('why', ''))]
    return '\n'.join(parts)


def scan(label, pattern, qonly=False, show=8):
    rx = re.compile(pattern)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-30s %-8s %-10s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:115]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# q055 · sin^4+cos^4 = a + b cos4x จริงทุก x ⇒ หา a/b
scan('q055a · sin^4 + cos^4 (กำลังสี่)', r'\\sin\^4|\\cos\^4|\\sin\^\{4\}|\\cos\^\{4\}')
scan('q055b · โจทย์ที่ให้เอกลักษณ์จริงทุกค่า x แล้วถามสัมประสิทธิ์',
     r'(?:จริงทุก|ทุกจำนวนจริง|สำหรับทุก)[\s\S]{0,60}?(?:แล้ว\s*[abก]|ค่าของ\s*\$?[ab])', qonly=True)

# q056 · ให้ sin theta + จตุภาค ⇒ tan(theta/2) + cot(theta/2)
scan('q056a · tan ครึ่งมุม บวก cot ครึ่งมุม', r'\\cot\\?\s*(?:\\d?frac|\\dfrac)\{[^}]*\}\{2\}|\\cot\\frac\{\\theta\}\{2\}')
scan('q056b · โจทย์ที่ให้ pi < theta < 3pi/2 (จตุภาค 3) แล้วถามครึ่งมุม',
     r'\\pi\s*<\s*\\theta\s*<\s*\\d?frac\{3\\pi\}\{2\}', qonly=True)
scan('q056c · ใช้สูตรครึ่งมุมแล้วต้องเลือกเครื่องหมายจากจตุภาคของครึ่งมุม',
     r'จตุภาคของ[\s\S]{0,30}ครึ่ง|ครึ่งมุม[\s\S]{0,60}จตุภาค|\\dfrac\{\\theta\}\{2\}[\s\S]{0,80}จตุภาค')

# q057 · sin3x + sinx = sin2x ⇒ นับคำตอบ (ห้ามหารทิ้ง)
scan('q057a · ผลบวกไซน์สองพจน์ที่ต้องแปลงเป็นผลคูณ',
     r'\\sin\s*3x\s*\+\s*\\sin\s*x|\\sin 3x \+ \\sin x|ผลบวกเป็นผลคูณ|sum to product|\\sin A \+ \\sin B')
scan('q057b · บทที่ 7 ที่ถามว่า "มีกี่คำตอบ"',
     r'มี(?:ทั้งหมด)?กี่คำตอบ|มีกี่คำตอบ|มีคำตอบทั้งหมดกี่', qonly=True, show=14)

# q058 · ให้ sin(A+B) กับ sin(A-B) ⇒ หา tanB/tanA
scan('q058a · ให้ sin(A+B) และ sin(A-B) พร้อมกัน',
     r'\\sin\s*\(?\s*A\s*\+\s*B[\s\S]{0,200}?\\sin\s*\(?\s*A\s*-\s*B|\\sin\(A\+B\)[\s\S]{0,200}\\sin\(A-B\)')
scan('q058b · ถามอัตราส่วนของแทนเจนต์สองมุม',
     r'\\dfrac\{\\tan [A-Za-z]\}\{\\tan [A-Za-z]\}|\\frac\{\\tan [A-Za-z]\}\{\\tan [A-Za-z]\}|\\tan A\s*:\s*\\tan B')

# q059 · 2sin^2 x - (2a+1) sin x + a = 0 มีคำตอบพอดี 3 คำตอบใน [0,2pi) ⇒ เซตของ a
scan('q059a · สมการกำลังสองใน sin x ที่มีพารามิเตอร์ แล้วคุมจำนวนคำตอบ',
     r'(?:\\sin|\\cos)\^2\s*x[\s\S]{0,120}?(?:a|k)[\s\S]{0,120}?(?:มีคำตอบ|จำนวนคำตอบ|กี่คำตอบ)', qonly=True, show=12)
scan('q059b · ถามเซตของค่าพารามิเตอร์ทั้งหมด',
     r'เซตของค่า\s*\$?[ak]|ค่าของ\s*\$?[ak]\$?\s*ทั้งหมด', qonly=True, show=12)

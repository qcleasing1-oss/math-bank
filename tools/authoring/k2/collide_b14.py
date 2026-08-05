# -*- coding: utf-8 -*-
"""กวาดชนก้อน 14 · รอบ 1 — q075-q079
เป้าหัวข้อ (จากโน้ตที่ commit ไว้ใน molds.py) : เลี่ยง 7.9 (ก้อน 13 ใช้ไป 3 ข้อ) และ 7.8 (ตัน)
                                              ⇒ เล็ง 7.7 (5 ข้อ) · 7.1 (7 ข้อ) · 7.10 (6 ข้อ)

ผู้สมัครรอบนี้
  A  7.10 · บันไดพาดกำแพง (แม่พิมพ์ที่กันไว้ตั้งแต่ก้อน 13 · B1=B2=B3=0)
  B  7.7  · สมการง่ายบนช่วงจำกัด แต่ถาม "คำตอบที่มากที่สุด/น้อยที่สุด" ⛔ ไม่ใช่ผลบวก (อิ่มตัว 77 ข้อ)
  C  7.7  · sin x + cos x = 1 แก้ด้วยการยกกำลังสอง ⇒ ต้องคัดรากแปลกปลอม (M = คัดรากแปลกปลอม)
  D  7.7  · sin 3x = cos 2x ⇒ นับจำนวนคำตอบ (M = แปลงโคฟังก์ชัน + สองสาขา)
  E  7.4  · sin^4 x + cos^4 x = a มีคำตอบกี่ค่า ⇒ ถอดช่วงของ a (ยากมาก · T=3)
  F  7.10 · ทางลาด (W5 · กันไว้ตั้งแต่ก้อน 13)
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


def scan(label, pattern, qonly=False, show=10):
    rx = re.compile(pattern)
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

# ── A · บันไดพาดกำแพง ────────────────────────────────────────────────────────
scan('A1 · บันได/ไม้พาดกำแพง-ผนัง (ยิงตรงทุกสำนวน)',
     r'บันได|พาด(?:อยู่)?(?:กับ|บน)?\s*(?:กำแพง|ผนัง|ฝา)|(?:กำแพง|ผนัง)[\s\S]{0,60}?เอน', show=14)

# ── B · ถาม "คำตอบที่มากที่สุด/น้อยที่สุด" ของสมการตรีโกณบนช่วงจำกัด ──────────
scan('B1 · ถามคำตอบที่มากที่สุด/น้อยที่สุดของสมการตรีโกณ',
     r'(?:คำตอบ|ค่า\s*x|ค่าของ\s*\$?x)[\s\S]{0,40}?(?:มากที่สุด|น้อยที่สุด)[\s\S]{0,80}?'
     r'(?:สมการ|\\sin|\\cos|\\tan)', qonly=True, show=14)
scan('B2 · “คำตอบที่เป็นบวกที่น้อยที่สุด” (สำนวนที่นิยมในคลัง)',
     r'บวกที่น้อยที่สุด|น้อยที่สุดที่เป็นบวก|มากที่สุดที่เป็นลบ', qonly=True, show=14)

# ── C · คัดรากแปลกปลอมจากการยกกำลังสอง ───────────────────────────────────────
scan('C1 · sin x + cos x = ค่าคงที่ (ทุกสำนวน)',
     r'\\sin\s*x\s*\+\s*\\cos\s*x|\\cos\s*x\s*\+\s*\\sin\s*x|'
     r'\\sin\s*\\theta\s*\+\s*\\cos\s*\\theta|\\cos\s*\\theta\s*\+\s*\\sin\s*\\theta', show=16)
scan('C2 · เอ่ยถึงรากแปลกปลอม / ต้องตรวจคำตอบกลับ',
     r'รากแปลกปลอม|คำตอบแปลกปลอม|แทนกลับ[\s\S]{0,40}?ตัดทิ้ง|ไม่สอดคล้อง[\s\S]{0,30}?สมการเดิม', show=14)

# ── D · sin ax = cos bx ⇒ นับคำตอบ ───────────────────────────────────────────
scan('D1 · สมการรูป sin(ax) = cos(bx) (ต่างฟังก์ชัน ต่างสัมประสิทธิ์)',
     r'\\sin\s*\d?\s*x\s*=\s*\\cos|\\cos\s*\d?\s*x\s*=\s*\\sin|'
     r'\\sin\s*3\s*x[\s\S]{0,20}?\\cos\s*2\s*x|\\cos\s*2\s*x[\s\S]{0,20}?\\sin\s*3\s*x', show=16)
scan('D2 · ใช้สูตรโคฟังก์ชัน pi/2 - x ในการแก้สมการ',
     r'\\frac\{\\pi\}\{2\}\s*-\s*\d?\s*x|\\dfrac\{\\pi\}\{2\}\s*-\s*\d?\s*x|90\^?\{?\\?circ\}?\s*-', show=14)

# ── E · sin^4 + cos^4 = a ⇒ ช่วงของ a / จำนวนคำตอบ ───────────────────────────
scan('E1 · sin^4 + cos^4 (ทุกสำนวน)',
     r'\\sin\s*\^\s*\{?4\}?[\s\S]{0,30}?\\cos\s*\^\s*\{?4\}?|'
     r'\\cos\s*\^\s*\{?4\}?[\s\S]{0,30}?\\sin\s*\^\s*\{?4\}?', show=16)
scan('E2 · จำนวนคำตอบเป็นเงื่อนไข ⇒ ถอดช่วงของพารามิเตอร์',
     r'มีคำตอบ[\s\S]{0,30}?(?:ทั้งหมด|เพียง|เท่ากับ)\s*\$?\d+\s*(?:ค่า|คำตอบ|จำนวน)[\s\S]{0,120}?'
     r'(?:ช่วง|เซตของ|ค่าของ\s*\$?[ak])', qonly=True, show=14)

# ── F · ทางลาด ───────────────────────────────────────────────────────────────
scan('F1 · ทางลาด/ทางชัน/พื้นเอียง', r'ทางลาด|ทางชัน|พื้นเอียง|ลาดเอียง|ความชันของทาง', show=14)

# ── G · ความหนาแน่นหัวข้อของเราเอง ──────────────────────────────────────────
print()
print('== G · ข้อที่เราแต่งเอง แยกตามหัวข้อย่อย ==')
cnt = {}
for q in items:
    if q.get('sourceTag', '').startswith('แต่งใหม่'):
        for s in (q.get('subTopics') or []):
            cnt[s] = cnt.get(s, 0) + 1
for k in sorted(cnt):
    print('   %-6s %d' % (k, cnt[k]))

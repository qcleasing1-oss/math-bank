# -*- coding: utf-8 -*-
"""กวาดชนก้อน 15 · รอบ 3 — ยิงเฉพาะแบบร่าง 5 ตัวที่คัดมาแล้ว (ไม่กรองบท)

รอบสองเคลียร์ให้แล้ว
  ✅ A1/A2 (1-2sin^2 · 2cos^2-1) = 0 ข้อ
  ✅ C1 (ให้ tan(A+B) เป็นค่า) = 0 ข้อ
  ✅ D3 (1/(sec-tan) - 1/(sec+tan)) = 0 ข้อ · F1 (sec^2-tan^2 ในคำถาม) = 0 ข้อ
รอบนี้ยิงตัวที่ยังไม่ได้ตรวจ + ตรวจซ้ำแบบเจาะจงตัวเลข/ถ้อยคำจริงที่จะใช้
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


def scan(label, pattern, qonly=False, show=10):
    rx = re.compile(pattern)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-32s %-8s %-12s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:108]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# ── q081 · หาค่า arccos/arcsin ของค่าพิเศษ "ตรง ๆ" ไม่ซ้อนอะไรเลย ──────────────
scan('q081-1 · arc ของค่าพิเศษ แล้วบวก/ลบกันตรง ๆ (ไม่มีฟังก์ชันตรีโกณครอบ)',
     r'\\arc(cos|sin|tan)\s*\\?l?e?f?t?\(?\s*-?\\?d?f?r?a?c?\{?\s*-?\d*\\?s?q?r?t?'
     r'[^$]{0,40}[+\-][^$]{0,10}\\arc(cos|sin|tan)', qonly=True, show=20)
scan('q081-2 · โจทย์ที่ "ค่าของ arccos(...)" เป็นทั้งหมดของคำถาม (สั้นมาก)',
     r'^[^$]{0,24}\$\\arc[^$]{0,80}\$[^$]{0,40}$', qonly=True, show=20)
scan('q081-3 · sqrt3/2 หรือ -sqrt3/2 อยู่ในอาร์กิวเมนต์ของ arc',
     r'\\arc(cos|sin)[^$]{0,30}\\sqrt\{3\}', qonly=True, show=20)

# ── q082 · ให้ tan ของผลบวกมุม แล้วถอยกลับหามุมเดี่ยว ─────────────────────────
scan('q082-1 · "tan(A+B) =" หรือ "tan(x+y) =" ทุกที่ (รวมเฉลย)',
     r'\\tan\s*\\?l?e?f?t?\(\s*[A-Za-z]\s*\+\s*[A-Za-z]\s*\\?r?i?g?h?t?\)\s*=', show=20)
scan('q082-2 · โจทย์ให้ tan มุมหนึ่ง แล้วถามหา sin ของอีกมุมหนึ่ง',
     r'\\tan\s*[A-Za-z][^$]{0,60}=[^$]{0,60}\$[^$]{0,80}\\sin\s*[A-Za-z]', qonly=True, show=20)
scan('q082-3 · สูตร tan ผลต่างมุมถูกใช้ถอยหลัง (เฉลยเอ่ย "ย้ายข้าง" + tan)',
     r'\\tan\(A\s*-\s*B\)|\\tan\s*\\left\(A\s*-\s*B', show=20)

# ── q083 · คอนจูเกต sec-tan สองเศษส่วนลบกัน ───────────────────────────────────
scan('q083-1 · เศษส่วนที่ตัวส่วนเป็น sec ± tan',
     r'\{\\sec[^}]{0,24}[+\-][^}]{0,14}\\tan[^}]{0,14}\}', show=20)
scan('q083-2 · csc ± cot เป็นตัวส่วน',
     r'\{\\csc[^}]{0,24}[+\-][^}]{0,14}\\cot[^}]{0,14}\}', show=20)
scan('q083-3 · คำถามเอ่ย sec กับ tan ของมุมเดียวกันในนิพจน์เดียว',
     r'\\sec\\?t?h?e?t?a?[^$]{0,30}\\tan', qonly=True, show=20)

# ── q084 · สามเหลี่ยมแนบในวงกลม ⇒ รัศมีวงล้อม ⇒ มุมที่จุดศูนย์กลาง ⇒ ความยาวส่วนโค้ง ─
scan('q084-1 · คำว่า "วงกลมล้อมรอบ" / "แนบในวงกลม" / "circumcircle" คู่กับตรีโกณ',
     r'วงกลมล้อมรอบ|แนบในวงกลม|บรรจุในวงกลม|วงกลมแนบนอก|รัศมีของวงกลมที่ล้อมรอบ', show=20)
scan('q084-2 · a/sin A = 2R (กฎไซน์ฉบับขยาย)',
     r'2R|2\s*R\b|\\dfrac\{a\}\{\\sin\s*A\}\s*=\s*2', show=20)
scan('q084-3 · "มุมที่จุดศูนย์กลาง" คู่กับ "มุมในส่วนโค้ง/มุมในวงกลม"',
     r'มุมที่จุดศูนย์กลาง|มุมที่จุดศูนย์กลางของวงกลม|มุมในครึ่งวงกลม', show=20)
scan('q084-4 · ความยาวส่วนโค้ง ในโจทย์ที่มีสามเหลี่ยม',
     r'(?s)ความยาวส่วนโค้ง.{0,600}สามเหลี่ยม|(?s)สามเหลี่ยม.{0,600}ความยาวส่วนโค้ง', show=20)
scan('q084-5 · กฎของโคไซน์ + เซกเตอร์/ส่วนโค้ง ในข้อเดียวกัน',
     r'(?s)กฎของโคไซน์.{0,900}(เซกเตอร์|ส่วนโค้ง)|(?s)(เซกเตอร์|ส่วนโค้ง).{0,900}กฎของโคไซน์',
     show=20)

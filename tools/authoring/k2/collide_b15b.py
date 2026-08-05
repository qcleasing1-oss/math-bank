# -*- coding: utf-8 -*-
"""กวาดชนก้อน 15 · รอบ 2 — แบบร่างชุดใหม่หลังรอบแรกตัด P1/P3 ทิ้ง

รอบแรกให้ผลว่า
  ✅ P2b (1 - 2 sin^2 t / 2 cos^2 t - 1 ที่มุมตัวเลข) = 0 ข้อ ⇒ ใช้ได้
  ❌ P1b ชนของเราเอง q016 · ❌ P3a ชนของเราเอง q051
  ⚠️ P4/P6/P8 แน่นมาก (27-34 ข้อ) ⇒ เลี่ยง

แบบร่างรอบสอง
  A ง่าย    7.6      · 1 - 2 sin^2 t ที่มุมตัวเลข ⇒ ยุบเป็น cos 2t            (P2b เคลียร์แล้ว)
  B ง่าย    7.8      · arccos/arcsin ของอาร์กิวเมนต์ลบ ⇒ กับดักช่วงหลัก
  C ปกลาง   7.5/7.1  · ให้ tan(A+B) กับ tan A ⇒ ถอยกลับหา tan B
  D ยาก     7.4      · sec-tan คอนจูเกต ⇒ ยุบนิพจน์
  E ยากมาก  7.8/7.6  · ครึ่งมุมของ arccos ⇒ ต้องอ่านจตุภาคของครึ่งมุมเอง
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

# ── A · 1 - 2 sin^2 t / 2 cos^2 t - 1 (กวาดกว้างกว่ารอบแรก รวมเรเดียน) ─────────
scan('A1 · 1 - 2 sin^2 (...) ทุกหน่วยมุม',
     r'1\s*-\s*2\s*\\sin\^', qonly=True, show=12)
scan('A2 · 2 cos^2 (...) - 1 ทุกหน่วยมุม',
     r'2\s*\\cos\^\{?2\}?[^$]{0,26}-\s*1', qonly=True, show=12)
scan('A3 · คำถามเอ่ย \\dfrac{\\pi}{12} หรือ 15 องศา คู่กับกำลังสอง',
     r'(\\dfrac\{\\pi\}\{12\}|15\^?\\?\{?circ)[^$]{0,60}\^\{?2', qonly=True, show=12)

# ── B · arccos / arcsin ที่อาร์กิวเมนต์เป็นลบ (ตรง ๆ ไม่ซ้อนฟังก์ชันตรีโกณ) ────
scan('B1 · arccos(-...) หรือ arcsin(-...) ในคำถาม',
     r'\\arc(cos|sin|tan)\s*\\?l?e?f?t?\(?\s*-|'
     r'\\arc(cos|sin|tan)\s*\\?l?e?f?t?\(\s*\\?-|'
     r'\\arc(cos|sin|tan)\\left\(-', qonly=True, show=14)
scan('B2 · ผลบวก arcsin + arccos อยู่ในคำถามเดียวกัน',
     r'\\arcsin[^$]{0,80}\\arccos|\\arccos[^$]{0,80}\\arcsin', qonly=True, show=14)
scan('B3 · คำว่า "ช่วงหลัก" หรือ "ค่าหลัก" ในเฉลย ของบท 7.8',
     r'ช่วงหลัก|ค่าหลัก|principal', show=14)

# ── C · ให้ tan(A+B) กับ tan A ⇒ ถอยกลับหา tan B ──────────────────────────────
scan('C1 · คำถามมี tan(A+B) หรือ tan(x+y) เป็นค่าที่ "ให้มา"',
     r'\\tan\s*\\?l?e?f?t?\(\s*[A-Za-z]\s*\+\s*[A-Za-z]\s*\\?r?i?g?h?t?\)\s*=', qonly=True, show=14)
scan('C2 · คำถามเอ่ย tan สองมุมพร้อมกันแล้วถามอีกมุม',
     r'\\tan\s*[A-Za-z]\s*=[^$]{0,40}\\tan', qonly=True, show=14)

# ── D · sec - tan / sec + tan คอนจูเกต ────────────────────────────────────────
scan('D1 · sec ... - tan ... หรือ sec ... + tan ... ในคำถาม',
     r'\\sec[^$]{0,20}[+\-][^$]{0,6}\\tan|\\tan[^$]{0,20}[+\-][^$]{0,6}\\sec', qonly=True, show=14)
scan('D2 · คำว่า "คอนจูเกต" หรือ การคูณด้วยสังยุค ในเฉลย',
     r'สังยุค|คอนจูเกต|conjugate', show=14)
scan('D3 · 1/(sec-tan) รูปเศษส่วนสองก้อนลบกัน',
     r'\\dfrac\{1\}\{\\sec[^}]*\}[^$]{0,30}\\dfrac\{1\}\{\\sec', qonly=True, show=14)

# ── E · ครึ่งมุมของ arccos (ผสม 7.8 กับ 7.6) ──────────────────────────────────
scan('E1 · sin/cos/tan ของ (1/2) arccos หรือ arccos หารสอง',
     r'\\dfrac\{1\}\{2\}\s*\\arc|\\arc(cos|sin|tan)[^$]{0,40}\}\{2\}|'
     r'\\dfrac\{\\arc(cos|sin|tan)', qonly=True, show=14)
scan('E2 · คำถามเอ่ย arc พร้อมคำว่า ครึ่งมุม/มุมสองเท่า ในเฉลย',
     r'(?s)\\arc.{0,4000}(ครึ่งมุม|มุมสองเท่า)', show=14)
scan('E3 · tan ของครึ่ง arccos (แม่พิมพ์เจาะจง)',
     r'\\tan[^$]{0,30}\\arccos|\\tan[^$]{0,30}\\arcsin', qonly=True, show=14)

# ── สำรอง F · เอกลักษณ์ 1 + tan^2 = sec^2 ที่ต้องใช้ย้อนทาง ────────────────────
scan('F1 · sec^2 - tan^2 หรือ csc^2 - cot^2 ในคำถาม',
     r'\\sec\^\{?2\}?[^$]{0,26}-[^$]{0,10}\\tan\^|\\csc\^\{?2\}?[^$]{0,26}-[^$]{0,10}\\cot\^',
     qonly=True, show=14)
scan('F2 · sec^4 หรือ tan^4 ในคำถาม',
     r'\\sec\^\{?4\}?|\\tan\^\{?4\}?|\\cos\^\{?4\}?|\\sin\^\{?4\}?', qonly=True, show=14)

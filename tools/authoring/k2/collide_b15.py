# -*- coding: utf-8 -*-
"""กวาดชนก้อน 15 · รอบ 1

โควตาที่ก้อนนี้ต้องทำให้ได้ (จาก grade_b14 + คำสั่ง ④)
  · ง่าย อย่างน้อย 2 ข้อ (แถบ ง่าย เหลือ 22.8% ไหลลงสองก้อนติด)
  · ยากมาก 1 ข้อ (ทุกก้อนต้องมี)
  · เลี่ยง 7.7 (สะสม 8 · ใช้ไป 3 ในก้อน 14) และ 7.2 (สะสม 20 สูงสุดของบท)
  ⇒ เล็ง 7.5 (8) · 7.6 (8) · 7.8 (4 · ต่ำสุด) · 7.11 (8) · 7.4 (9)

แบบร่างที่ยิงรอบนี้
  P1 ง่าย   7.5  · cos A cos B + sin A sin B ที่มุมตัวเลข ⇒ ยุบกลับเป็นผลต่างมุม
  P2 ง่าย   7.6  · 2 sin t cos t หรือ 1 - 2 sin^2 t ที่มุมตัวเลข ⇒ ยุบกลับเป็นมุมสองเท่า
  P3 ปกลาง  7.8  · arcsin(sin X) / arccos(cos X) เมื่อ X อยู่นอกช่วงหลัก (กับดักช่วงหลัก)
  P4 ยาก    7.6  · ครึ่งมุมที่ต้องอ่านจตุภาคของ theta/2 เอง (cos theta ให้มา theta อยู่ Q2)
  P5 ยาก    7.11 · เซกเตอร์ที่กำหนดเส้นรอบรูปคงที่ ⇒ พื้นที่มากสุด
  P6 ยากมาก 7.5  · ผลคูณแทนเจนต์สามมุม tan 20 tan 40 tan 80
  P7 ยากมาก 7.7  · sin t + sin 2t + sin 3t = 0 ⇒ นับคำตอบ (สำรอง · 7.7 อิ่มแล้ว)
  P8 ง่าย   7.5  · ผลบวกไซน์สองมุม ⇒ sum-to-product

⛔ แม่พิมพ์ที่ตีตราว่าอิ่มตัวแล้ว ห้ามแตะ: ผลบวกคำตอบสมการตรีโกณ (77) ·
   ผลคูณโคไซน์ยุบมุมสองเท่า (12) · a sin x + b cos x = c แบบมุมช่วย (80) ·
   คิดค่านิพจน์ arc ซ้อน (19) · ผลบวก arctan (14) · สมการ arcsin+arccos ·
   มุมเงยสองจุดสังเกต (8)
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
BY = {q['id']: q for q in items}


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
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:110]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# ── P1 · cos A cos B + sin A sin B ที่มุมตัวเลข (ยุบกลับเป็นผลต่างมุม) ────────────
scan('P1a · คำถามมีรูป cos_ cos_ + sin_ sin_ (หรือลบ) ที่มุมเป็นตัวเลข',
     r'\\cos\s*\d+[^$]{0,40}\\cos\s*\d+[^$]{0,20}[+\-][^$]{0,20}\\sin\s*\d+[^$]{0,40}\\sin\s*\d+',
     qonly=True, show=14)
scan('P1b · คำถามมีรูป sin_ cos_ + cos_ sin_ ที่มุมเป็นตัวเลข',
     r'\\sin\s*\d+[^$]{0,40}\\cos\s*\d+[^$]{0,20}[+\-][^$]{0,20}\\cos\s*\d+[^$]{0,40}\\sin\s*\d+',
     qonly=True, show=14)

# ── P2 · 2 sin t cos t / 1 - 2 sin^2 t ที่มุมตัวเลข ────────────────────────────
scan('P2a · คำถามมีรูป 2 sin_ cos_ ที่มุมเป็นตัวเลขเดียวกัน',
     r'2\s*\\sin\s*\d+[^$]{0,30}\\cos\s*\d+', qonly=True, show=14)
scan('P2b · คำถามมีรูป 1 - 2 sin^2 หรือ 2 cos^2 - 1 ที่มุมตัวเลข',
     r'1\s*-\s*2\s*\\sin\^|2\s*\\cos\^\{?2\}?\s*\d+[^$]{0,10}-\s*1', qonly=True, show=14)

# ── P3 · arcsin(sin X) / arccos(cos X) ซ้อนกลับ ───────────────────────────────
scan('P3a · arcsin(sin ...) หรือ arccos(cos ...) หรือ arctan(tan ...) ซ้อนกลับ',
     r'\\arcsin\s*\\?\(?\s*\\?l?e?f?t?\(?\s*\\sin|'
     r'\\arccos\s*\\?\(?\s*\\?l?e?f?t?\(?\s*\\cos|'
     r'\\arctan\s*\\?\(?\s*\\?l?e?f?t?\(?\s*\\tan|'
     r'\\sin\^\{-1\}[^$]{0,12}\\sin|\\cos\^\{-1\}[^$]{0,12}\\cos', show=20)
scan('P3b · คำว่า "ช่วงหลัก" หรือ "ค่าหลัก" ของฟังก์ชันผกผัน', r'ช่วงหลัก|ค่าหลัก', show=14)

# ── P4 · ครึ่งมุมที่ต้องอ่านจตุภาคของครึ่งมุมเอง ─────────────────────────────
scan('P4a · คำถามพูดถึง theta/2 หรือ x/2 ในฟังก์ชันตรีโกณ',
     r'\\sin\s*\\?l?e?f?t?\(?\s*\\d?frac\{[^}]*\}\{2\}|'
     r'\\cos\s*\\?l?e?f?t?\(?\s*\\d?frac\{[^}]*\}\{2\}|'
     r'\\sin\s*\\d?frac\{\\theta\}\{2\}|\\cos\s*\\d?frac\{\\theta\}\{2\}|'
     r'\\tan\s*\\d?frac\{\\theta\}\{2\}|\\frac\{x\}\{2\}|\\dfrac\{x\}\{2\}',
     qonly=True, show=20)
scan('P4b · คำว่า "ครึ่งมุม" ทั้งคลัง', r'ครึ่งมุม', show=20)

# ── P5 · เซกเตอร์เส้นรอบรูปคงที่ ⇒ พื้นที่มากสุด ────────────────────────────
scan('P5a · เซกเตอร์ + เส้นรอบรูป/ความยาวรอบ', r'เส้นรอบ.{0,30}เซกเตอร์|เซกเตอร์.{0,40}เส้นรอบ|'
     r'ความยาวรอบ.{0,30}เซกเตอร์|เซกเตอร์.{0,40}ความยาวรอบ', show=14)
scan('P5b · พื้นที่มากที่สุด/มากสุด ในบทตรีโกณ',
     r'พื้นที่.{0,25}มากที่สุด|พื้นที่.{0,25}สูงสุด', show=20)

# ── P6 · ผลคูณแทนเจนต์สามมุม ────────────────────────────────────────────────
scan('P6a · ผลคูณแทนเจนต์ตั้งแต่สองตัวขึ้นไปที่มุมเป็นตัวเลข',
     r'\\tan\s*\d+[^$]{0,25}\\tan\s*\d+', show=20)
scan('P6b · ผลคูณโคไซน์ที่มุมเป็นตัวเลข (แม่พิมพ์ที่ตีตราว่าอิ่มแล้ว · ตรวจซ้ำ)',
     r'\\cos\s*\d+[^$]{0,25}\\cos\s*\d+[^$]{0,25}\\cos\s*\d+', show=14)

# ── P7 · ผลรวมไซน์สามพจน์เป็นศูนย์ ──────────────────────────────────────────
scan('P7a · sin t + sin 2t + sin 3t หรือ cos t + cos 2t + cos 3t',
     r'\\sin\s*x\s*\+\s*\\sin\s*2\s*x|\\sin\s*\\theta\s*\+\s*\\sin\s*2\s*\\theta|'
     r'\\cos\s*x\s*\+\s*\\cos\s*2\s*x|\\cos\s*\\theta\s*\+\s*\\cos\s*2\s*\\theta', show=20)

# ── P8 · ผลบวกไซน์สองมุม ⇒ sum-to-product ──────────────────────────────────
scan('P8a · sin_ + sin_ หรือ cos_ + cos_ ที่มุมเป็นตัวเลข (sum-to-product)',
     r'\\sin\s*\d+\^?\{?\\?c?i?r?c?\}?\s*\+\s*\\sin\s*\d+|'
     r'\\cos\s*\d+\^?\{?\\?c?i?r?c?\}?\s*\+\s*\\cos\s*\d+', qonly=True, show=20)
scan('P8b · คำว่า "ผลบวกเป็นผลคูณ" / sum-to-product ในเฉลย',
     r'ผลบวกเป็นผลคูณ|ผลคูณเป็นผลบวก', show=14)

# ── สำมะโนหัวข้อย่อยฝั่งเรา เพื่อยืนยันโควตา ────────────────────────────────
print()
print('== สำมะโนหัวข้อย่อยของข้อที่เราแต่งเอง ==')
cnt = {}
lv = {}
for q in items:
    if not q['id'].startswith('gen-chap-07'):
        continue
    for s in (q.get('subTopics') or []):
        cnt[s] = cnt.get(s, 0) + 1
    lv[q.get('difficulty')] = lv.get(q.get('difficulty'), 0) + 1
for k in sorted(cnt):
    print('   %-6s %d' % (k, cnt[k]))
print('   ระดับ:', lv)

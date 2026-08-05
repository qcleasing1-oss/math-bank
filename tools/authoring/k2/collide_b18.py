# -*- coding: utf-8 -*-
"""กวาดชนก้อน 18 · รอบ 1 — ก้อนแรกที่มี 10 ข้อ (q095-q104) ตามมติครูเรื่องความเร็ว

แบบร่าง 10 แบบ (โควตาที่ตั้งใจ : ง่าย 2 · ปานกลาง 6 · ยาก 1 · ยากมาก 1)
  P1  ง่าย   7.7  · tan x = -1 ใน (0, 2pi) ⇒ คำตอบที่มีค่ามากที่สุด
  P2  ง่าย   7.8  · arcsin(sin(5pi/6)) ⇒ พับเข้าช่วงค่าหลัก
  P3  ปกลาง  7.5  · ให้อัตราส่วน+จตุภาคของสองมุม ⇒ sin(A+B)
  P4  ปกลาง  7.6  · ให้ cos theta และจตุภาค 2 ⇒ tan(theta/2)
  P5  ปกลาง  7.10 · เสาอากาศบนดาดฟ้า มุมเงยสองค่าจากจุดสังเกตจุดเดียว ⇒ ความยาวเสาอากาศ
  P6  ปกลาง  7.4  · sin/(1-cot) + cos/(1-tan) ⇒ ยุบเป็น sin + cos
  P7  ปกลาง  7.1  · 3 sin theta = 2 cos theta และจตุภาค 3 ⇒ csc theta
  P8  ปกลาง  7.7  · 2cos^2 x - 3cos x + 1 = 0 ⇒ จำนวนคำตอบใน [0, 2pi)
  P9  ยาก    7.7  · sin 3x = cos 2x ⇒ คำตอบบวกที่น้อยที่สุด
  P10 ยากมาก 7.10 · บอลลูนผูกเชือกสองเส้นลงหมุดบนพื้น ⇒ ระยะระหว่างหมุด (สามมิติ)

⭐ บทเรียนจากก้อน 17 ที่บังคับใช้รอบนี้ :
   (1) ต้องกวาดคลังของตัวเองด้วย ไม่ใช่กวาดแต่คลังเดิม (N1 ตายเพราะซ้ำ q016 ของเราเอง)
   (2) ต้องระวัง false positive จากคำซ้อน ⇒ ใช้ negative lookbehind ทุกคำที่เสี่ยง
   (3) แม่พิมพ์อิ่มตัวที่ห้ามแตะ : ผลบวกคำตอบสมการตรีโกณ · a sin x + b cos x = c แบบมุมช่วย
       · arc ซ้อน · ผลบวก arctan · มุมเงยสองจุดสังเกต · sin x + cos x = ค่าคงที่ · มุมสองเท่าไปข้างหน้า
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

# ── P1 · tan x = -1 หาคำตอบที่มากที่สุด ────────────────────────────────────
scan('P1a  คำถามมี tan และคำว่ามากที่สุด/มากสุด', r'tan.*(มากที่สุด|มากสุด|สูงสุด)', qonly=True)
scan('P1b  คำถามมี tan x = -1 ตรงตัว', r'tan\s*x\s*=\s*-\s*1|tan\\?,?\s*x\s*=\s*-1', qonly=True)

# ── P2 · arcsin(sin ...) พับเข้าช่วงค่าหลัก ────────────────────────────────
scan('P2a  arc ครอบ trig ตรง ๆ (arcsin(sin / arccos(cos / arctan(tan)',
     r'(arcsin|\\sin\^\{-1\})\s*\\?\(?\s*\\?\(?\s*\\sin|'
     r'(arccos|\\cos\^\{-1\})\s*\\?\(?\s*\\?\(?\s*\\cos|'
     r'(arctan|\\tan\^\{-1\})\s*\\?\(?\s*\\?\(?\s*\\tan')
scan('P2b  คำว่า ค่าหลัก / ช่วงหลัก', r'ค่าหลัก|ช่วงหลัก|principal')

# ── P3 · sin(A+B) จากอัตราส่วน + จตุภาค ────────────────────────────────────
scan('P3a  คำถามถาม sin(A+B) ตรงตัว', r'\\sin\s*\\?\(?\s*A\s*\+\s*B|\\sin\s*\(\s*A\s*\+\s*B', qonly=True)
scan('P3b  คำถามมีสองจตุภาคระบุพร้อมกัน', r'จตุภาคที่.*จตุภาคที่', qonly=True)

# ── P4 · tan(theta/2) จาก cos theta ────────────────────────────────────────
scan('P4a  คำถามถามครึ่งมุมของ tan', r'\\tan\s*\\?(frac|dfrac)?\s*\{?\s*\\?theta\s*\}?\s*\{?\s*2|'
     r'\\tan\s*\\dfrac\{\\theta\}\{2\}|\\tan\\left\(\\dfrac\{\\theta\}\{2\}', qonly=True)
scan('P4b  คำว่า ครึ่งมุม ในคำถาม', r'ครึ่งมุม|มุมครึ่ง', qonly=True)

# ── P5 · เสาอากาศ/ป้ายบนดาดฟ้า มุมเงยสองค่าจากจุดเดียว ─────────────────────
scan('P5a  คำว่า ดาดฟ้า / เสาอากาศ / ยอดอาคาร', r'ดาดฟ้า|เสาอากาศ|เสาสัญญาณ|ป้ายบนอาคาร')
scan('P5b  มุมเงยสองค่าในคำถามเดียว', r'มุมเงย[\s\S]{0,120}มุมเงย', qonly=True)

# ── P6 · sin/(1-cot) + cos/(1-tan) ─────────────────────────────────────────
scan('P6a  ตัวส่วนมี 1 - cot หรือ 1 - tan', r'1\s*-\s*\\cot|1\s*-\s*\\tan|1-\\cot|1-\\tan')
scan('P6b  คำถามเป็นผลบวกเศษส่วนตรีโกณสองก้อน',
     r'\\dfrac\{\\sin[\s\S]{0,60}\}\s*\+\s*\\dfrac\{\\cos', qonly=True)

# ── P7 · a sin theta = b cos theta + จตุภาค ⇒ csc ───────────────────────────
scan('P7a  คำถามมีสมการ k sin = m cos', r'\d\s*\\sin\s*\\?theta\s*=\s*\d\s*\\cos|'
     r'\d\\sin\\theta=\d\\cos', qonly=True)
scan('P7b  คำถามถาม csc', r'\\csc|\\operatorname\{cosec\}|โคเซแคนต์', qonly=True)

# ── P8 · สมการกำลังสองใน cos ⇒ นับจำนวนคำตอบ ───────────────────────────────
scan('P8a  คำถามมี cos^2 พร้อม cos และ = 0', r'\\cos\^\{?2\}?\s*x[\s\S]{0,40}\\cos\s*x[\s\S]{0,20}=\s*0', qonly=True)
scan('P8b  คำถามถามจำนวนคำตอบของสมการ', r'จำนวนคำตอบ|มีคำตอบกี่|กี่คำตอบ|กี่จำนวน', qonly=True)

# ── P9 · sin 3x = cos 2x ───────────────────────────────────────────────────
scan('P9a  คำถามมี sin(ตัวคูณ x) = cos(ตัวคูณ x)',
     r'\\sin\s*\d\s*x\s*=\s*\\cos\s*\d\s*x|\\cos\s*\d\s*x\s*=\s*\\sin\s*\d\s*x', qonly=True)
scan('P9b  คำถามถามคำตอบบวกที่น้อยที่สุด', r'บวกที่น้อยที่สุด|น้อยที่สุดที่เป็นบวก|ค่าบวกน้อยสุด', qonly=True)

# ── P10 · บอลลูนผูกเชือกสองเส้น (สามมิติ) ──────────────────────────────────
scan('P10a คำว่า บอลลูน / ลูกโป่ง / ว่าว', r'บอลลูน|ลูกโป่ง|ว่าว(?!ง)')
scan('P10b คำว่า เชือก คู่กับ หมุด/ตรึง', r'เชือก[\s\S]{0,80}(หมุด|ตรึง|ยึด)|( หมุด|ตรึง|ยึด)[\s\S]{0,80}เชือก')
scan('P10c โจทย์ที่มีมุม 150 องศา ในคำถาม', r'150\s*(องศา|\^\{?\\circ)', qonly=True)

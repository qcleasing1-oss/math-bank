# -*- coding: utf-8 -*-
"""กวาดชนก้อน 17 · รอบ 1

โควตาที่ก้อนนี้ต้องทำให้ได้ (จาก audit44 หลังก้อน 16 + คำสั่ง ④)
  · ง่าย 2 · ยาก 2 · ยากมาก 1  (ไม่มีปานกลางในก้อนนี้ — ปานกลางสะสม 34.8% เกินเป้า 35% แล้วเกือบพอดี)
  · เลี่ยงเป็น "แกนหลัก": 7.2 (20) · 7.3 (17) · 7.9 (14)
  ⇒ เล็ง 7.8 (6 · บางสุด) · 7.7 (9) · 7.10 (9) · 7.1 (10) · 7.5 · 7.6 · 7.11 (อย่างละ 10)

⭐ ข้อจำกัดเชิงคะแนนที่ต้องรู้ก่อนออกแบบ "ง่าย"
   ง่าย ต้อง tot <= 2 และ T <= 1 และ C == 0 · แต่ F >= 1 และ P >= 1 เสมอ
   ⇒ ง่ายที่แท้จริงต้องมี L = 0 ⇒ **ต้องเป็นโจทย์สัญลักษณ์ล้วน ห้ามมีบริบท/เรื่องเล่า**

แบบร่างที่ยิงรอบนี้
  W1 ง่าย   7.8  · โดเมนของ arcsin/arccos ที่อาร์กิวเมนต์เป็นเชิงเส้น ⇒ ตอบเป็นช่วงปิด
  W2 ง่าย   7.4  · ยุบนิพจน์เอกลักษณ์ (1-sin)(1+sin)sec^2 ⇒ ค่าคงที่
  W3 ยาก    7.7  · tan x + cot x = k ใน (0, pi) ⇒ พลิกเป็น sin 2x
  W4 ยาก    7.11 · พื้นที่เซกเมนต์ (เซกเตอร์ ลบ สามเหลี่ยม)
  W5 ยากมาก 7.6×7.5 · ให้ sin x + sin y = a และ cos x + cos y = b ⇒ หา tan((x+y)/2) / cos(x-y)
  W6 ยาก    7.10 · เดินเรือ/บอกทิศ (bearing) ⇒ ระยะจากจุดเริ่มต้น  (สำรอง)
  W7 ง่าย   7.1  · ให้อัตราส่วนหนึ่งของมุมแหลม ⇒ หาอีกอัตราส่วน  (สำรอง · น่าจะชนหนัก)

⛔ แม่พิมพ์ที่ตีตราว่าอิ่มตัวแล้ว ห้ามแตะ: ผลบวกคำตอบสมการตรีโกณ (77) ·
   ผลคูณโคไซน์ยุบมุมสองเท่า (12) · a sin x + b cos x = c แบบมุมช่วย (80) ·
   คิดค่านิพจน์ arc ซ้อน (19) · ผลบวก arctan (14) · สมการ arcsin+arccos ·
   มุมเงยสองจุดสังเกต (8) · sin x + cos x = ค่าคงที่ (25) · มุมสองเท่าไปข้างหน้า (25)
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
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:110]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# ── W1 · โดเมนของฟังก์ชันผกผันที่อาร์กิวเมนต์เชิงเส้น ────────────────────────
scan('W1a · คำถามถาม "โดเมน" ของฟังก์ชันที่มี arc', r'โดเมน.{0,90}(arc|\^\{-1\})', qonly=True, show=20)
scan('W1b · คำถามมี arcsin (ทุกแบบ)', r'\\arcsin|\\sin\^\{-1\}', qonly=True, show=20)
scan('W1c · arc ที่อาร์กิวเมนต์เป็น ax+b (มีเครื่องหมายบวก/ลบในวงเล็บ)',
     r'\\arc(sin|cos|tan)\s*\\?l?e?f?t?\(\s*[\d\\a-z]{1,12}\s*[-+]', qonly=True, show=20)
scan('W1d · คำว่า "โดเมน" ทั้งคลังบทตรีโกณ', r'โดเมน', qonly=True, show=20)

# ── W2 · ยุบนิพจน์เอกลักษณ์ให้เป็นค่าคงที่ ───────────────────────────────────
scan('W2a · คำถามสั่ง "ยุบ/ทำให้อยู่ในรูปอย่างง่าย/เท่ากับข้อใด"',
     r'อย่างง่าย|ยุบ|มีค่าเท่ากับข้อใด|เท่ากับข้อใดต่อไปนี้', qonly=True, show=20)
scan('W2b · นิพจน์ที่มี sec^2 หรือ csc^2 ในคำถาม', r'\\sec\^\{?2|\\csc\^\{?2', qonly=True, show=20)
scan('W2c · รูปผลคูณผลต่างกำลังสอง (1-sin)(1+sin) หรือคล้ายกัน',
     r'\(\s*1\s*[-+]\s*\\(sin|cos)[^)]{0,12}\)\s*\\?l?e?f?t?\(\s*1\s*[-+]\s*\\(sin|cos)',
     qonly=True, show=20)

# ── W3 · tan x + cot x = k ───────────────────────────────────────────────────
scan('W3a · คำถามมี tan และ cot ของมุมเดียวกันบวกกัน',
     r'\\tan[^$]{0,20}\+[^$]{0,10}\\cot|\\cot[^$]{0,20}\+[^$]{0,10}\\tan', qonly=True, show=20)
scan('W3b · คำว่า cot ในคำถามทั้งคลัง', r'\\cot', qonly=True, show=20)
scan('W3c · สมการที่ยุบไปเป็น sin 2x (ในเฉลย)', r'\\sin\s*2\s*x\s*=', show=20)

# ── W4 · พื้นที่เซกเมนต์ ─────────────────────────────────────────────────────
scan('W4a · คำว่า "เซกเมนต์" ทั้งคลัง', r'เซกเมนต์|เซ็กเมนต์', show=20)
scan('W4b · "พื้นที่ส่วนที่แรเงา" ในบทตรีโกณ', r'แรเงา|ระบายสี|ส่วนที่เหลือของวงกลม', show=20)
scan('W4c · เซกเตอร์ + สามเหลี่ยม ในคำถามเดียวกัน',
     r'เซกเตอร์[^$]{0,80}สามเหลี่ยม|สามเหลี่ยม[^$]{0,80}เซกเตอร์', qonly=True, show=20)
scan('W4d · สูตร r^2(theta - sin theta)/2 ในเฉลย',
     r'\\theta\s*-\s*\\sin\s*\\theta|\\alpha\s*-\s*\\sin\s*\\alpha', show=20)
scan('W4e · คำว่า "คอร์ด/เส้นตรงตัดวงกลม" ในบทตรีโกณ', r'คอร์ด|เส้นตรงตัดวงกลม', show=20)

# ── W5 · sin x + sin y = a และ cos x + cos y = b ─────────────────────────────
scan('W5a · คำถามให้ผลบวกของไซน์สองมุมต่างกัน',
     r'\\sin\s*[xA]\s*\+\s*\\sin\s*[yB]|\\sin\s*A\s*\+\s*\\sin\s*B', qonly=True, show=20)
scan('W5b · คำถามให้ผลบวกของโคไซน์สองมุมต่างกัน',
     r'\\cos\s*[xA]\s*\+\s*\\cos\s*[yB]|\\cos\s*A\s*\+\s*\\cos\s*B', qonly=True, show=20)
scan('W5c · สูตรผลบวกเป็นผลคูณ (sum-to-product) ในเฉลย',
     r'2\s*\\sin\s*\\?l?e?f?t?\\?d?frac\{[^}]*\+[^}]*\}\{2\}|ผลบวกเป็นผลคูณ|sum-to-product', show=20)
scan('W5d · คำถามถาม cos(x-y) หรือ cos(A-B)',
     r'\\cos\s*\\?l?e?f?t?\(\s*[xA]\s*-\s*[yB]\s*\\?r?i?g?h?t?\)', qonly=True, show=20)
scan('W5e · คำถามถาม tan((x+y)/2) หรือครึ่งของผลบวกมุม',
     r'\\tan\s*\\?l?e?f?t?\(?\s*\\?d?frac\{\s*[xA]\s*\+\s*[yB]\s*\}\{\s*2\s*\}', qonly=True, show=20)

# ── W6 · เดินเรือ/บอกทิศ (สำรอง) ─────────────────────────────────────────────
scan('W6a · คำบอกทิศแบบเดินเรือ', r'ทิศเหนือ|ทิศใต้|ทิศตะวันออก|ทิศตะวันตก|N\s*\d+|S\s*\d+', show=20)
scan('W6b · คำว่า "เรือ/แล่น/ออกเดินทาง" ในบทตรีโกณ', r'เรือ|แล่น|ออกเดินทาง', show=20)

# ── W7 · อัตราส่วนมุมแหลม (สำรอง · คาดว่าชนหนัก) ─────────────────────────────
scan('W7a · "มุมแหลม" + ให้ค่าอัตราส่วนหนึ่ง', r'มุมแหลม', qonly=True, show=20)

# ── สำมะโนหัวข้อย่อยฝั่งเรา เพื่อยืนยันโควตา ────────────────────────────────
print()
print('== สำมะโนหัวข้อย่อยของข้อที่เราแต่งเอง ==')
cnt, lv = {}, {}
for q in items:
    if not q['id'].startswith('gen-chap-07'):
        continue
    for s in (q.get('subTopics') or []):
        cnt[s] = cnt.get(s, 0) + 1
    lv[q.get('difficulty')] = lv.get(q.get('difficulty'), 0) + 1
for k in sorted(cnt):
    print('   %-6s %d' % (k, cnt[k]))
print('   ระดับ:', lv)

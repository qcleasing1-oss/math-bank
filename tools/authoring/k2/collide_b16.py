# -*- coding: utf-8 -*-
"""กวาดชนก้อน 16 · รอบ 1

โควตาที่ก้อนนี้ต้องทำให้ได้ (จาก audit44 หลังก้อน 15 + คำสั่ง ④)
  · ง่าย 1 · ปานกลาง 2 · ยาก 1 · ยากมาก 1
  · เลี่ยงเป็น "แกนหลัก": 7.2 (20) · 7.3 (17) · 7.9 (12)
  ⇒ เล็ง 7.8 (5 · บางสุด) · 7.10 (8) · 7.5 · 7.6 · 7.7 · 7.11 (อย่างละ 9)

แบบร่างที่ยิงรอบนี้
  R1 ง่าย   7.8  · เรนจ์ของ a·arccos x + b (ช่วงค่าหลักเป็นความรู้ก้อนเดียว)
  R2 ปกลาง  7.10 · เข็มนาฬิกาสองเข็ม ⇒ ระยะระหว่างปลายเข็ม (กฎโคไซน์)
  R3 ปกลาง  7.6  · ให้ tan(theta/2) ⇒ หา sin theta + cos theta (แทนที่แบบไวเออร์ชตราสส์)
  R4 ยาก    7.7  · cos 2x + b sin x = c ⇒ กำลังสองใน sin ⇒ ถาม "คำตอบที่มากที่สุด"
  R5 ยากมาก 7.9  · กรณีกำกวม SSA (สองรูปสามเหลี่ยม) ⇒ ผลต่างของด้านที่สาม
  R6 ยากมาก 7.11 · เซกเตอร์ที่เส้นรอบรูปคงที่ ⇒ พื้นที่มากสุด (สำรอง · เคยยิงในรอบ b15)
  R7 ง่าย   7.8  · โดเมนของ arcsin(ax+b) (สำรองของ R1)

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

# ── R1 · เรนจ์ของฟังก์ชันผกผันเชิงเส้น ────────────────────────────────────────
scan('R1a · คำถามถาม "เรนจ์/พิสัย" ของฟังก์ชันที่มี arccos/arcsin/arctan',
     r'(เรนจ์|พิสัย|ช่วงของค่า).{0,80}(arc|\^\{-1\})', qonly=True, show=20)
scan('R1b · ทุกข้อที่คำถามมี arccos', r'\\arccos|\\cos\^\{-1\}', qonly=True, show=20)
scan('R1c · a·arccos x + b (มีสัมประสิทธิ์หน้า arc)',
     r'\d\s*\\arccos|\d\s*\\arcsin|\d\s*\\arctan', qonly=True, show=20)

# ── R2 · เข็มนาฬิกา ⇒ ระยะปลายเข็ม ───────────────────────────────────────────
scan('R2a · คำว่า "นาฬิกา" ทั้งคลัง (ไม่กรองบท)', r'นาฬิกา', show=20)
scan('R2b · "เข็มสั้น/เข็มยาว/เข็มชั่วโมง/เข็มนาที"', r'เข็ม(สั้น|ยาว|ชั่วโมง|นาที)', show=20)

# ── R3 · แทนที่ครึ่งมุม (ไวเออร์ชตราสส์) ─────────────────────────────────────
scan('R3a · คำถามให้ค่า tan(theta/2) หรือ tan(x/2) มา',
     r'\\tan\s*\\?l?e?f?t?\(?\s*\\d?frac\{[^}]*\}\{2\}|\\tan\s*\\d?frac\{[^}]*\}\{2\}',
     qonly=True, show=20)
scan('R3b · คำว่า "ครึ่งมุม" ทั้งคลัง', r'ครึ่งมุม', show=20)
scan('R3c · คำถามถาม sin theta + cos theta (ผลบวกของสองฟังก์ชันมุมเดียว)',
     r'\\sin\s*\\theta\s*\+\s*\\cos\s*\\theta|\\cos\s*\\theta\s*\+\s*\\sin\s*\\theta|'
     r'\\sin\s*A\s*\+\s*\\cos\s*A|\\sin\s*x\s*\+\s*\\cos\s*x', qonly=True, show=20)

# ── R4 · cos 2x + b sin x = c ⇒ กำลังสองใน sin ──────────────────────────────
scan('R4a · คำถามมี cos 2x ร่วมกับ sin x ในสมการเดียว',
     r'\\cos\s*2\s*[xA\\theta][^$]{0,40}\\sin\s*[xA\\theta]|'
     r'\\sin\s*[xA\\theta][^$]{0,40}\\cos\s*2\s*[xA\\theta]', qonly=True, show=20)
scan('R4b · คำถามถาม "คำตอบที่มากที่สุด/ค่ามากที่สุดของ x"',
     r'(คำตอบ|ค่าของ\s*\$?x).{0,25}มากที่สุด|มากที่สุด.{0,20}(ที่สอดคล้อง|ของสมการ)',
     qonly=True, show=20)

# ── R5 · กรณีกำกวม SSA ⇒ สองรูปสามเหลี่ยม ───────────────────────────────────
scan('R5a · คำว่า "สองรูป/ได้สองรูป/เป็นไปได้สองแบบ" ในบทตรีโกณ',
     r'สองรูป|ได้\s*2\s*รูป|เป็นไปได้สองแบบ|สองกรณี', show=20)
scan('R5b · คำว่า "ผลต่างของ" ในบทตรีโกณ (ถามผลต่างของสองค่า)',
     r'ผลต่างของ', qonly=True, show=20)
scan('R5c · คำว่า "กำกวม" ทั้งคลัง', r'กำกวม', show=14)

# ── R6 · เซกเตอร์เส้นรอบรูปคงที่ ⇒ พื้นที่มากสุด ────────────────────────────
scan('R6a · เซกเตอร์ + เส้นรอบรูป/ความยาวรอบ',
     r'เส้นรอบ.{0,30}เซกเตอร์|เซกเตอร์.{0,40}เส้นรอบ|'
     r'ความยาวรอบ.{0,30}เซกเตอร์|เซกเตอร์.{0,40}ความยาวรอบ', show=14)

# ── R7 · โดเมนของ arcsin เชิงเส้น ───────────────────────────────────────────
scan('R7a · คำถามถาม "โดเมน" ของฟังก์ชันที่มี arc',
     r'โดเมน.{0,80}(arc|\^\{-1\})', qonly=True, show=20)

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

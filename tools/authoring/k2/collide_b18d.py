# -*- coding: utf-8 -*-
"""กวาดชนก้อน 18 · รอบ 4 — เหลือช่องเดียว (ง่าย 1 ช่อง)

⛔ ที่ตายในรอบ 3
   R1 (ง่าย 7.8 · โดเมนของ arcsin(3x-1)) — ไม่ตายแบบ ❌ เต็มสามส่วน แต่ **แน่นเกินไป**
      · gen-chap-07-trigonometry-q052 (ของเราเอง) = โดเมนของ arcsin(x^2 - 2x)  ⇒ A ตรง · M ตรง
      · gen-chap-07-trigonometry-q067 (ของเราเอง) = arccos((n+4)/6) หาค่าได้กี่จำนวน ⇒ M ตรง
      · samn-2561-03-q04 = arccos(9x^2) + arcsin(6x-1) ⇒ อาร์กิวเมนต์เชิงเส้นมีของแล้ว
      ⇒ ป้ายจะเป็น ⚠️ WATCH-A ทันทีที่ลงทะเบียน และข้อ "ง่าย" ไม่มีที่ให้ขยับหนี
      ⇒ **ทิ้งหัวข้อ 7.8 ทั้งช่องในก้อนนี้** — ยืนยันบทเรียนรอบ 2 อีกครั้ง :
        7.8 บางเฉพาะในชุดเรา (6 ข้อ) แต่คลังเดิมอัดแน่น ⇒ ตัวเลขของเราไม่ใช่หลักฐานว่ามีที่ว่าง

✅ ที่ผ่านเพิ่มในรอบ 3 (2 ข้อ)
   R2 ปกลาง 7.10 · หลังคาทรงจั่ว (R2a 2 ข้อคนละเรื่อง · R2b=0 · R2c=0)
      (pat1-2565-03-q11 เป็นแผงโซลาร์บนหลังคา — ให้ขาตั้งสองข้าง ไม่ใช่เรขาคณิตโครงจั่ว)
   R3 ปกลาง 7.6  · sin2t/(1+cos2t) เมื่อให้ sin t + จตุภาค (R3a=0 · R3b 1 ข้อเป็นลิมิต · R3c 1 ข้อเป็นสมการ)

ตัวแทนที่ยิงรอบนี้ (ต้องได้ ง่าย 1)
  S1 ง่าย 7.11 · ให้ความยาวส่วนโค้ง + รัศมี ⇒ พื้นที่เซกเตอร์ (ใช้ A = 1/2 * r * s)
  S2 ง่าย 7.4  · (สำรอง) ทำให้อยู่ในรูปอย่างง่าย : (sec^2 t - 1) cot t
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

# ── S1 · พื้นที่เซกเตอร์จากความยาวส่วนโค้ง + รัศมี ─────────────────────────
scan('S1a  คำถามมีทั้ง ส่วนโค้ง และ เซกเตอร์/เสี้ยววงกลม',
     r'ส่วนโค้ง[\s\S]{0,200}(เซกเตอร์|เสี้ยววงกลม|ภาคตัดของวงกลม)|'
     r'(เซกเตอร์|เสี้ยววงกลม|ภาคตัดของวงกลม)[\s\S]{0,200}ส่วนโค้ง', qonly=True, show=12)
scan('S1b  คำถามให้ความยาวส่วนโค้งเป็นตัวเลขพร้อมหน่วย',
     r'ส่วนโค้ง[\s\S]{0,60}ยาว|ยาว[\s\S]{0,20}ส่วนโค้ง|ความยาวส่วนโค้ง[\s\S]{0,30}(เท่ากับ|เป็น|คือ)\s*\$?\d',
     qonly=True, show=12)
scan('S1c  คำถามถามพื้นที่เซกเตอร์ตรง ๆ',
     r'พื้นที่[\s\S]{0,40}(เซกเตอร์|เสี้ยววงกลม)', qonly=True, show=12)

# ── S2 · (สำรอง) ยุบนิพจน์เอกลักษณ์ sec^2 - 1 คูณ cot ─────────────────────
scan('S2a  นิพจน์ sec^2 ลบ 1', r'\\sec\^\{?2\}?[\s\S]{0,20}-\s*1', qonly=True, show=10)
scan('S2b  คำถามมี cot คูณกับกำลังสองของ tan/sec',
     r'\\cot[\s\S]{0,25}(\\tan\^|\\sec\^)|(\\tan\^|\\sec\^)[\s\S]{0,25}\\cot', qonly=True, show=10)
scan('S2c  คำถามสั่งทำให้อยู่ในรูปอย่างง่าย', r'รูปอย่างง่าย|เขียนให้อยู่ในรูป', qonly=True, show=10)

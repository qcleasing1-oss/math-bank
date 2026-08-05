# -*- coding: utf-8 -*-
"""กวาดชนก้อน 18 · รอบ 5 — ช่อง "ง่าย" ช่องสุดท้าย (ดื้อที่สุดในก้อนนี้)

⛔ ที่ตายในรอบ 4
   S1 (ง่าย 7.11 · ส่วนโค้ง+รัศมี ⇒ พื้นที่เซกเตอร์)
      · gen-chap-07-trigonometry-q030 (ของเราเอง · ง่าย 7.11) = รัศมี+มุมเรเดียน ⇒ พื้นที่เซกเตอร์ ⇒ A ตรง
      · gen-chap-07-trigonometry-q060 (ของเราเอง · ง่าย 7.11) = รัศมี+ส่วนโค้ง ⇒ มุม        ⇒ G ตรง
      ⇒ ลงทะเบียนแล้วจะได้ ⚠️ WATCH-A ทันที · ทิ้ง
   S2 (ง่าย 7.4 · (sec^2 t - 1)cot t)
      · pat1-2556-03-q28 ใช้ (1 + tan^2 x)cot x — โซ่เอกลักษณ์ชุดเดียวกันเป๊ะ (พีทาโกรัส ⇒ คูณ cot)
      ⇒ M ตรง · ทิ้ง

⭐ ข้อสรุปเชิงโครงสร้างที่ได้จากรอบ 3-4-5 (ควรบันทึกไว้ใช้ทุกก้อนต่อไป)
   "ง่าย" บังคับ L = 0 ⇒ ห้ามมีบริบท ⇒ เหลือแต่ข้อสูตรเปล่า
   ⇒ ข้อสูตรเปล่าคือของที่คลัง 6,407 ข้ออัดแน่นที่สุด
   ⇒ **ช่อง "ง่าย" แพงกว่าช่อง "ยากมาก" ในแง่การหาแม่พิมพ์ว่าง** (ยากมากมีบริบทให้เดินได้ไม่จำกัด)
   ⇒ วิธีแก้ที่ใช้ได้จริง : หาคู่ (สิ่งที่ให้ · สิ่งที่ถาม) ที่ "กลับทาง" จากของเดิม แทนที่จะหาเนื้อหาใหม่

ตัวแทนที่ยิงรอบนี้ (ต้องได้ ง่าย 1)
  S3 ง่าย 7.11 · รัศมี + มุมเป็น "องศา" ⇒ ความยาวส่วนโค้ง (ต้องแปลงหน่วยก่อน)
  S4 ง่าย 7.9  · สองด้านกับมุมระหว่างที่เป็นมุมป้าน ⇒ พื้นที่สามเหลี่ยม (1/2 ab sin C)
  S5 ง่าย 7.1  · ให้ tan ของมุมแหลม ⇒ ค่าของ sin + cos (สามเหลี่ยมอ้างอิง)
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

# ── S3 · ความยาวส่วนโค้งจากมุมเป็นองศา ─────────────────────────────────────
scan('S3a  คำถามถามความยาวส่วนโค้งตรง ๆ',
     r'(ความยาว|ยาว)[\s\S]{0,25}ส่วนโค้ง[\s\S]{0,60}(เท่าใด|กี่|ข้อใด)|'
     r'ส่วนโค้ง[\s\S]{0,40}ยาวกี่', qonly=True, show=12)
scan('S3b  คำถามมีมุมเป็นองศาคู่กับคำว่า เรเดียน (ต้องแปลงหน่วย)',
     r'องศา[\s\S]{0,200}เรเดียน|เรเดียน[\s\S]{0,200}องศา', qonly=True, show=12)
scan('S3c  คำถามมีคำว่า จุดศูนย์กลาง คู่กับ องศา',
     r'จุดศูนย์กลาง[\s\S]{0,120}องศา|องศา[\s\S]{0,120}จุดศูนย์กลาง', qonly=True, show=12)

# ── S4 · พื้นที่สามเหลี่ยมจากสองด้าน+มุมระหว่าง ────────────────────────────
scan('S4a  คำถามถามพื้นที่ของรูปสามเหลี่ยม',
     r'พื้นที่[\s\S]{0,40}(รูปสามเหลี่ยม|สามเหลี่ยม)', qonly=True, show=14)
scan('S4b  เฉลยใช้สูตร 1/2 ab sin C', r'\\dfrac\{1\}\{2\}\s*\\?[a-z]*\s*a\s*b\s*\\sin|'
     r'พื้นที่[\s\S]{0,40}=\s*\\dfrac\{1\}\{2\}[\s\S]{0,40}\\sin', show=14)

# ── S5 · sin + cos จาก tan ของมุมแหลม ──────────────────────────────────────
scan('S5a  คำถามถามผลบวก sin + cos', r'\\sin\s*\\?[a-zA-Z\\]{1,8}\s*\+\s*\\cos', qonly=True, show=14)
scan('S5b  คำถามให้ tan เป็นเศษส่วนแล้วมุมแหลม',
     r'\\tan\s*\\?[a-zA-Z\\]{1,8}\s*=\s*\\dfrac\{\d+\}\{\d+\}', qonly=True, show=14)

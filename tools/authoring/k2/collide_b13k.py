# -*- coding: utf-8 -*-
"""กวาดรอบ 11 ของก้อน 13 — หาแม่พิมพ์แทน q073 ที่ ⛔ ไม่ใช่ 7.9

เหตุที่ต้องเปลี่ยน (บันทึกไว้เป็นหลักฐาน)
  ดีไซน์ SSA คลุมเครือ (b = 8 · A = pi/6 · a = 5 ⇒ ผลบวก c = 8sqrt3) ตายเพราะ
  gen-chap-07-trigonometry-q053 ของเราเอง : มุม A = 30 องศา · CA = 8 · BC = k
  ใช้สมการเดียวกันเป๊ะ c^2 - 8sqrt3 c + (64 - k^2) = 0 และใช้ผลบวกราก = 8sqrt3
  เป็นตัวตรวจเหมือนกัน ⇒ G ตรง (SSA ที่ b = 8, A = 30) · M ตรง (สมการกำลังสอง
  ในด้าน + วีเอต) ต่างแค่ A ⇒ ⚠️ WATCH-A ของข้อเราเอง ⇒ ทิ้ง
  และ chap-07-trigonometry-q110 (ยาก · 7.9) ก็เป็น SSA สองกรณี ⇒ พื้นผิวแน่นอยู่แล้ว

ก้อน 13 ตอนนี้เป็น 7.9 สามข้อแล้ว (q070 · q072 · q074) ⇒ ตัวแทนต้อง ⛔ ไม่ใช่ 7.9
หัวข้อย่อยที่บางที่สุด : 7.8 = 4 · 7.7 = 5 · 7.10 = 5
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
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:100]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# ── Z1 · บันไดพาดกำแพงแล้วไถล (สองตำแหน่ง ความยาวบันไดคงที่) ────────────────
scan('Z1a · บันได/พาดกำแพง (ทุกสำนวน)', r'บันได|พาดกำแพง|พิงกำแพง|พาดผนัง')
scan('Z1b · ไถล/เลื่อนลง/ดึงปลายล่างออก ⇒ เทียบสองตำแหน่ง',
     r'ไถล|เลื่อนลง|เลื่อนออก|ดึงปลายล่าง|ปลายบน[\s\S]{0,60}?ลง|เดิม[\s\S]{0,40}?ทำมุม[\s\S]{0,60}?เหลือ')

# ── Z2 · เอกลักษณ์ arcsin x + arccos x = pi/2 ────────────────────────────────
scan('Z2a · arcsin + arccos ของตัวแปรเดียวกัน (เอกลักษณ์ pi/2)',
     r'\\arcsin[\s\S]{0,40}?\+[\s\S]{0,30}?\\arccos|\\arccos[\s\S]{0,40}?\+[\s\S]{0,30}?\\arcsin|'
     r'\\sin\^\{-1\}[\s\S]{0,40}?\+[\s\S]{0,30}?\\cos\^\{-1\}')
scan('Z2b · พูดถึงค่าคงตัว pi/2 ที่ได้จากผลบวกฟังก์ชันผกผัน',
     r'\\arcsin\s*x\s*\+\s*\\arccos\s*x|เท่ากับ\s*\$?\\dfrac\{\\pi\}\{2\}\$?\s*เสมอ')

# ── Z3 · พิสัย/ช่วงของฟังก์ชันประกอบที่มีตรีโกณผกผัน ────────────────────────
scan('Z3a · ถามพิสัย/ช่วงของค่า ของฟังก์ชันที่มี arc',
     r'พิสัย[\s\S]{0,120}?\\arc|\\arc[\s\S]{0,120}?พิสัย|ช่วงของค่า[\s\S]{0,120}?\\arc', show=14)
scan('Z3b · ค่าสูงสุด/ต่ำสุด ของนิพจน์ที่มีฟังก์ชันตรีโกณผกผัน',
     r'(?:มากที่สุด|น้อยที่สุด|สูงสุด|ต่ำสุด)[\s\S]{0,150}?\\arc|'
     r'\\arc[\s\S]{0,150}?(?:มากที่สุด|น้อยที่สุด|สูงสุด|ต่ำสุด)', show=14)

# ── Z4 · โดเมนของฟังก์ชันผกผัน (ต้องตัดช่วงจากเงื่อนไข -1 <= u <= 1) ────────
scan('Z4 · โดเมนของฟังก์ชันที่มี arcsin/arccos (ต้องแก้ -1 <= u <= 1)',
     r'โดเมน[\s\S]{0,120}?\\arc|\\arc[\s\S]{0,120}?โดเมน|-1\s*\\le[\s\S]{0,60}?\\le\s*1', show=14)

# ── Z5 · ของเราเองในหัวข้อ 7.8 ทั้งหมด ──────────────────────────────────────
print()
print('== Z5 · ข้อที่เราแต่งเองในหัวข้อ 7.8 ==')
for q in items:
    if q['id'].startswith('gen-chap-07') and '7.8' in (q.get('subTopics') or []):
        print('   %-32s %-8s %s' % (q['id'], q.get('difficulty'),
              (q.get('question') or '').replace('\n', ' ')[:120]))

print()
print('== Z6 · ข้อในคลังที่ติดป้าย 7.8 ==')
n = 0
for q in items:
    if not q['id'].startswith('gen-chap-07') and '7.8' in (q.get('subTopics') or []):
        n += 1
        if n <= 20:
            print('   %-32s %-8s %s' % (q['id'], q.get('difficulty'),
                  (q.get('question') or '').replace('\n', ' ')[:110]))
print('   รวม %d ข้อ' % n)

# -*- coding: utf-8 -*-
"""กวาดรอบ 14 — สองผู้สมัครสุดท้ายของช่อง q073 (ทั้งคู่เป็น 7.10 ซึ่งเป็นหัวข้อบาง = 5 ข้อ)

ผู้สมัคร A (ยาก) · เสาธงตั้งฉากกับพื้นราบที่ O · A, B บนพื้น · มุม AOB เป็นมุมฉาก
  มุมเงยยอดเสาจาก A = 45 องศา · จาก B = 30 องศา · AB = 24 ⇒ ความสูงเสา
  OA = h · OB = h sqrt3 · AB^2 = h^2 + 3h^2 = 4h^2 ⇒ h = 12
  ⚠️ จุดตาย : พื้นผิว "มุมเงย" แน่นมากในคลัง ต้องดูว่ารูปทรงสามมิติ (มุมบนพื้นราบ) ว่างจริงไหม

ผู้สมัคร B (ปานกลาง) · บันไดพาดกำแพงสองตำแหน่ง ความยาวบันไดคงที่
  ทำมุม 60 องศา ⇒ ดึงปลายล่างออกจนเหลือ 45 องศา ⇒ ฐานเลื่อนออก 3 เมตร ⇒ หาความยาวบันได
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
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:105]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# ── ผู้สมัคร A · เสา/หอ สามมิติ : จุดสังเกตสองจุดที่ ⛔ ไม่อยู่ในแนวเดียวกัน ──
scan('A1 · มุมเงยจากสองจุดบนพื้นราบที่ทำมุมกันที่ฐาน (รูปทรงสามมิติ)',
     r'มุม\s*\$?A\\?hat\{?O\}?B|มุม\s*AOB|ทำมุม[\s\S]{0,60}?ที่ฐานเสา|'
     r'บนพื้นราบ[\s\S]{0,120}?มุมเงย[\s\S]{0,120}?มุมเงย', show=14)
scan('A2 · มุมเงยสองค่าจากสองจุด (ทุกสำนวน — ดูความหนาแน่นของพื้นผิว)',
     r'มุมเงย[\s\S]{0,200}?มุมเงย', show=16)
scan('A3 · เสาธง/เสาไฟ/หอคอย + ตั้งฉากกับพื้นราบ',
     r'เสาธง|เสาไฟ|หอคอย|เสาโทรทัศน์|ตั้งฉากกับพื้นราบ|ตั้งอยู่บนพื้นราบ', show=16)
scan('A4 · ลายเซ็นเชิงตัวเลขของผู้สมัคร A (45 กับ 30 องศา พร้อมกัน + มุมฉากที่ฐาน)',
     r'45\^?\{?\\?circ[\s\S]{0,140}?30\^?\{?\\?circ[\s\S]{0,140}?(?:มุมฉาก|90\^?\{?\\?circ)',
     qonly=True, show=14)

# ── ผู้สมัคร B · บันไดพาดกำแพง ───────────────────────────────────────────────
scan('B1 · บันได/ไม้/เสา พาดกับกำแพงหรือผนัง (ยิงตรงทุกสำนวน)',
     r'บันได[\s\S]{0,80}?(?:กำแพง|ผนัง|ฝา)|(?:กำแพง|ผนัง)[\s\S]{0,80}?บันได|'
     r'พาด(?:อยู่)?(?:กับ|บน)?\s*(?:กำแพง|ผนัง)', show=14)
scan('B2 · วัตถุยาวคงที่ที่เปลี่ยนมุมเอียงสองตำแหน่ง ⇒ หาความยาว',
     r'เดิมทำมุม[\s\S]{0,100}?เหลือ|จากเดิม[\s\S]{0,80}?องศา[\s\S]{0,80}?เป็น[\s\S]{0,40}?องศา|'
     r'ปลายล่าง[\s\S]{0,100}?ออกไป', show=14)
scan('B3 · ฐานเลื่อนออก/ปลายบนเลื่อนลง เป็นระยะที่กำหนด',
     r'เลื่อนออกไป[\s\S]{0,60}?เมตร|ห่างจากกำแพง[\s\S]{0,60}?เมตร|เลื่อนลงมา[\s\S]{0,60}?เมตร',
     show=14)

# ── ความหนาแน่นของ 7.10 ทั้งหมด (ของเราเอง) ────────────────────────────────
print()
print('== C1 · ข้อที่เราแต่งเองในหัวข้อ 7.10 ==')
for q in items:
    if q['id'].startswith('gen-chap-07') and '7.10' in (q.get('subTopics') or []):
        print('   %-32s %-8s %-12s %s' % (q['id'], q.get('difficulty'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:130]))

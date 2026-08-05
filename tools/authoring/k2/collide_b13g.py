# -*- coding: utf-8 -*-
"""กวาดรอบเจ็ด — คัดผู้ท้าชิงตำแหน่ง "ข้อยาก" ของก้อน 13
เป้าหัวข้อย่อยที่บางที่สุด : 7.8 = 4 · 7.7 = 5 · 7.10 = 5
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

scan('W1 · ระบบสมการสองตัวแปร sin x + sin y / cos x + cos y ⇒ ถาม cos(x-y)',
     r'\\sin\s*x\s*\+\s*\\sin\s*y|\\cos\s*x\s*\+\s*\\cos\s*y|\\cos\s*\(\s*x\s*-\s*y\s*\)')
scan('W2 · ให้ sin x + cos x = c ⇒ ถามนิพจน์สมมาตรอื่น (sin^3+cos^3 · tan+cot)',
     r'\\sin\s*x\s*\+\s*\\cos\s*x\s*=|\\sin\s*\\theta\s*\+\s*\\cos\s*\\theta\s*=|'
     r'\\sin\^\{?3\}?[\s\S]{0,20}?\+[\s\S]{0,10}?\\cos\^\{?3\}?')
scan('W3 · บันได/เสาพิงกำแพง มีกล่องหรือรั้วขวาง',
     r'บันได|พิงกำแพง|พิงผนัง|รั้ว[\s\S]{0,60}?กำแพง|เสา[\s\S]{0,40}?เอน')
scan('W4 · เงาของวัตถุ / ความยาวเงา + มุมของดวงอาทิตย์',
     r'เงาของ|ความยาวเงา|เงายาว|แสงอาทิตย์ทำมุม')
scan('W5 · ทางลาด / ความชันเป็นมุม / ไต่ระดับ',
     r'ทางลาด|ลาดเอียง|ทำมุม[\s\S]{0,40}?กับแนวราบ[\s\S]{0,60}?ปีน|ไต่ขึ้นไป')
scan('W6 · ค่าสูงสุด/ต่ำสุดของนิพจน์ที่ยุบเป็นกำลังสองของ cos หรือ sin (ยิงกว้าง)',
     r'(?:ค่าสูงสุด|ค่าต่ำสุด|ค่ามากที่สุด|ค่าน้อยที่สุด)[\s\S]{0,140}?\\(?:sin|cos)\^\{?2\}?|'
     r'\\(?:sin|cos)\^\{?2\}?[\s\S]{0,140}?(?:ค่าสูงสุด|ค่าต่ำสุด)', qonly=True, show=14)
scan('W7 · ถามคำตอบที่มากที่สุด/น้อยที่สุดของสมการตรีโกณในช่วง',
     r'คำตอบที่มากที่สุด|คำตอบที่น้อยที่สุด|ค่ามากที่สุดของ\s*\$?x\$?\s*ที่สอดคล้อง|'
     r'ค่าน้อยที่สุดของ\s*\$?x\$?\s*ที่สอดคล้อง', show=14)
scan('W8 · arccos/arcsin ของนิพจน์ที่ต้องเช็คพิสัยก่อน (ค่าหลัก)',
     r'ค่าหลัก|พิสัย[\s\S]{0,40}?\\arc|\\arcsin\left\(\\sin|\\arccos\\left\(\\cos|'
     r'\\arctan\\left\(\\tan', show=14)
scan('W9 · สมการที่มี sec/csc/cot ผสม (ไม่ใช่แค่ sin cos tan)',
     r'\\sec\s*\^?\{?\d?\}?\s*x[\s\S]{0,60}?=|\\csc[\s\S]{0,60}?=|\\cot\s*x[\s\S]{0,40}?=',
     qonly=True, show=14)
scan('W10 · มุมเงย/มุมก้ม (ดูว่าอิ่มตัวแค่ไหน)',
     r'มุมเงย|มุมก้ม', show=6)

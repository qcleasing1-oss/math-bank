# -*- coding: utf-8 -*-
"""กวาดชนก้อน 15 · รอบ 4 — เฉพาะ q080 หลังทะเบียนแม่พิมพ์เตือน WATCH-B สองคู่

เหตุ: แบบร่างเดิม (1 - 2 sin^2 75 องศา ⇒ cos 150) แม้โพรบถ้อยคำจะได้ 0 ข้อ
      แต่ทะเบียนชี้ว่า G+A ตรงกับ q012 และ q016 ของเราเอง และ q016 ใช้มุม 75 องศา
      เหมือนกันเป๊ะ ⇒ ต่างกันแค่แกน "ตัวเลข" แกนเดียว ผิดเจตนาของกฎเหล็กข้อ 5
      จึงต้องเปลี่ยน G (สิ่งที่โจทย์ให้) ไม่ใช่แค่เปลี่ยนเอกลักษณ์
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
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:104]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

scan('M1 · ให้ sin/cos เป็นเศษส่วน แล้วถามหา sin 2t (มุมสองเท่าไปข้างหน้า)',
     r'\\sin\s*2\s*\\?theta|\\sin\s*2\s*[A-Za-z]\b', qonly=True, show=16)
scan('M2 · ให้ cos 2t เป็นค่า แล้วถามย้อนกลับหา sin t หรือ cos t',
     r'\\cos\s*2\s*\\?t?h?e?t?a?[A-Za-z]?\s*=\s*[^$]{0,18}\$', qonly=True, show=16)
scan('M3 · ให้ tan t แล้วถาม tan 2t',
     r'\\tan\s*2\s*\\?theta|\\tan\s*2\s*[A-Za-z]\b', qonly=True, show=16)
scan('M4 · ให้ค่า sec หรือ csc แล้วถามฟังก์ชันของมุมสองเท่า',
     r'(\\sec|\\csc)[^$]{0,30}=[^$]{0,40}\$[^$]{0,60}(\\sin|\\cos|\\tan)\s*2', qonly=True, show=16)
scan('M5 · โจทย์ให้ "จุดบนวงกลมหนึ่งหน่วย" แล้วถามฟังก์ชันของมุมสองเท่า',
     r'(?s)วงกลมหนึ่งหน่วย.{0,220}(\\sin|\\cos|\\tan)\s*2', qonly=True, show=16)

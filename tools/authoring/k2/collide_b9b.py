# -*- coding: utf-8 -*-
"""กวาดรอบสอง — เจาะแม่พิมพ์ที่คิดไว้ 5 อัน หลังพบว่า 7.8 ในคลังหนามาก (75 ข้อ)

สิ่งที่รอบแรกบอก: แม่พิมพ์ “คิดค่าของนิพจน์ arc ซ้อน” และ “ผลบวก arctan” อิ่มตัวแล้ว
⇒ ต้องหาแม่พิมพ์ที่ถามคนละคำถาม ไม่ใช่แค่เปลี่ยนตัวเลข
"""
import io, json, glob, re, collections

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


def scan(label, pattern, qonly=False, show=8):
    rx = re.compile(pattern)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('══ %s ══  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-30s %-8s %-12s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:100]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# q050 · ค่าสุดขีดของฟังก์ชันที่สร้างจาก arc  (กำลังสองของ arcsin/arccos)
scan('q050 · (arcsin)^2 หรือ (arccos)^2 · ค่าสุดขีด',
     r'\\arcsin[^\n]{0,30}\)\s*\^\s*\{?2|\\arccos[^\n]{0,30}\)\s*\^\s*\{?2'
     r'|\\arcsin\^2|\\arccos\^2|\\sin\^\{-1\}[^\n]{0,20}\)\^2')
scan('q050b · ถามค่าสุดขีดของฟังก์ชันที่มี arc อยู่ด้วย',
     r'(?:arcsin|arccos|arctan)[\s\S]{0,400}?(?:ค่าสูงสุด|ค่าต่ำสุด|ค่ามากที่สุด|ค่าน้อยที่สุด)', qonly=True)

# q051 · เรียงลำดับค่าของ arc
scan('q051 · เรียงลำดับ/เปรียบเทียบค่าของ arc',
     r'(?:arcsin|arccos|arctan|\\sin\^\{-1\})[\s\S]{0,300}?(?:เรียงลำดับ|จากน้อยไปมาก|จากมากไปน้อย|ข้อใดเรียง)',
     qonly=True)

# q052 · โดเมน/เรนจ์ของฟังก์ชันประกอบที่มี arc
scan('q052 · โดเมนหรือเรนจ์ของฟังก์ชันที่มี arc',
     r'(?:arcsin|arccos|arctan|\\sin\^\{-1\}|\\cos\^\{-1\})[\s\S]{0,250}?(?:โดเมนของ|เรนจ์ของ)', qonly=True)

# q053 · กฎไซน์กรณีกำกวม SSA จริง ๆ (สองด้านกับมุมที่ไม่ประกบ)
scan('q053 · SSA · รูปสามเหลี่ยมที่เป็นไปได้สองรูป',
     r'สามเหลี่ยม[\s\S]{0,200}?(?:ได้กี่รูป|เป็นไปได้กี่|มีกี่รูป|สองรูป)', qonly=True)
scan('q053b · นับจำนวนรูปสามเหลี่ยมที่สร้างได้', r'จำนวนรูปสามเหลี่ยม|สร้างรูปสามเหลี่ยมได้')

# q054 · พื้นที่สามเหลี่ยมด้วย 1/2 ab sin C ผสมกฎโคไซน์
scan('q054 · พื้นที่สามเหลี่ยมจากสองด้านกับมุมประกบ',
     r'พื้นที่[\s\S]{0,160}?สามเหลี่ยม|สามเหลี่ยม[\s\S]{0,160}?พื้นที่', qonly=True, show=10)

# q054b · รูปสี่เหลี่ยมที่ต้องแบ่งเป็นสองสามเหลี่ยมแล้วใช้กฎโคไซน์สองรอบ
scan('q054b · สี่เหลี่ยมแบ่งเป็นสองสามเหลี่ยม (กฎโคไซน์สองรอบ)',
     r'สี่เหลี่ยม[\s\S]{0,200}?(?:กฎของโคไซน์|law of cosines)|รูปสี่เหลี่ยม[A-Z]{4}')
scan('q054c · สี่เหลี่ยมที่แนบในวงกลม (มุมตรงข้ามรวม 180)',
     r'แนบในวงกลม|วงกลมล้อมรอบ|cyclic quadrilateral|มุมตรงข้ามรวมกันได้ \$?180')

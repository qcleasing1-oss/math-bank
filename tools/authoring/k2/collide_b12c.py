# -*- coding: utf-8 -*-
"""กวาดรอบสามของก้อน 12 — ยิงตรงที่ "ห้าข้อที่จะแต่งจริง" ทีละข้อ (ไม่กรองบท)

รอบ 1–2 ให้ผลว่าแม่พิมพ์เหล่านี้ว่าง แต่ทั้งสองรอบยังกวาดแบบกว้าง
รอบนี้กวาดด้วยถ้อยคำ/สมการที่ข้อจริงจะใช้ และ **ไม่กรองบท** เพื่อกันการชนข้ามบท
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


def scan(label, pattern, qonly=False, show=8):
    rx = re.compile(pattern)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-30s %-8s %-12s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:105]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# q065 · sec - tan (หรือ csc - cot) ในสามเหลี่ยมมุมฉาก
scan('q065a · นิพจน์ sec − tan / csc − cot',
     r'\\sec[\s\S]{0,25}?-\s*\\tan|\\csc[\s\S]{0,25}?-\s*\\cot|'
     r'\\sec[\s\S]{0,25}?\+\s*\\tan|\\csc[\s\S]{0,25}?\+\s*\\cot')
scan('q065b · สามเหลี่ยมมุมฉากที่ให้ด้านประกอบมุมฉากสองด้าน 5 กับ 12',
     r'(?:5[\s\S]{0,60}?12|12[\s\S]{0,60}?5)[\s\S]{0,80}?(?:มุมฉาก|13)', qonly=True)

# q066 · รอก/สายพาน สองวงเชื่อมกัน
scan('q066 · รอก/สายพาน/เฟือง สองวงเชื่อมกัน ⇒ รอบต่อนาที',
     r'รอก|สายพาน|เฟือง|รอบต่อนาที|รอบ/นาที|ล้อ(?:ใหญ่|เล็ก)')

# q067 · นับจำนวนเต็มที่ทำให้ arcsin/arccos นิยามได้
scan('q067a · "นิยามได้" ของฟังก์ชันผกผัน',
     r'(?:\\arcsin|\\arccos|\\arctan|\\sin\^\{-1\}|\\cos\^\{-1\})[\s\S]{0,120}?'
     r'(?:นิยามได้|หาค่าได้|เป็นจำนวนจริง|อยู่ในโดเมน)')
scan('q067b · ถาม "จำนวนเต็ม n ทั้งหมดกี่จำนวน" ที่ผูกกับตรีโกณ',
     r'จำนวนเต็ม[\s\S]{0,120}?กี่จำนวน[\s\S]{0,200}?(?:\\sin|\\cos|\\tan|\\arcsin|\\arccos)|'
     r'(?:\\arcsin|\\arccos)[\s\S]{0,200}?จำนวนเต็ม[\s\S]{0,80}?กี่', qonly=True)

# q068 · ให้ค่าสูงสุด+ต่ำสุด+คาบ ⇒ ถอดสัมประสิทธิ์
scan('q068a · ให้ทั้งค่าสูงสุด ค่าต่ำสุด และคาบ ของฟังก์ชันตรีโกณ',
     r'ค่าสูงสุด[\s\S]{0,200}?ค่าต่ำสุด[\s\S]{0,250}?คาบ|คาบ[\s\S]{0,200}?ค่าสูงสุด[\s\S]{0,200}?ค่าต่ำสุด',
     qonly=True)
scan('q068b · ถามผลรวมของสัมประสิทธิ์ a+b+c ของฟังก์ชันตรีโกณ',
     r'(?:a\s*\+\s*b\s*\+\s*c|a\+b\+c)[\s\S]{0,200}?(?:\\sin|\\cos)|'
     r'(?:\\sin|\\cos)[\s\S]{0,250}?(?:a\s*\+\s*b\s*\+\s*c)', qonly=True)

# q069 · ช่วงของเส้นรอบรูปสามเหลี่ยม เมื่อรู้ด้านหนึ่งกับมุมตรงข้าม
scan('q069a · เส้นรอบรูปของสามเหลี่ยม + ค่าสูงสุด/ช่วง',
     r'เส้นรอบรูป[\s\S]{0,200}?(?:สูงสุด|มากที่สุด|ช่วง|เป็นไปได้)|'
     r'(?:สูงสุด|มากที่สุด)[\s\S]{0,150}?เส้นรอบรูป')
scan('q069b · ใช้ b+c = 2R(sin B + sin C) แปลงเป็นผลคูณ',
     r'\\sin\s*B\s*\+\s*\\sin\s*C|\\sin\s*A\s*\+\s*\\sin\s*B[\s\S]{0,60}?\+\s*\\sin\s*C|'
     r'b\s*\+\s*c[\s\S]{0,120}?(?:สูงสุด|มากที่สุด|2R)')
scan('q069c · โจทย์ที่ให้ "ด้านหนึ่งกับมุมตรงข้ามด้านนั้น" แล้วถามค่าสุดขีด',
     r'(?:ด้านตรงข้ามมุม\s*\$?A|a\s*=\s*\d+)[\s\S]{0,200}?(?:สูงสุด|มากที่สุด|น้อยที่สุด|ต่ำสุด)',
     qonly=True)

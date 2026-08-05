# -*- coding: utf-8 -*-
"""กวาดรอบเก้า — ผู้ท้าชิงตำแหน่ง "ข้อยาก" ชุดที่สาม
⛔ ตายไปแล้วรอบแปด : W1/W11 ระบบ sin+sin กับ cos+cos (chap-07-q178 ตรงเป๊ะ)
                      W8a ค่าหลักของฟังก์ชันผกผันซ้อน (gen-q051 ของเราเอง)
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


def scan(label, pattern, qonly=False, show=12):
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

scan('X1 · หน้าปัดนาฬิกา / เข็มสั้น-เข็มยาว', r'นาฬิกา|เข็มสั้น|เข็มยาว|หน้าปัด')
scan('X2 · กังหันลม / ใบพัด / จานหมุน', r'กังหัน|ใบพัด|จานหมุน|เข็มทิศ')
scan('X3 · โครงหลังคา / จั่ว / เสาค้ำ', r'หลังคา|จั่ว|เสาค้ำ|โครงถัก')
scan('X4 · ให้เส้นมัธยฐานมาแล้วถามด้าน (ทิศกลับของ F2)',
     r'มัธยฐาน[\s\S]{0,80}?ยาว|ยาว[\s\S]{0,60}?มัธยฐาน|4m\^2|2b\^2\s*\+\s*2c\^2')
scan('X5 · ให้สามด้านเป็นตัวเลข ⇒ ถามพื้นที่ (ยิงกว้างสุด ไม่กรองบท)',
     r'พื้นที่ของรูปสามเหลี่ยม|พื้นที่สามเหลี่ยม[\s\S]{0,60}?ตารางหน่วย|'
     r'จงหาพื้นที่ของรูปสามเหลี่ยม', show=14)
scan('X6 · โจทย์ที่ให้ "ด้านสามด้านยาว a, b, c หน่วย" ตรง ๆ ในบท 7',
     r'ยาว\s*\$?\d+\$?\s*หน่วย[\s\S]{0,80}?ยาว\s*\$?\d+\$?\s*หน่วย[\s\S]{0,80}?ยาว\s*\$?\d+\$?\s*หน่วย',
     qonly=True, show=14)
scan('X7 · สามเหลี่ยมที่มีมุมหนึ่งเป็นสองเท่าของอีกมุม (กันชนกับ q006/samn-2556-01-q03)',
     r'สองเท่าของ(?:ขนาดของ)?มุม|มุม[\s\S]{0,20}?=\s*2[\s\S]{0,10}?มุม|2\\hat', show=14)
scan('X8 · รัศมีวงกลมล้อมรอบสามเหลี่ยม (circumradius) / a/sinA = 2R',
     r'วงกลมล้อมรอบ|2R|\\dfrac\{a\}\{\\sin A\}|รัศมีของวงกลมที่ล้อมรอบ', show=14)

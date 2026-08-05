# -*- coding: utf-8 -*-
"""กวาดชนก้อน 16 · รอบ 5 — ชี้ขาดแบบร่าง V1 (เส้นแบ่งครึ่งมุมในสามเหลี่ยม)

ผลรอบ 4 (out_b16d.txt) ตัดสินไปแล้ว
  ⛔ U10 (tan A + tan B + tan C = tan A tan B tan C) ถูกฆ่า — เนื้อเต็มของ q001 ของเราเอง
     คือ "tan A : tan B : tan C = 1 : 2 : 3 ⇒ sin^2 A + sin^2 B + sin^2 C" ซึ่ง **กุญแจ**
     คือเอกลักษณ์ตัวนี้เป๊ะ · และ chap-07-q164 ตัวเลือก 1/3 ก็เป็นตระกูลเอกลักษณ์เดียวกัน
  ⛔ V2 (จำนวนคำตอบในช่วงยาว) ถูกฆ่า — A "จำนวนคำตอบ" หนาแน่นมาก : q057 · q079 · q043
     ของเราเอง + samn-2565-03-q26 (4 sin 5theta = 3 ใน [0,3pi] กี่ตัว) + alvl1-2567-03-q15
     + chap-07-q144 ⇒ ทั้ง A และ M ซ้ำ
  ⛔ V3 (อสมการที่มี arc) ถูกฆ่า — q067 (นับจำนวนเต็ม n ที่ arccos((n+4)/6) หาค่าได้) และ
     q052 (โดเมนของ arcsin(x^2-2x)) ของเราเองกินพื้นที่ "หาช่วงที่อาร์กิวเมนต์อยู่ใน [-1,1]"
     ไปแล้วทั้งคู่ ⇒ M ซ้ำ
  ⛔ V4 (ล้อ/รอก/สายพาน) ถูกฆ่า — q066 ของเราเองคือ "รอกสองตัวคล้องสายพานเส้นเดียวกัน"
     (ปานกลาง · 7.11/7.10) ตรงทั้ง G และ M

  ✅ V1 ยังไม่พบตัวชน — V1a 42 ข้อเป็น "แบ่งครึ่งและตั้งฉาก" ของบทเรขาวิเคราะห์เกือบทั้งหมด
     ฝั่งบท 7 ที่ติดมาคือ q119/q120 (คอร์ดในวงกลมหนึ่งหน่วย) และ q208/q209 (ทางโค้งถนน)
     ⇒ ไม่มีข้อไหนถาม "ความยาวของเส้นแบ่งครึ่งมุมในสามเหลี่ยม"
     รอบนี้ปิดจุดเสี่ยงที่เหลือ : chap-07-q220 · chap-09-q98 · chap-07-q126 (เนื้อเต็ม)
     + กวาดสูตร 2bc cos(A/2)/(b+c) และการ "แบ่งพื้นที่สามเหลี่ยมออกเป็นสองรูป" ทั้งคลัง
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

BY = {q['id']: q for q in items}


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
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:130]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

for _id in ('chap-07-trigonometry-q220', 'chap-09-vector-q98', 'chap-07-trigonometry-q126'):
    q = BY.get(_id)
    print()
    print('== เนื้อเต็ม %s ==' % _id)
    if not q:
        print('   (ไม่พบ)')
        continue
    print('   หัวข้อ:', '/'.join(q.get('subTopics') or []), '· ระดับ', q.get('difficulty'))
    print('   โจทย์:', (q.get('question') or '')[:800])
    for i, c in enumerate(q.get('choices') or []):
        print('   ตัวเลือก %d: %s' % (i + 1, str(c)[:150]))

# ── กวาดสูตรเส้นแบ่งครึ่งมุมโดยตรง (ทั้งเฉลยด้วย) ────────────────────────────
scan('V1e · สูตร 2bc cos(A/2)/(b+c) หรือรูปแบบใกล้เคียงในเฉลย',
     r'2bc\s*\\cos|\\dfrac\{2bc|เส้นแบ่งครึ่งมุม|ตัวแบ่งครึ่งมุม', show=20)
scan('V1f · คำว่า "แบ่งครึ่งมุม" เฉพาะบทตรีโกณ (กรองด้วยรหัส)',
     r'แบ่งครึ่งมุม', show=25)
scan('V1g · แนวคิด "แบ่งสามเหลี่ยมออกเป็นสองรูปแล้วบวกพื้นที่"',
     r'พื้นที่[^\n]{0,40}(รวมกัน|บวกกัน)[^\n]{0,60}สามเหลี่ยม|'
     r'\[ABD\]|\[ACD\]|พื้นที่สามเหลี่ยม\s*ABD', show=20)
scan('V1h · คำถามที่ให้สองด้านประกบมุม 2pi/3 หรือ 120 องศา (ตัวเลขชนกันไหม)',
     r'(\\dfrac\{2\\pi\}\{3\}|120\^\{\\circ\}|120\^\\circ)', qonly=True, show=25)

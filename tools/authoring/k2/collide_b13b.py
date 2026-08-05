# -*- coding: utf-8 -*-
"""กวาดรอบสองของก้อน 13 — แคบลงมาที่ "ดีไซน์จริง" ไม่ใช่หัวข้อกว้าง

สิ่งที่รอบแรก (collide_b13.py) สรุปได้
  ✅ ว่างจริง : H2 ให้สามด้าน ⇒ พื้นที่ = 0 · U3 ด้านเป็นลำดับเรขาคณิต = 0
  ⚠️ เกือบว่าง : E4 มุมพิเศษล้วน = 1 · R3 สองสามเหลี่ยมมุมฉากใช้ด้านร่วม = 2 (หนึ่งคือ q063 ของเราเอง)
  ⛔ อิ่มตัว   : E1 43 · N2 54 · E2 55 · E3 13 · N3 11 · S4 9 · N1 6
  ⛔ N4 ระยะข้ามแม่น้ำ/รังวัด = ตันจริง — chap-07-q207 (ช่างสำรวจ AB ขนานริมฝั่ง)
     กับ chap-07-q219 (หาความกว้างลำน้ำ AC = 50) เป็นแม่พิมพ์เดียวกันเป๊ะ ⇒ ทิ้ง
  ⚠️ F2 เส้นมัธยฐาน 140 ข้อเป็นผลลวง — regex กว้างไปจนไปโดน "มัธยฐาน" ของสถิติ
     กับจุดกึ่งกลางของเรขาคณิตพิกัด ⇒ รอบนี้กวาดใหม่แบบล็อกบทที่ 7

รอบนี้กวาดดีไซน์ที่จ่อจะใช้จริง 12 แบบ
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


def is7(q):
    return any(s.startswith('7') for s in (q.get('subTopics') or [])) or '7' in (q.get('topics') or [])


def scan(label, pattern, qonly=False, show=8, only7=False):
    rx = re.compile(pattern)
    pool = [q for q in items if is7(q)] if only7 else items
    hit = [q for q in pool if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ%s' % (label, len(hit), ' (เฉพาะบท 7)' if only7 else ''))
    for q in hit[:show]:
        print('   %-30s %-8s %-12s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:100]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ · เฉพาะบท 7 = %d ข้อ' % (len(items), len([q for q in items if is7(q)])))

# ── F2 กวาดใหม่แบบล็อกบท 7 ───────────────────────────────────────────────────
scan('F2-แคบ · เส้นมัธยฐาน/จุดกึ่งกลางด้าน — ล็อกบท 7',
     r'มัธยฐาน|จุดกึ่งกลางของด้าน|จุดกึ่งกลางด้าน|จุดกึ่งกลาง', only7=True, show=14)

# ── ดีไซน์ที่จ่อใช้จริง ───────────────────────────────────────────────────────
scan('P4 · หาค่าตรงตัวของผลบวกฟังก์ชันผกผัน (arcsin/arccos/arctan ที่ค่าพิเศษ)',
     r'\\arcsin\s*\(?\s*-?\\?d|\\arccos[\s\S]{0,50}?\+[\s\S]{0,30}?\\arcsin|'
     r'\\arcsin[\s\S]{0,50}?\+[\s\S]{0,30}?\\arccos|\\arccos[\s\S]{0,40}?\+[\s\S]{0,30}?\\arctan',
     qonly=True, show=14)

scan('P5 · ค่าหลัก / พิสัยของฟังก์ชันผกผัน (ตอบผิดเพราะเลือกมุมนอกพิสัย)',
     r'ค่าหลัก|พิสัยของ[\s\S]{0,30}?\\arc|ช่วง[\s\S]{0,40}?\\arccos[\s\S]{0,30}?นิยาม', show=14)

scan('P6 · สมการตรีโกณที่ต้องยกกำลังสองแล้วเกิดคำตอบแปลกปลอม',
     r'คำตอบแปลกปลอม|ยกกำลังสองทั้งสองข้าง|ตรวจคำตอบกลับ', show=14)

scan('P7 · ถามจำนวนคำตอบของสมการตรีโกณในช่วงที่กำหนด',
     r'มีคำตอบ[\s\S]{0,20}?กี่|จำนวนคำตอบ[\s\S]{0,40}?สมการ|กี่คำตอบ', qonly=True, show=14)

scan('P17 · รูปหลายเหลี่ยมด้านเท่ามุมเท่าแนบในวงกลม ⇒ พื้นที่/เส้นรอบรูป',
     r'เหลี่ยมด้านเท่ามุมเท่า|เหลี่ยมปกติ|\d+\s*เหลี่ยม[\s\S]{0,60}?แนบใน|แนบในวงกลม[\s\S]{0,60}?เหลี่ยม',
     show=14)

scan('P21 · เรือ/เครื่องบินสองลำออกจากจุดเดียวกันทำมุมกัน ⇒ ระยะห่าง (กฎ cos)',
     r'เรือสองลำ|ออกจากท่า|เครื่องบินสองลำ|ออกเดินทางจากจุดเดียวกัน|แล่นออกจาก', show=14)

scan('P24 · ผลคูณของ tan/cos ที่มุมเรียงกัน (tan20·tan40·tan80 · cos20·cos40·cos80)',
     r'\\tan\s*20[\s\S]{0,40}?\\tan\s*40|\\cos\s*20[\s\S]{0,40}?\\cos\s*40|'
     r'\\cos\dfrac\{\\pi\}\{9\}[\s\S]{0,60}?\\cos', show=14)

scan('P25 · ผลบวกกำลังสองของ sin ที่มุมเรียงกัน (sin^2 + sin^2 + ...)',
     r'\\sin\^\{?2\}?[\s\S]{0,25}?\+\s*\\sin\^\{?2\}?[\s\S]{0,25}?\+\s*\\sin\^\{?2\}?', show=14)

scan('P26 · สามเหลี่ยมที่ให้ "อัตราส่วนของด้าน" เป็นตัวเลขสามจำนวน ⇒ ถามมุม/พื้นที่',
     r'อัตราส่วน\s*\$?\s*\d+\s*[:：]\s*\d+\s*[:：]\s*\d+|ด้าน[\s\S]{0,40}?\d+\s*:\s*\d+\s*:\s*\d+',
     show=14)

scan('P27 · รูปสี่เหลี่ยมที่ลากเส้นทแยงมุมแล้วใช้กฎ cos สองครั้ง',
     r'สี่เหลี่ยม[\s\S]{0,120}?เส้นทแยงมุม[\s\S]{0,120}?(?:กฎของโคไซน์|\\cos)|'
     r'รูปสี่เหลี่ยม[\s\S]{0,80}?ด้านยาว[\s\S]{0,80}?ด้านยาว', only7=True, show=14)

scan('P28 · ให้พื้นที่สามเหลี่ยม + สองด้าน ⇒ ย้อนหามุม (กลับทิศของ D3)',
     r'พื้นที่[\s\S]{0,60}?ตารางหน่วย[\s\S]{0,80}?(?:มุม|\\theta)|มีพื้นที่[\s\S]{0,60}?จงหามุม',
     only7=True, show=14)

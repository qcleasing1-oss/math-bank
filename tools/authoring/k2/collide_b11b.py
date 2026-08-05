# -*- coding: utf-8 -*-
"""กวาดรอบสองของก้อน 11 — ปิดช่องที่รอบแรกยังตอบไม่ชัด

รอบแรกบอกอะไร
  ✅ ว่าง : A (ให้ s,r ⇒ ถามมุมเป็นองศา) 0 ข้อ · G (ด้านเรียงเลขคณิต) 0 ข้อ · I (ชนิดของสามเหลี่ยม) 0 ข้อ
  ⛔ อิ่ม : C คู่มุมประกอบ 84 ข้อ · E พื้นที่ segment 13 ข้อ (q107/q212/q217 ตรงตัว) ·
           H เซกเตอร์เส้นรอบรูปคงที่ ⇒ พื้นที่มากสุด (chap-13-q97 ตรงเป๊ะ) · J มุมก้ม-เงย-นาฬิกา 23 ข้อ
  ⚠️ F (เส้นมัธยฐาน) รอบแรกใช้ไม่ได้ — regex ไปโดน "มัธยฐาน" ของสถิติ 137 ข้อ ⇒ กวาดใหม่ที่นี่
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


def scan(label, pattern, qonly=False, show=6, only7=False):
    rx = re.compile(pattern)
    pool = [q for q in items if (not only7 or '7' in (q.get('topics') or [])
                                 or any(s.startswith('7.') for s in (q.get('subTopics') or [])))]
    hit = [q for q in pool if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ%s' % (label, len(hit), ' (เฉพาะบท 7)' if only7 else ''))
    for q in hit[:show]:
        print('   %-30s %-8s %-10s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:110]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# F แก้ใหม่ · เส้นมัธยฐานของสามเหลี่ยม (เฉพาะบท 7 · ไม่ใช่ค่ามัธยฐานทางสถิติ)
scan('F2 · เส้นมัธยฐาน/จุดกึ่งกลางด้าน ในบทตรีโกณ',
     r'มัธยฐาน|จุดกึ่งกลาง', only7=True, show=10)

# D2 · โจทย์ที่ให้ "สองด้านกับมุมระหว่างด้าน" แล้วถามพื้นที่ตรง ๆ
scan('D2 · ให้สองด้าน + มุมระหว่าง ⇒ ถามพื้นที่ (แบบตรง)',
     r'(?:มุมระหว่าง|มุมที่อยู่ระหว่าง)[\s\S]{0,150}?พื้นที่|พื้นที่[\s\S]{0,150}?มุมระหว่าง', qonly=True, show=10)

# D3 · กฎของโคไซน์ใช้หา "มุม" จากด้านสามด้าน (ระวังชนกับ q006 ของเรา)
scan('D3 · ให้ด้านสามด้าน ⇒ หามุม (กฎโคไซน์ย้อน)',
     r'ด้าน(?:ทั้ง)?สามด้าน[\s\S]{0,120}?มุม|ยาว\s*\$?\d+[\s\S]{0,60}?ยาว\s*\$?\d+[\s\S]{0,60}?ยาว\s*\$?\d+[\s\S]{0,80}?(?:มุม|\\cos)',
     qonly=True, only7=True, show=10)

# L · ความเร็วเชิงมุม / ล้อหมุน / รอก / สายพาน (7.11 ประยุกต์)
scan('L1 · ความเร็วเชิงมุม · ล้อหมุน · รอบต่อนาที · รอก · สายพาน',
     r'ความเร็วเชิงมุม|รอบต่อนาที|รอบ/นาที|รอก|สายพาน|ล้อ(?:รถ|จักรยาน|เกวียน)?หมุน|เฟือง', show=10)

# M · แพะผูกเชือกที่มุมรั้ว / พื้นที่ที่กวาดได้
scan('M1 · เชือกผูกที่มุม/หลัก แล้วถามพื้นที่ที่เข้าถึงได้',
     r'ผูก(?:ไว้)?(?:ที่|กับ)[\s\S]{0,60}?เชือก|เชือกยาว[\s\S]{0,80}?พื้นที่|แพะ|วัว|ล่าม', show=10)

# N · a cos A = b cos B  (เนื้อของ I) — เช็คแบบเจาะรูปสมการ
scan('N1 · เงื่อนไขรูป a cos A = b cos B / a cos B = b cos A',
     r'[abc]\s*\\cos\s*[ABC][\s\S]{0,40}?=[\s\S]{0,40}?[abc]\s*\\cos\s*[ABC]|\\cos\s*A\}\{a\}|\\dfrac\{\\cos A\}\{a\}', show=10)

# O · สามเหลี่ยมที่ด้านเป็นสามจำนวนเรียงกัน (เผื่อเขียนคนละสำนวนจาก G)
scan('O1 · ด้านสามด้านเป็นสามจำนวนที่เรียงต่อกัน / ต่างกันเท่า ๆ กัน',
     r'ด้าน[\s\S]{0,80}?(?:เรียงต่อกัน|ต่างกันอยู่|เป็นสามจำนวน)|(?:x-d|a-d)[\s\S]{0,40}?(?:x\+d|a\+d)', show=10)

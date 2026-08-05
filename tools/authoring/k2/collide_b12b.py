# -*- coding: utf-8 -*-
"""กวาดรอบสองของก้อน 12 — ปิดช่องที่รอบแรกยังตอบไม่ชัด

รอบแรกสรุปได้
  ⛔ อิ่ม : P1/P2 ทิศทาง-แบริ่ง (บท 7 มี 5 ข้อ · q222 คือ "สองคนเดินคนละทิศ ⇒ ระยะห่าง" ตรงตัว)
          Q1 arcsin(sin x) นอกช่วงหลัก (5 ข้อ · รวม q051 ของเราเอง + pat1-2562-02-q06)
          R1 บันได-เงา-เสา ในบท 7 = มุมเงย/มุมก้ม ซึ่งอิ่มอยู่แล้ว 23 ข้อ
          S2 ผลบวก sin^2 ของมุมเรียงกัน (chap-07-q02 · pat1-2558-03-q32 ตรงตัว)
  ✅ ว่าง : Q3 ผกผัน + ถามจำนวน/ไม่นิยาม = 0 ข้อ
          R2 สามเหลี่ยมมุมฉากพื้นฐาน ให้ด้าน ⇒ ถามอัตราส่วน = 2 ข้อ และทั้งคู่เป็น pat1 ระดับสูง
          R3 สองสามเหลี่ยมมุมฉากติดกัน = 1 ข้อ (เป็นข้อรูปแรเงา)
          S4 ค่าสูงสุด/ต่ำสุดใต้เงื่อนไข A+B+C = pi = 0 ข้อ
  ⚠️ S3 (2R) รอบแรกหลวมเกิน — regex ไปโดน '2R' ในบทเมทริกซ์ ⇒ กวาดใหม่ให้แคบ
  ⚠️ S1 (telescoping) รอบแรกหลวม ⇒ กวาดใหม่ให้แคบ
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

# ── S3 แก้ใหม่ · โจทย์ที่ "ให้หรือถามรัศมีวงกลมล้อมรอบสามเหลี่ยม" จริง ๆ (เฉพาะบท 7) ──
scan('S3b · รัศมีวงกลมล้อมรอบสามเหลี่ยม (บท 7 เท่านั้น)',
     r'วงกลมล้อมรอบ|วงล้อมรอบ|วงกลมที่ล้อมรอบ|circumradius|รัศมีของวงกลมที่ผ่านจุดยอด',
     only7=True, show=12)

# ── S1 แก้ใหม่ · ผลคูณ cos theta · cos 2theta · cos 4theta แบบเท่าตัวเรียงกัน ──
scan('S1b · ผลคูณโคไซน์มุมเป็นเท่าตัวเรียงกัน (cos t · cos 2t · cos 4t)',
     r'\\cos\s*\\?\w*\s*\\?c?d?o?t?\s*\\cos\s*2\s*\\?\w+[\s\S]{0,40}?\\cos\s*4|'
     r'\\cos\s*\\dfrac\{\\pi\}\{7\}[\s\S]{0,80}?\\cos\s*\\dfrac\{2\\pi\}\{7\}|'
     r'2\^\{?n\}?\s*\\sin', show=12)

# ── ฝั่ง 7.10 ที่ยังเหลือ ─────────────────────────────────────────────────────
scan('T1 · ทางลาด/ความชัน/มุมเอียงของพื้นผิว (ramp · หลังคา · ทางขึ้นเขา)',
     r'ทางลาด|ความชัน[\s\S]{0,60}?มุม|มุมเอียง|หลังคา|ลาดเอียง|พื้นเอียง|ขึ้นเนิน|ทางขึ้น', show=12)

scan('T2 · ลูกตุ้ม/ชิงช้า/แกว่ง เป็นส่วนโค้ง',
     r'ลูกตุ้ม|ชิงช้า(?!สวรรค์)|แกว่ง|เหวี่ยง', show=12)

scan('T3 · ระยะบนผิวโลก / เส้นละติจูด-ลองจิจูด / รัศมีโลก',
     r'ละติจูด|ลองจิจูด|ผิวโลก|รัศมีของโลก|เส้นศูนย์สูตร', show=12)

scan('T4 · เข็มนาฬิกา (ยืนยันว่าอิ่มจริง)',
     r'เข็มสั้น|เข็มยาว|เข็มนาที|เข็มชั่วโมง|หน้าปัดนาฬิกา', show=12)

# ── ฝั่ง "ยากมาก" ที่เป็นไปได้ ────────────────────────────────────────────────
scan('U1 · a sin x + b cos x ที่ต้องหาช่วงของ "ค่าคงตัว" ให้สมการมีคำตอบ',
     r'(?:\\sin|\\cos)[\s\S]{0,120}?มีคำตอบ[\s\S]{0,60}?(?:ค่าของ|ช่วง|เซตของ)|'
     r'สมการ[\s\S]{0,150}?มีคำตอบจริง', qonly=True, only7=True, show=12)

scan('U2 · กราฟตรีโกณที่ให้ค่าสูงสุด-ต่ำสุด-คาบ แล้วถามผลรวมของสัมประสิทธิ์',
     r'(?:a\s*\\sin|a\s*\\cos)[\s\S]{0,120}?(?:\+\s*d|\+\s*c)[\s\S]{0,150}?(?:a\s*\+\s*b|ผลรวมของ)',
     only7=True, show=12)

scan('U3 · ด้านสามด้านเป็นลำดับเรขาคณิต (อัตราส่วนคงที่)',
     r'ลำดับเรขาคณิต[\s\S]{0,150}?(?:ด้าน|สามเหลี่ยม)|ด้าน[\s\S]{0,100}?ลำดับเรขาคณิต', show=12)

scan('U4 · พื้นที่สามเหลี่ยมด้วยสูตรเฮรอน',
     r'เฮรอน|Heron|s\(s-a\)\(s-b\)\(s-c\)|\\sqrt\{s\(s', show=12)

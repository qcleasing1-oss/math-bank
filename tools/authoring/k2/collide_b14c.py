# -*- coding: utf-8 -*-
"""กวาดชนก้อน 14 · รอบ 3

ตายจากรอบ 2 (2 แบบร่าง)
  ✗ H  สมการเอกพันธ์ a sin^2 + b sin cos + c cos^2 = 0 ⇒ กำลังสองใน tan
       ชนกับ chap-07-trigonometry-q147 เต็ม ๆ (G ตรง · M ตรง ต่างแค่ A) ⇒ WATCH-A ทันที ⇒ ทิ้ง
  ✗ (เลี่ยง) แม่พิมพ์ "tan alpha, tan beta เป็นรากของสมการกำลังสอง" — หนาแน่น
       (chap-07-q182 · pat1-2561-02-q07 · q001 ของเราเอง)

ผู้สมัครใหม่แทนช่อง "ยาก"
  K  7.7/7.2 · sin(pi cos x) = 0 บน [0, 2pi) ⇒ ถาม "เซตคำตอบ"
     เครื่องมือ: ต้องเห็นว่าอาร์กิวเมนต์ข้างในถูกจำกัดด้วย -1 <= cos x <= 1
     ⇒ k เป็นจำนวนเต็มได้แค่ -1, 0, 1 ⇒ แปลงเป็นสมการพื้นฐานสามสมการ
     ⛔ ไม่ถาม "ผลบวกของคำตอบ" เพราะเราตีตราแม่พิมพ์นั้นว่าอิ่มตัวไปแล้ว (77 ข้อ) ตั้งแต่ก้อน 10

ตรวจซ้ำของเดิมที่จะใช้จริง
  A' บันได · F' ทางลาด — พิมพ์ข้อความเต็มของสองข้อที่ใกล้ที่สุดออกมาอ่านด้วยตา
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


def scan(label, pattern, qonly=False, show=10):
    rx = re.compile(pattern)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-32s %-8s %-12s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:110]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

# ── K · สมการตรีโกณซ้อนตรีโกณ (อาร์กิวเมนต์ข้างในเป็นฟังก์ชันตรีโกณ) ──────────
scan('K1 · sin(...cos x...) หรือ cos(...sin x...) — ตรีโกณซ้อนตรีโกณ',
     r'\\sin\s*\\?\(?\s*\\pi\s*\\cos|\\cos\s*\\?\(?\s*\\pi\s*\\sin|'
     r'\\sin\s*\\left\(\s*\\pi\s*\\cos|\\cos\s*\\left\(\s*\\pi\s*\\sin|'
     r'\\sin\s*\(\s*\\cos|\\cos\s*\(\s*\\sin|\\tan\s*\(\s*\\sin|\\sin\s*\(\s*\\tan', show=18)
scan('K2 · อาร์กิวเมนต์ข้างในถูกจำกัดพิสัย ⇒ จำนวนเต็ม k มีได้จำกัด',
     r'-\s*1\s*\\le\s*\\cos[\s\S]{0,60}?\\le\s*1[\s\S]{0,200}?จำนวนเต็ม|'
     r'เป็นจำนวนเต็มได้เพียง|k\s*=\s*-\s*1\s*,\s*0\s*,\s*1', show=16)
scan('K3 · ถาม “เซตคำตอบ” ของสมการตรีโกณบนช่วงจำกัด (ดูความหนาแน่นของ ask นี้)',
     r'เซตคำตอบของสมการ', qonly=True, show=8)

# ── ตรวจด้วยตา : สองข้อที่ใกล้ผู้สมัคร A' และ F' ที่สุด ──────────────────────
for qid in ['pat1-2564-03-q17', 'chap-07-trigonometry-q102', 'chap-07-trigonometry-q147',
            'chap-07-trigonometry-q145']:
    q = BY.get(qid)
    if not q:
        continue
    print()
    print('─' * 78)
    print(qid, '·', q.get('difficulty'), '·', '/'.join(q.get('subTopics') or []))
    print((q.get('question') or '').replace('<br>', '\n'))
    for i, c in enumerate(q.get('choices') or []):
        print('   (%d) %s' % (i + 1, c))

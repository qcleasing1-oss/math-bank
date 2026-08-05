# -*- coding: utf-8 -*-
"""กวาดรอบ 13 (รอบสุดท้ายของ q073) — ยิงตรงด้วยถ้อยคำและตัวเลขจริงของดีไซน์ที่เลือก

ดีไซน์ที่เลือกแทน SSA
  q073 ยาก · 7.5 · ให้ alpha, beta อยู่ใน (0, pi/2) และ tan alpha, tan beta
       เป็นรากของสมการ x^2 - 7x + 8 = 0 ⇒ หา alpha + beta
       ผลบวกราก 7 · ผลคูณราก 8 ⇒ tan(alpha+beta) = 7/(1-8) = -1
       ทั้งสองรากเป็นบวก ⇒ alpha + beta อยู่ใน (0, pi) ⇒ ตอบ 3pi/4
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

byid = {q['id']: q for q in items}


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

scan('U1 · ให้ค่า tan ของสองมุม แล้วถามผลบวกของสองมุมนั้น',
     r'\\tan\s*\\?(?:alpha|beta|theta|A|B)[\s\S]{0,140}?\\tan\s*\\?(?:alpha|beta|theta|A|B)'
     r'[\s\S]{0,140}?(?:\\alpha\s*\+\s*\\beta|A\s*\+\s*B|ผลบวกของมุม|ขนาดของมุม[\s\S]{0,20}?รวม)',
     qonly=True, show=14)
scan('U2 · ความสัมพันธ์ระหว่างรากกับสัมประสิทธิ์ ใช้ในบทตรีโกณ',
     r'ผลบวกของราก[\s\S]{0,200}?\\(?:sin|cos|tan)|\\(?:sin|cos|tan)[\s\S]{0,200}?ผลคูณของราก',
     show=14)
scan('U3 · สมการ x^2 - 7x + 8 (ตัวเลขจริงของข้อนี้)', r'x\^\{?2\}?\s*-\s*7x\s*\+\s*8')
scan('U4 · คำตอบ 3pi/4 ในบริบทผลบวกของสองมุม',
     r'\\dfrac\{3\\pi\}\{4\}[\s\S]{0,120}?(?:\\alpha|\\beta|ผลบวก)|'
     r'(?:\\alpha\s*\+\s*\\beta)[\s\S]{0,120}?\\dfrac\{3\\pi\}\{4\}', show=14)
scan('U5 · 1 - tan A tan B เป็นศูนย์ / ตัวส่วนเป็นศูนย์ในสูตรผลบวกมุม',
     r'1\s*-\s*\\tan[\s\S]{0,40}?\\tan[\s\S]{0,60}?(?:=\s*0|เป็นศูนย์)|ตัวส่วนเป็นศูนย์', show=14)

print()
print('== U6 · ข้อที่เราแต่งเองในหัวข้อ 7.5 ทั้งหมด ==')
for q in items:
    if q['id'].startswith('gen-chap-07') and '7.5' in (q.get('subTopics') or []):
        print('   %-32s %-8s %-12s %s' % (q['id'], q.get('difficulty'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:130]))

for qid in ('gen-chap-07-trigonometry-q001',):
    q = byid[qid]
    print()
    print('=' * 78)
    print('%s  [%s]  %s' % (qid, q.get('difficulty'), '/'.join(q.get('subTopics') or [])))
    print(q.get('question'))
    for i, c in enumerate(q.get('choices') or []):
        print('   (%d) %s' % (i + 1, c))
    print('   correct =', q.get('correct'))

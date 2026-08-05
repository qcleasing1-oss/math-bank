# -*- coding: utf-8 -*-
"""ส่องข้อที่ต้องตัดสินด้วยตา — ก้อน 13"""
import io, json, glob, re

items = {}
for p in sorted(glob.glob('/tmp/mb27/data/sets/*.json') +
                glob.glob('/home/claude/k1/out/*.json') +
                glob.glob('/home/claude/k2/out/*.json')):
    d = json.load(io.open(p, encoding='utf-8'))
    for q in d.get('questions', []):
        items[q['id']] = q

def show(qid, full=False):
    q = items.get(qid)
    print('\n' + '=' * 78)
    if not q:
        print('ไม่พบ', qid); return
    print('%s  [%s]  %s' % (qid, q.get('difficulty'), '/'.join(q.get('subTopics') or [])))
    print('-' * 78)
    print(q.get('question'))
    for i, c in enumerate(q.get('choices') or []):
        print('   (%d) %s' % (i + 1, c))
    print('   correct =', q.get('correct'))
    if full:
        ex = q.get('explanation') or []
        for ln in (ex if isinstance(ex, list) else [ex]):
            print('   |', ln)

for qid in ['gen-chap-07-trigonometry-q047', 'samn-2556-01-q03',
            'gen-chap-07-trigonometry-q006', 'chap-07-trigonometry-q83']:
    show(qid)

# ยิงตรง : สามด้าน 3,5,7 เฉพาะบท 7
print('\n' + '#' * 78)
print('# บท 7 ที่มีเลข 3 กับ 5 กับ 7 เป็นความยาวด้าน')
rx = re.compile(r'(?:ยาว|=)\s*\$?\s*7\s*(?:หน่วย|\$)')
for q in items.values():
    st = q.get('subTopics') or []
    if not any(s.startswith('7') for s in st):
        continue
    s = q.get('question') or ''
    if rx.search(s) and re.search(r'(?:ยาว|=)\s*\$?\s*[35]\s*(?:หน่วย|\$)', s):
        print('   %-32s %-8s %s' % (q['id'], q.get('difficulty'), s.replace('\n', ' ')[:110]))

# ยิงตรง : นิพจน์มุมพิเศษล้วนแบบ "ค่าของ ... เท่ากับ" ในบท 7
print('\n' + '#' * 78)
print('# บท 7 ที่ถาม "ค่าของ <นิพจน์มุมพิเศษ>" ล้วน ๆ (pi/6 pi/4 pi/3 หรือ 30 45 60)')
for q in items.values():
    st = q.get('subTopics') or []
    if not any(s.startswith('7') for s in st):
        continue
    s = q.get('question') or ''
    if re.search(r'ค่าของ', s) and re.search(
            r'\\dfrac\{\\pi\}\{[346]\}|\b(?:30|45|60)\^', s):
        print('   %-32s %-8s %s' % (q['id'], q.get('difficulty'), s.replace('\n', ' ')[:110]))

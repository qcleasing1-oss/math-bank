# -*- coding: utf-8 -*-
"""ดูข้อที่รอบสี่ชี้มาแบบเต็มตัว ก่อนตัดสินว่าชนหรือไม่ชน"""
import io, json, glob

items = {}
for p in sorted(glob.glob('/tmp/mb27/data/sets/*.json') +
                glob.glob('/home/claude/k1/out/*.json') +
                glob.glob('/home/claude/k2/out/*.json')):
    d = json.load(io.open(p, encoding='utf-8'))
    for q in d.get('questions', []):
        items[q['id']] = q

for qid in ['gen-chap-07-trigonometry-q010',
            'gen-chap-07-trigonometry-q033',
            'gen-chap-07-trigonometry-q060',
            'gen-chap-07-trigonometry-q030',
            'chap-07-trigonometry-q13',
            'chap-07-trigonometry-q14']:
    q = items.get(qid)
    if not q:
        print('!! ไม่พบ', qid); continue
    print('=' * 78)
    print(qid, '·', q.get('difficulty'), '·', '/'.join(q.get('subTopics') or []))
    print('โจทย์ :', (q.get('question') or '').replace('\n', ' '))
    print('ตัวเลือก :', q.get('choices'))
    print('ถูก :', q.get('correct'))

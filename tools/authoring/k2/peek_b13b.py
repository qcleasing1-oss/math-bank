# -*- coding: utf-8 -*-
"""เปิดข้อเต็มของสองข้อที่รอบ Y1 ชี้มา — ตัดสินว่าดีไซน์ SSA คลุมเครือรอดหรือไม่"""
import io, json, glob

items = {}
for p in sorted(glob.glob('/tmp/mb27/data/sets/*.json') +
                glob.glob('/home/claude/k1/out/*.json') +
                glob.glob('/home/claude/k2/out/*.json')):
    d = json.load(io.open(p, encoding='utf-8'))
    for q in d.get('questions', []):
        items[q['id']] = q


def show(qid, expl=False):
    q = items.get(qid)
    print()
    print('=' * 78)
    if not q:
        print('ไม่พบ', qid)
        return
    print('%s  [%s]  %s' % (qid, q.get('difficulty'), '/'.join(q.get('subTopics') or [])))
    print('-' * 78)
    print(q.get('question'))
    for i, c in enumerate(q.get('choices') or []):
        print('   (%d) %s' % (i + 1, c))
    print('   correct =', q.get('correct'))
    if expl:
        ex = q.get('explanation') or ''
        ex = ex if isinstance(ex, list) else [str(ex)]
        print('-' * 78)
        for line in ex:
            print('  ', line)


show('gen-chap-07-trigonometry-q053', expl=True)
show('chap-07-trigonometry-q110', expl=True)

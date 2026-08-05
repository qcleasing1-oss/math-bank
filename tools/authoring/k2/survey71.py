# -*- coding: utf-8 -*-
"""ดูข้อ 7.1 ทั้งหมด (ป้ายไหนก็ได้) + ข้อที่ 'ทรงสามเหลี่ยมมุมฉาก/อัตราส่วน' ทั้งบท 7"""
import json, io, glob, os, re

SETS = '/tmp/mb25/data/sets'
allq = []
for fp in sorted(glob.glob(SETS + '/*.json')):
    d = json.load(io.open(fp, encoding='utf-8'))
    for q in d.get('questions', []):
        allq.append((os.path.basename(fp), q))

print('=== ข้อที่มี 7.1 อยู่ในป้ายใดก็ได้ ===')
for fn, q in allq:
    st = [str(x) for x in (q.get('subTopics') or [])]
    if '7.1' in st:
        print(' %s · %s · %s · %s' % (q['id'], q.get('difficulty'), st, q.get('type')))
        print('   ', ' '.join(q.get('question','').split())[:260])
        for i, c in enumerate(q.get('choices') or []):
            print('     %d) %s' % (i+1, ' '.join(str(c).split())[:60]))
        print()

print('=== ทรง "ให้ค่าอัตราส่วนหนึ่ง หาอีกอัตราส่วน" ทั้งบท 7 (ทุกระดับ) ===')
PAT = re.compile(r'(สามเหลี่ยมมุมฉาก|ด้านตรงข้ามมุมฉาก|\\sec|\\csc|\\cot)')
n = 0
for fn, q in allq:
    st = [str(x) for x in (q.get('subTopics') or [])]
    if not st or not st[0].startswith('7.'): continue
    txt = q.get('question','')
    if PAT.search(txt):
        n += 1
        print(' %s · %s · %s' % (q['id'], q.get('difficulty'), st[0]))
        print('   ', ' '.join(txt.split())[:200])
print('รวม', n, 'ข้อ')

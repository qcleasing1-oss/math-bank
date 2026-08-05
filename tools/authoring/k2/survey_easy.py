# -*- coding: utf-8 -*-
"""ก้าว 2 · สำรวจข้อระดับ ง่าย ของบท 7 ทั้งหมด (ตัวหาร = ป้ายหลัก subTopics[0])"""
import json, io, os, glob, collections

SETS = '/tmp/mb25/data/sets'
rows = []
for fp in sorted(glob.glob(SETS + '/*.json')):
    d = json.load(io.open(fp, encoding='utf-8'))
    for q in d.get('questions', []):
        st = q.get('subTopics') or []
        if not st: continue
        if not str(st[0]).startswith('7.'): continue
        rows.append((os.path.basename(fp), q, str(st[0])))

print('ข้อที่ป้ายหลักเป็น 7.* ทั้งหมด:', len(rows))
easy = [r for r in rows if r[1].get('difficulty') == 'ง่าย']
print('ระดับ ง่าย:', len(easy))
c = collections.Counter(r[2] for r in easy)
for k in sorted(c, key=lambda x: (len(x), x)):
    print('  %-5s %d' % (k, c[k]))
print()
for fn, q, st in sorted(easy, key=lambda r: (len(r[2]), r[2], r[1]['id'])):
    stem = q.get('question', '')
    stem = ' '.join(stem.split())
    print('[%s] %s · %s · %s' % (st, q['id'], q.get('type'), 'IMG' if q.get('hasImage') else '--'))
    print('    ', stem[:300])
    ch = q.get('choices') or []
    if ch:
        print('     ตัวเลือก:', ' | '.join(' '.join(str(x).split())[:40] for x in ch))
    print()

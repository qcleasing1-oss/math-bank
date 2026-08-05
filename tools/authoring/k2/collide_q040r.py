# -*- coding: utf-8 -*-
"""STEP H · แม่พิมพ์แทน q040 · 'ค่า x ที่ทำให้ tan(bx+c) หาค่าไม่ได้'"""
import glob, json, re, io
QS=[]
for fp in sorted(glob.glob('/tmp/mb27/data/sets/*.json')):
    for q in json.load(io.open(fp,encoding='utf-8')).get('questions',[]): QS.append(('คลัง',q))
for fp in sorted(glob.glob('/home/claude/k1/out/*.json'))+sorted(glob.glob('/home/claude/k2/out/*.json')):
    for q in json.load(io.open(fp,encoding='utf-8')).get('questions',[]): QS.append(('ใหม่',q))
def stem(q):
    s=q.get('question')
    if isinstance(s,list): s=' '.join(x for x in s if isinstance(x,str))
    return (s or '').replace('\n',' ')
def full(q):
    return json.dumps(q,ensure_ascii=False)
P=[('1 · คำว่า หาค่าไม่ได้ / ไม่นิยาม ในตัวโจทย์', r'หาค่าไม่ได้|หาค่ามิได้|ไม่นิยาม|นิยามไม่ได้|ไม่มีนิยาม', stem),
   ('2 · โดเมนของฟังก์ชันตรีโกณ', r'โดเมนของ[^.]{0,40}(\\tan|\\sec|\\cot|\\csc)', stem),
   ('3 · เส้นกำกับ ในบทที่ 7 เท่านั้น', r'เส้นกำกับ|asymptote', stem),
   ('4 · tan(bx + c) รูปกราฟ (สัมประสิทธิ์หน้า x ไม่ใช่ 1)',
    r'\\tan\s*\\?\(?\s*\d\s*x|\\tan\\left\(\s*\d\s*x|\\cot\s*\\?\(?\s*\d\s*x|\\sec\s*\\?\(?\s*\d\s*x', stem),
   ('5 · pi/2 + n pi (เงื่อนไขที่ cos เป็นศูนย์) ทั้งข้อ รวมเฉลย',
    r'\\dfrac\{\\pi\}\{2\}\s*\+\s*n\\pi|\\frac\{\\pi\}\{2\}\s*\+\s*n\\pi', full)]
for t,p,g in P:
    rx=re.compile(p); hits=[(s,q) for s,q in QS if rx.search(g(q))]
    print(); print('='*78); print(t,' ⇒ ',len(hits),'ข้อ'); print('='*78)
    for s,q in hits[:12]:
        print('  [%s]'%s,q.get('id'),'|',q.get('difficulty'),'|',q.get('subTopics'))
        print('      ',stem(q)[:150])
    if len(hits)>12: print('   … อีก',len(hits)-12,'ข้อ')

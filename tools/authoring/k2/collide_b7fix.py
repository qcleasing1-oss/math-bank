# -*- coding: utf-8 -*-
"""STEP H · หาแม่พิมพ์แทน q040 · ต้องเป็น 7.3 ระดับปานกลาง ที่ไม่ใช่เรื่อง 'คาบ'
กวาด 4 แม่พิมพ์ที่คิดไว้ ว่าชนของเดิมหรือของเราเองหรือไม่"""
import glob, json, re, io
QS=[]
for fp in sorted(glob.glob('/tmp/mb27/data/sets/*.json')):
    for q in json.load(io.open(fp,encoding='utf-8')).get('questions',[]): QS.append(('คลัง',q))
for fp in sorted(glob.glob('/home/claude/k1/out/*.json'))+sorted(glob.glob('/home/claude/k2/out/*.json')):
    for q in json.load(io.open(fp,encoding='utf-8')).get('questions',[]): QS.append(('ใหม่',q))
print('ฐานเทียบ:',len(QS),'ข้อ')
def stem(q):
    s=q.get('question')
    if isinstance(s,list): s=' '.join(x for x in s if isinstance(x,str))
    return (s or '').replace('\n',' ')
PROBES=[
 ('A · เส้นกำกับแนวดิ่งของกราฟ tan / sec / cot', r'เส้นกำกับ|asymptote|อะซิมโทท'),
 ('A2 · กราฟของ tan(bx + c) หรือ sec ที่มีการเลื่อน',
  r'\\tan\s*\\left\(|\\tan\s*\(\s*\d?x|y\s*=\s*\\tan|y\s*=\s*\\sec|y\s*=\s*\\cot'),
 ('B · ช่วงที่ฟังก์ชันเพิ่มขึ้น / ลดลง', r'เพิ่มขึ้นในช่วง|ลดลงในช่วง|ฟังก์ชันเพิ่ม|ฟังก์ชันลด|เป็นฟังก์ชันเพิ่ม|เป็นฟังก์ชันลด'),
 ('C · ฟังก์ชันคู่ / ฟังก์ชันคี่', r'ฟังก์ชันคู่|ฟังก์ชันคี่|เป็นฟังก์ชันคี่'),
 ('D · นับจำนวนจุดสูงสุด/ต่ำสุด หรือรอบของกราฟในช่วงที่กำหนด',
  r'จุดสูงสุด[^.]{0,40}กี่|กี่จุด[^.]{0,30}สูงสุด|กี่รอบ|ครบกี่รอบ|จำนวนจุดสูงสุด'),
 ('E · เรนจ์ของฟังก์ชันตรีโกณ (คำว่า เรนจ์)', r'เรนจ์|พิสัยของฟังก์ชัน'),
 ('F · a sin x + b cos x เขียนเป็น R sin(x+alpha) / หาเรนจ์',
  r'\d\\sin\s*x\s*[+-]\s*\d\\cos\s*x|\d\\cos\s*x\s*[+-]\s*\d\\sin\s*x'),
 ('G · แอมพลิจูด', r'แอมพลิจูด'),
]
for t,p in PROBES:
    rx=re.compile(p); hits=[(s,q) for s,q in QS if rx.search(stem(q))]
    print(); print('='*78); print(t,' ⇒ ',len(hits),'ข้อ'); print('='*78)
    for s,q in hits[:10]:
        print('  [%s]'%s,q.get('id'),'|',q.get('difficulty'),'|',q.get('subTopics'))
        print('      ',stem(q)[:160])
    if len(hits)>10: print('   … อีก',len(hits)-10,'ข้อ')

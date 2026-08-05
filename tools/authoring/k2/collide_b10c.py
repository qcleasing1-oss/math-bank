# -*- coding: utf-8 -*-
"""กวาดรอบสาม · เฉพาะ q059 ฉบับปรับ — เปลี่ยนจาก "2cos^2 x + (2a-1)cos x - a = 0"
เป็น "cos 2x + (2a-1)cos x + (1-a) = 0" เพื่อบังคับให้ต้องเลือกสูตรมุมสองเท่ารูป cos เอง

เหตุผลที่ปรับ (บันทึกไว้กันลืม) : ให้คะแนน rubric ฉบับเดิมตามจริงได้ 11 = ยาก
ครูสั่งว่าทุกก้อนต้องมี "ยากมาก" และย้ำว่ายากมากเป็นผลผลิตของ "วิธีแต่ง"
⇒ จึงออกแบบข้อใหม่ให้ยากขึ้นจริง แล้วค่อยให้คะแนนใหม่ (⛔ ไม่ใช่ดันคะแนนของข้อเดิม)
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


def scan(label, pattern, qonly=False, show=10):
    rx = re.compile(pattern)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-28s %-8s %-10s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:120]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))
scan('A · โจทย์ที่มี cos 2x ปนกับ cos x ในสมการเดียว',
     r'\\cos\s*2x[\s\S]{0,80}\\cos\s*x|\\cos\s*x[\s\S]{0,80}\\cos\s*2x', qonly=True)
scan('B · สมการ cos2x/sin2x ที่มีพารามิเตอร์ a หรือ k',
     r'(?:\\cos|\\sin)\s*2x[\s\S]{0,100}?(?:\ba\b|\bk\b)', qonly=True)
scan('C · ถามเซตของค่าพารามิเตอร์ที่ทำให้สมการมีคำตอบจำนวนหนึ่ง',
     r'(?:พอดี|เท่ากับ|ทั้งหมด)\s*\$?3\$?\s*คำตอบ|มีคำตอบ(?:ทั้งหมด)?\s*\$?\d\$?\s*คำตอบ|จำนวนคำตอบ[\s\S]{0,40}เท่ากับ', qonly=True)
scan('D · เอกลักษณ์ cos 2x = 2cos^2 x - 1 ที่ใช้เป็นขั้นแรกของการแก้สมการ',
     r'2\\cos\^2\s*x\s*-\s*1|2\\cos\^\{2\}\s*x\s*-\s*1')

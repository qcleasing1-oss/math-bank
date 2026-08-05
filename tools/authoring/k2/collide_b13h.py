# -*- coding: utf-8 -*-
"""กวาดรอบแปด — ตรวจสองผู้ท้าชิงสุดท้าย (W8 ค่าหลักของฟังก์ชันผกผัน · W10 มุมเงย)"""
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


def scan(label, pattern, qonly=False, show=12):
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

scan('W8a · arcsin(sin ...) · arccos(cos ...) · arctan(tan ...) แบบซ้อนตรง ๆ',
     r'\\arcsin\\left\(\\sin|\\arccos\\left\(\\cos|\\arctan\\left\(\\tan|'
     r'\\arcsin\(\\sin|\\arccos\(\\cos|\\arctan\(\\tan|'
     r'\\sin\^\{-1\}\\left\(\\sin|\\cos\^\{-1\}\\left\(\\cos')
scan('W8b · คำว่า "ค่าหลัก" หรือ "พิสัยของฟังก์ชันผกผัน"',
     r'ค่าหลัก|พิสัยของฟังก์ชันผกผัน|เรนจ์ของ\s*\\?arc')
scan('W10 · มุมเงย / มุมก้ม (ดูความอิ่มตัวของ 7.10)',
     r'มุมเงย|มุมก้ม', show=4)
scan('W11 · ระบบสมการที่ให้ผลบวกของ sin สองมุมและผลบวกของ cos สองมุม (ยิงกว้าง)',
     r'\\sin\s*[A-Za-z]\s*\+\s*\\sin\s*[A-Za-z][\s\S]{0,200}?\\cos\s*[A-Za-z]\s*\+\s*\\cos|'
     r'\\cos\s*[A-Za-z]\s*\+\s*\\cos\s*[A-Za-z][\s\S]{0,200}?\\sin\s*[A-Za-z]\s*\+\s*\\sin')
scan('W12 · เทคนิค "ยกกำลังสองแล้วบวกกัน" ของสองสมการตรีโกณ',
     r'ยกกำลังสองทั้งสองสมการ|ยกกำลังสองแล้วบวก|บวกสมการทั้งสองที่ยกกำลังสอง')

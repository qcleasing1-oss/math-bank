# -*- coding: utf-8 -*-
"""กวาดคลังทั้งหมดก่อนออกแบบก้อน 9 — เป้าหมายคือหัวข้อย่อยที่เรายังบางที่สุด

จำนวนข้อที่แต่งแล้วต่อหัวข้อย่อย (ก่อนก้อน 9)
    7.1=5 · 7.2=17 · 7.3=17 · 7.4=8 · 7.5=4 · 7.6=4 · 7.7=3 · 7.8=0 · 7.9=2 · 7.10=3 · 7.11=5
⇒ 7.8 (ฟังก์ชันตรีโกณผกผัน) ยังไม่มีเลยสักข้อ เป็นช่องว่างใหญ่สุด
"""
import io, json, glob, re, sys, collections

BANK = sorted(glob.glob('/tmp/mb27/data/sets/*.json'))
MINE = sorted(glob.glob('/home/claude/k1/out/*.json') + glob.glob('/home/claude/k2/out/*.json'))

items = []
for p in BANK + MINE:
    try:
        d = json.load(io.open(p, encoding='utf-8'))
    except Exception:
        continue
    for q in d.get('questions', []):
        q['_src'] = p.split('/')[-1].replace('.json', '')
        items.append(q)
print('ฐานเทียบทั้งหมด %d ข้อ (คลัง %d ไฟล์ + ของเรา %d ไฟล์)' % (len(items), len(BANK), len(MINE)))


def txt(q):
    parts = [q.get('question') or '']
    parts += [str(c) for c in (q.get('choices') or [])]
    ex = q.get('explanation', '')
    parts += ex if isinstance(ex, list) else [str(ex or '')]
    for r in (q.get('rows') or []):
        parts += [str(r.get('text', '')), str(r.get('why', ''))]
    return '\n'.join(parts)


def scan(label, pattern, only_question=False, show=6):
    rx = re.compile(pattern)
    hit = []
    for q in items:
        s = (q.get('question') or '') if only_question else txt(q)
        if rx.search(s):
            hit.append(q)
    print()
    print('══ %s ══  เจอ %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        st = '/'.join(q.get('subTopics', []) or [])
        print('   %-34s %-9s %-10s %s'
              % (q['id'], q.get('difficulty', '?'), st, (q.get('question') or '')[:78].replace('\n', ' ')))
    if len(hit) > show:
        print('   ... อีก %d ข้อ' % (len(hit) - show))
    return hit


# ── 1) ฟังก์ชันผกผัน 7.8 · ทั้งคลังมีอะไรบ้าง ────────────────────────
inv = scan('ผกผันตรีโกณทุกแบบ (arcsin/arccos/arctan/sin^-1)',
           r'arcsin|arccos|arctan|arccot|arcsec|arccsc|\\sin\^\{-1\}|\\cos\^\{-1\}|\\tan\^\{-1\}'
           r'|sin\^\{-1\}|cos\^\{-1\}|tan\^\{-1\}', show=10)
c = collections.Counter('/'.join(q.get('subTopics', []) or ['-']) for q in inv)
print('   แยกตามหัวข้อย่อย:', dict(c))
c2 = collections.Counter(q['_src'] for q in inv)
print('   แยกตามชุด:', dict(c2))

# ── 2) แม่พิมพ์ที่เล็งไว้สำหรับก้อน 9 ────────────────────────────────
scan('q050 · ผกผันซ้อนกัน เช่น sin(arccos x)', r'(?:\\sin|\\cos|\\tan)\s*\(\s*\\?arc')
scan('q051 · ผลบวก arctan สองตัว', r'arctan[^\n]{0,60}\+[^\n]{0,20}arctan|\\tan\^\{-1\}[^\n]{0,60}\+[^\n]{0,25}\\tan\^\{-1\}')
scan('q052 · สมการที่ต้องแยกกรณีเพราะหารด้วย sin/cos', r'หารทั้งสองข้างด้วย|หารด้วย \$\\(?:sin|cos)')
scan('q053 · กฎไซน์กรณีกำกวม (ambiguous case)', r'กำกวม|ambiguous|สองรูป|ได้สองคำตอบ')
scan('q054 · มุมก้ม-มุมเงยสองจุดสังเกต', r'มุมเงย[^\n]{0,120}มุมเงย|มุมก้ม[^\n]{0,120}มุมก้ม')
scan('เรนจ์หลักของฟังก์ชันผกผัน', r'เรนจ์หลัก|ค่าหลัก|principal')

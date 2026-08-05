# -*- coding: utf-8 -*-
"""กวาดรอบสิบ — ผู้ท้าชิงตำแหน่ง "ข้อยาก" ตัวสุดท้าย : กรณีคลุมเครือของกฎของไซน์ (SSA)
ดีไซน์ : b = 8 · มุม A = pi/6 · a = 5  (b sin A = 4 < a = 5 < b = 8 ⇒ ได้สองรูป)
         c^2 - 8sqrt(3) c + 39 = 0 ⇒ c = 4sqrt(3) ± 3 ⇒ ผลบวก = 8sqrt(3)
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

scan('Y1 · กรณีคลุมเครือ / สร้างสามเหลี่ยมได้สองรูป',
     r'คลุมเครือ|ได้สองรูป|สองรูปที่ต่างกัน|สามเหลี่ยมสองรูปที่สอดคล้อง|เป็นไปได้สองแบบ|กี่รูป')
scan('Y2 · ให้ด้านสองด้านกับมุมที่ไม่ใช่มุมระหว่าง (SSA) แล้วถามด้านที่สาม',
     r'ตรงข้ามมุม[\s\S]{0,120}?ความยาวด้าน[\s\S]{0,60}?ที่เป็นไปได้|'
     r'ค่าที่เป็นไปได้ทั้งหมดของความยาวด้าน|ผลบวกของความยาวด้าน')
scan('Y3 · สมการกำลังสองของด้านที่ได้จากกฎของโคไซน์ (c^2 - 2bc cos A + ... = 0)',
     r'สมการกำลังสอง[\s\S]{0,80}?(?:กฎของโคไซน์|ด้าน)|'
     r'c\^\{?2\}?\s*-\s*\d*\s*\\?sqrt|เป็นสมการกำลังสองใน')
scan('Y4 · ผลบวกของรากสมการกำลังสอง (เวียต) ในบริบทเรขาคณิต',
     r'ผลบวกของค่าที่เป็นไปได้|ผลบวกของรากทั้งสอง|ผลบวกของคำตอบทั้งสอง', show=14)
scan('Y5 · กฎของไซน์แล้วได้ sin B = 4/5 (สองมุมที่เป็นไปได้)',
     r'\\sin\s*B\s*=\s*\\dfrac\{4\}\{5\}|\\sin\s*B\s*=\s*0\.8|มุมป้านหรือมุมแหลม')
scan('Y6 · โจทย์ที่มีทั้ง a = 5 · b = 8 · มุม 30 องศา หรือ pi/6',
     r'(?:^|[^0-9])8[\s\S]{0,80}?(?:30\^|\\dfrac\{\\pi\}\{6\})[\s\S]{0,80}?(?:^|[^0-9])5|'
     r'(?:30\^|\\dfrac\{\\pi\}\{6\})[\s\S]{0,120}?8[\s\S]{0,60}?5', qonly=True, show=8)

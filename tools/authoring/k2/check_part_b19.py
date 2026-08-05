# -*- coding: utf-8 -*-
"""ด่านตรวจไฟล์ข้อเดี่ยวของก้อน 19 — ผู้แต่งแต่ละคนรันกับไฟล์ของตัวเองก่อนส่งงาน

    python3 /home/claude/k2/check_part_b19.py 105

ตรวจสิ่งที่ check_k2.py จะตรวจอีกทีตอนรวมก้อน แต่ตรวจได้ทีละไฟล์ ⇒ ผู้แต่งไม่ต้องรอทั้งก้อน
⛔ ผ่านไฟล์นี้ ≠ ผ่าน check_k2 ทั้งหมด แต่ถ้าไฟล์นี้แดง ก็แดงแน่นอนตอนรวม
"""
import io, os, re, sys, collections

sys.path.insert(0, '/home/claude/k2')
from stems_b19 import STEMS

SPEC = {s[0]: s for s in STEMS}
n = int(sys.argv[1])
p = '/home/claude/k2/parts_b19/q%03d.py' % n
bad = []


def fail(m):
    bad.append(m)


if not os.path.exists(p):
    print('🔴 ไม่พบไฟล์ %s' % p)
    sys.exit(1)

raw = io.open(p, encoding='utf-8').read()
if not raw.startswith('# -*- coding: utf-8 -*-'):
    fail('ไฟล์ไม่ได้เริ่มด้วยบรรทัด coding')
try:
    compile(raw, p, 'exec')
except SyntaxError as e:
    print('🔴 SyntaxError บรรทัด %s : %s' % (e.lineno, e.msg))
    sys.exit(1)

captured = {}


def add(nn, st, level, stem, choices, correct, expl, notes):
    captured.update(dict(n=nn, st=st, level=level, stem=stem, choices=choices,
                         correct=correct, expl=expl, notes=notes, kind='mc'))


def add_fill(nn, st, level, stem, correct, accept, expl, notes):
    captured.update(dict(n=nn, st=st, level=level, stem=stem, choices=None,
                         correct=correct, accept=accept, expl=expl, notes=notes, kind='fill'))


exec(compile(raw, p, 'exec'), {'add': add, 'add_fill': add_fill})
if not captured:
    print('🔴 ไฟล์ไม่ได้เรียก add หรือ add_fill เลย')
    sys.exit(1)

s = SPEC[n]
if captured['n'] != n:
    fail('เลขข้อในไฟล์ (%s) ไม่ตรงชื่อไฟล์' % captured['n'])
if captured['kind'] != s[3]:
    fail('ชนิดผิด : ใช้ %s แต่สเปกบอก %s' % (captured['kind'], s[3]))
if captured['st'] != s[1]:
    fail('subTopics ผิด : %r ควรเป็น %r' % (captured['st'], s[1]))
if captured['level'] != s[2]:
    fail('ระดับผิด : %r ควรเป็น %r' % (captured['level'], s[2]))
if captured['stem'] != s[4]:
    fail('ตัวโจทย์ไม่ตรงสเปกทุกตัวอักษร')
if s[3] == 'mc':
    if captured['choices'] != s[5]:
        fail('ตัวเลือกไม่ตรงสเปก')
    if captured['correct'] != s[6]:
        fail('correct ผิด : %r ควรเป็น %r' % (captured['correct'], s[6]))
else:
    if captured['correct'] != s[6]:
        fail('correct ผิด : %r ควรเป็น %r' % (captured['correct'], s[6]))
    if captured.get('accept') != s[7]:
        fail('accept ไม่ตรงสเปก')

expl = captured['expl']
blob = raw

# ── สัญลักษณ์ต้องห้าม ────────────────────────────────────────────────────────
body = '\n'.join(expl) + '\n' + captured['stem'] + '\n' + '\n'.join(captured['choices'] or [])
for sym, why in [('\\frac', 'ใช้ \\dfrac เท่านั้น'), ('√', 'ห้าม √ ดิบ'),
                 ('\\subseteq', 'กฎเหล็ก 9'), ('\\phi', 'กฎเหล็ก 9'),
                 ('มากที่สุดเท่ากับ', 'สำนวนกำกวม'), ('น้อยที่สุดเท่ากับ', 'สำนวนกำกวม'),
                 ('\\"', 'ใช้ “ ” แทน')]:
    if sym in body:
        fail('พบ %r — %s' % (sym, why))
if re.search(r'\d\s*°', body):
    fail('ใช้ ° ดิบ ต้องเป็น ^\\circ')
if re.search(r'<b>[^<]*<b>', body):
    fail('มี <b> ซ้อน <b>')
if re.search(r'ดังรูป|จากรูป', body):
    fail('มีคำว่า “ดังรูป/จากรูป” — ก้อนนี้ไม่มีรูปสักข้อ')
if re.search(r'ข้อมูลเดิม|จากข้อ|ข้างต้น|ข้างบน|โจทย์เดิม|เช่นเดิม|ข้อถัดไป|ข้อก่อน',
             captured['stem']):
    fail('ตัวโจทย์อ้างข้ออื่น (กฎเหล็ก 7)')
if re.search(r'ตัวเลือกที่\s*\d', body):
    fail('พบ “ตัวเลือกที่ N” — ต้องเป็น “ตัวเลือก N”')

# ── คำว่า "ตัวเลือก" ────────────────────────────────────────────────────────
nchoice = len(re.findall(r'ตัวเลือก', body))
if s[3] == 'mc':
    if nchoice != 1:
        fail('คำว่า “ตัวเลือก” ปรากฏ %d ครั้ง (ต้องมี 1 ครั้ง เฉพาะบรรทัด ✅)' % nchoice)
else:
    if nchoice:
        fail('ข้อ fill ห้ามมีคำว่า “ตัวเลือก” แต่พบ %d ครั้ง' % nchoice)

# ── โครง STANDARD v2 ────────────────────────────────────────────────────────
heads = ['📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>', '📐 <b>โจทย์กำหนด</b>',
         '🎯 <b>เป้าหมาย</b>', '✅ <b>คำตอบ</b>', '💡 <b>เทคนิค</b>', '⚠️ <b>จุดพลาด</b>']
for hh in heads:
    if not any(l.startswith(hh) for l in expl):
        fail('เฉลยขาดหัวข้อ %s' % hh)
if not any(l.startswith('✔ <b>ตรวจคำตอบ') for l in expl):
    fail('เฉลยขาด ✔ ตรวจคำตอบ (วิธีอิสระ)')
if not any(l.startswith('<b>【') for l in expl):
    fail('เฉลยขาดบรรทัดชื่อวิธี 【 … 】')
nstep = len([l for l in expl if l.startswith('<b>ขั้นที่ ')])
if nstep < 3:
    fail('มีขั้นที่ %d ขั้น (ต้องอย่างน้อย 3)' % nstep)

ans = [l for l in expl if l.startswith('✅ <b>คำตอบ</b>')]
if len(ans) != 1:
    fail('บรรทัด ✅ คำตอบ มี %d บรรทัด (ต้องมี 1)' % len(ans))
elif s[3] == 'mc':
    want = '→ <b>ตัวเลือก %d</b>' % (s[6] + 1)
    if not ans[0].endswith(want):
        fail('บรรทัด ✅ ไม่ลงท้ายด้วย %r' % want)

for i, l in enumerate(expl):
    if l.count('$') % 2:
        fail('$ ไม่คู่ในบรรทัดเฉลยที่ %d : %r' % (i, l[:60]))

idx = [i for i, l in enumerate(expl) if l.startswith('⚠️ <b>จุดพลาด</b>')]
if idx:
    nreason = len([l for l in expl[idx[0] + 1:] if l.strip()])
    if nreason < 3:
        fail('บรรทัดจุดพลาดมี %d บรรทัด (ต้องอย่างน้อย 3)' % nreason)

nkb = len([l for l in expl[1:] if l.startswith('• ')
           and expl.index(l) < (expl.index('') if '' in expl else 99)])
head0 = expl.index('📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>')
kb = 0
for l in expl[head0 + 1:]:
    if l == '':
        break
    if l.startswith('• '):
        kb += 1
if not (4 <= kb <= 6):
    fail('บล็อกความรู้พื้นฐานมี %d บรรทัด (ต้อง 4-6)' % kb)

# ── notes ──────────────────────────────────────────────────────────────────
nt = captured['notes']
if not nt.startswith('V.mold:'):
    fail('notes ไม่ได้เริ่มด้วย V.mold:')
for kw in ['Rubric', 'Scoring was written before the level was read off.',
           'sympy (verify_b19.py)', 'Collision sweep']:
    if kw not in nt:
        fail('notes ขาดส่วน %r' % kw)
# ⛔ notes เป็นภาษาอังกฤษล้วน — ยกเว้นชื่อระดับสี่คำ ซึ่งแม่แบบก้อน 18 เขียนเป็นคำไทย
#    (`-> level: ง่าย.`) ⇒ ต้องคงธรรมเนียมเดิมไว้ ไม่ให้ก้อน 19 ลอยจากก้อนก่อน
nt_probe = nt
for _lv in ['ยากมาก', 'ปานกลาง', 'ง่าย', 'ยาก']:
    nt_probe = nt_probe.replace(_lv, '')
if re.search(r'[ก-๙]', nt_probe):
    fail('notes ต้องเป็นภาษาอังกฤษล้วน (ยกเว้นชื่อระดับ) แต่พบอักษรไทยอื่น')
if not re.search(r'-> level: (ง่าย|ปานกลาง|ยากมาก|ยาก)', nt):
    fail('notes ต้องมี "-> level: <ชื่อระดับภาษาไทย>" ตามธรรมเนียมก้อน 18')

print('=' * 70)
print('q%03d · %s · %s · เฉลย %d บรรทัด · notes %d ตัวอักษร'
      % (n, captured['kind'], captured['level'], len(expl), len(nt)))
if bad:
    for m in bad:
        print('  🔴 ' + m)
    print('⇒ ยังไม่ผ่าน (%d จุด)' % len(bad))
    sys.exit(1)
print('✅ ผ่านด่านไฟล์เดี่ยวทุกข้อ')

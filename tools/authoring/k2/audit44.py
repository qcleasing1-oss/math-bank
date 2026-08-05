# -*- coding: utf-8 -*-
"""ตรวจสะสมทุกข้อที่แต่งไปแล้ว (k1 9 ข้อ + k2 ที่มีในโฟลเดอร์ out ทั้งหมด · กวาดอัตโนมัติ)"""
import glob, json, io, re, collections, os

FILES = sorted(glob.glob('/home/claude/k1/out/*.json')) + \
        sorted(glob.glob('/home/claude/k2/out/*.json'))

bad = []
ALL = []
for fp in FILES:
    raw = io.open(fp, 'rb').read()
    txt = raw.decode('utf-8')
    d = json.loads(txt)
    # ไบต์ตรงเป๊ะ
    re_dump = json.dumps(d, ensure_ascii=False, indent=2)
    if re_dump != txt:
        bad.append('%s : ไบต์ไม่ตรงกับ json.dumps(indent=2)' % os.path.basename(fp))
    if b'\r' in raw:
        bad.append('%s : มี CRLF' % os.path.basename(fp))
    if txt.endswith('\n'):
        bad.append('%s : มีขึ้นบรรทัดท้ายไฟล์' % os.path.basename(fp))
    for q in d['questions']:
        ALL.append((os.path.basename(fp), q))

print('ไฟล์', len(FILES), 'ไฟล์ ·', len(ALL), 'ข้อ')

ids = [q['id'] for _, q in ALL]
if len(set(ids)) != len(ids):
    dup = [k for k, v in collections.Counter(ids).items() if v > 1]
    bad.append('id ซ้ำ: %s' % dup)

nums = sorted(q['questionNumber'] for _, q in ALL)
if nums != list(range(1, len(nums) + 1)):
    bad.append('เลขข้อไม่ต่อเนื่อง 1..%d : %s' % (len(nums), nums))

sets = set(q['setId'] for _, q in ALL)
if len(sets) != 1:
    bad.append('setId ไม่เดียว: %s' % sets)
tags = set(q['sourceTag'] for _, q in ALL)
if len(tags) != 1:
    bad.append('sourceTag ไม่เดียว: %s' % tags)

stems = collections.Counter()
CROSS = re.compile(r'ข้อมูลเดิม|จากข้อ|ข้างต้น|ข้างบน|โจทย์เดิม|เช่นเดิม|ข้อถัดไป|ข้อก่อน')
for fn, q in ALL:
    qid = q['id']
    if q.get('hasImage') is not False:
        bad.append('%s : hasImage ไม่ใช่ false' % qid)
    if 'imageSpec' in q:
        bad.append('%s : มี imageSpec' % qid)
    # ── ⭐ ก้อน 19 เปิดชนิด fill เป็นครั้งแรกของชุด ⇒ ด่านนี้ต้องแยกสองสาย ──────────
    #    ⛔ ไม่ได้ผ่อนกฎของ mc แม้แต่ข้อเดียว · สาย fill มีด่านของตัวเองที่เข้มพอกัน
    #    (ถ้าปล่อยให้ fill ลอดไปโดยไม่ตรวจ ด่านจะเขียวทั้งที่ตรวจไม่ครบ — กับดักเดิมของด่าน 7)
    if q.get('type') not in ('mc', 'fill'):
        bad.append('%s : type ไม่ใช่ mc หรือ fill' % qid)
    if q.get('type') == 'mc':
        if len(q.get('choices', [])) != 4:
            bad.append('%s : ตัวเลือกไม่ครบ 4' % qid)
        elif len(set(q['choices'])) != len(q['choices']):
            bad.append('%s : ตัวเลือกซ้ำกันเอง' % qid)
    else:
        if 'choices' in q:
            bad.append('%s : ข้อ fill ต้องไม่มีสนาม choices' % qid)
        if not isinstance(q.get('correct'), str) or not q['correct'].strip():
            bad.append('%s : ข้อ fill ต้องมี correct เป็นสตริงที่ไม่ว่าง' % qid)
        acc = q.get('accept')
        if not isinstance(acc, list) or not acc:
            bad.append('%s : ข้อ fill ต้องมีสนาม accept เป็นลิสต์ที่ไม่ว่าง' % qid)
        elif q.get('correct') not in acc:
            bad.append('%s : ข้อ fill มี accept ที่ไม่มีคำตอบหลักอยู่ในนั้น' % qid)
        elif len(set(acc)) != len(acc):
            bad.append('%s : ข้อ fill มีรูปแบบซ้ำในลิสต์ accept' % qid)
    if q.get('difficulty') not in ('ง่าย', 'ปานกลาง', 'ยาก', 'ยากมาก'):
        bad.append('%s : ระดับผิด %r' % (qid, q.get('difficulty')))
    st = q['question']
    stems[st] += 1
    if CROSS.search(st):
        bad.append('%s : ผิดกฎเหล็ก 7 (อ้างข้ออื่น)' % qid)
    s = json.dumps(q, ensure_ascii=False)
    if '\\"' in s:
        bad.append('%s : มี backslash-quote' % qid)
    for b in ('\\subseteq', '\\subsetneq', '\\nsubseteq', '\\phi', '\\varphi',
              '\\mathbb{I}', '^c', 'คาร์ดินาลิตี', 'มากที่สุดเท่ากับ', 'น้อยที่สุดเท่ากับ'):
        if b in s:
            bad.append('%s : พบสัญลักษณ์ต้องห้าม %s' % (qid, b))
    if re.search(r'\\frac', s):
        bad.append('%s : ใช้ \\frac (ต้องใช้ \\dfrac)' % qid)
    if '√' in s:
        bad.append('%s : มี √ ดิบ' % qid)
    # ⚠️ ต้องมีเหตุผล >= 3
    ex = q['explanation']
    try:
        i = next(k for k, l in enumerate(ex) if l.startswith('⚠️'))
    except StopIteration:
        bad.append('%s : ไม่มีบล็อก ⚠️' % qid); continue
    reasons = [l for l in ex[i + 1:] if l.strip()]
    if len(reasons) < 3:
        bad.append('%s : ⚠️ มีเหตุผลแค่ %d บรรทัด' % (qid, len(reasons)))
    # ✅ บรรทัดเดียว และลงท้ายถูกช่อง
    ok = [l for l in ex if l.startswith('✅')]
    if len(ok) != 1:
        bad.append('%s : บรรทัด ✅ มี %d บรรทัด' % (qid, len(ok)))
    elif q.get('type') == 'mc':
        if not ok[0].rstrip().endswith('<b>ตัวเลือก %d</b>' % (q['correct'] + 1)):
            bad.append('%s : ✅ ไม่ลงท้ายด้วยตัวเลือก %d' % (qid, q['correct'] + 1))
    # ห้ามมีคำว่า ตัวเลือก N ที่อื่น
    others = [l for l in ex if not l.startswith('✅') and re.search(r'ตัวเลือก\s*[1-4]', l)]
    if others:
        bad.append('%s : มีคำว่า ตัวเลือก N นอกบรรทัด ✅ (%d จุด)' % (qid, len(others)))
    # ⭐ ข้อ fill ไม่มีช่องให้เลือก ⇒ คำว่า "ตัวเลือก" ต้องไม่ปรากฏเลยทั้งข้อ
    if q.get('type') == 'fill' and 'ตัวเลือก' in json.dumps(q, ensure_ascii=False):
        bad.append('%s : ข้อ fill มีคำว่า “ตัวเลือก”' % qid)

for st, c in stems.items():
    if c > 1:
        bad.append('โจทย์ซ้ำคำต่อคำ %d ครั้ง: %s' % (c, st[:60]))

print()
print('── สรุประดับ ──')
for lv in ('ง่าย', 'ปานกลาง', 'ยาก', 'ยากมาก'):
    print('  %-8s %d' % (lv, sum(1 for _, q in ALL if q['difficulty'] == lv)))
print('── สรุปช่องคำตอบ ──')
cc = collections.Counter(q['correct'] + 1 for _, q in ALL if q.get('type') == 'mc')
nmc = sum(1 for _, q in ALL if q.get('type') == 'mc')
nfill = sum(1 for _, q in ALL if q.get('type') == 'fill')
for k in (1, 2, 3, 4):
    print('  ช่อง %d : %d' % (k, cc[k]))
print('  (นับจากข้อปรนัย %d ข้อ · ข้อ fill อีก %d ข้อไม่มีช่องคำตอบ ⇒ %.0f%% ของชุดเป็น fill)'
      % (nmc, nfill, 100.0 * nfill / (nmc + nfill)))
print('── สรุปหัวข้อย่อย ──')
sc = collections.Counter(s for _, q in ALL for s in q['subTopics'])
for k in sorted(sc, key=lambda x: [int(y) for y in x.split('.')]):
    print('  %-6s %d' % (k, sc[k]))

print()
if bad:
    print('❌ พบปัญหา', len(bad), 'จุด')
    for b in bad:
        print('   ·', b)
else:
    print('✅ ผ่านทุกด่านสะสม ·', len(ALL), 'ข้อ · 0 ปัญหา')

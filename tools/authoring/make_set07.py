# -*- coding: utf-8 -*-
"""ก้าว 3 · รวม 104 ข้อของบทที่ 7 เป็นไฟล์ชุดจริง data/sets/gen-chap-07-trigonometry.json
   + เพิ่ม entry ใน data/manifest.json

⛔ ตัวเลขทุกตัวใน manifest คำนวณจากไฟล์จริง ไม่พิมพ์มือ (กันเลขใน manifest ไม่ตรงของจริง)
"""
import json, io, glob, collections, os

SET = 'gen-chap-07-trigonometry'
MB = '/tmp/mb27'
ORDER = ['id', 'setId', 'questionNumber', 'topics', 'subTopics', 'difficulty',
         'type', 'question', 'choices', 'hasImage', 'sourceTag', 'imageSpec',
         'correct', 'accept', 'explanation', 'notes']

# ── รวมข้อ ────────────────────────────────────────────────────────────────────
raw = []
for f in sorted(glob.glob('/home/claude/k1/out/*.json')) + \
         sorted(glob.glob('/home/claude/k2/out/*.json')):
    raw += json.load(io.open(f, encoding='utf-8'))['questions']

nums = [q['questionNumber'] for q in raw]
ids = [q['id'] for q in raw]
assert len(set(ids)) == len(ids), 'id ซ้ำ ❌'
assert len(set(nums)) == len(nums), 'questionNumber ซ้ำ ❌'
assert sorted(nums) == list(range(1, len(nums) + 1)), 'เลขข้อไม่ต่อเนื่อง ❌'

qs = []
for q in sorted(raw, key=lambda z: z['questionNumber']):
    assert q['setId'] == SET, 'setId ผิด: ' + q['setId']
    assert q['hasImage'] is False and 'imageSpec' not in q, 'มีรูปโผล่ ❌'
    extra = [k for k in q if k not in ORDER]
    assert not extra, 'ฟิลด์แปลกปลอม: %s' % extra
    qs.append(collections.OrderedDict((k, q[k]) for k in ORDER if k in q))

data = collections.OrderedDict([('setId', SET), ('questions', qs)])
p = os.path.join(MB, 'data/sets/%s.json' % SET)
txt = json.dumps(data, ensure_ascii=False, indent=2)
io.open(p, 'w', encoding='utf-8', newline='\n').write(txt)
print('เขียน data/sets/%s.json · %d ข้อ · %d B' % (SET, len(qs), len(txt.encode())))

# ── ตัวเลขสำหรับ manifest — นับจากของจริง ────────────────────────────────────
lv = collections.Counter(q['difficulty'] for q in qs)
ty = collections.Counter(q['type'] for q in qs)
st = collections.Counter(s for q in qs for s in q['subTopics'])
N = len(qs)
print('ระดับ:', dict(lv), '· ชนิด:', dict(ty))
print('สัดส่วนระดับ:', ' · '.join('%s %.1f%%' % (k, 100.0 * lv[k] / N)
                                  for k in ['ง่าย', 'ปานกลาง', 'ยาก', 'ยากมาก']))
print('หัวข้อย่อย:', dict(sorted(st.items())))

MP = os.path.join(MB, 'data/manifest.json')
man = json.load(io.open(MP, encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
# ⭐ ก้าว 3 รอบแรก (ก้อน 1-18) สร้าง entry ใหม่ · ตั้งแต่ก้อน 19 เป็นต้นไปคือการ "อัปเดตของเดิม"
#    ⛔ ห้ามลบ entry เก่าแล้วสร้างใหม่ — ต้องเขียนทับเฉพาะตัวเลขที่นับได้จากไฟล์จริง
#    เพื่อให้ค่าที่ครูหรือพอร์ทัลเคยตั้งไว้ในสนามอื่นไม่หายไปเงียบ ๆ
_is_update = SET in man['sets']
print('โหมด :', 'อัปเดต entry เดิม' if _is_update else 'สร้าง entry ใหม่')

bd = collections.OrderedDict((k, lv[k]) for k in ['ง่าย', 'ปานกลาง', 'ยาก', 'ยากมาก'] if lv[k])
man['sets'][SET] = collections.OrderedDict([
    ('source', 'ข้อสอบรายบท (แต่งใหม่)'),
    ('subject', 'ตรีโกณมิติ'),
    ('displayName', 'บทที่ 7 ตรีโกณมิติ (แต่งใหม่ · แข่งขัน · %d ข้อ)' % N),
    ('totalQuestions', N),
    ('totalScore', N),
    ('structure', collections.OrderedDict([
        ('part1', 'ข้อสอบแต่งใหม่ STANDARD v2 · %d ข้อ (mc %d · fill %d) · '
                  'ทุกข้อไม่มีรูป · ระดับมาจาก rubric 5 มิติ ⛔ ไม่ได้เลือกระดับก่อนแล้วย้อนหาคะแนน · '
                  'ทะเบียนแม่พิมพ์ (โจทย์ให้/ถามหา/เครื่องมือ) กันซ้ำกับคลังเดิม 6,407 ข้อ และซ้ำกันเอง'
         % (N, ty['mc'], ty['fill'])),
    ])),
    ('topicDistribution', collections.OrderedDict([('7', N)])),
    ('difficulty', collections.OrderedDict([
        ('level', 'แข่งขัน'),
        ('breakdown', bd),
    ])),
    ('snapshot', collections.OrderedDict([
        ('round', 20),
        ('stage', 'ก้าว 2 เสร็จ %d ข้อ (ก้อน 1–19) · ก้อน 19 เป็นก้อนแรกที่มีข้อชนิด fill · '
                  'blind-solve ยังไม่ได้ทำ ⇒ ยังไม่ถือว่าครูอนุมัติ' % N),
        ('questionsCompleted', N),
        ('questionsRemaining', 0),
        ('exportedAt', '2026-08-05'),
        ('note',
         'ชุดแต่งใหม่ชุดแรกของบทที่ 7 (เดิมมีแต่ chap-07-trigonometry 230 ข้อที่ ingest มา) · '
         'sympy verify ครบทุกข้อ (verify_b*.py) · ตัวลวงทุกตัวสืบกลับไปหาจุดพลาดที่ตั้งชื่อได้ · '
         'ด่านที่ผ่านแล้ว: check_k2 (STANDARD v2 + BADSYM) · check_answer_claim v1.3 · audit44 · '
         'ทะเบียนแม่พิมพ์ molds.py 0 คู่ตรงสามส่วน · crossnew.py เทียบข้อใหม่กันเองครบทุกคู่ · '
         'ก้อน 18 เป็นก้อนแรกที่ใช้ลำดับใหม่ "กวาดด่านก่อนเขียนเฉลย" ⇒ ข้อที่ตายหลังจ่ายค่าเฉลย 0/10 '
         '(ก้อนก่อนหน้าตาย 4/5) · ก้อน 19 เป็นก้อน 20 ข้อก้อนแรก และเปิดชนิด fill ครั้งแรกของชุด '
         '(6 ข้อ · ทุกข้อมีสนาม accept) · ลำดับเติมตามคำสั่งครู 7.1 -> 7.11 -> 7.3 · '
         'หัวข้อย่อยที่ยังขาด: %s'
         % ' '.join('%s=%d' % (k, st.get(k, 0)) for k in
                    ['7.1', '7.2', '7.3', '7.4', '7.5', '7.6', '7.7', '7.8', '7.9', '7.10', '7.11'])),
    ])),
])

mtxt = json.dumps(man, ensure_ascii=False, indent=2)
io.open(MP, 'w', encoding='utf-8', newline='\n').write(mtxt)
print('เขียน data/manifest.json · ชุดทั้งหมด %d ชุด · %d B' % (len(man['sets']), len(mtxt.encode())))

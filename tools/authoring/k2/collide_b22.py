# -*- coding: utf-8 -*-
"""กวาดชนก้อน 22 (q165-q184) กับ **คลังจริงทั้งหมด** · 8 ส.ค. 69

⛔ ทำไมต้องกวาดทั้งที่ `_SPEC.md` ยืนยันกลางผ่าน 71/0 แล้ว
   verify_b22 ตรวจว่า **คำตอบถูก** ⛔ ไม่ได้ตรวจว่า **ข้อนี้เคยมีแล้วหรือยัง**
   สองเรื่องนี้คนละเรื่องกัน (㊸ : ด่านตรวจได้เฉพาะสิ่งที่มันมองเห็นจากที่ที่มันยืน)

⭐ กฎที่บังคับใช้รอบนี้
   (1) โพรบทุกตัว qonly=True — ตัดสินจาก**ตัวโจทย์** ⛔ ไม่ใช่จากเฉลย
   (2) กวาด `data/sets/*.json` ทั้ง 63 ชุด ⛔ ไม่ใช่เฉพาะชุดตรีโกณ (บทเรียนก้อน 12)
   (3) คำไทยสั้นต้องมีคำขยายประกบ (บทเรียนก้อน 17 : 'ล้อ' ชนใน 'สอดคล้อง')
   (4) 🔑 regex ไทย : `(?:คำ)?` ⛔ ไม่ใช่ `คำ?` — `ที่` = 3 จุดรหัส (㊶)
   (5) ㊶ : ตัวกวาดที่เป็น regex ต้องมีชุดทดสอบของตัวเอง **ทั้งเคสจับและเคสปล่อย**
       และเคสต้องคัดมาจาก**ของจริงในคลัง** ⛔ ไม่ใช่เคสที่ผมคิดเอง
"""
import io, os, re, json, glob, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
SETS = sorted(glob.glob(os.path.join(ROOT, 'data', 'sets', '*.json')))

items = []
for p in SETS:
    d = json.load(io.open(p, encoding='utf-8'))
    for q in d.get('questions', []):
        q['_src'] = os.path.basename(p).replace('.json', '')
        items.append(q)
seen, uniq = set(), []
for q in items:
    if q['id'] in seen:
        continue
    seen.add(q['id'])
    uniq.append(q)
items = uniq
print('ฐานเทียบ %d ชุด · %d ข้อ (ที่ทำงาน · วัด 8 ส.ค. 69)' % (len(SETS), len(items)))

# ข้อของก้อน 22 ยังไม่เข้าคลัง ⇒ ทุกฮิตที่เจอคือ "ของเดิม" ทั้งหมด
B22 = set('q%03d' % n for n in range(165, 185))
assert not [q for q in items if q['_src'].startswith('gen-chap-07') and q['id'][-4:] in B22], \
    'ก้อน 22 เข้าคลังไปแล้ว — ตรรกะของสคริปต์นี้ใช้ไม่ได้'


def qtext(q):
    return q.get('question') or ''


# ═══════════════════ ชุดทดสอบของตัวกวาดเอง (㊶) ═══════════════════
# เคสทุกตัวคัดจาก **ตัวโจทย์จริงในคลัง** ⛔ ไม่ใช่ประโยคที่ผมแต่งเอง
_REAL = {}
for q in items:
    _REAL[q['id']] = qtext(q)


def _t(pattern, item_id, want, why):
    got = bool(re.search(pattern, _REAL[item_id]))
    assert got == want, 'selftest ตัวกวาดล้ม: %s กับ %s ควรได้ %s (%s)' % (
        pattern, item_id, want, why)


# 🔻 ใบแก้ตัวกวาด (㊷ · แก้ **เครื่องมือ** ⛔ ไม่ใช่แก้คำตอบที่เขียนไว้)
#   selftest เคสแรกล้มทันทีที่รัน : q090 คือ `\cos^2 15^{\circ} - \sin^2 15^{\circ}` จริง
#   แต่ regex ของผมเขียน `\^\\circ` เฉย ๆ ⇒ ไม่รับรูปที่มีปีกกา
#   วัดจากคลังจริง : `^{\circ}` 37 จุด · `^\circ` 163 จุด ⇒ **มีทั้งสองรูป ต้องรับทั้งคู่**
#   ถ้าไม่มี selftest ตัวนี้ ตัวกวาดจะรายงาน "ไม่เจอของเดิม" แบบเขียว ๆ โดยตกไป 37 จุด (㊶)
DEG = r'\^\s*\{?\\circ\}?'

# ═══════════════════ ตารางโพรบ ═══════════════════
# (ข้อของเรา, ชื่อแม่พิมพ์, regex)  — regex เขียนให้จับ "รูปทรงคณิตศาสตร์" ⛔ ไม่ใช่สำนวน
PROBES = [
 ('q165', 'ผลบวกสองมุมแหลมจากค่า tan สองค่า',
  r'\\tan\s*A\s*=.{0,40}\\tan\s*B\s*='),
 ('q166', 'ค่าตรีโกณของมุม 105/15/75 องศา (มุมไม่พิเศษ)',
  r'\\(?:sin|cos|tan)\s*(?:\^\s*\{?2\}?\s*)?(?:105|15|75|165|195|255|285)\s*' + DEG),
 ('q167', 'ให้ tan ของผลบวกและผลต่าง แล้วถามมุมสองเท่า',
  r'\\tan\s*\(\s*A\s*(?:\{)?\s*\+.{0,30}\\tan\s*\(\s*A\s*(?:\{)?\s*-'),
 ('q168', 'ให้สองอัตราส่วนในสองจตุภาค แล้วถาม sin ของผลบวก/ผลต่าง',
  r'จตุภาคที่\s*\d.{0,120}จตุภาคที่\s*\d'),
 ('q169', 'ให้ cos ของผลบวก แล้วถามผลคูณ tan',
  r'\\tan\s*A\s*\\?,?\s*\\tan\s*B|\\tan\s*A\s*\\tan\s*B'),
 ('q170', 'ผลบวกสามมุมจากค่า tan สามค่า',
  r'\\tan\s*A\s*=.{0,80}\\tan\s*B\s*=.{0,80}\\tan\s*C\s*='),
 ('q171', 'ผลบวกของค่าอาร์กสองตัวที่อาร์กิวเมนต์พิเศษ',
  r'\\arc(?:sin|cos|tan)\s*\\?left?\(?.{0,30}\+\s*\\arc(?:sin|cos|tan)'),
 ('q172', 'ตรีโกณของค่าอาร์ก (sin ของ arccos ฯลฯ)',
  r'\\(?:sin|cos|tan)\s*\\?left?\(?\s*\\arc(?:sin|cos|tan)'),
 ('q173', 'อาร์กของตรีโกณของมุมนอกช่วงหลัก (arcsin(sin x))',
  r'\\arc(sin|cos|tan)\s*\\?left?\(?\s*\\\1\b'),
 ('q174', 'ตรีโกณของผลบวกอาร์กสองตัว',
  r'\\(?:sin|cos|tan)\s*\\?left?\(?\s*\\arc(?:sin|cos|tan).{0,60}\+\s*\\arc'),
 ('q175', 'ฟังก์ชันที่เป็นผลบวกอาร์กแทนเจนต์สองพจน์ของ x',
  r'\\arctan\s*x|\\arctan\s*\\?left?\(?\s*x'),
 ('q176', 'สมการอาร์ก = สองเท่าของอาร์ก',
  r'\\arcsin\s*x\s*=|=\s*2\s*\\arctan'),
 ('q177', 'สายลาดยาว L ให้ tan ของมุมลาด แล้วถามความสูงที่ไต่ได้',
  r'(?:กระเช้า|เคเบิล|ลิฟต์|สายพาน|กระเช้าลอยฟ้า)'),
 ('q178', 'ความสูงกับความยาวเงาบนพื้นราบ แล้วถามมุมเงย',
  r'เงา.{0,80}(?:มุมเงย|มุมที่แสง)|(?:มุมเงย|มุมที่แสง).{0,80}เงา'),
 ('q179', 'สามเหลี่ยม SAS ตัวเลข แล้วถามด้านที่สาม (กฎของโคไซน์)',
  r'60\s*' + DEG + r'.{0,60}(?:ยาว|หน่วย|เมตร)|(?:ยาว|หน่วย|เมตร).{0,60}60\s*' + DEG),
 ('q180', 'มุมเงยสองค่าจากจุดเดียว ไปยังโคนกับยอดของสิ่งที่อยู่บนอาคาร',
  r'มุมเงย.{0,140}(?:30|45|60)\s*' + DEG + r'.{0,140}มุมเงย'),
 ('q181', 'ผลบวกคำตอบของสมการตรีโกณชั้นเดียวในหนึ่งรอบ',
  r'ผลบวก(?:ของ)?คำตอบ.{0,80}สมการ|สมการ.{0,120}ผลบวก(?:ของ)?คำตอบ'),
 ('q182', 'สมการกำลังสองในฟังก์ชันตรีโกณตัวเดียว',
  r'\\(?:sin|cos|tan)\s*\^\s*\{?2\}?\s*x.{0,40}[+-].{0,10}\\(?:sin|cos|tan)\s*x'),
 ('q183', 'sin x + cos x = ค่าคงที่',
  r'\\sin\s*x\s*\+\s*\\cos\s*x\s*=|\\cos\s*x\s*\+\s*\\sin\s*x\s*='),
 ('q184', 'ผลบวกกำลังคู่ของ sin กับ cos เท่ากับอะไรสักอย่าง',
  r'\\sin\s*\^\s*\{?([468])\}?\s*x\s*\+\s*\\cos\s*\^\s*\{?\1\}?\s*x'),
]

# ── ชุดทดสอบ: ต้องจับ (ของจริงที่รู้คำตอบอยู่แล้ว) ───────────────────────────
_t(PROBES[1][2],  'gen-chap-07-trigonometry-q090', True,  'q090 = cos^2 15° - sin^2 15°')
_t(PROBES[3][2],  'gen-chap-07-trigonometry-q097', True,  'q097 มีสองจตุภาคในโจทย์')
_t(PROBES[4][2],  'gen-chap-07-trigonometry-q087', True,  'q087 ถาม tan A tan B')
_t(PROBES[6][2],  'gen-chap-07-trigonometry-q081', True,  'q081 = arccos(1/2) + arcsin(√3/2)')
_t(PROBES[8][2],  'gen-chap-07-trigonometry-q051', True,  'q051 มี arcsin(sin ...)')
_t(PROBES[17][2], 'gen-chap-07-trigonometry-q102', True,  'q102 = 2cos^2 x - 3cos x + 1 = 0')
_t(PROBES[19][2], 'gen-chap-07-trigonometry-q079', True,  'q079 = sin^8 x + cos^8 x')
# ── ชุดทดสอบ: ต้อง**ปล่อย** (ของจริงที่ไม่ควรโดนจับ) ─────────────────────────
_t(PROBES[1][2],  'gen-chap-07-trigonometry-q012', False, 'q012 = tan120 + cot135 ไม่ใช่มุม 105/15/75')
_t(PROBES[3][2],  'gen-chap-07-trigonometry-q051', False, 'q051 ไม่ได้พูดถึงจตุภาคเลย')
_t(PROBES[6][2],  'gen-chap-07-trigonometry-q067', False, 'q067 มี arccos ตัวเดียว ไม่ใช่ผลบวก')
_t(PROBES[8][2],  'gen-chap-07-trigonometry-q081', False, 'q081 เป็นผลบวกอาร์ก ⛔ ไม่ใช่อาร์กซ้อนตรีโกณ')
_t(PROBES[18][2], 'gen-chap-07-trigonometry-q103', False, 'q103 = sin 3x = cos 2x ⛔ ไม่ใช่ sin x + cos x')
_t(PROBES[19][2], 'gen-chap-07-trigonometry-q184' if False else
                  'gen-chap-07-trigonometry-q102', False, 'q102 ไม่มีกำลังคู่ 4/6/8')
print('✅ selftest ตัวกวาด: 13 เคส (จับ 7 · ปล่อย 6) — ทุกเคสคัดจากของจริงในคลัง')
print()

TRIG_ONLY = '--trig' in sys.argv
rows = []
for tag, name, rx in PROBES:
    hit = [q for q in items if re.search(rx, qtext(q))]
    if TRIG_ONLY:
        hit = [q for q in hit if '07-trigonometry' in q['_src'] or 'chap-07' in q['_src']]
    rows.append((tag, name, hit))
    flag = '🔴' if hit else '✅'
    print('%s %s · %s — เจอ %d ข้อ' % (flag, tag, name, len(hit)))
    for q in hit[:8]:
        print('     %-38s %-8s %-9s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), qtext(q).replace('\n', ' ')[:96]))
    if len(hit) > 8:
        print('     ... อีก %d ข้อ' % (len(hit) - 8))

print()
print('═' * 78)
print('สรุป: โพรบที่เจอของเดิม %d จาก %d' % (len([r for r in rows if r[2]]), len(rows)))
print('⛔ "เจอ" ⛔ ไม่ได้แปลว่าซ้ำ — แปลว่า **ต้องเปิดดูด้วยตา** (กฎเหล็กข้อ 5 = ต่าง 2 ใน 3 แกน)')

# -*- coding: utf-8 -*-
"""ด่านพิสูจน์ว่า "ไฟล์ชุดในคลัง = ผลผลิตของเครื่องมือชุดนี้ ตรงทุกไบต์"

ทำไมต้องมี: tools/authoring/ เก็บ **ต้นทาง** ของข้อ (parts_b*/) ส่วน data/sets/ เก็บ
**ผลผลิต** ⇒ ของสองชุดนี้ลอยจากกันได้ถ้าใครแก้ฝั่งเดียว · ด่านนี้ทำให้การซ้ำซ้อนนั้น
กลายเป็น "ของที่ตรวจได้" แทนที่จะเป็น "หนี้ที่รอระเบิด"

วิธีใช้ (หลัง bootstrap.sh):
    python3 tools/authoring/regen_check.py
ผ่าน = exit 0 · ไม่ตรง = exit 1 พร้อมบอกว่าต่างกี่ข้อ ข้อไหน
"""
import json, io, glob, collections, os, sys, subprocess, hashlib

SET = 'gen-chap-07-trigonometry'
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIVE = os.path.join(REPO, 'data/sets/%s.json' % SET)
ORDER = ['id', 'setId', 'questionNumber', 'topics', 'subTopics', 'difficulty',
         'type', 'question', 'choices', 'hasImage', 'sourceTag', 'imageSpec',
         'correct', 'accept', 'explanation', 'notes']

raw = []
# ⛔ ไม่ใช้ ~ และไม่รับสวิตช์เปลี่ยนที่ทำงาน — สคริปต์ทั้ง 175 ตัวตรึงพาธนี้ไว้ในตัวเอง
#    (ถ้าเปิดให้เปลี่ยนได้ ตัวสร้างจะขึ้น ✅ แต่เขียนของลงที่เดิม ⇒ ด่านเขียวทั้งที่ของผิดที่)
WORK = '/home/claude'
for f in sorted(glob.glob(WORK + '/k1/out/*.json')) + \
         sorted(glob.glob(WORK + '/k2/out/*.json')):
    raw += json.load(io.open(f, encoding='utf-8'))['questions']
if not raw:
    print('❌ ไม่พบผลผลิตใน ~/k1/out หรือ ~/k2/out — รัน bootstrap.sh ก่อน (ที่ทำงาน %s)' % WORK)
    sys.exit(1)

qs = [collections.OrderedDict((k, q[k]) for k in ORDER if k in q)
      for q in sorted(raw, key=lambda z: z['questionNumber'])]
txt = json.dumps(collections.OrderedDict([('setId', SET), ('questions', qs)]),
                 ensure_ascii=False, indent=2)
new = txt.encode('utf-8')
live = io.open(LIVE, 'rb').read()

def h(b):
    return hashlib.sha1(b'blob %d\x00' % len(b) + b).hexdigest()

print('สร้างใหม่จากเครื่องมือ : %d ข้อ · %d B · blob %s' % (len(qs), len(new), h(new)))
print('ไฟล์ในคลัง            : %d B · blob %s' % (len(live), h(live)))

if new == live:
    print('✅ ตรงกันทุกไบต์ — เครื่องมือชุดนี้สร้างของในคลังกลับมาได้ครบ')
    sys.exit(0)

a = {q['id']: q for q in qs}
b = {q['id']: q for q in json.load(io.open(LIVE, encoding='utf-8'))['questions']}
only_new = sorted(set(a) - set(b)); only_live = sorted(set(b) - set(a))
diff = sorted(k for k in set(a) & set(b) if a[k] != b[k])
print('❌ ไม่ตรง · มีแต่ในเครื่องมือ %d · มีแต่ในคลัง %d · เนื้อต่าง %d'
      % (len(only_new), len(only_live), len(diff)))
for k in (only_new[:5] + only_live[:5] + diff[:5]):
    print('   ', k)
sys.exit(1)

# -*- coding: utf-8 -*-
"""ตัวจับ “ซ้ำเชิงโครงสร้าง” v3 · เทียบทุกข้อที่เราแต่งเอง กับทั้งฐาน 6,357 ข้อ

═══ เหตุที่ต้องมีเครื่องมือนี้ ═══
การกวาดด้วยคำสำคัญ (collide_*.py) พลาดคู่ q025 ↔ q040 ไปได้
เพราะ q025 เขียนความหมายว่า “คาบ” ด้วยสัญลักษณ์ $f(x+T)=f(x)$ ล้วน ๆ ไม่มีคำไทยให้จับเลย
⇒ ต้องมีตัวจับที่ไม่พึ่งคำสำคัญ แต่ดู “โครงของถ้อยคำ” หลังลบตัวเลขทิ้งทั้งหมด

═══ บทเรียนที่ 1 · ภาษาไทยไม่เว้นวรรค ═══
v1 ตัดคำด้วยช่องว่าง ⇒ ล้มเหลว ทั้งประโยค “เป็นจำนวนจริงบวกที่น้อยที่สุดซึ่งทำให้”
กลายเป็น token เดียว ลายนิ้วมือเหลือ 5–6 token และมองไม่เห็นความหมาย (q025↔q040 ได้แค่ 0.375)
⇒ v2 เปลี่ยนไปใช้ n-gram ระดับตัวอักษร ซึ่งเป็นวิธีมาตรฐานของภาษาที่ไม่เว้นวรรค

═══ บทเรียนที่ 2 · ถ้อยคำสำเร็จรูปกลบสัญญาณ ═══
v2 จับคู่ q025↔q040 ได้จริง (con 0.58) แต่**จมอยู่อันดับ 5+**
เพราะคู่ปลอมอย่าง “ค่าของ …​ เท่ากับข้อใดต่อไปนี้” ได้ con 1.00 ลอยขึ้นมาบังหมด
วัดจากคลังจริง: “ให้” โผล่ 42% · “ต่อไปนี้” 40% · “ข้อใดต่อไปนี้” 34% · “ถ้า” 32% · “แล้ว” 30%
⇒ v3 **ลบถ้อยคำสำเร็จรูปทิ้งก่อนทำลายนิ้วมือ** และบังคับให้ต้องมีส่วนทับซ้อนขั้นต่ำจริง ๆ

วิธี: ลบถ้อยคำสำเร็จรูป → ลบตัวเลขและคำสั่ง LaTeX (เหลือชื่อฟังก์ชันเป็น @sin)
      → ตัด n-gram ตัวอักษรยาว 5 → วัด Jaccard และ Containment
      คู่ที่ “พูดเรื่องเดียวกัน ต่างแค่ตัวเลข” = กรณีที่ผิดกฎเหล็กข้อ 5 พอดี จะโผล่ทันที
"""
import glob, json, re, io, sys

N = 5          # ความยาว n-gram ระดับตัวอักษร
MINGRAM = 20   # โครงสั้นกว่านี้ ลายนิ้วมือไม่น่าเชื่อถือ ⇒ ข้าม
MININT = 12    # ต้องทับซ้อนกันอย่างน้อยเท่านี้ n-gram จึงจะนับ (กันคู่ปลอมจากข้อสั้น)

# ── ถ้อยคำสำเร็จรูป · เรียงจากยาวไปสั้น (ลบตัวยาวก่อน) ──
BOILER = [
    'มีค่าเท่ากับข้อใดต่อไปนี้', 'มีค่าตรงกับข้อใดต่อไปนี้', 'เท่ากับข้อใดต่อไปนี้',
    'ตรงกับข้อใดต่อไปนี้', 'สอดคล้องกับข้อใดต่อไปนี้', 'ข้อใดต่อไปนี้ถูกต้อง',
    'ข้อใดต่อไปนี้เป็นจริง', 'ข้อใดต่อไปนี้', 'เท่ากับข้อใด', 'ตรงกับข้อใด',
    'มีค่าเท่ากับ', 'เท่ากับเท่าใด', 'คือข้อใด', 'ในข้อใด', 'ต่อไปนี้',
    'กำหนดให้', 'ค่าของ', 'โดยที่', 'แล้ว', 'ถ้า', 'เมื่อ', 'ให้',
]

MINE, ALL = [], []
for fp in sorted(glob.glob('/tmp/mb27/data/sets/*.json')):
    for q in json.load(io.open(fp, encoding='utf-8')).get('questions', []):
        ALL.append(('คลัง', q))
for fp in sorted(glob.glob('/home/claude/k1/out/*.json')) + \
          sorted(glob.glob('/home/claude/k2/out/*.json')):
    for q in json.load(io.open(fp, encoding='utf-8')).get('questions', []):
        ALL.append(('ใหม่', q))
        MINE.append(q)


def stem(q):
    s = q.get('question')
    if isinstance(s, list):
        s = ' '.join(x for x in s if isinstance(x, str))
    return (s or '').replace('\n', ' ')


FN = ('arcsin|arccos|arctan|sin|cos|tan|cot|sec|csc|sqrt|pi|theta|alpha|beta|log')


def norm(s):
    """โครงของถ้อยคำ: เก็บชื่อฟังก์ชันไว้ ทิ้งถ้อยคำสำเร็จรูป ตัวเลข และสัญลักษณ์ที่เหลือ"""
    s = re.sub(r'\\(' + FN + r')(?![a-zA-Z])', r' @\1 ', s)   # ชื่อฟังก์ชัน → @sin
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)                        # คำสั่ง LaTeX อื่น ทิ้ง
    s = re.sub(r'[0-9]+', ' ', s)                             # ⭐ ทิ้งตัวเลขทั้งหมด
    for b in BOILER:                                          # ⭐ ทิ้งถ้อยคำสำเร็จรูป
        s = s.replace(b, ' ')
    s = re.sub(r'[^฀-๿a-zA-Z@]+', '', s)                      # เหลือไทย + ชื่อฟังก์ชัน
    return s


def grams(s):
    s = norm(s)
    return set(s[i:i + N] for i in range(len(s) - N + 1))


G = {}
for src, q in ALL:
    G[q['id']] = grams(stem(q))

TH = float(sys.argv[1]) if len(sys.argv) > 1 else 0.45
print('n-gram ตัวอักษรยาว %d · เกณฑ์ %.2f · โครงขั้นต่ำ %d · ทับซ้อนขั้นต่ำ %d'
      % (N, TH, MINGRAM, MININT))
print('เทียบ', len(MINE), 'ข้อของเรา กับ', len(ALL), 'ข้อ')
print()

flag = 0
for q in MINE:
    a = G[q['id']]
    if len(a) < MINGRAM:
        continue
    hits = []
    for src, r in ALL:
        if r['id'] == q['id']:
            continue
        b = G[r['id']]
        if len(b) < MINGRAM:
            continue
        inter = len(a & b)
        if inter < MININT:
            continue
        jac = inter / float(len(a | b))
        con = inter / float(min(len(a), len(b)))
        if max(jac, con) >= TH:
            hits.append((max(jac, con), jac, con, src, r))
    if not hits:
        continue
    flag += 1
    hits.sort(reverse=True, key=lambda x: x[0])
    print('=' * 78)
    print('🔎', q['id'], '|', q['difficulty'], '|', q['subTopics'])
    print('   ', stem(q)[:150])
    for m, jac, con, src, r in hits[:4]:
        print('    ↔ jac %.2f · con %.2f  [%s] %s | %s'
              % (jac, con, src, r['id'], r.get('difficulty')))
        print('        ', stem(r)[:150])
    print()

print('=' * 78)
print('ข้อของเราที่มีคู่คล้าย ≥ %.2f :' % TH, flag, 'ข้อ')

# -*- coding: utf-8 -*-
"""กวาดชนแบบ **เจาะชุดย่อย** — ทำคำอ้าง "Collision sweep …" ที่ทำซ้ำไม่ได้ ให้ทำซ้ำได้ · v1.1 · 22 ส.ค. 69

📜 ประวัติรุ่น
   v1.0  22 ส.ค. 02:0x — ฉบับแรก (27 โพรบ · กฎ self-hit · มิวแทนต์ 7)
   v1.1  22 ส.ค. 17:xx — แก้ 2 รอยร้าวที่ **ผู้ตรวจอิสระเจอโดยรันจากที่ที่ผมไม่ได้คิดถึง**
         ① `--selftest` เคยระเบิดเป็น `KeyError` เมื่อวางไฟล์นอกต้นไม้ repo
            ⇒ traceback ⛔ ไม่ใช่คำตัดสิน · ตอนนี้มี `preflight()` ⇒ พิมพ์เหตุแล้วคืน **2**
         ② เลิกผูก `ROOT = HERE/../../..` ตายตัว ⇒ `find_root()` **มองหา `data/sets/` จริง**
            รับ `--root=<path>` ได้ · ⇒ ปิด "ความลึกของโฟลเดอร์" ที่เคยเป็นตัวหารที่มองไม่เห็น
         ③ (ผลพลอยได้) แยกชนิดของแดง: **เครื่องมือพัง = 2** · **เนื้อหาชน = 1**
            🔴 บทเรียนระหว่างทาง: ยาแก้ ① **ย้ายบั๊กไปโผล่ที่ `read_debt()`** แทนที่จะดับมัน
               ⇒ ต้องยิงมิวแทนต์ซ้ำหลังแก้ทุกครั้ง — เพิ่ม 🧬M9 ไว้เฝ้าจุดนั้นโดยเฉพาะ

═══════════════════════════════════════════════════════════════════════════════
⛔ ปัญหาที่ไฟล์นี้เกิดมาแก้ — และสิ่งที่มัน **ไม่** แก้
═══════════════════════════════════════════════════════════════════════════════
`notes` ของ 27 ข้อในก้อน b20/b21 เขียนว่า
    "Collision sweep on 6417 items (bank 63 files + k1 out + k2 out),
     probe collide_b20.py / collide_b20b.py: … returns 0 items"
แต่ `collide_b20.py` · `collide_b20b.py` · `collide_b21.py` · `collide_b21b.py`
**⛔ ไม่มีอยู่จริง** — ยืนยัน 3 ขาอิสระแล้ว (git ⛔ ไม่เคย add · ดิสก์ครู ⛔ ไม่มี · ซองส่งมอบ ⛔ ไม่มี)
⇒ ตัวเลข 6,417 และคำว่า "returns 0 items" เป็น **คำบอกเล่า** ⛔ ไม่ใช่ **การวัดที่เปิดดูซ้ำได้**

🔑 **สิ่งที่ไฟล์นี้ทำ** — แปลงคำอ้างให้อยู่ในรูปที่ *วันนี้* ทดสอบซ้ำได้:
     คำอ้างเดิม (ตอนข้อยังไม่เข้าคลัง) : "แม่พิมพ์ของข้อนี้กวาดแล้วเจอ **0 ข้อ**"
     รูปที่ทดสอบได้วันนี้ (ข้ออยู่ในคลังแล้ว) : "กวาดแล้วต้องเจอ **1 ข้อ คือตัวมันเอง**"
   ⇒ เจอเกินตัวเอง = ชน · เจอ **0** = โพรบว่างเปล่า (⛔ ไม่ใช่ "สะอาด") ⇒ แดงทั้งคู่

⛔ **สิ่งที่ไฟล์นี้ ⛔ ไม่ได้ทำ — อย่าอ่านเกิน**
   ① ⛔ ไม่ได้ทำซ้ำการกวาดของเดิม — ตัวหารเดิม (6,417 = คลัง + `k1 out` + `k2 out` ของรอบนั้น)
      **ประกอบขึ้นใหม่ไม่ได้แล้ว** ที่ทำงานรอบนั้นหายไปพร้อมสคริปต์ ⇒ ตัวหารที่นี่คือ **คลังวันนี้**
      ⇒ ผลที่ได้คือ **ผลใหม่** ⛔ ไม่ใช่ "การยืนยันผลเก่า"
   ② ⛔ ไม่ได้ปลดหนี้ `NOTES_REF_DEBT` — `notes` ยังอ้างชื่อไฟล์ที่ ⛔ ไม่มีอยู่เหมือนเดิม
      หมุดของด่าน 21 จึงต้องอยู่ต่อ (กฎ ① ของด่าน 21) ⇒ **47 ยังเป็น 47**
   ③ ⛔ ไม่ได้ตัดสินว่าตัวลวงถูกหรือผิด — กวาดหา **การชนของแม่พิมพ์** อย่างเดียว
   ④ โพรบยืนบน **ตัวโจทย์** (`question`) เท่านั้น (qonly · กฎเดียวกับ `collide_b22.py`)
      ⇒ ⛔ มองไม่เห็นการชนที่โผล่เฉพาะในตัวเลือก/เฉลย

═══════════════════════════════════════════════════════════════════════════════
㉑ สามตัวเลขที่ต้องประกาศ
═══════════════════════════════════════════════════════════════════════════════
    ตัวหาร      : 27 ข้อที่มีโพรบ × คลัง `data/sets/*.json` ทั้งหมด (นับเองตอนรัน ⛔ ไม่ฝังเลข)
    แดงวันแรก   : 0 ข้อ (22 ส.ค. 69) — เจอเพื่อนบ้าน 2 ชื่อ ทั้งคู่ถูกประกาศไว้ใน `notes` อยู่แล้ว
    ผลกับเคสต้นเรื่อง : คำอ้าง "0 items" ของทั้ง 27 ข้อ **ทดสอบซ้ำได้แล้ว** ในรูปใหม่ (self-hit)

═══════════════════════════════════════════════════════════════════════════════
🕳️ จุดบอดที่ประกาศไว้ตรงนี้ เพื่อให้ "เขียว" ⛔ ไม่โกหก
═══════════════════════════════════════════════════════════════════════════════
  · โพรบเป็น **regex บนถ้อยคำ** ⇒ ข้อที่ชนกันแต่เขียนคนละสำนวน มันมองไม่เห็น
    (ทรงเดียวกับที่เจอใน `FINDING-ตัวกวาดที่ยืนบนคำมองไม่เห็นการชนเชิงตัวเลข`)
  · โพรบถูกถอดจาก **ถ้อยคำในโน้ตของข้อนั้นเอง** ⇒ ถ้าโน้ตบรรยายแม่พิมพ์ผิดมาแต่ต้น โพรบก็ผิดตาม
    ยาแก้ที่ใส่ไว้: กฎ self-hit ทำให้โพรบที่ **ว่างเปล่า** แดงทันที (แต่โพรบที่ **กว้างเกิน** ยังเงียบได้)
  · ครอบเฉพาะ 27 ข้อของ b20/b21 — อีก 20 ข้อของ b23 ที่อยู่ในหนี้เดียวกัน **ยังไม่มีโพรบ**
    ⇒ สคริปต์ **พิมพ์รายชื่อที่ยังไม่ครอบทุกครั้ง** ⛔ ไม่ตัดเงียบ

🔧 วิธีใช้
    python3 tools/authoring/k2/collide_subset.py              # กวาด 27 ข้อ b20/b21
    python3 tools/authoring/k2/collide_subset.py --selftest   # ชุดทดสอบของตัวกวาดเอง (รวมมิวแทนต์)
    python3 tools/authoring/k2/collide_subset.py --ids a,b,c  # กวาดเฉพาะบางข้อที่มีโพรบ
    รหัสออก 0 = ไม่มีชน · 1 = มีชน/โพรบพัง · 2 = ตัวเครื่องมือเองพัง
"""
import io, os, re, sys, ast, json, glob

HERE = os.path.dirname(os.path.abspath(__file__))
P = 'gen-chap-07-trigonometry-'


def find_root(start=None, override=None):
    r"""หารากคลังโดย **มองหา `data/sets/` จริง** ⛔ ไม่ใช่นับ `../` ตายตัว

    🔴 v1.0 เขียนว่า `ROOT = HERE/../../..` ⇒ ไฟล์ทำงานถูกก็ต่อเมื่อวางที่
       `<repo>/tools/authoring/k2/` เป๊ะ · ย้ายไฟล์ไปที่อื่น (เช่น `_delivery-qc\`)
       ⇒ ได้ตัวหาร 0 โดยที่ ⛔ ไม่มีอะไรบอกว่าสาเหตุคือ "วางผิดที่"
       ⇒ ⇒ **ความลึกของโฟลเดอร์กลายเป็นตัวหารที่มองไม่เห็น** (E→MB #90 §4)
    คืน (root, วิธีที่หาเจอ) — root = None ถ้าหาไม่เจอ ⇒ ผู้เรียกต้องทำให้มันแดง
    """
    if override:
        cand = os.path.abspath(os.path.expanduser(override))
        ok = os.path.isdir(os.path.join(cand, 'data', 'sets'))
        return (cand if ok else None), '--root=%s%s' % (override, '' if ok else ' (⛔ ไม่มี data/sets)')
    cur = os.path.abspath(start or HERE)
    while True:
        if os.path.isdir(os.path.join(cur, 'data', 'sets')):
            return cur, 'เดินขึ้นจากที่ตั้งไฟล์จนเจอ data/sets'
        nxt = os.path.dirname(cur)
        if nxt == cur:
            break
        cur = nxt
    cwd = os.path.abspath(os.getcwd())
    while True:
        if os.path.isdir(os.path.join(cwd, 'data', 'sets')):
            return cwd, 'เดินขึ้นจาก cwd จนเจอ data/sets'
        nxt = os.path.dirname(cwd)
        if nxt == cwd:
            break
        cwd = nxt
    return None, 'หา data/sets ⛔ ไม่เจอเลย ทั้งจากที่ตั้งไฟล์และจาก cwd'


ROOT, ROOT_HOW = find_root()

# ═══════════════════════════════════════════════════════════════════════════════
# ① ประกอบคลังเทียบ — วัดเองทุกครั้ง ⛔ ไม่มีเลขฝัง
# ═══════════════════════════════════════════════════════════════════════════════


def assemble(root=None):
    root = root or ROOT
    if not root:
        return [], 0, {}
    files = sorted(glob.glob(os.path.join(root, 'data', 'sets', '*.json')))
    items, raw = {}, 0
    for p in files:
        d = json.load(io.open(p, encoding='utf-8'))
        for q in d.get('questions', []):
            raw += 1
            if q['id'] in items:
                continue
            q = dict(q)
            q['_src'] = os.path.basename(p)[:-5]
            items[q['id']] = q
    return files, raw, items


def qtext(q):
    return q.get('question') or ''


# ═══════════════════════════════════════════════════════════════════════════════
# ② ตารางโพรบ — หนึ่งแถวต่อหนึ่งข้อ
#    parts  : เงื่อนไข **และ** ทุกตัว (นี่คือ "the pair that defines this item" ในโน้ต)
#    allow  : รายชื่อ ⛔ ไม่ใช่ตัวเลข · ทุกชื่อต้องมีเหตุผลเขียนกำกับ
#    claim  : ประโยคของ `notes` เองที่โพรบแถวนี้ถอดออกมา (เพื่อให้ตรวจย้อนได้ว่าถอดตรงไหม)
# ═══════════════════════════════════════════════════════════════════════════════
PROBES = [
 (P+'q125', 'จุดกึ่งกลางสองด้านของสามเหลี่ยม แล้วถามอัตราส่วนตรีโกณ',
  [r'จุดกึ่งกลางของด้าน[\s\S]{0,150}จุดกึ่งกลางของด้าน', r'\\(?:sin|cos|tan|cot|sec|csc)'], [],
  'names two midpoints of two different sides of one triangle … then asks for a trigonometric ratio'),
 (P+'q126', 'วงกลมแนบในสามเหลี่ยมมุมฉาก ถามรัศมี',
  [r'มุมฉาก', r'สัมผัสด้านทั้งสาม'], [],
  'an inscribed circle together with a right triangle, returns 0 items across the whole corpus'),
 (P+'q128', 'มัธยฐานจากมุมฉาก + พื้นที่ ⇒ ถาม sec + csc',
  [r'จุดกึ่งกลางของด้าน', r'มุมฉาก', r'\\sec[\s\S]{0,60}\\csc'], [],
  'no item in the corpus asks for sec + csc of an acute angle of a right triangle'),
 (P+'q129', 'จัตุรัสฝังในมุมฉาก + เงื่อนไขเส้นรอบรูป',
  [r'มุมฉาก', r'จัตุรัส', r'เส้นรอบรูป'], [],
  'an inscribed square crossed with a perimeter condition also returns zero'),
 (P+'q130', 'วงกลมสองวงรัศมีต่างกัน มุมที่จุดศูนย์กลางเท่ากัน',
  [r'วงกลมสองวง', r'ส่วนโค้ง', r'(?:ขนาด|ซึ่งมีขนาด)เท่ากัน'], [],
  '(two separate circles of different radii) crossed with (central angles of equal size) returns zero'),
 (P+'q131', 'เซกเตอร์คู่กับสามเหลี่ยมที่เกิดจากคอร์ด',
  [r'เซกเตอร์', r'สามเหลี่ยม'], [],
  'the word sector together with the word triangle inside the question text, returns 0 items'),
 (P+'q132', 'วงกลมสามวงสัมผัสกันภายนอกครบทุกคู่',
  [r'วงกลมสามวง', r'สัมผัสกันภายนอก'], [],
  'the full phrase for circles tangent to one another externally returns zero items'),
 (P+'q133', 'จัตุรัสกับบริเวณที่เป็นส่วนร่วมของสองบริเวณ',
  [r'จัตุรัส', r'ส่วนร่วม'], [],
  'Scan D1 (a square together with any word for a shared or overlapping part) returns 0 items'),
 (P+'q134', 'ครึ่งวงกลมบนเส้นผ่านศูนย์กลางที่ถูกแบ่ง',
  [r'ครึ่งวงกลม', r'เส้นผ่านศูนย์กลาง'],
  [(P+'q153', 'มาทีหลัง (b21) และโน้ตของ q153 เองประกาศ q134 ไว้เป็นเพื่อนบ้านแล้ว — '
              'q134 ให้ครึ่งวงกลม 3 รูปบนส่วนของเส้นตรงแล้วถามความยาว · '
              'q153 ให้ครึ่งวงกลม 4 รูปบนด้านจัตุรัสแล้วถามพื้นที่ ⇒ คนละ A คนละ M')],
  'the pair (semicircle and diameter in the same question) returns 0 items'),
 (P+'q135', 'เดินบนวงกลมหนึ่งหน่วยจากจุดที่ตั้งชื่อไว้ (⛔ ไม่ใช่ (1,0)) ⇒ ถามผลบวกพิกัดปลาย',
  [r'วงกลมหนึ่งหน่วย', r'(?:เคลื่อนที่|วัดส่วนโค้ง|วัด)จากจุด\s*\$[A-Z]\$',
   r'ค่าของ\s*\$[a-d]\s*\+\s*[a-d]\$'], [],
  'a unit-circle journey whose starting point is stated as a coordinate other than (1, 0) '
  'together with a request for the sum of the terminal coordinates, returns 0 items'),
 (P+'q136', 'กู้จุดฐานจากภาพหลังเลื่อน + ควอเตอร์เทิร์นสองทิศ',
  [r'วงกลมหนึ่งหน่วย', r't_0\s*[+-]\s*\\dfrac\{\\pi\}\{2\}'], [],
  '(an image supplied only after a shift …) crossed with (two quarter turns taken in opposite senses) '
  'returns zero items'),
 (P+'q137', 'ค่าสัมบูรณ์ของอัตราส่วนตรีโกณ + เงื่อนไขเครื่องหมายของผลคูณ',
  [r'\\left\|\\(?:sin|cos|tan)',
   r'\\(?:sin|cos|tan)\\?theta\s*\\cdot\s*\\(?:sin|cos|tan)\\?theta\s*>\s*0'], [],
  'Scan E2, a product of two trigonometric ratios compared with zero in the statement, '
  'returns exactly 1 item (q045) … no magnitude is ever supplied there'),
 (P+'q138', 'จุดปลายถูกจำกัดให้อยู่บนส่วนโค้งที่ลากระหว่างสองจุดที่ระบุ',
  [r'วงกลมหนึ่งหน่วย', r'อยู่บนส่วนโค้งที่ลากจากจุด'], [],
  'the phrase for lying on the arc drawn from a given point returns 0 items in the whole corpus'),
 (P+'q139', 'ฟังก์ชันนิยามสองท่อน ท่อนละกฎตรีโกณ',
  [r'นิยามโดย', r'f\(x\)\s*=[\s\S]{0,120}เมื่อ[\s\S]{0,120}f\(x\)\s*=[\s\S]{0,120}เมื่อ',
   r'\\(?:sin|cos|tan)'], [],
  'a two-interval piecewise definition together with trigonometric branches, returns 0 items'),
 (P+'q140', 'ผลคูณ sin·cos ที่อาร์กิวเมนต์เชิงเส้นสองเฟส ⇒ ผลบวก max+min',
  [r'ผลบวกของค่าสูงสุด(?:ที่เป็นไปได้)?(?:ของ.{0,12})?\s*(?:และ|กับ)\s*ค่าต่ำสุด',
   r'\\sin\\left\(\s*x\s*[+-][\s\S]{0,40}\\cos\\left\(\s*x\s*[+-]'], [],
  'The scan for a product of a sine and a cosine whose arguments are both linear in x returns 0 items'),
 (P+'q141', 'สมการค่าสัมบูรณ์ของตรีโกณที่มีพารามิเตอร์ + นับจำนวนคำตอบ',
  [r'\\left\|[\s\S]{0,40}\\(?:sin|cos|tan)', r'มีคำตอบทั้งหมด'], [],
  'Scan E1 … not one of them is an equation carrying a parameter, so the G of this item is untouched'),
 (P+'q142', 'ให้ค่า tan เป็นตัวเลข แล้วถามเศษส่วนดีกรีหนึ่งของ sin/cos ทั้งบนและล่าง',
  [r'\\tan\\?theta\s*=\s*\d',
   r'\\dfrac\{[^{}]*\\sin\\?theta[\s\S]{0,60}\\cos\\?theta[^{}]*\}\{[^{}]*\\sin\\?theta[\s\S]{0,60}\\cos\\?theta[^{}]*\}'],
  [], 'a numeric tangent value handed over together with a fraction that is first degree in sine and '
      'cosine on both levels, returns 0 items across the whole corpus'),
 (P+'q143', 'เศษส่วน cos/(1 − sin) เป็นข้อมูลตั้งต้น',
  [r'\\dfrac\{\\cos\\?theta\}\{1\s*-\s*\\sin\\?theta\}'], [],
  'a quotient with cos on top and 1 - sin underneath, returns 0 items across the whole corpus'),
 (P+'q144', 'ผลบวกส่วนกลับกำลังสองของ sin กับ cos เป็นข้อมูลที่ต้องแก้',
  [r'\\dfrac\{1\}\{\\sin\^2\\?theta\}\s*\+\s*\\dfrac\{1\}\{\\cos\^2\\?theta\}'], [],
  'the scan for a stem that hands over a reciprocal square sum as the datum to be solved '
  'returns zero items in the whole corpus'),
 (P+'q146', 'สามเหลี่ยมมุมฉากที่ด้านทั้งสามเป็นลำดับเรขาคณิต',
  [r'ลำดับเรขาคณิต', r'สามเหลี่ยม'],
  [(P+'q074', 'โน้ตของ q146 ประกาศชื่อนี้ไว้เองว่า "returns exactly 1 item, gen-chap-07-trigonometry-q074" — '
              'q074 เป็นสามเหลี่ยมใดๆ ถามเซตของขนาดมุม B ด้วยกฎโคไซน์ + AM-GM ⇒ ⛔ ไม่มีมุมฉาก คนละ A คนละ M')],
  'a geometric sequence together with a triangle, returns exactly 1 item across the whole corpus'),
 (P+'q149', 'สี่เหลี่ยมสองมุมฉาก จุดสองจุดอยู่คนละข้างของเส้นทแยง',
  [r'คนละข้างของ', r'มุมฉาก'], [],
  'the Thai phrase for "on opposite sides" returns 0 items in the whole corpus'),
 (P+'q151', 'เซกเตอร์ที่รัศมีถูกเพิ่ม โดยมุมที่จุดศูนย์กลางคงเดิม',
  [r'เซกเตอร์', r'เพิ่ม(?:ความยาว)?รัศมี|รัศมี[\s\S]{0,30}เพิ่ม'], [],
  'not one of them enlarges or otherwise changes the radius of a sector, the pattern for a radius '
  'being increased next to a sector returning zero items'),
 (P+'q153', 'ครึ่งวงกลมสี่รูปบนด้านของจัตุรัส',
  [r'ครึ่งวงกลม', r'จัตุรัส'], [],
  'the pair (semicircle and square in the same question) returns 0 items'),
 (P+'q156', 'ซ่อนค่าตรีโกณไว้ในพิกัดจุด + เงื่อนไขอยู่บนแกน',
  [r'อยู่บนแกน', r'\\(?:sin|cos|tan)'], [],
  'pairing that phrase [lying on an axis] with sine or cosine inside the same question returns 0 items'),
 (P+'q158', 'ผลรวมซิกมาของ cos ที่เลื่อนทีละ π/2',
  [r'\\sum', r'\\cos\\left\(\s*\\?theta\s*\+'], [],
  'a question text carrying a cosine of theta plus something returns 0 items, and a sigma sum living '
  'in any chapter 7 subtopic returns only 5 items, none of which sums over a quarter-turn shift'),
 (P+'q161', 'ผลบวก max+min ของส่วนกลับผลคูณ (sin²+c)(cos²+c)',
  [r'ผลบวกของค่าสูงสุด', r'\\sin\^2\s*x[\s\S]{0,40}\\cos\^2\s*x'], [],
  'the tighter pair that also demands the word for sum returns only 2 … only A overlaps '
  'while G and M both differ'),
 (P+'q164', 'กำลังสี่ของ sin/cos หารค่าคงที่เป็นข้อมูล ⇒ ถามกำลังหก',
  [r'\\dfrac\{\\(?:sin|cos)\^4\\?theta\}\{\d', r'\\dfrac\{\\(?:sin|cos)\^6\\?theta\}\{\d'], [],
  'the scan for a sixth power over a constant returns 0, so the requested expression itself is '
  'untouched anywhere'),
]

# ── เคส "ต้องปล่อย" (㊶) — ทุกชื่อคัดมาจาก **เพื่อนบ้านที่ `notes` เองระบุว่าใกล้แต่ไม่ใช่**
#    ⇒ ถ้าโพรบกว้างเกินจนกลืนเพื่อนบ้านพวกนี้ ชุดทดสอบจะล้มทันที
RELEASE = [
 (P+'q131', P+'q119', 'เทียบความยาวส่วนโค้งของสองเซกเตอร์ที่พื้นที่เท่ากัน — ⛔ ไม่มีสามเหลี่ยมเลย'),
 (P+'q133', 'chap-07-trigonometry-q211', 'ซ้อนวงกลมเต็มสองวง ใช้ segment = sector − triangle ⛔ ไม่ใช่จัตุรัส'),
 (P+'q134', 'chap-13-calculus-q98', 'โจทย์หาค่าสุดขีดบทแคลคูลัส ⛔ ไม่ใช่สามครึ่งวงกลมบนเส้นที่ถูกแบ่ง'),
 (P+'q135', P+'q136', 'เริ่มเดินจากพิกัด $(1,0)$ ตรง ๆ ⛔ ไม่ใช่จากจุดที่ตั้งชื่อไว้'),
 (P+'q136', P+'q008', 'ให้จุดปลายมาตรง ๆ แล้วถามจุดปลายหลังเลื่อนโคฟังก์ชัน ⛔ ไม่ต้องกู้จุดฐาน'),
 (P+'q137', P+'q045', 'ให้เงื่อนไขเครื่องหมายสองชุด แล้วถามแค่จตุภาค ⛔ ไม่มีขนาดให้เลย'),
 (P+'q138', P+'q023', 'ปักจุด P ด้วยจตุภาค + ระยะตรง แล้วถามความยาวส่วนโค้งเอง'),
 (P+'q142', P+'q091', 'เปิดด้วยเงื่อนไข cosθ ≠ 0 เหมือนกัน แต่ ⛔ ไม่มีค่าตัวเลข และเศษ/ส่วนดีกรีสาม'),
 (P+'q144', 'chap-07-trigonometry-q141', 'เป็นเอกลักษณ์ให้จัดรูป ⛔ ไม่มีมุมที่ต้องแก้'),
 (P+'q146', P+'q127', 'สามเหลี่ยมมุมฉากที่ด้านเป็นลำดับ **เลขคณิต** ⛔ ไม่ใช่เรขาคณิต'),
 (P+'q151', P+'q032', 'วงกลมซ้อนศูนย์กลางเดียวกัน เดินย้อนทางจากผลต่างพื้นที่ไปหาผลต่างส่วนโค้ง'),
 (P+'q153', P+'q133', 'จัตุรัสด้าน 12 ที่ใช้ภาษาเซตเหมือนกัน แต่ ⛔ ไม่มีครึ่งวงกลม'),
 (P+'q161', P+'q140', 'ถามผลบวก max+min เหมือนกัน แต่ G เป็นผลคูณ sin·cos สองเฟส ⛔ ไม่ใช่ส่วนกลับ'),
 (P+'q164', 'pat1-2557-11-q29', 'ผิวเดียวกันคือ sin⁴/5 + cos⁴/7 แต่ถาม sin²(2x) ⇒ สูตรมุมสองเท่า'),
]

# ── ชุดย่อยที่ไฟล์นี้ตั้งใจครอบ (รายชื่อ ⛔ ไม่ใช่ตัวเลข)
SUBSET_B20_B21 = [row[0] for row in PROBES]


# ═══════════════════════════════════════════════════════════════════════════════
# ③ คำตัดสิน — **ฟังก์ชันเดียว** ที่รหัสออกทั้งหมดต้องผ่าน
#    (บทเรียนจาก molds.py: รหัสออกที่คิดจากกองเดียว ทำให้คำตัดสินของอีกกองตกหาย)
# ═══════════════════════════════════════════════════════════════════════════════


def verdict(items, probes, subset=None):
    """คืน (rows, reds) · reds = (ชื่อ, เหตุ, ชนิด)

    ชนิด 'tool'    = ตัวเครื่องมือเองพัง/ยืนผิดที่ ⇒ รหัสออก **2**
    ชนิด 'content' = เนื้อหาในคลังมีปัญหาจริง    ⇒ รหัสออก **1**
    🔴 แยกสองอย่างนี้เพราะ "เทียบไม่ได้" ⛔ ไม่เท่ากับ "เทียบแล้วผ่าน" — และก็ ⛔ ไม่เท่ากับ "เจอของชน"
    """
    reds, rows = [], []
    if not items:
        reds.append(('ตัวหาร 0', 'คลังเทียบว่างเปล่า — "กวาดไม่เจอ" ⛔ ไม่เท่ากับ "ไม่มีของชน"', 'tool'))
        return rows, reds
    wanted = set(subset) if subset else None
    ran = 0
    for qid, mold, parts, allow, claim in probes:
        if wanted is not None and qid not in wanted:
            continue
        ran += 1
        try:
            rxs = [re.compile(p) for p in parts]
        except re.error as e:
            reds.append((qid, 'regex ของโพรบคอมไพล์ไม่ผ่าน: %s' % e, 'tool'))
            continue
        hits = [q['id'] for q in items.values() if all(r.search(qtext(q)) for r in rxs)]
        allow_ids = [a for a, _ in allow]
        if qid not in hits:
            reds.append((qid, '🕳️ โพรบว่างเปล่า — ⛔ ไม่จับแม้แต่ตัวข้อเอง '
                              '⇒ "กวาดแล้วไม่เจอ" ของแถวนี้เชื่อไม่ได้', 'tool'))
        extra = [h for h in hits if h != qid and h not in allow_ids]
        seen_allow = [h for h in hits if h in allow_ids]
        if extra:
            reds.append((qid, '🔴 ชนกับข้อที่ ⛔ ไม่ได้ประกาศไว้: ' + ', '.join(extra), 'content'))
        rows.append((qid, mold, hits, seen_allow, extra, allow, claim))
    if ran == 0:
        reds.append(('ตัวหาร 0', 'ไม่มีโพรบถูกรันเลย — "ผ่าน" แบบนี้ ⛔ ไม่มีความหมาย', 'tool'))
    return rows, reds


# ═══════════════════════════════════════════════════════════════════════════════
# ④ ชุดทดสอบของตัวกวาดเอง — มีทั้งเคส **จับ** และเคส **ปล่อย** และ **มิวแทนต์**
# ═══════════════════════════════════════════════════════════════════════════════
_fail = []


def say(tag, msg, ok):
    print('  %s %s · %s' % ('✅' if ok else '🔴', tag, msg))
    if not ok:
        _fail.append(tag)


# ── ฟิกซ์เจอร์ที่ชุดทดสอบต้องหยิบจากคลังจริง — ประกาศเป็น **รายชื่อ** เพื่อตรวจล่วงหน้าได้
SELFTEST_FIXTURES = [P+'q143', P+'q125']


def preflight(files, items, need_fixtures=True):
    """🔴 v1.0 ไม่มีขั้นนี้ — วางไฟล์ผิดที่แล้ว `--selftest` **ระเบิดเป็น traceback**
       (`KeyError: gen-chap-07-trigonometry-q143`) ⛔ ไม่ใช่คำตัดสิน (E→MB #90 §4)
       ⇒ traceback ⛔ ไม่ใช่ "แดง" — มันคือด่านที่ไม่ได้ตัดสินอะไรเลย
       คืนรายการเหตุที่ทำให้ทดสอบตัวเองไม่ได้ · ว่าง = พร้อมทดสอบ"""
    bad = []
    if not ROOT:
        bad.append('หารากคลัง ⛔ ไม่เจอ (%s) ⇒ ไฟล์นี้ถูกวางนอกต้นไม้ของ repo หรือ cwd ผิดที่' % ROOT_HOW)
    if not files:
        bad.append('data/sets ⛔ ไม่มีไฟล์เลย')
    if not items:
        bad.append('คลังเทียบว่างเปล่า (0 id) ⇒ ⛔ ไม่มีอะไรให้ทดสอบ')
    if need_fixtures:
        missing = [f for f in SELFTEST_FIXTURES if f not in items]
        if missing:
            bad.append('ฟิกซ์เจอร์ที่ชุดทดสอบต้องใช้หายไป: ' + ', '.join(missing))
    return bad


def say_cannot(bad):
    """พิมพ์คำตัดสิน "ยืนผิดที่" แบบเดียวกันทั้งโหมดหลักและโหมดทดสอบ"""
    print()
    print('🔴 ⛔ ตัดสินไม่ได้ — ⛔ ไม่ใช่ "ผ่าน" และ ⛔ ไม่ใช่ "ตก" · เป็น **ตัวเครื่องมือยืนผิดที่**')
    for b in bad:
        print('   · %s' % b)
    print('   ⇒ วิธีแก้: รันจากในต้นไม้ของ repo หรือส่ง --root=<path ของ repo>')


def selftest():
    global ROOT
    files, raw, items = assemble()
    print('ชุดทดสอบของ `collide_subset.py`')
    print('  รากคลัง: %s  (%s)' % (ROOT or '⛔ ไม่เจอ', ROOT_HOW))
    print('  คลังที่ใช้ทดสอบ: %d ไฟล์ · %d ระเบียน · %d id ไม่ซ้ำ' % (len(files), raw, len(items)))

    bad = preflight(files, items)
    if bad:
        say_cannot(bad)
        return 2

    print('\n── ① เคส **จับ**: ทุกโพรบต้องจับข้อของตัวเองได้ (กฎ self-hit) ──')
    rows, reds = verdict(items, PROBES)
    empty = [r[0] for r in reds if 'ว่างเปล่า' in r[1]]
    say('①', 'โพรบทั้ง %d แถวจับตัวเองครบ (ว่างเปล่า %d แถว)' % (len(PROBES), len(empty)), not empty)

    print('\n── ② เคส **ปล่อย**: เพื่อนบ้านที่โน้ตระบุว่า "ใกล้แต่ไม่ใช่" ต้องไม่ถูกจับ ──')
    byid = {r[0]: r for r in PROBES}
    caught = []
    for qid, other, why in RELEASE:
        if other not in items:
            caught.append('%s (⛔ ไม่มี id %s ในคลัง)' % (qid, other))
            continue
        rxs = [re.compile(p) for p in byid[qid][2]]
        if all(r.search(qtext(items[other])) for r in rxs):
            caught.append('%s กลืน %s' % (qid, other))
    say('②', 'เคสปล่อย %d เคส — ถูกกลืน %d' % (len(RELEASE), len(caught))
        + (' ⇒ ' + '; '.join(caught) if caught else ''), not caught)

    print('\n── ③ มิวแทนต์: ของที่ควรแดง **ต้องแดงจริง** ⛔ ไม่ใช่แค่ดูว่าเขียว ──')
    # 🧬 M1 โพรบว่างเปล่า (รูที่อันตรายที่สุด — "ไม่เจอของเดิม" แบบเขียวหลอก)
    m1 = [(P+'q125', 'x', [r'ข้อความที่ไม่มีวันปรากฏในคลัง๛๛๛'], [], '')]
    _, r1 = verdict(items, m1)
    say('🧬M1', 'โพรบที่จับอะไรไม่ได้เลย ⇒ ต้องแดง', bool(r1))
    # 🧬 M2 ฉีดข้อชนเข้าคลัง
    inj = dict(items)
    clone = dict(items[P+'q143'])
    clone['id'] = 'chap-00-fixture-q99'
    inj[clone['id']] = clone
    _, r2 = verdict(inj, [row for row in PROBES if row[0] == P+'q143'])
    say('🧬M2', 'ฉีดข้อที่โจทย์ซ้ำเป๊ะเข้าคลัง ⇒ ต้องแดง', bool(r2))
    # 🧬 M2b ของสะอาดชุดเดียวกันต้อง **เขียว** (คู่ตรงข้ามของ M2)
    _, r2b = verdict(items, [row for row in PROBES if row[0] == P+'q143'])
    say('🧬M2b', 'คลังจริงที่ยังไม่ถูกฉีด ⇒ ต้องเขียว', not r2b)
    # 🧬 M3 ตัวหาร 0
    _, r3 = verdict({}, PROBES)
    say('🧬M3', 'คลังว่าง (ตัวหาร 0) ⇒ ต้องแดง', bool(r3))
    # 🧬 M3b ไม่มีโพรบถูกรันเลย
    _, r3b = verdict(items, PROBES, subset=['ไม่มีข้อนี้'])
    say('🧬M3b', 'ไม่มีโพรบถูกรันเลย ⇒ ต้องแดง', bool(r3b))
    # 🧬 M4 ถอนชื่อออกจาก allow ⇒ แถวที่พึ่งชื่อนั้นต้องแดง (พิสูจน์ว่า allow ⛔ ไม่ใช่ของประดับ)
    stripped = [(a, b, c, [], e) for a, b, c, d, e in PROBES if d]
    say('🧬M4', 'ถอน allow ทิ้งทั้งหมด (%d แถวที่มี allow) ⇒ ต้องแดงทุกแถว' % len(stripped),
        bool(stripped) and len(verdict(items, stripped)[1]) == len(stripped))
    # 🧬 M5 regex พัง ⇒ ต้องแดง ⛔ ไม่ใช่ crash
    _, r5 = verdict(items, [(P+'q125', 'x', [r'('], [], '')])
    say('🧬M5', 'regex คอมไพล์ไม่ผ่าน ⇒ ต้องแดง (⛔ ไม่ระเบิด)', bool(r5))

    print('\n── ④ มิวแทนต์ของ v1.1 — ยาแก้ที่เพิ่งใส่ ต้องพิสูจน์ว่ามันกัดจริง ──')
    # 🧬 M6 ฟิกซ์เจอร์หาย ⇒ preflight ต้องจับ (นี่คือเคสที่ v1.0 ระเบิดเป็น traceback)
    say('🧬M6', 'ฟิกซ์เจอร์ที่ชุดทดสอบต้องใช้หายไป ⇒ preflight ต้องจับ ⛔ ไม่ระเบิด',
        bool(preflight(files, {k: v for k, v in items.items() if k not in SELFTEST_FIXTURES})))
    # 🧬 M6b คลังจริงที่ครบ ⇒ preflight ต้องเงียบ (คู่ตรงข้าม)
    say('🧬M6b', 'คลังจริงที่ครบ ⇒ preflight ต้องปล่อยผ่าน', not preflight(files, items))
    # 🧬 M7 ชี้รากไปที่โฟลเดอร์ที่ ⛔ ไม่มี data/sets ⇒ ต้องคืน None ⛔ ไม่ใช่เดาเอา
    #     (ใช้ <ROOT>/scripts เป็นของล่อ — มีอยู่จริงในคลัง แต่ ⛔ ไม่มี data/sets ข้างใน)
    say('🧬M7', 'ชี้ --root ไปที่โฟลเดอร์ที่มีจริงแต่ ⛔ ไม่มี data/sets ⇒ ต้องหาไม่เจอ',
        find_root(override=os.path.join(ROOT, 'scripts'))[0] is None)
    # 🧬 M7b ชี้ --root ไปที่รากจริง ⇒ ต้องเจอ (คู่ตรงข้ามของ M7)
    say('🧬M7b', 'ชี้ --root ไปที่รากจริง ⇒ ต้องเจอ',
        find_root(override=ROOT)[0] == ROOT)
    # 🧬 M8 ตัวหาร 0 ⇒ ชนิดของแดงต้องเป็น 'tool' ⛔ ไม่ใช่ 'content'
    _, r8 = verdict({}, PROBES)
    say('🧬M8', 'ตัวหาร 0 ⇒ ต้องเป็นแดงชนิด **เครื่องมือ** (รหัสออก 2) ⛔ ไม่ใช่ "เจอของชน"',
        bool(r8) and all(x[2] == 'tool' for x in r8))

    # 🧬 M9 read_debt ตอนไม่มีราก ⇒ ต้องคืน None ⛔ ไม่ระเบิด (รูที่โผล่ตอนแก้ M6 — ยาแก้ย้ายบั๊ก)
    _keep = ROOT
    ROOT = None
    try:
        _ok = read_debt() is None
    except Exception:
        _ok = False
    finally:
        ROOT = _keep
    say('🧬M9', 'ไม่มีรากคลัง ⇒ read_debt ต้องคืน None ⛔ ไม่ระเบิดเป็น traceback', _ok)

    print('\n── ⑤ ความสอดคล้องกับทะเบียนหนี้ของด่าน 21 ──')
    debt = read_debt()
    if debt is None:
        say('⑤', 'อ่าน NOTES_REF_DEBT ⛔ ไม่ได้', False)
    else:
        outside = [i for i in SUBSET_B20_B21 if i not in debt]
        say('⑤', 'ทุกข้อที่ไฟล์นี้ครอบ ต้องอยู่ในหนี้ของด่าน 21 (นอกทะเบียน %d ข้อ)' % len(outside),
            not outside)

    print('\n%s ชุดทดสอบ: ล้ม %d รายการ' % ('🔴' if _fail else '✅', len(_fail)))
    return 1 if _fail else 0


def read_debt():
    if not ROOT:
        return None          # 🔴 ⛔ ห้ามระเบิด — ผู้เรียกจัดการเองว่าจะแดงยังไง
    p = os.path.join(ROOT, 'scripts', 'check_notes_refs.py')
    if not os.path.exists(p):
        return None
    src = io.open(p, encoding='utf-8').read()
    for n in ast.parse(src).body:
        if isinstance(n, ast.Assign) and getattr(n.targets[0], 'id', '') == 'NOTES_REF_DEBT':
            return list(ast.literal_eval(n.value))
    return None


# ═══════════════════════════════════════════════════════════════════════════════
# ⑤ main
# ═══════════════════════════════════════════════════════════════════════════════


def main(argv):
    global ROOT, ROOT_HOW
    for a in argv:
        if a.startswith('--root='):
            ROOT, ROOT_HOW = find_root(override=a[7:])
    if '--selftest' in argv:
        return selftest()
    only = None
    for a in argv:
        if a.startswith('--ids='):
            only = [s.strip() for s in a[6:].split(',') if s.strip()]
    files, raw, items = assemble()
    print('㊳ รากคลัง          : %s  (%s)' % (ROOT or '⛔ ไม่เจอ', ROOT_HOW))
    print('㊳ ตัวหาร (วัดตอนรัน) : data/sets %d ไฟล์ · %d ระเบียน · %d id ไม่ซ้ำ'
          % (len(files), raw, len(items)))
    subset = only or SUBSET_B20_B21
    print('㊳ ชุดที่กวาด        : %d ข้อ (รายชื่ออยู่ในตาราง PROBES ของไฟล์นี้)' % len(subset))
    print('㊳ ยืนบนฟิลด์        : question เท่านั้น (qonly) ⛔ ไม่รวมตัวเลือก/เฉลย')
    bad = preflight(files, items, need_fixtures=False)
    if bad:
        say_cannot(bad)
        return 2
    print()
    rows, reds = verdict(items, PROBES, subset=subset)
    for qid, mold, hits, seen_allow, extra, allow, claim in rows:
        if extra:
            mark = '🔴'
        elif seen_allow:
            mark = '🟠'
        elif qid in hits:
            mark = '✅'
        else:
            mark = '🕳️'
        print('%s %-34s %s' % (mark, qid.replace(P, ''), mold))
        print('     เจอ %d ข้อ%s' % (len(hits), ' (= ตัวมันเองข้อเดียว)' if hits == [qid] else ''))
        for h in hits:
            if h == qid:
                continue
            why = dict(allow).get(h)
            print('       %s %s' % ('🟠 ประกาศไว้แล้ว:' if why else '🔴 ⛔ ไม่ได้ประกาศ:', h))
            if why:
                print('          เหตุผล: %s' % why)
    # ⛔ ไม่ตัดเงียบ — บอกเสมอว่ายังมีหนี้ส่วนไหนที่ไฟล์นี้ยังไม่ครอบ
    debt = read_debt() or []
    uncovered = [i for i in debt if i not in SUBSET_B20_B21]
    print()
    print('📌 หนี้ NOTES_REF_DEBT ทั้งหมด %d ข้อ · ไฟล์นี้ครอบ %d ข้อ · **ยังไม่ครอบ %d ข้อ**'
          % (len(debt), len(SUBSET_B20_B21), len(uncovered)))
    if uncovered:
        print('   ยังไม่มีโพรบ: ' + ', '.join(x.replace(P, '') for x in uncovered))
    print()
    if reds:
        tool = [r for r in reds if r[2] == 'tool']
        print('🔴 คำตัดสิน: มีปัญหา %d รายการ (ตัวเครื่องมือ %d · เนื้อหา %d)'
              % (len(reds), len(tool), len(reds) - len(tool)))
        for a, b, kind in reds:
            print('   · [%s] %s — %s' % ('เครื่องมือ' if kind == 'tool' else 'เนื้อหา', a, b))
        if tool:
            print('   ⇒ รหัสออก 2 = **ตัวเครื่องมือเองพัง** ⛔ ไม่ใช่ "เจอของชน"')
            return 2
        return 1
    print('✅ คำตัดสิน: ทุกโพรบจับตัวเองได้ และ ⛔ ไม่มีการชนที่ยังไม่ถูกประกาศ')
    print('   ⚠️ อ่านให้ตรง: นี่คือ **ผลใหม่ของวันนี้** ⛔ ไม่ใช่การยืนยันตัวเลข 6,417 ของเดิม')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

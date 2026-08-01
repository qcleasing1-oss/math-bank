#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ด่าน 10 · รายการ "สิ่งที่อนุญาต" ต้องไม่โตขึ้นเงียบ ๆ

ที่มา (1 ส.ค. 2569 · จดหมายพอร์ทัล E→MB #02 ตอบข้อ M7 / กับดัก ⑧):
  ด่าน 6 มี ALLOWED_PATHS = ['data/bank.json'] และ "หมุดปักค่า" (CONFIG_PIN)
  อยู่ในไฟล์เดียวกัน — ซึ่งเป็นกับดัก ⑧ เต็ม ๆ:
      🔴 กฎที่บังคับ "รอยต่อระหว่างรุ่น" ไปอยู่ในรุ่นใดรุ่นหนึ่งไม่ได้
         เพราะคนที่แก้รายการ ก็แก้หมุดในบรรทัดถัดไปได้พร้อมกัน
  พอร์ทัลจึงเสนอ (และรับมาทำ) ว่า ตัวเทียบต้องอยู่ "นอกทั้งสองรุ่น" = อยู่ที่ CI
  ⇒ เทียบรายการที่ HEAD กับที่ฐาน (HEAD~1 / event.before / PR base)
     ถ้ารายการ **โตขึ้น** ⇒ แดง เว้นแต่ข้อความ commit ในช่วงนั้นประกาศไว้ว่า
         ALLOWED_PATHS+: <เหตุผล>

  ⚠️ ข้อจำกัดที่พอร์ทัลรับรู้แล้วและยอมรับ:
     คนที่ตั้งใจเลี่ยง ก็พิมพ์บรรทัดประกาศนั้นเองได้ ด่านนี้ไม่ได้กันคนโกง
     สิ่งที่กันได้คือ **การขยายสิทธิ์แบบไม่มีใครสังเกต** — บังคับให้การขยาย
     ต้องทิ้งประโยคไว้ในประวัติ git ที่ค้นย้อนได้

⛔ อ่านไฟล์เป็น "ข้อความล้วน" เท่านั้น — ห้าม import สคริปต์ที่กำลังตรวจ
   (กฎเดียวกับด่าน 2 · ถ้า import ไฟล์ที่พัง ตัวด่านจะพังตามไปด้วย
    แล้วจะแยกไม่ออกว่า "ของพัง" หรือ "ด่านพัง")

รหัสออก: 0 = ผ่าน · 1 = เนื้อหาแดง · 2 = ตัวเครื่องมือแดง / เทียบไม่ได้
"""
import argparse
import ast
import re
import subprocess
import sys

CHECKER_VERSION = '1.0'

# (ไฟล์, ชื่อตัวแปร) ที่ต้องเฝ้า — เพิ่มได้ แต่การเพิ่ม "รายการที่เฝ้า" ไม่อันตราย
# อันตรายคือการเพิ่ม "สมาชิกในรายการที่ถูกเฝ้า" ซึ่งคือสิ่งที่ด่านนี้จับ
WATCHED = [
    ('scripts/check_bot_add.py', 'ALLOWED_PATHS'),
    ('scripts/check_flawed_source.py', 'ALLOWED_KINDS'),
]

MIN_REASON_LEN = 8


def parse_list(text, var):
    """อ่านค่ารายการของตัวแปร จากไฟล์ในรูป "ข้อความล้วน"

    คืน (สถานะ, ค่า)
      'ok'         → ลิสต์ของสตริง
      'absent'     → ไม่มีตัวแปรนี้ในไฟล์ (หรือถูกคอมเมนต์ไว้)
      'multi'      → มีการประกาศตัวแปรนี้มากกว่า 1 ที่ ⇒ ตัดสินไม่ได้
      'unparsable' → เจอแล้วแต่อ่านค่าไม่ออก
    ⛔ 'absent' ไม่ใช่ 'ลิสต์ว่าง' — "ไม่มีให้เทียบ" ต่างจาก "เทียบแล้วไม่มีอะไร"
       (กับดัก ⑥ · เป็นเหตุผลเดียวกับที่ scan_symbols แยก UNKNOWN_PREV ออกมา)
    """
    # ^ ต้นบรรทัด ⇒ บรรทัดที่ถูกคอมเมนต์ (#) จะไม่เข้าเงื่อนไข — ตั้งใจ
    pat = re.compile(r'(?m)^[ \t]*' + re.escape(var) + r'\s*=\s*(\[[^\]]*\]|\([^)]*\))')
    ms = pat.findall(text)
    if not ms:
        return 'absent', None
    if len(ms) > 1:
        return 'multi', None
    try:
        v = ast.literal_eval(ms[0])
    except Exception:
        return 'unparsable', None
    if not isinstance(v, (list, tuple)):
        return 'unparsable', None
    return 'ok', list(v)


def declared(messages, var):
    """ข้อความ commit ในช่วงนี้ ประกาศการขยายรายการนี้ไว้หรือยัง

    รูปแบบที่รับ:  <ชื่อตัวแปร>+: <เหตุผล>
    ⛔ ต้องระบุ "ชื่อตัวแปร" ให้ตรง — ประกาศตัวแปรอื่นไม่นับ
    ⛔ ต้องมีเหตุผลจริง — เครื่องหมายโคลอนลอย ๆ ไม่นับ
    """
    pat = re.compile(re.escape(var) + r'\+:[ \t]*(\S[^\n]*)')
    for m in messages:
        if not isinstance(m, str):
            continue
        g = pat.search(m)
        if g and len(g.group(1).strip()) >= MIN_REASON_LEN:
            return True
    return False


def growth_verdict(prev, now, messages, var):
    """คืนรายการปัญหา [(รหัส, ข้อความ)] · ว่าง = ผ่าน

    prev / now = ลิสต์สมาชิก หรือ None (= ไม่มีตัวแปรนั้น ณ จุดนั้น)
    ⛔ เทียบด้วย "สมาชิก" ไม่ใช่ "จำนวน" และไม่ใช่ "สตริงทั้งก้อน"
       — เอาออก 1 ใส่เข้า 1 จำนวนเท่าเดิม แต่สิทธิ์เปลี่ยน ⇒ ต้องแดง
    ⛔ รายการที่ "หดลง" ไม่แดง — ลดสิทธิ์ไม่ต้องขออนุญาต
    """
    if now is None:
        return [('var-gone',
                 f'ไม่พบตัวแปร {var} ที่ HEAD แล้ว — ถ้าเปลี่ยนชื่อ ด่านนี้จะตาบอดทันที '
                 f'⇒ ต้องแก้รายการ WATCHED ของด่าน 10 ให้ตรงกันก่อน')]
    base = [] if prev is None else prev
    added = [x for x in now if x not in base]
    if not added:
        return []
    if declared(messages, var):
        return []
    return [('undeclared-growth',
             f'{var} โตขึ้น {len(added)} รายการ ({" · ".join(map(str, added))}) '
             f'โดยไม่มีบรรทัดประกาศในข้อความ commit ช่วงนี้ '
             f'⇒ เขียน "{var}+: <เหตุผล>" (อย่างน้อย {MIN_REASON_LEN} ตัวอักษร) '
             f'ในข้อความ commit')]


# ═════════════════════════════════════════════════════════════
#  SELF-TEST
# ═════════════════════════════════════════════════════════════
SRC_OK = """
import os
ALLOWED_PATHS = ['data/bank.json']
X = 1
"""

SRC_MULTILINE = """
ALLOWED_KINDS = (
    'multiple-correct',
    'no-correct',
)
"""

SRC_COMMENTED = """
# ALLOWED_PATHS = ['data/bank.json', 'data/secret.json']
ALLOWED_PATHS = ['data/bank.json']
"""

SRC_ONLY_COMMENT = """
# ALLOWED_PATHS = ['data/bank.json']
"""

SRC_TWICE = """
ALLOWED_PATHS = ['data/bank.json']
ALLOWED_PATHS = ['data/bank.json', 'data/anything.json']
"""

SRC_WEIRD = """
ALLOWED_PATHS = [os.environ['X']]
"""

# (ชื่อเคส, ข้อความไฟล์, ตัวแปร, สถานะที่ต้องได้, ค่าที่ต้องได้)
PARSE_CASES = [
    ("ลิสต์บรรทัดเดียว", SRC_OK, 'ALLOWED_PATHS', 'ok', ['data/bank.json']),
    ("ทูเปิลหลายบรรทัด", SRC_MULTILINE, 'ALLOWED_KINDS', 'ok',
     ['multiple-correct', 'no-correct']),
    ("🔴 บรรทัดที่ถูกคอมเมนต์ ⛔ ห้ามนับ (ไม่งั้นเอาของจริงไปซ่อนใต้ # ได้)",
     SRC_COMMENTED, 'ALLOWED_PATHS', 'ok', ['data/bank.json']),
    ("มีแต่บรรทัดคอมเมนต์ ⇒ ถือว่าไม่มีตัวแปร",
     SRC_ONLY_COMMENT, 'ALLOWED_PATHS', 'absent', None),
    ("ไม่มีตัวแปรนี้เลย ⇒ absent ⛔ ไม่ใช่ลิสต์ว่าง",
     SRC_OK, 'ALLOWED_KINDS', 'absent', None),
    ("🔴 ประกาศ 2 ที่ ⇒ ตัดสินไม่ได้ ⛔ ห้ามหยิบอันสุดท้ายมาเงียบ ๆ",
     SRC_TWICE, 'ALLOWED_PATHS', 'multi', None),
    ("🔴 ค่าไม่ใช่ค่าคงที่ ⇒ อ่านไม่ออก ⛔ ห้ามเดา",
     SRC_WEIRD, 'ALLOWED_PATHS', 'unparsable', None),
]

V = 'ALLOWED_PATHS'
OK_MSG = [f'แก้ด่าน 6\n\n{V}+: เพิ่มไฟล์ผลรวมชุดใหม่ตามมติครู 1 ส.ค.']

# (ชื่อเคส, prev, now, ข้อความ commit, รหัสที่ต้องเจอ | None = ต้องผ่าน)
#  ⛔ ใช้ชื่อไฟล์สมมติชุดใหม่ (aaa/bbb) ไม่ทับกับตัวอย่างจริงข้างบน — กับดัก ⑦ข
GROW_CASES = [
    ("ไม่มีอะไรเปลี่ยน ⇒ ผ่าน", ['aaa'], ['aaa'], [''], None),

    ("รายการหดลง ⇒ ผ่าน (ลดสิทธิ์ไม่ต้องขอ)", ['aaa', 'bbb'], ['aaa'], [''], None),

    ("สลับลำดับเฉย ๆ ⇒ ผ่าน (เทียบสมาชิก ไม่ใช่ลำดับ)",
     ['aaa', 'bbb'], ['bbb', 'aaa'], [''], None),

    ("🔴 เพิ่ม 1 รายการ ไม่ประกาศ ⇒ แดง", ['aaa'], ['aaa', 'bbb'], [''],
     'undeclared-growth'),

    ("เพิ่ม 1 รายการ + ประกาศครบ ⇒ ผ่าน", ['aaa'], ['aaa', 'bbb'], OK_MSG, None),

    ("🔴 ประกาศแต่ไม่ให้เหตุผล (โคลอนลอย ๆ) ⇒ แดง",
     ['aaa'], ['aaa', 'bbb'], [f'{V}+:   '], 'undeclared-growth'),

    ("🔴 ประกาศชื่อตัวแปรอื่น ⇒ แดง (ประกาศผิดช่องไม่นับ)",
     ['aaa'], ['aaa', 'bbb'], ['ALLOWED_KINDS+: เพิ่มชนิดใหม่ตามมติ'],
     'undeclared-growth'),

    ("ประกาศอยู่ในข้อความ commit ที่ 2 จาก 3 ⇒ ผ่าน",
     ['aaa'], ['aaa', 'bbb'], ['ปรับ log', OK_MSG[0], 'แก้คำผิด'], None),

    ("🔴 เอาออก 1 ใส่เข้า 1 (จำนวนเท่าเดิม) ⇒ ยังต้องแดง",
     ['aaa', 'bbb'], ['aaa', 'ccc'], [''], 'undeclared-growth'),

    ("🔴 ฐานไม่มีตัวแปรนี้ (ไฟล์เพิ่งเกิด) ⇒ ทั้งก้อนคือของใหม่ ⇒ แดง",
     None, ['aaa'], [''], 'undeclared-growth'),

    ("ฐานไม่มีตัวแปร แต่ที่ HEAD ก็ยังว่าง ⇒ ผ่าน", None, [], [''], None),

    ("🔴 ตัวแปรหายไปจาก HEAD (เปลี่ยนชื่อหนีด่าน) ⇒ แดง",
     ['aaa'], None, OK_MSG, 'var-gone'),

    ("สมาชิกซ้ำในตัวเอง ⇒ ไม่ถือว่าโต", ['aaa'], ['aaa', 'aaa'], [''], None),

    ("🔴 ข้อความ commit เป็น None ปนมา ⇒ ต้องไม่ล้ม และยังแดงตามเดิม",
     ['aaa'], ['aaa', 'bbb'], [None, ''], 'undeclared-growth'),
]


def _mut_compare_len(prev, now, messages, var):
    """มิวแทนต์ ① เทียบด้วยจำนวนสมาชิก ⇒ สลับเข้า-ออกเท่ากันจะรอด"""
    if now is None:
        return [('var-gone', '')]
    base = [] if prev is None else prev
    if len(now) <= len(base) or declared(messages, var):
        return []
    return [('undeclared-growth', '')]


def _mut_any_plus(prev, now, messages, var):
    """มิวแทนต์ ② เห็น "+:" ที่ไหนก็ถือว่าประกาศแล้ว ⇒ ประกาศผิดช่องก็ผ่าน"""
    if now is None:
        return [('var-gone', '')]
    base = [] if prev is None else prev
    added = [x for x in now if x not in base]
    if not added:
        return []
    if any(isinstance(m, str) and '+:' in m for m in messages):
        return []
    return [('undeclared-growth', '')]


def _mut_ignore_var_gone(prev, now, messages, var):
    """มิวแทนต์ ③ ตัวแปรหายไปก็ถือว่าไม่มีอะไรโต ⇒ เปลี่ยนชื่อหนีด่านได้"""
    if now is None:
        return []
    return growth_verdict(prev, now, messages, var)


def _mut_never_red(prev, now, messages, var):
    """มิวแทนต์ ④ ไม่แดงเลย ⇒ กติกากลับไปอยู่แต่ในจดหมาย"""
    return []


def _mut_prev_absent_is_free(prev, now, messages, var):
    """มิวแทนต์ ⑤ ฐานไม่มีตัวแปร = ปล่อยผ่าน ⇒ สร้างไฟล์ใหม่แล้วใส่อะไรก็ได้"""
    if prev is None:
        return []
    return growth_verdict(prev, now, messages, var)


def _run_grow(fn):
    fails = []
    for name, prev, now, msgs, want in GROW_CASES:
        try:
            codes = [c for c, _ in fn(prev, now, msgs, V)]
            good = (codes == []) if want is None else (want in codes)
        except Exception:
            good = False
        if not good:
            fails.append(name)
    return fails


def selftest():
    print('─' * 62)
    print(f'SELF-TEST ด่าน 10 v{CHECKER_VERSION} — รายการที่อนุญาตต้องไม่โตเงียบ ๆ')
    print('─' * 62)
    ok = True

    print('  รายการที่เฝ้าอยู่:')
    for f, v in WATCHED:
        print(f'     {f} · {v}')
    print()

    print('  ── อ่านค่ารายการจากไฟล์ (ข้อความล้วน ⛔ ไม่ import) ──')
    for name, src, var, want_st, want_v in PARSE_CASES:
        st, v = parse_list(src, var)
        good = (st == want_st) and (v == want_v)
        why = '' if good else f'   ← ได้ ({st}, {v})'
        print(f'  {"✅" if good else "🔴"}  {name}{why}')
        ok &= good

    print()
    print('  ── ตัดสินว่า "โตขึ้นโดยไม่ประกาศ" หรือไม่ ──')
    for name, prev, now, msgs, want in GROW_CASES:
        codes = [c for c, _ in growth_verdict(prev, now, msgs, V)]
        good = (codes == []) if want is None else (want in codes)
        why = '' if good else f'   ← ได้ {codes} ต้องการ {want}'
        print(f'  {"✅" if good else "🔴"}  {name}{why}')
        ok &= good

    print()
    print('  ── ใส่บั๊กเข้าไปแล้วด่านต้องล้ม ──')
    print('     ⑦ข: แดงแล้วยังต้องถามต่อว่า “แดงเพราะเคสที่ตั้งใจหรือเปล่า”')
    for label, fails in (
        ('① เทียบด้วยจำนวนสมาชิก',        _run_grow(_mut_compare_len)),
        ('② เห็น "+:" ที่ไหนก็ผ่าน',       _run_grow(_mut_any_plus)),
        ('③ ตัวแปรหายไปก็ไม่ว่า',          _run_grow(_mut_ignore_var_gone)),
        ('④ ไม่แดงเลย',                    _run_grow(_mut_never_red)),
        ('⑤ ฐานไม่มีตัวแปร = ปล่อยผ่าน',   _run_grow(_mut_prev_absent_is_free)),
    ):
        good = len(fails) > 0
        print(f'  {"✅" if good else "🔴"}  มิวแทนต์ {label} ⇒ ล้ม {len(fails)}/{len(GROW_CASES)} เคส')
        for f in fails[:2]:
            print(f'         ↳ จับได้ที่: {f}')
        ok &= good

    print()
    if not WATCHED:
        print('  🔴 รายการ WATCHED ว่าง ⇒ ด่านนี้จะเขียวตลอดกาลโดยไม่เฝ้าอะไร')
        ok = False
    else:
        print(f'  ✅  รายการ WATCHED ไม่ว่าง ({len(WATCHED)} รายการ)')

    print()
    if not ok:
        print('🔴 SELF-TEST ไม่ผ่าน ⇒ ผลของด่านนี้กับของจริงเชื่อไม่ได้')
        return 2
    print(f'✅ SELF-TEST ผ่านครบ {len(PARSE_CASES)} + {len(GROW_CASES)} เคส'
          f' + มิวแทนต์ 5 ตัว')
    return 0


# ── ฝั่งที่คุยกับ git ──────────────────────────────────────────
def git(*a):
    """คืน (สำเร็จไหม, ข้อความ) — ⛔ ห้ามกลืนรหัสออกของ git"""
    try:
        r = subprocess.run(('git',) + a, capture_output=True, text=True)
    except Exception as e:
        return False, str(e)
    if r.returncode != 0:
        return False, (r.stderr or '').strip()
    return True, r.stdout


def read_at_base(path, base):
    """หาค่า "ก่อนหน้า" ของไฟล์ที่เฝ้าอยู่ — คืน (สถานะ, ข้อความไฟล์, คอมมิตที่ใช้)

      'ok'       → ไฟล์มีอยู่ที่คอมมิตฐานตรง ๆ
      'historic' → ไฟล์ไม่มีที่ฐาน แต่เคยมีในประวัติ ⇒ ใช้ครั้งล่าสุดที่ยังมี
      'never'    → ไม่เคยมีไฟล์นี้ในประวัติเลย ⇒ ไม่มีของให้เทียบจริง ๆ

    🔴 ทำไมต้องมี 'historic':
       ถ้าเทียบเฉพาะที่คอมมิตฐาน คนที่อยากขยายสิทธิ์เงียบ ๆ แค่
       "ลบไฟล์ทิ้งแล้วสร้างใหม่ในคอมมิตเดียว" ก็ทำให้ด่านนี้เห็นเป็น
       "ไฟล์ใหม่ ไม่มีของเทียบ" ได้ทันที ⇒ ช่องโหว่ที่เขียนได้ใน 1 บรรทัด
       ⇒ ต้องไล่ย้อนประวัติหาเวอร์ชันล่าสุดที่ยังมีตัวไฟล์อยู่
    """
    ok, txt = git('show', f'{base}:{path}')
    if ok:
        return 'ok', txt, base
    ok2, out = git('rev-list', base, '--', path)
    if ok2:
        for sha in out.split()[:20]:
            ok3, txt3 = git('show', f'{sha}:{path}')
            if ok3:
                return 'historic', txt3, sha
    return 'never', None, None


def main():
    ap = argparse.ArgumentParser(
        description='ตรวจว่ารายการ "สิ่งที่อนุญาต" ไม่โตขึ้นโดยไม่ประกาศ')
    ap.add_argument('--base', default=None,
                    help='คอมมิตฐานที่จะเทียบด้วย (ถ้าไม่ระบุ ใช้ HEAD~1)')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    a = ap.parse_args()

    if a.version:
        print(CHECKER_VERSION)
        return 0
    if a.selftest:
        return selftest()

    base = a.base or 'HEAD~1'
    okb, _ = git('rev-parse', '--verify', base + '^{commit}')
    if not okb:
        print(f'🔴 หาคอมมิตฐาน "{base}" ไม่เจอ ⇒ เทียบไม่ได้')
        print('   ⛔ "เทียบไม่ได้" ไม่เท่ากับ "เทียบแล้วผ่าน"')
        print('   (ถ้าเป็นคอมมิตแรกของ repo หรือ checkout ตื้น ให้ตั้ง fetch-depth: 0)')
        return 2

    okm, msgs_raw = git('log', '--format=%B%x00', f'{base}..HEAD')
    if not okm:
        print(f'🔴 อ่านข้อความ commit ช่วง {base}..HEAD ไม่ได้')
        return 2
    messages = [m for m in msgs_raw.split('\x00') if m.strip()]
    if not messages:
        # ช่วงว่าง (เช่น HEAD = base) — ยังต้องอ่านข้อความของ HEAD เอง
        _, m1 = git('log', '-1', '--format=%B', 'HEAD')
        messages = [m1]

    print(f'ด่าน 10 v{CHECKER_VERSION} · เทียบ {base} → HEAD '
          f'· ข้อความ commit ในช่วง {len(messages)} ก้อน')
    print()

    red = 0
    for path, var in WATCHED:
        # ── ค่า "ตอนนี้" อ่านจากไฟล์ที่จะถูกใช้จริง (working tree ของ CI) ──
        try:
            now_txt = open(path, encoding='utf-8').read()
        except Exception as e:
            print(f'🔴 อ่าน {path} ไม่ได้ — {e}')
            return 2
        st_now, v_now = parse_list(now_txt, var)
        if st_now in ('multi', 'unparsable'):
            print(f'🔴 {path} · {var} → {st_now} ⇒ ตัดสินไม่ได้')
            print('   ⛔ ตัดสินไม่ได้ ต้องแดงแบบเครื่องมือ ไม่ใช่ปล่อยผ่าน')
            return 2

        # ── ค่า "ที่ฐาน" อ่านจาก git โดยตรง ──
        how, prev_txt, at = read_at_base(path, base)
        if how == 'never':
            n = 0 if v_now is None else len(v_now)
            print(f'🟠 {path} · {var} — ไฟล์นี้ไม่เคยมีในประวัติก่อนหน้า '
                  f'({n} รายการ) ⇒ รอบนี้ยังไม่มีของให้เทียบ')
            print('     ⛔ บันทึกไว้ให้เห็นในบันทึก CI ว่า "ยังไม่ได้เทียบ" '
                  'ไม่ใช่ "เทียบแล้วผ่าน" — รอบหน้าจึงจะเฝ้าได้จริง')
            continue
        if how == 'historic':
            print(f'🟠 {path} · {var} — ไฟล์ไม่มีที่คอมมิตฐาน '
                  f'⇒ ย้อนไปใช้ครั้งล่าสุดที่ยังมี ({at[:7]}) '
                  f'(กันวิธีลบทิ้งแล้วสร้างใหม่เพื่อล้างของเทียบ)')
        st_prev, v_prev = parse_list(prev_txt, var)
        if st_prev in ('multi', 'unparsable'):
            print(f'🔴 {path} · {var} ที่ฐานอ่านไม่ออก ({st_prev}) ⇒ เทียบไม่ได้')
            return 2

        probs = growth_verdict(v_prev, v_now, messages, var)
        shown_prev = '(ไม่มีที่ฐาน)' if v_prev is None else str(v_prev)
        shown_now = '(หายไปแล้ว)' if v_now is None else str(v_now)
        if probs:
            red += 1
            print(f'🔴 {path} · {var}')
            print(f'     ฐาน   : {shown_prev}')
            print(f'     HEAD  : {shown_now}')
            for code, msg in probs:
                print(f'     [{code}] {msg}')
        else:
            n = 0 if v_now is None else len(v_now)
            print(f'✅ {path} · {var} — {n} รายการ ไม่โตขึ้นโดยไม่ประกาศ')
    print()
    if red:
        print(f'🔴 มี {red} รายการที่ขยายสิทธิ์โดยไม่ประกาศ')
        return 1
    print('✅ ไม่มีรายการอนุญาตใดโตขึ้นโดยไม่ประกาศ')
    return 0


if __name__ == '__main__':
    sys.exit(main())

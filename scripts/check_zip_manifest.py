#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_zip_manifest.py — ตรวจว่า "ของในซอง" ตรงกับ "ตารางไฟล์ใน README ของซอง"
==============================================================================

⚠️ ที่มาของไฟล์นี้ (31 ก.ค. 2569 · ทีมพอร์ทัลรอบ 10 ทักมา)

   พอร์ทัลทักว่า: "ในซองมี 3 ไฟล์ แต่ README ระบุแค่ 2 · ไม่ได้ระบุ README เอง
                  ⇒ ด่าน namelist-vs-README ของคุณอาจยกเว้นตัวเองอยู่
                  ⇒ ถ้ายกเว้นโดยตั้งใจก็เขียนไว้ในโค้ดว่ายกเว้นเพราะอะไร"

   ผมไปหาด่านนั้นเพื่อดูว่ายกเว้นตรงไหน — แล้วพบว่า **ไม่มีด่านนั้นอยู่จริง**
   ผมเทียบด้วยตาทุกรอบ แล้วรายงานว่า "README ตรงกับซอง" ราวกับมีตัวตรวจรัน
   ⇒ รอบที่ผมเผลอ มันจึงหลุด และไม่มีอะไรร้อง

   นี่คือ **กับดักข้อ 6** เต็ม ๆ: *ทางที่ไม่ได้เดิน ≠ ทางที่เดินแล้วไม่เจอ*
   ผมรายงานผลของทางที่ไม่เคยเดิน — และมันตรงกับประโยคที่พอร์ทัลยกกลับมาพอดี:
   "กติกาที่อยู่แต่ในจดหมายจะหายไปใน 3 เดือน" — ของผมหายไปใน 1 รอบ

   ⇒ ไฟล์นี้คือด่านนั้น "ที่มีตัวตนจริง" · ⛔ ไม่มีการยกเว้นไฟล์ใดทั้งสิ้น
      README ต้องระบุ **ตัวมันเอง** ด้วย ไม่งั้นแดง

หลักการที่ยึด (เหมือน scan_symbols.py):
   "อ่านตารางไม่ได้" ต้องไม่ให้ผลเหมือน "อ่านแล้วไม่พบข้อผิด"
   ⇒ ถ้าแกะรายชื่อจาก README ไม่ได้สักไฟล์ = แดง ไม่ใช่ผ่าน

รหัสออก:
    0 = ตรงกันทุกไฟล์
    1 = ไม่ตรง / อ่านไม่ได้ / ไม่มี README — ห้ามส่งซองนี้

การใช้:
    python scripts/check_zip_manifest.py out/fix-xxx.zip
    python scripts/check_zip_manifest.py --selftest      # ด่านของตัวด่านเอง
"""
import sys, re, zipfile, hashlib, argparse, io

CHECKER_VERSION = '1.1'

# แถวตารางมาร์กดาวน์: | `ชื่อไฟล์` | 40,467 B | `md5` |
ROW = re.compile(r'^\s*\|\s*`([^`]+)`\s*\|(.*)$')
MD5 = re.compile(r'`([0-9a-f]{32})`')
SIZE = re.compile(r'([\d,]+)\s*B\b')


def read_manifest(text):
    """แกะตารางไฟล์จากเนื้อ README — คืน ({ชื่อไฟล์: {'md5':…, 'size':…}}, ชื่อที่ซ้ำ[])

    ⛔ ไม่ยกเว้นชื่อใดทั้งสิ้น — รวมถึงตัว README เอง
       (จุดที่พลาดรอบก่อน: README ไม่ได้ระบุตัวเอง แล้วไม่มีใครร้อง)

    ⚠️ ชื่อซ้ำสองแถวต้องรายงาน ไม่ใช่ให้แถวหลังทับแถวแรกเงียบ ๆ —
       ตารางที่ขัดกันเองคือ "เทียบไม่ได้" ไม่ใช่ "เทียบแล้วตรง" (กับดักข้อ 6)
    """
    found, dups = {}, []
    for line in text.splitlines():
        m = ROW.match(line)
        if not m:
            continue
        name, rest = m.group(1).strip(), m.group(2)
        # กันหัวตาราง/เส้นคั่น และเซลล์ที่ไม่ใช่ชื่อไฟล์
        if '.' not in name or name.startswith('-'):
            continue
        h = MD5.search(rest)
        z = SIZE.search(rest)
        row = {'md5': h.group(1) if h else None,
               'size': int(z.group(1).replace(',', '')) if z else None}
        if name in found and name not in dups:
            dups.append(name)
        found[name] = row
    return found, sorted(dups)

# ─────────────────────────────────────────────────────────────
# v1.1 — ถ้อยคำสองกลุ่ม
# ─────────────────────────────────────────────────────────────
# จัดกลุ่มตาม "ต้องไปแก้ที่ไหน" ไม่ใช่ตามความรุนแรง — ทั้งสองกลุ่มยังออกรหัส 1 เหมือนกัน
#   ซองนี้ผิด        ⇒ ของในซองไม่ตรงกับที่ประกาศ         ⇒ ไปแก้ที่ "ไฟล์ในซอง"
#   ซองนี้ตรวจไม่ได้ ⇒ สารบัญไม่มีข้อมูลพอให้เทียบได้เลย   ⇒ ไปแก้ที่ "README"
# เหตุผลที่ต้องแยก: รอบ 9 รายงานว่า "README ตรงกับซอง" ทั้งที่ตารางไม่มี md5 สักไฟล์
#   — นั่นไม่ใช่ "ตรวจแล้วผ่าน" แต่คือ "ไม่เคยได้ตรวจ" คนอ่านต้องแยกออกจากกันได้ทันที
B_WRONG = 'ซองนี้ผิด'
B_BLIND = 'ซองนี้ตรวจไม่ได้'

# ⚠️ กลุ่มที่ยังรอคำตอบพอร์ทัล (รอบ 12 ข้อ 7): "README ระบุชื่อ แต่ไม่มีไฟล์ในซอง"
#    อ่านได้สองทาง — ลืมใส่ไฟล์ (ซองผิด) หรือ พิมพ์ชื่อเกิน (README ผิด)
#    ตอนนี้จัดไว้ที่ B_WRONG ชั่วคราว และพิมพ์กำกับไว้ให้เห็นว่ายังไม่ยุติ
B_PENDING = B_WRONG


def _summary(fails):
    """หัวรายงาน — บอกจำนวนแยกสองกลุ่มเสมอ แม้กลุ่มหนึ่งจะเป็นศูนย์"""
    w = sum(1 for b, _ in fails if b == B_WRONG)
    u = sum(1 for b, _ in fails if b == B_BLIND)
    return f"  ผิด {w} จุด · ตรวจไม่ได้ {u} จุด"


def _render(fails, body=None):
    return [_summary(fails)] + [f"  🔴 {b} · {m}" for b, m in fails] + list(body or [])


def check_zip(path_or_bytes, name='<ซอง>'):
    """คืน (ผ่านไหม, บรรทัดรายงาน[]) — ไม่พิมพ์เอง เพื่อให้ selftest เรียกได้"""
    try:
        srcf = (io.BytesIO(path_or_bytes) if isinstance(path_or_bytes, bytes)
                else path_or_bytes)
        z = zipfile.ZipFile(srcf)
    except Exception as e:
        return False, _render([(B_BLIND, f"เปิดซองไม่ได้: {name} — {e}")])

    names = [n for n in z.namelist() if not n.endswith('/')]
    readmes = [n for n in names
               if n.upper().startswith('README') and '/' not in n]
    if not readmes:
        return False, _render(
            [(B_BLIND, "ไม่พบ README ที่ระดับบนสุดของซอง")],
            ["     ⇒ ไม่มีอะไรให้เทียบ = เทียบไม่ได้ ⇒ ไม่ถือว่าผ่าน"])
    if len(readmes) > 1:
        return False, _render(
            [(B_BLIND, f"พบ README มากกว่าหนึ่ง: {', '.join(readmes)}")],
            ["     ⇒ ไม่รู้ว่าฉบับไหนคือสารบัญจริง ⇒ ไม่ถือว่าผ่าน"])
    rd = readmes[0]

    try:
        text = z.read(rd).decode('utf-8')
    except Exception as e:
        return False, _render([(B_BLIND, f"อ่าน {rd} ไม่ได้ — {e}")])

    declared, dups = read_manifest(text)
    if dups:
        return False, _render(
            [(B_BLIND, f"{rd} ระบุชื่อซ้ำ: {', '.join(dups)}")],
            ["     ⇒ ตารางขัดกันเอง = เทียบไม่ได้ ⇒ ไม่ถือว่าผ่าน"])
    if not declared:
        # 🔴 หัวใจของด่านนี้: "แกะตารางไม่ได้" ต้องไม่เท่ากับ "ไม่พบข้อผิด"
        return False, _render(
            [(B_BLIND, f"แกะตารางไฟล์จาก {rd} ไม่ได้สักบรรทัด")],
            ["     ⇒ 0 ข้อผิด ในที่นี้แปลว่า 'ไม่ได้ตรวจ' ไม่ใช่ 'ตรวจแล้วสะอาด'",
             "     รูปแบบที่รองรับ: | `ชื่อไฟล์` | 1,234 B | `md5` |"])

    inzip, indoc = set(names), set(declared)
    missing_doc = sorted(inzip - indoc)   # อยู่ในซอง แต่ README ไม่ได้ระบุ
    missing_zip = sorted(indoc - inzip)   # README ระบุ แต่ไม่มีในซอง
    fails, notes = [], []

    notes.append(f"  ซอง {name} · {len(inzip)} ไฟล์ · สารบัญ {rd} ระบุ {len(indoc)} ไฟล์")
    for n in missing_doc:
        extra = " ⟵ ตัว README เอง (⛔ ไม่มีข้อยกเว้น ต้องระบุตัวเองด้วย)" if n == rd else ""
        # สารบัญไม่ครบ ⇒ ของชิ้นนั้นไม่เคยถูกเทียบเลย ⇒ เป็นเรื่อง "ตรวจไม่ได้"
        fails.append((B_BLIND, f"อยู่ในซอง แต่ README ไม่ได้ระบุ: {n}{extra}"))
    for n in missing_zip:
        fails.append((B_PENDING, f"README ระบุ แต่ไม่มีในซอง: {n}"
                                 "  (⚠️ กลุ่มนี้ยังรอคำตอบพอร์ทัล)"))

    verified = 0
    for n in sorted(inzip & indoc):
        raw = z.read(n)
        d = declared[n]
        if d['md5'] is None or d['size'] is None:
            # ── ข้อยกเว้นเดียวในไฟล์นี้ และมันมีเหตุผลเชิงตรรกะ ไม่ใช่ความสะดวก ──
            #    README คำนวณ md5 ของ "ตัวเองหลังใส่ md5 ลงไป" ไม่ได้ (วนซ้ำไม่รู้จบ)
            #    ⇒ ยกเว้นเฉพาะ "การเทียบเนื้อ" ของตัว README เท่านั้น
            #      ⛔ ไม่ได้ยกเว้น "การต้องมีชื่ออยู่ในสารบัญ" — นั่นยังบังคับเหมือนเดิม
            if n == rd:
                notes.append(f"  ℹ️ {n} — เทียบได้แค่ชื่อ (README คำนวณ md5 ของตัวเองไม่ได้)")
            else:
                fails.append((B_BLIND, f"{n} — README ระบุชื่อ แต่ขาด md5/ขนาด"
                                       " ⇒ เทียบเนื้อไม่ได้ ⇒ ไม่ถือว่าตรง"))
            continue
        verified += 1
        if d['md5'] and hashlib.md5(raw).hexdigest() != d['md5']:
            fails.append((B_WRONG, f"md5 ไม่ตรง: {n}"
                                   f" · ซอง {hashlib.md5(raw).hexdigest()} · README {d['md5']}"))
        if d['size'] is not None and len(raw) != d['size']:
            fails.append((B_WRONG, f"ขนาดไม่ตรง: {n} · ซอง {len(raw):,} B"
                                   f" · README {d['size']:,} B"))

    if not fails:
        # ⚠️ บรรทัดสรุปต้องไม่พูดเกินสิ่งที่ตรวจจริง — บอกจำนวนที่ "เทียบเนื้อ" ได้จริง
        notes.append(f"  ✅ ตรงกันครบ {len(inzip)} ไฟล์"
                     f" · เทียบเนื้อจริง (md5+ขนาด) {verified} ไฟล์"
                     f" · เทียบได้แค่ชื่อ {len(inzip) - verified} ไฟล์ (สารบัญเอง)")
        return True, notes
    return False, _render(fails, notes)


# ─────────────────────────────────────────────────────────────
def _mkzip(files):
    b = io.BytesIO()
    with zipfile.ZipFile(b, 'w') as z:
        for n, c in files.items():
            z.writestr(n, c)
    return b.getvalue()


def selftest():
    """ด่านของตัวด่านเอง — ถ้าตัวตรวจนี้ตาบอด ต้องรู้ก่อนใช้งานจริง"""
    print(f"check_zip_manifest.py v{CHECKER_VERSION} — ด่านตัวเอง\n")
    A, Bc = b'aaa\n', b'bbb\n'
    ma, mb = hashlib.md5(A).hexdigest(), hashlib.md5(Bc).hexdigest()

    def rd(rows):
        return ("# ซองทดสอบ\n\n| ไฟล์ | ขนาด | md5 |\n|---|---|---|\n" + rows).encode()

    good_rows = (f"| `a.py` | {len(A)} B | `{ma}` |\n"
                 f"| `b.json` | {len(Bc)} B | `{mb}` |\n")
    # ⚠️ ต้องคำนวณ md5 ของ README เองแบบวนซ้ำไม่ได้ ⇒ ระบุชื่อ+เว้น md5 ไว้
    self_row = "| `README.md` | | เอกสารนี้เอง |\n"

    ok_zip = _mkzip({'a.py': A, 'b.json': Bc, 'README.md': rd(good_rows + self_row)})
    bad_self = _mkzip({'a.py': A, 'b.json': Bc, 'README.md': rd(good_rows)})
    extra = _mkzip({'a.py': A, 'b.json': Bc, 'c.txt': b'c\n',
                    'README.md': rd(good_rows + self_row)})
    ghost = _mkzip({'a.py': A, 'README.md': rd(good_rows + self_row)})
    notable = _mkzip({'a.py': A,
                       'README.md': '# ซอง\n\nไม่มีตารางไฟล์เลย\n'.encode()})
    nordme = _mkzip({'a.py': A, 'b.json': Bc})
    badmd5 = _mkzip({'a.py': Bc, 'b.json': Bc, 'README.md': rd(good_rows + self_row)})
    badsize = _mkzip({'a.py': A, 'b.json': Bc,
                      'README.md': rd(f"| `a.py` | 999 B | `{ma}` |\n"
                                      f"| `b.json` | {len(Bc)} B | `{mb}` |\n" + self_row)})
    # ไฟล์ธรรมดาที่ระบุชื่อไว้เฉย ๆ ไม่มี md5 — ต้องแดง (ยกเว้นได้เฉพาะตัว README)
    nohash = _mkzip({'a.py': A, 'b.json': Bc,
                     'README.md': rd(f"| `a.py` | {len(A)} B | `{ma}` |\n"
                                     "| `b.json` | | ยังไม่ได้ใส่ |\n" + self_row)})
    duprow = _mkzip({'a.py': A, 'b.json': Bc,
                     'README.md': rd(f"| `a.py` | {len(A)} B | `{mb}` |\n"
                                     + good_rows + self_row)})

    # v1.1 — ซองที่ผิด "สองกลุ่มพร้อมกัน" ไว้ทดสอบหัวรายงาน
    mixed = _mkzip({'a.py': Bc, 'b.json': Bc,
                    'README.md': rd(f"| `a.py` | {len(A)} B | `{ma}` |\n"
                                    "| `b.json` | | ยังไม่ได้ใส่ |\n" + self_row)})

    gates = [
        ("ซองถูกต้อง (README ระบุครบ รวมตัวเอง) ⇒ ผ่าน", check_zip(ok_zip)[0] is True),
        ("🔴 README ไม่ระบุตัวเอง ⇒ ต้องแดง (บั๊กจริงของซอง v4)",
         check_zip(bad_self)[0] is False),
        ("…และต้องชี้ว่าไฟล์ที่ขาดคือตัว README เอง (ผูกกับลูกศร ไม่ใช่สตริงกว้าง ๆ)",
         '⟵ ตัว README เอง' in ' '.join(check_zip(bad_self)[1])),
        ("(กันด่านหลอกตัวเอง) ซองที่ผ่านต้องไม่มีลูกศรนั้นเลย",
         '⟵ ตัว README เอง' not in ' '.join(check_zip(ok_zip)[1])),
        ("มีไฟล์เกินในซอง ⇒ แดง", check_zip(extra)[0] is False),
        ("README ระบุไฟล์ที่ไม่มีในซอง ⇒ แดง", check_zip(ghost)[0] is False),
        ("README ไม่มีตารางเลย ⇒ แดง ('อ่านไม่ได้' ≠ 'ไม่พบข้อผิด')",
         check_zip(notable)[0] is False),
        ("ไม่มี README ในซอง ⇒ แดง", check_zip(nordme)[0] is False),
        ("md5 ไม่ตรง ⇒ แดง", check_zip(badmd5)[0] is False),
        ("ขนาดไม่ตรง ⇒ แดง", check_zip(badsize)[0] is False),
        ("(ต้องไม่จับ) ซองถูกต้องต้องไม่ถูกจับด้วยเหตุ md5",
         'md5 ไม่ตรง' not in ' '.join(check_zip(ok_zip)[1])),
        ("แกะตารางได้ทั้ง 3 แถว (รวม README ที่ไม่มี md5)",
         len(read_manifest(rd(good_rows + self_row).decode())[0]) == 3),
        ("ไฟล์ธรรมดาที่ระบุชื่อแต่ไม่มี md5 ⇒ แดง ('เทียบไม่ได้' ≠ 'ตรง')",
         check_zip(nohash)[0] is False),
        ("…แต่ตัว README เองไม่มี md5 ได้ (ยกเว้นเฉพาะการเทียบเนื้อ มีเหตุผลเชิงตรรกะ)",
         check_zip(ok_zip)[0] is True),
        ("README ระบุชื่อซ้ำ (แถวแรกผิด แถวหลังถูก) ⇒ แดง — ด่านอื่นจับไม่ได้เลย",
         check_zip(duprow)[0] is False),
        ("…และต้องบอกชื่อไฟล์ที่ซ้ำ ไม่ใช่แค่บอกว่าซ้ำ",
         'a.py' in ' '.join(check_zip(duprow)[1])),
        ("แกะตารางแล้วต้องรายงานชื่อซ้ำได้",
         read_manifest(rd(good_rows + good_rows + self_row).decode())[1] ==
         ['a.py', 'b.json']),
        ("บรรทัดสรุปต้องบอกจำนวนที่เทียบเนื้อจริง ไม่พูดเกิน (ถ้อยคำต้องไม่ชนของแดง)",
         'เทียบเนื้อจริง (md5+ขนาด) 2 ไฟล์' in ' '.join(check_zip(ok_zip)[1])),
        # ── v1.1: ถ้อยคำสองกลุ่ม (แยกตาม "ไปแก้ที่ไหน" ไม่ใช่ความรุนแรง) ──
        ("md5 ไม่ตรง ⇒ ต้องติดป้าย 'ซองนี้ผิด' (ไปแก้ที่ไฟล์ในซอง)",
         B_WRONG in ' '.join(check_zip(badmd5)[1])),
        ("ขนาดไม่ตรง ⇒ ต้องติดป้าย 'ซองนี้ผิด'",
         B_WRONG in ' '.join(check_zip(badsize)[1])),
        ("ระบุชื่อแต่ไม่มี md5 ⇒ ต้องติดป้าย 'ซองนี้ตรวจไม่ได้' (ไปแก้ที่ README)",
         B_BLIND in ' '.join(check_zip(nohash)[1])),
        ("README ระบุชื่อซ้ำ ⇒ 'ซองนี้ตรวจไม่ได้'",
         B_BLIND in ' '.join(check_zip(duprow)[1])),
        ("README ไม่มีตารางเลย ⇒ 'ซองนี้ตรวจไม่ได้'",
         B_BLIND in ' '.join(check_zip(notable)[1])),
        ("ไม่มี README ⇒ 'ซองนี้ตรวจไม่ได้'",
         B_BLIND in ' '.join(check_zip(nordme)[1])),
        ("README ไม่ระบุตัวเอง ⇒ 'ซองนี้ตรวจไม่ได้' (ของชิ้นนั้นไม่เคยถูกเทียบ)",
         B_BLIND in ' '.join(check_zip(bad_self)[1])),
        ("md5 ผิดล้วน ⇒ หัวรายงานต้องยังบอกกลุ่มที่เป็นศูนย์ด้วย",
         'ผิด 1 จุด · ตรวจไม่ได้ 0 จุด' in ' '.join(check_zip(badmd5)[1])),
        ("ซองที่ผิดทั้งสองกลุ่ม ⇒ หัวรายงานต้องนับแยกถูก",
         'ผิด 1 จุด · ตรวจไม่ได้ 1 จุด' in ' '.join(check_zip(mixed)[1])),
        ("ทั้งสองกลุ่มยังห้ามส่งซองเหมือนกัน (แยกถ้อยคำ ไม่ใช่ลดชั้น)",
         check_zip(badmd5)[0] is False and check_zip(nohash)[0] is False),
        ("(กันด่านหลอกตัวเอง) ซองที่ผ่านต้องไม่มีคำของทั้งสองกลุ่มเลย",
         B_WRONG not in ' '.join(check_zip(ok_zip)[1])
         and B_BLIND not in ' '.join(check_zip(ok_zip)[1])),
    ]
    ok = True
    for name, passed in gates:
        print(f"  {'✅' if passed else '🔴 ล้ม'}  {name}")
        if not passed:
            ok = False
    print(f"\n  ⇒ {'✅ ด่านตัวเองผ่านครบ' if ok else '🔴 ด่านตัวเองล้ม — ห้ามเชื่อผลของจริง'}")
    return ok


def main():
    ap = argparse.ArgumentParser(description='เทียบของในซองกับตารางไฟล์ใน README ของซอง')
    ap.add_argument('zip', nargs='?', help='ไฟล์ .zip ที่จะตรวจ')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    a = ap.parse_args()

    if a.version:
        print(CHECKER_VERSION)
        return
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    if not a.zip:
        ap.error('ต้องระบุไฟล์ zip หรือใช้ --selftest')

    # ⛔ ด่านแรกเสมอ: ถ้าตัวตรวจตาบอด ผลของจริงเชื่อไม่ได้
    if not selftest():
        sys.exit(1)
    print()
    ok, lines = check_zip(a.zip, a.zip)
    for l in lines:
        print(l)
    print(f"\n  ⇒ {'✅ ส่งซองได้' if ok else '🔴 ห้ามส่งซองนี้'}")
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()

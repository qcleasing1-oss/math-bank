#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_zip_real_change.py — ด่าน "ซองต้องมีของเปลี่ยนจริง"
==============================================================================

⚠️ ที่มาของไฟล์นี้ (2 ส.ค. 2569 · กัดเข้าจริงในวันเดียวกับที่เขียน)

   ทีมพอร์ทัลเปิดซองรอบ 17 แล้วรายงานว่า "ซองว่าง — ไม่มีของเปลี่ยนเลย"
   ผมวัดแล้วพบว่าซองไม่ได้ว่าง แต่ **ฐานที่พอร์ทัลใช้เทียบ กลืนคอมมิตของซองไปแล้ว**
   ⇒ พอร์ทัลเทียบ "ของใหม่" กับ "ของใหม่" แล้วได้ผลต่าง 0 ทุกไฟล์ — ถูกต้องตามตัวหาร
     ของเครื่องมือ แต่ตอบผิดตามคำถามของคนถาม (กับดัก ⑨)

   บทเรียนที่ด่านนี้แปลงเป็นโค้ด:
      "ต่าง 0 ทุกไฟล์" ⛔ ไม่ใช่ข้อสรุปว่าซองว่าง
      มันคือสภาพที่ **ตัดสินไม่ได้** — เพราะแปลได้สองทางที่ตรงข้ามกันสุดขั้ว:
        (ก) ซองว่างจริง   (ข) ฐานที่ประกาศไม่ใช่ฐาน
      ⇒ ด่านที่ตัดสินไม่ได้แล้ว ต้องบอกว่าตัดสินไม่ได้ (รหัส 2)
        ⛔ ไม่ใช่บอกว่าของที่ตรวจผิด (กับดัก ⑨ ครึ่งประโยคหลัง)

   ⇒ ทีมพอร์ทัลขอเองว่าให้ย้ายด่านนี้เป็นตัวแรกของครึ่งหลังรอบ 17
     "เพราะมันเพิ่งกัดวันนี้"

──────────────────────────────────────────────────────────────────────────────
ข้อตกลงรหัสออก (ตามข้อตกลงกลางของคลัง: 0 ผ่าน · 1 เนื้อหาแดง · 2 เครื่องมือแดง)

    0 = ของในซองทุกชิ้น "ต่างจากฐาน" จริง (หรือเป็นไฟล์ใหม่ล้วน) ⇒ ส่งได้
    1 = ซองปนกัน — บางไฟล์เปลี่ยนจริง บางไฟล์เป็นสำเนาไบต์ต่อไบต์ของฐาน
        ⇒ ยังตัดสินได้ว่าผิด: ไฟล์ที่ไม่เปลี่ยนไม่ควรอยู่ในซอง
    2 = ตัดสินไม่ได้ ได้แก่
        · ของในซองเหมือนฐานหมดทุกไฟล์ (ข้อปรับ ๒ — เหตุการณ์เมื่อวานเป๊ะ ๆ)
        · ไม่มีของให้เทียบเลย (ซองมีแต่เอกสารซอง / ซองเปล่า)   ← ตัวหารเป็นศูนย์ (⑨)
        · ไม่ได้ประกาศฐาน / ฐานที่ประกาศไม่มีอยู่จริง
        · เปิดซองไม่ได้ · เรียก git ไม่ได้
        · มีเอกสารซองมากกว่า 1 ใบจนแยกไม่ออกว่าใบไหนคือเอกสาร

⛔ "เทียบไม่ได้" ไม่เท่ากับ "เทียบแล้วผ่าน" — ประโยคเดียวกับที่ขั้นเตรียม BASE_SHA
   ของ guards.yml ใช้อยู่ และเป็นเหตุผลที่ด่านนี้ไม่มีทางคืน 0 โดยไม่ได้เทียบอะไรเลย

──────────────────────────────────────────────────────────────────────────────
ข้อปรับ ๕ ข้อจากสเปก (MB→E #10 §0-②) และตำแหน่งที่ทำจริงในไฟล์นี้

   ข้อปรับ ๑ ต้องประกาศและพิมพ์ SHA ของฐาน · อ่านด้วย `git show <SHA>:<path>` เท่านั้น
             ⛔ ห้ามอ่านจาก working tree
             ⇒ read_base_bytes() · เทสต์ ⑦ พิสูจน์ด้วยการวาง working tree ให้ต่าง
   ข้อปรับ ๒ "ต่าง 0 ทุกไฟล์" ⇒ รหัส 2 ไม่ใช่ 1        ⇒ verdict() สาขา n_changed == 0
   ข้อปรับ ๓ รหัส 1 สงวนให้กรณีที่ยังตัดสินได้จริง      ⇒ verdict() สาขา ซองปนกัน
   ข้อปรับ ๔ พิมพ์สามจำนวน                              ⇒ บรรทัด "เทียบกับฐาน …"
   ข้อปรับ ๕ self-test บังคับ 3 เคส ①②③               ⇒ CASES[0..2] + เทสต์ ⑭ (e2e)

──────────────────────────────────────────────────────────────────────────────
🔴 จุดบอดที่เจอตอนออกแบบ ก่อนเขียนโค้ดบรรทัดแรก — และวิธีปิด

   ซองทุกใบมี `README-ZIP-<เรื่อง>-<วันที่>.md` ซึ่ง **ใหม่เสมอ** ตามนิยาม
   ถ้านับมันเป็น "ไฟล์ใหม่" ⇒ ทุกซองจะมีของใหม่อย่างน้อย 1 ชิ้นเสมอ
   ⇒ ด่านนี้จะเขียวแม้กับซองว่างสนิท = พังในหน้าที่เดียวที่มันมี

   ⇒ กติกา "เอกสารซอง vs สินค้า":
        เอกสารซอง = ไฟล์ชั้นบนสุดที่ชื่อขึ้นต้น README **และไม่มีอยู่ที่ฐาน**
        ถ้าชื่อขึ้นต้น README แต่ **มีอยู่ที่ฐาน** ⇒ เป็นสินค้า (เพราะเป็นการแก้เอกสารจริง)
      · เอกสารซองถูกตัดออกจากตัวหารทั้งหมด ⛔ ไม่นับเป็น "ไฟล์ใหม่ K"
      · มี 2 ใบขึ้นไป ⇒ แยกไม่ออก ⇒ รหัส 2 ⛔ ไม่เดา
      · ทุกครั้งพิมพ์บอกว่าจัดใบไหนเป็นอะไร ⛔ ไม่มีการตัดออกแบบเงียบ ๆ
   (กติกาชื่อ README ยกมาจาก scripts/check_zip_manifest.py ให้ตรงกันทั้งสองด่าน)

การใช้:
    python scripts/check_zip_real_change.py out/ซอง.zip --base <SHA> [--repo .]
    python scripts/check_zip_real_change.py --selftest       # ด่านของตัวด่านเอง
"""
import sys
import os
import io
import zipfile
import argparse
import subprocess
import tempfile
import shutil

CHECKER_VERSION = '1.0'

# ⚠️ ประโยคเขียว — ต้องปรากฏ **เฉพาะ** ในรายงานที่ตัดสินว่าผ่านเท่านั้น
#    เทสต์ ⑮ ("ยามถูกย้ายไปหลังบรรทัดเขียว") บังคับข้อนี้กับทุกเคสที่ไม่เขียว
GREEN_MARK = '✅ ซองนี้มีของเปลี่ยนจริงเทียบกับฐาน'

# จำนวนเคส self-test ที่ตรึงไว้ — ⛔ ลบเคสแล้วต้องแก้เลขนี้ด้วย จึงจะเงียบได้
# (ท่าเดียวกับ N_DECOY_* ใน check_exit_codes.py: ทำให้ "การถอดเทสต์" ต้องมีลายเซ็น)
N_SELFTEST_CASES = 15


# ─────────────────────────────────────────────────────────────
# ชั้นคุยกับ git — ทุกทางที่อ่าน "ฐาน" ต้องผ่านที่นี่
# ─────────────────────────────────────────────────────────────
def _git(repo, *args, binary=False):
    """รัน git ในคลังที่ระบุ · คืน (รหัส, ผลลัพธ์)

    ⛔ ห้ามใช้ shell=True — ชื่อไฟล์ในคลังนี้เป็นภาษาไทยและมีวงเล็บ
    """
    try:
        p = subprocess.run(['git', '-C', repo] + list(args),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (OSError, ValueError) as e:
        return 127, (b'' if binary else f'เรียก git ไม่ได้: {e}')
    return p.returncode, (p.stdout if binary else p.stdout.decode('utf-8', 'replace'))


def resolve_base(repo, sha):
    """คืน SHA เต็มถ้าฐานมีอยู่จริง มิฉะนั้นคืน None (ข้อปรับ ๑)"""
    if not sha:
        return None
    rc, out = _git(repo, 'rev-parse', '--verify', '--quiet', str(sha) + '^{commit}')
    if rc != 0:
        return None
    return out.strip() or None


def base_inventory(repo, sha):
    """รายชื่อไฟล์ทั้งหมด ณ คอมมิตฐาน — อ่านจาก object ⛔ ไม่ใช่ working tree"""
    rc, out = _git(repo, 'ls-tree', '-r', '--name-only', sha)
    if rc != 0:
        return None
    return set(line for line in out.split('\n') if line)


def read_base_bytes(repo, sha, path):
    """เนื้อไฟล์ ณ คอมมิตฐาน เป็นไบต์

    🔴 ข้อปรับ ๑ ทั้งข้ออยู่ในบรรทัดเดียวข้างล่างนี้: `git show <SHA>:<path>`
       ⛔ ห้ามเปลี่ยนเป็น open(os.path.join(repo, path)) ไม่ว่าจะสะดวกแค่ไหน
         เพราะ working tree คือ "ของที่ยังไม่ได้ commit" ซึ่งไม่ใช่ฐานของใครทั้งนั้น
       เทสต์ ⑦ จะแดงทันทีถ้ามีคนเปลี่ยน
    """
    rc, out = _git(repo, 'show', f'{sha}:{path}', binary=True)
    if rc != 0:
        return None
    return out


def last_touch(repo, sha, path):
    """คอมมิตสุดท้าย (ที่หรือก่อนฐาน) ที่แตะไฟล์นี้ — ใช้วินิจฉัยตอนรหัส 2

    🔴 นี่คือบรรทัดที่ถ้ามีเมื่อวาน จะบอกพอร์ทัลได้ทันทีว่า
       "ฐานที่คุณประกาศ กลืนคอมมิตของซองนี้ไปแล้ว"
    """
    rc, out = _git(repo, 'log', '-1', '--format=%h %ad %s', '--date=short',
                   sha, '--', path)
    if rc != 0 or not out.strip():
        return '(หาไม่เจอ)'
    return out.strip()


# ─────────────────────────────────────────────────────────────
# กติกา "เอกสารซอง vs สินค้า"
# ─────────────────────────────────────────────────────────────
def is_readme_name(name):
    """ชื่อไฟล์เข้าข่าย "อาจเป็นเอกสารซอง" ไหม

    เกณฑ์เดียวกับ check_zip_manifest.py: ขึ้นต้น README (ไม่สนตัวพิมพ์)
    และอยู่ **ชั้นบนสุด** ของซอง (ไม่มี '/' ในชื่อ)
    ⛔ ไฟล์ชื่อ README ที่อยู่ในโฟลเดอร์ย่อย = สินค้าที่ส่งเข้าคลัง ไม่ใช่เอกสารซอง
    """
    return name.upper().startswith('README') and '/' not in name


def split_paperwork(entries, base_files):
    """แยก (เอกสารซอง, สินค้า) — คืน (paperwork[], cargo[])"""
    paperwork = [n for n in entries if is_readme_name(n) and n not in base_files]
    cargo = [n for n in entries if n not in paperwork]
    return paperwork, cargo


# ─────────────────────────────────────────────────────────────
# ตัวตัดสิน
# ─────────────────────────────────────────────────────────────
def verdict(n_same, n_changed, n_new):
    """แปลผลนับเป็นรหัสออก + เหตุผล — แยกออกมาให้เทสต์เรียกตรง ๆ ได้

    ข้อปรับ ๒ : เปลี่ยนจริง 0 และไฟล์ใหม่ 0 ⇒ 2 (ไม่ใช่ 1)
    ข้อปรับ ๓ : 1 สงวนให้ "ซองปนกัน" ซึ่งยังตัดสินได้จริง
    """
    if n_changed + n_new == 0:
        return 2, ('ของในซองเหมือนฐานทุกไฟล์ ⇒ ตัดสินไม่ได้'
                   ' — แปลได้ทั้ง "ซองว่าง" และ "ฐานที่ประกาศไม่ใช่ฐาน"')
    if n_same > 0:
        return 1, (f'ซองปนกัน — {n_same} ไฟล์เป็นสำเนาไบต์ต่อไบต์ของฐาน'
                   f' ทั้งที่อีก {n_changed + n_new} ไฟล์เปลี่ยนจริง')
    return 0, 'ของในซองต่างจากฐานครบทุกไฟล์'


def check_zip(zip_src, base_sha, repo, name='(ซอง)'):
    """ตรวจซอง 1 ใบ · คืน (รหัส, บรรทัดรายงาน[])

    ⛔ ฟังก์ชันนี้ **ไม่พิมพ์** อะไรเลย — เพื่อให้ self-test เรียกซ้ำได้
      และเพื่อให้ "ประโยคเขียว" ถูกตรวจได้ว่าโผล่เฉพาะตอนเขียว (เทสต์ ⑮)
    """
    L = [f'── ด่าน "ซองต้องมีของเปลี่ยนจริง" v{CHECKER_VERSION} · {name}']

    # ⑧ ประกาศรุ่น — ด่านที่เทียบรุ่น ต้องบอกว่าเทียบรุ่นไหนกับรุ่นไหน
    rc, _ = _git(repo, 'rev-parse', '--git-dir')
    if rc != 0:
        L.append(f'🔴 เรียก git ในคลัง {repo} ไม่ได้ ⇒ ไม่มีฐานให้เทียบ')
        L.append('   ⛔ "เทียบไม่ได้" ไม่เท่ากับ "เทียบแล้วผ่าน"')
        return 2, L

    full = resolve_base(repo, base_sha)
    if full is None:
        L.append(f'🔴 ฐานที่ประกาศใช้ไม่ได้: {base_sha!r}')
        L.append('   ต้องระบุ --base <SHA> ที่มีอยู่จริงในคลังนี้ (ข้อปรับ ๑)')
        L.append('   ⛔ ด่านนี้ห้ามถอยไปเทียบกับอะไรก็ได้เอง')
        return 2, L

    rc_h, head = _git(repo, 'rev-parse', '--short', 'HEAD')
    L.append(f'⑧ รุ่นที่เทียบ : ฐาน = {full[:12]}  ·  HEAD ของคลังที่ใช้อ่าน = '
             + (head.strip() if rc_h == 0 else '(ไม่มี)'))
    L.append(f'   วิธีอ่านฐาน : git show {full[:12]}:<path>'
             '  ⛔ ไม่แตะ working tree (ข้อปรับ ๑)')

    base_files = base_inventory(repo, full)
    if base_files is None:
        L.append('🔴 อ่านสารบัญของคอมมิตฐานไม่ได้')
        return 2, L

    # ── เปิดซอง ──────────────────────────────────────────────
    try:
        if isinstance(zip_src, (bytes, bytearray)):
            zf = zipfile.ZipFile(io.BytesIO(zip_src))
        else:
            zf = zipfile.ZipFile(zip_src)
    except (zipfile.BadZipFile, OSError) as e:
        L.append(f'🔴 เปิดซองไม่ได้: {e}')
        return 2, L

    with zf:
        entries = [i.filename for i in zf.infolist() if not i.is_dir()]
        # ⑪ ประกาศคลังที่ใช้บังคับ — ตัวหารคือ "รายชื่อในซอง"
        #    ⛔ ไม่ใช่ไฟล์ที่วางอยู่บนดิสก์ และไม่ใช่ไฟล์ที่ถูก commit ไปแล้ว
        L.append(f'⑪ คลังที่ตรวจ : รายชื่อไฟล์ในซองเอง {len(entries)} ไฟล์'
                 ' ⛔ ไม่ใช่ไฟล์บนดิสก์')
        if not entries:
            L.append('🔴 ซองไม่มีไฟล์เลย ⇒ ไม่มีอะไรให้ตัดสิน')
            return 2, L

        paperwork, cargo = split_paperwork(entries, base_files)
        for n in paperwork:
            L.append(f'   📄 เอกสารซอง (ไม่นับเป็นของ) : {n}   — ไม่มีที่ฐาน')
        for n in entries:
            if is_readme_name(n) and n not in paperwork:
                L.append(f'   📦 นับเป็นของ : {n}   — มีอยู่ที่ฐานแล้ว ⇒ ถือเป็นการแก้เอกสารจริง')

        if len(paperwork) >= 2:
            L.append(f'🔴 มีเอกสารซองที่เข้าเกณฑ์ {len(paperwork)} ใบ ⇒ แยกไม่ออกว่าใบไหนคือเอกสาร')
            L.append('   ⛔ ด่านนี้ไม่เดา — ให้เหลือ README ชั้นบนสุดใบเดียวต่อซอง')
            return 2, L

        if not cargo:
            L.append('🔴 ซองมีแต่เอกสาร ไม่มีของ ⇒ ตัวหารเป็นศูนย์ (⑨) ⇒ ตัดสินไม่ได้')
            return 2, L

        same, changed, new = [], [], []
        for path in sorted(cargo):
            if path not in base_files:
                new.append(path)
                continue
            b = read_base_bytes(repo, full, path)
            if b is None:
                L.append(f'🔴 อ่าน {path} ที่ฐานไม่ได้ ทั้งที่มีชื่ออยู่ในสารบัญ')
                return 2, L
            (same if zf.read(path) == b else changed).append(path)

    # ── ข้อปรับ ๔ · สามจำนวน ────────────────────────────────
    n_cmp = len(same) + len(changed)
    L.append(f'เทียบกับฐาน {n_cmp}/{len(cargo)} ไฟล์'
             f' · เปลี่ยนจริง {len(changed)} ไฟล์'
             f' · ไฟล์ใหม่ {len(new)} ไฟล์')

    code, why = verdict(len(same), len(changed), len(new))

    for p in changed:
        L.append(f'   ✏️  เปลี่ยนจริง : {p}')
    for p in new:
        L.append(f'   ➕ ไฟล์ใหม่   : {p}')
    for p in same:
        L.append(f'   ⛔ เหมือนฐานเป๊ะ : {p}')
        L.append(f'      ฐานได้ของชิ้นนี้มาจาก : {last_touch(repo, full, p)}')

    if code == 0:
        L.append(GREEN_MARK + f' ({len(changed)} เปลี่ยน + {len(new)} ใหม่)')
        return 0, L

    if code == 1:
        L.append(f'🔴 {why}')
        L.append('   ⇒ ถอดไฟล์ที่ไม่ได้เปลี่ยนออกจากซอง แล้วสร้างซองใหม่')
        return 1, L

    L.append(f'🟠 {why}')
    L.append('   ตรวจสองทางนี้ก่อนสรุปว่า "ซองว่าง":')
    L.append(f'     ① ฐาน {full[:12]} กลืนคอมมิตของซองนี้ไปแล้วหรือยัง'
             ' — ดูบรรทัด "ฐานได้ของชิ้นนี้มาจาก" ข้างบน')
    L.append('     ② ซองว่างจริง')
    L.append('   ⛔ ด่านนี้จะไม่เลือกให้ — ตัดสินไม่ได้ ต้องบอกว่าตัดสินไม่ได้ (⑨)')
    return 2, L


# ─────────────────────────────────────────────────────────────
# self-test — สร้างคลัง git จริงในโฟลเดอร์ชั่วคราว ⛔ ไม่จำลอง git ด้วยมือ
# (บทเรียน ⑨ จากรอบ 17: ตัวจำลองที่เขียนเองแดง 92/98 แล้วปรากฏว่าตัวจำลองผิด)
# ─────────────────────────────────────────────────────────────
OLD, NEW, OLDX, NEWX, WT = b'OLD\n', b'NEW\n', b'X-OLD\n', b'X-NEW\n', b'WORKTREE\n'
R0, R1 = b'# readme base\n', b'# readme changed\n'


def _mkzip(files):
    """สร้างซองในหน่วยความจำ — คืนไบต์

    ⛔ ใช้ zipfile ของไพทอน ไม่ใช่คำสั่ง zip ของระบบ
      (คำสั่ง zip ไม่ตั้งบิต UTF-8 บนชื่อไฟล์ภาษาไทย ⇒ ด่าน 4 อ่านเป็นตัวยึกยือ)
    """
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, data in files.items():
            z.writestr(name, data)
    return buf.getvalue()


def _commit(repo, msg):
    for a in (['add', '-A'],
              ['-c', 'user.email=t@t', '-c', 'user.name=t',
               '-c', 'commit.gpgsign=false', 'commit', '-q', '-m', msg]):
        rc, out = _git(repo, *a)
        if rc != 0:
            raise RuntimeError(f'git {a[0]} ล้ม: {out}')
    rc, out = _git(repo, 'rev-parse', 'HEAD')
    return out.strip()


def _write(repo, rel, data):
    p = os.path.join(repo, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'wb') as f:
        f.write(data)


def _mkrepo(tmp):
    """คลังทดสอบ 2 คอมมิต + working tree ที่ตั้งใจให้ต่างจากทั้งสอง

    C0 : data/sets/s.json = OLD · viewer/x.js = OLDX · README-BASE.md = R0
    C1 : data/sets/s.json = NEW            (คอมมิตที่ "กลืนซองไปแล้ว")
    WT : data/sets/s.json = WORKTREE       (กับดักของข้อปรับ ๑)
    """
    repo = os.path.join(tmp, 'repo')
    os.makedirs(repo)
    rc, out = _git(repo, 'init', '-q')
    if rc != 0:
        raise RuntimeError(f'git init ล้ม: {out}')
    _write(repo, 'data/sets/s.json', OLD)
    _write(repo, 'viewer/x.js', OLDX)
    _write(repo, 'README-BASE.md', R0)
    c0 = _commit(repo, 'C0')
    _write(repo, 'data/sets/s.json', NEW)
    c1 = _commit(repo, 'C1')
    _write(repo, 'data/sets/s.json', WT)      # ⛔ ค้างไว้ ไม่ commit — โดยตั้งใจ
    return repo, c0, c1


def selftest():
    print(f'== self-test ด่าน "ซองต้องมีของเปลี่ยนจริง" v{CHECKER_VERSION} ==')
    print('   ข้อตกลง: 0 = ซองมีของเปลี่ยนจริง · 1 = ซองปนกัน · 2 = ตัดสินไม่ได้')
    tmp = tempfile.mkdtemp(prefix='zrc-')
    fails = []
    try:
        repo, c0, c1 = _mkrepo(tmp)

        # (ชื่อ, ซอง, ฐาน, รหัสที่ต้องได้, เหตุผลที่เคสนี้มีอยู่)
        cases = [
            ('① ซองที่เปลี่ยนจริง ⇒ 0',
             _mkzip({'data/sets/s.json': NEW, 'README-ZIP-a.md': b'x'}), c0, 0,
             'เคสบังคับข้อ ① ของข้อปรับ ๕'),

            ('② ซองที่ก๊อปไฟล์ฐานมาใส่ปนกับของจริง ⇒ 1',
             _mkzip({'data/sets/s.json': NEW, 'viewer/x.js': OLDX,
                     'README-ZIP-a.md': b'x'}), c0, 1,
             'เคสบังคับข้อ ② · ข้อปรับ ๓ (1 = ยังตัดสินได้)'),

            ('③ ฐาน == ตัวที่ตรวจ (จำลองเหตุการณ์เมื่อวาน) ⇒ 2',
             _mkzip({'data/sets/s.json': NEW, 'README-ZIP-a.md': b'x'}), c1, 2,
             'เคสบังคับข้อ ③ · ข้อปรับ ๒ — ⛔ ห้ามเป็น 1 และห้ามเป็น 0'),

            ('④ ซองมีแต่เอกสาร ⇒ 2',
             _mkzip({'README-ZIP-a.md': b'x'}), c0, 2,
             'ตัวหารเป็นศูนย์ (⑨) ⇒ ตัดสินไม่ได้ ⛔ ไม่ใช่ผ่าน'),

            ('⑤ ของเหมือนฐานหมด แต่ README ใหม่ ⇒ 2 ⛔ ไม่ใช่ 0',
             _mkzip({'data/sets/s.json': OLD, 'viewer/x.js': OLDX,
                     'README-ZIP-a.md': b'x'}), c0, 2,
             'จุดบอดที่เจอตอนออกแบบ — ถ้านับ README เป็น "ไฟล์ใหม่" ทุกซองจะเขียว'),

            ('⑥ ซองที่เป็นไฟล์ใหม่ล้วน ⇒ 0',
             _mkzip({'scripts/brand_new.py': b'n\n', 'README-ZIP-a.md': b'x'}), c0, 0,
             'ของใหม่ก็คือของที่เปลี่ยนจริง'),

            ('⑦ working tree ต่างจากฐาน — คำตัดสินต้องตามฐาน ⇒ 2',
             _mkzip({'data/sets/s.json': OLD, 'README-ZIP-a.md': b'x'}), c0, 2,
             'ข้อปรับ ๑: ถ้าเผลออ่าน working tree (=WORKTREE) จะได้ 0 แทน 2'),

            ('⑧ SHA ที่ไม่มีอยู่จริง ⇒ 2',
             _mkzip({'data/sets/s.json': NEW}), 'deadbeefdeadbeefdeadbeef', 2,
             'ฐานที่ประกาศต้องมีตัวตน'),

            ('⑨ ไม่ประกาศฐานเลย ⇒ 2',
             _mkzip({'data/sets/s.json': NEW}), None, 2,
             '⛔ ไม่มีโหมด "ไม่ต้องบอกฐานก็ได้"'),

            ('⑩ เปิดซองไม่ได้ ⇒ 2',
             b'this is not a zip at all', c0, 2,
             'เครื่องมือแดง ⛔ ไม่ใช่เนื้อหาแดง'),

            ('⑪ เอกสารซอง 2 ใบ ⇒ 2',
             _mkzip({'data/sets/s.json': NEW, 'README-ZIP-a.md': b'x',
                     'README-ZIP-b.md': b'y'}), c0, 2,
             'แยกไม่ออกว่าใบไหนคือเอกสาร ⇒ ไม่เดา'),

            ('⑫ README ที่มีอยู่ที่ฐานแล้วและถูกแก้ ⇒ นับเป็นของ ⇒ 0',
             _mkzip({'README-BASE.md': R1, 'README-ZIP-a.md': b'x'}), c0, 0,
             'ข้อยกเว้นต้องแคบที่สุด — ไม่ใช่ "ชื่อ README แล้วรอดทุกกรณี"'),
        ]

        reports = {}
        for label, zsrc, base, want, why in cases:
            got, lines = check_zip(zsrc, base, repo, name=label)
            reports[label] = '\n'.join(lines)
            ok = (got == want)
            print(f'  {"✅" if ok else "❌"} {label}   (ได้ {got})')
            if not ok:
                fails.append(f'{label}: ต้องได้ {want} แต่ได้ {got} — {why}')
                print('      ' + reports[label].replace('\n', '\n      '))

        # ⑬ ตัวกลายพันธุ์: ทิศทางของคำตัดสินต้องไม่สลับกัน
        for label, zsrc, base, want, why in cases:
            got, _ = check_zip(zsrc, base, repo, name=label)
            if want != 0 and got == 0:
                fails.append(f'⑬ {label} ไม่ควรเขียว แต่เขียว')
            if want == 0 and got == 2:
                fails.append(f'⑬ {label} ควรเขียว แต่บอกว่าตัดสินไม่ได้')
        print('  ✅ ⑬ ทิศทางคำตัดสินไม่สลับ (เคสแดงไม่เขียว · เคสเขียวไม่กลายเป็นตัดสินไม่ได้)')

        # ⑮ ยามถูกย้ายไปหลังบรรทัดเขียว: ประโยคเขียวห้ามโผล่ในรายงานที่ไม่เขียว
        leaked = [lb for (lb, _z, _b, want, _w) in cases
                  if want != 0 and GREEN_MARK in reports[lb]]
        if leaked:
            fails.append('⑮ ประโยคเขียวโผล่ในรายงานที่ไม่เขียว: ' + ', '.join(leaked))
        print('  ✅ ⑮ ประโยคเขียวไม่รั่วเข้ารายงานที่ไม่เขียว')

        # ⑭ e2e: รันเป็นโปรเซสจริง แล้วอ่าน returncode ที่เชลล์เห็น
        #    🔴 กับดัก ⑦ก: ฟังก์ชันคืนรหัสถูก ≠ โปรเซสออกด้วยรหัสนั้น
        me = os.path.abspath(__file__)
        for label, zsrc, base, want in (('①', _mkzip({'data/sets/s.json': NEW,
                                                      'README-ZIP-a.md': b'x'}), c0, 0),
                                        ('②', _mkzip({'data/sets/s.json': NEW,
                                                      'viewer/x.js': OLDX,
                                                      'README-ZIP-a.md': b'x'}), c0, 1),
                                        ('③', _mkzip({'data/sets/s.json': NEW,
                                                      'README-ZIP-a.md': b'x'}), c1, 2)):
            zp = os.path.join(tmp, f'e2e-{label}.zip')
            with open(zp, 'wb') as f:
                f.write(zsrc)
            p = subprocess.run([sys.executable, me, zp, '--base', base, '--repo', repo],
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ok = (p.returncode == want)
            print(f'  {"✅" if ok else "❌"} ⑭ e2e {label} — รหัสที่เชลล์เห็น = {p.returncode}')
            if not ok:
                fails.append(f'⑭ e2e {label}: ต้องได้ {want} แต่โปรเซสออก {p.returncode}')

        # จำนวนเคสต้องตรงกับที่ตรึงไว้ — ถอดเทสต์แล้วต้องมีลายเซ็น
        n_all = len(cases) + 3      # 12 เคสตาราง + ⑬ + ⑭ + ⑮
        if n_all != N_SELFTEST_CASES:
            fails.append(f'จำนวนเคสเป็น {n_all} แต่ N_SELFTEST_CASES = {N_SELFTEST_CASES}'
                         ' ⇒ มีคนเพิ่ม/ลบเทสต์โดยไม่ประกาศ')
    except Exception as e:                       # noqa: BLE001
        fails.append(f'self-test พังระหว่างเตรียมของ: {type(e).__name__}: {e}')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if fails:
        print('🔴 self-test ล้ม:')
        for f in fails:
            print('   · ' + f)
        return 2
    print(f'✅ self-test ผ่านครบ {N_SELFTEST_CASES} เคส')
    return 0


def main():
    ap = argparse.ArgumentParser(
        description='ด่าน "ซองต้องมีของเปลี่ยนจริง" — ซองต้องไม่ใช่สำเนาของฐาน')
    ap.add_argument('zip', nargs='?', help='ไฟล์ซอง .zip ที่จะส่ง')
    ap.add_argument('--base', help='SHA ของคอมมิตฐาน (บังคับ · ข้อปรับ ๑)')
    ap.add_argument('--repo', default=os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), help='คลัง git ที่ใช้อ่านฐาน')
    ap.add_argument('--selftest', action='store_true', help='ตรวจตัวด่านเอง')
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    if not a.zip:
        print('🔴 ไม่ได้ระบุซอง — ใช้: check_zip_real_change.py <ซอง.zip> --base <SHA>')
        print('   ⛔ "ไม่มีอะไรให้ตรวจ" ไม่เท่ากับ "ตรวจแล้วผ่าน"')
        return 2

    code, lines = check_zip(a.zip, a.base, a.repo, name=os.path.basename(a.zip))
    for line in lines:
        print(line)
    return code


if __name__ == '__main__':
    sys.exit(main())

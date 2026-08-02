#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ด่าน 11 · รหัสออกต้องแปลว่าอย่างที่ตกลงกันไว้ — และต้องมีคนอ่านมันจริง

ข้อตกลงที่ด่านนี้เฝ้า (ใช้ทั้งคลัง):
    0 = ผ่าน  ·  1 = เนื้อหาแดง  ·  2 = ตัวเครื่องมือแดง / เทียบไม่ได้

🔴 ทำไมต้องมีด่านสำหรับเรื่องนี้ (กับดัก ⑦ก · ⑦ข ในรูปของ CI):
   ตัวตรวจที่ "คืนรหัสถูกต้อง" กับตัวตรวจที่ "มีคนอ่านรหัสนั้น" ⛔ ไม่ใช่เรื่องเดียวกัน
   ระหว่างสองอย่างนี้มีที่ให้ของหายได้อย่างน้อย 4 ทาง และทุกทาง **หน้าตาเหมือนเขียว**:

     ① เขียน exit 3 (หรือเลขอะไรก็ได้) — CI เห็นว่า "ไม่ใช่ 0" ก็จริง
        แต่คนอ่าน log จะแยกไม่ออกว่า "เนื้อหาผิด" หรือ "เครื่องมือพัง"
        ⇒ สองอย่างนี้ต้องทำคนละอย่างกัน (อันแรกแก้ข้อ อันหลังแก้สคริปต์)
     ② `python x.py || true` — รหัสถูกกลืน ด่านกลายเป็น "รันแล้วพิมพ์อะไรบางอย่าง"
     ③ `continue-on-error: true` — เขียวทั้งที่ด่านแดง
     ④ `python x.py | tail -5` — รหัสที่ CI อ่านคือรหัสของ tail (ซึ่งคือ 0 เสมอ)

   ทั้งสี่ทางนี้ ⛔ ไม่มีทางไหนที่ "เห็นได้จากการอ่านผลรัน" — ต้องอ่านจากไฟล์เท่านั้น
   ⇒ จึงต้องเป็นด่าน ไม่ใช่กติกาในจดหมาย

🔴 ด่านนี้ตรวจตัวเองด้วย (ไฟล์นี้อยู่ใน scripts/ ⇒ เข้าข่ายกฎเดียวกันทุกข้อ)
   และมีด่านย่อยยืนยันเรื่องนั้นตรง ๆ — ⛔ ไม่ใช่ "เชื่อเพราะมันควรจะเป็นอย่างนั้น"

🔴 ตัวล่อถาวร (DECOYS) — และเหตุผลที่ต้องนับ:
   ด่านที่ไม่มีของให้จับ จะเขียวเหมือนกับด่านที่จับของได้ครบ (กับดัก ⑨)
   ⇒ เก็บตัวอย่าง "ของผิดที่ต้องจับให้ได้" ไว้ในไฟล์นี้ถาวร แล้ว **ยืนยันจำนวน**
     ถ้าวันหนึ่งมีคนลบตัวล่อทิ้งเพื่อให้ด่านเงียบ จำนวนจะไม่ตรง ⇒ แดงทันที

รหัสออก: 0 = ผ่าน · 1 = เนื้อหาแดง · 2 = ตัวเครื่องมือแดง
"""
import argparse
import ast
import os
import re
import sys

CHECKER_VERSION = '1.2'

# ── v1.2 (2 ส.ค. 69) — ปิดรูที่ "ภาษาของไฟล์" กลายเป็นทางหนีของกฎ ────────────
#
# 🔴 ที่มา: รอบ 17 เพิ่มตัวตรวจตัวแรกที่ ⛔ ไม่ใช่ไพทอน — scripts/check_export_figures.js
#    (ต้องเป็น JS เพราะของที่ถูกตรวจคือ viewer/export.js ซึ่งรันในเบราว์เซอร์)
#    รุ่น 1.1 อ่านเฉพาะไฟล์ที่ลงท้าย .py ⇒ ตัวตรวจ JS จะ:
#      · ไม่ถูกกฎ ⑦ก เฝ้าเลย (ลืมผูกเข้า CI = เขียวตลอดกาล)
#      · เขียน process.exit(3) ได้โดยไม่มีใครทัก
#    ⇒ รูนี้เกิดจากการที่ "ผมเองเป็นคนเพิ่มไฟล์ JS ตัวแรก" ⛔ ไม่ใช่ของเก่าที่ค้างมา
#      การรายงานรูที่ตัวเองเพิ่งเจาะ แล้วไม่อุด = สร้างหนี้ในรอบเดียวกับที่ประกาศว่าใช้หนี้
#
# ⚠️ ขอบเขตที่ทำได้จริง และตัวหารของมัน (⑨ — ประกาศไว้ ไม่ปล่อยให้ความเงียบแปลว่าครอบคลุม):
#    ฝั่ง .py  อ่านด้วย ast ⇒ เห็นโครงสร้าง (return จาก main() ก็จับได้)
#    ฝั่ง .js  ⛔ ไม่มี parser ⇒ อ่านด้วย regex เห็นเฉพาะ `process.exit(<เลขตายตัว>)`
#      สิ่งที่ฝั่ง JS ยัง ⛔ จับไม่ได้: `process.exitCode = 3` · `exit(x)` ที่ x เป็นตัวแปร ·
#      รหัสที่ throw ออกไปแล้ว node แปลงเป็น 1
#      ⇒ พิมพ์ตัวหารของสองฝั่งแยกกันเสมอ ⛔ ห้ามรวมเป็นเลขเดียว
#        เพราะ "ตรวจ .js ได้ 3 จุด" กับ "ตรวจ .py ได้ 80 จุด" ไม่ใช่หลักฐานชนิดเดียวกัน
# ─────────────────────────────────────────────────────────────────────────────

OK_CODES = (0, 1, 2)
SCRIPTS_DIR = 'scripts'
WORKFLOW = '.github/workflows/guards.yml'

# ฟังก์ชันที่ "ค่าคืน" ของมันกลายเป็นรหัสออกจริง ๆ
EXIT_FUNCS = ('main', 'selftest')

# ── รูปแบบการกลืนรหัสในไฟล์ workflow ──────────────────────────
# ⚠️ ทุกตัวที่นี่คือของที่ "ใช้ถูกก็มี" — แต่ในไฟล์ด่าน มันไม่มีเหตุผลที่ถูกเลย
#    ⇒ ถ้าวันหนึ่งมีเหตุผลจริง ให้เขียนเหตุผลไว้ท้ายบรรทัดด้วยคำว่า ยอมรับรหัส
SWALLOW = [
    (r'\|\|\s*true\b', '`|| true` กลืนรหัสออก ⇒ ด่านนี้เขียวเสมอไม่ว่าจะเกิดอะไร'),
    (r'\|\|\s*:\s*$', '`|| :` กลืนรหัสออก (เขียนสั้นกว่า || true แต่ผลเหมือนกัน)'),
    (r'continue-on-error:\s*true', 'continue-on-error: true ⇒ ด่านแดงแล้วงานยังเขียว'),
    (r'set\s+\+e\b', '`set +e` ปิดการหยุดเมื่อคำสั่งล้ม ⇒ บรรทัดถัดไปรันต่อทั้งที่ด่านแดง'),
    (r'exit\s+0\s*(?:#.*)?$', '`exit 0` ตรง ๆ ในบล็อกด่าน ⇒ ประกาศว่าผ่านโดยไม่ได้ตรวจ'),
]
ALLOW_MARK = 'ยอมรับรหัส'      # คำกำกับที่ยอมให้ผ่านได้ — ต้องเขียนด้วยมือ

# ── ตัวตรวจที่ "ตั้งใจ" ไม่ให้ CI เรียก — ต้องประกาศพร้อมเหตุผล ────────
#
# 🔴 ที่มา: ด่าน 11 (⑦ก) ตั้งกฎว่า "ตัวตรวจที่ไม่มีใครเรียก = ตัวตรวจที่ไม่มีอยู่จริง"
#    แล้ววันเดียวกันนั้นเองก็เจอของที่ขัดกฎโดยชอบธรรม: ด่านความสด
#    ซึ่งมติร่วมกับพอร์ทัลระบุชัดว่า ⛔ ห้ามผูกเข้า guards.yml (ฝั่ง sync เท่านั้น)
#    ⇒ ทางเลือกมีสามทาง และสองทางแรกแย่:
#       ① ตั้งชื่อเลี่ยงไม่ให้ขึ้นต้นด้วย check_  ⇒ ปิดด่านด้วยการตั้งชื่อ (แย่ที่สุด)
#       ② ถอดกฎ ⑦ก ทิ้ง                          ⇒ เสียด่านทั้งด่านเพราะข้อยกเว้นเดียว
#       ③ ให้ยกเว้นได้ แต่ "ต้องพิมพ์เหตุผล"      ⇒ เลือกทางนี้
#    เหตุผลของทาง ③: มันเปลี่ยน "ความเงียบ" ให้เป็น "ข้อความที่มีคนเขียน"
#    และรายการนี้ถูก ด่าน 10 เฝ้าไว้ ⇒ โตขึ้นเมื่อไรต้องประกาศในข้อความ commit
#
# ⚠️ ⛔ ห้ามใส่ตัวตรวจที่ *ควร* อยู่ใน CI แต่ยังไม่ได้ผูก ลงในรายการนี้
#    "ยังไม่ได้ผูก" ⇒ ให้ด่านแดงต่อไปจนกว่าจะผูก · ที่นี่มีไว้ให้เฉพาะของที่
#    ตั้งใจไม่ผูกอย่างถาวร และมีมติรองรับ
NOT_IN_CI = {
    'check_bank_freshness.py':
        'ด่านความสด — ใช้ฝั่ง sync ของพอร์ทัลเท่านั้น'
        ' · มติร่วม 1 ส.ค. 69: ⛔ ห้ามมีด่านฝั่ง push และ ⛔ ห้ามมีโหมดเตือนเฉย ๆ ฝั่ง push'
        ' (เพราะคนที่ push ไม่ใช่คนที่เสิร์ฟ bank.json ให้เด็ก)',
}
MIN_NOT_IN_CI_REASON = 20


def check_not_in_ci(table=None):
    """รายการยกเว้น ⑦ก ต้องมีเหตุผลจริง — คืน (ผ่านไหม, ปัญหา[])

    ⛔ เหตุผลว่าง/สั้น = การปิดด่านที่หน้าตาเหมือนการประกาศ
    """
    t = NOT_IN_CI if table is None else table
    bad = []
    if not isinstance(t, dict):
        return False, ['NOT_IN_CI ต้องเป็น dict {ชื่อไฟล์: เหตุผล} — ถ้าเป็น list เหตุผลจะหายทั้งรายการ']
    for k, v in t.items():
        if not isinstance(v, str) or len(v.strip()) < MIN_NOT_IN_CI_REASON:
            bad.append(f'{k}: เหตุผลสั้นกว่า {MIN_NOT_IN_CI_REASON} ตัวอักษร หรือไม่ใช่ข้อความ')
    return not bad, bad

# บรรทัดที่เอาผลของ python ไปต่อท่อ แล้วรหัสที่เหลือคือรหัสของตัวขวา
PIPE_RE = re.compile(r'python[0-9.]*\s+\S*scripts/\S+\.py[^|\n]*\|(?!\|)')
PIPE_SAFE = ('pipefail', 'PIPESTATUS')


def _int_literal(node):
    """คืนค่าจำนวนเต็มถ้า node เป็น "เลขตายตัว" มิฉะนั้นคืน None

    🔴 ทำไมต้องมีฟังก์ชันนี้แทนที่จะเช็ค ast.Constant ตรง ๆ:
       `sys.exit(-1)` ⛔ ไม่ใช่ Constant — ไพทอนอ่านเป็น UnaryOp(USub, Constant(1))
       ⇒ ด่านรุ่นแรกของผมปล่อย exit(-1) ผ่านหน้าไปเฉย ๆ (ด่านตัวเองจับได้)
       และ -1 คือรหัสที่อันตรายที่สุดในกลุ่มนี้ เพราะเชลล์เห็นเป็น 255
       ⇒ "ไม่ใช่ 0/1/2" แต่ก็ไม่ตรงกับเลขที่เราเขียนไว้ในโค้ดด้วย
    ⛔ ยังคงไม่จับ sys.exit(main()) หรือ sys.exit(f(x)) — ไม่ใช่เลขตายตัว
       (ตัดสินไม่ได้จากการอ่านไฟล์ ⇒ ไม่เดา)
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, int) \
            and not isinstance(node.value, bool):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        inner = _int_literal(node.operand)
        if inner is None:
            return None
        return -inner if isinstance(node.op, ast.USub) else inner
    return None


def exit_codes_py(src, where='<mem>'):
    """คืน [(บรรทัด, รหัส, ที่มา)] ของรหัสออกที่เป็นเลขตายตัวในซอร์สไพทอน"""
    out = []
    tree = ast.parse(src, filename=where)
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == 'exit' and node.args):
            v = _int_literal(node.args[0])
            if v is not None:
                out.append((node.lineno, v, 'sys.exit'))
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                and node.name in EXIT_FUNCS:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Return):
                    v = _int_literal(sub.value)
                    if v is not None:
                        out.append((sub.lineno, v, f'return จาก {node.name}()'))
    return sorted(out)


# ── ฝั่ง JavaScript ──────────────────────────────────────────────────────────
# ⚠️ อ่านด้วย regex ⛔ ไม่ใช่ parser — ดูเหตุผลและตัวหารในหัวไฟล์ (v1.2)
JS_EXIT_RE = re.compile(r'process\s*\.\s*exit\s*\(\s*(-?\d+)\s*\)')


def strip_js_comments(src):
    """ตัดคอมเมนต์ JS ทิ้ง โดยเก็บจำนวนบรรทัดไว้เท่าเดิม

    🔴 ทำไมต้องตัด: ไฟล์ด่านจะมีบรรทัดที่ *อธิบาย* กฎ เช่น
       `// ⛔ ห้ามเขียน process.exit(3)` — ถ้าไม่ตัด ด่านจะจับเอกสารของตัวเอง
       ⇒ ด่านที่ทำให้เขียนเอกสารไม่ได้ คือด่านที่จะโดนถอดทิ้ง (เหตุผลเดียวกับ strip_comment)
    ⛔ แต่ห้ามตัดดื้อ ๆ: `'ข้อความ // ไม่ใช่คอมเมนต์'` ต้องรอด และที่สำคัญกว่านั้น
       `console.log('ก') // ...` ⇒ ของจริงที่อยู่ *ก่อน* // ต้องไม่หายไปด้วย
    ⛔ เก็บ '\\n' ไว้ทุกตัว เพราะเลขบรรทัดที่รายงานต้องตรงกับไฟล์จริง
       (ด่านที่ชี้บรรทัดผิด = ด่านที่คนอ่านแล้วไม่เชื่อ แล้วก็เลิกอ่าน)
    """
    out, i, n = [], 0, len(src)
    q = None          # เครื่องหมายคำพูดที่กำลังเปิดค้างอยู่ (' " `)
    while i < n:
        ch = src[i]
        if q:
            if ch == '\\' and i + 1 < n:
                out.append(ch); out.append(src[i + 1]); i += 2; continue
            if ch == q:
                q = None
            out.append(ch); i += 1; continue
        if ch in '"\'`':
            q = ch; out.append(ch); i += 1; continue
        if ch == '/' and i + 1 < n and src[i + 1] == '/':
            while i < n and src[i] != '\n':
                i += 1
            continue
        if ch == '/' and i + 1 < n and src[i + 1] == '*':
            i += 2
            while i + 1 < n and not (src[i] == '*' and src[i + 1] == '/'):
                if src[i] == '\n':
                    out.append('\n')   # ⛔ เลขบรรทัดต้องไม่เลื่อน
                i += 1
            i += 2
            continue
        out.append(ch); i += 1
    return ''.join(out)


def exit_codes_js(src, where='<mem>'):
    """คืน [(บรรทัด, รหัส, ที่มา)] ของ process.exit(<เลขตายตัว>) ในซอร์ส JS"""
    code = strip_js_comments(src)
    out = []
    for m in JS_EXIT_RE.finditer(code):
        ln = code.count('\n', 0, m.start()) + 1
        out.append((ln, int(m.group(1)), 'process.exit'))
    return sorted(out)


def strip_comment(line):
    """ตัดคอมเมนต์ท้ายบรรทัดออก โดยรู้จักเครื่องหมายคำพูด

    🔴 ทำไมต้องมี (เจอจริงตอนต่อด่าน 11 เข้า guards.yml):
       คอมเมนต์ที่ "อธิบายกฎ" จะมีคำต้องห้ามอยู่ในตัวมันเองเสมอ —
       บรรทัดที่เขียนว่า `# ห้ามใช้ || true` โดนด่านจับ 🔴 ทั้งที่มันคือเอกสาร
       ⇒ ด่านที่ทำให้เขียนเอกสารของตัวเองไม่ได้ คือด่านที่จะโดนถอดทิ้ง
    ⛔ แต่ห้ามใช้ line.split('#')[0] ดื้อ ๆ:
       `echo "ก # ข" || true` จะถูกตัดจนคำว่า || true หายไป ⇒ ของจริงหลุด
       ⇒ ตัดที่ # ตัวแรกที่อยู่ "นอกเครื่องหมายคำพูด" และมีช่องว่าง/ต้นบรรทัดนำหน้า
    """
    q = None
    for i, ch in enumerate(line):
        if q:
            if ch == q:
                q = None
        elif ch in '"\'':
            q = ch
        elif ch == '#' and (i == 0 or line[i - 1].isspace()):
            return line[:i]
    return line


def exit_codes_yaml(text):
    """คืน [(บรรทัด, รหัส)] ของ `exit N` ในบล็อกเชลล์ของไฟล์ workflow"""
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        # -?\d+ ⛔ ไม่ใช่ \d+ — `exit -1` ในเชลล์ก็เกิดได้ และเชลล์เห็นเป็น 255
        m = re.search(r'(?<![\w-])exit\s+(-?\d+)\s*$', strip_comment(line).rstrip())
        if m:
            out.append((i, int(m.group(1))))
    return out


def swallowed(text):
    """คืน [(บรรทัด, ข้อความ, เหตุผล)] ของบรรทัดที่กลืนรหัสออก"""
    out = []
    for i, raw in enumerate(text.splitlines(), 1):
        if ALLOW_MARK in raw:
            continue          # มีคนเขียนเหตุผลกำกับด้วยมือ ⇒ ปล่อย (แต่ยังเห็นใน diff)
        line = strip_comment(raw)     # คอมเมนต์ที่อธิบายกฎ ⛔ ไม่ใช่การละเมิดกฎ
        for pat, why in SWALLOW:
            if re.search(pat, line):
                out.append((i, raw.strip(), why))
                break
        else:
            if PIPE_RE.search(line) and not any(k in text for k in PIPE_SAFE):
                out.append((i, raw.strip(),
                            'ต่อท่อจากตัวตรวจ ⇒ รหัสที่ CI อ่านคือรหัสของคำสั่งขวาสุด'
                            ' (แก้ด้วย set -o pipefail หรืออ่าน ${PIPESTATUS[0]})'))
    return out


def called_in_workflow(text, script_path):
    """ตัวตรวจตัวนี้ถูกเรียกในไฟล์ workflow หรือยัง — ⑦ก: คืนรหัสแล้ว ≠ มีคนอ่านรหัส"""
    return os.path.basename(script_path) in text


# ⚠️ นามสกุลที่ถือว่า "เป็นตัวตรวจได้" — v1.2 เพิ่ม .js
#    ⛔ ห้ามตัด .js ออกเพื่อให้ด่านเงียบ: ตัดเมื่อไร ตัวตรวจ JS จะหลุดจากกฎ ⑦ก ทันที
CHECKER_EXTS = ('.py', '.js')


def is_checker(fn):
    """ไฟล์นี้เข้าข่าย "ตัวตรวจที่ต้องมีคนเรียก" ไหม (กฎ ⑦ก)

    🔴 เกณฑ์คือ **คำนำหน้า check_ + นามสกุลในรายการ** ⛔ ไม่ใช่ภาษาที่เขียน
       ถ้าผูกกับภาษา ตัวตรวจภาษาใหม่จะหลุดออกจากกฎเงียบ ๆ ทุกครั้งที่เพิ่มภาษา
       (เกิดจริงในรอบ 17 — ตัวตรวจ JS ตัวแรกไม่มีใครเฝ้าเลย)
    """
    return fn.startswith('check_') and fn.endswith(CHECKER_EXTS)


# ─────────────────────────────────────────────────────────────
# ตัวล่อถาวร — ⛔ ห้ามลบ · จำนวนถูกยืนยันด้านล่าง
# ─────────────────────────────────────────────────────────────
DECOY_PY = [
    ('รหัส 3 ที่ไม่มีในข้อตกลง', 'import sys\nsys.exit(3)\n'),
    ('รหัส -1 (เชลล์จะเห็นเป็น 255)', 'import sys\nsys.exit(-1)\n'),
    ('รหัส 5 ซ่อนในเงื่อนไข', 'import sys\nif x:\n    sys.exit(5)\n'),
    ('return 3 จาก main() — กลายเป็นรหัสออกเหมือนกัน',
     'def main():\n    return 3\n'),
    ('return 7 จาก selftest()', 'def selftest():\n    return 7\n'),
]

DECOY_YML = [
    ('|| true', 'run: python scripts/x.py || true'),
    ('|| :', 'run: python scripts/x.py || :'),
    ('continue-on-error', '    continue-on-error: true'),
    ('set +e', '          set +e'),
    ('exit 0 ตรง ๆ', '          exit 0'),
    ('ต่อท่อจนรหัสหาย', '          python scripts/scan_symbols.py data/sets | tail -5'),
    # 🔴 คู่แฝดของตัวสะอาด "คอมเมนต์อธิบายกฎ" ข้างล่าง — ต้องมาเป็นคู่เสมอ
    #    ถ้ามีแต่ตัวสะอาด คนแก้จะ "ตัดที่ # ตัวแรก" แล้วด่านเงียบทั้งที่ของจริงหลุด
    ('# อยู่ในเครื่องหมายคำพูด ⇒ ยังต้องจับ || true ที่อยู่ข้างหลัง',
     '          echo "ก # ข" || true'),
]

DECOY_YML_EXIT = [
    ('exit 3 ในบล็อกเชลล์', '          exit 3', 3),
    ('exit 9 ในบล็อกเชลล์', '          exit 9', 9),
    ('exit -1 ในบล็อกเชลล์ (เชลล์เห็นเป็น 255)', '          exit -1', -1),
]

# 🔴 จำนวนตัวล่อ — ⛔ ห้ามแก้เพื่อให้ด่านเงียบ
#    ลบตัวล่อ 1 ตัวแล้วลดเลขนี้ตาม = การปิดด่านแบบที่มองไม่เห็นใน log
#    ⇒ เลขนี้ต้องขยับพร้อม "เหตุผลในข้อความ commit" เท่านั้น
N_DECOY_PY, N_DECOY_YML, N_DECOY_YML_EXIT = 5, 7, 3

# ของที่ต้อง "ไม่จับ" — กันด่านดุเกินจนคนปิดทิ้ง
DECOY_CLEAN_PY = [
    ('sys.exit(main()) — ไม่ใช่เลขตายตัว ⇒ ตัดสินไม่ได้ ⇒ ต้องไม่จับ',
     'import sys\ndef main():\n    return 0\nsys.exit(main())\n'),
    ('return 3 จากฟังก์ชันธรรมดา ⇒ ไม่ใช่รหัสออก ⇒ ต้องไม่จับ',
     'def helper():\n    return 3\n'),
    ('รหัส 0/1/2 ครบชุด ⇒ ต้องเงียบ',
     'import sys\nsys.exit(0)\nsys.exit(1)\nsys.exit(2)\n'),
]
DECOY_CLEAN_YML = [
    ('บรรทัดปกติ', '          python scripts/scan_symbols.py data/sets'),
    ('exit 1 / exit 2 ⇒ ถูกต้องตามข้อตกลง', '          exit 1\n          exit 2'),
    (f'กลืนรหัสแต่เขียนเหตุผลกำกับ ({ALLOW_MARK}) ⇒ ปล่อยได้',
     f'          python scripts/x.py || true   # {ALLOW_MARK}: ขั้นเก็บ log อย่างเดียว'),
    # 🔴 ตัวสะอาดสองตัวล่างนี้มาจากของจริง: ตอนเขียนคอมเมนต์อธิบายด่าน 11
    #    ลงใน guards.yml ด่านจับคอมเมนต์ของตัวเองแดง 3 จุด
    #    ⇒ ด่านที่ห้ามเขียนเอกสารของตัวเอง คือด่านที่จะโดนถอดทิ้งในที่สุด
    ('คอมเมนต์ที่ "อธิบาย" ท่ากลืนรหัส ⛔ ไม่ใช่การใช้ท่านั้น',
     '      #      ท่าที่ห้าม — `|| true` · `|| :` · `set +e` · `continue-on-error`'),
    ('คอมเมนต์ที่เขียนเลขรหัสไว้อธิบาย ⇒ ต้องไม่นับเป็นรหัสออกจริง',
     '      # ถ้าเจอแบบนี้ให้ออก exit 3 (ตัวอย่างในเอกสาร ไม่ใช่โค้ด)'),
]
N_CLEAN_PY, N_CLEAN_YML = 3, 5

# ── ตัวล่อฝั่ง JS (v1.2) ─────────────────────────────────────────────────────
DECOY_JS = [
    ('process.exit(3)', "process.exit(3);\n"),
    ('process.exit(-1) — เชลล์เห็นเป็น 255', "process.exit(-1);\n"),
    ('process.exit( 5 ) เว้นวรรคแทรก', "process.exit( 5 );\n"),
    ('process . exit(4) เว้นวรรครอบจุด', "process . exit(4);\n"),
    ('รหัสแปลกซ่อนใต้เงื่อนไข', "if (bad) { process.exit(9); }\n"),
]
DECOY_CLEAN_JS = [
    ('รหัส 0/1/2 ครบชุด ⇒ ต้องเงียบ',
     "process.exit(0);\nprocess.exit(1);\nprocess.exit(2);\n"),
    # 🔴 คู่แฝดของ DECOY_CLEAN_YML สองตัวล่าง — ด่านต้องอ่านเอกสารของตัวเองได้
    ('คอมเมนต์บรรทัดเดียวที่ "อธิบาย" รหัสแปลก ⛔ ไม่ใช่การใช้',
     "// ⛔ ห้ามเขียน process.exit(3) — ใช้ 1 หรือ 2 เท่านั้น\n"),
    ('คอมเมนต์บล็อกที่อธิบายรหัสแปลก',
     "/* ตัวอย่างที่ห้าม:\n *   process.exit(7)\n */\n"),
    ('ข้อความในเครื่องหมายคำพูดที่มี // อยู่ ⇒ ต้องไม่ถูกตัดจนของจริงหาย',
     "const u = 'http://x/y'; process.exit(1);\n"),
    ('exit ที่ส่งตัวแปร ⇒ ตัดสินไม่ได้ ⇒ ต้องไม่จับ (และประกาศไว้ในหัวไฟล์แล้ว)',
     "process.exit(RED ? 1 : 0);\n"),
]
N_DECOY_JS, N_CLEAN_JS = 5, 5


def selftest():
    print('─' * 62)
    print(f'SELF-TEST ด่าน 11 v{CHECKER_VERSION} — ความหมายของรหัสออก')
    print('─' * 62)
    print(f'  ข้อตกลง: {" · ".join(f"{c}" for c in OK_CODES)}'
          '  ⇒  0 ผ่าน · 1 เนื้อหาแดง · 2 เครื่องมือแดง')
    ok = True

    # ── ⑨ ยืนยันจำนวนตัวล่อก่อน แล้วค่อยเดินด่าน ──────────────
    counts = [
        ('ตัวล่อไพทอน', len(DECOY_PY), N_DECOY_PY),
        ('ตัวล่อ workflow (กลืนรหัส)', len(DECOY_YML), N_DECOY_YML),
        ('ตัวล่อ workflow (รหัสแปลก)', len(DECOY_YML_EXIT), N_DECOY_YML_EXIT),
        ('ตัวล่อ JS', len(DECOY_JS), N_DECOY_JS),
        ('ตัวสะอาดไพทอน', len(DECOY_CLEAN_PY), N_CLEAN_PY),
        ('ตัวสะอาด workflow', len(DECOY_CLEAN_YML), N_CLEAN_YML),
        ('ตัวสะอาด JS', len(DECOY_CLEAN_JS), N_CLEAN_JS),
    ]
    print()
    print('  ── ยืนยันจำนวนตัวล่อ (⛔ ลบตัวล่อ = ปิดด่านแบบเงียบ) ──')
    for name, got, want in counts:
        good = got == want
        print(f'  {"✅" if good else "🔴"}  {name} {got}/{want}')
        ok &= good
    if not ok:
        print('\n🔴 จำนวนตัวล่อไม่ตรง ⇒ ด่านข้างล่างเชื่อไม่ได้ (อาจเขียวเพราะไม่มีของให้จับ)')
        return 2

    print()
    print('  ── ตัวล่อต้องถูกจับได้ทุกตัว ──')
    for name, src in DECOY_PY:
        bad = [c for _, c, _ in exit_codes_py(src) if c not in OK_CODES]
        print(f'  {"✅" if bad else "🔴 ไม่จับ"}  {name}')
        ok &= bool(bad)
    for name, line in DECOY_YML:
        hit = swallowed(line)
        print(f'  {"✅" if hit else "🔴 ไม่จับ"}  {name}')
        ok &= bool(hit)
    for name, line, want in DECOY_YML_EXIT:
        hit = [c for _, c in exit_codes_yaml(line) if c not in OK_CODES]
        print(f'  {"✅" if hit == [want] else "🔴 ไม่จับ"}  {name}')
        ok &= hit == [want]
    for name, src in DECOY_JS:
        bad = [c for _, c, _ in exit_codes_js(src) if c not in OK_CODES]
        print(f'  {"✅" if bad else "🔴 ไม่จับ"}  [JS] {name}')
        ok &= bool(bad)

    print()
    print('  ── ของสะอาดต้องไม่ถูกจับ (กันด่านดุเกินจนมีคนปิดทิ้ง) ──')
    for name, src in DECOY_CLEAN_PY:
        bad = [c for _, c, _ in exit_codes_py(src) if c not in OK_CODES]
        print(f'  {"✅" if not bad else "🔴 จับเกิน: " + str(bad)}  (ต้องไม่จับ) {name}')
        ok &= not bad
    for name, line in DECOY_CLEAN_YML:
        hit = swallowed(line) + [x for x in exit_codes_yaml(line) if x[1] not in OK_CODES]
        print(f'  {"✅" if not hit else "🔴 จับเกิน: " + str(hit)}  (ต้องไม่จับ) {name}')
        ok &= not hit
    for name, src in DECOY_CLEAN_JS:
        bad = [c for _, c, _ in exit_codes_js(src) if c not in OK_CODES]
        print(f'  {"✅" if not bad else "🔴 จับเกิน: " + str(bad)}  (ต้องไม่จับ) [JS] {name}')
        ok &= not bad

    print()
    print('  ── ด่านนี้ตรวจตัวเองด้วยไหม ──')
    me = os.path.join(SCRIPTS_DIR, os.path.basename(__file__))
    self_checks = [
        (f'ไฟล์ของด่านนี้อยู่ใน {SCRIPTS_DIR}/ ⇒ เข้าข่ายกฎเดียวกับที่มันบังคับคนอื่น',
         os.path.basename(__file__).startswith('check_')),
        ('รหัสออกของด่านนี้เอง อยู่ในข้อตกลงครบทุกจุด',
         all(c in OK_CODES for _, c, _ in
             exit_codes_py(open(__file__, encoding='utf-8').read(), __file__))),
        ('ตัวล่อทั้งหมดเป็น "ข้อความ" ⛔ ไม่ใช่โค้ดที่รันจริง (ไม่งั้นด่านนี้จะออกเอง)',
         all(isinstance(s, str) for _, s in DECOY_PY)),
        # ── รายการยกเว้น ⑦ก ──
        ('รายการยกเว้นจริงผ่านด่านเหตุผล', check_not_in_ci()[0] is True),
        ('ยกเว้นโดยไม่เขียนเหตุผล ⇒ ต้องล้ม',
         check_not_in_ci({'x.py': ''})[0] is False),
        (f'เหตุผลสั้นกว่า {MIN_NOT_IN_CI_REASON} ตัวอักษร ⇒ ต้องล้ม',
         check_not_in_ci({'x.py': 'สั้นไป'})[0] is False),
        ('…และต้องบอกด้วยว่าไฟล์ไหนที่ผิด (ไม่ใช่แค่ "ล้ม")',
         'x.py' in ' '.join(check_not_in_ci({'x.py': ''})[1])),
        ('ถ้ามีคนเปลี่ยน NOT_IN_CI เป็น list ⇒ ต้องล้ม (เหตุผลจะหายทั้งรายการ)',
         check_not_in_ci(['check_bank_freshness.py'])[0] is False),
        ('⛔ ยกเว้นได้เฉพาะไฟล์ที่ขึ้นต้นด้วย check_ (ไฟล์อื่นไม่เคยอยู่ในกฎ ⑦ก อยู่แล้ว)',
         all(f.startswith('check_') for f in NOT_IN_CI)),
        # ── v1.2 · กฎ ⑦ก ต้องไม่ผูกกับภาษา ────────────────────────
        ('กฎ ⑦ก เฝ้าไฟล์ .js ด้วย ⛔ ไม่ใช่เฉพาะ .py',
         is_checker('check_export_figures.js') is True),
        ('…และยังเฝ้า .py เหมือนเดิม (ไม่ได้แลกของเก่าไปกับของใหม่)',
         is_checker('check_bot_add.py') is True),
        ('ไฟล์ที่ไม่ขึ้นต้น check_ ยังอยู่นอกกฎเหมือนเดิม',
         is_checker('build_bank.py') is False),
        ('⛔ ตั้งชื่อ test_*.js แล้วหลุดกฎ — ยืนยันว่ายังหลุดจริง จะได้ไม่มีใครเผลอใช้ชื่อนี้',
         is_checker('test_export_figures.js') is False),
        ('นามสกุลอื่นยังไม่อยู่ในกฎ (ประกาศไว้ ไม่ใช่ปล่อยให้เดา)',
         is_checker('check_something.sh') is False),
        # ── v1.2 · ตัวอ่าน JS ต้องชี้บรรทัดถูก ────────────────────
        ('เลขบรรทัดฝั่ง JS ตรงกับไฟล์จริง แม้มีคอมเมนต์บล็อกคั่น',
         exit_codes_js('/* ก\n * ข\n */\nprocess.exit(3);\n') == [(4, 3, 'process.exit')]),
        ('คอมเมนต์บล็อกที่มี process.exit อยู่ข้างใน ⇒ ต้องไม่นับ',
         exit_codes_js('/* process.exit(3) */\nprocess.exit(1);\n')
         == [(2, 1, 'process.exit')]),
        ('ของจริงที่อยู่ก่อน // บนบรรทัดเดียวกัน ⇒ ต้องไม่หายไปด้วย',
         exit_codes_js('process.exit(3); // อธิบาย\n') == [(1, 3, 'process.exit')]),
    ]
    for name, passed in self_checks:
        print(f'  {"✅" if passed else "🔴 ล้ม"}  {name}')
        ok &= passed

    print()
    if not ok:
        print('🔴 SELF-TEST ไม่ผ่าน ⇒ ผลของด่านนี้กับไฟล์จริงเชื่อไม่ได้')
        return 2
    print(f'✅ SELF-TEST ผ่าน — ตัวล่อ'
          f' {N_DECOY_PY + N_DECOY_YML + N_DECOY_YML_EXIT + N_DECOY_JS} ตัว'
          f' · ตัวสะอาด {N_CLEAN_PY + N_CLEAN_YML + N_CLEAN_JS} ตัว'
          f' · ด่านตรวจตัวเอง {len(self_checks)} ข้อ')
    return 0


def main():
    ap = argparse.ArgumentParser(description='ตรวจว่ารหัสออกแปลว่าอย่างที่ตกลงกันไว้')
    ap.add_argument('--scripts-dir', default=SCRIPTS_DIR)
    ap.add_argument('--workflow', default=WORKFLOW)
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    a = ap.parse_args()

    if a.version:
        print(CHECKER_VERSION)
        return 0
    if a.selftest:
        return selftest()

    print(f'ด่าน 11 v{CHECKER_VERSION} · ข้อตกลงรหัสออก 0 ผ่าน · 1 เนื้อหาแดง'
          ' · 2 เครื่องมือแดง')

    if not os.path.isdir(a.scripts_dir):
        print(f'🔴 ไม่พบโฟลเดอร์ {a.scripts_dir} ⇒ เทียบไม่ได้ ⛔ ไม่ใช่ "ไม่มีอะไรผิด"')
        return 2

    all_files = sorted(os.listdir(a.scripts_dir))
    files = [f for f in all_files if f.endswith('.py')]      # ฝั่งที่อ่านด้วย ast
    files_js = [f for f in all_files if f.endswith('.js')]   # ฝั่งที่อ่านด้วย regex
    if not files:
        print(f'🔴 ไม่มีไฟล์ .py ใน {a.scripts_dir} ⇒ ด่านนี้ไม่มีอะไรให้ตรวจ')
        print('   ⛔ "ไม่มีของให้ตรวจ" ไม่ใช่ "ตรวจแล้วผ่าน" (กับดัก ⑨)')
        return 2

    bad, n_codes = [], 0
    for fn in files:
        path = os.path.join(a.scripts_dir, fn)
        try:
            src = open(path, encoding='utf-8').read()
            codes = exit_codes_py(src, path)
        except (OSError, SyntaxError) as e:
            print(f'🔴 อ่าน/แปลง {path} ไม่ได้ ({e}) ⇒ เทียบไม่ได้')
            return 2
        n_codes += len(codes)
        for ln, c, src_kind in codes:
            if c not in OK_CODES:
                bad.append((path, ln, c, src_kind))

    # ── ฝั่ง .js (v1.2) — ตัวหารแยกต่างหาก ⛔ ห้ามรวมกับฝั่ง .py ──
    n_codes_js = 0
    for fn in files_js:
        path = os.path.join(a.scripts_dir, fn)
        try:
            codes = exit_codes_js(open(path, encoding='utf-8').read(), path)
        except OSError as e:
            print(f'🔴 อ่าน {path} ไม่ได้ ({e}) ⇒ เทียบไม่ได้')
            return 2
        n_codes_js += len(codes)
        for ln, c, src_kind in codes:
            if c not in OK_CODES:
                bad.append((path, ln, c, src_kind))

    # ── ไฟล์ workflow ────────────────────────────────────────
    wf_swallow, wf_bad, wf_text = [], [], None
    if os.path.exists(a.workflow):
        wf_text = open(a.workflow, encoding='utf-8').read()
        wf_swallow = swallowed(wf_text)
        wf_bad = [(ln, c) for ln, c in exit_codes_yaml(wf_text) if c not in OK_CODES]
    else:
        print(f'🔴 ไม่พบ {a.workflow} ⇒ ตรวจฝั่ง "มีคนอ่านรหัสไหม" ไม่ได้')
        return 2

    # ── ⑦ก · ตัวตรวจที่ไม่มีใครเรียก = ตัวตรวจที่ไม่มีอยู่จริง ──
    watched = [f for f in all_files if is_checker(f)]
    orphan = [f for f in watched
              if not called_in_workflow(wf_text, f) and f not in NOT_IN_CI]
    # ⑨ ตัวหารของรายการยกเว้น: ยกเว้นไฟล์ที่ไม่มีอยู่จริง = รายการเน่าที่ไม่มีใครรู้
    stale_waiver = [f for f in NOT_IN_CI if f not in all_files]
    ok_reason, reason_bad = check_not_in_ci()

    print(f'  อ่าน .py {len(files)} ไฟล์ · .js {len(files_js)} ไฟล์ ใน {a.scripts_dir}/'
          f' · ไฟล์ด่าน {a.workflow}')
    print(f'  ⑨ ตัวหาร (แยกฝั่ง ⛔ ห้ามรวม): รหัสออกที่เป็นเลขตายตัว'
          f' — .py {n_codes} จุด (อ่านด้วย ast) · .js {n_codes_js} จุด (อ่านด้วย regex)')
    print(f'  ⑨ ตัวหารกฎ ⑦ก: ไฟล์ที่ขึ้นต้น check_ และนามสกุลใน {CHECKER_EXTS}'
          f' = {len(watched)} ไฟล์')
    print('  ⚠️ ฝั่ง .js ยัง ⛔ จับไม่ได้: process.exitCode = N · exit(<ตัวแปร>) · throw'
          ' ⇒ "เงียบ" ที่นั่นแปลว่า "ยังไม่ได้ตรวจ" ไม่ใช่ "ตรวจแล้วสะอาด"')
    if n_codes == 0:
        print('🔴 ไม่พบรหัสออกที่เป็นเลขตายตัวเลยสักจุดฝั่ง .py ⇒ ตัวอ่านน่าจะพัง')
        return 2
    if files_js and n_codes_js == 0:
        print(f'🔴 มีไฟล์ .js {len(files_js)} ไฟล์ แต่อ่านรหัสออกไม่เจอสักจุด'
              ' ⇒ ตัวอ่านฝั่ง JS น่าจะพัง (หรือไฟล์เปลี่ยนท่าออกไปแล้ว)')
        print('   ⛔ "ไม่เจอ" ที่นี่ไม่ใช่ "สะอาด" — ตัวตรวจต้องออกจากโปรแกรมด้วย'
              ' process.exit() เสมอ (กับดัก ⑨)')
        return 2
    if watched and not files_js and any(f.endswith('.js') for f in NOT_IN_CI):
        print('🔴 NOT_IN_CI อ้างไฟล์ .js แต่ไม่มีไฟล์ .js อยู่จริง')
        return 2
    print()

    red = False
    if bad:
        red = True
        print(f'🔴 รหัสออกที่ไม่มีในข้อตกลง {len(bad)} จุด:')
        for path, ln, c, kind in bad:
            print(f'   {path}:{ln}  รหัส {c}  ({kind})')
        print('   ⇒ ใช้ 1 ถ้าเป็น "เนื้อหาในคลังผิด" · ใช้ 2 ถ้าเป็น "เครื่องมือ/ข้อมูล'
              'เทียบไม่ได้"')
        print('   เหตุผล: คนอ่าน log ต้องแยกได้ว่า "ไปแก้ข้อ" หรือ "ไปแก้สคริปต์"')
        print()
    if wf_bad:
        red = True
        print(f'🔴 `exit N` ที่ไม่มีในข้อตกลงใน {a.workflow} {len(wf_bad)} จุด:')
        for ln, c in wf_bad:
            print(f'   {a.workflow}:{ln}  รหัส {c}')
        print()
    if wf_swallow:
        red = True
        print(f'🔴 บรรทัดที่กลืนรหัสออก {len(wf_swallow)} จุด:')
        for ln, line, why in wf_swallow:
            print(f'   {a.workflow}:{ln}  {line}')
            print(f'      ↳ {why}')
        print(f'   ถ้ามีเหตุผลจริง ⇒ เขียนคำว่า "{ALLOW_MARK}: <เหตุผล>" ท้ายบรรทัดนั้น')
        print()
    if orphan:
        red = True
        print(f'🔴 ตัวตรวจที่ไม่มีใครเรียกใน {a.workflow} {len(orphan)} ไฟล์:')
        for f in orphan:
            print(f'   {a.scripts_dir}/{f}')
        print('   ⇒ กับดัก ⑦ก: "คืนรหัสถูกต้อง" ไม่เท่ากับ "มีคนอ่านรหัสนั้น"')
        print('     ตัวตรวจที่ไม่มีด่านเรียก = ตัวตรวจที่ไม่มีอยู่จริงในสายตา CI')
        print(f'   (ถ้าตั้งใจไม่ผูกอย่างถาวร ⇒ ประกาศใน NOT_IN_CI พร้อมเหตุผล'
              f' ≥{MIN_NOT_IN_CI_REASON} ตัวอักษร)')
        print()
    if not ok_reason:
        red = True
        print('🔴 รายการยกเว้น NOT_IN_CI มีรายการที่เหตุผลใช้ไม่ได้:')
        for m in reason_bad:
            print(f'   {m}')
        print('   ⇒ เหตุผลว่าง ๆ คือการปิดด่านที่หน้าตาเหมือนการประกาศ')
        print()
    if stale_waiver:
        red = True
        print(f'🔴 NOT_IN_CI ยกเว้นไฟล์ที่ไม่มีอยู่จริง {len(stale_waiver)} รายการ:')
        for f in stale_waiver:
            print(f'   {a.scripts_dir}/{f}  — ไม่มีไฟล์นี้')
        print('   ⇒ ⑨ ข้อยกเว้นที่ไม่ชี้ไปที่อะไรเลย = รายการเน่าที่รอวันยกเว้นผิดตัว')
        print()

    if red:
        return 1

    _n_check = len(watched)
    print(f'✅ รหัสออกทุกจุดอยู่ในข้อตกลง (.py {n_codes} จุด · .js {n_codes_js} จุด)'
          f' · ไม่มีบรรทัดกลืนรหัส · ตัวตรวจ {_n_check - len(NOT_IN_CI)}/{_n_check}'
          ' ไฟล์ถูกเรียกใน CI ครบ')
    for f, why in sorted(NOT_IN_CI.items()):
        # 🔴 พิมพ์ทุกรอบแม้ผ่าน — ข้อยกเว้นที่เงียบคือข้อยกเว้นที่ลืม
        print(f'   🟠 ยกเว้นโดยเจตนา: {f}')
        print(f'      ↳ {why}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

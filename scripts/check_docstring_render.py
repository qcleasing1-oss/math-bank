#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ด่าน 22 · check_docstring_render.py v1.0 — วัดที่ **ปลายทาง** ⛔ ไม่ใช่ที่ซอร์ส

ทำอะไร
------
อ่าน docstring ที่ python **เรนเดอร์ออกมาแล้ว** (ast.get_docstring) แล้วถามคำถามเดียว:
    มีอักขระควบคุมหลงเหลืออยู่ไหม  (ord < 32 และ ⛔ ไม่ใช่ \n)
ถ้ามี = ผู้เขียนพิมพ์ path วินโดวส์ลงใน docstring ธรรมดา แล้ว python **กินแบ็กสแลชไปแล้ว**
    ผู้เขียนพิมพ์   --bank data\bank.json
    คนอ่านเห็น      --bank dataank.json          (\b = BS · \r = CR · \t = TAB)

ทำไมต้องมีด่านนี้ (⛔ ไม่ใช่ "เพราะพลาดแล้วเลยเพิ่มด่าน")
-----------------------------------------------------
🔑 warning ของ python กับบั๊กตัวนี้เป็น **เซตคนละเซต — ทับกันแค่บางส่วน**
    escape ที่ **ผิด** (\{ \m \l …) ⇒ python เก็บไว้ทั้งดุ้น ⇒ 🟢 ⛔ ไม่ทำอะไร · แต่ **ส่งเสียง**
    escape ที่ **ถูก** (\b \r \t \f \v \a) ⇒ python กินไปแล้ว ⇒ 🔴 บั๊กจริง · แต่ **เงียบสนิท**
⇒ ตามล่า warning ⇒ ตัวชี้วัดถึงศูนย์ **ก่อน** ปัญหาหมด · ด่านนี้จึงวัดที่ผลลัพธ์ที่ผู้ใช้เห็น

🔑 และเกณฑ์ที่ใช้ **⛔ ไม่ใช่บัญชีดำ** — เป็น "อักขระ ord<32 ที่ ⛔ ไม่ใช่ \n"
    เหตุ: บัญชีดำชุด (\b \r \f \v \a) ที่ทั้งสองเลนใช้ตรงกัน **พลาด \t** ⇒ tools/technique_index.py
    รอดทั้งสองการกวาด ⇒ บัญชีดำที่ยาวขึ้นได้เรื่อย ๆ คือกฎที่จะพลาดอีก

ตัวเลข 3 ตัวที่ด่านต้องประกาศ (㉑)
--------------------------------
    ตัวหาร        : ไฟล์ .py ทั้งหมดใน SCOPE_ROOTS (⬤ นับเองตอนรัน ⛔ ไม่พิมพ์มือ)
                    ที่ 14ea26b8 = 335 ไฟล์ · 458 docstring
    แดงวันแรก     : FIRST_RED_FILES = 16 ไฟล์ ที่ 14ea26b8 (⬤ วัดเอง 27 ส.ค. 2569)
                    15 ไฟล์แรกเป็นชุดที่ E→MB #106 §2 กวาดเจอ · ตัวที่ 16 (\t) เพิ่มโดย MB→E #107
    เคสต้นเรื่อง  : tools/answer_bias.py (\b · ⛔ ไม่มี warning) และ
                    tools/technique_index.py (\t · ⛔ ไม่มี warning ⛔ และบัญชีดำเดิมก็ไม่จับ)

จุดบอดที่ประกาศไว้ — "เขียว" ของด่านนี้ ⛔ ไม่ได้แปลว่าคลังสะอาด
------------------------------------------------------------
    ① เห็นเฉพาะ docstring ของ Module/Class/Function/AsyncFunction
       ⛔ ไม่เห็น string literal อื่น
       ⬤ วัดแล้วที่ 14ea26b8: ขยายไปดู string literal ทั้ง 34,658 ตัว ⇒ บั๊กใหม่ **0** · เท็จบวก **2**
         (`'\r' in raw` ที่ตั้งใจเช็ก CRLF ใน check_k1.py / check_k2.py)
       ⇒ ขอบเขตนี้จึงเป็นของที่ **วัดแล้ว** ⛔ ไม่ใช่ของที่เดา
    ② ⛔ ไม่เห็น `\n` ที่ผู้เขียนพิมพ์เองใน docstring — แยกจากการขึ้นบรรทัดจริง ⛔ ไม่ได้
    ③ ⛔ ไม่เห็นไฟล์นอก SCOPE_ROOTS (⬤ ที่ 14ea26b8: _t1run/ 3 ไฟล์ กวาดแล้วสะอาด)
    ④ ⛔ ไม่รู้ว่า path ในข้อความ *ควร* เป็นอะไร — รู้แค่ว่า **มันถูกกินไปแล้ว**
    ⑤ ⛔ ไม่เห็น escape ที่ python กินแล้วได้อักขระ **ord ≥ 32**
       (แบ็กสแลชคู่ · เครื่องหมายคำพูดที่ถูก escape · \0–\7 · \xNN · \uNNNN · \N{…})
       ⬤ วัดแล้วที่ 14ea26b8 (E→MB #108 §3 ชี้ · MB วัดเองด้วย ast.get_source_segment):
          docstring ที่ python กินอะไรไป = 29 จุด ⇒ แบ็กสแลชคู่ × 62 = **เจตนา** (ต้องการแบ็กสแลชจริง)
          ตระกูล \0–\7 \xNN \uNNNN \N{…} = **0 จุด** ⇒ วันนี้ ⛔ ไม่มีบั๊กจริงในตระกูลนี้
       ⇒ ⚠️ วันที่มีคนพิมพ์ C:\x41 ในคำอธิบาย **ด่านนี้จะเงียบ** — และนี่คือขอบที่ **ประกาศไว้แล้ว**
          ⛔ ไม่ใช่ขอบที่เงียบ (ขอบที่ประกาศไว้ อันตรายน้อยกว่าขอบที่ไม่มีใครรู้ว่ามี)
       🔴 ⛔ ห้ามแก้ด้วยการเติม \xNN \uNNNN เข้าบัญชี — นั่นคือการกลับไปทำบัญชีดำที่เพิ่งพลาด \t มา

รหัสสาเหตุ (ทุกข้อความต้องบอก "ต้องแก้ที่:" — ธรรมเนียมจากก้อน A2)
    docstring-render-eaten   🔴 docstring ถูกกิน ⇒ ต้องแก้ที่: docstring (เติม r นำหน้า หรือ \\ สองขีด)
    docstring-parse-failed   🔴 ไฟล์ parse ⛔ ไม่ได้ ⇒ ต้องแก้ที่: ไฟล์ต้นทาง (⛔ ไม่ข้ามเงียบ)
    docstring-divisor-zero   🔴 ตัวหาร 0 ⇒ ต้องแก้ที่: ขอบเขตการกวาด (SCOPE_ROOTS ผิด)

ใช้:  python scripts/check_docstring_render.py [--root .]
      python scripts/check_docstring_render.py --selftest
"""
import argparse
import ast
import os
import sys
import tempfile

SCOPE_ROOTS = ("scripts", "tools")
SKIP_DIRS = {"__pycache__", "_to_delete", ".git", "node_modules", ".venv"}
FIRST_RED_FILES = 16          # ⬤ วัดเองที่ 14ea26b8 · 27 ส.ค. 2569
FIRST_RED_BASE = "14ea26b8"

CODE_EATEN = "docstring-render-eaten"
CODE_PARSE = "docstring-parse-failed"
CODE_ZERO = "docstring-divisor-zero"


def control_chars(text):
    """อักขระที่บอกว่า python กินแบ็กสแลชไปแล้ว — ord<32 ที่ ⛔ ไม่ใช่ \n"""
    return sorted({c for c in (text or "") if ord(c) < 32 and c != "\n"})


def iter_py_files(root, roots=SCOPE_ROOTS):
    out = []
    for r in roots:
        base = os.path.join(root, r)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                if fn.endswith(".py"):
                    out.append(os.path.join(dirpath, fn))
    return sorted(out)


def doc_nodes(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            yield node


def node_label(node):
    if isinstance(node, ast.Module):
        return "<module>"
    kind = "class" if isinstance(node, ast.ClassDef) else "def"
    return "%s %s (บรรทัด %d)" % (kind, node.name, node.lineno)


def scan(root, roots=SCOPE_ROOTS):
    """คืน (findings, n_files, n_docstrings) — findings = [(code, path, ที่, รายละเอียด)]"""
    findings = []
    files = iter_py_files(root, roots)
    n_doc = 0
    for path in files:
        rel = os.path.relpath(path, root)
        try:
            src = open(path, encoding="utf-8").read()
            tree = ast.parse(src)
        except Exception as exc:                       # fail-closed ⛔ ไม่ข้ามเงียบ
            findings.append((CODE_PARSE, rel, "-", "%s: %s" % (type(exc).__name__, exc)))
            continue
        for node in doc_nodes(tree):
            doc = ast.get_docstring(node, clean=False)
            if doc is None:
                continue
            n_doc += 1
            bad = control_chars(doc)
            if bad:
                shown = " ".join(hex(ord(c)) for c in bad)
                sample = ""
                for line in doc.split("\n"):
                    if control_chars(line):
                        sample = repr(line)[:120]
                        break
                findings.append((CODE_EATEN, rel, node_label(node),
                                 "อักขระที่ถูกกิน [%s] · เรนเดอร์: %s" % (shown, sample)))
    if not files:
        findings.append((CODE_ZERO, "-", "-", "⛔ ไม่พบไฟล์ .py เลยใน %s" % (list(roots),)))
    return findings, len(files), n_doc


FIX_HINT = {
    CODE_EATEN: "ต้องแก้ที่: docstring — เติม r นำหน้า (r\"\"\"…) หรือเขียนแบ็กสแลชสองขีด",
    CODE_PARSE: "ต้องแก้ที่: ไฟล์ต้นทาง — ด่านนี้ ⛔ ไม่ข้ามไฟล์ที่อ่านไม่ออก",
    CODE_ZERO: "ต้องแก้ที่: ขอบเขตการกวาด — SCOPE_ROOTS ชี้ผิดที่ ⇒ ตัวหาร 0 เชื่อไม่ได้",
}


def report(findings, n_files, n_doc, stream=sys.stdout):
    stream.write("ด่าน 22 · docstring ที่เรนเดอร์แล้ว — กวาด %d ไฟล์ · %d docstring\n"
                 % (n_files, n_doc))
    for code, path, where, detail in findings:
        stream.write("  🔴 [%s] %s · %s\n      %s\n      %s\n"
                     % (code, path, where, detail, FIX_HINT[code]))
    n_bad_files = len({f[1] for f in findings if f[0] != CODE_ZERO})
    stream.write("  ── พบ %d จุด · ใน %d ไฟล์ · จากตัวหาร %d ไฟล์ / %d docstring\n"
                 % (len(findings), n_bad_files, n_files, n_doc))
    return len(findings)


# ─────────────────────────── selftest ───────────────────────────
# 🧬 ฟิกซ์เจอร์ของด่านนี้ **เป็นของตัวเอง** ⛔ ไม่ยืนบนคลังจริง
#    เหตุ (rev12.2 §⑤①): วันที่คลังจริงสะอาด = วันที่งานสำเร็จ ⇒ เคส "ต้องแดง" จะเขียวเงียบ ๆ

F_EATEN_B = '"""ใช้: python x.py [--bank data\\bank.json]"""\n'
F_EATEN_R = '"""ใช้: python x.py [--done _t1run\\results]"""\n'
F_EATEN_T = '"""ใช้: python x.py [--out _t1run\\technique.html]"""\n'
F_EATEN_F = '"""หน้า\\form"""\n'
F_EATEN_V = '"""ตาราง\\vertical"""\n'
F_EATEN_A = '"""เตือน\\alert"""\n'
F_CLEAN_MULTI = '"""หัวเรื่อง\n\nบรรทัดสอง · ⛔ ไม่มีแบ็กสแลชเลย\n"""\n'
F_CLEAN_RAW = 'r"""ใช้: python x.py [--bank data\\bank.json]"""\n'
F_CLEAN_NEWLINE = '"""บรรทัดแรก\\nบรรทัดสอง"""\n'
F_CLEAN_LITERAL = "x = 1\nif '\\r' in 'abc':\n    pass\n"
F_FUNC = 'def f():\n    """ใช้: f(data\\bank.json)"""\n    return 1\n'
F_CLASS = 'class C:\n    """เก็บที่ data\\bank.json"""\n'
F_ASYNC = 'async def g():\n    """ผลไปที่ _t1run\\results"""\n'
F_CLEAN_DBL = "'''แบ็กสแลชจริง: เก็บที่ C:\\\\temp'''\n"
F_BROKEN = 'def (:\n'


def _write(d, name, text):
    p = os.path.join(d, "tools", name)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8", newline="").write(text)
    return p


def selftest():
    passed = []
    failed = []

    def case(label, ok):
        (passed if ok else failed).append(label)
        print("  %s %s" % ("✅" if ok else "❌", label))

    with tempfile.TemporaryDirectory() as d:
        _write(d, "a_b.py", F_EATEN_B)
        _write(d, "a_r.py", F_EATEN_R)
        _write(d, "a_t.py", F_EATEN_T)
        _write(d, "a_f.py", F_EATEN_F)
        _write(d, "a_v.py", F_EATEN_V)
        _write(d, "a_a.py", F_EATEN_A)
        _write(d, "ok_multi.py", F_CLEAN_MULTI)
        _write(d, "ok_raw.py", F_CLEAN_RAW)
        _write(d, "ok_newline.py", F_CLEAN_NEWLINE)
        _write(d, "ok_literal.py", F_CLEAN_LITERAL)
        _write(d, "b_func.py", F_FUNC)
        _write(d, "b_class.py", F_CLASS)
        _write(d, "b_async.py", F_ASYNC)
        _write(d, "ok_dbl.py", F_CLEAN_DBL)
        found, nf, nd = scan(d)
        hit = {os.path.basename(f[1]) for f in found}      # scan คืน path สัมพัทธ์ ⇒ เทียบด้วยชื่อไฟล์

        case("① \\b ใน docstring ⇒ จับได้", "a_b.py" in hit)
        case("② \\r ใน docstring ⇒ จับได้", "a_r.py" in hit)
        case("③ 🔑 \\t ใน docstring ⇒ จับได้ (บัญชีดำ \\b\\r\\f\\v\\a เดิม **พลาดตัวนี้**)",
             "a_t.py" in hit)
        case("④ \\f ⇒ จับได้", "a_f.py" in hit)
        case("⑤ \\v ⇒ จับได้", "a_v.py" in hit)
        case("⑥ \\a ⇒ จับได้", "a_a.py" in hit)
        case("⑦ (ต้องไม่จับ) docstring ปกติหลายบรรทัด ⇒ เงียบ", "ok_multi.py" not in hit)
        case("⑧ (ต้องไม่จับ) r-docstring ที่มี \\b ในซอร์ส ⇒ เงียบ", "ok_raw.py" not in hit)
        case("⑨ (ต้องไม่จับ · จุดบอด②) \\n ที่ผู้เขียนพิมพ์เอง ⇒ เงียบ",
             "ok_newline.py" not in hit)
        case("⑩ (ต้องไม่จับ · เท็จบวกจริงจาก check_k1.py) '\\r' ใน string ธรรมดา ⇒ เงียบ",
             "ok_literal.py" not in hit)
        case("⑪ docstring ของฟังก์ชัน ⇒ จับได้ (⛔ ไม่ใช่แค่ของโมดูล)", "b_func.py" in hit)
        case("⑫ docstring ของคลาส ⇒ จับได้", "b_class.py" in hit)
        case("⑬ docstring ของ async def ⇒ จับได้", "b_async.py" in hit)
        case("⑭ รายงานต้องชี้ **ราย docstring** ⛔ ไม่ใช่แค่ชื่อไฟล์",
             all(f[2] for f in found if f[0] == CODE_EATEN))
        case("⑮ ทุกข้อความต้องมีคำว่า \"ต้องแก้ที่:\" (ธรรมเนียม A2 ㊷)",
             all("ต้องแก้ที่:" in FIX_HINT[c] for c in (CODE_EATEN, CODE_PARSE, CODE_ZERO)))
        case("㉕ (ต้องไม่จับ · จุดบอด ⑤) docstring ที่มีแบ็กสแลชจริง ⇒ เงียบ",
             "ok_dbl.py" not in hit)
        case("⑯ ตัวหารต้องนับเอง ⛔ ไม่พิมพ์มือ (14 ไฟล์ · 13 docstring)", nf == 14 and nd == 13)

        _write(d, "broken.py", F_BROKEN)
        found2, nf2, _ = scan(d)
        case("⑰ 🔒 ไฟล์ที่ parse ⛔ ไม่ได้ ⇒ **แดง** ⛔ ไม่ข้ามเงียบ (fail-closed)",
             any(f[0] == CODE_PARSE for f in found2))

    with tempfile.TemporaryDirectory() as d2:
        found3, nf3, _ = scan(d2)
        case("⑱ ตัวหาร 0 ⇒ แดง (ทรงเดียวกับกฎ ③ ของด่าน 21)",
             any(f[0] == CODE_ZERO for f in found3))

    # ── 🧬 มิวแทนต์: เปลี่ยนเกณฑ์แล้วต้องพลาด ⇒ พิสูจน์ว่าเกณฑ์ตัวจริง "กัด" ────────────
    with tempfile.TemporaryDirectory() as d3:
        _write(d3, "a_t.py", F_EATEN_T)
        _write(d3, "a_b.py", F_EATEN_B)
        _write(d3, "ok_raw.py", F_CLEAN_RAW)
        real = control_chars

        # ⚠️ บรรทัดล่างมีอักขระควบคุมอยู่ใน string **โดยตั้งใจ** — มันคือบัญชีดำชุดเดิมที่
        #    เรากำลังพิสูจน์ว่าพลาด \t ⇒ ถ้าวันหนึ่งมีคนขยายด่านนี้ไปกวาด literal ทุกตัว
        #    ไฟล์นี้จะติดธง ⇒ นั่นคือ **เท็จบวกที่ประกาศไว้แล้ว** ⛔ ไม่ใช่บั๊ก
        BLACKLIST_OLD = "\x08\r\x0c\x0b\x07"      # \b \r \f \v \a — ⛔ ไม่มี \t

        def mut_blacklist(text):     # มิวแทนต์ ① — บัญชีดำชุดที่ทั้งสองเลนเคยใช้
            return sorted({c for c in (text or "") if c in BLACKLIST_OLD})

        def mut_source(text):        # มิวแทนต์ ② — วัดที่ซอร์สแทนปลายทาง
            return []

        g = globals()
        g["control_chars"] = mut_blacklist
        m1 = {os.path.basename(f[1]) for f in scan(d3)[0]}
        g["control_chars"] = mut_source
        m2 = {os.path.basename(f[1]) for f in scan(d3)[0]}
        g["control_chars"] = real
        base = {os.path.basename(f[1]) for f in scan(d3)[0]}

        case("⑲ 🧬 มิวแทนต์ 'ใช้บัญชีดำ \\b\\r\\f\\v\\a' ⇒ **ต้องพลาด \\t** (ตัวจริงจับได้)",
             "a_t.py" in base and "a_t.py" not in m1 and "a_b.py" in m1)
        case("⑳ 🧬 มิวแทนต์ 'วัดที่ซอร์ส' ⇒ **ต้องพลาดทุกตัว**", len(m2) == 0 and len(base) == 2)
        case("㉑ 🧬 ฟิกซ์เจอร์ที่ ⛔ ถูกมิวเทต ต้องเขียวทุกรอบ (คู่บังคับ rev12.2 §⑤①)",
             "ok_raw.py" not in base and "ok_raw.py" not in m1 and "ok_raw.py" not in m2)

    case("㉒ หัวไฟล์ผูกกับตัวเลขที่วัดได้ (แดงวันแรก %d ที่ %s)" % (FIRST_RED_FILES, FIRST_RED_BASE),
         isinstance(FIRST_RED_FILES, int) and FIRST_RED_FILES > 0
         and str(FIRST_RED_FILES) in __doc__ and FIRST_RED_BASE in __doc__)
    case("㉓ จุดบอดต้องถูกประกาศในหัวไฟล์ ⇒ \"เขียว\" ⛔ ไม่โกหก",
         "จุดบอดที่ประกาศไว้" in __doc__)
    case("㉔ 🔒 จุดบอด ⑤ (escape ที่ได้ ord ≥ 32) ต้องอยู่ในหัวไฟล์ ⛔ อยู่แต่ในจดหมายไม่ได้",
         "ord ≥ 32" in __doc__ and "0 จุด" in __doc__)

    total = len(passed) + len(failed)
    print("  ── ผ่าน %d · ล้ม %d · รวม %d เคส" % (len(passed), len(failed), total))
    return 1 if failed else 0


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--root", default=".")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        print("ด่าน 22 · check_docstring_render v1.0 — self-test")
        return selftest()
    findings, n_files, n_doc = scan(args.root)
    n = report(findings, n_files, n_doc)
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())

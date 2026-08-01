#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ด่าน 6 · ตรึงสิ่งที่บอทได้รับอนุญาตให้ git add — v1.0 (1 ส.ค. 69)

🔴 ทำไมกฎนี้ถึงมีอยู่ (ข้อความจากพอร์ทัล รอบ 13 · เก็บไว้ในไฟล์ ไม่ใช่ในจดหมาย):

    build-bank.yml เขียนได้เฉพาะ data/bank.json
    ถ้าเพิ่มไฟล์อื่น commit ของบอทจะไม่ผ่าน guards.yml
    (GitHub ไม่ re-trigger workflow บน GITHUB_TOKEN)
    ⇒ จะมีคอมมิตในสายหลักที่ไม่เคยผ่านด่าน

    "ไม่งั้นคนที่เจอด่านนี้แดงจะคิดว่าเป็นกฎจุกจิก แล้วหาทางปิด"

⇒ ด่านนี้จึงพิมพ์ "เหตุผล" ทุกครั้งที่แดง ไม่ใช่แค่ชื่อกฎ

⚠️ ด่านนี้ผูกกับ "สตริงในไฟล์ข้อความ" ซึ่งคือกับดักข้อ ⑦ ของเราเอง
   ⇒ จึงมี --selftest ที่มีตัวอย่างดี/เสียฝังในตัว และ CI ต้องรัน --selftest ก่อนเสมอ
   ⇒ ด่านที่ "ไม่เคยพิสูจน์ว่าจับได้" ไม่ต่างจากไม่มีด่าน

⛔ ขอบเขตที่ด่านนี้ *ไม่* ครอบคลุม (เขียนไว้ให้เห็น ไม่ให้เข้าใจว่าครอบจักรวาล):
   · git add ที่ถูกเรียกจากสคริปต์ภายนอกที่ workflow ไป source มา
   · ชื่อไฟล์ที่ประกอบจากตัวแปรเชลล์ เช่น  git add "$F"   (จับได้ว่าไม่ใช่ค่าที่อนุญาต ⇒ แดง)
   · การ push ด้วยเครื่องมืออื่นที่ไม่ใช่ git (เช่น REST API ของ GitHub)

🔴 v1.2 (1 ส.ค. 69) — ปิดรูตัวหาร (กับดัก ⑨):
   เดิม ถ้าไฟล์ที่ชี้ให้ตรวจ "ไม่มีคำสั่ง git เลยสักบรรทัด" ด่านนี้พิมพ์
       พบ git add 0 บรรทัด · git commit 0 บรรทัด  ⇒ ✅ ผ่าน   (รหัสออก 0)
   ซึ่งคือการขึ้นเขียวบน **ศูนย์** — ไม่ได้แปลว่า "ตรวจแล้วสะอาด"
   แต่แปลว่า "ไม่มีของให้ตรวจ" ⇒ ถ้าบอทถูกย้ายไปใช้ composite action,
   สคริปต์ภายนอก, หรือ gh api ด่านนี้จะเขียวตลอดไปโดยไม่ตรวจอะไรเลย
   ⇒ ตั้งแต่ v1.2 กรณีนี้เป็น **รหัสออก 2 (เครื่องมือแดง)** ไม่ใช่ 1
      เพราะตัวไฟล์ไม่ได้ผิดกฎ — ตัวด่านต่างหากที่มองไม่เห็นของที่ต้องเฝ้า

รหัสออก: 0 = ผ่าน · 1 = ไฟล์ผิดกฎ · 2 = ด่านเองใช้ไม่ได้ (self-test ล้ม / หาไฟล์ไม่เจอ /
        ไม่มีคำสั่ง git ให้ตรวจเลย)
"""
import sys, os, argparse

VERSION = '1.2'

ALLOWED_PATHS = ['data/bank.json']

# ธงที่ทำให้ขอบเขตของ add กว้างเกินคำสั่ง
BAD_FLAGS = ['-A', '--all', '-u', '--update', '-p', '--patch', '-i', '--interactive']
# ตัวถูกกระทำที่กวาดทั้งต้นไม้
BAD_OPERANDS = ['.', '*', './', ':/', ':/.', '..', '--']


def _strip_comment(line):
    """ตัดคอมเมนต์ของเชลล์ — # ที่ขึ้นต้นคำเท่านั้น (กัน URL อย่าง a#b)"""
    out, in_s, in_d = [], False, False
    for i, ch in enumerate(line):
        if ch == "'" and not in_d:
            in_s = not in_s
        elif ch == '"' and not in_s:
            in_d = not in_d
        elif ch == '#' and not in_s and not in_d and (i == 0 or line[i-1].isspace()):
            break
        out.append(ch)
    return ''.join(out)


def check_text(text):
    """คืน (ผิดกฎ[], สรุป{}) — ผิดกฎว่าง = ผ่าน"""
    bad, n_add, n_commit = [], 0, 0
    for ln, raw in enumerate(text.splitlines(), 1):
        line = _strip_comment(raw).strip()
        if not line:
            continue
        # หา 'git add' / 'git commit' ในบรรทัด (รองรับ && ; || ต่อกันในบรรทัดเดียว)
        # ⛔ ห้าม .split() แล้ว join กลับ — str.split() ไม่มีอาร์กิวเมนต์
        #    กลืน '\n' ที่แทรกไว้เป็นตัวคั่นทิ้ง ⇒ ทุกท่อนหลอมกลับเป็นท่อนเดียว
        #    (บั๊กจริงของ v1.0 · self-test จับได้เอง ⇒ นี่คือกับดักข้อ ⑦ ตัวเป็น ๆ)
        for seg in line.replace('||', '&&').replace(';', '&&').split('&&'):
            seg = seg.strip()
            t = seg.split()
            if len(t) < 2 or t[0] != 'git':
                continue
            if t[1] == 'commit':
                n_commit += 1
                for f in ('-a', '-am', '-am.', '--all'):
                    if f in t[2:] or any(x.startswith('-a') and not x.startswith('--')
                                         and 'a' in x[1:] for x in t[2:]
                                         if x.startswith('-') and not x.startswith('--')):
                        bad.append((ln, seg,
                                    "git commit -a เท่ากับ add ทุกไฟล์ที่ถูกติดตาม"
                                    " ⇒ เลี่ยงการตรึงนี้ไปเลย"))
                        break
                continue
            if t[1] != 'add':
                continue
            n_add += 1
            ops = t[2:]
            for x in ops:
                if '$' in x or '`' in x:
                    bad.append((ln, seg,
                                f"ชื่อไฟล์มาจากค่าที่คำนวณตอนรัน: {x}"
                                " ⇒ ขอบเขตจริงขึ้นกับค่าตอนนั้น ด่านนี้อ่านล่วงหน้าไม่ได้"))
                elif x in BAD_FLAGS or (x.startswith('-') and x not in ('--',)):
                    bad.append((ln, seg, f"ธง {x} ทำให้ขอบเขตกว้างเกินคำสั่ง"))
                elif x in BAD_OPERANDS:
                    bad.append((ln, seg, f"ตัวถูกกระทำ {x} กวาดทั้งต้นไม้"))
                elif x not in ALLOWED_PATHS:
                    bad.append((ln, seg,
                                f"เพิ่มไฟล์ที่ไม่ได้รับอนุญาต: {x}"
                                f" (อนุญาตเฉพาะ {', '.join(ALLOWED_PATHS)})"))
            if not ops:
                bad.append((ln, seg, "git add ที่ไม่มีตัวถูกกระทำ"))
    if n_commit and not n_add:
        bad.append((0, '(ทั้งไฟล์)',
                    "มี git commit แต่ไม่มี git add ที่ตรวจได้เลย"
                    " ⇒ ไฟล์ถูกจัดฉากด้วยวิธีอื่นที่ด่านนี้มองไม่เห็น"))
    return bad, {'add': n_add, 'commit': n_commit}


def divisor_hole(stat):
    """คืนเหตุผล (สตริง) ถ้า "ตัวหารเป็นศูนย์" · คืน None ถ้ามีของให้ตรวจจริง

    🔴 กับดัก ⑨ — ตัวเทียบทุกตัวต้องประกาศตัวหาร
       ตัวหารของด่านนี้คือ "จำนวนคำสั่ง git ที่อ่านเจอในไฟล์"
       ถ้าเป็น 0 ทั้งคู่ ประโยค "บอทแตะได้แค่ไฟล์ที่ตกลงกันไว้" ไม่มีฐานให้ยืน
       ⇒ ต้องพูดว่า "มองไม่เห็น" ไม่ใช่ "ผ่าน"

    ⚠️ แยกจากเคส n_commit>0 and n_add==0 ที่ check_text จับไว้แล้ว (นั่น = เนื้อหาแดง
       เพราะมี commit จริงแต่หา add ไม่เจอ) · เคสนี้คือ **ไม่มีอะไรเลยทั้งสองอย่าง**
    """
    if stat['add'] == 0 and stat['commit'] == 0:
        return ("อ่านไม่เจอคำสั่ง git แม้แต่บรรทัดเดียว"
                " ⇒ ไม่มีของให้ตรวจ ไม่ใช่ตรวจแล้วสะอาด")
    return None


# ─────────────────────────────────────────────────────────────
# ตัวอย่างฝังในตัว — ข้อพิสูจน์ว่าด่านนี้ "มีของให้จับแล้วจับได้จริง"
# ─────────────────────────────────────────────────────────────
GOOD = [
    ("ของจริงในวันนี้", """
      - name: Commit and push bank.json
        run: |
          git config user.name "github-actions[bot]"
          git add data/bank.json
          git commit -m "rebuild"
          git push
"""),
    ("บรรทัดที่ถูกคอมเมนต์ไว้ ต้องไม่นับเป็นคำสั่ง",
     "          # git add -A   ← ห้ามทำแบบนี้\n          git add data/bank.json\n"
     "          git commit -m x\n"),
    ("เชื่อมด้วย && ในบรรทัดเดียว",
     "          git add data/bank.json && git commit -m x && git push\n"),
    ("คอมเมนต์ต่อท้ายบรรทัดที่มีคำสั่งจริง ต้องถูกตัดก่อนอ่านตัวถูกกระทำ",
     "          git add data/bank.json   # อย่าเผลอเติม -A ตรงนี้\n"
     "          git commit -m x\n"),
]

# 🔴 ทุกเคสเสียต้องบอก "เหตุผลที่ต้องได้" ด้วย — ไม่ใช่แค่ "จับได้"
#    เพราะสิ่งที่คนอ่านแล้วใช้ตัดสินใจคือ "ข้อความ" ไม่ใช่ "รหัสออก"
#    ถ้าจับได้ด้วยเหตุผลผิด คนจะแก้ผิดที่ แล้วด่านก็เขียวโดยที่รูยังอยู่
#    (พบด้วยวิธีนับด่านที่ล้ม 1 ส.ค. 69 — ปิดตัวเช็คธงทิ้ง self-test v1.0 ยังเขียว)
BAD = [
    ("git add -A", "          git add -A\n          git commit -m x\n", "ธง -A"),
    ("git add .", "          git add .\n          git commit -m x\n", "กวาดทั้งต้นไม้"),
    ("git add -u", "          git add -u\n          git commit -m x\n", "ธง -u"),
    ("เพิ่มไฟล์นอกรายการ",
     "          git add data/bank.json docs/warn-baseline.json\n          git commit -m x\n",
     "ไม่ได้รับอนุญาต"),
    ("เพิ่มทั้งโฟลเดอร์ที่ชื่อขึ้นต้นเหมือนของที่อนุญาต",
     "          git add data\n          git commit -m x\n", "ไม่ได้รับอนุญาต"),
    ("ชื่อไฟล์มาจากตัวแปร",
     '          git add "$OUT"\n          git commit -m x\n', "คำนวณตอนรัน"),
    ("ชื่อไฟล์มาจากการแทนคำสั่ง $(...)",
     "          git add $(ls data)\n          git commit -m x\n", "คำนวณตอนรัน"),
    ("git commit -a เลี่ยงการตรึง", "          git commit -am x\n          git add data/bank.json\n",
     "git commit -a"),
    ("มี commit แต่ไม่มี add เลย", "          git commit -m x\n          git push\n",
     "ไม่มี git add"),
    ("git add เปล่า ๆ", "          git add\n          git commit -m x\n",
     "ไม่มีตัวถูกกระทำ"),
    ("แอบไว้หลัง && ในบรรทัดเดียวกับของถูก",
     "          git add data/bank.json && git add -A\n          git commit -m x\n", "ธง -A"),
]

# 🔴 เคสตัวหารเป็นศูนย์ — ต้อง "มองไม่เห็น" ไม่ใช่ "ผ่าน" (กับดัก ⑨)
#    ทั้งสามเคสนี้ check_text คืน bad ว่าง ⇒ ถ้าไม่มี divisor_hole ด่านจะเขียว
#    (พิสูจน์ด้วยของจริง 1 ส.ค. 69 — workflow ที่มีแต่ `run: echo hi` ได้ ✅ ผ่าน รหัสออก 0)
ZERO = [
    ("workflow ที่ไม่มีคำสั่ง git เลย",
     "name: x\njobs:\n  a:\n    steps:\n      - run: echo hi\n", True),
    ("ไฟล์ว่างเปล่า", "", True),
    ("มีแต่บรรทัดที่ถูกคอมเมนต์ไว้ทั้งหมด",
     "          # git add data/bank.json\n          # git commit -m x\n", True),
    ("มี git add จริง ⇒ ไม่ใช่รูตัวหาร",
     "          git add data/bank.json\n          git commit -m x\n", False),
    ("มีแต่ git commit (เนื้อหาแดงอยู่แล้ว) ⇒ ไม่ใช่รูตัวหาร",
     "          git commit -m x\n", False),
]

# 🔴 หมุดค่าตั้ง — การขยายสิทธิ์ต้อง "ตั้งใจแก้ที่นี่" ไม่ใช่แก้ผ่านไปเงียบ ๆ
#
# ⚠️ ขีดจำกัดที่รู้ตัว (กับดักข้อ ⑧): ถ้าใครเขียนหมุดนี้ใหม่เป็น
#      CONFIG_PIN = {'ALLOWED_PATHS': list(ALLOWED_PATHS)}
#    หมุดจะตามค่าจริงเสมอ ⇒ self-test ยังเขียวทั้งที่สิทธิ์ถูกขยาย
#    ด่านที่บังคับ "รอยต่อของรุ่น" อยู่ในรุ่นนั้นเองไม่ได้ — ตรวจได้ทางเดียวคือ
#    ตอนรีวิว diff ของไฟล์นี้ · จงใจไม่ซ่อนข้อจำกัดนี้ ดีกว่าปล่อยให้เชื่อเกินจริง
#    (วัดด้วยวิธีนับด่านที่ล้ม 1 ส.ค. 69 — ฉีดบั๊ก 7 ตัว จับได้ 6 · ตัวที่หลุดคือตัวนี้)
#
# ✅ อัปเดต 1 ส.ค. 69 — รูนี้ถูกปิดแล้ว (ตอบข้อ M7 ของพอร์ทัล · กับดัก ⑧):
#    ย้ายตัวเทียบออกไปอยู่ "นอกทั้งสองรุ่น" คือที่ CI แล้ว
#      → scripts/check_config_growth.py (ด่าน 10) เทียบ ALLOWED_PATHS
#        ที่ HEAD กับที่คอมมิตฐาน · โตขึ้น = แดง เว้นแต่ข้อความ commit
#        เขียนว่า  ALLOWED_PATHS+: <เหตุผล>
#    หมุดข้างล่างนี้ "คงไว้" อย่างรู้ตัว แต่เปลี่ยนหน้าที่:
#      เดิม = ตัวกันการขยายสิทธิ์  (ทำไม่ได้จริง — แก้พร้อมกันได้)
#      ใหม่ = ตัวกันการแก้พลาดในไฟล์นี้ไฟล์เดียว เช่น แก้ค่าแล้วลืมว่าแก้
#    ⛔ ห้ามเข้าใจว่าหมุดนี้คือด่านกันสิทธิ์ — ด่านกันสิทธิ์คือด่าน 10 เท่านั้น
CONFIG_PIN = {
    'ALLOWED_PATHS': ['data/bank.json'],
}


def selftest():
    ok = True
    print("─" * 62)
    print(f"SELF-TEST ด่าน 6 v{VERSION} — ตัวอย่างดี/เสียฝังในตัว")
    print("─" * 62)
    if ALLOWED_PATHS != CONFIG_PIN['ALLOWED_PATHS']:
        print(f"  🔴 ALLOWED_PATHS ถูกแก้เป็น {ALLOWED_PATHS}"
              f" แต่หมุดยังเป็น {CONFIG_PIN['ALLOWED_PATHS']}")
        print("     ⇒ ถ้าตั้งใจให้บอทเขียนไฟล์เพิ่มจริง ต้องแก้ CONFIG_PIN พร้อมกัน")
        print("       = ตัดสินใจโดยรู้ตัว · ห้ามขยายสิทธิ์ผ่านไปเงียบ ๆ")
        ok = False
    else:
        print(f"  ✅  (หมุดค่าตั้ง) ALLOWED_PATHS = {ALLOWED_PATHS}")
    for name, s in GOOD:
        bad, stat = check_text(s)
        good = not bad
        print(f"  {'✅' if good else '🔴 จับเกิน: ' + str(bad)}  (ต้องผ่าน) {name}")
        ok = ok and good
        # ⑨ เคสดีทุกเคสต้องมีของให้ตรวจจริง — ไม่งั้น "ผ่าน" ข้างบนไม่มีความหมาย
        if divisor_hole(stat) is not None:
            print(f"       🔴 แต่ตัวหารเป็นศูนย์ ⇒ เคสดีเคสนี้ไม่ได้พิสูจน์อะไรเลย")
            ok = False
    for name, s, want in BAD:
        bad, _ = check_text(s)
        msgs = ' | '.join(m for _, _, m in bad)
        if not bad:
            print(f"  🔴 จับไม่ได้  (ต้องจับได้) {name}")
            ok = False
        elif want not in msgs:
            # ⛔ "จับได้" ไม่พอ — ต้องจับได้ "เพราะเหตุผลที่ถูก"
            print(f"  🔴 จับได้แต่เหตุผลผิด  (ต้องมีคำว่า “{want}”) {name}")
            print(f"       ได้มาเป็น: {msgs}")
            ok = False
        else:
            print(f"  ✅  (ต้องจับได้ · เหตุผล “{want}”) {name}")
    for name, s, want_hole in ZERO:
        _, stat = check_text(s)
        hole = divisor_hole(stat) is not None
        if hole != want_hole:
            print(f"  🔴 ตัวหาร: ต้องเป็น "
                  f"{'รูตัวหาร' if want_hole else 'มีของให้ตรวจ'} แต่ได้ตรงข้าม — {name}")
            ok = False
        else:
            print(f"  ✅  (ตัวหาร: {'มองไม่เห็น ⇒ รหัสออก 2' if want_hole else 'มีของให้ตรวจ'})"
                  f" {name}")
    ok = _selftest_e2e() and ok
    print()
    return ok


def _selftest_e2e():
    """ยิงตัวเองจริงผ่าน subprocess แล้วดู "รหัสออก" ไม่ใช่ดูค่าที่ฟังก์ชันคืน

    🔴 กับดัก ⑦ก — "ตัวช่วยคืนค่าถูก" ≠ "มีคนเรียกตัวช่วยนั้น"
       ตารางข้างบนพิสูจน์แค่ว่า divisor_hole() คำนวณถูก
       ถ้าใครลบบรรทัดที่เรียกมันออกจาก main() ตารางข้างบนยัง ✅ ครบ
       ⇒ ต้องมีเคสที่วัด "รหัสออกของกระบวนการจริง" ปิดท้าย

    ⚠️ ลูกที่ถูกยิงจะรัน self-test เต็มเหมือนเดิมทุกเคส — ตัวแปรสภาพแวดล้อมนี้
       ห้ามข้ามการตรวจใด ๆ ทั้งสิ้น มันกันแค่ "ยิงหลานต่อไม่รู้จบ" เท่านั้น
       ⛔ ห้ามเปลี่ยนให้มันข้าม selftest — นั่นจะกลายเป็นทางลัดปิดด่าน
    """
    import subprocess, tempfile
    if os.environ.get('_BOTADD_E2E_CHILD') == '1':
        print("  🟠 (ปลายทางจริง) ข้ามการยิงซ้อนชั้น — นี่คือกระบวนการลูก")
        return True
    env = dict(os.environ, _BOTADD_E2E_CHILD='1')
    cases = [("ไม่มีคำสั่ง git เลย ⇒ ต้องได้ 2",
              "name: x\njobs:\n  a:\n    steps:\n      - run: echo hi\n", 2),
             ("git add -A ⇒ ต้องได้ 1",
              "          git add -A\n          git commit -m x\n", 1),
             ("ของถูกต้อง ⇒ ต้องได้ 0",
              "          git add data/bank.json\n          git commit -m x\n", 0)]
    ok = True
    with tempfile.TemporaryDirectory() as d:
        for name, body, want in cases:
            p = os.path.join(d, 'wf.yml')
            with open(p, 'w', encoding='utf-8') as f:
                f.write(body)
            r = subprocess.run([sys.executable, os.path.abspath(__file__), p],
                               capture_output=True, env=env)
            if r.returncode != want:
                print(f"  🔴 (ปลายทางจริง) ได้รหัสออก {r.returncode} ต้องเป็น {want} — {name}")
                print("       ⇒ ตัวช่วยอาจถูกต้อง แต่ main() ไม่ได้เรียกใช้ (กับดัก ⑦ก)")
                ok = False
            else:
                print(f"  ✅  (ปลายทางจริง · รหัสออก {want}) {name}")
    return ok


def main():
    ap = argparse.ArgumentParser(description=f'check_bot_add.py v{VERSION}')
    ap.add_argument('workflow', nargs='?', default='.github/workflows/build-bank.yml')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    a = ap.parse_args()
    if a.version:
        print(VERSION); return

    if not selftest():
        print("🔴 SELF-TEST ล้ม — ด่านนี้ผูกกับสตริง ถ้าพิสูจน์ไม่ได้ว่าจับได้")
        print("   ผลกับไฟล์จริงก็เชื่อไม่ได้ ⇒ ด่านแดง (กับดักข้อ ⑦)")
        sys.exit(2)
    if a.selftest:
        print("✅ self-test ผ่านครบ"); return

    if not os.path.exists(a.workflow):
        print(f"🔴 หาไฟล์ไม่เจอ: {a.workflow}")
        print("   ⇒ 'ไม่มีไฟล์ให้ตรวจ' ไม่ใช่ 'ตรวจแล้วสะอาด' ⇒ ด่านแดง")
        sys.exit(2)

    text = open(a.workflow, encoding='utf-8').read()
    bad, stat = check_text(text)
    print(f"ตรวจ {a.workflow} · พบ git add {stat['add']} บรรทัด"
          f" · git commit {stat['commit']} บรรทัด")
    print(f"  อนุญาตให้ add ได้เฉพาะ: {', '.join(ALLOWED_PATHS)}")
    print(f"  ⑨ ตัวหาร: คำสั่ง git ที่อ่านเจอ = {stat['add'] + stat['commit']} บรรทัด"
          " ⇒ ถ้าเป็น 0 แปลว่า “มองไม่เห็น” ⛔ ไม่ใช่ “สะอาด”")

    # 🔴 กับดัก ⑨ — ต้องอยู่ *ก่อน* การขึ้นเขียว
    why = divisor_hole(stat)
    if why is not None:
        print(f"\n  🔴 ด่านนี้ใช้ตัดสินไม่ได้ในรอบนี้: {why}")
        print(f"     ไฟล์ที่ชี้ให้ตรวจ: {a.workflow}")
        print("""
  เป็นไปได้สองทาง — และทั้งสองทางต้องมีคนตัดสินใจ ⛔ ไม่ใช่ปล่อยผ่าน:
    (ก) บอทไม่ commit อะไรแล้วจริง ⇒ ถอดด่านนี้ออกจาก guards.yml อย่างตั้งใจ
        พร้อมลบชื่อออกจากรายการที่ด่าน 11 เฝ้า (ไม่ใช่ทิ้งไว้ให้เขียวเปล่า ๆ)
    (ข) บอทยัง commit อยู่ แต่ผ่านทางที่ด่านนี้อ่านไม่เห็น
        (composite action · สคริปต์ที่ source มา · gh api · reusable workflow)
        ⇒ ด่านนี้กลายเป็นของประดับ · ต้องชี้ไปที่ไฟล์ที่มีคำสั่งจริง
          หรือขยายวิธีอ่านให้ครอบทางนั้น

  ⇒ รหัสออก 2 (เครื่องมือแดง) ไม่ใช่ 1 — ไฟล์ไม่ได้ผิดกฎ ตัวด่านต่างหากที่ตาบอด
""")
        sys.exit(2)

    if not bad:
        print("\n  ⇒ ✅ ผ่าน — บอทแตะได้แค่ไฟล์ที่ตกลงกันไว้")
        sys.exit(0)
    print("\n  🔴 ไม่ผ่าน:")
    for ln, seg, why in bad:
        print(f"     บรรทัด {ln}: {seg}")
        print(f"       ↳ {why}")
    print("""
  ── ทำไมกฎนี้ถึงมี (อ่านก่อนคิดจะปิดด่าน) ──────────────────────
  build-bank.yml เขียนได้เฉพาะ data/bank.json
  ถ้าเพิ่มไฟล์อื่นเข้าไปในคอมมิตของบอท คอมมิตนั้นจะไม่ผ่าน guards.yml
  เพราะ GitHub ไม่ re-trigger workflow ให้กับคอมมิตที่ push ด้วย GITHUB_TOKEN
  ⇒ จะมีคอมมิตอยู่ในสายหลักที่ "ไม่เคยผ่านด่านเลยสักครั้ง"
  ⇒ นี่ไม่ใช่กฎจุกจิกเรื่องความสะอาด — เป็นรูรั่วของด่านทั้งระบบ

  ถ้าจำเป็นต้องให้บอทเขียนไฟล์อื่นจริง ๆ ให้แก้ ALLOWED_PATHS ในไฟล์นี้
  พร้อมกันกับที่หาทางให้คอมมิตนั้นถูกตรวจ — ⛔ อย่าแก้ทางใดทางหนึ่งอย่างเดียว
""")
    sys.exit(1)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
flag_flawed_q119.py  -  E-lane (2026-09-18)

WHAT
  chap-09-vector-q119 ("คัดโอลิมปิก 2538") asks for the projection OC.
  choices[0] = 8/29 (12i+j) and choices[2] = 40/145 (12i+j) are THE SAME VALUE
  (40/145 = 8/29), so two options are correct. The key stays at index 2 (the book's
  answer). Teacher ruled 18 Sep 2026: flag it (real exam question => flag, never edit).
  Adds ONLY "flawedSource" (kind multiple-correct) to that one question in data/sets.
  The key, the choices, the explanation and notes are NOT touched. bank.json: bot rebuilds.

USAGE
  python flag_flawed_q119.py            dry-run (default)
  python flag_flawed_q119.py --apply    write (auto backup *.bak-flagq119-<stamp>, gitignored)

GATES (exit 2, nothing written)
  G1 repo root · G2 id found once · G3 no flag yet (identical flag => skip)
  G4 the defect is re-proved from the data: the two choices parse to the same fraction
     and the key still points at index 2 (no hard-coded trust)
  G5 flag passes scripts/check_flawed_source.py check_one()
  G6 file re-serialises byte-identical before edit
  G7 parsed diff = only "flawedSource" of that id
  G8 simulated build_bank(): only that flag differs from bank.json
  G9 (apply) backup md5 == original · re-read == intended bytes
"""
import argparse, hashlib, importlib.util, json, os, re, shutil, sys, tempfile
from datetime import datetime
from fractions import Fraction
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
QID = 'chap-09-vector-q119'
SET = 'chap-09-vector'
FLAG = {
    'kind': 'multiple-correct',
    'note': 'ตัวเลือก 1 คือ 8/29(12i+j) ซึ่งมีค่าเท่ากับตัวเลือก 3 คือ 40/145(12i+j) พอดี ⇒ มีตัวเลือกที่ถูกสองข้อ คีย์คงไว้ที่ข้อ 3 ตามเฉลยต้นฉบับ',
    'evidence': 'ครูอ๊อฟเคาะ 18 ก.ย. 2569 · E คำนวณซ้ำ: ภาพฉาย OC = (OA·OB/|OB|²)OB = (40/145)(12i+j) และ 40/145 = 8/29 (ตัดทอนด้วย 5) ⇒ ตัวเลือก 1 กับ 3 เป็นค่าเดียวกัน · ช่อง notes ของข้อนี้บันทึกความเท่ากันนี้ไว้ตั้งแต่ตอนนำเข้า · ต้นฉบับ "คัดโอลิมปิก 2538" เลือกข้อ 3',
    'decidedAt': '2026-09-18 · ครู QC',
}
FRAC = re.compile(r'\\[dt]?frac\{(\d+)\}\{(\d+)\}')


def die(m):
    print('STOP  ' + m)
    print('=> nothing written. exit 2')
    sys.exit(2)


def md5(b):
    return hashlib.md5(b).hexdigest()


def load_mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


KEYNAME = 'flawedSource'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--root', default=os.path.dirname(HERE))
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    print('flag_flawed_q119.py  mode=%s' % ('APPLY' if a.apply else 'DRY-RUN'))
    print('root = ' + root)
    p = os.path.join(root, 'data', 'sets', SET + '.json')
    bank_p = os.path.join(root, 'data', 'bank.json')
    man_p = os.path.join(root, 'data', 'manifest.json')
    bb_p = os.path.join(root, 'scripts', 'build_bank.py')
    cf_p = os.path.join(root, 'scripts', 'check_flawed_source.py')
    for x in (p, bank_p, man_p, bb_p, cf_p):
        if not os.path.exists(x):
            die('G1 missing: ' + x)
    print('G1 ok')

    raw = open(p, 'rb').read()
    d = json.loads(raw.decode('utf-8'))
    orig = json.loads(raw.decode('utf-8'))
    hits = [i for i, q in enumerate(d['questions']) if q.get('id') == QID]
    if len(hits) != 1:
        die('G2 %s found %d times' % (QID, len(hits)))
    q = d['questions'][hits[0]]
    print('G2 ok  %s at index %d' % (QID, hits[0]))

    if 'flawedSource' in q:
        if q['flawedSource'] == FLAG:
            print('G3 already flagged - nothing to do.')
            return 0
        die('G3 already has a different flawedSource: %r' % q['flawedSource'])
    print('G3 ok  not flagged yet')

    ch = q.get('choices') or []
    if q.get('correct') != 2 or len(ch) != 4:
        die('G4 expected correct=2 and 4 choices, got correct=%r len=%d' % (q.get('correct'), len(ch)))
    vals = []
    for c in ch:
        m = FRAC.search(c)
        vals.append(Fraction(int(m.group(1)), int(m.group(2))) if m else None)
    if None in vals:
        die('G4 cannot parse a fraction out of every choice: %r' % vals)
    same = [i for i, v in enumerate(vals) if v == vals[2]]
    if same != [0, 2]:
        die('G4 choices equal to the key are %s (expect [0, 2]) - values %s' % (same, vals))
    tail = [c[c.index(')') :] if ')' in c else c for c in ch]
    if len({re.sub(FRAC, '', c) for c in ch}) != 1:
        die('G4 the choices differ by more than the fraction - re-check by hand')
    print('G4 ok  choice1 = %s · choice3 = %s · equal ✓ · same vector part · key still index 2'
          % (vals[0], vals[2]))

    probs = load_mod('e_check_flawed', cf_p).check_one(FLAG)
    if probs:
        die('G5 flag fails gate 9: %s' % probs)
    print('G5 ok  flag passes gate 9 check_one()')

    for t in (b'', b'\n'):
        if json.dumps(d, ensure_ascii=False, indent=2).encode('utf-8') + t == raw:
            eol_tail = t
            break
    else:
        die('G6 %s.json does not re-serialise byte-identical' % SET)
    print('G6 ok  format check')

    new_q = {}
    for k, v in q.items():
        new_q[k] = v
        if k == 'id':
            new_q['flawedSource'] = FLAG
    q.clear()
    q.update(new_q)

    changed = 0
    for x, y in zip(orig['questions'], d['questions']):
        if x == y:
            continue
        if y['id'] != QID or {k: v for k, v in x.items() if k != 'flawedSource'} != \
                {k: v for k, v in y.items() if k != 'flawedSource'}:
            die('G7 unexpected change in %s' % y['id'])
        changed += 1
    if changed != 1 or len(orig['questions']) != len(d['questions']):
        die('G7 changed %d questions (expect 1)' % changed)
    print('G7 ok  only "flawedSource" of %s added' % QID)

    # ── G8 · เทียบ "build จาก sets ก่อนแก้" กับ "build จาก sets หลังแก้" ──
    #    ⛔ ไม่เทียบกับ bank.json เพราะ bank เป็นของที่บอทสร้าง จึงตามหลังเสมอ
    #       (ถ้าเทียบกับ bank สคริปต์จะหยุดผิดทันทีที่มีสคริปต์ตัวอื่นแก้ sets ไปก่อนในรอบเดียวกัน)
    man = json.load(open(man_p, encoding='utf-8'))
    bb = load_mod('e_build_bank', bb_p)

    def build(with_edit):
        tmp = tempfile.mkdtemp(prefix='e_sim_')
        try:
            os.makedirs(os.path.join(tmp, 'sets'))
            shutil.copy2(man_p, os.path.join(tmp, 'manifest.json'))
            for sid in man['sets']:
                src = os.path.join(root, 'data', 'sets', sid + '.json')
                if not os.path.exists(src):
                    continue
                dst = os.path.join(tmp, 'sets', sid + '.json')
                if sid == SET:
                    open(dst, 'wb').write(json.dumps(d if with_edit else orig,
                                                     ensure_ascii=False, indent=2).encode('utf-8') + eol_tail)
                else:
                    shutil.copy2(src, dst)
            return bb.build_bank(Path(tmp))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    before, after = build(False)['questions'], build(True)['questions']
    if len(before) != len(after):
        die('G8 question count changed %d -> %d' % (len(before), len(after)))
    dif = [y['id'] for x, y in zip(before, after) if x != y]
    if dif != [QID]:
        die('G8 rebuild differs at %s (expect only %s)' % (dif[:5], QID))
    q_after = next(z for z in after if z['id'] == QID)
    q_before = next(z for z in before if z['id'] == QID)
    if {k: v for k, v in q_before.items() if k != 'flawedSource'} != {k: v for k, v in q_after.items() if k != 'flawedSource'}:
        die('G8 rebuild changed something other than "%s"' % 'flawedSource')
    bank = json.load(open(bank_p, encoding='utf-8'))
    lag = [z['id'] for z in after
           if z != next((w for w in bank['questions'] if w['id'] == z['id']), None)]
    print('G8 ok  build(sets) ก่อน/หลัง ต่างกันเฉพาะ %s ที่คีย์ "%s"' % (QID, 'flawedSource'))
    print('     (bank.json ในเครื่องตามหลัง sets อยู่ %d ข้อ: %s — ปกติ จะตรงกันหลังบอท rebuild + Pull)'
          % (len(lag), lag[:6]))

    if not a.apply:
        print('\nDRY-RUN finished. nothing written.')
        print('to write:  python "%s" --apply' % os.path.abspath(__file__))
        return 0

    cur = open(p, 'rb').read()
    if cur != raw:
        die('G9 file changed on disk during run')
    stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    bak = p + '.bak-flagq119-' + stamp
    if os.path.exists(bak):
        die('G9 backup exists')
    shutil.copy2(p, bak)
    if md5(open(bak, 'rb').read()) != md5(cur):
        die('G9 backup md5 mismatch')
    new = json.dumps(d, ensure_ascii=False, indent=2).encode('utf-8') + eol_tail
    with open(p, 'wb') as f:
        f.write(new)
    if open(p, 'rb').read() != new:
        print('STOP  G9 re-read mismatch - restore from ' + bak)
        sys.exit(2)
    print('WROTE %s.json  md5 %s -> %s  backup %s' % (SET, md5(cur)[:8], md5(new)[:8], os.path.basename(bak)))
    print('\nAPPLY finished. key/choices/explanation untouched. bank.json untouched.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:
        print('TOOL ERROR  %s: %s' % (type(e).__name__, e))
        sys.exit(2)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_imagespec_q44.py  -  E-lane (2026-09-18)

WHAT
  pat1-2564-03-q44: the picture marks (5,3) as "ไกลสุด" but (5,3) is the NEAREST point
  on the circle to (8,7); the farthest point is (-1,-5).  The answer 15 and the whole
  explanation text are correct - only imageSpec is wrong.
      circle  centre (2,-1)  r = 5 ·  d((8,7),(2,-1)) = 10
      farthest = centre + 5*unit((2,-1)-(8,7)) = (2,-1) + 5*(-0.6,-0.8) = (-1,-5) · 10+5 = 15
      nearest  = (5,3) · 10-5 = 5
  Fix (data only, data/sets):
      green point   (5,3) "ไกลสุด (5,3) → 15"  ->  (-1,-5) "ไกลสุด (−1,−5) → 15"
      green segment (2,-1)->(5,3)              ->  (2,-1)->(-1,-5)
  Touches ONLY those two places of that one question. bank.json is rebuilt by the bot.

USAGE
  python fix_imagespec_q44.py            dry-run (default)
  python fix_imagespec_q44.py --apply    write (auto backup *.bak-q44img-<stamp>, gitignored)

GATES (exit 2, nothing written)
  G1 repo root · G2 id found once · G3 the exact old values are there (else: already fixed / changed)
  G4 geometry re-derived from the question's own numbers matches the new point (no hard-coded trust)
  G5 file re-serialises byte-identical before edit
  G6 parsed diff = only that question's imageSpec · only the point and the segment
  G7 simulated build_bank(): only that imageSpec differs from bank.json
  G8 (apply) backup md5 == original · re-read == intended bytes
"""
import argparse, hashlib, importlib.util, json, math, os, shutil, sys, tempfile
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
QID = 'pat1-2564-03-q44'
SET = 'pat1-2564-03'
OLD_LABEL = 'ไกลสุด (5,3) → 15'
NEW_LABEL = 'ไกลสุด (−1,−5) → 15'
CENTRE, R, OUTSIDE = (2.0, -1.0), 5.0, (8.0, 7.0)


def load_mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def die(m):
    print('STOP  ' + m)
    print('=> nothing written. exit 2')
    sys.exit(2)


def md5(b):
    return hashlib.md5(b).hexdigest()


KEYNAME = 'imageSpec'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--root', default=os.path.dirname(HERE))
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    print('fix_imagespec_q44.py  mode=%s' % ('APPLY' if a.apply else 'DRY-RUN'))
    print('root = ' + root)
    p = os.path.join(root, 'data', 'sets', SET + '.json')
    bank_p = os.path.join(root, 'data', 'bank.json')
    bb_p = os.path.join(root, 'scripts', 'build_bank.py')
    man_p = os.path.join(root, 'data', 'manifest.json')
    for x in (p, bank_p, bb_p, man_p):
        if not os.path.exists(x):
            die('G1 missing: ' + x)
    print('G1 ok')

    raw = open(p, 'rb').read()
    d = json.loads(raw.decode('utf-8'))
    hits = [i for i, q in enumerate(d['questions']) if q.get('id') == QID]
    if len(hits) != 1:
        die('G2 %s found %d times' % (QID, len(hits)))
    k = hits[0]
    orig = json.loads(raw.decode('utf-8'))
    q = d['questions'][k]
    print('G2 ok  %s at index %d' % (QID, k))

    for tail in (b'', b'\n'):
        if json.dumps(d, ensure_ascii=False, indent=2).encode('utf-8') + tail == raw:
            eol_tail = tail
            break
    else:
        die('G5 %s.json does not re-serialise byte-identical' % SET)
    print('G5 ok  format check')

    spec = q.get('imageSpec')
    if not isinstance(spec, list) or len(spec) != 1:
        die('G3 unexpected imageSpec shape')
    fig = spec[0]
    pts = [x for x in fig.get('points', []) if x.get('label') == OLD_LABEL]
    segs = [s for s in fig.get('segments', []) if s.get('to') == [5, 3]]
    if len(pts) != 1 or len(segs) != 1:
        die('G3 expected 1 point %r and 1 segment ending [5,3]; found %d / %d (already fixed?)' % (OLD_LABEL, len(pts), len(segs)))
    pt, seg = pts[0], segs[0]
    if [pt.get('re'), pt.get('im')] != [5, 3] or seg.get('from') != [2, -1]:
        die('G3 point/segment coordinates are not the expected ones')
    print('G3 ok  found the wrong label + segment')

    # G4 re-derive geometry from the circle in the same imageSpec
    circ = fig['circles'][0]
    if [float(x) for x in circ['center']] != list(CENTRE) or float(circ['r']) != R:
        die('G4 circle in imageSpec is not centre %s r %s' % (CENTRE, R))
    dx, dy = CENTRE[0] - OUTSIDE[0], CENTRE[1] - OUTSIDE[1]
    dist = math.hypot(dx, dy)
    far = (CENTRE[0] + R * dx / dist, CENTRE[1] + R * dy / dist)
    near = (CENTRE[0] - R * dx / dist, CENTRE[1] - R * dy / dist)
    if abs(far[0] + 1) > 1e-9 or abs(far[1] + 5) > 1e-9 or abs(near[0] - 5) > 1e-9 or abs(near[1] - 3) > 1e-9:
        die('G4 derived farthest %s nearest %s - not (-1,-5)/(5,3)' % (far, near))
    print('G4 ok  farthest=(-1,-5) dist %.0f · nearest=(5,3) dist %.0f  (derived, not assumed)'
          % (dist + R, dist - R))

    pt['re'], pt['im'], pt['label'] = -1, -5, NEW_LABEL
    seg['to'] = [-1, -5]
    print('     point   (5,3) %r  ->  (-1,-5) %r' % (OLD_LABEL, NEW_LABEL))
    print('     segment (2,-1)->(5,3)  ->  (2,-1)->(-1,-5)')

    A, B = orig['questions'], d['questions']
    if len(A) != len(B):
        die('G6 structure changed')
    changed = 0
    for x, y in zip(A, B):
        if x == y:
            continue
        if y['id'] != QID or {kk: vv for kk, vv in x.items() if kk != 'imageSpec'} != \
                {kk: vv for kk, vv in y.items() if kk != 'imageSpec'}:
            die('G6 unexpected change in %s' % y['id'])
        changed += 1
    if changed != 1:
        die('G6 changed %d questions (expect 1)' % changed)
    print('G6 ok  only imageSpec of %s changed' % QID)

    # ── G7 · เทียบ "build จาก sets ก่อนแก้" กับ "build จาก sets หลังแก้" ──
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
        die('G7 question count changed %d -> %d' % (len(before), len(after)))
    dif = [y['id'] for x, y in zip(before, after) if x != y]
    if dif != [QID]:
        die('G7 rebuild differs at %s (expect only %s)' % (dif[:5], QID))
    q_after = next(z for z in after if z['id'] == QID)
    q_before = next(z for z in before if z['id'] == QID)
    if {k: v for k, v in q_before.items() if k != 'imageSpec'} != {k: v for k, v in q_after.items() if k != 'imageSpec'}:
        die('G7 rebuild changed something other than "%s"' % 'imageSpec')
    bank = json.load(open(bank_p, encoding='utf-8'))
    lag = [z['id'] for z in after
           if z != next((w for w in bank['questions'] if w['id'] == z['id']), None)]
    print('G7 ok  build(sets) ก่อน/หลัง ต่างกันเฉพาะ %s ที่คีย์ "%s"' % (QID, 'imageSpec'))
    print('     (bank.json ในเครื่องตามหลัง sets อยู่ %d ข้อ: %s — ปกติ จะตรงกันหลังบอท rebuild + Pull)'
          % (len(lag), lag[:6]))

    if not a.apply:
        print('\nDRY-RUN finished. nothing written.')
        print('to write:  python "%s" --apply' % os.path.abspath(__file__))
        return 0

    cur = open(p, 'rb').read()
    if cur != raw:
        die('G8 file changed on disk during run')
    stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    bak = p + '.bak-q44img-' + stamp
    if os.path.exists(bak):
        die('G8 backup exists')
    shutil.copy2(p, bak)
    if md5(open(bak, 'rb').read()) != md5(cur):
        die('G8 backup md5 mismatch')
    new = json.dumps(d, ensure_ascii=False, indent=2).encode('utf-8') + eol_tail
    with open(p, 'wb') as f:
        f.write(new)
    if open(p, 'rb').read() != new:
        print('STOP  G8 re-read mismatch - restore from ' + bak)
        sys.exit(2)
    print('WROTE %s.json  md5 %s -> %s  backup %s' % (SET, md5(cur)[:8], md5(new)[:8], os.path.basename(bak)))
    print('\nAPPLY finished. bank.json untouched (bot rebuilds it).')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:
        print('TOOL ERROR  %s: %s' % (type(e).__name__, e))
        sys.exit(2)

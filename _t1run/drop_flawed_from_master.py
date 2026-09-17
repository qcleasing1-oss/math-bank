#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
drop_flawed_from_master.py  -  E-lane (2026-09-17)

WHAT
  Removes from _t1run/results/t1_MASTER.json every t1 solution whose question is
  "flawed with no key" in data/sets  (flawedSource present AND correct is null).
  Same rule as the 4 items the teacher excluded before t1 ran.
  Questions that are flagged but still HAVE a key (e.g. q140, q73) are kept.

  !! tools/merge_master.py (repo code, E does not touch it) has no such filter.
     tools/daily_sync.py re-runs merge_master => the dropped solutions COME BACK.
     => run this script again after every merge / daily sync
        (or use --check: exit 1 if any flawed solution is in MASTER)
     until CC adds the filter to merge_master.py.

USAGE
  python drop_flawed_from_master.py            dry-run (default)
  python drop_flawed_from_master.py --apply    write (auto backup *.bak-dropflawed-<stamp>, gitignored)
  python drop_flawed_from_master.py --check    report only, exit 1 if something would be dropped

RUN ORDER: flag_flawed_sources.py --apply FIRST (this script reads the flags from data/sets).

GATES (exit 2, nothing written)
  G1 paths · G2 the 6 ids decided on 17 Sep carry a no-key flag in data/sets (else: run flag script first)
  G3 MASTER is a list of records with unique ids · re-serialises byte-identical (indent=1, CRLF/LF kept)
  G4 result = before - dropped · no other record changed · order kept
  G5 (apply) backup md5 == original · re-read parses and has the expected ids
exit: 0 ok | 1 (--check) flawed solutions present | 2 stop
"""
import argparse, hashlib, json, os, shutil, sys
from datetime import datetime

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
HERE = os.path.dirname(os.path.abspath(__file__))
DECIDED_0917 = ['pat1-2564-03-q34', 'pat1-2564-03-q35', 'chap-07-trigonometry-q162',
                'chap-07-trigonometry-q23', 'chap-07-trigonometry-q45', 'pat1-2554-03-q49']


def die(m):
    print('STOP  ' + m)
    print('=> nothing written. exit 2')
    sys.exit(2)


def md5(b):
    return hashlib.md5(b).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group()
    g.add_argument('--apply', action='store_true')
    g.add_argument('--check', action='store_true')
    ap.add_argument('--root', default=os.path.dirname(HERE))
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    mode = 'APPLY' if a.apply else ('CHECK' if a.check else 'DRY-RUN')
    print('drop_flawed_from_master.py  mode=%s' % mode)
    man_p = os.path.join(root, 'data', 'manifest.json')
    sets_d = os.path.join(root, 'data', 'sets')
    mas_p = os.path.join(root, '_t1run', 'results', 't1_MASTER.json')
    for p in (man_p, sets_d, mas_p):
        if not os.path.exists(p):
            die('G1 missing: ' + p)
    print('G1 ok  ' + mas_p)

    man = json.load(open(man_p, encoding='utf-8'))
    drop, kept_flagged = {}, []
    for sid in man['sets']:
        p = os.path.join(sets_d, sid + '.json')
        if not os.path.exists(p):
            continue
        for q in json.load(open(p, encoding='utf-8'))['questions']:
            fs = q.get('flawedSource')
            if not fs:
                continue
            if q.get('correct') is None:
                drop[q['id']] = fs.get('kind')
            else:
                kept_flagged.append(q['id'])
    missing = [i for i in DECIDED_0917 if i not in drop]
    if missing:
        die('G2 not flagged in data/sets yet: %s  => run flag_flawed_sources.py --apply first' % missing)
    print('G2 ok  flawed & no key in data/sets: %d  (flagged but keyed, kept: %s)' % (len(drop), kept_flagged))

    raw = open(mas_p, 'rb').read()
    m = json.loads(raw.decode('utf-8'))
    if not isinstance(m, list) or not all(isinstance(r, dict) and 'id' in r for r in m):
        die('G3 MASTER is not a list of records')
    ids = [r['id'] for r in m]
    if len(set(ids)) != len(ids):
        die('G3 MASTER has duplicate ids')
    # merge_master.py writes in text mode => CRLF on Windows. Keep whatever is on disk.
    #   (JSON strings never contain raw newlines, so swapping line breaks is safe)
    eol = b'\r\n' if b'\r\n' in raw[:200] else b'\n'
    def ser(obj):
        return json.dumps(obj, ensure_ascii=False, indent=1).encode('utf-8').replace(b'\n', eol)
    if ser(m) != raw:
        die('G3 MASTER does not re-serialise byte-identical (indent=1, %s) - refuse to write' % ('CRLF' if eol == b'\r\n' else 'LF'))
    print('G3 ok  MASTER %d records, unique, format ok (indent=1, %s)' % (len(m), 'CRLF' if eol == b'\r\n' else 'LF'))

    hit = [i for i in ids if i in drop]
    new = [r for r in m if r['id'] not in drop]
    print('     to drop from MASTER: %d' % len(hit))
    for i in hit:
        print('       %-28s %s' % (i, drop[i]))
    if len(new) != len(m) - len(hit) or [r['id'] for r in new] != [i for i in ids if i not in drop]:
        die('G4 result mismatch')
    print('G4 ok  MASTER %d -> %d' % (len(m), len(new)))

    if a.check:
        print('CHECK: %s' % ('clean' if not hit else '%d flawed solutions present -> run with --apply' % len(hit)))
        return 1 if hit else 0
    if not a.apply:
        print('\nDRY-RUN finished. nothing written.')
        return 0
    if not hit:
        print('\nnothing to drop. nothing written.')
        return 0
    stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    bak = mas_p + '.bak-dropflawed-' + stamp
    if os.path.exists(bak):
        die('G5 backup exists')
    shutil.copy2(mas_p, bak)
    if md5(open(bak, 'rb').read()) != md5(raw):
        die('G5 backup md5 mismatch')
    out = ser(new)
    with open(mas_p, 'wb') as f:
        f.write(out)
    back = json.loads(open(mas_p, 'rb').read().decode('utf-8'))
    if [r['id'] for r in back] != [r['id'] for r in new]:
        print('STOP  G5 re-read mismatch - restore from ' + bak)
        sys.exit(2)
    print('WROTE t1_MASTER.json  %d -> %d records  md5 %s -> %s  backup %s' %
          (len(m), len(new), md5(raw)[:8], md5(out)[:8], os.path.basename(bak)))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:
        print('TOOL ERROR  %s: %s' % (type(e).__name__, e))
        sys.exit(2)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_keys_to_sets.py  -  E-lane (2026-09-17)

WHY
  apply_nokey_keys.py wrote 21 keys into data/bank.json only.
  bank.json is DERIVED: build-bank.yml rebuilds it from data/sets/*.json on every
  push that touches data/sets. data/sets has none of the 21 keys
  => the next rebuild would silently drop all of them.
  This script writes the same keys into data/sets (the source of truth).

WHAT
  - fill items : add "correct": "<value>" + "accept": [...] right after "answer"
                 (house style of 974 fill items: correct -> accept -> explanation;
                  accept = key + equivalents: integer N -> ["N","N.0"],
                  decimal with a short fraction -> [dec, "p/q", "\\dfrac{p}{q}"])
                 WHY accept: CI gate 18 (check_fill_answer --enforce-declared) is RED for a
                 changed fill item without accept - measured on a copy 17 Sep.
  - mc item q34: NEVER (teacher 17 Sep 2026: exam question is wrong, flagged flawedSource)
  - touches ONLY keys "correct"/"accept" of the listed ids. Nothing else. bank.json is NOT touched.

USAGE (run from anywhere)
  python apply_keys_to_sets.py                 dry-run (default) - writes nothing
  python apply_keys_to_sets.py --apply         write data/sets (auto backup first)
  --include-q34  CLOSED (17 Sep 2026: teacher ruled q34 a wrong exam question) -> STOP

GATES (any failure => exit 2, nothing written)
  G1 repo root looks right (manifest, sets, scripts/build_bank.py)
  G2 PROPOSED_KEYS.json: exactly 21 records, all t1_agrees=True, ids unique
  G3 value to write == bank.json current "correct" == proposed_correct (all three agree)
  G4 each id found exactly once in data/sets (manifest order)
  G5 current sets value is absent/null (already equal => skip, idempotent; other value => STOP)
  G6 fill: sets "answer" == value to write  |  mc: value is int and in range of choices
  G7 no id carries flawedSource, none is in the 4 teacher-closed ids
  G8 each touched file re-serialises byte-identical BEFORE edit (format check)
  G9 after edit: parsed diff = only "correct"/"accept" of listed ids changed
  G10 simulated build_bank() from edited sets == current bank.json questions
       apart from the new "accept" (and q34 when excluded) => bot rebuild keeps the keys
  G11 (apply) backup md5 == original, re-read written file == intended bytes

exit: 0 ok | 2 gate failed / tool error
"""
import argparse, hashlib, re, importlib.util, json, os, sys, tempfile, shutil
from datetime import datetime

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
Q34 = 'pat1-2564-03-q34'
CLOSED = {'pat1-2555-10-q15', 'pat1-2552-10-q17', 'pat1-2558-10-q37', 'chap-14-infiniteseries-q43',
          # teacher 17 Sep 2026: exam itself wrong -> never gets a key (q34 was the pending one)
          'pat1-2564-03-q34', 'pat1-2564-03-q35', 'chap-07-trigonometry-q162',
          'chap-07-trigonometry-q23', 'chap-07-trigonometry-q45', 'pat1-2554-03-q49'}
EXPECT_N = 21


def die(msg):
    print('STOP  ' + msg)
    print('=> nothing written. exit 2')
    sys.exit(2)


def dumps(obj):
    # data/sets format: indent=2, ensure_ascii=False, LF, NO trailing newline (measured 17 Sep)
    return json.dumps(obj, ensure_ascii=False, indent=2).encode('utf-8')


def make_accept(v):
    s = str(v)
    if re.fullmatch(r'-?\d+', s):
        return [s, s + '.0']
    if re.fullmatch(r'-?\d+\.\d+', s):
        from fractions import Fraction
        f = Fraction(s)
        out = [s]
        if f.denominator <= 100:
            n, d = f.numerator, f.denominator
            out += ['%d/%d' % (n, d), ('-' if n < 0 else '') + '\\dfrac{%d}{%d}' % (abs(n), d)]
        return out
    return None


def insert_after(q, after, items):
    out = {}
    for k, v in q.items():
        if k in items:
            continue
        out[k] = v
        if k == after:
            out.update(items)
    if after not in q:
        out.update(items)
    q.clear()
    q.update(out)


def md5(b):
    return hashlib.md5(b).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--include-q34', action='store_true')
    ap.add_argument('--root', default=os.path.dirname(HERE), help='repo root (default: parent of _t1run)')
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    mode = 'APPLY' if a.apply else 'DRY-RUN'
    print('apply_keys_to_sets.py  mode=%s  include_q34=%s' % (mode, a.include_q34))
    print('root = ' + root)

    # G1
    man_p = os.path.join(root, 'data', 'manifest.json')
    sets_d = os.path.join(root, 'data', 'sets')
    bank_p = os.path.join(root, 'data', 'bank.json')
    bb_p = os.path.join(root, 'scripts', 'build_bank.py')
    pk_p = os.path.join(HERE, 'PROPOSED_KEYS.json')
    for p in (man_p, sets_d, bank_p, bb_p, pk_p):
        if not os.path.exists(p):
            die('G1 missing: ' + p)
    print('G1 ok  repo root')

    # G2
    pk = json.load(open(pk_p, encoding='utf-8'))
    ids = [r['id'] for r in pk]
    if len(pk) != EXPECT_N or len(set(ids)) != EXPECT_N:
        die('G2 PROPOSED_KEYS has %d records / %d unique (expect %d)' % (len(pk), len(set(ids)), EXPECT_N))
    if not all(r.get('t1_agrees') is True for r in pk):
        die('G2 some record has t1_agrees != True')
    print('G2 ok  %d proposed keys, all blind==t1' % len(pk))

    if a.include_q34:
        die('--include-q34 is closed: teacher ruled q34 a wrong exam question (17 Sep 2026)')
    targets = {r['id']: r for r in pk if r['id'] != Q34}
    if not a.include_q34:
        print('     q34 EXCLUDED (pending teacher) -> %d ids' % len(targets))

    # G3
    bank = json.load(open(bank_p, encoding='utf-8'))
    bq = {q['id']: q for q in bank['questions']}
    want = {}
    for i, r in targets.items():
        if i not in bq:
            die('G3 %s not in bank.json' % i)
        bv = bq[i].get('correct')
        if bv is None or str(bv) != str(r['proposed_correct']):
            die('G3 %s bank.correct=%r != proposed=%r' % (i, bv, r['proposed_correct']))
        want[i] = bv  # exact value + type as already in bank.json
    print('G3 ok  bank.json == proposed for all %d' % len(want))

    # G4
    man = json.load(open(man_p, encoding='utf-8'))
    where = {}
    raw = {}
    data = {}
    for sid in man['sets']:
        p = os.path.join(sets_d, sid + '.json')
        if not os.path.exists(p):
            continue
        b = open(p, 'rb').read()
        d = json.loads(b.decode('utf-8'))
        for k, q in enumerate(d['questions']):
            if q.get('id') in want:
                where.setdefault(q['id'], []).append((sid, k))
                raw[sid] = b
                data[sid] = d
    for i in want:
        n = len(where.get(i, []))
        if n != 1:
            die('G4 %s found %d times in data/sets (expect 1)' % (i, n))
    print('G4 ok  every id found once, in %d set file(s): %s' % (len(data), ', '.join(sorted(data))))

    # G8 (before editing)
    for sid, b in raw.items():
        if dumps(data[sid]) != b:
            die('G8 %s.json does not re-serialise byte-identical -> format unknown, refuse to write' % sid)
    print('G8 ok  format check (indent=2, LF, no trailing newline)')

    orig = {sid: json.loads(b.decode('utf-8')) for sid, b in raw.items()}
    todo, skip = [], []
    expect_acc = {}
    for i, v in sorted(want.items()):
        sid, k = where[i][0]
        q = data[sid]['questions'][k]
        # G7
        if i in CLOSED or q.get('flawedSource'):
            die('G7 %s is flawed/closed - must not get a key' % i)
        acc = make_accept(v) if q.get('type') == 'fill' else None
        if acc:
            expect_acc[i] = acc
        # G5
        cur = q.get('correct', None)
        if cur is not None:
            if cur == v and type(cur) == type(v) and q.get('accept') == acc:
                skip.append(i)
                continue
            die('G5 %s sets already has correct=%r accept=%r (want %r %r) - stop' % (i, cur, q.get('accept'), v, acc))
        if 'accept' in q:
            die('G5 %s sets already has accept=%r without a key - stop' % (i, q['accept']))
        # G6
        if q.get('type') == 'fill':
            if str(q.get('answer')) != str(v):
                die('G6 %s fill: sets.answer=%r != %r' % (i, q.get('answer'), v))
            if not acc or len(set(acc)) != len(acc) or acc[0] != str(v):
                die('G6 %s cannot build accept for %r' % (i, v))
        elif q.get('type') == 'mc':
            ch = q.get('choices') or []
            if not isinstance(v, int) or not (0 <= v < len(ch) or 1 <= v <= len(ch)):
                die('G6 %s mc: correct=%r not valid for %d choices' % (i, v, len(ch)))
        else:
            die('G6 %s unexpected type %r' % (i, q.get('type')))
        if q.get('type') == 'fill':
            insert_after(q, 'answer', {'correct': v, 'accept': acc})
        else:
            q['correct'] = v            # mc: key exists (null) -> replace in place
        todo.append((i, sid, q.get('type'), v, acc))
    print('G5/G6/G7 ok  to write %d · already done %d' % (len(todo), len(skip)))
    for i, sid, t, v, acc in todo:
        print('     %-26s %-4s correct=%-8r accept=%s   (%s.json)' % (i, t, v, acc, sid))

    # G9
    changed = 0
    for sid in data:
        a_q, b_q = orig[sid]['questions'], data[sid]['questions']
        if len(a_q) != len(b_q) or {k: v for k, v in orig[sid].items() if k != 'questions'} != \
                {k: v for k, v in data[sid].items() if k != 'questions'}:
            die('G9 %s structure changed' % sid)
        for x, y in zip(a_q, b_q):
            if x == y:
                continue
            xs = {k: v for k, v in x.items() if k not in ('correct', 'accept')}
            ys = {k: v for k, v in y.items() if k not in ('correct', 'accept')}
            if xs != ys or y['id'] not in want:
                die('G9 unexpected change in %s' % y.get('id'))
            changed += 1
    if changed != len(todo):
        die('G9 changed %d != planned %d' % (changed, len(todo)))
    print('G9 ok  only "correct"/"accept" of %d ids changed' % changed)

    # G10 simulated bot rebuild (temp dir, build_bank.build_bank imported read-only)
    tmp = tempfile.mkdtemp(prefix='e_keys_')
    try:
        os.makedirs(os.path.join(tmp, 'sets'))
        shutil.copy2(man_p, os.path.join(tmp, 'manifest.json'))
        for sid in man['sets']:
            src = os.path.join(sets_d, sid + '.json')
            if not os.path.exists(src):
                continue
            dst = os.path.join(tmp, 'sets', sid + '.json')
            if sid in data:
                open(dst, 'wb').write(dumps(data[sid]))
            else:
                shutil.copy2(src, dst)
        spec = importlib.util.spec_from_file_location('e_build_bank', bb_p)
        mod = importlib.util.module_from_spec(spec)
        sys.dont_write_bytecode = True
        spec.loader.exec_module(mod)
        from pathlib import Path
        sim = mod.build_bank(Path(tmp))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    sq = sim['questions']
    if len(sq) != len(bank['questions']):
        die('G10 simulated build has %d questions, bank.json has %d' % (len(sq), len(bank['questions'])))
    newacc = expect_acc                      # includes ids already done (idempotent rerun)
    def strip(q):
        # flawedSource is ignored: flags live in data/sets first, bank.json catches up on the bot rebuild
        return {k: v for k, v in q.items() if not (k == 'accept' and q['id'] in newacc) and k != 'flawedSource'}
    diff = [y['id'] for x, y in zip(bank['questions'], sq) if strip(x) != strip(y)]
    allowed = set() if a.include_q34 else {Q34}
    extra = [d for d in diff if d not in allowed]
    for q in sq:
        if q['id'] in newacc and q.get('accept') != newacc[q['id']]:
            die('G10 accept of %s lost in simulated rebuild' % q['id'])
    if extra:
        die('G10 rebuilt bank would differ from current bank.json at %d ids: %s' % (len(extra), extra[:10]))
    keys_ok = sum(1 for q in sq if q['id'] in want and q.get('correct') == want[q['id']])
    if keys_ok != len(want):
        die('G10 only %d/%d keys survive simulated rebuild' % (keys_ok, len(want)))
    nokey = [q['id'] for q in sq if q.get('correct') is None and not q.get('retired')]
    print('G10 ok  simulated rebuild: %d/%d keys kept · +accept on %d ids · other differences: %s' %
          (keys_ok, len(want), len(newacc), diff or 'none'))
    print('     no-key after rebuild: %d  %s' % (len(nokey), nokey))

    if not a.apply:
        print('\nDRY-RUN finished. nothing written.')
        print('to write:  python "%s" --apply%s' % (os.path.abspath(__file__), ' --include-q34' if a.include_q34 else ''))
        return 0

    # G11 write
    stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    for sid in sorted({s for _, s, _, _, _ in todo}):
        p = os.path.join(sets_d, sid + '.json')
        cur = open(p, 'rb').read()
        if cur != raw[sid]:
            die('G11 %s.json changed on disk during run' % sid)
        bak = p + '.bak-setkeys-' + stamp          # *.bak-* is gitignored
        if os.path.exists(bak):
            die('G11 backup exists: ' + bak)
        shutil.copy2(p, bak)
        if md5(open(bak, 'rb').read()) != md5(cur):
            die('G11 backup md5 mismatch: ' + bak)
        new = dumps(data[sid])
        with open(p, 'wb') as f:
            f.write(new)
        if open(p, 'rb').read() != new:
            print('STOP  G11 re-read mismatch %s - restore from %s' % (p, bak))
            sys.exit(2)
        print('WROTE %s.json  md5 %s -> %s  backup %s' % (sid, md5(cur)[:8], md5(new)[:8], os.path.basename(bak)))
    print('\nAPPLY finished: %d keys written to data/sets. bank.json untouched.' % len(todo))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:
        print('TOOL ERROR  %s: %s' % (type(e).__name__, e))
        sys.exit(2)

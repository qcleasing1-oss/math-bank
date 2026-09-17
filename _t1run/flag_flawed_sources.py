#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
flag_flawed_sources.py  -  E-lane (2026-09-17)

WHAT
  Adds a "flawedSource" flag (gate-9 spec: kind/note/evidence/decidedAt) to the 6
  questions the teacher ruled "the exam itself is wrong" on 17 Sep 2026.
  Writes data/sets only (source of truth). bank.json is rebuilt by the bot.
  Key placement: right after "id" (same as the 12 Sep flag script).
  Touches ONLY the key "flawedSource" of these 6 ids. "correct" stays null.

USAGE
  python flag_flawed_sources.py            dry-run (default) - writes nothing
  python flag_flawed_sources.py --apply    write (auto backup *.bak-flag-<stamp>, gitignored)

GATES (any failure => exit 2, nothing written)
  G1 repo root
  G2 each id found exactly once in data/sets (manifest order)
  G3 correct is null (and fill answer is null) - flag is only for "no usable key"
  G4 no flag yet (identical flag => skip, different flag => STOP)
  G5 each flag passes scripts/check_flawed_source.py check_one() (imported read-only)
  G6 touched files re-serialise byte-identical before edit
  G7 parsed diff = only "flawedSource" of the 6 ids
  G8 simulated build_bank(): vs current bank.json only the 6 flags differ
  G9 (apply) backup md5 == original · re-read == intended bytes
exit: 0 ok | 2 stop
"""
import argparse, hashlib, importlib.util, json, os, shutil, sys, tempfile
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
DECIDED = '2026-09-17 · ครู QC'

FLAGS = {
    'pat1-2564-03-q34': {
        'kind': 'no-correct',
        'note': 'โจทย์กำหนดให้ช่วงกลางรถไฟเคลื่อนที่ด้วยความเร็วคงตัว (ความเร่ง = 0) แต่กราฟช่วงกลางให้ความเร่ง = A ⇒ ข้อมูลขัดกันเอง จึงไม่มีตัวเลือกใดถูก',
        'evidence': 'เฉลยต้นฉบับ PAT 1 (มี.ค. 64) หน้า 41 ระบุ «ตอบ -» และ «ข้อนี้โจทย์ผิด» (ครูแนบภาพในแชท 17 ก.ย. 2569) · ช่วงความเร็วคงตัวต้องมีความเร่ง 0 ขัดกับกราฟที่ความเร่งคงที่ A',
    },
    'pat1-2564-03-q35': {
        'kind': 'no-correct',
        'note': 'ใช้สถานการณ์เดียวกับข้อ 34 ซึ่งคำบรรยาย (ช่วงกลางความเร็วคงตัว) ขัดกับกราฟ (ช่วงกลางความเร่ง = A) ⇒ หาเวลาเดินทางรวมที่สอดคล้องทุกเงื่อนไขไม่ได้ จึงไม่มีตัวเลือกใดถูก',
        'evidence': 'เฉลยต้นฉบับ PAT 1 (มี.ค. 64) ข้อ 35 ระบุ «ตอบ -» และ «ข้อนี้โจทย์ผิด» (ครูแนบภาพในแชท 17 ก.ย. 2569) · ใช้กราฟและสถานการณ์เดียวกับข้อ 34 ที่ครูเคาะว่าโจทย์ผิดในวันเดียวกัน',
    },
    'chap-07-trigonometry-q162': {
        'kind': 'no-correct',
        'note': 'นิพจน์เท่ากับ tan(160° − 100°) = tan 60° = √3 ซึ่งเป็นค่าคงตัว ไม่ขึ้นกับ a และไม่ตรงกับตัวเลือกใดทั้ง 5 ข้อ',
        'evidence': 'เฉลยต้นฉบับ (ทุนเล่าเรียนหลวง กพ. 2542 ข้อ 162) สรุป «ตอบ ไม่มีข้อใดถูก» (ครูแนบภาพในแชท 17 ก.ย. 2569) · E คำนวณเชิงตัวเลข 17 ก.ย.: นิพจน์ = 1.7320508 ส่วนตัวเลือกทั้ง 5 = 1, 0.5774, 1.1918, −1.1918, 1.5557',
    },
    'chap-07-trigonometry-q23': {
        'kind': 'no-correct',
        'note': 'รากของสมการในช่วง [0, 2π] คือ π/6, 5π/6 และ 3π/2 ไม่มีช่วงในตัวเลือกใดบรรจุครบทั้งสามค่า',
        'evidence': 'เฉลยต้นฉบับ (ข้อสอบเข้ามหาวิทยาลัย 2534 ข้อ 23) สรุป «ตอบ ไม่มีข้อใดถูก» (ครูแนบภาพในแชท 17 ก.ย. 2569) · ให้ A = √(2sin²x + sin x) ได้ (A − 1)² = 0 ⇒ sin x = 1/2 หรือ −1 · แทนค่ากลับครบทั้งสามราก',
    },
    'chap-07-trigonometry-q45': {
        'kind': 'multiple-correct',
        'note': 'โจทย์ถามว่าประโยคในข้อใดไม่จริง แต่มีประโยคที่ไม่จริง 2 ข้อ คือตัวเลือก 1 และตัวเลือก 5 จึงตอบได้มากกว่าหนึ่งข้อ',
        'evidence': 'เฉลยท้ายหน้า 9 ของต้นฉบับระบุ «45. 1, 5» (สองคำตอบ) · E ตรวจเชิงตัวเลข 17 ก.ย. (A = 0.7): ตัวเลือก 1 ซ้าย = −0.0856 แต่ sec2A − tan2A = +0.0856 · ตัวเลือก 5 sec²A = 1.7094 แต่ 2cot2A·tanA = 0.2906 · ตัวเลือก 2, 3, 4 จริง',
    },
    'pat1-2554-03-q49': {
        'kind': 'no-correct',
        'note': 'เงื่อนไข x*d = x ทุก x บังคับ a = 0, b = 0, cd = 1 แล้ว 1*2 = 3 ให้ c = 3/2 แต่ 2*3 = 4 ให้ c = 2/3 ขัดกันเอง จึงไม่มีค่าที่สอดคล้องทุกเงื่อนไข',
        'evidence': 'เฉลยทางการ PAT 1 (มี.ค. 54) ข้อ 49 ระบุ «ไม่มีคำตอบ» (ครูแนบภาพในแชท 17 ก.ย. 2569) · E เทียบ PDF ข้อสอบตัวจริงแล้ว ต้นฉบับเป็นฝ่ายผิด ไม่ใช่การพิมพ์ผิดตอนนำเข้า',
    },
}
for v in FLAGS.values():
    v['decidedAt'] = DECIDED


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--root', default=os.path.dirname(HERE))
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    print('flag_flawed_sources.py  mode=%s' % ('APPLY' if a.apply else 'DRY-RUN'))
    print('root = ' + root)
    man_p = os.path.join(root, 'data', 'manifest.json')
    sets_d = os.path.join(root, 'data', 'sets')
    bank_p = os.path.join(root, 'data', 'bank.json')
    bb_p = os.path.join(root, 'scripts', 'build_bank.py')
    cf_p = os.path.join(root, 'scripts', 'check_flawed_source.py')
    for p in (man_p, sets_d, bank_p, bb_p, cf_p):
        if not os.path.exists(p):
            die('G1 missing: ' + p)
    print('G1 ok  repo root')

    man = json.load(open(man_p, encoding='utf-8'))
    raw, data, where = {}, {}, {}
    fmt = {}
    for sid in man['sets']:
        p = os.path.join(sets_d, sid + '.json')
        if not os.path.exists(p):
            continue
        b = open(p, 'rb').read()
        d = json.loads(b.decode('utf-8'))
        for k, q in enumerate(d['questions']):
            if q.get('id') in FLAGS:
                where.setdefault(q['id'], []).append((sid, k))
                raw[sid], data[sid] = b, d
    for i in FLAGS:
        if len(where.get(i, [])) != 1:
            die('G2 %s found %d times (expect 1)' % (i, len(where.get(i, []))))
    print('G2 ok  6 ids found once, in %s' % ', '.join(sorted(data)))

    # G6 format (try the two layouts used in this repo)
    for sid, b in raw.items():
        d = data[sid]
        for tail in (b'', b'\n'):
            if json.dumps(d, ensure_ascii=False, indent=2).encode('utf-8') + tail == b:
                fmt[sid] = tail
                break
        else:
            die('G6 %s.json does not re-serialise byte-identical - refuse to write' % sid)
    print('G6 ok  format check')

    chk = load_mod('e_check_flawed', cf_p)
    orig = {sid: json.loads(b.decode('utf-8')) for sid, b in raw.items()}
    todo, skip = [], []
    for i, flag in FLAGS.items():
        sid, k = where[i][0]
        q = data[sid]['questions'][k]
        if q.get('correct') is not None or q.get('answer') not in (None, ''):
            die('G3 %s has correct=%r answer=%r - flag is only for items without a key' % (i, q.get('correct'), q.get('answer')))
        if 'flawedSource' in q:
            if q['flawedSource'] == flag:
                skip.append(i)
                continue
            die('G4 %s already has a different flawedSource: %r' % (i, q['flawedSource']))
        probs = chk.check_one(flag)
        if probs:
            die('G5 %s flag fails gate 9: %s' % (i, probs))
        new = {}
        for kk, vv in q.items():
            new[kk] = vv
            if kk == 'id':
                new['flawedSource'] = flag
        q.clear()
        q.update(new)
        todo.append((i, sid, flag['kind']))
    print('G3/G4/G5 ok  to flag %d · already flagged %d' % (len(todo), len(skip)))
    for i, sid, kind in todo:
        print('     %-28s %-17s (%s.json)' % (i, kind, sid))

    changed = 0
    for sid in data:
        A, B = orig[sid]['questions'], data[sid]['questions']
        if len(A) != len(B) or [x['id'] for x in A] != [y['id'] for y in B]:
            die('G7 %s structure changed' % sid)
        for x, y in zip(A, B):
            if x == y:
                continue
            if {k: v for k, v in x.items() if k != 'flawedSource'} != {k: v for k, v in y.items() if k != 'flawedSource'} \
                    or y['id'] not in FLAGS:
                die('G7 unexpected change in %s' % y['id'])
            changed += 1
    if changed != len(todo):
        die('G7 changed %d != planned %d' % (changed, len(todo)))
    print('G7 ok  only "flawedSource" of %d ids changed' % changed)

    bank = json.load(open(bank_p, encoding='utf-8'))
    tmp = tempfile.mkdtemp(prefix='e_flag_')
    try:
        os.makedirs(os.path.join(tmp, 'sets'))
        shutil.copy2(man_p, os.path.join(tmp, 'manifest.json'))
        for sid in man['sets']:
            src = os.path.join(sets_d, sid + '.json')
            if not os.path.exists(src):
                continue
            dst = os.path.join(tmp, 'sets', sid + '.json')
            if sid in data:
                open(dst, 'wb').write(json.dumps(data[sid], ensure_ascii=False, indent=2).encode('utf-8') + fmt[sid])
            else:
                shutil.copy2(src, dst)
        sim = load_mod('e_build_bank', bb_p).build_bank(Path(tmp))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    sq = sim['questions']
    if len(sq) != len(bank['questions']):
        die('G8 simulated build has %d questions, bank.json %d' % (len(sq), len(bank['questions'])))
    strip = lambda q: {k: v for k, v in q.items() if not (k == 'flawedSource' and q['id'] in FLAGS)}
    diff = [y['id'] for x, y in zip(bank['questions'], sq) if strip(x) != strip(y)]
    if diff:
        die('G8 rebuilt bank would differ from bank.json beyond the flags at: %s  (pull first?)' % diff[:10])
    flagged = [q['id'] for q in sq if q.get('flawedSource')]
    nokey = [q['id'] for q in sq if q.get('correct') is None and not q.get('retired')]
    nokey_unflagged = [i for i in nokey if not next(x for x in sq if x['id'] == i).get('flawedSource')]
    print('G8 ok  simulated rebuild: flagged total %d · no-key %d · no-key WITHOUT flag %d %s' %
          (len(flagged), len(nokey), len(nokey_unflagged), nokey_unflagged))

    if not a.apply:
        print('\nDRY-RUN finished. nothing written.')
        print('to write:  python "%s" --apply' % os.path.abspath(__file__))
        return 0

    stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    for sid in sorted({s for _, s, _ in todo}):
        p = os.path.join(sets_d, sid + '.json')
        cur = open(p, 'rb').read()
        if cur != raw[sid]:
            die('G9 %s.json changed on disk during run' % sid)
        bak = p + '.bak-flag-' + stamp
        if os.path.exists(bak):
            die('G9 backup exists: ' + bak)
        shutil.copy2(p, bak)
        if md5(open(bak, 'rb').read()) != md5(cur):
            die('G9 backup md5 mismatch')
        new = json.dumps(data[sid], ensure_ascii=False, indent=2).encode('utf-8') + fmt[sid]
        with open(p, 'wb') as f:
            f.write(new)
        if open(p, 'rb').read() != new:
            print('STOP  G9 re-read mismatch %s - restore from %s' % (p, bak))
            sys.exit(2)
        print('WROTE %s.json  md5 %s -> %s  backup %s' % (sid, md5(cur)[:8], md5(new)[:8], os.path.basename(bak)))
    print('\nAPPLY finished: %d flags written to data/sets. bank.json untouched.' % len(todo))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:
        print('TOOL ERROR  %s: %s' % (type(e).__name__, e))
        sys.exit(2)

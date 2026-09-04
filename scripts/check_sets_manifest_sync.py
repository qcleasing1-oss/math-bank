#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""check_sets_manifest_sync.py v1.0 — ด่าน 24 · โฟลเดอร์คลังต้องตรงกับ manifest ทั้งสองทิศ

ที่มา (3-4 ก.ย. 2569 · ใบ 129/130/131/132 สาย MB-E):
  ไฟล์สำรอง `gen-chap-07-trigonometry.pre-merge60-BAK-…json` ถูกวางไว้ใน `data/sets/`
  ⇒ `build_bank.py` เดินตาม `manifest.sets` (บรรทัด 101) ⇒ มองไม่เห็น ⇒ bank.json ถูกต้อง
  ⇒ แต่ด่านที่ใช้ `glob('*.json')` เห็น ⇒ ด่าน 20 แดง **184 จุด** และรายงานว่า "id ซ้ำ"
  ⇒ ⇒ ผู้อ่านสองรายบนโฟลเดอร์เดียวกัน ให้คำตอบต่างกัน (63/6,557 กับ 64/6,741)
     และข้อความที่ได้ **ชี้ผิดที่** — คนอ่านไปไล่หาว่า "ข้อไหนชน" ทั้งที่เหตุคือ *ที่วางไฟล์*

  🔴 และมันไม่ใช่แค่ "นับผิด": `apply_tag_changes.py:56,103-104` และ
     `migrate_to_subtopics.py:203,244` เดิน glob แล้ว `write_text` ทับไฟล์ที่เจอ
     ⇒ ไฟล์นอก manifest ที่วางไว้ในนั้น **จะถูกแก้จริง** ⇒ สำรองที่ย้อนกลับไม่ได้

ด่านนี้ตัดสินอะไร:
  ทิศ ก  ไฟล์ใน `data/sets/` ที่ไม่มีใน `manifest.sets`      ⇒ "ย้ายออก หรือขึ้นทะเบียน"
  ทิศ ข  ชื่อใน `manifest.sets` ที่ไม่มีไฟล์จริง               ⇒ "manifest ประกาศของที่ไม่มี"
  ชั้น 2  ไฟล์ .json ชั้นบนของ `data/` ที่ไม่ได้ประกาศไว้        ⇒ จุดบอดที่ไม่มีด่านไหนมอง

ด่านนี้ ⛔ ไม่ตัดสินอะไร:
  ⛔ ไม่ดูเนื้อข้อสอบเลยสักตัวอักษร — เรื่องนั้นเป็นของด่าน 7/15/20
  ⛔ ไม่ผูกกับ **ชื่อไฟล์** เลย (ไม่มีคำว่า BAK / pre-merge / old ในกฎ)
     เหตุผล (ใบ 130 §3 ของ E): กฎที่ผูกกับชื่อไฟล์ = กฎที่ผูกกับวินัยของคนตั้งชื่อ
     ⇒ ไฟล์ชื่อ `gen-chap-07-trigonometry.old.json` ต้องถูกจับได้เท่ากัน

โหมด (คำเคาะครู 4 ก.ย. 69 · ใบ 132 §5 ข้อ ③):
  ค่าปริยาย = **เตือนอย่างเดียว รหัสออก 0** — เพราะตอนตั้งด่านมีไฟล์สำรองค้างอยู่จริง 2 ก้อน
  `--enforce` = แดงจริง (รหัส 1) ⇒ เปิดเมื่อครูเคาะ ⛔ ไม่เปิดเอง

รหัสออก (ข้อตกลงด่าน 11): 0 ผ่าน/เตือน · 1 เนื้อหาแดง · 2 ตัวเครื่องมือแดง
"""
import argparse
import json
import os
import shutil
import sys
import tempfile

VERSION = '1.0'

# ── ชั้นบนของ data/ : ไฟล์ .json ที่ "ประกาศไว้ว่าต้องมี" ────────────────────
#   ⛔ นี่คือรายการอนุญาต ⇒ ถ้าย้ายด่านนี้เข้า scripts/ ควรให้ ด่าน 10 เฝ้าขาขึ้น
#      (scripts/check_config_growth.py · WATCHED) — โตเงียบ ๆ ไม่ได้
DATA_ROOT_DECLARED = {
    'bank.json':     'ของที่ถูกสร้างโดย build_bank.py (บอทคอมมิตเองผ่าน build-bank.yml)',
    'manifest.json': 'ทะเบียนชุด — เป็นแหล่งจริงของด่านนี้เอง',
}

DECOY_MIN = {'ก': 3, 'ข': 3, 'ชั้น2': 3}


def read_manifest(path):
    r"""คืน (รายชื่อชุด, ข้อความผิดพลาด) — ⛔ อ่านไม่ได้ ไม่เท่ากับ "ไม่มีของเกิน"

    🔑 ทรงของ manifest.sets ⛔ ไม่ใช่ข้อสันนิษฐาน — ยึดตาม `build_bank.py:101`
       ซึ่งเขียนว่า `for sid in manifest['sets']` แล้วเอา sid ไปต่อเป็นชื่อไฟล์
       ⇒ ทั้ง **dict** (วนได้คีย์) และ **list ของสตริง** ให้ผลเดียวกันกับผู้สร้างคลัง
       ⇒ ⇒ ทรงอื่นนอกจากนี้ = ด่านนี้เทียบไม่ได้ ⇒ รหัส 2 ⛔ ไม่เดา
       ⬤ ของจริง 4 ก.ย. 69: เป็น **dict 63 คีย์** (ฉบับ v1.0 ก่อนแก้เดาว่าเป็น list แล้วออก 2)
    """
    try:
        data = json.load(open(path, encoding='utf-8'))
    except Exception as exc:
        return None, 'อ่าน %s ไม่ได้ — %s' % (path, exc)
    if not isinstance(data, dict) or 'sets' not in data:
        return None, '%s ไม่มีคีย์ sets ⇒ ด่านนี้ไม่มีแหล่งจริงให้เทียบ' % path
    sets = data['sets']
    if isinstance(sets, dict):
        ids = list(sets.keys())
    elif isinstance(sets, list):
        ids = sets
    else:
        return None, '%s คีย์ sets เป็น %s ⇒ วนแบบ build_bank.py:101 ไม่ได้' % (
            path, type(sets).__name__)
    if not all(isinstance(x, str) for x in ids):
        return None, '%s คีย์ sets วนแล้วได้ของที่ไม่ใช่สตริง ⇒ ต่อเป็นชื่อไฟล์ไม่ได้' % path
    return ids, None


def scan(sets_dir, manifest_path, data_root):
    r"""คืน dict ผลการเทียบ — ⛔ ไม่พิมพ์ ⛔ ไม่ตัดสิน (แยกการวัดออกจากการตัดสิน)"""
    declared, err = read_manifest(manifest_path)
    if err:
        return {'error': err}
    if not os.path.isdir(sets_dir):
        return {'error': 'ไม่มีโฟลเดอร์ %s' % sets_dir}

    on_disk = sorted(f for f in os.listdir(sets_dir) if f.endswith('.json'))
    disk_ids = {os.path.splitext(f)[0] for f in on_disk}
    declared_set = set(declared)

    extra = sorted(disk_ids - declared_set)      # ทิศ ก
    missing = sorted(declared_set - disk_ids)    # ทิศ ข

    root_extra = []
    if data_root and os.path.isdir(data_root):
        for f in sorted(os.listdir(data_root)):
            p = os.path.join(data_root, f)
            if os.path.isfile(p) and f.endswith('.json') and f not in DATA_ROOT_DECLARED:
                root_extra.append((f, os.path.getsize(p)))

    return {
        'error': None,
        'n_disk': len(on_disk),
        'n_declared': len(declared),
        'n_declared_unique': len(declared_set),
        'dup_declared': sorted({s for s in declared if declared.count(s) > 1}),
        'extra': extra,
        'missing': missing,
        'root_extra': root_extra,
    }


def report(res, sets_dir, data_root, enforce):
    r"""พิมพ์ผล แล้วคืนรหัสออก — ทุกบรรทัดพก **ตัวหาร** ติดเสมอ"""
    if res.get('error'):
        print('🔴 %s' % res['error'])
        print('   ⛔ "เทียบไม่ได้" ไม่เท่ากับ "เทียบแล้วผ่าน" ⇒ รหัส 2')
        return 2

    print('📌 ด่าน 24 · ตัวหาร: ไฟล์ .json ใน %s = %d ไฟล์ · manifest.sets ประกาศ %d ชื่อ (ไม่ซ้ำ %d)'
          % (sets_dir, res['n_disk'], res['n_declared'], res['n_declared_unique']))
    print('   ชั้นบน %s : ไฟล์ .json ที่ประกาศไว้ %d ชื่อ (%s)'
          % (data_root, len(DATA_ROOT_DECLARED), ' · '.join(sorted(DATA_ROOT_DECLARED))))

    hit = False
    if res['dup_declared']:
        hit = True
        print('🔴 manifest.sets มีชื่อซ้ำ %d ชื่อ: %s'
              % (len(res['dup_declared']), ' · '.join(res['dup_declared'])))

    if res['extra']:
        hit = True
        print('🔴 ทิศ ก · ไฟล์ใน %s ที่ไม่มีใน manifest.sets — %d จาก %d ไฟล์:'
              % (sets_dir, len(res['extra']), res['n_disk']))
        for name in res['extra']:
            print('   %s.json  ⇒ ย้ายออกจาก %s หรือขึ้นทะเบียนใน manifest.sets'
                  % (name, sets_dir))
        print('   ⚠️ ตราบใดที่มันอยู่ในนั้น: ด่านที่ใช้ glob จะนับมันด้วย ·'
              ' และ apply_tag_changes / migrate_to_subtopics จะ **เขียนทับมัน**')
    if res['missing']:
        hit = True
        print('🔴 ทิศ ข · manifest.sets ประกาศชื่อที่ไม่มีไฟล์ — %d จาก %d ชื่อ:'
              % (len(res['missing']), res['n_declared_unique']))
        for name in res['missing']:
            print('   %s.json  ⇒ build_bank.py จะข้ามชุดนี้เงียบ ๆ' % name)
    if res['root_extra']:
        hit = True
        print('🔴 ชั้น 2 · ไฟล์ .json ชั้นบนของ %s ที่ไม่ได้ประกาศ — %d ไฟล์:'
              % (data_root, len(res['root_extra'])))
        for name, size in res['root_extra']:
            print('   %s  (%s B)' % (name, format(size, ',')))
        print('   ⚠️ ชั้นนี้ ⛔ ไม่มีด่านไหนมองเห็นมาก่อน (ทุกด่าน glob แค่ %s)' % sets_dir)

    if not hit:
        print('✅ ด่าน 24 ผ่าน — โฟลเดอร์กับ manifest ตรงกันทั้งสองทิศ และชั้นบนสะอาด')
        return 0

    if enforce:
        print('⇒ 🔴 โหมด --enforce ⇒ รหัสออก 1 (เนื้อหา/ที่วางไฟล์ผิด)')
        return 1
    print('⇒ 🟠 โหมดเตือน (ค่าปริยาย · คำเคาะครู 4 ก.ย. 69) ⇒ รหัสออก 0')
    print('   เปิดเป็นแดงเมื่อครูเคาะ: เติม --enforce ในบรรทัดที่เรียกด่านนี้')
    return 0


# ─────────────────────────────────────────────────────────────
# self-test — ⛔ ต้องรันก่อนของจริงเสมอ (กับดัก ⑦)
#   ของล่อสองขั้ว: ของเสียที่กฎต้องจับ · ของสะอาดหน้าตาใกล้เคียงที่กฎต้องไม่จับ
# ─────────────────────────────────────────────────────────────
def _mkcase(root, sets, declared, root_files, shape='dict'):
    r"""สร้างเคสจำลอง — shape เลือกทรงของ manifest.sets (dict = ทรงของจริง · list = ทรงสำรอง)"""
    os.makedirs(os.path.join(root, 'sets'), exist_ok=True)
    for name in sets:
        open(os.path.join(root, 'sets', name), 'w', encoding='utf-8').write('{"questions":[]}')
    body = {sid: {} for sid in declared} if shape == 'dict' else list(declared)
    json.dump({'sets': body}, open(os.path.join(root, 'manifest.json'), 'w', encoding='utf-8'))
    for name in root_files:
        open(os.path.join(root, name), 'w', encoding='utf-8').write('{}')
    return scan(os.path.join(root, 'sets'), os.path.join(root, 'manifest.json'), root)


def selftest():
    cases = []
    # ── ของล่อทิศ ก (ไฟล์เกิน) — ⛔ ชื่อไฟล์ต่างกันทั้งสามแบบโดยตั้งใจ ──
    cases.append(('ก', 'ไฟล์สำรองชื่อมี BAK', ['a.json', 'a.pre-merge-BAK.json'], ['a'], [],
                  lambda r: r['extra'] == ['a.pre-merge-BAK']))
    cases.append(('ก', 'ไฟล์สำรองชื่อ .old — กฎที่ผูกชื่อจะพลาดตัวนี้',
                  ['a.json', 'a.old.json'], ['a'], [],
                  lambda r: r['extra'] == ['a.old']))
    cases.append(('ก', 'ไฟล์ชื่อสุภาพสิ้นดี แต่ไม่อยู่ในทะเบียน',
                  ['a.json', 'gen-chap-99-newset.json'], ['a'], [],
                  lambda r: r['extra'] == ['gen-chap-99-newset']))
    # ── ของล่อทิศ ข (ประกาศแล้วไม่มีไฟล์) ──
    cases.append(('ข', 'ประกาศ 2 มีไฟล์ 1', ['a.json'], ['a', 'b'], [],
                  lambda r: r['missing'] == ['b']))
    cases.append(('ข', 'ประกาศชื่อที่สะกดต่างจากไฟล์', ['a.json'], ['a', 'A'], [],
                  lambda r: r['missing'] == ['A']))
    cases.append(('ข', 'โฟลเดอร์ว่าง แต่ทะเบียนมี 1', [], ['a'], [],
                  lambda r: r['missing'] == ['a'] and r['n_disk'] == 0))
    # ── ของล่อชั้น 2 (ชั้นบนของ data/) ──
    cases.append(('ชั้น2', 'สำรอง bank ชั้นบน', ['a.json'], ['a'], ['bank.pre-merge-BAK.json'],
                  lambda r: [x[0] for x in r['root_extra']] == ['bank.pre-merge-BAK.json']))
    cases.append(('ชั้น2', 'ไฟล์ชั้นบนชื่อไม่มีคำใบ้เลย', ['a.json'], ['a'], ['scratch.json'],
                  lambda r: [x[0] for x in r['root_extra']] == ['scratch.json']))
    cases.append(('ชั้น2', 'ไฟล์ชั้นบน 2 ก้อนพร้อมกัน', ['a.json'], ['a'], ['x.json', 'y.json'],
                  lambda r: len(r['root_extra']) == 2))
    # ── ของสะอาด — กฎต้อง ⛔ ไม่จับ ──
    clean = [
        ('ตรงกันเป๊ะ 3 ชุด', ['a.json', 'b.json', 'c.json'], ['a', 'b', 'c'], []),
        ('ชั้นบนมีแต่ของที่ประกาศไว้', ['a.json'], ['a'], ['bank.json']),
        ('ไฟล์ที่ไม่ใช่ .json ในโฟลเดอร์ชุด ⇒ ⛔ ไม่ใช่เรื่องของด่านนี้',
         ['a.json', 'README.md'], ['a'], []),
    ]

    # ── ทรงของ manifest: ต้องอ่านได้ทั้ง dict และ list · ทรงอื่น ⇒ รหัส 2 ⛔ ไม่เดา
    shape_fails = []
    tmp0 = tempfile.mkdtemp(prefix='gate24-shape-')
    try:
        for shp in ('dict', 'list'):
            r = _mkcase(os.path.join(tmp0, shp), ['a.json', 'a.old.json'], ['a'], [], shape=shp)
            if r.get('error') or r['extra'] != ['a.old']:
                shape_fails.append('ทรง %s อ่านไม่ได้/ไม่จับ' % shp)
        bad_root = os.path.join(tmp0, 'weird')
        os.makedirs(os.path.join(bad_root, 'sets'), exist_ok=True)
        json.dump({'sets': 42}, open(os.path.join(bad_root, 'manifest.json'), 'w', encoding='utf-8'))
        r = scan(os.path.join(bad_root, 'sets'), os.path.join(bad_root, 'manifest.json'), bad_root)
        if not r.get('error'):
            shape_fails.append('ทรงประหลาด (sets = 42) ต้องเทียบไม่ได้ แต่กลับตอบว่าเทียบได้')
    finally:
        shutil.rmtree(tmp0, ignore_errors=True)

    print('self-test ด่าน 24 v%s' % VERSION)
    print('  ทรง manifest.sets · dict + list + ทรงประหลาด ⇒ %s'
          % ('✅ ผ่าน 3/3' if not shape_fails else '🔴 ' + ' · '.join(shape_fails)))
    hits = {'ก': 0, 'ข': 0, 'ชั้น2': 0}
    fails = []
    tmp = tempfile.mkdtemp(prefix='gate24-')
    try:
        for i, (rule, name, sets, declared, roots, check) in enumerate(cases):
            root = os.path.join(tmp, 'bad%d' % i)
            res = _mkcase(root, sets, declared, roots)
            if res.get('error') or not check(res):
                fails.append('กฎ %s · %s ⇒ ⛔ ไม่จับ' % (rule, name))
            else:
                hits[rule] += 1
        for j, (name, sets, declared, roots) in enumerate(clean):
            root = os.path.join(tmp, 'clean%d' % j)
            res = _mkcase(root, sets, declared, roots)
            if res.get('error'):
                fails.append('ของสะอาด · %s ⇒ ตัวด่านพัง: %s' % (name, res['error']))
            elif res['extra'] or res['missing'] or res['root_extra']:
                fails.append('ของสะอาด · %s ⇒ 🔴 ยิงมั่ว' % name)
        # ⑦ก · รหัสที่เชลล์เห็นจริง ⛔ ไม่ใช่ค่าคืนของฟังก์ชัน
        root = os.path.join(tmp, 'e2e')
        _mkcase(root, ['a.json', 'a.old.json'], ['a'], [])
        import subprocess
        cmd = [sys.executable, os.path.abspath(__file__),
               '--sets', os.path.join(root, 'sets'),
               '--manifest', os.path.join(root, 'manifest.json'),
               '--data-root', root]
        warn = subprocess.run(cmd, capture_output=True).returncode
        hard = subprocess.run(cmd + ['--enforce'], capture_output=True).returncode
        if warn != 0:
            fails.append('e2e · โหมดเตือนต้องคืน 0 แต่ได้ %d' % warn)
        if hard != 1:
            fails.append('e2e · โหมด --enforce ต้องคืน 1 แต่ได้ %d' % hard)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    for rule in sorted(hits):
        need = DECOY_MIN[rule]
        mark = '✅' if hits[rule] >= need else '🔴'
        print('  กฎ %-5s · ของล่อ %d/%d %s' % (rule, hits[rule], need, mark))
        if hits[rule] < need:
            fails.append('กฎ %s ของล่อไม่ครบขั้นต่ำ %d' % (rule, need))
    print('  ของสะอาด %d ตัว · e2e รหัสออก 2 โหมด' % len(clean))
    fails.extend(shape_fails)
    if fails:
        print('🔴 self-test ตก %d เคส:' % len(fails))
        for f in fails:
            print('   %s' % f)
        print('   ⇒ รหัส 2 — ของที่พังคือเครื่องมือ ⛔ ไม่ใช่เนื้อหา')
        return 2
    print('✅ self-test ผ่านทุกเคส (%d ของล่อ + %d ของสะอาด + 2 e2e)' % (len(cases), len(clean)))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sets', default=os.path.join('data', 'sets'))
    ap.add_argument('--manifest', default=os.path.join('data', 'manifest.json'))
    ap.add_argument('--data-root', default='data')
    ap.add_argument('--enforce', action='store_true',
                    help='ทำให้ผลที่เจอเป็นรหัส 1 (ค่าปริยาย = เตือนอย่างเดียว)')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    a = ap.parse_args()
    if a.version:
        print(VERSION)
        return 0
    if a.selftest:
        return selftest()
    return report(scan(a.sets, a.manifest, a.data_root), a.sets, a.data_root, a.enforce)


if __name__ == '__main__':
    sys.exit(main())

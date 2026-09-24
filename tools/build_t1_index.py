#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_t1_index.py — สร้าง _t1run/t1_index.json ใหม่จาก t1_MASTER.json  (มติครู ⑮ ก · 24 ก.ย. 69 · MB ใบ 409)

ที่มา: viewer/t1-overlay.js อ่าน '../_t1run/t1_index.json' (ทรง {id: record})
       แต่ไฟล์นั้นสร้างด้วยมือครั้งเดียว (25 ส.ค. · 951 ข้อ) แล้วไม่มีใครสร้างใหม่
       ขณะที่ MASTER โตเป็น 6,547 ข้อ ⇒ วิวเวอร์เห็น t1 แค่บางบท

ทำอะไร: อ่าน MASTER (list ของ record) ⇒ เขียน index เป็น {id: record} เรียงตามลำดับใน MASTER
        ⛔ ไม่แก้เนื้อ record แม้แต่ช่องเดียว · ⛔ ไม่เพิ่มคีย์อื่น (วิวเวอร์นับ Object.keys เป็นจำนวนข้อ)
        รูปแบบไฟล์ = json.dumps(ensure_ascii=False) ไม่มี indent ไม่มีขึ้นบรรทัดท้าย = แบบไฟล์เดิม
        (positive control: ป้อน 951 record ของไฟล์เดิม ⇒ ได้ไฟล์เดิมทุกไบต์)

ใช้ (รันที่รากของ math-bank):
  python tools/build_t1_index.py             ⇒ สร้าง/เขียนทับ _t1run/t1_index.json + พิมพ์รายงาน
  python tools/build_t1_index.py --check     ⇒ ไม่เขียน · ตรวจว่า index ตรงกับ MASTER ไหม
  python tools/build_t1_index.py --selftest
  (--master / --out ใช้ชี้ไฟล์อื่นตอนทดสอบ)

⚠️ index สร้างจาก MASTER ⇒ ทุกครั้งที่ merge_master.py เขียน MASTER ใหม่ ต้องรันตัวนี้ซ้ำ
   ไม่งั้นวิวเวอร์จะเห็นของเก่า · --check มีไว้จับกรณีนี้ (งาน ⑪ จะผูกเข้า merge)

รหัสออก: 0 = ผ่าน/ตรงกัน · 1 = index ไม่ตรงกับ MASTER (โหมด --check) · 2 = เครื่องมือ/ข้อมูลเข้าพัง
"""
import argparse, hashlib, json, os, re, sys
from collections import Counter

VERSION = '1.0'
MASTER = '_t1run/results/t1_MASTER.json'
OUT = '_t1run/t1_index.json'


class Bad(Exception):
    pass


def build(records):
    """list[record] ⇒ dict {id: record} ตามลำดับเดิม · ข้อมูลเสีย ⇒ Bad"""
    if not isinstance(records, list):
        raise Bad(f'MASTER ต้องเป็น list แต่ได้ {type(records).__name__}')
    out = {}
    for i, r in enumerate(records):
        if not isinstance(r, dict):
            raise Bad(f'record ที่ {i} ไม่ใช่ object')
        rid = r.get('id')
        if not isinstance(rid, str) or not rid.strip():
            raise Bad(f'record ที่ {i} ไม่มี id')
        if rid in out:
            raise Bad(f'id ซ้ำใน MASTER: {rid}')
        out[rid] = r
    if not out:
        raise Bad('MASTER ว่าง ⇒ "ไม่มีของ" ไม่เท่ากับ "สร้างสำเร็จ"')
    return out


def dump(d):
    return json.dumps(d, ensure_ascii=False).encode('utf-8')


def compare(old, new):
    """คืน (เพิ่ม, หาย, เนื้อต่าง) ระหว่าง index เดิมกับ index ที่ควรเป็น"""
    add = [k for k in new if k not in old]
    gone = [k for k in old if k not in new]
    diff = [k for k in new if k in old and old[k] != new[k]]
    return add, gone, diff


def group(i):
    m = re.match(r'(gen-)?chap-(\d+)', i)
    if not m:
        return 'ข้อสอบจริง'
    return ('gen-' if m.group(1) else '') + f'chap-{int(m.group(2)):02d}'


def md5(b):
    return hashlib.md5(b).hexdigest()[:8]


def load_json(p):
    try:
        with open(p, 'rb') as f:
            raw = f.read()
        return raw, json.loads(raw.decode('utf-8'))
    except FileNotFoundError:
        raise Bad(f'ไม่พบ {p} — ต้องรันที่รากของ math-bank')
    except Exception as e:
        raise Bad(f'อ่าน {p} ไม่ได้ — {e}')


def show_diff(add, gone, diff):
    print(f'  เทียบกับ index เดิม: เพิ่ม {len(add):,} · หาย {len(gone):,} · เนื้อต่าง {len(diff):,}')
    for tag, ids in (('หาย', gone), ('เนื้อต่าง', diff)):
        for k in ids[:20]:
            print(f'     {tag}: {k}')
        if len(ids) > 20:
            print(f'     … อีก {len(ids) - 20} ข้อ')


def run(a):
    mraw, recs = load_json(a.master)
    new = build(recs)
    print(f'build_t1_index v{VERSION} · MASTER {a.master} · {len(mraw):,} B · md5 {md5(mraw)} · {len(new):,} ข้อ')
    g = Counter(group(k) for k in new)
    print('  แยกกลุ่ม (ตาม id): ' + ' · '.join(f'{k} {v}' for k, v in sorted(g.items())))

    old = None
    if os.path.exists(a.out):
        oraw, old = load_json(a.out)
        if not isinstance(old, dict):
            raise Bad(f'{a.out} เดิมไม่ใช่ object ⇒ ทรงไม่ใช่ที่วิวเวอร์อ่าน')
        print(f'  index เดิม {a.out} · {len(oraw):,} B · md5 {md5(oraw)} · {len(old):,} ข้อ')
        add, gone, diff = compare(old, new)
        show_diff(add, gone, diff)
    else:
        print(f'  ยังไม่มี {a.out}')

    body = dump(new)
    if a.check:
        if old is not None and oraw == body:
            print('✅ index ตรงกับ MASTER ทุกไบต์')
            return 0
        if old is not None and old == new:
            print('🟠 เนื้อตรงกับ MASTER แต่ไบต์ต่าง (ลำดับ/รูปแบบ) ⇒ วิวเวอร์ใช้ได้ · รันโดยไม่ใส่ --check เพื่อเขียนใหม่')
            return 0
        print('🔴 index ไม่ตรงกับ MASTER ⇒ วิวเวอร์กำลังแสดงของเก่า · รันโดยไม่ใส่ --check เพื่อสร้างใหม่')
        return 1

    tmp = a.out + '.tmp'
    with open(tmp, 'wb') as f:
        f.write(body)
    os.replace(tmp, a.out)
    with open(a.out, 'rb') as f:
        back = f.read()
    if back != body or json.loads(back.decode('utf-8')) != new:
        print('🔴 อ่านกลับไม่ตรงกับที่เขียน')
        return 2
    print(f'✅ เขียน {a.out} · {len(back):,} B · md5 {md5(back)} · {len(new):,} ข้อ · ทุก record = MASTER ทุกช่อง')
    return 0


# ───────────────────────── SELF-TEST ─────────────────────────
def _r(i, **kw):
    d = {'id': i, 'v': 't1-v1', 'steps': []}
    d.update(kw)
    return d


def _mut_allow_dup(records):
    """มิวแทนต์: ไม่ตรวจ id ซ้ำ ⇒ ตัวหลังทับตัวหน้าเงียบ ๆ"""
    return {r['id']: r for r in records}


def _mut_drop_last(records):
    """มิวแทนต์: ทำข้อสุดท้ายหาย"""
    return build(records[:-1]) if len(records) > 1 else build(records)


def selftest():
    print(f'SELF-TEST build_t1_index v{VERSION}')
    ok = True

    def expect(name, cond):
        nonlocal ok
        print(f'  {"✅" if cond else "🔴"}  {name}')
        ok &= bool(cond)

    def raises(fn, *x):
        try:
            fn(*x)
        except Bad:
            return True
        except Exception:
            return False
        return False

    recs = [_r('b-q1', goal='ข'), _r('a-q2', goal='ก <x> $\\lt$')]
    d = build(recs)
    expect('ลำดับ id ตาม MASTER (ไม่เรียงใหม่)', list(d) == ['b-q1', 'a-q2'])
    expect('record ไม่ถูกแก้ (เป็นตัวเดียวกับต้นทาง)', d['a-q2'] is recs[1])
    expect('รูปแบบไฟล์ = json.dumps(ensure_ascii=False) ไทยไม่เป็น \\u', dump(d) == json.dumps(d, ensure_ascii=False).encode() and b'\\u0e' not in dump(d))
    expect('id ซ้ำ ⇒ พัง (รหัส 2)', raises(build, recs + [_r('b-q1')]))
    expect('record ไม่มี id ⇒ พัง', raises(build, [{'v': 't1-v1'}]))
    expect('id ว่าง ⇒ พัง', raises(build, [_r('  ')]))
    expect('MASTER ไม่ใช่ list ⇒ พัง', raises(build, {'a': 1}))
    expect('MASTER ว่าง ⇒ พัง', raises(build, []))
    a, g, df = compare({'b-q1': recs[0], 'old': _r('old')}, {'b-q1': _r('b-q1', goal='ใหม่'), 'a-q2': recs[1]})
    expect('--check เห็น เพิ่ม/หาย/เนื้อต่าง ครบทั้ง 3 แบบ', (a, g, df) == (['a-q2'], ['old'], ['b-q1']))
    expect('ตรงกันทุกอย่าง ⇒ ไม่มีต่าง', compare(d, build(recs)) == ([], [], []))
    # มิวแทนต์ต้องถูกจับ
    m1 = not raises(_mut_allow_dup, recs + [_r('b-q1')])
    expect('มิวแทนต์ ไม่ตรวจ id ซ้ำ ⇒ ถูกจับด้วยเคส "id ซ้ำ"', m1)
    m2 = _mut_drop_last(recs) != build(recs)
    expect('มิวแทนต์ ทำข้อสุดท้ายหาย ⇒ ถูกจับด้วยการเทียบกับ build()', m2)
    print('✅ SELF-TEST ผ่าน' if ok else '🔴 SELF-TEST ไม่ผ่าน')
    return 0 if ok else 2


def main():
    ap = argparse.ArgumentParser(description='สร้าง _t1run/t1_index.json จาก t1_MASTER.json (มติครู ⑮ ก)')
    ap.add_argument('--master', default=MASTER)
    ap.add_argument('--out', default=OUT)
    ap.add_argument('--check', action='store_true', help='ไม่เขียน · ตรวจว่า index ตรงกับ MASTER')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    a = ap.parse_args()
    if a.version:
        print(VERSION); return 0
    if a.selftest:
        return selftest()
    try:
        return run(a)
    except Bad as e:
        print(f'🔴 {e}')
        return 2


if __name__ == '__main__':
    sys.exit(main())

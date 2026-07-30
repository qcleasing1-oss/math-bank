#!/usr/bin/env python3
"""
build_bank.py — Phase F.4 build script (math-bank project)

รวม data/manifest.json + data/sets/*.json → data/bank.json
ใช้โดย GitHub Actions ตอน push เปลี่ยน manifest หรือ sets/
และใช้รัน local ก่อน push ก็ได้ (ตรวจสอบก่อน)

Usage:
  python scripts/build_bank.py                   # ใช้ data/ ใน repo root (default)
  python scripts/build_bank.py path/to/data      # ระบุ folder เอง
  python scripts/build_bank.py --stamp-always    # ประทับเวลาใหม่ทุกครั้งแม้เนื้อหาไม่เปลี่ยน

Exit codes:
  0 = success (รวมทั้งกรณี "ไม่มีอะไรเปลี่ยน")
  1 = error (ไฟล์หาย, JSON พัง, ฯลฯ)

Output format ต้อง byte-identical กับ migrate_bank.py round-trip
(json.dumps + ensure_ascii=False + indent=2 + ไม่ sort_keys)

--------------------------------------------------------------------------
แพตช์ 30 ก.ค. 2569 — ประทับเวลา build อัตโนมัติ (มติครู + คำขอทีมพอร์ทัล)

ปัญหาเดิม: บรรทัด `'exported': manifest['exported']` คัดค่ามาจาก manifest ตรง ๆ
ซึ่งค้างอยู่ที่ 2026-06-23T00:00:00Z เพราะไม่มีใคร bump ⇒ ด่านเช็คความสด
ฝั่งพอร์ทัล (curate.html) เป็น "ด่านที่โกหกเงียบ ๆ" ทุกครั้งที่ CI rebuild

ฟิลด์ที่เพิ่ม/เปลี่ยน:
  * exported         = เวลาที่เนื้อหาเปลี่ยนครั้งล่าสุด (UTC, ISO 8601 ลงท้าย Z)
  * manifestExported = ค่าเดิมจาก manifest — เก็บไว้ ไม่ทิ้ง
  * questionCount    = จำนวนข้อทั้งหมด
  * activeCount      = จำนวนข้อที่ไม่ retired  ← มาตรฐานกลางที่ทั้งสองฝ่ายอ้างอิงตัวเดียวกัน
  * retiredCount     = จำนวนข้อที่ retired
  * builtFromCommit  = GITHUB_SHA (หรือ 'local' ถ้ารัน local)

--------------------------------------------------------------------------
แพตช์ 30 ก.ค. 2569 (รอบ 2) — ส่งต่อ subTopicNames ลง bank.json (คำขอทีมพอร์ทัล ข้อ ③)

ปัญหาเดิม: `manifest.json` มี `subTopicNames` (194 รหัส) และ `deprecatedSubTopics`
(7 รหัส) อยู่แล้ว แต่ build_bank.py ไม่คัดสองฟิลด์นี้ลง bank.json ⇒ ฝั่งพอร์ทัล
ซึ่งอ่าน bank.json ตัวเดียว มองเห็นแต่รหัส ไม่เห็นชื่อหัวข้อ ⇒ census ของพอร์ทัล
แสดงชื่อเป็น "—" ทั้ง 184 รหัส และ**นับรหัสที่ไม่มีข้อเลยไม่ได้** (รหัสที่ไม่ปรากฏ
ใน questions จะหายไปจากการนับทั้งหมด — วัดแล้วต่างกัน 3 รหัสพอดี)

ฟิลด์ที่เพิ่ม:
  * subTopicNames       = dict รหัส → ชื่อไทย (คัดจาก manifest ตรง ๆ)
  * deprecatedSubTopics = list รหัสที่เลิกใช้ (12.12 + 16.1–16.6)
  * subTopicCount       = จำนวนรหัสทั้งหมด
  * liveSubTopicCount   = จำนวนรหัสที่ยังใช้ (ทั้งหมด − deprecated)

ทั้งสี่ฟิลด์เป็น **การคัดค่าเท่านั้น ไม่คำนวณใหม่** ⇒ manifest ยังเป็นแหล่งความจริง
เดียว (single source of truth) ถ้า manifest ไม่มีฟิลด์นี้ (repo เก่า) จะได้ค่าว่าง
ไม่ทำให้ build ล้ม

พฤติกรรมการเขียนไฟล์ (สำคัญ):
  โดยปริยาย จะเขียนไฟล์ **เฉพาะเมื่อเนื้อหาเปลี่ยนจริง** (เทียบโดยตัดฟิลด์ที่
  ผันแปรตามเวลาออกก่อน) ⇒ ไม่มี diff เปล่าทุกครั้งที่ CI รัน และ `exported`
  จึงหมายถึง "เวลาที่เนื้อหาคลังเปลี่ยนครั้งล่าสุด" ซึ่งเป็นความหมายที่
  ด่านเช็คความสดต้องการจริง ๆ (ตัวเลือก B ในเอกสารตอบพอร์ทัล v5 §9)

  ถ้าต้องการประทับเวลาทุกครั้งแม้เนื้อหาไม่เปลี่ยน ให้ใส่ `--stamp-always`
  (ตัวเลือก A — ด่านแม่นสุด แต่ bank.json จะมี diff ทุกรัน)
"""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# ฟิลด์ที่ผันแปรทุก build — ตัดออกก่อนเทียบว่า "เนื้อหาเปลี่ยนจริงไหม"
VOLATILE_KEYS = ('exported', 'builtFromCommit')


def utc_stamp() -> str:
    """เวลาปัจจุบันแบบ UTC ISO 8601 ลงท้าย Z (รูปแบบเดียวกับ manifest.exported)"""
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def content_key(bank: dict) -> str:
    """serialize bank โดยตัดฟิลด์ผันแปรออก — ใช้เทียบว่าเนื้อหาเปลี่ยนจริงไหม"""
    stripped = {k: v for k, v in bank.items() if k not in VOLATILE_KEYS}
    return json.dumps(stripped, ensure_ascii=False, indent=2)


def build_bank(data_dir: Path) -> dict:
    """รวม manifest + sets/*.json เป็น bank dict เดียว"""
    manifest_path = data_dir / 'manifest.json'
    sets_dir = data_dir / 'sets'

    if not manifest_path.exists():
        raise FileNotFoundError(f"ไม่พบ manifest: {manifest_path}")
    if not sets_dir.is_dir():
        raise FileNotFoundError(f"ไม่พบโฟลเดอร์ sets/: {sets_dir}")

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # อ่าน set files ตามลำดับใน manifest.sets (รักษา order ของคำถาม)
    all_questions = []
    missing = []
    for sid in manifest['sets']:
        set_path = sets_dir / f'{sid}.json'
        if not set_path.exists():
            missing.append(sid)
            continue
        with open(set_path, 'r', encoding='utf-8') as f:
            set_data = json.load(f)
        # validate setId match
        if set_data.get('setId') and set_data['setId'] != sid:
            raise ValueError(
                f"setId ใน {set_path.name} = {set_data['setId']!r} "
                f"ไม่ตรงกับ manifest key {sid!r}"
            )
        all_questions.extend(set_data['questions'])

    if missing:
        raise FileNotFoundError(
            f"ขาดไฟล์ set: {missing}\n"
            f"(set พวกนี้อยู่ใน manifest แต่ไม่มีไฟล์ใน sets/)"
        )

    # นับข้อ active / retired — นิยาม active = ไม่มีธง retired เป็นจริง (ไม่มีเงื่อนไขอื่น)
    n_retired = sum(1 for q in all_questions if q.get('retired'))

    # taxonomy หัวข้อย่อย — คัดจาก manifest ตรง ๆ (manifest = แหล่งความจริงเดียว)
    # ใช้ .get() เพื่อให้ repo ที่ manifest ยังไม่มีฟิลด์นี้ build ผ่านได้
    sub_names = manifest.get('subTopicNames', {})
    deprecated = manifest.get('deprecatedSubTopics', [])

    # ประกอบ bank — key เดิม 5 ตัวคงลำดับไว้ · key ใหม่แทรกหลัง exported
    return {
        'schemaVersion': manifest['schemaVersion'],
        'exported': utc_stamp(),
        'manifestExported': manifest['exported'],
        'questionCount': len(all_questions),
        'activeCount': len(all_questions) - n_retired,
        'retiredCount': n_retired,
        'subTopicCount': len(sub_names),
        'liveSubTopicCount': len([c for c in sub_names if c not in set(deprecated)]),
        'builtFromCommit': os.environ.get('GITHUB_SHA', 'local'),
        'topicNames': manifest['topicNames'],
        'subTopicNames': sub_names,
        'deprecatedSubTopics': deprecated,
        'sets': manifest['sets'],
        'questions': all_questions,
    }


def main() -> int:
    argv = [a for a in sys.argv[1:] if a != '--stamp-always']
    stamp_always = '--stamp-always' in sys.argv[1:]

    # หา data/ folder
    if argv:
        data_dir = Path(argv[0])
    else:
        # default: scripts/build_bank.py → ../data/
        script_dir = Path(__file__).parent
        data_dir = script_dir.parent / 'data'

    data_dir = data_dir.resolve()
    print(f"📂 Data folder: {data_dir}")

    if not data_dir.is_dir():
        print(f"❌ ไม่พบโฟลเดอร์ data/: {data_dir}", file=sys.stderr)
        return 1

    try:
        bank = build_bank(data_dir)
    except (FileNotFoundError, ValueError, KeyError, json.JSONDecodeError) as e:
        print(f"❌ Build ล้มเหลว: {e}", file=sys.stderr)
        return 1

    n_sets = len(bank['sets'])
    n_questions = bank['questionCount']
    n_active = bank['activeCount']
    n_retired = bank['retiredCount']

    output_path = data_dir / 'bank.json'

    # เช็คว่า "เนื้อหา" เปลี่ยนจริงไหม — เทียบโดยตัดฟิลด์ผันแปรออก (กัน diff เปล่าทุกรัน)
    if output_path.exists() and not stamp_always:
        try:
            old_bank = json.loads(output_path.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            old_bank = None
        if old_bank is not None and content_key(old_bank) == content_key(bank):
            # เนื้อหาเหมือนเดิม ⇒ คง exported เดิมไว้ ไม่เขียนไฟล์
            print(
                f"✅ bank.json ไม่เปลี่ยน "
                f"({n_sets} sets, {n_questions} questions, "
                f"active {n_active} / retired {n_retired}) "
                f"· exported คงเดิม {old_bank.get('exported')!r}"
            )
            return 0

    # Serialize — ใช้ format เดียวกับ migrate_bank.py เพื่อ round-trip ตรงกัน
    new_content = json.dumps(bank, ensure_ascii=False, indent=2)

    # เขียนไฟล์
    output_path.write_text(new_content, encoding='utf-8')
    print(
        f"✅ Built bank.json: {n_sets} sets, {n_questions} questions "
        f"(active {n_active} / retired {n_retired}), {len(new_content):,} chars"
    )
    print(
        f"   exported = {bank['exported']} · "
        f"builtFromCommit = {bank['builtFromCommit']}"
    )
    print(
        f"   subTopicNames = {bank['subTopicCount']} รหัส "
        f"(ใช้จริง {bank['liveSubTopicCount']} · "
        f"เลิกใช้ {len(bank['deprecatedSubTopics'])})"
    )
    if bank['subTopicCount'] == 0:
        print(
            "   ⚠️  manifest.json ไม่มี subTopicNames — "
            "ฝั่งพอร์ทัลจะยังเห็นชื่อหัวข้อเป็น '—'",
            file=sys.stderr,
        )
    return 0


if __name__ == '__main__':
    sys.exit(main())

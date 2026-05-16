#!/usr/bin/env python3
"""
build_bank.py — Phase F.4 build script (math-bank project)

รวม data/manifest.json + data/sets/*.json → data/bank.json
ใช้โดย GitHub Actions ตอน push เปลี่ยน manifest หรือ sets/
และใช้รัน local ก่อน push ก็ได้ (ตรวจสอบก่อน)

Usage:
  python scripts/build_bank.py                # ใช้ data/ ใน repo root (default)
  python scripts/build_bank.py path/to/data   # ระบุ folder เอง

Exit codes:
  0 = success (รวมทั้งกรณี "ไม่มีอะไรเปลี่ยน")
  1 = error (ไฟล์หาย, JSON พัง, ฯลฯ)

Output format ต้อง byte-identical กับ migrate_bank.py round-trip
(json.dumps + ensure_ascii=False + indent=2 + ไม่ sort_keys)
"""
import json
import sys
from pathlib import Path


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

    # ประกอบ bank — ลำดับ key ต้องตรงกับ migrate_bank.py
    return {
        'schemaVersion': manifest['schemaVersion'],
        'exported': manifest['exported'],
        'topicNames': manifest['topicNames'],
        'sets': manifest['sets'],
        'questions': all_questions,
    }


def main() -> int:
    # หา data/ folder
    if len(sys.argv) > 1:
        data_dir = Path(sys.argv[1])
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

    # Serialize — ใช้ format เดียวกับ migrate_bank.py เพื่อ round-trip ตรงกัน
    new_content = json.dumps(bank, ensure_ascii=False, indent=2)

    n_sets = len(bank['sets'])
    n_questions = len(bank['questions'])

    # เช็คว่าเปลี่ยนจริงไหม — ถ้าไม่เปลี่ยนก็ไม่เขียน (กัน mtime noise)
    output_path = data_dir / 'bank.json'
    if output_path.exists():
        old_content = output_path.read_text(encoding='utf-8')
        if old_content == new_content:
            print(
                f"✅ bank.json ไม่เปลี่ยน "
                f"({n_sets} sets, {n_questions} questions, {len(new_content):,} chars)"
            )
            return 0

    # เขียนไฟล์
    output_path.write_text(new_content, encoding='utf-8')
    print(
        f"✅ Built bank.json: {n_sets} sets, {n_questions} questions, "
        f"{len(new_content):,} chars"
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())

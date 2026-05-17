#!/usr/bin/env python3
"""
apply_tag_changes.py — apply tag changes from tag-changes-*.json file (Phase 3)

อ่านไฟล์ tag-changes ที่ download มาจาก admin.html → update data/sets/*.json
ตามที่คุณครูแก้ในเบราว์เซอร์

Schema ของไฟล์ tag-changes-*.json:
{
  "exported": "ISO timestamp",
  "schemaVersion": "3.0",
  "changeCount": N,
  "changes": [
    {
      "id": "samn-XXXX-XX-qNN",
      "previousTopics": ["..."],
      "previousSubTopics": ["..."],
      "newTopics": ["..."],
      "newSubTopics": ["..."]
    },
    ...
  ]
}

ความปลอดภัย:
  • Default = DRY-RUN — แสดง diff ไม่เขียนไฟล์
  • Idempotent — รันซ้ำให้ผลเหมือนเดิม (skip ข้อที่ matches new state อยู่แล้ว)
  • Warn ถ้า previousTopics/SubTopics ใน file ไม่ตรงกับใน sets/ (อาจมี concurrent edit)
  • Preserve format byte-identical กับ build_bank.py
    (ensure_ascii=False, indent=2, ไม่ sort_keys)

Usage:
  python scripts/apply_tag_changes.py path/to/tag-changes-2026-05-17-1430.json
  python scripts/apply_tag_changes.py path/to/tag-changes-2026-05-17-1430.json --apply
"""
import json
import sys
from pathlib import Path


def apply_changes(data_dir: Path, changes: list, apply_mode: bool) -> int:
    sets_dir = data_dir / 'sets'
    if not sets_dir.is_dir():
        print(f'❌ ไม่พบโฟลเดอร์ {sets_dir}', file=sys.stderr)
        return 1

    # Index changes by question id for fast lookup
    changes_by_id = {c['id']: dict(c) for c in changes}
    remaining = set(changes_by_id.keys())

    files_modified = []
    total_applied = 0
    total_skipped_idempotent = 0   # already matches new state
    total_drift = 0                # previousTopics in file != current in sets

    for set_file in sorted(sets_dir.glob('*.json')):
        with open(set_file, 'r', encoding='utf-8') as f:
            set_data = json.load(f)

        file_modified = False
        for q in set_data.get('questions', []):
            qid = q.get('id')
            if qid not in changes_by_id:
                continue
            remaining.discard(qid)

            change = changes_by_id[qid]
            new_topics = change['newTopics']
            new_sub = change['newSubTopics']
            prev_topics_in_file = change.get('previousTopics', [])
            prev_sub_in_file = change.get('previousSubTopics', [])

            current_topics = q.get('topics', [])
            current_sub = q.get('subTopics', [])

            # Already matches new state → idempotent skip
            if current_topics == new_topics and current_sub == new_sub:
                total_skipped_idempotent += 1
                continue

            # Drift detection: file says previous=X but disk has Y
            # (อาจเกิดถ้ามี edit concurrent ระหว่างที่ครู export ⇄ apply)
            drift = False
            if current_topics != prev_topics_in_file or current_sub != prev_sub_in_file:
                drift = True
                total_drift += 1
                print(f'  ⚠️  DRIFT  {qid}')
                print(f'      file expected: topics={prev_topics_in_file} subTopics={prev_sub_in_file}')
                print(f'      disk has:      topics={current_topics} subTopics={current_sub}')
                print(f'      will overwrite to: topics={new_topics} subTopics={new_sub}')
            else:
                print(f'  ✏️  {qid}: topics {current_topics} → {new_topics}'
                      f'  subTopics {current_sub} → {new_sub}')

            if apply_mode:
                q['topics'] = new_topics
                q['subTopics'] = new_sub

            total_applied += 1
            file_modified = True

        if file_modified and apply_mode:
            new_content = json.dumps(set_data, ensure_ascii=False, indent=2)
            set_file.write_text(new_content, encoding='utf-8')
            files_modified.append(set_file.name)

    print()
    print('═' * 64)
    print('📊 SUMMARY')
    print('═' * 64)
    print(f'Changes in file:           {len(changes)}')
    print(f'Applied:                   {total_applied}')
    print(f'Skipped (idempotent):      {total_skipped_idempotent}')
    if total_drift:
        print(f'⚠️  Drift detected:         {total_drift}  (file expected != disk; overwritten)')
    if remaining:
        print(f'⚠️  Not found in any set:   {len(remaining)}')
        for qid in sorted(remaining):
            print(f'      • {qid}')

    print()
    if apply_mode:
        print(f'✅ {len(files_modified)} files written:')
        for f in files_modified:
            print(f'      • data/sets/{f}')
        if files_modified:
            print()
            print('🎯 Next: verify diff ใน GitHub Desktop → push')
            print('   GitHub Actions จะ rebuild bank.json อัตโนมัติ')
    else:
        print('💡 DRY-RUN. To actually write files:')
        changes_file = sys.argv[1] if len(sys.argv) > 1 else '<changes.json>'
        print(f'    python scripts/apply_tag_changes.py {changes_file} --apply')

    return 0


def main(argv: list[str]) -> int:
    apply_mode = '--apply' in argv
    positional = [a for a in argv[1:] if not a.startswith('--')]

    if not positional:
        print('Usage: python scripts/apply_tag_changes.py <changes.json> [--apply]',
              file=sys.stderr)
        return 1

    changes_file = Path(positional[0])
    if not changes_file.exists():
        print(f'❌ ไม่พบไฟล์ {changes_file}', file=sys.stderr)
        return 1

    try:
        with open(changes_file, 'r', encoding='utf-8') as f:
            payload = json.load(f)
    except json.JSONDecodeError as e:
        print(f'❌ JSON parse error: {e}', file=sys.stderr)
        return 1

    changes = payload.get('changes', [])
    if not isinstance(changes, list):
        print('❌ "changes" field is not a list', file=sys.stderr)
        return 1

    print(f'📂 Changes file:   {changes_file.name}')
    print(f'⏰ Exported:       {payload.get("exported", "?")}')
    print(f'📝 Total changes:  {len(changes)}')
    print(f'🔧 Mode:           {"APPLY (writing files)" if apply_mode else "DRY-RUN (no writes)"}')
    print()

    # Find data/ dir (assume scripts/apply_tag_changes.py → ../data/)
    script_dir = Path(__file__).parent
    data_dir = (script_dir.parent / 'data').resolve()
    print(f'📂 Data folder:    {data_dir}')
    print()

    return apply_changes(data_dir, changes, apply_mode)


if __name__ == '__main__':
    sys.exit(main(sys.argv))

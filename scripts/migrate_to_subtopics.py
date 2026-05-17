#!/usr/bin/env python3
"""
migrate_to_subtopics.py
=======================

Phase 1 ของ tag audit + schema migration:
  1. เพิ่ม `subTopics: []` field ให้ทุก question ที่ยังไม่มี
  2. Apply tag audit — เพิ่ม "1" ลงใน subTopics ของ 43 ข้อที่ใช้ทฤษฎีเซตเป็น tool

Schema (ก่อน → หลัง):
  Before:  { "topics": ["7"] }
  After:   { "topics": ["7"], "subTopics": ["1"] }   ← ถ้าอยู่ใน TAG_AUDIT_LIST
           { "topics": ["7"], "subTopics": [] }       ← ถ้าไม่อยู่ใน list

ความปลอดภัย:
  • Default = DRY-RUN — แค่แสดง diff ไม่เขียนไฟล์
  • Idempotent — รัน 2 ครั้งให้ผลเหมือนเดิม (จะไม่ duplicate "1" ใน subTopics)
  • ถ้า "1" อยู่ใน topics อยู่แล้ว → ไม่เพิ่มใน subTopics (กัน double-tag)
  • Preserve format ตรง byte-identical กับ build_bank.py
    (ensure_ascii=False, indent=2, ไม่ sort_keys)

Usage:
  python scripts/migrate_to_subtopics.py            # DRY-RUN (default)
  python scripts/migrate_to_subtopics.py --apply    # เขียนไฟล์จริง
  python scripts/migrate_to_subtopics.py path/to/data --apply
"""
import json
import sys
from collections import OrderedDict
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────
# Tag audit results — 43 ข้อที่ผ่านการ review แล้ว ให้เพิ่ม "1" (เซต) ใน subTopics
# ─────────────────────────────────────────────────────────────────────────
TAG_AUDIT_ADD_SET = {
    # ── Group A: เซตเป็น tool ในตรรกศาสตร์ (เอกภพสัมพัทธ์) — 32 ข้อ ──
    'samn-2564-04-q02',
    'samn-2565-03-q02',
    'chap-02-logic-q43',
    'chap-02-logic-q44',
    'chap-02-logic-q45',
    'chap-02-logic-q46',
    'chap-02-logic-q52',
    'chap-02-logic-q56',
    'chap-02-logic-q59',
    'chap-02-logic-q61',
    'chap-02-logic-q62',
    'chap-02-logic-q63',
    'chap-02-logic-q65',
    'chap-02-logic-q66',
    'chap-02-logic-q67',
    'chap-02-logic-q68',
    'chap-02-logic-q69',
    'chap-02-logic-q70',
    'chap-02-logic-q71',
    'chap-02-logic-q72',
    'chap-02-logic-q103',
    'chap-02-logic-q104',
    'chap-02-logic-q105',
    'chap-02-logic-q106',
    'chap-02-logic-q107',
    'chap-02-logic-q108',
    'chap-02-logic-q109',
    'chap-02-logic-q110',
    'chap-02-logic-q111',
    'chap-02-logic-q112',
    'chap-02-logic-q113',
    'chap-02-logic-q115',
    # ── Group B: เซตเป็น tool ในบทอื่น ๆ — 11 ข้อ ──
    'samn-2555-01-q19',    # บท 8: S1 ∩ S2
    'samn-2556-01-q27',    # บท 10: A ∩ B
    'samn-2558-01-q13',    # บท 10: A ∩ B
    'samn-2558-01-q27',    # บท 10,13: พื้นที่ A ∩ B
    'samn-2558-12-q19',    # บท 7: S เป็นสับเซตของเซตใด
    'samn-2559-12-q08',    # บท 12: W = {A | A ⊂ S}
    'samn-2559-12-q12',    # บท 3: A ∩ B
    'samn-2559-12-q20',    # บท 12: สับเซต + intersection
    'samn-2564-04-q06',    # บท 8: เซตคำตอบ ⊂ เซตใด
    'samn-2565-03-q07',    # บท 8: A ∪ B
    'samn-2565-03-q16',    # บท 4: S ∩ T (จุดในระนาบ)
}


# ─────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────
def insert_subtopics_after_topics(q: dict) -> dict:
    """
    Return a new dict with `subTopics` inserted right after `topics`.
    Preserves all other field ordering (Python 3.7+ dict order).
    """
    if 'subTopics' in q:
        return q  # already has it — no reorder needed
    new_q = OrderedDict()
    for key, value in q.items():
        new_q[key] = value
        if key == 'topics':
            new_q['subTopics'] = []
    # Safety: ถ้าไม่มี topics ใน q (เคสประหลาด) ก็ append ท้าย
    if 'subTopics' not in new_q:
        new_q['subTopics'] = []
    return new_q


def apply_migration(set_data: dict) -> tuple[dict, list[dict]]:
    """
    Mutate set_data (ใหม่) + return (modified_data, list_of_changes).

    changes = [{id, action, before, after}]
        action ∈ {"add-subtopics-field", "add-set-tag", "skip-already-tagged"}
    """
    changes = []
    new_questions = []

    for q in set_data.get('questions', []):
        qid = q.get('id', '')
        original_topics = list(q.get('topics', []))
        had_subtopics_field = 'subTopics' in q
        original_subtopics = list(q.get('subTopics', []))

        # Step 1: ensure subTopics field exists (insert after topics)
        new_q = insert_subtopics_after_topics(dict(q))

        # Step 2: apply tag audit (add "1" to subTopics if applicable)
        if qid in TAG_AUDIT_ADD_SET:
            if '1' in original_topics:
                # มี "1" เป็น primary อยู่แล้ว — ไม่ต้อง tag เพิ่ม
                changes.append({
                    'id': qid,
                    'action': 'skip-already-primary',
                    'note': 'topics มี "1" อยู่แล้ว (เป็น primary)',
                })
            elif '1' in original_subtopics:
                # มี "1" ใน subTopics อยู่แล้ว — idempotent skip
                changes.append({
                    'id': qid,
                    'action': 'skip-already-subtagged',
                    'note': 'subTopics มี "1" อยู่แล้ว',
                })
            else:
                new_q['subTopics'] = list(new_q['subTopics']) + ['1']
                changes.append({
                    'id': qid,
                    'action': 'add-set-tag',
                    'before': {'topics': original_topics, 'subTopics': original_subtopics},
                    'after': {'topics': original_topics, 'subTopics': new_q['subTopics']},
                })
        elif not had_subtopics_field:
            # ไม่ใช่ tag audit target — แต่ต้อง migrate schema (เพิ่ม subTopics: [])
            changes.append({
                'id': qid,
                'action': 'add-subtopics-field',
            })

        new_questions.append(new_q)

    new_data = {
        **{k: v for k, v in set_data.items() if k != 'questions'},
        'questions': new_questions,
    }
    return new_data, changes


def serialize(data: dict) -> str:
    """Match build_bank.py format exactly."""
    return json.dumps(data, ensure_ascii=False, indent=2)


# ─────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────
def main(argv: list[str]) -> int:
    apply_mode = '--apply' in argv
    args = [a for a in argv[1:] if not a.startswith('--')]

    # Locate data dir
    if args:
        data_dir = Path(args[0])
    else:
        script_dir = Path(__file__).parent
        data_dir = script_dir.parent / 'data'
    data_dir = data_dir.resolve()

    sets_dir = data_dir / 'sets'
    if not sets_dir.is_dir():
        print(f'❌ ไม่พบ {sets_dir}', file=sys.stderr)
        return 1

    print(f'📂 Data folder: {data_dir}')
    print(f'🔧 Mode: {"APPLY (writing files)" if apply_mode else "DRY-RUN (no writes)"}')
    print()

    # Cumulative stats
    total_files = 0
    total_questions = 0
    total_schema_migrations = 0
    total_set_tags_added = 0
    total_skipped = 0
    files_modified = []
    audit_hits = set()

    # Process each sets/*.json file
    for set_file in sorted(sets_dir.glob('*.json')):
        total_files += 1
        with open(set_file, 'r', encoding='utf-8') as f:
            set_data = json.load(f)

        new_data, changes = apply_migration(set_data)
        total_questions += len(set_data.get('questions', []))

        # Stats
        n_schema = sum(1 for c in changes if c['action'] == 'add-subtopics-field')
        n_tag = sum(1 for c in changes if c['action'] == 'add-set-tag')
        n_skip = sum(1 for c in changes if c['action'].startswith('skip'))
        total_schema_migrations += n_schema
        total_set_tags_added += n_tag
        total_skipped += n_skip

        # Track audit hits for verification at end
        for c in changes:
            if c['action'] in ('add-set-tag', 'skip-already-primary', 'skip-already-subtagged'):
                audit_hits.add(c['id'])

        # Per-file diff
        old_content = serialize(set_data)
        new_content = serialize(new_data)
        if old_content != new_content:
            files_modified.append(set_file.name)
            print(f'📝 {set_file.name}')
            print(f'   schema migration: {n_schema} questions')
            print(f'   set tag added:    {n_tag} questions')
            if n_skip:
                print(f'   skipped:          {n_skip} questions (already tagged)')
            # Show first 3 tag audit hits per file (preview)
            tag_changes = [c for c in changes if c['action'] == 'add-set-tag']
            for c in tag_changes[:3]:
                print(f'     • {c["id"]}: topics={c["before"]["topics"]} '
                      f'→ subTopics={c["after"]["subTopics"]}')
            if len(tag_changes) > 3:
                print(f'     • ... และอีก {len(tag_changes)-3} ข้อ')
            print()

            if apply_mode:
                set_file.write_text(new_content, encoding='utf-8')

    # Verify TAG_AUDIT_ADD_SET coverage
    missing = TAG_AUDIT_ADD_SET - audit_hits
    extra = audit_hits - TAG_AUDIT_ADD_SET

    print('═══════════════════════════════════════════════')
    print('📊 SUMMARY')
    print('═══════════════════════════════════════════════')
    print(f'Files scanned:           {total_files}')
    print(f'Questions scanned:       {total_questions}')
    print(f'Files to modify:         {len(files_modified)}')
    print(f'Schema migrations:       {total_schema_migrations}  (เพิ่ม subTopics: [])')
    print(f'Set tags added:          {total_set_tags_added}     (เพิ่ม "1" ใน subTopics)')
    print(f'Skipped (idempotent):    {total_skipped}')
    print()
    print(f'Tag audit target:        {len(TAG_AUDIT_ADD_SET)} ข้อ')
    print(f'Tag audit hits:          {len(audit_hits)} ข้อ')
    if missing:
        print(f'⚠️  Missing (not found in any set): {sorted(missing)}')
    if not missing and not extra:
        print('✅ Tag audit ครบ ตรงตาม TAG_AUDIT_ADD_SET')

    print()
    if apply_mode:
        print('✅ Files written. Next: verify diff in GitHub Desktop, then push.')
    else:
        print('💡 This was a DRY-RUN. To actually write files:')
        print('    python scripts/migrate_to_subtopics.py --apply')

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

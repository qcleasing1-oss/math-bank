# -*- coding: utf-8 -*-
"""รันตรรกะจริงของด่าน 7 (check_answer_claim.py v1.3) กับ 5 ข้อใหม่
   ⛔ ไม่ก็อปโค้ด — import ฟังก์ชันจากไฟล์จริงใน /tmp/mb27"""
import importlib.util, io, json, glob, sys

spec = importlib.util.spec_from_file_location(
    'cac', '/tmp/mb27/scripts/check_answer_claim.py')
cac = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cac)
print('CHECKER_VERSION =', cac.CHECKER_VERSION)

files = sorted(glob.glob('/home/claude/k2/out/k2-*.json'))
assert files, 'ไม่พบไฟล์'
bad = 0
for fp in files:
    d = json.load(io.open(fp, encoding='utf-8'))
    for q in d['questions']:
        elig = cac.eligible(q)
        kind, val = cac.declared_choice(q['explanation'])
        want = q['correct'] + 1
        ok = elig and kind == 'one' and val == want
        print('  %s | eligible=%s | %-4s %-6s | correct+1 = %d | %s'
              % (q['id'], elig, kind, val, want, '✅' if ok else '🔴'))
        if not ok:
            bad += 1
print()
print('ประกาศครบทุกข้อ ⇒ หนี้ใหม่ที่เพิ่มให้ด่าน 7 =', bad, 'ข้อ')
sys.exit(1 if bad else 0)

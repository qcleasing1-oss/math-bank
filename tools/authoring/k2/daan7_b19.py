# -*- coding: utf-8 -*-
"""รันตรรกะจริงของด่าน 7 (check_answer_claim.py) กับ 20 ข้อของก้อน 19
   ⛔ ไม่ก็อปโค้ด — import ฟังก์ชันจากไฟล์จริงใน /tmp/mb27

⭐ เรื่องใหม่ของก้อน 19 : มีข้อชนิด fill 6 ข้อ
   `cac.eligible()` รับเฉพาะ type == 'mc' ⇒ ข้อ fill **ด่าน 7 มองไม่เห็นเลย**
   ⛔ "ด่านมองไม่เห็น" ไม่เท่ากับ "ตรวจแล้วผ่าน" ⇒ ไฟล์นี้จึงรายงานแยกสองถัง
      และบอกตรง ๆ ว่าข้อ fill ถูกตรวจด้วยอะไรแทน (audit44.py สายใหม่ + check_part_b19.py)
"""
import importlib.util, io, json, glob, sys

spec = importlib.util.spec_from_file_location(
    'cac', '/tmp/mb27/scripts/check_answer_claim.py')
cac = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cac)
print('CHECKER_VERSION =', cac.CHECKER_VERSION)

FILE = '/home/claude/k2/out/k2-ก้อน19-20ข้อ-7.1-7.11-7.3.json'
d = json.load(io.open(FILE, encoding='utf-8'))
bad = 0
nmc = nfill = 0
for q in d['questions']:
    if q.get('type') == 'fill':
        nfill += 1
        blob = json.dumps(q, ensure_ascii=False)
        clean = 'ตัวเลือก' not in blob
        print('  %s | fill — ด่าน 7 มองไม่เห็น | ไม่มีคำว่า “ตัวเลือก” = %s | %s'
              % (q['id'], clean, '✅' if clean else '🔴'))
        if not clean:
            bad += 1
        continue
    nmc += 1
    elig = cac.eligible(q)
    kind, val = cac.declared_choice(q['explanation'])
    want = q['correct'] + 1
    ok = elig and kind == 'one' and val == want
    print('  %s | eligible=%s | %-4s %-6s | correct+1 = %d | %s'
          % (q['id'], elig, kind, val, want, '✅' if ok else '🔴'))
    if not ok:
        bad += 1

print()
print('ข้อปรนัย %d ข้อ ⇒ ประกาศเลขช่องได้ครบและตรงคีย์ทุกข้อ' % nmc)
print('ข้อ fill %d ข้อ ⇒ อยู่นอกขอบเขตของด่าน 7 โดยการออกแบบของด่านเอง' % nfill)
print('   ⇒ ตรวจแทนด้วย : audit44.py (correct เป็นสตริง · accept มีคำตอบหลัก · ห้ามคำว่า “ตัวเลือก”)')
print('   ⇒ และ check_part_b19.py (โครง STANDARD v2 · จุดพลาด >= 3 บรรทัด)')
print()
print('หนี้ใหม่ที่ก้อน 19 เพิ่มให้ด่าน 7 =', bad, 'ข้อ')
sys.exit(1 if bad else 0)

# -*- coding: utf-8 -*-
"""เทียบผล blind-solve QC กับคีย์ในคลัง — ⛔ รันในแชท**ผู้แต่ง** เท่านั้น

    python3 qc_compare.py <ไฟล์ผลจากแชท QC>.json

ไฟล์ผลที่รับ = JSON block ที่ skill `blind-solve-qc` ปิดท้ายรายงาน :
    {"results": [{"id": "...", "type": "mc", "answer_index0": 2,
                  "answer_value": null, "confidence": "สูง", "flags": []}, ...]}

⭐ ทำไมไม่มีไฟล์ `*-KEY.json` แยก : คีย์อยู่ใน `data/sets/*.json` ในคลังอยู่แล้ว
   ถ้าทำสำเนาคีย์ไว้อีกที่ (โดยเฉพาะใน project ที่แชท QC มองเห็นได้) ⇒ ซองรั่ว
   ⇒ ด่านนี้อ่านคีย์จากคลังโดยตรง ⛔ ไม่สร้างสำเนา

รหัสออก : 0 = ตรงกันหมดและไม่มีธง · 1 = มีข้อไม่ตรงหรือมีธง (ต้องอ่านทีละข้อ)
"""
import io, json, sys, glob, collections
from fractions import Fraction

SET = 'gen-chap-07-trigonometry'
MB = '/tmp/mb27'


def norm_fill(s):
    """เทียบคำตอบ fill แบบทนรูปแบบ : '9/40' · '0.225' · 0.225 ⇒ ค่าเดียวกัน"""
    if s is None:
        return None
    t = str(s).strip().replace('\\dfrac', '').replace('\\frac', '')
    t = t.replace('{', '').replace('}', '/').replace('$', '').strip().rstrip('/')
    try:
        if '/' in t:
            a, b = t.split('/')[:2]
            return Fraction(int(a.strip()), int(b.strip()))
        return Fraction(t)
    except Exception:
        return str(s).strip()


def main():
    if len(sys.argv) < 2:
        print('ใช้: python3 qc_compare.py <ไฟล์ผล QC>.json')
        sys.exit(2)
    res = json.load(io.open(sys.argv[1], encoding='utf-8'))
    if isinstance(res, dict):
        res = res.get('results', [])

    key = {}
    for p in sorted(glob.glob(MB + '/data/sets/*.json')):
        for q in json.load(io.open(p, encoding='utf-8')).get('questions', []):
            key[q['id']] = q

    agree = disagree = flagged = unknown = 0
    rows = []
    for r in res:
        qid = r.get('id')
        q = key.get(qid)
        if q is None:
            unknown += 1
            rows.append((qid, '❓ ไม่พบข้อนี้ในคลัง', '', ''))
            continue
        fl = r.get('flags') or []
        if fl:
            flagged += 1
            rows.append((qid, '🚩 ' + ' · '.join(fl), 'ความมั่นใจ ' + str(r.get('confidence')), ''))
            continue
        if q['type'] == 'mc':
            got, want = r.get('answer_index0'), q['correct']
            ok = got == want
            shown = ('ช่อง %s' % (got + 1) if isinstance(got, int) else str(got),
                     'ช่อง %d' % (want + 1))
        else:
            got, want = norm_fill(r.get('answer_value')), norm_fill(q['correct'])
            ok = got == want
            shown = (str(r.get('answer_value')), str(q['correct']))
        if ok:
            agree += 1
        else:
            disagree += 1
            rows.append((qid, '🔴 ไม่ตรงคีย์', 'ผู้แก้ตอบ ' + shown[0], 'คลังเก็บ ' + shown[1]))

    print('=' * 78)
    print('เทียบผล blind-solve %d ข้อ' % len(res))
    print('=' * 78)
    for a, b, c, d in rows:
        print('  %-38s %-26s %-22s %s' % (a, b, c, d))
    if not rows:
        print('  (ไม่มีข้อที่ต้องดูด้วยตา)')
    print()
    print('  ตรงกับคีย์        %d' % agree)
    print('  🔴 ไม่ตรงคีย์      %d   ⇒ ต้องตัดสินว่า "เฉลยเราผิด" หรือ "ผู้แก้พลาด" ทีละข้อ' % disagree)
    print('  🚩 ติดธง          %d   ⇒ โจทย์อาจกำกวม/ข้อมูลไม่พอ ⛔ ไม่ใช่ความผิดของผู้แก้' % flagged)
    print('  ❓ ไม่พบในคลัง     %d' % unknown)
    print()
    print('⛔ "ตรงกับคีย์" ไม่เท่ากับ "ข้อดี" — ข้อที่ผู้แก้ตอบถูกแต่ความมั่นใจต่ำ ก็ยังต้องอ่าน')
    low = [r['id'] for r in res if r.get('confidence') == 'ต่ำ' and not (r.get('flags') or [])]
    if low:
        print('   ข้อที่ตอบได้แต่ความมั่นใจต่ำ %d ข้อ : %s' % (len(low), ' '.join(low)))
    sys.exit(1 if (disagree or flagged or unknown) else 0)


if __name__ == '__main__':
    main()

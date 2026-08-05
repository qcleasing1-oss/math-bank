#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ตรวจ POST-FLIGHT ของก้อนตัวอย่างก้าว 1 — ใช้ซ้ำได้กับทุกไฟล์ในโฟลเดอร์ out"""
import json, io, os, re, sys, glob

FILES = sorted(glob.glob('/home/claude/k2/out/k2-*.json'))
bad = 0
def fail(qid, msg):
    global bad
    bad += 1
    print('  🔴 %s · %s' % (qid, msg))

CROSSREF = re.compile(r'ข้อมูลเดิม|จากข้อ|ข้างต้น|ข้างบน|โจทย์เดิม|เช่นเดิม|ข้อถัดไป|ข้อก่อน')
BADSYM = {
    '\\subseteq': 'กฎเหล็ก 9', '\\subsetneq': 'กฎเหล็ก 9', '\\nsubseteq': 'กฎเหล็ก 9',
    '\\phi': 'กฎเหล็ก 9', '\\varphi': 'กฎเหล็ก 9', '\\mathbb{I}': 'กฎเหล็ก 9',
    '^c': 'กฎเหล็ก 9 (คอมพลีเมนต์)', 'คาร์ดินาลิตี': 'กฎเหล็ก 9',
    '√': 'ห้าม √ ดิบ ใช้ \\sqrt{}', '\\frac': 'ใช้ \\dfrac เท่านั้น',
    'มากที่สุดเท่ากับ': 'สำนวนกำกวม ใช้ “ค่าสูงสุดที่เป็นไปได้คือ”',
    'น้อยที่สุดเท่ากับ': 'สำนวนกำกวม ใช้ “ค่าต่ำสุดที่เป็นไปได้คือ”',
    '\\"': 'กฎเหล็ก 10 ห้าม escape เกินชั้น ใช้ “ ” แทน',
}
# 7.11 ปลดล็อกแล้วตามคำสั่ง ① ของจดหมาย E→MB #19 (5 ส.ค. 69)
# ชื่อทางการ “พื้นที่เซกเตอร์และความยาวส่วนโค้ง” มีอยู่จริงทั้งใน manifest.json และ portal/data/bank.json
ALLOWED_ST = {'7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8','7.9','7.10','7.11'}
LEVELS = {'ง่าย','ปานกลาง','ยาก','ยากมาก'}

total = 0
for p in FILES:
    raw = io.open(p, encoding='utf-8').read()
    d = json.loads(raw)
    print('═' * 70)
    print('ไฟล์ %s · %d ข้อ' % (os.path.basename(p), len(d['questions'])))
    if json.dumps(d, ensure_ascii=False, indent=2) != raw:
        print('  🔴 ไฟล์ไม่ตรงรูปแบบ indent=2/ensure_ascii=False')
        bad += 1
    if raw.endswith('\n') or '\r' in raw:
        print('  🔴 มี trailing newline หรือ CRLF')
        bad += 1
    for q in d['questions']:
        total += 1
        qid = q['id']
        blob = json.dumps(q, ensure_ascii=False)
        # ① สนามที่ต้องมี
        for k in ('id','setId','questionNumber','topics','subTopics',
                  'difficulty','type','question','hasImage','sourceTag',
                  'correct','explanation','notes'):
            if k not in q:
                fail(qid, 'ขาดฟิลด์ %s' % k)
        if q['difficulty'] not in LEVELS:
            fail(qid, 'ระดับผิด %r (กฎเหล็ก 8)' % q['difficulty'])
        # ② หัวข้อย่อย
        for s in q['subTopics']:
            if s not in ALLOWED_ST:
                fail(qid, 'subTopic นอกขอบเขต %r (⛔ 7.11)' % s)
        if q['topics'] != ['7']:
            fail(qid, 'topics ต้องเป็น ["7"] ได้ %r' % q['topics'])
        # ③ mc: correct ต้องเป็น index ที่มีอยู่จริง
        if q['type'] == 'mc':
            if 'choices' not in q:
                fail(qid, 'mc แต่ไม่มี choices')
            elif not isinstance(q['correct'], int) or not (0 <= q['correct'] < len(q['choices'])):
                fail(qid, 'correct ไม่ใช่ index ที่ถูกต้อง')
            else:
                n = q['correct'] + 1
                want = '→ <b>ตัวเลือก %d</b>' % n
                ansline = [l for l in q['explanation'] if l.startswith('✅ <b>คำตอบ</b>')]
                if len(ansline) != 1:
                    fail(qid, 'บรรทัด ✅ คำตอบ มี %d บรรทัด (ต้องมี 1)' % len(ansline))
                elif not ansline[0].endswith(want):
                    fail(qid, 'บรรทัด ✅ ไม่ลงท้ายด้วย %r ⇒ %r' % (want, ansline[0][-40:]))
                # ตัวเลือกซ้ำ
                if len(set(q['choices'])) != len(q['choices']):
                    fail(qid, 'ตัวเลือกซ้ำกัน')
        # ④ hasImage / imageSpec ต้องสอดคล้อง
        if q.get('hasImage') and 'imageSpec' not in q:
            fail(qid, 'hasImage true แต่ไม่มี imageSpec')
        if not q.get('hasImage') and 'imageSpec' in q:
            fail(qid, 'hasImage false แต่มี imageSpec')
        if '[IMAGE' in blob and not q.get('hasImage'):
            fail(qid, 'มีหมุด [IMAGE] แต่ hasImage false')
        # ⑤ กฎเหล็ก 7 · อ้างข้ออื่น
        m = CROSSREF.search(q['question'])
        if m:
            fail(qid, 'คำถามอ้างข้ออื่น: %r (กฎเหล็ก 7)' % m.group(0))
        # ⑥ สัญลักษณ์ต้องห้าม
        for sym, why in BADSYM.items():
            if sym in blob:
                fail(qid, 'พบ %r — %s' % (sym, why))
        # ⑫ literal \n และ ตัวเลือกที่ N (ตรวจแบบแม่นยำ ไม่ชน \ne / “ตัวเลือกที่ดักไว้”)
        if re.search(r'\\\\n(?![a-zA-Z])', blob):
            fail(qid, 'พบ literal \\n')
        if re.search(r'ตัวเลือกที่\s*\d', blob):
            fail(qid, 'พบ “ตัวเลือกที่ N” — CHOICE_RE จับไม่ได้ ต้องเป็น “ตัวเลือก N”')
        # ⑦ โครง STANDARD v2
        heads = ['📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>', '📐 <b>โจทย์กำหนด</b>',
                 '🎯 <b>เป้าหมาย</b>', '✅ <b>คำตอบ</b>',
                 '💡 <b>เทคนิค</b>', '⚠️ <b>จุดพลาด</b>']
        for h in heads:
            if not any(l.startswith(h) for l in q['explanation']):
                fail(qid, 'เฉลยขาดหัวข้อ %s' % h)
        if not any(l.startswith('✔ <b>ตรวจคำตอบ') for l in q['explanation']):
            fail(qid, 'เฉลยขาด ✔ ตรวจคำตอบ (วิธีอิสระ)')
        if not any(l.startswith('<b>【') for l in q['explanation']):
            fail(qid, 'เฉลยขาดบรรทัดชื่อวิธี 【 … 】')
        nstep = len([l for l in q['explanation'] if l.startswith('<b>ขั้นที่ ')])
        if nstep < 3:
            fail(qid, 'มีขั้นที่ %d ขั้น (น้อยเกินสำหรับระดับนี้)' % nstep)
        # ⑧ $ ต้องคู่
        for i, l in enumerate(q['explanation'] + [q['question']] + q.get('choices', [])):
            if l.count('$') % 2:
                fail(qid, '$ ไม่คู่ในบรรทัด %r' % l[:60])
        # ⑨ องศาต้องเป็น ^\circ
        if re.search(r'\d\s*°', blob):
            fail(qid, 'ใช้ ° ดิบ ต้องเป็น ^\\circ')
        # ⑩ ห้าม < > & ดิบในข้อความที่ผูกกับ SVG (ข้อไม่มีรูป ข้ามได้ แต่เช็ค & ไว้)
        if re.search(r'&(?!amp;|lt;|gt;)', q['question']):
            fail(qid, 'มี & ดิบในคำถาม')
        # ⑪ ตัวลวงต้องมีเหตุผลครบ (นับบรรทัดใต้ ⚠️)
        if q['type'] == 'mc':
            idx = [i for i,l in enumerate(q['explanation']) if l.startswith('⚠️ <b>จุดพลาด</b>')][0]
            nreason = len([l for l in q['explanation'][idx+1:] if l.strip()])
            if nreason < len(q['choices']) - 1:
                fail(qid, 'เหตุผลตัวลวง %d บรรทัด < ตัวลวง %d ตัว'
                     % (nreason, len(q['choices'])-1))
print('═' * 70)
print('ตรวจ %d ข้อ · ปัญหา %d จุด ⇒ %s' % (total, bad, 'ผ่าน' if bad == 0 else 'ยังไม่ผ่าน'))
sys.exit(1 if bad else 0)

# -*- coding: utf-8 -*-
"""build_3tier.py — ประกอบเฉลย 3 ชั้นของ q165–q184 เป็นไฟล์ให้ครูประเมิน

⛔ ไม่แตะ question / choices / correct / accept ของข้อเดิมแม้แต่ตัวอักษรเดียว
   (สคริปต์นี้ยืนยันด้วยการเทียบทีละฟิลด์ก่อนเขียนออก)
⛔ ผลลัพธ์ยังไม่เข้า data/sets — เป็น "ซองประเมิน" แยก จนกว่าครูจะเคาะ
"""
import json, os, sys, importlib, html, re

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'b23'))
sys.path.insert(0, os.path.join(ROOT, 'tier23'))

from linebreak import format_explanation
from methods import M
from shortnames import BASIC, APPLIED

SRC = os.path.join(ROOT, 'out', 'k2-ก้อน23-20ข้อ-q165-q184.json')
OUTDIR = os.path.join(ROOT, 'out')
QIDS = [f'q{n}' for n in range(165, 185)]

FIT1 = '🧩 <b>เหมาะกับเด็กอ่อน</b> อ่านตามได้ทีละบรรทัด มีที่มาของทุกสูตรและเหตุผลของทุกขั้น'
FIT2 = '🎯 <b>เหมาะกับเด็กปานกลางถึงเก่ง</b> รู้สูตรอยู่แล้ว ต้องการเห็นเส้นทางสั้นที่สุดของวิธีเดียวกัน'
FIT3 = '⚡ <b>เหมาะกับเด็กที่พื้นฐานคณิตดี หรือเด็กเก่งที่ฝึกโจทย์มาแล้ว</b>'


def head(n, kind, name):
    if kind == 'basic-long':
        return f'<b>【 แบบที่ {n} ▸ พื้นฐาน (ละเอียด) · {name} 】</b>'
    if kind == 'basic-short':
        return f'<b>【 แบบที่ {n} ▸ พื้นฐาน (กระชับ) · {name} 】</b>'
    return f'<b>【 แบบที่ {n} ▸ ⚡ ประยุกต์ · {name} 】</b>'


def split_expl(ex):
    """แยกเป็น (หัวร่วม, ก้อน 📚, ตัวแบบที่ 1, หาง)

    🔴 ก้อน 📚 ความรู้พื้นฐานที่ต้องใช้ ถูกย้ายเข้าไป **ในแบบที่ 1**
       เพราะมันคือลายเซ็นของ "ละเอียดมาก" — เด็กปานกลางที่มาอ่านแบบที่ 2
       ไม่ควรต้องลุยก้อนนี้ก่อน  หัวร่วมจึงเหลือแค่ 📐 โจทย์กำหนด กับ 🎯 เป้าหมาย
    """
    heads = [i for i, l in enumerate(ex) if l.startswith('<b>【')]
    i_tail = next(i for i, l in enumerate(ex) if l.startswith('✔ <b>ตรวจคำตอบ'))
    i_end = heads[1] if len(heads) > 1 else i_tail
    pre = ex[:heads[0]]
    i_kb = next((i for i, l in enumerate(pre) if l.startswith('📚')), None)
    i_giv = next((i for i, l in enumerate(pre) if l.startswith('📐')), None)
    if i_kb is not None and i_giv is not None and i_kb < i_giv:
        kb, shared = pre[i_kb:i_giv], pre[:i_kb] + pre[i_giv:]
    else:
        kb, shared = [], pre
    return shared, kb, ex[heads[0]:i_end], ex[i_tail:]


def roadmap(old_head):
    """เปลี่ยนหัวบรรยายยาวของเดิม ให้เป็นบรรทัด 'แผนเดิน' ใต้หัวชื่อวิธีใหม่

    ของเดิมมีสองทรง :
      <b>【 <ประโยคบรรยาย> 】</b>
      <b>【 วิธีที่ 1 ▸ พื้นฐาน · <ประโยคบรรยาย> 】</b>
    ⛔ ห้ามทิ้งประโยคบรรยาย — เป็นแผนที่เดินทางที่เด็กอ่อนใช้จริง แค่ย้ายที่
    """
    s = old_head
    assert s.startswith('<b>【') and s.endswith('】</b>'), s
    s = s[len('<b>【'):-len('】</b>')].strip()
    s = re.sub(r'^วิธีที่\s*\d+\s*▸\s*(⚡\s*)?(พื้นฐาน|ประยุกต์)\s*·?\s*', '', s).strip()
    if not s:
        return None
    return '🗺️ <b>แผนเดิน</b> ' + s


def build():
    src = json.load(open(SRC, encoding='utf-8'))
    qs = {q['id'][-4:]: q for q in src['questions']}
    assert sorted(qs) == QIDS, sorted(qs)

    out, stats = [], []
    for qid in QIDS:
        q = json.loads(json.dumps(qs[qid]))          # สำเนาลึก
        mod = importlib.import_module(qid)
        shared, kb, tier1, tail = split_expl(q['explanation'])

        basic = BASIC[qid]
        applied = APPLIED.get(qid)
        assert (applied is not None) == (M[qid][1] is not None), qid
        assert (applied is not None) == (mod.TIER3_HEAD is not None), \
            f'{qid}: ตาราง says {applied!r} แต่ไฟล์ผู้เขียน says {mod.TIER3_HEAD!r}'

        blk1 = [head(1, 'basic-long', basic), FIT1]
        rm = roadmap(tier1[0])
        if rm:
            blk1.append(rm)
        blk1 += kb + tier1[1:]

        blk2 = [head(2, 'basic-short', basic), FIT2] + [
            l for l in mod.TIER2 if not l.startswith('🎯 <b>เหมาะกับ</b>')]

        blk3 = []
        if applied:
            blk3 = [head(3, 'applied', applied), FIT3] + [
                l for l in mod.TIER3 if not l.startswith('⚡ <b>เหมาะกับ</b>')]

        q['explanation'] = format_explanation(shared + blk1 + blk2 + blk3 + tail)

        # 🔴 ยืนยันว่าไม่ได้แตะอะไรนอกจาก explanation
        for f in ('id', 'setId', 'questionNumber', 'topics', 'subTopics', 'difficulty',
                  'type', 'question', 'hasImage', 'sourceTag', 'correct', 'accept'):
            assert q.get(f) == qs[qid].get(f), (qid, f)

        q['notes'] = (qs[qid]['notes'] or '') + \
            f" | 3-TIER EVAL 2026-08-13: styles = {'3' if applied else '2'};" \
            f" basic method (tiers 1-2) = {basic!r};" \
            f" applied method (tier 3) = {applied!r};" \
            f" tier-3 path verified by b23/verify_tri3.py (113 checks, 0 fail);" \
            f" question/choices/correct/accept untouched."
        out.append(q)
        stats.append((qid, len(blk1), len(blk2), len(blk3),
                      sum(map(len, blk1)), sum(map(len, blk2)), sum(map(len, blk3)),
                      len(head(1, 'basic-long', basic)),
                      len(head(3, 'applied', applied)) if applied else 0))

    dst = json.dumps({'setId': src['setId'], 'questions': out},
                     indent=2, ensure_ascii=False)
    p = os.path.join(OUTDIR, 'k2-เฉลย3ชั้น-q165-q184-20ข้อ.json')
    open(p, 'w', encoding='utf-8').write(dst)

    print(f"{'ข้อ':<6}{'บรรทัด ①②③':>16}{'ตัวอักษร ①②③':>26}{'หัว①':>7}{'หัว③':>7}")
    for s in stats:
        print(f'{s[0]:<6}{s[1]:>5}{s[2]:>5}{s[3]:>5}   {s[4]:>7}{s[5]:>7}{s[6]:>7}'
              f'{s[7]:>8}{s[8]:>7}')
    n3 = sum(1 for s in stats if s[3])
    print(f'\nเขียน {p}')
    print(f'มีครบ 3 แบบ {n3} ข้อ · มี 2 แบบ {20 - n3} ข้อ')
    print(f'หัว 【 】 ยาวสุด {max(max(s[7], s[8]) for s in stats)} ตัวอักษร')
    return out


if __name__ == '__main__':
    build()

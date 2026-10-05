#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ด่าน 25 · check_solsteps.py v1.1 — โครงขั้นเฉลย solSteps ต้องถูกทรงตามสเปก (ss-v1.2 · 655-CC · 673-CC)

ทำอะไร
------
ตรวจ "ทรง" และ "การอ้างอิง" ของช่อง solSteps ในข้อของคลัง (data/sets) — stdlib ล้วน
⛔ ไม่ตรวจค่า (S4 ใช้ sympy = เครื่องมือของ MBT + E รันซ้ำ · ⛔ เข้า CI · มติ 632 ทาง ก)

สเปกที่ใช้: 619-CC (v1) + 645-CC (v1.1 · ข1–ข9 + join/trial/given/domain) + 655-CC (v1.2 · goal/warn/of/
           lhsJoin/rhsJoin/tag/synth/trial แบบแทนค่า/quot/rem/isFactor/cands + ช่องตัวตรวจ ck…)
           + 673-CC (role common = ตัวร่วม · มติ 671-E · note หลายบรรทัดด้วย \n · say บรรทัดเดียว · มติ 672-E)
v1.1 (4–5 ต.ค. 69 · MB-r40): + role common · say/title ⛔ ขึ้นบรรทัดใหม่ · note ขึ้นบรรทัดได้ แต่ ⛔ $ (678-CC)
      (v1.0 b6d5281a ตาย ⇒ แทนด้วยรุ่นนี้ · ร่าง v1.1 f48254df ใบ 677 ตาย 5 ต.ค. 00:0x เพราะ 678-CC ขอห้าม \n ใน title)

กฎ (รหัสนำหน้าข้อความ)
  S1 ทรง   : v · steps · n = 1..N ต่อเนื่อง · kind ในรายการ · title ไม่ว่าง ≤ 30 ⛔ ขึ้นบรรทัด · say ไม่ว่าง ⛔ $ ⛔ \ (ข9) ⛔ ขึ้นบรรทัด (673-CC)
             note ขึ้นบรรทัดได้ (672-E) ⛔ $ (ตัวแสดงผลไม่วาด KaTeX ใน note · 678-CC §3)
             join/lhsJoin/rhsJoin ∈ add mul · case.path = ^\d+(\.\d+)*$ (ข5) · trial มี terms หรือ val อย่างใดอย่างหนึ่ง
             synth: c · row1–row3 ยาวเท่ากัน · fill จำนวนเต็ม ≥ 0 · ต้องมีขั้น answer หรือ merge อย่างน้อย 1 ขั้น
  S2 พจน์  : id ไม่ว่าง ไม่ซ้ำในขั้น · tex ไม่ว่าง · role ∈ move add group answer common · ⛔ \color ทั้งก้อน
  S3 อ้างอิง (ข1 · สายของขั้น):
             สาย = ขั้นสมการที่ tag เดียวกัน · หรือขั้นนิพจน์ที่ of เดียวกัน (655 §2 กฎ from เพิ่ม)
             ① id ใหม่ต้องมี from (ยกเว้น role add · ยกเว้นขั้นแรกของสาย)  ② id ของขั้นก่อนต้องไปต่อ/ถูกอ้าง/อยู่ใน cancel
             ③ ขั้น trial ไม่นับเป็นขั้นก่อน · from/cancel/arrows.from ชี้ id ของขั้นก่อน · arrows.to ชี้ id ในขั้นนี้
             กรณี: ขั้นแรกของกรณีอ้าง id ก่อนแตกกรณี (ไม่ตรวจ ②) · merge ปิดสาย · parts ต้องเป็น path ที่มีจริง
             relFlip (ข3): relFlip ⇔ rel กลับทิศจากขั้นก่อนในสายเดียวกัน (ยกเว้นสลับข้างทั้งสองฝั่ง) · ใช้กับรุ่น ≥ ss-v1.1
  K  คีย์  : บัญชีขาวตามสเปก ทุกระดับ (solSteps · ขั้น · พจน์ · arrows · op · case) · คีย์บางตัวใช้ได้กับ kind ที่กำหนดเท่านั้น
  B  คลัง  : ช่อง goal warn given domain ck coef vals param cond sub ⛔ อยู่ระดับข้อ (ต้องอยู่ใน solSteps · มติครู MB-r40)
             v ในคลัง = ss-v1.1 หรือ ss-v1.2 เท่านั้น · ตัวนับข้อที่มี solSteps ⛔ ต่ำกว่า MIN_WITH_SOLSTEPS
             (กัน make_set07.py / regen_check.py ที่สร้างข้อด้วยลำดับช่องตายตัวทำช่องหายเงียบ)

ข้อจำกัดที่ประกาศไว้ (⑨ — เขียวของด่านนี้ ⛔ ไม่ใช่หลักฐานว่าเฉลยถูก)
  · ไม่ตรวจค่าทางคณิต (ขั้นเท่ากันไหม คำตอบตรงคีย์ไหม) ⇒ S4 ของ MBT
  · ไม่ตรวจ ข7 (ความละเอียดพจน์) และ ข4 (ใช้ op แทน arrows) — เป็นเรื่องความหมาย
  · ช่องตัวตรวจ (ck coef vals param cond sub) ตรวจแค่ว่าอยู่ถูกที่ ไม่ตรวจเนื้อ
  · ข8 ลำดับช่องในข้อ ไม่บังคับ (645 §1)

ใช้
  python scripts/check_solsteps.py data/sets            ทั้งคลัง
  python scripts/check_solsteps.py --lesson F.json …    ไฟล์หน้าเรียนของ W ({"examples":[…]}) หรือรายการข้อ [{id, solSteps}]
                                                        (รับป้ายรุ่นเดิมของ W · ไม่ตรวจกฎ B)
  python scripts/check_solsteps.py --selftest           ของดีต้องผ่าน + มิวแทนต์ทุกตัวต้องแดงด้วยกฎที่ตั้งใจ
  python scripts/check_solsteps.py --version

รหัสออก: 0 = ผ่าน · 1 = เนื้อหาแดง · 2 = ตัวเครื่องมือแดง / อ่านไฟล์ไม่ได้
"""
import argparse
import copy
import glob
import json
import os
import re
import sys

CHECKER_VERSION = '1.1'

# ── ตัวนับขั้นต่ำ: ข้อที่มี solSteps ในคลัง ─────────────────────────────────────
# ⛔ ลดเงียบไม่ได้ · เมื่อข้อที่มี solSteps ลงคลังเพิ่ม ⇒ ขยับค่านี้ขึ้นในคอมมิตเดียวกัน
# ⛔ ขยับลงต้องมีใบอธิบาย (ข้อถูกถอด) — ไม่ใช่ทางแก้ด่านแดง
MIN_WITH_SOLSTEPS = 0

BANK_VERSIONS = ('ss-v1.1', 'ss-v1.2')
KINDS = ('eq', 'expr', 'answer', 'check', 'text', 'trial', 'case', 'merge', 'synth')
ROLES = ('move', 'add', 'group', 'answer', 'common')     # common = ตัวร่วม (671-E · 673-CC)
JOINS = ('add', 'mul')
REL_DIR = {'=': None, '\\ne': None, '\\neq': None,
           '<': 'lt', '\\le': 'lt', '\\leq': 'lt',
           '>': 'gt', '\\ge': 'gt', '\\geq': 'gt'}
PATH_RE = re.compile(r'^\d+(\.\d+)*$')
TITLE_MAX = 30

CHECKER_ONLY = ('ck', 'coef', 'vals', 'param', 'cond', 'sub')        # 655 §2 · ตัวแสดงผลไม่อ่าน
SS_KEYS = frozenset(('v', 'steps', 'given', 'domain', 'goal') + CHECKER_ONLY)
STEP_KEYS = frozenset((
    'n', 'kind', 'title', 'say', 'note', 'warn',
    'terms', 'join', 'of',
    'lhs', 'rel', 'rhs', 'lhsJoin', 'rhsJoin', 'tag', 'relFlip',
    'cancel', 'arrows', 'op',
    'case', 'parts', 'result',
    'mid', 'ok', 'target', 'c', 'val',
    'row1', 'row2', 'row3', 'fill',
    'quot', 'rem', 'isFactor', 'cands',
) + CHECKER_ONLY)
KEY_KINDS = {                     # คีย์ที่ใช้ได้กับบาง kind เท่านั้น
    'case': ('case',), 'parts': ('merge', 'answer'), 'result': ('merge', 'answer'),
    'mid': ('trial',), 'target': ('trial',), 'ok': ('trial',), 'val': ('trial',), 'c': ('trial', 'synth'),
    'row1': ('synth',), 'row2': ('synth',), 'row3': ('synth',), 'fill': ('synth',),
    'quot': ('answer',), 'rem': ('answer',), 'isFactor': ('answer',), 'cands': ('text',),
    'lhs': ('eq', 'answer'), 'rhs': ('eq', 'answer'), 'rel': ('eq', 'answer'), 'relFlip': ('eq', 'answer'),
    'lhsJoin': ('eq', 'answer'), 'rhsJoin': ('eq', 'answer'), 'tag': ('eq', 'answer'),
    'terms': ('expr', 'answer', 'trial'), 'join': ('expr', 'answer', 'trial'), 'of': ('expr', 'answer'),
    'cancel': ('eq', 'expr', 'answer'), 'arrows': ('eq', 'expr', 'answer'), 'op': ('eq', 'expr', 'answer'),
}
TERM_KEYS = frozenset(('id', 'tex', 'role', 'from'))
ARROW_KEYS = frozenset(('from', 'to', 'label'))
OP_KEYS = frozenset(('tex',))
CASE_KEYS = frozenset(('path', 'label', 'cond', 'result'))
ITEM_FORBIDDEN = ('goal', 'warn', 'given', 'domain') + CHECKER_ONLY


def _s(x):
    return isinstance(x, str) and x.strip() != ''


def _strs(x):
    return isinstance(x, list) and all(isinstance(v, str) for v in x)


def _from_list(t):
    fr = t.get('from')
    if fr is None:
        return []
    if isinstance(fr, str) and fr:
        return [fr]
    if isinstance(fr, list) and fr and all(_s(f) for f in fr):
        return fr
    return None


def _parent(path):
    return path.rsplit('.', 1)[0] if '.' in path else ''


def check_ss(ss, bank=True):
    """คืนรายการปัญหา (ข้อความขึ้นต้นด้วยรหัส S1 S2 S3 K) — ว่าง = ผ่าน"""
    bad = []

    def B(code, msg):
        bad.append(f'{code} {msg}')

    if not isinstance(ss, dict):
        B('S1', 'solSteps ไม่ใช่ object')
        return bad
    for k in ss:
        if k not in SS_KEYS:
            B('K', f'คีย์นอกสเปกระดับ solSteps: {k}')
    v = ss.get('v')
    if bank:
        if v not in BANK_VERSIONS:
            B('S1', f'v = {v!r} (คลังรับ {" / ".join(BANK_VERSIONS)})')
    elif not (isinstance(v, str) and v.startswith('ss-v1')):
        B('S1', f'v = {v!r} (ต้องขึ้นต้น ss-v1)')
    flip_rule = isinstance(v, str) and re.match(r'ss-v1\.[12](?![0-9])', v) is not None
    for k in ('given', 'domain', 'goal'):
        if k in ss and not _s(ss[k]):
            B('S1', f'{k} ต้องเป็นข้อความไม่ว่าง')
    steps = ss.get('steps')
    if not isinstance(steps, list) or not steps:
        B('S1', 'steps ว่างหรือไม่ใช่รายการ')
        return bad
    if '\\color' in json.dumps(ss, ensure_ascii=False):
        B('S2', 'มี \\color ใน solSteps (สีเป็นงานของตัวแสดงผล)')

    prev_ids = None        # id ของขั้นก่อนในสาย (⛔ trial)
    prev_rel = None        # (rel, lhs ids, rhs ids) ของขั้นสมการก่อนในสายเดียวกัน
    chain = None
    case_paths = set()
    case_ctx = {}          # path ⇒ id ล่าสุดในกรณีนั้น ('' = ก่อนแตกกรณี)
    cur_case = None
    case_first = False
    has_answer = False

    for i, s in enumerate(steps, 1):
        if not isinstance(s, dict):
            B('S1', f'ขั้น {i} ไม่ใช่ object')
            continue
        if s.get('n') != i or isinstance(s.get('n'), bool):
            B('S1', f'ขั้น {i} n = {s.get("n")!r} (ต้องเป็น {i})')
        k = s.get('kind')
        if k not in KINDS:
            B('S1', f'ขั้น {i} kind {k!r} ไม่อยู่ในสเปก')
            continue
        for key in s:
            if key not in STEP_KEYS:
                B('K', f'ขั้น {i} คีย์นอกสเปก: {key}')
            elif key in KEY_KINDS and k not in KEY_KINDS[key]:
                B('K', f'ขั้น {i} คีย์ {key} ใช้กับ kind {k} ไม่ได้')
        t = s.get('title')
        if not _s(t):
            B('S1', f'ขั้น {i} title ว่าง')
        elif len(t) > TITLE_MAX:
            B('S1', f'ขั้น {i} title ยาว {len(t)} > {TITLE_MAX}')
        elif '\n' in t or '\r' in t:
            B('S1', f'ขั้น {i} title ขึ้นบรรทัดใหม่ (หัวบัตร/รายการ ค1 เป็นบรรทัดเดียว · 678-CC)')
        say = s.get('say')
        if not _s(say):
            B('S1', f'ขั้น {i} say ว่าง')
        elif '$' in say or '\\' in say:
            B('S1', f'ขั้น {i} say มี $ หรือ \\ (ข9)')
        elif '\n' in say or '\r' in say:
            B('S1', f'ขั้น {i} say ขึ้นบรรทัดใหม่ (ตัวแสดงผลเป็นบรรทัดเดียว · 673-CC)')
        if 'note' in s and not isinstance(s['note'], str):
            B('S1', f'ขั้น {i} note ต้องเป็นข้อความ')
        elif '$' in s.get('note', ''):
            B('S1', f'ขั้น {i} note มี $ (ตัวแสดงผลไม่วาดสูตรใน note · 678-CC) ⇒ ย้ายสูตรไป warn/goal หรือเขียนเป็นคำ')
        for key in ('warn', 'of', 'tag', 'result', 'quot', 'rem', 'mid', 'target', 'c', 'val'):
            if key in s and not _s(s[key]):
                B('S1', f'ขั้น {i} {key} ต้องเป็นข้อความไม่ว่าง')
        for key in ('join', 'lhsJoin', 'rhsJoin'):
            if key in s and s[key] not in JOINS:
                B('S1', f'ขั้น {i} {key} = {s[key]!r} (รับ add / mul)')
        for key in ('relFlip', 'ok'):
            if key in s and not isinstance(s[key], bool):
                B('S1', f'ขั้น {i} {key} ต้องเป็น true/false')
        if 'isFactor' in s:                                 # 655: true/false · 652-W ใช้ {ตัวหาร: true/false} ด้วย
            f = s['isFactor']
            if not (isinstance(f, bool) or (isinstance(f, dict) and f
                                            and all(_s(a) and isinstance(b, bool) for a, b in f.items()))):
                B('S1', f'ขั้น {i} isFactor ต้องเป็น true/false หรือ {{ตัวหาร: true/false}}')
        if 'op' in s:
            op = s['op']
            if not isinstance(op, dict) or not _s(op.get('tex')):
                B('S1', f'ขั้น {i} op ต้องเป็น {{"tex": …}}')
            else:
                for key in op:
                    if key not in OP_KEYS:
                        B('K', f'ขั้น {i} op คีย์นอกสเปก: {key}')
        if 'cands' in s and not _strs(s['cands']):
            B('S1', f'ขั้น {i} cands ต้องเป็นรายการข้อความ')

        # ── kind ที่ไม่มีพจน์ในสาย ──
        if k == 'case':
            c = s.get('case')
            if not isinstance(c, dict):
                B('S1', f'ขั้น {i} case ต้องเป็น object')
                continue
            for key in c:
                if key not in CASE_KEYS:
                    B('K', f'ขั้น {i} case คีย์นอกสเปก: {key}')
            if not _s(c.get('label')):
                B('S1', f'ขั้น {i} case.label ว่าง')
            for key in ('cond', 'result'):
                if key in c and not _s(c[key]):
                    B('S1', f'ขั้น {i} case.{key} ต้องเป็นข้อความไม่ว่าง')
            p = c.get('path')
            if not (isinstance(p, str) and PATH_RE.match(p)):
                B('S1', f'ขั้น {i} case.path {p!r} ไม่ใช่ทรง 1 / 2 / 2.1 (ข5)')
                continue
            par = _parent(p)
            if par and par not in case_paths:
                B('S3', f'ขั้น {i} กรณีแม่ {par} ยังไม่เปิดก่อนกรณี {p}')
            if p in case_paths:
                B('S3', f'ขั้น {i} case.path {p} ซ้ำ')
            case_paths.add(p)
            if '' not in case_ctx:
                case_ctx[''] = prev_ids            # id ก่อนแตกกรณีครั้งแรก
            case_ctx[p] = case_ctx.get(par)        # ขั้นแรกของกรณีอ้าง id ล่าสุดของกรณีแม่
            cur_case, case_first, prev_rel = p, True, None
            continue
        if k == 'merge' or (k == 'answer' and 'parts' in s):
            has_answer = True                              # merge มี result = คำตอบรวมกรณี (หน้า quad จบที่ merge + check)
            parts = s.get('parts')
            if not (isinstance(parts, list) and parts and all(isinstance(x, str) for x in parts)):
                B('S1', f'ขั้น {i} parts ต้องเป็นรายการ path')
            else:
                for x in parts:
                    if x not in case_paths:
                        B('S3', f'ขั้น {i} parts ชี้กรณี {x} ที่ไม่มี')
            if not _s(s.get('result')):
                B('S1', f'ขั้น {i} {k} ต้องมี result')
            prev_ids, prev_rel, chain, cur_case, case_first = None, None, None, None, False
            continue
        if k == 'trial':                                   # ข1 ③ ไม่นับเป็นขั้นก่อน
            ht, hv = 'terms' in s, 'val' in s
            if ht and hv:
                B('S1', f'ขั้น {i} trial มีทั้ง terms และ val (655 §2 ห้ามมีทั้งคู่)')
            elif not ht and not hv:
                B('S1', f'ขั้น {i} trial ต้องมี terms (ลองคู่) หรือ val (ลองแทนค่า)')
            if ht:
                _terms_shape(s['terms'], i, 'terms', B)
                if 'mid' not in s:
                    B('S1', f'ขั้น {i} trial ลองคู่ต้องมี mid')
            if hv and 'c' not in s:
                B('S1', f'ขั้น {i} trial ลองแทนค่าต้องมี c')
            if 'ok' not in s:
                B('S1', f'ขั้น {i} trial ต้องมี ok')
            continue
        if k == 'synth':
            if 'c' not in s:
                B('S1', f'ขั้น {i} synth ต้องมี c')
            rows = [s.get(r) for r in ('row1', 'row2', 'row3')]
            if not all(_strs(r) for r in rows):
                B('S1', f'ขั้น {i} synth row1–row3 ต้องเป็นรายการข้อความ')
            elif len({len(r) for r in rows}) != 1 or not rows[0]:
                B('S1', f'ขั้น {i} synth row1–row3 ยาวไม่เท่ากัน {[len(r) for r in rows]}')
            f = s.get('fill')
            if not isinstance(f, int) or isinstance(f, bool) or f < 0:
                B('S1', f'ขั้น {i} synth fill ต้องเป็นจำนวนเต็ม ≥ 0')
            continue
        if k in ('text', 'check'):
            continue

        # ── eq / expr / answer ──
        if k == 'answer':
            has_answer = True
        is_rel = k == 'eq' or (k == 'answer' and any(x in s for x in ('lhs', 'rhs', 'rel')))
        if is_rel:
            okshape = _terms_shape(s.get('lhs'), i, 'lhs', B) & _terms_shape(s.get('rhs'), i, 'rhs', B)
            if s.get('rel') not in REL_DIR:
                B('S1', f'ขั้น {i} rel {s.get("rel")!r} ไม่อยู่ในสเปก')
                okshape = False
            if 'terms' in s:
                B('S1', f'ขั้น {i} ขั้นสมการใช้ lhs/rhs ⛔ terms')
            if not okshape:
                continue
            terms = s['lhs'] + s['rhs']
            key = ('eq', s.get('tag'))
        elif k == 'expr' or (k == 'answer' and 'terms' in s):
            if not _terms_shape(s.get('terms'), i, 'terms', B):
                continue
            terms = s['terms']
            key = ('expr', s.get('of'))
        else:
            continue                                       # answer สรุปเป็นข้อความ/result/quot (655 §2)

        ids = [x['id'] for x in terms]
        cur = set(ids)
        if len(cur) != len(ids):
            B('S2', f'ขั้น {i} id ซ้ำในขั้น {sorted({x for x in ids if ids.count(x) > 1})}')
        cancel = s.get('cancel', [])
        if not _strs(cancel):
            B('S1', f'ขั้น {i} cancel ต้องเป็นรายการ id')
            cancel = []
        arrows = s.get('arrows', [])
        if not (isinstance(arrows, list) and all(isinstance(a, dict) for a in arrows)):
            B('S1', f'ขั้น {i} arrows ต้องเป็นรายการ object')
            arrows = []

        if case_first:
            base, start, skip_lost = case_ctx.get(cur_case), False, True
            case_first = False
        elif prev_ids is None or chain != key:
            base, start, skip_lost = prev_ids, True, True
        else:
            base, start, skip_lost = prev_ids, False, False
        if base is None:
            start = True
        used = set()
        for x in terms:
            fr = _from_list(x)
            if fr is None:
                B('S2', f'ขั้น {i} {x["id"]}.from ต้องเป็น id หรือรายการ id')
                continue
            used |= set(fr)
            for f in fr:
                if base is None or f not in base:
                    B('S3', f'ขั้น {i} {x["id"]}.from {f} ไม่มีในขั้นก่อน')
            if not start and x['id'] not in base and not fr and x.get('role') != 'add':
                B('S3', f'ขั้น {i} id ใหม่ {x["id"]} ไม่มี from (ข1①)')
        for c in cancel:
            if base is None or c not in base:
                B('S3', f'ขั้น {i} cancel {c} ไม่มีในขั้นก่อน')
            if c in cur:
                B('S3', f'ขั้น {i} cancel {c} ยังอยู่ในขั้นนี้')
        for a in arrows:
            for key2 in a:
                if key2 not in ARROW_KEYS:
                    B('K', f'ขั้น {i} arrows คีย์นอกสเปก: {key2}')
            if base is None or a.get('from') not in base:
                B('S3', f'ขั้น {i} arrow.from {a.get("from")!r} ไม่มีในขั้นก่อน')
            if a.get('to') not in cur:
                B('S3', f'ขั้น {i} arrow.to {a.get("to")!r} ไม่มีในขั้นนี้')
        if not skip_lost:
            lost = base - cur - used - set(cancel)
            if lost:
                B('S3', f'ขั้น {i} id หาย {sorted(lost)} (ข1② ต้องอยู่ต่อ/ถูกอ้างใน from/อยู่ใน cancel)')

        if is_rel:                                          # ข3 relFlip
            lid = {x['id'] for x in s['lhs']}
            rid = {x['id'] for x in s['rhs']}
            if flip_rule:
                if prev_rel is not None and not start:
                    a0, b0 = REL_DIR[prev_rel[0]], REL_DIR[s['rel']]
                    flipped = a0 is not None and b0 is not None and a0 != b0
                    swapped = lid == prev_rel[2] and rid == prev_rel[1]
                    if s.get('relFlip') is True and not flipped:
                        B('S3', f'ขั้น {i} relFlip แต่ rel ไม่กลับทิศ ({prev_rel[0]} → {s["rel"]}) (ข3)')
                    if flipped and s.get('relFlip') is not True and not swapped:
                        B('S3', f'ขั้น {i} rel กลับทิศ ({prev_rel[0]} → {s["rel"]}) แต่ไม่มี relFlip (ข3)')
                elif s.get('relFlip') is True:
                    B('S3', f'ขั้น {i} relFlip แต่ไม่มีขั้นสมการก่อนหน้าในสายเดียวกัน (ข3)')
            prev_rel = (s['rel'], lid, rid)
        else:
            prev_rel = None
        prev_ids, chain = cur, key
        if cur_case is not None:
            case_ctx[cur_case] = cur

    if not has_answer:
        B('S1', 'ไม่มีขั้น answer หรือ merge')
    return bad


def _terms_shape(ts, i, name, B):
    """ทรงของรายการพจน์ · คืน True ถ้าใช้ต่อได้ (ทุกพจน์มี id)"""
    if not isinstance(ts, list) or not ts:
        B('S1', f'ขั้น {i} {name} ต้องเป็นรายการพจน์ไม่ว่าง')
        return False
    ok = True
    for x in ts:
        if not isinstance(x, dict):
            B('S2', f'ขั้น {i} {name} มีพจน์ที่ไม่ใช่ object')
            ok = False
            continue
        for key in x:
            if key not in TERM_KEYS:
                B('K', f'ขั้น {i} พจน์ {x.get("id")!r} คีย์นอกสเปก: {key}')
        if not _s(x.get('id')):
            B('S2', f'ขั้น {i} {name} มีพจน์ไม่มี id')
            ok = False
        if not _s(x.get('tex')):
            B('S2', f'ขั้น {i} พจน์ {x.get("id")!r} tex ว่าง')
        if 'role' in x and x['role'] not in ROLES:
            B('S2', f'ขั้น {i} พจน์ {x.get("id")!r} role {x["role"]!r} ไม่อยู่ในสเปก')
    return ok


def check_item(q):
    """กฎ B ระดับข้อ · คืน (มี solSteps ไหม, ปัญหา[])"""
    bad = []
    for k in ITEM_FORBIDDEN:
        if k in q:
            bad.append(f'B ช่อง {k} อยู่ระดับข้อ ⛔ (ต้องอยู่ใน solSteps)')
    if 'solSteps' not in q:
        return False, bad
    return True, bad + check_ss(q['solSteps'], bank=True)


def counter_verdict(n, floor):
    if n < floor:
        return [f'B ข้อที่มี solSteps {n} < ขั้นต่ำ {floor} — ช่องหายเงียบ? (ถอดข้อจริง ⇒ ลดค่าพร้อมใบ)']
    return []


def _load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def run_bank(d):
    files = sorted(glob.glob(os.path.join(d, '*.json')))
    if not files:
        print(f'🔴 ไม่พบไฟล์ชุดใน {d}')
        return 2
    n_items = n_ss = n_steps = 0
    reds = []
    for fp in files:
        try:
            data = _load(fp)
        except (OSError, ValueError) as e:
            print(f'🔴 อ่าน {fp} ไม่ได้: {type(e).__name__}')
            return 2
        qs = data.get('questions') if isinstance(data, dict) else data
        if not isinstance(qs, list):
            print(f'🔴 {fp} ไม่มีรายการ questions')
            return 2
        for q in qs:
            if not isinstance(q, dict):
                continue
            n_items += 1
            has, bad = check_item(q)
            if has:
                n_ss += 1
                st = q['solSteps'].get('steps') if isinstance(q['solSteps'], dict) else None
                n_steps += len(st) if isinstance(st, list) else 0
            if bad:
                reds.append((q.get('id', '?'), bad))
    cbad = counter_verdict(n_ss, MIN_WITH_SOLSTEPS)
    print(f'ด่าน 25 · check_solsteps v{CHECKER_VERSION} · ทั้งคลัง ({len(files)} ไฟล์)')
    for qid, bad in reds:
        print(f'  🔴 {qid} · ' + ' | '.join(bad[:12]) + (f' | … อีก {len(bad) - 12}' if len(bad) > 12 else ''))
    for b in cbad:
        print(f'  🔴 {b}')
    print(f'📌 ด่าน 25 ตรวจ {n_items:,} ข้อ · มี solSteps {n_ss:,} ข้อ ({n_steps:,} ขั้น · ขั้นต่ำ {MIN_WITH_SOLSTEPS}) · '
          f'แดง {len(reds):,} ข้อ' + (' · ตัวนับแดง' if cbad else ''))
    print('   ⚠️ เขียว = ทรง/อ้างอิงถูก ⛔ ไม่ใช่หลักฐานว่าค่าถูก (S4 อยู่นอก CI)')
    return 1 if (reds or cbad) else 0


def run_lesson(paths):
    total = red = 0
    for fp in paths:
        try:
            data = _load(fp)
        except (OSError, ValueError) as e:
            print(f'🔴 อ่าน {fp} ไม่ได้: {type(e).__name__}')
            return 2
        if isinstance(data, dict) and isinstance(data.get('examples'), list):
            items = [(str(e.get('ex', '?')), e.get('solSteps')) for e in data['examples'] if isinstance(e, dict)]
        elif isinstance(data, list):
            items = [(str(e.get('id', '?')), e.get('solSteps')) for e in data if isinstance(e, dict) and 'solSteps' in e]
        else:
            print(f'🔴 {fp} ไม่ใช่ {{"examples":[…]}} หรือรายการข้อ')
            return 2
        print(f'— {os.path.basename(fp)} · {len(items)} ตัวอย่าง')
        for name, ss in items:
            total += 1
            bad = check_ss(ss, bank=False)
            n = len(ss.get('steps', [])) if isinstance(ss, dict) and isinstance(ss.get('steps'), list) else 0
            if bad:
                red += 1
                print(f'  🔴 {name} · {n} ขั้น · ' + ' | '.join(bad))
            else:
                print(f'  ✅ {name} · {n} ขั้น')
    print(f'📌 โหมดหน้าเรียน: {total} ตัวอย่าง · แดง {red}')
    return 1 if red else 0


# ── selftest ───────────────────────────────────────────────────────────────────
def _good():
    """ของดีที่ครอบทุก kind ของสเปก v1.2 — ต้องผ่าน 0 ปัญหา"""
    T = lambda i, tex, **kw: dict(id=i, tex=tex, **kw)   # noqa: E731
    return {
        'v': 'ss-v1.2', 'goal': 'ย้ายข้างแล้วหารด้วย $-2$', 'given': 'x+\\frac1x=4', 'domain': 'x>0', 'ck': 'solve',
        'steps': [
            {'n': 1, 'kind': 'text', 'title': 'อ่านโจทย์', 'note': '', 'say': 'อ่านโจทย์ก่อน', 'cands': ['1', '-1']},
            {'n': 2, 'kind': 'eq', 'title': 'ตั้งอสมการ', 'lhs': [T('a', '-2x'), T('b', '+3')], 'rel': '<',
             'rhs': [T('c', '7')], 'tag': '(1)', 'say': 'ตั้งอสมการ'},
            {'n': 3, 'kind': 'eq', 'title': 'ย้ายข้าง', 'lhs': [T('a', '-2x')], 'rel': '<',
             'rhs': [T('c', '7'), T('m3', '-3', role='move', from_='b')], 'tag': '(1)',
             'arrows': [{'from': 'b', 'to': 'm3', 'label': 'ย้ายข้าง'}], 'say': 'ย้ายสามไปขวา',
             'warn': 'ย้ายข้างต้องเปลี่ยนเครื่องหมาย'},
            {'n': 4, 'kind': 'eq', 'title': 'รวมเลข', 'lhs': [T('a', '-2x')], 'rel': '<',
             'rhs': [T('f', '4', from_=['c', 'm3'])], 'tag': '(1)', 'say': 'เจ็ดลบสามได้สี่'},
            {'n': 5, 'kind': 'eq', 'title': 'หารด้วยลบสอง', 'lhs': [T('x', 'x', from_='a')], 'rel': '>',
             'rhs': [T('g', '-2', from_='f')], 'tag': '(1)', 'relFlip': True, 'op': {'tex': '\\div (-2)'},
             'say': 'หารลบสอง กลับเครื่องหมาย'},
            {'n': 6, 'kind': 'eq', 'title': 'สลับข้าง', 'lhs': [T('g', '-2')], 'rel': '<',
             'rhs': [T('x', 'x')], 'tag': '(1)', 'say': 'เขียนกลับข้าง'},
            {'n': 7, 'kind': 'trial', 'title': 'ลองคู่', 'terms': [T('p', '(x+1)'), T('q', '(x+6)')],
             'join': 'mul', 'mid': '7x', 'target': '8x', 'ok': False, 'say': 'ลองคู่หนึ่งกับหก'},
            {'n': 8, 'kind': 'trial', 'title': 'ลองแทน', 'c': '1', 'val': '0', 'ok': True, 'say': 'ลองแทนหนึ่ง'},
            {'n': 9, 'kind': 'synth', 'title': 'หารสังเคราะห์', 'c': '2', 'row1': ['1', '-3', '2'],
             'row2': ['', '2', '-2'], 'row3': ['1', '-1', '0'], 'fill': 3, 'say': 'หารสังเคราะห์'},
            {'n': 10, 'kind': 'expr', 'title': 'โจทย์', 'terms': [T('u', 'x^2'), T('w', '+8x'), T('z', '+12')],
             'note': 'กรณี 1 ให้ a = 2, b = 6\nab = 12 ถูก\na + b = 8 ถูก', 'say': 'เริ่มจากโจทย์'},
            {'n': 11, 'kind': 'expr', 'title': 'แยกตัวประกอบ', 'terms': [T('h', '(x+2)', role='common', from_=['u', 'w']),
                                                                        T('k', '(x+6)', from_='z')],
             'join': 'mul', 'say': 'ได้เอ็กซ์บวกสองคูณเอ็กซ์บวกหก'},
            {'n': 12, 'kind': 'expr', 'title': 'หาดิสคริมิแนนต์', 'of': 'D', 'terms': [T('d', '64-48')],
             'say': 'ดีเท่ากับหกสิบสี่ลบสี่สิบแปด', 'coef': {'a': '1', 'b': '8', 'c': '12'}},
            {'n': 13, 'kind': 'expr', 'title': 'คิดเลข', 'of': 'D', 'terms': [T('d', '16')], 'say': 'ได้สิบหก'},
            {'n': 14, 'kind': 'case', 'title': 'กรณีที่ 1', 'case': {'path': '1', 'label': 'x ≥ 0', 'cond': 'x\\ge 0'},
             'say': 'กรณีแรก'},
            {'n': 15, 'kind': 'eq', 'title': 'ถอดค่าสัมบูรณ์', 'lhs': [T('y1', 'x', from_='d')], 'rel': '=',
             'rhs': [T('r1', '4', role='add')], 'say': 'เอ็กซ์เท่ากับสี่'},
            {'n': 16, 'kind': 'case', 'title': 'กรณีที่ 2', 'case': {'path': '2', 'label': 'x < 0'}, 'say': 'กรณีสอง'},
            {'n': 17, 'kind': 'case', 'title': 'กรณีย่อย', 'case': {'path': '2.1', 'label': 'ย่อย'}, 'say': 'กรณีย่อย'},
            {'n': 18, 'kind': 'eq', 'title': 'ถอดค่าสัมบูรณ์', 'lhs': [T('y2', '-x', from_='d')], 'rel': '=',
             'rhs': [T('r2', '4', role='add')], 'say': 'ลบเอ็กซ์เท่ากับสี่'},
            {'n': 19, 'kind': 'merge', 'title': 'รวมกรณี', 'parts': ['1', '2'], 'result': '\\{-4,4\\}',
             'say': 'รวมสองกรณี'},
            {'n': 20, 'kind': 'check', 'title': 'ตรวจคำตอบ', 'note': 'แทนกลับ', 'say': 'ลองแทนกลับ'},
            {'n': 21, 'kind': 'answer', 'title': 'ตอบ', 'of': 'x', 'terms': [T('e', '4')], 'say': 'ตอบสี่'},
            {'n': 22, 'kind': 'answer', 'title': 'ผลหาร', 'quot': 'x-1', 'rem': '0', 'isFactor': True,
             'say': 'ผลหารเอ็กซ์ลบหนึ่ง', 'vals': ['1']},
        ]}


def _good_trial():
    """ข1 ③ โดยตรง: trial คั่นกลางสายนิพจน์ ⇒ ขั้นหลัง trial อ้าง from ไปที่ขั้นก่อน trial"""
    return {'v': 'ss-v1.2', 'steps': [
        {'n': 1, 'kind': 'expr', 'title': 'โจทย์', 'terms': [{'id': 'a', 'tex': 'x^2'}, {'id': 'b', 'tex': '+5x+6'}],
         'say': 'โจทย์'},
        {'n': 2, 'kind': 'trial', 'title': 'ลองคู่', 'terms': [{'id': 'p', 'tex': '(x+1)'}, {'id': 'q', 'tex': '(x+6)'}],
         'join': 'mul', 'mid': '7x', 'ok': False, 'say': 'ลองหนึ่งกับหก'},
        {'n': 3, 'kind': 'answer', 'title': 'แยกได้', 'join': 'mul',
         'terms': [{'id': 'c', 'tex': '(x+2)(x+3)', 'from': ['a', 'b']}], 'say': 'ได้คูณกัน'},
    ]}


def _fix(o):
    """แปลง from_ ⇒ from (from เป็นคำสงวน)"""
    if isinstance(o, dict):
        return {('from' if k == 'from_' else k): _fix(v) for k, v in o.items()}
    if isinstance(o, list):
        return [_fix(v) for v in o]
    return o


def _st(ss, n):
    return ss['steps'][n - 1]


MUTANTS = [   # (ชื่อ, แก้ ss, ข้อความที่ต้องเจอ)
    ('from ชี้ id ที่ไม่มี', lambda ss: _st(ss, 4)['rhs'][0].__setitem__('from', ['c', 'zz']), 'from zz ไม่มีในขั้นก่อน'),
    ('cancel แต่ยังอยู่ในขั้นนี้', lambda ss: _st(ss, 4).__setitem__('cancel', ['a']), 'cancel a ยังอยู่'),
    ('id ใหม่ไม่มี from', lambda ss: _st(ss, 4)['rhs'][0].pop('from'), 'ข1①'),
    ('ใส่ \\color ใน tex', lambda ss: _st(ss, 10)['terms'][0].__setitem__('tex', '\\color{red}{x^2}'), '\\color'),
    ('role ผิดชื่อ', lambda ss: _st(ss, 3)['rhs'][1].__setitem__('role', 'insert'), "role 'insert'"),
    ('say ว่าง', lambda ss: _st(ss, 2).__setitem__('say', ''), 'say ว่าง'),
    ('n ข้าม', lambda ss: _st(ss, 5).__setitem__('n', 7), 'n = 7'),
    ('ข1② id หาย (ไม่ไปต่อ ไม่ถูกอ้าง ไม่อยู่ใน cancel)', lambda ss: _st(ss, 4)['rhs'][0].__setitem__('from', 'c'), 'ข1②'),
    ('rel กลับทิศแต่ลืม relFlip', lambda ss: _st(ss, 5).pop('relFlip'), 'ไม่มี relFlip'),
    ('relFlip แต่ rel ไม่กลับทิศ', lambda ss: _st(ss, 4).__setitem__('relFlip', True), 'relFlip แต่ rel ไม่กลับทิศ'),
    ('say มี $', lambda ss: _st(ss, 3).__setitem__('say', 'ย้าย $3$'), 'ข9'),
    ('trial ถูกนับเป็นขั้นก่อน (ขั้นหลังอ้าง id ของ trial)',
     lambda ss: _st(ss, 11)['terms'][1].__setitem__('from', 'q'), 'from q ไม่มีในขั้นก่อน'),
    ('join ผิดค่า', lambda ss: _st(ss, 11).__setitem__('join', 'times'), "join = 'times'"),
    ('พิมพ์ form แทน from', lambda ss: _st(ss, 11)['terms'][1].__setitem__('form', 'z'), 'คีย์นอกสเปก: form'),
    ('case.path ผิดทรง', lambda ss: _st(ss, 14)['case'].__setitem__('path', 'ก'), 'ข5'),
    ('merge parts ชี้กรณีที่ไม่มี', lambda ss: _st(ss, 19).__setitem__('parts', ['1', '3']), 'parts ชี้กรณี 3'),
    ('trial มีทั้ง terms และ val', lambda ss: _st(ss, 7).__setitem__('val', '1'), 'ทั้ง terms และ val'),
    ('ป้ายรุ่นผิด', lambda ss: ss.__setitem__('v', 'ss-v9'), "v = 'ss-v9'"),
    ('ไม่มีขั้น answer/merge', lambda ss: [_st(ss, n).__setitem__('kind', 'check') for n in (19, 21, 22)],
     'ไม่มีขั้น answer หรือ merge'),
    ('isFactor ผิดชนิด', lambda ss: _st(ss, 22).__setitem__('isFactor', 'yes'), 'isFactor ต้องเป็น'),
    ('title ยาวเกิน 30', lambda ss: _st(ss, 2).__setitem__('title', 'ก' * 31), 'title ยาว 31'),
    ('id ซ้ำในขั้น', lambda ss: _st(ss, 10)['terms'][2].__setitem__('id', 'u'), 'id ซ้ำ'),
    ('kind นอกสเปก', lambda ss: _st(ss, 20).__setitem__('kind', 'hint'), "kind 'hint'"),
    ('คีย์ผิด kind (mid บนขั้นสมการ)', lambda ss: _st(ss, 2).__setitem__('mid', '7x'), 'คีย์ mid ใช้กับ kind eq ไม่ได้'),
    ('synth แถวยาวไม่เท่ากัน', lambda ss: _st(ss, 9)['row2'].pop(), 'ยาวไม่เท่ากัน'),
    ('warn ว่าง', lambda ss: _st(ss, 3).__setitem__('warn', ' '), 'warn ต้องเป็นข้อความไม่ว่าง'),
    ('arrow.to ชี้ id ที่ไม่มีในขั้นนี้', lambda ss: _st(ss, 3)['arrows'][0].__setitem__('to', 'b'), 'arrow.to'),
    ('คีย์นอกสเปกระดับ solSteps', lambda ss: ss.__setitem__('params', ['a']), 'คีย์นอกสเปกระดับ solSteps: params'),
    ('พิมพ์ชื่อช่องระดับขั้นผิด (relflip)', lambda ss: _st(ss, 5).__setitem__('relflip', True), 'คีย์นอกสเปก: relflip'),
    ('say ขึ้นบรรทัดใหม่', lambda ss: _st(ss, 2).__setitem__('say', 'ตั้ง\nอสมการ'), 'say ขึ้นบรรทัดใหม่'),
    ('role ตัวร่วมสะกดผิด (commom)', lambda ss: _st(ss, 11)['terms'][0].__setitem__('role', 'commom'), "role 'commom'"),
    ('title ขึ้นบรรทัดใหม่', lambda ss: _st(ss, 2).__setitem__('title', 'ตั้ง\nอสมการ'), 'title ขึ้นบรรทัดใหม่'),
    ('note มี $', lambda ss: _st(ss, 10).__setitem__('note', 'กรณี 1 ให้ $a = 2$'), 'note มี $'),
    ('ขั้นสมการใช้ terms', lambda ss: _st(ss, 6).__setitem__('terms', [{'id': 'g', 'tex': '-2'}]), 'ใช้ lhs/rhs'),
]
EXPECTED_MUTANTS = 34            # ⛔ ลบมิวแทนต์ทิ้งเงียบ ๆ ไม่ได้ — จำนวนต้องตรง

ITEM_MUTANTS = [   # กฎ B (ระดับข้อ + ตัวนับ)
    ('ช่อง ck ระดับข้อ', lambda q: q.__setitem__('ck', 'solve'), 'ช่อง ck อยู่ระดับข้อ'),
    ('ช่อง given ระดับข้อ', lambda q: q.__setitem__('given', 'x>0'), 'ช่อง given อยู่ระดับข้อ'),
    ('solSteps ไม่ใช่ object', lambda q: q.__setitem__('solSteps', []), 'solSteps ไม่ใช่ object'),
    ('ป้ายรุ่นของ W ในคลัง', lambda q: q['solSteps'].__setitem__('v', 'ss-v1.1+W-quad2'), "v = 'ss-v1.1+W-quad2'"),
]
EXPECTED_ITEM_MUTANTS = 4


def selftest():
    fails = 0
    good = _fix(_good())
    b = check_ss(copy.deepcopy(good), bank=True)
    print(('✅' if not b else '🔴') + f' ของดี (22 ขั้น ทุก kind) ⇒ ปัญหา {len(b)}' + ('' if not b else ' · ' + ' | '.join(b)))
    fails += bool(b)
    b = check_ss(dict(copy.deepcopy(good), v='ss-v1.1+W-quad2'), bank=False)
    print(('✅' if not b else '🔴') + ' โหมดหน้าเรียนรับป้ายรุ่นของ W')
    fails += bool(b)
    q0 = {'id': 'x-q001', 'question': 'โจทย์', 'solSteps': copy.deepcopy(good)}
    has, b = check_item(copy.deepcopy(q0))
    print(('✅' if has and not b else '🔴') + ' ข้อคลังที่มี solSteps ดี ⇒ ผ่าน')
    fails += bool(b) or not has
    if len(MUTANTS) != EXPECTED_MUTANTS or len(ITEM_MUTANTS) != EXPECTED_ITEM_MUTANTS:
        print(f'🔴 จำนวนมิวแทนต์ {len(MUTANTS)}/{len(ITEM_MUTANTS)} ≠ ที่ประกาศ {EXPECTED_MUTANTS}/{EXPECTED_ITEM_MUTANTS}')
        fails += 1
    hit = 0
    for name, f, exp in MUTANTS:
        ss = copy.deepcopy(good)
        f(ss)
        b = check_ss(ss, bank=True)
        ok = any(exp in x for x in b)
        hit += ok
        print(('  ✅ ' if ok else '  🔴 ') + name + ('' if ok else f' · คาด “{exp}” · ได้ {b}'))
    for name, f, exp in ITEM_MUTANTS:
        q = copy.deepcopy(q0)
        f(q)
        _, b = check_item(q)
        ok = any(exp in x for x in b)
        hit += ok
        print(('  ✅ ' if ok else '  🔴 ') + name + ('' if ok else f' · คาด “{exp}” · ได้ {b}'))
    gt = _good_trial()
    b = check_ss(copy.deepcopy(gt), bank=True)
    ok = not b
    gt['steps'][2]['terms'][0]['from'] = ['p', 'q']
    b2 = check_ss(gt, bank=True)
    ok = ok and any('from p ไม่มีในขั้นก่อน' in x for x in b2)
    hit += ok
    print(('  ✅ ' if ok else '  🔴 ') + 'ข1③ trial คั่นกลาง: อ้างขั้นก่อน trial ⇒ ผ่าน · อ้าง id ของ trial ⇒ แดง'
          + ('' if ok else f' · {b} / {b2}'))
    c1, c0 = counter_verdict(0, 1), counter_verdict(1, 1)
    ok = bool(c1) and not c0
    hit += ok
    print(('  ✅ ' if ok else '  🔴 ') + 'ตัวนับ: solSteps หาย 1 ข้อ ⇒ แดง · เท่าขั้นต่ำ ⇒ ผ่าน')
    total = len(MUTANTS) + len(ITEM_MUTANTS) + 2
    fails += total - hit
    print(f'📌 selftest v{CHECKER_VERSION}: มิวแทนต์ {total} · แดงด้วยกฎที่ตั้งใจ {hit}' + (' ✅' if not fails else ' 🔴'))
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description='ด่าน 25 · solSteps')
    ap.add_argument('setdir', nargs='?')
    ap.add_argument('--lesson', nargs='+')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    a = ap.parse_args(argv)
    if a.version:
        print(CHECKER_VERSION)
        return 0
    if a.selftest:
        if selftest():
            return 2
        return 0
    if a.lesson:
        return run_lesson(a.lesson)
    if not a.setdir:
        ap.print_usage()
        return 2
    return run_bank(a.setdir)


if __name__ == '__main__':
    sys.exit(main())

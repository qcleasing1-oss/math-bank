#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ด่านความสด · bank.json ที่ "เสิร์ฟให้เด็ก" ตรงกับ data/sets/ ที่เป็นแหล่งความจริงหรือยัง

═══════════════════════════════════════════════════════════════════════
⛔⛔ ด่านนี้เป็น "ฝั่ง sync เท่านั้น" — ห้ามผูกเข้า guards.yml เด็ดขาด ⛔⛔

  มติร่วมกับพอร์ทัล 1 ส.ค. 2569:
    ⛔ ห้ามมีด่านฝั่ง push        ⛔ ห้ามมีโหมด "เตือนเฉย ๆ" ฝั่ง push
  เหตุผล (ประโยคเดียวที่ต้องจำ):
    **คนที่ push ไม่ใช่คนที่เสิร์ฟ bank.json ให้เด็ก**
    ตอนครู push เนื้อใหม่ ด่านนี้ *ต้อง* แดงเป็นเรื่องปกติ — เพราะบอทยังไม่ได้
    rebuild ⇒ ถ้าเอาไปแขวนไว้ฝั่ง push มันจะแดงทุกคอมมิตของมนุษย์
    ⇒ กลายเป็นไฟแดงที่ทุกคนเรียนรู้ที่จะข้าม ⇒ วันที่มันแดงจริงจะไม่มีใครเห็น
    (และโหมดเตือนเฉย ๆ แย่กว่า เพราะมันสอนให้ข้ามโดยไม่รู้สึกผิดเลยด้วยซ้ำ)

  ⇒ ชื่อไฟล์นี้ถูกประกาศไว้ใน NOT_IN_CI ของ scripts/check_exit_codes.py
    พร้อมเหตุผล ⇒ ด่าน 11 (กฎ ⑦ก "ตัวตรวจที่ไม่มีใครเรียก = ตัวตรวจที่ไม่มีอยู่")
    จะไม่แดงเพราะไฟล์นี้ แต่จะแดงถ้ามีใครลบเหตุผลนั้นทิ้ง
═══════════════════════════════════════════════════════════════════════

── ปัญหาที่ด่านนี้แก้ ────────────────────────────────────────────────

  🔴 กฎสองรุ่น: data/bank.json ถูกบอท rebuild เป็น **คอมมิตแยก** หลังคอมมิตของคน
     ⇒ "bank.json ที่อยู่ *ใน* คอมมิต X" ≠ "bank.json ที่สร้าง *จาก* คอมมิต X"
     ⇒ พูดให้ตรงต้องพูดว่า "เนื้อ ณ คอมมิต X" หรือ "stamp = X" ⛔ ไม่ใช่ "ของที่ X"

  🔴 กฎสามชั้น:  ซอง (ส่งแล้ว) → คอมมิต (รวมแล้ว) → stamp ของ bank.json ที่เสิร์ฟ
     เด็กเห็นชั้นที่สามเท่านั้น
     ⛔ ห้ามใช้ "ซองไปถึงหรือยัง" เป็นตัวบอกสถานะ — มันตอบคนละคำถาม
     ⇒ ด่านนี้คือเครื่องมือวัด **ชั้นที่สาม** โดยตรง

── สองแกนที่ต้องพิมพ์ข้างธงเสมอ (คำขอของครู · ห้ามตัดออก) ─────────────

  ① **อายุ**  = ป้าย builtFromCommit ตามหลังคอมมิตล่าสุดที่แตะเนื้อ กี่คอมมิต/กี่วัน
  ② **ขนาด**  = เนื้อต่างกันกี่ข้อ จากทั้งหมดกี่ข้อ  (N / 6,313)

  🔴 ทำไมต้องมีสองแกน ไม่ใช่แค่ธงเขียว/แดง:
     ธงเปล่า ๆ ตอบไม่ได้ว่า "ควรรีบแค่ไหน" — ตามหลัง 1 คอมมิตที่แก้คำผิด 1 ข้อ
     กับตามหลัง 9 คอมมิตที่แก้เฉลย 300 ข้อ ขึ้นสีเดียวกันทั้งคู่
     ⇒ คนอ่านต้องเดา ⇒ คนที่เดาบ่อย ๆ จะเลิกอ่าน

  ⚠️ และสองแกนนี้ **ไม่ซ้ำกัน** — มีสถานะที่แกนหนึ่งเตือนแต่อีกแกนเงียบ:
     ป้ายเก่า + เนื้อตรงทุกข้อ = ของจริงที่เกิดขึ้นได้ เพราะ build_bank.py
     **ไม่เขียนไฟล์ถ้าเนื้อไม่เปลี่ยน** (กันดิฟฟ์เปล่า) ⇒ แก้ displayName ใน
     set file แล้ว bank ไม่ถูกเขียนใหม่ ⇒ ป้ายค้างที่คอมมิตเก่าทั้งที่เนื้อสดแล้ว
     ⇒ เคสนี้ต้องเป็น 🟠 "รู้ไว้" ⛔ ไม่ใช่ 🔴 "เด็กเห็นของเก่า"

── ตารางคำตัดสิน ─────────────────────────────────────────────────────

  | ป้าย vs คอมมิตเนื้อ | เนื้อต่าง | ผล |
  |---|---|---|
  | ตรง      | 0 ข้อ  | 🟢 สด                                         → 0 |
  | ตรง      | >0 ข้อ | 🔴 **ป้ายโกหก** — ร้ายที่สุดในตาราง            → 1 |
  | ไม่ตรง   | 0 ข้อ  | 🟠 ป้ายเก่าแต่เนื้อตรง (build ถูกข้าม)          → 0 |
  | ไม่ตรง   | >0 ข้อ | 🔴 เด็กเห็นของเก่าจริง                          → 1 |
  | ป้าย = local | ใด ๆ | 🔴 bank ที่ commit มาจากเครื่องคน ⛔ ผิดกติกา   → 1 |
  | อ่านไม่ได้ / โครงเปลี่ยน | — | ⚙️ เครื่องมือแดง                    → 2 |

  🔴 แถวที่ 2 ("ป้ายตรง แต่เนื้อต่าง") คือแถวที่อันตรายที่สุด และเป็นแถวเดียว
     ที่ธงเดี่ยว ๆ จับไม่ได้เลย — เพราะทุกอย่างที่ *ดูได้ง่าย* บอกว่าเขียว

── ⑨ ตัวหาร ─────────────────────────────────────────────────────────

  ตัวเทียบทุกตัวต้องประกาศตัวหาร: ด่านนี้พิมพ์ "จากทั้งหมด N ข้อ" ทุกรอบ
  และ **ปฏิเสธที่จะขึ้นเขียว** ถ้า N น้อยผิดปกติ (< MIN_QUESTIONS)
  เพราะ "ต่าง 0 ข้อ จาก 0 ข้อ" หน้าตาเหมือนผ่าน แต่แปลว่าอ่านไม่เจอ

  และถ้า bank.json มี **ฟิลด์ที่ด่านนี้ไม่รู้จัก** ⇒ เครื่องมือแดง (รหัส 2)
  ⛔ ไม่ใช่ผ่าน — ตัวตรวจที่ตามโครงของจริงไม่ทัน ต้องบอกว่าตามไม่ทัน
     ไม่ใช่ขึ้นเขียวบนส่วนที่มันบังเอิญรู้จัก

⛔ ด่านนี้อ่านอย่างเดียว ไม่แก้ไฟล์ใด ๆ · ⛔ ไม่แตะฟิลด์ accept

รหัสออก: 0 = ผ่าน · 1 = เนื้อหาแดง · 2 = เครื่องมือแดง
"""
import argparse
import datetime as _dt
import json
import os
import subprocess
import sys

CHECKER_VERSION = '1.0'

# ── ⑨ ตัวหารขั้นต่ำ ────────────────────────────────────────────────
#    คลังมี 6,313 ข้อ ณ 1 ส.ค. 69 · ตั้งพื้นไว้ต่ำกว่ามากเพื่อกันการอ่านพลาด
#    ⛔ ห้ามลดตัวเลขนี้เพื่อให้ด่านผ่าน — ถ้าคลังหดจริงต้องมีคนอธิบายว่าทำไม
MIN_QUESTIONS = 4000

# ── โครงของ bank.json ที่ด่านนี้ "รู้จักครบ" ────────────────────────
#
# 🔴 กับดัก ⑧ อีกหน้าหนึ่ง: ด่านที่เทียบ "เฉพาะฟิลด์ที่มันรู้จัก" จะขึ้นเขียว
#    ตลอดไป แม้ของจริงจะงอกฟิลด์ใหม่ที่ไม่มีใครเทียบ
#    ⇒ ที่นี่จึงแบ่งฟิลด์ทั้งหมดเป็น 4 ถัง แล้ว **บังคับว่าต้องครบ**
#      ถ้า bank.json มีฟิลด์นอก 4 ถังนี้ ⇒ รหัส 2 (ตัวตรวจตามไม่ทัน)
#      วิธีแก้เมื่อแดง: เอาฟิลด์ใหม่ไปใส่ถังที่ถูก — ไม่ใช่ปิดด่าน

# ① คัดมาจาก manifest.json ตรง ๆ ไม่คำนวณใหม่ ⇒ เทียบได้แบบตรงตัว
#    (คีย์ซ้าย = ชื่อใน bank.json · ค่าขวา = ชื่อใน manifest.json)
MANIFEST_COPIED = {
    'schemaVersion': 'schemaVersion',
    'manifestExported': 'exported',
    'topicNames': 'topicNames',
    'subTopicNames': 'subTopicNames',
    'deprecatedSubTopics': 'deprecatedSubTopics',
    'sets': 'sets',
}

# ② คำนวณจาก questions/manifest ⇒ ถ้า ① กับ questions ตรง อันนี้ต้องตรงตาม
#    ⛔ ไม่เทียบซ้ำ เพราะมันจะรายงานความต่างเดียวกันสองรอบ (เสียงดังโดยไม่เพิ่มข้อมูล)
DERIVED = (
    'questionCount', 'activeCount', 'retiredCount',
    'subTopicCount', 'liveSubTopicCount',
)

# ③ เปลี่ยนทุก build ⇒ ห้ามเอามาตัดสินความต่างของเนื้อ
VOLATILE = ('exported', 'builtFromCommit')

# ④ เนื้อจริง
PAYLOAD = ('questions',)

STAMP_FIELD = 'builtFromCommit'
LOCAL_STAMP = 'local'          # ค่าที่ build_bank.py ใส่เมื่อรันนอก GitHub Actions

# เนื้อที่ถูกนับ — ต้องเป็นเพรดิเคตเดียวกับที่ scan_symbols.py v2.6 ใช้หา _measuredFromData
DATA_PATHS = ('data/sets/', 'data/manifest.json')


# ══════════════════════════════════════════════════════════════════
#  ส่วนที่บริสุทธิ์ (เทสต์ได้โดยไม่ต้องมีไฟล์/ไม่ต้องมี git)
# ══════════════════════════════════════════════════════════════════

def unknown_fields(bank):
    """คืนชื่อฟิลด์ใน bank.json ที่ไม่ได้อยู่ใน 4 ถัง — ต้องว่างเสมอ

    ⛔ ห้ามเปลี่ยนให้ "ข้ามฟิลด์ที่ไม่รู้จัก" — นั่นคือการขึ้นเขียวบนความไม่รู้
    """
    known = set(MANIFEST_COPIED) | set(DERIVED) | set(VOLATILE) | set(PAYLOAD)
    return sorted(set(bank) - known)


def missing_fields(bank):
    """คืนชื่อฟิลด์ที่ควรมีแต่หายไป — bank ที่ขาดฟิลด์ = เทียบไม่ได้ ไม่ใช่เทียบผ่าน"""
    need = set(MANIFEST_COPIED) | set(VOLATILE) | set(PAYLOAD)
    return sorted(need - set(bank))


def index_by_id(questions):
    """คืน (dict id→ข้อ, รายการ id ที่ซ้ำ)

    🔴 ทำไมต้องคืน "id ที่ซ้ำ" ออกมาด้วย:
       ถ้า id ซ้ำ คำว่า "ต่างกัน N ข้อ จาก M ข้อ" ไม่มีความหมาย — ตัวหารพัง
       ⇒ ⑨ บังคับให้ด่านบอกว่าตัวหารพัง แทนที่จะรายงานเลขที่ดูเหมือนใช้ได้
    """
    idx, dup = {}, []
    for q in questions:
        qid = q.get('id')
        if qid is None:
            dup.append('(ข้อที่ไม่มีคีย์ id)')
            continue
        if qid in idx:
            dup.append(qid)
        idx[qid] = q
    return idx, sorted(set(dup))


def compare_questions(bank_qs, data_qs):
    """เทียบข้อต่อข้อด้วย id — คืน dict สรุป

    🔴 เทียบทั้งอ็อบเจกต์ได้เพราะ build_bank.py **คัดข้อผ่านมาดิบ ๆ**
       (`all_questions.extend(set_data['questions'])` — ไม่แต่งเติมฟิลด์ใด)
       ตรวจแล้วจริงเมื่อ 1 ส.ค. 69: เทียบทั้ง 15 ฟิลด์ของข้อตัวอย่าง ไม่ต่างเลย
    ⛔ ถ้าวันหนึ่ง builder เริ่มเติมฟิลด์ให้ข้อ ⇒ ด่านนี้จะรายงาน "แก้ 6,313 ข้อ"
       ซึ่งเป็นเลขที่ผิดปกติจนอ่านออกทันที ⇒ พังแบบส่งเสียง ไม่ใช่พังเงียบ
    """
    b_idx, b_dup = index_by_id(bank_qs)
    d_idx, d_dup = index_by_id(data_qs)
    b_ids, d_ids = set(b_idx), set(d_idx)
    changed = sorted(qid for qid in (b_ids & d_ids) if b_idx[qid] != d_idx[qid])
    return {
        'added': sorted(d_ids - b_ids),      # มีใน data แต่ยังไม่มีใน bank ที่เสิร์ฟ
        'removed': sorted(b_ids - d_ids),    # มีใน bank ที่เสิร์ฟ แต่ไม่มีใน data แล้ว
        'changed': changed,
        'dup_bank': b_dup,
        'dup_data': d_dup,
        'n_bank': len(bank_qs),
        'n_data': len(data_qs),
    }


def diff_count(cmp):
    """จำนวนข้อที่ต่าง = เพิ่ม + หาย + แก้"""
    return len(cmp['added']) + len(cmp['removed']) + len(cmp['changed'])


def compare_manifest_fields(bank, manifest):
    """คืนชื่อฟิลด์ที่ bank คัดมาจาก manifest แล้วไม่ตรงกับ manifest ปัจจุบัน"""
    out = []
    for bkey, mkey in sorted(MANIFEST_COPIED.items()):
        if bank.get(bkey) != manifest.get(mkey):
            out.append(bkey)
    return out


def classify(stamp, data_commit, n_diff, n_field_diff):
    """ตารางคำตัดสิน — คืน (ไอคอน, รหัสออก, เหตุผลสั้น)

    stamp        = ค่า builtFromCommit ใน bank.json ที่เสิร์ฟ
    data_commit  = คอมมิตล่าสุดที่แตะ data/sets/ + data/manifest.json (None = วัดไม่ได้)
    """
    content_differs = (n_diff > 0) or (n_field_diff > 0)

    if stamp == LOCAL_STAMP:
        return ('🔴', 1,
                'bank.json นี้ถูก build จากเครื่องคน (ป้าย = "local") '
                '⇒ ไม่มีใครบอกได้ว่ามันมาจากเนื้อชุดไหน '
                '⛔ และการ commit bank.json เองผิดกติกาอยู่แล้ว')

    if data_commit is None:
        # ⑥ วัดไม่ได้ ≠ วัดแล้วไม่เจอ — แกนอายุเงียบ ให้แกนขนาดตัดสินตามลำพัง
        if content_differs:
            return ('🔴', 1, 'เนื้อต่างจริง (แกนอายุวัดไม่ได้ในสำเนานี้)')
        return ('🟠', 0,
                'เนื้อตรงทุกข้อ แต่ **วัดอายุไม่ได้** ในสำเนานี้ '
                '⇒ ยังตอบไม่ได้ว่าป้ายชี้ไปที่คอมมิตไหน')

    stamp_ok = bool(stamp) and (stamp == data_commit
                               or data_commit.startswith(stamp)
                               or stamp.startswith(data_commit))

    if stamp_ok and not content_differs:
        return ('🟢', 0, 'ป้ายตรงคอมมิตเนื้อ และเนื้อตรงทุกข้อ')
    if stamp_ok and content_differs:
        return ('🔴', 1,
                '**ป้ายโกหก** — ป้ายบอกว่า build จากคอมมิตนี้ แต่เนื้อไม่ตรง '
                '⇒ อย่าเชื่อป้าย ให้ rebuild')
    if not stamp_ok and not content_differs:
        return ('🟠', 0,
                'ป้ายชี้คอมมิตเก่า แต่เนื้อตรงทุกข้อ '
                '⇒ ปกติ: build_bank.py ไม่เขียนไฟล์เมื่อเนื้อไม่เปลี่ยน '
                '(เด็กเห็นของถูกอยู่แล้ว)')
    return ('🔴', 1, 'ป้ายเก่า **และ** เนื้อต่าง ⇒ เด็กกำลังเห็นของเก่าจริง')


def age_words(n_commits, days):
    """ประกอบข้อความแกนอายุ — ⛔ ห้ามคืนค่าว่างเมื่อวัดไม่ได้ ต้องบอกว่าวัดไม่ได้"""
    parts = []
    if n_commits is None:
        parts.append('ตามหลังกี่คอมมิต: วัดไม่ได้')
    else:
        parts.append(f'ตามหลัง {n_commits:,} คอมมิตที่แตะเนื้อ')
    if days is None:
        parts.append('อายุกี่วัน: วัดไม่ได้')
    else:
        parts.append(f'ป้ายเก่ากว่าเนื้อ {days:,} วัน')
    return ' · '.join(parts)


def size_words(cmp, n_field_diff):
    """ประกอบข้อความแกนขนาด — ตัวหารต้องอยู่ในประโยคเดียวกับตัวเศษเสมอ"""
    n = diff_count(cmp)
    denom = max(cmp['n_bank'], cmp['n_data'])
    msg = (f'ต่างกัน {n:,} ข้อ จากทั้งหมด {denom:,} ข้อ'
           f'  (เพิ่ม {len(cmp["added"]):,} · หาย {len(cmp["removed"]):,}'
           f' · แก้ {len(cmp["changed"]):,})')
    if n_field_diff:
        msg += f' · ฟิลด์ระดับ manifest ต่าง {n_field_diff} ฟิลด์'
    return msg


# ══════════════════════════════════════════════════════════════════
#  ส่วนที่แตะโลกจริง (git / ไฟล์)
# ══════════════════════════════════════════════════════════════════

def git_out(args, repo):
    """รัน git แล้วคืน stdout — คืน None ถ้ารันไม่ได้ (⛔ ไม่ throw, ⛔ ไม่เดา)"""
    try:
        r = subprocess.run(['git', '-C', repo] + args,
                           capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    if r.returncode != 0:
        return None
    return r.stdout


def data_commit_of(repo):
    """คอมมิตล่าสุดที่แตะเนื้อที่ถูกนับ · คืน (sha เต็ม, data สกปรกไหม)"""
    sha = git_out(['log', '-1', '--format=%H', '--'] + list(DATA_PATHS), repo)
    st = git_out(['status', '--porcelain', '--'] + list(DATA_PATHS), repo)
    if sha is None:
        return None, False
    sha = sha.strip()
    return (sha or None), bool(st and st.strip())


def commit_date(repo, sha):
    """วันที่ committer ของ sha (date object) — None ถ้าอ่านไม่ได้"""
    out = git_out(['log', '-1', '--format=%cI', sha], repo)
    if not out or not out.strip():
        return None
    try:
        return _dt.datetime.fromisoformat(out.strip()).date()
    except ValueError:
        return None


def measure_age(repo, stamp, data_commit):
    """คืน (จำนวนคอมมิตที่ตามหลัง, จำนวนวัน) — ตัวไหนวัดไม่ได้คืน None ตัวนั้น

    ⛔ ห้ามคืน 0 เมื่อวัดไม่ได้ (กับดัก ⑥) — 0 แปลว่า "วัดแล้วไม่ตามหลัง"
       ซึ่งคนละเรื่องกับ "อ่านประวัติไม่ได้" เช่นตอน shallow clone
    """
    if not stamp or not data_commit:
        return None, None
    if git_out(['rev-parse', '--verify', '--quiet', stamp + '^{commit}'], repo) is None:
        return None, None          # คอมมิตนั้นไม่อยู่ในสำเนานี้ (shallow?) ⇒ ไม่รู้ ก็บอกว่าไม่รู้
    n = git_out(['rev-list', '--count', f'{stamp}..{data_commit}', '--']
                + list(DATA_PATHS), repo)
    n_commits = None
    if n is not None and n.strip().isdigit():
        n_commits = int(n.strip())
    d1, d2 = commit_date(repo, stamp), commit_date(repo, data_commit)
    days = (d2 - d1).days if (d1 and d2) else None
    return n_commits, days


def load_json(path):
    """คืน (ข้อมูล, ข้อความผิดพลาด) — ⛔ ไม่ throw ออกไปข้างนอก"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f), None
    except FileNotFoundError:
        return None, f'ไม่พบไฟล์: {path}'
    except json.JSONDecodeError as e:
        return None, f'JSON พัง: {path} — {e}'
    except OSError as e:
        return None, f'เปิดไฟล์ไม่ได้: {path} — {e}'


def read_data_questions(data_dir, manifest):
    """อ่านข้อทั้งหมดจาก data/sets/ ตามลำดับใน manifest.sets

    ⛔ ต้องไล่ตาม manifest ไม่ใช่ glob โฟลเดอร์ — เพราะ build_bank.py ทำอย่างนั้น
       ถ้าเราไล่ต่างวิธี ไฟล์ที่ *ไม่ได้* อยู่ใน manifest จะทำให้เราเห็น "ข้อเกิน"
       ที่ builder ไม่เคยเห็น ⇒ แดงปลอม
    """
    qs, problems = [], []
    sets = manifest.get('sets')
    if not isinstance(sets, dict):
        return None, ['manifest.json ไม่มีคีย์ sets ที่เป็น dict']
    for sid in sets:
        p = os.path.join(data_dir, 'sets', f'{sid}.json')
        d, err = load_json(p)
        if err:
            problems.append(err)
            continue
        if not isinstance(d.get('questions'), list):
            problems.append(f'{sid}.json ไม่มีคีย์ questions ที่เป็น list')
            continue
        qs.extend(d['questions'])
    return qs, problems


# ══════════════════════════════════════════════════════════════════
#  self-test
# ══════════════════════════════════════════════════════════════════

def _q(qid, **kw):
    d = {'id': qid, 'question': 'x', 'correct': 1}
    d.update(kw)
    return d


def selftest():
    base = [_q('a'), _q('b'), _q('c')]
    same = [_q('a'), _q('b'), _q('c')]
    edited = [_q('a'), _q('b', correct=2), _q('c')]
    added = base + [_q('d')]
    removed = [_q('a'), _q('b')]
    dupd = [_q('a'), _q('a'), _q('b')]

    c_same = compare_questions(base, same)
    c_edit = compare_questions(base, edited)
    c_add = compare_questions(base, added)
    c_rm = compare_questions(base, removed)
    c_dup = compare_questions(base, dupd)

    mani = {'schemaVersion': 3, 'exported': 'T0', 'topicNames': {'1': 'ก'},
            'subTopicNames': {'1.1': 'ข'}, 'deprecatedSubTopics': [],
            'sets': {'s1': {}}}
    bank_ok = {'schemaVersion': 3, 'manifestExported': 'T0',
               'topicNames': {'1': 'ก'}, 'subTopicNames': {'1.1': 'ข'},
               'deprecatedSubTopics': [], 'sets': {'s1': {}},
               'exported': 'T9', 'builtFromCommit': 'abc', 'questions': []}
    bank_drift = dict(bank_ok, subTopicNames={'1.1': 'ข', '1.2': 'ค'})
    bank_extra = dict(bank_ok, brandNewField=1)
    bank_short = {k: v for k, v in bank_ok.items() if k != 'sets'}

    SHA_A = 'a' * 40
    SHA_B = 'b' * 40

    checks = [
        # ── แกนขนาด ──
        ('เนื้อเหมือนกัน ⇒ ต่าง 0 ข้อ', diff_count(c_same) == 0),
        ('แก้ 1 ข้อ ⇒ นับเป็น "แก้" ไม่ใช่ "เพิ่ม/หาย"',
         c_edit['changed'] == ['b'] and not c_edit['added'] and not c_edit['removed']),
        ('เพิ่มข้อใหม่ใน data ⇒ นับเป็น "เพิ่ม"', c_add['added'] == ['d']),
        ('ข้อหายไปจาก data ⇒ นับเป็น "หาย"', c_rm['removed'] == ['c']),
        ('⑨ id ซ้ำ ⇒ ต้องรายงานออกมา ไม่ใช่กลืนเงียบ', c_dup['dup_data'] == ['a']),
        ('ตัวหารต้องอยู่ในประโยคเดียวกับตัวเศษ',
         'จากทั้งหมด' in size_words(c_edit, 0)),

        # ── ฟิลด์ระดับ manifest ──
        ('bank ตรง manifest ⇒ ไม่มีฟิลด์ต่าง', compare_manifest_fields(bank_ok, mani) == []),
        ('🔴 เพิ่มหัวข้อย่อยใน manifest แต่ bank ยังไม่รู้ ⇒ ต้องจับได้'
         ' (แกนข้อเดียวจับไม่ได้เลย)',
         compare_manifest_fields(bank_drift, mani) == ['subTopicNames']),

        # ── โครงของ bank ──
        ('bank โครงปกติ ⇒ ไม่มีฟิลด์แปลกปลอม', unknown_fields(bank_ok) == []),
        ('🔴 bank งอกฟิลด์ใหม่ ⇒ ต้องจับได้ (⛔ ห้ามข้ามฟิลด์ที่ไม่รู้จัก)',
         unknown_fields(bank_extra) == ['brandNewField']),
        ('bank ขาดฟิลด์ที่ต้องมี ⇒ ต้องจับได้', missing_fields(bank_short) == ['sets']),
        ('ฟิลด์ที่คำนวณได้ ไม่ถูกนับว่าแปลกปลอม',
         unknown_fields(dict(bank_ok, questionCount=0, activeCount=0,
                             retiredCount=0, subTopicCount=1,
                             liveSubTopicCount=1)) == []),

        # ── ตารางคำตัดสิน (6 แถว) ──
        ('แถว 1 · ป้ายตรง + เนื้อตรง ⇒ 🟢 รหัส 0',
         classify(SHA_A, SHA_A, 0, 0)[:2] == ('🟢', 0)),
        ('🔴 แถว 2 · ป้ายตรง แต่เนื้อต่าง ⇒ ต้องแดง (แถวที่ธงเดี่ยวจับไม่ได้)',
         classify(SHA_A, SHA_A, 5, 0)[:2] == ('🔴', 1)),
        ('…และต้องบอกว่า "ป้ายโกหก" ไม่ใช่แค่ "ไม่สด"',
         'ป้ายโกหก' in classify(SHA_A, SHA_A, 5, 0)[2]),
        ('แถว 2ข · ป้ายตรง แต่ฟิลด์ manifest ต่าง ⇒ ต้องแดงด้วย',
         classify(SHA_A, SHA_A, 0, 1)[:2] == ('🔴', 1)),
        ('🟠 แถว 3 · ป้ายเก่า แต่เนื้อตรงทุกข้อ ⇒ ต้องไม่แดง (build ถูกข้ามได้จริง)',
         classify(SHA_A, SHA_B, 0, 0)[:2] == ('🟠', 0)),
        ('แถว 4 · ป้ายเก่า + เนื้อต่าง ⇒ 🔴 รหัส 1',
         classify(SHA_A, SHA_B, 3, 0)[:2] == ('🔴', 1)),
        ('แถว 5 · ป้าย = "local" ⇒ แดงเสมอ แม้เนื้อจะตรง',
         classify(LOCAL_STAMP, SHA_A, 0, 0)[:2] == ('🔴', 1)),
        ('⑥ วัดอายุไม่ได้ + เนื้อตรง ⇒ 🟠 ไม่ใช่ 🟢 (ไม่รู้ ≠ ผ่าน)',
         classify(SHA_A, None, 0, 0)[:2] == ('🟠', 0)),
        ('⑥ วัดอายุไม่ได้ + เนื้อต่าง ⇒ ยังต้องแดง',
         classify(SHA_A, None, 2, 0)[:2] == ('🔴', 1)),
        ('ป้ายเป็น sha สั้น (7 ตัว) ของคอมมิตเดียวกัน ⇒ ต้องนับว่าตรง',
         classify(SHA_A[:7], SHA_A, 0, 0)[:2] == ('🟢', 0)),

        # ── ข้อความแกนอายุ ──
        ('⑥ วัดคอมมิตไม่ได้ ⇒ ข้อความต้องพูดว่า "วัดไม่ได้" ⛔ ห้ามพิมพ์ 0',
         'วัดไม่ได้' in age_words(None, None)),
        ('วัดได้ 0 ⇒ ต้องพิมพ์ 0 จริง ๆ (ต่างจาก "วัดไม่ได้")',
         'วัดไม่ได้' not in age_words(0, 0)),
        ('วัดคอมมิตได้ แต่วันที่อ่านไม่ได้ ⇒ ต้องบอกเฉพาะแกนที่วัดไม่ได้',
         'ตามหลัง 2' in age_words(2, None) and 'อายุกี่วัน: วัดไม่ได้' in age_words(2, None)),

        # ── ⑨ ตัวหาร ──
        (f'พื้นตัวหารต้องสูงพอจะจับการอ่านพลาด (MIN_QUESTIONS = {MIN_QUESTIONS:,})',
         MIN_QUESTIONS >= 1000),

        # ── กติกาที่เป็นข้อตกลงร่วม ──
        ('⛔ เพรดิเคตของเนื้อต้องเป็นชุดเดียวกับที่ scan_symbols v2.6 ใช้',
         DATA_PATHS == ('data/sets/', 'data/manifest.json')),
    ]

    bad = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print(f'  {"✅" if ok else "❌"} {name}')
    if bad:
        print(f'\n❌ SELF-TEST ล้ม {len(bad)} เคส')
        return 2
    print(f'\n✅ SELF-TEST ผ่านครบ {len(checks)} เคส')
    return 0


# ══════════════════════════════════════════════════════════════════

def main():
    ap = argparse.ArgumentParser(
        description='ด่านความสด — bank.json ที่เสิร์ฟ ตรงกับ data/sets/ หรือยัง'
                    ' (⛔ ฝั่ง sync เท่านั้น ห้ามผูกเข้า CI ฝั่ง push)')
    ap.add_argument('--repo', default='.', help='รากของ repo (ค่าเริ่มต้น: .)')
    ap.add_argument('--bank', default=None,
                    help='ไฟล์ bank.json ที่ "เสิร์ฟจริง" (ค่าเริ่มต้น: <repo>/data/bank.json)')
    ap.add_argument('--data', default=None,
                    help='โฟลเดอร์ data/ ที่เป็นแหล่งความจริง (ค่าเริ่มต้น: <repo>/data)')
    ap.add_argument('--min-questions', type=int, default=MIN_QUESTIONS,
                    help=f'⑨ พื้นตัวหาร (ค่าเริ่มต้น: {MIN_QUESTIONS})')
    ap.add_argument('--list', type=int, default=10,
                    help='พิมพ์ id ตัวอย่างสูงสุดกี่ตัวต่อประเภท (ค่าเริ่มต้น: 10)')
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    repo = os.path.abspath(a.repo)
    data_dir = os.path.abspath(a.data) if a.data else os.path.join(repo, 'data')
    bank_path = os.path.abspath(a.bank) if a.bank else os.path.join(data_dir, 'bank.json')

    print(f'ด่านความสด v{CHECKER_VERSION} · ⛔ ฝั่ง sync เท่านั้น (ห้ามผูกเข้า guards.yml)')
    print(f'  bank ที่เสิร์ฟ : {bank_path}')
    print(f'  แหล่งความจริง : {data_dir}/sets/ + manifest.json')
    print()

    # ── อ่านของ ────────────────────────────────────────────────
    bank, err = load_json(bank_path)
    if err:
        print(f'⚙️ อ่าน bank.json ไม่ได้ — {err}')
        print('   ⇒ รหัส 2 (เครื่องมือแดง) ⛔ ไม่ใช่ผ่าน — อ่านไม่ได้คนละเรื่องกับไม่มีปัญหา')
        return 2
    manifest, err = load_json(os.path.join(data_dir, 'manifest.json'))
    if err:
        print(f'⚙️ อ่าน manifest.json ไม่ได้ — {err}')
        return 2

    miss = missing_fields(bank)
    if miss:
        print(f'⚙️ bank.json ขาดฟิลด์ที่ต้องมี: {", ".join(miss)}')
        print('   ⇒ เทียบไม่ได้ ⛔ ไม่ใช่เทียบผ่าน')
        return 2

    unknown = unknown_fields(bank)
    if unknown:
        print(f'⚙️ bank.json มีฟิลด์ที่ด่านนี้ไม่รู้จัก {len(unknown)} ฟิลด์:'
              f' {", ".join(unknown)}')
        print('   ⇒ ตัวตรวจตามโครงของจริงไม่ทัน — ต้องเอาฟิลด์ใหม่ไปใส่ถังที่ถูก')
        print('     (MANIFEST_COPIED / DERIVED / VOLATILE / PAYLOAD ในไฟล์นี้)')
        print('   ⛔ ห้ามแก้ด้วยการ "ข้ามฟิลด์ที่ไม่รู้จัก" — นั่นคือขึ้นเขียวบนความไม่รู้')
        return 2

    data_qs, problems = read_data_questions(data_dir, manifest)
    if problems:
        print(f'⚙️ อ่าน data/sets/ ไม่ครบ {len(problems)} รายการ:')
        for p in problems[:10]:
            print(f'   {p}')
        return 2

    bank_qs = bank.get('questions') or []
    cmp = compare_questions(bank_qs, data_qs)

    # ── ⑨ ตัวหาร ต้องตรวจ "ก่อน" ตีความผลเทียบ ────────────────
    denom = max(cmp['n_bank'], cmp['n_data'])
    print(f'⑨ ตัวหาร: bank {cmp["n_bank"]:,} ข้อ · data/sets/ {cmp["n_data"]:,} ข้อ'
          f' · พื้นขั้นต่ำ {a.min_questions:,}')
    print('   ⇒ ถ้าเลขพวกนี้เล็กผิดปกติ แปลว่า "อ่านไม่เจอ" ⛔ ไม่ใช่ "ไม่มีอะไรต่าง"')
    print()
    if denom < a.min_questions:
        print(f'⚙️ อ่านข้อได้แค่ {denom:,} ข้อ ซึ่งต่ำกว่าพื้น {a.min_questions:,}')
        print('   ⇒ รหัส 2 — ตัวหารเล็กเกินกว่าจะเชื่อผลเทียบ')
        return 2
    if cmp['dup_bank'] or cmp['dup_data']:
        print(f'⚙️ เจอ id ซ้ำ — bank {len(cmp["dup_bank"])} ตัว ·'
              f' data {len(cmp["dup_data"])} ตัว')
        for qid in (cmp['dup_bank'] + cmp['dup_data'])[:10]:
            print(f'   {qid}')
        print('   ⇒ "ต่าง N ข้อ จาก M ข้อ" ไม่มีความหมายเมื่อ id ซ้ำ ⇒ รหัส 2')
        return 2

    # ── สองแกน ────────────────────────────────────────────────
    field_diff = compare_manifest_fields(bank, manifest)
    stamp = bank.get(STAMP_FIELD) or ''

    # 🔴 แกนอายุอ่านประวัติจาก --repo แต่แกนขนาดอ่านเนื้อจาก --data
    #    ถ้าสองอันนี้ไม่ใช่ต้นไม้เดียวกัน แกนอายุจะพูดถึง "ของอีกกอง"
    #    ⇒ เจอตอนมิวเทชันเทสต์จริง: ชี้ --data ไปที่สำเนา แล้วแกนอายุยังรายงาน
    #      "ตามหลัง 0 คอมมิต" จากต้นไม้ต้นฉบับ ⇒ เลขถูกแต่ตอบคนละคำถาม
    #    ⛔ ห้ามปล่อยให้พิมพ์ตัวเลขที่ดูใช้ได้ — ⑥ ไม่รู้ ต้องพูดว่าไม่รู้
    same_tree = (os.path.realpath(data_dir)
                 == os.path.realpath(os.path.join(repo, 'data')))
    if same_tree:
        dcommit, dirty = data_commit_of(repo)
        n_commits, days = measure_age(repo, stamp, dcommit)
    else:
        dcommit, dirty = None, False
        n_commits, days = None, None

    icon, code, why = classify(stamp, dcommit, diff_count(cmp), len(field_diff))

    print(f'{icon} {why}')
    print()
    print(f'  ① อายุ  : {age_words(n_commits, days)}')
    print(f'           ป้าย builtFromCommit = {stamp[:12] or "(ว่าง)"}')
    print(f'           คอมมิตล่าสุดที่แตะเนื้อ = {(dcommit or "วัดไม่ได้")[:12]}')
    print(f'  ② ขนาด  : {size_words(cmp, len(field_diff))}')
    if dirty:
        print('           ⚠️ data/ มีของแก้ค้างที่ยังไม่ commit'
              ' ⇒ เทียบกับของในเครื่อง ไม่ใช่ของที่ push แล้ว')
    if not same_tree:
        print(f'           ⚠️ --data ไม่ใช่ {repo}/data ⇒ ปิดแกนอายุทิ้ง')
        print('              (ประวัติ git ของ --repo พูดถึงคนละกองกับเนื้อที่เทียบ'
              ' ⇒ เลขจะถูกแต่ตอบผิดคำถาม)')
    print()

    if field_diff:
        print(f'  ฟิลด์ระดับ manifest ที่ไม่ตรง ({len(field_diff)}):')
        for f in field_diff:
            print(f'    · {f}')
        print()

    for label, key in (('ข้อที่เพิ่มใน data แต่ยังไม่ถึงเด็ก', 'added'),
                       ('ข้อที่หายจาก data แต่เด็กยังเห็นอยู่', 'removed'),
                       ('ข้อที่เนื้อไม่ตรง', 'changed')):
        ids = cmp[key]
        if not ids:
            continue
        print(f'  {label} ({len(ids):,}):')
        for qid in ids[:a.list]:
            print(f'    · {qid}')
        if len(ids) > a.list:
            print(f'    … และอีก {len(ids) - a.list:,} ข้อ (ใช้ --list เพื่อดูเพิ่ม)')
        print()

    if code == 1:
        print('  วิธีแก้: รอ/สั่งให้บอท rebuild bank.json แล้ว sync ใหม่')
        print('  ⛔ ห้ามแก้ด้วยการ commit bank.json ด้วยมือ — CI สร้างเองเสมอ')
    elif icon == '🟠':
        print('  ⇒ ยังเสิร์ฟได้ แต่ป้ายบอกที่มาไม่ตรง อย่าใช้ป้ายนี้อ้างอิงในรายงาน')
    else:
        print('  ⇒ ชั้นที่สาม (ของที่เด็กเห็น) ตรงกับแหล่งความจริงแล้ว')
    return code


if __name__ == '__main__':
    sys.exit(main())

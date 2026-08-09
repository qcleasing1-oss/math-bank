# -*- coding: utf-8 -*-
"""ตัวหารกลาง — "คลังจริงทั้งใบ" สำหรับด่านของสายแต่งข้อสอบ   · 8 ส.ค. 2569

═══ ทำไมต้องมีไฟล์นี้ ═══
ก้อน 22 ตาย 5 ข้อ (2 ใบซ้ำข้อสอบจริง) ทั้งที่ทุกด่านเขียว รากไม่ใช่ "ลืมกวาด"
แต่เป็น **ตัวหารของด่าน ≠ ตัวหารของคำถาม** :

    molds.py   ตัวหาร = 164 ข้อที่เราแต่งเอง
    คำถามจริง  ตัวหาร = 6,477 ข้อทั้งคลัง
    ⇒ ด่านตอบคำถาม "ซ้ำของเราเองไหม" ได้ถูก 100%
    ⇒ แต่คนอ่านคิดว่ามันตอบ "เคยมีคนถามแล้วหรือยัง"

⇒ ⇒ ยาแก้ ⛔ ไม่ใช่ "จำให้ได้" — คือทำให้ตัวหารของด่าน **เป็น** ตัวหารของคำถาม
   ไฟล์นี้คือตัวหารนั้น · ด่านไหนนำเข้าไฟล์นี้ จะ **รันไม่ได้ถ้าไม่เห็นคลังครบ**

═══ กติกาที่ไฟล์นี้บังคับ ═══
① อ่านคลังไม่ได้ / อ่านได้น้อยกว่าพื้น ⇒ โยน BankUnavailable
   ⛔ ห้ามคืน "0 ข้อ" แล้วปล่อยให้ผู้เรียกตีความว่าสะอาด
   ("ไม่เจอของซ้ำ จาก 0 ข้อ" กับ "ไม่เจอของซ้ำ จาก 6,477 ข้อ" พิมพ์ออกมาเหมือนกันเป๊ะ)
② ป้ายของตัวหารต้องครบ ㊳ 5 ขา — ไฟล์นี้ออกให้ 3 ขาที่เป็นของคลัง
   (ที่มา = data/sets · หน่วย = ข้อไม่ซ้ำ · ขอบเขต = ทุกชุดรวมข้อสอบจริง)
   ผู้เรียกเติมอีก 2 ขาเอง (เวลาที่วัด · คอมมิตที่ใช้ตัดสิน)

รันตรง ๆ เพื่อดูตัวหารวันนี้:  python3 tools/authoring/k2/bankscope.py
รันชุดทดสอบของตัวเอง:        python3 tools/authoring/k2/bankscope.py --selftest
"""
import io, os, json, glob, hashlib, sys

# พื้นตัวหาร — ต่ำกว่านี้แปลว่าอ่านคลังไม่ครบ ⛔ ไม่ใช่ "คลังเล็ก"
# (ตัวเลขเดียวกับ --min-questions ปริยายของ scripts/scan_symbols.py)
MIN_QUESTIONS = 6000

_HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = os.path.normpath(os.path.join(_HERE, '..', '..', '..'))


class BankUnavailable(RuntimeError):
    """อ่านคลังไม่ได้ = **ตัวตรวจใช้ไม่ได้** ⛔ ไม่ใช่ "ตรวจแล้วสะอาด"

    🔴 นี่คือเหตุผลทั้งหมดที่ไฟล์นี้มีอยู่: ถ้าโยนไม่ได้ ผู้เรียกจะเผลอเดินต่อ
       ด้วยตัวหารที่หดลงเงียบ ๆ แล้วรายงานผลด้วยน้ำเสียงเดิม
    """


def load_bank(root=None, min_questions=MIN_QUESTIONS):
    """อ่านคลังทั้งใบ — คืน dict ของตัวหาร · โยน BankUnavailable ถ้าอ่านไม่ครบ

    ตัดข้อซ้ำด้วย `id` แบบเดียวกับ collide_bNN.py เป๊ะ (ตัวหารเดียวกันโดยโครงสร้าง)
    """
    root = root or DEFAULT_ROOT
    sets_dir = os.path.join(root, 'data', 'sets')
    if not os.path.isdir(sets_dir):
        raise BankUnavailable(f'ไม่พบโฟลเดอร์คลัง: {sets_dir}')
    paths = sorted(glob.glob(os.path.join(sets_dir, '*.json')))
    if not paths:
        raise BankUnavailable(f'โฟลเดอร์คลังว่าง: {sets_dir}')

    seen, ids = set(), []
    for p in paths:
        try:
            d = json.load(io.open(p, encoding='utf-8'))
        except (ValueError, OSError) as e:
            # ⛔ ห้ามข้ามไฟล์ที่พังแล้วเดินต่อ — ตัวหารจะหดโดยไม่มีใครรู้
            raise BankUnavailable(f'อ่านไฟล์ชุดไม่ได้: {os.path.basename(p)} — {e}')
        for q in d.get('questions', []):
            i = q.get('id')
            if i is None or i in seen:
                continue
            seen.add(i)
            ids.append(i)

    if len(ids) < min_questions:
        raise BankUnavailable(
            f'อ่านได้ {len(ids):,} ข้อ — ต่ำกว่าพื้น {min_questions:,} ข้อ'
            ' ⇒ ผลรอบนี้ใช้อ้างอิงไม่ได้ (อาจชี้ผิดโฟลเดอร์/ไฟล์หายไป)')

    return {
        'files': len(paths),
        'questions': len(ids),
        'idDigest': hashlib.sha256('\n'.join(sorted(ids)).encode()).hexdigest()[:16],
        'ids': frozenset(ids),
    }


def scope_str(bank):
    """ป้ายตัวหารแบบสตริงเดียว — รูปแบบนี้คือสิ่งที่ถูกเก็บลงใบเสร็จ

    ⚠️ มี idDigest อยู่ด้วยโดยตั้งใจ: "จำนวนข้อเท่าเดิม" ⛔ ไม่ได้แปลว่า "คลังเดิม"
       (ถอน 1 เพิ่ม 1 ⇒ ยอดนิ่ง แต่ของที่ต้องกวาดเปลี่ยนไปแล้ว)
    """
    return '%dไฟล์·%dข้อ·%s' % (bank['files'], bank['questions'], bank['idDigest'])


def compare_scope(receipt_scope, bank):
    """เทียบป้ายในใบเสร็จกับคลัง ณ ตอนนี้ — คืน (ผ่านไหม, เหตุผล)

    🔴 กงล้อ: คลังโตขึ้นตั้งแต่วันกวาด ⇒ ใบเสร็จ **หมดอายุ** ⇒ ต้องกวาดใหม่
       ⛔ ไม่ใช่ "เตือนเฉย ๆ" — ใบเสร็จที่กวาดจากคลัง 6,000 ข้อ
       ไม่เคยพูดอะไรเลยเกี่ยวกับข้อที่ 6,001
    """
    now = scope_str(bank)
    if receipt_scope == now:
        return True, 'ตรงกับคลังวันนี้'
    try:
        n_old = int(receipt_scope.split('·')[1].replace('ข้อ', ''))
    except (IndexError, ValueError):
        return False, f'ป้ายในใบเสร็จอ่านไม่ได้ ({receipt_scope!r}) ⇒ เทียบไม่ได้ ⇒ ไม่ถือว่าผ่าน'
    if n_old < bank['questions']:
        return False, (f'กวาดไว้ตอนคลังมี {n_old:,} ข้อ · วันนี้ {bank["questions"]:,} ข้อ'
                       f' ⇒ ใบเสร็จหมดอายุ ต้องกวาดใหม่')
    if n_old > bank['questions']:
        return False, (f'ใบเสร็จอ้างคลัง {n_old:,} ข้อ แต่วันนี้เหลือ {bank["questions"]:,} ข้อ'
                       ' ⇒ คลังหดลง — ตรวจว่าชี้ถูกโฟลเดอร์ไหม')
    return False, (f'จำนวนข้อเท่ากัน ({n_old:,}) แต่ลายนิ้วมือต่าง'
                   ' ⇒ มีข้อถูกสลับ/แทนที่ตั้งแต่วันกวาด ⇒ ใบเสร็จหมดอายุ')


# ═══════════════════════ ชุดทดสอบของตัวเอง (㊶) ═══════════════════════
def selftest():
    import tempfile, shutil
    ok = True

    def say(name, good):
        nonlocal ok
        print('  %s %s' % ('✅' if good else '🔴 ล้ม', name))
        ok &= bool(good)

    bank = load_bank()
    say('อ่านคลังจริงได้ · %s' % scope_str(bank),
        bank['questions'] >= MIN_QUESTIONS and bank['files'] > 1)

    # ① โฟลเดอร์ไม่มี ⇒ ต้องโยน ⛔ ไม่ใช่คืน 0
    tmp = tempfile.mkdtemp()
    try:
        try:
            load_bank(tmp)
            say('โฟลเดอร์คลังหาย ⇒ ต้องโยน BankUnavailable', False)
        except BankUnavailable:
            say('โฟลเดอร์คลังหาย ⇒ โยน BankUnavailable ⛔ ไม่คืน 0 ข้อ', True)

        # ② คลังหดลงต่ำกว่าพื้น ⇒ ต้องโยน (เคสจริง: ชี้ผิดโฟลเดอร์ย่อย)
        os.makedirs(os.path.join(tmp, 'data', 'sets'))
        io.open(os.path.join(tmp, 'data', 'sets', 'tiny.json'), 'w',
                encoding='utf-8').write(json.dumps(
                    {'questions': [{'id': 'x1'}, {'id': 'x2'}]}, ensure_ascii=False))
        try:
            load_bank(tmp)
            say('คลัง 2 ข้อ ⇒ ต้องโยน (ต่ำกว่าพื้น)', False)
        except BankUnavailable:
            say('คลัง 2 ข้อ ⇒ โยน (ต่ำกว่าพื้น) ⛔ ไม่รายงานว่าสะอาด', True)

        # ③ ไฟล์ JSON พัง ⇒ ต้องโยน ⛔ ห้ามข้ามไฟล์แล้วเดินต่อ
        io.open(os.path.join(tmp, 'data', 'sets', 'broken.json'), 'w',
                encoding='utf-8').write('{ พัง')
        try:
            load_bank(tmp, min_questions=0)
            say('ไฟล์ชุดพัง ⇒ ต้องโยน ⛔ ห้ามข้ามเงียบ ๆ', False)
        except BankUnavailable:
            say('ไฟล์ชุดพัง ⇒ โยน ⛔ ไม่ข้ามเงียบ ๆ (ตัวหารจะหดโดยไม่มีใครรู้)', True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # ④ ป้ายตรงกับคลังวันนี้ ⇒ ผ่าน
    say('ใบเสร็จที่ป้ายตรง ⇒ ผ่าน', compare_scope(scope_str(bank), bank)[0] is True)

    # ⑤ ใบเสร็จกวาดตอนคลังเล็กกว่า ⇒ ต้องหมดอายุ
    old = '63ไฟล์·%dข้อ·%s' % (bank['questions'] - 1, bank['idDigest'])
    good5, why5 = compare_scope(old, bank)
    # ⛔ ห้ามตัดข้อความด้วย [:40] — E→MB #51 §5 จับได้ว่ามันตัดเลขขาดกลางคำ
    #    ("วันนี้ 6,47)") · เป็นข้อความที่คนอ่านตอนด่านแดง ⇒ ㊳ ตัวเลขที่ป้ายไม่ครบ
    say('ใบเสร็จกวาดตอนคลังเล็กกว่า ⇒ หมดอายุ', good5 is False)
    print('       เหตุที่ด่านให้: %s' % why5)

    # ⑥ 🔑 ยอดเท่ากันแต่ลายนิ้วมือต่าง ⇒ ต้องหมดอายุ
    #    (ถอน 1 เพิ่ม 1 ⇒ ยอดนิ่ง — เคสที่ป้ายแบบ "นับอย่างเดียว" จับไม่ได้)
    swapped = '63ไฟล์·%dข้อ·%s' % (bank['questions'], '0' * 16)
    say('ยอดเท่ากันแต่ลายนิ้วมือต่าง (ถอน1เพิ่ม1) ⇒ ต้องหมดอายุ',
        compare_scope(swapped, bank)[0] is False)

    # ⑦ ป้ายอ่านไม่ได้ ⇒ "เทียบไม่ได้" ≠ "เทียบแล้วผ่าน"
    say('ป้ายอ่านไม่ได้ ⇒ ไม่ถือว่าผ่าน', compare_scope('ของมั่ว', bank)[0] is False)

    # ⑧ 🧬 กลายพันธุ์: ถ้า compare_scope ปล่อยผ่านทุกอย่าง ด่าน ⑤⑥⑦ ต้องล้ม
    say('🧬 ด่าน ⑤⑥⑦ รับน้ำหนักจริง (มีอย่างน้อย 3 เคสที่ต้องคืน False)',
        sum(1 for s in (old, swapped, 'ของมั่ว')
            if compare_scope(s, bank)[0] is False) == 3)
    return ok


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        print('▼▼▼ ชุดทดสอบของ bankscope เอง (㊶) ▼▼▼')
        passed = selftest()
        print('ผลชุดทดสอบ:', 'ผ่านครบ ✅' if passed else 'ล้ม ❌')
        sys.exit(0 if passed else 1)
    b = load_bank()
    print('ตัวหารคลังวันนี้ :', scope_str(b))
    print('  ที่มา    : data/sets/*.json  (%d ไฟล์)' % b['files'])
    print('  หน่วย    : ข้อไม่ซ้ำ (ตัดซ้ำด้วย id เหมือน collide_bNN.py)')
    print('  ขอบเขต   : ทุกชุด ⛔ ไม่ใช่เฉพาะชุดที่เราแต่งเอง')

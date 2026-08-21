# -*- coding: utf-8 -*-
"""linebreak — จัดบรรทัดเฉลยให้ขึ้นบรรทัดใหม่ที่ตัวเชื่อม **โดยไม่ทำลายโครงที่ด่านตรวจ**

═══ ทำไมไฟล์นี้ถึงมี ═══
ครู QC อ่านก้อน 23 แล้วบอกว่า *"เฉลยพิมพ์ต่อยาวกันไม่มีการจัดบรรทัดให้อ่านง่ายเลย
พิมพ์เรียงติดกันแบบนี้เด็กอ่านยาก ใช้ ⇒ เป็นตัวเชื่อมควรขึ้นบรรทัดใหม่"*  (13 ส.ค. 2569)

⬤ วัดของจริงตอนนั้น (20 ข้อ · 1,244 บรรทัดที่ไม่ว่าง):
    บรรทัดยาวเกิน 200 ตัวอักษร = **577 บรรทัด (46%)** · ความยาวกลาง 190 · **ยาวสุด 794**
    ตัวเชื่อม `⇒` ที่อยู่นอกสูตร = **1,867 ตัว** ⇒ เฉลี่ย 1.5 ตัวต่อบรรทัด

═══ 🔴 ทำไมถึงตัดมั่วไม่ได้ — ด่านที่จะพังถ้าตัดผิดที่ ═══
    ① `$` ต้องคู่กันในทุกบรรทัด        ⇒ ห้ามตัดกลาง `$...$`
    ② `<b>` ต้องปิดในบรรทัดเดียวกัน     ⇒ ห้ามตัดกลาง `<b>...</b>` (ไม่งั้นแท็กค้าง)
    ③ บรรทัด `✅ <b>คำตอบ</b>` ต้องลงท้ายด้วย `→ <b>ตัวเลือก N</b>` เป๊ะ ⇒ **ห้ามตัดบรรทัดนี้เลย**
       (และข้อ fill ด่าน 17 บังคับว่าค่าคำตอบต้องอยู่ในบรรทัดนั้น)
    ④ บล็อก 📚 นับบรรทัดที่ขึ้นต้นด้วย `• ` ต้องได้ 4–6 ⇒ **ท่อนต่อห้ามขึ้นต้นด้วย `• `**
    ⑤ บรรทัดหัวข้อ (`<b>ขั้นที่ N`, `<b>【`) ตรวจด้วย startswith ⇒ ท่อนแรกต้องคงหัวเดิมไว้

═══ ⚠️ ㊳ ป้ายกำกับ ═══
    วิธีวัด : ตัดที่ตัวเชื่อมที่อยู่ **นอก** `$...$` และ **นอก** `<b>...</b>` เท่านั้น
    หน่วย   : บรรทัดใน list ของ `explanation`
    ขอบเขต  : เฉพาะก้อนที่ build ผ่านไฟล์นี้ ⛔ **ไม่แตะข้อเดิมในคลัง**
    🔒 จุดบอด : ⛔ ไม่รู้ว่าตัวเรนเดอร์ของพอร์ทัลขึ้นบรรทัดใหม่ให้ทุกสมาชิกของ list จริงไหม
                — ยึดจากโครงสร้างเดิมของคลังที่แยกหัวข้อเป็นคนละสมาชิก ⇒ **ต้องให้ครูดูของจริงยืนยัน**
    🔒 จุดบอด : บรรทัดชื่อวิธี `<b>【 … 】</b>` **ยังยาวได้ถึง ~380 ตัวอักษร** เพราะทั้งบรรทัด
                อยู่ในแท็ก `<b>` เดียว ⇒ ตัดแล้วแท็กค้าง ⇒ **ตั้งใจไม่ตัด** (23 บรรทัดจาก 3,281)
                ⇒ ถ้าครูอยากให้สั้นลงด้วย ต้องแก้ที่ **วิธีเขียนหัวข้อ** ⛔ ไม่ใช่ที่ตัวจัดบรรทัด

รันชุดทดสอบของตัวเอง:  python3 linebreak.py --selftest
"""
import sys

__version__ = '1.0'

# ตัวเชื่อมหลักที่ครูสั่งให้ขึ้นบรรทัดใหม่
ARROW = '⇒'
# ตัวคั่นรอง — ใช้ต่อเมื่อท่อนยัง **ยาวมาก** หลังตัดด้วย ⇒ แล้ว
MIDDOT = ' · '

SPLIT_MIN = 80         # บรรทัดสั้นกว่านี้ ⛔ ไม่ตัด (ตัดแล้วเป็นเศษสั้น ๆ อ่านยากกว่าเดิม)
MIDDOT_MIN = 190       # ท่อนที่ยังยาวเกินนี้ จึงตัดด้วย · ต่อ
NEVER_SPLIT = ('✅ <b>คำตอบ</b>',)


def _safe_positions(s, token):
    """ตำแหน่งของ token ที่อยู่ **นอก** `$...$` และ **นอก** `<b>...</b>`"""
    pos, in_math, in_b, i = [], False, 0, 0
    while i < len(s):
        if s[i] == '$':
            in_math = not in_math
            i += 1
            continue
        if not in_math:
            if s.startswith('<b>', i):
                in_b += 1
                i += 3
                continue
            if s.startswith('</b>', i):
                in_b = max(0, in_b - 1)
                i += 4
                continue
            if in_b == 0 and s.startswith(token, i):
                pos.append(i)
        i += 1
    return pos


def _cut(line, token, keep_token_on_new_line=True):
    """ตัดบรรทัดที่ทุกตำแหน่งของ token ที่ปลอดภัย · คืน list ของท่อน"""
    pos = _safe_positions(line, token)
    if not pos:
        return [line]
    out, prev = [], 0
    for p in pos:
        piece = line[prev:p].rstrip()
        if piece:
            out.append(piece)
        prev = p if keep_token_on_new_line else p + len(token)
    tail = line[prev:].rstrip()
    if tail:
        out.append(tail)
    return out or [line]


def _ok(piece, is_first=False):
    """ท่อนหนึ่งใช้ได้ไหม — `$` คู่ · `<b>` ปิดครบ · **ท่อนต่อ** ⛔ ไม่ขึ้นต้นด้วย `• `

    ⚠️ กฎ `• ` ใช้กับ **ท่อนต่อเท่านั้น** — ท่อนแรกต้องคงหัว `• ` เดิมไว้ ไม่งั้น
       บล็อก 📚 จะนับบรรทัดหัวข้อขาดไป (เคสนี้ชุดทดสอบจับได้ตอนเขียนครั้งแรก)
    """
    return (piece.count('$') % 2 == 0
            and piece.count('<b>') == piece.count('</b>')
            and (is_first or not piece.startswith('• ')))


def split_line(line):
    """คืน list ของบรรทัดหลังจัด — ถ้าตัดไม่ปลอดภัย คืนบรรทัดเดิมทั้งบรรทัด"""
    if not line.strip():
        return [line]
    for head in NEVER_SPLIT:
        if line.startswith(head):
            return [line]
    if len(line) < SPLIT_MIN:
        return [line]

    pieces = _cut(line, ARROW)
    if len(pieces) > 1 and all(_ok(p, i == 0) for i, p in enumerate(pieces)):
        line_pieces = pieces
    else:
        line_pieces = [line]

    # รอบสอง — ท่อนที่ยังยาวมาก ตัดด้วย · ต่อ
    final = []
    for p in line_pieces:
        if len(p) > MIDDOT_MIN:
            sub = _cut(p, MIDDOT)
            sub = [x.lstrip() if x.startswith('· ') else x for x in sub]
            sub = ['· ' + x if i and not x.startswith(('·', '⇒')) else x
                   for i, x in enumerate(sub)]
            if len(sub) > 1 and all(_ok(x, i == 0) for i, x in enumerate(sub)):
                final.extend(sub)
                continue
        final.append(p)
    return final


def format_explanation(expl):
    """จัดบรรทัดทั้ง list · **idempotent** (รันซ้ำได้ผลเดิม)"""
    out = []
    for line in expl:
        out.extend(split_line(line))
    return out


# ═══════════════════════════ ชุดทดสอบของตัวเอง ═══════════════════════════
def _selftest():
    ok = 0

    def check(name, cond):
        nonlocal ok
        assert cond, '🔴 ' + name
        print('  ✅ ' + name)
        ok += 1

    # ① ตัดที่ ⇒ ที่อยู่นอกสูตรจริง
    a = 'ก' * 80 + ' ⇒ ' + 'ข' * 80 + ' ⇒ ' + 'ค' * 80
    r = split_line(a)
    check('ตัดที่ ⇒ นอกสูตร ได้ 3 ท่อน และท่อนต่อขึ้นต้นด้วย ⇒',
          len(r) == 3 and r[1].startswith('⇒') and r[2].startswith('⇒'))

    # ② ⛔ ห้ามตัด ⇒ ที่อยู่ใน $...$
    b = 'ค่าของ ' + 'ก' * 130 + ' คือ $a \\Rightarrow b$ และ $x ⇒ y$ จบ'
    r = split_line(b)
    check('⇒ ที่อยู่ใน $...$ ⛔ ไม่ถูกตัด', len(r) == 1)

    # ③ ⛔ ห้ามตัดบรรทัด ✅ คำตอบ
    c = '✅ <b>คำตอบ</b> ' + 'ก' * 200 + ' ⇒ อะไรสักอย่าง → <b>ตัวเลือก 2</b>'
    r = split_line(c)
    check('บรรทัด ✅ คำตอบ ⛔ ไม่ถูกตัด (ด่านบังคับให้ลงท้ายเป๊ะ)',
          len(r) == 1 and r[0].endswith('→ <b>ตัวเลือก 2</b>'))

    # ④ ⛔ ห้ามตัดกลาง <b>...</b>
    d = 'ก' * 130 + ' <b>หัวข้อ ⇒ ที่มีลูกศรข้างใน</b> ท้ายบรรทัด'
    r = split_line(d)
    check('⇒ ที่อยู่ใน <b>...</b> ⛔ ไม่ถูกตัด',
          all(x.count('<b>') == x.count('</b>') for x in r))

    # ⑤ ท่อนต่อ ⛔ ห้ามขึ้นต้นด้วย `• ` (ไม่งั้นบล็อก 📚 นับผิด)
    e = '• ' + 'ก' * 100 + ' ⇒ ' + 'ข' * 100
    r = split_line(e)
    check('บรรทัด • ถูกตัดได้ แต่ท่อนต่อ ⛔ ไม่ขึ้นต้นด้วย •',
          len(r) == 2 and r[0].startswith('• ') and not r[1].startswith('• '))

    # ⑥ $ ต้องคู่ในทุกท่อน
    f = ('• สูตร $a^2 + b^2 = c^2$ ' + 'ก' * 100
         + ' ⇒ แทนค่า $x = \\dfrac{1}{2}$ ' + 'ข' * 60 + ' ⇒ ได้ $y = 3$')
    r = split_line(f)
    check('$ คู่กันในทุกท่อน', all(x.count('$') % 2 == 0 for x in r))

    # ⑦ บรรทัดสั้น ⛔ ไม่ตัด
    check('บรรทัดสั้นกว่า %d ⛔ ไม่ตัด' % SPLIT_MIN,
          split_line('สั้น ⇒ มาก') == ['สั้น ⇒ มาก'])

    # ⑧ idempotent — รันซ้ำได้ผลเดิม
    src = [a, b, c, d, e, f, '', '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>']
    one = format_explanation(src)
    two = format_explanation(one)
    check('idempotent (จัดซ้ำแล้วผลเดิม)', one == two)

    # ⑨ ⛔ ไม่ทำเนื้อหาหาย — ตัวอักษรที่ไม่ใช่ช่องว่างต้องเท่าเดิม
    def dense(x):
        return ''.join(''.join(x).split())
    check('⛔ ไม่มีตัวอักษรหาย/เกิน', dense(one) == dense(src))

    # ⑩ ตัดรอบสองด้วย · เมื่อท่อนยังยาวมาก
    g = 'ก' * 300 + MIDDOT + 'ข' * 300
    r = split_line(g)
    check('ท่อนที่ยาวเกิน %d ถูกตัดด้วย · ต่อ' % MIDDOT_MIN, len(r) >= 2)

    # ⑪ บรรทัดชื่อวิธี 【 】 ⛔ ไม่ถูกตัด (ทั้งบรรทัดอยู่ในแท็ก <b> เดียว)
    h = '<b>【 ' + 'ก' * 150 + ' ⇒ ' + 'ข' * 150 + ' 】</b>'
    r = split_line(h)
    check('บรรทัดชื่อวิธี 【 】 ⛔ ไม่ถูกตัด (กันแท็ก <b> ค้าง)',
          len(r) == 1 and r[0].count('<b>') == r[0].count('</b>') == 1)

    # ⑫ ท่อนต่อทุกท่อนต้องขึ้นต้นด้วยตัวเชื่อม ⇒ หรือ · (อ่านแล้วรู้ว่าต่อจากบรรทัดบน)
    r = split_line('• ' + 'ก' * 90 + ' ⇒ ' + 'ข' * 90 + ' ⇒ ' + 'ค' * 90)
    check('ท่อนต่อทุกท่อนขึ้นต้นด้วยตัวเชื่อม',
          len(r) >= 3 and all(x.startswith(('⇒', '·')) for x in r[1:]))

    print('=' * 62)
    print('linebreak v%s · selftest ผ่าน %d เคส' % (__version__, ok))


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        _selftest()
    else:
        print(__doc__)

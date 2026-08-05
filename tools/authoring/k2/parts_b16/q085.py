# -*- coding: utf-8 -*-
add(
    85,
    ['7.8'],
    'ง่าย',
    'กำหนดให้ $f(x) = 3\\arccos x - \\dfrac{\\pi}{2}$ '
    'สำหรับทุกจำนวนจริง $x$ ที่ทำให้ $f$ หาค่าได้ เรนจ์ของ $f$ คือข้อใด',
    [
        '$\\left[-2\\pi,\\ \\pi\\right]$',
        '$\\left[-\\dfrac{\\pi}{2},\\ \\dfrac{\\pi}{2}\\right]$',
        '$\\left[-\\dfrac{\\pi}{2},\\ \\dfrac{5\\pi}{2}\\right]$',
        '$\\left[0,\\ \\pi\\right]$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• $\\arccos x$ อ่านว่า “มุมที่มีโคไซน์เท่ากับ $x$” โดยตกลงกันว่าต้องเลือกมุมที่อยู่ในช่วง '
        '$[0,\\ \\pi]$ เท่านั้น ช่วงนี้เรียกว่าช่วงค่าหลัก และมีไว้เพื่อให้แต่ละค่าของ $x$ '
        'ให้มุมออกมาเพียงมุมเดียว',
        '• โดเมนของ $\\arccos$ คือ $[-1,\\ 1]$ เพราะโคไซน์ของมุมใด ๆ ไม่มีทางออกนอกช่วงนี้',
        '• $\\arccos$ เป็นฟังก์ชันต่อเนื่องและ<b>ลด</b> คือเมื่อ $x$ ไล่จาก $-1$ ขึ้นไปถึง $1$ '
        'ค่า $\\arccos x$ จะไล่จาก $\\pi$ ลงมาถึง $0$ อย่างต่อเนื่อง '
        'จึงรับค่าได้<b>ครบทุกค่า</b>ในช่วง $[0,\\ \\pi$] ไม่ใช่แค่ค่าปลาย',
        '• การแปลงช่วงด้วยฟังก์ชันเชิงเส้น : ถ้า $a \\le u \\le b$ แล้ว',
        '  คูณด้วยจำนวน<b>บวก</b> $m$ ตลอดอสมการ เครื่องหมายไม่กลับด้าน ได้ $ma \\le mu \\le mb$',
        '  และบวกหรือลบค่าคงตัวเท่ากันทุกข้าง ช่วงจะเลื่อนไปทั้งช่วงโดยไม่กลับด้านเช่นกัน',
        '• ช่วงค่าหลักที่มักถูกหยิบสลับกันคือของ $\\arcsin$ ซึ่งเป็น '
        '$\\left[-\\dfrac{\\pi}{2},\\ \\dfrac{\\pi}{2}\\right]$ '
        '⛔ คนละช่วงกับของ $\\arccos$ อย่างสิ้นเชิง',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $f(x) = 3\\arccos x - \\dfrac{\\pi}{2}$',
        '• $x$ เป็นจำนวนจริงใดก็ได้ที่ทำให้ $f$ หาค่าได้ นั่นคือ $-1 \\le x \\le 1$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาเรนจ์ของ $f$ นั่นคือเซตของค่าทั้งหมดที่ $f(x)$ เป็นไปได้',
        '',
        '<b>【 เขียนช่วงของก้อนในให้จบก่อน แล้วค่อยแปลงช่วงตามการคูณและการลบทีละขั้น 】</b>',
        '',
        '<b>ขั้นที่ 1 · เขียนช่วงของก้อนในสุด</b>',
        '• ตั้งชื่อก้อนในว่า $u = \\arccos x$ เพื่อไม่ให้สับสนกับตัวแปร $x$ เดิม',
        '• ตามข้อตกลงช่วงค่าหลักของอาร์กโคไซน์ จะได้ $0 \\le u \\le \\pi$ ทันที',
        '• และเพราะ $\\arccos$ ต่อเนื่องและลดจาก $\\pi$ ไปถึง $0$ บนโดเมน $[-1,\\ 1]$ '
        'ค่า $u$ จึงวิ่งได้<b>ครบทุกค่า</b>ในช่วง $[0,\\ \\pi]$ ไม่ได้กระโดดข้ามค่าใดเลย '
        'ข้อเท็จจริงนี้สำคัญ เพราะทำให้คำตอบสุดท้ายเป็นช่วงปิดเต็มช่วง ไม่ใช่แค่สองจุดปลาย',
        '',
        '<b>ขั้นที่ 2 · คูณตลอดด้วย $3$</b>',
        '• เริ่มจาก $0 \\le u \\le \\pi$',
        '• คูณตลอดด้วย $3$ ซึ่งเป็นจำนวนบวก เครื่องหมายอสมการจึง<b>ไม่กลับด้าน</b> '
        'ได้ $0 \\le 3u \\le 3\\pi$',
        '',
        '<b>ขั้นที่ 3 · ลบ $\\dfrac{\\pi}{2}$ ตลอด แล้วสรุปเป็นเรนจ์</b>',
        '• ลบ $\\dfrac{\\pi}{2}$ ทุกข้างของอสมการ ได้ '
        '$0 - \\dfrac{\\pi}{2} \\le 3u - \\dfrac{\\pi}{2} \\le 3\\pi - \\dfrac{\\pi}{2}$',
        '• คิดปลายขวา : $3\\pi - \\dfrac{\\pi}{2} = \\dfrac{6\\pi}{2} - \\dfrac{\\pi}{2} '
        '= \\dfrac{5\\pi}{2}$',
        '• เพราะ $f(x) = 3u - \\dfrac{\\pi}{2}$ พอดี จึงได้ '
        '$-\\dfrac{\\pi}{2} \\le f(x) \\le \\dfrac{5\\pi}{2}$',
        '• ตรวจว่าปลายทั้งสองเกิดขึ้นได้จริง ไม่ใช่แค่ขอบเขต : '
        'ที่ $x = 1$ ได้ $u = 0$ จึง $f(1) = -\\dfrac{\\pi}{2}$ '
        'และที่ $x = -1$ ได้ $u = \\pi$ จึง $f(-1) = 3\\pi - \\dfrac{\\pi}{2} = \\dfrac{5\\pi}{2}$',
        '• ดังนั้นเรนจ์ของ $f$ คือ $\\left[-\\dfrac{\\pi}{2},\\ \\dfrac{5\\pi}{2}\\right]$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไม่แปลงช่วงเลย แต่ตั้งสมการ $f(x) = k$ '
        'แล้วถามย้อนว่า $k$ ค่าใดบ้างที่หา $x$ ได้จริง)</b>',
        '• ให้ $f(x) = k$ นั่นคือ $3\\arccos x - \\dfrac{\\pi}{2} = k$ '
        'จัดรูปได้ $\\arccos x = \\dfrac{k + \\dfrac{\\pi}{2}}{3}$',
        '• สมการ $\\arccos x = \\theta$ จะมีคำตอบ $x$ ได้ก็ต่อเมื่อ $\\theta$ อยู่ในช่วงค่าหลัก '
        'คือ $0 \\le \\theta \\le \\pi$ และเมื่อนั้นคำตอบคือ $x = \\cos\\theta$ ซึ่งอยู่ใน '
        '$[-1,\\ 1]$ เสมอ',
        '• แทน $\\theta = \\dfrac{k + \\dfrac{\\pi}{2}}{3}$ ลงในเงื่อนไข จะได้ '
        '$0 \\le \\dfrac{k + \\dfrac{\\pi}{2}}{3} \\le \\pi$',
        '• คูณตลอดด้วย $3$ ได้ $0 \\le k + \\dfrac{\\pi}{2} \\le 3\\pi$ '
        'แล้วลบ $\\dfrac{\\pi}{2}$ ตลอด ได้ '
        '$-\\dfrac{\\pi}{2} \\le k \\le \\dfrac{5\\pi}{2}$',
        '• ได้ช่วงของ $k$ ตรงกับเรนจ์ที่คำนวณไว้ทุกประการ และวิธีนี้ยังยืนยันเพิ่มว่า '
        '$k$ <b>ทุกค่า</b>ในช่วงนั้นใช้ได้จริง เพราะสร้าง $x = \\cos\\theta$ กลับมาได้เสมอ',
        '• ลองค่ากลางเพื่อความมั่นใจ : $x = 0$ ให้ $u = \\dfrac{\\pi}{2}$ จึง '
        '$f(0) = \\dfrac{3\\pi}{2} - \\dfrac{\\pi}{2} = \\pi$ ซึ่งอยู่ระหว่าง '
        '$-\\dfrac{\\pi}{2}$ กับ $\\dfrac{5\\pi}{2}$ จริง',
        '',
        '✅ <b>คำตอบ</b> เรนจ์ของ $f$ คือ '
        '$\\left[-\\dfrac{\\pi}{2},\\ \\dfrac{5\\pi}{2}\\right]$ → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• โจทย์หาเรนจ์ของฟังก์ชันที่ห่อฟังก์ชันผกผันไว้ข้างใน ให้ทำแบบ “ไล่จากในออกนอก” เสมอ '
        'คือเขียนช่วงของก้อนในสุดก่อน แล้วค่อยเดินตามการดำเนินการทีละตัวจนถึงผิวนอก '
        'วิธีนี้ทำให้ไม่มีขั้นไหนถูกข้าม',
        '• ให้ท่องคู่ช่วงค่าหลักติดตัวไว้ : $\\arccos$ ได้ $[0,\\ \\pi]$ '
        'ส่วน $\\arcsin$ และ $\\arctan$ อยู่รอบศูนย์ '
        'คือ $\\left[-\\dfrac{\\pi}{2},\\ \\dfrac{\\pi}{2}\\right]$ '
        'เหตุผลที่ $\\arccos$ ต่างพวก เพราะโคไซน์เป็นฟังก์ชันคู่ '
        'ถ้าเลือกช่วงรอบศูนย์จะได้สองมุมที่ให้โคไซน์เท่ากัน ทำให้ไม่เป็นฟังก์ชัน',
        '• เมื่อคูณอสมการ ให้ดูเครื่องหมายของตัวคูณทุกครั้ง ตัวคูณบวกไม่กลับด้าน '
        'ตัวคูณลบกลับด้าน ข้อนี้ตัวคูณเป็น $3$ จึงปลอดภัย '
        'แต่ถ้าโจทย์เปลี่ยนเป็น $-3$ ปลายซ้ายกับปลายขวาจะสลับที่กันทันที',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $\\left[-2\\pi,\\ \\pi\\right]$ เพราะหยิบช่วงค่าหลักผิดฟังก์ชัน '
        'คือใช้ $-\\dfrac{\\pi}{2} \\le u \\le \\dfrac{\\pi}{2}$ ซึ่งเป็นของ $\\arcsin$ '
        'แล้วแปลงต่อได้ $-2\\pi \\le f \\le \\pi$ '
        'วิธีกันคือถามกลับว่า “ค่าที่ตอบเป็นมุมที่มีโคไซน์เท่ากับอะไร” '
        'ถ้าเป็นอาร์กโคไซน์ มุมต้องไม่มีทางติดลบเลย',
        '• ได้ $\\left[-\\dfrac{\\pi}{2},\\ \\dfrac{\\pi}{2}\\right]$ เพราะลืมคูณ $3$ '
        'คือเลื่อนช่วง $[0,\\ \\pi]$ ลงมา $\\dfrac{\\pi}{2}$ อย่างเดียว '
        'ให้สังเกตว่าความยาวของช่วงคำตอบต้องเป็น $3$ เท่าของความยาวช่วงเดิมเสมอ '
        'ช่วงเดิมยาว $\\pi$ คำตอบจึงต้องยาว $3\\pi$ ไม่ใช่ $\\pi$',
        '• ได้ $\\left[0,\\ \\pi\\right]$ เพราะตอบช่วงค่าหลักของ $\\arccos$ ออกไปเลย '
        'โดยไม่ได้แปลงตามสูตรที่โจทย์ให้ '
        'เป็นการตอบเรนจ์ของ<b>ก้อนใน</b>แทนเรนจ์ของ<b>ทั้งฟังก์ชัน</b> '
        'ให้เช็คด้วยการแทนค่าจริงหนึ่งค่า เช่น $x = 1$ ได้ $f(1) = -\\dfrac{\\pi}{2}$ '
        'ซึ่งติดลบ จึงเป็นไปไม่ได้ที่เรนจ์จะเริ่มที่ $0$',
    ],
    'V.mold: G = a single inverse-cosine expression wrapped in an affine map with a positive coefficient / '
    'A = the range of the whole function as a closed interval / M = write the principal range of the inner '
    'arccos, then push that interval through multiplication by a positive constant and a constant shift. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 with total at most 2, T = 0 and C = 0 -> level: ง่าย. '
    'One deliberate design decision keeps this honestly easy: the coefficient is positive (3), so the '
    'inequality never flips. A negative coefficient would turn the flip into a genuine turning point, '
    'scoring T = 1 and pushing the item to ปานกลาง; the batch needed one easy item, so the positive '
    'coefficient was chosen at design time rather than by lowering a score afterwards. '
    'Subtopic 7.8 is the thinnest in the authored corpus at 5 items out of 84, so this slot fills a real '
    'coverage gap. '
    'sympy (verify_b16.py): f(1) evaluates to -pi/2 and f(-1) to 5*pi/2; an independent numeric sweep of '
    'f over 801 sample points of [-1, 1] returns exactly those two as the minimum and maximum, and f(0) '
    'returns pi confirming interior values are attained. All three distractors machine-computed from named '
    'error paths: [-2*pi, pi] from substituting the arcsin principal range, [-pi/2, pi/2] from dropping the '
    'factor 3, and [0, pi] from reporting the inner principal range untransformed. '
    'Collision sweep on 6397 items (bank 62 files + k1 out + k2 out), probe collide_b16.py round 1: no '
    'chapter-7 item asks for a range of an inverse-trig expression at all; the 34 items containing arccos '
    'and the 23 items with a coefficient in front of an inverse-trig function are all value-of-expression '
    'molds. The saturated inverse-trig molds in the corpus are nested arc evaluation at 19 items, arctan '
    'sums at 14 items, and the arcsin-plus-arccos equation family; this item is none of those. Nearest '
    'authored relatives are q052 (domain of arcsin of a quadratic) and q067 (counting integers that keep an '
    'arccos argument legal): both ask about the input side, this one asks about the output side.',
)

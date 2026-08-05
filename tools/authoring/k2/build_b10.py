# -*- coding: utf-8 -*-
"""ก้อน 10 · 7.5 ผลบวก-ผลต่างมุม + 7.6 มุมสองเท่า-ครึ่งมุม + 7.7 สมการตรีโกณ · 5 ข้อ (q055-q059)

ระดับมาจาก grade_b10.py (คิดคะแนน rubric ก่อน ไม่ใช่เลือกระดับแล้วย้อนหาคะแนน):
  q055 ปานกลาง 6 · q056 ปานกลาง 5 · q057 ปานกลาง 5 · q058 ปานกลาง 3 · q059 ยากมาก 12
ช่องคำตอบ: 4, 2, 1, 3, 2 (สะสมเป็น 14/15/16/14 จาก 59 ข้อ)
sympy: verify_b10.py 73/73 ผ่าน
แม่พิมพ์: molds.py --test ❌ 0 คู่ · ไม่มีคู่ WATCH ใหม่
"""
import json, io, os, collections
OUT = '/home/claude/k2/out'
os.makedirs(OUT, exist_ok=True)
SRC = 'แต่งใหม่ v2 · แข่งขัน · 2569'
SET = 'gen-chap-07-trigonometry'
Q = []


def add(n, st, level, stem, choices, correct, expl, notes):
    Q.append(collections.OrderedDict([
        ('id', '%s-q%03d' % (SET, n)), ('setId', SET), ('questionNumber', n),
        ('topics', ['7']), ('subTopics', st), ('difficulty', level),
        ('type', 'mc'), ('question', stem), ('choices', choices),
        ('hasImage', False), ('sourceTag', SRC), ('correct', correct),
        ('explanation', expl), ('notes', notes),
    ]))
    print('q%03d ok' % n)
# ══════════════════════════════════════════════════════════════════ q055
add(55, ['7.6', '7.5'], 'ปานกลาง',
    'กำหนดให้ $a$ และ $b$ เป็นจำนวนจริงซึ่งทำให้ '
    '$\\sin^4 x + \\cos^4 x = a + b\\cos 4x$ '
    'เป็นจริงสำหรับทุกจำนวนจริง $x$ แล้ว $\\dfrac{a}{b}$ เท่ากับข้อใด',
    ['$-3$', '$\\dfrac{1}{3}$', '$1$', '$3$'], 3,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เอกลักษณ์หลัก $\\sin^2 x + \\cos^2 x = 1$ ซึ่งเป็นจริงทุกจำนวนจริง $x$',
        '• เอกลักษณ์พีชคณิต $A^2 + B^2 = (A+B)^2 - 2AB$ '
        'ใช้ยุบผลบวกของกำลังสองให้เหลือของที่รู้ค่าแล้ว',
        '• สูตรมุมสองเท่า $\\sin 2\\theta = 2\\sin\\theta\\cos\\theta$ '
        '⇒ ยกกำลังสองทั้งสองข้างได้ $\\sin^2 2\\theta = 4\\sin^2\\theta\\cos^2\\theta$ '
        '(⛔ สังเกตเลข $4$ ให้ดี เพราะเป็นจุดที่หลุดกันบ่อยที่สุด)',
        '• สูตรลดกำลัง $\\sin^2\\theta = \\dfrac{1 - \\cos 2\\theta}{2}$ '
        'ใช้กับมุม $2x$ จะได้ $\\sin^2 2x = \\dfrac{1 - \\cos 4x}{2}$',
        '• ถ้าสมการ $P + Q\\cos 4x = a + b\\cos 4x$ เป็นจริง<b>ทุก</b>ค่า $x$ '
        'แล้วต้องได้ $a = P$ และ $b = Q$ '
        '(เทียบสัมประสิทธิ์ได้ เพราะ $\\cos 4x$ ไม่ใช่ค่าคงตัว)',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• นิพจน์ฝั่งซ้ายคือ $\\sin^4 x + \\cos^4 x$ ซึ่งเป็นกำลังสี่ของฟังก์ชันตรีโกณ',
        '• ฝั่งขวาคือ $a + b\\cos 4x$ ซึ่งเป็นมุม $4x$ ไม่ใช่มุม $x$',
        '• เงื่อนไข “เป็นจริงสำหรับทุกจำนวนจริง $x$” คือใบอนุญาตให้เทียบสัมประสิทธิ์',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่า $a$ และ $b$ ที่ทำให้สองฝั่งเท่ากันทุก $x$ แล้วตอบอัตราส่วน $\\dfrac{a}{b}$',
        '',
        '<b>【 ยุบกำลังสี่ด้วยเอกลักษณ์ผลบวกกำลังสอง แล้วไต่มุมขึ้นทีละเท่า '
        'จากมุม $x$ ไปมุม $2x$ ด้วยสูตรมุมสองเท่า และจากมุม $2x$ ไปมุม $4x$ '
        'ด้วยสูตรลดกำลัง 】</b>',
        '',
        '<b>ขั้นที่ 1 · ยุบกำลังสี่ให้เหลือกำลังสอง</b>',
        '• มอง $A = \\sin^2 x$ และ $B = \\cos^2 x$ '
        'จะได้ $\\sin^4 x + \\cos^4 x = A^2 + B^2$',
        '• ใช้ $A^2 + B^2 = (A+B)^2 - 2AB$ ได้ '
        '$\\sin^4 x + \\cos^4 x = \\left(\\sin^2 x + \\cos^2 x\\right)^2 '
        '- 2\\sin^2 x\\cos^2 x$',
        '• แทน $\\sin^2 x + \\cos^2 x = 1$ ได้ '
        '$\\sin^4 x + \\cos^4 x = 1 - 2\\sin^2 x\\cos^2 x$',
        '',
        '<b>ขั้นที่ 2 · ไต่จากมุม $x$ ขึ้นเป็นมุม $2x$</b>',
        '• จาก $\\sin 2x = 2\\sin x\\cos x$ ยกกำลังสองทั้งสองข้าง '
        'ได้ $\\sin^2 2x = 4\\sin^2 x\\cos^2 x$',
        '• จัดรูปเพื่อดึงสิ่งที่ต้องการ ได้ '
        '$\\sin^2 x\\cos^2 x = \\dfrac{\\sin^2 2x}{4}$',
        '• แทนกลับ ได้ $1 - 2 \\cdot \\dfrac{\\sin^2 2x}{4} '
        '= 1 - \\dfrac{1}{2}\\sin^2 2x$',
        '',
        '<b>ขั้นที่ 3 · ไต่จากมุม $2x$ ขึ้นเป็นมุม $4x$ ด้วยสูตรลดกำลัง</b>',
        '• สูตรลดกำลังกับมุม $2x$ ให้ $\\sin^2 2x = \\dfrac{1 - \\cos 4x}{2}$',
        '• แทนลงไป ได้ $1 - \\dfrac{1}{2} \\cdot \\dfrac{1 - \\cos 4x}{2} '
        '= 1 - \\dfrac{1 - \\cos 4x}{4}$',
        '• กระจายและรวมพจน์ ได้ '
        '$1 - \\dfrac{1}{4} + \\dfrac{1}{4}\\cos 4x = \\dfrac{3}{4} '
        '+ \\dfrac{1}{4}\\cos 4x$',
        '',
        '<b>ขั้นที่ 4 · เทียบสัมประสิทธิ์แล้วหาอัตราส่วน</b>',
        '• ได้ $\\dfrac{3}{4} + \\dfrac{1}{4}\\cos 4x = a + b\\cos 4x$ '
        'เป็นจริงทุก $x$',
        '• เทียบพจน์คงตัว ได้ $a = \\dfrac{3}{4}$ '
        '· เทียบพจน์หน้า $\\cos 4x$ ได้ $b = \\dfrac{1}{4}$',
        '• ดังนั้น $\\dfrac{a}{b} = \\dfrac{3/4}{1/4} = 3$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่า $x$ สองค่าแล้วแก้ระบบสมการสองตัวแปร)</b>',
        '• เงื่อนไข “จริงทุก $x$” แปลว่าแทน $x$ ค่าไหนก็ต้องเป็นจริง '
        '⇒ เลือกค่าที่คำนวณง่ายสองค่ามาตั้งเป็นระบบสมการ',
        '• แทน $x = 0$ ฝั่งซ้ายได้ $0 + 1 = 1$ '
        'ฝั่งขวาได้ $a + b\\cos 0 = a + b$ ⇒ สมการที่หนึ่ง $a + b = 1$',
        '• แทน $x = \\dfrac{\\pi}{4}$ ฝั่งซ้ายได้ '
        '$\\left(\\dfrac{\\sqrt{2}}{2}\\right)^4 + \\left(\\dfrac{\\sqrt{2}}{2}\\right)^4 '
        '= \\dfrac{1}{4} + \\dfrac{1}{4} = \\dfrac{1}{2}$ '
        'ฝั่งขวาได้ $a + b\\cos\\pi = a - b$ ⇒ สมการที่สอง $a - b = \\dfrac{1}{2}$',
        '• บวกสองสมการได้ $2a = \\dfrac{3}{2}$ ⇒ $a = \\dfrac{3}{4}$ '
        'แล้วลบกันได้ $2b = \\dfrac{1}{2}$ ⇒ $b = \\dfrac{1}{4}$',
        '• อัตราส่วน $\\dfrac{a}{b} = 3$ ตรงกับวิธีแรก '
        'และค่าที่ได้ยังผ่านการสุ่มตรวจที่ $x$ ค่าอื่นด้วย',
        '',
        '✅ <b>คำตอบ</b> $\\dfrac{a}{b} = 3$ → <b>ตัวเลือก 4</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอกำลังสี่ของ $\\sin$ กับ $\\cos$ บวกกัน ให้นึกถึง '
        '$A^2 + B^2 = (A+B)^2 - 2AB$ ทันที เพราะ $A+B$ ยุบเป็น $1$ ได้ฟรี ๆ '
        'เหลือแค่จัดการพจน์ $2AB$ พจน์เดียว',
        '• เวลาโจทย์ฝั่งขวาเป็นมุม $4x$ แต่ฝั่งซ้ายเป็นมุม $x$ '
        'ให้คิดเป็นการ<b>ไต่มุมทีละเท่า</b> คือ $x \\to 2x \\to 4x$ '
        'อย่ากระโดดหาสูตรมุมสี่เท่าโดยตรง ซึ่งจำยากและพลาดง่าย',
        '• เงื่อนไข “จริงทุก $x$” มีค่ามาก เพราะเปิดทางให้ทำได้สองแบบ '
        'คือเทียบสัมประสิทธิ์ หรือแทนค่าง่าย ๆ หลายค่าแล้วแก้ระบบ '
        'ใช้แบบหนึ่งทำ อีกแบบตรวจ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• $1$ — เขียน $2\\sin^2 x\\cos^2 x = \\sin^2 2x$ โดยลืมเลข $4$ '
        'ในสูตร $\\sin^2 2x = 4\\sin^2 x\\cos^2 x$ '
        'จึงได้ $1 - \\sin^2 2x = \\dfrac{1}{2} + \\dfrac{1}{2}\\cos 4x$ '
        'แล้วได้ $a = b = \\dfrac{1}{2}$ ⇒ อัตราส่วนเป็น $1$ '
        'นี่คือจุดพลาดหลักของข้อนี้',
        '• $-3$ — จำสูตรลดกำลังสลับเครื่องหมายเป็น '
        '$\\sin^2 2x = \\dfrac{1 + \\cos 4x}{2}$ '
        '(ซึ่งเป็นสูตรของ $\\cos^2 2x$) จึงได้ '
        '$\\dfrac{3}{4} - \\dfrac{1}{4}\\cos 4x$ ⇒ $b = -\\dfrac{1}{4}$ '
        'และอัตราส่วนติดลบ',
        '• $\\dfrac{1}{3}$ — หา $a$ กับ $b$ ได้ถูกทั้งคู่ '
        'แต่ตอบเป็น $\\dfrac{b}{a}$ กลับหัวจากที่โจทย์ถาม',
    ],
    'V.mold: G = a FOURTH-POWER trig expression declared equal to an unknown-coefficient form '
    'a + b cos 4x for every real x / A = the RATIO a/b, not the coefficients themselves / '
    'M = collapse the sum of squares with (A+B)^2 - 2AB, then climb the angle one doubling at a '
    'time (x -> 2x via the double-angle square, 2x -> 4x via power reduction) and match '
    'coefficients. Rubric F2 C0 P2 T2 L0 = 6 -> ปานกลาง (one key: seeing that the fourth powers '
    'collapse through (sin^2+cos^2)^2; after that every step is a named formula, and there is no '
    'case split). sympy: verified sin^4 x + cos^4 x - (3/4 + cos(4x)/4) collapses symbolically '
    'and numerically at 60 digits for random x, plus the two-point linear system a+b=1, '
    'a-b=1/2 solved independently. Traps: 1 comes from dropping the factor 4 in '
    'sin^2 2x = 4 sin^2 x cos^2 x, -3 comes from flipping the sign in the power-reduction '
    'formula, 1/3 is the reciprocal. Collision sweep on 6367 items: no bank item asks for the '
    'coefficients of a cos-4x expansion of sin^4 + cos^4; the items containing sin^4/cos^4 all '
    'ask for a numeric value at a specific angle, and the true-for-all-x items in the bank sit '
    'in the polynomial and logarithm chapters.')
# ══════════════════════════════════════════════════════════════════ q056
add(56, ['7.6'], 'ปานกลาง',
    'กำหนดให้ $\\theta$ เป็นจำนวนจริงซึ่ง $\\pi < \\theta < \\dfrac{3\\pi}{2}$ '
    'และ $\\tan\\dfrac{\\theta}{2} + \\cot\\dfrac{\\theta}{2} = -\\dfrac{25}{12}$ '
    'แล้ว $\\cos\\theta$ เท่ากับข้อใด',
    ['$-\\dfrac{24}{25}$', '$-\\dfrac{7}{25}$', '$\\dfrac{7}{25}$',
     '$\\dfrac{24}{25}$'], 1,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• นิยาม $\\tan u = \\dfrac{\\sin u}{\\cos u}$ และ $\\cot u = \\dfrac{\\cos u}{\\sin u}$',
        '• เอกลักษณ์หลัก $\\sin^2 u + \\cos^2 u = 1$',
        '• สูตรมุมสองเท่า $\\sin 2u = 2\\sin u\\cos u$ '
        '⇒ อ่านกลับได้ว่า $\\sin u\\cos u = \\dfrac{\\sin 2u}{2}$',
        '• จตุภาคที่ $3$ คือช่วง $\\pi < \\theta < \\dfrac{3\\pi}{2}$ '
        'ซึ่ง $\\sin\\theta < 0$ และ $\\cos\\theta < 0$ ทั้งคู่',
        '• การหารช่วงด้วยสอง ถ้า $\\pi < \\theta < \\dfrac{3\\pi}{2}$ '
        'แล้ว $\\dfrac{\\pi}{2} < \\dfrac{\\theta}{2} < \\dfrac{3\\pi}{4}$ '
        '⇒ ครึ่งมุมตกอยู่ในจตุภาคที่ $2$ ไม่ใช่จตุภาคที่ $3$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• ค่าที่ให้มาเป็นค่าของ<b>ครึ่งมุม</b> คือ '
        '$\\tan\\dfrac{\\theta}{2} + \\cot\\dfrac{\\theta}{2} = -\\dfrac{25}{12}$',
        '• ช่วงที่ให้มาเป็นช่วงของ<b>มุมเต็ม</b> คือ '
        '$\\pi < \\theta < \\dfrac{3\\pi}{2}$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่า $\\cos\\theta$ ซึ่งเป็นค่าของมุมเต็ม '
        '⇒ ต้องเดินจากครึ่งมุมกลับขึ้นไปหามุมเต็ม',
        '',
        '<b>【 ยุบผลบวก $\\tan + \\cot$ ให้เป็นเศษส่วนเดียวด้วยเอกลักษณ์หลัก '
        'แล้วใช้สูตรมุมสองเท่าดันครึ่งมุมกลับขึ้นเป็นมุมเต็มทันที '
        'จบด้วยการเลือกเครื่องหมายจากจตุภาคของมุมเต็ม 】</b>',
        '',
        '<b>ขั้นที่ 1 · ยุบผลบวกให้เป็นเศษส่วนเดียว</b>',
        '• ให้ $u = \\dfrac{\\theta}{2}$ เพื่อเขียนสั้นลง',
        '• เขียนตามนิยาม ได้ '
        '$\\tan u + \\cot u = \\dfrac{\\sin u}{\\cos u} + \\dfrac{\\cos u}{\\sin u}$',
        '• ทำส่วนร่วม ได้ '
        '$\\dfrac{\\sin^2 u + \\cos^2 u}{\\sin u\\cos u}$',
        '• เศษยุบด้วยเอกลักษณ์หลักเป็น $1$ ⇒ '
        '$\\tan u + \\cot u = \\dfrac{1}{\\sin u\\cos u}$',
        '',
        '<b>ขั้นที่ 2 · ดันครึ่งมุมกลับขึ้นเป็นมุมเต็ม</b>',
        '• จาก $\\sin 2u = 2\\sin u\\cos u$ ได้ '
        '$\\sin u\\cos u = \\dfrac{\\sin 2u}{2}$',
        '• แทนลงไป ได้ '
        '$\\tan u + \\cot u = \\dfrac{1}{\\sin 2u / 2} = \\dfrac{2}{\\sin 2u}$',
        '• เนื่องจาก $u = \\dfrac{\\theta}{2}$ จึงได้ $2u = \\theta$ พอดี ⇒ '
        '$\\tan\\dfrac{\\theta}{2} + \\cot\\dfrac{\\theta}{2} = \\dfrac{2}{\\sin\\theta}$',
        '',
        '<b>ขั้นที่ 3 · แก้หาค่า $\\sin\\theta$</b>',
        '• แทนค่าที่โจทย์ให้ ได้ $\\dfrac{2}{\\sin\\theta} = -\\dfrac{25}{12}$',
        '• คูณไขว้ ได้ $-25\\sin\\theta = 24$ ⇒ $\\sin\\theta = -\\dfrac{24}{25}$',
        '• ตรวจความสมเหตุสมผลก่อนไปต่อ ค่าที่ได้ติดลบ '
        'ซึ่งสอดคล้องกับจตุภาคที่ $3$ ที่โจทย์กำหนด',
        '',
        '<b>ขั้นที่ 4 · หาค่า $\\cos\\theta$ แล้วเลือกเครื่องหมายจากจตุภาค</b>',
        '• จากเอกลักษณ์หลัก $\\cos^2\\theta = 1 - \\sin^2\\theta '
        '= 1 - \\dfrac{576}{625} = \\dfrac{49}{625}$',
        '• ถอดรากได้สองความเป็นไปได้ คือ $\\cos\\theta = \\dfrac{7}{25}$ '
        'หรือ $\\cos\\theta = -\\dfrac{7}{25}$',
        '• ช่วง $\\pi < \\theta < \\dfrac{3\\pi}{2}$ คือจตุภาคที่ $3$ '
        'ซึ่ง $\\cos\\theta < 0$ ⇒ ตัดค่าบวกทิ้ง',
        '• ดังนั้น $\\cos\\theta = -\\dfrac{7}{25}$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · เดินย้อนด้วยสูตร '
        '$\\tan\\dfrac{\\theta}{2} = \\dfrac{\\sin\\theta}{1 + \\cos\\theta}$)</b>',
        '• สมมติคำตอบถูก คือ $\\sin\\theta = -\\dfrac{24}{25}$ '
        'และ $\\cos\\theta = -\\dfrac{7}{25}$ แล้วเดินย้อนกลับไปหาค่าครึ่งมุม',
        '• ใช้สูตร $\\tan\\dfrac{\\theta}{2} = \\dfrac{\\sin\\theta}{1 + \\cos\\theta}$ '
        'ได้ $\\dfrac{-24/25}{1 - 7/25} = \\dfrac{-24/25}{18/25} = -\\dfrac{4}{3}$',
        '• จากนั้น $\\cot\\dfrac{\\theta}{2} = -\\dfrac{3}{4}$ '
        '⇒ ผลบวก $-\\dfrac{4}{3} - \\dfrac{3}{4} = -\\dfrac{16}{12} - \\dfrac{9}{12} '
        '= -\\dfrac{25}{12}$ ตรงกับที่โจทย์ให้พอดี',
        '• ตรวจจตุภาคของครึ่งมุมด้วย จาก $\\pi < \\theta < \\dfrac{3\\pi}{2}$ '
        'ได้ $\\dfrac{\\pi}{2} < \\dfrac{\\theta}{2} < \\dfrac{3\\pi}{4}$ '
        'ซึ่งเป็นจตุภาคที่ $2$ ⇒ แทนเจนต์ของครึ่งมุมต้องติดลบ '
        'สอดคล้องกับ $-\\dfrac{4}{3}$ ที่คำนวณได้',
        '• ถ้าลองใช้ค่าบวก $\\cos\\theta = \\dfrac{7}{25}$ แทน จะได้ '
        '$\\tan\\dfrac{\\theta}{2} = \\dfrac{-24/25}{32/25} = -\\dfrac{3}{4}$ '
        'และผลบวกกลายเป็น $-\\dfrac{25}{12}$ เท่ากันด้วย '
        '⇒ ยืนยันว่าค่าที่โจทย์ให้<b>ไม่พอ</b>ตัดสินเครื่องหมาย '
        'ต้องใช้ช่วงของ $\\theta$ เท่านั้น',
        '',
        '✅ <b>คำตอบ</b> $\\cos\\theta = -\\dfrac{7}{25}$ → <b>ตัวเลือก 2</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอ $\\tan u + \\cot u$ อย่าเพิ่งตั้งสมการกำลังสอง '
        'ให้จำไว้เลยว่ามันยุบเป็น $\\dfrac{1}{\\sin u\\cos u} = \\dfrac{2}{\\sin 2u}$ '
        'ซึ่งเปลี่ยนโจทย์ครึ่งมุมให้กลายเป็นโจทย์มุมเต็มทันทีในบรรทัดเดียว',
        '• โจทย์ที่ให้ช่วงของมุมมาเสมอ แปลว่าจะต้องมีจังหวะถอดรากที่ได้สองเครื่องหมาย '
        'อ่านช่วงตั้งแต่แรกแล้วจดไว้ว่าจตุภาคไหน อะไรบวกอะไรลบ',
        '• ระวังว่าครึ่งมุมกับมุมเต็ม<b>อยู่คนละจตุภาค</b>ได้ '
        'ในข้อนี้มุมเต็มอยู่จตุภาคที่ $3$ แต่ครึ่งมุมอยู่จตุภาคที่ $2$',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• $\\dfrac{7}{25}$ — ถอดรากจาก $\\cos^2\\theta = \\dfrac{49}{625}$ '
        'แล้วหยิบค่าบวกโดยไม่อ่านช่วงที่โจทย์ให้ '
        'นี่คือจุดพลาดหลักของข้อนี้ และเป็นเหตุผลที่โจทย์วางช่วงไว้ในจตุภาคที่ $3$',
        '• $-\\dfrac{24}{25}$ — หยุดที่ค่ากลางทาง คือตอบ $\\sin\\theta$ '
        'ที่ได้จากขั้นที่ $3$ แทนที่จะเดินต่อไปหา $\\cos\\theta$ ตามที่โจทย์ถาม',
        '• $\\dfrac{24}{25}$ — ตอบค่ากลางทางเหมือนกรณีข้างต้น '
        'แต่ยังทำเครื่องหมายหายไปด้วยจากการคูณไขว้ '
        '$\\dfrac{2}{\\sin\\theta} = -\\dfrac{25}{12}$',
    ],
    'V.mold: G = the VALUE of a half-angle expression tan(t/2) + cot(t/2) plus the quadrant of '
    'the FULL angle / A = cos of the full angle / M = collapse tan + cot into 1/(sin u cos u), '
    'then push the half angle back up to the full angle with the double-angle formula, and let '
    'the quadrant pick the sign at the square-root step. Rubric F2 C1 P0 T2 L0 = 5 -> ปานกลาง '
    '(one key: knowing tan u + cot u = 2/sin 2u collapses the half angle in a single line; the '
    'sign case is decided instantly by the given range). sympy: sp.simplify cannot collapse '
    'tan(t/2) + cot(t/2) - 2/sin(t) directly, so the identity was proved in half-angle form '
    'via together(expand_trig(sin u/cos u + cos u/sin u - 2/sin 2u)) = 0 and sampled numerically '
    'at 60 digits; the independent route tan(t/2) = sin t/(1 + cos t) = -4/3 was verified too. '
    'Traps: 7/25 ignores the quadrant, -24/25 stops at the intermediate sin value, 24/25 is that '
    'same intermediate value with the sign lost. Collision sweep on 6367 items: the bank has no '
    'item that GIVES a half-angle expression and asks for a full-angle value; every half-angle '
    'item in the bank runs the other direction (full angle given, half angle asked), which is '
    'why this one was reversed after the first sweep flagged pat1-2559-10-q11.')
# ══════════════════════════════════════════════════════════════════ q057
add(57, ['7.7', '7.5'], 'ปานกลาง',
    'จำนวนคำตอบที่แตกต่างกันทั้งหมดของสมการ $\\sin 5x = \\sin x$ '
    'ในช่วง $0 < x < \\pi$ เท่ากับข้อใด',
    ['$3$', '$4$', '$5$', '$6$'], 0,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• $\\sin A = \\sin B$ ก็ต่อเมื่อ $A = B + 2k\\pi$ '
        '<b>หรือ</b> $A = \\pi - B + 2k\\pi$ เมื่อ $k$ เป็นจำนวนเต็ม '
        '⛔ ต้องทำ<b>ทั้งสองสาขา</b> ไม่ใช่สาขาเดียว',
        '• ช่วง $0 < x < \\pi$ เป็น<b>ช่วงเปิด</b> '
        '⇒ ค่า $x = 0$ และ $x = \\pi$ ใช้ไม่ได้',
        '• คำว่า “จำนวนคำตอบที่แตกต่างกัน” แปลว่าถ้าค่าเดียวกันโผล่จากทั้งสองสาขา '
        'ให้นับเพียงครั้งเดียว',
        '• สูตรผลต่างเป็นผลคูณ '
        '$\\sin A - \\sin B = 2\\cos\\dfrac{A+B}{2}\\sin\\dfrac{A-B}{2}$ '
        '(ใช้ในบล็อกตรวจคำตอบ)',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• สมการคือ $\\sin 5x = \\sin x$ ซึ่งเป็นไซน์เท่ากับไซน์ ไม่ใช่เท่ากับตัวเลข',
        '• ช่วงที่สนใจคือ $0 < x < \\pi$ ซึ่งเป็นครึ่งรอบและเป็นช่วงเปิดทั้งสองข้าง',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• นับว่ามีค่า $x$ ที่<b>ต่างกัน</b>กี่ค่าในช่วงเปิดนี้ที่ทำให้สมการเป็นจริง',
        '',
        '<b>【 แตกเป็นสองสาขาตามเงื่อนไข $\\sin A = \\sin B$ '
        'ไล่ค่า $k$ ในแต่ละสาขาให้ครบเฉพาะที่ตกในช่วงเปิด '
        'แล้วรวมสองเซตแบบตัดค่าซ้ำออก 】</b>',
        '',
        '<b>ขั้นที่ 1 · แตกสมการเป็นสองสาขา</b>',
        '• ให้ $A = 5x$ และ $B = x$ ⇒ เงื่อนไขคือ '
        '$5x = x + 2k\\pi$ หรือ $5x = \\pi - x + 2k\\pi$',
        '• สาขาที่หนึ่ง $5x - x = 2k\\pi$ ⇒ $4x = 2k\\pi$ ⇒ '
        '$x = \\dfrac{k\\pi}{2}$',
        '• สาขาที่สอง $5x + x = \\pi + 2k\\pi$ ⇒ $6x = (2k+1)\\pi$ ⇒ '
        '$x = \\dfrac{(2k+1)\\pi}{6}$',
        '',
        '<b>ขั้นที่ 2 · ไล่ค่า $k$ ของสาขาที่หนึ่งในช่วงเปิด</b>',
        '• $k = 0$ ได้ $x = 0$ ⇒ ⛔ ตกขอบ ใช้ไม่ได้เพราะช่วงเป็นช่วงเปิด',
        '• $k = 1$ ได้ $x = \\dfrac{\\pi}{2}$ ⇒ ✔ อยู่ในช่วง',
        '• $k = 2$ ได้ $x = \\pi$ ⇒ ⛔ ตกขอบ ใช้ไม่ได้',
        '• ค่า $k$ ที่ใหญ่กว่าหรือเล็กกว่านี้จะหลุดออกนอกช่วงทั้งหมด '
        '⇒ สาขาที่หนึ่งให้คำตอบเพียงค่าเดียวคือ $\\dfrac{\\pi}{2}$',
        '',
        '<b>ขั้นที่ 3 · ไล่ค่า $k$ ของสาขาที่สองในช่วงเปิด</b>',
        '• $k = 0$ ได้ $x = \\dfrac{\\pi}{6}$ ⇒ ✔ อยู่ในช่วง',
        '• $k = 1$ ได้ $x = \\dfrac{3\\pi}{6} = \\dfrac{\\pi}{2}$ ⇒ ✔ อยู่ในช่วง',
        '• $k = 2$ ได้ $x = \\dfrac{5\\pi}{6}$ ⇒ ✔ อยู่ในช่วง',
        '• $k = 3$ ได้ $x = \\dfrac{7\\pi}{6}$ ซึ่งเกิน $\\pi$ '
        'และ $k = -1$ ได้ $x = -\\dfrac{\\pi}{6}$ ซึ่งต่ำกว่า $0$ '
        '⇒ สาขาที่สองให้สามค่า คือ '
        '$\\dfrac{\\pi}{6},\\ \\dfrac{\\pi}{2},\\ \\dfrac{5\\pi}{6}$',
        '',
        '<b>ขั้นที่ 4 · รวมสองเซตแล้วตัดค่าซ้ำ</b>',
        '• เซตจากสาขาที่หนึ่งคือ $\\left\\{\\dfrac{\\pi}{2}\\right\\}$ '
        'เซตจากสาขาที่สองคือ '
        '$\\left\\{\\dfrac{\\pi}{6},\\ \\dfrac{\\pi}{2},\\ \\dfrac{5\\pi}{6}\\right\\}$',
        '• ค่า $\\dfrac{\\pi}{2}$ โผล่ในทั้งสองสาขา ⇒ นับเพียงครั้งเดียว',
        '• ยูเนียนได้ '
        '$\\left\\{\\dfrac{\\pi}{6},\\ \\dfrac{\\pi}{2},\\ \\dfrac{5\\pi}{6}\\right\\}$ '
        '⇒ มีคำตอบที่แตกต่างกัน $3$ ค่า',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แปลงผลต่างเป็นผลคูณแล้วนับศูนย์ของแต่ละตัวประกอบ)</b>',
        '• ย้ายข้างเป็น $\\sin 5x - \\sin x = 0$ '
        'แล้วใช้สูตรผลต่างเป็นผลคูณ ได้ '
        '$2\\cos\\dfrac{5x+x}{2}\\sin\\dfrac{5x-x}{2} = 2\\cos 3x\\sin 2x = 0$',
        '• ตัวประกอบแรก $\\cos 3x = 0$ ⇒ $3x = \\dfrac{\\pi}{2} + k\\pi$ ⇒ '
        '$x = \\dfrac{\\pi}{6},\\ \\dfrac{\\pi}{2},\\ \\dfrac{5\\pi}{6}$ ในช่วงเปิด',
        '• ตัวประกอบที่สอง $\\sin 2x = 0$ ⇒ $2x = k\\pi$ ⇒ '
        '$x = \\dfrac{\\pi}{2}$ ค่าเดียวในช่วงเปิด',
        '• ยูเนียนของศูนย์ทั้งสองตัวประกอบได้ $3$ ค่าเท่าเดิม ตรงกับวิธีแรก',
        '• ข้อสังเกตสำคัญ ที่ $x = \\dfrac{\\pi}{2}$ ตัวประกอบ<b>ทั้งสอง</b>เป็นศูนย์พร้อมกัน '
        '⇒ เป็นรากซ้ำ กราฟของ $\\sin 5x - \\sin x$ แตะแกนโดยไม่เปลี่ยนเครื่องหมาย '
        'ใครที่นับคำตอบด้วยการดูจุดที่กราฟตัดแกนจะนับได้เพียง $2$ ซึ่งขาดไป $1$',
        '',
        '✅ <b>คำตอบ</b> สมการมีคำตอบที่แตกต่างกัน $3$ ค่า → <b>ตัวเลือก 1</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอ $\\sin A = \\sin B$ ให้เขียนสองสาขาลงกระดาษก่อนเสมอ '
        'แล้วค่อยไล่ $k$ ทีละสาขา อย่ารีบยุบหรือหารทิ้ง '
        'เพราะการหารด้วยฟังก์ชันตรีโกณจะทำคำตอบหายทันที',
        '• เขียนคำตอบเป็น<b>เซต</b> ไม่ใช่รายการ '
        'เพราะโจทย์แบบนี้จงใจให้สองสาขาทับกันหนึ่งค่าเสมอ ⇒ ยูเนียนจะตัดซ้ำให้เอง',
        '• อ่านวงเล็บของช่วงให้ชัดว่าเปิดหรือปิด '
        'ในข้อนี้ถ้าเป็นช่วงปิด $[0,\\ \\pi]$ คำตอบจะเพิ่มเป็น $5$ ทันที',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• $4$ — ทำครบสองสาขาแล้วเอาจำนวนมาบวกกันตรง ๆ '
        'คือ $1 + 3 = 4$ โดยไม่สังเกตว่า $\\dfrac{\\pi}{2}$ ซ้ำกัน '
        'นี่คือจุดพลาดหลักของข้อนี้',
        '• $5$ — ตัดค่าซ้ำถูกต้อง แต่อ่านช่วงเป็นช่วงปิด $[0,\\ \\pi]$ '
        'จึงรับ $x = 0$ และ $x = \\pi$ จากสาขาที่หนึ่งเข้ามาด้วย '
        'ได้เป็นห้าค่า',
        '• $6$ — พลาดทั้งสองอย่างพร้อมกัน คืออ่านเป็นช่วงปิดและไม่ตัดค่าซ้ำ '
        'จึงได้สาขาละสามค่าแล้วบวกเป็น $3 + 3 = 6$',
    ],
    'V.mold: G = an equation of the form sin(5x) = sin(x) on an OPEN half-turn interval / '
    'A = the number of DISTINCT solutions / M = split into the two branches of sin A = sin B, '
    'enumerate k in each, then union with de-duplication, with the open endpoints doing extra '
    'work. Rubric F1 C2 P0 T2 L0 = 5 -> ปานกลาง (the two branches are a genuine case split, and '
    'the key is realising the branches overlap and the interval is open). sympy: both branch '
    'families enumerated over k = -8..8 and intersected with the open interval, giving exactly '
    '{pi/6, pi/2, 5pi/6}; independently the factorisation sin 5x - sin x = 2 cos 3x sin 2x was '
    'proved symbolically and the union of the two factors zeros matched. NOTE recorded in '
    'verify_b10.py: a numeric SIGN-CHANGE sweep finds only 2 crossings because x = pi/2 is a '
    'double root (zero of BOTH factors), so counting must be done on the root set. Traps: 4 = '
    'no de-duplication, 5 = closed interval with de-duplication, 6 = closed interval and no '
    'de-duplication. Collision sweep on 6367 items: the planned sin 3x + sin x = sin 2x was '
    'identical to chap-07-trigonometry-q59 and pat1-2557-03-q36 so it was replaced; no bank item '
    'runs sin(5x) = sin(x) or asks for a distinct-solution count on an open interval.')
# ══════════════════════════════════════════════════════════════════ q058
add(58, ['7.5'], 'ปานกลาง',
    'กำหนดให้ $A$ และ $B$ เป็นจำนวนจริงซึ่ง $\\tan A$ และ $\\tan B$ หาค่าได้ '
    'และ $\\tan B \\ne 0$ โดยที่ $\\sin(A+B) = \\dfrac{3}{5}$ '
    'และ $\\sin(A-B) = \\dfrac{1}{5}$ '
    'แล้ว $\\dfrac{\\tan A}{\\tan B}$ เท่ากับข้อใด',
    ['$\\dfrac{1}{3}$', '$\\dfrac{1}{2}$', '$2$', '$3$'], 2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• สูตรผลบวกมุม $\\sin(A+B) = \\sin A\\cos B + \\cos A\\sin B$',
        '• สูตรผลต่างมุม $\\sin(A-B) = \\sin A\\cos B - \\cos A\\sin B$',
        '• สองสูตรนี้ต่างกันแค่เครื่องหมายกลาง '
        '⇒ บวกกันแล้วพจน์หลังตัดกัน ลบกันแล้วพจน์หน้าตัดกัน',
        '• นิยาม $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ ⇒ '
        '$\\dfrac{\\tan A}{\\tan B} = \\dfrac{\\sin A / \\cos A}{\\sin B / \\cos B} '
        '= \\dfrac{\\sin A\\cos B}{\\cos A\\sin B}$',
        '• ⛔ $\\dfrac{\\sin(A+B)}{\\sin(A-B)}$ <b>ไม่เท่ากับ</b> '
        '$\\dfrac{\\tan A}{\\tan B}$ เพราะไซน์ไม่ใช่ฟังก์ชันที่กระจายผ่านการบวกได้',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• ค่าที่ให้มาเป็นค่าของ<b>มุมผสม</b> คือ $\\sin(A+B) = \\dfrac{3}{5}$ '
        'และ $\\sin(A-B) = \\dfrac{1}{5}$',
        '• โจทย์ไม่ได้ให้ค่าของ $A$ หรือ $B$ แยกกัน '
        'และไม่ได้ให้จตุภาคของมุมใดเลย',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาอัตราส่วน $\\dfrac{\\tan A}{\\tan B}$ '
        '⇒ สังเกตว่าเป็น<b>อัตราส่วน</b> ไม่ใช่ค่าของ $\\tan A$ หรือ $\\tan B$ '
        'จึงไม่จำเป็นต้องหามุมทั้งสองแยกกัน',
        '',
        '<b>【 กระจายสองสูตรออกมา แล้วบวกและลบกันเพื่อดึงผลคูณไขว้สองก้อน '
        'ซึ่งเป็นเศษและส่วนของอัตราส่วนที่โจทย์ถามพอดี 】</b>',
        '',
        '<b>ขั้นที่ 1 · กระจายสองสูตรที่โจทย์ให้</b>',
        '• จากค่าแรก $\\sin A\\cos B + \\cos A\\sin B = \\dfrac{3}{5}$',
        '• จากค่าที่สอง $\\sin A\\cos B - \\cos A\\sin B = \\dfrac{1}{5}$',
        '• สังเกตว่าตอนนี้เหลือของที่ไม่รู้ค่าเพียงสองก้อน คือ '
        '$\\sin A\\cos B$ กับ $\\cos A\\sin B$',
        '',
        '<b>ขั้นที่ 2 · บวกสองสมการเพื่อดึงก้อนแรก</b>',
        '• บวกกัน พจน์ $\\cos A\\sin B$ ตัดกันพอดี ได้ '
        '$2\\sin A\\cos B = \\dfrac{3}{5} + \\dfrac{1}{5} = \\dfrac{4}{5}$',
        '• ดังนั้น $\\sin A\\cos B = \\dfrac{2}{5}$',
        '',
        '<b>ขั้นที่ 3 · ลบสองสมการเพื่อดึงก้อนที่สอง</b>',
        '• ลบกัน พจน์ $\\sin A\\cos B$ ตัดกันพอดี ได้ '
        '$2\\cos A\\sin B = \\dfrac{3}{5} - \\dfrac{1}{5} = \\dfrac{2}{5}$',
        '• ดังนั้น $\\cos A\\sin B = \\dfrac{1}{5}$',
        '',
        '<b>ขั้นที่ 4 · ประกอบเป็นอัตราส่วนที่โจทย์ถาม</b>',
        '• เขียนอัตราส่วนตามนิยามแทนเจนต์ ได้ '
        '$\\dfrac{\\tan A}{\\tan B} = \\dfrac{\\sin A\\cos B}{\\cos A\\sin B}$',
        '• แทนสองก้อนที่หาได้ ได้ '
        '$\\dfrac{2/5}{1/5} = 2$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · หารสองสูตรด้วย $\\cos A\\cos B$ '
        'แล้วตั้งสมการของอัตราส่วนโดยตรง)</b>',
        '• หารทั้งสองสูตรที่กระจายแล้วด้วย $\\cos A\\cos B$ '
        'จะได้ $\\dfrac{\\sin(A+B)}{\\cos A\\cos B} = \\tan A + \\tan B$ '
        'และ $\\dfrac{\\sin(A-B)}{\\cos A\\cos B} = \\tan A - \\tan B$',
        '• หารสองผลลัพธ์นี้กัน ตัว $\\cos A\\cos B$ หายไป ได้เอกลักษณ์ '
        '$\\dfrac{\\sin(A+B)}{\\sin(A-B)} = \\dfrac{\\tan A + \\tan B}{\\tan A - \\tan B}$',
        '• ให้ $r = \\dfrac{\\tan A}{\\tan B}$ แล้วหารเศษและส่วนฝั่งขวาด้วย $\\tan B$ '
        '(ทำได้เพราะโจทย์กำหนด $\\tan B \\ne 0$) ได้ $\\dfrac{r+1}{r-1}$',
        '• ฝั่งซ้ายเท่ากับ $\\dfrac{3/5}{1/5} = 3$ ⇒ สมการคือ '
        '$\\dfrac{r+1}{r-1} = 3$ ⇒ $r + 1 = 3r - 3$ ⇒ $r = 2$ ค่าเดียว '
        'ตรงกับวิธีแรก',
        '• เส้นทางนี้ยังอธิบายด้วยว่าทำไมเลข $3$ ถึงน่าหลง เพราะ $3$ คืออัตราส่วนของ '
        '<b>ไซน์</b>สองตัว ซึ่งเป็นแค่ฝั่งซ้ายของสมการ ไม่ใช่คำตอบ',
        '',
        '✅ <b>คำตอบ</b> $\\dfrac{\\tan A}{\\tan B} = 2$ → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เห็น $\\sin(A+B)$ กับ $\\sin(A-B)$ มาคู่กันเมื่อไร ให้กระจายแล้ว '
        '<b>บวกกับลบ</b>ทันที เพราะสองสูตรต่างกันแค่เครื่องหมายกลาง '
        'การบวกและการลบจะแยกผลคูณไขว้สองก้อนออกมาให้ฟรี ๆ',
        '• โจทย์ที่ถาม<b>อัตราส่วน</b>มักไม่ต้องหามุมจริงเลย '
        'ให้ถามตัวเองก่อนว่าอัตราส่วนนั้นเขียนด้วยก้อนที่หาได้แล้วหรือยัง',
        '• ทุกครั้งที่อยากหารค่าที่โจทย์ให้ตรง ๆ ให้หยุดคิดว่าฟังก์ชันนั้น '
        'กระจายผ่านการบวกได้หรือไม่ ซึ่งไซน์และโคไซน์<b>ไม่ได้</b>',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• $3$ — หารค่าที่โจทย์ให้ตรง ๆ เป็น '
        '$\\dfrac{\\sin(A+B)}{\\sin(A-B)} = \\dfrac{3/5}{1/5} = 3$ '
        'แล้วเชื่อว่าเท่ากับอัตราส่วนของแทนเจนต์ '
        'นี่คือจุดพลาดหลักของข้อนี้ และเป็นเหตุผลที่ตัวเลข $3$ ถูกวางไว้เป็นตัวเลือก',
        '• $\\dfrac{1}{2}$ — ทำถูกทุกขั้น แต่ประกอบอัตราส่วนกลับข้างเป็น '
        '$\\dfrac{\\tan B}{\\tan A} = \\dfrac{\\cos A\\sin B}{\\sin A\\cos B}$',
        '• $\\dfrac{1}{3}$ — พลาดสองอย่างพร้อมกัน คือหารค่าที่โจทย์ให้ตรง ๆ '
        'แล้วยังกลับข้างอัตราส่วนอีกที ได้ $\\dfrac{1/5}{3/5}$',
    ],
    'V.mold: G = the values of sin(A+B) AND sin(A-B) together, with no quadrant and no '
    'individual angle / A = the RATIO tan A / tan B / M = expand both sum-and-difference '
    'formulas, then add and subtract them to isolate the two cross products sinA cosB and '
    'cosA sinB, which are exactly the numerator and denominator of the requested ratio. '
    'Rubric F1 C0 P0 T2 L0 = 3 -> ปานกลาง (one key: seeing that the ratio of tangents IS the '
    'ratio of the two cross products, so neither angle is ever needed; everything else is two '
    'named formulas and arithmetic). sympy: solved for concrete angle pairs satisfying both '
    'givens and measured tan A / tan B = 2 to within 1e-25, repeated for a second pair with A+B '
    'in the second quadrant; independently proved sin(A+B)/sin(A-B) = (tanA+tanB)/(tanA-tanB) '
    'symbolically and solved (r+1)/(r-1) = 3 for the unique r = 2. Traps: 3 divides the two '
    'givens directly, 1/2 inverts the ratio, 1/3 does both. Collision sweep on 6367 items: no '
    'bank item gives BOTH sin(A+B) and sin(A-B) at once, and no bank item asks for a ratio of '
    'two tangents; the sum-and-difference items in the bank all give one composite value plus a '
    'quadrant and ask for a single trig value.')
# ══════════════════════════════════════════════════════════════════ q059
add(59, ['7.7', '7.6'], 'ยากมาก',
    'กำหนดให้ $a$ เป็นจำนวนจริง ถ้าสมการ '
    '$\\cos 2x + (2a-1)\\cos x + (1-a) = 0$ '
    'มีคำตอบที่แตกต่างกันทั้งหมดพอดี $3$ คำตอบในช่วง $0 \\le x < 2\\pi$ '
    'แล้วเซตของค่า $a$ ทั้งหมดที่เป็นไปได้ตรงกับข้อใด',
    ['$\\{1\\}$', '$\\{-1,\\ 1\\}$',
     '$\\left\\{-1,\\ -\\dfrac{1}{2},\\ 1\\right\\}$',
     '$\\left\\{-1,\\ \\dfrac{1}{2},\\ 1\\right\\}$'], 1,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• สูตรมุมสองเท่าของโคไซน์เขียนได้<b>สามรูป</b> คือ '
        '$\\cos 2x = \\cos^2 x - \\sin^2 x = 2\\cos^2 x - 1 = 1 - 2\\sin^2 x$ '
        '⇒ ต้องเลือกรูปที่ทำให้สมการเหลือฟังก์ชันตรีโกณชนิดเดียว',
        '• การแยกตัวประกอบพหุนามกำลังสอง $2c^2 + (2a-1)c - a$ '
        'ทำได้ด้วยการจับคู่ $2c^2 + 2ac - c - a = 2c(c+a) - (c+a) = (2c-1)(c+a)$',
        '• จำนวนคำตอบของ $\\cos x = m$ ในช่วง $0 \\le x < 2\\pi$ '
        'ขึ้นกับค่า $m$ คือ ได้ $2$ คำตอบเมื่อ $-1 < m < 1$ '
        'ได้ $1$ คำตอบเมื่อ $m = 1$ (ที่ $x = 0$) หรือ $m = -1$ (ที่ $x = \\pi$) '
        'และไม่มีคำตอบเมื่อ $|m| > 1$',
        '• เมื่อสมการแยกได้เป็นสองสาขา จำนวนคำตอบรวมคือจำนวนสมาชิกของ<b>ยูเนียน</b> '
        '⇒ ถ้าสองสาขาให้ค่า $x$ ตัวเดียวกัน ต้องนับครั้งเดียว',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• สมการมีทั้งมุม $2x$ และมุม $x$ ปนกัน และมีพารามิเตอร์ $a$ '
        'อยู่ทั้งในพจน์หน้า $\\cos x$ และในพจน์คงตัว',
        '• ช่วงที่กำหนดคือ $0 \\le x < 2\\pi$ ซึ่งเป็นหนึ่งรอบเต็มแบบปิดซ้ายเปิดขวา '
        '⇒ $x = 0$ ใช้ได้ แต่ $x = 2\\pi$ ใช้ไม่ได้',
        '• เงื่อนไขคือจำนวนคำตอบต้องเป็น $3$ <b>พอดี</b> ไม่ใช่อย่างน้อย $3$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาเซตของค่า $a$ ทั้งหมดที่ทำให้จำนวนคำตอบที่แตกต่างกันเท่ากับ $3$ พอดี',
        '',
        '<b>【 เลือกรูปของสูตรมุมสองเท่าให้สมการกลายเป็นพหุนามใน $\\cos x$ ล้วน '
        'แยกตัวประกอบเป็นสาขาคงที่บวกสาขาที่มีพารามิเตอร์ '
        'แล้วนับคำตอบของสาขาพารามิเตอร์แบบแยกกรณี พร้อมตรวจกรณีที่สองสาขาให้ค่าซ้ำกัน 】</b>',
        '',
        '<b>ขั้นที่ 1 · เลือกรูปของสูตรมุมสองเท่าให้ถูกตัว</b>',
        '• สมการมี $\\cos x$ อยู่แล้ว ⇒ ต้องการให้ทุกพจน์เป็นฟังก์ชันของ $\\cos x$ '
        'จึงเลือกรูป $\\cos 2x = 2\\cos^2 x - 1$',
        '• ⛔ ถ้าเลือกรูป $1 - 2\\sin^2 x$ สมการจะปนทั้ง $\\sin$ และ $\\cos$ '
        'ต้องเสียจังหวะแทน $\\sin^2 x = 1 - \\cos^2 x$ เพิ่มอีกขั้นจึงจะถึงที่เดียวกัน',
        '• แทนลงไป ได้ $2\\cos^2 x - 1 + (2a-1)\\cos x + 1 - a = 0$',
        '• พจน์ $-1$ กับ $+1$ ตัดกัน เหลือ '
        '$2\\cos^2 x + (2a-1)\\cos x - a = 0$',
        '',
        '<b>ขั้นที่ 2 · แยกตัวประกอบเป็นสองสาขา</b>',
        '• ให้ $c = \\cos x$ ⇒ สมการคือ $2c^2 + (2a-1)c - a = 0$',
        '• จับคู่แยกตัวประกอบ $2c^2 + 2ac - c - a = 2c(c+a) - 1(c+a) = (2c-1)(c+a)$',
        '• ดังนั้น $(2\\cos x - 1)(\\cos x + a) = 0$ ⇒ '
        'สาขาที่หนึ่ง $\\cos x = \\dfrac{1}{2}$ '
        'และสาขาที่สอง $\\cos x = -a$',
        '• สังเกตว่าสาขาที่หนึ่ง<b>ไม่มี $a$ อยู่เลย</b> ⇒ เป็นสาขาคงที่',
        '',
        '<b>ขั้นที่ 3 · นับคำตอบของสาขาคงที่</b>',
        '• $\\cos x = \\dfrac{1}{2}$ ในช่วง $0 \\le x < 2\\pi$ ได้ '
        '$x = \\dfrac{\\pi}{3}$ และ $x = \\dfrac{5\\pi}{3}$',
        '• สาขานี้จึงให้ $2$ คำตอบ<b>เสมอ</b> ไม่ว่า $a$ จะเป็นเท่าใด '
        '⇒ เหลือโควตาให้สาขาที่สองอีก $1$ คำตอบพอดี',
        '',
        '<b>ขั้นที่ 4 · แยกกรณีจำนวนคำตอบของสาขาพารามิเตอร์</b>',
        '• กรณี $|-a| > 1$ นั่นคือ $|a| > 1$ ⇒ $\\cos x = -a$ ไม่มีคำตอบ '
        '⇒ รวมได้ $2$ คำตอบ ⛔ ไม่ถึง $3$',
        '• กรณี $-a = 1$ หรือ $-a = -1$ นั่นคือ $a = -1$ หรือ $a = 1$ ⇒ '
        '$\\cos x = -a$ ให้คำตอบเพียง $1$ ค่า (ที่ $x = 0$ หรือ $x = \\pi$ ตามลำดับ) '
        '⇒ รวมได้ $3$ คำตอบ ✔',
        '• กรณี $-1 < -a < 1$ นั่นคือ $|a| < 1$ ⇒ $\\cos x = -a$ ให้ $2$ ค่า '
        '⇒ รวมได้ $4$ คำตอบ ⛔ เกิน $3$',
        '',
        '<b>ขั้นที่ 5 · ตรวจกรณีซ่อนที่สองสาขาให้ค่าซ้ำกัน</b>',
        '• กรณีที่ต้องระวังคือ $-a = \\dfrac{1}{2}$ นั่นคือ $a = -\\dfrac{1}{2}$ '
        'ซึ่งทำให้สมการมีรากซ้ำ $c = \\dfrac{1}{2}$',
        '• ตอนนั้นสาขาที่สองให้ $x = \\dfrac{\\pi}{3},\\ \\dfrac{5\\pi}{3}$ '
        'ซึ่งเป็นค่า<b>เดียวกัน</b>กับสาขาคงที่ ⇒ ยูเนียนยังมีแค่ $2$ ค่า '
        '⛔ ไม่ใช่ $4$ และไม่ใช่ $3$ ⇒ $a = -\\dfrac{1}{2}$ ใช้ไม่ได้',
        '• กรณีนี้ถูกครอบด้วยกรณี $|a| < 1$ ในขั้นที่ $4$ อยู่แล้ว '
        'จึงไม่เปลี่ยนคำตอบ แต่ต้องตรวจเพราะเป็นค่าที่ตัวเลือกวางดักไว้',
        '• สรุปเซตของ $a$ ที่ใช้ได้คือ $\\{-1,\\ 1\\}$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่า $a$ แต่ละตัวกลับเข้าสมการต้นฉบับ '
        'แล้วนับคำตอบจริง)</b>',
        '• แทน $a = 1$ สมการต้นฉบับกลายเป็น $\\cos 2x + \\cos x = 0$ ⇒ '
        '$2\\cos^2 x + \\cos x - 1 = 0$ ⇒ $(2\\cos x - 1)(\\cos x + 1) = 0$ ⇒ '
        '$x = \\dfrac{\\pi}{3},\\ \\pi,\\ \\dfrac{5\\pi}{3}$ ⇒ $3$ คำตอบ ✔',
        '• แทน $a = -1$ สมการกลายเป็น $\\cos 2x - 3\\cos x + 2 = 0$ ⇒ '
        '$2\\cos^2 x - 3\\cos x + 1 = 0$ ⇒ $(2\\cos x - 1)(\\cos x - 1) = 0$ ⇒ '
        '$x = 0,\\ \\dfrac{\\pi}{3},\\ \\dfrac{5\\pi}{3}$ ⇒ $3$ คำตอบ ✔',
        '• แทน $a = -\\dfrac{1}{2}$ ได้ $(2\\cos x - 1)\\left(\\cos x '
        '- \\dfrac{1}{2}\\right) = 0$ ซึ่งเป็นเงื่อนไขเดียวกันสองครั้ง ⇒ '
        '$x = \\dfrac{\\pi}{3},\\ \\dfrac{5\\pi}{3}$ ⇒ $2$ คำตอบ ⛔',
        '• แทน $a = \\dfrac{1}{2}$ ได้ $\\cos x = \\dfrac{1}{2}$ '
        'หรือ $\\cos x = -\\dfrac{1}{2}$ ⇒ '
        '$x = \\dfrac{\\pi}{3},\\ \\dfrac{2\\pi}{3},\\ \\dfrac{4\\pi}{3},\\ \\dfrac{5\\pi}{3}$ '
        '⇒ $4$ คำตอบ ⛔',
        '• กวาดค่า $a$ ตั้งแต่ $-3$ ถึง $3$ ทีละ $\\dfrac{1}{8}$ '
        'แล้วนับคำตอบทุกครั้ง พบว่ามีเพียง $a = -1$ และ $a = 1$ เท่านั้นที่ให้ $3$ คำตอบ',
        '',
        '✅ <b>คำตอบ</b> เซตของค่า $a$ ทั้งหมดคือ $\\{-1,\\ 1\\}$ → <b>ตัวเลือก 2</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• สมการที่มีทั้งมุม $2x$ และมุม $x$ ให้ถามก่อนว่า '
        '“รูปไหนของสูตรมุมสองเท่าจะทำให้เหลือฟังก์ชันชนิดเดียว” '
        'ในข้อนี้ต้องเป็นรูป $2\\cos^2 x - 1$ เพราะพจน์อื่นเป็น $\\cos x$ ทั้งหมด',
        '• โจทย์คุมจำนวนคำตอบที่มีพารามิเตอร์ ให้แยกให้ได้ว่า '
        '<b>สาขาไหนคงที่</b>และ<b>สาขาไหนขยับตามพารามิเตอร์</b> '
        'สาขาคงที่จะบอกโควตาที่เหลือให้ทันที',
        '• จุดที่ $\\cos x = \\pm 1$ พิเศษเสมอ เพราะเป็นจุดสูงสุดและต่ำสุดของกราฟ '
        '⇒ ให้คำตอบเพียงค่าเดียวต่อหนึ่งรอบ ในขณะที่ค่าอื่นให้สองค่า '
        'ข้อสอบที่ขอ “จำนวนคำตอบเป็นเลขคี่” เกือบทั้งหมดเล่นกับจุดสองจุดนี้',
        '• เจอรากซ้ำอย่าเพิ่งดีใจว่าได้คำตอบเพิ่ม '
        'ให้ย้อนไปดูว่ารากนั้นให้ค่า $x$ ที่<b>ซ้ำกับสาขาอื่น</b>หรือไม่',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• $\\{1\\}$ — จำได้เพียงว่า $\\cos x = 1$ ให้คำตอบค่าเดียว '
        'จึงแก้ $-a = 1$ ได้ $a = -1$ หรือแก้เป็น $a = 1$ ทางเดียว '
        'แล้วลืมว่า $\\cos x = -1$ ก็ให้คำตอบเดียวเช่นกัน ⇒ เก็บได้แค่ค่าเดียว '
        'นี่คือจุดพลาดหลักของข้อนี้',
        '• $\\left\\{-1,\\ -\\dfrac{1}{2},\\ 1\\right\\}$ — เห็นรากซ้ำที่ '
        '$a = -\\dfrac{1}{2}$ แล้วคิดว่ารากซ้ำเพิ่มคำตอบเข้ามาอีกหนึ่ง '
        'ทั้งที่มันให้ค่า $x$ ซ้ำกับสาขาคงที่ทุกค่า ⇒ จำนวนคำตอบลดเหลือ $2$ ไม่ใช่ $3$',
        '• $\\left\\{-1,\\ \\dfrac{1}{2},\\ 1\\right\\}$ — สับสนเครื่องหมายระหว่าง '
        '$a$ กับ $-a$ จึงคิดว่า $a = \\dfrac{1}{2}$ คือกรณีรากซ้ำ '
        'ทั้งที่ $a = \\dfrac{1}{2}$ ให้ $\\cos x = -\\dfrac{1}{2}$ '
        'ซึ่งเพิ่มคำตอบมาสองค่า รวมเป็น $4$',
    ],
    'V.mold: G = a PARAMETERISED equation mixing cos 2x with cos x, with the parameter sitting in '
    'both the linear coefficient and the constant term / A = the SET of all parameter values '
    'giving exactly 3 distinct solutions on one full turn / M = choose the cos-form of the '
    'double-angle identity yourself so the equation becomes a polynomial in cos x, factor it into '
    'a FIXED branch plus a PARAMETER branch, count the parameter branch by cases, and catch the '
    'hidden repeated-root case where the two branches coincide. Rubric F3 C3 P2 T3 L1 = 12 -> '
    'ยากมาก (two chained keys: picking the right form of cos 2x, then splitting into a fixed and '
    'a moving branch; nested cases plus one hidden case). ⛔ NOTE: the first draft of this item '
    'was 2cos^2 x + (2a-1)cos x - a = 0, which graded honestly at 11 = ยาก; rather than inflate '
    'the score, the QUESTION was redesigned to open one angle-identity step earlier, and the '
    'rubric was then re-scored from scratch. sympy: swept a from -3 to 3 in steps of 1/8 and '
    'counted distinct roots on [0, 2pi), obtaining exactly {-1, 1}; verified the substitution and '
    'the factorisation (2c-1)(c+a) symbolically, and confirmed that choosing the 1-2sin^2 x form '
    'requires one extra substitution to reach the same polynomial. Traps: {1} keeps only one of '
    'the two endpoint cases, {-1,-1/2,1} treats the repeated root as an extra solution when it '
    'duplicates the fixed branch, {-1,1/2,1} confuses a with -a. Collision sweep on 6367 items '
    '(collide_b10c.py): 0 items mix cos 2x with cos x under a parameter; the 4 items asking for '
    'a parameter set giving exactly 3 solutions are all absolute-value questions in chapters 3 '
    'and 5 (gen-chap-03-real-q031, q034, q196, gen-chap-05-function-q127), a different chapter '
    'and a different mechanism; the nearest chapter-7 item is pat1-2559-10-q34 '
    '(cos 2x + sin x = tan 225 degrees) which has no parameter and does not count solutions.')


data = collections.OrderedDict([('setId', SET), ('questions', Q)])
path = os.path.join(
    OUT,
    'k2-ก้อน10-5ข้อ-7.5-7.6-7.7-สัมประสิทธิ์-ครึ่งมุมกลับทิศ-นับคำตอบ-อัตราส่วนแทน-พารามิเตอร์.json')
txt = json.dumps(data, ensure_ascii=False, indent=2)
io.open(path, 'w', encoding='utf-8', newline='\n').write(txt)
print('เขียน', os.path.basename(path), '·', len(txt.encode()), 'B ·', len(Q), 'ข้อ')

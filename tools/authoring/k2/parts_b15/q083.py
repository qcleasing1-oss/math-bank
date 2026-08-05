# -*- coding: utf-8 -*-
add(
    83,
    ['7.4', '7.7'],
    'ยาก',
    'กำหนดให้ $0 < \\theta < 2\\pi$ และ '
    '$\\dfrac{1}{\\sec\\theta - \\tan\\theta} - \\dfrac{1}{\\sec\\theta + \\tan\\theta} '
    '= \\sec\\theta - 1$ '
    'แล้วค่าของ $\\sin\\theta + \\cos\\theta$ เท่ากับข้อใด',
    [
        '$-\\dfrac{7}{5}$',
        '$-\\dfrac{4}{3}$',
        '$-1$',
        '$\\dfrac{1}{5}$',
    ],
    3,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เอกลักษณ์พีทาโกรัสรูปที่สอง : $\\sec^2\\theta - \\tan^2\\theta = 1$ '
        'ซึ่งได้จากการหาร $\\sin^2\\theta + \\cos^2\\theta = 1$ ด้วย $\\cos^2\\theta$ ตลอดทั้งสมการ',
        '• ผลต่างกำลังสอง : $(x - y)(x + y) = x^2 - y^2$ '
        'เมื่อนำมาใช้กับ $\\sec\\theta$ และ $\\tan\\theta$ จะได้ '
        '$(\\sec\\theta - \\tan\\theta)(\\sec\\theta + \\tan\\theta) = \\sec^2\\theta - \\tan^2\\theta = 1$ '
        'นั่นคือสองวงเล็บนี้เป็นส่วนกลับของกันและกันเสมอ',
        '• นิยาม : $\\sec\\theta = \\dfrac{1}{\\cos\\theta}$ และ '
        '$\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        'ทั้งสองใช้ได้เมื่อ $\\cos\\theta \\ne 0$ เท่านั้น',
        '• การยกกำลังสองทั้งสองข้างของสมการ อาจสร้างรากแปลกปลอมที่ไม่ใช่คำตอบของสมการเดิม '
        'จึงต้องนำรากทุกตัวกลับไปแทนในสมการต้นฉบับและตรวจเงื่อนไขของโจทย์ทุกครั้ง',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $0 < \\theta < 2\\pi$ ซึ่งเป็นช่วงเปิด ไม่รวมปลายทั้งสองข้าง',
        '• $\\dfrac{1}{\\sec\\theta - \\tan\\theta} - \\dfrac{1}{\\sec\\theta + \\tan\\theta} '
        '= \\sec\\theta - 1$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\sin\\theta + \\cos\\theta$',
        '',
        '<b>【 ยุบข้างซ้ายด้วยผลต่างกำลังสองก่อน แล้วจึงเปลี่ยนทุกอย่างเป็นไซน์กับโคไซน์ '
        'และคัดรากแปลกปลอมด้วยช่วงที่โจทย์ให้ 】</b>',
        '',
        '<b>ขั้นที่ 1 · ยุบข้างซ้ายโดยไม่กระจายเศษส่วน</b>',
        '• รวมเศษส่วนสองก้อนโดยใช้ตัวส่วนร่วม : '
        '$\\dfrac{1}{\\sec\\theta - \\tan\\theta} - \\dfrac{1}{\\sec\\theta + \\tan\\theta} '
        '= \\dfrac{(\\sec\\theta + \\tan\\theta) - (\\sec\\theta - \\tan\\theta)}'
        '{(\\sec\\theta - \\tan\\theta)(\\sec\\theta + \\tan\\theta)}$',
        '• คิดตัวเศษ : $\\sec\\theta + \\tan\\theta - \\sec\\theta + \\tan\\theta = 2\\tan\\theta$',
        '• คิดตัวส่วนด้วยผลต่างกำลังสอง : '
        '$\\sec^2\\theta - \\tan^2\\theta = 1$ ซึ่งเป็นเอกลักษณ์พีทาโกรัสรูปที่สองพอดี',
        '• ดังนั้นข้างซ้ายทั้งก้อนยุบเหลือ $\\dfrac{2\\tan\\theta}{1} = 2\\tan\\theta$ '
        '⛔ นี่คือกุญแจดอกแรก ถ้ากระจายเศษส่วนออกมาตรง ๆ จะจมอยู่กับตัวส่วนที่ไม่ยอมหายไป',
        '• สมการจึงกลายเป็น $2\\tan\\theta = \\sec\\theta - 1$',
        '',
        '<b>ขั้นที่ 2 · เปลี่ยนเป็นไซน์กับโคไซน์แล้วกำจัดตัวส่วน</b>',
        '• แทนนิยาม : $2 \\times \\dfrac{\\sin\\theta}{\\cos\\theta} '
        '= \\dfrac{1}{\\cos\\theta} - 1$',
        '• คูณทั้งสมการด้วย $\\cos\\theta$ ซึ่งทำได้เพราะสมการเดิมมี $\\sec\\theta$ อยู่ '
        'จึงต้องมี $\\cos\\theta \\ne 0$ อยู่แล้ว : '
        '$2\\sin\\theta = 1 - \\cos\\theta$',
        '',
        '<b>ขั้นที่ 3 · แก้ระบบร่วมกับเอกลักษณ์พีทาโกรัส</b>',
        '• ยกกำลังสองทั้งสองข้าง : $4\\sin^2\\theta = 1 - 2\\cos\\theta + \\cos^2\\theta$',
        '• แทน $\\sin^2\\theta = 1 - \\cos^2\\theta$ : '
        '$4(1 - \\cos^2\\theta) = 1 - 2\\cos\\theta + \\cos^2\\theta$',
        '• กระจายและย้ายข้างให้เป็นสมการกำลังสองในตัวแปร $\\cos\\theta$ : '
        '$4 - 4\\cos^2\\theta = 1 - 2\\cos\\theta + \\cos^2\\theta$ '
        'จึงได้ $5\\cos^2\\theta - 2\\cos\\theta - 3 = 0$',
        '• แยกตัวประกอบ : $(5\\cos\\theta + 3)(\\cos\\theta - 1) = 0$ '
        'จึงได้ $\\cos\\theta = -\\dfrac{3}{5}$ หรือ $\\cos\\theta = 1$',
        '',
        '<b>ขั้นที่ 4 · คัดรากแปลกปลอมด้วยช่วงที่โจทย์ให้</b>',
        '• กรณี $\\cos\\theta = 1$ มุมเดียวที่ทำได้ในหนึ่งรอบคือ $\\theta = 0$ หรือ $\\theta = 2\\pi$ '
        '⛔ ทั้งสองค่าอยู่นอกช่วงเปิด $0 < \\theta < 2\\pi$ ที่โจทย์กำหนด จึงตัดทิ้ง '
        'นี่คือกุญแจดอกที่สอง รากตัวนี้เกิดจากการยกกำลังสองในขั้นที่แล้ว ไม่ใช่คำตอบจริง',
        '• กรณี $\\cos\\theta = -\\dfrac{3}{5}$ นำกลับไปแทนในสมการก่อนยกกำลังสอง '
        'ซึ่งคือ $2\\sin\\theta = 1 - \\cos\\theta$ : '
        '$2\\sin\\theta = 1 + \\dfrac{3}{5} = \\dfrac{8}{5}$ จึงได้ $\\sin\\theta = \\dfrac{4}{5}$',
        '• ตรวจว่าคู่นี้ใช้ได้จริง : '
        '$\\left(\\dfrac{4}{5}\\right)^2 + \\left(-\\dfrac{3}{5}\\right)^2 '
        '= \\dfrac{16}{25} + \\dfrac{9}{25} = 1$ ผ่านเอกลักษณ์พีทาโกรัส '
        'และไซน์เป็นบวกคู่กับโคไซน์เป็นลบ แปลว่ามุมอยู่ในจตุภาคที่สอง ซึ่งอยู่ในช่วงที่โจทย์ให้',
        '• รวมคำตอบ : '
        '$\\sin\\theta + \\cos\\theta = \\dfrac{4}{5} + \\left(-\\dfrac{3}{5}\\right) = \\dfrac{1}{5}$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ใช้ตัวแปรครึ่งมุม $u = \\tan\\dfrac{\\theta}{2}$ '
        'ซึ่งไม่ต้องยกกำลังสองและไม่ต้องแยกกรณีเลย)</b>',
        '• สูตรตัวแปรครึ่งมุม : $\\sin\\theta = \\dfrac{2u}{1 + u^2}$ และ '
        '$\\cos\\theta = \\dfrac{1 - u^2}{1 + u^2}$',
        '• แทนลงในสมการที่ได้จากขั้นที่ 2 คือ $2\\sin\\theta = 1 - \\cos\\theta$ : '
        '$\\dfrac{4u}{1 + u^2} = 1 - \\dfrac{1 - u^2}{1 + u^2}$',
        '• ข้างขวารวมเป็นเศษส่วนเดียว : '
        '$\\dfrac{(1 + u^2) - (1 - u^2)}{1 + u^2} = \\dfrac{2u^2}{1 + u^2}$',
        '• ตัวส่วนเท่ากันทั้งสองข้างและไม่เป็นศูนย์ จึงเทียบตัวเศษได้ : $4u = 2u^2$ '
        'นั่นคือ $2u(u - 2) = 0$ จึงได้ $u = 0$ หรือ $u = 2$',
        '• กรณี $u = 0$ หมายถึง $\\tan\\dfrac{\\theta}{2} = 0$ ซึ่งให้ $\\theta = 0$ '
        'อยู่นอกช่วงเปิดที่โจทย์ให้ จึงตัดทิ้ง ตรงกับรากแปลกปลอมที่ตัดไปในเส้นทางแรกพอดี',
        '• กรณี $u = 2$ : $\\sin\\theta = \\dfrac{2 \\times 2}{1 + 4} = \\dfrac{4}{5}$ และ '
        '$\\cos\\theta = \\dfrac{1 - 4}{1 + 4} = -\\dfrac{3}{5}$ '
        'จึงได้ $\\sin\\theta + \\cos\\theta = \\dfrac{1}{5}$ เท่ากับเส้นทางแรก',
        '• เส้นทางนี้ไม่ได้ยกกำลังสองเลย จึงไม่มีทางสร้างรากแปลกปลอมขึ้นมาเอง '
        'การที่ยังได้คำตอบเดียวกันจึงยืนยันทั้งค่าคำตอบและความถูกต้องของการคัดราก',
        '',
        '✅ <b>คำตอบ</b> $\\dfrac{1}{5}$ → <b>ตัวเลือก 4</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• จำคู่ผันของตรีโกณไว้สองคู่ คือ $(\\sec\\theta - \\tan\\theta)$ กับ '
        '$(\\sec\\theta + \\tan\\theta)$ ที่คูณกันได้ $1$ '
        'และ $(\\csc\\theta - \\cot\\theta)$ กับ $(\\csc\\theta + \\cot\\theta)$ ที่คูณกันได้ $1$ เช่นกัน '
        'เห็นวงเล็บคู่นี้เมื่อไรให้นึกถึงผลต่างกำลังสองก่อนเสมอ ⛔ อย่ารีบกระจายเศษส่วน',
        '• สมการที่ผ่านการยกกำลังสองมีโอกาสเกิดรากแปลกปลอมเสมอ '
        'ให้ติดนิสัยเขียนบรรทัดสุดท้ายว่า “ตรวจรากกับสมการก่อนยกกำลังสองและกับช่วงที่โจทย์ให้” '
        'ในข้อนี้ช่วงเป็นช่วงเปิด การมองข้ามคำว่าเปิดหรือปิดเพียงคำเดียวทำให้ได้คำตอบเกินมาหนึ่งค่า',
        '• เมื่อโจทย์ถามค่าของ $\\sin\\theta + \\cos\\theta$ ให้ตรวจความเป็นไปได้ด้วยขอบเขต '
        'ค่าของผลบวกนี้ต้องอยู่ระหว่าง $-\\sqrt{2}$ กับ $\\sqrt{2}$ เสมอ '
        'ซึ่งมีค่าประมาณ $-1.414$ ถึง $1.414$ ค่าใดที่หลุดออกนอกช่วงนี้ตัดทิ้งได้ทันที',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $-\\dfrac{7}{5}$ เพราะจับคู่เครื่องหมายผิด '
        'คือหา $\\cos\\theta = -\\dfrac{3}{5}$ ได้ถูกต้องแล้ว แต่หา $\\sin\\theta$ จากเอกลักษณ์พีทาโกรัส '
        'ซึ่งให้ทั้ง $\\dfrac{4}{5}$ และ $-\\dfrac{4}{5}$ แล้วเลือกตัวที่ติดลบ '
        'จึงได้ $-\\dfrac{4}{5} - \\dfrac{3}{5} = -\\dfrac{7}{5}$ '
        'วิธีกันคือหา $\\sin\\theta$ จากสมการเชิงเส้น $2\\sin\\theta = 1 - \\cos\\theta$ '
        'ซึ่งกำหนดเครื่องหมายให้เองอยู่แล้ว ⛔ ไม่ต้องย้อนไปใช้เอกลักษณ์ที่มีสองเครื่องหมาย',
        '• ได้ $-\\dfrac{4}{3}$ เพราะตอบค่าที่หาได้ระหว่างทางแทนสิ่งที่โจทย์ถาม '
        'ค่านี้คือ $\\tan\\theta$ ซึ่งเท่ากับ '
        '$\\dfrac{\\sin\\theta}{\\cos\\theta} = \\dfrac{4}{5} \\div \\left(-\\dfrac{3}{5}\\right) '
        '= -\\dfrac{4}{3}$ '
        'ความพลาดแบบนี้เกิดตอนที่โจทย์มีหลายก้าวจนลืมว่าเป้าหมายคืออะไร '
        'ให้เขียนสิ่งที่ถามไว้มุมกระดาษตั้งแต่แรกแล้วกลับมาอ่านก่อนวงคำตอบ',
        '• ได้ $-1$ เพราะยุบข้างซ้ายผิดเป็น $2\\sec\\theta$ '
        'ซึ่งเป็นผลของรูปที่เครื่องหมายกลางเป็นบวก คือ '
        '$\\dfrac{1}{\\sec\\theta - \\tan\\theta} + \\dfrac{1}{\\sec\\theta + \\tan\\theta} '
        '= 2\\sec\\theta$ '
        'เมื่อสับสนสองรูปนี้จะได้สมการ $2\\sec\\theta = \\sec\\theta - 1$ '
        'ซึ่งให้ $\\sec\\theta = -1$ นั่นคือ $\\cos\\theta = -1$ และ $\\theta = \\pi$ '
        'จึงได้ $\\sin\\pi + \\cos\\pi = 0 + (-1) = -1$ '
        'ให้คิดตัวเศษออกมาให้เห็นจริง ๆ ทุกครั้ง ตัวเศษของรูปลบคือ $2\\tan\\theta$ '
        'ส่วนตัวเศษของรูปบวกคือ $2\\sec\\theta$ ต่างกันคนละฟังก์ชัน',
    ],
    'V.mold: G = a trigonometric equation whose left side is a difference of two reciprocals of the conjugate '
    'pair sec-minus-tan and sec-plus-tan, with theta restricted to the open interval (0, 2pi) / A = the value '
    'of sin(theta) + cos(theta) / M = collapse the conjugate pair through the Pythagorean identity '
    'sec^2 - tan^2 = 1, reduce to a linear relation between sine and cosine, square, solve the quadratic in '
    'cosine, and discard the extraneous root using the open interval. '
    'Rubric F2 C2 P2 T2 L0 = 8/15 with total at least 8 and T at least 2 -> level: ยาก. '
    'Honesty note on the grading: the first draft of this slot was a conjugate-expression evaluation given a '
    'value of cosecant, which scored F2 C1 P0 T2 L0 = 5 and would have been ปานกลาง rather than ยาก; rather '
    'than inflating a dimension, the item was rebuilt as an equation so that a genuine second turning point '
    'exists, namely the extraneous root produced by squaring. '
    'sympy (verify_b15.py): the left side minus 2*tan(theta) simplifies to 0, confirming the collapse; the '
    'system {2s = 1 - c, s^2 + c^2 = 1} is solved symbolically and returns exactly two roots, of which '
    '(s, c) = (0, 1) is the extraneous one that corresponds to theta = 0 or 2pi and is excluded by the open '
    'interval, leaving sin = 4/5 and cos = -3/5 and the answer 1/5. Two independent confirmations are run: '
    'substituting t1 = pi - arcsin(4/5) back into the original equation gives left minus right equal to 0, '
    'and the half-angle substitution u = tan(theta/2) reduces the equation to 4u = 2u^2 whose roots are 0 and '
    '2, reproducing the same accepted and rejected branches without any squaring step. '
    'All three distractors machine-computed from named error paths: -7/5 from -4/5 + -3/5 which is the '
    'wrong sign pairing, -4/3 from S/C which is answering tan(theta) found in passing, and -1 from '
    'sin(pi) + cos(pi) which follows from collapsing the left side into 2*sec(theta); a further sympy check '
    'confirms that the plus form of the same expression really does equal 2*sec(theta), so that error path is '
    'a real confusion between two neighbouring identities rather than an invented one. '
    'Collision sweep on 6392 items (bank 62 files + k1 out + k2 out): the nearest relative in the authored '
    'corpus is q007, which shares the machinery label M-PYTHID-CONJ, but its given is an expression to '
    'evaluate and its asked is a different quantity, so the mold registry reports no flag; the saturated '
    'equation molds in the chapter, namely the sum of roots of a trigonometric equation at 77 items and the '
    'auxiliary-angle form at 80 items, are both untouched here because this item asks for a value of a '
    'sine-plus-cosine expression rather than for roots.',
)

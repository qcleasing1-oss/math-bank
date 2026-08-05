# -*- coding: utf-8 -*-
add(
    91,
    ['7.4'],
    'ง่าย',
    'กำหนดให้ $\\theta$ เป็นจำนวนจริงซึ่ง $\\cos\\theta \\ne 0$ '
    'นิพจน์ $\\dfrac{\\sin^3\\theta + \\sin\\theta\\cos^2\\theta}'
    '{\\cos^3\\theta + \\cos\\theta\\sin^2\\theta}$ เท่ากับข้อใด',
    [
        '$1$',
        '$\\cot\\theta$',
        '$\\tan\\theta$',
        '$\\tan^3\\theta$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เอกลักษณ์พีทาโกรัส $\\sin^2\\theta + \\cos^2\\theta = 1$ ใช้ได้กับ $\\theta$ ทุกจำนวนจริง '
        'และเพราะบวกสลับที่กันได้ จะเขียนเป็น $\\cos^2\\theta + \\sin^2\\theta = 1$ ก็ค่าเท่ากัน',
        '• นิยามของแทนเจนต์คือ $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        'ให้จำภาพว่า<b>ไซน์อยู่ข้างบน</b> ส่วนโคแทนเจนต์กลับหัวกัน คือ '
        '$\\cot\\theta = \\dfrac{\\cos\\theta}{\\sin\\theta}$ สองตัวนี้ถูกหยิบสลับกันบ่อยมาก',
        '• การดึงตัวประกอบร่วม คือการอ่านผลบวกย้อนกลับให้กลายเป็นผลคูณ : '
        '$ab + ac = a\\left(b + c\\right)$ ใช้ได้เมื่อทุกพจน์มีก้อนเดียวกันคูณอยู่',
        '• กำลังสามแยกเป็นกำลังหนึ่งคูณกำลังสองได้เสมอ เช่น '
        '$\\sin^3\\theta = \\sin\\theta \\cdot \\sin^2\\theta$ การเขียนแบบนี้ทำให้เห็นก้อนร่วมชัดขึ้น',
        '• กฎการตัดเศษส่วนที่ต้องท่องให้ขึ้นใจ : ตัดได้เฉพาะก้อนที่<b>คูณ</b>กันอยู่ทั้งบนและล่าง '
        'และก้อนนั้นต้องไม่เป็นศูนย์ ⛔ ห้ามตัดพจน์ที่<b>บวก</b>กันอยู่เป็นอันขาด',
        '• เงื่อนไข $\\cos\\theta \\ne 0$ ที่โจทย์ให้ มีไว้สองหน้าที่ '
        'คือกันไม่ให้ตัวส่วนกลายเป็นศูนย์ และทำให้ $\\tan\\theta$ หาค่าได้จริง',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $\\theta$ เป็นจำนวนจริงที่ $\\cos\\theta \\ne 0$',
        '• นิพจน์ $\\dfrac{\\sin^3\\theta + \\sin\\theta\\cos^2\\theta}'
        '{\\cos^3\\theta + \\cos\\theta\\sin^2\\theta}$',
        '• สังเกตหน้าตาก่อนลงมือ : ตัวเศษเป็นผลบวกของสองพจน์ ตัวส่วนก็เป็นผลบวกของสองพจน์',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• ทำนิพจน์นี้ให้อยู่ในรูปอย่างง่ายที่สุด แล้วดูว่าตรงกับหน้าตาใด',
        '',
        '<b>【 ดึงตัวประกอบร่วมออกจากทั้งตัวเศษและตัวส่วน แล้วใช้เอกลักษณ์พีทาโกรัส'
        'ทำวงเล็บที่ได้ให้กลายเป็น $1$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · ดึงตัวประกอบร่วมที่ตัวเศษ</b>',
        '• ตัวเศษคือ $\\sin^3\\theta + \\sin\\theta\\cos^2\\theta$',
        '• เขียนพจน์แรกให้เห็นก้อนร่วมก่อน : $\\sin^3\\theta = \\sin\\theta \\cdot \\sin^2\\theta$ '
        'ส่วนพจน์หลังมี $\\sin\\theta$ ติดอยู่ข้างหน้าอยู่แล้ว',
        '• ทั้งสองพจน์จึงมี $\\sin\\theta$ ร่วมกัน ดึงออกนอกวงเล็บได้ '
        '$\\sin^3\\theta + \\sin\\theta\\cos^2\\theta '
        '= \\sin\\theta\\left(\\sin^2\\theta + \\cos^2\\theta\\right)$',
        '• ตรวจด้วยการกระจายกลับทุกครั้ง : ได้ $\\sin^3\\theta$ กับ $\\sin\\theta\\cos^2\\theta$ '
        'ครบทั้งสองพจน์ตามเดิม แสดงว่าดึงถูก',
        '',
        '<b>ขั้นที่ 2 · ดึงตัวประกอบร่วมที่ตัวส่วน</b>',
        '• ตัวส่วนคือ $\\cos^3\\theta + \\cos\\theta\\sin^2\\theta$ '
        'ทำแบบเดียวกับขั้นที่แล้ว เพียงสลับบทบาทของไซน์กับโคไซน์',
        '• $\\cos^3\\theta = \\cos\\theta \\cdot \\cos^2\\theta$ และพจน์หลังมี $\\cos\\theta$ '
        'ติดอยู่ข้างหน้าแล้ว ก้อนร่วมคราวนี้จึงเป็น $\\cos\\theta$',
        '• ดึงออกได้ $\\cos^3\\theta + \\cos\\theta\\sin^2\\theta '
        '= \\cos\\theta\\left(\\cos^2\\theta + \\sin^2\\theta\\right)$ '
        'กระจายกลับแล้วได้ของเดิมพอดีเช่นกัน',
        '',
        '<b>ขั้นที่ 3 · ใช้เอกลักษณ์พีทาโกรัส แล้วตัดก้อนที่คูณอยู่</b>',
        '• นำผลสองขั้นก่อนมาประกอบกลับเป็นเศษส่วนเดิม ได้ '
        '$\\dfrac{\\sin\\theta\\left(\\sin^2\\theta + \\cos^2\\theta\\right)}'
        '{\\cos\\theta\\left(\\cos^2\\theta + \\sin^2\\theta\\right)}$',
        '• วงเล็บข้างบนคือ $\\sin^2\\theta + \\cos^2\\theta$ เท่ากับ $1$ ตามเอกลักษณ์พีทาโกรัส',
        '• วงเล็บข้างล่างคือ $\\cos^2\\theta + \\sin^2\\theta$ ซึ่งเป็นก้อนเดียวกันเพียงสลับที่บวก '
        'จึงเท่ากับ $1$ เหมือนกัน วงเล็บบนกับล่างมีค่าเท่ากันเป๊ะ',
        '• เศษส่วนกลายเป็น $\\dfrac{\\sin\\theta \\cdot 1}{\\cos\\theta \\cdot 1}$ '
        'ตัดวงเล็บทั้งสองทิ้งได้ เพราะเป็นก้อนที่<b>คูณ</b>อยู่ทั้งบนและล่าง '
        'และมีค่าเป็น $1$ ซึ่งไม่เป็นศูนย์ การหารด้วยก้อนนี้จึงปลอดภัย',
        '• ตัวส่วนที่เหลือคือ $\\cos\\theta$ ซึ่งโจทย์รับประกันแล้วว่าไม่เป็นศูนย์ จึงหารได้จริง',
        '• เหลือ $\\dfrac{\\sin\\theta}{\\cos\\theta}$ ตรงกับนิยามของแทนเจนต์พอดี จึงได้ '
        '$\\dfrac{\\sin^3\\theta + \\sin\\theta\\cos^2\\theta}'
        '{\\cos^3\\theta + \\cos\\theta\\sin^2\\theta} = \\tan\\theta$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไม่ดึงตัวประกอบเลย แต่แทนค่ามุมจริงลงไปคิดเป็นตัวเลขสองมุม)</b>',
        '• แทน $\\theta = 45^{\\circ}$ ซึ่ง $\\sin 45^{\\circ} = \\cos 45^{\\circ} '
        '= \\dfrac{\\sqrt{2}}{2}$',
        '• ตัวเศษ $= \\left(\\dfrac{\\sqrt{2}}{2}\\right)^3 '
        '+ \\dfrac{\\sqrt{2}}{2}\\left(\\dfrac{\\sqrt{2}}{2}\\right)^2 '
        '= \\dfrac{\\sqrt{2}}{2} \\cdot 1$ และตัวส่วนคิดแบบเดียวกันได้ '
        '$\\dfrac{\\sqrt{2}}{2} \\cdot 1$ เท่ากันพอดี',
        '• อัตราส่วนจึงเป็น $1$ และ $\\tan 45^{\\circ} = 1$ ตรงกัน ✓',
        '• แทน $\\theta = 60^{\\circ}$ ซึ่ง $\\sin 60^{\\circ} = \\dfrac{\\sqrt{3}}{2}$ '
        'และ $\\cos 60^{\\circ} = \\dfrac{1}{2}$',
        '• ตัวเศษ $= \\dfrac{\\sqrt{3}}{2}\\left(\\dfrac{3}{4} + \\dfrac{1}{4}\\right) '
        '= \\dfrac{\\sqrt{3}}{2}$ และตัวส่วน '
        '$= \\dfrac{1}{2}\\left(\\dfrac{1}{4} + \\dfrac{3}{4}\\right) = \\dfrac{1}{2}$',
        '• อัตราส่วน $= \\dfrac{\\sqrt{3}}{2} \\div \\dfrac{1}{2} = \\sqrt{3}$ '
        'และ $\\tan 60^{\\circ} = \\sqrt{3}$ ตรงกันอีกครั้ง ✓',
        '• การแทนถึงสองมุมไม่ได้ทำเผื่อเล่น ๆ แต่ช่วยคัดคำตอบหลอกทิ้งได้จริง : ที่ $\\theta = '
        '60^{\\circ}$ ค่าที่ถูกคือ $\\sqrt{3}$ ขณะที่ $1$ ก็ดี $\\cot 60^{\\circ} '
        '= \\dfrac{1}{\\sqrt{3}}$ ก็ดี และ $\\tan^3 60^{\\circ} = 3\\sqrt{3}$ ก็ดี '
        'ล้วนต่างจาก $\\sqrt{3}$ ชัดเจน จึงตกไปทั้งหมด',
        '• ⛔ ข้อสังเกตสำคัญ : ถ้าแทนแค่ $\\theta = 45^{\\circ}$ มุมเดียวจะแยกไม่ออกเลย เพราะที่มุมนี้ '
        '$\\tan 45^{\\circ} = \\cot 45^{\\circ} = \\tan^3 45^{\\circ} = 1$ เท่ากันหมดทั้งสามค่า '
        'และยังพ้องกับค่าคงตัว $1$ อีกด้วย บทเรียนคือมุมที่ใช้ตรวจต้องไม่พิเศษเกินไป',
        '',
        '✅ <b>คำตอบ</b> $\\dfrac{\\sin^3\\theta + \\sin\\theta\\cos^2\\theta}'
        '{\\cos^3\\theta + \\cos\\theta\\sin^2\\theta} = \\tan\\theta$ → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอเศษส่วนตรีโกณที่ข้างบนและข้างล่างเป็น<b>ผลบวก</b>ของหลายพจน์ '
        'ให้มองหาตัวประกอบร่วมก่อนเสมอ อย่าเพิ่งตัดอะไรทิ้ง เพราะการตัดใช้ได้กับผลคูณเท่านั้น',
        '• ก้อน $\\sin^2\\theta + \\cos^2\\theta$ ชอบซ่อนอยู่ในวงเล็บที่เกิดหลังการดึงตัวประกอบ '
        'ถ้าดึงแล้วเห็นก้อนนี้โผล่มา แปลว่าเดินถูกทาง เพราะมันจะยุบเหลือ $1$ ทันที',
        '• เวลาตรวจด้วยการแทนมุม ให้เลี่ยงมุมที่พิเศษเกินไป เช่น $45^{\\circ}$ ซึ่งไซน์เท่ากับโคไซน์ '
        'ทำให้หลายคำตอบพ้องกันหมด ควรแทนสองมุม โดยมีมุมที่ค่าแยกกันชัด เช่น $60^{\\circ}$ ด้วย',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $\\tan^3\\theta$ เพราะเห็นพจน์ที่สองของตัวเศษคือ $\\sin\\theta\\cos^2\\theta$ '
        'กับพจน์ที่สองของตัวส่วนคือ $\\cos\\theta\\sin^2\\theta$ หน้าตาคล้ายกันมาก '
        '(มีทั้งไซน์และโคไซน์เหมือนกัน ต่างแค่ตัวไหนถูกยกกำลังสอง) จึงเข้าใจผิดว่า “ตัดทิ้งคู่กันได้” '
        'แล้วเหลือ $\\dfrac{\\sin^3\\theta}{\\cos^3\\theta} = \\tan^3\\theta$ · ทำแบบนั้นไม่ได้ '
        'ลองหารสองพจน์นั้นดูจริง ๆ จะได้ '
        '$\\dfrac{\\sin\\theta\\cos^2\\theta}{\\cos\\theta\\sin^2\\theta} = \\cot\\theta$ '
        'ซึ่งไม่ใช่ $1$ (ที่ $\\theta = 60^{\\circ}$ ค่านี้เป็น $\\dfrac{1}{\\sqrt{3}}$) '
        'สองพจน์นั้นจึงไม่หักล้างกัน · กฎที่ต้องท่องคือ'
        '<b>ตัดได้เฉพาะตัวประกอบที่คูณกันอยู่ ⛔ ห้ามตัดพจน์ที่บวกกันอยู่</b>',
        '• ได้ $\\cot\\theta$ เพราะเดินถูกทุกขั้นจนเหลือ $\\dfrac{\\sin\\theta}{\\cos\\theta}$ แล้ว '
        'แต่จำนิยามกลับหัว ไปเขียนว่า $\\tan\\theta = \\dfrac{\\cos\\theta}{\\sin\\theta}$ '
        'ซึ่งที่จริงเป็นนิยามของ $\\cot\\theta$ วิธีกันคือท่องให้ติดว่าแทนเจนต์มีไซน์อยู่<b>ข้างบน</b> '
        'แล้วตรวจซ้ำด้วยมุมจริง เช่นที่ $\\theta = 60^{\\circ}$ ได้ $\\dfrac{\\sin 60^{\\circ}}'
        '{\\cos 60^{\\circ}} = \\sqrt{3}$ ซึ่งคือ $\\tan 60^{\\circ}$ ไม่ใช่ $\\cot 60^{\\circ} '
        '= \\dfrac{1}{\\sqrt{3}}$',
        '• ได้ $1$ เพราะตัดวงเล็บที่เหมือนกันถูกต้องแล้ว แต่เผลอตัด $\\sin\\theta$ ที่อยู่หน้าวงเล็บ'
        'ข้างบน กับ $\\cos\\theta$ ที่อยู่หน้าวงเล็บข้างล่างทิ้งไปด้วย เหมือนคิดว่า '
        '“ข้างบนกับข้างล่างคล้ายกัน ก็ตัดหมดแล้วเหลือ $1$” ทั้งที่ $\\sin\\theta$ กับ $\\cos\\theta$ '
        'เป็นคนละก้อนกัน จะตัดได้ต้องเป็นก้อนที่<b>เหมือนกันเป๊ะ</b>เท่านั้น '
        'ตรวจง่าย ๆ ด้วย $\\theta = 60^{\\circ}$ ได้ค่า $\\sqrt{3}$ ซึ่งไม่ใช่ $1$',
    ],
    'V.mold: G = a rational trig expression whose numerator and denominator each factor into (single '
    'function) x (sin^2 + cos^2) / A = the equivalent simplified expression / M = factor the common single '
    'function out of both, apply the Pythagorean identity, cancel. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 with total at most 2, T = 0 and C = 0 -> level: ง่าย. '
    'F = 1 for the single knowledge block (the Pythagorean identity together with the tangent definition, '
    'which travel as one recall here). C = 0 because subtopic 7.4 alone answers it end to end. '
    'P = 1 and deliberately not 2: factoring the numerator and factoring the denominator are the same kind '
    'of move performed twice side by side, not two consecutive stages where the output of the first is the '
    'input of the second, so they count as one stage rather than a chain. The benchmark is q087, where '
    'P = 2 was earned by solving a linear system and then forming a ratio out of its output; nothing here '
    'has that dependency. T = 0 because spotting a common factor inside a sum of two terms is routine '
    'pattern work with no turning point, and L = 0 because the statement is pure symbols with no worded '
    'context, as every ง่าย item in this corpus must have. Scoring was written before the level was read '
    'off. '
    'sympy (verify_b17.py): trigsimp of (sin(t)**3 + sin(t)*cos(t)**2)/(cos(t)**3 + cos(t)*sin(t)**2) '
    'returns tan(theta) exactly, and independent numeric substitution at 45 and 60 degrees returns 1 and '
    'sqrt(3), matching tan of those angles. All three distractors machine-computed from named error paths: '
    'tan^3(theta) from cancelling the two second terms against each other, cot(theta) from writing the '
    'tangent definition upside down, and 1 from cancelling the leading sin(theta) and cos(theta) along with '
    'the identical brackets. The tan^3 path is provably an error and not a coincidence: sympy collapses '
    'sin*cos^2/(cos*sin^2) to cot(theta), not 1, so those two terms genuinely do not cancel. '
    'Collision sweep on 6402 items (bank 62 files + k1 out + k2 out), probe collide_b17c.py: scan N2d '
    '(fractions whose numerator opens with sin^3 or cos^3 in the question text) returns 0 items corpus-wide, '
    'and scan N2e (questions carrying both sin^3 and cos^2) returns exactly 1 item, pat1-2557-03-q11, which '
    'is an unrelated mold. Choices are ordered by the symbol rule (constant first, then single functions by '
    'name, then higher powers), so the answer slot is forced by that rule and was not chosen.',
)

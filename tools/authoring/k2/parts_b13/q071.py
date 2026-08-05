# -*- coding: utf-8 -*-
add(
    71,
    ['7.1'],
    'ง่าย',
    'ค่าของ $\\dfrac{\\sin^2 \\dfrac{\\pi}{6} + \\tan^2 \\dfrac{\\pi}{3}}{\\cos^2 \\dfrac{\\pi}{4}}$ '
    'เท่ากับข้อใด',
    [
        '$7$',
        '$\\dfrac{7}{6}$',
        '$\\dfrac{13}{8}$',
        '$\\dfrac{13}{2}$',
    ],
    3,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ค่าของอัตราส่วนตรีโกณมิติที่มุมพิเศษซึ่งต้องจำให้แม่น : '
        '$\\sin \\dfrac{\\pi}{6} = \\dfrac{1}{2}$ , $\\cos \\dfrac{\\pi}{4} = \\dfrac{\\sqrt{2}}{2}$ '
        'และ $\\tan \\dfrac{\\pi}{3} = \\sqrt{3}$',
        '• สัญลักษณ์ $\\sin^2 \\theta$ หมายถึง $(\\sin \\theta)^2$ นั่นคือหาค่าของฟังก์ชันก่อนแล้วจึงยกกำลังสอง '
        '⛔ ไม่ใช่การยกกำลังสองให้มุมก่อน',
        '• มุมในหน่วยเรเดียนที่ตรงกับมุมพิเศษ : $\\dfrac{\\pi}{6}$ คือ $30^{\\circ}$ , '
        '$\\dfrac{\\pi}{4}$ คือ $45^{\\circ}$ และ $\\dfrac{\\pi}{3}$ คือ $60^{\\circ}$',
        '• การหารด้วยเศษส่วน ทำได้โดยคูณด้วยส่วนกลับของตัวหาร',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• นิพจน์ $\\dfrac{\\sin^2 \\dfrac{\\pi}{6} + \\tan^2 \\dfrac{\\pi}{3}}{\\cos^2 \\dfrac{\\pi}{4}}$',
        '• ทุกมุมที่ปรากฏเป็นมุมพิเศษที่ทราบค่าแน่นอน',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของนิพจน์นี้ในรูปจำนวนตรรกยะ',
        '',
        '<b>【 หาค่าของแต่ละก้อนแยกกันให้ครบก่อน แล้วจึงประกอบกลับเข้าเป็นเศษส่วนเดียว 】</b>',
        '',
        '<b>ขั้นที่ 1 · หาค่าของแต่ละพจน์ในตัวเศษ</b>',
        '• พจน์แรก : $\\sin \\dfrac{\\pi}{6} = \\dfrac{1}{2}$ '
        'จากนั้นจึงยกกำลังสอง ได้ $\\sin^2 \\dfrac{\\pi}{6} = \\left(\\dfrac{1}{2}\\right)^2 = \\dfrac{1}{4}$',
        '• พจน์ที่สอง : $\\tan \\dfrac{\\pi}{3} = \\sqrt{3}$ '
        'จากนั้นจึงยกกำลังสอง ได้ $\\tan^2 \\dfrac{\\pi}{3} = (\\sqrt{3})^2 = 3$',
        '• รวมตัวเศษ : $\\dfrac{1}{4} + 3 = \\dfrac{1}{4} + \\dfrac{12}{4} = \\dfrac{13}{4}$',
        '',
        '<b>ขั้นที่ 2 · หาค่าของตัวส่วน</b>',
        '• $\\cos \\dfrac{\\pi}{4} = \\dfrac{\\sqrt{2}}{2}$',
        '• ยกกำลังสอง : $\\cos^2 \\dfrac{\\pi}{4} = \\left(\\dfrac{\\sqrt{2}}{2}\\right)^2 = '
        '\\dfrac{2}{4} = \\dfrac{1}{2}$',
        '',
        '<b>ขั้นที่ 3 · ประกอบกลับเข้าเป็นเศษส่วนเดียวแล้วยุบ</b>',
        '• นำตัวเศษหารด้วยตัวส่วน : $\\dfrac{13}{4} \\div \\dfrac{1}{2}$',
        '• การหารด้วยเศษส่วน ทำได้โดยคูณด้วยส่วนกลับ : $\\dfrac{13}{4} \\times \\dfrac{2}{1} = \\dfrac{26}{4}$',
        '• ยุบเศษส่วนให้เป็นอย่างต่ำ : $\\dfrac{26}{4} = \\dfrac{13}{2}$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ใช้เอกลักษณ์เซแคนต์แทนการเปิดตารางค่ามุมพิเศษ)</b>',
        '• แทนที่จะจำค่า $\\tan \\dfrac{\\pi}{3}$ ใช้เอกลักษณ์ $\\tan^2 \\theta = \\sec^2 \\theta - 1$ '
        'โดยที่ $\\sec \\dfrac{\\pi}{3} = 2$ จึงได้ $\\tan^2 \\dfrac{\\pi}{3} = 2^2 - 1 = 3$',
        '• แทนที่จะหารด้วย $\\cos^2 \\dfrac{\\pi}{4}$ ให้มองเป็นการคูณด้วย '
        '$\\sec^2 \\dfrac{\\pi}{4} = (\\sqrt{2})^2 = 2$',
        '• นิพจน์จึงกลายเป็น $\\left(\\dfrac{1}{4} + 3\\right) \\times 2 = \\dfrac{13}{4} \\times 2 = \\dfrac{13}{2}$',
        '• ลองตรวจด้วยทศนิยมอีกชั้น : ตัวเศษ $= 0.25 + 3 = 3.25$ และตัวส่วน $= 0.5$ '
        'จะได้ $3.25 \\div 0.5 = 6.5$ ซึ่งเท่ากับ $\\dfrac{13}{2}$ พอดี',
        '',
        '✅ <b>คำตอบ</b> $\\dfrac{13}{2}$ → <b>ตัวเลือก 4</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เมื่อเห็นตัวส่วนเป็นกำลังสองของ $\\cos$ หรือ $\\sin$ ให้เปลี่ยนการหารเป็นการคูณด้วย '
        '$\\sec^2$ หรือ $\\csc^2$ ทันที จะไม่ต้องจัดการเศษส่วนซ้อนเศษส่วนเลย',
        '• ประมาณคำตอบไว้ก่อนกันพลาด : $\\tan^2 \\dfrac{\\pi}{3} = 3$ เพียงพจน์เดียวก็มากกว่า $3$ แล้ว '
        'และการหารด้วย $\\dfrac{1}{2}$ คือการคูณสอง คำตอบจึงต้องมากกว่า $6$ แน่นอน',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $7$ เพราะลืมยกกำลังสองให้ $\\sin \\dfrac{\\pi}{6}$ กลายเป็นคิดตัวเศษว่า '
        '$\\dfrac{1}{2} + 3 = \\dfrac{7}{2}$ แล้วหารด้วย $\\dfrac{1}{2}$ ได้ $7$ '
        'ให้ระวังว่าเลขยกกำลังเขียนไว้ที่ชื่อฟังก์ชัน แต่มีผลกับค่าของฟังก์ชัน',
        '• ได้ $\\dfrac{7}{6}$ เพราะจำค่าสลับกัน ใช้ $\\tan \\dfrac{\\pi}{3} = \\dfrac{1}{\\sqrt{3}}$ '
        'ซึ่งที่จริงเป็นค่าของ $\\tan \\dfrac{\\pi}{6}$ ทำให้ตัวเศษกลายเป็น '
        '$\\dfrac{1}{4} + \\dfrac{1}{3} = \\dfrac{7}{12}$ ให้จำว่ามุมยิ่งใหญ่ค่าแทนเจนต์ยิ่งมาก '
        'มุม $60^{\\circ}$ จึงต้องได้ค่ามากกว่า $1$',
        '• ได้ $\\dfrac{13}{8}$ เพราะนำ $\\cos^2 \\dfrac{\\pi}{4} = \\dfrac{1}{2}$ ไปคูณแทนที่จะหาร '
        'ได้ $\\dfrac{13}{4} \\times \\dfrac{1}{2}$ การเปลี่ยนหารเป็นคูณต้องใช้ส่วนกลับของตัวหารเสมอ '
        'ไม่ใช่ตัวหารเดิม',
    ],
    'V.mold: G = a purely symbolic expression built only from special-angle values written in radian form '
    '(pi/6, pi/3, pi/4), each squared / A = the numeric value of the expression / M = evaluate each special-angle '
    'value first, square it, combine the numerator, then divide by the denominator using the reciprocal rule. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 -> level: ง่าย. sympy (verify_b13.py): route 1 evaluates the three special '
    'values and returns 13/2; route 2 is independent of the tangent and cosine tables — it rewrites tan^2 as '
    'sec^2 - 1 and the division as multiplication by sec^2(pi/4), returning 13/2 again. All three distractors '
    'machine-computed from named error paths: 7 from dropping the square on sin(pi/6), 7/6 from swapping '
    'tan(pi/3) with tan(pi/6), 13/8 from multiplying by cos^2(pi/4) instead of dividing. A guard asserts that '
    'the estimation bound quoted in the เทคนิค block (the answer must exceed 6) kills exactly one distractor '
    'and not all three, so the item cannot be answered by the bound alone. Collision sweep on 6382 items '
    '(bank 62 files + k1 + k2 out): the shape of three distinct squared trigonometric functions at three '
    'distinct special angles written in radians, arranged as a single fraction, returns 0 hits; the literal '
    'value 13/2 as an answer to a trigonometric expression returns 0 hits. Redesign history: draft 1 used '
    'degrees rather than radians and matched the surface of several bank items in chapter 7 too closely, so '
    'the whole expression was rewritten in radian form, which also makes the item carry its own reminder that '
    'pi/3 and pi/6 are not interchangeable — the exact confusion that distractor 2 is built from.',
)

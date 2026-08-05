# -*- coding: utf-8 -*-
add(
    87,
    ['7.5', '7.4'],
    'ปานกลาง',
    'กำหนดให้ $A$ และ $B$ เป็นจำนวนจริงซึ่ง $\\cos(A + B) = \\dfrac{3}{5}$ '
    'และ $\\cos(A - B) = \\dfrac{4}{5}$ '
    'โดยที่ $\\cos A \\cos B \\ne 0$ แล้ว $\\tan A \\tan B$ มีค่าเท่ากับข้อใด',
    [
        '$-\\dfrac{1}{7}$',
        '$\\dfrac{1}{7}$',
        '$\\dfrac{1}{5}$',
        '$7$',
    ],
    1,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• สูตรผลต่างมุมของโคไซน์ : $\\cos(A - B) = \\cos A \\cos B + \\sin A \\sin B$',
        '• สูตรผลบวกมุมของโคไซน์ : $\\cos(A + B) = \\cos A \\cos B - \\sin A \\sin B$',
        '• วิธีจำเครื่องหมาย : ฝั่งซ้ายเป็นผล<b>บวก</b>มุม ฝั่งขวาจะเป็นผล<b>ลบ</b> คือสลับกันเสมอ '
        'และทั้งสองสูตรขึ้นต้นด้วยก้อน $\\cos A \\cos B$ เหมือนกัน ต่างกันแค่เครื่องหมายหน้าก้อนไซน์',
        '• นิยามแทนเจนต์ : $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        'เมื่อ $\\cos\\theta \\ne 0$ ดังนั้น '
        '$\\tan A \\tan B = \\dfrac{\\sin A \\sin B}{\\cos A \\cos B}$',
        '• เทคนิคเชิงโครงสร้างที่ใช้บ่อย : ถ้ามีสองสมการที่ต่างกันเพียงเครื่องหมายของก้อนหนึ่ง '
        'การนำสมการทั้งสองมาบวกกันจะทำให้ก้อนนั้นหายไป และการนำมาลบกันจะทำให้อีกก้อนหนึ่งหายไป '
        'เท่ากับแยกก้อนสองก้อนออกจากกันได้ทันทีโดยไม่ต้องรู้ค่า $A$ หรือ $B$ เลย',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $\\cos(A + B) = \\dfrac{3}{5}$',
        '• $\\cos(A - B) = \\dfrac{4}{5}$',
        '• $\\cos A \\cos B \\ne 0$ จึงเขียน $\\tan A$ และ $\\tan B$ ได้',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\tan A \\tan B$',
        '',
        '<b>【 อย่าหาค่า A กับ B แยกกัน แต่ให้มองก้อน cos A cos B กับ sin A sin B '
        'เป็นตัวแปรสองตัว แล้วบวก-ลบสองสมการเพื่อแยกก้อนออกจากกัน 】</b>',
        '',
        '<b>ขั้นที่ 1 · กางสูตรทั้งสองให้เป็นระบบสมการสองตัวแปร</b>',
        '• ตั้งชื่อก้อนเพื่อไม่ให้ตาลาย ให้ $p = \\cos A \\cos B$ และ $q = \\sin A \\sin B$',
        '• จากสูตรผลบวกมุม : $\\cos(A + B) = p - q$ ดังนั้น $p - q = \\dfrac{3}{5}$',
        '• จากสูตรผลต่างมุม : $\\cos(A - B) = p + q$ ดังนั้น $p + q = \\dfrac{4}{5}$',
        '• จุดสำคัญคือสองสมการนี้มีตัวแปรแค่ $p$ กับ $q$ เท่านั้น '
        '⛔ ไม่ต้องรู้ค่า $A$ หรือ $B$ เลย และการพยายามถอด $A$ กับ $B$ ออกมาเป็นมุมจริง ๆ '
        'ด้วยอาร์กโคไซน์จะทำให้งานยาวขึ้นโดยไม่จำเป็น',
        '',
        '<b>ขั้นที่ 2 · บวกและลบสองสมการเพื่อแยก $p$ กับ $q$</b>',
        '• นำสองสมการมาบวกกัน ก้อน $q$ จะตัดกันหมด ได้ '
        '$(p - q) + (p + q) = \\dfrac{3}{5} + \\dfrac{4}{5}$ นั่นคือ $2p = \\dfrac{7}{5}$',
        '• ดังนั้น $p = \\dfrac{7}{10}$ นั่นคือ $\\cos A \\cos B = \\dfrac{7}{10}$',
        '• นำสมการที่สองลบด้วยสมการแรก ก้อน $p$ จะตัดกันหมด ได้ '
        '$(p + q) - (p - q) = \\dfrac{4}{5} - \\dfrac{3}{5}$ นั่นคือ $2q = \\dfrac{1}{5}$',
        '• ดังนั้น $q = \\dfrac{1}{10}$ นั่นคือ $\\sin A \\sin B = \\dfrac{1}{10}$',
        '• ⚠️ ระวังลำดับการลบให้ดี ต้องเอาสมการของผล<b>ต่าง</b>มุมเป็นตัวตั้ง เพราะสมการนั้นคือ '
        '$p + q$ ถ้าสลับตัวตั้งจะได้ $q$ ติดลบ ซึ่งจะพาไปสู่คำตอบที่ผิดเครื่องหมาย',
        '',
        '<b>ขั้นที่ 3 · ประกอบกลับเป็น $\\tan A \\tan B$</b>',
        '• จากนิยามแทนเจนต์ '
        '$\\tan A \\tan B = \\dfrac{\\sin A}{\\cos A} \\cdot \\dfrac{\\sin B}{\\cos B} '
        '= \\dfrac{\\sin A \\sin B}{\\cos A \\cos B} = \\dfrac{q}{p}$',
        '• แทนค่า : $\\dfrac{q}{p} = \\dfrac{\\ \\dfrac{1}{10}\\ }{\\ \\dfrac{7}{10}\\ } '
        '= \\dfrac{1}{10} \\times \\dfrac{10}{7} = \\dfrac{1}{7}$',
        '• สังเกตว่าตัวส่วน $10$ ตัดกันพอดี เหลือเพียงอัตราส่วนของตัวเศษ '
        'จึงได้ $\\tan A \\tan B = \\dfrac{1}{7}$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · สร้างมุมจริงคู่หนึ่งที่สอดคล้องกับโจทย์ '
        'แล้วคูณแทนเจนต์ตรง ๆ)</b>',
        '• ลองเสนอมุมคู่หนึ่งคือ $A = \\dfrac{\\pi}{4}$ และ $B = \\arctan\\dfrac{1}{7}$ '
        'แล้วตรวจว่าสอดคล้องกับเงื่อนไขที่โจทย์ให้จริงหรือไม่',
        '• จาก $\\tan B = \\dfrac{1}{7}$ ได้สามเหลี่ยมมุมฉากที่ด้านตรงข้ามยาว $1$ '
        'ด้านประชิดยาว $7$ ด้านตรงข้ามมุมฉากจึงยาว $\\sqrt{1 + 49} = \\sqrt{50} = 5\\sqrt{2}$ '
        'ดังนั้น $\\sin B = \\dfrac{1}{5\\sqrt{2}}$ และ $\\cos B = \\dfrac{7}{5\\sqrt{2}}$',
        '• และ $\\sin A = \\cos A = \\dfrac{\\sqrt{2}}{2}$',
        '• ตรวจเงื่อนไขแรก : $\\cos(A + B) = \\cos A \\cos B - \\sin A \\sin B '
        '= \\dfrac{\\sqrt{2}}{2}\\cdot\\dfrac{7}{5\\sqrt{2}} '
        '- \\dfrac{\\sqrt{2}}{2}\\cdot\\dfrac{1}{5\\sqrt{2}} '
        '= \\dfrac{7}{10} - \\dfrac{1}{10} = \\dfrac{6}{10} = \\dfrac{3}{5}$ ✔ ตรง',
        '• ตรวจเงื่อนไขที่สอง : $\\cos(A - B) = \\dfrac{7}{10} + \\dfrac{1}{10} '
        '= \\dfrac{8}{10} = \\dfrac{4}{5}$ ✔ ตรง',
        '• เมื่อมุมคู่นี้ใช้ได้จริง ก็คูณแทนเจนต์ได้ตรง ๆ '
        '$\\tan A \\tan B = 1 \\times \\dfrac{1}{7} = \\dfrac{1}{7}$ ตรงกับวิธีแรก',
        '',
        '✅ <b>คำตอบ</b> $\\tan A \\tan B = \\dfrac{1}{7}$ → <b>ตัวเลือก 2</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เห็นคู่ $\\cos(A+B)$ กับ $\\cos(A-B)$ มาพร้อมกันเมื่อไร ให้คิดถึงการบวกและลบสองสมการทันที '
        'เพราะสองสูตรนี้ต่างกันแค่เครื่องหมายของก้อนไซน์ การบวกจะได้ '
        '$\\cos A \\cos B$ และการลบจะได้ $\\sin A \\sin B$ '
        'คู่ $\\sin(A+B)$ กับ $\\sin(A-B)$ ก็ใช้กลไกเดียวกันแต่จะได้ '
        '$\\sin A \\cos B$ กับ $\\cos A \\sin B$ แทน',
        '• เมื่อโจทย์ถามค่าที่เป็น<b>อัตราส่วน</b>ของสองก้อน ให้เดาไว้ก่อนว่าไม่ต้องหาค่ามุมจริง '
        'เพราะตัวส่วนที่เหมือนกันมักตัดกันหมด ข้อนี้ทั้ง $p$ และ $q$ มีตัวส่วน $10$ เท่ากัน '
        'จึงเหลือแค่ $1$ ต่อ $7$',
        '• ตั้งชื่อก้อนใหญ่เป็นตัวแปรตัวเดียว เช่น $p$ กับ $q$ ช่วยลดความผิดพลาดได้มาก '
        'เพราะเปลี่ยนโจทย์ตรีโกณให้กลายเป็นระบบสมการเชิงเส้นธรรมดาที่คุ้นมือตั้งแต่ ม.ต้น',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $-\\dfrac{1}{7}$ เพราะจำเครื่องหมายของสองสูตรสลับกัน คือไปตั้งว่า '
        '$\\cos(A + B) = p + q$ และ $\\cos(A - B) = p - q$ '
        'ผลคือ $q = -\\dfrac{1}{10}$ แล้วอัตราส่วนติดลบตามไปด้วย '
        'วิธีกันแบบเร็วคือแทนค่าง่าย ๆ ตรวจสูตรก่อนใช้ เช่นให้ $A = B = \\dfrac{\\pi}{2}$ '
        'จะได้ $\\cos(A+B) = \\cos\\pi = -1$ ส่วน $p - q = 0 - 1 = -1$ ตรงกัน '
        'แต่ $p + q = 1$ ไม่ตรง จึงยืนยันว่าผลบวกมุมต้องคู่กับเครื่องหมายลบ',
        '• ได้ $\\dfrac{1}{5}$ เพราะนำสองค่าที่โจทย์ให้มาลบกันแล้วตอบค่านั้นทันที '
        'คือคิดว่า $\\dfrac{4}{5} - \\dfrac{3}{5} = \\dfrac{1}{5}$ คือคำตอบ '
        'ค่านี้ที่จริงคือ $2\\sin A \\sin B$ ยังไม่ได้หารสอง และยังไม่ได้หารด้วย $\\cos A \\cos B$ '
        'ให้ย้ำกับตัวเองว่าโจทย์ถามหา<b>อัตราส่วน</b> ไม่ได้ถามหาผลต่าง',
        '• ได้ $7$ เพราะหารกลับหัว คือคิด $\\dfrac{p}{q}$ แทน $\\dfrac{q}{p}$ '
        'ต้นเหตุคือลืมว่าแทนเจนต์มีไซน์อยู่<b>ข้างบน</b> '
        'ให้ตรวจด้วยความรู้สึกเชิงขนาด ก้อนโคไซน์ $\\dfrac{7}{10}$ ใหญ่กว่าก้อนไซน์ $\\dfrac{1}{10}$ '
        'มาก ผลคูณของแทนเจนต์จึงต้องเป็นจำนวนที่<b>น้อยกว่า</b> $1$ ไม่ใช่มากกว่า',
    ],
    'V.mold: G = the two values cos(A+B) and cos(A-B) given as data, with no individual angle available / '
    'A = the value of the product tan A tan B / M = name the two products cos A cos B and sin A sin B as a '
    'pair of unknowns, add and subtract the two given equations to split them, then form the ratio. '
    'Rubric F2 C2 P2 T1 L0 = 7/15 with total in 3..7 and T <= 2 -> level: ปานกลาง. '
    'F = 2 for the two knowledge blocks (the sum-and-difference cosine formulas, and the tangent definition '
    'as a ratio). C = 2 because 7.5 supplies the expansion and 7.4 supplies the identity rewriting of the '
    'product of tangents; the item is not answerable from either alone. P = 2 for the two-stage chain '
    '(solve the linear system, then form the ratio). T = 1 for the single genuine key: seeing that the pair '
    'of givens should be treated as a linear system in two composite unknowns rather than solved for A and '
    'B individually. L = 0 because the statement is pure symbols with no worded context at all. '
    'sympy (verify_b16.py): (4/5 + 3/5)/2 simplifies to 7/10 and (4/5 - 3/5)/2 to 1/10, whose quotient is '
    'exactly 1/7. Two independent paths confirm it: a numeric path taking A = (acos(3/5) + acos(4/5))/2 and '
    'B = (acos(3/5) - acos(4/5))/2 and multiplying the tangents returns 0.142857142857143 and reproduces '
    'both givens to 1e-12; and a symbolic witness path with A = pi/4, B = atan(1/7) where sympy simplifies '
    'cos(A+B) to exactly 3/5, cos(A-B) to exactly 4/5 and tan A tan B to exactly 1/7. All three distractors '
    'machine-computed from named error paths: -1/7 from swapping the sign convention of the two formulas, '
    '1/5 from subtracting the two givens and stopping, and 7 from inverting the ratio. '
    'Collision sweep on 6397 items (bank 62 files + k1 out + k2 out), probe collide_b16.py round 3: only '
    'one item pairs cos(A+B) with cos(A-B) as simultaneous data, chap-07-trigonometry-q108, and its G is a '
    'triangle with stated side lengths rather than two bare cosine values, so G differs; a second probe for '
    'items asking specifically for a product of tangents returned zero hits in the whole corpus. The '
    'saturated sum-and-difference molds are the auxiliary-angle family a sin x + b cos x = c at 80 items '
    'and the double-angle-forward family at 25 items; this item is neither, since nothing here is an '
    'equation to be solved.',
)

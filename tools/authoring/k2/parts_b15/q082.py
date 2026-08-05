# -*- coding: utf-8 -*-
add(
    82,
    ['7.5', '7.1'],
    'ปานกลาง',
    'กำหนดให้ $A$ และ $B$ เป็นมุมแหลม โดยที่ $\\tan(A + B) = 3$ และ '
    '$\\tan A = \\dfrac{1}{2}$ แล้วค่าของ $\\sin B$ เท่ากับข้อใด',
    [
        '$-\\dfrac{\\sqrt{2}}{2}$',
        '$\\dfrac{\\sqrt{2}}{2}$',
        '$\\dfrac{5\\sqrt{29}}{29}$',
        '$\\dfrac{5\\sqrt{26}}{26}$',
    ],
    1,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• สูตรผลต่างมุมของแทนเจนต์ : '
        '$\\tan(X - Y) = \\dfrac{\\tan X - \\tan Y}{1 + \\tan X \\tan Y}$ '
        'ให้สังเกตว่าตัวเศษใช้เครื่องหมายลบตามชื่อสูตร แต่ตัวส่วนใช้เครื่องหมายบวก ซึ่งกลับกัน',
        '• สูตรผลบวกมุมของแทนเจนต์ : '
        '$\\tan(X + Y) = \\dfrac{\\tan X + \\tan Y}{1 - \\tan X \\tan Y}$ '
        'ซึ่งตัวเศษบวกและตัวส่วนลบ กลับกันกับสูตรผลต่างพอดี',
        '• เมื่อรู้ค่าแทนเจนต์ของมุมแหลม สามารถสร้างสามเหลี่ยมมุมฉากที่มีด้านตรงข้ามมุมยาวเท่ากับตัวเศษ '
        'และด้านประชิดมุมยาวเท่ากับตัวส่วน แล้วใช้ทฤษฎีบทพีทาโกรัสหาด้านตรงข้ามมุมฉาก '
        'จากนั้นอ่านค่าไซน์และโคไซน์ออกมาได้ทันที',
        '• มุมแหลมคือมุมที่อยู่ระหว่าง $0$ กับ $\\dfrac{\\pi}{2}$ '
        'อัตราส่วนตรีโกณมิติทุกตัวของมุมแหลมมีค่าเป็นบวกทั้งหมด',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $A$ และ $B$ เป็นมุมแหลมทั้งคู่',
        '• $\\tan(A + B) = 3$',
        '• $\\tan A = \\dfrac{1}{2}$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\sin B$',
        '',
        '<b>【 มอง $B$ เป็นผลต่าง $(A + B) - A$ เพื่อใช้ของที่โจทย์ให้ทั้งสองอย่างพร้อมกัน '
        'แล้วเปลี่ยนแทนเจนต์เป็นไซน์ด้วยสามเหลี่ยมมุมฉาก 】</b>',
        '',
        '<b>ขั้นที่ 1 · เขียนมุมที่ต้องการให้อยู่ในรูปของมุมที่รู้ค่าแล้ว</b>',
        '• โจทย์ให้ค่าแทนเจนต์ของมุม $A + B$ กับของมุม $A$ แต่ถามเรื่องของมุม $B$ เพียงมุมเดียว',
        '• เขียนมุม $B$ ใหม่โดยไม่เปลี่ยนค่า : $B = (A + B) - A$ '
        'การเขียนแบบนี้ทำให้ทั้งสองสิ่งที่โจทย์ให้ถูกใช้พร้อมกันในสูตรเดียว',
        '• ⛔ ห้ามเดาว่า $\\tan B = \\tan(A + B) - \\tan A$ '
        'เพราะแทนเจนต์ไม่ใช่ฟังก์ชันที่กระจายผ่านการลบได้',
        '',
        '<b>ขั้นที่ 2 · ใช้สูตรผลต่างมุมของแทนเจนต์</b>',
        '• จากสูตร โดยให้ $X = A + B$ และ $Y = A$ : '
        '$\\tan B = \\dfrac{\\tan(A + B) - \\tan A}{1 + \\tan(A + B)\\tan A}$',
        '• แทนค่าที่โจทย์ให้ : '
        '$\\tan B = \\dfrac{3 - \\dfrac{1}{2}}{1 + 3 \\times \\dfrac{1}{2}}$',
        '• คิดตัวเศษ : $3 - \\dfrac{1}{2} = \\dfrac{6}{2} - \\dfrac{1}{2} = \\dfrac{5}{2}$',
        '• คิดตัวส่วน : $1 + \\dfrac{3}{2} = \\dfrac{2}{2} + \\dfrac{3}{2} = \\dfrac{5}{2}$',
        '• หารกัน : $\\tan B = \\dfrac{\\ \\dfrac{5}{2}\\ }{\\ \\dfrac{5}{2}\\ } = 1$',
        '',
        '<b>ขั้นที่ 3 · เปลี่ยนจากแทนเจนต์เป็นไซน์</b>',
        '• สร้างสามเหลี่ยมมุมฉากของมุม $B$ จาก $\\tan B = \\dfrac{1}{1}$ '
        'โดยให้ด้านตรงข้ามมุม $B$ ยาว $1$ หน่วย และด้านประชิดมุม $B$ ยาว $1$ หน่วย',
        '• หาด้านตรงข้ามมุมฉากด้วยทฤษฎีบทพีทาโกรัส : '
        '$\\sqrt{1^2 + 1^2} = \\sqrt{2}$',
        '• อ่านค่าไซน์จากนิยาม : '
        '$\\sin B = \\dfrac{1}{\\sqrt{2}} = \\dfrac{\\sqrt{2}}{2}$',
        '',
        '<b>ขั้นที่ 4 · ตรวจว่าคำตอบสอดคล้องกับเงื่อนไขมุมแหลม</b>',
        '• $\\tan B = 1$ ให้มุม $B$ ที่เป็นมุมแหลมคือ $\\dfrac{\\pi}{4}$ '
        'ซึ่งอยู่ในเงื่อนไขที่โจทย์กำหนดจริง',
        '• ค่า $\\sin B = \\dfrac{\\sqrt{2}}{2}$ มีค่าประมาณ $0.707$ '
        'เป็นจำนวนบวกที่ไม่เกิน $1$ จึงเป็นค่าไซน์ที่เป็นไปได้ของมุมแหลม',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไม่ใช้สูตรผลต่างของแทนเจนต์เลย '
        'แต่สร้างสามเหลี่ยมของมุม $A$ กับมุม $A + B$ แล้วใช้สูตรผลต่างของไซน์)</b>',
        '• จาก $\\tan A = \\dfrac{1}{2}$ และ $A$ เป็นมุมแหลม สร้างสามเหลี่ยมด้าน $1$ กับ $2$ '
        'ได้ด้านตรงข้ามมุมฉากยาว $\\sqrt{5}$ จึงได้ '
        '$\\sin A = \\dfrac{1}{\\sqrt{5}}$ และ $\\cos A = \\dfrac{2}{\\sqrt{5}}$',
        '• จาก $\\tan(A + B) = 3 = \\dfrac{3}{1}$ สร้างสามเหลี่ยมด้าน $3$ กับ $1$ '
        'ได้ด้านตรงข้ามมุมฉากยาว $\\sqrt{10}$ '
        'และเนื่องจากแทนเจนต์เป็นบวกและมุมผลรวมของมุมแหลมสองมุมที่มีแทนเจนต์เป็นบวกต้องเป็นมุมแหลม '
        'จึงได้ $\\sin(A + B) = \\dfrac{3}{\\sqrt{10}}$ และ $\\cos(A + B) = \\dfrac{1}{\\sqrt{10}}$',
        '• ใช้สูตรผลต่างของไซน์กับ $B = (A + B) - A$ : '
        '$\\sin B = \\sin(A + B)\\cos A - \\cos(A + B)\\sin A$',
        '• แทนค่า : '
        '$\\sin B = \\dfrac{3}{\\sqrt{10}} \\times \\dfrac{2}{\\sqrt{5}} - '
        '\\dfrac{1}{\\sqrt{10}} \\times \\dfrac{1}{\\sqrt{5}} '
        '= \\dfrac{6}{\\sqrt{50}} - \\dfrac{1}{\\sqrt{50}} = \\dfrac{5}{\\sqrt{50}}$',
        '• ยุบราก : $\\sqrt{50} = 5\\sqrt{2}$ ดังนั้น '
        '$\\sin B = \\dfrac{5}{5\\sqrt{2}} = \\dfrac{1}{\\sqrt{2}} = \\dfrac{\\sqrt{2}}{2}$',
        '• เส้นทางนี้ไม่ได้แตะสูตรผลต่างของแทนเจนต์เลย แต่ได้ค่าเดียวกัน จึงยืนยันว่าคำตอบถูกต้อง',
        '',
        '✅ <b>คำตอบ</b> $\\dfrac{\\sqrt{2}}{2}$ → <b>ตัวเลือก 2</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอโจทย์ที่ให้ค่าของ “มุมรวม” กับ “มุมหนึ่ง” แล้วถามอีกมุมหนึ่ง '
        'ให้เขียนมุมที่ถามเป็นผลต่างทันที เช่น $B = (A + B) - A$ '
        'เทคนิคนี้ใช้ได้กับทุกฟังก์ชันตรีโกณ ไม่เฉพาะแทนเจนต์',
        '• วิธีจำเครื่องหมายของสูตรแทนเจนต์คือจำว่า “เศษตามชื่อ ส่วนตรงข้าม” '
        'สูตรผลบวกมีเศษบวกและส่วนลบ ส่วนสูตรผลต่างมีเศษลบและส่วนบวก '
        'ถ้าจำสลับ ตัวส่วนของข้อนี้จะกลายเป็น $1 - \\dfrac{3}{2} = -\\dfrac{1}{2}$ '
        'แล้วได้ $\\tan B = -5$ ซึ่งขัดกับเงื่อนไขว่า $B$ เป็นมุมแหลมทันที',
        '• ใช้เงื่อนไขมุมแหลมเป็นเครื่องคัดคำตอบ ค่าไซน์ของมุมแหลมต้องเป็นบวกเสมอ '
        'ค่าใดที่ติดลบตัดทิ้งได้ทันทีโดยไม่ต้องคำนวณต่อ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $-\\dfrac{\\sqrt{2}}{2}$ เพราะสลับลำดับการลบในสูตร '
        'ไปเขียนเป็น $\\dfrac{\\tan A - \\tan(A + B)}{1 + \\tan A \\tan(A + B)}$ '
        'ซึ่งเป็นสูตรของมุม $A - (A + B)$ นั่นคือมุม $-B$ '
        'จึงได้ $\\tan(-B) = -1$ แล้วอ่านออกมาเป็นไซน์ติดลบ '
        'ให้เขียนบรรทัด $B = (A + B) - A$ ลงกระดาษก่อนแทนสูตรทุกครั้ง',
        '• ได้ $\\dfrac{5\\sqrt{29}}{29}$ เพราะกระจายแทนเจนต์ผ่านการลบ '
        'คือคิดว่า $\\tan B = \\tan(A + B) - \\tan A = 3 - \\dfrac{1}{2} = \\dfrac{5}{2}$ '
        'แล้วสร้างสามเหลี่ยมด้าน $5$ กับ $2$ ได้ด้านตรงข้ามมุมฉากยาว $\\sqrt{29}$ '
        'ฟังก์ชันตรีโกณไม่ใช่ฟังก์ชันเชิงเส้น จึงกระจายผ่านบวกลบไม่ได้ '
        'ทดสอบง่าย ๆ ด้วย $\\tan(45^{\\circ} - 45^{\\circ}) = 0$ แต่ $\\tan 45^{\\circ} - \\tan 45^{\\circ}$ '
        'ก็เท่ากับ $0$ เหมือนกันจึงยังไม่เห็นข้อผิด ลองใช้ $\\tan(60^{\\circ} - 30^{\\circ})$ '
        'ซึ่งเท่ากับ $\\dfrac{\\sqrt{3}}{3}$ แต่ผลต่างของแทนเจนต์เท่ากับ '
        '$\\sqrt{3} - \\dfrac{\\sqrt{3}}{3} = \\dfrac{2\\sqrt{3}}{3}$ ซึ่งไม่เท่ากัน',
        '• ได้ $\\dfrac{5\\sqrt{26}}{26}$ เพราะจำเครื่องหมายตัวส่วนสลับ '
        'ไปใช้ตัวส่วน $1 - \\tan(A + B)\\tan A = 1 - \\dfrac{3}{2} = -\\dfrac{1}{2}$ '
        'จึงได้ $\\tan B = -5$ แล้วทิ้งเครื่องหมายลบไปเพราะเห็นว่า $B$ เป็นมุมแหลม '
        'จากนั้นสร้างสามเหลี่ยมด้าน $5$ กับ $1$ ได้ด้านตรงข้ามมุมฉากยาว $\\sqrt{26}$ '
        'การได้ค่าติดลบทั้งที่โจทย์บอกว่าเป็นมุมแหลม คือสัญญาณว่าใช้สูตรผิด '
        'ต้องย้อนกลับไปแก้สูตร ⛔ ไม่ใช่ทิ้งเครื่องหมายแล้วเดินต่อ',
    ],
    'V.mold: G = the tangent of a compound angle A+B together with the tangent of one component A, both '
    'angles declared acute / A = the sine of the other component B / M = rewrite B as (A+B) - A, apply the '
    'tangent difference formula, then convert the resulting tangent to a sine through a reference right '
    'triangle. Rubric F2 C1 P1 T1 L0 = 5/15 with total at least 3 and T at most 2 -> level: ปานกลาง. '
    'sympy (verify_b15.py): route 1 computes (3 - 1/2)/(1 + 3*(1/2)) and returns 1, then sin(atan(1)) returns '
    'sqrt(2)/2; route 2 reconstructs the actual angles A0 = atan(1/2) and B0 = atan(1) and confirms both that '
    'tan(A0+B0) simplifies back to 3 and that both angles lie strictly inside (0, pi/2), so the acute-angle '
    'hypothesis in the stem is consistent rather than decorative. All three distractors machine-computed from '
    'named error paths: -sqrt(2)/2 from sin(atan((1/2 - 3)/(1 + (1/2)*3))) which is the reversed subtraction '
    'order, 5*sqrt(29)/29 from sin(atan(5/2)) which is the distribute-tangent-over-subtraction slip, and '
    '5*sqrt(26)/26 from sin(atan(5)) which is the flipped denominator sign followed by discarding the minus; '
    'a further check confirms that the flipped denominator really does produce -5, so that path is traceable. '
    'The negative distractor is eliminable by the acute-angle condition alone, which is deliberate: it '
    'rewards the student who reads the hypothesis, while the two irrational distractors remain to punish the '
    'two formula slips that a range check cannot catch. '
    'Collision sweep on 6392 items (bank 62 files + k1 out + k2 out): the saturated compound-angle molds in '
    'the corpus are the auxiliary-angle form a sin x + b cos x = c at 80 items and the double-angle collapse '
    'of a cosine product at 12 items; this item is neither, and the specific shape of recovering one '
    'component angle from the compound angle is not present in the chapter.',
)

# -*- coding: utf-8 -*-
add(
    81,
    ['7.8'],
    'ง่าย',
    'ค่าของ $\\arccos\\left(\\dfrac{1}{2}\\right) + \\arcsin\\left(\\dfrac{\\sqrt{3}}{2}\\right)$ '
    'เท่ากับข้อใด',
    [
        '$\\dfrac{\\pi}{3}$',
        '$\\dfrac{\\pi}{2}$',
        '$\\dfrac{2\\pi}{3}$',
        '$\\pi$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• $\\arccos x$ อ่านว่า “มุมที่มีโคไซน์เท่ากับ $x$” โดยตกลงกันว่าต้องเลือกมุมที่อยู่ในช่วง '
        '$[0, \\pi]$ เท่านั้น ช่วงนี้เรียกว่าช่วงค่าหลัก และมีไว้เพื่อให้แต่ละค่าของ $x$ '
        'ให้มุมออกมาเพียงมุมเดียว',
        '• $\\arcsin x$ อ่านว่า “มุมที่มีไซน์เท่ากับ $x$” โดยต้องเลือกมุมที่อยู่ในช่วง '
        '$\\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$ เท่านั้น',
        '• ค่าที่มุมพิเศษที่ต้องใช้ : $\\cos\\dfrac{\\pi}{3} = \\dfrac{1}{2}$ และ '
        '$\\sin\\dfrac{\\pi}{3} = \\dfrac{\\sqrt{3}}{2}$ '
        'ส่วนมุมพิเศษอีกมุมที่มักถูกหยิบสลับกันคือ $\\cos\\dfrac{\\pi}{6} = \\dfrac{\\sqrt{3}}{2}$ และ '
        '$\\sin\\dfrac{\\pi}{6} = \\dfrac{1}{2}$',
        '• เอกลักษณ์ $\\arcsin x + \\arccos x = \\dfrac{\\pi}{2}$ '
        'ใช้ได้ก็ต่อเมื่อสองพจน์รับ<b>ค่าเดียวกัน</b>เท่านั้น '
        'ถ้าค่าที่รับต่างกัน เอกลักษณ์นี้ใช้ไม่ได้เลย',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• นิพจน์ $\\arccos\\left(\\dfrac{1}{2}\\right) + \\arcsin\\left(\\dfrac{\\sqrt{3}}{2}\\right)$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของนิพจน์นี้ในหน่วยเรเดียน',
        '',
        '<b>【 แปลงแต่ละพจน์เป็นมุมทีละพจน์ โดยเช็คช่วงค่าหลักของแต่ละฟังก์ชันก่อนตอบ 】</b>',
        '',
        '<b>ขั้นที่ 1 · หาค่าของพจน์แรก</b>',
        '• ให้ $\\alpha = \\arccos\\left(\\dfrac{1}{2}\\right)$ '
        'ความหมายคือ $\\alpha$ เป็นมุมที่ $\\cos\\alpha = \\dfrac{1}{2}$ และ $0 \\le \\alpha \\le \\pi$',
        '• มุมพิเศษที่มีโคไซน์เท่ากับ $\\dfrac{1}{2}$ คือ $\\dfrac{\\pi}{3}$ '
        'และค่านี้อยู่ในช่วง $[0, \\pi]$ จริง จึงใช้ได้',
        '• ⛔ ระวังการหยิบสลับ ค่า $\\dfrac{1}{2}$ เป็นค่า<b>โคไซน์</b>ของ $\\dfrac{\\pi}{3}$ '
        'แต่เป็นค่า<b>ไซน์</b>ของ $\\dfrac{\\pi}{6}$ จึงได้ $\\alpha = \\dfrac{\\pi}{3}$ '
        'ไม่ใช่ $\\dfrac{\\pi}{6}$',
        '',
        '<b>ขั้นที่ 2 · หาค่าของพจน์ที่สอง</b>',
        '• ให้ $\\beta = \\arcsin\\left(\\dfrac{\\sqrt{3}}{2}\\right)$ '
        'ความหมายคือ $\\beta$ เป็นมุมที่ $\\sin\\beta = \\dfrac{\\sqrt{3}}{2}$ และ '
        '$-\\dfrac{\\pi}{2} \\le \\beta \\le \\dfrac{\\pi}{2}$',
        '• มุมพิเศษที่มีไซน์เท่ากับ $\\dfrac{\\sqrt{3}}{2}$ คือ $\\dfrac{\\pi}{3}$ '
        'และค่านี้อยู่ในช่วงค่าหลักของอาร์กไซน์จริง จึงใช้ได้',
        '• สังเกตว่ามุม $\\dfrac{2\\pi}{3}$ ก็มีไซน์เท่ากับ $\\dfrac{\\sqrt{3}}{2}$ เหมือนกัน '
        'แต่ ⛔ ใช้ไม่ได้ เพราะอยู่นอกช่วงค่าหลักของอาร์กไซน์ จึงได้ $\\beta = \\dfrac{\\pi}{3}$',
        '',
        '<b>ขั้นที่ 3 · บวกสองพจน์เข้าด้วยกัน</b>',
        '• ⛔ ก่อนบวก ให้สังเกตว่าค่าที่สองฟังก์ชันรับเข้าไปคือ $\\dfrac{1}{2}$ กับ '
        '$\\dfrac{\\sqrt{3}}{2}$ ซึ่ง<b>ไม่ใช่ค่าเดียวกัน</b> '
        'ดังนั้นเอกลักษณ์ $\\arcsin x + \\arccos x = \\dfrac{\\pi}{2}$ ใช้กับนิพจน์นี้ไม่ได้ '
        'ต้องคิดทีละพจน์เท่านั้น',
        '• บวกค่าที่ได้จากสองขั้นแรก : '
        '$\\alpha + \\beta = \\dfrac{\\pi}{3} + \\dfrac{\\pi}{3} = \\dfrac{2\\pi}{3}$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไม่หาค่าของแต่ละพจน์เลย '
        'แต่ใช้สูตรผลบวกมุมคำนวณโคไซน์และไซน์ของผลรวมโดยตรง)</b>',
        '• ให้ $\\alpha = \\arccos\\left(\\dfrac{1}{2}\\right)$ '
        'จะได้ $\\cos\\alpha = \\dfrac{1}{2}$ ทันทีจากนิยาม '
        'และเพราะ $\\alpha$ อยู่ในช่วง $[0, \\pi]$ ซึ่งไซน์เป็นบวกเสมอ '
        'จึงได้ $\\sin\\alpha = \\sqrt{1 - \\left(\\dfrac{1}{2}\\right)^2} = \\dfrac{\\sqrt{3}}{2}$',
        '• ให้ $\\beta = \\arcsin\\left(\\dfrac{\\sqrt{3}}{2}\\right)$ '
        'จะได้ $\\sin\\beta = \\dfrac{\\sqrt{3}}{2}$ ทันทีจากนิยาม '
        'และเพราะ $\\beta$ อยู่ในช่วง $\\left[-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right]$ '
        'ซึ่งโคไซน์เป็นบวกเสมอ จึงได้ '
        '$\\cos\\beta = \\sqrt{1 - \\left(\\dfrac{\\sqrt{3}}{2}\\right)^2} = \\dfrac{1}{2}$',
        '• ใช้สูตรผลต่างของผลคูณ : '
        '$\\cos(\\alpha + \\beta) = \\cos\\alpha\\cos\\beta - \\sin\\alpha\\sin\\beta '
        '= \\dfrac{1}{2}\\cdot\\dfrac{1}{2} - \\dfrac{\\sqrt{3}}{2}\\cdot\\dfrac{\\sqrt{3}}{2} '
        '= \\dfrac{1}{4} - \\dfrac{3}{4} = -\\dfrac{1}{2}$',
        '• ใช้สูตรผลบวกของไซน์เพื่อระบุจตุภาค : '
        '$\\sin(\\alpha + \\beta) = \\sin\\alpha\\cos\\beta + \\cos\\alpha\\sin\\beta '
        '= \\dfrac{\\sqrt{3}}{2}\\cdot\\dfrac{1}{2} + \\dfrac{1}{2}\\cdot\\dfrac{\\sqrt{3}}{2} '
        '= \\dfrac{\\sqrt{3}}{2}$',
        '• โคไซน์เป็นลบแต่ไซน์เป็นบวก แสดงว่ามุมผลรวมอยู่ในจตุภาคที่สอง '
        'และมุมในจตุภาคที่สองที่มีโคไซน์เท่ากับ $-\\dfrac{1}{2}$ คือ $\\dfrac{2\\pi}{3}$ '
        'ตรงกับคำตอบที่ได้จากเส้นทางแรกพอดี',
        '',
        '✅ <b>คำตอบ</b> $\\dfrac{2\\pi}{3}$ → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เวลาเจอฟังก์ชันตรีโกณผกผัน ให้แปลเป็นประโยคก่อนคำนวณเสมอ เช่นอ่าน '
        '$\\arcsin\\left(\\dfrac{\\sqrt{3}}{2}\\right)$ ว่า “มุมในช่วง '
        '$-\\dfrac{\\pi}{2}$ ถึง $\\dfrac{\\pi}{2}$ ที่มีไซน์เท่ากับ $\\dfrac{\\sqrt{3}}{2}$” '
        'การพูดช่วงออกมาด้วยทุกครั้งจะทำให้ไม่ลืมข้อจำกัดของช่วงค่าหลัก',
        '• ตารางมุมพิเศษที่สลับกันบ่อยที่สุดคือ $\\dfrac{\\pi}{6}$ กับ $\\dfrac{\\pi}{3}$ '
        'ให้ยึดหลักว่ามุมยิ่งใหญ่ ไซน์ยิ่งมาก และโคไซน์ยิ่งน้อย ในช่วง $0$ ถึง $\\dfrac{\\pi}{2}$ '
        'เมื่อ $\\dfrac{\\pi}{3}$ ใหญ่กว่า $\\dfrac{\\pi}{6}$ ไซน์ของมันจึงต้องเป็นตัวที่มากกว่า '
        'นั่นคือ $\\dfrac{\\sqrt{3}}{2}$',
        '• เอกลักษณ์ $\\arcsin x + \\arccos x = \\dfrac{\\pi}{2}$ เป็นของดี แต่ต้องเช็คก่อนใช้ทุกครั้ง '
        'ว่าสองพจน์รับค่าเดียวกันหรือไม่ ถ้าโจทย์จงใจให้ค่าต่างกัน แปลว่าโจทย์กำลังดักตรงจุดนี้พอดี',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $\\dfrac{\\pi}{3}$ เพราะสลับตารางมุมพิเศษทั้งสองพจน์ '
        'คือคิดว่า $\\arccos\\left(\\dfrac{1}{2}\\right) = \\dfrac{\\pi}{6}$ '
        'และ $\\arcsin\\left(\\dfrac{\\sqrt{3}}{2}\\right) = \\dfrac{\\pi}{6}$ '
        'แล้วบวกกันได้ $\\dfrac{\\pi}{3}$ '
        'วิธีกันคือถามกลับทุกครั้งว่า “โคไซน์ของมุมที่ตอบ เท่ากับค่าที่โจทย์ให้จริงหรือไม่” '
        'ซึ่ง $\\cos\\dfrac{\\pi}{6} = \\dfrac{\\sqrt{3}}{2}$ ไม่ใช่ $\\dfrac{1}{2}$ จึงผิดทันที',
        '• ได้ $\\dfrac{\\pi}{2}$ เพราะยัดเอกลักษณ์ $\\arcsin x + \\arccos x = \\dfrac{\\pi}{2}$ '
        'ทั้งที่สองพจน์รับค่าคนละค่า เอกลักษณ์นี้มาจากข้อเท็จจริงว่ามุมสองมุมที่มีไซน์กับโคไซน์ '
        'เท่ากับ<b>ค่าเดียวกัน</b>เป็นมุมประกอบมุมฉากซึ่งกันและกัน '
        'พอค่าที่รับต่างกัน ความสัมพันธ์นั้นก็หายไป',
        '• ได้ $\\pi$ เพราะหยิบมุมนอกช่วงค่าหลักของอาร์กโคไซน์ '
        'คือตอบ $\\arccos\\left(\\dfrac{1}{2}\\right) = \\dfrac{2\\pi}{3}$ '
        'ทั้งที่ $\\cos\\dfrac{2\\pi}{3} = -\\dfrac{1}{2}$ ซึ่งติดลบ ไม่ตรงกับค่าที่โจทย์ให้ '
        'แล้วนำไปบวกกับ $\\dfrac{\\pi}{3}$ ได้ $\\pi$ '
        'ให้จำว่ามุมในจตุภาคที่สองมีโคไซน์เป็นลบเสมอ ค่าที่โจทย์ให้เป็นบวกจึงต้องได้มุมแหลม',
    ],
    'V.mold: G = a sum of two inverse trigonometric expressions evaluated at two different special values, '
    'both arguments positive / A = the exact value of the sum in radians / M = evaluate each principal value '
    'separately from the definition and the principal-range restriction, then add. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 with total at most 2, T = 0 and C = 0 -> level: ง่าย. '
    'Two design decisions keep this honestly easy. First, the two arguments are deliberately different '
    '(1/2 against sqrt(3)/2) so the complementary identity does not apply and the item is a plain two-term '
    'evaluation rather than an identity-recognition puzzle. Second, both arguments are positive, so the '
    'principal range never actually binds on the correct path; the earlier draft used a negative argument, '
    'which made the principal range a real turning point and scored T = 1 for a total of 3, landing in '
    'ปานกลาง instead of ง่าย, so that draft was dropped. '
    'Subtopic 7.8 is the scarcest in the authored corpus at only 4 items out of 79, so this slot fills a real '
    'coverage gap while also supplying one of the two easy items the level distribution needed. '
    'sympy (verify_b15.py): acos(1/2) returns pi/3, asin(sqrt(3)/2) returns pi/3, and the sum returns 2*pi/3; '
    'a separate check confirms the two arguments are unequal, which is what makes the complementary identity '
    'inapplicable. All three distractors machine-computed from named error paths: pi/3 from pi/6 + pi/6 which '
    'is the swapped special-angle table, pi/2 from forcing the complementary identity, and pi from '
    '2*pi/3 + pi/3 which is the out-of-principal-range slip; a further check confirms cos(2*pi/3) really is '
    '-1/2, so that third error path is traceable rather than invented. '
    'Collision sweep on 6392 items (bank 62 files + k1 out + k2 out): the saturated inverse-trig molds in the '
    'corpus are nested arc evaluation at 19 items, arctan sums at 14 items, and the arcsin-plus-arccos '
    'equation family; this item is none of those, being a plain two-term sum of principal values at special '
    'arguments.',
)

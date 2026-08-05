# -*- coding: utf-8 -*-
add(
    90,
    ['7.6'],
    'ง่าย',
    'ค่าของ $\\cos^2 15^{\\circ} - \\sin^2 15^{\\circ}$ เท่ากับข้อใด',
    [
        '$-\\dfrac{\\sqrt{3}}{2}$',
        '$\\dfrac{1}{2}$',
        '$\\dfrac{\\sqrt{3}}{2}$',
        '$1$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• สูตรมุมสองเท่าของโคไซน์เขียนได้สามหน้าตา แต่ทุกหน้าตาเท่ากันหมด คือ '
        '$\\cos 2A = \\cos^2 A - \\sin^2 A = 2\\cos^2 A - 1 = 1 - 2\\sin^2 A$ '
        'ข้อนี้ใช้หน้าตาแรก',
        '• สูตรนี้ใช้ได้กับมุม $A$ ทุกมุม ไม่จำกัดว่าต้องเป็นมุมแหลม เพราะพิสูจน์มาจาก '
        '$\\cos(A + A)$ ซึ่งเป็นสูตรผลบวกมุมที่ใช้ได้ทั่วไป',
        '• อ่านสูตรให้ถูกทาง : ด้านซ้ายมีมุม $2A$ ด้านขวามีมุม $A$ '
        'ดังนั้นเมื่อเห็นด้านขวาก่อน สิ่งที่ต้องทำคือ<b>คูณมุมด้วยสอง</b> ไม่ใช่หารด้วยสอง',
        '• ค่าที่ต้องจำได้ทันที $\\cos 30^{\\circ} = \\dfrac{\\sqrt{3}}{2}$ '
        'และ $\\sin 30^{\\circ} = \\dfrac{1}{2}$ สองค่านี้หน้าตาใกล้กันจึงถูกหยิบสลับกันบ่อย',
        '• ⛔ อย่าสับสนกับเอกลักษณ์พีทาโกรัส $\\sin^2 A + \\cos^2 A = 1$ '
        'ซึ่งเป็นการ<b>บวก</b> ส่วนโจทย์นี้เป็นการ<b>ลบ</b> คนละสูตรกันคนละคำตอบ',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• นิพจน์ $\\cos^2 15^{\\circ} - \\sin^2 15^{\\circ}$',
        '• มุมทั้งสองที่ปรากฏเป็นมุมเดียวกัน คือ $15^{\\circ}$ ทั้งคู่',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของนิพจน์นี้ออกมาเป็นตัวเลข',
        '',
        '<b>【 มองว่านิพจน์คือสูตรมุมสองเท่าที่ถูกกระจายไว้แล้ว จึงยุบกลับให้เหลือมุมเดียว 】</b>',
        '',
        '<b>ขั้นที่ 1 · ระบุว่าโจทย์อยู่ในหน้าตาไหนของสูตร</b>',
        '• เขียนสูตรก่อน แล้วค่อยเทียบ : $\\cos 2A = \\cos^2 A - \\sin^2 A$',
        '• เทียบด้านขวาของสูตรกับโจทย์ทีละก้อน ก้อนแรก $\\cos^2 A$ ตรงกับ $\\cos^2 15^{\\circ}$ '
        'และก้อนหลัง $\\sin^2 A$ ตรงกับ $\\sin^2 15^{\\circ}$',
        '• ทั้งสองก้อนบังคับค่าเดียวกันคือ $A = 15^{\\circ}$ จึงเทียบสูตรได้อย่างสมบูรณ์ '
        'ไม่มีก้อนไหนเหลือค้าง',
        '',
        '<b>ขั้นที่ 2 · แทนค่า $A$ ลงในด้านซ้ายของสูตร</b>',
        '• ด้านซ้ายคือ $\\cos 2A$ แทน $A = 15^{\\circ}$ ได้ '
        '$\\cos\\left(2 \\times 15^{\\circ}\\right) = \\cos 30^{\\circ}$',
        '• ดังนั้น $\\cos^2 15^{\\circ} - \\sin^2 15^{\\circ} = \\cos 30^{\\circ}$',
        '',
        '<b>ขั้นที่ 3 · อ่านค่าจากมุมมาตรฐาน</b>',
        '• $\\cos 30^{\\circ} = \\dfrac{\\sqrt{3}}{2}$',
        '• จึงได้ $\\cos^2 15^{\\circ} - \\sin^2 15^{\\circ} = \\dfrac{\\sqrt{3}}{2}$',
        '• ตรวจความสมเหตุสมผลอย่างเร็ว : $15^{\\circ}$ เป็นมุมเล็ก โคไซน์จึงใหญ่กว่าไซน์ '
        'ผลลบจึงต้องเป็นบวก และต้องไม่เกิน $1$ ⇒ ค่าที่ได้อยู่ในกรอบนี้จริง',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไม่ใช้สูตรมุมสองเท่าเลย '
        'แต่หาค่าจริงของ $\\cos^2 15^{\\circ}$ และ $\\sin^2 15^{\\circ}$ ทีละตัวด้วยสูตรครึ่งมุม)</b>',
        '• สูตรครึ่งมุมรูปกำลังสอง : $\\cos^2 A = \\dfrac{1 + \\cos 2A}{2}$ '
        'และ $\\sin^2 A = \\dfrac{1 - \\cos 2A}{2}$',
        '• ที่ $A = 15^{\\circ}$ จะได้ $2A = 30^{\\circ}$ และ $\\cos 30^{\\circ} = \\dfrac{\\sqrt{3}}{2}$',
        '• จึง $\\cos^2 15^{\\circ} = \\dfrac{1 + \\dfrac{\\sqrt{3}}{2}}{2} '
        '= \\dfrac{2 + \\sqrt{3}}{4}$',
        '• และ $\\sin^2 15^{\\circ} = \\dfrac{1 - \\dfrac{\\sqrt{3}}{2}}{2} '
        '= \\dfrac{2 - \\sqrt{3}}{4}$',
        '• นำมาลบกัน $\\dfrac{2 + \\sqrt{3}}{4} - \\dfrac{2 - \\sqrt{3}}{4} '
        '= \\dfrac{2 + \\sqrt{3} - 2 + \\sqrt{3}}{4} = \\dfrac{2\\sqrt{3}}{4} '
        '= \\dfrac{\\sqrt{3}}{2}$',
        '• ตรงกับคำตอบเดิมทุกประการ และวิธีนี้ยังตรวจได้อีกชั้นว่าถ้านำสองก้อนมา<b>บวก</b>กัน '
        'จะได้ $\\dfrac{4}{4} = 1$ ซึ่งคือเอกลักษณ์พีทาโกรัสพอดี',
        '',
        '✅ <b>คำตอบ</b> $\\cos^2 15^{\\circ} - \\sin^2 15^{\\circ} = \\dfrac{\\sqrt{3}}{2}$ '
        '→ <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เห็นนิพจน์ที่มีฟังก์ชันเดียวกันสองก้อนกำลังสองของ<b>มุมเดียวกัน</b>เมื่อไร '
        'ให้นึกถึงสูตรมุมสองเท่าก่อนเสมอ เครื่องหมายลบชี้ไปที่ $\\cos 2A$ '
        'ส่วนเครื่องหมายบวกชี้ไปที่เอกลักษณ์พีทาโกรัสซึ่งได้ $1$ ทันที',
        '• จำคู่สูตรที่มักถูกสลับกันเป็นคู่ ๆ ไว้ว่า '
        '$\\cos 2A$ มาจากรูป<b>กำลังสองลบกัน</b> ส่วน $\\sin 2A = 2\\sin A\\cos A$ '
        'มาจากรูป<b>คูณกันแล้วคูณสอง</b> หน้าตาไม่เหมือนกันเลย ถ้าจำภาพนี้ได้จะไม่หยิบสลับ',
        '• เวลามุมในโจทย์ไม่ใช่มุมมาตรฐาน เช่น $15^{\\circ}$ หรือ $22.5^{\\circ}$ '
        'มักเป็นสัญญาณว่าโจทย์ตั้งใจให้ยุบเป็นมุมสองเท่า เพราะมุมสองเท่าของมันจะกลายเป็น '
        'มุมมาตรฐานที่อ่านค่าได้',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $1$ เพราะอ่านนิพจน์เป็นเอกลักษณ์พีทาโกรัส $\\cos^2 + \\sin^2 = 1$ '
        'คือมองข้ามเครื่องหมายลบไป วิธีกันคืออ่านเครื่องหมายกลางนิพจน์ออกเสียงก่อนลงมือทุกครั้ง '
        'และจำไว้ว่าคำตอบ $1$ จะเกิดได้ก็ต่อเมื่อเป็นการบวกเท่านั้น',
        '• ได้ $\\dfrac{1}{2}$ เพราะยุบสูตรถูกแล้วว่ามุมกลายเป็น $30^{\\circ}$ '
        'แต่หยิบฟังก์ชันผิดไปเป็น $\\sin 30^{\\circ}$ '
        'ให้ย้อนดูด้านซ้ายของสูตรที่ใช้ว่าเป็น $\\cos 2A$ '
        'ฟังก์ชันที่ออกมาจึงต้องเป็นโคไซน์เหมือนเดิม ไม่เปลี่ยนเป็นไซน์',
        '• ได้ $-\\dfrac{\\sqrt{3}}{2}$ เพราะสลับที่ตัวตั้งกับตัวลบเป็น '
        '$\\sin^2 15^{\\circ} - \\cos^2 15^{\\circ}$ ซึ่งเท่ากับ $-\\cos 30^{\\circ}$ '
        'ให้ตรวจด้วยสามัญสำนึกว่ามุม $15^{\\circ}$ เป็นมุมเล็ก โคไซน์ย่อมมากกว่าไซน์ '
        'ผลลบจึงต้องเป็นจำนวนบวก ค่าติดลบจึงเป็นไปไม่ได้',
    ],
    'V.mold: G = a numeric expression in the already-expanded double-angle shape cos^2 15 - sin^2 15 / '
    'A = the value of that expression / M = recognise the expanded shape, collapse it back to cos 2A, '
    'evaluate at a standard angle. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 with total at most 2, T = 0 and C = 0 -> level: ง่าย. '
    'The design decision that keeps it honestly easy: recognising an already-expanded standard formula is '
    'plain formula recall, not a turning point, which is the same call made for q016 (collapsing the '
    'angle-difference formula) at T = 0. Scoring was written before the level was read off. '
    'Pure symbols, no context, so L = 0 as every ง่าย item in this corpus must have. '
    'sympy (verify_b17.py): cos(pi/12)**2 - sin(pi/12)**2 simplifies to sqrt(3)/2 exactly. All three '
    'distractors machine-computed from named error paths: 1 from reading the minus as a plus (Pythagorean '
    'identity), 1/2 from collapsing correctly to the 30 degree angle but taking sine instead of cosine, and '
    '-sqrt(3)/2 from swapping minuend and subtrahend. Choices are in ascending numeric order '
    '(-0.866, 0.5, 0.866, 1) so the answer slot is forced by the values, not chosen. '
    'Collision sweep on 6402 items (bank 62 files + k1 out + k2 out), probe collide_b17c.py: the pattern '
    'cos^2 A - sin^2 A appears in only 4 items corpus-wide and none of them is a collapse-and-evaluate '
    'question. chap-07-q48 hands the expression over as given data inside a larger problem, chap-07-q83 '
    'wraps mismatched angles inside arcsin as a deliberate trap in subtopic 7.8, chap-07-q142 asks which '
    'identity matches a form, and chap-07-q148 is an equation to solve. The first draft for this easy slot '
    '(sin 75 cos 15 - cos 75 sin 15) was killed at probe time because it duplicated our own '
    'gen-chap-07-trigonometry-q016 word for word.',
)

# -*- coding: utf-8 -*-
add(
    80,
    ['7.6'],
    'ง่าย',
    'กำหนดให้ $\\cos 2\\theta = \\dfrac{7}{25}$ '
    'แล้วค่าของ $\\sin^2\\theta$ เท่ากับข้อใด',
    [
        '$\\dfrac{9}{25}$',
        '$\\dfrac{16}{25}$',
        '$\\dfrac{18}{25}$',
        '$\\dfrac{32}{25}$',
    ],
    0,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เอกลักษณ์มุมสองเท่าของโคไซน์เขียนได้สามรูปที่สมมูลกัน คือ '
        '$\\cos 2\\theta = \\cos^2\\theta - \\sin^2\\theta$ , '
        '$\\cos 2\\theta = 1 - 2\\sin^2\\theta$ และ '
        '$\\cos 2\\theta = 2\\cos^2\\theta - 1$ '
        'ทั้งสามรูปให้ค่าเท่ากันเสมอ ต่างกันเพียงว่าเหลือฟังก์ชันตัวใดไว้',
        '• เอกลักษณ์พีทาโกรัส : $\\sin^2\\theta + \\cos^2\\theta = 1$ '
        'ซึ่งเป็นตัวเปลี่ยนรูปทั้งสามข้างต้นให้กันและกันได้',
        '• ค่าของ $\\sin^2\\theta$ เป็นกำลังสองของจำนวนที่มีค่าระหว่าง $-1$ กับ $1$ '
        'จึงต้องอยู่ในช่วง $0 \\le \\sin^2\\theta \\le 1$ เสมอ '
        'ข้อนี้ใช้ช่วงนี้เป็นเครื่องมือคัดคำตอบที่เป็นไปไม่ได้',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $\\cos 2\\theta = \\dfrac{7}{25}$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\sin^2\\theta$',
        '',
        '<b>【 เลือกรูปมุมสองเท่าที่เหลือไว้เฉพาะไซน์ แล้วมองสมการเป็นสมการเชิงเส้นในตัวแปร '
        '$\\sin^2\\theta$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · เลือกรูปของเอกลักษณ์ให้ตรงกับสิ่งที่โจทย์ถาม</b>',
        '• สิ่งที่ต้องหาคือ $\\sin^2\\theta$ ดังนั้นควรเลือกรูปที่ข้างขวามีเฉพาะไซน์ตัวเดียว '
        'นั่นคือ $\\cos 2\\theta = 1 - 2\\sin^2\\theta$',
        '• ⛔ ไม่เลือกรูป $\\cos 2\\theta = 2\\cos^2\\theta - 1$ '
        'เพราะจะได้ $\\cos^2\\theta$ แล้วต้องเสียเวลาแปลงกลับด้วยเอกลักษณ์พีทาโกรัสอีกชั้นหนึ่ง',
        '• ⛔ ไม่เลือกรูป $\\cos 2\\theta = \\cos^2\\theta - \\sin^2\\theta$ '
        'เพราะมีฟังก์ชันสองตัวปนกันในสมการเดียว ยังแก้ไม่ได้ทันที',
        '',
        '<b>ขั้นที่ 2 · แทนค่าที่โจทย์ให้ลงในเอกลักษณ์ที่เลือกไว้</b>',
        '• แทน $\\cos 2\\theta = \\dfrac{7}{25}$ ลงในรูปที่เลือก : '
        '$\\dfrac{7}{25} = 1 - 2\\sin^2\\theta$',
        '• ย้าย $2\\sin^2\\theta$ ไปข้างซ้ายและย้าย $\\dfrac{7}{25}$ ไปข้างขวา : '
        '$2\\sin^2\\theta = 1 - \\dfrac{7}{25}$',
        '• ทำเป็นเศษส่วนตัวส่วนเดียวกัน โดยเขียน $1$ เป็น $\\dfrac{25}{25}$ : '
        '$2\\sin^2\\theta = \\dfrac{25}{25} - \\dfrac{7}{25} = \\dfrac{18}{25}$',
        '',
        '<b>ขั้นที่ 3 · หารด้วยสัมประสิทธิ์ให้เหลือสิ่งที่ถามเดี่ยว ๆ</b>',
        '• หารทั้งสองข้างด้วย $2$ ⛔ ขั้นนี้คือขั้นที่พลาดกันมากที่สุดในข้อแบบนี้ : '
        '$\\sin^2\\theta = \\dfrac{18}{25} \\div 2 = \\dfrac{18}{50} = \\dfrac{9}{25}$',
        '',
        '<b>ขั้นที่ 4 · ตรวจความสมเหตุสมผลของค่าที่ได้</b>',
        '• ค่า $\\dfrac{9}{25} = 0.36$ อยู่ในช่วง $0$ ถึง $1$ จริง จึงเป็นค่าที่เป็นไปได้ของ $\\sin^2\\theta$',
        '• สังเกตว่าโจทย์ถาม $\\sin^2\\theta$ ไม่ได้ถาม $\\sin\\theta$ '
        'จึงไม่ต้องพิจารณากรณีบวกลบและไม่ต้องรู้ว่ามุม $\\theta$ อยู่จตุภาคใด '
        'ถ้าโจทย์ถาม $\\sin\\theta$ คำตอบจะเป็น $\\dfrac{3}{5}$ หรือ $-\\dfrac{3}{5}$ ซึ่งตอบไม่ได้แน่นอน',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ใช้รูปมุมสองเท่าในพจน์ของแทนเจนต์ '
        'ซึ่งไม่ผ่านรูป $1 - 2\\sin^2\\theta$ เลย)</b>',
        '• เอกลักษณ์มุมสองเท่าอีกรูปหนึ่งคือ '
        '$\\cos 2\\theta = \\dfrac{1 - \\tan^2\\theta}{1 + \\tan^2\\theta}$',
        '• ให้ $u = \\tan^2\\theta$ แล้วแทนค่าที่โจทย์ให้ : $\\dfrac{1 - u}{1 + u} = \\dfrac{7}{25}$',
        '• คูณไขว้ : $25(1 - u) = 7(1 + u)$ นั่นคือ $25 - 25u = 7 + 7u$',
        '• รวมพจน์ : $18 = 32u$ จึงได้ $u = \\dfrac{18}{32} = \\dfrac{9}{16}$',
        '• เปลี่ยนกลับเป็นไซน์ด้วยความสัมพันธ์ '
        '$\\sin^2\\theta = \\dfrac{\\tan^2\\theta}{1 + \\tan^2\\theta}$ : '
        '$\\sin^2\\theta = \\dfrac{\\ \\dfrac{9}{16}\\ }{\\ \\dfrac{25}{16}\\ } = \\dfrac{9}{25}$',
        '• ยืนยันด้วยตัวเลขจริงอีกชั้นหนึ่ง ถ้าใช้สามเหลี่ยมมุมฉากด้าน $3$ , $4$ , $5$ '
        'โดยให้ $\\sin\\theta = \\dfrac{3}{5}$ และ $\\cos\\theta = \\dfrac{4}{5}$ '
        'จะได้ $\\cos 2\\theta = \\cos^2\\theta - \\sin^2\\theta = \\dfrac{16}{25} - \\dfrac{9}{25} '
        '= \\dfrac{7}{25}$ ตรงกับที่โจทย์ให้พอดี และ $\\sin^2\\theta = \\dfrac{9}{25}$ จริง',
        '• สองเส้นทางที่ใช้เอกลักษณ์คนละตัวให้ค่าเดียวกัน จึงยืนยันว่าคำตอบถูกต้อง',
        '',
        '✅ <b>คำตอบ</b> $\\dfrac{9}{25}$ → <b>ตัวเลือก 1</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เอกลักษณ์มุมสองเท่าของโคไซน์มีสามรูป ให้จำวิธีเลือกแบบนี้ '
        'โจทย์ถามไซน์ก็หยิบรูปที่เหลือไซน์ โจทย์ถามโคไซน์ก็หยิบรูปที่เหลือโคไซน์ '
        'การเลือกรูปให้ถูกตั้งแต่บรรทัดแรกช่วยตัดงานแปลงกลับไปกลับมาทิ้งได้ทั้งหมด',
        '• จำรูปที่จัดใหม่ไว้ใช้ตรง ๆ ได้เลยสองรูป คือ '
        '$\\sin^2\\theta = \\dfrac{1 - \\cos 2\\theta}{2}$ และ '
        '$\\cos^2\\theta = \\dfrac{1 + \\cos 2\\theta}{2}$ '
        'สังเกตว่าไซน์คู่กับเครื่องหมายลบ และโคไซน์คู่กับเครื่องหมายบวก '
        'วิธีจำคือแทน $\\theta = 0$ ทดสอบ จะได้ $\\sin^2 0 = \\dfrac{1 - 1}{2} = 0$ ซึ่งถูกต้อง '
        'ถ้าจำสลับเครื่องหมายจะได้ $1$ ซึ่งผิดทันที',
        '• เมื่อได้คำตอบเป็นค่าของ $\\sin^2\\theta$ หรือ $\\cos^2\\theta$ ให้ตรวจก่อนตอบเสมอว่า '
        'ค่านั้นอยู่ระหว่าง $0$ กับ $1$ หรือไม่ ค่าที่เกิน $1$ คือสัญญาณว่าคำนวณผิดแน่นอน',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $\\dfrac{16}{25}$ เพราะจำเครื่องหมายในเอกลักษณ์สลับ '
        'ไปใช้ $\\cos 2\\theta = 2\\sin^2\\theta - 1$ ซึ่งไม่มีรูปนี้จริง '
        'จึงคำนวณ $2\\sin^2\\theta = 1 + \\dfrac{7}{25} = \\dfrac{32}{25}$ แล้วหารสองได้ $\\dfrac{16}{25}$ '
        'ค่านี้แท้จริงคือ $\\cos^2\\theta$ ของข้อนี้พอดี จึงดูน่าเชื่อมาก '
        'วิธีกันคือทดสอบด้วย $\\theta = 0$ รูปที่ถูกต้องต้องให้ $\\cos 0 = 1$ '
        'ซึ่งรูปที่มีเครื่องหมายสลับจะให้ $-1$ ทันที',
        '• ได้ $\\dfrac{18}{25}$ เพราะลืมสัมประสิทธิ์ $2$ หน้า $\\sin^2\\theta$ '
        'คือจำเอกลักษณ์เป็น $\\cos 2\\theta = 1 - \\sin^2\\theta$ '
        'จึงได้ $\\sin^2\\theta = 1 - \\dfrac{7}{25} = \\dfrac{18}{25}$ แล้วหยุดตรงนั้น '
        'ค่านี้คือค่าที่ยังไม่ได้หารด้วย $2$ ให้ระวังว่าเลข $2$ ในเอกลักษณ์นี้ไม่ใช่ของประดับ',
        '• ได้ $\\dfrac{32}{25}$ เพราะพลาดสองชั้นพร้อมกัน คือจำเครื่องหมายสลับแล้วยังลืมหารด้วย $2$ '
        'จึงได้ $1 + \\dfrac{7}{25} = \\dfrac{32}{25}$ '
        'ค่านี้มากกว่า $1$ ซึ่งเป็นไปไม่ได้สำหรับ $\\sin^2\\theta$ ในทุกกรณี '
        'ถ้าฝึกนิสัยตรวจช่วงค่าก่อนตอบ จะคัดค่านี้ทิ้งได้ทันทีโดยไม่ต้องคำนวณซ้ำ',
    ],
    'V.mold: G = the value of cos(2t) given as a single fraction / A = the value of sin^2(t) / '
    'M = pick the sine-only form of the cosine double-angle identity and solve the resulting linear equation '
    'in sin^2(t). Rubric F1 C0 P1 T0 L0 = 2/15 with total at most 2, T = 0 and C = 0 -> level: ง่าย. '
    'The item deliberately asks for sin^2(t) rather than sin(t): asking for sin(t) would force a quadrant '
    'discussion and a plus-minus case, which would push C and T up and the item would no longer be ง่าย. '
    'The batch needed two genuinely easy items because the ง่าย band had drifted to 22.8 percent, below the '
    '25 percent target. sympy (verify_b15.py): route 1 solves 1 - 2*s = 7/25 and returns 9/25; route 2 is '
    'independent of that identity entirely, evaluating sin(acos(7/25)/2)**2 symbolically and returning 9/25, '
    'and a third check confirms cos(2*t0) returns 7/25. All three distractors machine-computed from named '
    'error paths: 16/25 from (1 + 7/25)/2 which is the sign-flipped identity, 18/25 from 1 - 7/25 which is '
    'the forgotten coefficient 2, and 32/25 from 1 + 7/25 which is both slips at once. The last distractor '
    'exceeds 1 on purpose so the explanation can teach the range check as a first-line filter. '
    'Collision sweep on 6392 items (bank 62 files + k1 out + k2 out), probe collide_b15d.py: the forward '
    'direction (given sin or cos of t, compute cos 2t) is crowded at 25 items, but the reverse direction '
    '(given cos 2t, recover a square of a half-argument function) appears in only 3 items and none of them '
    'shares this mold. Redesign history: the first draft of this slot was 1 - 2*sin^2(75 degrees), which the '
    'mold registry flagged WATCH-B against q012 and q016 and which also reused the 75 degree surface, leaving '
    'only the numbers axis different; it was killed and replaced by this reverse-direction design.',
)

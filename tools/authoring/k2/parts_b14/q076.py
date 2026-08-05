# -*- coding: utf-8 -*-
add(
    76,
    ['7.7', '7.2'],
    'ปานกลาง',
    'ค่าของ $x$ ที่มากที่สุดซึ่งสอดคล้องกับสมการ $\\tan 2x = -\\sqrt{3}$ '
    'เมื่อ $0 \\le x < \\pi$ เท่ากับข้อใด',
    [
        '$\\dfrac{\\pi}{3}$',
        '$\\dfrac{5\\pi}{6}$',
        '$\\dfrac{11\\pi}{12}$',
        '$\\dfrac{5\\pi}{3}$',
    ],
    1,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เมื่อสมการมีอาร์กิวเมนต์เป็น $2x$ ช่วงที่ต้องไล่คำตอบคือช่วงของ $2x$ ไม่ใช่ช่วงของ $x$ '
        'จึงต้องแปลงช่วงที่โจทย์ให้เป็นช่วงของอาร์กิวเมนต์ก่อนเสมอ',
        '• ฟังก์ชันแทนเจนต์มีคาบเท่ากับ $\\pi$ และมีค่าเป็นลบในจตุภาคที่สองและจตุภาคที่สี่ '
        'ส่วนมีค่าเป็นบวกในจตุภาคที่หนึ่งและจตุภาคที่สาม',
        '• มุมอ้างอิงที่ให้ค่าแทนเจนต์เท่ากับ $\\sqrt{3}$ คือ $\\dfrac{\\pi}{3}$ '
        'เพราะ $\\tan\\dfrac{\\pi}{3} = \\sqrt{3}$ ส่วน $\\tan\\dfrac{\\pi}{6} = \\dfrac{1}{\\sqrt{3}}$ '
        'ซึ่งเป็นคนละค่ากัน',
        '• การหามุมในจตุภาคที่ต้องการจากมุมอ้างอิง $\\alpha$ ใช้ว่า จตุภาคที่สองคือ $\\pi - \\alpha$ '
        'และจตุภาคที่สี่คือ $2\\pi - \\alpha$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• สมการ $\\tan 2x = -\\sqrt{3}$',
        '• ช่วงของตัวแปรคือ $0 \\le x < \\pi$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $x$ ที่มากที่สุดในบรรดาค่าทั้งหมดที่สอดคล้องกับสมการภายในช่วงที่กำหนด',
        '',
        '<b>【 ขยายช่วงของอาร์กิวเมนต์ก่อน แล้วจึงไล่สาขาของแทนเจนต์ให้ครบ ก่อนหารกลับเป็นค่าของ $x$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · แปลงช่วงของ $x$ ให้เป็นช่วงของอาร์กิวเมนต์</b>',
        '• ตั้งตัวแปรใหม่ให้อ่านง่าย โดยให้ $\\theta = 2x$ สมการจึงกลายเป็น $\\tan\\theta = -\\sqrt{3}$',
        '• นำ $2$ คูณตลอดอสมการที่โจทย์ให้ : จาก $0 \\le x < \\pi$ ได้ $0 \\le 2x < 2\\pi$ '
        'นั่นคือ $0 \\le \\theta < 2\\pi$',
        '• ⚠️ ขั้นนี้คือหัวใจของข้อนี้ ช่วงของ $\\theta$ ยาวเป็นสองเท่าของช่วงของ $x$ '
        'จึงบรรจุคาบของแทนเจนต์ได้สองคาบเต็ม แปลว่าต้องได้คำตอบสองค่า ไม่ใช่ค่าเดียว',
        '',
        '<b>ขั้นที่ 2 · หามุมอ้างอิงและระบุจตุภาคที่ทำให้แทนเจนต์เป็นลบ</b>',
        '• ค่าสัมบูรณ์ของข้างขวาคือ $\\sqrt{3}$ และมุมแหลมที่ให้ค่าแทนเจนต์เท่ากับ $\\sqrt{3}$ '
        'คือ $\\dfrac{\\pi}{3}$ จึงได้มุมอ้างอิง $\\alpha = \\dfrac{\\pi}{3}$',
        '• เครื่องหมายลบบอกว่า $\\theta$ ต้องอยู่ในจตุภาคที่สองหรือจตุภาคที่สี่',
        '• จตุภาคที่สอง : $\\theta = \\pi - \\dfrac{\\pi}{3} = \\dfrac{2\\pi}{3}$',
        '• จตุภาคที่สี่ : $\\theta = 2\\pi - \\dfrac{\\pi}{3} = \\dfrac{5\\pi}{3}$',
        '• ทั้งสองค่าอยู่ในช่วง $0 \\le \\theta < 2\\pi$ จริง จึงใช้ได้ทั้งคู่',
        '',
        '<b>ขั้นที่ 3 · หารกลับเป็นค่าของ $x$ แล้วเลือกค่าที่มากที่สุด</b>',
        '• จาก $\\theta = 2x$ ได้ $x = \\dfrac{\\theta}{2}$',
        '• สาขาที่หนึ่ง : $x = \\dfrac{1}{2} \\times \\dfrac{2\\pi}{3} = \\dfrac{\\pi}{3}$',
        '• สาขาที่สอง : $x = \\dfrac{1}{2} \\times \\dfrac{5\\pi}{3} = \\dfrac{5\\pi}{6}$',
        '• ตรวจว่าทั้งสองค่าอยู่ในช่วงที่โจทย์ให้ : $\\dfrac{\\pi}{3}$ ประมาณ $1.05$ '
        'และ $\\dfrac{5\\pi}{6}$ ประมาณ $2.62$ ซึ่งน้อยกว่า $\\pi$ ประมาณ $3.14$ ทั้งคู่',
        '• เปรียบเทียบสองค่าที่ได้ ค่าที่มากกว่าคือ $\\dfrac{5\\pi}{6}$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · เขียนสมการใหม่ให้อยู่ในรูปไซน์ตัวเดียว '
        'แล้วอ่านคำตอบทั้งหมดออกมาพร้อมกันโดยไม่ต้องไล่จตุภาค)</b>',
        '• คูณไขว้จาก $\\tan 2x = -\\sqrt{3}$ ได้ $\\sin 2x = -\\sqrt{3}\\cos 2x$ '
        'จึงเทียบเท่ากับ $\\sin 2x + \\sqrt{3}\\cos 2x = 0$ '
        'โดยการคูณไขว้นี้ทำได้เพราะแทนเจนต์นิยามได้ต้องมี $\\cos 2x$ ไม่เท่ากับศูนย์อยู่แล้ว',
        '• ดึงตัวประกอบ $2$ ออกมาแล้วจัดเป็นสูตรผลบวกมุม : '
        '$\\sin 2x + \\sqrt{3}\\cos 2x = 2\\left(\\dfrac{1}{2}\\sin 2x + \\dfrac{\\sqrt{3}}{2}\\cos 2x\\right)$ '
        'ซึ่งเท่ากับ $2\\left(\\sin 2x\\cos\\dfrac{\\pi}{3} + \\cos 2x\\sin\\dfrac{\\pi}{3}\\right) '
        '= 2\\sin\\left(2x + \\dfrac{\\pi}{3}\\right)$',
        '• สมการจึงเหลือ $\\sin\\left(2x + \\dfrac{\\pi}{3}\\right) = 0$ '
        'ซึ่งเป็นจริงก็ต่อเมื่อ $2x + \\dfrac{\\pi}{3} = k\\pi$ เมื่อ $k$ เป็นจำนวนเต็ม',
        '• ย้ายข้างแล้วหารด้วย $2$ : $x = \\dfrac{k\\pi}{2} - \\dfrac{\\pi}{6}$',
        '• ไล่ค่า $k$ ทีละค่า : $k = 0$ ได้ $x = -\\dfrac{\\pi}{6}$ ซึ่งอยู่นอกช่วง · '
        '$k = 1$ ได้ $x = \\dfrac{\\pi}{3}$ ซึ่งอยู่ในช่วง · '
        '$k = 2$ ได้ $x = \\dfrac{5\\pi}{6}$ ซึ่งอยู่ในช่วง · '
        '$k = 3$ ได้ $x = \\dfrac{4\\pi}{3}$ ซึ่งเกิน $\\pi$ จึงอยู่นอกช่วง',
        '• ได้ชุดคำตอบชุดเดียวกันกับวิธีแรกครบทั้งสองค่า และไม่มีคำตอบอื่นแทรกอยู่ระหว่างกลาง '
        'จึงยืนยันว่าค่าที่มากที่สุดคือ $\\dfrac{5\\pi}{6}$',
        '• แทนค่ากลับเข้าสมการเดิมเพื่อความมั่นใจ : เมื่อ $x = \\dfrac{5\\pi}{6}$ '
        'จะได้ $2x = \\dfrac{5\\pi}{3}$ ซึ่งอยู่ในจตุภาคที่สี่และมีมุมอ้างอิง $\\dfrac{\\pi}{3}$ '
        'ดังนั้น $\\tan\\dfrac{5\\pi}{3} = -\\tan\\dfrac{\\pi}{3} = -\\sqrt{3}$ ตรงกับสมการที่โจทย์ให้',
        '',
        '✅ <b>คำตอบ</b> $\\dfrac{5\\pi}{6}$ → <b>ตัวเลือก 2</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• กฎที่ใช้ได้กับสมการตรีโกณทุกข้อที่อาร์กิวเมนต์ไม่ใช่ $x$ เปล่า ๆ คือ '
        'คูณช่วงด้วยสัมประสิทธิ์หน้าตัวแปรก่อนเป็นอย่างแรก '
        'ถ้าสัมประสิทธิ์เป็น $2$ จำนวนคำตอบจะเป็นสองเท่า ถ้าเป็น $3$ ก็จะเป็นสามเท่า '
        'การนับจำนวนคำตอบที่ควรได้ตั้งแต่ต้นทำให้รู้ทันทีว่าไล่สาขาครบหรือยัง',
        '• เมื่อโจทย์ถามค่าที่มากที่สุดหรือน้อยที่สุด ให้แก้ให้ครบทุกคำตอบก่อนแล้วค่อยเลือก '
        'อย่ารีบหยุดที่คำตอบแรกที่เจอ เพราะคำตอบแรกที่เจอมักเป็นค่าที่เล็กที่สุด ไม่ใช่ค่าที่มากที่สุด',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $\\dfrac{\\pi}{3}$ เพราะไม่ได้ขยายช่วงของอาร์กิวเมนต์ '
        'คือไปไล่หา $2x$ ภายในช่วง $0 \\le 2x < \\pi$ ซึ่งเป็นช่วงของ $x$ ไม่ใช่ของ $2x$ '
        'จึงเจอสาขาเดียวคือ $2x = \\dfrac{2\\pi}{3}$ แล้วสรุปว่ามีคำตอบเดียว '
        'ค่านี้เป็นคำตอบจริงของสมการ แต่เป็นคำตอบที่น้อยกว่า ไม่ใช่ค่าที่มากที่สุด',
        '• ได้ $\\dfrac{11\\pi}{12}$ เพราะใช้มุมอ้างอิงผิดเป็น $\\dfrac{\\pi}{6}$ '
        'โดยสับสนระหว่าง $\\tan\\dfrac{\\pi}{6} = \\dfrac{1}{\\sqrt{3}}$ กับ $\\tan\\dfrac{\\pi}{3} = \\sqrt{3}$ '
        'จึงได้ $2x = \\dfrac{5\\pi}{6}$ กับ $2x = \\dfrac{11\\pi}{6}$ '
        'แล้วหารสองเป็น $\\dfrac{5\\pi}{12}$ กับ $\\dfrac{11\\pi}{12}$ '
        'ให้ตรวจด้วยการแทนกลับทุกครั้ง ค่านี้ให้ $\\tan\\dfrac{11\\pi}{6} = -\\dfrac{1}{\\sqrt{3}}$ '
        'ซึ่งไม่ตรงกับสมการ',
        '• ได้ $\\dfrac{5\\pi}{3}$ เพราะลืมหารด้วย $2$ ในขั้นสุดท้าย '
        'จึงรายงานค่าของอาร์กิวเมนต์ $\\theta$ ออกไปแทนค่าของ $x$ '
        'ค่านี้คัดทิ้งได้ทันทีด้วยการดูช่วงที่โจทย์ให้ เพราะ $\\dfrac{5\\pi}{3}$ '
        'มากกว่า $\\pi$ จึงอยู่นอกช่วงที่โจทย์อนุญาต',
    ],
    'V.mold: G = a tangent equation whose argument is a scaled variable, posed on a restricted interval / '
    'A = the greatest solution in that interval / M = expand the interval of the argument first, enumerate both '
    'tangent branches from the reference angle and the sign, divide back, then take the maximum. Rubric '
    'F1 C1 P1 T1 L0 = 4/15 with T at most 2 and total at least 3 -> level: ปานกลาง. sympy (verify_b14.py): '
    'route 1 runs solveset on tan(2x) + sqrt(3) over the half-open interval from 0 to pi and returns exactly '
    'two values, pi/3 and 5pi/6, whose maximum is 5pi/6; route 2 is independent, sweeping the sign of '
    'sin(2x) + sqrt(3)cos(2x) numerically over 200000 subdivisions and finding exactly two sign changes whose '
    'larger location matches 5pi/6 to within 1e-4, so it neither uses solveset nor the branch enumeration. All '
    'three distractors machine-computed from named error paths: pi/3 is confirmed to be a genuine solution of '
    'the equation that arises from failing to expand the argument interval, 11pi/12 is produced by re-running '
    'the branch enumeration with the reference angle pi/6 instead of pi/3 and taking the maximum, and 5pi/3 is '
    'produced by solving for theta = 2x over a full turn and reporting the largest theta without dividing by '
    'two. A guard asserts the four values are pairwise distinct numerically and that the cheapest check '
    'available to a student, namely the requirement that the answer lie in the interval from 0 to pi, '
    'eliminates only 5pi/3, so two distractors survive it. Collision sweep on 6387 items across three probe '
    'rounds: the phrase asking for the greatest solution of a trigonometric equation on a bounded interval '
    'returns 0 hits in chapter 7, and the phrasing probe for the greatest value satisfying an equation returns '
    'one hit that lies in chapter 3 only. This item deliberately avoids the sum-of-solutions ask, which the '
    'registry marks as saturated at 77 items across the bank.',
)

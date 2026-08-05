# -*- coding: utf-8 -*-
add(
    101,
    ['7.1', '7.2'],
    'ปานกลาง',
    'กำหนดให้ $\\theta$ เป็นมุมในจตุภาคที่ 3 '
    'ซึ่งสอดคล้องกับสมการ $3\\sin\\theta = 2\\cos\\theta$ '
    'ค่าของ $\\csc\\theta$ เท่ากับข้อใด',
    [
        '$-\\dfrac{\\sqrt{13}}{2}$',
        '$-\\dfrac{\\sqrt{13}}{3}$',
        '$\\dfrac{3}{2}$',
        '$\\dfrac{\\sqrt{13}}{2}$',
    ],
    0,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• นิยามของแทนเจนต์ : $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        'ใช้ได้เมื่อ $\\cos\\theta \\ne 0$ '
        'ประโยชน์ของนิยามนี้คือ ถ้าสมการมีทั้ง $\\sin\\theta$ และ $\\cos\\theta$ '
        'ที่กำลังหนึ่งเท่ากันทั้งคู่ เราหารทั้งสมการด้วย $\\cos\\theta$ '
        'แล้วจะยุบตัวแปรสองตัวให้เหลือ $\\tan\\theta$ ตัวเดียวได้ทันที',
        '• ฟังก์ชันส่วนกลับสามตัวที่ต้องแยกให้ออก : '
        '$\\csc\\theta = \\dfrac{1}{\\sin\\theta}$ · '
        '$\\sec\\theta = \\dfrac{1}{\\cos\\theta}$ · '
        '$\\cot\\theta = \\dfrac{\\cos\\theta}{\\sin\\theta} = \\dfrac{1}{\\tan\\theta}$ '
        '⛔ จุดที่สับสนกันมากที่สุดคือ $\\csc$ เป็นส่วนกลับของ $\\sin$ '
        'ส่วน $\\sec$ เป็นส่วนกลับของ $\\cos$ '
        'ให้จำจากตัวอักษรตัวที่สามของชื่อแทนตัวแรก',
        '• สามเหลี่ยมอ้างอิง : ถ้ารู้ค่า $\\tan$ ของมุมเป็นเศษส่วนของจำนวนเต็ม '
        'ให้วาดสามเหลี่ยมมุมฉากที่ด้านตรงข้ามยาวเท่ากับตัวเศษ และด้านประชิดยาวเท่ากับตัวส่วน '
        'แล้วใช้ทฤษฎีบทพีทาโกรัส $c^2 = a^2 + b^2$ '
        'หาความยาวด้านตรงข้ามมุมฉาก จากนั้นอ่านอัตราส่วนตัวอื่นออกมาได้ครบทุกตัว',
        '• เครื่องหมายตามจตุภาค : บนวงกลมหนึ่งหน่วย $\\sin\\theta$ คือพิกัด $y$ '
        'และ $\\cos\\theta$ คือพิกัด $x$ ของจุดปลายส่วนโค้ง '
        'จตุภาคที่ 3 อยู่ล่างซ้าย ทั้ง $x$ และ $y$ จึงติดลบทั้งคู่ '
        'ผลคือ $\\sin\\theta < 0$ และ $\\cos\\theta < 0$ '
        'แต่ $\\tan\\theta > 0$ เพราะลบหารลบได้บวก',
        '• ฟังก์ชันส่วนกลับมีเครื่องหมายเหมือนตัวตั้งต้นเสมอ '
        'เพราะ $1$ เป็นจำนวนบวก การหาร $1$ ด้วยจำนวนลบย่อมได้จำนวนลบ '
        'ดังนั้น $\\csc\\theta$ ติดลบเมื่อ $\\sin\\theta$ ติดลบ '
        'และ $\\cot\\theta$ ต้องมีเครื่องหมายเดียวกับ $\\tan\\theta$ นั่นคือ<b>เป็นบวก</b>ในจตุภาคที่ 3',
        '• การจัดรูปเศษส่วนที่มีรากที่สองอยู่ที่ตัวส่วน : '
        '$\\dfrac{1}{\\left(\\dfrac{a}{\\sqrt{n}}\\right)} = \\dfrac{\\sqrt{n}}{a}$ '
        'เพราะการหารด้วยเศษส่วนคือการคูณด้วยส่วนกลับของตัวหาร '
        'ตัวเศษกับตัวส่วนของตัวหารจึงสลับที่กัน',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• มุม $\\theta$ อยู่ในจตุภาคที่ 3',
        '• $\\theta$ สอดคล้องกับสมการ $3\\sin\\theta = 2\\cos\\theta$',
        '• สังเกตหน้าตาก่อนลงมือ : สมการนี้มี $\\sin\\theta$ และ $\\cos\\theta$ '
        'อยู่คนละข้าง โดยทั้งคู่เป็นกำลังหนึ่งและไม่มีพจน์ค่าคงตัวโดด ๆ เลย '
        'หน้าตาแบบนี้แปลว่าหารด้วย $\\cos\\theta$ ได้ทันทีแล้วจะเหลือ $\\tan\\theta$ ตัวเดียว',
        '• สมการบอกได้แค่<b>อัตราส่วน</b>ระหว่างไซน์กับโคไซน์ ไม่ได้บอกเครื่องหมาย '
        'เครื่องหมายต้องไปหยิบจากเงื่อนไขจตุภาคที่ 3 ที่โจทย์กำหนดมาต่างหาก',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\csc\\theta$ ซึ่งเป็นส่วนกลับของ $\\sin\\theta$',
        '',
        '<b>【 หารสมการด้วย $\\cos\\theta$ ให้เหลือ $\\tan\\theta$ ตัวเดียว '
        'อ่านความยาวด้านทั้งสามจากสามเหลี่ยมอ้างอิงเพื่อได้ขนาดของ $\\sin\\theta$ '
        'เติมเครื่องหมายลบตามจตุภาคที่ 3 แล้วจึงพลิกกลับเป็น $\\csc\\theta$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · ยุบสมการสองฟังก์ชันให้เหลือ $\\tan\\theta$ ตัวเดียว</b>',
        '• สูตรที่ใช้ : $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$',
        '• ตรวจก่อนว่าหารได้ไหม : ถ้า $\\cos\\theta = 0$ สมการจะกลายเป็น '
        '$3\\sin\\theta = 0$ ทำให้ $\\sin\\theta = 0$ ด้วย '
        'แต่ $\\sin^2\\theta + \\cos^2\\theta = 1$ บอกว่าทั้งสองตัวเป็นศูนย์พร้อมกันไม่ได้ '
        'จึงสรุปว่า $\\cos\\theta \\ne 0$ หารได้อย่างปลอดภัย',
        '• นำสมการ $3\\sin\\theta = 2\\cos\\theta$ มาหารทั้งสองข้างด้วย $\\cos\\theta$ '
        'ได้ $\\dfrac{3\\sin\\theta}{\\cos\\theta} = \\dfrac{2\\cos\\theta}{\\cos\\theta}$',
        '• ข้างขวา $\\cos\\theta$ ตัดกันเหลือ $2$ · '
        'ข้างซ้ายจับ $3$ ออกมาไว้หน้าได้ $3 \\times \\dfrac{\\sin\\theta}{\\cos\\theta} = 3\\tan\\theta$',
        '• สมการจึงเหลือ $3\\tan\\theta = 2$ '
        'หารทั้งสองข้างด้วย $3$ ได้ $\\tan\\theta = \\dfrac{2}{3}$',
        '• เช็คความสมเหตุสมผลทันที : ค่าที่ได้เป็นบวก '
        'ซึ่งตรงกับข้อเท็จจริงว่าแทนเจนต์เป็นบวกในจตุภาคที่ 3 พอดี ไม่ขัดกับเงื่อนไขที่โจทย์ให้',
        '',
        '<b>ขั้นที่ 2 · อ่านขนาดของอัตราส่วนจากสามเหลี่ยมอ้างอิง</b>',
        '• สูตรที่ใช้ : ทฤษฎีบทพีทาโกรัส $c^2 = a^2 + b^2$ '
        'โดย $a$ คือด้านตรงข้ามมุมอ้างอิง $b$ คือด้านประชิด และ $c$ คือด้านตรงข้ามมุมฉาก',
        '• ระบุตัวแปรจากค่า $\\tan\\theta = \\dfrac{2}{3}$ : '
        'เนื่องจากแทนเจนต์คือด้านตรงข้ามหารด้านประชิด จึงตั้ง $a = 2$ และ $b = 3$',
        '• แทนค่า : $c^2 = 2^2 + 3^2 = 4 + 9 = 13$ '
        'ถอดรากที่สองได้ $c = \\sqrt{13}$ ซึ่งมีค่าประมาณ $3.606$',
        '• อ่านขนาดของไซน์จากสามเหลี่ยมนี้ : ไซน์คือด้านตรงข้ามหารด้านตรงข้ามมุมฉาก '
        'จึงได้ขนาดเท่ากับ $\\dfrac{a}{c} = \\dfrac{2}{\\sqrt{13}}$',
        '• ⛔ ย้ำว่าค่านี้เป็นเพียง<b>ขนาด</b>ที่ได้จากรูปสามเหลี่ยม '
        'ซึ่งด้านทุกด้านยาวเป็นบวกเสมอ ยังไม่ใช่ค่าของ $\\sin\\theta$ จริง ๆ '
        'เพราะยังไม่ได้ใส่เครื่องหมายตามจตุภาค',
        '',
        '<b>ขั้นที่ 3 · เติมเครื่องหมายตามจตุภาคที่ 3</b>',
        '• กฎที่ใช้ : ในจตุภาคที่ 3 จุดปลายส่วนโค้งบนวงกลมหนึ่งหน่วยมีทั้งพิกัด $x$ '
        'และพิกัด $y$ เป็นลบ ดังนั้น $\\sin\\theta < 0$ และ $\\cos\\theta < 0$',
        '• นำเครื่องหมายลบไปติดกับขนาดที่ได้จากขั้นที่ 2 : '
        '$\\sin\\theta = -\\dfrac{2}{\\sqrt{13}}$ และ $\\cos\\theta = -\\dfrac{3}{\\sqrt{13}}$',
        '• ตรวจกับสมการต้นทางว่าคู่นี้ใช้ได้จริง : '
        'ข้างซ้าย $3 \\times \\left(-\\dfrac{2}{\\sqrt{13}}\\right) = -\\dfrac{6}{\\sqrt{13}}$ · '
        'ข้างขวา $2 \\times \\left(-\\dfrac{3}{\\sqrt{13}}\\right) = -\\dfrac{6}{\\sqrt{13}}$ '
        'สองข้างเท่ากันพอดี ✓',
        '• ตรวจกับเอกลักษณ์หลัก : '
        '$\\sin^2\\theta + \\cos^2\\theta = \\dfrac{4}{13} + \\dfrac{9}{13} = \\dfrac{13}{13} = 1$ ✓ '
        'แปลว่าคู่ค่านี้เป็นจุดที่อยู่บนวงกลมหนึ่งหน่วยจริง',
        '',
        '<b>ขั้นที่ 4 · พลิก $\\sin\\theta$ กลับเป็น $\\csc\\theta$</b>',
        '• สูตรที่ใช้ : $\\csc\\theta = \\dfrac{1}{\\sin\\theta}$',
        '• แทนค่า $\\sin\\theta = -\\dfrac{2}{\\sqrt{13}}$ ลงไป ได้ '
        '$\\csc\\theta = 1 \\div \\left(-\\dfrac{2}{\\sqrt{13}}\\right)$',
        '• หารด้วยเศษส่วนคือคูณด้วยส่วนกลับของตัวหาร จึงได้ '
        '$\\csc\\theta = 1 \\times \\left(-\\dfrac{\\sqrt{13}}{2}\\right) = -\\dfrac{\\sqrt{13}}{2}$',
        '• ประเมินค่าเป็นทศนิยมเพื่อดูความสมเหตุสมผล : '
        '$-\\dfrac{\\sqrt{13}}{2}$ มีค่าประมาณ $-1.803$ '
        'ซึ่งมีขนาดมากกว่า $1$ ตามที่ควรเป็น เพราะ $\\csc$ เป็นส่วนกลับของ $\\sin$ '
        'ที่มีขนาดไม่เกิน $1$ เสมอ',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไม่วาดสามเหลี่ยมอ้างอิงเลย แต่ใช้เอกลักษณ์ '
        '$1 + \\cot^2\\theta = \\csc^2\\theta$)</b>',
        '• เอกลักษณ์นี้ได้จากการหาร $\\sin^2\\theta + \\cos^2\\theta = 1$ '
        'ตลอดทั้งสมการด้วย $\\sin^2\\theta$ จึงใช้ได้เมื่อ $\\sin\\theta \\ne 0$',
        '• จากขั้นที่ 1 เรามี $\\tan\\theta = \\dfrac{2}{3}$ '
        'ดังนั้น $\\cot\\theta = \\dfrac{1}{\\tan\\theta} = \\dfrac{3}{2}$',
        '• แทนลงเอกลักษณ์ : '
        '$\\csc^2\\theta = 1 + \\left(\\dfrac{3}{2}\\right)^2 = 1 + \\dfrac{9}{4} = \\dfrac{13}{4}$',
        '• ถอดรากที่สองทั้งสองข้าง ได้สองความเป็นไปได้คือ '
        '$\\csc\\theta = \\dfrac{\\sqrt{13}}{2}$ หรือ $\\csc\\theta = -\\dfrac{\\sqrt{13}}{2}$',
        '• ตัดสินเครื่องหมายด้วยเงื่อนไขจตุภาคที่ 3 : ที่นั่น $\\sin\\theta$ ติดลบ '
        'ส่วนกลับของจำนวนลบก็ยังเป็นจำนวนลบ จึงต้องเลือกค่าที่ติดลบ',
        '• ได้ $\\csc\\theta = -\\dfrac{\\sqrt{13}}{2}$ ตรงกับผลของเส้นทางแรกทุกประการ ✓ '
        'เส้นทางนี้ไม่ผ่านการหาความยาวด้านของรูปสามเหลี่ยมเลย จึงยืนยันได้อย่างเป็นอิสระ',
        '',
        '✅ <b>คำตอบ</b> ค่าของ $\\csc\\theta$ เท่ากับ $-\\dfrac{\\sqrt{13}}{2}$ → <b>ตัวเลือก 1</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอสมการที่มี $\\sin$ กับ $\\cos$ กำลังหนึ่งอยู่คนละข้างและไม่มีพจน์ค่าคงตัว '
        'ให้หารด้วย $\\cos$ ทันที นี่เป็นทางลัดมาตรฐานที่เปลี่ยนสมการสองฟังก์ชันให้เหลือฟังก์ชันเดียว',
        '• แยกงานเป็นสองชั้นเสมอ ชั้นแรกหา<b>ขนาด</b>จากสามเหลี่ยมอ้างอิง '
        'ชั้นที่สองหา<b>เครื่องหมาย</b>จากจตุภาค ถ้ารวบสองชั้นเป็นก้าวเดียวจะลืมเครื่องหมายเกือบทุกครั้ง',
        '• วิธีตรวจเครื่องหมายที่เร็วที่สุดคือจำว่าฟังก์ชันส่วนกลับมีเครื่องหมายเดียวกับตัวตั้งต้น '
        '$\\csc$ ตามเครื่องหมาย $\\sin$ · $\\sec$ ตามเครื่องหมาย $\\cos$ · '
        '$\\cot$ ตามเครื่องหมาย $\\tan$ ซึ่งในจตุภาคที่ 3 จะได้ลบ ลบ และบวก ตามลำดับ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $-\\dfrac{\\sqrt{13}}{3}$ เพราะพลิกผิดตัว คือไปหาส่วนกลับของ $\\cos\\theta$ '
        'แทนที่จะเป็นส่วนกลับของ $\\sin\\theta$ '
        'ซึ่งให้ $\\dfrac{1}{\\cos\\theta} = 1 \\div \\left(-\\dfrac{3}{\\sqrt{13}}\\right) = -\\dfrac{\\sqrt{13}}{3}$ · '
        'ค่านี้คือ $\\sec\\theta$ ไม่ใช่ $\\csc\\theta$ '
        'พิสูจน์ว่าผิดได้ด้วยนิยาม เพราะถ้าค่านี้เป็น $\\csc\\theta$ จริง '
        'ผลคูณ $\\sin\\theta \\times \\csc\\theta$ ต้องเท่ากับ $1$ '
        'แต่คำนวณจริงได้ $\\left(-\\dfrac{2}{\\sqrt{13}}\\right)\\left(-\\dfrac{\\sqrt{13}}{3}\\right) = \\dfrac{2}{3}$ ซึ่งไม่ใช่ $1$ · '
        'วิธีกันคือท่องว่าตัวอักษรตัวที่สามของ $\\csc$ คือ $c$ ซึ่งชี้ไปที่ $\\sin$ ไม่ใช่ $\\cos$',
        '• ได้ค่า $\\dfrac{3}{2}$ เพราะเดินไปจนถึง $\\cot\\theta$ แล้วหยุด ไม่ได้พลิกต่อไปหา $\\csc\\theta$ '
        '⭐ จุดที่ต้องอ่านให้ละเอียดคือค่านี้<b>เป็นจำนวนบวก</b> ไม่ใช่จำนวนลบ '
        'เพราะ $\\cot\\theta = \\dfrac{\\cos\\theta}{\\sin\\theta} = \\dfrac{-3/\\sqrt{13}}{-2/\\sqrt{13}}$ '
        'ซึ่งเป็นลบหารลบ เครื่องหมายลบทั้งบนและล่างตัดกันหายไป เหลือ $\\dfrac{3}{2}$ พอดี · '
        'ผลลัพธ์นี้สอดคล้องกับ $\\cot\\theta = \\dfrac{1}{\\tan\\theta} = \\dfrac{3}{2}$ '
        'ซึ่งเป็นบวกอยู่แล้วเพราะแทนเจนต์เป็นบวกในจตุภาคที่ 3 '
        'ดังนั้นเด็กที่คิดว่า “อยู่จตุภาคที่ 3 ทุกค่าต้องติดลบ” จึงเข้าใจผิด · '
        'ค่านี้ผิดเพราะไม่ใช่สิ่งที่โจทย์ถาม พิสูจน์ได้ด้วย $\\sin\\theta \\times \\csc\\theta = 1$ '
        'ซึ่งถ้าใช้ $\\dfrac{3}{2}$ จะได้ '
        '$\\left(-\\dfrac{2}{\\sqrt{13}}\\right)\\left(\\dfrac{3}{2}\\right) = -\\dfrac{3}{\\sqrt{13}}$ '
        'ซึ่งไม่ใช่ $1$ · '
        'สังเกตอีกอย่างว่าค่านี้มีขนาด $1.5$ ในขณะที่คำตอบจริงมีขนาดประมาณ $1.803$ จึงไม่ใช่ค่าเดียวกัน',
        '• ได้ค่า $\\dfrac{\\sqrt{13}}{2}$ เพราะข้ามขั้นที่ 3 ไปเลย '
        'คืออ่านขนาด $\\dfrac{2}{\\sqrt{13}}$ จากสามเหลี่ยมอ้างอิงแล้วพลิกทันทีโดยไม่ใส่เครื่องหมายลบ · '
        'ค่านี้ผิดเพราะขัดกับเงื่อนไขจตุภาคที่โจทย์กำหนด '
        'ถ้า $\\csc\\theta$ เป็นบวก แปลว่า $\\sin\\theta = \\dfrac{2}{\\sqrt{13}}$ เป็นบวก '
        'และเมื่อแทนกลับในสมการ $3\\sin\\theta = 2\\cos\\theta$ '
        'จะบังคับให้ $\\cos\\theta = \\dfrac{3}{\\sqrt{13}}$ เป็นบวกตามไปด้วย '
        'มุมที่มีทั้งไซน์และโคไซน์เป็นบวกย่อมอยู่ในจตุภาคที่ 1 ไม่ใช่จตุภาคที่ 3 ตามที่โจทย์บอก · '
        'วิธีกันคืออ่านเงื่อนไขจตุภาคซ้ำอีกครั้งก่อนวงคำตอบทุกครั้ง',
        '• อีกทางที่พลาดกันบ่อยคือสลับด้านของสามเหลี่ยมอ้างอิง '
        'โดยเผลออ่านว่า $\\tan\\theta = \\dfrac{3}{2}$ จากตัวเลข $3$ กับ $2$ ที่เห็นในสมการ '
        'ทั้งที่การหารด้วย $\\cos\\theta$ ให้ $\\tan\\theta = \\dfrac{2}{3}$ '
        'การสลับนี้ทำให้ได้ $\\sin\\theta = -\\dfrac{3}{\\sqrt{13}}$ '
        'และพลิกออกมาเป็น $-\\dfrac{\\sqrt{13}}{3}$ '
        'ซึ่งไปตรงกับค่าที่เกิดจากการพลิกผิดตัวพอดี ทำให้เส้นทางผิดสองแบบมาบรรจบกันที่ค่าเดียวกัน · '
        'ตัวจับผิดที่เร็วที่สุดคือย้อนกลับไปดูสมการ ตัวเลข $3$ อยู่หน้า $\\sin\\theta$ '
        'จึงต้องไปโผล่ที่<b>ตัวส่วน</b>ของ $\\tan\\theta$ ไม่ใช่ตัวเศษ',
    ],
    'V.mold: G = a linear equation tying sine and cosine of the same angle together, plus the single '
    'extra fact that the angle sits in the third quadrant / A = the value of the cosecant of that angle / '
    'M = divide the equation through by cosine to collapse it to a tangent value, read the missing side '
    'off a reference triangle with Pythagoras, attach the quadrant sign to the sine, then invert. '
    'Rubric F2 C1 P2 T1 L0 = 6/15 -> level: ปานกลาง. '
    'F = 2 because two separate knowledge blocks are needed and neither can be skipped: the quotient '
    'definition of tangent that lets the equation be divided through, and the reciprocal definitions that '
    'tell cosecant apart from secant and cotangent. F is not 3 because no identity beyond the Pythagorean '
    'one is required and there is no case split. C = 1 because the item is stitched from subtopic 7.1 '
    '(ratios and the reference triangle) and subtopic 7.2 (signs by quadrant); one join only, so not 2. '
    'P = 2 because the work really does fall into two stages that cannot be merged: the first stage '
    'produces a magnitude from the triangle, and the second stage reinterprets that magnitude by giving '
    'it a sign before the inversion is allowed. The benchmark is q086, where filling in a missing ratio '
    'first and only then substituting was likewise recorded as a two-stage chain rather than one closing '
    'computation. T = 1 and not 2 because the quadrant is stated outright in the question and does not '
    'have to be inferred; the benchmark is q097 in this same block, held at T = 1 for exactly that '
    'reason. L = 0 because the statement is bare symbol talk with no worded scene to model at all; the '
    'benchmarks are q030 and q060, both held at L = 0 for the same reason. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b18.py): with s101 = -2/sqrt(13) and c101 = -3/sqrt(13), the check 3*s101 - 2*c101 '
    'returns 0, so the pair really does satisfy the given equation, and s101**2 + c101**2 returns 1, so '
    'the pair really is a point of the unit circle; both signs are negative, which is what the third '
    'quadrant demands. The answer 1/s101 was machine-simplified to -sqrt(13)/2. Every distractor was '
    'machine-computed from a named error path rather than invented: 1/(2/sqrt(13)) returns sqrt(13)/2 for '
    'dropping the quadrant sign, 1/c101 returns -sqrt(13)/3 for inverting the cosine instead of the sine, '
    'and c101/s101 returns Rational(3, 2) for stopping at the cotangent. That last value is worth '
    'spelling out: the machine result is positive three halves, not negative, because the two minus signs '
    'cancel in the quotient, and it agrees with 1/tan = 3/2 since tangent is positive in the third '
    'quadrant; the explanation says so explicitly. '
    'Collision sweep on 6407 items (bank 62 files + k1 out + k2 out), probe collide_b18b.py: the scan '
    'looked for items whose question text hands over a linear relation between sine and cosine of one '
    'angle and then asks for a reciprocal function value; the result set is empty, so no item in the '
    'corpus runs this mould. Nearby items hand over one ratio directly and ask for another, matching on '
    'G alone and not on M. '
    'Choices are ordered ascending by numeric value (about -1.803, then about -1.202, then 1.5, then '
    'about 1.803), so the answer slot is forced by that rule and was not chosen.',
)

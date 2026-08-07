# -*- coding: utf-8 -*-
add(
    142,
    ['7.4'],
    'ง่าย',
    'กำหนดให้ $\\theta$ เป็นจำนวนจริงซึ่ง $\\cos\\theta \\ne 0$ และ $\\tan\\theta = 4$ '
    'ค่าของ $\\dfrac{3\\sin\\theta - 2\\cos\\theta}{\\sin\\theta + 5\\cos\\theta}$ เท่ากับข้อใด',
    [
        '$-\\dfrac{5}{21}$',
        '$\\dfrac{9}{10}$',
        '$\\dfrac{10}{9}$',
        '$\\dfrac{14}{9}$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• นิยามของ $\\tan$ ในรูปของ $\\sin$ กับ $\\cos$ : $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        'นิยามนี้เขียนได้ก็ต่อเมื่อ $\\cos\\theta \\ne 0$ เพราะตัวส่วนของเศษส่วนห้ามเป็นศูนย์ · '
        'ตัวที่คู่กันคือ $\\cot\\theta = \\dfrac{\\cos\\theta}{\\sin\\theta}$ ซึ่งเป็นส่วนกลับของ $\\tan\\theta$ '
        '⇒ ถ้า $\\tan\\theta = 4$ แล้ว $\\cot\\theta = \\dfrac{1}{4}$ ⛔ ไม่ใช่ $4$',
        '• การหารทั้งเศษและทั้งส่วนด้วยจำนวนเดียวกันไม่ทำให้ค่าของเศษส่วนเปลี่ยน : '
        'ถ้า $c \\ne 0$ แล้ว $\\dfrac{a}{b} = \\dfrac{a \\div c}{b \\div c}$ '
        'เหตุผลคือการหารข้างบนและข้างล่างด้วย $c$ ก็คือการคูณทั้งสองข้างด้วย $\\dfrac{1}{c}$ พร้อมกัน '
        'ซึ่งเท่ากับคูณเศษส่วนเดิมด้วย $1$ ⇒ เปลี่ยนแค่หน้าตา ไม่เปลี่ยนค่า',
        '• การหารผลบวกหรือผลต่างด้วยจำนวนหนึ่ง ให้หารเข้าไปทีละพจน์ : '
        '$\\dfrac{x + y}{c} = \\dfrac{x}{c} + \\dfrac{y}{c}$ '
        'และตัวเลขที่คูณอยู่หน้าพจน์ดึงออกมาไว้นอกเศษส่วนได้ '
        '⇒ $\\dfrac{3\\sin\\theta}{\\cos\\theta} = 3 \\times \\dfrac{\\sin\\theta}{\\cos\\theta} = 3\\tan\\theta$ '
        'ส่วน $\\dfrac{\\cos\\theta}{\\cos\\theta}$ ยุบเหลือ $1$ เพราะตัวเหมือนกันหารกันลงตัวเสมอ',
        '• ⭐ กุญแจของข้อนี้ : ถ้าเศษกับส่วนของเศษส่วนหนึ่ง <b>เป็นพจน์ดีกรีหนึ่งใน '
        '$\\sin\\theta$ และ $\\cos\\theta$ เหมือนกันทั้งคู่</b> '
        'คือทุกพจน์เป็นค่าคงที่คูณกับ $\\sin\\theta$ หรือ $\\cos\\theta$ เพียงตัวเดียว '
        'ไม่มีกำลังสอง ไม่มีผลคูณของสองตัว และไม่มีพจน์ที่เป็นตัวเลขโดด ๆ '
        'แล้วการหารทั้งเศษและส่วนด้วย $\\cos\\theta$ จะทำให้ทุกพจน์กลายเป็น $\\tan\\theta$ หรือค่าคงที่จนหมด '
        '⇒ รู้ค่า $\\tan\\theta$ เพียงค่าเดียวก็แทนลงไปได้ทันที',
        '• สามเหลี่ยมอ้างอิงที่จะใช้ตอนตรวจคำตอบ : ถ้า $\\tan\\theta = 4 = \\dfrac{4}{1}$ '
        'และ $\\theta$ อยู่ในจตุภาคที่ $1$ จะวาดรูปสามเหลี่ยมมุมฉากที่มีด้านตรงข้ามมุม $\\theta$ ยาว $4$ '
        'และด้านประชิดยาว $1$ ⇒ ด้านตรงข้ามมุมฉากยาว $\\sqrt{4^2 + 1^2} = \\sqrt{17}$ ตามพีทาโกรัส '
        '⇒ $\\sin\\theta = \\dfrac{4}{\\sqrt{17}}$ และ $\\cos\\theta = \\dfrac{1}{\\sqrt{17}}$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $\\theta$ เป็นจำนวนจริง โดยมีเงื่อนไขกำกับว่า $\\cos\\theta \\ne 0$',
        '• $\\tan\\theta = 4$',
        '• นิพจน์ที่ต้องหาค่าคือ $\\dfrac{3\\sin\\theta - 2\\cos\\theta}{\\sin\\theta + 5\\cos\\theta}$',
        '• สังเกตหน้าตาก่อนลงมือ : เศษมีสองพจน์คือ $3\\sin\\theta$ กับ $-2\\cos\\theta$ '
        'และส่วนก็มีสองพจน์คือ $\\sin\\theta$ กับ $5\\cos\\theta$ '
        'ทุกพจน์เป็นค่าคงที่คูณกับ $\\sin\\theta$ หรือ $\\cos\\theta$ ตัวเดียวล้วน ๆ '
        '⇒ เศษกับส่วน<b>เป็นพจน์ดีกรีหนึ่งเหมือนกันทั้งคู่</b> ตรงกับหน้าตาที่หารด้วย $\\cos\\theta$ แล้วยุบได้',
        '• สังเกตอีกอย่าง : โจทย์ให้ค่ามาเพียงค่าเดียวคือ $\\tan\\theta$ '
        'ไม่ได้บอกว่า $\\theta$ อยู่ในจตุภาคใด และไม่ได้ให้ $\\sin\\theta$ กับ $\\cos\\theta$ แยกกันมาเลย '
        '⇒ เป็นสัญญาณว่าเส้นทางที่ถูกต้องต้องเดินด้วย $\\tan\\theta$ ตัวเดียวจนจบ',
        '• เงื่อนไข $\\cos\\theta \\ne 0$ ที่โจทย์แถมมาไม่ใช่ของประดับ '
        'แต่เป็นใบอนุญาตให้หารทั้งเศษและส่วนด้วย $\\cos\\theta$ ได้อย่างถูกต้อง '
        'และยังเป็นเงื่อนไขที่ทำให้ $\\tan\\theta$ มีค่าจริง ๆ ด้วย',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\dfrac{3\\sin\\theta - 2\\cos\\theta}{\\sin\\theta + 5\\cos\\theta}$ ออกมาเป็นตัวเลขค่าเดียว '
        'โดยใช้ข้อมูลเพียงว่า $\\tan\\theta = 4$',
        '',
        '<b>【 หารทั้งเศษและทั้งส่วนด้วย $\\cos\\theta$ ซึ่งทำได้เพราะโจทย์รับรองว่า $\\cos\\theta \\ne 0$ '
        'ทุกพจน์จะยุบกลายเป็น $\\tan\\theta$ หรือค่าคงที่ '
        'เหลือรูป $\\dfrac{3\\tan\\theta - 2}{\\tan\\theta + 5}$ แล้วแทน $\\tan\\theta = 4$ ลงไปตรง ๆ 】</b>',
        '',
        '<b>ขั้นที่ 1 · ตรวจใบอนุญาตก่อนหาร แล้วเลือกตัวหารให้ถูกตัว</b>',
        '• สูตรที่ใช้ : $\\dfrac{a}{b} = \\dfrac{a \\div c}{b \\div c}$ เมื่อ $c \\ne 0$',
        '• ระบุตัวแปรให้ชัดก่อนแทนค่า : $a = 3\\sin\\theta - 2\\cos\\theta$ คือเศษ '
        '· $b = \\sin\\theta + 5\\cos\\theta$ คือส่วน · $c = \\cos\\theta$ คือตัวที่จะเอาไปหารทั้งสองข้าง',
        '• ตรวจเงื่อนไข $c \\ne 0$ : ผ่านทันที เพราะโจทย์เขียนไว้ตรง ๆ ว่า $\\cos\\theta \\ne 0$ '
        '⛔ ถ้าโจทย์ไม่ได้เขียนบรรทัดนี้ไว้ จะหารด้วย $\\cos\\theta$ ทันทีไม่ได้ ต้องแยกกรณีก่อน',
        '• ทำไมต้องหารด้วย $\\cos\\theta$ ไม่ใช่ $\\sin\\theta$ : เพราะค่าที่โจทย์ให้มาคือ $\\tan\\theta$ '
        'ซึ่งมี $\\cos\\theta$ อยู่ที่ตัวส่วนตามนิยาม $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        '⇒ หารด้วย $\\cos\\theta$ แล้วจะได้ $\\tan\\theta$ โผล่ออกมาพอดี',
        '• เขียนรูปที่จะทำงานต่อ : นิพจน์ '
        '$= \\dfrac{(3\\sin\\theta - 2\\cos\\theta) \\div \\cos\\theta}{(\\sin\\theta + 5\\cos\\theta) \\div \\cos\\theta}$ '
        '⇒ ต่อจากนี้แค่จัดการข้างบนกับข้างล่างทีละก้อน',
        '',
        '<b>ขั้นที่ 2 · หารเศษด้วย $\\cos\\theta$</b>',
        '• สูตรที่ใช้ : $\\dfrac{x + y}{c} = \\dfrac{x}{c} + \\dfrac{y}{c}$ คือหารเข้าไปทีละพจน์',
        '• ระบุตัวแปร : $x = 3\\sin\\theta$ · $y = -2\\cos\\theta$ · $c = \\cos\\theta$',
        '• แทนค่า : $\\dfrac{3\\sin\\theta - 2\\cos\\theta}{\\cos\\theta} '
        '= \\dfrac{3\\sin\\theta}{\\cos\\theta} - \\dfrac{2\\cos\\theta}{\\cos\\theta}$',
        '• ยุบทีละก้อน : ก้อนแรก $\\dfrac{3\\sin\\theta}{\\cos\\theta} = 3\\tan\\theta$ ตามนิยามของ $\\tan$ '
        '· ก้อนหลัง $\\dfrac{2\\cos\\theta}{\\cos\\theta} = 2$ เพราะ $\\cos\\theta$ ตัดกันหมด '
        '(ตัดได้เพราะ $\\cos\\theta \\ne 0$)',
        '• สรุปเศษใหม่ : $3\\tan\\theta - 2$ ⇒ ไม่มี $\\sin\\theta$ กับ $\\cos\\theta$ หลงเหลืออยู่เลย',
        '',
        '<b>ขั้นที่ 3 · หารส่วนด้วย $\\cos\\theta$ ด้วยวิธีเดียวกัน</b>',
        '• สูตรที่ใช้ : $\\dfrac{x + y}{c} = \\dfrac{x}{c} + \\dfrac{y}{c}$ เหมือนขั้นที่ 2',
        '• ระบุตัวแปร : $x = \\sin\\theta$ · $y = 5\\cos\\theta$ · $c = \\cos\\theta$',
        '• แทนค่า : $\\dfrac{\\sin\\theta + 5\\cos\\theta}{\\cos\\theta} '
        '= \\dfrac{\\sin\\theta}{\\cos\\theta} + \\dfrac{5\\cos\\theta}{\\cos\\theta}$',
        '• ยุบ : $\\dfrac{\\sin\\theta}{\\cos\\theta} = \\tan\\theta$ และ '
        '$\\dfrac{5\\cos\\theta}{\\cos\\theta} = 5$ ⇒ ส่วนใหม่คือ $\\tan\\theta + 5$',
        '• ประกอบเศษกับส่วนที่ยุบแล้วเข้าด้วยกัน : '
        '$\\dfrac{3\\sin\\theta - 2\\cos\\theta}{\\sin\\theta + 5\\cos\\theta} '
        '= \\dfrac{3\\tan\\theta - 2}{\\tan\\theta + 5}$ '
        '⇒ ความเท่ากันบรรทัดนี้เป็นจริงสำหรับทุกค่าของ $\\theta$ ที่ $\\cos\\theta \\ne 0$ '
        'และตัวส่วนไม่เป็นศูนย์ ไม่ได้ใช้ค่า $4$ ที่โจทย์ให้เลยแม้แต่นิดเดียว',
        '',
        '<b>ขั้นที่ 4 · แทนค่า $\\tan\\theta = 4$ แล้วยุบให้เป็นตัวเลข</b>',
        '• สูตรที่ใช้ : รูปที่ยุบแล้วจากขั้นที่ 3 คือ $\\dfrac{3\\tan\\theta - 2}{\\tan\\theta + 5}$',
        '• ระบุตัวแปร : $\\tan\\theta = 4$ ตามที่โจทย์ให้มา ⇒ ไม่มีตัวไม่รู้ค่าเหลืออยู่อีกเลย',
        '• ตรวจตัวส่วนก่อนแทนค่าเสมอ : $\\tan\\theta + 5 = 4 + 5 = 9$ ซึ่งไม่เป็นศูนย์ '
        '⇒ แทนค่าได้อย่างปลอดภัย เศษส่วนไม่ระเบิด',
        '• แทนค่า : $\\dfrac{3(4) - 2}{4 + 5}$',
        '• ยุบ : เศษ $= 12 - 2 = 10$ · ส่วน $= 9$ ⇒ ค่าของนิพจน์ $= \\dfrac{10}{9}$ '
        'ซึ่งเป็นเศษส่วนอย่างต่ำอยู่แล้วเพราะ $10$ กับ $9$ ไม่มีตัวประกอบร่วมนอกจาก $1$',
        '• 📌 มองย้อนกลับไปทั้งสี่ขั้น จะเห็นว่า<b>ไม่ต้องหา $\\sin\\theta$ กับ $\\cos\\theta$ แยกกันเลย</b> '
        'และไม่ต้องรู้ด้วยซ้ำว่า $\\theta$ อยู่ในจตุภาคใด '
        'เพราะเมื่อ $\\theta$ ย้ายไปอยู่จตุภาคที่เครื่องหมายของ $\\sin$ กับ $\\cos$ กลับข้างพร้อมกัน '
        'เศษกับส่วนก็เปลี่ยนเครื่องหมายพร้อมกันทั้งคู่ ⇒ เครื่องหมายลบตัดกันทิ้งไป ค่าของเศษส่วนคงเดิม',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่า $\\sin\\theta$ กับ $\\cos\\theta$ จริงจากสามเหลี่ยมอ้างอิง '
        'โดยไม่ผ่านสูตรลัดที่หารด้วย $\\cos\\theta$ เลย)</b>',
        '• เส้นทางข้างบนอาศัยการหารทั้งเศษและส่วนด้วย $\\cos\\theta$ '
        'การตรวจรอบนี้จะไม่แตะการหารนั้นเลย แต่จะสร้างค่า $\\sin\\theta$ กับ $\\cos\\theta$ ขึ้นมาจริง ๆ '
        'แล้วแทนลงในนิพจน์ต้นฉบับตรง ๆ ถ้าได้ค่าเดียวกันแปลว่าการยุบข้างบนไม่ได้ทำอะไรหล่นหาย',
        '• เลือก $\\theta$ ในจตุภาคที่ $1$ ก่อน : $\\tan\\theta = 4 = \\dfrac{4}{1}$ '
        '⇒ สามเหลี่ยมอ้างอิงมีด้านตรงข้ามยาว $4$ ด้านประชิดยาว $1$ '
        'และด้านตรงข้ามมุมฉากยาว $\\sqrt{1^2 + 4^2} = \\sqrt{17}$ '
        '⇒ $\\sin\\theta = \\dfrac{4}{\\sqrt{17}}$ และ $\\cos\\theta = \\dfrac{1}{\\sqrt{17}}$',
        '• คิดเศษของนิพจน์ต้นฉบับ : $3\\sin\\theta - 2\\cos\\theta '
        '= \\dfrac{3(4)}{\\sqrt{17}} - \\dfrac{2(1)}{\\sqrt{17}} = \\dfrac{12 - 2}{\\sqrt{17}} '
        '= \\dfrac{10}{\\sqrt{17}}$',
        '• คิดส่วนของนิพจน์ต้นฉบับ : $\\sin\\theta + 5\\cos\\theta '
        '= \\dfrac{4}{\\sqrt{17}} + \\dfrac{5(1)}{\\sqrt{17}} = \\dfrac{4 + 5}{\\sqrt{17}} '
        '= \\dfrac{9}{\\sqrt{17}}$',
        '• หารกัน : $\\dfrac{10}{\\sqrt{17}} \\div \\dfrac{9}{\\sqrt{17}} = \\dfrac{10}{9}$ '
        'เพราะ $\\sqrt{17}$ ที่อยู่ตัวส่วนของทั้งสองก้อนตัดกันหมดพอดี ✓ ตรงกับผลของขั้นที่ 4',
        '• 📌 ตรวจเพิ่มอีกชั้นด้วยจตุภาคที่ $3$ ซึ่งเป็นอีกที่หนึ่งที่ $\\tan\\theta = 4$ ได้ : '
        'ที่นั่น $\\sin\\theta = -\\dfrac{4}{\\sqrt{17}}$ และ $\\cos\\theta = -\\dfrac{1}{\\sqrt{17}}$ '
        '⇒ เศษ $= -\\dfrac{10}{\\sqrt{17}}$ และส่วน $= -\\dfrac{9}{\\sqrt{17}}$ '
        '⇒ หารกันได้ $\\dfrac{10}{9}$ เท่าเดิม เพราะเครื่องหมายลบทั้งบนและล่างตัดกันทิ้ง '
        '⇒ ยืนยันว่าคำตอบไม่ขึ้นกับจตุภาค สมกับที่โจทย์ไม่ได้บอกจตุภาคมาให้',
        '',
        '✅ <b>คำตอบ</b> ค่าของ $\\dfrac{3\\sin\\theta - 2\\cos\\theta}{\\sin\\theta + 5\\cos\\theta}$ '
        'เมื่อ $\\tan\\theta = 4$ เท่ากับ $\\dfrac{10}{9}$ → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• พอเห็นเศษส่วนที่<b>ทุกพจน์ทั้งข้างบนและข้างล่างมี $\\sin$ หรือ $\\cos$ ยกกำลังหนึ่งพอดี</b> '
        'ให้คิดถึงการหารด้วย $\\cos\\theta$ เป็นอย่างแรกเสมอ '
        'เพราะจะเปลี่ยนโจทย์ให้เหลือตัวแปรเดียวคือ $\\tan\\theta$ ทันที '
        'เคล็ดเดียวกันนี้ใช้ได้กับรูปทั่วไป $\\dfrac{p\\sin\\theta + q\\cos\\theta}{r\\sin\\theta + s\\cos\\theta} '
        '= \\dfrac{p\\tan\\theta + q}{r\\tan\\theta + s}$',
        '• ถ้าดีกรีของเศษกับส่วน<b>ไม่เท่ากัน</b> เคล็ดนี้ใช้ไม่ได้ '
        'เช่น $\\dfrac{3\\sin\\theta - 2\\cos\\theta}{\\sin\\theta\\cos\\theta}$ '
        'ข้างล่างเป็นดีกรีสอง หารด้วย $\\cos\\theta$ แล้วจะเหลือ $\\sin\\theta$ ค้างอยู่ '
        '⇒ กรณีแบบนั้นต้องหา $\\sin\\theta$ กับ $\\cos\\theta$ จริง ๆ และต้องรู้จตุภาคด้วย '
        '⇒ ก่อนใช้เคล็ดนี้ให้นับดีกรีทุกพจน์ก่อนเสมอ',
        '• ตรวจความสมเหตุสมผลอย่างเร็วก่อนวงคำตอบ : เมื่อ $\\tan\\theta = 4$ ถือว่าใหญ่พอสมควร '
        'พจน์ที่มี $\\sin\\theta$ จะเด่นกว่าพจน์ที่มี $\\cos\\theta$ '
        '⇒ ค่าของนิพจน์ควรใกล้ ๆ $\\dfrac{3\\sin\\theta}{\\sin\\theta} = 3$ แบบหย่อนลงมา '
        'และต้องเป็นจำนวนบวกแน่ ๆ เพราะเศษ $12 - 2$ กับส่วน $4 + 5$ เป็นบวกทั้งคู่ '
        '⇒ ค่าที่ติดลบตัดทิ้งได้ทันทีโดยไม่ต้องคำนวณ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ถ้าได้ค่า $-\\dfrac{5}{21}$ แปลว่าหันไปหารทั้งเศษและส่วนด้วย $\\sin\\theta$ แทน '
        'ซึ่งจะได้รูป $\\dfrac{3 - 2\\cot\\theta}{1 + 5\\cot\\theta}$ แล้วเผลอแทน $\\cot\\theta = 4$ '
        'ทั้งที่ $4$ เป็นค่าของ $\\tan\\theta$ ไม่ใช่ $\\cot\\theta$ ⇒ คิดออกมาได้ '
        '$\\dfrac{3 - 8}{1 + 20} = -\\dfrac{5}{21}$ · ค่านี้ผิดเพราะสลับ $\\tan$ กับ $\\cot$ '
        '<b>ที่ถูกคือ $\\cot\\theta = \\dfrac{1}{4}$</b> เนื่องจากทั้งสองเป็นส่วนกลับของกัน '
        'ถ้าแทนด้วยค่าที่ถูกต้องจะได้ $\\dfrac{3 - 2\\left(\\dfrac{1}{4}\\right)}'
        '{1 + 5\\left(\\dfrac{1}{4}\\right)} = \\dfrac{\\dfrac{5}{2}}{\\dfrac{9}{4}} = \\dfrac{10}{9}$ '
        'กลับมาเท่าเดิม ⇒ เส้นทางหารด้วย $\\sin\\theta$ ไม่ได้ผิด แต่ผิดที่ค่าที่แทน · '
        'ยังฟ้องได้อีกทางว่าค่านี้ติดลบ ทั้งที่เศษกับส่วนของนิพจน์ต้นฉบับเป็นบวกทั้งคู่เมื่อ '
        '$\\theta$ อยู่ในจตุภาคที่ $1$',
        '• ถ้าได้ค่า $\\dfrac{9}{10}$ แปลว่าคำนวณถูกหมดทุกขั้นแล้ว '
        'แต่ตอนเขียนคำตอบเผลอกลับเศษกับส่วน คือหยิบ $9$ ขึ้นไปไว้ข้างบนและกด $10$ ลงมาไว้ข้างล่าง · '
        'ค่านี้ผิดเพราะเป็นส่วนกลับของคำตอบจริง ตรวจได้ทันทีด้วยการแทนค่าจริงจากสามเหลี่ยมอ้างอิง : '
        'เศษของนิพจน์คือ $\\dfrac{10}{\\sqrt{17}}$ ซึ่ง<b>มากกว่า</b>ส่วนซึ่งเป็น $\\dfrac{9}{\\sqrt{17}}$ '
        '⇒ ค่าของเศษส่วนต้องมากกว่า $1$ แต่ $\\dfrac{9}{10}$ น้อยกว่า $1$ ⇒ เป็นไปไม่ได้',
        '• ถ้าได้ค่า $\\dfrac{14}{9}$ แปลว่าเดินถูกทางแล้ว แต่ทำเครื่องหมายพลาดที่พจน์ $-2\\cos\\theta$ '
        'คือหารแล้วเขียนเป็น $3\\tan\\theta + 2$ ทั้งที่ต้องเป็น $3\\tan\\theta - 2$ '
        '⇒ ได้ $\\dfrac{12 + 2}{9} = \\dfrac{14}{9}$ · ค่านี้ผิดเพราะเครื่องหมายลบหน้าพจน์ '
        '$2\\cos\\theta$ ต้องติดไปกับพจน์นั้นตลอดทาง '
        'พิสูจน์ซ้ำด้วยการแทนค่าจริง : $3\\sin\\theta - 2\\cos\\theta = \\dfrac{12 - 2}{\\sqrt{17}}$ '
        'ซึ่งเป็น $\\dfrac{10}{\\sqrt{17}}$ ⛔ ไม่ใช่ $\\dfrac{14}{\\sqrt{17}}$',
        '• อีกเส้นทางที่พลาดกันบ่อยคือรีบหา $\\sin\\theta$ กับ $\\cos\\theta$ แยกกันตั้งแต่ต้น '
        'แล้วไปติดปัญหาว่าโจทย์ไม่ได้บอกจตุภาค จึงเดาเครื่องหมายเอาเองแล้วใส่ลบให้ตัวใดตัวหนึ่ง '
        'เช่นใช้ $\\sin\\theta = \\dfrac{4}{\\sqrt{17}}$ คู่กับ $\\cos\\theta = -\\dfrac{1}{\\sqrt{17}}$ '
        '⇒ จะได้ $\\dfrac{12 + 2}{4 - 5} = -14$ ซึ่งผิด เพราะคู่เครื่องหมายแบบนั้นให้ '
        '$\\tan\\theta = -4$ ขัดกับที่โจทย์กำหนด · '
        'ทางที่ปลอดภัยคือหารด้วย $\\cos\\theta$ ตั้งแต่แรกแล้วไม่ต้องยุ่งกับเครื่องหมายเลย',
    ],
    'V.mold: G = one real number theta pinned down by exactly two facts, the licence cos(theta) != 0 and '
    'the single ratio value tan(theta) = 4, together with a fraction whose numerator 3*sin(theta) - '
    '2*cos(theta) and denominator sin(theta) + 5*cos(theta) are both first degree in sin(theta) and '
    'cos(theta), with no square, no product of the two functions and no bare constant term anywhere / '
    'A = the numeric value of that fraction, chosen from four printed numbers / M = divide numerator and '
    'denominator by cos(theta), a move licensed precisely by the given cos(theta) != 0, so every term '
    'collapses into either tan(theta) or a constant and the fraction becomes (3*tan(theta) - 2) / '
    '(tan(theta) + 5), after which tan(theta) = 4 is substituted directly; sin(theta) and cos(theta) are '
    'never produced separately and the quadrant of theta is never needed. '
    'Rubric F1 C0 P1 T0 L0 = 2/15, and a total of 2 with T at most 1 and C equal to 0 is exactly the band '
    'the grader reserves for the easiest tier -> level: ง่าย. F = 1 because one single piece of knowledge '
    'carries the whole item, the definition tan = sin / cos, applied through the ordinary arithmetic rule '
    'that dividing top and bottom of a fraction by the same nonzero quantity leaves its value unchanged; '
    'no Pythagorean identity, no addition formula and no double angle formula is required at any point. '
    'C = 0 because the work never leaves subtopic 7.4: there is no equation to solve, no unit circle to '
    'read, no sector and no graph, so nothing has to be joined to anything. P = 1 because the chain is '
    'three short moves, divide the numerator, divide the denominator, substitute one number, and the '
    'final arithmetic is 12 - 2 over 4 + 5 with no fraction arithmetic beyond that. T = 0 because there '
    'is no hidden turning point to uncover: the statement hands over cos(theta) != 0 in plain sight, '
    'which is the only permission the method needs, and the matching degree of numerator and denominator '
    'is visible on the surface of the printed expression rather than having to be engineered. L = 0 '
    'because the item is pure symbol work with no scene, no figure and no real-world situation to model. '
    'The item was deliberately not lifted toward the medium band: withholding the quadrant would have '
    'been meaningless here since the answer is quadrant independent, and adding a second identity would '
    'have raised F and P past the easy ceiling this batch still needs filled. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b20.py): simplify of (3*sin(th) - 2*cos(th)) / (sin(th) + 5*cos(th)) minus '
    '(3*tan(th) - 2) / (tan(th) + 5) returns 0, so the collapsed form is not an approximation but an '
    'identity wherever both sides are defined; substituting th = atan(4) into the original fraction '
    'returns Rational(10, 9), matching the stored key. Every error path printed in the pitfalls block was '
    'machine-computed rather than invented: Rational(3 - 8, 1 + 20) returns -5/21 for the path that '
    'divides by sin(theta) and then feeds 4 into cot(theta), while cot(atan(4)) returns Rational(1, 4), '
    'so the machine also confirms the repair, (3 - 2*Rational(1, 4)) / (1 + 5*Rational(1, 4)) returning '
    '10/9; 1 / Rational(10, 9) returns 9/10 for the inverted answer; and Rational(3*4 + 2, 9) returns '
    '14/9 for the sign slip on the -2*cos(theta) term. The independent check was machine-verified too: '
    'sin(atan(4)) returns 4*sqrt(17)/17 and cos(atan(4)) returns sqrt(17)/17, the numerator evaluates to '
    '10*sqrt(17)/17 and the denominator to 9*sqrt(17)/17, whose quotient is 10/9, and at th = atan(4) + '
    'pi the same two expressions return -10*sqrt(17)/17 and -9*sqrt(17)/17, whose quotient is 10/9 once '
    'more, which is the machine statement of the quadrant independence claimed in the explanation. The '
    'denominator is safe on the given data since tan(theta) + 5 evaluates to 9. '
    'Collision sweep on 6417 items (bank 63 files + k1 out + k2 out), probe collide_b20.py / '
    'collide_b20b.py: the pair that defines this item, a numeric tangent value handed over together with '
    'a fraction that is first degree in sine and cosine on both levels, returns 0 items across the whole '
    'corpus. The nearest relative is gen-chap-07-trigonometry-q091, which opens with the same licence '
    'clause cos(theta) != 0 and also lives in subtopic 7.4, but it supplies no numeric value at all and '
    'asks which symbolic expression the fraction equals, its numerator and denominator being third '
    'degree, so it is solved by factoring and applying the Pythagorean identity rather than by dividing '
    'through by cos(theta); it therefore shares neither G, since nothing numeric is given, nor A, since '
    'the answer is a function and not a number, nor M. Other items that mix sine and cosine inside one '
    'printed fraction sit in the identity and equation families of subtopics 7.5 to 7.7, where the task '
    'is to solve for theta or to simplify a double angle, not to evaluate at a known tangent. Choices '
    'are ordered ascending by numeric value (-5/21, then 9/10, then 10/9, then 14/9), so the answer slot '
    'is forced by that rule and was not chosen.',
)

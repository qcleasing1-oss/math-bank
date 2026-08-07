# -*- coding: utf-8 -*-
add(
    162,
    ['7.4'],
    'ง่าย',
    'กำหนดให้ $\\theta$ เป็นจำนวนจริงซึ่ง $\\sin\\theta\\cos\\theta \\ne 0$ '
    'และ $\\tan\\theta + \\cot\\theta = 5$ '
    'ค่าของ $\\sin\\theta\\cos\\theta$ เท่ากับข้อใด',
    [
        '$\\dfrac{1}{10}$',
        '$\\dfrac{1}{5}$',
        '$\\dfrac{2}{5}$',
        '$5$',
    ],
    1,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• <b>$\\tan$ กับ $\\cot$ ไม่ใช่ของใหม่ ทั้งคู่คือ $\\sin$ กับ $\\cos$ ที่เขียนย่อไว้</b> : '
        'นิยามบอกว่า $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        'และ $\\cot\\theta = \\dfrac{\\cos\\theta}{\\sin\\theta}$ '
        'สังเกตว่าสองก้อนนี้เป็นเศษส่วนที่กลับหัวกันพอดี ตัวเศษของก้อนหนึ่งคือตัวส่วนของอีกก้อนหนึ่ง '
        '⇒ เมื่อโจทย์ให้ $\\tan$ กับ $\\cot$ ปนกันมา ทางเดินที่ปลอดภัยที่สุดคือ '
        'เขียนทุกอย่างกลับเป็น $\\sin$ กับ $\\cos$ ก่อน แล้วค่อยคิดต่อ '
        'เพราะ $\\sin$ กับ $\\cos$ เป็นตัวตั้งต้นที่เอกลักษณ์อื่น ๆ อ้างถึงได้หมด',
        '• <b>เอกลักษณ์พีทาโกรัส $\\sin^2\\theta + \\cos^2\\theta = 1$</b> : '
        'ที่มาของเอกลักษณ์นี้คือวงกลมหนึ่งหน่วย จุดปลายส่วนโค้งของมุม $\\theta$ '
        'คือจุด $(\\cos\\theta,\\ \\sin\\theta)$ ซึ่งอยู่บนวงกลมรัศมี $1$ '
        'จุดทุกจุดบนวงกลมนั้นสอดคล้องกับสมการ $x^2 + y^2 = 1$ '
        '⇒ แทน $x = \\cos\\theta$ และ $y = \\sin\\theta$ ก็ได้ $\\cos^2\\theta + \\sin^2\\theta = 1$ ทันที '
        'ข้อสำคัญคือเอกลักษณ์นี้เป็นจริงกับ $\\theta$ <b>ทุกค่า</b> ไม่ต้องรู้ว่า $\\theta$ เป็นมุมเท่าใด',
        '• <b>การบวกเศษส่วนที่ตัวส่วนต่างกัน</b> : ต้องทำตัวส่วนให้เหมือนกันก่อนจึงบวกตัวเศษได้ '
        'ตัวส่วนร่วมของ $\\dfrac{A}{B}$ กับ $\\dfrac{B}{A}$ คือ $AB$ '
        '⇒ $\\dfrac{A}{B} + \\dfrac{B}{A} = \\dfrac{A\\cdot A}{AB} + \\dfrac{B\\cdot B}{AB} '
        '= \\dfrac{A^2 + B^2}{AB}$ '
        'ขั้นนี้ทำได้เมื่อ $A$ และ $B$ ไม่เป็นศูนย์ทั้งคู่ เพราะตัวส่วนห้ามเป็นศูนย์',
        '• <b>การกลับเศษกับส่วน</b> : ถ้า $\\dfrac{1}{X} = k$ โดยที่ $k \\ne 0$ แล้ว $X = \\dfrac{1}{k}$ '
        'เหตุผลไม่ใช่การท่องจำ แต่มาจากการคูณไขว้ : คูณสองข้างด้วย $X$ ได้ $1 = kX$ '
        'จากนั้นหารสองข้างด้วย $k$ ได้ $X = \\dfrac{1}{k}$ '
        '⇒ ค่าที่โจทย์ให้กับค่าที่โจทย์ถามอาจเป็นคู่กลับหัวของกันและกัน ซึ่งเป็นกรณีของข้อนี้พอดี',
        '• <b>สูตรมุมสองเท่าและเพดานของผลคูณ $\\sin\\theta\\cos\\theta$</b> : '
        'จาก $\\sin 2\\theta = 2\\sin\\theta\\cos\\theta$ ย้ายข้างได้ว่า '
        '$\\sin\\theta\\cos\\theta = \\dfrac{1}{2}\\sin 2\\theta$ '
        'และเพราะค่าของ $\\sin$ อยู่ระหว่าง $-1$ กับ $1$ เสมอ จึงได้เพดานว่า '
        '$\\left|\\sin\\theta\\cos\\theta\\right| \\le \\dfrac{1}{2}$ '
        'สูตรนี้ไม่ได้ใช้หาคำตอบของข้อนี้ แต่ใช้เป็นไม้บรรทัดคัดค่าที่เป็นไปไม่ได้ออกได้ทันที',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $\\theta$ เป็นจำนวนจริง ⛔ ไม่มีการบอกจตุภาคหรือช่วงของ $\\theta$ เลยแม้แต่ตัวเดียว',
        '• เงื่อนไข $\\sin\\theta\\cos\\theta \\ne 0$ แปลว่า $\\sin\\theta \\ne 0$ และ $\\cos\\theta \\ne 0$ '
        'พร้อมกัน (ผลคูณจะเป็นศูนย์ก็ต่อเมื่อมีตัวใดตัวหนึ่งเป็นศูนย์) '
        '⇒ เงื่อนไขนี้มีไว้เพื่อรับประกันว่า $\\tan\\theta$ กับ $\\cot\\theta$ หาค่าได้จริง '
        'และตัวส่วนที่จะเกิดขึ้นระหว่างทางไม่เป็นศูนย์',
        '• ค่าที่โจทย์ให้มาคือ $\\tan\\theta + \\cot\\theta = 5$ เพียงบรรทัดเดียว',
        '• สังเกตหน้าตาก่อนลงมือ : สิ่งที่โจทย์ถามคือ <b>ผลคูณ</b> $\\sin\\theta\\cos\\theta$ '
        'ซึ่งเป็นตัวส่วนร่วมของ $\\dfrac{\\sin\\theta}{\\cos\\theta}$ กับ $\\dfrac{\\cos\\theta}{\\sin\\theta}$ พอดี '
        '⇒ พอรวมสองพจน์ที่โจทย์ให้เข้าด้วยกัน ผลคูณก้อนนี้จะโผล่มาเองที่ตัวส่วน '
        'นี่คือสัญญาณว่าโจทย์ไม่ได้ต้องการให้หา $\\theta$',
        '• สังเกตอีกอย่าง : โจทย์ไม่บอกจตุภาคเลย ทั้งที่ปกติโจทย์ที่ต้องหา $\\sin\\theta$ หรือ '
        '$\\cos\\theta$ แยกกันจะต้องบอกเสมอเพื่อกำหนดเครื่องหมาย '
        '⇒ การที่ไม่บอกเป็นหลักฐานว่าคำตอบต้องออกมาค่าเดียวโดยไม่ขึ้นกับว่า $\\theta$ เป็นมุมใด',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\sin\\theta\\cos\\theta$ ออกมาเป็นตัวเลขค่าเดียว โดยใช้เงื่อนไข '
        '$\\tan\\theta + \\cot\\theta = 5$ ที่โจทย์ให้',
        '',
        '<b>【 เขียน $\\tan\\theta$ กับ $\\cot\\theta$ กลับเป็น $\\sin$ กับ $\\cos$ '
        'แล้วรวมเป็นเศษส่วนก้อนเดียว ตัวเศษจะยุบเหลือ $1$ ด้วยเอกลักษณ์พีทาโกรัส '
        'เหลือ $\\dfrac{1}{\\sin\\theta\\cos\\theta} = 5$ จากนั้นกลับเศษกับส่วนก็ได้คำตอบ 】</b>',
        '',
        '<b>ขั้นที่ 1 · เขียนทั้งสองพจน์เป็น $\\sin$ กับ $\\cos$ แล้วรวมเป็นเศษส่วนเดียว</b>',
        '• สูตรที่ใช้ : นิยาม $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        'และ $\\cot\\theta = \\dfrac{\\cos\\theta}{\\sin\\theta}$ '
        'พร้อมกฎการบวกเศษส่วน $\\dfrac{A}{B} + \\dfrac{B}{A} = \\dfrac{A^2 + B^2}{AB}$',
        '• ระบุตัวแปรให้ชัดก่อนแทนค่า : ในกฎการบวกเศษส่วนข้างบน ให้ $A = \\sin\\theta$ '
        'และ $B = \\cos\\theta$ ⇒ ตัวส่วนร่วม $AB$ ก็คือ $\\sin\\theta\\cos\\theta$ '
        'ซึ่งเป็นก้อนเดียวกับที่โจทย์ถามพอดี',
        '• แทนค่า : $\\tan\\theta + \\cot\\theta '
        '= \\dfrac{\\sin\\theta}{\\cos\\theta} + \\dfrac{\\cos\\theta}{\\sin\\theta}$',
        '• ทำตัวส่วนร่วม : คูณก้อนแรกด้วย $\\dfrac{\\sin\\theta}{\\sin\\theta}$ '
        'และคูณก้อนหลังด้วย $\\dfrac{\\cos\\theta}{\\cos\\theta}$ '
        '(ทั้งสองก้อนที่เอาไปคูณมีค่าเท่ากับ $1$ จึงไม่ทำให้ค่าเปลี่ยน) ⇒ '
        '$\\dfrac{\\sin^2\\theta}{\\sin\\theta\\cos\\theta} '
        '+ \\dfrac{\\cos^2\\theta}{\\sin\\theta\\cos\\theta}$',
        '• ยุบ : ตัวส่วนเหมือนกันแล้ว จึงบวกตัวเศษเข้าด้วยกันได้ ⇒ '
        '$\\tan\\theta + \\cot\\theta = \\dfrac{\\sin^2\\theta + \\cos^2\\theta}{\\sin\\theta\\cos\\theta}$',
        '• ⛔ ตรงนี้ต้องมีเงื่อนไขค้ำ : การเขียนแบบนี้ทำได้เพราะโจทย์รับประกันไว้แล้วว่า '
        '$\\sin\\theta\\cos\\theta \\ne 0$ ⇒ ตัวส่วนไม่เป็นศูนย์ ทุกบรรทัดจึงมีความหมาย',
        '',
        '<b>ขั้นที่ 2 · ใช้เอกลักษณ์พีทาโกรัสยุบตัวเศษให้เหลือ $1$</b>',
        '• สูตรที่ใช้ : $\\sin^2\\theta + \\cos^2\\theta = 1$ ซึ่งเป็นจริงกับ $\\theta$ ทุกค่า',
        '• ระบุตัวแปร : ตัวเศษที่ได้จากขั้นที่ 1 คือ $\\sin^2\\theta + \\cos^2\\theta$ '
        'ซึ่งตรงกับด้านซ้ายของเอกลักษณ์ทุกตัวอักษร ไม่ต้องดัดแปลงอะไรเลย '
        '· ตัวส่วนคือ $\\sin\\theta\\cos\\theta$ ปล่อยไว้อย่างนั้นก่อน',
        '• แทนค่า : $\\dfrac{\\sin^2\\theta + \\cos^2\\theta}{\\sin\\theta\\cos\\theta} '
        '= \\dfrac{1}{\\sin\\theta\\cos\\theta}$',
        '• ยุบ : ได้เอกลักษณ์สำเร็จรูปว่า '
        '$\\tan\\theta + \\cot\\theta = \\dfrac{1}{\\sin\\theta\\cos\\theta}$',
        '• 📌 หยุดอ่านตรงนี้ให้ดี : ด้านขวาที่ได้คือ <b>ส่วนกลับ</b> ของสิ่งที่โจทย์ถามพอดีเป๊ะ '
        'พูดอีกแบบคือ สิ่งที่โจทย์ให้มา ($\\tan\\theta + \\cot\\theta$) กับสิ่งที่โจทย์ถาม '
        '($\\sin\\theta\\cos\\theta$) เป็นคู่กลับหัวของกันและกัน '
        '⇒ ไม่ต้องหาค่า $\\theta$ ไม่ต้องหา $\\sin\\theta$ หรือ $\\cos\\theta$ แยกกันเลยแม้แต่ตัวเดียว',
        '',
        '<b>ขั้นที่ 3 · แทนค่าที่โจทย์ให้ แล้วกลับเศษกับส่วนเพื่ออ่านคำตอบ</b>',
        '• สูตรที่ใช้ : เอกลักษณ์จากขั้นที่ 2 คือ '
        '$\\tan\\theta + \\cot\\theta = \\dfrac{1}{\\sin\\theta\\cos\\theta}$ '
        'ร่วมกับกฎการกลับเศษกับส่วน ถ้า $\\dfrac{1}{X} = k$ และ $k \\ne 0$ แล้ว $X = \\dfrac{1}{k}$',
        '• ระบุตัวแปร : $X = \\sin\\theta\\cos\\theta$ คือสิ่งที่ต้องการหา '
        '· $k = 5$ คือค่าที่โจทย์ให้ ซึ่งไม่เป็นศูนย์ จึงใช้กฎการกลับเศษกับส่วนได้',
        '• แทนค่า : $\\dfrac{1}{\\sin\\theta\\cos\\theta} = 5$',
        '• ยุบทีละบรรทัดแบบไม่ลัด : คูณสองข้างด้วย $\\sin\\theta\\cos\\theta$ '
        '(ทำได้เพราะไม่เป็นศูนย์) ⇒ $1 = 5\\sin\\theta\\cos\\theta$ '
        '⇒ หารสองข้างด้วย $5$ ⇒ $\\sin\\theta\\cos\\theta = \\dfrac{1}{5}$',
        '• อ่านผลให้เข้าใจ : คำตอบเป็นจำนวนเดียวโดยไม่ต้องรู้ว่า $\\theta$ เป็นมุมใด '
        'ซึ่งเข้ากับข้อสังเกตตอนต้นว่าโจทย์ไม่ได้บอกจตุภาคมาเลย ⇒ เดินมาถูกทาง ✓',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · หาค่า $\\tan\\theta$ จริงจากสมการกำลังสอง '
        'แล้วแทนกลับไปหาผลคูณ $\\sin\\theta\\cos\\theta$ · '
        'ปิดท้ายด้วยการตรวจเพดาน $\\left|\\sin\\theta\\cos\\theta\\right| \\le \\dfrac{1}{2}$)</b>',
        '• เส้นทางข้างบนเลี่ยงการหา $\\theta$ ทั้งหมด รอบนี้จะทำตรงข้ามคือ '
        '<b>หา $\\theta$ จริง ๆ ออกมาก่อน</b> แล้วค่อยแทนกลับ ถ้าสองทางให้ค่าตรงกัน '
        'แปลว่าเอกลักษณ์ที่ยุบมาในขั้นที่ 2 ไม่ได้ยุบผิด',
        '• ตั้งตัวแปรใหม่ : ให้ $t = \\tan\\theta$ ⇒ $\\cot\\theta = \\dfrac{1}{t}$ '
        '⇒ เงื่อนไขของโจทย์กลายเป็น $t + \\dfrac{1}{t} = 5$',
        '• คูณสองข้างด้วย $t$ (ทำได้เพราะ $\\cos\\theta \\ne 0$ และ $\\sin\\theta \\ne 0$ '
        '⇒ $t \\ne 0$) ⇒ $t^2 + 1 = 5t$ ⇒ $t^2 - 5t + 1 = 0$',
        '• แก้ด้วยสูตรกำลังสอง : $t = \\dfrac{5 \\pm \\sqrt{25 - 4}}{2} '
        '= \\dfrac{5 \\pm \\sqrt{21}}{2}$ ⇒ ได้ $t \\approx 4.7913$ กับ $t \\approx 0.2087$ '
        'ทั้งสองรากเป็นจำนวนจริงบวก ⇒ $\\theta$ อยู่ในจตุภาคที่ 1 ได้ทั้งคู่',
        '• แทนกลับหาผลคูณ : จาก $t = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        'สร้างสามเหลี่ยมมุมฉากที่มีด้านตรงข้ามมุม $\\theta$ ยาว $t$ และด้านประชิดยาว $1$ '
        '⇒ ด้านตรงข้ามมุมฉากยาว $\\sqrt{1 + t^2}$ ⇒ '
        '$\\sin\\theta\\cos\\theta = \\dfrac{t}{\\sqrt{1+t^2}} \\cdot \\dfrac{1}{\\sqrt{1+t^2}} '
        '= \\dfrac{t}{1 + t^2}$',
        '• ใช้สมการกำลังสองช่วยยุบโดยไม่ต้องแทนตัวเลขที่มีกรณฑ์ : '
        'จาก $t^2 - 5t + 1 = 0$ ย้ายข้างได้ $t^2 + 1 = 5t$ ⇒ '
        '$\\dfrac{t}{1+t^2} = \\dfrac{t}{5t} = \\dfrac{1}{5}$ ✓ ตรงกับคำตอบเดิมทุกประการ',
        '• 📌 <b>ทั้งสองรากให้ค่าเดียวกัน</b> เพราะขั้นตอนข้างบนใช้แต่ความจริงว่า $t^2+1 = 5t$ '
        'ซึ่งรากทั้งสองสอดคล้องเหมือนกัน · ดูให้ลึกอีกชั้น ผลคูณของสองรากเท่ากับ $1$ '
        '(อ่านจากพจน์คงที่ของ $t^2 - 5t + 1 = 0$) ⇒ รากหนึ่งเป็นส่วนกลับของอีกราก '
        '⇒ มุมสองมุมนี้ (ราว $78.21^{\\circ}$ กับ $11.79^{\\circ}$) บวกกันได้ $90^{\\circ}$ '
        'จึงเป็นคู่ที่สลับค่า $\\sin$ กับ $\\cos$ กัน และผลคูณ $\\sin\\theta\\cos\\theta$ '
        'ไม่เปลี่ยนค่าเมื่อสลับตัวคูณสองตัว',
        '• 📌 ตรวจเพดานอีกชั้น : $\\sin\\theta\\cos\\theta = \\dfrac{1}{2}\\sin 2\\theta$ '
        '⇒ ค่าที่เป็นไปได้ต้องอยู่ในช่วง $-\\dfrac{1}{2}$ ถึง $\\dfrac{1}{2}$ เท่านั้น '
        '· คำตอบที่ได้คือ $\\dfrac{1}{5} = 0.2$ ซึ่ง $0.2 \\le 0.5$ ✓ ผ่านเกณฑ์ค่าที่เป็นไปได้',
        '• 📌 ตรวจย้อนบรรทัดสุดท้าย : แทน $\\sin\\theta\\cos\\theta = \\dfrac{1}{5}$ '
        'กลับเข้านิพจน์ที่โจทย์ให้ ⇒ $\\tan\\theta + \\cot\\theta '
        '= \\dfrac{1}{1/5} = 5$ ✓ ตรงกับเงื่อนไขที่โจทย์กำหนดพอดี',
        '',
        '✅ <b>คำตอบ</b> จาก $\\tan\\theta + \\cot\\theta = \\dfrac{1}{\\sin\\theta\\cos\\theta} = 5$ '
        'กลับเศษกับส่วนได้ $\\sin\\theta\\cos\\theta = \\dfrac{1}{5}$ → <b>ตัวเลือก 2</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอ $\\tan$ $\\cot$ $\\sec$ หรือ $\\csc$ ปนกันเมื่อไร ให้เขียนกลับเป็น $\\sin$ กับ $\\cos$ '
        'ทันทีเป็นก้าวแรกเสมอ แล้วรวมเป็นเศษส่วนเดียว '
        'เพราะเอกลักษณ์ที่ยุบของได้จริง ๆ คือ $\\sin^2\\theta + \\cos^2\\theta = 1$ '
        'ซึ่งจะโผล่มาให้ใช้ก็ต่อเมื่อทุกอย่างอยู่ในรูป $\\sin$ กับ $\\cos$ แล้วเท่านั้น',
        '• จำผลลัพธ์ของข้อนี้ไว้เป็นเอกลักษณ์สำเร็จรูปได้เลยว่า '
        '$\\tan\\theta + \\cot\\theta = \\dfrac{1}{\\sin\\theta\\cos\\theta} = \\dfrac{2}{\\sin 2\\theta}$ '
        'เจอโจทย์ตระกูลนี้อีกจะเหลือแค่การกลับเศษกับส่วนหรือการหารด้วยสอง '
        'แต่ต้องระวังให้ดีว่ารูปไหนจับคู่กับค่าอะไร',
        '• ก่อนวงคำตอบของโจทย์ที่ถามหาผลคูณ $\\sin\\theta\\cos\\theta$ ให้เอาไม้บรรทัด '
        '$\\left|\\sin\\theta\\cos\\theta\\right| \\le \\dfrac{1}{2}$ มาทาบเสมอ '
        'ค่าที่เกินเพดานนี้ตัดทิ้งได้ทันทีโดยไม่ต้องคำนวณอะไรเพิ่ม',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ถ้าได้ค่า $\\dfrac{1}{10}$ แปลว่ายุบนิพจน์ได้ถูกจนถึง '
        '$\\dfrac{1}{\\sin\\theta\\cos\\theta} = 5$ แล้ว แต่ตอนกลับเศษกับส่วนกลับหยิบเลข '
        '$\\dfrac{1}{2}$ ที่ติดอยู่ในสูตรมุมสองเท่ามาคูณเพิ่มโดยไม่มีเหตุผล '
        'จึงได้ $\\dfrac{1}{2} \\times \\dfrac{1}{5} = \\dfrac{1}{10}$ · '
        'ค่านี้ผิดแน่นอน พิสูจน์ด้วยการแทนกลับ : ถ้า $\\sin\\theta\\cos\\theta = \\dfrac{1}{10}$ จริง '
        'จะได้ $\\tan\\theta + \\cot\\theta = \\dfrac{1}{1/10} = 10$ ซึ่งขัดกับ $5$ ที่โจทย์ให้ · '
        'ที่มาของความสับสนคือ $\\dfrac{1}{2}$ ในสูตร $\\sin\\theta\\cos\\theta '
        '= \\dfrac{1}{2}\\sin 2\\theta$ ต้องคู่กับ $\\sin 2\\theta$ เท่านั้น '
        '⛔ ไม่ใช่คูณเข้ากับผลลัพธ์ที่ยุบมาโดยตรง',
        '• ถ้าได้ค่า $\\dfrac{2}{5}$ แปลว่าเดินสายมุมสองเท่าโดยใช้ '
        '$\\tan\\theta + \\cot\\theta = \\dfrac{2}{\\sin 2\\theta}$ ซึ่งถูกต้อง '
        'จนได้ $\\dfrac{2}{\\sin 2\\theta} = 5 \\Rightarrow \\sin 2\\theta = \\dfrac{2}{5}$ '
        'แล้วตอบค่านี้ออกไปทันที เพราะเข้าใจผิดว่า $\\sin 2\\theta$ คือ $\\sin\\theta\\cos\\theta$ · '
        '<b>ความจริงคือ</b> $\\sin 2\\theta = 2\\sin\\theta\\cos\\theta$ '
        '⇒ $\\sin\\theta\\cos\\theta = \\dfrac{1}{2}\\sin 2\\theta '
        '= \\dfrac{1}{2} \\times \\dfrac{2}{5} = \\dfrac{1}{5}$ '
        'นั่นคือค่าที่ได้ยังต้องหารสองอีกหนึ่งครั้ง · '
        'พิสูจน์ว่าค่านี้ผิดด้วยการแทนกลับเช่นกัน : ถ้า $\\sin\\theta\\cos\\theta = \\dfrac{2}{5}$ '
        'จะได้ $\\tan\\theta + \\cot\\theta = \\dfrac{1}{2/5} = \\dfrac{5}{2}$ ไม่ใช่ $5$',
        '• ถ้าได้ค่า $5$ แปลว่ายุบนิพจน์เป็น $\\dfrac{1}{\\sin\\theta\\cos\\theta} = 5$ ได้ถูกแล้ว '
        'แต่<b>ลืมกลับเศษกับส่วน</b> คือลอกตัวเลขทางขวามือมาตอบตรง ๆ '
        'ทั้งที่ตัวเลข $5$ นั้นเป็นค่าของ<b>ส่วนกลับ</b>ของสิ่งที่โจทย์ถาม · '
        'ค่านี้ไม่ใช่แค่ผิด แต่<b>เป็นไปไม่ได้เลย</b> เพราะ '
        '$\\left|\\sin\\theta\\cos\\theta\\right| '
        '= \\left|\\dfrac{1}{2}\\sin 2\\theta\\right| \\le \\dfrac{1}{2}$ '
        'ผลคูณก้อนนี้จึงเกิน $\\dfrac{1}{2}$ ไม่ได้ไม่ว่ากรณีใด แต่ $5$ ใหญ่กว่า $\\dfrac{1}{2}$ ถึงสิบเท่า · '
        'แทนกลับก็ขัดกันชัดเจน : ถ้า $\\sin\\theta\\cos\\theta = 5$ '
        'จะได้ $\\tan\\theta + \\cot\\theta = \\dfrac{1}{5}$ ไม่ใช่ $5$',
        '• อีกเส้นทางที่เสียเวลาโดยไม่จำเป็นคือรีบไล่หาค่า $\\theta$ ตั้งแต่บรรทัดแรก '
        'ทั้งที่โจทย์ไม่ได้บอกจตุภาคมาให้เลย · เส้นทางนั้นจะพาไปเจอ '
        '$t = \\dfrac{5 \\pm \\sqrt{21}}{2}$ ซึ่งเป็นจำนวนอตรรกยะสองค่า '
        'แล้วมักจบด้วยการปัดเศษจนคำตอบเพี้ยน · '
        'สัญญาณเตือนว่าไม่ต้องหา $\\theta$ คือโจทย์ถามหา<b>ผลคูณ</b> '
        '$\\sin\\theta\\cos\\theta$ ซึ่งเป็นก้อนสมมาตร ไม่ได้ถาม $\\sin\\theta$ หรือ '
        '$\\cos\\theta$ แยกกัน ⇒ ก้อนสมมาตรแบบนี้มักอ่านออกมาได้ทั้งก้อนโดยไม่ต้องแยกชิ้นส่วน',
    ],
    'V.mold: G = the single equation tan(theta) + cot(theta) = 5 for a real theta, handed over with the '
    'defining condition sin(theta)cos(theta) != 0 and with no quadrant and no interval named at all / '
    'A = the value of the product sin(theta)cos(theta) / M = rewrite both given terms through their '
    'definitions as sin over cos and cos over sin, put them over the common denominator '
    'sin(theta)cos(theta), let the Pythagorean identity collapse the numerator to 1, which turns the '
    'given expression into 1/(sin(theta)cos(theta)), and then read the answer off as the reciprocal of '
    'the given number, since the quantity asked for is exactly the reciprocal of the quantity given. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 with the total at 2 or below, T at most 1 and C exactly 0 '
    '-> level: ง่าย. '
    'F = 1 because one identity carries the whole item, sin^2 + cos^2 = 1; the two definitions of tan '
    'and cot are not counted as a second and third formula because they are the definitions of the '
    'symbols themselves rather than results to be recalled, and the double angle relation appears only '
    'in the check and in the impossibility argument, never on the solving path. C = 0 because nothing '
    'has to be joined to anything: no intermediate result is produced and then fed into a separate '
    'relation, the given expression is rewritten in place and the single equation that remains is '
    'inverted. P = 1 because the manipulation is one common denominator followed by one reciprocal, '
    'with no numbers larger than 5 and no algebra to rearrange; a solver who knows the identity finishes '
    'in a single line. T = 0 because nothing is hidden or has to be discarded: the non vanishing '
    'condition is printed in the statement instead of being left for the solver to notice, no root has '
    'to be rejected, no sign has to be decided, and the deliberate absence of a quadrant is not a trap '
    'but a consequence of the answer being independent of theta. L = 0 because the item is purely '
    'symbolic, with no figure to reconstruct and no scene to translate. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): simplify(tan(t) + cot(t) - 1/(sin(t)cos(t))) returns 0, so the collapse used '
    'in step 2 is machine confirmed as an identity rather than asserted. Solving tan(t) + 1/tan(t) = 5 '
    'for tan(t) returns the two roots (5 - sqrt(21))/2 and (5 + sqrt(21))/2, numerically about 0.208712 '
    'and 4.791288, and feeding each root back through sin(atan(s))cos(atan(s)) produces a set of size 1 '
    'whose only element is 1/5, so the independent route agrees with the main route and both roots agree '
    'with each other; the same set computed as s/(1 + s^2) is again exactly 1/5. Every wrong value was '
    'machine computed from a named error path instead of being invented near the answer: the product '
    '(1/2)(1/5) returns 1/10 for the solver who drags the factor one half out of the double angle '
    'formula and multiplies it into an answer that never contained sin(2 theta), 2 sin(t)cos(t) '
    'evaluated at either root returns 2/5, which is the value of sin(2 theta) and is what the solver '
    'reports who confuses sin(2 theta) with sin(theta)cos(theta), and 5 itself is what the solver '
    'reports who never inverts the collapsed equation. Each wrong value was also refuted by back '
    'substitution into the given expression: 1/(1/10) returns 10, 1/(2/5) returns 5/2 and 1/5 returns '
    '1/5, none of which is the given 5. The impossibility of the last one was checked separately, since '
    'maximum and minimum of sin(t)cos(t) over a full period return 1/2 and -1/2, so no real theta can '
    'make the product 5, while the key 1/5 = 0.2 sits inside that band. The ordering check confirms that '
    '1/10 < 1/5 < 2/5 < 5. '
    'Collision sweep on 6457 items (bank 63 files + k1 out + k2 out), probe rerun for this item over the '
    'same corpus: the string for cot appears in 41 statements and the pair tan together with cot appears '
    'in 19 statements, and every one of those 19 was read. The nearest relative by G is '
    'gen-chap-07-trigonometry-q004, which also hands over tan(theta) + cot(theta) as a constant, but it '
    'pins theta to the interval from 0 to pi, sets the constant negative at -5/2 and asks for '
    'sin^3(theta) - cos^3(theta), so its A is a difference of cubes and its M has to fix the sign of '
    'sin(theta) - cos(theta) from the interval and then factor a cubic difference, a machinery this item '
    'never touches; it shares only the G surface and is graded far above this one. The next relative, '
    'gen-chap-07-trigonometry-q056, uses the half angle version tan(theta/2) + cot(theta/2) and asks for '
    'cos(theta), so its M is a half angle transfer rather than a reciprocal read. In the other direction '
    'gen-chap-07-trigonometry-q014 travels the reverse arrow, handing over sin(theta)cos(theta) = 1/4 '
    'and asking for (sin(theta) + cos(theta))^2, so what is given here is what is asked there and the '
    'mechanism is an expansion rather than a collapse. A search for a statement that asks for the value '
    'of the product sin(theta)cos(theta) returns only gen-chap-07-trigonometry-q138 and '
    'gen-chap-07-trigonometry-q144, and in neither is the product the answer: in the first it sits '
    'inside a radical in a much longer expression on the unit circle, and in the second the answer is '
    'tan(theta) + sin(theta)cos(theta) with a quarter interval that picks a branch, both of them graded '
    'at the top level. So the triple formed by a bare tan plus cot equation, a request for the product '
    'itself, and a plain reciprocal read is empty in the corpus. Choices are ordered ascending by value '
    '(1/10, then 1/5, then 2/5, then 5), so the answer slot is forced by that rule and was not chosen.',
)

# -*- coding: utf-8 -*-
add(
    137,
    ['7.2'],
    'ยาก',
    'กำหนดให้ $\\theta$ เป็นจำนวนจริงซึ่ง $\\dfrac{\\pi}{2} < \\theta < \\dfrac{3\\pi}{2}$ '
    'โดยที่ $\\left|\\cos\\theta\\right| = \\dfrac{20}{29}$ '
    'และ $\\cos\\theta \\cdot \\tan\\theta > 0$ '
    'แล้วค่าของ $29\\left(\\sin\\theta - \\cos\\theta\\right)$ เท่ากับข้อใดต่อไปนี้',
    [
        '$-41$',
        '$-1$',
        '$1$',
        '$41$',
    ],
    3,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ⭐ <b>กุญแจดอกแรกของข้อนี้ · ผลคูณ $\\cos\\theta \\cdot \\tan\\theta$ ยุบเหลือฟังก์ชันเดียวได้</b> : '
        'จากนิยาม $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ ซึ่งใช้ได้ทุกครั้งที่ $\\cos\\theta \\ne 0$ '
        'จะได้ $\\cos\\theta \\cdot \\tan\\theta = \\cos\\theta \\cdot \\dfrac{\\sin\\theta}{\\cos\\theta} = \\sin\\theta$ '
        'ตัว $\\cos\\theta$ ตัดกันหมดพอดี ⇒ ผลคูณก้อนนี้<b>เท่ากับ</b> $\\sin\\theta$ ไม่ใช่แค่เครื่องหมายเหมือนกัน '
        '⇒ เงื่อนไข $\\cos\\theta \\cdot \\tan\\theta > 0$ จึงแปลว่า $\\sin\\theta > 0$ ได้ทันทีในบรรทัดเดียว '
        '⛔ ไม่ต้องไปไล่เครื่องหมายของสองตัวแยกกันให้ยุ่ง',
        '• <b>ความหมายของค่าสัมบูรณ์</b> : ถ้า $\\left|x\\right| = a$ เมื่อ $a > 0$ แล้วจะได้ $x = a$ หรือ $x = -a$ '
        'อย่างใดอย่างหนึ่ง ⇒ ค่าสัมบูรณ์บอก<b>ขนาด</b>อย่างเดียว ไม่เคยบอกเครื่องหมาย '
        'ดังนั้นเมื่อโจทย์ให้ค่าสัมบูรณ์มา ต้องไปหาหลักฐานจากบรรทัดอื่นของโจทย์มาตัดสินเครื่องหมายเสมอ '
        '⛔ ห้ามเดาว่าเป็นบวกเพราะเห็นเลขบวกอยู่ในเครื่องหมายค่าสัมบูรณ์',
        '• <b>วงกลมหนึ่งหน่วยกับเครื่องหมายของ $\\sin$ และ $\\cos$</b> : ถ้าจุดปลายส่วนโค้งของมุม $\\theta$ '
        'บนวงกลมหนึ่งหน่วยคือจุด $(x, y)$ แล้ว $\\cos\\theta = x$ และ $\\sin\\theta = y$ '
        '⇒ เครื่องหมายของ $\\cos$ คือเครื่องหมายของพิกัดแนวนอน และเครื่องหมายของ $\\sin$ คือเครื่องหมายของพิกัดแนวตั้ง '
        '⇒ จตุภาคที่ $1$ ได้ $(+, +)$ · จตุภาคที่ $2$ ได้ $(-, +)$ · จตุภาคที่ $3$ ได้ $(-, -)$ · '
        'จตุภาคที่ $4$ ได้ $(+, -)$',
        '• <b>ช่วงของ $\\theta$ แปลเป็นบริเวณบนวงกลมได้</b> : มุม $\\dfrac{\\pi}{2}$ ชี้ขึ้นตรง ๆ '
        'และมุม $\\dfrac{3\\pi}{2}$ ชี้ลงตรง ๆ ⇒ เมื่อ $\\theta$ เดินจาก $\\dfrac{\\pi}{2}$ ไปยัง $\\dfrac{3\\pi}{2}$ '
        'จุดปลายส่วนโค้งจะกวาดผ่าน<b>ครึ่งซ้าย</b>ของวงกลมทั้งครึ่ง ซึ่งเป็นบริเวณที่พิกัดแนวนอนเป็นลบทั้งหมด '
        '⇒ ช่วงนี้บังคับให้ $\\cos\\theta < 0$ เสมอ โดยไม่ต้องรู้ว่า $\\theta$ เป็นค่าใดแน่',
        '• <b>เอกลักษณ์พีทาโกรัส</b> : $\\sin^2\\theta + \\cos^2\\theta = 1$ ทุกค่าของ $\\theta$ '
        '⇒ ย้ายข้างได้เป็น $\\sin^2\\theta = 1 - \\cos^2\\theta$ ⇒ ถอดรากได้ $\\left|\\sin\\theta\\right| = '
        '\\sqrt{1 - \\cos^2\\theta}$ · สังเกตว่าการถอดรากให้แต่<b>ขนาด</b>อีกเช่นกัน '
        'เครื่องหมายของ $\\sin\\theta$ ต้องมาจากที่อื่น · ชุดจำนวนเต็มที่ควรจำคู่กับตัวส่วน $29$ คือ '
        '$20$-$21$-$29$ เพราะ $400 + 441 = 841$ พอดี',
        '• <b>วินัยข้อสุดท้ายที่ทำให้ข้อนี้ไม่พลาด</b> : โจทย์ที่ให้เงื่อนไขมาหลายบรรทัด '
        'ต้องใช้<b>ครบทุกบรรทัด</b>ก่อนวงคำตอบ ข้อนี้ให้มาสามชั้นคือช่วงของ $\\theta$ · ค่าสัมบูรณ์ของ $\\cos\\theta$ '
        'และอสมการผลคูณ ⇒ ถ้าคำนวณจบแล้วยังมีชั้นใดไม่ได้ถูกใช้เลย แปลว่าเดินผิดทางแน่นอน '
        'ให้ย้อนกลับไปดูว่าลืมชั้นไหน',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $\\theta$ เป็นจำนวนจริง ซึ่งอยู่ในช่วง $\\dfrac{\\pi}{2} < \\theta < \\dfrac{3\\pi}{2}$ '
        '(เป็นช่วงเปิด ⇒ ปลายทั้งสองไม่นับ)',
        '• $\\left|\\cos\\theta\\right| = \\dfrac{20}{29}$ ⇒ รู้แต่ขนาดของ $\\cos\\theta$ ยังไม่รู้เครื่องหมาย',
        '• $\\cos\\theta \\cdot \\tan\\theta > 0$ ⇒ เป็นเงื่อนไขเครื่องหมายที่ผูกสองฟังก์ชันไว้ด้วยกัน',
        '• สังเกตหน้าตาก่อนลงมือ : เงื่อนไขที่โจทย์ให้มามีสามชั้น และแต่ละชั้นทำหน้าที่ไม่เหมือนกันเลย '
        'ชั้นค่าสัมบูรณ์ให้<b>ขนาด</b> ส่วนอีกสองชั้นเป็นตัวตัดสิน<b>เครื่องหมาย</b> '
        '⇒ วางแผนได้ทันทีว่าต้องเก็บให้ครบทั้งสาม แล้วค่อยแทนค่าเป็นก้าวสุดท้าย',
        '• สังเกตอีกอย่าง : ตัวเลข $29$ ที่คูณอยู่หน้าวงเล็บเป็นตัวเดียวกับตัวส่วนของ $\\dfrac{20}{29}$ พอดี '
        '⇒ เมื่อแทนค่าแล้วตัวส่วนจะถูกตัดทิ้งหมด คำตอบจึงเป็นจำนวนเต็ม ไม่มีเศษส่วนค้าง '
        'และเมื่อขาหนึ่งของสามเหลี่ยมอ้างอิงเป็น $20$ กับด้านตรงข้ามมุมฉากเป็น $29$ อีกขาต้องเป็น $21$',
        '• สังเกตข้อสุดท้าย : โจทย์ไม่ได้บอกตรง ๆ สักคำว่าจุดปลายส่วนโค้งอยู่จตุภาคใด '
        '⇒ งานหลักของข้อนี้คือการ<b>สืบจตุภาคเอง</b>จากเงื่อนไขที่ให้มา',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $29\\left(\\sin\\theta - \\cos\\theta\\right)$ ซึ่งจะทำได้ก็ต่อเมื่อรู้ทั้ง $\\sin\\theta$ '
        'และ $\\cos\\theta$ พร้อมเครื่องหมายที่ถูกต้องของทั้งคู่',
        '',
        '<b>【 ยุบเงื่อนไขผลคูณให้เหลือ $\\sin\\theta > 0$ ก่อน แล้วใช้ช่วงที่โจทย์ให้บังคับว่า $\\cos\\theta < 0$ '
        'จับสองผลนี้ชนกันจะได้จตุภาคที่ $2$ จากนั้นเติมขนาดของ $\\sin\\theta$ ด้วยเอกลักษณ์พีทาโกรัส '
        'แล้วจึงแทนค่าลงในนิพจน์เป็นก้าวสุดท้าย 】</b>',
        '',
        '<b>ขั้นที่ 1 · ยุบเงื่อนไขผลคูณให้เหลือฟังก์ชันเดียว (หัวใจของข้อนี้)</b>',
        '• สูตรที่ใช้ : $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        'ซึ่งเป็นนิยามของ $\\tan$ ในรูปของ $\\sin$ กับ $\\cos$',
        '• ระบุตัวแปรก่อนแทนค่า : ก้อนที่โจทย์ให้เงื่อนไขไว้คือ $\\cos\\theta \\cdot \\tan\\theta$ '
        '· ตัวที่จะถูกแทนคือ $\\tan\\theta$ · เงื่อนไขที่ต้องรักษาไว้คือ $\\cos\\theta \\ne 0$ '
        'ซึ่งเป็นจริงแน่นอนในข้อนี้ เพราะ $\\left|\\cos\\theta\\right| = \\dfrac{20}{29} \\ne 0$ '
        '⇒ ตัดทอนได้อย่างสบายใจ',
        '• แทนค่า : $\\cos\\theta \\cdot \\tan\\theta = \\cos\\theta \\cdot \\dfrac{\\sin\\theta}{\\cos\\theta}$',
        '• ยุบ : $\\cos\\theta$ ที่อยู่ข้างหน้ากับ $\\cos\\theta$ ที่อยู่ในตัวส่วนตัดกันพอดี '
        '⇒ $\\cos\\theta \\cdot \\tan\\theta = \\sin\\theta$',
        '• แปลเงื่อนไขใหม่ : เมื่อสองก้อนนี้เท่ากันเสมอ เงื่อนไข $\\cos\\theta \\cdot \\tan\\theta > 0$ '
        'จึงเป็นเงื่อนไขเดียวกับ $\\sin\\theta > 0$ ทุกประการ ⇒ <b>ผลของขั้นนี้คือ $\\sin\\theta > 0$</b>',
        '• ⛔ ระวังตรงนี้ให้มาก : ห้ามแปลผลคูณเป็นบวกว่า “$\\cos\\theta$ กับ $\\tan\\theta$ ต้องเครื่องหมายเดียวกัน” '
        'แล้วนั่งไล่ตารางเครื่องหมายทีละจตุภาค เพราะเส้นทางนั้นยาวกว่าและพลาดง่ายกว่ามาก '
        'ในเมื่อผลคูณยุบเป็น $\\sin\\theta$ ได้ตรง ๆ อยู่แล้ว ก็อ่านเครื่องหมายของ $\\sin\\theta$ ทีเดียวจบ',
        '',
        '<b>ขั้นที่ 2 · ใช้ช่วงที่โจทย์ให้มาตัดสินเครื่องหมายของ $\\cos\\theta$</b>',
        '• สิ่งที่ใช้ : ความสัมพันธ์ $\\cos\\theta = $ พิกัดแนวนอนของจุดปลายส่วนโค้งบนวงกลมหนึ่งหน่วย',
        '• ระบุขอบเขต : โจทย์ให้ $\\dfrac{\\pi}{2} < \\theta < \\dfrac{3\\pi}{2}$ '
        '· มุม $\\dfrac{\\pi}{2}$ พาจุดปลายไปอยู่ที่ $(0, 1)$ ซึ่งเป็นยอดบนสุด '
        '· มุม $\\dfrac{3\\pi}{2}$ พาจุดปลายไปอยู่ที่ $(0, -1)$ ซึ่งเป็นก้นล่างสุด',
        '• อ่านผล : มุมที่อยู่ระหว่างสองค่านี้พาจุดปลายกวาดผ่านครึ่งซ้ายของวงกลมทั้งครึ่ง '
        '⇒ พิกัดแนวนอนของจุดปลายเป็นจำนวนลบตลอดช่วง ⇒ <b>$\\cos\\theta < 0$ เสมอ</b> '
        '(ปลายช่วงทั้งสองที่พิกัดแนวนอนเป็น $0$ ถูกตัดออกไปแล้ว เพราะเป็นช่วงเปิด '
        'อีกทั้ง $\\tan$ ก็ไม่นิยามที่มุมทั้งสองนั้นด้วย)',
        '• ถอดค่าสัมบูรณ์ : จาก $\\left|\\cos\\theta\\right| = \\dfrac{20}{29}$ '
        'ได้ผู้สมัครสองค่าคือ $\\cos\\theta = \\dfrac{20}{29}$ หรือ $\\cos\\theta = -\\dfrac{20}{29}$',
        '• คัดทิ้งด้วยผลที่เพิ่งได้ : ผู้สมัครค่าบวกขัดกับ $\\cos\\theta < 0$ จึงใช้ไม่ได้ '
        '⇒ เหลือ $\\cos\\theta = -\\dfrac{20}{29}$ เพียงค่าเดียว',
        '',
        '<b>ขั้นที่ 3 · รวมผลของสองขั้นแรกเข้าด้วยกัน แล้วเติมค่าของ $\\sin\\theta$</b>',
        '• รวมสองชั้น : ขั้นที่ 1 ให้ $\\sin\\theta > 0$ และขั้นที่ 2 ให้ $\\cos\\theta < 0$ '
        '⇒ จุดปลายส่วนโค้งมีพิกัดแนวตั้งเป็นบวกและพิกัดแนวนอนเป็นลบ ⇒ อยู่ในจตุภาคที่ $2$ '
        'ซึ่งเป็นจตุภาคเดียวที่ให้เครื่องหมายคู่นี้',
        '• สูตรที่ใช้หาขนาด : $\\sin^2\\theta = 1 - \\cos^2\\theta$ ซึ่งย้ายข้างมาจากเอกลักษณ์ '
        '$\\sin^2\\theta + \\cos^2\\theta = 1$',
        '• แทนค่า : $\\sin^2\\theta = 1 - \\left(-\\dfrac{20}{29}\\right)^2 = 1 - \\dfrac{400}{841}$ '
        '· สังเกตว่าการยกกำลังสองทำให้เครื่องหมายลบหายไป จึงได้ $\\dfrac{400}{841}$ เท่ากันกับกรณีบวก',
        '• ยุบ : $1 = \\dfrac{841}{841}$ ⇒ $\\sin^2\\theta = \\dfrac{841 - 400}{841} = \\dfrac{441}{841}$',
        '• ถอดราก : $\\sqrt{441} = 21$ และ $\\sqrt{841} = 29$ '
        '⇒ $\\left|\\sin\\theta\\right| = \\dfrac{21}{29}$ ⇒ ผู้สมัครสองค่าคือ $\\pm\\dfrac{21}{29}$',
        '• เลือกเครื่องหมายด้วยผลของขั้นที่ 1 : ต้องได้ $\\sin\\theta > 0$ '
        '⇒ <b>$\\sin\\theta = \\dfrac{21}{29}$</b> (ค่าบวก) · สอดคล้องกับจตุภาคที่ $2$ ที่หาไว้พอดี',
        '',
        '<b>ขั้นที่ 4 · แทนค่าลงในนิพจน์ที่โจทย์ถาม</b>',
        '• นิพจน์ที่ต้องหา : $29\\left(\\sin\\theta - \\cos\\theta\\right)$',
        '• ระบุตัวแปร : $\\sin\\theta = \\dfrac{21}{29}$ จากขั้นที่ 3 '
        '· $\\cos\\theta = -\\dfrac{20}{29}$ จากขั้นที่ 2',
        '• แทนค่า : $29\\left(\\sin\\theta - \\cos\\theta\\right) = '
        '29\\left(\\dfrac{21}{29} - \\left(-\\dfrac{20}{29}\\right)\\right)$',
        '• จัดการเครื่องหมายลบสองชั้นก่อน : ลบด้วยจำนวนลบเท่ากับบวกด้วยจำนวนบวก '
        '⇒ ในวงเล็บกลายเป็น $\\dfrac{21}{29} + \\dfrac{20}{29} = \\dfrac{41}{29}$',
        '• ยุบ : $29 \\times \\dfrac{41}{29} = 41$ เพราะ $29$ ตัดกับตัวส่วนพอดี '
        '⇒ ค่าของนิพจน์เท่ากับ $41$',
        '• เดินอีกทางให้ผลเดียวกัน : กระจาย $29$ เข้าไปก่อนก็ได้ '
        '$29 \\times \\dfrac{21}{29} = 21$ และ $29 \\times \\left(-\\dfrac{20}{29}\\right) = -20$ '
        '⇒ $21 - (-20) = 21 + 20 = 41$ ✓',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไล่ผู้สมัครทั้งสี่จตุภาคในหนึ่งรอบ '
        'แล้วตรวจเงื่อนไขทีละข้อในตารางว่าเหลือรอดกี่ค่า)</b>',
        '• เส้นทางข้างบนใช้วิธี<b>อนุมาน</b> คือค่อย ๆ บีบเงื่อนไขจนเหลือจตุภาคเดียว '
        'การตรวจรอบนี้จะเดินกลับทางกันคือ <b>ไล่ผู้สมัครทุกตัวก่อน</b> แล้วค่อยคัดออกทีละข้อ '
        'ถ้าสองวิธีที่คิดคนละทางให้คำตอบตรงกัน และเหลือผู้สมัครรอดเพียงค่าเดียว '
        'ก็ยืนยันได้ทั้งว่าคำตอบถูกและว่าโจทย์ไม่กำกวม',
        '• ตั้งต้น : มุมที่ทำให้ $\\left|\\cos\\theta\\right| = \\dfrac{20}{29}$ มีสี่ค่าในหนึ่งรอบ '
        'โดยมีมุมอ้างอิง $\\alpha$ ซึ่ง $\\cos\\alpha = \\dfrac{20}{29}$ และ $\\alpha \\approx 0.810$ เรเดียน '
        '⇒ ผู้สมัครคือ $\\alpha$ · $\\pi - \\alpha$ · $\\pi + \\alpha$ · $2\\pi - \\alpha$ '
        'ซึ่งมีค่าประมาณ $0.810$ · $2.332$ · $3.951$ · $5.473$ ตามลำดับ '
        '(เทียบกับ $\\dfrac{\\pi}{2} \\approx 1.571$ และ $\\dfrac{3\\pi}{2} \\approx 4.712$)',
        '• ผู้สมัครที่ $1$ · จตุภาคที่ $1$ · $\\theta \\approx 0.810$ ⇒ $\\cos\\theta = \\dfrac{20}{29}$ , '
        '$\\sin\\theta = \\dfrac{21}{29}$ · อยู่ในช่วงที่โจทย์ให้ไหม : <b>ไม่อยู่</b> '
        'เพราะ $0.810 < \\dfrac{\\pi}{2}$ ⇒ ตกตั้งแต่ด่านแรก (ทั้งที่ผ่านเงื่อนไข $\\sin\\theta > 0$)',
        '• ผู้สมัครที่ $2$ · จตุภาคที่ $2$ · $\\theta \\approx 2.332$ ⇒ $\\cos\\theta = -\\dfrac{20}{29}$ , '
        '$\\sin\\theta = \\dfrac{21}{29}$ · อยู่ในช่วงไหม : <b>อยู่</b> เพราะ '
        '$1.571 < 2.332 < 4.712$ ✓ · $\\sin\\theta > 0$ ไหม : <b>ใช่</b> ✓ '
        '(ตรวจซ้ำที่เงื่อนไขดิบเลยก็ได้ $\\cos\\theta \\cdot \\tan\\theta = '
        '\\left(-\\dfrac{20}{29}\\right)\\left(-\\dfrac{21}{20}\\right) = \\dfrac{21}{29} > 0$ ✓) '
        '⇒ <b>รอดทั้งสองด่าน</b>',
        '• ผู้สมัครที่ $3$ · จตุภาคที่ $3$ · $\\theta \\approx 3.951$ ⇒ $\\cos\\theta = -\\dfrac{20}{29}$ , '
        '$\\sin\\theta = -\\dfrac{21}{29}$ · อยู่ในช่วงไหม : <b>อยู่</b> ✓ '
        '· $\\sin\\theta > 0$ ไหม : <b>ไม่ใช่</b> ✗ ⇒ ตกด่านที่สอง '
        '(ตรวจที่เงื่อนไขดิบก็ฟ้องเหมือนกัน $\\cos\\theta \\cdot \\tan\\theta = '
        '\\left(-\\dfrac{20}{29}\\right)\\left(\\dfrac{21}{20}\\right) = -\\dfrac{21}{29} < 0$)',
        '• ผู้สมัครที่ $4$ · จตุภาคที่ $4$ · $\\theta \\approx 5.473$ ⇒ $\\cos\\theta = \\dfrac{20}{29}$ , '
        '$\\sin\\theta = -\\dfrac{21}{29}$ · อยู่ในช่วงไหม : <b>ไม่อยู่</b> เพราะ '
        '$5.473 > \\dfrac{3\\pi}{2}$ ✗ · $\\sin\\theta > 0$ ไหม : <b>ไม่ใช่</b> ✗ ⇒ ตกทั้งสองด่าน',
        '• สรุปตาราง : ผู้สมัครสี่ค่า ตกไปสามค่า <b>เหลือรอดเพียงค่าเดียว</b> คือจตุภาคที่ $2$ '
        'ตรงกับที่ขั้นที่ 3 อนุมานไว้ ⇒ แทนค่าได้ $29\\left(\\dfrac{21}{29} + \\dfrac{20}{29}\\right) = '
        '21 + 20 = 41$ ✓ ตรงกับขั้นที่ 4',
        '• ตรวจอีกชั้นด้วยเอกลักษณ์ : คู่ค่าที่ใช้ต้องอยู่บนวงกลมหนึ่งหน่วยจริง '
        '$\\left(\\dfrac{21}{29}\\right)^2 + \\left(-\\dfrac{20}{29}\\right)^2 = '
        '\\dfrac{441 + 400}{841} = \\dfrac{841}{841} = 1$ ✓ '
        'สอดคล้องกับสามเหลี่ยมมุมฉากด้าน $20$-$21$-$29$ ที่ $400 + 441 = 841$ พอดี',
        '',
        '✅ <b>คำตอบ</b> จตุภาคที่ $2$ เป็นจตุภาคเดียวที่ผ่านครบทั้งสามเงื่อนไข ⇒ $\\sin\\theta = \\dfrac{21}{29}$ '
        'และ $\\cos\\theta = -\\dfrac{20}{29}$ ⇒ ค่าของ $29\\left(\\sin\\theta - \\cos\\theta\\right)$ '
        'เท่ากับ $41$ → <b>ตัวเลือก 4</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• พอเห็น<b>ผลคูณ</b>ของฟังก์ชันตรีโกณอยู่ในเงื่อนไขอสมการ ให้ลองยุบเป็นฟังก์ชันเดียวก่อนเสมอ '
        'เพราะคู่ที่ยุบได้มีอยู่ไม่กี่คู่และเจอบ่อยมาก : $\\cos\\theta\\tan\\theta = \\sin\\theta$ · '
        '$\\sin\\theta\\cot\\theta = \\cos\\theta$ · $\\tan\\theta\\cot\\theta = 1$ · '
        '$\\sin\\theta\\csc\\theta = 1$ · $\\cos\\theta\\sec\\theta = 1$ '
        '⇒ ยุบได้เมื่อไรก็อ่านเครื่องหมายจบในบรรทัดเดียว เร็วกว่าลากตารางเครื่องหมายทั้งสี่จตุภาคมาก',
        '• จำ “ครึ่งวงกลม” ไว้แทนการท่องจตุภาค : ช่วง $\\left(\\dfrac{\\pi}{2}, \\dfrac{3\\pi}{2}\\right)$ '
        'คือครึ่งซ้าย ⇒ $\\cos < 0$ · ช่วง $\\left(0, \\pi\\right)$ คือครึ่งบน ⇒ $\\sin > 0$ · '
        'ช่วง $\\left(-\\dfrac{\\pi}{2}, \\dfrac{\\pi}{2}\\right)$ คือครึ่งขวา ⇒ $\\cos > 0$ '
        '⇒ เห็นช่วงแบบนี้ในโจทย์เมื่อไรให้แปลเป็นเครื่องหมายทันที อย่าเสียเวลาหาว่า $\\theta$ เป็นค่าใดแน่',
        '• ท่องชุดพีทาโกรัสที่เป็นจำนวนเต็มไว้ให้ขึ้นใจ : $3$-$4$-$5$ · $5$-$12$-$13$ · $8$-$15$-$17$ · '
        '$7$-$24$-$25$ · $20$-$21$-$29$ · $9$-$40$-$41$ · พอเห็นตัวส่วน $29$ คู่กับตัวเศษ $20$ '
        'ก็ควรนึกออกทันทีว่าอีกขาคือ $21$ โดยไม่ต้องคำนวณ $1 - \\dfrac{400}{841}$ จริง ประหยัดเวลาในห้องสอบ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ถ้าได้ค่า $-41$ แปลว่าไม่ได้ใช้ช่วงที่โจทย์ให้มาเลยสักชั้น '
        'มักเกิดจากยุบผลคูณได้ถูกจน $\\sin\\theta > 0$ แล้วสับสนต่อ หรือไปสรุปเอาเองว่าจุดปลายส่วนโค้งอยู่จตุภาคที่ $4$ '
        'จึงใช้ $\\cos\\theta = \\dfrac{20}{29}$ คู่กับ $\\sin\\theta = -\\dfrac{21}{29}$ '
        '⇒ $29\\left(-\\dfrac{21}{29} - \\dfrac{20}{29}\\right) = -21 - 20 = -41$ · '
        'ค่านี้ผิดแน่นอนสองชั้น : มุมในจตุภาคที่ $4$ มีค่าประมาณ $5.473$ เรเดียน '
        'ซึ่งมากกว่า $\\dfrac{3\\pi}{2} \\approx 4.712$ จึงหลุดออกนอกช่วงที่โจทย์บังคับ '
        'และยังมี $\\sin\\theta < 0$ ทำให้ $\\cos\\theta \\cdot \\tan\\theta = \\sin\\theta < 0$ '
        'ขัดกับอสมการที่โจทย์ให้ไว้อีกด้วย',
        '• ถ้าได้ค่า $-1$ แปลว่าตีความผลคูณเป็นบวกว่า “$\\cos\\theta$ กับ $\\tan\\theta$ ต้องมีเครื่องหมายเดียวกัน” '
        'แล้วจำผิดว่าจตุภาคที่ $3$ มี $\\tan\\theta < 0$ จึงคิดว่าลบคูณลบได้บวก เลยเลือกจตุภาคที่ $3$ '
        'ได้ $\\cos\\theta = -\\dfrac{20}{29}$ คู่กับ $\\sin\\theta = -\\dfrac{21}{29}$ '
        '⇒ $29\\left(-\\dfrac{21}{29} + \\dfrac{20}{29}\\right) = -21 + 20 = -1$ · '
        'ค่านี้ผิดเพราะข้อเท็จจริงกลับกัน : จตุภาคที่ $3$ มี $\\tan\\theta > 0$ ต่างหาก '
        'ที่นี่ $\\tan\\theta = \\dfrac{-21/29}{-20/29} = \\dfrac{21}{20} > 0$ '
        '⇒ ผลคูณ $\\left(-\\dfrac{20}{29}\\right)\\left(\\dfrac{21}{20}\\right) = -\\dfrac{21}{29}$ '
        'ซึ่ง<b>เป็นลบ</b> จึงขัดกับเงื่อนไขทันที · '
        'บทเรียนคือถ้ายุบผลคูณเป็น $\\sin\\theta$ ตั้งแต่แรก ก็จะไม่มีทางหลงเข้ากับดักนี้เลย',
        '• ถ้าได้ค่า $1$ แปลว่าเดินครึ่งทางถูก คือยุบ $\\cos\\theta \\cdot \\tan\\theta$ เป็น $\\sin\\theta$ ได้ '
        'จึงรู้ว่า $\\sin\\theta > 0$ แล้วเติม $\\sin\\theta = \\dfrac{21}{29}$ ถูกต้อง '
        'แต่ตอนถอดค่าสัมบูรณ์กลับหยิบ $\\cos\\theta = \\dfrac{20}{29}$ มาเฉย ๆ '
        'โดยไม่เอาช่วง $\\dfrac{\\pi}{2} < \\theta < \\dfrac{3\\pi}{2}$ มาตัดสินเครื่องหมาย '
        '⇒ $29\\left(\\dfrac{21}{29} - \\dfrac{20}{29}\\right) = 21 - 20 = 1$ · '
        'ค่านี้ผิดเพราะคู่ค่าที่ใช้เป็นของจตุภาคที่ $1$ ซึ่งมี $\\theta \\approx 0.810$ เรเดียน '
        'น้อยกว่า $\\dfrac{\\pi}{2} \\approx 1.571$ ⇒ อยู่นอกช่วงที่โจทย์บังคับ · '
        'นี่คือกับดักหลักของข้อนี้ เพราะเงื่อนไขค่าสัมบูรณ์กับอสมการผลคูณถูกใช้ครบแล้วทั้งคู่ '
        'เหลือแค่ชั้นเดียวที่ไม่ได้ใช้ แต่ชั้นเดียวนั้นเป็นตัวพลิกคำตอบทั้งข้อ',
        '• เส้นทางพลาดที่ป้องกันได้ง่ายที่สุดคือลืมคูณ $29$ ปิดท้าย แล้วตอบ $\\dfrac{41}{29}$ '
        'หรือหยุดกลางทางแล้วตอบ $\\dfrac{21}{29}$ ซึ่งเป็นเพียงค่าของ $\\sin\\theta$ ไม่ใช่ค่าของนิพจน์ · '
        'ยาแก้ที่ใช้ได้กับทั้งข้อคือ ก่อนวงคำตอบให้ไล่นิ้วกลับไปทีละบรรทัดแล้วถามว่า '
        '“เงื่อนไขทุกชั้นถูกใช้ไปแล้วหรือยัง” ข้อนี้มีสามชั้นคือช่วงของ $\\theta$ · ค่าสัมบูรณ์ '
        'และอสมการผลคูณ ⇒ ถ้ายังมีชั้นใดไม่ได้แตะ แปลว่ายังทำไม่จบ ห้ามวงคำตอบ',
    ],
    'V.mold: G = a real number theta pinned down by three conditions of three different kinds, the half '
    'turn interval pi/2 < theta < 3pi/2, the absolute value |cos theta| = 20/29 which supplies a magnitude '
    'only, and the product inequality cos theta * tan theta > 0 / A = the value of 29(sin theta - cos '
    'theta) / M = collapse the product into a single ratio, since cos theta * tan theta is identically sin '
    'theta, so the inequality reads sin theta > 0 in one line, then read cos theta < 0 straight off the '
    'given interval because that interval is the left half of the unit circle, intersect the two sign '
    'facts to land in quadrant 2, and rebuild the magnitude of sin theta from the Pythagorean identity '
    'before substituting; the mechanism label is M-COLLAPSE-PRODUCT-TO-SINGLE-SIGN. '
    'Rubric F2 C2 P1 T3 L0 = 8/15, total at least 8 with C at least 2 and T at least 2 -> level: ยาก. '
    'F = 2 for two formula blocks that must both be present, the quotient definition of tangent that '
    'collapses the product and the Pythagorean identity that supplies the magnitude of the sine; neither '
    'alone finishes the item, and nothing beyond these two standard tools is needed, so F was not raised '
    'to 3. C = 2 because three different kinds of reasoning have to be joined in one item: an algebraic '
    'identity applied to a condition rather than to the quantity asked for, an interval of real numbers '
    'translated into a region of the unit circle, and the intersection of two sign facts that neither '
    'condition states on its own. P = 1 because the arithmetic is very short once the branch is settled, '
    'being 1 - 400/841, one square root of a perfect square, and one subtraction of two fractions that '
    'already share a denominator. T = 3 because every one of the three given conditions is a turning '
    'point and dropping any single one still leaves a clean integer that looks like a finished answer: '
    'ignoring the interval yields 1, ignoring the product inequality yields -1, and ignoring both yields '
    '-41, so a solver who uses two conditions out of three is never warned by an ugly value. L = 0 '
    'because the item is symbolic throughout, with no figure to reconstruct and no worded situation to '
    'model. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b20.py): the collapse itself was verified as an identity, since simplify(cos(t) * '
    'tan(t) - sin(t)) returns 0, so the product condition and the condition sin theta > 0 are the same '
    'condition rather than merely compatible ones. With b = acos(Rational(20, 29)) the four candidate '
    'angles b, pi - b, pi + b and 2 * pi - b evaluate to 0.809784, 2.331809, 3.951376 and 5.473402; the '
    'in-range test pi/2 < x < 3 * pi/2 and the test cos(x) * tan(x) > 0 were applied to each, and exactly '
    'one candidate survives both, namely pi - b, for which simplify(29 * (sin(x) - cos(x))) returns 41. '
    'The exact values behind that survivor were confirmed too: 1 - Rational(20, 29)**2 returns 441/841, '
    'sqrt(441) returns 21 and sqrt(841) returns 29 with no residual radical, and Rational(21, 29)**2 + '
    'Rational(20, 29)**2 returns 1. Every wrong value was machine-computed from a named error path '
    'instead of being invented: 29 * (Rational(-21, 29) - Rational(20, 29)) returns -41 for the quadrant '
    '4 reading that never uses the interval, 29 * (Rational(-21, 29) + Rational(20, 29)) returns -1 for '
    'the quadrant 3 reading, and 29 * (Rational(21, 29) - Rational(20, 29)) returns 1 for pulling the '
    'positive root out of the absolute value. The refutation quoted in the trap block was machine-checked '
    'as well: at pi + b the tangent simplifies to 21/20, a positive number, so cos * tan simplifies to '
    '-21/29, which is negative and fails the given inequality, confirming that the memory slip about the '
    'sign of the tangent in quadrant 3 is the actual error there. '
    'Collision sweep on 6417 items (bank 63 files + k1 out + k2 out), probe collide_b20.py / '
    'collide_b20b.py: the same three roots now carry 6437 unique ids, the 6417 of the batch 19 sweep plus '
    'the twenty items of that batch which have since landed in k2 out. Scan E1, an absolute value wrapped '
    'around a trigonometric ratio inside the statement, returns 5 items, of which four are plainly '
    'unrelated, a sum of three absolute sines whose range is asked, an absolute sine of an arctangent, an '
    'integral of an absolute difference of sines, and a complex-number item. Scan E2, a product of two '
    'trigonometric ratios compared with zero in the statement, returns exactly 1 item, '
    'gen-chap-07-trigonometry-q045, which hands over two such products and asks only which quadrant the '
    'terminal point lies in; no magnitude is ever supplied there and no value is ever computed, so it '
    'shares neither A nor M with this item. Scan E3, the interval from pi/2 to 3pi/2 written out as a '
    'double inequality, returns 0 items across the whole corpus. Scan E4, a difference of a sine and a '
    'cosine inside the asked expression, returns 2 items, one that fixes the terminal point by a line '
    'through the origin plus an explicitly named quadrant, and one vector item. Scan E5, the fractions '
    '20/29 or 21/29 anywhere in a statement, returns 0 items, so the 20-21-29 triple is unused in this '
    'shape. Scan E6, a bare sign condition on a single trigonometric ratio, returns 3 items, and the '
    'pair E1 with E6 returns 0. Two near relatives were logged as WATCH and cleared under iron rule 5. '
    'The first is gen-chap-07-trigonometry-q022, which asks for 25(sin theta + cos theta) off a 7-24-25 '
    'triple and therefore echoes the packaging of A, but its G is a tangent value together with one bare '
    'sign condition, so there is no product to collapse and no interval to translate, and its M is a '
    'reference triangle with a sign attached. The second is pat1-2565-03-q10, a past-paper item that does '
    'carry both an absolute value and a product inequality, but the product there is sin times tan, which '
    'collapses to a square over a single ratio and therefore fixes only the sign of the cosine, its '
    'magnitude is the special-angle value 1/2, and its A is the pair of coordinates of a point reached '
    'along an arc of length pi + theta, so G, A and M all differ. The mechanism label '
    'M-COLLAPSE-PRODUCT-TO-SINGLE-SIGN is absent from the register of used mechanisms. Choices are '
    'ordered ascending by numeric value (-41, then -1, then 1, then 41), so the answer slot is forced by '
    'that rule and was not chosen.',
)

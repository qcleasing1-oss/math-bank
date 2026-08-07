# -*- coding: utf-8 -*-
add_fill(
    138,
    ['7.2'],
    'ยากมาก',
    'บนวงกลมหนึ่งหน่วยที่มีจุดศูนย์กลางอยู่ที่จุดกำเนิด วัดส่วนโค้งจากจุด $(1, 0)$ '
    'ไปในทิศทวนเข็มนาฬิกาเป็นระยะ $\\theta$ หน่วย เมื่อ $0 \\le \\theta < 2\\pi$ '
    'ได้จุดปลายส่วนโค้งคือจุด $P$ ถ้าจุด $P$ อยู่บนส่วนโค้งที่ลากจากจุด '
    '$\\left(-\\dfrac{\\sqrt{2}}{2},\\ \\dfrac{\\sqrt{2}}{2}\\right)$ '
    'ไปในทิศทวนเข็มนาฬิกาจนถึงจุด '
    '$\\left(-\\dfrac{\\sqrt{2}}{2},\\ -\\dfrac{\\sqrt{2}}{2}\\right)$ '
    'และ $\\sec\\theta\\,\\csc\\theta = -\\dfrac{25}{12}$ แล้วค่าของ '
    '$\\dfrac{\\sqrt{1 - 2\\sin\\theta\\cos\\theta}}{\\sin\\theta + \\cos\\theta} + '
    '\\dfrac{\\sqrt{1 + 2\\sin\\theta\\cos\\theta}}{\\sin\\theta - \\cos\\theta}$ เท่ากับเท่าใด',
    '-48/7',
    ['-48/7', '-\\dfrac{48}{7}'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• วงกลมหนึ่งหน่วยคือวงกลมรัศมี $1$ หน่วยที่มีจุดศูนย์กลางอยู่ที่จุดกำเนิด '
        'ถ้าวัดส่วนโค้งจากจุด $(1, 0)$ ไปในทิศทวนเข็มนาฬิกาเป็นระยะ $\\theta$ หน่วย '
        'จุดปลายส่วนโค้งจะเป็นจุด $\\left(\\cos\\theta,\\ \\sin\\theta\\right)$ เสมอ '
        '· เหตุผลที่ความยาวส่วนโค้งกับขนาดมุมเป็นเลขตัวเดียวกันได้ก็เพราะสูตร $s = r\\theta$ '
        'เมื่อรัศมี $r = 1$ จะเหลือ $s = \\theta$ พอดี ⇒ อ่านพิกัดของจุดบนวงกลมหนึ่งหน่วย '
        'ก็คืออ่านค่า $\\cos\\theta$ กับ $\\sin\\theta$ นั่นเอง',
        '• $\\sec\\theta$ กับ $\\csc\\theta$ เป็นส่วนกลับของ $\\cos\\theta$ กับ $\\sin\\theta$ '
        'ตามลำดับ คือ $\\sec\\theta = \\dfrac{1}{\\cos\\theta}$ และ '
        '$\\csc\\theta = \\dfrac{1}{\\sin\\theta}$ (นิยามได้เมื่อตัวส่วนไม่เป็นศูนย์) '
        '⇒ คูณกันได้ $\\sec\\theta\\csc\\theta = \\dfrac{1}{\\sin\\theta\\cos\\theta}$ '
        '· ⭐ ที่ต้องอ่านให้ออกคือ การให้ค่าผลคูณนี้มา ก็เท่ากับให้ค่า '
        '$\\sin\\theta\\cos\\theta$ มาแล้ว เพียงกลับเศษเป็นส่วน',
        '• เอกลักษณ์พีทาโกรัส $\\sin^{2}\\theta + \\cos^{2}\\theta = 1$ '
        'ทำให้กระจายกำลังสองของผลบวกและผลต่างได้สั้นมาก : '
        '$\\left(\\sin\\theta + \\cos\\theta\\right)^{2} = \\sin^{2}\\theta + '
        '2\\sin\\theta\\cos\\theta + \\cos^{2}\\theta = 1 + 2\\sin\\theta\\cos\\theta$ '
        'และในทำนองเดียวกัน $\\left(\\sin\\theta - \\cos\\theta\\right)^{2} = '
        '1 - 2\\sin\\theta\\cos\\theta$ ⇒ สิ่งที่อยู่ใต้กรณฑ์ทั้งสองตัวในโจทย์ '
        'ไม่ใช่ของแปลก แต่เป็นกำลังสองสมบูรณ์ที่รู้จักดีอยู่แล้ว',
        '• ⛔ กฎที่ตัดสินข้อนี้ : เครื่องหมายกรณฑ์ $\\sqrt{\\ }$ หมายถึงรากที่สองที่ '
        '<b>ไม่ติดลบ</b> เสมอ ⇒ $\\sqrt{x^{2}} = \\left|x\\right|$ ⛔ ไม่ใช่ $x$ '
        '· ดังนั้น $\\sqrt{1 - 2\\sin\\theta\\cos\\theta} = '
        '\\left|\\sin\\theta - \\cos\\theta\\right|$ และ '
        '$\\sqrt{1 + 2\\sin\\theta\\cos\\theta} = \\left|\\sin\\theta + \\cos\\theta\\right|$ '
        '⇒ จะถอดเครื่องหมายค่าสัมบูรณ์ออกได้ ต้องรู้ก่อนว่าข้างในเป็นบวกหรือลบ',
        '• การอ่านจุดพิเศษบนวงกลมหนึ่งหน่วยกลับเป็นขนาดมุม : จุดที่ค่าสัมบูรณ์ของพิกัดทั้งสอง '
        'เท่ากันและเท่ากับ $\\dfrac{\\sqrt{2}}{2}$ คือจุดที่มีมุมอ้างอิงเป็น $\\dfrac{\\pi}{4}$ '
        'จากนั้นดูเครื่องหมายของพิกัดเพื่อบอกจตุภาค ⇒ จตุภาคที่ $2$ ได้มุม '
        '$\\pi - \\dfrac{\\pi}{4} = \\dfrac{3\\pi}{4}$ · จตุภาคที่ $3$ ได้มุม '
        '$\\pi + \\dfrac{\\pi}{4} = \\dfrac{5\\pi}{4}$',
        '• การเทียบขนาดของ $\\left|\\sin\\theta\\right|$ กับ $\\left|\\cos\\theta\\right|$ '
        'ภายในจตุภาคเดียวกัน : เส้นทแยงมุม $\\theta = \\dfrac{\\pi}{4},\\ \\dfrac{3\\pi}{4},\\ '
        '\\dfrac{5\\pi}{4},\\ \\dfrac{7\\pi}{4}$ คือตำแหน่งที่ทั้งสองค่าเท่ากันพอดี '
        'เพราะที่นั่น $\\left|\\tan\\theta\\right| = 1$ ⇒ บนช่วง '
        '$\\left(\\dfrac{\\pi}{2},\\ \\dfrac{3\\pi}{4}\\right)$ มี '
        '$\\left|\\tan\\theta\\right| > 1$ ⇒ $\\left|\\sin\\theta\\right| > '
        '\\left|\\cos\\theta\\right|$ ส่วนบนช่วง $\\left(\\dfrac{3\\pi}{4},\\ \\pi\\right)$ '
        'มี $\\left|\\tan\\theta\\right| < 1$ ⇒ $\\left|\\cos\\theta\\right| > '
        '\\left|\\sin\\theta\\right|$ · ⭐ ข้อเท็จจริงบรรทัดนี้เองที่จะเป็นตัวชี้เครื่องหมายของ '
        '$\\sin\\theta + \\cos\\theta$ ในภายหลัง',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• จุด $P$ เป็นจุดปลายส่วนโค้งที่วัดจากจุด $(1, 0)$ ไปในทิศทวนเข็มนาฬิกาเป็นระยะ '
        '$\\theta$ หน่วย บนวงกลมหนึ่งหน่วย โดย $0 \\le \\theta < 2\\pi$ '
        '⇒ พิกัดของ $P$ คือ $\\left(\\cos\\theta,\\ \\sin\\theta\\right)$',
        '• จุด $P$ ถูกจำกัดให้อยู่บนส่วนโค้งที่ลากจากจุด '
        '$\\left(-\\dfrac{\\sqrt{2}}{2},\\ \\dfrac{\\sqrt{2}}{2}\\right)$ '
        'ไปในทิศทวนเข็มนาฬิกาจนถึงจุด '
        '$\\left(-\\dfrac{\\sqrt{2}}{2},\\ -\\dfrac{\\sqrt{2}}{2}\\right)$',
        '• ค่าของผลคูณ $\\sec\\theta\\csc\\theta$ เท่ากับ $-\\dfrac{25}{12}$',
        '• สังเกตหน้าตาก่อนลงมือ : สิ่งที่อยู่ใต้กรณฑ์ทั้งสองตัวคือ '
        '$1 - 2\\sin\\theta\\cos\\theta = \\left(\\sin\\theta - \\cos\\theta\\right)^{2}$ '
        'และ $1 + 2\\sin\\theta\\cos\\theta = \\left(\\sin\\theta + \\cos\\theta\\right)^{2}$ '
        'ส่วนตัวส่วนของสองเศษส่วนคือ $\\sin\\theta + \\cos\\theta$ และ '
        '$\\sin\\theta - \\cos\\theta$ ⇒ นิพจน์นี้ <b>จับคู่ไขว้</b> ไว้ตั้งแต่ต้น '
        'คือรากของ $\\left(\\sin\\theta - \\cos\\theta\\right)^{2}$ ไปอยู่เหนือ '
        '$\\sin\\theta + \\cos\\theta$ · ถ้าจับคู่ตรงกันแต่ละก้อนจะกลายเป็น '
        '$\\dfrac{\\left|x\\right|}{x}$ ซึ่งได้แค่ $1$ หรือ $-1$ และโจทย์จะจืดทันที '
        '⇒ การไขว้คู่นี้เป็นของตั้งใจ และเป็นเหตุผลที่คำตอบไม่ใช่จำนวนเต็มเล็ก ๆ',
        '• สังเกตอีกอย่างซึ่งสำคัญกว่า : ปลายส่วนโค้งทั้งสองข้างที่โจทย์เขียนไว้อยู่คนละจตุภาคกัน '
        '(จุดแรกอยู่จตุภาคที่ $2$ จุดหลังอยู่จตุภาคที่ $3$) '
        '⇒ ส่วนโค้งที่ให้มา <b>คร่อมสองจตุภาค</b> ⇒ การรู้แค่ว่า $P$ อยู่จตุภาคไหน '
        'ยังไม่พอที่จะปิดคำตอบ ต้องเอาปลายส่วนโค้งมาใช้เป็นขอบเขตจริง ๆ '
        'นี่เป็นสัญญาณล่วงหน้าว่าจะมีคู่ค่าที่ผ่านเงื่อนไขจตุภาคแต่หลุดออกนอกส่วนโค้ง',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\dfrac{\\sqrt{1 - 2\\sin\\theta\\cos\\theta}}{\\sin\\theta + \\cos\\theta} '
        '+ \\dfrac{\\sqrt{1 + 2\\sin\\theta\\cos\\theta}}{\\sin\\theta - \\cos\\theta}$ '
        'ออกมาเป็นจำนวนเดียว',
        '',
        '<b>【 เปลี่ยนผลคูณ $\\sec\\theta\\csc\\theta$ ให้เป็นค่าของ $\\sin\\theta\\cos\\theta$ '
        'แล้วแปลปลายส่วนโค้งทั้งสองจุดกลับเป็นขนาดมุม เพื่อเขียนเงื่อนไขของ $P$ ให้เป็นช่วงของ '
        '$\\theta$ จากนั้นใช้เครื่องหมายของผลคูณคู่กับเครื่องหมายของ $\\cos\\theta$ บีบให้เหลือ '
        'สาขาเดียว ถอดค่า $\\sin\\theta$ กับ $\\cos\\theta$ ออกมาจากกำลังสองสมบูรณ์สองอัน '
        'โดยตัดสินเครื่องหมายจากช่วง ⛔ ไม่ใช่จากความเคยชิน แล้วจึงแทนค่าลงในนิพจน์ 】</b>',
        '',
        '<b>ขั้นที่ 1 · แปลเงื่อนไขผลคูณ $\\sec\\theta\\csc\\theta$ ให้เป็นค่าของ '
        '$\\sin\\theta\\cos\\theta$</b>',
        '• สูตรที่ใช้ : $\\sec\\theta = \\dfrac{1}{\\cos\\theta}$ และ '
        '$\\csc\\theta = \\dfrac{1}{\\sin\\theta}$',
        '• ระบุตัวแปรก่อนแทนค่า : ให้ $s = \\sin\\theta$ และ $c = \\cos\\theta$ '
        'เพื่อให้บรรทัดต่อ ๆ ไปสั้นลง',
        '• คูณสองสูตรเข้าด้วยกัน : $\\sec\\theta\\csc\\theta = '
        '\\dfrac{1}{\\cos\\theta}\\cdot\\dfrac{1}{\\sin\\theta} = '
        '\\dfrac{1}{\\sin\\theta\\cos\\theta} = \\dfrac{1}{sc}$',
        '• แทนค่าที่โจทย์ให้ : $\\dfrac{1}{sc} = -\\dfrac{25}{12}$ '
        '⇒ กลับเศษเป็นส่วนทั้งสองข้าง (ทำได้เพราะทั้งสองข้างไม่เป็นศูนย์) '
        '⇒ $sc = \\sin\\theta\\cos\\theta = -\\dfrac{12}{25}$',
        '• อ่านความหมายของเครื่องหมายทันทีขณะที่ยังจำได้ : $sc < 0$ แปลว่า $\\sin\\theta$ '
        'กับ $\\cos\\theta$ มีเครื่องหมายตรงข้ามกัน ⇒ จุด $P$ ต้องอยู่ในจตุภาคที่ $2$ '
        'หรือจตุภาคที่ $4$ เท่านั้น · ⛔ แต่ข้อมูลแค่นี้ยัง<b>ไม่พอ</b>ปิดคำตอบ '
        'เพราะยังเหลือความเป็นไปได้ตั้งสองจตุภาค',
        '• บันทึกไว้ด้วยว่าเงื่อนไขนี้บังคับกลาย ๆ ว่า $\\sin\\theta \\ne 0$ และ '
        '$\\cos\\theta \\ne 0$ (ไม่เช่นนั้น $\\sec\\theta$ หรือ $\\csc\\theta$ '
        'จะไม่นิยาม) ⇒ จุดบนแกนทั้งสี่จุดถูกตัดออกไปตั้งแต่บรรทัดนี้',
        '',
        '<b>ขั้นที่ 2 · แปลส่วนโค้งที่โจทย์ให้เป็นช่วงของ $\\theta$</b>',
        '• อ่านปลายข้างแรก $\\left(-\\dfrac{\\sqrt{2}}{2},\\ \\dfrac{\\sqrt{2}}{2}\\right)$ : '
        'ค่าสัมบูรณ์ของพิกัดทั้งสองเท่ากัน ⇒ มุมอ้างอิงคือ $\\dfrac{\\pi}{4}$ · '
        'พิกัดที่หนึ่งเป็นลบและพิกัดที่สองเป็นบวก ⇒ อยู่จตุภาคที่ $2$ ⇒ ขนาดมุมคือ '
        '$\\pi - \\dfrac{\\pi}{4} = \\dfrac{3\\pi}{4}$',
        '• อ่านปลายข้างที่สอง $\\left(-\\dfrac{\\sqrt{2}}{2},\\ -\\dfrac{\\sqrt{2}}{2}\\right)$ : '
        'มุมอ้างอิง $\\dfrac{\\pi}{4}$ เหมือนกัน แต่พิกัดเป็นลบทั้งคู่ ⇒ อยู่จตุภาคที่ $3$ '
        '⇒ ขนาดมุมคือ $\\pi + \\dfrac{\\pi}{4} = \\dfrac{5\\pi}{4}$',
        '• เดินทวนเข็มนาฬิกาคือเดินไปทาง $\\theta$ ที่เพิ่มขึ้น ⇒ ส่วนโค้งที่โจทย์ระบุแปลตรงตัวได้ว่า '
        '$\\dfrac{3\\pi}{4} \\le \\theta \\le \\dfrac{5\\pi}{4}$ '
        '(ค่าเหล่านี้อยู่ในกรอบ $0 \\le \\theta < 2\\pi$ ที่โจทย์วางไว้อยู่แล้ว)',
        '• เก็บเกี่ยวข้อมูลจากช่วงนี้ทันที — เรื่องที่ได้ฟรีคือเครื่องหมายของ $\\cos\\theta$ : '
        'ที่ปลายทั้งสองข้างมี $\\cos\\theta = -\\dfrac{\\sqrt{2}}{2}$ และระหว่างทาง '
        '$\\cos\\theta$ ลดลงไปต่ำสุดที่ $\\cos\\pi = -1$ แล้วไต่กลับขึ้นมา '
        '⇒ ตลอดช่วงนี้ $\\cos\\theta \\le -\\dfrac{\\sqrt{2}}{2} < 0$ '
        '⇒ <b>ทั้งช่วงมี $\\cos\\theta < 0$</b>',
        '• ⛔ เรื่องที่<b>ไม่ได้</b>ฟรีคือจตุภาค : ช่วง '
        '$\\left[\\dfrac{3\\pi}{4},\\ \\dfrac{5\\pi}{4}\\right]$ คร่อมทั้งจตุภาคที่ $2$ '
        '(ตอน $\\dfrac{3\\pi}{4} \\le \\theta < \\pi$) และจตุภาคที่ $3$ '
        '(ตอน $\\pi < \\theta \\le \\dfrac{5\\pi}{4}$) โดยมี $\\theta = \\pi$ '
        'ซึ่งอยู่บนแกนคั่นกลาง ⇒ ยังต้องหาเงื่อนไขมาบีบต่อ',
        '',
        '<b>ขั้นที่ 3 · เลือกสาขา — เอาเครื่องหมายของผลคูณมาชนกับเครื่องหมายของ $\\cos\\theta$</b>',
        '• ของสองอย่างที่มีอยู่ในมือ : จากขั้นที่ 1 ได้ $sc = -\\dfrac{12}{25} < 0$ '
        'และจากขั้นที่ 2 ได้ $c < 0$ ตลอดช่วง',
        '• หารเพื่อดึงเครื่องหมายของ $s$ ออกมา : $s = \\dfrac{sc}{c}$ '
        '⇒ เศษเป็นลบและตัวส่วนเป็นลบ ⇒ ผลหารเป็นบวก ⇒ $\\sin\\theta > 0$',
        '• $s > 0$ คู่กับ $c < 0$ แปลว่า $P$ อยู่ในจตุภาคที่ $2$ '
        '⇒ ตัดกับช่วงในขั้นที่ 2 แล้วเหลือ $\\dfrac{3\\pi}{4} < \\theta < \\pi$ '
        'ซึ่งเป็น<b>ครึ่งบน</b>ของส่วนโค้งที่โจทย์ให้',
        '• ตรวจให้ชัดว่าครึ่งล่างหายไปเพราะอะไร : ถ้า $\\pi < \\theta \\le \\dfrac{5\\pi}{4}$ '
        'จะอยู่จตุภาคที่ $3$ ซึ่งมีทั้ง $\\sin\\theta < 0$ และ $\\cos\\theta < 0$ '
        '⇒ ผลคูณ $sc$ จะเป็น<b>บวก</b> ขัดกับ $sc = -\\dfrac{12}{25}$ ⇒ ตัดทิ้งทั้งครึ่ง',
        '• ปลายทั้งสองข้างก็ใช้ไม่ได้เช่นกัน : ที่ $\\theta = \\dfrac{3\\pi}{4}$ ได้ '
        '$sc = \\left(\\dfrac{\\sqrt{2}}{2}\\right)\\left(-\\dfrac{\\sqrt{2}}{2}\\right) '
        '= -\\dfrac{1}{2}$ ซึ่งไม่เท่ากับ $-\\dfrac{12}{25}$ · ที่ $\\theta = \\pi$ ได้ '
        '$\\sin\\pi = 0$ ซึ่งขัดกับข้อสังเกตท้ายขั้นที่ 1 ⇒ ช่วงที่เหลือเป็นช่วงเปิดจริง ๆ',
        '',
        '<b>ขั้นที่ 4 · หาค่า $\\sin\\theta$ กับ $\\cos\\theta$ '
        'โดยตัดสินเครื่องหมายจากช่วง ⛔ จุดหักของข้อนี้</b>',
        '• สูตรที่ใช้คือกำลังสองสมบูรณ์สองอันจากบล็อกความรู้พื้นฐาน แทนค่า '
        '$sc = -\\dfrac{12}{25}$ ลงไปตรง ๆ : '
        '$\\left(s + c\\right)^{2} = 1 + 2sc = 1 - \\dfrac{24}{25} = \\dfrac{1}{25}$',
        '• และ $\\left(s - c\\right)^{2} = 1 - 2sc = 1 + \\dfrac{24}{25} = \\dfrac{49}{25}$',
        '• ถอดรากอย่างซื่อสัตย์ก่อน คือเขียนเป็นค่าสัมบูรณ์ : '
        '$\\left|s + c\\right| = \\sqrt{\\dfrac{1}{25}} = \\dfrac{1}{5}$ และ '
        '$\\left|s - c\\right| = \\sqrt{\\dfrac{49}{25}} = \\dfrac{7}{5}$ '
        '⇒ ตอนนี้รู้แค่<b>ขนาด</b> ยังไม่รู้เครื่องหมาย',
        '• เครื่องหมายของ $s - c$ ตัดสินได้ง่าย : จากขั้นที่ 3 มี $s > 0 > c$ '
        '⇒ ลบจำนวนลบก็คือบวกเพิ่ม ⇒ $s - c > 0$ ⇒ $s - c = \\dfrac{7}{5}$',
        '• ⛔ เครื่องหมายของ $s + c$ คือจุดที่ต้องใช้ช่วง ไม่ใช่ความเคยชิน : บนช่วง '
        '$\\left(\\dfrac{3\\pi}{4},\\ \\pi\\right)$ มี '
        '$\\left|\\cos\\theta\\right| > \\left|\\sin\\theta\\right|$ (เหตุผลอยู่ในบล็อก '
        'ความรู้พื้นฐาน คือ $\\left|\\tan\\theta\\right| < 1$ บนช่วงนี้) '
        'และตัวที่ใหญ่กว่านั้นเป็นลบ ⇒ เมื่อบวกกันฝ่ายลบชนะ ⇒ $s + c < 0$ '
        '⇒ $s + c = -\\dfrac{1}{5}$',
        '• แก้ระบบสองสมการนี้ : บวกกันได้ $2s = \\dfrac{7}{5} + \\left(-\\dfrac{1}{5}\\right) '
        '= \\dfrac{6}{5}$ ⇒ $s = \\sin\\theta = \\dfrac{3}{5}$ · '
        'ลบกันได้ $2c = \\left(-\\dfrac{1}{5}\\right) - \\dfrac{7}{5} = -\\dfrac{8}{5}$ '
        '⇒ $c = \\cos\\theta = -\\dfrac{4}{5}$',
        '• ⭐ ทำไมบรรทัดเครื่องหมายข้างบนถึงเป็นหัวใจของข้อนี้ : ถ้าเผลอหยิบ '
        '$s + c = +\\dfrac{1}{5}$ จะได้ $s = \\dfrac{4}{5}$ กับ $c = -\\dfrac{3}{5}$ '
        'ซึ่ง<b>ก็อยู่ในจตุภาคที่ $2$ เหมือนกัน</b> และ<b>ก็ให้ '
        '$sc = -\\dfrac{12}{25}$ เท่ากันเป๊ะ</b> ⇒ เงื่อนไขระดับจตุภาคแยกสองคู่นี้ไม่ออกเลย',
        '• สิ่งเดียวที่แยกออกคือขอบล่าง $\\dfrac{3\\pi}{4}$ ของส่วนโค้ง : คู่ '
        '$\\left(\\dfrac{4}{5},\\ -\\dfrac{3}{5}\\right)$ ตรงกับ '
        '$\\theta = \\pi - \\arcsin\\dfrac{4}{5} \\approx 2.2143$ เรเดียน ขณะที่ '
        '$\\dfrac{3\\pi}{4} \\approx 2.3562$ ⇒ จุดนั้นอยู่<b>ก่อน</b>จุดเริ่มต้นของส่วนโค้ง '
        'จึงหลุดออกนอกบริเวณที่โจทย์อนุญาต ⇒ ทิ้ง · ส่วนคู่ '
        '$\\left(\\dfrac{3}{5},\\ -\\dfrac{4}{5}\\right)$ ตรงกับ '
        '$\\theta \\approx 2.4981$ ซึ่งอยู่ในส่วนโค้งพอดี ⇒ เก็บไว้',
        '',
        '<b>ขั้นที่ 5 · แทนค่าลงในนิพจน์ โดยคุมกรณฑ์ให้ไม่ติดลบทุกตัว</b>',
        '• กรณฑ์ตัวแรก : $\\sqrt{1 - 2sc} = \\sqrt{\\dfrac{49}{25}} = \\dfrac{7}{5}$ '
        '· ค่านี้เท่ากับ $\\left|s - c\\right|$ และบังเอิญตรงกับ $s - c$ พอดีเพราะ '
        '$s - c > 0$ อยู่แล้ว',
        '• กรณฑ์ตัวที่สอง : $\\sqrt{1 + 2sc} = \\sqrt{\\dfrac{1}{25}} = \\dfrac{1}{5}$ '
        '⛔ ตรงนี้ต่างจากตัวแรก เพราะ $s + c = -\\dfrac{1}{5}$ เป็นลบ '
        '⇒ กรณฑ์เท่ากับ $\\left|s + c\\right| = \\dfrac{1}{5}$ ⛔ ไม่ใช่ $s + c$ '
        '· รากที่สองเป็นค่าไม่ติดลบเสมอ',
        '• เศษส่วนก้อนแรก : $\\dfrac{\\sqrt{1 - 2sc}}{s + c} = '
        '\\dfrac{\\dfrac{7}{5}}{-\\dfrac{1}{5}} = \\dfrac{7}{5}\\times\\left(-5\\right) = -7$',
        '• เศษส่วนก้อนที่สอง : $\\dfrac{\\sqrt{1 + 2sc}}{s - c} = '
        '\\dfrac{\\dfrac{1}{5}}{\\dfrac{7}{5}} = \\dfrac{1}{5}\\times\\dfrac{5}{7} '
        '= \\dfrac{1}{7}$',
        '• บวกกันโดยทำตัวส่วนให้เท่ากัน : $-7 + \\dfrac{1}{7} = -\\dfrac{49}{7} + '
        '\\dfrac{1}{7} = -\\dfrac{48}{7}$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่า $\\sin\\theta = \\dfrac{3}{5}$ และ '
        '$\\cos\\theta = -\\dfrac{4}{5}$ กลับเข้าไปตรวจเงื่อนไขทุกข้อของโจทย์ '
        'แล้วประเมินค่านิพจน์เป็นทศนิยมตรง ๆ ⛔ ไม่แตะเอกลักษณ์กำลังสองสมบูรณ์อีกเลย)</b>',
        '• ตรวจว่าเป็นจุดบนวงกลมหนึ่งหน่วยจริง : '
        '$\\left(\\dfrac{3}{5}\\right)^{2} + \\left(-\\dfrac{4}{5}\\right)^{2} = '
        '\\dfrac{9}{25} + \\dfrac{16}{25} = \\dfrac{25}{25} = 1$ ✓',
        '• ตรวจเงื่อนไขผลคูณ : $\\sin\\theta\\cos\\theta = '
        '\\dfrac{3}{5}\\cdot\\left(-\\dfrac{4}{5}\\right) = -\\dfrac{12}{25}$ '
        '⇒ $\\sec\\theta\\csc\\theta = \\dfrac{1}{-\\dfrac{12}{25}} = -\\dfrac{25}{12}$ ✓ '
        'ตรงกับที่โจทย์ให้พอดี',
        '• ตรวจเงื่อนไขส่วนโค้ง : $\\theta = \\pi - \\arcsin\\dfrac{3}{5} \\approx '
        '3.1416 - 0.6435 = 2.4981$ เรเดียน · ขอบของส่วนโค้งคือ '
        '$\\dfrac{3\\pi}{4} \\approx 2.3562$ กับ $\\dfrac{5\\pi}{4} \\approx 3.9270$ '
        '⇒ $2.3562 < 2.4981 < 3.9270$ ✓ จุด $P$ อยู่บนส่วนโค้งที่โจทย์ระบุจริง',
        '• ประเมินค่านิพจน์ด้วยทศนิยมโดยไม่ผ่านสูตรใด ๆ : $\\sin\\theta \\approx 0.6$ · '
        '$\\cos\\theta \\approx -0.8$ ⇒ $1 - 2sc \\approx 1.96$ ⇒ กรณฑ์ $\\approx 1.4$ · '
        '$1 + 2sc \\approx 0.04$ ⇒ กรณฑ์ $\\approx 0.2$ · $s + c \\approx -0.2$ · '
        '$s - c \\approx 1.4$ ⇒ ค่ารวม $\\approx \\dfrac{1.4}{-0.2} + \\dfrac{0.2}{1.4} '
        '= -7 + 0.142857 = -6.857143$ · เทียบกับ $-\\dfrac{48}{7} \\approx -6.857143$ ✓',
        '• 📌 ตรวจเพิ่มอีกชั้นว่าสาขาที่เลือกเป็นสาขาเดียวจริง : คู่ '
        '$\\left(\\sin\\theta,\\ \\cos\\theta\\right) = '
        '\\left(\\dfrac{4}{5},\\ -\\dfrac{3}{5}\\right)$ ก็ให้ '
        '$\\sec\\theta\\csc\\theta = -\\dfrac{25}{12}$ เหมือนกันทุกประการ '
        'แต่ให้ $\\theta \\approx 2.2143$ ซึ่งน้อยกว่า $2.3562$ ⇒ อยู่นอกส่วนโค้ง ⇒ ใช้ไม่ได้ '
        '· ⇒ ข้อสรุปที่ต้องจำจากข้อนี้คือ ประโยคเรื่องส่วนโค้งในโจทย์ไม่ใช่เครื่องประดับ '
        'แต่เป็นเงื่อนไขเดียวที่ทำให้คำตอบเป็นค่าเดียว',
        '',
        '✅ <b>คำตอบ</b> ค่าของนิพจน์ที่โจทย์ถามเท่ากับ $-\\dfrac{48}{7}$',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอโจทย์ที่ให้ผลคูณหรือผลบวกของอัตราส่วนส่วนกลับมา เช่น '
        '$\\sec\\theta\\csc\\theta$ หรือ $\\tan\\theta + \\cot\\theta$ '
        'ให้แปลงเป็นค่าของ $\\sin\\theta\\cos\\theta$ ทันทีเป็นก้าวแรก '
        'เพราะพอได้ $\\sin\\theta\\cos\\theta$ แล้ว กำลังสองสมบูรณ์สองอัน '
        '$\\left(s \\pm c\\right)^{2} = 1 \\pm 2sc$ จะยกขนาดของ $s + c$ กับ $s - c$ '
        'มาให้ทันทีบรรทัดเดียว',
        '• เวลาถอดของออกจากกรณฑ์ ให้เขียนค่าสัมบูรณ์ไว้ก่อนเสมอ แล้วค่อยไปหาเครื่องหมายทีหลัง '
        '· วิธีจำสั้น ๆ คือ “จตุภาคบอกเครื่องหมายของ $\\sin$ กับ $\\cos$ แยกกันได้ '
        'แต่เครื่องหมายของ<b>ผลบวก</b> $\\sin\\theta + \\cos\\theta$ ต้องดูว่าตัวไหนใหญ่กว่า” '
        '⇒ ต้องใช้ช่วง ไม่ใช่ใช้จตุภาค',
        '• จำเส้นทแยงมุมสี่เส้น $\\dfrac{\\pi}{4},\\ \\dfrac{3\\pi}{4},\\ \\dfrac{5\\pi}{4},\\ '
        '\\dfrac{7\\pi}{4}$ ไว้ให้ขึ้นใจ เพราะเป็นเส้นที่ '
        '$\\left|\\sin\\theta\\right| = \\left|\\cos\\theta\\right|$ พอดี '
        '⇒ เป็นเส้นแบ่งธรรมชาติเวลาต้องเทียบว่าตัวไหนใหญ่กว่า และมักเป็นขอบของช่วง '
        'ที่โจทย์แนวนี้หยิบมาใช้',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\dfrac{50}{7}$ เพราะหยุดวิเคราะห์ที่ระดับ “จตุภาค” เฉย ๆ '
        'คือรู้แค่ว่า $\\sin\\theta\\cos\\theta < 0$ กับ $\\cos\\theta < 0$ '
        'จึงสรุปว่า $P$ อยู่จตุภาคที่ $2$ แล้วหยิบคู่ '
        '$\\left(\\sin\\theta,\\ \\cos\\theta\\right) = '
        '\\left(\\dfrac{4}{5},\\ -\\dfrac{3}{5}\\right)$ มาแทน — นี่คือกับดักหลักของข้อนี้ '
        'และอันตรายที่สุด เพราะคู่นี้ผ่านทั้งเอกลักษณ์ '
        '$\\sin^{2}\\theta + \\cos^{2}\\theta = 1$ และผ่านเงื่อนไข '
        '$\\sec\\theta\\csc\\theta = -\\dfrac{25}{12}$ ครบถ้วน '
        '· สิ่งที่ผิดคือมันตรงกับ $\\theta \\approx 2.2143$ ขณะที่ส่วนโค้งเริ่มที่ '
        '$\\dfrac{3\\pi}{4} \\approx 2.3562$ ⇒ จุดนั้นหลุดออกนอกส่วนโค้งที่โจทย์ระบุ '
        '⇒ บทเรียนคือ<b>จตุภาคเดียวกันมีคู่คำตอบสองคู่</b> ต้องเอาขอบล่าง '
        '$\\dfrac{3\\pi}{4}$ มาตัด แทนค่าคู่นี้ลงไปจะได้ '
        '$\\dfrac{7/5}{1/5} + \\dfrac{1/5}{7/5} = 7 + \\dfrac{1}{7} = \\dfrac{50}{7}$ '
        'ซึ่งเป็นค่าที่ผิด',
        '• ได้ค่า $-\\dfrac{50}{7}$ เพราะถอดกรณฑ์โดยไม่ใส่ค่าสัมบูรณ์ คือเผลอเขียน '
        '$\\sqrt{1 + 2\\sin\\theta\\cos\\theta} = \\sin\\theta + \\cos\\theta$ '
        'ทั้งที่บนส่วนโค้งนี้ $\\sin\\theta + \\cos\\theta = -\\dfrac{1}{5}$ เป็นลบ '
        '· ผิดแน่นอนเพราะฝั่งซ้ายเป็นรากที่สองซึ่งไม่มีทางติดลบ ส่วนฝั่งขวาติดลบ '
        '⇒ สองข้างเป็นคนละเครื่องหมายกันตั้งแต่ต้น · เดินตามเส้นทางนี้จะได้ '
        '$\\dfrac{s - c}{s + c} + \\dfrac{s + c}{s - c} = -7 - \\dfrac{1}{7} '
        '= -\\dfrac{50}{7}$ · ค่าที่ถูกต้องคือใช้ '
        '$\\left|\\sin\\theta + \\cos\\theta\\right| = \\dfrac{1}{5}$',
        '• ได้ค่า $\\dfrac{48}{7}$ เพราะใช้แต่เงื่อนไข $\\sin\\theta\\cos\\theta < 0$ '
        'แล้วไปหยิบจตุภาคที่ $4$ คือ $\\left(\\sin\\theta,\\ \\cos\\theta\\right) = '
        '\\left(-\\dfrac{3}{5},\\ \\dfrac{4}{5}\\right)$ '
        'โดยไม่ได้ใช้ส่วนโค้งที่โจทย์ให้เลยแม้แต่นิดเดียว '
        '· ผิดแน่นอนเพราะคู่นี้ตรงกับ $\\theta \\approx 5.6397$ เรเดียน '
        'ซึ่งมากกว่า $\\dfrac{5\\pi}{4} \\approx 3.9270$ ⇒ อยู่นอกส่วนโค้งไปไกล '
        '· สังเกตด้วยว่าค่าที่ได้เป็น<b>ค่าตรงข้าม</b>ของคำตอบจริงพอดี '
        'เพราะการเปลี่ยนเครื่องหมายของทั้ง $\\sin\\theta$ และ $\\cos\\theta$ '
        'ไม่กระทบกรณฑ์ทั้งสองตัวเลย แต่พลิกเครื่องหมายของตัวส่วนทั้งสองตัว '
        '⇒ ความบังเอิญที่ดูสวยแบบนี้เป็นสัญญาณเตือนให้ย้อนกลับไปอ่านเงื่อนไขที่ยังไม่ได้ใช้',
        '• ได้ค่า $0$ เพราะจับคู่กรณฑ์กับตัวส่วนสลับกัน คือเผลออ่านโจทย์เป็น '
        '$\\dfrac{\\sqrt{1 + 2sc}}{s + c} + \\dfrac{\\sqrt{1 - 2sc}}{s - c}$ '
        'ซึ่งจะกลายเป็น $\\dfrac{\\left|s + c\\right|}{s + c} + '
        '\\dfrac{\\left|s - c\\right|}{s - c} = \\left(-1\\right) + 1 = 0$ '
        '· ผิดเพราะอ่านตำแหน่งของกรณฑ์ผิดตั้งแต่แรก และค่าที่ได้ยัง<b>ไม่ขึ้นกับ</b> '
        '$-\\dfrac{25}{12}$ ที่โจทย์อุตส่าห์ให้มาเลยแม้แต่น้อย '
        '⇒ ถ้าคำนวณแล้วพบว่าข้อมูลก้อนหนึ่งของโจทย์ไม่เคยถูกใช้ '
        'ให้ย้อนกลับไปดูว่าลอกนิพจน์มาถูกหรือไม่ก่อนเสมอ',
    ],
    'V.mold: G = a point P on the unit circle centred at the origin, reached by measuring an arc of '
    'length theta counterclockwise from (1, 0) with 0 <= theta < 2*pi, restricted to the sub-arc that '
    'runs counterclockwise from (-sqrt(2)/2, sqrt(2)/2) to (-sqrt(2)/2, -sqrt(2)/2), together with the '
    'single numeric datum sec(theta)*csc(theta) = -25/12 / A = the value of a sum of two fractions whose '
    'numerators are the square roots of 1 - 2*sin*cos and 1 + 2*sin*cos and whose denominators are the '
    'cross-paired quantities sin + cos and sin - cos, asked as a free numeric response with no candidate '
    'values on the page / M = M-SUBQUADRANT-ARC-PICKS-BRANCH, that is: turn the product of the two '
    'reciprocal ratios into sin*cos = -12/25, read the two named unit-circle points back as the angles '
    '3*pi/4 and 5*pi/4 so that the stated arc becomes the closed interval [3*pi/4, 5*pi/4] on which the '
    'cosine is at most -sqrt(2)/2 and therefore negative throughout, combine the negative product with '
    'the negative cosine to force a positive sine and hence the upper half of that interval, recover '
    '|sin + cos| = 1/5 and |sin - cos| = 7/5 from the two square completions, fix each sign from the '
    'interval rather than from habit (on (3*pi/4, pi) the cosine dominates in size, so sin + cos is '
    'negative), and only then substitute while keeping every radical non-negative. '
    'Rubric F3 C3 P2 T3 L1 = 12/15, which reaches the very-hard threshold of 12 with T = 3 -> level: '
    'ยากมาก. F = 3 because three independent pieces of knowledge must all be present and none can be '
    'skipped: the reciprocal definitions that collapse sec*csc into 1/(sin*cos), the pair of square '
    'completions (sin +/- cos)^2 = 1 +/- 2*sin*cos, and the rule that the radical sign denotes the '
    'non-negative root so that sqrt(x^2) = |x|; drop any one of the three and the item cannot be '
    'started, finished, or signed correctly. C = 3 because three conditions of genuinely different '
    'kinds have to be welded: an algebraic one (the value of the product), a positional one (the named '
    'arc, which must first be translated into an interval of theta), and an order comparison inside '
    'that interval (|cos| against |sin|); each one alone leaves the answer undetermined, and the third '
    'is invisible to a reader who thinks in quadrants. P = 2 rather than 3 because the arithmetic is '
    'short once the branch is settled, being two square roots of exact squares and one addition of '
    'fractions, so length is not what makes this item hard. T = 3 because two hidden turning points '
    'must both be discovered before any answer can be written: first that the given arc straddles two '
    'quadrants so that quadrant reasoning is not a substitute for the arc, and second that even inside '
    'the surviving quadrant two rational pairs satisfy every stated numeric condition, (3/5, -4/5) and '
    '(4/5, -3/5), and they are separated only by the lower endpoint 3*pi/4; a solver who misses either '
    'turn produces a clean-looking wrong value rather than getting stuck. L = 1 because the statement '
    'carries no real-world scene and no figure, yet the reader must still place two named points on the '
    'circle and see the arc between them in order to read off the interval at all. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b20.py): the q138 block builds the four rational candidates (3/5, -4/5), (4/5, -3/5), '
    '(-3/5, 4/5) and (-4/5, 3/5), keeps only those with 1/(s*c) equal to -25/12, which all four satisfy, '
    'and then filters by 3*pi/4 <= atan2(s, c) mod 2*pi <= 5*pi/4; exactly one survives, and the value of '
    'sqrt(1-2*s*c)/(s+c) + sqrt(1+2*s*c)/(s-c) at that survivor simplifies to -48/7, matching the stored '
    'key, which the rational-form check confirms as the string -48/7. Two trap lines sit in the same '
    'block: with s = 3/5 and c = -4/5, the expression (s-c)/(s+c) + (s+c)/(s-c), which is what dropping '
    'the absolute value produces, simplifies to -50/7, and the swapped pairing '
    'sqrt(1+2*s*c)/(s+c) + sqrt(1-2*s*c)/(s-c) simplifies to exactly 0. The remaining error paths were '
    'also computed by machine rather than invented: the candidate (4/5, -3/5) sits at theta about '
    '2.214297 radians, below 3*pi/4 about 2.356194, and its expression value is exactly 50/7; the '
    'quadrant-4 candidate (-3/5, 4/5) sits at theta about 5.639684, above 5*pi/4 about 3.926991, and its '
    'value is exactly 48/7, the exact negative of the true answer; and the fourth candidate (-4/5, 3/5) '
    'at theta about 5.355890 returns -50/7. The check block was verified to be independent: substituting '
    's = 3/5 and c = -4/5 returns s^2 + c^2 = 1 and s*c = -12/25 hence sec*csc = -25/12, the surviving '
    'angle is theta = pi - asin(3/5) about 2.498092 which lies strictly between 2.356194 and 3.926991, '
    'and a purely numeric evaluation of the original expression at that angle returns -6.857143, equal '
    'to -48/7 to six decimal places. '
    'Collision sweep re-run for this item over 6437 de-duplicated items (85 files: the bank sets '
    'directory plus k1 out plus k2 out), executed directly in this session because no collide_b20.py '
    'exists in the tree yet. On the G axis the opening template is shared with gen-chap-07-trigonometry-'
    'q023, which pins P by naming quadrant 2 plus a straight-line distance of sqrt(3) from (1, 0) and '
    'asks for the arc length itself, and with gen-chap-07-trigonometry-q041, which asks only which '
    'quadrant an arc of 670 units lands in; gen-chap-07-trigonometry-q008 gives the endpoint outright '
    'and asks for the endpoint after a cofunction shift. All three ask for a position or a length, never '
    'for the value of an expression, and none of them restricts P to an arc drawn between two named '
    'points: the phrase for lying on the arc drawn from a given point returns 0 items in the whole '
    'corpus, and the pair (unit circle text and both coordinates equal to sqrt(2)/2) returns 0 items. '
    'The closest relative on the constraint axis is chap-07-trigonometry-q48, which does hand over an '
    'interval, 3*pi/4 <= theta <= pi, but states it as a plain inequality that lies wholly inside one '
    'quadrant, hands over cos^2 - sin^2 = 1/sqrt(2) rather than a product, and asks for a tangent '
    'expression in which no radical sign ever has to be decided. The closest relative on the mechanism '
    'axis is gen-chap-07-trigonometry-q004, where tan + cot = -5/2 is likewise a reciprocal datum that '
    'reduces to sin*cos = -2/5; it was checked by machine that its stated range 0 < theta < pi admits '
    'two pairs just as ours does, but its target sin^3 - cos^3 = (s - c)(1 + s*c) evaluates to the same '
    '9*sqrt(5)/25 for both, so that item has no branch to separate and cannot share M. Elsewhere: a '
    'question mentioning both 3*pi/4 and 5*pi/4 returns 2 items, chap-07-trigonometry-q18 and '
    'gen-chap-07-trigonometry-q123, both graph-shape items in subtopic 7.3; sec and csc appear together '
    'in 6 items, none of which hands over the product sec*csc as a datum, the pattern sec ... csc ... = '
    'returning 0 items; and inside subtopic 7.2 the corpus holds 76 items, of which 11 are fill and none '
    'is graded very hard, so this item opens that cell rather than reusing it. Since this is a fill item '
    'there is no choice list, so no answer slot exists and nothing about the answer could have been '
    'positioned by hand.',
)

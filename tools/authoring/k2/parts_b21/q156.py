# -*- coding: utf-8 -*-
add(
    156,
    ['7.2'],
    'ปานกลาง',
    'กำหนดให้ $\\theta$ เป็นจำนวนจริงซึ่ง $0 \\le \\theta < 2\\pi$ และจุด $P$ มีพิกัดเป็น '
    '$\\left(13\\cos\\theta - 5,\\ 13\\sin\\theta + 12\\right)$ ถ้าจุด $P$ อยู่บนแกน $X$ '
    'และ $\\tan\\theta > 0$ แล้วพิกัดที่หนึ่งของจุด $P$ เท่ากับข้อใดต่อไปนี้',
    [
        '$-17$',
        '$-10$',
        '$0$',
        '$24$',
    ],
    1,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• จุดในระนาบเขียนเป็นคู่อันดับ $(x,\\ y)$ เสมอ โดยตัวหน้าคือ<b>พิกัดที่หนึ่ง</b> '
        'ซึ่งบอกตำแหน่งในแนวนอน และตัวหลังคือ<b>พิกัดที่สอง</b> ซึ่งบอกตำแหน่งในแนวตั้ง · '
        'จุดใดจะอยู่บนแกน $X$ ก็ต่อเมื่อ<b>พิกัดที่สองเป็นศูนย์</b> เพราะแกน $X$ คือเส้นตรงแนวนอน '
        'ที่ทุกจุดบนเส้นนี้ไม่ได้ยกสูงขึ้นหรือกดต่ำลงจากเส้นเลย ⇒ ระยะในแนวตั้งเท่ากับ $0$ พอดี · '
        '⛔ อย่าสลับกับแกน $Y$ ซึ่งเงื่อนไขคือพิกัดที่<b>หนึ่ง</b>เป็นศูนย์',
        '• นิยามของ $\\sin\\theta$ กับ $\\cos\\theta$ บนวงกลมหนึ่งหน่วย : เมื่อวัดส่วนโค้งยาว $\\theta$ หน่วย '
        'จากจุด $(1,\\ 0)$ ไปตามวงกลมหนึ่งหน่วย จุดปลายส่วนโค้งที่ได้คือจุด $(\\cos\\theta,\\ \\sin\\theta)$ '
        '⇒ $\\cos\\theta$ คือพิกัดแนวนอนของจุดปลาย และ $\\sin\\theta$ คือพิกัดแนวตั้งของจุดปลาย '
        '⇒ เครื่องหมายของทั้งสองค่าจึงบอกจตุภาคได้ทันที : จตุภาคที่ 1 บวกทั้งคู่ · จตุภาคที่ 2 '
        'มี $\\sin$ บวกและ $\\cos$ ลบ · จตุภาคที่ 3 ลบทั้งคู่ · จตุภาคที่ 4 มี $\\sin$ ลบและ $\\cos$ บวก',
        '• ความสัมพันธ์ $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ : เศษส่วนจะเป็นบวกได้ก็ต่อเมื่อ'
        'ตัวเศษกับตัวส่วนเป็นบวกทั้งคู่หรือเป็นลบทั้งคู่ ⇒ เงื่อนไข $\\tan\\theta > 0$ แปลตรงตัวได้ว่า '
        '$\\sin\\theta$ กับ $\\cos\\theta$ ต้อง<b>มีเครื่องหมายเดียวกัน</b> '
        '⇒ จุดปลายส่วนโค้งต้องอยู่ในจตุภาคที่ 1 หรือจตุภาคที่ 3 เท่านั้น',
        '• เอกลักษณ์พีทาโกรัส $\\sin^2\\theta + \\cos^2\\theta = 1$ ใช้หาค่าหนึ่งเมื่อรู้อีกค่าหนึ่ง '
        'แต่ให้มาเพียง<b>ขนาด</b>เท่านั้น เพราะการถอดรากที่สองมีทั้งค่าบวกและค่าลบ ⇒ '
        '⛔ เอกลักษณ์นี้เลือกเครื่องหมายให้ไม่ได้ ต้องให้เงื่อนไขอื่นในโจทย์เป็นคนเลือก · '
        'ถ้าจำสามเหลี่ยมอ้างอิงที่ด้านเป็นจำนวนเต็มไว้ เช่น $5$-$12$-$13$ ก็จะถอดรากได้ในหัวโดยไม่ต้องคำนวณ',
        '• ⭐ <b>กุญแจดอกที่หนึ่งของข้อนี้</b> : เงื่อนไขสองข้อที่โจทย์ให้มาทำหน้าที่คนละอย่างกัน — '
        'ข้อที่ว่าจุดอยู่บนแกน $X$ เป็นข้อที่<b>ให้ค่า</b> คือเปลี่ยนพิกัดที่สองให้เป็นสมการแล้วดึงค่าตรีโกณมิติออกมา '
        '· ส่วนข้อที่ว่า $\\tan\\theta > 0$ เป็นข้อที่<b>คัดผู้เข้าชิง</b> คือไม่ได้เพิ่มค่าใหม่ '
        'แต่ตัดสาขาที่เกินออกไป ⇒ ⛔ ถ้าใช้ไม่ครบทั้งสองข้อ จะเหลือคำตอบค้างอยู่สองค่าและเลือกผิดได้ทันที',
        '• ⭐ <b>กุญแจดอกที่สองของข้อนี้</b> : สมการ $\\sin\\theta = k$ เมื่อ $-1 < k < 0$ '
        'มีคำตอบใน $0 \\le \\theta < 2\\pi$ อยู่<b>สองค่าเสมอ</b> ค่าหนึ่งอยู่ในจตุภาคที่ 3 และอีกค่าหนึ่งอยู่ในจตุภาคที่ 4 '
        'เพราะบนวงกลมหนึ่งหน่วย เส้นแนวนอนที่ระดับความสูง $k$ ตัดวงกลมสองจุด และจุดตัดทั้งสองอยู่ใต้แกน $X$ '
        '⇒ ต้องเตรียมใจไว้ตั้งแต่ต้นว่าจะได้ผู้เข้าชิงสองราย และจะต้องมีขั้นตอนคัดตามมาแน่นอน',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $\\theta$ เป็นจำนวนจริงซึ่ง $0 \\le \\theta < 2\\pi$ ⇒ กวาดครบหนึ่งรอบพอดี ไม่มีการวนซ้ำรอบ',
        '• จุด $P$ มีพิกัดเป็น $\\left(13\\cos\\theta - 5,\\ 13\\sin\\theta + 12\\right)$ '
        '⇒ พิกัดที่หนึ่งของจุด $P$ คือ $13\\cos\\theta - 5$ และพิกัดที่สองของจุด $P$ คือ $13\\sin\\theta + 12$',
        '• เงื่อนไขข้อแรก : จุด $P$ อยู่บนแกน $X$',
        '• เงื่อนไขข้อที่สอง : $\\tan\\theta > 0$',
        '• สังเกตหน้าตาก่อนลงมือ : ค่าตรีโกณมิติไม่ได้ถูกยกมาให้ตรง ๆ แต่ถูกซ่อนอยู่ในพิกัดของจุด '
        '⇒ งานแรกคือแปลเงื่อนไขเชิงเรขาคณิตให้กลายเป็นสมการเสียก่อน · '
        'อีกอย่างที่ควรสังเกตคือตัวเลข $13$ กับ $12$ เป็นสองด้านของสามเหลี่ยมมุมฉาก $5$-$12$-$13$ '
        '⇒ เดาได้ตั้งแต่ยังไม่ลงมือว่าเลขจะออกมาลงตัวสวย · และเมื่อ $\\theta$ ไล่ครบหนึ่งรอบ จุด $P$ '
        'จะวิ่งเป็นวงกลมรัศมี $13$ ที่มีจุดศูนย์กลางอยู่ที่ $(-5,\\ 12)$ ซึ่งเก็บไว้ใช้ตรวจคำตอบตอนท้ายได้',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าพิกัดที่หนึ่งของจุด $P$ ซึ่งก็คือค่าของ $13\\cos\\theta - 5$ ออกมาเป็นจำนวนจริงจำนวนเดียว',
        '',
        '<b>【 แปลเงื่อนไขที่ว่าจุด $P$ อยู่บนแกน $X$ ให้เป็นสมการ $13\\sin\\theta + 12 = 0$ '
        'เพื่อดึงค่า $\\sin\\theta = -\\dfrac{12}{13}$ ออกมาจากพิกัดที่สอง จากนั้นใช้เงื่อนไข $\\tan\\theta > 0$ '
        'คัดผู้เข้าชิงสองรายให้เหลือเฉพาะจตุภาคที่ 3 แล้วอ่าน $\\cos\\theta = -\\dfrac{5}{13}$ '
        'จากสามเหลี่ยมอ้างอิง $5$-$12$-$13$ พร้อมเครื่องหมายลบ ก่อนแทนกลับลงในพิกัดที่หนึ่ง 】</b>',
        '',
        '<b>ขั้นที่ 1 · แปลเงื่อนไข “อยู่บนแกน $X$” ให้เป็นสมการ</b>',
        '• สูตรที่ใช้ : จุด $(x,\\ y)$ อยู่บนแกน $X$ ก็ต่อเมื่อ $y = 0$ '
        '⇒ เงื่อนไขนี้แตะเฉพาะ<b>พิกัดที่สอง</b> ไม่ได้แตะพิกัดที่หนึ่งเลย',
        '• ระบุตัวแปร : พิกัดที่สองของจุด $P$ คือ $13\\sin\\theta + 12$ ตามที่โจทย์กำหนดมา',
        '• แทนค่า : $13\\sin\\theta + 12 = 0$',
        '• ยุบสมการ : ย้าย $12$ ไปอีกข้าง ได้ $13\\sin\\theta = -12$ '
        'แล้วหารด้วย $13$ ทั้งสองข้าง ได้ $\\sin\\theta = -\\dfrac{12}{13}$',
        '• ตรวจความเป็นไปได้ก่อนเดินต่อ : ค่าของ $\\sin$ ต้องอยู่ระหว่าง $-1$ กับ $1$ เสมอ '
        'และ $\\dfrac{12}{13} < 1$ ⇒ มีจำนวนจริง $\\theta$ ที่ให้ค่านี้จริง ⇒ โจทย์ไม่ขัดแย้งในตัวเอง',
        '• 🔴 <b>กับดักที่หนึ่งของข้อนี้อยู่ตรงนี้</b> : เด็กจำนวนมากอ่านคำว่าแกน $X$ แล้วมือไปหยิบพิกัดที่หนึ่ง'
        'ทันทีเพราะเห็นตัวอักษร $X$ ตรงกัน ทั้งที่เงื่อนไขบอกว่าจุดอยู่บน<b>เส้น</b>แกน $X$ '
        'ซึ่งเป็นเส้นแนวนอน ⇒ สิ่งที่เป็นศูนย์คือความสูง นั่นคือพิกัดที่สอง · '
        'ถ้าหยิบผิดเป็นพิกัดที่หนึ่งเป็นศูนย์ นั่นคือเงื่อนไขของแกน $Y$ ซึ่งเป็นคนละเส้นกันคนละแนวกัน',
        '',
        '<b>ขั้นที่ 2 · หาผู้เข้าชิงทุกรายในหนึ่งรอบ</b>',
        '• สูตรที่ใช้ : $\\sin\\theta$ คือพิกัดแนวตั้งของจุดปลายส่วนโค้งบนวงกลมหนึ่งหน่วย '
        '⇒ $\\sin\\theta < 0$ ก็ต่อเมื่อจุดปลายส่วนโค้งอยู่<b>ใต้</b>แกน $X$',
        '• ระบุตัวเลข : ค่าที่ได้จากขั้นที่ 1 คือ $\\sin\\theta = -\\dfrac{12}{13}$ ซึ่งเป็นจำนวนลบ '
        '⇒ จุดปลายส่วนโค้งอยู่ใต้แกน $X$ ⇒ อยู่ในจตุภาคที่ 3 หรือจตุภาคที่ 4 เท่านั้น',
        '• นับผู้เข้าชิง : ลากเส้นแนวนอนที่ระดับความสูง $-\\dfrac{12}{13}$ ตัดวงกลมหนึ่งหน่วยได้สองจุด '
        'จุดหนึ่งอยู่ทางซ้ายของแกน $Y$ (จตุภาคที่ 3) และอีกจุดหนึ่งอยู่ทางขวาของแกน $Y$ (จตุภาคที่ 4) '
        '⇒ ในช่วง $0 \\le \\theta < 2\\pi$ จึงมีผู้เข้าชิงพอดีสองราย',
        '• ⭐ ย้ำให้ชัด : ทั้งสองรายนี้ต่างก็ทำให้จุด $P$ อยู่บนแกน $X$ ได้จริงทั้งคู่ '
        '⇒ เงื่อนไขข้อแรกเพียงข้อเดียว<b>ยังตัดสินไม่ได้</b> ⇒ ยังตอบไม่ได้ ต้องใช้เงื่อนไขที่เหลือต่อ',
        '',
        '<b>ขั้นที่ 3 · ใช้เงื่อนไข $\\tan\\theta > 0$ คัดให้เหลือสาขาเดียว</b>',
        '• สูตรที่ใช้ : $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        '⇒ $\\tan\\theta > 0$ ก็ต่อเมื่อ $\\sin\\theta$ กับ $\\cos\\theta$ มีเครื่องหมายเดียวกัน',
        '• ระบุเครื่องหมายที่รู้แล้ว : จากขั้นที่ 1 ได้ $\\sin\\theta = -\\dfrac{12}{13} < 0$ '
        '⇒ เพื่อให้เครื่องหมายเหมือนกัน จึงบังคับว่า $\\cos\\theta < 0$ ด้วย',
        '• อ่านจตุภาค : $\\sin\\theta < 0$ และ $\\cos\\theta < 0$ พร้อมกัน ⇒ ตรงกับจตุภาคที่ 3 เท่านั้น',
        '• ตรวจสาขาที่ถูกทิ้งให้เห็นกับตา : ถ้าเป็นจตุภาคที่ 4 จะได้ $\\sin\\theta < 0$ แต่ $\\cos\\theta > 0$ '
        '⇒ $\\tan\\theta$ เป็นลบ ⇒ ขัดกับเงื่อนไข $\\tan\\theta > 0$ ⇒ ทิ้งสาขานี้ไป',
        '• ⭐ สรุปขั้นนี้ : ผู้เข้าชิงสองรายเหลือรายเดียว คือรายที่อยู่ในจตุภาคที่ 3 '
        '⇒ ค่าของ $\\cos\\theta$ ถูกล็อกทั้งขนาดและเครื่องหมายแล้ว ⇒ โจทย์ข้อนี้มีคำตอบเดียว ไม่กำกวม',
        '',
        '<b>ขั้นที่ 4 · หาค่า $\\cos\\theta$ พร้อมเครื่องหมายที่ถูกต้อง</b>',
        '• สูตรที่ใช้ : $\\sin^2\\theta + \\cos^2\\theta = 1$ ⇒ $\\cos^2\\theta = 1 - \\sin^2\\theta$',
        '• แทนค่า : $\\cos^2\\theta = 1 - \\left(-\\dfrac{12}{13}\\right)^2 = 1 - \\dfrac{144}{169}$',
        '• ยุบ : $1 = \\dfrac{169}{169}$ ⇒ $\\cos^2\\theta = \\dfrac{169 - 144}{169} = \\dfrac{25}{169}$',
        '• ถอดรากที่สอง : $\\cos\\theta = \\dfrac{5}{13}$ หรือ $\\cos\\theta = -\\dfrac{5}{13}$ '
        '⇒ ได้แต่<b>ขนาด</b>คือ $\\dfrac{5}{13}$ ส่วนเครื่องหมายต้องหยิบมาจากขั้นที่ 3 ซึ่งบอกไว้แล้วว่า '
        '$\\cos\\theta < 0$ ⇒ $\\cos\\theta = -\\dfrac{5}{13}$',
        '• ตรวจด้วยสามเหลี่ยมอ้างอิง : ด้าน $5$ , $12$ และ $13$ เข้ากันได้กับพีทาโกรัส เพราะ '
        '$5^2 + 12^2 = 25 + 144 = 169 = 13^2$ ✓ ⇒ ในจตุภาคที่ 3 จุดปลายส่วนโค้งคือ '
        '$\\left(-\\dfrac{5}{13},\\ -\\dfrac{12}{13}\\right)$ ซึ่งติดลบทั้งสองพิกัดตามที่ควรเป็น',
        '• 🔴 <b>กับดักที่สองของข้อนี้อยู่ตรงนี้</b> : เลข $12$ ที่โผล่มาในโจทย์เป็นของ<b>ไซน์</b> '
        'เพราะมันมาจากพิกัดที่สอง ⇒ ในสามเหลี่ยมอ้างอิง $12$ คือด้านตรงข้ามมุม และ $5$ คือด้านประชิด '
        '⛔ ถ้าเผลอยก $12$ ไปเป็นของโคไซน์ จะได้ $\\cos\\theta = -\\dfrac{12}{13}$ ซึ่งเป็นคนละค่ากันทันที',
        '',
        '<b>ขั้นที่ 5 · แทนค่ากลับเข้าพิกัดที่หนึ่ง</b>',
        '• สูตรที่ใช้ : พิกัดที่หนึ่งของจุด $P$ คือ $13\\cos\\theta - 5$ ตามที่โจทย์กำหนดมาตั้งแต่ต้น',
        '• ระบุตัวแปร : ค่าที่ต้องแทนคือ $\\cos\\theta = -\\dfrac{5}{13}$ จากขั้นที่ 4 '
        '⛔ ไม่ใช่ $\\sin\\theta$ เพราะบรรทัดของพิกัดที่หนึ่งใช้โคไซน์',
        '• แทนค่า : พิกัดที่หนึ่ง $= 13\\left(-\\dfrac{5}{13}\\right) - 5$',
        '• ยุบ : เลข $13$ หน้าวงเล็บตัดกับ $13$ ที่เป็นตัวส่วนพอดี เหลือ $-5$ '
        '⇒ พิกัดที่หนึ่ง $= -5 - 5 = -10$',
        '• ตรวจความสมเหตุสมผลอย่างเร็ว : $\\cos\\theta$ เป็นลบ ⇒ $13\\cos\\theta$ เป็นลบ '
        'แล้วยังถูกลบออกอีก $5$ ⇒ คำตอบต้องเป็นจำนวนลบแน่นอน ✓ '
        'และเพราะ $-1 \\le \\cos\\theta \\le 1$ เสมอ พิกัดที่หนึ่งจึงต้องอยู่ในช่วง $-18$ ถึง $8$ '
        '⇒ ค่า $-10$ อยู่ในช่วงนี้จริง ✓',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่ากลับเข้าเงื่อนไขทั้งสองข้อของโจทย์พร้อมกัน '
        'แล้วยืนยันซ้ำด้วยระยะทางบนวงกลมรัศมี $13$)</b>',
        '• เส้นทางข้างบนเดินจากเงื่อนไขไปหาค่า รอบนี้จะเดินย้อนกลับ คือถือว่าจุดปลายส่วนโค้งคือ '
        '$\\left(-\\dfrac{5}{13},\\ -\\dfrac{12}{13}\\right)$ เป็นของที่มีอยู่แล้ว '
        'แล้วตรวจว่ามันสอดคล้องกับทุกบรรทัดของโจทย์หรือไม่ ⇒ เป็นการตรวจที่ไม่แตะการคัดจตุภาคเลยแม้แต่ก้าวเดียว',
        '• เงื่อนไขข้อแรก จุด $P$ ต้องอยู่บนแกน $X$ : พิกัดที่สองเท่ากับ '
        '$13\\left(-\\dfrac{12}{13}\\right) + 12 = -12 + 12 = 0$ ✓ '
        '⇒ จุด $P$ คือจุด $(-10,\\ 0)$ ซึ่งอยู่บนแกน $X$ จริง',
        '• เงื่อนไขข้อที่สอง $\\tan\\theta$ ต้องเป็นบวก : '
        '$\\tan\\theta = \\dfrac{-12/13}{-5/13} = \\dfrac{12}{5}$ ซึ่งเป็นจำนวนบวก ✓ '
        '(ลบหารลบได้บวก และ $13$ ตัดกันหมดพอดี)',
        '• ตรวจว่าจุดปลายส่วนโค้งอยู่บนวงกลมหนึ่งหน่วยจริง : '
        '$\\left(\\dfrac{5}{13}\\right)^2 + \\left(\\dfrac{12}{13}\\right)^2 = \\dfrac{25 + 144}{169} '
        '= \\dfrac{169}{169} = 1$ ✓ ⇒ ค่าที่ใช้ทั้งคู่เป็นค่าตรีโกณมิติที่มีอยู่จริง',
        '• 📌 ยืนยันอีกชั้นด้วยเรขาคณิต : เมื่อ $\\theta$ ไล่ครบหนึ่งรอบ จุด $P$ จะวิ่งบนวงกลมรัศมี $13$ '
        'ที่มีจุดศูนย์กลางอยู่ที่ $(-5,\\ 12)$ ⇒ คำตอบที่ได้ต้องอยู่ห่างจากจุดศูนย์กลางเป็นระยะ $13$ พอดี : '
        'ระยะจาก $(-10,\\ 0)$ ถึง $(-5,\\ 12)$ เท่ากับ $\\sqrt{(-10+5)^2 + (0-12)^2} = \\sqrt{25 + 144} '
        '= \\sqrt{169} = 13$ ✓ ⇒ ตรงเป๊ะ',
        '• 📌 กรองค่าที่เหลือด้วยขอบเขตแบบไม่ต้องคำนวณ : เพราะ $-1 \\le \\cos\\theta \\le 1$ '
        'พิกัดที่หนึ่ง $13\\cos\\theta - 5$ จึงอยู่ในช่วง $-18$ ถึง $8$ เสมอ '
        '⇒ ค่า $24$ ตกไปทันทีโดยไม่ต้องแตะตรีโกณมิติเลยสักบรรทัด',
        '',
        '✅ <b>คำตอบ</b> พิกัดที่หนึ่งของจุด $P$ เท่ากับ $-10$ → <b>ตัวเลือก 2</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอวลี “อยู่บนแกน …” ให้แปลเป็นสมการทันทีก่อนคิดอย่างอื่น : อยู่บนแกน $X$ ⇒ พิกัดที่สองเป็น $0$ '
        '· อยู่บนแกน $Y$ ⇒ พิกัดที่หนึ่งเป็น $0$ · วิธีจำที่ไม่มีวันสลับคือนึกภาพเส้นจริง : '
        'แกน $X$ เป็นเส้นแนวนอน ทุกจุดบนเส้นนี้จึงไม่มีความสูง ⇒ ตัวที่หายไปคือความสูง',
        '• เงื่อนไขที่มาในรูปเครื่องหมาย เช่น $\\tan\\theta > 0$ หรือ $\\sin\\theta\\cos\\theta < 0$ '
        'ให้แปลงเป็นตารางเครื่องหมายสี่จตุภาคทันที แล้วอ่านว่าเหลือจตุภาคใดบ้าง '
        '⇒ จะคัดสาขาได้ในหนึ่งบรรทัด โดยไม่ต้องไปหาค่ามุมจริง ๆ ซึ่งข้อนี้ไม่ได้ถามอยู่แล้ว',
        '• เห็นเลข $13$ มาคู่กับ $12$ หรือ $5$ ให้นึกถึงสามเหลี่ยม $5$-$12$-$13$ ทันที '
        '⇒ ถอดรากได้ในหัวโดยไม่ต้องคำนวณ · ชุดที่ควรจำติดตัวคือ $3$-$4$-$5$ · $5$-$12$-$13$ · '
        '$8$-$15$-$17$ · $7$-$24$-$25$ · $20$-$21$-$29$',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $-17$ เพราะแปลเงื่อนไขแรกถูกแล้วว่าพิกัดที่สองเป็นศูนย์ แต่ตอนสร้างสามเหลี่ยมอ้างอิง'
        'กลับสลับบทบาทของไซน์กับโคไซน์ คือยกเลข $12$ ไปเป็นของโคไซน์ ⇒ ใช้ $\\cos\\theta = -\\dfrac{12}{13}$ '
        '⇒ พิกัดที่หนึ่ง $= 13\\left(-\\dfrac{12}{13}\\right) - 5 = -12 - 5 = -17$ · '
        'ค่านี้พิสูจน์ว่าผิดได้ด้วยการแทนกลับ : ถ้า $\\cos\\theta = -\\dfrac{12}{13}$ แล้ว '
        '$\\sin\\theta = \\pm\\dfrac{5}{13}$ ⇒ พิกัดที่สองเท่ากับ $13\\left(\\pm\\dfrac{5}{13}\\right) + 12$ '
        'ซึ่งได้ $17$ หรือ $7$ ⇒ ไม่เป็นศูนย์สักกรณี ⇒ จุด $P$ ไม่ได้อยู่บนแกน $X$ ⇒ ขัดเงื่อนไขข้อแรกเต็ม ๆ · '
        'วิธีกันคือดูว่าสมการที่แก้มาจากบรรทัดไหน : บรรทัดพิกัดที่สองมี $\\sin$ อยู่ '
        '⇒ ค่าที่ดึงออกมาได้จึงเป็นค่าของ $\\sin$ ไม่ใช่ $\\cos$',
        '• ได้ค่า $0$ เพราะหา $\\sin\\theta = -\\dfrac{12}{13}$ มาถูกต้องแล้ว แต่<b>ตกเงื่อนไข</b> '
        '$\\tan\\theta > 0$ ไประหว่างทาง แล้วไปหยิบผู้เข้าชิงรายที่อยู่ในจตุภาคที่ 4 '
        '⇒ ใช้ $\\cos\\theta = \\dfrac{5}{13}$ ⇒ พิกัดที่หนึ่ง $= 13\\left(\\dfrac{5}{13}\\right) - 5 = 5 - 5 = 0$ · '
        'ค่านี้ผิดเพราะเมื่อแทนกลับจะได้ $\\tan\\theta = \\dfrac{-12/13}{5/13} = -\\dfrac{12}{5}$ '
        'ซึ่งเป็นจำนวน<b>ลบ</b> ⇒ ขัดกับเงื่อนไขที่โจทย์บังคับไว้ว่าต้องเป็นบวก · '
        'ค่านี้ยั่วใจเป็นพิเศษเพราะเลข $0$ ทำให้จุด $P$ กลายเป็นจุดกำเนิด ซึ่งดูเผิน ๆ ก็ยัง “อยู่บนแกน $X$” ได้ '
        '⇒ มันผ่านเงื่อนไขข้อแรกจริง แต่ตายที่ข้อที่สอง · วิธีกันคือขีดฆ่าเงื่อนไขในโจทย์ทีละข้อเมื่อใช้ไปแล้ว '
        'ถ้ายังมีข้อที่ไม่ถูกขีดฆ่าเหลืออยู่ แปลว่ายังตอบไม่ได้',
        '• ได้ค่า $24$ เพราะแปลวลี “อยู่บนแกน $X$” ผิดตั้งแต่บรรทัดแรก ไปตั้งให้<b>พิกัดที่หนึ่ง</b>เป็นศูนย์ '
        '(ซึ่งที่จริงเป็นเงื่อนไขของแกน $Y$) ⇒ แก้ $13\\cos\\theta - 5 = 0$ ได้ $\\cos\\theta = \\dfrac{5}{13}$ '
        'แล้วใช้ $\\tan\\theta > 0$ เลือก $\\sin\\theta = \\dfrac{12}{13}$ '
        'จากนั้นรายงานพิกัดอีกตัวคือ $13\\left(\\dfrac{12}{13}\\right) + 12 = 12 + 12 = 24$ · '
        'ค่านี้ผิดสองชั้น : ชั้นแรก สิ่งที่รายงานออกมาเป็นพิกัดที่<b>สอง</b> ไม่ใช่สิ่งที่โจทย์ถาม · '
        'ชั้นที่สอง พิกัดที่หนึ่งเท่ากับ $13\\cos\\theta - 5$ ซึ่งอยู่ในช่วง $-18$ ถึง $8$ เสมอ '
        'เพราะ $-1 \\le \\cos\\theta \\le 1$ ⇒ ค่า $24$ เป็นไปไม่ได้เลยไม่ว่าจะเลือก $\\theta$ ใด · '
        'วิธีกันคือวาดแกนสองเส้นลงมุมกระดาษแล้วชี้ว่าเส้นไหนคือแกน $X$ ก่อนตั้งสมการทุกครั้ง',
        '• อีกเส้นทางที่พลาดกันบ่อยคือหยุดกลางทางแล้วตอบของที่ยังไม่เสร็จ เช่นตอบ $-\\dfrac{5}{13}$ '
        'ซึ่งเป็นเพียงค่าของ $\\cos\\theta$ หรือตอบ $-5$ เพราะแทนค่าแล้วได้ $13\\cos\\theta = -5$ '
        'พอดี จึงเผลอวงคำตอบตรงนั้นโดยลืมลบอีก $5$ ตามสูตรพิกัด · ค่า $-5$ ผิดและตรวจจับได้ทันทีด้วยการแทนกลับ : '
        'ถ้าพิกัดที่หนึ่งเป็น $-5$ จะต้องมี $13\\cos\\theta = 0$ ⇒ $\\cos\\theta = 0$ '
        '⇒ $\\tan\\theta$ ไม่นิยาม เพราะตัวส่วนเป็นศูนย์ ⇒ เงื่อนไข $\\tan\\theta > 0$ ใช้ไม่ได้เลย '
        '⇒ ขัดโจทย์ทันที · วิธีกันคือกลับไปอ่านบรรทัดสุดท้ายของโจทย์อีกครั้งก่อนวงคำตอบเสมอ '
        'ว่าสิ่งที่ถามคือพิกัด ไม่ใช่ค่าตรีโกณมิติ',
    ],
    'V.mold: G = G-PARAM-POINT-ON-AXIS-WITH-SIGN-CONDITION, a point P whose two coordinates are the affine '
    'images 13*cos(th) - 5 and 13*sin(th) + 12 of one unknown angle th running over a single turn, pinned '
    'down by one geometric statement, that P sits on the X axis, and one sign statement, that tan(th) is '
    'positive / A = A-COORDINATE-VALUE, the first coordinate of P / '
    'M = M-AXIS-ZERO-THEN-QUADRANT-PICK, read the axis statement as second coordinate equal to zero so that '
    'sin(th) = -12/13 falls out of the second slot alone, observe that this leaves two candidate angles in '
    '[0, 2*pi), one in the third and one in the fourth quadrant, spend the sign statement on demanding that '
    'sine and cosine carry the same sign so that only the third quadrant survives, fix cos(th) = -5/13 with '
    'the 5-12-13 reference triangle where the magnitude comes from the Pythagorean identity and the sign '
    'comes from the surviving quadrant, and only then substitute into the first slot. '
    'Rubric F2 C1 P2 T2 L0 = 7/15, with tot >= 3 and T <= 2 -> level: ปานกลาง. '
    'F = 2 because two formula blocks carry the item, the unit-circle definition of sine and cosine as the '
    'coordinates of the arc endpoint together with the Pythagorean identity, and the quotient identity for '
    'tangent used purely as a sign test; F was not raised to 3 because no third theorem is needed anywhere, '
    'no sum or difference formula, no double angle, no law of sines or cosines. C = 1 because exactly one '
    'idea is imported from outside subtopic 7.2, the coordinate-plane fact that lying on the X axis forces '
    'the second coordinate to vanish, and once that translation is done the whole item lives inside the '
    'unit circle, so the chain is one link long and not two. P = 2 for five short stages of different '
    'kinds: translate the axis statement into an equation, isolate sin(th), count the candidates in one '
    'turn, apply the sign test, extract cos(th) with its sign and substitute back; P was not raised to 3 '
    'because every stage is a single line of arithmetic with no expansion, no quadratic and no system to '
    'solve. T = 2 for two hidden conditions: which of the two coordinates the axis statement actually '
    'kills, since the letter X in the phrase points at the coordinate that is not the one set to zero, and '
    'the sign of the cosine, which the identity can never supply because the square root is two-valued and '
    'which only the tangent condition can decide. T was not raised to 3 because both traps are settled by '
    'one sign table, there is no case split to carry forward, no extraneous root to discard and no second '
    'admissible angle to compare. L = 0 because the item is symbolic from start to finish, no figure has to '
    'be drawn and no real-world scene has to be modelled, the quadrant work being done on signs rather than '
    'on a sketch. The total stops at 7, one short of the tot >= 8 gate for ยาก, so that gate cannot open '
    'even though T = 2, and the item falls to the tot >= 3 with T <= 2 gate instead. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): solveset of 13*sin(th) + 12 = 0 over Interval.Ropen(0, 2*pi) returns exactly '
    'two angles, and filtering them on tan(th) > 0 leaves exactly one, which is the machine proof both that '
    'the item has a single admissible angle and is therefore not ambiguous, and that the discarded branch '
    'is discarded by the sign condition rather than by the interval. On the surviving branch 13*cos(th) - 5 '
    'evaluates to -10. Every wrong value on offer was machine-computed from a named error path instead of '
    'being invented: -17 is 13*Rational(-12, 13) - 5, the value obtained when the reference triangle is '
    'read with 12 assigned to the cosine, and it fails the axis condition because the sine would then be '
    'plus or minus 5/13 and 13*sin(th) + 12 would be 17 or 7, never 0; 0 is 13*Rational(5, 13) - 5, the '
    'fourth-quadrant branch that survives only when the tangent condition is dropped, and it fails that '
    'condition since tan(th) = (-12/13)/(5/13) = -12/5 < 0; 24 comes from reading the axis condition off '
    'the wrong slot, that is solving 13*cos(th) - 5 = 0 for cos(th) = 5/13, keeping the branch with '
    'sin(th) = 12/13 that does satisfy tan(th) > 0 and then reporting 13*sin(th) + 12 = 24, and the machine '
    'confirms both that this number is the second coordinate and that it lies outside the interval [-18, 8] '
    'which is the full range of 13*cos(th) - 5. The independent check was machine-verified as well: '
    '13*(-12/13) + 12 = 0, tan(th) = 12/5 > 0, (12/13)**2 + (5/13)**2 = 1, and the distance from (-10, 0) '
    'to the centre (-5, 12) of the circle traced by P is sqrt(25 + 144) = 13 exactly. '
    'Collision sweep on 6457 items (bank 63 files + k1 out + k2 out), probe collide_b21.py / '
    'collide_b21b.py: the Thai phrase for lying on an axis returns 22 questions and every single one of '
    'them sits in chapters 4, 5 or 13, that is analytic geometry, functions and calculus, with rhombi, '
    'circles, parabolas and rectangles rather than angles; pairing that phrase with sine or cosine inside '
    'the same question returns 0 items, so no item in the corpus has ever turned an axis condition into a '
    'trigonometric equation, which is the whole mechanism here. The words for first coordinate and second '
    'coordinate return 0 items. A tangent sign condition inside a question returns 2 items: '
    'gen-chap-07-trigonometry-q137, the nearest relative in the corpus, which hands the magnitude of the '
    'cosine over directly as 20/29 together with a product sign condition and asks for 29*(sin - cos), and '
    'gen-chap-07-trigonometry-q045, which supplies two product sign conditions and asks only which quadrant '
    'the arc endpoint lies in. Both part company at G, because neither hides the trigonometric value inside '
    'a coordinate expression that has to be decoded first, and both part company at A, because neither asks '
    'for a coordinate; q045 parts company at M as well since it never touches the Pythagorean identity. The '
    '5-12-13 numeric surface returns 4 items, the closest being gen-chap-07-trigonometry-q008, which does '
    'place the arc endpoint at (-5/13, -12/13) in the third quadrant exactly as this item does, but hands '
    'that point over ready-made and asks for the cofunction image at pi/2 - th, so it shares the numbers '
    'and nothing else. Choices are ordered ascending by numeric value (-17, then -10, then 0, then 24), so '
    'the answer slot is forced by that rule and was not chosen.',
)

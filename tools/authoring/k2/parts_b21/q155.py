# -*- coding: utf-8 -*-
add_fill(
    155,
    ['7.2'],
    'ง่าย',
    'บนวงกลมหนึ่งหน่วยที่มีจุดศูนย์กลางอยู่ที่จุดกำเนิด ให้ $A$ เป็นจุดปลายส่วนโค้งของ $\\alpha$ '
    'และ $B$ เป็นจุดปลายส่วนโค้งของ $\\beta$ โดยวัดส่วนโค้งจากจุด $(1, 0)$ '
    'ถ้า $\\alpha + \\beta = \\pi$ และจุด $A$ คือจุด '
    '$\\left(-\\dfrac{8}{17},\\ \\dfrac{15}{17}\\right)$ '
    'แล้วผลคูณของพิกัดที่หนึ่งของจุด $A$ กับพิกัดที่หนึ่งของจุด $B$ เท่ากับเท่าใด',
    '-64/289',
    ['-64/289', '-\\dfrac{64}{289}'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• นิยามของจุดปลายส่วนโค้ง : วงกลมหนึ่งหน่วยคือวงกลมที่มีรัศมียาว $1$ หน่วย '
        'และมีจุดศูนย์กลางอยู่ที่จุดกำเนิด · ถ้าวัดส่วนโค้งจากจุด $(1, 0)$ ไปตามเส้นรอบวง '
        'เป็นระยะ $\\theta$ หน่วย (ทวนเข็มนาฬิกาเมื่อ $\\theta$ เป็นบวก) '
        'จุดปลายที่ได้คือจุด $(\\cos\\theta,\\ \\sin\\theta)$ เสมอ '
        '⇒ พิกัดที่หนึ่งของจุดปลายส่วนโค้งคือค่า $\\cos$ และพิกัดที่สองคือค่า $\\sin$ '
        'ของจำนวนนั้น · นี่ไม่ใช่สูตรที่ต้องท่อง แต่เป็น<b>นิยาม</b>ของ $\\sin$ กับ $\\cos$ '
        'สำหรับจำนวนจริงทุกจำนวน ⇒ เห็นจุดปลายส่วนโค้งเมื่อไร ให้แปลงเป็นค่าตรีโกณได้ทันที',
        '• สมการของวงกลมหนึ่งหน่วย : ทุกจุด $(x,\\ y)$ บนวงกลมนี้อยู่ห่างจากจุดกำเนิดเท่ากับ $1$ '
        '⇒ สอดคล้องกับสมการ $x^{2} + y^{2} = 1$ · เมื่อแทน $x = \\cos\\theta$ และ '
        '$y = \\sin\\theta$ ก็จะได้เอกลักษณ์ $\\cos^{2}\\theta + \\sin^{2}\\theta = 1$ ออกมาเอง '
        '⇒ ใช้สมการนี้ตรวจได้ทันทีว่าคู่อันดับที่ยื่นมาเป็นจุดบนวงกลมหนึ่งหน่วยจริงหรือไม่',
        '• คู่มุมที่บวกกันได้ $\\pi$ คือการ<b>สะท้อนข้ามแกน $Y$</b> : '
        'ระยะโค้งจากจุด $(1, 0)$ ไปถึงจุด $(-1, 0)$ ในทิศทวนเข็มนาฬิกายาว $\\pi$ หน่วยพอดี '
        '· จุดปลายส่วนโค้งของ $\\alpha$ อยู่ห่างจากจุด $(1, 0)$ ไปข้างหน้าเป็นระยะโค้ง $\\alpha$ '
        'ส่วนจุดปลายส่วนโค้งของ $\\pi - \\alpha$ อยู่ห่างจากจุด $(-1, 0)$ '
        '<b>ย้อนกลับ</b>มาเป็นระยะโค้ง $\\alpha$ เท่ากันเป๊ะ '
        '⇒ สองจุดนี้อยู่สูงเท่ากันและห่างจากแกน $Y$ เท่ากันแต่คนละฝั่ง '
        '⇒ เป็นภาพสะท้อนของกันและกันข้ามแกน $Y$',
        '• การสะท้อนข้ามแกน $Y$ ทำอะไรกับพิกัด : ภาพสะท้อนของจุด $(x,\\ y)$ ข้ามแกน $Y$ '
        'คือจุด $(-x,\\ y)$ ⇒ <b>พิกัดที่หนึ่งกลับเครื่องหมาย ส่วนพิกัดที่สองคงเดิม</b> '
        '· แปลกลับเป็นสูตรมุมสัมพันธ์ได้ว่า $\\cos(\\pi - \\alpha) = -\\cos\\alpha$ '
        'และ $\\sin(\\pi - \\alpha) = \\sin\\alpha$ '
        '⛔ ห้ามสับสนกับการสลับบทบาทของ $\\sin$ กับ $\\cos$ '
        'เพราะการสลับบทบาทเกิดกับคู่มุมที่บวกกันได้ $\\dfrac{\\pi}{2}$ '
        'ซึ่งเป็นการสะท้อนข้ามเส้นตรง $y = x$ คนละภาพกันคนละสูตรกัน',
        '• การคูณเศษส่วนและเครื่องหมาย : $\\dfrac{a}{b} \\cdot \\dfrac{c}{d} = \\dfrac{ac}{bd}$ '
        'คือคูณเศษกับเศษและส่วนกับส่วน · จำนวนลบคูณจำนวนบวกได้จำนวนลบเสมอ '
        '⇒ ถ้ารู้ว่าตัวคูณสองตัวมีเครื่องหมายต่างกัน ก็รู้ล่วงหน้าได้เลยว่าคำตอบต้องติดลบ '
        'โดยยังไม่ต้องคูณตัวเลขจริง ๆ · ตัวเลขที่จะเจอในข้อนี้คือชุด $8$-$15$-$17$ '
        'ซึ่งตรวจได้ว่า $8^{2} + 15^{2} = 64 + 225 = 289 = 17^{2}$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• เวทีของโจทย์คือวงกลมหนึ่งหน่วยที่มีจุดศูนย์กลางอยู่ที่จุดกำเนิด '
        'และวัดส่วนโค้งจากจุด $(1, 0)$ ตามธรรมเนียมมาตรฐาน',
        '• จุด $A$ เป็นจุดปลายส่วนโค้งของ $\\alpha$ และจุด $B$ เป็นจุดปลายส่วนโค้งของ $\\beta$',
        '• ความสัมพันธ์ระหว่างสองจำนวนนี้ถูกมัดไว้ด้วยสมการเดียว คือ $\\alpha + \\beta = \\pi$',
        '• พิกัดของจุด $A$ ให้มาครบทั้งสองช่อง คือ '
        '$A\\left(-\\dfrac{8}{17},\\ \\dfrac{15}{17}\\right)$',
        '• สังเกตหน้าตาก่อนลงมือ : โจทย์<b>ไม่ได้บอก</b>ว่า $\\alpha$ มีขนาดเท่าใด '
        'และก็ไม่จำเป็นต้องรู้ด้วย เพราะ $\\alpha + \\beta = \\pi$ จัดรูปได้เป็น '
        '$\\beta = \\pi - \\alpha$ ซึ่งเป็นคู่มุมสัมพันธ์มาตรฐานที่อ่านพิกัดต่อได้ทันที '
        '⇒ ⛔ ห้ามเสียเวลาไล่หาว่า $\\alpha$ กางกี่เรเดียนหรือกี่องศา',
        '• สังเกตอีกอย่าง : สิ่งที่ถามคือผลคูณของ<b>พิกัดที่หนึ่ง</b>ของสองจุด '
        '⇒ ตัวที่ต้องใช้จริงมีแค่ช่องซ้ายของแต่ละคู่อันดับ ส่วนพิกัดที่สองเป็นข้อมูลประกอบ '
        'ที่จะเอาไว้ใช้ตอนตรวจคำตอบ',
        '• อ่านตำแหน่งของจุด $A$ ให้ออกตั้งแต่ต้น : พิกัดที่หนึ่งติดลบและพิกัดที่สองเป็นบวก '
        '⇒ จุด $A$ อยู่ในจตุภาคที่ $2$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาผลคูณของพิกัดที่หนึ่งของจุด $A$ กับพิกัดที่หนึ่งของจุด $B$ ออกมาเป็นจำนวนเดียว',
        '',
        '<b>【 อ่านพิกัดของจุด $A$ ให้กลายเป็นค่า $\\cos\\alpha$ กับ $\\sin\\alpha$ '
        'ตามนิยามของจุดปลายส่วนโค้ง '
        'จากนั้นจัดรูปเงื่อนไขให้เป็น $\\beta = \\pi - \\alpha$ '
        'ซึ่งเป็นมุมสัมพันธ์ที่ตรงกับการสะท้อนจุดข้ามแกน $Y$ '
        'จึงอ่านพิกัดที่หนึ่งของจุด $B$ ได้ทันทีด้วยการกลับเครื่องหมายของพิกัดที่หนึ่งของจุด $A$ '
        'แล้วปิดงานด้วยการคูณสองจำนวนนั้นเข้าด้วยกัน 】</b>',
        '',
        '<b>ขั้นที่ 1 · แปลพิกัดของจุด $A$ ให้เป็นค่าตรีโกณของ $\\alpha$</b>',
        '• นิยามที่ใช้ : จุดปลายส่วนโค้งของ $\\alpha$ คือจุด $(\\cos\\alpha,\\ \\sin\\alpha)$ '
        'เลือกใช้นิยามนี้เพราะเป็นสะพานเส้นเดียวที่เปลี่ยน “จุดบนวงกลม” ให้กลายเป็น “ค่าตรีโกณ”',
        '• ระบุสิ่งที่โจทย์ให้ : จุด $A$ คือจุด '
        '$\\left(-\\dfrac{8}{17},\\ \\dfrac{15}{17}\\right)$',
        '• จับคู่ทีละช่องตามตำแหน่ง : ช่องซ้ายตรงกับ $\\cos\\alpha$ และช่องขวาตรงกับ $\\sin\\alpha$ '
        '⇒ $\\cos\\alpha = -\\dfrac{8}{17}$ และ $\\sin\\alpha = \\dfrac{15}{17}$',
        '• 📌 อ่านความหมายให้ออก : $\\cos\\alpha$ ติดลบแต่ $\\sin\\alpha$ เป็นบวก '
        '⇒ จุด $A$ อยู่ในจตุภาคที่ $2$ ⇒ $\\alpha$ เป็นจำนวนที่วางตัวอยู่ระหว่าง '
        '$\\dfrac{\\pi}{2}$ กับ $\\pi$ (นับหนึ่งรอบแรก) '
        '⇒ ข้อมูลนี้จะเอาไว้ตรวจเครื่องหมายของคำตอบตอนท้าย',
        '',
        '<b>ขั้นที่ 2 · เปลี่ยน $\\beta$ ให้อยู่ในรูปของ $\\alpha$ แล้วอ่านพิกัดที่หนึ่งของจุด $B$</b>',
        '• จัดรูปเงื่อนไขที่โจทย์ให้ : จาก $\\alpha + \\beta = \\pi$ '
        'ย้าย $\\alpha$ ไปอีกข้างได้ $\\beta = \\pi - \\alpha$',
        '• สิ่งที่ต้องการคือพิกัดที่หนึ่งของจุด $B$ ซึ่งตามนิยามในขั้นที่ $1$ '
        'ก็คือ $\\cos\\beta = \\cos(\\pi - \\alpha)$',
        '• สูตรมุมสัมพันธ์ที่ใช้ : $\\cos(\\pi - \\alpha) = -\\cos\\alpha$ '
        '· เหตุผลเชิงรูปที่ทำให้สูตรนี้ไม่ต้องท่อง : จุดปลายส่วนโค้งของ $\\pi - \\alpha$ '
        'คือภาพสะท้อนของจุดปลายส่วนโค้งของ $\\alpha$ ข้ามแกน $Y$ '
        '⇒ พิกัดที่หนึ่งกลับเครื่องหมาย ส่วนพิกัดที่สองคงเดิม',
        '• ระบุตัวแปรก่อนแทนค่า : $\\cos\\alpha = -\\dfrac{8}{17}$ (ได้จากขั้นที่ $1$)',
        '• แทนค่า : $\\cos\\beta = -\\left(-\\dfrac{8}{17}\\right) = \\dfrac{8}{17}$ '
        '⇒ พิกัดที่หนึ่งของจุด $B$ เท่ากับ $\\dfrac{8}{17}$',
        '• ⛔ จุดที่ต้องตรวจก่อนเดินต่อ : $\\alpha$ อยู่ในจตุภาคที่ $2$ '
        '⇒ $\\beta = \\pi - \\alpha$ ต้องตกอยู่ในจตุภาคที่ $1$ ⇒ พิกัดที่หนึ่งของจุด $B$ '
        'ต้องเป็นจำนวนบวก · ค่าที่คำนวณได้คือ $\\dfrac{8}{17}$ ซึ่งเป็นบวกจริง ⇒ ผ่าน',
        '',
        '<b>ขั้นที่ 3 · คูณพิกัดที่หนึ่งของสองจุดเข้าด้วยกัน</b>',
        '• สิ่งที่ต้องคำนวณตามที่โจทย์ถาม : (พิกัดที่หนึ่งของจุด $A$) คูณกับ '
        '(พิกัดที่หนึ่งของจุด $B$) ซึ่งเขียนด้วยสัญลักษณ์ได้เป็น $\\cos\\alpha \\cdot \\cos\\beta$',
        '• ระบุตัวแปร : $\\cos\\alpha = -\\dfrac{8}{17}$ (ขั้นที่ $1$) และ '
        '$\\cos\\beta = \\dfrac{8}{17}$ (ขั้นที่ $2$)',
        '• แทนค่า : $\\cos\\alpha \\cdot \\cos\\beta = '
        '\\left(-\\dfrac{8}{17}\\right)\\left(\\dfrac{8}{17}\\right)$',
        '• ยุบโดยคูณเศษกับเศษและส่วนกับส่วน : '
        '$= -\\dfrac{8 \\times 8}{17 \\times 17} = -\\dfrac{64}{289}$ '
        '· เครื่องหมายเป็นลบเพราะจำนวนลบคูณจำนวนบวก ⛔ ห้ามทิ้งเครื่องหมายลบเด็ดขาด',
        '• ตรวจขนาดคร่าว ๆ ทันที : $-\\dfrac{64}{289} \\approx -0.2215$ '
        'ซึ่งมีขนาดไม่เกิน $1$ ตรงตามที่ควรเป็น เพราะพิกัดของจุดบนวงกลมหนึ่งหน่วย '
        'มีขนาดไม่เกิน $1$ ทั้งคู่ ผลคูณของสองจำนวนนั้นจึงมีขนาดไม่เกิน $1$ ด้วย '
        '· และเป็นจำนวนลบ ซึ่งตรงกับที่จุดสองจุดอยู่คนละฝั่งของแกน $Y$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · หาพิกัดของจุด $B$ ให้ครบทั้งสองช่อง '
        'แล้วตรวจด้วยสมการวงกลมหนึ่งหน่วยกับความสมมาตรของรูป แทนการเดินสูตรมุมสัมพันธ์ซ้ำรอบเดิม)</b>',
        '• ด่านที่หนึ่ง ตรวจว่าจุด $A$ ที่โจทย์ยื่นมาอยู่บนวงกลมหนึ่งหน่วยจริงหรือไม่ '
        'โดยแทนลงสมการ $x^{2} + y^{2} = 1$ : '
        '$\\left(-\\dfrac{8}{17}\\right)^{2} + \\left(\\dfrac{15}{17}\\right)^{2} = '
        '\\dfrac{64 + 225}{289} = \\dfrac{289}{289} = 1$ ✓ '
        '⇒ ข้อมูลที่โจทย์ให้สอดคล้องกันเอง และเป็นชุด $8$-$15$-$17$ ที่คุ้นตา',
        '• หาพิกัดที่สองของจุด $B$ ให้ครบ : $\\sin\\beta = \\sin(\\pi - \\alpha) = \\sin\\alpha '
        '= \\dfrac{15}{17}$ ⇒ รวมกับขั้นที่ $2$ จะได้จุด '
        '$B\\left(\\dfrac{8}{17},\\ \\dfrac{15}{17}\\right)$ ครบทั้งสองช่อง',
        '• ด่านที่สอง ตรวจว่าจุด $B$ ที่หาได้อยู่บนวงกลมหนึ่งหน่วยด้วยหรือไม่ : '
        '$\\left(\\dfrac{8}{17}\\right)^{2} + \\left(\\dfrac{15}{17}\\right)^{2} = '
        '\\dfrac{64 + 225}{289} = \\dfrac{289}{289} = 1$ ✓ '
        '⇒ ถ้าเผลอกลับเครื่องหมายผิดช่อง ด่านนี้จะยังผ่านก็จริง แต่ด่านที่สามข้างล่างจะจับได้',
        '• ด่านที่สาม ตรวจความสมมาตรของสองจุด : '
        '$A\\left(-\\dfrac{8}{17},\\ \\dfrac{15}{17}\\right)$ กับ '
        '$B\\left(\\dfrac{8}{17},\\ \\dfrac{15}{17}\\right)$ '
        'มีพิกัดที่สองเท่ากันเป๊ะ และพิกัดที่หนึ่งเป็นจำนวนตรงข้ามกัน '
        '⇒ สองจุดนี้เป็นภาพสะท้อนกันข้ามแกน $Y$ จริง ตรงกับที่คู่มุม $\\alpha$ กับ '
        '$\\pi - \\alpha$ ต้องเป็นทุกประการ ⇒ พิกัดที่หามาไม่ได้หลุดกรอบของรูป',
        '• ด่านที่สี่ ปิดท้ายด้วยตัวเลขล้วนโดยไม่แตะสูตรมุมสัมพันธ์เลย : '
        'จุด $A$ ที่ได้มาตรงกับ $\\alpha \\approx 118.07^{\\circ}$ '
        '⇒ $\\beta = 180^{\\circ} - 118.07^{\\circ} = 61.93^{\\circ}$ '
        '⇒ พิกัดที่หนึ่งของจุด $B$ คือ $\\cos 61.93^{\\circ} \\approx 0.4706$ '
        'ซึ่งก็คือ $\\dfrac{8}{17}$ นั่นเอง ⇒ ผลคูณ $\\approx (-0.4706)(0.4706) \\approx -0.2215$ '
        'ตรงกับ $-\\dfrac{64}{289} \\approx -0.2215$ ✓',
        '',
        '✅ <b>คำตอบ</b> ผลคูณของพิกัดที่หนึ่งของจุด $A$ กับพิกัดที่หนึ่งของจุด $B$ '
        'เท่ากับ $-\\dfrac{64}{289}$ ซึ่งเป็นผลคูณของพิกัดสองจำนวนบนวงกลมหนึ่งหน่วย '
        'จึงเป็นจำนวนล้วนที่ไม่มีหน่วย',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอคู่จำนวนที่บวกกันได้ $\\pi$ ให้แปลเป็น<b>ภาพ</b>ทันทีว่า “สะท้อนข้ามแกน $Y$” '
        '⇒ พิกัดที่หนึ่งกลับเครื่องหมาย พิกัดที่สองคงเดิม · '
        'จำสองประโยคนี้ประโยคเดียวแทนการท่องสูตรมุมสัมพันธ์ทีละบรรทัด '
        'แล้วจะไม่มีวันจำสลับกับคู่มุมแบบอื่นเลย',
        '• จำภาพของคู่มุมที่เหลือควบไปพร้อมกัน : จำนวนตรงข้าม $-\\alpha$ '
        'คือสะท้อนข้ามแกน $X$ ⇒ ได้จุด $(x,\\ -y)$ · $\\pi + \\alpha$ '
        'คือสะท้อนผ่านจุดกำเนิด ⇒ ได้จุด $(-x,\\ -y)$ · $\\dfrac{\\pi}{2} - \\alpha$ '
        'คือสะท้อนข้ามเส้นตรง $y = x$ ⇒ ได้จุด $(y,\\ x)$ ซึ่งเป็นที่มาของสูตรโคฟังก์ชัน '
        '⇒ ทั้งสี่ภาพนี้ครอบคลุมมุมสัมพันธ์ที่ออกสอบเกือบทั้งหมด',
        '• ก่อนเชื่อคู่อันดับที่โจทย์ยื่นมา ให้ยกกำลังสองสองช่องแล้วบวกกันดูก่อนว่าได้ $1$ หรือไม่ '
        '⇒ ใช้เวลาสองวินาที แต่จับได้ทั้งการอ่านโจทย์ผิดช่องและการคัดลอกตัวเลขผิด '
        'ก่อนที่จะเสียเวลาคำนวณต่อไปทั้งข้อ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\dfrac{64}{289}$ ซึ่งเป็นจำนวนบวก เพราะจำสูตรผิดเป็น '
        '$\\cos(\\pi - \\alpha) = +\\cos\\alpha$ จึงคิดว่าพิกัดที่หนึ่งของจุด $B$ '
        'เท่ากับ $-\\dfrac{8}{17}$ เหมือนจุด $A$ แล้วคูณจำนวนลบสองตัวได้ผลบวก · '
        'พิสูจน์ว่าผิดจริงโดยไม่ต้องคำนวณ : จุด $A$ อยู่ในจตุภาคที่ $2$ '
        'ดังนั้น $\\beta = \\pi - \\alpha$ ต้องอยู่ในจตุภาคที่ $1$ ซึ่งมีพิกัดที่หนึ่งเป็นบวกเสมอ '
        '⇒ ผลคูณของจำนวนลบกับจำนวนบวกต้องติดลบ ค่าที่เป็นบวกจึงเป็นไปไม่ได้ตั้งแต่ต้น · '
        'พิสูจน์อีกทาง : ถ้า $\\cos\\beta = \\cos\\alpha$ จริง จุด $B$ ก็ต้องทับจุด $A$ '
        'หรือไม่ก็เป็นภาพสะท้อนของจุด $A$ ข้ามแกน $X$ ซึ่งขัดกับความสมมาตรรอบแกน $Y$ '
        'ที่คู่มุมบวกกันได้ $\\pi$ บังคับไว้',
        '• ได้ค่า $-\\dfrac{120}{289}$ เพราะอ่านเงื่อนไขผิดเป็น '
        '$\\beta = \\dfrac{\\pi}{2} - \\alpha$ แล้วใช้สูตรโคฟังก์ชัน '
        '$\\cos\\left(\\dfrac{\\pi}{2} - \\alpha\\right) = \\sin\\alpha = \\dfrac{15}{17}$ '
        '⇒ คูณได้ $\\left(-\\dfrac{8}{17}\\right)\\left(\\dfrac{15}{17}\\right) '
        '= -\\dfrac{120}{289}$ · ที่ผิดเพราะโจทย์เขียนไว้ชัดว่า $\\alpha + \\beta = \\pi$ '
        'ไม่ใช่ $\\alpha + \\beta = \\dfrac{\\pi}{2}$ ⇒ เส้นทางนี้ตอบโจทย์คนละข้อ · '
        'ตรวจย้อนได้ทันที : ถ้าใช้ $\\beta = \\dfrac{\\pi}{2} - \\alpha$ '
        'ผลบวกของสองจำนวนจะกลายเป็น $\\dfrac{\\pi}{2}$ ไม่ใช่ $\\pi$ ตามที่โจทย์กำหนด · '
        'ต้นตอของความสับสนคือการจำว่า “มุมสัมพันธ์ต้องสลับ $\\sin$ กับ $\\cos$” '
        'ทั้งที่การสลับเกิดเฉพาะกับการสะท้อนข้ามเส้นตรง $y = x$ เท่านั้น '
        'ส่วนคู่ที่บวกกันได้ $\\pi$ เป็นการสะท้อนข้ามแกน $Y$ ซึ่ง<b>ไม่สลับช่อง</b>เลย',
        '• ได้ค่า $\\dfrac{225}{289}$ เพราะอ่านคำถามผิดเป็นผลคูณของพิกัดที่<b>สอง</b> '
        'จึงคูณ $\\sin\\alpha \\cdot \\sin\\beta = '
        '\\left(\\dfrac{15}{17}\\right)\\left(\\dfrac{15}{17}\\right) = \\dfrac{225}{289}$ · '
        'เส้นทางนี้คำนวณถูกทุกจังหวะ แต่ตอบคนละคำถามกับที่โจทย์ถาม · '
        'จับผิดได้จากเครื่องหมายทันที : จุดทั้งสองอยู่เหนือแกน $X$ ทั้งคู่ '
        'พิกัดที่สองจึงเป็นบวกทั้งคู่ ผลคูณย่อมเป็นบวก '
        'แต่จุดทั้งสองอยู่คนละฝั่งของแกน $Y$ ผลคูณของพิกัดที่หนึ่งจึงต้องติดลบ '
        '⇒ เห็นคำตอบเป็นบวกเมื่อไรแปลว่าหยิบผิดช่องแน่นอน · '
        'วิธีกันพลาดคือขีดเส้นใต้คำว่า “พิกัดที่หนึ่ง” ในโจทย์ก่อนลงมือคำนวณ',
        '• ได้ค่า $\\dfrac{8}{17}$ เพราะหยุดที่ขั้นที่ $2$ '
        'คือหาพิกัดที่หนึ่งของจุด $B$ ได้แล้วรีบตอบ โดยลืมว่าโจทย์ถามหา<b>ผลคูณ</b> '
        'ของพิกัดที่หนึ่งของสองจุด ไม่ได้ถามพิกัดของจุด $B$ เฉย ๆ · '
        'ค่านี้ผิดชัดเจนเพราะเป็นจำนวนบวก ทั้งที่คำตอบจริงต้องติดลบตามเหตุผลเรื่องคนละฝั่งของแกน $Y$ '
        '· วิธีกันพลาดคือกลับไปอ่านประโยคคำถามอีกครั้งก่อนเขียนคำตอบลงกระดาษเสมอ '
        'ว่าคำนามตัวสุดท้ายที่โจทย์ถามคือคำว่าอะไร',
    ],
    'V.mold: G = the unit circle centred at the origin with arcs measured from the point (1, 0), two arc '
    'endpoints A and B belonging to alpha and to beta, one single relation tying the two numbers together, '
    'alpha + beta = pi, and the full coordinate pair of A handed over outright as (-8/17, 15/17), with the '
    'size of alpha itself never disclosed / A = the product of the first coordinate of A and the first '
    'coordinate of B, asked as a free numeric response with no candidate values printed anywhere on the '
    'page / M = read the pair of A as (cos alpha, sin alpha) straight from the definition of an arc '
    'endpoint, rewrite the relation as beta = pi - alpha, recognise that supplementary arcs land on points '
    'that are mirror images across the Y axis so that the first coordinate flips sign while the second one '
    'is untouched, take the first coordinate of B as 8/17, and multiply the two first coordinates to close. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 -> level: ง่าย. '
    'F = 1 because a single trigonometric fact is in play, the supplementary reduction cos(pi - x) = '
    '-cos(x); the statement that an arc endpoint is (cos, sin) is the definition the subtopic is built on '
    'rather than a second formula to recall, and the fraction multiplication that finishes the item is '
    'ordinary arithmetic. C = 0 because everything stays inside subtopic 7.2 and no result from any other '
    'subtopic is imported, so there is no second key to be joined to the first. P = 1 because the work '
    'occupies one arena only: one sign flip and one multiplication of two fractions, with no intermediate '
    'quantity that has to be carried anywhere, which follows the q145 baseline where a closing one-line '
    'computation does not buy a second point. T = 0 because nothing is hidden and nothing has to be '
    'rejected: the relation alpha + beta = pi is stated outright, both coordinates of A are printed with '
    'their signs so no quadrant has to be deduced before the work can start, beta is determined uniquely '
    'by alpha so no branch splits, and the sign change is part of the one formula being applied rather '
    'than a separate trap laid in the wording. L = 0 because the item is symbolic in the sense of the L '
    'baseline: the coordinate pair can be substituted on sight and no figure has to be drawn before the '
    'work can begin, since the circle carries no auxiliary construction at all. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): the q155 block sets ca = Rational(-8,17) and sa = Rational(15,17), recovers '
    'alpha as atan2(sa, ca) rather than assuming a quadrant, and sets be = pi - al so that the relation '
    'alpha + beta = pi holds by construction instead of by assertion. Four separate checks were then run '
    'by machine: ca**2 + sa**2 simplifies to 1, so the given point really does sit on the unit circle and '
    'the datum is self-consistent; cos(be) simplifies to Rational(8,17) exactly, confirming the sign flip; '
    'ca*cos(be) simplifies to Rational(-64,289); and the stored key string -64/289 was parsed as a '
    'rational and compared against that value rather than eyeballed. Every wrong road printed in the '
    'pitfalls block was computed by machine and not invented: dropping the sign gives ca*ca = 64/289, '
    'mistaking the relation for a complementary one and applying the cofunction gives ca*sa = -120/289, '
    'reading the question as the product of the second coordinates gives sa*sa = 225/289, and stopping at '
    'the first coordinate of B gives 8/17. The numeric closing check was machine-evaluated too: alpha is '
    '118.0724869... degrees and beta is 61.9275130... degrees, their sum is pi to full working precision, '
    'cos(beta) is 0.470588..., and the product is -0.221453..., which agrees with -64/289 to every digit '
    'printed. The symmetry claim was verified as an identity rather than by picture, since ca + cos(be) '
    'evaluates to 0 while sa - sin(be) evaluates to 0, which is exactly what a reflection across the Y '
    'axis means. '
    'Collision sweep on 6457 items (bank 63 files + k1 out + k2 out), probes run as regular expressions '
    'over the question text only so that the first gate never reads an explanation: the phrase for arc '
    'endpoint returns 11 items and the phrase for unit circle returns 19, but the pair (arc endpoint) '
    'crossed with (product) returns 0 items, the pair (unit circle) crossed with (product) returns 0 '
    'items, and the phrase for first coordinate returns 0 items in the whole corpus, so nothing in the '
    'bank asks for a product of coordinates at all. The literal answer value 64/289 appears in no '
    'question. The nearest neighbour by surface is gen-chap-07-trigonometry-q021, which also hands over an '
    'arc endpoint as an explicit pair, there (-3/5, 4/5), but it asks for the value of a sum of two '
    'trigonometric expressions, sin(theta + pi) + cos(-theta), so its A is a sum of ratios and its M mixes '
    'the half-turn reflection through the origin with the reflection across the X axis, neither of which '
    'is the Y axis reflection this item turns on. The pattern for a stated relation of the form alpha + '
    'beta returns 5 items, namely chap-03-realnumber-q30, chap-07-trigonometry-q37, chap-07-'
    'trigonometry-q56, chap-07-trigonometry-q182 and samn-2556-01-q16, and every one of them lives in the '
    'sum and difference formulas or in the solving of equations, with no unit circle point anywhere in '
    'sight, so the shared token is a false positive at the level of mechanism. The remaining arc endpoint '
    'items ask for a quadrant, for a parameter count or for a coordinate of a single point, so their A '
    'never involves two points at once. Since this is a fill item there is no choice list, so no answer '
    'slot exists and nothing about the answer could have been positioned by hand.',
)

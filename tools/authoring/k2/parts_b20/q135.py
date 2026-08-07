# -*- coding: utf-8 -*-
add(
    135,
    ['7.2'],
    'ง่าย',
    'บนวงกลมหนึ่งหน่วยที่มีจุดศูนย์กลางอยู่ที่จุดกำเนิด ให้จุด $A$ คือจุด $(0, -1)$ '
    'เมื่อเคลื่อนที่จากจุด $A$ ไปตามเส้นรอบวงในทิศทวนเข็มนาฬิกาเป็นระยะทาง $\\dfrac{\\pi}{3}$ หน่วย '
    'จะได้จุดปลายคือจุด $P(a, b)$ แล้วค่าของ $a + b$ เท่ากับข้อใดต่อไปนี้',
    [
        '$-\\dfrac{\\sqrt{3}+1}{2}$',
        '$\\dfrac{1-\\sqrt{3}}{2}$',
        '$\\dfrac{\\sqrt{3}-1}{2}$',
        '$\\dfrac{\\sqrt{3}+1}{2}$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• <b>วงกลมหนึ่งหน่วย</b> คือวงกลมที่มีจุดศูนย์กลางอยู่ที่จุดกำเนิดและมีรัศมียาว $1$ หน่วย '
        'สมการของวงกลมนี้คือ $x^2 + y^2 = 1$ · ทุกจุดบนวงกลมนี้เขียนได้ในรูป '
        '$(\\cos\\theta , \\sin\\theta)$ เมื่อ $\\theta$ คือขนาดของมุมที่วัดจากแกน $x$ ด้านบวก '
        'เหตุผลคือ ในสามเหลี่ยมมุมฉากที่มีด้านตรงข้ามมุมฉากยาว $1$ ด้านประชิดจะยาว $\\cos\\theta$ '
        'และด้านตรงข้ามจะยาว $\\sin\\theta$ พอดี ⇒ พิกัดของจุดจึงเป็นค่าตรีโกณทั้งคู่',
        '• <b>ระยะทางตามส่วนโค้งกับขนาดของมุม</b> : สูตรความยาวส่วนโค้งคือ $s = r\\theta$ '
        'เมื่อ $s$ คือความยาวส่วนโค้ง $r$ คือรัศมี และ $\\theta$ คือขนาดของมุมที่จุดศูนย์กลาง '
        'หน่วยเรเดียน ⇒ จัดรูปได้เป็น $\\theta = \\dfrac{s}{r}$ · ⭐ บนวงกลม<b>หนึ่งหน่วย</b> '
        'รัศมีเป็น $1$ ⇒ $\\theta = \\dfrac{s}{1} = s$ นั่นคือ '
        '<b>ระยะทางที่เดินไปตามเส้นรอบวงเท่ากับขนาดของมุมเป็นเรเดียนพอดี</b> ตัวเลขเดียวกันเป๊ะ',
        '• <b>จุดสำคัญสี่จุดบนวงกลมหนึ่งหน่วย</b> ที่ต้องจำให้แม่น : มุม $0$ คู่กับจุด $(1, 0)$ '
        'ทางขวาสุด · มุม $\\dfrac{\\pi}{2}$ คู่กับจุด $(0, 1)$ บนสุด · มุม $\\pi$ คู่กับจุด $(-1, 0)$ '
        'ซ้ายสุด · มุม $\\dfrac{3\\pi}{2}$ คู่กับจุด $(0, -1)$ ล่างสุด '
        '⇒ จุดที่พิกัด $y$ เป็น $-1$ คือมุม $\\dfrac{3\\pi}{2}$ ⛔ ไม่ใช่ $\\dfrac{\\pi}{2}$',
        '• <b>ทิศทางของการเคลื่อนที่</b> : เดินทวนเข็มนาฬิกา ⇒ ขนาดของมุม<b>เพิ่มขึ้น</b> '
        'จึงนำระยะที่เดินไป<b>บวก</b>เข้ากับมุมเริ่มต้น · เดินตามเข็มนาฬิกา ⇒ ขนาดของมุม<b>ลดลง</b> '
        'จึงต้องนำไป<b>ลบ</b> ⇒ เครื่องหมายบวกหรือลบถูกกำหนดโดยคำบอกทิศในโจทย์เท่านั้น',
        '• <b>มุมอ้างอิงกับเครื่องหมายตามจตุภาค</b> : มุมอ้างอิงคือมุมแหลมที่วัดจากแกน $x$ '
        'ไปหาด้านสิ้นสุดของมุมนั้น ใช้หาขนาดของ $\\cos$ กับ $\\sin$ ส่วนเครื่องหมายดูจากจตุภาค '
        'เพราะ $\\cos$ คือพิกัด $x$ และ $\\sin$ คือพิกัด $y$ ⇒ จตุภาคที่ $1$ บวกทั้งคู่ · '
        'จตุภาคที่ $2$ มี $\\cos$ เป็นลบ · จตุภาคที่ $3$ ลบทั้งคู่ · '
        'จตุภาคที่ $4$ มี $\\cos$ เป็นบวกและ $\\sin$ เป็นลบ',
        '• <b>ค่าตรีโกณของมุมพิเศษ</b> ที่ข้อนี้ต้องใช้ : $\\cos\\dfrac{\\pi}{6} = \\dfrac{\\sqrt{3}}{2}$ '
        'และ $\\sin\\dfrac{\\pi}{6} = \\dfrac{1}{2}$ ค่าคู่นี้อ่านได้จากสามเหลี่ยมมุมฉากที่มีมุม '
        '$30^{\\circ}$-$60^{\\circ}$-$90^{\\circ}$ ซึ่งมีด้านยาวเป็นอัตราส่วน $1 : \\sqrt{3} : 2$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• วงกลมหนึ่งหน่วยที่มีจุดศูนย์กลางอยู่ที่จุดกำเนิด ⇒ รัศมียาว $1$ หน่วย',
        '• จุดเริ่มต้นคือจุด $A$ ซึ่งมีพิกัด $(0, -1)$ นั่นคือจุดล่างสุดของวงกลม',
        '• เคลื่อนที่ไปตามเส้นรอบวงในทิศ<b>ทวนเข็มนาฬิกา</b> เป็นระยะทาง $\\dfrac{\\pi}{3}$ หน่วย',
        '• จุดที่ไปหยุดเรียกว่าจุด $P(a, b)$ โดย $a$ คือพิกัด $x$ และ $b$ คือพิกัด $y$ ของจุดปลาย',
        '• สังเกตหน้าตาก่อนลงมือ : จุดเริ่มต้นของข้อนี้ <b>ไม่ใช่</b>จุด $(1, 0)$ ที่คุ้นเคย '
        'แต่เป็นจุด $(0, -1)$ ⇒ งานด่านแรกคือแปลงจุดเริ่มต้นให้กลายเป็น<b>ขนาดของมุม</b>เสียก่อน '
        'แล้วค่อยบวกระยะที่เดินไป ⛔ ห้ามเผลอเดินจากมุม $0$ ตามความเคยชิน',
        '• สังเกตอีกอย่าง : โจทย์ให้ระยะทางมาเป็น $\\dfrac{\\pi}{3}$ ซึ่งมี $\\pi$ ติดมาด้วย '
        'นี่คือสัญญาณว่าจะทำงานกันในหน่วยเรเดียนตลอดทั้งข้อ ⇒ ไม่ต้องแปลงเป็นองศาให้เสียเวลา',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $a + b$ นั่นคือผลบวกของพิกัดทั้งสองของจุดปลาย $P$',
        '',
        '<b>【 เปลี่ยนจุดเริ่มต้น $(0, -1)$ ให้กลายเป็นขนาดของมุมก่อน จากนั้นเปลี่ยนระยะทางตามส่วนโค้ง '
        'ให้เป็นขนาดของมุมด้วยสูตร $\\theta = \\dfrac{s}{r}$ แล้วบวกกันตามทิศทวนเข็ม '
        'สุดท้ายอ่านพิกัดของมุมปลายด้วยมุมอ้างอิงและเครื่องหมายของจตุภาค แล้วจึงบวกพิกัดทั้งสอง 】</b>',
        '',
        '<b>ขั้นที่ 1 · เปลี่ยนจุดเริ่มต้น $A(0, -1)$ ให้กลายเป็นขนาดของมุม</b>',
        '• สูตรที่ใช้ : จุดบนวงกลมหนึ่งหน่วยที่คู่กับมุม $\\theta$ คือ $(\\cos\\theta , \\sin\\theta)$',
        '• ระบุตัวแปรให้ชัดก่อนแทนค่า : ต้องการมุม $\\theta_A$ ที่ทำให้ $\\cos\\theta_A = 0$ '
        'และ $\\sin\\theta_A = -1$ พร้อมกัน เพราะพิกัด $x$ ของจุด $A$ เป็น $0$ '
        'และพิกัด $y$ ของจุด $A$ เป็น $-1$',
        '• แทนค่าเงื่อนไขแรก : $\\cos\\theta_A = 0$ ⇒ ภายในหนึ่งรอบจะได้ $\\theta_A = \\dfrac{\\pi}{2}$ '
        'หรือ $\\theta_A = \\dfrac{3\\pi}{2}$ เพราะมีเพียงสองจุดบนวงกลมที่พิกัด $x$ เป็นศูนย์ '
        'คือจุดบนสุดกับจุดล่างสุด',
        '• ยุบด้วยเงื่อนไขที่สอง : $\\sin\\dfrac{\\pi}{2} = 1$ ซึ่งไม่ใช่ $-1$ จึงตัดทิ้ง '
        'เหลือ $\\sin\\dfrac{3\\pi}{2} = -1$ ✓ ⇒ $\\theta_A = \\dfrac{3\\pi}{2}$',
        '• ⛔ <b>จุดพลิกของข้อนี้อยู่ตรงนี้</b> : จุด $(0, -1)$ ตรงกับมุม $\\dfrac{3\\pi}{2}$ '
        'ไม่ใช่ $\\dfrac{\\pi}{2}$ · มุม $\\dfrac{\\pi}{2}$ คู่กับจุด $(0, 1)$ ซึ่งอยู่<b>บนสุด</b> '
        'ของวงกลม คนละจุดกับที่โจทย์ให้มาซึ่งอยู่<b>ล่างสุด</b> ⇒ ตรวจเครื่องหมายของพิกัด $y$ '
        'ให้ดีทุกครั้งก่อนเขียนมุมลงกระดาษ',
        '',
        '<b>ขั้นที่ 2 · เปลี่ยนระยะทางตามส่วนโค้งให้กลายเป็นขนาดของมุมที่กวาดไป</b>',
        '• สูตรที่ใช้ : $s = r\\theta$ ⇒ จัดรูปโดยหารทั้งสองข้างด้วย $r$ ได้ '
        '$\\theta = \\dfrac{s}{r}$ หารได้เพราะรัศมีเป็นจำนวนบวกเสมอ',
        '• ระบุตัวแปร : $s = \\dfrac{\\pi}{3}$ หน่วย คือระยะทางที่โจทย์ให้มา · $r = 1$ หน่วย '
        'เพราะเป็นวงกลมหนึ่งหน่วย · $\\theta$ คือขนาดของมุมที่กวาดไปซึ่งกำลังหา',
        '• แทนค่า : $\\theta = \\dfrac{\\pi/3}{1}$',
        '• ยุบ : การหารด้วย $1$ ไม่เปลี่ยนค่า ⇒ $\\theta = \\dfrac{\\pi}{3}$ เรเดียน',
        '• อ่านความหมายให้ชัด : เลข $\\dfrac{\\pi}{3}$ ตัวเดียวกันทำหน้าที่สองอย่างในข้อนี้ '
        'คือเป็นทั้ง<b>ความยาว</b>ของส่วนโค้งและ<b>ขนาดของมุม</b>เป็นเรเดียน '
        'ที่เป็นแบบนี้ได้เพราะรัศมีเป็น $1$ พอดี ⛔ ถ้ารัศมีไม่ใช่ $1$ จะใช้แทนกันตรง ๆ ไม่ได้',
        '',
        '<b>ขั้นที่ 3 · รวมมุมเริ่มต้นกับมุมที่กวาดไป ให้ได้มุมของจุดปลาย</b>',
        '• สูตรที่ใช้ : เคลื่อนที่ทวนเข็มนาฬิกา ⇒ มุมเพิ่มขึ้น ⇒ '
        'มุมปลาย $=$ มุมเริ่มต้น $+$ มุมที่กวาดไป',
        '• ระบุตัวแปร : มุมเริ่มต้น $= \\dfrac{3\\pi}{2}$ จากขั้นที่ 1 · '
        'มุมที่กวาดไป $= \\dfrac{\\pi}{3}$ จากขั้นที่ 2 · ทิศเป็นทวนเข็มนาฬิกาตามที่โจทย์ระบุ '
        'จึงใช้เครื่องหมายบวก',
        '• แทนค่า : มุมปลาย $= \\dfrac{3\\pi}{2} + \\dfrac{\\pi}{3}$',
        '• ยุบ : ทำส่วนให้เท่ากันด้วย ค.ร.น. ของ $2$ กับ $3$ ซึ่งคือ $6$ ⇒ '
        '$\\dfrac{3\\pi}{2} = \\dfrac{9\\pi}{6}$ และ $\\dfrac{\\pi}{3} = \\dfrac{2\\pi}{6}$ '
        '⇒ มุมปลาย $= \\dfrac{9\\pi}{6} + \\dfrac{2\\pi}{6} = \\dfrac{11\\pi}{6}$',
        '• ตรวจว่ายังไม่ครบรอบ : หนึ่งรอบเต็มคือ $2\\pi = \\dfrac{12\\pi}{6}$ '
        'และ $\\dfrac{11\\pi}{6} < \\dfrac{12\\pi}{6}$ ⇒ ยังเดินไม่ครบรอบ '
        'จึงไม่ต้องลบ $2\\pi$ ออกเพื่อทอนให้อยู่ในหนึ่งรอบ',
        '',
        '<b>ขั้นที่ 4 · อ่านพิกัดของจุดปลายจากมุม $\\dfrac{11\\pi}{6}$ แล้วบวกกัน</b>',
        '• หาจตุภาคก่อน : $\\dfrac{3\\pi}{2} = \\dfrac{9\\pi}{6}$ และ $2\\pi = \\dfrac{12\\pi}{6}$ '
        '⇒ $\\dfrac{9\\pi}{6} < \\dfrac{11\\pi}{6} < \\dfrac{12\\pi}{6}$ '
        '⇒ ด้านสิ้นสุดของมุมอยู่ใน<b>จตุภาคที่ 4</b>',
        '• หามุมอ้างอิง : มุมอยู่ในจตุภาคที่ 4 จึงวัดย้อนกลับไปหาแกน $x$ ด้านบวก ⇒ '
        'มุมอ้างอิง $= 2\\pi - \\dfrac{11\\pi}{6} = \\dfrac{12\\pi}{6} - \\dfrac{11\\pi}{6} '
        '= \\dfrac{\\pi}{6}$',
        '• ใส่เครื่องหมายตามจตุภาคที่ 4 : พิกัด $x$ เป็นบวกและพิกัด $y$ เป็นลบ ⇒ '
        '$a = \\cos\\dfrac{11\\pi}{6} = +\\cos\\dfrac{\\pi}{6} = \\dfrac{\\sqrt{3}}{2}$ '
        'และ $b = \\sin\\dfrac{11\\pi}{6} = -\\sin\\dfrac{\\pi}{6} = -\\dfrac{1}{2}$',
        '• แทนค่าลงในสิ่งที่โจทย์ถาม : $a + b = \\dfrac{\\sqrt{3}}{2} + \\left(-\\dfrac{1}{2}\\right)$',
        '• ยุบ : ตัวส่วนเท่ากันอยู่แล้วคือ $2$ จึงรวมตัวเศษได้ทันที ⇒ '
        '$a + b = \\dfrac{\\sqrt{3} - 1}{2}$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนพิกัดลงสมการวงกลม $x^2 + y^2 = 1$ '
        'แล้วล้อมกรอบด้วยเครื่องหมายของจตุภาค)</b>',
        '• เส้นทางข้างบนเดินด้วยการบวกมุมแล้วเปิดตารางค่ามุมพิเศษ การตรวจรอบนี้จะไม่บวกมุมอีกเลย '
        'แต่จะถามว่าจุด $\\left(\\dfrac{\\sqrt{3}}{2} , -\\dfrac{1}{2}\\right)$ '
        'อยู่บนวงกลมหนึ่งหน่วยจริงหรือไม่ ซึ่งเป็นเงื่อนไขที่จุดปลายต้องผ่านแน่นอน '
        'เพราะโจทย์บังคับให้เดินไปตามเส้นรอบวง',
        '• แทนพิกัดลงสมการวงกลม : $\\left(\\dfrac{\\sqrt{3}}{2}\\right)^2 '
        '+ \\left(-\\dfrac{1}{2}\\right)^2 = \\dfrac{3}{4} + \\dfrac{1}{4} = \\dfrac{4}{4} = 1$ ✓ '
        'ผ่านสมการ $x^2 + y^2 = 1$ พอดี ⇒ จุดที่ได้อยู่บนวงกลมหนึ่งหน่วยจริง',
        '• ตรวจชั้นที่สองด้วย<b>จตุภาค</b> โดยไม่ใช้ตัวเลขเลย : เดินทวนเข็มนาฬิกาจากจุด $(0, -1)$ '
        'ซึ่งเป็นจุดล่างสุด ไปเป็นระยะ $\\dfrac{\\pi}{3}$ ซึ่ง<b>น้อยกว่า</b> $\\dfrac{\\pi}{2}$ '
        'อันเป็นความยาวส่วนโค้งจากจุดล่างสุดไปถึงจุด $(1, 0)$ ⇒ ยังเดินไปไม่ถึงจุด $(1, 0)$ '
        '⇒ จุดปลายต้องอยู่ใน<b>จตุภาคที่ 4</b> เท่านั้น',
        '• อยู่ในจตุภาคที่ 4 แปลว่า $a > 0$ และ $b < 0$ ⇒ พิกัดทั้งสองมีเครื่องหมายต่างกัน '
        '⇒ ค่าที่เกิดจากจุดซึ่งพิกัดเป็นลบทั้งคู่ และค่าที่เกิดจากจุดซึ่งพิกัดเป็นบวกทั้งคู่ '
        'ถูกตัดทิ้งได้ทันทีโดยไม่ต้องคำนวณ',
        '• 📌 ปิดท้ายด้วยค่าประมาณ : $\\sqrt{3} \\approx 1.732$ ⇒ '
        '$\\dfrac{\\sqrt{3} - 1}{2} \\approx \\dfrac{1.732 - 1}{2} \\approx 0.366$ '
        'ซึ่งเป็นบวกและมีขนาดเล็กกว่า $1$ ตรงกับที่ควรเป็น เพราะ $a$ กับ $b$ '
        'มีเครื่องหมายต่างกันจึงหักล้างกันบางส่วน ✓',
        '',
        '✅ <b>คำตอบ</b> จุดปลายคือจุด $P\\left(\\dfrac{\\sqrt{3}}{2} , -\\dfrac{1}{2}\\right)$ '
        'ดังนั้นค่าของ $a + b$ เท่ากับ $\\dfrac{\\sqrt{3} - 1}{2}$ → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• ท่องจุดสำคัญสี่จุดคู่กับมุมให้ขึ้นใจ — $(1, 0)$ คู่กับ $0$ · $(0, 1)$ คู่กับ '
        '$\\dfrac{\\pi}{2}$ · $(-1, 0)$ คู่กับ $\\pi$ · $(0, -1)$ คู่กับ $\\dfrac{3\\pi}{2}$ '
        'พอจำได้ โจทย์ที่ให้เริ่มเดินจากจุดแปลก ๆ จะเหลืองานแค่บวกลบเศษส่วนของ $\\pi$ เท่านั้น',
        '• ระยะทางตามส่วนโค้งเท่ากับขนาดของมุมได้เฉพาะบนวงกลม<b>หนึ่งหน่วย</b>เท่านั้น '
        'ถ้าโจทย์เปลี่ยนรัศมีเป็น $3$ แล้วให้เดินเป็นระยะ $\\dfrac{\\pi}{3}$ '
        'มุมที่กวาดไปจะเป็น $\\dfrac{\\pi/3}{3} = \\dfrac{\\pi}{9}$ ไม่ใช่ $\\dfrac{\\pi}{3}$ '
        '⇒ อ่านคำว่า “หนึ่งหน่วย” ให้เห็นก่อนใช้ทางลัดนี้ทุกครั้ง',
        '• ก่อนคำนวณค่าจริง ให้เดาจตุภาคของจุดปลายด้วยการนึกภาพก่อนเสมอ '
        'จะได้รู้เครื่องหมายของพิกัดล่วงหน้า แล้วใช้เครื่องหมายนั้นกวาดค่าที่เป็นไปไม่ได้ทิ้ง '
        'เหลือผู้เข้าชิงไม่กี่ตัว วิธีนี้เร็วกว่าการคำนวณครบทุกทางในห้องสอบมาก',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ถ้าได้ค่า $-\\dfrac{\\sqrt{3}+1}{2}$ แปลว่าวัดผิดทิศเป็น<b>ตามเข็ม</b>นาฬิกา '
        'จึงเอาไปลบแทนบวก ⇒ มุมปลายกลายเป็น $\\dfrac{3\\pi}{2} - \\dfrac{\\pi}{3} '
        '= \\dfrac{9\\pi}{6} - \\dfrac{2\\pi}{6} = \\dfrac{7\\pi}{6}$ ⇒ จุดปลายเป็น '
        '$\\left(-\\dfrac{\\sqrt{3}}{2} , -\\dfrac{1}{2}\\right)$ ⇒ ผลบวกเป็น '
        '$-\\dfrac{\\sqrt{3}+1}{2} \\approx -1.366$ · ค่านี้ผิดแน่นอนเพราะมุม $\\dfrac{7\\pi}{6}$ '
        'อยู่ในจตุภาคที่ 3 ซึ่งพิกัดเป็นลบทั้งคู่ แต่โจทย์บอกชัดว่าเดิน<b>ทวนเข็ม</b>นาฬิกา '
        'ซึ่งพาจุดจากล่างสุดวิ่งเข้าหาจุด $(1, 0)$ ทางขวา ไม่ใช่วิ่งไปทางซ้าย',
        '• ถ้าได้ค่า $\\dfrac{1-\\sqrt{3}}{2}$ แปลว่าวางจุดเริ่มต้นผิดเป็นจุด $(0, 1)$ '
        'เพราะสับสนบนกับล่าง ⇒ มุมปลายกลายเป็น $\\dfrac{\\pi}{2} + \\dfrac{\\pi}{3} '
        '= \\dfrac{5\\pi}{6}$ ⇒ จุดปลายเป็น $\\left(-\\dfrac{\\sqrt{3}}{2} , \\dfrac{1}{2}\\right)$ '
        '⇒ ผลบวกเป็น $\\dfrac{1-\\sqrt{3}}{2} \\approx -0.366$ · ค่านี้ผิดเพราะจุดเริ่มต้น '
        'ที่โจทย์ให้มีพิกัด $y$ เป็น $-1$ ไม่ใช่ $1$ ⇒ ตรวจจับได้ทันทีด้วยการอ่านเครื่องหมาย '
        'หน้าเลข $1$ ในพิกัดของจุด $A$ · สังเกตด้วยว่าค่านี้เป็นลบ ทั้งที่จุดปลายจริง '
        'มีพิกัด $x$ เป็นบวกและใหญ่กว่าขนาดของพิกัด $y$',
        '• ถ้าได้ค่า $\\dfrac{\\sqrt{3}+1}{2}$ แปลว่าเผลอวัดส่วนโค้งจากจุด $(1, 0)$ '
        'ตามความเคยชิน โดยไม่ได้ใช้จุด $A$ ที่โจทย์กำหนดเลย ⇒ มุมปลายกลายเป็น $\\dfrac{\\pi}{3}$ '
        '⇒ จุดปลายเป็น $\\left(\\dfrac{1}{2} , \\dfrac{\\sqrt{3}}{2}\\right)$ ⇒ ผลบวกเป็น '
        '$\\dfrac{\\sqrt{3}+1}{2} \\approx 1.366$ · ค่านี้ผิดเพราะจุดดังกล่าวอยู่ในจตุภาคที่ 1 '
        'ซึ่งพิกัดเป็นบวกทั้งคู่ แต่การเดินทวนเข็มนาฬิกาจากจุดล่างสุดเป็นระยะเพียง '
        '$\\dfrac{\\pi}{3}$ ซึ่งน้อยกว่า $\\dfrac{\\pi}{2}$ ยังไปไม่ถึงจุด $(1, 0)$ ด้วยซ้ำ '
        'จึงข้ามเข้าจตุภาคที่ 1 ไม่ได้เด็ดขาด',
        '• อีกเส้นทางที่พลาดกันบ่อยคือเอาระยะทาง $\\dfrac{\\pi}{3}$ ไปแปลงเป็น $60^{\\circ}$ '
        'แล้วบวกกับ $\\dfrac{3\\pi}{2}$ ทั้งที่ยังเป็นเรเดียน ⇒ ได้นิพจน์ที่หน่วยปนกัน '
        'ซึ่งไม่มีความหมายทางคณิตศาสตร์ · ให้เลือกหน่วยเดียวแล้วอยู่กับหน่วยนั้นจนจบข้อ '
        'ถ้าจะทำงานเป็นองศาก็ต้องเปลี่ยนมุมเริ่มต้นเป็น $270^{\\circ}$ ให้ครบคู่ '
        'แล้วจะได้ $270^{\\circ} + 60^{\\circ} = 330^{\\circ}$ ซึ่งก็คือ $\\dfrac{11\\pi}{6}$ '
        'ค่าเดียวกันกับที่ได้ในขั้นที่ 3',
        '• สุดท้าย ระวังการหยุดก่อนเส้นชัยด้วยการตอบพิกัดเพียงตัวเดียว เช่นตอบ $\\dfrac{\\sqrt{3}}{2}$ '
        'ซึ่งเป็นค่าของ $a$ อย่างเดียว หรือตอบ $-\\dfrac{1}{2}$ ซึ่งเป็นค่าของ $b$ อย่างเดียว · '
        'โจทย์ถามหา $a + b$ ⇒ ต้องบวกพิกัดทั้งสองเข้าด้วยกันก่อนเสมอ '
        'ให้กลับไปอ่านบรรทัดสุดท้ายของโจทย์อีกครั้งก่อนวงคำตอบทุกครั้ง',
    ],
    'V.mold: G = the unit circle centred at the origin, together with a starting point A that is '
    'deliberately not the customary (1, 0) but the bottom point (0, -1), an arc length of pi/3 measured '
    'along the circumference, and an explicit counterclockwise direction / A = the sum a + b of the two '
    'coordinates of the terminal point P, not either coordinate on its own / '
    'M = M-ARC-FROM-NONSTANDARD-START, that is, convert the given starting point into the angle 3*pi/2, '
    'convert the arc length into an angle through theta = s / r with r = 1 so the two numbers coincide, '
    'add because the motion is counterclockwise to reach 11*pi/6, then read the coordinates off the '
    'reference angle pi/6 with quadrant four signs and add them. '
    'Rubric F1 C0 P1 T0 L0 = 2/15, a total of 2 with T at most 1 and C equal to 0, which is exactly the '
    'band reserved for the easiest tier -> level: ง่าย. F = 1 because one body of knowledge carries the '
    'whole item, the coordinate description of the unit circle together with the special-angle values; '
    'the arc-length relation degenerates to an identity here because the radius is 1, so it adds no '
    'second formula in any real sense. C = 0 because only subtopic 7.2 is touched from the first line to '
    'the last: no identity is applied, no equation is solved, no triangle outside the unit circle is '
    'built, and no other subtopic is required at any point. P = 1 because the arithmetic chain is short '
    'and every stage is a single move: add two fractions of pi over the common denominator 6, then add '
    'two special values that already share the denominator 2. T = 0 because nothing has to be discovered '
    'or reinterpreted; the statement names the starting point by its coordinates and names the direction '
    'in words, so both the base angle and the sign of the increment are handed over rather than inferred, '
    'and the only thing that could trip a student is ordinary recall of which point carries 3*pi/2. '
    'L = 0 because the statement carries no real-world scene at all: it is a circle and a point given in '
    'pure coordinates, so no translation from a story into mathematics is needed. The item was not pushed '
    'into the medium band on purpose, because raising it would need a second required conversion or a '
    'hidden condition, and the batch quota needs this slot to stay easy. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b20.py): with a0 set to Rational(3, 2) * pi, the expression '
    'cos(a0 + pi/3) + sin(a0 + pi/3) simplifies to (sqrt(3) - 1)/2, which is the stored key and matches '
    'the third listed value exactly. Every error path was machine-computed from a named mistake instead '
    'of being invented: cos(a0 - pi/3) + sin(a0 - pi/3) returns -(sqrt(3) + 1)/2 for reversing the '
    'direction to clockwise, cos(pi/2 + pi/3) + sin(pi/2 + pi/3) returns (1 - sqrt(3))/2 for placing the '
    'start at (0, 1) instead of (0, -1), and cos(pi/3) + sin(pi/3) returns (sqrt(3) + 1)/2 for sweeping '
    'from the habitual start (1, 0). The independent check was machine-verified as well: '
    'cos(11*pi/6)**2 + sin(11*pi/6)**2 simplifies to 1, so the terminal point satisfies x**2 + y**2 = 1, '
    'and the numerical values -1.366, -0.366, 0.366 and 1.366 confirm both the ordering of the printed '
    'values and the sign argument, since only one of them is positive and smaller than 1 as quadrant four '
    'demands. The quadrant claim was checked too: 3*pi/2 < 11*pi/6 < 2*pi holds, and 2*pi - 11*pi/6 '
    'returns pi/6 for the reference angle. '
    'Collision sweep on 6417 items (bank 63 files + k1 out + k2 out), probe collide_b20.py / '
    'collide_b20b.py: the pair that defines this item, a unit-circle journey whose starting point is '
    'stated as a coordinate other than (1, 0) together with a request for the sum of the terminal '
    'coordinates, returns 0 items across the whole corpus. The nearest relatives inside chapter 7 either '
    'hand over an angle directly and ask for a single trigonometric value, or walk around the circle from '
    'the standard start, so they share neither the given nor the mechanism; items that do add a quarter '
    'turn work from an angle already in hand rather than from a named point, which removes the one '
    'conversion that gives this item its work. Choices are ordered ascending by numeric value, from about '
    '-1.366 through -0.366 and 0.366 to about 1.366, so the answer slot is forced by that rule and was '
    'not chosen by hand.',
)

# -*- coding: utf-8 -*-
add_fill(
    136,
    ['7.2'],
    'ปานกลาง',
    'บนวงกลมหนึ่งหน่วยที่มีจุดศูนย์กลางอยู่ที่จุดกำเนิด ให้ $P(t)$ '
    'แทนจุดปลายส่วนโค้งที่ได้จากการวัดส่วนโค้งจากจุด $(1, 0)$ '
    'ไปตามเส้นรอบวงเป็นระยะ $|t|$ หน่วย โดยวัดในทิศทวนเข็มนาฬิกาเมื่อ $t > 0$ '
    'และวัดในทิศตามเข็มนาฬิกาเมื่อ $t < 0$ กำหนดให้ $t_0$ เป็นจำนวนจริงซึ่ง '
    '$P(t_0 + \\pi) = \\left(-\\dfrac{9}{41},\\ \\dfrac{40}{41}\\right)$ '
    'ถ้า $P\\left(t_0 + \\dfrac{\\pi}{2}\\right) = (a, b)$ และ '
    '$P\\left(t_0 - \\dfrac{\\pi}{2}\\right) = (c, d)$ แล้วค่าของ $a + d$ เท่ากับเท่าใด',
    '31/41',
    ['31/41', '\\dfrac{31}{41}'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• จุดปลายส่วนโค้งบนวงกลมหนึ่งหน่วยมีพิกัดเป็น <b>โคไซน์กับไซน์</b> ของระยะที่วัดไปเสมอ '
        'นั่นคือ $P(t) = (\\cos t,\\ \\sin t)$ ทุกค่า $t$ · '
        'ประโยคนี้ไม่ใช่ทฤษฎีบทที่ต้องพิสูจน์ แต่เป็น<b>นิยาม</b>ของ $\\cos$ และ $\\sin$ ในระดับชั้นนี้ '
        '⇒ พิกัดช่องหน้าคือ $\\cos$ และพิกัดช่องหลังคือ $\\sin$ ⛔ ห้ามสลับกันเด็ดขาด',
        '• เหตุผลที่ใช้ “ระยะที่วัดไปตามเส้นรอบวง” แทน “ขนาดของมุม” ได้เลย : '
        'ความยาวส่วนโค้งคือ $s = r\\theta$ และวงกลมหนึ่งหน่วยมี $r = 1$ '
        '⇒ $s = \\theta$ พอดี ระยะที่เดินไปจึงเท่ากับขนาดของมุมที่จุดศูนย์กลางเมื่อวัดเป็นเรเดียน · '
        'เครื่องหมายของ $t$ ทำหน้าที่บอกทิศ คือบวกแปลว่าทวนเข็มนาฬิกา และลบแปลว่าตามเข็มนาฬิกา',
        '• เดินต่อไปอีก<b>ครึ่งรอบ</b> คือบวก $\\pi$ จะได้จุดที่อยู่ตรงข้ามกันผ่านจุดศูนย์กลางพอดี '
        '⇒ $\\cos(t + \\pi) = -\\cos t$ และ $\\sin(t + \\pi) = -\\sin t$ '
        'พูดเป็นภาษาคนคือ<b>กลับเครื่องหมายทั้งสองช่อง</b> · '
        'และเพราะกลับเครื่องหมายสองครั้งได้ของเดิม การ<b>ถอยกลับ</b>ครึ่งรอบจึงใช้กฎเดียวกันนี้ได้เลย',
        '• เดินไปอีก<b>หนึ่งในสี่รอบ</b> สองทิศให้ผลคนละแบบ ต้องจำให้แยกกันชัด ๆ : '
        'ทิศเดินหน้าได้ $\\cos\\left(t + \\dfrac{\\pi}{2}\\right) = -\\sin t$ '
        'และ $\\sin\\left(t + \\dfrac{\\pi}{2}\\right) = \\cos t$ · '
        'ทิศถอยหลังได้ $\\cos\\left(t - \\dfrac{\\pi}{2}\\right) = \\sin t$ '
        'และ $\\sin\\left(t - \\dfrac{\\pi}{2}\\right) = -\\cos t$ '
        '⛔ สังเกตว่าเครื่องหมายลบย้ายที่กันคนละบรรทัด ⇒ เดินหน้ากับถอยหลังไม่ใช่เรื่องเดียวกัน',
        '• วิธีจำที่ไม่ต้องท่องสี่บรรทัดข้างบน คือมองเป็น<b>การหมุนพิกัด</b>รอบจุดกำเนิด : '
        'หมุนทวนเข็มนาฬิกา $\\dfrac{\\pi}{2}$ ส่ง $(x, y)$ ไปเป็น $(-y,\\ x)$ · '
        'หมุนตามเข็มนาฬิกา $\\dfrac{\\pi}{2}$ ส่ง $(x, y)$ ไปเป็น $(y,\\ -x)$ · '
        'ภาพสองอันนี้ต่างกันอยู่ครึ่งรอบพอดี จึงเป็นจุดตรงข้ามกันเสมอ ⛔ เหมือนกันไม่ได้',
        '• ทุกจุดที่อยู่บนวงกลมหนึ่งหน่วยต้องสอดคล้องกับ $x^{2} + y^{2} = 1$ '
        'เพราะวงกลมนี้คือเซตของจุดที่ห่างจากจุดกำเนิดเป็นระยะ $1$ หน่วย '
        '⇒ ใช้เงื่อนไขนี้ตรวจได้ทันทีว่าคู่พิกัดที่เขียนออกมามีสิทธิ์เป็นจุดบนวงกลมนี้จริงหรือไม่ '
        'และใช้เตือนได้ด้วยว่าพิกัดแต่ละช่องต้องอยู่ในช่วง $[-1, 1]$ เท่านั้น',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $P(t)$ คือจุดปลายส่วนโค้งที่ได้จากการเริ่มเดินที่จุด $(1, 0)$ '
        'แล้ววัดไปตามเส้นรอบวงเป็นระยะ $|t|$ หน่วย โดยทวนเข็มนาฬิกาเมื่อ $t > 0$ '
        'และตามเข็มนาฬิกาเมื่อ $t < 0$ ⇒ ตรงกับนิยาม $P(t) = (\\cos t,\\ \\sin t)$ ทุกตัวอักษร',
        '• สิ่งที่โจทย์ยื่นมาให้คือ $P(t_0 + \\pi) = \\left(-\\dfrac{9}{41},\\ \\dfrac{40}{41}\\right)$ '
        '⇒ ⛔ นี่<b>ไม่ใช่</b>ค่าของ $P(t_0)$ แต่เป็นจุดที่เดินเลยไปแล้วอีกครึ่งรอบ',
        '• $P\\left(t_0 + \\dfrac{\\pi}{2}\\right) = (a, b)$ '
        '⇒ $a$ คือพิกัดช่องหน้าของจุดที่หมุน<b>ไปข้างหน้า</b>หนึ่งในสี่รอบ จึงเป็นค่าโคไซน์',
        '• $P\\left(t_0 - \\dfrac{\\pi}{2}\\right) = (c, d)$ '
        '⇒ $d$ คือพิกัดช่องหลังของจุดที่หมุน<b>ถอยหลัง</b>หนึ่งในสี่รอบ จึงเป็นค่าไซน์',
        '• สังเกตหน้าตาก่อนลงมือ : เครื่องหมายหน้า $\\dfrac{\\pi}{2}$ ในวงเล็บสองอันนั้น<b>ไม่เหมือนกัน</b> '
        'อันหนึ่งเป็นบวกอีกอันเป็นลบ ⇒ นี่คือหัวใจของข้อนี้ ห้ามกวาดตาผ่านแล้วคิดว่าเป็นจุดเดียวกัน · '
        'อีกอย่างคือโจทย์ถามแค่ $a + d$ ซึ่งหยิบพิกัด<b>ช่องหน้า</b>ของจุดหนึ่ง '
        'มาบวกกับพิกัด<b>ช่องหลัง</b>ของอีกจุดหนึ่ง ⇒ ไม่ต้องหา $b$ กับ $c$ ก็ตอบได้',
        '• สังเกตอีกอย่าง : $9^{2} + 40^{2} = 81 + 1600 = 1681 = 41^{2}$ '
        '⇒ จุดที่โจทย์ให้มาอยู่บนวงกลมหนึ่งหน่วยจริง เงื่อนไขในโจทย์จึงไม่ขัดกันเอง '
        'และตัวเลขชุด $9$-$40$-$41$ นี้จะโผล่มาซ้ำตลอดทั้งข้อ',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $a + d$ ซึ่งเป็นผลบวกของพิกัดช่องหน้าของ $P\\left(t_0 + \\dfrac{\\pi}{2}\\right)$ '
        'กับพิกัดช่องหลังของ $P\\left(t_0 - \\dfrac{\\pi}{2}\\right)$',
        '',
        '<b>【 ถอยกลับครึ่งรอบเพื่อกู้ $\\cos t_0$ กับ $\\sin t_0$ ออกมาจากจุดที่โจทย์ยื่นให้เสียก่อน '
        'จากนั้นจึงหมุนไปข้างหน้าหนึ่งในสี่รอบเพื่ออ่านค่า $a$ '
        'และหมุนถอยหลังหนึ่งในสี่รอบเพื่ออ่านค่า $d$ '
        'โดยระวังว่าสองทิศนี้ให้เครื่องหมายคนละแบบ แล้วจึงบวกกันบนตัวส่วนร่วม $41$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · ถอยกลับครึ่งรอบ เพื่อกู้ $\\cos t_0$ และ $\\sin t_0$</b>',
        '• สูตรที่ใช้ : นิยาม $P(t) = (\\cos t,\\ \\sin t)$ ⇒ แทน $t$ ด้วย $t_0 + \\pi$ ได้ '
        '$P(t_0 + \\pi) = \\left(\\cos(t_0 + \\pi),\\ \\sin(t_0 + \\pi)\\right)$',
        '• ระบุตัวแปรก่อนแทนค่า : ใช้กฎเลื่อนครึ่งรอบกับทั้งสองช่อง '
        '$\\cos(t_0 + \\pi) = -\\cos t_0$ และ $\\sin(t_0 + \\pi) = -\\sin t_0$ '
        '⇒ ตอนนี้ตัวที่ไม่รู้ค่าเหลือแค่ $\\cos t_0$ กับ $\\sin t_0$ ซึ่งเป็นสิ่งที่เราต้องการพอดี',
        '• แทนค่า แล้วจับคู่พิกัดช่องต่อช่องกับสิ่งที่โจทย์ให้ : '
        '$-\\cos t_0 = -\\dfrac{9}{41}$ และ $-\\sin t_0 = \\dfrac{40}{41}$',
        '• ยุบทีละสมการด้วยการคูณสองข้างด้วย $-1$ : '
        '$\\cos t_0 = \\dfrac{9}{41}$ และ $\\sin t_0 = -\\dfrac{40}{41}$',
        '• 📌 อ่านความหมายของผลที่ได้ : $\\cos t_0$ เป็นบวกแต่ $\\sin t_0$ เป็นลบ '
        '⇒ จุด $P(t_0)$ อยู่ในจตุภาคที่ $4$ ส่วนจุดที่โจทย์ให้มามีช่องหน้าเป็นลบและช่องหลังเป็นบวก '
        '⇒ อยู่ในจตุภาคที่ $2$ · สองจุดนี้อยู่ตรงข้ามกันผ่านจุดกำเนิดพอดี '
        'ซึ่งเป็นสิ่งที่ต้องเป็นอยู่แล้วสำหรับจุดที่ห่างกันครึ่งรอบ ⇒ เครื่องหมายที่ถอดออกมาไม่ได้พลิกผิดทาง',
        '',
        '<b>ขั้นที่ 2 · หมุนไปข้างหน้าหนึ่งในสี่รอบ เพื่ออ่านค่า $a$</b>',
        '• โจทย์เขียนว่า $P\\left(t_0 + \\dfrac{\\pi}{2}\\right) = (a, b)$ '
        'และนิยามบอกว่าพิกัดช่องหน้าคือโคไซน์ ⇒ $a = \\cos\\left(t_0 + \\dfrac{\\pi}{2}\\right)$ '
        '⛔ ไม่ใช่ไซน์ เพราะไซน์คือ $b$ ซึ่งข้อนี้ไม่ได้ถาม',
        '• สูตรที่ใช้ : กฎเลื่อนหนึ่งในสี่รอบทิศเดินหน้า '
        '$\\cos\\left(t + \\dfrac{\\pi}{2}\\right) = -\\sin t$',
        '• ระบุตัวแปร : ในสูตรนี้ $t$ คือ $t_0$ และค่าที่ต้องหยิบมาใช้คือ $\\sin t_0$ '
        'ซึ่งขั้นที่ $1$ หามาได้แล้วว่าเท่ากับ $-\\dfrac{40}{41}$',
        '• แทนค่าแล้วยุบ : $a = -\\sin t_0 = -\\left(-\\dfrac{40}{41}\\right) = \\dfrac{40}{41}$ '
        '⇒ ลบสองตัวหักล้างกันจนได้ค่าบวก',
        '• เก็บไว้ใช้ตรวจตอนท้าย แม้โจทย์จะไม่ได้ถาม : '
        '$b = \\sin\\left(t_0 + \\dfrac{\\pi}{2}\\right) = \\cos t_0 = \\dfrac{9}{41}$ '
        '⇒ จุดนี้คือ $\\left(\\dfrac{40}{41},\\ \\dfrac{9}{41}\\right)$',
        '',
        '<b>ขั้นที่ 3 · หมุนถอยหลังหนึ่งในสี่รอบ เพื่ออ่านค่า $d$ ⭐ จุดสำคัญของข้อนี้อยู่ตรงนี้</b>',
        '• โจทย์เขียนว่า $P\\left(t_0 - \\dfrac{\\pi}{2}\\right) = (c, d)$ '
        'และนิยามบอกว่าพิกัดช่องหลังคือไซน์ ⇒ $d = \\sin\\left(t_0 - \\dfrac{\\pi}{2}\\right)$',
        '• สูตรที่ใช้ : กฎเลื่อนหนึ่งในสี่รอบทิศถอยหลัง '
        '$\\sin\\left(t - \\dfrac{\\pi}{2}\\right) = -\\cos t$ '
        '⛔ ⛔ ตรงนี้คือจุดที่เด็กพลาดกันมากที่สุด : ผลลัพธ์คือ $-\\cos t$ '
        'ไม่ใช่ $\\cos t$ เฉย ๆ เครื่องหมายลบหายไม่ได้',
        '• ระบุตัวแปร : ในสูตรนี้ $t$ คือ $t_0$ และค่าที่ต้องหยิบมาใช้คือ $\\cos t_0$ '
        'ซึ่งขั้นที่ $1$ หามาได้แล้วว่าเท่ากับ $\\dfrac{9}{41}$',
        '• แทนค่าแล้วยุบ : $d = -\\cos t_0 = -\\dfrac{9}{41}$',
        '• ⭐ เทียบขั้นที่ $2$ กับขั้นที่ $3$ ให้เห็นกับตาว่าทำไมสองทิศให้ผลไม่เหมือนกัน : '
        'ระยะจาก $t_0 - \\dfrac{\\pi}{2}$ ไปถึง $t_0 + \\dfrac{\\pi}{2}$ เท่ากับ '
        '$\\dfrac{\\pi}{2} - \\left(-\\dfrac{\\pi}{2}\\right) = \\pi$ '
        'ซึ่งก็คือครึ่งรอบพอดี ⇒ จุดสองจุดนี้อยู่ตรงข้ามกันผ่านจุดกำเนิด '
        'พิกัดของมันจึงต้องกลับเครื่องหมายกันช่องต่อช่อง '
        '⇒ เป็นไปไม่ได้เลยที่เดินหน้ากับถอยหลังหนึ่งในสี่รอบจะให้ค่าชุดเดียวกัน',
        '',
        '<b>ขั้นที่ 4 · บวกสองค่าที่ได้ แล้วตรวจว่าเป็นเศษส่วนอย่างต่ำ</b>',
        '• สิ่งที่ต้องหาคือ $a + d$ ⇒ หยิบผลของขั้นที่ $2$ มาบวกกับผลของขั้นที่ $3$',
        '• แทนค่า : $a + d = \\dfrac{40}{41} + \\left(-\\dfrac{9}{41}\\right) '
        '= \\dfrac{40}{41} - \\dfrac{9}{41}$',
        '• ยุบ : ตัวส่วนเท่ากันอยู่แล้วจึงลบเฉพาะตัวเศษ '
        '$\\dfrac{40 - 9}{41} = \\dfrac{31}{41}$',
        '• ตรวจว่าย่อต่อไม่ได้ : $41$ เป็นจำนวนเฉพาะ และ $31$ ไม่ใช่พหุคูณของ $41$ '
        '⇒ ตัวหารร่วมมากของ $31$ กับ $41$ คือ $1$ ⇒ $\\dfrac{31}{41}$ เป็นเศษส่วนอย่างต่ำแล้ว',
        '• เช็คความสมเหตุสมผลทันที : $\\dfrac{31}{41} \\approx 0.756$ '
        'ซึ่งอยู่ในช่วง $[-2, 2]$ ตามที่ต้องเป็น เพราะ $a$ และ $d$ ต่างก็เป็นพิกัดของจุดบนวงกลมหนึ่งหน่วย '
        'จึงอยู่ในช่วง $[-1, 1]$ ทั้งคู่ ⇒ ผลบวกของทั้งสองจะหลุดออกนอกช่วงนี้ไม่ได้',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · เลิกใช้สูตรเลื่อนมุมทั้งหมด '
        'แล้วหันไปหมุนพิกัดของจุดบนระนาบตรง ๆ พร้อมเดินย้อนกลับเข้าเงื่อนไขที่โจทย์ให้)</b>',
        '• เส้นทางแรกพึ่งกฎเลื่อนมุมล้วน ๆ ทั้งสี่ขั้น ⇒ วิธีตรวจที่ไม่ซ้ำทางเดิม '
        'คือไม่แตะกฎเลื่อนมุมเลยสักบรรทัด แต่ใช้ผลของการหมุนจุดรอบจุดกำเนิดแทน '
        'แล้วปิดท้ายด้วยการเดินย้อนศรกลับไปเทียบกับข้อมูลที่โจทย์ให้',
        '• ด่านแรก ตรวจว่าคู่พิกัดที่ถอดได้ในขั้นที่ $1$ เป็นจุดบนวงกลมหนึ่งหน่วยจริงหรือไม่ : '
        '$\\left(\\dfrac{9}{41}\\right)^{2} + \\left(-\\dfrac{40}{41}\\right)^{2} '
        '= \\dfrac{81 + 1600}{1681} = \\dfrac{1681}{1681} = 1$ ✓ '
        '⇒ ผ่าน ถ้าถอดเครื่องหมายผิดจนได้ค่าเกิน $1$ ด่านนี้จะจับได้ทันที',
        '• ด่านที่สอง เดินย้อนศร : ถ้า $P(t_0) = \\left(\\dfrac{9}{41},\\ -\\dfrac{40}{41}\\right)$ จริง '
        'การเดินต่อไปอีกครึ่งรอบต้องพาไปยังจุดตรงข้ามผ่านจุดกำเนิด '
        'คือ $\\left(-\\dfrac{9}{41},\\ \\dfrac{40}{41}\\right)$ '
        'ซึ่งตรงกับที่โจทย์ให้มาทุกช่อง ✓ ⇒ ยืนยันว่าขั้นที่ $1$ ไม่ได้กลับเครื่องหมายสลับทาง',
        '• ด่านที่สาม หมุนทวนเข็มนาฬิกาหนึ่งในสี่รอบด้วยกฎ $(x, y) \\mapsto (-y,\\ x)$ : '
        'จุด $\\left(\\dfrac{9}{41},\\ -\\dfrac{40}{41}\\right)$ ถูกส่งไปเป็น '
        '$\\left(\\dfrac{40}{41},\\ \\dfrac{9}{41}\\right)$ ⇒ อ่านช่องหน้าได้ $a = \\dfrac{40}{41}$ ✓ '
        'ตรงกับขั้นที่ $2$ และช่องหลังก็ได้ $b = \\dfrac{9}{41}$ ตรงกับที่เก็บไว้',
        '• ด่านที่สี่ หมุนตามเข็มนาฬิกาหนึ่งในสี่รอบด้วยกฎ $(x, y) \\mapsto (y,\\ -x)$ : '
        'จุดเดิมถูกส่งไปเป็น $\\left(-\\dfrac{40}{41},\\ -\\dfrac{9}{41}\\right)$ '
        '⇒ อ่านช่องหลังได้ $d = -\\dfrac{9}{41}$ ✓ ตรงกับขั้นที่ $3$',
        '• ปิดท้าย : ภาพที่ได้จากสองด่านหลังคือ $\\left(\\dfrac{40}{41},\\ \\dfrac{9}{41}\\right)$ '
        'กับ $\\left(-\\dfrac{40}{41},\\ -\\dfrac{9}{41}\\right)$ '
        'ซึ่งกลับเครื่องหมายกันครบทั้งสองช่องพอดี ⇒ ยืนยันด้วยตาอีกชั้นว่าเดินหน้ากับถอยหลังคนละจุดจริง · '
        'บวกกันได้ $\\dfrac{40}{41} - \\dfrac{9}{41} = \\dfrac{31}{41}$ เท่ากับเส้นทางแรกทุกประการ ✓',
        '',
        '✅ <b>คำตอบ</b> ค่าของ $a + d$ เท่ากับ $\\dfrac{31}{41}$ '
        'ซึ่งมาจาก $a = \\dfrac{40}{41}$ บวกกับ $d = -\\dfrac{9}{41}$ '
        'และเขียนเป็นทศนิยมโดยประมาณได้ $0.756$ · เป็นผลบวกของพิกัดบนวงกลมหนึ่งหน่วย '
        'จึงเป็นจำนวนล้วนที่ไม่มีหน่วย',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอโจทย์ที่ยื่นค่าของจุดหลังเลื่อนมาให้แทนที่จะยื่นจุดต้นทาง ให้<b>ถอยกลับไปที่จุดต้นทางก่อนเสมอ</b> '
        'อย่าพยายามกระโดดจาก $t_0 + \\pi$ ไป $t_0 + \\dfrac{\\pi}{2}$ ในก้าวเดียว '
        'เพราะระยะระหว่างสองจุดนั้นคือ $-\\dfrac{\\pi}{2}$ ซึ่งเป็นการถอยหลัง เผลอนิดเดียวก็บวกผิดทิศ · '
        'การกู้ $\\cos t_0$ กับ $\\sin t_0$ ออกมาเป็นตัวเลขก่อน ทำให้ทุกคำถามที่เหลือกลายเป็นการแทนค่าเฉย ๆ',
        '• ถ้าจำกฎเลื่อนสี่บรรทัดไม่ไหว ให้วาดวงกลมแล้วหมุนจุดเอาเอง : '
        'ทวนเข็มนาฬิกา $\\dfrac{\\pi}{2}$ คือ $(x, y) \\mapsto (-y,\\ x)$ '
        'และตามเข็มนาฬิกา $\\dfrac{\\pi}{2}$ คือ $(x, y) \\mapsto (y,\\ -x)$ '
        '⇒ จำสองบรรทัดนี้แทนได้ทั้งหมด และยังกันการสับสนเรื่องทิศได้ในตัว '
        'เพราะเห็นภาพว่าหมุนไปทางไหน',
        '• ก่อนตอบ ให้ชี้นิ้วอ่านซ้ำว่ากำลังหยิบพิกัด<b>ช่องไหน</b>ของ<b>จุดไหน</b> · '
        'ข้อนี้ขอ $a$ ซึ่งเป็นช่องหน้าของจุดแรก และขอ $d$ ซึ่งเป็นช่องหลังของจุดที่สอง '
        '⇒ หยิบข้ามช่องเมื่อไรก็ได้ค่าผิดทันทีทั้งที่คำนวณถูกทุกบรรทัด',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $-\\dfrac{31}{41}$ เพราะสลับทิศการหมุนของทั้งสองจุด '
        'คือไปใช้ $a = \\sin t_0 = -\\dfrac{40}{41}$ และ $d = \\cos t_0 = \\dfrac{9}{41}$ '
        'ทั้งที่กฎบอกว่าต้องมีเครื่องหมายลบนำหน้าทั้งคู่ · '
        'ค่านี้ผิดจริง ตรวจได้โดยไม่ต้องคำนวณซ้ำ : ถ้า $a$ ติดลบ '
        'จุด $P\\left(t_0 + \\dfrac{\\pi}{2}\\right)$ จะต้องอยู่ทางซ้ายของแกน $Y$ '
        'แต่การหมุน $\\left(\\dfrac{9}{41},\\ -\\dfrac{40}{41}\\right)$ ทวนเข็มนาฬิกาหนึ่งในสี่รอบ '
        'พาจุดจากจตุภาคที่ $4$ ไปยังจตุภาคที่ $1$ ซึ่งพิกัดช่องหน้าต้องเป็นบวก ⇒ ขัดกันชัดเจน · '
        'สังเกตว่าค่าที่ได้เป็นจำนวนตรงข้ามของคำตอบจริงพอดี ซึ่งเป็นลายเซ็นของการสลับทิศทั้งคู่',
        '• ได้ค่า $\\dfrac{49}{41}$ เพราะคิดว่าเดินหน้ากับถอยหลัง $\\dfrac{\\pi}{2}$ ให้ผลเหมือนกัน '
        'จึงใช้ $d = \\cos t_0 = \\dfrac{9}{41}$ โดยทำเครื่องหมายลบตกไป '
        'แล้วบวกได้ $\\dfrac{40}{41} + \\dfrac{9}{41} = \\dfrac{49}{41}$ · '
        'ค่านี้ผิดแน่นอนเพราะกฎที่ถูกคือ $\\sin\\left(t - \\dfrac{\\pi}{2}\\right) = -\\cos t$ · '
        'พิสูจน์อีกทางด้วยการหมุนพิกัด : ตามเข็มนาฬิกาหนึ่งในสี่รอบพา '
        '$\\left(\\dfrac{9}{41},\\ -\\dfrac{40}{41}\\right)$ ไปเป็น '
        '$\\left(-\\dfrac{40}{41},\\ -\\dfrac{9}{41}\\right)$ ซึ่งอยู่ในจตุภาคที่ $3$ '
        '⇒ ช่องหลังต้องเป็นลบ จะเป็น $\\dfrac{9}{41}$ ไม่ได้เลย',
        '• ได้ค่า $0$ เพราะอ่านโจทย์ผิดเป็น $b + d$ '
        'แล้วคำนวณ $\\dfrac{9}{41} + \\left(-\\dfrac{9}{41}\\right) = 0$ · '
        'ค่านี้เกิดจากการหยิบผิดช่อง ไม่ได้เกิดจากการคิดเลขผิดสักบรรทัด '
        'จึงเป็นกับดักที่เนียนที่สุดในข้อนี้ · '
        'ที่มันออกมาเป็น $0$ พอดีก็เพราะ $b = \\cos t_0$ และ $d = -\\cos t_0$ '
        'เป็นจำนวนตรงข้ามกันเสมอไม่ว่าโจทย์จะให้ตัวเลขอะไรมา '
        '⇒ ถ้าคำนวณแล้วได้ $0$ ให้สงสัยไว้ก่อนเลยว่าหยิบผิดช่อง แล้วย้อนไปอ่านโจทย์ใหม่',
        '• ได้ค่า $-\\dfrac{31}{41}$ อีกทางหนึ่ง โดยพลาดคนละจุดกับข้อแรก '
        'คือลืมกลับเครื่องหมายตอนถอด $P(t_0 + \\pi)$ กลับมาเป็น $P(t_0)$ '
        'จึงหยิบตัวเลขที่โจทย์ให้ไปใช้ดื้อ ๆ เป็น $\\cos t_0 = -\\dfrac{9}{41}$ '
        'และ $\\sin t_0 = \\dfrac{40}{41}$ ⇒ ได้ $a = -\\sin t_0 = -\\dfrac{40}{41}$ '
        'กับ $d = -\\cos t_0 = \\dfrac{9}{41}$ ⇒ รวมกันเป็น $-\\dfrac{31}{41}$ · '
        'ค่านี้ผิดเพราะจุดที่โจทย์ให้คือ $P(t_0 + \\pi)$ ไม่ใช่ $P(t_0)$ '
        'และการเดินครึ่งรอบทำให้พิกัดกลับเครื่องหมายทั้งสองช่อง ⇒ ข้ามขั้นที่ $1$ ไม่ได้ · '
        '📌 บทเรียนคือค่าที่พลาดสองเส้นทางนี้บังเอิญตรงกัน '
        'จึงห้ามใช้ “ได้เลขสวย” เป็นหลักฐานว่าทำถูก ต้องแทนกลับเข้าโจทย์เสมอ',
    ],
    'V.mold: G = the unit circle wrapping function P(t) spelled out in words rather than by formula, with '
    'the winding starting at (1, 0), running counterclockwise for positive t and clockwise for negative t, '
    'together with one real number t0 whose image is never handed over directly: what the statement '
    'supplies is the image after a further half turn, namely P(t0 + pi) = (-9/41, 40/41), and two more '
    'images named only through their coordinate pairs, P(t0 + pi/2) = (a, b) and P(t0 - pi/2) = (c, d) / '
    'A = the value of a + d, that is the first coordinate of one image added to the second coordinate of '
    'the other, asked as a free numeric response with no candidate values printed anywhere on the page / '
    'M = M-HALF-TURN-UNDO-THEN-QUARTER-BOTH-WAYS, that is: read the verbal definition as '
    'P(t) = (cos t, sin t), undo the half turn by flipping the sign of both coordinates to recover '
    'cos t0 = 9/41 and sin t0 = -40/41, then step a quarter turn forward for a = cos(t0 + pi/2) = -sin t0 '
    'and a quarter turn backward for d = sin(t0 - pi/2) = -cos t0, keeping the two shift rules apart '
    'because they place the minus sign on different functions, and finally add over the common '
    'denominator 41. '
    'Rubric F2 C1 P2 T1 L1 = 7/15, total below 8 so the hard band is not reached -> level: ปานกลาง. '
    'F = 2 because two blocks of knowledge are in play and neither can replace the other: the identity of '
    'the wrapping function with the pair (cos t, sin t), which is what converts a sentence about arc '
    'measurement into coordinates at all, and the shift rules for pi and for pi/2 in both directions; F is '
    'not 3 because the Pythagorean relation x^2 + y^2 = 1 appears only inside the verification block and '
    'is never needed to produce the answer. C = 1 because the item welds the coordinate reading of a point '
    'on the unit circle to the algebra of shifted arguments, but both halves live under the single '
    'subtopic label 7.2 and no genuinely second subtopic has to be entered, which is what a C = 2 item '
    'requires. P = 2 because the work runs in two stages of different kinds: a reversal stage that walks '
    'backwards from the supplied image to cos t0 and sin t0, and an evaluation stage that walks forwards '
    'and backwards by a quarter turn; the closing subtraction 40/41 - 9/41 is trailing arithmetic inside '
    'the second stage rather than a third stage, following the q105 and q113 baseline where a final '
    'reduction does not buy a further point. T = 1 and deliberately not 2 because there is exactly one '
    'turning point, namely that a quarter turn forward and a quarter turn backward do not land on '
    'mirrored data: one produces minus the sine while the other produces minus the cosine, so the two '
    'answers are not interchangeable; the undoing of the half turn is a mechanical double sign flip '
    'announced by the wording of the statement and does not count as a second independent discovery, '
    'which is what T = 2 would demand. L = 1 because the statement carries no figure and no real-world '
    'scene, yet the reader must still set up the unit circle and both senses of rotation mentally before '
    'any sign can be trusted, so it sits above the purely symbolic L = 0 baseline while staying planar and '
    'therefore below L = 2. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b20.py): with c0 = Rational(9,41) and s0 = Rational(-40,41) and t0 = atan2(s0, c0), the '
    'machine first confirms that the item is self consistent by evaluating cos(t0 + pi) to -9/41 and '
    'sin(t0 + pi) to 40/41, which reproduces the pair printed in the statement exactly, so the recovered '
    'values of cos t0 and sin t0 are verified rather than assumed. It then simplifies cos(t0 + pi/2) to '
    '40/41 and sin(t0 - pi/2) to -9/41 and their sum to 31/41, and the stored answer string 31/41 was '
    'parsed as a rational and compared against that value instead of being eyeballed. Every wrong road '
    'printed in the pitfalls block was computed by machine and not invented: the swapped rotation sense '
    's0 + c0 returns -31/41, the dropped minus sign -s0 + c0 returns 49/41, the misread request b + d '
    'evaluates to cos t0 - cos t0 = 0 identically, and the road that skips the half turn reversal and '
    'feeds the printed pair straight in returns -31/41 as well, which is why the last pitfall line warns '
    'explicitly that two different mistakes collide on one value and that a familiar looking number is no '
    'evidence of correct work. The independent route was checked separately as coordinate rotation: '
    'mapping (x, y) to (-y, x) sends (9/41, -40/41) to (40/41, 9/41) and mapping (x, y) to (y, -x) sends '
    'it to (-40/41, -9/41), and the two images are exact negatives of each other, which is the machine '
    'form of the claim that the two quarter turns are half a revolution apart. '
    'Collision sweep on 6437 items (bank 63 files + k1 out + k2 out), probe collide_b20.py / '
    'collide_b20b.py: the phrase for the unit circle returns 16 items in the whole corpus, but the pair '
    '(an image supplied only after a shift, so that the base point has to be recovered first) crossed with '
    '(two quarter turns taken in opposite senses) returns zero items. The nearest neighbour is '
    'gen-chap-07-trigonometry-q008, which hands over the endpoint for t = theta directly and asks for the '
    'endpoint at pi/2 - theta: there the base point needs no recovery, the shift is a cofunction '
    'reflection rather than a rotation, only one shifted point is involved, and the requested object is a '
    'whole coordinate pair. The second nearest is gen-chap-07-trigonometry-q021, which also supplies the '
    'endpoint directly and asks for sin(theta + pi) + cos(-theta), so it shares the half turn rule but '
    'uses it forwards, never asks the reader to invert it, and returns the value of a trigonometric '
    'expression rather than a sum of coordinates read off two different points. Neither reuses this '
    'mechanism, in which the half turn is deliberately placed on the given datum so that the reversal must '
    'happen before anything else can start. Since this is a fill item there is no choice list, so no '
    'answer slot exists and nothing about the answer could have been positioned by hand.',
)

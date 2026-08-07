# -*- coding: utf-8 -*-
add(
    164,
    ['7.4'],
    'ยากมาก',
    'กำหนดให้ $\\theta$ เป็นจำนวนจริงซึ่ง $\\dfrac{\\sin^4\\theta}{3} + \\dfrac{\\cos^4\\theta}{5} = \\dfrac{1}{8}$ '
    'ค่าของ $\\dfrac{\\sin^6\\theta}{9} + \\dfrac{\\cos^6\\theta}{25}$ เท่ากับข้อใด',
    [
        '$\\dfrac{1}{512}$',
        '$\\dfrac{1}{64}$',
        '$\\dfrac{17}{256}$',
        '$\\dfrac{1}{8}$',
    ],
    1,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เอกลักษณ์พีทาโกรัส : $\\sin^{2}\\theta + \\cos^{2}\\theta = 1$ ทุกค่าของ $\\theta$ · '
        'ที่เป็นเช่นนี้เพราะจุดบนวงกลมหนึ่งหน่วยที่คู่กับมุม $\\theta$ มีพิกัดเป็น '
        '$(\\cos\\theta,\\ \\sin\\theta)$ และจุดนั้นห่างจุดกำเนิดเท่ากับ $1$ เสมอ '
        'เมื่อเขียนระยะทางกำลังสองออกมาจึงได้เอกลักษณ์นี้ทันที · '
        'สิ่งที่จะใช้จริงในข้อนี้คือรูปย้ายข้าง $\\cos^{2}\\theta = 1 - \\sin^{2}\\theta$ '
        'ซึ่งแปลว่า ถ้ารู้ค่าของ $\\sin^{2}\\theta$ เมื่อไร ก็รู้ค่าของ $\\cos^{2}\\theta$ ทันที '
        '⇒ ของสองอย่างที่ดูเหมือนตัวไม่รู้สองตัว แท้จริงเป็นตัวไม่รู้ตัวเดียว '
        'และเพราะทั้งคู่เป็นกำลังสองของจำนวนจริง จึงมีกรอบบังคับติดมาด้วยว่า '
        '$0 \\le \\sin^{2}\\theta \\le 1$ เสมอ',
        '• กำลังคู่กลืนเครื่องหมายทิ้ง : $\\sin^{4}\\theta = \\left(\\sin^{2}\\theta\\right)^{2}$ '
        'และ $\\sin^{6}\\theta = \\left(\\sin^{2}\\theta\\right)^{3}$ '
        'เช่นเดียวกันกับฝั่ง $\\cos$ ⇒ ทั้งเงื่อนไขและนิพจน์ที่ถามประกอบขึ้นจาก '
        '$\\sin^{2}\\theta$ กับ $\\cos^{2}\\theta$ ล้วน ๆ ไม่มีพจน์กำลังคี่แม้แต่พจน์เดียว · '
        'ผลที่ตามมาซึ่งสำคัญมากคือ ถ้าเปลี่ยนเครื่องหมายของ $\\sin\\theta$ หรือ $\\cos\\theta$ '
        'หรือทั้งคู่ ค่าของทุกก้อนในข้อนี้<b>ไม่เปลี่ยนเลย</b> '
        '⇒ เครื่องมือประจำตัวที่ชื่อว่า “ดูจตุภาคเพื่อคัดเครื่องหมาย” จะไม่มีงานทำในข้อนี้',
        '• สมการกำลังสองกับดิสคริมิแนนต์ : สมการ $ax^{2} + bx + c = 0$ เมื่อ $a \\ne 0$ '
        'มีจำนวนรากจริงตัดสินด้วยค่า $b^{2} - 4ac$ · ถ้าค่านี้เป็นบวกจะมีสองราก '
        'ถ้าเป็นลบจะไม่มีรากจริง และ 🔴 ถ้า<b>เท่ากับศูนย์</b>จะมีรากจริงเพียงค่าเดียว '
        'ซึ่งเทียบเท่ากับการที่ฝั่งซ้ายเขียนได้เป็นกำลังสองสมบูรณ์ $(px - q)^{2} = 0$ · '
        'ความหมายที่ต้องจำคือ สมการแบบนี้ไม่ได้ให้ผู้เข้าชิงมาสองราย '
        'แล้วรอให้เราหาข้อมูลเพิ่มมาคัด แต่มัน<b>บังคับค่าไว้ค่าเดียว</b>ตั้งแต่บรรทัดแรกที่เขียนมันลงไป',
        '• การอ่านเศษส่วนแบบดึงตัวประกอบร่วมออกมา : $\\dfrac{u^{2}}{p}$ เขียนใหม่ได้เป็น '
        '$u \\cdot \\dfrac{u}{p}$ และ $\\dfrac{u^{3}}{p^{2}}$ เขียนใหม่ได้เป็น '
        '$u \\cdot \\left(\\dfrac{u}{p}\\right)^{2}$ · '
        'การอ่านแบบนี้มีประโยชน์ตรงที่ ถ้าบังเอิญสองก้อนมีค่า $\\dfrac{u}{p}$ เท่ากันพอดี '
        'ทั้งผลบวกจะยุบเหลือ “ค่านั้น คูณ ผลบวกของตัวหน้า” '
        '⇒ ตัวเลขจะออกมาเป็นระเบียบทันทีโดยไม่ต้องกระจายอะไรเลย',
        '• อสมการโคชี-ชวาร์ซรูปเศษส่วนสองพจน์ : เมื่อ $p > 0$ และ $q > 0$ จะได้ '
        '$\\dfrac{a^{2}}{p} + \\dfrac{b^{2}}{q} \\ge \\dfrac{(a + b)^{2}}{p + q}$ เสมอ '
        'โดยเท่ากันก็ต่อเมื่อ $\\dfrac{a}{p} = \\dfrac{b}{q}$ · '
        'พิสูจน์ได้ตรง ๆ ด้วยการคูณไขว้แล้วย้ายข้าง จะเหลือ $(qa - pb)^{2} \\ge 0$ '
        'ซึ่งจริงเสมอเพราะเป็นกำลังสองของจำนวนจริง · '
        'อ่านความหมายได้ว่า ฝั่งขวาคือ<b>ค่าต่ำสุด</b>ที่ฝั่งซ้ายเป็นไปได้ '
        '⇒ ถ้าโจทย์ยื่นค่าฝั่งซ้ายมาเท่ากับค่าต่ำสุดนั้นพอดี แปลว่าโจทย์กำลังบอกเราว่า '
        'สถานการณ์นี้เป็นกรณีที่เท่ากัน ซึ่งเกิดได้ที่จุดเดียวเท่านั้น',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• เงื่อนไขหนึ่งบรรทัด : $\\dfrac{\\sin^{4}\\theta}{3} + \\dfrac{\\cos^{4}\\theta}{5} '
        '= \\dfrac{1}{8}$ · ตัวหารสองตัวคือ $3$ กับ $5$ และเลขชี้กำลังคือ $4$ ทั้งสองก้อน',
        '• สิ่งที่ถาม : $\\dfrac{\\sin^{6}\\theta}{9} + \\dfrac{\\cos^{6}\\theta}{25}$ · '
        'ตัวหารสองตัวคือ $9$ กับ $25$ และเลขชี้กำลังคือ $6$ ทั้งสองก้อน '
        '⇒ 🔴 ตัวหารของนิพจน์ที่ถาม<b>ไม่ใช่</b>ตัวหารเดิม แต่เป็นกำลังสองของตัวหารเดิม '
        'เพราะ $9 = 3^{2}$ และ $25 = 5^{2}$ · ต้องขีดเส้นใต้ข้อเท็จจริงนี้ไว้ตั้งแต่ยังไม่ลงมือ',
        '• สังเกตหน้าตาก่อนลงมือ : โจทย์<b>ไม่ได้บอกช่วงของ</b> $\\theta$ เลยแม้แต่คำเดียว '
        'ไม่บอกจตุภาค ไม่บอกว่าเป็นมุมแหลม ไม่บอกขอบซ้ายขอบขวา · '
        'ของแบบนี้มีทางเป็นไปได้แค่สองทาง ทางแรกคือโจทย์บกพร่อง '
        'ทางที่สองคือค่าที่ถาม<b>ไม่ขึ้นกับ</b>ว่า $\\theta$ อยู่ที่ไหน · '
        'มองกลับไปที่หน้าตาของทั้งสองก้อนจะเห็นว่ามีแต่กำลังคู่ทั้งหมด '
        '⇒ ทางที่สองคือคำอธิบายที่ถูก และนั่นแปลว่าทั้งข้อขึ้นอยู่กับตัวเลขเพียงตัวเดียวคือ '
        '$\\sin^{2}\\theta$',
        '• สังเกตอีกอย่างที่เป็นเบาะแสใหญ่ : ตัวเลขฝั่งขวาของเงื่อนไขคือ $\\dfrac{1}{8}$ '
        'และผลบวกของตัวหารทั้งสองคือ $3 + 5 = 8$ พอดี '
        '⇒ ค่าที่โจทย์ยื่นมาคือ $\\dfrac{1}{3 + 5}$ เป๊ะ ๆ · '
        'ความบังเอิญแบบนี้แทบไม่เคยเป็นความบังเอิญจริง ๆ '
        'มันคือลายเซ็นของกรณีที่เท่ากันในอสมการโคชี-ชวาร์ซ '
        'ซึ่งเป็นสัญญาณล่วงหน้าว่าเงื่อนไขจะบังคับคำตอบไว้ค่าเดียว',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\dfrac{\\sin^{6}\\theta}{9} + \\dfrac{\\cos^{6}\\theta}{25}$ ออกมาเป็นตัวเลขตัวเดียว · '
        '⛔ ไม่ต้องหาว่า $\\theta$ เท่ากับเท่าใด และ⛔ ไม่ต้องรู้ว่า $\\theta$ อยู่จตุภาคไหน '
        'เพราะสิ่งเดียวที่นิพจน์นี้ต้องการคือค่าของ $\\sin^{2}\\theta$ '
        '⇒ งานทั้งหมดจึงเหลือแค่สองท่อน ท่อนแรกคือรีดค่าของ $\\sin^{2}\\theta$ ออกจากเงื่อนไข '
        'ท่อนที่สองคือแทนค่าลงไปในนิพจน์ที่ถามอย่างระมัดระวัง',
        '',
        '<b>【 แทน $s = \\sin^{2}\\theta$ เพื่อยุบทั้งข้อให้เหลือตัวแปรเดียว '
        'แล้วคูณตัวส่วนทิ้งจนเงื่อนไขกลายเป็นสมการกำลังสอง '
        'ซึ่งจะพบว่ามันเป็นกำลังสองสมบูรณ์ จึงบังคับ $s$ ไว้ค่าเดียวโดยไม่มีสาขาให้คัดเลย '
        'จากนั้นแทนค่าลงในนิพจน์ที่ถาม โดยระวังว่าตัวส่วนของนิพจน์นั้นเป็นกำลังสองของตัวส่วนเดิม 】</b>',
        '',
        '<b>ขั้นที่ 1 · เปลี่ยนทั้งข้อให้เหลือตัวแปรเดียว</b>',
        '• ทำไมต้องเปลี่ยน : ตราบใดที่ยังเขียนว่า $\\sin\\theta$ กับ $\\cos\\theta$ '
        'สมองจะเผลอคิดว่ามีของสองอย่างต้องหา และจะเผลอไปหาเครื่องมือเรื่องมุมมาใช้ · '
        'แต่ข้อนี้ไม่มีพจน์กำลังคี่เลย ⇒ ตั้งชื่อก้อนกำลังสองเป็นตัวแปรใหม่ตัวเดียว '
        'แล้วทั้งข้อจะกลายเป็นพีชคณิตล้วนที่ไม่มีเรื่องมุมเหลืออยู่เลย',
        '• สูตรที่ใช้ : $\\cos^{2}\\theta = 1 - \\sin^{2}\\theta$ จากเอกลักษณ์พีทาโกรัส '
        'ประกอบกับการเขียนกำลังคู่ให้เป็นกำลังของก้อนกำลังสอง '
        '$\\sin^{4}\\theta = \\left(\\sin^{2}\\theta\\right)^{2}$ และ '
        '$\\sin^{6}\\theta = \\left(\\sin^{2}\\theta\\right)^{3}$',
        '• ระบุตัวแปรก่อนแทนค่า : ให้ $s = \\sin^{2}\\theta$ '
        '⇒ ได้ทันทีว่า $\\cos^{2}\\theta = 1 - s$ · '
        'และเพราะ $s$ เป็นกำลังสองของจำนวนจริงที่มีขนาดไม่เกิน $1$ '
        'จึงมีกรอบติดมาด้วยว่า $0 \\le s \\le 1$ '
        '(กรอบนี้จะถูกเอามาใช้ตรวจในตอนท้ายของขั้นที่ 2)',
        '• แทนค่าลงในเงื่อนไข : $\\dfrac{\\sin^{4}\\theta}{3} + \\dfrac{\\cos^{4}\\theta}{5} '
        '= \\dfrac{s^{2}}{3} + \\dfrac{(1 - s)^{2}}{5}$ '
        '⇒ เงื่อนไขที่โจทย์ให้กลายเป็น $\\dfrac{s^{2}}{3} + \\dfrac{(1 - s)^{2}}{5} = \\dfrac{1}{8}$',
        '• แทนค่าลงในนิพจน์ที่ถามด้วย เพื่อจะได้เห็นเป้าหมายในภาษาเดียวกัน : '
        '$\\dfrac{\\sin^{6}\\theta}{9} + \\dfrac{\\cos^{6}\\theta}{25} '
        '= \\dfrac{s^{3}}{9} + \\dfrac{(1 - s)^{3}}{25}$',
        '• ยุบความคิดให้เหลือประโยคเดียว : ทั้งข้อกลายเป็นคำถามพีชคณิตล้วนว่า '
        '“ถ้า $\\dfrac{s^{2}}{3} + \\dfrac{(1 - s)^{2}}{5} = \\dfrac{1}{8}$ '
        'แล้ว $\\dfrac{s^{3}}{9} + \\dfrac{(1 - s)^{3}}{25}$ เท่ากับเท่าใด” '
        '⇒ คำว่ามุม จตุภาค และเครื่องหมาย หายไปจากข้อนี้อย่างสมบูรณ์',
        '',
        '<b>ขั้นที่ 2 · 🔴 หัวใจของข้อนี้ — สมการที่ได้เป็นกำลังสองสมบูรณ์ จึงบังคับคำตอบเดียว</b>',
        '• สูตรที่ใช้ : กำจัดตัวส่วนด้วยการคูณทั้งสองข้างด้วยตัวคูณร่วมน้อยของ $3$, $5$ และ $8$ '
        'ซึ่งเท่ากับ $120$ · เลือก $120$ เพราะหารลงตัวทั้งสามตัวพอดี '
        'จึงไม่มีเศษส่วนหลงเหลือให้พลาดในบรรทัดถัดไป',
        '• แทนค่า : $120 \\cdot \\dfrac{s^{2}}{3} = 40s^{2}$ · '
        '$120 \\cdot \\dfrac{(1 - s)^{2}}{5} = 24(1 - s)^{2}$ · '
        '$120 \\cdot \\dfrac{1}{8} = 15$ ⇒ สมการกลายเป็น $40s^{2} + 24(1 - s)^{2} = 15$',
        '• กระจายอย่างระมัดระวัง : $(1 - s)^{2} = 1 - 2s + s^{2}$ '
        '⛔ ไม่ใช่ $1 - s^{2}$ · '
        '⇒ $24(1 - s)^{2} = 24 - 48s + 24s^{2}$ '
        '⇒ ทั้งสมการเป็น $40s^{2} + 24 - 48s + 24s^{2} = 15$',
        '• ยุบ : รวมพจน์ $s^{2}$ ได้ $40 + 24 = 64$ และย้าย $15$ มาทางซ้ายได้ $24 - 15 = 9$ '
        '⇒ $64s^{2} - 48s + 9 = 0$',
        '• 🔴 หยุดดูสมการนี้ให้ดีก่อนแก้ : ตรวจดิสคริมิแนนต์ก่อนเลย '
        '$b^{2} - 4ac = (-48)^{2} - 4(64)(9) = 2304 - 2304 = 0$ '
        '⇒ ดิสคริมิแนนต์เป็นศูนย์ ⇒ สมการนี้มีรากจริง<b>เพียงค่าเดียว</b>',
        '• เขียนเป็นกำลังสองสมบูรณ์เพื่อยืนยันด้วยตา : $64 = 8^{2}$ · $9 = 3^{2}$ · '
        'และพจน์กลางต้องเป็น $2(8)(3) = 48$ ซึ่งตรงกับสัมประสิทธิ์ที่เห็นพอดี '
        '⇒ $64s^{2} - 48s + 9 = (8s - 3)^{2}$ ⇒ สมการคือ $(8s - 3)^{2} = 0$ '
        '⇒ $8s - 3 = 0$ ⇒ $s = \\dfrac{3}{8}$',
        '• ⛔ สิ่งที่<b>ไม่ต้อง</b>ทำในข้อนี้ และเป็นจุดที่ทำให้ข้อนี้ยาก : '
        'ตามปกติเมื่อยุบเงื่อนไขตรีโกณแล้วได้สมการกำลังสอง เราจะได้ผู้เข้าชิงสองราย '
        'แล้วต้องไปงมหาช่วงของมุมหรือจตุภาคมาคัดออกหนึ่งราย · '
        'ข้อนี้ไม่มีขั้นตอนนั้นเลย เพราะรากซ้ำแปลว่ามีผู้เข้าชิงรายเดียวมาตั้งแต่ต้น '
        'ใครที่มัวหาข้อมูลเรื่องจตุภาคอยู่ แปลว่าอ่านสมการยังไม่ขาด',
        '• ตรวจกรอบที่ตั้งไว้ในขั้นที่ 1 ก่อนเดินต่อ : $s = \\dfrac{3}{8} = 0.375$ '
        'ซึ่งอยู่ระหว่าง $0$ กับ $1$ จริง ✓ ⇒ ค่านี้เป็นค่าที่ $\\sin^{2}\\theta$ เป็นได้จริง '
        '⇒ สรุปได้ว่า $\\sin^{2}\\theta = \\dfrac{3}{8}$ และ '
        '$\\cos^{2}\\theta = 1 - \\dfrac{3}{8} = \\dfrac{5}{8}$',
        '',
        '<b>ขั้นที่ 3 · แทนค่าในนิพจน์ที่ถาม โดยจับตาที่ตัวส่วนซึ่งถูกยกกำลังสองแล้ว</b>',
        '• สูตรที่ใช้ : ยกกำลังสามของเศษส่วน $\\left(\\dfrac{m}{n}\\right)^{3} '
        '= \\dfrac{m^{3}}{n^{3}}$ แล้วจึงหารด้วยตัวหารที่โจทย์เขียนไว้',
        '• ระบุตัวเลขทุกตัวก่อนแทน : $\\sin^{2}\\theta = \\dfrac{3}{8}$ · '
        '$\\cos^{2}\\theta = \\dfrac{5}{8}$ · ตัวหารที่ต้องใช้คือ $9$ กับ $25$ '
        '⛔ ไม่ใช่ $3$ กับ $5$ ซึ่งเป็นของเงื่อนไขเดิม',
        '• แทนค่าก้อนแรก : $\\sin^{6}\\theta = \\left(\\sin^{2}\\theta\\right)^{3} '
        '= \\left(\\dfrac{3}{8}\\right)^{3} = \\dfrac{27}{512}$ '
        '⇒ $\\dfrac{\\sin^{6}\\theta}{9} = \\dfrac{27}{512} \\cdot \\dfrac{1}{9} = \\dfrac{3}{512}$',
        '• แทนค่าก้อนที่สอง : $\\cos^{6}\\theta = \\left(\\cos^{2}\\theta\\right)^{3} '
        '= \\left(\\dfrac{5}{8}\\right)^{3} = \\dfrac{125}{512}$ '
        '⇒ $\\dfrac{\\cos^{6}\\theta}{25} = \\dfrac{125}{512} \\cdot \\dfrac{1}{25} = \\dfrac{5}{512}$',
        '• ยุบ : ตัวส่วนตรงกันอยู่แล้ว จึงบวกเศษได้ทันที '
        '$\\dfrac{3}{512} + \\dfrac{5}{512} = \\dfrac{8}{512}$ '
        '⇒ ตัดทอนด้วย $8$ ทั้งเศษและส่วนได้ $\\dfrac{1}{64}$',
        '',
        '<b>ขั้นที่ 4 · อ่านโครงสร้างซ้ำอีกรอบ เพื่อยืนยันว่าเลขสวยไม่ได้มาเพราะบังเอิญ</b>',
        '• ทำไมต้องอ่านซ้ำ : ตัวเลขที่ออกมาลงตัวเกินไป ($\\dfrac{3}{512}$ กับ $\\dfrac{5}{512}$ '
        'บวกกันแล้วได้ $\\dfrac{8}{512}$ พอดี) เป็นสัญญาณว่ามีโครงสร้างซ่อนอยู่ '
        'และการเห็นโครงสร้างนั้นจะทำให้เข้าใจว่าโจทย์ถูกออกแบบมาอย่างไร',
        '• สูตรที่ใช้ : การอ่านเศษส่วนแบบดึงตัวประกอบร่วม '
        '$\\dfrac{u^{2}}{p} = u \\cdot \\dfrac{u}{p}$ และ '
        '$\\dfrac{u^{3}}{p^{2}} = u \\cdot \\left(\\dfrac{u}{p}\\right)^{2}$',
        '• ระบุตัวแปรก่อนแทนค่า : ที่ $s = \\dfrac{3}{8}$ ให้คิดค่าของ '
        '$\\dfrac{s}{3}$ กับ $\\dfrac{1 - s}{5}$ · '
        '$\\dfrac{s}{3} = \\dfrac{3}{8} \\div 3 = \\dfrac{1}{8}$ และ '
        '$\\dfrac{1 - s}{5} = \\dfrac{5}{8} \\div 5 = \\dfrac{1}{8}$ '
        '⇒ 🔴 ทั้งสองก้อนเท่ากันพอดี เรียกค่านี้ว่า $t = \\dfrac{1}{8}$',
        '• แทนค่าแล้วยุบเงื่อนไขเดิม : $\\dfrac{s^{2}}{3} + \\dfrac{(1 - s)^{2}}{5} '
        '= s \\cdot t + (1 - s) \\cdot t = t\\left[s + (1 - s)\\right] = t = \\dfrac{1}{8}$ ✓ '
        'ตรงกับที่โจทย์ให้มาพอดี โดยไม่ต้องกระจายอะไรเลย',
        '• แทนค่าแล้วยุบนิพจน์ที่ถามด้วยกลไกเดียวกัน : $\\dfrac{s^{3}}{9} + \\dfrac{(1 - s)^{3}}{25} '
        '= s \\cdot t^{2} + (1 - s) \\cdot t^{2} = t^{2}\\left[s + (1 - s)\\right] = t^{2} '
        '= \\left(\\dfrac{1}{8}\\right)^{2} = \\dfrac{1}{64}$ ✓ ตรงกับขั้นที่ 3',
        '• 📌 ความหมายที่ได้จากบรรทัดนี้ : คำตอบคือ<b>กำลังสอง</b>ของค่าที่โจทย์ให้ '
        'ไม่ใช่กำลังสาม · เหตุผลอยู่ที่ตัวส่วน $9$ กับ $25$ เป็นกำลังสองของ $3$ กับ $5$ '
        'จึงกลายเป็น $t^{2}$ · ถ้าโจทย์อยากได้ $t^{3} = \\dfrac{1}{512}$ จริง ๆ '
        'โจทย์ต้องเขียนนิพจน์ว่า $\\dfrac{\\sin^{8}\\theta}{27} + \\dfrac{\\cos^{8}\\theta}{125}$ '
        'ซึ่งเป็นคนละนิพจน์กับที่ถาม',
        '',
        '<b>ขั้นที่ 5 · ปิดประเด็นเรื่องจตุภาคให้ขาด</b>',
        '• คำถามที่ค้างอยู่ในใจ : ในเมื่อโจทย์ไม่บอกช่วงของ $\\theta$ '
        'แล้วจะมั่นใจได้อย่างไรว่าคำตอบมีค่าเดียว ไม่ใช่ว่าบางมุมได้ค่าหนึ่ง บางมุมได้อีกค่าหนึ่ง',
        '• ตอบด้วยเหตุผลเรื่องกำลังคู่ : ขั้นที่ 2 บังคับ $\\sin^{2}\\theta = \\dfrac{3}{8}$ '
        'ซึ่งแปลว่า $\\sin\\theta = \\sqrt{\\dfrac{3}{8}}$ หรือ $\\sin\\theta = -\\sqrt{\\dfrac{3}{8}}$ '
        'และคู่กันก็มีสองทางเลือกสำหรับ $\\cos\\theta$ ⇒ รวมเป็นสี่แบบตามสี่จตุภาค · '
        'แต่นิพจน์ที่ถามใช้เพียง $\\sin^{6}\\theta$ กับ $\\cos^{6}\\theta$ '
        'ซึ่งเป็นกำลังคู่ ⇒ ทั้งสี่แบบให้ค่าเดียวกันหมด คือ $\\dfrac{1}{64}$',
        '• ตรวจว่ามีมุมอยู่จริง ไม่ใช่แค่เลขลอย ๆ : ค่า $\\dfrac{3}{8}$ อยู่ในช่วง $[0,\\ 1]$ '
        'จึงมีมุมจริงรองรับ เช่นมุมแหลมที่ $\\sin\\theta = \\sqrt{\\dfrac{3}{8}} \\approx 0.6124$ '
        'ซึ่งมีขนาดประมาณ $37.76^{\\circ}$ · '
        'มุมอื่น ๆ ที่ใช้ได้คือมุมที่สะท้อนของมุมนี้ไปยังอีกสามจตุภาค '
        '⇒ เงื่อนไขของโจทย์มีมุมสอดคล้องอยู่จริงและทุกมุมให้คำตอบเดียวกัน',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · สร้างค่าจริงของ $\\sin\\theta$ กับ $\\cos\\theta$ ขึ้นมาก่อน '
        'แล้วแทนกลับเข้าไปทดสอบทั้งเงื่อนไขและนิพจน์ที่ถาม '
        '⛔ โดยไม่ย้อนกลับไปแตะสมการกำลังสองในขั้นที่ 2 อีกเลย)</b>',
        '• แนวคิดของการตรวจ : ขั้นที่ 1 ถึง 5 เดินจากเงื่อนไขไป<b>สร้าง</b>คำตอบ '
        'ส่วนรอบนี้เดินย้อนศร คือหยิบมุมที่เป็นรูปธรรมขึ้นมาหนึ่งมุมก่อน '
        'แล้ว<b>ทดสอบ</b>ว่ามันผ่านทุกประโยคของโจทย์หรือไม่ · '
        'ถ้าผ่าน แปลว่าคำตอบใช้ได้จริงโดยไม่ต้องเชื่อบรรทัดใดในเส้นทางเดิมเลย',
        '• สร้างค่าจริงขึ้นมา : เลือกมุมในจตุภาคที่ $1$ โดยให้ '
        '$\\sin\\theta = \\sqrt{\\dfrac{3}{8}}$ และ $\\cos\\theta = \\sqrt{\\dfrac{5}{8}}$ · '
        'ตรวจก่อนว่าคู่นี้ถูกกฎหมาย $\\sin^{2}\\theta + \\cos^{2}\\theta '
        '= \\dfrac{3}{8} + \\dfrac{5}{8} = 1$ ✓ ⇒ มีมุมจริงที่ให้ค่าคู่นี้',
        '• ทดสอบประโยคที่โจทย์เขียนไว้ : $\\sin^{4}\\theta = \\left(\\dfrac{3}{8}\\right)^{2} '
        '= \\dfrac{9}{64}$ ⇒ $\\dfrac{\\sin^{4}\\theta}{3} = \\dfrac{9}{64} \\div 3 = \\dfrac{3}{64}$ · '
        '$\\cos^{4}\\theta = \\left(\\dfrac{5}{8}\\right)^{2} = \\dfrac{25}{64}$ '
        '⇒ $\\dfrac{\\cos^{4}\\theta}{5} = \\dfrac{25}{64} \\div 5 = \\dfrac{5}{64}$ '
        '⇒ บวกกันได้ $\\dfrac{3}{64} + \\dfrac{5}{64} = \\dfrac{8}{64} = \\dfrac{1}{8}$ ✓ '
        'ตรงกับเงื่อนไขที่โจทย์ให้ทุกประการ',
        '• ทดสอบนิพจน์ที่ถามจากค่าจริงชุดเดียวกัน : $\\dfrac{\\sin^{6}\\theta}{9} '
        '= \\dfrac{27/512}{9} = \\dfrac{3}{512}$ และ $\\dfrac{\\cos^{6}\\theta}{25} '
        '= \\dfrac{125/512}{25} = \\dfrac{5}{512}$ ⇒ รวมได้ $\\dfrac{8}{512} = \\dfrac{1}{64}$ ✓',
        '• เปลี่ยนจตุภาคแล้วทดสอบซ้ำเพื่อปิดประตูให้สนิท : ใช้ '
        '$\\sin\\theta = \\sqrt{\\dfrac{3}{8}}$ แต่ให้ $\\cos\\theta = -\\sqrt{\\dfrac{5}{8}}$ '
        '(เป็นมุมในจตุภาคที่ $2$) · ทุกเลขชี้กำลังในข้อนี้เป็นเลขคู่ '
        'จึงกลืนเครื่องหมายลบทิ้งหมด ⇒ ได้ $\\dfrac{1}{8}$ และ $\\dfrac{1}{64}$ เท่าเดิมทั้งคู่ ✓ '
        '⇒ ยืนยันด้วยการทดลองจริงว่าคำตอบ<b>ไม่ขึ้นกับจตุภาค</b>',
        '• 📌 เสริมด้วยการตรวจชั้นที่สองซึ่งไม่ต้องแทนตัวเลขเลย : '
        'อสมการโคชี-ชวาร์ซให้ $\\dfrac{s^{2}}{3} + \\dfrac{(1 - s)^{2}}{5} '
        '\\ge \\dfrac{\\left[s + (1 - s)\\right]^{2}}{3 + 5} = \\dfrac{1}{8}$ เสมอ '
        '⇒ ค่าต่ำสุดที่ฝั่งซ้ายเป็นไปได้คือ $\\dfrac{1}{8}$ '
        'ซึ่งเท่ากับค่าที่โจทย์ยื่นมาพอดี ⇒ สถานการณ์นี้คือกรณีที่เท่ากัน '
        'ซึ่งเกิดขึ้นก็ต่อเมื่อ $\\dfrac{s}{3} = \\dfrac{1 - s}{5}$ ⇒ $5s = 3 - 3s$ '
        '⇒ $s = \\dfrac{3}{8}$ · '
        'ได้ค่าเดิมโดยไม่แตะการกระจายและไม่แตะสมการกำลังสองเลยแม้แต่บรรทัดเดียว '
        '⇒ เป็นหลักฐานชั้นที่สองว่าเงื่อนไขบังคับคำตอบไว้ค่าเดียวจริง',
        '',
        '✅ <b>คำตอบ</b> แทน $s = \\sin^{2}\\theta$ แล้วเงื่อนไขยุบเป็น $(8s - 3)^{2} = 0$ '
        'ซึ่งบังคับ $\\sin^{2}\\theta = \\dfrac{3}{8}$ และ $\\cos^{2}\\theta = \\dfrac{5}{8}$ เพียงค่าเดียว '
        '⇒ $\\dfrac{\\sin^{6}\\theta}{9} + \\dfrac{\\cos^{6}\\theta}{25} '
        '= \\dfrac{3}{512} + \\dfrac{5}{512} = \\dfrac{1}{64}$ → <b>ตัวเลือก 2</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เห็นโจทย์ตรีโกณที่มีแต่กำลังคู่ของ $\\sin$ กับ $\\cos$ และไม่บอกช่วงของมุมมาเลย '
        'ให้อ่านออกทันทีว่าโจทย์ตั้งใจให้ตอบได้โดยไม่ต้องรู้จตุภาค '
        '⇒ ตั้ง $s = \\sin^{2}\\theta$ ได้เลยโดยไม่ต้องลังเล '
        'แล้วทั้งข้อจะกลายเป็นพีชคณิตของตัวแปรตัวเดียว · '
        'กลับกัน ถ้าโจทย์แบบนี้อุตส่าห์บอกช่วงมาให้ ต้องสงสัยทันทีว่ามีพจน์กำลังคี่ซ่อนอยู่ที่ไหนสักแห่ง',
        '• เจอรูป $\\dfrac{a^{2}}{p} + \\dfrac{b^{2}}{q} = \\dfrac{1}{p + q}$ '
        'โดยที่ $a + b = 1$ ให้จำลายเซ็นนี้ไว้ว่าเป็นกรณีที่เท่ากันของอสมการโคชี-ชวาร์ซ '
        '⇒ ใช้เงื่อนไขเท่ากัน $\\dfrac{a}{p} = \\dfrac{b}{q}$ หาค่าได้ในบรรทัดเดียว '
        'โดยไม่ต้องกระจายและไม่ต้องแก้สมการกำลังสองเลย · '
        'ของแถมคือรู้ทันทีว่าคำตอบมีค่าเดียว เพราะกรณีที่เท่ากันเกิดได้ที่จุดเดียว',
        '• ก่อนแก้สมการกำลังสองทุกครั้ง ให้คิดดิสคริมิแนนต์ $b^{2} - 4ac$ ก่อนหนึ่งบรรทัด · '
        'ถ้าได้ศูนย์ แปลว่ามีรากเดียวและฝั่งซ้ายเป็นกำลังสองสมบูรณ์ '
        '⇒ ประหยัดเวลาไปทั้งขั้นตอนการคัดสาขา และที่สำคัญกว่านั้นคือกันไม่ให้เผลอ<b>สร้าง</b>รากที่สองขึ้นมาเอง '
        'แล้วเสียเวลาไปหาข้อมูลที่โจทย์ไม่เคยให้มาเพื่อคัดมันทิ้ง',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\dfrac{1}{512}$ เพราะเดาแพตเทิร์นจากเลขชี้กำลังแทนการคำนวณ · '
        'เส้นทางพลาดคือเห็นว่าเงื่อนไขให้ $\\dfrac{1}{8} = \\dfrac{1}{3 + 5}$ '
        'แล้วเห็นเลขชี้กำลังของนิพจน์ที่ถามเป็น $6 = 2 \\times 3$ '
        'จึงสรุปเอาเองว่าคำตอบต้องเป็น $\\dfrac{1}{(3 + 5)^{3}} = \\dfrac{1}{512}$ · '
        'ต้นเหตุคือไปนับ<b>เลขชี้กำลังของฟังก์ชัน</b>แทนที่จะนับกำลังของ<b>ตัวส่วน</b> · '
        'ค่านี้ผิดจริงและพิสูจน์ได้จากขั้นที่ 4 ซึ่งแสดงว่า '
        'ผลบวกยุบเป็น $t^{k}$ โดย $k$ คือกำลังของตัวส่วน ไม่ใช่ครึ่งหนึ่งของเลขชี้กำลัง · '
        'ที่นี่ตัวส่วนคือ $9 = 3^{2}$ กับ $25 = 5^{2}$ ⇒ ได้ $t^{2} = \\dfrac{1}{64}$ · '
        'นิพจน์ที่มีค่า $\\dfrac{1}{512}$ จริง ๆ คือ '
        '$\\dfrac{\\sin^{8}\\theta}{27} + \\dfrac{\\cos^{8}\\theta}{125}$ '
        'ซึ่งเปลี่ยนทั้งเลขชี้กำลังและตัวส่วนไปพร้อมกัน ⇒ ไม่ใช่สิ่งที่โจทย์ถาม',
        '• ได้ค่า $\\dfrac{17}{256}$ เพราะหา $s = \\dfrac{3}{8}$ มาถูกต้องทุกบรรทัด '
        'แต่ตอนแทนค่ากลับหยิบตัวหารของ<b>เงื่อนไขเดิม</b>มาใช้ คือใช้ $3$ กับ $5$ '
        'แทนที่จะเป็น $9$ กับ $25$ ⇒ ได้ $\\dfrac{27/512}{3} + \\dfrac{125/512}{5} '
        '= \\dfrac{9}{512} + \\dfrac{25}{512} = \\dfrac{34}{512} = \\dfrac{17}{256}$ · '
        'ต้นเหตุคืออ่านโจทย์ครั้งเดียวตอนเริ่มต้น แล้วทำงานจากภาพจำของเงื่อนไข '
        'โดยไม่กลับไปอ่านบรรทัดที่ถามซ้ำก่อนแทนค่า · '
        'ค่านี้ผิดจริงและพิสูจน์ได้ทันทีด้วยการเทียบตัวเลข '
        'เพราะนิพจน์ที่โจทย์เขียนมีตัวส่วนเป็น $9$ กับ $25$ ชัดเจน '
        'และตัวเลขที่ได้ก็ใหญ่กว่าคำตอบจริงราวสี่เท่า ซึ่งเป็นผลจากการหารด้วยของที่เล็กกว่าที่ควร · '
        'วิธีกันคือเขียนตัวหารที่ถูกต้องลงบนกระดาษก่อนแทนค่าเสมอ',
        '• ได้ค่า $\\dfrac{1}{8}$ เพราะคิดว่านิพจน์ที่ถามเป็นเพียงการเขียนเงื่อนไขเดิมใหม่ '
        'จึงตอบค่าเดิมกลับไปโดยไม่หา $\\sin^{2}\\theta$ เลยสักครั้ง · '
        'ต้นเหตุคือเห็นหน้าตาสองก้อนคล้ายกันมาก คือเป็นผลบวกของกำลังคู่หารด้วยค่าคงตัวเหมือนกัน '
        'จึงเหมารวมว่าเป็นก้อนเดียวกัน · '
        'ค่านี้ผิดจริงและพิสูจน์ได้โดยไม่ต้องแก้สมการอะไรเลย '
        'เพราะสองนิพจน์มีดีกรีต่างกัน (กำลัง $4$ กับกำลัง $6$) จึงเป็นคนละฟังก์ชันกัน · '
        'ตรวจซ้ำด้วยตัวเลขจริงก็ได้ ที่ $\\sin^{2}\\theta = \\dfrac{3}{8}$ '
        'เงื่อนไขให้ค่า $\\dfrac{1}{8}$ ส่วนนิพจน์ที่ถามให้ค่า $\\dfrac{1}{64}$ '
        'ซึ่งเป็นกำลังสองของกัน ไม่ใช่ค่าเท่ากัน',
        '• เสียเวลาไปทั้งข้อกับการงมหาจตุภาค แล้วสรุปว่าโจทย์ให้ข้อมูลไม่พอ '
        'จึงเดาคำตอบส่งไปเฉย ๆ · '
        'ต้นเหตุคือความเคยชินจากโจทย์ตระกูลใกล้เคียงที่ยุบแล้วได้สองรากเสมอ '
        'จนเผลอคิดว่าทุกข้อต้องมีขั้นตอนคัดเครื่องหมาย · '
        'ความจริงคือขั้นที่ 2 ให้รากซ้ำ ⇒ ไม่มีสาขาให้คัดตั้งแต่ต้น '
        'และขั้นที่ 5 พิสูจน์แล้วว่าทั้งสี่จตุภาคให้ค่าเดียวกันคือ $\\dfrac{1}{64}$ '
        'เพราะทุกเลขชี้กำลังในข้อนี้เป็นเลขคู่ · '
        'วิธีกันคือกวาดตาดูเลขชี้กำลังทั้งข้อก่อนลงมือ ถ้าเป็นเลขคู่หมด '
        'ให้ตัดเรื่องเครื่องหมายทิ้งไปได้เลยและอย่าไปรออีก',
        '• ได้ว่า “ไม่มีคำตอบจริง” เพราะกระจาย $(1 - s)^{2}$ ผิดเป็น $1 - s^{2}$ '
        '⇒ สมการกลายเป็น $40s^{2} + 24 - 24s^{2} = 15$ ⇒ $16s^{2} = -9$ '
        '⇒ $s^{2} = -\\dfrac{9}{16}$ ซึ่งไม่มีรากจริง จึงคิดว่าโจทย์ผิด · '
        'ต้นเหตุคือลืมพจน์กลาง $-2s$ ในการกระจายกำลังสองของผลต่าง · '
        'ค่านี้ผิดจริงและจับได้ทันทีด้วยการทดสอบด้วยเลขง่าย ๆ '
        'เช่นแทน $s = 1$ ลงในของจริง $(1 - 1)^{2} = 0$ '
        'แต่สูตรที่กระจายผิดให้ $1 - 1^{2} = 0$ เท่ากัน จึงจับไม่ได้ '
        'ต้องลอง $s = 2$ ซึ่งของจริงได้ $(1 - 2)^{2} = 1$ ส่วนของผิดได้ $1 - 4 = -3$ '
        '⇒ ต่างกันชัดเจน ⇒ ยืนยันว่ากระจายผิด · '
        'วิธีกันคือกระจายกำลังสองของผลต่างทีละพจน์เสมอ ⛔ ห้ามลัด',
    ],
    'V.mold: G = a single symbolic condition, the weighted quartic sum sin^4(theta)/3 + cos^4(theta)/5 = '
    '1/8, handed over with no range for theta anywhere in the statement, an absence that is itself a piece '
    'of information because the right hand side 1/8 is exactly 1/(3+5), the sum of the two denominators / '
    'A = the value of the companion weighted sextic sum sin^6(theta)/9 + cos^6(theta)/25, whose denominators '
    'are the squares of the original two, offered as one of four positive rationals / '
    'M = M-WEIGHTED-POWER-PERFECT-SQ-FORCE, that is: substitute s = sin^2(theta) so that cos^2(theta) '
    'becomes 1 - s and the whole item turns into algebra in one variable on the interval from 0 to 1, clear '
    'the denominators by multiplying through by 120 to reach 40s^2 + 24(1-s)^2 = 15, expand and collect into '
    '64s^2 - 48s + 9 = 0, notice that the discriminant is exactly zero so the left side is the perfect '
    'square (8s - 3)^2 and the condition therefore pins s = 3/8 as a repeated root with no branch to select, '
    'and finally cube 3/8 and 5/8 and divide by 9 and 25 rather than by 3 and 5, which yields 3/512 + 5/512 '
    '= 1/64; the same value falls out structurally because s/3 and (1-s)/5 are both equal to t = 1/8, so the '
    'condition collapses to t and the requested expression collapses to t^2. '
    'Rubric F3 C3 P3 T3 L0 = 12/15, which reaches the threshold of 12 with T at its ceiling and therefore '
    'clears the very-hard gate -> level: ยากมาก. '
    'F = 3 because three separate knowledge blocks must all be owned before the item moves: the Pythagorean '
    'identity in its rearranged form together with the range restriction it carries, the discriminant test '
    'and the perfect-square factorisation of a quadratic, and the equality case of the two-term '
    'Cauchy-Schwarz inequality that explains why the given constant is the minimum; F is not higher because '
    '3 is the ceiling. C = 3 because only one of the three keys is handed over: the equation is given, but '
    'the constraint 0 <= s <= 1 that certifies the root as a genuine value of sin^2 and the structural link '
    'between the denominators 3 and 5 and the denominators 9 and 25 both have to be manufactured by the '
    'student, and without the second of those the substitution step silently produces a value that is '
    'present among the four listed ratios. P = 3 for an unreorderable chain of eight stages, substitution, '
    'clearing by 120, expansion of a squared difference, collection, the discriminant test, the '
    'factorisation, the cubing of two fractions with denominator 512 and the final reduction, which matches '
    'the depth that earned P = 3 for the seven-stage chain of the q144 precedent. T = 3 because three '
    'independent turning points sit in the item and missing any one of them lands the student on a value '
    'that is actually printed on the page: first that the quadratic is a perfect square so the condition '
    'forces one value and the habitual branch-selection step does not exist here, second that the requested '
    'denominators are the squares of the original ones so that reusing 3 and 5 gives 17/256, and third that '
    'the collapse is to t^2 and not t^3 so that the pattern guess 1/(3+5)^3 gives 1/512. L = 0 because the '
    'statement is purely symbolic with no figure to draw, no scene to model and no graph to picture before '
    'the algebra can start, which is the one dimension where this item is genuinely cheap. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): in the q164 block, factor of the numerator of s**2/3 + (1-s)**2/5 - 1/8 returns '
    '(8*s - 3)**2/120, which is the machine proof that the condition is a perfect square rather than a '
    'quadratic with two roots; solve of the same equation returns a list of length exactly 1 whose only '
    'entry is 3/8, and the length was asserted, so the uniqueness claim that the whole explanation rests on '
    'is checked by machine and not by eye; at that root, s**3/9 + (1-s)**3/25 evaluates to exactly 1/64, '
    'matching the stored key, and the choice list was passed through the ascending-order check. The block '
    'was re-run in this session and extended: discriminant(64*s**2 - 48*s + 9, s) returns 0; minimum of '
    's**2/3 + (1-s)**2/5 over the closed interval from 0 to 1 returns 1/8, which is the machine statement '
    'that the constant handed over by the problem is the Cauchy-Schwarz bound and hence the equality case; '
    's/3 and (1-s)/5 both evaluate to 1/8 at the root, confirming the structural reading of step 4; and '
    'solve of the original trigonometric equation in theta returns four families, one per quadrant, all of '
    'which were evaluated to confirm that the requested expression is 1/64 at every one of them. Every wrong '
    'value in the pitfalls block was computed by machine from its named error path rather than invented: '
    'keeping the original denominators gives s**3/3 + (1-s)**3/5 = 17/256; the expression that really equals '
    '1/512 is s**4/27 + (1-s)**4/125, which sympy confirms equals 1/(3+5)**3 and is not the expression on '
    'the page; the condition itself evaluates to 1/8, the square root of the answer rather than the answer; '
    'and the mis-expansion of (1-s)^2 as 1 - s^2 turns the equation into 16*s**2 = -9, which sympy reports '
    'as having no real solution, so that path refutes itself. The four sign combinations built from '
    'sin = +/-sqrt(3/8) and cos = +/-sqrt(5/8) were each substituted directly and all four return 1/8 for '
    'the condition and 1/64 for the requested expression, which is the machine form of the '
    'quadrant-independence argument. '
    'Collision sweep on 6457 de-duplicated items (86 files: the bank sets directory plus k1 out plus k2 '
    'out), run directly in this session because no collide_b21.py exists in the tree: the scan for a stem '
    'that places a fourth power of sine or cosine over a constant returns exactly 1 item in the whole '
    'corpus, and the scan for a sixth power over a constant returns 0, so the requested expression itself '
    'is untouched anywhere. The one near neighbour is recorded here rather than hidden: pat1-2557-11-q29 '
    'hands over sin^4(x)/5 + cos^4(x)/7 = 1/12, the same equality-case surface with different weights, but '
    'it asks for sin^2(2x)/5 + cos^2(2x)/7, so its A is a double-angle expression and its published '
    'solution runs on the double-angle formulas, whereas this item keeps the same even-power family one '
    'degree higher and squares the denominators, so G overlaps in shape while A and M both differ and the '
    'reused constants are different as well; that item is also graded ปานกลาง, which is consistent with its '
    'shorter chain. Two further relatives were checked and cleared: gen-chap-07-trigonometry-q079, which '
    'sets 8(sin^8 x + cos^8 x) = 1 and asks for the number of solutions, shares only the idea of an '
    'inequality attaining its bound, but its weights are equal so the equality point is the symmetric one '
    'and its A is a count rather than a value; and chap-07-trigonometry-q141, the only other stem that '
    'carries a sixth-power sum, is a pure identity to be simplified with no unknown to solve for. The pair '
    'of a repeated-root condition crossed with chapter 7 returns 0 items, and among the 122 items carrying '
    'subtopic 7.4 none forces its answer through a zero discriminant. Choices are ordered by numerical '
    'value from small to large, 1/512 about 0.00195, then 1/64 = 0.015625, then 17/256 about 0.0664, then '
    '1/8 = 0.125, so the answer slot is forced by that rule and was not positioned by hand.',
)

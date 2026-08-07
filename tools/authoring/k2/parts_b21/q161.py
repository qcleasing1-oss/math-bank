# -*- coding: utf-8 -*-
add_fill(
    161,
    ['7.3'],
    'ยาก',
    'กำหนดให้ $f(x) = \\dfrac{30}{\\left(\\sin^2 x + 2\\right)\\left(\\cos^2 x + 2\\right)}$ '
    'สำหรับทุกจำนวนจริง $x$ ผลบวกของค่าสูงสุดที่เป็นไปได้ของ $f(x)$ '
    'กับค่าต่ำสุดที่เป็นไปได้ของ $f(x)$ เท่ากับเท่าใด',
    '49/5',
    ['49/5', '\\dfrac{49}{5}', '9.8'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เอกลักษณ์พีทาโกรัส $\\sin^2 x + \\cos^2 x = 1$ เป็นจริงสำหรับทุกจำนวนจริง $x$ '
        '· เหตุผลมาจากวงกลมหนึ่งหน่วย คือจุด $\\left(\\cos x,\\ \\sin x\\right)$ '
        'อยู่ห่างจากจุดกำเนิดเป็นระยะ $1$ เสมอ แล้วใช้ระยะทางระหว่างจุดสองจุด '
        '⇒ ประโยชน์ที่แท้จริงของเอกลักษณ์นี้คือ<b>ยุบของสองตัวให้เหลือตัวเดียว</b> '
        'พอเห็น $\\sin^2$ กับ $\\cos^2$ อยู่ในนิพจน์เดียวกันเมื่อไร ให้นึกถึงมันก่อนเสมอ',
        '• ช่วงค่าของ $\\sin^2 x$ : จาก $-1 \\le \\sin x \\le 1$ เมื่อยกกำลังสองจะได้ '
        '$0 \\le \\sin^2 x \\le 1$ และปลายทั้งสองข้างเกิดขึ้นจริง '
        '(ที่ $x = 0$ ได้ $0$ · ที่ $x = \\dfrac{\\pi}{2}$ ได้ $1$) · '
        '⛔ กับดักที่ต้องปิดตั้งแต่บรรทัดนี้ : $\\sin^2 x$ กับ $\\cos^2 x$ '
        '<b>ไม่เป็นอิสระต่อกัน</b> เพราะบวกกันได้ $1$ พอดี '
        '⇒ จะบอกว่าแต่ละตัววิ่งได้ทั้งช่วง $[0, 1]$ พร้อม ๆ กันไม่ได้',
        '• พาราโบลา $w(1 - w) = -w^2 + w$ : สัมประสิทธิ์ของ $w^2$ เป็นลบ ⇒ เป็นพาราโบลาคว่ำ '
        '· รากของมันคือ $w = 0$ กับ $w = 1$ ⇒ จุดยอดอยู่กึ่งกลางรากทั้งสอง คือที่ $w = \\dfrac{1}{2}$ '
        '⇒ ค่าที่จุดยอดเท่ากับ $\\dfrac{1}{2}\\left(1 - \\dfrac{1}{2}\\right) = \\dfrac{1}{4}$ '
        'ซึ่งเป็นค่าสูงสุดของมัน · ส่วนบนช่วงปิด $[0, 1]$ ค่าที่ต่ำที่สุดอยู่ที่ปลายช่วง คือ $0$',
        '• เศษส่วนที่<b>เศษเป็นค่าคงตัวบวก</b>และตัวส่วนเป็นบวกตลอด : ถ้า $k > 0$ และ $D > 0$ '
        'แล้ว $\\dfrac{k}{D}$ จะเล็กลงเมื่อ $D$ โตขึ้น และโตขึ้นเมื่อ $D$ เล็กลง '
        '⇒ ตัวส่วน<b>น้อยที่สุด</b>ให้ค่าของเศษส่วน<b>มากที่สุด</b> '
        'และตัวส่วนมากที่สุดให้ค่าของเศษส่วนน้อยที่สุด ⛔ ทิศทางตรงนี้กลับด้านกับสัญชาตญาณ',
        '• ค่าสูงสุดหรือค่าต่ำสุดจะเรียกว่าเป็นค่าสุดขีดได้ ก็ต่อเมื่อ<b>มี $x$ จริงที่ทำให้เกิดค่านั้น</b> '
        '⇒ หาขอบได้แล้วต้องย้อนไปชี้ $x$ ที่ทำให้ถึงขอบเสมอ ถ้าชี้ไม่ได้แปลว่าขอบที่ได้มาหลวมเกินจริง '
        'และค่าที่รายงานจะไม่ใช่ค่าที่ฟังก์ชันรับได้',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $f(x) = \\dfrac{30}{\\left(\\sin^2 x + 2\\right)\\left(\\cos^2 x + 2\\right)}$ '
        'โดยที่ $x$ เป็นจำนวนจริงใดก็ได้ ไม่มีการจำกัดช่วง',
        '• เศษเป็นค่าคงตัว $30$ ⇒ ไม่ขยับตาม $x$ เลย · ส่วนตัวส่วนเป็นผลคูณของสองก้อน '
        'ก้อนละ “กำลังสองของฟังก์ชันตรีโกณ บวก $2$”',
        '• ตรวจความมีอยู่ของฟังก์ชันก่อน : $\\sin^2 x \\ge 0$ ⇒ $\\sin^2 x + 2 \\ge 2$ '
        'และในทำนองเดียวกัน $\\cos^2 x + 2 \\ge 2$ ⇒ ตัวส่วนมีค่าอย่างน้อย $4$ '
        'จึงไม่มีทางเป็นศูนย์ ⇒ $f$ นิยามได้ทุกจำนวนจริง และ $f(x) > 0$ เสมอ',
        '• สังเกตหน้าตาก่อนลงมือ : ในตัวส่วนมีตัวแปรตรีโกณโผล่มาสองหน้า คือ $\\sin^2 x$ กับ '
        '$\\cos^2 x$ แต่สองหน้านี้ผูกกันด้วยเอกลักษณ์พีทาโกรัส ⇒ เดาได้ล่วงหน้าตั้งแต่ยังไม่คำนวณว่า '
        'พอกระจายวงเล็บออกมา พจน์ที่เป็นเชิงเส้นของทั้งคู่จะยุบรวมกันเป็นค่าคงตัว '
        'แล้วตัวส่วนจะเหลือก้อนที่ขยับได้เพียงก้อนเดียว',
        '• สังเกตอีกอย่างซึ่งคนมักข้าม : เศษเป็นค่าคงตัว ⇒ งานทั้งหมดของข้อนี้คือ'
        '<b>หาช่วงของตัวส่วน</b> แล้วค่อยพลิกกลับตอนท้าย ⛔ ไม่ใช่ไล่หาค่าสุดขีดของ $f$ ตรง ๆ',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาผลบวกของค่าสูงสุดที่เป็นไปได้ของ $f(x)$ กับค่าต่ำสุดที่เป็นไปได้ของ $f(x)$',
        '',
        '<b>【 กระจายตัวส่วนแล้วใช้เอกลักษณ์พีทาโกรัสยุบจนเหลือตัวแปรเดียวคือ $\\sin^2 x\\cos^2 x$ '
        'จากนั้นแทน $w = \\sin^2 x$ เพื่อเปลี่ยนก้อนนั้นเป็นพาราโบลาคว่ำ $w(1 - w)$ บนช่วงปิด $[0, 1]$ '
        'อ่านช่วงของตัวส่วนออกมา แล้วพลิกกลับเป็นช่วงของ $f$ เพราะเศษเป็นค่าคงตัวบวก '
        'ปิดท้ายด้วยการบวกค่าสูงสุดกับค่าต่ำสุดเข้าด้วยกัน 】</b>',
        '',
        '<b>ขั้นที่ 1 · กระจายตัวส่วน แล้วยุบด้วยเอกลักษณ์พีทาโกรัส</b>',
        '• สูตรที่ใช้ : การกระจายวงเล็บสองวง $(a + 2)(b + 2) = ab + 2a + 2b + 4$ '
        '⛔ ห้ามลืมพจน์ไขว้ $2a$ กับ $2b$',
        '• ระบุตัวแปรก่อนแทนค่า : ให้ $a = \\sin^2 x$ และ $b = \\cos^2 x$ '
        'ทั้งคู่เป็นจำนวนจริงที่ขึ้นกับ $x$',
        '• แทนค่าลงในสูตร : $\\left(\\sin^2 x + 2\\right)\\left(\\cos^2 x + 2\\right) '
        '= \\sin^2 x\\cos^2 x + 2\\sin^2 x + 2\\cos^2 x + 4$',
        '• ยุบพจน์กลางสองพจน์ : $2\\sin^2 x + 2\\cos^2 x = 2\\left(\\sin^2 x + \\cos^2 x\\right) '
        '= 2(1) = 2$ ⇒ นี่คือจุดที่เอกลักษณ์พีทาโกรัสทำงาน',
        '• ⇒ ตัวส่วน $= \\sin^2 x\\cos^2 x + 2 + 4 = \\sin^2 x\\cos^2 x + 6$',
        '• ⇒ เขียนฟังก์ชันใหม่ได้เป็น $f(x) = \\dfrac{30}{\\sin^2 x\\cos^2 x + 6}$ '
        '⇒ ตอนนี้ทั้งข้อเหลือของที่ขยับได้เพียงก้อนเดียว คือ $\\sin^2 x\\cos^2 x$ ตรงกับที่คาดไว้',
        '• ตรวจย้อนกลับทันทีกันหลงทาง : แทน $x = 0$ ลงรูปเดิมได้ตัวส่วน $(0 + 2)(1 + 2) = 6$ '
        'และแทน $x = 0$ ลงรูปที่ยุบแล้วได้ $0 + 6 = 6$ ✓ ตรงกันพอดี',
        '',
        '<b>ขั้นที่ 2 · หาช่วงของ $\\sin^2 x\\cos^2 x$ ⛔ จุดที่พลาดกันมากที่สุดของทั้งข้อ</b>',
        '• ให้ $w = \\sin^2 x$ ⇒ จากบล็อกความรู้พื้นฐานได้ $0 \\le w \\le 1$',
        '• ใช้เอกลักษณ์พีทาโกรัสอีกครั้งเพื่อกำจัดตัวแปรที่เหลือ : $\\cos^2 x = 1 - \\sin^2 x = 1 - w$',
        '• แทนค่า : $\\sin^2 x\\cos^2 x = w(1 - w) = -w^2 + w$ '
        '⇒ ปัญหาตรีโกณกลายเป็นปัญหาพาราโบลาบนช่วงปิด $[0, 1]$ เรียบร้อย',
        '• หาค่าสูงสุด : พาราโบลาคว่ำ รากคือ $w = 0$ กับ $w = 1$ ⇒ จุดยอดที่ $w = \\dfrac{1}{2}$ '
        '⇒ ค่าสูงสุดเท่ากับ $\\dfrac{1}{2}\\left(1 - \\dfrac{1}{2}\\right) '
        '= \\dfrac{1}{2}\\cdot\\dfrac{1}{2} = \\dfrac{1}{4}$',
        '• หาค่าต่ำสุด : บนช่วงปิดที่พาราโบลาคว่ำ ค่าน้อยที่สุดอยู่ที่ปลายช่วง '
        '⇒ ที่ $w = 0$ ได้ $0(1 - 0) = 0$ และที่ $w = 1$ ได้ $1(1 - 1) = 0$ ⇒ ค่าต่ำสุดเท่ากับ $0$',
        '• ยืนยันว่าปลายทั้งสองเกิดขึ้นจริง ⛔ ไม่ใช่แค่ขอบลอย ๆ : '
        '$w = \\dfrac{1}{2}$ คือ $\\sin^2 x = \\dfrac{1}{2}$ ซึ่งเกิดที่ $x = \\dfrac{\\pi}{4}$ '
        '· $w = 0$ คือ $\\sin^2 x = 0$ ซึ่งเกิดที่ $x = 0$',
        '• ⇒ $0 \\le \\sin^2 x\\cos^2 x \\le \\dfrac{1}{4}$',
        '• ⛔ เหตุผลที่เพดานเป็น $\\dfrac{1}{4}$ ไม่ใช่ $1$ : ถึงแม้ $\\sin^2 x$ '
        'จะขึ้นไปถึง $1$ ได้ และ $\\cos^2 x$ ก็ขึ้นไปถึง $1$ ได้ '
        'แต่ทั้งคู่<b>ขึ้นไปถึงพร้อมกันไม่ได้</b> เพราะบวกกันได้ $1$ พอดี '
        '⇒ ถ้าตัวหนึ่งเป็น $1$ อีกตัวต้องเป็น $0$ ผลคูณจึงกลายเป็น $0$ ไม่ใช่ $1$ '
        '⇒ ผลคูณจะใหญ่ที่สุดตอนที่ทั้งคู่แบ่งกันคนละครึ่งพอดี',
        '',
        '<b>ขั้นที่ 3 · แปลช่วงที่ได้ให้เป็นช่วงของตัวส่วน</b>',
        '• ตั้งชื่อตัวส่วน : ให้ $D = \\sin^2 x\\cos^2 x + 6$ '
        '⇒ จากขั้นที่ 1 ได้ $f(x) = \\dfrac{30}{D}$',
        '• บวก $6$ เข้าไปทุกจุดของอสมการในขั้นที่ 2 (การบวกค่าคงตัวไม่กลับทิศอสมการ) : '
        '$0 + 6 \\le D \\le \\dfrac{1}{4} + 6$',
        '• ยุบฝั่งขวา : $\\dfrac{1}{4} + 6 = \\dfrac{1}{4} + \\dfrac{24}{4} = \\dfrac{25}{4}$',
        '• ⇒ $6 \\le D \\le \\dfrac{25}{4}$ และปลายทั้งสองเกิดจริง '
        'คือ $x = 0$ ให้ $D = 6$ · $x = \\dfrac{\\pi}{4}$ ให้ $D = \\dfrac{25}{4}$',
        '',
        '<b>ขั้นที่ 4 · พลิกกลับเป็นค่าของ $f$ แล้วบวกสองค่าเข้าด้วยกัน</b>',
        '• เศษเป็นค่าคงตัวบวก $30$ และ $D > 0$ เสมอ ⇒ $D$ ใหญ่ ทำให้ $f$ เล็ก '
        '· $D$ เล็ก ทำให้ $f$ ใหญ่ ⇒ ปลายทั้งสองของช่วงสลับหน้าที่กัน',
        '• ค่าสูงสุดของ $f$ เกิดที่ $D$ น้อยที่สุด คือ $D = 6$ '
        '⇒ ค่าสูงสุดที่เป็นไปได้ของ $f(x)$ คือ $\\dfrac{30}{6} = 5$',
        '• ค่าต่ำสุดของ $f$ เกิดที่ $D$ มากที่สุด คือ $D = \\dfrac{25}{4}$ '
        '⇒ ค่าต่ำสุดที่เป็นไปได้ของ $f(x)$ คือ '
        '$\\dfrac{30}{\\dfrac{25}{4}} = 30 \\cdot \\dfrac{4}{25} = \\dfrac{120}{25} = \\dfrac{24}{5}$',
        '• บวกกันตามที่โจทย์สั่ง : $5 + \\dfrac{24}{5} = \\dfrac{25}{5} + \\dfrac{24}{5} '
        '= \\dfrac{25 + 24}{5} = \\dfrac{49}{5}$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่ามุมจริงลงในนิพจน์ต้นฉบับตรง ๆ '
        'โดยไม่กระจายวงเล็บ ไม่ใช้เอกลักษณ์พีทาโกรัส และไม่แตะพาราโบลาเลยสักครั้ง)</b>',
        '• แทน $x = 0$ ⇒ $\\sin^2 0 = 0$ และ $\\cos^2 0 = 1$ ⇒ '
        '$f(0) = \\dfrac{30}{(0 + 2)(1 + 2)} = \\dfrac{30}{2 \\cdot 3} = \\dfrac{30}{6} = 5$ '
        '✓ ตรงกับค่าสูงสุดที่ขั้นที่ 4 อ้างไว้ และยืนยันว่าค่านี้ $f$ รับได้จริง',
        '• แทน $x = \\dfrac{\\pi}{4}$ ⇒ $\\sin^2\\dfrac{\\pi}{4} = \\cos^2\\dfrac{\\pi}{4} '
        '= \\dfrac{1}{2}$ ⇒ $f\\left(\\dfrac{\\pi}{4}\\right) '
        '= \\dfrac{30}{\\left(\\dfrac{5}{2}\\right)\\left(\\dfrac{5}{2}\\right)} '
        '= \\dfrac{30}{\\dfrac{25}{4}} = \\dfrac{24}{5} = 4.8$ '
        '✓ ตรงกับค่าต่ำสุดที่ขั้นที่ 4 อ้างไว้ และรับได้จริงเช่นกัน',
        '• ทดจุดกลางเพื่อดูว่าเรนจ์ที่อ้างไม่หลุดขอบ : แทน $x = \\dfrac{\\pi}{6}$ ⇒ '
        '$\\sin^2\\dfrac{\\pi}{6} = \\dfrac{1}{4}$ และ $\\cos^2\\dfrac{\\pi}{6} = \\dfrac{3}{4}$ ⇒ '
        '$f\\left(\\dfrac{\\pi}{6}\\right) = \\dfrac{30}{\\left(\\dfrac{9}{4}\\right)'
        '\\left(\\dfrac{11}{4}\\right)} = \\dfrac{30}{\\dfrac{99}{16}} = \\dfrac{480}{99} '
        '= \\dfrac{160}{33} \\approx 4.85$',
        '• ค่าที่ได้อยู่ระหว่าง $4.8$ กับ $5$ พอดี ✓ ⇒ ไม่มีจุดใดทะลุขอบทั้งบนและล่าง '
        'ซึ่งเป็นหลักฐานว่าช่วง $\\left[\\dfrac{24}{5},\\ 5\\right]$ ที่อ้างไว้ไม่แคบเกินจริง '
        '· รวมกับข้อเท็จจริงว่าปลายทั้งสองเกิดขึ้นจริง จึงสรุปได้ว่าไม่กว้างเกินจริงด้วย',
        '• ⇒ ผลบวกที่ต้องการเท่ากับ $5 + \\dfrac{24}{5} = \\dfrac{49}{5}$ '
        'เท่ากับผลของขั้นที่ 4 ทุกประการ',
        '• 📌 จุดที่ทำให้การตรวจนี้เป็นอิสระจริง : ทางเดินนี้ไม่ได้กระจายวงเล็บ '
        'ไม่ได้ยุบด้วยเอกลักษณ์พีทาโกรัส และไม่ได้แตะพาราโบลา $w(1 - w)$ เลย '
        '⇒ ถ้าทางเดินหลักกระจายวงเล็บผิดหรืออ่านเพดานของผลคูณผิด ทางเดินนี้จะไม่ผิดตาม '
        '⇒ การที่สองทางเดินให้ค่าเดียวกันจึงเป็นหลักฐานที่หนักแน่น',
        '',
        '✅ <b>คำตอบ</b> ค่าสูงสุดที่เป็นไปได้ของ $f(x)$ คือ $5$ '
        'และค่าต่ำสุดที่เป็นไปได้ของ $f(x)$ คือ $\\dfrac{24}{5}$ '
        'ผลบวกจึงเท่ากับ $5 + \\dfrac{24}{5} = \\dfrac{49}{5}$',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอเศษส่วนที่เศษเป็นค่าคงตัว ให้เลิกมองเศษไปเลย แล้วทุ่มเวลาไปหาช่วงของตัวส่วนให้จบก่อน '
        'จากนั้นค่อยพลิกกลับตอนท้าย · เขียนคำเตือน “ตัวส่วนเล็ก ให้ค่าใหญ่” '
        'กำกับไว้ข้างกระดาษตั้งแต่ยังไม่เริ่มคิด จะกันการสลับทิศได้ทั้งข้อ',
        '• เห็น $\\sin^2 x$ กับ $\\cos^2 x$ อยู่ในนิพจน์เดียวกันเมื่อไร ให้แทน $w = \\sin^2 x$ '
        'แล้วเขียน $\\cos^2 x = 1 - w$ ทันที ⇒ โจทย์ตรีโกณจะกลายเป็นโจทย์พหุนามบนช่วงปิด $[0, 1]$ '
        'ซึ่งหาค่าสุดขีดได้ด้วยของสองอย่างเท่านั้น คือจุดยอดกับปลายช่วง',
        '• ทุกครั้งที่ได้ขอบบนหรือขอบล่างมา ให้ย้อนไปหา $x$ ที่ทำให้เกิดค่านั้นเสมอ '
        '· ถ้าหา $x$ ไม่ได้ แปลว่าขอบนั้นหลวมเกินจริงและยังไม่ใช่ค่าสุดขีด '
        '· ขั้นตอนนี้เองที่ทำให้จับได้ว่า $\\sin^2 x\\cos^2 x$ ขึ้นไปถึง $1$ ไม่ได้',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\dfrac{65}{7}$ เพราะกระจายและยุบตัวส่วนถูกจนได้ $\\sin^2 x\\cos^2 x + 6$ แล้ว '
        'แต่เห็นว่า $\\sin^2 x$ อยู่ใน $[0, 1]$ และ $\\cos^2 x$ ก็อยู่ใน $[0, 1]$ '
        'จึงสรุปว่าผลคูณของทั้งคู่วิ่งได้ทั้งช่วง $[0, 1]$ ⇒ ตัวส่วนอยู่ใน $[6, 7]$ '
        '⇒ ค่าสูงสุดเป็น $\\dfrac{30}{6} = 5$ และค่าต่ำสุดเป็น $\\dfrac{30}{7}$ '
        '⇒ ผลบวก $5 + \\dfrac{30}{7} = \\dfrac{65}{7} \\approx 9.29$ · '
        'ค่านี้ผิดแน่นอน เพราะการที่ตัวส่วนจะเป็น $7$ ได้ ต้องมี $x$ ที่ทำให้ '
        '$\\sin^2 x\\cos^2 x = 1$ ซึ่งบังคับให้ $\\sin^2 x = 1$ และ $\\cos^2 x = 1$ พร้อมกัน '
        'แล้วจะได้ $\\sin^2 x + \\cos^2 x = 2$ ขัดกับเอกลักษณ์พีทาโกรัสที่บอกว่าต้องเท่ากับ $1$ · '
        'วิธีกันคือจำไว้ว่าเลขสองก้อนที่ผลบวกถูกล็อกไว้ ห้ามคิดช่วงของแต่ละก้อนแยกกัน',
        '• ได้ค่า $\\dfrac{125}{13}$ เพราะจำเพดานผิดตัว คือหยิบข้อเท็จจริงที่ว่าค่าสูงสุดของ '
        '$\\sin x\\cos x$ เท่ากับ $\\dfrac{1}{2}$ มาใช้กับ $\\sin^2 x\\cos^2 x$ ตรง ๆ '
        '⇒ ตัวส่วนสูงสุดกลายเป็น $\\dfrac{1}{2} + 6 = \\dfrac{13}{2}$ '
        '⇒ ค่าต่ำสุดกลายเป็น $\\dfrac{30}{\\dfrac{13}{2}} = \\dfrac{60}{13}$ '
        '⇒ ผลบวก $5 + \\dfrac{60}{13} = \\dfrac{125}{13} \\approx 9.62$ · '
        'ค่านี้ผิดเพราะ $\\sin^2 x\\cos^2 x = \\left(\\sin x\\cos x\\right)^2$ '
        '⇒ เมื่อของข้างในถูกยกกำลังสอง เพดานของมันก็ต้องถูกยกกำลังสองตามไปด้วย '
        '⇒ เพดานที่ถูกต้องคือ $\\left(\\dfrac{1}{2}\\right)^2 = \\dfrac{1}{4}$ ไม่ใช่ $\\dfrac{1}{2}$ · '
        'ตรวจซ้ำได้ด้วยการแทน $x = \\dfrac{\\pi}{4}$ ซึ่งเป็นจุดที่ผลคูณโตที่สุด '
        'แล้วอ่านค่าจริงออกมาได้ $\\dfrac{1}{2}\\cdot\\dfrac{1}{2} = \\dfrac{1}{4}$',
        '• ได้ค่า $\\dfrac{495}{34}$ เพราะกระจายวงเล็บโดยลืมพจน์ไขว้ คือเขียน '
        '$\\left(\\sin^2 x + 2\\right)\\left(\\cos^2 x + 2\\right) = \\sin^2 x\\cos^2 x + 4$ '
        'ทิ้งพจน์ $2\\sin^2 x + 2\\cos^2 x = 2$ ไปทั้งก้อน ⇒ ตัวส่วนกลายเป็นอยู่ใน '
        '$\\left[4,\\ \\dfrac{17}{4}\\right]$ ⇒ ค่าสูงสุดกลายเป็น $\\dfrac{30}{4} = \\dfrac{15}{2}$ '
        'และค่าต่ำสุดกลายเป็น $\\dfrac{120}{17}$ ⇒ ผลบวก '
        '$\\dfrac{15}{2} + \\dfrac{120}{17} = \\dfrac{495}{34} \\approx 14.56$ · '
        'ค่านี้ผิดแน่นอน ตรวจได้ในบรรทัดเดียวโดยแทน $x = 0$ ลงตัวส่วนต้นฉบับ '
        'ได้ $(0 + 2)(1 + 2) = 6$ แต่รูปที่กระจายผิดให้ $0 + 4 = 4$ ⇒ ไม่ตรงกัน '
        '⇒ การกระจายนั้นผิดตั้งแต่บรรทัดแรก · วิธีกันคือกระจายวงเล็บสองวงให้ครบสี่พจน์ทุกครั้ง',
        '• ได้ค่า $\\dfrac{48}{5}$ เพราะหาช่วงของตัวส่วนได้ $\\left[6,\\ \\dfrac{25}{4}\\right]$ '
        'ถูกต้องแล้ว แต่สลับทิศตอนพลิกกลับ คือคิดว่าตัวส่วนมากที่สุดจะให้ค่าของ $f$ มากที่สุด '
        'จึงหยิบ $\\dfrac{30}{\\dfrac{25}{4}} = \\dfrac{24}{5}$ มาเป็นค่าสูงสุด '
        'แล้วเผลอใช้ค่าเดียวกันนี้ซ้ำอีกครั้งเป็นค่าต่ำสุด '
        '⇒ ผลบวก $\\dfrac{24}{5} + \\dfrac{24}{5} = \\dfrac{48}{5} = 9.6$ · '
        'ค่านี้ผิดสองชั้นพร้อมกัน ชั้นแรกคือทิศกลับด้าน ชั้นที่สองคือค่าสูงสุดกับค่าต่ำสุด '
        'กลายเป็นค่าเดียวกัน ซึ่งเกิดขึ้นได้ก็ต่อเมื่อ $f$ เป็นฟังก์ชันคงตัวเท่านั้น '
        'แต่ $f$ ไม่คงตัว เพราะ $f(0) = 5$ ขณะที่ $f\\left(\\dfrac{\\pi}{4}\\right) = \\dfrac{24}{5}$ '
        'ซึ่งไม่เท่ากัน ⇒ ขัดกันเองทันที',
    ],
    'V.mold: G = a single rational function of one real variable, f(x) = 30 divided by the product of '
    '(sin squared x plus 2) and (cos squared x plus 2), defined for every real x, with a constant numerator '
    'and a denominator built as a product of two shifted squares of the two co-functions / A = the sum of '
    'the largest possible value of f and the smallest possible value of f, asked as a free numeric response '
    'with no candidate values printed anywhere on the page / M = M-PYTHID-COLLAPSE-PRODUCT-DENOM-THEN-'
    'BOUNDED-PRODUCT-RECIP, that is: expand the two brackets in full, let the Pythagorean identity swallow '
    'the cross terms 2 sin squared x plus 2 cos squared x into the constant 2 so that the denominator '
    'collapses to sin squared x cos squared x plus 6 and only one moving quantity survives, substitute '
    'w = sin squared x so that cos squared x = 1 - w and the surviving quantity becomes the downward '
    'parabola w(1-w) on the closed interval [0,1] whose ceiling is one quarter at w = one half and whose '
    'floor is zero at either endpoint, push that range through the shift by 6 to get a denominator range of '
    '[6, 25/4], and finally invert, because a positive constant numerator makes the function decreasing in '
    'the denominator, so the two endpoints trade places and give 5 and 24/5 whose sum is 49/5. '
    'Rubric F2 C2 P2 T3 L0 = 9/15, which clears the threshold of 8 with T at least 2, while the total stays '
    'below 12 so the very-hard band is out of reach even though T sits at its ceiling -> level: ยาก. '
    'F = 2 because exactly two pieces of stored knowledge carry the item, the Pythagorean identity and the '
    'range of a square of a sine, while the vertex of a downward parabola is pre-trigonometric algebra '
    'rather than a third formula to recall; F is not 3 because no sum formula, no double angle, no law of '
    'sines or cosines and no inverse function appears anywhere. C = 2 because two different subjects are '
    'welded together and neither half can be deleted: a trigonometric identity has to fire first to reduce '
    'two coupled quantities to one, and only then does an algebraic extremum argument on a closed interval '
    'become available; a solver who can do only one of the two halves cannot start. P = 2 because the '
    'arithmetic is a real but bounded chain, one bracket expansion of four terms, one cancellation, one '
    'vertex evaluation, one shift, two divisions by a fraction and one addition of unlike fractions, with '
    'no long grind; the weight of the item is deliberately placed on seeing rather than on computing. '
    'T = 3 because three independent hidden turns must all be found before any answer can be trusted: '
    'first that the denominator collapses at all, which is invisible until the brackets are expanded; '
    'second, and this is the trap that decides the item, that sin squared x and cos squared x are not free '
    'to reach 1 together because their sum is locked at 1, so the product is capped at one quarter and not '
    'at 1; and third that the numerator being a positive constant reverses the direction, so the largest '
    'denominator produces the smallest function value and the two endpoints swap roles at the very last '
    'step. L = 0 because the statement is purely symbolic, carries no real-world scene, no figure and '
    'nothing to draw, and every quantity can be substituted immediately. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): in the q161 block, simplify of expand((sin(x)**2+2)*(cos(x)**2+2)) minus '
    '(sin(x)**2*cos(x)**2+6) returns exactly 0, which is the machine statement that the collapse of step 1 '
    'is an identity and not a lucky substitution; with D = w*(1-w)+6 the calls minimum(30/D, w, '
    'Interval(0,1)) and maximum(30/D, w, Interval(0,1)) return 24/5 and 5, their sum is 49/5, and the '
    'stored key string 49/5 was compared against that sum as a rational rather than as text. Two further '
    'checks were run in this session on top of the block: minimum and maximum of the original untouched '
    'expression 30/((sin(x)**2+2)*(cos(x)**2+2)) taken over all real x return 24/5 and 5 as well, so the '
    'reduction to a single variable did not quietly change the answer, and direct substitution gives '
    'f(0) = 5, f(pi/4) = 24/5 and f(pi/6) = 160/33, about 4.8485, which lies strictly between the two '
    'extremes and is the independent check reproduced in the explanation. Every error path in the pitfalls '
    'block was computed by machine rather than invented: taking the product range as [0,1] gives 5 + 30/7 = '
    '65/7, about 9.2857; capping the product at one half instead of one quarter gives 5 + 60/13 = 125/13, '
    'about 9.6154; dropping the cross terms leaves a denominator range of [4, 17/4] and gives 15/2 + 120/17 '
    '= 495/34, about 14.559, while the same wrong expansion evaluated at x = 0 returns 4 against the true 6, '
    'which is the one-line refutation quoted in the explanation; and reversing the direction while reusing '
    'one endpoint twice gives 24/5 + 24/5 = 48/5. '
    'Collision sweep on 6457 de-duplicated items (86 files: the bank sets directory plus k1 out plus k2 '
    'out), run directly in this session because no collide_b21.py exists in the tree: the pair (largest '
    'value and smallest value asked in the same question) returns 20 items and the tighter pair that also '
    'demands the word for sum returns only 2, gen-chap-05-function-q094, which is an absolute value '
    'function on a closed interval in chapter 5, and gen-chap-07-trigonometry-q140, which is the one real '
    'neighbour and is recorded here rather than hidden: it also sits in subtopic 7.3 and also asks for the '
    'sum of the largest and smallest values of an f, but its G is a product of a sine and a cosine carrying '
    'two different phase shifts, its M is the collapse of that product into a single sinusoid so that the '
    'sum falls straight out of the vertical shift, it is a multiple choice item and its level is ปานกลาง, '
    'so only A overlaps while G and M both differ. Searching for the two squared co-functions appearing '
    'together returns 22 items, all of them identity manipulations or equation solving rather than range '
    'questions; the bracket shape of a squared sine plus a small integer inside parentheses returns 1 item, '
    'chap-07-trigonometry-q23, which is a radical equation in subtopic 7.7; and no item anywhere in the '
    'corpus asks for the range of the product of the two squared co-functions. The closest item by '
    'mechanism is gen-chap-07-trigonometry-q038, a constant over 5 plus 3 sin x asking only for the largest '
    'value: it shares the final inversion step but its denominator is linear in a single trigonometric '
    'function, so no identity is needed, no coupling trap exists, only one extreme is requested and its '
    'level is ปานกลาง. Inside subtopic 7.3 the corpus holds 51 items and none of them builds its '
    'denominator as a product of two brackets. Since this is a fill item there is no choice list, so no '
    'answer slot exists and nothing about the answer could have been positioned by hand.',
)

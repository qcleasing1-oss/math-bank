# -*- coding: utf-8 -*-
add(
    157,
    ['7.2'],
    'ยาก',
    'กำหนดให้ $\\alpha$ และ $\\beta$ เป็นจำนวนจริงซึ่ง $0 < \\alpha < 2\\pi$ , $0 < \\beta < 2\\pi$ '
    'และ $\\alpha + \\beta = \\dfrac{3\\pi}{2}$ ถ้า $\\cos\\alpha = -\\dfrac{24}{25}$ และ $\\cos\\beta > 0$ '
    'แล้วค่าของ $25\\left(\\sin\\alpha + \\sin\\beta\\right)$ เท่ากับข้อใดต่อไปนี้',
    [
        '$-31$',
        '$0$',
        '$17$',
        '$31$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• อ่านค่าตรีโกณมิติจากวงกลมหนึ่งหน่วยก่อนเสมอ : เมื่อวัดส่วนโค้งยาว $\\theta$ หน่วยจากจุด $(1,0)$ '
        'ไปตามวงกลมรัศมี $1$ หน่วยที่มีจุดศูนย์กลางอยู่ที่จุดกำเนิด จุดปลายของส่วนโค้งจะมีพิกัดเป็น '
        '$\\left(\\cos\\theta , \\sin\\theta\\right)$ ⇒ เครื่องหมายของ $\\cos\\theta$ ก็คือเครื่องหมายของพิกัดที่หนึ่ง '
        'และเครื่องหมายของ $\\sin\\theta$ ก็คือเครื่องหมายของพิกัดที่สอง · จตุภาคที่ $1$ บวกทั้งคู่ · '
        'จตุภาคที่ $2$ มี $\\cos$ เป็นลบ แต่ $\\sin$ เป็นบวก · จตุภาคที่ $3$ ลบทั้งคู่ · '
        'จตุภาคที่ $4$ มี $\\cos$ เป็นบวก แต่ $\\sin$ เป็นลบ',
        '• การรู้ค่า $\\cos$ เพียงค่าเดียว<b>ยังไม่พอ</b>ที่จะระบุมุมได้ : ในช่วง $0 < \\theta < 2\\pi$ '
        'สมการ $\\cos\\theta = k$ เมื่อ $-1 < k < 1$ มีคำตอบ<b>สองค่าเสมอ</b> '
        'เพราะจุดสองจุดบนวงกลมที่สะท้อนกันข้ามแกนนอนมีพิกัดที่หนึ่งเท่ากันเป๊ะ แต่มีพิกัดที่สองตรงข้ามกัน '
        '⇒ สองสาขานั้นให้ $\\sin\\theta$ คนละเครื่องหมาย ⇒ ต้องมีเงื่อนไขอีกข้อมาชี้ขาดว่าจะเก็บสาขาไหน '
        '⛔ ห้ามเดาจตุภาคเอาเองด้วยความเคยชิน',
        '• อัตลักษณ์พีทาโกรัส $\\sin^{2}\\theta + \\cos^{2}\\theta = 1$ มาจากการที่จุด '
        '$\\left(\\cos\\theta , \\sin\\theta\\right)$ อยู่บนวงกลมรัศมี $1$ หน่วยจริง ๆ '
        '⇒ จัดรูปได้เป็น $\\sin\\theta = \\pm\\sqrt{1 - \\cos^{2}\\theta}$ · '
        '⛔ เครื่องหมายหน้าเครื่องหมายกรณฑ์ต้องมาจาก<b>จตุภาค</b>เท่านั้น ไม่ได้มาจากตัวสูตร · '
        'สามเหลี่ยมอ้างอิงที่ใช้ในข้อนี้คือชุด $7$-$24$-$25$ เพราะ $7^{2} + 24^{2} = 49 + 576 = 625 = 25^{2}$',
        '• สูตรผลต่างของมุม : $\\sin(A - B) = \\sin A\\cos B - \\cos A\\sin B$ และ '
        '$\\cos(A - B) = \\cos A\\cos B + \\sin A\\sin B$ · แทน $A = \\dfrac{3\\pi}{2}$ '
        'ซึ่งมี $\\sin\\dfrac{3\\pi}{2} = -1$ และ $\\cos\\dfrac{3\\pi}{2} = 0$ '
        'จะได้สูตรมุมสัมพันธ์สองบรรทัดที่ข้อนี้ต้องใช้ คือ '
        '$\\sin\\left(\\dfrac{3\\pi}{2} - \\theta\\right) = -\\cos\\theta$ และ '
        '$\\cos\\left(\\dfrac{3\\pi}{2} - \\theta\\right) = -\\sin\\theta$ '
        '⇒ สังเกตว่าฟังก์ชัน<b>เปลี่ยนชนิด</b>ไปเป็นโคฟังก์ชันของมันเอง เพราะ $\\dfrac{3\\pi}{2}$ อยู่บนแกนตั้ง',
        '• ⭐ <b>กุญแจดอกที่หนึ่งของข้อนี้</b> : ผู้สมัครที่ต้องคัดอยู่ที่มุม $\\alpha$ '
        'แต่เงื่อนไขที่โจทย์ให้มาสำหรับคัดกลับเขียนไว้บนมุม $\\beta$ '
        '⇒ ต้อง<b>ย้ายเงื่อนไขข้ามตัวแปร</b>ก่อนถึงจะใช้ได้ โดยอาศัยความสัมพันธ์ '
        '$\\alpha + \\beta = \\dfrac{3\\pi}{2}$ เปลี่ยน $\\cos\\beta$ ให้กลายเป็นฟังก์ชันของ $\\alpha$ '
        '⇒ เงื่อนไขที่ดูเหมือนพูดถึงมุมอีกตัวหนึ่งจะกลายเป็นเงื่อนไขเรื่องเครื่องหมายของ $\\sin\\alpha$ ทันที',
        '• ⭐ <b>กุญแจดอกที่สองของข้อนี้</b> : เงื่อนไข $0 < \\beta < 2\\pi$ หน้าตาเหมือนเป็นตัวคัดสาขา '
        'แต่พอแทน $\\beta = \\dfrac{3\\pi}{2} - \\alpha$ ลงไปจะพบว่ามันแปลเป็นเพียง $0 < \\alpha < \\dfrac{3\\pi}{2}$ '
        'ซึ่งผู้สมัครทั้งสองรายผ่านหมด ⇒ <b>ไม่ได้ตัดใครทิ้งเลยสักราย</b> '
        '⇒ ตัวที่ชี้ขาดจริง ๆ คือ $\\cos\\beta > 0$ เท่านั้น ⛔ ถ้าเผลอคิดว่าเงื่อนไขช่วงพอแล้ว จะเหลือสองสาขาและตอบไม่ได้',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $\\alpha$ และ $\\beta$ เป็นจำนวนจริง โดยที่ $0 < \\alpha < 2\\pi$ และ $0 < \\beta < 2\\pi$',
        '• ผลบวกของสองมุมคงที่ : $\\alpha + \\beta = \\dfrac{3\\pi}{2}$ '
        '⇒ ย้ายข้างได้ทันทีว่า $\\beta = \\dfrac{3\\pi}{2} - \\alpha$ ⇒ ทั้งข้อเหลือตัวแปรอิสระเพียงตัวเดียวคือ $\\alpha$',
        '• $\\cos\\alpha = -\\dfrac{24}{25}$ ⇒ ค่าติดลบ ⇒ พิกัดที่หนึ่งของจุดปลายส่วนโค้งอยู่ทางซ้ายของแกนตั้ง '
        '⇒ $\\alpha$ อยู่ในจตุภาคที่ $2$ หรือจตุภาคที่ $3$ อย่างใดอย่างหนึ่ง',
        '• $\\cos\\beta > 0$ ⇒ นี่คือเงื่อนไขเดียวในโจทย์ที่พูดถึง $\\beta$ โดยตรง และเป็นตัวคัดสาขาตัวจริง',
        '• สังเกตหน้าตาก่อนลงมือ : สิ่งที่ถามคือ $25\\left(\\sin\\alpha + \\sin\\beta\\right)$ '
        '⇒ ต้องหาให้ได้ทั้ง $\\sin\\alpha$ และ $\\sin\\beta$ ⇒ ต้องรู้จตุภาคของ $\\alpha$ ให้แน่ชัดเสียก่อน '
        '· ตัวคูณ $25$ ที่ครอบไว้ข้างนอกตรงกับตัวส่วนของ $\\dfrac{24}{25}$ พอดี '
        '⇒ เป็นสัญญาณว่าคำตอบตั้งใจให้ออกมาเป็นจำนวนเต็ม และตัวเลขทั้งชุดมาจากสามเหลี่ยม $7$-$24$-$25$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $25\\left(\\sin\\alpha + \\sin\\beta\\right)$ ออกมาเป็นจำนวนจริงจำนวนเดียว',
        '',
        '<b>【 หา $\\sin\\alpha$ จากอัตลักษณ์พีทาโกรัสก่อน จะได้ผู้สมัครสองรายที่ต่างกันแค่เครื่องหมาย '
        'จากนั้นใช้ $\\cos\\left(\\dfrac{3\\pi}{2} - \\alpha\\right) = -\\sin\\alpha$ '
        'แปลงเงื่อนไข $\\cos\\beta > 0$ ให้กลายเป็น $\\sin\\alpha < 0$ ⇒ เหลือสาขาจตุภาคที่ $3$ เพียงสาขาเดียว '
        'แล้วใช้ $\\sin\\left(\\dfrac{3\\pi}{2} - \\alpha\\right) = -\\cos\\alpha$ หา $\\sin\\beta$ '
        'ก่อนแทนลงในนิพจน์ที่โจทย์ถาม 】</b>',
        '',
        '<b>ขั้นที่ 1 · หาผู้สมัครของมุม $\\alpha$ จากค่าโคไซน์ที่โจทย์ให้มา</b>',
        '• สูตรที่ใช้ : $\\sin^{2}\\theta + \\cos^{2}\\theta = 1$ ⇒ $\\sin^{2}\\theta = 1 - \\cos^{2}\\theta$',
        '• ระบุตัวแปร : มุมที่กำลังพิจารณาคือ $\\alpha$ ซึ่งมี $\\cos\\alpha = -\\dfrac{24}{25}$',
        '• แทนค่า : $\\sin^{2}\\alpha = 1 - \\left(-\\dfrac{24}{25}\\right)^{2} = 1 - \\dfrac{576}{625}$',
        '• ยุบ : $1 = \\dfrac{625}{625}$ ⇒ $\\sin^{2}\\alpha = \\dfrac{625 - 576}{625} = \\dfrac{49}{625}$ '
        '⇒ $\\sin\\alpha = \\pm\\dfrac{7}{25}$ เพราะ $49 = 7^{2}$ และ $625 = 25^{2}$',
        '• ⭐ ตอนนี้ได้ผู้เข้าชิงมาสองราย และทั้งสองรายก็สอดคล้องกับ $\\cos\\alpha = -\\dfrac{24}{25}$ '
        'ทุกประการ : รายแรกคือ $\\alpha$ ที่อยู่ในจตุภาคที่ $2$ ซึ่งมี $\\sin\\alpha = +\\dfrac{7}{25}$ '
        '· รายที่สองคือ $\\alpha$ ที่อยู่ในจตุภาคที่ $3$ ซึ่งมี $\\sin\\alpha = -\\dfrac{7}{25}$',
        '• เขียนมุมทั้งสองเป็นตัวเลขไว้ใช้ตรวจตอนท้าย โดยให้ $\\gamma$ แทนมุมแหลมที่มี '
        '$\\cos\\gamma = \\dfrac{24}{25}$ ซึ่งมีค่าประมาณ $0.284$ เรเดียน '
        '⇒ ผู้สมัครรายแรกคือ $\\alpha = \\pi - \\gamma \\approx 2.858$ '
        'และผู้สมัครรายที่สองคือ $\\alpha = \\pi + \\gamma \\approx 3.425$',
        '• 📌 ย้ำว่ายัง<b>ตอบไม่ได้</b> เพราะสองสาขานี้ให้ $\\sin\\alpha$ คนละเครื่องหมาย '
        '⇒ ค่าที่โจทย์ถามจะออกมาคนละค่ากันแน่นอน ⇒ ต้องไปคัดสาขาก่อนในขั้นถัดไป',
        '',
        '<b>ขั้นที่ 2 · แปลงเงื่อนไขที่เขียนไว้บน $\\beta$ ให้กลายเป็นเงื่อนไขของ $\\alpha$ แล้วคัดสาขา</b>',
        '• สูตรที่ใช้ : $\\cos(A - B) = \\cos A\\cos B + \\sin A\\sin B$',
        '• ระบุตัวแปร : จาก $\\alpha + \\beta = \\dfrac{3\\pi}{2}$ ⇒ $\\beta = \\dfrac{3\\pi}{2} - \\alpha$ '
        '⇒ ตั้ง $A = \\dfrac{3\\pi}{2}$ และ $B = \\alpha$',
        '• 📌 ตรวจเงื่อนไขช่วงให้จบก่อน : $0 < \\beta < 2\\pi$ ⇒ '
        '$0 < \\dfrac{3\\pi}{2} - \\alpha < 2\\pi$ ⇒ ข้างซ้ายให้ $\\alpha < \\dfrac{3\\pi}{2}$ '
        'และข้างขวาให้ $\\alpha > -\\dfrac{\\pi}{2}$ ซึ่งจริงอยู่แล้วเพราะ $\\alpha > 0$ '
        '⇒ รวมกับ $0 < \\alpha < 2\\pi$ เหลือ $0 < \\alpha < \\dfrac{3\\pi}{2} \\approx 4.712$ '
        '⇒ ผู้สมัครทั้งสองราย ($\\approx 2.858$ และ $\\approx 3.425$) ผ่านหมด '
        '⇒ ⛔ เงื่อนไขช่วงไม่ได้คัดใครออกเลยแม้แต่รายเดียว',
        '• แทนค่าลงสูตรผลต่าง : $\\cos\\beta = \\cos\\left(\\dfrac{3\\pi}{2} - \\alpha\\right) = '
        '\\cos\\dfrac{3\\pi}{2}\\cos\\alpha + \\sin\\dfrac{3\\pi}{2}\\sin\\alpha$',
        '• ยุบด้วยค่าที่มุมแกน : $\\cos\\dfrac{3\\pi}{2} = 0$ และ $\\sin\\dfrac{3\\pi}{2} = -1$ '
        '⇒ $\\cos\\beta = (0)\\cos\\alpha + (-1)\\sin\\alpha = -\\sin\\alpha$',
        '• 🔴 <b>หัวใจของข้อนี้อยู่ตรงนี้</b> : เงื่อนไข $\\cos\\beta > 0$ '
        'จึงแปลว่า $-\\sin\\alpha > 0$ ⇒ $\\sin\\alpha < 0$ '
        '⇒ เงื่อนไขที่เขียนไว้บนมุมหนึ่ง กลายเป็นเงื่อนไขเรื่องเครื่องหมายของอีกมุมหนึ่งเรียบร้อยแล้ว',
        '• คัดผู้สมัครรายแรก (จตุภาคที่ $2$) : สาขานี้มี $\\sin\\alpha = +\\dfrac{7}{25}$ '
        '⇒ $\\cos\\beta = -\\dfrac{7}{25}$ ซึ่งเป็นลบ ⇒ ⛔ ขัดกับเงื่อนไข $\\cos\\beta > 0$ ⇒ ทิ้งสาขานี้ '
        '(ตรวจซ้ำด้วยตัวเลขได้ว่า $\\beta = \\dfrac{3\\pi}{2} - 2.858 \\approx 1.855$ '
        'ซึ่งมากกว่า $\\dfrac{\\pi}{2} \\approx 1.571$ ⇒ $\\beta$ ตกอยู่ในจตุภาคที่ $2$ จริง)',
        '• คัดผู้สมัครรายที่สอง (จตุภาคที่ $3$) : สาขานี้มี $\\sin\\alpha = -\\dfrac{7}{25}$ '
        '⇒ $\\cos\\beta = +\\dfrac{7}{25}$ ซึ่งเป็นบวก ✓ ⇒ เก็บสาขานี้ไว้',
        '• ⭐ สรุปผลการคัด : เหลือสาขาเดียวคือ $\\alpha$ อยู่ในจตุภาคที่ $3$ และ '
        '$\\sin\\alpha = -\\dfrac{7}{25}$ ⇒ โจทย์ข้อนี้มีคำตอบเดียว ไม่กำกวม · '
        'มองอีกมุมหนึ่งก็ได้ว่า $\\sin\\alpha < 0$ บังคับให้ $\\pi < \\alpha < 2\\pi$ '
        'พอมาเจอกับ $\\alpha < \\dfrac{3\\pi}{2}$ จากเงื่อนไขช่วง ก็บีบเหลือจตุภาคที่ $3$ พอดี',
        '',
        '<b>ขั้นที่ 3 · หา $\\sin\\beta$ ด้วยสูตรผลต่างอีกครั้ง</b>',
        '• สูตรที่ใช้ : $\\sin(A - B) = \\sin A\\cos B - \\cos A\\sin B$',
        '• ระบุตัวแปร : ยังคง $A = \\dfrac{3\\pi}{2}$ และ $B = \\alpha$ เหมือนเดิม',
        '• แทนค่า : $\\sin\\beta = \\sin\\left(\\dfrac{3\\pi}{2} - \\alpha\\right) = '
        '\\sin\\dfrac{3\\pi}{2}\\cos\\alpha - \\cos\\dfrac{3\\pi}{2}\\sin\\alpha$',
        '• ยุบ : $= (-1)\\cos\\alpha - (0)\\sin\\alpha = -\\cos\\alpha$ '
        '⇒ ⭐ ได้เอกลักษณ์ประจำข้อนี้ว่า $\\sin\\beta = -\\cos\\alpha$ '
        '⇒ สังเกตว่าฟังก์ชันเปลี่ยนชนิดจาก $\\sin$ ไปเป็น $\\cos$ พร้อมกับติดเครื่องหมายลบมาด้วย '
        '⛔ ห้ามทำหล่นทั้งสองอย่าง',
        '• แทนค่าที่โจทย์ให้ : $\\cos\\alpha = -\\dfrac{24}{25}$ '
        '⇒ $\\sin\\beta = -\\left(-\\dfrac{24}{25}\\right) = \\dfrac{24}{25}$',
        '• 📌 ตรวจความสอดคล้องของมุม $\\beta$ ทันทีก่อนเดินต่อ : จากขั้นที่ 2 ได้ '
        '$\\cos\\beta = \\dfrac{7}{25}$ และรอบนี้ได้ $\\sin\\beta = \\dfrac{24}{25}$ '
        '⇒ $\\sin^{2}\\beta + \\cos^{2}\\beta = \\dfrac{576}{625} + \\dfrac{49}{625} = \\dfrac{625}{625} = 1$ ✓ '
        '⇒ มุม $\\beta$ นี้มีอยู่จริงบนวงกลมหนึ่งหน่วย และเป็นบวกทั้งคู่ ⇒ $\\beta$ อยู่ในจตุภาคที่ $1$',
        '',
        '<b>ขั้นที่ 4 · แทนค่าลงในนิพจน์ที่โจทย์ถาม</b>',
        '• สูตรที่ใช้ : นิพจน์ที่ต้องหาคือ $25\\left(\\sin\\alpha + \\sin\\beta\\right)$',
        '• ระบุตัวเลขที่จะแทน : $\\sin\\alpha = -\\dfrac{7}{25}$ จากขั้นที่ 2 · '
        '$\\sin\\beta = \\dfrac{24}{25}$ จากขั้นที่ 3',
        '• แทนค่า : $25\\left(-\\dfrac{7}{25} + \\dfrac{24}{25}\\right)$',
        '• ยุบวงเล็บก่อน : $-\\dfrac{7}{25} + \\dfrac{24}{25} = \\dfrac{-7 + 24}{25} = \\dfrac{17}{25}$ '
        '⇒ $25 \\times \\dfrac{17}{25} = 17$',
        '• หรือจะกระจาย $25$ เข้าไปก่อนก็ได้ผลเท่ากัน : '
        '$25\\left(-\\dfrac{7}{25}\\right) = -7$ และ $25\\left(\\dfrac{24}{25}\\right) = 24$ '
        '⇒ $-7 + 24 = 17$ ⇒ ⭐ ตัวส่วน $25$ ถูกตัวคูณ $25$ ตัดทิ้งพอดี คำตอบจึงเป็นจำนวนเต็ม',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · หยิบมุมจริงเป็นเรเดียนมาแทนกลับเข้าทุกเงื่อนไขของโจทย์ '
        'แล้ววัดด้วยค่าประมาณ โดยไม่แตะสูตรผลต่างเลยแม้แต่บรรทัดเดียว)</b>',
        '• เส้นทางข้างบนเดินด้วยเอกลักษณ์ล้วน ๆ รอบนี้จะเปลี่ยนเป็นการหยิบตัวเลขมุมจริงมาแทน '
        'แล้วไล่ตรวจเงื่อนไขของโจทย์ทีละบรรทัดว่าครบหรือไม่ ⇒ ถ้าผ่านหมดแสดงว่าคู่มุมที่คัดไว้ถูกต้อง',
        '• มุมแหลมที่มีโคไซน์เท่ากับ $\\dfrac{24}{25}$ มีขนาดประมาณ $0.284$ เรเดียน '
        '⇒ สาขาที่เก็บไว้คือ $\\alpha \\approx \\pi + 0.284 \\approx 3.425$ '
        'และ $\\beta = \\dfrac{3\\pi}{2} - \\alpha \\approx 4.712 - 3.425 = 1.287$',
        '• เงื่อนไขช่วงทั้งสองข้อ : $0 < 3.425 < 6.283$ ✓ และ $0 < 1.287 < 6.283$ ✓',
        '• เงื่อนไขผลบวก : $3.425 + 1.287 = 4.712$ ซึ่งเท่ากับ $\\dfrac{3\\pi}{2}$ ✓',
        '• เงื่อนไขค่าโคไซน์ของ $\\alpha$ : $\\cos(3.425) \\approx -0.96$ '
        'และ $-\\dfrac{24}{25} = -0.96$ ⇒ ตรงกัน ✓',
        '• เงื่อนไขเครื่องหมายของ $\\cos\\beta$ : $\\cos(1.287) \\approx 0.28$ ซึ่งเป็นบวก ✓ '
        'และ $0.28 = \\dfrac{7}{25}$ พอดี ⇒ ตรงกับที่คำนวณไว้ในขั้นที่ 2 · '
        'ยืนยันด้วยขอบเขตได้อีกชั้นว่า $1.287 < \\dfrac{\\pi}{2} \\approx 1.571$ '
        '⇒ $\\beta$ อยู่ในจตุภาคที่ $1$ จริง ⇒ โคไซน์ต้องเป็นบวก',
        '• ค่าที่โจทย์ถาม : $\\sin(3.425) \\approx -0.28$ และ $\\sin(1.287) \\approx 0.96$ '
        '⇒ $25(-0.28 + 0.96) = 25(0.68) = 17$ ✓ ตรงกับผลที่ได้จากเส้นทางเอกลักษณ์',
        '• ตรวจอัตลักษณ์ของทั้งสองมุมด้วยสามเหลี่ยมมุมฉากชุดเดียวกัน : ทั้ง $\\alpha$ และ $\\beta$ '
        'ต่างก็มีสามเหลี่ยมอ้างอิงเป็นชุด $7$-$24$-$25$ และ $7^{2} + 24^{2} = 49 + 576 = 625 = 25^{2}$ ✓ '
        '⇒ ตัวเลขทั้งชุดสอดคล้องกันเอง',
        '• 📌 ข้อสังเกตเสริมที่ปิดคดีได้เร็ว : เพราะ $\\alpha + \\beta = \\dfrac{3\\pi}{2}$ เป็นค่าคงที่ '
        'สองมุมนี้จึงเป็น “มุมประกอบสามควอเตอร์” ของกันและกัน ⇒ $\\sin\\beta = -\\cos\\alpha = \\dfrac{24}{25}$ '
        '<b>เสมอ</b> ไม่ว่าจะเลือกสาขาไหน ⇒ พจน์ที่สองของนิพจน์เท่ากับ $24$ ตายตัว '
        '⇒ สิ่งเดียวที่ตัดสินคำตอบคือเครื่องหมายของ $\\sin\\alpha$ ⇒ ค่าที่เป็นไปได้มีแค่ '
        '$24 - 7 = 17$ กับ $24 + 7 = 31$ และเงื่อนไข $\\cos\\beta > 0$ คือสิ่งเดียวที่ชี้ขาดระหว่างสองค่านี้',
        '',
        '✅ <b>คำตอบ</b> ค่าของ $25\\left(\\sin\\alpha + \\sin\\beta\\right)$ เท่ากับ $17$ → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• พอเจอโจทย์ที่ผูกสองมุมไว้ด้วยผลบวกคงที่ ให้รีบเขียนมุมหนึ่งในรูปของอีกมุมหนึ่งทันที '
        'แล้ว<b>ยุบทั้งข้อให้เหลือตัวแปรเดียว</b> · ข้อนี้พอเขียน $\\beta = \\dfrac{3\\pi}{2} - \\alpha$ '
        'ทุกเงื่อนไขก็ย้ายมาอยู่บน $\\alpha$ ได้หมด ⇒ การคัดสาขาจึงทำได้ในที่เดียว '
        '⛔ ถ้าปล่อยให้เงื่อนไขกระจายอยู่บนสองตัวแปร จะมองไม่เห็นว่าเงื่อนไขไหนคัดอะไรได้บ้าง',
        '• จำกลุ่มมุมสัมพันธ์ด้วย<b>แกน</b> ไม่ใช่ด้วยการท่อง : $\\pi \\pm \\theta$ กับ $2\\pi \\pm \\theta$ '
        'วัดจากแกนนอน ⇒ ฟังก์ชัน<b>ไม่เปลี่ยนชนิด</b> · ส่วน $\\dfrac{\\pi}{2} \\pm \\theta$ กับ '
        '$\\dfrac{3\\pi}{2} \\pm \\theta$ วัดจากแกนตั้ง ⇒ ต้อง<b>เปลี่ยนเป็นโคฟังก์ชัน</b> '
        '($\\sin$ สลับกับ $\\cos$) เสมอ ⇒ ข้อนี้ $\\dfrac{3\\pi}{2}$ อยู่บนแกนตั้ง จึงต้องสลับแน่นอน',
        '• ตรวจสูตรมุมสัมพันธ์ที่จำมาด้วยการแทนมุมง่าย ๆ ก่อนใช้เสมอ : ลองแทน $\\theta = 0$ '
        'ลงใน $\\sin\\left(\\dfrac{3\\pi}{2} - \\theta\\right)$ จะได้ $\\sin\\dfrac{3\\pi}{2} = -1$ '
        'ส่วนสูตรที่จำไว้คือ $-\\cos 0 = -1$ ⇒ ตรงกัน ✓ ⇒ ใช้เวลาสองวินาทีแต่กันพลาดเรื่องเครื่องหมายได้ทั้งข้อ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $-31$ เพราะคัดสาขาถูกแล้ว คือได้ $\\sin\\alpha = -\\dfrac{7}{25}$ มาอย่างถูกต้อง '
        'แต่ตอนแปลง $\\sin\\beta$ กลับทำเครื่องหมายลบหล่นหาย คือเขียนว่า '
        '$\\sin\\left(\\dfrac{3\\pi}{2} - \\alpha\\right) = \\cos\\alpha$ ⇒ ได้ $\\sin\\beta = -\\dfrac{24}{25}$ '
        '⇒ $25\\left(-\\dfrac{7}{25} - \\dfrac{24}{25}\\right) = -7 - 24 = -31$ · '
        'ค่านี้ผิดและจับได้สองชั้น : ชั้นแรก แทน $\\theta = 0$ ลงในสูตรที่ใช้จะได้ '
        '$\\sin\\dfrac{3\\pi}{2} = -1$ แต่ $\\cos 0 = +1$ ⇒ สูตรที่ใช้ผิดตั้งแต่ต้น · '
        'ชั้นที่สอง ถ้า $\\sin\\beta$ ติดลบจริงพร้อมกับ $\\cos\\beta > 0$ แล้ว $\\beta$ ต้องอยู่ในจตุภาคที่ $4$ '
        '⇒ $\\beta \\approx 2\\pi - 1.287 \\approx 4.996$ ⇒ $\\alpha = \\dfrac{3\\pi}{2} - \\beta \\approx -0.284$ '
        'ซึ่งติดลบ ⇒ ขัดกับ $0 < \\alpha$ ที่โจทย์กำหนด ⇒ เป็นไปไม่ได้ · '
        'วิธีกันคือเขียนสูตรผลต่างเต็ม ๆ แล้วแทน $\\sin\\dfrac{3\\pi}{2} = -1$ ลงไปตรง ๆ '
        'แทนการนึกเอาว่าโคฟังก์ชันแล้วเครื่องหมายคงเป็นบวก',
        '• ได้ค่า $0$ เพราะจำมุมสัมพันธ์ผิดเป็น $\\sin\\left(\\dfrac{3\\pi}{2} - \\alpha\\right) = -\\sin\\alpha$ '
        'คือใส่เครื่องหมายลบมาถูก แต่<b>ลืมเปลี่ยนเป็นโคฟังก์ชัน</b> ⇒ สองพจน์ในวงเล็บหักล้างกันพอดี '
        '⇒ $25\\left(\\sin\\alpha - \\sin\\alpha\\right) = 0$ · ค่านี้ผิดเพราะ $\\dfrac{3\\pi}{2}$ '
        'อยู่บน<b>แกนตั้ง</b> ⇒ กฎบังคับให้สลับ $\\sin$ กับ $\\cos$ เสมอ · '
        'ทดสอบเร็วด้วย $\\alpha = \\dfrac{\\pi}{2}$ ก็เห็นทันที : ข้างซ้ายได้ $\\sin\\pi = 0$ '
        'แต่ข้างขวาตามสูตรที่จำผิดได้ $-\\sin\\dfrac{\\pi}{2} = -1$ ⇒ ขัดกัน ⇒ สูตรผิด '
        '(ในขณะที่สูตรที่ถูกให้ $-\\cos\\dfrac{\\pi}{2} = 0$ ⇒ ตรงกันพอดี) · '
        'อีกชั้นหนึ่งใช้สามัญสำนึกได้ว่า ถ้าคำตอบเป็น $0$ ตายตัวไม่ว่าจะเลือกสาขาใด '
        'โจทย์ก็ไม่มีเหตุผลที่จะให้เงื่อนไข $\\cos\\beta > 0$ มาแต่แรก',
        '• ได้ค่า $31$ เพราะ<b>ไม่ได้ใช้เงื่อนไข</b> $\\cos\\beta > 0$ เลยแม้แต่นิดเดียว '
        'พอเห็นว่า $\\cos\\alpha$ ติดลบก็เดาตามความเคยชินว่ามุมอยู่ในจตุภาคที่ $2$ '
        '⇒ หยิบ $\\sin\\alpha = +\\dfrac{7}{25}$ มาใช้ ⇒ $25\\left(\\dfrac{7}{25} + \\dfrac{24}{25}\\right) = 7 + 24 = 31$ · '
        'ค่านี้ผิดเพราะสาขานั้นทำให้ $\\alpha \\approx 2.858$ ⇒ $\\beta \\approx 4.712 - 2.858 = 1.855$ '
        'ซึ่งมากกว่า $\\dfrac{\\pi}{2} \\approx 1.571$ ⇒ $\\beta$ ตกอยู่ในจตุภาคที่ $2$ '
        '⇒ $\\cos\\beta \\approx -0.28 = -\\dfrac{7}{25}$ ซึ่งเป็น<b>ลบ</b> ⇒ ขัดกับเงื่อนไขที่โจทย์เขียนไว้ตรง ๆ '
        '⇒ ต้องทิ้งสาขานี้ · นี่คือกับดักหลักของข้อนี้ : เงื่อนไขคัดถูกเขียนไว้บนมุม $\\beta$ '
        'ทั้งที่สิ่งที่ต้องคัดคือสาขาของมุม $\\alpha$ ⇒ คนที่มองว่าเป็นคนละเรื่องกันจะข้ามเงื่อนไขนี้ไปเลย · '
        'วิธีกันคือนับเงื่อนไขในโจทย์ให้ครบทุกข้อก่อนวงคำตอบ แล้วถามตัวเองว่าใช้ครบทุกข้อหรือยัง',
        '• เส้นทางพลาดที่เหลือคือหยุดกลางทางหรือคิดเครื่องหมายจากที่ผิด : บางคนตอบ $\\dfrac{17}{25}$ '
        'หรือ $0.68$ เพราะลืมคูณ $25$ กลับเข้าไป ทั้งที่ตัวคูณนั้นอยู่ในโจทย์มาตั้งแต่ต้นและมีไว้เพื่อให้คำตอบเป็นจำนวนเต็ม · '
        'อีกกลุ่มหนึ่งเลือก $\\sin\\alpha = -\\sqrt{1 - \\cos^{2}\\alpha}$ ด้วยเหตุผลว่า “ $\\cos$ ติดลบ '
        'แล้ว $\\sin$ ก็ควรติดลบตาม ” ⇒ ข้อนี้บังเอิญได้เครื่องหมายถูก แต่<b>เหตุผลผิด</b> '
        'เพราะจตุภาคที่ $2$ ก็มี $\\cos$ ติดลบเหมือนกันแต่ $\\sin$ เป็นบวก '
        '⇒ ถ้าโจทย์เปลี่ยนเงื่อนไขเป็น $\\cos\\beta < 0$ คนกลุ่มนี้จะพลาดทันที · '
        'วิธีกันคือยึดกฎว่าเครื่องหมายของ $\\sin$ ต้องอ่านจากจตุภาคที่พิสูจน์มาแล้วเท่านั้น '
        'และจตุภาคต้องมาจากเงื่อนไขที่โจทย์ให้ ⛔ ไม่ใช่จากความรู้สึก',
    ],
    'V.mold: G = G-TWO-ANGLES-FIXED-SUM-COSINE-VALUE-ON-ONE-SIGN-CONDITION-ON-THE-OTHER, two real numbers '
    'alpha and beta each confined to the open interval from 0 to 2*pi and locked together by the constant '
    'sum alpha + beta = 3*pi/2, with the numeric datum cos(alpha) = -24/25 attached to the first angle and '
    'the screening datum cos(beta) > 0 attached to the second / A = A-EXPRESSION-VALUE, the value of the '
    'scaled sum 25*(sin(alpha) + sin(beta)), a single integer / '
    'M = M-PARTNER-ANGLE-CONDITION-REDUCED-ONTO-BASE-ANGLE, write beta = 3*pi/2 - alpha, push the condition '
    'stated on beta back onto alpha through cos(3*pi/2 - alpha) = -sin(alpha) so that cos(beta) > 0 becomes '
    'sin(alpha) < 0, which is what actually kills the quadrant-two candidate, then convert the second term '
    'with sin(3*pi/2 - alpha) = -cos(alpha) and evaluate. '
    'Rubric F2 C2 P2 T3 L0 = 9/15, with tot >= 8 and T >= 2 -> level: ยาก. '
    'F = 2 because exactly two formula blocks carry the item, the Pythagorean identity that produces the '
    'two sign candidates and the difference formulas for sine and cosine evaluated at 3*pi/2; F was not '
    'raised to 3 because no third theorem enters anywhere, no double angle, no sum to product, no equation '
    'solving. C = 2 because two independent ideas have to be chained before the arithmetic can start, first '
    'the quadrant reading of a signed cosine and second the transfer of a condition from one variable to '
    'the other across a fixed angle sum; either link alone leaves the item unanswerable. P = 2 because the '
    'computation itself is short once the branch is fixed, one square root of 49/625, two reductions and '
    'one cancellation of 25 against the denominator; P was not raised to 3 because there is no long '
    'expansion and no equation to solve. T = 3 for three hidden conditions stacked on one another: the '
    'screening condition is written on beta while the candidate set lives on alpha, so a solver who reads '
    'the conditions as belonging to separate angles never applies it; the interval condition '
    '0 < beta < 2*pi looks decisive but reduces to 0 < alpha < 3*pi/2 and eliminates neither candidate, so '
    'it is a decoy; and the reduction at 3*pi/2 changes the function to its cofunction and carries a minus '
    'sign at the same time, so two independent slips are available in one line. L = 0 because the item is '
    'purely symbolic, there is no figure to draw and no real-world situation to model, every datum is '
    'already an equation. The total stops at 9, so the tot >= 12 gate for ยากมาก is out of reach no matter '
    'how T is read, while the ยาก gate is met on tot >= 8 together with T >= 2 and is read before the '
    'ปานกลาง gate, so the item lands where it does. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): solveset(cos(th) = -24/25) on the open interval from 0 to 2*pi returns exactly '
    'two roots, approximately 2.85780 and 3.42539; mapping each root a to b = 3*pi/2 - a and filtering on '
    '0 < b < 2*pi together with cos(b) > 0 leaves exactly one survivor, which is the machine proof that the '
    'item is not ambiguous and also the machine proof that the interval part of the filter is inert, since '
    'both roots pass it and only the sign test separates them. On the surviving branch sin(alpha) is '
    'Rational(-7, 25), cos(beta) is Rational(7, 25), sin(beta) is Rational(24, 25) and '
    '25*(sin(alpha) + sin(beta)) simplifies to 17. expand_trig confirms the two reductions independently, '
    'sin(3*pi/2 - x) = -cos(x) and cos(3*pi/2 - x) = -sin(x). Every wrong value on offer was machine '
    'computed from a named error path rather than invented: 25*(sin(a) + cos(a)) on the surviving branch '
    'returns -31, which is the path that drops the minus sign of the sine reduction; 25*(sin(a) - sin(a)) '
    'returns 0, which is the path that reduces to -sin instead of the cofunction; and 25*(sin(a) - cos(a)) '
    'evaluated on the rejected quadrant-two root returns 31, which is the path that never applies '
    'cos(beta) > 0 at all. The numeric back substitution was machine checked as well: acos(24/25) = '
    '0.283794, alpha = 3.425387, beta = 1.287002, cos(beta) = 0.28 and sin(beta) = 0.96 exactly, and '
    'beta < pi/2 = 1.570796 so beta really does sit in the first quadrant. '
    'Collision sweep on 6457 unique items (bank 63 files + k1 out + k2 out, 6601 raw records with 144 '
    'duplicates dropped): the equation alpha + beta = 3*pi/2 inside a question returns 0 items, and a sign '
    'condition of the shape cos(beta) > 0 placed on a second angle returns 0 items, so the governing '
    'structure of this item is empty in the corpus. Questions carrying both alpha and beta return 13 '
    'items; the trigonometric ones among them (chap-07-trigonometry-q37, q56, q155, q156, q182 and '
    'samn-2556-01-q16) all hand over a compound expression such as cos(alpha + beta) or a pair of summed '
    'values and are solved with the sum and difference machinery, that is the M-SUMDIFF family, not one of '
    'them fixes the sum of the two angles and uses it to move a screening condition from one angle to the '
    'other. Two near relatives deserve to be named. gen-chap-07-trigonometry-q022 shares the surface most '
    'closely: it is also 7.2, also wraps the answer in a factor of 25 and also lives on the 7-24-25 '
    'triple, but it supplies tan(theta) = 7/24 with sin(theta) < 0 on the same single angle and is solved '
    'by M-REF-TRIANGLE-WITH-SIGN, so it has no partner angle, no fixed sum and no reduction step at all; '
    'notably its correct answer -31 appears here only as a wrong value. gen-chap-07-trigonometry-q137 is '
    'the nearest mechanism relative: it screens two candidates of a single theta by the sign condition '
    'cos(theta)*tan(theta) > 0 and asks for 29*(sin(theta) - cos(theta)), so it shares the branch-picking '
    'shape but the condition already sits on the angle being screened, which is exactly the step this item '
    'adds. A scan for the reduction 3*pi/2 - angle returns 2 items, chap-07-trigonometry-q138 and '
    'gen-chap-07-trigonometry-q036, and both use it to simplify a given expression rather than to transport '
    'a condition, so they meet this item at F and part company at G, A and M. Choices are ordered ascending '
    'by numeric value (-31, then 0, then 17, then 31), so the answer slot is forced by that rule and was '
    'not chosen.',
)

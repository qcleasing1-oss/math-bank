# -*- coding: utf-8 -*-
add(
    144,
    ['7.4'],
    'ยากมาก',
    'กำหนดให้ $\\theta$ เป็นจำนวนจริงซึ่ง $\\dfrac{\\pi}{2} < \\theta < \\dfrac{3\\pi}{4}$ '
    'และ $\\dfrac{1}{\\sin^2\\theta} + \\dfrac{1}{\\cos^2\\theta} = \\dfrac{100}{9}$ '
    'ค่าของ $\\tan\\theta + \\sin\\theta\\cos\\theta$ เท่ากับข้อใด',
    [
        '$-\\dfrac{33}{10}$',
        '$-\\dfrac{27}{10}$',
        '$-\\dfrac{19}{30}$',
        '$\\dfrac{33}{10}$',
    ],
    0,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เอกลักษณ์พีทาโกรัส : $\\sin^{2}\\theta + \\cos^{2}\\theta = 1$ ทุกค่าของ $\\theta$ · '
        'ที่เป็นเช่นนี้เพราะจุดบนวงกลมหนึ่งหน่วยที่คู่กับมุม $\\theta$ มีพิกัดเป็น '
        '$(\\cos\\theta,\\ \\sin\\theta)$ และจุดนั้นอยู่ห่างจุดกำเนิดเท่ากับ $1$ เสมอ '
        'เมื่อเขียนระยะทางกำลังสองออกมาจึงได้เอกลักษณ์นี้ทันที · '
        'ประโยชน์ที่ใช้บ่อยที่สุดคือใช้แทนเลข $1$ ที่โผล่มาจากการรวมเศษส่วน '
        'หรือใช้ย้อนกลับคือแทน $\\sin^{2}\\theta + \\cos^{2}\\theta$ ด้วยเลข $1$ เพื่อยุบนิพจน์ให้สั้นลง',
        '• เครื่องหมายของอัตราส่วนตรีโกณมิติในแต่ละจตุภาค อ่านจากพิกัดของจุดบนวงกลมหนึ่งหน่วย : '
        'จตุภาคที่ $2$ คือส่วนที่ $x$ เป็นลบและ $y$ เป็นบวก ⇒ $\\cos\\theta < 0$ และ $\\sin\\theta > 0$ '
        'จึงได้ผลพลอยได้สองอย่างที่จะใช้ในข้อนี้ คือ $\\sin\\theta\\cos\\theta < 0$ '
        'เพราะเป็นบวกคูณลบ และ $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta} < 0$ '
        'เพราะเป็นบวกหารด้วยลบ · ⛔ ข้อจำกัดที่ต้องจำให้ขึ้นใจคือ จตุภาคบอกได้แต่ '
        '<b>เครื่องหมาย</b> ไม่เคยบอก <b>ขนาด</b>',
        '• ความสัมพันธ์ที่จะเป็นสะพานของข้อนี้ : '
        '$\\tan\\theta + \\cot\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta} + \\dfrac{\\cos\\theta}{\\sin\\theta} '
        '= \\dfrac{\\sin^{2}\\theta + \\cos^{2}\\theta}{\\sin\\theta\\cos\\theta} '
        '= \\dfrac{1}{\\sin\\theta\\cos\\theta}$ · '
        'ที่มาคือทำตัวส่วนร่วมแล้วใช้เอกลักษณ์พีทาโกรัสกับเศษ · '
        'อ่านความหมายได้ว่า ถ้ารู้ค่าของผลคูณ $\\sin\\theta\\cos\\theta$ เมื่อไร '
        'ก็รู้ค่าของ $\\tan\\theta + \\cot\\theta$ ทันทีโดยไม่ต้องรู้ $\\theta$ เลย',
        '• การถอดรากที่สอง : จาก $X^{2} = k$ เมื่อ $k > 0$ จะได้ $X = \\sqrt{k}$ '
        'หรือ $X = -\\sqrt{k}$ เสมอ ⛔ ห้ามหยิบเฉพาะค่าบวก · '
        'เหตุผลคือการยกกำลังสองทำลายเครื่องหมายทิ้ง ทั้ง $+\\dfrac{3}{10}$ และ $-\\dfrac{3}{10}$ '
        'ยกกำลังสองแล้วได้ $\\dfrac{9}{100}$ เหมือนกันเป๊ะ '
        'เครื่องหมายที่หายไปจึงต้องไปกู้คืนจากข้อมูลอื่นที่โจทย์ให้มา ไม่ใช่จากสมการนั้นเอง',
        '• สมการรูป $t + \\dfrac{1}{t} = k$ : คูณด้วย $t$ ทั้งสองข้าง (ทำได้เมื่อ $t \\ne 0$) '
        'จะได้สมการกำลังสอง $t^{2} - kt + 1 = 0$ · '
        'สิ่งที่ต้องสังเกตคือผลคูณของรากทั้งสองเท่ากับ $1$ เสมอ ⇒ รากทั้งสองเป็น<b>ส่วนกลับของกัน</b> '
        'และเมื่อผลคูณเป็นบวก รากทั้งสองย่อมมีเครื่องหมายเหมือนกันเสมอ '
        '⇒ 🔴 การเช็คเครื่องหมายอย่างเดียวจะไม่มีวันแยกรากคู่นี้ออกจากกันได้',
        '• พฤติกรรมของ $\\tan\\theta$ บนช่วง $\\left(\\dfrac{\\pi}{2},\\ \\pi\\right)$ : '
        'เมื่อ $\\theta$ ขยับออกจาก $\\dfrac{\\pi}{2}$ ไปทางขวาเล็กน้อย $\\cos\\theta$ '
        'เป็นลบและเข้าใกล้ศูนย์ ส่วน $\\sin\\theta$ เข้าใกล้ $1$ '
        '⇒ อัตราส่วนดิ่งลงไปทาง $-\\infty$ · จากนั้น $\\tan\\theta$ '
        '<b>เพิ่มขึ้นเรื่อย ๆ</b> ตลอดช่วงจนถึงค่า $0$ ที่ $\\theta = \\pi$ · '
        'จุดหมุดที่ต้องจำคือ $\\tan\\dfrac{3\\pi}{4} = -1$ · '
        'เพราะฟังก์ชันเพิ่มขึ้นตลอดช่วง ขอบเขตของมุมจึงแปลตรง ๆ เป็นขอบเขตของค่า $\\tan$ ได้',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $\\theta$ เป็นจำนวนจริงที่ $\\dfrac{\\pi}{2} < \\theta < \\dfrac{3\\pi}{4}$ · '
        '🔴 อ่านช่วงนี้ให้ละเอียด มันไม่ใช่ทั้งจตุภาค แต่เป็นเพียง<b>ครึ่งซ้าย</b>ของจตุภาคที่ $2$ '
        '(จตุภาคที่ $2$ เต็ม ๆ คือตั้งแต่ $\\dfrac{\\pi}{2}$ ถึง $\\pi$) '
        '⇒ ช่วงนี้พกข้อมูลมาสองชั้น ชั้นแรกคือเครื่องหมายจากจตุภาค '
        'ชั้นที่สองคือขนาดจากขอบบน $\\dfrac{3\\pi}{4}$',
        '• เงื่อนไขเชิงสมการ : $\\dfrac{1}{\\sin^{2}\\theta} + \\dfrac{1}{\\cos^{2}\\theta} '
        '= \\dfrac{100}{9}$ · สังเกตว่าตัวเลขทางขวาเป็นกำลังสองพอดี '
        'เพราะ $\\dfrac{100}{9} = \\left(\\dfrac{10}{3}\\right)^{2}$ '
        'ซึ่งเป็นสัญญาณว่าเส้นทางข้างหน้าจะมีการถอดรากและตัวเลขจะออกมาเป็นเศษส่วนสวย ๆ',
        '• สังเกตหน้าตาก่อนลงมือ : ก้อนที่โจทย์ให้มา<b>สมมาตร</b>ระหว่าง $\\sin\\theta$ กับ $\\cos\\theta$ '
        'คือสลับสองตัวนี้แล้วสมการหน้าตาเหมือนเดิมทุกประการ · '
        'แต่สิ่งที่โจทย์ถามคือ $\\tan\\theta + \\sin\\theta\\cos\\theta$ ซึ่ง<b>ไม่สมมาตร</b> '
        'เพราะสลับแล้ว $\\tan\\theta$ กลายเป็น $\\cot\\theta$ '
        '⇒ เดาได้ตั้งแต่ยังไม่คำนวณว่า เงื่อนไขจะให้คำตอบมาเป็นคู่ '
        'และคำตอบทั้งคู่จะให้ค่าที่ถามไม่เท่ากัน ⇒ ต้องมีอะไรสักอย่างในโจทย์ทำหน้าที่ชี้ขาด '
        'และสิ่งเดียวที่เหลืออยู่ก็คือช่วงของ $\\theta$',
        '• สังเกตอีกอย่าง : เงื่อนไขทั้งก้อนพูดถึงแต่ $\\sin^{2}\\theta$ กับ $\\cos^{2}\\theta$ '
        'ไม่มีพจน์เดี่ยว ๆ เลย ⇒ มันจะบอกเราได้อย่างมากแค่เรื่อง<b>ขนาด</b>ของผลคูณ '
        '$\\sin\\theta\\cos\\theta$ เท่านั้น ส่วนเครื่องหมายต้องหาจากที่อื่น',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\tan\\theta + \\sin\\theta\\cos\\theta$ ซึ่งเป็นผลบวกของสองก้อนที่ต่างชนิดกัน '
        '⇒ ต้องหาให้ครบทั้งค่าของ $\\tan\\theta$ และค่าของ $\\sin\\theta\\cos\\theta$ '
        'แล้วจึงบวกกันในขั้นสุดท้าย · ห้ามหยุดกลางทางเมื่อได้ก้อนใดก้อนหนึ่ง',
        '',
        '<b>【 ยุบเงื่อนไขให้เหลือแต่ผลคูณ $\\sin\\theta\\cos\\theta$ '
        'แล้วใช้จตุภาคที่ $2$ ตัดสินเครื่องหมายของผลคูณนั้น '
        'จากนั้นพลิกผลคูณกลับหัวเพื่อเปลี่ยนทั้งข้อให้เป็นสมการกำลังสองใน $\\tan\\theta$ '
        'ซึ่งจะได้รากที่เป็นส่วนกลับของกันสองราก '
        'สุดท้ายใช้ขอบบน $\\dfrac{3\\pi}{4}$ ของช่วงคัดให้เหลือรากเดียว แล้วจึงประกอบเป็นคำตอบ 】</b>',
        '',
        '<b>ขั้นที่ 1 · ยุบเงื่อนไขสองก้อนให้เหลือก้อนเดียว</b>',
        '• ทำไมต้องยุบก่อน : เงื่อนไขที่ให้มามีตัวไม่รู้สองก้อนคือ $\\sin\\theta$ กับ $\\cos\\theta$ '
        'ซึ่งจับต้นชนปลายไม่ถูก แต่ถ้ารวมเป็นก้อนเดียวได้ ทั้งข้อจะเหลือตัวไม่รู้เพียงตัวเดียว '
        'แล้วทุกอย่างจะไหลตามมาเอง',
        '• สูตรที่ใช้ : ทำตัวส่วนร่วมของเศษส่วนสองก้อน '
        '$\\dfrac{1}{A} + \\dfrac{1}{B} = \\dfrac{B + A}{AB}$ '
        'ประกอบกับเอกลักษณ์ $\\sin^{2}\\theta + \\cos^{2}\\theta = 1$',
        '• ระบุตัวแปรก่อนแทนค่า : ที่นี่ $A = \\sin^{2}\\theta$ และ $B = \\cos^{2}\\theta$ '
        '⇒ ตัวส่วนร่วมคือ $\\sin^{2}\\theta\\cos^{2}\\theta$ '
        'และเศษที่ได้คือ $\\cos^{2}\\theta + \\sin^{2}\\theta$',
        '• แทนค่า : $\\dfrac{1}{\\sin^{2}\\theta} + \\dfrac{1}{\\cos^{2}\\theta} '
        '= \\dfrac{\\cos^{2}\\theta + \\sin^{2}\\theta}{\\sin^{2}\\theta\\cos^{2}\\theta}$',
        '• ยุบ : เศษเท่ากับ $1$ พอดีตามเอกลักษณ์พีทาโกรัส '
        'และตัวส่วนเขียนรวบเป็นกำลังสองก้อนเดียวได้ '
        'เพราะ $\\sin^{2}\\theta\\cos^{2}\\theta = (\\sin\\theta\\cos\\theta)^{2}$ '
        '⇒ เงื่อนไขทั้งก้อนกลายเป็น '
        '$\\dfrac{1}{(\\sin\\theta\\cos\\theta)^{2}} = \\dfrac{100}{9}$',
        '• หยุดอ่านความหมายสักครู่ : บรรทัดนี้บอกว่าเงื่อนไขยาว ๆ ที่โจทย์ให้มา '
        'แท้จริงแล้วพูดถึงสิ่งเดียวเท่านั้นคือผลคูณ $\\sin\\theta\\cos\\theta$ '
        'มันไม่ได้บอกอะไรเกี่ยวกับ $\\sin\\theta$ หรือ $\\cos\\theta$ แยกกันเลยแม้แต่นิดเดียว',
        '',
        '<b>ขั้นที่ 2 · ถอดรากที่สอง แล้วกู้เครื่องหมายคืนด้วยจตุภาค</b>',
        '• สูตรที่ใช้ : กลับเศษส่วนทั้งสองข้าง (ทำได้เพราะทั้งสองข้างไม่เป็นศูนย์) '
        'แล้วถอดรากที่สองแบบมีทั้งสองเครื่องหมาย $X^{2} = k \\Rightarrow X = \\pm\\sqrt{k}$',
        '• ระบุตัวแปรก่อนแทนค่า : ให้ $X = \\sin\\theta\\cos\\theta$ '
        'และจากขั้นที่ 1 ได้ $\\dfrac{1}{X^{2}} = \\dfrac{100}{9}$',
        '• แทนค่าแล้วยุบ : กลับเศษส่วนทั้งสองข้างได้ $X^{2} = \\dfrac{9}{100}$ '
        '⇒ ถอดรากได้ $X = \\dfrac{3}{10}$ หรือ $X = -\\dfrac{3}{10}$ · '
        '⛔ ถึงตรงนี้ยัง<b>ห้ามเลือก</b>ว่าตัวไหนถูก เพราะสมการไม่มีข้อมูลพอจะตัดสิน',
        '• กู้เครื่องหมายคืนจากช่วงที่โจทย์ให้ : ช่วง $\\dfrac{\\pi}{2} < \\theta < \\dfrac{3\\pi}{4}$ '
        'อยู่ในจตุภาคที่ $2$ ทั้งช่วง ⇒ $\\sin\\theta > 0$ และ $\\cos\\theta < 0$ '
        '⇒ ผลคูณของบวกกับลบย่อมเป็นลบ ⇒ $\\sin\\theta\\cos\\theta < 0$',
        '• สรุปขั้นนี้ : $\\sin\\theta\\cos\\theta = -\\dfrac{3}{10}$ '
        'เพียงค่าเดียวเท่านั้น ส่วน $+\\dfrac{3}{10}$ ถูกทิ้งเพราะขัดกับจตุภาค',
        '• ตรวจความสมเหตุสมผลของขนาดไว้ก่อนเดินต่อ : เนื่องจาก '
        '$\\sin\\theta\\cos\\theta = \\dfrac{1}{2}\\sin 2\\theta$ '
        'และ $\\sin$ ของอะไรก็ตามมีค่าอยู่ระหว่าง $-1$ กับ $1$ '
        '⇒ ผลคูณนี้ต้องมีขนาดไม่เกิน $\\dfrac{1}{2}$ เสมอ · '
        'ค่าที่ได้มีขนาด $\\dfrac{3}{10} = 0.3$ ซึ่งไม่เกิน $0.5$ ✓ ผ่านด่านความสมเหตุสมผล',
        '',
        '<b>ขั้นที่ 3 · เปลี่ยนทั้งข้อให้เป็นสมการกำลังสองใน $\\tan\\theta$</b>',
        '• ทำไมต้องเปลี่ยนไปเล่นกับ $\\tan\\theta$ : สิ่งที่โจทย์ถามมี $\\tan\\theta$ อยู่ '
        'และเรามีผลคูณ $\\sin\\theta\\cos\\theta$ อยู่ในมือแล้ว '
        'สะพานที่เชื่อมสองสิ่งนี้เข้าหากันคือความสัมพันธ์ '
        '$\\tan\\theta + \\cot\\theta = \\dfrac{1}{\\sin\\theta\\cos\\theta}$ '
        'ซึ่งเปลี่ยนข้อมูลเรื่องผลคูณให้กลายเป็นข้อมูลเรื่อง $\\tan\\theta$ ได้ตรง ๆ',
        '• แทนค่า : $\\tan\\theta + \\cot\\theta = \\dfrac{1}{-\\dfrac{3}{10}} = -\\dfrac{10}{3}$',
        '• ตั้งตัวแปรใหม่ให้สะอาด : ให้ $t = \\tan\\theta$ · '
        'เนื่องจาก $\\cot\\theta = \\dfrac{1}{\\tan\\theta} = \\dfrac{1}{t}$ '
        'สมการข้างบนจึงกลายเป็น $t + \\dfrac{1}{t} = -\\dfrac{10}{3}$ · '
        'ทำได้เพราะในช่วงที่โจทย์ให้ $\\sin\\theta$ กับ $\\cos\\theta$ ไม่เป็นศูนย์ทั้งคู่ '
        '⇒ $t$ มีค่าและไม่เป็นศูนย์',
        '• ยุบให้พ้นเศษส่วน : คูณทั้งสองข้างด้วย $3t$ ได้ $3t^{2} + 3 = -10t$ '
        '⇒ ย้ายข้างให้เรียบร้อยเป็น $3t^{2} + 10t + 3 = 0$',
        '• แยกตัวประกอบ : มองหาการแยกที่คูณกันแล้วได้ $3t^{2}$ กับ $3$ '
        'และไขว้กันแล้วบวกได้ $10t$ ⇒ $(3t + 1)(t + 3) = 0$ '
        '⇒ $t = -\\dfrac{1}{3}$ หรือ $t = -3$',
        '• 🔴 หยุดดูลักษณะของรากคู่นี้ให้ดี : ทั้งสองรากเป็น<b>ลบทั้งคู่</b> '
        'ซึ่งสอดคล้องกับจตุภาคที่ $2$ เหมือนกันทั้งคู่ '
        'และผลคูณของทั้งสองรากเท่ากับ $\\left(-\\dfrac{1}{3}\\right)(-3) = 1$ '
        '⇒ เป็นส่วนกลับของกันพอดี ⇒ '
        'การตรวจเครื่องหมายด้วยจตุภาคจะ<b>ช่วยอะไรไม่ได้เลย</b>ในการแยกสองรากนี้',
        '',
        '<b>ขั้นที่ 4 · 🔴 กับดักหลักของข้อนี้ — ใช้ขอบบนของช่วงคัดรากให้เหลือตัวเดียว</b>',
        '• สถานการณ์ตอนนี้ : มีผู้เข้าชิงสองราย คือ $\\tan\\theta = -3$ กับ '
        '$\\tan\\theta = -\\dfrac{1}{3}$ · ทั้งคู่สอดคล้องกับสมการที่โจทย์ให้ทุกประการ '
        'และทั้งคู่ก็อยู่ในจตุภาคที่ $2$ ⇒ เครื่องมือที่ใช้มาถึงตรงนี้หมดฤทธิ์แล้ว '
        'ต้องหยิบข้อมูลที่ยังไม่ได้ใช้ออกมา นั่นคือ<b>ขอบบน</b>ของช่วง',
        '• แปลช่วงของมุมให้เป็นช่วงของค่า $\\tan$ : บนช่วง '
        '$\\left(\\dfrac{\\pi}{2},\\ \\dfrac{3\\pi}{4}\\right)$ ฟังก์ชัน $\\tan$ เพิ่มขึ้นตลอด · '
        'ที่ปลายซ้าย เมื่อ $\\theta$ เข้าใกล้ $\\dfrac{\\pi}{2}$ ค่า $\\tan\\theta$ ดิ่งลงไปทาง $-\\infty$ · '
        'ที่ปลายขวา $\\tan\\dfrac{3\\pi}{4} = -1$ '
        '⇒ ค่า $\\tan\\theta$ วิ่งจาก $-\\infty$ ขึ้นมาถึง $-1$ '
        '⇒ สรุปเป็นอสมการได้ว่า $\\tan\\theta < -1$',
        '• คัดราก : $-3 < -1$ ✓ ผ่านเงื่อนไข จึงเก็บไว้ · '
        '$-\\dfrac{1}{3} > -1$ ⛔ ไม่ผ่าน จึงต้องทิ้ง '
        '(เทียบง่าย ๆ ว่า $-0.333$ อยู่ทางขวาของ $-1$ บนเส้นจำนวน) '
        '⇒ เหลือ $\\tan\\theta = -3$ เพียงค่าเดียว',
        '• รากที่ถูกทิ้งไปอยู่ที่ไหนกันแน่ : ถ้า $\\tan\\theta = -\\dfrac{1}{3}$ '
        'มุมที่ได้คือ $\\theta = \\pi - \\arctan\\dfrac{1}{3} \\approx 3.1416 - 0.3217 = 2.8198$ เรเดียน · '
        'ค่านี้อยู่ในจตุภาคที่ $2$ จริง (เพราะยังน้อยกว่า $\\pi \\approx 3.1416$) '
        'แต่มัน<b>เลย</b>ขอบบน $\\dfrac{3\\pi}{4} \\approx 2.3562$ ไปแล้ว '
        '⇒ เป็นมุมที่สอดคล้องกับสมการแต่หลุดออกนอกช่วงที่โจทย์กำหนด',
        '• 🔴 บทเรียนของขั้นนี้ที่ต้องขีดเส้นใต้ : ถ้าใช้แค่คำว่า “จตุภาคที่ $2$” '
        'จะแยกสองรากนี้ไม่ได้เลย เพราะทั้งคู่อยู่ในจตุภาคเดียวกันและเป็นลบเหมือนกัน · '
        'สิ่งที่ทำงานจริงคือขอบบน $\\dfrac{3\\pi}{4}$ ซึ่งเป็นข้อมูลเรื่อง<b>ขนาด</b> ไม่ใช่เรื่องเครื่องหมาย '
        '⇒ เห็นช่วงที่แคบกว่าหนึ่งจตุภาคเมื่อไร ให้รู้ทันทีว่าโจทย์ตั้งใจให้ใช้ขอบของช่วง',
        '',
        '<b>ขั้นที่ 5 · ประกอบสองก้อนเข้าเป็นคำตอบ</b>',
        '• ระบุของที่มีอยู่ในมือให้ครบก่อนบวก : จากขั้นที่ 4 ได้ $\\tan\\theta = -3$ · '
        'จากขั้นที่ 2 ได้ $\\sin\\theta\\cos\\theta = -\\dfrac{3}{10}$',
        '• แทนค่า : $\\tan\\theta + \\sin\\theta\\cos\\theta = (-3) + \\left(-\\dfrac{3}{10}\\right)$',
        '• ยุบ : ทำเป็นตัวส่วนเดียวกัน $-3 = -\\dfrac{30}{10}$ '
        '⇒ $-\\dfrac{30}{10} - \\dfrac{3}{10} = -\\dfrac{33}{10}$',
        '• เช็คด้วยสามัญสำนึกปิดขั้น : เรากำลังเอาจำนวนลบเล็ก ๆ ไปบวกกับ $-3$ '
        '⇒ ผลลัพธ์ต้องเป็นลบและมีขนาด<b>มากกว่า</b> $3$ เล็กน้อย · '
        'ค่า $-\\dfrac{33}{10} = -3.3$ ก็เป็นลบและมีขนาด $3.3$ ซึ่งมากกว่า $3$ อยู่ $0.3$ พอดี ✓ '
        'ตัวกรองสั้น ๆ บรรทัดนี้ตัดค่าที่เป็นบวกและค่าที่มีขนาดเล็กกว่า $1$ ทิ้งได้ทันที',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไม่ย้อนกลับไปแตะสมการกำลังสองเลย '
        'แต่สร้างค่าจริงของ $\\sin\\theta$ กับ $\\cos\\theta$ ขึ้นมาจากสามเหลี่ยมอ้างอิง '
        'แล้วแทนกลับเข้าไปทดสอบทุกประโยคที่โจทย์เขียนไว้)</b>',
        '• แนวคิดของการตรวจ : ขั้นที่ 1 ถึง 5 เป็นการ<b>สร้าง</b>คำตอบขึ้นมาจากเงื่อนไข '
        'ส่วนรอบนี้เดินย้อนศร คือสมมติว่ารู้คำตอบแล้ว จึงสร้างมุมที่เป็นรูปธรรมขึ้นมาหนึ่งมุม '
        'แล้ว<b>ทดสอบ</b>ว่ามันผ่านทุกประโยคของโจทย์หรือไม่ · '
        'ถ้าผ่านครบทุกประโยค แปลว่าคำตอบใช้ได้จริง โดยไม่ต้องเชื่อบรรทัดใดในเส้นทางเดิมเลย',
        '• สร้างค่าจริงจากสามเหลี่ยมอ้างอิง : จาก $\\tan\\theta = -3 = \\dfrac{3}{-1}$ '
        'ให้วาดสามเหลี่ยมมุมฉากที่มีด้านประกอบมุมฉากยาว $3$ กับ $1$ '
        '⇒ ด้านตรงข้ามมุมฉากยาว $\\sqrt{3^{2} + 1^{2}} = \\sqrt{10}$ '
        '⇒ ขนาดของ $\\sin$ คือ $\\dfrac{3}{\\sqrt{10}}$ และขนาดของ $\\cos$ คือ $\\dfrac{1}{\\sqrt{10}}$ · '
        'ติดเครื่องหมายตามจตุภาคที่ $2$ คือ $\\sin$ เป็นบวกและ $\\cos$ เป็นลบ '
        '⇒ $\\sin\\theta = \\dfrac{3}{\\sqrt{10}}$ และ $\\cos\\theta = -\\dfrac{1}{\\sqrt{10}}$',
        '• ตรวจว่าคู่ที่สร้างขึ้นเป็นคู่ที่ถูกกฎหมายจริง : '
        '$\\sin^{2}\\theta + \\cos^{2}\\theta = \\dfrac{9}{10} + \\dfrac{1}{10} = 1$ ✓ '
        'จึงมีมุมจริง ๆ ที่ให้ค่าคู่นี้',
        '• ประโยคที่หนึ่ง สมการที่โจทย์กำหนด : '
        '$\\dfrac{1}{\\sin^{2}\\theta} = \\dfrac{1}{9/10} = \\dfrac{10}{9}$ '
        'และ $\\dfrac{1}{\\cos^{2}\\theta} = \\dfrac{1}{1/10} = 10$ '
        '⇒ บวกกันได้ $\\dfrac{10}{9} + 10 = \\dfrac{10}{9} + \\dfrac{90}{9} = \\dfrac{100}{9}$ ✓ ตรงเป๊ะ',
        '• ประโยคที่สอง ช่วงของมุม : $\\theta = \\pi - \\arctan 3 \\approx 3.1416 - 1.2490 = 1.8926$ เรเดียน · '
        'เทียบกับขอบล่าง $\\dfrac{\\pi}{2} \\approx 1.5708$ และขอบบน '
        '$\\dfrac{3\\pi}{4} \\approx 2.3562$ ⇒ $1.5708 < 1.8926 < 2.3562$ ✓ อยู่ในช่วงจริง',
        '• ประโยคที่สาม ค่าของผลคูณที่ใช้ในขั้นที่ 2 : '
        '$\\sin\\theta\\cos\\theta = \\dfrac{3}{\\sqrt{10}} \\cdot \\left(-\\dfrac{1}{\\sqrt{10}}\\right) '
        '= -\\dfrac{3}{10}$ ✓ ตรงกับที่ขั้นที่ 2 อ้างไว้ โดยรอบนี้ได้มาจากค่าจริง ไม่ได้มาจากการถอดราก',
        '• ประกอบผลการตรวจ : $\\tan\\theta + \\sin\\theta\\cos\\theta '
        '= -3 + \\left(-\\dfrac{3}{10}\\right) = -\\dfrac{33}{10}$ ✓ ตรงกับคำตอบที่ได้',
        '• ตรวจรากที่ถูกทิ้งด้วยวิธีเดียวกันเพื่อปิดประตูให้สนิท : ถ้าใช้ '
        '$\\sin\\theta = \\dfrac{1}{\\sqrt{10}}$ และ $\\cos\\theta = -\\dfrac{3}{\\sqrt{10}}$ '
        '(ซึ่งให้ $\\tan\\theta = -\\dfrac{1}{3}$) จะได้ '
        '$\\dfrac{1}{\\sin^{2}\\theta} + \\dfrac{1}{\\cos^{2}\\theta} = 10 + \\dfrac{10}{9} = \\dfrac{100}{9}$ ✓ '
        'ผ่านสมการเหมือนกันทุกประการ แต่มุมที่ได้คือ $2.8198$ เรเดียน ซึ่งมากกว่า $2.3562$ '
        '⛔ ตกประโยคเรื่องช่วง ⇒ ยืนยันว่าขอบบนของช่วงคือสิ่งเดียวที่แยกสองรากออกจากกันได้จริง',
        '',
        '✅ <b>คำตอบ</b> ในช่วงที่โจทย์กำหนดได้ $\\sin\\theta\\cos\\theta = -\\dfrac{3}{10}$ '
        'และ $\\tan\\theta = -3$ จึงได้ $\\tan\\theta + \\sin\\theta\\cos\\theta '
        '= -3 - \\dfrac{3}{10} = -\\dfrac{33}{10}$ → <b>ตัวเลือก 1</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เห็น $\\dfrac{1}{\\sin^{2}\\theta}$ กับ $\\dfrac{1}{\\cos^{2}\\theta}$ บวกกันเมื่อไร '
        'ให้ทำตัวส่วนร่วมทันทีโดยไม่ต้องคิดอะไรมาก เพราะเศษจะยุบเป็น $1$ เสมอ '
        'และทั้งก้อนจะกลายเป็น $\\dfrac{1}{(\\sin\\theta\\cos\\theta)^{2}}$ '
        '⇒ ตัวไม่รู้สองตัวหดเหลือตัวเดียวในก้าวเดียว · '
        'ก้อนพี่น้องที่ยุบด้วยกลไกเดียวกันคือ $\\tan\\theta + \\cot\\theta$ '
        'ซึ่งยุบเป็น $\\dfrac{1}{\\sin\\theta\\cos\\theta}$',
        '• เจอสมการรูป $t + \\dfrac{1}{t} = k$ ให้รู้ทันทีว่ารากทั้งสองเป็นส่วนกลับของกัน '
        'จึงมีเครื่องหมายเหมือนกันเสมอ ⇒ การเช็คจตุภาคจะแยกมันไม่ออก · '
        'ให้กวาดสายตากลับไปหาช่วงที่โจทย์ให้ทันที ถ้าช่วงนั้น<b>แคบกว่า</b>หนึ่งจตุภาค '
        'แปลว่าโจทย์ตั้งใจให้ใช้ขอบของช่วงเป็นตัวชี้ขาด ไม่ใช่ให้ใช้แค่เครื่องหมาย',
        '• วิธีแปลช่วงของมุมเป็นช่วงของค่า $\\tan$ ที่พลาดยากที่สุดคือ '
        'แทนค่ามุมที่ปลายทั้งสองข้างของช่วงก่อน แล้วอาศัยข้อเท็จจริงว่า $\\tan$ '
        'เพิ่มขึ้นตลอดในทุกช่วงที่มันนิยาม · ที่นี่ปลายขวาให้ $\\tan\\dfrac{3\\pi}{4} = -1$ '
        'และปลายซ้ายให้ค่าดิ่งลง $-\\infty$ ⇒ ได้อสมการ $\\tan\\theta < -1$ ในบรรทัดเดียว',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $-\\dfrac{19}{30}$ ซึ่งเป็นกับดักหลักของข้อนี้ · '
        'เส้นทางพลาดคือคำนวณถูกทุกบรรทัดจนได้รากสองราก แล้วตรวจแค่ว่า “อยู่ในจตุภาคที่ $2$ ไหม” '
        'เห็นว่า $-\\dfrac{1}{3}$ เป็นลบก็รับไว้ ⇒ '
        'ได้ $-\\dfrac{1}{3} + \\left(-\\dfrac{3}{10}\\right) = -\\dfrac{10}{30} - \\dfrac{9}{30} '
        '= -\\dfrac{19}{30}$ · '
        'ต้นเหตุคือหยุดที่จตุภาคโดยไม่อ่านขอบบนของช่วง · '
        'ค่านี้ผิดจริงและพิสูจน์ได้ แม้ว่ารากนี้จะสอดคล้องกับ<b>สมการ</b>ที่โจทย์ให้ทุกประการ '
        'เพราะมุมที่คู่กับมันคือ $\\theta \\approx 2.8198$ เรเดียน '
        'ซึ่งมากกว่าขอบบน $\\dfrac{3\\pi}{4} \\approx 2.3562$ ⇒ หลุดออกนอกช่วง · '
        'ตรวจซ้ำได้อีกทางด้วยอสมการ $\\tan\\theta < -1$ บนช่วงนี้ '
        'แต่ $-\\dfrac{1}{3} \\approx -0.333$ ซึ่งมากกว่า $-1$ ⇒ เป็นไปไม่ได้ · '
        'วิธีกันคือทุกครั้งที่ได้รากมากกว่าหนึ่งราก ให้เอามุมกลับไปวัดกับขอบของช่วงทีละข้างเสมอ',
        '• ได้ค่า $-\\dfrac{27}{10}$ เพราะคัดรากถูกแล้วว่า $\\tan\\theta = -3$ '
        'แต่ตอนถอดรากในขั้นที่ 2 หยิบเฉพาะค่าบวก คือใช้ $\\sin\\theta\\cos\\theta = +\\dfrac{3}{10}$ '
        '⇒ ได้ $-3 + \\dfrac{3}{10} = -\\dfrac{27}{10}$ · '
        'ต้นเหตุคือลืมว่าการยกกำลังสองทำลายเครื่องหมายทิ้ง จึงต้องกู้คืนจากจตุภาค · '
        'ค่านี้ผิดจริงและพิสูจน์ได้ทันที เพราะในจตุภาคที่ $2$ มี $\\sin\\theta > 0$ และ $\\cos\\theta < 0$ '
        '⇒ ผลคูณต้องเป็นลบ · '
        'ยิ่งกว่านั้นเมื่อแทนค่าจริง $\\sin\\theta = \\dfrac{3}{\\sqrt{10}}$ '
        'กับ $\\cos\\theta = -\\dfrac{1}{\\sqrt{10}}$ จะได้ผลคูณเป็น $-\\dfrac{3}{10}$ ตรง ๆ '
        'ไม่มีทางเป็นบวกได้เลย · '
        'วิธีกันคือเขียนเครื่องหมาย $\\pm$ ไว้ให้ครบทุกครั้งที่ถอดราก '
        'แล้วทำเครื่องหมายไว้ว่าจะกลับมาใช้ช่วงของมุมตัดทิ้งทีหลัง',
        '• ได้ค่า $\\dfrac{33}{10}$ เพราะไม่ได้ใช้ช่วงที่โจทย์ให้เลยแม้แต่นิดเดียว '
        'คือถอดรากแล้วหยิบ $\\sin\\theta\\cos\\theta = +\\dfrac{3}{10}$ '
        'จากนั้นได้สมการ $t + \\dfrac{1}{t} = \\dfrac{10}{3}$ ⇒ $3t^{2} - 10t + 3 = 0$ '
        '⇒ หยิบราก $t = 3$ มาใช้ ⇒ ได้ $3 + \\dfrac{3}{10} = \\dfrac{33}{10}$ · '
        'ต้นเหตุคืออ่านโจทย์เห็นแต่สมการ ข้ามบรรทัดที่บอกช่วงของ $\\theta$ ไปทั้งบรรทัด · '
        'ค่านี้ผิดจริงและพิสูจน์ได้ เพราะทุกมุมในช่วงที่โจทย์ให้อยู่ในจตุภาคที่ $2$ '
        'ซึ่งบังคับว่า $\\tan\\theta < 0$ และ $\\sin\\theta\\cos\\theta < 0$ '
        '⇒ ผลบวกของสองก้อนที่เป็นลบทั้งคู่ต้องเป็นลบเสมอ '
        '⇒ คำตอบที่เป็นบวกเป็นไปไม่ได้ตั้งแต่ต้น โดยไม่ต้องคำนวณอะไรเลย',
        '• ได้ค่ากลางทางเป็น $\\sin\\theta\\cos\\theta = -\\dfrac{10}{3}$ '
        'เพราะลืมกลับเศษส่วนในขั้นที่ 2 คืออ่านว่า $(\\sin\\theta\\cos\\theta)^{2} = \\dfrac{100}{9}$ '
        'ทั้งที่ของจริงคือ $\\dfrac{1}{(\\sin\\theta\\cos\\theta)^{2}} = \\dfrac{100}{9}$ · '
        'ต้นเหตุคือเห็นเลข $\\dfrac{100}{9}$ แล้วรีบถอดรากโดยไม่ดูว่ามันนั่งอยู่ตรงไหนของเศษส่วน · '
        'ค่านี้ผิดจริงและพิสูจน์ได้โดยไม่ต้องเดินต่อ เพราะ '
        '$\\sin\\theta\\cos\\theta = \\dfrac{1}{2}\\sin 2\\theta$ '
        'จึงมีขนาดไม่เกิน $\\dfrac{1}{2}$ เสมอ แต่ $\\dfrac{10}{3} \\approx 3.33$ '
        'ซึ่งเกินไปไกลมาก ⇒ เป็นไปไม่ได้ · '
        'วิธีกันคือหลังถอดรากทุกครั้ง ให้เทียบขนาดของค่าที่ได้กับกรอบธรรมชาติของฟังก์ชันนั้นก่อนเดินต่อ',
    ],
    'V.mold: G = one symbolic condition, the reciprocal square sum 1/sin^2(theta) + 1/cos^2(theta) = '
    '100/9, handed over together with a range that is deliberately not a whole quadrant but the open '
    'interval from pi/2 to 3pi/4, which is only the left half of the second quadrant / A = the value of '
    'the mixed expression tan(theta) + sin(theta)cos(theta), offered as one of four signed rationals / '
    'M = put the two reciprocal squares over a common denominator so that the condition collapses to '
    '1/(sin theta cos theta)^2 = 100/9, invert and take the square root to get a product of magnitude '
    '3/10, let the quadrant fix that sign as negative, invert the product again to reach tan + cot = '
    '-10/3, clear the fraction into 3t^2 + 10t + 3 = 0 whose roots -3 and -1/3 multiply to 1 and are '
    'therefore a reciprocal pair carrying the same sign, and finally translate the upper endpoint 3pi/4, '
    'where the tangent equals -1, into the inequality tan theta < -1 that cuts the pair down to the '
    'single root -3 before the two pieces are added. '
    'Rubric F3 C2 P3 T3 L1 = 12/15, clearing the gate that demands a total of at least 12 together with '
    'T = 3 -> level: ยากมาก. '
    'F = 3 for three separate knowledge blocks that must all be owned before the item can move: the '
    'Pythagorean identity used to collapse a sum of reciprocal squares, the quadrant rule for the signs '
    'of sine, cosine and their product, and the monotone behaviour of the tangent on an interval between '
    'two consecutive asymptotes, which is what converts a range of angles into a range of tangent values; '
    'F is not higher because 3 is the ceiling. C = 2 because two constraints of completely different '
    'kinds, one an equation and one an interval, have to be fused before either is usable, and the '
    'interval has to be spent twice for two different purposes, first for a sign and later for a '
    'magnitude; it is not 3 because both constraints are handed over explicitly and neither has to be '
    'manufactured by the student. P = 3 for a chain of seven stages that cannot be reordered, since the '
    'square root cannot be signed until the quadrant is read, the tangent equation cannot be written '
    'until the product is signed, the quadratic cannot be factored until that equation exists and the '
    'root cannot be chosen until both roots are in hand; the q129 companion of this same batch was '
    'capped at P = 3 for a chain of the same depth. T = 3 because three independent turning points sit '
    'in the item and missing any single one lands the student on a value that is actually present among '
    'the four listed ratios: recovering the sign that squaring destroyed, noticing that the two roots '
    'are reciprocals and therefore share a sign so that the quadrant test is powerless, and reading the '
    'upper endpoint of the interval as the only instrument that can separate them. The second and third '
    'turns are the decisive ones and follow the q129 precedent for T = 3, where several unrelated '
    'insights must all be found before the answer can be pinned. L = 1 and not 0 because no picture is '
    'supplied and the student has to draw the unit circle, or equivalently the tangent curve on that '
    'interval, before the endpoint 3pi/4 can be turned into an inequality; it is not 2 because there is '
    'nothing to model and no scene to translate, only a graph to picture. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b20.py): simplify(1/sin(th)**2 + 1/cos(th)**2 - 1/(sin(th)*cos(th))**2) returns 0, '
    'which is the machine proof of the collapse performed in step 1; solve(3*t**2 + 10*t + 3, t) returns '
    '[-3, -1/3] and factor returns (t + 3)*(3*t + 1), so the pair of roots and the factorisation shown in '
    'the explanation are both confirmed. The two candidate angles pi - atan(3) and pi - atan(1/3) were '
    'then filtered by machine against both clauses of the statement at once, and exactly one survives: '
    'N(pi - atan(3)) is about 1.8925 and lies between 1.5708 and 2.3562, while N(pi - atan(1/3)) is about '
    '2.8198 and overshoots the upper endpoint, even though simplify of 1/sin^2 + 1/cos^2 returns 100/9 at '
    'both angles, which is the machine statement of the central trap that the equation alone cannot '
    'separate the roots. For the survivor, tan evaluates to -3, sin*cos evaluates to -3/10 and the '
    'requested sum evaluates to -33/10. Every wrong value in the pitfalls block was computed by machine '
    'from its named error path rather than invented: keeping the positive root of the product gives '
    '-3 + 3/10 = -27/10; keeping the second tangent root gives tan + sin*cos at pi - atan(1/3), which '
    'sympy returns as -19/30; ignoring the range entirely gives 3 + 3/10 = 33/10; and the reciprocal slip '
    'that reads (sin cos)^2 = 100/9 refutes itself, since sin*cos equals sin(2*theta)/2 and so has '
    'magnitude at most 1/2 while 10/3 is about 3.333. The independent check was run on constructed values '
    'as well: with sin = 3/sqrt(10) and cos = -1/sqrt(10), sympy returns sin^2 + cos^2 = 1, '
    '1/sin^2 + 1/cos^2 = 100/9, sin*cos = -3/10 and sin/cos = -3, so the whole answer stands on values '
    'that were built forwards rather than on the derivation being trusted. '
    'Collision sweep on 6417 items (bank 63 files + k1 out + k2 out), probe collide_b20.py / '
    'collide_b20b.py: the scan for a stem that hands over a reciprocal square sum as the datum to be '
    'solved returns zero items in the whole corpus. The only three stems that carry that shape at all '
    'carry it for other purposes: pat1-2554-12-q43, where the sines belong to the sides of a triangle; '
    'pat1-2558-10-q06, where sec squared and csc squared sit on top of arc functions and the expression '
    'is merely evaluated; and chap-07-trigonometry-q141, where the whole thing is an identity to be '
    'simplified with no unknown angle anywhere, so none of them asks the student to solve for an angle. '
    'The narrower pair of a range strictly inside one quadrant crossed with a reciprocal pair of tangent '
    'roots also returns zero. The two neighbours that pin an angle between 3pi/4 and pi, '
    'chap-07-trigonometry-q48 and chap-07-trigonometry-q167, both hand over a datum of the sin-plus-cos '
    'or cos-squared-minus-sin-squared family and use the range only to fix a single sign, never to '
    'separate two roots that already share one; pat1-2563-02-q08 is the closest item by surface, since '
    'it also restricts the angle and also asks for a tangent expression, but its datum is sin x + cos x '
    'set equal to a constant, a mould this batch is forbidden to touch, and its range is a full quadrant '
    'that does no cutting work at all; and gen-chap-07-trigonometry-q100, the only other 7.4 item that '
    'puts tan and cot together, is a pure identity simplification with no numbers, so it shares neither '
    'A nor M. Choices are ordered by numerical value from small to large, -33/10 = -3.3, then '
    '-27/10 = -2.7, then -19/30 about -0.633, then 33/10 = 3.3, so the answer slot is forced by that '
    'rule and was not positioned by hand.',
)

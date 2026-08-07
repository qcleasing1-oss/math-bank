# -*- coding: utf-8 -*-
add(
    143,
    ['7.4'],
    'ยาก',
    'กำหนดให้ $\\theta$ เป็นจำนวนจริงซึ่ง $-\\dfrac{\\pi}{2} < \\theta < \\dfrac{\\pi}{2}$ '
    'และ $\\dfrac{\\cos\\theta}{1 - \\sin\\theta} = 3$ '
    'ค่าของ $\\dfrac{1 + \\sin\\theta}{\\cos\\theta} + \\tan\\theta$ เท่ากับข้อใด',
    [
        '$-\\dfrac{13}{3}$',
        '$\\dfrac{5}{3}$',
        '$\\dfrac{15}{4}$',
        '$\\dfrac{13}{3}$',
    ],
    3,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เอกลักษณ์พีทาโกรัส : $\\sin^2\\theta + \\cos^2\\theta = 1$ '
        'ที่มาของเอกลักษณ์นี้คือจุด $(\\cos\\theta , \\sin\\theta)$ อยู่บนวงกลมหนึ่งหน่วยเสมอ '
        'ระยะจากจุดกำเนิดถึงจุดนั้นจึงเท่ากับ $1$ ⇒ ยกกำลังสองตามพีทาโกรัสได้เอกลักษณ์ข้างต้น · '
        'รูปที่ข้อนี้ต้องใช้คือย้ายข้างเป็น $\\cos^2\\theta = 1 - \\sin^2\\theta$ '
        'แล้วแยกตัวประกอบผลต่างกำลังสองฝั่งขวาได้เป็น '
        '$1 - \\sin^2\\theta = (1 - \\sin\\theta)(1 + \\sin\\theta)$ '
        '⇒ ก้อน $1 - \\sin\\theta$ กับก้อน $1 + \\sin\\theta$ เป็น<b>คู่หู</b>ที่คูณกันแล้วยุบเป็น $\\cos^2\\theta$ พอดี',
        '• ⭐ <b>คู่สังยุคที่เป็นหัวใจของข้อนี้</b> : เมื่อเจอเศษส่วนที่มี $1 - \\sin\\theta$ อยู่ที่ตัวส่วน '
        'ให้คูณทั้งเศษและส่วนด้วย $1 + \\sin\\theta$ ซึ่งเป็นคู่สังยุคของมัน '
        'การคูณแบบนี้ไม่เปลี่ยนค่าของเศษส่วนเลย เพราะเท่ากับคูณด้วย $\\dfrac{1 + \\sin\\theta}{1 + \\sin\\theta}$ '
        'ซึ่งก็คือคูณด้วย $1$ นั่นเอง ⇒ ผลที่ได้คือ '
        '$\\dfrac{\\cos\\theta}{1 - \\sin\\theta} = \\dfrac{1 + \\sin\\theta}{\\cos\\theta}$ '
        '<b>เป็นจริงทุกค่าของ $\\theta$ ที่ทั้งสองฝั่งนิยามได้</b> ⛔ ไม่ใช่จริงเฉพาะบางค่า',
        '• นิยามของ $\\tan$ ในรูปของ $\\sin$ กับ $\\cos$ : $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        '⇒ ถ้ารู้ทั้ง $\\sin\\theta$ และ $\\cos\\theta$ แล้ว จะได้ $\\tan\\theta$ ทันทีด้วยการหาร '
        'และเห็นได้เลยว่า $\\tan\\theta$ จะหาค่าไม่ได้เมื่อ $\\cos\\theta = 0$',
        '• ช่วง $-\\dfrac{\\pi}{2} < \\theta < \\dfrac{\\pi}{2}$ บอกอะไร : '
        'มุมในช่วงนี้วางอยู่ในจตุภาคที่ $1$ หรือจตุภาคที่ $4$ หรือเป็นมุม $0$ '
        'ซึ่งทั้งหมดเป็นครึ่งขวาของวงกลมหนึ่งหน่วย จุดปลายรัศมีจึงมีพิกัดที่หนึ่งเป็นบวกเสมอ '
        '⇒ <b>$\\cos\\theta > 0$ แน่นอน</b> · ข้อมูลบรรทัดนี้คือสิ่งที่ใช้ตัดสินเครื่องหมายตอนถอดกรณฑ์ '
        'และเป็นเหตุผลที่โจทย์ต้องให้ช่วงมา ไม่ได้ให้มาเป็นของแถม',
        '• <b>รากแปลกปลอม</b> คืออะไร : การยกกำลังสองทั้งสองข้างของสมการเป็นการเดินทางเที่ยวเดียว '
        'ทุกคำตอบของสมการเดิมยังเป็นคำตอบของสมการใหม่ แต่สมการใหม่อาจมีคำตอบส่วนเกินโผล่มาด้วย '
        'เพราะ $A = B$ กับ $A^2 = B^2$ ไม่เท่ากัน (ตัวหลังยอมรับกรณี $A = -B$ เข้ามาด้วย) '
        '⇒ หลังยกกำลังสองต้อง<b>แทนรากทุกตัวกลับเข้าสมการเดิม</b>เสมอ แล้วตัดตัวที่ไม่ผ่านทิ้ง',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $\\theta$ เป็นจำนวนจริงในช่วง $-\\dfrac{\\pi}{2} < \\theta < \\dfrac{\\pi}{2}$ '
        '(เป็นช่วงเปิด ⇒ ปลายทั้งสองข้างไม่ถูกนับรวม)',
        '• $\\dfrac{\\cos\\theta}{1 - \\sin\\theta} = 3$',
        '• เงื่อนไขแฝงที่ตัวโจทย์บังคับมาเองโดยไม่ต้องเขียน : ตัวส่วนของสมการที่ให้มาต้องไม่เป็นศูนย์ '
        '⇒ $1 - \\sin\\theta \\ne 0$ นั่นคือ $\\sin\\theta \\ne 1$ · '
        'และนิพจน์ที่โจทย์ถามมี $\\cos\\theta$ อยู่ที่ตัวส่วน ⇒ $\\cos\\theta \\ne 0$ ด้วย',
        '• สังเกตหน้าตาก่อนลงมือ : สิ่งที่โจทย์<b>ให้</b>คือ $\\dfrac{\\cos\\theta}{1 - \\sin\\theta}$ '
        'ส่วนก้อนแรกที่โจทย์<b>ถาม</b>คือ $\\dfrac{1 + \\sin\\theta}{\\cos\\theta}$ '
        'สองก้อนนี้สลับที่กันระหว่างเศษกับส่วน และเปลี่ยนเครื่องหมายกลางจากลบเป็นบวก '
        '⇒ นี่คือหน้าตาของ<b>คู่สังยุค</b> ซึ่งเป็นสัญญาณว่าอย่าเพิ่งรีบแก้สมการ ให้ลองยุบดูก่อน',
        '• สังเกตอีกอย่าง : โจทย์ถามผลบวกของสองก้อน ⇒ ต้องได้ครบทั้งสองก้อนถึงจะตอบได้ '
        'ก้อนที่สองคือ $\\tan\\theta$ ซึ่งไม่ใช่คู่สังยุคของอะไรเลย ⇒ ก้อนนี้ต้องลงแรงหาจริง ๆ',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\dfrac{1 + \\sin\\theta}{\\cos\\theta} + \\tan\\theta$ '
        'ซึ่งเป็นจำนวนจริงจำนวนเดียว โดยใช้สมการกับช่วงที่โจทย์ให้มาเท่านั้น',
        '',
        '<b>【 ⭐ มองให้ออกว่าก้อนแรกที่โจทย์ถามคือคู่สังยุคของก้อนที่โจทย์ให้ ค่าจึงเท่ากับ $3$ ทันที '
        'โดยไม่ต้องรู้ $\\sin\\theta$ หรือ $\\cos\\theta$ เลย จากนั้นจึงค่อยลงแรงหา $\\tan\\theta$ '
        'ด้วยการเปลี่ยนสมการที่โจทย์ให้เป็นสมการของ $\\sin\\theta$ ยกกำลังสอง แยกตัวประกอบ '
        'แล้วตัดรากแปลกปลอมที่ทำให้ตัวส่วนเป็นศูนย์ทิ้ง 】</b>',
        '',
        '<b>ขั้นที่ 1 · ⭐ กุญแจดอกที่ 1 — คูณคู่สังยุค แล้วก้อนแรกที่โจทย์ถามจะเท่ากับ $3$ ทันที</b>',
        '• สูตรที่ใช้ : คูณเศษและส่วนด้วยจำนวนเดียวกันแล้วค่าไม่เปลี่ยน '
        'นั่นคือ $\\dfrac{P}{Q} = \\dfrac{P \\times R}{Q \\times R}$ เมื่อ $R \\ne 0$ '
        'ที่นี่เลือก $R = 1 + \\sin\\theta$ เพราะมันเป็นคู่สังยุคของตัวส่วน $1 - \\sin\\theta$',
        '• ระบุตัวแปรให้ชัดก่อนลงมือ : $P = \\cos\\theta$ คือเศษของก้อนที่โจทย์ให้ '
        '· $Q = 1 - \\sin\\theta$ คือส่วนของก้อนนั้น · $R = 1 + \\sin\\theta$ คือคู่สังยุคที่จะเอามาคูณ',
        '• แทนค่าแล้วเดินทีละก้าว ก้าวที่ 1 คูณคู่สังยุคเข้าไปทั้งบนและล่าง : '
        '$\\dfrac{\\cos\\theta}{1 - \\sin\\theta} '
        '= \\dfrac{\\cos\\theta\\,(1 + \\sin\\theta)}{(1 - \\sin\\theta)(1 + \\sin\\theta)}$',
        '• ก้าวที่ 2 ยุบตัวส่วนด้วยผลต่างกำลังสอง : $(1 - \\sin\\theta)(1 + \\sin\\theta) = 1 - \\sin^2\\theta$ '
        '⇒ $= \\dfrac{\\cos\\theta\\,(1 + \\sin\\theta)}{1 - \\sin^2\\theta}$',
        '• ก้าวที่ 3 ใช้เอกลักษณ์พีทาโกรัสเปลี่ยนตัวส่วนให้เป็น $\\cos$ : $1 - \\sin^2\\theta = \\cos^2\\theta$ '
        '⇒ $= \\dfrac{\\cos\\theta\\,(1 + \\sin\\theta)}{\\cos^2\\theta}$',
        '• ก้าวที่ 4 ตัดทอน $\\cos\\theta$ ที่เศษกับที่ส่วนออกหนึ่งตัว (ตัดได้เพราะ $\\cos\\theta \\ne 0$) '
        '⇒ $= \\dfrac{1 + \\sin\\theta}{\\cos\\theta}$',
        '• 🔴 <b>สรุปกุญแจดอกที่ 1 ให้ชัด</b> : เราเพิ่งพิสูจน์ว่า '
        '$\\dfrac{\\cos\\theta}{1 - \\sin\\theta}$ กับ $\\dfrac{1 + \\sin\\theta}{\\cos\\theta}$ '
        'เป็นนิพจน์<b>เดียวกัน</b> เขียนคนละหน้าตาเท่านั้น ⇒ ค่าของทั้งสองต้องเท่ากันเสมอ '
        'โจทย์บอกว่าก้อนซ้ายเท่ากับ $3$ ⇒ $\\dfrac{1 + \\sin\\theta}{\\cos\\theta} = 3$ ทันที '
        '⛔ ไม่ต้องหา $\\sin\\theta$ หรือ $\\cos\\theta$ ก่อนแม้แต่นิดเดียว นี่คือหัวใจของข้อนี้',
        '',
        '<b>ขั้นที่ 2 · กุญแจดอกที่ 2 — เปลี่ยนสมการที่โจทย์ให้เป็นสมการของ $\\sin\\theta$ แล้วแก้</b>',
        '• ทำไมยังต้องทำงานต่อ : ก้อนที่สองที่โจทย์ถามคือ $\\tan\\theta$ '
        'ซึ่งไม่ได้ยุบรวมกับก้อนแรกและไม่มีคู่สังยุคให้ใช้ ⇒ ต้องรู้ $\\sin\\theta$ กับ $\\cos\\theta$ จริง ๆ',
        '• สูตรที่ใช้ : คูณไขว้เพื่อเก็บกวาดตัวส่วนออกจากสมการที่โจทย์ให้ '
        '⇒ จาก $\\dfrac{\\cos\\theta}{1 - \\sin\\theta} = 3$ ได้ $\\cos\\theta = 3\\,(1 - \\sin\\theta)$',
        '• ระบุตัวแปร : ให้ $s = \\sin\\theta$ เพื่อให้เขียนสั้นลง '
        '· ในช่วง $-\\dfrac{\\pi}{2} < \\theta < \\dfrac{\\pi}{2}$ มี $\\cos\\theta > 0$ '
        '⇒ ถอดรากได้เป็น $\\cos\\theta = \\sqrt{1 - s^2}$ โดย<b>เลือกรากบวกอย่างเดียว</b>',
        '• แทนค่า : $\\sqrt{1 - s^2} = 3\\,(1 - s)$',
        '• ยกกำลังสองทั้งสองข้างเพื่อปลดกรณฑ์ : $1 - s^2 = 9\\,(1 - s)^2$',
        '• แยกตัวประกอบแทนการกระจาย เพราะทั้งสองข้างมีก้อน $1 - s$ ร่วมกันอยู่แล้ว : '
        'ฝั่งซ้าย $1 - s^2 = (1 - s)(1 + s)$ ⇒ สมการกลายเป็น $(1 - s)(1 + s) = 9\\,(1 - s)^2$',
        '• ย้ายทุกอย่างไปข้างเดียวแล้วดึงตัวร่วม $1 - s$ ออกมา : '
        '$(1 - s)\\left[(1 + s) - 9\\,(1 - s)\\right] = 0$ '
        '⇒ วงเล็บใหญ่ยุบเป็น $1 + s - 9 + 9s = 10s - 8$ ⇒ $(1 - s)(10s - 8) = 0$',
        '• ผลคูณเป็นศูนย์ ⇒ ตัวใดตัวหนึ่งเป็นศูนย์ ⇒ $s = 1$ <b>หรือ</b> $s = \\dfrac{8}{10} = \\dfrac{4}{5}$',
        '• ⛔ ระวังนิสัยอันตราย : ห้ามหารทั้งสองข้างด้วย $1 - s$ เพื่อความรวดเร็ว '
        'เพราะเราไม่รู้ว่า $1 - s$ เป็นศูนย์หรือไม่ การหารด้วยของที่อาจเป็นศูนย์ทำให้รากหายไปเงียบ ๆ '
        '⇒ ให้ย้ายข้างแล้วดึงตัวร่วมเสมอ',
        '',
        '<b>ขั้นที่ 3 · 🔴 ตัดรากแปลกปลอมทิ้ง แล้วอ่านค่า $\\cos\\theta$ กับ $\\tan\\theta$</b>',
        '• ตรวจราก $s = 1$ ก่อน : ถ้า $\\sin\\theta = 1$ แล้ว $\\cos^2\\theta = 1 - 1^2 = 0$ '
        '⇒ $\\cos\\theta = 0$ · แทนกลับเข้าสมการที่โจทย์ให้จะได้ '
        '$\\dfrac{\\cos\\theta}{1 - \\sin\\theta} = \\dfrac{0}{1 - 1} = \\dfrac{0}{0}$ ซึ่ง<b>หาค่าไม่ได้</b> '
        '⇒ ราก $s = 1$ ทำให้ตัวส่วนของโจทย์เป็นศูนย์ จึงไม่ใช่คำตอบของสมการเดิม ⇒ <b>ตัดทิ้ง</b>',
        '• ตัดซ้ำได้อีกทางหนึ่งด้วยช่วงที่โจทย์ให้ : $\\sin\\theta = 1$ เกิดขึ้นได้ที่ $\\theta = \\dfrac{\\pi}{2}$ เท่านั้น '
        'ซึ่งเป็นปลายช่วงที่โจทย์ไม่นับรวม ⇒ ตัดทิ้งซ้ำอีกรอบด้วยเหตุผลคนละข้อกัน',
        '• เหลือราก $s = \\dfrac{4}{5}$ เพียงตัวเดียว ⇒ $\\sin\\theta = \\dfrac{4}{5}$',
        '• หา $\\cos\\theta$ จากสมการที่จัดรูปไว้ในขั้นที่ 2 : $\\cos\\theta = 3\\,(1 - \\sin\\theta)$ '
        '⇒ แทนค่า $\\cos\\theta = 3\\left(1 - \\dfrac{4}{5}\\right) = 3 \\times \\dfrac{1}{5} = \\dfrac{3}{5}$ '
        '· ได้ค่าบวก ✓ ตรงกับช่วงที่โจทย์ให้ ⇒ รากนี้ผ่านการตรวจ',
        '• หา $\\tan\\theta$ จากนิยาม : $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        '⇒ แทนค่า $\\tan\\theta = \\dfrac{4}{5} \\div \\dfrac{3}{5}$ '
        '⇒ ยุบ : หารเศษส่วนคือคูณด้วยส่วนกลับ $= \\dfrac{4}{5} \\times \\dfrac{5}{3} = \\dfrac{4}{3}$',
        '',
        '<b>ขั้นที่ 4 · รวมสองก้อนเข้าด้วยกันเป็นคำตอบ</b>',
        '• สูตรที่ใช้ : นิพจน์ที่โจทย์ถาม $= \\dfrac{1 + \\sin\\theta}{\\cos\\theta} + \\tan\\theta$',
        '• ระบุตัวแปร : ก้อนแรก $= 3$ ได้จากกุญแจดอกที่ 1 ในขั้นที่ 1 '
        '· ก้อนที่สอง $= \\tan\\theta = \\dfrac{4}{3}$ ได้จากขั้นที่ 3',
        '• แทนค่า : นิพจน์ $= 3 + \\dfrac{4}{3}$',
        '• ยุบ : ทำส่วนให้เท่ากันก่อน $3 = \\dfrac{9}{3}$ '
        '⇒ $\\dfrac{9}{3} + \\dfrac{4}{3} = \\dfrac{9 + 4}{3} = \\dfrac{13}{3}$',
        '• ตรวจความสมเหตุสมผลอย่างเร็ว : $\\dfrac{13}{3} \\approx 4.33$ ซึ่งเป็นบวกและมากกว่า $3$ อยู่เล็กน้อย '
        'ตรงกับสามัญสำนึกว่าเราเอา $3$ มาบวกกับจำนวนบวกที่ไม่ถึง $2$ ✓',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่า $\\sin\\theta$ กับ $\\cos\\theta$ ที่ได้ '
        'กลับเข้าสมการต้นฉบับโดยตรง แล้วตรวจช่วงและเอกลักษณ์พีทาโกรัสซ้ำ)</b>',
        '• เส้นทางข้างบนเดินจากสมการไปหาค่า การตรวจรอบนี้เดินย้อนกลับ '
        'คือหยิบค่าที่ได้ไปแทนในเงื่อนไขทุกบรรทัดของโจทย์ ถ้าทุกบรรทัดเป็นจริงพร้อมกัน '
        'แปลว่าค่าที่หามาสอดคล้องกับโจทย์จริง ⛔ ไม่มีการใช้คู่สังยุคหรือการยกกำลังสองซ้ำอีกเลย',
        '• ตรวจสมการที่โจทย์ให้ : แทน $\\sin\\theta = \\dfrac{4}{5}$ และ $\\cos\\theta = \\dfrac{3}{5}$ '
        '⇒ ตัวส่วนคือ $1 - \\dfrac{4}{5} = \\dfrac{1}{5}$ '
        '⇒ $\\dfrac{\\cos\\theta}{1 - \\sin\\theta} = \\dfrac{3}{5} \\div \\dfrac{1}{5} '
        '= \\dfrac{3}{5} \\times 5 = 3$ ✓ ตรงกับที่โจทย์กำหนดเป๊ะ',
        '• ตรวจช่วงที่โจทย์กำหนด : $\\sin\\theta = \\dfrac{4}{5} > 0$ และ $\\cos\\theta = \\dfrac{3}{5} > 0$ '
        '⇒ จุดปลายรัศมีอยู่ในจตุภาคที่ $1$ ⇒ $0 < \\theta < \\dfrac{\\pi}{2}$ '
        'ซึ่งเป็นสับเซตของช่วง $-\\dfrac{\\pi}{2} < \\theta < \\dfrac{\\pi}{2}$ ✓',
        '• ตรวจเอกลักษณ์พีทาโกรัส เพื่อยืนยันว่าคู่ค่านี้เป็นคู่ที่มีอยู่จริงบนวงกลมหนึ่งหน่วย : '
        '$\\left(\\dfrac{4}{5}\\right)^2 + \\left(\\dfrac{3}{5}\\right)^2 '
        '= \\dfrac{16}{25} + \\dfrac{9}{25} = \\dfrac{25}{25} = 1$ ✓',
        '• ตรวจกุญแจดอกที่ 1 ด้วยตัวเลขจริง ⭐ (คำนวณตรง ๆ ไม่ผ่านเอกลักษณ์) : '
        '$\\dfrac{1 + \\sin\\theta}{\\cos\\theta} = \\dfrac{1 + \\dfrac{4}{5}}{\\dfrac{3}{5}} '
        '= \\dfrac{9}{5} \\div \\dfrac{3}{5} = 3$ ✓ '
        'ได้ $3$ เท่ากับก้อนที่โจทย์ให้จริง ⇒ ยืนยันว่าที่ขั้นที่ 1 อ้างว่าสองก้อนเท่ากันนั้นถูกต้อง',
        '• ประกอบคำตอบใหม่จากค่าที่ตรวจแล้ว : $3 + \\dfrac{4}{3} = \\dfrac{13}{3}$ ✓ '
        'ได้ค่าเดิมเป็นครั้งที่สอง โดยเดินคนละทาง',
        '',
        '✅ <b>คำตอบ</b> ค่าของ $\\dfrac{1 + \\sin\\theta}{\\cos\\theta} + \\tan\\theta$ '
        'เท่ากับ $\\dfrac{13}{3}$ → <b>ตัวเลือก 4</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• ท่องคู่สังยุคสามคู่ที่ออกสอบบ่อยที่สุดไว้ให้ขึ้นใจ : '
        '$1 - \\sin\\theta$ คู่กับ $1 + \\sin\\theta$ (คูณกันได้ $\\cos^2\\theta$) · '
        '$1 - \\cos\\theta$ คู่กับ $1 + \\cos\\theta$ (คูณกันได้ $\\sin^2\\theta$) · '
        '$\\sec\\theta - \\tan\\theta$ คู่กับ $\\sec\\theta + \\tan\\theta$ (คูณกันได้ $1$) · '
        'พอเห็นก้อนใดก้อนหนึ่งในสามคู่นี้โผล่มาที่ตัวส่วน ให้นึกถึงการคูณคู่สังยุคเป็นอย่างแรกเสมอ',
        '• อ่านสิ่งที่โจทย์ถามให้จบก่อนลงมือคำนวณ ถ้าก้อนที่ถามมีหน้าตาเป็นคู่สังยุคของก้อนที่โจทย์ให้ '
        'ให้ทดลองยุบก่อนเลยทันที เพราะบ่อยครั้งค่าจะโผล่มาฟรี ๆ โดยไม่ต้องแก้สมการสักบรรทัด '
        'ประหยัดเวลาในห้องสอบได้มหาศาลและตัดโอกาสคำนวณผิดไปหนึ่งเส้นทางเต็ม ๆ',
        '• กฎเหล็กที่ต้องติดตัว : ทุกครั้งที่ยกกำลังสองสองข้างของสมการ หรือทุกครั้งที่คูณไขว้ตัวส่วนออก '
        'ต้องแทนรากทุกตัวกลับเข้าสมการ<b>ต้นฉบับ</b>เสมอ ⛔ ไม่ใช่แทนกลับเข้าสมการที่จัดรูปแล้ว '
        'เพราะรากแปลกปลอมมักผ่านสมการที่จัดรูปแล้วได้สบาย แต่จะตกทันทีเมื่อเจอสมการต้นฉบับ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ถ้าได้ค่า $-\\dfrac{13}{3}$ แปลว่าหลังยกกำลังสองแล้วไปหยิบรากลบของ $\\cos\\theta$ มาใช้ '
        'คือใช้ $\\sin\\theta = \\dfrac{4}{5}$ คู่กับ $\\cos\\theta = -\\dfrac{3}{5}$ '
        '⇒ ได้ $\\dfrac{1 + \\sin\\theta}{\\cos\\theta} = \\dfrac{9}{5} \\div \\left(-\\dfrac{3}{5}\\right) = -3$ '
        'และ $\\tan\\theta = -\\dfrac{4}{3}$ ⇒ รวมกันได้ $-3 - \\dfrac{4}{3} = -\\dfrac{13}{3}$ · '
        'ค่านี้ผิดสองชั้น ชั้นแรกคือขัดกับช่วงที่โจทย์ให้ เพราะ $-\\dfrac{\\pi}{2} < \\theta < \\dfrac{\\pi}{2}$ '
        'บังคับให้ $\\cos\\theta > 0$ · ชั้นที่สองพิสูจน์ด้วยการแทนกลับ : '
        '$\\dfrac{-\\dfrac{3}{5}}{1 - \\dfrac{4}{5}} = -3$ ซึ่งไม่เท่ากับ $3$ ที่โจทย์กำหนด ⇒ ตกตั้งแต่บรรทัดแรกของโจทย์',
        '• ถ้าได้ค่า $\\dfrac{5}{3}$ แปลว่าเห็นว่าก้อนที่ถามกับก้อนที่ให้มีเศษกับส่วนสลับที่กัน '
        'แล้วรีบสรุปว่าเป็น<b>ส่วนกลับ</b>ของกัน จึงใช้ $\\dfrac{1 + \\sin\\theta}{\\cos\\theta} = \\dfrac{1}{3}$ '
        '⇒ รวมกับ $\\tan\\theta = \\dfrac{4}{3}$ ได้ $\\dfrac{1}{3} + \\dfrac{4}{3} = \\dfrac{5}{3}$ · '
        'ค่านี้ผิดเพราะเครื่องหมายกลางเปลี่ยนจากลบเป็นบวกไปด้วย ไม่ได้สลับที่เฉย ๆ '
        'ส่วนกลับที่แท้จริงของ $\\dfrac{\\cos\\theta}{1 - \\sin\\theta}$ คือ $\\dfrac{1 - \\sin\\theta}{\\cos\\theta}$ '
        'ซึ่งมีเครื่องหมายลบ ⛔ ไม่ใช่ก้อนที่โจทย์ถาม · '
        'พิสูจน์ด้วยตัวเลขจริงได้ทันที : $\\dfrac{1 + \\dfrac{4}{5}}{\\dfrac{3}{5}} = 3$ ⛔ ไม่ใช่ $\\dfrac{1}{3}$',
        '• ถ้าได้ค่า $\\dfrac{15}{4}$ แปลว่าสลับค่าของ $\\sin\\theta$ กับ $\\cos\\theta$ กันตอนอ่านคำตอบ '
        'คือหยิบ $\\sin\\theta = \\dfrac{3}{5}$ กับ $\\cos\\theta = \\dfrac{4}{5}$ ⇒ $\\tan\\theta = \\dfrac{3}{4}$ '
        '⇒ รวมกับก้อนแรกได้ $3 + \\dfrac{3}{4} = \\dfrac{15}{4}$ · '
        'ค่านี้ผิด พิสูจน์ด้วยการแทนกลับเข้าสมการที่โจทย์ให้ : '
        '$\\dfrac{\\dfrac{4}{5}}{1 - \\dfrac{3}{5}} = \\dfrac{4}{5} \\div \\dfrac{2}{5} = 2$ '
        'ซึ่งได้ $2$ ⛔ ไม่ใช่ $3$ ⇒ คู่ค่าที่สลับกันนี้ไม่สอดคล้องกับโจทย์ตั้งแต่ต้น',
        '• ถ้าได้ค่า $3$ แปลว่าเห็นกุญแจดอกที่ 1 ออกแล้ว แต่หยุดแค่ก้อนแรก ลืมบวก $\\tan\\theta$ ปิดท้าย · '
        'สัญญาณเตือนคือคำตอบที่จะวงยังไม่ได้ใช้เครื่องหมายบวกที่เขียนอยู่กลางนิพจน์ที่โจทย์ถามเลย · '
        'อีกเส้นทางหนึ่งที่พังคนละแบบคือเก็บราก $s = 1$ ไว้แล้วพยายามคิดต่อ '
        'ซึ่งจะพาไปเจอ $\\cos\\theta = 0$ ทำให้ทั้ง $\\tan\\theta$ และตัวส่วนของโจทย์หาค่าไม่ได้ '
        '⇒ ถ้าคิดแล้วเจอ $0$ อยู่ที่ตัวส่วนเมื่อไร แปลว่ากำลังถือรากแปลกปลอมอยู่ ต้องย้อนกลับไปตัดทิ้ง',
    ],
    'V.mold: G = a real number theta pinned to the open interval from -pi/2 to pi/2 together with one '
    'numerical equation, cos(theta) / (1 - sin(theta)) = 3, and nothing else / A = the value of the '
    'two-term expression (1 + sin(theta)) / cos(theta) + tan(theta) / M = see first that the leading '
    'term of the requested expression is the conjugate rewriting of the quotient that was handed over, '
    'so it equals 3 with no computation at all, then earn the second term by cross multiplying the given '
    'equation into cos(theta) = 3 * (1 - sin(theta)), replacing cos(theta) by the positive root '
    'sqrt(1 - s**2) that the stated interval forces, squaring, pulling the common factor (1 - s) out '
    'instead of dividing by it, and discarding the extraneous root s = 1 because it is exactly the value '
    'that zeroes the denominator of the given equation. '
    'Rubric F2 C2 P2 T2 L0 = 8/15 with the total at or above 8 and T at least 2 -> level: ยาก. '
    'F = 2 because two knowledge blocks are both required and neither closes the item alone: the '
    'Pythagorean identity in its factored form (1 - sin)(1 + sin) = cos**2, which is what makes the '
    'conjugate multiplication collapse, and the sign rule that reads cos(theta) > 0 off the stated '
    'interval, which is what makes the square root single valued. F was not raised to 3 because both '
    'are first-course facts used in their plainest form, with no auxiliary angle, no sum or difference '
    'formula and no half-angle work anywhere in the solution. C = 2 because the item really is two '
    'independent keys wired in series: the conjugate observation delivers the first term outright and '
    'gives no information about tan(theta) whatsoever, while the equation solving delivers tan(theta) '
    'and never needed the conjugate, so a solver who owns only one key finishes with only half the '
    'answer. P = 2 because the arithmetic is short once the plan exists, being one cross multiplication, '
    'one squaring, one factorisation of a linear-times-linear product and one addition of fractions, but '
    'it is still a chain of stages where a later stage cannot start before an earlier one closes. T = 2 '
    'for two hidden conditions that the statement never spells out: the squaring step manufactures the '
    'root s = 1, which is precisely the value that makes the given denominator 1 - sin(theta) vanish and '
    'must therefore be thrown away, and the same squaring erases the sign of cos(theta), which only the '
    'interval can restore. T was held at 2 and not raised to 3 because the interval is handed over '
    'openly in the first line of the statement, so the sign question is answered by reading rather than '
    'by case analysis, and because the discarded root is exposed by a single substitution back into the '
    'original equation. L = 0 because the item is purely symbolic, with no figure to picture, no scene '
    'to model and no quantity to name before the algebra can start. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b20.py): simplify(cos(th) / (1 - sin(th)) - (1 + sin(th)) / cos(th)) returns 0, which '
    'is the machine statement of the central claim that the two expressions are one and the same, so the '
    'leading term is 3 by substitution alone. solve(Eq(sqrt(1 - s**2), 3 * (1 - s)), s) returns the pair '
    '[4/5, 1], confirming both that the factorisation (1 - s) * (10 * s - 8) = 0 is complete and that '
    'the extra root really is s = 1, and expand of that product reproduces the squared equation term by '
    'term. At th0 = asin(4/5) the machine returns cos(th0) / (1 - sin(th0)) = 3, matching the statement, '
    '(1 + sin(th0)) / cos(th0) = 3, matching the conjugate claim numerically as well as symbolically, '
    'tan(th0) = 4/3, and the requested sum = 13/3. Every wrong value was machine-computed from a named '
    'error path rather than invented: -3 - 4/3 returns -13/3 for the branch that keeps the negative '
    'cosine, and the same branch was pushed back through the statement, where (-3/5) / (1 - 4/5) returns '
    '-3 instead of 3, so it fails the given equation outright; 1/3 + 4/3 returns 5/3 for reading the '
    'requested term as the reciprocal of the given quotient; 3 + 3/4 returns 15/4 for swapping the sine '
    'and cosine values, and that swap was also pushed back through the statement, where (4/5) / '
    '(1 - 3/5) returns 2 instead of 3. The independent check was machine-verified too: (4/5)**2 + '
    '(3/5)**2 returns 1, and asin(4/5) evaluates to about 0.927, which sits inside the interval. '
    'Collision sweep on 6437 items (bank 63 files + k1 out + k2 out), probe collide_b20.py / '
    'collide_b20b.py: the exact configuration of this item, a quotient with cos on top and 1 - sin '
    'underneath, returns 0 items across the whole corpus, whether the scan reads stems only or stems '
    'together with choices and full explanations. The nearest relatives share vocabulary and nothing '
    'else. gen-chap-07-trigonometry-q007 hands over sec A - tan A = 1/3 inside a right triangle and asks '
    'for sin A, so its G is a triangle rather than an interval on the line and its M is the sec-tan '
    'conjugate used to build a system of two equations. gen-chap-07-trigonometry-q083 is an equation to '
    'be solved over a full turn using the same sec-tan conjugate, so its A is a sum of sine and cosine '
    'and its M is equation solving with branch counting. gen-chap-07-trigonometry-q100 asks for the '
    'simplified form of a symmetric two-fraction expression with no numerical data at all, so it has no '
    'G worth comparing and its A is an identity rather than a value. chap-07-trigonometry-q04 contains '
    'the ratio (1 + sin x) / (1 - sin x) but wraps it in a logarithm and asks for an equivalent '
    'logarithmic form, which is a different chapter pairing entirely. The pair that defines this item, a '
    'conjugate quotient given as a number together with a request for the value of its twin plus a '
    'tangent, returns 0 items. Choices are ordered ascending by numeric value (-13/3, then 5/3, then '
    '15/4, then 13/3), so the answer slot is forced by that rule and was not chosen.',
)

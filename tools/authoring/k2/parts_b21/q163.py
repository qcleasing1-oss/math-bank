# -*- coding: utf-8 -*-
add(
    163,
    ['7.4'],
    'ปานกลาง',
    'กำหนดให้ $k$ เป็นจำนวนจริงซึ่งทำให้ $\\left(\\sin\\theta + \\csc\\theta\\right)^2 + '
    '\\left(\\cos\\theta + \\sec\\theta\\right)^2 = k + \\tan^2\\theta + \\cot^2\\theta$ '
    'เป็นจริงสำหรับทุกจำนวนจริง $\\theta$ ที่ $\\sin\\theta\\cos\\theta \\ne 0$ แล้ว $k$ เท่ากับข้อใด',
    [
        '$3$',
        '$5$',
        '$6$',
        '$7$',
    ],
    3,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ฟังก์ชันตรีโกณมิติสามตัวหลังเป็นเพียง<b>ส่วนกลับ</b>ของสามตัวแรก ไม่ใช่ของใหม่ที่ต้องท่องเพิ่ม : '
        '$\\csc\\theta = \\dfrac{1}{\\sin\\theta}$ · $\\sec\\theta = \\dfrac{1}{\\cos\\theta}$ · '
        '$\\cot\\theta = \\dfrac{\\cos\\theta}{\\sin\\theta}$ · เพราะทั้งสามตัวมีตัวส่วน '
        'จึงต้องมีเงื่อนไขกำกับว่าตัวส่วนห้ามเป็นศูนย์ ⇒ บรรทัด $\\sin\\theta\\cos\\theta \\ne 0$ '
        'ในโจทย์จึงไม่ได้โยนมาลอย ๆ แต่เป็นการรับประกันว่าทุกพจน์ในสมการหาค่าได้จริง',
        '• สูตรกำลังสองของผลบวก : $\\left(a+b\\right)^2 = a^2 + 2ab + b^2$ · '
        'พจน์กลาง $2ab$ เรียกว่า<b>พจน์ไขว้</b> และเป็นพจน์ที่หล่นหายบ่อยที่สุดเวลากระจาย · '
        'เหตุผลที่มันต้องมีอยู่คือ $\\left(a+b\\right)^2$ แปลว่า $\\left(a+b\\right)\\left(a+b\\right)$ '
        '⇒ แจกแจงแล้วได้สี่พจน์คือ $a\\cdot a$ , $a\\cdot b$ , $b\\cdot a$ และ $b\\cdot b$ '
        '⇒ สองพจน์ตรงกลางเท่ากันจึงรวมกันเป็น $2ab$ ⛔ ไม่มีทางที่ $\\left(a+b\\right)^2$ จะเท่ากับ $a^2+b^2$ '
        'เว้นแต่ $ab = 0$ ซึ่งข้อนี้เป็นไปไม่ได้',
        '• ⭐ <b>กุญแจดอกที่หนึ่งของข้อนี้</b> : เมื่อ $a$ กับ $b$ เป็น<b>ส่วนกลับของกันและกัน</b> '
        'พจน์ไขว้จะยุบเป็นค่าคงตัวทันที เพราะ $2ab = 2 \\cdot a \\cdot \\dfrac{1}{a} = 2$ · '
        'ในข้อนี้ $2\\sin\\theta\\csc\\theta = 2\\sin\\theta \\cdot \\dfrac{1}{\\sin\\theta} = 2$ '
        'และ $2\\cos\\theta\\sec\\theta = 2\\cos\\theta \\cdot \\dfrac{1}{\\cos\\theta} = 2$ '
        '⇒ ทั้งสองก้อนแจกค่าคงตัวมาให้ก้อนละ $2$ โดย<b>ไม่ขึ้นกับ</b> $\\theta$ เลยแม้แต่น้อย '
        '⇒ ค่าคงตัวเหล่านี้แหละที่จะไปโผล่เป็นส่วนหนึ่งของ $k$',
        '• เอกลักษณ์พีทาโกรัสกับลูกหลานสองตัวของมัน : ตัวแม่คือ $\\sin^2\\theta + \\cos^2\\theta = 1$ · '
        'หารทั้งสมการด้วย $\\sin^2\\theta$ จะได้ $1 + \\cot^2\\theta = \\csc^2\\theta$ · '
        'หารทั้งสมการด้วย $\\cos^2\\theta$ จะได้ $\\tan^2\\theta + 1 = \\sec^2\\theta$ '
        '⇒ สองบรรทัดหลังไม่ต้องท่องแยก แค่หยิบตัวแม่มาหารก็ได้มาเองทั้งคู่ '
        '⇒ และนี่คือสะพานเส้นเดียวที่จะพา $\\csc^2\\theta$ กับ $\\sec^2\\theta$ ฝั่งซ้าย '
        'ไปหา $\\cot^2\\theta$ กับ $\\tan^2\\theta$ ฝั่งขวาได้',
        '• ⭐ <b>กุญแจดอกที่สองของข้อนี้</b> คือความหมายของวลี “ เป็นจริงสำหรับทุกจำนวนจริง $\\theta$ ” : '
        'สมการที่เป็นจริงทุกค่าของตัวแปรเรียกว่า<b>เอกลักษณ์</b> ⇒ วิธีหาค่าคงตัวคือจัดรูปฝั่งซ้ายด้วยพีชคณิต'
        'จนหน้าตาเหมือนฝั่งขวาเป๊ะ แล้วจึงเทียบส่วนที่เป็นค่าคงตัวของทั้งสองฝั่ง · '
        '⛔ การแทนค่ามุมเพียงมุมเดียวแล้วแก้หา $k$ ยัง<b>ไม่ใช่การพิสูจน์</b> เพราะมันยืนยันได้แค่ว่าค่านั้นใช้ได้ที่มุมนั้น '
        '⇒ ใช้เป็นเครื่องมือ<b>ตรวจ</b>ได้ดีมาก แต่ใช้แทนการกระจายไม่ได้',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• สมการที่ให้มาคือ $\\left(\\sin\\theta + \\csc\\theta\\right)^2 + '
        '\\left(\\cos\\theta + \\sec\\theta\\right)^2 = k + \\tan^2\\theta + \\cot^2\\theta$',
        '• สมการนี้เป็นจริงสำหรับทุกจำนวนจริง $\\theta$ ที่ $\\sin\\theta\\cos\\theta \\ne 0$ '
        '⇒ เงื่อนไขนี้คือการตัดมุมที่ $\\sin\\theta = 0$ หรือ $\\cos\\theta = 0$ ทิ้ง '
        'เพราะมุมเหล่านั้นทำให้ $\\csc\\theta$ , $\\sec\\theta$ , $\\tan\\theta$ หรือ $\\cot\\theta$ หาค่าไม่ได้',
        '• $k$ เป็นจำนวนจริง<b>ค่าคงตัว</b>เพียงค่าเดียว ⇒ ห้ามให้คำตอบออกมาติด $\\theta$ อยู่ด้วย '
        'ถ้าจัดรูปแล้วยังเหลือ $\\theta$ ในคำตอบ แปลว่าเดินผิดทางแน่นอน',
        '• สังเกตหน้าตาก่อนลงมือ : ฝั่งซ้ายเป็นกำลังสองของ “ ฟังก์ชันบวกส่วนกลับของตัวมันเอง ” ถึงสองก้อน '
        '⇒ พจน์ไขว้ของทั้งสองก้อนจะกลายเป็นตัวเลขล้วน · ส่วนฝั่งขวามีแต่ $\\tan^2\\theta$ กับ $\\cot^2\\theta$ '
        '⇒ เป้าหมายระหว่างทางจึงชัดเจนว่าต้องแปลง $\\csc^2\\theta$ กับ $\\sec^2\\theta$ ที่โผล่มาฝั่งซ้าย'
        'ให้กลายเป็นสองตัวนี้ให้ได้ แล้วส่วนที่เหลือคือ $k$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $k$ ออกมาเป็นจำนวนจริงจำนวนเดียวที่ทำให้สมการเป็นจริงพร้อมกันทุกมุม',
        '',
        '<b>【 กระจายกำลังสองทั้งสองก้อนให้ครบทุกพจน์โดยไม่ทิ้งพจน์ไขว้ '
        'ซึ่งพจน์ไขว้ทั้งสองจะยุบเป็นเลข $2$ เพราะแต่ละก้อนเป็นผลบวกของฟังก์ชันกับส่วนกลับของมันเอง '
        'จากนั้นยุบ $\\sin^2\\theta + \\cos^2\\theta$ เป็น $1$ แล้วเปลี่ยน $\\csc^2\\theta$ เป็น '
        '$1 + \\cot^2\\theta$ กับ $\\sec^2\\theta$ เป็น $1 + \\tan^2\\theta$ '
        'จนสองฝั่งมีหางเหมือนกันแล้วจึงเทียบค่าคงตัว 】</b>',
        '',
        '<b>ขั้นที่ 1 · กระจายกำลังสองทั้งสองก้อน ⛔ ห้ามลืมพจน์ไขว้</b>',
        '• สูตรที่ใช้ : $\\left(a+b\\right)^2 = a^2 + 2ab + b^2$',
        '• ระบุตัวแปรของก้อนแรก : $a = \\sin\\theta$ และ $b = \\csc\\theta$',
        '• แทนค่าก้อนแรก : $\\left(\\sin\\theta + \\csc\\theta\\right)^2 = '
        '\\sin^2\\theta + 2\\sin\\theta\\csc\\theta + \\csc^2\\theta$',
        '• ยุบพจน์ไขว้ของก้อนแรก : $2\\sin\\theta\\csc\\theta = 2\\sin\\theta \\cdot '
        '\\dfrac{1}{\\sin\\theta} = 2$ ⇒ $\\left(\\sin\\theta + \\csc\\theta\\right)^2 = '
        '\\sin^2\\theta + 2 + \\csc^2\\theta$',
        '• ระบุตัวแปรของก้อนที่สอง : $a = \\cos\\theta$ และ $b = \\sec\\theta$',
        '• แทนค่าและยุบพจน์ไขว้ของก้อนที่สองด้วยวิธีเดียวกัน : '
        '$2\\cos\\theta\\sec\\theta = 2\\cos\\theta \\cdot \\dfrac{1}{\\cos\\theta} = 2$ '
        '⇒ $\\left(\\cos\\theta + \\sec\\theta\\right)^2 = \\cos^2\\theta + 2 + \\sec^2\\theta$',
        '• 📌 จุดที่ต้องหยุดดูให้ดี : พจน์ไขว้ทั้งสองก้อน<b>ไม่ได้หายไป</b> แต่กลายร่างเป็นเลข $2$ ก้อนละหนึ่งตัว '
        '⇒ รวมเป็นค่าคงตัว $4$ ที่จะติดอยู่ในผลลัพธ์ตลอดไป · ถ้าตรงนี้ทิ้งพจน์ไขว้ไป คำตอบสุดท้ายจะขาดไป $4$ ทันที',
        '',
        '<b>ขั้นที่ 2 · รวมสองก้อนเข้าด้วยกันแล้วยุบด้วยเอกลักษณ์พีทาโกรัส</b>',
        '• สูตรที่ใช้ : $\\sin^2\\theta + \\cos^2\\theta = 1$',
        '• นำผลจากขั้นที่ 1 มาบวกกัน : ฝั่งซ้าย $= \\left(\\sin^2\\theta + 2 + \\csc^2\\theta\\right) '
        '+ \\left(\\cos^2\\theta + 2 + \\sec^2\\theta\\right)$',
        '• จัดพจน์ใหม่โดยจับคู่ให้ตรงชนิดกัน : ฝั่งซ้าย $= \\left(\\sin^2\\theta + \\cos^2\\theta\\right) '
        '+ \\left(2 + 2\\right) + \\csc^2\\theta + \\sec^2\\theta$',
        '• แทนค่าเอกลักษณ์ : $\\sin^2\\theta + \\cos^2\\theta = 1$ และรวมค่าคงตัว $2 + 2 = 4$ '
        '⇒ ฝั่งซ้าย $= 1 + 4 + \\csc^2\\theta + \\sec^2\\theta = 5 + \\csc^2\\theta + \\sec^2\\theta$',
        '• ⭐ ตอนนี้ฝั่งซ้ายเหลือแค่ค่าคงตัว $5$ บวกกับกำลังสองของส่วนกลับสองตัว '
        '⇒ ยังเทียบกับฝั่งขวาไม่ได้ เพราะฝั่งขวาพูดด้วยภาษา $\\tan$ กับ $\\cot$ ไม่ใช่ $\\csc$ กับ $\\sec$ '
        '⇒ ต้องแปลภาษาให้ตรงกันก่อนในขั้นถัดไป',
        '',
        '<b>ขั้นที่ 3 · แปลง $\\csc^2\\theta$ กับ $\\sec^2\\theta$ ให้พูดภาษาเดียวกับฝั่งขวา</b>',
        '• สูตรที่ใช้ : $\\csc^2\\theta = 1 + \\cot^2\\theta$ และ $\\sec^2\\theta = 1 + \\tan^2\\theta$ '
        '· ทั้งคู่ได้มาจากการหารเอกลักษณ์พีทาโกรัสด้วย $\\sin^2\\theta$ และ $\\cos^2\\theta$ ตามลำดับ',
        '• แทนค่าลงในผลของขั้นที่ 2 : ฝั่งซ้าย $= 5 + \\left(1 + \\cot^2\\theta\\right) '
        '+ \\left(1 + \\tan^2\\theta\\right)$',
        '• รวมค่าคงตัวที่โผล่ออกมาใหม่ : $5 + 1 + 1 = 7$ '
        '⇒ ฝั่งซ้าย $= 7 + \\tan^2\\theta + \\cot^2\\theta$',
        '• 📌 นับที่มาของเลข $7$ ให้ครบทีละก้อนกันตกหล่น : มาจากเอกลักษณ์พีทาโกรัส $1$ · '
        'มาจากพจน์ไขว้สองตัว $2 + 2 = 4$ · มาจากการแปลง $\\csc^2\\theta$ อีก $1$ · '
        'และมาจากการแปลง $\\sec^2\\theta$ อีก $1$ ⇒ $1 + 4 + 1 + 1 = 7$',
        '',
        '<b>ขั้นที่ 4 · เทียบสองฝั่งแล้วอ่านค่า $k$</b>',
        '• สูตรที่ใช้ : ถ้านิพจน์สองนิพจน์เท่ากันทุกค่าของตัวแปร และจัดรูปมาอยู่ในหน้าตาเดียวกันแล้ว '
        'ส่วนที่เป็นค่าคงตัวของทั้งสองฝั่งต้องเท่ากัน',
        '• ระบุสิ่งที่จะเทียบ : ฝั่งซ้ายที่จัดรูปเสร็จแล้วคือ $7 + \\tan^2\\theta + \\cot^2\\theta$ · '
        'ฝั่งขวาที่โจทย์ให้มาคือ $k + \\tan^2\\theta + \\cot^2\\theta$',
        '• แทนค่าและตัดส่วนที่เหมือนกันออก : ทั้งสองฝั่งมีหาง $\\tan^2\\theta + \\cot^2\\theta$ เหมือนกันเป๊ะ '
        '⇒ ลบหางนี้ออกจากทั้งสองฝั่งได้ ⇒ เหลือ $7 = k$',
        '• ยุบผลลัพธ์ : $k = 7$ ⇒ เป็นจำนวนจริงจำนวนเดียว ไม่ติด $\\theta$ ⇒ สอดคล้องกับที่โจทย์ประกาศไว้ว่า '
        '$k$ เป็นค่าคงตัว ⇒ ตรงนี้ยังใช้เป็นการตรวจความสมเหตุสมผลของเส้นทางได้อีกชั้นหนึ่งด้วย',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่ามุมจริงสองมุมที่คำนวณง่ายแล้วเทียบตัวเลขสองฝั่งตรง ๆ '
        'โดยไม่แตะการกระจายพีชคณิตเลยแม้แต่ก้าวเดียว)</b>',
        '• มุมแรก เลือก $\\theta = \\dfrac{\\pi}{4}$ ซึ่งผ่านเงื่อนไข $\\sin\\theta\\cos\\theta \\ne 0$ '
        '⇒ ค่าที่ต้องใช้คือ $\\sin\\theta = \\cos\\theta = \\dfrac{\\sqrt{2}}{2}$ · '
        '$\\csc\\theta = \\sec\\theta = \\sqrt{2}$ · $\\tan\\theta = \\cot\\theta = 1$',
        '• คิดฝั่งซ้ายเป็นตัวเลข : สองก้อนหน้าตาเหมือนกันเป๊ะ ⇒ ฝั่งซ้าย $= 2\\left(\\dfrac{\\sqrt{2}}{2} '
        '+ \\sqrt{2}\\right)^2 = 2\\left(\\dfrac{3\\sqrt{2}}{2}\\right)^2 = 2 \\cdot \\dfrac{18}{4} = 9$',
        '• คิดฝั่งขวาเป็นตัวเลข : ฝั่งขวา $= k + 1^2 + 1^2 = k + 2$ ⇒ จับสองฝั่งเท่ากัน $k + 2 = 9$ '
        '⇒ $k = 7$ ✓ ตรงกับที่กระจายไว้',
        '• มุมที่สอง เพื่อยืนยันว่าไม่ใช่เรื่องบังเอิญของมุมสวย เลือกมุมแหลม $\\theta$ ที่ $\\tan\\theta = 2$ '
        '⇒ สามเหลี่ยมมุมฉากด้าน $1$ , $2$ และ $\\sqrt{5}$ ให้ $\\sin^2\\theta = \\dfrac{4}{5}$ · '
        '$\\cos^2\\theta = \\dfrac{1}{5}$ · $\\csc^2\\theta = \\dfrac{5}{4}$ · $\\sec^2\\theta = 5$ · '
        '$\\cot^2\\theta = \\dfrac{1}{4}$',
        '• ฝั่งซ้าย $= \\dfrac{4}{5} + 2 + \\dfrac{5}{4} + \\dfrac{1}{5} + 2 + 5 = '
        '\\left(\\dfrac{4}{5} + \\dfrac{1}{5}\\right) + 4 + \\dfrac{5}{4} + 5 = '
        '1 + 4 + \\dfrac{5}{4} + 5 = \\dfrac{45}{4}$',
        '• ฝั่งขวา $= k + 4 + \\dfrac{1}{4} = k + \\dfrac{17}{4}$ ⇒ $k = \\dfrac{45}{4} - \\dfrac{17}{4} '
        '= \\dfrac{28}{4} = 7$ ✓ ได้ค่าเดิมทั้งที่มุมคนละมุมและตัวเลขคนละชุด',
        '• 📌 ⚠️ ย้ำเตือนวิธีคิด : การแทนค่ามุมสองมุมแล้วได้ $7$ เท่ากันเป็นเพียงหลักฐานที่<b>หนักแน่นมาก</b> '
        'ว่าเดินมาถูก ⛔ แต่ยังไม่ใช่การพิสูจน์ว่าสมการเป็นเอกลักษณ์ · '
        'สิ่งที่พิสูจน์จริงคือการกระจายในขั้นที่ 1 ถึงขั้นที่ 4 ซึ่งไม่ได้อาศัยมุมใดมุมหนึ่งเลย '
        '⇒ ใช้การแทนค่าเป็นด่านตรวจเท่านั้น อย่าใช้แทนการจัดรูป',
        '',
        '✅ <b>คำตอบ</b> ค่าของ $k$ เท่ากับ $7$ → <b>ตัวเลือก 4</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอ $\\left(\\text{ฟังก์ชัน} + \\text{ส่วนกลับของฟังก์ชันนั้น}\\right)^2$ เมื่อไร '
        'ให้เขียนผลลัพธ์ทันทีว่า “ กำลังสองของตัวหน้า บวก $2$ บวก กำลังสองของตัวหลัง ” '
        'เพราะพจน์ไขว้ยุบเป็น $2$ เสมอ ⇒ ประหยัดเวลาและกันลืมพจน์ไขว้ไปพร้อมกัน · '
        'รูปแบบนี้ใช้ได้กับทุกคู่ส่วนกลับ ไม่ว่าจะเป็น $\\sin$ กับ $\\csc$ , $\\cos$ กับ $\\sec$ '
        'หรือ $\\tan$ กับ $\\cot$',
        '• เวลาต้องหาค่าคงตัวในเอกลักษณ์ ให้ดู<b>ฝั่งขวา</b>ก่อนว่าเขาพูดด้วยฟังก์ชันตัวใด แล้วค่อยจัดฝั่งซ้าย'
        'ให้พูดภาษาเดียวกัน ⇒ ข้อนี้ฝั่งขวาใช้ $\\tan$ กับ $\\cot$ จึงรู้ตั้งแต่ยังไม่ลงมือว่าปลายทางต้องแปลง '
        '$\\sec^2\\theta$ กับ $\\csc^2\\theta$ ⛔ ถ้ามุ่งหน้าแปลงทุกอย่างเป็น $\\sin$ กับ $\\cos$ '
        'จะได้เศษส่วนซ้อนที่ยาวกว่าเดิมโดยไม่จำเป็น',
        '• นับที่มาของค่าคงตัวเป็นก้อน ๆ แล้วจดไว้ข้างกระดาษ : พีทาโกรัสให้ $1$ · พจน์ไขว้ให้ $4$ · '
        'การแปลงส่วนกลับสองครั้งให้อีก $2$ ⇒ รวม $7$ · การนับแบบนี้ทำให้ตรวจย้อนได้ทันทีว่าตกก้อนไหนไป '
        'และเป็นวิธีจับผิดตัวเองที่เร็วกว่าการกระจายใหม่ทั้งหมด',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $3$ เพราะกระจายกำลังสองผิดเป็น $\\left(a+b\\right)^2 = a^2 + b^2$ '
        'คือทิ้งพจน์ไขว้ไปทั้งสองก้อน ⇒ ฝั่งซ้ายเหลือ $\\sin^2\\theta + \\csc^2\\theta + \\cos^2\\theta '
        '+ \\sec^2\\theta = 1 + \\left(1+\\cot^2\\theta\\right) + \\left(1+\\tan^2\\theta\\right) '
        '= 3 + \\tan^2\\theta + \\cot^2\\theta$ ⇒ อ่านออกมาเป็น $3$ · '
        'ค่านี้ผิดและตรวจจับได้ในบรรทัดเดียว โดยแทน $\\theta = \\dfrac{\\pi}{4}$ ลงสมการเดิม : '
        'ฝั่งซ้ายเป็น $9$ ส่วนฝั่งขวาจะเป็น $3 + 1 + 1 = 5$ ซึ่งไม่เท่ากัน ⇒ สมการไม่เป็นจริง '
        '· วิธีกันคือท่องให้ขึ้นใจว่า $\\left(a+b\\right)^2$ มี<b>สามพจน์</b>เสมอ ไม่ใช่สองพจน์',
        '• ได้ค่า $5$ เพราะกระจายก้อนโคไซน์ครบ แต่ลืมพจน์ไขว้ของก้อนไซน์ไปหนึ่งก้อน (หรือสลับกัน '
        'คือครบก้อนไซน์แต่ลืมก้อนโคไซน์ ผลลัพธ์เท่ากัน) ⇒ ค่าคงตัวจากพจน์ไขว้เหลือ $2$ แทนที่จะเป็น $4$ '
        '⇒ ขาดไป $2$ พอดี ⇒ ได้ $5 + \\tan^2\\theta + \\cot^2\\theta$ · '
        'ค่านี้ผิดเพราะเมื่อแทน $\\theta = \\dfrac{\\pi}{4}$ ฝั่งขวาจะเป็น $5 + 2 = 7$ '
        'แต่ฝั่งซ้ายเป็น $9$ ⇒ ต่างกันอยู่ $2$ ซึ่งคือพจน์ไขว้ที่ลืมไปเป๊ะ ๆ · '
        'วิธีกันคือกระจายทีละก้อนแล้ววงพจน์ไขว้ของแต่ละก้อนไว้ก่อนรวม ⛔ ห้ามรวบสองก้อนพร้อมกันในหัว',
        '• ได้ค่า $6$ เพราะนับพจน์ไขว้ครบทั้งสองก้อนแล้ว ($2+2=4$) และแปลง $\\csc^2\\theta$ กับ '
        '$\\sec^2\\theta$ ถูกต้องทั้งคู่ แต่ตอนจัดพจน์กลับเผลอตัด $\\sin^2\\theta + \\cos^2\\theta$ '
        'ทิ้งเป็น $0$ ราวกับว่ามันหักล้างกัน แทนที่จะแทนเป็น $1$ ⇒ ได้ $0 + 4 + 1 + 1 = 6$ · '
        'ค่านี้พลาดเพียงหนึ่งหน่วยจึงหลอกตาที่สุดในบรรดาค่าผิดทั้งหมด แต่ผิดแน่นอนเพราะ '
        '$\\sin^2\\theta + \\cos^2\\theta$ เป็นผล<b>บวก</b>ของกำลังสองสองจำนวน จึงเป็นบวกเสมอ '
        'และมีค่าเท่ากับ $1$ ตามเอกลักษณ์พีทาโกรัส ⛔ ไม่มีทางเป็น $0$ ได้เลย · '
        'ตรวจซ้ำด้วยการแทน $\\theta = \\dfrac{\\pi}{4}$ ก็เห็นทันทีว่าฝั่งขวาจะเป็น $6 + 2 = 8$ '
        'ขณะที่ฝั่งซ้ายเป็น $9$ ⇒ ขาดไป $1$ ตรงกับที่ตัดทิ้งไปพอดี',
        '• อีกเส้นทางที่พลาดกันบ่อยคือรีบแทนค่ามุมเดียวแล้วปิดงานทันทีโดยไม่กระจายเลย '
        'ซึ่งบังเอิญได้ $7$ ถูกในข้อนี้ แต่เป็นการเดินที่ไม่ปลอดภัย เพราะถ้าโจทย์เปลี่ยนเป็นสมการที่'
        '<b>ไม่ใช่</b>เอกลักษณ์จริง การแทนมุมเดียวจะให้ค่า $k$ ออกมาค่าหนึ่งเสมอทั้งที่ไม่มี $k$ ใดใช้ได้ทุกมุม '
        '⇒ เด็กจะตอบไปโดยไม่รู้ตัวว่าโจทย์นั้นไม่มีคำตอบ · วิธีกันคือถือหลักว่าการแทนค่าใช้ '
        '<b>ตรวจ</b> ได้อย่างเดียว ส่วนการยืนยันว่าเป็นเอกลักษณ์ต้องมาจากการจัดรูปพีชคณิตที่ไม่อ้างอิงมุมใดเลย',
    ],
    'V.mold: G = G-TRIG-IDENTITY-UNKNOWN-CONSTANT-RECIPROCAL-SQUARES, an equation declared to hold for '
    'every real theta with sin*cos nonzero whose left side is the sum of the squares of two reciprocal '
    'pairs, sine plus cosecant and cosine plus secant, and whose right side is an unknown real constant k '
    'plus the tail tan^2 + cot^2 / A = A-CONSTANT-VALUE, the single value of k / '
    'M = M-EXPAND-RECIPROCAL-SQUARE-CROSS-TERM-CONSTANT, expand both binomial squares in full so that each '
    'cross term collapses to the bare constant 2 precisely because the two summands are reciprocals of one '
    'another, gather sin^2 + cos^2 into 1, then rewrite csc^2 as 1 + cot^2 and sec^2 as 1 + tan^2 so that '
    'both sides carry the identical tail and the constants can be matched term by term. '
    'Rubric F2 C1 P2 T1 L0 = 6/15, with tot >= 3 and T <= 2 -> level: ปานกลาง. '
    'F = 2 because exactly two formula blocks carry the item, the algebraic square of a sum and the '
    'Pythagorean identity together with its two divided offspring; F was not raised to 3 because no third '
    'theorem enters anywhere, no sum or difference formula, no double angle, no equation to solve. C = 1 '
    'because the one idea imported from outside subtopic 7.4 is binomial expansion, routine algebra rather '
    'than a second mathematical key, so the chain is one identity family plus one link. P = 2 for four '
    'short stages of different kinds: expand two squares, collect and apply the Pythagorean identity, '
    'convert the two reciprocal squares, and match constants; P was not raised to 3 because every stage is '
    'two or three lines and nothing has to be carried across stages except a running constant. T = 1 for '
    'the single hidden condition, that the two cross terms do not vanish but turn into constants, which is '
    'exactly what the three wrong values on offer harvest; T was not raised to 2 because there is no root '
    'to screen, no branch to choose, no sign to decide and no domain trap beyond the one the stem already '
    'states out loud. L = 0 because the item is symbolic throughout, no figure to draw and no worded '
    'situation to model. The total of 6 sits well under the tot >= 8 gate for ยาก, and that gate also '
    'demands T >= 2 or C >= 2, both of which fail here, so ยาก is closed on both counts; the ง่าย gate '
    'needs tot <= 2 with C = 0, which the item misses, so ปานกลาง is the only band left. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): rewriting (sin+csc)^2 + (cos+sec)^2 - tan^2 - cot^2 in terms of cosine and '
    'simplifying returns the bare integer 7 with no theta left in it, which is the machine proof that the '
    'stated equation really is an identity and that k exists and is unique; a second machine pass seeded '
    'at 7 evaluates the same difference at 12 pseudo-random rational angles of the form p/211 to 30 '
    'significant digits and finds every deviation from 7 below 1e-25, so the constancy is confirmed '
    'numerically as well as symbolically. Every wrong value on offer was machine-computed from a named '
    'error path rather than invented: dropping both cross terms leaves sin^2 + csc^2 + cos^2 + sec^2, '
    'whose difference from the tail simplifies to exactly 3; keeping only one of the two cross terms '
    'simplifies to exactly 5; keeping both cross terms and both reciprocal conversions but reading '
    'sin^2 + cos^2 as 0 instead of 1 simplifies to exactly 6. The independent check was machine-verified '
    'too: at theta = pi/4 the left side evaluates to 9 while the tail evaluates to 2, and at the acute '
    'angle with tan = 2 the left side evaluates to 45/4 while the tail evaluates to 17/4, so both angles '
    'return 45/4 - 17/4 = 9 - 2 = 7. '
    'Collision sweep on 6457 items (bank 63 files + k1 out + k2 out, 6601 raw records with 144 duplicates '
    'dropped), probes run as regular expressions over the question text of the whole corpus: cosecant '
    'appears in only 16 questions in the entire bank and the pair (cosecant, secant) inside one question '
    'returns 8, none of which declares an unknown constant; the pair (tan squared, cot squared) inside a '
    'question returns exactly 1 item, chap-07-trigonometry-q181, which sets tan^2(x+y) + cot^2(x+y) equal '
    'to a quadratic in x and asks for all pairs (x, y), so it shares neither A nor M and merely reuses the '
    'same tail on the surface. The structural relative for G is gen-chap-07-trigonometry-q055, which '
    'declares sin^4 x + cos^4 x = a + b*cos 4x for all real x, but it carries two unknown constants, asks '
    'for their ratio, sits in subtopics 7.6 and 7.5, and is driven by power reduction, so it parts company '
    'at both A and M. The nearest relative by mechanism is gen-chap-07-trigonometry-q014, which supplies '
    'the product sin t * cos t = 1/4 and asks for the value of (sin t + cos t)^2: there the cross term is '
    'the given datum and the whole point of the item, whereas here the cross term is a constant that no '
    'datum can change, and that item has no unknown constant to solve for at all. A scan for a squared '
    'sum of two trigonometric terms in a question returns 3 items, the other two being chap-08-explog-q203 '
    'and pat1-2555-10-q18, both in other chapters with other unknowns. Choices are ordered ascending by '
    'numeric value (3, then 5, then 6, then 7), so the answer slot is forced by that rule and was not '
    'chosen.',
)

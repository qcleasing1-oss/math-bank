# -*- coding: utf-8 -*-
add_fill(
    141,
    ['7.3'],
    'ยาก',
    'ให้ $k$ เป็นจำนวนจริง ถ้าสมการ $\\left|3\\sin x - 1\\right| = k$ มีคำตอบทั้งหมด $3$ คำตอบ '
    'ในช่วง $0 \\le x < 2\\pi$ แล้วค่าของ $k$ เท่ากับเท่าใด',
    '2',
    ['2', '2.0'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ค่าสัมบูรณ์ $\\left|A\\right|$ คือระยะจากจำนวน $A$ ไปถึง $0$ บนเส้นจำนวน ⇒ เป็นระยะทางจึงไม่มีวันติดลบ '
        '· ผลที่ตามมาสองข้อซึ่งต้องใช้ทั้งคู่ในข้อนี้ : ข้อแรก สมการ $\\left|A\\right| = k$ '
        'จะเป็นจริงได้ก็ต่อเมื่อ $k \\ge 0$ เท่านั้น ถ้า $k < 0$ คือไม่มีคำตอบเลยโดยไม่ต้องคำนวณอะไรต่อ '
        '· ข้อที่สอง เมื่อ $k \\ge 0$ ประโยค $\\left|A\\right| = k$ แปลว่า $A$ อยู่ห่างจาก $0$ เป็นระยะ $k$ พอดี '
        'ซึ่งบนเส้นจำนวนมีที่แบบนั้นได้สองที่ คือทางขวา $A = k$ และทางซ้าย $A = -k$ '
        '⇒ ⛔ ต้องแตกเป็น<b>สองกิ่ง</b>เสมอ ห้ามทิ้งกิ่งใดกิ่งหนึ่ง',
        '• เรนจ์ของฟังก์ชันไซน์ : $-1 \\le \\sin x \\le 1$ สำหรับทุกจำนวนจริง $x$ '
        '⇒ สมการ $\\sin x = u$ จะมีคำตอบก็ต่อเมื่อ $\\left|u\\right| \\le 1$ '
        '· ถ้า $\\left|u\\right| > 1$ แปลว่าเส้นแนวนอน $y = u$ ลอยอยู่เหนือยอดคลื่นหรือจมอยู่ใต้ท้องคลื่น '
        'จึงไม่ตัดกราฟเลยสักจุด ⇒ ได้ $0$ คำตอบทันที',
        '• จำนวนคำตอบของ $\\sin x = u$ ในช่วง $0 \\le x < 2\\pi$ ขึ้นกับว่า $\\left|u\\right|$ '
        'อยู่ตรงไหนเทียบกับ $1$ · เหตุผลอ่านจากกราฟไซน์หนึ่งคาบได้ตรง ๆ คือ ในหนึ่งคาบกราฟไต่ขึ้นถึงยอดสูงสุด '
        '$1$ ที่ $x = \\dfrac{\\pi}{2}$ เพียงยอดเดียว แล้วไหลลงถึงท้องต่ำสุด $-1$ ที่ $x = \\dfrac{3\\pi}{2}$ '
        'เพียงท้องเดียว ⇒ เส้นแนวนอนที่พาดอยู่ระหว่างยอดกับท้องจะตัดกราฟสองครั้ง ครั้งหนึ่งตอนขาขึ้น '
        'อีกครั้งตอนขาลง แต่พอเส้นเลื่อนขึ้นไปแตะยอดพอดี จุดตัดสองจุดจะวิ่งเข้าหากันจนรวมเป็นจุดเดียว',
        '• ช่วง $0 \\le x < 2\\pi$ เป็นช่วง<b>ครึ่งเปิด</b> ⇒ นับ $x = 0$ แต่ ⛔ ไม่นับ $x = 2\\pi$ '
        '· เหตุผลคือไซน์มีคาบเท่ากับ $2\\pi$ ⇒ $\\sin 2\\pi = \\sin 0$ ถ้านับปลายทั้งสองข้างจะได้ค่าซ้ำหน้าเดิม '
        'กลายเป็นนับเกิน ⇒ ช่วงครึ่งเปิดนี้จึงเก็บ “หนึ่งคาบพอดีโดยไม่ซ้ำ” '
        'เวลานับจำนวนคำตอบต้องอ่านเครื่องหมายให้ขาดว่าเป็น $<$ หรือ $\\le$',
        '• เลข $3$ เป็นจำนวน<b>คี่</b> และนี่คือแก่นของข้อนี้ : แต่ละกิ่งให้จำนวนคำตอบได้เพียง $0$ · $1$ '
        'หรือ $2$ เท่านั้น ⇒ คู่ของจำนวนที่บวกกันได้ $3$ จึงเหลือแค่ $1 + 2$ กับ $2 + 1$ '
        '⇒ ต้องมีกิ่งหนึ่งให้ $1$ คำตอบพอดีเสมอ · ส่วน $0 + 3$ และ $3 + 0$ เป็นไปไม่ได้ '
        'เพราะไม่มีค่า $u$ ใดเลยที่ทำให้ $\\sin x = u$ มีถึง $3$ คำตอบภายในหนึ่งคาบ',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $k$ เป็นจำนวนจริง และสมการที่พิจารณาคือ $\\left|3\\sin x - 1\\right| = k$',
        '• เงื่อนไขที่โจทย์บังคับคือ สมการนี้ต้องมีคำตอบทั้งหมด $3$ คำตอบ ในช่วง $0 \\le x < 2\\pi$',
        '• สังเกตหน้าตาก่อนลงมือ : ฝั่งขวาของเครื่องหมายเท่ากับเป็น $k$ เปล่า ๆ อยู่ตรงข้ามกับค่าสัมบูรณ์ '
        '⇒ เงื่อนไข $k \\ge 0$ ติดมากับโจทย์เองโดยไม่ต้องมีใครเขียนบอก '
        '⇒ เวลาแก้สมการหาผู้ท้าชิงได้หลายค่า ต้องคัดค่าที่ติดลบทิ้งทุกครั้ง',
        '• สังเกตอย่างที่สอง ซึ่งเป็นสัญญาณบอกทางของข้อนี้ : เส้นแนวนอนตัดกราฟคลื่นเป็นจำนวน<b>คู่</b>ตามปกติ '
        '(ขาขึ้นหนึ่งจุด ขาลงหนึ่งจุด) แต่โจทย์กลับสั่งให้ได้ $3$ ซึ่งเป็นจำนวนคี่ '
        '⇒ แปลว่าต้องมีจุดใดจุดหนึ่งที่ผิดปกติ คือจุดที่จุดตัดสองจุดยุบรวมเป็นจุดเดียว '
        '⇒ ตั้งแต่อ่านโจทย์จบก็เดาทางได้แล้วว่าคำตอบต้องเป็นค่า $k$ ที่ทำให้เกิดการยุบรวมนั้นพอดี',
        '• สังเกตอย่างที่สาม : สองกิ่งที่จะแตกออกมาไม่สมมาตรกัน เพราะมี $-1$ เกาะอยู่ในค่าสัมบูรณ์ '
        '⇒ กิ่งหนึ่งจะให้ $\\sin x = \\dfrac{1 + k}{3}$ ส่วนอีกกิ่งให้ $\\sin x = \\dfrac{1 - k}{3}$ '
        'ซึ่งเป็นคนละค่ากัน ⇒ ⛔ ห้ามเหมารวมว่าสองกิ่งให้ผลเหมือนกัน ต้องนับแยกทีละกิ่ง',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $k$ ที่ทำให้สมการมีคำตอบครบ $3$ คำตอบพอดีในช่วงที่โจทย์กำหนด',
        '',
        '<b>【 แตกค่าสัมบูรณ์เป็นสองกิ่งแล้วจัดให้เหลือ $\\sin x$ เดี่ยว ๆ ทั้งสองกิ่ง '
        'ต่อด้วยการวางตารางจำนวนคำตอบของ $\\sin x = u$ บนช่วง $0 \\le x < 2\\pi$ '
        'แล้วใช้ข้อเท็จจริงว่า $3$ แยกเป็นผลบวกของจำนวนคำตอบสองกิ่งได้ทางเดียวคือ $1 + 2$ '
        'จึงบังคับให้กิ่งหนึ่งต้องมีค่า $\\left|u\\right| = 1$ พอดี ⇒ ได้ผู้ท้าชิงสองค่า '
        'สุดท้ายแทนผู้ท้าชิงกลับไปนับจำนวนคำตอบจริงทีละค่าเพื่อคัดให้เหลือค่าเดียว 】</b>',
        '',
        '<b>ขั้นที่ 1 · แตกค่าสัมบูรณ์เป็นสองกิ่ง แล้วจัดให้เหลือ $\\sin x$ เดี่ยว ๆ</b>',
        '• เงื่อนไขแรกสุดก่อนแตะอะไร : ฝั่งซ้ายเป็นค่าสัมบูรณ์ซึ่งไม่ติดลบ ⇒ ต้องมี $k \\ge 0$ '
        'ไม่เช่นนั้นสมการไม่มีคำตอบเลย ⇒ จำเงื่อนไขนี้ไว้ใช้คัดค่าที่ขั้นที่ 3',
        '• สูตรที่ใช้ : $\\left|A\\right| = k$ เมื่อ $k \\ge 0$ ⇒ $A = k$ หรือ $A = -k$ '
        '· ระบุตัวแปรก่อนแทนค่า : ในข้อนี้ $A = 3\\sin x - 1$',
        '• กิ่งที่หนึ่ง : $3\\sin x - 1 = k$ ⇒ ย้าย $-1$ ไปบวกอีกข้างได้ $3\\sin x = 1 + k$ '
        '⇒ หารด้วย $3$ ทั้งสองข้าง ได้ $\\sin x = \\dfrac{1 + k}{3}$',
        '• กิ่งที่สอง : $3\\sin x - 1 = -k$ ⇒ ย้าย $-1$ ไปบวกอีกข้างได้ $3\\sin x = 1 - k$ '
        '⇒ หารด้วย $3$ ทั้งสองข้าง ได้ $\\sin x = \\dfrac{1 - k}{3}$',
        '• เขียนชื่อย่อไว้ใช้ต่อ : ให้ $u_{1} = \\dfrac{1 + k}{3}$ และ $u_{2} = \\dfrac{1 - k}{3}$ '
        '⇒ โจทย์เดิมกลายเป็น “$\\sin x = u_{1}$ หรือ $\\sin x = u_{2}$” ซึ่งเป็นสมการไซน์ธรรมดาสองอันวางคู่กัน',
        '• ⭐ ตรวจเรื่องการนับซ้ำให้จบก่อนเดินต่อ เพราะถ้าสองกิ่งมีคำตอบร่วมกัน การบวกจำนวนคำตอบจะเกินจริง '
        '· เทียบสองค่านี้ : $u_{1} = u_{2}$ ก็ต่อเมื่อ $\\dfrac{1 + k}{3} = \\dfrac{1 - k}{3}$ '
        '⇒ $1 + k = 1 - k$ ⇒ $2k = 0$ ⇒ $k = 0$ '
        '· แต่ที่ $k = 0$ สมการเหลือ $\\sin x = \\dfrac{1}{3}$ อันเดียวซึ่งให้ $2$ คำตอบ ไม่ใช่ $3$ '
        '⇒ ทุกค่า $k$ ที่ยังมีสิทธิ์เป็นคำตอบล้วนมี $k > 0$ ⇒ $u_{1} \\ne u_{2}$ '
        '⇒ เซตคำตอบของสองกิ่งไม่ทับกันเลย ⇒ <b>บวกจำนวนคำตอบของสองกิ่งได้ตรง ๆ</b>',
        '',
        '<b>ขั้นที่ 2 · วางตารางจำนวนคำตอบของ $\\sin x = u$ ในช่วง $0 \\le x < 2\\pi$</b>',
        '• ตารางนี้คือเครื่องมือหลักของข้อนี้ มีสามแถวเท่านั้น อ่านจากกราฟไซน์หนึ่งคาบทั้งหมด '
        '⇒ เขียนไว้ข้างกระดาษก่อนแทนค่าใด ๆ',
        '• แถวที่ 1 · $\\left|u\\right| < 1$ ⇒ ได้ <b>$2$ คำตอบ</b> '
        '· เพราะเส้นแนวนอน $y = u$ พาดอยู่ระหว่างท้องคลื่นกับยอดคลื่นแบบไม่แตะทั้งสองอย่าง '
        '⇒ ตัดกราฟหนึ่งครั้งตอนกราฟกำลังไต่ขึ้น และอีกหนึ่งครั้งตอนกราฟกำลังไหลลง',
        '• แถวที่ 2 · $\\left|u\\right| = 1$ ⇒ ได้ <b>$1$ คำตอบ</b> '
        '· กรณี $u = 1$ เส้นแตะยอดคลื่นพอดี ซึ่งในหนึ่งคาบมียอดเดียวที่ $x = \\dfrac{\\pi}{2}$ '
        '· กรณี $u = -1$ เส้นแตะท้องคลื่นพอดี ซึ่งในหนึ่งคาบมีท้องเดียวที่ $x = \\dfrac{3\\pi}{2}$ '
        '⇒ ⛔ แถวนี้คือแถวที่คนพลาดกันมากที่สุด เพราะเผลอนับเป็น $2$ ตามความเคยชินจากแถวที่ 1 '
        'ทั้งที่จุดตัดสองจุดยุบรวมกันเหลือจุดเดียวไปแล้ว',
        '• แถวที่ 3 · $\\left|u\\right| > 1$ ⇒ ได้ <b>$0$ คำตอบ</b> '
        '· เพราะค่า $u$ หลุดออกนอกเรนจ์ของไซน์ เส้นแนวนอนจึงลอยพ้นกราฟไปเลย ไม่มีจุดตัด',
        '• อ่านตารางนี้เป็นภาษาคนได้ว่า จำนวนคำตอบเป็น<b>เลขคู่</b>ทุกกรณี ยกเว้นกรณีเดียวคือตอนที่ '
        '$\\left|u\\right| = 1$ พอดี ซึ่งให้เลขคี่คือ $1$ ⇒ นี่คือประตูเดียวที่จะพาไปสู่ผลรวมคี่',
        '',
        '<b>ขั้นที่ 3 · แปลงเงื่อนไข “$3$ คำตอบ” ให้เป็นเงื่อนไขบนกิ่ง ⇒ ได้ผู้ท้าชิงสองค่า</b>',
        '• จำนวนคำตอบทั้งหมด $=$ จำนวนคำตอบของกิ่งที่หนึ่ง $+$ จำนวนคำตอบของกิ่งที่สอง '
        '(บวกได้ตรง ๆ ตามที่พิสูจน์ไว้ท้ายขั้นที่ 1 ว่าไม่มีคำตอบร่วม)',
        '• แต่ละกิ่งหยิบค่าได้จากตารางเพียง $0$ · $1$ หรือ $2$ ⇒ จับคู่ที่บวกกันได้ $3$ ให้ครบทุกแบบ : '
        '$0 + 3$ ⛔ ใช้ไม่ได้เพราะไม่มีแถวไหนให้ $3$ · $1 + 2$ ✓ ใช้ได้ · $2 + 1$ ✓ ใช้ได้ '
        '· $3 + 0$ ⛔ ใช้ไม่ได้ด้วยเหตุผลเดียวกับแบบแรก ⇒ เหลือทางเดียวจริง ๆ คือ '
        '<b>กิ่งหนึ่งให้ $1$ คำตอบ และอีกกิ่งให้ $2$ คำตอบ</b>',
        '• อีกมุมหนึ่งของข้อสรุปเดียวกัน ซึ่งช่วยยืนยันว่าไม่มีค่าอื่นหลุดรอด : ถ้าไม่มีกิ่งไหนแตะ '
        '$\\left|u\\right| = 1$ เลย จำนวนคำตอบของทั้งสองกิ่งจะเป็นเลขคู่ทั้งคู่ ($0$ หรือ $2$) '
        '⇒ ผลรวมเป็นเลขคู่เสมอ ⇒ เป็น $3$ ไม่ได้เด็ดขาด '
        '⇒ ⭐ ค่า $k$ ที่ใช้ได้ต้องมาจากเงื่อนไข $\\left|u\\right| = 1$ เท่านั้น ไม่มีทางอื่น',
        '• กรณี A · ให้กิ่งที่หนึ่งเป็นกิ่งที่ให้ $1$ คำตอบ ⇒ แก้ '
        '$\\left|\\dfrac{1 + k}{3}\\right| = 1$ ⇒ คูณสองข้างด้วย $3$ ได้ $\\left|1 + k\\right| = 3$ '
        '⇒ แตกค่าสัมบูรณ์อีกครั้ง $1 + k = 3$ ⇒ $k = 2$ หรือ $1 + k = -3$ ⇒ $k = -4$ '
        '· คัดด้วยเงื่อนไข $k \\ge 0$ จากขั้นที่ 1 ⇒ ทิ้ง $k = -4$ ⇒ เหลือ $k = 2$',
        '• กรณี B · ให้กิ่งที่สองเป็นกิ่งที่ให้ $1$ คำตอบ ⇒ แก้ '
        '$\\left|\\dfrac{1 - k}{3}\\right| = 1$ ⇒ คูณสองข้างด้วย $3$ ได้ $\\left|1 - k\\right| = 3$ '
        '⇒ แตกค่าสัมบูรณ์ $1 - k = 3$ ⇒ $k = -2$ หรือ $1 - k = -3$ ⇒ $k = 4$ '
        '· คัดด้วยเงื่อนไข $k \\ge 0$ ⇒ ทิ้ง $k = -2$ ⇒ เหลือ $k = 4$',
        '• สรุปผู้ท้าชิงที่รอดมาถึงตรงนี้มีสองค่า คือ $k = 2$ และ $k = 4$ '
        '⛔ หยุดตอบตรงนี้ยังไม่ได้ เพราะเงื่อนไข $\\left|u\\right| = 1$ รับประกันแค่ว่ากิ่งนั้นให้ $1$ คำตอบ '
        'แต่ยัง<b>ไม่ได้ตรวจเลย</b>ว่าอีกกิ่งให้ $2$ คำตอบตามที่ต้องการหรือไม่ ⇒ ต้องเดินต่อขั้นที่ 4',
        '',
        '<b>ขั้นที่ 4 · ตรวจผู้ท้าชิงทีละค่าด้วยตารางของขั้นที่ 2 ⛔ จุดหักของข้อนี้</b>',
        '• ทดสอบ $k = 2$ · กิ่งที่หนึ่ง : $u_{1} = \\dfrac{1 + 2}{3} = \\dfrac{3}{3} = 1$ '
        '⇒ $\\left|u_{1}\\right| = 1$ ⇒ ตรงกับแถวที่ 2 ของตาราง ⇒ ได้ $1$ คำตอบ',
        '• ทดสอบ $k = 2$ · กิ่งที่สอง : $u_{2} = \\dfrac{1 - 2}{3} = -\\dfrac{1}{3}$ '
        '⇒ $\\left|u_{2}\\right| = \\dfrac{1}{3} < 1$ ⇒ ตรงกับแถวที่ 1 ของตาราง ⇒ ได้ $2$ คำตอบ',
        '• รวมของ $k = 2$ : $1 + 2 = 3$ คำตอบ ✓ <b>ตรงกับที่โจทย์สั่งพอดี</b>',
        '• ทดสอบ $k = 4$ · กิ่งที่หนึ่ง : $u_{1} = \\dfrac{1 + 4}{3} = \\dfrac{5}{3}$ '
        '⇒ $\\left|u_{1}\\right| = \\dfrac{5}{3} > 1$ ⇒ ตรงกับแถวที่ 3 ⇒ ได้ $0$ คำตอบ '
        '(อธิบายเป็นภาษาคนได้ว่า ไซน์ขึ้นไม่ถึง $\\dfrac{5}{3}$ เพราะเพดานของมันคือ $1$)',
        '• ทดสอบ $k = 4$ · กิ่งที่สอง : $u_{2} = \\dfrac{1 - 4}{3} = \\dfrac{-3}{3} = -1$ '
        '⇒ $\\left|u_{2}\\right| = 1$ ⇒ แถวที่ 2 ⇒ ได้ $1$ คำตอบ',
        '• รวมของ $k = 4$ : $0 + 1 = 1$ คำตอบ ✗ ⇒ ขาดไป $2$ คำตอบ ⇒ ทิ้งค่านี้ '
        '· เหตุผลลึก ๆ ที่ $k = 4$ ตกคือ พอ $k$ โตขึ้น กิ่งที่หนึ่งจะดันตัวเองหลุดเพดาน $1$ ไปก่อน '
        '⇒ กิ่งที่ควรจะเป็นผู้ให้ $2$ คำตอบกลับกลายเป็นผู้ให้ $0$ คำตอบเสียเอง',
        '• สรุปจากขั้นนี้ : เหลือผู้ท้าชิงเพียงค่าเดียวที่ผ่านทุกเงื่อนไข คือ $k = 2$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทน $k = 2$ กลับเข้าสมการเดิมแล้วแจงรากออกมาทีละรากจนครบ '
        '⛔ ไม่แตะตารางนับจำนวนคำตอบของขั้นที่ 2 อีกเลย)</b>',
        '• แทน $k = 2$ ลงในโจทย์เดิมได้ $\\left|3\\sin x - 1\\right| = 2$ '
        '⇒ แตกค่าสัมบูรณ์ตรง ๆ ได้ $3\\sin x - 1 = 2$ หรือ $3\\sin x - 1 = -2$',
        '• กรณี $3\\sin x - 1 = 2$ ⇒ $3\\sin x = 3$ ⇒ $\\sin x = 1$ '
        '⇒ ในช่วง $0 \\le x < 2\\pi$ ค่า $x$ ที่ทำให้ไซน์เท่ากับ $1$ มีเพียง $x = \\dfrac{\\pi}{2}$ '
        '⇒ <b>ราก 1 ค่า</b> ที่ประมาณ $1.5708$ เรเดียน',
        '• กรณี $3\\sin x - 1 = -2$ ⇒ $3\\sin x = -1$ ⇒ $\\sin x = -\\dfrac{1}{3}$ '
        '⇒ ไซน์ติดลบในควอดรันต์ที่สามและที่สี่ ⇒ ได้ $x = \\pi + \\arcsin\\dfrac{1}{3}$ '
        'และ $x = 2\\pi - \\arcsin\\dfrac{1}{3}$ ⇒ <b>ราก 2 ค่า</b>',
        '• ใส่ตัวเลขกำกับให้เห็นภาพ : $\\arcsin\\dfrac{1}{3} \\approx 0.3398$ เรเดียน '
        '⇒ รากสองค่านี้อยู่ที่ประมาณ $3.4814$ และ $5.9433$ เรเดียน '
        '⇒ ทั้งสองค่าอยู่ในช่วง $0 \\le x < 2\\pi \\approx 6.2832$ จริง ✓ และไม่ซ้ำกับ $1.5708$',
        '• แจงรายชื่อรากทั้งหมด : $\\dfrac{\\pi}{2}$ · $\\pi + \\arcsin\\dfrac{1}{3}$ '
        '· $2\\pi - \\arcsin\\dfrac{1}{3}$ ⇒ <b>นับได้ $3$ ค่าพอดี</b> ✓ ตรงกับที่โจทย์สั่ง '
        '⇒ ยืนยันว่า $k = 2$ ใช้ได้จริง',
        '• 📌 เสริมด้วยมุมมองกราฟ ซึ่งยืนยันอีกชั้นว่าไม่มีค่า $k$ อื่นอีกแล้ว : '
        'มองสมการเป็นการหาจุดตัดของกราฟ $y = \\left|3\\sin x - 1\\right|$ กับเส้นแนวนอน $y = k$ '
        '· ภายในหนึ่งคาบ $3\\sin x - 1$ วิ่งจาก $-4$ ถึง $2$ ⇒ หลังใส่ค่าสัมบูรณ์แล้ว '
        'กราฟจึงมีค่าอยู่ในช่วง $\\left[0,\\ 4\\right]$',
        '• จุดสุดขั้วของกราฟนี้มีอยู่สี่จุดเท่านั้น คือ ยอดสูง $4$ ที่ $x = \\dfrac{3\\pi}{2}$ '
        '(มาจากท้องคลื่นที่ถูกพับขึ้น) · ยอดเตี้ย $2$ ที่ $x = \\dfrac{\\pi}{2}$ '
        '· และจุดที่กราฟแตะพื้น $0$ อีกสองจุดซึ่งเกิดตรงที่ $\\sin x = \\dfrac{1}{3}$',
        '• เส้นแนวนอนจะให้จำนวนจุดตัดเป็นเลข<b>คี่</b>ก็ต่อเมื่อเส้นนั้นพาดผ่านจุดสุดขั้ว '
        'เป็นจำนวน<b>คี่จุด</b>พร้อมกัน ⇒ ที่ $k = 2$ เส้นแตะยอดเตี้ยจุดเดียว ⇒ ได้ $3$ จุดตัด ✓ '
        '· ที่ $k = 4$ เส้นแตะยอดสูงจุดเดียว ⇒ ได้ $1$ จุดตัด '
        '· ที่ $k = 0$ เส้นแตะพื้นพร้อมกัน $2$ จุด ซึ่งเป็นจำนวนคู่ ⇒ ได้ $2$ จุดตัด '
        '⇒ ไล่ครบทุกจุดสุดขั้วแล้วมีเพียง $k = 2$ ที่ให้ $3$ ✓',
        '',
        '✅ <b>คำตอบ</b> ค่าของ $k$ เท่ากับ $2$',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอโจทย์ที่สั่ง “จำนวนคำตอบเป็นเลขคี่” ของสมการตรีโกณเมื่อไร ให้คิดถึงคำว่า<b>ยอดหรือท้องคลื่น</b>ทันที '
        'เพราะเส้นแนวนอนตัดคลื่นเป็นคู่เสมอ ความคี่จึงเกิดได้เฉพาะตอนที่จุดตัดสองจุดยุบรวมเป็นจุดเดียวที่จุดสุดขั้ว '
        '⇒ เปลี่ยนโจทย์ที่ดูยากให้เหลือแค่ “หาค่าที่ทำให้ $\\left|u\\right| = 1$ พอดี” ซึ่งแก้ได้ในบรรทัดเดียว',
        '• เขียนตารางสามแถวของ $\\sin x = u$ ($\\left|u\\right| < 1$ ให้ $2$ · $\\left|u\\right| = 1$ ให้ $1$ '
        '· $\\left|u\\right| > 1$ ให้ $0$) ไว้ข้างกระดาษ<b>ก่อน</b>เริ่มคิด แล้วบังคับตัวเองให้ชี้ลงตารางทุกครั้งที่นับ '
        '⇒ กันการนับด้วยความเคยชินว่า “สมการไซน์ให้สองคำตอบ” ซึ่งจริงเฉพาะแถวแรกเท่านั้น',
        '• การหาผู้ท้าชิงกับการตรวจผู้ท้าชิงเป็นคนละงานกัน ⇒ เงื่อนไขที่ใช้ล่าค่ามักเป็นเพียงเงื่อนไข<b>จำเป็น</b> '
        'ไม่ใช่เงื่อนไขที่เพียงพอ ⇒ ได้ค่ามากี่ค่าก็ต้องแทนกลับไปนับใหม่ทุกค่า '
        'ข้อนี้เป็นตัวอย่างชัดเจนเพราะผู้ท้าชิงสองค่าผ่านเงื่อนไขเดียวกันเป๊ะ แต่รอดจริงค่าเดียว',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $4$ เพราะนับว่า $\\sin x = 1$ ให้ $2$ คำตอบเหมือนค่าอื่น ๆ '
        'โดยลืมว่าที่ยอดคลื่นพอดีจุดตัดสองจุดยุบรวมเหลือจุดเดียว — นี่คือเส้นทางพลาดหลักของข้อนี้ '
        '· เดินตามความคิดนั้นจะได้ว่า $k = 2$ ให้ $2 + 2 = 4$ คำตอบ ⇒ ตัดทิ้ง แล้วเหลือผู้ท้าชิงอีกค่าเดียว '
        'จึงตอบ $4$ ไปตามการกำจัด · ค่านี้ผิดแน่นอน ตรวจได้โดยแทน $k = 4$ กลับเข้าสมการเดิม '
        '$\\left|3\\sin x - 1\\right| = 4$ ⇒ กิ่งบวกให้ $\\sin x = \\dfrac{5}{3}$ ซึ่งเกินเพดาน $1$ ของไซน์ '
        '⇒ ไม่มีคำตอบเลย · กิ่งลบให้ $\\sin x = -1$ ⇒ มีคำตอบเดียวคือ $x = \\dfrac{3\\pi}{2}$ '
        '⇒ รวมได้ $1$ คำตอบ ไม่ใช่ $3$ · สังเกตด้วยว่าถ้านับแบบผิดนี้จริง ทุกค่า $k$ จะให้จำนวนคำตอบเป็นเลขคู่หมด '
        '⇒ จะไม่มีค่าใดให้ $3$ ได้เลย ซึ่งขัดกับโจทย์ที่ยืนยันว่ามีอยู่จริง ⇒ เป็นสัญญาณว่าวิธีนับนั้นเสียเอง',
        '• ได้ข้อสรุปว่า “ไม่มีค่า $k$ ที่ใช้ได้” เพราะตัดกิ่ง $3\\sin x - 1 = -k$ ทิ้ง '
        'แล้วเหลือพิจารณาแค่ $\\sin x = \\dfrac{1 + k}{3}$ กิ่งเดียว มักเกิดจากการนึกว่าค่าสัมบูรณ์ '
        '“แค่ทำให้เป็นบวก” จึงถอดเครื่องหมายทิ้งไปเฉย ๆ · เดินตามเส้นทางนี้จะได้จำนวนคำตอบเพียง $2$ '
        '(เมื่อ $0 \\le k < 2$) หรือ $1$ (เมื่อ $k = 2$) หรือ $0$ (เมื่อ $k > 2$) '
        '⇒ ไม่มีทางได้ $3$ ⇒ สรุปผิดว่าโจทย์ไม่มีคำตอบ · ที่ผิดคือลืมว่านิพจน์ $3\\sin x - 1$ ติดลบได้จริง '
        'เช่นที่ $x = \\dfrac{3\\pi}{2}$ ได้ $3(-1) - 1 = -4$ ⇒ กิ่งลบมีของอยู่จริงและเป็นกิ่งที่ให้ $2$ คำตอบ '
        'ตอนที่ $k = 2$ ⇒ ทิ้งกิ่งนั้นเท่ากับทิ้งคำตอบไปสองในสามของทั้งหมด',
        '• ได้ค่า $1$ เพราะใช้ช่วง<b>ปิด</b> $\\left[0,\\ 2\\pi\\right]$ แทนช่วงครึ่งเปิดที่โจทย์เขียนไว้ '
        '· เส้นทางนี้เกิดตอนไปสนใจกิ่ง $\\sin x = \\dfrac{1 - k}{3}$ แล้วให้มันเป็นศูนย์ ซึ่งได้ที่ $k = 1$ '
        '⇒ $\\sin x = 0$ ⇒ นับ $x = 0$ · $x = \\pi$ · $x = 2\\pi$ เป็น $3$ ค่า แล้วเผลอตอบ $1$ '
        '· ค่านี้ผิดแน่นอน พิสูจน์ได้สองทาง : ทางแรก โจทย์เขียน $0 \\le x < 2\\pi$ ⇒ $x = 2\\pi$ อยู่นอกช่วง '
        'จึง ⛔ ไม่นับ เหลือกิ่งนี้เพียง $2$ คำตอบ · ทางที่สอง ต่อให้ยอมนับ $x = 2\\pi$ ก็ยังตอบไม่ได้อยู่ดี '
        'เพราะยังมีอีกกิ่งที่ถูกลืมคือ $\\sin x = \\dfrac{1 + 1}{3} = \\dfrac{2}{3}$ ซึ่งให้อีก $2$ คำตอบ '
        '⇒ ยอดรวมกลายเป็น $5$ ในช่วงปิด · เมื่อนับตามช่วงที่โจทย์กำหนดจริง $k = 1$ ให้ $2 + 2 = 4$ คำตอบ '
        'ไม่ใช่ $3$ ⇒ วิธีกันคือวงกลมเครื่องหมาย $<$ กับ $\\le$ ที่ปลายช่วงตั้งแต่อ่านโจทย์รอบแรก',
        '• ได้ค่า $-2$ (หรือ $-4$) เพราะแก้ $\\left|1 - k\\right| = 3$ กับ $\\left|1 + k\\right| = 3$ '
        'ได้ครบทั้งสี่ราก คือ $-4$ · $-2$ · $2$ · $4$ แล้วหยิบรากใดรากหนึ่งมาตอบโดยไม่คัดด้วยเงื่อนไข $k \\ge 0$ '
        '· ค่าติดลบผิดแน่นอน เพราะฝั่งซ้ายของโจทย์เป็นค่าสัมบูรณ์ซึ่งไม่ติดลบ '
        '⇒ ที่ $k = -2$ สมการ $\\left|3\\sin x - 1\\right| = -2$ ไม่มีคำตอบเลยสักค่า ได้ $0$ คำตอบ ไม่ใช่ $3$ '
        '· จุดกันพลาดคือเขียนเงื่อนไข $k \\ge 0$ ลงกระดาษตั้งแต่บรรทัดแรกที่แตะค่าสัมบูรณ์ '
        'ไม่ใช่รอไปนึกได้ตอนท้าย',
    ],
    'V.mold: G = a real parameter k standing alone on the right of an absolute value, in the equation '
    'abs(3*sin x - 1) = k, together with the demand that the equation carry exactly 3 solutions on the '
    'half-open interval 0 <= x < 2*pi / A = the single admissible value of k, asked as a free numeric '
    'response with no candidate values on the page / M = M-ABS-TWO-BRANCH-ROOT-COUNT, that is: split the '
    'absolute value into the two branches 3*sin x - 1 = k and 3*sin x - 1 = -k, isolate sine in each to '
    'reach sin x = (1 + k)/3 and sin x = (1 - k)/3, check that the two branch values differ whenever k is '
    'not 0 so the two solution sets are disjoint and the counts may simply be added, apply the three-row '
    'count table for sin x = u on one period (two solutions when the absolute value of u is below 1, one '
    'solution when it equals 1, none when it exceeds 1), observe that 3 splits as a sum of two entries of '
    'that table only as 1 + 2, conclude that one branch must land exactly on the value 1 in absolute value, '
    'solve that condition to obtain the two candidates k = 2 and k = 4 after discarding the negative roots '
    'forced out by k >= 0, and finally recount each candidate to keep only the one that really delivers 3. '
    'Rubric F2 C2 P3 T2 L0 = 9/15, a total inside the 8 to 11 band with C at least 2 and T at least 2, and '
    'below 12 so the very-hard band is out of reach -> level: ยาก. '
    'F = 2 because exactly two pieces of knowledge must be held at once: the branching rule for an '
    'absolute-value equation together with its sign precondition, and the count of preimages of a value '
    'under sine on one period including the degenerate case at the crest and the trough; F is not 3 '
    'because no identity, no addition formula and no substitution is needed anywhere, the sine is never '
    'transformed, only read. C = 2 because the item genuinely welds an algebraic object onto a graphical '
    'one: the absolute value contributes a case split that belongs to the algebra of real numbers, while '
    'the counting of preimages belongs to subtopic 7.3 and to the shape of the sine graph, and removing '
    'either half leaves the item either trivial or unanswerable. P = 3 because the work runs in three '
    'stages of different kinds where a later stage consumes an object built by an earlier one: the '
    'branching produces the two expressions in k, the count table turns each expression into a number, and '
    'the parity argument then runs the count table backwards to generate candidates before running it '
    'forwards again on each candidate. T = 2 because there is exactly one hidden turning point, namely '
    'that an odd total is impossible unless one branch sits exactly at the crest or the trough, which is '
    'what converts a vague demand about a count into a solvable equation; T is not 3 because that single '
    'insight opens the whole item, whereas a T = 3 item needs two independent discoveries before any '
    'computation may start. L = 0 because the statement carries no real-world scene, no figure and no '
    'named objects, it is a bare symbolic equation with an interval, and the only reading care demanded is '
    'the strict inequality at the right end of the interval, which is a notation matter rather than a '
    'modelling one. Scoring was written before the level was read off. '
    'sympy (verify_b20.py): in the q141 block the counting function is built from the branch set '
    '{(1 + k)/3, (1 - k)/3}, awarding 0 when the absolute value of the entry exceeds 1, 1 when it equals 1 '
    'and 2 otherwise, and the sweep over every k of the form i/20 for i from 0 to 120 returns a list of '
    'length 1 whose single element is 2, so the answer is provably unique on that grid; the same block '
    'records that k = 1 yields 4 solutions and k = 4 yields 1. This authoring session re-derived all of it '
    'independently of that hand-written counter, by calling solveset on Eq(Abs(3*sin(x) - 1), k) over '
    'Interval.Ropen(0, 2*pi) for each k, which returns 2 solutions at k = 0, 4 solutions at k = 1/2, 1 and '
    '3/2, exactly 3 at k = 2, 2 solutions at k = 5/2, 3 and 7/2, exactly 1 at k = 4 and the empty set at '
    'k = 9/2, and a finer sweep over every k of the form i/40 for i from 0 to 200 again returns the single '
    'hit k = 2. The three roots at k = 2 were printed explicitly as pi/2, pi + asin(1/3) and '
    '2*pi - asin(1/3), that is about 1.5708, 3.4814 and 5.9433, all inside the stated interval and '
    'pairwise distinct, which is the machine version of the independent check block. Every error path in '
    'the pitfalls block was computed rather than invented: counting a value of absolute value 1 as two '
    'preimages makes every k produce an even count, in particular 4 at k = 2 and 2 at k = 4, so that rule '
    'admits no k at all and the true count at k = 4 is 1; keeping only the plus branch gives counts drawn '
    'from the set {0, 1, 2} over the whole sweep, so 3 is unreachable; the closed interval [0, 2*pi] at '
    'k = 1 returns 5 solutions rather than 3 while the half-open interval returns 4, and sin x = 0 alone '
    'returns 3 points on the closed interval against 2 on the half-open one, which is exactly the '
    'miscount described; and the endpoint condition itself was solved in full, abs(1 + k) = 3 giving '
    'k = 2 or k = -4 and abs(1 - k) = 3 giving k = -2 or k = 4, so the sign precondition k >= 0 is what '
    'removes two of the four roots. The extreme values were confirmed as well, the expression '
    'abs(3*sin x - 1) reaching 4 at 3*pi/2 and 2 at pi/2 with 0 attained at sin x = 1/3, which supports '
    'the graphical remark that odd intersection counts arise only when the horizontal line passes through '
    'an odd number of extreme points at once. '
    'Collision sweep on 6437 de-duplicated items (85 files: the bank sets directory of 63 files plus k1 '
    'out plus k2 out), run directly in this session because no collide_b20.py exists in the tree yet. '
    'Scan E1, an absolute value written with the left-right delimiters in the same question as a sine, a '
    'cosine or a tangent, returns 4 items: chap-07-trigonometry-q92 and chap-14-infiniteseries-q54 use the '
    'bars only to wrap a value that is being evaluated, chap-07-trigonometry-q183 puts them inside a '
    'definite integral, and gen-chap-07-trigonometry-q029 sums three absolute sines to study a range; not '
    'one of them is an equation carrying a parameter, so the G of this item is untouched. Scan E2, the '
    'stated interval 0 <= x < 2*pi, returns 7 items, of which the counting ones are '
    'gen-chap-07-trigonometry-q079 and gen-chap-07-trigonometry-q102, both of which hand over a fixed '
    'equation and ask how many solutions it has, the reverse direction of travel from this item, and both '
    'of which live in subtopic 7.7 and resolve by factoring a polynomial in a single trigonometric '
    'function. Scan E3, the phrase for a prescribed number of solutions, surfaces the two genuine near '
    'neighbours and both are logged rather than waved away. The first is '
    'gen-chap-07-trigonometry-q059, which also fixes a parameter by demanding exactly 3 distinct solutions '
    'on 0 <= x < 2*pi and so shares the shape of A, but it carries no absolute value at all, its mechanism '
    'is a double-angle reduction followed by factoring a quadratic in cos x, its subtopics are 7.7 and '
    '7.6 rather than 7.3, it is multiple choice asking for a whole set of parameter values, and its answer '
    'is a two-element set; the pair is therefore recorded as a WATCH and cleared under iron rule 5, since '
    'G and M both differ. The second is gen-chap-03-real-q031, which asks for the value of k making '
    'abs(x^2 - 6x + 8) = k carry exactly 3 real roots, the closest skeleton in the corpus in that the odd '
    'count again forces a tangency, but it sits in chapter 3 on subtopics 3.7 and 3.4, its inner function '
    'is a parabola whose fold produces a local maximum at a single interior point rather than a periodic '
    'wave restricted to one period, it is multiple choice, and no interval convention is involved; the '
    'transfer of the idea across chapters is what makes this item hard rather than derivative, and the '
    'pair is logged as a WATCH as well. Scan E4 over the 48 items carrying subtopic 7.3 finds no item '
    'whose answer is a parameter value, the nearest being gen-chap-07-trigonometry-q043, which counts the '
    'solutions of sin x = x/10 and hands over no parameter, so the pair (subtopic 7.3 and A-PARAM-VALUE) '
    'is empty in the corpus. The mold triple G-ABS-EQ-PARAM-SOLUTION-COUNT / A-PARAM-VALUE / '
    'M-ABS-TWO-BRANCH-ROOT-COUNT appears once in the register of 144 rows, namely as this item itself, and '
    'the banned saturated molds of section 4.1 are all absent, in particular M-SECTOR-FORMULAS is nowhere '
    'near this item. Since this is a fill item there is no choice list, so no answer slot exists and '
    'nothing about the answer could have been positioned by hand.',
)

# -*- coding: utf-8 -*-
add(
    154,
    ['7.11'],
    'ยาก',
    'เซกเตอร์ของวงกลมรูปหนึ่งมีเส้นรอบรูปยาว $24$ หน่วย โดยเส้นรอบรูปนับรัศมีทั้งสองเส้นและส่วนโค้ง '
    'ถ้ารัศมีของเซกเตอร์รูปนี้ยาวไม่เกิน $5$ หน่วย และมุมที่จุดศูนย์กลางของเซกเตอร์มีขนาด $\\theta$ เรเดียน '
    'โดยที่ $0 < \\theta \\le 2\\pi$ แล้วพื้นที่ของเซกเตอร์รูปนี้มีค่าสูงสุดที่เป็นไปได้คือกี่ตารางหน่วย',
    [
        '$35$',
        '$36$',
        '$60$',
        '$70$',
    ],
    0,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• <b>เส้นรอบรูปของเซกเตอร์</b> คือเส้นที่เดินรอบขอบของเซกเตอร์จริง ๆ ซึ่งมีสามท่อน '
        'คือรัศมีสองเส้นกับส่วนโค้งอีกหนึ่งเส้น ⇒ ถ้ารัศมียาว $r$ หน่วย และส่วนโค้งยาว $s$ หน่วย '
        'เส้นรอบรูปจะเท่ากับ $2r + s$ หน่วย · ⛔ อย่าสับสนกับเส้นรอบวงของวงกลมทั้งวง '
        'ซึ่งเป็นส่วนโค้งล้วน ๆ ไม่มีรัศมีรวมอยู่ด้วยเลย',
        '• <b>ความยาวส่วนโค้ง</b> $s = r\\theta$ เมื่อ $\\theta$ เป็นขนาดของมุมที่จุดศูนย์กลางในหน่วย<b>เรเดียน</b> · '
        'เหตุผล : หนึ่งเรเดียนถูกนิยามให้เป็นมุมที่รองรับส่วนโค้งยาวเท่ากับรัศมีพอดี '
        '⇒ มุมขนาด $\\theta$ เรเดียนจึงรองรับส่วนโค้งยาวเป็น $\\theta$ เท่าของรัศมี · '
        'พลิกกลับได้เป็น $\\theta = \\dfrac{s}{r}$ ซึ่งใช้ตรวจย้อนว่ามุมที่ได้ยังเป็นมุมของเซกเตอร์จริงหรือไม่',
        '• <b>พื้นที่ของเซกเตอร์</b> $= \\dfrac{1}{2} r s = \\dfrac{1}{2} r^2 \\theta$ ตารางหน่วย · '
        'เหตุผล : เซกเตอร์กินพื้นที่ของวงกลมทั้งวงตามสัดส่วนของมุม ⇒ พื้นที่ $= \\dfrac{\\theta}{2\\pi} \\times \\pi r^2 '
        '= \\dfrac{1}{2} r^2 \\theta$ แล้วแทน $r\\theta$ ด้วย $s$ ก็ได้รูปแรกทันที '
        '⇒ ⛔ สัมประสิทธิ์ $\\dfrac{1}{2}$ หายไปไม่ได้เด็ดขาด',
        '• <b>ค่าสูงสุดของพาราโบลาคว่ำเมื่อตัวแปรถูกจำกัดช่วง</b> : กราฟของ $y = ax^2 + bx + c$ ที่มี $a < 0$ '
        'จะไต่ขึ้นเรื่อย ๆ จนถึงจุดยอดที่ $x = \\dfrac{-b}{2a}$ แล้วจึงเลี้ยวลง · '
        '⭐ แต่ถ้าโจทย์ยอมให้ $x$ วิ่งได้เพียงบางช่วง และจุดยอด<b>หลุดออกนอกช่วงนั้น</b> '
        'ค่าสูงสุดจะไม่ได้อยู่ที่จุดยอด แต่ย้ายไปอยู่ที่<b>ขอบของช่วงด้านที่ใกล้จุดยอดที่สุด</b> '
        'เพราะตลอดช่วงที่ใช้ได้กราฟยังไต่ขึ้นทางเดียว ยังไม่ทันเลี้ยวลงเลย',
        '• <b>เงื่อนไขทุกข้อในโจทย์ต้องเป็นจริงพร้อมกัน</b> : คำว่า “ยาวไม่เกิน $5$ หน่วย” แปลเป็นอสมการได้ว่า $r \\le 5$ '
        'ส่วนเงื่อนไข $0 < \\theta \\le 2\\pi$ บังคับว่ารูปที่ได้ต้องเป็นเซกเตอร์จริง คือกางแล้วไม่เกินหนึ่งรอบวง '
        '⇒ ค่าที่ผ่านเงื่อนไขบางข้อแต่ตกเงื่อนไขอื่นถือว่า<b>ใช้ไม่ได้</b> ต้องคัดทิ้งทั้งค่า',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• เซกเตอร์รูปหนึ่งมีเส้นรอบรูปยาว $24$ หน่วย โดยนับรัศมีทั้งสองเส้นและส่วนโค้ง ⇒ $2r + s = 24$',
        '• รัศมียาวไม่เกิน $5$ หน่วย ⇒ $r \\le 5$',
        '• มุมที่จุดศูนย์กลางมีขนาด $\\theta$ เรเดียน โดยที่ $0 < \\theta \\le 2\\pi$',
        '• สังเกตหน้าตาก่อนลงมือ : โจทย์ให้เงื่อนไขมาสองชั้น ชั้นแรกคือเส้นรอบรูปคงที่ซึ่งเป็นสมการ '
        'ชั้นที่สองคือเพดานของรัศมีซึ่งเป็น<b>อสมการ</b> · เงื่อนไขที่เป็นอสมการมักถูกอ่านผ่านตาไป '
        'ทั้งที่ในข้อนี้มันคือตัวชี้ขาดคำตอบทั้งข้อ ⇒ ห้ามลืมเด็ดขาดว่า $r$ ขึ้นไปได้ไกลสุดแค่ $5$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าสูงสุดที่เป็นไปได้ของพื้นที่เซกเตอร์ เมื่อ $r$ กับ $\\theta$ วิ่งไปได้ทุกค่าที่ยัง<b>ไม่ขัด</b>เงื่อนไขทั้งสามข้อข้างบนพร้อมกัน',
        '',
        '<b>【 ใช้เส้นรอบรูปกำจัดส่วนโค้งออกไป ให้พื้นที่เหลือตัวแปรเดียวคือรัศมี จนได้พาราโบลาคว่ำ '
        'แล้วตรวจว่าจุดยอดของมันตกอยู่ในช่วงที่โจทย์อนุญาตหรือไม่ ถ้าไม่ตกก็ไล่ค่าไปที่ขอบของช่วง '
        'จากนั้นตรวจย้อนว่ามุมที่ได้ยังเป็นมุมของเซกเตอร์จริง 】</b>',
        '',
        '<b>ขั้นที่ 1 · เขียนพื้นที่ให้เหลือตัวแปรเดียว</b>',
        '• สูตรที่ใช้ : เส้นรอบรูป $= 2r + s$ และพื้นที่ $= \\dfrac{1}{2} r s$',
        '• ระบุตัวแปรให้ชัดก่อนแทนค่า : $r$ คือความยาวรัศมีเป็นหน่วย · $s$ คือความยาวส่วนโค้งเป็นหน่วย · '
        'ทั้งสองตัวเป็นความยาว จึงเป็นจำนวนบวกทั้งคู่',
        '• แทนค่าในเงื่อนไขเส้นรอบรูป : $2r + s = 24$ ⇒ ย้ายข้างได้ $s = 24 - 2r$ '
        '⇒ ตอนนี้ส่วนโค้งไม่ใช่ตัวแปรอิสระอีกต่อไป แต่ถูกรัศมีลากไปด้วยทุกครั้งที่รัศมีขยับ',
        '• แทน $s$ ลงในสูตรพื้นที่ : $A = \\dfrac{1}{2} r (24 - 2r)$',
        '• ยุบให้เรียบร้อย : $A = \\dfrac{1}{2}(24r - 2r^2) = 12r - r^2$ '
        '⇒ ได้ฟังก์ชันของ $r$ เพียงตัวเดียวตามที่ต้องการ',
        '',
        '<b>ขั้นที่ 2 · ดูหน้าตาของ $A(r)$ ว่ามันสูงสุดตรงไหนถ้าไม่มีเงื่อนไขอะไรมาขวาง</b>',
        '• จัดเรียงตามกำลัง : $A(r) = -r^2 + 12r$ ⇒ เทียบกับ $ax^2 + bx + c$ ได้ $a = -1$ , $b = 12$ , $c = 0$',
        '• เพราะ $a = -1 < 0$ กราฟจึงเป็น<b>พาราโบลาคว่ำ</b> ⇒ มันมีจุดสูงสุดจุดเดียวคือจุดยอด',
        '• สูตรตำแหน่งจุดยอด : $r = \\dfrac{-b}{2a}$ ⇒ แทนค่า $r = \\dfrac{-12}{2(-1)} = \\dfrac{-12}{-2} = 6$',
        '• แทนกลับเพื่อดูความสูงของจุดยอด : $A(6) = 12(6) - 6^2 = 72 - 36 = 36$ '
        '⇒ ถ้าโจทย์ปล่อยรัศมีวิ่งได้อิสระ คำตอบก็ควรเป็น $36$ ตารางหน่วย',
        '',
        '<b>ขั้นที่ 3 · จุดพลิกของข้อนี้ — จุดยอดอยู่นอกช่วงที่โจทย์อนุญาต</b>',
        '• ⛔ โจทย์บังคับไว้ว่า $r \\le 5$ แต่จุดยอดอยู่ที่ $r = 6$ ซึ่ง $6 > 5$ '
        '⇒ รัศมี $6$ หน่วย<b>ผิดเงื่อนไข</b> ใช้ไม่ได้ ⇒ ค่า $36$ เอื้อมไม่ถึงตั้งแต่ต้น',
        '• ถามต่อว่าแล้วบนช่วงที่ใช้ได้จริง กราฟทำตัวอย่างไร : พิจารณาอัตราการเปลี่ยนแปลง '
        '$\\dfrac{dA}{dr} = 12 - 2r$ ซึ่งเป็นบวกทุกค่าที่ $r < 6$ ⇒ ตลอดช่วง $r \\le 5$ ฟังก์ชัน $A$ '
        '<b>เพิ่มขึ้น</b>อย่างเดียว ยังไม่ถึงจุดเลี้ยว',
        '• ดูซ้ำอีกทางโดยไม่ต้องใช้อัตราการเปลี่ยนแปลง : จัดกำลังสองสมบูรณ์ได้ $A = 36 - (r - 6)^2$ '
        '⇒ อยากให้ $A$ มาก ต้องทำให้ $(r - 6)^2$ เล็ก คือดัน $r$ ให้เข้าใกล้ $6$ มากที่สุดเท่าที่กติกายอม '
        '⇒ กติกายอมให้ไกลสุดแค่ $r = 5$',
        '• สรุปตำแหน่งที่ให้ค่าสูงสุด : ⇒ ค่าสูงสุดเกิดที่<b>ขอบของช่วง</b> คือ $r = 5$ ⛔ ไม่ใช่ที่จุดยอด',
        '• แทนค่า : $A(5) = 12(5) - 5^2 = 60 - 25 = 35$ ตารางหน่วย',
        '',
        '<b>ขั้นที่ 4 · ตรวจว่าเซกเตอร์ที่ได้มีอยู่จริง</b>',
        '• ⭐ ยังปิดข้อไม่ได้จนกว่าจะรู้ว่า $r = 5$ สร้างเซกเตอร์ที่ถูกกติกาข้อสุดท้ายด้วย คือ $0 < \\theta \\le 2\\pi$',
        '• หาส่วนโค้งก่อน : $s = 24 - 2r$ ⇒ แทนค่า $s = 24 - 2(5) = 24 - 10 = 14$ หน่วย',
        '• หามุมจากสูตร $\\theta = \\dfrac{s}{r}$ ⇒ แทนค่า $\\theta = \\dfrac{14}{5} = 2.8$ เรเดียน',
        '• เทียบกับกติกา : $2.8 > 0$ ✓ และ $2.8 \\le 2\\pi$ เพราะ $2\\pi$ มีค่าประมาณ $6.28$ ✓ '
        '⇒ เซกเตอร์รัศมี $5$ หน่วยที่กางเป็นมุม $2.8$ เรเดียนนี้มีอยู่จริง ⇒ ค่า $35$ ใช้ได้',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่ารัศมีหลายค่าในช่วงที่ใช้ได้แล้วดูแนวโน้ม '
        'พร้อมหาขอบล่างของรัศมีจากเงื่อนไขของมุม)</b>',
        '• เส้นทางข้างบนตัดสินด้วยรูปร่างของกราฟ การตรวจรอบนี้จะไม่แตะกราฟเลย '
        'แต่จะลองแทนค่าเป็นตัวเลขล้วนแล้วดูว่าพื้นที่เดินไปทางไหน',
        '• $r = 3$ ⇒ $s = 24 - 6 = 18$ ⇒ $\\theta = \\dfrac{18}{3} = 6$ ซึ่งไม่เกิน $2\\pi$ ✓ '
        '⇒ $A = \\dfrac{1}{2}(3)(18) = 27$',
        '• $r = 4$ ⇒ $s = 16$ ⇒ $\\theta = 4$ ✓ ⇒ $A = \\dfrac{1}{2}(4)(16) = 32$',
        '• $r = 4.5$ ⇒ $s = 15$ ⇒ $\\theta = \\dfrac{10}{3}$ ✓ ⇒ $A = \\dfrac{1}{2}(4.5)(15) = 33.75$',
        '• $r = 5$ ⇒ $s = 14$ ⇒ $\\theta = 2.8$ ✓ ⇒ $A = \\dfrac{1}{2}(5)(14) = 35$',
        '• อ่านแนวโน้ม : $27 < 32 < 33.75 < 35$ ⇒ พื้นที่เพิ่มขึ้นเรื่อย ๆ จนไปสุดที่ขอบพอดี '
        '⇒ ยืนยันว่าค่าสูงสุดอยู่ที่ขอบจริง ไม่มีค่าใดในช่วงแซง $35$ ได้ ✓',
        '• 📌 ปิดท้ายด้วยการหาขอบล่างของรัศมี เพื่อยืนยันว่า $6$ ไม่ได้แอบอยู่ในช่วงที่ใช้ได้ : '
        'เงื่อนไข $\\theta \\le 2\\pi$ เขียนได้เป็น $\\dfrac{24 - 2r}{r} \\le 2\\pi$ ⇒ คูณไขว้ด้วย $r$ ซึ่งเป็นบวก '
        'ได้ $24 - 2r \\le 2\\pi r$ ⇒ $24 \\le (2 + 2\\pi) r$ ⇒ $r \\ge \\dfrac{24}{2 + 2\\pi}$ ซึ่งมีค่าประมาณ $2.90$',
        '• ⇒ ช่วงที่ใช้ได้จริงทั้งหมดคือ $2.90 \\le r \\le 5$ ซึ่ง<b>ไม่มี</b> $r = 6$ อยู่ในนั้นแน่นอน ✓ '
        'และที่ปลายล่างสุด $r \\approx 2.90$ พื้นที่มีค่าประมาณ $26.37$ ตารางหน่วย ซึ่งน้อยกว่า $35$ อยู่มาก '
        '⇒ ปลายล่างไม่ใช่ผู้ชนะ ✓',
        '',
        '✅ <b>คำตอบ</b> พื้นที่ของเซกเตอร์รูปนี้มีค่าสูงสุดที่เป็นไปได้คือ $35$ ตารางหน่วย '
        '(เกิดที่รัศมี $5$ หน่วย ส่วนโค้ง $14$ หน่วย และมุม $2.8$ เรเดียน) → <b>ตัวเลือก 1</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• โจทย์หาค่าสูงสุดที่มีของสองอย่างผูกกันอยู่ ให้<b>ยุบเหลือตัวแปรเดียวก่อนเสมอ</b> '
        'โดยใช้เงื่อนไขที่เป็นสมการเป็นตัวกำจัด แล้วค่อยดูหน้าตาของฟังก์ชันที่เหลือ '
        '⇒ ถ้ายุบแล้วออกมาเป็นพาราโบลา ก็จบด้วยจุดยอดหรือขอบช่วงเสมอ',
        '• จำประโยคเดียวนี้ให้ขึ้นใจ : <b>หาจุดยอดได้ ยังไม่ใช่ว่าใช้จุดยอดได้</b> · '
        'ทุกครั้งที่โจทย์แถมอสมการของตัวแปรมาให้ ต้องเอาตำแหน่งจุดยอดไปทาบกับอสมการนั้นก่อน '
        'ถ้าจุดยอดหลุดออกไป ให้ย้ายไปตอบที่ขอบด้านที่ใกล้จุดยอดที่สุดทันที',
        '• การจัดกำลังสองสมบูรณ์ $A = 36 - (r - 6)^2$ เป็นเครื่องมือที่เห็นภาพเร็วกว่าการหาอนุพันธ์ในข้อแบบนี้ '
        'เพราะมันบอกทั้งความสูงสุดของกราฟและทิศที่ต้องดันตัวแปรไปในบรรทัดเดียว · '
        'และก่อนวงคำตอบให้แทนค่ากลับเสมอ เพื่อดูว่ารูปที่ได้ยังมีอยู่จริงตามเงื่อนไขที่เหลือ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $36$ เพราะเขียน $A = 12r - r^2$ ถูกแล้ว แล้วใช้จุดยอดที่ $r = 6$ ทันที '
        '<b>โดยละเลยเงื่อนไขที่ว่ารัศมียาวไม่เกิน $5$ หน่วย</b> · พิสูจน์ว่าผิด : รัศมี $6$ หน่วยขัดกับ $r \\le 5$ '
        'ตั้งแต่บรรทัดแรกที่โจทย์กำหนด ⇒ เซกเตอร์รูปนั้นไม่อยู่ในกลุ่มที่โจทย์พูดถึงเลย · '
        'อีกทั้งบนช่วงที่ใช้ได้ $A = 36 - (r - 6)^2$ โดยมี $(r - 6)^2 \\ge 1$ เสมอ ⇒ $A \\le 35$ ตลอดช่วง '
        '⇒ ค่า $36$ เอื้อมไม่ถึงจริง ๆ',
        '• ได้ค่า $60$ เพราะใช้ $r = 5$ ถูกแล้ว แต่หาขนาดมุมผิดเป็น $\\theta = \\dfrac{24}{5}$ '
        'คือเอา<b>เส้นรอบรูปทั้งเส้น</b>ไปหารด้วยรัศมี แทนที่จะเอาเฉพาะความยาวส่วนโค้ง $14$ ไปหาร '
        'แล้วได้ $A = \\dfrac{1}{2}(5)^2\\left(\\dfrac{24}{5}\\right) = 60$ · พิสูจน์ว่าผิด : ถ้า $\\theta = \\dfrac{24}{5}$ จริง '
        'ส่วนโค้งจะยาว $r\\theta = 5 \\times \\dfrac{24}{5} = 24$ หน่วย ⇒ เส้นรอบรูปกลายเป็น $2(5) + 24 = 34$ หน่วย '
        'ซึ่งไม่ใช่ $24$ หน่วยตามที่โจทย์กำหนด',
        '• ได้ค่า $70$ เพราะใช้ $r = 5$ และ $s = 14$ ถูกทั้งคู่ แต่<b>ลืมสัมประสิทธิ์</b> $\\dfrac{1}{2}$ ในสูตรพื้นที่ '
        '⇒ คำนวณเป็น $rs = 5(14) = 70$ · พิสูจน์ว่าผิด : วงกลมเต็มวงรัศมี $5$ หน่วยมีพื้นที่ $25\\pi$ '
        'หรือประมาณ $78.54$ ตารางหน่วย และเซกเตอร์นี้กินเพียงสัดส่วน $\\dfrac{2.8}{2\\pi}$ '
        'หรือประมาณ $44.6$ ส่วนใน $100$ ส่วนของวงเต็ม ⇒ พื้นที่ต้องประมาณ $35$ ตารางหน่วย '
        'ค่า $70$ คิดเป็นเกือบ $90$ ส่วนใน $100$ ส่วนของวงเต็ม ซึ่งต้องใช้มุมกว้างราว $5.6$ เรเดียน ไม่ใช่ $2.8$ เรเดียน',
        '• อีกเส้นทางที่พลาดกันคือคิดกลับด้านว่ารัศมียิ่งเล็กยิ่งเหลือส่วนโค้งยาว พื้นที่จึงน่าจะมากที่สุดที่ปลายล่างของช่วง '
        '· พิสูจน์ว่าผิดด้วยการแทนค่าตรง ๆ : ที่ $r \\approx 2.90$ ได้ $A \\approx 26.37$ ตารางหน่วย '
        'ซึ่งน้อยกว่า $35$ ⇒ ปลายล่างให้พื้นที่น้อยกว่าปลายบนอย่างชัดเจน '
        'เพราะพื้นที่ $\\dfrac{1}{2} r s$ ขึ้นกับ<b>ผลคูณ</b>ของสองความยาว ไม่ได้ขึ้นกับส่วนโค้งเพียงอย่างเดียว',
    ],
    'V.mold: G = a circular sector whose perimeter, counted as the two radii plus the arc, is fixed at 24 '
    'units, together with a cap saying the radius is at most 5 units and the standing requirement that the '
    'central angle satisfies 0 < theta <= 2*pi / A = the greatest possible area of that sector / '
    'M = M-FIXED-PERIMETER-SECTOR-MAX-AT-RADIUS-CAP, that is, eliminate the arc through s = 24 - 2r to get '
    'the downward parabola A(r) = 12r - r^2, locate its vertex at r = 6, notice that the cap throws that '
    'vertex out of the admissible set, and therefore read the maximum off the boundary r = 5 after checking '
    'that the angle it produces is still a legal sector angle. '
    'Rubric F2 C2 P1 T3 L0 = 8/15, total at least 8 with T at least 2 -> level: ยาก. '
    'F = 2 for the two formula blocks that are both needed, the perimeter description 2r + s = 24 and the '
    'sector area one half times r times s; nothing beyond those two is required, so F was not raised to 3. '
    'C = 2 because a sector item has to be joined to quadratic optimisation and then to a feasibility test '
    'on the angle, three separate kinds of reasoning meeting in one item. P = 1 because once the picture is '
    'settled the arithmetic is only 12*5 - 25 and one division, with no stage feeding a long computation '
    'into the next. T = 3 because the trap is the whole item: the vertex r = 6 is computed correctly and is '
    'still unusable, the wrong value 36 rewards exactly that omission, and the true maximum sits on the '
    'boundary of an interval where no stationary point exists, which is the case students are least drilled '
    'on. L = 0 because the figure is described symbolically, there is no worded scene to model and no '
    'drawing is needed beyond a bare sector. The total is 8, below the 12 that the highest level requires, '
    'so T = 3 on its own cannot lift it. Scoring was written before the level was read off. '
    'sympy (verify_b21.py): expand(Rational(1,2)*r*(24-2*r)) returns 12*r - r**2, solve(diff(A,r),r) '
    'returns [6] and A.subs(r,6) is 36, so the unconstrained vertex is confirmed to land exactly on the '
    'offered wrong value; A.subs(r,5) is 35 and a sweep of A over r = 2.90, 2.91, ..., 5.00 attains its '
    'largest value at the right endpoint 500/100, so the maximum really sits on the boundary. The angle at '
    'the answer was machine-checked too: (24 - 2*5)/5 = 14/5 = 2.8 which is at most 2*pi = 6.28319, and the '
    'lower cut 24/(2 + 2*pi) = 2.897436 follows from theta <= 2*pi, so the admissible interval is about '
    '[2.8974, 5] and 6 lies well outside it. Every wrong value was machine-computed from a named error path '
    'instead of being invented: A(6) = 36 for using the vertex against the cap, '
    '(1/2)*25*(24/5) = 60 for dividing the whole perimeter by the radius instead of the arc, and '
    '5*14 = 70 for dropping the coefficient one half. The four sample points quoted in the verification '
    'block were evaluated exactly, A(3) = 27, A(4) = 32, A(9/2) = 135/4 and A(5) = 35 with angles 6, 4, '
    '10/3 and 14/5, all legal, the low end gives A = 26.3741, and the identity '
    '36 - (r - 6)**2 - (12*r - r**2) simplifies to 0, which is the completing-the-square form quoted in the '
    'technique block. '
    'Collision sweep on 6457 items (bank 63 files + k1 out + k2 out), scans run over that merged id set: '
    'the pair (a word for perimeter, the word for sector) returns 3 items, gen-chap-07-trigonometry-q031 '
    'which gives radius and area and asks for the perimeter, gen-chap-07-trigonometry-q034 which gives '
    'perimeter and area and asks for the sum of the admissible angles, and chap-13-calculus-q97. The pair '
    '(the word for sector, either word for a largest value) returns exactly 1 item, chap-13-calculus-q97, '
    'logged as a WATCH and cleared under iron rule 5: that item fixes a perimeter of 20 with no cap at all, '
    'so its answer is the vertex value 25 and it is filed under 13.8 as a derivative exercise, whereas the '
    'mechanism here is the opposite one, a vertex that cannot be reached so the maximum is forced onto the '
    'boundary, which is also why the vertex value 36 is a wrong value here rather than the key. The pair '
    '(radius, at most) returns 0 items and the phrase for the greatest possible value returns 2 items, both '
    'chapter 7 range-of-a-function questions with no sector in them. Among the 32 items carrying subtopic '
    '7.11 exactly one contains the words for at most, gen-chap-07-trigonometry-q133 of batch 20, where that '
    'phrase describes a distance condition and not a bound on a variable being optimised. The mechanism '
    'label M-FIXED-PERIMETER-SECTOR-MAX-AT-RADIUS-CAP is absent from the register of used mechanisms, and '
    'the saturated device segment area = sector minus triangle is not touched anywhere in this item. '
    'Choices are ordered ascending by numeric value (35, then 36, then 60, then 70), so the answer slot is '
    'forced by that rule and was not chosen.',
)

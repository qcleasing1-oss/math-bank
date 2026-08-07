# -*- coding: utf-8 -*-
add_fill(
    134,
    ['7.11'],
    'ยาก',
    'ส่วนของเส้นตรง $AB$ ยาว $20$ หน่วย และจุด $C$ เป็นจุดบนส่วนของเส้นตรง $AB$ '
    'โดยที่ $AC$ ยาวกว่า $CB$ เขียนรูปครึ่งวงกลมสามรูปไว้ทางด้านเดียวกันของ $AB$ ได้แก่ '
    'ครึ่งวงกลมที่มี $AB$ เป็นเส้นผ่านศูนย์กลาง ครึ่งวงกลมที่มี $AC$ เป็นเส้นผ่านศูนย์กลาง '
    'และครึ่งวงกลมที่มี $CB$ เป็นเส้นผ่านศูนย์กลาง ถ้าบริเวณที่อยู่ภายในครึ่งวงกลมที่มี $AB$ '
    'เป็นเส้นผ่านศูนย์กลาง แต่อยู่ภายนอกครึ่งวงกลมอีกสองรูป มีพื้นที่เท่ากับ $24\\pi$ '
    'ตารางหน่วย แล้ว $AC$ ยาวกี่หน่วย',
    '12',
    ['12', '12.0'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• พื้นที่ของวงกลมที่มีรัศมียาว $r$ เท่ากับ $\\pi r^{2}$ · ครึ่งวงกลมคือครึ่งหนึ่งของวงกลมเต็มวงพอดี '
        'พื้นที่จึงเท่ากับ $\\dfrac{1}{2}\\pi r^{2}$ · มองด้วยภาษาของหัวข้อนี้ก็ได้ผลเดียวกัน คือครึ่งวงกลมเป็นเซกเตอร์ '
        'ที่มีมุมที่จุดศูนย์กลางเท่ากับ $\\pi$ เรเดียน (ครึ่งหนึ่งของหนึ่งรอบซึ่งเท่ากับ $2\\pi$ เรเดียน) '
        'แทนลงในสูตรพื้นที่เซกเตอร์ $A = \\dfrac{1}{2}r^{2}\\theta$ ได้ $A = \\dfrac{1}{2}r^{2}\\pi$ ตรงกันพอดี',
        '• ⛔ กับดักที่ต้องปิดตั้งแต่บรรทัดแรก : สูตรพื้นที่กินค่า<b>รัศมี</b> ไม่ใช่ค่าเส้นผ่านศูนย์กลาง '
        'ถ้าเส้นผ่านศูนย์กลางยาว $d$ แล้วรัศมียาว $r = \\dfrac{d}{2}$ ⇒ พื้นที่ครึ่งวงกลมเขียนด้วยเส้นผ่านศูนย์กลางได้เป็น '
        '$\\dfrac{1}{2}\\pi\\left(\\dfrac{d}{2}\\right)^{2} = \\dfrac{\\pi d^{2}}{8}$ · '
        'ที่ต้องระวังเป็นพิเศษเพราะพื้นที่ผูกกับ<b>กำลังสอง</b>ของความยาว ⇒ เผลอเอา $d$ ไปแทนที่ $r$ ตรง ๆ '
        'พื้นที่จะโตเกินจริงถึง $4$ เท่า ไม่ใช่แค่ $2$ เท่า',
        '• จุด $C$ อยู่บนส่วนของเส้นตรง $AB$ ⇒ ท่อนย่อยสองท่อนต่อกันได้เส้นเดิมพอดี คือ $AC + CB = AB$ เสมอ '
        '⇒ รู้ท่อนหนึ่งก็ได้อีกท่อนทันทีด้วยการลบ จึงตั้งตัวแปรเพียงตัวเดียวก็พอ ไม่ต้องตั้งสองตัวแล้วแก้ระบบสมการ',
        '• สมการกำลังสองในรูป $x^{2} + bx + c = 0$ แยกตัวประกอบได้เมื่อหาจำนวนสองจำนวนที่คูณกันได้ $c$ '
        'และบวกกันได้ $-b$ · เมื่อแยกได้เป็น $(x - p)(x - q) = 0$ แล้ว ผลคูณเป็นศูนย์แปลว่าตัวประกอบตัวใดตัวหนึ่งเป็นศูนย์ '
        '⇒ ได้ราก $2$ ราก คือ $x = p$ และ $x = q$',
        '• ⛔ ประเด็นที่แพ้กันบ่อยที่สุด : “รากของสมการ” กับ “คำตอบของโจทย์” ไม่ใช่สิ่งเดียวกัน '
        'สมการเป็นเพียงการแปลข้อมูล<b>บางส่วน</b>ของโจทย์ให้เป็นสัญลักษณ์ ⇒ รากที่ขัดกับเงื่อนไขอื่นในโจทย์ต้องถูกทิ้ง '
        'เงื่อนไขที่ใช้คัดรากมีทั้งชนิดที่ชัดในตัว (ความยาวต้องเป็นบวก) และชนิดที่โจทย์เขียนบอกเป็นถ้อยคำ',
        '• การแปลถ้อยคำเปรียบเทียบให้เป็นอสมการ : ประโยค “$AC$ ยาวกว่า $CB$” เขียนเป็น $AC > CB$ '
        '⇒ ถ้าให้ $AC = u$ แล้ว $CB = 20 - u$ อสมการกลายเป็น $u > 20 - u$ ⇒ ย้ายข้างได้ $2u > 20$ ⇒ $u > 10$ '
        'อ่านเป็นภาษาคนได้ว่า จุด $C$ ต้องอยู่เลยจุดกึ่งกลางของ $AB$ ไปทางฝั่ง $B$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• ส่วนของเส้นตรง $AB$ ยาว $20$ หน่วย และจุด $C$ เป็นจุดบนส่วนของเส้นตรงนี้ ⇒ $AC + CB = 20$',
        '• เงื่อนไขที่โจทย์เขียนกำกับไว้ชัด ๆ อีกข้อคือ $AC$ ยาวกว่า $CB$',
        '• ครึ่งวงกลมสามรูปอยู่ทางด้านเดียวกันของ $AB$ โดยมี $AB$ · $AC$ · $CB$ เป็นเส้นผ่านศูนย์กลางตามลำดับ '
        '⇒ วาดตามได้ว่าครึ่งวงกลมเล็กสองรูปเรียงกันอยู่ภายในครึ่งวงกลมใหญ่ นั่งอยู่บนเส้น $AB$ เส้นเดียวกัน '
        'และแตะกันที่จุด $C$ เพียงจุดเดียว ⇒ ครึ่งวงกลมเล็กทั้งสองรูปไม่ซ้อนทับกันเลย',
        '• บริเวณที่อยู่ภายในครึ่งวงกลมใหญ่ แต่อยู่ภายนอกครึ่งวงกลมเล็กทั้งสองรูป มีพื้นที่เท่ากับ $24\\pi$ ตารางหน่วย',
        '• สังเกตหน้าตาก่อนลงมือ : พื้นที่ของครึ่งวงกลมทุกรูปมี $\\pi$ เป็นตัวประกอบร่วม และค่าที่โจทย์ให้ก็เขียนในรูป '
        '$24\\pi$ ⇒ $\\pi$ จะถูกหารทิ้งได้ทั้งสมการตั้งแต่ก้าวแรก ⇒ เดาได้ล่วงหน้าว่าคำตอบต้องเป็นจำนวนที่ไม่มี $\\pi$ ติดอยู่ '
        'ใครตอบออกมาแล้วยังมี $\\pi$ ค้างแปลว่าหลงทางแน่นอน',
        '• สังเกตอีกอย่างซึ่งสำคัญกว่า : เงื่อนไข “$AC$ ยาวกว่า $CB$” ไม่ได้ถูกใช้เลยตอนตั้งสมการพื้นที่ '
        'เพราะพื้นที่ไม่สนใจว่าท่อนไหนยาวกว่ากัน ⇒ โจทย์อุตส่าห์เขียนไว้แปลว่าจะต้องได้ใช้ทีหลัง '
        'เป็นสัญญาณล่วงหน้าว่าสมการจะให้รากมากกว่าหนึ่งราก',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาความยาวของ $AC$ ออกมาเป็นจำนวนหน่วย',
        '',
        '<b>【 ตั้ง $AC = u$ ⇒ $CB = 20 - u$ แล้วเปลี่ยนเส้นผ่านศูนย์กลางทั้งสามให้เป็นรัศมีก่อนเข้าสูตร '
        'จากนั้นเขียนพื้นที่ที่เหลือเป็น พื้นที่ครึ่งวงกลมใหญ่ ลบ พื้นที่ครึ่งวงกลมเล็กสองรูป ตั้งให้เท่ากับ $24\\pi$ '
        'ตัด $\\pi$ ทิ้งแล้วแก้สมการกำลังสอง สุดท้ายคัดรากที่เหลือด้วยเงื่อนไข $AC > CB$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · ตั้งตัวแปร แล้วเปลี่ยนเส้นผ่านศูนย์กลางทั้งสามให้เป็นรัศมีก่อนเข้าสูตร</b>',
        '• ระบุตัวแปรก่อนแทนค่า : ให้ $AC = u$ หน่วย · เนื่องจากจุด $C$ อยู่บน $AB$ ซึ่งยาว $20$ หน่วย '
        'จึงได้ $CB = 20 - u$ หน่วยทันที · ทั้งสองท่อนเป็นความยาวจริง จึงต้องเป็นบวกทั้งคู่ ⇒ $0 < u < 20$',
        '• สูตรที่ใช้ : พื้นที่ครึ่งวงกลม $= \\dfrac{1}{2}\\pi r^{2}$ โดยที่ $r$ คือรัศมี '
        '⛔ ทุกความยาวที่โจทย์ให้มาเป็นเส้นผ่านศูนย์กลาง ⇒ ต้องหารสองก่อนเสมอ',
        '• ครึ่งวงกลมใหญ่ : เส้นผ่านศูนย์กลางคือ $AB = 20$ ⇒ รัศมี $= \\dfrac{20}{2} = 10$ '
        '⇒ พื้นที่ $= \\dfrac{1}{2}\\pi(10)^{2} = \\dfrac{1}{2}\\pi(100) = 50\\pi$ ตารางหน่วย',
        '• ครึ่งวงกลมบน $AC$ : เส้นผ่านศูนย์กลางคือ $u$ ⇒ รัศมี $= \\dfrac{u}{2}$ '
        '⇒ พื้นที่ $= \\dfrac{1}{2}\\pi\\left(\\dfrac{u}{2}\\right)^{2} = \\dfrac{1}{2}\\pi\\cdot\\dfrac{u^{2}}{4} '
        '= \\dfrac{\\pi u^{2}}{8}$ ตารางหน่วย',
        '• ครึ่งวงกลมบน $CB$ : เดินเส้นทางเดียวกันโดยเปลี่ยน $u$ เป็น $20 - u$ '
        '⇒ พื้นที่ $= \\dfrac{\\pi(20 - u)^{2}}{8}$ ตารางหน่วย',
        '• ยืนยันตัวหาร $8$ อีกรอบกันลืม : ตัวประกอบ $\\dfrac{1}{2}$ มาจากคำว่าครึ่งวงกลม '
        'และตัวประกอบ $\\dfrac{1}{4}$ มาจากการยกกำลังสองของ $\\dfrac{d}{2}$ ⇒ คูณกันได้ $\\dfrac{1}{8}$',
        '',
        '<b>ขั้นที่ 2 · ตั้งสมการพื้นที่ที่เหลือ แล้วตัด $\\pi$ ทิ้งทั้งสมการ</b>',
        '• เหตุผลที่ใช้การลบได้ตรง ๆ : ครึ่งวงกลมเล็กทั้งสองรูปอยู่ภายในครึ่งวงกลมใหญ่ทั้งคู่ '
        'และไม่ซ้อนทับกันเอง (แตะกันแค่ที่จุด $C$ ซึ่งไม่มีพื้นที่) '
        '⇒ พื้นที่ที่เหลือ $=$ พื้นที่ครึ่งวงกลมใหญ่ $-$ พื้นที่ครึ่งวงกลมเล็กสองรูป โดยไม่ต้องบวกคืนส่วนที่ซ้อนกัน',
        '• แทนค่า : $50\\pi - \\dfrac{\\pi u^{2}}{8} - \\dfrac{\\pi(20 - u)^{2}}{8} = 24\\pi$',
        '• หารทั้งสมการด้วย $\\pi$ (ทำได้เพราะ $\\pi$ ไม่เป็นศูนย์) : '
        '$50 - \\dfrac{u^{2}}{8} - \\dfrac{(20 - u)^{2}}{8} = 24$',
        '• คูณทั้งสมการด้วย $8$ เพื่อล้างตัวส่วน : $400 - u^{2} - (20 - u)^{2} = 192$',
        '',
        '<b>ขั้นที่ 3 · กระจายและยุบให้เป็นสมการกำลังสอง แล้วแยกตัวประกอบ</b>',
        '• กระจายวงเล็บด้วยสูตร $(a - b)^{2} = a^{2} - 2ab + b^{2}$ : '
        '$(20 - u)^{2} = 400 - 40u + u^{2}$',
        '• แทนกลับ : $400 - u^{2} - \\left(400 - 40u + u^{2}\\right) = 192$ '
        '⇒ กระจายเครื่องหมายลบเข้าไป $400 - u^{2} - 400 + 40u - u^{2} = 192$',
        '• ยุบพจน์คล้าย : $400$ กับ $-400$ ตัดกันหมด เหลือ $-2u^{2} + 40u = 192$ '
        '⇒ ย้ายข้างให้เป็นศูนย์ $-2u^{2} + 40u - 192 = 0$',
        '• หารทั้งสมการด้วย $-2$ เพื่อให้สัมประสิทธิ์หน้า $u^{2}$ เป็น $1$ : $u^{2} - 20u + 96 = 0$',
        '• แยกตัวประกอบ : หาสองจำนวนที่คูณกันได้ $96$ และบวกกันได้ $20$ ⇒ ได้ $8$ กับ $12$ '
        '(ตรวจได้ว่า $8 \\times 12 = 96$ และ $8 + 12 = 20$) ⇒ $(u - 8)(u - 12) = 0$',
        '• ผลคูณเป็นศูนย์ ⇒ $u = 8$ หรือ $u = 12$',
        '• ⛔ หยุดตรงนี้ยังไม่ได้ : ทั้ง $8$ และ $12$ ต่างก็อยู่ในช่วง $0 < u < 20$ '
        '⇒ เงื่อนไข “ความยาวต้องเป็นบวก” คัดรากทิ้งไม่ได้เลยสักรากเดียว ต้องหาเงื่อนไขอื่นมาคัด',
        '',
        '<b>ขั้นที่ 4 · คัดรากด้วยเงื่อนไข $AC$ ยาวกว่า $CB$ ⛔ จุดหักของข้อนี้</b>',
        '• เงื่อนไขที่โจทย์ให้มาแต่ยังไม่ได้ใช้คือ $AC > CB$ ⇒ เขียนด้วยตัวแปรได้ $u > 20 - u$ '
        '⇒ ย้ายข้าง $2u > 20$ ⇒ $u > 10$',
        '• ทดสอบรากแรก $u = 8$ : จะได้ $CB = 20 - 8 = 12$ ⇒ $AC = 8$ ซึ่งสั้นกว่า $CB = 12$ '
        '⇒ ขัดกับเงื่อนไขที่โจทย์เขียนไว้ ⇒ ทิ้งรากนี้',
        '• ทดสอบรากที่สอง $u = 12$ : จะได้ $CB = 20 - 12 = 8$ ⇒ $AC = 12$ ซึ่งยาวกว่า $CB = 8$ '
        '⇒ ผ่านเงื่อนไขทุกข้อ (และผ่าน $u > 10$ ด้วย)',
        '• สรุปจากขั้นนี้ : เหลือรากเดียวที่ใช้ได้ คือ $u = AC = 12$ หน่วย',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่า $AC = 12$ กลับเข้าโจทย์แล้วคำนวณพื้นที่ครึ่งวงกลมทั้งสามรูป '
        'ด้วยตัวเลขจริง โดยไม่แตะสมการกำลังสองอีกเลย)</b>',
        '• ถ้า $AC = 12$ แล้ว $CB = 20 - 12 = 8$ ⇒ เส้นผ่านศูนย์กลางทั้งสามเส้นคือ $20$ · $12$ · $8$ '
        '⇒ หารสองได้รัศมีสามค่าคือ $10$ · $6$ · $4$',
        '• พื้นที่ครึ่งวงกลมใหญ่ $= \\dfrac{1}{2}\\pi(10)^{2} = 50\\pi$ ตารางหน่วย',
        '• พื้นที่ครึ่งวงกลมบน $AC$ $= \\dfrac{1}{2}\\pi(6)^{2} = \\dfrac{1}{2}\\pi(36) = 18\\pi$ ตารางหน่วย',
        '• พื้นที่ครึ่งวงกลมบน $CB$ $= \\dfrac{1}{2}\\pi(4)^{2} = \\dfrac{1}{2}\\pi(16) = 8\\pi$ ตารางหน่วย',
        '• พื้นที่ที่เหลือ $= 50\\pi - 18\\pi - 8\\pi = 24\\pi$ ตารางหน่วย ✓ ตรงกับค่าที่โจทย์ให้พอดี',
        '• ตรวจเงื่อนไขอีกข้อให้ครบ : $AC = 12$ ยาวกว่า $CB = 8$ จริง ✓ '
        'และ $12 + 8 = 20$ เท่ากับความยาว $AB$ พอดี ✓',
        '• 📌 เสริมที่ต้องรู้ให้ชัด : ลองแทน $u = 8$ ดูบ้าง จะได้รัศมี $10$ · $4$ · $6$ '
        '⇒ พื้นที่ที่เหลือ $= 50\\pi - 8\\pi - 18\\pi = 24\\pi$ เท่ากันเป๊ะ '
        'เหตุผลคือนิพจน์พื้นที่ที่เหลือยุบได้เป็น $\\dfrac{\\pi}{4}\\,u(20 - u)$ ซึ่งสมมาตรรอบ $u = 10$ '
        '⇒ การสลับ $AC$ กับ $CB$ ไม่ทำให้พื้นที่เปลี่ยนเลย',
        '• ⇒ ข้อสรุปที่ต้องจำจากข้อนี้ : <b>สมการอย่างเดียวแยกสองรากนี้ไม่ได้เลย</b> '
        'เพราะทั้ง $8$ และ $12$ ให้พื้นที่ $24\\pi$ เหมือนกัน ⇒ สิ่งเดียวที่แยกได้คือเงื่อนไข '
        '“$AC$ ยาวกว่า $CB$” ที่โจทย์เขียนไว้ ⇒ การตรวจว่าพื้นที่ออกมาเป็น $24\\pi$ จึงยังไม่พอ '
        'ต้องตรวจอสมการควบคู่ไปด้วยทุกครั้ง',
        '',
        '✅ <b>คำตอบ</b> $AC$ ยาว $12$ หน่วย',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอคำว่า “เส้นผ่านศูนย์กลาง” เมื่อไร ให้เขียน $r = \\dfrac{d}{2}$ กำกับข้างกระดาษทันที<b>ก่อน</b>แตะสูตรพื้นที่ '
        'หรือจำสูตรลัดไปเลยว่าครึ่งวงกลมที่มีเส้นผ่านศูนย์กลาง $d$ มีพื้นที่ $\\dfrac{\\pi d^{2}}{8}$ '
        'จะได้ไม่ต้องหารสองกลางคัน ซึ่งเป็นจุดที่คนพลาดกันมากที่สุด',
        '• พอแก้สมการแล้วได้รากมากกว่าหนึ่งราก ให้ย้อนกลับไปอ่านโจทย์ทีละประโยคเพื่อหาเงื่อนไขที่ยังไม่ได้ใช้ '
        'ประโยคเปรียบเทียบอย่าง “ยาวกว่า” “มากกว่า” “เป็นมุมแหลม” มักถูกเขียนไว้เพื่อการนี้โดยเฉพาะ '
        '⇒ ถ้าอ่านจบแล้วยังมีประโยคที่ไม่เคยถูกแตะเลย แปลว่ายังทำไม่จบ',
        '• นิพจน์พื้นที่ที่เหลือของรูปแบบนี้ยุบได้สวยเป็น $\\dfrac{\\pi}{4}\\,(AC)(CB)$ '
        'ตรวจซ้ำได้เร็วมาก เช่น $\\dfrac{\\pi}{4}(12)(8) = 24\\pi$ ✓ '
        'และรูปนี้ยังบอกใบ้ด้วยว่าพื้นที่ขึ้นกับผลคูณของสองท่อนเท่านั้น จึงสมมาตรและให้สองรากเสมอ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $8$ เพราะแก้สมการได้สองราก $8$ กับ $12$ แล้วหยิบรากแรกที่เจอมาตอบ '
        'โดยไม่ใช้เงื่อนไข $AC$ ยาวกว่า $CB$ เลย — นี่คือกับดักหลักของข้อนี้ และเป็นเส้นทางพลาดที่อันตรายที่สุด '
        'เพราะถ้าเด็กเอา $u = 8$ ไปตรวจโดยคำนวณพื้นที่ จะได้ $50\\pi - 8\\pi - 18\\pi = 24\\pi$ ตรงกับโจทย์ทุกประการ '
        '⇒ การตรวจด้วยพื้นที่ไม่มีทางจับผิดข้อนี้ได้ · สิ่งที่ผิดจริงคือ $u = 8$ ทำให้ $AC = 8$ และ $CB = 12$ '
        'ซึ่งแปลว่า $AC$ สั้นกว่า $CB$ ขัดกับประโยคในโจทย์ตรง ๆ ⇒ วิธีกันคือขีดเส้นใต้ประโยคเงื่อนไขไว้ตั้งแต่อ่านรอบแรก '
        'แล้วเอารากทุกรากไปทดสอบกับประโยคนั้นก่อนตอบ',
        '• ได้ค่า $10 + 2\\sqrt{19} \\approx 18.72$ เพราะเอา $AB$ · $AC$ · $CB$ ไปใช้เป็น<b>รัศมี</b>ตรง ๆ '
        'ลืมว่าโจทย์ให้มาเป็นเส้นผ่านศูนย์กลางจึงต้องหารสองก่อน ⇒ ได้สมการ '
        '$\\dfrac{\\pi}{2}\\left(400 - u^{2} - (20 - u)^{2}\\right) = 24\\pi$ ⇒ $u^{2} - 20u + 24 = 0$ '
        '⇒ $u = 10 \\pm 2\\sqrt{19}$ · ค่านี้ผิดแน่นอน พิสูจน์ได้สองทาง : ทางแรก ถ้ารัศมีของรูปใหญ่เป็น $20$ '
        'เส้นผ่านศูนย์กลางของมันจะยาว $40$ หน่วย ขัดกับ $AB = 20$ ที่โจทย์ให้ · ทางที่สอง '
        'แทน $u = 10 + 2\\sqrt{19}$ กลับเข้านิพจน์พื้นที่ที่ถูกต้อง $\\dfrac{\\pi}{4}u(20 - u)$ '
        'จะได้พื้นที่ $6\\pi$ ไม่ใช่ $24\\pi$ · สังเกตด้วยว่าคำตอบที่ติดกรณฑ์เป็นสัญญาณเตือนอยู่แล้ว '
        'เพราะโจทย์ให้ตัวเลขลงตัวมาทั้งหมด',
        '• ได้ค่า $10 + 2\\sqrt{13} \\approx 17.21$ เพราะใช้สูตรพื้นที่<b>วงกลมเต็มวง</b> $\\pi r^{2}$ '
        'กับทั้งสามรูป แทนที่จะใช้ $\\dfrac{1}{2}\\pi r^{2}$ ของครึ่งวงกลม ⇒ ได้สมการ '
        '$\\pi(100) - \\pi\\left(\\dfrac{u}{2}\\right)^{2} - \\pi\\left(\\dfrac{20 - u}{2}\\right)^{2} = 24\\pi$ '
        '⇒ $u^{2} - 20u + 48 = 0$ ⇒ $u = 10 \\pm 2\\sqrt{13}$ · ค่านี้ผิดแน่นอน เพราะการคูณทุกพจน์ด้วย $2$ '
        'เท่ากับบอกว่าพื้นที่จริงของบริเวณที่เหลือเป็นเพียงครึ่งเดียวของที่ตั้งไว้ '
        '⇒ แทน $u = 10 + 2\\sqrt{13}$ กลับเข้านิพจน์ที่ถูกต้องจะได้พื้นที่ $12\\pi$ พอดี ซึ่งเป็นครึ่งหนึ่งของ $24\\pi$ '
        '⇒ ขัดกับโจทย์ · จุดกันพลาดคือย้ำกับตัวเองว่ารูปทั้งสามเป็นครึ่งวงกลม ตัวประกอบ $\\dfrac{1}{2}$ '
        'ต้องติดไปทุกพจน์ ไม่ใช่ติดแค่พจน์แรก',
        '• ได้ค่า $4\\sqrt{13} \\approx 14.42$ เพราะลบพื้นที่ครึ่งวงกลมเล็กเพียงรูปเดียว คือแก้ '
        '$50\\pi - \\dfrac{\\pi u^{2}}{8} = 24\\pi$ ⇒ $u^{2} = 208$ ⇒ $u = 4\\sqrt{13}$ '
        'ซึ่งมักเกิดจากการอ่านโจทย์ข้ามคำว่า “อีกสองรูป” แล้วนึกว่ามีครึ่งวงกลมเล็กแค่รูปเดียว · '
        'ค่านี้ผิดแน่นอน ตรวจได้โดยแทนกลับเข้านิพจน์ที่ถูกต้อง $\\dfrac{\\pi}{4}u(20 - u)$ '
        'จะได้พื้นที่ $\\left(20\\sqrt{13} - 52\\right)\\pi \\approx 20.11\\pi$ ซึ่งไม่เท่ากับ $24\\pi$ · '
        'อีกทั้งเส้นทางนี้ทิ้งครึ่งวงกลมบน $CB$ หายไปทั้งรูป ทั้งที่โจทย์บรรยายไว้ชัดว่ามีครึ่งวงกลมสามรูป '
        '⇒ นับจำนวนรูปให้ครบก่อนตั้งสมการทุกครั้ง',
    ],
    'V.mold: G = a segment AB of length 20 carrying an interior point C, with three semicircles erected on '
    'the same side of AB on the diameters AB, AC and CB, with the area of the region lying inside the '
    'largest semicircle but outside the two smaller ones handed over as 24*pi, and with the extra verbal '
    'condition that AC is longer than CB / A = the length of AC, asked as a free numeric response with no '
    'candidate values on the page / M = M-SEMICIRCLES-ON-SPLIT-DIAMETER-SOLVE-PART, that is: name AC = u so '
    'that CB = 20 - u, halve each of the three given diameters to reach the radii 10, u/2 and (20 - u)/2, '
    'write the three semicircle areas, subtract the two small ones from the large one, cancel the common '
    'factor pi, clear the denominator 8 to reach the quadratic u^2 - 20u + 96 = 0, factor it as '
    '(u - 8)(u - 12) = 0, and only then use the stated inequality AC > CB to discard one of the two roots. '
    'Rubric F2 C2 P2 T2 L1 = 9/15, which clears the threshold of 8 with T at least 2 and C at least 2, '
    'while the total stays below 12 so the very-hard band is out of reach -> level: ยาก. '
    'F = 2 because two separate pieces of knowledge must be held at once: the area of a semicircle together '
    'with the rule that the formula consumes a radius and not a diameter, and the factoring of a monic '
    'quadratic; F is not 3 because no third identity is needed anywhere, the whole trigonometric content '
    'reduces to the sector area formula specialised to a central angle of pi. C = 2 because the item '
    'genuinely welds a mensuration statement in subtopic 7.11 onto an algebraic one: an area condition '
    'produces the equation while an order condition on two lengths selects among its solutions, and '
    'removing either half leaves the item either unsolvable or ambiguous. P = 2 rather than 3 because the '
    'work runs in two stages of different kinds, building and reducing the area equation and then solving '
    'and filtering, and no stage consumes an object built by a third stage. T = 2 because there is exactly '
    'one hidden turning point, namely that the quadratic returns two admissible positive roots and that the '
    'unused sentence in the statement is the only thing that separates them; T is not 3 because that '
    'insight is the single one required, whereas a T = 3 item needs two independent discoveries before any '
    'computation may start. L = 1 because the statement carries no real-world scene and no figure, yet the '
    'reader must still draw the three semicircles on one line to see that the two small ones sit inside the '
    'large one, touch only at C and therefore never overlap, which is what licenses plain subtraction. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b20.py): in the q134 block, with u positive, the expression '
    'pi*Integer(10)**2/2 - pi*(u/2)**2/2 - pi*((20-u)/2)**2/2 simplifies to pi*u*(20 - u)/4, and solve of '
    'that expression set equal to 24*pi returns exactly [8, 12], so the equation provably carries two '
    'roots; the filter [x for x in roots if x > 20 - x] leaves the single value 12, which is the stored '
    'answer. The independence of the check block was verified separately: substituting u = 12 returns '
    '24*pi and substituting u = 8 also returns 24*pi, which is machine proof that no area computation can '
    'separate the pair, and the difference of the expression evaluated at 10 + t and at 10 - t simplifies '
    'to 0, which exhibits the symmetry about u = 10 that creates the second root. Every error path in the '
    'pitfalls block was computed by machine rather than invented: treating the three given lengths as radii '
    'gives 400 - u^2 - (20-u)^2 = 48 with roots 10 +/- 2*sqrt(19), about 1.2822 and 18.7178, and feeding '
    '10 + 2*sqrt(19) back into the true area expression returns exactly 6*pi instead of 24*pi; using the '
    'full-circle formula for all three shapes doubles every term and gives roots 10 +/- 2*sqrt(13), about '
    '2.7889 and 17.2111, whose true area at 10 + 2*sqrt(13) is exactly 12*pi, one half of the stated '
    'value; and subtracting only the semicircle on AC gives 50*pi - pi*u^2/8 = 24*pi with the single root '
    '4*sqrt(13), about 14.4222, whose true area is 4*pi*(5*sqrt(13) - 13), about 20.111*pi. '
    'Collision sweep re-run for this item over 6437 de-duplicated items (85 files: the bank sets directory '
    'plus k1 out plus k2 out), executed directly in this session because no collide_b20.py exists in the '
    'tree yet: the Thai word for semicircle appears in the question text of exactly 2 items in the whole '
    'corpus, chap-13-calculus-q98 and chap-13-calculus-q237, both of which are chapter 13 optimisation '
    'problems that maximise a rectangle or a window area and share neither the answer type nor the '
    'mechanism; the pair (semicircle and diameter in the same question) returns 0 items, and the phrase '
    'for three semicircles returns 0 items, so the configuration of three semicircles on a split diameter '
    'is untouched. Inside subtopic 7.11 the corpus holds 27 items, of which only 2 hand over an area and '
    'ask for a length, namely gen-chap-07-trigonometry-q115 (two sectors of equal area, asking for the '
    'second radius) and gen-chap-07-trigonometry-q031 (radius and area given, asking for the perimeter of '
    'the sector); neither involves semicircles, neither produces a quadratic, and neither requires a root '
    'to be discarded by an inequality, so G, A and M are all clear. Since this is a fill item there is no '
    'choice list, so no answer slot exists and nothing about the answer could have been positioned by hand.',
)

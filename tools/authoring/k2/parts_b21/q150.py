# -*- coding: utf-8 -*-
add(
    150,
    ['7.11'],
    'ง่าย',
    'ล้อวงกลมล้อหนึ่งมีรัศมียาว $40$ เซนติเมตร '
    'กลิ้งไปบนพื้นราบในแนวเส้นตรงโดยไม่ลื่นไถล '
    'ถ้าล้อนี้หมุนไปครบ $15$ รอบพอดี แล้วล้อนี้เคลื่อนที่ไปได้ระยะทางกี่เซนติเมตร',
    [
        '$80\\pi$',
        '$600\\pi$',
        '$1200\\pi$',
        '$2400\\pi$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• <b>เส้นรอบวงของวงกลม</b> : วงกลมที่มีรัศมียาว $r$ มีเส้นรอบวงยาว $2\\pi r$ '
        'สูตรนี้เขียนได้อีกแบบว่า $\\pi d$ เมื่อ $d$ คือความยาวเส้นผ่านศูนย์กลาง '
        'ทั้งสองแบบเป็นสูตรเดียวกัน เพราะ $d = 2r$ ⇒ $\\pi d = \\pi (2r) = 2\\pi r$ '
        'ที่มาของสูตรคือนิยามของ $\\pi$ เอง นั่นคือ $\\pi$ เป็นอัตราส่วนของเส้นรอบวงต่อเส้นผ่านศูนย์กลาง '
        'ซึ่งได้ค่าเท่ากันหมดไม่ว่าวงกลมจะใหญ่หรือเล็ก ⇒ เส้นรอบวง $= \\pi \\times d$ เสมอ',
        '• <b>กลิ้งโดยไม่ลื่นไถล</b> แปลว่าอะไร : ขณะที่ล้อกลิ้งไปข้างหน้า '
        'จุดบนขอบล้อจะลงมาแตะพื้นทีละจุดเรียงต่อกันไปโดยไม่มีการไถลข้ามจุดใดเลย '
        'จุดที่แตะพื้นจึงเรียงกันเป็นรอยยาวบนพื้น และรอยนั้นก็คือขอบล้อที่ถูกคลี่ออกมาวางราบพอดี '
        '⇒ เมื่อล้อหมุนครบหนึ่งรอบ ขอบล้อคลี่ออกจนครบวง ระยะทางที่ล้อเคลื่อนที่ไปจึงเท่ากับ '
        '<b>เส้นรอบวง</b> ของล้อพอดี ไม่ขาดไม่เกิน '
        '(นึกภาพเชือกที่พันรอบล้อไว้พอดีหนึ่งรอบ แล้วดึงคลี่ออกมาวางเป็นเส้นตรงบนพื้น '
        'ความยาวเชือกที่ได้ก็คือระยะทางของหนึ่งรอบ)',
        '• <b>หลายรอบก็คือการบวกซ้ำ</b> : ทุกรอบล้อเคลื่อนที่ได้ระยะเท่ากันหมด '
        'เพราะเส้นรอบวงของล้อไม่เปลี่ยน ⇒ หมุน $n$ รอบก็คือเอาระยะของหนึ่งรอบมาบวกกัน $n$ ครั้ง '
        'ซึ่งเขียนเป็นการคูณได้ว่า ระยะทางรวม $= n \\times 2\\pi r$',
        '• <b>วิธีคูณเมื่อมี $\\pi$ ติดอยู่</b> : ให้มอง $\\pi$ เป็นก้อนหนึ่งก้อนที่ยังไม่ต้องแทนค่า '
        'แล้วคูณเฉพาะตัวเลขที่อยู่ข้างหน้า เช่น $15 \\times 80\\pi = (15 \\times 80)\\pi = 1200\\pi$ '
        'ข้อดีคือคำตอบจะเป็นค่าที่แม่นยำ ไม่คลาดเคลื่อนจากการปัดเศษระหว่างทาง',
        '• <b>ค่าประมาณไว้ตรวจตอนท้าย</b> : $\\pi \\approx 3.14$ และหน่วยความยาว '
        '$100$ เซนติเมตร $= 1$ เมตร สองอย่างนี้ไม่ได้ใช้คำนวณคำตอบ '
        'แต่ใช้เปลี่ยนคำตอบให้เป็นระยะที่นึกภาพออก เพื่อดูว่าสมเหตุสมผลหรือไม่',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• ล้อเป็นรูปวงกลม มีรัศมียาว $40$ เซนติเมตร',
        '• ล้อกลิ้งไปบนพื้นราบในแนวเส้นตรง โดยไม่ลื่นไถล '
        '⇒ ขอบล้อสัมผัสพื้นแบบคลี่ออกทีละจุด ไม่มีการลื่นทิ้งช่วง',
        '• ล้อหมุนไปครบ $15$ รอบพอดี คำว่า “พอดี” บอกว่าเป็นจำนวนรอบเต็ม ไม่มีเศษของรอบเหลือค้าง',
        '• สังเกตหน้าตาก่อนลงมือ : ตัวเลข $40$ ที่โจทย์ให้มาเป็น<b>รัศมี</b> ⛔ ไม่ใช่เส้นผ่านศูนย์กลาง '
        'ด้วยเหตุนี้สูตรที่หยิบมาใช้ต้องเป็น $2\\pi r$ ถ้าเผลอใช้ $\\pi r$ จะได้ระยะเพียงครึ่งเดียวทันที',
        '• สังเกตอีกอย่าง : ค่าที่โจทย์ให้เลือกทุกค่ามี $\\pi$ ติดอยู่ '
        '⇒ ไม่ต้องแทน $\\pi \\approx 3.14$ เลยตลอดการคำนวณ ปล่อยให้ $\\pi$ ติดไปจนจบจะเร็วและแม่นกว่า',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาระยะทางที่ล้อเคลื่อนที่ไปได้ตลอดการกลิ้ง $15$ รอบ โดยตอบเป็นหน่วยเซนติเมตร',
        '',
        '<b>【 อ่านเงื่อนไข “ไม่ลื่นไถล” ให้กลายเป็นข้อเท็จจริงว่าหนึ่งรอบเท่ากับหนึ่งเส้นรอบวง '
        'แล้วคำนวณเส้นรอบวงจากรัศมีด้วยสูตร $2\\pi r$ จากนั้นคูณด้วยจำนวนรอบ 】</b>',
        '',
        '<b>ขั้นที่ 1 · เปลี่ยนเงื่อนไข “กลิ้งโดยไม่ลื่นไถล” ให้เป็นระยะทางของหนึ่งรอบ</b>',
        '• หลักการที่ใช้ : ระยะทางที่ล้อเคลื่อนที่ได้ต่อการหมุนหนึ่งรอบ $=$ เส้นรอบวงของล้อ',
        '• เหตุผลที่หลักการนี้เป็นจริง : เมื่อไม่มีการลื่นไถล จุดบนขอบล้อจะแตะพื้นเรียงกันไปทีละจุด '
        'จุดที่เพิ่งแตะพื้นจะอยู่ถัดจากจุดก่อนหน้าพอดี ไม่มีช่วงไหนที่ล้อไถลผ่านพื้นไปโดยขอบล้อไม่หมุนตาม '
        '⇒ ความยาวของรอยที่ล้อลากไว้บนพื้นเท่ากับความยาวของขอบล้อที่หมุนผ่านไป',
        '• หมุนครบหนึ่งรอบคือขอบล้อหมุนผ่านไปครบทั้งวง '
        '⇒ ความยาวของขอบล้อที่หมุนผ่านไปคือเส้นรอบวงทั้งเส้น '
        '⇒ ระยะทางของหนึ่งรอบ $=$ เส้นรอบวง',
        '• ⛔ ระวังตรงนี้ : ถ้าล้อลื่นไถล ระยะทางที่ได้จะ<b>น้อยกว่า</b>เส้นรอบวง '
        'เพราะล้อหมุนทิ้งเปล่าอยู่กับที่บางช่วง ⇒ ข้อความ “โดยไม่ลื่นไถล” ในโจทย์คือเงื่อนไขที่ตัดกรณีนี้ทิ้งไป '
        'ทำให้เราใช้ความเท่ากันข้างบนได้อย่างสบายใจ',
        '',
        '<b>ขั้นที่ 2 · คำนวณเส้นรอบวงของล้อจากรัศมีที่โจทย์ให้มา</b>',
        '• สูตรที่ใช้ : เส้นรอบวง $C = 2\\pi r$',
        '• ระบุตัวแปรให้ชัดก่อนแทนค่า : $r = 40$ เซนติเมตร คือรัศมีของล้อตามที่โจทย์ให้ '
        '· $C$ คือเส้นรอบวงที่ต้องการหา · $\\pi$ ปล่อยไว้เป็นสัญลักษณ์ ยังไม่แทนค่าตัวเลข',
        '• แทนค่า : $C = 2 \\times \\pi \\times 40$',
        '• ยุบ : จัดตัวเลขมาคูณกันก่อน $2 \\times 40 = 80$ ⇒ $C = 80\\pi$ เซนติเมตร',
        '• อ่านผลให้เข้าใจ : ขอบล้อทั้งวงถ้าคลี่ออกวางเป็นเส้นตรงจะยาว $80\\pi$ เซนติเมตร '
        'และตามขั้นที่ 1 นี่คือระยะทางที่ล้อเคลื่อนที่ได้ต่อการหมุนหนึ่งรอบ',
        '',
        '<b>ขั้นที่ 3 · คูณระยะของหนึ่งรอบด้วยจำนวนรอบ เพื่อได้ระยะทางรวม</b>',
        '• สูตรที่ใช้ : ระยะทางรวม $= n \\times C$ '
        'ซึ่งมาจากการที่ทุกรอบเคลื่อนที่ได้ระยะเท่ากัน จึงเอาระยะของหนึ่งรอบมาบวกกัน $n$ ครั้ง',
        '• ระบุตัวแปร : $n = 15$ รอบ ตามที่โจทย์ให้ · $C = 80\\pi$ เซนติเมตร จากขั้นที่ 2',
        '• แทนค่า : ระยะทางรวม $= 15 \\times 80\\pi$',
        '• ยุบ : คูณเฉพาะตัวเลขข้างหน้า $\\pi$ คือ $15 \\times 80 = 1200$ '
        '⇒ ระยะทางรวม $= 1200\\pi$ เซนติเมตร',
        '• อ่านหน่วยให้ถูก : รัศมีมีหน่วยเป็นเซนติเมตร ⇒ เส้นรอบวงก็เป็นเซนติเมตร '
        'ส่วนจำนวนรอบเป็นตัวเลขล้วนไม่มีหน่วย ⇒ ผลคูณจึงยังมีหน่วยเป็นเซนติเมตร '
        'ตรงกับหน่วยที่โจทย์ถามพอดี ✓',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · เดินใหม่ทั้งเส้นด้วยเส้นผ่านศูนย์กลางและสูตร $\\pi d$ '
        'แล้วปิดท้ายด้วยการประมาณค่าเป็นเมตรเพื่อดูความสมเหตุสมผล)</b>',
        '• เส้นทางข้างบนใช้สูตร $2\\pi r$ ซึ่งเดินจากรัศมีโดยตรง '
        'การตรวจรอบนี้จะไม่แตะสูตรนั้นเลย แต่จะเปลี่ยนไปคิดผ่านเส้นผ่านศูนย์กลางแทน '
        'ถ้าสองทางให้ค่าตรงกัน แปลว่าไม่ได้พลาดที่การหยิบสูตร',
        '• หาเส้นผ่านศูนย์กลางก่อน : $d = 2r = 2 \\times 40 = 80$ เซนติเมตร',
        '• ใช้สูตร $C = \\pi d$ ซึ่งมาจากนิยามของ $\\pi$ ตรง ๆ : $C = \\pi \\times 80 = 80\\pi$ เซนติเมตร '
        '✓ ตรงกับเส้นรอบวงที่ได้จาก $2\\pi r$ ในขั้นที่ 2 ทุกประการ',
        '• ระยะทางรวม $= 15 \\times 80\\pi = 1200\\pi$ เซนติเมตร ✓ ได้ค่าเดิม',
        '• 📌 ตรวจซ้ำอีกชั้นด้วยการประมาณค่า : แทน $\\pi \\approx 3.1416$ '
        'จะได้ $1200\\pi \\approx 1200 \\times 3.1416 = 3769.9$ ⇒ ราว $3770$ เซนติเมตร '
        'ซึ่งเท่ากับ $37.7$ เมตร โดยประมาณ',
        '• ตรวจความสมเหตุสมผลของตัวเลขนี้ : ล้อรัศมี $40$ เซนติเมตร คือล้อที่มีเส้นผ่านศูนย์กลาง '
        '$80$ เซนติเมตร ซึ่งใกล้เคียงกับขนาดล้อจักรยานคันหนึ่ง ล้อขนาดนี้หมุนหนึ่งรอบไปได้ราว '
        '$2.5$ เมตร ⇒ หมุน $15$ รอบก็ควรไปได้ราว $2.5 \\times 15 = 37.5$ เมตร '
        'ตรงกับ $37.7$ เมตรที่คำนวณได้ ⇒ คำตอบ <b>สมเหตุสมผล</b> ✓',
        '',
        '✅ <b>คำตอบ</b> ล้อรัศมี $40$ เซนติเมตร กลิ้งโดยไม่ลื่นไถลครบ $15$ รอบ '
        'เคลื่อนที่ไปได้ระยะทาง $1200\\pi$ เซนติเมตร → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• จำเป็นประโยคเดียวว่า “กลิ้งไม่ลื่นไถล : หนึ่งรอบ $=$ หนึ่งเส้นรอบวง” '
        'แล้วโจทย์ตระกูลนี้จะเหลือแค่การคูณ ไม่ว่าจะถามระยะทางจากจำนวนรอบ '
        'หรือย้อนกลับไปถามจำนวนรอบจากระยะทาง (กรณีหลังใช้การหารด้วยเส้นรอบวงแทน)',
        '• กันความจำสับสนระหว่าง $2\\pi r$ กับ $\\pi r^2$ ด้วยการดูหน่วย : '
        'เส้นรอบวงเป็นความยาว จึงต้องมี $r$ ยกกำลังหนึ่ง ได้หน่วยเป็นเซนติเมตร '
        'ส่วนพื้นที่ต้องมี $r$ ยกกำลังสอง ได้หน่วยเป็นตารางเซนติเมตร '
        '⇒ โจทย์ข้อนี้ถามระยะทางซึ่งเป็นความยาว จึงต้องหยิบสูตรที่มี $r$ กำลังหนึ่ง',
        '• เก็บ $\\pi$ ไว้เป็นสัญลักษณ์จนถึงบรรทัดสุดท้าย อย่าเพิ่งแทน $3.14$ ตั้งแต่ต้น '
        'เพราะค่าที่โจทย์ให้เลือกเขียนในรูปที่มี $\\pi$ อยู่แล้ว การแทนค่ากลางทางมีแต่จะเสียเวลา '
        'และเสี่ยงเทียบค่าผิดตอนปัดเศษ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ถ้าได้ค่า $80\\pi$ แปลว่าคำนวณเส้นรอบวงถูกแล้ว แต่หยุดอยู่แค่นั้น '
        'คือตอบระยะทางของการหมุน<b>เพียงรอบเดียว</b> ลืมคูณด้วยจำนวนรอบ $15$ ที่โจทย์ให้มา · '
        'ค่านี้ผิดแน่นอน พิสูจน์ด้วยการประมาณ : $80\\pi \\approx 251$ เซนติเมตร หรือราว $2.5$ เมตรเท่านั้น '
        'ล้อที่กลิ้งไปตั้ง $15$ รอบเป็นไปไม่ได้ที่จะเคลื่อนที่ได้แค่ระยะเท่ากับก้าวสามก้าว · '
        'สัญญาณเตือนคือเลข $15$ ในโจทย์ยังไม่ถูกใช้เลยแม้แต่ครั้งเดียว ⇒ แปลว่ายังทำไม่จบ',
        '• ถ้าได้ค่า $600\\pi$ แปลว่าจำสูตรเส้นรอบวงผิดเป็น $\\pi r$ '
        'ซึ่งเกิดจากการจำสูตร $\\pi d$ ได้ แต่เอารัศมีไปแทนที่ตำแหน่งของเส้นผ่านศูนย์กลาง '
        'จึงคิดเป็น $\\pi (40) \\times 15 = 600\\pi$ · '
        'ค่านี้ผิดเพราะ $\\pi r$ ไม่ใช่สูตรของสิ่งใดในวงกลมเลย ตัวอักษรใน $\\pi d$ ต้องเป็น '
        '<b>เส้นผ่านศูนย์กลาง</b> เท่านั้น และ $d = 2r$ ไม่ใช่ $r$ · '
        'ตรวจได้ทันทีว่าค่านี้เป็นครึ่งหนึ่งของคำตอบพอดี เพราะ $\\pi r$ เป็นครึ่งหนึ่งของ $2\\pi r$ '
        '⇒ $600\\pi$ คือระยะทางที่ล้อจะได้ถ้าหมุนเพียง $7.5$ รอบ ไม่ใช่ $15$ รอบ',
        '• ถ้าได้ค่า $2400\\pi$ แปลว่าแปลงรัศมีเป็นเส้นผ่านศูนย์กลาง $d = 2r = 80$ ถูกแล้ว '
        'แต่ยังหยิบสูตร $2\\pi$ มาคูณซ้ำอีกชั้น กลายเป็น $2\\pi d = 2\\pi (80) = 160\\pi$ '
        'แล้วคูณ $15$ ได้ $2400\\pi$ · ค่านี้ผิดเพราะนับเลข $2$ ซ้ำสองครั้ง : '
        'หนึ่งครั้งตอนเปลี่ยน $r$ เป็น $d$ และอีกครั้งในสูตร ⇒ $2\\pi d = 2\\pi (2r) = 4\\pi r$ '
        'ซึ่งเป็นสองเท่าของเส้นรอบวงจริง · ผลคือ $2400\\pi \\approx 7540$ เซนติเมตร หรือราว '
        '$75.4$ เมตร ซึ่งเป็นสองเท่าพอดีของ $37.7$ เมตร ⇒ ขัดกับการประมาณว่าล้อจักรยานหมุน '
        '$15$ รอบไปได้ราว $37$ เมตร',
        '• อีกเส้นทางที่พลาดกันบ่อยคือคำนวณถูกหมดแต่ตอบผิดหน่วย '
        'คือแปลงเป็น $37.7$ เมตรแล้วตอบตัวเลขนั้นไป ทั้งที่โจทย์ถามเป็นเซนติเมตร · '
        'ให้กลับไปอ่านคำถามบรรทัดสุดท้ายเสมอก่อนวงคำตอบว่าโจทย์ขอหน่วยอะไร '
        'ที่นี่โจทย์ให้รัศมีมาเป็นเซนติเมตรและถามระยะทางเป็นเซนติเมตร '
        'จึงไม่ต้องแปลงหน่วยเลยแม้แต่ครั้งเดียว การแปลงเป็นเมตรมีไว้ใช้ตรวจความสมเหตุสมผลเท่านั้น',
    ],
    'V.mold: G = a circular wheel of radius 40 centimetres that rolls along flat ground in a straight '
    'line without slipping, handed over together with the exact count of 15 complete revolutions / '
    'A = the distance in centimetres that the wheel travels / M = read the no-slip clause as the '
    'statement that one revolution advances the wheel by exactly one circumference, compute that '
    'circumference from the radius as 2*pi*40 = 80*pi, then multiply by the revolution count to reach '
    '15*80*pi = 1200*pi. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 with the total at 2 or below, T at most 1 and C exactly 0 '
    '-> level: ง่าย. '
    'F = 1 because a single formula carries the whole item, the circumference 2*pi*r; the no-slip '
    'sentence is a modelling remark rather than a second formula, since it only tells the solver that '
    'the distance per turn is that same circumference. C = 0 because nothing has to be joined to '
    'anything: no second result is manufactured and then fed into a later relation, the one formula is '
    'evaluated and the outcome is scaled. P = 1 because the arithmetic is two multiplications, 2 times '
    '40 and 15 times 80, with pi carried along untouched as a symbol, so there is no intermediate '
    'quantity to store and no algebra to rearrange. T = 0 because the statement hides nothing: it names '
    'the radius as a radius, says the ground is flat and the path is straight, says the rolling happens '
    'without slipping, and says the 15 turns are complete ones, so every condition needed is stated '
    'outright and none has to be inferred or discarded. L = 0 because although a wheel is named, the '
    'scene needs no figure and no configuration to reconstruct; the single clause about not slipping '
    'maps onto the substitution immediately, which is the same standing as a purely symbolic item. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): 15*2*pi*40 evaluates to 1200*pi exactly, so the key is machine-confirmed '
    'rather than asserted. Every wrong value was machine-computed from a named error path instead of '
    'being invented near the answer: 2*pi*40 returns 80*pi for the solver who computes one turn and '
    'forgets the count, pi*40*15 returns 600*pi for the solver who misremembers the circumference as '
    'pi*r by putting the radius into the slot that belongs to the diameter, and 2*pi*80*15 returns '
    '2400*pi for the solver who converts the radius to the diameter 80 correctly but then applies the '
    'factor 2 a second time inside the formula, which is 2*pi*d = 4*pi*r, exactly twice the true '
    'circumference. The independent check was verified as well: with d = 2*40 = 80 the product pi*d '
    'returns 80*pi, matching 2*pi*r, and the numeric evaluation of 1200*pi is about 3769.91 '
    'centimetres, that is about 37.7 metres, against the sanity estimate of 15 turns of a wheel whose '
    'one-turn advance is about 2.51 metres. The ordering check confirms that 80*pi < 600*pi < 1200*pi '
    '< 2400*pi. '
    'Collision sweep on 6586 items (bank 6442 files + k1 out + k2 out), probe rerun for this item over '
    'the same corpus: the Thai word for rolling returns 0 items across the whole corpus, and the Thai '
    'phrase for without slipping also returns 0 items, so no bank item states a rolling-contact '
    'condition at all. Only six items mention a wheel once the false positives from the unrelated Thai '
    'word for consistent-with are removed, and none of them is this mold. The nearest relative is '
    'gen-chap-07-trigonometry-q066, two pulleys on parallel axles linked by one belt that neither slips '
    'nor stretches, which asks for the revolutions per minute of the larger pulley; it shares only the '
    'idea of contact without slipping, while its G is a linked pair of wheels with a transmitted rate, '
    'its A is a rate rather than a length, and its M equates the rim speeds of two circles, so it '
    'shares none of the three labels with this item. The other candidate, chap-13-calculus-q108, names '
    'a rotating wheel but hands over an angle as a function of time and asks for angular velocity and '
    'angular acceleration by differentiation, which is a calculus mold. The pair formed by a revolution '
    'count together with a circumference returns 17 items, all of which turn out to be about points '
    'travelling along a circle in the unit-circle sense rather than a circle rolling along a line. '
    'Choices are ordered ascending by the coefficient of pi (80, then 600, then 1200, then 2400), so '
    'the answer slot is forced by that rule and was not chosen.',
)

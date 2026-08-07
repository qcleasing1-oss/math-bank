# -*- coding: utf-8 -*-
add(
    152,
    ['7.11'],
    'ปานกลาง',
    'ใบปัดน้ำฝนของรถยนต์คันหนึ่งติดอยู่กับแขนปัดซึ่งหมุนรอบจุดหมุนคงที่จุดหนึ่ง '
    'ยางปัดน้ำเป็นส่วนของแขนปัดที่อยู่ห่างจากจุดหมุนตั้งแต่ $18$ เซนติเมตร ถึง $48$ เซนติเมตร '
    'เมื่อแขนปัดกวาดจากตำแหน่งหนึ่งไปยังอีกตำแหน่งหนึ่งบนกระจกซึ่งเป็นระนาบราบ '
    'แขนปัดกวาดมุมที่จุดหมุนได้ $120^\\circ$ '
    'พื้นที่ของบริเวณบนกระจกที่ยางปัดน้ำกวาดผ่านเท่ากับกี่ตารางเซนติเมตร',
    [
        '$108\\pi$',
        '$300\\pi$',
        '$660\\pi$',
        '$768\\pi$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• <b>เซกเตอร์</b> คือชิ้นของวงกลมที่ถูกเฉือนออกมาด้วยรัศมีสองเส้น '
        'ถ้ารัศมียาว $r$ หน่วย และมุมที่จุดศูนย์กลางมีขนาด $\\theta$ เรเดียน '
        'พื้นที่ของเซกเตอร์คือ $\\dfrac{1}{2}r^2\\theta$ · ที่มาของสูตรคิดเป็นสัดส่วนได้ตรง ๆ : '
        'วงกลมทั้งวงกินมุม $2\\pi$ เรเดียน และมีพื้นที่ $\\pi r^2$ '
        'เซกเตอร์ที่กินมุมเพียง $\\theta$ จึงได้พื้นที่เป็นเศษส่วน $\\dfrac{\\theta}{2\\pi}$ ของทั้งวง '
        'นั่นคือ $\\dfrac{\\theta}{2\\pi}\\times\\pi r^2 = \\dfrac{1}{2}r^2\\theta$ · '
        '⛔ สูตรนี้ใช้ได้ก็ต่อเมื่อมุมอยู่ในหน่วยเรเดียนแล้วเท่านั้น ถ้าโจทย์ให้มาเป็นองศาต้องแปลงก่อนเสมอ',
        '• การแปลงองศาเป็นเรเดียน : ครึ่งรอบของวงกลมคือ $180^{\\circ}$ และก็คือ $\\pi$ เรเดียนด้วย '
        '⇒ $1^{\\circ} = \\dfrac{\\pi}{180}$ เรเดียน ⇒ เอาจำนวนองศาคูณด้วย $\\dfrac{\\pi}{180}$ '
        'ก็ได้ขนาดของมุมในหน่วยเรเดียน · ตรวจผลได้ง่าย ๆ ด้วยการเทียบกับหมุดที่จำง่าย เช่น '
        '$90^{\\circ} = \\dfrac{\\pi}{2}$ และ $180^{\\circ} = \\pi$',
        '• <b>เซกเตอร์วงแหวน</b> คือบริเวณที่อยู่ระหว่างส่วนโค้งสองเส้นซึ่งมีจุดศูนย์กลางร่วมกัน '
        'และถูกขนาบด้วยรัศมีคู่เดียวกัน · หน้าตาเหมือนเซกเตอร์ที่ถูกเจาะรูออกตรงกลาง '
        'ถ้ารัศมีวงนอกยาว $R$ รัศมีวงในยาว $r$ และทั้งคู่กินมุมเดียวกันคือ $\\theta$ เรเดียน '
        'พื้นที่หาได้ด้วยการเอาเซกเตอร์ใหญ่ตั้งแล้วหักเซกเตอร์เล็กทิ้ง : '
        '$\\dfrac{1}{2}R^2\\theta - \\dfrac{1}{2}r^2\\theta = \\dfrac{1}{2}\\theta\\left(R^2 - r^2\\right)$ '
        '· การดึง $\\dfrac{1}{2}\\theta$ ออกมาเป็นตัวประกอบร่วมทำได้เพราะเซกเตอร์ทั้งสองใช้มุมเดียวกันเป๊ะ ๆ',
        '• ⭐ <b>ผลต่างของกำลังสอง กับ กำลังสองของผลต่าง เป็นคนละจำนวนกัน</b> '
        'สูตรเซกเตอร์วงแหวนต้องการ $R^2 - r^2$ ซึ่งแยกตัวประกอบได้เป็น $(R-r)(R+r)$ '
        '⛔ ไม่ใช่ $(R-r)^2$ · เช็คด้วยตัวเลขชุดที่ข้อนี้ใช้ก็เห็นทันที : '
        '$48^2 - 18^2 = 2304 - 324 = 1980$ ในขณะที่ $(48-18)^2 = 30^2 = 900$ '
        'ซึ่งห่างกันเกินสองเท่า ⇒ เผลอสลับเมื่อไรคำตอบเพี้ยนทันที',
        '• การอ่านสถานการณ์ให้ตรงกับรูปทรง : บริเวณที่ถูกเช็ดคือบริเวณที่มี<b>ตัวยาง</b>พาดผ่านจริง ๆ '
        'ไม่ใช่ทุกที่ที่แขนกวาดไปถึง · ถ้าตัวกวาดเริ่มต้นห่างจากจุดหมุนออกไประยะหนึ่ง '
        'บริเวณใกล้จุดหมุนจะไม่มีอะไรไปแตะเลย ⇒ ต้องเจาะรูตรงกลางทิ้งเสมอ',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• ยางปัดน้ำเป็นส่วนของแขนปัดที่อยู่ห่างจากจุดหมุนตั้งแต่ $18$ เซนติเมตร ถึง $48$ เซนติเมตร '
        '⇒ ระยะไกลสุดของยางคือ $R = 48$ และระยะใกล้สุดของยางคือ $r = 18$',
        '• แขนปัดหมุนรอบจุดหมุนคงที่จุดเดียว และกวาดมุมที่จุดหมุนได้ $120^{\\circ}$',
        '• กระจกเป็นระนาบราบ ⇒ บริเวณที่ถูกเช็ดเป็นรูปแบนบนระนาบเดียว คิดพื้นที่ได้ตรง ๆ '
        'โดยไม่ต้องคิดเรื่องความโค้งของผิวใด ๆ เลย',
        '• สังเกตหน้าตาก่อนลงมือ : ยางไม่ได้เริ่มต้นที่จุดหมุน แต่เริ่มที่ระยะ $18$ เซนติเมตร '
        '⇒ บริเวณที่กวาดผ่านมี “รู” อยู่ตรงกลาง จึงเป็น<b>เซกเตอร์วงแหวน</b> '
        '⛔ ไม่ใช่เซกเตอร์เต็มรูปที่พุ่งจากจุดหมุนออกไปถึง $48$',
        '• สังเกตอีกอย่าง : ค่าที่มีให้เลือกทุกค่าติด $\\pi$ ทั้งหมด ⇒ คำตอบอยู่ในรูปจำนวนคูณ $\\pi$ '
        '⇒ เก็บ $\\pi$ ไว้เป็นสัญลักษณ์ตลอดทาง ⛔ ไม่ต้องแทน $\\pi$ ด้วย $3.14$ ให้เสียเวลาและเสียความแม่น',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาพื้นที่ของบริเวณบนกระจกที่ยางปัดน้ำกวาดผ่าน ในหน่วยตารางเซนติเมตร '
        'นั่นคือหาพื้นที่ของเซกเตอร์วงแหวนที่มีรัศมีวงนอก $48$ รัศมีวงใน $18$ และมุมที่จุดหมุน $120^{\\circ}$',
        '',
        '<b>【 ระบุก่อนว่าบริเวณที่กวาดผ่านเป็นเซกเตอร์วงแหวน แล้วแปลง $120^{\\circ}$ เป็น '
        '$\\dfrac{2\\pi}{3}$ เรเดียน จากนั้นใช้ $\\dfrac{1}{2}\\theta\\left(R^2-r^2\\right)$ '
        'ซึ่งคือเซกเตอร์รัศมี $48$ หักด้วยเซกเตอร์รัศมี $18$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · ระบุรูปทรงของบริเวณที่ยางกวาดผ่านให้ถูกก่อนลงมือคำนวณ</b>',
        '• จุดใดบนกระจกจะถูกเช็ด ก็ต่อเมื่อมีจุดบนตัวยางพาดผ่านจุดนั้น '
        '⇒ ต้องดูว่าตัวยางกินระยะจากจุดหมุนช่วงใดบ้าง',
        '• จุดบนตัวยางอยู่ห่างจากจุดหมุนเป็นระยะ $d$ เซนติเมตร โดย $18 \\le d \\le 48$ ตามที่โจทย์บอก',
        '• เมื่อแขนหมุนไป จุดที่ระยะ $d$ จะลากรอยเป็นส่วนโค้งของวงกลมรัศมี $d$ ที่กินมุม $120^{\\circ}$ '
        '⇒ พอรวมทุกค่าของ $d$ ตั้งแต่ $18$ ถึง $48$ เข้าด้วยกัน จะได้บริเวณที่อยู่ระหว่างส่วนโค้งรัศมี $18$ '
        'กับส่วนโค้งรัศมี $48$ ซึ่งก็คือเซกเตอร์วงแหวนพอดี',
        '• ⛔ <b>จุดพลิกของข้อนี้อยู่ตรงนี้</b> : จุดที่อยู่ห่างจากจุดหมุนน้อยกว่า $18$ เซนติเมตร '
        'ไม่มีส่วนใดของตัวยางไปถึงเลยแม้แต่จุดเดียว เพราะช่วงที่เป็นยางเริ่มต้นที่ $18$ พอดี '
        '⇒ พื้นที่ส่วนนั้นต้องถูกหักออก ไม่นับรวมเป็นบริเวณที่กวาดผ่าน',
        '',
        '<b>ขั้นที่ 2 · แปลงมุมที่กวาดจากองศาเป็นเรเดียน</b>',
        '• สูตรที่ใช้ : มุมในหน่วยเรเดียน $=$ จำนวนองศา $\\times\\ \\dfrac{\\pi}{180}$',
        '• ระบุตัวแปร : จำนวนองศาที่แขนกวาดได้คือ $120$',
        '• แทนค่า : $\\theta = 120 \\times \\dfrac{\\pi}{180} = \\dfrac{120\\pi}{180}$',
        '• ยุบ : $120$ กับ $180$ มีตัวหารร่วมมากเป็น $60$ ⇒ '
        '$\\dfrac{120\\pi}{180} = \\dfrac{2\\pi}{3}$',
        '• ⇒ $\\theta = \\dfrac{2\\pi}{3}$ เรเดียน · ตรวจความสมเหตุสมผลอย่างเร็ว : '
        '$\\dfrac{2\\pi}{3}$ อยู่ระหว่าง $\\dfrac{\\pi}{2}$ กับ $\\pi$ ซึ่งตรงกับข้อเท็จจริงที่ว่า '
        '$120^{\\circ}$ อยู่ระหว่าง $90^{\\circ}$ กับ $180^{\\circ}$ ✓',
        '',
        '<b>ขั้นที่ 3 · เขียนพื้นที่ให้เป็นผลต่างของเซกเตอร์สองรูป แล้วดึงตัวประกอบร่วม</b>',
        '• สูตรที่ใช้ : พื้นที่ที่ต้องการ $=$ พื้นที่เซกเตอร์รัศมี $R$ $-$ พื้นที่เซกเตอร์รัศมี $r$ '
        '$= \\dfrac{1}{2}R^2\\theta - \\dfrac{1}{2}r^2\\theta$',
        '• ระบุตัวแปร : $R = 48$ คือระยะไกลสุดของยาง · $r = 18$ คือระยะใกล้สุดของยาง · '
        '$\\theta = \\dfrac{2\\pi}{3}$ คือมุมที่กวาดได้ ซึ่งใช้ร่วมกันทั้งสองเซกเตอร์ '
        'เพราะแขนอันเดียวกันหมุนไปพร้อมกันทั้งเส้น',
        '• ดึงตัวประกอบร่วม : ทั้งสองพจน์มี $\\dfrac{1}{2}\\theta$ เหมือนกัน '
        '⇒ $\\dfrac{1}{2}R^2\\theta - \\dfrac{1}{2}r^2\\theta = \\dfrac{1}{2}\\theta\\left(R^2 - r^2\\right)$',
        '• ⭐ อ่านสูตรนี้ให้ขึ้นใจว่าในวงเล็บคือ $R^2 - r^2$ ซึ่งเป็น<b>ผลต่างของกำลังสอง</b> '
        '⛔ ไม่ใช่ $(R-r)^2$ ซึ่งเป็นกำลังสองของผลต่าง · '
        'เหตุผลคือแต่ละเซกเตอร์ถูกยกกำลังสองด้วยรัศมีของตัวเองก่อน แล้วจึงค่อยนำมาลบกัน',
        '',
        '<b>ขั้นที่ 4 · แทนตัวเลขแล้วยุบทีละก้าว</b>',
        '• แทนค่า : พื้นที่ $= \\dfrac{1}{2}\\left(\\dfrac{2\\pi}{3}\\right)\\left(48^2 - 18^2\\right)$',
        '• ยุบสัมประสิทธิ์หน้าก่อน : $\\dfrac{1}{2}\\times\\dfrac{2\\pi}{3} = \\dfrac{2\\pi}{6} '
        '= \\dfrac{\\pi}{3}$',
        '• ยุบในวงเล็บ : $48^2 = 2304$ และ $18^2 = 324$ ⇒ $2304 - 324 = 1980$',
        '• คูณสองก้อนเข้าด้วยกัน : พื้นที่ $= \\dfrac{\\pi}{3}\\times 1980 = \\dfrac{1980\\pi}{3} = 660\\pi$ '
        'เพราะ $1980 \\div 3 = 660$',
        '• ⇒ พื้นที่ของบริเวณที่ยางปัดน้ำกวาดผ่านคือ $660\\pi$ ตารางเซนติเมตร '
        '· เก็บไว้ในรูปที่ติด $\\pi$ ตามหน้าตาของค่าที่มีให้เลือก ⛔ ไม่ต้องกดเป็นทศนิยม',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · คิดพื้นที่ของเซกเตอร์วงนอกและเซกเตอร์วงในออกมาเป็นตัวเลขคนละก้อน '
        'แล้วค่อยลบกันตอนท้าย ปิดท้ายด้วยด่านขอบเขตและการแยกตัวประกอบผลต่างกำลังสอง)</b>',
        '• เส้นทางข้างบนยุบสูตรให้เหลือ $\\dfrac{1}{2}\\theta\\left(R^2-r^2\\right)$ '
        'ตั้งแต่ก่อนแทนตัวเลข การตรวจรอบนี้จะไม่ยุบสูตรอะไรเลย '
        'แต่จะกดพื้นที่ของเซกเตอร์ทั้งสองรูปออกมาเป็นตัวเลขแยกกันคนละก้อน แล้วจึงลบกันเป็นก้าวสุดท้าย',
        '• เซกเตอร์วงนอก รัศมี $48$ : $\\dfrac{1}{2}\\left(\\dfrac{2\\pi}{3}\\right)(48)^2 '
        '= \\dfrac{\\pi}{3}\\times 2304 = 768\\pi$ ตารางเซนติเมตร',
        '• เซกเตอร์วงใน รัศมี $18$ : $\\dfrac{1}{2}\\left(\\dfrac{2\\pi}{3}\\right)(18)^2 '
        '= \\dfrac{\\pi}{3}\\times 324 = 108\\pi$ ตารางเซนติเมตร',
        '• ลบกัน : $768\\pi - 108\\pi = 660\\pi$ ✓ ตรงกับผลของเส้นทางแรกทุกตัวอักษร '
        'ทั้งที่สองเส้นทางนี้ไม่ได้ใช้ก้าวใดร่วมกันเลย',
        '• 📌 <b>ด่านเชิงขอบเขตที่ใช้กรองได้ทันทีโดยไม่ต้องคำนวณ</b> : '
        'บริเวณที่ยางกวาดผ่านเป็นเพียงส่วนหนึ่งของเซกเตอร์รัศมี $48$ เต็มรูป '
        '⇒ คำตอบต้อง<b>น้อยกว่า</b> $768\\pi$ อย่างแน่นอน ⇒ ค่าที่ไม่น้อยกว่า $768\\pi$ ตกรอบทันที · '
        'และวงแหวนที่กว้างถึง $30$ เซนติเมตรและอยู่ไกลจากจุดหมุน ย่อมกินพื้นที่<b>มากกว่า</b>รูตรงกลาง '
        'ซึ่งมีพื้นที่เพียง $108\\pi$ อยู่มาก ⇒ ค่าที่เล็กใกล้ ๆ $108\\pi$ ตกรอบเช่นกัน',
        '• 📌 <b>ด่านแยกตัวประกอบ</b> ใช้ยืนยันเลข $1980$ ว่าไม่ได้มาจากการกดเครื่องผิด : '
        '$48^2 - 18^2 = (48-18)(48+18) = 30 \\times 66 = 1980$ ✓ ตรงกับ $2304 - 324$ พอดี · '
        'ที่สำคัญคือรูปแยกตัวประกอบนี้ทำให้เห็นชัดว่าคำตอบผูกกับ $(48-18)(48+18)$ '
        '⛔ ไม่ใช่ $(48-18)^2 = 900$ เพราะตัวประกอบตัวที่สองคือ<b>ผลบวก</b> $66$ ไม่ใช่ผลต่าง $30$',
        '',
        '✅ <b>คำตอบ</b> พื้นที่ของบริเวณบนกระจกที่ยางปัดน้ำกวาดผ่านเท่ากับ $660\\pi$ ตารางเซนติเมตร '
        '→ <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• จำสูตรเซกเตอร์วงแหวนเป็นก้อนเดียวไปเลยว่า $\\dfrac{1}{2}\\theta\\left(R^2 - r^2\\right)$ '
        'แล้วอ่านออกเสียงในใจว่า “ครึ่งหนึ่งของมุม คูณ ผลต่างของกำลังสองของรัศมี” '
        'การท่องคำว่า “ผลต่างของกำลังสอง” ติดมากับสูตร จะกันความผิดพลาดที่พบบ่อยที่สุดของโจทย์แนวนี้ได้ทั้งหมด',
        '• เจอโจทย์ของจริงที่ตัวกวาดหรือตัวเช็ด<b>ไม่ได้</b>เริ่มต้นจากจุดหมุน ให้วาดรูตรงกลางทิ้งไว้ก่อนเสมอ '
        'แล้วค่อยอ่านตัวเลขสองตัวว่าตัวไหนเป็นรัศมีวงใน ตัวไหนเป็นรัศมีวงนอก '
        '· โจทย์แนวนี้มักให้ระยะมาเป็นช่วง เช่น “ตั้งแต่ … ถึง …” ซึ่งเป็นสัญญาณของรูตรงกลางโดยตรง',
        '• อ่านหน้าตาของค่าที่มีให้เลือกก่อนลงมือคำนวณ : ที่นี่ทุกค่าติด $\\pi$ '
        '⇒ รู้ทันทีว่าไม่ต้องแทนค่าประมาณของ $\\pi$ เลย และรู้ด้วยว่าคำตอบไม่มีทางมีกรณฑ์โผล่มา '
        '⇒ ถ้าคำนวณแล้วได้อะไรที่ติด $\\sqrt{3}$ แปลว่าเดินผิดทางตั้งแต่ต้น',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $108\\pi$ เพราะหยิบ $18$ มาเป็นรัศมีเพียงค่าเดียว '
        '⇒ $\\dfrac{1}{2}\\left(\\dfrac{2\\pi}{3}\\right)(18)^2 = 108\\pi$ · '
        'ค่านี้ผิดเพราะมันคือพื้นที่ของเซกเตอร์วงในล้วน ๆ ซึ่งเป็นบริเวณที่อยู่ห่างจากจุดหมุน<b>ไม่ถึง</b> $18$ '
        'เซนติเมตร ⇒ เป็นบริเวณที่ไม่มีส่วนใดของตัวยางไปแตะเลยแม้แต่จุดเดียว '
        'จึงเป็นการตอบพื้นที่ของสิ่งที่ตรงข้ามกับที่โจทย์ถามพอดี · '
        'ตรวจจับได้ในหนึ่งวินาทีด้วยการเทียบขนาด : ยางยาว $48-18 = 30$ เซนติเมตร '
        'ซึ่งยาวกว่าช่วงที่ยางเข้าไม่ถึงเสียอีก แต่ $108\\pi$ กลับเล็กกว่า $768\\pi$ ถึงเจ็ดเท่า '
        '⇒ เล็กเกินจริงอย่างเห็นได้ชัด',
        '• ได้ค่า $300\\pi$ เพราะเอาความยาวของตัวยาง $48 - 18 = 30$ ไปใช้เป็นรัศมีของเซกเตอร์ '
        '⇒ $\\dfrac{1}{2}\\left(\\dfrac{2\\pi}{3}\\right)(30)^2 = \\dfrac{\\pi}{3}\\times 900 = 300\\pi$ · '
        'นี่คือการยกกำลังสองของผลต่าง ทั้งที่สูตรต้องการผลต่างของกำลังสอง · '
        'พิสูจน์ว่าผิดด้วยตัวเลขได้ทันที : $48^2 - 18^2 = 1980$ แต่ $(48-18)^2 = 900$ '
        'ต่างกันถึง $1080$ ซึ่งไม่ใช่ความคลาดเคลื่อนเล็ก ๆ · '
        'พิสูจน์เชิงรูปทรงได้อีกทาง : $30$ คือ<b>ความกว้าง</b>ของวงแหวน ไม่ใช่ระยะจากจุดหมุนถึงขอบใด ๆ เลย '
        'จึงไม่มีเซกเตอร์รูปใดในสถานการณ์นี้ที่มีรัศมี $30$ · '
        'อีกทั้งวงแหวนที่กว้าง $30$ แต่วางอยู่ไกลจากจุดหมุน ย่อมกินพื้นที่มากกว่าเซกเตอร์รัศมี $30$ '
        'ที่เกาะอยู่ติดจุดหมุนเสมอ',
        '• ได้ค่า $768\\pi$ เพราะคิดเป็นเซกเตอร์รัศมี $48$ เต็มรูป โดยลืมหักวงในทิ้ง '
        '⇒ $\\dfrac{1}{2}\\left(\\dfrac{2\\pi}{3}\\right)(48)^2 = 768\\pi$ · '
        'ค่านี้ผิดเพราะไปนับพื้นที่ช่วงที่อยู่ห่างจากจุดหมุนไม่ถึง $18$ เซนติเมตรเข้ามาด้วย '
        'ทั้งที่ช่วงนั้นเป็นแขนเปล่าไม่มียาง · ตรวจได้เป๊ะ ๆ ด้วยการลบ : '
        '$768\\pi - 660\\pi = 108\\pi$ ซึ่งเท่ากับพื้นที่ของเซกเตอร์รัศมี $18$ พอดี '
        '⇒ ยืนยันว่านับเกินไปเท่ากับรูตรงกลางเป๊ะทุกตารางเซนติเมตร · '
        'สัญญาณเตือนอีกอย่างคือเส้นทางนี้ไม่ได้ใช้เลข $18$ ที่โจทย์ให้มาเลยสักครั้ง',
        '• อีกเส้นทางที่พลาดกันบ่อยคือลืมตัวประกอบ $\\dfrac{1}{2}$ ในสูตรพื้นที่เซกเตอร์ '
        '⇒ ไปคิดเป็น $\\theta\\left(R^2 - r^2\\right) = \\dfrac{2\\pi}{3}\\times 1980 = 1320\\pi$ · '
        'ค่านี้ใหญ่กว่าเซกเตอร์รัศมี $48$ เต็มรูปซึ่งมีพื้นที่ $768\\pi$ เสียอีก '
        'ทั้งที่บริเวณที่ถามเป็นแค่ส่วนหนึ่งของเซกเตอร์รูปนั้น ⇒ เป็นไปไม่ได้โดยสิ้นเชิง · '
        'วิธีกันคือเขียนเลข $\\dfrac{1}{2}$ ลงไปพร้อมกับสูตรทุกครั้งที่ลงมือ '
        'และตรวจปลายทางด้วยด่านขอบเขตว่าคำตอบต้องน้อยกว่าเซกเตอร์วงนอกเต็มรูปเสมอ',
    ],
    'V.mold: G = a windscreen wiper mounted on an arm that turns about one fixed pivot, where the rubber '
    'occupies only the part of the arm lying between 18 cm and 48 cm from that pivot, together with the '
    '120 degree angle the arm sweeps across a flat sheet of glass / A = the area of the region on the '
    'glass that the rubber itself passes over, in square centimetres / M = read the swept region as an '
    'annular sector rather than a full sector because the rubber does not begin at the pivot, convert '
    '120 degrees to 2*pi/3 radians, and evaluate one sector of radius 48 with the sector of radius 18 '
    'removed, that is (1/2)*theta*(R**2 - r**2). '
    'Rubric F2 C1 P1 T1 L1 = 6/15, inside the 3 to 7 band with T no higher than 2 and the total below 8, '
    '-> level: ปานกลาง. F = 2 because two formulas must be held at once, the degree to radian conversion '
    'and the sector area, and the annular form is the first one applied to a difference of two radii '
    'rather than to a single radius. C = 1 because subtopic 7.11 has to be joined to the elementary '
    'algebraic identity for a difference of squares, a real but shallow crossing since the factorisation '
    'is only used as a check and the arithmetic goes through either way. P = 1 because once the shape is '
    'named the computation is short, one conversion, two squares, one subtraction and one multiplication, '
    'with no branching and no case work. T = 1 for the single turning point, that the region has a hole '
    'in the middle because the rubber starts 18 cm out from the pivot; T was held at 1 and not raised to '
    '2 because the statement says outright that the rubber runs from 18 cm to 48 cm, so the inner radius '
    'is handed over as a number and nothing has to be inferred about where the rubber begins. L = 1 '
    'because the item carries a real world scene that the solver must translate into a plane figure, but '
    'the scene stays inside one plane and the glass is stated to be flat, so it never reaches the two of '
    'a three dimensional set-up. The total of 6 fails the ยาก threshold of 8, and C = 1 with T = 1 fails '
    'both of the alternative gates for that level as well. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): with R = 48, r = 18 and theta = 2*pi/3, Rational(1,2)*theta*(R**2 - r**2) '
    'simplifies to 660*pi, float value 2073.45115136926, so the key at index 2 is exact; the same run '
    'confirms 48**2 - 18**2 = 1980 and its factorisation (48-18)*(48+18) = 30*66 = 1980, while '
    '(48-18)**2 = 900, so the two readings really are different numbers. Every wrong value was '
    'machine-computed from a named error path instead of being invented: '
    'Rational(1,2)*theta*18**2 = 108*pi, about 339.29, for taking 18 as the only radius and so measuring '
    'the inner sector the rubber never touches; Rational(1,2)*theta*(48-18)**2 = 300*pi, about 942.48, '
    'for squaring the difference of the radii instead of differencing their squares; and '
    'Rational(1,2)*theta*48**2 = 768*pi, about 2412.74, for treating the region as the full sector of '
    'radius 48 and forgetting to remove the inner one. The unlisted fourth path, dropping the factor 1/2, '
    'was evaluated too: theta*(48**2 - 18**2) = 1320*pi, about 4146.90, which exceeds the whole outer '
    'sector and matches nothing on offer. The bounding argument used in the independent check was '
    'verified numerically as well, 339.29 < 2073.45 < 2412.74, so the answer sits strictly between the '
    'inner sector and the outer sector, and the two sectors computed separately, 768*pi - 108*pi, return '
    '660*pi along a path the main solution never walks. '
    'Collision sweep on 6457 items (bank 63 files + k1 out + k2 out, that is the 6437 quoted in the '
    'batch-20 notes plus the 20 items of batch 20 that have since landed in k2 out), probes run over the '
    'question text only: the Thai word for windscreen wiper returns 0 items across the whole corpus, and '
    'the words for wiper arm and wiper blade return 0 items as well, so the scene itself is new. The word '
    'for annulus returns exactly 1 item, chap-12-probability-q28, which colours a ring of eight cells and '
    'is a counting problem with no geometry of area in it at all. The verb meaning to sweep returns 4 '
    'items, of which 3 are false positives where the string sits inside the Thai word for a piece of '
    'candy in chapter 12, and the only real one is gen-chap-07-trigonometry-q033, a pendulum on a 45 cm '
    'rod sweeping 24 degrees, which asks for an arc length from a single radius and shares neither A nor '
    'M; that item also uses a saturated background this one deliberately avoids. The nearest neighbour in '
    'the whole corpus is gen-chap-07-trigonometry-q032, two concentric circles of radii 5 and 8 with a '
    'symbolic angle theta, which hands the solver the annular sector area 39*pi/4 and asks by how much '
    'the outer arc exceeds the inner arc: it runs in the opposite direction, from area back to an arc '
    'difference, its A is a length rather than an area, and it carries no scene at all, so it is a watch '
    'and not a clash. The pair formed by a sector together with a difference of areas returns 0 items, '
    'and the pair formed by a sector together with 120 degrees returns exactly 1 item, '
    'gen-chap-07-trigonometry-q094, which rolls a sector of paper into a cone and asks for a volume. '
    'Inside batch 21 the closest item is q151, which also ends up subtracting two sector areas, but there '
    'the radius grows while the angle is held fixed and the angle itself has to be recovered from an arc '
    'increment first, so its G and its M are both different and its answer carries no pi. Choices are '
    'ordered ascending by numeric value, 108, 300, 660 and 768 in units of pi, so the answer slot is '
    'forced by that rule and was not chosen.',
)

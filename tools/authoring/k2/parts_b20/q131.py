# -*- coding: utf-8 -*-
add(
    131,
    ['7.11'],
    'ปานกลาง',
    'เซกเตอร์ของวงกลมรูปหนึ่งมีรัศมียาว $6$ หน่วย และมีมุมที่จุดศูนย์กลางขนาด '
    '$\\dfrac{2\\pi}{3}$ เรเดียน '
    'เมื่อลากคอร์ดเชื่อมจุดปลายทั้งสองของส่วนโค้งของเซกเตอร์รูปนี้ '
    'จะได้รูปสามเหลี่ยมซึ่งมีรัศมีทั้งสองเส้นและคอร์ดเส้นนั้นเป็นด้านทั้งสามด้าน '
    'พื้นที่ของเซกเตอร์รูปนี้เป็นกี่เท่าของพื้นที่ของรูปสามเหลี่ยมดังกล่าว',
    [
        '$\\dfrac{3\\sqrt{3}}{4\\pi}$',
        '$\\dfrac{2\\sqrt{3}\\,\\pi}{9}$',
        '$\\dfrac{4\\sqrt{3}\\,\\pi}{9}$',
        '$\\dfrac{4\\pi}{3}$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• <b>เซกเตอร์</b> คือชิ้นของวงกลมที่ถูกเฉือนออกมาด้วยรัศมีสองเส้น '
        'มีขอบเป็นรัศมีสองเส้นกับส่วนโค้งหนึ่งเส้น · ถ้ารัศมียาว $r$ หน่วย '
        'และมุมที่จุดศูนย์กลางมีขนาด $\\theta$ เรเดียน แล้วพื้นที่ของเซกเตอร์คือ '
        '$\\dfrac{1}{2}r^2\\theta$ · ที่มาของสูตรนี้คิดเป็นสัดส่วนได้ตรง ๆ : '
        'วงกลมทั้งวงกินมุม $2\\pi$ เรเดียน และมีพื้นที่ $\\pi r^2$ '
        'เซกเตอร์ที่กินมุมเพียง $\\theta$ จึงได้พื้นที่เท่ากับเศษส่วน $\\dfrac{\\theta}{2\\pi}$ ของทั้งวง '
        'นั่นคือ $\\dfrac{\\theta}{2\\pi}\\times\\pi r^2 = \\dfrac{1}{2}r^2\\theta$ · '
        '⛔ สูตรนี้ใช้ได้ก็ต่อเมื่อมุมอยู่ในหน่วยเรเดียนแล้วเท่านั้น',
        '• เมื่อรู้ความยาวด้านสองด้านของรูปสามเหลี่ยมพร้อมกับ<b>มุมที่อยู่ระหว่างด้านทั้งสองนั้น</b> '
        'จะหาพื้นที่ได้ด้วยสูตร $\\dfrac{1}{2}ab\\sin C$ เมื่อ $a$ กับ $b$ เป็นด้านสองด้านนั้น '
        'และ $C$ เป็นมุมที่ประกบอยู่ระหว่างมัน · ที่มาของสูตรมาจากพื้นที่แบบเดิมคือ '
        '$\\dfrac{1}{2}\\times$ ฐาน $\\times$ สูง : ให้ด้าน $a$ เป็นฐาน แล้วลากเส้นตั้งฉากจากปลายอีกข้างของด้าน $b$ '
        'ลงมายังแนวฐาน จะได้ส่วนสูงยาว $b\\sin C$ ⇒ พื้นที่ $= \\dfrac{1}{2}\\times a\\times b\\sin C$ · '
        '⭐ ข้อสำคัญคือมุมต้องอยู่<b>ระหว่าง</b>ด้านทั้งสอง ถ้าหยิบมุมอื่นมาใช้จะผิดทันที',
        '• ⭐ ค่า $\\sin$ ของมุมป้านหาได้จาก<b>มุมอ้างอิง</b> : ถ้ามุม $\\theta$ อยู่ระหว่าง '
        '$\\dfrac{\\pi}{2}$ กับ $\\pi$ (ควอดแรนต์ที่สอง) มุมอ้างอิงของมันคือ $\\pi - \\theta$ '
        'และเนื่องจาก $\\sin$ ในควอดแรนต์ที่สองมีค่าเป็นบวก จึงได้ $\\sin\\theta = \\sin(\\pi - \\theta)$ · '
        'ที่ $\\theta = \\dfrac{2\\pi}{3}$ มุมอ้างอิงคือ $\\pi - \\dfrac{2\\pi}{3} = \\dfrac{\\pi}{3}$ '
        '⇒ $\\sin\\dfrac{2\\pi}{3} = \\sin\\dfrac{\\pi}{3} = \\dfrac{\\sqrt{3}}{2}$ · '
        '⛔ ห้ามเผลอเป็น $\\dfrac{1}{2}$ เพราะ $\\dfrac{1}{2}$ เป็นค่าของ $\\sin\\dfrac{\\pi}{6}$ '
        'ซึ่งจะเกิดขึ้นก็ต่อเมื่อมุมอ้างอิงเป็น $\\dfrac{\\pi}{6}$ เท่านั้น',
        '• ประโยคที่ว่า “$X$ เป็นกี่เท่าของ $Y$” แปลเป็นสัญลักษณ์ได้ว่า $\\dfrac{X}{Y}$ เสมอ · '
        'วิธีจำคือสิ่งที่ตามหลังคำว่า “ของ” จะไปนั่งอยู่ที่<b>ตัวส่วน</b> '
        'ส่วนสิ่งที่ถูกถามว่าเป็นกี่เท่าจะขึ้นไปอยู่ที่<b>ตัวเศษ</b> · '
        'ถ้าวางกลับข้าง ค่าที่ได้จะกลายเป็นส่วนกลับของคำตอบที่ถูกต้อง ซึ่งเป็นคนละจำนวนกันโดยสิ้นเชิง',
        '• การทำส่วนไม่ให้ติดกรณฑ์ : เศษส่วนที่มีกรณฑ์อยู่ที่ตัวส่วนถือว่ายังไม่อยู่ในรูปมาตรฐาน '
        'แก้ได้ด้วยการคูณทั้งเศษและส่วนด้วยกรณฑ์ตัวนั้น ซึ่งเท่ากับคูณด้วย $1$ จึงไม่ทำให้ค่าเปลี่ยน · '
        'เช่น $\\dfrac{4\\pi}{3\\sqrt{3}} = \\dfrac{4\\pi\\times\\sqrt{3}}{3\\sqrt{3}\\times\\sqrt{3}} '
        '= \\dfrac{4\\sqrt{3}\\,\\pi}{9}$ เพราะ $\\sqrt{3}\\times\\sqrt{3} = 3$ และ $3\\times 3 = 9$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• เซกเตอร์ของวงกลมรูปหนึ่งมีรัศมียาว $6$ หน่วย',
        '• มุมที่จุดศูนย์กลางของเซกเตอร์รูปนี้มีขนาด $\\dfrac{2\\pi}{3}$ เรเดียน '
        'ซึ่งเทียบเป็นองศาได้ $120^{\\circ}$ จึงเป็นมุมป้าน',
        '• เมื่อลากคอร์ดเชื่อมจุดปลายทั้งสองของส่วนโค้ง จะได้รูปสามเหลี่ยมที่มีด้านสามด้านคือ '
        'รัศมีเส้นที่หนึ่ง รัศมีเส้นที่สอง และคอร์ดเส้นนั้น',
        '• สังเกตหน้าตาก่อนลงมือ : ทั้งเซกเตอร์และรูปสามเหลี่ยมใช้รัศมีชุดเดียวกันและมุมที่จุดศูนย์กลางมุมเดียวกัน '
        '⇒ ข้อมูลที่โจทย์ให้มาสองตัวคือ $r$ กับ $\\theta$ พอสำหรับหาพื้นที่ทั้งสองรูปแล้ว '
        '⛔ ไม่ต้องเสียเวลาหาความยาวคอร์ดเลยแม้แต่นิดเดียว เพราะสูตรพื้นที่สามเหลี่ยมที่จะใช้ '
        'ขอเพียงด้านสองด้านกับมุมที่อยู่ระหว่างด้านทั้งสอง',
        '• สังเกตอีกอย่าง : พื้นที่เซกเตอร์จะติด $\\pi$ ส่วนพื้นที่สามเหลี่ยมจะติด $\\sqrt{3}$ '
        'เมื่อเอามาหารกัน $\\pi$ ไม่มีอะไรมาตัดและ $\\sqrt{3}$ ก็ไม่มีอะไรมาตัด '
        '⇒ คำตอบต้องมีทั้ง $\\pi$ และ $\\sqrt{3}$ ปรากฏอยู่ด้วยกัน',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาว่าพื้นที่ของเซกเตอร์เป็นกี่เท่าของพื้นที่ของรูปสามเหลี่ยม '
        'นั่นคือหาค่าของ $\\dfrac{\\text{พื้นที่เซกเตอร์}}{\\text{พื้นที่สามเหลี่ยม}}$ '
        'โดยให้พื้นที่เซกเตอร์อยู่ที่ตัวเศษ และพื้นที่สามเหลี่ยมอยู่ที่ตัวส่วน',
        '',
        '<b>【 หาพื้นที่เซกเตอร์ด้วย $\\dfrac{1}{2}r^2\\theta$ แล้วหาพื้นที่สามเหลี่ยมด้วย '
        '$\\dfrac{1}{2}ab\\sin C$ โดยใช้ด้านยาว $6$ สองด้านกับมุม $\\dfrac{2\\pi}{3}$ ที่อยู่ระหว่างมัน '
        'จากนั้นนำพื้นที่ทั้งสองมาหารกันแล้วทำส่วนไม่ให้ติดกรณฑ์ 】</b>',
        '',
        '<b>ขั้นที่ 1 · หาพื้นที่ของเซกเตอร์</b>',
        '• ตั้งชื่อให้เรียกง่ายก่อน : ให้ $A_1$ แทนพื้นที่ของเซกเตอร์ และ $A_2$ แทนพื้นที่ของรูปสามเหลี่ยม',
        '• สูตรที่ใช้ : $A_1 = \\dfrac{1}{2}r^2\\theta$',
        '• ระบุตัวแปร : $r = 6$ คือรัศมีที่โจทย์ให้ · $\\theta = \\dfrac{2\\pi}{3}$ '
        'คือมุมที่จุดศูนย์กลาง ซึ่งโจทย์ให้มาเป็นเรเดียนอยู่แล้ว จึงเสียบเข้าสูตรได้ทันทีโดยไม่ต้องแปลงหน่วย',
        '• แทนค่า : $A_1 = \\dfrac{1}{2}(6)^2\\left(\\dfrac{2\\pi}{3}\\right)$',
        '• ยุบทีละก้าว : $(6)^2 = 36$ ⇒ $\\dfrac{1}{2}(36) = 18$ ⇒ '
        '$18\\times\\dfrac{2\\pi}{3} = \\dfrac{36\\pi}{3} = 12\\pi$',
        '• ⇒ พื้นที่ของเซกเตอร์คือ $A_1 = 12\\pi$ ตารางหน่วย · '
        '⭐ เก็บไว้ในรูปที่ติด $\\pi$ อย่าเพิ่งกดเป็นทศนิยม เพราะขั้นสุดท้ายต้องเอาไปหารกับจำนวนที่ติดกรณฑ์ '
        'การเก็บรูปไว้จะทำให้ยุบได้สวยและไม่มีความคลาดเคลื่อนจากการปัดเศษ',
        '',
        '<b>ขั้นที่ 2 · ระบุด้านและมุมของรูปสามเหลี่ยมให้ครบก่อนเลือกสูตร</b>',
        '• รัศมีของวงกลมวงเดียวกันยาวเท่ากันทุกเส้น เพราะทุกจุดบนวงกลมอยู่ห่างจากจุดศูนย์กลางเป็นระยะเท่ากัน '
        '⇒ ด้านสองด้านของรูปสามเหลี่ยมที่เป็นรัศมี ยาว $6$ หน่วยทั้งคู่',
        '• ด้านที่สามคือคอร์ดที่เชื่อมจุดปลายทั้งสองของส่วนโค้ง ซึ่งเรายังไม่รู้ความยาว',
        '• มุมที่อยู่ระหว่างรัศมีสองเส้นนั้น ก็คือมุมที่จุดศูนย์กลางของเซกเตอร์นั่นเอง '
        'จึงมีขนาด $\\dfrac{2\\pi}{3}$ เรเดียน',
        '• ⭐ <b>จุดที่ทำให้ข้อนี้เดินง่ายกว่าที่คิด</b> : ด้านที่เรารู้ค่าคือ $6$ กับ $6$ '
        'และมุมที่รู้ค่าก็คือมุมที่ประกบอยู่ระหว่างด้านทั้งสองนั้นพอดี '
        '⇒ ตรงกับเงื่อนไขของสูตร $\\dfrac{1}{2}ab\\sin C$ เป๊ะ ๆ '
        '⛔ จึงไม่ต้องหาความยาวคอร์ดและไม่ต้องหาส่วนสูงใด ๆ เลย',
        '',
        '<b>ขั้นที่ 3 · หาค่าของ $\\sin\\dfrac{2\\pi}{3}$ ด้วยมุมอ้างอิง</b>',
        '• มุม $\\dfrac{2\\pi}{3}$ เรเดียน เทียบเป็นองศาได้ $\\dfrac{2}{3}\\times 180^{\\circ} = 120^{\\circ}$ '
        'ซึ่งอยู่ระหว่าง $90^{\\circ}$ กับ $180^{\\circ}$ ⇒ เป็นมุมในควอดแรนต์ที่สอง',
        '• หามุมอ้างอิง : มุมอ้างอิง $= \\pi - \\theta = \\pi - \\dfrac{2\\pi}{3} '
        '= \\dfrac{3\\pi - 2\\pi}{3} = \\dfrac{\\pi}{3}$',
        '• ในควอดแรนต์ที่สอง ค่าของ $\\sin$ เป็นบวก ⇒ '
        '$\\sin\\dfrac{2\\pi}{3} = +\\sin\\dfrac{\\pi}{3} = \\dfrac{\\sqrt{3}}{2}$',
        '• ⛔ <b>จุดพลิกของข้อนี้อยู่ตรงนี้</b> : มุมอ้างอิงคือ $\\dfrac{\\pi}{3}$ '
        'ไม่ใช่ $\\dfrac{\\pi}{6}$ จึงได้ $\\dfrac{\\sqrt{3}}{2}$ ไม่ใช่ $\\dfrac{1}{2}$ · '
        'ตรวจซ้ำได้ง่าย ๆ ด้วยการบวกกลับ : $\\dfrac{2\\pi}{3} + \\dfrac{\\pi}{3} = \\pi$ ✓ '
        'ในขณะที่ $\\dfrac{2\\pi}{3} + \\dfrac{\\pi}{6} = \\dfrac{5\\pi}{6}$ ซึ่งไม่ครบ $\\pi$ '
        '⇒ $\\dfrac{\\pi}{6}$ ไม่ใช่มุมอ้างอิงของมุมนี้แน่นอน',
        '',
        '<b>ขั้นที่ 4 · หาพื้นที่ของรูปสามเหลี่ยม</b>',
        '• สูตรที่ใช้ : $A_2 = \\dfrac{1}{2}ab\\sin C$',
        '• ระบุตัวแปร : $a = 6$ และ $b = 6$ คือรัศมีสองเส้นที่เป็นด้านประกอบมุม '
        '· $C = \\dfrac{2\\pi}{3}$ คือมุมที่อยู่ระหว่างด้านทั้งสองนั้น',
        '• แทนค่า : $A_2 = \\dfrac{1}{2}(6)(6)\\sin\\dfrac{2\\pi}{3}$',
        '• ยุบทีละก้าว : $\\dfrac{1}{2}(6)(6) = \\dfrac{36}{2} = 18$ ⇒ '
        '$A_2 = 18\\times\\dfrac{\\sqrt{3}}{2} = \\dfrac{18\\sqrt{3}}{2} = 9\\sqrt{3}$',
        '• ⇒ พื้นที่ของรูปสามเหลี่ยมคือ $A_2 = 9\\sqrt{3}$ ตารางหน่วย · '
        'ตรวจความสมเหตุสมผลอย่างเร็ว : $9\\sqrt{3} \\approx 15.59$ ซึ่งน้อยกว่า $12\\pi \\approx 37.70$ '
        'สอดคล้องกับความจริงที่ว่ารูปสามเหลี่ยมวางอยู่ภายในเซกเตอร์',
        '',
        '<b>ขั้นที่ 5 · หารกันแล้วจัดรูปให้ส่วนไม่ติดกรณฑ์</b>',
        '• เขียนสิ่งที่โจทย์ถามให้เป็นเศษส่วน : $\\dfrac{A_1}{A_2} = \\dfrac{12\\pi}{9\\sqrt{3}}$ '
        'โดยพื้นที่เซกเตอร์อยู่ตัวเศษ เพราะโจทย์ถามว่าเซกเตอร์เป็นกี่เท่าของสามเหลี่ยม',
        '• ตัดตัวเลขหน้าให้เล็กลงก่อน : $12$ กับ $9$ มีตัวหารร่วมมากเป็น $3$ '
        '⇒ $\\dfrac{12\\pi}{9\\sqrt{3}} = \\dfrac{4\\pi}{3\\sqrt{3}}$',
        '• ทำส่วนไม่ให้ติดกรณฑ์ โดยคูณทั้งเศษและส่วนด้วย $\\sqrt{3}$ : '
        '$\\dfrac{4\\pi}{3\\sqrt{3}}\\times\\dfrac{\\sqrt{3}}{\\sqrt{3}} '
        '= \\dfrac{4\\sqrt{3}\\,\\pi}{3\\times 3} = \\dfrac{4\\sqrt{3}\\,\\pi}{9}$',
        '• การคูณด้วย $\\dfrac{\\sqrt{3}}{\\sqrt{3}}$ คือการคูณด้วย $1$ ค่าจึงไม่เปลี่ยน '
        'เปลี่ยนแต่หน้าตาให้อยู่ในรูปมาตรฐาน',
        '• ⇒ พื้นที่ของเซกเตอร์เป็น $\\dfrac{4\\sqrt{3}\\,\\pi}{9}$ เท่าของพื้นที่ของรูปสามเหลี่ยม',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ประมาณค่าเป็นทศนิยมทั้งสองฝั่ง แล้วปิดท้ายด้วยเหตุผลเชิงขอบเขต '
        'ที่ว่าเซกเตอร์ต้องใหญ่กว่ารูปสามเหลี่ยมเสมอ)</b>',
        '• เส้นทางข้างบนเดินด้วยการจัดรูปพีชคณิตล้วน การตรวจรอบนี้จะไม่จัดรูปอะไรอีกเลย '
        'แต่จะกดตัวเลขออกมาเป็นทศนิยมทั้งสองฝั่งแล้วดูว่าตรงกันหรือไม่',
        '• ฝั่งที่หนึ่ง คิดจากพื้นที่จริงของทั้งสองรูป : พื้นที่เซกเตอร์ $12\\pi \\approx 12(3.1416) = 37.70$ '
        'ตารางหน่วย · พื้นที่สามเหลี่ยม $9\\sqrt{3} \\approx 9(1.7321) = 15.59$ ตารางหน่วย '
        '⇒ อัตราส่วน $\\approx \\dfrac{37.70}{15.59} \\approx 2.418$',
        '• ฝั่งที่สอง กดค่าที่ตอบไปออกมาเป็นทศนิยม : $\\dfrac{4\\sqrt{3}\\,\\pi}{9} '
        '\\approx \\dfrac{4(1.7321)(3.1416)}{9} \\approx \\dfrac{21.766}{9} \\approx 2.418$ ✓ '
        'ตรงกับฝั่งที่หนึ่งทุกหลักที่กดออกมา',
        '• เหตุผลเชิงขอบเขตที่ใช้กันพลาดได้ทันทีโดยไม่ต้องคำนวณ : รูปสามเหลี่ยมทั้งรูปวางอยู่ภายในเซกเตอร์ '
        'เพราะมีจุดยอดร่วมกันที่จุดศูนย์กลางและใช้รัศมีคู่เดียวกันเป็นขอบ '
        'ต่างกันแค่ขอบที่สามซึ่งฝั่งหนึ่งเป็นคอร์ดตรง ส่วนอีกฝั่งเป็นส่วนโค้งที่โป่งออกไปข้างนอก '
        '⇒ พื้นที่เซกเตอร์ต้องมากกว่าพื้นที่สามเหลี่ยมเสมอ ⇒ อัตราส่วนที่ถามต้องมากกว่า $1$ '
        '⇒ ค่าที่น้อยกว่า $1$ ตกรอบได้ทันทีโดยไม่ต้องคิดต่อ',
        '• ตรวจหน้าตาของคำตอบเป็นด่านสุดท้าย : ตัวเศษต้องมี $\\pi$ ติดมาจากพื้นที่เซกเตอร์ '
        'และต้องมี $\\sqrt{3}$ ติดมาจากพื้นที่สามเหลี่ยม · ค่า $\\dfrac{4\\sqrt{3}\\,\\pi}{9}$ มีครบทั้งสองอย่าง ✓',
        '',
        '✅ <b>คำตอบ</b> พื้นที่ของเซกเตอร์เป็น $\\dfrac{4\\sqrt{3}\\,\\pi}{9}$ '
        'เท่าของพื้นที่ของรูปสามเหลี่ยม → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• ทางลัดที่ใช้ได้ทุกครั้งที่เซกเตอร์กับรูปสามเหลี่ยมมาจากรัศมีชุดเดียวกันและมุมเดียวกัน : '
        'เขียนอัตราส่วนแล้วตัด $\\dfrac{1}{2}r^2$ ทิ้งทั้งเศษและส่วนตั้งแต่ยังไม่แทนตัวเลข '
        'จะเหลือแค่ $\\dfrac{\\theta}{\\sin\\theta}$ · ที่นี่คือ '
        '$\\dfrac{2\\pi/3}{\\sqrt{3}/2} = \\dfrac{4\\pi}{3\\sqrt{3}} = \\dfrac{4\\sqrt{3}\\,\\pi}{9}$ '
        'ได้คำตอบเดียวกันโดยไม่ต้องคำนวณพื้นที่จริงสักรูปเดียว และรัศมี $6$ ก็ไม่ถูกใช้เลยด้วยซ้ำ',
        '• ท่องค่ามุมพิเศษให้แม่นเป็นคู่ ๆ : $\\sin\\dfrac{\\pi}{6} = \\dfrac{1}{2}$ · '
        '$\\sin\\dfrac{\\pi}{3} = \\dfrac{\\sqrt{3}}{2}$ · แล้วจำกฎมุมอ้างอิงคู่ไปด้วยว่า '
        'มุมป้านให้เอา $\\pi$ ตั้งลบ ก่อนจะเปิดตารางค่ามุมพิเศษเสมอ',
        '• ก่อนวงคำตอบให้ใช้ “การนับหน้าตา” กรองค่าที่เป็นไปไม่ได้ทิ้งอย่างเร็ว : '
        'อัตราส่วนของพื้นที่สองรูปเป็นจำนวนที่ไม่มีหน่วย และในข้อนี้ต้องติดทั้ง $\\pi$ กับ $\\sqrt{3}$ '
        'พร้อมกัน ⇒ ค่าที่มีแต่ $\\pi$ ไม่มี $\\sqrt{3}$ ตกรอบทันทีโดยยังไม่ต้องคำนวณอะไรเลย',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\dfrac{3\\sqrt{3}}{4\\pi}$ เพราะวางเศษกับส่วนกลับข้าง คือไปคิดว่ารูปสามเหลี่ยมเป็นกี่เท่าของเซกเตอร์ '
        '⇒ $\\dfrac{9\\sqrt{3}}{12\\pi} = \\dfrac{3\\sqrt{3}}{4\\pi}$ · '
        'ค่านี้ผิดแน่นอนและตรวจจับได้ในหนึ่งวินาที เพราะกดออกมาได้ประมาณ $\\dfrac{15.59}{37.70} \\approx 0.413$ '
        'ซึ่ง<b>น้อยกว่า</b> $1$ ทั้งที่รูปสามเหลี่ยมวางอยู่ข้างในเซกเตอร์ '
        'ของที่เล็กกว่าจะเป็น $2.418$ เท่าของของที่ใหญ่กว่าไม่ได้ · '
        'วิธีกันคือแปลประโยคเป็นเศษส่วนตั้งแต่ก่อนคำนวณ โดยยึดกฎว่าอะไรตามหลังคำว่า “ของ” ให้ลงไปอยู่ตัวส่วน',
        '• ได้ค่า $\\dfrac{2\\sqrt{3}\\,\\pi}{9}$ เพราะลืมตัวประกอบ $\\dfrac{1}{2}$ ในสูตรพื้นที่สามเหลี่ยม '
        'คือไปใช้ $r^2\\sin\\theta = 36\\times\\dfrac{\\sqrt{3}}{2} = 18\\sqrt{3}$ '
        '⇒ $\\dfrac{12\\pi}{18\\sqrt{3}} = \\dfrac{2\\pi}{3\\sqrt{3}} = \\dfrac{2\\sqrt{3}\\,\\pi}{9}$ · '
        'ค่านี้ผิดเพราะพื้นที่สามเหลี่ยมที่แท้จริงหาซ้ำได้ด้วยฐานคูณสูง : คอร์ดยาว $6\\sqrt{3}$ หน่วย '
        'และส่วนสูงจากจุดศูนย์กลางลงมาตั้งฉากกับคอร์ดยาว $3$ หน่วย '
        '⇒ พื้นที่ $= \\dfrac{1}{2}(6\\sqrt{3})(3) = 9\\sqrt{3}$ ไม่ใช่ $18\\sqrt{3}$ · '
        'สังเกตว่า $18\\sqrt{3} \\approx 31.18$ ซึ่งกินพื้นที่เกือบทั้งเซกเตอร์ที่มีอยู่ $37.70$ '
        'ทั้งที่ส่วนโค้งโป่งออกไปไกลมาก ⇒ ใหญ่เกินจริงอย่างเห็นได้ชัด',
        '• ได้ค่า $\\dfrac{4\\pi}{3}$ เพราะใช้มุมอ้างอิงผิดตัว ไปแทน $\\sin\\dfrac{2\\pi}{3} = \\dfrac{1}{2}$ '
        '⇒ พื้นที่สามเหลี่ยมกลายเป็น $\\dfrac{1}{2}(6)(6)\\left(\\dfrac{1}{2}\\right) = 9$ '
        '⇒ $\\dfrac{12\\pi}{9} = \\dfrac{4\\pi}{3}$ · ค่านี้ผิดสองชั้น : ชั้นแรก '
        '$\\dfrac{1}{2}$ เป็นค่าของ $\\sin\\dfrac{\\pi}{6}$ แต่มุมอ้างอิงของ $\\dfrac{2\\pi}{3}$ คือ '
        '$\\pi - \\dfrac{2\\pi}{3} = \\dfrac{\\pi}{3}$ จึงต้องได้ $\\dfrac{\\sqrt{3}}{2}$ · '
        'ชั้นที่สอง หน้าตาของค่านี้ไม่มี $\\sqrt{3}$ ติดมาเลย ทั้งที่พื้นที่สามเหลี่ยมที่ถูกต้องคือ $9\\sqrt{3}$ '
        'ซึ่งเป็นจำนวนอตรรกยะ ⇒ ผลหารจะตัด $\\sqrt{3}$ ทิ้งไปเฉย ๆ ไม่ได้',
        '• อีกเส้นทางที่พลาดกันบ่อยคือเผลอใช้พื้นที่ของ<b>วงกลมทั้งวง</b>แทนพื้นที่เซกเตอร์ '
        '⇒ $\\pi r^2 = 36\\pi$ แล้วหารด้วย $9\\sqrt{3}$ ได้ $\\dfrac{4\\pi}{\\sqrt{3}} '
        '= \\dfrac{4\\sqrt{3}\\,\\pi}{3} \\approx 7.26$ · '
        'สัญญาณเตือนดังทันทีสองอย่าง : หนึ่ง ตัวเลข $\\dfrac{2\\pi}{3}$ ที่โจทย์ให้มายังไม่ได้ถูกใช้เลยสักครั้ง '
        'สอง ค่าที่ได้ไม่ตรงกับค่าใดที่มีให้เลือกเลย · '
        'ให้ถามตัวเองทุกครั้งก่อนตอบว่า “ข้อมูลที่โจทย์ให้มา ถูกใช้ครบทุกตัวแล้วหรือยัง”',
    ],
    'V.mold: G = one sector of a circle given only by a numerical radius of 6 units and a central angle of '
    '2*pi/3 radians, with the chord joining the two endpoints of its arc drawn so that the two radii and '
    'that chord bound a triangle sitting inside the sector / A = how many times the area of the sector is '
    'the area of that triangle, i.e. a pure ratio of two areas rather than either area on its own / '
    'M = evaluate the sector area from (1/2)*r^2*theta, evaluate the triangle area from the two-sides-and-'
    'included-angle formula with the included angle being the same central angle, resolve sin(2*pi/3) '
    'through the reference angle pi/3, then divide the first by the second and rationalise the '
    'denominator. '
    'Rubric F2 C1 P2 T1 L0 = 6/15, total inside the 5 to 7 band with T no higher than 1 -> level: '
    'ปานกลาง. F = 2 because two distinct formulas must be held at once, the sector area and the '
    'included-angle triangle area, and neither one alone answers the question. C = 1 because subtopic '
    '7.11 has to be joined to the triangle-area tool of the right-triangle and area family, a real but '
    'shallow crossing since both tools are handed the very same r and theta and no second trigonometric '
    'identity is needed. P = 2 because the work splits into two productions of different kinds followed '
    'by a combination: one area, then a second area whose sine value must first be resolved, then the '
    'division and the rationalising of the denominator. T = 1 for the single turning point, that '
    'sin(2*pi/3) equals sqrt(3)/2 and not 1/2 because the reference angle is pi/3; T was held at 1 and '
    'not raised to 2 because the statement spells out that the triangle is bounded by the two radii and '
    'the chord, so the solver has nothing to infer about which sides and which angle enter the formula, '
    'and the direction of the ratio is spelled out by the words as well. L = 0 because the item is a bare '
    'plane figure with no worded situation to model and no scene to translate. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b20.py): Rational(1,2)*6**2*(2*pi/3) simplifies to 12*pi, sin(2*pi/3) returns '
    'sqrt(3)/2 and is confirmed equal to sin(pi/3), Rational(1,2)*6*6*sin(2*pi/3) simplifies to 9*sqrt(3), '
    'and radsimp of 12*pi/(9*sqrt(3)) returns 4*sqrt(3)*pi/9 with float value 2.4183991523122903, so the '
    'key at index 2 is exact. The triangle area was recomputed twice more by machine along paths the '
    'solution never walks: the chord is 2*6*sin(pi/3) = 6*sqrt(3) and the law of cosines gives the same '
    'chord from 6**2 + 6**2 - 2*6*6*cos(2*pi/3) = 108, after which both Heron on sides 6, 6, 6*sqrt(3) '
    'and base times height, (1/2)*6*sqrt(3)*3, return 9*sqrt(3). Every wrong value was machine-computed '
    'from a named error path instead of being invented: 9*sqrt(3)/(12*pi) = 3*sqrt(3)/(4*pi) is about '
    '0.4135 for inverting the ratio, 12*pi/(6**2*sin(2*pi/3)) = 2*sqrt(3)*pi/9 is about 1.2092 for '
    'dropping the factor 1/2 from the triangle area, and 12*pi/((1/2)*6*6*(1/2)) = 4*pi/3 is about 4.1888 '
    'for reading the reference angle as pi/6. The unlisted fourth path, using the whole circle instead of '
    'the sector, was evaluated too: 36*pi/(9*sqrt(3)) = 4*sqrt(3)*pi/3 is about 7.2552 and matches '
    'nothing on offer. The bounding argument used in the independent check was verified numerically as '
    'well, 15.588 < 37.699, so the ratio is above 1 and every value below 1 is impossible. '
    'Collision sweep on 6437 items (bank 63 files + k1 out + k2 out, that is the 6417 quoted in the '
    'batch-20 spec plus the 20 items of batch 19 that have since landed in k2 out), probe collide_b20.py '
    '/ collide_b20b.py: the pair that defines this item, the word sector together with the word triangle '
    'inside the question text, returns 0 items across the whole corpus, and the pair sector together with '
    'a ratio of areas returns 0 items as well. The scan for sector together with the phrase how many '
    'times returns exactly 1 item, gen-chap-07-trigonometry-q119, which compares the arc lengths of two '
    'sectors of equal area and contains no triangle at all, sharing neither G nor A nor M. The nearest '
    'surface neighbours are gen-chap-07-trigonometry-q030, which hands over a radius and the same angle '
    '2*pi/3 and asks for the sector area alone in a single step, and gen-chap-07-trigonometry-q118, '
    'which uses the same angle with radius 12 and asks by how much the arc exceeds the chord; both stop '
    'at one figure and neither forms a ratio. The saturated segment tool, sector minus triangle, is '
    'deliberately not used here: the solution forms a quotient and never a difference, and the probe for '
    'the word segment returns 0 items. Choices are ordered ascending by numeric value, 0.4135, then '
    '1.2092, then 2.4184, then 4.1888, so the answer slot is forced by that rule and was not chosen.',
)

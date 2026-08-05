# -*- coding: utf-8 -*-
add(
    103,
    ['7.7', '7.5'],
    'ยาก',
    'จำนวนจริงบวกที่น้อยที่สุดซึ่งสอดคล้องกับสมการ $\\sin 3x = \\cos 2x$ เท่ากับข้อใด',
    [
        '$\\dfrac{\\pi}{10}$',
        '$\\dfrac{\\pi}{6}$',
        '$\\dfrac{\\pi}{5}$',
        '$\\dfrac{\\pi}{2}$',
    ],
    0,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เอกลักษณ์มุมประกอบ : $\\cos\\theta = \\sin\\left(\\dfrac{\\pi}{2} - \\theta\\right)$ '
        'และในทางกลับกัน $\\sin\\theta = \\cos\\left(\\dfrac{\\pi}{2} - \\theta\\right)$ '
        'ที่มาคือในสามเหลี่ยมมุมฉาก มุมแหลมสองมุมรวมกันได้ $\\dfrac{\\pi}{2}$ เสมอ '
        'ด้านตรงข้ามของมุมหนึ่งจึงกลายเป็นด้านประชิดของอีกมุมหนึ่ง อัตราส่วนไซน์ของมุมหนึ่ง '
        'จึงเท่ากับอัตราส่วนโคไซน์ของมุมที่เหลือพอดี และเมื่อขยายไปบนวงกลมหนึ่งหน่วยแล้ว '
        'เอกลักษณ์นี้ใช้ได้กับ<b>ทุกจำนวนจริง</b> ไม่ได้จำกัดเฉพาะมุมแหลม',
        '• เงื่อนไขที่ไซน์สองก้อนเท่ากัน : $\\sin A = \\sin B$ ก็ต่อเมื่อ $A = B + 2k\\pi$ '
        'หรือ $A = \\pi - B + 2k\\pi$ เมื่อ $k$ เป็นจำนวนเต็ม '
        'ที่มาคือค่าไซน์คือพิกัดตามแนวตั้งของจุดบนวงกลมหนึ่งหน่วย เส้นแนวนอนหนึ่งเส้นตัดวงกลมได้ '
        '<b>สองจุด</b> จุดหนึ่งอยู่ที่มุม $B$ อีกจุดอยู่ที่มุม $\\pi - B$ ซึ่งสมมาตรกันรอบแกนตั้ง '
        'และการหมุนครบรอบเพิ่มอีกกี่รอบก็ได้พิกัดเดิม จึงบวก $2k\\pi$ ต่อท้ายทั้งสองกรณี',
        '• เพราะ $k$ เป็นจำนวนเต็มใด ๆ จะเป็นบวก เป็นลบ หรือเป็นศูนย์ก็ได้ '
        'คำตอบของสมการตรีโกณจึงไม่ใช่ค่าเดียว แต่เป็น<b>วงศ์คำตอบ</b> คือชุดอนันต์ที่เรียงห่างเท่า ๆ กัน '
        'วิธีหาค่าบวกที่เล็กที่สุดของวงศ์หนึ่ง ๆ คือไล่ $k$ ลงทีละขั้นจาก $0$ จนค่าเริ่มติดลบ '
        'แล้วถอยกลับมาหนึ่งขั้น',
        '• สมการแบบนี้ให้วงศ์คำตอบมากกว่าหนึ่งวงศ์ ค่าบวกที่เล็กที่สุดของ<b>ทั้งสมการ</b> '
        'จึงหาได้จากการเก็บค่าบวกที่เล็กที่สุดของแต่ละวงศ์มาก่อน แล้วจึงเทียบกันอีกที '
        '⛔ ห้ามหยุดที่วงศ์แรกที่แก้ได้',
        '• การแทนค่ากลับแล้วพบว่าสมการเป็นจริง บอกได้เพียงว่าค่านั้น<b>เป็นคำตอบ</b> '
        'แต่ไม่ได้บอกเลยว่ามันเป็นคำตอบที่เล็กที่สุด โจทย์ที่ถามหาค่าเล็กสุดจึงต้องมีขั้นเปรียบเทียบเสมอ '
        'จะข้ามไม่ได้เด็ดขาด',
        '• การเทียบขนาดของเศษส่วนที่มี $\\pi$ อยู่ที่ตัวเศษเหมือนกัน ให้ดูตัวส่วน '
        'ตัวส่วนยิ่งใหญ่ ค่ายิ่งน้อย ดังนั้น $\\dfrac{\\pi}{10} < \\dfrac{\\pi}{6} < \\dfrac{\\pi}{5} '
        '< \\dfrac{\\pi}{2}$ ซึ่งมีค่าประมาณ $0.314$ · $0.524$ · $0.628$ · $1.571$ ตามลำดับ',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• สมการที่ต้องแก้คือ $\\sin 3x = \\cos 2x$',
        '• ตัวแปร $x$ เป็นจำนวนจริง และโจทย์สนใจเฉพาะค่าที่เป็นบวก โดยไม่ได้ปิดขอบเขตด้านบนไว้',
        '• สังเกตหน้าตาก่อนลงมือ : สองข้างของสมการเป็นฟังก์ชันคนละชนิด ข้างหนึ่งเป็นไซน์ อีกข้างเป็นโคไซน์ '
        'และมุมก็เป็นพหุคูณคนละตัว คือ $3x$ กับ $2x$ '
        'ก้าวแรกจึงต้องทำให้เป็นฟังก์ชันชนิดเดียวกันก่อน ยังแก้อะไรไม่ได้ถ้าชนิดยังไม่ตรงกัน',
        '• ⛔ ทางที่ดูเหมือนตรงไปตรงมาแต่พาไปตาย คือกระจาย $\\sin 3x = 3\\sin x - 4\\sin^3 x$ '
        'และ $\\cos 2x = 1 - 2\\sin^2 x$ ให้เหลือแต่ $\\sin x$ '
        'เพราะจะได้พหุนามกำลังสาม $4\\sin^3 x - 2\\sin^2 x - 3\\sin x + 1 = 0$ '
        'ซึ่งแยกตัวประกอบด้วยมือได้ยากและพลาดง่ายมาก',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาจำนวนจริงที่เป็นบวกและมีค่าเล็กที่สุด ซึ่งแทนลงในสมการ $\\sin 3x = \\cos 2x$ แล้วเป็นจริง',
        '',
        '<b>【 เปลี่ยน $\\cos 2x$ ให้เป็นไซน์ด้วยเอกลักษณ์มุมประกอบ แล้วเปิดเงื่อนไขสองวงศ์ของ '
        '$\\sin A = \\sin B$ หาคำตอบให้ครบทุกวงศ์ จากนั้นจึงเทียบค่าบวกที่เล็กที่สุดของแต่ละวงศ์ 】</b>',
        '',
        '<b>ขั้นที่ 1 · ทำให้สองข้างเป็นฟังก์ชันชนิดเดียวกัน</b>',
        '• สูตรที่ใช้ : $\\cos\\theta = \\sin\\left(\\dfrac{\\pi}{2} - \\theta\\right)$',
        '• ระบุตัวแปรก่อนแทนค่า : $\\theta$ ในสูตรคือมุมที่อยู่ใต้โคไซน์ '
        'ซึ่งข้อนี้ทั้งก้อนคือ $2x$ ⛔ ไม่ใช่ $x$ เฉย ๆ',
        '• แทนค่า : $\\cos 2x = \\sin\\left(\\dfrac{\\pi}{2} - 2x\\right)$',
        '• สมการจึงกลายเป็น $\\sin 3x = \\sin\\left(\\dfrac{\\pi}{2} - 2x\\right)$ '
        'ตอนนี้ทั้งสองข้างเป็นไซน์เหมือนกันแล้ว จึงเทียบมุมกันได้',
        '',
        '<b>ขั้นที่ 2 · เปิดเงื่อนไขสองวงศ์ของสมการไซน์เท่ากัน</b>',
        '• สูตรที่ใช้ : $\\sin A = \\sin B$ ก็ต่อเมื่อ $A = B + 2k\\pi$ หรือ $A = \\pi - B + 2k\\pi$ '
        'เมื่อ $k$ เป็นจำนวนเต็ม',
        '• ระบุตัวแปร : $A = 3x$ และ $B = \\dfrac{\\pi}{2} - 2x$',
        '• แทนค่าลงทั้งสองกรณี จะได้สองสมการที่ต้องแก้แยกกัน '
        'วงศ์ที่หนึ่ง $3x = \\dfrac{\\pi}{2} - 2x + 2k\\pi$ '
        'และวงศ์ที่สอง $3x = \\pi - \\left(\\dfrac{\\pi}{2} - 2x\\right) + 2k\\pi$',
        '• ⛔ จุดที่พลาดกันมากที่สุดของทั้งข้ออยู่ตรงนี้ : ต้องเขียนให้ครบทั้งสองวงศ์ '
        'ถ้าเขียนวงศ์เดียวแล้วเดินต่อ คำตอบที่ได้จะเป็นคำตอบจริงก็จริง แต่ไม่มีทางรู้ว่าเล็กที่สุดหรือไม่',
        '',
        '<b>ขั้นที่ 3 · แก้วงศ์ที่หนึ่งให้เป็นสูตรทั่วไป แล้วดึงค่าบวกที่เล็กที่สุดออกมา</b>',
        '• เริ่มจาก $3x = \\dfrac{\\pi}{2} - 2x + 2k\\pi$ ย้าย $-2x$ ข้ามไปบวกทางซ้าย '
        'ได้ $3x + 2x = \\dfrac{\\pi}{2} + 2k\\pi$ นั่นคือ $5x = \\dfrac{\\pi}{2} + 2k\\pi$',
        '• หารทั้งสองข้างด้วย $5$ ได้สูตรทั่วไปของวงศ์นี้ '
        '$x = \\dfrac{\\pi}{10} + \\dfrac{2k\\pi}{5}$ '
        'ซึ่งอ่านได้ว่าเป็นลำดับที่เริ่มจาก $\\dfrac{\\pi}{10}$ แล้วขยับทีละ $\\dfrac{2\\pi}{5}$',
        '• ไล่ค่า $k$ ทีละตัว : $k = 0$ ให้ $x = \\dfrac{\\pi}{10}$ (เป็นบวก ✓) · '
        '$k = 1$ ให้ $x = \\dfrac{\\pi}{10} + \\dfrac{4\\pi}{10} = \\dfrac{5\\pi}{10} = \\dfrac{\\pi}{2}$ · '
        '$k = -1$ ให้ $x = \\dfrac{\\pi}{10} - \\dfrac{4\\pi}{10} = -\\dfrac{3\\pi}{10}$ '
        'ซึ่งติดลบ จึงใช้ไม่ได้',
        '• ค่าบวกที่เล็กที่สุดของวงศ์ที่หนึ่งจึงคือ $\\dfrac{\\pi}{10}$ '
        'และสังเกตไว้ด้วยว่า $\\dfrac{\\pi}{2}$ ก็โผล่มาจากวงศ์นี้เองที่ $k = 1$',
        '',
        '<b>ขั้นที่ 4 · แก้วงศ์ที่สองให้เป็นสูตรทั่วไป แล้วดึงค่าบวกที่เล็กที่สุดออกมา</b>',
        '• เริ่มจาก $3x = \\pi - \\left(\\dfrac{\\pi}{2} - 2x\\right) + 2k\\pi$ '
        'กระจายวงเล็บโดยพลิกเครื่องหมายทุกพจน์ข้างใน ได้ '
        '$3x = \\pi - \\dfrac{\\pi}{2} + 2x + 2k\\pi$',
        '• ยุบพจน์ที่เป็น $\\pi$ ก่อน : $\\pi - \\dfrac{\\pi}{2} = \\dfrac{\\pi}{2}$ '
        'สมการจึงเหลือ $3x = \\dfrac{\\pi}{2} + 2x + 2k\\pi$',
        '• ย้าย $2x$ มาลบทางซ้าย ได้ $3x - 2x = \\dfrac{\\pi}{2} + 2k\\pi$ '
        'นั่นคือ $x = \\dfrac{\\pi}{2} + 2k\\pi$ ซึ่งเป็นสูตรทั่วไปของวงศ์ที่สอง',
        '• ไล่ค่า $k$ : $k = 0$ ให้ $x = \\dfrac{\\pi}{2}$ (เป็นบวก ✓) · '
        '$k = -1$ ให้ $x = \\dfrac{\\pi}{2} - 2\\pi = -\\dfrac{3\\pi}{2}$ ซึ่งติดลบ จึงใช้ไม่ได้',
        '• ค่าบวกที่เล็กที่สุดของวงศ์ที่สองจึงคือ $\\dfrac{\\pi}{2}$',
        '',
        '<b>ขั้นที่ 5 · เทียบผู้ชนะของแต่ละวงศ์แล้วเลือกตัวที่เล็กกว่า</b>',
        '• ผู้เข้าชิงมีสองตัวเท่านั้น คือ $\\dfrac{\\pi}{10}$ จากวงศ์ที่หนึ่ง '
        'และ $\\dfrac{\\pi}{2}$ จากวงศ์ที่สอง เพราะภายในวงศ์เดียวกันค่าถัดไปมีแต่จะโตขึ้น',
        '• เทียบขนาด : $\\dfrac{\\pi}{10} \\approx 0.314$ ส่วน $\\dfrac{\\pi}{2} \\approx 1.571$ '
        'ตัวเศษเท่ากันแต่ตัวส่วนของตัวแรกใหญ่กว่า ค่าจึงน้อยกว่า',
        '• สรุปได้ว่าจำนวนจริงบวกที่เล็กที่สุดซึ่งสอดคล้องกับสมการนี้คือ $\\dfrac{\\pi}{10}$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่าตัวเลขลงสมการเดิมตรง ๆ แล้วปิดช่วงที่เหลือด้วยสมบัติเพิ่มขึ้นของไซน์ '
        'โดยไม่แตะสูตรวงศ์คำตอบเลย)</b>',
        '• แทน $x = \\dfrac{\\pi}{10}$ ลงในสมการเดิม จะได้มุมสองมุมคือ '
        '$3x = \\dfrac{3\\pi}{10}$ และ $2x = \\dfrac{2\\pi}{10}$',
        '• บวกมุมทั้งสองดู : $\\dfrac{3\\pi}{10} + \\dfrac{2\\pi}{10} = \\dfrac{5\\pi}{10} '
        '= \\dfrac{\\pi}{2}$ แปลว่ามุมทั้งสองเป็นมุมประกอบกันพอดี '
        'ไซน์ของมุมหนึ่งจึงต้องเท่ากับโคไซน์ของอีกมุมโดยอัตโนมัติ สมการเป็นจริงแน่นอน ✓',
        '• ดูเป็นตัวเลขก็ตรงกัน : $3x$ คือ 54 องศา และ $2x$ คือ 36 องศา '
        'ซึ่ง $\\sin$ ของ 54 องศา และ $\\cos$ ของ 36 องศา มีค่าประมาณ $0.809$ เท่ากันทั้งคู่',
        '• เหลือแค่ต้องปิดช่องว่างว่าไม่มีคำตอบใดเล็กกว่านี้ : ให้ $0 < x < \\dfrac{\\pi}{10}$ '
        'จะได้ $5x < \\dfrac{\\pi}{2}$ ซึ่งจัดรูปใหม่เป็น $3x < \\dfrac{\\pi}{2} - 2x$',
        '• ในช่วงนี้ทั้ง $3x$ และ $\\dfrac{\\pi}{2} - 2x$ ต่างก็อยู่ระหว่าง $0$ กับ $\\dfrac{\\pi}{2}$ '
        'ซึ่งเป็นช่วงที่ไซน์เพิ่มขึ้นอย่างเคร่งครัด มุมที่เล็กกว่าจึงให้ค่าไซน์ที่น้อยกว่าเสมอ '
        'ได้ $\\sin 3x < \\sin\\left(\\dfrac{\\pi}{2} - 2x\\right) = \\cos 2x$',
        '• นั่นคือ $\\sin 3x - \\cos 2x$ ติดลบตลอดช่วง $\\left(0, \\dfrac{\\pi}{10}\\right)$ '
        'ไม่มีจุดใดเป็นศูนย์ได้เลย ⇒ $\\dfrac{\\pi}{10}$ คือค่าบวกตัวแรกจริง ✓ '
        'และเส้นทางนี้ยังคัดค่า $\\dfrac{\\pi}{2}$ ทิ้งได้ทันที เพราะ $\\dfrac{\\pi}{10}$ '
        'เป็นคำตอบที่เล็กกว่าและมีอยู่จริง',
        '',
        '✅ <b>คำตอบ</b> จำนวนจริงบวกที่เล็กที่สุดซึ่งสอดคล้องกับสมการ $\\sin 3x = \\cos 2x$ '
        'คือ $\\dfrac{\\pi}{10}$ → <b>ตัวเลือก 1</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอสมการที่ข้างหนึ่งเป็นไซน์อีกข้างเป็นโคไซน์ ให้เปลี่ยนเป็นชนิดเดียวกันด้วยมุมประกอบก่อนเสมอ '
        'อย่าเพิ่งกระจายเป็นพหุนามใน $\\sin x$ เพราะเส้นทางนั้นจะพาไปเจอสมการกำลังสามที่แยกตัวประกอบยาก '
        'ทั้งที่วิธีมุมประกอบใช้บรรทัดเดียวก็จบ',
        '• มีลูกเล่นตรวจเร็วสำหรับสมการรูป $\\sin(ax) = \\cos(bx)$ คือลองให้ผลบวกของมุมเท่ากับ '
        '$\\dfrac{\\pi}{2}$ ตรง ๆ นั่นคือแก้ $ax + bx = \\dfrac{\\pi}{2}$ '
        'ข้อนี้ให้ $5x = \\dfrac{\\pi}{2}$ ⇒ $x = \\dfrac{\\pi}{10}$ ทันที '
        'ใช้เดาคำตอบล่วงหน้าได้ แต่ยังต้องเดินวงศ์ที่สองเพื่อยืนยันว่าไม่มีอะไรเล็กกว่า',
        '• คำว่า “เล็กที่สุด” ในโจทย์เป็นสัญญาณว่าต้องมีของให้เทียบมากกว่าหนึ่งชิ้น '
        'ถ้าคิดแล้วมีชิ้นเดียวให้เทียบ แปลว่าน่าจะหาวงศ์คำตอบมาไม่ครบ ให้ย้อนกลับไปดูขั้นที่เปิดสองกรณี',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\dfrac{\\pi}{6}$ เพราะเลือกเดินทางพหุนาม แล้วแยกตัวประกอบผิด · '
        'กระจายได้ถูกจนถึง $4\\sin^3 x - 2\\sin^2 x - 3\\sin x + 1 = 0$ '
        'แล้วเดาว่าแยกเป็น $(2\\sin x - 1)(2\\sin^2 x - 1) = 0$ จึงสรุปว่า $\\sin x = \\dfrac{1}{2}$ '
        'และตอบ $x = \\dfrac{\\pi}{6}$ · แต่กระจายกลับดูจะเห็นว่า '
        '$(2\\sin x - 1)(2\\sin^2 x - 1) = 4\\sin^3 x - 2\\sin^2 x - 2\\sin x + 1$ '
        'ซึ่งพจน์กลางเป็น $-2\\sin x$ ไม่ใช่ $-3\\sin x$ ⇒ แยกผิดตั้งแต่ต้น · '
        'ค่านี้ผิดจริง ตรวจได้ด้วยการแทนกลับลงสมการเดิม : '
        '$\\sin\\dfrac{\\pi}{2} - \\cos\\dfrac{\\pi}{3} = 1 - \\dfrac{1}{2} = \\dfrac{1}{2}$ '
        'ซึ่งไม่เป็นศูนย์',
        '• ได้ค่า $\\dfrac{\\pi}{5}$ เพราะจำเอกลักษณ์มุมประกอบผิด ไปใช้ผลบวกมุมเป็น $\\pi$ '
        'แทนที่จะเป็น $\\dfrac{\\pi}{2}$ คือเขียนว่า $\\cos 2x = \\sin(\\pi - 2x)$ '
        'แล้วได้ $3x = \\pi - 2x$ ⇒ $5x = \\pi$ ⇒ $x = \\dfrac{\\pi}{5}$ · '
        'สูตรนี้ผิดเพราะ $\\sin(\\pi - \\theta) = \\sin\\theta$ ต่างหาก ไม่ใช่ $\\cos\\theta$ · '
        'ค่านี้ผิดจริง แทนกลับแล้วได้ $\\sin\\dfrac{3\\pi}{5} - \\cos\\dfrac{2\\pi}{5} '
        '\\approx 0.951 - 0.309 = 0.642$ ซึ่งห่างจากศูนย์อยู่มาก',
        '• ⭐ ได้ค่า $\\dfrac{\\pi}{2}$ เป็นกับดักที่อันตรายที่สุดของทั้งข้อ เพราะแทนกลับแล้ว'
        '<b>สมการเป็นจริง</b>จริง ๆ : $\\sin\\dfrac{3\\pi}{2} - \\cos\\pi = (-1) - (-1) = 0$ '
        'เด็กที่ตรวจด้วยการแทนกลับอย่างเดียวจึงมั่นใจว่าถูกแล้ว · '
        'ที่มาคือแก้เฉพาะวงศ์ที่สองวงศ์เดียวแล้วหยุด หรือแก้วงศ์แรกแล้วเผลอหยิบ $k = 1$ มาตอบ · '
        'แต่โจทย์ไม่ได้ถามว่าค่าใดเป็นคำตอบ โจทย์ถามค่าบวกที่เล็กที่สุด '
        'และ $\\dfrac{\\pi}{2} \\approx 1.571$ ใหญ่กว่า $\\dfrac{\\pi}{10} \\approx 0.314$ ถึงห้าเท่า '
        'ซึ่ง $\\dfrac{\\pi}{10}$ ก็เป็นคำตอบเหมือนกัน ⇒ บทเรียนคือการแทนกลับพิสูจน์ได้แค่ว่า '
        '“เป็นคำตอบ” ไม่เคยพิสูจน์ว่า “เล็กที่สุด” ต้องมีขั้นเทียบข้ามวงศ์เสมอ',
        '• อีกทางที่พลาดกันบ่อยคือแก้ถูกหมดแต่ตกม้าตายตอนแปลงหน่วย · '
        'คิดในหน่วยองศาว่า $5x$ เท่ากับ 90 องศา จึงได้ $x$ เป็น 18 องศา '
        'แล้วมองหาเลข 18 ในรายการคำตอบที่ให้มาไม่เจอ เลยเดาค่าที่รู้สึกว่าใกล้เคียง '
        'ทั้งที่ $\\dfrac{\\pi}{6}$ คือ 30 องศา และ $\\dfrac{\\pi}{5}$ คือ 36 องศา ซึ่งไม่ใช่ทั้งคู่ · '
        'วิธีกันคือแปลงให้จบก่อนเทียบ : 18 องศา คือ $18 \\times \\dfrac{\\pi}{180} = \\dfrac{\\pi}{10}$ '
        'พอดี',
    ],
    'V.mold: G = a bare equation sin(3x) = cos(2x) over the reals, with no interval and no numerical data '
    '/ A = the smallest positive real satisfying it / M = rewrite the cosine with the co-function '
    'identity so both sides are sines, open the two-family general solution of sin A = sin B, turn each '
    'family into a progression in k, and compare the least positive member of each. '
    'Rubric F3 C2 P2 T2 L0 = 9/15 with total 9, T = 2 and F = 3 -> level: ยาก. '
    'F = 3, the ceiling, because three knowledge blocks are all load bearing: the co-function identity, '
    'the two-family criterion for equal sines, and treating the integer k as a progression to minimise '
    'over. C = 2 and not 3 because 7.7 and 7.5 must genuinely be used together but both sit inside '
    'chapter 7, and the polynomial route that would pull in algebra from elsewhere is ruled out rather '
    'than required. P = 2 and deliberately not 3: stage two reinterprets the two general solutions as '
    'progressions and minimises over them, a real second stage, but it closes with a comparison of two '
    'already-computed numbers rather than a third computation producing a new object; benchmark q086 and '
    'q097. T = 2 because a candidate can satisfy the equation and still be the wrong answer, so '
    'substitution alone is not a proof; not 3 because the stem itself says smallest, which signposts the '
    'comparison and leaves only the discovery of the second family. L = 0 because there is no worded '
    'scene to model at all, benchmarks q030 and q060. Total 9 is short of the 12 needed for ยากมาก and no '
    'dimension was pushed to close that gap. Scoring was written before the level was read off. '
    'sympy (verify_b18.py): confirmation had to run on two tracks, because solveset returns the roots in '
    'an atan form that simplify() will not collapse, so no symbolic equality against pi/10 is available. '
    'Track one is exact: sin(3*pi/10) - cos(2*pi/10) reduces to 0, so pi/10 is a root. Track two attacks '
    'minimality. solveset(sin(3*x) - cos(2*x), x, Interval.open(0, pi)) returns pi/2 together with '
    'atan(sqrt(2)*(-1 + sqrt(5))/(2*sqrt(sqrt(5) + 5))) and pi minus that same atan; the smallest '
    'member, picked by a 40-digit numeric key, evaluates to '
    '0.3141592653589793238462643383279502884197, agreeing with N(pi/10, 40) in all 40 digits, and the '
    'assertion abs(N(lo - pi/10, 40)) < 1e-35 passed. Since a numeric match alone does not exclude a root '
    'lower down, the same track closes the gap: g(x) = sin(3x) - cos(2x) was lambdified and sampled at '
    '3999 equally spaced interior points of (0, pi/10) and every value came out negative, minimum '
    '-0.999764 and maximum -0.000231, so g never reaches zero there. That sign scan is the numerical '
    'shadow of the monotonicity argument used in the independent check, and the two tracks agree. '
    'Distractors were machine-computed: pi/6 leaves residue 1/2, pi/5 leaves 1/4 - sqrt(5)/4 + '
    'sqrt(2*sqrt(5) + 10)/4, about 0.642, and pi/2 was deliberately confirmed to BE a root, '
    'sin(3*pi/2) - cos(pi) = 0, so a separate assertion records that this one is refuted only by the '
    'minimality requirement and never by substitution. '
    'Collision sweep on 6407 items (bank 62 files + k1 out + k2 out), probe collide_b18e.py: the mold of '
    'a sine at one multiple set equal to a cosine at another multiple, asking for the smallest positive '
    'solution, appears nowhere in the corpus; the saturated neighbouring mold is asking for the sum of '
    'all solutions inside a stated interval, 77 items, which this item avoids by leaving the interval '
    'open above and asking for a minimum instead of a sum. Choices are ordered ascending by numeric value '
    '(pi/10 about 0.314, then pi/6 about 0.524, then pi/5 about 0.628, then pi/2 about 1.571), so the '
    'answer slot is forced by that rule and was not chosen.',
)

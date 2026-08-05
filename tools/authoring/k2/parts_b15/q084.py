# -*- coding: utf-8 -*-
add(
    84,
    ['7.9', '7.11'],
    'ยากมาก',
    'รูปสามเหลี่ยม $ABC$ แนบในวงกลมวงหนึ่ง โดยที่ $AB = 8$ หน่วย $AC = 5$ หน่วย '
    'รูปสามเหลี่ยม $ABC$ มีพื้นที่ $10\\sqrt{3}$ ตารางหน่วย และ $BC < AB$ '
    'แล้วความยาวของส่วนโค้ง $BC$ ที่ไม่มีจุด $A$ อยู่บนส่วนโค้งนั้น มีหน่วยเป็นหน่วยความยาว '
    'เท่ากับข้อใด',
    [
        '$\\dfrac{7\\sqrt{3}}{3}$',
        '$\\dfrac{7\\sqrt{3}\\pi}{9}$',
        '$7$',
        '$\\dfrac{14\\sqrt{3}\\pi}{9}$',
    ],
    3,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• พื้นที่ของรูปสามเหลี่ยมเมื่อรู้ด้านสองด้านกับมุมระหว่างด้านทั้งสอง : '
        'พื้นที่ $= \\dfrac{1}{2} \\times bc \\times \\sin A$ '
        'โดย $b$ กับ $c$ เป็นด้านที่ประกอบมุม $A$',
        '• มุมภายในของรูปสามเหลี่ยมต้องอยู่ในช่วง $0 < A < \\pi$ '
        'ในช่วงนี้ค่าไซน์ค่าหนึ่งให้มุมได้<b>สองมุม</b>เสมอ ยกเว้นกรณีที่ไซน์เท่ากับ $1$ '
        'สองมุมนั้นคือมุมแหลมมุมหนึ่งกับมุมป้านที่เป็นมุมประกอบสองมุมฉากของมุมแหลมนั้น',
        '• กฎของโคไซน์ : $a^2 = b^2 + c^2 - 2bc\\cos A$ '
        'ใช้หาด้านที่อยู่ตรงข้ามมุมที่รู้ค่า',
        '• กฎของไซน์ฉบับขยาย : $\\dfrac{a}{\\sin A} = 2R$ '
        'โดย $R$ เป็นรัศมีของวงกลมที่ล้อมรอบรูปสามเหลี่ยมนั้น',
        '• ทฤษฎีมุมในส่วนโค้ง : มุมที่จุดศูนย์กลางของวงกลมมีขนาดเป็นสองเท่าของมุมในส่วนโค้ง '
        'เมื่อทั้งสองมุมรองรับส่วนโค้งเดียวกัน',
        '• ความยาวส่วนโค้ง : $s = r\\gamma$ เมื่อ $\\gamma$ เป็นขนาดของมุมที่จุดศูนย์กลางในหน่วยเรเดียน',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• รูปสามเหลี่ยม $ABC$ มีจุดยอดทั้งสามอยู่บนวงกลมวงเดียวกัน',
        '• $AB = 8$ หน่วย และ $AC = 5$ หน่วย ซึ่งเป็นด้านสองด้านที่ประกอบมุม $A$',
        '• พื้นที่ของรูปสามเหลี่ยม $ABC$ เท่ากับ $10\\sqrt{3}$ ตารางหน่วย',
        '• $BC < AB$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาความยาวของส่วนโค้ง $BC$ ด้านที่ไม่มีจุด $A$ อยู่บนส่วนโค้งนั้น',
        '',
        '<b>【 ถอยจากพื้นที่กลับไปหามุม $A$ ซึ่งได้สองกิ่ง แล้วใช้เงื่อนไขความยาวด้านคัดกิ่ง '
        'จากนั้นเดินต่อไปยังรัศมี มุมที่จุดศูนย์กลาง และความยาวส่วนโค้ง 】</b>',
        '',
        '<b>ขั้นที่ 1 · ถอยจากพื้นที่กลับไปหาค่าไซน์ของมุม $A$</b>',
        '• ด้าน $AB$ กับ $AC$ เป็นด้านสองด้านที่ประกอบมุม $A$ พอดี '
        'จึงใช้สูตรพื้นที่ที่มีมุมระหว่างด้านได้ทันที',
        '• แทนค่า : $\\dfrac{1}{2} \\times 5 \\times 8 \\times \\sin A = 10\\sqrt{3}$',
        '• ยุบสัมประสิทธิ์ข้างซ้าย : $20\\sin A = 10\\sqrt{3}$',
        '• หารด้วย $20$ : $\\sin A = \\dfrac{\\sqrt{3}}{2}$',
        '',
        '<b>ขั้นที่ 2 · แตกกิ่งของมุม $A$ แล้วคำนวณด้าน $BC$ ของทั้งสองกิ่ง</b>',
        '• ⛔ กุญแจดอกแรก มุมภายในรูปสามเหลี่ยมอยู่ในช่วง $0 < A < \\pi$ '
        'และในช่วงนี้ $\\sin A = \\dfrac{\\sqrt{3}}{2}$ ให้มุมได้สองมุม คือ '
        '$A = \\dfrac{\\pi}{3}$ และ $A = \\dfrac{2\\pi}{3}$ '
        'การหยิบมุมแหลมมาใช้เลยโดยไม่พิจารณามุมป้านเป็นการข้ามขั้น แม้จะบังเอิญได้คำตอบถูกก็ตาม',
        '• กิ่งที่หนึ่ง $A = \\dfrac{\\pi}{3}$ ใช้กฎของโคไซน์ : '
        '$BC^2 = 5^2 + 8^2 - 2 \\times 5 \\times 8 \\times \\cos\\dfrac{\\pi}{3} '
        '= 25 + 64 - 80 \\times \\dfrac{1}{2} = 89 - 40 = 49$ '
        'จึงได้ $BC = 7$',
        '• กิ่งที่สอง $A = \\dfrac{2\\pi}{3}$ ใช้กฎของโคไซน์ : '
        '$BC^2 = 25 + 64 - 80 \\times \\left(-\\dfrac{1}{2}\\right) = 89 + 40 = 129$ '
        'จึงได้ $BC = \\sqrt{129}$ ซึ่งมีค่าประมาณ $11.36$',
        '',
        '<b>ขั้นที่ 3 · ใช้เงื่อนไขที่โจทย์ให้คัดกิ่งที่ใช้ไม่ได้</b>',
        '• ⛔ กุญแจดอกที่สอง เงื่อนไข $BC < AB$ ใช้ทันทีไม่ได้ '
        'ต้องคำนวณ $BC$ ของทั้งสองกิ่งออกมาก่อนจึงเปรียบเทียบได้',
        '• กิ่งที่หนึ่งให้ $BC = 7$ ซึ่งน้อยกว่า $AB = 8$ จริง จึงเก็บไว้',
        '• กิ่งที่สองให้ $BC = \\sqrt{129} \\approx 11.36$ ซึ่งมากกว่า $8$ จึงตัดทิ้ง',
        '• มีทางลัดที่เร็วกว่า ถ้ามุม $A$ เป็นมุมป้าน ด้านที่อยู่ตรงข้ามมุม $A$ คือ $BC$ '
        'จะต้องเป็นด้านที่ยาวที่สุดของรูปสามเหลี่ยม ซึ่งขัดกับเงื่อนไข $BC < AB$ ทันที '
        'จึงตัดกิ่งมุมป้านได้โดยไม่ต้องคำนวณเลย',
        '• สรุปว่า $A = \\dfrac{\\pi}{3}$ และ $BC = 7$ หน่วย',
        '',
        '<b>ขั้นที่ 4 · หารัศมีของวงกลมที่ล้อมรอบด้วยกฎของไซน์ฉบับขยาย</b>',
        '• ด้าน $BC$ อยู่ตรงข้ามมุม $A$ จึงจับคู่กันได้ในกฎของไซน์ : '
        '$\\dfrac{BC}{\\sin A} = 2R$',
        '• แทนค่า : $2R = \\dfrac{7}{\\ \\dfrac{\\sqrt{3}}{2}\\ } = \\dfrac{14}{\\sqrt{3}}$',
        '• จึงได้ $R = \\dfrac{7}{\\sqrt{3}} = \\dfrac{7\\sqrt{3}}{3}$ หน่วย',
        '',
        '<b>ขั้นที่ 5 · หามุมที่จุดศูนย์กลางแล้วคำนวณความยาวส่วนโค้ง</b>',
        '• ⛔ กุญแจดอกที่สาม มุม $A$ เป็นมุมในส่วนโค้งที่รองรับส่วนโค้ง $BC$ ด้านที่ไม่มีจุด $A$ '
        'มุมที่จุดศูนย์กลางซึ่งรองรับส่วนโค้งเดียวกันจึงมีขนาดเป็นสองเท่าของมุม $A$ '
        'นั่นคือ $\\gamma = 2A = \\dfrac{2\\pi}{3}$ ⛔ ไม่ใช่ $\\dfrac{\\pi}{3}$',
        '• ใช้สูตรความยาวส่วนโค้ง : '
        '$s = R\\gamma = \\dfrac{7\\sqrt{3}}{3} \\times \\dfrac{2\\pi}{3} '
        '= \\dfrac{14\\sqrt{3}\\pi}{9}$ หน่วย',
        '• ค่าประมาณคือ $8.46$ หน่วย',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ตรวจย้อนจากวงกลมกลับมาหาคอร์ด '
        'โดยไม่ใช้กฎของโคไซน์และไม่ใช้สูตรพื้นที่เลย)</b>',
        '• บนวงกลมรัศมี $R$ คอร์ดที่รองรับมุมที่จุดศูนย์กลางขนาด $\\gamma$ มีความยาวเท่ากับ '
        '$2R\\sin\\dfrac{\\gamma}{2}$ ซึ่งเป็นสูตรที่ได้จากการลากรัศมีสองเส้นแล้วแบ่งครึ่งมุม',
        '• แทนค่าที่หามาได้ : '
        '$2 \\times \\dfrac{7\\sqrt{3}}{3} \\times \\sin\\dfrac{\\pi}{3} '
        '= \\dfrac{14\\sqrt{3}}{3} \\times \\dfrac{\\sqrt{3}}{2} = \\dfrac{14 \\times 3}{6} = 7$',
        '• คอร์ดที่คำนวณย้อนกลับมาได้ยาว $7$ หน่วย ตรงกับด้าน $BC$ ที่หาไว้พอดี '
        'แสดงว่ารัศมีกับมุมที่จุดศูนย์กลางที่ใช้ถูกต้องทั้งคู่',
        '• ตรวจขนาดอีกสองชั้น หนึ่ง ส่วนโค้งต้องยาวกว่าคอร์ดที่รองรับเสมอ '
        'ซึ่ง $8.46$ มากกว่า $7$ จริง สอง ส่วนโค้งต้องสั้นกว่าเส้นรอบวงทั้งวง '
        'ซึ่งเท่ากับ $2\\pi R \\approx 25.4$ และ $8.46$ ก็น้อยกว่าจริง '
        'อีกทั้งมุมที่จุดศูนย์กลางเท่ากับหนึ่งในสามของหนึ่งรอบพอดี '
        'ส่วนโค้งจึงต้องยาวเท่ากับหนึ่งในสามของเส้นรอบวง คือประมาณ $8.46$ ตรงตามที่คำนวณได้',
        '',
        '✅ <b>คำตอบ</b> $\\dfrac{14\\sqrt{3}\\pi}{9}$ → <b>ตัวเลือก 4</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เมื่อโจทย์ให้พื้นที่ของรูปสามเหลี่ยมมาเป็นข้อมูลตั้งต้นแทนที่จะให้มุมมาตรง ๆ '
        'แปลว่าโจทย์กำลังซ่อนการแตกกิ่งไว้ เพราะการถอยจากพื้นที่กลับไปได้แค่ค่าไซน์ '
        'และค่าไซน์หนึ่งค่าให้มุมภายในรูปสามเหลี่ยมได้สองมุมเสมอ '
        'ให้เขียนทั้งสองกิ่งลงกระดาษก่อน แล้วค่อยหาเงื่อนไขในโจทย์มาคัด',
        '• เงื่อนไขที่ใช้คัดกิ่งได้เร็วที่สุดคือความสัมพันธ์ระหว่างขนาดของมุมกับความยาวของด้าน '
        'ในรูปสามเหลี่ยมใด ๆ ด้านที่ยาวกว่าจะอยู่ตรงข้ามมุมที่ใหญ่กว่าเสมอ '
        'ดังนั้นถ้ามุมใดเป็นมุมป้าน ด้านตรงข้ามมุมนั้นต้องเป็นด้านที่ยาวที่สุดทันที',
        '• เวลาข้ามจากรูปสามเหลี่ยมไปหาวงกลมที่ล้อมรอบ ให้จำสองสะพานนี้คู่กันเสมอ '
        'สะพานแรกคือกฎของไซน์ฉบับขยายที่พาไปหารัศมี '
        'สะพานที่สองคือทฤษฎีมุมในส่วนโค้งที่เปลี่ยนมุมของรูปสามเหลี่ยมให้เป็นมุมที่จุดศูนย์กลาง '
        'ขาดสะพานใดสะพานหนึ่งก็เดินไปถึงความยาวส่วนโค้งไม่ได้',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $\\dfrac{7\\sqrt{3}}{3}$ เพราะหยุดที่รัศมีแล้วคิดว่าจบ '
        'ค่านี้คือ $R$ ซึ่งเป็นเพียงผลลัพธ์กลางทาง ยังไม่ได้คูณด้วยขนาดของมุมที่จุดศูนย์กลาง '
        'สังเกตหน่วยและรูปพีชคณิตช่วยได้ ความยาวส่วนโค้งของมุมที่ไม่ใช่มุมพิเศษเชิงเส้น '
        'ต้องมี $\\pi$ ติดอยู่ในคำตอบเสมอ ค่าที่ไม่มี $\\pi$ จึงยังไม่ใช่ความยาวส่วนโค้ง',
        '• ได้ $\\dfrac{7\\sqrt{3}\\pi}{9}$ เพราะลืมทฤษฎีมุมในส่วนโค้ง '
        'คือนำมุม $A = \\dfrac{\\pi}{3}$ ไปคูณกับรัศมีโดยตรงเป็น '
        '$\\dfrac{7\\sqrt{3}}{3} \\times \\dfrac{\\pi}{3}$ '
        'มุม $A$ เป็นมุมที่จุดยอด $A$ ซึ่งอยู่บนเส้นรอบวง ไม่ใช่มุมที่จุดศูนย์กลาง '
        'สูตร $s = r\\gamma$ ใช้ได้กับมุมที่จุดศูนย์กลางเท่านั้น '
        'ตัวตรวจที่จับความพลาดนี้ได้คือเทียบส่วนโค้งกับคอร์ด ค่านี้ประมาณ $4.23$ '
        'ซึ่งสั้นกว่าคอร์ด $BC = 7$ เป็นไปไม่ได้ในทางเรขาคณิต',
        '• ได้ $7$ เพราะตอบความยาวคอร์ด $BC$ แทนความยาวส่วนโค้ง '
        'คอร์ดคือส่วนของเส้นตรงที่เชื่อมจุด $B$ กับจุด $C$ ส่วนส่วนโค้งคือทางโค้งไปตามวงกลม '
        'สองสิ่งนี้ต่างกันเสมอ และส่วนโค้งยาวกว่าคอร์ดทุกกรณี '
        'ให้อ่านคำถามซ้ำก่อนวงคำตอบว่าถามระยะตรงหรือถามระยะตามส่วนโค้ง',
        '• ได้คำตอบที่ถูกโดยบังเอิญแต่กระบวนการไม่ครบ เกิดกับผู้ที่หยิบ $A = \\dfrac{\\pi}{3}$ '
        'ทันทีโดยไม่พิจารณากิ่งมุมป้าน ข้อนี้กิ่งที่ถูกคัดออกเป็นกิ่งมุมป้านพอดี '
        'แต่ถ้าโจทย์เปลี่ยนเงื่อนไขเป็น $BC > AB$ คำตอบจะกลายเป็นอีกกิ่งหนึ่งทันที '
        'การเขียนทั้งสองกิ่งแล้วคัดด้วยเงื่อนไขจึงเป็นขั้นตอนที่ข้ามไม่ได้',
    ],
    'V.mold: G = a triangle inscribed in a circle with two sides and the area given, plus an inequality '
    'comparing the third side with one of the given sides / A = the length of the arc BC not containing A / '
    'M = recover sin A from the area formula, branch into the two interior angles that share that sine, '
    'compute the third side on both branches with the law of cosines, discriminate with the given inequality, '
    'then cross to the circle through the extended law of sines and the inscribed-angle theorem before '
    'applying the arc-length formula. '
    'Rubric F3 C3 P2 T3 L1 = 12/15 with total at least 12 and T = 3 -> level: ยากมาก. '
    'Honesty note on the grading: the first draft of this slot handed the angle A = 60 degrees directly and '
    'scored F3 C2 P2 T2 L1 = 10, which is ยาก and not ยากมาก. Rather than pushing L from 1 to 2 or T from 2 '
    'to 3 to fit the plan, the question itself was redesigned so that the angle is hidden behind the area, '
    'which creates a real two-branch ambiguity and a genuine third turning point. This follows order 4 of '
    'letter E to MB number 19, that ยากมาก is a product of how the item is built and not a property of the '
    'chapter. L is graded 1 and not 2 because the figure is planar, following the precedent set by q077. '
    'sympy (verify_b15.py): solving (1/2)*5*8*x = 10*sqrt(3) returns sin A = sqrt(3)/2; solveset over the '
    'open interval (0, pi) returns exactly the two branches pi/3 and 2*pi/3, which is the structural heart of '
    'the item; the law of cosines gives BC = 7 on the first branch and BC = sqrt(129) which is about 11.3578 '
    'on the second, and the filter BC < AB = 8 leaves exactly one branch; R = a/(2 sin A) returns '
    '7*sqrt(3)/3, the central angle 2A returns 2*pi/3, and the arc length R*gamma returns 14*sqrt(3)*pi/9. '
    'Three independent checks confirm the geometry: the chord subtending the central angle 2*pi/3 on a circle '
    'of that radius comes back to exactly 7, the arc is longer than the chord, and the arc is shorter than '
    'the full circumference. All three distractors machine-computed from named error paths: 7*sqrt(3)/3 from '
    'stopping at the radius, 7*sqrt(3)*pi/9 from using A itself as the central angle instead of 2A, and 7 '
    'from answering the chord instead of the arc. '
    'Collision sweep on 6392 items (bank 62 files + k1 out + k2 out), probe collide_b15e.py with no chapter '
    'filter: giving the area of a triangle as input data rather than as the question returns 1 hit which is a '
    'three-dimensional chapter 9 item and not a collision; a side-comparison condition of the form XY < ZW in '
    'a stem returns 0 hits anywhere in the corpus, so the discriminating device is genuinely new. The nearest '
    'neighbours are chap-07-trigonometry-q122, which gives the area together with an angle stated directly '
    'and asks for a side with no branching at all, and our own gen-chap-07-trigonometry-q069, which gives BC '
    'and the angle A and asks for a range of the perimeter; neither shares the given, the asked, or the '
    'machinery.',
)

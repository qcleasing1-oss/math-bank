# -*- coding: utf-8 -*-
add(
    72,
    ['7.9'],
    'ปานกลาง',
    'กำหนดให้สามเหลี่ยม $ABC$ มีด้าน $AB$ ยาว $5$ หน่วย ด้าน $AC$ ยาว $6$ หน่วย '
    'และมุม $A$ มีขนาด $\\dfrac{2\\pi}{3}$ เรเดียน ถ้า $M$ เป็นจุดกึ่งกลางของด้าน $AC$ '
    'แล้วความยาวของ $BM$ เท่ากับข้อใด',
    [
        '$7$',
        '$\\sqrt{19}$',
        '$\\sqrt{34}$',
        '$\\sqrt{91}$',
    ],
    0,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• กฎของโคไซน์ : ในสามเหลี่ยมที่ทราบด้านสองด้านและมุมที่อยู่ระหว่างด้านทั้งสองนั้น '
        'ด้านที่สามหาได้จาก $(\\text{ด้านตรงข้ามมุมที่ให้})^2 = '
        '(\\text{ด้านที่หนึ่ง})^2 + (\\text{ด้านที่สอง})^2 - 2(\\text{ด้านที่หนึ่ง})(\\text{ด้านที่สอง})\\cos(\\text{มุมที่ให้})$',
        '• จุดกึ่งกลางของส่วนของเส้นตรงแบ่งส่วนของเส้นตรงนั้นออกเป็นสองส่วนที่ยาวเท่ากัน '
        'ดังนั้นถ้า $M$ เป็นจุดกึ่งกลางของ $AC$ แล้ว $AM = MC = \\dfrac{1}{2}AC$',
        '• มุมขนาด $\\dfrac{2\\pi}{3}$ เรเดียน คือมุม $120^{\\circ}$ ซึ่งเป็นมุมป้าน '
        'และ $\\cos \\dfrac{2\\pi}{3} = -\\dfrac{1}{2}$ เพราะมุมนี้อยู่ในจตุภาคที่สอง '
        'มีมุมอ้างอิงเป็น $\\dfrac{\\pi}{3}$ และโคไซน์ในจตุภาคที่สองมีค่าเป็นลบ',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• สามเหลี่ยม $ABC$ มี $AB = 5$ หน่วย และ $AC = 6$ หน่วย',
        '• มุม $A$ ซึ่งเป็นมุมระหว่างด้าน $AB$ กับด้าน $AC$ มีขนาด $\\dfrac{2\\pi}{3}$ เรเดียน',
        '• $M$ เป็นจุดกึ่งกลางของด้าน $AC$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาความยาวของส่วนของเส้นตรง $BM$',
        '',
        '<b>【 ย้ายสายตาจากสามเหลี่ยมใหญ่ $ABC$ ไปที่สามเหลี่ยมย่อย $ABM$ ที่ใช้มุม $A$ ร่วมกัน '
        'แล้วใช้กฎของโคไซน์ครั้งเดียว 】</b>',
        '',
        '<b>ขั้นที่ 1 · เลือกสามเหลี่ยมที่มี $BM$ เป็นด้านหนึ่ง แล้วดูว่ารู้อะไรครบหรือยัง</b>',
        '• ส่วนของเส้นตรง $BM$ เป็นด้านหนึ่งของสามเหลี่ยม $ABM$ ซึ่งมีจุดยอดคือ $A$ , $B$ และ $M$',
        '• ในสามเหลี่ยม $ABM$ นี้ ด้าน $AB$ ยาว $5$ หน่วยตามที่โจทย์ให้มาโดยตรง',
        '• มุมที่จุด $A$ ของสามเหลี่ยม $ABM$ คือมุมระหว่างรังสี $AB$ กับรังสี $AM$ '
        'ซึ่ง $M$ อยู่บนด้าน $AC$ พอดี รังสี $AM$ จึงเป็นรังสีเดียวกับรังสี $AC$ '
        'มุมนี้จึงเท่ากับมุม $A$ ของสามเหลี่ยมใหญ่ นั่นคือ $\\dfrac{2\\pi}{3}$ เรเดียน',
        '• เหลือเพียงด้าน $AM$ ที่ยังไม่รู้ค่า ซึ่งหาได้จากเงื่อนไขจุดกึ่งกลาง',
        '',
        '<b>ขั้นที่ 2 · ใช้เงื่อนไขจุดกึ่งกลางหาความยาว $AM$</b>',
        '• $M$ เป็นจุดกึ่งกลางของ $AC$ ดังนั้น $AM = \\dfrac{1}{2}AC$',
        '• แทนค่า $AC = 6$ หน่วย : $AM = \\dfrac{1}{2} \\times 6 = 3$ หน่วย',
        '• ⚠️ ตรงนี้คือจุดตัดสินของข้อ ต้องใช้ $AM = 3$ ⛔ ไม่ใช่ $AC = 6$',
        '',
        '<b>ขั้นที่ 3 · ใช้กฎของโคไซน์ในสามเหลี่ยม $ABM$</b>',
        '• เขียนสูตรให้ตรงกับด้านที่ต้องการก่อน โดย $BM$ อยู่ตรงข้ามมุม $A$ : '
        '$BM^2 = AB^2 + AM^2 - 2(AB)(AM)\\cos A$',
        '• แทนค่าที่มีครบแล้ว : $BM^2 = 5^2 + 3^2 - 2(5)(3)\\cos \\dfrac{2\\pi}{3}$',
        '• แทนค่าโคไซน์ของมุมป้าน : $\\cos \\dfrac{2\\pi}{3} = -\\dfrac{1}{2}$ '
        'จะได้ $BM^2 = 25 + 9 - 30 \\times \\left(-\\dfrac{1}{2}\\right)$',
        '• จัดการเครื่องหมาย ลบกับลบกลายเป็นบวก : $BM^2 = 25 + 9 + 15 = 49$',
        '',
        '<b>ขั้นที่ 4 · ถอดรากที่สอง</b>',
        '• ความยาวของส่วนของเส้นตรงต้องเป็นจำนวนบวก จึงเลือกรากบวกเพียงค่าเดียว',
        '• $BM = \\sqrt{49} = 7$ หน่วย',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · วางระบบพิกัดฉากแล้วใช้สูตรระยะห่างระหว่างจุด)</b>',
        '• วางจุด $A$ ไว้ที่จุดกำเนิด $(0, 0)$ และวางด้าน $AB$ ไปตามแกน $X$ ทางบวก '
        'จะได้ $B$ อยู่ที่ $(5, 0)$',
        '• จุด $C$ อยู่ห่างจาก $A$ เป็นระยะ $6$ หน่วย ในทิศที่ทำมุม $\\dfrac{2\\pi}{3}$ กับแกน $X$ '
        'ทางบวก จึงได้ $C = \\left(6\\cos \\dfrac{2\\pi}{3} ,\\ 6\\sin \\dfrac{2\\pi}{3}\\right) = '
        '\\left(6 \\times \\left(-\\dfrac{1}{2}\\right) ,\\ 6 \\times \\dfrac{\\sqrt{3}}{2}\\right) = '
        '(-3 ,\\ 3\\sqrt{3})$',
        '• ตรวจว่าพิกัดนี้ถูกต้องจริง : $AC = \\sqrt{(-3)^2 + (3\\sqrt{3})^2} = \\sqrt{9 + 27} = '
        '\\sqrt{36} = 6$ ตรงกับที่โจทย์ให้',
        '• จุดกึ่งกลาง $M$ ของ $AC$ หาได้จากค่าเฉลี่ยของพิกัดปลายทั้งสอง : '
        '$M = \\left(\\dfrac{0 + (-3)}{2} ,\\ \\dfrac{0 + 3\\sqrt{3}}{2}\\right) = '
        '\\left(-\\dfrac{3}{2} ,\\ \\dfrac{3\\sqrt{3}}{2}\\right)$',
        '• ใช้สูตรระยะห่างระหว่างจุด $B$ กับ $M$ : '
        '$BM^2 = \\left(5 - \\left(-\\dfrac{3}{2}\\right)\\right)^2 + '
        '\\left(0 - \\dfrac{3\\sqrt{3}}{2}\\right)^2 = '
        '\\left(\\dfrac{13}{2}\\right)^2 + \\dfrac{27}{4} = \\dfrac{169}{4} + \\dfrac{27}{4} = '
        '\\dfrac{196}{4} = 49$',
        '• ได้ $BM = 7$ หน่วย ตรงกับคำตอบที่หามาได้ โดยวิธีนี้ไม่ได้ใช้กฎของโคไซน์เลย',
        '',
        '✅ <b>คำตอบ</b> $7$ → <b>ตัวเลือก 1</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เมื่อโจทย์พูดถึงจุดกึ่งกลางของด้านใดด้านหนึ่ง ให้รีบวาดสามเหลี่ยมย่อยที่มีจุดนั้นเป็นจุดยอด '
        'แล้วถามตัวเองว่าในสามเหลี่ยมย่อยนั้นรู้ครบ “สองด้านกับมุมที่อยู่ระหว่างกลาง” หรือยัง '
        'ถ้าครบก็ใช้กฎของโคไซน์ได้ทันทีโดยไม่ต้องจำสูตรเส้นมัธยฐานใด ๆ',
        '• ประมาณคำตอบไว้กันพลาด : มุม $A$ เป็นมุมป้าน ด้านตรงข้ามมุมป้านย่อมยาวกว่าด้านประกอบทั้งสอง '
        'ดังนั้น $BM$ ต้องมากกว่า $5$ แน่นอน และในทางกลับกันด้านของสามเหลี่ยมต้องน้อยกว่าผลบวก '
        'ของอีกสองด้าน คือน้อยกว่า $5 + 3 = 8$ คำตอบจึงอยู่ระหว่าง $5$ กับ $8$',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $\\sqrt{91}$ เพราะลืมเงื่อนไขจุดกึ่งกลาง แล้วใช้ $AC = 6$ เต็มความยาวแทน $AM = 3$ '
        'ได้ $25 + 36 + 30 = 91$ ค่านี้ที่จริงคือความยาวของด้าน $BC$ ไม่ใช่ $BM$',
        '• ได้ $\\sqrt{19}$ เพราะใช้ $\\cos \\dfrac{2\\pi}{3} = +\\dfrac{1}{2}$ '
        'ทำให้พจน์สุดท้ายกลายเป็นลบ ได้ $25 + 9 - 15 = 19$ '
        'ให้จำว่ามุมป้านอยู่ในจตุภาคที่สองซึ่งโคไซน์ติดลบเสมอ',
        '• ได้ $\\sqrt{34}$ เพราะตัดพจน์ $-2(AB)(AM)\\cos A$ ทิ้ง ราวกับว่ามุม $A$ เป็นมุมฉาก '
        'ได้ $25 + 9 = 34$ ทฤษฎีบทพีทาโกรัสใช้ได้เฉพาะเมื่อมุมระหว่างด้านทั้งสองเป็นมุมฉากเท่านั้น',
    ],
    'V.mold: G = a triangle given by two sides and the included obtuse angle in radian form, plus a midpoint '
    'named on one of those two sides / A = the length of the segment from the opposite vertex to that midpoint '
    '/ M = restrict attention to the sub-triangle ABM, which shares the given angle, and apply the law of '
    'cosines once — deliberately without the ready-made median-length formula. Rubric F1 C1 P1 T1 L0 = 4/15 '
    '-> level: ปานกลาง. sympy (verify_b13.py): route 1 gives BM^2 = 49 so BM = 7; route 2 is independent of the '
    'law of cosines entirely — it places A at the origin and B at (5, 0), computes C = (-3, 3*sqrt(3)), checks '
    '|AC| = 6, takes M as the coordinate midpoint, and the distance formula returns BM^2 = 49 again. All three '
    'distractors machine-computed from named error paths: sqrt(91) from using the full AC = 6 instead of '
    'AM = 3 (this value is genuinely BC, so the wrong answer is a real quantity in the figure, which is what '
    'makes it tempting), sqrt(19) from the sign error cos(2pi/3) = +1/2, sqrt(34) from dropping the cosine '
    'term as if angle A were right. A guard asserts that the estimation bound quoted in the เทคนิค block '
    '(5 < BM < 8) leaves sqrt(34) alive, so the bound narrows the field but does not decide the item by itself. '
    'Collision sweep on 6382 items (bank 62 files + k1 + k2 out): the pairing of a named midpoint with the law '
    'of cosines returns 0 hits, and a direct sweep for the word median across the whole bank without any '
    'chapter filter also returns 0 hits in a triangle-solving context. Redesign history: an earlier draft asked '
    'for the median length using the standard median formula, which would have made the item a formula-recall '
    'exercise; moving to the sub-triangle route keeps the conceptual step (seeing that the given angle survives '
    'into the sub-triangle) that the C = 1 score is paid for.',
)

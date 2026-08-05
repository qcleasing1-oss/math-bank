# -*- coding: utf-8 -*-
add(
    75,
    ['7.1', '7.10'],
    'ปานกลาง',
    'บันไดอันหนึ่งยาว $8$ เมตร วางพาดกับกำแพงซึ่งตั้งฉากกับพื้นราบ '
    'โดยปลายล่างของบันไดวางอยู่บนพื้นราบ ปลายบนของบันไดพิงอยู่กับกำแพง '
    'และตัวบันไดทำมุมขนาด $60^{\\circ}$ กับพื้นราบ '
    'แล้วปลายบนของบันไดอยู่สูงจากพื้นราบ มีหน่วยเป็นเมตร เท่ากับข้อใด',
    [
        '$4$',
        '$4\\sqrt{2}$',
        '$4\\sqrt{3}$',
        '$8\\sqrt{3}$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ในสามเหลี่ยมมุมฉาก เมื่อเลือกมุมแหลมมุมหนึ่งมาเป็นมุมอ้างอิง ด้านทั้งสามจะมีชื่อเรียกดังนี้ '
        'ด้านตรงข้ามมุมฉากคือด้านที่ยาวที่สุด · ด้านตรงข้ามมุมอ้างอิง · และด้านประชิดมุมอ้างอิง',
        '• อัตราส่วนตรีโกณมิติของมุมอ้างอิง $\\theta$ '
        'คือ $\\sin\\theta = \\dfrac{\\text{ด้านตรงข้ามมุม}}{\\text{ด้านตรงข้ามมุมฉาก}}$ , '
        '$\\cos\\theta = \\dfrac{\\text{ด้านประชิดมุม}}{\\text{ด้านตรงข้ามมุมฉาก}}$ และ '
        '$\\tan\\theta = \\dfrac{\\text{ด้านตรงข้ามมุม}}{\\text{ด้านประชิดมุม}}$',
        '• ค่าที่มุมพิเศษที่ต้องใช้ : $\\sin 60^{\\circ} = \\dfrac{\\sqrt{3}}{2}$ , '
        '$\\cos 60^{\\circ} = \\dfrac{1}{2}$ และ $\\tan 60^{\\circ} = \\sqrt{3}$',
        '• ทฤษฎีบทพีทาโกรัส : ในสามเหลี่ยมมุมฉาก กำลังสองของด้านตรงข้ามมุมฉาก '
        'เท่ากับผลบวกของกำลังสองของด้านประกอบมุมฉากทั้งสอง',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• บันไดเป็นแนวตรง ยาว $8$ เมตร',
        '• กำแพงตั้งฉากกับพื้นราบ ปลายล่างของบันไดอยู่บนพื้นราบ ปลายบนพิงกำแพง',
        '• บันไดทำมุมขนาด $60^{\\circ}$ กับพื้นราบ',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาความสูงจากพื้นราบขึ้นไปถึงปลายบนของบันได มีหน่วยเป็นเมตร',
        '',
        '<b>【 มองบันไดเป็นด้านตรงข้ามมุมฉาก แล้วเลือกอัตราส่วนตรีโกณจากตำแหน่งของด้านที่โจทย์ถาม 】</b>',
        '',
        '<b>ขั้นที่ 1 · วาดรูปและตั้งชื่อจุดทั้งสาม</b>',
        '• ให้ $A$ เป็นจุดที่ปลายล่างของบันไดแตะพื้น ให้ $B$ เป็นจุดที่กำแพงตั้งอยู่บนพื้น '
        'โดย $B$ อยู่ในแนวเดียวกับ $A$ ตรงโคนกำแพง และให้ $C$ เป็นจุดที่ปลายบนของบันไดแตะกำแพง',
        '• เนื่องจากกำแพงตั้งฉากกับพื้นราบ สามเหลี่ยม $ABC$ จึงเป็นสามเหลี่ยมมุมฉากที่มีมุมฉากอยู่ที่ $B$',
        '• ตัวบันไดคือด้าน $AC$ ซึ่งอยู่ตรงข้ามกับมุมฉากที่ $B$ ดังนั้น $AC$ เป็นด้านตรงข้ามมุมฉาก '
        'และมีความยาว $8$ เมตร',
        '• มุมที่บันไดทำกับพื้นราบคือมุมที่จุด $A$ จึงได้ว่ามุม $A$ มีขนาด $60^{\\circ}$',
        '',
        '<b>ขั้นที่ 2 · ระบุว่าสิ่งที่โจทย์ถามอยู่ตำแหน่งใดเมื่อเทียบกับมุมอ้างอิง</b>',
        '• ความสูงของปลายบนบันไดจากพื้นราบ วัดตามแนวกำแพง จึงเป็นความยาวของด้าน $BC$',
        '• เมื่อใช้มุมที่ $A$ เป็นมุมอ้างอิง ด้าน $BC$ อยู่ตรงข้ามกับมุมนั้นพอดี '
        'จึงเป็นด้านตรงข้ามมุมอ้างอิง ⛔ ไม่ใช่ด้านประชิด',
        '• อัตราส่วนที่จับคู่ระหว่างด้านตรงข้ามมุมกับด้านตรงข้ามมุมฉากมีเพียงอัตราส่วนเดียวคือไซน์ '
        'จึงต้องใช้ $\\sin 60^{\\circ}$ ⛔ ไม่ใช่โคไซน์และไม่ใช่แทนเจนต์',
        '',
        '<b>ขั้นที่ 3 · เขียนสมการจากนิยาม แล้วแทนค่า</b>',
        '• จากนิยาม : $\\sin 60^{\\circ} = \\dfrac{BC}{AC}$',
        '• คูณด้วย $AC$ ทั้งสองข้างเพื่อย้าย $BC$ ออกมาเดี่ยว ๆ : $BC = AC \\times \\sin 60^{\\circ}$',
        '• แทนค่าที่โจทย์ให้และค่ามุมพิเศษ : $BC = 8 \\times \\dfrac{\\sqrt{3}}{2}$',
        '• ยุบตัวเลข โดยหาร $8$ ด้วย $2$ ได้ $4$ : $BC = 4\\sqrt{3}$ เมตร',
        '',
        '<b>ขั้นที่ 4 · ตรวจความสมเหตุสมผลของขนาด</b>',
        '• ค่าประมาณของ $\\sqrt{3}$ คือ $1.732$ ดังนั้น $4\\sqrt{3}$ มีค่าประมาณ $6.93$ เมตร',
        '• ความสูงนี้ต้องน้อยกว่าความยาวบันได $8$ เมตร เสมอ เพราะด้าน $BC$ '
        'เป็นด้านประกอบมุมฉาก ส่วน $AC$ เป็นด้านตรงข้ามมุมฉากซึ่งยาวที่สุดในสามเหลี่ยม '
        'ค่า $6.93$ น้อยกว่า $8$ จริง จึงผ่านการตรวจเบื้องต้น',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · หาด้านราบก่อนด้วยโคไซน์ แล้วย้อนหาความสูงด้วยทฤษฎีบทพีทาโกรัส '
        'โดยไม่ใช้ไซน์เลย)</b>',
        '• หาระยะจากปลายล่างของบันไดถึงโคนกำแพง ซึ่งเป็นด้านประชิดมุมที่ $A$ : '
        '$AB = AC \\times \\cos 60^{\\circ} = 8 \\times \\dfrac{1}{2} = 4$ เมตร',
        '• ใช้ทฤษฎีบทพีทาโกรัสกับสามเหลี่ยม $ABC$ ที่มีมุมฉากอยู่ที่ $B$ : $AB^2 + BC^2 = AC^2$',
        '• แทนค่า : $4^2 + BC^2 = 8^2$ นั่นคือ $16 + BC^2 = 64$',
        '• ย้ายข้าง : $BC^2 = 48$ แล้วถอดรากที่สอง โดยความยาวต้องเป็นจำนวนบวก : '
        '$BC = \\sqrt{48} = \\sqrt{16 \\times 3} = 4\\sqrt{3}$',
        '• เส้นทางนี้ใช้เพียงโคไซน์กับทฤษฎีบทพีทาโกรัส ไม่ได้ใช้ไซน์เลย แต่ได้ค่าเดียวกัน '
        'จึงยืนยันว่าคำตอบถูกต้อง',
        '',
        '✅ <b>คำตอบ</b> $4\\sqrt{3}$ → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เวลาแก้โจทย์สามเหลี่ยมมุมฉากที่มาในรูปคำบรรยาย ให้ทำสามอย่างนี้ตามลำดับเสมอ '
        'หนึ่ง วาดรูปแล้วชี้ว่ามุมฉากอยู่ที่ไหน สอง ระบายว่าด้านที่โจทย์ให้กับด้านที่โจทย์ถาม '
        'อยู่ตำแหน่งใดเมื่อเทียบกับมุมที่รู้ค่า สาม จึงค่อยเลือกอัตราส่วน '
        'ถ้าเลือกอัตราส่วนก่อนวาดรูป มีโอกาสสูงมากที่จะหยิบผิดตัว',
        '• จำรูปสามเหลี่ยมมุม $30^{\\circ}$ กับ $60^{\\circ}$ ไว้เป็นภาพเดียว '
        'ถ้าด้านตรงข้ามมุมฉากยาว $2k$ ด้านตรงข้ามมุม $30^{\\circ}$ จะยาว $k$ '
        'และด้านตรงข้ามมุม $60^{\\circ}$ จะยาว $k\\sqrt{3}$ '
        'ในข้อนี้ $2k = 8$ จึงได้ $k = 4$ และความสูงซึ่งอยู่ตรงข้ามมุม $60^{\\circ}$ '
        'จึงเท่ากับ $4\\sqrt{3}$ ทันทีโดยไม่ต้องคูณเศษส่วน',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $4$ เพราะหยิบอัตราส่วนผิดตัว ไปใช้ $BC = 8\\cos 60^{\\circ} = 4$ '
        'โคไซน์จับคู่ด้านประชิดมุมกับด้านตรงข้ามมุมฉาก ค่า $4$ ที่ได้จึงเป็นระยะจากปลายบันไดถึงโคนกำแพง '
        'ตามแนวพื้น ไม่ใช่ความสูง ให้ถามตัวเองทุกครั้งว่าด้านที่ต้องการอยู่ตรงข้ามมุมหรือประชิดมุม',
        '• ได้ $4\\sqrt{2}$ เพราะเผลอใช้มุม $45^{\\circ}$ แทนมุมที่โจทย์ให้ '
        'จึงคำนวณ $8\\sin 45^{\\circ} = 8 \\times \\dfrac{1}{\\sqrt{2}} = 4\\sqrt{2}$ '
        'ความพลาดนี้มักเกิดเพราะคุ้นกับรูปสามเหลี่ยมหน้าจั่วมุมฉากจนหยิบมาใช้อัตโนมัติ '
        'ให้อ่านตัวเลขมุมในโจทย์ซ้ำก่อนแทนค่าเสมอ',
        '• ได้ $8\\sqrt{3}$ เพราะใช้แทนเจนต์แทนไซน์ จึงคำนวณ $8\\tan 60^{\\circ} = 8\\sqrt{3}$ '
        'แทนเจนต์เป็นอัตราส่วนระหว่างด้านประกอบมุมฉากสองด้าน ไม่ได้เกี่ยวกับด้านตรงข้ามมุมฉากเลย '
        'ค่าที่ได้ประมาณ $13.86$ ซึ่งยาวกว่าตัวบันไดเอง เป็นไปไม่ได้ในทางกายภาพ '
        'ให้ใช้หลักว่าด้านประกอบมุมฉากต้องสั้นกว่าด้านตรงข้ามมุมฉากเสมอเป็นตัวคัดกรองด่านแรก',
    ],
    'V.mold: G = a single right triangle given as a word problem, with the hypotenuse length and the acute '
    'angle it makes with the horizontal both given / A = the vertical leg / M = pick the correct trigonometric '
    'ratio from the position of the requested side relative to the reference angle, then substitute a special '
    'angle value. Rubric F1 C0 P1 T0 L1 = 3/15 with T = 0 and total at least 3 -> level: ปานกลาง. Note on '
    'honesty of the grading: this slot was planned as ง่าย, but the honest score came out at 3 because the item '
    'is a word problem that the student must translate into a figure without any picture supplied, which is '
    'exactly what L = 1 measures; the level was accepted as ปานกลาง rather than pushing L down to 0, because '
    'every item the teacher has already accepted as ง่าย (q010, q065, q070) is a bare symbolic problem with no '
    'context at all. sympy (verify_b14.py): route 1 evaluates 8*sin(rad(60)) and returns 4*sqrt(3); route 2 is '
    'independent of the sine function entirely, computing the horizontal leg 8*cos(rad(60)) = 4 first and then '
    'recovering the vertical leg through sqrt(8^2 - 4^2), and the two agree symbolically. All three distractors '
    'machine-computed from named error paths: 4 from 8*cos(60) which is the adjacent-instead-of-opposite slip, '
    '4*sqrt(2) from 8*sin(45) which is the wrong-special-angle slip, and 8*sqrt(3) from 8*tan(60) which is the '
    'wrong-ratio slip. A guard asserts the four values are pairwise distinct numerically and that the '
    'common-sense bound (the height must be smaller than the ladder length of 8) eliminates only 8*sqrt(3), so '
    'two distractors survive the cheapest sanity check and the item cannot be answered by estimation alone. '
    'Collision sweep on 6387 items (bank 62 files + k1 out + k2 out) across three probe rounds: the word '
    'ladder appears in 16 items, all of which are false positives outside chapter 7 (ladder as a metaphor in '
    'sequences and in statistics), and the direct probe restricted to chapter 7 returns 0 hits, so this surface '
    'is genuinely unused in the trigonometry chapter. Redesign history: this candidate was cleared during '
    'batch 13 probing and deliberately held in reserve rather than used there, because batch 13 needed an item '
    'carrying a three-dimensional reading load and this one is planar.',
)

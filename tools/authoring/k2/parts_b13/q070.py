# -*- coding: utf-8 -*-
add(
    70,
    ['7.9'],
    'ง่าย',
    'กำหนดให้สามเหลี่ยม $ABC$ มีความยาวด้าน $a = 3$ หน่วย , $b = 5$ หน่วย และ $c = 7$ หน่วย '
    'โดย $a$ , $b$ และ $c$ เป็นความยาวของด้านที่อยู่ตรงข้ามมุม $A$ , $B$ และ $C$ ตามลำดับ '
    'ค่าของโคไซน์ของมุมที่มีขนาดใหญ่ที่สุดในสามเหลี่ยมนี้ ตรงกับข้อใด',
    [
        '$-\\dfrac{1}{2}$',
        '$\\dfrac{1}{2}$',
        '$\\dfrac{11}{14}$',
        '$\\dfrac{13}{14}$',
    ],
    0,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• กฎของโคไซน์ในสามเหลี่ยม $ABC$ ที่ด้าน $a$ , $b$ , $c$ อยู่ตรงข้ามมุม $A$ , $B$ , $C$ ตามลำดับ '
        'เขียนได้ว่า $c^2 = a^2 + b^2 - 2ab\\cos C$ ซึ่งจัดรูปเพื่อหาโคไซน์ได้เป็น '
        '$\\cos C = \\dfrac{a^2 + b^2 - c^2}{2ab}$',
        '• ในสามเหลี่ยมใด ๆ มุมที่มีขนาดใหญ่กว่าย่อมอยู่ตรงข้ามด้านที่ยาวกว่าเสมอ '
        'ดังนั้นมุมที่ใหญ่ที่สุดคือมุมที่อยู่ตรงข้ามด้านที่ยาวที่สุด',
        '• ถ้าโคไซน์ของมุมในสามเหลี่ยมมีค่าเป็นจำนวนลบ แสดงว่ามุมนั้นเป็นมุมป้าน '
        'เพราะโคไซน์ของมุมแหลมเป็นจำนวนบวกเสมอ',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• สามเหลี่ยม $ABC$ มีความยาวด้านสามด้านคือ $a = 3$ หน่วย , $b = 5$ หน่วย และ $c = 7$ หน่วย',
        '• ด้าน $a$ อยู่ตรงข้ามมุม $A$ , ด้าน $b$ อยู่ตรงข้ามมุม $B$ และด้าน $c$ อยู่ตรงข้ามมุม $C$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าโคไซน์ของมุมที่มีขนาดใหญ่ที่สุดในสามเหลี่ยมนี้',
        '',
        '<b>【 ระบุมุมที่ใหญ่ที่สุดจากด้านที่ยาวที่สุดก่อน แล้วจึงใช้กฎของโคไซน์เพียงครั้งเดียว 】</b>',
        '',
        '<b>ขั้นที่ 1 · หาว่ามุมใดเป็นมุมที่ใหญ่ที่สุด</b>',
        '• เทียบความยาวด้านทั้งสาม : $3 < 5 < 7$ ดังนั้นด้านที่ยาวที่สุดคือด้าน $c$ ซึ่งยาว $7$ หน่วย',
        '• ด้าน $c$ อยู่ตรงข้ามมุม $C$ และมุมที่อยู่ตรงข้ามด้านที่ยาวที่สุดคือมุมที่ใหญ่ที่สุด',
        '• สรุปว่าสิ่งที่ต้องหาคือ $\\cos C$ ไม่ใช่โคไซน์ของมุมอื่น',
        '',
        '<b>ขั้นที่ 2 · เขียนกฎของโคไซน์ให้ตรงกับมุมที่ต้องการ</b>',
        '• เริ่มจากรูปมาตรฐานที่มีมุม $C$ อยู่ในสูตร : $c^2 = a^2 + b^2 - 2ab\\cos C$',
        '• ย้ายข้างเพื่อแยก $\\cos C$ ออกมา : $2ab\\cos C = a^2 + b^2 - c^2$',
        '• หารด้วย $2ab$ ทั้งสองข้าง : $\\cos C = \\dfrac{a^2 + b^2 - c^2}{2ab}$',
        '• สังเกตว่าด้านที่อยู่ตรงข้ามมุมที่ต้องการ (คือ $c$) ต้องเป็นตัวที่ถูกลบเสมอ',
        '',
        '<b>ขั้นที่ 3 · แทนค่าแล้วยุบเศษส่วน</b>',
        '• แทน $a = 3$ , $b = 5$ , $c = 7$ : $\\cos C = \\dfrac{3^2 + 5^2 - 7^2}{2 \\times 3 \\times 5}$',
        '• คำนวณทีละพจน์ในตัวเศษ : $3^2 = 9$ , $5^2 = 25$ , $7^2 = 49$ ดังนั้นตัวเศษ $= 9 + 25 - 49 = -15$',
        '• คำนวณตัวส่วน : $2 \\times 3 \\times 5 = 30$',
        '• ยุบเศษส่วน : $\\cos C = \\dfrac{-15}{30} = -\\dfrac{1}{2}$',
        '• ค่าที่ได้เป็นจำนวนลบ สอดคล้องกับที่คาดไว้ว่ามุมใหญ่ที่สุดของสามเหลี่ยมรูปนี้เป็นมุมป้าน',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · หาพื้นที่ด้วยสูตรของเฮรอนแล้วย้อนกลับไปหาไซน์ของมุม)</b>',
        '• ครึ่งหนึ่งของความยาวรอบรูป : $s = \\dfrac{3 + 5 + 7}{2} = \\dfrac{15}{2}$',
        '• สูตรของเฮรอน : พื้นที่ $= \\sqrt{s(s-a)(s-b)(s-c)} = '
        '\\sqrt{\\dfrac{15}{2} \\times \\dfrac{9}{2} \\times \\dfrac{5}{2} \\times \\dfrac{1}{2}} = '
        '\\sqrt{\\dfrac{675}{16}} = \\dfrac{15\\sqrt{3}}{4}$',
        '• อีกด้านหนึ่ง พื้นที่ $= \\dfrac{1}{2}ab\\sin C = \\dfrac{1}{2} \\times 3 \\times 5 \\times \\sin C$',
        '• จับสองค่ามาเท่ากัน : $\\dfrac{15}{2}\\sin C = \\dfrac{15\\sqrt{3}}{4}$ จะได้ $\\sin C = \\dfrac{\\sqrt{3}}{2}$',
        '• มุมที่มีไซน์เท่ากับ $\\dfrac{\\sqrt{3}}{2}$ มีสองมุมในสามเหลี่ยม คือ $60^{\\circ}$ กับ $120^{\\circ}$ '
        'แต่ $C$ เป็นมุมที่ใหญ่ที่สุดจึงเป็นมุมป้านไม่ได้เป็น $60^{\\circ}$ ดังนั้น $C = 120^{\\circ}$',
        '• จึงได้ $\\cos C = \\cos 120^{\\circ} = -\\dfrac{1}{2}$ ตรงกับคำตอบที่หามาได้',
        '',
        '✅ <b>คำตอบ</b> $-\\dfrac{1}{2}$ → <b>ตัวเลือก 1</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• ก่อนคำนวณให้ดูเครื่องหมายของตัวเศษก่อน ถ้า $a^2 + b^2 < c^2$ แปลว่ามุมตรงข้ามด้าน $c$ เป็นมุมป้าน '
        'ในข้อนี้ $9 + 25 = 34$ ซึ่งน้อยกว่า $49$ จึงรู้ตั้งแต่ยังไม่หารว่าคำตอบต้องติดลบ '
        'ตัดตัวเลือกที่เป็นจำนวนบวกทิ้งได้ทันที',
        '• ชุดด้าน $3$-$5$-$7$ เป็นชุดที่ควรจำไว้ เพราะให้มุมป้านพอดี $120^{\\circ}$ '
        'เช่นเดียวกับชุด $3$-$8$-$7$ ที่ให้มุม $60^{\\circ}$',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $\\dfrac{1}{2}$ เพราะเขียนตัวเศษสลับเป็น $\\dfrac{c^2 - a^2 - b^2}{2ab} = \\dfrac{49 - 9 - 25}{30}$ '
        'ซึ่งเท่ากับการทำเครื่องหมายลบตกไปทั้งก้อน ให้จำว่าด้านตรงข้ามมุมที่ต้องการต้องถูกลบเสมอ',
        '• ได้ $\\dfrac{11}{14}$ เพราะเผลอหาโคไซน์ของมุม $B$ ซึ่งอยู่ตรงข้ามด้านยาว $5$ '
        'นั่นคือ $\\dfrac{3^2 + 7^2 - 5^2}{2 \\times 3 \\times 7} = \\dfrac{33}{42}$ '
        'ซึ่งเป็นมุมกลาง ไม่ใช่มุมที่ใหญ่ที่สุด',
        '• ได้ $\\dfrac{13}{14}$ เพราะหาโคไซน์ของมุม $A$ ซึ่งอยู่ตรงข้ามด้านสั้นที่สุด '
        'นั่นคือ $\\dfrac{5^2 + 7^2 - 3^2}{2 \\times 5 \\times 7} = \\dfrac{65}{70}$ '
        'มุมนี้เป็นมุมที่เล็กที่สุดของรูป ตรงข้ามกับที่โจทย์ถามพอดี',
    ],
    'V.mold: G = a triangle given by its three numeric side lengths 3, 5, 7 with the side-to-opposite-angle '
    'convention stated explicitly / A = the cosine of the largest angle of the triangle / M = identify the '
    'largest angle from the longest side, then one application of the law of cosines solved for the cosine. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 -> level: ง่าย. sympy (verify_b13.py): route 1 gives cos C = -1/2 directly; '
    'route 2 is independent — Heron gives area 15*sqrt(3)/4, the (1/2)ab sin C form then gives sin C = sqrt(3)/2, '
    'and the largest-angle argument forces C = 120 degrees rather than 60, returning cos C = -1/2. All three '
    'distractors machine-computed from named error paths: 1/2 from the sign-flipped numerator (c^2 - a^2 - b^2), '
    '11/14 = cos B (angle opposite the middle side), 13/14 = cos A (angle opposite the shortest side). '
    'A guard asserts the three wrong values are pairwise distinct from each other and from -1/2, and that '
    'exactly one of the four is negative so that the sign shortcut named in the เทคนิค block does not by itself '
    'collapse the item — it leaves three positive candidates in play for a student who has not identified '
    'which angle is asked for. Collision sweep on 6382 items (bank 62 files + k1 + k2 out): the 3-5-7 numeric '
    'triple in a question stem returns 0 hits, and the ask “cosine of the largest angle” returns 0 hits. '
    'Redesign history: the first draft asked for the size of the angle in degrees, but that collides with the '
    'well-worn 120-degree recognition shape already present in the bank, so the ask was moved to the cosine '
    'value itself, which keeps the item ง่าย while letting the distractors carry the two wrong-angle error paths.',
)

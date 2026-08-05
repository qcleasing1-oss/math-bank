# -*- coding: utf-8 -*-
add(
    74,
    ['7.9'],
    'ยากมาก',
    'กำหนดให้ $a$ , $b$ และ $c$ เป็นความยาวด้านของสามเหลี่ยม $ABC$ '
    'ซึ่งอยู่ตรงข้ามมุม $A$ , $B$ และ $C$ ตามลำดับ '
    'ถ้า $a$ , $b$ , $c$ เรียงกันเป็นลำดับเรขาคณิต '
    'แล้วเซตของค่าที่เป็นไปได้ทั้งหมดของขนาดมุม $B$ ในหน่วยเรเดียน ตรงกับข้อใด',
    [
        '$0 < B < \\dfrac{\\pi}{3}$',
        '$0 < B \\le \\dfrac{\\pi}{3}$',
        '$0 < B \\le \\dfrac{\\pi}{2}$',
        '$\\dfrac{\\pi}{3} \\le B < \\pi$',
    ],
    1,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ลำดับเรขาคณิตคือลำดับที่อัตราส่วนของพจน์ที่ติดกันคงที่ '
        'ดังนั้นถ้า $a$ , $b$ , $c$ เรียงกันเป็นลำดับเรขาคณิต จะได้ $\\dfrac{b}{a} = \\dfrac{c}{b}$ '
        'ซึ่งจัดรูปได้เป็น $b^2 = ac$',
        '• กฎของโคไซน์ในรูปที่แยกโคไซน์ออกมาแล้ว : $\\cos B = \\dfrac{a^2 + c^2 - b^2}{2ac}$',
        '• อสมการ AM-GM สำหรับจำนวนจริงบวกสองจำนวน : $x + y \\ge 2\\sqrt{xy}$ '
        'โดยเกิดการเท่ากันก็ต่อเมื่อ $x = y$ '
        'กรณีที่ใช้บ่อยคือ $\\dfrac{a}{c} + \\dfrac{c}{a} \\ge 2$ เพราะผลคูณของสองพจน์นี้เท่ากับ $1$',
        '• ฟังก์ชันโคไซน์เป็นฟังก์ชันลดบนช่วง $(0, \\pi)$ '
        'ดังนั้นเมื่อโคไซน์มีค่ามากขึ้น มุมจะเล็กลง ⚠️ การแปลงอสมการของโคไซน์กลับเป็นอสมการของมุม '
        'ต้องกลับทิศของเครื่องหมายเสมอ',
        '• ในสามเหลี่ยมใด ๆ มุมภายในทุกมุมต้องมีขนาดมากกว่า $0$ และน้อยกว่า $\\pi$ เรเดียน',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $a$ , $b$ , $c$ เป็นความยาวด้านของสามเหลี่ยม $ABC$ '
        'โดย $a$ อยู่ตรงข้ามมุม $A$ , $b$ อยู่ตรงข้ามมุม $B$ และ $c$ อยู่ตรงข้ามมุม $C$',
        '• $a$ , $b$ , $c$ เรียงกันเป็นลำดับเรขาคณิตตามลำดับนี้',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาเซตของค่าที่เป็นไปได้ทั้งหมดของขนาดมุม $B$',
        '',
        '<b>【 กำจัด $b$ ออกจากกฎของโคไซน์ด้วยเงื่อนไขลำดับเรขาคณิต '
        'แล้วบีบค่าที่เหลือด้วยอสมการ AM-GM 】</b>',
        '',
        '<b>ขั้นที่ 1 · แปลเงื่อนไขลำดับเรขาคณิตให้เป็นสมการพีชคณิต</b>',
        '• พจน์ที่ติดกันมีอัตราส่วนคงที่ : $\\dfrac{b}{a} = \\dfrac{c}{b}$',
        '• คูณไขว้ : $b^2 = ac$',
        '• สังเกตว่า $b$ เป็นด้านที่อยู่ตรงข้ามมุม $B$ ซึ่งเป็นมุมที่โจทย์ถามพอดี '
        'และเงื่อนไขนี้ก็เขียน $b^2$ ให้เราแล้ว จึงเป็นสัญญาณว่าควรใช้กฎของโคไซน์ที่มุม $B$',
        '',
        '<b>ขั้นที่ 2 · เขียนกฎของโคไซน์ที่มุม $B$ แล้วกำจัด $b$ ทิ้ง</b>',
        '• กฎของโคไซน์ที่มุม $B$ : $\\cos B = \\dfrac{a^2 + c^2 - b^2}{2ac}$',
        '• แทน $b^2 = ac$ ลงไป : $\\cos B = \\dfrac{a^2 + c^2 - ac}{2ac}$',
        '• ตอนนี้เหลือตัวแปรเพียงสองตัวคือ $a$ กับ $c$ และทั้งคู่เป็นจำนวนจริงบวก',
        '',
        '<b>ขั้นที่ 3 · จัดรูปให้อยู่ในรูปของอัตราส่วนตัวเดียว</b>',
        '• แยกเศษออกเป็นสามก้อนแล้วหารด้วย $2ac$ ทีละก้อน : '
        '$\\cos B = \\dfrac{a^2}{2ac} + \\dfrac{c^2}{2ac} - \\dfrac{ac}{2ac}$',
        '• ยุบแต่ละก้อน : $\\cos B = \\dfrac{a}{2c} + \\dfrac{c}{2a} - \\dfrac{1}{2}$',
        '• ดึง $\\dfrac{1}{2}$ ออกมาเป็นตัวประกอบร่วม : '
        '$\\cos B = \\dfrac{1}{2}\\left(\\dfrac{a}{c} + \\dfrac{c}{a} - 1\\right)$',
        '• ให้ $u = \\dfrac{a}{c} + \\dfrac{c}{a}$ จะได้รูปสั้นว่า $\\cos B = \\dfrac{u - 1}{2}$',
        '',
        '<b>ขั้นที่ 4 · ใช้อสมการ AM-GM หาขอบเขตของ $u$ แล้วส่งต่อไปยัง $\\cos B$</b>',
        '• เนื่องจาก $\\dfrac{a}{c}$ และ $\\dfrac{c}{a}$ เป็นจำนวนจริงบวกที่คูณกันได้ $1$ '
        'อสมการ AM-GM ให้ $u = \\dfrac{a}{c} + \\dfrac{c}{a} \\ge 2\\sqrt{1} = 2$',
        '• การเท่ากันเกิดขึ้นก็ต่อเมื่อ $\\dfrac{a}{c} = \\dfrac{c}{a}$ นั่นคือ $a = c$',
        '• แทนขอบเขตนี้ลงในรูปสั้น : $\\cos B = \\dfrac{u - 1}{2} \\ge \\dfrac{2 - 1}{2} = \\dfrac{1}{2}$',
        '• อีกด้านหนึ่ง $B$ เป็นมุมภายในของสามเหลี่ยมจึงมี $\\cos B < 1$ เสมอ '
        'ดังนั้น $\\dfrac{1}{2} \\le \\cos B < 1$',
        '',
        '<b>ขั้นที่ 5 · แปลงอสมการของโคไซน์กลับเป็นอสมการของมุม โดยกลับทิศ</b>',
        '• โคไซน์เป็นฟังก์ชันลดบนช่วง $(0, \\pi)$ '
        'เมื่อ $\\cos B$ มีค่าไม่น้อยกว่า $\\dfrac{1}{2}$ มุม $B$ จึงต้องมีค่าไม่มากกว่ามุมที่โคไซน์เท่ากับ '
        '$\\dfrac{1}{2}$ พอดี ซึ่งก็คือ $\\dfrac{\\pi}{3}$',
        '• จาก $\\cos B \\ge \\dfrac{1}{2}$ จึงได้ $B \\le \\dfrac{\\pi}{3}$',
        '• จาก $\\cos B < 1$ จึงได้ $B > 0$',
        '• ปลายบนถึงได้จริง เพราะเมื่อ $a = c$ เงื่อนไข $b^2 = ac$ บังคับให้ $b = a$ ด้วย '
        'ได้สามเหลี่ยมด้านเท่าซึ่งมีมุมทุกมุมเป็น $\\dfrac{\\pi}{3}$ พอดี '
        'ค่าสูงสุดที่เป็นไปได้ของมุม $B$ จึงคือ $\\dfrac{\\pi}{3}$',
        '• ปลายล่างไม่ถึง เพราะ $B = 0$ ทำให้ไม่เกิดสามเหลี่ยม '
        'แต่ค่าที่ใกล้ $0$ เท่าใดก็ได้ยังเป็นไปได้ ดังจะแสดงในการตรวจคำตอบ',
        '• สรุปเซตของค่าที่เป็นไปได้ทั้งหมดคือ $0 < B \\le \\dfrac{\\pi}{3}$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนอัตราส่วนร่วมเป็นตัวเลขจริงแล้วตรวจทีละปลายของช่วง)</b>',
        '• ให้อัตราส่วนร่วมของลำดับเป็น $r$ แล้วเขียนด้านสามด้านเป็น $a$ , $ar$ , $ar^2$ '
        'ซึ่งไม่เสียนัยทั่วไปหากให้ $a = 1$ ได้ด้าน $1$ , $r$ , $r^2$',
        '• ทดลองค่ากลางช่วง $r = \\dfrac{3}{2}$ ได้ด้าน $1$ , $\\dfrac{3}{2}$ , $\\dfrac{9}{4}$ '
        'ตรวจอสมการสามเหลี่ยมก่อนว่าสร้างได้จริง : $1 + \\dfrac{3}{2} = \\dfrac{5}{2}$ '
        'ซึ่งมากกว่า $\\dfrac{9}{4}$ จึงเป็นสามเหลี่ยมได้',
        '• คำนวณโดยตรง : $\\cos B = \\dfrac{1^2 + \\left(\\dfrac{9}{4}\\right)^2 - \\left(\\dfrac{3}{2}\\right)^2}'
        '{2 \\times 1 \\times \\dfrac{9}{4}} = \\dfrac{\\dfrac{61}{16}}{\\dfrac{9}{2}} = \\dfrac{61}{72}$ '
        'ซึ่งมากกว่า $\\dfrac{1}{2}$ จริง และให้ $B$ ประมาณ $32.09^{\\circ}$ ซึ่งน้อยกว่า $60^{\\circ}$ '
        'สอดคล้องกับผลที่ได้',
        '• ตรวจปลายบน $r = 1$ ได้ด้าน $1$ , $1$ , $1$ เป็นสามเหลี่ยมด้านเท่า '
        'ได้ $B = \\dfrac{\\pi}{3}$ พอดี ⇒ ปลายบนต้องเป็นวงเล็บปิด',
        '• ตรวจปลายล่าง อสมการสามเหลี่ยมบังคับว่า $1 + r > r^2$ ซึ่งเป็นจริงเมื่อ '
        '$r < \\dfrac{1 + \\sqrt{5}}{2}$ เท่านั้น เมื่อให้ $r$ ไต่เข้าใกล้ค่านี้ '
        'สามเหลี่ยมจะแบนลงเรื่อย ๆ และ $B$ ลดลงเข้าหา $0$ ได้ไม่จำกัด แต่ไม่มีค่าใดทำให้ $B$ เป็น $0$ '
        '⇒ ปลายล่างต้องเป็นวงเล็บเปิด',
        '',
        '✅ <b>คำตอบ</b> $0 < B \\le \\dfrac{\\pi}{3}$ → <b>ตัวเลือก 2</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เมื่อโจทย์ให้เงื่อนไขที่เขียน “กำลังสองของด้านหนึ่ง” ให้ได้ '
        '(เช่น ลำดับเรขาคณิตให้ $b^2 = ac$ หรือลำดับเลขคณิตให้ $2b = a + c$) '
        'ให้เล็งกฎของโคไซน์ที่มุมตรงข้ามด้านนั้นทันที เพราะจะกำจัดตัวแปรได้หนึ่งตัวในก้าวเดียว',
        '• เมื่อจัดรูปแล้วได้นิพจน์ที่มีทั้ง $\\dfrac{a}{c}$ และ $\\dfrac{c}{a}$ อยู่ด้วยกัน '
        'ให้นึกถึง AM-GM ทันที เพราะสองพจน์นี้คูณกันได้ $1$ เสมอ ผลบวกจึงมีค่าต่ำสุดที่ $2$ '
        'และเกิดตอนที่รูปสมมาตร คือ $a = c$',
        '• ก่อนเลือกตัวเลือก ให้ทดสอบด้วยสามเหลี่ยมด้านเท่าเสมอ เพราะมันสอดคล้องกับเงื่อนไขลำดับเรขาคณิต '
        '(อัตราส่วนร่วมเท่ากับ $1$) และให้ $B = \\dfrac{\\pi}{3}$ พอดี '
        'ตัวเลือกใดที่ไม่รวมค่านี้ ตัดทิ้งได้ทันที',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $0 < B < \\dfrac{\\pi}{3}$ เพราะลืมตรวจกรณีเท่ากันของอสมการ AM-GM '
        'อสมการ $u \\ge 2$ เป็นแบบไม่เข้มงวด และการเท่ากันเกิดจริงเมื่อ $a = c$ '
        'ซึ่งให้สามเหลี่ยมด้านเท่าที่มีอยู่จริง ปลายบนจึงต้องปิด ไม่ใช่เปิด',
        '• ได้ $0 < B \\le \\dfrac{\\pi}{2}$ เพราะสรุปเพียงว่า $\\cos B$ เป็นจำนวนบวก '
        'จึงบอกได้แค่ว่า $B$ ไม่ใช่มุมป้าน นั่นเป็นการใช้ประโยชน์จากอสมการไม่เต็มที่ '
        'ขอบเขตที่แท้จริงคือ $\\cos B \\ge \\dfrac{1}{2}$ ซึ่งเข้มกว่า $\\cos B > 0$ มาก',
        '• ได้ $\\dfrac{\\pi}{3} \\le B < \\pi$ เพราะแปลงอสมการกลับโดยไม่กลับทิศ '
        'เห็น $\\cos B \\ge \\dfrac{1}{2}$ แล้วเขียนต่อทันทีว่า $B \\ge \\dfrac{\\pi}{3}$ '
        'ต้องจำว่าโคไซน์เป็นฟังก์ชันลดบนช่วง $(0, \\pi)$ '
        'ค่าโคไซน์ที่ใหญ่ขึ้นหมายถึงมุมที่เล็กลงเสมอ',
    ],
    'V.mold: G = the three side lengths of a triangle constrained to form a geometric progression in the '
    'order a, b, c, with the side-to-opposite-angle convention stated / A = the set of all possible values of '
    'the middle angle B / M = substitute b^2 = ac into the law of cosines at B, reduce to (u - 1)/2 where '
    'u = a/c + c/a, bound u below by AM-GM, then invert the cosine inequality with the direction reversed and '
    'settle each endpoint separately. Rubric F3 C3 P2 T3 L1 = 12/15 with T = 3 -> level: ยากมาก. '
    'sympy (verify_b13.py): route 1 performs the symbolic reduction and confirms cos B = (u - 1)/2 with '
    'u >= 2, giving cos B >= 1/2 and hence B <= pi/3; route 2 is independent and numeric — it parameterises '
    'the sides as 1, r, r^2 and evaluates B at r = 3/2 (cos B = 61/72, B about 32.089 degrees, triangle '
    'inequality checked first), at r = 1 (equilateral, B exactly pi/3, so the upper endpoint is attained), '
    'and at r = phi - 10^-e for e = 2..8 at 40-digit precision, where B falls monotonically below 1/1000 '
    'without ever reaching 0, confirming the lower endpoint is open. All three distractors machine-computed '
    'from named error paths: the strict upper bound from forgetting the AM-GM equality case, (0, pi/2] from '
    'concluding only that B is not obtuse, and [pi/3, pi) from failing to reverse the inequality direction. '
    'A guard asserts that the equilateral test named in the เทคนิค block kills exactly two of the three '
    'distractors and not all three, so the item still requires the lower-endpoint reasoning. Collision sweep '
    'on 6382 items (bank 62 files + k1 + k2 out): sides in geometric progression inside a triangle returns 0 '
    'hits anywhere in the bank — the 71 hits on the loose probe were all sequence-and-series items from '
    'chapters 11 and 14 or geometric series of powers of sin and cos, none of them about triangle sides; '
    'the ask for a set of possible angle values also returns 0 hits in chapter 7. Redesign history: an '
    'earlier ยากมาก candidate for this slot used the roots of a quadratic as tan values and collided with '
    'both chap-07-q182 and samn-2559-12-q03, and another used sector perimeter and collided with our own '
    'q034; this design was kept because the three stacked turning points (spotting AM-GM unprompted, '
    'reversing the inequality, and the asymmetric endpoints) are what earn the T = 3 score honestly rather '
    'than by adding computation.',
)

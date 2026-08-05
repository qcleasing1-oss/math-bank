# -*- coding: utf-8 -*-
add(
    88,
    ['7.6', '7.9'],
    'ยาก',
    'สามเหลี่ยม $ABC$ มี $AB = 10$ หน่วย $AC = 15$ หน่วย และมุม $A$ กาง '
    '$\\dfrac{\\pi}{3}$ เรเดียน '
    'ลากส่วนของเส้นตรง $AD$ ที่แบ่งมุม $A$ ออกเป็นสองมุมเท่ากัน โดยจุด $D$ อยู่บนด้าน $BC$ '
    'ความยาวของ $AD$ เท่ากับกี่หน่วย',
    [
        '$6$',
        '$6\\sqrt{3}$',
        '$12$',
        '$5\\sqrt{7}$',
    ],
    1,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• พื้นที่สามเหลี่ยมเมื่อรู้ด้านสองด้านกับมุมระหว่างด้าน : '
        'พื้นที่ $= \\dfrac{1}{2}\\,ab\\sin C$ เมื่อ $a$ กับ $b$ เป็นด้านที่ประกบมุม $C$',
        '• สมบัติของการบวกพื้นที่ : ถ้าเส้นตรงจากจุดยอดตัดด้านตรงข้ามที่จุดหนึ่ง '
        'รูปเดิมจะถูกแบ่งเป็นสามเหลี่ยมสองรูปที่ไม่ทับกันและปิดเต็มรูปเดิมพอดี '
        'ผลบวกพื้นที่ของสองรูปย่อยจึงเท่ากับพื้นที่รูปใหญ่เสมอ',
        '• ค่าตรีโกณของมุมพิเศษที่ต้องใช้ : $\\sin\\dfrac{\\pi}{3} = \\dfrac{\\sqrt{3}}{2}$ '
        'และ $\\sin\\dfrac{\\pi}{6} = \\dfrac{1}{2}$ และ $\\cos\\dfrac{\\pi}{6} = \\dfrac{\\sqrt{3}}{2}$',
        '• สูตรมุมสองเท่าของไซน์ : $\\sin\\theta = 2\\sin\\dfrac{\\theta}{2}\\cos\\dfrac{\\theta}{2}$ '
        'สูตรนี้คือสะพานที่เชื่อมพื้นที่ของรูปใหญ่ซึ่งใช้มุมเต็ม '
        'เข้ากับพื้นที่ของรูปย่อยซึ่งใช้มุมครึ่ง',
        '• กฎของโคไซน์ : $a^{2} = b^{2} + c^{2} - 2bc\\cos A$ ใช้สำหรับหาด้าน $BC$ '
        'ซึ่งเป็นคนละส่วนกับ $AD$',
        '• ทฤษฎีบทเส้นแบ่งครึ่งมุม : เส้นที่แบ่งครึ่งมุม $A$ ตัดด้าน $BC$ ที่จุด $D$ '
        'จะได้ $\\dfrac{BD}{DC} = \\dfrac{AB}{AC}$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $AB = 10$ หน่วย และ $AC = 15$ หน่วย',
        '• มุม $A$ กาง $\\dfrac{\\pi}{3}$ เรเดียน หรือ $60$ องศา',
        '• $AD$ แบ่งมุม $A$ ออกเป็นสองมุมเท่ากัน แต่ละมุมจึงกาง $\\dfrac{\\pi}{6}$',
        '• จุด $D$ อยู่บนด้าน $BC$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาความยาว $AD$',
        '',
        '<b>【 ไม่ต้องหาด้าน BC เลย ให้ใช้ความจริงว่าพื้นที่สามเหลี่ยมย่อยสองรูปรวมกัน '
        'เท่ากับพื้นที่รูปใหญ่ แล้วให้ AD เป็นตัวแปรเดียวในสมการนั้น 】</b>',
        '',
        '<b>ขั้นที่ 1 · วางตัวแปรและจัดข้อมูลของสามรูป</b>',
        '• ให้ $t = AD$ ซึ่งเป็นสิ่งที่ต้องการหา',
        '• เพราะ $AD$ แบ่งครึ่งมุม $A$ จึงได้มุม $BAD$ และมุม $CAD$ กางเท่ากันคือ '
        '$\\dfrac{1}{2}\\cdot\\dfrac{\\pi}{3} = \\dfrac{\\pi}{6}$',
        '• สามเหลี่ยม $ABD$ มีด้าน $AB = 10$ และ $AD = t$ ประกบมุม $\\dfrac{\\pi}{6}$',
        '• สามเหลี่ยม $ACD$ มีด้าน $AC = 15$ และ $AD = t$ ประกบมุม $\\dfrac{\\pi}{6}$',
        '• สามเหลี่ยม $ABC$ มีด้าน $AB = 10$ และ $AC = 15$ ประกบมุม $\\dfrac{\\pi}{3}$',
        '• สังเกตว่าทั้งสามรูปรู้ด้านสองด้านกับมุมระหว่างด้านครบ จึงเขียนพื้นที่ได้ทุกรูป '
        'และรูปย่อยสองรูปมี $t$ อยู่ในสูตรทั้งคู่',
        '',
        '<b>ขั้นที่ 2 · เขียนพื้นที่ทั้งสามรูปแล้วผูกเป็นสมการเดียว</b>',
        '• พื้นที่สามเหลี่ยม $ABD = \\dfrac{1}{2}\\,(AB)(AD)\\sin\\dfrac{\\pi}{6} '
        '= \\dfrac{1}{2}\\,(10)(t)\\left(\\dfrac{1}{2}\\right)$',
        '• พื้นที่สามเหลี่ยม $ACD = \\dfrac{1}{2}\\,(AC)(AD)\\sin\\dfrac{\\pi}{6} '
        '= \\dfrac{1}{2}\\,(15)(t)\\left(\\dfrac{1}{2}\\right)$',
        '• พื้นที่สามเหลี่ยม $ABC = \\dfrac{1}{2}\\,(AB)(AC)\\sin\\dfrac{\\pi}{3} '
        '= \\dfrac{1}{2}\\,(10)(15)\\left(\\dfrac{\\sqrt{3}}{2}\\right)$',
        '• จุด $D$ อยู่บนด้าน $BC$ รูปย่อยสองรูปจึงปิดรูปใหญ่พอดีโดยไม่ทับกัน ได้สมการ '
        'พื้นที่ $ABD$ บวกพื้นที่ $ACD$ เท่ากับพื้นที่ $ABC$',
        '• ⚠️ ตรงนี้คือหัวใจของข้อนี้ ต้องใช้มุม $\\dfrac{\\pi}{6}$ ในสองรูปย่อย '
        'แต่ใช้มุม $\\dfrac{\\pi}{3}$ ในรูปใหญ่ '
        'ถ้าเผลอใช้มุมเดียวกันทั้งสามรูปสมการจะผิดตั้งแต่บรรทัดแรก',
        '',
        '<b>ขั้นที่ 3 · แก้สมการหา $t$</b>',
        '• แทนค่าลงสมการ : '
        '$\\dfrac{1}{2}(10)(t)\\left(\\dfrac{1}{2}\\right) '
        '+ \\dfrac{1}{2}(15)(t)\\left(\\dfrac{1}{2}\\right) '
        '= \\dfrac{1}{2}(10)(15)\\left(\\dfrac{\\sqrt{3}}{2}\\right)$',
        '• คิดฝั่งซ้าย : $\\dfrac{10t}{4} + \\dfrac{15t}{4} = \\dfrac{25t}{4}$',
        '• คิดฝั่งขวา : $\\dfrac{150\\sqrt{3}}{4}$',
        '• ตัวส่วน $4$ เท่ากันทั้งสองฝั่ง จึงเหลือ $25t = 150\\sqrt{3}$',
        '• ดังนั้น $t = \\dfrac{150\\sqrt{3}}{25} = 6\\sqrt{3}$ หน่วย',
        '• ตรวจความสมเหตุสมผลคร่าว ๆ : $6\\sqrt{3} \\approx 10.39$ '
        'ซึ่งอยู่ระหว่าง $10$ กับ $15$ สมเหตุสมผล เพราะเส้นแบ่งครึ่งมุมต้องยาวไม่เกินด้านที่ยาวกว่า '
        'และเอียงเข้าหาด้านที่สั้นกว่าเล็กน้อย',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · วางพิกัดจริงแล้วหาจุด $D$ '
        'ด้วยทฤษฎีบทเส้นแบ่งครึ่งมุม ไม่ใช้พื้นที่เลย)</b>',
        '• วางจุด $A$ ที่จุดกำเนิด และวางด้าน $AB$ ไปตามแกน $x$ ด้านบวก จะได้ $B = (10,\\ 0)$',
        '• ด้าน $AC$ ทำมุม $\\dfrac{\\pi}{3}$ กับแกน $x$ จึงได้ '
        '$C = \\left(15\\cos\\dfrac{\\pi}{3},\\ 15\\sin\\dfrac{\\pi}{3}\\right) '
        '= \\left(\\dfrac{15}{2},\\ \\dfrac{15\\sqrt{3}}{2}\\right)$',
        '• ทฤษฎีบทเส้นแบ่งครึ่งมุมให้ $\\dfrac{BD}{DC} = \\dfrac{AB}{AC} = \\dfrac{10}{15} '
        '= \\dfrac{2}{3}$ นั่นคือ $D$ แบ่ง $BC$ ในอัตราส่วน $2 : 3$ นับจาก $B$',
        '• จุดที่แบ่งส่วนของเส้นตรงในอัตราส่วน $m : n$ นับจากปลายแรก คำนวณได้จาก '
        '$D = \\dfrac{n\\,B + m\\,C}{m + n}$ แทนค่า $m = 2$ และ $n = 3$ ได้ '
        '$D = \\dfrac{3B + 2C}{5}$',
        '• คิดพิกัด : แนวนอนได้ $\\dfrac{3(10) + 2\\left(\\dfrac{15}{2}\\right)}{5} '
        '= \\dfrac{30 + 15}{5} = 9$ และแนวตั้งได้ '
        '$\\dfrac{3(0) + 2\\left(\\dfrac{15\\sqrt{3}}{2}\\right)}{5} '
        '= \\dfrac{15\\sqrt{3}}{5} = 3\\sqrt{3}$ จึงได้ $D = (9,\\ 3\\sqrt{3})$',
        '• ระยะจากจุดกำเนิด : $AD = \\sqrt{9^{2} + (3\\sqrt{3})^{2}} = \\sqrt{81 + 27} '
        '= \\sqrt{108} = 6\\sqrt{3}$ ตรงกับวิธีแรก',
        '• ตรวจเพิ่มว่า $AD$ แบ่งครึ่งมุมจริง : ความชันของ $AD$ คือ '
        '$\\dfrac{3\\sqrt{3}}{9} = \\dfrac{\\sqrt{3}}{3}$ '
        'ซึ่งเป็นแทนเจนต์ของมุม $\\dfrac{\\pi}{6}$ พอดี จึงเป็นครึ่งหนึ่งของ $\\dfrac{\\pi}{3}$ จริง',
        '',
        '✅ <b>คำตอบ</b> $AD = 6\\sqrt{3}$ หน่วย → <b>ตัวเลือก 2</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เทคนิค “แบ่งพื้นที่แล้วบวกกลับ” ใช้ได้ทุกครั้งที่มีเส้นลากจากจุดยอดไปตัดด้านตรงข้าม '
        'เพราะมันเปลี่ยนโจทย์ความยาวที่ดูยาก ให้กลายเป็นสมการเชิงเส้นที่มีตัวแปรตัวเดียว '
        'ข้อดีคือไม่ต้องหาด้าน $BC$ และไม่ต้องหามุมอื่นเลย',
        '• ถ้าทำโจทย์แบบนี้บ่อย ให้เก็บผลทั่วไปไว้ใช้ตรวจคำตอบ : เส้นแบ่งครึ่งมุม $A$ '
        'ในสามเหลี่ยมที่มีด้านประกบยาว $b$ กับ $c$ จะยาว '
        '$\\dfrac{2bc\\cos\\dfrac{A}{2}}{b + c}$ '
        'ข้อนี้แทนค่าได้ $\\dfrac{2(15)(10)\\left(\\dfrac{\\sqrt{3}}{2}\\right)}{25} = 6\\sqrt{3}$ '
        'ตรงกัน สูตรนี้เกิดจากขั้นตอนเดียวกับที่ทำข้างบนแต่ยังไม่แทนตัวเลข '
        'และตัว $\\cos\\dfrac{A}{2}$ ในสูตรมาจากสูตรมุมสองเท่าของไซน์ตรง ๆ',
        '• เมื่อรูปใหญ่ถูกแบ่งด้วยเส้นแบ่งครึ่งมุม ให้ระวังว่ามุมของรูปย่อยเป็นครึ่งหนึ่งของมุมเดิม '
        'อ่านโจทย์แล้วรีบเขียนค่ามุมของทั้งสามรูปลงข้างรูปทันทีก่อนลงมือคำนวณ '
        'จะกันความผิดพลาดที่พบบ่อยที่สุดของโจทย์ตระกูลนี้ได้',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $6$ เพราะใช้มุม $\\dfrac{\\pi}{3}$ กับทั้งสามรูป คือลืมว่าเส้นแบ่งครึ่งมุม '
        'ทำให้รูปย่อยเหลือมุมแค่ $\\dfrac{\\pi}{6}$ '
        'เมื่อไซน์เท่ากันหมดมันจะตัดทิ้งทั้งสมการ เหลือ $t(10 + 15) = (10)(15)$ '
        'จึงได้ $t = 6$ วิธีกันคือเขียนค่ามุมกำกับลงในรูปย่อยทุกรูปก่อนเริ่มคำนวณ',
        '• ได้ $12$ เพราะจำสูตรสำเร็จมาแต่ทำ $\\cos\\dfrac{A}{2}$ หล่นหาย '
        'กลายเป็น $\\dfrac{2bc}{b + c} = \\dfrac{300}{25} = 12$ '
        'ค่านี้ผิดแน่นอนเพราะมันไม่ขึ้นกับมุม $A$ เลย ทั้งที่มุม $A$ แคบหรือกว้าง '
        'ความยาวเส้นแบ่งครึ่งมุมย่อมต่างกัน ให้ใช้ข้อสังเกตนี้จับสูตรที่จำผิดได้ทันที',
        '• ได้ $5\\sqrt{7}$ เพราะเผลอไปหาด้าน $BC$ ด้วยกฎของโคไซน์ '
        'คือ $BC^{2} = 100 + 225 - 2(10)(15)\\left(\\dfrac{1}{2}\\right) = 175$ '
        'แล้วตอบค่านั้น เป็นการตอบผิดส่วน โจทย์ถามความยาวเส้นที่ลากจากจุดยอด $A$ '
        'ไม่ใช่ด้านตรงข้าม ให้ย้อนอ่านคำถามอีกรอบก่อนวงคำตอบเสมอ',
        '• ได้ค่าเกินจริงเพราะคิดว่าเส้นแบ่งครึ่งมุมแบ่งด้าน $BC$ ออกเป็นสองส่วนเท่ากัน '
        'ที่จริงส่วนที่เท่ากันคือ<b>มุม</b> ไม่ใช่<b>ด้าน</b> '
        'ด้านจะถูกแบ่งตามอัตราส่วน $AB$ ต่อ $AC$ ซึ่งข้อนี้เป็น $2$ ต่อ $3$ ไม่ใช่ $1$ ต่อ $1$',
    ],
    'V.mold: G = a triangle given by two sides and the included angle, with a cevian that bisects that '
    'angle / A = the length of the bisector itself / M = split the triangle into two sub-triangles along the '
    'bisector, write all three areas with the two-sides-and-included-angle formula, and solve the resulting '
    'linear equation for the bisector length. Rubric F3 C2 P2 T2 L1 = 10/15 with total >= 8 and T >= 2 '
    '-> level: ยาก. F = 3 for the three knowledge blocks (the area formula, the additivity of areas across '
    'the cevian, and the half-angle relation that links the big angle to the halved one). C = 2 because 7.6 '
    'supplies the half-angle bridge and 7.9 supplies the triangle-solving machinery. P = 2 for the two-stage '
    'chain (assemble the three areas into one equation, then solve). T = 2 for the two genuine keys: '
    'realising that the areas add rather than trying to compute BC first, and keeping the sub-triangle angle '
    'at half the original. L = 1 for a single-plane worded geometric context, matching the q077 precedent. '
    'The item is not ยากมาก because the total is 10 rather than 12 and neither T = 3 nor F = 3 with a '
    'turning point count of 3 is reached; the solution path, once the area split is seen, is short and has '
    'no branching. '
    'sympy (verify_b16.py): solving 1/2*10*t*sin(pi/6) + 1/2*15*t*sin(pi/6) = 1/2*10*15*sin(pi/3) returns '
    't = 6*sqrt(3) exactly, and the closed form 2*b*c*cos(A/2)/(b+c) simplifies to the same value. An '
    'independent coordinate path places A at the origin, B at (10, 0), C at 15 units along the pi/3 '
    'direction, locates D by the angle-bisector ratio D = (b*B + c*C)/(b+c), and the resulting distance '
    'simplifies to exactly 6*sqrt(3); the same path confirms the angle BAD equals pi/6, i.e. AD really does '
    'bisect. All three distractors machine-computed from named error paths: 6 = b*c/(b+c) from using the '
    'full angle in both sub-triangles, 12 = 2*b*c/(b+c) from dropping cos(A/2), and 5*sqrt(7) = BC from '
    'answering the opposite side. '
    'Collision sweep on 6397 items (bank 62 files + k1 out + k2 out), probe collide_b16e.py round 5: the '
    'phrase “แบ่งครึ่งมุม” combined with a request for the cevian length returns zero hits, and the concept '
    'probe V1g (splitting a triangle into two pieces and adding the areas) also returns zero hits in the '
    'whole corpus. The nearest relative anywhere is chap-09-vector-q98, which does use the bisector ratio '
    'AB:AC = BP:PC, but its G supplies the ratio together with a given cevian length, its A asks for '
    'cos(A/2), and its M is vector algebra, so all three axes differ. The 42 items matching “แบ่งครึ่ง” in '
    'the corpus are almost all perpendicular bisectors from the coordinate-geometry chapter.',
)

# -*- coding: utf-8 -*-
add(
    96,
    ['7.4'],
    'ง่าย',
    'ให้ $t$ เป็นจำนวนจริงซึ่ง $\\sin t \\ne 0$ และ $\\cos t \\ne 0$ '
    'นิพจน์ $\\sin t \\sec t \\cot t$ เขียนในรูปอย่างง่ายได้ตรงกับข้อใด',
    [
        '$1$',
        '$\\cot t$',
        '$\\sin t$',
        '$\\tan^2 t$',
    ],
    0,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ฟังก์ชันตรีโกณมิติหกตัวจับกันเป็นคู่ส่วนกลับสามคู่ ได้แก่ $\\sin$ กับ $\\csc$ · '
        '$\\cos$ กับ $\\sec$ · และ $\\tan$ กับ $\\cot$ คู่กลางคือคู่ที่พลาดกันมากที่สุด '
        'เพราะชื่อ $\\sec$ ไม่มีคำว่า co นำหน้า แต่กลับไปจับคู่กับ $\\cos$ เขียนเป็นสูตรคือ '
        '$\\sec t = \\dfrac{1}{\\cos t}$ ⛔ ไม่ใช่ $\\dfrac{1}{\\sin t}$',
        '• โคแทนเจนต์นิยามว่า $\\cot t = \\dfrac{\\cos t}{\\sin t}$ ซึ่งเป็นตัวกลับหัวของ '
        '$\\tan t = \\dfrac{\\sin t}{\\cos t}$ พูดสั้น ๆ คือของ $\\cot$ มี<b>โคไซน์อยู่ชั้นบน</b> '
        'คนจำนวนมากเผลอเขียนสองตัวนี้สลับกัน จึงควรเช็กทุกครั้งว่าตัวใดอยู่ชั้นบน',
        '• การคูณเศษส่วนคือคูณตัวเศษเข้ากับตัวเศษ และคูณตัวส่วนเข้ากับตัวส่วน นั่นคือ '
        '$\\dfrac{a}{b} \\cdot \\dfrac{c}{d} = \\dfrac{ac}{bd}$ ส่วนก้อนที่ไม่ได้เป็นเศษส่วน '
        'ก็ใส่ตัวส่วนเป็น $1$ ได้เสมอ เช่น $\\sin t = \\dfrac{\\sin t}{1}$',
        '• เมื่อ $a$ ไม่เป็นศูนย์ จะได้ $\\dfrac{a}{a} = 1$ เสมอ กฎเล็ก ๆ ข้อนี้คือหัวใจของการ “ตัด” '
        'ทั้งหมด และใช้ได้เฉพาะกับก้อนที่<b>คูณ</b>กันอยู่บนกับล่างเท่านั้น',
        '• คำว่า “รูปอย่างง่าย” ในโจทย์ตรีโกณหมายถึงเอกลักษณ์ คือรูปใหม่ที่มีค่าเท่ากับรูปเดิม '
        'สำหรับ $t$ <b>ทุกค่า</b>ที่นิพจน์นิยามได้ ไม่ใช่เท่ากันเฉพาะบางมุมที่บังเอิญลงตัว',
        '• เงื่อนไขที่โจทย์วางไว้ไม่ได้ใส่มาเล่น ๆ : ถ้า $\\cos t = 0$ ตัว $\\sec t$ จะหาค่าไม่ได้ '
        'และถ้า $\\sin t = 0$ ตัว $\\cot t$ จะหาค่าไม่ได้ สองเงื่อนไขนี้จึงเป็นใบอนุญาต'
        'ให้เราเดินทุกขั้นได้โดยไม่ต้องกลัวว่าจะเผลอหารด้วยศูนย์',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $t$ เป็นจำนวนจริงซึ่ง $\\sin t \\ne 0$ และ $\\cos t \\ne 0$',
        '• นิพจน์ $\\sin t \\sec t \\cot t$ ซึ่งเป็นผลคูณของฟังก์ชันสามตัว '
        'และทั้งสามตัวใช้มุมเดียวกันหมด คือ $t$',
        '• สังเกตหน้าตาก่อนลงมือ : ทั้งก้อนเป็นผลคูณล้วน ไม่มีเครื่องหมายบวกหรือลบคั่นเลยแม้แต่จุดเดียว '
        'งานหน้าตาแบบนี้แทบไม่ต้องพึ่งเอกลักษณ์พีทาโกรัส ขอเพียงแปลงทุกตัวให้เหลือไซน์กับโคไซน์ '
        'แล้วมองหาคู่ที่ตัดกันได้',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• ทำผลคูณ $\\sin t \\sec t \\cot t$ ให้เหลือรูปอย่างง่ายที่สุด แล้วเทียบว่าตรงกับหน้าตาใด',
        '',
        '<b>【 แทนนิยามของ $\\sec t$ และ $\\cot t$ กลับไปเป็นไซน์กับโคไซน์ '
        'รวมทุกก้อนเป็นเศษส่วนชั้นเดียว แล้วตัดตัวประกอบที่ซ้ำกันบนกับล่าง 】</b>',
        '',
        '<b>ขั้นที่ 1 · แทนนิยามของสองตัวที่ยังไม่ใช่ไซน์หรือโคไซน์</b>',
        '• สูตรตัวแรกที่ใช้คือ $\\sec\\alpha = \\dfrac{1}{\\cos\\alpha}$ · ระบุตัวแปร : '
        'มุมในข้อนี้คือ $t$ จึงแทน $\\alpha = t$ · ได้ $\\sec t = \\dfrac{1}{\\cos t}$',
        '• สูตรตัวที่สองคือ $\\cot\\alpha = \\dfrac{\\cos\\alpha}{\\sin\\alpha}$ · แทน $\\alpha = t$ '
        'เหมือนเดิม · ได้ $\\cot t = \\dfrac{\\cos t}{\\sin t}$',
        '• ทั้งสองบรรทัดใช้ได้จริงในข้อนี้ เพราะโจทย์รับประกันว่า $\\cos t \\ne 0$ '
        'ซึ่งเป็นตัวส่วนของ $\\sec t$ และ $\\sin t \\ne 0$ ซึ่งเป็นตัวส่วนของ $\\cot t$',
        '• นำสองบรรทัดนั้นไปวางแทนที่ในนิพจน์เดิม ได้ '
        '$\\sin t \\sec t \\cot t = \\sin t \\cdot \\dfrac{1}{\\cos t} \\cdot '
        '\\dfrac{\\cos t}{\\sin t}$',
        '• ⛔ จุดที่ต้องระวัง : ตัวประกอบตัวหน้าสุดคือ $\\sin t$ ปล่อยไว้อย่างนั้นได้เลย '
        'เพราะไซน์เป็นหนึ่งในสองตัวที่เราตั้งใจจะเก็บไว้อยู่แล้ว',
        '',
        '<b>ขั้นที่ 2 · คูณสามก้อนให้กลายเป็นเศษส่วนชั้นเดียว</b>',
        '• สูตรที่ใช้คือ $\\dfrac{a}{b} \\cdot \\dfrac{c}{d} = \\dfrac{ac}{bd}$ · '
        'ก่อนใช้ต้องทำให้ทุกก้อนอยู่ในรูปเศษส่วนเสียก่อน จึงเขียนก้อนแรกใหม่เป็น '
        '$\\sin t = \\dfrac{\\sin t}{1}$',
        '• ระบุตัวแปรทีละช่อง : ตัวเศษที่จะคูณกันคือ $\\sin t$ กับ $1$ กับ $\\cos t$ '
        'ส่วนตัวส่วนที่จะคูณกันคือ $1$ กับ $\\cos t$ กับ $\\sin t$',
        '• แทนค่าลงในสูตรแล้วยุบ : $\\dfrac{\\sin t}{1} \\cdot \\dfrac{1}{\\cos t} \\cdot '
        '\\dfrac{\\cos t}{\\sin t} = \\dfrac{\\sin t \\cdot 1 \\cdot \\cos t}'
        '{1 \\cdot \\cos t \\cdot \\sin t} = \\dfrac{\\sin t \\cos t}{\\cos t \\sin t}$',
        '• อ่านผลที่ได้ให้ชัดก่อนไปต่อ : ชั้นบนมี $\\sin t$ หนึ่งตัวกับ $\\cos t$ หนึ่งตัว '
        'ชั้นล่างก็มีอย่างละหนึ่งตัวเท่ากันเป๊ะ ต่างกันเพียงลำดับการเขียนซึ่งไม่มีผล '
        'เพราะการคูณสลับที่กันได้',
        '',
        '<b>ขั้นที่ 3 · ตัดตัวประกอบที่ซ้ำกัน แล้วสรุปว่าเหลือค่าคงตัว</b>',
        '• แยกเศษส่วนก้อนเดียวออกเป็นผลคูณของสองเศษส่วนก่อน เพื่อให้เห็นคู่ที่ตรงกันชัด ๆ : '
        '$\\dfrac{\\sin t \\cos t}{\\cos t \\sin t} = \\dfrac{\\sin t}{\\sin t} \\cdot '
        '\\dfrac{\\cos t}{\\cos t}$',
        '• ใช้กฎ $\\dfrac{a}{a} = 1$ เมื่อ $a \\ne 0$ · ระบุตัวแปรรอบแรก : $a$ คือ $\\sin t$ '
        'ซึ่งโจทย์บอกว่าไม่เป็นศูนย์ · แทนค่าได้ $\\dfrac{\\sin t}{\\sin t} = 1$',
        '• ใช้กฎเดิมอีกรอบ : คราวนี้ $a$ คือ $\\cos t$ ซึ่งไม่เป็นศูนย์เช่นกัน · แทนค่าได้ '
        '$\\dfrac{\\cos t}{\\cos t} = 1$ · คูณผลสองรอบเข้าด้วยกัน $1 \\cdot 1 = 1$ จึงได้ '
        '$\\sin t \\sec t \\cot t = 1$',
        '• ย้ำเหตุผลที่ตัดได้ : $\\sin t$ กับ $\\cos t$ เป็นก้อนที่<b>คูณ</b>กันอยู่ทั้งชั้นบนและชั้นล่าง '
        'และไม่เป็นศูนย์ทั้งคู่ ⛔ ถ้าเป็นพจน์ที่บวกกันอยู่ จะตัดแบบนี้ไม่ได้เด็ดขาด',
        '• สังเกตผลลัพธ์ให้ดี : ไม่มี $t$ หลงเหลืออยู่เลยแม้แต่ตัวเดียว แปลว่านิพจน์นี้เป็นค่าคงตัว '
        'คือได้ $1$ เท่ากันหมดทุกมุมที่นิพจน์นิยามได้ ตรงกับความหมายของเอกลักษณ์พอดี',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไม่แตะนิยามใด ๆ แต่แทนมุมจริงสองมุมแล้วคูณออกมาเป็นตัวเลข)</b>',
        '• มุมแรกใช้ $t = 30^{\\circ}$ ซึ่ง $\\sin 30^{\\circ} = \\dfrac{1}{2}$ และ '
        '$\\cos 30^{\\circ} = \\dfrac{\\sqrt{3}}{2}$',
        '• เตรียมค่าที่ต้องใช้ : $\\sec 30^{\\circ} = \\dfrac{1}{\\cos 30^{\\circ}} '
        '= \\dfrac{2}{\\sqrt{3}}$ และ $\\cot 30^{\\circ} = \\dfrac{\\cos 30^{\\circ}}'
        '{\\sin 30^{\\circ}} = \\dfrac{\\sqrt{3}/2}{1/2} = \\sqrt{3}$',
        '• คูณทั้งสามค่าเข้าด้วยกัน : $\\dfrac{1}{2} \\cdot \\dfrac{2}{\\sqrt{3}} \\cdot \\sqrt{3} '
        '= \\dfrac{1}{\\sqrt{3}} \\cdot \\sqrt{3} = 1$ ✓',
        '• มุมที่สองใช้ $t = 60^{\\circ}$ ซึ่ง $\\sin 60^{\\circ} = \\dfrac{\\sqrt{3}}{2}$ และ '
        '$\\cos 60^{\\circ} = \\dfrac{1}{2}$ จึงได้ $\\sec 60^{\\circ} = 2$ และ '
        '$\\cot 60^{\\circ} = \\dfrac{1/2}{\\sqrt{3}/2} = \\dfrac{1}{\\sqrt{3}}$',
        '• คูณทั้งสามค่าเข้าด้วยกัน : $\\dfrac{\\sqrt{3}}{2} \\cdot 2 \\cdot '
        '\\dfrac{1}{\\sqrt{3}} = \\sqrt{3} \\cdot \\dfrac{1}{\\sqrt{3}} = 1$ ✓ '
        'ได้ $1$ เท่ากับมุมแรกพอดี ซึ่งสอดคล้องกับข้อสรุปว่านิพจน์นี้เป็นค่าคงตัว',
        '• สองมุมนี้ยังใช้คัดหน้าตาที่เหลือทิ้งได้ในคราวเดียวกัน : ที่ $t = 30^{\\circ}$ '
        'ค่าที่ถูกคือ $1$ ขณะที่ $\\cot 30^{\\circ} = \\sqrt{3}$ ก็ดี $\\sin 30^{\\circ} '
        '= \\dfrac{1}{2}$ ก็ดี และ $\\tan^2 30^{\\circ} = \\dfrac{1}{3}$ ก็ดี '
        'ไม่มีค่าใดเป็น $1$ เลย · ที่ $t = 60^{\\circ}$ ก็ตกไปทั้งหมดเช่นกัน เพราะได้ '
        '$\\dfrac{1}{\\sqrt{3}}$ · $\\dfrac{\\sqrt{3}}{2}$ · และ $3$ ตามลำดับ',
        '• เหตุผลที่ไม่หยิบมุม $45^{\\circ}$ มาตรวจ : ที่มุมนั้น $\\cot 45^{\\circ} = 1$ '
        'และ $\\tan^2 45^{\\circ} = 1$ พอดีทั้งคู่ พ้องกับค่าที่ถูกทุกประการ '
        'การแทนมุมนั้นจึงยืนยันได้เพียงว่าคำตอบของเราไม่ขัดกับความจริง '
        'แต่คัดหน้าตาที่ผิดออกไม่ได้เลยแม้แต่ตัวเดียว',
        '',
        '✅ <b>คำตอบ</b> $\\sin t \\sec t \\cot t = 1$ → <b>ตัวเลือก 1</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอผลคูณของฟังก์ชันตรีโกณหลายชนิดที่มุมเดียวกัน ให้เปลี่ยนทุกตัวเป็นไซน์กับโคไซน์ก่อนเป็นอันดับแรก '
        'เพราะเมื่อเหลือเพียงสองชนิด คู่ที่ตัดกันได้จะโผล่มาให้เห็นเองโดยไม่ต้องเดา',
        '• ท่องคู่ส่วนกลับให้ติดปากเป็นคู่ ๆ : $\\sin$ กับ $\\csc$ · $\\cos$ กับ $\\sec$ · '
        '$\\tan$ กับ $\\cot$ จะเห็นว่าตัวที่มี co นำหน้าไปจับกับตัวที่ไม่มี co เสมอ '
        'จำได้แบบนี้แล้วจะไม่เขียน $\\sec t$ เป็น $\\dfrac{1}{\\sin t}$ อีก',
        '• ถ้าสิ่งที่ยุบได้เป็นค่าคงตัว การตรวจจะง่ายมาก เพราะค่าคงตัวต้องให้เลขเดิมทุกมุม '
        'แทนสองมุมแล้วได้เลขเดียวกันถือเป็นสัญญาณที่ดี แต่ถ้าได้คนละค่า '
        'แปลว่าสิ่งที่ยุบมาไม่ใช่ค่าคงตัวแน่นอน ให้ย้อนกลับไปหาที่ผิดทันที',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $\\cot t$ เพราะจำคู่ส่วนกลับสลับกัน ไปเขียนว่า $\\sec t = \\dfrac{1}{\\sin t}$ '
        'ทั้งที่นั่นคือนิยามของ $\\csc t$ เมื่อเดินต่อจึงได้ $\\sin t \\cdot \\dfrac{1}{\\sin t} '
        '\\cdot \\dfrac{\\cos t}{\\sin t} = \\dfrac{\\cos t}{\\sin t} = \\cot t$ · '
        'พิสูจน์ว่าผิดด้วยมุมจริง : ที่ $t = 60^{\\circ}$ ค่าจริงของ $\\sec 60^{\\circ}$ คือ '
        '$\\dfrac{1}{\\cos 60^{\\circ}} = 2$ ไม่ใช่ $\\dfrac{2}{\\sqrt{3}}$ '
        'และผลคูณจริงทั้งก้อนเท่ากับ $1$ ขณะที่ $\\cot 60^{\\circ} = \\dfrac{1}{\\sqrt{3}}$ '
        'ซึ่งน้อยกว่า $1$ ชัดเจน · วิธีกันคือดูตัวอักษร co ให้ครบก่อนลงมือเขียนนิยาม',
        '• ได้ $\\sin t$ เพราะเห็นชื่อ $\\sec$ กับ $\\cot$ วางติดกันแล้วเหมาเอาว่าสองตัวนี้'
        'เป็นส่วนกลับของกันและกัน จึงคูณกันได้ $1$ แล้วตัดคู่ทิ้ง เหลือ $\\sin t$ ตัวเดียว · '
        'ที่จริงส่วนกลับของ $\\sec$ คือ $\\cos$ และส่วนกลับของ $\\cot$ คือ $\\tan$ '
        'สองตัวนี้จึงไม่ใช่คู่กัน · คิดจริงจะได้ $\\sec t \\cot t = \\dfrac{1}{\\cos t} \\cdot '
        '\\dfrac{\\cos t}{\\sin t} = \\csc t$ ไม่ใช่ $1$ (ที่ $t = 30^{\\circ}$ ก้อนนี้เป็น $2$) '
        '· ค่าที่ได้จึงผิดจริง เพราะที่ $t = 30^{\\circ}$ ค่า $\\sin 30^{\\circ} '
        '= \\dfrac{1}{2}$ ไม่ใช่ $1$',
        '• ได้ $\\tan^2 t$ เพราะพลิกนิยามของ $\\cot$ กลับหัว ไปเขียนว่า $\\cot t '
        '= \\dfrac{\\sin t}{\\cos t}$ ซึ่งอันที่จริงคือนิยามของ $\\tan t$ เมื่อคูณต่อจึงได้ '
        '$\\sin t \\cdot \\dfrac{1}{\\cos t} \\cdot \\dfrac{\\sin t}{\\cos t} '
        '= \\dfrac{\\sin^2 t}{\\cos^2 t} = \\tan^2 t$ · เส้นทางนี้หน้าตาดูสมเหตุสมผล '
        'แต่ตรวจด้วยมุมจริงแล้วพังทันที : ที่ $t = 60^{\\circ}$ ได้ $\\tan^2 60^{\\circ} = 3$ '
        'ขณะที่ผลคูณจริงเป็น $1$ · ต้นตอคือจำสลับ ทั้งที่ $\\cot 60^{\\circ}$ เท่ากับ '
        '$\\dfrac{1}{\\sqrt{3}}$ ไม่ใช่ $\\sqrt{3}$',
    ],
    'V.mold: G = a bare product of three trigonometric functions at one and the same argument, two of them '
    'a reciprocal function and a quotient function / A = the equivalent simplified form / M = replace sec '
    'and cot by their sine-cosine definitions, multiply the three factors into one single-storey fraction, '
    'then cancel the two repeated factors. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 with total at most 2, T = 0 and C = 0 -> level: ง่าย. '
    'F = 1 for the one knowledge block being tested, the definition family (the sec-cos reciprocal pair and '
    'the quotient form of cot), which is recalled as a single package rather than as two separate facts. '
    'C = 0 because subtopic 7.4 alone carries the item from start to finish. P = 1 and deliberately not 2: '
    'rewriting sec and rewriting cot are two instances of the very same move made side by side, and neither '
    'feeds the other, so together they form one stage rather than a chain. The benchmarks are q087, where '
    'P = 2 was earned because a linear system had to be solved before its output could be turned into a '
    'ratio, and q091, where two parallel factorings were likewise held at P = 1. T = 0 because there is no '
    'turning point: converting to sine and cosine is the default first move here. L = 0 because the '
    'statement is pure symbols with no worded setting, as every ง่าย item must be. Scoring was written '
    'before the level was read off. '
    'sympy (verify_b18.py): simplify(sin(t)*sec(t)*cot(t)) returns exactly 1, and numeric evaluation at '
    't = pi/6 and t = pi/3 returns 1.0 to machine precision at both, matching the two hand checks in the '
    'explanation. All three distractors machine-computed from named error paths: sin(t)*(1/sin(t))*'
    '(cos(t)/sin(t)) simplifies to cot(t), the sec-as-1/sin path; sin(t)*(1/cos(t))*(sin(t)/cos(t)) '
    'simplifies to tan(t)**2, the flipped-cot path; and for the third path sympy confirms sec(t)*cot(t) '
    'simplifies to csc(t) and not to 1, so the claim that those two factors annihilate and leave sin(t) is '
    'provably false rather than merely unlucky. A separate check evaluated all four candidates at pi/4 and '
    'found 1, cot, and tan**2 all equal to 1 there, which is why the numeric verification was run at 30 and '
    '60 degrees instead. '
    'Collision sweep on 6407 items (bank 62 files + k1 out + k2 out), probe collide_b18h.py: the scan for a '
    'bare product of three trig functions sharing one argument returns 0 items corpus-wide, and the phrase '
    'for simplified form appears in the question text of only 3 items out of 6407, none of them a bare trig '
    'product. A backreference probe pushed the nearest neighbours out: chap-07-trigonometry-q137 asks for a '
    'value in terms of M and runs on reference-angle reduction, so it meets this item on G only and '
    'diverges on A and M; and the sibling q091 shares subtopic 7.4 but its G is a rational expression built '
    'from sums and its M is factoring, not definition substitution. '
    'Choices are ordered by the symbol rule (constant first, then single functions by name, then higher '
    'powers), so the answer slot is forced by that rule and was not chosen.',
)

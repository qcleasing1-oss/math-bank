# -*- coding: utf-8 -*-
add(
    78,
    ['7.7', '7.2'],
    'ยาก',
    'เซตคำตอบของสมการ $\\sin(\\pi\\cos x) = 0$ เมื่อ $0 \\le x < 2\\pi$ ตรงกับข้อใด',
    [
        '$\\{0, \\dfrac{\\pi}{2}, \\pi, \\dfrac{3\\pi}{2}\\}$',
        '$\\{0, \\pi\\}$',
        '$\\{\\dfrac{\\pi}{2}, \\dfrac{3\\pi}{2}\\}$',
        '$\\{0, \\dfrac{\\pi}{2}, \\pi, \\dfrac{3\\pi}{2}, 2\\pi\\}$',
    ],
    0,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ไซน์เป็นศูนย์ที่จำนวนเท่าของ $\\pi$ ทุกตัว นั่นคือ $\\sin A = 0$ '
        'ก็ต่อเมื่อ $A = k\\pi$ เมื่อ $k$ เป็นจำนวนเต็ม '
        'โดย $k$ เป็นจำนวนเต็มลบหรือศูนย์ก็ได้',
        '• พิสัยของโคไซน์ถูกจำกัดเสมอ นั่นคือ $-1 \\le \\cos x \\le 1$ ทุกจำนวนจริง $x$',
        '• ค่าบนวงกลมหนึ่งหน่วยที่ต้องใช้ในช่วง $0 \\le x < 2\\pi$ : '
        '$\\cos x = 1$ ที่ $x = 0$ เท่านั้น , $\\cos x = 0$ ที่ $x = \\dfrac{\\pi}{2}$ '
        'และ $x = \\dfrac{3\\pi}{2}$ , $\\cos x = -1$ ที่ $x = \\pi$ เท่านั้น',
        '• เครื่องหมาย $\\le$ ที่ปลายซ้ายกับเครื่องหมายน้อยกว่าล้วนที่ปลายขวา '
        'แปลว่าช่วงนี้รวมจุด $0$ แต่ไม่รวมจุด $2\\pi$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• สมการ $\\sin(\\pi\\cos x) = 0$ ซึ่งเป็นไซน์ที่มีโคไซน์ซ้อนอยู่ข้างใน',
        '• ช่วงที่ต้องหาคำตอบคือ $0 \\le x < 2\\pi$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาเซตของค่า $x$ ทั้งหมดในช่วงที่กำหนดซึ่งสอดคล้องกับสมการ',
        '',
        '<b>【 บีบอาร์กิวเมนต์ข้างในด้วยพิสัยของโคไซน์ แล้วแตกเป็นสมการพื้นฐานสามสมการ 】</b>',
        '',
        '<b>ขั้นที่ 1 · เปลี่ยนสมการซ้อนให้กลายเป็นเงื่อนไขของ $\\cos x$ ล้วน ๆ</b>',
        '• ⚠️ ห้ามกระจาย $\\sin$ เข้าไปในผลคูณ $\\pi\\cos x$ เพราะไซน์ไม่ได้กระจายบนผลคูณ '
        'ให้มองก้อน $\\pi\\cos x$ ทั้งก้อนเป็นอาร์กิวเมนต์ตัวเดียว แล้วตั้งชื่อว่า $A$',
        '• ใช้เงื่อนไขไซน์เป็นศูนย์กับ $A$ : $\\sin A = 0$ ก็ต่อเมื่อ $A = k\\pi$ '
        'เมื่อ $k$ เป็นจำนวนเต็ม',
        '• แทน $A = \\pi\\cos x$ กลับเข้าไป : $\\pi\\cos x = k\\pi$',
        '• หารทั้งสองข้างด้วย $\\pi$ ซึ่งไม่เป็นศูนย์ : $\\cos x = k$ เมื่อ $k$ เป็นจำนวนเต็ม',
        '',
        '<b>ขั้นที่ 2 · บีบค่า $k$ ที่เป็นไปได้ด้วยพิสัยของโคไซน์</b>',
        '• เงื่อนไขที่ได้บอกว่าโคไซน์ต้องเท่ากับจำนวนเต็มพอดี '
        'แต่โคไซน์ถูกขังอยู่ระหว่าง $-1$ กับ $1$ เสมอ จึงต้องมี $-1 \\le k \\le 1$',
        '• จำนวนเต็มที่อยู่ในช่วงนี้มีเพียงสามตัว คือ $k = -1$ , $k = 0$ และ $k = 1$',
        '• ⚠️ จุดที่พลาดกันบ่อยคือลืม $k = 0$ เพราะเผลอคิดว่าอาร์กิวเมนต์ต้องเป็นจำนวนเท่าของ $\\pi$ '
        'ที่ไม่ใช่ศูนย์ ที่จริง $\\sin 0 = 0$ ⇒ $k = 0$ ใช้ได้เต็มตัว',
        '',
        '<b>ขั้นที่ 3 · แก้สมการพื้นฐานทั้งสามบนช่วง $0 \\le x < 2\\pi$</b>',
        '• กรณี $k = -1$ ได้ $\\cos x = -1$ ซึ่งบนวงกลมหนึ่งหน่วยเกิดที่จุดซ้ายสุดเพียงจุดเดียว '
        'จึงได้ $x = \\pi$ เท่านั้น',
        '• กรณี $k = 0$ ได้ $\\cos x = 0$ ซึ่งเกิดที่จุดบนสุดและจุดล่างสุดของวงกลมหนึ่งหน่วย '
        'จึงได้ $x = \\dfrac{\\pi}{2}$ และ $x = \\dfrac{3\\pi}{2}$ รวมสองค่า',
        '• กรณี $k = 1$ ได้ $\\cos x = 1$ ซึ่งเกิดที่จุดขวาสุด จึงได้ $x = 0$ '
        'ส่วน $x = 2\\pi$ ก็ทำให้ $\\cos x = 1$ จริงเหมือนกัน '
        'แต่ ⛔ ตกไปเพราะช่วงที่โจทย์กำหนดไม่รวมปลายขวา',
        '• ⚠️ สังเกตว่าจำนวนคำตอบของแต่ละกรณีไม่เท่ากัน สองกรณีให้รากเดียว '
        'อีกกรณีให้สองราก จึงนับทีละกรณีเสมอ ห้ามเหมาว่ากรณีละสองราก',
        '',
        '<b>ขั้นที่ 4 · รวมคำตอบของทั้งสามกรณีเป็นเซตเดียว</b>',
        '• เซตคำตอบ $= \\{\\pi\\} \\cup \\{\\dfrac{\\pi}{2}, \\dfrac{3\\pi}{2}\\} \\cup \\{0\\} '
        '= \\{0, \\dfrac{\\pi}{2}, \\pi, \\dfrac{3\\pi}{2}\\}$',
        '• เซตนี้มีสมาชิกสี่ตัว และไม่มีสมาชิกซ้ำกันระหว่างกรณี',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่ากลับเข้าสมการเดิมทีละสมาชิก '
        'แล้วทดสอบค่าที่ไม่ได้อยู่ในเซตเพื่อกันการนับเกิน)</b>',
        '• ที่ $x = 0$ : $\\cos 0 = 1$ ⇒ $\\sin(\\pi \\times 1) = \\sin\\pi = 0$ ⇒ เป็นคำตอบจริง',
        '• ที่ $x = \\dfrac{\\pi}{2}$ : $\\cos\\dfrac{\\pi}{2} = 0$ ⇒ '
        '$\\sin(\\pi \\times 0) = \\sin 0 = 0$ ⇒ เป็นคำตอบจริง',
        '• ที่ $x = \\pi$ : $\\cos\\pi = -1$ ⇒ $\\sin(-\\pi) = 0$ ⇒ เป็นคำตอบจริง',
        '• ที่ $x = \\dfrac{3\\pi}{2}$ : $\\cos\\dfrac{3\\pi}{2} = 0$ ⇒ $\\sin 0 = 0$ ⇒ เป็นคำตอบจริง',
        '• ทดสอบค่าที่ไม่ได้อยู่ในเซต $x = \\dfrac{\\pi}{3}$ : $\\cos\\dfrac{\\pi}{3} = \\dfrac{1}{2}$ ⇒ '
        '$\\sin\\dfrac{\\pi}{2} = 1$ ซึ่งไม่เป็นศูนย์ ⇒ ไม่ใช่คำตอบ ถูกต้องแล้วที่ไม่นับ',
        '• ทดสอบอีกค่าหนึ่ง $x = \\dfrac{2\\pi}{3}$ : $\\cos\\dfrac{2\\pi}{3} = -\\dfrac{1}{2}$ ⇒ '
        '$\\sin\\left(-\\dfrac{\\pi}{2}\\right) = -1$ ซึ่งไม่เป็นศูนย์ ⇒ ไม่ใช่คำตอบเช่นกัน',
        '• ทุกขั้นในการแก้เป็นการเปลี่ยนรูปแบบสมมูลสองทาง ไม่ใช่การอนุมานทางเดียว '
        'เซตที่ได้จึงครบถ้วนพอดี ไม่มีคำตอบตกหล่นและไม่มีคำตอบแปลกปลอม',
        '',
        '✅ <b>คำตอบ</b> $\\{0, \\dfrac{\\pi}{2}, \\pi, \\dfrac{3\\pi}{2}\\}$ → <b>ตัวเลือก 1</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• สมการตรีโกณที่มีตรีโกณซ้อนอยู่ข้างใน ให้แก้จากชั้นนอกเข้าหาชั้นในเสมอ '
        'ชั้นนอกจะเปลี่ยนสมการให้กลายเป็นสมการพื้นฐานที่มีพารามิเตอร์จำนวนเต็มติดมาด้วย '
        'แล้วค่อยใช้พิสัยของชั้นในบีบพารามิเตอร์นั้นให้เหลือไม่กี่ค่า',
        '• ประโยคว่า “โคไซน์ต้องเท่ากับจำนวนเต็ม” เป็นกุญแจของโจทย์แนวนี้ทั้งตระกูล '
        'เพราะพิสัยแคบ ๆ ของตรีโกณตัดจำนวนเต็มทิ้งเกือบทั้งหมด เหลือเพียงสามค่าเท่านั้น '
        'ถ้าชั้นในเป็นไซน์ก็ได้ผลเหมือนกันทุกประการ',
        '• เวลาโจทย์ถามเป็น “เซตคำตอบ” ให้กลับไปอ่านเครื่องหมายที่ปลายช่วงอีกครั้งก่อนตอบ '
        'เพราะจุดปลายมักเป็นคำตอบของสมการพอดี ผู้ออกข้อสอบจึงชอบวางกับดักไว้ตรงนั้น',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $\\{\\dfrac{\\pi}{2}, \\dfrac{3\\pi}{2}\\}$ เพราะใช้เพียงกรณี $k = 0$ กรณีเดียว '
        'คือแก้แค่ $\\cos x = 0$ แล้วหยุด โดยลืมว่าพารามิเตอร์ $k$ ยังรับค่า $-1$ และ $1$ ได้อีก '
        'ให้เขียนช่วง $-1 \\le k \\le 1$ ออกมาก่อนเสมอแล้วไล่ให้ครบทุกจำนวนเต็มในช่วง',
        '• ได้ $\\{0, \\pi\\}$ เพราะใช้เพียงกรณี $k = -1$ กับ $k = 1$ '
        'โดยเข้าใจผิดว่าอาร์กิวเมนต์ของไซน์ต้องเป็นจำนวนเท่าของ $\\pi$ ที่ไม่ใช่ศูนย์ '
        'ที่จริง $\\sin 0 = 0$ อยู่แล้ว กรณี $k = 0$ จึงใช้ได้ และเป็นกรณีที่ให้คำตอบมากที่สุดถึงสองค่า',
        '• ได้ $\\{0, \\dfrac{\\pi}{2}, \\pi, \\dfrac{3\\pi}{2}, 2\\pi\\}$ เพราะไล่กรณีครบถูกต้องแล้ว '
        'แต่ใส่ $x = 2\\pi$ เข้ามาด้วย ค่านี้สอดคล้องกับสมการจริง '
        'ทว่าอยู่นอกช่วงที่โจทย์กำหนดเพราะเครื่องหมายที่ปลายขวาเป็นน้อยกว่าล้วน '
        'ให้ขีดเส้นใต้เครื่องหมายปลายช่วงไว้ตั้งแต่ตอนอ่านโจทย์',
    ],
    'V.mold: G = a nested trigonometric equation in which a cosine sits inside the argument of a sine, together '
    'with a half-open interval of length one full turn / A = the solution set itself, listed element by element, '
    'and deliberately not the sum or the count of the solutions / M = strip the outer sine to get cosine equal '
    'to an integer parameter, squeeze that parameter with the bounded range of cosine down to three values, '
    'solve each basic equation separately on the unit circle, then take the union. Rubric F2 C2 P2 T2 L0 = '
    '8/15 with T at least 2, so the level is ยาก. sympy '
    '(verify_b14.py): route 1 performs the membership test that the zero set of sine really is the set of '
    'integer multiples of pi, using two-directional contains checks rather than structural equality, then '
    'derives k in the set minus one, zero, one by the range squeeze, then calls solveset on each of the three '
    'basic equations over the half-open interval; route 2 is a numeric sweep of the absolute value of the '
    'left-hand side that is aware the function touches zero without changing sign at the extrema of cosine, so '
    'it detects local minima of the absolute value and refines each one by two hundred ternary iterations. The '
    'numeric route independently recovers exactly the same four points, and it also asserts that x equal to two '
    'pi is a genuine root before that point is filtered out by the interval condition, which is precisely the '
    'documented provenance of the five-element distractor. All three distractors machine-computed from named '
    'error paths: the two-element set of pi over two and three pi over two from using only k equal to zero, the '
    'set of zero and pi from using only k equal to plus or minus one, and the five-element set from including '
    'the excluded right endpoint. A guard asserts the four candidate sets are pairwise distinct and that no '
    'single sanity bound kills more than one distractor at a time, since the three error paths are independent '
    'of one another. Note on choice ordering: the choices here are set-valued, not numeric, so the ascending '
    'convention does not apply and the correct set is placed first. Collision sweep on 6387 items across three '
    'probe rounds: probes for a trigonometric function nested inside another, for the phrase asking for the '
    'solution set, and for the range-squeeze machinery return no item that matches on all three axes; the '
    'nearest relatives in the bank ask for the sum of the solutions of an ordinary trigonometric equation, a '
    'mold already saturated at seventy-seven items and therefore ruled off-limits, which is why this item asks '
    'for the set itself. Registry entry G-NESTED-SIN-OF-PI-COS-ASK-SET with no full triple match.',
)

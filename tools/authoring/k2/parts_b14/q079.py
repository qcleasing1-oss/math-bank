# -*- coding: utf-8 -*-
add(
    79,
    ['7.7', '7.4'],
    'ยากมาก',
    'จำนวนคำตอบของสมการ $8(\\sin^{8} x + \\cos^{8} x) = 1$ เมื่อ $0 \\le x < 2\\pi$ เท่ากับข้อใด',
    [
        '$0$',
        '$1$',
        '$2$',
        '$4$',
    ],
    3,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เอกลักษณ์หลักของบทนี้ : $\\sin^{2} x + \\cos^{2} x = 1$ '
        'ซึ่งทำให้เขียน $\\cos^{2} x$ ด้วย $\\sin^{2} x$ ได้เสมอ',
        '• กำลังคู่ยุบเป็นกำลังของกำลังสองได้ : $\\sin^{8} x = (\\sin^{2} x)^{4}$ '
        'และ $\\cos^{8} x = (\\cos^{2} x)^{4}$',
        '• พิสัยของกำลังสอง : $0 \\le \\sin^{2} x \\le 1$ ทุกจำนวนจริง $x$',
        '• การกระจายแบบสมมาตร : $(a + b)^{4} + (a - b)^{4} = 2\\left(a^{4} + 6a^{2}b^{2} + b^{4}\\right)$ '
        'ซึ่งทำให้พจน์กำลังคี่ของ $b$ หายไปหมด',
        '• มุมที่ให้ค่าไซน์เป็น $\\pm\\dfrac{1}{\\sqrt{2}}$ ในช่วง $0 \\le x < 2\\pi$ '
        'มีสี่มุม คือ $\\dfrac{\\pi}{4}$ , $\\dfrac{3\\pi}{4}$ , $\\dfrac{5\\pi}{4}$ '
        'และ $\\dfrac{7\\pi}{4}$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• สมการ $8(\\sin^{8} x + \\cos^{8} x) = 1$',
        '• ช่วงที่ต้องนับคำตอบคือ $0 \\le x < 2\\pi$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาจำนวนคำตอบของสมการในช่วงที่กำหนด ⛔ ไม่ใช่ตัวคำตอบเอง',
        '',
        '<b>【 ยุบเหลือตัวแปรเดียวด้วยเอกลักษณ์ แล้วอ่านสมการว่าเป็น “ข้างซ้ายแตะค่าต่ำสุดพอดี” 】</b>',
        '',
        '<b>ขั้นที่ 1 · ยุบสองฟังก์ชันให้เหลือตัวแปรเดียว</b>',
        '• ให้ $s = \\sin^{2} x$ แล้วเอกลักษณ์หลักให้ $\\cos^{2} x = 1 - s$ '
        'โดยพิสัยบังคับว่า $0 \\le s \\le 1$',
        '• เขียนกำลังแปดใหม่ผ่านกำลังสอง : $\\sin^{8} x = s^{4}$ และ $\\cos^{8} x = (1 - s)^{4}$',
        '• ตั้งชื่อข้างซ้ายที่ยุบแล้วว่า $P(s) = s^{4} + (1 - s)^{4}$ '
        'สมการจึงกลายเป็น $8P(s) = 1$ นั่นคือ $P(s) = \\dfrac{1}{8}$',
        '',
        '<b>ขั้นที่ 2 · หาค่าต่ำสุดของ $P$ โดยไม่ใช้แคลคูลัส ด้วยการวางจุดกึ่งกลางเป็นศูนย์กลาง</b>',
        '• สังเกตว่า $s$ กับ $1 - s$ มีผลบวกคงที่เท่ากับ $1$ เสมอ '
        'จึงเขียนทั้งคู่รอบจุดกึ่งกลางได้ว่า $s = \\dfrac{1}{2} + t$ '
        'และ $1 - s = \\dfrac{1}{2} - t$ โดย $-\\dfrac{1}{2} \\le t \\le \\dfrac{1}{2}$',
        '• ใช้การกระจายแบบสมมาตรกับ $a = \\dfrac{1}{2}$ และ $b = t$ : '
        '$P = 2\\left(\\dfrac{1}{16} + 6 \\times \\dfrac{1}{4}t^{2} + t^{4}\\right)$',
        '• ยุบตัวเลข : $P = \\dfrac{1}{8} + 3t^{2} + 2t^{4}$',
        '• ⭐ รูปนี้อ่านค่าต่ำสุดได้ทันทีโดยไม่ต้องอนุพันธ์ เพราะ $3t^{2}$ และ $2t^{4}$ '
        'ไม่เป็นลบทั้งคู่ ดังนั้น $P$ มีค่าต่ำสุดเท่ากับ $\\dfrac{1}{8}$ ที่ $t = 0$',
        '',
        '<b>ขั้นที่ 3 · อ่านสมการว่าเป็นการแตะค่าต่ำสุดพอดี</b>',
        '• สมการที่ต้องแก้คือ $P(s) = \\dfrac{1}{8}$ ซึ่งเป็นค่าต่ำสุดของ $P$ พอดีเป๊ะ '
        'ไม่ใช่ค่าที่อยู่สูงกว่าค่าต่ำสุด',
        '• แทนรูปที่ยุบแล้ว : $\\dfrac{1}{8} + 3t^{2} + 2t^{4} = \\dfrac{1}{8}$ '
        'จึงเหลือ $3t^{2} + 2t^{4} = 0$',
        '• ดึงตัวร่วม : $t^{2}\\left(3 + 2t^{2}\\right) = 0$ '
        'โดยวงเล็บหลังเป็นจำนวนบวกเสมอเพราะมีค่าอย่างน้อย $3$ '
        'จึงบังคับให้ $t^{2} = 0$ นั่นคือ $t = 0$ เพียงค่าเดียว',
        '• ย้อนกลับเป็นตัวแปร $s$ : $s = \\dfrac{1}{2}$ ซึ่งอยู่ในพิสัย $0 \\le s \\le 1$ จริง',
        '• ⚠️ ถึงตรงนี้ยังตอบไม่ได้ เพราะสิ่งที่นับได้คือจำนวนค่าของ $s$ ไม่ใช่จำนวนค่าของ $x$',
        '',
        '<b>ขั้นที่ 4 · แปลค่าของ $s$ กลับเป็นจำนวนมุมในช่วงที่กำหนด</b>',
        '• จาก $s = \\sin^{2} x = \\dfrac{1}{2}$ ได้ $\\sin x = \\dfrac{1}{\\sqrt{2}}$ '
        'หรือ $\\sin x = -\\dfrac{1}{\\sqrt{2}}$ '
        'เพราะการถอดรากของกำลังสองให้ทั้งค่าบวกและค่าลบ',
        '• กรณีค่าบวกให้มุมในจตุภาคที่หนึ่งและที่สอง คือ $x = \\dfrac{\\pi}{4}$ '
        'และ $x = \\dfrac{3\\pi}{4}$',
        '• กรณีค่าลบให้มุมในจตุภาคที่สามและที่สี่ คือ $x = \\dfrac{5\\pi}{4}$ '
        'และ $x = \\dfrac{7\\pi}{4}$',
        '• ทั้งสี่ค่าอยู่ในช่วง $0 \\le x < 2\\pi$ ทั้งหมด จำนวนคำตอบจึงเท่ากับ $4$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ใช้อนุพันธ์หาค่าต่ำสุดแทนการกระจายแบบสมมาตร '
        'แล้วยืนยันจำนวนมุมด้วยคาบของฟังก์ชัน)</b>',
        '• หาจุดวิกฤตของ $P$ ด้วยอนุพันธ์ : $P\'(s) = 4s^{3} - 4(1 - s)^{3}$ '
        'ให้เท่ากับศูนย์จะได้ $s^{3} = (1 - s)^{3}$',
        '• การยกกำลังสามเป็นฟังก์ชันหนึ่งต่อหนึ่งบนจำนวนจริง จึงได้ $s = 1 - s$ '
        'นั่นคือ $s = \\dfrac{1}{2}$ เป็นจุดวิกฤตเพียงจุดเดียว '
        'และ $P\\left(\\dfrac{1}{2}\\right) = 2 \\times \\dfrac{1}{16} = \\dfrac{1}{8}$ ตรงกัน',
        '• ตรวจปลายพิสัยด้วย : $P(0) = 1$ และ $P(1) = 1$ ซึ่งมากกว่า $\\dfrac{1}{8}$ ทั้งคู่ '
        'ยืนยันว่าจุดวิกฤตนั้นเป็นค่าต่ำสุดจริง สมการจึงมีรากในตัวแปร $s$ เพียงรากเดียว',
        '• แทนค่ากลับเข้าสมการเดิมที่ $x = \\dfrac{\\pi}{4}$ : '
        '$\\sin^{8}\\dfrac{\\pi}{4} + \\cos^{8}\\dfrac{\\pi}{4} '
        '= 2 \\times \\left(\\dfrac{1}{\\sqrt{2}}\\right)^{8} = 2 \\times \\dfrac{1}{16} = \\dfrac{1}{8}$ '
        'คูณแปดได้ $1$ พอดี',
        '• ยืนยันจำนวนด้วยความสมมาตร : ฟังก์ชัน $\\sin^{8} x + \\cos^{8} x$ มีคาบเท่ากับ '
        '$\\dfrac{\\pi}{2}$ และในหนึ่งคาบมีมุมที่ทำให้ $\\sin^{2} x = \\dfrac{1}{2}$ เพียงมุมเดียว '
        'ช่วง $0 \\le x < 2\\pi$ ยาวเท่ากับสี่คาบพอดี จึงได้ $4$ คำตอบ ตรงกับที่ไล่มาทีละมุม',
        '',
        '✅ <b>คำตอบ</b> $4$ → <b>ตัวเลือก 4</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เมื่อเห็นกำลังคู่สูง ๆ ของไซน์บวกโคไซน์ ให้เปลี่ยนตัวแปรเป็น $s = \\sin^{2} x$ ทันที '
        'โจทย์ตระกูลนี้จะยุบเหลือพหุนามตัวแปรเดียวบนช่วงปิด $[0, 1]$ เสมอ '
        'แล้วปัญหาตรีโกณก็กลายเป็นปัญหาพีชคณิตล้วน',
        '• พอเห็นว่าสองก้อนมีผลบวกคงที่ ให้วางตัวแปรใหม่ไว้ที่จุดกึ่งกลางเป็น '
        '$\\dfrac{1}{2} + t$ กับ $\\dfrac{1}{2} - t$ พจน์กำลังคี่จะตัดกันหมด '
        'เหลือรูปที่อ่านค่าต่ำสุดออกด้วยตาโดยไม่ต้องใช้แคลคูลัสเลย',
        '• สมการที่ตั้งค่าไว้เท่ากับค่าต่ำสุดพอดีคือสมการที่ “แตะแล้วเด้ง” '
        'มันให้รากในตัวแปรที่ยุบแล้วเพียงรากเดียว แต่จำนวนมุมที่ได้กลับมามักมากกว่านั้นหลายเท่า '
        'ให้แยกให้ขาดระหว่างจำนวนรากของตัวแปรแทนกับจำนวนคำตอบที่โจทย์ถาม',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $0$ เพราะจำค่าต่ำสุดผิดชั้น โดยยกค่าต่ำสุดของ $\\sin^{6} x + \\cos^{6} x$ '
        'ซึ่งเท่ากับ $\\dfrac{1}{4}$ มาใช้กับกำลังแปด แล้วสรุปว่าข้างซ้ายมีค่าอย่างน้อย '
        '$8 \\times \\dfrac{1}{4} = 2$ ซึ่งมากกว่า $1$ จึงตัดสินว่าไม่มีคำตอบ '
        'ที่จริงกำลังยิ่งสูง ค่าต่ำสุดยิ่งลดลง กำลังแปดให้ $\\dfrac{1}{8}$ ไม่ใช่ $\\dfrac{1}{4}$',
        '• ได้ $1$ เพราะหยุดนับที่ตัวแปรแทน เมื่อแก้ได้ $s = \\dfrac{1}{2}$ เพียงค่าเดียว '
        'ก็ตอบว่ามีคำตอบเดียวทันที โดยลืมว่าคำถามถามจำนวนค่าของ $x$ '
        'และการถอดกำลังสองย้อนกลับทำให้หนึ่งค่าของ $s$ แตกเป็นหลายมุม',
        '• ได้ $2$ เพราะถอดรากแล้วเก็บเฉพาะเครื่องหมายบวก คือใช้แค่ '
        '$\\sin x = \\dfrac{1}{\\sqrt{2}}$ จึงได้เพียงสองมุมในครึ่งบนของวงกลมหนึ่งหน่วย '
        'ที่จริง $\\sin^{2} x = \\dfrac{1}{2}$ ยอมรับค่าลบด้วย ซึ่งเพิ่มมุมในครึ่งล่างอีกสองมุม',
    ],
    'V.mold: G = an equation whose left side is a high even power sum of sine and cosine scaled by a constant '
    'chosen so that the equation states exactly that the left side attains its own minimum / A = the count of '
    'solutions on one full turn, deliberately not the sum of the solutions nor the value of the expression / '
    'M = reduce to one variable through the Pythagorean identity, recognise the touch-the-floor reading of the '
    'equation, solve the resulting single-root algebraic condition, then unfold the square root back into four '
    'angles. Rubric F3 C3 P2 T3 L1 = 12/15 with T equal to 3, so the level is ยากมาก. sympy (verify_b14.py): '
    'route 1 forms the polynomial s to the fourth plus one minus s to the fourth, confirms by solve that its '
    'derivative has exactly one real critical point at one half and that the minimum value there is one eighth, '
    'then substitutes back and enumerates the four angles with solveset over the half-open interval; route 2 '
    'avoids calculus completely by expanding one half plus t to the fourth plus one half minus t to the fourth '
    'into one eighth plus three t squared plus two t to the fourth and reading the minimum off the non-negative '
    'terms, and it separately computes sp.minimum of the sixth power sum as one quarter, which is the machine '
    'provenance of the zero distractor. All three distractors machine-computed from named error paths: zero '
    'from carrying the sixth-power minimum of one quarter over to the eighth power, one from stopping at the '
    'single root in the reduced variable, and two from keeping only the positive square root. A guard asserts '
    'the four counts are distinct and that no single sanity bound eliminates more than one of them, since a '
    'student who tests only the angle pi over four confirms that solutions exist, which kills zero but leaves '
    'one and two both alive. Collision sweep on 6387 items across three probe rounds: probes for eighth powers '
    'of sine and cosine, for the count-the-solutions ask, and for the sum-is-constant substitution return no '
    'item matching on all three axes; the sixth-power identity appears in the bank only as an expression '
    'evaluation, never as an equation set equal to its own minimum, and the saturated sum-of-solutions mold at '
    'seventy-seven items is avoided by asking for the count instead. Registry entry '
    'G-EIGHTH-POWER-TOUCHES-MINIMUM-COUNT-ROOTS with no full triple match.',
)

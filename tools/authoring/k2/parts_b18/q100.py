# -*- coding: utf-8 -*-
add(
    100,
    ['7.4'],
    'ปานกลาง',
    'ให้ $\\theta$ เป็นจำนวนจริงซึ่ง $\\sin\\theta \\ne \\cos\\theta$ '
    'และ $\\sin\\theta\\cos\\theta \\ne 0$ '
    'นิพจน์ $\\dfrac{\\sin\\theta}{1-\\cot\\theta} + \\dfrac{\\cos\\theta}{1-\\tan\\theta}$ '
    'เท่ากับข้อใด',
    [
        '$\\dfrac{1}{\\sin\\theta - \\cos\\theta}$',
        '$\\sin\\theta + \\cos\\theta$',
        '$\\sin\\theta - \\cos\\theta$',
        '$\\tan\\theta + \\cot\\theta$',
    ],
    1,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ฟังก์ชันตรีโกณทุกตัวเขียนกลับมาเป็น $\\sin$ กับ $\\cos$ ได้เสมอ '
        'โดย $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        'และ $\\cot\\theta = \\dfrac{\\cos\\theta}{\\sin\\theta}$ '
        'เวลาเจอนิพจน์ที่มีหลายฟังก์ชันปนกัน ให้แปลงทุกตัวลงมาเป็นสองตัวนี้ก่อน '
        'เพราะของที่อยู่ในภาษาเดียวกันเท่านั้นถึงจะบวกลบตัดกันได้',
        '• การลบเศษส่วนออกจากเลข $1$ ต้องทำตัวส่วนให้เหมือนกันก่อน '
        'โดยมองว่า $1 = \\dfrac{b}{b}$ จะได้ '
        '$1 - \\dfrac{a}{b} = \\dfrac{b}{b} - \\dfrac{a}{b} = \\dfrac{b-a}{b}$ '
        '⛔ จุดที่พลาดกันบ่อยคือลำดับการลบ ตัวที่มาแทนเลข $1$ ต้องอยู่หน้าเสมอ',
        '• เศษส่วนซ้อนเศษส่วน ให้กลับตัวหารแล้วคูณ นั่นคือ '
        '$\\dfrac{A}{\\dfrac{B}{C}} = A \\times \\dfrac{C}{B}$ '
        'พูดเป็นภาษาคนว่า “หารด้วยเศษส่วน เท่ากับ คูณด้วยส่วนกลับของเศษส่วนนั้น”',
        '• ก้อน $a - b$ กับก้อน $b - a$ ต่างกันแค่เครื่องหมายลบตัวเดียว '
        'จึงย้ายไปมาได้ด้วยกฎ $\\dfrac{X}{b-a} = -\\dfrac{X}{a-b}$ '
        'กฎนี้คือกุญแจของข้อนี้ เพราะมันทำให้เศษส่วนสองก้อนที่ตัวส่วนดูไม่เหมือนกัน '
        'กลายเป็นตัวส่วนเดียวกันได้ทันที',
        '• การแยกตัวประกอบผลต่างกำลังสอง : $a^2 - b^2 = (a-b)(a+b)$ '
        'ใช้เมื่อเห็นของยกกำลังสองสองก้อนลบกัน ตัวประกอบที่ได้จะเป็นคู่ผลต่างคูณผลบวก',
        '• เอกลักษณ์พีทาโกรัส $\\sin^2\\theta + \\cos^2\\theta = 1$ '
        '⛔ ระวังให้ดีว่าเอกลักษณ์นี้ใช้กับการ<b>บวก</b>กันเท่านั้น '
        'ถ้าเจอ $\\sin^2\\theta - \\cos^2\\theta$ ซึ่งเป็นการลบ จะยุบเป็น $1$ ไม่ได้เด็ดขาด',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• นิพจน์ที่ต้องจัดรูปคือ '
        '$\\dfrac{\\sin\\theta}{1-\\cot\\theta} + \\dfrac{\\cos\\theta}{1-\\tan\\theta}$',
        '• เงื่อนไข $\\sin\\theta\\cos\\theta \\ne 0$ '
        'มีไว้ให้ $\\tan\\theta$ และ $\\cot\\theta$ นิยามได้ทั้งคู่',
        '• เงื่อนไข $\\sin\\theta \\ne \\cos\\theta$ '
        'มีไว้กันไม่ให้ตัวส่วนเป็นศูนย์ และยังเป็นใบอนุญาตให้ตัดก้อน '
        '$\\sin\\theta - \\cos\\theta$ ทิ้งได้ในขั้นสุดท้าย',
        '• สังเกตหน้าตาก่อนลงมือ : สองพจน์นี้เป็นฝาแฝดที่สลับ $\\sin$ กับ $\\cos$ กันพอดี '
        'เมื่อจัดเสร็จ ตัวส่วนของทั้งคู่จะเป็นก้อนเดียวกันแต่กลับด้านกัน '
        'ความสมมาตรนี้บอกล่วงหน้าว่างานหลักของข้อนี้อยู่ที่<b>เครื่องหมาย</b> ไม่ใช่การคำนวณหนัก ๆ',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• ยุบผลบวกของเศษส่วนซ้อนสองก้อนนี้ให้เหลือรูปอย่างง่ายที่สุด',
        '',
        '<b>【 แปลง $\\cot\\theta$ กับ $\\tan\\theta$ เป็น $\\sin\\theta$ และ $\\cos\\theta$ '
        'เพื่อยุบเศษส่วนซ้อนของแต่ละพจน์ แล้วพลิกเครื่องหมายตัวส่วนของพจน์ที่สองให้ตรงกับพจน์แรก '
        'จากนั้นแยกตัวประกอบผลต่างกำลังสองแล้วตัดทิ้ง 】</b>',
        '',
        '<b>ขั้นที่ 1 · เปลี่ยนทุกฟังก์ชันให้เป็นไซน์กับโคไซน์ แล้วยุบตัวส่วนของแต่ละพจน์</b>',
        '• สูตรที่ใช้ : $\\cot\\theta = \\dfrac{\\cos\\theta}{\\sin\\theta}$ '
        'และ $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ '
        'พร้อมกฎรวมเศษส่วน $1 - \\dfrac{a}{b} = \\dfrac{b-a}{b}$',
        '• ระบุตัวแปรของกฎรวมเศษส่วนสำหรับตัวส่วนพจน์แรก : $a$ คือ $\\cos\\theta$ '
        'และ $b$ คือ $\\sin\\theta$',
        '• แทนค่า ได้ตัวส่วนพจน์แรกเป็น '
        '$1 - \\cot\\theta = 1 - \\dfrac{\\cos\\theta}{\\sin\\theta} '
        '= \\dfrac{\\sin\\theta}{\\sin\\theta} - \\dfrac{\\cos\\theta}{\\sin\\theta} '
        '= \\dfrac{\\sin\\theta - \\cos\\theta}{\\sin\\theta}$',
        '• ทำแบบเดียวกันกับตัวส่วนพจน์ที่สอง คราวนี้ $a$ คือ $\\sin\\theta$ '
        'และ $b$ คือ $\\cos\\theta$ จึงได้ '
        '$1 - \\tan\\theta = 1 - \\dfrac{\\sin\\theta}{\\cos\\theta} '
        '= \\dfrac{\\cos\\theta - \\sin\\theta}{\\cos\\theta}$',
        '• ⛔ หยุดดูให้ดีตรงนี้ : ตัวเศษของสองก้อนที่ได้คือ $\\sin\\theta - \\cos\\theta$ '
        'กับ $\\cos\\theta - \\sin\\theta$ ซึ่ง<b>เรียงกลับด้านกัน</b> '
        'ห้ามมองผ่านว่าเป็นก้อนเดียวกัน เพราะมันต่างกันหนึ่งเครื่องหมายลบ',
        '',
        '<b>ขั้นที่ 2 · ยุบพจน์แรกให้เป็นเศษส่วนชั้นเดียว</b>',
        '• สูตรที่ใช้ : $\\dfrac{A}{\\dfrac{B}{C}} = A \\times \\dfrac{C}{B}$',
        '• ระบุตัวแปร : $A$ คือ $\\sin\\theta$ ซึ่งเป็นตัวเศษเดิม · '
        '$B$ คือ $\\sin\\theta - \\cos\\theta$ · $C$ คือ $\\sin\\theta$',
        '• แทนค่า ได้ '
        '$\\dfrac{\\sin\\theta}{\\dfrac{\\sin\\theta - \\cos\\theta}{\\sin\\theta}} '
        '= \\sin\\theta \\times \\dfrac{\\sin\\theta}{\\sin\\theta - \\cos\\theta}$',
        '• ยุบผลคูณ ได้พจน์แรกเป็น $\\dfrac{\\sin^2\\theta}{\\sin\\theta - \\cos\\theta}$ '
        'ตัวเศษกลายเป็นกำลังสองเพราะ $\\sin\\theta$ ตัวเดิมถูกคูณด้วย $\\sin\\theta$ '
        'ที่ยกขึ้นมาจากตัวส่วนชั้นใน',
        '',
        '<b>ขั้นที่ 3 · ยุบพจน์ที่สอง แล้วพลิกเครื่องหมายตัวส่วนให้ตรงกับพจน์แรก</b>',
        '• ใช้สูตรเศษส่วนซ้อนตัวเดิม โดยคราวนี้ $A$ คือ $\\cos\\theta$ · '
        '$B$ คือ $\\cos\\theta - \\sin\\theta$ · $C$ คือ $\\cos\\theta$',
        '• แทนค่า ได้ '
        '$\\dfrac{\\cos\\theta}{\\dfrac{\\cos\\theta - \\sin\\theta}{\\cos\\theta}} '
        '= \\cos\\theta \\times \\dfrac{\\cos\\theta}{\\cos\\theta - \\sin\\theta} '
        '= \\dfrac{\\cos^2\\theta}{\\cos\\theta - \\sin\\theta}$',
        '• ตอนนี้ตัวส่วนของสองพจน์ยังไม่เหมือนกัน จึงบวกกันตรง ๆ ไม่ได้ '
        'ใช้กฎพลิกเครื่องหมาย $\\dfrac{X}{b-a} = -\\dfrac{X}{a-b}$ '
        'โดยให้ $X$ คือ $\\cos^2\\theta$ · $a$ คือ $\\sin\\theta$ · $b$ คือ $\\cos\\theta$',
        '• แทนค่า ได้ $\\dfrac{\\cos^2\\theta}{\\cos\\theta - \\sin\\theta} '
        '= -\\dfrac{\\cos^2\\theta}{\\sin\\theta - \\cos\\theta}$ '
        'ผลที่ได้คือตัวส่วนของสองพจน์เท่ากันแล้ว แต่พจน์ที่สองติดลบมาด้วย '
        'เครื่องหมายลบตัวนี้คือหัวใจของข้อนี้ทั้งข้อ',
        '',
        '<b>ขั้นที่ 4 · บวกสองพจน์ แล้วแยกตัวประกอบผลต่างกำลังสองเพื่อตัดทิ้ง</b>',
        '• นำผลจากสองขั้นที่แล้วมาบวกกัน : '
        '$\\dfrac{\\sin^2\\theta}{\\sin\\theta - \\cos\\theta} '
        '+ \\left(-\\dfrac{\\cos^2\\theta}{\\sin\\theta - \\cos\\theta}\\right) '
        '= \\dfrac{\\sin^2\\theta - \\cos^2\\theta}{\\sin\\theta - \\cos\\theta}$',
        '• ⛔ ตัวเศษเป็นการ<b>ลบ</b>กัน จึงห้ามยุบเป็น $1$ ด้วยเอกลักษณ์พีทาโกรัส '
        'ของที่ยุบเป็น $1$ ได้ต้องเป็น $\\sin^2\\theta + \\cos^2\\theta$ ซึ่งเป็นการบวก',
        '• สูตรที่ใช้แทนคือผลต่างกำลังสอง : $a^2 - b^2 = (a-b)(a+b)$ '
        'ระบุตัวแปร $a$ คือ $\\sin\\theta$ และ $b$ คือ $\\cos\\theta$',
        '• แทนค่า ได้ตัวเศษเป็น '
        '$\\sin^2\\theta - \\cos^2\\theta = (\\sin\\theta - \\cos\\theta)(\\sin\\theta + \\cos\\theta)$',
        '• เขียนรวมทั้งก้อน : '
        '$\\dfrac{(\\sin\\theta - \\cos\\theta)(\\sin\\theta + \\cos\\theta)}'
        '{\\sin\\theta - \\cos\\theta}$ '
        'มีก้อน $\\sin\\theta - \\cos\\theta$ อยู่ทั้งบนและล่าง จึงตัดกันได้ '
        'และตัดได้อย่างถูกกฎเพราะโจทย์กำหนดไว้แล้วว่า $\\sin\\theta \\ne \\cos\\theta$ '
        'ก้อนนี้จึงไม่เป็นศูนย์',
        '• เหลือคำตอบสุดท้าย $\\sin\\theta + \\cos\\theta$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไม่จัดรูปเชิงสัญลักษณ์เลย แต่แทนมุมจริงลงทั้งสองข้างแล้วเทียบตัวเลข)</b>',
        '• เลือกมุมทดสอบ $\\theta = \\dfrac{\\pi}{6}$ ซึ่งใช้ได้ เพราะ '
        '$\\sin\\dfrac{\\pi}{6} = \\dfrac{1}{2}$ ไม่เท่ากับ '
        '$\\cos\\dfrac{\\pi}{6} = \\dfrac{\\sqrt{3}}{2}$ และทั้งคู่ไม่เป็นศูนย์',
        '• ค่าที่ต้องใช้ : $\\cot\\dfrac{\\pi}{6} = \\sqrt{3}$ '
        'และ $\\tan\\dfrac{\\pi}{6} = \\dfrac{1}{\\sqrt{3}}$',
        '• พจน์แรกของนิพจน์ต้นทาง : '
        '$\\dfrac{\\dfrac{1}{2}}{1-\\sqrt{3}} = \\dfrac{1}{2(1-\\sqrt{3})} '
        '= -\\dfrac{1}{2(\\sqrt{3}-1)}$',
        '• พจน์ที่สอง : ตัวส่วนคือ '
        '$1 - \\dfrac{1}{\\sqrt{3}} = \\dfrac{\\sqrt{3}-1}{\\sqrt{3}}$ จึงได้ '
        '$\\dfrac{\\sqrt{3}}{2} \\times \\dfrac{\\sqrt{3}}{\\sqrt{3}-1} '
        '= \\dfrac{3}{2(\\sqrt{3}-1)}$',
        '• บวกกัน : $-\\dfrac{1}{2(\\sqrt{3}-1)} + \\dfrac{3}{2(\\sqrt{3}-1)} '
        '= \\dfrac{2}{2(\\sqrt{3}-1)} = \\dfrac{1}{\\sqrt{3}-1}$ '
        'คูณทั้งบนและล่างด้วย $\\sqrt{3}+1$ เพื่อทำตัวส่วนให้เป็นจำนวนตรรกยะ ได้ '
        '$\\dfrac{\\sqrt{3}+1}{3-1} = \\dfrac{\\sqrt{3}+1}{2}$ ซึ่งมีค่าประมาณ $1.366$',
        '• เทียบกับคำตอบที่จัดรูปได้ : $\\sin\\dfrac{\\pi}{6} + \\cos\\dfrac{\\pi}{6} '
        '= \\dfrac{1}{2} + \\dfrac{\\sqrt{3}}{2} = \\dfrac{1+\\sqrt{3}}{2}$ '
        'ซึ่งมีค่าประมาณ $1.366$ เท่ากันพอดี ✓ '
        'ตัวเลขนี้ยังคัดค่าหลอกทิ้งได้หมดในคราวเดียว เพราะไม่มีค่าใดที่เหลือให้ผลลัพธ์ $1.366$ อีกเลย',
        '',
        '✅ <b>คำตอบ</b> นิพจน์นี้ยุบได้เป็น $\\sin\\theta + \\cos\\theta$ → <b>ตัวเลือก 2</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอนิพจน์ที่มีสองพจน์สลับ $\\sin$ กับ $\\cos$ กันแบบสมมาตร ให้เดาไว้ก่อนเลยว่า '
        'ตัวส่วนที่จัดออกมาจะกลับด้านกัน แล้วรีบเขียนกฎ $\\dfrac{X}{b-a} = -\\dfrac{X}{a-b}$ '
        'ไว้ข้าง ๆ กระดาษ จะได้ไม่ลืมพลิกเครื่องหมายตอนรวมพจน์',
        '• กฎเร็วสำหรับจำ : $\\sin^2\\theta + \\cos^2\\theta$ ที่เป็นการบวกเท่านั้นจึงยุบเป็น $1$ ได้ '
        'ส่วน $\\sin^2\\theta - \\cos^2\\theta$ ที่เป็นการลบให้คิดถึงผลต่างกำลังสองทันที '
        'เพราะโจทย์แนวจัดรูปมักวางกับดักไว้ตรงนี้พอดี',
        '• เมื่อจัดรูปเสร็จแล้วไม่มั่นใจ ให้แทนมุมง่าย ๆ อย่าง $\\dfrac{\\pi}{6}$ '
        'หรือ $\\dfrac{\\pi}{3}$ ลงทั้งนิพจน์ต้นทางและคำตอบที่ได้ '
        'ถ้าตัวเลขสองฝั่งไม่ตรงกัน แปลว่าจัดรูปพลาดแน่นอน วิธีนี้ใช้เวลาไม่ถึงหนึ่งนาทีแต่กันพลาดได้เกือบทั้งหมด',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\dfrac{1}{\\sin\\theta - \\cos\\theta}$ เพราะลืมพลิกเครื่องหมายในขั้นที่ 3 '
        'คือเห็นตัวส่วน $\\cos\\theta - \\sin\\theta$ แล้วเหมาว่าเป็นก้อนเดียวกับ '
        '$\\sin\\theta - \\cos\\theta$ จึงเอาตัวเศษมาบวกกันตรง ๆ ได้ '
        '$\\dfrac{\\sin^2\\theta + \\cos^2\\theta}{\\sin\\theta - \\cos\\theta} '
        '= \\dfrac{1}{\\sin\\theta - \\cos\\theta}$ · '
        'ค่านี้ผิดจริง ตรวจได้ด้วยการแทน $\\theta = \\dfrac{\\pi}{6}$ '
        'จะได้ $\\dfrac{1}{\\dfrac{1}{2} - \\dfrac{\\sqrt{3}}{2}} = \\dfrac{2}{1-\\sqrt{3}} '
        '= -(1+\\sqrt{3})$ ซึ่งประมาณ $-2.732$ '
        'ติดลบ ทั้งที่นิพจน์ต้นทางที่มุมเดียวกันคำนวณได้ $1.366$ ซึ่งเป็นบวก',
        '• ได้ค่า $\\sin\\theta - \\cos\\theta$ เพราะเดินมาถูกจนถึง '
        '$\\dfrac{\\sin^2\\theta - \\cos^2\\theta}{\\sin\\theta - \\cos\\theta}$ '
        'แล้วไปตัดทอนแบบผิดกฎในขั้นสุดท้าย คือหารทีละพจน์เอาเองว่า '
        '$\\sin^2\\theta \\div \\sin\\theta = \\sin\\theta$ และ '
        '$\\cos^2\\theta \\div \\cos\\theta = \\cos\\theta$ '
        'ทั้งที่ตัวส่วนเป็นก้อนบวกลบ จะตัดได้ก็ต่อเมื่อแยกตัวประกอบตัวเศษออกมาเป็นก้อนคูณกันก่อนเท่านั้น · '
        'ค่านี้ผิดจริง เพราะที่ $\\theta = \\dfrac{\\pi}{6}$ ได้ '
        '$\\dfrac{1}{2} - \\dfrac{\\sqrt{3}}{2} = \\dfrac{1-\\sqrt{3}}{2}$ '
        'ซึ่งประมาณ $-0.366$ ไม่ใช่ $1.366$ · '
        'สังเกตว่าค่านี้เป็นส่วนกลับของค่าหลอกตัวแรกพอดี ทั้งคู่จึงมาจากการจัดการเครื่องหมายที่ตัวส่วนพลาดเหมือนกัน',
        '• ได้ค่า $\\tan\\theta + \\cot\\theta$ เพราะสับสนของข้ามพจน์ตอนรวมเศษส่วน '
        'คือเห็นว่าพจน์แรกต้องคูณด้วย $\\sin\\theta$ และพจน์ที่สองต้องคูณด้วย $\\cos\\theta$ '
        'แล้วเหมาเอาว่าตัวส่วนร่วมคือผลคูณ $\\sin\\theta\\cos\\theta$ '
        'พร้อมกับบวกตัวเศษได้ $\\sin^2\\theta + \\cos^2\\theta = 1$ '
        'จึงลงเอยที่ $\\dfrac{1}{\\sin\\theta\\cos\\theta}$ '
        'ซึ่งเท่ากับ $\\tan\\theta + \\cot\\theta$ พอดี · '
        'ค่านี้ผิดจริง เพราะที่ $\\theta = \\dfrac{\\pi}{6}$ ได้ '
        '$\\sqrt{3} + \\dfrac{1}{\\sqrt{3}} = \\dfrac{4\\sqrt{3}}{3}$ ซึ่งประมาณ $2.309$ '
        'ห่างจาก $1.366$ อยู่มาก · '
        'ที่พลาดเพราะเอาตัวคูณที่ใช้ล้างเศษส่วนซ้อนไปปนกับตัวส่วนร่วม ซึ่งเป็นคนละหน้าที่กัน',
        '• อีกทางที่พลาดกันบ่อยคือพลิกเครื่องหมายผิดข้าง ไปพลิกตัวส่วนของพจน์แรกแทนพจน์ที่สอง '
        'จะได้ $\\dfrac{\\cos^2\\theta - \\sin^2\\theta}{\\cos\\theta - \\sin\\theta} '
        '= -(\\sin\\theta + \\cos\\theta)$ '
        'ซึ่งที่ $\\theta = \\dfrac{\\pi}{6}$ มีค่าประมาณ $-1.366$ ติดลบสวนทางกับค่าจริง · '
        'วิธีกันคือเลือกก้อนตัวส่วนที่จะยึดเป็นหลักไว้ก่อนหนึ่งก้อน แล้วบังคับให้อีกพจน์วิ่งมาหาก้อนนั้นเสมอ '
        'อย่าพลิกทั้งสองฝั่งสลับไปมา',
    ],
    'V.mold: G = a two-term sum of compound fractions in one real angle theta, each term a bare trig '
    'function over 1 minus a cofunction ratio, with the guards sin != cos and sin*cos != 0 / A = the '
    'simplified closed form of that sum / M = rewrite cot and tan as ratios, clear each compound '
    'fraction, see that the two denominators are one block written in opposite order, flip the sign of '
    'one so they match, then factor the difference of squares and cancel under the guard sin != cos. '
    'Rubric F2 C1 P2 T1 L0 = 6/15 -> level: ปานกลาง. F = 2 because two knowledge blocks are needed and '
    'neither can be skipped: the quotient identities, and the difference-of-squares factorisation that '
    'unlocks the cancellation; q096, finished by one string of reciprocal identities, is the F = 1 line. '
    'C = 1 because subtopic 7.4 supplies the identities while the closing move borrows one outside tool, '
    'factorisation, and no more. P = 2 and not 3 because the work splits into exactly two stages, each '
    'term reduced to a single-storey fraction and only then combined and cancelled, the second stage '
    'reinterpreting what the first produced; benchmark q086, against q091 which set the P = 1 line for '
    'moves that merely sit side by side. T = 1 and not 2 because the sign flip is a genuine turning point '
    'but the shape of the two denominators announces it rather than hiding it, the q097 benchmark for a '
    'decisive fact left visible. L = 0 because the statement is bare symbol work with no scene to model, '
    'benchmarks q030 and q060. Scoring was written before the level was read off. '
    'sympy (verify_b18.py): simplify(sin(th)/(1 - cot(th)) + cos(th)/(1 - tan(th)) - (sin(th) + cos(th))) '
    'returns 0, so the identity is exact and not merely true at sample points, and the same expression at '
    'th = 3/10, 9/10 and 23/10 radians returned 0 each time. Every distractor was machine-computed from a '
    'named error path: (sin**2 + cos**2)/(sin - cos) was confirmed to reduce to 1/(sin - cos), the value '
    'of merging the terms without flipping the second denominator; sin - cos is what the illegal '
    'term-by-term cancellation of (sin**2 - cos**2)/(sin - cos) returns, the exact reciprocal of the '
    'first; tan + cot was verified equal to 1/(sin*cos), reached by mistaking the two clearing '
    'multipliers for a common denominator. At th = pi/6 the three give about -2.732, -0.366 and 2.309 '
    'against the true (1 + sqrt(3))/2 about 1.366, so none sits close enough to confuse. '
    'Collision sweep on 6407 items (bank 62 files + k1 out + k2 out), probe collide_b18d.py: the mold '
    '“sum of two fractions whose denominators differ only by the order of subtraction” returns no item in '
    'the corpus; the nearest neighbours are single compound fractions of the form trig over 1 plus or '
    'minus another trig, which never force the sign flip because there is nothing to combine them with, '
    'and a separate scan for the paired terms sin over 1 minus cot and cos over 1 minus tan appearing '
    'together also came back empty. Choices are ordered ascending in lexicographic order of their LaTeX '
    'strings, which for this set realises the symbolic rule constant-led form first (the reciprocal with '
    '1 on top), then the two sin-led binomials with plus before minus, then the tan-led one, so the '
    'answer slot is forced by that rule and was not chosen.',
)

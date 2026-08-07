# -*- coding: utf-8 -*-
add_fill(
    145,
    ['7.1'],
    'ง่าย',
    'รูปสามเหลี่ยม $ABC$ มีมุม $C$ เป็นมุมฉาก ถ้า $\\sin A + \\cos A = \\dfrac{7}{5}$ '
    'แล้วค่าของ $\\sin A \\cdot \\cos A$ เท่ากับเท่าใด',
    '12/25',
    ['12/25', '\\dfrac{12}{25}', '0.48'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เอกลักษณ์พีทาโกรัส : สำหรับทุกมุม $A$ จะได้ $\\sin^{2}A + \\cos^{2}A = 1$ เสมอ '
        '⇒ ที่มาของสูตรนี้อ่านได้จากสามเหลี่ยมมุมฉากตรง ๆ : ถ้าด้านตรงข้ามมุม $A$ ยาว $a$ '
        'ด้านประชิดมุม $A$ ยาว $b$ และด้านตรงข้ามมุมฉากยาว $c$ '
        'พีทาโกรัสบอกว่า $a^{2} + b^{2} = c^{2}$ · เมื่อหารทั้งสมการด้วย $c^{2}$ '
        'จะได้ $\\left(\\dfrac{a}{c}\\right)^{2} + \\left(\\dfrac{b}{c}\\right)^{2} = 1$ '
        'ซึ่งก็คือ $\\sin^{2}A + \\cos^{2}A = 1$ นั่นเอง ⇒ ไม่ใช่สูตรลอย ๆ ให้ท่องจำ '
        'แต่เป็นพีทาโกรัสที่ถูกหารด้วยด้านตรงข้ามมุมฉาก',
        '• การกระจายกำลังสองของผลบวก : $(x + y)^{2} = x^{2} + 2xy + y^{2}$ '
        '⇒ จุดที่ต้องมองให้ออกคือพจน์กลาง $2xy$ ซึ่งเป็น<b>ผลคูณ</b>ของสองตัวนั้น '
        'พูดอีกอย่างคือ การยกกำลังสองผลบวกจะ<b>ผลิตผลคูณออกมาให้เอง</b> '
        '⇒ นี่คือสะพานมาตรฐานที่พาเราเดินจากคำว่า “ผลบวก” ไปหาคำว่า “ผลคูณ” '
        'โดยไม่ต้องรู้ค่าของ $x$ และ $y$ ทีละตัวเลย',
        '• การแก้สมการเชิงเส้นสองจังหวะ : สมการหน้าตา $1 + 2u = k$ ต้องแก้สองจังหวะเสมอ '
        'คือ<b>ลบ</b>ค่าคงตัวออกก่อน แล้วจึง<b>หาร</b>ด้วยสัมประสิทธิ์ '
        '⇒ ถ้าทำจังหวะเดียวแล้วหยุด ค่าที่ได้จะไม่ใช่ $u$ '
        'แต่เป็น $2u$ ซึ่งใหญ่กว่าคำตอบจริงอยู่เท่าตัวพอดี',
        '• เพดานของผลคูณ $\\sin A\\cos A$ : กำลังสองของจำนวนจริงใด ๆ ห้ามติดลบ '
        '⇒ $(\\sin A - \\cos A)^{2} \\ge 0$ ⇒ กระจายได้ $1 - 2\\sin A\\cos A \\ge 0$ '
        '⇒ $\\sin A\\cos A \\le \\dfrac{1}{2}$ · ในทำนองเดียวกัน $(\\sin A + \\cos A)^{2} \\ge 0$ '
        'ให้ $\\sin A\\cos A \\ge -\\dfrac{1}{2}$ ⇒ ผลคูณนี้ต้องอยู่ในช่วง '
        '$\\left[-\\dfrac{1}{2},\\ \\dfrac{1}{2}\\right]$ เสมอไม่ว่ามุมจะเป็นเท่าใด '
        '⇒ เก็บเพดานนี้ไว้ใช้คัดค่าที่เป็นไปไม่ได้ทิ้งตั้งแต่ยังไม่ทันคิดละเอียด',
        '• มุมในสามเหลี่ยมมุมฉาก : มุมภายในทั้งสามรวมกันได้ $180^{\\circ}$ '
        'ถ้ามุมหนึ่งกางเต็ม $90^{\\circ}$ อีกสองมุมที่เหลือจึงรวมกันได้ $90^{\\circ}$ พอดี '
        '⇒ ทั้งคู่ต้องเป็นมุมแหลม ⇒ $\\sin$ และ $\\cos$ ของมุมแหลมเป็นบวกทั้งคู่ '
        '(เพราะเป็นอัตราส่วนของความยาวด้านซึ่งเป็นจำนวนบวก)',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• รูปสามเหลี่ยม $ABC$ มีมุม $C$ เป็นมุมฉาก ⇒ มุม $A$ กับมุม $B$ เป็นมุมแหลมทั้งคู่ '
        '⇒ $\\sin A > 0$ และ $\\cos A > 0$',
        '• ผลบวกของอัตราส่วนทั้งสองถูกกำหนดมาให้แล้ว คือ $\\sin A + \\cos A = \\dfrac{7}{5}$',
        '• สังเกตหน้าตาก่อนลงมือ : โจทย์ยื่น<b>ผลบวก</b>มาให้ แล้วถามหา<b>ผลคูณ</b> '
        '⇒ นี่คือคู่ที่มีสะพานเชื่อมกันอยู่แล้ว เพราะ '
        '$(\\sin A + \\cos A)^{2}$ กระจายออกมาแล้วมีพจน์ $2\\sin A\\cos A$ อยู่ตรงกลางพอดี '
        '⇒ เดาทางได้ตั้งแต่ยังไม่ลงมือว่าต้องยกกำลังสอง ⛔ ไม่ใช่ไล่หาขนาดของมุม $A$',
        '• สังเกตอีกอย่าง : โจทย์ไม่ได้บอกความยาวด้านสักด้าน และไม่ได้บอกขนาดมุมสักมุม '
        '⇒ สิ่งที่ถามต้องคำนวณได้จากข้อมูลชิ้นเดียวที่ให้มา ⛔ ไม่ต้องไปหาว่ามุม $A$ กางกี่องศา',
        '• ตรวจความเป็นไปได้ของข้อมูลก่อนเชื่อ : จากเพดานข้างต้น $(\\sin A + \\cos A)^{2} '
        '= 1 + 2\\sin A\\cos A \\le 1 + 1 = 2$ ⇒ ผลบวกนี้ยาวได้ไม่เกิน $\\sqrt{2} \\approx 1.4142$ '
        '· ค่าที่โจทย์ให้คือ $\\dfrac{7}{5} = 1.4$ ซึ่งเฉียดเพดานแต่ยังไม่เกิน '
        '⇒ ข้อมูลชุดนี้เป็นไปได้จริง มีมุมแหลมที่ทำให้เป็นจริงอยู่จริง',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\sin A \\cdot \\cos A$ ออกมาเป็นจำนวนเดียว',
        '',
        '<b>【 ยกกำลังสองสมการที่โจทย์ให้ทั้งสองข้าง เพื่อบังคับให้พจน์ผลคูณ '
        '$2\\sin A\\cos A$ โผล่ออกมากลางการกระจาย '
        'แล้วยุบ $\\sin^{2}A + \\cos^{2}A$ ให้เป็น $1$ ด้วยเอกลักษณ์พีทาโกรัส '
        'จะเหลือสมการเชิงเส้นของผลคูณ ซึ่งแก้ได้ด้วยการลบ $1$ แล้วหารด้วย $2$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · ยกกำลังสองทั้งสองข้างของสมการที่โจทย์ให้</b>',
        '• สูตรที่ใช้ : $(x + y)^{2} = x^{2} + 2xy + y^{2}$ '
        'เลือกใช้เพราะเป็นเครื่องมือเดียวที่เปลี่ยนผลบวกให้กลายเป็นสิ่งที่มีผลคูณอยู่ข้างใน',
        '• ระบุตัวแปรก่อนแทนค่า : ให้ $x = \\sin A$ และ $y = \\cos A$ '
        '· การยกกำลังสองทั้งสองข้างทำได้เพราะสองข้างของสมการเท่ากันอยู่แล้ว '
        'ของที่เท่ากันเมื่อยกกำลังสองก็ยังเท่ากัน',
        '• แทนค่า : $(\\sin A + \\cos A)^{2} = \\left(\\dfrac{7}{5}\\right)^{2}$',
        '• กระจายฝั่งซ้าย และยกกำลังสองทั้งเศษและส่วนของฝั่งขวา '
        '⛔ ตัวส่วนก็ต้องยกกำลังสองด้วย : '
        '$\\sin^{2}A + 2\\sin A\\cos A + \\cos^{2}A = \\dfrac{49}{25}$',
        '',
        '<b>ขั้นที่ 2 · ยุบสองพจน์หัวท้ายด้วยเอกลักษณ์พีทาโกรัส</b>',
        '• สูตรที่ใช้ : $\\sin^{2}A + \\cos^{2}A = 1$ '
        'ใช้ได้กับทุกมุมโดยไม่มีเงื่อนไข จึงใช้กับมุม $A$ ของข้อนี้ได้ทันที',
        '• จัดกลุ่มก่อนแทนค่า ⇒ ย้ายพจน์กลางไปไว้ท้ายสุดเพื่อให้เห็นก้อนที่จะยุบชัด ๆ : '
        '$\\left(\\sin^{2}A + \\cos^{2}A\\right) + 2\\sin A\\cos A = \\dfrac{49}{25}$',
        '• แทนค่าก้อนในวงเล็บด้วย $1$ : $1 + 2\\sin A\\cos A = \\dfrac{49}{25}$',
        '• 📌 ถึงตรงนี้สิ่งที่โจทย์ถามอยู่ในสมการเรียบร้อยแล้ว และเหลือเป็นสมการเชิงเส้นธรรมดา '
        'ที่มีสิ่งไม่รู้ค่าเพียงก้อนเดียวคือ $\\sin A\\cos A$ '
        '⇒ ⛔ ไม่ต้องแยกหา $\\sin A$ กับ $\\cos A$ ทีละตัวให้เสียเวลา',
        '',
        '<b>ขั้นที่ 3 · แก้สมการเชิงเส้นสองจังหวะ ⭐ จุดตายของข้อนี้อยู่ตรงนี้</b>',
        '• จังหวะแรก ลบ $1$ ออกทั้งสองข้าง : '
        '$2\\sin A\\cos A = \\dfrac{49}{25} - 1 = \\dfrac{49}{25} - \\dfrac{25}{25} = \\dfrac{24}{25}$',
        '• จังหวะที่สอง หารด้วย $2$ ทั้งสองข้าง ⛔ ห้ามหยุดที่จังหวะแรกเด็ดขาด '
        'เพราะสิ่งที่โจทย์ถามคือ $\\sin A\\cos A$ ไม่ใช่ $2\\sin A\\cos A$ : '
        '$\\sin A\\cos A = \\dfrac{24}{25} \\div 2 = \\dfrac{24}{50} = \\dfrac{12}{25}$',
        '• ตรวจกับเพดานทันทีก่อนไปต่อ : $\\dfrac{12}{25} = 0.48$ ซึ่งไม่เกิน '
        '$\\dfrac{1}{2} = 0.5$ ⇒ ผ่านเกณฑ์ที่ว่าผลคูณของ $\\sin$ กับ $\\cos$ '
        'ของมุมเดียวกันต้องไม่เกินครึ่ง · และเป็นจำนวนบวก ซึ่งตรงกับที่มุม $A$ เป็นมุมแหลม',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ย้อนกลับไปหาค่า $\\sin A$ และ $\\cos A$ '
        'ออกมาเป็นตัวเลขจริงจากสมการกำลังสอง แล้วคูณกันตรง ๆ '
        'โดยไม่ใช้การกระจายกำลังสองของผลบวกอีกเลย)</b>',
        '• แนวคิดของการตรวจ : ถ้าสองจำนวนมีผลบวกเป็น $\\dfrac{7}{5}$ '
        'และผลคูณเป็น $\\dfrac{12}{25}$ จริง สองจำนวนนั้นต้องเป็นรากของสมการกำลังสอง '
        '$t^{2} - (\\text{ผลบวก})t + (\\text{ผลคูณ}) = 0$ '
        '⇒ ถ้าแก้ออกมาแล้วได้คู่ที่เป็น $\\sin$ กับ $\\cos$ ของมุมแหลมได้จริง ก็ยืนยันคำตอบ',
        '• ตั้งสมการ : $t^{2} - \\dfrac{7}{5}t + \\dfrac{12}{25} = 0$ '
        '· คูณทั้งสมการด้วย $25$ เพื่อกำจัดเศษส่วน : $25t^{2} - 35t + 12 = 0$',
        '• แยกตัวประกอบ : $(5t - 3)(5t - 4) = 0$ ⇒ $t = \\dfrac{3}{5}$ หรือ $t = \\dfrac{4}{5}$',
        '• ด่านที่หนึ่ง คู่นี้เป็น $\\sin$ กับ $\\cos$ ของมุมเดียวกันได้ไหม : '
        '$\\left(\\dfrac{3}{5}\\right)^{2} + \\left(\\dfrac{4}{5}\\right)^{2} '
        '= \\dfrac{9}{25} + \\dfrac{16}{25} = \\dfrac{25}{25} = 1$ ✓ '
        '⇒ ผ่านเอกลักษณ์พีทาโกรัส และเป็นบวกทั้งคู่ตามที่มุมแหลมต้องเป็น',
        '• ด่านที่สอง ผลบวกตรงกับที่โจทย์ให้ไหม : '
        '$\\dfrac{3}{5} + \\dfrac{4}{5} = \\dfrac{7}{5}$ ✓ ตรงเป๊ะ',
        '• ด่านที่สาม คูณกันตรง ๆ : $\\dfrac{3}{5} \\times \\dfrac{4}{5} = \\dfrac{12}{25}$ ✓ '
        '⇒ ตรงกับที่คำนวณไว้ในขั้นที่ $3$ ทุกประการ',
        '• 📌 อ่านความหมายให้ออก : รูปสามเหลี่ยมของข้อนี้ก็คือสามเหลี่ยม $3$-$4$-$5$ ที่คุ้นเคยนั่นเอง '
        '(ด้านยาว $3$, $4$ และ $5$ หน่วย ซึ่ง $3^{2} + 4^{2} = 5^{2}$) '
        '· สลับกันว่า $\\sin A$ เป็น $\\dfrac{3}{5}$ หรือ $\\dfrac{4}{5}$ ก็ได้ '
        'เพราะสองกรณีนี้คือการมองรูปเดิมจากมุม $A$ หรือจากมุม $B$ '
        'และผลคูณออกมาเท่ากันทั้งสองกรณี ⇒ คำตอบไม่กำกวม',
        '',
        '✅ <b>คำตอบ</b> ค่าของ $\\sin A \\cdot \\cos A$ เท่ากับ $\\dfrac{12}{25}$ '
        'ซึ่งเขียนเป็นทศนิยมได้ $0.48$ และเป็นอัตราส่วนของความยาวด้านคูณกันจึงไม่มีหน่วย',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอโจทย์ที่ให้<b>ผลบวก</b>ของ $\\sin$ กับ $\\cos$ แล้วถาม<b>ผลคูณ</b> '
        '(หรือให้ผลคูณแล้วถามผลบวก) ให้ยกกำลังสองทันทีโดยไม่ต้องคิดนาน '
        'เพราะสองปริมาณนี้ผูกกันด้วยสมการเดียวคือ '
        '$(\\sin A + \\cos A)^{2} = 1 + 2\\sin A\\cos A$ ⇒ รู้ค่าหนึ่งก็ได้อีกค่าทันที '
        '⛔ ไม่ต้องหาขนาดของมุมเลยแม้แต่นิดเดียว',
        '• จำคู่แฝดของสูตรนี้ไว้ด้วย : $(\\sin A - \\cos A)^{2} = 1 - 2\\sin A\\cos A$ '
        '⇒ นำสองสูตรมาบวกกันจะได้ $2$ เสมอ '
        '· ประโยชน์ตรงหน้าคือ ข้อนี้หา $\\sin A - \\cos A$ ต่อได้ทันทีโดยไม่ต้องเริ่มใหม่ '
        'คือ $1 - \\dfrac{24}{25} = \\dfrac{1}{25}$ ⇒ ผลต่างเป็น $\\pm\\dfrac{1}{5}$',
        '• ก่อนตอบให้ตรวจเพดานเสมอ : ผลคูณ $\\sin A\\cos A$ ต้องอยู่ระหว่าง '
        '$-\\dfrac{1}{2}$ กับ $\\dfrac{1}{2}$ ⇒ ค่าไหนที่คำนวณได้แล้วหลุดกรอบนี้ '
        'ไม่ต้องตรวจซ้ำก็รู้ว่าคิดผิด ⇒ เป็นตัวกรองที่ใช้เวลาสองวินาทีแต่กันพลาดได้หลายเส้นทาง',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\dfrac{24}{25}$ เพราะหยุดที่จังหวะแรกของขั้นที่ $3$ '
        'คือลบ $1$ แล้วรีบตอบ ทั้งที่ค่านั้นคือ $2\\sin A\\cos A$ ยังไม่ได้หารด้วย $2$ · '
        'ค่านี้ผิดแน่นอนโดยไม่ต้องคำนวณอะไรเพิ่ม เพราะ $\\dfrac{24}{25} = 0.96$ '
        'ซึ่งทะลุเพดาน $\\dfrac{1}{2}$ ไปเกือบเท่าตัว · พิสูจน์อีกทางหนึ่ง : '
        'ถ้าผลคูณเป็น $\\dfrac{24}{25}$ จริง ผลบวกจะต้องเป็น '
        '$\\sqrt{1 + \\dfrac{48}{25}} = \\dfrac{\\sqrt{73}}{5} \\approx 1.709$ '
        'ซึ่งไม่ใช่ $\\dfrac{7}{5}$ ที่โจทย์ให้ · สังเกตว่าค่านี้เป็นสองเท่าของค่าจริงพอดี '
        'ซึ่งเป็นลายเซ็นของการลืมหารสอง',
        '• ได้ค่า $\\dfrac{49}{50}$ เพราะยกกำลังสองได้ $\\dfrac{49}{25}$ แล้วรีบหารด้วย $2$ ทันที '
        'โดย<b>ลืมลบ $1$ ก่อน</b> คือทำสองจังหวะสลับลำดับและตกไปหนึ่งจังหวะ · '
        'ค่านี้ผิดจริง เพราะ $\\dfrac{49}{50} = 0.98$ ก็ทะลุเพดาน $\\dfrac{1}{2}$ เช่นกัน · '
        'ต้นตอของความพลาดคือลืมว่าฝั่งซ้ายหลังกระจายมีสามพจน์ ไม่ใช่พจน์เดียว '
        'ก้อน $\\sin^{2}A + \\cos^{2}A$ ที่ยุบเป็น $1$ ต้องถูกย้ายข้างออกไปก่อนเสมอ',
        '• ได้ค่า $\\dfrac{7}{10}$ เพราะคิดเอาเองว่าผลคูณเท่ากับครึ่งหนึ่งของผลบวก '
        'จึงหยิบ $\\dfrac{7}{5}$ มาหารด้วย $2$ ตรง ๆ โดยไม่ยกกำลังสองเลย · '
        'ค่านี้ตัดทิ้งได้ทันทีเพราะ $\\dfrac{7}{10} = 0.7$ ซึ่งเกินเพดาน $\\dfrac{1}{2}$ · '
        'พิสูจน์ตรง ๆ อีกทาง : ถ้าผลคูณเป็น $\\dfrac{7}{10}$ ผลบวกจะต้องเป็น '
        '$\\sqrt{1 + \\dfrac{7}{5}} = \\sqrt{\\dfrac{12}{5}} \\approx 1.549$ '
        'ซึ่งมากกว่า $\\sqrt{2}$ เสียอีก จึงเป็นไปไม่ได้เลยสำหรับมุมจริง ๆ · '
        'ที่หลงคิดแบบนี้เพราะเห็นเลข $2$ ในพจน์ $2\\sin A\\cos A$ แล้วเผลอเอาไปหารผลบวก '
        'ทั้งที่เลข $2$ ตัวนั้นเกิดขึ้น<b>หลัง</b>การยกกำลังสอง ไม่ใช่ก่อน',
        '• ได้ค่า $\\dfrac{22}{5}$ เพราะยกกำลังสองแล้วยกเฉพาะตัวเศษ '
        'เขียน $\\left(\\dfrac{7}{5}\\right)^{2}$ เป็น $\\dfrac{49}{5}$ '
        '⇒ ลบ $1$ ได้ $\\dfrac{44}{5}$ แล้วหารด้วย $2$ ได้ $\\dfrac{22}{5} = 4.4$ · '
        'ค่านี้ผิดชัดเจนเพราะนอกจากจะทะลุเพดาน $\\dfrac{1}{2}$ แล้ว '
        'ยังมากกว่า $1$ ทั้งที่ $\\sin A$ และ $\\cos A$ ต่างก็มีค่าไม่เกิน $1$ '
        'ผลคูณของสองจำนวนที่ไม่เกิน $1$ จึงเกิน $1$ ไม่ได้เลย · '
        'กฎที่ต้องจำคือ $\\left(\\dfrac{p}{q}\\right)^{2} = \\dfrac{p^{2}}{q^{2}}$ '
        'ตัวส่วนต้องยกกำลังสองด้วยเสมอ',
    ],
    'V.mold: G = a right triangle ABC whose right angle sits at C, handed over with exactly one numeric '
    'datum, namely that the sum sin A + cos A equals 7/5, with no side length and no angle size given '
    'anywhere in the statement / A = the value of the product sin A * cos A, asked as a free numeric '
    'response with no candidate values printed on the page / M = square the given sum so that the cross '
    'term 2*sin A*cos A is manufactured in the middle of the expansion, collapse sin^2 A + cos^2 A to 1 '
    'through the Pythagorean identity, and read the product off the resulting linear equation by '
    'subtracting 1 and then dividing by 2. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 -> level: ง่าย. '
    'F = 1 because one trigonometric formula is in play, the Pythagorean identity; the binomial expansion '
    '(x+y)^2 = x^2 + 2xy + y^2 is ordinary algebra rather than a second trigonometric key, and nothing '
    'else can substitute for the identity here. C = 0 because the whole item stays inside subtopic 7.1 '
    'and never reaches out to a second subtopic, so there is no second key to join to the first. P = 1 '
    'because the work occupies a single arena: one squaring, one collapse, and the two-beat linear finish '
    'that follows is the tail of that same move rather than a fresh stage, which follows the q105 and '
    'q113 baseline where a closing reduction does not buy a second point. T = 0 because nothing has to be '
    'discovered before the work can start: the right angle at C is stated outright, no branch has to be '
    'rejected since both roots of the verification quadratic give the same product, and no sign decision '
    'is forced because an acute angle makes both ratios positive. L = 0 because the statement is symbolic '
    'in the sense of the L baseline: the given equation can be squared on sight and no figure has to be '
    'drawn before the work can begin. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): solving the system s + c = 7/5 together with s^2 + c^2 = 1 over the positive '
    'reals returns exactly two branches, (s, c) = (3/5, 4/5) and (4/5, 3/5), and the set of products '
    'taken over those branches has size 1, which is checked explicitly so that the item is proved '
    'unambiguous rather than assumed to be; that single product simplifies to 12/25 exactly, and the '
    'stored key string 12/25 was parsed as a rational and compared against that value rather than '
    'eyeballed. Every wrong road printed in the pitfalls block was computed by machine and not invented: '
    'stopping one beat early gives (7/5)^2 - 1 = 24/25, halving before subtracting gives (7/5)^2/2 = '
    '49/50, halving the sum itself gives (7/5)/2 = 7/10, and squaring only the numerator gives '
    '(49/5 - 1)/2 = 22/5. The ceiling used to knock all four down was derived and checked separately, '
    'since (s - c)^2 >= 0 forces s*c <= 1/2, and machine evaluation confirms 24/25 = 0.96, 49/50 = 0.98, '
    '7/10 = 0.7 and 22/5 = 4.4 all sit above 0.5 while the true 12/25 = 0.48 sits below it. The datum '
    'itself was checked for feasibility as well: sin A + cos A can never exceed sqrt(2) = 1.41421..., and '
    '7/5 = 1.4 clears that bar, so a real acute angle satisfying the hypothesis exists. '
    'Collision sweep on 6457 items (bank 63 files + k1 out + k2 out), probes run as regular expressions '
    'over the question text of the whole corpus: the pattern for a stated sum of sine and cosine returns '
    '28 items, of which only 3 also name the angle A, and the pair (right angle at C) crossed with (a '
    'sine or cosine relation given rather than side lengths) returns 5 items, none of which asks for the '
    'product. The nearest neighbour by mechanism is gen-chap-07-trigonometry-q014, which runs this road '
    'in reverse: it hands over the product sin t * cos t = 1/4 and asks for the square of the sum, so its '
    'M is the already-registered M-PYTHID-EXPAND and its unknown is the quantity this item is given. The '
    'nearest neighbour by surface is chap-07-trigonometry-q140, which also states a sum of sine and '
    'cosine but asks for the sum of cubes and therefore turns on the cube factorisation rather than on '
    'the product itself; incidentally sympy reports that its datum 3/2 exceeds sqrt(2), so that older '
    'item has no real solution at all, which is worth a separate look by the bank owners and is recorded '
    'here rather than acted on. Two further relatives, gen-chap-07-trigonometry-q011 and '
    'gen-chap-07-trigonometry-q065, both start from side or tangent data and produce the sum as their '
    'answer, so their A is what this item supplies as its G. No item in the corpus goes from a stated '
    'sum straight to the product inside a right triangle. Since this is a fill item there is no choice '
    'list, so no answer slot exists and nothing about the answer could have been positioned by hand.',
)

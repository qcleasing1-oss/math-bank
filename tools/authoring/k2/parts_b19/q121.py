# -*- coding: utf-8 -*-
add(
    121,
    ['7.3'],
    'ง่าย',
    'คาบของฟังก์ชัน $g(x) = 5\\cos\\left(\\dfrac{2x}{3}\\right) - 1$ '
    'เมื่อวัดเป็นองศา เท่ากับข้อใด',
    [
        '$180^{\\circ}$',
        '$240^{\\circ}$',
        '$270^{\\circ}$',
        '$540^{\\circ}$',
    ],
    3,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ฟังก์ชันที่มีลวดลายซ้ำเดิมไปเรื่อย ๆ เรียกว่าฟังก์ชันที่เป็นคาบ '
        'และ<b>คาบ</b>คือความยาวช่วงบนแกน $X$ ที่สั้นที่สุดซึ่งเดินไปแล้วลวดลายกลับมาเหมือนเดิมทุกจุด '
        'เขียนเป็นเงื่อนไขได้ว่า ถ้า $T$ เป็นคาบ แล้วต้องมี $g(x + T) = g(x)$ จริงสำหรับ $x$ ทุกตัว '
        'ไม่ใช่จริงแค่บางตัว',
        '• คาบพื้นฐานของ $\\cos$ คือ $360^{\\circ}$ เหตุผลอยู่ที่วงกลมหนึ่งหน่วย : '
        '$\\cos\\theta$ คือพิกัดตามแนวนอนของจุดที่เดินไปบนวงกลมเป็นมุม $\\theta$ '
        'จุดนั้นจะกลับมาที่ตำแหน่งเดิมก็ต่อเมื่อเดินครบหนึ่งรอบพอดี ซึ่งคือ $360^{\\circ}$ '
        'เดินแค่ครึ่งรอบ $180^{\\circ}$ จุดจะไปอยู่ฝั่งตรงข้าม พิกัดแนวนอนกลับเครื่องหมาย ยังไม่ซ้ำเดิม',
        '• <b>ที่มาของสูตรคาบ</b> สำหรับ $\\cos(bx)$ : สิ่งที่ต้องกวาดครบหนึ่งรอบไม่ใช่ตัว $x$ '
        'แต่เป็น<b>อาร์กิวเมนต์</b> คือก้อนที่อยู่ในวงเล็บของ $\\cos$ ตอน $x$ เดินจาก $x$ ไปถึง $x + T$ '
        'อาร์กิวเมนต์เดินจาก $bx$ ไปถึง $b(x + T)$ นั่นคือเดินไปได้ $bT$ '
        'จะซ้ำเดิมก็ต่อเมื่ออาร์กิวเมนต์กวาดครบ $360^{\\circ}$ หนึ่งรอบ จึงต้องมี $bT = 360^{\\circ}$ '
        'ย้ายข้างได้ $T = \\dfrac{360^{\\circ}}{b}$ ⇒ ถ้าสัมประสิทธิ์เป็น $b$ ก็ต้องให้ $x$ เดินไป '
        '$\\dfrac{360^{\\circ}}{b}$ นี่คือที่มาของสูตร ไม่ใช่กฎที่ต้องท่องเปล่า ๆ',
        '• ที่เขียนสูตรเต็มเป็น $\\dfrac{360^{\\circ}}{|b|}$ เพราะคาบเป็น<b>ความยาวช่วง</b> '
        'จึงต้องเป็นจำนวนบวกเสมอ · ถ้า $b$ ติดลบ อาร์กิวเมนต์ก็แค่กวาดย้อนทาง '
        'แต่ $\\cos(-u) = \\cos u$ ค่าที่ได้เรียงเหมือนเดิมทุกประการ ระยะที่ใช้ซ้ำรอยจึงเท่ากัน '
        'ค่าสัมบูรณ์จึงทำหน้าที่แค่ตัดเครื่องหมายลบทิ้ง',
        '• ⛔ เลขที่คูณอยู่ข้างหน้าและเลขที่บวกลบอยู่ข้างหลัง <b>ไม่มีผลต่อคาบเลย</b> : '
        'ในรูป $a\\cos(bx) + d$ ตัว $a$ ทำหน้าที่ยืดหรือหดกราฟ<b>ตามแนวตั้ง</b> '
        'ส่วน $d$ ทำหน้าที่เลื่อนกราฟขึ้นลง<b>ตามแนวตั้ง</b> ทั้งคู่ไม่ได้ไปแตะ $x$ สักนิด '
        'จังหวะที่ลวดลายกลับมาซ้ำเดิมจึงไม่ขยับ · มีแต่ $b$ ตัวเดียวเท่านั้นที่กำหนดคาบ',
        '• การหารด้วยเศษส่วน ให้<b>กลับตัวหาร</b>แล้วเปลี่ยนหารเป็นคูณ นั่นคือ '
        '$A \\div \\dfrac{p}{q} = A \\times \\dfrac{q}{p}$ · '
        '⛔ และต้องระวังหน่วย ถ้าโจทย์วัดมุมเป็นเรเดียนสูตรจะเป็น $\\dfrac{2\\pi}{|b|}$ '
        'ข้อนี้โจทย์สั่งให้วัดเป็นองศา จึงต้องใช้ $360^{\\circ}$ เป็นตัวตั้ง ห้ามสลับหน่วยกัน',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• ฟังก์ชัน $g(x) = 5\\cos\\left(\\dfrac{2x}{3}\\right) - 1$',
        '• โจทย์สั่งให้วัดคาบเป็นองศา จึงต้องใช้หนึ่งรอบเท่ากับ $360^{\\circ}$ ไม่ใช่ $2\\pi$',
        '• สังเกตหน้าตาก่อนลงมือ : ก้อนในวงเล็บของ $\\cos$ เขียนว่า $\\dfrac{2x}{3}$ '
        'ซึ่งอ่านได้เป็น $\\dfrac{2}{3} \\times x$ แปลว่าสัมประสิทธิ์ที่คูณอยู่กับ $x$ คือ $\\dfrac{2}{3}$ '
        'ทั้งก้อน ⛔ ไม่ใช่ $2$ และ ⛔ ไม่ใช่ $3$ ตัวใดตัวหนึ่ง',
        '• สังเกตต่ออีกชั้น : $\\dfrac{2}{3}$ เป็นจำนวนที่<b>น้อยกว่า</b> $1$ '
        'อาร์กิวเมนต์จึงเดินช้ากว่า $x$ กว่าจะกวาดครบหนึ่งรอบ $x$ ต้องเดินไกลกว่า $360^{\\circ}$ '
        'คำตอบจึงต้องเป็นค่าที่มากกว่า $360^{\\circ}$ แน่นอน รู้ล่วงหน้าไว้ก่อนคิดจริง',
        '• เลข $5$ ที่คูณอยู่หน้า $\\cos$ คือแอมพลิจูด และเลข $-1$ ที่ต่อท้ายคือเส้นกลาง '
        'ทั้งสองตัวนี้เป็นเรื่องของแนวตั้งล้วน ๆ ⛔ ไม่มีผลต่อคาบเลยแม้แต่น้อย จึงยกทิ้งไปได้ตั้งแต่ต้น',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาคาบของฟังก์ชัน $g$ โดยตอบเป็นองศา',
        '',
        '<b>【 อ่านสัมประสิทธิ์ที่คูณอยู่กับ $x$ ออกมาให้ได้ก่อน '
        'แล้วบังคับให้อาร์กิวเมนต์กวาดครบหนึ่งรอบ $360^{\\circ}$ '
        'จะได้สมการที่แก้หาคาบด้วยการหารเศษส่วนเพียงครั้งเดียว 】</b>',
        '',
        '<b>ขั้นที่ 1 · จัดฟังก์ชันให้เข้ารูปมาตรฐาน แล้วชี้ตัวที่เกี่ยวกับคาบ</b>',
        '• รูปมาตรฐานที่ใช้เทียบ : $y = a\\cos(bx) + d$',
        '• ระบุตัวแปรทีละตัวจาก $g(x) = 5\\cos\\left(\\dfrac{2x}{3}\\right) - 1$ · '
        '$a = 5$ คือแอมพลิจูด · $d = -1$ คือค่าที่บวกต่อท้าย ซึ่งเป็นระดับของเส้นกลาง',
        '• ส่วนที่อยู่ในวงเล็บคือ $\\dfrac{2x}{3}$ ให้แยก $x$ ออกมาให้เห็นชัดก่อน : '
        '$\\dfrac{2x}{3} = \\dfrac{2 \\times x}{3} = \\dfrac{2}{3} \\times x$ '
        'เทียบกับ $bx$ ได้ทันทีว่า $b = \\dfrac{2}{3}$',
        '• ⛔ จุดที่ต้องระวังตั้งแต่บรรทัดนี้ : ตัวส่วน $3$ เป็นส่วนหนึ่งของสัมประสิทธิ์ '
        'ห้ามหยิบแต่ $2$ ขึ้นมาแล้วทิ้ง $3$ ไว้ข้างหลัง เพราะ $\\dfrac{2}{3}$ ต้องไปทั้งก้อน',
        '• ตัดสิ่งที่ไม่เกี่ยวออกจากสายตา : $a = 5$ ยืดกราฟตามแนวตั้ง $d = -1$ เลื่อนกราฟลง '
        'ทั้งสองไม่แตะ $x$ จึงไม่เปลี่ยนจังหวะการซ้ำ · เหลือของที่ต้องใช้คิดคาบเพียงตัวเดียวคือ '
        '$b = \\dfrac{2}{3}$',
        '',
        '<b>ขั้นที่ 2 · เขียนเงื่อนไขการซ้ำรอย แล้วสร้างสมการจากการกวาดครบหนึ่งรอบ</b>',
        '• เงื่อนไขที่ใช้ : $T$ เป็นคาบ ก็ต่อเมื่ออาร์กิวเมนต์ของ $\\cos$ กวาดไปได้ครบ '
        '$360^{\\circ}$ พอดีหนึ่งรอบ เมื่อ $x$ เดินไปเป็นระยะ $T$',
        '• ระบุตัวแปร : อาร์กิวเมนต์ตอนนี้คือ $\\dfrac{2}{3}x$ · '
        'พอ $x$ กลายเป็น $x + T$ อาร์กิวเมนต์กลายเป็น $\\dfrac{2}{3}(x + T)$',
        '• หาระยะที่อาร์กิวเมนต์เดินไปได้ ด้วยการเอาค่าใหม่ลบค่าเดิม : '
        '$\\dfrac{2}{3}(x + T) - \\dfrac{2}{3}x = \\dfrac{2}{3}x + \\dfrac{2}{3}T - \\dfrac{2}{3}x '
        '= \\dfrac{2}{3}T$ · สังเกตว่า $x$ ตัดกันหายไปหมด แปลว่าระยะนี้ไม่ขึ้นกับว่าเริ่มที่จุดไหน',
        '• ตั้งให้ระยะที่ได้เท่ากับหนึ่งรอบ : $\\dfrac{2}{3}T = 360^{\\circ}$',
        '• ย้ายข้างโดยหารทั้งสองข้างด้วย $\\dfrac{2}{3}$ ซึ่งทำได้เพราะไม่เป็นศูนย์ ได้รูปที่จะแทนค่า '
        '$T = \\dfrac{360^{\\circ}}{\\dfrac{2}{3}} = 360^{\\circ} \\div \\dfrac{2}{3}$ '
        'ซึ่งก็คือหน้าตาเดียวกับสูตร $\\dfrac{360^{\\circ}}{|b|}$ ที่เพิ่งสร้างขึ้นมาเองกับมือ',
        '',
        '<b>ขั้นที่ 3 · คิดเลขหารเศษส่วนโดยกลับตัวหารแล้วคูณ</b>',
        '• สูตรที่ใช้ : $A \\div \\dfrac{p}{q} = A \\times \\dfrac{q}{p}$',
        '• เทียบตัวแปร : $A = 360^{\\circ}$ · $\\dfrac{p}{q} = \\dfrac{2}{3}$ '
        'ตัวที่ต้องกลับหัวคือตัวหาร กลับแล้วได้ $\\dfrac{3}{2}$ ⛔ ตัวตั้งไม่ต้องแตะ',
        '• แทนลงสูตร : $T = 360^{\\circ} \\times \\dfrac{3}{2} = \\dfrac{360^{\\circ} \\times 3}{2} '
        '= \\dfrac{1080^{\\circ}}{2}$',
        '• ยุบเศษส่วนสุดท้าย : $\\dfrac{1080^{\\circ}}{2} = 540^{\\circ}$ จึงได้ $T = 540^{\\circ}$',
        '• ตรงกับที่ประเมินไว้ตั้งแต่ต้น เพราะ $540^{\\circ}$ มากกว่า $360^{\\circ}$ จริง '
        'สมกับที่สัมประสิทธิ์ $\\dfrac{2}{3}$ น้อยกว่า $1$',
        '',
        '<b>ขั้นที่ 4 · ยืนยันว่าไม่มีค่าบวกที่สั้นกว่านี้ใช้ได้</b>',
        '• คาบต้องเป็นจำนวนบวกที่สั้นที่สุดซึ่งทำให้ลวดลายซ้ำเดิม จึงต้องเช็คว่าไม่มีตัวสั้นกว่า',
        '• สมมติว่ามีค่าบวก $T_0$ ที่สั้นกว่า $540^{\\circ}$ แล้วใช้เป็นคาบได้ '
        'อาร์กิวเมนต์จะกวาดไปได้ $\\dfrac{2}{3}T_0$ ซึ่งน้อยกว่า $\\dfrac{2}{3}(540^{\\circ}) '
        '= 360^{\\circ}$',
        '• แต่ $\\cos$ จะคืนค่าเดิมครบทุกจุดก็ต่อเมื่อกวาดครบรอบเต็มเท่านั้น '
        'กวาดไม่ถึงรอบจึงยังกลับมาไม่ครบ ⇒ $T_0$ เป็นคาบไม่ได้',
        '• สรุปว่า $540^{\\circ}$ เป็นค่าที่สั้นที่สุดจริง ⇒ เป็นคาบของ $g$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไม่ใช้สูตรคาบเลย '
        'แต่แทนตัวเลขจริงลงในฟังก์ชันที่จุด $x = 0$ แล้วเทียบค่ากันตรง ๆ)</b>',
        '• คิดค่าตั้งต้นก่อน : $g(0) = 5\\cos(0^{\\circ}) - 1 = 5(1) - 1 = 4$',
        '• ถ้า $540^{\\circ}$ เป็นคาบจริง ค่าที่ $x = 540^{\\circ}$ ต้องกลับมาเป็น $4$ เท่าเดิม · '
        'อาร์กิวเมนต์คือ $\\dfrac{2}{3}(540^{\\circ}) = 360^{\\circ}$ ⇒ '
        '$g(540^{\\circ}) = 5\\cos(360^{\\circ}) - 1 = 5(1) - 1 = 4$ ✓ ตรงกันพอดี',
        '• ลองค่า $180^{\\circ}$ ดูบ้าง : อาร์กิวเมนต์คือ $\\dfrac{2}{3}(180^{\\circ}) = 120^{\\circ}$ '
        '⇒ $g(180^{\\circ}) = 5\\cos(120^{\\circ}) - 1 = 5\\left(-\\dfrac{1}{2}\\right) - 1 '
        '= -\\dfrac{7}{2}$ ซึ่งไม่เท่ากับ $4$ ⇒ ใช้เป็นคาบไม่ได้',
        '• ลองค่า $240^{\\circ}$ : อาร์กิวเมนต์คือ $\\dfrac{2}{3}(240^{\\circ}) = 160^{\\circ}$ '
        '⇒ $g(240^{\\circ}) = 5\\cos(160^{\\circ}) - 1$ ซึ่งมีค่าประมาณ $5(-0.94) - 1 \\approx -5.70$ '
        'ไม่เท่ากับ $4$ ⇒ ใช้เป็นคาบไม่ได้',
        '• ลองค่า $270^{\\circ}$ ซึ่งเป็นครึ่งหนึ่งของคำตอบพอดี : '
        'อาร์กิวเมนต์เพิ่มขึ้นแค่ $\\dfrac{2}{3}(270^{\\circ}) = 180^{\\circ}$ คือครึ่งรอบ '
        'ทำให้ $\\cos$ กลับเครื่องหมาย ⇒ $g(270^{\\circ}) = 5\\cos(180^{\\circ}) - 1 = 5(-1) - 1 = -6$ '
        'ไม่เท่ากับ $4$ ⇒ ใช้เป็นคาบไม่ได้',
        '• เดินคนละเส้นทางกับสูตร แต่คัดออกได้เหลือค่าเดียวคือ $540^{\\circ}$ ✓',
        '',
        '✅ <b>คำตอบ</b> คาบของฟังก์ชัน $g$ เมื่อวัดเป็นองศา เท่ากับ $540^{\\circ}$ '
        '→ <b>ตัวเลือก 4</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• ให้จำ $b$ ว่าเป็นตัวบีบหรือยืดกราฟ<b>ตามแนวนอน</b> : ถ้า $|b| > 1$ อาร์กิวเมนต์วิ่งเร็วกว่า $x$ '
        'กราฟถูกบีบ คาบจึงสั้นกว่า $360^{\\circ}$ · ถ้า $0 < |b| < 1$ อาร์กิวเมนต์วิ่งช้ากว่า '
        'กราฟถูกยืด คาบจึงยาวกว่า $360^{\\circ}$ · ข้อนี้ $|b| = \\dfrac{2}{3}$ น้อยกว่า $1$ '
        'จึงคัดค่าที่สั้นกว่า $360^{\\circ}$ ทิ้งได้ทั้งหมดตั้งแต่ยังไม่ได้คิดเลข',
        '• ก่อนหาคาบ ให้กวาดสายตาลบเลขที่อยู่<b>นอกวงเล็บ</b>ทิ้งก่อนเสมอ ทั้งตัวคูณข้างหน้าและตัวบวกข้างหลัง '
        'เหลือไว้เฉพาะสิ่งที่ติดอยู่กับ $x$ ในวงเล็บ · ทำแบบนี้แล้วโจทย์จะเหลือของให้คิดแค่ตัวเดียว',
        '• วิธีตรวจที่เร็วที่สุดคือย้อนกลับ : เอาคาบที่ได้คูณกับ $b$ แล้วต้องได้หนึ่งรอบพอดี · '
        'ข้อนี้ $\\dfrac{2}{3} \\times 540^{\\circ} = 360^{\\circ}$ ครบรอบพอดี ✓ '
        'ถ้าคูณแล้วไม่ได้ $360^{\\circ}$ แปลว่าหารสลับข้างแน่นอน',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $180^{\\circ}$ เพราะอ่านสัมประสิทธิ์ผิด หยิบแต่ตัวเศษ $2$ ขึ้นมาแล้วทิ้งตัวส่วน $3$ '
        'จึงคิดเป็น $\\dfrac{360^{\\circ}}{2} = 180^{\\circ}$ · '
        'ค่านี้ผิดแน่นอน ตรวจได้ด้วยการแทนกลับ : อาร์กิวเมนต์จะเดินไปแค่ '
        '$\\dfrac{2}{3}(180^{\\circ}) = 120^{\\circ}$ ซึ่งเป็นแค่หนึ่งในสามของรอบ ยังไม่ครบรอบเลย '
        'และคิดค่าจริงได้ $g(180^{\\circ}) = 5\\cos(120^{\\circ}) - 1 = -\\dfrac{7}{2}$ '
        'ต่างจาก $g(0) = 4$ ชัดเจน · วิธีกันคือเขียน $\\dfrac{2x}{3}$ ใหม่เป็น $\\dfrac{2}{3} \\times x$ '
        'ให้เห็นก้อนสัมประสิทธิ์เต็มก้อนก่อนเสมอ',
        '• ได้ค่า $240^{\\circ}$ เพราะคูณแทนที่จะหาร คือคิดเป็น $360^{\\circ} \\times \\dfrac{2}{3} '
        '= 240^{\\circ}$ · ค่านี้ผิดเพราะสวนทางกับสามัญสำนึกตั้งแต่แรก : สัมประสิทธิ์ $\\dfrac{2}{3}$ '
        'น้อยกว่า $1$ ทำให้กราฟถูก<b>ยืด</b> คาบต้อง<b>ยาวกว่า</b> $360^{\\circ}$ แต่ค่านี้กลับสั้นลง · '
        'แทนกลับก็ไม่ผ่าน เพราะอาร์กิวเมนต์เดินไปได้ $\\dfrac{2}{3}(240^{\\circ}) = 160^{\\circ}$ '
        'ไม่ครบรอบ และ $g(240^{\\circ}) = 5\\cos(160^{\\circ}) - 1 \\approx -5.70$ ไม่ใช่ $4$ · '
        'วิธีกันคือกลับไปดูที่มาของสูตร ซึ่งมาจาก $bT = 360^{\\circ}$ ⇒ $T$ ต้องถูก $b$ <b>หาร</b>',
        '• ได้ค่า $270^{\\circ}$ เพราะใช้คาบพื้นฐานผิดตัว คือเอา $180^{\\circ}$ มาเป็นตัวตั้ง '
        'แล้วคิดเป็น $\\dfrac{180^{\\circ}}{\\dfrac{2}{3}} = 270^{\\circ}$ · '
        'ต้นตอคือ $180^{\\circ}$ เป็นคาบพื้นฐานของ $\\tan$ ไม่ใช่ของ $\\cos$ '
        'เพราะ $\\tan$ ซ้ำเดิมทุกครึ่งรอบ แต่ $\\cos$ ต้องครบรอบเต็มจึงจะซ้ำ · '
        'ตรวจได้ทันทีว่าผิด เพราะอาร์กิวเมนต์เพิ่มขึ้นแค่ $\\dfrac{2}{3}(270^{\\circ}) = 180^{\\circ}$ '
        'ซึ่งทำให้ $\\cos$ กลับเครื่องหมาย ได้ $g(270^{\\circ}) = 5\\cos(180^{\\circ}) - 1 = -6$ '
        'ซึ่งเป็นค่าต่ำสุดของ $g$ ตรงข้ามกับค่าสูงสุด $4$ ที่ $x = 0$ พอดี',
        '• อีกทางที่พลาดกันบ่อยคือหลงไปหยิบเลข $5$ หรือ $-1$ มาคิด เช่นตอบ $\\dfrac{360^{\\circ}}{5} '
        '= 72^{\\circ}$ · ค่านี้ผิดเพราะ $5$ เป็นแอมพลิจูดซึ่งยืดกราฟตามแนวตั้ง และ $-1$ เป็นเส้นกลาง '
        'ซึ่งเลื่อนกราฟตามแนวตั้ง ทั้งคู่ไม่ได้ไปแตะ $x$ เลย จึง<b>ไม่มีผลต่อคาบ</b>แม้แต่น้อย · '
        'ให้จำว่ามีแต่ตัวที่คูณอยู่กับ $x$ ในวงเล็บเท่านั้นที่เปลี่ยนคาบได้',
        '• อีกทางหนึ่งคือลืมอ่านหน่วยที่โจทย์สั่ง แล้วไปใช้สูตรฝั่งเรเดียน ได้ '
        '$\\dfrac{2\\pi}{\\dfrac{2}{3}} = 3\\pi$ ซึ่งไม่ตรงกับค่าใดเลย · '
        'ค่า $3\\pi$ เรเดียนก็คือ $540^{\\circ}$ นั่นเอง แปลว่าคิดถูกแต่รายงานผิดหน่วย '
        'โจทย์สั่งไว้ชัดว่าให้วัดเป็นองศา จึงต้องแปลงกลับก่อนตอบทุกครั้ง',
    ],
    'V.mold: G = one cosine function handed over in closed form, with a fractional coefficient sitting on '
    'x inside the bracket and with a vertical stretch in front and a vertical shift behind / A = the '
    'period of that function, reported in degrees / M = read off the coefficient b that multiplies x, '
    'force the argument to sweep exactly one full turn of 360 degrees while x advances by the period, and '
    'divide, which is a single division of a whole number by a fraction. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 with total at most 2, T = 0 and C = 0 -> level: ง่าย. '
    'F = 1 because one knowledge block, the period of a cosine read from the coefficient on x, carries '
    'the item end to end; noticing that the stretch 5 and the shift -1 leave the period untouched is part '
    'of that same block rather than a second one, since both are read off the one standard shape '
    'a*cos(b*x) + d, and the reciprocal rule for dividing by a fraction is arithmetic the student already '
    'owns. C = 0 because subtopic 7.3 answers the item alone, with nothing borrowed from another '
    'subtopic. P = 1 and deliberately not 2: pulling the coefficient 2/3 out of 2*x/3 and then dividing '
    '360 by it belong to one closing computation, not to two stages where the first produces an object '
    'the second must reinterpret. The benchmarks are q095, where dividing a fraction by a fraction was '
    'recorded as one stage rather than two, and q091, where two moves sitting side by side were held at '
    'one stage as well. T = 0 because there is no turning point: the coefficient stands directly in front '
    'of x with nothing disguising it, there is no sum of two waves whose periods would have to be '
    'combined and no half angle to unpick, and the vertical numbers announce themselves as vertical. '
    'L = 0 because the statement is a bare symbolic formula with no worded scene to model; the benchmarks '
    'are q030, q060 and q095, all held at L = 0 for the same pure symbol talk. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b19.py): 360/Rational(2,3) returns 540 exactly, and the ordering check confirmed the '
    'ascending sequence 180 < 240 < 270 < 540. Every error path in the pitfalls block was computed by '
    'machine rather than invented: Rational(360,2) = 180 for keeping only the numerator of the '
    'coefficient and dropping its denominator, 360*Rational(2,3) = 240 for multiplying where the '
    'derivation calls for dividing, and 180/Rational(2,3) = 270 for taking 180 as the base period, which '
    'belongs to the tangent and not to the cosine. Each was then refuted numerically by evaluating the '
    'function itself rather than by re-quoting the formula: g(0) = 4, while g at 180 degrees is '
    '5*cos(2*pi/3) - 1 = -7/2, g at 240 degrees is 5*cos(8*pi/9) - 1, about -5.70, and g at 270 degrees '
    'is 5*cos(pi) - 1 = -6, none of which equals 4, whereas g at 540 degrees is 5*cos(2*pi) - 1 = 4 and '
    'matches g(0). The radian slip was checked too: 2*pi/Rational(2,3) = 3*pi, which is the same angle as '
    '540 degrees and therefore a unit error rather than an arithmetic one. '
    'Collision sweep on 6417 items (bank 63 files + k1 out + k2 out), probe collide_b19.py / '
    'collide_b19b.py: scan C2 (question text asking for the period of a function) returned 3 items and '
    'scan C2b (the word for period standing together with the word for degree inside one statement) '
    'returned 1, which is a false positive, since those two letters were matched inside an unrelated '
    'compound word in a solar panel item filed under subtopics 7.10 and 7.9. Of the three C2 hits, '
    'gen-chap-07-trigonometry-q009 hands over a maximum and a minimum and asks for a function value, '
    'gen-chap-05-function-q404 lives in chapter 5 and reads a periodic function off a graph, and '
    'pat1-2564-03-q16 is a multi-statement item weighing several claims at once, so none of them asks for '
    'a period on its own. The nearest neighbour inside our own generated set is '
    'gen-chap-07-trigonometry-q025, which asks for the period of a sum, sin(4x) + cos(6x), and is settled '
    'by taking the least common multiple of two separate periods, mechanism M-LCM-PERIOD, a different '
    'tool altogether from reading a single coefficient. The mold registry was run under both candidate '
    'labels: with A = A-PERIOD it raises one WATCH-B pair against q025 and no failure, and with '
    'A = A-PERIOD-DEGREE it raises nothing, so iron rule 5 is clear either way and the sharper label was '
    'kept. Choices are ordered ascending by degree measure (180, then 240, then 270, then 540), so the '
    'answer slot is forced by that rule and was not chosen.',
)

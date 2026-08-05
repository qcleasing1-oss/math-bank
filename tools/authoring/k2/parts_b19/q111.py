# -*- coding: utf-8 -*-
add(
    111,
    ['7.1', '7.5'],
    'ยาก',
    'รูปสิบสองเหลี่ยมด้านเท่ามุมเท่ารูปหนึ่งแนบในวงกลมซึ่งมีรัศมียาว $r$ หน่วย '
    'เส้นรอบรูปของรูปสิบสองเหลี่ยมรูปนี้เท่ากับข้อใด',
    [
        '$6r\\left(\\sqrt{6} - \\sqrt{2}\\right)$',
        '$2\\pi r$',
        '$24r\\left(2 - \\sqrt{3}\\right)$',
        '$12r$',
    ],
    0,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• รูปหลายเหลี่ยมด้านเท่ามุมเท่าที่ “แนบใน” วงกลม หมายถึงรูปที่จุดยอด<b>ทุกจุด</b>อยู่บนเส้นรอบวงพอดี '
        'ผลที่ตามมาคือระยะจากจุดศูนย์กลางของวงกลมไปยังจุดยอดแต่ละจุดยาวเท่ากันหมด และเท่ากับรัศมี $r$ '
        'ถ้าลากส่วนของเส้นตรงจากจุดศูนย์กลางไปยังจุดยอดครบทุกจุด รูป $n$ เหลี่ยมจะถูกซอยออกเป็นสามเหลี่ยม<b>หน้าจั่ว</b> '
        '$n$ รูปที่เท่ากันทุกประการ โดยขาทั้งสองข้างของทุกรูปยาว $r$ เท่ากันหมด',
        '• มุมรอบจุดหนึ่งจุดรวมกันได้ $360^{\\circ}$ เสมอ เมื่อสามเหลี่ยมหน้าจั่วทั้ง $n$ รูปเท่ากันทุกประการ '
        'มุมที่จุดศูนย์กลางของแต่ละรูปจึงต้องเท่ากันหมด และมีขนาดเท่ากับ $\\dfrac{360^{\\circ}}{n}$ '
        'มุมนี้เรียกว่ามุมที่จุดศูนย์กลางซึ่งรองรับด้านหนึ่งด้าน',
        '• ในสามเหลี่ยมหน้าจั่ว เส้นตั้งฉากที่ลากจากยอด (จุดที่ขาสองข้างมาบรรจบกัน) ลงไปยังฐาน '
        'จะ<b>แบ่งครึ่งทั้งฐานและแบ่งครึ่งมุมยอด</b>พร้อมกัน เหตุผลคือสามเหลี่ยมย่อยสองรูปที่ถูกแบ่งออกมา '
        'มีด้านตรงข้ามมุมฉากยาวเท่ากัน (ขาของหน้าจั่วทั้งคู่) มีด้านตั้งฉากเป็นด้านร่วม และมีมุมฉากทั้งคู่ '
        'จึงเท่ากันทุกประการ ⇒ ด้านที่คู่กันยาวเท่ากัน และมุมที่คู่กันมีขนาดเท่ากัน',
        '• อัตราส่วนตรีโกณมิติในสามเหลี่ยมมุมฉาก : $\\sin$ ของมุมแหลมมุมหนึ่ง '
        'เท่ากับความยาวด้านตรงข้ามมุมนั้น หารด้วยความยาวด้านตรงข้ามมุมฉาก '
        'ย้ายข้างได้เป็น “ด้านตรงข้ามมุม $=$ ด้านตรงข้ามมุมฉาก $\\times \\sin$ ของมุมนั้น”',
        '• สูตรผลต่างมุมของไซน์ : $\\sin(A - B) = \\sin A\\cos B - \\cos A\\sin B$ '
        '⛔ สังเกตว่าเครื่องหมายตรงกลางเป็นลบตามเครื่องหมายในวงเล็บ และตัวหน้าเป็น $\\sin$ คูณ $\\cos$ '
        'ส่วนตัวหลังเป็น $\\cos$ คูณ $\\sin$ (สลับกัน) ห้ามเขียนเป็น $\\sin A \\sin B$ เด็ดขาด · '
        'ค่ามุมพิเศษที่ต้องใช้คือ $\\sin 45^{\\circ} = \\dfrac{1}{\\sqrt{2}}$ · $\\cos 45^{\\circ} = \\dfrac{1}{\\sqrt{2}}$ '
        '· $\\sin 30^{\\circ} = \\dfrac{1}{2}$ · $\\cos 30^{\\circ} = \\dfrac{\\sqrt{3}}{2}$',
        '• การทำตัวส่วนให้เป็นจำนวนตรรกยะ : ถ้ามีกรณฑ์ค้างอยู่ที่ตัวส่วน ให้คูณทั้งตัวเศษและตัวส่วนด้วยกรณฑ์ตัวนั้น '
        'เช่น $\\dfrac{1}{\\sqrt{2}} = \\dfrac{1 \\times \\sqrt{2}}{\\sqrt{2} \\times \\sqrt{2}} = \\dfrac{\\sqrt{2}}{2}$ '
        'ทำได้เพราะ $\\sqrt{2} \\times \\sqrt{2} = 2$ ซึ่งเป็นจำนวนตรรกยะแล้ว · '
        'และกฎคูณกรณฑ์ที่ต้องใช้ตามมาคือ $\\sqrt{a} \\times \\sqrt{b} = \\sqrt{ab}$ เมื่อ $a$ และ $b$ ไม่เป็นลบ',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• รูปหลายเหลี่ยมด้านเท่ามุมเท่าที่มี $12$ ด้าน (จำนวนด้าน $n = 12$ และมีจุดยอด $12$ จุดเช่นกัน)',
        '• รูปนี้แนบในวงกลมซึ่งมีรัศมียาว $r$ หน่วย ⇒ จุดยอดทั้ง $12$ จุดอยู่บนเส้นรอบวง '
        'และระยะจากจุดศูนย์กลางถึงจุดยอดทุกจุดยาว $r$ เท่ากันหมด',
        '• สังเกตหน้าตาก่อนลงมือ : โจทย์ไม่ได้ให้ตัวเลขของรัศมีมาเลย ให้มาเป็นตัวอักษร $r$ '
        'คำตอบจึงต้องอยู่ในรูปค่าคงตัวคูณกับ $r$ กำลังหนึ่ง (ความยาวคูณจำนวนเท่า ยังคงเป็นความยาว) '
        'ไม่ใช่ $r^2$ ซึ่งเป็นหน้าตาของพื้นที่ · และเนื่องจาก $\\dfrac{360^{\\circ}}{12} = 30^{\\circ}$ '
        'ลงตัวสวยงาม เดาได้ตั้งแต่ยังไม่คิดว่าจะต้องไปเจอมุม $30^{\\circ}$ หรือครึ่งของมัน',
        '• ⛔ จุดที่ต้องตั้งสติ : สิ่งที่โจทย์ถามคือเส้นรอบรูปของรูป<b>สิบสองเหลี่ยม</b> '
        'ไม่ใช่เส้นรอบวงของวงกลม ทั้งสองอย่างนี้เป็นคนละเส้นกัน',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาเส้นรอบรูปของรูปสิบสองเหลี่ยมด้านเท่ามุมเท่ารูปนี้ ในรูปของ $r$ '
        'ซึ่งก็คือผลรวมความยาวของด้านทั้ง $12$ ด้าน และเพราะทุกด้านยาวเท่ากัน จึงเท่ากับ $12$ คูณความยาวของด้านหนึ่งด้าน',
        '',
        '<b>【 ลากรัศมีไปยังจุดยอดทุกจุดเพื่อซอยรูปเป็นสามเหลี่ยมหน้าจั่ว $12$ รูป '
        'แล้วลากเส้นตั้งฉากจากจุดศูนย์กลางลงบนด้านหนึ่งเพื่อได้สามเหลี่ยมมุมฉากที่มีมุม $15^{\\circ}$ '
        'อ่านครึ่งด้านเป็น $r\\sin 15^{\\circ}$ จากนั้นสร้างค่า $\\sin 15^{\\circ}$ ขึ้นมาเองด้วยสูตรผลต่างมุม '
        '$45^{\\circ} - 30^{\\circ}$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · หามุมที่จุดศูนย์กลางซึ่งรองรับด้านหนึ่งด้าน</b>',
        '• สูตรที่ใช้ : มุมที่จุดศูนย์กลางของรูป $n$ เหลี่ยมด้านเท่ามุมเท่าที่แนบในวงกลม $= \\dfrac{360^{\\circ}}{n}$',
        '• ที่มาของสูตรนี้ (อย่าท่องเฉย ๆ) : ตั้งชื่อจุดศูนย์กลางว่า $O$ แล้วลากส่วนของเส้นตรงจาก $O$ '
        'ไปยังจุดยอดทั้ง $12$ จุด จะได้สามเหลี่ยม $12$ รูปที่มีจุดยอด $O$ ร่วมกัน '
        'ทุกรูปมีขาสองข้างยาว $r$ เท่ากัน และมีฐานเป็นด้านของรูปสิบสองเหลี่ยมซึ่งยาวเท่ากันหมด '
        '⇒ ทั้ง $12$ รูปเท่ากันทุกประการแบบ ด.ด.ด. ⇒ มุมที่จุด $O$ ของทุกรูปมีขนาดเท่ากัน',
        '• มุม $12$ มุมนี้เรียงต่อกันจนรอบจุด $O$ พอดี ผลรวมจึงเป็น $360^{\\circ}$',
        '• ระบุตัวแปร : ให้ $A$ และ $B$ เป็นจุดยอดสองจุดที่อยู่ติดกัน จะได้ $OA = OB = r$ '
        'และ $AB$ คือด้านหนึ่งด้านของรูปสิบสองเหลี่ยม',
        '• แทนค่า $n = 12$ : ขนาดของมุม $A\\hat{O}B = \\dfrac{360^{\\circ}}{12} = 30^{\\circ}$',
        '',
        '<b>ขั้นที่ 2 · ลากเส้นตั้งฉากจากจุดศูนย์กลาง แล้วอ่านครึ่งด้านด้วย $\\sin$ (กุญแจดอกที่หนึ่ง)</b>',
        '• ลากเส้นตั้งฉากจากจุด $O$ ลงไปพบด้าน $AB$ ที่จุด $M$ '
        'ตอนนี้สามเหลี่ยมหน้าจั่ว $OAB$ ถูกแบ่งเป็นสามเหลี่ยมมุมฉากสองรูป คือ $OMA$ กับ $OMB$',
        '• สามเหลี่ยมสองรูปนี้เท่ากันทุกประการ เพราะ $OA = OB = r$ (ด้านตรงข้ามมุมฉากยาวเท่ากัน) '
        '· $OM$ เป็นด้านร่วม · และมุมที่ $M$ เป็นมุมฉากทั้งคู่',
        '• 🔑 <b>กุญแจดอกที่หนึ่ง</b> ผลจากการเท่ากันทุกประการมีสองอย่างที่ต้องใช้ '
        '(1) $AM = MB$ ⇒ จุด $M$ เป็นจุดกึ่งกลางของด้าน $AB$ ⇒ $AM$ คือ<b>ครึ่งหนึ่ง</b>ของด้าน '
        '(2) มุม $A\\hat{O}M$ มีขนาดเท่ากับมุม $B\\hat{O}M$ ⇒ มุมที่จุดศูนย์กลางถูกแบ่งครึ่งด้วย '
        '⇒ มุมที่จะเข้าสูตรคือ $\\dfrac{30^{\\circ}}{2} = 15^{\\circ}$ '
        '⛔ ไม่ใช่มุมเต็ม $30^{\\circ}$ เพราะมุม $30^{\\circ}$ ไม่ได้อยู่ในสามเหลี่ยมมุมฉากรูปใดเลย',
        '• สูตรที่ใช้ : ในสามเหลี่ยมมุมฉาก ด้านตรงข้ามมุม $=$ ด้านตรงข้ามมุมฉาก $\\times \\sin$ ของมุมนั้น',
        '• ระบุตัวแปรในสามเหลี่ยมมุมฉาก $OMA$ : มุมที่จุด $O$ มีขนาด $15^{\\circ}$ '
        '· ด้านตรงข้ามมุมนี้คือ $AM$ · ด้านตรงข้ามมุมฉากคือ $OA$ ซึ่งยาว $r$',
        '• แทนค่า : $AM = OA \\times \\sin 15^{\\circ} = r\\sin 15^{\\circ}$',
        '• ยุบเป็นความยาวด้านเต็ม : $AB = 2 \\times AM = 2r\\sin 15^{\\circ}$',
        '• 🔑 <b>กุญแจดอกที่สอง</b> ด้าน $AB$ เป็น<b>ส่วนของเส้นตรง</b>ที่เชื่อมจุดยอดสองจุด '
        'จึงเป็น “คอร์ด” ของวงกลม ⛔ ไม่ใช่ “ส่วนโค้ง” ที่โค้งไปตามขอบวงกลม '
        'เส้นตรงเป็นทางที่สั้นที่สุดระหว่างจุดสองจุดเสมอ คอร์ดจึงสั้นกว่าส่วนโค้งที่รองรับกันเสมอ '
        '⇒ เส้นรอบรูปของรูปสิบสองเหลี่ยมต้องสั้นกว่าเส้นรอบวงเสมอ ⇒ ⛔ ห้ามตอบเส้นรอบวง',
        '',
        '<b>ขั้นที่ 3 · สร้างค่า $\\sin 15^{\\circ}$ ขึ้นมาเองด้วยสูตรผลต่างมุม</b>',
        '• $15^{\\circ}$ ไม่ใช่มุมพิเศษที่ท่องกันมา แต่เขียนเป็นผลต่างของมุมพิเศษสองมุมได้ : '
        '$15^{\\circ} = 45^{\\circ} - 30^{\\circ}$ ซึ่งทั้ง $45^{\\circ}$ และ $30^{\\circ}$ เป็นมุมที่รู้ค่าอยู่แล้ว',
        '• สูตรที่ใช้ : $\\sin(A - B) = \\sin A\\cos B - \\cos A\\sin B$',
        '• ระบุตัวแปร : $A = 45^{\\circ}$ และ $B = 30^{\\circ}$ '
        '⇒ $\\sin 15^{\\circ} = \\sin 45^{\\circ}\\cos 30^{\\circ} - \\cos 45^{\\circ}\\sin 30^{\\circ}$',
        '• ก่อนแทนค่า ให้จัดค่ามุม $45^{\\circ}$ ให้ตัวส่วนเป็นจำนวนตรรกยะเสียก่อน : '
        '$\\sin 45^{\\circ} = \\dfrac{1}{\\sqrt{2}} = \\dfrac{1 \\times \\sqrt{2}}{\\sqrt{2} \\times \\sqrt{2}} '
        '= \\dfrac{\\sqrt{2}}{2}$ และในทำนองเดียวกัน $\\cos 45^{\\circ} = \\dfrac{\\sqrt{2}}{2}$ '
        'ทำขั้นนี้ก่อนจะทำให้บรรทัดถัดไปไม่มีกรณฑ์ค้างอยู่ที่ตัวส่วนเลย',
        '• แทนค่าทั้งสี่ตัวลงในสูตร : '
        '$\\sin 15^{\\circ} = \\dfrac{\\sqrt{2}}{2} \\times \\dfrac{\\sqrt{3}}{2} '
        '- \\dfrac{\\sqrt{2}}{2} \\times \\dfrac{1}{2}$',
        '• คูณเศษกับเศษ ส่วนกับส่วน โดยใช้ $\\sqrt{2} \\times \\sqrt{3} = \\sqrt{6}$ : '
        '$\\sin 15^{\\circ} = \\dfrac{\\sqrt{6}}{4} - \\dfrac{\\sqrt{2}}{4}$',
        '• ตัวส่วนเท่ากันแล้ว รวมเป็นเศษส่วนเดียว : '
        '$\\sin 15^{\\circ} = \\dfrac{\\sqrt{6} - \\sqrt{2}}{4}$ '
        '⛔ ห้ามเผลอตัด $\\sqrt{6}$ กับ $\\sqrt{2}$ ให้เหลือ $\\sqrt{3}$ เพราะเครื่องหมายตรงกลางเป็นลบ ไม่ใช่หาร',
        '• ประเมินค่าไว้ตรวจ : $\\sqrt{6} \\approx 2.4495$ และ $\\sqrt{2} \\approx 1.4142$ '
        '⇒ $\\sin 15^{\\circ} \\approx \\dfrac{1.0353}{4} \\approx 0.2588$ '
        'ซึ่งเป็นจำนวนบวกที่น้อยกว่า $1$ สมเหตุสมผลกับการที่ $15^{\\circ}$ เป็นมุมแหลมขนาดเล็ก',
        '',
        '<b>ขั้นที่ 4 · คูณด้วยจำนวนด้านเพื่อให้ได้เส้นรอบรูป</b>',
        '• สูตรที่ใช้ : เส้นรอบรูป $=$ จำนวนด้าน $\\times$ ความยาวของด้านหนึ่งด้าน '
        '(ใช้ได้เพราะรูปนี้ด้านเท่าทุกด้าน)',
        '• ระบุตัวแปร : จำนวนด้าน $= 12$ และความยาวด้านหนึ่งด้าน $= 2r\\sin 15^{\\circ}$ จากขั้นที่ 2',
        '• แทนค่า : เส้นรอบรูป $= 12 \\times 2r\\sin 15^{\\circ} = 24r\\sin 15^{\\circ}$',
        '• นำค่า $\\sin 15^{\\circ} = \\dfrac{\\sqrt{6} - \\sqrt{2}}{4}$ จากขั้นที่ 3 มาแทนต่อ : '
        'เส้นรอบรูป $= 24r \\times \\dfrac{\\sqrt{6} - \\sqrt{2}}{4}$',
        '• ยุบตัวเลข $\\dfrac{24}{4} = 6$ ได้ เส้นรอบรูป $= 6r\\left(\\sqrt{6} - \\sqrt{2}\\right)$ หน่วย',
        '• ค่าประมาณของคำตอบ : $6 \\times 1.0353 \\approx 6.2117$ ⇒ เส้นรอบรูปยาวประมาณ $6.2117r$ หน่วย',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · สร้าง $\\sin 15^{\\circ}$ ขึ้นใหม่ด้วยสูตรมุมสองเท่าของโคไซน์ '
        'โดยไม่แตะสูตรผลต่างมุมเลย แล้วเทียบค่าประมาณกับเส้นรอบวง)</b>',
        '• เดินคนละทางกับขั้นที่ 3 โดยเริ่มจากสูตรมุมสองเท่า $\\cos 2\\theta = 1 - 2\\sin^2\\theta$ '
        'แล้วให้ $\\theta = 15^{\\circ}$ ⇒ $2\\theta = 30^{\\circ}$ ซึ่งเป็นมุมพิเศษที่รู้ค่า',
        '• ได้ $\\cos 30^{\\circ} = 1 - 2\\sin^2 15^{\\circ}$ ⇒ '
        '$\\dfrac{\\sqrt{3}}{2} = 1 - 2\\sin^2 15^{\\circ}$ ⇒ '
        '$2\\sin^2 15^{\\circ} = 1 - \\dfrac{\\sqrt{3}}{2} = \\dfrac{2 - \\sqrt{3}}{2}$ ⇒ '
        '$\\sin^2 15^{\\circ} = \\dfrac{2 - \\sqrt{3}}{4}$',
        '• นำคำตอบจากเส้นทางเดิมมายกกำลังสองเทียบดู : '
        '$\\left(\\dfrac{\\sqrt{6} - \\sqrt{2}}{4}\\right)^2 '
        '= \\dfrac{6 - 2\\sqrt{6}\\sqrt{2} + 2}{16} = \\dfrac{8 - 2\\sqrt{12}}{16} '
        '= \\dfrac{8 - 4\\sqrt{3}}{16} = \\dfrac{2 - \\sqrt{3}}{4}$ '
        'ตรงกันเป๊ะกับที่สูตรมุมสองเท่าให้ ✓ (และ $15^{\\circ}$ เป็นมุมแหลม $\\sin$ จึงเป็นบวก '
        'รากที่สองจึงเลือกค่าบวกได้ทันที)',
        '• ตรวจชั้นที่สองด้วยสามัญสำนึกเชิงเรขาคณิต : เส้นรอบวงของวงกลมยาว $2\\pi r \\approx 6.2832r$ '
        'ส่วนเส้นรอบรูปที่คำนวณได้ยาวประมาณ $6.2117r$ ซึ่งน้อยกว่าอยู่เล็กน้อย '
        'ตรงกับข้อเท็จจริงว่ารูปหลายเหลี่ยมแนบในต้องมีเส้นรอบรูปสั้นกว่าเส้นรอบวงเสมอ '
        'และเมื่อจำนวนด้านมากถึง $12$ ด้าน รูปก็เกือบกลมแล้ว ค่าจึงควรใกล้กันมากอย่างที่เห็น ✓',
        '• ตรวจชั้นที่สามด้วยกรณีที่รู้คำตอบอยู่แล้ว : ถ้าใช้วิธีเดียวกันกับรูปหกเหลี่ยมด้านเท่า '
        '($n = 6$) จะได้ด้านยาว $2r\\sin 30^{\\circ} = 2r\\left(\\dfrac{1}{2}\\right) = r$ '
        'ซึ่งถูกต้อง เพราะรูปหกเหลี่ยมด้านเท่าที่แนบในวงกลมมีด้านยาวเท่ากับรัศมีพอดี '
        '⇒ กลไก “ครึ่งมุมกับครึ่งคอร์ด” ที่ใช้ในข้อนี้ผ่านการทดสอบกับกรณีที่ตรวจสอบได้ด้วยตาแล้ว ✓',
        '',
        '✅ <b>คำตอบ</b> เส้นรอบรูปของรูปสิบสองเหลี่ยมด้านเท่ามุมเท่ารูปนี้เท่ากับ '
        '$6r\\left(\\sqrt{6} - \\sqrt{2}\\right)$ หน่วย → <b>ตัวเลือก 1</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• สรุปเป็นสูตรกลางไว้ใช้ได้ทุกข้อ : รูป $n$ เหลี่ยมด้านเท่ามุมเท่าที่แนบในวงกลมรัศมี $r$ '
        'มีด้านยาว $2r\\sin\\dfrac{180^{\\circ}}{n}$ และมีเส้นรอบรูป $2nr\\sin\\dfrac{180^{\\circ}}{n}$ '
        'สังเกตว่ามุมในสูตรเป็น $\\dfrac{180^{\\circ}}{n}$ ไม่ใช่ $\\dfrac{360^{\\circ}}{n}$ '
        'เพราะถูกแบ่งครึ่งไปแล้วหนึ่งครั้ง · วิธีตรวจว่าจำสูตรถูกคือแทน $n = 6$ '
        'ถ้าได้ด้านยาว $r$ พอดีแสดงว่าจำถูก',
        '• เจอมุมที่ไม่ใช่มุมพิเศษ ให้พยายามเขียนเป็นผลบวกหรือผลต่างของมุมพิเศษก่อนเสมอ : '
        '$15^{\\circ} = 45^{\\circ} - 30^{\\circ}$ · $75^{\\circ} = 45^{\\circ} + 30^{\\circ}$ '
        '· $105^{\\circ} = 60^{\\circ} + 45^{\\circ}$ · $165^{\\circ} = 120^{\\circ} + 45^{\\circ}$',
        '• ใช้ $2\\pi r \\approx 6.2832r$ เป็นเพดานตรวจคำตอบของโจทย์แนวนี้ '
        'คำตอบที่เป็นเส้นรอบรูปของรูปหลายเหลี่ยมแนบในต้อง<b>น้อยกว่า</b>ค่านี้เสมอ '
        'ส่วนรูปหลายเหลี่ยมที่แนบนอกวงกลม (ทุกด้านสัมผัสวงกลม) ต้อง<b>มากกว่า</b>ค่านี้เสมอ '
        'แค่ประมาณค่าเป็นทศนิยมก็คัดค่าที่เป็นไปไม่ได้ทิ้งได้ทันทีโดยไม่ต้องคิดใหม่ทั้งข้อ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $2\\pi r$ เพราะคิดว่าเส้นรอบรูปของรูปสิบสองเหลี่ยมคือความยาวรอบวงกลม '
        'นั่นคือหลงว่าด้านของรูปหลายเหลี่ยมคือส่วนโค้ง ทั้งที่ด้านเป็นคอร์ด (ส่วนของเส้นตรง) · '
        'พิสูจน์ว่าผิด : ระหว่างจุดยอดสองจุดที่ติดกัน คอร์ด $AB$ เป็นเส้นตรง ส่วนโค้งเป็นเส้นโค้ง '
        'และเส้นตรงคือทางที่สั้นที่สุดระหว่างจุดสองจุด ⇒ คอร์ดสั้นกว่าส่วนโค้งเสมอ '
        'เมื่อบวกครบทั้ง $12$ คู่ ผลรวมของคอร์ดจึงต้องน้อยกว่าผลรวมของส่วนโค้งซึ่งก็คือเส้นรอบวง '
        '⇒ คำตอบต้องน้อยกว่า $2\\pi r$ อย่างเคร่งครัด ค่านี้จึงเป็นไปไม่ได้ · '
        'ตัวเลขก็ยืนยัน : $6.2832r > 6.2117r$',
        '• ได้ค่า $24r\\left(2 - \\sqrt{3}\\right)$ เพราะใช้ $\\tan 15^{\\circ}$ แทน $\\sin 15^{\\circ}$ '
        'คือไปเขียนว่า $AM = OM\\tan 15^{\\circ}$ แล้วเผลอใช้ $OM = r$ ทั้งที่ $r$ คือ $OA$ ไม่ใช่ $OM$ · '
        'ค่านี้เท่ากับ $24r\\tan 15^{\\circ}$ ซึ่งเป็นเส้นรอบรูปของรูปสิบสองเหลี่ยมที่แนบ<b>นอก</b>วงกลม '
        '(รูปที่ทุกด้านสัมผัสวงกลม จึงมีระยะจากจุดศูนย์กลางถึงกึ่งกลางด้านเท่ากับ $r$) · '
        'พิสูจน์ว่าผิด : $2 - \\sqrt{3} \\approx 0.2679$ ⇒ ค่านี้ประมาณ $6.4308r$ '
        'ซึ่ง<b>มากกว่า</b>เส้นรอบวง $6.2832r$ เป็นไปไม่ได้สำหรับรูปที่อยู่ข้างในวงกลมทั้งรูป '
        'เพราะเส้นรอบรูปของรูปนูนที่อยู่ภายในรูปนูนอีกรูปหนึ่งต้องสั้นกว่าเสมอ · '
        'ตัวจับผิดที่เร็วที่สุดคือถามตัวเองว่า $r$ ที่โจทย์ให้เป็นระยะถึง<b>จุดยอด</b>หรือถึง<b>กึ่งกลางด้าน</b> '
        'คำว่า “แนบใน” บอกว่าจุดยอดอยู่บนวงกลม ⇒ $r$ เป็นด้านตรงข้ามมุมฉาก ⇒ ต้องใช้ $\\sin$',
        '• ได้ค่า $12r$ เพราะใช้มุมเต็ม $30^{\\circ}$ แทนครึ่งมุม $15^{\\circ}$ '
        'คือเขียนเป็น $24r\\sin 30^{\\circ} = 24r\\left(\\dfrac{1}{2}\\right) = 12r$ '
        'ซึ่งเกิดจากการลืมว่าเส้นตั้งฉากแบ่งครึ่งมุมที่จุดศูนย์กลางไปแล้ว · '
        'พิสูจน์ว่าผิดสองชั้น : (1) $12r > 6.2832r$ ยาวเป็นเกือบสองเท่าของเส้นรอบวง เป็นไปไม่ได้ '
        '(2) เส้นทางนี้ให้ด้านหนึ่งด้านยาว $2r\\sin 30^{\\circ} = r$ ซึ่งเป็นความยาวด้านของรูป<b>หกเหลี่ยม</b> '
        'ด้านเท่าที่แนบในวงกลมวงเดียวกัน แต่รูปสิบสองเหลี่ยมมีด้านมากกว่าเป็นสองเท่า ด้านจึงต้องสั้นกว่า '
        'ไม่ใช่ยาวเท่ากัน',
        '• ได้ค่า $3r\\left(\\sqrt{6} - \\sqrt{2}\\right)$ เพราะหยุดที่ครึ่งคอร์ด '
        'คือเอา $AM = r\\sin 15^{\\circ}$ ไปคูณ $12$ ตรง ๆ โดยลืมคูณ $2$ เพื่อทำให้เป็นด้านเต็ม $AB$ · '
        'พิสูจน์ว่าผิด : ค่านี้ประมาณ $3.1058r$ · จับจุดยอดสองจุดที่อยู่ตรงข้ามกันในรูปสิบสองเหลี่ยม '
        'ระยะระหว่างจุดทั้งสองคือเส้นผ่านศูนย์กลางยาว $2r$ และขอบของรูปถูกแบ่งเป็นสองทางเดินที่เชื่อมจุดทั้งสอง '
        'ทางเดินแต่ละทางยาวไม่น้อยกว่า $2r$ (เพราะเส้นตรงสั้นที่สุด) ⇒ เส้นรอบรูปต้องยาวอย่างน้อย $4r$ '
        'แต่ $3.1058r < 4r$ ⇒ เป็นไปไม่ได้ · '
        'วิธีกันคือเขียนกำกับไว้ทุกครั้งว่าสิ่งที่ $\\sin$ ให้มาคือ<b>ครึ่งด้าน</b> ไม่ใช่ด้านเต็ม',
    ],
    'V.mold: G = a regular twelve-sided polygon inscribed in a circle whose radius is handed over as the '
    'bare letter r, with no numeric length anywhere in the statement / A = the perimeter of that polygon, '
    'expressed in terms of r / M = split the polygon into twelve congruent isosceles triangles by drawing '
    'the radii to every vertex, drop the perpendicular from the centre onto one side so that it bisects '
    'both the side and the central angle, read the half-side as r*sin(15 degrees) out of the resulting '
    'right triangle, manufacture sin(15 degrees) from the sine difference formula on 45 minus 30 degrees, '
    'and finally multiply the side by twelve. '
    'Rubric F3 C2 P3 T2 L1 = 11/15 with total at least 8 and T at least 2 -> level: ยาก, the third '
    'band, matching the level recorded for this item in stems_b19. '
    'F = 3 because three separate knowledge blocks are each load bearing: the central angle of a regular '
    'n-gon equals 360/n, the perpendicular from the centre of a circle bisects a chord and its central '
    'angle, and the exact value of sin(15 degrees) has to be built rather than recalled. Drop any one of '
    'the three and the item cannot be finished. C = 2 because subtopic 7.1 supplies the right-triangle '
    'ratio while 7.5 supplies the compound-angle formula, and neither subtopic closes the item on its own. '
    'P = 3 and not 2 because there are three genuine stages that feed one another in a chain: the central '
    'angle is produced first, it is then reinterpreted as an angle inside a right triangle to yield one '
    'side length, and only then is that length turned into a perimeter. Each stage consumes an object the '
    'previous stage created. T = 2 because two independent turning points sit in the path: the angle that '
    'enters the sine is the half of the central angle rather than the full 30 degrees, and the side of the '
    'polygon is a chord rather than an arc, which is what keeps the circumference from being the answer. '
    'T is held at 2 and not 3 because both turning points are standard consequences of the inscribed '
    'figure and neither requires an auxiliary construction that is not already suggested by the phrase '
    'inscribed in a circle. L = 1 because no diagram accompanies the statement, so the student must draw '
    'the twelve-gon, the two radii and the perpendicular before any formula can be applied; the benchmark '
    'is q072, held at L = 1 for the same unaided construction, and L = 0 is not available because the '
    'statement is not pure symbol manipulation. Scoring was written before the level was read off. '
    'sympy (verify_b19.py): 12*2*r*sin(pi/12) was simplified and expanded and matches '
    '6*r*(sqrt(6) - sqrt(2)) exactly, so the closed form in the answer line is machine confirmed rather '
    'than hand-simplified. The construction of the special value was checked separately: '
    'sin(rad(45))*cos(rad(30)) - cos(rad(45))*sin(rad(30)) simplifies to sin(pi/12), which is exactly the '
    'difference-formula step written out in step 3. Every wrong path was machine computed from a named '
    'error rather than invented: 24*r*sin(pi/6) returns 12*r for the student who feeds the full central '
    'angle into the sine instead of its half, 24*r*tan(pi/12) simplifies to 24*r*(2 - sqrt(3)) for the '
    'student who uses the circumscribed configuration by taking r as the apothem, and 2*pi*r stands for '
    'the student who mistakes the chord for the arc. Numerically the four coefficients of r are 6.2117, '
    '6.2832, 6.4308 and 12, so the two impossible values sit above the circumference bound 2*pi and are '
    'refuted by that bound alone. The half-side slip 12*r*sin(pi/12) was also evaluated, giving about '
    '3.1058*r, below the convexity floor 4*r. '
    'Collision sweep on 6417 items (bank 63 files + k1 out + k2 out), probe collide_b19.py / '
    'collide_b19b.py: scan A7 (regular equilateral and equiangular polygon in the question text) returns '
    '0 items and scan A7b (polygon inscribed in a circle together with a request for a perimeter) also '
    'returns 0 items. The two wide scans were then read by hand: S5 (the Thai word for polygon-sided '
    'appearing together with the word for circle) returns 29 items and S6 (a polygon whose side count is '
    'spelled out as a Thai word) returns 7 items, and in both lists every hit asks for an area, a '
    'coordinate, or a count of line segments, never for a perimeter. The three closest neighbours are '
    'chap-07-trigonometry-q106, which puts an n-sided regular polygon in a circle of radius a and asks for '
    'the area, and chap-07-q214 together with chap-07-q216, which do the same for a hexagon. All three '
    'share the figure but differ in A, so the radius here is deliberately named r rather than a to keep '
    'even the surface of q106 from being echoed, and the area question is deliberately not asked. Choices '
    'are ordered ascending by the numeric coefficient of r (6.2117, then 6.2832, then 6.4308, then 12), '
    'so the answer slot is forced by that rule and was not chosen.',
)

# -*- coding: utf-8 -*-
add_fill(
    130,
    ['7.11'],
    'ง่าย',
    'วงกลมสองวงมีรัศมียาว $6$ หน่วย และ $15$ หน่วย ตามลำดับ ส่วนโค้ง $A$ '
    'เป็นส่วนโค้งบนวงกลมที่มีรัศมียาว $6$ หน่วย และส่วนโค้ง $B$ '
    'เป็นส่วนโค้งบนวงกลมที่มีรัศมียาว $15$ หน่วย '
    'โดยส่วนโค้งทั้งสองเส้นรองรับมุมที่จุดศูนย์กลางของวงกลมวงของตนซึ่งมีขนาดเท่ากัน '
    'ถ้า $s_A$ และ $s_B$ เป็นความยาวของส่วนโค้ง $A$ และความยาวของส่วนโค้ง $B$ '
    'ตามลำดับ แล้วค่าของ $\\dfrac{s_B}{s_A}$ เท่ากับเท่าใด',
    '5/2',
    ['5/2', '\\dfrac{5}{2}', '2.5'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ความยาวของส่วนโค้งบนวงกลมหาได้จากสูตร $s = r\\theta$ '
        'โดย $s$ คือความยาวของส่วนโค้ง · $r$ คือรัศมีของวงกลมวงนั้น '
        'และ $\\theta$ คือขนาดของมุมที่จุดศูนย์กลางซึ่งส่วนโค้งเส้นนั้นรองรับอยู่ '
        '⛔ สูตรนี้ใช้ได้ก็ต่อเมื่อวัดมุมเป็น<b>เรเดียน</b>เท่านั้น '
        'ถ้าโจทย์ให้มุมมาเป็นองศาต้องแปลงเป็นเรเดียนก่อนเสมอ',
        '• เหตุผลที่สูตรออกมาหน้าตาแบบนี้ มาจากนิยามของเรเดียนโดยตรง : '
        'มุมขนาด $1$ เรเดียน คือมุมที่จุดศูนย์กลางซึ่งรองรับส่วนโค้งที่ยาวเท่ากับรัศมีพอดี '
        'ดังนั้นมุมขนาด $\\theta$ เรเดียน ก็ย่อมรองรับส่วนโค้งที่ยาวเป็น $\\theta$ เท่าของรัศมี '
        'นั่นคือ $s = r\\theta$ · จำนิยามนี้ไว้จะไม่หลงจำสูตรผิด',
        '• อ่านสูตร $s = r\\theta$ ให้เป็นภาษาคน : ถ้ามุมถูกตรึงไว้ไม่ให้เปลี่ยน '
        'ความยาวของส่วนโค้งจะแปรผันตรงกับรัศมี<b>กำลังหนึ่ง</b> '
        'คือวงกลมรัศมียาวเป็นสองเท่า ส่วนโค้งที่รองรับมุมเดิมก็ยาวเป็นสองเท่าตามไปด้วยพอดี '
        '⛔ ไม่ใช่สี่เท่า เพราะกำลังสองเป็นเรื่องของ<b>พื้นที่</b> ไม่ใช่ความยาว '
        '(พื้นที่เซกเตอร์คือ $A = \\dfrac{1}{2}r^{2}\\theta$ ซึ่งมี $r$ ยกกำลังสองอยู่จริง)',
        '• เมื่อนำสองปริมาณมาหารกันเป็นอัตราส่วน ตัวประกอบใดที่เหมือนกันทั้งเศษและส่วนจะตัดกันทิ้งเสมอ '
        'เช่น $\\dfrac{15k}{6k} = \\dfrac{15}{6}$ สำหรับทุกค่า $k$ ที่ไม่เป็นศูนย์ '
        'สมบัตินี้เองที่ทำให้โจทย์บางข้อตอบได้ทั้งที่ยังมีตัวเลขบางตัวไม่รู้ค่า',
        '• ⛔ ต้องแยกให้ขาดระหว่าง “อัตราส่วน” กับ “ผลต่าง” : อัตราส่วนเกิดจากการ<b>หาร</b> '
        'ตอบว่าของสิ่งหนึ่งเป็นกี่เท่าของอีกสิ่งหนึ่ง และเป็นจำนวนล้วนที่ไม่มีหน่วย '
        'ส่วนผลต่างเกิดจากการ<b>ลบ</b> ตอบว่าต่างกันอยู่เท่าไร และยังคงมีหน่วยติดอยู่ '
        'คำถามที่ขึ้นต้นว่า “ค่าของ $\\dfrac{s_B}{s_A}$” จึงเป็นคำถามฝั่งหาร ไม่ใช่ฝั่งลบ',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• มีวงกลมสองวง วงแรกรัศมียาว $6$ หน่วย และวงที่สองรัศมียาว $15$ หน่วย',
        '• ส่วนโค้ง $A$ อยู่บนวงกลมที่มีรัศมียาว $6$ หน่วย ⇒ ใช้ $r = 6$ กับส่วนโค้งเส้นนี้',
        '• ส่วนโค้ง $B$ อยู่บนวงกลมที่มีรัศมียาว $15$ หน่วย ⇒ ใช้ $r = 15$ กับส่วนโค้งเส้นนี้',
        '• มุมที่จุดศูนย์กลางซึ่งส่วนโค้งทั้งสองเส้นรองรับ มีขนาด<b>เท่ากัน</b> '
        '⇒ เขียนแทนมุมทั้งสองด้วยตัวอักษรตัวเดียวกันได้เลย สมมติให้เป็น $\\theta$ เรเดียน',
        '• สังเกตหน้าตาก่อนลงมือ : โจทย์บอกแค่ว่ามุมทั้งสอง<b>เท่ากัน</b> '
        'แต่ไม่เคยบอกเลยว่ามุมนั้นกางกี่เรเดียนหรือกี่องศา ⇒ นี่คือสัญญาณว่าคำตอบต้องออกมาเป็นค่าเดียว '
        'ที่ใช้ได้กับทุกขนาดมุม มิฉะนั้นโจทย์จะตอบไม่ได้ ⇒ เดาได้ตั้งแต่ยังไม่คิดว่า $\\theta$ ต้องตัดกันทิ้ง',
        '• สังเกตอีกอย่าง : สิ่งที่ถามคือ $\\dfrac{s_B}{s_A}$ ซึ่งมี $B$ อยู่<b>ข้างบน</b> '
        'และ $B$ เป็นส่วนโค้งของวงใหญ่ ⇒ คำตอบต้องเป็นจำนวนที่มากกว่า $1$ อย่างแน่นอน',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\dfrac{s_B}{s_A}$ ซึ่งเป็นอัตราส่วนของความยาวส่วนโค้ง $B$ ต่อความยาวส่วนโค้ง $A$',
        '',
        '<b>【 ตั้งชื่อมุมร่วมที่โจทย์บอกว่าเท่ากันว่า $\\theta$ เรเดียน '
        'แล้วเขียนความยาวส่วนโค้งทั้งสองเส้นด้วยสูตร $s = r\\theta$ '
        'จากนั้นนำมาหารกัน $\\theta$ จะตัดกันทิ้งไปเอง เหลือเพียงอัตราส่วนของรัศมีให้ยุบเป็นคำตอบ 】</b>',
        '',
        '<b>ขั้นที่ 1 · ตั้งชื่อมุมร่วม แล้วเขียนความยาวของส่วนโค้ง $A$</b>',
        '• สูตรที่ใช้ : $s = r\\theta$ ใช้ได้เพราะโจทย์กำลังพูดถึงส่วนโค้งของวงกลม '
        'และเราจะกำหนดหน่วยของมุมเป็นเรเดียนเองตั้งแต่ต้น จึงเข้าเงื่อนไขของสูตรพอดี',
        '• ระบุตัวแปรก่อนแทนค่า : ให้มุมที่จุดศูนย์กลางซึ่งส่วนโค้งทั้งสองเส้นรองรับมีขนาด $\\theta$ เรเดียน '
        'ที่เขียนได้เป็นตัวเดียวกันทั้งสองวง ก็เพราะโจทย์ระบุไว้ตรง ๆ ว่ามุมทั้งสองมีขนาดเท่ากัน '
        '⛔ ถ้าโจทย์ไม่ได้บอกข้อนี้ จะตั้งชื่อร่วมกันแบบนี้ไม่ได้เด็ดขาด',
        '• สำหรับส่วนโค้ง $A$ : รัศมีของวงกลมที่ส่วนโค้งเส้นนี้อยู่คือ $r = 6$ หน่วย '
        'และมุมที่รองรับคือ $\\theta$',
        '• แทนค่า : $s_A = r\\theta = 6\\theta$ หน่วย',
        '',
        '<b>ขั้นที่ 2 · เขียนความยาวของส่วนโค้ง $B$ ด้วยสูตรเดียวกัน</b>',
        '• สูตรที่ใช้ : $s = r\\theta$ ตัวเดิม เพราะส่วนโค้ง $B$ ก็เป็นส่วนโค้งของวงกลมเช่นกัน',
        '• ระบุตัวแปร : รัศมีของวงกลมที่ส่วนโค้ง $B$ อยู่คือ $r = 15$ หน่วย '
        'ส่วนมุมที่รองรับยังคงเป็น $\\theta$ ตัวเดิม ⛔ ห้ามตั้งชื่อใหม่เป็นมุมคนละตัว '
        'เพราะจะทิ้งเงื่อนไขสำคัญที่สุดของโจทย์ไปเปล่า ๆ',
        '• แทนค่า : $s_B = r\\theta = 15\\theta$ หน่วย',
        '• เช็คความสมเหตุสมผลทันที : $15\\theta$ มากกว่า $6\\theta$ อยู่แล้วสำหรับทุกมุมที่กางจริง '
        '(นั่นคือ $\\theta > 0$) ⇒ ตรงกับสามัญสำนึกว่ามุมเท่ากันแต่วงใหญ่กว่า ส่วนโค้งย่อมยาวกว่า',
        '',
        '<b>ขั้นที่ 3 · หารกันเพื่อหาอัตราส่วน ⭐ จุดสำคัญของข้อนี้อยู่ตรงนี้</b>',
        '• สิ่งที่ต้องหาคือ $\\dfrac{s_B}{s_A}$ ⇒ นำผลจากขั้นที่ $2$ วางเป็นตัวเศษ '
        'และผลจากขั้นที่ $1$ วางเป็นตัวส่วน',
        '• แทนค่า : $\\dfrac{s_B}{s_A} = \\dfrac{15\\theta}{6\\theta}$',
        '• ⭐ $\\theta$ ปรากฏอยู่ทั้งบนและล่างในฐานะตัวคูณ และ $\\theta$ ไม่เป็นศูนย์ '
        '(เพราะเป็นมุมที่กางจริง มิฉะนั้นส่วนโค้งจะยุบเป็นจุดเดียว) ⇒ ตัดกันทิ้งได้ '
        '$\\dfrac{15\\theta}{6\\theta} = \\dfrac{15}{6}$',
        '• ยุบเศษส่วนด้วยการหารทั้งเศษและส่วนด้วย $3$ : $\\dfrac{15}{6} = \\dfrac{5}{2}$',
        '• 📌 อ่านความหมายของสิ่งที่เพิ่งเกิดขึ้นให้ออก : ค่า $\\theta$ หายไปจากคำตอบจนหมด '
        'แปลว่า<b>อัตราส่วนของความยาวส่วนโค้งเท่ากับอัตราส่วนของรัศมีเสมอ</b> '
        'และค่านี้ไม่ขึ้นกับขนาดของมุมเลยแม้แต่น้อย · '
        'เพราะเหตุนี้โจทย์จึงไม่จำเป็นต้องบอกขนาดมุมมาให้ และเราก็ตอบได้ทั้งที่ไม่รู้ค่ามุม',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไม่ตัดอะไรทิ้งเลย '
        'แต่แทนค่ามุมจริงลงไปสองค่า แล้วคำนวณความยาวส่วนโค้งทั้งสองเส้นแยกกันเป็นตัวเลข)</b>',
        '• เส้นทางแรกได้คำตอบมาจากการตัด $\\theta$ ทิ้ง ⇒ วิธีตรวจที่ไม่ซ้ำทางเดิม '
        'คือเลือกมุมมาสักค่าหนึ่งแล้วคิดความยาวจริงของส่วนโค้งทั้งสองเส้นออกมาก่อน '
        'ค่อยเอามาหารกันทีหลัง ซึ่งไม่ต้องพึ่งการตัดทอนใด ๆ เลย',
        '• ลองมุมแรก $\\theta = \\dfrac{\\pi}{3}$ เรเดียน : '
        '$s_A = 6 \\times \\dfrac{\\pi}{3} = 2\\pi$ หน่วย และ '
        '$s_B = 15 \\times \\dfrac{\\pi}{3} = 5\\pi$ หน่วย '
        '⇒ $\\dfrac{s_B}{s_A} = \\dfrac{5\\pi}{2\\pi} = \\dfrac{5}{2}$ ✓',
        '• ลองมุมที่สอง $\\theta = \\dfrac{\\pi}{6}$ เรเดียน ซึ่งเป็นคนละมุมกับรอบแรกชัดเจน : '
        '$s_A = 6 \\times \\dfrac{\\pi}{6} = \\pi$ หน่วย และ '
        '$s_B = 15 \\times \\dfrac{\\pi}{6} = \\dfrac{5\\pi}{2}$ หน่วย '
        '⇒ $\\dfrac{s_B}{s_A} = \\dfrac{5\\pi}{2} \\div \\pi = \\dfrac{5}{2}$ ✓',
        '• สองรอบใช้มุมต่างกัน ความยาวส่วนโค้งที่ได้ก็เป็นคนละชุด '
        '(รอบแรกได้ $2\\pi$ กับ $5\\pi$ · รอบสองได้ $\\pi$ กับ $\\dfrac{5\\pi}{2}$) '
        'แต่อัตราส่วนออกมาเป็น $\\dfrac{5}{2}$ เท่าเดิมทั้งสองรอบ '
        '⇒ ยืนยันทั้งตัวคำตอบ และยืนยันข้อสรุปที่ว่าคำตอบไม่ขึ้นกับขนาดของมุมจริง ๆ ✓',
        '',
        '✅ <b>คำตอบ</b> ค่าของ $\\dfrac{s_B}{s_A}$ เท่ากับ $\\dfrac{5}{2}$ '
        'ซึ่งเขียนเป็นทศนิยมได้ $2.5$ และเป็นอัตราส่วนล้วนจึงไม่มีหน่วย',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอโจทย์ที่บอกว่าปริมาณบางอย่าง “เท่ากัน” แต่ไม่ยอมบอกค่ามาให้ '
        'ให้รีบตั้งชื่อตัวแปรตัวเดียวแทนมันทั้งสองที่ทันที แล้วเดินสูตรต่อไปตามปกติ '
        'ตัวที่ไม่รู้ค่ามักตัดกันทิ้งตอนหารกันเสมอ ⇒ การไม่รู้ค่ามุมไม่ใช่อุปสรรค แต่เป็นคำใบ้ว่าให้หาร',
        '• จำเส้นแบ่งของกำลังให้แม่น : เมื่อมุมคงที่ ความยาว (ส่วนโค้ง คอร์ด เส้นรอบวง) '
        'แปรผันตามรัศมี<b>กำลังหนึ่ง</b> ส่วนพื้นที่ (เซกเตอร์ วงกลมทั้งวง) '
        'แปรผันตามรัศมี<b>กำลังสอง</b> ⇒ ถามความยาวให้ใช้ $\\dfrac{15}{6}$ '
        'ถามพื้นที่จึงจะใช้ $\\left(\\dfrac{15}{6}\\right)^{2}$',
        '• ก่อนตอบให้ชี้นิ้วอ่านอีกครั้งว่าใครอยู่เศษใครอยู่ส่วน · '
        'ข้อนี้ถาม $\\dfrac{s_B}{s_A}$ โดย $B$ เป็นวงใหญ่และอยู่ข้างบน '
        'คำตอบจึงต้องมากกว่า $1$ ⇒ ถ้าคำนวณแล้วได้ค่าน้อยกว่า $1$ แสดงว่าเขียนกลับหัวแน่นอน',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\dfrac{2}{5}$ เพราะเขียนอัตราส่วนกลับหัว คือคำนวณ '
        '$\\dfrac{s_A}{s_B} = \\dfrac{6\\theta}{15\\theta} = \\dfrac{2}{5}$ '
        'ทั้งที่โจทย์ถาม $\\dfrac{s_B}{s_A}$ · ค่านี้ผิดแน่นอนโดยไม่ต้องคำนวณอะไรเลย '
        'เพราะมุมทั้งสองเท่ากันแต่วงของส่วนโค้ง $B$ ใหญ่กว่า ⇒ $s_B$ ต้องยาวกว่า $s_A$ '
        '⇒ อัตราส่วนที่มี $s_B$ อยู่เศษต้องมากกว่า $1$ แต่ $\\dfrac{2}{5} = 0.4$ ซึ่งน้อยกว่า $1$ · '
        'สังเกตว่า $\\dfrac{2}{5}$ กับ $\\dfrac{5}{2}$ เป็นส่วนกลับของกันและกันพอดี ยืนยันว่าพลาดที่การวางเศษ-ส่วน',
        '• ได้ค่า $\\dfrac{25}{4}$ เพราะคิดว่าความยาวส่วนโค้งแปรผันตาม<b>กำลังสอง</b>ของรัศมี '
        'จึงคำนวณ $\\left(\\dfrac{15}{6}\\right)^{2} = \\dfrac{225}{36} = \\dfrac{25}{4} = 6.25$ '
        '(เป็นการหยิบพฤติกรรมของ<b>พื้นที่</b>มาใช้กับความยาว) · ค่านี้ผิดจริง พิสูจน์ด้วยการแทนมุมลงไป : '
        'ให้ $\\theta = \\dfrac{\\pi}{3}$ จะได้ $s_A = 2\\pi$ และ $s_B = 5\\pi$ '
        '⇒ อัตราส่วนจริงคือ $2.5$ ไม่ใช่ $6.25$ · '
        'ที่ $\\dfrac{25}{4}$ ถูกต้องคือกรณีถาม<b>พื้นที่</b>ของเซกเตอร์ เพราะ $A = \\dfrac{1}{2}r^{2}\\theta$ '
        'มี $r$ ยกกำลังสอง แต่ $s = r\\theta$ มี $r$ กำลังหนึ่งเท่านั้น',
        '• ได้ค่า $9$ เพราะไปหา<b>ผลต่าง</b>ของรัศมี $15 - 6 = 9$ แทนที่จะหาอัตราส่วน '
        '· ค่านี้ผิดสองชั้น : ชั้นแรก คำถามที่เขียนเป็นเศษส่วน $\\dfrac{s_B}{s_A}$ '
        'คือคำสั่งให้หาร ไม่ใช่ให้ลบ และผลหารของความยาวสองค่าต้องเป็นจำนวนล้วนที่ไม่มีหน่วย '
        'แต่ $9$ ที่ได้มายังติดหน่วยความยาวอยู่ · ชั้นที่สอง ผลต่างของความยาวส่วนโค้งจริง ๆ คือ '
        '$s_B - s_A = 15\\theta - 6\\theta = 9\\theta$ ซึ่งเปลี่ยนค่าไปเรื่อยตามขนาดมุม '
        'เช่น $\\theta = \\dfrac{\\pi}{3}$ ให้ $3\\pi$ แต่ $\\theta = \\dfrac{\\pi}{6}$ ให้ $\\dfrac{3\\pi}{2}$ '
        '⇒ ผลต่างไม่ใช่ค่าคงที่ จึงเป็นคำตอบของโจทย์ข้อนี้ไม่ได้ตั้งแต่ต้น',
        '• ได้ค่า $\\dfrac{3}{2}$ เพราะคิดผลต่างของรัศมีแล้วเทียบกับรัศมีวงเล็ก '
        'คือคำนวณ $\\dfrac{15 - 6}{6} = \\dfrac{9}{6} = \\dfrac{3}{2}$ · '
        'ค่านี้ไม่ได้ไร้ความหมายเสียทีเดียว มันคือ<b>ส่วนที่เกินมา</b> '
        'นั่นคือบอกว่า $s_B$ ยาวกว่า $s_A$ อยู่อีก $\\dfrac{3}{2}$ เท่าของ $s_A$ '
        'แต่สิ่งที่โจทย์ถามคือ $s_B$ เป็นกี่เท่าของ $s_A$ ซึ่งต้องนับตัว $s_A$ ก้อนเดิมรวมเข้าไปด้วย · '
        'ความสัมพันธ์ที่ถูกคือ $\\dfrac{s_B}{s_A} = 1 + \\dfrac{3}{2} = \\dfrac{5}{2}$ '
        '⇒ ค่าที่พลาดกับคำตอบจริงห่างกันพอดี $1$ ซึ่งเป็นลายเซ็นของความสับสนระหว่าง '
        '“เป็นกี่เท่า” กับ “มากกว่ากี่เท่า”',
    ],
    'V.mold: G = two circles handed over by their radii as the bare numbers 6 and 15, with one named arc '
    'riding on each circle and a single stated link between them, namely that the central angle each arc '
    'subtends inside its own circle has the same size, while that size is never given any numerical value '
    'anywhere in the statement / A = the value of the ratio s_B/s_A of the two arc lengths, asked as a '
    'free numeric response with no candidate values printed on the page / M = give the shared central '
    'angle a single name theta measured in radians, write each arc through the arc-length relation '
    's = r*theta, then divide the two expressions so that theta cancels and the arc ratio collapses onto '
    'the bare radius ratio 15/6, which reduces to 5/2. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 -> level: ง่าย. '
    'F = 1 because exactly one formula is in play, the arc-length relation s = r*theta for an angle '
    'measured in radians; no second identity is needed and none can substitute for it. C = 0 because the '
    'whole item stays inside subtopic 7.11 and never reaches out to a second subtopic, so there is no '
    'second key to join to the first. P = 1 because the work occupies a single arena: the two arcs are '
    'written down and divided in one move, and the closing arithmetic 15/6 = 5/2 is the tail of that same '
    'move rather than a fresh stage, which follows the q105 and q113 baseline where a final reduction '
    'does not buy a second point. T = 0 because the only condition that matters, the equality of the two '
    'central angles, is handed to the reader in plain words; nothing has to be discovered, no branch has '
    'to be rejected, and the cancellation of theta is a direct consequence of that stated equality rather '
    'than a hidden key that must be found first. L = 0 because the statement is symbolic in the sense of '
    'the L baseline: each arc is pinned to its own circle by name and radius, so the formula can be '
    'applied immediately and no figure has to be drawn before the work can start. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b20.py): with th declared positive, (15*th)/(6*th) simplifies to 5/2 exactly, and the '
    'stored answer string 5/2 was parsed as a rational and compared against that value rather than '
    'eyeballed. Every wrong road printed in the pitfalls block was computed by machine and not invented: '
    'the inverted reading (6*th)/(15*th) returns 2/5, the area-style squaring (15/6)**2 returns 25/4, the '
    'plain difference 15 - 6 returns 9, and the relative difference Rational(15-6,6) returns 3/2, which '
    'sympy also confirms sits exactly one unit below the true answer since 1 + 3/2 = 5/2. The independent '
    'route was machine checked separately in b20/w711/v130_131.py, which substitutes three concrete '
    'angles, theta = 1/3, theta = 4/3 and theta = pi/2, computes both arc lengths from scratch in each '
    'case and reports the ratio 5/2 all three times, so the claim that the answer does not depend on the '
    'angle rests on computation rather than on assertion. '
    'Collision sweep on 6417 items (bank 63 files + k1 out + k2 out), probe collide_b20.py / '
    'collide_b20b.py: the pair (two separate circles of different radii) crossed with (central angles of '
    'equal size) returns zero items in the whole corpus. The nearest neighbour by answer label is q119 of '
    'the previous batch, which also carries A-ARC-RATIO, but its G is one sector rescaled under a fixed '
    'area and its M runs through an area invariant, so there the radius ratio is something to be derived '
    'rather than the answer itself; the nearest neighbour by shape is gen-chap-07-q032, a pair of '
    'concentric circles sharing one centre, whose mechanism is the difference of two sectors. Neither '
    'reuses this mechanism, in which the angle is deliberately left unmeasured precisely so that it '
    'cancels. Since this is a fill item there is no choice list, so no answer slot exists and nothing '
    'about the answer could have been positioned by hand.',
)

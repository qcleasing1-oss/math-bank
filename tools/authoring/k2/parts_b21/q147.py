# -*- coding: utf-8 -*-
add_fill(
    147,
    ['7.1'],
    'ปานกลาง',
    'รูปสี่เหลี่ยมคางหมู $ABCD$ มีด้าน $AB$ ขนานกับด้าน $DC$ '
    'โดยมุม $D\\hat{A}B$ และมุม $A\\hat{D}C$ เป็นมุมฉาก ถ้าด้าน $AB$ ยาว $9$ หน่วย '
    'ด้าน $DC$ ยาว $24$ หน่วย และด้าน $AD$ ยาว $8$ หน่วย '
    'แล้วค่าของ $\\cos(B\\hat{C}D)$ เท่ากับเท่าใด',
    '15/17',
    ['15/17', '\\dfrac{15}{17}'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• รูปสี่เหลี่ยมคางหมูคือรูปสี่เหลี่ยมที่มีด้านขนานกันหนึ่งคู่ · '
        'ถ้ามุมภายในสองมุมที่อยู่ปลายทั้งสองข้างของด้านที่ไม่ขนานด้านหนึ่งเป็นมุมฉากทั้งคู่ '
        'ด้านที่ไม่ขนานด้านนั้นจะตั้งฉากกับด้านคู่ขนาน<b>ทั้งสองเส้น</b>พร้อมกัน '
        'เพราะเส้นตรงที่ตั้งฉากกับเส้นหนึ่ง ย่อมตั้งฉากกับทุกเส้นที่ขนานกับเส้นนั้นด้วย '
        '⇒ ด้านนั้นทำหน้าที่เป็นความสูงของรูปได้ทันที ไม่ต้องไปหาความสูงจากที่อื่น',
        '• อัตราส่วนตรีโกณมิติของมุมแหลมใช้ได้เฉพาะใน<b>สามเหลี่ยมมุมฉาก</b>เท่านั้น โดย '
        '$\\cos$ ของมุมแหลมมุมหนึ่ง เท่ากับ ความยาวด้านประชิดมุมนั้น หารด้วย ความยาวด้านตรงข้ามมุมฉาก '
        'และ $\\sin$ ของมุมเดียวกัน เท่ากับ ความยาวด้านตรงข้ามมุมนั้น หารด้วย ความยาวด้านตรงข้ามมุมฉาก '
        '⛔ ถ้าสามเหลี่ยมที่มองอยู่ยังไม่มีมุมฉาก จะอ่านค่าแบบนี้ไม่ได้เลย '
        'ต้องสร้างมุมฉากขึ้นมาก่อนเสมอ',
        '• เหตุผลที่อ่านค่าแบบนี้ได้ : สามเหลี่ยมมุมฉากสองรูปที่มีมุมแหลมเท่ากันย่อมคล้ายกัน '
        '⇒ อัตราส่วนของด้านคู่ที่สมนัยกันมีค่าคงที่เสมอ ไม่ว่ารูปจะวาดใหญ่หรือเล็ก '
        'ค่าที่อ่านได้จึงขึ้นกับ<b>ขนาดของมุม</b>เพียงอย่างเดียว ไม่ขึ้นกับขนาดของรูป',
        '• ทฤษฎีบทพีทาโกรัส : ในสามเหลี่ยมมุมฉาก กำลังสองของด้านตรงข้ามมุมฉาก '
        'เท่ากับผลบวกของกำลังสองของด้านประกอบมุมฉากทั้งสองด้าน · '
        'ชุดตัวเลขที่ควรจำเพราะพบบ่อยคือ $8$-$15$-$17$ ซึ่งตรวจได้จริงว่า '
        '$8^{2}+15^{2} = 64+225 = 289 = 17^{2}$',
        '• รูปสี่เหลี่ยมที่มีมุมฉากครบสามมุม มุมที่สี่ต้องเป็นมุมฉากด้วยเสมอ '
        'เพราะผลบวกของมุมภายในรูปสี่เหลี่ยมเท่ากับ $360^{\\circ}$ ⇒ รูปนั้นเป็นรูปสี่เหลี่ยมมุมฉาก '
        'และรูปสี่เหลี่ยมมุมฉากมีด้านตรงข้ามยาวเท่ากันเป็นคู่ ๆ · '
        'สมบัตินี้เองที่ทำให้เรา “ย้ายความยาว” จากด้านหนึ่งไปอ่านที่อีกด้านหนึ่งได้',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• รูปสี่เหลี่ยมคางหมู $ABCD$ มีด้าน $AB$ ขนานกับด้าน $DC$',
        '• มุมที่จุด $A$ คือมุม $D\\hat{A}B$ และมุมที่จุด $D$ คือมุม $A\\hat{D}C$ เป็นมุมฉากทั้งคู่ '
        '⇒ ด้าน $AD$ ตั้งฉากกับทั้งด้าน $AB$ และด้าน $DC$',
        '• ความยาวที่ให้มาครบสามค่า : $AB = 9$ หน่วย · $DC = 24$ หน่วย · $AD = 8$ หน่วย',
        '• วิธีวาดตามคำบรรยาย (วาดเองได้เลยด้วยไม้บรรทัด) : ลากส่วนของเส้นตรงแนวนอนยาว $24$ หน่วย '
        'ให้ปลายซ้ายเป็นจุด $D$ และปลายขวาเป็นจุด $C$ · จากจุด $D$ ลากขึ้นในแนวตั้งฉากยาว $8$ หน่วย '
        'ปลายบนคือจุด $A$ · จากจุด $A$ ลากไปทางขวาในแนวขนานกับ $DC$ ยาว $9$ หน่วย ปลายคือจุด $B$ · '
        'สุดท้ายลากส่วนของเส้นตรงเชื่อมจุด $B$ กับจุด $C$ ⇒ ได้รูปที่ตรงตามเงื่อนไขของโจทย์ครบทุกข้อ',
        '• สังเกตหน้าตาก่อนลงมือ : มุม $B\\hat{C}D$ เป็นมุมที่จุด $C$ ซึ่งอยู่ระหว่างด้าน $CB$ กับด้าน $CD$ '
        'และมุมนี้<b>ยังไม่ได้อยู่ในสามเหลี่ยมมุมฉากรูปใดเลย</b> ⇒ อ่านค่า $\\cos$ ทันทีไม่ได้ '
        'ต้องลากเส้นช่วยสร้างมุมฉากขึ้นมาก่อน',
        '• สังเกตอีกอย่าง : ด้านคู่ขนานยาวไม่เท่ากัน ($24$ หน่วย กับ $9$ หน่วย) '
        'ส่วนที่ฐานล่างยื่นเกินฐานบนออกมาคือ $24 - 9 = 15$ หน่วย '
        '⇒ ตัวเลข $15$ นี้แหละที่จะกลายเป็นด้านหนึ่งของสามเหลี่ยมที่เรากำลังจะสร้าง',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\cos(B\\hat{C}D)$ ซึ่งเป็นค่าโคไซน์ของมุมภายในที่จุด $C$ ของรูปสี่เหลี่ยมคางหมูรูปนี้',
        '',
        '<b>【 ลากเส้นตั้งฉากจากจุด $B$ ลงมาตัดด้าน $DC$ ที่จุด $E$ '
        'เพื่อหั่นรูปคางหมูออกเป็นรูปสี่เหลี่ยมมุมฉาก $ABED$ กับรูปสามเหลี่ยมมุมฉาก $BEC$ '
        'แล้วย้ายความยาวสองด้านออกมาจากด้านตรงข้ามของรูปสี่เหลี่ยมมุมฉากนั้น '
        'หาด้านที่สามของสามเหลี่ยมด้วยทฤษฎีบทพีทาโกรัส '
        'จากนั้นอ่านค่าโคไซน์ที่จุด $C$ จากสามเหลี่ยมมุมฉากรูปนั้นตรง ๆ 】</b>',
        '',
        '<b>ขั้นที่ 1 · ลากเส้นตั้งฉากจากจุด $B$ ลงมาที่ฐาน $DC$ แล้วยืนยันว่าได้รูปสี่เหลี่ยมมุมฉาก</b>',
        '• สิ่งที่ทำ : จากจุด $B$ ลากส่วนของเส้นตรงตั้งฉากลงมาตัดด้าน $DC$ '
        'เรียกจุดตัดที่เกิดขึ้นว่าจุด $E$ ⇒ รูปคางหมูถูกหั่นออกเป็นสองชิ้น คือ $ABED$ กับ $BEC$',
        '• เหตุผลที่ชิ้นซ้ายเป็นรูปสี่เหลี่ยมมุมฉาก : ในรูปสี่เหลี่ยม $ABED$ '
        'มุมที่จุด $A$ เป็นมุมฉาก (โจทย์ให้มา) · มุมที่จุด $D$ เป็นมุมฉาก (โจทย์ให้มา) · '
        'มุมที่จุด $E$ เป็นมุมฉาก (เพราะเราเพิ่งลาก $BE$ ให้ตั้งฉากกับ $DC$) '
        '⇒ มีมุมฉากครบสามมุม มุมที่จุด $B$ จึงต้องเป็นมุมฉากด้วย ⇒ $ABED$ เป็นรูปสี่เหลี่ยมมุมฉาก',
        '• ใช้สมบัติด้านตรงข้ามของรูปสี่เหลี่ยมมุมฉากยาวเท่ากัน เพื่อย้ายความยาวสองค่า : '
        '$DE = AB = 9$ หน่วย และ $BE = AD = 8$ หน่วย '
        '⇒ ตอนนี้เรารู้ความสูงของรูปแล้วว่าเท่ากับ $8$ หน่วย',
        '• ⛔ จุดที่ต้องตรวจก่อนเดินต่อ : จุด $E$ ต้องตกลงมาอยู่<b>ระหว่าง</b>จุด $D$ กับจุด $C$ จริง ๆ '
        'ตรวจได้ว่า $DE = 9$ ซึ่งน้อยกว่า $DC = 24$ ⇒ จุด $E$ อยู่บนด้าน $DC$ แน่นอน ไม่เลยจุด $C$ ออกไป',
        '',
        '<b>ขั้นที่ 2 · หาความยาว $EC$ ซึ่งเป็นด้านที่ประชิดมุมที่จุด $C$</b>',
        '• ความสัมพันธ์ที่ใช้ : เมื่อจุด $E$ อยู่ระหว่างจุด $D$ กับจุด $C$ จะได้ $DE + EC = DC$ '
        'จัดรูปเป็น $EC = DC - DE$',
        '• ระบุตัวแปรก่อนแทนค่า : $DC = 24$ หน่วย (โจทย์ให้มา) และ $DE = 9$ หน่วย (ย้ายมาจากขั้นที่ $1$)',
        '• แทนค่า : $EC = 24 - 9 = 15$ หน่วย',
        '• 📌 อ่านความหมายให้ออก : $15$ คือส่วนที่ฐานล่างยาวเกินฐานบนออกมา '
        'และเพราะรูปนี้มีมุมฉากอยู่ฝั่ง $A$ กับ $D$ ทั้งคู่ ส่วนเกินทั้งก้อนจึงไปกองอยู่ฝั่งขวาฝั่งเดียว '
        '⛔ ไม่ได้ถูกแบ่งครึ่งไปสองข้างเหมือนคางหมูหน้าจั่ว',
        '',
        '<b>ขั้นที่ 3 · หาความยาว $BC$ ด้วยทฤษฎีบทพีทาโกรัส</b>',
        '• สามเหลี่ยม $BEC$ มีมุมฉากอยู่ที่จุด $E$ เพราะ $BE$ ตั้งฉากกับ $DC$ '
        '⇒ ด้าน $BC$ ที่อยู่ตรงข้ามมุมฉากคือด้านตรงข้ามมุมฉากของสามเหลี่ยมรูปนี้',
        '• สูตรที่ใช้ : $BC^{2} = BE^{2} + EC^{2}$',
        '• ระบุตัวแปร : $BE = 8$ หน่วย (จากขั้นที่ $1$) และ $EC = 15$ หน่วย (จากขั้นที่ $2$)',
        '• แทนค่า : $BC^{2} = 8^{2} + 15^{2} = 64 + 225 = 289$',
        '• ยุบ : $BC = \\sqrt{289} = 17$ หน่วย ⇒ เลือกรากบวกเพราะเป็นความยาวด้าน '
        '· สังเกตว่าได้สามเหลี่ยมชุด $8$-$15$-$17$ พอดี',
        '',
        '<b>ขั้นที่ 4 · อ่านค่าโคไซน์ที่จุด $C$ จากสามเหลี่ยม $BEC$</b>',
        '• ก่อนอื่นต้องยืนยันว่ามุมสองมุมนี้คือมุมเดียวกัน : มุม $B\\hat{C}D$ คือมุมระหว่างรังสี $CB$ กับรังสี $CD$ '
        'และเพราะจุด $E$ อยู่บนส่วนของเส้นตรง $DC$ ระหว่าง $D$ กับ $C$ '
        'รังสี $CD$ กับรังสี $CE$ จึงเป็นรังสีเดียวกัน ⇒ มุม $B\\hat{C}D$ กับมุม $B\\hat{C}E$ คือมุมเดียวกันแน่นอน',
        '• จัดตำแหน่งด้านให้ถูก เมื่อยืนมองจากมุมที่จุด $C$ ในสามเหลี่ยมมุมฉาก $BEC$ : '
        'ด้านประชิดมุมคือ $EC$ · ด้านตรงข้ามมุมคือ $BE$ · ด้านตรงข้ามมุมฉากคือ $BC$',
        '• สูตรที่ใช้ : $\\cos(B\\hat{C}D) = \\dfrac{EC}{BC}$ '
        '⛔ ตัวส่วนต้องเป็นด้านตรงข้ามมุมฉากเสมอ ห้ามหยิบด้านอื่นมาเป็นตัวส่วน',
        '• แทนค่า : $\\cos(B\\hat{C}D) = \\dfrac{15}{17}$',
        '• ตรวจความสมเหตุสมผลทันที : $\\dfrac{15}{17} \\approx 0.882$ ซึ่งอยู่ระหว่าง $0$ กับ $1$ '
        'ตรงตามที่โคไซน์ของมุมแหลมต้องเป็น · และค่าที่เข้าใกล้ $1$ ขนาดนี้บอกว่ามุมที่จุด $C$ แคบมาก '
        '(ประมาณ $28^{\\circ}$) ซึ่งเข้ากับรูปที่วาดไว้ เพราะฐานยื่นออกไปตั้ง $15$ หน่วย แต่สูงขึ้นแค่ $8$ หน่วย',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · วางระบบพิกัดฉากแล้วใช้ผลคูณเชิงสเกลาร์ของเวกเตอร์สองเส้นที่ออกจากจุดยอดเดียวกัน)</b>',
        '• เส้นทางแรกได้คำตอบมาจากการหั่นรูปแล้วอ่านอัตราส่วนของด้าน ⇒ วิธีตรวจที่ไม่ซ้ำทางเดิม '
        'คือทิ้งการหั่นรูปทั้งหมด แล้วเปลี่ยนทุกจุดให้เป็นคู่อันดับบนระบบพิกัดฉาก คิดด้วยพีชคณิตล้วน',
        '• วางจุดตามเงื่อนไขของโจทย์ : $D$ อยู่ที่ $(0, 0)$ · $C$ อยู่ที่ $(24, 0)$ · $A$ อยู่ที่ $(0, 8)$ · '
        '$B$ อยู่ที่ $(9, 8)$ · การวางแบบนี้ถูกต้องครบทุกเงื่อนไข เพราะ $AD$ อยู่ในแนวตั้งจึงตั้งฉากกับ $DC$ '
        'ที่อยู่ในแนวนอน (มุมที่ $D$ เป็นมุมฉาก) · $AB$ อยู่ในแนวนอนจึงขนานกับ $DC$ และตั้งฉากกับ $AD$ '
        '(มุมที่ $A$ เป็นมุมฉาก) · ส่วนความยาวก็ครบ คือ $AB = 9$ หน่วย, $DC = 24$ หน่วย และ $AD = 8$ หน่วย',
        '• เขียนเวกเตอร์สองเส้นที่ออกจากจุด $C$ ไปตามแขนทั้งสองของมุมที่ต้องการ : '
        '$\\vec{CB} = (9 - 24, 8 - 0) = (-15, 8)$ และ $\\vec{CD} = (0 - 24, 0 - 0) = (-24, 0)$',
        '• หาขนาดของเวกเตอร์ทั้งสอง : $|\\vec{CB}| = \\sqrt{(-15)^{2} + 8^{2}} = \\sqrt{289} = 17$ '
        'และ $|\\vec{CD}| = 24$',
        '• ใช้สูตรผลคูณเชิงสเกลาร์ $\\vec{u} \\cdot \\vec{v} = |\\vec{u}| \\, |\\vec{v}| \\cos\\theta$ '
        'จัดรูปเป็น $\\cos\\theta = \\dfrac{\\vec{u} \\cdot \\vec{v}}{|\\vec{u}| \\, |\\vec{v}|}$ ⇒ '
        '$\\cos(B\\hat{C}D) = \\dfrac{(-15)(-24) + (8)(0)}{17 \\times 24} = \\dfrac{360}{408} = \\dfrac{15}{17}$ ✓ '
        'ตรงกับเส้นทางแรกทั้งที่ไม่ได้ลากเส้นตั้งฉากช่วยเลยแม้แต่เส้นเดียว',
        '• 📌 ตรวจซ้ำอีกชั้นด้วยเอกลักษณ์พีทาโกรัส : จากสามเหลี่ยม $BEC$ จะได้ '
        '$\\sin(B\\hat{C}D) = \\dfrac{BE}{BC} = \\dfrac{8}{17}$ ⇒ '
        '$\\left(\\dfrac{15}{17}\\right)^{2} + \\left(\\dfrac{8}{17}\\right)^{2} = '
        '\\dfrac{225 + 64}{289} = \\dfrac{289}{289} = 1$ ✓ '
        'ซึ่งตรงกับเอกลักษณ์ $\\sin^{2}\\theta + \\cos^{2}\\theta = 1$ ⇒ ยืนยันว่าคู่ค่านี้มาจากมุมเดียวกันจริง',
        '',
        '✅ <b>คำตอบ</b> ค่าของ $\\cos(B\\hat{C}D)$ เท่ากับ $\\dfrac{15}{17}$ '
        'ซึ่งเป็นอัตราส่วนของความยาวสองด้าน จึงเป็นจำนวนล้วนที่ไม่มีหน่วย',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอรูปคางหมูที่มีมุมฉากสองมุมติดกัน แล้วโจทย์ถามอัตราส่วนตรีโกณของมุมอีกฝั่งหนึ่ง '
        'ให้ลากเส้นตั้งฉากจากปลายของฐานสั้นลงมาที่ฐานยาวเป็นอันดับแรกเสมอ · '
        'เส้นเดียวนี้เปลี่ยนรูปที่ใช้สูตรไม่ได้ ให้กลายเป็นรูปสี่เหลี่ยมมุมฉากที่ใช้ย้ายความยาว '
        'บวกกับสามเหลี่ยมมุมฉากที่ใช้อ่านอัตราส่วนได้ทันที',
        '• จำชุดสามเหลี่ยมมุมฉากที่มีด้านเป็นจำนวนเต็มไว้ให้ขึ้นใจ : $3$-$4$-$5$ · $5$-$12$-$13$ · '
        '$8$-$15$-$17$ · $7$-$24$-$25$ · $9$-$40$-$41$ ⇒ เห็นด้านประกอบมุมฉากสองด้านเมื่อไร '
        'จะเดาด้านตรงข้ามมุมฉากได้ในหัวทันที แล้วค่อยตรวจด้วยพีทาโกรัสอีกครั้งให้แน่ใจ',
        '• ก่อนเขียนคำตอบลงกระดาษ ให้ถามตัวเองสองคำถามเสมอ : มุมที่ถามเป็นมุมแหลมหรือไม่ '
        'และค่าที่ได้อยู่ระหว่าง $0$ กับ $1$ หรือไม่ · ถ้ามุมเป็นมุมแหลมแต่ค่าที่ได้เกิน $1$ '
        'แปลว่าเขียนเศษส่วนกลับหัวแน่นอน ⇒ จับผิดตัวเองได้ก่อนส่งกระดาษ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\dfrac{8}{17}$ เพราะเผลอหยิบด้าน $BE$ ซึ่งเป็นด้าน<b>ตรงข้าม</b>มุมที่จุด $C$ '
        'มาวางเป็นตัวเศษ · ค่านี้คือ $\\sin(B\\hat{C}D)$ ไม่ใช่ $\\cos(B\\hat{C}D)$ · '
        'พิสูจน์ว่าผิดจริง : มุมที่มีโคไซน์เท่ากับ $\\dfrac{8}{17}$ จะกางประมาณ $62^{\\circ}$ '
        'แต่มุมที่จุด $C$ ของรูปนี้กางเพียงประมาณ $28^{\\circ}$ '
        '(ดูจากฐานที่ยื่นออกไป $15$ หน่วย เทียบกับความสูงเพียง $8$ หน่วย ซึ่งเป็นมุมที่แบนมาก) '
        '⇒ คนละมุมกันชัดเจน · วิธีกันพลาดคือท่องว่าโคไซน์คู่กับด้าน “ประชิด” เสมอ',
        '• ได้ค่า $\\dfrac{17}{15}$ เพราะเขียนเศษส่วนกลับหัว เอาด้านตรงข้ามมุมฉากขึ้นไปเป็นตัวเศษ · '
        'ค่านี้คือ $\\sec(B\\hat{C}D)$ ซึ่งเป็นส่วนกลับของคำตอบจริง · พิสูจน์ว่าผิดจริงโดยไม่ต้องคำนวณเลย : '
        '$\\dfrac{17}{15} \\approx 1.13$ ซึ่งมากกว่า $1$ แต่ในสามเหลี่ยมมุมฉาก '
        'ด้านตรงข้ามมุมฉากยาวที่สุดเสมอ ตัวเศษของโคไซน์จึงเล็กกว่าตัวส่วนเสมอ '
        '⇒ ค่าโคไซน์ของมุมแหลมต้องอยู่ระหว่าง $0$ กับ $1$ เท่านั้น เกิน $1$ เมื่อไรคือผิดทันที',
        '• ได้ค่า $\\dfrac{5}{8}$ เพราะเอา $EC = 15$ ไปหารด้วย $DC = 24$ ซึ่งเป็นฐานทั้งเส้นของคางหมู '
        'แทนที่จะหารด้วยด้านตรงข้ามมุมฉาก $BC = 17$ ⇒ $\\dfrac{15}{24} = \\dfrac{5}{8}$ · '
        'ที่ผิดเพราะ $DC$ ไม่ได้เป็นด้านของสามเหลี่ยมมุมฉาก $BEC$ เลยแม้แต่ด้านเดียว '
        'มันยาวเลยจุด $E$ ออกไปทางซ้ายอีก $9$ หน่วย · พิสูจน์ด้วยตัวเลข : '
        'มุมที่มีโคไซน์เท่ากับ $\\dfrac{5}{8} = 0.625$ จะกางประมาณ $51^{\\circ}$ '
        'ซึ่งไม่ใช่มุมที่จุด $C$ ที่กางประมาณ $28^{\\circ}$',
        '• ได้ค่าติดลบ $-\\dfrac{15}{17}$ เพราะคำนวณส่วนเกินของฐานกลับด้านเป็น $AB - DC = 9 - 24 = -15$ '
        'แล้วลากเครื่องหมายลบติดไปจนถึงคำตอบ · ที่ผิดเห็นได้ตั้งแต่บรรทัดแรก : '
        'ผลลบที่ออกมาถูกใช้เป็น<b>ความยาวด้าน</b>ของสามเหลี่ยม ซึ่งเป็นจำนวนลบไม่ได้เด็ดขาด '
        '⇒ ต้องเอาฐานยาวตั้ง แล้วลบฐานสั้นออก คือ $DC - AB$ เสมอ · '
        'อีกชั้นหนึ่ง มุมที่จุด $C$ เป็นมุมแหลม โคไซน์ของมุมแหลมเป็นบวกเสมอ '
        'ค่าติดลบจึงเป็นไปไม่ได้ตั้งแต่ต้น',
    ],
    'V.mold: G = a right trapezoid ABCD handed over in words alone, with AB parallel to DC, the interior '
    'angles at A and at D both declared right angles, and three lengths given as bare numbers, AB = 9, '
    'DC = 24 and AD = 8, so the reader has to build the picture from the sentence before any formula can '
    'be applied / A = the value of the cosine of the interior angle at C, written cos(BCD), asked as a '
    'free numeric response with no candidate values printed anywhere on the page / M = drop the single '
    'perpendicular from B onto DC and call its foot E, recognise ABED as a rectangle because three of its '
    'angles are right, carry DE = AB = 9 and BE = AD = 8 across from that rectangle, subtract to get '
    'EC = 24 - 9 = 15, close the right triangle BEC with the Pythagorean theorem to get BC = 17, and read '
    'the cosine at C off that triangle as EC/BC = 15/17. '
    'Rubric F2 C1 P2 T1 L1 = 7/15 -> level: ปานกลาง. '
    'F = 2 because two separate results are needed and neither can stand in for the other: the Pythagorean '
    'theorem to produce the hypotenuse of triangle BEC, and the definition of the cosine ratio in a right '
    'triangle to turn two side lengths into the requested number; the rectangle property that opposite '
    'sides are equal is used too, but it is a fact about the figure rather than a third formula to recall. '
    'C = 1 because the item joins one geometric key, the auxiliary perpendicular that splits the trapezoid '
    'into a rectangle plus a right triangle, to one trigonometric key, and the second key cannot be '
    'applied until the first has produced the two legs; it is not 2 because both keys live inside subtopic '
    '7.1 and no result from any other subtopic is imported. P = 2 because the work runs through two '
    'distinct arenas, first the reconstruction of DE, BE and EC from the rectangle, then the hypotenuse '
    'and the ratio; it is not 3 because each arena is a single line of arithmetic and nothing has to be '
    'carried across a case split. T = 1 because there is exactly one place to fall, namely which leg of '
    'triangle BEC is adjacent to the angle at C, plus the small step of noticing that ray CD and ray CE '
    'are the same ray so the angle inside the triangle really is the angle asked about; it is not 2 '
    'because no condition is hidden and no candidate has to be rejected. L = 1 because the figure is '
    'described in words only and has to be drawn before the work can start, which is exactly the L = 1 '
    'line of the batch brief; it is not 2 because everything stays inside one plane. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): the q147 block sets EC = 24 - 9 and BC = sqrt(EC**2 + 8**2), checks BC against '
    '17 exactly, and compares Rational(15,17) against the stored key by parsing the key string 15/17 as a '
    'rational rather than by eye. Both printed wrong roads were computed by machine and not invented: '
    'Rational(8,17) is what taking the opposite leg produces, and Rational(15,24) reduces to 5/8, which is '
    'what dividing by the whole base DC instead of by the hypotenuse produces. The independent route was '
    'checked in the same spirit: with D at (0,0), C at (24,0), A at (0,8) and B at (9,8) the vectors '
    'CB = (-15,8) and CD = (-24,0) give a dot product of 360 and magnitudes 17 and 24, so the cosine is '
    '360/408, which reduces to 15/17 and agrees with the synthetic route. The Pythagorean identity was '
    'evaluated as well, (15/17)**2 + (8/17)**2 = 289/289 = 1, and the three angles quoted in the pitfalls '
    'were obtained by machine from the arccosine: 15/17 gives about 28.07 degrees, 8/17 gives about 61.93 '
    'degrees and 5/8 gives about 51.32 degrees, so each rejected value is shown to belong to a different '
    'angle rather than merely asserted to be wrong. '
    'Collision sweep on 6457 items (bank 63 files + k1 out + k2 out), probe run over question text only so '
    'that the first gate never reads an explanation: the Thai word for trapezoid appears in exactly 3 '
    'items across the whole corpus, and the pair (trapezoid) crossed with (right angle) returns 0 items, '
    'as does the pair (trapezoid) crossed with (cosine); the literal answer value 15/17 appears in no '
    'question in the corpus. The nearest neighbour is gen-chap-07-trigonometry-q112, which shares the '
    'surface G of a trapezoid ABCD with AB parallel to DC and even names the same angle BCD, but there the '
    'two base angles arrive as a sine value and as 45 degrees, the figure carries no right angle at all, '
    'its A is the area of the trapezoid and its M drops two altitudes and finishes with a tangent; here '
    'the trapezoid is right-angled, one perpendicular suffices, and the answer is a cosine, so G, A and M '
    'all differ. The other two hits, chap-05-function-q06 and pat1-2564-03-q34, sit in the function and '
    'the calculus chapters and use the shape only as a region under a graph. Since this is a fill item '
    'there is no choice list, so no answer slot exists and nothing about the answer could have been '
    'positioned by hand.',
)

# -*- coding: utf-8 -*-
add_fill(
    109,
    ['7.1', '7.6'],
    'ยาก',
    'รูปสามเหลี่ยม $ABC$ มีมุม $C$ เป็นมุมฉาก ด้าน $AC$ ยาว $7$ หน่วย '
    'และด้าน $BC$ ยาว $24$ หน่วย ถ้า $AD$ เป็นเส้นแบ่งครึ่งมุม $A$ '
    'โดยจุด $D$ อยู่บนด้าน $BC$ แล้ว $AD$ ยาวกี่หน่วย',
    '35/4',
    ['35/4', '8.75', '\\dfrac{35}{4}'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ในรูปสามเหลี่ยมมุมฉาก ด้านที่อยู่ตรงข้ามมุมฉากคือด้านที่ยาวกว่าอีกสองด้านเสมอ '
        'และความยาวทั้งสามผูกกันด้วยทฤษฎีบทพีทาโกรัส คือ '
        '(ด้านประกอบมุมฉากตัวที่หนึ่ง)$^2$ + (ด้านประกอบมุมฉากตัวที่สอง)$^2$ = (ด้านตรงข้ามมุมฉาก)$^2$ '
        'ผลที่ตามมาซึ่งจะได้ใช้ตรวจคำตอบคือ ด้านตรงข้ามมุมฉากต้องยาวกว่าด้านประกอบมุมฉากทุกด้านเสมอ',
        '• อัตราส่วนตรีโกณมิติของมุมแหลมในรูปสามเหลี่ยมมุมฉาก อ่านจากตำแหน่งของด้านเทียบกับมุมที่สนใจ : '
        '$\\sin = \\dfrac{\\text{ด้านตรงข้าม}}{\\text{ด้านตรงข้ามมุมฉาก}}$ · '
        '$\\cos = \\dfrac{\\text{ด้านประชิด}}{\\text{ด้านตรงข้ามมุมฉาก}}$ · '
        '$\\tan = \\dfrac{\\text{ด้านตรงข้าม}}{\\text{ด้านประชิด}}$ '
        'เหตุที่อ่านแบบนี้ได้เพราะรูปสามเหลี่ยมมุมฉากที่มีมุมแหลมเท่ากันย่อมคล้ายกัน อัตราส่วนของด้านจึงคงที่',
        '• เส้นแบ่งครึ่งมุม $A$ คือรังสีที่ออกจากจุดยอด $A$ แล้วผ่าซีกมุม $A$ ออกเป็นสองมุมที่เท่ากันพอดี '
        'มุมย่อยแต่ละมุมจึงมีขนาด $\\dfrac{A}{2}$ · เมื่อปลายอีกข้างของเส้นนี้ไปหยุดที่จุด $D$ บนด้าน $BC$ '
        'รูปสามเหลี่ยม $ACD$ ที่เกิดขึ้นจะยังมีมุมฉากอยู่ที่ $C$ เหมือนเดิม เพราะ $D$ อยู่บนเส้นตรงเดียวกับ $BC$ '
        'เราจึงมีรูปสามเหลี่ยมมุมฉากรูปเล็กซ้อนอยู่ในรูปใหญ่ โดยใช้ด้าน $AC$ ร่วมกัน',
        '• ⛔ กับดักใหญ่ที่สุดของข้อนี้ : $\\tan\\dfrac{A}{2} \\ne \\dfrac{1}{2}\\tan A$ '
        'เพราะ $\\tan$ ไม่ใช่ฟังก์ชันที่ครึ่งมุมแล้วค่าจะเหลือครึ่งตาม ลองแทน $A = 60^{\\circ}$ ดูก็เห็นทันที : '
        '$\\tan 60^{\\circ} = \\sqrt{3} \\approx 1.732$ ครึ่งหนึ่งของมันคือ $0.866$ '
        'แต่ $\\tan 30^{\\circ} = \\dfrac{1}{\\sqrt{3}} \\approx 0.577$ ซึ่งไม่ใช่ค่าเดียวกันเลย '
        'สูตรที่ถูกต้องคือ $\\tan\\dfrac{A}{2} = \\dfrac{1 - \\cos A}{\\sin A}$',
        '• ที่มาของสูตรครึ่งมุมข้างบน มาจากสูตรมุมสองเท่าสองบรรทัด คือ '
        '$\\sin A = 2\\sin\\dfrac{A}{2}\\cos\\dfrac{A}{2}$ และ $\\cos A = 1 - 2\\sin^{2}\\dfrac{A}{2}$ '
        'บรรทัดหลังจัดรูปได้เป็น $1 - \\cos A = 2\\sin^{2}\\dfrac{A}{2}$ '
        'เมื่อนำมาหารกันจะได้ $\\dfrac{1 - \\cos A}{\\sin A} = '
        '\\dfrac{2\\sin^{2}\\dfrac{A}{2}}{2\\sin\\dfrac{A}{2}\\cos\\dfrac{A}{2}} = '
        '\\dfrac{\\sin\\dfrac{A}{2}}{\\cos\\dfrac{A}{2}} = \\tan\\dfrac{A}{2}$ '
        'จำที่มานี้ไว้จะไม่หลงไปหารสองมั่ว ๆ',
        '• คู่หูอีกสูตรที่จะได้ใช้ตอนตรวจคำตอบคือ $\\cos A = 2\\cos^{2}\\dfrac{A}{2} - 1$ '
        'ย้ายข้างได้ $\\cos\\dfrac{A}{2} = \\sqrt{\\dfrac{1 + \\cos A}{2}}$ '
        'ที่เลือกรากบวกได้เพราะในรูปสามเหลี่ยมมุมฉาก มุม $A$ เป็นมุมแหลม '
        'ดังนั้น $\\dfrac{A}{2}$ ก็เป็นมุมแหลมด้วย และโคไซน์ของมุมแหลมเป็นบวกเสมอ',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• รูปสามเหลี่ยม $ABC$ มีมุม $C$ เป็นมุมฉาก ⇒ ด้าน $AC$ กับด้าน $BC$ เป็นด้านประกอบมุมฉาก '
        'ส่วน $AB$ เป็นด้านตรงข้ามมุมฉาก',
        '• ด้าน $AC$ ยาว $7$ หน่วย และด้าน $BC$ ยาว $24$ หน่วย',
        '• $AD$ เป็นเส้นแบ่งครึ่งมุม $A$ โดยจุด $D$ อยู่บนด้าน $BC$ '
        '⇒ มุม $D\\hat{A}C$ มีขนาดเท่ากับ $\\dfrac{A}{2}$ พอดี',
        '• สังเกตหน้าตาก่อนลงมือ : เลข $7$ กับ $24$ เป็นด้านประกอบมุมฉากของสามชุดจำนวนพีทาโกรัสชุดคุ้นตา '
        '$7$-$24$-$25$ ⇒ เดาได้ตั้งแต่ยังไม่คิดว่า $AB$ จะออกมาเป็นจำนวนเต็มสวย ๆ '
        'และค่าของ $\\sin A$ กับ $\\cos A$ จะเป็นเศษส่วนที่มีตัวส่วนเป็น $25$ ทั้งคู่',
        '• สังเกตอีกอย่าง : มุมที่ต้องใช้ทำงานจริงคือ $\\dfrac{A}{2}$ ไม่ใช่ $A$ '
        'เพราะเส้นที่ถามคือเส้นแบ่งครึ่งมุม ⇒ ต้องมีขั้นแปลงจากมุมเต็มไปเป็นครึ่งมุมอย่างแน่นอน',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาความยาวของ $AD$ ซึ่งเป็นเส้นแบ่งครึ่งมุม $A$ ที่ลากจากจุด $A$ ไปหยุดที่จุด $D$ บนด้าน $BC$',
        '',
        '<b>【 เติมด้าน $AB$ ด้วยพีทาโกรัสเพื่ออ่าน $\\sin A$ กับ $\\cos A$ '
        'แล้วใช้สูตรครึ่งมุม $\\tan\\dfrac{A}{2} = \\dfrac{1 - \\cos A}{\\sin A}$ '
        'ไปหาความยาว $CD$ ในรูปสามเหลี่ยมมุมฉากรูปเล็ก $ACD$ '
        'สุดท้ายปิดงานด้วยพีทาโกรัสอีกครั้งเพื่อหา $AD$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · หาด้าน $AB$ แล้วอ่านค่า $\\sin A$ กับ $\\cos A$ ในสามเหลี่ยมใหญ่</b>',
        '• สูตรที่ใช้ : $AC^{2} + BC^{2} = AB^{2}$ ใช้ได้เพราะมุมที่ $C$ เป็นมุมฉาก '
        '⇒ ด้านที่อยู่ตรงข้ามกับ $C$ คือ $AB$ จึงเป็นด้านตรงข้ามมุมฉาก',
        '• ระบุตัวแปรก่อนแทนค่า : $AC = 7$ คือด้านประกอบมุมฉากด้านหนึ่ง · $BC = 24$ '
        'คือด้านประกอบมุมฉากอีกด้านหนึ่ง · $AB$ คือด้านตรงข้ามมุมฉากซึ่งยังไม่รู้ค่า',
        '• แทนค่า : $7^{2} + 24^{2} = AB^{2}$ ⇒ $49 + 576 = AB^{2}$ ⇒ $AB^{2} = 625$',
        '• ยุบ : $AB = \\sqrt{625} = 25$ หน่วย (เลือกรากบวกเพราะเป็นความยาวด้าน)',
        '• มุม $A$ อยู่ที่จุดยอด $A$ ⇒ ด้านตรงข้ามมุม $A$ คือ $BC = 24$ · ด้านประชิดมุม $A$ คือ $AC = 7$ '
        '· ด้านตรงข้ามมุมฉากคือ $AB = 25$',
        '• อ่านอัตราส่วนออกมาได้ทันที : $\\sin A = \\dfrac{BC}{AB} = \\dfrac{24}{25}$ '
        'และ $\\cos A = \\dfrac{AC}{AB} = \\dfrac{7}{25}$',
        '',
        '<b>ขั้นที่ 2 · แปลงมุมเต็มเป็นครึ่งมุมด้วยสูตรครึ่งมุม ⛔ จุดหักของข้อนี้</b>',
        '• ⛔ ก่อนอื่นต้องปักหมุดไว้ให้แน่นว่า $\\tan\\dfrac{A}{2} \\ne \\dfrac{1}{2}\\tan A$ '
        'ถ้าเผลอหารสองจะได้ $\\dfrac{1}{2} \\times \\dfrac{24}{7} = \\dfrac{12}{7}$ '
        'ซึ่งเป็นค่าที่ผิดและจะพาให้ผิดยาวไปจนจบข้อ',
        '• สูตรที่ใช้ : $\\tan\\dfrac{A}{2} = \\dfrac{1 - \\cos A}{\\sin A}$ '
        'ใช้ได้เพราะ $\\sin A = \\dfrac{24}{25}$ ไม่เป็นศูนย์ จึงหารได้อย่างปลอดภัย',
        '• ระบุตัวแปร : ตัวเศษคือ $1$ ลบด้วยโคไซน์ของ<b>มุมเต็ม</b> · ตัวส่วนคือไซน์ของ<b>มุมเต็ม</b> '
        '⛔ ทั้งสองที่ใช้มุมเต็ม $A$ ไม่ใช่ $\\dfrac{A}{2}$ ผลลัพธ์ที่ออกมาต่างหากที่เป็นของครึ่งมุม',
        '• แทนค่า : $\\tan\\dfrac{A}{2} = \\dfrac{1 - \\dfrac{7}{25}}{\\dfrac{24}{25}}$',
        '• จัดตัวเศษก่อน : $1 - \\dfrac{7}{25} = \\dfrac{25}{25} - \\dfrac{7}{25} = \\dfrac{18}{25}$',
        '• ได้เศษส่วนซ้อนสองชั้น $\\dfrac{\\dfrac{18}{25}}{\\dfrac{24}{25}}$ '
        'ให้กลับตัวหารแล้วคูณ : $\\dfrac{18}{25} \\times \\dfrac{25}{24} = \\dfrac{18}{24}$ '
        '(เลข $25$ ตัดกันหมดพอดี)',
        '• ยุบเศษส่วนด้วยการหารทั้งบนและล่างด้วย $6$ : $\\dfrac{18}{24} = \\dfrac{3}{4}$ '
        'สรุปว่า $\\tan\\dfrac{A}{2} = \\dfrac{3}{4}$',
        '• เช็คด้วยสามัญสำนึกทันที : $\\tan A = \\dfrac{24}{7} \\approx 3.43$ '
        'ส่วน $\\tan\\dfrac{A}{2} = 0.75$ ซึ่งเล็กกว่ามาก และเล็กกว่า $\\dfrac{1}{2}\\tan A \\approx 1.71$ '
        'อยู่พอสมควร ⇒ ยืนยันอีกครั้งว่าครึ่งมุมไม่ใช่ครึ่งของค่า $\\tan$',
        '',
        '<b>ขั้นที่ 3 · ใช้ครึ่งมุมในรูปสามเหลี่ยมมุมฉากรูปเล็ก $ACD$ เพื่อหา $CD$</b>',
        '• พิจารณารูปสามเหลี่ยม $ACD$ : จุด $D$ อยู่บนด้าน $BC$ และมุมที่ $C$ เป็นมุมฉากอยู่แล้ว '
        '⇒ รูปสามเหลี่ยม $ACD$ เป็นรูปสามเหลี่ยมมุมฉากที่มีมุมฉากอยู่ที่ $C$ เช่นกัน',
        '• สูตรที่ใช้ : $\\tan(D\\hat{A}C) = \\dfrac{CD}{AC}$ '
        'เพราะเมื่อมองจากมุม $D\\hat{A}C$ แล้ว ด้าน $CD$ เป็นด้านตรงข้าม และด้าน $AC$ เป็นด้านประชิด',
        '• ระบุตัวแปร : มุม $D\\hat{A}C$ มีขนาด $\\dfrac{A}{2}$ ตามนิยามของเส้นแบ่งครึ่งมุม '
        '· $AC = 7$ · $CD$ คือสิ่งที่กำลังหา',
        '• แทนค่า : $\\dfrac{3}{4} = \\dfrac{CD}{7}$ ⇒ คูณไขว้ได้ '
        '$CD = 7 \\times \\dfrac{3}{4} = \\dfrac{21}{4}$ หน่วย',
        '• ตรวจความสมเหตุสมผลของตำแหน่งจุด $D$ : $\\dfrac{21}{4} = 5.25$ ซึ่งน้อยกว่า $BC = 24$ '
        '⇒ จุด $D$ ตกอยู่ภายในด้าน $BC$ จริงตามที่โจทย์บรรยาย ไม่หลุดออกไปนอกด้าน',
        '',
        '<b>ขั้นที่ 4 · ปิดงานด้วยพีทาโกรัสในรูปสามเหลี่ยม $ACD$</b>',
        '• สูตรที่ใช้ : $AC^{2} + CD^{2} = AD^{2}$ ใช้ได้เพราะมุมที่ $C$ ในรูปสามเหลี่ยม $ACD$ เป็นมุมฉาก '
        '⇒ ด้านตรงข้ามมุมฉากของรูปเล็กคือ $AD$ ซึ่งเป็นสิ่งที่โจทย์ถามพอดี',
        '• ระบุตัวแปร : $AC = 7$ · $CD = \\dfrac{21}{4}$ · $AD$ คือคำตอบที่ต้องการ',
        '• แทนค่า : $AD^{2} = 7^{2} + \\left(\\dfrac{21}{4}\\right)^{2} = 49 + \\dfrac{441}{16}$',
        '• ทำตัวส่วนให้เท่ากันก่อนบวก : $49 = \\dfrac{49 \\times 16}{16} = \\dfrac{784}{16}$ '
        '⇒ $AD^{2} = \\dfrac{784}{16} + \\dfrac{441}{16} = \\dfrac{1225}{16}$',
        '• ถอดรากทั้งเศษและส่วน : $AD = \\sqrt{\\dfrac{1225}{16}} = \\dfrac{\\sqrt{1225}}{\\sqrt{16}} '
        '= \\dfrac{35}{4}$ หน่วย (เลือกรากบวกเพราะเป็นความยาวด้าน)',
        '• เขียนเป็นทศนิยมได้ $\\dfrac{35}{4} = 8.75$ หน่วย · '
        'ค่านี้มากกว่า $AC = 7$ สมกับที่เป็นด้านตรงข้ามมุมฉากของรูปเล็ก และน้อยกว่า $AB = 25$ '
        'ซึ่งก็สมเหตุสมผลเพราะ $D$ อยู่ใกล้ $C$ มากกว่าใกล้ $B$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไม่แตะพีทาโกรัสและไม่ใช้ $CD$ เลย '
        'แต่หา $\\cos\\dfrac{A}{2}$ แล้วเดินด้วย $AD = AC \\div \\cos\\dfrac{A}{2}$)</b>',
        '• ในรูปสามเหลี่ยมมุมฉาก $ACD$ ถ้ามองจากมุม $\\dfrac{A}{2}$ '
        'ด้าน $AC$ คือด้านประชิด และ $AD$ คือด้านตรงข้ามมุมฉาก '
        '⇒ $\\cos\\dfrac{A}{2} = \\dfrac{AC}{AD}$ ⇒ ย้ายข้างได้ $AD = \\dfrac{AC}{\\cos\\dfrac{A}{2}}$ '
        'เส้นทางนี้ต้องการเพียงค่า $\\cos\\dfrac{A}{2}$ ตัวเดียว ไม่ต้องรู้ $CD$ และไม่ต้องยกกำลังสองอะไรเลย',
        '• หา $\\cos\\dfrac{A}{2}$ ด้วยสามเหลี่ยมมุมช่วย : ค่า $\\tan\\dfrac{A}{2} = \\dfrac{3}{4}$ '
        'แปลว่ามีรูปสามเหลี่ยมมุมฉากที่ด้านตรงข้ามยาว $3$ และด้านประชิดยาว $4$ '
        'ด้านตรงข้ามมุมฉากจึงยาว $\\sqrt{3^{2}+4^{2}} = \\sqrt{25} = 5$ '
        '⇒ เป็นสามเหลี่ยม $3$-$4$-$5$ ⇒ $\\cos\\dfrac{A}{2} = \\dfrac{4}{5}$',
        '• เดินสูตร : $AD = 7 \\div \\dfrac{4}{5} = 7 \\times \\dfrac{5}{4} = \\dfrac{35}{4}$ '
        'ตรงกับคำตอบที่ได้จากเส้นทางแรกพอดี ✓',
        '• ยืนยันค่า $\\cos\\dfrac{A}{2}$ ซ้ำอีกชั้นโดยไม่พึ่งสามเหลี่ยม $3$-$4$-$5$ : '
        'ใช้ $\\cos\\dfrac{A}{2} = \\sqrt{\\dfrac{1 + \\cos A}{2}} '
        '= \\sqrt{\\dfrac{1 + \\dfrac{7}{25}}{2}} = \\sqrt{\\dfrac{\\dfrac{32}{25}}{2}} '
        '= \\sqrt{\\dfrac{16}{25}} = \\dfrac{4}{5}$ ✓ ตรงกันทั้งสองทาง',
        '• ตรวจเงื่อนไขของโจทย์ปิดท้าย : จากคำตอบย้อนกลับไปหา $CD$ ได้ '
        '$CD = AD\\sin\\dfrac{A}{2} = \\dfrac{35}{4} \\times \\dfrac{3}{5} = \\dfrac{21}{4} = 5.25$ '
        'ซึ่งน้อยกว่า $24$ จริง ⇒ จุด $D$ อยู่บนด้าน $BC$ ตามที่โจทย์กำหนดทุกประการ ✓',
        '',
        '✅ <b>คำตอบ</b> เส้นแบ่งครึ่งมุม $AD$ ยาว $\\dfrac{35}{4}$ หน่วย หรือเท่ากับ $8.75$ หน่วย',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอคำว่า “แบ่งครึ่งมุม” เมื่อไร ให้เขียนตัวหนังสือกำกับไว้ข้างกระดาษทันทีว่า '
        '“มุมที่จะใช้คือครึ่งมุม และครึ่งมุมต้องมาจากสูตรครึ่งมุมเท่านั้น” '
        'สูตรที่คล่องมือที่สุดคือ $\\tan\\dfrac{A}{2} = \\dfrac{1 - \\cos A}{\\sin A}$ '
        'เพราะรับ $\\sin$ กับ $\\cos$ ของมุมเต็มเข้าไปตรง ๆ โดยไม่ต้องถอดรากและไม่ต้องเลือกเครื่องหมาย',
        '• เส้นแบ่งครึ่งมุมที่ลากจากมุมแหลมในรูปสามเหลี่ยมมุมฉาก จะสร้างรูปสามเหลี่ยมมุมฉากรูปเล็ก '
        'ที่ใช้ด้านประชิดร่วมกับรูปใหญ่เสมอ ⇒ พอรู้ค่า $\\tan$ ของครึ่งมุมแล้ว '
        'ก็คูณด้านร่วมนั้นเข้าไปได้ทันทีเพื่อหาด้านอีกข้าง แล้วปิดด้วยพีทาโกรัส',
        '• ค่าตรีโกณที่ออกมาเป็น $\\dfrac{3}{4}$ หรือ $\\dfrac{4}{3}$ ให้นึกถึงสามเหลี่ยม $3$-$4$-$5$ ทันที '
        'จะได้ $\\sin$ และ $\\cos$ ของมุมนั้นมาฟรี ๆ โดยไม่ต้องถอดรากอีกรอบ '
        'เทคนิคนี้ย่นเวลาตรวจคำตอบได้มาก',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\sqrt{193} \\approx 13.89$ เพราะหารสองมั่ว คือใช้ '
        '$\\tan\\dfrac{A}{2} = \\dfrac{1}{2}\\tan A = \\dfrac{1}{2} \\times \\dfrac{24}{7} = \\dfrac{12}{7}$ '
        'แล้วได้ $CD = 7 \\times \\dfrac{12}{7} = 12$ ⇒ $AD = \\sqrt{49 + 144} = \\sqrt{193}$ · '
        'ค่านี้ผิดแน่นอน พิสูจน์ได้สองทาง : ทางแรก ถ้ามุมย่อยมี $\\tan$ เท่ากับ $\\dfrac{12}{7}$ '
        'มุมย่อยนั้นจะมีขนาดประมาณ $59.74^{\\circ}$ สองเท่าของมันคือประมาณ $119.49^{\\circ}$ '
        'ซึ่งเป็นมุมป้าน เป็นไปไม่ได้ เพราะมุม $A$ ในรูปสามเหลี่ยมมุมฉากต้องเป็นมุมแหลม '
        '(ค่าจริงคือประมาณ $73.74^{\\circ}$) · ทางที่สอง ใช้สูตรมุมสองเท่า '
        '$\\tan 2x = \\dfrac{2\\tan x}{1 - \\tan^{2}x}$ กับ $\\tan x = \\dfrac{12}{7}$ '
        'จะได้ค่าประมาณ $-1.77$ ซึ่งติดลบ ไม่ใช่ $\\tan A = \\dfrac{24}{7} \\approx 3.43$ '
        '⇒ ยืนยันว่า $\\dfrac{12}{7}$ ไม่ใช่ $\\tan$ ของครึ่งมุม',
        '• ได้ค่า $\\dfrac{21}{4}$ เพราะหยุดงานเร็วไปหนึ่งขั้น คือหา $CD$ ได้แล้วนึกว่าจบ '
        'ทั้งที่โจทย์ถามความยาว $AD$ ไม่ใช่ $CD$ · ค่านี้ผิดแบบเห็นได้ทันทีโดยไม่ต้องคำนวณอะไรเลย '
        'เพราะ $AD$ เป็นด้านตรงข้ามมุมฉากของรูปสามเหลี่ยมมุมฉาก $ACD$ '
        'จึงต้องยาวกว่าด้านประกอบมุมฉาก $AC = 7$ เสมอ แต่ $\\dfrac{21}{4} = 5.25$ ซึ่งสั้นกว่า $7$ '
        '⇒ เป็นไปไม่ได้ · วิธีกันคือขีดเส้นใต้สิ่งที่โจทย์ถามไว้ตั้งแต่อ่านโจทย์รอบแรก',
        '• ได้ค่า $\\dfrac{75}{4} = 18.75$ เพราะใช้สมบัติเส้นแบ่งครึ่งมุมที่ว่า '
        '$\\dfrac{BD}{DC} = \\dfrac{AB}{AC} = \\dfrac{25}{7}$ ร่วมกับ $BD + DC = 24$ '
        'ซึ่งให้ $DC = 24 \\times \\dfrac{7}{32} = \\dfrac{21}{4}$ และ '
        '$BD = 24 \\times \\dfrac{25}{32} = \\dfrac{75}{4}$ แล้วเผลอตอบ $BD$ ไป · '
        'สังเกตว่าสมบัตินี้ให้ $DC$ ตรงกับที่คำนวณด้วยสูตรครึ่งมุมพอดี จึงไม่ผิดที่ตัวสมบัติ '
        'แต่ผิดที่หยิบชิ้นส่วนผิดชิ้น เพราะ $BD$ กับ $DC$ ต่างก็เป็นท่อนย่อยของด้าน $BC$ '
        '(ตรวจได้จาก $\\dfrac{75}{4} + \\dfrac{21}{4} = \\dfrac{96}{4} = 24$ พอดี) '
        'ส่วน $AD$ เป็นเส้นเฉียงที่พาดข้ามรูป ไม่ได้อยู่บน $BC$ เลย',
        '• ได้ค่า $25$ เพราะใช้มุมเต็มแทนครึ่งมุมในขั้นตรวจ คือคิด '
        '$AD = \\dfrac{AC}{\\cos A} = 7 \\div \\dfrac{7}{25} = 25$ · '
        'ค่านี้คือความยาว $AB$ พอดีเป๊ะ ซึ่งแปลว่าเผลอลากเส้นไปจบที่จุด $B$ แทนที่จะจบที่จุด $D$ '
        'ถ้าเป็นเช่นนั้นจริงจะต้องได้ $CD = 24$ แต่ค่าจริงคือ $\\dfrac{21}{4} = 5.25$ '
        '⇒ ขัดกันชัดเจน · จุดกันพลาดคือถามตัวเองทุกครั้งว่ามุมที่กำลังใช้เป็นมุมของรูปใหญ่หรือรูปเล็ก',
        '• ได้ค่า $\\dfrac{175}{16} = 10.9375$ เพราะลืมถอดรากในสูตรครึ่งมุมของโคไซน์ '
        'คือคำนวณ $\\dfrac{1 + \\cos A}{2} = \\dfrac{16}{25}$ แล้วหยิบ $\\dfrac{16}{25}$ ไปใช้เป็น '
        '$\\cos\\dfrac{A}{2}$ เลย ทั้งที่ $\\dfrac{16}{25}$ เป็นค่าของ $\\cos^{2}\\dfrac{A}{2}$ '
        '⇒ ได้ $AD = 7 \\div \\dfrac{16}{25} = \\dfrac{175}{16}$ · '
        'ค่านี้ผิดแน่นอน ตรวจได้ด้วยการแทนกลับในสูตรมุมสองเท่า : ถ้า $\\cos\\dfrac{A}{2} = \\dfrac{16}{25}$ '
        'จะได้ $\\cos A = 2\\left(\\dfrac{16}{25}\\right)^{2} - 1 = \\dfrac{512}{625} - 1 '
        '= -\\dfrac{113}{625} \\approx -0.18$ ซึ่งติดลบ แปลว่ามุม $A$ เป็นมุมป้าน '
        'ขัดกับข้อเท็จจริงที่ว่ามุม $A$ ในรูปสามเหลี่ยมมุมฉากต้องเป็นมุมแหลม '
        'และขัดกับค่าที่โจทย์บังคับไว้คือ $\\cos A = \\dfrac{7}{25}$',
    ],
    'V.mold: G = a right triangle with the right angle named at C and the two legs handed over as the '
    'bare numbers 7 and 24, plus a cevian described purely in words as the bisector of the acute angle A '
    'whose foot D is stated to lie on the leg BC / A = the length of that bisector AD, asked as a free '
    'numeric response with no candidate values on the page / M = complete the 7-24-25 triple to read '
    'cos A and sin A, push them through the half-angle identity tan(A/2) = (1 - cos A)/sin A, multiply '
    'that ratio by the shared leg AC to obtain CD inside the nested right triangle ACD, then close with '
    'Pythagoras on that nested triangle. '
    'Rubric F3 C2 P3 T2 L1 = 11/15 with total below 12, so the very-hard band is not reached -> level: ยาก. '
    'F = 3 because three separate pieces of knowledge must be held at once: the Pythagorean '
    'relation, the ratio definitions of sin, cos and tan for an acute angle, and the tangent half-angle '
    'identity; no two of them can substitute for a third. C = 2 because the item genuinely joins subtopic '
    '7.1 (ratios inside a right triangle) with subtopic 7.6 (half-angle identities); removing either one '
    'leaves the item unsolvable. P = 3 because the work runs in a chain of three stages where each stage '
    'consumes an object the previous stage produced: the triple yields cos A and sin A, those yield '
    'tan(A/2), and tan(A/2) yields CD, which only then feeds Pythagoras. T = 2 and deliberately not 3: '
    'there is exactly one turning point, namely the recognition that the bisector forces the half angle '
    'and that its tangent is not half the tangent of the full angle; once that is seen the remaining road '
    'is routine, whereas a T = 3 item such as q117 requires two independent insights to be discovered '
    'before any computation can start. L = 1 because the statement, although free of any real-world '
    'scene, still has to be translated from prose into a figure: the reader must place D on BC and notice '
    'that triangle ACD inherits the right angle at C. Scoring was written before the level was read off. '
    'sympy (verify_b19.py): with A = atan(24/7), simplify((1 - cos(A))/sin(A)) returns 3/4 and equals '
    'tan(A/2) symbolically; 7*Rational(3,4) returns 21/4, which is confirmed strictly less than 24 so the '
    'foot D really lies inside BC; sqrt(7**2 + Rational(21,4)**2) returns 35/4 exactly, matching the '
    'stored answer and its decimal form 8.75. The independent route was machine checked separately: '
    'sqrt((1 + Rational(7,25))/2) returns 4/5, the same 4/5 that the 3-4-5 auxiliary triangle gives, and '
    '7/Rational(4,5) returns 35/4. Every error path in the pitfalls block was computed by machine rather '
    'than invented: half of tan A is 12/7, giving CD = 12 and AD = sqrt(193) about 13.892, refuted '
    'because 2*atan(12/7) is about 119.49 degrees, an obtuse value impossible for the acute angle A, and '
    'because tan(2*atan(12/7)) evaluates to about -1.768 rather than 24/7; stopping at CD gives 21/4 = '
    '5.25, refuted because a hypotenuse cannot be shorter than the leg AC = 7; the angle-bisector ratio '
    'BD/DC = 25/7 with BD + DC = 24 gives BD = 75/4 = 18.75 and DC = 21/4, whose sum sympy confirms is '
    'exactly 24, so 75/4 is provably a piece of BC and not the cevian; using the full angle gives '
    '7/Rational(7,25) = 25, which equals AB and would place D at B; and dropping the square root gives '
    '7/Rational(16,25) = 175/16 = 10.9375, refuted because 2*Rational(16,25)**2 - 1 = -113/625 is '
    'negative and would make A obtuse. '
    'Collision sweep on 6417 items (bank 63 files + k1 out + k2 out), probe collide_b19.py / '
    'collide_b19b.py: scan A5 (question text carrying the Thai phrase for angle bisector) returns exactly '
    'one item in the whole corpus, gen-chap-04-coord-q202, which asks for the equation of an angle '
    'bisector in coordinate geometry and shares neither the answer type nor the mechanism; scan A5b '
    '(angle bisector intersected with right triangle) returns zero items, so the pair is untouched. The '
    'nearest neighbours inside chapter 7 all hand over an angle in degrees and ask for a ratio, whereas '
    'this item hands over two legs and asks for a length built on a half angle. Since this is a fill '
    'item there is no choice list, so no answer slot exists and nothing about the answer could have been '
    'positioned by hand.',
)

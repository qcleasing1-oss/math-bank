# -*- coding: utf-8 -*-
add_fill(
    158,
    ['7.2'],
    'ยากมาก',
    'กำหนดให้ $\\theta$ เป็นจำนวนจริงซึ่ง $\\sin\\theta \\ne 0$ และ $\\cos\\theta \\ne 0$ โดยที่ '
    '$\\dfrac{\\csc\\theta}{\\cot\\theta} = -\\dfrac{61}{11}$ และ $\\sin\\theta < 0$ แล้วค่าของ '
    '$61\\displaystyle\\sum_{k=1}^{14}\\cos\\left(\\theta + \\dfrac{k\\pi}{2}\\right)$ เท่ากับเท่าใด',
    '71',
    ['71'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• นิยามของฟังก์ชันตรีโกณมิติส่วนกลับ : $\\csc\\theta = \\dfrac{1}{\\sin\\theta}$ · '
        '$\\sec\\theta = \\dfrac{1}{\\cos\\theta}$ · $\\cot\\theta = \\dfrac{\\cos\\theta}{\\sin\\theta}$ '
        '· เหตุผลที่โจทย์ต้องเขียนกำกับว่า $\\sin\\theta \\ne 0$ และ $\\cos\\theta \\ne 0$ '
        'ก็เพราะตัวส่วนของนิยามเหล่านี้ห้ามเป็นศูนย์ ⇒ สองบรรทัดนั้นไม่ใช่คำประดับ '
        'แต่เป็นใบรับรองว่าทุกตัวที่โจทย์เขียนมาหาค่าได้จริง '
        '· และการหารเศษส่วนด้วยเศษส่วนคือการคูณด้วยส่วนกลับ ⇒ $\\dfrac{a \\div b}{c \\div d} = '
        '\\dfrac{a}{b} \\times \\dfrac{d}{c}$',
        '• เอกลักษณ์พีทาโกรัส $\\sin^{2}\\theta + \\cos^{2}\\theta = 1$ ใช้เดินจาก $\\cos\\theta$ ไปหา '
        '$\\sin\\theta$ ได้ โดยย้ายข้างเป็น $\\sin^{2}\\theta = 1 - \\cos^{2}\\theta$ แล้วถอดกรณฑ์ '
        '⇒ $\\sin\\theta = \\pm\\sqrt{1 - \\cos^{2}\\theta}$ ⛔ เครื่องหมาย $\\pm$ ตรงนี้เอกลักษณ์'
        '<b>ตอบให้ไม่ได้</b> เพราะการยกกำลังสองกลืนเครื่องหมายทิ้งไปแล้ว '
        '⇒ ต้องมีข้อมูลจากที่อื่นมาชี้ขาดเสมอ',
        '• สูตรลดรูปเมื่อบวกมุมเพิ่มทีละหนึ่งในสี่รอบ : $\\cos\\left(\\theta + \\dfrac{\\pi}{2}\\right) = '
        '-\\sin\\theta$ · $\\cos(\\theta + \\pi) = -\\cos\\theta$ · '
        '$\\cos\\left(\\theta + \\dfrac{3\\pi}{2}\\right) = \\sin\\theta$ · '
        '$\\cos(\\theta + 2\\pi) = \\cos\\theta$ · เหตุผลที่ไม่ต้องท่องจำ : จุดปลายส่วนโค้งของ $\\theta$ '
        'บนวงกลมหนึ่งหน่วยคือจุด $(\\cos\\theta , \\sin\\theta)$ การบวก $\\dfrac{\\pi}{2}$ '
        'คือการหมุนจุดนั้นทวนเข็มนาฬิกาไปหนึ่งในสี่รอบ ซึ่งพาจุด $(a , b)$ ไปเป็นจุด $(-b , a)$ '
        '⇒ พิกัดแรกซึ่งก็คือค่า $\\cos$ ตัวใหม่ กลายเป็น $-b = -\\sin\\theta$ '
        '⇒ หมุนต่อไปอีกก็ได้บรรทัดถัดไปเรื่อย ๆ จนครบรอบแล้วกลับมาที่จุดเดิม',
        '• คาบของ $\\cos$ เท่ากับ $2\\pi$ ⇒ $\\cos(x + 2\\pi m) = \\cos x$ ทุกจำนวนเต็ม $m$ '
        '· ประโยชน์คือเวลาเจอมุมที่บวกไปไกลมาก ให้ดึงรอบเต็มออกทิ้งเสียก่อน แล้วเหลือแต่เศษที่เล็กกว่าหนึ่งรอบ '
        '⇒ นี่เป็นเครื่องมือเดียวที่ทำให้พจน์ท้าย ๆ ของผลรวมยาว ๆ กลับมามีหน้าตาเหมือนพจน์ต้น ๆ ได้',
        '• การจับกลุ่มผลรวมที่ค่าวนซ้ำ : ถ้าค่าของพจน์วนซ้ำทุก $4$ พจน์ และสี่พจน์ติดกันบวกกันได้ $0$ '
        'แล้วผลรวมของ $n$ พจน์แรกจะขึ้นกับ<b>เศษ</b>ของ $n$ เมื่อหารด้วย $4$ เท่านั้น '
        '· เขียนเป็น $n = 4q + r$ ⇒ ก้อนละสี่พจน์จำนวน $q$ ก้อนหายไปหมด เหลือเพียง $r$ พจน์ท้ายที่ต้องคิดจริง '
        '⛔ กับดักคือถ้ารีบสรุปว่า “หักล้างกันหมด” โดยไม่หาเศษก่อน จะได้ $0$ ทุกครั้ง '
        'ซึ่งถูกเฉพาะกรณี $r = 0$ เท่านั้น',
        '• สามจำนวน $11$ , $60$ , $61$ เป็นความยาวด้านของสามเหลี่ยมมุมฉาก เพราะ '
        '$11^{2} + 60^{2} = 121 + 3600 = 3721 = 61^{2}$ ⇒ ถ้าด้านตรงข้ามมุมฉากยาว $61$ และด้านหนึ่งยาว $11$ '
        'อีกด้านจะยาว $60$ พอดีโดยไม่มีกรณฑ์ติดค้าง · จำชุดนี้ไว้จะถอดกรณฑ์ในขั้นที่ 2 ได้ทันที',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• $\\theta$ เป็นจำนวนจริงซึ่ง $\\sin\\theta \\ne 0$ และ $\\cos\\theta \\ne 0$ '
        '⇒ ทั้ง $\\csc\\theta$ และ $\\cot\\theta$ หาค่าได้ และการตัดทอนที่จะทำในขั้นที่ 1 ก็ทำได้อย่างถูกกฎ',
        '• เงื่อนไขหลักคือ $\\dfrac{\\csc\\theta}{\\cot\\theta} = -\\dfrac{61}{11}$',
        '• เงื่อนไขเสริมที่ห้ามลืมเด็ดขาดคือ $\\sin\\theta < 0$',
        '• สิ่งที่ต้องหาคือค่าของ $61\\displaystyle\\sum_{k=1}^{14}\\cos\\left(\\theta + '
        '\\dfrac{k\\pi}{2}\\right)$ ซึ่งเป็นผลบวกของโคไซน์ $14$ พจน์ คูณด้วย $61$ อีกที '
        '· ตัวนับ $k$ วิ่งจาก $1$ ถึง $14$ ⛔ ไม่ได้เริ่มที่ $0$',
        '• สังเกตหน้าตาก่อนลงมือ (หนึ่ง) : เงื่อนไขที่ให้มามีทั้ง $\\csc\\theta$ และ $\\cot\\theta$ '
        'ซึ่งดูเหมือนของสองอย่าง แต่ทั้งคู่มี $\\sin\\theta$ ฝังอยู่ข้างใน ⇒ เดาทางได้ตั้งแต่ยังไม่คำนวณว่า '
        '$\\sin\\theta$ น่าจะตัดกันหายไป และเงื่อนไขก้อนนี้จะเหลือข้อมูลเรื่อง $\\cos\\theta$ เพียงอย่างเดียว '
        '⇒ ถ้าเป็นเช่นนั้นจริง เครื่องหมายของ $\\sin\\theta$ ย่อมยังไม่ถูกกำหนด '
        'จึงต้องมีบรรทัด $\\sin\\theta < 0$ มาปิดช่องว่างนี้',
        '• สังเกตหน้าตาก่อนลงมือ (สอง) : มุมของพจน์ที่ $k$ คือ $\\theta + \\dfrac{k\\pi}{2}$ '
        '⇒ เดินจากพจน์หนึ่งไปพจน์ถัดไป มุมเพิ่มขึ้นครั้งละ $\\dfrac{\\pi}{2}$ พอดี ซึ่งคือหนึ่งในสี่รอบ '
        '⇒ ⛔ อย่าลงมือกดหาค่าโคไซน์ทีละพจน์ทั้ง $14$ พจน์ ให้ไปดูโครงของวงรอบก่อนว่าค่าซ้ำทุกกี่พจน์',
        '• สังเกตหน้าตาก่อนลงมือ (สาม) : ตัวเลข $61$ ที่คูณอยู่ข้างนอกเป็นตัวเดียวกับ $61$ ที่เป็นตัวส่วนในเงื่อนไข '
        '⇒ ผู้ออกข้อสอบตั้งใจให้ตัวส่วนถูกล้างจนคำตอบออกมาเป็นจำนวนเต็ม '
        '⇒ ถ้าคำนวณแล้วได้เศษส่วนที่ตัด $61$ ไม่ลง แปลว่าเดินผิดทางที่ไหนสักแห่ง',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $61\\displaystyle\\sum_{k=1}^{14}\\cos\\left(\\theta + \\dfrac{k\\pi}{2}\\right)$ '
        'ออกมาเป็นจำนวนเดียว',
        '',
        '<b>【 ยุบ $\\dfrac{\\csc\\theta}{\\cot\\theta}$ ให้เหลือ $\\sec\\theta$ เพื่ออ่านค่า $\\cos\\theta$ '
        'ออกมาก่อน · ใช้เงื่อนไข $\\sin\\theta < 0$ ชี้ขาดเครื่องหมายของ $\\sin\\theta$ · '
        'แล้วมองผลรวม $14$ พจน์เป็นก้อนละสี่พจน์ที่บวกกันได้ศูนย์ จนเหลือเพียงสองพจน์ท้ายที่ต้องคิดจริง 】</b>',
        '',
        '<b>ขั้นที่ 1 · ยุบเงื่อนไขที่ดูซับซ้อนให้เหลือของง่ายที่สุดก่อนลงมือทำอย่างอื่น</b>',
        '• เหตุผลที่ต้องทำขั้นนี้ก่อน : เงื่อนไขที่โจทย์ให้เขียนด้วย $\\csc$ กับ $\\cot$ '
        'ซึ่งเป็นฟังก์ชันที่คนส่วนใหญ่ไม่คุ้นมือ ถ้าดันทุรังคำนวณทั้งอย่างนั้นจะเปลืองแรงและพลาดง่าย '
        '· กติกาที่ปลอดภัยเสมอคือ<b>เปลี่ยนทุกอย่างให้เป็น</b> $\\sin$ <b>กับ</b> $\\cos$ ก่อน แล้วค่อยดูว่าอะไรตัดกันได้',
        '• สูตรที่ใช้ : $\\csc\\theta = \\dfrac{1}{\\sin\\theta}$ และ $\\cot\\theta = '
        '\\dfrac{\\cos\\theta}{\\sin\\theta}$',
        '• แทนค่าลงในเงื่อนไข : $\\dfrac{\\csc\\theta}{\\cot\\theta} = \\dfrac{\\dfrac{1}{\\sin\\theta}}'
        '{\\dfrac{\\cos\\theta}{\\sin\\theta}}$',
        '• ยุบด้วยกฎการหารเศษส่วน (กลับเศษส่วนตัวล่างแล้วคูณ) : $= \\dfrac{1}{\\sin\\theta} \\times '
        '\\dfrac{\\sin\\theta}{\\cos\\theta}$ ⇒ $\\sin\\theta$ โผล่ทั้งตัวส่วนของก้อนแรกและตัวเศษของก้อนหลัง '
        '⇒ ตัดกันได้ ⭐ และตรงนี้เองที่บรรทัด $\\sin\\theta \\ne 0$ ในโจทย์ออกฤทธิ์ เพราะการตัดตัวประกอบทิ้ง '
        'ทำได้ก็ต่อเมื่อตัวนั้นไม่ใช่ศูนย์ ⇒ เหลือ $\\dfrac{1}{\\cos\\theta}$ ซึ่งตามนิยามคือ $\\sec\\theta$',
        '• สรุปเงื่อนไขในรูปใหม่ : $\\sec\\theta = -\\dfrac{61}{11}$',
        '• พลิกกลับเป็น $\\cos\\theta$ : เพราะ $\\sec\\theta$ กับ $\\cos\\theta$ เป็นส่วนกลับของกันและกัน '
        '⇒ $\\cos\\theta = \\dfrac{1}{\\sec\\theta} = \\dfrac{1}{-\\dfrac{61}{11}} = -\\dfrac{11}{61}$',
        '• ตรวจความสมเหตุสมผลทันทีกันหลงทาง : ค่าของ $\\cos$ ต้องอยู่ระหว่าง $-1$ กับ $1$ เสมอ '
        '· ค่าที่ได้คือ $-\\dfrac{11}{61} \\approx -0.18$ ซึ่งอยู่ในช่วงนั้นจริง ✓ '
        '⛔ ถ้าใครเผลอตอบว่า $\\cos\\theta = -\\dfrac{61}{11} \\approx -5.55$ '
        'จะรู้ได้ทันทีว่าผิดเพราะเกินขอบเขตของโคไซน์ไปมาก',
        '',
        '<b>ขั้นที่ 2 · หา $\\sin\\theta$ ด้วยเอกลักษณ์พีทาโกรัส แล้วให้เงื่อนไข $\\sin\\theta < 0$ '
        'เป็นผู้ตัดสินเครื่องหมาย</b>',
        '• สูตรที่ใช้ : $\\sin^{2}\\theta + \\cos^{2}\\theta = 1$ ⇒ ย้ายข้างเป็น '
        '$\\sin^{2}\\theta = 1 - \\cos^{2}\\theta$',
        '• ระบุตัวแปรแล้วแทนค่า : จากขั้นที่ 1 ได้ $\\cos\\theta = -\\dfrac{11}{61}$ '
        '⇒ $\\cos^{2}\\theta = \\left(-\\dfrac{11}{61}\\right)^{2} = \\dfrac{121}{3721}$ '
        '(ยกกำลังสองแล้วเครื่องหมายลบหายไป เพราะจำนวนลบยกกำลังสองได้ผลเป็นบวก)',
        '• ยุบ : $\\sin^{2}\\theta = 1 - \\dfrac{121}{3721} = \\dfrac{3721 - 121}{3721} = '
        '\\dfrac{3600}{3721}$ ⇒ ถอดกรณฑ์ทั้งเศษและส่วน โดย $3600 = 60^{2}$ และ $3721 = 61^{2}$ '
        '⇒ $\\sin\\theta = \\pm\\dfrac{60}{61}$',
        '• ⭐ จุดตัดสินใจที่ห้ามข้าม : ถึงตรงนี้เอกลักษณ์บอกได้แค่<b>ขนาด</b>ของ $\\sin\\theta$ '
        'ยังบอกเครื่องหมายไม่ได้ เพราะทั้ง $\\dfrac{60}{61}$ และ $-\\dfrac{60}{61}$ ยกกำลังสองแล้วได้ '
        '$\\dfrac{3600}{3721}$ เท่ากัน · ผู้ที่ชี้ขาดคือบรรทัด $\\sin\\theta < 0$ ที่โจทย์เขียนไว้ '
        '⇒ เลือกค่าลบ ⇒ $\\sin\\theta = -\\dfrac{60}{61}$',
        '• เหตุผลลึกอีกชั้นว่าทำไมโจทย์ต้องเขียนบรรทัดนั้นมาให้ : ขั้นที่ 1 ให้ $\\cos\\theta < 0$ '
        'ซึ่งเกิดได้ทั้งในจตุภาคที่ $2$ (ที่นั่น $\\sin\\theta > 0$) และจตุภาคที่ $3$ '
        '(ที่นั่น $\\sin\\theta < 0$) ⇒ ถ้าไม่มีเงื่อนไขเสริม โจทย์จะมีสองคำตอบทันที '
        '· เมื่อบังคับว่า $\\sin\\theta < 0$ จึงเหลือจตุภาคที่ $3$ สาขาเดียว ซึ่งเข้ากันได้ดีกับ '
        '$\\cos\\theta < 0$ ที่หามาแล้ว',
        '• เก็บของสองชิ้นที่จะใช้ต่อ : $\\sin\\theta = -\\dfrac{60}{61}$ และ '
        '$\\cos\\theta = -\\dfrac{11}{61}$ ⇒ ทั้งคู่<b>เป็นลบ</b> จำข้อนี้ไว้ให้แม่น '
        'เพราะขั้นที่ 3 จะต้องใช้ค่าติดลบสองตัวนี้กลับเครื่องหมาย',
        '',
        '<b>ขั้นที่ 3 · 🔴 หัวใจของข้อ · อ่านโครงของผลรวม $14$ พจน์ แทนที่จะไล่คิดทีละพจน์</b>',
        '• กางผลรวมออกดูก่อนว่าหน้าตาเป็นอย่างไร : พจน์ที่ $1$ คือ '
        '$\\cos\\left(\\theta + \\dfrac{\\pi}{2}\\right)$ · พจน์ที่ $2$ คือ $\\cos(\\theta + \\pi)$ · '
        'พจน์ที่ $3$ คือ $\\cos\\left(\\theta + \\dfrac{3\\pi}{2}\\right)$ · พจน์ที่ $4$ คือ '
        '$\\cos(\\theta + 2\\pi)$ · ไล่ต่อไปจนถึงพจน์ที่ $14$ คือ $\\cos(\\theta + 7\\pi)$',
        '• ⭐ กุญแจดอกที่ 1 : ระยะห่างของมุมระหว่างพจน์ติดกันคือ $\\dfrac{\\pi}{2}$ คงที่ตลอด '
        'ซึ่งเท่ากับหนึ่งในสี่รอบ ⇒ หมุนสี่ครั้งก็ครบหนึ่งรอบพอดีและกลับมาที่จุดเดิม '
        '⇒ ค่าของพจน์ต้อง<b>วนซ้ำทุกสี่พจน์</b> ⇒ ไม่ว่าผลรวมจะยาวแค่ไหน ค่าที่โผล่มาก็มีแค่สี่แบบเท่านั้น',
        '• ใช้สูตรลดรูปเขียนสี่แบบนั้นออกมาให้ครบ : $\\cos\\left(\\theta + \\dfrac{\\pi}{2}\\right) = '
        '-\\sin\\theta$ · $\\cos(\\theta + \\pi) = -\\cos\\theta$ · '
        '$\\cos\\left(\\theta + \\dfrac{3\\pi}{2}\\right) = \\sin\\theta$ · $\\cos(\\theta + 2\\pi) = '
        '\\cos\\theta$',
        '• ⭐ กุญแจดอกที่ 2 : บวกสี่พจน์ติดกันนี้เข้าด้วยกัน '
        '$(-\\sin\\theta) + (-\\cos\\theta) + \\sin\\theta + \\cos\\theta = 0$ '
        '· เหตุผลที่ได้ศูนย์พอดีคือของสี่ชิ้นนี้จับคู่กันเองได้ครบ ตัวที่หนึ่งกับตัวที่สามเป็นจำนวนตรงข้ามกัน '
        'และตัวที่สองกับตัวที่สี่ก็เป็นจำนวนตรงข้ามกัน ⇒ <b>ทุกก้อนสี่พจน์ติดกันบวกกันได้ศูนย์เสมอ</b> '
        'ไม่ว่า $\\theta$ จะมีค่าเท่าไร',
        '• ⭐ กุญแจดอกที่ 3 ซึ่งเป็นจุดที่ข้อนี้ตั้งใจดัก : ต้องหารดูว่ามีก้อนสี่พจน์กี่ก้อนและเหลือเศษกี่พจน์ '
        '⇒ $14 = 4 \\times 3 + 2$ ⇒ พจน์ที่ $1$ ถึงพจน์ที่ $12$ จัดได้พอดี $3$ ก้อน '
        'และหายไปทั้งหมด ⇒ <b>เหลือพจน์ที่</b> $13$ <b>กับพจน์ที่</b> $14$ ที่ยังไม่มีคู่มาหักล้าง '
        '⛔ ตรงนี้ห้ามรีบสรุปว่าหักล้างกันหมด เพราะ $14$ หารด้วย $4$ ไม่ลงตัว',
        '• คิดพจน์ที่ $13$ : มุมคือ $\\theta + \\dfrac{13\\pi}{2}$ · ดึงรอบเต็มออกโดยเขียน '
        '$\\dfrac{13\\pi}{2} = \\dfrac{\\pi}{2} + 6\\pi$ (ตรวจได้ว่า $\\dfrac{\\pi}{2} + 6\\pi = '
        '\\dfrac{\\pi + 12\\pi}{2} = \\dfrac{13\\pi}{2}$ ✓ และ $6\\pi$ คือสามรอบเต็ม) '
        '⇒ ใช้คาบ $2\\pi$ ตัดสามรอบทิ้ง ⇒ $\\cos\\left(\\theta + \\dfrac{13\\pi}{2}\\right) = '
        '\\cos\\left(\\theta + \\dfrac{\\pi}{2}\\right) = -\\sin\\theta$',
        '• คิดพจน์ที่ $14$ : มุมคือ $\\theta + \\dfrac{14\\pi}{2} = \\theta + 7\\pi$ · '
        'เขียน $7\\pi = \\pi + 6\\pi$ ⇒ ตัดสามรอบทิ้งอีกครั้ง ⇒ $\\cos(\\theta + 7\\pi) = '
        '\\cos(\\theta + \\pi) = -\\cos\\theta$',
        '• รวมสองพจน์ที่เหลือแล้วแทนค่าจากขั้นที่ 2 : ผลรวมทั้งหมด $= -\\sin\\theta - \\cos\\theta = '
        '-\\left(-\\dfrac{60}{61}\\right) - \\left(-\\dfrac{11}{61}\\right) = \\dfrac{60}{61} + '
        '\\dfrac{11}{61} = \\dfrac{71}{61}$ · สังเกตว่าเครื่องหมายลบสองชั้นกลายเป็นบวกทั้งสองพจน์ '
        'เพราะค่าที่แทนลงไปเป็นลบอยู่แล้ว ⇒ ผลรวมออกมาเป็นบวก',
        '',
        '<b>ขั้นที่ 4 · คูณด้วยตัวเลขที่ค้างอยู่หน้าเครื่องหมายผลรวม</b>',
        '• สิ่งที่โจทย์ถามคือ $61$ เท่าของผลรวม ไม่ใช่ตัวผลรวมเปล่า ⇒ ต้องคูณกลับก่อนตอบ',
        '• แทนค่า : $61 \\times \\dfrac{71}{61} = 71$ ⇒ ตัวประกอบ $61$ ตัดกับตัวส่วนพอดี '
        'เหลือจำนวนเต็ม $71$',
        '• ⭐ อ่านเจตนาของผู้ออกข้อสอบให้ออก : เลข $61$ ที่วางไว้ข้างนอกไม่ได้ใส่มามั่ว '
        'แต่ใส่มาเพื่อล้างตัวส่วน $61$ ที่จะเกิดขึ้นแน่ ๆ จากสามเหลี่ยม $11$-$60$-$61$ '
        '⇒ ถ้าคำนวณถึงบรรทัดสุดท้ายแล้วยังตัด $61$ ไม่ลง แปลว่าต้องย้อนไปหาที่ผิด',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · เขียนค่าของทั้งสิบสี่พจน์ออกมาเป็นตัวเลขจริงทีละพจน์แล้วบวกตรง ๆ '
        'โดยไม่ใช้การจับกลุ่มหรือการหารหาเศษเลย)</b>',
        '• เตรียมค่าที่จะใช้แทน : $\\sin\\theta = -\\dfrac{60}{61}$ และ $\\cos\\theta = -\\dfrac{11}{61}$ '
        '⇒ $-\\sin\\theta = \\dfrac{60}{61}$ และ $-\\cos\\theta = \\dfrac{11}{61}$',
        '• แถวที่หนึ่ง (พจน์ที่ $1$ ถึงพจน์ที่ $4$) : $-\\sin\\theta = \\dfrac{60}{61}$ · '
        '$-\\cos\\theta = \\dfrac{11}{61}$ · $\\sin\\theta = -\\dfrac{60}{61}$ · '
        '$\\cos\\theta = -\\dfrac{11}{61}$ ⇒ บวกตัวเศษกันตรง ๆ ได้ $60 + 11 - 60 - 11 = 0$ '
        '⇒ แถวนี้รวมได้ $0$',
        '• แถวที่สอง (พจน์ที่ $5$ ถึงพจน์ที่ $8$) : มุมของแต่ละพจน์มากกว่าแถวแรกอยู่ $2\\pi$ พอดี '
        '(เพราะเลื่อนไป $4$ พจน์ $= 4 \\times \\dfrac{\\pi}{2}$) ⇒ ค่าทั้งสี่ช่องเท่ากับแถวแรกทุกช่อง '
        '⇒ $\\dfrac{60}{61}$ · $\\dfrac{11}{61}$ · $-\\dfrac{60}{61}$ · $-\\dfrac{11}{61}$ '
        '⇒ แถวนี้รวมได้ $0$',
        '• แถวที่สาม (พจน์ที่ $9$ ถึงพจน์ที่ $12$) : ด้วยเหตุผลเดียวกัน ค่าทั้งสี่ช่องเท่ากับแถวแรกอีกครั้ง '
        '⇒ $\\dfrac{60}{61}$ · $\\dfrac{11}{61}$ · $-\\dfrac{60}{61}$ · $-\\dfrac{11}{61}$ '
        '⇒ แถวนี้รวมได้ $0$',
        '• แถวที่สี่ (เหลือแค่สองช่อง คือพจน์ที่ $13$ กับพจน์ที่ $14$) : $\\dfrac{60}{61}$ · '
        '$\\dfrac{11}{61}$ ⇒ แถวนี้รวมได้ $\\dfrac{60 + 11}{61} = \\dfrac{71}{61}$ '
        '· ⛔ แถวนี้ขาดไปสองช่องจึงไม่มีตัวมาหักล้าง นี่คือเหตุผลที่ผลรวมไม่เป็นศูนย์',
        '• บวกทุกแถว : $0 + 0 + 0 + \\dfrac{71}{61} = \\dfrac{71}{61}$ ⇒ คูณ $61$ ได้ '
        '$61 \\times \\dfrac{71}{61} = 71$ ✓ ตรงกับทางเดินหลักทุกประการ',
        '• ตรวจย้อนกลับไปที่ตัวโจทย์ว่าค่าที่หามาสอดคล้องจริงหรือไม่ : '
        '$\\sec\\theta = \\dfrac{1}{\\cos\\theta} = \\dfrac{1}{-\\dfrac{11}{61}} = -\\dfrac{61}{11}$ ✓ '
        'ตรงกับค่าที่โจทย์ให้ · $\\sin\\theta = -\\dfrac{60}{61} < 0$ ✓ ตรงกับเงื่อนไขเสริม · '
        'และ $11^{2} + 60^{2} = 121 + 3600 = 3721 = 61^{2}$ ✓ ⇒ จุด '
        '$\\left(-\\dfrac{11}{61} , -\\dfrac{60}{61}\\right)$ อยู่บนวงกลมหนึ่งหน่วยจริง '
        '⇒ มุม $\\theta$ แบบนี้มีอยู่จริง โจทย์ไม่ขัดแย้งในตัวเอง',
        '',
        '✅ <b>คำตอบ</b> ผลรวม $14$ พจน์ยุบเหลือ $-\\sin\\theta - \\cos\\theta = \\dfrac{71}{61}$ '
        'ดังนั้นค่าของ $61\\displaystyle\\sum_{k=1}^{14}\\cos\\left(\\theta + \\dfrac{k\\pi}{2}\\right)$ '
        'เท่ากับ $61 \\times \\dfrac{71}{61} = 71$',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอผลรวมยาว ๆ ที่มุมเพิ่มขึ้นทีละเท่ากัน ห้ามไล่คิดทีละพจน์ ให้หา<b>ความยาวของวงรอบ</b>ก่อน '
        'แล้วเอาจำนวนพจน์ตั้งหารด้วยความยาววงรอบ ⇒ เขียน $n = 4q + r$ ให้เห็นกับตา '
        'แล้วคิดเฉพาะ $r$ พจน์ท้ายเท่านั้น · ขั้นตอนหาเศษนี้แหละที่คนมักข้าม',
        '• เงื่อนไขที่เขียนด้วยฟังก์ชันแปลก ๆ อย่าง $\\csc$ , $\\sec$ , $\\cot$ '
        'ให้แปลงกลับเป็น $\\sin$ กับ $\\cos$ ทันทีตั้งแต่บรรทัดแรก '
        'เพราะของที่ตัดกันได้จะโผล่ให้เห็นเองโดยไม่ต้องใช้ไหวพริบอะไรเลย',
        '• ทุกครั้งที่เห็นบรรทัดบอกเครื่องหมายอย่าง $\\sin\\theta < 0$ หรือคำบอกจตุภาค '
        'ให้ขีดเส้นใต้ไว้ทันทีตั้งแต่อ่านโจทย์รอบแรก เพราะมันจะถูกใช้ตอนถอดกรณฑ์ซึ่งอยู่กลางทาง '
        'และเป็นจุดที่ลืมง่ายที่สุด · หลักคิดคือ เอกลักษณ์บอกขนาด เงื่อนไขบอกเครื่องหมาย',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $0$ เพราะเห็นว่าสี่พจน์ติดกันบวกกันได้ศูนย์ แล้วรีบสรุปว่าทั้ง $14$ พจน์หักล้างกันหมด '
        '⇒ ค่านี้ผิดแน่นอน พิสูจน์ได้สองทาง : ทางแรก $14$ หารด้วย $4$ ได้ $3$ เศษ $2$ '
        '⇒ จัดก้อนสี่พจน์ได้เพียง $3$ ก้อน ครอบคลุมแค่พจน์ที่ $1$ ถึงพจน์ที่ $12$ '
        'ยังเหลือพจน์ที่ $13$ กับพจน์ที่ $14$ ที่ไม่มีคู่ · ทางที่สอง ถ้าผลรวมเป็น $0$ จริง '
        'จะต้องได้ $-\\sin\\theta - \\cos\\theta = 0$ นั่นคือ $\\sin\\theta = -\\cos\\theta$ '
        'หรือ $\\tan\\theta = -1$ แต่ข้อนี้ $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta} = '
        '\\dfrac{-\\dfrac{60}{61}}{-\\dfrac{11}{61}} = \\dfrac{60}{11}$ ซึ่งไม่เท่ากับ $-1$ '
        '⇒ ผลรวมเป็นศูนย์ไม่ได้',
        '• ได้ค่า $-71$ เพราะจัดกลุ่มถูกและหาเศษถูกแล้ว แต่จำสูตรลดรูปผิดเป็น '
        '$\\cos\\left(\\theta + \\dfrac{\\pi}{2}\\right) = \\sin\\theta$ (ตกเครื่องหมายลบ) '
        '⇒ สองพจน์ที่เหลือกลายเป็น $\\sin\\theta + \\cos\\theta = -\\dfrac{71}{61}$ ⇒ ตอบ $-71$ · '
        'ค่านี้ผิดแน่นอน ตรวจได้ด้วยการแทนมุมจริงลงไปสักมุม : ให้ $\\theta = \\dfrac{\\pi}{4}$ '
        'จะได้ $\\cos\\left(\\dfrac{\\pi}{4} + \\dfrac{\\pi}{2}\\right) = \\cos\\dfrac{3\\pi}{4} = '
        '-\\dfrac{\\sqrt{2}}{2}$ ในขณะที่ $\\sin\\dfrac{\\pi}{4} = \\dfrac{\\sqrt{2}}{2}$ '
        '⇒ ทั้งสองต่างกันที่เครื่องหมายชัดเจน ⇒ สูตรที่ถูกต้องคือมีลบ · '
        'อีกทางหนึ่งดูจากเครื่องหมายก็พอ : ข้อนี้ $\\sin\\theta$ กับ $\\cos\\theta$ เป็นลบทั้งคู่ '
        '⇒ $-\\sin\\theta$ กับ $-\\cos\\theta$ เป็นบวกทั้งคู่ ⇒ ผลรวมต้องเป็นบวก ไม่มีทางเป็น $-71$',
        '• ได้ค่า $-49$ เพราะข้ามบรรทัด $\\sin\\theta < 0$ ไป แล้วหยิบรากบวก $\\sin\\theta = '
        '\\dfrac{60}{61}$ มาใช้ ⇒ ผลรวมกลายเป็น $-\\dfrac{60}{61} + \\dfrac{11}{61} = -\\dfrac{49}{61}$ '
        '⇒ ตอบ $-49$ · ค่านี้ผิดแน่นอน เพราะค่าดังกล่าวมาจากมุมในจตุภาคที่ $2$ ซึ่งมี $\\sin\\theta > 0$ '
        'ขัดกับเงื่อนไขที่โจทย์เขียนไว้ตรง ๆ ว่า $\\sin\\theta < 0$ · '
        'น่าสังเกตว่าสาขานี้ยังคงให้ $\\sec\\theta = -\\dfrac{61}{11}$ ได้เหมือนกันทุกประการ '
        '⇒ แปลว่าเงื่อนไขก้อนแรกก้อนเดียวแยกสองสาขานี้ไม่ออก และบรรทัดเรื่องเครื่องหมายคือสิ่งเดียวที่ตัดสิน '
        '⇒ ใครมองข้ามบรรทัดนั้นจะไม่มีทางรู้เลยว่าตัวเองหยิบผิดสาขา',
        '• ได้ค่า $60$ เพราะเริ่มบวกตั้งแต่ $k = 0$ ทั้งที่ตัวนับเริ่มที่ $k = 1$ ⇒ มีพจน์เกินมาหนึ่งพจน์ '
        'คือ $\\cos(\\theta + 0) = \\cos\\theta = -\\dfrac{11}{61}$ ⇒ ผลรวมกลายเป็น '
        '$\\dfrac{71}{61} + \\left(-\\dfrac{11}{61}\\right) = \\dfrac{60}{61}$ ⇒ ตอบ $60$ · '
        'ค่านี้ผิดแน่นอน ตรวจได้จากตัวโจทย์เองว่าเขียน $k$ เริ่มที่ $1$ ไม่ใช่ $0$ '
        '· มองอีกมุมก็ได้ว่าถ้านับ $15$ พจน์ จำนวนพจน์จะกลายเป็น $15 = 4 \\times 3 + 3$ '
        '⇒ เหลือเศษ $3$ พจน์ ไม่ใช่ $2$ พจน์ ⇒ โครงของคำตอบเปลี่ยนไปคนละแบบ '
        '⇒ วิธีกันพลาดคืออ่านขอบล่างกับขอบบนของเครื่องหมายผลรวมให้ชัดก่อนลงมือทุกครั้ง',
    ],
    'V.mold: G = a real number theta pinned down by one compound ratio condition csc(theta)/cot(theta) = '
    '-61/11, guarded by the two non-vanishing clauses sin(theta) != 0 and cos(theta) != 0, and disambiguated '
    'by the single sign clause sin(theta) < 0 / A = the numerical value of 61 times a fourteen-term sum of '
    'cosines whose arguments march forward in steps of exactly a quarter turn, asked as a free numeric '
    'response with no candidate values on the page / M = M-PERIOD-FOUR-BLOCK-CANCEL-WITH-REMAINDER, that is: '
    'rewrite the ratio in sines and cosines so that the sine cancels and the condition collapses to '
    'sec(theta) = -61/11 and hence cos(theta) = -11/61, use the Pythagorean identity to get sin(theta) up to '
    'sign and let the sign clause choose the negative root -60/61, then notice that the summand repeats with '
    'a cycle of four because each step is a quarter turn, that any four consecutive terms add to zero because '
    'the first cancels the third and the second cancels the fourth, that 14 = 4*3 + 2 so only the thirteenth '
    'and fourteenth terms survive, fold those two back with the period 2*pi to -sin(theta) and -cos(theta), '
    'and finally multiply the surviving 71/61 by the outer 61. '
    'Rubric F3 C3 P3 T3 L0 = 12/15, which reaches the threshold of 12 with T = 3, so the very-hard band is '
    'entered -> level: ยากมาก. F = 3 because five separate pieces of knowledge have to be held at once and '
    'none may be dropped: the reciprocal definitions of csc, sec and cot, the division rule for a fraction '
    'over a fraction, the Pythagorean identity together with the fact that it fixes only the magnitude of the '
    'sine, the four quarter-turn reduction formulas in their correct signs, and the periodicity of cosine '
    'used to fold an argument that has run past three full turns. C = 3 because the item welds four '
    'independent conditions into one chain in which every link eats the output of the previous one: the ratio '
    'condition produces the cosine, the cosine plus the sign clause produces the sine, the structure of the '
    'summand produces the two surviving terms, and only then do the sine and cosine values become usable '
    'numbers; removing any single link leaves the item unsolvable. P = 3 because the written trail is long '
    'even though no single step is heavy: the ratio has to be collapsed, a square root of 3600/3721 has to be '
    'taken, all fourteen terms have to be accounted for, two of them have to be reduced modulo 2*pi '
    'separately, and the outer factor has to be applied at the end, and the independent check writes every '
    'one of the fourteen terms out as an explicit fraction. T = 3 because three independent hidden turning '
    'points must all be found before a correct number appears: first that 14 is not a multiple of 4 so that '
    'the pleasing observation that four consecutive terms vanish is a trap unless the remainder is computed, '
    'second that the ratio condition alone leaves two quadrant branches which give different answers so the '
    'sign clause is load-bearing rather than decorative, and third that the summation index starts at 1 and '
    'not at 0, which is exactly the difference between a remainder of two and a remainder of three. L = 0 '
    'because the statement is purely symbolic, carries no real-world scene, no figure and no picture that the '
    'reader would have to build in the head; every quantity can be substituted the moment it is read. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): in the q158 block, simplify(Add(*[cos(x + k*pi/2) for k in range(1, 15)])) '
    'returns exactly -sin(x) - cos(x), so the fourteen-term collapse is machine-proved as an identity in x '
    'rather than argued from a picture. The branch bookkeeping was then checked rather than assumed: '
    'solveset(Eq(csc(th)/cot(th), Rational(-61, 11)), th, Interval.Ropen(0, 2*pi)) returns exactly two '
    'solutions, namely atan(60/11) + pi with sin = -60/61 and cos = -11/61, and pi - atan(60/11) with '
    'sin = 60/61 and cos = -11/61; filtering by sin < 0 leaves exactly one survivor, and '
    '61*Add(*[cos(t + k*pi/2) for k in range(1, 15)]) on that survivor evaluates to exactly 71, which is the '
    'stored answer and passes the rational check. The triple was confirmed by 11**2 + 60**2 == 61**2, that '
    'is 121 + 3600 == 3721. Every error path in the pitfalls block was computed by machine rather than '
    'invented: the all-cancel claim would need sin + cos = 0, that is tan = -1, whereas the machine reports '
    'tan = 60/11 on the surviving branch, so 0 is impossible; flipping the sign of the quarter-turn formula '
    'gives 61*(sin + cos) = -71; the rejected branch, which is precisely what dropping the clause sin < 0 '
    'produces, evaluates to -49 and was read straight off the second solveset root rather than constructed by '
    'hand; and running the index from k = 0 gives simplify(Add(*[cos(x + k*pi/2) for k in range(0, 15)])) = '
    '-sin(x), whose value is 60, matching the off-by-one story exactly. '
    'Collision sweep on 6457 de-duplicated items (86 files: the bank sets directory plus k1 out plus k2 out), '
    'probe executed directly in this session because no collide_b21.py exists in the tree yet: a question '
    'text carrying an argument of the form theta + k*pi/2 returns 0 items, a question text carrying a cosine '
    'of theta plus something returns 0 items, and a sigma sum living in any chapter 7 subtopic returns only 5 '
    'items, none of which sums a trigonometric function over a quarter-turn shift, the nearest being '
    'pat1-2553-07-q29 which forms a ratio of two sums of cosines and sines over whole degrees and is solved '
    'by a sum-to-product pairing, a different A and a different M. The ratio csc over cot returns 4 items in '
    'the whole corpus and none of them divides one by the other: chap-06-matrix-q107 is a determinant, '
    'pat1-2555-03-q40 is a limit, pat1-2559-10-q11 is a half-angle product and pat1-2563-02-q37 is a '
    'quotient of a different shape whose mechanism is a Pythagorean simplification. Two deliberate WATCH '
    'entries are logged because they share surface with this item and nothing more: '
    'gen-chap-07-trigonometry-q022 hands over tan = 7/24 with sin < 0 and asks for 25(sin + cos), and '
    'gen-chap-07-trigonometry-q137 hands over the absolute value of a cosine with a product sign condition '
    'and asks for 29(sin - cos); both share the habit of scaling a combination of sine and cosine by the '
    'hypotenuse of the underlying triple and both use the sign clause to pick a quadrant, but in both the '
    'thing being scaled is a bare two-term combination read straight off the reference triangle, whereas here '
    'the thing being scaled is a fourteen-term sum whose value only appears after a cycle length and a '
    'remainder have been found, so A and M both differ while only G stays close. The pair of a shifted '
    'argument and a reduction formula returns 3 items, of which chap-07-trigonometry-q21 is the closest, and '
    'it applies a reduction to two isolated terms rather than to a sum whose length has to be divided by the '
    'cycle. Since this is a fill item there is no choice list, so no answer slot exists and nothing about the '
    'answer could have been positioned by hand.',
)

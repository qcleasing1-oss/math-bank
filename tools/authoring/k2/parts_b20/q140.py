# -*- coding: utf-8 -*-
add(
    140,
    ['7.3'],
    'ปานกลาง',
    'กำหนดให้ $f(x) = 4\\sin\\left(x + \\dfrac{\\pi}{6}\\right)\\cos\\left(x - \\dfrac{\\pi}{3}\\right) + 1$ '
    'สำหรับทุกจำนวนจริง $x$ ผลบวกของค่าสูงสุดและค่าต่ำสุดของ $f$ เท่ากับข้อใด',
    [
        '$-2$',
        '$2$',
        '$4$',
        '$6$',
    ],
    3,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• <b>เอกลักษณ์โคฟังก์ชัน</b> : $\\cos\\theta = \\sin\\left(\\dfrac{\\pi}{2} - \\theta\\right)$ '
        'ทุกค่าของ $\\theta$ · ที่มาของมันคือในรูปสามเหลี่ยมมุมฉาก มุมแหลมสองมุมรวมกันได้ '
        '$\\dfrac{\\pi}{2}$ เสมอ ด้านที่เป็น “ด้านประชิด” ของมุมหนึ่ง จึงเป็น “ด้านตรงข้าม” '
        'ของอีกมุมหนึ่งพอดี ⇒ $\\cos$ ของมุมหนึ่งกับ $\\sin$ ของมุมที่เหลือจึงเป็นจำนวนเดียวกัน '
        'และเมื่อขยายไปยังวงกลมหนึ่งหน่วยก็ยังจริงสำหรับทุกจำนวนจริง ไม่จำกัดแค่มุมแหลม',
        '• <b>มุมที่รวมกันได้สองมุมฉาก</b> : $\\sin(\\pi - \\theta) = \\sin\\theta$ '
        'เพราะบนวงกลมหนึ่งหน่วย จุดปลายของมุม $\\theta$ กับจุดปลายของมุม $\\pi - \\theta$ '
        'สะท้อนกันข้ามแกนตั้ง ⇒ พิกัด $y$ ซึ่งก็คือค่า $\\sin$ เท่ากันทั้งคู่ '
        '(ส่วนพิกัด $x$ กลับเครื่องหมาย จึงทำให้ $\\cos$ กลับเครื่องหมาย แต่ข้อนี้ใช้เฉพาะ $\\sin$)',
        '• เรนจ์ของไซน์ : ค่า $\\sin$ ของจำนวนจริงใด ๆ คือพิกัด $y$ ของจุดบนวงกลมหนึ่งหน่วย '
        'ซึ่งวิ่งได้ตลอดช่วง $[-1, 1]$ และไปถึงปลายทั้งสองข้างได้จริง ⇒ ถ้า $u = \\sin(\\text{อะไรก็ตาม})$ '
        'แล้ว $u$ กวาดครบทั้งช่วง $[-1, 1]$ ไม่ขาดค่าใดเลยเมื่อ $x$ วิ่งทั่วจำนวนจริง',
        '• ⭐ <b>ผลของการยกกำลังสอง</b> : ถ้า $u \\in [-1, 1]$ แล้ว $u^2 \\in [0, 1]$ '
        '⛔ ไม่ใช่ $[-1, 1]$ · เหตุผลคือกำลังสองของจำนวนจริงเป็นลบไม่ได้ ⇒ พื้นล่างถูกยกจาก $-1$ '
        'ขึ้นมาเป็น $0$ โดยค่า $0$ เกิดตอน $u = 0$ และค่า $1$ เกิดตอน $u = 1$ หรือ $u = -1$ '
        '⇒ ปลายบนไม่เปลี่ยน แต่ปลายล่างเปลี่ยน นี่คือจุดที่พลาดกันมากที่สุดของโจทย์แนวนี้',
        '• การส่งเรนจ์ผ่านฟังก์ชันเชิงเส้น : ถ้า $v \\in [m, M]$ และ $a > 0$ '
        'แล้ว $av + b \\in [am + b,\\ aM + b]$ เพราะการคูณด้วยจำนวนบวกไม่สลับลำดับของอสมการ '
        'และการบวกค่าคงตัวก็เลื่อนทั้งช่วงไปเท่า ๆ กัน ⇒ ปลายล่างยังคงมาจากปลายล่างเสมอ',
        '• ⛔ <b>กับดักเรื่องความเป็นอิสระ</b> : ถ้า $A$ และ $B$ ต่างก็อยู่ในช่วง $[-1, 1]$ '
        'จะสรุปว่า $AB$ มีเรนจ์ $[-1, 1]$ <b>ไม่ได้ทันที</b> ต้องดูก่อนว่า $A$ กับ $B$ '
        'ขยับเป็นอิสระต่อกันจริงหรือไม่ ถ้าทั้งคู่ผูกกับตัวแปรเดียวกัน ค่าที่เป็นไปได้ของ $AB$ '
        'อาจแคบกว่าที่คิดมาก ⇒ ต้องตรวจความสัมพันธ์ระหว่างสองก้อนก่อนเสมอ',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• ฟังก์ชัน $f(x) = 4\\sin\\left(x + \\dfrac{\\pi}{6}\\right)\\cos\\left(x - \\dfrac{\\pi}{3}\\right) + 1$',
        '• นิยามไว้สำหรับทุกจำนวนจริง $x$ ⇒ โดเมนเป็นจำนวนจริงทั้งเส้น ไม่มีการตัดช่วงใด ๆ '
        'ดังนั้นอะไรก็ตามที่ $\\sin$ กับ $\\cos$ ทำได้ตามธรรมชาติ ก็เกิดขึ้นได้ครบในข้อนี้',
        '• สังเกตหน้าตาก่อนลงมือ : ให้เอาอาร์กิวเมนต์ของสองก้อนมาลบกันก่อนทำอย่างอื่น '
        '$\\left(x + \\dfrac{\\pi}{6}\\right) - \\left(x - \\dfrac{\\pi}{3}\\right) '
        '= \\dfrac{\\pi}{6} + \\dfrac{\\pi}{3} = \\dfrac{\\pi}{2}$ '
        '⇒ ตัว $x$ ตัดกันหมด เหลือผลต่างเป็นค่าคงตัว $\\dfrac{\\pi}{2}$ พอดี '
        '⇒ นี่คือลายเซ็นของ<b>คู่โคฟังก์ชัน</b> แปลว่าสองวงเล็บนี้ไม่ได้ขยับเป็นอิสระต่อกันเลย',
        '• สังเกตอีกอย่าง : โจทย์ไม่ได้กำหนดช่วงของ $x$ และไม่ได้ให้ค่าใดมาแทน '
        '⇒ งานทั้งหมดคือเรื่องเรนจ์ล้วน ๆ ไม่ใช่การแทนค่า',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าสูงสุดของ $f$ และค่าต่ำสุดของ $f$ แล้วนำมาบวกกัน ตอบเป็นตัวเลขค่าเดียว',
        '',
        '<b>【 ใช้โคฟังก์ชันพิสูจน์ว่าสองวงเล็บคือจำนวนเดียวกันทุกค่า $x$ '
        'จนผลคูณยุบเหลือกำลังสองก้อนเดียว แล้วอ่านเรนจ์จากช่วงของกำลังสอง '
        'ซึ่งมีพื้นเป็น $0$ ไม่ใช่ $-1$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · เปลี่ยนก้อน $\\cos$ ให้กลายเป็น $\\sin$ ด้วยเอกลักษณ์โคฟังก์ชัน</b>',
        '• สูตรที่ใช้ : $\\cos\\theta = \\sin\\left(\\dfrac{\\pi}{2} - \\theta\\right)$',
        '• ระบุตัวแปรให้ชัดก่อนแทนค่า : ก้อนที่จะแปลงคือ $\\cos\\left(x - \\dfrac{\\pi}{3}\\right)$ '
        '⇒ เทียบกับสูตรได้ $\\theta = x - \\dfrac{\\pi}{3}$',
        '• แทนค่า : $\\cos\\left(x - \\dfrac{\\pi}{3}\\right) '
        '= \\sin\\left(\\dfrac{\\pi}{2} - \\left(x - \\dfrac{\\pi}{3}\\right)\\right)$',
        '• ยุบข้างใน : กระจายเครื่องหมายลบเข้าวงเล็บก่อน ได้ '
        '$\\dfrac{\\pi}{2} - x + \\dfrac{\\pi}{3}$ '
        'แล้วรวมค่าคงตัวโดยทำส่วนให้เท่ากันเป็น $6$ : '
        '$\\dfrac{\\pi}{2} + \\dfrac{\\pi}{3} = \\dfrac{3\\pi}{6} + \\dfrac{2\\pi}{6} = \\dfrac{5\\pi}{6}$',
        '• สรุปขั้นนี้ : $\\cos\\left(x - \\dfrac{\\pi}{3}\\right) = \\sin\\left(\\dfrac{5\\pi}{6} - x\\right)$',
        '',
        '<b>ขั้นที่ 2 · พลิกอาร์กิวเมนต์ด้วยสูตรมุมที่รวมกันได้สองมุมฉาก</b>',
        '• สูตรที่ใช้ : $\\sin(\\pi - \\theta) = \\sin\\theta$ ซึ่งอ่านย้อนทางได้ว่า '
        '$\\sin\\theta = \\sin(\\pi - \\theta)$',
        '• ระบุตัวแปร : คราวนี้ $\\theta = \\dfrac{5\\pi}{6} - x$ ซึ่งเป็นผลจากขั้นที่ 1',
        '• แทนค่า : $\\sin\\left(\\dfrac{5\\pi}{6} - x\\right) '
        '= \\sin\\left(\\pi - \\left(\\dfrac{5\\pi}{6} - x\\right)\\right)$',
        '• ยุบข้างใน : $\\pi - \\dfrac{5\\pi}{6} + x = \\dfrac{6\\pi}{6} - \\dfrac{5\\pi}{6} + x '
        '= \\dfrac{\\pi}{6} + x$',
        '• ⭐ <b>กุญแจของข้อนี้โผล่ตรงนี้</b> : รวมสองขั้นเข้าด้วยกันได้ '
        '$\\cos\\left(x - \\dfrac{\\pi}{3}\\right) = \\sin\\left(x + \\dfrac{\\pi}{6}\\right)$ '
        '<b>ทุกค่าของ $x$</b> ⇒ สองวงเล็บในโจทย์ไม่ใช่ของสองชิ้นที่ขยับอิสระต่อกัน '
        'แต่เป็นจำนวนเดียวกันเป๊ะ ๆ',
        '• ตรวจความสมเหตุสมผลของกุญแจแบบเร็ว ๆ ด้วยการแทน $x = 0$ : '
        'ฝั่งซ้าย $\\cos\\left(-\\dfrac{\\pi}{3}\\right) = \\dfrac{1}{2}$ '
        'และฝั่งขวา $\\sin\\dfrac{\\pi}{6} = \\dfrac{1}{2}$ ⇒ เท่ากันจริง ✓',
        '',
        '<b>ขั้นที่ 3 · ยุบ $f$ ให้เหลือกำลังสองก้อนเดียว แล้วอ่านเรนจ์</b>',
        '• แทนผลของขั้นที่ 2 กลับเข้าไปในฟังก์ชันเดิม : '
        '$f(x) = 4\\sin\\left(x + \\dfrac{\\pi}{6}\\right) \\cdot '
        '\\sin\\left(x + \\dfrac{\\pi}{6}\\right) + 1$',
        '• ยุบ : ก้อนเดียวกันคูณกันเองคือกำลังสอง ⇒ '
        '$f(x) = 4\\sin^2\\left(x + \\dfrac{\\pi}{6}\\right) + 1$',
        '• ตั้งตัวแปรช่วยเพื่ออ่านเรนจ์ให้ง่าย : ให้ $u = \\sin\\left(x + \\dfrac{\\pi}{6}\\right)$ '
        '⇒ $f = 4u^2 + 1$ · เมื่อ $x$ วิ่งทั่วจำนวนจริง อาร์กิวเมนต์ $x + \\dfrac{\\pi}{6}$ '
        'ก็วิ่งทั่วจำนวนจริงเช่นกัน ⇒ $u$ กวาดครบช่วง $[-1, 1]$',
        '• 📌 <b>จุดพลิกของข้อนี้</b> : ยกกำลังสองแล้ว $u^2$ มีช่วงเป็น $[0, 1]$ '
        'ไม่ใช่ $[-1, 1]$ เพราะกำลังสองเป็นลบไม่ได้ ⇒ พื้นล่างคือ $0$ ⛔ ไม่ใช่ $-1$',
        '• ส่งช่วงผ่านฟังก์ชันเชิงเส้น $4v + 1$ โดย $v = u^2 \\in [0, 1]$ และสัมประสิทธิ์ $4$ เป็นบวก '
        '⇒ ปลายล่าง $4(0) + 1 = 1$ · ปลายบน $4(1) + 1 = 5$ ⇒ $f \\in [1, 5]$',
        '',
        '<b>ขั้นที่ 4 · ยืนยันว่าปลายทั้งสองไปถึงได้จริง แล้วบวกกัน</b>',
        '• ปลายบนไปถึงได้จริงหรือไม่ ต้องมี $x$ ที่ทำให้ $u^2 = 1$ : '
        'เลือก $x + \\dfrac{\\pi}{6} = \\dfrac{\\pi}{2}$ ⇒ $x = \\dfrac{\\pi}{2} - \\dfrac{\\pi}{6} '
        '= \\dfrac{\\pi}{3}$ ซึ่งเป็นจำนวนจริง ⇒ ค่าสูงสุดของ $f$ คือ $5$',
        '• ปลายล่างไปถึงได้จริงหรือไม่ ต้องมี $x$ ที่ทำให้ $u = 0$ : '
        'เลือก $x + \\dfrac{\\pi}{6} = 0$ ⇒ $x = -\\dfrac{\\pi}{6}$ ซึ่งเป็นจำนวนจริงเช่นกัน '
        '(หรือจะเลือก $x = \\dfrac{5\\pi}{6}$ ก็ได้ค่าเดียวกัน) ⇒ ค่าต่ำสุดของ $f$ คือ $1$',
        '• การตรวจว่า “ไปถึงได้จริง” สำคัญ เพราะถ้าปลายใดปลายหนึ่งไปไม่ถึง '
        'ค่านั้นจะเป็นเพียงขอบเขต ไม่ใช่ค่าสูงสุดหรือค่าต่ำสุดที่แท้จริง',
        '• สิ่งที่โจทย์ถามคือผลบวกของทั้งสองค่า : $5 + 1 = 6$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่า $x$ จริงลงในนิพจน์ต้นฉบับ '
        'โดยไม่แตะเอกลักษณ์โคฟังก์ชันเลยแม้แต่ก้าวเดียว)</b>',
        '• เส้นทางข้างบนพึ่งการยุบสองวงเล็บให้เป็นก้อนเดียว การตรวจรอบนี้จะไม่ยุบอะไรทั้งสิ้น '
        'แต่จะหยิบค่า $x$ ที่ควรทำให้เกิดค่าสุดขีดมาแทนลงในสูตรเดิมตรง ๆ '
        'ถ้าได้ $5$ กับ $1$ ออกมาจริง แปลว่าปลายทั้งสองของเรนจ์ถูกต้อง',
        '• แทน $x = \\dfrac{\\pi}{3}$ ลงในนิพจน์เดิม : '
        '$\\sin\\left(\\dfrac{\\pi}{3} + \\dfrac{\\pi}{6}\\right) = \\sin\\dfrac{\\pi}{2} = 1$ '
        'และ $\\cos\\left(\\dfrac{\\pi}{3} - \\dfrac{\\pi}{3}\\right) = \\cos 0 = 1$ '
        '⇒ $f = 4(1)(1) + 1 = 5$ ✓ ตรงกับค่าสูงสุดที่หาไว้',
        '• แทน $x = -\\dfrac{\\pi}{6}$ : '
        '$\\sin\\left(-\\dfrac{\\pi}{6} + \\dfrac{\\pi}{6}\\right) = \\sin 0 = 0$ '
        '⇒ ผลคูณทั้งก้อนเป็น $0$ ไม่ว่าตัว $\\cos$ จะเป็นเท่าใด ⇒ $f = 0 + 1 = 1$ ✓ '
        'ตรงกับค่าต่ำสุดที่หาไว้',
        '• ลองจุดกลางเพื่อดูว่าค่าไม่หลุดขอบ — แทน $x = 0$ : '
        '$4\\sin\\dfrac{\\pi}{6}\\cos\\left(-\\dfrac{\\pi}{3}\\right) + 1 '
        '= 4\\left(\\dfrac{1}{2}\\right)\\left(\\dfrac{1}{2}\\right) + 1 = 2$ '
        'ซึ่งอยู่ระหว่าง $1$ กับ $5$ ✓',
        '• ลองอีกจุดหนึ่งให้มั่นใจ — แทน $x = \\dfrac{\\pi}{6}$ : '
        '$4\\sin\\dfrac{\\pi}{3}\\cos\\left(-\\dfrac{\\pi}{6}\\right) + 1 '
        '= 4\\left(\\dfrac{\\sqrt{3}}{2}\\right)\\left(\\dfrac{\\sqrt{3}}{2}\\right) + 1 = 3 + 1 = 4$ '
        'ซึ่งก็ยังอยู่ในช่วง $[1, 5]$ ✓',
        '• ปิดเพดานอีกชั้นด้วยการประมาณอย่างหยาบ : ค่าของ $\\sin$ และ $\\cos$ '
        'ต่างก็ไม่เกิน $1$ ในค่าสัมบูรณ์ ⇒ $4\\sin(\\cdot)\\cos(\\cdot) + 1 \\le 4(1)(1) + 1 = 5$ เสมอ '
        'และเพิ่งเห็นแล้วว่า $x = \\dfrac{\\pi}{3}$ แตะเพดานนั้นได้พอดี '
        '⇒ ยืนยันว่า $5$ เป็นค่าสูงสุดจริง ไม่ใช่แค่ขอบเขตลอย ๆ',
        '• ไล่ค่า $x$ ต่อเนื่องตลอดหนึ่งคาบก็ได้ภาพเดียวกัน คือค่าต่ำสุดที่พบคือ $1$ '
        'และค่าสูงสุดที่พบคือ $5$ ไม่มีจุดใดต่ำกว่า $1$ เลย ⇒ ผลบวก $5 + 1 = 6$ ✓',
        '',
        '✅ <b>คำตอบ</b> ค่าสูงสุดของ $f$ คือ $5$ และค่าต่ำสุดของ $f$ คือ $1$ '
        'ผลบวกของทั้งสองค่าจึงเท่ากับ $6$ → <b>ตัวเลือก 4</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เห็นผลคูณของ $\\sin$ กับ $\\cos$ ที่อาร์กิวเมนต์เป็นเชิงเส้นใน $x$ ทั้งคู่ '
        'ให้<b>ลบอาร์กิวเมนต์กันก่อนเสมอ</b> ถ้าผลต่างออกมาเป็น $\\dfrac{\\pi}{2}$ '
        'แปลว่าเป็นคู่โคฟังก์ชัน ยุบเป็นกำลังสองได้ทันทีโดยไม่ต้องกางสูตรผลคูณเป็นผลบวกให้เสียเวลา '
        'ส่วนกรณีผลต่างเป็น $0$ ก็ยุบได้เช่นกัน ⇒ ผลต่างของอาร์กิวเมนต์คือสิ่งแรกที่ต้องดู',
        '• เวลาหาเรนจ์ของนิพจน์ที่มีก้อนตรีโกณอยู่ข้างใน ให้ตั้งตัวแปรใหม่แทนก้อนนั้น '
        'เช่น $u = \\sin(\\cdot)$ แล้วเปลี่ยนโจทย์เป็นเรื่องพีชคณิตล้วนของ $u$ '
        'จะเห็นชัดขึ้นมากว่าปลายบนกับปลายล่างมาจากค่า $u$ ใด และช่วยกันพลาดเรื่องเครื่องหมาย',
        '• ก่อนวงคำตอบให้แทนค่าง่าย ๆ อย่าง $x = 0$ ลงในสูตร<b>เดิม</b>เสมอ '
        'ถ้าค่าที่ได้หลุดออกนอกช่วงที่เพิ่งสรุปไป แปลว่าคิดพลาดแน่นอนโดยไม่ต้องตรวจอย่างอื่นเลย '
        'ข้อนี้แทน $x = 0$ ได้ $2$ ซึ่งอยู่ใน $[1, 5]$ พอดี',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ถ้าได้ค่า $-2$ แปลว่าจำเอกลักษณ์โคฟังก์ชันกลับเครื่องหมาย '
        'คือไปเขียนว่า $\\cos\\left(x - \\dfrac{\\pi}{3}\\right) = -\\sin\\left(x + \\dfrac{\\pi}{6}\\right)$ '
        '⇒ $f = 1 - 4\\sin^2\\left(x + \\dfrac{\\pi}{6}\\right)$ ⇒ เรนจ์กลายเป็น $[-3, 1]$ '
        '⇒ ผลบวก $1 + (-3) = -2$ · ค่านี้ผิดแน่นอน พิสูจน์ได้ด้วยการแทน $x = \\dfrac{\\pi}{3}$ '
        'ลงในสูตรเดิม ซึ่งให้ $f = 5$ เป็นบวก แต่เส้นทางนี้ทำนายว่าค่าที่จุดนั้นต้องเป็น $-3$ '
        '⇒ ขัดกันเอง · ที่มาของความผิดคือลืมว่าอาร์กิวเมนต์ทั้งสองต่างกัน '
        '$\\dfrac{\\pi}{2}$ แบบ “บวก” ไม่ใช่แบบที่ต้องพลิกเครื่องหมาย',
        '• ถ้าได้ค่า $2$ แปลว่ามองว่าสองวงเล็บขยับเป็นอิสระต่อกัน จึงคิดว่า '
        '$\\sin$ ทำค่าได้ถึง $1$ พร้อมกับที่ $\\cos$ ทำค่าได้ถึง $1$ และก็ทำค่าได้ถึง $-1$ '
        'พร้อมกันได้ด้วย ⇒ ผลคูณ $4\\sin(\\cdot)\\cos(\\cdot)$ ถูกเดาว่ามีช่วง $[-4, 4]$ '
        '⇒ $f$ มีช่วง $[-3, 5]$ ⇒ ผลบวก $5 + (-3) = 2$ · ปลายบนบังเอิญถูก แต่ปลายล่างผิด '
        'เพราะเมื่อทั้งสองก้อนเป็นจำนวนเดียวกัน ผลคูณคือกำลังสอง ซึ่งเป็นลบไม่ได้เลย '
        '⇒ ค่า $-3$ ไม่มีทางเกิดขึ้น ยืนยันได้ว่าไม่มี $x$ ใดให้ $f$ ต่ำกว่า $1$',
        '• ถ้าได้ค่า $4$ มีสองเส้นทางที่ไปโผล่ตรงนั้น · เส้นทางแรก ยุบเป็น '
        '$4\\sin^2\\left(x + \\dfrac{\\pi}{6}\\right)$ ถูกต้องแล้ว แต่ลืมบวก $1$ ทั้งสองปลาย '
        '⇒ อ่านค่าสูงสุดเป็น $4$ และค่าต่ำสุดเป็น $0$ ⇒ ผลบวก $4 + 0 = 4$ · '
        'เส้นทางที่สอง ได้เรนจ์ $[1, 5]$ ถูกต้องแล้ว แต่ตอบ<b>ผลต่าง</b>แทนผลบวก คือ $5 - 1 = 4$ · '
        'ทั้งสองเส้นทางผิด ตรวจจับได้ด้วยการแทน $x = \\dfrac{\\pi}{3}$ ลงในสูตรเดิม '
        'ซึ่งให้ $f = 5$ ไม่ใช่ $4$ ⇒ ค่าคงตัว $+1$ ยังอยู่ครบ และคำที่โจทย์ใช้คือ “ผลบวก”',
        '• อีกเส้นทางที่พลาดกันบ่อยคือเผลอสรุปว่า $u^2$ มีช่วงเป็น $[-1, 1]$ ตามช่วงของ $u$ '
        'โดยลืมว่ากำลังสองยกพื้นล่างขึ้นมาเป็น $0$ · ถ้าคิดแบบนั้นจะได้ $f \\in [-3, 5]$ '
        'ซึ่งไปชนค่า $2$ พอดี · สัญญาณเตือนคือค่าที่จะตอบบอกว่ามี $x$ บางค่าทำให้ $f$ ติดลบ '
        'แต่ $f$ เขียนได้เป็นจำนวนที่ไม่เป็นลบบวกกับ $1$ จึงไม่มีทางต่ำกว่า $1$ ได้เลย',
    ],
    'V.mold: G = a single trigonometric function of one real variable, f(x) = 4 sin(x + pi/6) cos(x - '
    'pi/3) + 1, handed over as a product of a sine and a cosine whose arguments are both linear in x and '
    'differ by exactly pi/2, with the domain stated as all real numbers / A = the sum of the maximum '
    'value and the minimum value of f / M = apply the cofunction identity cos(t) = sin(pi/2 - t) and then '
    'the supplementary identity sin(pi - t) = sin(t) to prove the two brackets denote the same number for '
    'every x, collapse the product into 4 sin^2(x + pi/6) + 1, and read the range off the square, whose '
    'floor is 0 rather than -1. '
    'Rubric F2 C1 P2 T2 L0 = 7/15 with the total landing in the 3 to 7 band and T no higher than 2 '
    '-> level: ปานกลาง. '
    'F = 2 because two distinct identity facts are needed before any range work can start, the '
    'cofunction identity and the supplementary-angle identity, and neither of them alone finishes the '
    'collapse. C = 1 because identity manipulation has to be joined to range reasoning, a real crossing '
    'between two different kinds of work, but shallow in the sense that once the collapse is done the '
    'range step is a single standard reading of a square. P = 2 because the work runs in two stages of '
    'different kinds: the first stage rewrites the cosine bracket twice to expose the merge, and only '
    'after the expression has become 4u^2 + 1 can the second stage push the interval through and verify '
    'that both endpoints are attained. T = 2 for the hidden condition that carries the whole item, that '
    'the two brackets are not independent factors but one and the same number, together with the second '
    'trap that squaring lifts the floor from -1 to 0; T was held at 2 and not raised to 3 because the '
    'difference of the arguments is visible on the surface and a solver who habitually subtracts the '
    'arguments meets the merge immediately, with no case split and no boundary discussion needed. '
    'L = 0 because the item is pure symbolic work with no figure to picture and no worded situation to '
    'model, so the statement can be substituted into directly. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b20.py): simplify(cos(x - pi/3) - sin(x + pi/6)) returns 0, which certifies the merge '
    'as an identity over the reals rather than at sampled points, and '
    'simplify(expand_trig(f - (4*sin(x + pi/6)**2 + 1))) also returns 0, so the collapsed form is exact. '
    'maximum(f, x, Reals) returns 5, minimum(f, x, Reals) returns 1, and their sum returns 6. Every '
    'error path was machine-computed from a named mistake instead of being invented: the sign-flipped '
    'cofunction gives 1 - 4*sin(x + pi/6)**2, whose maximum is 1 and minimum is -3 for a sum of -2; '
    'treating the two brackets as independent puts the product in [-4, 4] and f in [-3, 5] for a sum of '
    '2; dropping the constant +1 after a correct collapse leaves 4 and 0 for a sum of 4, and the same '
    'value 4 is returned by the second path that reports the difference 5 - 1 instead of the sum. The '
    'independent check was machine-verified as well: f(pi/3) evaluates to 5, f(-pi/6) evaluates to 1, '
    'f(0) evaluates to 2, f(pi/6) evaluates to 4, and a numerical sweep of x across a full period at a '
    'step of a tenth of a degree returns a smallest value of 1 attained at 150 degrees and a largest '
    'value of 5 attained at 60 degrees, with nothing outside [1, 5]. '
    'Collision sweep on 6437 items (bank 63 files + k1 out + k2 out), probe collide_b20.py / '
    'collide_b20b.py: the phrase asking for the sum of a maximum and a minimum returns 4 items across '
    'the whole corpus and none of them sits in the trigonometry chapter, the nearest being an absolute '
    'value function on a closed interval and a linear programming item. Inside the trigonometry chapter '
    'the scan for maximum or minimum or range language returns 11 items, and every one of them is a '
    'different mechanism: a quadratic in sin x, a reciprocal of an affine sine, an amplitude and shift '
    'reading off a sin(bx) + c template, a sum of squared inverse functions, and a plain affine cosine. '
    'The scan for a product of a sine and a cosine whose arguments are both linear in x returns 0 items, '
    'so the merge that defines this item is unused in the corpus, and no saturated mold is touched since '
    'the collapse is a cofunction merge rather than a product-to-sum expansion or a double-angle '
    'rewrite. Choices are ordered ascending by numeric value (-2, then 2, then 4, then 6), so the answer '
    'slot is forced by that rule and was not chosen.',
)

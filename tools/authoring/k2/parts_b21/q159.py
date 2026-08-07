# -*- coding: utf-8 -*-
add(
    159,
    ['7.3'],
    'ง่าย',
    'ข้อใดเป็นฟังก์ชันคี่ นั่นคือสอดคล้องกับ $f(-x) = -f(x)$ '
    'สำหรับทุกจำนวนจริง $x$ ในโดเมนของฟังก์ชันนั้น',
    [
        '$f(x) = \\cos 2x$',
        '$f(x) = \\left|\\sin x\\right|$',
        '$f(x) = \\sin x\\cos x$',
        '$f(x) = 1 + \\sin x$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• <b>ฟังก์ชันคี่กับฟังก์ชันคู่ คือคำที่บอกว่าเกิดอะไรขึ้นเมื่อเปลี่ยน $x$ เป็น $-x$</b> : '
        'ฟังก์ชัน $f$ เป็น<b>ฟังก์ชันคี่</b> เมื่อ $f(-x) = -f(x)$ สำหรับทุกค่า $x$ ในโดเมน '
        'แปลเป็นภาษาพูดว่า “พลิกอินพุตเป็นลบ แล้วเอาต์พุตพลิกเครื่องหมายตามไปด้วย” '
        'ส่วนฟังก์ชัน $f$ เป็น<b>ฟังก์ชันคู่</b> เมื่อ $f(-x) = f(x)$ สำหรับทุกค่า $x$ ในโดเมน '
        'แปลว่า “พลิกอินพุตเป็นลบ แล้วเอาต์พุตเท่าเดิมไม่กระดิก” '
        'ในภาพกราฟ ฟังก์ชันคี่มีกราฟสมมาตรรอบจุดกำเนิด (หมุนกราฟ $180^{\\circ}$ รอบจุดกำเนิดแล้วทับรูปเดิม) '
        'ส่วนฟังก์ชันคู่มีกราฟสมมาตรรอบแกน $Y$ (พับกระดาษตามแกน $Y$ แล้วทับกันสนิท)',
        '• <b>ยังมีทางที่สามเสมอ คือไม่คู่และไม่คี่</b> : ฟังก์ชันหนึ่งไม่จำเป็นต้องเป็นอย่างใดอย่างหนึ่ง '
        'ถ้าลองแทน $-x$ แล้วผลที่ได้ไม่เท่ากับ $f(x)$ และก็ไม่เท่ากับ $-f(x)$ ด้วย '
        'ฟังก์ชันนั้นก็เป็นฟังก์ชันที่ไม่คู่และไม่คี่ ⇒ เวลาตรวจจึงต้องเทียบผลที่ได้กับ '
        '<b>สองเป้าหมาย</b> คือ $f(x)$ กับ $-f(x)$ ไม่ใช่เป้าหมายเดียว',
        '• <b>ของพื้นฐานสองชิ้นที่ต้องมีติดมือ</b> : $\\sin(-x) = -\\sin x$ '
        '(ไซน์เป็นฟังก์ชันคี่) และ $\\cos(-x) = \\cos x$ (โคไซน์เป็นฟังก์ชันคู่) '
        'ที่มาอ่านได้จากวงกลมหนึ่งหน่วย : มุม $-x$ คือการวัดมุมขนาดเท่ากับมุม $x$ แต่วัดกลับทิศ '
        '⇒ จุดปลายส่วนโค้งของ $-x$ เป็นเงาสะท้อนของจุดปลายส่วนโค้งของ $x$ ข้ามแกน $X$ '
        'การสะท้อนข้ามแกน $X$ ทำให้พิกัดแรกคงเดิมแต่พิกัดที่สองกลับเครื่องหมาย '
        'และพิกัดแรกคือค่า $\\cos$ ส่วนพิกัดที่สองคือค่า $\\sin$ '
        '⇒ $\\cos$ จึงเท่าเดิม และ $\\sin$ จึงกลับเครื่องหมาย',
        '• <b>ค่าสัมบูรณ์กลืนเครื่องหมายทิ้ง</b> : ไม่ว่า $A$ จะเป็นบวกหรือลบ ก็ได้ $\\left|-A\\right| = \\left|A\\right|$ เสมอ '
        'เพราะค่าสัมบูรณ์คือระยะห่างจากศูนย์ ซึ่งไม่มีทางติดลบ '
        '⇒ เครื่องหมายลบที่โผล่ออกมาข้างในเครื่องหมายค่าสัมบูรณ์จะถูกลบทิ้งทันที ออกมาข้างนอกไม่ได้',
        '• <b>กฎเครื่องหมายของผลคูณ</b> : ถ้า $g$ เป็นฟังก์ชันคี่ และ $h$ เป็นฟังก์ชันคู่ '
        'แล้วผลคูณ $g(x)h(x)$ เป็นฟังก์ชันคี่ พิสูจน์ตรง ๆ ได้ว่า '
        '$g(-x)h(-x) = \\left(-g(x)\\right)\\left(h(x)\\right) = -g(x)h(x)$ '
        'นั่นคือมีเครื่องหมายลบตัวเดียวหลุดออกมาหน้าผลคูณ ⇒ ตรงกับนิยามของฟังก์ชันคี่พอดี',
        '• <b>ค่าคงตัวที่ไม่ใช่ศูนย์ทำลายความเป็นคี่</b> : ค่าคงตัวไม่สนใจว่าอินพุตเป็น $x$ หรือ $-x$ '
        'มันจึงไม่ยอมกลับเครื่องหมายตาม ⇒ ตัวตรวจเร็วที่ใช้ได้เสมอคือแทน $x = 0$ '
        'ถ้า $f$ เป็นฟังก์ชันคี่และ $0$ อยู่ในโดเมน จะได้ $f(0) = -f(0)$ ⇒ $2f(0) = 0$ ⇒ $f(0) = 0$ '
        'ดังนั้นฟังก์ชันใดที่ $f(0) \\ne 0$ จะเป็นฟังก์ชันคี่ไม่ได้เลย',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• โจทย์เขียนนิยามของฟังก์ชันคี่มาให้ในตัวแล้ว คือ $f(-x) = -f(x)$ '
        'และย้ำว่าต้องเป็นจริง<b>สำหรับทุกจำนวนจริง</b> $x$ ในโดเมน ไม่ใช่จริงแค่บางค่า',
        '• มีนิพจน์ให้พิจารณาสี่นิพจน์ ได้แก่ $\\cos 2x$ · $\\left|\\sin x\\right|$ · '
        '$\\sin x\\cos x$ · $1 + \\sin x$ ทุกนิพจน์นิยามได้ทุกจำนวนจริง $x$ '
        '⇒ ไม่ต้องกังวลเรื่องโดเมนขาดหาย และไม่ต้องระวังค่าที่ทำให้ตัวส่วนเป็นศูนย์',
        '• สังเกตหน้าตาก่อนลงมือ : สิ่งที่โจทย์ให้มาไม่ใช่ค่าตัวเลข แต่เป็น<b>สูตรของฟังก์ชัน</b> '
        '⇒ สิ่งที่ต้องทำคือแทน $-x$ ลงไปแทนที่ $x$ ทุกจุดในสูตร แล้วดูว่าเครื่องหมายลบหลุดออกมาหน้าสูตรได้หรือไม่ '
        '⛔ ไม่ใช่การแทนตัวเลขค่าใดค่าหนึ่งแล้วรีบสรุป',
        '• สังเกตอีกอย่าง : ทั้งสี่นิพจน์สร้างขึ้นจาก $\\sin$ กับ $\\cos$ เท่านั้น '
        '⇒ ของพื้นฐานสองชิ้น $\\sin(-x) = -\\sin x$ กับ $\\cos(-x) = \\cos x$ '
        'ใช้ได้ครบทุกนิพจน์ ไม่ต้องหาเครื่องมืออื่นเพิ่มอีกเลย',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หานิพจน์ที่เป็นฟังก์ชันคี่จริงตามนิยาม $f(-x) = -f(x)$ '
        'พร้อมแสดงให้เห็นว่าอีกสามนิพจน์ที่เหลือไม่ผ่านนิยามนี้ เพราะเหตุใด',
        '',
        '<b>【 แทน $-x$ ลงไปในนิพจน์ทีละตัว ยุบด้วย $\\sin(-x) = -\\sin x$ และ $\\cos(-x) = \\cos x$ '
        'แล้วเทียบผลที่ได้กับสองเป้าหมายคือ $f(x)$ กับ $-f(x)$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · วางเครื่องมือที่จะใช้ซ้ำทั้งสี่รอบ และวางวิธีอ่านผล</b>',
        '• สูตรที่ใช้ : $\\sin(-x) = -\\sin x$ และ $\\cos(-x) = \\cos x$ ทั้งสองอันเป็นจริงทุกจำนวนจริง $x$',
        '• ระบุตัวแปรให้ชัด : ตัว $x$ ในสูตรเป็นตัวแทนของ “สิ่งที่อยู่ในวงเล็บ” ไม่ใช่ตัวอักษร $x$ เท่านั้น '
        '⇒ เขียนแทนได้ทุกก้อน เช่น $\\cos(-2x) = \\cos 2x$ ก็ได้จากการมองก้อน $2x$ เป็นตัวเดียว',
        '• วิธีอ่านผลหลังแทนค่า : เมื่อได้ผลของ $f(-x)$ ออกมาแล้ว ให้เทียบกับสองเป้าหมาย '
        'ถ้าตรงกับ $-f(x)$ ⇒ เป็นฟังก์ชันคี่ · ถ้าตรงกับ $f(x)$ ⇒ เป็นฟังก์ชันคู่ '
        '· ถ้าไม่ตรงกับทั้งสองอย่าง ⇒ ไม่คู่และไม่คี่',
        '• 📌 เขียน $-f(x)$ ออกมาให้เห็นกับตาก่อนเทียบทุกครั้ง อย่าเทียบในหัว '
        'เพราะจุดที่คนพลาดคือเทียบกับ $f(x)$ อย่างเดียวแล้วเห็นว่า “ไม่เท่า” ก็รีบสรุปว่าเป็นคี่',
        '',
        '<b>ขั้นที่ 2 · ตรวจนิพจน์ $\\cos 2x$</b>',
        '• สูตรที่ใช้ : $\\cos(-A) = \\cos A$ โดยมองก้อน $A$ เป็นตัวเดียว',
        '• ระบุตัวแปร : ที่นี่ $f(x) = \\cos 2x$ ⇒ เมื่อแทน $x$ ด้วย $-x$ '
        'สิ่งที่อยู่ในวงเล็บกลายเป็น $2(-x) = -2x$ ⇒ ก้อน $A$ ของเราคือ $2x$',
        '• แทนค่า : $f(-x) = \\cos\\left(2(-x)\\right) = \\cos(-2x)$',
        '• ยุบ : ใช้ $\\cos(-A) = \\cos A$ กับ $A = 2x$ ได้ $\\cos(-2x) = \\cos 2x$ ⇒ $f(-x) = \\cos 2x$',
        '• เทียบสองเป้าหมาย : $f(x) = \\cos 2x$ ⇒ $f(-x) = f(x)$ ✓ ตรงกับนิยามของ<b>ฟังก์ชันคู่</b> '
        'ส่วน $-f(x) = -\\cos 2x$ ซึ่งไม่เท่ากับ $\\cos 2x$ (ถ้าเท่ากันจะบังคับให้ $\\cos 2x = 0$ ทุกค่า $x$ ซึ่งไม่จริง '
        'เพราะที่ $x = 0$ ได้ $\\cos 0 = 1 \\ne 0$) ⇒ นิพจน์นี้เป็นฟังก์ชันคู่ ⛔ ไม่ใช่ฟังก์ชันคี่',
        '',
        '<b>ขั้นที่ 3 · ตรวจนิพจน์ $\\left|\\sin x\\right|$</b>',
        '• สูตรที่ใช้ : $\\sin(-x) = -\\sin x$ ก่อน แล้วตามด้วยสมบัติค่าสัมบูรณ์ $\\left|-A\\right| = \\left|A\\right|$',
        '• ระบุตัวแปร : ที่นี่ $f(x) = \\left|\\sin x\\right|$ ⇒ ตัวที่อยู่ในเครื่องหมายค่าสัมบูรณ์คือ $\\sin x$ '
        '⇒ ก้อน $A$ ของเราคือ $\\sin x$',
        '• แทนค่า : $f(-x) = \\left|\\sin(-x)\\right| = \\left|-\\sin x\\right|$',
        '• ยุบ : ใช้ $\\left|-A\\right| = \\left|A\\right|$ กับ $A = \\sin x$ ได้ '
        '$\\left|-\\sin x\\right| = \\left|\\sin x\\right|$ ⇒ $f(-x) = \\left|\\sin x\\right|$',
        '• เทียบสองเป้าหมาย : $f(-x) = f(x)$ ✓ ⇒ เป็น<b>ฟังก์ชันคู่</b> '
        '· จุดสำคัญคือเครื่องหมายลบที่ได้มาจาก $\\sin(-x)$ นั้นเกิดขึ้นจริง แต่มันติดอยู่<b>ข้างใน</b>เครื่องหมายค่าสัมบูรณ์ '
        'จึงถูกกลืนหายไป หลุดออกมาหน้านิพจน์ไม่ได้ ⇒ นิพจน์นี้จึงไม่ใช่ฟังก์ชันคี่',
        '• ตรวจซ้ำอีกทางด้วยค่าเดียว : ที่ $x = \\dfrac{\\pi}{2}$ ได้ $f\\left(\\dfrac{\\pi}{2}\\right) = \\left|1\\right| = 1$ '
        'และ $f\\left(-\\dfrac{\\pi}{2}\\right) = \\left|-1\\right| = 1$ '
        'ถ้าเป็นฟังก์ชันคี่ต้องได้ $-1$ ⇒ ขัดกันชัดเจน',
        '',
        '<b>ขั้นที่ 4 · ตรวจนิพจน์ $\\sin x\\cos x$</b>',
        '• สูตรที่ใช้ : $\\sin(-x) = -\\sin x$ และ $\\cos(-x) = \\cos x$ ใช้พร้อมกันทั้งสองตัว '
        'เพราะนิพจน์นี้เป็นผลคูณของสองก้อน',
        '• ระบุตัวแปร : ที่นี่ $f(x) = \\sin x\\cos x$ ⇒ ก้อนแรกคือ $\\sin x$ ซึ่งเป็นฟังก์ชันคี่ '
        '· ก้อนที่สองคือ $\\cos x$ ซึ่งเป็นฟังก์ชันคู่',
        '• แทนค่า : $f(-x) = \\sin(-x)\\cos(-x)$ ⇒ แทนทีละก้อน '
        'ก้อนแรกได้ $\\sin(-x) = -\\sin x$ · ก้อนที่สองได้ $\\cos(-x) = \\cos x$ '
        '⇒ $f(-x) = \\left(-\\sin x\\right)\\left(\\cos x\\right)$',
        '• ยุบ : ดึงเครื่องหมายลบออกมาไว้หน้าผลคูณ '
        '$\\left(-\\sin x\\right)\\left(\\cos x\\right) = -\\sin x\\cos x$ ⇒ $f(-x) = -\\sin x\\cos x$',
        '• เทียบสองเป้าหมาย : $-f(x) = -\\sin x\\cos x$ ⇒ $f(-x) = -f(x)$ ✓ '
        'ตรงกับนิยามของ<b>ฟังก์ชันคี่</b> และตรงทุกจำนวนจริง $x$ เพราะทุกก้าวที่เดินมาเป็นเอกลักษณ์ที่จริงทุกค่า '
        'ไม่ได้อาศัยค่า $x$ ค่าใดค่าหนึ่งเลย ⇒ นิพจน์นี้คือคำตอบ',
        '• อ่านผลด้วยกฎเครื่องหมาย : คี่คูณคู่ได้คี่ ซึ่งตรงกับที่คำนวณมา '
        'เพราะมีเครื่องหมายลบโผล่มาตัวเดียวจากก้อน $\\sin$ ส่วนก้อน $\\cos$ ไม่สร้างเครื่องหมายลบเพิ่ม',
        '',
        '<b>ขั้นที่ 5 · ตรวจนิพจน์ $1 + \\sin x$</b>',
        '• สูตรที่ใช้ : $\\sin(-x) = -\\sin x$ ส่วนค่าคงตัว $1$ ไม่มีตัว $x$ อยู่เลย จึงไม่เปลี่ยนแปลงเมื่อแทน $-x$',
        '• ระบุตัวแปร : ที่นี่ $f(x) = 1 + \\sin x$ ⇒ พจน์แรกคือค่าคงตัว $1$ '
        '· พจน์ที่สองคือ $\\sin x$ ซึ่งเป็นฟังก์ชันคี่',
        '• แทนค่า : $f(-x) = 1 + \\sin(-x)$',
        '• ยุบ : $\\sin(-x) = -\\sin x$ ⇒ $f(-x) = 1 - \\sin x$',
        '• เทียบสองเป้าหมาย : $f(x) = 1 + \\sin x$ ⇒ $f(-x) \\ne f(x)$ '
        'เพราะ $1 - \\sin x = 1 + \\sin x$ จะบังคับให้ $\\sin x = 0$ ทุกค่า $x$ ซึ่งไม่จริง '
        '· และ $-f(x) = -1 - \\sin x$ ⇒ $f(-x) \\ne -f(x)$ เพราะ $1 - \\sin x = -1 - \\sin x$ '
        'จะบังคับให้ $1 = -1$ ซึ่งเป็นเท็จเสมอ ⇒ นิพจน์นี้<b>ไม่คู่และไม่คี่</b>',
        '• ต้นตออยู่ตรงค่าคงตัว : พจน์ $\\sin x$ เป็นคี่จริง แต่ค่าคงตัว $1$ ไม่ยอมกลับเครื่องหมายตาม '
        'ตรวจเร็วได้ด้วย $f(0) = 1 + \\sin 0 = 1 \\ne 0$ ซึ่งขัดกับข้อเท็จจริงที่ว่าฟังก์ชันคี่ที่นิยามที่ $0$ ต้องมี $f(0) = 0$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนค่าจำนวนจริงคู่หนึ่งคือ $x = \\dfrac{\\pi}{6}$ กับ '
        '$x = -\\dfrac{\\pi}{6}$ ลงในทุกนิพจน์ แล้ววางผลเทียบกันเป็นตาราง)</b>',
        '• เส้นทางข้างบนเดินด้วยสัญลักษณ์ล้วน คือแทน $-x$ แล้วยุบด้วยเอกลักษณ์ '
        'การตรวจรอบนี้จะไม่แตะเอกลักษณ์เหล่านั้นเลย แต่เปลี่ยนไปใช้ตัวเลขจริงแทน '
        'ถ้าสองทางชี้ไปที่นิพจน์เดียวกัน แปลว่าไม่ได้พลาดที่การยุบสัญลักษณ์',
        '• ค่าที่ต้องใช้ : $\\sin\\dfrac{\\pi}{6} = \\dfrac{1}{2}$ · $\\cos\\dfrac{\\pi}{6} = \\dfrac{\\sqrt{3}}{2}$ '
        '· $\\sin\\left(-\\dfrac{\\pi}{6}\\right) = -\\dfrac{1}{2}$ · $\\cos\\left(-\\dfrac{\\pi}{6}\\right) = \\dfrac{\\sqrt{3}}{2}$',
        '• แถวที่ 1 — $\\sin x\\cos x$ : ที่ $x = \\dfrac{\\pi}{6}$ ได้ '
        '$\\dfrac{1}{2} \\cdot \\dfrac{\\sqrt{3}}{2} = \\dfrac{\\sqrt{3}}{4}$ '
        'และที่ $x = -\\dfrac{\\pi}{6}$ ได้ $\\left(-\\dfrac{1}{2}\\right)\\left(\\dfrac{\\sqrt{3}}{2}\\right) = -\\dfrac{\\sqrt{3}}{4}$ '
        '⇒ สองค่านี้<b>ตรงข้ามกันพอดี</b> ✓ สอดคล้องกับ $f(-x) = -f(x)$',
        '• แถวที่ 2 — $\\cos 2x$ : ที่ $x = \\dfrac{\\pi}{6}$ ได้ $\\cos\\dfrac{\\pi}{3} = \\dfrac{1}{2}$ '
        'และที่ $x = -\\dfrac{\\pi}{6}$ ได้ $\\cos\\left(-\\dfrac{\\pi}{3}\\right) = \\dfrac{1}{2}$ '
        '⇒ สองค่านี้<b>เท่ากัน</b> และไม่ใช่ศูนย์ ⇒ เป็นฟังก์ชันคู่ ตัดออกจากการเป็นฟังก์ชันคี่',
        '• แถวที่ 3 — $\\left|\\sin x\\right|$ : ที่ $x = \\dfrac{\\pi}{6}$ ได้ $\\left|\\dfrac{1}{2}\\right| = \\dfrac{1}{2}$ '
        'และที่ $x = -\\dfrac{\\pi}{6}$ ได้ $\\left|-\\dfrac{1}{2}\\right| = \\dfrac{1}{2}$ '
        '⇒ <b>เท่ากัน</b>อีกเช่นกัน ⇒ เป็นฟังก์ชันคู่ ตัดออก',
        '• แถวที่ 4 — $1 + \\sin x$ : ที่ $x = \\dfrac{\\pi}{6}$ ได้ $1 + \\dfrac{1}{2} = \\dfrac{3}{2}$ '
        'และที่ $x = -\\dfrac{\\pi}{6}$ ได้ $1 - \\dfrac{1}{2} = \\dfrac{1}{2}$ '
        '⇒ <b>ไม่เท่ากันและไม่ตรงข้ามกัน</b> (ตรงข้ามของ $\\dfrac{3}{2}$ คือ $-\\dfrac{3}{2}$ ไม่ใช่ $\\dfrac{1}{2}$) ⇒ ตัดออก',
        '• 📌 ตรวจซ้ำอีกทางหนึ่งด้วยการเปลี่ยนหน้าตาของนิพจน์ที่ได้ : '
        '$\\sin x\\cos x = \\dfrac{1}{2}\\sin 2x$ ซึ่งเป็นค่าคงตัวคูณกับไซน์ของก้อน $2x$ '
        'และไซน์เป็นฟังก์ชันคี่ ⇒ $\\dfrac{1}{2}\\sin\\left(-2x\\right) = -\\dfrac{1}{2}\\sin 2x$ '
        '⇒ ยืนยันความเป็นฟังก์ชันคี่อีกทางโดยไม่ต้องใช้กฎเครื่องหมายของผลคูณเลย',
        '• ⚠️ ข้อจำกัดที่ต้องรู้ตัวไว้ : การแทนค่าเพียงคู่เดียว<b>พิสูจน์ไม่ได้</b>ว่านิพจน์นั้นเป็นฟังก์ชันคี่ '
        'เพราะนิยามบังคับว่าต้องจริงทุกค่า $x$ ⇒ ตารางนี้ใช้ได้เต็มที่ในการ<b>ตัด</b>นิพจน์ที่ไม่ใช่ออก '
        'ส่วนนิพจน์ที่รอดมาต้องพิสูจน์ด้วยนิยามอย่างที่ทำไว้แล้วในขั้นที่ 4 จึงจะเรียกว่าจบ',
        '',
        '✅ <b>คำตอบ</b> นิพจน์ที่เป็นฟังก์ชันคี่คือ $\\sin x\\cos x$ '
        'เพราะ $\\sin(-x)\\cos(-x) = \\left(-\\sin x\\right)\\left(\\cos x\\right) = -\\sin x\\cos x$ '
        'ซึ่งเท่ากับ $-f(x)$ สำหรับทุกจำนวนจริง $x$ → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• จำกฎเครื่องหมายให้ขึ้นใจ แล้วคัดกรองได้เร็วมาก : คี่คูณคี่ได้คู่ · คู่คูณคู่ได้คู่ '
        '· คี่คูณคู่ได้คี่ (นับจำนวนเครื่องหมายลบที่หลุดออกมา ถ้าหลุดมาจำนวนคี่ตัวก็ได้ของคี่) '
        'ในบทตรีโกณให้จำแค่ว่า $\\sin$ กับ $\\tan$ เป็นคี่ ส่วน $\\cos$ เป็นคู่ '
        'แล้วนิพจน์ที่เป็นผลคูณจะอ่านผลได้ทันทีโดยไม่ต้องแทน $-x$',
        '• เห็นเครื่องหมายค่าสัมบูรณ์ครอบอยู่เมื่อไร ให้เอนไปทางฟังก์ชันคู่ไว้ก่อน '
        'เพราะ $\\left|g(-x)\\right| = \\left|\\pm g(x)\\right| = \\left|g(x)\\right|$ '
        'ทั้งกรณีที่ $g$ เป็นคี่และกรณีที่ $g$ เป็นคู่ ⇒ ค่าสัมบูรณ์ของฟังก์ชันคี่หรือคู่ใด ๆ เป็นฟังก์ชันคู่เสมอ '
        '(ยกเว้นกรณีน่าเบื่อที่ $g$ เป็นศูนย์ตลอด ซึ่งเป็นทั้งคู่และคี่)',
        '• ใช้ $f(0)$ เป็นตะแกรงร่อนก่อนลงมือคำนวณ : ฟังก์ชันคี่ที่นิยามที่ $0$ ต้องมี $f(0) = 0$ เสมอ '
        'ลองแทน $x = 0$ ในสี่นิพจน์จะได้ $1$ · $0$ · $0$ · $1$ ตามลำดับ '
        '⇒ ร่อนทิ้งได้ทันทีสองนิพจน์คือ $\\cos 2x$ กับ $1 + \\sin x$ เหลือให้ตรวจละเอียดแค่สองตัว',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• เลือกนิพจน์ $\\cos 2x$ เพราะจำมาว่า “มุมสองเท่าทำให้พาริตีเปลี่ยน” '
        'คือคิดว่าการคูณมุมด้วย $2$ จะพลิกฟังก์ชันคู่ให้กลายเป็นคี่ · ความจำนี้ไม่จริงเลย '
        'ตัวคูณที่อยู่กับ $x$ ไม่มีผลต่อพาริตี เพราะเมื่อแทน $-x$ ก้อนข้างในกลายเป็น $-2x$ '
        'แล้ว $\\cos(-2x) = \\cos 2x$ ⇒ โคไซน์ยังคงเป็นฟังก์ชันคู่เหมือนเดิม '
        '· พิสูจน์ว่าผิดได้ด้วยตัวเลขค่าเดียว : ที่ $x = \\dfrac{\\pi}{6}$ ได้ $\\dfrac{1}{2}$ '
        'และที่ $x = -\\dfrac{\\pi}{6}$ ก็ได้ $\\dfrac{1}{2}$ ซึ่งต้องเป็น $-\\dfrac{1}{2}$ ถ้าเป็นฟังก์ชันคี่',
        '• เลือกนิพจน์ $\\left|\\sin x\\right|$ เพราะมองแต่ $\\sin$ ที่อยู่ข้างใน '
        'เห็นว่าไซน์เป็นฟังก์ชันคี่ก็รีบสรุปว่าทั้งก้อนเป็นคี่ตามไปด้วย โดยลืมว่ามีเครื่องหมายค่าสัมบูรณ์ครอบอยู่ '
        '· ที่ผิดคือเครื่องหมายลบที่ได้จาก $\\sin(-x) = -\\sin x$ ติดอยู่ข้างในค่าสัมบูรณ์ '
        'และค่าสัมบูรณ์กลืนเครื่องหมายทิ้ง ⇒ ลบตัวนั้นออกมาข้างนอกไม่ได้ '
        '· พิสูจน์ว่าผิดที่ $x = \\dfrac{\\pi}{2}$ : ได้ $\\left|\\sin\\dfrac{\\pi}{2}\\right| = 1$ '
        'ส่วนที่ $x = -\\dfrac{\\pi}{2}$ ได้ $\\left|-1\\right| = 1$ ซึ่งไม่ใช่ $-1$ '
        '· อีกอย่างที่มองข้ามคือค่าสัมบูรณ์ไม่มีทางติดลบ แต่ฟังก์ชันคี่ที่ไม่เป็นศูนย์ตลอดต้องมีค่าติดลบบ้าง',
        '• เลือกนิพจน์ $1 + \\sin x$ เพราะมองแต่พจน์ $\\sin x$ ซึ่งเป็นฟังก์ชันคี่จริง '
        'แล้วคิดว่าค่าคงตัวที่บวกอยู่ข้างหน้าเป็นแค่ของประดับ ไม่กระทบอะไร '
        '· ที่ผิดคือค่าคงตัว $1$ ไม่มี $x$ อยู่เลย มันจึงไม่กลับเครื่องหมายตาม '
        'ได้ $f(-x) = 1 - \\sin x$ ในขณะที่ $-f(x) = -1 - \\sin x$ ⇒ สองอย่างนี้ต่างกันอยู่ $2$ เสมอ '
        '· พิสูจน์เร็วที่สุดด้วย $x = 0$ : ได้ $f(0) = 1$ แต่ฟังก์ชันคี่ที่นิยามที่ $0$ ต้องมี $f(0) = 0$ '
        '⇒ นิพจน์นี้เป็นฟังก์ชันคี่ไม่ได้ตั้งแต่ต้น',
        '• อีกเส้นทางที่พาไปผิดคือแทนตัวเลขเพียงค่าเดียวแล้วรีบสรุปว่าเป็นฟังก์ชันคี่ '
        'ตัวอย่างที่หลอกได้จริงคือแทน $x = \\dfrac{\\pi}{4}$ ในนิพจน์ $\\cos 2x$ '
        'จะได้ $\\cos\\dfrac{\\pi}{2} = 0$ ทั้งที่ $x$ เป็นบวกและเป็นลบ และ $0 = -0$ พอดี '
        '⇒ ค่าคู่นี้ “ผ่าน” เงื่อนไข $f(-x) = -f(x)$ ทั้งที่นิพจน์นั้นเป็นฟังก์ชันคู่ '
        '· บทเรียนคือการแทนค่าใช้ตัดของที่ไม่ใช่ออกได้ แต่ใช้ยืนยันไม่ได้ '
        'ต้องกลับไปพิสูจน์ด้วยนิยามให้จริงทุกค่า $x$ เสมอ',
    ],
    'V.mold: G = a list of four trigonometric expressions built only from sine and cosine, namely '
    'cos(2x), the absolute value of sin(x), the product sin(x)cos(x), and the constant 1 added to '
    'sin(x), handed over together with the defining condition f(-x) = -f(x) spelled out inside the '
    'stem / A = which one of the four is an odd function / M = substitute -x for x in each expression '
    'in turn, reduce the result with the two parity facts sin(-x) = -sin(x) and cos(-x) = cos(x), and '
    'compare the reduced form against both targets f(x) and -f(x), so that even, odd and neither are '
    'all reachable outcomes. Mold labels: G-FOUR-TRIG-EXPRESSIONS-PARITY / A-WHICH-IS-ODD / '
    'M-PARITY-TEST-SUB-NEG-X, and the M label is new to the register, since no earlier item in this '
    'chapter tests a parity definition at all. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 with the total at 2 or below, T at most 1 and C exactly 0 '
    '-> level: ง่าย. '
    'F = 1 because a single fact family carries the whole item, the parity of the two basic circular '
    'functions, sine odd and cosine even; the absolute value rule and the sign rule for a product are '
    'consequences of that same family rather than separate formulas a solver must have memorised. '
    'C = 0 because nothing is chained: each of the four expressions is tested on its own and no '
    'intermediate result from one test is fed into another, so the four checks could be done in any '
    'order or even by four different people. P = 1 because each test is one substitution followed by '
    'one sign reduction, with no arithmetic beyond moving a minus sign, although the work has to be '
    'repeated four times, which is what keeps this above a zero. T = 0 because the statement hides '
    'nothing at all: the defining condition is printed in the stem, the phrase covering every real x '
    'is printed as well, and all four expressions are defined on the whole real line, so there is no '
    'excluded value to notice, no branch to discard and no unstated assumption to recover. L = 0 '
    'because the item is purely symbolic, with no scene to picture, no figure to reconstruct and no '
    'sentence of context to translate into mathematics. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): for each of the four expressions the test simplify(f(-x) + f(x)) == 0 was '
    'evaluated, exactly one of them returns True, and its position is index 2 counting from zero, '
    'which is the machine confirmation of the key rather than an assertion. The complementary test '
    'simplify(f(-x) - f(x)) == 0 was run here as well and returns True for cos(2x) and for the '
    'absolute value of sin(x), and False for the last expression on both tests, so the three named '
    'error paths are machine-computed and not invented: cos(2x) lands in the even class, the absolute '
    'value of sin(x) lands in the even class because the sign produced by sin(-x) is trapped inside '
    'the absolute value, and 1 + sin(x) lands in neither class since 1 - sin(x) equals neither '
    '1 + sin(x) nor -1 - sin(x). The independent check was verified too: at x = pi/6 and x = -pi/6 '
    'the four expressions return sqrt(3)/4 against -sqrt(3)/4, then 1/2 against 1/2, then 1/2 against '
    '1/2, then 3/2 against 1/2, so the numeric table separates the odd one from the rest. The second '
    'cross-check simplify(sin(x)*cos(x) - sin(2*x)/2) returns 0, which re-derives the same conclusion '
    'through a sine of a doubled angle. The warning printed in the write-up was machine-checked as '
    'well: at x = pi/4 the expression cos(2x) returns 0 at both signs of x, and 0 equals -0, so a '
    'single substitution really can let an even expression pass the odd test, which is why the '
    'surviving expression is proved from the definition instead. '
    'Collision sweep on 6457 items (63 bank set files + k1 out + k2 out, duplicate ids removed), '
    'probe rerun for this item over the same corpus: the Thai phrase for odd function appears in the '
    'question text of 10 items and the phrase for even function in 8, and every one of them sits in '
    'chapter 5 on functions under subtopic 5.16, none in chapter 7. The nearest relative is '
    'gen-chap-05-function-q305, which asks which of the following is an odd function and therefore '
    'shares the A label, but its four candidates are built from x, x squared and the absolute value '
    'of x, so its G is a list of algebraic expressions and its M is the sign behaviour of the '
    'absolute value on powers of x, and it carries no trigonometry at all; sharing one label out of '
    'three is a WATCH and not a collision. The other close reading, pat1-2563-02-q12, prints the same '
    'defining line f(-x) = -f(x), but only as one hypothesis among three that are then combined into '
    'a functional equation to be solved, so its A is the value of a composite and its M is '
    'substitution into a system, which shares nothing with a parity classification. Restricting the '
    'sweep to chapter 7 items whose question or choices contain any parity wording returns 1 item, '
    'pat1-2552-07-q39, which is a false positive from the Thai word for a matching pair of socks in a '
    'counting problem, so the pair formed by trigonometry together with a parity test is empty across '
    'the whole corpus. The four candidates here are expressions rather than numeric values, so the '
    'ascending-value rule that governs numeric items does not apply to this item; the list arrived '
    'fixed from the central spec and the author had no freedom over which slot holds the key.',
)

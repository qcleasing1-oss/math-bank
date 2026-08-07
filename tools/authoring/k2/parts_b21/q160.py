# -*- coding: utf-8 -*-
add(
    160,
    ['7.3'],
    'ปานกลาง',
    'กำหนดให้ $h(x) = \\cos\\left(\\dfrac{\\pi}{3}\\sin x\\right)$ สำหรับทุกจำนวนจริง $x$ '
    'ค่าต่ำสุดที่เป็นไปได้ของ $h(x)$ คือข้อใด',
    [
        '$-1$',
        '$-\\dfrac{1}{2}$',
        '$\\dfrac{1}{2}$',
        '$\\dfrac{\\sqrt{3}}{2}$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ฟังก์ชันข้อนี้เป็น<b>ฟังก์ชันประกอบ</b> คือมีฟังก์ชันซ้อนกันอยู่สองชั้น : ชั้นในคือ '
        '$u = \\dfrac{\\pi}{3}\\sin x$ และชั้นนอกคือ $\\cos u$ ⇒ เขียนย่อได้ว่า $h(x) = \\cos u$ · '
        'กติกาของฟังก์ชันแบบนี้คือ ⭐ <b>ต้องไล่จากในออกนอก</b> ⇒ หาก่อนว่าชั้นในวิ่งไปได้ถึงช่วงไหน '
        'แล้วจึงค่อยถามว่าชั้นนอกทำอะไรบนช่วงนั้น · เหตุผลที่ต้องเรียงแบบนี้คือ ค่าของ $h$ ทุกค่า '
        'ล้วนเป็นค่าของ $\\cos u$ เฉพาะที่ $u$ ไปถึงได้จริงเท่านั้น ⇒ ถ้า $u$ ไปไม่ถึงมุมใด '
        'ค่าของโคไซน์ที่มุมนั้นก็ไม่นับเป็นค่าของ $h$',
        '• ขอบเขตของไซน์ : $-1 \\le \\sin x \\le 1$ สำหรับทุกจำนวนจริง $x$ · เหตุผลอ่านจากวงกลมหนึ่งหน่วยได้ตรง ๆ '
        'เพราะ $\\sin x$ คือพิกัด $y$ ของจุดบนวงกลมรัศมี $1$ ซึ่งสูงได้มากที่สุดแค่ $1$ และต่ำได้มากที่สุดแค่ $-1$ · '
        'และปลายทั้งสองข้างนี้ไปถึงได้จริง เพราะ $\\sin\\dfrac{\\pi}{2} = 1$ กับ $\\sin\\left(-\\dfrac{\\pi}{2}\\right) = -1$',
        '• การคูณอสมการด้วยจำนวนบวก : ถ้า $-1 \\le s \\le 1$ และ $k > 0$ แล้ว $-k \\le ks \\le k$ '
        '⇒ เครื่องหมายอสมการไม่พลิก เพราะการคูณด้วยจำนวนบวกไม่สลับลำดับของจำนวน · '
        'บรรทัดนี้คือเครื่องมือที่ใช้ย้ายช่วงของ $\\sin x$ ไปเป็นช่วงของอาร์กิวเมนต์',
        '• พฤติกรรมของโคไซน์บนช่วงแคบ ๆ รอบศูนย์ : $\\cos$ เป็น<b>ฟังก์ชันคู่</b> คือ $\\cos(-u) = \\cos u$ '
        '⇒ กราฟสมมาตรรอบแกนตั้ง · และ $\\cos$ ลดลงเรื่อย ๆ เมื่อ $u$ เดินจาก $0$ ไปทาง $\\pi$ · '
        'สองข้อนี้รวมกันบอกว่า บนช่วงปิดที่สมมาตรรอบศูนย์อย่าง $[-c,\\ c]$ เมื่อ $0 < c \\le \\pi$ '
        'ค่าสูงสุดของ $\\cos u$ อยู่ที่กลางช่วงคือ $u = 0$ และค่าต่ำสุดอยู่ที่<b>ปลายช่วง</b> $u = \\pm c$ '
        '⇒ ⛔ ห้ามไปหยิบ $-1$ ซึ่งเป็นค่าต่ำสุดของโคไซน์ตลอดทั้งเส้นจำนวนจริงมาใช้ ถ้าช่วงยังไปไม่ถึง $\\pi$',
        '• เครื่องมือตัดทิ้งอย่างเร็ว : ถ้า $\\left|u\\right| < \\dfrac{\\pi}{2}$ แล้ว $\\cos u > 0$ เสมอ · '
        'เหตุผลจากวงกลมหนึ่งหน่วยคือมุมที่กางจากแกน $x$ ไม่ถึงหนึ่งมุมฉาก จะได้จุดที่อยู่ทางขวาของแกน $y$ '
        '⇒ พิกัด $x$ ของจุดนั้นเป็นบวก ⇒ บรรทัดนี้ใช้ตัดค่าที่ติดลบทิ้งได้ทันทีโดยไม่ต้องคำนวณอะไรเลย',
        '• ค่ามุมพิเศษที่ต้องแยกให้ขาด : $\\cos\\dfrac{\\pi}{3} = \\dfrac{1}{2}$ ส่วน $\\sin\\dfrac{\\pi}{3} = \\dfrac{\\sqrt{3}}{2}$ '
        '⇒ สองค่านี้เป็นคนละค่ากัน ⛔ จุดที่สลับกันบ่อยที่สุดคือมุม $\\dfrac{\\pi}{3}$ นี่เอง · '
        'วิธีกันคือจำว่าที่มุม $\\dfrac{\\pi}{3}$ จุดบนวงกลมหนึ่งหน่วยอยู่ค่อนไปทางสูง ⇒ พิกัด $y$ ต้องใหญ่กว่าพิกัด $x$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• ฟังก์ชัน $h(x) = \\cos\\left(\\dfrac{\\pi}{3}\\sin x\\right)$ นิยามไว้สำหรับทุกจำนวนจริง $x$ '
        '⇒ โดเมนคือจำนวนจริงทั้งหมด ไม่มีเงื่อนไขมาตัดช่วงของ $x$ เลย',
        '• แยกชั้นให้ชัดก่อนลงมือ : ชั้นในคือ $\\dfrac{\\pi}{3}\\sin x$ · ชั้นนอกคือโคไซน์ · '
        'ตัวคูณ $\\dfrac{\\pi}{3}$ อยู่<b>ข้างในวงเล็บ</b> ของโคไซน์ ⇒ มันไปบีบอาร์กิวเมนต์ ไม่ได้ไปขยายค่าของฟังก์ชัน',
        '• สังเกตหน้าตาก่อนลงมือ : ตัวแปร $x$ ไม่ได้เข้าไปในโคไซน์แบบตรง ๆ แต่ถูกห่อด้วยไซน์อีกชั้นหนึ่ง '
        '⇒ อาร์กิวเมนต์ของโคไซน์จึง<b>ไม่ได้วิ่งทั่วเส้นจำนวนจริง</b> ⇒ ⛔ ห้ามใช้สูตรสำเร็จรูปที่ว่า '
        'ค่าต่ำสุดของโคไซน์คือ $-1$ · เทียบกับ $\\cos 3x$ ซึ่งอาร์กิวเมนต์ $3x$ วิ่งได้ทั่วเส้นจำนวนจริง '
        'จึงใช้สูตรสำเร็จรูปได้ แต่ข้อนี้ใช้ไม่ได้',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าต่ำสุดที่เป็นไปได้ของ $h(x)$ เมื่อ $x$ วิ่งทั่วจำนวนจริง นั่นคือค่าที่เล็กที่สุดในเรนจ์ของ $h$ '
        'และต้องเป็นค่าที่<b>เกิดขึ้นจริง</b>ที่ $x$ ค่าใดค่าหนึ่ง ไม่ใช่แค่ขอบล่างที่ไปไม่ถึง',
        '',
        '<b>【 ไล่จากในออกนอกสองชั้น : ชั้นแรกหาว่าอาร์กิวเมนต์ $\\dfrac{\\pi}{3}\\sin x$ วิ่งได้แค่ในช่วง '
        '$\\left[-\\dfrac{\\pi}{3},\\ \\dfrac{\\pi}{3}\\right]$ ชั้นที่สองดูว่าโคไซน์บนช่วงนั้นต่ำสุดที่ปลายช่วง '
        'ได้ค่า $\\cos\\dfrac{\\pi}{3} = \\dfrac{1}{2}$ แล้วปิดท้ายด้วยการยืนยันว่าค่านี้เกิดขึ้นจริงที่ '
        '$x = \\dfrac{\\pi}{2}$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · หาช่วงที่อาร์กิวเมนต์ของโคไซน์วิ่งไปถึงได้</b>',
        '• สูตรที่ใช้ : $-1 \\le \\sin x \\le 1$ สำหรับทุกจำนวนจริง $x$',
        '• ระบุตัวแปร : ให้ $u$ แทนอาร์กิวเมนต์ของโคไซน์ นั่นคือ $u = \\dfrac{\\pi}{3}\\sin x$ '
        '⇒ ฟังก์ชันที่โจทย์ให้เขียนใหม่ได้เป็น $h = \\cos u$',
        '• แทนค่า : คูณอสมการ $-1 \\le \\sin x \\le 1$ ตลอดทั้งสามส่วนด้วย $\\dfrac{\\pi}{3}$ '
        'ซึ่งเป็นจำนวนบวก ⇒ เครื่องหมายอสมการไม่พลิก',
        '• ยุบ : $-\\dfrac{\\pi}{3} \\le \\dfrac{\\pi}{3}\\sin x \\le \\dfrac{\\pi}{3}$ '
        '⇒ $u \\in \\left[-\\dfrac{\\pi}{3},\\ \\dfrac{\\pi}{3}\\right]$',
        '• ตรวจว่าปลายช่วงไปถึงได้จริงทั้งสองข้าง : ที่ $x = \\dfrac{\\pi}{2}$ ได้ $\\sin x = 1$ '
        '⇒ $u = \\dfrac{\\pi}{3}$ · ที่ $x = -\\dfrac{\\pi}{2}$ ได้ $\\sin x = -1$ ⇒ $u = -\\dfrac{\\pi}{3}$ '
        '⇒ ช่วงที่ได้เป็น<b>ช่วงปิด</b> คือรวมปลายทั้งสองข้างเข้าไปด้วย และ $u$ กวาดเต็มช่วงนี้ '
        'เพราะไซน์เป็นฟังก์ชันต่อเนื่อง',
        '• ⚠️ <b>บรรทัดนี้คือหัวใจของทั้งข้อ</b> : อาร์กิวเมนต์วิ่งได้กว้างที่สุดแค่ $\\dfrac{\\pi}{3}$ '
        'ซึ่งมีค่าประมาณ $1.047$ เท่านั้น ⇒ มัน<b>ไปไม่ถึง</b> $\\pi$ ซึ่งมีค่าประมาณ $3.142$ '
        'อันเป็นมุมเดียวในหนึ่งรอบที่ทำให้โคไซน์ลงไปถึง $-1$ ⇒ ค่า $-1$ จึงถูกตัดออกตั้งแต่ขั้นนี้',
        '',
        '<b>ขั้นที่ 2 · หาค่าต่ำสุดของโคไซน์บนช่วงที่ได้จากขั้นที่ 1</b>',
        '• สูตรที่ใช้ : บนช่วงปิด $\\left[-c,\\ c\\right]$ เมื่อ $0 < c \\le \\pi$ ฟังก์ชัน $\\cos u$ '
        'มีค่าสูงสุดที่ $u = 0$ และมีค่าต่ำสุดที่ปลายช่วง $u = \\pm c$ · '
        'เหตุผลมาจากสองข้อรวมกัน คือโคไซน์เป็นฟังก์ชันคู่ ⇒ ปลายช่วงสองข้างให้ค่าเท่ากัน '
        'และโคไซน์ลดลงเมื่อมุมเดินออกจาก $0$ ⇒ ยิ่งไกลจากกลางช่วงค่ายิ่งน้อย',
        '• ระบุตัวแปร : ข้อนี้ $c = \\dfrac{\\pi}{3}$ ซึ่งอยู่ในเงื่อนไข $0 < c \\le \\pi$ จริง',
        '• แทนค่าที่กลางช่วง : $u = 0$ ⇒ $\\cos 0 = 1$ ⇒ นี่คือค่าสูงสุดของ $h$',
        '• แทนค่าที่ปลายช่วงข้างขวา : $u = \\dfrac{\\pi}{3}$ ⇒ $\\cos\\dfrac{\\pi}{3} = \\dfrac{1}{2}$',
        '• แทนค่าที่ปลายช่วงข้างซ้าย : $u = -\\dfrac{\\pi}{3}$ ⇒ $\\cos\\left(-\\dfrac{\\pi}{3}\\right) '
        '= \\cos\\dfrac{\\pi}{3} = \\dfrac{1}{2}$ ⇒ ⭐ ได้ค่าเท่ากับปลายข้างขวาเป๊ะ '
        'เพราะโคไซน์เป็นฟังก์ชัน<b>คู่</b> ⛔ ไม่ใช่ฟังก์ชันคี่ ⇒ เครื่องหมายลบข้างในไม่ได้ทำให้ค่าที่ออกมาติดลบ',
        '• ยุบ : ค่าของ $\\cos u$ เมื่อ $u$ กวาดทั่วช่วง $\\left[-\\dfrac{\\pi}{3},\\ \\dfrac{\\pi}{3}\\right]$ '
        'จึงไล่จาก $\\dfrac{1}{2}$ ขึ้นไปจนถึง $1$ ⇒ เรนจ์ของ $h$ คือ $\\left[\\dfrac{1}{2},\\ 1\\right]$ '
        '⇒ ค่าต่ำสุดคือ $\\dfrac{1}{2}$',
        '',
        '<b>ขั้นที่ 3 · ยืนยันว่าค่าต่ำสุดที่ได้เกิดขึ้นจริง</b>',
        '• สูตรที่ใช้ : ค่าต่ำสุดของฟังก์ชันต้องเป็นค่าที่ฟังก์ชัน<b>รับได้จริง</b> '
        '⇒ ต้องชี้ $x$ ให้ได้อย่างน้อยหนึ่งค่าที่ทำให้ $h(x)$ เท่ากับค่านั้นพอดี ไม่ใช่แค่บอกว่าเป็นขอบล่าง',
        '• ระบุตัวแปร : ต้องการให้ $u = \\dfrac{\\pi}{3}$ ⇒ ต้องการให้ $\\sin x = 1$ '
        '⇒ เลือก $x = \\dfrac{\\pi}{2}$ ซึ่งเป็นจำนวนจริง จึงอยู่ในโดเมนของ $h$ แน่นอน',
        '• แทนค่าเข้าฟังก์ชันเดิมทีละชั้น : ชั้นในได้ $\\dfrac{\\pi}{3}\\sin\\dfrac{\\pi}{2} '
        '= \\dfrac{\\pi}{3} \\times 1 = \\dfrac{\\pi}{3}$ · ชั้นนอกได้ $\\cos\\dfrac{\\pi}{3} = \\dfrac{1}{2}$',
        '• ยุบ : $h\\left(\\dfrac{\\pi}{2}\\right) = \\dfrac{1}{2}$ ⇒ ค่า $\\dfrac{1}{2}$ '
        'เกิดขึ้นจริงที่ $x = \\dfrac{\\pi}{2}$ ✓ ⇒ รวมกับขั้นที่ 2 ที่บอกว่าไม่มีค่าใดต่ำกว่านี้ '
        'จึงสรุปได้ว่า $\\dfrac{1}{2}$ เป็นค่าต่ำสุดจริง',
        '• 📌 เก็บของแถมไว้ด้วย : ที่ $x = -\\dfrac{\\pi}{2}$ ก็ได้ $h = \\dfrac{1}{2}$ เช่นกัน '
        '⇒ ค่าต่ำสุดนี้เกิดขึ้นที่ $x$ หลายค่า ซึ่งเป็นเรื่องปกติของฟังก์ชันที่เป็นคาบ',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · กวาดแทนค่า $x$ หลายค่าแล้วดูว่ามีค่าไหนหลุดช่วงหรือไม่ '
        'ปิดท้ายด้วยเหตุผลเชิงโครงสร้างเรื่องเครื่องหมาย)</b>',
        '• เส้นทางข้างบนเดินจากช่วงของอาร์กิวเมนต์ไปหาค่าต่ำสุด รอบนี้จะไม่แตะช่วงเลยแม้แต่ก้าวเดียว '
        'แต่จะหยิบ $x$ มาแทนค่าทีละตัวแล้วดูว่ามีค่าใดต่ำกว่า $\\dfrac{1}{2}$ หรือติดลบบ้างหรือไม่',
        '• $x = 0$ ⇒ $\\sin 0 = 0$ ⇒ $h = \\cos 0 = 1$',
        '• $x = \\dfrac{\\pi}{2}$ ⇒ $\\sin x = 1$ ⇒ $h = \\cos\\dfrac{\\pi}{3} = \\dfrac{1}{2}$',
        '• $x = -\\dfrac{\\pi}{2}$ ⇒ $\\sin x = -1$ ⇒ $h = \\cos\\left(-\\dfrac{\\pi}{3}\\right) = \\dfrac{1}{2}$ '
        '⇒ ได้เท่ากับกรณีก่อนหน้าพอดี ซึ่งเป็นหลักฐานตรง ๆ ว่าโคไซน์เป็นฟังก์ชันคู่',
        '• $x = \\dfrac{\\pi}{6}$ ⇒ $\\sin x = \\dfrac{1}{2}$ ⇒ $h = \\cos\\dfrac{\\pi}{6} = \\dfrac{\\sqrt{3}}{2} '
        '\\approx 0.866$',
        '• $x = \\pi$ ⇒ $\\sin \\pi = 0$ ⇒ $h = \\cos 0 = 1$',
        '• ⇒ ทุกค่าที่กวาดมาอยู่ระหว่าง $\\dfrac{1}{2}$ กับ $1$ ทั้งหมด และ<b>ไม่มีค่าไหนติดลบเลย</b> ✓ '
        'ตรงกับเรนจ์ $\\left[\\dfrac{1}{2},\\ 1\\right]$ ที่คำนวณไว้',
        '• 📌 เหตุผลเชิงโครงสร้างที่ปิดประตูค่าติดลบทั้งหมดในทีเดียว : จากขั้นที่ 1 ได้ '
        '$\\left|u\\right| \\le \\dfrac{\\pi}{3} < \\dfrac{\\pi}{2}$ และโคไซน์ของมุมที่กางจากแกน $x$ '
        'ไม่ถึงหนึ่งมุมฉากย่อมเป็นบวกเสมอ ⇒ $h(x) > 0$ ทุกจำนวนจริง $x$ '
        '⇒ ค่า $-1$ กับค่า $-\\dfrac{1}{2}$ ตัดทิ้งได้ทันทีโดยไม่ต้องคำนวณอะไรเลย '
        'เหลือผู้เข้าชิงเพียง $\\dfrac{1}{2}$ กับ $\\dfrac{\\sqrt{3}}{2}$ และ $\\dfrac{1}{2} < \\dfrac{\\sqrt{3}}{2}$ '
        '⇒ ค่าต่ำสุดต้องเป็น $\\dfrac{1}{2}$ ✓',
        '',
        '✅ <b>คำตอบ</b> ค่าต่ำสุดที่เป็นไปได้ของ $h(x)$ คือ $\\dfrac{1}{2}$ → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอฟังก์ชันตรีโกณซ้อนตรีโกณเมื่อไร ให้เขียนคำว่า “อาร์กิวเมนต์วิ่งได้แค่ไหน” ลงกระดาษก่อนเป็นอันดับแรก '
        'แล้วค่อยตอบคำถามข้อที่สองว่า “ฟังก์ชันข้างนอกทำอะไรบนช่วงนั้น” · '
        'สองคำถามนี้เรียงสลับกันไม่ได้ เพราะคำตอบของคำถามแรกคือโดเมนของคำถามที่สอง',
        '• วิธีดูอย่างเร็วว่าจะใช้สูตรแอมพลิจูดสำเร็จรูปได้หรือไม่ : ถ้าอาร์กิวเมนต์เป็น<b>ฟังก์ชันเชิงเส้น</b>ของ $x$ '
        'อย่าง $3x$ หรือ $2x + \\dfrac{\\pi}{4}$ มันจะวิ่งทั่วเส้นจำนวนจริง ⇒ ใช้ได้ · '
        'แต่ถ้าอาร์กิวเมนต์มีตรีโกณห่ออยู่อีกชั้นอย่างข้อนี้ มันจะถูกขังอยู่ในช่วงแคบ ⇒ ⛔ ใช้ไม่ได้ '
        'ต้องไล่ทีละชั้นเสมอ',
        '• เมื่อช่วงของอาร์กิวเมนต์สมมาตรรอบศูนย์และแคบกว่าครึ่งรอบ ให้ดูแค่สองที่พอ คือกลางช่วงกับปลายช่วง '
        '· ค่าที่กลางช่วงคือค่าสูงสุด ค่าที่ปลายช่วงคือค่าต่ำสุด ⇒ ไม่ต้องวาดกราฟทั้งเส้นให้เสียเวลา',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $-1$ เพราะเห็นคำว่าโคไซน์แล้วตอบทันทีว่า “โคไซน์มีค่าต่ำสุด $-1$ เสมอ” '
        'โดยไม่ดูเลยว่าอาร์กิวเมนต์วิ่งไปได้ถึงไหน · ค่านี้ผิดและพิสูจน์ได้ตรง ๆ ว่าเกิดขึ้นไม่ได้ : '
        'การจะให้ $h(x) = -1$ ต้องมี $\\dfrac{\\pi}{3}\\sin x = \\pi$ ⇒ $\\sin x = 3$ '
        'ซึ่งเป็นไปไม่ได้เพราะไซน์ของจำนวนจริงใด ๆ มีค่าไม่เกิน $1$ ⇒ ไม่มี $x$ ใดในโลกให้ค่านี้ · '
        'วิธีกันคือถามตัวเองก่อนเสมอว่าอาร์กิวเมนต์ไปถึง $\\pi$ ได้จริงหรือไม่ ข้อนี้ไปได้ไกลสุดแค่ '
        '$\\dfrac{\\pi}{3}$ ซึ่งเป็นเพียงหนึ่งในสามของระยะที่ต้องการ',
        '• ได้ค่า $-\\dfrac{1}{2}$ เพราะเดินมาถูกครึ่งทาง คือรู้ว่าต้องแทน $\\sin x = -1$ '
        'จนได้ $\\cos\\left(-\\dfrac{\\pi}{3}\\right)$ แล้ว แต่ตอนถอดเครื่องหมายลบออกจากวงเล็บกลับคิดว่าโคไซน์เป็น'
        'ฟังก์ชัน<b>คี่</b> จึงเขียนต่อว่าเท่ากับ $-\\cos\\dfrac{\\pi}{3} = -\\dfrac{1}{2}$ · '
        'ความจริงคือ<b>โคไซน์เป็นฟังก์ชันคู่</b> $\\cos(-u) = \\cos u$ ⇒ $\\cos\\left(-\\dfrac{\\pi}{3}\\right) '
        '= +\\dfrac{1}{2}$ · ตัวที่เป็นฟังก์ชันคี่คือไซน์กับแทนเจนต์ ไม่ใช่โคไซน์ · '
        'ตรวจซ้ำได้อีกสองชั้น : ชั้นแรก การจะให้ $h(x) = -\\dfrac{1}{2}$ ต้องมี '
        '$\\dfrac{\\pi}{3}\\sin x = \\dfrac{2\\pi}{3}$ ⇒ $\\sin x = 2$ ซึ่งเป็นไปไม่ได้ · '
        'ชั้นที่สอง อาร์กิวเมนต์ทุกตัวมีขนาดไม่เกิน $\\dfrac{\\pi}{3}$ ซึ่งน้อยกว่าหนึ่งมุมฉาก '
        '⇒ ค่าที่ออกมาต้องเป็นบวกเสมอ · วิธีกันคือท่องคู่ให้ติดปากว่าโคไซน์คู่ ไซน์คี่',
        '• ได้ค่า $\\dfrac{\\sqrt{3}}{2}$ เพราะหาช่วงของอาร์กิวเมนต์ได้ถูกต้องแล้วว่าคือ '
        '$\\left[-\\dfrac{\\pi}{3},\\ \\dfrac{\\pi}{3}\\right]$ และรู้ด้วยว่าค่าต่ำสุดอยู่ที่ปลายช่วง '
        'แต่ตอนอ่านค่ามุมพิเศษกลับหยิบผิดตัว คือใช้ $\\sin\\dfrac{\\pi}{3} = \\dfrac{\\sqrt{3}}{2}$ '
        'แทนที่จะเป็น $\\cos\\dfrac{\\pi}{3} = \\dfrac{1}{2}$ · ค่านี้ผิดทั้งที่มันเป็นค่าที่ $h$ รับได้จริง '
        'ซึ่งทำให้หลอกได้แนบเนียนกว่าเพื่อน : มันเกิดที่ $x = \\dfrac{\\pi}{6}$ เพราะ $\\sin\\dfrac{\\pi}{6} '
        '= \\dfrac{1}{2}$ ⇒ อาร์กิวเมนต์เป็น $\\dfrac{\\pi}{6}$ ⇒ $h = \\cos\\dfrac{\\pi}{6} '
        '= \\dfrac{\\sqrt{3}}{2}$ · แต่มันอยู่<b>กลางเรนจ์</b> ไม่ใช่ก้นเรนจ์ เพราะ '
        '$\\dfrac{\\sqrt{3}}{2} \\approx 0.866$ ซึ่งมากกว่า $\\dfrac{1}{2} = 0.5$ '
        '⇒ ยังมีค่าที่ต่ำกว่านี้อยู่ ⇒ ไม่ใช่ค่าต่ำสุด · วิธีกันคือวาดสามเหลี่ยมมุมฉาก $30$-$60$-$90$ '
        'ขึ้นมาเช็คทุกครั้งก่อนเขียนค่ามุมพิเศษลงกระดาษ',
        '• อีกเส้นทางที่พลาดกันบ่อยคือสลับหัวท้าย ตอบ $1$ ซึ่งเป็นค่า<b>สูงสุด</b>ของ $h$ ไม่ใช่ค่าต่ำสุด · '
        'ค่านี้เกิดที่กลางช่วงคือ $u = 0$ ซึ่งมาจาก $\\sin x = 0$ เช่น $x = 0$ หรือ $x = \\pi$ · '
        'ที่สลับกันเพราะพอเห็นว่า $\\sin x$ ตัวเล็กที่สุดคือ $-1$ ก็คิดว่าต้องให้ค่า $h$ เล็กที่สุดตามไปด้วย '
        'ทั้งที่โคไซน์ไม่ได้เพิ่มตามอาร์กิวเมนต์ แต่ขึ้นกับ<b>ระยะห่างจากศูนย์</b>ของอาร์กิวเมนต์ต่างหาก '
        '⇒ อาร์กิวเมนต์ที่เล็กที่สุดคือ $-\\dfrac{\\pi}{3}$ กลับให้ค่าเท่ากับอาร์กิวเมนต์ที่ใหญ่ที่สุดคือ '
        '$\\dfrac{\\pi}{3}$ พอดี · วิธีกันคือเขียนคำว่าต่ำสุดหรือสูงสุดวงกลมไว้ตั้งแต่อ่านโจทย์จบบรรทัดแรก',
    ],
    'V.mold: G = G-COS-OF-SCALED-SINE-COMPOSITE, one composite function h(x) = cos((pi/3)*sin x) defined '
    'for every real x, where the outer function is a cosine and its argument is a sine scaled by pi/3, so '
    'the variable never reaches the cosine directly / A = A-MIN-VALUE, the smallest value h can actually '
    'take / M = M-INNER-BOUND-THEN-COS-ON-SUBINTERVAL, bound the inner layer first, -1 <= sin x <= 1 gives '
    'the argument the closed interval [-pi/3, pi/3], then read the outer cosine on that interval only, '
    'where evenness makes the two endpoints agree and monotone decrease away from 0 puts the minimum at '
    'the endpoints, giving cos(pi/3) = 1/2, and finally exhibit x = pi/2 to prove the value is attained. '
    'Rubric F2 C1 P1 T2 L0 = 6/15, total below 8 so the ยาก gate cannot open, and T <= 2 -> level: '
    'ปานกลาง. F = 2 because two facts carry the item, the bound on sine and the behaviour of cosine on a '
    'closed interval that is symmetric about zero and narrower than half a turn; F was not raised to 3 '
    'because no identity, no double angle and no solving of any equation is needed anywhere. C = 1 for the '
    'single crossing outside subtopic 7.3, namely the idea of a composite function and the fact that the '
    'range of the inner layer becomes the domain of the outer one, which is imported from the function '
    'chapter but used at its shallowest; it is not 2 because nothing else is joined on, the whole chain is '
    'two links long. P = 1 because the arithmetic is three substitutions and one comparison, one '
    'multiplication of an inequality by a positive constant and two special-angle lookups, with no '
    'branching and no case work. T = 2 for two hidden turns: the reflex answer -1 is unreachable because '
    'the argument stops at pi/3 and never gets near pi, and the endpoint -pi/3 does not produce a negative '
    'value because cosine is even rather than odd, which is exactly what the second wrong value on offer '
    'exploits. T was not raised to 3 because both turns are guarded by the same single observation about '
    'the interval, and once that interval is written down there is no branch left to choose and no root to '
    'reject. L = 0 because the item is purely symbolic, there is no figure to draw and no real-world scene '
    'to model, the function is handed over in closed form. The total of 6 sits inside the 3 to 7 band and '
    'misses the ยาก threshold of 8 by two points even though T = 2, since that gate needs the total as '
    'well; the ง่าย gate is missed too because it demands a total of at most 2 with C = 0. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): with g = cos(pi*u/3), minimum(g, u, Interval(-1, 1)) returns Rational(1, 2) '
    'and maximum returns 1, which is the machine proof that the range of h is exactly [1/2, 1] and that '
    'the key at index 2 is the true minimum rather than a lower bound nobody reaches; the same run '
    'evaluates cos(pi*sin(pi/2)/3) and gets Rational(1, 2), so the minimum is attained at a named real x. '
    'A separate sweep of 4001 sample points of x across [0, 2*pi] returned a smallest value of '
    '0.5000000000000001 and a largest value of 1.0, so no sampled point falls outside the computed range '
    'and none of them is negative. Every wrong value on offer was machine-computed from a named error path '
    'instead of being invented: solving (pi/3)*s = pi for s returns s = 3, so h = -1 would require sin x = '
    '3 and is unreachable; solving (pi/3)*s = 2*pi/3 returns s = 2, so h = -1/2 would require sin x = 2 '
    'and is unreachable as well, and cos(-pi/3) - cos(pi/3) simplifies to 0, which is the machine '
    'statement that cosine is even and that the odd-function slip is a slip; solving (pi/3)*s = pi/6 '
    'returns s = 1/2, so sqrt(3)/2 is a genuine value of h attained at x = pi/6, and its float value '
    '0.8660254 is larger than 0.5, so it is a value inside the range but not the smallest one. The '
    'structural screen used in the independent check was verified numerically too, pi/3 = 1.0471976 is '
    'less than pi/2 = 1.5707963, so every argument stays inside the quarter turn where cosine is positive '
    'and no negative value can occur at all. '
    'Collision sweep on 6457 unique items (bank 63 files + k1 out + k2 out, 6601 raw records with 144 '
    'duplicates dropped), probes run over the question text: the phrase for the smallest possible value '
    'returns 4 items, of which gen-chap-07-trigonometry-q013 asks for the minimum of 4 - 5*cos(3*x) and is '
    'the exact contrast case rather than a clash, since there the argument 3*x is linear and sweeps the '
    'whole real line so the textbook amplitude rule applies and cosine really does reach -1, which is the '
    'very rule this item is built to block; gen-chap-07-trigonometry-q044 asks for the minimum of '
    'sin(x)**2 - 4*sin(x) + 3 and is the nearest relative by mechanism because it also substitutes the '
    'inner sine and works on [-1, 1], but its outer layer is a quadratic polynomial handled by completing '
    'the square, not a trigonometric function evaluated on a shrunken angle interval, so its M is '
    'different and the evenness turn does not exist there; the remaining two, q029 and q050, are a sum of '
    'three absolute sines and a sum of squared inverse functions. A scan for a trigonometric function '
    'sitting inside the argument of another trigonometric function returns 47 items and the only one that '
    'shares the surface of this G is gen-chap-07-trigonometry-q078, sin(pi*cos x) = 0 on [0, 2*pi), which '
    'asks for a solution set and is solved by listing the multiples of pi that the argument can hit, so it '
    'is subtopic 7.7 with a different A and a different M and touches this item only in appearance; the '
    'others are quadratics in a single ratio, matrix determinants and inverse-function equations. The pair '
    'formed by the word for range together with a trigonometric function returns 113 items, none of which '
    'asks for the extreme value of a trig-inside-trig composite; the closest by subtopic are q009, q123 '
    'and q124, which all read amplitude, period and shift off a*sin(b*x + c) + d and run in the reverse '
    'direction, from stated extremes back to the parameters. Inside batch 21 the closest item is q161, '
    'which also bounds an inner quantity first, but there the inner substitution is sin(x)**2 on [0, 1] '
    'and the outer layer is a reciprocal of a quadratic, and it asks for the sum of the extremes rather '
    'than the minimum alone. Choices are ordered ascending by numeric value, -1, then -0.5, then 0.5, then '
    'sqrt(3)/2 = 0.8660254, so the answer slot is forced by that rule and was not chosen.',
)

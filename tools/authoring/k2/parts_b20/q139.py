# -*- coding: utf-8 -*-
add(
    139,
    ['7.3'],
    'ง่าย',
    'กำหนดให้ฟังก์ชัน $f$ นิยามโดย $f(x) = 6\\sin x$ เมื่อ $0 \\le x < \\dfrac{\\pi}{2}$ '
    'และ $f(x) = 2 - 4\\cos x$ เมื่อ $\\dfrac{\\pi}{2} \\le x \\le 2\\pi$ '
    'ค่าของ $f\\left(\\dfrac{\\pi}{6}\\right) + f(\\pi)$ เท่ากับข้อใด',
    [
        '$1$',
        '$3$',
        '$7$',
        '$9$',
    ],
    3,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• <b>ฟังก์ชันที่นิยามเป็นช่วง</b> คือฟังก์ชันเพียงตัวเดียวที่มีกฎการหาค่ามากกว่าหนึ่งกฎ '
        'โดยแต่ละกฎมีช่วงของ $x$ กำกับไว้ว่าใช้ได้กับค่าใดบ้าง '
        'ช่วงที่กำกับไม่ใช่ของประดับ แต่เป็นส่วนหนึ่งของนิยามเท่า ๆ กับตัวสูตร '
        '⇒ ก่อนแทนค่าทุกครั้งต้องตอบให้ได้ก่อนว่า $x$ ที่จะแทนตกอยู่ในช่วงของกฎใด '
        'แล้วจึงใช้กฎนั้นเพียงกฎเดียว ⛔ ห้ามหยิบกฎแรกที่ตาเห็นมาใช้รวดทุกค่า',
        '• การเทียบขนาดของมุมที่เขียนในรูปเรเดียน : เมื่อทุกตัวมี $\\pi$ เป็นตัวร่วม '
        'ให้ดูแต่จำนวนที่คูณอยู่กับ $\\pi$ เพราะ $\\pi$ เป็นจำนวนบวก '
        'การคูณด้วยจำนวนบวกตัวเดียวกันไม่ทำให้ลำดับมากน้อยสลับกัน · เช่น '
        '$\\dfrac{\\pi}{6} = \\dfrac{1}{6}\\pi$ และ $\\dfrac{\\pi}{2} = \\dfrac{1}{2}\\pi$ '
        '⇒ เทียบแค่ $\\dfrac{1}{6}$ กับ $\\dfrac{1}{2}$ ก็สรุปได้ว่า $\\dfrac{\\pi}{6} < \\dfrac{\\pi}{2}$',
        '• ค่ามุมพิเศษตัวแรกที่ต้องใช้ : $\\sin\\dfrac{\\pi}{6} = \\dfrac{1}{2}$ '
        'ที่มาไม่ใช่การท่องเปล่า ๆ แต่มาจากสามเหลี่ยมมุมฉากที่มีมุมขนาด $30^{\\circ}$ '
        'ซึ่งมีอัตราส่วนความยาวด้านเป็น $1 : \\sqrt{3} : 2$ '
        'ด้านตรงข้ามมุม $30^{\\circ}$ จึงยาวครึ่งหนึ่งของด้านตรงข้ามมุมฉากพอดี '
        'และ $\\dfrac{\\pi}{6}$ เรเดียนก็คือ $30^{\\circ}$ นั่นเอง',
        '• ค่ามุมพิเศษตัวที่สองที่ต้องใช้ : $\\cos\\pi = -1$ '
        'ที่มาคือบนวงกลมหนึ่งหน่วย มุมขนาด $\\pi$ เรเดียนคือการหมุนไปครึ่งรอบ '
        'ปลายรัศมีจึงไปหยุดที่จุด $(-1,\\ 0)$ และนิยามบอกว่า $\\cos$ ของมุมคือพิกัดแรกของจุดนั้น '
        '⇒ $\\cos\\pi = -1$ ⛔ ไม่ใช่ $1$ · ค่าของ $\\cos$ จะเป็น $1$ ก็ต่อเมื่อปลายรัศมีอยู่ที่จุด '
        '$(1,\\ 0)$ ซึ่งตรงกับมุม $0$ หรือมุม $2\\pi$ เท่านั้น',
        '• สองเรื่องที่ต้องระวังตอนแทนค่าลงในกฎ $2 - 4\\cos x$ : (1) จำนวนลบคูณจำนวนลบได้จำนวนบวก '
        '⇒ ถ้า $\\cos x = -1$ แล้ว $-4\\cos x = -4 \\times (-1) = 4$ ⇒ ค่าของกฎจะ<b>เพิ่มขึ้น</b> ไม่ใช่ลดลง · '
        '(2) เลข $2$ ที่นำหน้าเป็นส่วนหนึ่งของกฎ ⛔ ห้ามทิ้ง · '
        'และเพราะ $-1 \\le \\cos x \\le 1$ เสมอ ค่าของกฎนี้จึงอยู่ระหว่าง $2 - 4 = -2$ กับ $2 + 4 = 6$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• ฟังก์ชัน $f$ มีกฎสองกิ่ง · กิ่งแรกคือ $f(x) = 6\\sin x$ ใช้เมื่อ $0 \\le x < \\dfrac{\\pi}{2}$ '
        '· กิ่งที่สองคือ $f(x) = 2 - 4\\cos x$ ใช้เมื่อ $\\dfrac{\\pi}{2} \\le x \\le 2\\pi$',
        '• ช่วงของสองกิ่งไม่ทับกันเลยและต่อกันพอดีที่ $x = \\dfrac{\\pi}{2}$ '
        'โดยจุดต่อนี้เป็นของกิ่งที่สอง เพราะกิ่งแรกกำกับด้วยเครื่องหมาย $<$ '
        'ส่วนกิ่งที่สองกำกับด้วย $\\le$ ⇒ ทุกค่าของ $x$ ตั้งแต่ $0$ ถึง $2\\pi$ มีกฎใช้ได้กฎเดียวเสมอ ไม่กำกวม',
        '• ต้องใช้ค่าของฟังก์ชันสองค่า คือค่าที่ $x = \\dfrac{\\pi}{6}$ และค่าที่ $x = \\pi$ แล้วนำมาบวกกัน',
        '• สังเกตหน้าตาก่อนลงมือ : ค่าที่ต้องแทนสองตัวอยู่คนละฝั่งของเส้นแบ่ง $\\dfrac{\\pi}{2}$ '
        'เพราะ $\\dfrac{\\pi}{6} \\approx 0.52$ ซึ่งน้อยกว่า $\\dfrac{\\pi}{2} \\approx 1.57$ '
        'ส่วน $\\pi \\approx 3.14$ ซึ่งมากกว่า ⇒ สองค่านี้ตกคนละกิ่ง '
        '⇒ ต้องใช้สูตรคนละอันกัน นี่คือหัวใจของข้อนี้',
        '• สังเกตอีกอย่าง : มุมที่ต้องแทนทั้งสองเป็นมุมพิเศษที่อ่านค่าได้จากสามเหลี่ยมมุมฉากพิเศษ '
        'และจากวงกลมหนึ่งหน่วย '
        '⇒ ตัวเลขจะออกมาเป็นจำนวนเต็มทั้งหมด ไม่ต้องใช้เครื่องคิดเลขเลย',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของผลบวก $f\\left(\\dfrac{\\pi}{6}\\right) + f(\\pi)$ '
        'ซึ่งเป็นจำนวนจริงเพียงจำนวนเดียว',
        '',
        '<b>【 ตรวจก่อนว่าค่าของ $x$ แต่ละตัวตกอยู่ในช่วงของกิ่งใด '
        'แล้วจึงแทนค่าลงในกฎของกิ่งนั้นทีละค่า สุดท้ายจึงนำผลลัพธ์ทั้งสองมาบวกกัน 】</b>',
        '',
        '<b>ขั้นที่ 1 · เลือกกิ่งให้ $x = \\dfrac{\\pi}{6}$ แล้วคำนวณ $f\\left(\\dfrac{\\pi}{6}\\right)$</b>',
        '• เกณฑ์ที่ใช้ตัดสิน : กิ่งแรกใช้ได้เมื่อ $0 \\le x < \\dfrac{\\pi}{2}$ '
        '⇒ ต้องตรวจสองด้าน คือค่าที่จะแทนต้องไม่น้อยกว่า $0$ และต้องน้อยกว่า $\\dfrac{\\pi}{2}$',
        '• ระบุตัวแปรให้ชัด : ค่าที่จะแทนคือ $x = \\dfrac{\\pi}{6}$',
        '• ตรวจด้านซ้าย : $\\dfrac{\\pi}{6} > 0$ แน่นอน เพราะ $\\pi$ เป็นจำนวนบวกและถูกหารด้วย $6$ '
        'ซึ่งเป็นจำนวนบวก · ตรวจด้านขวา : เขียนใหม่เป็น $\\dfrac{\\pi}{6} = \\dfrac{1}{6}\\pi$ '
        'และ $\\dfrac{\\pi}{2} = \\dfrac{1}{2}\\pi$ ⇒ เทียบ $\\dfrac{1}{6}$ กับ $\\dfrac{1}{2}$ '
        'ได้ว่า $\\dfrac{1}{6} < \\dfrac{1}{2}$ ⇒ $\\dfrac{\\pi}{6} < \\dfrac{\\pi}{2}$ ✓ '
        '⇒ ค่านี้ตกอยู่ในช่วงของ<b>กิ่งแรก</b>',
        '• สูตรที่ใช้ได้จึงเป็นกิ่งแรก : $f(x) = 6\\sin x$',
        '• แทนค่า : $f\\left(\\dfrac{\\pi}{6}\\right) = 6\\sin\\dfrac{\\pi}{6}$',
        '• ยุบ : $\\sin\\dfrac{\\pi}{6} = \\dfrac{1}{2}$ '
        '⇒ $f\\left(\\dfrac{\\pi}{6}\\right) = 6 \\times \\dfrac{1}{2} = 3$',
        '',
        '<b>ขั้นที่ 2 · เลือกกิ่งให้ $x = \\pi$ แล้วคำนวณ $f(\\pi)$</b>',
        '• เกณฑ์ที่ใช้ตัดสิน : กิ่งที่สองใช้ได้เมื่อ $\\dfrac{\\pi}{2} \\le x \\le 2\\pi$',
        '• ระบุตัวแปรให้ชัด : ค่าที่จะแทนคือ $x = \\pi$ ซึ่งเขียนได้เป็น $1 \\times \\pi$',
        '• ตรวจทั้งสองด้านพร้อมกันด้วยจำนวนที่คูณอยู่กับ $\\pi$ : ฝั่งซ้ายคือ $\\dfrac{1}{2}$ '
        '· ตัวเราคือ $1$ · ฝั่งขวาคือ $2$ ⇒ $\\dfrac{1}{2} < 1 < 2$ '
        '⇒ $\\dfrac{\\pi}{2} < \\pi < 2\\pi$ ✓ ⇒ ค่านี้ตกอยู่ในช่วงของ<b>กิ่งที่สอง</b>',
        '• ⛔ ระวังตรงนี้ให้มาก : ห้ามเผลอใช้ $6\\sin x$ กับ $x = \\pi$ '
        'เพราะช่วงของกิ่งแรกจบลงก่อนถึง $\\dfrac{\\pi}{2}$ ด้วยซ้ำ กฎนั้นจึงไม่ครอบคลุมมุม $\\pi$ เลย',
        '• สูตรที่ใช้ได้จึงเป็นกิ่งที่สอง : $f(x) = 2 - 4\\cos x$',
        '• ระบุค่าที่ต้องรู้ก่อนแทน : $\\cos\\pi = -1$ ตามที่อ่านได้จากจุด $(-1,\\ 0)$ บนวงกลมหนึ่งหน่วย',
        '• แทนค่า : $f(\\pi) = 2 - 4 \\times (-1)$',
        '• ยุบทีละก้อน : $-4 \\times (-1) = 4$ เพราะลบคูณลบได้บวก ⇒ $f(\\pi) = 2 + 4 = 6$',
        '',
        '<b>ขั้นที่ 3 · นำค่าทั้งสองมาบวกกันตามที่โจทย์ถาม</b>',
        '• สูตรที่ใช้ : ผลบวกที่ต้องการ $= f\\left(\\dfrac{\\pi}{6}\\right) + f(\\pi)$',
        '• ระบุตัวแปร : $f\\left(\\dfrac{\\pi}{6}\\right) = 3$ จากขั้นที่ 1 · $f(\\pi) = 6$ จากขั้นที่ 2',
        '• แทนค่า : ผลบวก $= 3 + 6$',
        '• ยุบ : $3 + 6 = 9$',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · เทียบสองกิ่งที่จุดต่อ แล้วคุมด้วยกรอบค่าที่แต่ละกิ่งเป็นไปได้)</b>',
        '• เส้นทางข้างล่างนี้ไม่แทนค่าซ้ำรอยเดิม แต่จะตรวจสองอย่างที่เป็นคนละเรื่องกับการแทนค่า '
        'คือตรวจว่า<b>การเลือกกิ่งมีผลจริง</b> และตรวจว่าค่าที่ได้ตกอยู่ในกรอบที่กิ่งนั้นเป็นไปได้',
        '• ตรวจที่จุดต่อ $x = \\dfrac{\\pi}{2}$ ก่อน : ถ้าลากกิ่งแรกต่อไปจนถึงจุดนั้น จะได้ '
        '$6\\sin\\dfrac{\\pi}{2} = 6 \\times 1 = 6$ ส่วนกิ่งที่สองที่จุดเดียวกันให้ '
        '$2 - 4\\cos\\dfrac{\\pi}{2} = 2 - 4 \\times 0 = 2$ ⇒ สองกิ่งไม่บรรจบกัน ห่างกันถึง $4$ หน่วย',
        '• ⇒ <b>ฟังก์ชันนี้ขาดที่จุดต่อ</b> ไม่ใช่เส้นเดียวต่อเนื่องกัน '
        '⇒ ถ้าหยิบกิ่งผิด ค่าที่ได้จะเพี้ยนทันทีโดยไม่มีอะไรมาช่วยกลบ ⛔ เดาไม่ได้ '
        'นี่คือหลักฐานว่าขั้นตอนการตรวจช่วงในขั้นที่ 1 กับขั้นที่ 2 เป็นงานที่ขาดไม่ได้',
        '• ตรวจกรอบค่าของกิ่งที่สอง : เพราะ $-1 \\le \\cos x \\le 1$ ⇒ $-4 \\le -4\\cos x \\le 4$ '
        '⇒ ค่าของ $2 - 4\\cos x$ อยู่ในช่วง $[-2,\\ 6]$ ⇒ ค่า $f(\\pi) = 6$ ที่หาได้ '
        'คือค่าสูงสุดของกิ่งนั้นพอดี ซึ่งเกิดขึ้นเมื่อ $\\cos x = -1$ '
        'และมุมในช่วง $\\dfrac{\\pi}{2} \\le x \\le 2\\pi$ ที่ทำให้ $\\cos x = -1$ ก็คือ $x = \\pi$ จริง ✓ '
        'สมเหตุสมผลทุกทาง',
        '• ตรวจกรอบค่าของกิ่งแรกด้วย : บนช่วง $0 \\le x < \\dfrac{\\pi}{2}$ ค่าของ $\\sin x$ '
        'ไต่จาก $0$ ขึ้นไปโดยยังไม่ถึง $1$ ⇒ ค่าของ $6\\sin x$ อยู่ในช่วง $[0,\\ 6)$ '
        '⇒ ค่า $f\\left(\\dfrac{\\pi}{6}\\right) = 3$ ตกอยู่กลางกรอบพอดี ✓',
        '• ปิดท้ายด้วยกรอบของผลบวก : ค่าจากกิ่งแรกอยู่ใน $[0,\\ 6)$ และค่าจากกิ่งที่สองอยู่ใน $[-2,\\ 6]$ '
        '⇒ ผลบวกเป็นไปได้ตั้งแต่ $-2$ จนถึงต่ำกว่า $12$ ⇒ ค่า $9$ ที่ได้อยู่ในกรอบนี้ ✓',
        '',
        '✅ <b>คำตอบ</b> $f\\left(\\dfrac{\\pi}{6}\\right) = 3$ และ $f(\\pi) = 6$ '
        'ดังนั้นผลบวกเท่ากับ $3 + 6 = 9$ → <b>ตัวเลือก 4</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• พอเห็นคำว่า “นิยามโดย” พร้อมมีเงื่อนไข “เมื่อ ...” ห้อยท้ายสูตรมากกว่าหนึ่งอัน '
        'ให้วาดเส้นจำนวนสั้น ๆ ข้างกระดาษทันที ปักหมุด $0$ · $\\dfrac{\\pi}{2}$ · $2\\pi$ '
        'แล้วจุดตำแหน่งของค่าที่โจทย์สั่งให้แทนลงไป ⇒ จะเห็นด้วยตาว่าค่าไหนตกกิ่งไหน '
        'ปลอดภัยกว่าการอ่านเงื่อนไขในใจแล้วรีบแทนค่า',
        '• เวลาต้องเทียบขนาดของมุมเรเดียนหลาย ๆ ตัว อย่ารีบเปลี่ยนเป็นทศนิยม '
        'ให้ดึง $\\pi$ ออกมาเป็นตัวร่วมแล้วเทียบเฉพาะจำนวนที่คูณอยู่ '
        'เช่น $\\dfrac{1}{6} < \\dfrac{1}{2} < 1 < 2$ ⇒ เรียงลำดับได้ครบในบรรทัดเดียวโดยไม่ต้องกดเครื่องคิดเลข',
        '• ค่ามุมพิเศษที่มักถูกจำสลับเครื่องหมายคือค่าที่มุมครึ่งรอบ ให้ผูกกับภาพวงกลมหนึ่งหน่วยเสมอ : '
        'มุม $\\pi$ อยู่ที่จุด $(-1,\\ 0)$ ⇒ $\\cos\\pi = -1$ และ $\\sin\\pi = 0$ '
        '⇒ จำภาพจุดได้จุดเดียว ได้ค่าตรีโกณสองค่าพร้อมกัน',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ถ้าได้ค่า $1$ แปลว่าจำเครื่องหมายผิดเป็น $\\cos\\pi = 1$ '
        'ทำให้ $f(\\pi) = 2 - 4 \\times 1 = -2$ แล้วบวกได้ $3 + (-2) = 1$ · '
        'ค่านี้ผิดแน่นอน พิสูจน์ด้วยวงกลมหนึ่งหน่วย : มุม $\\pi$ คือการหมุนครึ่งรอบไปหยุดที่จุด $(-1,\\ 0)$ '
        'พิกัดแรกจึงเป็น $-1$ ⛔ ไม่ใช่ $1$ · ยิ่งกว่านั้นค่า $-2$ ที่ได้คือค่าต่ำสุดของกิ่งที่สอง '
        'ซึ่งเกิดเมื่อ $\\cos x = 1$ นั่นคือที่ปลายช่วง $x = 2\\pi$ ไม่ใช่ที่ $x = \\pi$',
        '• ถ้าได้ค่า $3$ แปลว่าใช้กิ่งแรกกับ $x = \\pi$ ทั้งที่ $\\pi$ อยู่ในช่วงของกิ่งที่สอง '
        'คือคิด $6\\sin\\pi = 6 \\times 0 = 0$ แล้วบวกได้ $3 + 0 = 3$ · '
        'ค่านี้ผิดเพราะช่วงของกิ่งแรกคือ $0 \\le x < \\dfrac{\\pi}{2}$ และ $\\pi \\approx 3.14$ '
        'ซึ่งมากกว่า $\\dfrac{\\pi}{2} \\approx 1.57$ ⇒ กฎ $6\\sin x$ ไม่ได้นิยามค่าที่ $x = \\pi$ ไว้เลย · '
        'สังเกตเพิ่ม : ถ้ากิ่งแรกใช้ได้ตลอดทั้งเส้นจริง โจทย์ก็ไม่มีเหตุผลใดที่จะเขียนกิ่งที่สองขึ้นมา',
        '• ถ้าได้ค่า $7$ แปลว่าเลือกกิ่งถูกแล้วแต่ลืมพจน์คงที่ $2$ ในกิ่งที่สอง '
        'คือคิดแค่ $-4\\cos\\pi = 4$ แล้วบวกได้ $3 + 4 = 7$ · '
        'ค่านี้ผิดเพราะเลข $2$ เป็นส่วนหนึ่งของกฎเท่า ๆ กับพจน์ $-4\\cos x$ '
        'ตรวจซ้ำได้จากกรอบค่า : ถ้าตัด $2$ ทิ้ง ค่าของกิ่งที่สองจะอยู่ในช่วง $[-4,\\ 4]$ '
        'ซึ่งไม่ตรงกับกฎที่โจทย์เขียนไว้ เพราะกฎจริงให้ค่าอยู่ในช่วง $[-2,\\ 6]$',
        '• อีกเส้นทางที่พลาดกันบ่อยคือหาค่าได้ครบทั้งสองค่าแล้วแต่ตอบเพียงค่าเดียว คือตอบ $3$ หรือ $6$ '
        'โดยลืมว่าโจทย์ถามหา<b>ผลบวก</b>ของค่าทั้งสอง · '
        'วิธีกันพลาดคือขีดเส้นใต้เครื่องหมายบวกในโจทย์ตั้งแต่อ่านรอบแรก '
        'แล้วถามตัวเองก่อนวงคำตอบว่าได้ใช้ค่าที่หามาครบทุกค่าแล้วหรือยัง',
    ],
    'V.mold: G = one function handed over by two trigonometric rules, each rule carrying its own '
    'interval of x written beside it, the first rule 6*sin(x) on 0 <= x < pi/2 and the second rule '
    '2 - 4*cos(x) on pi/2 <= x <= 2*pi / A = the sum of the two function values f(pi/6) + f(pi) / '
    'M = decide for each input separately which interval it falls into, substitute it into that branch '
    'alone using the special-angle values sin(pi/6) = 1/2 and cos(pi) = -1, then add the two results. '
    'Rubric F1 C0 P1 T0 L0 = 2/15 with total at most 2, T = 0 and C = 0 -> level: ง่าย. '
    'F = 1 because a single knowledge block carries the item from start to finish: reading a piecewise '
    'definition, which means matching an input to the interval that owns it before touching the formula; '
    'the two special-angle values belong to that same block as the standard table entries, no identity '
    'is applied and no theorem is derived. C = 0 because subtopic 7.3 answers the item on its own and '
    'nothing is borrowed from another subtopic; comparing pi/6 with pi/2 is ordinary arithmetic on the '
    'same radian scale rather than a second body of knowledge. P = 1 and deliberately not 2 because the '
    'two substitutions and the closing addition sit side by side in one computation, and neither '
    'substitution manufactures an intermediate object that the other has to reinterpret; the benchmark '
    'is q120, held at one stage for two moves standing next to each other rather than chained. T = 0 '
    'because nothing is hidden: each interval is printed on the same line as the rule it governs, and '
    'neither input sits at the junction pi/2, which is the only place where the tie between the strict '
    'and the non-strict inequality would have to be settled, so choosing a branch here is a reading step '
    'and not a turning point; had one of the two inputs been exactly pi/2, T would have risen to 1 and '
    'the item would have left this band. L = 0 because the statement is bare symbol talk with no worded '
    'scene to model and no figure to picture; the benchmarks are q120 and the other pure-formula items '
    'held at L = 0 for the same reason. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b20.py): with f1 = 6*sin(x) and f2 = 2 - 4*cos(x), f1.subs(x, pi/6) returns 3 exactly '
    'and f2.subs(x, pi) returns 6 exactly, so the sum returns 9; sin(pi/6) evaluates to 1/2 and cos(pi) '
    'to -1 as exact rationals with no floating point anywhere. Every wrong path was machine-computed '
    'from a named error instead of being invented: f1.subs(x, pi/6) + f1.subs(x, pi) returns 3 for '
    'keeping the first branch at x = pi, since 6*sin(pi) returns 0; f1.subs(x, pi/6) + (-4*cos(pi)) '
    'returns 7 for dropping the constant 2; and f1.subs(x, pi/6) + (2 - 4*1) returns 1 for storing '
    'cos(pi) as +1, whose second term is -2. The independent check was machine-verified as well: at the '
    'junction 6*sin(pi/2) returns 6 while 2 - 4*cos(pi/2) returns 2, a gap of 4, so the function is '
    'discontinuous there and the branch cannot be guessed from the value; maximum(2 - 4*cos(x), x, '
    'Interval(pi/2, 2*pi)) returns 6 and the matching minimum returns -2, so f(pi) = 6 sits exactly at '
    'the top of its own branch, reached where cos(x) = -1, while 2 - 4*cos(2*pi) returns -2 at the other '
    'end; on the first branch 6*sin(x) stays inside [0, 6) with the upper end unreachable because pi/2 '
    'is excluded, and the value 3 sits inside it. The ordering was checked numerically too: pi/6 is '
    'about 0.5236, pi/2 about 1.5708, pi about 3.1416 and 2*pi about 6.2832, confirming that the first '
    'input lands in the first interval and the second input strictly inside the second. '
    'Collision sweep on 6437 items (bank 63 files + k1 out + k2 out), probe rerun over the same merged '
    'corpus that collide_b20.py loads: the opening phrase of this item, a function handed over by a '
    'stated defining rule, returns 17 items across the corpus and not one of them defines the function '
    'with a trigonometric rule, so the pair that defines this item, a two-interval piecewise definition '
    'together with trigonometric branches, returns 0 items. The four items that mention both an interval '
    'condition and a trigonometric function are not piecewise at all: two of them recover the parameters '
    'of a single sine wave from its extreme positions, one is a multi-statement true-or-false item that '
    'places a quadratic beside sin(x) on a domain and asks which claim holds, and one is an exam item '
    'that uses a quadratic only to pin down the value of sin(theta). The surface shape f(a) + f(b) '
    'appears in 74 items, but its intersection with a two-branch definition returns exactly 1 item, a '
    'calculus continuity item whose branches are a rational expression and a linear expression with an '
    'unknown coefficient, so it shares neither G nor M with this item. The nearest relative inside '
    'subtopic 7.3 asks for f(pi/3) + f(pi/4) of a single cosine rule whose coefficient must first be '
    'recovered from a count of zeros on an interval, so it shares A alone while both G and M differ. '
    'Choices are ordered ascending by numeric value (1, then 3, then 7, then 9), so the answer slot is '
    'forced by that rule and was not chosen.',
)

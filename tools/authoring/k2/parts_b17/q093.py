# -*- coding: utf-8 -*-
# 🔴 แก้ 2026-08-05 หลัง blind-solve QC : คีย์เดิมเป็น 2 (10√2) ซึ่ง **ผิด**
#    เหตุ : ฉบับเดิมวางมุมผิดสองที่ — โคนเสาใช้ 90+15=105 (ที่ถูกคือ 90-15=75)
#           และปลายเงาใช้ 60-15=45 (ที่ถูกคือ 60+15=75)
#    ทั้งสองชุดบวกได้ 180 เหมือนกัน ด่าน "บวกมุมสามมุม" จึงเขียวทั้งที่รูปผิด
#    ⇒ บทเรียน : วิธีตรวจที่ยังใช้ "มุมชุดเดิม" ไม่ใช่วิธีอิสระ · ฉบับนี้ตรวจด้วยพิกัดแทน
add(
    93,
    ['7.10', '7.9'],
    'ยาก',
    'เสาต้นหนึ่งสูง $20$ เมตร ตั้งตรงในแนวดิ่งอยู่ที่เชิงเนิน '
    'โดยพื้นของเนินเป็นพื้นลาดตรงที่ทำมุม $15^{\\circ}$ กับแนวระดับ '
    'ขณะหนึ่งแสงอาทิตย์ส่องทำมุมเงย $60^{\\circ}$ กับแนวระดับ '
    'ทำให้เงาของเสาทอดขึ้นไปตามพื้นลาด '
    'ถ้าแนวแสงอาทิตย์ แนวเสา และแนวลาดของเนิน อยู่ในระนาบดิ่งเดียวกัน '
    'แล้วเงาของเสาที่วัดตามพื้นลาดยาวกี่เมตร',
    [
        '$10\\left(\\sqrt{6} - \\sqrt{2}\\right)$',
        '$\\dfrac{20\\sqrt{3}}{3}$',
        '$10\\sqrt{2}$',
        '$10\\sqrt{6}$',
    ],
    0,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• มุมเงย คือมุมที่วัดจาก<b>แนวระดับ</b>เงยขึ้นไปหาแนวที่สนใจ '
        'ดังนั้นคำว่ามุมเงย $60^{\\circ}$ ของแสงอาทิตย์ แปลว่าแนวลำแสงเอียงทำมุม $60^{\\circ}$ '
        'กับพื้นระดับ ไม่ใช่กับเสาและไม่ใช่กับพื้นลาด · มุมของพื้นลาด $15^{\\circ}$ ก็วัดจากแนวระดับเช่นกัน',
        '• ⛔ กับดักที่ทำให้ข้อนี้พลาดกันมากที่สุด : มุมภายในของสามเหลี่ยมที่จุดหนึ่ง ๆ '
        'คือมุมระหว่าง<b>รังสีสองเส้นที่ชี้ออกจากจุดนั้นไปหาจุดยอดอีกสองจุด</b> '
        '⛔ ไม่ใช่มุมระหว่าง “แนวลาด” กับ “แนวแสง” ลอย ๆ · '
        'เส้นเดียวกันมีสองทิศ ถ้าหยิบผิดทิศจะได้มุมประกอบ $180^{\\circ}$ ลบออกไป ซึ่งพาผิดทั้งข้อ',
        '• วิธีกันพลาดที่ใช้ได้จริง : วาดรูปก่อน แล้วอ่านมุมจากรูป ⛔ อย่าท่องเป็นสูตรว่าเมื่อไรบวกเมื่อไรลบ '
        'ตัวช่วยจำที่ใช้ได้คือ ถ้าเนิน<b>เงยหนีจากดวงอาทิตย์</b> มุมที่ปลายเงาจะเป็นผลบวก '
        'ถ้าเนิน<b>เงยเข้าหาดวงอาทิตย์</b> จึงจะเป็นผลลบ · ข้อนี้เงาทอดขึ้นเนิน แปลว่าเนินเงยหนีดวงอาทิตย์',
        '• ผลรวมของมุมภายในสามเหลี่ยมเท่ากับ $180^{\\circ}$ เสมอ ⛔ แต่การบวกได้ $180^{\\circ}$ '
        '<b>ไม่ได้แปลว่ามุมชุดนั้นถูก</b> — มุมสองชุดที่ต่างกันก็บวกได้ $180^{\\circ}$ ได้ทั้งคู่ '
        'จึงใช้ยืนยันความถูกต้องของรูปไม่ได้ ต้องตรวจด้วยวิธีที่ไม่พึ่งมุมชุดเดิม',
        '• กฎของไซน์ : ในสามเหลี่ยมใด ๆ ด้านแต่ละด้านหารด้วยไซน์ของมุมตรงข้ามด้านนั้นจะได้ค่าเท่ากันหมด '
        'เขียนได้ว่า $\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C}$ '
        'โดย $a$ อยู่ตรงข้ามมุม $A$ เสมอ · และถ้าสามเหลี่ยมมีมุมเท่ากันสองมุม ด้านตรงข้ามมุมคู่นั้นจะยาวเท่ากัน',
        '• ค่ามุมที่ต้องหยิบได้ทันที $\\sin 30^{\\circ} = \\dfrac{1}{2}$ · '
        '$\\sin 75^{\\circ} = \\dfrac{\\sqrt{6} + \\sqrt{2}}{4} \\approx 0.9659$ · '
        'และเทคนิคจัดรูปที่จะได้ใช้คือคูณด้วยสังยุค : '
        '$\\dfrac{40}{\\sqrt{6} + \\sqrt{2}} = \\dfrac{40\\left(\\sqrt{6} - \\sqrt{2}\\right)}{6 - 2} '
        '= 10\\left(\\sqrt{6} - \\sqrt{2}\\right)$',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• เสาสูง $20$ เมตร ตั้งตรงในแนวดิ่ง อยู่ที่เชิงเนินพอดี',
        '• พื้นของเนินเป็นพื้นลาดตรง ทำมุม $15^{\\circ}$ กับแนวระดับ',
        '• แสงอาทิตย์ทำมุมเงย $60^{\\circ}$ กับแนวระดับ',
        '• เงาของเสาทอดขึ้นไปตามพื้นลาด และทุกแนวอยู่ในระนาบดิ่งเดียวกัน '
        'จึงเป็นปัญหาบนระนาบแบน ๆ แผ่นเดียว ไม่ใช่ปัญหาสามมิติ',
        '• สังเกตหน้าตาก่อนลงมือ : คำว่าเงาทอด<b>ขึ้น</b>ไปตามพื้นลาด บอกตำแหน่งดวงอาทิตย์ให้เสร็จในตัว '
        'เงาต้องอยู่ฝั่งตรงข้ามกับดวงอาทิตย์เสมอ ⇒ ดวงอาทิตย์อยู่ฝั่งเชิงเนิน ส่วนเนินเงยหนีออกไปอีกทาง',
        '• ข้อนี้ไม่มีรูปประกอบ ต้องวาดเอง ให้วาดตามลำดับนี้ '
        'ลากเส้นแนวระดับหนึ่งเส้นก่อน แล้วทำจุด $B$ ไว้บนเส้นนั้น จุด $B$ คือโคนเสาซึ่งอยู่ที่เชิงลาดพอดี',
        '• จากจุด $B$ ลากเส้นขึ้นตรง ๆ ในแนวดิ่ง แทนตัวเสาที่ยาว $20$ เมตร ปลายบนของเส้นนี้คือ $T$ ยอดเสา',
        '• จากจุด $B$ ลากอีกเส้นหนึ่งเฉียงขึ้น<b>ไปทางขวา</b> ทำมุม $15^{\\circ}$ กับแนวระดับ '
        'เส้นนี้คือพื้นลาดของเนิน ⇒ ดวงอาทิตย์จึงอยู่ทาง<b>ซ้าย</b>เหนือแนวระดับ',
        '• ทำจุด $S$ ไว้บนเส้นลาดนั้น แล้วลากเส้น $TS$ เชื่อม เส้น $TS$ คือแนวลำแสงอาทิตย์ '
        'ที่เฉียดยอดเสาลงมากระทบพื้นลาดพอดี จุด $S$ จึงเป็นปลายเงา',
        '• เมื่อวาดครบจะได้สามเหลี่ยม $TBS$ ที่มีด้าน $TB = 20$ เมตร '
        'และมีเงาที่โจทย์ถามคือด้าน $BS$ ซึ่งวัดไปตามพื้นลาด',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาความยาว $BS$ ซึ่งคือความยาวเงาที่วัดตามพื้นลาด',
        '',
        '<b>【 อ่านมุมภายในทั้งสามของสามเหลี่ยม $TBS$ จากรูปที่วาด โดยดูทีละจุดว่ารังสีสองเส้นที่ออกจากจุดนั้น '
        'ชี้ไปทางไหนบ้าง แล้วจึงใช้กฎของไซน์เพียงครั้งเดียวเพื่อดึงด้าน $BS$ ออกมา 】</b>',
        '',
        '<b>ขั้นที่ 1 · หามุมที่โคนเสา คือมุม $T\\hat{B}S$</b>',
        '• ที่จุด $B$ มีรังสีสองเส้นที่เป็นด้านของสามเหลี่ยม : เส้นหนึ่งชี้ขึ้นตรง ๆ ไปหายอดเสา $T$ '
        'อีกเส้นหนึ่งชี้เฉียงขึ้นไปทางขวาตามพื้นลาดไปหาปลายเงา $S$',
        '• เทียบทั้งสองเส้นกับแนวระดับเส้นเดียวกัน : เส้นที่ชี้ไปหา $T$ ทำมุม $90^{\\circ}$ '
        'ส่วนเส้นที่ชี้ไปหา $S$ ทำมุม $15^{\\circ}$',
        '• ทั้งสองเส้นเงยขึ้นทางเดียวกันจากแนวระดับ มุมระหว่างกันจึงเป็นผลต่าง : '
        '$T\\hat{B}S = 90^{\\circ} - 15^{\\circ} = 75^{\\circ}$',
        '• ⛔ จุดที่พลาดกันบ่อยคือเผลอตอบ $90^{\\circ} + 15^{\\circ} = 105^{\\circ}$ '
        'ค่านั้นคือมุมระหว่างเสากับพื้นลาดที่ไต่<b>ลง</b>ไปอีกฝั่ง ซึ่งไม่ใช่ด้านของสามเหลี่ยมรูปนี้เลย',
        '• ตรวจกับรูปทันที : พื้นลาดเงยขึ้นไปทางเดียวกับที่เสาชี้ ⇒ พื้นลาดจึง<b>หุบเข้าหา</b>เสา '
        'มุมที่โคนเสาต้องแคบกว่ามุมฉาก ⇒ $75^{\\circ}$ สมเหตุสมผล ส่วน $105^{\\circ}$ ขัดกับรูป',
        '',
        '<b>ขั้นที่ 2 · หามุมที่ปลายเงา คือมุม $T\\hat{S}B$ แล้วต่อด้วยมุมที่ยอดเสา</b>',
        '• ที่จุด $S$ ก็มีรังสีสองเส้นเช่นกัน : เส้นหนึ่งชี้ย้อนลงตามพื้นลาดกลับไปหาโคนเสา $B$ '
        'อีกเส้นหนึ่งชี้เฉียงขึ้นไปทางซ้ายไปหายอดเสา $T$ ซึ่งก็คือทิศที่ดวงอาทิตย์อยู่',
        '• เส้นที่ชี้กลับไปหา $B$ คือทิศไต่<b>ลง</b>ของพื้นลาด จึงกดต่ำกว่าแนวระดับอยู่ $15^{\\circ}$',
        '• เส้นที่ชี้ไปหา $T$ คือแนวเงยขึ้นหาดวงอาทิตย์ ทำมุม $60^{\\circ}$ กับแนวระดับ',
        '• คราวนี้สองเส้นอยู่<b>คนละข้าง</b>ของแนวระดับ (เส้นหนึ่งกดลง อีกเส้นเงยขึ้น) '
        'มุมระหว่างกันจึงเป็นผลบวก : $T\\hat{S}B = 60^{\\circ} + 15^{\\circ} = 75^{\\circ}$',
        '• ⛔ จุดที่พลาดกันมากที่สุดของทั้งข้อคือเผลอตอบ $60^{\\circ} - 15^{\\circ} = 45^{\\circ}$ '
        'เพราะนึกภาพว่าคนยืนบนพื้นลาดแล้วเงยมองดวงอาทิตย์ '
        'ภาพนั้นจะถูกก็ต่อเมื่อเนินเงยขึ้น<b>เข้าหา</b>ดวงอาทิตย์ '
        'แต่ข้อนี้เนินเงยขึ้น<b>หนี</b>ดวงอาทิตย์ (เพราะเงาทอดขึ้นเนิน) ⇒ ต้องบวก ไม่ใช่ลบ',
        '• เมื่อรู้สองมุมแล้ว มุมที่สามได้มาฟรีจากผลรวมมุมภายใน '
        'มุมที่ยอดเสา $= 180^{\\circ} - 75^{\\circ} - 75^{\\circ} = 30^{\\circ}$',
        '• ⭐ สังเกตของแถมที่จะได้ใช้ตอนตรวจ : มุมที่โคนเสากับมุมที่ปลายเงาเท่ากันพอดีที่ $75^{\\circ}$ '
        'สามเหลี่ยม $TBS$ จึงเป็นสามเหลี่ยมหน้าจั่ว ⇒ ด้านตรงข้ามมุมคู่นั้นยาวเท่ากัน คือ $TS = TB = 20$ เมตร '
        'แปลว่าลำแสงช่วงจากยอดเสาถึงปลายเงายาว $20$ เมตรเท่ากับตัวเสาพอดี',
        '',
        '<b>ขั้นที่ 3 · ใช้กฎของไซน์ในสามเหลี่ยม $TBS$ หาความยาวเงา</b>',
        '• จับคู่ด้านกับมุมตรงข้ามให้ถูกก่อนแทนค่า : ด้าน $BS$ ซึ่งคือเงา อยู่ตรงข้ามมุมที่ยอดเสา คือ $30^{\\circ}$ '
        'ส่วนด้าน $TB$ ซึ่งคือเสายาว $20$ เมตร อยู่ตรงข้ามมุมที่ปลายเงา คือ $75^{\\circ}$',
        '• เขียนสูตรก่อน : $\\dfrac{BS}{\\sin 30^{\\circ}} = \\dfrac{TB}{\\sin 75^{\\circ}}$',
        '• ย้ายข้างให้เหลือสิ่งที่ต้องการอยู่เดี่ยว ๆ : $BS = \\dfrac{20\\sin 30^{\\circ}}{\\sin 75^{\\circ}}$',
        '• แทนค่า : $BS = \\dfrac{20 \\times \\dfrac{1}{2}}{\\dfrac{\\sqrt{6} + \\sqrt{2}}{4}} '
        '= \\dfrac{10}{\\dfrac{\\sqrt{6} + \\sqrt{2}}{4}} = \\dfrac{40}{\\sqrt{6} + \\sqrt{2}}$',
        '• ตัวส่วนยังมีกรณฑ์อยู่ ให้คูณทั้งเศษและส่วนด้วยสังยุค $\\sqrt{6} - \\sqrt{2}$ : '
        '$BS = \\dfrac{40\\left(\\sqrt{6} - \\sqrt{2}\\right)}{\\left(\\sqrt{6}\\right)^{2} - \\left(\\sqrt{2}\\right)^{2}} '
        '= \\dfrac{40\\left(\\sqrt{6} - \\sqrt{2}\\right)}{4} = 10\\left(\\sqrt{6} - \\sqrt{2}\\right)$',
        '• คิดเป็นทศนิยมคร่าว ๆ : $\\sqrt{6} \\approx 2.449$ และ $\\sqrt{2} \\approx 1.414$ '
        'จึงได้ $BS \\approx 10 \\times 1.035 = 10.35$ เมตร',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · วางระบบพิกัดแล้วหาจุดตัดของลำแสงกับพื้นลาดตรง ๆ '
        '⛔ ไม่แตะมุมภายในสามเหลี่ยมชุดเดิมเลยแม้แต่มุมเดียว)</b>',
        '• วางโคนเสาไว้ที่จุดกำเนิด ได้ $B = (0, 0)$ และยอดเสา $T = (0, 20)$ '
        'ส่วนพื้นลาดคือเส้นตรง $y = x\\tan 15^{\\circ}$ สำหรับ $x \\ge 0$',
        '• ลำแสงออกจาก $T$ ลงไปทางขวาโดยกดลง $60^{\\circ}$ จากแนวระดับ '
        'เขียนเป็นเส้นทางเดินได้ว่า $(x, y) = \\left(s\\cos 60^{\\circ},\\ 20 - s\\sin 60^{\\circ}\\right)$ '
        'เมื่อ $s$ คือระยะที่เดินไปตามลำแสง',
        '• ปลายเงาคือจุดที่ลำแสงชนพื้นลาด จึงต้องมี '
        '$20 - s\\sin 60^{\\circ} = \\left(s\\cos 60^{\\circ}\\right)\\tan 15^{\\circ}$',
        '• ย้ายข้าง : $20 = s\\left(\\sin 60^{\\circ} + \\cos 60^{\\circ}\\tan 15^{\\circ}\\right)$ '
        'และค่าในวงเล็บคือ $\\dfrac{\\sqrt{3}}{2} + \\dfrac{1}{2}\\left(2 - \\sqrt{3}\\right) = 1$ พอดี '
        '⇒ $s = 20$ ซึ่งตรงกับที่ขั้นที่ 2 ทำนายไว้ว่าลำแสงช่วงนี้ยาวเท่ากับเสา ✓',
        '• แทนกลับได้ปลายเงา $S = \\left(10,\\ 20 - 10\\sqrt{3}\\right)$ '
        'จากนั้นวัดระยะจากโคนเสา : $BS = \\sqrt{10^{2} + \\left(20 - 10\\sqrt{3}\\right)^{2}} '
        '= 20\\sqrt{2 - \\sqrt{3}} \\approx 10.35$ เมตร',
        '• เดินคนละเส้นทางกันโดยสิ้นเชิงแต่ได้ $10.35$ เท่ากัน ✓ '
        'และ $20\\sqrt{2 - \\sqrt{3}}$ กับ $10\\left(\\sqrt{6} - \\sqrt{2}\\right)$ เป็นจำนวนเดียวกันจริง '
        'เพราะยกกำลังสองแล้วได้ $400\\left(2 - \\sqrt{3}\\right) = 800 - 400\\sqrt{3}$ เท่ากันทั้งคู่',
        '• ⭐ ตัวตรวจสามัญสำนึกที่คัดตัวเลือกทิ้งได้สามตัวในบรรทัดเดียว : '
        'ถ้าพื้นเป็นพื้นราบ เงาจะยาว $\\dfrac{20}{\\tan 60^{\\circ}} = \\dfrac{20\\sqrt{3}}{3} \\approx 11.55$ เมตร '
        'แต่พื้นลาด<b>ยกตัวขึ้นมารับลำแสงก่อนถึงระยะนั้น</b> เงาจึงต้อง<b>สั้นกว่า</b> $11.55$ เสมอ '
        '⇒ มีเพียง $10.35$ เท่านั้นที่ผ่านเงื่อนไขนี้ ส่วน $11.55$ · $14.14$ และ $24.49$ ตกทันที',
        '',
        '✅ <b>คำตอบ</b> เงาของเสาที่วัดตามพื้นลาดยาว $10\\left(\\sqrt{6} - \\sqrt{2}\\right)$ เมตร '
        'หรือประมาณ $10.35$ เมตร → <b>ตัวเลือก 1</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• โจทย์เงาบนพื้นลาดทุกข้อ ให้ตัดสินก่อนเป็นอันดับแรกว่า<b>เนินเงยเข้าหาหรือเงยหนีดวงอาทิตย์</b> '
        'เพราะคำตอบทั้งข้อแขวนอยู่กับข้อนี้ข้อเดียว · เงาทอด<b>ขึ้น</b>เนิน แปลว่าเนินเงยหนี ⇒ มุมที่ปลายเงาเป็นผลบวก '
        'ถ้าเงาทอด<b>ลง</b>เนิน จึงจะเป็นผลลบ',
        '• มุมภายในของสามเหลี่ยมต้องอ่านจาก<b>รังสีที่ชี้ไปหาจุดยอดอีกสองจุดจริง ๆ</b> '
        'เส้นตรงหนึ่งเส้นมีสองทิศเสมอ หยิบผิดทิศจะได้มุมที่ต่างไป $180^{\\circ}$ ลบออก '
        'ซึ่งบวกกันแล้วก็ยังได้ $180^{\\circ}$ อยู่ดี จึงจับไม่ได้ด้วยการบวกมุม',
        '• ⛔ อย่าใช้ “บวกสามมุมได้ $180^{\\circ}$” เป็นด่านตรวจว่ารูปถูก '
        'ให้ตรวจด้วยเครื่องมือที่<b>ไม่พึ่งมุมชุดเดิม</b>แทน เช่น วางพิกัดแล้วหาจุดตัด หรือเทียบกับกรณีพื้นราบ '
        'ซึ่งคิดได้ในหัวและตัดตัวเลือกทิ้งได้ทันที',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ $\\dfrac{20\\sqrt{3}}{3} \\approx 11.55$ เพราะลืมไปเลยว่าพื้นเป็นทางลาด '
        'แล้วคิดเหมือนเงาทอดบนพื้นราบ จึงใช้สามเหลี่ยมมุมฉากธรรมดา '
        '$\\dfrac{20}{\\tan 60^{\\circ}} = \\dfrac{20\\sqrt{3}}{3}$ · '
        'ค่านี้ผิดแน่นอนเพราะไม่ได้ใช้เลข $15^{\\circ}$ ที่โจทย์ให้มาเลยแม้แต่ครั้งเดียว '
        'และค่านี้ยังเป็น<b>ขอบบน</b>ของคำตอบพอดี ⇒ คำตอบจริงต้องน้อยกว่านี้เสมอ',
        '• ได้ $10\\sqrt{2} \\approx 14.14$ เพราะวาดรูปกลับด้าน คิดว่าเงาทอด<b>ลง</b>ตามพื้นลาด '
        'ซึ่งจะได้มุมโคนเสา $90^{\\circ} + 15^{\\circ} = 105^{\\circ}$ และมุมปลายเงา '
        '$60^{\\circ} - 15^{\\circ} = 45^{\\circ}$ จึงคิดเป็น '
        '$\\dfrac{20\\sin 30^{\\circ}}{\\sin 45^{\\circ}} = 10\\sqrt{2}$ · '
        '⛔ ค่านี้อันตรายที่สุดเพราะมุมชุดนี้ก็บวกได้ $180^{\\circ}$ เหมือนกัน '
        'จึงรอดด่านบวกมุมไปได้ · ตัวจับที่ได้ผลคือเทียบกับพื้นราบ : $14.14 > 11.55$ '
        'แปลว่าเงาบนเนินยาวกว่าเงาบนพื้นราบ ซึ่งขัดกับภาพที่เนินยกขึ้นมารับแสง',
        '• ได้ $10\\sqrt{6} \\approx 24.49$ เพราะลอกมุมเงย $60^{\\circ}$ มาใช้เป็นมุมที่ยอดเสาโดยตรง '
        'แทนที่จะเป็น $30^{\\circ}$ ที่คำนวณมา แล้วยังใช้ $45^{\\circ}$ ที่ปลายเงาซ้ำอีก จึงคิดเป็น '
        '$\\dfrac{20\\sin 60^{\\circ}}{\\sin 45^{\\circ}} = 10\\sqrt{6}$ · '
        'ค่านี้ยาวกว่าตัวเสาเสียอีก ทั้งที่แสงส่องเอียง $60^{\\circ}$ ซึ่งค่อนข้างชัน '
        'เงาจึงต้องสั้นกว่าเสาแน่ ๆ ⇒ ตัดทิ้งได้ตั้งแต่ยังไม่จัดรูป',
        '• อีกทางที่พลาดได้คือตอบ $20$ เพราะไปหยิบความยาวลำแสงช่วง $TS$ มาตอบแทนเงา $BS$ · '
        'สองอย่างนี้ยาวไม่เท่ากัน $TS$ คือระยะที่แสงเดินในอากาศ ส่วน $BS$ คือรอยเงาที่ทาบอยู่บนพื้นลาด '
        'โจทย์ถามอย่างหลัง ให้ย้อนอ่านคำถามอีกครั้งก่อนวงคำตอบเสมอ',
    ],
    'V.mold: G = a vertical pole at the foot of an inclined slope with the sun elevation given / '
    'A = the length of the shadow measured up the slope / M = assemble the three interior angles of the '
    'oblique triangle by reading the actual rays at each vertex, then one application of the law of sines. '
    'Rubric F2 C2 P2 T2 L1 = 9/15 with total at least 8 -> level: ยาก. '
    'F = 2 because two knowledge blocks are needed: reading every stated direction against one shared '
    'horizontal reference line, and the law of sines. F was deliberately not raised to 3, because reading '
    'the definition of an angle of elevation is not a separate new knowledge block on top of those two, '
    'it is part of the same reference-line reading. C = 2 because the item genuinely crosses 7.10 (turning '
    'a worded outdoor scene into angles) into 7.9 (solving the oblique triangle); neither half alone '
    'answers it. P = 2 for the two-stage chain, all three angles first and only then the side. T = 2 for '
    'the twin turning points that carry the whole item: at the pole foot the slope closes in toward the '
    'pole so the angle is 90 - 15, while at the shadow tip the hill tilts away from the sun so the angle '
    'is 60 + 15, and a student who copies one sign onto the other lands on a distractor either way. '
    'L = 1 because everything lies in a single vertical plane, which the stem states outright, so this is '
    'a plane scene and not a three-dimensional one; that follows the q089 and q077 precedent where a '
    'single-plane worded context scores 1 and a genuinely spatial scene scores 2. '
    'Scoring was written before the level was read off. '
    'sympy: angle at the pole foot = 5*pi/12 (75 deg), at the shadow tip = 5*pi/12 (75 deg), at the pole '
    'top = pi/6 (30 deg). The triangle is therefore isosceles and TS = TB = 20 exactly, which the '
    'coordinate check reproduces as the ray parameter s = 20. The law-of-sines expression '
    '20*sin(pi/6)/sin(5*pi/12) radsimplifies to 10*(sqrt(6)-sqrt(2)) = 10.352762. The independent check is '
    'a coordinate solve that never touches those angles: solving 20 - s*sin(60 deg) = s*cos(60 deg)*tan(15 '
    'deg) gives s = 20 and S = (10, 20 - 10*sqrt(3)), and sqrt(10**2 + (20-10*sqrt(3))**2) = '
    '20*sqrt(2-sqrt(3)), which equals 10*(sqrt(6)-sqrt(2)) since both square to 800 - 400*sqrt(3). '
    'All three distractors machine-computed from named error paths: 20*sqrt(3)/3 = 11.547005 from '
    'forgetting the slope and treating the ground as flat, 10*sqrt(2) = 14.142136 from drawing the mirror '
    'figure in which the shadow runs down the slope (angles 105, 45, 30), and 10*sqrt(6) = 24.494897 from '
    'copying the 60 degree elevation straight onto the pole top instead of the computed 30. A one-line '
    'bound rules out three of the four options: the flat-ground shadow is 20/tan(60 deg) = 11.547005 and a '
    'slope that rises to meet the ray must shorten the shadow, so the answer has to be below 11.547005 and '
    'only 10.352762 qualifies. Choices are in ascending numeric order (10.35, 11.55, 14.14, 24.49) so the '
    'answer slot is forced by the values, not chosen. '
    'CORRECTION 2026-08-05: this item shipped with correct = 2 (10*sqrt(2)), which was wrong. The original '
    'write-up placed the angle at the pole foot at 90 + 15 = 105 and the angle at the shadow tip at '
    '60 - 15 = 45. Both are the mirror figure, in which the shadow would run down the slope rather than up '
    'it. The error survived every gate because 105 + 45 + 30 also sums to 180, and because the original '
    'so-called independent check re-used the same three angles through the law of cosines, so it confirmed the '
    'wrong figure instead of testing it. sympy confirmed the wrong numbers faithfully, since it was fed the '
    'wrong angles. An independent blind solver caught it on the first pass. The lesson recorded here: a '
    'check that reuses the same angle assignment is not an independent check, and an angle sum of 180 '
    'proves nothing about whether the assignment matches the drawing. '
    'Collision sweep on 6402 items (bank 62 files + k1 out + k2 out), probe collide_b17c.py: the word เงา '
    'in the sun-shadow sense does not appear in a single item corpus-wide; the 8 hits the probe returned are '
    'all other words that merely share the letters. The nearest item is chap-07-trigonometry-q224 (a radio '
    'mast 40 m tall standing on a hill, two angles given, asking for the length of a guy wire): it differs '
    'on G (it hands over a measured distance and measured angles, whereas this item hands over a pole '
    'height, a sun elevation and a slope inclination) and it differs on A (guy-wire length vs shadow '
    'length), so 2 of the 3 axes differ and rule 5 is satisfied.',
)

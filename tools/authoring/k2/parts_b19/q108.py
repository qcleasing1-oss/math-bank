# -*- coding: utf-8 -*-
add(
    108,
    ['7.1'],
    'ยาก',
    'รูปสามเหลี่ยม $ABC$ มีมุม $B$ เป็นมุมฉาก จุด $D$ เป็นจุดบนด้าน $BC$ '
    'ซึ่งทำให้มุม $A\\hat{D}B$ มีขนาด $60^{\\circ}$ '
    'ถ้ามุม $A\\hat{C}B$ มีขนาด $30^{\\circ}$ และ $DC$ ยาว $12$ หน่วย แล้ว $AB$ ยาวกี่หน่วย',
    [
        '$3\\sqrt{3}$',
        '$6$',
        '$4\\sqrt{3}$',
        '$6\\sqrt{3}$',
    ],
    3,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• อัตราส่วนแทนเจนต์ของมุมแหลมในสามเหลี่ยมมุมฉาก คือความยาวด้านตรงข้ามมุมนั้น '
        'หารด้วยความยาวด้านประชิดมุมนั้น เขียนเป็นสูตรว่า '
        '$\\tan\\theta = \\dfrac{\\text{ด้านตรงข้าม}}{\\text{ด้านประชิด}}$ '
        '⛔ คำว่า “ด้านประชิด” ในสูตรนี้หมายถึงด้านที่ประกอบมุมฉากเท่านั้น '
        'ไม่ใช่ด้านตรงข้ามมุมฉาก ซึ่งเป็นจุดที่สับสนกันบ่อยที่สุด',
        '• เมื่อรู้ด้านตรงข้ามแล้วอยากได้ด้านประชิด ให้ย้ายข้างสูตรข้างบน '
        'คูณไขว้ได้ $\\tan\\theta \\times (\\text{ด้านประชิด}) = \\text{ด้านตรงข้าม}$ '
        'แล้วหารทั้งสองข้างด้วย $\\tan\\theta$ ได้ '
        '$\\text{ด้านประชิด} = \\dfrac{\\text{ด้านตรงข้าม}}{\\tan\\theta}$ '
        'อ่านเป็นภาษาคนว่า “ฐาน เท่ากับ ความสูง หารด้วย แทนของมุม”',
        '• ค่าตรีโกณของมุมพิเศษที่ต้องใช้ ได้มาจากสามเหลี่ยมด้านเท่าที่ผ่าครึ่ง '
        'ซึ่งมีด้านเป็น $1$, $\\sqrt{3}$ และ $2$ โดยด้าน $1$ อยู่ตรงข้ามมุม $30^{\\circ}$ '
        'และด้าน $\\sqrt{3}$ อยู่ตรงข้ามมุม $60^{\\circ}$ จึงได้ '
        '$\\tan 30^{\\circ} = \\dfrac{1}{\\sqrt{3}}$ · $\\tan 60^{\\circ} = \\sqrt{3}$ · '
        '$\\sin 60^{\\circ} = \\dfrac{\\sqrt{3}}{2}$ · $\\cos 60^{\\circ} = \\dfrac{1}{2}$',
        '• จุดที่อยู่ “บนด้าน” ของรูปเหลี่ยม แปลว่าจุดนั้นอยู่ระหว่างปลายทั้งสองของด้านนั้น '
        'ดังนั้นถ้าจุด $D$ อยู่บนด้าน $BC$ แล้วจุด $B$ จุด $D$ และจุด $C$ '
        'จะเรียงอยู่บนเส้นตรงเดียวกันตามลำดับนี้ ทำให้ $BD + DC = BC$ '
        'ซึ่งย้ายข้างได้เป็น $DC = BC - BD$ ⛔ ไม่ใช่ $BD - BC$ และไม่ใช่ผลบวก',
        '• มุมสองมุมที่อยู่บนเส้นตรงเดียวกันและประชิดกัน รวมกันได้ $180^{\\circ}$ เสมอ '
        'เรียกว่ามุมประชิดบนเส้นตรง เพราะเส้นตรงหนึ่งเส้นกางเป็นมุมตรงขนาด $180^{\\circ}$ '
        'สมบัตินี้จะถูกใช้ตอนตรวจคำตอบด้วยเส้นทางที่สอง',
        '• สามเหลี่ยมหน้าจั่วมีสมบัติว่า ถ้ามุมสองมุมของสามเหลี่ยมมีขนาดเท่ากัน '
        'แล้วด้านที่อยู่ตรงข้ามมุมทั้งสองนั้นจะยาวเท่ากันด้วย '
        'และสมบัตินี้ใช้ย้อนกลับได้ทั้งสองทิศทาง จึงเป็นเครื่องมือที่ทำให้ '
        '“รู้มุม” กลายเป็น “รู้ความยาว” ได้โดยไม่ต้องคำนวณอะไรเลย',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• รูปสามเหลี่ยม $ABC$ มีมุม $B$ เป็นมุมฉาก แปลว่าด้าน $AB$ ตั้งฉากกับด้าน $BC$',
        '• จุด $D$ เป็นจุดที่อยู่บนด้าน $BC$ นั่นคืออยู่ระหว่างจุด $B$ กับจุด $C$ '
        'จึงมีจุดสามจุดเรียงกันบนเส้นตรงเดียวกันตามลำดับ $B$ แล้ว $D$ แล้ว $C$ '
        'และเมื่อลากส่วนของเส้นตรง $AD$ ขึ้นไปหาจุดยอด $A$ จะเกิดสามเหลี่ยมมุมฉากซ้อนกันสองรูป '
        'คือรูปเล็ก $ABD$ กับรูปใหญ่ $ABC$ ซึ่งใช้ด้าน $AB$ ร่วมกันและมีมุมฉากที่จุด $B$ ร่วมกัน',
        '• มุม $A\\hat{D}B$ ซึ่งเป็นมุมที่จุด $D$ ในสามเหลี่ยมรูปเล็ก มีขนาด $60^{\\circ}$',
        '• มุม $A\\hat{C}B$ ซึ่งเป็นมุมที่จุด $C$ ในสามเหลี่ยมรูปใหญ่ มีขนาด $30^{\\circ}$',
        '• ส่วนของเส้นตรง $DC$ ยาว $12$ หน่วย ซึ่งเป็นท่อนขวาของด้าน $BC$ '
        '⛔ ไม่ใช่ความยาวของด้าน $BC$ ทั้งเส้น',
        '• สังเกตหน้าตาก่อนลงมือ : โจทย์ให้ความยาวมาแค่ตัวเดียว และตัวนั้นไม่ใช่ด้านของสามเหลี่ยมมุมฉากรูปใดเลย '
        'แต่เป็น<b>ผลต่าง</b>ของฐานสองฐาน จึงเดาทางได้ตั้งแต่ยังไม่ลงมือว่า '
        'ต้องตั้งตัวแปรไว้ที่ด้านร่วม $AB$ แล้วเขียนฐานทั้งสองในรูปของตัวแปรตัวเดียวกัน '
        'จากนั้นค่อยเอาผลต่างไปเท่ากับ $12$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาความยาวของด้าน $AB$ ซึ่งเป็นด้านที่ตั้งฉากกับ $BC$ ที่จุด $B$',
        '',
        '<b>【 ตั้งให้ $AB = h$ แล้วใช้แทนเจนต์ของมุม $60^{\\circ}$ กับมุม $30^{\\circ}$ '
        'เขียนฐาน $BD$ และฐาน $BC$ ให้อยู่ในรูปของ $h$ ทั้งคู่ '
        'จากนั้นใช้ความจริงที่ว่า $DC = BC - BD$ ตั้งเป็นสมการตัวแปรเดียวแล้วแก้หา $h$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · วางรูปให้ชัดแล้วตั้งชื่อสิ่งที่ยังไม่รู้</b>',
        '• วาดเส้นแนวนอนหนึ่งเส้นแทนด้าน $BC$ วางจุด $B$ ไว้ซ้ายสุด จุด $C$ ไว้ขวาสุด '
        'แล้ววางจุด $D$ ไว้ระหว่างกลาง จากนั้นลากเส้นขึ้นในแนวตั้งจากจุด $B$ ไปยังจุด $A$ '
        'เส้นแนวตั้งนี้ตั้งฉากกับ $BC$ พอดี เพราะโจทย์บอกว่ามุม $B$ เป็นมุมฉาก',
        '• ต่อจุด $A$ ลงมาหาจุด $D$ และต่อจุด $A$ ลงมาหาจุด $C$ '
        'จะได้สามเหลี่ยมมุมฉากสองรูปที่ซ้อนกันอยู่ คือ $ABD$ กับ $ABC$',
        '• ⭐ กุญแจดอกแรกของทั้งข้อ : สามเหลี่ยมสองรูปนี้ใช้ด้าน $AB$ ร่วมกัน '
        'และมุม $A\\hat{B}D$ ก็เป็นมุมฉากเช่นเดียวกับมุม $A\\hat{B}C$ '
        'เพราะจุด $D$ อยู่บนรังสีเดียวกันกับจุด $C$ เมื่อมองจากจุด $B$ '
        'ดังนั้นตัวแปรที่ควรตั้งคือด้านร่วมนี้ ไม่ใช่ฐาน',
        '• ตั้งให้ $AB = h$ หน่วย โดย $h$ เป็นจำนวนบวก เพราะเป็นความยาวของด้าน',
        '',
        '<b>ขั้นที่ 2 · ใช้แทนเจนต์ของมุม $60^{\\circ}$ เขียนฐาน $BD$ ให้อยู่ในรูปของ $h$</b>',
        '• สูตรที่ใช้ : $\\text{ด้านประชิด} = \\dfrac{\\text{ด้านตรงข้าม}}{\\tan\\theta}$',
        '• ระบุตัวแปรให้ชัดก่อนแทนค่า : ทำงานอยู่ในสามเหลี่ยมมุมฉากรูปเล็ก $ABD$ '
        '· มุมที่หยิบมาใช้คือมุมที่จุด $D$ ซึ่งมีขนาด $60^{\\circ}$ '
        '· ด้านตรงข้ามมุมนี้คือ $AB$ ซึ่งยาว $h$ '
        '· ด้านประชิดมุมนี้ที่ประกอบมุมฉากด้วยคือ $BD$ ซึ่งเป็นสิ่งที่ต้องการเขียนออกมา',
        '• แทนค่า : $BD = \\dfrac{h}{\\tan 60^{\\circ}}$',
        '• ใส่ค่าของมุมพิเศษลงไป $\\tan 60^{\\circ} = \\sqrt{3}$ จึงยุบได้เป็น '
        '$BD = \\dfrac{h}{\\sqrt{3}}$',
        '• เก็บผลไว้ในใจว่า $BD$ สั้นกว่า $h$ อยู่เล็กน้อย เพราะหารด้วย $\\sqrt{3}$ '
        'ซึ่งมีค่าประมาณ $1.732$ นั่นสมเหตุสมผล เพราะมุมที่ $D$ ชันถึง $60^{\\circ}$ '
        'เท้าของเส้นจึงอยู่ใกล้จุด $B$',
        '',
        '<b>ขั้นที่ 3 · ใช้แทนเจนต์ของมุม $30^{\\circ}$ เขียนฐาน $BC$ ให้อยู่ในรูปของ $h$ ตัวเดิม</b>',
        '• สูตรที่ใช้ : $\\text{ด้านประชิด} = \\dfrac{\\text{ด้านตรงข้าม}}{\\tan\\theta}$ ตัวเดิมทุกประการ',
        '• ระบุตัวแปร : คราวนี้ทำงานในสามเหลี่ยมมุมฉากรูปใหญ่ $ABC$ '
        '· มุมที่หยิบมาใช้คือมุมที่จุด $C$ ซึ่งมีขนาด $30^{\\circ}$ '
        '· ด้านตรงข้ามมุมนี้ก็ยังคงเป็น $AB$ ซึ่งยาว $h$ ตัวเดียวกับขั้นที่แล้ว '
        '· ด้านประชิดคือ $BC$ ทั้งเส้น',
        '• แทนค่า : $BC = \\dfrac{h}{\\tan 30^{\\circ}}$',
        '• ใส่ค่าของมุมพิเศษ $\\tan 30^{\\circ} = \\dfrac{1}{\\sqrt{3}}$ '
        'การหารด้วยเศษส่วนคือการคูณด้วยส่วนกลับของตัวหาร จึงได้ '
        '$BC = h \\div \\dfrac{1}{\\sqrt{3}} = h \\times \\sqrt{3} = h\\sqrt{3}$',
        '• ⭐ ตรงนี้คือหัวใจที่ทำให้โจทย์แก้ได้ : ทั้ง $BD$ และ $BC$ ถูกเขียนด้วยตัวอักษร $h$ '
        'ตัวเดียวกันแล้ว เพราะทั้งสองรูปมองความสูง $AB$ เส้นเดียวกัน '
        'ของที่ไม่รู้ในโจทย์จึงเหลือเพียงตัวเดียว',
        '',
        '<b>ขั้นที่ 4 · ตั้งสมการจากผลต่างของสองฐานแล้วแก้หา $h$</b>',
        '• สูตรที่ใช้ : เพราะจุด $D$ อยู่ระหว่างจุด $B$ กับจุด $C$ จึงได้ $BD + DC = BC$ '
        'ย้ายข้างเป็น $DC = BC - BD$',
        '• ระบุตัวแปร : $DC = 12$ ตามที่โจทย์ให้ · $BC = h\\sqrt{3}$ จากขั้นที่ 3 '
        '· $BD = \\dfrac{h}{\\sqrt{3}}$ จากขั้นที่ 2',
        '• แทนค่าทั้งสามลงในสมการ : $12 = h\\sqrt{3} - \\dfrac{h}{\\sqrt{3}}$',
        '• ยุบข้างขวาโดยทำให้เป็นเศษส่วนที่มีตัวส่วนเดียวกันคือ $\\sqrt{3}$ '
        'เขียน $h\\sqrt{3}$ ใหม่เป็น $\\dfrac{h\\sqrt{3} \\times \\sqrt{3}}{\\sqrt{3}} '
        '= \\dfrac{3h}{\\sqrt{3}}$ เพราะ $\\sqrt{3} \\times \\sqrt{3} = 3$',
        '• ลบกันได้ $\\dfrac{3h}{\\sqrt{3}} - \\dfrac{h}{\\sqrt{3}} = \\dfrac{3h - h}{\\sqrt{3}} '
        '= \\dfrac{2h}{\\sqrt{3}}$ สมการจึงเหลือสั้น ๆ ว่า $\\dfrac{2h}{\\sqrt{3}} = 12$',
        '• แก้หา $h$ โดยคูณทั้งสองข้างด้วย $\\sqrt{3}$ ได้ $2h = 12\\sqrt{3}$ '
        'แล้วหารทั้งสองข้างด้วย $2$ ได้ $h = 6\\sqrt{3}$',
        '• แทนกลับเพื่อยืนยันว่าย้ายข้างไม่ผิด : ถ้า $h = 6\\sqrt{3}$ แล้ว '
        '$BD = \\dfrac{6\\sqrt{3}}{\\sqrt{3}} = 6$ และ $BC = 6\\sqrt{3} \\times \\sqrt{3} = 18$ '
        'ผลต่างคือ $18 - 6 = 12$ ซึ่งตรงกับ $DC$ ที่โจทย์กำหนดพอดี ✓ '
        'และ $12$ น้อยกว่า $18$ จริง จุด $D$ จึงตกอยู่ในด้าน $BC$ ไม่เลยออกไปข้างนอก ✓',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · ไล่มุมจนพบว่าสามเหลี่ยม $ADC$ เป็นสามเหลี่ยมหน้าจั่วที่มี '
        '$AD = DC = 12$ แล้วอ่าน $AB$ ด้วยไซน์ โดยไม่แตะแทนเจนต์และไม่ตั้งสมการเลยแม้แต่ครั้งเดียว)</b>',
        '• เริ่มจากมุมที่จุด $D$ : จุด $B$ จุด $D$ จุด $C$ อยู่บนเส้นตรงเดียวกัน '
        'มุม $A\\hat{D}B$ กับมุม $A\\hat{D}C$ จึงเป็นมุมประชิดบนเส้นตรง รวมกันได้ $180^{\\circ}$ '
        'ได้ว่า $A\\hat{D}C = 180^{\\circ} - 60^{\\circ} = 120^{\\circ}$',
        '• ไปที่สามเหลี่ยม $ADC$ ซึ่งมุมภายในสามมุมรวมกันได้ $180^{\\circ}$ '
        'รู้แล้วสองมุมคือ $A\\hat{D}C = 120^{\\circ}$ และ $A\\hat{C}D = 30^{\\circ}$ '
        'ซึ่งเป็นมุมเดียวกับมุม $A\\hat{C}B$ ที่โจทย์ให้ เพราะจุด $D$ อยู่บนด้าน $BC$ '
        'มุมที่จุด $C$ จึงกางเท่ากันไม่ว่าจะมองไปที่ $D$ หรือไปที่ $B$',
        '• หามุมที่เหลือ : $D\\hat{A}C = 180^{\\circ} - 120^{\\circ} - 30^{\\circ} = 30^{\\circ}$',
        '• ⭐ ภาพที่สวยที่สุดของข้อนี้โผล่ตรงนี้ : มุม $D\\hat{A}C$ กับมุม $D\\hat{C}A$ '
        'ต่างก็มีขนาด $30^{\\circ}$ เท่ากันพอดี สามเหลี่ยม $ADC$ จึงเป็นสามเหลี่ยมหน้าจั่ว '
        'และด้านที่อยู่ตรงข้ามมุมทั้งสองต้องยาวเท่ากัน '
        'ด้านตรงข้ามมุมที่ $A$ คือ $DC$ ส่วนด้านตรงข้ามมุมที่ $C$ คือ $AD$ '
        'จึงสรุปได้ทันทีว่า $AD = DC = 12$ หน่วย โดยไม่ต้องคำนวณอะไรเลย',
        '• เมื่อรู้ $AD$ แล้ว หันกลับไปมองสามเหลี่ยมมุมฉาก $ABD$ ซึ่ง $AD$ เป็นด้านตรงข้ามมุมฉาก '
        'ใช้สูตร $\\sin\\theta = \\dfrac{\\text{ด้านตรงข้าม}}{\\text{ด้านตรงข้ามมุมฉาก}}$ '
        'กับมุมที่ $D$ ขนาด $60^{\\circ}$ จะได้ '
        '$AB = AD\\sin 60^{\\circ} = 12 \\times \\dfrac{\\sqrt{3}}{2} = 6\\sqrt{3}$',
        '• เดินคนละเส้นทางกันโดยสิ้นเชิงแต่ได้ $6\\sqrt{3}$ เท่ากัน ✓ '
        'และเส้นทางนี้ยังแถมของให้ฟรีอีกชิ้น คือ '
        '$BD = AD\\cos 60^{\\circ} = 12 \\times \\dfrac{1}{2} = 6$ '
        'ซึ่งตรงกับ $BD = 6$ ที่คำนวณได้จากเส้นทางหลักพอดี ✓ '
        'เท่ากับตรวจซ้ำได้สองชั้นในคราวเดียว',
        '',
        '✅ <b>คำตอบ</b> ด้าน $AB$ ยาว $6\\sqrt{3}$ หน่วย → <b>ตัวเลือก 4</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอโจทย์ที่มีสามเหลี่ยมมุมฉากสองรูปซ้อนกันโดยใช้ความสูงเส้นเดียวกัน '
        'แล้วโจทย์ให้ระยะระหว่างเท้าของสองรูปมา ให้ตั้งตัวแปรไว้ที่<b>ความสูงที่ใช้ร่วมกัน</b>เสมอ '
        'ห้ามตั้งไว้ที่ฐาน เพราะฐานมีสองเส้นและจะกลายเป็นสองตัวแปรทันที '
        'พอตั้งที่ความสูงแล้ว ฐานทั้งสองจะถูกเขียนด้วยตัวแปรตัวเดียวกันโดยอัตโนมัติ',
        '• คู่มุม $30^{\\circ}$ กับ $60^{\\circ}$ มีของแถมที่ควรจำ คือ '
        '$\\tan 30^{\\circ} \\times \\tan 60^{\\circ} = \\dfrac{1}{\\sqrt{3}} \\times \\sqrt{3} = 1$ '
        'ฐานสองเส้นจึงเป็นส่วนกลับของกันและกันเมื่อเทียบกับความสูง '
        'ทำให้ผลต่างยุบเหลือ $\\dfrac{2h}{\\sqrt{3}}$ ซึ่งสั้นมาก '
        'ถ้าคิดแล้วนิพจน์ยาวรุงรัง ให้ย้อนกลับไปดูว่าหยิบมุมสลับกันหรือเปล่า',
        '• เห็นเลข $60^{\\circ}$ อยู่ที่จุดกลางบนเส้นตรง ให้คิดถึงมุมประชิดที่ได้ $120^{\\circ}$ ทันที '
        'แล้วไล่มุมในสามเหลี่ยมอีกรูปดู หลายครั้งจะเจอสามเหลี่ยมหน้าจั่วซ่อนอยู่ '
        'ซึ่งเปลี่ยนความยาวที่โจทย์ให้ไปติดตัวอีกด้านหนึ่งได้ฟรี ๆ '
        'เป็นทางลัดที่เร็วกว่าการตั้งสมการมาก',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $3\\sqrt{3}$ เพราะวางจุด $D$ ผิดข้าง คือไปวางไว้นอกส่วน $BC$ '
        'จึงเขียนความสัมพันธ์เป็นผลบวก $BC + BD = 12$ แทนที่จะเป็นผลต่าง '
        'ทำให้ได้ $h\\sqrt{3} + \\dfrac{h}{\\sqrt{3}} = \\dfrac{4h}{\\sqrt{3}} = 12 '
        '\\Rightarrow h = 3\\sqrt{3}$ · '
        'ค่านี้ผิดจริง ตรวจได้ด้วยการแทนกลับ : ถ้า $h = 3\\sqrt{3}$ แล้ว $BD = 3$ และ $BC = 9$ '
        'ทำให้ $DC = 9 - 3 = 6$ ซึ่งไม่ใช่ $12$ ที่โจทย์ให้ · '
        'วิธีกันคืออ่านคำว่า “จุดบนด้าน $BC$” ให้ขึ้นใจว่าแปลว่าอยู่<b>ระหว่าง</b>ปลายทั้งสอง '
        'จึงต้องเป็นผลต่างเสมอ',
        '• ได้ค่า $6$ เพราะไล่มุมจนได้ $AD = 12$ ถูกต้องแล้ว แต่ตอนอ่านค่าสุดท้ายหยิบผิดฟังก์ชัน '
        'ไปใช้ $AB = 12\\sin 30^{\\circ} = 6$ แทนที่จะเป็น $12\\sin 60^{\\circ}$ · '
        'ที่ผิดเพราะในสามเหลี่ยม $ABD$ มุมที่จุด $D$ คือ $60^{\\circ}$ ไม่ใช่ $30^{\\circ}$ '
        'และ $AB$ คือด้านตรงข้ามมุมที่ $D$ · '
        'ค่านี้ผิดจริง ตรวจได้ทันทีด้วยความยาว : ถ้า $AB = 6$ แล้ว $BC = 6\\sqrt{3}$ '
        'ซึ่งมีค่าประมาณ $10.39$ สั้นกว่า $DC = 12$ ทั้งที่ $DC$ เป็นเพียงท่อนหนึ่งของ $BC$ '
        'จึงเป็นไปไม่ได้ · สังเกตด้วยว่าเลข $6$ นี้แท้จริงคือความยาว $BD$ ไม่ใช่ $AB$',
        '• ได้ค่า $4\\sqrt{3}$ เพราะอ่านโจทย์ข้ามไป คิดว่า $12$ ที่โจทย์ให้คือความยาวของ $BC$ ทั้งเส้น '
        'จึงลืมสามเหลี่ยมรูปเล็กทิ้งไปเลย แล้วใช้มุม $30^{\\circ}$ กับ $BC$ ตรง ๆ '
        'ได้ $h = 12\\tan 30^{\\circ} = \\dfrac{12}{\\sqrt{3}} = 4\\sqrt{3}$ · '
        'ค่านี้ผิดจริง แทนกลับแล้วได้ $BC = 12$ และ $BD = 4$ ทำให้ $DC = 12 - 4 = 8$ '
        'ซึ่งไม่ใช่ $12$ · เส้นทางนี้ยังทิ้งเงื่อนไข $60^{\\circ}$ ไปเปล่า ๆ '
        'ให้ถือเป็นสัญญาณเตือนว่าถ้าแก้เสร็จแล้วยังมีตัวเลขในโจทย์ที่ไม่ได้ใช้เลย แปลว่าอ่านโจทย์ผิด',
        '• อีกทางที่พลาดกันบ่อยคือทำถูกตลอดจนได้ $AD = 12$ จากสามเหลี่ยมหน้าจั่ว '
        'แล้วดีใจว่าได้คำตอบ จึงตอบ $12$ ทันทีโดยลืมว่าโจทย์ถามหา $AB$ ไม่ใช่ $AD$ · '
        'ค่านี้ผิดเพราะ $AD$ เป็นด้านตรงข้ามมุมฉากของสามเหลี่ยม $ABD$ '
        'ซึ่งต้องยาวกว่าด้าน $AB$ เสมอ ยังต้องคูณด้วย $\\sin 60^{\\circ}$ อีกหนึ่งก้าวจึงจะได้ '
        '$6\\sqrt{3}$ ซึ่งมีค่าประมาณ $10.39$ สั้นกว่า $12$ จริงตามที่ควรเป็น · '
        'วิธีกันคือกลับไปอ่านประโยคคำถามอีกครั้งก่อนวงคำตอบทุกครั้ง',
    ],
    'V.mold: G = a right triangle ABC with the right angle at B, a point D taken on the side BC so that '
    'the angle ADB measures 60 degrees, the angle ACB measuring 30 degrees, and the single length DC = 12 '
    'handed over, which is the gap between the feet of the two slanted lines rather than a side of either '
    'right triangle / A = the length of the shared vertical leg AB / M = name the shared leg h, turn each '
    'of the two given angles into a base written in h through the tangent ratio, then use the collinearity '
    'of B, D, C to write DC = BC - BD as a one-variable equation and solve it. '
    'Rubric F2 C1 P3 T2 L1 = 9/15 with total 9 and T = 2 -> level: ยาก, the third of the four bands. '
    'F = 2 because exactly two knowledge blocks carry the item: the definition of the tangent ratio in a '
    'right triangle, and the exact values of the special angles 30 and 60; nothing beyond those two is '
    'needed on the main route. C = 1 because subtopic 7.1 is joined by one outside idea only, namely '
    'setting up an equation from the difference of two segments lying on the same line, which is plane '
    'geometry rather than a second trigonometric subtopic. P = 3, the ceiling, because the work really '
    'does pass through three stages that each hand an object to the next: BD written in h, then BC written '
    'in the same h, then the difference of those two expressions set equal to 12 and solved; the benchmark '
    'is q107, which was held at P = 2 because its second stage merely reads a ratio off sides already '
    'produced instead of building a third object. T = 2 because two keys must be found and neither is '
    'stated: the solver must see that AB is the leg shared by both right triangles and place the variable '
    'there rather than on a base, and must see that DC = BC - BD rather than a sum or the reverse '
    'difference. T is not 3 because once those two keys are turned the route is forced, with no branch to '
    'choose and no spurious root to discard. L = 1 because there is no figure supplied and the solver must '
    'draw two nested right triangles and place the four labels correctly, but the scene stays inside one '
    'plane with no modelling of a worded situation; the benchmark is q107, held at L = 1 for the same '
    'reason. Total 9 clears the threshold of 8 with T at least 2, and falls short of the 12 needed for the '
    'top band, and no dimension was inflated to close that gap. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b19.py): with BD = h/tan(60 degrees) and BC = h/tan(30 degrees), '
    'solve(Eq(BC - BD, 12), h) returns 6*sqrt(3) exactly, and back-substitution gives BD = 6, BC = 18, '
    'BC - BD = 12. The independent angle-chase route was machine checked separately: 12*sin(60 degrees) '
    'returns 6*sqrt(3), matching the main route, and 12*cos(60 degrees) returns 6, matching the BD found '
    'on the main route, so the two routes agree on two different quantities and not merely on the final '
    'answer. Every distractor was machine-computed from a named error path rather than invented: '
    'solve(Eq(BC + BD, 12), h) returns 3*sqrt(3) for placing D outside the segment and adding instead of '
    'subtracting, 12*sin(30 degrees) returns 6 for picking the wrong special angle after the isosceles '
    'step, and 12*tan(30 degrees) returns 4*sqrt(3) for reading the given 12 as the whole of BC. Each was '
    'then refuted by feeding it back through the main relation: h = 3*sqrt(3) yields DC = 6, h = 6 yields '
    'DC = 4*sqrt(3) which is about 6.93, and h = 4*sqrt(3) yields DC = 8, none of which is 12. The '
    'ordering assertion order([3*sqrt(3), 6, 4*sqrt(3), 6*sqrt(3)]) passed on the numeric keys 5.196, 6, '
    '6.928 and 10.392. '
    'Collision sweep on 6417 items (bank 63 files + k1 out + k2 out), probe collide_b19.py / '
    'collide_b19b.py: scan A4 intersected the phrase for a point lying on a stated side with the word for '
    'right angle, and scan A4b searched for the wording that describes the gap between the feet of two '
    'slanted lines in the same figure; three items surfaced and none shares this mold. '
    'gen-chap-07-q126 concerns a line drawn parallel to a side inside a triangle, chap-13-q233 is a '
    'calculus optimisation that merely mentions a right angle, and pat1-2564-03-q21 drops an altitude onto '
    'the hypotenuse and then asks for a compound-angle expression, so its A and its M both differ. The '
    'pairing of two nested right triangles sharing one leg with a segment difference as the only supplied '
    'length is empty in the corpus. Choices are ordered ascending by numeric value (3*sqrt(3) about 5.196, '
    'then 6, then 4*sqrt(3) about 6.928, then 6*sqrt(3) about 10.392), so the answer slot is forced by '
    'that rule and was not chosen.',
)

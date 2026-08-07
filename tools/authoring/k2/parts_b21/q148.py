# -*- coding: utf-8 -*-
add(
    148,
    ['7.1'],
    'ยาก',
    'รูปสามเหลี่ยม $ABC$ มีมุม $C$ เป็นมุมฉาก ถ้าด้าน $AB$ ยาวกว่าด้าน $BC$ อยู่ $2$ หน่วย '
    'และด้าน $AB$ ยาวกว่าด้าน $CA$ อยู่ $9$ หน่วย แล้วค่าของ $\\tan A$ เท่ากับข้อใด',
    [
        '$\\dfrac{8}{15}$',
        '$\\dfrac{3}{4}$',
        '$\\dfrac{15}{8}$',
        '$\\dfrac{9}{2}$',
    ],
    2,
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ตั้งชื่อด้านให้เรียบร้อยก่อนเป็นอันดับแรก เพราะข้อนี้ไม่ได้ให้ความยาวด้านใดมาเป็นตัวเลขเลยสักด้าน : '
        'ให้ $a$ แทนความยาวด้าน $BC$ ซึ่งอยู่<b>ตรงข้าม</b>มุม $A$ · ให้ $b$ แทนความยาวด้าน $CA$ '
        'ซึ่งเป็นด้าน<b>ประชิด</b>มุม $A$ · ให้ $c$ แทนความยาวด้าน $AB$ · '
        'เมื่อมุม $C$ เป็นมุมฉาก ด้าน $AB$ ซึ่งอยู่ตรงข้ามมุม $C$ จึงเป็นด้านตรงข้ามมุมฉาก '
        'และเป็นด้านที่ยาวที่สุดของรูปเสมอ',
        '• นิยามอัตราส่วนตรีโกณมิติในสามเหลี่ยมมุมฉากต้องอ่านจากมุมที่สนใจเสมอ : $\\tan A$ '
        'คือความยาวด้านตรงข้ามมุม $A$ หารด้วยความยาวด้านประชิดมุม $A$ ⇒ $\\tan A = \\dfrac{BC}{CA} = \\dfrac{a}{b}$ · '
        'เหตุผลมาจาก $\\tan A = \\dfrac{\\sin A}{\\cos A} = \\dfrac{a/c}{b/c} = \\dfrac{a}{b}$ '
        'ซึ่งด้านตรงข้ามมุมฉาก $c$ ตัดกันหายไปพอดี · ⛔ ระวังการกลับเศษกับส่วน เพราะ $\\dfrac{b}{a}$ '
        'ไม่ใช่ $\\tan A$ แต่เป็น $\\tan B$ (มุม $B$ มีด้านตรงข้ามคือ $b$ และมีด้านประชิดคือ $a$)',
        '• ทฤษฎีบทพีทาโกรัส : ในสามเหลี่ยมมุมฉาก กำลังสองของด้านตรงข้ามมุมฉากเท่ากับผลบวกของกำลังสองของ'
        'ด้านประกอบมุมฉากทั้งสอง ⇒ $a^2 + b^2 = c^2$ · สมการนี้คือสะพานเส้นเดียวที่ผูกความยาวทั้งสามด้านไว้ด้วยกัน '
        '⇒ เมื่อโจทย์ให้ความสัมพันธ์ระหว่างด้านมาสองข้อ สะพานเส้นนี้จะเติมข้อที่สามให้ครบพอดี',
        '• ⭐ <b>กุญแจดอกที่หนึ่งของข้อนี้</b> : โจทย์ให้<b>ผลต่าง</b>ของความยาวมาสองคู่ '
        'และทั้งสองคู่ต่างก็วัดออกจากด้านเดียวกันคือด้าน $AB$ ⇒ ถ้าตั้งให้ $AB$ เป็นตัวแปรเดียวของทั้งข้อ '
        'อีกสองด้านจะเขียนแทนด้วยตัวแปรนั้นได้ทันทีในรูป $c-2$ กับ $c-9$ '
        '⇒ พีทาโกรัสที่เดิมมีสามตัวแปรจะยุบเหลือสมการเดียวที่มีตัวแปรเดียว',
        '• ⭐ <b>กุญแจดอกที่สองของข้อนี้</b> : รากของสมการกำลังสองเป็นเพียง<b>ผู้เข้าชิง</b> ยังไม่ใช่คำตอบ '
        'ต้องเอาไปตรวจกับความเป็นจริงทางเรขาคณิตทุกรากก่อน เพราะความยาวด้านต้องเป็นจำนวนบวกเสมอ · '
        '⛔ จุดที่พลาดกันมากคือตรวจแค่ตัวแปรที่ตั้งไว้ว่าเป็นบวกแล้วปล่อยผ่าน ทั้งที่ด้านอื่นถูกเขียนอยู่ในรูปของตัวแปรนั้น '
        '⇒ รากที่ทำให้ตัวแปรเป็นบวกอาจทำให้ด้านอื่นติดลบก็ได้ ⇒ ต้องตรวจให้ครบ<b>ทุกด้าน</b>',
        '• เครื่องมือกรองคำตอบอย่างเร็ว : ในสามเหลี่ยมมุมฉาก ด้านที่อยู่ตรงข้ามมุมที่ใหญ่กว่าย่อมยาวกว่า '
        '⇒ ถ้าด้านตรงข้ามมุม $A$ ยาวกว่าด้านประชิดมุม $A$ แล้วมุม $A$ ต้องใหญ่กว่า $45^{\\circ}$ '
        '⇒ $\\tan A > \\tan 45^{\\circ} = 1$ · ข้อสังเกตบรรทัดนี้ใช้ตัดค่าที่น้อยกว่า $1$ ทิ้งได้โดยไม่ต้องคำนวณอะไรเลย',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• รูปสามเหลี่ยม $ABC$ มีมุม $C$ เป็นมุมฉาก ⇒ ด้าน $AB$ คือด้านตรงข้ามมุมฉาก',
        '• ด้าน $AB$ ยาวกว่าด้าน $BC$ อยู่ $2$ หน่วย ⇒ เขียนเป็นสมการได้ว่า $c - a = 2$',
        '• ด้าน $AB$ ยาวกว่าด้าน $CA$ อยู่ $9$ หน่วย ⇒ เขียนเป็นสมการได้ว่า $c - b = 9$',
        '• สังเกตหน้าตาก่อนลงมือ : โจทย์ไม่ได้ให้ความยาวด้านใดมาเป็นตัวเลขสักด้าน ให้มาแต่<b>ผลต่าง</b> '
        '⇒ ต้องสร้างสมการขึ้นมาเองแล้วแก้หาความยาวจริงให้ได้ก่อน จึงจะอ่านอัตราส่วนตรีโกณมิติได้ · '
        'และเพราะผลต่างทั้งสองคู่วัดออกจากด้าน $AB$ เหมือนกัน การยกด้าน $AB$ ขึ้นเป็นตัวแปรหลักจึงประหยัดแรงที่สุด',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\tan A$ ออกมาเป็นจำนวนจริงจำนวนเดียว',
        '',
        '<b>【 ตั้ง $AB = c$ เป็นตัวแปรเดียว แล้วเขียนด้านที่เหลือเป็น $BC = c-2$ กับ $CA = c-9$ '
        'แทนลงพีทาโกรัสจะยุบเหลือ $c^2 - 22c + 85 = 0$ ซึ่งแยกตัวประกอบได้สองราก '
        'จากนั้นคัดรากที่ทำให้ด้าน $CA$ ติดลบทิ้งไป เหลือสามเหลี่ยม $8$-$15$-$17$ '
        'แล้วจึงอ่านค่า $\\tan A$ จากนิยาม 】</b>',
        '',
        '<b>ขั้นที่ 1 · เปลี่ยนผลต่างสองคู่ให้เป็นความยาวด้านที่เขียนด้วยตัวแปรเดียว</b>',
        '• สูตรที่ใช้ : ประโยคที่ว่า “ $X$ ยาวกว่า $Y$ อยู่ $k$ หน่วย ” แปลเป็นสมการได้ว่า $X - Y = k$ '
        'ซึ่งจัดรูปใหม่ได้เป็น $Y = X - k$',
        '• ระบุตัวแปร : ให้ $c = AB$ · $a = BC$ · $b = CA$ ตามที่ตั้งชื่อไว้ในความรู้พื้นฐาน',
        '• แทนค่าเงื่อนไขข้อแรก : $AB - BC = 2$ ⇒ $c - a = 2$ ⇒ $a = c - 2$',
        '• แทนค่าเงื่อนไขข้อที่สอง : $AB - CA = 9$ ⇒ $c - b = 9$ ⇒ $b = c - 9$',
        '• ⭐ ตอนนี้ทั้งสามด้านเขียนด้วยตัวแปรตัวเดียวได้ครบแล้ว : $BC = c-2$ · $CA = c-9$ · $AB = c$ '
        '⇒ ยังเหลือความสัมพันธ์ที่ยังไม่ได้ใช้อีกหนึ่งข้อ คือมุมฉากที่จุด $C$ ซึ่งจะแปลงเป็นพีทาโกรัสในขั้นถัดไป',
        '• 📌 จดเงื่อนไขความเป็นจริงไว้ข้างกระดาษตั้งแต่ตอนนี้ : ความยาวด้านทุกด้านต้องเป็นบวก '
        '⇒ $c > 0$ และ $c - 2 > 0$ และ $c - 9 > 0$ · สามข้อนี้ยุบรวมกันเหลือข้อเดียวคือ $c > 9$ '
        'เพราะข้อที่เข้มที่สุดครอบข้ออื่นไว้หมดแล้ว · บรรทัดนี้จะเป็นตัวตัดสินในขั้นที่ 4',
        '',
        '<b>ขั้นที่ 2 · แทนลงทฤษฎีบทพีทาโกรัสแล้วยุบให้เหลือสมการกำลังสอง</b>',
        '• สูตรที่ใช้ : $a^2 + b^2 = c^2$ โดย $a$ กับ $b$ เป็นด้านประกอบมุมฉาก และ $c$ เป็นด้านตรงข้ามมุมฉาก',
        '• ระบุตัวแปร : มุมฉากอยู่ที่จุด $C$ ⇒ ด้านประกอบมุมฉากคือ $BC = c-2$ กับ $CA = c-9$ '
        '· ด้านตรงข้ามมุมฉากคือ $AB = c$',
        '• แทนค่า : $(c-2)^2 + (c-9)^2 = c^2$',
        '• กระจายทีละวงเล็บ : $(c-2)^2 = c^2 - 4c + 4$ และ $(c-9)^2 = c^2 - 18c + 81$',
        '• รวมสองก้อนเข้าด้วยกัน : $c^2 - 4c + 4 + c^2 - 18c + 81 = c^2$ ⇒ $2c^2 - 22c + 85 = c^2$',
        '• ลบ $c^2$ ออกจากทั้งสองข้าง : $c^2 - 22c + 85 = 0$',
        '• สังเกตว่าพจน์ $c^2$ หายไปเพียงตัวเดียว ⇒ สมการที่ได้ยัง<b>เป็นสมการกำลังสอง</b> ไม่ได้ยุบเป็นสมการเชิงเส้น '
        '⇒ เตรียมใจไว้ได้เลยว่าจะได้รากออกมาสองราก และจะต้องมีขั้นตอนคัดรากตามมาแน่นอน',
        '',
        '<b>ขั้นที่ 3 · แก้สมการกำลังสองด้วยการแยกตัวประกอบ</b>',
        '• สูตรที่ใช้ : ถ้า $c^2 - (p+q)c + pq = 0$ แล้วจะแยกตัวประกอบได้เป็น $(c-p)(c-q) = 0$ '
        '⇒ งานของเราคือหาจำนวนสองจำนวนที่บวกกันได้ $22$ และคูณกันได้ $85$',
        '• ระบุตัวเลข : แยกตัวประกอบ $85 = 5 \\times 17$ และตรวจผลบวก $5 + 17 = 22$ ✓ ⇒ คู่ที่ต้องการคือ $5$ กับ $17$',
        '• แยกตัวประกอบ : $c^2 - 22c + 85 = (c-17)(c-5) = 0$',
        '• ตรวจการแยกตัวประกอบก่อนใช้ต่อ โดยกระจายกลับ : $(c-17)(c-5) = c^2 - 5c - 17c + 85 = c^2 - 22c + 85$ ✓ '
        'ตรงกับสมการเดิมทุกพจน์',
        '• ผลคูณจะเป็นศูนย์ได้ก็ต่อเมื่อตัวประกอบตัวใดตัวหนึ่งเป็นศูนย์ ⇒ $c = 17$ <b>หรือ</b> $c = 5$ '
        '⇒ ได้ผู้เข้าชิงมาสองราย ซึ่ง<b>ยังไม่ใช่</b>คำตอบทั้งคู่จนกว่าจะผ่านการตรวจในขั้นที่ 4',
        '',
        '<b>ขั้นที่ 4 · คัดรากด้วยเงื่อนไขที่ว่าความยาวด้านต้องเป็นบวก</b>',
        '• สูตรที่ใช้ : ความยาวของด้านในรูปเรขาคณิตต้องเป็นจำนวนบวกเสมอ '
        '⇒ รากใดที่ทำให้ด้านใดด้านหนึ่งออกมาเป็นศูนย์หรือติดลบ ต้องทิ้งรากนั้นทันที',
        '• กรณีที่หนึ่ง $c = 5$ : ได้ $BC = c - 2 = 3$ ซึ่งเป็นบวกดูดี แต่พอคิดด้านที่เหลือจะได้ '
        '$CA = c - 9 = 5 - 9 = -4$ ⇒ ⛔ ความยาวด้านติดลบเป็นไปไม่ได้ ⇒ ทิ้งรากนี้',
        '• 🔴 <b>กับดักหลักของข้อนี้อยู่ตรงนี้</b> : รากที่ต้องทิ้งไม่ได้ติดลบด้วยตัวมันเอง เพราะ $c = 5$ '
        'ก็เป็นจำนวนบวก และด้าน $BC = 3$ ก็ยังเป็นบวก ⇒ ถ้าตรวจแค่ตัวแปร $c$ หรือตรวจแค่ด้านเดียวจะผ่านฉลุยและ'
        'หลงเดินต่อด้วยรากนี้ · ตัวที่พังคือด้าน $CA$ ซึ่งผูกกับตัวเลขที่ใหญ่กว่าคือ $9$ '
        '⇒ ตรงกับเงื่อนไข $c > 9$ ที่จดไว้ตั้งแต่ขั้นที่ 1 พอดี และ $5$ ไม่ผ่านเงื่อนไขนั้นอย่างชัดเจน',
        '• กรณีที่สอง $c = 17$ : ได้ $BC = 17 - 2 = 15$ · $CA = 17 - 9 = 8$ · $AB = 17$ '
        '⇒ เป็นบวกครบทั้งสามด้าน และผ่านเงื่อนไข $c > 9$ ⇒ ⭐ เหลือรูปสามเหลี่ยมที่เป็นไปได้เพียงรูปเดียว '
        'คือสามเหลี่ยมที่มีด้าน $8$-$15$-$17$ ⇒ โจทย์ข้อนี้จึงมีคำตอบเดียว ไม่กำกวม',
        '• สรุปความยาวทั้งสามด้านที่จะใช้ต่อ : $BC = 15$ หน่วย · $CA = 8$ หน่วย · $AB = 17$ หน่วย',
        '',
        '<b>ขั้นที่ 5 · อ่านค่า $\\tan A$ จากนิยาม</b>',
        '• สูตรที่ใช้ : $\\tan A$ เท่ากับความยาวด้านตรงข้ามมุม $A$ หารด้วยความยาวด้านประชิดมุม $A$',
        '• ระบุตัวแปรให้ชัดก่อนแทนค่า : มุม $A$ อยู่ที่จุดยอด $A$ · ด้านที่ไม่แตะจุดยอด $A$ เลยคือด้าน $BC$ '
        '⇒ $BC$ เป็นด้านตรงข้ามมุม $A$ · ส่วนด้านประชิดมุม $A$ ที่ไม่ใช่ด้านตรงข้ามมุมฉากคือด้าน $CA$ '
        '⇒ $\\tan A = \\dfrac{BC}{CA}$',
        '• แทนค่าความยาวที่ได้จากขั้นที่ 4 : $\\tan A = \\dfrac{15}{8}$',
        '• ยุบเศษส่วน : ตัวหารร่วมมากของ $15$ กับ $8$ เท่ากับ $1$ ⇒ $\\dfrac{15}{8}$ เป็นเศษส่วนอย่างต่ำอยู่แล้ว '
        '· ตรวจความสมเหตุสมผลอย่างเร็ว : $\\dfrac{15}{8} = 1.875$ ซึ่งมากกว่า $1$ '
        'ตรงกับข้อสังเกตในความรู้พื้นฐานที่ว่าด้านตรงข้ามมุม $A$ ยาวกว่าด้านประชิด ✓',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แทนความยาวสามด้านที่ได้กลับเข้าเงื่อนไขทุกข้อของโจทย์ '
        'แล้วกรองซ้ำด้วยขอบเขตของมุม $45^{\\circ}$)</b>',
        '• เส้นทางข้างบนเดินจากเงื่อนไขไปหาความยาว รอบนี้จะเดินย้อนกลับ คือถือความยาว $15$ , $8$ และ $17$ '
        'เป็นของที่มีอยู่แล้ว แล้วตรวจว่ามันสอดคล้องกับทุกบรรทัดของโจทย์หรือไม่ '
        '⇒ เป็นการตรวจที่ไม่แตะสมการกำลังสองและไม่แตะการแยกตัวประกอบเลยแม้แต่ก้าวเดียว',
        '• เงื่อนไขข้อแรก ด้าน $AB$ ต้องยาวกว่าด้าน $BC$ อยู่ $2$ หน่วย : $17 - 15 = 2$ ✓',
        '• เงื่อนไขข้อที่สอง ด้าน $AB$ ต้องยาวกว่าด้าน $CA$ อยู่ $9$ หน่วย : $17 - 8 = 9$ ✓',
        '• เงื่อนไขข้อที่สาม มุม $C$ ต้องเป็นมุมฉาก : $15^2 + 8^2 = 225 + 64 = 289$ และ $17^2 = 289$ '
        '⇒ เท่ากันพอดี ✓ ⇒ รูปสามเหลี่ยมนี้มีอยู่จริงและมีมุมฉากอยู่ที่จุด $C$ จริง',
        '• 📌 กรองซ้ำด้วยขอบเขต : ด้านตรงข้ามมุม $A$ ยาว $15$ หน่วย ซึ่งยาวกว่าด้านประชิดที่ยาว $8$ หน่วย '
        '⇒ มุม $A$ ต้องใหญ่กว่า $45^{\\circ}$ ⇒ $\\tan A > 1$ '
        '⇒ ค่าที่น้อยกว่า $1$ ตัดทิ้งได้ทันทีโดยไม่ต้องคำนวณ เหลือผู้เข้าชิงเพียง $\\dfrac{15}{8}$ กับ $\\dfrac{9}{2}$',
        '• ตัดผู้เข้าชิงที่เหลือด้วยพีทาโกรัสอีกชั้น : ค่า $\\dfrac{9}{2}$ เกิดจากสามเหลี่ยมที่มีด้าน $9$ , $2$ และ $11$ '
        'ซึ่ง $9^2 + 2^2 = 81 + 4 = 85$ ไม่เท่ากับ $11^2 = 121$ ⇒ สามเหลี่ยมนั้นไม่มีมุมฉาก ⇒ ตกไป '
        '⇒ เหลือ $\\dfrac{15}{8}$ เพียงค่าเดียวที่รอดทุกด่าน ✓',
        '',
        '✅ <b>คำตอบ</b> ค่าของ $\\tan A$ เท่ากับ $\\dfrac{15}{8}$ → <b>ตัวเลือก 3</b>',
        '',
        '💡 <b>เทคนิค</b>',
        '• พอเจอโจทย์ที่ให้มาแต่<b>ผลต่าง</b>ของความยาว ให้มองหาด้านที่ถูกอ้างถึงบ่อยที่สุดแล้วยกด้านนั้นขึ้นเป็นตัวแปรเดียว '
        '· ข้อนี้ด้าน $AB$ ถูกอ้างถึงทั้งสองเงื่อนไข ⇒ ตั้ง $AB = c$ แล้วอีกสองด้านจะตามมาเองในรูป $c-2$ กับ $c-9$ '
        '⇒ เหลือสมการเดียวตัวแปรเดียว ⛔ ถ้าตั้งสามตัวแปรแล้วค่อยไล่แทนกันไปมา จะเสียเวลาและมีโอกาสสลับด้านสูงมาก',
        '• เขียนเงื่อนไข “ทุกด้านต้องเป็นบวก” ลงกระดาษ<b>ก่อน</b>แก้สมการเสมอ ไม่ใช่ไปนึกได้หลังจากได้รากมาแล้ว '
        '· ข้อนี้เงื่อนไขทั้งสามยุบเหลือ $c > 9$ เพียงบรรทัดเดียว ⇒ พอได้ราก $c = 17$ กับ $c = 5$ ก็คัดจบในหนึ่งวินาที '
        'โดยไม่ต้องย้อนกลับไปแทนค่าทีละด้านให้เสี่ยงลืม',
        '• จำสามเหลี่ยมมุมฉากที่ด้านเป็นจำนวนเต็มไว้สักชุด : $3$-$4$-$5$ · $5$-$12$-$13$ · $8$-$15$-$17$ · '
        '$7$-$24$-$25$ · $20$-$21$-$29$ ⇒ พอตัวเลขที่คำนวณได้ตรงกับชุดใดชุดหนึ่ง ก็มั่นใจได้ทันทีว่าเดินมาถูกทาง '
        'และยังใช้เดาย้อนได้ด้วยว่าโจทย์ตั้งใจให้เลขออกมาลงตัว',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\dfrac{8}{15}$ เพราะหาความยาวด้านมาถูกครบทั้งสามด้านแล้ว คือ $15$ , $8$ และ $17$ '
        'แต่ตอนอ่านอัตราส่วนกลับสลับด้านตรงข้ามกับด้านประชิด คือเขียนเป็น $\\dfrac{CA}{BC}$ '
        'แทนที่จะเป็น $\\dfrac{BC}{CA}$ · ค่านี้คือ $\\tan B$ ไม่ใช่ $\\tan A$ และพิสูจน์ว่าผิดได้สองชั้น : '
        'ชั้นแรก $\\dfrac{8}{15} \\approx 0.533$ ซึ่งน้อยกว่า $1$ แต่มุม $A$ อยู่ตรงข้ามด้านที่ยาวกว่า '
        'จึงต้องใหญ่กว่า $45^{\\circ}$ และ $\\tan$ ของมันต้องมากกว่า $1$ · ชั้นที่สอง มุม $A$ กับมุม $B$ '
        'รวมกันได้ $90^{\\circ}$ ⇒ $\\tan A \\cdot \\tan B = 1$ ⇒ ค่าทั้งสองเป็นส่วนกลับของกันและกัน '
        'จึงเป็นคนละค่ากันแน่นอน · วิธีกันคือชี้นิ้วที่จุดยอด $A$ แล้วถามว่าด้านใด<b>ไม่แตะ</b>จุดยอดนั้นเลย '
        'ด้านนั้นคือด้านตรงข้ามมุม $A$ ซึ่งต้องขึ้นเป็นตัวเศษของ $\\tan A$',
        '• ได้ค่า $\\dfrac{3}{4}$ เพราะเก็บราก $c = 5$ เอาไว้ แล้วพอเห็นว่า $CA = 5 - 9 = -4$ ติดลบ '
        'ก็ใส่ค่าสัมบูรณ์ให้กลายเป็น $4$ ด้วยความรู้สึกว่าความยาวคงต้องเป็นบวกอยู่แล้ว '
        '⇒ ได้รูปสามเหลี่ยม $3$-$4$-$5$ ปลอมขึ้นมา ⇒ $\\tan A = \\dfrac{3}{4}$ · '
        'ค่านี้ผิดเพราะการใส่ค่าสัมบูรณ์เป็นการ<b>ดัดคำตอบให้เข้ากับใจ</b> ไม่ใช่การแก้สมการ : '
        'ลองแทนกลับเข้าเงื่อนไขของโจทย์ก็เห็นทันทีว่ารูป $3$-$4$-$5$ นี้มี $AB - CA = 5 - 4 = 1$ '
        'ซึ่งไม่ใช่ $9$ ตามที่โจทย์กำหนด ⇒ ขัดกับเงื่อนไขข้อที่สองเต็ม ๆ · '
        'กรองด้วยขอบเขตได้อีกชั้นว่า $\\dfrac{3}{4} < 1$ ทั้งที่คำตอบของข้อนี้ต้องมากกว่า $1$ · '
        'วิธีกันคือถือกฎเหล็กว่ารากที่ทำให้ด้านใดติดลบต้อง<b>ทิ้ง</b> ⛔ ห้ามดัดให้เป็นบวก',
        '• ได้ค่า $\\dfrac{9}{2}$ เพราะแก้สมการกำลังสองผิดวิธี คือใช้สูตร $c = \\dfrac{-B \\pm \\sqrt{B^2-4AC}}{2A}$ '
        'แล้วตัดพจน์รากที่สองทิ้งไป เหลือแต่ $c = \\dfrac{22}{2} = 11$ ⇒ $BC = 11 - 2 = 9$ และ $CA = 11 - 9 = 2$ '
        '⇒ $\\tan A = \\dfrac{9}{2}$ · ค่านี้ผิดและตรวจจับได้สามชั้น : ชั้นแรก แทน $11$ กลับเข้าสมการเดิมได้ '
        '$11^2 - 22(11) + 85 = 121 - 242 + 85 = -36$ ซึ่งไม่เท่ากับ $0$ ⇒ $11$ ไม่ใช่รากตั้งแต่ต้น · '
        'ชั้นที่สอง รูปที่มีด้าน $9$ , $2$ และ $11$ ไม่ใช่สามเหลี่ยมมุมฉาก เพราะ $9^2 + 2^2 = 85$ '
        'แต่ $11^2 = 121$ · ชั้นที่สาม $9 + 2 = 11$ พอดี ⇒ อสมการสามเหลี่ยมบังคับว่าด้านสองด้านรวมกันต้อง'
        '<b>ยาวกว่า</b>ด้านที่สาม ⇒ รูปนี้แบนราบจนไม่มีพื้นที่ ไม่ใช่รูปสามเหลี่ยม · '
        'วิธีกันคือเขียนสูตรกำลังสองให้ครบทั้งพจน์ ⛔ ห้ามตัดกรณฑ์ทิ้ง และแทนรากกลับเข้าสมการเดิมทุกครั้ง',
        '• อีกเส้นทางที่พลาดกันบ่อยคือหยุดกลางทางแล้วตอบความยาวด้านแทนอัตราส่วน เช่นตอบ $17$ '
        'ซึ่งเป็นเพียงความยาวด้าน $AB$ หรือตอบ $\\dfrac{15}{17}$ ซึ่งเป็นค่าของ $\\sin A$ '
        'เพราะเผลอหารด้วยด้านตรงข้ามมุมฉาก · สองค่านี้ผิดเพราะ $\\tan$ ไม่ได้ใช้ด้านตรงข้ามมุมฉากเลย '
        'มันใช้เฉพาะด้านประกอบมุมฉากสองด้านเท่านั้น และสิ่งที่โจทย์ถามเป็น<b>อัตราส่วน</b> '
        'ซึ่งเป็นความยาวหารความยาว ⇒ ผลลัพธ์ต้องเป็นจำนวนที่ไม่มีหน่วย ไม่ใช่ความยาวหลักสิบ · '
        'วิธีกันคือกลับไปอ่านบรรทัดสุดท้ายของโจทย์อีกครั้งก่อนวงคำตอบเสมอ',
    ],
    'V.mold: G = G-RIGHT-TRI-TWO-DIFFERENCES-FROM-HYP, a right triangle ABC with the right angle at C in '
    'which not one side length is handed over as a number, only two differences and both of them measured '
    'from the same side AB, namely AB - BC = 2 and AB - CA = 9 / A = A-RATIO-VALUE, the value of tan A / '
    'M = M-HYP-DIFFERENCES-QUADRATIC-REJECT-BY-NEGATIVE-LEG, set AB = c as the single unknown so that the '
    'two legs read c - 2 and c - 9, collapse Pythagoras into the one-variable quadratic c**2 - 22*c + 85 = '
    '0, factor it as (c - 17)*(c - 5), reject the root c = 5 because it drives the leg CA = c - 9 to -4 '
    'even though c itself and the other leg stay positive, and read tan A = BC/CA off the surviving '
    '8-15-17 triangle. '
    'Rubric F2 C1 P3 T2 L1 = 9/15, with tot >= 8 and T >= 2 -> level: ยาก. '
    'F = 2 because exactly two formula blocks carry the item, Pythagoras and the right-triangle definition '
    'of tan as opposite over adjacent; F was not raised to 3 because no third theorem is needed anywhere, '
    'no median, no bisector, no identity. C = 1 because the single idea imported from outside subtopic 7.1 '
    'is one-variable quadratic factoring, which is routine algebra rather than a second mathematical key, '
    'so the chain is trigonometry plus one link and not trigonometry plus two. P = 3 for five stages of '
    'different kinds: translate two worded differences into equations, substitute into Pythagoras, expand '
    'two binomials and cancel one c**2, factor and read off two roots, screen the roots and only then '
    'evaluate the ratio. T = 2 for two hidden conditions: the root c = 5 is itself positive and even '
    'leaves BC = c - 2 = 3 positive, so it can only be killed by testing the other leg CA = c - 9, which '
    'is the point of the whole item, and the asked ratio is tan and not its reciprocal, which is exactly '
    'what the first wrong value on offer exploits. T was not raised to 3 because once the positivity test '
    'is applied there is no branch left to choose, no second admissible triangle to compare and no case '
    'split to carry, unlike the q063 and q089 benchmarks. L = 1 because no figure is supplied and the '
    'solver has to draw the triangle first and decide which side faces angle A, but the scene is a single '
    'plane figure with no worded real-world situation to model. The total stops at 9, so the tot >= 12 '
    'gate for ยากมาก is far out of reach; the ยาก gate is met on tot >= 8 together with T >= 2 and is read '
    'before the ปานกลาง gate, so the item lands where it does. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): solving the system c - a = 2, c - b = 9, a**2 + b**2 = c**2 over the reals '
    'returns exactly two solutions, (a, b, c) = (3, -4, 5) and (15, 8, 17); filtering on a > 0 and b > 0 '
    'leaves exactly one of them, which is the machine proof both that the item has a single admissible '
    'triangle and is therefore not ambiguous, and that the discarded root is discarded by a derived leg '
    'turning negative rather than by the unknown itself turning negative. On the surviving branch '
    'Rational(15, 8) is the value of tan A = BC/CA. Every wrong value on offer was machine-computed from a '
    'named error path instead of being invented: Rational(8, 15) is BC and CA swapped, that is tan B, the '
    'reciprocal of the answer because A and B are complementary; 3/4 comes from keeping the rejected root '
    'c = 5 and taking the absolute value of CA = -4, which manufactures a 3-4-5 triangle that fails the '
    'given AB - CA = 9 since 5 - 4 = 1; 9/2 comes from dropping the square-root term of the quadratic '
    'formula so that c = 22/2 = 11, and 11 is not a root at all since 11**2 - 22*11 + 85 = -36, while the '
    'sides 9, 2, 11 satisfy neither Pythagoras (81 + 4 = 85 against 121) nor even the triangle inequality '
    '(9 + 2 = 11 exactly). The independent check was machine-verified as well: 17 - 15 = 2, 17 - 8 = 9 and '
    '15**2 + 8**2 = 289 = 17**2. '
    'Collision sweep on 6457 unique items (bank 63 files + k1 out + k2 out, 6601 raw records with 144 '
    'duplicates dropped): the pair (the comparative phrase for being longer than a side together with the '
    'word for a right angle) inside a question returns 1 item, gen-chap-07-trigonometry-q129, which puts '
    'three points D, E and F on the sides of a right triangle and shares neither A nor M with this item; '
    'the phrase for being longer than a named side returns 3 items, the other two being '
    'chap-13-calculus-q98, a rectangle of largest area inside a semicircle, and pat1-2564-03-q01, which is '
    'the nearest structural relative in the whole corpus, a rectangular floor whose diagonal exceeds the '
    'long side by 2 and whose long side exceeds the short side by 14. That one sits in chapter 3 with '
    'subtopics 3.12 and 3.4, it asks for a labour cost computed from the area instead of a trigonometric '
    'ratio, and its two differences are chained (diagonal to long side, then long side to short side) '
    'rather than both being measured from the hypotenuse, so its quadratic is screened by the unknown '
    'itself coming out negative at w = -6, not by a derived side coming out negative, which is precisely '
    'the turning point of this item; the two molds therefore part company at A and at M and touch only on '
    'the surface of G. The word for a right angle together with tan in a question returns 7 items, the '
    'nearest being gen-chap-07-trigonometry-q015, which supplies one leg and tan A and asks for the other '
    'leg, that is the reverse direction, and gen-chap-07-trigonometry-q065, which hands both legs over as '
    'numbers and asks for a compound ratio; not one of the seven makes the solver build the sides out of '
    'differences first. A narrow scan for the 8-15-17 triple inside a right-triangle question returns 0 '
    'items, so the numeric surface does not echo anything either. Choices are ordered ascending by numeric '
    'value (8/15 = 0.5333, then 3/4 = 0.75, then 15/8 = 1.875, then 9/2 = 4.5), so the answer slot is '
    'forced by that rule and was not chosen.',
)

# -*- coding: utf-8 -*-
add_fill(
    149,
    ['7.1'],
    'ยากมาก',
    'รูปสี่เหลี่ยม $ABCD$ มีมุม $A\\hat{B}C$ และมุม $A\\hat{D}C$ เป็นมุมฉาก '
    'โดยจุด $B$ และจุด $D$ อยู่คนละข้างของเส้นตรง $AC$ กำหนดให้ด้าน $AB$ ยาว $20$ หน่วย '
    'รูปสามเหลี่ยม $ABC$ มีเส้นรอบรูปยาว $60$ หน่วย และรูปสี่เหลี่ยม $ABCD$ มีพื้นที่ $234$ ตารางหน่วย '
    'แล้วค่าของ $\\tan(D\\hat{A}C) + \\tan(D\\hat{C}A)$ เท่ากับเท่าใด',
    '625/168',
    ['625/168', '\\dfrac{625}{168}'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• ในสามเหลี่ยมมุมฉาก ด้านที่อยู่<b>ตรงข้าม</b>มุมฉากเรียกว่าด้านตรงข้ามมุมฉาก และเป็นด้านที่ยาวที่สุดเสมอ '
        '· วิธีอ่านให้ไม่พลาดคือดูว่ามุมฉากอยู่ที่จุดยอดใด แล้วด้านตรงข้ามมุมฉากคือด้านที่เชื่อมอีกสองจุดที่เหลือ '
        'เช่น สามเหลี่ยม $ABC$ ที่มีมุมฉากที่ $B$ จะมีด้านตรงข้ามมุมฉากคือ $AC$ '
        '· ทฤษฎีบทพีทาโกรัสเขียนได้ว่า (ด้านประกอบมุมฉากที่หนึ่ง)$^{2}$ $+$ (ด้านประกอบมุมฉากที่สอง)$^{2}$ '
        '$=$ (ด้านตรงข้ามมุมฉาก)$^{2}$ ⛔ ต้องวางด้านให้ถูกช่องก่อนแทนค่าเสมอ',
        '• อัตราส่วน $\\tan$ ของมุมแหลมในสามเหลี่ยมมุมฉาก นิยามว่า $\\tan(\\text{มุม}) = '
        '\\dfrac{\\text{ความยาวด้านตรงข้ามมุมนั้น}}{\\text{ความยาวด้านประชิดมุมนั้น}}$ '
        '⛔ ตัวส่วนคือด้านประชิดที่<b>ไม่ใช่</b>ด้านตรงข้ามมุมฉาก · วิธีหาด้านตรงข้ามมุมหนึ่ง ๆ '
        'คือชี้นิ้วที่จุดยอดของมุมนั้นแล้วมองข้ามไปยังด้านที่ไม่แตะจุดยอดนั้นเลย',
        '• พื้นที่ของสามเหลี่ยมมุมฉากเท่ากับ $\\dfrac{1}{2}\\times$ ผลคูณของด้านประกอบมุมฉากทั้งสองด้าน '
        'เหตุผลคือด้านสองด้านนี้ตั้งฉากกันอยู่แล้ว จึงหยิบด้านหนึ่งเป็นฐานและอีกด้านเป็นส่วนสูงได้ทันที '
        'โดยไม่ต้องลากเส้นสูงเพิ่ม ⛔ ห้ามเผลอเอาด้านตรงข้ามมุมฉากมาคูณด้วย',
        '• เส้นทแยงมุมของรูปสี่เหลี่ยมแบ่งรูปออกเป็นสามเหลี่ยมสองรูป · ถ้าจุดยอดอีกสองจุดอยู่<b>คนละข้าง</b>'
        'ของเส้นทแยงมุมเส้นนั้น สามเหลี่ยมสองรูปจะไม่ซ้อนทับกันเลย (ซ้อนกันแค่บนเส้นทแยงมุมซึ่งไม่มีพื้นที่) '
        '⇒ พื้นที่ของรูปสี่เหลี่ยมเท่ากับ<b>ผลบวก</b>ของพื้นที่สามเหลี่ยมสองรูปพอดี '
        '⇒ ประโยคเรื่องคนละข้างในโจทย์จึงไม่ใช่คำประดับ แต่เป็นใบอนุญาตให้บวกพื้นที่ตรง ๆ ได้',
        '• เอกลักษณ์ของนิพจน์สมมาตร : สำหรับจำนวนบวก $p$ กับ $q$ ใด ๆ จะได้ '
        '$\\dfrac{p}{q} + \\dfrac{q}{p} = \\dfrac{p^{2} + q^{2}}{pq}$ (ทำส่วนร่วมแล้วบวกเศษ) '
        '⇒ รู้เพียง<b>ผลบวกกำลังสอง</b>กับ<b>ผลคูณ</b>ก็ตอบได้ ไม่ต้องรู้ $p$ กับ $q$ แยกกัน '
        '· และเพราะ $(p - q)^{2} \\ge 0$ ⇒ $p^{2} + q^{2} \\ge 2pq$ ⇒ ค่าของนิพจน์นี้ไม่มีทางน้อยกว่า $2$ '
        '⇒ ใช้เป็นด่านตรวจเร็ว ๆ ได้ว่าคำตอบที่ออกมาน้อยกว่า $2$ ต้องผิดแน่นอน',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• รูปสี่เหลี่ยม $ABCD$ มีมุม $A\\hat{B}C$ และมุม $A\\hat{D}C$ เป็นมุมฉากทั้งคู่ '
        '⇒ มีสามเหลี่ยมมุมฉากสองรูปคือ $ABC$ (มุมฉากที่ $B$) กับ $ACD$ (มุมฉากที่ $D$)',
        '• จุด $B$ กับจุด $D$ อยู่คนละข้างของเส้นตรง $AC$ ⇒ $AC$ เป็นเส้นทแยงมุมของรูปสี่เหลี่ยม '
        'และสามเหลี่ยมสองรูปนั่งอยู่คนละฝั่งของเส้นนี้ ไม่ทับกัน',
        '• ด้าน $AB$ ยาว $20$ หน่วย · รูปสามเหลี่ยม $ABC$ มีเส้นรอบรูปยาว $60$ หน่วย · '
        'รูปสี่เหลี่ยม $ABCD$ มีพื้นที่ $234$ ตารางหน่วย',
        '• สังเกตหน้าตาก่อนลงมือ (หนึ่ง) : โจทย์ไม่ได้บอกความยาวของ $AD$ หรือ $DC$ ไว้เลยสักเส้นเดียว '
        'ทั้งที่คำถามพูดถึงมุมสองมุมในสามเหลี่ยม $ACD$ ⇒ แปลว่าต้องมีทางเดินที่ไปถึงคำตอบได้'
        '<b>โดยไม่ต้องรู้</b>ความยาวสองเส้นนั้นแยกกัน ไม่งั้นข้อมูลย่อมไม่พอ',
        '• สังเกตหน้าตาก่อนลงมือ (สอง) : มุม $D\\hat{A}C$ กับมุม $D\\hat{C}A$ เป็นมุมแหลมสองมุม'
        'ของสามเหลี่ยมมุมฉากรูปเดียวกัน ⇒ รวมกันได้ $90^{\\circ}$ ⇒ ค่า $\\tan$ ของสองมุมนี้เป็นส่วนกลับของกันและกัน '
        '⇒ สิ่งที่โจทย์ถามมีหน้าตาเป็น $t + \\dfrac{1}{t}$ ซึ่งเป็นนิพจน์สมมาตร '
        '⇒ เดาทางล่วงหน้าได้ว่าจะต้องใช้ผลบวกกำลังสองกับผลคูณ',
        '• สังเกตหน้าตาก่อนลงมือ (สาม) : ข้อมูลถูกโยนมาสองก้อนคนละสามเหลี่ยม '
        '(เส้นรอบรูปเป็นของรูปซ้าย ส่วนพื้นที่เป็นของรูปทั้งใบ) ⇒ ต้องมีสะพานสักเส้นที่ส่งข้อมูลข้ามฝั่ง '
        'และสะพานเส้นนั้นย่อมเป็นเส้นเดียวที่รูปทั้งสองใช้ร่วมกัน คือ $AC$',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาค่าของ $\\tan(D\\hat{A}C) + \\tan(D\\hat{C}A)$ ออกมาเป็นจำนวน',
        '',
        '<b>【 วาดภาพเองก่อนแล้วชี้ให้ได้ว่า $AC$ เป็นด้านตรงข้ามมุมฉากของสามเหลี่ยมทั้งสองรูปพร้อมกัน '
        'จากนั้นใช้เส้นรอบรูปคู่กับพีทาโกรัสในรูปซ้ายเพื่อหา $BC$ กับ $AC$ '
        'แล้วหักพื้นที่รูปซ้ายออกจากพื้นที่ทั้งใบเพื่อให้ได้ผลคูณ $AD \\cdot DC$ '
        'สุดท้ายยุบนิพจน์ที่ถามให้เป็น $\\dfrac{AD^{2} + DC^{2}}{AD \\cdot DC}$ ซึ่งตอบได้โดยไม่ต้องหา $AD$ กับ $DC$ แยกกัน 】</b>',
        '',
        '<b>ขั้นที่ 1 · วาดภาพตามคำบรรยายด้วยตัวเอง แล้วอ่านให้ออกว่ามุมฉากทั้งสองมุมชี้ไปที่ด้านเดียวกัน</b>',
        '• ⛔ ข้อนี้ไม่มีภาพมาให้ ต้องวาดเองก่อนเป็นอันดับแรก มิฉะนั้นจะมองไม่เห็นว่าอะไรเชื่อมกับอะไร '
        '· ลำดับการวาดที่ปลอดภัยที่สุดคือเริ่มจากเส้นที่ใช้ร่วมกันก่อน',
        '• ลากส่วนของเส้นตรง $AC$ ในแนวนอนไว้กลางกระดาษ กำกับปลายซ้ายว่า $A$ ปลายขวาว่า $C$ '
        '⇒ เส้นนี้คือเส้นทแยงมุมร่วม และจะเป็นตัวเอกของทั้งข้อ',
        '• วางจุด $B$ ไว้<b>เหนือ</b>เส้น $AC$ แล้วลาก $BA$ กับ $BC$ โดยให้สองเส้นนี้ตั้งฉากกันที่จุด $B$ '
        '⇒ ได้สามเหลี่ยม $ABC$ ที่มีมุมฉากที่ $B$ ตามที่โจทย์กำหนด',
        '• วางจุด $D$ ไว้<b>ใต้</b>เส้น $AC$ ซึ่งเป็นคนละข้างกับจุด $B$ ตามประโยคในโจทย์ '
        'แล้วลาก $DA$ กับ $DC$ โดยให้ตั้งฉากกันที่จุด $D$ ⇒ ได้สามเหลี่ยม $ACD$ ที่มีมุมฉากที่ $D$',
        '• เดินตาม $A \\to B \\to C \\to D \\to A$ จะได้ขอบของรูปสี่เหลี่ยม $ABCD$ ครบทั้งสี่ด้าน '
        'โดยมี $AC$ พาดอยู่ข้างในเป็นเส้นทแยงมุมที่ผ่ารูปออกเป็นสองซีก ซีกบนคือสามเหลี่ยม $ABC$ '
        'ซีกล่างคือสามเหลี่ยม $ACD$',
        '• ⭐ กุญแจดอกที่ 1 ที่ต้องอ่านให้ออกจากภาพนี้ : มุมฉากอยู่ที่ $B$ ⇒ ด้านตรงข้ามมุมฉากของสามเหลี่ยม $ABC$ '
        'คือด้านที่เชื่อม $A$ กับ $C$ นั่นคือ $AC$ · มุมฉากอยู่ที่ $D$ ⇒ ด้านตรงข้ามมุมฉากของสามเหลี่ยม $ACD$ '
        'ก็คือด้านที่เชื่อม $A$ กับ $C$ นั่นคือ $AC$ เส้นเดิมอีกเช่นกัน '
        '⇒ เส้นเดียวทำหน้าที่ด้านตรงข้ามมุมฉากให้สามเหลี่ยมทั้งสองรูปพร้อมกัน '
        '⇒ นี่คือสะพานที่ส่งข้อมูลจากซีกบนไปซีกล่าง และเป็นเหตุผลว่าทำไมโจทย์ถึงกล้าให้ข้อมูลคนละก้อนกับคนละรูป',
        '• ผลพลอยได้จากภาพอีกอย่างที่ต้องบันทึกไว้ใช้ในขั้นที่ 3 : เพราะ $B$ กับ $D$ อยู่คนละข้างของ $AC$ '
        'สามเหลี่ยมสองรูปจึงไม่ซ้อนทับกัน ⇒ พื้นที่รูปสี่เหลี่ยม $ABCD$ $=$ พื้นที่สามเหลี่ยม $ABC$ $+$ '
        'พื้นที่สามเหลี่ยม $ACD$ โดยไม่ต้องบวกลบส่วนที่ซ้อนกันเลย',
        '',
        '<b>ขั้นที่ 2 · ใช้เส้นรอบรูปคู่กับพีทาโกรัสในสามเหลี่ยม $ABC$ เพื่อหา $BC$ กับ $AC$</b>',
        '• สูตรที่ใช้ : เส้นรอบรูปของสามเหลี่ยม $=$ ผลบวกความยาวด้านทั้งสามด้าน '
        '⇒ $AB + BC + CA = 60$ · แทนค่า $AB = 20$ ที่โจทย์ให้ ⇒ $20 + BC + CA = 60$ ⇒ $BC + CA = 40$',
        '• ระบุตัวแปรก่อนแทนค่า : ให้ $BC = x$ หน่วย ⇒ จากบรรทัดบนได้ $CA = 40 - x$ หน่วยทันที '
        '· เหตุผลที่ตั้งตัวแปรตัวเดียวพอ คือความยาวสองเส้นนี้ถูกมัดไว้ด้วยสมการเส้นรอบรูปอยู่แล้ว '
        'รู้เส้นหนึ่งก็ได้อีกเส้นด้วยการลบ ไม่ต้องตั้งสองตัวแล้วแก้ระบบสมการให้ยาว',
        '• สูตรที่ใช้ต่อ : พีทาโกรัสในสามเหลี่ยม $ABC$ · จากขั้นที่ 1 รู้แล้วว่า $AC$ เป็นด้านตรงข้ามมุมฉาก '
        'ส่วน $AB$ กับ $BC$ เป็นด้านประกอบมุมฉาก ⇒ วางสูตรได้ว่า $AB^{2} + BC^{2} = CA^{2}$',
        '• แทนค่า : $20^{2} + x^{2} = (40 - x)^{2}$ ⇒ $400 + x^{2} = (40 - x)^{2}$',
        '• กระจายฝั่งขวาด้วยสูตร $(a - b)^{2} = a^{2} - 2ab + b^{2}$ : $(40 - x)^{2} = 1600 - 80x + x^{2}$ '
        '⇒ สมการกลายเป็น $400 + x^{2} = 1600 - 80x + x^{2}$',
        '• ⭐ จุดที่ต้องสังเกต : พจน์ $x^{2}$ โผล่ทั้งสองข้างเท่ากันพอดี ⇒ ตัดทิ้งได้ทั้งคู่ '
        '⇒ สมการที่ดูเหมือนกำลังสองยุบลงเหลือ<b>สมการเชิงเส้น</b> $400 = 1600 - 80x$ '
        '⇒ ย้ายข้าง $80x = 1600 - 400 = 1200$ ⇒ $x = \\dfrac{1200}{80} = 15$',
        '• ยุบให้เป็นความยาวจริง : $BC = 15$ หน่วย และ $CA = 40 - 15 = 25$ หน่วย',
        '• ตรวจทันทีกันหลงทาง : $20 + 15 + 25 = 60$ ✓ ตรงกับเส้นรอบรูป และ $15^{2} + 20^{2} = 225 + 400 = 625 = 25^{2}$ ✓ '
        'สังเกตว่าได้สามเหลี่ยม $15$-$20$-$25$ ซึ่งก็คือสามเหลี่ยม $3$-$4$-$5$ ขยาย $5$ เท่านั่นเอง',
        '',
        '<b>ขั้นที่ 3 · แยกพื้นที่ออกเป็นสองซีก เพื่อดึงผลคูณ $AD \\cdot DC$ และผลบวก $AD^{2} + DC^{2}$ ออกมา</b>',
        '• พื้นที่ซีกบน : สามเหลี่ยม $ABC$ มีมุมฉากที่ $B$ ⇒ ด้านประกอบมุมฉากคือ $AB$ กับ $BC$ '
        '⇒ พื้นที่ $= \\dfrac{1}{2}(AB)(BC) = \\dfrac{1}{2}(20)(15) = \\dfrac{1}{2}(300) = 150$ ตารางหน่วย '
        '⛔ ห้ามหยิบ $AC = 25$ มาคูณ เพราะ $AC$ เป็นด้านตรงข้ามมุมฉาก ไม่ใช่ด้านประกอบมุมฉาก',
        '• พื้นที่ซีกล่าง : ใช้ใบอนุญาตจากขั้นที่ 1 ที่ว่าพื้นที่สองซีกบวกกันได้ตรง ๆ '
        '⇒ พื้นที่สามเหลี่ยม $ACD$ $= 234 - 150 = 84$ ตารางหน่วย '
        '⭐ นี่คือกุญแจดอกที่ 3 และเป็นจุดที่คนพลาดกันมากที่สุด เพราะเลข $234$ ที่โจทย์ให้เป็นพื้นที่ของ'
        '<b>ทั้งใบ</b> ไม่ใช่ของซีกล่างเพียงซีกเดียว',
        '• เปลี่ยนพื้นที่ให้เป็นผลคูณของด้าน : สามเหลี่ยม $ACD$ มีมุมฉากที่ $D$ '
        '⇒ ด้านประกอบมุมฉากคือ $AD$ กับ $DC$ ⇒ $\\dfrac{1}{2}(AD)(DC) = 84$ '
        '⇒ คูณสองทั้งสมการ ⇒ $AD \\cdot DC = 168$',
        '• เปลี่ยนด้านตรงข้ามมุมฉากให้เป็นผลบวกกำลังสอง : พีทาโกรัสในสามเหลี่ยม $ACD$ '
        '⇒ $AD^{2} + DC^{2} = AC^{2}$ · แทนค่า $AC = 25$ ที่ได้จากขั้นที่ 2 '
        '⇒ $AD^{2} + DC^{2} = 25^{2} = 625$',
        '• ⭐ สรุปสถานะตรงนี้ให้ชัด : ตอนนี้เรารู้ทั้ง<b>ผลคูณ</b> $AD \\cdot DC = 168$ และ'
        '<b>ผลบวกกำลังสอง</b> $AD^{2} + DC^{2} = 625$ ทั้งที่ยังไม่รู้ค่าของ $AD$ หรือ $DC$ แยกกันเลยสักตัว '
        '⇒ ถ้านิพจน์ที่ถามต้องการแค่สองก้อนนี้ ก็จบได้โดยไม่ต้องแก้หาความยาวเลย',
        '',
        '<b>ขั้นที่ 4 · เขียนนิพจน์ที่ถามด้วย $AD$ กับ $DC$ แล้วยุบด้วยความสมมาตร ⛔ จุดหักของข้อนี้</b>',
        '• เขียน $\\tan(D\\hat{A}C)$ : มุมนี้อยู่ที่จุดยอด $A$ ในสามเหลี่ยม $ACD$ '
        '⇒ ด้านตรงข้ามมุมนี้คือ $DC$ (ด้านที่ไม่แตะจุด $A$) และด้านประชิดที่ไม่ใช่ด้านตรงข้ามมุมฉากคือ $AD$ '
        '⇒ $\\tan(D\\hat{A}C) = \\dfrac{DC}{AD}$',
        '• เขียน $\\tan(D\\hat{C}A)$ : มุมนี้อยู่ที่จุดยอด $C$ ในสามเหลี่ยมเดียวกัน '
        '⇒ ด้านตรงข้ามคือ $AD$ และด้านประชิดคือ $DC$ ⇒ $\\tan(D\\hat{C}A) = \\dfrac{AD}{DC}$ '
        '· สังเกตว่าเป็นส่วนกลับของบรรทัดบนพอดี ซึ่งตรงกับที่ทำนายไว้ตอนอ่านโจทย์ '
        'เพราะมุมสองมุมนี้รวมกันได้ $90^{\\circ}$',
        '• ผลบวกที่โจทย์ถาม $= \\dfrac{DC}{AD} + \\dfrac{AD}{DC}$ '
        '⇒ ทำตัวส่วนร่วมเป็น $AD \\cdot DC$ ⇒ $= \\dfrac{DC \\cdot DC}{AD \\cdot DC} + '
        '\\dfrac{AD \\cdot AD}{AD \\cdot DC} = \\dfrac{DC^{2} + AD^{2}}{AD \\cdot DC}$',
        '• ⭐ กุญแจดอกที่ 4 : รูปที่ยุบได้นี้ต้องการเพียงผลบวกกำลังสองกับผลคูณ ซึ่งขั้นที่ 3 หามาไว้ครบแล้วทั้งคู่ '
        '⇒ แทนค่าได้ทันที $\\dfrac{AD^{2} + DC^{2}}{AD \\cdot DC} = \\dfrac{625}{168}$',
        '• ตรวจว่าเศษส่วนนี้ยุบต่อไม่ได้ : $168 = 2^{3} \\times 3 \\times 7$ ส่วน $625 = 5^{4}$ '
        '⇒ ไม่มีตัวประกอบร่วมนอกจาก $1$ ⇒ $\\dfrac{625}{168}$ เป็นรูปอย่างต่ำแล้ว มีค่าประมาณ $3.72$',
        '• 📌 ประเด็นที่ต้องเข้าใจให้ทะลุ : ถ้าลองแก้หา $AD$ กับ $DC$ จริง ๆ จะได้สองสาขาคือ '
        '$(AD , DC) = (7 , 24)$ หรือ $(AD , DC) = (24 , 7)$ (ขั้นตรวจคำตอบข้างล่างจะแก้ให้ดู) '
        'ซึ่งโจทย์ไม่ได้บอกว่าสาขาไหนถูก ⇒ ถ้าโจทย์ถาม $\\tan$ เพียงมุมเดียวจะกำกวมทันที '
        'แต่เพราะโจทย์ถาม<b>ผลบวก</b>ซึ่งเป็นนิพจน์สมมาตร การสลับ $AD$ กับ $DC$ ไม่ทำให้ค่าเปลี่ยนเลย '
        '⇒ ทั้งสองสาขาให้ $\\dfrac{625}{168}$ เท่ากัน ⇒ โจทย์จึงมีคำตอบเดียวและไม่กำกวม',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · แก้หา $AD$ กับ $DC$ ออกมาเป็นตัวเลขจริงด้วยสมการกำลังสอง '
        'แล้วแทนลงนิพจน์เดิมตรง ๆ โดยไม่ใช้การยุบแบบสมมาตรเลย)</b>',
        '• เริ่มจากของสองก้อนในขั้นที่ 3 : $AD \\cdot DC = 168$ และ $AD^{2} + DC^{2} = 625$',
        '• หาผลบวกของสองความยาว : $(AD + DC)^{2} = AD^{2} + 2(AD)(DC) + DC^{2} = 625 + 2(168) = 625 + 336 = 961$ '
        '⇒ $AD + DC = \\sqrt{961} = 31$ (เลือกรากบวก เพราะเป็นผลบวกของความยาว)',
        '• สองจำนวนที่บวกกันได้ $31$ และคูณกันได้ $168$ คือรากของสมการ $t^{2} - 31t + 168 = 0$ '
        '⇒ หาสองจำนวนที่คูณกันได้ $168$ และบวกกันได้ $31$ ⇒ ได้ $7$ กับ $24$ ⇒ $(t - 7)(t - 24) = 0$ '
        '⇒ $t = 7$ หรือ $t = 24$ ⇒ ความยาวสองเส้นคือ $7$ กับ $24$ หน่วย',
        '• ตรวจว่าคู่นี้เข้ากับข้อมูลของโจทย์จริง : $7^{2} + 24^{2} = 49 + 576 = 625 = 25^{2}$ ✓ '
        '(พีทาโกรัสในสามเหลี่ยม $ACD$ ผ่าน) และ $\\dfrac{1}{2}(7)(24) = 84$ ✓ '
        '⇒ พื้นที่รวม $150 + 84 = 234$ ตารางหน่วย ✓ ตรงกับที่โจทย์ให้พอดี',
        '• แทนลงนิพจน์เดิมแบบไม่ยุบ : ถ้า $AD = 7$ และ $DC = 24$ จะได้ '
        '$\\tan(D\\hat{A}C) + \\tan(D\\hat{C}A) = \\dfrac{24}{7} + \\dfrac{7}{24} = \\dfrac{576 + 49}{168} '
        '= \\dfrac{625}{168}$ ✓ ตรงกับคำตอบที่ได้จากทางเดินหลัก',
        '• สลับสาขาเพื่อยืนยันความไม่กำกวม : ถ้า $AD = 24$ และ $DC = 7$ จะได้ '
        '$\\dfrac{7}{24} + \\dfrac{24}{7} = \\dfrac{625}{168}$ เท่าเดิมเป๊ะ '
        '⇒ ยืนยันด้วยตัวเลขจริงว่าคำตอบไม่ขึ้นกับว่าเลือกสาขาไหน',
        '• ด่านตรวจใหญ่-เล็กปิดท้าย : ค่าที่ได้ $\\dfrac{625}{168} \\approx 3.72$ ซึ่งไม่น้อยกว่า $2$ '
        '⇒ ผ่านกฎ $t + \\dfrac{1}{t} \\ge 2$ ที่เขียนไว้ในบล็อกความรู้พื้นฐาน ✓',
        '',
        '✅ <b>คำตอบ</b> ค่าของ $\\tan(D\\hat{A}C) + \\tan(D\\hat{C}A)$ เท่ากับ '
        '$\\dfrac{AD^{2} + DC^{2}}{AD \\cdot DC} = \\dfrac{625}{168}$',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอนิพจน์หน้าตาสมมาตรอย่าง $\\dfrac{p}{q} + \\dfrac{q}{p}$ ให้รีบเขียนเป็น '
        '$\\dfrac{p^{2} + q^{2}}{pq}$ ทันที<b>ก่อน</b>ลงมือหาค่า $p$ กับ $q$ '
        'เพราะโจทย์แนวนี้มักจงใจให้ข้อมูลมาในรูปผลคูณ (จากพื้นที่) และผลบวกกำลังสอง (จากพีทาโกรัส) '
        'ซึ่งเป็นของสองก้อนที่หาได้ง่ายกว่าความยาวแต่ละเส้นมาก',
        '• มุมแหลมสองมุมของสามเหลี่ยมมุมฉากรวมกันได้ $90^{\\circ}$ เสมอ ⇒ ค่า $\\tan$ ของสองมุมนั้นเป็นส่วนกลับกัน '
        '⇒ ผลบวกของมันคือ $t + \\dfrac{1}{t}$ ซึ่งมีค่าไม่น้อยกว่า $2$ เสมอ และเท่ากับ $2$ พอดีเมื่อสามเหลี่ยมหน้าจั่ว '
        '⇒ ใช้เป็นด่านตรวจคำตอบได้ทันทีโดยไม่ต้องคำนวณอะไรใหม่',
        '• ภาพรวมที่ช่วยให้จำโครงข้อนี้ได้ : เพราะมุม $A\\hat{B}C$ และมุม $A\\hat{D}C$ เป็นมุมฉากทั้งคู่ '
        'จุด $B$ กับจุด $D$ จึงอยู่บนวงกลมที่มี $AC$ เป็นเส้นผ่านศูนย์กลาง (มุมในครึ่งวงกลมเป็นมุมฉาก) '
        '⇒ $ABCD$ เป็นรูปสี่เหลี่ยมแนบในวงกลมรัศมี $\\dfrac{25}{2}$ หน่วย '
        '⇒ เห็นชัดว่าทำไม $AC$ ถึงเป็นตัวเชื่อมเดียวของทั้งข้อ · เจอโจทย์ที่มีมุมฉากสองมุมมองด้านเดียวกันเมื่อไร '
        'ให้นึกถึงวงกลมวงนี้ไว้ก่อนเสมอ',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $\\dfrac{625}{468}$ เพราะเอา $234$ ไปใช้เป็นพื้นที่ของสามเหลี่ยม $ACD$ ทั้งก้อน '
        'ลืมหักพื้นที่สามเหลี่ยม $ABC$ ซึ่งเท่ากับ $150$ ออกก่อน ⇒ ได้ $AD \\cdot DC = 2(234) = 468$ '
        '⇒ ตอบ $\\dfrac{625}{468}$ · ค่านี้ผิดแน่นอน พิสูจน์ได้สองทาง : ทางแรก '
        'ถ้าพื้นที่สามเหลี่ยม $ACD$ เท่ากับ $234$ จริง พื้นที่ทั้งใบจะเป็น $150 + 234 = 384$ ตารางหน่วย '
        'ไม่ใช่ $234$ ที่โจทย์ให้ · ทางที่สอง $\\dfrac{625}{468} \\approx 1.34$ ซึ่ง<b>น้อยกว่า</b> $2$ '
        'ขัดกับกฎ $t + \\dfrac{1}{t} \\ge 2$ ⇒ ไม่มีสามเหลี่ยมมุมฉากรูปใดในโลกให้ค่านี้ได้ '
        '(เทียบตรง ๆ ก็ได้ว่า $AD^{2} + DC^{2} = 625$ แต่ $2(AD)(DC) = 936$ ซึ่งมากกว่า ขัดกับ $(AD - DC)^{2} \\ge 0$)',
        '• ได้ค่า $\\dfrac{625}{84}$ เพราะหาพื้นที่สามเหลี่ยม $ACD$ ได้ $84$ ถูกต้องแล้ว '
        'แต่เอา $84$ ไปใช้เป็น $AD \\cdot DC$ ทันที ลืมคูณสองเพื่อล้าง $\\dfrac{1}{2}$ ในสูตรพื้นที่ '
        '⇒ ตอบ $\\dfrac{625}{84} \\approx 7.44$ · ค่านี้ผิดแน่นอน ตรวจได้โดยเดินย้อน : '
        'ถ้า $AD \\cdot DC = 84$ จริง พื้นที่สามเหลี่ยม $ACD$ จะเท่ากับ $\\dfrac{1}{2}(84) = 42$ ตารางหน่วย '
        '⇒ พื้นที่ทั้งใบ $= 150 + 42 = 192$ ตารางหน่วย ไม่ใช่ $234$ ⇒ ขัดกับโจทย์ · '
        'วิธีกันพลาดคือเขียนสมการเต็มรูป $\\dfrac{1}{2}(AD)(DC) = 84$ ลงกระดาษก่อน แล้วค่อยคูณสองอย่างเป็นขั้นตอน '
        'อย่ากระโดดจากพื้นที่ไปเป็นผลคูณของด้านในหัว',
        '• ได้ค่า $\\dfrac{24}{7} \\approx 3.43$ หรือ $\\dfrac{7}{24} \\approx 0.29$ เพราะแก้จนได้ '
        '$AD$ กับ $DC$ เป็น $7$ กับ $24$ สำเร็จแล้ว แต่ตอบค่า $\\tan$ ของมุมเพียงมุมเดียว '
        'ทั้งที่โจทย์ถาม<b>ผลบวก</b>ของ $\\tan$ สองมุม ⇒ ตอบไม่ครบ · '
        'พิสูจน์ว่าผิดได้ทันทีจากโครงของโจทย์เอง : โจทย์ไม่ได้ระบุว่า $AD$ หรือ $DC$ เส้นไหนยาว $7$ '
        '⇒ ถ้าคำตอบที่ต้องการเป็น $\\tan$ มุมเดียว ค่าจะเป็นได้ทั้ง $\\dfrac{24}{7}$ และ $\\dfrac{7}{24}$ '
        'ซึ่งแปลว่าโจทย์ไม่มีคำตอบเดียว ⇒ เป็นไปไม่ได้สำหรับข้อที่ต้องเติมคำตอบ '
        '· อีกทั้ง $\\dfrac{7}{24} \\approx 0.29$ ยังน้อยกว่า $2$ ซึ่งขัดกับกฎของผลบวกด้วย '
        '⇒ วิธีกันพลาดคือขีดเส้นใต้เครื่องหมายบวกในโจทย์ตั้งแต่อ่านรอบแรก',
        '• ได้ค่า $\\dfrac{50}{21} \\approx 2.38$ เพราะอ่านตำแหน่งมุมฉากผิด ไปเข้าใจว่าด้าน $AB$ ที่ยาว $20$ '
        'คือด้านตรงข้ามมุมฉากของสามเหลี่ยม $ABC$ จึงเอาเลข $20$ ไปสวมเป็น $AC$ '
        '⇒ ใช้ $AC^{2} = 400$ แทน $625$ ในขั้นสุดท้าย ⇒ ได้ $\\dfrac{400}{168} = \\dfrac{50}{21}$ · '
        'ค่านี้ผิดแน่นอน พิสูจน์ได้สองทาง : ทางแรก มุมฉากอยู่ที่ $B$ ⇒ ด้านตรงข้ามมุมฉากคือ $AC$ '
        'ซึ่งต้องยาวกว่าด้านประกอบมุมฉากทุกด้าน ⇒ $AC > AB = 20$ เสมอ ⇒ $AC = 20$ เป็นไปไม่ได้ตั้งแต่ต้น · '
        'ทางที่สอง ถ้าฝืนให้ $AC = 20$ แล้ว เส้นรอบรูปจะบังคับให้ $BC = 60 - 20 - 20 = 20$ '
        '⇒ ตรวจพีทาโกรัสได้ $20^{2} + 20^{2} = 800$ ซึ่งไม่เท่ากับ $20^{2} = 400$ ⇒ สามเหลี่ยมแบบนั้นไม่มีอยู่จริง '
        '⇒ ค่าที่ถูกต้องคือ $AC = 25$ ตามที่ขั้นที่ 2 คำนวณไว้',
    ],
    'V.mold: G = a quadrilateral ABCD whose angle at B and angle at D are both right angles, with the two '
    'vertices B and D stated to lie on opposite sides of the line AC, together with one leg AB = 20, the '
    'perimeter of triangle ABC handed over as 60 and the area of the whole quadrilateral handed over as 234 '
    '/ A = the numerical value of the symmetric expression tan(DAC) + tan(DCA), asked as a free numeric '
    'response with no candidate values on the page / M = M-SHARED-HYPOTENUSE-SPLIT-AREA-SYMMETRIC-TAN, that '
    'is: read both right angles as naming one and the same segment AC as the hypotenuse of both triangles, '
    'set BC = x so that CA = 40 - x from the perimeter, feed that into Pythagoras so the squared terms '
    'cancel and the apparent quadratic collapses to the linear equation 80x = 1200 giving BC = 15 and '
    'AC = 25, subtract the area of ABC from the area of the quadrilateral to get the area of ACD and hence '
    'the product AD*DC = 168, take AD^2 + DC^2 = AC^2 = 625 from Pythagoras in the second triangle, and '
    'finally collapse DC/AD + AD/DC into (AD^2 + DC^2)/(AD*DC) so that neither AD nor DC is ever needed on '
    'its own. '
    'Rubric F3 C3 P3 T3 L1 = 13/15, which clears the threshold of 12 with T = 3, so the very-hard band is '
    'reached -> level: ยากมาก. F = 3 because four separate pieces of knowledge must be held at once and none '
    'of them can be dropped: the rule that locates the hypotenuse from the position of the right angle, '
    'Pythagoras used twice in two different triangles, the area of a right triangle as half the product of '
    'its two legs, and the algebraic collapse p/q + q/p = (p^2 + q^2)/(pq); the tangent ratio itself has to '
    'be read off correctly in a triangle whose vertices are named in an unfamiliar order, which is a fifth '
    'demand on the same page. C = 3 because the item welds four independent conditions into one chain and '
    'every link consumes the output of the previous one: the perimeter produces the sides, the sides produce '
    'the area of the first triangle, that area subtracted from the quadrilateral area produces the product '
    'of the two unknown legs, and the diagonal produced in the first triangle is what turns Pythagoras in '
    'the second triangle into a usable number; removing any single link leaves the item unsolvable. P = 3 '
    'because the written work runs through four stages of genuinely different kinds, a construction stage, '
    'an equation stage, an area-bookkeeping stage and an algebraic collapse, and the third stage consumes '
    'objects built by both of the first two. T = 3 because two independent hidden turning points must both '
    'be found before any answer appears: first that the two right angles at B and at D are not two separate '
    'facts but one fact about the single segment AC, which is the only bridge between the two halves of the '
    'figure, and second that the requested expression is symmetric in AD and DC so that the pair may be left '
    'unresolved forever, which is what rescues the item from the two-branch ambiguity that would sink it if '
    'a single tangent had been asked; on top of these the area of the quadrilateral must be recognised as a '
    'total rather than as the area of the second triangle. L = 1 because the statement carries no real-world '
    'scene and no figure, yet the reader must still build the picture from words, placing B above AC and D '
    'below it, before any of the geometry can be read off; L is not 2 because the whole configuration stays '
    'in one plane. '
    'Scoring was written before the level was read off. '
    'sympy (verify_b21.py): in the q149 block, solve([20 + BC + CA - 60, CA**2 - BC**2 - 400], [BC, CA]) '
    'with both symbols positive returns BC = 15 and CA = 25, the area of ABC evaluates to Rational(1,2)*20*15 '
    '= 150, the product 2*(234 - 150) evaluates to 168, and CA**2/prod evaluates to exactly Rational(625,168), '
    'which is the stored answer and is confirmed rational by the rat check. The absence of ambiguity was '
    'machine-checked separately rather than argued: solve([AD*DC - 168, AD**2 + DC**2 - 625], [AD, DC]) with '
    'both symbols positive returns exactly the two branches (7, 24) and (24, 7), and the set of simplified '
    'values of DC/AD + AD/DC taken over both branches has size 1, so the two branches provably give the same '
    'number and the free-response answer is unique. The independent check block was recomputed the same way: '
    '(AD + DC)^2 = 625 + 2*168 = 961 gives AD + DC = 31, the roots of t^2 - 31t + 168 are exactly 7 and 24, '
    '7^2 + 24^2 = 625 and 7*24/2 = 84 so that 150 + 84 = 234, and 24/7 + 7/24 = 625/168. Every error path in '
    'the pitfalls block was computed by machine rather than invented: using 234 as the area of ACD gives '
    'AD*DC = 468 and the value 625/468, about 1.3355, which is below the bound t + 1/t >= 2 and is refuted '
    'again by 2*468 = 936 > 625; using the area 84 directly as the product gives 625/84, about 7.4405, whose '
    'implied area of ACD is 42 and whose implied total area is 192 rather than 234; answering a single '
    'tangent gives 24/7, about 3.4286, or 7/24, about 0.2917; and mistaking AB for the hypotenuse and using '
    'AC^2 = 400 gives 400/168 = 50/21, about 2.3810, which is refuted by 20^2 + 20^2 = 800 not equal to 400. '
    'Collision sweep on 6457 de-duplicated items (86 files: the bank sets directory plus k1 out plus k2 out), '
    'probe executed directly in this session because no collide_b21.py exists in the tree yet: the Thai '
    'phrase for "on opposite sides" returns 0 items in the whole corpus, a question text holding a sum of '
    'the form tan(...) + tan(...) returns 0 items, and the pair (tangent and area in the same question text) '
    'also returns 0 items, so the surface of this item is untouched. The pair (quadrilateral and right '
    'angle) returns 11 items, of which the nearest is chap-07-trigonometry-q123, a quadrilateral with one '
    'right angle whose area is the thing being asked for and whose mechanism is the law of cosines in '
    'subtopics 7.9 and 7.10, that is the reverse direction of this item and a different M. The pair '
    '(perimeter and right angle) returns 3 items, all of them generated siblings: q106 scales a leg ratio to '
    'a perimeter, q127 puts the three sides in arithmetic progression, and q129 inscribes a square, so none '
    'of them hands over one leg and a perimeter and asks for the diagonal. The closest relative by mechanism '
    'is gen-chap-07-trigonometry-q128, which hands over an area and asks for the symmetric expression '
    'sec A + csc A in a single right triangle, and it is logged here as a deliberate WATCH: it shares the '
    'idea that a symmetric combination can be evaluated without resolving the individual sides, but it lives '
    'in one triangle with the median to the hypotenuse as its key, whereas this item needs two triangles '
    'glued along a shared hypotenuse, an area split and a perimeter equation, so G and M both differ. Since '
    'this is a fill item there is no choice list, so no answer slot exists and nothing about the answer '
    'could have been positioned by hand.',
)

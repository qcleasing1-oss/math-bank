# -*- coding: utf-8 -*-
add_fill(
    151,
    ['7.11'],
    'ปานกลาง',
    'เซกเตอร์ของวงกลมรูปหนึ่งมีรัศมียาว $6$ หน่วย ถ้าเพิ่มความยาวรัศมีของเซกเตอร์รูปนี้เป็น $9$ หน่วย '
    'โดยขนาดของมุมที่จุดศูนย์กลางยังคงเท่าเดิม ปรากฏว่าส่วนโค้งของเซกเตอร์ยาวเพิ่มขึ้นจากเดิม $4$ หน่วย '
    'แล้วพื้นที่ของเซกเตอร์รูปนี้เพิ่มขึ้นจากเดิมกี่ตารางหน่วย',
    '30',
    ['30', '30.0'],
    [
        '📚 <b>ความรู้พื้นฐานที่ต้องใช้</b>',
        '• เซกเตอร์ของวงกลม คือบริเวณที่ถูกล้อมด้วยรัศมีสองเส้นกับส่วนโค้งที่อยู่ระหว่างปลายของรัศมีทั้งสองเส้นนั้น '
        'สิ่งที่บอกรูปร่างของเซกเตอร์ได้ครบมีเพียงสองอย่างคือ <b>ความยาวรัศมี</b> กับ '
        '<b>ขนาดของมุมที่จุดศูนย์กลาง</b> ซึ่งเขียนแทนด้วย $\\theta$ '
        '⇒ ถ้ารู้สองอย่างนี้ ทั้งความยาวส่วนโค้งและพื้นที่จะถูกกำหนดตายตัวทันที',
        '• ความยาวส่วนโค้ง $s = r\\theta$ · ที่มาของสูตรคิดด้วยสัดส่วนล้วน ๆ คือ ส่วนโค้งที่กางมุม $\\theta$ '
        'กินสัดส่วน $\\dfrac{\\theta}{2\\pi}$ ของวงเต็ม เมื่อคูณสัดส่วนนี้เข้ากับเส้นรอบวงซึ่งยาว $2\\pi r$ '
        'จะได้ $s = \\dfrac{\\theta}{2\\pi} \\times 2\\pi r = r\\theta$ '
        '⛔ ใช้ได้ก็ต่อเมื่อ $\\theta$ มีหน่วยเป็น<b>เรเดียน</b>เท่านั้น',
        '• พื้นที่เซกเตอร์ $A = \\dfrac{1}{2}r^{2}\\theta$ · ที่มาคิดด้วยสัดส่วนแบบเดียวกันเป๊ะ ๆ คือ '
        'เซกเตอร์กินสัดส่วน $\\dfrac{\\theta}{2\\pi}$ ของวงกลมทั้งวงซึ่งมีพื้นที่ $\\pi r^{2}$ '
        'จะได้ $A = \\dfrac{\\theta}{2\\pi} \\times \\pi r^{2} = \\dfrac{1}{2}r^{2}\\theta$ '
        '⭐ จุดที่ต้องจำให้แม่นคือสูตรนี้ผูกกับ $r^{2}$ ไม่ใช่ $r$ ⇒ รัศมีมีอิทธิพลต่อพื้นที่แรงกว่าที่มีต่อส่วนโค้ง',
        '• ผลต่างของกำลังสอง : $a^{2} - b^{2} = (a-b)(a+b)$ ⛔ ซึ่ง<b>ไม่เท่ากับ</b> $(a-b)^{2}$ '
        'ลองแทนด้วยเลขจริงคู่ที่จะได้ใช้ในข้อนี้ก็เห็นทันที คือ $9^{2} - 6^{2} = 81 - 36 = 45$ '
        'ส่วน $(9-6)^{2} = 3^{2} = 9$ ⇒ ห่างกันถึงห้าเท่า จึงสลับกันไม่ได้เด็ดขาด',
        '• เทคนิคอ่านโจทย์ที่ของบางอย่างเปลี่ยนและบางอย่างคงเดิม : สิ่งใดที่โจทย์บอกว่า “เท่าเดิม” '
        'ให้เขียนแทนด้วย<b>สัญลักษณ์ตัวเดียวกัน</b>ทั้งก่อนและหลัง ⛔ ห้ามตั้งตัวแปรใหม่ให้มัน '
        'เพราะการใช้ตัวเดียวกันนี่เองที่ทำให้ข้อมูลของสองสถานการณ์เชื่อมถึงกันและแก้ได้',
        '',
        '📐 <b>โจทย์กำหนด</b>',
        '• เซกเตอร์รูปเดิมมีรัศมียาว $6$ หน่วย · หลังจากเพิ่มรัศมีแล้ว เซกเตอร์รูปใหม่มีรัศมียาว $9$ หน่วย',
        '• ขนาดของมุมที่จุดศูนย์กลาง<b>ยังคงเท่าเดิม</b> ⇒ ให้มุมนี้เป็น $\\theta$ เรเดียน '
        'แล้วใช้ $\\theta$ ตัวเดียวกันนี้ทั้งกับรูปเดิมและรูปใหม่ ⛔ โจทย์ไม่ได้บอกค่าของ $\\theta$ มาให้',
        '• ส่วนโค้งของเซกเตอร์ยาวเพิ่มขึ้นจากเดิม $4$ หน่วย ⇒ เลข $4$ นี้คือ<b>ผลต่าง</b>ของความยาวส่วนโค้งสองเส้น '
        '⛔ ไม่ใช่ความยาวของส่วนโค้งเส้นใดเส้นหนึ่ง',
        '• สังเกตหน้าตาก่อนลงมือ : ทั้งสูตรส่วนโค้งและสูตรพื้นที่ต่างก็มี $\\theta$ เป็นตัวประกอบอยู่ด้วยกันทั้งคู่ '
        'และ $\\theta$ เป็นของชิ้นเดียวที่ยังไม่รู้ค่า ⇒ เดาแผนได้ทันทีว่าต้องรีดค่า $\\theta$ ออกมาจากข้อมูลส่วนโค้งก่อน '
        'แล้วจึงเอาไปป้อนสูตรพื้นที่',
        '• สังเกตอีกอย่าง : ตัวเลขที่โจทย์ให้มาไม่มี $\\pi$ ติดอยู่เลยสักตัว และสูตรที่จะใช้ก็ไม่มี $\\pi$ '
        '⇒ คำตอบควรออกมาเป็นจำนวนสวย ๆ ที่ไม่มี $\\pi$ ติด ถ้าคำนวณแล้วมี $\\pi$ โผล่มาแปลว่าเดินผิดทางแน่นอน',
        '',
        '🎯 <b>เป้าหมาย</b>',
        '• หาว่าพื้นที่ของเซกเตอร์รูปใหม่มากกว่าพื้นที่ของเซกเตอร์รูปเดิมอยู่เท่าใด '
        'คือหาค่าของ (พื้นที่รูปใหม่) $-$ (พื้นที่รูปเดิม) โดยตอบเป็นจำนวนที่มีหน่วยเป็นตารางหน่วย',
        '',
        '<b>【 ตรึงมุมที่จุดศูนย์กลางไว้เป็น $\\theta$ ตัวเดียวทั้งก่อนและหลัง '
        '⇒ ส่วนโค้งที่เพิ่มขึ้นคือ $9\\theta - 6\\theta$ ซึ่งเท่ากับ $4$ จึงรีดค่า $\\theta$ ออกมาได้ '
        '⇒ แล้วเอา $\\theta$ ไปเข้าสูตรพื้นที่ในรูปผลต่าง $\\dfrac{1}{2}\\theta\\left(9^{2} - 6^{2}\\right)$ 】</b>',
        '',
        '<b>ขั้นที่ 1 · แปลถ้อยคำว่า “มุมยังคงเท่าเดิม” ให้กลายเป็นสัญลักษณ์</b>',
        '• สูตรที่ใช้ : $s = r\\theta$ เมื่อ $\\theta$ เป็นเรเดียน',
        '• ระบุตัวแปรก่อนแทนค่า : รัศมีเดิม $r_{1} = 6$ · รัศมีใหม่ $r_{2} = 9$ · '
        'ส่วนมุมที่จุดศูนย์กลางเป็น $\\theta$ <b>ตัวเดียวกัน</b>ทั้งสองครั้ง เพราะโจทย์บอกไว้ชัดว่ามุมยังคงเท่าเดิม '
        '⛔ ถ้าเผลอตั้งเป็นมุมสองตัวคือ $\\theta_{1}$ กับ $\\theta_{2}$ จะได้สมการหนึ่งสมการที่มีตัวไม่รู้ค่าสองตัว '
        'ซึ่งแก้ไม่ได้ทันที ⇒ ข้อมูลชิ้นที่มีค่าที่สุดของโจทย์ข้อนี้คือถ้อยคำว่า “เท่าเดิม” นั่นเอง',
        '• แทนค่า : ส่วนโค้งเดิมยาว $s_{1} = 6\\theta$ หน่วย · ส่วนโค้งใหม่ยาว $s_{2} = 9\\theta$ หน่วย',
        '• ยุบ : ยังยุบเป็นตัวเลขไม่ได้ในขั้นนี้ เพราะยังไม่รู้ค่า $\\theta$ '
        '⇒ เก็บทั้งสองไว้เป็นนิพจน์ที่มี $\\theta$ ติดอยู่ก่อน แล้วไปหาค่า $\\theta$ ในขั้นถัดไป',
        '',
        '<b>ขั้นที่ 2 · ใช้ข้อมูลที่ว่าส่วนโค้งยาวเพิ่มขึ้น $4$ หน่วย มาแก้หา $\\theta$</b>',
        '• สูตรที่ใช้ : (ส่วนโค้งที่เพิ่มขึ้น) $=$ (ส่วนโค้งใหม่) $-$ (ส่วนโค้งเดิม) $= s_{2} - s_{1}$',
        '• แทนค่า : $9\\theta - 6\\theta = 4$',
        '• ยุบ : ดึงตัวประกอบร่วม $\\theta$ ออกมา จะได้ $(9-6)\\theta = 4$ นั่นคือ $3\\theta = 4$ '
        '⇒ $\\theta = \\dfrac{4}{3}$ เรเดียน',
        '• ⚠️ จุดชี้เป็นชี้ตายของข้อนี้อยู่ตรงนี้ : ตัวหารคือ <b>ผลต่างของรัศมี</b> ซึ่งเท่ากับ $9 - 6 = 3$ '
        '⛔ ไม่ใช่ $9$ และ ⛔ ไม่ใช่ $6$ · เหตุผลอ่านออกจากบรรทัดบนได้ตรง ๆ คือหลังดึง $\\theta$ ออกมาเป็นตัวประกอบร่วมแล้ว '
        'ของที่เหลือคือ $(9-6)$ ทั้งก้อน เพราะเลข $4$ ที่โจทย์ให้เป็นผลต่างของส่วนโค้ง '
        'จึงต้องจับคู่กับผลต่างของรัศมี ไม่ใช่กับรัศมีตัวใดตัวหนึ่งซึ่งจับคู่กับส่วนโค้งทั้งเส้น',
        '• ตรวจว่ามุมที่ได้ใช้ได้จริงก่อนไปต่อ : $\\theta = \\dfrac{4}{3} \\approx 1.33$ เรเดียน '
        'ซึ่งเป็นจำนวนบวก และไม่เกินหนึ่งรอบเพราะ $2\\pi \\approx 6.28$ '
        '⇒ $0 < \\dfrac{4}{3} \\le 2\\pi$ ✓ เป็นมุมที่จุดศูนย์กลางของเซกเตอร์ได้จริง',
        '',
        '<b>ขั้นที่ 3 · เขียนผลต่างของพื้นที่ให้อยู่ในรูปที่มี $\\theta$ ตัวเดียว</b>',
        '• สูตรที่ใช้ : $A = \\dfrac{1}{2}r^{2}\\theta$',
        '• ระบุตัวแปร : พื้นที่เดิม $A_{1} = \\dfrac{1}{2}\\left(6^{2}\\right)\\theta$ · '
        'พื้นที่ใหม่ $A_{2} = \\dfrac{1}{2}\\left(9^{2}\\right)\\theta$ '
        'โดย $\\theta$ ยังเป็นตัวเดียวกันอยู่เหมือนเดิม เพราะการเพิ่มรัศมีไม่ได้ไปแตะมุมเลย',
        '• แทนค่าแล้วลบกัน : $A_{2} - A_{1} = \\dfrac{1}{2}\\left(9^{2}\\right)\\theta '
        '- \\dfrac{1}{2}\\left(6^{2}\\right)\\theta$',
        '• ยุบ : ดึง $\\dfrac{1}{2}\\theta$ ออกมาเป็นตัวประกอบร่วม จะได้ '
        '$A_{2} - A_{1} = \\dfrac{1}{2}\\theta\\left(9^{2} - 6^{2}\\right) = \\dfrac{1}{2}\\theta(81 - 36) '
        '= \\dfrac{1}{2}\\theta(45)$',
        '• ⚠️ กับดักคู่แฝดของขั้นที่ 2 : สิ่งที่เข้าวงเล็บคือ <b>ผลต่างของกำลังสอง</b> '
        '$9^{2} - 6^{2} = 45$ ⛔ ไม่ใช่กำลังสองของผลต่าง $(9-6)^{2} = 9$ · '
        'เหตุผลคือสูตรพื้นที่ยกกำลังสองรัศมีของแต่ละรูปเสียก่อน แล้วเราจึงค่อยเอาผลลัพธ์มาลบกัน '
        'ลำดับการทำงานสองอย่างนี้สลับกันไม่ได้',
        '',
        '<b>ขั้นที่ 4 · แทนค่า $\\theta$ ที่หาได้ แล้วคิดออกมาเป็นตัวเลข</b>',
        '• แทน $\\theta = \\dfrac{4}{3}$ ลงในนิพจน์ของขั้นที่ 3 : '
        '$A_{2} - A_{1} = \\dfrac{1}{2}\\left(\\dfrac{4}{3}\\right)(45)$',
        '• ยุบทีละก้าว : $\\dfrac{1}{2}\\left(\\dfrac{4}{3}\\right) = \\dfrac{2}{3}$ '
        '⇒ $A_{2} - A_{1} = \\dfrac{2}{3} \\times 45 = 30$',
        '• ตรวจความสมเหตุสมผล : ค่าที่ได้เป็นจำนวนบวก ซึ่งต้องเป็นเช่นนั้นอยู่แล้วเพราะรัศมีโตขึ้น '
        'พื้นที่จึงต้องโตตาม · และไม่มี $\\pi$ ติดค้างมาด้วย ตรงกับที่คาดไว้ตั้งแต่ตอนอ่านโจทย์',
        '',
        '✔ <b>ตรวจคำตอบ (วิธีอิสระ · คิดพื้นที่ของเซกเตอร์ทั้งสองรูปแยกกันออกมาเป็นตัวเลขจริงก่อน '
        'แล้วค่อยนำมาลบกันตอนท้าย ⛔ ไม่ใช้รูปผลต่างของกำลังสองเลยแม้แต่ครั้งเดียว)</b>',
        '• พื้นที่ของเซกเตอร์รูปเดิม : $A_{1} = \\dfrac{1}{2}(36)\\left(\\dfrac{4}{3}\\right) '
        '= 18 \\times \\dfrac{4}{3} = 24$ ตารางหน่วย',
        '• พื้นที่ของเซกเตอร์รูปใหม่ : $A_{2} = \\dfrac{1}{2}(81)\\left(\\dfrac{4}{3}\\right) '
        '= \\dfrac{81}{2} \\times \\dfrac{4}{3} = 54$ ตารางหน่วย',
        '• ผลต่าง : $54 - 24 = 30$ ตารางหน่วย ✓ ตรงกับเส้นทางแรกพอดี '
        'ทั้งที่เส้นทางนี้ไม่ได้แตะเอกลักษณ์ $a^{2}-b^{2}$ เลย',
        '• ตรวจย้อนกลับไปหาข้อมูลที่โจทย์ให้มาอีกชั้นหนึ่ง : ส่วนโค้งเดิมยาว '
        '$6\\left(\\dfrac{4}{3}\\right) = 8$ หน่วย · ส่วนโค้งใหม่ยาว $9\\left(\\dfrac{4}{3}\\right) = 12$ หน่วย '
        '⇒ ยาวเพิ่มขึ้น $12 - 8 = 4$ หน่วย ✓ ตรงกับที่โจทย์บังคับไว้เป๊ะ ๆ '
        '⇒ ค่า $\\theta = \\dfrac{4}{3}$ ที่ใช้ไปนั้นถูกต้องแน่นอน',
        '• ตรวจซ้ำอีกทางด้วยสูตรที่ไม่ใช้มุมเลย : พื้นที่เซกเตอร์เขียนได้อีกแบบว่า $A = \\dfrac{1}{2}rs$ '
        '⇒ รูปเดิมได้ $\\dfrac{1}{2}(6)(8) = 24$ ✓ · รูปใหม่ได้ $\\dfrac{1}{2}(9)(12) = 54$ ✓ '
        'ลงตัวตรงกันทั้งสามทาง',
        '',
        '✅ <b>คำตอบ</b> พื้นที่ของเซกเตอร์รูปนี้เพิ่มขึ้นจากเดิม $30$ ตารางหน่วย '
        '(จากเดิม $24$ ตารางหน่วย เป็น $54$ ตารางหน่วย)',
        '',
        '💡 <b>เทคนิค</b>',
        '• เจอคำว่า “เท่าเดิม” หรือ “คงที่” ในโจทย์ที่มีสองสถานการณ์ ให้รีบเขียนของสิ่งนั้นด้วยสัญลักษณ์ตัวเดียวกันทันที '
        'นั่นคือของขวัญที่โจทย์แอบยื่นให้ เพราะมันทำหน้าที่เป็นสะพานเชื่อมข้อมูลก่อนกับหลังเข้าด้วยกัน '
        'และมักเป็นตัวที่ตัดทิ้งหรือรีดค่าออกมาได้ในภายหลัง',
        '• ปริมาณที่โจทย์บอกว่า “เพิ่มขึ้น” ให้เขียนเป็นการลบของสองนิพจน์เต็ม ๆ ก่อนเสมอ '
        'แล้วค่อยดึงตัวประกอบร่วมออก ⇒ จะเห็นเองว่าอะไรควรเป็นตัวหาร '
        'วิธีนี้กันพลาดได้ดีกว่าการรีบหารด้วยเลขที่เห็นเด่นที่สุดในโจทย์',
        '• เมื่อได้ขนาดของมุมที่จุดศูนย์กลางมาแล้ว ให้เช็คทันทีว่าอยู่ในช่วง $0 < \\theta \\le 2\\pi$ หรือไม่ '
        'เพราะมุมที่จุดศูนย์กลางของเซกเตอร์กางเกินหนึ่งรอบไม่ได้ ⇒ ถ้าหลุดกรอบนี้แปลว่าคำนวณผิดตั้งแต่ต้น',
        '',
        '⚠️ <b>จุดพลาด</b>',
        '• ได้ค่า $10$ เพราะหาขนาดมุมผิดเป็น $\\theta = \\dfrac{4}{9}$ คือเอาส่วนโค้งที่เพิ่มขึ้น $4$ '
        'ไปหารด้วย<b>รัศมีใหม่</b> $9$ แล้วคิดต่อได้ $\\dfrac{1}{2}\\left(\\dfrac{4}{9}\\right)(45) = 10$ '
        '· ต้นเหตุคือเผลออ่านเลข $4$ เป็นความยาวส่วนโค้งของเซกเตอร์รูปใหม่ทั้งเส้น '
        'ทั้งที่โจทย์บอกว่าเป็นเพียงส่วนที่<b>เพิ่มขึ้น</b> · ค่านี้ผิดแน่นอน ตรวจได้ทันทีโดยลองสมมติว่า '
        '$\\theta = \\dfrac{4}{9}$ จริง จะได้ส่วนโค้งเดิมยาว $6\\left(\\dfrac{4}{9}\\right) = \\dfrac{8}{3}$ '
        'และส่วนโค้งใหม่ยาว $9\\left(\\dfrac{4}{9}\\right) = 4$ ⇒ ยาวเพิ่มขึ้นเพียง '
        '$4 - \\dfrac{8}{3} = \\dfrac{4}{3} \\approx 1.33$ หน่วย ซึ่งไม่ใช่ $4$ หน่วยตามที่โจทย์บังคับ',
        '• ได้ค่า $15$ เพราะหาขนาดมุมผิดเป็น $\\theta = \\dfrac{4}{6}$ คือเอา $4$ ไปหารด้วย<b>รัศมีเดิม</b> $6$ '
        'แล้วคิดต่อได้ $\\dfrac{1}{2}\\left(\\dfrac{2}{3}\\right)(45) = 15$ '
        '· เป็นความพลาดชนิดเดียวกับข้อบนแต่หยิบรัศมีคนละตัว ⇒ ยืนยันว่าการหารด้วยรัศมี<b>ตัวใดตัวหนึ่ง</b> '
        'ไม่ใช่ทางที่ถูก · ตรวจได้โดยแทนกลับ : ถ้า $\\theta = \\dfrac{2}{3}$ ส่วนโค้งเดิมยาว '
        '$6\\left(\\dfrac{2}{3}\\right) = 4$ และส่วนโค้งใหม่ยาว $9\\left(\\dfrac{2}{3}\\right) = 6$ '
        '⇒ ยาวเพิ่มขึ้น $6 - 4 = 2$ หน่วย ไม่ใช่ $4$ หน่วย',
        '• ได้ค่า $6$ เพราะหามุมได้ถูกต้องแล้วว่า $\\theta = \\dfrac{4}{3}$ แต่ไปคิดผลต่างของพื้นที่เป็น '
        '$\\dfrac{1}{2}\\theta(9-6)^{2} = \\dfrac{1}{2}\\left(\\dfrac{4}{3}\\right)(9) = 6$ '
        'คือยกกำลังสองผลต่างของรัศมี แทนที่จะใช้ผลต่างของกำลังสองของรัศมี '
        '· ค่านี้ผิดเพราะ $(9-6)^{2} = 9$ ส่วน $9^{2} - 6^{2} = 45$ ซึ่งต่างกันลิบลับ '
        '· มองเชิงรูปก็ยิ่งชัด นิพจน์ $\\dfrac{1}{2}\\theta(3)^{2}$ คือพื้นที่ของเซกเตอร์รัศมี $3$ '
        'ซึ่งเป็นรูปที่ไม่มีอยู่ในโจทย์เลยสักรูป · แทนกลับด้วยตัวเลขจริงก็ปิดคดีได้ '
        'พื้นที่รูปเดิมคือ $24$ และรูปใหม่คือ $54$ ⇒ ผลต่างที่แท้จริงคือ $30$ ไม่ใช่ $6$',
        '• ได้ค่า $60$ เพราะลืมสัมประสิทธิ์ $\\dfrac{1}{2}$ ในสูตรพื้นที่เซกเตอร์ '
        '⇒ คิดเป็น $\\theta(81 - 36) = \\dfrac{4}{3}(45) = 60$ '
        '· สังเกตว่าค่านี้เป็นสองเท่าของคำตอบที่ถูกต้องพอดี ซึ่งเป็นลายเซ็นประจำตัวของการลืมหารสอง '
        '· ตรวจได้โดยดูว่าถ้าใช้สูตรที่ลืม $\\dfrac{1}{2}$ พื้นที่รูปเดิมจะกลายเป็น $48$ และรูปใหม่จะเป็น $108$ '
        'แต่สูตร $A = \\dfrac{1}{2}rs$ ซึ่งเป็นคนละหน้าตากันให้ค่า $24$ กับ $54$ ⇒ ขัดกันเอง '
        'จึงรู้ได้ว่าเส้นทางที่ลืม $\\dfrac{1}{2}$ นั้นผิด',
        '• ได้ค่า $\\dfrac{4}{3}$ เพราะหยุดกลางทาง ตอบขนาดของมุมที่จุดศูนย์กลางแทนผลต่างของพื้นที่ '
        '· ค่านี้เป็นเพียงผลพลอยได้ของขั้นที่ 2 เท่านั้น ยังไม่ได้ตอบสิ่งที่โจทย์ถาม '
        '· สังเกตหน่วยก็จับได้ทันที เพราะโจทย์ถามหาจำนวน<b>ตารางหน่วย</b> แต่ $\\dfrac{4}{3}$ มีหน่วยเป็นเรเดียน '
        'ซึ่งเป็นหน่วยของมุม ไม่ใช่หน่วยของพื้นที่',
    ],
    'V.mold: G = one and the same sector whose radius is enlarged from 6 units to 9 units while the '
    'central angle is explicitly held fixed, with the only numeric fact about the change being that the '
    'arc grew longer by 4 units, and with the central angle itself never handed over / A = the increase '
    'in the area of the sector, asked as a free numeric response in square units with no candidate values '
    'printed anywhere on the page / M = registered as G-SECTOR-RADIUS-GROWS-ARC-DELTA / A-AREA-DELTA / '
    'M-ARC-INCREMENT-TO-ANGLE-THEN-AREA in molds.py: carry a single symbol theta through both states '
    'because the angle is fixed, read the arc increment as 9*theta - 6*theta so that the divisor is the '
    'difference of the radii 9 - 6 = 3 and never one radius alone, recover theta = 4/3 radians, check it '
    'against the interval 0 < theta <= 2*pi, then write the area increment as (1/2)*theta*(9**2 - 6**2), '
    'a difference of squares and not a square of a difference, and evaluate it to 30. '
    'Rubric F2 C1 P1 T1 L0 = 5/15, at least 3 with T at most 2 and total below 8 so the hard band is not '
    'reached -> level: ปานกลาง. F = 2 because two formulas are genuinely required and neither substitutes '
    'for the other, the arc length s = r*theta which is the only door into the unknown angle and the '
    'sector area (1/2)*r**2*theta which is the only door out of it; the algebraic identity for a '
    'difference of squares is school algebra and is not billed as a third formula. C = 1 because the two '
    'formulas are chained in one direction only, arc first and area second, and the whole item sits '
    'inside the single subtopic 7.11 rather than reaching into a second one the way a C = 2 item does. '
    'P = 1 and deliberately not 2 because once theta is in hand the remaining work is a single '
    'substitution followed by one multiplication, 45 times 2/3, with no case split, no second equation '
    'and no rearrangement worth the name; the norm set by q113 and q145 puts arithmetic of this weight at '
    'one. T = 1 because there is exactly one hidden condition, namely that the 4 units are a difference '
    'and must therefore be divided by the difference of the radii, which is the trap the values 10 and 15 '
    'are built from; the second slip about squares is the same reading error wearing different clothes '
    'rather than an independent discovery, so the count stays at one and does not climb to 2. L = 0 '
    'because the statement is a bare symbolic sector with no real-world scene, no figure and no '
    'three-dimensional object, and a reader can substitute into the formulas without drawing anything at '
    'all. Scoring was written before the level was read off. '
    'sympy (verify_b21.py): the q151 block solves 9*th - 6*th = 4 for a positive symbol and returns '
    'theta = 4/3, confirms numerically that 4/3 does not exceed 2*pi so the angle really can be a central '
    'angle, evaluates (1/2)*theta*(81 - 36) to exactly 30 which matches the stored key 30 and its '
    'accepted decimal form 30.0, and confirms that the key is rational so that a student never has to '
    'type a surd or a pi. Two of the error paths were machine computed in that same block, '
    '(1/2)*(4/9)*45 = 10 for dividing by the new radius and (4/3)*45 = 60 for dropping the coefficient '
    '1/2; the remaining two were computed the same way rather than invented, (1/2)*(2/3)*45 = 15 for '
    'dividing by the old radius and (1/2)*(4/3)*(9-6)**2 = 6 for squaring the difference. Every wrong '
    'value was then pushed back through the data the statement fixes so that each pitfall line carries '
    'its own refutation: theta = 4/9 makes the arc grow by 4 - 8/3 = 4/3 and theta = 2/3 makes it grow by '
    '6 - 4 = 2, neither of which is the 4 the statement demands. The independent check was verified too, '
    'the two areas standing alone are (1/2)*36*(4/3) = 24 and (1/2)*81*(4/3) = 54 whose difference is 30, '
    'the two arcs are 6*(4/3) = 8 and 9*(4/3) = 12 whose difference is 4, and the angle free form '
    'A = (1/2)*r*s reproduces both areas as (1/2)*6*8 = 24 and (1/2)*9*12 = 54. '
    'Collision sweep on 6457 items (bank 63 files + k1 out + k2 out), run inline for this item with the '
    'corpus assembly of collide_b19.py because collide_b21.py is not committed yet: the Thai word for '
    'sector appears in the question text of exactly 13 items in the whole corpus, and not one of them '
    'enlarges or otherwise changes the radius of a sector, the pattern for a radius being increased next '
    'to a sector returning zero items; the pattern for an arc growing longer returns zero and the pattern '
    'for an area increasing over a former value returns zero as well, so the whole idea of a before state '
    'and an after state is new to the bank. WATCH, disclosed rather than hidden: the nearest relative is '
    'gen-chap-07-trigonometry-q032, which stands two concentric circles of radii 5 and 8 and cuts both '
    'with one pair of radii so that the two sectors share a central angle, hands over the area between '
    'the two arcs as 39*pi/4 and asks how much longer the outer arc is than the inner one. That item '
    'shares the algebraic skeleton but runs it backwards, from an area difference to an arc difference, '
    'while this item runs from an arc difference to an area difference, so A is the opposite quantity and '
    'M is the reverse traversal; G differs as well because q032 has two circles standing at the same '
    'moment whereas this one has a single sector before and after a change, and q032 keeps pi in both its '
    'data and its answer 3*pi/2 whereas every number here is rational. The other sector neighbours are '
    'further off: gen-chap-07-trigonometry-q119 sets two sectors of equal area with one radius twice the '
    'other and asks for a ratio of arcs with no numbers at all, gen-chap-07-trigonometry-q115 equates two '
    'sector areas to solve for a radius, and q113 and q114 are single sector formula items with nothing '
    'changing. Inside this same batch q152 also uses a difference of squares of radii, but its central '
    'angle is handed over directly so the arc increment step that is the entire point of this item never '
    'occurs there, and its answer carries pi. Since this is a fill item there is no choice list, so no '
    'answer slot exists and nothing about the answer could have been positioned by hand.',
)

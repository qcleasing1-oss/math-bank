# -*- coding: utf-8 -*-
"""shortnames.py — ชื่อวิธีฉบับย่อ สำหรับวางในหัว 【 】

เหตุผล : ตัวอย่างที่ครูส่งมายาวราว 60–75 ตัวอักษรทั้งบรรทัด
  【 วิธีที่ 1 ▸ พื้นฐาน · จุดตัดแล้วทดสอบเครื่องหมายทีละช่วง (sign-line test) 】
ชื่อรอบแรกใน methods.py ยาวเกินไป (สูงสุด 103 ตัวอักษร ⇒ หัวยาว 144)
ผู้เขียน 6 คนรายงานตรงกันว่าเกินเป้า ⇒ ย่อที่ตารางนี้ที่เดียว
⛔ ห้ามย่อจนความหมายเปลี่ยน — ชื่อต้องยังบอกได้ว่าวิธีนั้นทำอะไร และต้องมีอังกฤษในวงเล็บ
"""

BASIC = {
 'q165': 'ตอบทีละพจน์ตามช่วงหลัก (principal-value evaluation)',
 'q166': 'เปลี่ยนตัวแปรพร้อมเลื่อนช่วง (substitution with interval shift)',
 'q167': 'กระจายมุมสองเท่าแล้วดึงตัวร่วม (double-angle then factoring)',
 'q168': 'สามเหลี่ยมอ้างอิงบนช่วงหลัก (reference right triangle)',
 'q169': 'สูตรผลบวกมุม $45^\\circ + 30^\\circ$ (angle-sum formula)',
 'q170': 'คู่สังยุคของ $\\csc$ กับ $\\cot$ (conjugate pair)',
 'q171': 'มุมสองเท่ารูปไซน์ล้วน (sine-only double angle)',
 'q172': 'ล็อกจตุภาคครึ่งมุม แล้วใช้รูปไม่มีราก (sign-free half-angle)',
 'q173': 'ผลคูณจากพื้นที่ คู่กำลังสองสมบูรณ์ (product-and-sum)',
 'q174': 'ระยะตั้งฉากแล้วหาคอร์ด (perpendicular distance and chord)',
 'q175': 'กฎของโคไซน์แล้วต่อกฎของไซน์ (law of cosines, then law of sines)',
 'q176': 'กฎของโคไซน์ที่มุม $B$ แล้วอ่านความสูง (law of cosines, then height)',
 'q177': 'คุมโดเมนก่อน แล้วยกกำลังสอง (domain first, then squaring)',
 'q178': 'กฎของไซน์คู่สูตรมุมสองเท่า (law of sines with double angle)',
 'q179': 'สองสมการมุมเงย กำจัดระยะฐาน (two elevation equations)',
 'q180': 'กฎของโคไซน์โดยตรง (law of cosines)',
 'q181': 'แยกกรณีด้วยสูตรผลบวกอาร์กแทนเจนต์ (arctangent addition rule)',
 'q182': 'หามุมภายในก่อน แล้วลบจาก $180^\\circ$ (interior angle first)',
 'q183': 'ตั้งสมการกำลังสองแล้วหารากทั้งสอง (solve the quadratic)',
 'q184': 'อาร์กโคไซน์เป็นฟังก์ชันลด คู่โดเมน (decreasing-function argument)',
}

APPLIED = {
 'q165': 'เอกลักษณ์เติมเต็มของ $\\arcsin$ กับ $\\arccos$ (complementary identity)',
 'q167': 'ผลต่างไซน์เป็นผลคูณ (sum-to-product)',
 'q169': 'มุมครึ่งแล้วคลายรากซ้อน (half-angle then denesting)',
 'q172': 'แทนครึ่งมุมแบบไวเออร์ชตราสส์ (Weierstrass substitution)',
 'q174': 'เวียตาบนสมการระยะ (Vieta on the distance equation)',
 'q175': 'รัศมีวงล้อมจากพื้นที่ (circumradius from area)',
 'q176': 'ประกบสามเหลี่ยมมุมฉากสองรูป (Pythagorean decomposition)',
 'q178': 'ทฤษฎีบทมุมสองเท่า $b^{2} = c(c + a)$ (double-angle triangle theorem)',
 'q179': 'สูตรผลต่างแทนเจนต์ (tangent-difference formula)',
 'q180': 'วางพิกัดฉากแล้ววัดระยะ (coordinate method)',
 'q181': 'แทนด้วยแทนเจนต์ (tangent substitution)',
 'q183': 'เวียตา · ผลต่างรากจากผลบวกกับผลคูณ (Vieta’s difference of roots)',
 'q184': 'แปลงเป็นอาร์กไซน์ด้วยเอกลักษณ์เติมเต็ม (complementary identity)',
}

# ⛔ ชื่ออังกฤษต้องมีทุกตัว (กฎที่ครูสั่ง : "ชื่อวิธีทั้งภาษาไทยภาษาอังกฤษ")
for _t in (BASIC, APPLIED):
    for _k, _v in _t.items():
        assert _v.count('(') >= 1 and _v.rstrip().endswith(')'), (_k, _v)
assert set(BASIC) == {f'q{n}' for n in range(165, 185)}
assert set(APPLIED) <= set(BASIC)

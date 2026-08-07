# ใบสั่งออกแบบโจทย์ · ก้อน 20 · ชุด `gen-chap-07-trigonometry` (ข้อ q125–q144)

คุณคือผู้ออกแบบ **โจทย์ + ตัวเลือก + คำตอบ** เท่านั้น ⛔ ยังไม่ต้องเขียนเฉลยละเอียด

## ⛔ กฎเหล็กที่ผิดไม่ได้เลย

1. **ทุกข้อไม่มีรูป** — `hasImage: false` · ⛔ ห้ามมีคำว่า “ดังรูป” “จากรูป” “รูปที่กำหนด” ในโจทย์
   ⇒ ถ้าโจทย์ต้องอาศัยรูป **ให้บรรยายด้วยข้อความจนวาดตามได้** หรือเปลี่ยนโจทย์
2. **ทุกข้อสมบูรณ์ในตัว** ⛔ ห้ามอ้างข้ออื่น (“จากข้อ…” “ข้างต้น” “เช่นเดิม”) — ระบบสุ่มลำดับข้อ
3. **LaTeX**: ใช้ `\dfrac` ⛔ ห้าม `\frac` · องศาเขียน `30^\circ` ⛔ ห้าม `30°` · ⛔ ห้าม `√` ดิบ (ใช้ `\sqrt{}`)
   ⛔ ห้ามใช้ `\"` — ใช้อัญประกาศไทย `“ ”`
4. ⛔ ห้ามใช้สำนวน **“มากที่สุดเท่ากับ” / “น้อยที่สุดเท่ากับ”** (กำกวม) ⇒ เขียน “ค่าสูงสุดที่เป็นไปได้คือ”
5. **ตัวลวงต้องมีที่มาจริง** — ทุกตัวเลือกผิดต้องตอบได้ว่า “เด็กพลาดขั้นไหนถึงได้ค่านี้”
   ⛔ ห้ามสุ่มเลขใกล้เคียง · ต้องเขียน trap ของแต่ละตัวมาให้ครบ
6. **ต้อง verify ด้วย sympy จริง** ก่อนส่ง — ทั้งคำตอบและทุกเส้นทางตัวลวง (รันโค้ดจริง ⛔ ไม่ใช่คิดในหัว)
7. ข้อชนิด **`fill`**: คำตอบต้องเป็น **จำนวนตรรกยะ** ⛔ ห้ามให้เด็กพิมพ์กรณฑ์ · `\pi` · ทศนิยมไม่รู้จบ
   และ ⛔ **ห้ามมีคำว่า “ตัวเลือก” ที่ไหนเลยในข้อนั้น**
8. ข้อชนิด **`mc`**: 4 ตัวเลือก · ถ้าเป็นค่าตัวเลข **ให้เรียงจากน้อยไปมาก** (ด่านตรวจข้อนี้)

## ⛔ ฉากหลังโลกจริงที่ห้ามใช้ (อิ่มตัวแล้ว)

บันได · ทางลาด · ชิงช้าสวรรค์ · เสาธง · รอก/สายพาน · แพะผูกเชือก · เข็มนาฬิกา · ถังนอนราบ ·
ม้วนกรวย · โรงเรือน · ประภาคาร · เรือสองลำ · ลูกตุ้ม · มุมเงยจากสองจุดสังเกต

📌 **ฉากหลังไม่ใช่เงื่อนไขของความยาก** — ถ้าคิดฉากหลังไม่ออก ให้ทำเป็นเรขาคณิต/พีชคณิตล้วน
ก้อนก่อนได้ระดับ “ยากมาก” โดยไม่ใช้ฉากหลังเลย ด้วยการ **ต่อกุญแจหลายดอก**

## ⛔ แม่พิมพ์ที่อิ่มตัวแล้ว ห้ามแตะ

ผลบวกคำตอบสมการตรีโกณ · ผลคูณโคไซน์ยุบมุมสองเท่า · `a sin x + b cos x = c` มุมช่วย ·
ค่านิพจน์ arc ซ้อน · ผลบวก arctan · สมการ arcsin+arccos · `sin x + cos x = ค่าคงที่` ·
มุมสองเท่าไปข้างหน้า · พื้นที่สามเหลี่ยม ½ab sin C · โดเมน arcsin/arccos อาร์กิวเมนต์เชิงเส้น ·
**พื้นที่เซกเมนต์ = เซกเตอร์ − สามเหลี่ยม** · พื้นที่รูป n เหลี่ยมด้านเท่าแนบในวงกลม
(ถามได้แต่ **เส้นรอบรูป** และห้ามใช้ตัวแปร `a` เป็นรัศมี)

## เกณฑ์ระดับ (ให้คะแนนก่อน แล้วค่อยอ่านระดับ ⛔ ห้ามเลือกระดับแล้วย้อนหาคะแนน)

`F` สูตรที่ต้องใช้ · `C` การต่อกุญแจ · `P` ความยาวการคำนวณ · `T` กับดัก/เงื่อนไขซ่อน · `L` ภาระแปลโจทย์
แต่ละมิติ 0–3 · รวมเต็ม 15

```
รวม ≥ 12 และ (T = 3 หรือ (T ≥ 2 และ F = 3))  ⇒ ยากมาก
รวม ≥ 8  และ (T ≥ 2 หรือ C ≥ 2)               ⇒ ยาก
รวม ≥ 3  และ T ≤ 2                            ⇒ ปานกลาง
รวม ≤ 2  และ T ≤ 1 และ C = 0                  ⇒ ง่าย
```

`L`: 0 = สัญลักษณ์ล้วน/เรขาคณิตที่แทนค่าได้ทันที · 1 = ต้องวาดเอง หรือบริบทระนาบเดียว · 2 = สามมิติ

## ทะเบียนแม่พิมพ์ — ต้องเลี่ยงของเดิม

ทุกข้อต้องระบุ **3 ส่วน**: `G` (โจทย์ให้อะไร) · `A` (ถามหาอะไร) · `M` (เครื่องมือหลักที่ใช้แก้)
⛔ **ห้ามตรงกับข้อเดิมทั้งสามส่วน** และพยายามอย่าให้ `M` ซ้ำของเดิมเลย

`M` ที่ใช้ไปแล้ว (⛔ อย่าใช้ซ้ำ — ตั้งชื่อใหม่ที่บอกกลไกจริง):
M-SECTOR-FORMULAS · M-REDUCTION · M-LAW-COS · M-PYTHID-CONJ · M-PYTHAG-DEF · M-REF-TRIANGLE ·
M-REF-ANGLE-SIGN · M-DOUBLE · M-MOD2PI · M-SOLVE-SET-GENERAL · M-TAN-TRI-IDENT · M-HALF-YUB ·
M-AMGM · M-CUBE-FACTOR · M-PARAM-RANGE · M-UC-SYMMETRY · M-AMP-MID-PERIOD · M-RANGE-BOUND ·
M-PYTHID-EXPAND · M-SUMDIFF · M-LAW-SIN · M-DIST-FORMULA · M-LCM-PERIOD · M-TRANSFORM-ORDER ·
M-ABS-PIECEWISE · M-LINE-INTERSECT-UC · M-COUNT-CYCLE · M-RANGE-RECIP · M-DENOM-ZERO ·
M-AUX-ANGLE · M-GRAPH-COUNT · M-QUAD-IN-TRIG · M-SIGN-TABLE · M-UC-COMPARE · M-INEQ-UC ·
M-MONOTONE-UC · M-ZERO-COUNT-PARAM · M-ARC-COMPLEMENT-QUAD · M-ARC-PRINCIPAL-FOLD ·
M-DOUBLE-INEQ-QUAD · M-AMBIGUOUS-EXISTENCE · M-DIAG-TWICE-LAWCOS · M-POWER-REDUCTION ·
M-HALFANGLE-COLLAPSE · M-TWO-BRANCH-DEDUP · M-SPLIT-SUMDIFF · M-ARC-RAD-TO-DEG ·
M-AREA-HALF-AB-SIN · M-COTERMINAL-REDUCE · M-SPECIAL-ANGLE-SUBST · M-LAWCOS-ON-SUB-TRIANGLE ·
M-RIGHT-TRI-SINE-DIRECT · M-SHARED-HEIGHT-SINE-TWICE · M-MINIMUM-EQUALITY-CASE ·
M-DOUBLE-REVERSE · M-PRINCIPAL-RANGE-AFFINE-MAP · M-SPLIT-SUMDIFF-RATIO · M-AREA-SPLIT-HALF-ANGLE ·
M-THREE-SECTORS-DIFF-RADII · M-DOUBLE-COLLAPSE-EVAL · M-FACTOR-PYTHID-CANCEL ·
M-SEGMENT-AREA-TIMES-LENGTH · M-OBLIQUE-TRI-LAW-SIN · M-EXPAND-TO-SINCOS-CANCEL ·
M-SIGN-BY-QUADRANT-THEN-SUM · M-DOUBLE-ANGLE-COLLAPSE-TO-TAN · M-COMMON-DENOM-SYMMETRIC-COLLAPSE ·
M-REF-TRIANGLE-WITH-SIGN · M-FACTOR-QUAD-COUNT-BRANCHES · M-COFUNCTION-TWO-FAMILIES ·
M-HEIGHT-THEN-COSINE-LAW · M-PYTHID-DIRECT · M-SCALE-FACTOR-PYTHAG · M-PYTHAG-QUADRATIC-SOLVE ·
M-TWO-TANGENTS-SHARED-LEG · M-HALF-ANGLE-TAN-IN-RIGHT-TRI · M-SIMILAR-RIGHT-TRIANGLES ·
M-CENTRAL-ANGLE-HALF-CHORD · M-DROP-TWO-ALTITUDES-TAN · M-HALF-R-TIMES-ARC · M-ELIMINATE-RADIUS ·
M-EQUATE-AREAS-SOLVE-RADIUS · M-RATIO-OF-FULL-TURN · M-INSCRIBED-CIRCLE-IN-SECTOR ·
M-ARC-AND-CHORD-HALF-ANGLE · M-AREA-INVARIANT-SCALING · M-READ-COEFFICIENT ·
M-PERIOD-FROM-COEFF · M-EVALUATE-DIRECT · M-MATCH-PERIOD-AND-SHIFT · M-HALF-PERIOD-FROM-MAX-TO-MIN

## รูปแบบผลลัพธ์ที่ต้องส่งกลับ (JSON เท่านั้น ⛔ ไม่มีข้อความอื่นนอก JSON)

```json
{"items": [
 {"n": 125, "subTopics": ["7.1"], "level": "ง่าย", "type": "fill",
  "question": "ข้อความโจทย์ ...",
  "correct": "225/136",
  "accept": ["225/136", "\\dfrac{225}{136}"],
  "rubric": {"F":1,"C":0,"P":1,"T":0,"L":0},
  "mold": {"G":"G-...","A":"A-...","M":"M-..."},
  "traps": ["ค่าที่ได้ถ้าสลับ sin กับ cos = ... เพราะ ...", "..."],
  "sympy": "โค้ดที่รันจริงเพื่อยืนยัน (สั้น ๆ)"},
 {"n": 126, "subTopics": ["7.1"], "level": "ปานกลาง", "type": "mc",
  "question": "...", "choices": ["$...$","$...$","$...$","$...$"], "correct": 2,
  "rubric": {...}, "mold": {...},
  "traps": ["ตัวเลือก 1 มาจาก ...", "ตัวเลือก 2 มาจาก ...", "ตัวเลือก 4 มาจาก ..."],
  "sympy": "..."}
]}
```

`correct` ของ `mc` นับจาก **0** (ตัวเลือกที่เด็กเห็นเป็นช่อง `correct + 1`)

## 🆕 แม่พิมพ์ที่ **ก้อน 20** เพิ่งใช้ไป — ⛔ ห้ามซ้ำอีก

M-MIDSEGMENT-DOUBLE-TO-HYPOTENUSE (เส้นเชื่อมจุดกึ่งกลาง = ครึ่งด้านตรงข้ามมุมฉาก) ·
M-INRADIUS-RIGHT-TRI-AREA-OVER-S (รัศมีวงกลมแนบในสามเหลี่ยมมุมฉาก) ·
M-AP-SIDES-FORCE-3-4-5 (ด้านเป็นลำดับเลขคณิต) · M-MEDIAN-HALF-HYP-SYMMETRIC-SUM (มัธยฐานจากมุมฉาก) ·
M-INSCRIBED-SQUARE-THEN-BRANCH-PICK (จัตุรัสแนบในสามเหลี่ยมมุมฉาก) ·
M-EQUAL-CENTRAL-ANGLE-ARC-PROPORTION (ส่วนโค้งมุมที่จุดศูนย์กลางเท่ากัน) ·
M-SECTOR-TRIANGLE-AREA-RATIO (อัตราส่วนเซกเตอร์ต่อสามเหลี่ยม) ·
M-TANGENT-CIRCLES-CENTRAL-REGION-ARC-SUM (วงกลมสามวงสัมผัสกัน) ·
M-TWO-QUARTER-DISCS-INCLUSION-EXCLUSION (เสี้ยววงกลมสองรูปในจัตุรัส) ·
M-SEMICIRCLES-ON-SPLIT-DIAMETER-SOLVE-PART (ครึ่งวงกลมสามรูป) ·
M-ARC-FROM-NONSTANDARD-START (เริ่มวัดจากจุดที่ไม่ใช่ (1,0)) ·
M-QUARTER-TURN-BOTH-DIRECTIONS (หมุนควอเตอร์สองทิศ) ·
M-COLLAPSE-PRODUCT-TO-SINGLE-SIGN (ยุบ cos·tan = sin) ·
M-SUBQUADRANT-ARC-PICKS-BRANCH (ส่วนโค้งย่อยคร่อมสองจตุภาค) ·
M-PIECEWISE-BRANCH-SELECT (ฟังก์ชันนิยามเป็นช่วง) ·
M-COFUNCTION-PRODUCT-TO-SQUARE (ผลคูณโคฟังก์ชันยุบเป็นกำลังสอง) ·
M-ABS-TWO-BRANCH-ROOT-COUNT (ค่าสัมบูรณ์นับจำนวนคำตอบ) ·
M-DIVIDE-BY-COS-TO-TAN (หารด้วย cos ทั้งเศษและส่วน) ·
M-CONJ-SINE-PAIR-THEN-EXTRANEOUS-ROOT (คูณคอนจูเกต + รากแปลกปลอม) ·
M-RECIP-SQUARES-TO-TAN-QUAD-ROOT-PICK (ผลบวกส่วนกลับกำลังสอง)

⚠️ **ก้อน 20 ใช้ “ช่วงย่อยคัดราก” ไป 3 ข้อแล้ว** (q138 q143 q144)
⇒ ก้อนนี้ใช้ได้ไม่เกิน **1 ข้อ** ⛔ อย่าให้กลายเป็นสูตรสำเร็จของความยาก

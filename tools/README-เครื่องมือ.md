# 🧰 คู่มือเครื่องมือ math-bank — **27 ตัว** · ทุกตัวรันบนเครื่องครู · ค่า token = 0

> เปิด **Command Prompt** แล้วพิมพ์ 2 บรรทัดนี้ก่อนเสมอ
> ```
> A:
> cd "A:\โปรเจคสอนคณิตศาสตร์\math-bank"
> ```
> ต้องมี Python 3 (เช็คด้วย `python --version`) · ทุกตัวมี `--help`

## ⭐ ทางลัด: ดับเบิลคลิก `รูทีนประจำวัน.bat`
รันให้ครบ 5 อย่าง (รวมผล → หน้าติดตาม → ยามเฝ้างบ → STATUS → สำรองข้อมูล) แล้วเปิด `progress.html` ให้อัตโนมัติ

---

# 📊 กลุ่ม 1 — ดูความคืบหน้า

## 1. `progress.py` ⭐ ตัวหลัก
```
python tools\progress.py --queue _t1run\QUEUE_now.json --out _t1run\progress.html
```
หน้าเดียวเห็นครบ: ตัวเลขรวม · กราฟเสร็จรายวัน · **คิวถัดไป 40 ข้อ** · ตารางทุกชุด (เสร็จกี่ข้อ/ทั้งหมด · วันเวลาเสร็จล่าสุด)
**คลิกแถวชุด** → กางเป็นเลขข้อทุกข้อ 🟩เสร็จ 🟧ในคิว ⬜ยังไม่ทำ · **ชี้เมาส์ที่เลขข้อ** เห็นวันเวลาที่ทำเสร็จ + หัวข้อย่อย + ความยาก · มีช่องค้นหาและตัวกรอง

## 2. `stats.py` — แดชบอร์ดสั้น
```
python tools\stats.py --out _t1run\dashboard.html
```
ยอดรายบท/รายความยาก + ธงคุณภาพ 3 ตัว

## 3. `status_md.py` — สรุปสถานะไว้เปิดแชทใหม่ (ประหยัด token ตรง ๆ)
```
python tools\status_md.py --out STATUS.md
```
เปิดแชทใหม่แล้วให้ AI อ่านไฟล์นี้ไฟล์เดียว ⛔ ไม่ต้องเล่าประวัติซ้ำ

## 4. `token_estimate.py` — ดูราคาก่อนสั่งงาน
```
python tools\token_estimate.py --rest          ← ทำให้ครบทั้งคลังราคาเท่าไร
python tools\token_estimate.py --items 500     ← ทำอีก 500 ข้อราคาเท่าไร
```
⬤ ฐานราคาวัดจากเฉลยจริงที่ทำเสร็จแล้ว ⛔ ไม่ใช่ตัวเลขที่แต่งขึ้น

---

# 🔍 กลุ่ม 2 — ตรวจคุณภาพคลัง

## 5. `validate_bank.py` — ตรวจสุขภาพคลังทั้งใบ
```
python tools\validate_bank.py
```
จับ: ยอดจริง · ข้อติดหลายบท · id ซ้ำ · ป้ายความยากหาย · `correct` เกินช่วง · ตัวเลือกซ้ำ · **โจทย์อ้างรูป/ตารางแต่ไม่มีรูป** · รูปฝั่งเฉลย (เสี่ยงเฉลยรั่ว)

## 6. `old_vs_new.py` — หาข้อที่เฉลยน่าจะมีปัญหา
```
python tools\old_vs_new.py --out _t1run\old_vs_new.csv
```
🔴 ทั้งเก่าและใหม่ไม่ตรงเฉลย (เฉลยในคลังอาจผิด) · 🟠 เฉลยใหม่ไม่ตรง · เติม `--all` เพื่อดู 🟡 (สัญญาณลวงเยอะ)

## 7. `near_dup.py` — หาโจทย์ซ้ำ/คล้ายกันเองในคลัง
```
python tools\near_dup.py --same-topic --th 0.82 --out _t1run\near_dup.csv
```
`--th` ยิ่งสูงยิ่งเข้ม (0.9 = เกือบเหมือนกันเป๊ะ) · ⚠️ คล้าย ≠ ซ้ำ ต้องเปิดดูก่อน

## 8. `answer_bias.py` — เฉลยกระจุกไหม · ตัวลวงชี้เฉลยไหม
```
python tools\answer_bias.py --out _t1run\answer_bias.csv
```
แยกวิเคราะห์ตามจำนวนตัวเลือก (3/4/5 ตัวเลือกเทียบข้ามกันไม่ได้) + จับข้อที่เฉลยยาวกว่าตัวลวงมากจนเดาได้

## 9. `subtopic_map.py` — หัวข้อย่อยไหนยังไม่มีโจทย์
```
python tools\subtopic_map.py --out _t1run\subtopic_map.html
```
🟥 แดง = ยังไม่มีโจทย์เลย · 🟩 เขียว = มีเฉลยครบ · 🟨 เหลือง = ทำไปบ้าง

## 10. `normalize_tex.py` — จัดรูปสูตรให้เป็นแบบเดียวกัน
```
python tools\normalize_tex.py                 ← ตรวจอย่างเดียว (ปลอดภัย)
python tools\normalize_tex.py --write         ← แก้จริง (สำรองไฟล์เดิมให้อัตโนมัติ)
```
กฎ: `\( \)` `\[ \]` → `$ $` · `\tfrac` → `\dfrac` · เลขไทยในสูตร → เลขอารบิก

---

# ⚙️ กลุ่ม 3 — เดินสายงานผลิตเฉลย

## 11. `queue_builder.py` — สร้างคิว = คลัง − ที่ทำแล้ว
```
python tools\queue_builder.py --out _t1run\QUEUE_now.json
python tools\queue_builder.py --topic 7 --difficulty ยาก --limit 200 --skip-image --out _t1run\QUEUE_now.json
```
สร้าง `DONE.json` ให้ด้วย · นับกลับหลังเขียนเสมอ · คิวว่าง = หยุด ⛔ ไม่เขียนทับ

## 12. `merge_master.py` — รวมผลทุกไฟล์ ตัดซ้ำ
```
python tools\merge_master.py
```
เลือกฉบับดีที่สุดต่อข้อ: ตรงเฉลยก่อน → ขั้นตอน/กับดักเยอะกว่า → ยาวกว่า

## 13. `check_t1.py` — ตรวจเฉลยตามสเปก
```
python tools\..\_t1run\check_t1.py _t1run\results .
```
ฟิลด์ครบ · LaTeX · ความยาว · คำตอบตรงเฉลย · traps ตรงตัวลวง → `report.csv`

## 14. `budget_guard.py` — ยามเฝ้างบ + จับงานซ้ำ
```
python tools\budget_guard.py
```
เตือน 🔴 เมื่อ **พบฉบับซ้ำ** หรือ **ได้ของใหม่ 0 ตั้งแต่ครั้งก่อน** · บันทึกลง `_t1run\budget_log.csv`

## 15. `snapshot.py` — สำรองกันงานหาย
```
python tools\snapshot.py --keep 7
```
zip + ลายนิ้วมือ md5 เก็บใน `_snapshots\`

## 16. `folder_diff.py` — เทียบสองโฟลเดอร์
```
python tools\folder_diff.py "A:\โปรเจคสอนคณิตศาสตร์\สื่อการสอน" "A:\โปรเจคสอนคณิตศาสตร์\math-bank" --ext .json
```

---

# 🏫 กลุ่ม 4 — ใช้สอนจริงในห้องเรียน

## 17. `exam_builder.py` — ออกข้อสอบ + สลับชุด + เฉลย + กระดาษคำตอบ
```
python tools\exam_builder.py --topic 7 --n 20 --difficulty ปานกลาง ยาก --variants 2 --title "สอบกลางภาค ตรีโกณ"
```
- `--variants 2` = ชุด ก/ข สลับทั้งลำดับข้อและลำดับตัวเลือก **พร้อมเฉลยแยกชุด** ⇒ กันลอก
- **จำ id ที่เคยออกไว้** ⇒ ครั้งหน้าไม่ออกซ้ำ (ปิดด้วย `--allow-repeat`)
- `--skip-image` ข้ามข้อที่มีรูป · `--seed 1` ให้ได้ชุดเดิมซ้ำได้
- ได้ไฟล์เดียวมีครบ: กระดาษข้อสอบทุกชุด + เฉลย + กระดาษคำตอบ · **Ctrl+P พิมพ์** (เฉลย/id ไม่ติดไปกับกระดาษข้อสอบ)

## 18. `ladder_set.py` — ชุดฝึกไล่ระดับ ง่าย→ยาก
```
python tools\ladder_set.py --topic 7 --pattern 3,4,2 --out _t1run\ladder.html
```
สำหรับเด็กที่ตามไม่ทัน — หัวข้อเดียวกันแต่ไต่ระดับ

## 19. `reveal_viewer.py` — เฉลยเปิดทีละขั้น
```
python tools\reveal_viewer.py --limit 400 --out _t1run\reveal.html
```
ให้เด็กลองก่อน แล้วกด "เปิดขั้นถัดไป" ทีละขั้น · มีปุ่มใบ้ / กับดัก / เปิดทั้งหมด

## 20. `worked_example_picker.py` — ตัวอย่างสอนหน้าห้อง
```
python tools\worked_example_picker.py --per 2 --out _t1run\examples.html
```
หัวข้อย่อยละ 1-3 ข้อ เลือกฉบับที่อธิบายครบสุด

## 21. `formula_sheet.py` — ใบสรุปสูตรรายบท
```
python tools\formula_sheet.py --min 2 --out _t1run\formula_sheet.html
```

## 22. `trap_registry.py` — ทะเบียนกับดัก "เด็กมักพลาดตรงไหน"
```
python tools\trap_registry.py --out _t1run\trap_registry.html --csv _t1run\trap_registry.csv
```

## 23. `technique_index.py` — คลังเทคนิครายบท
```
python tools\technique_index.py --out _t1run\technique_index.html --csv _t1run\technique_index.csv
```

## 24. `figure_gen.py` — วาดรูปประกอบเป็น SVG
```
python tools\figure_gen.py unitcircle --angle 150 --out fig.svg
python tools\figure_gen.py triangle --a 7 --b 7 --angle 60 --out fig.svg
python tools\figure_gen.py polygon-in-circle --sides 6 --r 7 --out fig.svg
python tools\figure_gen.py numberline --from -3 --to 5 --marks="-1,2.5" --out fig.svg
python tools\figure_gen.py axes --fn "x**2-2" --out fig.svg
```
⚠️ ถ้าค่าติดลบให้ใช้ `--marks="-1,2"` (มีเครื่องหมาย =) กัน Windows เข้าใจผิดว่าเป็นออปชัน

---

# 👩‍🏫 กลุ่ม 5 — หลังสอบ (ต้องมีไฟล์คำตอบนักเรียน)

**รูปแบบไฟล์คำตอบ** — CSV หัวตารางแบบนี้เป๊ะ ๆ (ใช้ชื่อเล่น/เลขที่แทนชื่อจริงได้ · ⛔ ไฟล์อยู่บนเครื่องครู ไม่ส่งออกไปไหน)
```
student,id,answer
เลขที่ 1,pat1-2554-12-q17,3
เลขที่ 1,pat1-2554-12-q18,1
```

## 25. `item_analysis.py` — วิเคราะห์ข้อสอบ
```
python tools\item_analysis.py --responses คำตอบ.csv --out _t1run\item_analysis.csv
```
ได้ **ค่าความยาก p** · **อำนาจจำแนก r** (เด็กเก่ง-เด็กอ่อนแยกกันได้ไหม) · **ตัวลวงที่ไม่มีใครเลือก** ⇒ รู้ว่าข้อไหนควรแก้หรือทิ้ง

## 26. `remedial_set.py` — ใบงานซ่อมเสริมอัตโนมัติ
```
python tools\remedial_set.py --responses คำตอบ.csv --n 10 --out _t1run\remedial.html
python tools\remedial_set.py --responses คำตอบ.csv --student "เลขที่ 12" --n 8
```
ดูว่าพลาดหัวข้อย่อยไหนบ่อย → ดึงโจทย์ง่าย-ปานกลางหัวข้อเดียวกันที่**ยังไม่เคยออก**มาให้ฝึกใหม่

---

# 🗂️ กลุ่ม 6 — จัดการข้อมูล

## 27. `csv_roundtrip.py` — แก้คลังใน Excel
```
python tools\csv_roundtrip.py export --topic 7 --csv bank_edit.csv     ← ออกไปแก้
python tools\csv_roundtrip.py import --csv bank_edit.csv               ← นำกลับ (สำรองอัตโนมัติ)
```
⚠️ นำกลับจะอัปเดตเฉพาะ id ที่มีอยู่แล้ว ⛔ ไม่สร้างข้อใหม่ ⛔ ไม่ลบข้อ · ตัวเลือกคั่นด้วย ` ||| `

## 28. `id_registry.py` — เลข id ถัดไปของแต่ละชุด
```
python tools\id_registry.py --set alvl1-2566-03
```
บอก id ถัดไปที่ควรใช้ + เลขที่ว่างอยู่ ⇒ กันตั้งชื่อชนกัน

---

# 📌 จำไว้ 4 ข้อ

1. **ทุกตัวอ่านอย่างเดียว** ยกเว้น 3 ตัวที่เขียนไฟล์: `queue_builder.py` (คิว/DONE) · `merge_master.py` (MASTER) · และ `normalize_tex.py` / `csv_roundtrip.py` **เฉพาะเมื่อสั่ง `--write` / `import`** (สำรองไฟล์เดิมให้ทุกครั้ง)
2. ไฟล์ HTML ที่มีสูตรคณิตศาสตร์เรียกฟอนต์สูตรจากอินเทอร์เน็ต — เปิดตอนออนไลน์จะเห็นสูตรสวย
3. ทุกตัวรับ `--help` · ระบุที่อยู่ไฟล์เองได้ทุกตัว เช่น `--done "_t1run\results" "D:\ที่อื่น"`
4. ⚠️ ตัวที่ใช้การจับข้อความ (`old_vs_new` · `near_dup` · `validate_bank` ช่องอ้างรูป) ให้ผลเป็น **"รายการที่ต้องเปิดดู" ⛔ ไม่ใช่คำตัดสิน**

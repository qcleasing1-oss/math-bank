# 📋 Prompt สำหรับแชทใหม่ — rewrite เฉลย math-bank

## วิธีใช้
1. เปิดแชทใหม่ใน Claude
2. คัดลอก template ข้างล่างทั้งหมด แล้วแก้ตรง `<<<...>>>` 3 จุด:
   - `<<<ชุดที่กำลังทำ>>>` — เช่น `samn-2555-01`
   - `<<<ชุดที่ทำเสร็จแล้ว>>>` — list ที่เคยทำผ่านมา
   - `<<<ชุดถัดไป>>>` — ชุดที่จะทำตามมา
3. แนบไฟล์ตามที่ระบุท้าย prompt
4. Send

---

## 🎯 Master Template (คัดลอกตั้งแต่บรรทัดถัดไป)

```
ปรับเฉลยชุด <<<ชุดที่กำลังทำ>>> ด้วย style verbose step-by-step
(แบบเดียวกับ alvl1-2567-03 ที่ทำไปแล้ว)

# Context: math-bank rewrite-explanations project

## Style guide (apply ทุกข้อ)
- ใช้ "ขั้นที่ 1:", "ขั้นที่ 2:", "ขั้นที่ 3:" แสดงโครงสร้างชัด
- Bullet "•" อธิบายสูตร/สัญลักษณ์ทีละตัว
- ใส่เหตุผลในวงเล็บ เช่น "(คูณค่าลบ → สลับเครื่องหมาย)"
- บรรทัดสุดท้ายลงท้าย "ตอบ: ... ตรงกับ ข้อ X" (mc) หรือ "ตอบ: ค่า" (fill)
- ความยาวเฉลย 9-21 บรรทัด/ข้อ (ขึ้นกับความซับซ้อน)
- ใช้ LaTeX inline $...$ สำหรับคณิตศาสตร์
- ภาษาไทยเป็นหลัก ปนคำคณิตศาสตร์ภาษาอังกฤษได้ (chain rule, Vieta, partial fractions)

## Schema (ห้ามเปลี่ยน)
- Key order ต่อข้อ: id, setId, questionNumber, topics, subTopics, type,
  level, score, question, hasImage, [renderReady, imageNote, imageSpec],
  choices/correct, explanation
- correct ใน mc = 0-indexed (ข้อ 1 = 0)
- ห้ามเปลี่ยน hasImage / renderReady / imageNote / imageSpec — แก้เฉพาะ explanation
- ไฟล์ output ต้องเป็น JSON ที่ valid (indent=2, ensure_ascii=False)

## Roadmap ทั้งหมด (13 ชุด, จาก simple → complex)

### Phase A: วิชาสามัญ 11 ชุด (เริ่มจากที่นี่)
1. samn-2555-01  ← จุดเริ่ม
2. samn-2556-01
3. samn-2557-01
4. samn-2558-01
5. samn-2558-12
6. samn-2559-12
7. samn-2561-03
8. samn-2562-03
9. samn-2563-03
10. samn-2564-04
11. samn-2565-03

### Phase B: A-Level เก่า (1 ชุด)
12. alvl1-2566-03

### Phase C: รายบท (128 ข้อ — แบ่งหลาย batch)
13. chap-02-logic
    - Batch 1: Q1-Q44   (ข้อสอบเข้ามหาวิทยาลัย ครึ่งแรก)
    - Batch 2: Q45-Q88  (ข้อสอบเข้ามหาวิทยาลัย ครึ่งหลัง + เสริมประสบการณ์ต้น)
    - Batch 3: Q89-Q128 (เสริมประสบการณ์ที่เหลือ)

## สถานะปัจจุบัน
- ทำเสร็จแล้ว: alvl1-2567-03, <<<ชุดที่ทำเสร็จแล้ว>>>
- กำลังทำ: <<<ชุดที่กำลังทำ>>>
- ถัดไป: <<<ชุดถัดไป>>>

## Workflow ปลอดภัย (anti-crash protocol)
1. View JSON file ก่อน วิเคราะห์โครงสร้าง topic จำนวนข้อ ข้อมีรูป
2. List ข้อทั้งหมดให้ครูดู แล้วถาม confirm ก่อน rewrite (ป้องกัน scope creep)
3. ทำ rewrite ทีละ batch (15 ข้อ/batch) ใน Python script
4. Verify หลัง merge: คำตอบยังตรง, key order ไม่เปลี่ยน, JSON valid
5. Present ไฟล์ใหม่ — ครูตรวจก่อน push
6. ห้าม push เอง

## Context monitoring
- 🟢 <60%: ปกติ
- 🟡 60-80%: ใกล้เต็ม → เตรียม handover (จบ batch แล้วขึ้นแชทใหม่)
- 🔴 >80%: STOP + handover ทันที

## ไฟล์ที่แนบมา
1. <<<ชุดที่กำลังทำ>>>.json — ไฟล์ source ที่ต้อง rewrite
2. PDF เฉลยต้นฉบับ (ถ้ามี) — ไว้อ้างอิงคำตอบ
3. (optional) alvl1-2567-03.json — ตัวอย่าง style ที่ต้องทำตาม

เริ่มได้เลยครับ
```

---

## 📌 ตัวอย่างการใช้งาน

### ครั้งที่ 1 (เริ่มต้น):
```
ปรับเฉลยชุด samn-2555-01 ด้วย style verbose step-by-step
...
## สถานะปัจจุบัน
- ทำเสร็จแล้ว: alvl1-2567-03
- กำลังทำ: samn-2555-01
- ถัดไป: samn-2556-01
```
แนบ: `samn-2555-01.json`, PDF เฉลย ม.ค.55, `alvl1-2567-03.json` (ดู style)

### ครั้งที่ 5 (ทำได้ครึ่งทาง):
```
ปรับเฉลยชุด samn-2558-12 ด้วย style verbose step-by-step
...
## สถานะปัจจุบัน
- ทำเสร็จแล้ว: alvl1-2567-03, samn-2555-01, samn-2556-01, samn-2557-01, samn-2558-01
- กำลังทำ: samn-2558-12
- ถัดไป: samn-2559-12
```

### ครั้งสุดท้าย (รายบท batch 3):
```
ปรับเฉลยชุด chap-02-logic Q89-Q128 (batch 3 สุดท้าย) ด้วย style verbose step-by-step
...
## สถานะปัจจุบัน
- ทำเสร็จแล้ว: alvl1-2567-03, ทุกชุดวิชาสามัญ, alvl1-2566-03,
              chap-02-logic Q1-Q88 (batch 1, 2)
- กำลังทำ: chap-02-logic Q89-Q128 (batch 3)
- ถัดไป: เสร็จทั้งคลัง! 🎉
```

---

## 💡 Tips

**ทำไมเรียงแบบนี้:**
- **วิชาสามัญก่อน** เพราะข้อสอบ 30 ข้อ/ชุด — ขนาดพอเหมาะกับ 1 แชท ไม่ต้องแบ่ง batch
- **A-Level 2566 หลังวิชาสามัญ** เพราะ format คล้ายกัน 30 ข้อ/ชุด
- **รายบทไว้ท้าย** เพราะ 128 ข้อต้องแบ่ง 2-3 batch ต่อ 1 ชุด ใช้ context มากที่สุด

**ประหยัด context:**
- ในแชทใหม่ อย่าให้ Claude อ่าน bank.json ทั้งหมด — ให้อ่านเฉพาะ `data/sets/<setId>.json`
- ถ้า context ใกล้เต็ม (🟡) ให้จบ batch ปัจจุบัน push แล้วขึ้นแชทใหม่ต่อ
- ไม่ต้องส่ง alvl1-2567-03.json ทุกแชท — แนบเฉพาะแชทแรก ๆ ที่ Claude ต้องเรียน style

**ถ้า Claude สับสน:**
- ส่ง screenshot Q1 จาก admin viewer ที่ render ออกมาแล้ว — เห็นทั้ง style ใหม่ (alvl1-2567-03) และเก่า (ชุดที่ยังไม่ rewrite) ครูจะเทียบให้ดูได้

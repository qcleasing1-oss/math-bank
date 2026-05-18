# 📥 Prompt สำหรับแชทใหม่ — INGEST ชุดข้อสอบใหม่เข้า math-bank

> **ต่างจาก rewrite!** ไฟล์นี้ใช้เมื่อต้องการ**เพิ่มชุดใหม่**ที่ยังไม่มีในคลัง
> (สร้างไฟล์ JSON ใหม่จาก PDF + อัปเดต manifest)

## เมื่อไหร่ใช้ template ไหน

| สถานการณ์ | ใช้ template |
|---|---|
| ปรับเฉลยชุดที่มีอยู่ในคลังแล้ว | `handover-prompt-template.md` |
| เพิ่มชุดข้อสอบใหม่ที่ยังไม่มี | `ingest-prompt-template.md` (ไฟล์นี้) |

---

## วิธีใช้
1. เปิดแชทใหม่ใน Claude
2. คัดลอก template ข้างล่าง แก้ตรง `<<<...>>>` ตามที่ต้องการ
3. แนบ PDF ข้อสอบ + เฉลย, manifest.json อันล่าสุด, และ alvl1-2567-03.json (เป็นตัวอย่าง schema)
4. Send

---

## 🎯 Master Template (คัดลอกตั้งแต่บรรทัดถัดไป)

```
ingest ชุดข้อสอบใหม่: <<<setId>>>

# Context: math-bank ingest project

## ข้อมูลชุดใหม่
- setId: <<<setId>>>             (เช่น samn-2560-03, alvl1-2568-03, chap-01-set)
- source: <<<แหล่ง>>>             (เช่น วิชาสามัญ, A-Level, ข้อสอบรายบท)
- subject: <<<วิชา>>>             (เช่น คณิตศาสตร์, คณิตศาสตร์ประยุกต์ 1)
- year: <<<พ.ศ.>>>                (เช่น 2560)
- month: <<<เดือน>>>              (เช่น 3)
- examDate: <<<วันที่สอบเต็ม>>>     (เช่น วันอาทิตย์ที่ 15 มีนาคม 2560 เวลา 8.30-10.00 น.)
- totalQuestions: <<<จำนวนข้อ>>>   (30 สำหรับวิชาสามัญ/A-Level, อาจมากกว่าสำหรับรายบท)
- totalScore: <<<คะแนนรวม>>>      (100 สำหรับวิชาสามัญ/A-Level)
- structure:
    part1: <<<โครงสร้างตอน 1>>>    (เช่น แบบปรนัย 5 ตัวเลือก 25 ข้อ ข้อละ 3 คะแนน)
    part2: <<<โครงสร้างตอน 2>>>    (เช่น แบบระบายตัวเลข 5 ข้อ ข้อละ 5 คะแนน)

## งานที่ต้องทำ
1. อ่าน PDF ข้อสอบ extract: โจทย์ + ตัวเลือก + เฉลย + เลขข้อ
2. วิเคราะห์ topic แต่ละข้อ → topicDistribution
3. ระบุข้อที่มีรูป (hasImage:true, renderReady:false)
4. เขียน explanation แบบ verbose step-by-step (ดู style ด้านล่าง)
5. สร้าง <<<setId>>>.json (schema v3)
6. อัปเดต manifest.json (เพิ่ม entry, ใส่ตามลำดับเวลา)
7. Verify: คำตอบตรง PDF, topicDistribution sum = totalQuestions, key order ถูก
8. Present 2 ไฟล์ (JSON + manifest) — รอครู push ไม่ push เอง

## Style เฉลย (verbose step-by-step)
- ใช้ "ขั้นที่ 1:", "ขั้นที่ 2:", "ขั้นที่ 3:" แสดงโครงสร้างชัด
- Bullet "•" อธิบายสูตร/สัญลักษณ์ทีละตัว
- ใส่เหตุผลในวงเล็บ เช่น "(คูณค่าลบ → สลับเครื่องหมาย)"
- บรรทัดสุดท้าย: "ตอบ: ... ตรงกับ ข้อ X" (mc) หรือ "ตอบ: ค่า" (fill)
- ความยาวเฉลย 9-21 บรรทัด/ข้อ
- LaTeX inline $...$ สำหรับคณิตศาสตร์
- ภาษาไทยเป็นหลัก ปนคำคณิตศาสตร์ภาษาอังกฤษได้

## Schema v3 (ห้ามเปลี่ยน)
ระดับชุด (manifest.json sets[setId]):
  source, subject, year, month, examDate, totalQuestions, totalScore,
  structure {part1, part2}, topicDistribution {topicId: count}

ระดับข้อ (questions array):
  id (format: "setId-qNN"),
  setId, questionNumber, topics (list of strings), subTopics (list, อาจว่าง),
  type ("mc" หรือ "fill"), level ("easy"|"medium"|"hard"),
  score (3 หรือ 5 หรือตามโครงสร้าง),
  question (string with LaTeX),
  hasImage (boolean),
  [renderReady (boolean, ถ้า hasImage:true)],
  [imageNote (string, อธิบายรูปคำพูด)],
  [imageSpec (object, ถ้ามี renderer)],
  choices (list of 5 strings, ถ้า type:mc),
  correct (0-indexed สำหรับ mc, หรือค่าตัวเลขสำหรับ fill),
  [accept (list, ถ้า fill มีหลายคำตอบที่รับ)],
  explanation (list of strings, แต่ละ string = 1 บรรทัดในเฉลย)

## Topic mapping (จาก manifest.json topicNames)
1: เซต           2: ตรรกศาสตร์         3: จำนวนจริง
4: เรขาคณิตวิเคราะห์    5: ความสัมพันธ์และฟังก์ชัน    6: เมทริกซ์
7: ตรีโกณมิติ       8: เลขยกกำลังและลอการิทึม    9: เวกเตอร์ในสามมิติ
10: จำนวนเชิงซ้อน   11: ลำดับและอนุกรม           12: หลักการนับและความน่าจะเป็น
13: แคลคูลัส        14: ลำดับและอนุกรมอนันต์      15: สถิติ
16: กำหนดการเชิงเส้น  17: ทฤษฎีจำนวน

## File location ใน repo
- data/sets/<<<setId>>>.json (ไฟล์ใหม่)
- data/manifest.json (อัปเดต)
- GH Actions Phase F.4 จะ rebuild bank.json อัตโนมัติหลัง push

## Anti-crash protocol
1. View PDF ทั้งหมด + JSON template (alvl1-2567-03.json) ก่อน
2. List แผน topic distribution + ข้อมีรูป ให้ครู confirm ก่อน
3. สร้าง Python script ที่ build JSON ทั้งไฟล์ (ป้องกัน JSON syntax error)
4. Run + verify (เช็คคำตอบ + key order + topic sum)
5. Present 2 ไฟล์ — ห้าม push เอง

## Context monitoring
- 🟢 <60%: ปกติ
- 🟡 60-80%: ใกล้เต็ม
- 🔴 >80%: หยุด + handover

## ไฟล์ที่แนบ
1. PDF ข้อสอบ + เฉลยต้นฉบับ
2. manifest.json (อันล่าสุด หลังทำชุดก่อนหน้าเสร็จ)
3. alvl1-2567-03.json (template ตัวอย่าง schema + style ใหม่)

เริ่มได้เลยครับ
```

---

## 📌 ตัวอย่างการใช้งาน 3 สถานการณ์

### สถานการณ์ 1: ingest A-Level ใหม่ (ออกข้อสอบรายปี)
```
ingest ชุดข้อสอบใหม่: alvl1-2568-03

## ข้อมูลชุดใหม่
- setId: alvl1-2568-03
- source: A-Level
- subject: คณิตศาสตร์ประยุกต์ 1
- year: 2568
- month: 3
- examDate: วันอาทิตย์ที่ 16 มีนาคม 2568 เวลา 8.30-10.00 น.
- totalQuestions: 30
- totalScore: 100
- structure:
    part1: แบบปรนัย 5 ตัวเลือก เลือก 1 คำตอบที่ถูกที่สุด จำนวน 25 ข้อ ข้อละ 3 คะแนน รวม 75 คะแนน
    part2: แบบระบายตัวเลขที่เป็นคำตอบ จำนวน 5 ข้อ ข้อละ 5 คะแนน รวม 25 คะแนน
```
แนบ: PDF ข้อสอบ A-Level 68, manifest.json, alvl1-2567-03.json

---

### สถานการณ์ 2: ingest บทใหม่ในรายบท (เช่น เซต)
```
ingest ชุดข้อสอบใหม่: chap-01-set

## ข้อมูลชุดใหม่
- setId: chap-01-set
- source: ข้อสอบรายบท
- subject: เซต
- totalQuestions: <<<นับจากที่รวบรวมได้>>>
- totalScore: <<<= totalQuestions ถ้าข้อละ 1 คะแนน>>>
- structure:
    part1: ข้อสอบเข้ามหาวิทยาลัย (Q1-QX), เสริมประสบการณ์ (QY-Qสุดท้าย) — ทุกข้อจัดอยู่ในบทเซต
- ไม่ต้องใส่ topicDistribution ปกติ เพราะทุกข้อเป็น topic เดียว: {"1": <จำนวนข้อ>}
```
แนบ: รวมข้อสอบรายบทเซต (PDF), manifest.json, chap-02-logic.json (template เพราะ structure คล้ายกัน)

**บทที่น่าจะ ingest ต่อ** (เรียงตามลำดับบท):
- chap-01-set (เซต)
- chap-03-real-number (จำนวนจริง)
- chap-04-analytic-geometry (เรขาคณิตวิเคราะห์)
- chap-05-relation-function (ความสัมพันธ์และฟังก์ชัน)
- chap-06-matrix (เมทริกซ์)
- chap-07-trigonometry (ตรีโกณมิติ)
- chap-08-exponential-logarithm (เลขยกกำลังและลอการิทึม)
- chap-09-vector-3d (เวกเตอร์ในสามมิติ)
- chap-10-complex (จำนวนเชิงซ้อน)
- chap-11-sequence (ลำดับและอนุกรม)
- chap-12-counting-probability (หลักการนับและความน่าจะเป็น)
- chap-13-calculus (แคลคูลัส)
- chap-14-infinite-sequence (ลำดับและอนุกรมอนันต์)
- chap-15-statistics (สถิติ)

⚠️ **บทใหญ่ๆ (เช่น แคลคูลัส, สถิติ) อาจต้องแบ่ง 2-3 batch** เหมือน chap-02-logic

---

### สถานการณ์ 3: ingest ข้อสอบประเภทใหม่ (เช่น สสวท., สอวน., O-NET, PAT 1)
```
ingest ชุดข้อสอบใหม่: pat1-2566-10

## ข้อมูลชุดใหม่
- setId: pat1-2566-10
- source: PAT 1
- subject: ความถนัดทางคณิตศาสตร์
- year: 2566
- month: 10
- examDate: ...
- totalQuestions: 45      (PAT 1 มี 45 ข้อ)
- totalScore: 300         (ข้อละ ~6.67 คะแนน)
- structure: ...
```

**ก่อนทำต้องเพิ่ม source ใหม่ใน convention:**
- prefix ใหม่ เช่น `pat1-` (PAT 1), `onet-` (O-NET), `sw-` (สสวท.), `posn-` (สอวน.)
- ไม่ต้องเพิ่ม field ใหม่ใน schema — แค่ใช้ source string ใหม่

---

## 💡 Tips สำหรับ ingest

### ลำดับชุดใหม่ที่แนะนำ (หลัง rewrite 13 ชุดเสร็จ)
**Phase D: ชุดที่ขาดในวิชาสามัญ/A-Level**
- alvl1-2568-03 (A-Level มี.ค. 68)
- alvl1-2569-03 (A-Level มี.ค. 69 — ถ้าออกแล้ว)
- samn-2560-03 (วิชาสามัญ มี.ค. 60 — ถ้าจัดสอบ)

**Phase E: รายบทที่เหลือ 14 บท** (ไล่ตามเลข chap-01 → chap-15 ยกเว้น chap-02 ที่ทำแล้ว)
- เริ่มจากบทพื้นฐาน: เซต → จำนวนจริง → ฟังก์ชัน
- ตามด้วยบทหลัก: ตรีโกณ → log/exp → vector → calculus
- จบที่บทยาก: สถิติ → ความน่าจะเป็น

**Phase F: ข้อสอบประเภทใหม่ (optional)**
- PAT 1, O-NET, สสวท., สอวน. — ถ้าครูสนใจขยาย

### ก่อน ingest ทุกครั้ง — ตรวจ manifest
ก่อนคัดลอก template ครูเปิด `manifest.json` ปัจจุบันก่อน เช็คว่า:
- ✅ setId ที่จะ ingest ยังไม่มีในคลัง
- ✅ examDate ไม่ซ้ำกับ set อื่น
- ✅ source string สอดคล้องกับ convention เดิม

### ประหยัด context (สำคัญ!)
- **อย่าแนบ bank.json** (793 KB — กิน context มหาศาล)
- แนบเฉพาะ manifest.json + ไฟล์ JSON template 1 ไฟล์ (alvl1-2567-03.json)
- PDF ใหญ่ก็ OK Claude อ่านได้

### ถ้าข้อสอบยาว 50+ ข้อ
- แบ่งเป็น batch (Q1-25, Q26-50)
- ใช้สมการ "สถานะปัจจุบัน" ใน prompt เพื่อ resume

---

## 🗺️ Roadmap ทั้งหมดของ math-bank (ภาพรวม)

```
✅ Phase 0 (เสร็จแล้ว): ingest 14 ชุดเริ่มต้น + alvl1-2567-03
🔄 Phase 1 (กำลังทำ): rewrite เฉลย 13 ชุดเก่า → ใช้ handover-prompt-template.md
🆕 Phase 2 (ต่อไป): ingest ชุดใหม่ → ใช้ ingest-prompt-template.md (ไฟล์นี้)
       Phase D: A-Level ใหม่ๆ + ปีที่ขาด
       Phase E: รายบท 14 บท
       Phase F: ข้อสอบประเภทอื่น (PAT, O-NET, ...) — optional
🎨 Phase 3 (แยก): พัฒนา image renderer สำหรับข้อที่ renderReady:false
       (Venn 3 เซ็ต, function-plot ใหม่ๆ, ฯลฯ)
```

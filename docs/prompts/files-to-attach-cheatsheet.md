# 📎 Cheatsheet: ไฟล์ที่ต้องแนบในแชทใหม่

> ใช้สรุปนี้ก่อนกด Send ทุกครั้ง — แนบผิดทำให้ Claude ใช้ context เปลือง

---

## 🔄 Scenario A: REWRITE เฉลย (ชุดมีในคลังแล้ว)

### ✅ ต้องแนบ (3 ไฟล์)

| # | ไฟล์ | หาจากไหน | หมายเหตุ |
|---|---|---|---|
| 1 | **`<setId>.json`** | `math-bank/data/sets/<setId>.json` | ไฟล์ที่จะ rewrite (เช่น `samn-2555-01.json`) |
| 2 | **`handover-prompt-template.md`** | ที่ครูเซฟไว้ | บอก Claude workflow ทั้งหมด |
| 3 | **PDF เฉลยต้นฉบับ** | แหล่งดาวน์โหลดเดิม | ให้ Claude verify คำตอบ + ดูแนวเฉลยที่ครู math center ทำไว้ |

### 💡 ทำไมต้อง PDF
JSON มีแค่ explanation สั้นๆ Claude ไม่เห็นแนวคิดต้นฉบับ ถ้าไม่มี PDF → Claude rewrite ตาม explanation เดิมเท่านั้น ซึ่งสั้นไป

### ❌ ห้ามแนบ
- `bank.json` (793 KB — กิน context ~30% ทันที!)
- `alvl1-2567-03.json` (ไม่จำเป็น เพราะ template มี style guide แล้ว)
- JSON ของ set อื่นที่ไม่เกี่ยว

---

## 📥 Scenario B: INGEST ชุดใหม่ (เพิ่มชุดที่ยังไม่มี)

### ✅ ต้องแนบ (4 ไฟล์)

| # | ไฟล์ | หาจากไหน | หมายเหตุ |
|---|---|---|---|
| 1 | **PDF ข้อสอบ + เฉลย** | แหล่งดาวน์โหลดเดิม | source หลักของข้อมูล |
| 2 | **`manifest.json`** | `math-bank/data/manifest.json` (อันล่าสุด) | ต้องอัปเดตเพิ่ม entry |
| 3 | **`ingest-prompt-template.md`** | ที่ครูเซฟไว้ | บอก Claude workflow |
| 4 | **`alvl1-2567-03.json`** | `math-bank/data/sets/alvl1-2567-03.json` | template schema + style |

### 💡 ถ้า ingest รายบท (เช่น chap-01-set)
แนบ `chap-02-logic.json` แทน `alvl1-2567-03.json` (structure คล้ายกัน — มี part1 เดียว, ทุกข้อ topic เดียว)

### ❌ ห้ามแนบ
- `bank.json` (กิน context)
- JSON ของ set ที่ไม่เกี่ยว
- ไฟล์รูปภาพแยก (Claude อ่านได้จาก PDF อยู่แล้ว)

---

## 📊 เปรียบเทียบ 2 scenarios

| ประเด็น | Rewrite | Ingest |
|---|---|---|
| ผลลัพธ์ | แก้ไฟล์เดิม (1 ไฟล์) | สร้างไฟล์ใหม่ + อัปเดต manifest (2 ไฟล์) |
| ต้องการ PDF? | ✅ (verify เฉลย) | ✅✅ (essential — เป็น source หลัก) |
| ต้องการ manifest.json? | ❌ ไม่ต้อง | ✅ ต้อง (จะอัปเดต) |
| ต้องการ alvl1-2567-03.json? | ❌ ไม่ต้อง | ✅ ต้อง (เป็น template) |
| Context start | ~25-30% | ~35-40% (PDF + manifest กิน) |

---

## 🚨 Tips สำคัญ

### ก่อนกด Send ทุกครั้ง — checklist
- [ ] ตรวจขนาดไฟล์ JSON ที่จะแนบ ไม่เกิน 200 KB
  - ถ้าเกิน อาจเป็น bank.json ที่ติดมา → เอาออก
- [ ] ตรวจว่ามีกี่ไฟล์ที่แนบ — Rewrite: 3 ไฟล์ / Ingest: 4 ไฟล์
- [ ] template `.md` ใส่ครบ — Claude ต้องใช้บอกตัวเองว่าทำอะไร

### ถ้าลืมแนบไฟล์
- Claude จะถามครูเอง — ไม่ต้องกังวล
- แต่จะเสียเวลา 1 turn

### PDF ขนาดใหญ่
- PDF เฉลย 10-30 หน้า OK ปกติ
- PDF >50 หน้า อาจกิน context มาก → ขอ Claude อ่านเฉพาะหน้าที่ต้องการ

### หา manifest.json ล่าสุด
- ดึงจาก GitHub repo `data/manifest.json` (commit ล่าสุด)
- ไม่ใช่ตัวที่ Claude สร้างให้ในแชทเก่า (ถ้ามีการ push หลายครั้ง อาจไม่ใช่ตัวล่าสุด)

---

## 🎯 ตัวอย่างจริง

### ตัวอย่าง 1: Rewrite samn-2555-01
**แนบ:**
- `samn-2555-01.json` (จาก math-bank repo)
- `handover-prompt-template.md`
- `วิชาสามัญ_คณิต_มกราคม2555.pdf`

**ข้อความในแชท:**
> ปรับเฉลยชุด samn-2555-01 ตาม template ที่แนบมา

(Claude จะอ่าน .md เอง ไม่ต้องคัดลอกเต็มๆ)

---

### ตัวอย่าง 2: Ingest alvl1-2568-03
**แนบ:**
- `ALevel1_มีนาคม_2568.pdf`
- `manifest.json` (จาก math-bank repo, commit ล่าสุด)
- `ingest-prompt-template.md`
- `alvl1-2567-03.json` (จาก math-bank repo)

**ข้อความในแชท:**
> ingest ชุดใหม่ alvl1-2568-03 ตาม template ที่แนบมา

---

### ตัวอย่าง 3: Ingest chap-03-real-number (รายบท)
**แนบ:**
- PDF รวมข้อสอบบทจำนวนจริง
- `manifest.json`
- `ingest-prompt-template.md`
- `chap-02-logic.json` ← template สำหรับรายบท (ไม่ใช่ alvl1-2567-03)

**ข้อความในแชท:**
> ingest ชุดใหม่ chap-03-real-number ตาม template ที่แนบ
> ใช้ chap-02-logic.json เป็น schema template (เพราะ structure รายบทเหมือนกัน)

---

## 📁 สรุปไฟล์ที่ครูควรเก็บไว้ที่เครื่อง

ในโฟลเดอร์เดียวกัน เก็บไว้เปิดเร็ว:
```
math-bank-prompts/
├── handover-prompt-template.md       (rewrite workflow)
├── ingest-prompt-template.md         (ingest workflow)
└── files-to-attach-cheatsheet.md     (ไฟล์นี้)
```

ส่วนไฟล์อื่นๆ ดึงจาก GitHub repo ตอนต้องใช้:
- JSON ของ set ที่จะทำ
- manifest.json ล่าสุด
- alvl1-2567-03.json หรือ chap-02-logic.json (เป็น template)
- PDF จากแหล่งดาวน์โหลดเดิม

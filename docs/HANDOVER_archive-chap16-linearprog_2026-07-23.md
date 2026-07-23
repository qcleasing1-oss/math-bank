# 🗂️ HANDOVER — Archive บท กำหนดการเชิงเส้น (`chap-16-linearprog`)

**วันที่:** 23 ก.ค. 2569 · **ผู้ทำ:** E-lane (Cowork) · **สถานะ:** เสร็จ + verify ผ่านทุกข้อ · **พร้อม commit/push**

> **TL;DR** — กำหนดการเชิงเส้น ไม่อยู่ในหลักสูตรปัจจุบันแล้ว (มติครู) → archive **เฉพาะบทเฉพาะ** `chap-16-linearprog` (45 ข้อ) ออกจากคลัง · คำถาม LP ที่ปนอยู่ในชุด **PAT1 เก่า (21 ข้อ) คงไว้** เป็นบันทึกประวัติศาสตร์

---

## 1 · ขอบเขต (สำคัญ — ไม่ใช่ลบ LP ทั้งหมด)

| รายการ | การจัดการ | จำนวน |
|---|---|---|
| set `chap-16-linearprog` (บทเฉพาะ) | **ย้ายเข้า `data/_archive/`** | 45 ข้อ |
| คำถาม `topic 16` ในชุด PAT1 (2552–2563) | **คงไว้** | 21 ข้อ |
| `topicNames["16"] = "กำหนดการเชิงเส้น"` (manifest) | **คงไว้** | — |

**ทำไมคง `topicNames["16"]`:** ข้อ LP ใน PAT1 ที่เก็บไว้ยังอ้าง topic 16 อยู่ — ถ้าลบชื่อ topic ข้อพวกนี้จะ render พัง

---

## 2 · ไฟล์ที่เปลี่ยน (git)

```
M  data/manifest.json                 ลบ key "chap-16-linearprog" ออกจาก sets (−28 บรรทัด) · topicNames คงเดิม
M  data/bank.json                     rebuild ใหม่ (−45 ข้อ · 5548 → 5503)
D  data/sets/chap-16-linearprog.json  ย้ายออก (ไป _archive/)
?? data/_archive/                     ใหม่: ไฟล์บท + manifest สำรอง + RESTORE-NOTE
```

diff รวม: **ลบล้วน 7,998 บรรทัด · เพิ่ม 0** — เป็น archive ล้วน ไม่มีการแก้เนื้อโจทย์ใดๆ

---

## 3 · วิธีที่ทำ (reproducible — ไม่แก้ไฟล์ที่ถูก generate ด้วยมือ)

1. ลบ key `chap-16-linearprog` จาก `manifest['sets']` (Python `load → del → dump`, format เดิม `ensure_ascii=False, indent=2`)
2. `mv data/sets/chap-16-linearprog.json data/_archive/`
3. `python scripts/build_bank.py` → regenerate `bank.json` (exit 0)

> ⚠️ `bank.json` เป็นไฟล์ **generate** — ห้ามแก้มือ · แก้ที่ `manifest`/`sets` แล้ว rebuild เท่านั้น (ตามที่ `build_bank.py` ออกแบบ)

---

## 4 · ผลตรวจ (verify)

| ตรวจ | คาดหวัง | ผล |
|---|---|---|
| total questions | 5503 | ✅ 5503 |
| `chap-16-linearprog` ใน `bank.sets` | ไม่มี | ✅ False |
| ข้อ id ขึ้นต้น `chap-16-linearprog` | 0 | ✅ 0 |
| `topic-16` คงเหลือ (PAT1 ล้วน) | 21 | ✅ 21 |
| `topicNames["16"]` | คงอยู่ | ✅ กำหนดการเชิงเส้น |
| hardcode ใน `admin.html` / `export.js` | 0 | ✅ 0 |
| `bank.json` valid JSON | valid | ✅ |

viewer (`admin.html`) โหลดจาก `manifest.json` + `sets/{id}.json` → จะไม่ลิสต์ chap-16 อีก และไม่ fetch ไฟล์ที่หาย

---

## 5 · วิธีกู้คืน (ถ้าหลักสูตรเปลี่ยนอีก)

ละเอียดใน `data/_archive/RESTORE-NOTE_chap-16-linearprog.md` — ย่อ:

1. `mv data/_archive/chap-16-linearprog.json data/sets/`
2. เพิ่ม key `"chap-16-linearprog"` กลับใน `data/manifest.json → sets` (คัดบล็อกจาก manifest สำรองใน `_archive/`)
3. `python scripts/build_bank.py`

---

## 6 · หมายเหตุ / ค้าง

- **ข้อความค้าง 1 จุดใน manifest (ไม่กระทบ):** ชุดสถิติมี `note` อ้างชื่อ "chap-16-linearprog" เป็นตัวอย่าง convention การวาง `[IMAGE]` marker — เป็นข้อความล้วน ปล่อยไว้เป็นบันทึกประวัติ
- **skill แต่งข้อสอบ** (`math-question-authoring`) ยังลิสต์ 18 บท รวมกำหนดการเชิงเส้น — แก้ที่ **Settings › Capabilities** (แก้ในโค้ด repo ไม่ได้)
- **commit:** พร้อม push ผ่าน GitHub Desktop · ตอน push GitHub Actions จะ rebuild `bank.json` ได้ผลเดียวกัน (idempotent ไม่ drift)
- **ฝั่งพอร์ทัล/แผน (คนละ repo):** ROADMAP · SPEC-IDEA · QUEUE · TOOLS อัปเดตเป็น **17 บท** แล้ว (🟢7 · 🟡6 · 🔴4)

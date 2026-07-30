# patch: build_bank.py — ประทับเวลา export อัตโนมัติ + ส่งต่อ subTopicNames

**วันที่:** 30 ก.ค. 2569 (แก้ไขรอบ 2) · **ตอบข้อ ② และ ③ ของทีมพอร์ทัล** · **มติครู: อนุมัติข้อ ②**

> **⚠️ ZIP นี้แทนที่ `build_bank-stamp-patch.zip` ตัวก่อนหน้า** — ถ้ายังไม่ push ตัวเก่า ให้ใช้ตัวนี้แทนเลย
> ถ้า push ตัวเก่าไปแล้ว ให้แตกตัวนี้ทับ (ไฟล์เดียวกัน) แล้ว push อีกครั้ง

## วิธีติดตั้ง
แตก ZIP ทับที่ราก repo `math-bank` — ไฟล์เดียวคือ `scripts/build_bank.py`
แล้ว push ผ่าน GitHub Desktop ตามปกติ

## จะเกิดอะไรขึ้นหลัง push
`scripts/build_bank.py` อยู่ใน trigger path ของ `.github/workflows/build-bank.yml`
⇒ CI จะ rebuild `data/bank.json` ให้เองทันที · **ห้าม commit `bank.json` เอง**
⇒ commit แรกจะมี diff ใหญ่ครั้งเดียว เพราะ bank.json ได้คีย์ใหม่ 9 ตัว หลังจากนั้นจะนิ่ง

## สิ่งที่เปลี่ยน

### รอบ 1 — ด่านเช็คความสด (ข้อ ② ของพอร์ทัล)
| ฟิลด์ | ก่อน | หลัง |
|---|---|---|
| `exported` | คัดจาก `manifest['exported']` ⇒ ค้างที่ 2026-06-23 | เวลาที่เนื้อหาเปลี่ยนครั้งล่าสุด (UTC) |
| `manifestExported` | — | ค่าเดิมจาก manifest (เก็บไว้ ไม่ทิ้ง) |
| `questionCount` | — | จำนวนข้อทั้งหมด |
| `activeCount` | — | จำนวนข้อที่ไม่ retired |
| `retiredCount` | — | จำนวนข้อที่ retired |
| `builtFromCommit` | — | `GITHUB_SHA` หรือ `"local"` |

### รอบ 2 — ชื่อหัวข้อย่อย (ข้อ ③ ของพอร์ทัล)
| ฟิลด์ | ก่อน | หลัง |
|---|---|---|
| `subTopicNames` | **ไม่มีใน bank.json** (มีแต่ใน manifest) | dict `รหัส → ชื่อไทย` · 194 รหัส |
| `deprecatedSubTopics` | **ไม่มีใน bank.json** | list 7 รหัส (`12.12` + `16.1`–`16.6`) |
| `subTopicCount` | — | 194 |
| `liveSubTopicCount` | — | 187 (194 − deprecated) |

**ทำไมต้องมี:** ฝั่งพอร์ทัลอ่าน `bank.json` ไฟล์เดียว เมื่อไม่มี `subTopicNames`
census ของพอร์ทัลจึงแสดงชื่อหัวข้อเป็น `—` ทุกรหัส **และนับรหัสที่ยังไม่มีข้อเลยไม่ได้**
(รหัสที่ไม่ปรากฏใน `questions` จะหายไปจากการนับ — วัดแล้วต่างกัน **3 รหัสพอดี**:
พอร์ทัลนับได้ 184 รหัส / ควรเป็น 187)

**ไม่มีการคำนวณใหม่** — ทั้งสี่ฟิลด์คัดจาก `manifest.json` ตรง ๆ ⇒ manifest ยังเป็น
แหล่งความจริงเดียว · ถ้า manifest ไม่มีฟิลด์นี้ จะได้ค่าว่างพร้อมคำเตือน ไม่ทำให้ build ล้ม

คีย์เดิม 5 ตัวคงลำดับเดิมทุกตัว · คีย์ใหม่แทรกระหว่าง `exported` กับ `sets`
ลำดับคีย์สุดท้ายของ `bank.json`:

```
schemaVersion · exported · manifestExported · questionCount · activeCount ·
retiredCount · subTopicCount · liveSubTopicCount · builtFromCommit ·
topicNames · subTopicNames · deprecatedSubTopics · sets · questions
```

## พฤติกรรมการเขียนไฟล์
ค่าตั้งต้น: เขียนเฉพาะเมื่อ **เนื้อหา** เปลี่ยนจริง (เทียบโดยตัด `exported`/`builtFromCommit` ออก)
⇒ ไม่มี diff เปล่าทุกครั้งที่ CI รัน · ถ้าต้องการประทับเวลาทุกครั้ง ใช้ `--stamp-always`

> **หมายเหตุที่ต้องให้ครูเคาะ:** ของเดิมที่บรรทัด 100–109 มีด่าน "ไม่เขียนถ้าไม่เปลี่ยน" อยู่แล้ว
> แพตช์นี้จึง**รักษาพฤติกรรมนั้นไว้เป็นค่าตั้งต้น** (ตัวเลือก B) ไม่ใช่ตัวเลือก A ที่เคยเสนอ
> เพราะตัวเลือก A จะทำลายด่านเดิมโดยไม่ตั้งใจ · ถ้าครูอยากได้ A ให้เติม `--stamp-always` ใน workflow

## ผลทดสอบ (รันครบ 6 รอบก่อนส่ง)
| รอบ | สิ่งที่ทดสอบ | ผล |
|---|---|---|
| 1 | build สด ไม่มี bank.json เดิม | ✅ 62 sets · 6,308 ข้อ · active 6,283 / retired 25 · 194 รหัส (ใช้จริง 187) |
| 2 | รันซ้ำ เนื้อหาไม่เปลี่ยน | ✅ ไม่เขียนไฟล์ · byte-identical · `exported` คงเดิม |
| 3 | แก้ `notes` ของ 1 ข้อ | ✅ เขียนไฟล์ · `exported` ขยับ |
| 4 | `--stamp-always` โดยเนื้อหาไม่เปลี่ยน | ✅ `exported` ขยับ · `questions` เหมือนเดิมทุกข้อ |
| 5 | manifest ที่**ไม่มี** `subTopicNames` (repo เก่า) | ✅ build ผ่าน · ได้ `{}` + คำเตือน · `GITHUB_SHA` ถูกอ่าน |
| 6 | round-trip format | ✅ `json.dumps(..., ensure_ascii=False, indent=2)` byte-identical · ไม่มี BOM · ไม่มี newline ท้ายไฟล์ (เหมือนเดิม) |

## ทดสอบก่อน push ได้ (ไม่แตะของจริง)
```
cp -r data /tmp/t && python scripts/build_bank.py /tmp/t
```

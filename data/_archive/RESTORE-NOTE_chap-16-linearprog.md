# Archive: chap-16-linearprog (กำหนดการเชิงเส้น)

**วันที่:** 23 ก.ค. 2569
**เหตุผล:** กำหนดการเชิงเส้น ไม่อยู่ในหลักสูตรปัจจุบันแล้ว (มติครู)
**ขอบเขต:** archive เฉพาะบทเฉพาะ (setId `chap-16-linearprog`, 45 ข้อ)
คำถาม LP ที่ปนอยู่ในชุด PAT1 เก่า (topic 16, ~21 ข้อ) = **คงไว้** (บันทึกประวัติศาสตร์)
`topicNames["16"] = "กำหนดการเชิงเส้น"` ใน manifest = **คงไว้** (ข้อ PAT1 ยังอ้างถึง)

## ไฟล์ในโฟลเดอร์นี้
- `chap-16-linearprog.json` — บทเฉพาะที่ย้ายออกมา (45 ข้อ)
- `manifest_before-chap16-archive_20260723.json` — manifest ก่อนแก้ (สำรอง)

## วิธีกู้คืน (ถ้าหลักสูตรเปลี่ยนอีก)
1. `mv data/_archive/chap-16-linearprog.json data/sets/`
2. เพิ่ม key `"chap-16-linearprog"` กลับใน `data/manifest.json` → `sets`
   (คัดลอกบล็อกจาก `manifest_before-chap16-archive_20260723.json`)
3. `python scripts/build_bank.py` → rebuild bank.json

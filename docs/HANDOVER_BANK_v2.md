# 📋 HANDOVER — Project คลังข้อสอบ (BANK) v2

> **เขียนเมื่อ:** 15 พฤษภาคม 2569 (2026-05-15)
> **เขียนโดย:** Claude (แชท Phase B)
> **สำหรับ:** Claude คนถัดไปที่จะ work ใน project นี้
> **คุณครู:** คุณครูOFF (ครูคณิต ม.ปลาย)
> **Supersedes:** `HANDOVER_BANK_v1.md`

---

## 🚀 TL;DR — เริ่มอ่าน 30 วินาทีนี้ก่อน

**Project คลังข้อสอบ "math-bank"** = single source of truth สำหรับข้อสอบคณิตศาสตร์ ม.ปลาย (วิชาสามัญ + อนาคต PAT1)

- ✅ **Phase A + B + C เสร็จสมบูรณ์** — folder structure, admin viewer **พร้อม renderer**, GitHub repo, GitHub Pages deploy
- ⏳ **Phase D รอทำ (NEXT)** — เพิ่ม imageSpec ให้ set ที่เหลือ (samn-2562 ลงไป + chap-02-logic)
- 🔮 **Phase E (optional)** — เพิ่ม renderer types อื่น ๆ เมื่อมีข้อที่ต้องการ (ztable, polygon, unit-circle, stacked-bar, venn)

**Repo + URLs:**
```
GitHub repo:    https://github.com/qcleasing1-oss/math-bank
Admin viewer:   https://qcleasing1-oss.github.io/math-bank/viewer/admin.html  (รหัส: teacher2026)
Bank JSON:      https://qcleasing1-oss.github.io/math-bank/data/bank.json
```

---

## 👤 User Profile — คุณครูOFF

- 🎓 ครูคณิตศาสตร์ ม.ปลาย ในประเทศไทย — ใช้ภาษาไทยเป็นหลัก
- 💻 ใช้ **Windows + Python 3.12** บนไดรฟ์ A:
- 🔧 ระดับเทคนิค: **มือใหม่** ด้านโค้ดและ GitHub แต่ตอนนี้ใช้ GitHub Desktop ได้คล่อง + เริ่มแก้ infra-level issue ได้เอง (port, file://, hard refresh)
- 🐌 ชอบ workflow ที่ค่อยๆ ทีละขั้น + screenshot verify ก่อน irreversible action
- ⚠️ **ห้าม assume ว่าคุณครูรู้คำสั่ง shell หรือ git syntax** — เขียน step-by-step พร้อมคำอธิบายเสมอ
- ✨ **คุณครูตอบเร็วและพร้อม collaborate** — screenshot ส่งทันที, ทำตาม instruction ได้ดี

**Local path บนเครื่องคุณครู:**
```
A:\โปรเจคสอนคณิตศาสตร์\math-bank\
├── data\bank.json
├── viewer\
│   ├── admin.html      ← มี renderer integration แล้ว (Phase B)
│   └── renderers.js    ← NEW (Phase B) — SVG renderers, port จาก portal
├── docs\
│   ├── HANDOVER_BANK_v1.md  ← เก่า
│   └── HANDOVER_BANK_v2.md  ← ไฟล์นี้
├── .gitattributes
└── README.md
```

**GitHub Desktop:**
- Account: **`qcleasing1-oss`**
- Repo เปิดอยู่: **math-bank** (Public)
- Workflow: เห็น diff → ใส่ summary → Commit to main → Push origin → รอ 1 นาที → live

---

## 📊 Bank Schema (สำคัญที่สุด — อ่านก่อนแก้ใดๆ)

### Top-level structure (schema v3)
```json
{
  "schemaVersion": 3,
  "exported": "2026-05-11",
  "topicNames": { "1": "เซต", ..., "15": "สถิติ" },
  "sets": {
    "samn-2563-03": {
      "source": "วิชาสามัญ",
      "subject": "คณิตศาสตร์",
      "year": 2563,
      "month": 3,
      "examDate": "วันอาทิตย์ที่ 15 มีนาคม 2563 เวลา 8.30-10.00 น.",
      "totalQuestions": 30,
      "totalScore": 100,
      "structure": { ... },
      "topicDistribution": { "3": 4, "15": 2, ... }
    }
  },
  "questions": [ /* array */ ]
}
```

### Question object
```json
{
  "id": "samn-2563-03-q24",
  "setId": "samn-2563-03",
  "questionNumber": 24,
  "topics": ["15"],
  "type": "mc" | "fill",
  "level": "easy" | "medium" | "hard",
  "score": 4,
  "question": "...LaTeX ใน $...$...",
  "hasImage": true,
  "choices": ["75.00", "76.75", "77.45", "78.50", "79.00"],   // มีเฉพาะ mc
  "correct": 2,                                                // ⚠️ 0-INDEXED!
  "accept": ["6"],                                             // มีเฉพาะ fill (รายการที่ยอมรับ)
  "imageNote": "คำอธิบายรูปภาษาไทย",
  "imageSpec": { /* optional, ดูข้างล่าง */ },
  "explanation": ["บรรทัด 1", "บรรทัด 2", ...]
}
```

### ⚠️⚠️⚠️ Convention สำคัญที่เคยพลาด

- **`correct` ใน mc คือ INDEX แบบ 0-indexed** ของ array `choices`
- ตัวอย่าง: `correct: 2` ของ Q24 หมายถึง `choices[2]` = "77.45"
- ใน admin.html มี `i === q.correct` (ถูกต้องแล้ว) — ห้ามแก้กลับเป็น `i + 1 === q.correct`

### imageSpec types — สถานะใน math-bank renderers.js

| Type | สถานะ | Use case |
|---|---|---|
| `normal-curve` | ✅ **Implemented** | Q24 ของ samn-2563-03 (โค้งระฆัง + shade + ลูกศร) |
| `ztable-with-curves` | ⏳ Pending | Z-table พร้อม mini curves |
| `polygon-labeled` | ⏳ Pending | รูปเรขาคณิตมี label มุม/ด้าน |
| `unit-circle-figure` | ⏳ Pending | วงกลมหนึ่งหน่วย + จุดที่กำหนด |
| `stacked-bar-100` | ⏳ Pending | กราฟแท่งซ้อน 100% (สถิติ) |
| `3set-c-in-a-shade-ab-minus-c` | ⏳ Pending | Venn 3 วง (chap-01-set q36) |

**Reference สำหรับ renderer ตัวอื่น ๆ:** อยู่ใน portal `index__1_.html` ของแชท Phase B (พอรต portal มาตรง ๆ ได้ — byte-identical pattern)

---

## 📦 Scope ปัจจุบัน — 12 sets, 458 ข้อ

| Set ID | จำนวน | สถานะ imageSpec |
|---|---|---|
| `samn-2564-04` | 30 | ✅ Complete (มี imageSpec) |
| `samn-2565-03` | 30 | ✅ Complete |
| `samn-2563-03` | 30 | ✅ **Q24 render สมบูรณ์ (Phase B)** |
| `samn-2562-03` | 30 | ⏳ Pending |
| `samn-2561-03` | 30 | ⏳ Pending |
| `samn-2559-12` | 30 | ⏳ Pending |
| `samn-2558-12` | 30 | ⏳ Pending |
| `samn-2558-01` | 30 | ⏳ Pending |
| `samn-2557-01` | 30 | ⏳ Pending |
| `samn-2556-01` | 30 | ⏳ Pending |
| `samn-2555-01` | 30 | ⏳ Pending |
| `chap-02-logic` | 128 | ⏳ Pending |

**รวม: 458 ข้อ** | bank.json ~789KB

---

## 🟢 Phase B — เสร็จสมบูรณ์ (15 พ.ค. 2569)

### ผลลัพธ์

- 🆕 **`viewer/renderers.js`** (79 บรรทัด, 5.2KB) — มี `normalPdf`, `renderNormalCurve`, `renderImage` switch
- ✏️ **`viewer/admin.html`** patched 3 จุด:
  - บรรทัด 14: เพิ่ม `<script defer src="renderers.js"></script>`
  - บรรทัด 277-286: เพิ่ม CSS `.img-rendered` (กรอบขาว แสดง SVG)
  - บรรทัด 524-548: แก้ logic ใน `renderQBody` — เรียก `renderImage()` พร้อม fallback ถ้า type ไม่รองรับ
- 🚀 **Deployed** to production — Q24 ของ samn-2563-03 ขึ้น SVG ที่ qcleasing1-oss.github.io แล้ว

### Architecture ของ renderers.js

```javascript
function normalPdf(x) { /* standard normal PDF */ }
function renderNormalCurve(spec) { /* returns <svg>...</svg> string */ }

function renderImage(spec) {
  if (!spec || !spec.type) return null;
  switch (spec.type) {
    case 'normal-curve': return renderNormalCurve(spec);
    // TODO: case 'ztable-with-curves': ...
    default: return null;  // unknown → admin.html จะ fallback ไป placeholder
  }
}
```

**Key design:** ถ้า `renderImage` คืน `null` → admin.html จะแสดง **placeholder card สีเหลือง** (เดิม) — graceful degradation ทำให้ data ใหม่ที่มี type ที่ยังไม่ implement ไม่พัง

### บทเรียนที่ได้ระหว่าง Phase B (สำคัญ! Claude คนต่อไปจะเจอซ้ำ)

| Pitfall | อาการ | วิธีแก้ |
|---|---|---|
| **เปิดไฟล์ผ่าน `file://`** | "Failed to fetch" (ไม่มี HTTP status) | ต้องเปิดผ่าน HTTP server (`python -m http.server`) |
| **Port ชนกับ python ตัวเดิม** | เห็นเว็บอื่น/404 ที่ `localhost:8000` | ใช้ port อื่น เช่น 8001 |
| **Browser cache** | Push แล้วยังเห็นเวอร์ชันเก่า | Hard refresh (Ctrl+Shift+R) ทุกครั้งหลัง push |
| **GitHub Desktop เตือน LF→CRLF** | warning สีเหลือง | ปกติบน Windows, ไม่กระทบ functional |

### Workflow ที่ใช้ทดสอบ (recommended)

```cmd
:: 1. เปิด File Explorer ไปที่ math-bank → คลิก address bar → พิมพ์ cmd → Enter
:: 2. ใน CMD ที่เปิดขึ้น:
python -m http.server 8001

:: 3. browser → http://localhost:8001/viewer/admin.html → teacher2026
:: 4. ทดสอบจนพอใจ
:: 5. GitHub Desktop → Commit → Push
:: 6. browser tab ใหม่ → production URL → Ctrl+Shift+R → verify
```

---

## 🔵 Phase D — เพิ่ม imageSpec set ที่เหลือ (NEXT)

### Workflow ปกติของ Phase D

```
1. คุณครูแนบ PDF / screenshot ของข้อสอบ (เฉพาะข้อที่มีรูป)
2. บอก Claude เช่น "เพิ่ม imageSpec ให้ samn-2562-03 q5 type normal-curve"
3. Claude:
   a. อ่าน imageSpec ของ Q24 (samn-2563-03) เป็น reference pattern
   b. เสนอ imageSpec JSON ตามที่เห็นในรูป
   c. แสดง JSON edit แบบ atomic
4. คุณครู save ลง bank.json
5. Test local (port 8001) → verify SVG ถูกต้อง
6. ถ้า OK → GitHub Desktop → Commit → Push
7. รอ 1-2 นาที → portal/admin live ใช้งานได้
```

### Reference imageSpec — Q24 ของ samn-2563-03 (normal-curve)

```json
{
  "type": "normal-curve",
  "width": 450,
  "height": 220,
  "shadeFromLeft": -1.5,
  "shadeBetween": [[0, 1]],
  "xLabels": [
    {"z": -1.5, "text": "40", "line": true},
    {"z": 0,    "text": "55", "line": true},
    {"z": 1,    "text": "65", "line": true}
  ],
  "valueLabels": [
    {"z": -2.7, "yFrac": 0.35, "text": "0.0668", "arrowTo": {"z": -1.9, "yFrac": 0.92}},
    {"z": 1.6,  "yFrac": 0.15, "text": "0.3413", "arrowTo": {"z": 0.55, "yFrac": 0.55}}
  ]
}
```

### Spec fields ของ `normal-curve` (อ้างจาก renderers.js)

| Field | Type | คำอธิบาย |
|---|---|---|
| `width`, `height` | number (optional) | ขนาด SVG (default 450 x 220) |
| `zRange` | `[min, max]` (optional) | ช่วงแกน x (default `[-3.5, 3.5]`) |
| `shadeFromLeft` | number (optional) | z ที่เริ่ม shade จากด้านซ้าย (สีเทา) |
| `shadeFromRight` | number (optional) | z ที่เริ่ม shade จากด้านขวา (สีเทา) |
| `shadeBetween` | `[[z1, z2], ...]` (optional) | คู่ของ z ที่จะ shade ระหว่าง (สีฟ้า) |
| `xLabels` | `[{z, text, line?}, ...]` | ป้ายบนแกน x; `line: true` = ลากเส้นลงจากเส้นโค้ง |
| `valueLabels` | `[{z, yFrac, text, arrowTo?}, ...]` | ป้ายเลขลอย + ลูกศรชี้ไปยังจุด `{z, yFrac}` |

### เป้าหมาย Phase D

ทำได้ **หลายข้อต่อแชต** — context เบาเพราะแต่ละ imageSpec แยกกัน  
**ลำดับแนะนำ:** เริ่มจาก set ที่มี normal-curve เยอะ (จะใช้ renderer ที่มีแล้ว) → ค่อย ๆ พบ type ใหม่ที่ต้อง implement (เข้า Phase E)

---

## 🔮 Phase E — เพิ่ม renderer types (เมื่อต้องการ)

เมื่อเจอข้อที่ต้องการ type ใหม่ (เช่น `polygon-labeled`):

1. Port renderer จาก portal `index__1_.html` (มี `renderPolygonLabeled`, `renderZTable`, ฯลฯ ครบทุกตัว)
2. เพิ่มฟังก์ชันใน `renderers.js`
3. เพิ่ม `case 'xxx': return renderXxx(spec);` ใน `renderImage` switch
4. Test local → push → live
5. ปลด TODO comment ใน `renderers.js`

**Reference:** Portal `index__1_.html` มี renderer ทุกตัวอยู่แล้วที่ line ~1422-1500 (HW-TPL scope) และ ~3215-3300 (BV-MAIN scope) — byte-identical

---

## 🔄 Workflow ปกติ (commit/push routine)

ทุกครั้งที่แก้ bank.json:

1. **ที่ Claude:** Claude เสนอ JSON edit
2. **คุณครู:** save ลงใน `A:\โปรเจคสอนคณิตศาสตร์\math-bank\data\bank.json`
3. **Test local** ก่อน push (โดยเฉพาะถ้าแก้ imageSpec ใหม่):
   - File Explorer → math-bank → address bar พิมพ์ `cmd`
   - `python -m http.server 8001`
   - browser → `http://localhost:8001/viewer/admin.html`
4. **GitHub Desktop:**
   - tab "Changes" — เห็น diff สีแดง/เขียว
   - **Always review diff before commit** (pre-flight)
   - Summary: `Add imageSpec for samn-XXXX-XX qNN` (atomic message)
   - Commit to main
5. **Push origin** — ขวาบน คลิกปุ่ม
6. รอ 1-2 นาที → Actions tab → 🟢 → live
7. Production URL → **Ctrl+Shift+R** → verify

---

## ⚠️ Anti-Crash Protocol (สำคัญสำหรับ Claude คนใหม่)

1. **One atomic task per turn** — อย่ารวมหลายงานในเทิร์นเดียว
2. **Pre/post-flight check ทุก JSON edit** — view ก่อนแก้, verify หลังแก้
3. **ขอ confirm ก่อน irreversible action** — push, force-push, delete file
4. **อย่ากระโดด phase** — ทำตามลำดับ A → B → D → E
5. **คุณครูพูดไทย** — ตอบเป็นไทย แต่ code/path เป็นอังกฤษ
6. **Screenshot verify** — ขอให้คุณครูส่ง screenshot เมื่อ:
   - ทำขั้นใหม่ครั้งแรก
   - หลัง action สำคัญ (commit, push, deploy)
   - มี error / สงสัย
7. **อย่า assume technical knowledge** — เขียน step-by-step พร้อมคำสั่ง copy-paste ได้
8. **Aesthetic preference:** parchment cream + Sarabun font — อย่าเปลี่ยน theme โดยไม่ขอ
9. **Test local ก่อน push เสมอ** — ป้องกัน hot fix ค้างใน production
10. **Hard refresh หลัง push** — Ctrl+Shift+R, ไม่ใช่ F5

---

## 📋 Files ที่ Claude คนใหม่ควรอ่านในแชทใหม่

**ต้องแนบใน project knowledge (หรือแชท):**
1. `HANDOVER_BANK_v2.md` (ไฟล์นี้) — อ่านก่อน
2. `bank.json` (จาก `data/bank.json`) — เมื่อจำเป็น

**Optional (เฉพาะ Phase E — เพิ่ม renderer ใหม่):**
3. Portal `index__1_.html` — สำหรับ port renderer functions
4. `viewer/renderers.js` ปัจจุบัน — ดู pattern ของ renderer ที่มีอยู่

**ไม่ต้องแนบ:**
- `HANDOVER_BANK_v1.md` (เก่า — content ครอบคลุมใน v2 แล้ว)
- `viewer/admin.html` (Claude อ่านสดจาก repo หรือขอคุณครูส่ง — ไม่ค่อยต้องแก้แล้ว)

---

## 💬 ข้อความเริ่มแชทใหม่ (copy-paste ได้เลย)

```
สวัสดี Claude ฉันคือคุณครูOFF
ต่อยอด project "คลังข้อสอบคณิต ม.ปลาย" จากแชทก่อน

แนบไฟล์:
- HANDOVER_BANK_v2.md — อ่านก่อน (จะรู้สถานะปัจจุบัน + bank schema + URLs + workflow)
- bank.json — bank ปัจจุบัน

วันนี้อยากทำ Phase _____ [ D / E — เลือก ]

ทำตาม anti-crash protocol — 1 atomic task per turn
```

---

## 🗝️ Key References

- **Admin viewer password:** `teacher2026`
- **GitHub username:** `qcleasing1-oss`
- **Repo name:** `math-bank`
- **Local path:** `A:\โปรเจคสอนคณิตศาสตร์\math-bank\`
- **Branch:** `main`
- **Total questions:** 458 ใน 12 sets
- **Recommended local server port:** `8001` (8000 อาจชนกับ python ตัวเดิม)
- **Hard refresh shortcut:** `Ctrl+Shift+R`

---

## ✅ Health Check ของ Claude คนใหม่

ก่อนเริ่มงาน Claude คนใหม่ควรยืนยัน 3 ข้อนี้กับคุณครู (ในประโยคเดียว ไม่ต้องถามรายข้อ):

1. URL `https://qcleasing1-oss.github.io/math-bank/viewer/admin.html` ยังเปิดได้และ Q24 ของ samn-2563-03 ยังขึ้น SVG ปกติ?
2. คุณครูเปิด GitHub Desktop ได้?
3. มีไฟล์ที่อยากแนบเพิ่ม (PDF ข้อสอบ, screenshot) ในแชทนี้ไหม?

แล้วลุยตาม phase ที่คุณครูเลือก

---

## 🎯 Closing notes

โปรเจคนี้ใช้เวลารวมทั้ง Phase A + B + C ประมาณ **23 turns** — Phase B ใช้เวลา ~11 turns (รวม debug infra-level 3 ปัญหา) — ไม่มี hot fix ค้างใน production

**คุณครูเก่งและตามได้เร็ว:**
- Phase A (แชทก่อน): "ไม่เคยใช้ GitHub" → "deploy public website ผ่าน Pages เป็นเอง" ในเวลาไม่กี่ชั่วโมง
- Phase B (แชทนี้): debug `file://` → port shadow → cache → ได้ครบเอง โดยมี Claude guide

**ปัจจุบัน:** bank นี้ deploy live แล้ว — Q24 ของ samn-2563-03 พร้อมใช้สอนจริง 🎨

ขอให้ Claude คนใหม่สนุกกับการต่อยอดงานนี้ — bank นี้จะกลายเป็นทรัพยากรประโยชน์มากต่อการสอนคณิตศาสตร์ในไทย 🇹🇭📚

— Claude (15 พ.ค. 2569, Phase B)

# 📚 CONTEXT-FOR-COWORK.md

> **เอกสาร bootstrap สำหรับ Cowork — ต้องอ่านก่อนเริ่มงานทุกครั้ง**
>
> ไฟล์นี้รวม context ทั้งหมดที่ Cowork ต้องรู้เกี่ยวกับโปรเจค math-bank
> รวมข้อมูลที่อยู่ใน Chat userMemories (ไม่ porting ข้าม Cowork อัตโนมัติ)
> Last updated: 4 มิ.ย. 2569

---

## 1. 👤 ใครคือใคร

- **ผู้ใช้:** ครู OFF (QC)
- **อาชีพ:** ครูคณิตศาสตร์ ม.ปลาย ในไทย
- **ภาษาหลัก:** ไทย (Cowork ตอบเป็นไทยเสมอ ยกเว้นโค้ด/คำสั่ง)
- **ทักษะ:** มือใหม่ด้าน code/CLI แต่ใช้ **GitHub Desktop คล่อง**
- **Workflow ที่ครูถนัด:**
  - แก้ไฟล์ใน VS Code / preview ใน Live Server
  - commit + push ผ่าน GitHub Desktop GUI (ไม่ใช้ git CLI)
  - ดู preview ใน browser ด้วย viewer/admin.html

---

## 2. 🎯 โปรเจค math-bank

- **เป้าหมาย:** คลังข้อสอบคณิตศาสตร์ ม.ปลาย (สำหรับ verify เฉลย + ฝึกทำของนักเรียน)
- **Repo:** `github.com/qcleasing1-oss/math-bank`
- **Local path (เครื่องครู):** `A:\โปรเจคสอนคณิตศาสตร์\math-bank`
- **Admin viewer (production):** `https://qcleasing1-oss.github.io/math-bank/viewer/admin.html`
  - รหัสผ่าน: `teacher2026`
- **ขอบเขต:** วิชาสามัญ + PAT1 + A-Level + รายบท (chap-01 ถึง chap-17)

---

## 3. 📊 สถานะคลังปัจจุบัน (verified 3 มิ.ย. 69)

**42 ชุด · 1,985 ข้อ**

| ประเภท | จำนวนชุด | หมายเหตุ |
|---|---|---|
| PAT1 | 24 ชุด | 2552–2565 ครบทุกครั้งสอบ |
| สามัญ (samn) | 11 ชุด | |
| A-Level (alvl1) | 4 ชุด | 2566-03 / 2567-03 / 2568-03-v2 / 2569-03 |
| รายบท | 3 บท | chap-01-set (82 ข้อ), chap-02-logic (128 ข้อ), chap-03-realnumber (190 ข้อ) |

INGEST PAT1+A-Level+samn ครบทั้งหมดแล้ว — chap-04 ถึง chap-17 **ยังไม่เริ่ม**

---

## 4. 🏗️ Architecture (Phase F.4 — modular source)

```
math-bank/
├── data/
│   ├── manifest.json         ← list ทุกชุด (indent=2)
│   ├── sets/
│   │   ├── chap-01-set.json
│   │   ├── chap-02-logic.json
│   │   ├── pat1-2565-10.json
│   │   └── ... (42 ไฟล์)
│   └── bank.json             ← AUTO-BUILD จาก GitHub Actions ⚠️ ห้ามแก้มือ
├── viewer/
│   ├── admin.html            ← v4 (difficulty Phase 4)
│   ├── renderers.js          ← 1435 บรรทัด, ~65KB, iter 3 deployed
│   └── ...
├── docs/
│   └── CONTEXT-FOR-COWORK.md ← ไฟล์นี้
└── .github/workflows/        ← build bank.json อัตโนมัติเมื่อ push sets/
```

**กฎสำคัญ:**
- ครู (หรือ Cowork) commit เฉพาะ `data/sets/<setId>.json` + `data/manifest.json` (ถ้าเพิ่ม/ลบชุด)
- **ห้ามแก้ `data/bank.json` มือ** — GitHub Actions build เอง
- **ห้าม push `viewer/renderers.js`** โดยไม่บอกครู (เป็น deploy critical)

---

## 5. 🎬 งานปัจจุบัน: Phase E — chap-01-set 3-set Venn batch

### Scope หลัก: 14 ข้อ 3-set ใน chap-01-set
**Q36, Q38, Q40, Q44, Q45, Q46, Q47, Q48, Q50, Q51, Q52, Q54, Q74, Q75, Q79**

### Batch order
- **E1 (กำลังทำ):** Q36, Q38, Q40 (3 ข้อ easier 3-set)
- **E2:** Q44, Q45, Q46, Q47
- **E3:** Q48, Q50, Q51
- **E4:** Q52, Q54, Q74, Q75
- **E5:** Q79 + cleanup

### Spec ที่เตรียมไว้แล้ว — Q48 (batch E3)

```json
{
  "imageSpec": {
    "type": "venn-diagram",
    "sets": 3,
    "layout": "intersecting",
    "labels": {"A": "ก", "B": "ข", "C": "ค"},
    "regions": {
      "A_only": "x", "AB_only": "20", "B_only": "y",
      "AC_only": "22", "ABC": "23", "BC_only": "11", "C_only": "9"
    },
    "universe": false
  }
}
```

**⚠️ Q48 PDF typo:** เฉลยเขียน "ค = 75 คะแนน" แต่จริง 65 (ผลรวม 70+64+65=199 ตรงข้อ 2)

**Math (verified):**
- `100 = 20 + 23 + 11 + 22 + 9 + x + y` → `x + y = 15`
- `ก = x + 65`, `ข = y + 54`, `ก − ข = 6` → `x − y = −5`
- ได้ `y=10, x=5` → `ก=70, ข=64, ค=65`
- คำตอบ: **ข้อ 3 ผิด** (ผู้ลงให้ ก เท่านั้น = x = 5 ไม่ใช่ 10)

### Scope รอง (รอ phase ถัดไป — ไม่ใน E1-E5)

- Q33 — custom `C ⊆ A ∪ B` (special layout, renderer ยังไม่รองรับ)
- Q49 — region arrows (special)
- Q55 — box-set (special)
- Q74 โจทย์ — array of 5 ภาพ

---

## 6. 🔒 INGEST PROTOCOL — กฎเหล็ก (ห้ามข้าม ห้ามลัด)

### ⛔ กฎข้อเดียวที่สำคัญที่สุด

**ห้าม trust text extract จาก PDF เด็ดขาด — ต้องเปิดภาพ PDF อ่านทุกข้อ**

เหตุผล: PDF ชุดข้อสอบไทยมักฟอนต์เพี้ยน — text extract มั่ว (เลขยกกำลังหาย, ตัวห้อยหาย, `sin`→`LMN`, `cos`→`QRL`, ตัวแปร a,b→r,s, ฐาน log เพี้ยน)

### ลำดับงานต่อ 1 ข้อ (ทำครบทุก step)

**STEP 1 — เปิดภาพ (ไม่ใช่ text)**
```bash
# render หน้าที่มีข้อนั้น เป็น png ความละเอียดสูง
pdftoppm -png -f <หน้า> -l <หน้า> -r 150 exam.pdf pg
```
- อ่าน **โจทย์ + ทุก choice + เลขข้อ** จากภาพ
- ระวังเป็นพิเศษ: เลขยกกำลัง (x² vs x⁴), ตัวห้อย (z₁, log ฐาน), ตัวแปร (f vs F, a vs r, √2 vs √x), เครื่องหมาย (≤ ≥ ≠), เศษส่วนซ้อน
- **text extract ใช้ได้แค่เป็นตัวช่วยสะกดคำไทยยาว ๆ เท่านั้น — ตัวเลข/สูตร/ตัวแปร เชื่อภาพ 100%**

**STEP 2 — พิมพ์โจทย์ + choices**
- โจทย์หลายบรรทัด → **newline จริง** ใน string (กด Enter) **ห้ามพิมพ์ `\n` literal**
- choices ที่มี LaTeX → ครอบ `$...$` เสมอ
- `√` → `\sqrt{}` / เศษส่วน → `\dfrac{}` (ห้าม bare √)
- ตัวแปรต้องตรง PDF เป๊ะ

**STEP 3 — verify คณิตด้วย sympy/numpy ทันที**
```python
import sympy as sp
# คำนวณคำตอบจากโจทย์ที่เพิ่งพิมพ์ → ดูว่าตรง choice ไหน
```
- ถ้าผลลัพธ์ **ไม่ตรง choice ใดเลย** → กลับไป STEP 1 เปิดภาพอ่านใหม่
- ถ้าตรง choice → จด index (0-indexed) ไว้

**STEP 4 — เทียบ answer key**
- `correct + 1` ต้องตรง PDF answer key
- ถ้าคำนวณได้คำตอบ แต่ตำแหน่งไม่ตรง key → อ่านโจทย์ผิดแน่ → กลับ STEP 1

**STEP 5 — เขียน explanation ตาม STANDARD v2** (ดูข้อ 7)

---

## 7. 📐 STANDARD v2 — Explanation Ordering (คงที่ ห้ามสลับ)

```
📐 ความรู้พื้นฐาน
   ↓
ขั้นที่ 1: ...
ขั้นที่ 2: ...
ขั้นที่ N: ...
   ↓
[🔄 วิธีอื่น (optional — ต่อเมื่อต่างมุมจริง + ถูกคณิต + ไม่ด้อยกว่า)]
   ↓
✔ ตรวจคำตอบ
   ↓
✅ คำตอบ: ... → ตัวเลือก N
   ↓
💡 เทคนิคที่ใช้
   ↓
⚠️ จุดที่เด็กมักผิด
```

**กฎ:**
- ทุกข้อต้องมี 💡 + ⚠️ เสมอ
- 🔄 เพิ่มเฉพาะวิธีต่างมุมจริง (verify ถูกคณิต + ไม่ด้อยกว่าวิธีหลัก)
- ละเอียดพอเด็กไม่เก่งอ่านเข้าใจเอง (อธิบายสูตร/นิยามก่อน, ทุกขั้นมีเหตุผล)
- verify ท้าย
- บรรทัดว่าง `""` คั่น section
- `<b>...</b>` ครอบหัว section

---

## 8. 📋 Field Order Canonical

### type=mc
```
id → setId → questionNumber → topics → subTopics → difficulty
→ type → level → score → question → choices → hasImage → sourceTag
→ [source] → imageSpec → correct → explanation → notes
```

### type=fill
```
id → setId → questionNumber → topics → subTopics → difficulty
→ type → level → score → question → hasImage → sourceTag
→ [source] → imageSpec → correct → accept → explanation → notes
```

**Field rules:**
- `correct` ใน mc = **0-indexed integer**
- `correct` ใน fill = **string**
- field `choices` **ห้ามมี**ในข้อ type=fill
- `topics` = list of string เช่น `["8"]` (เลขบทหลัก 1–17)
- `subTopics` = list of string (บทที่เป็น tool จริง ไม่ใส่ถ้าแค่คำปรากฏ)

---

## 9. ✅ POST-FLIGHT — 8 Checks (รันก่อน save/push ทุกครั้ง)

```python
import json, io, re

path = 'data/sets/<setId>.json'  # เปลี่ยน path ตามไฟล์
d = json.load(io.open(path, encoding='utf-8'))
qs = d['questions']
problems = []

# (1) choices LaTeX without $
sig = re.compile(r'\\(begin|frac|dfrac|sqrt|cdot|le|ge|ne|pm|infty|vec|left|right|overline|sum|int|forall|exists|sim|cup|cap|notin|triangle|varnothing)')
for q in qs:
    for i, c in enumerate(q.get('choices', []) or []):
        if sig.search(c) and '$' not in c:
            problems.append(f"(1) Q{q['questionNumber']}[{i}] หลุด $")

# (2) literal \n
bad_nl = re.compile(r'\\n(?![a-zA-Z])')
for q in qs:
    fields = [q.get('question', '')] + (q.get('choices', []) or []) + (q.get('explanation', []) or [])
    for f in fields:
        if isinstance(f, str) and bad_nl.search(f):
            problems.append(f"(2) \\n literal Q{q['questionNumber']}")

# (3) bare √ (U+221A)
for q in qs:
    if '\u221a' in json.dumps(q, ensure_ascii=False):
        problems.append(f"(3) bare √ Q{q['questionNumber']}")

# (4) correct None for mc
for q in qs:
    if q.get('type') == 'mc' and q.get('correct') is None:
        problems.append(f"(4) correct None Q{q['questionNumber']}")

# (5) surrogate
try:
    open(path, 'rb').read().decode('utf-8')
except Exception as e:
    problems.append(f"(5) {e}")

# (6) bmatrix raw
for q in qs:
    for line in q.get('explanation', []) or []:
        if '\\begin{bmatrix' in line and '$' not in line:
            problems.append(f"(6) bmatrix Q{q['questionNumber']}")

# (7) ยอมแพ้
for q in qs:
    for line in q.get('explanation', []) or []:
        for kw in ['ยอมแพ้', 'ตามเฉลย']:
            if kw in line:
                problems.append(f"(7) {kw} Q{q['questionNumber']}")

# (8) [IMAGE] marker for Venn questions
venn_qs = [24, 32, 35, 36, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 54, 71, 73, 74, 75, 79]
for q in qs:
    if q['questionNumber'] in venn_qs and q.get('hasImage'):
        exp = q.get('explanation', [])
        if exp and exp[0] != '[IMAGE]':
            problems.append(f"(8) [IMAGE] marker missing Q{q['questionNumber']}")

print('FAIL:' if problems else 'PASS ✅')
for p in problems:
    print(' -', p)
```

**ทั้ง 8 ต้องเป็น 0 ก่อน save**

---

## 10. 🚀 Push Workflow (ทำตามเป๊ะ)

1. **Pull origin ก่อน** เสมอ (กัน rebase conflict) — Cowork สั่ง `git pull` หรือบอกครู pull ผ่าน GitHub Desktop
2. แก้ไฟล์ `data/sets/<setId>.json`
3. **POST-FLIGHT 8 checks** ต้อง PASS
4. สร้าง preview HTML standalone (KaTeX + Sarabun + parchment `#f6f1e6`)
5. **ขอครู screenshot verify** preview ก่อน push
6. ครู OK → commit ผ่าน GitHub Desktop
7. **Push เฉพาะ `data/sets/<setId>.json`** (และ `data/manifest.json` ถ้าเพิ่ม/ลบชุด)
8. **ห้ามแตะ:** `data/bank.json` (auto-build), `viewer/renderers.js` (deploy critical)

---

## 11. 🎨 Renderer Status (อย่า re-deploy ถ้าไม่จำเป็น)

**Deployed ใน `viewer/renderers.js` iter 3 (1435 lines, ~65KB):**

| Type | Variants | สถานะ |
|---|---|---|
| `venn-diagram` | 2-set intersecting + disjoint | ✅ |
| `venn-diagram` | 3-set intersecting (iter 3) | ✅ |
| `normal-curve` | shading + annotations | ✅ |
| `function-plot` | 4 kinds + shadeBetween | ✅ |
| `ztable-with-curves` | | ✅ |
| `unit-circle-figure` | array form | ✅ |
| `stacked-bar-100` | | ✅ |
| `polygon-labeled` | | ✅ |

**Geometry 3-set Venn (iter 3):**
- r=68, d=70, equilateral triangle, viewBox 400×360
- Labels: outward unit vector, labOff=r+32
- 8 regions: `A_only`/`B_only`/`C_only`/`AB_only`/`AC_only`/`BC_only`/`ABC`/`outside`
- Shading: nested clipPath + white-circle punch-outs

**ยังไม่รองรับ (อย่ารับงานเหล่านี้ใน batch ปกติ):**
- 3-set disjoint
- Custom layout (Q33 `C ⊆ A ∪ B`, Q49 arrows, Q55 box-set)
- Multi-image (Q74 array)

---

## 12. 📚 Key Learnings — Pattern A-F (ระวังให้ดี)

### Pattern A: HANDOVER เก่าอาจอ่าน Claude คนก่อนผิด
- ก่อน rewrite ใดๆ ต้องดู PDF เฉลยจริง — ไม่ trust HANDOVER, JSON เดิม
- ตัวอย่าง Q41: HANDOVER บอก "ภาพ Venn เปล่า" แต่ PDF จริงใช้ regions

### Pattern B: Thai ใน labels render italic แปลก
- Renderer ใช้ italic Cambria Math สำหรับ labels `A/B/C`
- ภาษาไทยใน italic → ดู ad-hoc
- **Default:** ASCII single letter (`C`, `S`, `A`) + อธิบายความหมายใน explanation
- **Exception:** ถ้า PDF ใช้ ก/ข/ค ตัวเดียวสั้น ๆ → ทดสอบ preview ได้ (Q48 OK)

### Pattern C: Region positions hardcoded
- Renderer iter 3 มี position constants ตายตัว
- Region label ยาว (>3 chars) อาจ overflow → ทดสอบ preview
- Single letter หรือ single number = safe เสมอ

### Pattern D: `universe=true` เมื่อไหร่
- **`true`:** มี outside region (ไม่อยู่ในเซตใดเลย) / โจทย์ระบุ "universal set" / "เซตเอกภพ"
- **`false`:** "ทุกคนต้องอยู่อย่างน้อย 1 เซต" (Q48 case — 100 คน อยู่ใน ก ∪ ข ∪ ค ครบ)

### Pattern E: Push workflow
- Pull origin **ก่อน** Commit
- Push เฉพาะ `data/sets/<setId>.json`
- ไม่แตะ `bank.json` (auto-build)
- ไม่แตะ `renderers.js` (deploy critical)

### Pattern F: Preview พังใน artifact viewer?
- Artifact viewer ไม่ load external `<script src=>`
- ต้อง **inline** renderers.js ลงใน HTML
- หรือใช้ Live Server บนเครื่องครู (ใน Cowork ใช้ Live Server ดีกว่า)

### Pattern G (เพิ่มจาก Cowork experience)
- `sympy.cbrt(negative)` คืน complex root ไม่ใช่ real root — ใช้ `sign(x)*abs(x)**(1/3)` แทน
- ข้อที่โจทย์ขัดแย้งในตัวเอง → `correct=null` + อธิบายในเฉลย (ห้าม guess)
- `<` ติดตัวอักษรใน `$...$` → browser parse เป็น HTML tag → ต้องเว้นวรรค (`$y < x$`)
- คำพูดไทยใน JSON ใช้ double-quote ธรรมดา ห้ามมี backslash นำหน้า
- `\ne` ใน preview HTML render เป็น ≡ (cosmetic bug ของ local preview เท่านั้น) — ไม่ต้องแก้ JSON
- ไม่ใช้ Unicode `√` เดี่ยว ๆ ใน SVG — ใช้ `_ucMathToSvg()` helper แทน

---

## 13. 🔢 Chapter IDs (1–17)

```
1 = เซต              10 = จำนวนเชิงซ้อน
2 = ตรรกศาสตร์        11 = ลำดับและอนุกรม
3 = จำนวนจริง         12 = การนับและความน่าจะเป็น
4 = เรขาคณิตวิเคราะห์  13 = แคลคูลัส
5 = ฟังก์ชัน          14 = อนุกรมอนันต์
6 = เมทริกซ์          15 = สถิติ
7 = ตรีโกณมิติ         16 = กำหนดการเชิงเส้น
8 = ลอการิทึม          17 = ทฤษฎีจำนวน
9 = เวกเตอร์
```

---

## 14. 🛠️ Tools & Environment (เครื่องครู)

- **OS:** Windows
- **GitHub Desktop:** workflow หลัก (ครูไม่ใช้ git CLI)
- **Editor:** VS Code + Live Server extension
- **Python tools ที่ต้องใช้ได้:** sympy, numpy, pypdf, pymupdf (fitz), pdftoppm, PIL
- **JSON write convention:**
  - `json.dumps(ensure_ascii=False, indent=2)` (chap-01-set ใช้ indent=2)
  - `io.open(encoding='utf-8')`
  - LF line endings (Windows อาจแปลง CRLF auto — OK)
  - ไม่มี trailing newline
  - ไม่มี BOM
- **Rendering:** KaTeX (strict: false), Sarabun font, parchment `#f6f1e6`

---

## 15. 🚦 Long-term Scope (หลัง Phase E เสร็จ)

### งานใหญ่อันดับ 1
**chap-04 ถึง chap-17** — ~14 บท พันข้อ ยังไม่ ingest text เลย

### งานรอง
- **Difficulty tag** ~39 ชุดที่เหลือ (batch tag)
- **Audit 🔄 วิธีอื่น:** alvl1-2568-03-v2, samn-2561-03 (Q4/Q6/Q21)
- **Venn renderer per-chapter:** เซต → ตรรก → จำนวนจริง (paused ระหว่างทำ 3-set batch)
- **chap-02-logic, chap-03-realnumber Venn:** ออก verification report แบบ chap-01-set

---

## 16. ⚠️ Things to NEVER Do

1. ❌ **ห้าม trust text extract จาก PDF** — เปิดภาพเสมอ
2. ❌ **ห้ามแก้ `data/bank.json`** มือ
3. ❌ **ห้าม push ไฟล์โดยไม่ POST-FLIGHT PASS ก่อน**
4. ❌ **ห้าม push ไฟล์โดยไม่ขอครู verify preview ก่อน**
5. ❌ **ห้าม assume HANDOVER ถูก** — verify กับ PDF ต้นฉบับ
6. ❌ **ห้าม push `viewer/renderers.js`** โดยไม่บอกครู
7. ❌ **ห้ามใช้ `correct=null`** เว้นแต่โจทย์ขัดแย้งในตัวเอง (ห้าม guess)
8. ❌ **ห้ามตอบเป็นอังกฤษ** เว้นแต่ครูถามเป็นอังกฤษ
9. ❌ **ห้าม batch ใหญ่เกิน 10 ข้อ** ต่อ task (ลด 5-7 ถ้า context โตเร็ว)
10. ❌ **ห้าม push โดยไม่ pull origin ก่อน**

---

## 17. 🎬 Workflow ต่อ 1 ข้อ Ingest (Summary)

1. **เปิดภาพ PDF** — `pdftoppm -png -f <p> -l <p> -r 150 exam.pdf pg`
2. **เทียบ JSON เดิม vs PDF** — flag จุดที่ต้อง rewrite
3. **ระบุ region labels + set labels จาก PDF** (สำหรับ Venn)
4. **Sympy verify** คณิตทุกข้อ
5. **Rewrite explanation** ถ้า approach JSON เก่าไม่ตรง PDF
6. **ใส่ imageSpec + [IMAGE] marker** บนสุด explanation (สำหรับข้อมี hasImage)
7. **Drop legacy fields** — `needsExplanationImage`, update `notes`
8. **POST-FLIGHT 8 checks** ต้อง PASS
9. **Preview HTML standalone** — ครู verify ผ่าน screenshot
10. **Push** เฉพาะ `data/sets/<setId>.json`

---

## 📌 สรุปหัวใจ 1 บรรทัด

**เปิดภาพ PDF ทุกข้อ → พิมพ์ (ตัวแปรตรง PDF, ครอบ `$`, newline จริง) → verify sympy ทันที → เทียบ key → POST-FLIGHT 8 ข้อ → preview → ครู OK → push**

---

*จบเอกสาร — Cowork พร้อมเริ่มงานได้แล้ว*

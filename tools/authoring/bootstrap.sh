#!/usr/bin/env bash
# วางเครื่องมือแต่งข้อกลับเข้าที่ทำงาน แล้วสร้างผลผลิตขึ้นมาใหม่ทั้งหมด
#
# ⛔ ทำไมต้องคัดลอกไปที่ /home/claude แทนที่จะรันตรงจาก repo
#    สคริปต์ทั้ง 175 ตัวตรึงพาธไว้ที่ /home/claude/k1 และ /home/claude/k2 มาตั้งแต่ก้อนแรก
#    การไล่แก้พาธในทุกไฟล์มีความเสี่ยงพิมพ์ผิดสูงกว่าประโยชน์ที่ได้
#    ⇒ ย้ายที่ทำงานให้ตรงกับสคริปต์ ไม่ใช่แก้สคริปต์ให้ตรงกับที่ทำงาน
#
# ใช้:  bash tools/authoring/bootstrap.sh          # ปฏิเสธถ้ามีของเดิมอยู่
#       bash tools/authoring/bootstrap.sh --force  # ทับของเดิม
#
# 🔴 ที่ทำงานเปลี่ยนไม่ได้ — ต้องเป็น /home/claude เท่านั้น
#    เคยลองทำสวิตช์ MB_WORK ไว้ แล้วพบว่ามัน "ผ่านหลอก" : ตัวสร้างขึ้น ✅ ครบทุกตัว
#    แต่มันเขียนผลผลิตลง /home/claude/*/out ตามพาธที่ตรึงไว้ในตัวเอง ⛔ ไม่ใช่ที่ทำงานใหม่
#    ⇒ สวิตช์ที่ทำให้ด่านเขียวโดยที่ของไปอยู่ผิดที่ อันตรายกว่าไม่มีสวิตช์เลย จึงถอดออก

set -euo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
SRC="$REPO/tools/authoring"
WORK=/home/claude          # ⛔ ห้ามเปลี่ยน — สคริปต์ 175 ตัวตรึงพาธนี้ไว้ในตัวเอง
FORCE="${1:-}"

echo "repo   : $REPO"
echo "ที่ทำงาน: $WORK"

for d in k1 k2; do
  if [ -e "$WORK/$d" ] && [ "$FORCE" != "--force" ]; then
    echo "🔴 มี $WORK/$d อยู่แล้ว — หยุด ⛔ กันเขียนทับงานที่ยังไม่ได้เก็บ"
    echo "   ถ้าตั้งใจทับ สั่ง: bash $0 --force"
    exit 1
  fi
done

mkdir -p "$WORK"
for d in k1 k2; do
  rm -rf "${WORK:?}/$d"
  cp -r "$SRC/$d" "$WORK/$d"
  mkdir -p "$WORK/$d/out"
done
echo "✅ วางเครื่องมือแล้ว · $(find "$WORK/k1" "$WORK/k2" -name '*.py' | wc -l) สคริปต์"

echo
echo "── สร้างผลผลิตใหม่จากต้นทาง (parts_b*/) ──────────────────────────────"
cd "$WORK"
fail=0
for f in k1/build_h.py k1/build_m.py k1/build_vh.py k1/v2.py k1/v2b.py k1/v2c.py k1/v3.py \
         k2/build_b3.py k2/build_b4.py k2/build_b5.py k2/build_b6.py k2/build_b7.py \
         k2/build_b8.py k2/build_b9.py k2/build_b10.py k2/build_b11.py k2/build_b12.py \
         k2/build_b13.py k2/build_b14.py k2/build_b15.py k2/build_b16.py k2/build_b17.py \
         k2/build_b18.py k2/build_b19.py k2/build_b20.py k2/build_b21.py \
         k2/build_e.py k2/build_e2.py; do
  [ -f "$f" ] || continue
  if python3 "$f" >/dev/null 2>&1; then printf '  ✅ %s\n' "$f"
  else printf '  ❌ %s\n' "$f"; fail=1; fi
done
[ "$fail" = 0 ] || { echo "🔴 มีตัวสร้างที่รันไม่ผ่าน — หยุด"; exit 1; }

echo
echo "── ด่านพิสูจน์ว่าสร้างของในคลังกลับมาได้ตรงทุกไบต์ ──────────────────"
python3 "$SRC/regen_check.py"

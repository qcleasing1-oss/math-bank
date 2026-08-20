@echo off
chcp 65001 >nul
cd /d "A:\โปรเจคสอนคณิตศาสตร์\math-bank"
echo ===== 1/5 รวมผลเป็นไฟล์เดียว =====
python tools\merge_master.py
echo ===== 2/5 หน้าติดตามความคืบหน้า =====
python tools\progress.py --queue _t1run\QUEUE_now.json --out _t1run\progress.html
echo ===== 3/5 ยามเฝ้างบ + จับงานซ้ำ =====
python tools\budget_guard.py
echo ===== 4/5 สรุปสถานะ (ใช้เปิดแชทใหม่) =====
python tools\status_md.py --out STATUS.md
echo ===== 5/5 สำรองข้อมูล =====
python tools\snapshot.py
echo.
echo เสร็จแล้ว — กำลังเปิดหน้าติดตามงาน...
start "" "_t1run\progress.html"
pause

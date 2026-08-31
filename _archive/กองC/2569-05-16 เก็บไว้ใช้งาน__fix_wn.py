#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_wn.py  —  แทนคำย่อ "ว.N" เป็น "วิธีที่ N" ในไฟล์ข้อสอบทุกชุด
วางไฟล์นี้ไว้ที่ราก repo (โฟลเดอร์เดียวกับ data/) แล้วรัน:  python fix_wn.py
- แก้เฉพาะ field "explanation" เท่านั้น
- ไม่แตะข้อความใน $...$ (ยืนยันแล้วว่าไม่มี ว.N อยู่ในสูตร)
- คงรูปแบบไฟล์เดิม (indent 1/2 ตรวจอัตโนมัติ, LF, ไม่มี BOM, ไม่มี trailing newline)
- เขียนทับเฉพาะไฟล์ที่มีการเปลี่ยน แล้วพิมพ์สรุป
ดู diff ใน GitHub Desktop ก่อน commit เสมอ
"""
import json, re, glob, os, sys

PAT = re.compile(r'ว\.\s?([1234])')
REPL = r'วิธีที่ \1'

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CWD = os.getcwd()

def _looks_like_sets(d):
    """True ถ้าโฟลเดอร์มีไฟล์ชุดข้อสอบ (json ที่มี key 'questions')"""
    for p in glob.glob(os.path.join(d, '*.json')):
        try:
            with open(p, 'r', encoding='utf-8-sig') as f:
                obj = json.load(f)
            if isinstance(obj, dict) and 'questions' in obj:
                return True
        except Exception:
            continue
    return False

def find_sets_dir():
    # ลองตามลำดับ: โฟลเดอร์ที่ไฟล์สคริปต์อยู่ -> data/sets ใต้ที่รัน -> sets -> ที่รัน
    for d in (SCRIPT_DIR,
              os.path.join(CWD, 'data', 'sets'),
              os.path.join(CWD, 'sets'),
              CWD):
        if os.path.isdir(d) and _looks_like_sets(d):
            return d
    return None

def detect_indent(raw_no_trail, data):
    for ind in (2, 1):
        if json.dumps(data, ensure_ascii=False, indent=ind) == raw_no_trail:
            return ind
    return None

def process(path):
    with open(path, 'rb') as f:
        raw_bytes = f.read()
    bom = raw_bytes.startswith(b'\xef\xbb\xbf')
    text = raw_bytes.decode('utf-8-sig' if bom else 'utf-8')
    crlf = '\r\n' in text
    work = text.replace('\r\n', '\n')
    trailing = work.endswith('\n')
    raw_no_trail = work[:-1] if trailing else work

    data = json.loads(work)
    indent = detect_indent(raw_no_trail, data)
    if indent is None:
        print(f'  ! SKIP (indent ตรวจไม่ได้ ไม่กล้าแก้): {path}')
        return 0

    n = 0
    for q in data.get('questions', []):
        e = q.get('explanation')
        if not isinstance(e, list):
            continue
        for i, line in enumerate(e):
            if isinstance(line, str) and PAT.search(line):
                new, cnt = PAT.subn(REPL, line)
                if cnt:
                    e[i] = new
                    n += cnt
    if n == 0:
        return 0

    out = json.dumps(data, ensure_ascii=False, indent=indent)
    if trailing:
        out += '\n'
    if crlf:
        out = out.replace('\n', '\r\n')
    out_bytes = out.encode('utf-8')
    if bom:
        out_bytes = b'\xef\xbb\xbf' + out_bytes
    with open(path, 'wb') as f:
        f.write(out_bytes)
    return n

def main():
    sets_dir = find_sets_dir()
    if not sets_dir:
        print('หาโฟลเดอร์ชุดข้อสอบไม่เจอ')
        print('วาง fix_wn.py ไว้ในโฟลเดอร์ data/sets/ (ที่มีไฟล์ *.json ของชุด) แล้วรันใหม่')
        sys.exit(1)
    print(f'โฟลเดอร์ชุดข้อสอบ: {sets_dir}')
    files = sorted(glob.glob(os.path.join(sets_dir, '*.json')))
    total_files = total_repl = 0
    for path in files:
        try:
            n = process(path)
        except Exception as ex:
            print(f'  ! ERROR {path}: {ex}')
            continue
        if n:
            total_files += 1
            total_repl += n
            print(f'  แก้ {n:>3} ที่: {os.path.basename(path)}')
    print(f'\nสรุป: เปลี่ยน {total_repl} ครั้ง ใน {total_files} ไฟล์ (ทั้งหมด {len(files)} ไฟล์)')
    print('>> ตรวจ diff ใน GitHub Desktop แล้วค่อย commit')

if __name__ == '__main__':
    main()

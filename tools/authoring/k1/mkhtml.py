# -*- coding: utf-8 -*-
"""แปลงเอกสารก้าว 1 เป็น HTML อ่านง่าย (MathJax เรนเดอร์ LaTeX ให้เห็นเป็นสูตรจริง)
   ⚠️ กัน markdown ไปยุ่งกับ $...$ ด้วยการแทนที่เป็น placeholder ก่อนแปลง แล้วค่อยใส่กลับ"""
import io, os, re, markdown

SRC = '/home/claude/k1/out/ก้าว1-ตัวอย่างตรีโกณ9ข้อ-ให้ครูเคาะระดับ-2026-08-04.md'
DST = '/home/claude/k1/out/ก้าว1-ตัวอย่างตรีโกณ9ข้อ-ให้ครูเคาะระดับ-2026-08-04.html'

raw = io.open(SRC, encoding='utf-8').read()

# ① เก็บทุกช่วง $...$ ออกมาก่อน (ไม่ให้ markdown แตะ _ หรือ * ข้างใน)
math = []
def stash(m):
    math.append(m.group(0))
    return '\x00MATH%d\x00' % (len(math) - 1)
protected = re.sub(r'\$[^$\n]+\$', stash, raw)
assert '$' not in protected, protected[protected.index('$') - 60:protected.index('$') + 60]

body = markdown.markdown(protected, extensions=['tables', 'nl2br'])

# ② ใส่สูตรกลับ
def restore(m):
    return math[int(m.group(1))]
body = re.sub(r'\x00MATH(\d+)\x00', restore, body)
assert '\x00' not in body

HTML = """<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ก้าว 1 · ตัวอย่างตรีโกณ 9 ข้อ ให้ครูเคาะระดับ</title>
<script>
window.MathJax = {
  tex: {inlineMath: [['$', '$']], displayMath: [['$$', '$$']]},
  options: {skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']}
};
</script>
<script id="MathJax-script">__MATHJAX__</script>
<style>
  body { font-family: "Sarabun", "Noto Sans Thai", "Segoe UI", sans-serif;
         max-width: 900px; margin: 0 auto; padding: 28px 20px 90px;
         line-height: 1.85; color: #1c1c1c; background: #fbfbf9; font-size: 17px; }
  h1 { font-size: 27px; border-bottom: 3px solid #2b6cb0; padding-bottom: 10px; }
  h2 { font-size: 22px; margin-top: 44px; border-left: 6px solid #2b6cb0;
       padding-left: 12px; background: #eef4fb; }
  h3 { font-size: 18px; margin-top: 26px; color: #2b4c6f; }
  table { border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 15px; }
  th, td { border: 1px solid #cfd8e0; padding: 7px 10px; text-align: left; vertical-align: top; }
  th { background: #eef4fb; }
  code { background: #eeeeea; padding: 1px 5px; border-radius: 4px; font-size: 14px; }
  hr { border: 0; border-top: 2px dashed #c9c9c4; margin: 40px 0; }
  blockquote { border-left: 5px solid #d69e2e; background: #fffaf0;
               margin: 18px 0; padding: 10px 16px; }
  ol > li { margin: 5px 0; }
  ul > li { margin: 5px 0; }
  .no-print { position: fixed; right: 14px; bottom: 14px; background: #2b6cb0; color: #fff;
              padding: 9px 15px; border-radius: 8px; font-size: 14px; box-shadow: 0 2px 8px #0003; }
  @media print { .no-print { display: none } body { background: #fff } }
</style>
</head>
<body>
__BODY__
<div class="no-print">พิมพ์ด้วย Ctrl+P ได้</div>
</body>
</html>
"""
# ③ ฝัง MathJax (แบบ SVG — ไม่ต้องโหลดฟอนต์จากเน็ต) ลงในไฟล์เลย
#    เพราะเครื่องครูอาจเปิดไฟล์แบบออฟไลน์ และ CDN ก็ถูกบล็อกในสภาพแวดล้อมนี้ด้วย
MJ = io.open('/home/claude/k1/node_modules/mathjax/es5/tex-mml-svg.js', encoding='utf-8').read()
assert '</script' not in MJ
out = HTML.replace('__BODY__', body).replace('__MATHJAX__', MJ)
io.open(DST, 'w', encoding='utf-8', newline='\n').write(out)
print('เขียน', os.path.basename(DST), '·', len(out.encode()), 'B ·', len(math), 'ช่วงสูตร')

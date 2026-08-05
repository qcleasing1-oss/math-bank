# -*- coding: utf-8 -*-
"""กวาดรอบหก — หา "ข้อยาก" ตัวใหม่แทน q073

เหตุที่ต้องทิ้ง q073 (แบบจำลองน้ำขึ้นน้ำลง + ถามเวลารวมที่ระดับเกินเกณฑ์)
  gen-chap-07-trigonometry-q047 (ชิงช้าสวรรค์ · รัศมี 18 · คาบ 8 นาที · สูงกว่า 30 ม.
  ใน 15 นาทีแรก รวมกี่นาที) เป็น **A เดียวกัน + M เดียวกัน** ต่างแค่ผิวเรื่อง
  ⇒ ⚠️ WATCH-A กับข้อของเราเอง ⇒ ไม่ผ่านมาตรฐานคุณภาพ ⇒ ออกแบบใหม่
"""
import io, json, glob, re, collections

items = []
for p in sorted(glob.glob('/tmp/mb27/data/sets/*.json') +
                glob.glob('/home/claude/k1/out/*.json') +
                glob.glob('/home/claude/k2/out/*.json')):
    d = json.load(io.open(p, encoding='utf-8'))
    for q in d.get('questions', []):
        q['_src'] = p.split('/')[-1].replace('.json', '')
        items.append(q)


def txt(q):
    parts = [q.get('question') or '']
    parts += [str(c) for c in (q.get('choices') or [])]
    ex = q.get('explanation') or ''
    parts += ex if isinstance(ex, list) else [str(ex)]
    for r in (q.get('rows') or []):
        parts += [str(r.get('text', '')), str(r.get('why', ''))]
    return '\n'.join(parts)


def scan(label, pattern, qonly=False, show=10):
    rx = re.compile(pattern)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-32s %-8s %-12s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:100]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

c = collections.Counter()
for q in items:
    if q['id'].startswith('gen-chap-07'):
        for s in (q.get('subTopics') or []):
            c[s] += 1
print('หัวข้อย่อยของข้อที่เราแต่งเอง :', dict(sorted(c.items())))

scan('T1 · เส้นแบ่งครึ่งมุมภายใน (ยิงตรงอีกครั้ง)',
     r'แบ่งครึ่งมุม|เส้นแบ่งครึ่งมุม|BD\s*แบ่งมุม|แบ่งมุม\s*\$?[A-Z]')
scan('T2 · ช่วงของพารามิเตอร์ที่ทำให้สมการตรีโกณ "มีคำตอบ"',
     r'มีคำตอบ[\s\S]{0,60}?(?:ค่าของ\s*\$?k|พารามิเตอร์)|'
     r'ที่ทำให้สมการ[\s\S]{0,80}?มีคำตอบ|สมการ[\s\S]{0,100}?มีคำตอบ[\s\S]{0,20}?เมื่อ')
scan('T3 · สมการรูป sin(mx) = cos(nx) (ใช้มุมประกอบ/โคฟังก์ชัน)',
     r'\\sin\s*\(?\s*\d?\s*x\s*\)?\s*=\s*\\cos|\\cos\s*\(?\s*\d?\s*x\s*\)?\s*=\s*\\sin')
scan('T4 · เซกเตอร์/ส่วนโค้ง ผสมกับสามเหลี่ยม (พื้นที่ส่วนที่เหลือ)',
     r'เซกเตอร์[\s\S]{0,120}?สามเหลี่ยม|สามเหลี่ยม[\s\S]{0,120}?เซกเตอร์|'
     r'พื้นที่ส่วนที่แรเงา|เสี้ยววงกลม|segment ของวงกลม')
scan('T5 · อัตราเร็วเชิงมุม / ล้อหมุน / รอบต่อนาที + ความยาวส่วนโค้ง',
     r'อัตราเร็วเชิงมุม|รอบต่อนาที|รอบต่อวินาที|เรเดียนต่อวินาที|ล้อ[\s\S]{0,60}?รัศมี')
scan('T6 · สมการที่มีค่าสัมบูรณ์ของฟังก์ชันตรีโกณ',
     r'\\left\|\s*\\(?:sin|cos|tan)|\|\\(?:sin|cos|tan)\s*x\s*\|', qonly=True)
scan('T7 · มุมภายนอก / มุมประกอบสองมุมของสามเหลี่ยม + กฎของไซน์',
     r'มุมภายนอก[\s\S]{0,80}?สามเหลี่ยม|ต่อด้าน[\s\S]{0,60}?ออกไป')
scan('T8 · ให้ tan ของสองมุมในสามเหลี่ยม ⇒ หามุมที่สาม / ด้าน',
     r'\\tan\s*A\s*=[\s\S]{0,60}?\\tan\s*B\s*=|\\tan\s*A[\s\S]{0,40}?\\tan\s*B[\s\S]{0,40}?\\tan\s*C')
scan('T9 · สามเหลี่ยมสองรูปที่ใช้ด้านร่วม แล้วถามด้านของรูปที่สอง (กฎ sin ต่อกฎ cos)',
     r'ด้านร่วม|ใช้ด้าน[\s\S]{0,40}?ร่วมกัน|จุด\s*\$?D\$?\s*อยู่บนด้าน|จุด\s*\$?D\$?\s*บนด้าน')
scan('T10 · ค่าสูงสุด-ต่ำสุดของ a sin^2 + b cos + c (ยุบเป็นกำลังสองของ cos)',
     r'ค่าสูงสุด[\s\S]{0,80}?\\sin\^\{?2\}?|\\sin\^\{?2\}?[\s\S]{0,60}?\+[\s\S]{0,30}?\\cos\s*x'
     r'[\s\S]{0,60}?(?:ค่าสูงสุด|ค่าต่ำสุด)')

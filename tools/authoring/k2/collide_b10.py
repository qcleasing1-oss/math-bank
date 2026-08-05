# -*- coding: utf-8 -*-
"""กวาดคลังก่อนแต่งก้อน 10 · เจาะ 7.5 / 7.6 / 7.7 ซึ่งยังบางมาก (4 / 4 / 3 ข้อ)

แม่พิมพ์ที่คิดไว้
  q055 7.5+7.7 · a sin x + b cos x = k · ถามช่วงของ k ที่ทำให้มีคำตอบตามจำนวนที่กำหนด
  q056 7.6     · ครึ่งมุม · ให้ tan ของมุมใหญ่ + จตุภาค ⇒ หา tan ครึ่งมุม (ต้องตัดสินจตุภาคของครึ่งมุมเอง)
  q057 7.7     · ผลบวกของคำตอบทั้งหมดในช่วง (ไม่ใช่ตัวคำตอบ)
  q058 7.7     · สมการที่ยกกำลังสองแล้วเกิดรากปลอม ⇒ ถามจำนวนคำตอบจริง
  q059 7.6     · ผลคูณโคไซน์ที่ยุบด้วยสูตรมุมสองเท่า (telescoping)
"""
import io, json, glob, re

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


def scan(label, pattern, qonly=False, show=8):
    rx = re.compile(pattern)
    hit = [q for q in items if rx.search((q.get('question') or '') if qonly else txt(q))]
    print()
    print('== %s ==  %d ข้อ' % (label, len(hit)))
    for q in hit[:show]:
        print('   %-30s %-8s %-10s %s' % (q['id'], q.get('difficulty', '?'),
              '/'.join(q.get('subTopics') or []), (q.get('question') or '').replace('\n', ' ')[:110]))
    if len(hit) > show:
        print('   ... อีก %d' % (len(hit) - show))
    return hit


print('ฐานเทียบ %d ข้อ' % len(items))

scan('q055a · a sin + b cos ผสมกัน (R-formula / มุมช่วย)',
     r'\\sin\s*x\s*[+\-]\s*\d*\s*\\?\\cos\s*x|\\sqrt\{a\^2\s*\+\s*b\^2\}|มุมช่วย|R\s*\\sin')
scan('q055b · ถามค่า k ที่ทำให้สมการมีคำตอบ (พารามิเตอร์ฝั่งขวา)',
     r'(?:มีคำตอบ|มีรากคำตอบ|มีจำนวนคำตอบ)[\s\S]{0,80}?(?:กี่|ค่าของ|ช่วงใด|เท่าใด)', qonly=True)

scan('q056 · ครึ่งมุม tan(theta/2)',
     r'\\tan\s*\\?(?:frac|dfrac)?\s*\{?\\?theta\s*\}?\s*\{?2|\\tan\\frac\{\\theta\}\{2\}|ครึ่งมุม|\\frac\{\\theta\}\{2\}|\\dfrac\{\\theta\}\{2\}')
scan('q056b · โจทย์ที่ถามค่าตรีโกณของครึ่งมุม', r'(?:\\frac|\\dfrac)\{[A-Za-z\\]+\}\{2\}', qonly=True)

scan('q057 · ผลบวกของคำตอบทั้งหมด (sum of roots) ของสมการตรีโกณ',
     r'ผลบวกของ(?:คำตอบ|ค่า|รากคำตอบ|ทุกคำตอบ)', qonly=True, show=12)

scan('q058 · จำนวนคำตอบของสมการตรีโกณในช่วง',
     r'(?:สมการ|\\sin|\\cos|\\tan)[\s\S]{0,140}?มีคำตอบ(?:ทั้งหมด)?กี่', qonly=True, show=12)
scan('q058b · รากปลอมจากการยกกำลังสอง', r'รากปลอม|คำตอบปลอม|ต้องตรวจคำตอบกลับ|extraneous')

scan('q059 · ผลคูณโคไซน์แบบยุบด้วยมุมสองเท่า',
     r'\\cos[\s\S]{0,10}20[\s\S]{0,30}\\cos[\s\S]{0,10}40|\\cos\s*20\^|\\cos 36\^|\\cos\s*\\frac\{\\pi\}\{7\}')
scan('q059b · โจทย์ที่เป็นผลคูณของฟังก์ชันตรีโกณสามตัวขึ้นไป',
     r'(?:\\sin|\\cos)[^\n]{0,25}(?:\\sin|\\cos)[^\n]{0,25}(?:\\sin|\\cos)[^\n]{0,25}(?:\\sin|\\cos)', qonly=True)

#!/usr/bin/env node
/* check_export_figures.js — ด่านที่ 12: viewer/export.js ต้องเลือกรูปเหมือน viewer/admin.html
 *
 * ⚠️ ชื่อไฟล์ต้องขึ้นต้นด้วย check_ เสมอ — ⛔ ห้ามเปลี่ยนเป็น test_ หรืออย่างอื่น
 *    เหตุผล: กฎ ⑦ก ของด่าน 11 ("ตัวตรวจที่ไม่มีใครเรียก = ตัวตรวจที่ไม่มีอยู่จริง")
 *    เลือกไฟล์ที่จะเฝ้าโดยดูจากคำนำหน้า check_ ⇒ ตั้งชื่ออย่างอื่น = หลุดจากด่าน 11 เงียบ ๆ
 *    (ร่างแรกของไฟล์นี้ชื่อ test_export_figures.js — ซึ่งไม่มีใครเฝ้าเลย ทั้งที่ตั้งใจให้เป็นด่าน)
 *
 * ทำไมต้องมีด่านนี้ (ที่มา 2 ส.ค. 69):
 *   admin.html กับ export.js ตัดสิน "รูปไหนอยู่โจทย์ รูปไหนอยู่เฉลย" คนละที่ คนละสำเนา
 *   วันที่เขียนด่านนี้ ทั้งสองต่างกันจริง 2 จุด และจุดแรกกัดข้อสอบจริงอยู่ 8 ข้อ
 *   ⇒ ปัญหาไม่ใช่ "โค้ดผิด" แต่คือ "กฎเดียวกันถูกเก็บสองที่" — ด่านนี้คือรอยเชื่อม
 *
 * 🔴 ทำไมด่านนี้ไม่ใช่การเขียนตรรกะเดิมซ้ำ (กับดัก ⑦ข — เขียวเพราะด่านไหนกันแน่):
 *   ของที่ถูกทดสอบ = ไบต์จริงของ viewer/export.js — โหลดผ่าน vm แล้วเรียก window.doExport()
 *   จริง ๆ ไม่ใช่ก๊อปฟังก์ชันมาวางในเทสต์ · getMarkedIndices ก็ดึงซอร์สจริงจาก admin.html
 *   ส่วน "เฉลย" (oracle) ที่เอามาเทียบ เป็นการเขียนกฎซ้ำ — ซึ่งจะเพี้ยนจาก admin.html ได้
 *   ⇒ จึงมี §A ตรึงข้อความซอร์สของ admin.html ไว้ ถ้า admin.html เปลี่ยนกฎ ด่านนี้แดงทันที
 *
 * exit 0 = ผ่าน · 1 = เนื้อหาแดง (export.js เลือกรูปต่างจาก admin) · 2 = เครื่องมือแดง
 * ⑨ ทุกตัวเลขที่พิมพ์ต้องมีตัวหารกำกับ
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const REPO = process.argv[2] || path.resolve(__dirname, '..');
const P_EXPORT = path.join(REPO, 'viewer', 'export.js');
const P_ADMIN = path.join(REPO, 'viewer', 'admin.html');
const P_SETS = path.join(REPO, 'data', 'sets');

let RED = 0;
const fail = (m) => { RED++; console.log('  ✗ ' + m); };
const ok = (m) => console.log('  ✓ ' + m);
function tool(msg) { console.log('\n🔧 เครื่องมือแดง: ' + msg); process.exit(2); }

for (const p of [P_EXPORT, P_ADMIN, P_SETS]) {
  if (!fs.existsSync(p)) tool('ไม่พบ ' + p);
}
const EXPORT_SRC = fs.readFileSync(P_EXPORT, 'utf8');
const ADMIN_SRC = fs.readFileSync(P_ADMIN, 'utf8');

console.log('═'.repeat(66));
console.log('ด่าน 12 · export.js ต้องเลือกรูปเหมือน admin.html');
console.log('═'.repeat(66));

/* ─────────────────────────────────────────────────────────────
   §A ตรึงกฎฝั่ง admin.html — ถ้าที่นั่นเปลี่ยน ด่านนี้ต้องแดง
   (ไม่ใช่เงียบแล้วปล่อยให้ oracle ล้าสมัย)
   ───────────────────────────────────────────────────────────── */
console.log('\n§A ตรึงข้อความกฎใน admin.html (ตัวหาร: 3 ชิ้นที่ต้องเจอ)');
const PINS = [
  ['_getSpecByIdx การ์ด idx===0', /return\s+idx\s*===\s*0\s*\?\s*imageSpec\s*:\s*null\s*;/],
  ['ตัวกรองรูปโจทย์ (ลิสต์)', /filter\(\(s,\s*i\)\s*=>\s*!_markedIdx\.has\(i\)\s*\|\|\s*\(s\s*&&\s*s\.inQuestion\)\)/],
  ['ตัวกรองรูปโจทย์ (dict)', /!_markedIdx\.has\(0\)\s*\|\|\s*\(q\.imageSpec\s*&&\s*q\.imageSpec\.inQuestion\)/],
];
let pinsFound = 0;
const pinsLost = [];
for (const [name, re] of PINS) {
  if (re.test(ADMIN_SRC)) { pinsFound++; ok(name + ' — ยังตรงกับที่ด่านนี้สมมติไว้'); }
  else { pinsLost.push(name); console.log('  ✗ ' + name + ' — admin.html เปลี่ยนกฎแล้ว'); }
}
console.log('  ⇒ เจอ ' + pinsFound + ' / ' + PINS.length + ' ชิ้น');

/* 🔴 หมุดหลุดแม้ชิ้นเดียว = "เครื่องมือแดง" (2) ⛔ ไม่ใช่ "เนื้อหาแดง" (1)
 *    และต้องหยุดตรงนี้ ⛔ ห้ามเดินต่อไป §B–§D
 *
 *    ที่มา: จับได้ตอนรันด่านนี้กับ admin.html ที่ดัดแปลงไว้ทดสอบ (2 ส.ค. 69)
 *    ร่างแรกนับหมุดหลุดเป็น fail() ธรรมดาแล้วเดินต่อ ⇒ ผลที่พิมพ์ออกมาจริงคือ
 *      ✗ ตัวกรองรูปโจทย์ (ลิสต์) — admin.html เปลี่ยนกฎแล้ว
 *      ✓ export.js เลือกรูปตรงกับ admin.html ทุกข้อ — 2150 / 2150   ← ⛔ บรรทัดนี้โกหก
 *    บรรทัดเขียวนั้นเทียบกับ oracle ที่ ⛔ ไม่ใช่กฎของ admin.html อีกต่อไปแล้ว
 *    ⇒ กับดัก ⑨ เต็มรูปแบบ: "เครื่องมือที่ตอบถูกตามตัวหารของมัน ยังตอบผิดตามคำถามของคุณได้"
 *      ตัวหารของมัน = oracle ที่แช่ไว้ · คำถามจริง = "วันนี้ export.js ตรงกับ admin.html ไหม"
 *    ⇒ และเป็นกับดัก ⑦ข ด้วย: เขียวเพราะด่านไหนกันแน่ — เขียวเพราะกฎเก่า ไม่ใช่เพราะของตรงกัน
 *
 *    ⚠️ ทำไมต้องเป็น 2 ไม่ใช่ 1: รหัส 1 แปลว่า "ของที่ถูกตรวจผิด" ซึ่งชี้คนไปแก้ export.js
 *       แต่สถานะจริงคือ "ด่านนี้ตัดสินไม่ได้แล้ว" — คนที่ต้องขยับคือคนอัปเดต oracle ในไฟล์นี้
 *       (กฎทั่วไป: ทุกด่านต้องมีกิ่ง "ไม่มีอะไรให้ตรวจ / ตรวจไม่ได้" ที่คืน 2)
 */
if (pinsLost.length) {
  tool('หมุดกฎใน admin.html หลุด ' + pinsLost.length + ' / ' + PINS.length + ' ชิ้น'
    + ' — ' + pinsLost.join(' · ')
    + '\n   ⇒ oracle ในไฟล์นี้ไม่ได้เป็นตัวแทนของ admin.html อีกต่อไป'
    + '\n   ⛔ จึงหยุดก่อนถึง §B–§D: ตัวเลข “ตรงกัน N/N” ที่คำนวณจาก oracle ที่ล้าแล้ว'
    + ' คือคำตอบที่ถูกตามตัวหารของมัน แต่ผิดตามคำถามที่เราถาม (กับดัก ⑨/⑦ข)'
    + '\n   วิธีแก้: อ่านกฎใหม่ใน viewer/admin.html แล้วอัปเดตทั้ง PINS และ oracle ในไฟล์นี้'
    + ' ให้ตรงกัน ⛔ ห้ามลบหมุดทิ้งเพื่อให้ด่านเงียบ');
}

/* ─────────────────────────────────────────────────────────────
   §B ดึง getMarkedIndices ตัวจริงจาก admin.html มาใช้ (ไม่เขียนใหม่)
   ───────────────────────────────────────────────────────────── */
const gmiMatch = ADMIN_SRC.match(/function getMarkedIndices\(explanation\)\s*\{[\s\S]*?\n  \}/);
if (!gmiMatch) tool('ดึงซอร์ส getMarkedIndices จาก admin.html ไม่ได้');
const getMarkedIndices = vm.runInNewContext(gmiMatch[0] + '; getMarkedIndices');

/* ─────────────────────────────────────────────────────────────
   §C oracle — กฎที่ตรึงไว้ใน §A เขียนเป็นโค้ด
   ───────────────────────────────────────────────────────────── */
function oracleQuestionSpecs(q) {
  const marked = getMarkedIndices(q.explanation);
  if (!q.imageSpec) return [];
  if (Array.isArray(q.imageSpec)) {
    return q.imageSpec.filter((s, i) => !marked.has(i) || (s && !Array.isArray(s) && s.inQuestion));
  }
  return (!marked.has(0) || q.imageSpec.inQuestion) ? [q.imageSpec] : [];
}

/* ─────────────────────────────────────────────────────────────
   §D โหลด export.js ตัวจริงเข้า sandbox แล้วเรียก doExport() จริง
   ───────────────────────────────────────────────────────────── */
function runExport(setId, questions, withAns) {
  const captured = { html: null, name: null };
  const el = (v) => ({ value: v });
  const ctx = {
    console,
    CURRENT_SET: setId,
    LOADED_SETS: { [setId]: { questions } },
    MANIFEST: { sets: { [setId]: { displayName: setId } } },
    getMarkedIndices,
    escapeHtml: (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'),
    setLabel: (s) => (s && s.displayName) || '',
    // renderImage ปลอม: ไม่วาด SVG จริง แค่บอกว่า "ถูกเรียกด้วย spec ตัวไหน"
    // ⇒ ด่านนี้ตรวจ *การเลือกรูป* ไม่ใช่ *การวาดรูป* (คนละด่าน คนละตัวหาร)
    renderImage: function rimg(spec) {
      if (!spec) return null;
      if (Array.isArray(spec)) {
        const parts = spec.map(rimg).filter(Boolean);
        return parts.length ? parts.join('') : null;
      }
      return '«FIG:' + (spec.__tag != null ? spec.__tag : '?') + '»';
    },
    Blob: function (a) { this.parts = a; },
    URL: { createObjectURL: () => 'blob:x', revokeObjectURL: () => {} },
    alert: (m) => { throw new Error('export.js เรียก alert: ' + m); },
    setTimeout: () => {},
    document: {
      querySelector: (sel) => sel.indexOf('exp-fmt') >= 0 ? el('word') : el(withAns ? 'full' : 'q'),
      getElementById: () => ({ hidden: true, textContent: '' }),
      createElement: () => ({ click() {}, set href(v) {}, set download(v) { captured.name = v; } }),
      body: { appendChild(a) {}, removeChild(a) {} },
    },
  };
  ctx.window = ctx;
  ctx.Blob.prototype = {};
  // ดัก _download ผ่าน Blob: เนื้อไฟล์คือ args ตัวแรกของ new Blob([...])
  const origBlob = ctx.Blob;
  ctx.Blob = function (parts) { captured.html = String(parts[0]); return new origBlob(parts); };
  vm.createContext(ctx);
  vm.runInContext(EXPORT_SRC, ctx, { filename: 'viewer/export.js' });
  if (typeof ctx.window.doExport !== 'function') tool('โหลด export.js แล้วไม่มี window.doExport');
  ctx.window.doExport();
  if (captured.html == null) tool('เรียก doExport() แล้วไม่ได้เนื้อไฟล์กลับมา');
  return captured.html;
}

// แยกรูปฝั่งโจทย์ ออกจากรูปฝั่งเฉลย (เฉลยอยู่ใน div.exp-sol)
function figsOf(html) {
  const perQ = html.split('<div class="exp-q">').slice(1);
  return perQ.map((chunk) => {
    const cut = chunk.indexOf('<div class="exp-sol">');
    const head = cut >= 0 ? chunk.slice(0, cut) : chunk;
    const tail = cut >= 0 ? chunk.slice(cut) : '';
    const grab = (s) => (s.match(/«FIG:([^»]*)»/g) || []).map((x) => x.slice(5, -1));
    return { q: grab(head), e: grab(tail), warn: (head + tail).match(/exp-fig-missing/g) || [] };
  });
}

/* ─────────────────────────────────────────────────────────────
   §E เดินคลังจริงทั้งหมด
   ───────────────────────────────────────────────────────────── */
console.log('\n§B เทียบทีละข้อบนคลังจริง');
const files = fs.readdirSync(P_SETS).filter((f) => f.endsWith('.json')).sort();
if (files.length === 0) tool('data/sets ไม่มีไฟล์ .json สักไฟล์ (ตัวหาร 0) — ไม่มีอะไรให้ตรวจ');

let nQ = 0, nFig = 0, nMismatch = 0, nInQ = 0, nInQok = 0;
const mismatches = [];
for (const fn of files) {
  const d = JSON.parse(fs.readFileSync(path.join(P_SETS, fn), 'utf8'));
  const qs = (d.questions || []).filter((q) => q && q.imageSpec);
  if (!qs.length) continue;
  // ติดป้าย __tag ให้ทุก spec เพื่อรู้ว่ารูปไหนถูกเลือก
  const tagged = qs.map((q, qi) => {
    const c = JSON.parse(JSON.stringify(q));
    const els = Array.isArray(c.imageSpec) ? c.imageSpec : [c.imageSpec];
    els.forEach((s, i) => { if (s && !Array.isArray(s)) s.__tag = qi + '.' + i; });
    return c;
  });
  const html = runExport(fn.replace(/\.json$/, ''), tagged, false); // ใบ "เฉพาะโจทย์"
  const got = figsOf(html);
  if (got.length !== tagged.length) tool('จำนวนบล็อกข้อที่ export.js พิมพ์ (' + got.length + ') ไม่เท่าจำนวนข้อที่ป้อน (' + tagged.length + ') ในไฟล์ ' + fn);
  tagged.forEach((q, qi) => {
    nQ++;
    const want = oracleQuestionSpecs(q).map((s) => (s && !Array.isArray(s)) ? s.__tag : '?');
    nFig += want.length;
    const els = Array.isArray(q.imageSpec) ? q.imageSpec : [q.imageSpec];
    const hasInQ = els.some((s) => s && !Array.isArray(s) && s.inQuestion);
    const mine = got[qi].q.filter((t) => t !== '?');
    // ⚠️ ต้องนับจาก mine (ผลจริงของ export.js) ไม่ใช่ want (เฉลยของด่านเอง)
    //    ถ้านับจาก want บรรทัดนี้จะเขียวตลอดกาล ไม่ว่า export.js จะทำอะไร — กับดัก ⑦ข
    if (hasInQ) { nInQ++; if (mine.length) nInQok++; }
    if (JSON.stringify(mine) !== JSON.stringify(want.filter((t) => t !== '?'))) {
      nMismatch++;
      if (mismatches.length < 12) mismatches.push(q.id + ' — admin ว่า [' + want + '] · export ว่า [' + mine + ']');
    }
  });
}
if (nQ === 0) tool('เดินคลังแล้วไม่เจอข้อที่มี imageSpec สักข้อ (ตัวหาร 0) — ไม่มีอะไรให้ตรวจ');

if (nMismatch === 0) ok('export.js เลือกรูปตรงกับ admin.html ทุกข้อ — ' + nQ + ' / ' + nQ + ' ข้อที่มีรูป (' + nFig + ' จุดที่ควรอยู่ในโจทย์)');
else { fail('เลือกรูปต่างกัน ' + nMismatch + ' / ' + nQ + ' ข้อที่มีรูป'); mismatches.forEach((m) => console.log('      · ' + m)); }

if (nInQ === 0) tool('คลังไม่มีข้อที่ตั้ง inQuestion เลย (ตัวหาร 0) — ด่านนี้จะเขียวโดยไม่ได้ตรวจอะไร');
if (nInQok === nInQ) ok('ข้อที่ตั้ง inQuestion ได้รูปในใบโจทย์ครบ — ' + nInQok + ' / ' + nInQ + ' ข้อ');
else fail('ข้อที่ตั้ง inQuestion แต่ใบโจทย์ยังไม่มีรูป ' + (nInQ - nInQok) + ' / ' + nInQ + ' ข้อ');

/* ─────────────────────────────────────────────────────────────
   §F เคสสังเคราะห์ — ต้องแดงถ้าเอาการ์ดออก (mutant)
   ───────────────────────────────────────────────────────────── */
console.log('\n§C เคสที่แต่งขึ้น (ตัวหาร: 5 เคส)');
const F = (tag, extra) => Object.assign({ type: 'function-plot', __tag: tag }, extra || {});
const CASES = [
  { name: 'dict + [IMAGE:0] ไม่มี inQuestion ⇒ โจทย์ไม่มีรูป',
    q: { id: 't1', questionNumber: 1, question: 'x', imageSpec: F('a'), explanation: ['[IMAGE:0]'] },
    wantQ: [], wantE: ['a'], wantWarn: 0 },
  { name: 'dict + [IMAGE:0] + inQuestion ⇒ โจทย์มีรูป และเฉลยก็มี',
    q: { id: 't2', questionNumber: 2, question: 'x', imageSpec: F('b', { inQuestion: true }), explanation: ['[IMAGE:0]'] },
    wantQ: ['b'], wantE: ['b'], wantWarn: 0 },
  { name: '🔴 dict + [IMAGE:7] ⇒ ต้องขึ้นป้ายเตือน ไม่ใช่คืนรูป 0 เงียบ ๆ',
    q: { id: 't3', questionNumber: 3, question: 'x', imageSpec: F('c'), explanation: ['[IMAGE:7]'] },
    wantQ: ['c'], wantE: [], wantWarn: 1 },
  { name: 'ลิสต์ 2 รูป หมุดตัวที่ 1 ตัวเดียว ⇒ โจทย์เหลือรูป 0',
    q: { id: 't4', questionNumber: 4, question: 'x', imageSpec: [F('d0'), F('d1')], explanation: ['[IMAGE:1]'] },
    wantQ: ['d0'], wantE: ['d1'], wantWarn: 0 },
  { name: 'ลิสต์ 2 รูป หมุดครบ แต่ตัวที่ 1 ตั้ง inQuestion ⇒ โจทย์ได้เฉพาะตัวที่ 1',
    q: { id: 't5', questionNumber: 5, question: 'x', imageSpec: [F('e0'), F('e1', { inQuestion: true })], explanation: ['[IMAGE:0]', '[IMAGE:1]'] },
    wantQ: ['e1'], wantE: ['e0', 'e1'], wantWarn: 0 },
];
const synthHtml = runExport('synthetic', CASES.map((c) => c.q), true); // ใบ "พร้อมเฉลย"
const synth = figsOf(synthHtml);
if (synth.length !== CASES.length) tool('เคสสังเคราะห์: พิมพ์ออกมา ' + synth.length + ' บล็อก จาก ' + CASES.length + ' เคส');
CASES.forEach((c, i) => {
  const g = synth[i];
  const bad = [];
  if (JSON.stringify(g.q) !== JSON.stringify(c.wantQ)) bad.push('โจทย์ได้ [' + g.q + '] ควรเป็น [' + c.wantQ + ']');
  if (JSON.stringify(g.e) !== JSON.stringify(c.wantE)) bad.push('เฉลยได้ [' + g.e + '] ควรเป็น [' + c.wantE + ']');
  if (g.warn.length !== c.wantWarn) bad.push('ป้ายเตือน ' + g.warn.length + ' ควรเป็น ' + c.wantWarn);
  if (bad.length) fail(c.name + ' → ' + bad.join(' · '));
  else ok(c.name);
});

/* ─────────────────────────────────────────────────────────────
   §G ใบ JSON ก็ต้องเก็บรูป inQuestion ไว้ (คนละเส้นทางกับใบพิมพ์)
   ───────────────────────────────────────────────────────────── */
console.log('\n§D เส้นทาง JSON (ตัวหาร: 2 เคส)');
{
  const ctxCases = [
    { name: 'JSON เฉพาะโจทย์: รูปที่หมุดแล้วไม่มี inQuestion ⇒ ต้องถูกตัดออก',
      q: { id: 'j1', questionNumber: 1, question: 'x', imageSpec: F('j1'), explanation: ['[IMAGE:0]'] }, wantHas: false },
    { name: 'JSON เฉพาะโจทย์: รูปที่หมุดแล้วตั้ง inQuestion ⇒ ต้องอยู่ต่อ',
      q: { id: 'j2', questionNumber: 2, question: 'x', imageSpec: F('j2', { inQuestion: true }), explanation: ['[IMAGE:0]'] }, wantHas: true },
  ];
  for (const c of ctxCases) {
    let out = null;
    const ctx = {
      console, CURRENT_SET: 's', LOADED_SETS: { s: { questions: [c.q] } },
      MANIFEST: { sets: { s: {} } }, getMarkedIndices,
      escapeHtml: String, setLabel: () => '', renderImage: () => '<svg/>',
      URL: { createObjectURL: () => 'blob:x', revokeObjectURL: () => {} },
      alert: (m) => { throw new Error(m); }, setTimeout: () => {},
      Blob: function (parts) { out = String(parts[0]); },
      document: {
        querySelector: (sel) => ({ value: sel.indexOf('exp-fmt') >= 0 ? 'json' : 'q' }),
        getElementById: () => ({ hidden: true, textContent: '' }),
        createElement: () => ({ click() {}, set href(v) {}, set download(v) {} }),
        body: { appendChild() {}, removeChild() {} },
      },
    };
    ctx.window = ctx;
    vm.createContext(ctx);
    vm.runInContext(EXPORT_SRC, ctx, { filename: 'viewer/export.js' });
    ctx.window.doExport();
    if (out == null) tool('เส้นทาง JSON ไม่คืนเนื้อไฟล์');
    const has = out.indexOf('"imageSpec"') >= 0;
    if (has === c.wantHas) ok(c.name);
    else fail(c.name + ' → ' + (has ? 'ยังมี imageSpec' : 'ไม่มี imageSpec'));
    if (out.indexOf('"explanation"') >= 0 || out.indexOf('"correct"') >= 0 || out.indexOf('"accept"') >= 0)
      fail('ใบ JSON เฉพาะโจทย์หลุดเฉลย/คำตอบออกไป (' + c.q.id + ')');
  }
}

console.log('\n' + '═'.repeat(66));
if (RED === 0) { console.log('✅ ผ่านทั้งหมด — ' + nQ + ' ข้อจากคลังจริง + 7 เคสที่แต่งขึ้น'); process.exit(0); }
console.log('🔴 แดง ' + RED + ' รายการ'); process.exit(1);

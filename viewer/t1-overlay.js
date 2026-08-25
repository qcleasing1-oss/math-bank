/* ============================================================================
   t1-overlay.js — โชว์ "เฉลยละเอียด t1" ในวิวเวอร์เดิม + ปุ่มกรอง
   ----------------------------------------------------------------------------
   ⛔ ไฟล์นี้ ⛔ ไม่แก้ตรรกะเดิมของ admin.html เลย — ห่อ (wrap) ฟังก์ชันเดิมเท่านั้น
   ⛔ ⛔ ไม่แตะ renderers.js · ⛔ ไม่แตะไฟล์ข้อมูล
   แตะ admin.html แค่ **1 บรรทัด** = <script defer src="t1-overlay.js"></script>
   ถ้าลบบรรทัดนั้นออก วิวเวอร์กลับเป็นของเดิมเป๊ะ ⇒ ถอนได้ทันทีถ้า MB ไม่เอา
   E-lane · 24 ส.ค. 2569
   ============================================================================ */
(function () {
  'use strict';

  var T1 = null;                 // { id: t1record }
  var READY = false;
  var MODE = 'all';              // all | t1 | t1img
  var SRC = '../_t1run/t1_index.json';

  /* ---------- helper: escape + คณิต ---------- */
  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  var _DL = /\$|\\\(|\\\[/;
  var _TEX = /\\[a-zA-Z]{2,}|[_^]\{|\\\\|[_^][0-9a-zA-Z](?![a-zA-Z])/;
  function _stripText(s) {
    return s.replace(/\\(?:text|mathrm|textbf|textit|operatorname)\s*\{[^{}]*\}/g, '');
  }
  // สูตรบางบรรทัดในข้อมูลลืมใส่ตัวคั่น $…$ ⇒ KaTeX มองไม่เห็น ⇒ โผล่เป็นโค้ดดิบ
  function autodelim(s, isEq) {
    if (typeof s !== 'string') return s;
    var t = s.trim();
    if (!t || _DL.test(t) || !_TEX.test(t)) return s;
    if (isEq) return '$$' + t + '$$';
    return /^[\x20-\x7E]+$/.test(_stripText(t)) ? '$$' + t + '$$' : s;
  }
  function md(s, isEq) {
    return esc(autodelim(s, isEq)).replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>');
  }
  function ul(a) {
    return '<ul class="t1-ul">' + a.map(function (x) { return '<li>' + md(x) + '</li>'; }).join('') + '</ul>';
  }

  /* ---------- helper: ข้อมูลบางข้อส่ง string มาแทน array ⇒ .map ระเบิด ---------- */
  function arr(v) { return v == null ? [] : (Array.isArray(v) ? v : [v]); }
  function normT1(t) {
    if (!t || typeof t !== 'object') return null;
    var o = {}, k; for (k in t) o[k] = t[k];
    o.kb_ref = arr(o.kb_ref); o.given = arr(o.given); o.hints = arr(o.hints); o.technique = arr(o.technique);
    o.traps = arr(o.traps).filter(function (x) { return x && typeof x === 'object'; });
    o.steps = arr(o.steps).filter(function (x) { return x && typeof x === 'object'; }).map(function (s) {
      var q = {}, kk; for (kk in s) q[kk] = s[kk]; q.work = arr(q.work); return q;
    });
    if (o.verify && typeof o.verify === 'object') {
      var v = {}, k2; for (k2 in o.verify) v[k2] = o.verify[k2]; v.lines = arr(v.lines); o.verify = v;
    } else if (o.verify != null) { o.verify = { how: String(o.verify), lines: [], result: '' }; }
    return o;
  }

  /* ---------- รูป: ยืมสเปกเดียวกับเฉลยเดิม (สคีมา t1 ⛔ ไม่มีฟิลด์รูป) ---------- */
  function svgOf(spec) {
    try {
      if (typeof _renderSpecToSvg === 'function') return _renderSpecToSvg(spec);
      if (typeof renderImage === 'function') return renderImage(spec);
    } catch (e) {}
    return null;
  }
  function t1Figure(sp) {
    if (!sp) return '';
    var a = Array.isArray(sp) ? sp : [sp], out = '', i, g;
    for (i = 0; i < a.length; i++) {
      if (!a[i]) continue;
      g = svgOf(a[i]);
      if (g) out += '<div class="t1-img">' + g + '</div>';
    }
    if (!out) return '';
    return '<div class="t1-sec t1-figsec"><div class="t1-h">🖼 รูปประกอบ '
         + '<span class="t1-tag">ยืมจากเฉลยเดิม</span></div>' + out + '</div>';
  }

  /* ---------- ตัวเฉลยละเอียด ---------- */
  function renderT1(t, sp) {
    try { t = normT1(t); } catch (e) {
      return '<div class="t1-none">🔴 ข้อมูลข้อนี้ผิดรูป — ' + esc(String(e)) + '</div>';
    }
    if (!t) return '';
    var h = '';
    h += t1Figure(sp);
    if (t.kb_ref.length) h += '<div class="t1-sec"><div class="t1-h">📚 ความรู้พื้นฐานที่ใช้</div><div class="t1-chips">'
      + t.kb_ref.map(function (k) { return '<span class="t1-chip">' + esc(k) + '</span>'; }).join('') + '</div></div>';
    if (t.given.length) h += '<div class="t1-sec"><div class="t1-h">📥 โจทย์ให้อะไรมา</div>' + ul(t.given) + '</div>';
    if (t.goal) h += '<div class="t1-sec"><div class="t1-h">🎯 เป้าหมาย</div><div class="t1-goal">' + md(t.goal) + '</div></div>';
    if (t.steps.length) {
      h += '<div class="t1-sec"><div class="t1-h">🪜 ขั้นตอน</div>';
      t.steps.forEach(function (s) {
        h += '<div class="t1-step"><div class="t1-st"><span class="t1-n">' + esc(s.n) + '</span>' + md(s.title) + '</div>';
        if (s.formula) h += '<div class="t1-row"><div class="t1-lab">สูตรที่ใช้</div>' + md(s.formula) + '</div>';
        if (s.why)     h += '<div class="t1-row"><div class="t1-lab">ทำไมต้องทำขั้นนี้</div>' + md(s.why) + '</div>';
        if (s.work.length) h += '<div class="t1-row"><div class="t1-lab">ลงมือ</div>' + ul(s.work) + '</div>';
        if (s.eq)      h += '<div class="t1-eq">' + md(s.eq, 1) + '</div>';
        if (s.check)   h += '<div class="t1-check">🔎 ' + md(s.check) + '</div>';
        h += '</div>';
      });
      h += '</div>';
    }
    if (t.verify) {
      h += '<div class="t1-sec"><div class="t1-h">✅ ตรวจคำตอบด้วยวิธีอื่น</div><div class="t1-verify">';
      if (t.verify.how) h += '<div class="t1-row">' + md(t.verify.how) + '</div>';
      if (t.verify.lines.length) h += ul(t.verify.lines);
      if (t.verify.result) h += '<div class="t1-row"><b>' + md(t.verify.result) + '</b></div>';
      h += '</div></div>';
    }
    if (t.traps.length) {
      h += '<details open class="t1-fold t1-trap"><summary>⚠️ กับดักที่เด็กมักติด (' + t.traps.length + ')</summary><div class="t1-fb">';
      t.traps.forEach(function (p) {
        h += '<div class="t1-trapi"><div class="t1-got">ตอบผิดเป็น: ' + md(p.got) + '</div>';
        if (p.why) h += '<div class="t1-row"><span class="t1-lab">เพราะ</span> ' + md(p.why) + '</div>';
        if (p.caught_by) h += '<div class="t1-check">จับได้ด้วย: ' + md(p.caught_by) + '</div>';
        h += '</div>';
      });
      h += '</div></details>';
    }
    if (t.technique.length) h += '<div class="t1-sec"><div class="t1-h">💡 เทคนิคจำไว้ใช้ครั้งหน้า</div>' + ul(t.technique) + '</div>';
    if (t.hints.length) {
      h += '<details open class="t1-fold t1-hint"><summary>🪜 ใบ้ทีละขั้น (' + t.hints.length + ') — สำหรับเด็กที่ยังทำไม่ได้</summary><div class="t1-fb">';
      t.hints.forEach(function (x, i) { h += '<div class="t1-hi"><b>ใบ้ ' + (i + 1) + '</b><div>' + md(x) + '</div></div>'; });
      h += '</div></details>';
    }
    return h;
  }

  function t1Block(q) {
    if (!READY || !T1) return '';
    var rec = T1[q.id];
    if (!rec) return '';
    var ns = (rec.steps || []).length, nt = (rec.traps || []).length;
    return '<div class="q-section t1-wrap"><h4>เฉลยละเอียด (t1) '
      + '<span class="t1-meta">' + ns + ' ขั้น · ' + nt + ' กับดัก</span></h4>'
      + '<div class="t1-body">' + renderT1(rec, q.imageSpec) + '</div></div>';
  }

  /* ---------- ห่อฟังก์ชันเดิม ⛔ ไม่แก้ของเดิม ---------- */
  function wrap() {
    if (typeof window.renderQBody !== 'function' || typeof window.renderQCard !== 'function') return false;
    var oB = window.renderQBody, oC = window.renderQCard;
    window.renderQBody = function (q) { return oB(q) + t1Block(q); };
    window.renderQCard = function (q, opts) {
      var h = oC(q, opts);
      var hasT1 = (READY && T1 && T1[q.id]) ? '1' : '0';
      var hasImg = (q.imageSpec || q.hasImage) ? '1' : '0';
      var badge = hasT1 === '1'
        ? '<span class="badge t1b" title="มีเฉลยละเอียด t1 แล้ว">t1</span>' : '';
      h = h.replace('<details class="q-card',
        '<details data-qid="' + esc(q.id) + '" data-t1="' + hasT1 + '" data-img="' + hasImg + '" class="q-card');
      if (badge) h = h.replace('<span class="badge type">', badge + '<span class="badge type">');
      return h;
    };
    return true;
  }

  /* ---------- แถบกรอง ---------- */
  function bar() {
    var b = document.getElementById('t1bar');
    if (b) return b;
    b = document.createElement('div');
    b.id = 't1bar';
    b.innerHTML =
      '<span class="t1bl">เฉลยละเอียด</span>' +
      '<button data-m="all">ทั้งหมด <i></i></button>' +
      '<button data-m="t1">มีเฉลยใหม่แล้ว <i></i></button>' +
      '<button data-m="t1img">มีเฉลยใหม่ + มีรูป <i></i></button>' +
      '<span class="t1st" id="t1st">กำลังโหลด…</span>';
    document.body.appendChild(b);
    b.addEventListener('click', function (e) {
      var t = e.target.closest('button[data-m]');
      if (!t) return;
      MODE = t.getAttribute('data-m');
      apply();
    });
    return b;
  }

  function apply() {
    var b = bar();
    b.querySelectorAll('button[data-m]').forEach(function (x) {
      x.classList.toggle('on', x.getAttribute('data-m') === MODE);
    });
    var cards = document.querySelectorAll('details.q-card[data-qid]');
    var n = { all: 0, t1: 0, t1img: 0 }, shown = 0;
    cards.forEach(function (c) {
      var h1 = c.getAttribute('data-t1') === '1', im = c.getAttribute('data-img') === '1';
      n.all++; if (h1) n.t1++; if (h1 && im) n.t1img++;
      var ok = MODE === 'all' ? true : (MODE === 't1' ? h1 : (h1 && im));
      c.style.display = ok ? '' : 'none';
      if (ok) shown++;
    });
    b.querySelector('[data-m="all"] i').textContent = n.all;
    b.querySelector('[data-m="t1"] i').textContent = n.t1;
    b.querySelector('[data-m="t1img"] i').textContent = n.t1img;
    document.getElementById('t1st').textContent =
      READY ? ('แสดง ' + shown + ' / ' + n.all + ' ข้อ') : 'กำลังโหลดเฉลยละเอียด…';
  }

  /* ---------- CSS (ใส่เอง ⛔ ไม่แก้ CSS เดิม) ---------- */
  function css() {
    var s = document.createElement('style');
    s.textContent = [
      '#t1bar{position:fixed;right:14px;bottom:14px;z-index:9999;display:flex;gap:6px;align-items:center;',
      'background:#fff;border:1px solid #d7dee8;border-radius:12px;padding:7px 10px;box-shadow:0 6px 22px rgba(20,30,50,.16);font-size:13px}',
      '#t1bar .t1bl{font-weight:700;color:#3b4a63;margin-right:2px}',
      '#t1bar button{border:1px solid #d7dee8;background:#f7f9fc;border-radius:9px;padding:5px 10px;cursor:pointer;font:inherit;color:#2c3a52}',
      '#t1bar button.on{background:#2f6df0;border-color:#2f6df0;color:#fff}',
      '#t1bar button i{font-style:normal;opacity:.72;margin-left:5px;font-variant-numeric:tabular-nums}',
      '#t1bar .t1st{color:#63708a;margin-left:4px}',
      '.badge.t1b{background:#e7f0ff;color:#1b48a8;border:1px solid #bcd2f7;margin-right:4px}',
      '.t1-wrap{border-top:2px solid #e3e9f3;margin-top:10px;padding-top:8px}',
      '.t1-meta{font-weight:400;font-size:12px;color:#6b7891;margin-left:8px}',
      '.t1-body{font-size:14.5px;line-height:1.72}',
      '.t1-sec{margin:9px 0}',
      '.t1-h{font-weight:700;color:#2f3d55;margin-bottom:4px}',
      '.t1-chips{display:flex;flex-wrap:wrap;gap:5px}',
      '.t1-chip{background:#eef3fb;border:1px solid #d6e2f5;border-radius:7px;padding:1px 8px;font-size:12.5px}',
      '.t1-goal{background:#eefaf1;border-left:4px solid #38a169;border-radius:7px;padding:7px 11px}',
      '.t1-ul{margin:3px 0 3px 20px;padding:0}',
      '.t1-step{background:#f7f9fd;border:1px solid #e2e9f4;border-radius:10px;padding:8px 11px;margin:7px 0}',
      '.t1-st{font-weight:700;color:#223050;display:flex;gap:8px;align-items:baseline}',
      '.t1-n{background:#2f6df0;color:#fff;border-radius:50%;width:21px;height:21px;display:inline-flex;',
      'align-items:center;justify-content:center;font-size:12px;flex:0 0 21px}',
      '.t1-row{margin-top:4px}',
      '.t1-lab{font-size:12px;color:#6b7891;font-weight:600}',
      '.t1-eq{background:#fff;border:1px dashed #c9d5e8;border-radius:8px;padding:7px 11px;margin-top:5px;overflow-x:auto}',
      '.t1-check{color:#2f6b4f;font-size:13.5px;margin-top:4px}',
      '.t1-verify{background:#f3f8ff;border-radius:8px;padding:7px 11px}',
      '.t1-fold{border:1px solid #e2e9f4;border-radius:10px;margin:9px 0;background:#fff}',
      '.t1-fold>summary{cursor:pointer;padding:7px 11px;font-weight:700;color:#2f3d55}',
      '.t1-fb{padding:0 11px 9px}',
      '.t1-trap>summary{color:#9a3412}.t1-trap{background:#fffaf5;border-color:#f3ddc8}',
      '.t1-trapi{border-top:1px solid #f0e2d2;padding:6px 0}',
      '.t1-got{font-weight:600;color:#9a3412}',
      '.t1-hint{background:#f6f5ff;border-color:#ddd9f5}.t1-hint>summary{color:#4c3f9e}',
      '.t1-hi{border-top:1px solid #e6e2f7;padding:6px 0}',
      '.t1-figsec{background:#f6f9ff;border:1px solid #d7e3f7;border-radius:10px;padding:8px 11px}',
      '.t1-img{margin:8px 0;overflow-x:auto}.t1-img svg{max-width:100%;height:auto}',
      '.t1-tag{font-weight:400;font-size:12px;background:#e7f0ff;color:#1b48a8;border-radius:6px;padding:1px 7px}',
      '.t1-none{color:#9a3412}',
      '@media print{#t1bar{display:none}}'
    ].join('');
    document.head.appendChild(s);
  }

  /* ---------- เริ่ม ---------- */
  function boot() {
    css();
    if (!wrap()) {
      var st = document.getElementById('t1st');
      if (st) st.textContent = '🔴 ต่อกับวิวเวอร์ไม่ได้';
      console.error('[t1-overlay] ⛔ ไม่เจอ renderQBody/renderQCard — หยุด ไม่แตะอะไรทั้งนั้น');
      return;
    }
    bar(); apply();
    fetch(SRC, { cache: 'no-cache' })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (d) {
        T1 = d; READY = true;
        console.log('[t1-overlay] โหลดเฉลยละเอียด ' + Object.keys(d).length + ' ข้อ');
        apply();
      })
      .catch(function (e) {
        var st = document.getElementById('t1st');
        if (st) st.textContent = '🔴 โหลด t1 ไม่ได้: ' + e.message;
        console.error('[t1-overlay] โหลด ' + SRC + ' ไม่ได้', e);
      });
    // การ์ดถูกวาดใหม่ทุกครั้งที่เปลี่ยนบท/ชุด ⇒ ต้องกรองซ้ำ
    var mo = new MutationObserver(function () { apply(); });
    var main = document.querySelector('main') || document.body;
    mo.observe(main, { childList: true, subtree: true });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();

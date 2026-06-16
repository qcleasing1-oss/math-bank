/* export.js — ส่งออกชุดข้อสอบเป็น PDF / Word / JSON
 * โหลดเป็นไฟล์แยกจาก admin.html (พึ่ง global: LOADED_SETS, MANIFEST, CURRENT_SET,
 * escapeHtml, getMarkedIndices, setLabel, renderImage). ถ้าไฟล์นี้พัง จะไม่กระทบหน้า login/แอป
 */
(function () {
  'use strict';

  function _set() { return (typeof CURRENT_SET !== 'undefined') ? CURRENT_SET : null; }
  function _loaded(sid) { return (typeof LOADED_SETS !== 'undefined') ? LOADED_SETS[sid] : null; }
  function _manifestSet(sid) { return (typeof MANIFEST !== 'undefined' && MANIFEST && MANIFEST.sets) ? (MANIFEST.sets[sid] || {}) : {}; }
  function _marked(expl) { return (typeof getMarkedIndices === 'function') ? getMarkedIndices(expl) : new Set(); }
  function _esc(s) { return (typeof escapeHtml === 'function') ? escapeHtml(s) : String(s == null ? '' : s); }
  function _label(s) { return (typeof setLabel === 'function') ? setLabel(s) : (s && s.displayName) || ''; }

  window.openExportModal = function () {
    var sid = _set();
    if (!sid || !_loaded(sid)) { alert('เลือกชุดข้อสอบจากเมนู "ดูตาม Set" ก่อน แล้วจึงส่งออก'); return; }
    var n = (_loaded(sid).questions || []).length;
    var subEl = document.getElementById('exportModalSub');
    if (subEl) subEl.textContent = _label(_manifestSet(sid)) + ' \u00b7 ' + n + ' \u0e02\u0e49\u0e2d';
    var m = document.getElementById('exportModal');
    if (m) m.hidden = false;
  };
  window.closeExportModal = function () {
    var m = document.getElementById('exportModal');
    if (m) m.hidden = true;
  };
  window.doExport = function () {
    var fmtEl = document.querySelector('input[name="exp-fmt"]:checked');
    var contEl = document.querySelector('input[name="exp-content"]:checked');
    var fmt = fmtEl ? fmtEl.value : 'pdf';
    var withAns = contEl ? (contEl.value === 'full') : false;
    var sid = _set();
    window.closeExportModal();
    if (!sid || !_loaded(sid)) return;
    if (fmt === 'json') exportSetJSON(sid, withAns);
    else if (fmt === 'word') exportSetWord(sid, withAns);
    else exportSetPrint(sid, withAns);
  };

  function _filename(sid, ext, withAns) { return sid + '-' + (withAns ? 'พร้อมเฉลย' : 'โจทย์') + '.' + ext; }
  function _download(content, type, filename) {
    var blob = new Blob([content], { type: type });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url; a.download = filename;
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  function _stripAnswers(questions) {
    return questions.map(function (q) {
      var c = JSON.parse(JSON.stringify(q));
      delete c.explanation; delete c.correct; delete c.accept;
      if (c.imageSpec) {
        var marked = _marked(q.explanation);
        if (Array.isArray(c.imageSpec)) {
          var kept = c.imageSpec.filter(function (_, i) { return !marked.has(i); });
          if (kept.length) c.imageSpec = kept; else delete c.imageSpec;
        } else if (marked.has(0)) { delete c.imageSpec; }
      }
      return c;
    });
  }
  function exportSetJSON(sid, withAns) {
    var set = _loaded(sid), s = _manifestSet(sid);
    var questions = withAns ? set.questions : _stripAnswers(set.questions);
    var payload = {
      setId: sid, displayName: _label(s),
      exportedContent: withAns ? 'questions+answers' : 'questions-only',
      exported: new Date().toISOString(), questionCount: questions.length, questions: questions
    };
    _download(JSON.stringify(payload, null, 2), 'application/json', _filename(sid, 'json', withAns));
  }

  function _texToMathML(tex, display) {
    try {
      if (typeof katex === 'undefined') return _esc(tex);
      var html = katex.renderToString(tex, { output: 'mathml', throwOnError: false, displayMode: !!display });
      var m = html.match(/<math[\s\S]*?<\/math>/);
      return m ? m[0] : _esc(tex);
    } catch (e) { return _esc(tex); }
  }
  function _convMath(str, mathMode) {
    if (str == null) return '';
    if (mathMode !== 'mathml') return str;
    var out = String(str).replace(/\$\$([\s\S]+?)\$\$/g, function (_, t) { return _texToMathML(t, true); });
    out = out.replace(/\$([^$]+?)\$/g, function (_, t) { return _texToMathML(t, false); });
    return out;
  }
  function _fig(spec) {
    if (!spec || typeof renderImage !== 'function') return '';
    var svg = renderImage(spec);
    return svg ? '<div class="exp-fig">' + svg + '</div>' : '';
  }
  function _tables(q) {
    if (!Array.isArray(q.tables) || !q.tables.length) return '';
    return q.tables.map(function (t) {
      var tb = '<table class="exp-table" border="1" cellspacing="0" cellpadding="4">';
      if (Array.isArray(t.headers) && t.headers.length)
        tb += '<thead><tr>' + t.headers.map(function (h) { return '<th>' + h + '</th>'; }).join('') + '</tr></thead>';
      if (Array.isArray(t.rows) && t.rows.length)
        tb += '<tbody>' + t.rows.map(function (r) { return '<tr>' + r.map(function (c) { return '<td>' + c + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody>';
      tb += '</table>';
      return tb + (t.caption ? '<div class="exp-cap">' + t.caption + '</div>' : '');
    }).join('');
  }
  function _expLine(line, q, mathMode) {
    if (typeof line !== 'string') return '<div>' + line + '</div>';
    var re = /\[IMAGE(?::(\d+))?\]/g, last = 0, m, buf = '', any = false;
    while ((m = re.exec(line)) !== null) {
      any = true;
      buf += _convMath(line.slice(last, m.index), mathMode);
      var idx = (m[1] !== undefined) ? parseInt(m[1], 10) : 0;
      var spec = Array.isArray(q.imageSpec) ? q.imageSpec[idx] : q.imageSpec;
      buf += _fig(spec);
      last = m.index + m[0].length;
    }
    buf += _convMath(line.slice(last), mathMode);
    if (!any && line.indexOf('\u3010') >= 0) {
      if (/วิธีที่\s*1/.test(line)) return '<div class="method-detail">' + buf + '</div>';
      if (/วิธีที่\s*2/.test(line)) return '<div class="method-quick">' + buf + '</div>';
    }
    return '<div>' + buf + '</div>';
  }
  function _questionHTML(q, withAns, mathMode) {
    var h = '<div class="exp-q"><div class="exp-qnum">ข้อ ' + q.questionNumber + '</div>';
    h += '<div class="exp-qtext">' + _convMath(q.question || '', mathMode) + '</div>';
    h += _tables(q);
    var marked = _marked(q.explanation), qSpec = null;
    if (q.imageSpec) {
      if (Array.isArray(q.imageSpec)) {
        var u = q.imageSpec.filter(function (_, i) { return !marked.has(i); });
        if (u.length) qSpec = u;
      } else if (!marked.has(0)) { qSpec = q.imageSpec; }
    }
    if (qSpec) h += _fig(qSpec);
    if (q.type === 'mc' && Array.isArray(q.choices)) {
      h += '<ol class="exp-choices">';
      q.choices.forEach(function (c, i) {
        var cls = (withAns && i === q.correct) ? ' class="exp-correct"' : '';
        h += '<li' + cls + '>' + _convMath(c, mathMode) + '</li>';
      });
      h += '</ol>';
    } else if (q.type === 'fill' && withAns) {
      h += '<div class="exp-ans">ตอบ: ' + _convMath(String(q.correct), mathMode) + '</div>';
    }
    if (withAns && Array.isArray(q.explanation) && q.explanation.length) {
      h += '<div class="exp-sol"><div class="exp-sol-h">เฉลย</div>';
      q.explanation.forEach(function (line) { h += _expLine(line, q, mathMode); });
      h += '</div>';
    }
    return h + '</div>';
  }
  function _css() {
    return "body{font-family:'Sarabun','TH Sarabun New',sans-serif;color:#1a1a1a;line-height:1.6;max-width:760px;margin:24px auto;padding:0 16px;font-size:15px}"
      + ".exp-title{font-size:20px;margin:0 0 2px}"
      + ".exp-sub{font-size:13px;color:#666;margin-bottom:18px;border-bottom:1px solid #ccc;padding-bottom:10px}"
      + ".exp-q{margin:0 0 18px;padding:0 0 14px;border-bottom:1px dashed #ddd;page-break-inside:avoid}"
      + ".exp-qnum{font-weight:700;margin-bottom:4px}.exp-qtext{white-space:pre-line;margin-bottom:6px}"
      + ".exp-choices{margin:6px 0 0;padding-left:26px}.exp-choices li{margin-bottom:3px}"
      + ".exp-correct{font-weight:700}.exp-correct::after{content:' \u2713';color:#2e7d32}"
      + ".exp-ans{margin-top:6px;font-weight:600}"
      + ".exp-sol{margin-top:8px;background:#f7f5ef;border-left:3px solid #8b3a1f;padding:8px 12px;border-radius:4px}"
      + ".exp-sol-h{font-weight:700;margin-bottom:4px}"
      + ".exp-fig{margin:8px 0}.exp-fig svg{max-width:100%;height:auto}"
      + ".exp-table{border-collapse:collapse;margin:8px 0}.exp-cap{font-size:12px;color:#666}"
      + ".method-detail{background:#eaf6ec;border-left:4px solid #2e9e4f;padding:6px 10px;margin:8px 0}"
      + ".method-quick{background:#fbf0e0;border-left:4px solid #d98a2b;padding:6px 10px;margin:8px 0}";
  }
  function _parts(sid, withAns, mathMode) {
    var set = _loaded(sid), s = _manifestSet(sid), qs = set.questions || [];
    return {
      title: _label(s),
      sub: _esc(sid) + ' \u00b7 ' + qs.length + ' \u0e02\u0e49\u0e2d \u00b7 ' + (withAns ? 'พร้อมเฉลย' : 'เฉพาะโจทย์'),
      css: _css(),
      body: qs.map(function (q) { return _questionHTML(q, withAns, mathMode); }).join('')
    };
  }

  function exportSetPrint(sid, withAns) {
    var w = window.open('', '_blank');
    if (!w) { alert('เบราว์เซอร์บล็อก popup - โปรดอนุญาต popup ของหน้านี้แล้วลองใหม่'); return; }
    var p = _parts(sid, withAns, 'tex'), d = w.document;
    d.open();
    d.write('<!DOCTYPE html><html lang="th"><head><meta charset="utf-8"><title>' + _esc(p.title) + '</title>'
      + '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">'
      + '<style>' + p.css + '</style></head><body>'
      + '<h1 class="exp-title">' + _esc(p.title) + '</h1><div class="exp-sub">' + p.sub + '</div>'
      + p.body + '</body></html>');
    d.close();
    var loadScript = function (srcUrl, cb) { var s = d.createElement('script'); s.src = srcUrl; s.onload = cb; d.head.appendChild(s); };
    loadScript('https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js', function () {
      loadScript('https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js', function () {
        try { w.renderMathInElement(d.body, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }], throwOnError: false }); } catch (e) {}
        w.focus();
        setTimeout(function () { w.print(); }, 350);
      });
    });
  }

  function exportSetWord(sid, withAns) {
    var p = _parts(sid, withAns, 'mathml');
    var html = '\uFEFF<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/TR/REC-html40">'
      + '<head><meta charset="utf-8"><title>' + _esc(p.title) + '</title><style>' + p.css + '</style></head><body>'
      + '<h1 class="exp-title">' + _esc(p.title) + '</h1><div class="exp-sub">' + p.sub + '</div>'
      + p.body + '</body></html>';
    _download(html, 'application/msword', _filename(sid, 'doc', withAns));
  }
})();

// ============================================================
// renderers.js — SVG renderers สำหรับ imageSpec ใน bank
// ------------------------------------------------------------
// Port จาก portal (HANDOVER_v9.md, byte-identical)
// ใช้กับ viewer/admin.html ของ project math-bank
// อนาคต: portal สื่อการสอนจะ fetch ไฟล์เดียวกันนี้ → สอดคล้องกัน
//
// Coverage ปัจจุบัน:
//   ✅ normal-curve         (Q24 ของ samn-2563-03)
//   ✅ function-plot        (Q22 ของ samn-2562-03 — generic: parabola, piecewise-linear, polynomial)
//   ✅ ztable-with-curves   (Q4 ของ samn-2564-04 — normal curves + reference table)
//   ✅ unit-circle-figure   (Q9 samn-2565-03 + Q23 samn-2564-04 — 12 features incl. spiral + LaTeX)
//   ✅ stacked-bar-100      (Q30 samn-2565-03 — 100% composition bar chart)
//   ✅ polygon-labeled      (Q15 samn-2559-12 — labeled polygons with vertices/sides/angle marks)
//   ⏳ 3set-c-in-a-shade-ab-minus-c
//
// renderImage() จะคืน null ถ้า type ยังไม่รองรับ
// → admin.html จะ fallback ไปแสดง placeholder card เดิม
//
// CRITICAL NOTE — square root rendering:
//   ห้ามใช้ Unicode U+221A (√) เดี่ยว ๆ เพราะไม่มี vinculum (ขีดบน radicand)
//   inside unit-circle SVG: ใช้ _ucMathToSvg() — native SVG <text>√</text> + <line> วาด vinculum
//   (foreignObject + KaTeX ใน SVG context จะหาย/เพี้ยน — ใช้ native SVG จะปลอดภัยกว่า)
//   regular HTML (question/explanation): KaTeX ใน admin.html ใช้ได้ปกติ ไม่ต้องแก้
// ============================================================


// ----- helper: standard normal PDF -----
function normalPdf(x){return Math.exp(-x*x/2)/Math.sqrt(2*Math.PI);}

// ----- helper: counter for unique mask IDs (used by venn-diagram) -----
let _vennIdCounter = 0;


// ----- renderer: normal distribution curve -----
// Spec fields:
//   width, height          - SVG canvas (default 450 x 220)
//   zRange                 - [min, max] (default [-3.5, 3.5])
//   shadeFromLeft          - z value: shade area to the left
//   shadeFromRight         - z value: shade area to the right
//   shadeBetween           - [[z1, z2], ...]: shade segments
//   xLabels                - [{z, text, line?}, ...] labels on x-axis
//   valueLabels            - [{z, yFrac, text, arrowTo?}, ...] floating labels
function renderNormalCurve(spec){const W=spec.width||450,H=spec.height||220,pX=38,pB=36,pT=50;
  const pW=W-2*pX,pH=H-pT-pB;
  const xM=(spec.zRange&&spec.zRange[0])??-3.5,xX=(spec.zRange&&spec.zRange[1])??3.5,yX=0.42;
  const x2=x=>pX+pW*(x-xM)/(xX-xM);const y2=y=>pT+pH*(1-y/yX);const bY=y2(0);
  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  svg+=`<defs><marker id="ncArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/></marker></defs>`;
  if(spec.shadeFromLeft!==undefined){const fz=spec.shadeFromLeft,N=200,pts=[`${x2(xM)},${bY}`];
    for(let i=0;i<=N;i++){const x=xM+(fz-xM)*i/N,y=normalPdf(x);pts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}
    pts.push(`${x2(fz)},${bY}`);svg+=`<polygon points="${pts.join(' ')}" fill="#b8b8b8" opacity="0.7"/>`;}
  if(spec.shadeFromRight!==undefined){const fz=spec.shadeFromRight,N=200,pts=[`${x2(fz)},${bY}`];
    for(let i=0;i<=N;i++){const x=fz+(xX-fz)*i/N,y=normalPdf(x);pts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}
    pts.push(`${x2(xX)},${bY}`);svg+=`<polygon points="${pts.join(' ')}" fill="#b8b8b8" opacity="0.7"/>`;}
  (spec.shadeBetween||[]).forEach(seg=>{const[fz,tz]=seg,N=200,pts=[`${x2(fz)},${bY}`];
    for(let i=0;i<=N;i++){const x=fz+(tz-fz)*i/N,y=normalPdf(x);pts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}
    pts.push(`${x2(tz)},${bY}`);svg+=`<polygon points="${pts.join(' ')}" fill="#7d9bbf" opacity="0.75"/>`;});
  svg+=`<line x1="${pX-8}" y1="${bY}" x2="${W-pX+8}" y2="${bY}" stroke="#444" stroke-width="1"/>`;
  const cN=300,cPts=[];for(let i=0;i<=cN;i++){const x=xM+(xX-xM)*i/cN,y=normalPdf(x);cPts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}
  svg+=`<polyline points="${cPts.join(' ')}" fill="none" stroke="#222" stroke-width="1.6"/>`;
  (spec.xLabels||[]).forEach(l=>{const xp=x2(l.z);
    if(l.line){const yp=y2(normalPdf(l.z));svg+=`<line x1="${xp}" y1="${bY}" x2="${xp}" y2="${yp}" stroke="#222" stroke-width="1"/>`;}
    else{svg+=`<line x1="${xp}" y1="${bY-2}" x2="${xp}" y2="${bY+3}" stroke="#444" stroke-width="0.8"/>`;}
    svg+=`<text x="${xp}" y="${bY+18}" text-anchor="middle" font-size="14" fill="#222">${l.text}</text>`;});
  (spec.valueLabels||[]).forEach(l=>{const lx=x2(l.z),ly=pT+pH*l.yFrac;
    svg+=`<text x="${lx}" y="${ly}" text-anchor="middle" font-size="13" fill="#222">${l.text}</text>`;
    if(l.arrowTo){const ax=x2(l.arrowTo.z),ay=pT+pH*l.arrowTo.yFrac;
      svg+=`<line x1="${lx}" y1="${ly+4}" x2="${ax}" y2="${ay}" stroke="#222" stroke-width="1.2" marker-end="url(#ncArr)"/>`;}});
  return svg+'</svg>';}


// ----- renderer: function plot (generic curves + shading) -----
// Spec fields:
//   width, height         - SVG canvas (default 450 x 280)
//   xRange, yRange        - [min, max] for data axes (default [-3, 3], [-1, 5])
//   axes                  - {arrows?: bool, xLabel?, yLabel?, originLabel?}
//   functions             - [{id, kind, ...args, domain?, label?: {text, at:[x,y], anchor?}}, ...]
//     kinds:
//       'parabola'         + vertex:[h,k], throughPoint:[px,py]
//       'piecewise-linear' + points:[[x,y],[x,y],...]
//       'polynomial'       + coefs:[aN,...,a1,a0]    (highest degree first; Horner's)
//       'roots-polynomial' + roots:[r1,r2,...], leadingCoef?:1
//     each function also accepts: dashed?:bool (true → เส้นประ), domain?, label?:{text,at:[x,y],anchor?}
//   shadeBetween          - [{funcA, funcB, xRange:[a,b], color?}, ...]   funcA = lower, funcB = upper
//   annotations           - [{text, at:[x,y], anchor?, arrowTo?:[x,y]}, ...] floating labels (optional arrow pointing to a target)
function renderFunctionPlot(spec){const W=spec.width||450,H=spec.height||280,pX=30,pB=24,pT=20;
  const pW=W-2*pX,pH=H-pT-pB;
  const xR=spec.xRange||[-3,3],yR=spec.yRange||[-1,5];
  const xM=xR[0],xX=xR[1],yM=yR[0],yX=yR[1];
  const x2=x=>pX+pW*(x-xM)/(xX-xM);const y2=y=>pT+pH*(1-(y-yM)/(yX-yM));
  const fnVal=(fn,x)=>{
    if(fn.kind==='parabola'){const[h,k]=fn.vertex,[px,py]=fn.throughPoint;const a=(py-k)/((px-h)*(px-h));return a*(x-h)*(x-h)+k;}
    if(fn.kind==='piecewise-linear'){const pts=fn.points;for(let i=0;i<pts.length-1;i++){const[x1,y1]=pts[i],[x3,y3]=pts[i+1];if(x>=Math.min(x1,x3)&&x<=Math.max(x1,x3)){if(x3===x1)return y1;return y1+(y3-y1)*(x-x1)/(x3-x1);}}return null;}
    if(fn.kind==='polynomial'){let y=0;fn.coefs.forEach(c=>{y=y*x+c;});return y;}
    if(fn.kind==='roots-polynomial'){const a=fn.leadingCoef||1;let y=a;fn.roots.forEach(r=>{y*=(x-r);});return y;}
    return 0;};
  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  svg+=`<defs><marker id="fpArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/></marker></defs>`;
  const fnMap={};(spec.functions||[]).forEach(fn=>{fnMap[fn.id]=fn;});
  (spec.shadeBetween||[]).forEach(s=>{const fA=fnMap[s.funcA],fB=fnMap[s.funcB];if(!fA||!fB)return;
    const[xa,xb]=s.xRange,N=120,pts=[];
    for(let i=0;i<=N;i++){const x=xa+(xb-xa)*i/N,y=fnVal(fB,x);pts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}
    for(let i=N;i>=0;i--){const x=xa+(xb-xa)*i/N,y=fnVal(fA,x);pts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}
    svg+=`<polygon points="${pts.join(' ')}" fill="${s.color||'#b8b8b8'}" opacity="0.7"/>`;});
  const ax=spec.axes||{},x0=x2(0),y0=y2(0),arr=ax.arrows?' marker-end="url(#fpArr)"':'';
  svg+=`<line x1="${pX-8}" y1="${y0}" x2="${W-pX+8}" y2="${y0}" stroke="#222" stroke-width="1.2"${arr}/>`;
  svg+=`<line x1="${x0}" y1="${H-pB+8}" x2="${x0}" y2="${pT-8}" stroke="#222" stroke-width="1.2"${arr}/>`;
  if(ax.xLabel)svg+=`<text x="${W-pX+12}" y="${y0+5}" font-size="14" font-style="italic" fill="#222">${ax.xLabel}</text>`;
  if(ax.yLabel)svg+=`<text x="${x0-8}" y="${pT-6}" font-size="14" font-style="italic" fill="#222" text-anchor="end">${ax.yLabel}</text>`;
  if(ax.originLabel)svg+=`<text x="${x0-6}" y="${y0+14}" font-size="13" fill="#222" text-anchor="end">${ax.originLabel}</text>`;
  (spec.functions||[]).forEach(fn=>{const dom=fn.domain||xR,N=200,pts=[];
    for(let i=0;i<=N;i++){const x=dom[0]+(dom[1]-dom[0])*i/N,y=fnVal(fn,x);
      if(y!==null&&isFinite(y))pts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}
    const dashAttr=fn.dashed?' stroke-dasharray="5 4"':'';
    svg+=`<polyline points="${pts.join(' ')}" fill="none" stroke="#222" stroke-width="1.6"${dashAttr}/>`;
    if(fn.label){const[lx,ly]=fn.label.at,anc=fn.label.anchor||'start';
      svg+=`<text x="${x2(lx)}" y="${y2(ly)}" font-size="14" font-style="italic" fill="#222" text-anchor="${anc}">${fn.label.text}</text>`;}});
  (spec.annotations||[]).forEach(a=>{const[lx,ly]=a.at,anc=a.anchor||'start';
    svg+=`<text x="${x2(lx)}" y="${y2(ly)}" font-size="13" fill="#222" text-anchor="${anc}">${a.text}</text>`;
    if(a.arrowTo){const[ax,ay]=a.arrowTo;
      svg+=`<line x1="${x2(lx)}" y1="${y2(ly)+5}" x2="${x2(ax)}" y2="${y2(ay)}" stroke="#222" stroke-width="1" marker-end="url(#fpArr)"/>`;}});
  return svg+'</svg>';}


// ----- renderer: ztable-with-curves -----
// Layout: table on the left (~64%), curves stacked on the right (~36%, each 1 row).
// Each curve illustrates the shaded area in the table row directly to its left.
//
// Spec fields:
//   width, height                  - SVG canvas (default 480 x 280)
//   curves[]                       - array of curve specs
//     .zPosition                   - z value to mark/shade to
//     .shadeFromLeft               - bool: shade area from -∞ to z
//     .shadeFromRight              - bool: shade area from z to +∞
//     .labels[]                    - [{x, text}, ...] labels on x-axis
//     .side                        - "right" | "left" (reserved; currently stacks on right)
//   table.headerLeft, .headerRight - column header strings
//   table.columns[]                - [{z, area}, ...]
function renderZTable(spec) {
  const W = spec.width || 480;
  const H = spec.height || 280;
  const curves = spec.curves || [];
  const table = spec.table || {};

  // Layout: table left (64%), curves right (36%) stacked
  const tableW = Math.round(W * 0.64);
  const curveAreaW = W - tableW;

  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" `
          + `style="background:#fff;font-family:'Sarabun',sans-serif;">`;

  // Curves on the right (stacked vertically)
  if (curves.length > 0) {
    const slotH = H / curves.length;
    curves.forEach((c, i) => {
      svg += _ztMiniCurve(c, tableW, i * slotH, curveAreaW, slotH);
    });
  }

  // Table on the left
  if (table.columns && table.columns.length > 0) {
    svg += _ztTableRows(table, 0, 0, tableW, H);
  }

  return svg + '</svg>';
}

// internal: mini normal curve for one z-value (drawn inside a slot rect)
function _ztMiniCurve(c, x0, y0, w, h) {
  const padX = 14, padTop = 14, padBot = 24;
  const plotW = w - 2 * padX;
  const plotH = h - padTop - padBot;
  const xMin = -3, xMax = 3, yMax = 0.45;

  const xToPx = z => x0 + padX + plotW * (z - xMin) / (xMax - xMin);
  const yToPx = v => y0 + padTop + plotH * (1 - v / yMax);
  const baseY = yToPx(0);

  const zp = c.zPosition;
  let s = '';

  // Shading from -∞ to z
  if (c.shadeFromLeft) {
    const N = 80;
    const pts = [`${xToPx(xMin)},${baseY}`];
    for (let i = 0; i <= N; i++) {
      const z = xMin + (zp - xMin) * i / N;
      pts.push(`${xToPx(z).toFixed(2)},${yToPx(normalPdf(z)).toFixed(2)}`);
    }
    pts.push(`${xToPx(zp)},${baseY}`);
    s += `<polygon points="${pts.join(' ')}" fill="#b8b8b8" opacity="0.7"/>`;
  }

  // Shading from z to +∞
  if (c.shadeFromRight) {
    const N = 80;
    const pts = [`${xToPx(zp)},${baseY}`];
    for (let i = 0; i <= N; i++) {
      const z = zp + (xMax - zp) * i / N;
      pts.push(`${xToPx(z).toFixed(2)},${yToPx(normalPdf(z)).toFixed(2)}`);
    }
    pts.push(`${xToPx(xMax)},${baseY}`);
    s += `<polygon points="${pts.join(' ')}" fill="#b8b8b8" opacity="0.7"/>`;
  }

  // Baseline (x-axis)
  s += `<line x1="${x0 + padX - 4}" y1="${baseY}" `
     + `x2="${x0 + w - padX + 4}" y2="${baseY}" `
     + `stroke="#444" stroke-width="1"/>`;

  // The curve itself
  const N = 120;
  const cPts = [];
  for (let i = 0; i <= N; i++) {
    const z = xMin + (xMax - xMin) * i / N;
    cPts.push(`${xToPx(z).toFixed(2)},${yToPx(normalPdf(z)).toFixed(2)}`);
  }
  s += `<polyline points="${cPts.join(' ')}" fill="none" stroke="#222" stroke-width="1.4"/>`;

  // Vertical line from baseline up to curve at z
  const xpZ = xToPx(zp);
  const ypZ = yToPx(normalPdf(zp));
  s += `<line x1="${xpZ}" y1="${baseY}" x2="${xpZ}" y2="${ypZ}" `
     + `stroke="#222" stroke-width="1"/>`;

  // X-axis labels (ticks + text)
  (c.labels || []).forEach(l => {
    const xp = xToPx(l.x);
    s += `<line x1="${xp}" y1="${baseY - 2}" x2="${xp}" y2="${baseY + 3}" `
       + `stroke="#444" stroke-width="0.8"/>`;
    s += `<text x="${xp}" y="${baseY + 16}" text-anchor="middle" `
       + `font-size="13" fill="#222" font-style="italic">${l.text}</text>`;
  });

  return s;
}

// internal: 2-column reference table (z, area)
function _ztTableRows(table, x0, y0, w, h) {
  const cols = table.columns || [];
  const nRows = cols.length + 1;  // +1 for header

  const padX = 10, padY = 12;
  const innerX = x0 + padX;
  const innerY = y0 + padY;
  const innerW = w - 2 * padX;
  const innerH = h - 2 * padY;

  const rowH = innerH / nRows;
  const headerH = rowH;

  // 2-column split: z = 26%, area = 74%
  const col1W = innerW * 0.26;
  const col2W = innerW - col1W;

  let s = '';

  // Outer border
  s += `<rect x="${innerX}" y="${innerY}" width="${innerW}" height="${rowH * nRows}" `
     + `fill="#fff" stroke="#222" stroke-width="1.4"/>`;

  // Header background
  s += `<rect x="${innerX}" y="${innerY}" width="${innerW}" height="${headerH}" `
     + `fill="#f0e9d6"/>`;

  // Header text
  s += `<text x="${innerX + col1W / 2}" y="${innerY + headerH * 0.62}" `
     + `text-anchor="middle" font-size="15" fill="#222" `
     + `font-style="italic" font-weight="500">${table.headerLeft || ''}</text>`;
  s += `<text x="${innerX + col1W + col2W / 2}" y="${innerY + headerH * 0.62}" `
     + `text-anchor="middle" font-size="13" fill="#222">${table.headerRight || ''}</text>`;

  // Vertical separator
  s += `<line x1="${innerX + col1W}" y1="${innerY}" `
     + `x2="${innerX + col1W}" y2="${innerY + rowH * nRows}" `
     + `stroke="#222" stroke-width="1"/>`;

  // Line under header
  s += `<line x1="${innerX}" y1="${innerY + headerH}" `
     + `x2="${innerX + innerW}" y2="${innerY + headerH}" `
     + `stroke="#222" stroke-width="1"/>`;

  // Data rows
  cols.forEach((c, i) => {
    const ry = innerY + headerH + i * rowH;
    if (i > 0) {
      s += `<line x1="${innerX}" y1="${ry}" `
         + `x2="${innerX + innerW}" y2="${ry}" `
         + `stroke="#222" stroke-width="0.7"/>`;
    }
    s += `<text x="${innerX + col1W / 2}" y="${ry + rowH * 0.62}" `
       + `text-anchor="middle" font-size="14" fill="#222">${c.z}</text>`;
    s += `<text x="${innerX + col1W + col2W / 2}" y="${ry + rowH * 0.62}" `
       + `text-anchor="middle" font-size="14" fill="#222">${c.area}</text>`;
  });

  return s;
}


// ----- helper: mini SVG-LaTeX renderer (no foreignObject, no KaTeX dependency) -----
// Supports: \sqrt{X} with vinculum, italic letters, minus sign (-), \ space, \, thin space
// Used inside SVG context where foreignObject+KaTeX has CSS quirks (Q23 samn-2564-04 case).
// For complex LaTeX (e.g. \dfrac) — extend this function if needed in future.
function _ucMathToSvg(latex, x, y, fontSize) {
  const expr = latex.replace(/^\$|\$$/g, '');
  const ff = "'Cambria Math','Times New Roman',serif";
  let cur = x;
  let out = '';
  function chW(ch) {
    if (ch === ',' || ch === ' ') return fontSize * 0.3;
    if (ch === '(' || ch === ')') return fontSize * 0.4;
    if (ch === '−' || ch === '-') return fontSize * 0.55;
    if (ch === '√') return fontSize * 0.7;
    return fontSize * 0.55;
  }
  function emit(text, italic) {
    const it = italic ? ' font-style="italic"' : '';
    out += `<text x="${cur.toFixed(2)}" y="${y.toFixed(2)}" `
         + `font-family="${ff}" font-size="${fontSize}" fill="#222"${it}>${text}</text>`;
    for (const ch of text) cur += chW(ch);
  }
  let i = 0;
  while (i < expr.length) {
    const m = /^\\sqrt\s*\{([^}]*)\}/.exec(expr.substring(i));
    if (m) {
      const rad = m[1];
      emit('√', false);
      let radW = 0;
      for (const ch of rad) radW += chW(ch);
      const barY = y - fontSize * 0.78;
      out += `<line x1="${(cur - 1).toFixed(2)}" y1="${barY.toFixed(2)}" `
           + `x2="${(cur + radW + 1).toFixed(2)}" y2="${barY.toFixed(2)}" `
           + `stroke="#222" stroke-width="1"/>`;
      emit(rad, false);
      i += m[0].length;
      continue;
    }
    if (expr.substr(i, 2) === '\\ ') { cur += fontSize * 0.3; i += 2; continue; }
    if (expr.substr(i, 2) === '\\,') { cur += fontSize * 0.2; i += 2; continue; }
    if (expr[i] === '-') { emit('−', false); i += 1; continue; }
    const isLetter = /[a-zA-Z]/.test(expr[i]);
    let end = i;
    while (end < expr.length 
           && expr[end] !== '\\' 
           && expr[end] !== '-'
           && (/[a-zA-Z]/.test(expr[end]) === isLetter)) end++;
    const seg = expr.substring(i, end);
    emit(seg, isLetter);
    i = end;
  }
  return out;
}


// ----- renderer: unit-circle-figure -----
// Layout: square SVG (default 320x320) with circle centered, radius in px (default 100).
// Math convention: (x, y) in unit coords (-1..1) maps to SVG with Y-axis flipped.
//
// Spec fields (12 features):
//   size, radius                  - canvas size, circle radius (px)
//   showAxes                      - bool (default true)
//   axisLabels                    - {x: 'X', y: 'Y'}
//   mainCircleDashed              - bool (Q23 fig 1)
//   dots[]                        - {id, x, y, label?, labelDx?, labelDy?,
//                                    showCoord? (supports LaTeX via $..$),
//                                    coordPos?:{dx,dy}}
//   radii[]                       - [{toDot}]
//   chords[]                      - [{fromDot, toDot}]
//   rightAngles[]                 - [{at, refs:[ref1, ref2]}]  small square at vertex
//   perimeterArcs[]               - [{fromDot, toDot, emphasized?}] short arc on circle
//   arcs[]                        - [{fromAngle, toAngle, label?, radius, labelOffset?}]
//                                   internal angle indicators (math angle convention, Y-up)
//   internalSpiralArrow           - {innerRadius, outerRadius, numTurns, startAngle, direction}
//   annotations[]                 - [{x, y, text, fontSize?, anchor?}]  floating text in SVG px
//
// LaTeX in showCoord ($...$): rendered via _ucMathToSvg() — pure SVG, no foreignObject
//   (foreignObject + KaTeX has CSS rendering issues for nested math; native SVG is reliable)
// Greek letters (α, β, etc.): forced serif font (Sarabun lacks Greek glyphs).
function renderUnitCircle(spec){
  const size = spec.size || 320;
  const radius = spec.radius || 100;
  const cx = size / 2, cy = size / 2;
  const toSvg = (x, y) => [cx + radius * x, cy - radius * y];

  const dots = {};
  (spec.dots || []).forEach(d => {
    const [px, py] = toSvg(d.x, d.y);
    dots[d.id] = Object.assign({}, d, {px, py});
  });

  let svg = `<svg viewBox="0 0 ${size} ${size}" width="${size}" height="${size}" `
          + `xmlns="http://www.w3.org/2000/svg" `
          + `style="background:#fff;font-family:'Sarabun',sans-serif;">`;
  svg += `<defs><marker id="ucArr" viewBox="0 0 10 10" refX="9" refY="5" `
       + `markerWidth="7" markerHeight="7" orient="auto-start-reverse">`
       + `<path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/></marker></defs>`;

  // Axes
  if (spec.showAxes !== false) {
    const ax = spec.axisLabels || {};
    const pad = 10;
    svg += `<line x1="${pad}" y1="${cy}" x2="${size-pad}" y2="${cy}" stroke="#222" stroke-width="1" marker-end="url(#ucArr)"/>`;
    svg += `<line x1="${cx}" y1="${size-pad}" x2="${cx}" y2="${pad}" stroke="#222" stroke-width="1" marker-end="url(#ucArr)"/>`;
    if (ax.x) svg += `<text x="${size-pad-4}" y="${cy-6}" font-size="14" font-style="italic" fill="#222" text-anchor="end">${ax.x}</text>`;
    if (ax.y) svg += `<text x="${cx+8}" y="${pad+10}" font-size="14" font-style="italic" fill="#222">${ax.y}</text>`;
  }

  // Main circle (solid or dashed)
  const dashed = spec.mainCircleDashed ? ' stroke-dasharray="4 3"' : '';
  svg += `<circle cx="${cx}" cy="${cy}" r="${radius}" fill="none" stroke="#222" stroke-width="1.4"${dashed}/>`;

  // radii (origin → dot)
  (spec.radii || []).forEach(r => {
    const d = dots[r.toDot]; if (!d) return;
    svg += `<line x1="${cx}" y1="${cy}" x2="${d.px}" y2="${d.py}" stroke="#222" stroke-width="1.2"/>`;
  });

  // chords (dot → dot)
  (spec.chords || []).forEach(c => {
    const a = dots[c.fromDot], b = dots[c.toDot]; if (!a || !b) return;
    svg += `<line x1="${a.px}" y1="${a.py}" x2="${b.px}" y2="${b.py}" stroke="#222" stroke-width="1.2"/>`;
  });

  // perimeterArcs (along main circle, short arc, emphasized = thicker)
  (spec.perimeterArcs || []).forEach(arc => {
    const a = dots[arc.fromDot], b = dots[arc.toDot]; if (!a || !b) return;
    const t1 = Math.atan2(a.py - cy, a.px - cx);
    const t2 = Math.atan2(b.py - cy, b.px - cx);
    let dt = t2 - t1;
    while (dt > Math.PI) dt -= 2 * Math.PI;
    while (dt <= -Math.PI) dt += 2 * Math.PI;
    const sweep = dt > 0 ? 1 : 0;
    const w = arc.emphasized ? 2.8 : 1.4;
    svg += `<path d="M ${a.px.toFixed(2)} ${a.py.toFixed(2)} A ${radius} ${radius} 0 0 ${sweep} ${b.px.toFixed(2)} ${b.py.toFixed(2)}" fill="none" stroke="#222" stroke-width="${w}"/>`;
  });

  // rightAngles (small square at vertex, aligned with arms toward refs)
  (spec.rightAngles || []).forEach(ra => {
    const v = dots[ra.at]; if (!v) return;
    const refs = (ra.refs || []).map(rid => dots[rid]).filter(Boolean);
    if (refs.length < 2) return;
    const dirs = refs.map(r => {
      const dx = r.px - v.px, dy = r.py - v.py;
      const L = Math.sqrt(dx*dx + dy*dy) || 1;
      return [dx/L, dy/L];
    });
    const sz = 9;
    const p0x = v.px + sz*dirs[0][0], p0y = v.py + sz*dirs[0][1];
    const p2x = v.px + sz*dirs[1][0], p2y = v.py + sz*dirs[1][1];
    const p1x = p0x + sz*dirs[1][0], p1y = p0y + sz*dirs[1][1];
    svg += `<path d="M ${p0x.toFixed(2)} ${p0y.toFixed(2)} L ${p1x.toFixed(2)} ${p1y.toFixed(2)} L ${p2x.toFixed(2)} ${p2y.toFixed(2)}" fill="none" stroke="#222" stroke-width="1"/>`;
  });

  // arcs (internal angle indicators α/β with optional labels — math CCW convention)
  // Greek labels use SERIF font (Sarabun lacks Greek glyphs).
  (spec.arcs || []).forEach(a => {
    const r = a.radius || 20;
    const t1 = a.fromAngle, t2 = a.toAngle;
    const x1 = cx + r * Math.cos(t1), y1 = cy - r * Math.sin(t1);
    const x2 = cx + r * Math.cos(t2), y2 = cy - r * Math.sin(t2);
    const dt = t2 - t1;
    const sweep = dt > 0 ? 0 : 1;
    const largeArc = Math.abs(dt) > Math.PI ? 1 : 0;
    svg += `<path d="M ${x1.toFixed(2)} ${y1.toFixed(2)} A ${r} ${r} 0 ${largeArc} ${sweep} ${x2.toFixed(2)} ${y2.toFixed(2)}" fill="none" stroke="#222" stroke-width="1"/>`;
    if (a.label) {
      const tMid = (t1 + t2) / 2;
      const rLabel = r + 10;
      const offX = (a.labelOffset && a.labelOffset[0]) || 0;
      const offY = (a.labelOffset && a.labelOffset[1]) || 0;
      const lx = cx + rLabel * Math.cos(tMid) + offX;
      const ly = cy - rLabel * Math.sin(tMid) + offY;
      svg += `<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" `
           + `font-family="'Cambria Math','Times New Roman',serif" `
           + `font-size="17" font-style="italic" fill="#222" text-anchor="middle">${a.label}</text>`;
    }
  });

  // internalSpiralArrow (multi-turn spiral with arrowhead at endpoint)
  if (spec.internalSpiralArrow) {
    const sp = spec.internalSpiralArrow;
    const rIn = (sp.innerRadius || 0.2) * radius;
    const rOut = (sp.outerRadius || 0.6) * radius;
    const turns = sp.numTurns || 1;
    const dirSign = sp.direction === 'cw' ? -1 : 1;
    const a0 = sp.startAngle || 0;
    const sweep = dirSign * turns * 2 * Math.PI;
    const N = 120;
    const pts = [];
    let endX = 0, endY = 0, tangent = [1, 0];
    for (let i = 0; i <= N; i++) {
      const t = i / N;
      const a = a0 + sweep * t;
      const r = rIn + (rOut - rIn) * t;
      const px = cx + r * Math.cos(a);
      const py = cy - r * Math.sin(a);
      pts.push(`${px.toFixed(2)},${py.toFixed(2)}`);
      if (i === N) {
        endX = px; endY = py;
        const dr_dt = rOut - rIn, da_dt = sweep;
        tangent = [
          dr_dt * Math.cos(a) - r * Math.sin(a) * da_dt,
          -(dr_dt * Math.sin(a) + r * Math.cos(a) * da_dt)
        ];
      }
    }
    svg += `<polyline points="${pts.join(' ')}" fill="none" stroke="#222" stroke-width="1.2"/>`;
    const [tx, ty] = tangent;
    const tL = Math.sqrt(tx*tx + ty*ty) || 1;
    const ux = tx / tL, uy = ty / tL;
    const nx = -uy, ny = ux;
    const ah = 8;
    const baseX = endX - ah * ux, baseY = endY - ah * uy;
    const blX = baseX + ah * 0.45 * nx, blY = baseY + ah * 0.45 * ny;
    const brX = baseX - ah * 0.45 * nx, brY = baseY - ah * 0.45 * ny;
    svg += `<polygon points="${endX.toFixed(2)},${endY.toFixed(2)} ${blX.toFixed(2)},${blY.toFixed(2)} ${brX.toFixed(2)},${brY.toFixed(2)}" fill="#222"/>`;
  }

  // annotations (floating text at absolute SVG coords — serif if Greek or single letter)
  (spec.annotations || []).forEach(a => {
    const fs = a.fontSize || 14;
    const anchor = a.anchor || 'start';
    const useSerif = /[\u0370-\u03FF]/.test(a.text) || a.text.length === 1;
    const fontAttr = useSerif ? ` font-family="'Cambria Math','Times New Roman',serif"` : '';
    svg += `<text x="${a.x}" y="${a.y}" font-size="${fs}"${fontAttr} `
         + `fill="#222" text-anchor="${anchor}" font-style="italic">${a.text}</text>`;
  });

  // dots (drawn last so they're on top of all lines/arcs)
  (spec.dots || []).forEach(d => {
    const dt = dots[d.id];
    svg += `<circle cx="${dt.px}" cy="${dt.py}" r="3" fill="#222"/>`;
    if (d.label) {
      const dx = d.labelDx != null ? d.labelDx : 8;
      const dy = d.labelDy != null ? d.labelDy : -4;
      svg += `<text x="${(dt.px+dx).toFixed(2)}" y="${(dt.py+dy).toFixed(2)}" `
           + `font-family="'Cambria Math','Times New Roman',serif" `
           + `font-size="16" font-style="italic" fill="#222">${d.label}</text>`;
    }
    if (d.showCoord) {
      const cdx = (d.coordPos && d.coordPos.dx != null) ? d.coordPos.dx : 6;
      const cdy = (d.coordPos && d.coordPos.dy != null) ? d.coordPos.dy : 16;
      const cxPos = dt.px + cdx, cyPos = dt.py + cdy;
      const raw = d.showCoord;
      if (raw.indexOf('$') !== -1) {
        // LaTeX in SVG — use native SVG renderer (NOT foreignObject + KaTeX)
        // because foreignObject + KaTeX has CSS layout issues (√ disappears, etc.)
        // _ucMathToSvg supports \sqrt{} with proper vinculum natively.
        svg += _ucMathToSvg(raw, cxPos, cyPos, 14);
      } else {
        svg += `<text x="${cxPos.toFixed(2)}" y="${cyPos.toFixed(2)}" font-size="12" fill="#222">${raw}</text>`;
      }
    }
  });

  return svg + '</svg>';
}


// ----- renderer: 100% stacked bar chart -----
// Spec fields:
//   width, height          - SVG canvas (default 400 x 380)
//   yLabel                 - vertical y-axis label (Thai text, rotated -90°)
//   categories             - [{name, segments: [{label, value}, ...]}, ...]
//                            segments stack bottom→top; values are percentages (0..100)
//   legend                 - [{label}, ...] aligned with segment indices (optional)
//   yAxis                  - {min, max, step} (default {min:0, max:100, step:10})
//   colors                 - [color, ...] per segment index (optional; defaults to parchment palette)
//   textColors             - [color, ...] per segment index (optional; auto-chosen if absent)
function renderStackedBar100(spec){
  const W = spec.width || 400;
  const H = spec.height || 380;
  const yLabel = spec.yLabel || '';
  const cats = spec.categories || [];
  const legend = spec.legend || [];
  const yAxis = spec.yAxis || {min: 0, max: 100, step: 10};

  // Default 4-segment palette (warm parchment: light cream → dark brown)
  const defaultColors = ['#e6dfd0', '#b8aa88', '#7a6e54', '#3a3424'];
  const defaultTextColors = ['#222', '#222', '#fff', '#fff'];
  const colors = spec.colors || defaultColors;
  const textColors = spec.textColors || defaultTextColors;

  // Layout: leave room for y-label (left), legend (right), category labels (bottom)
  const padL = 60;
  const padR = legend.length > 0 ? 60 : 25;
  const padT = 25;
  const padB = 60;
  const plotW = W - padL - padR;
  const plotH = H - padT - padB;
  const baseY = padT + plotH;
  const topY = padT;

  // Bar layout: equal-width bars with equal gaps (n+1 gaps for n bars)
  const nBars = cats.length;
  const barW = Math.min(80, plotW * 0.35);
  const gapW = (plotW - nBars * barW) / (nBars + 1);

  // Y scale: pixels per unit
  const yRange = yAxis.max - yAxis.min;
  const yScale = plotH / yRange;

  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" `
          + `style="background:#fff;font-family:'Sarabun',sans-serif;">`;

  // Y-axis label (rotated -90°), centered vertically on plot area
  if(yLabel){
    const lx = 14, ly = padT + plotH/2;
    svg += `<text x="${lx}" y="${ly}" transform="rotate(-90 ${lx} ${ly})" `
         + `text-anchor="middle" font-size="12" fill="#222">${yLabel}</text>`;
  }

  // Y-axis vertical line
  svg += `<line x1="${padL}" y1="${topY}" x2="${padL}" y2="${baseY}" `
       + `stroke="#222" stroke-width="1"/>`;

  // Y-axis ticks + numeric labels (from min to max, stepping by step)
  for(let v = yAxis.min; v <= yAxis.max + 1e-9; v += yAxis.step){
    const y = baseY - (v - yAxis.min) * yScale;
    svg += `<line x1="${padL-3}" y1="${y.toFixed(2)}" x2="${padL}" y2="${y.toFixed(2)}" `
         + `stroke="#222" stroke-width="1"/>`;
    svg += `<text x="${padL-6}" y="${(y+4).toFixed(2)}" text-anchor="end" `
         + `font-size="11" fill="#222">${v}</text>`;
  }

  // X-axis horizontal line (baseline)
  svg += `<line x1="${padL}" y1="${baseY}" x2="${padL + plotW}" y2="${baseY}" `
       + `stroke="#222" stroke-width="1"/>`;

  // Bars + stacked segments
  cats.forEach((cat, ci) => {
    const barX = padL + gapW + ci * (barW + gapW);
    const barCx = barX + barW/2;

    let cumValue = 0;
    (cat.segments || []).forEach((seg, si) => {
      const segBottomY = baseY - cumValue * yScale;
      const segTopY = baseY - (cumValue + seg.value) * yScale;
      const segH = segBottomY - segTopY;

      // Segment rectangle (thin border for separation)
      svg += `<rect x="${barX.toFixed(2)}" y="${segTopY.toFixed(2)}" `
           + `width="${barW.toFixed(2)}" height="${segH.toFixed(2)}" `
           + `fill="${colors[si % colors.length]}" `
           + `stroke="#222" stroke-width="0.8"/>`;

      // Segment label (centered; smaller font if segment is short)
      const labelY = (segBottomY + segTopY) / 2 + 4;
      const labelColor = textColors[si % textColors.length];
      const fontSize = segH < 22 ? 11 : 13;
      svg += `<text x="${barCx.toFixed(2)}" y="${labelY.toFixed(2)}" `
           + `text-anchor="middle" font-size="${fontSize}" `
           + `fill="${labelColor}">${seg.label}</text>`;

      cumValue += seg.value;
    });

    // Category label below bar
    svg += `<text x="${barCx.toFixed(2)}" y="${(baseY + 25).toFixed(2)}" `
         + `text-anchor="middle" font-size="14" fill="#222">${cat.name || ''}</text>`;
  });

  // Legend (right side, vertically stacked)
  if(legend.length > 0){
    const legX = padL + plotW + 20;
    const legStartY = padT + 50;
    legend.forEach((leg, li) => {
      const ly = legStartY + li * 25;
      svg += `<rect x="${legX}" y="${ly}" width="14" height="14" `
           + `fill="${colors[li % colors.length]}" `
           + `stroke="#222" stroke-width="0.8"/>`;
      svg += `<text x="${legX + 20}" y="${ly + 12}" `
           + `font-size="13" fill="#222">${leg.label}</text>`;
    });
  }

  return svg + '</svg>';
}


// ----- renderer: labeled polygon (vertices + sides + angle marks) -----
// Spec fields:
//   width, height          - SVG canvas (default 380 x 300)
//   vertices               - {<name>: [x, y], ...}  — vertex positions
//   vertexLabels           - {<name>: {dx, dy}, ...}  — label offsets from each vertex
//   sides                  - [{from, to, label?, labelOffset?, style?, arrows?}, ...]
//                            style:  "solid" (default) or "dashed"
//                            arrows: "end", "start", or "both" (for vector-style sides)
//                            label:  length text (e.g. "5", "x", "AB") — optional
//                            labelOffset: {dx, dy} fine-tune from midpoint
//   angleMarks             - [{at, from, to, type, ...}, ...]
//                            type "right": square marker; optional `size` (default 10)
//                            type "arc":   arc + optional `label`; optional `radius` (18),
//                                          `labelDistance` (radius+14)
//   annotations            - [{x, y, text, fontSize?, anchor?}, ...]  — free-form text
function renderPolygonLabeled(spec){
  const W = spec.width || 380;
  const H = spec.height || 300;
  const verts = spec.vertices || {};
  const vLabels = spec.vertexLabels || {};
  const sides = spec.sides || [];
  const angleMarks = spec.angleMarks || [];
  const annotations = spec.annotations || [];

  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;

  // --- defs: arrow marker for vector-style sides ---
  svg += `<defs>`
       + `<marker id="pl-arrow" viewBox="0 0 10 10" refX="9" refY="5" `
       + `markerWidth="7" markerHeight="7" orient="auto-start-reverse">`
       + `<path d="M0 0 L10 5 L0 10 z" fill="#222"/></marker>`
       + `</defs>`;

  // Helpers
  const V = name => {
    const p = verts[name];
    return (p && p.length >= 2) ? p : [0, 0];
  };
  const unitVec = (p1, p2) => {
    const dx = p2[0] - p1[0], dy = p2[1] - p1[1];
    const len = Math.sqrt(dx*dx + dy*dy);
    if(len < 1e-9) return [1, 0];
    return [dx/len, dy/len];
  };

  // --- 1. Sides (drawn first, bottom layer) ---
  sides.forEach(s => {
    const p1 = V(s.from), p2 = V(s.to);
    const dashAttr = (s.style === 'dashed') ? ' stroke-dasharray="4 3"' : '';
    let arrowAttr = '';
    if(s.arrows === 'end' || s.arrows === 'both'){
      arrowAttr += ' marker-end="url(#pl-arrow)"';
    }
    if(s.arrows === 'start' || s.arrows === 'both'){
      arrowAttr += ' marker-start="url(#pl-arrow)"';
    }
    svg += `<line x1="${p1[0]}" y1="${p1[1]}" x2="${p2[0]}" y2="${p2[1]}" `
         + `stroke="#222" stroke-width="1.5"${dashAttr}${arrowAttr}/>`;
  });

  // --- 2. Angle marks (over sides) ---
  angleMarks.forEach(am => {
    const center = V(am.at);
    const uFrom = unitVec(center, V(am.from));
    const uTo   = unitVec(center, V(am.to));

    if(am.type === 'right'){
      // Square marker: two outer sides of a small square at the corner
      const size = am.size || 10;
      const c1 = [center[0] + size*uFrom[0], center[1] + size*uFrom[1]];
      const corner = [center[0] + size*(uFrom[0]+uTo[0]), center[1] + size*(uFrom[1]+uTo[1])];
      const c2 = [center[0] + size*uTo[0], center[1] + size*uTo[1]];
      svg += `<path d="M ${c1[0].toFixed(2)} ${c1[1].toFixed(2)} `
           + `L ${corner[0].toFixed(2)} ${corner[1].toFixed(2)} `
           + `L ${c2[0].toFixed(2)} ${c2[1].toFixed(2)}" `
           + `fill="none" stroke="#222" stroke-width="1"/>`;
    }
    else if(am.type === 'arc'){
      const r = am.radius || 18;
      const start = [center[0] + r*uFrom[0], center[1] + r*uFrom[1]];
      const end   = [center[0] + r*uTo[0],   center[1] + r*uTo[1]];

      // Sweep flag: SVG y is down, so cross > 0 ⇒ uTo is CW from uFrom on screen
      //   ⇒ sweep along positive-angle (CW on screen) ⇒ sweep-flag = 1
      // Always use small arc (large-arc-flag = 0) — interior angles of polygons are ≤ 180°
      const cross = uFrom[0]*uTo[1] - uFrom[1]*uTo[0];
      const sweepFlag = (cross > 0) ? 1 : 0;

      svg += `<path d="M ${start[0].toFixed(2)} ${start[1].toFixed(2)} `
           + `A ${r} ${r} 0 0 ${sweepFlag} `
           + `${end[0].toFixed(2)} ${end[1].toFixed(2)}" `
           + `fill="none" stroke="#222" stroke-width="1"/>`;

      // Label on bisector of the two rays
      if(am.label){
        const dist = (am.labelDistance != null) ? am.labelDistance : (r + 14);
        const bx = uFrom[0] + uTo[0];
        const by = uFrom[1] + uTo[1];
        const blen = Math.sqrt(bx*bx + by*by);
        if(blen > 1e-9){
          const lx = center[0] + dist*(bx/blen);
          const ly = center[1] + dist*(by/blen);
          svg += `<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" `
               + `font-family="'Cambria Math','Times New Roman',serif" `
               + `font-size="13" fill="#222" text-anchor="middle" `
               + `dominant-baseline="central">${am.label}</text>`;
        }
      }
    }
  });

  // --- 3. Side length labels (after angle marks) ---
  sides.forEach(s => {
    if(!s.label) return;
    const p1 = V(s.from), p2 = V(s.to);
    const mx = (p1[0] + p2[0]) / 2;
    const my = (p1[1] + p2[1]) / 2;
    const off = s.labelOffset || {};
    const lx = mx + (off.dx || 0);
    const ly = my + (off.dy || 0);
    svg += `<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" `
         + `font-family="'Cambria Math','Times New Roman',serif" `
         + `font-size="15" fill="#222" text-anchor="middle" `
         + `dominant-baseline="central">${s.label}</text>`;
  });

  // --- 4. Vertex labels (top layer) ---
  Object.keys(verts).forEach(name => {
    const p = V(name);
    const off = vLabels[name] || {};
    const lx = p[0] + (off.dx || 0);
    const ly = p[1] + (off.dy || 0);
    svg += `<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" `
         + `font-family="'Cambria Math','Times New Roman',serif" `
         + `font-size="18" fill="#222">${name}</text>`;
  });

  // --- 5. Free-form annotations (top, optional) ---
  annotations.forEach(a => {
    const fs = a.fontSize || 14;
    const anchor = a.anchor || 'start';
    svg += `<text x="${a.x}" y="${a.y}" `
         + `font-family="'Cambria Math','Times New Roman',serif" `
         + `font-size="${fs}" fill="#222" text-anchor="${anchor}">${a.text||''}</text>`;
  });

  return svg + '</svg>';
}


// ----- main entry -----
// Returns: SVG string ที่ใช้ insert ผ่าน innerHTML ได้เลย,
//          หรือ null ถ้า type ไม่รองรับ (caller จะ fallback)
// Accepts a single spec OR an array of specs (Q23 has imageSpec = [fig1, fig2]).
// ----- renderer: stem-and-leaf plot (แผนภาพต้นใบ) -----
// Spec fields:
//   rows       - [{stem:'4', leaves:['2','4','5','6']}, ...]  (required)
//   highlight  - ['6:6','7:0']  รูปแบบ 'stem:leafIndex' (0-based) → เน้นใบนั้น (optional)
//   caption    - heading 2 ช่อง default 'ต้น | ใบ' (optional; ใส่ '' เพื่อซ่อน)
//   width      - SVG width (optional; auto จากจำนวนใบมากสุด)
//   unitNote   - ข้อความหน่วยใต้ตาราง (optional)
function renderStemLeaf(spec){
  const rows = spec.rows || [];
  if(rows.length === 0) return null;

  const accent = '#8b3a1f';          // burnt sienna (เน้น)
  const ink = '#222';
  const rule = '#3a3424';            // เส้นตาราง (warm dark)
  const fs = 16;                     // font size ตัวเลข
  const rowH = 30;                   // ความสูงต่อแถว
  const stemColW = 54;               // ความกว้างคอลัมน์ต้น
  const leafGap = 24;                // ระยะห่างใบแต่ละตัว
  const padT = 14, padB = 14, padL = 14, padR = 18;
  const headH = (spec.caption === '') ? 6 : 26;

  // จำนวนใบมากสุด → กำหนดความกว้าง
  const maxLeaves = Math.max(...rows.map(r => (r.leaves||[]).length));
  const leafAreaW = maxLeaves * leafGap + 14;
  const W = spec.width || (padL + stemColW + leafAreaW + padR);
  const H = padT + headH + rows.length * rowH + padB + (spec.unitNote ? 22 : 0);

  // set ของ highlight เพื่อ lookup เร็ว
  const hi = new Set(spec.highlight || []);

  const sepX = padL + stemColW;      // เส้นแบ่งแนวตั้ง ต้น|ใบ
  const topY = padT + headH;
  const botY = topY + rows.length * rowH;

  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" `
          + `style="background:#fff;font-family:'Sarabun',sans-serif;">`;

  // หัวตาราง (ต้น | ใบ)
  if(spec.caption !== ''){
    const cap = spec.caption || 'ต้น | ใบ';
    const parts = cap.split('|');
    const stemHead = (parts[0]||'ต้น').trim();
    const leafHead = (parts[1]||'ใบ').trim();
    svg += `<text x="${(padL + stemColW/2).toFixed(1)}" y="18" text-anchor="middle" `
         + `font-size="13" font-weight="700" fill="${ink}">${stemHead}</text>`;
    svg += `<text x="${(sepX + 16).toFixed(1)}" y="18" text-anchor="start" `
         + `font-size="13" font-weight="700" fill="${ink}">${leafHead}</text>`;
  }

  // เส้นแบ่งแนวตั้ง (ต้น | ใบ)
  svg += `<line x1="${sepX}" y1="${topY}" x2="${sepX}" y2="${botY}" `
       + `stroke="${rule}" stroke-width="1.5"/>`;

  // แต่ละแถว
  rows.forEach((r, ri) => {
    const yBase = topY + ri*rowH + rowH*0.65;   // baseline ตัวเลข
    // ต้น (ชิดขวาก่อนเส้นแบ่ง)
    svg += `<text x="${(sepX - 12).toFixed(1)}" y="${yBase.toFixed(1)}" `
         + `text-anchor="end" font-size="${fs}" fill="${ink}">${r.stem}</text>`;
    // ใบ
    (r.leaves||[]).forEach((leaf, li) => {
      const lx = sepX + 16 + li*leafGap;
      const key = `${r.stem}:${li}`;
      const isHi = hi.has(key);
      const isVar = /[a-zA-Zก-ฮ]/.test(String(leaf));   // ตัวแปร → italic
      if(isHi){
        // วงกลมเน้น
        svg += `<circle cx="${(lx).toFixed(1)}" cy="${(yBase - fs*0.32).toFixed(1)}" r="11" `
             + `fill="none" stroke="${accent}" stroke-width="1.6"/>`;
      }
      svg += `<text x="${lx.toFixed(1)}" y="${yBase.toFixed(1)}" text-anchor="middle" `
           + `font-size="${fs}" fill="${isHi?accent:ink}"${isVar?' font-style="italic"':''}>${leaf}</text>`;
    });
  });

  // หน่วย/หมายเหตุใต้ตาราง
  if(spec.unitNote){
    svg += `<text x="${padL}" y="${(botY + 18).toFixed(1)}" text-anchor="start" `
         + `font-size="11" fill="#5a4f3d">${spec.unitNote}</text>`;
  }

  svg += `</svg>`;
  return svg;
}


// ----- renderer: venn-diagram -----
// Iteration 1 coverage: 2-set intersecting (Q24/Q32/Q71/Q73 of chap-01-set)
// Future iterations will add: 2-set disjoint, 3-set intersecting,
// custom layouts (inner-C), region arrows, box-set.
//
// Spec fields:
//   sets: 2 (3 in future iters)
//   layout: 'intersecting' (other values in future iters)
//   labels: {A:'A', B:'B'}             - text outside circles
//   regions: {A_only,B_only,AB,outside} - text inside each region
//   shade: ['A_only','B_only','AB','outside']  - 0+ regions to fill
//   universe: bool                     - draw outer rectangle + U label
//   width, height                      - optional canvas size
//
// Region IDs (2-set):  A_only · B_only · AB · outside
//
// DESIGN: A_only/B_only/outside use SVG <mask> (bulletproof — just
// "show circle X, hide circle Y"). AB uses lens path (small arcs of
// both circles meeting at intersection points). All four regions can
// shade independently — opacity is uniform regardless of combination.
function renderVennDiagram(spec){
  if(!spec || spec.type !== 'venn-diagram') return null;
  const sets = spec.sets || 2;
  const layout = spec.layout || 'intersecting';
  if(sets === 2 && layout === 'intersecting'){
    return _venn2Intersecting(spec);
  }
  if(sets === 2 && layout === 'disjoint'){
    return _venn2Disjoint(spec);
  }
  return null;   // other variants → iteration 3+ (fallback to placeholder)
}

function _venn2Intersecting(spec){
  // ---- canvas ----
  const W = spec.width || 360;
  const H = spec.height || 240;

  // ---- geometry ----
  const r = 70;
  const d = 70;                     // center-distance (must be < 2r for overlap)
  const cx = W / 2, cy = H / 2;
  const xA = cx - d/2, xB = cx + d/2;
  const yt = Math.sqrt(r*r - (d/2)*(d/2));
  const mid = cx;
  const PtX = mid, PtY = cy - yt;   // top intersection
  const PbX = mid, PbY = cy + yt;   // bottom intersection

  // universe box
  const ubW = 280, ubH = 180;
  const ubX = cx - ubW/2, ubY = cy - ubH/2;

  // ---- defaults ----
  const labels  = spec.labels  || { A: 'A', B: 'B' };
  const regions = spec.regions || {};
  const shadeSet = new Set(spec.shade || []);
  const universe = !!spec.universe;

  // ---- colors ----
  const SHADE = '#b8aa88';          // warm tan (matches stacked-bar palette)
  const SHADE_OP = 0.55;
  const INK = '#222';
  const RULE = '#3a3424';

  // ---- unique mask IDs (per-call, prevents collisions across multiple venns) ----
  const uid = ++_vennIdCounter;
  const M = (n) => `vMask${uid}_${n}`;

  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" `
          + `style="background:#fff;font-family:'Sarabun',sans-serif;">`;

  // 0. <defs> — masks for shading
  svg += `<defs>`;
  if(shadeSet.has('A_only')){
    svg += `<mask id="${M('Aonly')}" maskUnits="userSpaceOnUse">`
         + `<rect x="0" y="0" width="${W}" height="${H}" fill="black"/>`
         + `<circle cx="${xA}" cy="${cy}" r="${r}" fill="white"/>`
         + `<circle cx="${xB}" cy="${cy}" r="${r}" fill="black"/>`
         + `</mask>`;
  }
  if(shadeSet.has('B_only')){
    svg += `<mask id="${M('Bonly')}" maskUnits="userSpaceOnUse">`
         + `<rect x="0" y="0" width="${W}" height="${H}" fill="black"/>`
         + `<circle cx="${xB}" cy="${cy}" r="${r}" fill="white"/>`
         + `<circle cx="${xA}" cy="${cy}" r="${r}" fill="black"/>`
         + `</mask>`;
  }
  if(universe && shadeSet.has('outside')){
    svg += `<mask id="${M('outside')}" maskUnits="userSpaceOnUse">`
         + `<rect x="${ubX}" y="${ubY}" width="${ubW}" height="${ubH}" fill="white"/>`
         + `<circle cx="${xA}" cy="${cy}" r="${r}" fill="black"/>`
         + `<circle cx="${xB}" cy="${cy}" r="${r}" fill="black"/>`
         + `</mask>`;
  }
  svg += `</defs>`;

  // 1. SHADING (filled regions, drawn BEFORE circles so strokes overlay)
  if(universe && shadeSet.has('outside')){
    svg += `<rect x="0" y="0" width="${W}" height="${H}" `
         + `fill="${SHADE}" opacity="${SHADE_OP}" mask="url(#${M('outside')})"/>`;
  }
  if(shadeSet.has('A_only')){
    svg += `<rect x="0" y="0" width="${W}" height="${H}" `
         + `fill="${SHADE}" opacity="${SHADE_OP}" mask="url(#${M('Aonly')})"/>`;
  }
  if(shadeSet.has('B_only')){
    svg += `<rect x="0" y="0" width="${W}" height="${H}" `
         + `fill="${SHADE}" opacity="${SHADE_OP}" mask="url(#${M('Bonly')})"/>`;
  }
  if(shadeSet.has('AB')){
    // Lens: small arc of A (right side) + small arc of B (left side), both CW
    const p = `M ${PtX} ${PtY} `
            + `A ${r} ${r} 0 0 1 ${PbX} ${PbY} `
            + `A ${r} ${r} 0 0 1 ${PtX} ${PtY} Z`;
    svg += `<path d="${p}" fill="${SHADE}" opacity="${SHADE_OP}"/>`;
  }

  // 2. UNIVERSE BOX
  if(universe){
    svg += `<rect x="${ubX}" y="${ubY}" width="${ubW}" height="${ubH}" `
         + `fill="none" stroke="${RULE}" stroke-width="1.4"/>`;
    svg += `<text x="${ubX + 8}" y="${ubY + 18}" `
         + `font-family="'Cambria Math','Times New Roman',serif" `
         + `font-size="15" font-style="italic" fill="${INK}">U</text>`;
  }

  // 3. CIRCLES
  svg += `<circle cx="${xA}" cy="${cy}" r="${r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  svg += `<circle cx="${xB}" cy="${cy}" r="${r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;

  // 4. SET LABELS (outside, top corners)
  const labFS = 17;
  svg += `<text x="${xA - r * 0.85}" y="${cy - r - 4}" `
       + `font-family="'Cambria Math','Times New Roman',serif" `
       + `font-size="${labFS}" font-style="italic" fill="${INK}" text-anchor="middle">${labels.A}</text>`;
  svg += `<text x="${xB + r * 0.85}" y="${cy - r - 4}" `
       + `font-family="'Cambria Math','Times New Roman',serif" `
       + `font-size="${labFS}" font-style="italic" fill="${INK}" text-anchor="middle">${labels.B}</text>`;

  // 5. REGION TEXT (centroid placement)
  const regFS = 16;
  if(regions.A_only !== undefined){
    svg += `<text x="${xA - r * 0.45}" y="${cy + 5}" `
         + `text-anchor="middle" font-size="${regFS}" fill="${INK}">${regions.A_only}</text>`;
  }
  if(regions.B_only !== undefined){
    svg += `<text x="${xB + r * 0.45}" y="${cy + 5}" `
         + `text-anchor="middle" font-size="${regFS}" fill="${INK}">${regions.B_only}</text>`;
  }
  if(regions.AB !== undefined){
    svg += `<text x="${mid}" y="${cy + 5}" `
         + `text-anchor="middle" font-size="${regFS}" fill="${INK}">${regions.AB}</text>`;
  }
  if(regions.outside !== undefined){
    const ox = universe ? (ubX + ubW - 14) : (W - 14);
    const oy = universe ? (ubY + ubH - 10) : (H - 10);
    svg += `<text x="${ox}" y="${oy}" text-anchor="end" font-size="${regFS}" fill="${INK}">${regions.outside}</text>`;
  }

  // 6. ELEMENT LABELS (members of a set, e.g. 'a', 'b', 'c')
  svg += _vennDrawElements(spec, {
    A_only: [xA - r * 0.45, cy],
    B_only: [xB + r * 0.45, cy],
    AB:     [mid, cy],
    outside: universe ? [cx, ubY + ubH - 22] : [cx, H - 22]
  });

  return svg + '</svg>';
}


// ----- helper: draw element labels (e.g. 'a', 'b', 'c' as set members) -----
// Auto-places elements in a horizontal row centered at the region centroid.
// Italic + serif for single ASCII letters (math variable convention);
// upright Sarabun for everything else (Thai words, multi-char names).
// Optional per-element override: dx, dy nudge from auto-placed position.
function _vennDrawElements(spec, centroids){
  const elements = spec.elements || [];
  if(elements.length === 0) return '';

  // Group by region (preserve order within each region)
  const byRegion = new Map();
  elements.forEach(e => {
    const r = e.region || 'outside';
    if(!byRegion.has(r)) byRegion.set(r, []);
    byRegion.get(r).push(e);
  });

  const FS = 14;
  const GAP = FS * 1.1;
  const INK = '#222';
  let out = '';

  byRegion.forEach((items, region) => {
    const c = centroids[region];
    if(!c) return;
    const totalW = (items.length - 1) * GAP;
    const startX = c[0] - totalW / 2;
    items.forEach((el, i) => {
      const x = startX + i * GAP + (el.dx || 0);
      const y = c[1] + 5 + (el.dy || 0);
      const useItalic = /^[a-zA-Z]$/.test(el.text);
      const fontAttr = useItalic
        ? ` font-family="'Cambria Math','Times New Roman',serif" font-style="italic"`
        : '';
      out += `<text x="${x.toFixed(2)}" y="${y.toFixed(2)}" text-anchor="middle" `
           + `font-size="${FS}" fill="${INK}"${fontAttr}>${el.text}</text>`;
    });
  });

  return out;
}


// ----- 2-set disjoint variant (vงไม่ตัดกัน) -----
// Two circles placed side-by-side with a gap between them.
// Regions: 'A' (whole left circle), 'B' (whole right circle), 'outside' (rest of universe).
// No 'AB' region (since circles don't intersect).
function _venn2Disjoint(spec){
  // ---- canvas ----
  const W = spec.width || 380;
  const H = spec.height || 240;

  // ---- geometry: 2 non-overlapping circles ----
  const r = 60;
  const gap = 40;                     // gap between circles
  const cx = W / 2, cy = H / 2;
  const xA = cx - r - gap / 2;
  const xB = cx + r + gap / 2;

  // universe box
  const ubW = 320, ubH = 180;
  const ubX = cx - ubW / 2, ubY = cy - ubH / 2;

  // ---- defaults ----
  const labels  = spec.labels  || { A: 'A', B: 'B' };
  const regions = spec.regions || {};
  const shadeSet = new Set(spec.shade || []);
  const universe = !!spec.universe;

  // ---- colors ----
  const SHADE = '#b8aa88';
  const SHADE_OP = 0.55;
  const INK = '#222';
  const RULE = '#3a3424';

  const uid = ++_vennIdCounter;
  const M = (n) => `vMask${uid}_${n}`;

  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" `
          + `style="background:#fff;font-family:'Sarabun',sans-serif;">`;

  // 0. <defs> — outside mask only (A and B are full-circle, no mask needed)
  if(universe && shadeSet.has('outside')){
    svg += `<defs>`
         + `<mask id="${M('outside')}" maskUnits="userSpaceOnUse">`
         + `<rect x="${ubX}" y="${ubY}" width="${ubW}" height="${ubH}" fill="white"/>`
         + `<circle cx="${xA}" cy="${cy}" r="${r}" fill="black"/>`
         + `<circle cx="${xB}" cy="${cy}" r="${r}" fill="black"/>`
         + `</mask></defs>`;
  }

  // 1. SHADING
  if(universe && shadeSet.has('outside')){
    svg += `<rect x="0" y="0" width="${W}" height="${H}" `
         + `fill="${SHADE}" opacity="${SHADE_OP}" mask="url(#${M('outside')})"/>`;
  }
  // Whole-circle shade for disjoint A or B (no inner subtraction needed)
  if(shadeSet.has('A')){
    svg += `<circle cx="${xA}" cy="${cy}" r="${r}" fill="${SHADE}" opacity="${SHADE_OP}"/>`;
  }
  if(shadeSet.has('B')){
    svg += `<circle cx="${xB}" cy="${cy}" r="${r}" fill="${SHADE}" opacity="${SHADE_OP}"/>`;
  }

  // 2. UNIVERSE BOX
  if(universe){
    svg += `<rect x="${ubX}" y="${ubY}" width="${ubW}" height="${ubH}" `
         + `fill="none" stroke="${RULE}" stroke-width="1.4"/>`;
    svg += `<text x="${ubX + 8}" y="${ubY + 18}" `
         + `font-family="'Cambria Math','Times New Roman',serif" `
         + `font-size="15" font-style="italic" fill="${INK}">U</text>`;
  }

  // 3. CIRCLES
  svg += `<circle cx="${xA}" cy="${cy}" r="${r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  svg += `<circle cx="${xB}" cy="${cy}" r="${r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;

  // 4. SET LABELS (above each circle)
  const labFS = 16;
  svg += `<text x="${xA}" y="${cy - r - 6}" `
       + `font-family="'Sarabun',sans-serif" `
       + `font-size="${labFS}" fill="${INK}" text-anchor="middle">${labels.A}</text>`;
  svg += `<text x="${xB}" y="${cy - r - 6}" `
       + `font-family="'Sarabun',sans-serif" `
       + `font-size="${labFS}" fill="${INK}" text-anchor="middle">${labels.B}</text>`;

  // 5. REGION TEXT (if any — typically for letter labels)
  const regFS = 16;
  if(regions.A !== undefined){
    svg += `<text x="${xA}" y="${cy + 5}" text-anchor="middle" font-size="${regFS}" fill="${INK}">${regions.A}</text>`;
  }
  if(regions.B !== undefined){
    svg += `<text x="${xB}" y="${cy + 5}" text-anchor="middle" font-size="${regFS}" fill="${INK}">${regions.B}</text>`;
  }
  if(regions.outside !== undefined){
    const ox = universe ? (ubX + ubW - 14) : (W - 14);
    const oy = universe ? (ubY + ubH - 10) : (H - 10);
    svg += `<text x="${ox}" y="${oy}" text-anchor="end" font-size="${regFS}" fill="${INK}">${regions.outside}</text>`;
  }

  // 6. ELEMENT LABELS
  svg += _vennDrawElements(spec, {
    A: [xA, cy],
    B: [xB, cy],
    outside: universe ? [cx, ubY + ubH - 22] : [cx, H - 22]
  });

  return svg + '</svg>';
}


function renderImage(spec){
  if(!spec) return null;
  // Array of specs → render each, wrap in horizontal flex container
  if(Array.isArray(spec)){
    const parts = spec.map(s => renderImage(s)).filter(Boolean);
    if(parts.length === 0) return null;
    return `<div style="display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start;">`
         + parts.map(p => `<div>${p}</div>`).join('')
         + `</div>`;
  }
  if(!spec.type) return null;
  switch(spec.type){
    case 'normal-curve':
      return renderNormalCurve(spec);
    case 'function-plot':
      return renderFunctionPlot(spec);
    case 'ztable-with-curves':
      return renderZTable(spec);
    case 'unit-circle-figure':
      return renderUnitCircle(spec);
    case 'stacked-bar-100':
      return renderStackedBar100(spec);
    case 'polygon-labeled':
      return renderPolygonLabeled(spec);
    case 'stem-leaf':
      return renderStemLeaf(spec);
    case 'venn-diagram':
      return renderVennDiagram(spec);
    // TODO: case '3set-c-in-a-shade-ab-minus-c': return venn3CinA_shadeABminusC_13();
    default:
      return null; // unknown type → admin.html จะ fallback ไปแสดง placeholder
  }
}

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
//   ✅ venn-c-oval / venn-c-in-a  (Q33 / Q36 chap-01-set; portal alias: 3set-c-in-aub, 3set-c-in-a-shade-ab-minus-c)
//   ✅ disk-shading         (Q3 chap-05-function — แผ่นวงกลม + sector/halfplane ตัด clipPath)
//   ✅ number-line          (Q14 chap-05-function — รังสี/จุดทึบ-โปร่ง)
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
//       'parabola-h'       + vertex:[h,k], throughPoint:[px,py], yDomain?:[ymin,ymax]  (sideways x=a(y-k)^2+h, opens right/left; iterates over y — not shadeBetween-compatible)
//       'ellipse-arc'      + center?:[cx,cy], a, b, half?:'upper'|'lower'|'right'|'left', fullOutline?:bool  (half circle/ellipse; upper/lower iterate x, left/right iterate y; fullOutline draws faint dashed full ellipse)
//       'hyperbola'        + center?:[h,k], a, b, orientation?:'horizontal'(default)|'vertical', branches?:'both'(default)|'right'|'left'|'up'|'down', asymptotes?:bool, tRange?:[t0,t1]  (each branch a separate polyline via cosh/sinh; asymptotes drawn dashed/grey first; NOT shadeBetween-compatible)
//       'piecewise-linear' + points:[[x,y],[x,y],...]
//       'polynomial'       + coefs:[aN,...,a1,a0]    (highest degree first; Horner's)
//       'roots-polynomial' + roots:[r1,r2,...], leadingCoef?:1
//     each function also accepts: dashed?:bool (true → เส้นประ), domain?, label?:{text,at:[x,y],anchor?}, strokeWidth?:number (default 1.6; spec.lineWidth = ค่า default ทั้งกราฟ)
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
    if(fn.kind==='rational'){const a=(fn.a!==undefined?fn.a:1),b=fn.b||0,c=fn.c||0;return a/(x-b)+c;}
    return 0;};
  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  svg+=`<defs><marker id="fpArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/></marker></defs>`;
  // grid (behind everything; only when grid + ticks present)
  if(spec.grid){(spec.xTicks||[]).forEach(t=>{if(t===0)return;const xp=x2(t);svg+=`<line x1="${xp.toFixed(2)}" y1="${pT}" x2="${xp.toFixed(2)}" y2="${pT+pH}" stroke="#e8e8e8" stroke-width="0.6"/>`;});
    (spec.yTicks||[]).forEach(t=>{if(t===0)return;const yp=y2(t);svg+=`<line x1="${pX}" y1="${yp.toFixed(2)}" x2="${pX+pW}" y2="${yp.toFixed(2)}" stroke="#e8e8e8" stroke-width="0.6"/>`;});}
  const fnMap={};(spec.functions||[]).forEach(fn=>{fnMap[fn.id]=fn;});
  (spec.shadeBetween||[]).forEach(s=>{const fA=fnMap[s.funcA],fB=fnMap[s.funcB];if(!fA||!fB)return;
    const[xa,xb]=s.xRange,N=120,pts=[];
    for(let i=0;i<=N;i++){const x=xa+(xb-xa)*i/N,y=fnVal(fB,x);pts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}
    for(let i=N;i>=0;i--){const x=xa+(xb-xa)*i/N,y=fnVal(fA,x);pts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}
    svg+=`<polygon points="${pts.join(' ')}" fill="${s.color||'#b8b8b8'}" opacity="0.7"/>`;});
  const ax=spec.axes||{},x0=x2(0),y0=y2(0),arr=ax.arrows?' marker-end="url(#fpArr)"':'';
  svg+=`<line x1="${pX-8}" y1="${y0}" x2="${W-pX+8}" y2="${y0}" stroke="#222" stroke-width="1.2"${arr}/>`;
  svg+=`<line x1="${x0}" y1="${H-pB+8}" x2="${x0}" y2="${pT-8}" stroke="#222" stroke-width="1.2"${arr}/>`;
  // tick marks + numbers (after axes; only if ticks present)
  (spec.xTicks||[]).forEach(t=>{if(t===0)return;const xp=x2(t);svg+=`<line x1="${xp.toFixed(2)}" y1="${(y0-3).toFixed(2)}" x2="${xp.toFixed(2)}" y2="${(y0+3).toFixed(2)}" stroke="#222"/><text x="${xp.toFixed(2)}" y="${(y0+15).toFixed(2)}" text-anchor="middle" font-size="11" fill="#555">${t}</text>`;});
  (spec.yTicks||[]).forEach(t=>{if(t===0)return;const yp=y2(t);svg+=`<line x1="${(x0-3).toFixed(2)}" y1="${yp.toFixed(2)}" x2="${(x0+3).toFixed(2)}" y2="${yp.toFixed(2)}" stroke="#222"/><text x="${(x0-6).toFixed(2)}" y="${(yp+4).toFixed(2)}" text-anchor="end" font-size="11" fill="#555">${t}</text>`;});
  if(ax.xLabel)svg+=`<text x="${W-pX+12}" y="${y0+5}" font-size="14" font-style="italic" fill="#222">${ax.xLabel}</text>`;
  if(ax.yLabel)svg+=`<text x="${x0-8}" y="${pT-6}" font-size="14" font-style="italic" fill="#222" text-anchor="end">${ax.yLabel}</text>`;
  if(ax.originLabel)svg+=`<text x="${x0-6}" y="${y0+14}" font-size="13" fill="#222" text-anchor="end">${ax.originLabel}</text>`;
  (spec.functions||[]).forEach(fn=>{const dom=fn.domain||xR,N=200,col=fn.color||'#222',dashAttr=fn.dashed?' stroke-dasharray="5 4"':'',sw=fn.strokeWidth||spec.lineWidth||1.6;
    if(fn.kind==='parabola-h'){const[h,k]=fn.vertex,[px,py]=fn.throughPoint,a=(px-h)/((py-k)*(py-k)),yd=fn.yDomain||yR,pts=[];
      for(let i=0;i<=N;i++){const y=yd[0]+(yd[1]-yd[0])*i/N,X=a*(y-k)*(y-k)+h;pts.push(`${x2(X).toFixed(2)},${y2(y).toFixed(2)}`);}
      svg+=`<polyline points="${pts.join(' ')}" fill="none" stroke="${col}" stroke-width="${sw}"${dashAttr}/>`;
    }else if(fn.kind==='ellipse-arc'){const[cx,cy]=fn.center||[0,0],aa=fn.a,bb=fn.b,half=fn.half||'upper',pts=[];
      if(fn.fullOutline){svg+=`<ellipse cx="${x2(cx).toFixed(2)}" cy="${y2(cy).toFixed(2)}" rx="${Math.abs(x2(cx+aa)-x2(cx)).toFixed(2)}" ry="${Math.abs(y2(cy+bb)-y2(cy)).toFixed(2)}" fill="none" stroke="${col}" stroke-width="${sw}" stroke-dasharray="5 4"/>`;}
      if(fn.startAngle!==undefined&&fn.endAngle!==undefined){const a0=fn.startAngle*Math.PI/180,a1=fn.endAngle*Math.PI/180;
        for(let i=0;i<=N;i++){const th=a0+(a1-a0)*i/N,x=cx+aa*Math.cos(th),y=cy+bb*Math.sin(th);pts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}}
      else if(half==='upper'||half==='lower'){const s=half==='upper'?1:-1;
        for(let i=0;i<=N;i++){const x=cx-aa+2*aa*i/N,t=1-((x-cx)/aa)**2,y=cy+s*bb*Math.sqrt(Math.max(0,t));pts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}}
      else{const s=half==='right'?1:-1;
        for(let i=0;i<=N;i++){const y=cy-bb+2*bb*i/N,t=1-((y-cy)/bb)**2,x=cx+s*aa*Math.sqrt(Math.max(0,t));pts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}}
      svg+=`<polyline points="${pts.join(' ')}" fill="none" stroke="${col}" stroke-width="${sw}"${dashAttr}/>`;
    }else if(fn.kind==='hyperbola'){const[hh,kk]=fn.center||[0,0],aa=fn.a,bb=fn.b,orient=fn.orientation||'horizontal',br=fn.branches||'both',tr=fn.tRange||[-2,2],NH=140;
      if(fn.asymptotes){const slope=orient==='horizontal'?bb/aa:aa/bb;
        [1,-1].forEach(ss=>{const m=ss*slope,ax1=xM,ax2=xX,ay1=kk+m*(ax1-hh),ay2=kk+m*(ax2-hh);
          svg+=`<line x1="${x2(ax1).toFixed(2)}" y1="${y2(ay1).toFixed(2)}" x2="${x2(ax2).toFixed(2)}" y2="${y2(ay2).toFixed(2)}" stroke="#999" stroke-width="1" stroke-dasharray="4 3"/>`;});}
      let signs;
      if(orient==='horizontal'){signs=br==='right'?[1]:br==='left'?[-1]:[1,-1];}
      else{signs=br==='up'?[1]:br==='down'?[-1]:[1,-1];}
      signs.forEach(s=>{const pts2=[];
        for(let i=0;i<=NH;i++){const t=tr[0]+(tr[1]-tr[0])*i/NH;let X,Y;
          if(orient==='horizontal'){X=hh+s*aa*Math.cosh(t);Y=kk+bb*Math.sinh(t);}
          else{Y=kk+s*aa*Math.cosh(t);X=hh+bb*Math.sinh(t);}
          pts2.push(`${x2(X).toFixed(2)},${y2(Y).toFixed(2)}`);}
        svg+=`<polyline points="${pts2.join(' ')}" fill="none" stroke="${col}" stroke-width="${sw}"${dashAttr}/>`;});
    }else if(fn.kind==='rational'){const b=fn.b||0,runs=[];let cur=[],prevSide=null;
      for(let i=0;i<=N;i++){const x=dom[0]+(dom[1]-dom[0])*i/N,y=fnVal(fn,x),side=(x-b)>=0?1:-1;
        if(prevSide!==null&&side!==prevSide){if(cur.length)runs.push(cur);cur=[];}
        prevSide=side;
        if(y!==null&&isFinite(y))cur.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}
      if(cur.length)runs.push(cur);
      runs.forEach(r=>{if(r.length>1)svg+=`<polyline points="${r.join(' ')}" fill="none" stroke="${col}" stroke-width="${sw}"${dashAttr}/>`;});
    }else{const pts=[];
      for(let i=0;i<=N;i++){const x=dom[0]+(dom[1]-dom[0])*i/N,y=fnVal(fn,x);
        if(y!==null&&isFinite(y))pts.push(`${x2(x).toFixed(2)},${y2(y).toFixed(2)}`);}
      svg+=`<polyline points="${pts.join(' ')}" fill="none" stroke="${col}" stroke-width="${sw}"${dashAttr}/>`;}
    if(fn.label){const[lx,ly]=fn.label.at,anc=fn.label.anchor||'start',lcol=fn.label.color||'#222';
      if(/\\sqrt/.test(fn.label.text)){const fs=14,lw=_nlLatexW(fn.label.text,fs),ox=(anc==='end'?-lw:anc==='middle'?-lw/2:0);
        svg+=_sqMathLabel(fn.label.text,x2(lx)+ox,y2(ly),fs,lcol);}
      else svg+=`<text x="${x2(lx)}" y="${y2(ly)}" font-size="14" font-style="italic" fill="${lcol}" text-anchor="${anc}">${fn.label.text}</text>`;}});
  // straight reference segments (after functions)
  (spec.segments||[]).forEach(s=>{const[fx,fy]=s.from,[tx,ty]=s.to,d=s.dashed?' stroke-dasharray="5 4"':'';
    svg+=`<line x1="${x2(fx).toFixed(2)}" y1="${y2(fy).toFixed(2)}" x2="${x2(tx).toFixed(2)}" y2="${y2(ty).toFixed(2)}" stroke="#222" stroke-width="1.4"${d}/>`;});
  // dots (after segments)
  (spec.dots||[]).forEach(d=>{const cx=x2(d.x).toFixed(2),cy=y2(d.y).toFixed(2);
    // leader line จุด→ป้าย (optional: labelLine:true) วาดใต้จุดก่อน
    if(d.label&&d.labelLine){const dx=(d.labelDx!==undefined?d.labelDx:6),dy=(d.labelDy!==undefined?d.labelDy:-6);
      svg+=`<line x1="${cx}" y1="${cy}" x2="${(x2(d.x)+dx).toFixed(2)}" y2="${(y2(d.y)+dy).toFixed(2)}" stroke="${d.labelLineColor||'#999'}" stroke-width="0.9" stroke-dasharray="3 2"/>`;}
    if(d.open)svg+=`<circle cx="${cx}" cy="${cy}" r="3.5" fill="#fff" stroke="#222" stroke-width="1.4"/>`;
    else svg+=`<circle cx="${cx}" cy="${cy}" r="3.5" fill="#222"/>`;
    if(d.label){const anc=d.labelAnchor||'start',dx=(d.labelDx!==undefined?d.labelDx:6),dy=(d.labelDy!==undefined?d.labelDy:-6);
      svg+=`<text x="${(x2(d.x)+dx).toFixed(2)}" y="${(y2(d.y)+dy).toFixed(2)}" font-size="13" fill="${d.labelColor||'#222'}" text-anchor="${anc}">${d.label}</text>`;}});
  (spec.annotations||[]).forEach(a=>{const[lx,ly]=a.at,anc=a.anchor||'start';
    if(/\\sqrt/.test(a.text)){const fs=13,lw=_nlLatexW(a.text,fs),ox=(anc==='end'?-lw:anc==='middle'?-lw/2:0);
      svg+=_sqMathLabel(a.text,x2(lx)+ox,y2(ly),fs,'#222');}
    else svg+=`<text x="${x2(lx)}" y="${y2(ly)}" font-size="13" fill="#222" text-anchor="${anc}">${a.text}</text>`;
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
function _ucMathToSvg(latex, x, y, fontSize, color) {
  const expr = latex.replace(/^\$|\$$/g, '');
  const col = color || '#222';
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
         + `font-family="${ff}" font-size="${fontSize}" fill="${col}"${it}>${text}</text>`;
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
           + `stroke="${col}" stroke-width="1"/>`;
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
//   dots[]                        - {id, x, y, label?, labelDx?, labelDy?, open?,
//                                    showCoord? (supports LaTeX via $..$),
//                                    coordPos?:{dx,dy}}   open→hollow dot (excluded endpoint)
//   radii[]                       - [{toDot}]
//   chords[]                      - [{fromDot, toDot, extend?, dashed?}]
//                                   extend→lengthen past both ends (long line); dashed→dashed
//   rightAngles[]                 - [{at, refs:[ref1, ref2]}]  small square at vertex
//   perimeterArcs[]               - [{fromDot, toDot, emphasized?, major?, dashed?, arrow?}]
//                                   short arc on circle; major→long arc (>180°);
//                                   dashed→dashed stroke; arrow→arrowhead at toDot (dir fromDot→toDot)
//   shadedSegments[]              - [{fromDot, toDot, major?, fill?, opacity?}]
//                                   fill circular segment cut by chord; major→larger segment
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
       + `<path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/></marker>`;
  // extra colored arrow markers (one per distinct perimeterArc color, so arrowheads match line color)
  const _ucArrColors = Array.from(new Set((spec.perimeterArcs || []).map(a => a.color).filter(Boolean)));
  _ucArrColors.forEach(c => {
    const cid = 'ucArr_' + c.replace(/[^a-zA-Z0-9]/g, '');
    svg += `<marker id="${cid}" viewBox="0 0 10 10" refX="9" refY="5" `
         + `markerWidth="7" markerHeight="7" orient="auto-start-reverse">`
         + `<path d="M 0 0 L 10 5 L 0 10 z" fill="${c}"/></marker>`;
  });
  svg += `</defs>`;

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

  // shadedSegments (fill a circular segment cut by chord fromDot→toDot;
  //   major:true → the larger segment (>half disk). Drawn here so lines/arcs/dots sit on top.
  //   sampled polyline arc → unambiguous fill region. fill/opacity optional.)
  (spec.shadedSegments || []).forEach(seg => {
    const a = dots[seg.fromDot], b = dots[seg.toDot]; if (!a || !b) return;
    const A = Math.atan2(-(a.py - cy), a.px - cx); // math angle (Y-up) of a
    const B = Math.atan2(-(b.py - cy), b.px - cx); // math angle (Y-up) of b
    let d = B - A;
    while (d <= -Math.PI) d += 2 * Math.PI;
    while (d > Math.PI) d -= 2 * Math.PI;          // short signed span A→B in (-π, π]
    if (seg.major) { d = d > 0 ? d - 2 * Math.PI : d + 2 * Math.PI; } // long way round
    const N = 64;
    const pts = [`${a.px.toFixed(2)},${a.py.toFixed(2)}`,
                 `${b.px.toFixed(2)},${b.py.toFixed(2)}`];
    for (let i = 1; i <= N; i++) {                  // arc from B back to A along chosen span
      const ang = (A + d) - d * (i / N);
      const px = cx + radius * Math.cos(ang);
      const py = cy - radius * Math.sin(ang);
      pts.push(`${px.toFixed(2)},${py.toFixed(2)}`);
    }
    const fill = seg.fill || '#7a6e54';
    const op = seg.opacity != null ? seg.opacity : 0.20;
    svg += `<polygon points="${pts.join(' ')}" fill="${fill}" fill-opacity="${op}" stroke="none"/>`;
  });

  // radii (origin → dot)
  (spec.radii || []).forEach(r => {
    const d = dots[r.toDot]; if (!d) return;
    svg += `<line x1="${cx}" y1="${cy}" x2="${d.px}" y2="${d.py}" stroke="#222" stroke-width="1.2"/>`;
  });

  // chords (dot → dot; extend → lengthen past both ends into a long line;
  //         dashed → dashed stroke)
  (spec.chords || []).forEach(c => {
    const a = dots[c.fromDot], b = dots[c.toDot]; if (!a || !b) return;
    if (!c.extend && !c.dashed) {
      // legacy path (byte-identical to original) for plain chords
      svg += `<line x1="${a.px}" y1="${a.py}" x2="${b.px}" y2="${b.py}" stroke="#222" stroke-width="1.2"/>`;
      return;
    }
    let x1 = a.px, y1 = a.py, x2 = b.px, y2 = b.py;
    if (c.extend) {
      const dx = x2 - x1, dy = y2 - y1, L = Math.sqrt(dx*dx + dy*dy) || 1;
      const ux = dx/L, uy = dy/L;
      const e = (typeof c.extend === 'number') ? c.extend : radius * 0.5;
      x1 -= ux*e; y1 -= uy*e; x2 += ux*e; y2 += uy*e;
    }
    const dash = c.dashed ? ' stroke-dasharray="5 4"' : '';
    svg += `<line x1="${x1.toFixed(2)}" y1="${y1.toFixed(2)}" x2="${x2.toFixed(2)}" y2="${y2.toFixed(2)}" stroke="#222" stroke-width="1.2"${dash}/>`;
  });

  // perimeterArcs (along main circle; emphasized=thicker, major=long arc (>180°),
  //                dashed=dashed stroke, arrow=arrowhead at toDot end (dir = fromDot→toDot))
  (spec.perimeterArcs || []).forEach(arc => {
    const a = dots[arc.fromDot], b = dots[arc.toDot]; if (!a || !b) return;
    const t1 = Math.atan2(a.py - cy, a.px - cx);
    const t2 = Math.atan2(b.py - cy, b.px - cx);
    let dt = t2 - t1;
    while (dt > Math.PI) dt -= 2 * Math.PI;
    while (dt <= -Math.PI) dt += 2 * Math.PI;
    // default = minor arc (<=180°). major:true → complementary long arc (flip sweep + largeArc).
    let sweep = dt > 0 ? 1 : 0;
    let largeArc = 0;
    if (arc.major) { sweep = sweep ? 0 : 1; largeArc = 1; }
    const w = arc.emphasized ? 2.8 : 1.4;
    const dash = arc.dashed ? ' stroke-dasharray="5 4"' : '';
    const col = arc.color || '#222';
    const mkId = arc.color ? ('ucArr_' + arc.color.replace(/[^a-zA-Z0-9]/g, '')) : 'ucArr';
    const mk = arc.arrow ? ` marker-end="url(#${mkId})"` : '';
    svg += `<path d="M ${a.px.toFixed(2)} ${a.py.toFixed(2)} A ${radius} ${radius} 0 ${largeArc} ${sweep} ${b.px.toFixed(2)} ${b.py.toFixed(2)}" fill="none" stroke="${col}" stroke-width="${w}"${dash}${mk}/>`;
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
    if (d.open) {
      // hollow dot = open/excluded endpoint (e.g. strict inequality boundary)
      svg += `<circle cx="${dt.px}" cy="${dt.py}" r="3.6" fill="#fff" stroke="#222" stroke-width="1.4"/>`;
    } else {
      svg += `<circle cx="${dt.px}" cy="${dt.py}" r="3" fill="#222"/>`;
    }
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
// Math label renderer for polygon-labeled (native SVG, supports \sqrt{} with
// vinculum). anchor: 'start' | 'middle' | 'end'. Vertical baseline = central (y = center).
function _polyMathToSvg(latex, x, y, fontSize, anchor){
  const expr = latex.replace(/^\$|\$$/g, '');
  const ff = "'Cambria Math','Times New Roman',serif";
  function chW(ch){
    if(ch === ',' || ch === ' ') return fontSize * 0.3;
    if(ch === '(' || ch === ')') return fontSize * 0.4;
    if(ch === '−' || ch === '-') return fontSize * 0.55;
    if(ch === '√') return fontSize * 0.7;
    return fontSize * 0.55;
  }
  const toks = []; let i = 0;
  while(i < expr.length){
    const m = /^\\sqrt\s*\{([^}]*)\}/.exec(expr.substring(i));
    if(m){ toks.push({t:'sqrt', rad:m[1]}); i += m[0].length; continue; }
    const supM = /^\^\{([^}]*)\}/.exec(expr.substring(i)) || /^\^(.)/.exec(expr.substring(i));
    if(supM){ toks.push({t:'sup', s:supM[1]}); i += supM[0].length; continue; }
    if(expr.substr(i,2) === '\\ '){ toks.push({t:'sp', w:fontSize*0.3}); i += 2; continue; }
    if(expr.substr(i,2) === '\\,'){ toks.push({t:'sp', w:fontSize*0.2}); i += 2; continue; }
    if(expr[i] === '-'){ toks.push({t:'txt', s:'−', italic:false}); i += 1; continue; }
    const isLetter = /[a-zA-Z]/.test(expr[i]);
    let end = i;
    while(end < expr.length && expr[end] !== '\\' && expr[end] !== '-' && expr[end] !== '^'
          && (/[a-zA-Z]/.test(expr[end]) === isLetter)) end++;
    toks.push({t:'txt', s:expr.substring(i,end), italic:isLetter}); i = end;
  }
  function tokW(tk){
    if(tk.t === 'sp') return tk.w;
    if(tk.t === 'sqrt'){ let w = chW('√'); for(const c of tk.rad) w += chW(c); return w; }
    if(tk.t === 'sup'){ let w = 0; for(const c of tk.s) w += chW(c)*0.7; return w; }
    let w = 0; for(const c of tk.s) w += chW(c); return w;
  }
  let total = 0; for(const tk of toks) total += tokW(tk);
  let cur = anchor === 'middle' ? x - total/2 : (anchor === 'end' ? x - total : x);
  const barY = y - fontSize * 0.55;
  let out = '';
  function emit(text, italic){
    const it = italic ? ' font-style="italic"' : '';
    out += `<text x="${cur.toFixed(2)}" y="${y.toFixed(2)}" font-family="${ff}" `
         + `font-size="${fontSize}" fill="#222" dominant-baseline="central"${it}>${text}</text>`;
  }
  for(const tk of toks){
    if(tk.t === 'sp'){ cur += tk.w; continue; }
    if(tk.t === 'sqrt'){
      emit('√', false); cur += chW('√');
      let radW = 0; for(const c of tk.rad) radW += chW(c);
      out += `<line x1="${(cur-1).toFixed(2)}" y1="${barY.toFixed(2)}" `
           + `x2="${(cur+radW+1).toFixed(2)}" y2="${barY.toFixed(2)}" stroke="#222" stroke-width="1"/>`;
      emit(tk.rad, false); cur += radW; continue;
    }
    if(tk.t === 'sup'){
      const supFs = fontSize * 0.7, supY = y - fontSize * 0.35;
      out += `<text x="${cur.toFixed(2)}" y="${supY.toFixed(2)}" font-family="${ff}" `
           + `font-size="${supFs}" fill="#222" dominant-baseline="central">${tk.s}</text>`;
      cur += tokW(tk); continue;
    }
    emit(tk.s, tk.italic); cur += tokW(tk);
  }
  return out;
}
function _polyHasMath(s){ return typeof s === 'string' && (s.indexOf('\\sqrt') !== -1 || s.indexOf('$') !== -1); }

function renderPolygonLabeled(spec){
  const W = spec.width || 380;
  const H = spec.height || 300;
  const verts = spec.vertices || {};
  const vLabels = spec.vertexLabels || {};
  const sides = spec.sides || [];
  const angleMarks = spec.angleMarks || [];
  const annotations = spec.annotations || [];
  const ellipses = spec.ellipses || [];

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

  // --- (-1) Shade regions (absolute bottom: circle/polygon boundaries, evenodd) ---
  const shadeRegions = spec.shadeRegions || [];
  shadeRegions.forEach(sr => {
    const fill = sr.fill || '#8fb3e0';
    const op = (sr.op != null) ? sr.op : 0.55;
    const rule = sr.fillRule || 'evenodd';
    let d = '';
    (sr.parts || []).forEach(pt => {
      if (pt.circle) {
        const cc = pt.circle.center, cr = pt.circle.r;
        d += `M ${(cc[0]-cr).toFixed(2)} ${cc[1].toFixed(2)} `
           + `A ${cr} ${cr} 0 1 0 ${(cc[0]+cr).toFixed(2)} ${cc[1].toFixed(2)} `
           + `A ${cr} ${cr} 0 1 0 ${(cc[0]-cr).toFixed(2)} ${cc[1].toFixed(2)} Z `;
      } else if (pt.polygon) {
        const pts = pt.polygon.map(n => V(n));
        d += 'M ' + pts.map(p => `${p[0].toFixed(2)} ${p[1].toFixed(2)}`).join(' L ') + ' Z ';
      }
    });
    if (d) svg += `<path d="${d}" fill="${fill}" fill-opacity="${op}" fill-rule="${rule}" stroke="none"/>`;
  });

  // --- 0. Ellipses (very bottom layer) ---
  // {from, to, minorRatio, style}: major axis = segment from→to (e.g. two vertices),
  // minor semi-axis = (major semi-axis) * minorRatio. Drawn rotated to align with from→to.
  ellipses.forEach(el => {
    const p1 = V(el.from), p2 = V(el.to);
    const cx = (p1[0] + p2[0]) / 2, cy = (p1[1] + p2[1]) / 2;
    const dx = p2[0] - p1[0], dy = p2[1] - p1[1];
    const a = Math.sqrt(dx*dx + dy*dy) / 2;
    const ratio = (el.minorRatio != null) ? el.minorRatio : 0.5;
    const b = a * ratio;
    const ang = Math.atan2(dy, dx) * 180 / Math.PI;
    const dash = (el.style === 'dashed') ? ' stroke-dasharray="4 3"' : '';
    svg += `<ellipse cx="${cx.toFixed(2)}" cy="${cy.toFixed(2)}" `
         + `rx="${a.toFixed(2)}" ry="${b.toFixed(2)}" fill="none" `
         + `stroke="#222" stroke-width="1.2"${dash} `
         + `transform="rotate(${ang.toFixed(2)} ${cx.toFixed(2)} ${cy.toFixed(2)})"/>`;
  });

  // --- 1. Sides (drawn over ellipses) ---
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
    if(_polyHasMath(s.label)){
      svg += _polyMathToSvg(s.label, lx, ly, 15, 'middle');
    } else {
      svg += `<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" `
           + `font-family="'Cambria Math','Times New Roman',serif" `
           + `font-size="15" fill="#222" text-anchor="middle" `
           + `dominant-baseline="central">${s.label}</text>`;
    }
  });

  // --- 4. Vertex labels (top layer) ---
  Object.keys(verts).forEach(name => {
    const p = V(name);
    const off = vLabels[name] || {};
    const lx = p[0] + (off.dx || 0);
    const ly = p[1] + (off.dy || 0);
    svg += `<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" `
         + `font-family="'Cambria Math','Times New Roman',serif" `
         + `font-size="18" fill="#222">${(vLabels[name] && vLabels[name].text) || name}</text>`;
  });

  // --- 5. Free-form annotations (top, optional) ---
  annotations.forEach(a => {
    const fs = a.fontSize || 14;
    const anchor = a.anchor || 'start';
    if(_polyHasMath(a.text)){
      svg += _polyMathToSvg(a.text, a.x, a.y, fs, anchor);
    } else {
      svg += `<text x="${a.x}" y="${a.y}" `
           + `font-family="'Cambria Math','Times New Roman',serif" `
           + `font-size="${fs}" fill="#222" text-anchor="${anchor}">${a.text||''}</text>`;
    }
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
  if(sets === 3 && layout === 'intersecting'){
    return _venn3Intersecting(spec);
  }
  return null;   // other variants → future iterations
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


// ----- 3-set intersecting variant (3 วงตัดกัน) -----
// Three equal circles arranged at vertices of an equilateral triangle:
// A = top-left, B = top-right, C = bottom-center.
// Region IDs: A_only · B_only · C_only · AB_only · AC_only · BC_only · ABC · outside
//
// DESIGN:
// - Set labels positioned via outward unit vector from triangle centroid.
//   labOff = r + 32 → labels sit clearly outside the circles (no edge overlap).
// - Region text positions tuned so AB_only / AC_only / BC_only stay ≥ 18px
//   away from the EXCLUDED circle's edge while remaining safely inside their
//   included circles (verified via geometry: edge clearance 18.4–19.8 px).
// - Shading: single-circle regions via <mask>; lenses (Aᵢ∩Aⱼ) and the central
//   region (A∩B∩C) via explicit <path> arcs. NO nested clip-path — that renders
//   EMPTY in some browsers (confirmed). All 7 regions are pairwise disjoint, so
//   they paint at uniform opacity in any order. Verified pixel-exact vs resvg.
function _venn3Intersecting(spec){
  // ---- canvas ----
  const W = spec.width || 400;
  const capH = spec.caption ? 30 : 0;     // optional title strip (e.g. choice number)
  const contentH = spec.height || 360;
  const H = contentH + capH;

  // ---- geometry: equilateral triangle of centers ----
  const r = 68;             // circle radius
  const d = 70;             // center-to-center distance
  const cx = W / 2;
  const cy = capH + contentH / 2 - 4;     // shift content below caption strip
  const triH = d * Math.sqrt(3) / 2;
  // A = top-left, B = top-right, C = bottom-center
  const xA = cx - d/2, yA = cy - triH/3;
  const xB = cx + d/2, yB = cy - triH/3;
  const xC = cx,       yC = cy + 2*triH/3;
  // Triangle centroid = (cx, cy) by construction — used for outward label vectors
  const tcx = cx, tcy = cy;

  // ---- universe box ----
  const ubW = 360, ubH = 310;
  const ubX = cx - ubW/2;
  const ubY = cy - ubH/2;

  // ---- defaults ----
  const labels  = spec.labels  || { A: 'A', B: 'B', C: 'C' };
  const regions = spec.regions || {};
  const shadeSet = new Set(spec.shade || []);
  const universe = !!spec.universe;

  // ---- colors ----
  const SHADE = '#b8aa88';
  const SHADE_OP = 0.55;
  const INK = '#222';
  const RULE = '#3a3424';

  // ---- unique mask IDs (per-call, prevents collisions across multiple venns) ----
  const uid = ++_vennIdCounter;
  const M = (n) => `vM${uid}_${n}`;

  // ---- shading helpers: mask (single-circle − others) + <path> (lens, central) ----
  //   NO nested clip-path (renders empty in some browsers); mask+path is the proven approach.
  const F2 = (v) => v.toFixed(2);
  const ctrOf = { A:[xA,yA], B:[xB,yB], C:[xC,yC] };
  // equal-radius circle∩circle → [Q(+normal), Q(−normal)]
  function isect3(x1,y1,x2,y2){
    const dx=x2-x1, dy=y2-y1, dd=Math.sqrt(dx*dx+dy*dy);
    const hh=Math.sqrt(Math.max(0, r*r - (dd/2)*(dd/2)));
    const mx=(x1+x2)/2, my=(y1+y2)/2, nx=-dy/dd, ny=dx/dd;
    return [{x:mx+nx*hh, y:my+ny*hh}, {x:mx-nx*hh, y:my-ny*hh}];
  }
  // full lens (Pᵢ∩Pⱼ): arc of circ-i then arc of circ-j (sweep 1,1 — verified vs resvg)
  function lensPath3(x1,y1,x2,y2){
    const q=isect3(x1,y1,x2,y2);
    return `M ${F2(q[0].x)} ${F2(q[0].y)} A ${r} ${r} 0 0 1 ${F2(q[1].x)} ${F2(q[1].y)} `
         + `A ${r} ${r} 0 0 1 ${F2(q[0].x)} ${F2(q[0].y)} Z`;
  }
  // inner intersection of a pair (closer to triangle centroid tcx,tcy)
  function innerPt(x1,y1,x2,y2){
    const q=isect3(x1,y1,x2,y2);
    return (Math.hypot(q[0].x-tcx,q[0].y-tcy) < Math.hypot(q[1].x-tcx,q[1].y-tcy)) ? q[0] : q[1];
  }
  // central A∩B∩C: innerAB →(arc A)→ innerAC →(arc C)→ innerBC →(arc B)→ back (sweep 0,0,0 — verified)
  function abcPath3(){
    const iAB=innerPt(xA,yA,xB,yB), iAC=innerPt(xA,yA,xC,yC), iBC=innerPt(xB,yB,xC,yC);
    return `M ${F2(iAB.x)} ${F2(iAB.y)} `
         + `A ${r} ${r} 0 0 0 ${F2(iAC.x)} ${F2(iAC.y)} `
         + `A ${r} ${r} 0 0 0 ${F2(iBC.x)} ${F2(iBC.y)} `
         + `A ${r} ${r} 0 0 0 ${F2(iAB.x)} ${F2(iAB.y)} Z`;
  }

  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" `
          + `style="background:#fff;font-family:'Sarabun',sans-serif;">`;

  // 0b. CAPTION (optional title strip, e.g. choice label "1.")
  if(spec.caption){
    svg += `<text x="${W/2}" y="21" text-anchor="middle" font-size="18" `
         + `font-weight="bold" fill="${INK}" font-family="'Sarabun',sans-serif">${spec.caption}</text>`;
  }

  // 0. <defs> — masks: single-circle regions (incl − excl) + lens-minus-third
  svg += `<defs>`;
  const SHADE_RECT = `<rect x="0" y="0" width="${W}" height="${H}"`;
  const singleDef = { A_only:['A',['B','C']], B_only:['B',['A','C']], C_only:['C',['A','B']] };
  Object.keys(singleDef).forEach(k => {
    if(!shadeSet.has(k)) return;
    const inc=singleDef[k][0], exc=singleDef[k][1];
    svg += `<mask id="${M(k)}" maskUnits="userSpaceOnUse">`
         + `${SHADE_RECT} fill="black"/>`
         + `<circle cx="${ctrOf[inc][0]}" cy="${ctrOf[inc][1]}" r="${r}" fill="white"/>`
         + exc.map(e=>`<circle cx="${ctrOf[e][0]}" cy="${ctrOf[e][1]}" r="${r}" fill="black"/>`).join('')
         + `</mask>`;
  });
  const lensDef = { AB_only:'C', AC_only:'B', BC_only:'A' };
  Object.keys(lensDef).forEach(k => {
    if(!shadeSet.has(k)) return;
    const e=lensDef[k];
    svg += `<mask id="${M(k)}" maskUnits="userSpaceOnUse">`
         + `${SHADE_RECT} fill="white"/>`
         + `<circle cx="${ctrOf[e][0]}" cy="${ctrOf[e][1]}" r="${r}" fill="black"/></mask>`;
  });
  svg += `</defs>`;

  // 1. UNIVERSE BOX (drawn first so circles + shading sit on top)
  if(universe){
    svg += `<rect x="${ubX}" y="${ubY}" width="${ubW}" height="${ubH}" `
         + `fill="none" stroke="${RULE}" stroke-width="1.4"/>`;
    svg += `<text x="${ubX + 10}" y="${ubY + 20}" `
         + `font-family="'Cambria Math','Times New Roman',serif" `
         + `font-size="15" font-style="italic" fill="${INK}">U</text>`;
  }

  // 2. SHADING — all 7 regions are pairwise DISJOINT → uniform opacity, order-independent.
  //    single-circle regions via <mask>; lenses & central region via explicit <path>.
  const SH = `fill="${SHADE}" opacity="${SHADE_OP}"`;
  if(shadeSet.has('A_only'))  svg += `${SHADE_RECT} ${SH} mask="url(#${M('A_only')})"/>`;
  if(shadeSet.has('B_only'))  svg += `${SHADE_RECT} ${SH} mask="url(#${M('B_only')})"/>`;
  if(shadeSet.has('C_only'))  svg += `${SHADE_RECT} ${SH} mask="url(#${M('C_only')})"/>`;
  if(shadeSet.has('AB_only')) svg += `<path d="${lensPath3(xA,yA,xB,yB)}" ${SH} mask="url(#${M('AB_only')})"/>`;
  if(shadeSet.has('AC_only')) svg += `<path d="${lensPath3(xA,yA,xC,yC)}" ${SH} mask="url(#${M('AC_only')})"/>`;
  if(shadeSet.has('BC_only')) svg += `<path d="${lensPath3(xB,yB,xC,yC)}" ${SH} mask="url(#${M('BC_only')})"/>`;
  if(shadeSet.has('ABC'))     svg += `<path d="${abcPath3()}" ${SH}/>`;

  // 3. CIRCLE OUTLINES (drawn AFTER shading so they sit visibly on top)
  svg += `<circle cx="${xA}" cy="${yA}" r="${r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  svg += `<circle cx="${xB}" cy="${yB}" r="${r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  svg += `<circle cx="${xC}" cy="${yC}" r="${r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;

  // 4. SET LABELS — outward unit vector from triangle centroid, offset r+32
  const labFS = 17;
  const labOff = r + 32;
  function outwardLabel(xCirc, yCirc, txt){
    const dx = xCirc - tcx, dy = yCirc - tcy;
    const len = Math.sqrt(dx*dx + dy*dy);
    const ux = dx/len, uy = dy/len;
    const lx = xCirc + ux * labOff;
    const ly = yCirc + uy * labOff + 5;
    return `<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" `
         + `font-family="'Cambria Math','Times New Roman',serif" `
         + `font-size="${labFS}" font-style="italic" fill="${INK}" text-anchor="middle">${txt}</text>`;
  }
  svg += outwardLabel(xA, yA, labels.A);
  svg += outwardLabel(xB, yB, labels.B);
  svg += outwardLabel(xC, yC, labels.C);

  // 5. REGION TEXT (centroid placement, tuned for 18+ px edge clearance from excluded circles)
  const regFS = 14;
  const positions = {
    A_only:  [xA - r*0.50,           yA - r*0.10],
    B_only:  [xB + r*0.50,           yB - r*0.10],
    C_only:  [xC,                     yC + r*0.55],
    AB_only: [(xA+xB)/2,             (yA+yB)/2 - r*0.40],   // ↑ away from C top
    AC_only: [(xA+xC)/2 - r*0.36,    (yA+yC)/2 + r*0.13],   // ← away from B
    BC_only: [(xB+xC)/2 + r*0.36,    (yB+yC)/2 + r*0.13],   // → away from A
    ABC:     [cx,                     cy + triH/6 + 2],
  };
  Object.entries(positions).forEach(([key, pos]) => {
    if(regions[key] !== undefined){
      const txt = String(regions[key]);
      const useItalic = /^[a-zA-Z]$/.test(txt);
      const fontAttr = useItalic
        ? ` font-family="'Cambria Math','Times New Roman',serif" font-style="italic"`
        : '';
      svg += `<text x="${pos[0].toFixed(2)}" y="${(pos[1]+5).toFixed(2)}" `
           + `text-anchor="middle" font-size="${regFS}" fill="${INK}"${fontAttr}>${txt}</text>`;
    }
  });
  if(regions.outside !== undefined){
    const ox = universe ? (ubX + ubW - 14) : (W - 14);
    const oy = universe ? (ubY + ubH - 14) : (H - 14);
    const txt = String(regions.outside);
    svg += `<text x="${ox}" y="${oy}" text-anchor="end" font-size="${regFS}" fill="${INK}">${txt}</text>`;
  }

  return svg + '</svg>';
}


// ----- adapter: 3set-labeled (portal schema) -> _venn3Intersecting -----
// Portal's lessons embed copies using this shape; bank stores imageSpec in
// THIS shape so portal wires directly with no mapping. Adapter only renames
// keys + converts labels array->object, then reuses the existing 3-set venn.
//   portal:  { type:"3set-labeled", labels:["ก","ข","ค"],
//              values:{aOnly,bOnly,cOnly,abNotC,acNotB,bcNotA,abc,outside},
//              width (CSS max-width), height (ignored) }
// GUARD: skip any region whose value is undefined/null/"" so we never emit
//        "undefined"/"null"/empty text (matches portal's blank rule). A value
//        of "?" passes through verbatim and renders as "?" (intended).
function render3SetLabeled(spec){
  if(!spec || spec.type !== '3set-labeled') return null;
  const v = spec.values || {};
  const KEYMAP = {
    aOnly:'A_only', bOnly:'B_only', cOnly:'C_only',
    abNotC:'AB_only', acNotB:'AC_only', bcNotA:'BC_only',
    abc:'ABC', outside:'outside'
  };
  const regions = {};
  for(const pk in KEYMAP){
    const val = v[pk];
    if(val === undefined || val === null || val === '') continue; // blank guard
    regions[KEYMAP[pk]] = val; // verbatim — "?" stays "?"
  }
  const lab = Array.isArray(spec.labels) ? spec.labels : ['A','B','C'];
  const innerSpec = {
    type: 'venn-diagram', sets: 3, layout: 'intersecting',
    labels: { A: (lab[0] != null ? lab[0] : 'A'),
              B: (lab[1] != null ? lab[1] : 'B'),
              C: (lab[2] != null ? lab[2] : 'C') },
    regions,
    universe: (regions.outside !== undefined), // outside present -> draw U box
    width: 400, height: 380                    // match portal's fixed viewBox
  };
  const inner = renderVennDiagram(innerSpec);
  if(!inner) return null;
  const cssW = spec.width || 240;              // portal default when omitted
  return `<div style="max-width:${cssW}px;">${inner}</div>`;
}

// ----- venn: C nested inside A, B intersects A (C disjoint from B) -----
// topology โจทย์ "C ⊂ A, B ตัด A" (เช่น Q36 Entrance 2530)
//   shade:['AB'] = แรเงา A∩B (lens), punch C → semantically (A∩B)−C
function venn3CinA(spec){
  if(!spec || spec.type !== 'venn-c-in-a') return null;
  const W = spec.width || 300;
  const capH = spec.caption ? 30 : 0;
  const contentH = spec.height || 200;
  const H = contentH + capH;
  const INK='#222', RULE='#3a3424', SHADE='#b8aa88', SHADE_OP=0.55;
  const cy = capH + contentH/2;
  const A = { x: W*0.42, y: cy, r: 70 };
  const B = { x: W*0.70, y: cy, r: 54 };
  const C = { x: W*0.50, y: cy, r: 37 };   // C⊆A but reaches into A∩B → punch makes (A∩B)−C
  const labels = spec.labels || {A:'A',B:'B',C:'C'};
  const shadeSet = new Set(spec.shade || []);
  const uid = ++_vennIdCounter;
  const CP = (n)=>`vci${uid}_${n}`;
  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:'Sarabun',sans-serif;">`;
  if(spec.caption){
    svg += `<text x="${W/2}" y="21" text-anchor="middle" font-size="18" font-weight="bold" `
         + `fill="${INK}" font-family="'Sarabun',sans-serif">${spec.caption}</text>`;
  }
  svg += `<defs>`
       + `<clipPath id="${CP('A')}"><circle cx="${A.x}" cy="${A.y}" r="${A.r}"/></clipPath>`
       + `<clipPath id="${CP('B')}"><circle cx="${B.x}" cy="${B.y}" r="${B.r}"/></clipPath>`
       + `</defs>`;
  if(shadeSet.has('AB')){
    let inner = `<rect x="0" y="0" width="${W}" height="${H}" fill="${SHADE}" opacity="${SHADE_OP}"/>`;
    inner += `<circle cx="${C.x}" cy="${C.y}" r="${C.r}" fill="white"/>`;
    inner = `<g clip-path="url(#${CP('B')})">${inner}</g>`;
    inner = `<g clip-path="url(#${CP('A')})">${inner}</g>`;
    svg += inner;
  }
  svg += `<circle cx="${A.x}" cy="${A.y}" r="${A.r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  svg += `<circle cx="${B.x}" cy="${B.y}" r="${B.r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  svg += `<circle cx="${C.x}" cy="${C.y}" r="${C.r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  const lab=(x,y,t)=>`<text x="${x.toFixed(1)}" y="${y.toFixed(1)}" `
       + `font-family="'Cambria Math','Times New Roman',serif" font-size="17" font-style="italic" `
       + `fill="${INK}" text-anchor="middle">${t}</text>`;
  svg += lab(A.x - A.r*0.92, A.y - A.r*0.78, labels.A);
  svg += lab(B.x + B.r*0.78, B.y - B.r*0.82, labels.B);
  svg += lab(C.x - C.r*0.5, C.y + 5, labels.C);
  return svg + '</svg>';
}

// ----- venn: C is a horizontal ellipse spanning A∪B (C ⊆ A∪B) -----
// topology โจทย์ "C วงรีพาด A∪B" (เช่น Q33 Entrance 2525); universe box default
function venn3COval(spec){
  if(!spec || spec.type !== 'venn-c-oval') return null;
  const W = spec.width || 320;
  const capH = spec.caption ? 30 : 0;
  const H = capH + 245;
  const INK='#222', RULE='#3a3424';
  const universe = (spec.universe !== false);
  const labels = spec.labels || {A:'A',B:'B',C:'C'};
  const y0 = capH;
  const A = { x:118, y:y0+115, r:66 };
  const B = { x:204, y:y0+115, r:66 };
  const C = { x:161, y:y0+115, rx:80, ry:27 };   // center = A,B center → ห่างจุดตัดบน-ล่างเท่ากัน
  const ubX=18, ubY=y0+30, ubW=284, ubH=200;
  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:'Sarabun',sans-serif;">`;
  if(spec.caption){
    svg += `<text x="${W/2}" y="21" text-anchor="middle" font-size="18" font-weight="bold" `
         + `fill="${INK}" font-family="'Sarabun',sans-serif">${spec.caption}</text>`;
  }
  if(universe){
    svg += `<rect x="${ubX}" y="${ubY}" width="${ubW}" height="${ubH}" fill="none" stroke="${RULE}" stroke-width="1.4"/>`;
  }
  svg += `<circle cx="${A.x}" cy="${A.y}" r="${A.r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  svg += `<circle cx="${B.x}" cy="${B.y}" r="${B.r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  svg += `<ellipse cx="${C.x}" cy="${C.y}" rx="${C.rx}" ry="${C.ry}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  const lab=(x,y,t)=>`<text x="${x.toFixed(1)}" y="${y.toFixed(1)}" `
       + `font-family="'Cambria Math','Times New Roman',serif" font-size="17" font-style="italic" `
       + `fill="${INK}" text-anchor="middle">${t}</text>`;
  svg += lab(A.x - A.r*0.82, A.y - A.r*0.74, labels.A);
  svg += lab(B.x + B.r*0.82, B.y - B.r*0.74, labels.B);
  svg += lab(C.x - C.rx - 14, C.y + 5,        labels.C);
  if(universe){
    svg += `<text x="${ubX+ubW-14}" y="${ubY+ubH-12}" text-anchor="end" `
         + `font-family="'Cambria Math','Times New Roman',serif" font-size="16" font-style="italic" `
         + `fill="${INK}">${spec.universeLabel || 'U'}</text>`;
  }
  return svg + '</svg>';
}

// ----- venn: C nested inside (A − B); B intersects A; C disjoint from B -----
// topology โจทย์ "C ⊂ (A − B)" → C อยู่ในส่วน A-only (ซ้าย) ห่าง B ชัด, A∩B ยังมีได้
//   shade tokens (atomic, ต่อกันได้): 'A_only' = (A−B)−C , 'C' = วง C , 'AB' = A∩B , 'B_only' = B−A
//   ตัวอย่างประกอบ:  A∪B = ['A_only','C','AB','B_only'] ;  A = ['A_only','C','AB'] ;
//                    B∪C = ['B_only','AB','C'] ;  (A∩B)∪C = ['AB','C'] ;  B−A = ['B_only']
function venn3CinAOnly(spec){
  if(!spec || spec.type !== 'venn-c-in-a-only') return null;
  const W = spec.width || 300;
  const capH = spec.caption ? 30 : 0;
  const contentH = spec.height || 210;
  const H = contentH + capH;
  const INK='#222', RULE='#3a3424', SHADE='#b8aa88', SHADE_OP=0.55;
  const cy = capH + contentH/2;
  // geometry (verified): C⊆A, C∩B=∅, A∩B≠∅, C ซ้ายของ lens
  const A = { x: W*0.40, y: cy, r: 78 };
  const B = { x: W*0.70, y: cy, r: 62 };
  const C = { x: W*0.30, y: cy, r: 28 };
  const labels = spec.labels || {A:'A',B:'B',C:'C'};
  const shadeSet = new Set(spec.shade || []);
  const uid = ++_vennIdCounter;
  const M = (n)=>`vcao${uid}_${n}`;

  // A∩B lens (centers share y=cy): intersection points (xi, cy±hi)
  const dAB = B.x - A.x;
  const aDist = (dAB*dAB + A.r*A.r - B.r*B.r) / (2*dAB);
  const xi = A.x + aDist;
  const hi = Math.sqrt(Math.max(0, A.r*A.r - aDist*aDist));
  // right boundary = arc of A; left boundary = arc of B (both short, CW) — proven 2-set technique
  const lensPath = `M ${xi.toFixed(2)} ${(cy-hi).toFixed(2)} `
                 + `A ${A.r} ${A.r} 0 0 1 ${xi.toFixed(2)} ${(cy+hi).toFixed(2)} `
                 + `A ${B.r} ${B.r} 0 0 1 ${xi.toFixed(2)} ${(cy-hi).toFixed(2)} Z`;

  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:'Sarabun',sans-serif;">`;
  if(spec.caption){
    svg += `<text x="${W/2}" y="21" text-anchor="middle" font-size="18" font-weight="bold" `
         + `fill="${INK}" font-family="'Sarabun',sans-serif">${spec.caption}</text>`;
  }
  // SHADING — uses <mask> (single-circle regions) + explicit <path> (lens); NO nested clip-path
  // (nested clip-path-on-<g> renders empty in some browsers; mask+path is the proven 2-set approach)
  svg += `<defs>`;
  if(shadeSet.has('A_only')){
    // A − B − C
    svg += `<mask id="${M('Aonly')}" maskUnits="userSpaceOnUse">`
         + `<rect x="0" y="0" width="${W}" height="${H}" fill="black"/>`
         + `<circle cx="${A.x}" cy="${A.y}" r="${A.r}" fill="white"/>`
         + `<circle cx="${B.x}" cy="${B.y}" r="${B.r}" fill="black"/>`
         + `<circle cx="${C.x}" cy="${C.y}" r="${C.r}" fill="black"/>`
         + `</mask>`;
  }
  if(shadeSet.has('B_only')){
    // B − A
    svg += `<mask id="${M('Bonly')}" maskUnits="userSpaceOnUse">`
         + `<rect x="0" y="0" width="${W}" height="${H}" fill="black"/>`
         + `<circle cx="${B.x}" cy="${B.y}" r="${B.r}" fill="white"/>`
         + `<circle cx="${A.x}" cy="${A.y}" r="${A.r}" fill="black"/>`
         + `</mask>`;
  }
  svg += `</defs>`;
  // regions A_only / AB / B_only / C are pairwise disjoint → uniform opacity, order-independent
  if(shadeSet.has('A_only'))
    svg += `<rect x="0" y="0" width="${W}" height="${H}" fill="${SHADE}" opacity="${SHADE_OP}" mask="url(#${M('Aonly')})"/>`;
  if(shadeSet.has('AB'))
    svg += `<path d="${lensPath}" fill="${SHADE}" opacity="${SHADE_OP}"/>`;
  if(shadeSet.has('B_only'))
    svg += `<rect x="0" y="0" width="${W}" height="${H}" fill="${SHADE}" opacity="${SHADE_OP}" mask="url(#${M('Bonly')})"/>`;
  if(shadeSet.has('C'))
    svg += `<circle cx="${C.x}" cy="${C.y}" r="${C.r}" fill="${SHADE}" opacity="${SHADE_OP}"/>`;
  // CIRCLE OUTLINES on top
  svg += `<circle cx="${A.x}" cy="${A.y}" r="${A.r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  svg += `<circle cx="${B.x}" cy="${B.y}" r="${B.r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  svg += `<circle cx="${C.x}" cy="${C.y}" r="${C.r}" fill="none" stroke="${RULE}" stroke-width="1.6"/>`;
  // LABELS (outward)
  const lab=(x,y,t)=>`<text x="${x.toFixed(1)}" y="${y.toFixed(1)}" `
       + `font-family="'Cambria Math','Times New Roman',serif" font-size="17" font-style="italic" `
       + `fill="${INK}" text-anchor="middle">${t}</text>`;
  svg += lab(A.x - A.r*0.72, A.y - A.r*0.78, labels.A);
  svg += lab(B.x + B.r*0.78, B.y - B.r*0.82, labels.B);
  svg += lab(C.x,            C.y + 5,        labels.C);
  return svg + '</svg>';
}


// ----- renderer: number-line -----
// Spec: width,height,axisY,solutionY
//   scale:'even' + criticals:[..] → จุดวิกฤตห่างเท่ากัน (sign-line convention) [additive]
//   xRange (ใช้เมื่อ scale != even)
//   ticks[] | labels[{at,text,dy}] | labels[{at,num,den,neg}] (เศษส่วนซ้อน) | labels[{at,latex,dy}] (\sqrt ฯลฯ มี vinculum ผ่าน _ucMathToSvg) [additive]
//   signs[{from,to,label,color}]  (from/to=null → ขอบ)
//   bands[{from,to,color,opacity,top,height}]
//   segments[{from,to,color,y}]; rays[{from,dir,color,y}]; points[{at,open,color,y}]  (y = px lane override) [additive]
//   annotations[{text,x,y,anchor}]
// width estimator for centering _ucMathToSvg labels (mirrors its chW advancement)
function _nlLatexW(latex,fs){
  const e=latex.replace(/^\$|\$$/g,'');
  const chW=ch=>{ if(ch===','||ch===' ')return fs*0.3; if(ch==='('||ch===')')return fs*0.4; if(ch==='\u2212'||ch==='-')return fs*0.55; if(ch==='\u221a')return fs*0.7; return fs*0.55; };
  let i=0,w=0;
  while(i<e.length){
    const m=/^\\sqrt\s*\{([^}]*)\}/.exec(e.substring(i));
    if(m){ w+=chW('\u221a'); for(const c of m[1]) w+=chW(c); i+=m[0].length; continue; }
    if(e.substr(i,2)==='\\ '){w+=fs*0.3;i+=2;continue;}
    if(e.substr(i,2)==='\\,'){w+=fs*0.2;i+=2;continue;}
    if(e[i]==='-'){w+=fs*0.55;i+=1;continue;}
    w+=chW(e[i]); i+=1;
  }
  return w;
}
function renderNumberLine(spec){
  const W=spec.width||300,H=spec.height||74;
  const pX=22, axisY=(spec.axisY!==undefined?spec.axisY:H*0.55);
  const solY=(spec.solutionY!==undefined?spec.solutionY:axisY);
  // x-mapping: even (criticals ห่างเท่ากัน) หรือ linear
  let x2;
  if(spec.scale==='even' && Array.isArray(spec.criticals) && spec.criticals.length){
    const cs=spec.criticals.slice().sort((a,b)=>a-b), n=cs.length;
    const step=(W-2*pX)/(n+1), px=cs.map((_,k)=>pX+(k+1)*step);
    x2=x=>{
      if(n===1) return px[0]+(x-cs[0])*step;
      if(x<=cs[0]) return px[0]+(x-cs[0])*(px[1]-px[0])/(cs[1]-cs[0]);
      if(x>=cs[n-1]) return px[n-1]+(x-cs[n-1])*(px[n-1]-px[n-2])/(cs[n-1]-cs[n-2]);
      for(let k=0;k<n-1;k++) if(x>=cs[k]&&x<=cs[k+1]) return px[k]+(x-cs[k])/(cs[k+1]-cs[k])*(px[k+1]-px[k]);
      return px[0];
    };
  } else {
    const xR=spec.xRange||[-5,5], xM=xR[0], xX=xR[1];
    x2=x=>pX+(W-2*pX)*(x-xM)/(xX-xM);
  }
  const edgePx=(v,left)=>(v===null||v===undefined?(left?pX:W-pX):x2(v));
  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  const _uid='nl'+Math.floor(Math.random()*1e9);          // unique per-SVG → กัน id ลูกศรชนกันหลายเส้นจำนวนในหน้าเดียว
  const _baseArr=_uid+'_a';
  const _arrId=c=>_uid+'_a_'+String(c).replace(/[^a-zA-Z0-9]/g,'');
  let _defs=`<marker id="${_baseArr}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/></marker>`;
  [...new Set((spec.rays||[]).map(r=>r.color||'#222'))].forEach(c=>{_defs+=`<marker id="${_arrId(c)}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="${c}"/></marker>`;});
  svg+=`<defs>${_defs}</defs>`;
  // background highlight bands (behind everything)
  (spec.bands||[]).forEach(b=>{
    const xa=edgePx(b.from,true), xb=edgePx(b.to,false);
    const top=(b.top!==undefined?b.top:axisY-15), h=(b.height!==undefined?b.height:30);
    svg+=`<rect x="${Math.min(xa,xb).toFixed(2)}" y="${top.toFixed(2)}" width="${Math.abs(xb-xa).toFixed(2)}" height="${h}" fill="${b.color||'#efe2a4'}" fill-opacity="${b.opacity!==undefined?b.opacity:0.55}"/>`;});
  // base number line
  svg+=`<line x1="${(pX-8).toFixed(2)}" y1="${axisY}" x2="${(W-pX+8).toFixed(2)}" y2="${axisY}" stroke="#222" stroke-width="1.1" marker-start="url(#${_baseArr})" marker-end="url(#${_baseArr})"/>`;
  // tick mark + labels (plain / dy / stacked fraction)
  const tMark=xp=>{svg+=`<line x1="${xp.toFixed(2)}" y1="${(axisY-3).toFixed(2)}" x2="${xp.toFixed(2)}" y2="${(axisY+3).toFixed(2)}" stroke="#222"/>`;};
  const tText=(xp,txt,dy)=>{svg+=`<text x="${xp.toFixed(2)}" y="${(axisY+16+(dy||0)).toFixed(2)}" text-anchor="middle" font-size="11" fill="#555">${txt}</text>`;};
  const tFrac=(xp,num,den,neg)=>{const off=neg?3:0, bx=xp+off, bh=5, by=axisY+15;
    if(neg) svg+=`<text x="${(bx-bh-4).toFixed(2)}" y="${(by+4).toFixed(2)}" text-anchor="middle" font-size="12" fill="#555">\u2212</text>`;
    svg+=`<text x="${bx.toFixed(2)}" y="${(by-3).toFixed(2)}" text-anchor="middle" font-size="11" fill="#555">${num}</text>`;
    svg+=`<line x1="${(bx-bh).toFixed(2)}" y1="${by.toFixed(2)}" x2="${(bx+bh).toFixed(2)}" y2="${by.toFixed(2)}" stroke="#555" stroke-width="1"/>`;
    svg+=`<text x="${bx.toFixed(2)}" y="${(by+11).toFixed(2)}" text-anchor="middle" font-size="11" fill="#555">${den}</text>`;};
  (spec.ticks||[]).forEach(t=>{const xp=x2(t);tMark(xp);tText(xp,t);});
  (spec.labels||[]).forEach(l=>{const xp=x2(l.at);tMark(xp);
    if(l.num!==undefined&&l.den!==undefined) tFrac(xp,l.num,l.den,l.neg);
    else if(l.latex!==undefined){const fs=11,w=_nlLatexW(l.latex,fs);svg+=_ucMathToSvg(l.latex,xp-w/2,axisY+16+(l.dy||0),fs);}
    else tText(xp,l.text,l.dy);});
  // signs (+/-) centered per region (px-based), above axis
  (spec.signs||[]).forEach(s=>{const mid=(edgePx(s.from,true)+edgePx(s.to,false))/2;
    svg+=`<text x="${mid.toFixed(2)}" y="${(axisY-9).toFixed(2)}" text-anchor="middle" font-size="13" font-weight="bold" fill="${s.color||'#c0392b'}">${s.label}</text>`;});
  // segments (per-element y lane)
  (spec.segments||[]).forEach(s=>{const yy=(s.y!==undefined?s.y:solY);
    svg+=`<line x1="${x2(s.from).toFixed(2)}" y1="${yy}" x2="${x2(s.to).toFixed(2)}" y2="${yy}" stroke="${s.color||'#222'}" stroke-width="3"/>`;});
  // rays
  (spec.rays||[]).forEach(r=>{const a=x2(r.from),edge=r.dir==='left'?(pX-8):(W-pX+8),yy=(r.y!==undefined?r.y:solY);
    svg+=`<line x1="${a.toFixed(2)}" y1="${yy}" x2="${edge.toFixed(2)}" y2="${yy}" stroke="${r.color||'#222'}" stroke-width="3" marker-end="url(#${_arrId(r.color||'#222')})"/>`;});
  // points
  (spec.points||[]).forEach(p=>{const cx=x2(p.at).toFixed(2),col=p.color||'#222',yy=(p.y!==undefined?p.y:solY);
    if(p.open) svg+=`<circle cx="${cx}" cy="${yy}" r="4" fill="#fff" stroke="${col}" stroke-width="1.6"/>`;
    else svg+=`<circle cx="${cx}" cy="${yy}" r="4" fill="${col}"/>`;});
  // annotations (px coords) — color/fontSize/weight optional (default คงเดิม)
  (spec.annotations||[]).forEach(a=>{
    const fw=a.weight?` font-weight="${a.weight}"`:'';
    svg+=`<text x="${a.x!==undefined?a.x:8}" y="${a.y!==undefined?a.y:14}" font-size="${a.fontSize||13}" fill="${a.color||'#222'}" text-anchor="${a.anchor||'start'}"${fw}>${a.text}</text>`;});
  return svg+'</svg>';
}

// ----- renderer: disk-shading -----
// แผ่นวงกลม (disk) + แรเงาบริเวณ (sector จากจุดกำเนิด / half-plane) ตัดด้วยแผ่นวงกลม
// ใช้ clipPath ชั้นเดียว (แผ่นวงกลม) ครอบ shade polygon — ไม่ nested (กัน render ว่างในบางเบราว์เซอร์)
// อัตราส่วนคงที่ (วงกลมไม่เพี้ยนเป็นวงรี): สเกล px/หน่วย = min ของสองแกน, จัดกึ่งกลางอัตโนมัติ
//
// Spec:
//   radius            - รัศมีแผ่นวงกลม (หน่วยข้อมูล) — บังคับ
//   width,height      - ขนาด canvas (default 200 x 184  ≈ W-16)
//   xRange,yRange     - ช่วงข้อมูล (default ±radius*1.3 สมมาตร)
//   diskDashed        - ขอบวงกลมเป็นเส้นประ (ถ้าไม่รวมขอบ) default false (ทึบ)
//   shade: [region]   - บริเวณแรเงา (ตัดด้วยแผ่นวงกลมทุก region):
//       {kind:'sector', angles:[deg0,deg1]}              เซกเตอร์จากจุดกำเนิด (องศาคณิต ทวนเข็ม)
//       {kind:'halfplane', line:[[x1,y1],[x2,y2]], test:[tx,ty]}  ครึ่งระนาบฝั่งที่มีจุด test
//   lines: [{from:[x,y],to:[x,y],dashed}]   เส้นอ้างอิง (เช่น y=x, y=-x) วาดทับ shade
//   axisTicks: [{at, axis:'x'|'y', latex}]  ป้ายแกน เช่น \sqrt{2} (มี vinculum ผ่าน _ucMathToSvg)
//   dots: [{x,y,open,label,labelDx,labelDy,labelAnchor}]
//   annotations: [{at:[x,y],text,anchor}]
function renderDiskShading(spec){
  const W=spec.width||200, H=spec.height||(W-16), pad=18;
  const R=spec.radius||Math.SQRT2;
  const m=R*1.3;
  const xR=spec.xRange||[-m,m], yR=spec.yRange||[-m,m];
  const xM=xR[0],xX=xR[1],yM=yR[0],yX=yR[1];
  const pW=W-2*pad, pH=H-2*pad;
  const s=Math.min(pW/(xX-xM), pH/(yX-yM));               // px ต่อหน่วย (เท่ากันทั้งสองแกน)
  const offX=pad+(pW-(xX-xM)*s)/2, offY=pad+(pH-(yX-yM)*s)/2;
  const x2=x=>offX+(x-xM)*s;
  const y2=y=>offY+(yX-y)*s;                              // flip แกน y
  const cx=x2(0), cy=y2(0), rPix=R*s;
  const BIG=(xX-xM+yX-yM)*4;                              // ขนาดใหญ่พอครอบครึ่งระนาบ
  const SHADE='#8fb3e0', SHADE_OP=0.55;

  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  const CID='diskClip_'+Math.floor(Math.random()*1e6);
  svg+=`<defs><clipPath id="${CID}"><circle cx="${cx.toFixed(2)}" cy="${cy.toFixed(2)}" r="${rPix.toFixed(2)}"/></clipPath>`;
  svg+=`<marker id="dsArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/></marker></defs>`;

  // แกน x,y (บาง อยู่หลังสุด)
  svg+=`<line x1="${(x2(xM)-2).toFixed(2)}" y1="${cy.toFixed(2)}" x2="${(x2(xX)+2).toFixed(2)}" y2="${cy.toFixed(2)}" stroke="#bbb" stroke-width="1" marker-end="url(#dsArr)"/>`;
  svg+=`<line x1="${cx.toFixed(2)}" y1="${(y2(yM)+2).toFixed(2)}" x2="${cx.toFixed(2)}" y2="${(y2(yX)-2).toFixed(2)}" stroke="#bbb" stroke-width="1" marker-end="url(#dsArr)"/>`;

  // ----- shade regions (ตัดด้วยแผ่นวงกลม clipPath ชั้นเดียว) -----
  const polys=[];
  (spec.shade||[]).forEach(rg=>{
    if(rg.kind==='sector'){
      const[a0,a1]=rg.angles, p0=[Math.cos(a0*Math.PI/180)*BIG, Math.sin(a0*Math.PI/180)*BIG],
            p1=[Math.cos(a1*Math.PI/180)*BIG, Math.sin(a1*Math.PI/180)*BIG];
      // จุดกลางส่วนโค้งกันกรณีมุมกาง ~180 (ให้สามเหลี่ยมครอบเซกเตอร์เสมอ)
      const am=(a0+a1)/2, pm=[Math.cos(am*Math.PI/180)*BIG, Math.sin(am*Math.PI/180)*BIG];
      polys.push([[0,0],p0,pm,p1]);
    }else if(rg.kind==='halfplane'){
      const[[x1,y1],[x2d,y2d]]=rg.line, dx=x2d-x1, dy=y2d-y1, L=Math.hypot(dx,dy)||1;
      const ux=dx/L, uy=dy/L;                              // ทิศตามเส้น
      let nx=-uy, ny=ux;                                   // ตั้งฉาก
      const mx=(x1+x2d)/2, my=(y1+y2d)/2;
      const[tx,ty]=rg.test;
      if((tx-mx)*nx+(ty-my)*ny < 0){ nx=-nx; ny=-ny; }     // ให้ normal ชี้ไปฝั่ง test
      const A=[x1-ux*BIG, y1-uy*BIG], B=[x2d+ux*BIG, y2d+uy*BIG];
      const C=[B[0]+nx*BIG, B[1]+ny*BIG], D=[A[0]+nx*BIG, A[1]+ny*BIG];
      polys.push([A,B,C,D]);
    }
  });
  if(polys.length){
    svg+=`<g clip-path="url(#${CID})" fill="${SHADE}" fill-opacity="${SHADE_OP}">`;
    polys.forEach(p=>{ svg+=`<polygon points="${p.map(([px,py])=>`${x2(px).toFixed(2)},${y2(py).toFixed(2)}`).join(' ')}"/>`; });
    svg+=`</g>`;
  }

  // ขอบแผ่นวงกลม
  const dash=spec.diskDashed?' stroke-dasharray="4 3"':'';
  svg+=`<circle cx="${cx.toFixed(2)}" cy="${cy.toFixed(2)}" r="${rPix.toFixed(2)}" fill="none" stroke="#222" stroke-width="1.5"${dash}/>`;

  // เส้นอ้างอิง (y=x ฯลฯ) — ตัดให้พอดีในกรอบ
  (spec.lines||[]).forEach(ln=>{
    const d=ln.dashed?' stroke-dasharray="5 4"':'';
    svg+=`<line x1="${x2(ln.from[0]).toFixed(2)}" y1="${y2(ln.from[1]).toFixed(2)}" x2="${x2(ln.to[0]).toFixed(2)}" y2="${y2(ln.to[1]).toFixed(2)}" stroke="#555" stroke-width="1.2"${d}/>`;
  });

  // ป้ายแกน (√2 ฯลฯ) — _ucMathToSvg ให้ vinculum
  (spec.axisTicks||[]).forEach(t=>{
    const isX=t.axis!=='y';
    const px=isX?x2(t.at):cx, py=isX?cy:y2(t.at);
    svg+=`<line x1="${(px-(isX?0:3)).toFixed(2)}" y1="${(py-(isX?3:0)).toFixed(2)}" x2="${(px+(isX?0:3)).toFixed(2)}" y2="${(py+(isX?3:0)).toFixed(2)}" stroke="#222"/>`;
    const lx=isX?px:(px-20), ly=isX?(py+14):(py+4);
    svg+=_ucMathToSvg(t.latex, lx, ly, 11);
  });

  // dots
  (spec.dots||[]).forEach(d=>{const dx=x2(d.x).toFixed(2),dy=y2(d.y).toFixed(2);
    if(d.open) svg+=`<circle cx="${dx}" cy="${dy}" r="3" fill="#fff" stroke="#222" stroke-width="1.4"/>`;
    else svg+=`<circle cx="${dx}" cy="${dy}" r="3" fill="#222"/>`;
    if(d.label){const anc=d.labelAnchor||'start',ddx=(d.labelDx!==undefined?d.labelDx:5),ddy=(d.labelDy!==undefined?d.labelDy:-5);
      svg+=`<text x="${(x2(d.x)+ddx).toFixed(2)}" y="${(y2(d.y)+ddy).toFixed(2)}" font-size="11" fill="#222" text-anchor="${anc}">${d.label}</text>`;}});

  // math labels (พิกัด เช่น (\sqrt{2},0)) — _polyMathToSvg ให้ √ vinculum + รองรับ anchor
  (spec.labels||[]).forEach(l=>{const anc=l.anchor||'start',ddx=(l.dx!==undefined?l.dx:0),ddy=(l.dy!==undefined?l.dy:0);
    svg+=_polyMathToSvg(l.latex, x2(l.at[0])+ddx, y2(l.at[1])+ddy, l.fontSize||10, anc);});

  // annotations (plain text)
  (spec.annotations||[]).forEach(a=>{const anc=a.anchor||'start';
    svg+=`<text x="${x2(a.at[0]).toFixed(2)}" y="${y2(a.at[1]).toFixed(2)}" font-size="12" fill="#222" text-anchor="${anc}">${a.text}</text>`;});

  return svg+'</svg>';
}

// ----- renderer: intersecting-circles (two equal circles + lens shading) -----
// schema:
// { type:"intersecting-circles", width,height, cx,cy, r, d, angle(deg,default0),
//   shadeLens:bool, lensStyle:"solid"|"dots"(default solid),
//   perpRadii:{at:"top"|"bottom", rightAngle:bool, dashed:bool},
//   radiusArrows:[{side:"start"|"end", label}],
//   labels:[{x,y,text,fontSize,anchor}] }
function renderIntersectingCircles(spec){
  const W=spec.width||300, H=spec.height||210;
  const r=spec.r||85, d=spec.d||r, ang=(spec.angle||0)*Math.PI/180;
  const cx=(spec.cx!=null)?spec.cx:W/2, cy=(spec.cy!=null)?spec.cy:H/2;
  const ux=Math.cos(ang), uy=Math.sin(ang);          // axis O1->O2 (screen coords, y down)
  const nx=-uy, ny=ux;                                // perpendicular (one side)
  const O1=[cx-(d/2)*ux, cy-(d/2)*uy];
  const O2=[cx+(d/2)*ux, cy+(d/2)*uy];
  // intersection points: midpoint ± h along perpendicular
  const h=Math.sqrt(Math.max(0, r*r-(d/2)*(d/2)));
  const Ptop=[cx+nx*h, cy+ny*h];                      // "+n" side
  const Pbot=[cx-nx*h, cy-ny*h];
  const SHADE='#8fb3e0', SHADE_OP=0.55;
  const uid=Math.floor(Math.random()*1e6);

  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  svg+=`<defs>`
     + `<clipPath id="c1_${uid}"><circle cx="${O1[0].toFixed(2)}" cy="${O1[1].toFixed(2)}" r="${r.toFixed(2)}"/></clipPath>`
     + `<marker id="icArr_${uid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#222"/></marker>`
     + `</defs>`;

  // --- lens shade (circle2 clipped by circle1) ---
  if(spec.shadeLens){
    svg+=`<g clip-path="url(#c1_${uid})"><circle cx="${O2[0].toFixed(2)}" cy="${O2[1].toFixed(2)}" r="${r.toFixed(2)}" fill="${SHADE}" fill-opacity="${SHADE_OP}"/></g>`;
  }
  // --- circle outlines ---
  [O1,O2].forEach(O=>{
    svg+=`<circle cx="${O[0].toFixed(2)}" cy="${O[1].toFixed(2)}" r="${r.toFixed(2)}" fill="none" stroke="#222" stroke-width="1.5"/>`;
  });

  // --- center crosses (dashed H+V diameters per circle, extended) ---
  if(spec.centerCross){
    const ext=(spec.centerCross.extend!=null)?spec.centerCross.extend:20;
    const dash=(spec.centerCross.dashed!==false)?' stroke-dasharray="5 4"':'';
    [O1,O2].forEach(O=>{
      // horizontal diameter
      svg+=`<line x1="${(O[0]-r-ext).toFixed(2)}" y1="${O[1].toFixed(2)}" x2="${(O[0]+r+ext).toFixed(2)}" y2="${O[1].toFixed(2)}" stroke="#222" stroke-width="1"${dash}/>`;
      // vertical diameter
      svg+=`<line x1="${O[0].toFixed(2)}" y1="${(O[1]-r-ext).toFixed(2)}" x2="${O[0].toFixed(2)}" y2="${(O[1]+r+ext).toFixed(2)}" stroke="#222" stroke-width="1"${dash}/>`;
    });
  }

  // --- crosshairs: H+V dashed diameter through each center (extended by ext) ---
  if(spec.crosshairs){
    const ext=(spec.crosshairExt!=null)?spec.crosshairExt:12;
    [O1,O2].forEach(O=>{
      svg+=`<line x1="${(O[0]-r-ext).toFixed(2)}" y1="${O[1].toFixed(2)}" x2="${(O[0]+r+ext).toFixed(2)}" y2="${O[1].toFixed(2)}" stroke="#222" stroke-width="1.1" stroke-dasharray="5 4"/>`;
      svg+=`<line x1="${O[0].toFixed(2)}" y1="${(O[1]-r-ext).toFixed(2)}" x2="${O[0].toFixed(2)}" y2="${(O[1]+r+ext).toFixed(2)}" stroke="#222" stroke-width="1.1" stroke-dasharray="5 4"/>`;
    });
  }

  // --- perpendicular radii to an intersection point ---
  if(spec.perpRadii){
    const P=(spec.perpRadii.at==='bottom')?Pbot:Ptop;
    const dash=(spec.perpRadii.dashed!==false)?' stroke-dasharray="5 4"':'';
    svg+=`<line x1="${O1[0].toFixed(2)}" y1="${O1[1].toFixed(2)}" x2="${P[0].toFixed(2)}" y2="${P[1].toFixed(2)}" stroke="#222" stroke-width="1.2"${dash}/>`;
    svg+=`<line x1="${O2[0].toFixed(2)}" y1="${O2[1].toFixed(2)}" x2="${P[0].toFixed(2)}" y2="${P[1].toFixed(2)}" stroke="#222" stroke-width="1.2"${dash}/>`;
    if(spec.perpRadii.rightAngle){
      const a=[(O1[0]-P[0]),(O1[1]-P[1])], b=[(O2[0]-P[0]),(O2[1]-P[1])];
      const la=Math.hypot(a[0],a[1])||1, lb=Math.hypot(b[0],b[1])||1;
      const ax=a[0]/la, ay=a[1]/la, bx=b[0]/lb, by=b[1]/lb, s=12;
      const c1=[P[0]+s*ax,P[1]+s*ay], cr=[P[0]+s*(ax+bx),P[1]+s*(ay+by)], c2=[P[0]+s*bx,P[1]+s*by];
      svg+=`<path d="M ${c1[0].toFixed(2)} ${c1[1].toFixed(2)} L ${cr[0].toFixed(2)} ${cr[1].toFixed(2)} L ${c2[0].toFixed(2)} ${c2[1].toFixed(2)}" fill="none" stroke="#222" stroke-width="1"/>`;
    }
  }

  // --- radius double-arrows (along axis, outward from each center) ---
  (spec.radiusArrows||[]).forEach(ra=>{
    let A,B,O;
    if(ra.side==='end'){ O=O2; A=[O2[0],O2[1]]; B=[O2[0]+r*ux, O2[1]+r*uy]; }
    else { O=O1; A=[O1[0]-r*ux, O1[1]-r*uy]; B=[O1[0],O1[1]]; }
    svg+=`<line x1="${A[0].toFixed(2)}" y1="${A[1].toFixed(2)}" x2="${B[0].toFixed(2)}" y2="${B[1].toFixed(2)}" stroke="#222" stroke-width="1.2" marker-start="url(#icArr_${uid})" marker-end="url(#icArr_${uid})"/>`;
    if(ra.label){
      const mx=(A[0]+B[0])/2, my=(A[1]+B[1])/2;
      const lx=mx-nx*14, ly=my-ny*14;   // offset to -n side (above for horizontal)
      svg+=`<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-size="15" fill="#222" text-anchor="middle" dominant-baseline="central">${ra.label}</text>`;
    }
  });

  // --- free labels ---
  (spec.labels||[]).forEach(l=>{
    svg+=`<text x="${l.x}" y="${l.y}" font-family="'Cambria Math','Times New Roman',serif" font-size="${l.fontSize||14}" fill="#222" text-anchor="${l.anchor||'start'}">${l.text||''}</text>`;
  });

  return svg+'</svg>';
}

// ----- renderer: circle-segment (single circle + radii + chord + segment shade + reflex angle mark) -----
// schema:
// { type:"circle-segment", width,height, r(px),
//   radii:[{deg, label, labelDist(0..1, default .6)}, ...],   // each radius center->edge; tips of first two define chord
//   chord:bool,                                               // draw chord between first two radius tips
//   shade:"minor"|"major",        shadeStyle:"dots"|"solid",  // shade the segment on minor(short)/major(long) arc side
//   angleMark:{side:"minor"|"major", label, rArc(px,default 30)} }  // arc on chosen side + label at its mid-angle
function renderCircleSegment(spec){
  const W=spec.width||210, H=spec.height||210, r=spec.r||80;
  const cx=(spec.cx!=null)?spec.cx:W/2, cy=(spec.cy!=null)?spec.cy:H/2;
  const D2R=Math.PI/180;
  const ptAt=(deg,rad)=>[cx+rad*Math.cos(deg*D2R), cy-rad*Math.sin(deg*D2R)]; // screen coords (y down)
  const SHADE='#8fb3e0', SHADE_OP=0.55;
  const uid=Math.floor(Math.random()*1e6);
  const radii=spec.radii||[];
  const a0=(radii[0]?radii[0].deg:60), a1=(radii[1]?radii[1].deg:-60);
  const spanCCW=((a1-a0)%360+360)%360;          // CCW sweep a0 -> a1, 0..360
  const minorCCW=spanCCW<=180;                  // minor (<=180) side reached from a0 going CCW?
  const minorSpan=minorCCW?spanCCW:360-spanCCW;
  // sampler: from `fromDeg`, direction ccw, total `span` degrees, radius `rad`
  const samplePts=(fromDeg,ccw,span,rad)=>{
    const N=Math.max(10,Math.round(span/4)), out=[];
    for(let i=0;i<=N;i++){ const t=ccw?(fromDeg+span*i/N):(fromDeg-span*i/N); out.push(ptAt(t,rad)); }
    return out;
  };

  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  svg+=`<defs>`;
  if((spec.shadeStyle||'dots')==='dots'){
    svg+=`<pattern id="csDots_${uid}" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#fff"/><circle cx="3" cy="3" r="1.15" fill="#4d75a8"/></pattern>`;
  }
  svg+=`<marker id="csArr_${uid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#222"/></marker>`;
  svg+=`</defs>`;

  // --- segment shade (arc on chosen side + chord) ---
  if(spec.shade){
    const wantMinor=(spec.shade!=='major');
    const ccw = wantMinor ? minorCCW : !minorCCW;
    const span = wantMinor ? minorSpan : 360-minorSpan;
    const pts=samplePts(a0,ccw,span,r);
    const d='M '+pts.map(p=>p[0].toFixed(2)+' '+p[1].toFixed(2)).join(' L ')+' Z';
    const fill=((spec.shadeStyle||'dots')==='dots')?`url(#csDots_${uid})`:SHADE;
    const op=((spec.shadeStyle||'dots')==='dots')?1:SHADE_OP;
    svg+=`<path d="${d}" fill="${fill}" fill-opacity="${op}" stroke="none"/>`;
  }

  // --- circle outline ---
  svg+=`<circle cx="${cx.toFixed(2)}" cy="${cy.toFixed(2)}" r="${r.toFixed(2)}" fill="none" stroke="#222" stroke-width="1.5"/>`;

  // --- radii (center -> edge) + labels ---
  radii.forEach(rd=>{
    const tip=ptAt(rd.deg,r);
    svg+=`<line x1="${cx.toFixed(2)}" y1="${cy.toFixed(2)}" x2="${tip[0].toFixed(2)}" y2="${tip[1].toFixed(2)}" stroke="#222" stroke-width="1.5"/>`;
    if(rd.label!=null){
      const ld=(rd.labelDist!=null?rd.labelDist:0.6);
      const lp=ptAt(rd.deg, r*ld);
      // offset perpendicular (outward from sector centre) a touch
      const off=11, perp=rd.deg+ (minorCCW?90:-90);
      const lx=lp[0]+off*Math.cos(perp*D2R), ly=lp[1]-off*Math.sin(perp*D2R);
      svg+=`<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-size="15" fill="#222" text-anchor="middle" dominant-baseline="central">${rd.label}</text>`;
    }
  });

  // --- chord between first two radius tips ---
  if(spec.chord && radii.length>=2){
    const t0=ptAt(a0,r), t1=ptAt(a1,r);
    svg+=`<line x1="${t0[0].toFixed(2)}" y1="${t0[1].toFixed(2)}" x2="${t1[0].toFixed(2)}" y2="${t1[1].toFixed(2)}" stroke="#222" stroke-width="1.5"/>`;
  }

  // --- angle mark arc + label (on chosen side) ---
  if(spec.angleMark){
    const am=spec.angleMark, rArc=(am.rArc!=null?am.rArc:30);
    const wantMinor=(am.side==='minor');
    const ccw = wantMinor ? minorCCW : !minorCCW;
    const span = wantMinor ? minorSpan : 360-minorSpan;
    const pts=samplePts(a0,ccw,span,rArc);
    const d='M '+pts.map(p=>p[0].toFixed(2)+' '+p[1].toFixed(2)).join(' L ');
    svg+=`<path d="${d}" fill="none" stroke="#222" stroke-width="1.1"/>`;
    if(am.label!=null){
      const midDeg = a0 + (ccw?1:-1)*span/2;
      const lp=ptAt(midDeg, rArc+13);
      svg+=`<text x="${lp[0].toFixed(2)}" y="${lp[1].toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-size="13" fill="#222" text-anchor="middle" dominant-baseline="central">${am.label}</text>`;
    }
  }

  // --- center dot ---
  svg+=`<circle cx="${cx.toFixed(2)}" cy="${cy.toFixed(2)}" r="1.6" fill="#222"/>`;

  // --- free labels ---
  (spec.labels||[]).forEach(l=>{
    svg+=`<text x="${l.x}" y="${l.y}" font-family="'Cambria Math','Times New Roman',serif" font-size="${l.fontSize||14}" fill="#222" text-anchor="${l.anchor||'start'}">${l.text||''}</text>`;
  });

  return svg+'</svg>';
}

// ----- renderer: triangle-sector-cut (right triangle with a circular sector removed at its apex) -----
// schema:
// { type:"triangle-sector-cut", width,height, unit(px/unit,default 55),
//   circle:{r}, axes:bool,                         // full circle at apex (origin) + crosshair axes
//   triangle:{legX, legY},                         // apex 45deg at origin; bottom leg +x len legX, right leg +y len legY; right angle at (legX,0)
//   sectorCutDeg(default 45),  shadeStyle:"dots"|"solid",
//   radiusLabel:{deg, text},                       // label along a radius direction
//   edgeLabels:[{side:"bottom"|"right", text}],
//   rightAngle:bool }                              // right-angle square at (legX,0)
function renderTriangleSectorCut(spec){
  const unit=spec.unit||55, pad=24, lpad=16;
  const r=(spec.circle&&spec.circle.r!=null)?spec.circle.r:1;
  const legX=(spec.triangle&&spec.triangle.legX!=null)?spec.triangle.legX:2;
  const legY=(spec.triangle&&spec.triangle.legY!=null)?spec.triangle.legY:2;
  const secDeg=(spec.sectorCutDeg!=null)?spec.sectorCutDeg:45;
  const Ox=pad+r*unit, Oy=pad+legY*unit;
  const W=spec.width||Math.ceil(Ox+legX*unit+pad+lpad);
  const H=spec.height||Math.ceil(Oy+r*unit+pad+lpad);
  const D2R=Math.PI/180;
  const X=x=>Ox+x*unit, Y=y=>Oy-y*unit;
  const polar=(deg,rad)=>[Ox+rad*unit*Math.cos(deg*D2R), Oy-rad*unit*Math.sin(deg*D2R)];
  const SHADE='#8fb3e0', SHADE_OP=0.55;
  const uid=Math.floor(Math.random()*1e6);
  const dots=((spec.shadeStyle||'dots')==='dots');

  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  svg+=`<defs>`;
  if(dots) svg+=`<pattern id="tscDots_${uid}" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#fff"/><circle cx="3" cy="3" r="1.15" fill="#4d75a8"/></pattern>`;
  svg+=`</defs>`;

  // --- shaded region: triangle minus sector (B -> P1 -> arc(0..secDeg) -> C -> Z) ---
  const B=[X(legX),Y(0)], C=[X(legX),Y(legY)], P1=polar(0,r);
  const N=Math.max(10,Math.round(secDeg/3)); const arc=[];
  for(let i=0;i<=N;i++){ arc.push(polar(secDeg*i/N, r)); }
  let d='M '+B[0].toFixed(2)+' '+B[1].toFixed(2)+' L '+P1[0].toFixed(2)+' '+P1[1].toFixed(2);
  arc.forEach(p=>{ d+=' L '+p[0].toFixed(2)+' '+p[1].toFixed(2); });
  d+=' L '+C[0].toFixed(2)+' '+C[1].toFixed(2)+' Z';
  const fill=dots?`url(#tscDots_${uid})`:SHADE, op=dots?1:SHADE_OP;
  svg+=`<path d="${d}" fill="${fill}" fill-opacity="${op}" stroke="none"/>`;

  // --- crosshair axes through origin (behind circle/triangle) ---
  if(spec.axes!==false){
    const ext=14;
    svg+=`<line x1="${(Ox-r*unit-ext).toFixed(2)}" y1="${Oy.toFixed(2)}" x2="${(Ox+r*unit+ext).toFixed(2)}" y2="${Oy.toFixed(2)}" stroke="#222" stroke-width="1"/>`;
    svg+=`<line x1="${Ox.toFixed(2)}" y1="${(Oy-r*unit-ext).toFixed(2)}" x2="${Ox.toFixed(2)}" y2="${(Oy+r*unit+ext).toFixed(2)}" stroke="#222" stroke-width="1"/>`;
  }

  // --- full circle ---
  svg+=`<circle cx="${Ox.toFixed(2)}" cy="${Oy.toFixed(2)}" r="${(r*unit).toFixed(2)}" fill="none" stroke="#222" stroke-width="1.5"/>`;

  // --- triangle sides (solid): bottom O->B, right B->C, hypotenuse O->C ---
  svg+=`<line x1="${Ox.toFixed(2)}" y1="${Oy.toFixed(2)}" x2="${B[0].toFixed(2)}" y2="${B[1].toFixed(2)}" stroke="#222" stroke-width="1.5"/>`;
  svg+=`<line x1="${B[0].toFixed(2)}" y1="${B[1].toFixed(2)}" x2="${C[0].toFixed(2)}" y2="${C[1].toFixed(2)}" stroke="#222" stroke-width="1.5"/>`;
  svg+=`<line x1="${Ox.toFixed(2)}" y1="${Oy.toFixed(2)}" x2="${C[0].toFixed(2)}" y2="${C[1].toFixed(2)}" stroke="#222" stroke-width="1.5"/>`;

  // --- right-angle mark at B=(legX,0) ---
  if(spec.rightAngle!==false){
    const s=10; // legs from B: toward O (-x) and toward C (+y up => screen -y)
    const a=[B[0]-s,B[1]], c=[B[0]-s,B[1]-s], b=[B[0],B[1]-s];
    svg+=`<path d="M ${a[0].toFixed(2)} ${a[1].toFixed(2)} L ${c[0].toFixed(2)} ${c[1].toFixed(2)} L ${b[0].toFixed(2)} ${b[1].toFixed(2)}" fill="none" stroke="#222" stroke-width="1"/>`;
  }

  // --- radius label (along a direction) ---
  if(spec.radiusLabel){
    const rl=spec.radiusLabel, lp=polar((rl.deg!=null?rl.deg:45), r*0.5);
    // nudge up-left off the line
    svg+=`<text x="${(lp[0]-9).toFixed(2)}" y="${(lp[1]-2).toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-size="14" fill="#222" text-anchor="middle" dominant-baseline="central">${rl.text}</text>`;
  }

  // --- edge labels ---
  (spec.edgeLabels||[]).forEach(e=>{
    let lx,ly;
    if(e.side==='right'){ lx=X(legX)+12; ly=Y(legY/2); }
    else { lx=X((r+legX)/2); ly=Y(0)+16; }  // bottom: midpoint of segment outside circle
    svg+=`<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-size="15" fill="#222" text-anchor="middle" dominant-baseline="central">${e.text}</text>`;
  });

  // --- free labels ---
  (spec.labels||[]).forEach(l=>{
    svg+=`<text x="${l.x}" y="${l.y}" font-family="'Cambria Math','Times New Roman',serif" font-size="${l.fontSize||14}" fill="#222" text-anchor="${l.anchor||'start'}">${l.text||''}</text>`;
  });

  return svg+'</svg>';
}

// === pyramid-square: square-base pyramid (oblique projection) =================
// { type:"pyramid-square", width,height,
//   baseW(px,default 150), depth(px,default 58), skew(px,default depth*0.5),
//   apexH(px,default 120),
//   labels:{apex,frontLeft,frontRight,frontMid,center},  // default A,B,C,D,O
//   angle:{text:"75°"},          // angle mark at front-left B, between BC and BA
//   baseLabel, bdLabel, odLabel, // text labels on BC / BD / OD (optional)
//   showHeight(default true: dashed A-O + right-angle at O),
//   showApothem(default true: solid O-D), showSlant(default true: solid A-D) }
// labels are plain text (no √/Thai inside figure) → cairosvg-safe
function renderPyramidSquare(spec){
  const pad=24;
  const baseW=spec.baseW||150, depth=spec.depth||58;
  const skew=(spec.skew!=null)?spec.skew:depth*0.5;
  const apexH=spec.apexH||120;
  const lab=Object.assign({apex:'A',frontLeft:'B',frontRight:'C',frontMid:'D',center:'O'},spec.labels||{});

  const bx=pad+18, by=pad+apexH+depth+16;
  const B=[bx,by], C=[bx+baseW,by];
  const BL=[bx+skew,by-depth], BR=[bx+baseW+skew,by-depth];
  const D=[(B[0]+C[0])/2,(B[1]+C[1])/2];
  const O=[(B[0]+C[0]+BL[0]+BR[0])/4,(B[1]+C[1]+BL[1]+BR[1])/4];
  const A=[O[0],O[1]-apexH];
  const W=spec.width||Math.ceil(BR[0]+pad+20);
  const H=spec.height||Math.ceil(by+pad);

  const L=(p,q,st)=>`<line x1="${p[0].toFixed(2)}" y1="${p[1].toFixed(2)}" x2="${q[0].toFixed(2)}" y2="${q[1].toFixed(2)}" stroke="#222" stroke-width="${st==='thin'?1:1.5}"${st==='dash'?' stroke-dasharray="5 4"':''}/>`;
  const T=(x,y,t,fs,anch)=>`<text x="${x.toFixed(2)}" y="${y.toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-size="${fs||15}" fill="#222" text-anchor="${anch||'middle'}" dominant-baseline="central">${t}</text>`;

  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;

  // hidden (back) edges + height dashed
  svg+=L(BL,BR,'dash');
  svg+=L(A,BL,'dash');
  svg+=L(A,BR,'dash');
  if(spec.showHeight!==false) svg+=L(A,O,'dash');

  // visible solid edges
  svg+=L(B,C); svg+=L(B,BL); svg+=L(C,BR); svg+=L(A,B); svg+=L(A,C);

  // apothem O-D + slant A-D solid
  if(spec.showApothem!==false) svg+=L(O,D);
  if(spec.showSlant!==false) svg+=L(A,D);

  // right-angle mark at O between O->A and O->D
  if(spec.showHeight!==false){
    const u=(p,q)=>{const dx=q[0]-p[0],dy=q[1]-p[1],m=Math.hypot(dx,dy)||1;return [dx/m,dy/m];};
    const s=11, ua=u(O,A), ud=u(O,D);
    const p1=[O[0]+ua[0]*s,O[1]+ua[1]*s], p3=[O[0]+ud[0]*s,O[1]+ud[1]*s];
    const p2=[O[0]+(ua[0]+ud[0])*s,O[1]+(ua[1]+ud[1])*s];
    svg+=`<path d="M ${p1[0].toFixed(2)} ${p1[1].toFixed(2)} L ${p2[0].toFixed(2)} ${p2[1].toFixed(2)} L ${p3[0].toFixed(2)} ${p3[1].toFixed(2)}" fill="none" stroke="#222" stroke-width="1"/>`;
  }

  // angle mark at B between B->C and B->A (sampled arc, cairosvg-safe)
  if(spec.angle){
    const ang=p=>Math.atan2(p[1]-B[1],p[0]-B[0]);
    const a1=ang(C); let d=ang(A)-a1; while(d>Math.PI)d-=2*Math.PI; while(d<-Math.PI)d+=2*Math.PI;
    const rad=26, N=Math.max(8,Math.round(Math.abs(d)/0.12));
    let dd='';
    for(let i=0;i<=N;i++){const a=a1+d*i/N;dd+=(i?' L ':'M ')+(B[0]+rad*Math.cos(a)).toFixed(2)+' '+(B[1]+rad*Math.sin(a)).toFixed(2);}
    svg+=`<path d="${dd}" fill="none" stroke="#222" stroke-width="1"/>`;
    const am=a1+d/2, lr=rad+14;
    svg+=T(B[0]+lr*Math.cos(am),B[1]+lr*Math.sin(am),spec.angle.text||'',14);
  }

  // length labels
  if(spec.baseLabel) svg+=T((B[0]+C[0])/2,by+30,spec.baseLabel,14);
  if(spec.bdLabel)   svg+=T((B[0]+D[0])/2,by+15,spec.bdLabel,13);
  if(spec.odLabel)   svg+=T((O[0]+D[0])/2+11,(O[1]+D[1])/2,spec.odLabel,13);

  // point labels
  svg+=T(A[0],A[1]-11,lab.apex,15);
  svg+=T(B[0]-11,B[1]+6,lab.frontLeft,15,'end');
  svg+=T(C[0]+11,C[1]+6,lab.frontRight,15,'start');
  svg+=T(D[0],D[1]+15,lab.frontMid,15);
  svg+=T(O[0]+10,O[1]-5,lab.center,15,'start');

  return svg+'</svg>';
}

// === tower-two-observers: vertical pole + 2 ground observers w/ elevation angles =
// pseudo-3D. ground right-triangle ABC (right angle at A): AB horizontal, AC down,
// CB hypotenuse. pole BT vertical at B (top T). sight lines A->T, C->T with
// elevation angle marks. flag on top. N arrow.
// { type:"tower-two-observers", width,height,
//   legAB(px,default 150), legAC(px,default 88), acSkew(px,default 0),
//   towerH(px,default 95), flag(default true), hLabel(default "h"),
//   acLabel(default "10"),
//   angles:[{at:"A",text:"60°"},{at:"C",text:"45°"}],
//   labels:{A,B,C}, north(default "right"),
//   rightAngleA(default true), rightAngleB(default true) }
// labels plain ascii (A/B/C/h/10/60°/45°/N) → cairosvg-safe
function renderTowerTwoObservers(spec){
  const pad=24;
  const legAB=spec.legAB||150, legAC=spec.legAC||88, acSkew=(spec.acSkew!=null)?spec.acSkew:0;
  const towerH=spec.towerH||95;
  const lab=Object.assign({A:'A',B:'B',C:'C'},spec.labels||{});
  const hLabel=(spec.hLabel!=null)?spec.hLabel:'h';
  const acLabel=(spec.acLabel!=null)?spec.acLabel:'10';

  const ay=pad+towerH+22;
  const A=[pad+24,ay], B=[pad+24+legAB,ay];
  const C=[A[0]+acSkew,ay+legAC];
  const T=[B[0],B[1]-towerH];
  const W=spec.width||Math.ceil(B[0]+pad+26);
  const H=spec.height||Math.ceil(C[1]+pad+18);

  const L=(p,q,st)=>`<line x1="${p[0].toFixed(2)}" y1="${p[1].toFixed(2)}" x2="${q[0].toFixed(2)}" y2="${q[1].toFixed(2)}" stroke="#222" stroke-width="${st==='thin'?1:1.5}"${st==='dash'?' stroke-dasharray="5 4"':''}/>`;
  const T_=(x,y,t,fs,anch)=>`<text x="${x.toFixed(2)}" y="${y.toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-size="${fs||15}" fill="#222" text-anchor="${anch||'middle'}" dominant-baseline="central">${t}</text>`;
  const u=(p,q)=>{const dx=q[0]-p[0],dy=q[1]-p[1],m=Math.hypot(dx,dy)||1;return [dx/m,dy/m];};
  const angArc=(V,P,Q,rad,txt)=>{ // arc at V from V->P to V->Q (shorter dir) + label
    const a1=Math.atan2(P[1]-V[1],P[0]-V[0]); let d=Math.atan2(Q[1]-V[1],Q[0]-V[0])-a1;
    while(d>Math.PI)d-=2*Math.PI; while(d<-Math.PI)d+=2*Math.PI;
    const N=Math.max(8,Math.round(Math.abs(d)/0.12)); let dd='';
    for(let i=0;i<=N;i++){const a=a1+d*i/N;dd+=(i?' L ':'M ')+(V[0]+rad*Math.cos(a)).toFixed(2)+' '+(V[1]+rad*Math.sin(a)).toFixed(2);}
    let s=`<path d="${dd}" fill="none" stroke="#222" stroke-width="1"/>`;
    const am=a1+d/2, lr=rad+13;
    s+=T_(V[0]+lr*Math.cos(am),V[1]+lr*Math.sin(am),txt,13);
    return s;
  };
  const rAngle=(V,d1,d2,s)=>{ // right-angle square at V along unit dirs d1,d2
    const p1=[V[0]+d1[0]*s,V[1]+d1[1]*s], p3=[V[0]+d2[0]*s,V[1]+d2[1]*s];
    const p2=[V[0]+(d1[0]+d2[0])*s,V[1]+(d1[1]+d2[1])*s];
    return `<path d="M ${p1[0].toFixed(2)} ${p1[1].toFixed(2)} L ${p2[0].toFixed(2)} ${p2[1].toFixed(2)} L ${p3[0].toFixed(2)} ${p3[1].toFixed(2)}" fill="none" stroke="#222" stroke-width="1"/>`;
  };

  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;

  // sight lines (thin) A->T, C->T
  svg+=L(A,T,'thin'); svg+=L(C,T,'thin');
  // ground triangle ABC solid
  svg+=L(A,B); svg+=L(A,C); svg+=L(C,B);
  // pole B->T solid
  svg+=L(B,T);

  // flag at top T (small right-pointing triangle)
  if(spec.flag!==false){
    svg+=`<path d="M ${T[0].toFixed(2)} ${T[1].toFixed(2)} L ${(T[0]+16).toFixed(2)} ${(T[1]+5).toFixed(2)} L ${T[0].toFixed(2)} ${(T[1]+10).toFixed(2)} Z" fill="#222"/>`;
  }

  // right-angle marks
  if(spec.rightAngleA!==false) svg+=rAngle(A,u(A,B),u(A,C),11);
  if(spec.rightAngleB!==false) svg+=rAngle(B,u(B,A),u(B,T),11);

  // elevation angle arcs
  (spec.angles||[{at:'A',text:'60°'},{at:'C',text:'45°'}]).forEach(an=>{
    if(an.at==='A') svg+=angArc(A,B,T,30,an.text||'');
    else if(an.at==='C') svg+=angArc(C,B,T,30,an.text||'');
  });

  // pole height label "h" (right of pole midpoint)
  if(hLabel) svg+=T_(B[0]+12,(B[1]+T[1])/2,hLabel,14,'start');
  // AC label "10" (left of AC midpoint)
  if(acLabel) svg+=T_((A[0]+C[0])/2-12,(A[1]+C[1])/2,acLabel,13,'end');

  // point labels
  svg+=T_(A[0]-11,A[1]-2,lab.A,15,'end');
  svg+=T_(B[0]+11,B[1]-3,lab.B,15,'start');
  svg+=T_(C[0]-4,C[1]+13,lab.C,15,'end');

  // N arrow (bottom-right by default, pointing right)
  const nd=spec.north||'right';
  if(nd){
    const nx=W-pad-10, ny=H-pad+2;
    if(nd==='right'){
      svg+=`<line x1="${(nx-30).toFixed(2)}" y1="${ny.toFixed(2)}" x2="${nx.toFixed(2)}" y2="${ny.toFixed(2)}" stroke="#222" stroke-width="1.2"/>`;
      svg+=`<path d="M ${nx.toFixed(2)} ${ny.toFixed(2)} L ${(nx-6).toFixed(2)} ${(ny-3.5).toFixed(2)} L ${(nx-6).toFixed(2)} ${(ny+3.5).toFixed(2)} Z" fill="#222"/>`;
      svg+=T_(nx+8,ny,'N',13,'start');
    }
  }

  return svg+'</svg>';
}

// === roads-tangent-arc: two roads cross at ค; arc tangent to both in 120° wedge ==
// ค at top. two full lines cross at ค (acute angle = crossDeg). arc (new road) sits
// in the obtuse wedge (180-crossDeg) opening downward, tangent to both roads.
// center O on the downward bisector at PO = rPx/sin((180-crossDeg)/2). R arrow O->arc.
// dashed line ค->nearest arc point = shortest distance. tangent right-angle marks.
// { type:"roads-tangent-arc", width,height, rPx(default 130), crossDeg(default 60),
//   apexLabel(default "ค"), angleLabel(default "60°"),
//   radiusLabel(default "R = 510 เมตร"),
//   roadLabelLeft, roadLabelRight, roadLabelArc,   // optional (Thai)
//   showShortest(default true), showTangentMarks(default true) }
// NOTE: Thai labels (ค / road names / เมตร) → cairosvg renders geometry only;
//       verify Thai on real viewer.
function renderRoadsTangentArc(spec){
  const pad=26;
  const rPx=spec.rPx||130;
  const cross=spec.crossDeg||60;
  const half=(180-cross)/2;            // half of obtuse wedge (=60 when cross=60)
  const hr=half*Math.PI/180;
  const PO=rPx/Math.sin(hr);

  // local frame: ค at (0,0), down bisector = +y
  const dl=[-Math.sin(hr),Math.cos(hr)];   // down-left road dir
  const dr=[ Math.sin(hr),Math.cos(hr)];   // down-right road dir
  const O=[0,PO];
  const t=PO*Math.cos(hr);                  // ค->tangent-point distance along road
  const Fl=[dl[0]*t,dl[1]*t], Fr=[dr[0]*t,dr[1]*t];
  const Ldown=t+46, Lup=52;
  const NA=[0,PO-rPx];                       // nearest arc point to ค

  // extents (local) to size canvas — only actually-drawn points
  const pts=[O,Fl,Fr,NA,[0,0],
             [dl[0]*Ldown,dl[1]*Ldown],[dr[0]*Ldown,dr[1]*Ldown],
             [-dr[0]*Lup,-dr[1]*Lup],[-dl[0]*Lup,-dl[1]*Lup]];
  let minx=Math.min(...pts.map(p=>p[0])), maxx=Math.max(...pts.map(p=>p[0]));
  let miny=Math.min(...pts.map(p=>p[1])), maxy=Math.max(...pts.map(p=>p[1]));
  const rightExtra=20;                       // small room for 60°/road labels
  maxx+=rightExtra; miny-=18; maxy+=8;        // room for ค label / road labels
  const ox=pad-minx, oy=pad-miny;            // local->screen offset
  const W=spec.width||Math.ceil(maxx-minx+2*pad);
  const H=spec.height||Math.ceil(maxy-miny+2*pad);
  const P=p=>[p[0]+ox,p[1]+oy];              // to screen

  const L=(p,q,st)=>{const a=P(p),b=P(q);return `<line x1="${a[0].toFixed(2)}" y1="${a[1].toFixed(2)}" x2="${b[0].toFixed(2)}" y2="${b[1].toFixed(2)}" stroke="#222" stroke-width="${st==='thin'?1:1.5}"${st==='dash'?' stroke-dasharray="6 4"':''}/>`;};
  const TX=(p,t,fs,anch)=>{const a=P(p);return `<text x="${a[0].toFixed(2)}" y="${a[1].toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-size="${fs||14}" fill="#222" text-anchor="${anch||'middle'}" dominant-baseline="central">${t}</text>`;};

  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;

  // roads (full lines through ค): up-stub + down-segment, each road solid
  svg+=L([-dr[0]*Lup,-dr[1]*Lup],[dr[0]*Ldown,dr[1]*Ldown]); // road B (up-left .. down-right)
  svg+=L([-dl[0]*Lup,-dl[1]*Lup],[dl[0]*Ldown,dl[1]*Ldown]); // road A (up-right .. down-left)

  // tangent arc (new road) — upper arc bulging toward ค
  {
    let a1=Math.atan2(Fl[1]-O[1],Fl[0]-O[0]), a2=Math.atan2(Fr[1]-O[1],Fr[0]-O[0]);
    let d=a2-a1; while(d<=-Math.PI)d+=2*Math.PI; while(d>Math.PI)d-=2*Math.PI;
    const mid=a1+d/2; if(O[1]+rPx*Math.sin(mid) > O[1]) d = d>0?d-2*Math.PI:d+2*Math.PI;
    const N=Math.max(20,Math.round(Math.abs(d)/0.07)); let dd='';
    for(let i=0;i<=N;i++){const a=a1+d*i/N; const pp=P([O[0]+rPx*Math.cos(a),O[1]+rPx*Math.sin(a)]); dd+=(i?' L ':'M ')+pp[0].toFixed(2)+' '+pp[1].toFixed(2);}
    svg+=`<path d="${dd}" fill="none" stroke="#222" stroke-width="2"/>`;
  }

  // radii O -> Fl, O -> Fr (perpendicular to roads at tangent points)
  if(spec.showRadii){
    const rl=(p)=>{const a=P(O),b=P(p);return `<line x1="${a[0].toFixed(2)}" y1="${a[1].toFixed(2)}" x2="${b[0].toFixed(2)}" y2="${b[1].toFixed(2)}" stroke="#222" stroke-width="1"/>`;};
    svg+=rl(Fl); svg+=rl(Fr);
  }

  // radius arrow O -> NA (top of arc)
  {
    const a=P(O), b=P(NA);
    svg+=`<line x1="${a[0].toFixed(2)}" y1="${a[1].toFixed(2)}" x2="${b[0].toFixed(2)}" y2="${b[1].toFixed(2)}" stroke="#222" stroke-width="1"/>`;
    // arrowhead at NA pointing up
    svg+=`<path d="M ${b[0].toFixed(2)} ${b[1].toFixed(2)} L ${(b[0]-3.5).toFixed(2)} ${(b[1]+6).toFixed(2)} L ${(b[0]+3.5).toFixed(2)} ${(b[1]+6).toFixed(2)} Z" fill="#222"/>`;
    // center dot
    svg+=`<circle cx="${a[0].toFixed(2)}" cy="${a[1].toFixed(2)}" r="2" fill="#222"/>`;
  }

  // dashed shortest distance ค -> NA
  if(spec.showShortest!==false) svg+=L([0,0],NA,'dash');

  // tangent right-angle marks at Fl, Fr (between road dir and radius F->O)
  if(spec.showTangentMarks!==false){
    const mark=(F,roadDir)=>{
      const u=(v)=>{const m=Math.hypot(v[0],v[1])||1;return [v[0]/m,v[1]/m];};
      const dRoad=u(roadDir), dRad=u([O[0]-F[0],O[1]-F[1]]); const s=9;
      const p1=P([F[0]+dRoad[0]*s,F[1]+dRoad[1]*s]);
      const p3=P([F[0]+dRad[0]*s,F[1]+dRad[1]*s]);
      const p2=P([F[0]+(dRoad[0]+dRad[0])*s,F[1]+(dRoad[1]+dRad[1])*s]);
      return `<path d="M ${p1[0].toFixed(2)} ${p1[1].toFixed(2)} L ${p2[0].toFixed(2)} ${p2[1].toFixed(2)} L ${p3[0].toFixed(2)} ${p3[1].toFixed(2)}" fill="none" stroke="#222" stroke-width="1"/>`;
    };
    svg+=mark(Fl,dl); svg+=mark(Fr,dr);
  }

  // 60° angle arc at ค on the right wedge (between up-right ray and down-right ray)
  {
    const upR=[-dl[0],-dl[1]];   // up-right = opposite of down-left (road A up)
    const a1=Math.atan2(upR[1],upR[0]), a2=Math.atan2(dr[1],dr[0]);
    let d=a2-a1; while(d>Math.PI)d-=2*Math.PI; while(d<-Math.PI)d+=2*Math.PI;
    const rad=24, N=Math.max(8,Math.round(Math.abs(d)/0.12)); let dd='';
    for(let i=0;i<=N;i++){const a=a1+d*i/N; const pp=P([rad*Math.cos(a),rad*Math.sin(a)]); dd+=(i?' L ':'M ')+pp[0].toFixed(2)+' '+pp[1].toFixed(2);}
    svg+=`<path d="${dd}" fill="none" stroke="#222" stroke-width="1"/>`;
    const am=a1+d/2, lr=rad+13;
    svg+=TX([lr*Math.cos(am),lr*Math.sin(am)],spec.angleLabel||'60°',13);
  }

  // labels
  const PLAB=spec.pointLabels||{};
  const rtxt=spec.radiusLabel||'510';
  svg+=TX([0,-Lup-12],spec.apexLabel||'ค',16);                       // ค above
  svg+=TX([10, PO-rPx/2], rtxt,13,'start');                          // 510 on bisector radius
  if(spec.showRadii) svg+=TX([(O[0]+Fr[0])/2+9,(O[1]+Fr[1])/2], rtxt,13,'start'); // 510 on right radius
  if(PLAB.tanL)   svg+=TX([Fl[0]-11,Fl[1]-7],PLAB.tanL,14,'end');    // ฉ
  if(PLAB.tanR)   svg+=TX([Fr[0]+11,Fr[1]-7],PLAB.tanR,14,'start');  // ง
  if(PLAB.near)   svg+=TX([-11,PO-rPx+2],PLAB.near,13,'end');        // ข
  if(PLAB.center) svg+=TX([11,PO+3],PLAB.center,14,'start');         // น
  if(spec.roadLabelLeft)  svg+=TX([dl[0]*Ldown-2,dl[1]*Ldown+14],spec.roadLabelLeft,12,'end');
  if(spec.roadLabelRight) svg+=TX([dr[0]*Ldown+2,dr[1]*Ldown+14],spec.roadLabelRight,12,'start');
  if(spec.roadLabelArc)   svg+=TX([-30,PO-rPx+30],spec.roadLabelArc,12,'end');

  return svg+'</svg>';
}

// === mirror-reflect-buildings: 2-panel optics figure (Q210) ====================
// panel1 (scene): sun + vertical incident ray -> mirror at A on roof of bldg A(hA);
//   reflects up to top of bldg B(hB) at horizontal dist; right-triangle A-C-B
//   (AC=dist horiz, CB=hB-hA vert, right angle at C, elevation theta at A).
// panel2 (detail): incident S (vertical) -> tilted mirror(alpha) -> reflect to B;
//   dashed normal bisects (beta=beta); theta(refl vs horiz) & alpha(mirror vs horiz).
// { type:'mirror-reflect-buildings', width,height, hA(10),hB(50),dist(30),
//   labels:{A,B,C}, hALabel('10'),distLabel('30'),cbLabel('40'),hBLabel('50'),
//   thetaLabel,alphaLabel,betaLabel,sLabel }  geometry+Greek render under cairosvg
function renderMirrorReflectBuildings(spec){
  spec=spec||{};
  const hA=spec.hA||10, hB=spec.hB||50, dist=spec.dist||30;
  const diff=hB-hA;
  const pxU=104/hB;
  const hAp=hA*pxU, hBp=hB*pxU, diffp=diff*pxU, distp=dist*pxU;
  const lab=Object.assign({A:'A',B:'B',C:'C'},spec.labels||{});
  const thL=spec.thetaLabel||'\u03b8', alL=spec.alphaLabel||'\u03b1',
        beL=spec.betaLabel||'\u03b2', sL=spec.sLabel||'S';
  const hALabel=spec.hALabel||'10', distLabel=spec.distLabel||'30',
        cbLabel=spec.cbLabel||'40', hBLabel=spec.hBLabel||'50';

  const pad=24, bwA=26, bwB=30, gap=30;

  // ---------- PANEL 1 (scene) ----------
  const sunRoom=80;
  const groundY=pad+sunRoom+hBp;
  const xA0=pad+26;
  const A=[xA0+bwA, groundY-hAp];
  const C=[A[0]+distp, A[1]];
  const B=[C[0], A[1]-diffp];          // = groundY-hBp
  const bBx=C[0];                       // building B left edge at C
  const p1Right=bBx+bwB+38;            // room for "50"

  // ---------- PANEL 2 (mirror detail) ----------
  const sX=p1Right+gap;
  const thetaRad=Math.atan2(diff,dist);          // elevation
  const alphaRad=Math.PI/4-0.5*thetaRad;         // mirror angle
  const cLen=78, bLen=96, mLen=44, nLen=70, sLen=70;
  const A2=[sX+62, pad+sunRoom+18];
  const dirRefl=[Math.cos(thetaRad),-Math.sin(thetaRad)];   // up-right
  const dirMirR=[Math.cos(alphaRad),Math.sin(alphaRad)];    // down-right
  const dirNorm=[Math.sin(alphaRad),-Math.cos(alphaRad)];   // up (bisector)
  const B2=[A2[0]+dirRefl[0]*bLen, A2[1]+dirRefl[1]*bLen];
  const C2=[B2[0], A2[1]];                                   // below B2, on horizontal
  const S2=[A2[0], A2[1]-sLen];                              // straight above (noon)
  const mR=[A2[0]+dirMirR[0]*mLen, A2[1]+dirMirR[1]*mLen];
  const mL=[A2[0]-dirMirR[0]*mLen, A2[1]-dirMirR[1]*mLen];
  const Ntip=[A2[0]+dirNorm[0]*nLen, A2[1]+dirNorm[1]*nLen];

  const W=spec.width||Math.ceil(Math.max(C2[0],B2[0])+pad+14);
  const H=spec.height||Math.ceil(groundY+pad+10);

  // ---------- draw helpers ----------
  const L=(p,q,st)=>`<line x1="${p[0].toFixed(2)}" y1="${p[1].toFixed(2)}" x2="${q[0].toFixed(2)}" y2="${q[1].toFixed(2)}" stroke="#222" stroke-width="${st==='thin'?1:(st==='thick'?2:1.5)}"${st==='dash'?' stroke-dasharray="5 4"':''}/>`;
  const TX=(x,y,t,fs,anch)=>`<text x="${x.toFixed(2)}" y="${y.toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-size="${fs||14}" fill="#222" text-anchor="${anch||'middle'}" dominant-baseline="central">${t}</text>`;
  const u=(p,q)=>{const dx=q[0]-p[0],dy=q[1]-p[1],m=Math.hypot(dx,dy)||1;return[dx/m,dy/m];};
  const arcA=(V,P1,P2,rad,txt,fs,lpush)=>{
    const a1=Math.atan2(P1[1]-V[1],P1[0]-V[0]); let d=Math.atan2(P2[1]-V[1],P2[0]-V[0])-a1;
    while(d>Math.PI)d-=2*Math.PI; while(d<-Math.PI)d+=2*Math.PI;
    const N=Math.max(8,Math.round(Math.abs(d)/0.1)); let dd='';
    for(let i=0;i<=N;i++){const a=a1+d*i/N;dd+=(i?' L ':'M ')+(V[0]+rad*Math.cos(a)).toFixed(2)+' '+(V[1]+rad*Math.sin(a)).toFixed(2);}
    let s=`<path d="${dd}" fill="none" stroke="#222" stroke-width="1"/>`;
    if(txt){const am=a1+d/2,lr=rad+(lpush||12);s+=TX(V[0]+lr*Math.cos(am),V[1]+lr*Math.sin(am),txt,fs||12);}
    return s;
  };
  const rAngle=(V,d1,d2,s)=>{
    const p1=[V[0]+d1[0]*s,V[1]+d1[1]*s],p3=[V[0]+d2[0]*s,V[1]+d2[1]*s];
    const p2=[V[0]+(d1[0]+d2[0])*s,V[1]+(d1[1]+d2[1])*s];
    return `<path d="M ${p1[0].toFixed(2)} ${p1[1].toFixed(2)} L ${p2[0].toFixed(2)} ${p2[1].toFixed(2)} L ${p3[0].toFixed(2)} ${p3[1].toFixed(2)}" fill="none" stroke="#222" stroke-width="1"/>`;
  };
  const arrowHead=(tip,dir)=>{ // dir = travel direction (unit)
    const back=[tip[0]-dir[0]*9,tip[1]-dir[1]*9], pp=[-dir[1],dir[0]];
    const w1=[back[0]+pp[0]*4,back[1]+pp[1]*4], w2=[back[0]-pp[0]*4,back[1]-pp[1]*4];
    return `<path d="M ${tip[0].toFixed(2)} ${tip[1].toFixed(2)} L ${w1[0].toFixed(2)} ${w1[1].toFixed(2)} L ${w2[0].toFixed(2)} ${w2[1].toFixed(2)} Z" fill="#222"/>`;
  };

  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  svg+=`<defs><pattern id="mrbHatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#222" stroke-width="0.7"/></pattern></defs>`;

  // ground line spanning panel 1
  svg+=L([pad,groundY],[bBx+bwB+10,groundY],'thin');

  // buildings (hatched)
  svg+=`<rect x="${xA0.toFixed(2)}" y="${(groundY-hAp).toFixed(2)}" width="${bwA}" height="${hAp.toFixed(2)}" fill="url(#mrbHatch)" stroke="#222" stroke-width="1.5"/>`;
  svg+=`<rect x="${bBx.toFixed(2)}" y="${B[1].toFixed(2)}" width="${bwB}" height="${(groundY-B[1]).toFixed(2)}" fill="url(#mrbHatch)" stroke="#222" stroke-width="1.5"/>`;

  // triangle A-C-B
  svg+=L(A,C); svg+=L(C,B); svg+=L(A,B,'thick');     // AB = reflected ray (emphasis)
  svg+=arrowHead(B,u(A,B));
  svg+=rAngle(C,u(C,A),u(C,B),10);
  svg+=arcA(A,C,B,26,thL,13,11);

  // sun + vertical incident arrow to A
  const sun=[A[0]-30, pad+20];
  svg+=`<circle cx="${sun[0].toFixed(2)}" cy="${sun[1].toFixed(2)}" r="11" fill="none" stroke="#222" stroke-width="1.3"/>`;
  for(let k=0;k<8;k++){const a=k*Math.PI/4;const r1=13,r2=18;svg+=`<line x1="${(sun[0]+r1*Math.cos(a)).toFixed(2)}" y1="${(sun[1]+r1*Math.sin(a)).toFixed(2)}" x2="${(sun[0]+r2*Math.cos(a)).toFixed(2)}" y2="${(sun[1]+r2*Math.sin(a)).toFixed(2)}" stroke="#222" stroke-width="1.1"/>`;}
  const inA=[A[0], A[1]-8];
  svg+=L([A[0],sun[1]+22],inA);
  svg+=arrowHead(inA,[0,1]);

  // labels panel1
  svg+=TX(xA0-7, groundY-hAp/2, hALabel, 12, 'end');          // 10 = height, left side of bldg A
  svg+=TX((A[0]+C[0])/2, A[1]+13, distLabel, 12);              // 30 below AC
  svg+=TX(C[0]-11, (C[1]+B[1])/2, cbLabel, 12, 'end');         // 40 left of CB
  svg+=TX(bBx+bwB+16, (groundY+B[1])/2, hBLabel, 12, 'start'); // 50 right of bldg B
  svg+=TX(A[0]-10, A[1]-11, lab.A, 14, 'end');                 // A above-left, clear of lines
  svg+=TX(B[0]-4, B[1]-12, lab.B, 14);
  svg+=TX(C[0]+10, C[1]+9, lab.C, 14, 'start');

  // ---------- PANEL 2 draw ----------
  // horizontal AC2, dashed normal & BC2
  svg+=L(A2,C2);                                  // horizontal AC
  svg+=L(B2,C2,'dash');                            // vertical BC dashed
  svg+=L(A2,Ntip,'dash');                          // normal dashed
  // mirror bar
  svg+=L(mL,mR,'thick');
  // incident S -> A2
  svg+=L(S2,[A2[0],A2[1]-9]);
  svg+=arrowHead([A2[0],A2[1]-9],[0,1]);
  // reflected A2 -> B2
  svg+=L(A2,B2);
  svg+=arrowHead(B2,dirRefl);
  // right angle at C2
  svg+=rAngle(C2,u(C2,A2),u(C2,B2),10);
  // angle arcs at A2: theta(AC..refl), alpha(AC..mirror down), beta(S..normal), beta(normal..refl)
  svg+=arcA(A2,C2,B2,30,thL,13,12);
  svg+=arcA(A2,C2,mR,17,alL,12,10);
  svg+=arcA(A2,S2,Ntip,22,beL,12,11);
  svg+=arcA(A2,Ntip,B2,34,beL,12,11);
  // labels panel2
  svg+=TX(S2[0]-3,S2[1]-9,sL,14,'end');
  svg+=TX(B2[0]+4,B2[1]-11,lab.B,14,'start');
  svg+=TX(C2[0]+10,C2[1]+9,lab.C,14,'start');
  svg+=TX(A2[0]-7,A2[1]+11,lab.A,14,'end');

  return svg+'</svg>';
}

// box-space-diagonal: 3D rectangular box (Q200), oblique projection.
// O front-bottom-left origin, A top vertex above O, B top vertex diagonally opposite A.
// face diagonal AB (dashed) + space diagonal OB (dotted), angle at B between them.
// hidden back edges dotted; axes x (down-right), y (depth, from B outward), z (up).
// spec: type, width, height, labels{O,A,B}, axisLabels{x,y,z},
//   xLabel('12'), yLabel('9'), angleLabel('30'), showAxes(true).
// all labels ascii/degree, fully cairosvg-verifiable (no Thai).
function renderBoxSpaceDiagonal(spec){
  spec=spec||{};
  const lab=Object.assign({O:'O',A:'A',B:'B'},spec.labels||{});
  const ax=Object.assign({x:'x',y:'y',z:'z'},spec.axisLabels||{});
  const xLabel=spec.xLabel||'12', yLabel=spec.yLabel||'9', angLabel=spec.angleLabel||'30\u00b0';

  // oblique projection basis (screen, y-down)
  const ex=[122, 20];      // x-axis (=12) right + slightly down
  const ey=[78, -46];      // y-axis (=9 depth) right + up (back)
  const ez=[0, -82];       // z-axis (height) up

  // local origin O at [0,0]; vertices a*ex+b*ey+c*ez
  const V=(a,b,c)=>[a*ex[0]+b*ey[0]+c*ez[0], a*ex[1]+b*ey[1]+c*ez[1]];
  const O=V(0,0,0), Xr=V(1,0,0), Yb=V(0,1,0), XYb=V(1,1,0);
  const A=V(0,0,1), AXr=V(1,0,1), AYb=V(0,1,1), B=V(1,1,1);

  // axis arrow ends (beyond box) — y extends outward from B (depth dir), matches source
  const zEnd=[ez[0]*1.45, ez[1]*1.45];
  const xEnd=[ex[0]*1.5, ex[1]*1.5];
  const Bv=[ex[0]+ey[0]+ez[0], ex[1]+ey[1]+ez[1]];
  const yEnd=[Bv[0]+ey[0]*0.72, Bv[1]+ey[1]*0.72];

  // extents
  const all=[O,Xr,Yb,XYb,A,AXr,AYb,B,zEnd,xEnd,yEnd];
  let minx=Math.min(...all.map(p=>p[0])), maxx=Math.max(...all.map(p=>p[0]));
  let miny=Math.min(...all.map(p=>p[1])), maxy=Math.max(...all.map(p=>p[1]));
  const pad=26;
  minx-=14; maxx+=22; miny-=14; maxy+=16;     // label room
  const ox=pad-minx, oy=pad-miny;
  const W=spec.width||Math.ceil(maxx-minx+2*pad);
  const H=spec.height||Math.ceil(maxy-miny+2*pad);
  const P=p=>[p[0]+ox,p[1]+oy];

  const L=(p,q,st)=>{const a=P(p),b=P(q);let da='';if(st==='dash')da=' stroke-dasharray="6 4"';else if(st==='dot')da=' stroke-dasharray="1.5 3"';return `<line x1="${a[0].toFixed(2)}" y1="${a[1].toFixed(2)}" x2="${b[0].toFixed(2)}" y2="${b[1].toFixed(2)}" stroke="#222" stroke-width="${st==='thin'?1:1.5}"${da}/>`;};
  const TX=(p,t,fs,anch)=>{const a=P(p);return `<text x="${a[0].toFixed(2)}" y="${a[1].toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-size="${fs||14}" fill="#222" text-anchor="${anch||'middle'}" dominant-baseline="central">${t}</text>`;};
  const u=(p,q)=>{const dx=q[0]-p[0],dy=q[1]-p[1],m=Math.hypot(dx,dy)||1;return[dx/m,dy/m];};
  const arrow=(tip,dir)=>{const t=P(tip);const b=[t[0]-dir[0]*9,t[1]-dir[1]*9],pp=[-dir[1],dir[0]];const w1=[b[0]+pp[0]*4,b[1]+pp[1]*4],w2=[b[0]-pp[0]*4,b[1]-pp[1]*4];return `<path d="M ${t[0].toFixed(2)} ${t[1].toFixed(2)} L ${w1[0].toFixed(2)} ${w1[1].toFixed(2)} L ${w2[0].toFixed(2)} ${w2[1].toFixed(2)} Z" fill="#222"/>`;};
  const arcA=(Vp,P1,P2,rad,txt,fs,lpush)=>{
    const a1=Math.atan2(P1[1]-Vp[1],P1[0]-Vp[0]); let d=Math.atan2(P2[1]-Vp[1],P2[0]-Vp[0])-a1;
    while(d>Math.PI)d-=2*Math.PI; while(d<-Math.PI)d+=2*Math.PI;
    const N=Math.max(8,Math.round(Math.abs(d)/0.1)); let dd='';
    for(let i=0;i<=N;i++){const a=a1+d*i/N;const pp=P([Vp[0]+rad*Math.cos(a),Vp[1]+rad*Math.sin(a)]);dd+=(i?' L ':'M ')+pp[0].toFixed(2)+' '+pp[1].toFixed(2);}
    let s=`<path d="${dd}" fill="none" stroke="#222" stroke-width="1"/>`;
    if(txt){const am=a1+d/2,lr=rad+(lpush||12);s+=TX([Vp[0]+lr*Math.cos(am),Vp[1]+lr*Math.sin(am)],txt,fs||12);}
    return s;
  };

  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;

  // hidden back edges (dotted) — 3 edges at back-bottom-left Yb
  svg+=L(O,Yb,'dot'); svg+=L(Yb,XYb,'dot'); svg+=L(Yb,AYb,'dot');

  // axes (drawn behind box where relevant)
  if(spec.showAxes!==false){
    svg+=L(O,zEnd,'thin'); svg+=arrow(zEnd,u(O,zEnd)); svg+=TX([zEnd[0],zEnd[1]-9],ax.z,13);
    svg+=L(O,xEnd,'thin'); svg+=arrow(xEnd,u(O,xEnd)); svg+=TX([xEnd[0]+8,xEnd[1]+6],ax.x,13,'start');
    svg+=L(B,yEnd,'thin'); svg+=arrow(yEnd,u(B,yEnd)); svg+=TX([yEnd[0]+9,yEnd[1]-2],ax.y,13,'start');
  }

  // visible solid edges
  svg+=L(O,Xr); svg+=L(O,A); svg+=L(Xr,XYb); svg+=L(Xr,AXr);
  svg+=L(A,AXr); svg+=L(A,AYb); svg+=L(AXr,B); svg+=L(AYb,B); svg+=L(XYb,B);

  // diagonals: AB (top face, dashed) + OB (space, dotted)
  svg+=L(A,B,'dash'); svg+=L(O,B,'dot');

  // 30 angle at B between B->A and B->O
  svg+=arcA(B,A,O,22,angLabel,12,10);

  // edge labels 12 (O-Xr), 9 (A-AYb top y-edge)
  svg+=TX([(O[0]+Xr[0])/2, (O[1]+Xr[1])/2+13], xLabel, 13);
  svg+=TX([(A[0]+AYb[0])/2-6, (A[1]+AYb[1])/2-10], yLabel, 13, 'end');

  // vertex labels
  svg+=TX([O[0]-11,O[1]+2], lab.O, 14, 'end');
  svg+=TX([A[0]-11,A[1]], lab.A, 14, 'end');
  svg+=TX([B[0]+11,B[1]], lab.B, 14, 'start');

  return svg+'</svg>';
}

// === roads-curve-survey: inaccessible-vertex survey + tangent circular curve (Q209) ===
// Two straight roads meet at inaccessible apex A (in a ravine). Survey points X (on road A-B)
// and Y (on road A-C); survey line XY. Circular curve radius R tangent to both roads at B,C;
// centre O on bisector AO. Construction overlay: AO bisector(dashed), OB/OC radii, right
// angles at X (AXY), B, C, and 30°+30° at A. √/Greek via _ucMathToSvg → full cairosvg verify.
// { type:'roads-curve-survey', width,height, halfDeg(27), abPx(290), axPx(110), ayPx(150),
//   roadLen(378), ravineY(18), labels:{A,X,Y,B,C,O,P,Q},
//   xyLabel('105\\sqrt{3}'), rLabel('R = 200\\sqrt{3}'),
//   angXLabel('90°'), angYLabel('150°'), angALabel('30°') }  defaults suffice.
function renderRoadsCurveSurvey(spec){
  const pad = 26;
  const half = (spec.halfDeg||27)*Math.PI/180;
  const uL=[-Math.sin(half),Math.cos(half)], uR=[Math.sin(half),Math.cos(half)], uD=[0,1];
  const ABd=spec.abPx||290, AOd=ABd/Math.cos(half), Rd=AOd*Math.sin(half);
  const dX=spec.axPx||110, dY=spec.ayPx||150, dRoad=spec.roadLen||378;
  const A=[0,0];
  const sc=(u,d)=>[u[0]*d,u[1]*d];
  const B=sc(uL,ABd), C=sc(uR,ABd), O=[0,AOd];
  const X=sc(uL,dX), Y=sc(uR,dY), Pp=sc(uL,dRoad), Qp=sc(uR,dRoad);

  // canvas extents from drawn geometric points (+ ravine)
  const gpts=[A,Pp,Qp,O,B,C,X,Y];
  let minx=Math.min(...gpts.map(p=>p[0])), maxx=Math.max(...gpts.map(p=>p[0]));
  let miny=Math.min(...gpts.map(p=>p[1])), maxy=Math.max(...gpts.map(p=>p[1]));
  const ravineY=(spec.ravineY!==undefined)?spec.ravineY:18;
  miny=Math.min(miny,ravineY-20);
  minx-=24; maxx+=24; miny-=14; maxy+=20;
  const ox=pad-minx, oy=pad-miny;
  const W=spec.width||Math.ceil(maxx-minx+2*pad);
  const H=spec.height||Math.ceil(maxy-miny+2*pad);
  const P=p=>[p[0]+ox,p[1]+oy];
  const u=(v)=>{const m=Math.hypot(v[0],v[1])||1;return[v[0]/m,v[1]/m];};

  const L=(p,q,col,dash,w)=>{const a=P(p),b=P(q);return `<line x1="${a[0].toFixed(2)}" y1="${a[1].toFixed(2)}" x2="${b[0].toFixed(2)}" y2="${b[1].toFixed(2)}" stroke="${col||'#222'}" stroke-width="${w||1.5}"${dash?` stroke-dasharray="${dash}"`:''}/>`;};
  const TX=(p,t,fs,anch,col)=>{const a=P(p);return `<text x="${a[0].toFixed(2)}" y="${a[1].toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-size="${fs||14}" fill="${col||'#222'}" text-anchor="${anch||'middle'}" dominant-baseline="central">${t}</text>`;};
  const SQ=(p,latex,fs,col)=>{const a=P(p);return _ucMathToSvg(latex,a[0],a[1],fs||16,col||'#222');};

  const lab=Object.assign({A:'A',X:'X',Y:'Y',B:'B',C:'C',O:'O',P:'P',Q:'Q'},spec.labels||{});

  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;

  // ravine: wavy horizontal line + jagged Z marks at both ends
  {
    const wy=ravineY, x0=minx+6, x1=maxx-6, step=27, amp=4;
    const s0=P([x0,wy]); let d='M '+s0[0].toFixed(2)+' '+s0[1].toFixed(2)+' ';
    let xx=x0,i=0;
    while(xx<x1){const x2=Math.min(xx+step,x1);const my=wy+((i%2===0)?amp:-amp);const c=P([xx+step/2,my]),e=P([x2,wy]);d+=`Q ${c[0].toFixed(2)} ${c[1].toFixed(2)} ${e[0].toFixed(2)} ${e[1].toFixed(2)} `;xx=x2;i++;}
    svg+=`<path d="${d}" fill="none" stroke="#aaa" stroke-width="1.2"/>`;
    const zz=(zx)=>{const a=P([zx,wy-24]),b=P([zx+22,wy-16]),c=P([zx+4,wy-8]),e=P([zx+26,wy]);return `<polyline points="${a[0].toFixed(2)},${a[1].toFixed(2)} ${b[0].toFixed(2)},${b[1].toFixed(2)} ${c[0].toFixed(2)},${c[1].toFixed(2)} ${e[0].toFixed(2)},${e[1].toFixed(2)}" fill="none" stroke="#aaa" stroke-width="1.2"/>`;};
    svg+=zz(x0+24); svg+=zz(x1-50);
  }

  // construction (faint): AO bisector + OC radius (dashed)
  svg+=L(A,O,'#888','5 4',1.2);
  svg+=L(O,C,'#888','5 4',1.2);

  // roads A->P (left), A->Q (right)
  svg+=L(A,Pp,'#222',null,2);
  svg+=L(A,Qp,'#222',null,2);

  // survey line XY (blue)
  svg+=L(X,Y,'#1559c4',null,2);

  // tangent arc B..C bulging toward apex A
  {
    let a1=Math.atan2(B[1]-O[1],B[0]-O[0]), a2=Math.atan2(C[1]-O[1],C[0]-O[0]);
    let dd=a2-a1; while(dd<=-Math.PI)dd+=2*Math.PI; while(dd>Math.PI)dd-=2*Math.PI;
    const mid=a1+dd/2; if(O[1]+Rd*Math.sin(mid) > O[1]) dd = dd>0?dd-2*Math.PI:dd+2*Math.PI;
    const N=Math.max(24,Math.round(Math.abs(dd)/0.06)); let path='';
    for(let k=0;k<=N;k++){const a=a1+dd*k/N;const pp=P([O[0]+Rd*Math.cos(a),O[1]+Rd*Math.sin(a)]);path+=(k?' L ':'M ')+pp[0].toFixed(2)+' '+pp[1].toFixed(2);}
    svg+=`<path d="${path}" fill="none" stroke="#222" stroke-width="2"/>`;
  }

  // radius arrow O -> B (solid) + arrowhead + centre dot
  {
    svg+=L(O,B,'#222',null,1.5);
    const ad=u([B[0]-O[0],B[1]-O[1]]); const hb=P([B[0]-ad[0]*13,B[1]-ad[1]*13]); const bb=P(B); const pp=[-ad[1],ad[0]];
    svg+=`<polygon points="${bb[0].toFixed(2)},${bb[1].toFixed(2)} ${(hb[0]+pp[0]*5).toFixed(2)},${(hb[1]+pp[1]*5).toFixed(2)} ${(hb[0]-pp[0]*5).toFixed(2)},${(hb[1]-pp[1]*5).toFixed(2)}" fill="#222"/>`;
    const o=P(O); svg+=`<circle cx="${o[0].toFixed(2)}" cy="${o[1].toFixed(2)}" r="2" fill="#222"/>`;
  }

  // right-angle marks: X (AXY), B (OB perp road), C (OC perp road)
  const raMark=(p,d1,d2,s)=>{s=s||11;const a=P([p[0]+d1[0]*s,p[1]+d1[1]*s]),b=P([p[0]+(d1[0]+d2[0])*s,p[1]+(d1[1]+d2[1])*s]),c=P([p[0]+d2[0]*s,p[1]+d2[1]*s]);return `<polyline points="${a[0].toFixed(2)},${a[1].toFixed(2)} ${b[0].toFixed(2)},${b[1].toFixed(2)} ${c[0].toFixed(2)},${c[1].toFixed(2)}" fill="none" stroke="#222" stroke-width="1.3"/>`;};
  svg+=raMark(X,u([A[0]-X[0],A[1]-X[1]]),u([Y[0]-X[0],Y[1]-X[1]]));
  svg+=raMark(B,u([A[0]-B[0],A[1]-B[1]]),u([O[0]-B[0],O[1]-B[1]]));
  svg+=raMark(C,u([A[0]-C[0],A[1]-C[1]]),u([O[0]-C[0],O[1]-C[1]]));

  // angle arcs at A: 30 (left, BAO) + 30 (right, CAO)
  const angArc=(center,d1,d2,r,label,loff)=>{
    const a1=Math.atan2(d1[1],d1[0]),a2=Math.atan2(d2[1],d2[0]);
    let dd=a2-a1; while(dd>Math.PI)dd-=2*Math.PI; while(dd<-Math.PI)dd+=2*Math.PI;
    const N=Math.max(8,Math.round(Math.abs(dd)/0.1));let path='';
    for(let k=0;k<=N;k++){const a=a1+dd*k/N;const pp=P([center[0]+r*Math.cos(a),center[1]+r*Math.sin(a)]);path+=(k?' L ':'M ')+pp[0].toFixed(2)+' '+pp[1].toFixed(2);}
    const bis=u([d1[0]+d2[0],d1[1]+d2[1]]);const lp=[center[0]+bis[0]*(r+loff),center[1]+bis[1]*(r+loff)];
    return `<path d="${path}" fill="none" stroke="#b8350e" stroke-width="1.3"/>`+TX(lp,label,14,'middle','#b8350e');
  };
  svg+=angArc(A,uL,uD,40,spec.angALabel||'30°',22);
  svg+=angArc(A,uD,uR,40,spec.angALabel||'30°',22);

  // given-value labels
  svg+=SQ([(X[0]+Y[0])/2-4,(X[1]+Y[1])/2-9],spec.xyLabel||'105\\sqrt{3}',16,'#1559c4');
  svg+=SQ([(O[0]+B[0])/2-78,(O[1]+B[1])/2-2],spec.rLabel||'R = 200\\sqrt{3}',16,'#222');
  svg+=TX([X[0]-13,X[1]+18],spec.angXLabel||'90°',14,'end','#b8350e');
  svg+=TX([Y[0]-30,Y[1]+17],spec.angYLabel||'150°',14,'start','#b8350e');

  // point dots + labels
  const dot=p=>{const a=P(p);return `<circle cx="${a[0].toFixed(2)}" cy="${a[1].toFixed(2)}" r="3" fill="#222"/>`;};
  [A,X,Y,B,C,O].forEach(p=>{svg+=dot(p);});
  svg+=TX([A[0],A[1]-13],lab.A,16,'middle');
  svg+=TX([X[0]-15,X[1]-7],lab.X,15,'end');
  svg+=TX([Y[0]+11,Y[1]+9],lab.Y,15,'start');
  svg+=TX([B[0]-15,B[1]+4],lab.B,15,'end');
  svg+=TX([C[0]+12,C[1]+4],lab.C,15,'start');
  svg+=TX([O[0],O[1]+15],lab.O,15,'middle');
  svg+=TX([Pp[0]-13,Pp[1]+8],lab.P,15,'end');
  svg+=TX([Qp[0]+11,Qp[1]+8],lab.Q,15,'start');

  return svg+'</svg>';
}

function renderQuarterCircleInscribedRect(spec){
  const Rm=spec.radius||2, ang=(spec.angleDeg||60)*Math.PI/180, s=spec.scale||116, pad=30;
  const Bx=Rm*Math.cos(ang), By=Rm*Math.sin(ang);
  const O=[0,0], Pp=[Rm,0], Qp=[0,Rm], A=[0,By], B=[Bx,By], C=[Bx,0];
  const W=spec.width||Math.ceil(Rm*s+2*pad+16), H=spec.height||Math.ceil(Rm*s+2*pad+16);
  const ox=pad+8, oy=H-pad-8;
  const T=p=>[ox+p[0]*s, oy-p[1]*s];
  const SHADE='#8fb3e0', SHADE_OP=0.55;
  const TXpx=(x,y,t,fs,anch,col)=>`<text x="${x.toFixed(2)}" y="${y.toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-size="${fs||15}" fill="${col||'#222'}" text-anchor="${anch||'middle'}" dominant-baseline="central">${t}</text>`;
  const L=(p,q,col,dash,w)=>{const a=T(p),b=T(q);return `<line x1="${a[0].toFixed(2)}" y1="${a[1].toFixed(2)}" x2="${b[0].toFixed(2)}" y2="${b[1].toFixed(2)}" stroke="${col||'#222'}" stroke-width="${w||1.5}"${dash?` stroke-dasharray="${dash}"`:''}/>`;};
  const lab=Object.assign({O:'O',A:'A',B:'B',C:'C',P:'P',Q:'Q'},spec.labels||{});
  const aO=T(O),aP=T(Pp),aQ=T(Qp),aA=T(A),aB=T(B),aC=T(C);

  // arc P->Q as polyline (avoids SVG arc-flag ambiguity; robust in cairosvg + browser)
  const NA=48, arc=[];
  for(let i=0;i<=NA;i++){const t=(Math.PI/2)*i/NA; arc.push(T([Rm*Math.cos(t),Rm*Math.sin(t)]));}
  const arcD=arc.map(a=>`${a[0].toFixed(2)} ${a[1].toFixed(2)}`).join(' L ');

  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;

  // shaded region = quarter disk MINUS rectangle (evenodd)
  const diskPath=`M ${aO[0].toFixed(2)} ${aO[1].toFixed(2)} L ${arcD} Z`;
  const rectPath=`M ${aO[0].toFixed(2)} ${aO[1].toFixed(2)} L ${aA[0].toFixed(2)} ${aA[1].toFixed(2)} L ${aB[0].toFixed(2)} ${aB[1].toFixed(2)} L ${aC[0].toFixed(2)} ${aC[1].toFixed(2)} Z`;
  svg+=`<path d="${diskPath} ${rectPath}" fill="${SHADE}" fill-opacity="${SHADE_OP}" fill-rule="evenodd" stroke="none"/>`;

  // quarter-circle outline: radii OP, OQ + arc
  svg+=L(O,Pp,'#222',null,1.6);
  svg+=L(O,Qp,'#222',null,1.6);
  svg+=`<path d="M ${arcD}" fill="none" stroke="#222" stroke-width="1.6"/>`;

  // rectangle OABC outline
  svg+=`<path d="${rectPath}" fill="none" stroke="#222" stroke-width="1.4"/>`;

  // OB diagonal + angle marker at O (between +x axis OC and OB)
  svg+=L(O,B,'#222',null,1.2);
  {
    const arr=26, Nm=18, mk=[];
    for(let i=0;i<=Nm;i++){const t=ang*i/Nm; mk.push([ox+arr*Math.cos(t), oy-arr*Math.sin(t)]);}
    svg+=`<path d="M ${mk.map(m=>`${m[0].toFixed(2)} ${m[1].toFixed(2)}`).join(' L ')}" fill="none" stroke="#b8350e" stroke-width="1.2"/>`;
    const ml=ang/2, lr=arr+13;
    svg+=TXpx(ox+lr*Math.cos(ml), oy-lr*Math.sin(ml), spec.angleLabel||'60\u00b0', 13, 'middle', '#b8350e');
  }

  // optional radius label on OP
  if(spec.rLabel){ svg+=TXpx((aO[0]+aP[0])/2, aO[1]+15, spec.rLabel, 13, 'middle', '#555'); }

  // point dots + labels
  const dot=a=>`<circle cx="${a[0].toFixed(2)}" cy="${a[1].toFixed(2)}" r="2.6" fill="#222"/>`;
  [aO,aA,aB,aC,aP,aQ].forEach(a=>{svg+=dot(a);});
  svg+=TXpx(aO[0]-10, aO[1]+13, lab.O, 15, 'middle');
  svg+=TXpx(aP[0]+11, aP[1]+3,  lab.P, 15, 'start');
  svg+=TXpx(aQ[0]-3,  aQ[1]-11, lab.Q, 15, 'middle');
  svg+=TXpx(aA[0]-11, aA[1],    lab.A, 15, 'end');
  svg+=TXpx(aB[0]+9,  aB[1]-7,  lab.B, 15, 'start');
  svg+=TXpx(aC[0]+4,  aC[1]+14, lab.C, 15, 'middle');

  return svg+'</svg>';
}

// ----- renderer: argand-plane -----
// Complex plane (Argand diagram) with EQUAL aspect ratio so |z|=r circles
// render as true circles (not ellipses) and loci/perp-bisectors stay correct.
// One px-per-unit scale for both Re & Im; data box centered in the canvas.
//
// Spec fields:
//   width, height                 - canvas px (default 360 x 320)
//   pad:{l,r,t,b}                 - optional px margins
//   reRange:[a,b], imRange:[a,b]  - data window (origin should lie inside)
//   axes:{ arrows?(default true), reLabel?(default 'Re'), imLabel?(default 'Im'),
//          originLabel?, reTicks:[...], imTicks:[...] }
//   circles:[ {center:[re,im], r, dashed?, color?, fill?, label?, labelAt?} ]
//   lines:[   {through:[[x,y],[x,y]] | point:[x,y],slope:m, dashed?, color?,
//              label?, labelAt?, labelAnchor?} ]   loci — clipped to data box
//   segments:[ {from:[re,im], to:[re,im], dashed?, color?} ]   finite guides
//   vectors:[ {to:[re,im], from?:[re,im](default O), label?, labelAt?,
//              labelDx?, labelDy?, labelAnchor?, color?} ]   arrow from→to
//   angleArcs:[ {at:[re,im], from:[re,im], to:[re,im], r?(px), label?, color?} ]
//   points:[ {re, im, label? | showCoord?, open?, color?,
//              labelDx?, labelDy?, labelAnchor?, labelFs?} ]   open→hollow dot
// LaTeX labels ($..$ / \sqrt{}) rendered via _ucMathToSvg (native √ vinculum).
function renderArgandPlane(spec){
  const W = spec.width || 360, H = spec.height || 320;
  const pd = spec.pad || {};
  const pL = pd.l != null ? pd.l : 28;
  const pR = pd.r != null ? pd.r : 24;
  const pT = pd.t != null ? pd.t : 22;
  const pB = pd.b != null ? pd.b : 26;
  const reR = spec.reRange || [-1, 1];
  const imR = spec.imRange || [-1, 1];
  const reSpan = reR[1] - reR[0], imSpan = imR[1] - imR[0];
  const pW = W - pL - pR, pH = H - pT - pB;
  const scale = Math.min(pW / reSpan, pH / imSpan);   // EQUAL aspect
  const boxW = scale * reSpan, boxH = scale * imSpan;
  const offX = pL + (pW - boxW) / 2;
  const offY = pT + (pH - boxH) / 2;
  const X = re => offX + (re - reR[0]) * scale;
  const Y = im => offY + (imR[1] - im) * scale;        // Y flipped
  const ff = "'Cambria Math','Times New Roman',serif";

  const lbl = (text, x, y, fs, color, anchor) => {
    color = color || '#222'; anchor = anchor || 'start';
    if(/\\sqrt/.test(text)){
      const w = _nlLatexW(text, fs), ox = anchor === 'end' ? -w : anchor === 'middle' ? -w/2 : 0;
      return _ucMathToSvg(text, x + ox, y, fs, color);
    }
    return `<text x="${x.toFixed(2)}" y="${y.toFixed(2)}" font-family="${ff}" `
         + `font-size="${fs}" fill="${color}" text-anchor="${anchor}">${text}</text>`;
  };
  const head = (x1, y1, x2, y2, color, size) => {   // filled arrowhead at (x2,y2)
    size = size || 8;
    const ang = Math.atan2(y2 - y1, x2 - x1);
    const xa = x2 + size * Math.cos(ang + Math.PI - 0.42), ya = y2 + size * Math.sin(ang + Math.PI - 0.42);
    const xb = x2 + size * Math.cos(ang + Math.PI + 0.42), yb = y2 + size * Math.sin(ang + Math.PI + 0.42);
    return `<path d="M${x2.toFixed(2)} ${y2.toFixed(2)} L${xa.toFixed(2)} ${ya.toFixed(2)} `
         + `L${xb.toFixed(2)} ${yb.toFixed(2)} z" fill="${color}"/>`;
  };

  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  svg += `<defs><marker id="apArr" viewBox="0 0 10 10" refX="9" refY="5" `
       + `markerWidth="7" markerHeight="7" orient="auto-start-reverse">`
       + `<path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/></marker></defs>`;

  // ---- axes ----
  const ax = spec.axes || {};
  const x0 = X(0), y0 = Y(0);
  const arr = ax.arrows !== false ? ' marker-end="url(#apArr)"' : '';
  svg += `<line x1="${(pL - 4).toFixed(2)}" y1="${y0.toFixed(2)}" `
       + `x2="${(W - pR + 8).toFixed(2)}" y2="${y0.toFixed(2)}" `
       + `stroke="#222" stroke-width="1.2"${arr}/>`;
  svg += `<line x1="${x0.toFixed(2)}" y1="${(H - pB + 6).toFixed(2)}" `
       + `x2="${x0.toFixed(2)}" y2="${(pT - 8).toFixed(2)}" `
       + `stroke="#222" stroke-width="1.2"${arr}/>`;
  (ax.reTicks || []).forEach(t => { if(t === 0) return; const xp = X(t);
    svg += `<line x1="${xp.toFixed(2)}" y1="${(y0 - 3).toFixed(2)}" x2="${xp.toFixed(2)}" y2="${(y0 + 3).toFixed(2)}" stroke="#222"/>`
         + `<text x="${xp.toFixed(2)}" y="${(y0 + 14).toFixed(2)}" text-anchor="middle" font-size="10" fill="#555">${t}</text>`; });
  (ax.imTicks || []).forEach(t => { if(t === 0) return; const yp = Y(t);
    svg += `<line x1="${(x0 - 3).toFixed(2)}" y1="${yp.toFixed(2)}" x2="${(x0 + 3).toFixed(2)}" y2="${yp.toFixed(2)}" stroke="#222"/>`
         + `<text x="${(x0 - 6).toFixed(2)}" y="${(yp + 3.5).toFixed(2)}" text-anchor="end" font-size="10" fill="#555">${t}</text>`; });
  const reLab = ax.reLabel !== undefined ? ax.reLabel : 'Re';
  const imLab = ax.imLabel !== undefined ? ax.imLabel : 'Im';
  if(reLab) svg += `<text x="${(W - pR + 10).toFixed(2)}" y="${(y0 + 4).toFixed(2)}" font-size="13" fill="#222">${reLab}</text>`;
  if(imLab) svg += `<text x="${(x0 + 6).toFixed(2)}" y="${(pT - 1).toFixed(2)}" font-size="13" fill="#222">${imLab}</text>`;
  if(ax.originLabel) svg += `<text x="${(x0 - 7).toFixed(2)}" y="${(y0 + 13).toFixed(2)}" font-size="12" fill="#222" text-anchor="end">${ax.originLabel}</text>`;

  // ---- circles ----
  (spec.circles || []).forEach(c => {
    const cx = X(c.center[0]), cy = Y(c.center[1]), rPx = c.r * scale;
    const dash = c.dashed ? ' stroke-dasharray="5 4"' : '';
    svg += `<circle cx="${cx.toFixed(2)}" cy="${cy.toFixed(2)}" r="${rPx.toFixed(2)}" `
         + `fill="${c.fill || 'none'}" stroke="${c.color || '#222'}" stroke-width="1.5"${dash}/>`;
    if(c.label && c.labelAt) svg += lbl(c.label, X(c.labelAt[0]), Y(c.labelAt[1]), c.labelFs || 12, c.color || '#222', c.labelAnchor || 'start');
  });

  // ---- loci lines (clipped analytically to data box; no giant coords) ----
  (spec.lines || []).forEach(L => {
    let p1, p2;
    if(L.through){ p1 = L.through[0]; p2 = L.through[1]; }
    else if(L.point && L.slope !== undefined){ p1 = L.point; p2 = [L.point[0] + 1, L.point[1] + L.slope]; }
    else return;
    const dx = p2[0] - p1[0], dy = p2[1] - p1[1];
    // Liang-Barsky: clip the infinite line to [reR]x[imR] in data coords
    const pp = [-dx, dx, -dy, dy];
    const qq = [p1[0] - reR[0], reR[1] - p1[0], p1[1] - imR[0], imR[1] - p1[1]];
    let t0 = -1e9, t1 = 1e9, ok = true;
    for(let i = 0; i < 4; i++){
      if(pp[i] === 0){ if(qq[i] < 0){ ok = false; break; } }
      else { const r = qq[i] / pp[i]; if(pp[i] < 0){ if(r > t0) t0 = r; } else { if(r < t1) t1 = r; } }
    }
    if(!ok || t0 > t1) return;
    const Ax = p1[0] + t0 * dx, Ay = p1[1] + t0 * dy, Bx = p1[0] + t1 * dx, By = p1[1] + t1 * dy;
    const dash = L.dashed ? ' stroke-dasharray="5 4"' : '';
    svg += `<line x1="${X(Ax).toFixed(2)}" y1="${Y(Ay).toFixed(2)}" x2="${X(Bx).toFixed(2)}" y2="${Y(By).toFixed(2)}" `
         + `stroke="${L.color || '#222'}" stroke-width="1.5"${dash}/>`;
    if(L.label && L.labelAt) svg += lbl(L.label, X(L.labelAt[0]), Y(L.labelAt[1]), L.labelFs || 12, L.color || '#222', L.labelAnchor || 'start');
  });

  // ---- finite guide segments ----
  (spec.segments || []).forEach(s => {
    const dash = s.dashed !== false ? ' stroke-dasharray="4 3"' : '';
    svg += `<line x1="${X(s.from[0]).toFixed(2)}" y1="${Y(s.from[1]).toFixed(2)}" `
         + `x2="${X(s.to[0]).toFixed(2)}" y2="${Y(s.to[1]).toFixed(2)}" `
         + `stroke="${s.color || '#888'}" stroke-width="1.1"${dash}/>`;
  });

  // ---- vectors (arrow from→to, manual colored head) ----
  (spec.vectors || []).forEach(v => {
    const from = v.from || [0, 0], to = v.to, col = v.color || '#222';
    const x1 = X(from[0]), y1 = Y(from[1]), x2 = X(to[0]), y2 = Y(to[1]);
    svg += `<line x1="${x1.toFixed(2)}" y1="${y1.toFixed(2)}" x2="${x2.toFixed(2)}" y2="${y2.toFixed(2)}" stroke="${col}" stroke-width="1.8"/>`;
    svg += head(x1, y1, x2, y2, col, 8);
    if(v.label){ const at = v.labelAt || to;
      svg += lbl(v.label, X(at[0]) + (v.labelDx != null ? v.labelDx : 6), Y(at[1]) + (v.labelDy != null ? v.labelDy : -6), v.labelFs || 14, col, v.labelAnchor || 'start'); }
  });

  // ---- angle arcs ----
  (spec.angleArcs || []).forEach(a => {
    const v = a.at || [0, 0], vx = X(v[0]), vy = Y(v[1]), rPx = a.r || 22;
    const sa = -Math.atan2(a.from[1] - v[1], a.from[0] - v[0]);   // screen angle (Y flipped)
    const ea = -Math.atan2(a.to[1] - v[1], a.to[0] - v[0]);
    const x1 = vx + rPx * Math.cos(sa), y1 = vy + rPx * Math.sin(sa);
    const x2 = vx + rPx * Math.cos(ea), y2 = vy + rPx * Math.sin(ea);
    let diff = ea - sa; while(diff <= -Math.PI) diff += 2 * Math.PI; while(diff > Math.PI) diff -= 2 * Math.PI;
    const sweep = diff > 0 ? 1 : 0;
    svg += `<path d="M${x1.toFixed(2)} ${y1.toFixed(2)} A${rPx} ${rPx} 0 0 ${sweep} ${x2.toFixed(2)} ${y2.toFixed(2)}" `
         + `fill="none" stroke="${a.color || '#222'}" stroke-width="1.2"/>`;
    if(a.label){ const mid = sa + diff / 2, lr = rPx + 11;
      svg += lbl(a.label, vx + lr * Math.cos(mid), vy + lr * Math.sin(mid) + 4, a.labelFs || 12, a.color || '#222', 'middle'); }
  });

  // ---- points (top layer) ----
  (spec.points || []).forEach(p => {
    const cx = X(p.re), cy = Y(p.im), col = p.color || '#222';
    if(p.open) svg += `<circle cx="${cx.toFixed(2)}" cy="${cy.toFixed(2)}" r="3.6" fill="#fff" stroke="${col}" stroke-width="1.5"/>`;
    else svg += `<circle cx="${cx.toFixed(2)}" cy="${cy.toFixed(2)}" r="3.6" fill="${col}"/>`;
    const txt = p.label !== undefined ? p.label : (p.showCoord !== undefined ? p.showCoord : null);
    if(txt !== null){
      const dx = p.labelDx != null ? p.labelDx : 7, dy = p.labelDy != null ? p.labelDy : -7;
      svg += lbl(txt, cx + dx, cy + dy, p.labelFs || 13, col, p.labelAnchor || 'start');
    }
  });

  return svg + '</svg>';
}


// renderer: conic-ellipse-hyperbola (วงรี + ไฮเพอร์โบลาแกนตั้ง ศูนย์กลางร่วม)
function renderConicEllipseHyperbola(spec){
  const W=spec.width||320, H=spec.height||300, pad=20;
  const xR=spec.xRange||[-8,4], yR=spec.yRange||[-5,7];
  const xM=xR[0],xX=xR[1],yM=yR[0],yX=yR[1];
  const pW=W-2*pad, pH=H-2*pad;
  const s=Math.min(pW/(xX-xM), pH/(yX-yM));        // px/หน่วย เท่ากันสองแกน (ไม่บิด)
  const offX=pad+(pW-(xX-xM)*s)/2, offY=pad+(pH-(yX-yM)*s)/2;
  const X=x=>offX+(x-xM)*s, Y=y=>offY+(yX-y)*s;    // flip y
  const c=spec.center||[0,0], cx=c[0], cy=c[1];
  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  svg+=`<defs><marker id="cax" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#888"/></marker></defs>`;
  // axes
  svg+=`<line x1="${X(xM).toFixed(1)}" y1="${Y(0).toFixed(1)}" x2="${X(xX).toFixed(1)}" y2="${Y(0).toFixed(1)}" stroke="#aaa" stroke-width="1" marker-end="url(#cax)"/>`;
  svg+=`<line x1="${X(0).toFixed(1)}" y1="${Y(yM).toFixed(1)}" x2="${X(0).toFixed(1)}" y2="${Y(yX).toFixed(1)}" stroke="#aaa" stroke-width="1" marker-end="url(#cax)"/>`;
  // asymptotes (dashed) — vertical: slope ±A/B · horizontal: slope ±B/A
  const hy=spec.hyperbola;
  const horiz = hy && hy.orientation==='horizontal';
  if(hy && spec.showAsymptotes!==false){
    const m = horiz ? hy.B/hy.A : hy.A/hy.B;
    [m,-m].forEach(slope=>{
      const x1=xM, y1=cy+slope*(xM-cx), x2=xX, y2=cy+slope*(xX-cx);
      svg+=`<line x1="${X(x1).toFixed(1)}" y1="${Y(y1).toFixed(1)}" x2="${X(x2).toFixed(1)}" y2="${Y(y2).toFixed(1)}" stroke="#bbb" stroke-width="1" stroke-dasharray="5 4"/>`;
    });
  }
  // ellipse
  const el=spec.ellipse;
  if(el){
    svg+=`<ellipse cx="${X(cx).toFixed(1)}" cy="${Y(cy).toFixed(1)}" rx="${(el.b*s).toFixed(1)}" ry="${(el.a*s).toFixed(1)}" fill="none" stroke="#2e6fb0" stroke-width="1.8"/>`;
  }
  // hyperbola — vertical: y=cy±A√(1+(x-cx)²/B²) · horizontal: x=cx±A√(1+(y-cy)²/B²)
  if(hy){
    const N=120;
    if(horiz){
      ['rt','lf'].forEach(br=>{
        let pts=[];
        for(let k=0;k<=N;k++){
          const y=yM+(yX-yM)*k/N, t=1+Math.pow(y-cy,2)/(hy.B*hy.B);
          const x=(br==='rt'?cx+hy.A*Math.sqrt(t):cx-hy.A*Math.sqrt(t));
          if(x>=xM-1 && x<=xX+1) pts.push([X(x),Y(y)]);
        }
        if(pts.length>1) svg+=`<polyline points="${pts.map(p=>p[0].toFixed(1)+','+p[1].toFixed(1)).join(' ')}" fill="none" stroke="#c0392b" stroke-width="1.9"/>`;
      });
    } else {
      ['up','dn'].forEach(br=>{
        let pts=[];
        for(let k=0;k<=N;k++){
          const x=xM+(xX-xM)*k/N, t=1+Math.pow(x-cx,2)/(hy.B*hy.B);
          const y=(br==='up'?cy+hy.A*Math.sqrt(t):cy-hy.A*Math.sqrt(t));
          if(y>=yM-1 && y<=yX+1) pts.push([X(x),Y(y)]);
        }
        if(pts.length>1) svg+=`<polyline points="${pts.map(p=>p[0].toFixed(1)+','+p[1].toFixed(1)).join(' ')}" fill="none" stroke="#c0392b" stroke-width="1.9"/>`;
      });
    }
  }
  // dots (foci/vertices + marked points) with plain labels
  (spec.dots||[]).forEach(d=>{
    svg+=`<circle cx="${X(d.x).toFixed(1)}" cy="${Y(d.y).toFixed(1)}" r="3.2" fill="${d.color||'#222'}"/>`;
    if(d.label){const dx=d.labelDx!==undefined?d.labelDx:6, dy=d.labelDy!==undefined?d.labelDy:-6;
      const lx=X(d.x)+dx, ly=Y(d.y)+dy, fs=11;
      if(/\\sqrt|\$/.test(d.label) && typeof _ucMathToSvg==='function'){
        // estimate width for anchor (mirror _ucMathToSvg chW)
        const inner=d.label.replace(/\\sqrt\s*\{([^}]*)\}/g,'√$1').replace(/[\${}]/g,'').replace(/\\[a-zA-Z]+/g,'');
        let w=0; for(const ch of inner){ w += (ch===','||ch===' ')?fs*0.3:((ch==='('||ch===')')?fs*0.4:(ch==='√'?fs*0.7:fs*0.55)); }
        const sx=(d.anchor==='end')?lx-w:((d.anchor==='middle')?lx-w/2:lx);
        svg+=_ucMathToSvg(d.label, sx, ly, fs, d.color||'#222');
      } else {
        svg+=`<text x="${lx.toFixed(1)}" y="${ly.toFixed(1)}" font-size="${fs}" fill="${d.color||'#222'}" text-anchor="${d.anchor||'start'}">${d.label}</text>`;
      }}
  });
  // plain annotations
  (spec.annotations||[]).forEach(a=>{
    svg+=`<text x="${X(a.at[0]).toFixed(1)}" y="${Y(a.at[1]).toFixed(1)}" font-size="${a.fontSize||11}" fill="${a.color||'#222'}" text-anchor="${a.anchor||'start'}">${a.text}</text>`;
  });
  return svg+'</svg>';
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
    case 'argand-plane':
      return renderArgandPlane(spec);
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
    case '3set-labeled':
      return render3SetLabeled(spec);
    case 'venn-c-in-a':
      return venn3CinA(spec);
    case 'venn-c-oval':
      return venn3COval(spec);
    case 'venn-c-in-a-only':
      return venn3CinAOnly(spec);
    case 'number-line':
      return renderNumberLine(spec);
    case 'disk-shading':
      return renderDiskShading(spec);
    case 'intersecting-circles':
      return renderIntersectingCircles(spec);
    case 'circle-segment':
      return renderCircleSegment(spec);
    case 'triangle-sector-cut':
      return renderTriangleSectorCut(spec);
    case 'pyramid-square':
      return renderPyramidSquare(spec);
    case 'tower-two-observers':
      return renderTowerTwoObservers(spec);
    case 'roads-tangent-arc':
      return renderRoadsTangentArc(spec);
    case 'mirror-reflect-buildings':
      return renderMirrorReflectBuildings(spec);
    case 'box-space-diagonal':
      return renderBoxSpaceDiagonal(spec);
    case 'roads-curve-survey':
      return renderRoadsCurveSurvey(spec);
    case 'quarter-circle-inscribed-rect':
      return renderQuarterCircleInscribedRect(spec);
    // portal convergence (§3): portal เรียกชื่อ type 3set-* → map ไป function เดิม
    //   geometry เดียวกับ venn-c-oval / venn-c-in-a+shade (verify แล้วผ่าน Q33/Q36 chap-01-set)
    case '3set-c-in-aub':
      return venn3COval(Object.assign({}, spec, {type:'venn-c-oval'}));
    case '3set-c-in-a-shade-ab-minus-c':
      return venn3CinA(Object.assign({}, spec, {type:'venn-c-in-a', shade: spec.shade || ['AB']}));
    case 'sampled-curve-with-gaps':
      return renderSampledCurveGaps(spec);
    case 'path-with-vertical-angles':
      return renderPathVerticalAngles(spec);
    case 'nested-midpoint-squares':
      return renderNestedMidpointSquares(spec);
    case 'nested-circle-square':
      return renderNestedCircleSquare(spec);
    case 'feasible-region':
      return renderFeasibleRegion(spec);
    case 'box-plot':
      return renderBoxPlot(spec);
    case 'matchstick-staircase':
      return renderMatchstickStaircase(spec);
    case 'conic-ellipse-hyperbola':
      return renderConicEllipseHyperbola(spec);
    case 'circle-on-plane':
      return renderCircleOnPlane(spec);
    case 'l-shape-grid':
      return renderLShapeGrid(spec);
    default:
      return null; // unknown type → admin.html จะ fallback ไปแสดง placeholder
  }
}


// ----- renderer: sampled-curve-with-gaps -----
// Plots one or more pre-sampled polyline segments (data coords) on labeled axes,
// leaving gaps between segments (e.g. y = √(cos 2x) half-wave bumps over its domain).
// Curve points are pre-sampled by the author (no eval); renderer only maps data→px.
// Spec fields:
//   width, height
//   xRange:[xmin,xmax], yRange:[ymin,ymax]              (data coords)
//   segments: [ [[x,y],...], ... ]                       each = one continuous polyline
//   xTicks: [ {x, num?,den?,neg?} | {x,text} | {x,latex} (√ via _ucMathToSvg) ]
//   yTicks: [ {y, text} | {y,num,den,neg} ]   (label placed left of y-axis)
//   axisLabels: {x:'x', y:'y'}                            (at axis arrow tips)
//   curveColor (default '#222'), curveWidth (default 1.8)
//   pad:{l,r,t,b}                                         optional px margins
function renderSampledCurveGaps(spec){
  const W = spec.width || 520, H = spec.height || 210;
  const xr = spec.xRange || [-1, 1], yr = spec.yRange || [0, 1];
  const pad = spec.pad || {};
  const pL = (pad.l != null) ? pad.l : 30;
  const pR = (pad.r != null) ? pad.r : 26;
  const pT = (pad.t != null) ? pad.t : 18;
  const pB = (pad.b != null) ? pad.b : 36;
  const X = v => pL + (v - xr[0]) / (xr[1] - xr[0]) * (W - pL - pR);
  const Y = v => (H - pB) - (v - yr[0]) / (yr[1] - yr[0]) * (H - pT - pB);
  const col = spec.curveColor || '#222';
  const cw  = spec.curveWidth || 1.8;
  const ff  = "'Cambria Math','Times New Roman',serif";

  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  svg += `<defs><marker id="scg-arrow" viewBox="0 0 10 10" refX="8" refY="5" `
       + `markerWidth="7" markerHeight="7" orient="auto-start-reverse">`
       + `<path d="M0 0 L10 5 L0 10 z" fill="#222"/></marker></defs>`;

  const x0 = X(0), y0 = Y(0);

  // axes: x-axis at data y=0 (arrow →), y-axis at data x=0 (arrow ↑)
  svg += `<line x1="${(pL - 6).toFixed(2)}" y1="${y0.toFixed(2)}" `
       + `x2="${(W - pR + 8).toFixed(2)}" y2="${y0.toFixed(2)}" `
       + `stroke="#222" stroke-width="1.4" marker-end="url(#scg-arrow)"/>`;
  svg += `<line x1="${x0.toFixed(2)}" y1="${(H - pB + 2).toFixed(2)}" `
       + `x2="${x0.toFixed(2)}" y2="${(pT - 2).toFixed(2)}" `
       + `stroke="#222" stroke-width="1.4" marker-end="url(#scg-arrow)"/>`;

  // axis labels at arrow tips
  const al = spec.axisLabels || {};
  if (al.x) svg += `<text x="${(W - pR + 11).toFixed(2)}" y="${(y0 + 5).toFixed(2)}" `
                 + `font-family="${ff}" font-size="15" font-style="italic" fill="#222">${al.x}</text>`;
  if (al.y) svg += `<text x="${(x0 + 7).toFixed(2)}" y="${(pT + 3).toFixed(2)}" `
                 + `font-family="${ff}" font-size="15" font-style="italic" fill="#222">${al.y}</text>`;

  // curve segments (gaps = separate paths)
  (spec.segments || []).forEach(seg => {
    if (!seg || seg.length < 2) return;
    const d = 'M ' + seg.map(p => `${X(p[0]).toFixed(2)} ${Y(p[1]).toFixed(2)}`).join(' L ');
    svg += `<path d="${d}" fill="none" stroke="${col}" stroke-width="${cw}" `
         + `stroke-linejoin="round" stroke-linecap="round"/>`;
  });

  // stacked-fraction label, centered at xp, top of numerator at topY
  const fracLabel = (xp, topY, num, den, neg) => {
    const fs = 12;
    const numStr = String(num), denStr = String(den);
    const halfW = Math.max(numStr.length, denStr.length) * fs * 0.30 + 1;
    const barY = topY + fs + 1;
    if (neg) svg += `<text x="${(xp - halfW - 4).toFixed(2)}" y="${(barY + 4).toFixed(2)}" `
                  + `text-anchor="middle" font-family="${ff}" font-size="${fs}" fill="#222">\u2212</text>`;
    svg += `<text x="${xp.toFixed(2)}" y="${(barY - 3).toFixed(2)}" text-anchor="middle" `
         + `font-family="${ff}" font-size="${fs}" fill="#222">${numStr}</text>`;
    svg += `<line x1="${(xp - halfW).toFixed(2)}" y1="${barY.toFixed(2)}" `
         + `x2="${(xp + halfW).toFixed(2)}" y2="${barY.toFixed(2)}" stroke="#222" stroke-width="1"/>`;
    svg += `<text x="${xp.toFixed(2)}" y="${(barY + 12).toFixed(2)}" text-anchor="middle" `
         + `font-family="${ff}" font-size="${fs}" fill="#222">${denStr}</text>`;
  };

  // x ticks + labels (below axis)
  (spec.xTicks || []).forEach(t => {
    const xp = X(t.x);
    svg += `<line x1="${xp.toFixed(2)}" y1="${(y0 - 4).toFixed(2)}" `
         + `x2="${xp.toFixed(2)}" y2="${(y0 + 4).toFixed(2)}" stroke="#222" stroke-width="1"/>`;
    const topY = y0 + 8;
    if (t.num !== undefined && t.den !== undefined) {
      fracLabel(xp, topY, t.num, t.den, t.neg);
    } else if (t.latex !== undefined) {
      const fs = 12, w = _nlLatexW(t.latex, fs);
      svg += _ucMathToSvg(t.latex, xp - w / 2, topY + fs + 2, fs);
    } else if (t.text !== undefined) {
      svg += `<text x="${xp.toFixed(2)}" y="${(topY + 12).toFixed(2)}" text-anchor="middle" `
           + `font-family="${ff}" font-size="12" fill="#222">${t.text}</text>`;
    }
  });

  // y ticks + labels (left of y-axis)
  (spec.yTicks || []).forEach(t => {
    const yp = Y(t.y);
    svg += `<line x1="${(x0 - 4).toFixed(2)}" y1="${yp.toFixed(2)}" `
         + `x2="${(x0 + 4).toFixed(2)}" y2="${yp.toFixed(2)}" stroke="#222" stroke-width="1"/>`;
    const tx = x0 - 8;
    if (t.text !== undefined) {
      svg += `<text x="${tx.toFixed(2)}" y="${(yp + 4).toFixed(2)}" text-anchor="end" `
           + `font-family="${ff}" font-size="13" fill="#222">${t.text}</text>`;
    }
  });

  return svg + '</svg>';
}


// ----- renderer: path-with-vertical-angles -----
// Draws a connected path (rods laid end-to-end) with a dashed VERTICAL reference ray
// (arrowhead up) at chosen vertices, and an angle arc between that vertical and the
// outgoing rod — e.g. q71: rods a,b,c each making angle A,B,C with the vertical.
// All coordinates are pixel coords (author lays out geometry; renderer only draws).
// Spec fields:
//   width, height
//   points: [[x,y],...]                          path vertices P..Q (px)
//   pointLabels: [ {text,dx?,dy?} | null, ... ]  optional label per point
//   dotIndices: [..]                             filled dots (default: all points)
//   segLabels: [ {text,dx?,dy?} | null, ... ]    label per segment (len = points-1)
//   verticalLen: px (default 48)                 length of dashed vertical-up ray
//   verticals: [idx,...]                         points that get a dashed vertical (default: all but last)
//   arrowOnVertical: bool (default true)
//   angles: [ {at:idx, to:idx2, radius?, label, labelDx?, labelDy?} ]  arc vertical-up → toward point idx2
//   color (default '#222'), lineWidth (default 1.7)
function renderPathVerticalAngles(spec){
  const W = spec.width || 400, H = spec.height || 230;
  const pts = spec.points || [];
  const col = spec.color || '#222';
  const lw  = spec.lineWidth || 1.7;
  const ff  = "'Cambria Math','Times New Roman',serif";
  const vLen = (spec.verticalLen != null) ? spec.verticalLen : 48;
  const arrowV = (spec.arrowOnVertical !== false);
  const dotSet = spec.dotIndices ? new Set(spec.dotIndices) : null;

  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  svg += `<defs><marker id="pva-arrow" viewBox="0 0 10 10" refX="8" refY="5" `
       + `markerWidth="7" markerHeight="7" orient="auto-start-reverse">`
       + `<path d="M0 0 L10 5 L0 10 z" fill="${col}"/></marker></defs>`;

  const unit = (p1, p2) => {
    const dx = p2[0]-p1[0], dy = p2[1]-p1[1];
    const L = Math.sqrt(dx*dx+dy*dy) || 1;
    return [dx/L, dy/L];
  };

  // 1) dashed vertical reference rays (upward), bottom layer
  const vertIdx = spec.verticals || pts.map((_,i)=>i).slice(0, Math.max(0, pts.length-1));
  vertIdx.forEach(i => {
    const p = pts[i]; if(!p) return;
    const topY = p[1] - vLen;
    svg += `<line x1="${p[0].toFixed(2)}" y1="${(p[1]+6).toFixed(2)}" `
         + `x2="${p[0].toFixed(2)}" y2="${topY.toFixed(2)}" `
         + `stroke="${col}" stroke-width="1" stroke-dasharray="4 3"`
         + `${arrowV ? ' marker-end="url(#pva-arrow)"' : ''}/>`;
  });

  // 2) path segments (rods)
  for(let i=0; i<pts.length-1; i++){
    const a = pts[i], b = pts[i+1];
    svg += `<line x1="${a[0].toFixed(2)}" y1="${a[1].toFixed(2)}" `
         + `x2="${b[0].toFixed(2)}" y2="${b[1].toFixed(2)}" `
         + `stroke="${col}" stroke-width="${lw}"/>`;
  }

  // 3) angle arcs (vertical-up → rod toward point idx2)
  (spec.angles || []).forEach(an => {
    const center = pts[an.at]; const target = pts[an.to];
    if(!center || !target) return;
    const r = an.radius || 20;
    const uUp = [0, -1];                 // vertical up
    const uTo = unit(center, target);    // toward rod end
    const start = [center[0] + r*uUp[0], center[1] + r*uUp[1]];
    const end   = [center[0] + r*uTo[0], center[1] + r*uTo[1]];
    const cross = uUp[0]*uTo[1] - uUp[1]*uTo[0];   // y-down screen
    const sweep = (cross > 0) ? 1 : 0;
    svg += `<path d="M ${start[0].toFixed(2)} ${start[1].toFixed(2)} `
         + `A ${r} ${r} 0 0 ${sweep} ${end[0].toFixed(2)} ${end[1].toFixed(2)}" `
         + `fill="none" stroke="${col}" stroke-width="1"/>`;
    if(an.label){
      let bx = uUp[0]+uTo[0], by = uUp[1]+uTo[1];
      const bl = Math.sqrt(bx*bx+by*by) || 1; bx/=bl; by/=bl;
      const d = (r + 13);
      const lx = center[0] + d*bx + (an.labelDx||0);
      const ly = center[1] + d*by + (an.labelDy||0);
      svg += `<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" `
           + `font-family="${ff}" font-size="14" font-style="italic" fill="${col}" `
           + `text-anchor="middle" dominant-baseline="central">${an.label}</text>`;
    }
  });

  // 4) segment labels
  (spec.segLabels || []).forEach((s,i) => {
    if(!s || s.text===undefined) return;
    const a = pts[i], b = pts[i+1]; if(!a||!b) return;
    const mx = (a[0]+b[0])/2 + (s.dx||0);
    const my = (a[1]+b[1])/2 + (s.dy||0);
    svg += `<text x="${mx.toFixed(2)}" y="${my.toFixed(2)}" `
         + `font-family="${ff}" font-size="14" font-style="italic" fill="${col}" `
         + `text-anchor="middle" dominant-baseline="central">${s.text}</text>`;
  });

  // 5) dots
  pts.forEach((p,i) => {
    if(dotSet && !dotSet.has(i)) return;
    svg += `<circle cx="${p[0].toFixed(2)}" cy="${p[1].toFixed(2)}" r="3.2" fill="${col}"/>`;
  });

  // 6) point labels (top layer)
  (spec.pointLabels || []).forEach((pl,i) => {
    if(!pl || pl.text===undefined) return;
    const p = pts[i]; if(!p) return;
    const lx = p[0] + (pl.dx||0), ly = p[1] + (pl.dy||0);
    svg += `<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" `
         + `font-family="${ff}" font-size="15" fill="${col}">${pl.text}</text>`;
  });

  return svg + '</svg>';
}


// ----- helper: _sqMathLabel -----
// Mini math typesetter for SVG labels (used by the nested-square renderers).
// Like _ucMathToSvg but draws \sqrt{...} as ONE connected radical path: the √ check
// sits IN FRONT of the radicand and its top connects to the vinculum bar over it
// (fixes the detached-√ look of _ucMathToSvg at small sizes — local only, no global change).
function _sqMathLabel(latex, x, y, fs, color){
  const expr = latex.replace(/^\$|\$$/g, '');
  const col = color || '#222';
  const ff = "'Cambria Math','Times New Roman',serif";
  let cur = x, out = '';
  const chW = ch => {
    if (ch === ',' || ch === ' ') return fs * 0.30;
    if (ch === '(' || ch === ')') return fs * 0.40;
    if (ch === '−' || ch === '-') return fs * 0.55;
    if (ch === '/') return fs * 0.40;
    return fs * 0.55;
  };
  const emit = (text, italic) => {
    const it = italic ? ' font-style="italic"' : '';
    out += `<text x="${cur.toFixed(2)}" y="${y.toFixed(2)}" font-family="${ff}" `
         + `font-size="${fs}" fill="${col}"${it}>${text}</text>`;
    for (const ch of text) cur += chW(ch);
  };
  let i = 0;
  while (i < expr.length) {
    const m = /^\\sqrt\s*\{([^}]*)\}/.exec(expr.substring(i));
    if (m) {
      const rad = m[1];
      let radW = 0; for (const ch of rad) radW += chW(ch);
      // connected radical: down-tick → valley → peak → horizontal bar over radicand
      const peakY = y - fs * 0.92;
      const x0 = cur;
      const xValley = cur + fs * 0.16;
      const xPeak = cur + fs * 0.34;
      const xBarEnd = xPeak + radW + fs * 0.20;
      out += `<path d="M ${x0.toFixed(2)} ${(y - fs * 0.28).toFixed(2)} `
           + `L ${xValley.toFixed(2)} ${(y + fs * 0.02).toFixed(2)} `
           + `L ${xPeak.toFixed(2)} ${peakY.toFixed(2)} `
           + `L ${xBarEnd.toFixed(2)} ${peakY.toFixed(2)}" `
           + `fill="none" stroke="${col}" stroke-width="1" stroke-linejoin="round"/>`;
      cur = xPeak + fs * 0.08;          // radicand starts just after the peak
      emit(rad, false);
      cur += fs * 0.10;
      i += m[0].length;
      continue;
    }
    if (expr.substr(i, 2) === '\\ ') { cur += fs * 0.3; i += 2; continue; }
    if (expr.substr(i, 2) === '\\,') { cur += fs * 0.2; i += 2; continue; }
    if (expr[i] === '-') { emit('−', false); i += 1; continue; }
    const isLetter = /[a-zA-Z]/.test(expr[i]);
    let end = i;
    while (end < expr.length && expr[end] !== '\\' && expr[end] !== '-'
           && (/[a-zA-Z]/.test(expr[end]) === isLetter)) end++;
    emit(expr.substring(i, end), isLetter);
    i = end;
  }
  return out;
}


// ----- renderer: nested-midpoint-squares (Q68) -----
// Outer axis-aligned square (side label `a`); each inner square's corners sit at the
// MIDPOINTS of the previous square's sides → rotates 45° and shrinks by 1/√2 each step.
// Pure geometric construction (vertices = midpoints of previous layer) — self-consistent.
// Spec fields:
//   size        canvas px (default 280, square)
//   margin      px gap from edge to outer square (default 38)
//   layers      number of squares to draw (default 5)
//   sideLabel   latex on outer bottom side (e.g. 'a')  [via _ucMathToSvg]
//   innerLabel  latex near layer-1 edge (e.g. '\\dfrac{a}{\\sqrt{2}}' ⇒ pass 'a/\\sqrt{2}')  optional
//   showMidDots dots at the midpoints of the outer square (default true)
//   colors      stroke palette per layer (optional)
function renderNestedMidpointSquares(spec){
  const S = spec.size || 280;
  const cx = S / 2, cy = S / 2;
  const margin = (spec.margin != null) ? spec.margin : 38;
  const half = (S / 2) - margin;            // half-side of outer square
  const layers = spec.layers || 5;
  const palette = spec.colors ||
    ['#1565c0', '#d35400', '#2e7d32', '#6a1b9a', '#c62828', '#00838f'];

  let svg = `<svg viewBox="0 0 ${S} ${S}" width="${S}" height="${S}" `
          + `xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;

  // layer 0 = axis-aligned outer square; layer k+1 = midpoints of layer k sides
  let verts = [[cx - half, cy - half], [cx + half, cy - half],
               [cx + half, cy + half], [cx - half, cy + half]];
  const allLayers = [];
  for (let k = 0; k < layers; k++) {
    allLayers.push(verts);
    verts = verts.map((v, i) => {
      const w = verts[(i + 1) % 4];
      return [(v[0] + w[0]) / 2, (v[1] + w[1]) / 2];
    });
  }

  // draw squares: outer thickest → inner thinner
  allLayers.forEach((vs, k) => {
    const col = palette[k % palette.length];
    const sw = Math.max(1.1, 2.2 - k * 0.3);
    const pts = vs.map(p => `${p[0].toFixed(2)},${p[1].toFixed(2)}`).join(' ');
    svg += `<polygon points="${pts}" fill="none" stroke="${col}" stroke-width="${sw}"/>`;
  });

  // dots at midpoints of outer square (= vertices of layer 1) → "มุมที่จุดกึ่งกลางด้าน"
  if (spec.showMidDots !== false && allLayers.length > 1) {
    allLayers[1].forEach(p => {
      svg += `<circle cx="${p[0].toFixed(2)}" cy="${p[1].toFixed(2)}" `
           + `r="3" fill="${palette[0]}"/>`;
    });
  }

  // outer side label `a` below bottom-center
  if (spec.sideLabel) {
    const fs = 16;
    const w = _nlLatexW(spec.sideLabel, fs);
    svg += _sqMathLabel(spec.sideLabel, cx - w / 2, cy + half + 20, fs, '#222');
  }

  // optional inner label near layer-1 top-right edge midpoint (outward)
  if (spec.innerLabel && allLayers.length > 1) {
    const fs = 13;
    const lx = cx + half / 2, ly = cy - half / 2;      // midpoint of layer-1 top-right edge
    svg += _sqMathLabel(spec.innerLabel, lx + 6, ly - 6, fs, palette[1]);
  }

  return svg + '</svg>';
}


// ----- renderer: nested-circle-square (Q69) -----
// Concentric alternating figure: circle C1 (diameter d) ⊃ inscribed square ⊃ inscribed
// circle C2 ⊃ inscribed square ⊃ circle C3 … each step scales by 1/√2.
// Squares axis-aligned, vertices on the enclosing circle; next circle tangent to the
// square's sides. All concentric — circle stays a true circle (single px scale).
// Spec fields:
//   size           canvas px (default 300, square)
//   margin         px gap from edge to C1 (default 26)
//   circles        number of circles C1..Cn to draw (default 3)
//   circleLabels   ['C_1','C_2','C_3'] (base_sub form) drawn at top gap of each circle
//   diameterLabel  latex for the C1 diameter (e.g. 'd'); '' ⇒ no diameter line
//   colors         {circle, square, dim}  stroke colors (optional)
// subscript label: 'C_1' → italic base + lowered, smaller subscript (no Unicode-subscript
// glyph dependency). returns {svg, width}. plain text (no '_') → italic base only.
function _ncsSubLabel(text, x, y, fs, color){
  const ff = "'Cambria Math','Times New Roman',serif";
  const m = /^([A-Za-z]+)_\{?([0-9A-Za-z]+)\}?$/.exec(text);
  if(!m){
    const w = text.length * fs * 0.58;
    return { svg: `<text x="${x.toFixed(2)}" y="${y.toFixed(2)}" font-family="${ff}" `
                + `font-size="${fs}" font-style="italic" fill="${color}">${text}</text>`, width: w };
  }
  const base = m[1], sub = m[2];
  const baseW = base.length * fs * 0.58;
  const subFs = fs * 0.72;
  const subW = sub.length * subFs * 0.58;
  let svg = `<text x="${x.toFixed(2)}" y="${y.toFixed(2)}" font-family="${ff}" `
          + `font-size="${fs}" font-style="italic" fill="${color}">${base}</text>`;
  svg += `<text x="${(x + baseW).toFixed(2)}" y="${(y + fs * 0.28).toFixed(2)}" `
       + `font-family="${ff}" font-size="${subFs.toFixed(1)}" fill="${color}">${sub}</text>`;
  return { svg, width: baseW + subW };
}
function renderNestedCircleSquare(spec){
  const S = spec.size || 300;
  const cx = S / 2, cy = S / 2;
  const margin = (spec.margin != null) ? spec.margin : 26;
  const R0 = (S / 2) - margin;              // radius of C1
  const nC = spec.circles || 3;
  const inv = 1 / Math.sqrt(2);
  const col = spec.colors || {};
  const cCirc = col.circle || '#1565c0';
  const cSq   = col.square || '#d35400';
  const cDim  = col.dim || '#777';

  // radii: R_i = R0 * (1/√2)^i  for i = 0 .. nC-1
  const R = [];
  for (let i = 0; i < nC; i++) R.push(R0 * Math.pow(inv, i));

  let svg = `<svg viewBox="0 0 ${S} ${S}" width="${S}" height="${S}" `
          + `xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  svg += `<defs><marker id="ncs-ar" viewBox="0 0 10 10" refX="8" refY="5" `
       + `markerWidth="7" markerHeight="7" orient="auto-start-reverse">`
       + `<path d="M0 0 L10 5 L0 10 z" fill="${cDim}"/></marker></defs>`;

  // squares inscribed in C_i (i = 0 .. nC-2): half-side = R_i/√2 = R_{i+1}
  for (let i = 0; i < nC - 1; i++) {
    const hs = R[i] * inv;
    svg += `<rect x="${(cx - hs).toFixed(2)}" y="${(cy - hs).toFixed(2)}" `
         + `width="${(2 * hs).toFixed(2)}" height="${(2 * hs).toFixed(2)}" `
         + `fill="none" stroke="${cSq}" stroke-width="1.4"/>`;
  }

  // circles C1..Cn (outer first)
  R.forEach((r, i) => {
    const sw = Math.max(1.2, 2.0 - i * 0.25);
    svg += `<circle cx="${cx}" cy="${cy}" r="${r.toFixed(2)}" `
         + `fill="none" stroke="${cCirc}" stroke-width="${sw}"/>`;
  });

  // diameter line + label d across C1 (dashed, light, arrows both ends)
  if (spec.diameterLabel !== '') {
    const dl = spec.diameterLabel || 'd';
    svg += `<line x1="${(cx - R0).toFixed(2)}" y1="${cy}" `
         + `x2="${(cx + R0).toFixed(2)}" y2="${cy}" stroke="${cDim}" `
         + `stroke-width="1" stroke-dasharray="4 3" `
         + `marker-start="url(#ncs-ar)" marker-end="url(#ncs-ar)"/>`;
    const fs = 15;
    const lx = cx + (R0 + R[1]) / 2;          // right gap between C1 and C2
    svg += _ucMathToSvg(dl, lx - _nlLatexW(dl, fs) / 2, cy - 6, fs, '#222');
  }

  // circle labels at the top gap of each circle (just inside the top arc)
  const labels = spec.circleLabels || [];
  labels.slice(0, nC).forEach((t, i) => {
    if (!t) return;
    const fs = 14;
    const yTop = cy - R[i] + 16;
    const probe = _ncsSubLabel(t, 0, 0, fs, cCirc);   // measure width
    const lab = _ncsSubLabel(t, cx - probe.width / 2, yTop, fs, cCirc);
    svg += lab.svg;
  });

  return svg + '</svg>';
}

// ----- renderer: feasible-region (linear programming) -----
// Spec fields:
//   width,height            - SVG canvas (default 360 x 330)
//   xRange,yRange           - [min,max] data ranges
//   grid                    - bool: faint integer gridlines
//   xTicks,yTicks           - arrays of tick values on each axis
//   axes:{arrows,xLabel,yLabel,originLabel}
//   region:{vertices:[[x,y]...], label:{text,at}}   // frame-clipped polygon (closed)
//   constraints:[{from:[x,y],to:[x,y],dashed?,color?,label:{text,at,anchor}}]
//   corners:[{x,y,label,anchor,dx,dy,optimum?}]      // real vertices (not clipped)
//   objective?:{isoLines:[{from,to}],arrow:{from,to},label:{text,at}}
//   note                    - caption under the figure
function renderFeasibleRegion(spec){
  const W = spec.width || 360, H = spec.height || 330;
  const xr = spec.xRange || [0,10], yr = spec.yRange || [0,10];
  const x0=xr[0], x1=xr[1], y0=yr[0], y1=yr[1];
  const mL=44, mR=18, mT=22, mB=spec.note?52:32;
  const pW=W-mL-mR, pH=H-mT-mB;
  const X = x => mL + (x-x0)/(x1-x0)*pW;
  const Y = y => mT + (1-(y-y0)/(y1-y0))*pH;
  const INK='#222', REG='#7fb3d5', REGE='#3a6ea5', OPT='#c0392b', AX='#555', GRID='#e6ebf1';
  function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
  const f=n=>(+n).toFixed(1);
  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" `
          + `xmlns="http://www.w3.org/2000/svg" `
          + `style="background:#fff;font-family:'Sarabun',sans-serif;">`;
  svg += `<defs>`
       + `<marker id="frAx" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="${AX}"/></marker>`
       + `<marker id="frP" markerWidth="10" markerHeight="10" refX="6.5" refY="3" orient="auto"><path d="M0,0 L7.5,3 L0,6 Z" fill="${OPT}"/></marker>`
       + `</defs>`;

  // --- faint grid ---
  if(spec.grid){
    (spec.xTicks||[]).forEach(t=>{ const px=X(t);
      svg+=`<line x1="${f(px)}" y1="${f(Y(y0))}" x2="${f(px)}" y2="${f(Y(y1))}" stroke="${GRID}" stroke-width="1"/>`; });
    (spec.yTicks||[]).forEach(t=>{ const py=Y(t);
      svg+=`<line x1="${f(X(x0))}" y1="${f(py)}" x2="${f(X(x1))}" y2="${f(py)}" stroke="${GRID}" stroke-width="1"/>`; });
  }

  // --- feasible region polygon ---
  if(spec.region && spec.region.vertices && spec.region.vertices.length>=3){
    const pts = spec.region.vertices.map(p=>`${f(X(p[0]))},${f(Y(p[1]))}`).join(' ');
    svg+=`<polygon points="${pts}" fill="${REG}" fill-opacity="0.42" stroke="${REGE}" stroke-width="1"/>`;
    if(spec.region.label){const L=spec.region.label;
      svg+=`<text x="${f(X(L.at[0]))}" y="${f(Y(L.at[1]))}" font-size="13" fill="#2c5f8a" text-anchor="middle">${esc(L.text)}</text>`; }
  }

  // --- constraint boundary lines ---
  (spec.constraints||[]).forEach(c=>{
    const col=c.color||AX, dash=c.dashed?' stroke-dasharray="5 4"':'', cw=c.width||1.3;
    svg+=`<line x1="${f(X(c.from[0]))}" y1="${f(Y(c.from[1]))}" x2="${f(X(c.to[0]))}" y2="${f(Y(c.to[1]))}" stroke="${col}" stroke-width="${cw}"${dash}/>`;
    if(c.label){const L=c.label;
      svg+=`<text x="${f(X(L.at[0]))}" y="${f(Y(L.at[1]))}" font-size="11" fill="${col}" text-anchor="${L.anchor||'middle'}">${esc(L.text)}</text>`; }
  });

  // --- objective iso-lines + direction arrow ---
  if(spec.objective){
    (spec.objective.isoLines||[]).forEach(l=>{
      svg+=`<line x1="${f(X(l.from[0]))}" y1="${f(Y(l.from[1]))}" x2="${f(X(l.to[0]))}" y2="${f(Y(l.to[1]))}" stroke="${OPT}" stroke-width="1.3" stroke-dasharray="6 4"/>`; });
    if(spec.objective.arrow){const a=spec.objective.arrow;
      svg+=`<line x1="${f(X(a.from[0]))}" y1="${f(Y(a.from[1]))}" x2="${f(X(a.to[0]))}" y2="${f(Y(a.to[1]))}" stroke="${OPT}" stroke-width="1.7" marker-end="url(#frP)"/>`; }
    if(spec.objective.label){const L=spec.objective.label;
      svg+=`<text x="${f(X(L.at[0]))}" y="${f(Y(L.at[1]))}" font-size="11" fill="${OPT}" text-anchor="middle">${esc(L.text)}</text>`; }
  }

  // --- axes (over region, under corners) ---
  svg+=`<line x1="${f(X(x0))}" y1="${f(Y(0))}" x2="${f(X(x1))}" y2="${f(Y(0))}" stroke="${AX}" stroke-width="1.2" marker-end="url(#frAx)"/>`;
  svg+=`<line x1="${f(X(0))}" y1="${f(Y(y0))}" x2="${f(X(0))}" y2="${f(Y(y1))}" stroke="${AX}" stroke-width="1.2" marker-end="url(#frAx)"/>`;
  (spec.xTicks||[]).forEach(t=>{ const px=X(t),py=Y(0);
    svg+=`<line x1="${f(px)}" y1="${f(py-3)}" x2="${f(px)}" y2="${f(py+3)}" stroke="${AX}" stroke-width="1"/>`;
    svg+=`<text x="${f(px)}" y="${f(py+14)}" font-size="10" fill="#444" text-anchor="middle">${esc(t)}</text>`; });
  (spec.yTicks||[]).forEach(t=>{ const px=X(0),py=Y(t);
    svg+=`<line x1="${f(px-3)}" y1="${f(py)}" x2="${f(px+3)}" y2="${f(py)}" stroke="${AX}" stroke-width="1"/>`;
    svg+=`<text x="${f(px-7)}" y="${f(py+3.5)}" font-size="10" fill="#444" text-anchor="end">${esc(t)}</text>`; });
  const ax=spec.axes||{};
  svg+=`<text x="${f(X(0)-9)}" y="${f(Y(0)+14)}" font-size="11" fill="#444" text-anchor="middle">${esc(ax.originLabel||'O')}</text>`;
  if(ax.xLabel) svg+=`<text x="${f(X(x1))}" y="${f(Y(0)+24)}" font-size="11.5" fill="#333" text-anchor="end" font-style="italic">${esc(ax.xLabel)}</text>`;
  if(ax.yLabel) svg+=`<text x="${f(X(0)+8)}" y="${f(Y(y1)-6)}" font-size="11.5" fill="#333" text-anchor="start" font-style="italic">${esc(ax.yLabel)}</text>`;

  // --- corner points + optimum marker ---
  (spec.corners||[]).forEach(c=>{
    const px=X(c.x),py=Y(c.y);
    if(c.optimum){
      svg+=`<circle cx="${f(px)}" cy="${f(py)}" r="5.5" fill="none" stroke="${OPT}" stroke-width="2"/>`;
      svg+=`<circle cx="${f(px)}" cy="${f(py)}" r="2.3" fill="${OPT}"/>`;
    } else {
      svg+=`<circle cx="${f(px)}" cy="${f(py)}" r="2.8" fill="${INK}"/>`;
    }
    if(c.label){
      const anchor=c.anchor||'middle', dx=c.dx||0, dy=c.dy||0;
      const fill=c.optimum?OPT:'#333', wt=c.optimum?' font-weight="bold"':'';
      svg+=`<text x="${f(px+dx)}" y="${f(py+dy)}" font-size="11" fill="${fill}" text-anchor="${anchor}"${wt}>${esc(c.label)}</text>`;
    }
  });

  // --- note ---
  if(spec.note){
    svg+=`<text x="${f(W/2)}" y="${f(H-11)}" font-size="11.5" fill="#555" text-anchor="middle">${esc(spec.note)}</text>`;
  }

  svg+=`</svg>`;
  return svg;
}


// ----- renderer: box-plot (vertical, multi-group) -----
// แผนภาพกล่อง (box-and-whisker) แนวตั้ง หลายกลุ่ม — reusable ทั้ง curriculum สถิติ
// Spec:
//   width,height
//   yRange:[lo,hi]     (default: auto จาก min/max ทุกกลุ่ม + padding 8%)
//   yTicks:[...]       (ป้าย/ขีดแกน Y)
//   yLabel?            (ป้ายแกน Y แนวตั้งด้านซ้าย)
//   boxWidth?          (px ความกว้างกล่อง, default 44)
//   guides?            (เส้นประแนวนอนจากทุกสถิติ → แกน Y; default false)
//   groups:[{label,min,q1,median,q3,max}, ...]
function renderBoxPlot(spec){
  const W=spec.width||300, H=spec.height||280;
  const groups=spec.groups||[];
  function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
  const f=n=>(+n).toFixed(2);
  let yr=spec.yRange;
  if(!yr){
    let lo=Infinity,hi=-Infinity;
    groups.forEach(g=>{lo=Math.min(lo,g.min);hi=Math.max(hi,g.max);});
    const pad=(hi-lo)*0.08||1; yr=[Math.floor(lo-pad),Math.ceil(hi+pad)];
  }
  const y0=yr[0], y1=yr[1];
  const pL=spec.yLabel?52:40, pR=18, pT=18, pB=34;
  const plotW=W-pL-pR, plotH=H-pT-pB;
  const Y=v=>pT+(1-(v-y0)/(y1-y0))*plotH;
  const bw=spec.boxWidth||44;
  const INK='#222', AX='#555', GUIDE='#bbb';
  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:'Sarabun',sans-serif;">`;
  svg+=`<defs><marker id="bpAx" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="${AX}"/></marker></defs>`;
  const axX=pL;
  // Y axis (arrow up)
  svg+=`<line x1="${f(axX)}" y1="${f(H-pB)}" x2="${f(axX)}" y2="${f(pT-6)}" stroke="${AX}" stroke-width="1.1" marker-end="url(#bpAx)"/>`;
  // Y ticks + labels
  (spec.yTicks||[]).forEach(t=>{
    const yp=Y(t);
    svg+=`<line x1="${f(axX-4)}" y1="${f(yp)}" x2="${f(axX)}" y2="${f(yp)}" stroke="${AX}"/>`;
    svg+=`<text x="${f(axX-7)}" y="${f(yp+3.5)}" text-anchor="end" font-size="11" fill="${AX}">${esc(t)}</text>`;
  });
  // Y label (rotated)
  if(spec.yLabel){
    const my=pT+plotH/2;
    svg+=`<text x="15" y="${f(my)}" text-anchor="middle" font-size="11.5" fill="${AX}" transform="rotate(-90 15 ${f(my)})">${esc(spec.yLabel)}</text>`;
  }
  // groups
  const n=groups.length||1;
  groups.forEach((g,k)=>{
    const cx=pL+plotW*(k+0.5)/n;
    const lx=cx-bw/2, rx=cx+bw/2;
    const yq1=Y(g.q1), yq3=Y(g.q3), ymd=Y(g.median), ymin=Y(g.min), ymax=Y(g.max);
    // guides: dashed axis → box left edge for each statistic
    if(spec.guides){
      [g.min,g.q1,g.median,g.q3,g.max].forEach(v=>{
        const yp=Y(v);
        svg+=`<line x1="${f(axX)}" y1="${f(yp)}" x2="${f(lx)}" y2="${f(yp)}" stroke="${GUIDE}" stroke-width="0.8" stroke-dasharray="3,3"/>`;
      });
    }
    // upper whisker + cap
    svg+=`<line x1="${f(cx)}" y1="${f(yq3)}" x2="${f(cx)}" y2="${f(ymax)}" stroke="${INK}" stroke-width="1.2"/>`;
    svg+=`<line x1="${f(cx-bw*0.28)}" y1="${f(ymax)}" x2="${f(cx+bw*0.28)}" y2="${f(ymax)}" stroke="${INK}" stroke-width="1.2"/>`;
    // lower whisker + cap
    svg+=`<line x1="${f(cx)}" y1="${f(yq1)}" x2="${f(cx)}" y2="${f(ymin)}" stroke="${INK}" stroke-width="1.2"/>`;
    svg+=`<line x1="${f(cx-bw*0.28)}" y1="${f(ymin)}" x2="${f(cx+bw*0.28)}" y2="${f(ymin)}" stroke="${INK}" stroke-width="1.2"/>`;
    // box (q1..q3)
    svg+=`<rect x="${f(lx)}" y="${f(yq3)}" width="${f(bw)}" height="${f(yq1-yq3)}" fill="#fff" stroke="${INK}" stroke-width="1.3"/>`;
    // median line
    svg+=`<line x1="${f(lx)}" y1="${f(ymd)}" x2="${f(rx)}" y2="${f(ymd)}" stroke="${INK}" stroke-width="1.6"/>`;
    // group label (below)
    svg+=`<text x="${f(cx)}" y="${f(H-pB+16)}" text-anchor="middle" font-size="12" fill="${INK}">${esc(g.label)}</text>`;
  });
  return svg+'</svg>';
}


// ----- renderer: matchstick-staircase -----
// Draws a sequence of "matchstick staircase" figures in one SVG (multi-panel).
// Each figure n = staircase of unit squares: column k (1-indexed, left→right) has
// height k cells on a shared baseline → total matchsticks = n(n+3) (e.g. 4,10,18,...).
// Every unit edge is drawn once (shared edges de-duplicated) as a matchstick:
// a wood-coloured rounded stroke inset from the grid corners + small head dot.
// Spec fields:
//   width, height            (optional; auto-computed from figures)
//   cell                     (px per unit square, default 30)
//   gap                      (px between panels, default 46)
//   stickColor, headColor    (optional)
//   figures: [ { n:Int, caption:[String,...] }, ... ]   caption lines centred below panel
function renderMatchstickStaircase(spec){
  function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
  const f=n=>(+n).toFixed(2);
  const u=spec.cell||30, gap=spec.gap||46;
  const figs=spec.figures||[];
  const WOOD=spec.stickColor||'#b88a4a', HEAD=spec.headColor||'#9c3327';
  const inset=2.4, sw=3.2, headR=2.6;
  const pL=16, pR=16, pT=14, capTop=12, lineH=16, pB=10;
  let maxN=1, maxCap=0;
  figs.forEach(g=>{maxN=Math.max(maxN,g.n); maxCap=Math.max(maxCap,(g.caption||[]).length);});
  const maxH=maxN*u;
  // panel left offsets
  let cur=pL; const lay=[];
  figs.forEach(g=>{const w=g.n*u; lay.push({left:cur,w}); cur+=w+gap;});
  const totalW=(lay.length? lay[lay.length-1].left+lay[lay.length-1].w : pL)+pR;
  const W=spec.width||totalW;
  const baselineY=pT+maxH;
  const H=spec.height||(baselineY+capTop+maxCap*lineH+pB);
  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:'Sarabun',sans-serif;">`;
  function stick(x1,y1,x2,y2){
    const dx=x2-x1, dy=y2-y1, L=Math.hypot(dx,dy)||1, ux=dx/L, uy=dy/L;
    const ax=x1+ux*inset, ay=y1+uy*inset, bx=x2-ux*inset, by=y2-uy*inset;
    const hx=ax+ux*headR*1.2, hy=ay+uy*headR*1.2;
    return `<line x1="${f(ax)}" y1="${f(ay)}" x2="${f(bx)}" y2="${f(by)}" stroke="${WOOD}" stroke-width="${sw}" stroke-linecap="round"/>`
         + `<circle cx="${f(hx)}" cy="${f(hy)}" r="${headR}" fill="${HEAD}"/>`;
  }
  figs.forEach((g,fi)=>{
    const n=g.n, lo=lay[fi];
    const PX=mx=>lo.left+mx*u;
    const PY=my=>baselineY-my*u;
    const hset=new Set(), vset=new Set();
    for(let i=0;i<n;i++){ const ht=i+1;
      for(let j=0;j<ht;j++){
        hset.add(i+','+j); hset.add(i+','+(j+1));   // bottom & top edges
        vset.add(i+','+j); vset.add((i+1)+','+j);   // left & right edges
      }
    }
    hset.forEach(k=>{const p=k.split(',').map(Number);
      svg+=stick(PX(p[0]),PY(p[1]),PX(p[0]+1),PY(p[1]));});      // head at left
    vset.forEach(k=>{const p=k.split(',').map(Number);
      svg+=stick(PX(p[0]),PY(p[1]),PX(p[0]),PY(p[1]+1));});      // head at bottom
    const cx=lo.left+lo.w/2;
    (g.caption||[]).forEach((line,li)=>{
      svg+=`<text x="${f(cx)}" y="${f(baselineY+capTop+li*lineH+4)}" text-anchor="middle" font-size="12.5" fill="#333">${esc(line)}</text>`;
    });
  });
  return svg+'</svg>';
}

// ============================================================
// circle-on-plane — วงกลม (ศูนย์กลางที่ใดก็ได้) บนระนาบพิกัดจริง
//   รองรับ: แกน X,Y จริง + grid, วงกลมหลายวง (solid/dashed),
//   เส้นตรง (เส้นตัด/สัมผัส), แรเงา half-plane ∩ disk, จุด, รัศมี, ป้าย (LaTeX vinculum)
//   scale เท่ากันทั้งสองแกน → วงกลมกลมเสมอ
// ============================================================
function renderCircleOnPlane(spec){
  const W=spec.width||300, H=spec.height||300, pad=spec.pad||26;
  const xm=spec.xRange[0], xX=spec.xRange[1], ym=spec.yRange[0], yX=spec.yRange[1];
  const pW=W-2*pad, pH=H-2*pad;
  const s=Math.min(pW/(xX-xm), pH/(yX-ym));               // px/หน่วย เท่ากันสองแกน
  const offX=pad+(pW-(xX-xm)*s)/2, offY=pad+(pH-(yX-ym)*s)/2;
  const x2=x=>offX+(x-xm)*s;
  const y2=y=>offY+(yX-y)*s;                              // flip แกน y
  const uid=Math.floor(Math.random()*1e6);
  const SHADE=spec.shadeColor||'#9aa0a6', SHADE_OP=(spec.shadeOpacity!=null)?spec.shadeOpacity:0.4;
  const BIG=(xX-xm+yX-ym)*4;
  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;

  // defs: arrow + clipPath ต่อวงกลม (สำหรับ half-plane shade)
  svg+=`<defs><marker id="copArr_${uid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#333"/></marker>`;
  (spec.circles||[]).forEach((c,i)=>{
    svg+=`<clipPath id="copC_${uid}_${i}"><circle cx="${x2(c.center[0]).toFixed(2)}" cy="${y2(c.center[1]).toFixed(2)}" r="${(c.r*s).toFixed(2)}"/></clipPath>`;
  });
  svg+=`</defs>`;

  // grid (จาง ที่จำนวนเต็ม)
  if(spec.grid){
    svg+=`<g stroke="#e8e8e8" stroke-width="1">`;
    for(let gx=Math.ceil(xm); gx<=Math.floor(xX); gx++) svg+=`<line x1="${x2(gx).toFixed(2)}" y1="${y2(yX).toFixed(2)}" x2="${x2(gx).toFixed(2)}" y2="${y2(ym).toFixed(2)}"/>`;
    for(let gy=Math.ceil(ym); gy<=Math.floor(yX); gy++) svg+=`<line x1="${x2(xm).toFixed(2)}" y1="${y2(gy).toFixed(2)}" x2="${x2(xX).toFixed(2)}" y2="${y2(gy).toFixed(2)}"/>`;
    svg+=`</g>`;
  }

  // แรเงา half-plane ∩ วงกลม (อยู่ล่าง ใต้ขอบวงกลม)
  (spec.shade||[]).forEach(sh=>{
    if(sh.kind==='halfplane'){
      const x1=sh.line[0][0],y1=sh.line[0][1],x2d=sh.line[1][0],y2d=sh.line[1][1];
      const dx=x2d-x1, dy=y2d-y1, L=Math.hypot(dx,dy)||1, ux=dx/L, uy=dy/L;
      let nx=-uy, ny=ux;
      const mx=(x1+x2d)/2, my=(y1+y2d)/2, tx=sh.test[0], ty=sh.test[1];
      if((tx-mx)*nx+(ty-my)*ny<0){nx=-nx;ny=-ny;}
      const A=[x1-ux*BIG,y1-uy*BIG], B=[x2d+ux*BIG,y2d+uy*BIG];
      const C=[B[0]+nx*BIG,B[1]+ny*BIG], D=[A[0]+nx*BIG,A[1]+ny*BIG];
      const pts=[A,B,C,D].map(p=>`${x2(p[0]).toFixed(2)},${y2(p[1]).toFixed(2)}`).join(' ');
      const clip=(sh.clipCircle!=null)?` clip-path="url(#copC_${uid}_${sh.clipCircle})"`:'';
      svg+=`<polygon points="${pts}" fill="${SHADE}" fill-opacity="${SHADE_OP}"${clip}/>`;
    }
  });

  // แกน X,Y จริง (วาดที่ x=0 / y=0 ถ้าอยู่ในช่วง)
  if(spec.axes!==false){
    const ax=spec.axes||{};
    const cyA=y2(0), cxA=x2(0);
    const arr=(ax.arrows!==false)?` marker-end="url(#copArr_${uid})"`:'';
    if(0>=ym&&0<=yX){ svg+=`<line x1="${x2(xm).toFixed(2)}" y1="${cyA.toFixed(2)}" x2="${(x2(xX)+2).toFixed(2)}" y2="${cyA.toFixed(2)}" stroke="#333" stroke-width="1.2"${arr}/>`;
      if(ax.xLabel) svg+=`<text x="${(x2(xX)+5).toFixed(2)}" y="${(cyA+4).toFixed(2)}" font-size="13" fill="#333">${ax.xLabel}</text>`; }
    if(0>=xm&&0<=xX){ svg+=`<line x1="${cxA.toFixed(2)}" y1="${y2(ym).toFixed(2)}" x2="${cxA.toFixed(2)}" y2="${(y2(yX)-2).toFixed(2)}" stroke="#333" stroke-width="1.2"${arr}/>`;
      if(ax.yLabel) svg+=`<text x="${(cxA-4).toFixed(2)}" y="${(y2(yX)-4).toFixed(2)}" font-size="13" fill="#333" text-anchor="end">${ax.yLabel}</text>`; }
    if(ax.originLabel&&0>=ym&&0<=yX&&0>=xm&&0<=xX) svg+=`<text x="${(cxA-5).toFixed(2)}" y="${(cyA+13).toFixed(2)}" font-size="12" fill="#333" text-anchor="end">${ax.originLabel}</text>`;
  }

  // ขีด+เลขแกน
  (spec.ticks||[]).forEach(t=>{
    const isX=t.axis!=='y';
    const px=isX?x2(t.at):x2(0), py=isX?y2(0):y2(t.at);
    svg+=`<line x1="${(px-(isX?0:4)).toFixed(2)}" y1="${(py-(isX?4:0)).toFixed(2)}" x2="${(px+(isX?0:4)).toFixed(2)}" y2="${(py+(isX?4:0)).toFixed(2)}" stroke="#333" stroke-width="1.2"/>`;
    if(t.label!=null){ const lx=isX?px:(px-7), ly=isX?(py+13):(py+4);
      svg+=`<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" font-size="11" fill="#333" text-anchor="${isX?'middle':'end'}">${t.label}</text>`; }
  });

  // วงกลม
  (spec.circles||[]).forEach(c=>{
    const dash=c.dashed?' stroke-dasharray="5 4"':'';
    svg+=`<circle cx="${x2(c.center[0]).toFixed(2)}" cy="${y2(c.center[1]).toFixed(2)}" r="${(c.r*s).toFixed(2)}" fill="none" stroke="${c.color||'#222'}" stroke-width="${c.width||1.6}"${dash}/>`;
  });

  // เส้นตรง (เส้นตัด/สัมผัส)
  (spec.lines||[]).forEach(ln=>{
    const dash=ln.dashed?' stroke-dasharray="6 4"':'';
    svg+=`<line x1="${x2(ln.from[0]).toFixed(2)}" y1="${y2(ln.from[1]).toFixed(2)}" x2="${x2(ln.to[0]).toFixed(2)}" y2="${y2(ln.to[1]).toFixed(2)}" stroke="${ln.color||'#222'}" stroke-width="${ln.width||1.4}"${dash}/>`;
  });

  // รัศมี/เส้นเสริม
  (spec.segments||[]).forEach(sg=>{
    const dash=sg.dashed?' stroke-dasharray="5 4"':'';
    svg+=`<line x1="${x2(sg.from[0]).toFixed(2)}" y1="${y2(sg.from[1]).toFixed(2)}" x2="${x2(sg.to[0]).toFixed(2)}" y2="${y2(sg.to[1]).toFixed(2)}" stroke="${sg.color||'#222'}" stroke-width="${sg.width||1.3}"${dash}/>`;
  });

  // จุด
  (spec.dots||[]).forEach(d=>{
    const dx=x2(d.x).toFixed(2), dy=y2(d.y).toFixed(2);
    if(d.open) svg+=`<circle cx="${dx}" cy="${dy}" r="3" fill="#fff" stroke="${d.color||'#222'}" stroke-width="1.4"/>`;
    else svg+=`<circle cx="${dx}" cy="${dy}" r="3" fill="${d.color||'#222'}"/>`;
  });

  // ป้าย (LaTeX vinculum ผ่าน _polyMathToSvg ถ้ามี \sqrt/$, ไม่งั้น plain — ไทยเรนเดอร์ผ่าน Sarabun portal)
  //   optional: leader:true → เส้นประโยงจุด(at)→ป้าย · color → สีข้อความ (เฉพาะ plain text; math label คงดำ)
  (spec.labels||[]).forEach(l=>{
    const lx=x2(l.at[0])+(l.dx||0), ly=y2(l.at[1])+(l.dy||0), anc=l.anchor||'start', fs=l.fontSize||12;
    const t=(l.text!=null)?l.text:l.latex;
    if(l.leader){const ax=x2(l.at[0]),ay=y2(l.at[1]);
      svg+=`<line x1="${ax.toFixed(2)}" y1="${ay.toFixed(2)}" x2="${lx.toFixed(2)}" y2="${ly.toFixed(2)}" stroke="${l.leaderColor||l.color||'#999'}" stroke-width="0.9" stroke-dasharray="3 2"/>`;}
    if(_polyHasMath(t)) svg+=_polyMathToSvg(t,lx,ly,fs,anc);
    else svg+=`<text x="${lx.toFixed(2)}" y="${ly.toFixed(2)}" font-size="${fs}" fill="${l.color||'#222'}" text-anchor="${anc}">${t}</text>`;
  });

  return svg+'</svg>';
}

// ----- renderer: l-shape-grid -----
// รูปตัว L: คอลัมน์แนวตั้ง N ช่อง (บนลงล่าง) ต่อกับแถวแนวนอน M ช่อง (ซ้ายไปขวา)
// โดยช่องล่างสุดของแนวตั้ง = ช่องซ้ายสุดของแนวนอน (ช่องร่วมมุม, ใส่ cornerLabel)
// spec fields:
//   width, height, cellSize (default 45), x0, y0 (มุมบนซ้ายของคอลัมน์แนวตั้ง)
//   vertCount (default 6), horizCount (default 6) — รวมช่องมุมทั้งคู่
//   cornerLabel (default 'x'), vertLabel, horizLabel (ป้ายไทย — ใช้ plain <text> ไม่ fix font)
function renderLShapeGrid(spec){
  const W=spec.width||480, H=spec.height||340;
  const cell=spec.cellSize||45;
  const vertCount=spec.vertCount||6, horizCount=spec.horizCount||6;
  const x0=(spec.x0!=null)?spec.x0:140, y0=(spec.y0!=null)?spec.y0:40;
  let svg=`<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" xmlns="http://www.w3.org/2000/svg" style="background:#fff;">`;
  // แนวตั้ง (บนลงล่าง)
  for(let i=0;i<vertCount;i++){
    const y=y0+i*cell;
    svg+=`<rect x="${x0}" y="${y}" width="${cell}" height="${cell}" fill="none" stroke="#222" stroke-width="1.3"/>`;
  }
  // แนวนอน (ต่อจากช่องมุม, ไม่วาดซ้ำช่องมุม)
  const cornerY=y0+(vertCount-1)*cell;
  for(let j=1;j<horizCount;j++){
    const x=x0+j*cell;
    svg+=`<rect x="${x}" y="${cornerY}" width="${cell}" height="${cell}" fill="none" stroke="#222" stroke-width="1.3"/>`;
  }
  // ป้ายช่องมุม (ตัวแปรคณิต เช่น x) — เอียงแบบตัวแปร
  const cornerLabel=(spec.cornerLabel!=null)?spec.cornerLabel:'x';
  const cx=x0+cell/2, cy=cornerY+cell/2;
  svg+=`<text x="${cx.toFixed(2)}" y="${(cy+5).toFixed(2)}" font-family="'Cambria Math','Times New Roman',serif" font-style="italic" font-size="16" fill="#222" text-anchor="middle">${cornerLabel}</text>`;
  // ป้ายแนวตั้ง (เหนือคอลัมน์)
  if(spec.vertLabel){
    svg+=`<text x="${(x0+cell/2).toFixed(2)}" y="${(y0-14).toFixed(2)}" font-size="14" fill="#222" text-anchor="middle">${spec.vertLabel}</text>`;
  }
  // ป้ายแนวนอน (ขวาสุดของแถว)
  if(spec.horizLabel){
    svg+=`<text x="${(x0+horizCount*cell+8).toFixed(2)}" y="${(cornerY+cell/2+5).toFixed(2)}" font-size="14" fill="#222" text-anchor="start">${spec.horizLabel}</text>`;
  }
  return svg+'</svg>';
}

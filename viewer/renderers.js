// ============================================================
// renderers.js — SVG renderers สำหรับ imageSpec ใน bank
// ------------------------------------------------------------
// Port จาก portal (HANDOVER_v9.md, byte-identical)
// ใช้กับ viewer/admin.html ของ project math-bank
// อนาคต: portal สื่อการสอนจะ fetch ไฟล์เดียวกันนี้ → สอดคล้องกัน
//
// Coverage ปัจจุบัน:
//   ✅ normal-curve     (Q24 ของ samn-2563-03)
//   ✅ function-plot    (Q22 ของ samn-2562-03 — generic: parabola, piecewise-linear, polynomial)
//   ⏳ ztable-with-curves
//   ⏳ polygon-labeled
//   ⏳ unit-circle-figure
//   ⏳ stacked-bar-100
//   ⏳ 3set-c-in-a-shade-ab-minus-c
//
// renderImage() จะคืน null ถ้า type ยังไม่รองรับ
// → admin.html จะ fallback ไปแสดง placeholder card เดิม
// ============================================================


// ----- helper: standard normal PDF -----
function normalPdf(x){return Math.exp(-x*x/2)/Math.sqrt(2*Math.PI);}


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
    svg+=`<polyline points="${pts.join(' ')}" fill="none" stroke="#222" stroke-width="1.6"/>`;
    if(fn.label){const[lx,ly]=fn.label.at,anc=fn.label.anchor||'start';
      svg+=`<text x="${x2(lx)}" y="${y2(ly)}" font-size="14" font-style="italic" fill="#222" text-anchor="${anc}">${fn.label.text}</text>`;}});
  (spec.annotations||[]).forEach(a=>{const[lx,ly]=a.at,anc=a.anchor||'start';
    svg+=`<text x="${x2(lx)}" y="${y2(ly)}" font-size="13" fill="#222" text-anchor="${anc}">${a.text}</text>`;
    if(a.arrowTo){const[ax,ay]=a.arrowTo;
      svg+=`<line x1="${x2(lx)}" y1="${y2(ly)+5}" x2="${x2(ax)}" y2="${y2(ay)}" stroke="#222" stroke-width="1" marker-end="url(#fpArr)"/>`;}});
  return svg+'</svg>';}


// ----- main entry -----
// Returns: SVG string ที่ใช้ insert ผ่าน innerHTML ได้เลย,
//          หรือ null ถ้า type ไม่รองรับ (caller จะ fallback)
function renderImage(spec){
  if(!spec || !spec.type) return null;
  switch(spec.type){
    case 'normal-curve':
      return renderNormalCurve(spec);
    case 'function-plot':
      return renderFunctionPlot(spec);
    // TODO: case 'ztable-with-curves':           return renderZTable(spec);
    // TODO: case 'polygon-labeled':              return renderPolygonLabeled(spec);
    // TODO: case 'unit-circle-figure':           return renderUnitCircleFigure(spec);
    // TODO: case 'stacked-bar-100':              return renderStackedBar100(spec);
    // TODO: case '3set-c-in-a-shade-ab-minus-c': return venn3CinA_shadeABminusC_13();
    default:
      return null; // unknown type → admin.html จะ fallback ไปแสดง placeholder
  }
}

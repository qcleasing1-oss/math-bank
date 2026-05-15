// ============================================================
// renderers.js — SVG renderers สำหรับ imageSpec ใน bank
// ------------------------------------------------------------
// Port จาก portal (HANDOVER_v9.md, byte-identical)
// ใช้กับ viewer/admin.html ของ project math-bank
// อนาคต: portal สื่อการสอนจะ fetch ไฟล์เดียวกันนี้ → สอดคล้องกัน
//
// Coverage ปัจจุบัน:
//   ✅ normal-curve     (Q24 ของ samn-2563-03)
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


// ----- main entry -----
// Returns: SVG string ที่ใช้ insert ผ่าน innerHTML ได้เลย,
//          หรือ null ถ้า type ไม่รองรับ (caller จะ fallback)
function renderImage(spec){
  if(!spec || !spec.type) return null;
  switch(spec.type){
    case 'normal-curve':
      return renderNormalCurve(spec);
    // TODO: case 'ztable-with-curves':           return renderZTable(spec);
    // TODO: case 'polygon-labeled':              return renderPolygonLabeled(spec);
    // TODO: case 'unit-circle-figure':           return renderUnitCircleFigure(spec);
    // TODO: case 'stacked-bar-100':              return renderStackedBar100(spec);
    // TODO: case '3set-c-in-a-shade-ab-minus-c': return venn3CinA_shadeABminusC_13();
    default:
      return null; // unknown type → admin.html จะ fallback ไปแสดง placeholder
  }
}

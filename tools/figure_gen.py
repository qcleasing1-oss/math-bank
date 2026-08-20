#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""figure_gen.py — วาดรูปประกอบมาตรฐานเป็นไฟล์ SVG (ไม่ต้องพึ่ง AI · แก้ตัวเลขแล้ววาดใหม่ได้ทันที)
ใช้:
  python figure_gen.py unitcircle --angle 150 --out fig.svg
  python figure_gen.py triangle --a 7 --b 7 --angle 60 --labels A,B,C --out fig.svg
  python figure_gen.py polygon-in-circle --sides 6 --r 7 --out fig.svg
  python figure_gen.py numberline --from -3 --to 5 --marks -1,2.5 --out fig.svg
  python figure_gen.py axes --fn "x**2-2" --xmin -3 --xmax 3 --out fig.svg
"""
import math, argparse
def head(w=420,h=320): return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="Segoe UI,Tahoma" font-size="13">'
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('kind',choices=['unitcircle','triangle','polygon-in-circle','numberline','axes'])
    ap.add_argument('--angle',type=float,default=60); ap.add_argument('--a',type=float,default=6)
    ap.add_argument('--b',type=float,default=6); ap.add_argument('--sides',type=int,default=6)
    ap.add_argument('--r',type=float,default=1); ap.add_argument('--labels',default='A,B,C')
    ap.add_argument('--from',dest='x0',type=float,default=-3); ap.add_argument('--to',dest='x1',type=float,default=5)
    ap.add_argument('--marks',default=''); ap.add_argument('--fn',default='x**2')
    ap.add_argument('--xmin',type=float,default=-3); ap.add_argument('--xmax',type=float,default=3)
    ap.add_argument('--out',default='fig.svg')
    k=ap.parse_args(); s=[]
    if k.kind=='unitcircle':
        cx,cy,R=210,160,120; th=math.radians(k.angle); x,y=cx+R*math.cos(th),cy-R*math.sin(th)
        s=[head(),f'<circle cx={cx} cy={cy} r={R} fill="none" stroke="#333"/>',
           f'<line x1={cx-R-18} y1={cy} x2={cx+R+18} y2={cy} stroke="#999"/>',
           f'<line x1={cx} y1={cy-R-18} x2={cx} y2={cy+R+18} stroke="#999"/>',
           f'<line x1={cx} y1={cy} x2={x:.1f} y2={y:.1f} stroke="#b8763e" stroke-width=2/>',
           f'<circle cx={x:.1f} cy={y:.1f} r=4 fill="#b8763e"/>',
           f'<path d="M {cx+34} {cy} A 34 34 0 {1 if k.angle>180 else 0} 0 {cx+34*math.cos(th):.1f} {cy-34*math.sin(th):.1f}" fill="none" stroke="#b8763e"/>',
           f'<text x={cx+42} y={cy-12} fill="#b8763e">{k.angle:g}°</text>',
           f'<text x={x+8:.0f} y={y-8:.0f}>({math.cos(th):.3f}, {math.sin(th):.3f})</text>','</svg>']
    elif k.kind=='triangle':
        L=k.labels.split(','); th=math.radians(k.angle); sc=190/max(k.a,k.b)
        A=(90,250); B=(90+k.a*sc,250); C=(90+k.b*sc*math.cos(th),250-k.b*sc*math.sin(th))
        s=[head(),f'<polygon points="{A[0]:.0f},{A[1]:.0f} {B[0]:.0f},{B[1]:.0f} {C[0]:.0f},{C[1]:.0f}" fill="#fdf6ee" stroke="#333" stroke-width=2/>',
           f'<text x={A[0]-16:.0f} y={A[1]+16:.0f}>{L[0]}</text>',f'<text x={B[0]+6:.0f} y={B[1]+16:.0f}>{L[1] if len(L)>1 else "B"}</text>',
           f'<text x={C[0]-4:.0f} y={C[1]-8:.0f}>{L[2] if len(L)>2 else "C"}</text>',
           f'<text x={(A[0]+B[0])/2:.0f} y={A[1]+20:.0f} fill="#b8763e">{k.a:g}</text>',
           f'<text x={(A[0]+C[0])/2-24:.0f} y={(A[1]+C[1])/2:.0f} fill="#b8763e">{k.b:g}</text>',
           f'<path d="M {A[0]+30} {A[1]} A 30 30 0 0 0 {A[0]+30*math.cos(th):.1f} {A[1]-30*math.sin(th):.1f}" fill="none" stroke="#b8763e"/>',
           f'<text x={A[0]+36:.0f} y={A[1]-10:.0f} fill="#b8763e">{k.angle:g}°</text>','</svg>']
    elif k.kind=='polygon-in-circle':
        cx,cy,R=210,160,120
        pts=' '.join(f'{cx+R*math.cos(2*math.pi*i/k.sides-math.pi/2):.1f},{cy+R*math.sin(2*math.pi*i/k.sides-math.pi/2):.1f}' for i in range(k.sides))
        s=[head(),f'<circle cx={cx} cy={cy} r={R} fill="#eef4fb" stroke="#333"/>',
           f'<polygon points="{pts}" fill="#fff" stroke="#b8763e" stroke-width=2/>',
           f'<line x1={cx} y1={cy} x2={cx+R} y2={cy} stroke="#999" stroke-dasharray="4 3"/>',
           f'<text x={cx+R/2-8:.0f} y={cy-6}>r = {k.r:g}</text>',
           f'<text x=14 y=24 fill="#555">{k.sides} เหลี่ยมด้านเท่าในวงกลม · พื้นที่แรเงา = วงกลม − {k.sides} เหลี่ยม</text>','</svg>']
    elif k.kind=='numberline':
        w=440; y=90; x0,x1=k.x0,k.x1; sc=(w-80)/max(1e-9,(x1-x0))
        px=lambda v:40+(v-x0)*sc
        s=[head(w,150),f'<line x1=20 y1={y} x2={w-20} y2={y} stroke="#333" stroke-width=2 marker-end=""/>']
        v=math.ceil(x0)
        while v<=x1:
            s.append(f'<line x1={px(v):.1f} y1={y-7} x2={px(v):.1f} y2={y+7} stroke="#333"/>')
            s.append(f'<text x={px(v):.1f} y={y+26} text-anchor="middle">{v:g}</text>'); v+=1
        for m in [x for x in k.marks.split(',') if x.strip()]:
            mv=float(m); s.append(f'<circle cx={px(mv):.1f} cy={y} r=6 fill="#b8763e"/>')
            s.append(f'<text x={px(mv):.1f} y={y-14} text-anchor="middle" fill="#b8763e">{mv:g}</text>')
        s.append('</svg>')
    else:
        w,h=440,320; cx,cy=w/2,h/2; sc=(w-60)/max(1e-9,(k.xmax-k.xmin))
        pts=[]
        for i in range(201):
            x=k.xmin+(k.xmax-k.xmin)*i/200
            try: y=eval(k.fn,{'x':x,'math':math,'__builtins__':{}})
            except Exception: continue
            X=30+(x-k.xmin)*sc; Y=cy-y*sc/2
            if -50<Y<h+50: pts.append(f'{X:.1f},{Y:.1f}')
        s=[head(w,h),f'<line x1=20 y1={cy} x2={w-20} y2={cy} stroke="#999"/>',
           f'<line x1={cx} y1=20 x2={cx} y2={h-20} stroke="#999"/>',
           f'<polyline points="{" ".join(pts)}" fill="none" stroke="#b8763e" stroke-width=2/>',
           f'<text x=14 y=20 fill="#555">y = {k.fn}</text>','</svg>']
    open(k.out,'w',encoding='utf-8').write('\n'.join(s))
    print(f'✅ {k.out} ({k.kind}) — เปิดด้วยเบราว์เซอร์ หรือแทรกในหน้าเว็บ/เอกสารได้เลย')
if __name__=='__main__': main()

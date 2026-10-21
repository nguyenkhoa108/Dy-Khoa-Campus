from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import os
O='/tmp/claude-0/logo/out/'
def text_path(fontfile,s,size,track_em=0.0,x0=0,y0=0):
    f=TTFont(fontfile);gs=f.getGlyphSet();cm=f.getBestCmap();upm=f['head'].unitsPerEm;hm=f['hmtx']
    sc=size/upm;x=x0;d=''
    for ch in s:
        g=cm[ord(ch)];pen=SVGPathPen(gs)
        tp=TransformPen(pen,(sc,0,0,-sc,x,y0));gs[g].draw(tp);d+=pen.getCommands()
        x+=hm[g][0]*sc+track_em*size
    x-=track_em*size
    return d,x-x0
G='#1f4b3a';R='#a4504c'
def icon(c,ox=0,oy=0,s=1):
    t=lambda v:v*s
    return (f'<g transform="translate({ox} {oy}) scale({s})">'
      f'<rect x="18" y="18" width="46" height="46" rx="3" fill="{c}" fill-opacity=".16"/>'
      f'<rect x="12" y="12" width="46" height="46" rx="3" fill="{c}" fill-opacity=".32"/>'
      f'<rect x="6" y="6" width="46" height="46" rx="3" fill="{c}" fill-opacity=".56"/>'
      f'<rect x="0" y="0" width="46" height="46" rx="3" fill="{c}"/></g>')
def save(name,w,h,body):
    open(O+name,'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" width="{w:.0f}" height="{h:.0f}">{body}</svg>')
BL='BVP-Black.ttf';BD='BVP-Bold.ttf'
# icons
save('doc-sau-icon.svg',64,64,icon(G))
save('doc-sau-icon-dark.svg',64,64,icon('#cfe3d6'))
# lockup
def lockup(cicon,cword,ctag):
    d1,w1=text_path(BL,'ĐỌC SÂU',44,-0.02,78,48)   # baseline y=40 ; accents above ~ y=0
    d2,w2=text_path(BD,'LONGFORM',11.5,0.32,80,72)
    W=78+max(w1,w2+2)+2;H=76
    return W,H,icon(cicon,0,8,1)+f'<path d="{d1}" fill="{cword}"/><path d="{d2}" fill="{ctag}"/>'
W,H,b=lockup(G,G,R);save('doc-sau-logo.svg',W,H,b)
W,H,b=lockup('#cfe3d6','#f3efe6','#e7b7a4');save('doc-sau-logo-dark.svg',W,H,b)
# one-color white (for photos/dark overlays)
W,H,b=lockup('#ffffff','#ffffff','#ffffff');save('doc-sau-logo-white.svg',W,H,b)
# watermark pill
d1,w1=text_path(BL,'ĐỌC SÂU',15,-0.01,34,21.5)
d2,w2=text_path(BD,'LONGFORM',7.5,0.26,34+w1+6,22)
PW=34+w1+6+w2+12;PH=32
save('doc-sau-dau-anh.svg',PW,PH,f'<rect width="{PW:.1f}" height="{PH}" rx="5" fill="#faf8f4" fill-opacity=".94"/>'+icon(G,8,5,0.34)+f'<path d="{d1}" fill="{G}"/><path d="{d2}" fill="{R}"/>')
print('ok',W,H,PW)

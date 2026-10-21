import random, math
random.seed(7)
W,H=1200,675
# nodes in BFS-like spread from source at left-center
src=(250,330)
nodes=[(src,0)]
edges=[]
layers=[1,4,9,16,24,30]
prev=[0]
for li,count in enumerate(layers[1:],start=1):
    cur=[]
    for k in range(count):
        r=120*li+random.uniform(-25,25)
        ang=math.radians(-62+124*(k+random.uniform(0.2,0.8))/count)
        x=src[0]+r*math.cos(ang)*1.05; y=src[1]+r*math.sin(ang)*0.82
        if x>W-60 or y<40 or y>H-40: continue
        if x>870 and y>560: continue   # keep logo corner clear
        nodes.append(((x,y),li)); idx=len(nodes)-1; cur.append(idx)
        # connect to 1-2 nearest in previous layer
        pr=sorted(prev,key=lambda j:(nodes[j][0][0]-x)**2+(nodes[j][0][1]-y)**2)
        for j in pr[:1 if random.random()<0.6 else 2]: edges.append((j,idx))
    prev=cur
cut_edge=edges[2]  # one early edge to be "cut"
def pt(i): return nodes[i][0]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W*2}" height="{H*2}">',
'<defs><radialGradient id="bg" cx="25%" cy="48%" r="85%"><stop offset="0" stop-color="#1c3a2e"/><stop offset="1" stop-color="#0c1712"/></radialGradient>',
'<radialGradient id="glow"><stop offset="0" stop-color="#e2574c" stop-opacity=".55"/><stop offset="1" stop-color="#e2574c" stop-opacity="0"/></radialGradient></defs>',
f'<rect width="{W}" height="{H}" fill="url(#bg)"/>']
# faint grid of tiny dots
for gx in range(20,W,30):
    for gy in range(20,H,30):
        svg.append(f'<circle cx="{gx}" cy="{gy}" r="0.8" fill="#ffffff" fill-opacity=".06"/>')
svg.append(f'<circle cx="{src[0]}" cy="{src[1]}" r="150" fill="url(#glow)"/>')
for e in edges:
    (x1,y1),(x2,y2)=pt(e[0]),pt(e[1])
    if e==cut_edge:
        mx,my=(x1+x2)/2,(y1+y2)/2; dx,dy=(x2-x1),(y2-y1); L=math.hypot(dx,dy); ux,uy=dx/L,dy/L
        g=14
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{mx-ux*g}" y2="{my-uy*g}" stroke="#e2574c" stroke-width="2.2" stroke-opacity=".85"/>')
        svg.append(f'<line x1="{mx+ux*g}" y1="{my+uy*g}" x2="{x2}" y2="{y2}" stroke="#e2574c" stroke-width="2.2" stroke-opacity=".35" stroke-dasharray="4 5"/>')
        # cut mark (scissor-like X)
        px,py=-uy,ux
        for s in (-1,1):
            svg.append(f'<line x1="{mx+px*24-ux*12*s}" y1="{my+py*24-uy*12*s}" x2="{mx-px*24+ux*12*s}" y2="{my-py*24+uy*12*s}" stroke="#f3efe6" stroke-width="3.2" stroke-linecap="round"/>')
        continue
    depth=nodes[e[1]][1]
    op=max(.25,.85-depth*0.1)
    svg.append(f'<path d="M{x1:.1f} {y1:.1f} Q{(x1+x2)/2+ (y2-y1)*0.12:.1f} {(y1+y2)/2-(x2-x1)*0.12:.1f} {x2:.1f} {y2:.1f}" fill="none" stroke="#e2574c" stroke-width="{2.2-depth*0.25:.2f}" stroke-opacity="{op:.2f}"/>')
for i,((x,y),d) in enumerate(nodes):
    if i==0:
        svg.append(f'<circle cx="{x}" cy="{y}" r="16" fill="#e2574c"/><circle cx="{x}" cy="{y}" r="26" fill="none" stroke="#e2574c" stroke-opacity=".5" stroke-width="2"/>')
    else:
        r=max(3.2,9-d*1.1)
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#e2574c" fill-opacity="{max(.45,1-d*0.1):.2f}"/>')
# a few "true" mint nodes lagging near source
for (x,y) in [(170,250),(150,410),(205,470),(120,330)]:
    svg.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#cfe3d6"/>')
svg.append('<line x1="150" y1="410" x2="120" y2="330" stroke="#cfe3d6" stroke-opacity=".6" stroke-width="1.6"/><line x1="170" y1="250" x2="120" y2="330" stroke="#cfe3d6" stroke-opacity=".6" stroke-width="1.6"/><line x1="205" y1="470" x2="150" y2="410" stroke="#cfe3d6" stroke-opacity=".6" stroke-width="1.6"/>')
svg.append('</svg>')
open('cover.svg','w').write('\n'.join(svg))
print(len(nodes),len(edges))

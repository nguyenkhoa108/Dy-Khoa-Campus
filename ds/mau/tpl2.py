import re,html
F='/tmp/claude-0/fonts/node_modules/@fontsource/'
md=open('art.md').read()
body=md.split('# Tin giả khoa học lan truyền thế nào, và vì sao gỡ bỏ thôi là chưa đủ?')[1]
main,rest=body.split('**Đôi lời giới thiệu**')
intro_txt,refs=rest.split('**Tài liệu tham khảo** (khối xổ xuống)')
refs=refs.split('**Ghi chú cho người duyệt')[0]
def inl(s):
    s=html.escape(s,quote=False)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'\*([^*]+)\*',r'<em>\1</em>',s)
    return s
blocks=[b.strip() for b in main.strip().split('\n\n') if b.strip() and b.strip()!='---']
FIG={ # chapter index -> after nth paragraph within chapter, figure
 -1:(1,'h1-thi-nghiem-loomba','Hình 1. Thiết kế và kết quả chính của thí nghiệm Loomba và cộng sự (2021).'),
 2:(2,'h2-tin-sai-lan-nhanh-hon','Hình 2. Tin sai và tin đúng trên Twitter, theo Vosoughi và cộng sự (2018).'),
 3:(2,'h3-khao-sat-hoi-hoang-gia-anh','Hình 3. Kết quả khảo sát của Hội Hoàng gia Anh và YouGov (The Royal Society, 2022).'),
 5:(4,'h4-bon-diem-can-thiep','Hình 4. Bốn điểm can thiệp theo NASEM (2025).'),
}
out=[];toc=[];ch=0;sapo=None;pin=0;chap_titles=[];teaser_next=False;cur_ch=0
pending_fig=None
for b in blocks:
    if b.startswith('## '):
        t=b[3:]
        numbered=not(t.startswith('Kết') or t.startswith('Hỏi nhanh'))
        if numbered:
            ch+=1;cur_ch=ch;toc.append((f'ch{ch}',t))
            out.append(f'@@OPEN{ch}@@')
        else:
            cur_ch=None
            out.append(f'<h2 class="plain" id="{"ket" if t.startswith("Kết") else "hoi"}">{inl(t)}</h2>')
        pin=0;chap_titles.append(t);teaser_next=numbered;continue
    if b.startswith('### '): out.append(f'<h3>{inl(b[4:])}</h3>');continue
    if re.match(r'^(- |\d\. )',b):
        tag='ol' if b[0].isdigit() else 'ul'
        items=[re.sub(r'^(- |\d\. )','',l) for l in b.split('\n')]
        if tag=='ol' and 'Sự thật' in b:
            out.append('<figure class="fig"><img src="fig/h5-bon-buoc-dinh-chinh.png" alt=""><figcaption>Hình 6. Cấu trúc bốn bước của <em>Cẩm nang bác bỏ tin sai 2020</em> (Lewandowsky và cộng sự, 2020).</figcaption></figure>')
        out.append(f'<{tag}>'+''.join(f'<li>{inl(i)}</li>' for i in items)+f'</{tag}>');continue
    if sapo is None and b.startswith('**'):
        sapo=inl(b.strip('*'));continue
    if teaser_next:
        m=re.match(r'\*\*(.+?)\*\*(.*)',b,re.S)
        out[-1]=out[-1].replace(f'@@OPEN{cur_ch}@@',f'@@OPEN{cur_ch}|{html.escape(m.group(1)) if m else ""}@@')
        teaser_next=False
        if m and not m.group(2).strip(): continue
        b=m.group(2).strip() if m else b
        out.append(f'<p class="lead">{inl(b)}</p>');pin+=1
    else:
        out.append(f'<p>{inl(b)}</p>');pin+=1
    key=(cur_ch-1) if cur_ch else (-1 if ch==0 else None)
    if key in FIG and FIG[key][0]==pin:
        _,f,cap=FIG[key];out.append(f'<figure class="fig"><img src="fig/{f}.png" alt=""><figcaption>{cap}</figcaption></figure>');FIG.pop(key)
    if 'Tiêm phòng tâm lý' in ''.join(out[-3:]) and 'h6' not in ''.join(out) and 'Roozenbeek và cộng sự, 2022). Theo thông cáo' in b:
        out.append('<figure class="fig"><img src="fig/h6-tiem-phong-tam-ly-youtube.png" alt=""><figcaption>Hình 5. Phễu thử nghiệm thực địa trên YouTube (Roozenbeek và cộng sự, 2022).</figcaption></figure>')
h='\n'.join(out)
# opening paragraphs before ch1 -> first gets dropcap
h=h.replace('<p>','<p class="first">',1)
def opener(m):
    n=int(m.group(1));teaser=m.group(2) or '';t=toc[n-1][1]
    return f'</div><section class="op" id="ch{n}"><div class="op-in"><div class="op-n">{n:02d}</div><div class="op-t"><div class="op-k">CHƯƠNG {n:02d} / 0{len(toc)}</div><h2>{inl(t)}</h2><p>{teaser}</p></div></div></section><div class="col">'
h=re.sub(r'@@OPEN(\d+)\|?([^@]*)@@',opener,h)
pq='</div><blockquote class="band"><p>Đừng chỉ hỏi "làm sao xóa tin sai", mà hãy hỏi "mắt xích nào trong hệ thống mình có thể làm tốt hơn".</p></blockquote><div class="col">'
h=h.replace('<h2 class="plain" id="ket">',pq+'<h2 class="plain" id="ket">',1)
side='<aside class="sn"><b>NASEM</b>Viện Hàn lâm Khoa học, Kỹ thuật và Y học Hoa Kỳ. Báo cáo đồng thuận năm 2025 về tin sai khoa học do một hội đồng chuyên gia biên soạn.</aside>'
h=h.replace('<p class="lead">Đây là định nghĩa',side+'<p class="lead">Đây là định nghĩa',1)
intro=''.join(f'<p>{inl(x.strip())}</p>' for x in intro_txt.strip().split('\n\n') if x.strip() and x.strip()!='---')
refl=''.join(f'<li>{inl(x.strip())}</li>' for x in refs.strip().split('\n\n') if x.strip() and x.strip()!='---')
words=len(re.sub('<[^>]+>',' ',h).split()); mins=round(words/230)
fonts=''.join(f'<link rel="stylesheet" href="{F}{x}.css">' for x in ['newsreader/400','newsreader/400-italic','newsreader/600','newsreader/700','be-vietnam-pro/400','be-vietnam-pro/600','be-vietnam-pro/700','be-vietnam-pro/800','be-vietnam-pro/900'])
LOGOW=open('/tmp/claude-0/logo/out/doc-sau-logo-white.svg').read(); ICONL=open('/tmp/claude-0/logo/out/doc-sau-icon-dark.svg').read()
strip=''.join(f'<a href="#{s}"><b>{i+1:02d}</b><span>{inl(t)}</span></a>' for i,(s,t) in enumerate(toc))
title='Tin giả khoa học lan truyền thế nào, và vì sao gỡ bỏ thôi là chưa đủ?'
css='''
:root{--g:#13241d;--g2:#1f4b3a;--mint:#cfe3d6;--r:#c4554b;--r2:#a4504c;--ink:#1b1d1c;--paper:#f4efe4;--line:#ddd5c5}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:"Be Vietnam Pro",sans-serif;overflow-x:hidden}
a{color:var(--g2);text-underline-offset:3px}
.site{height:56px;background:#fff;display:flex;align-items:center;padding:0 28px;font-size:13px;color:#6f7772;border-bottom:1px solid var(--line)}
.site b{background:#1f4b3a;color:#fff;padding:3px 6px;font-family:Newsreader;margin-right:8px}
/* reading bar */
.rb{position:fixed;top:0;left:0;right:0;height:50px;background:var(--g);color:#f3efe6;display:flex;align-items:center;gap:16px;padding:0 24px;z-index:50;transform:translateY(-100%);transition:transform .3s}
.rb.show{transform:none}
.rb svg{height:22px;width:auto}.rb .lb{font-weight:900;letter-spacing:.06em;font-size:14px}
.rb .cur{font-size:14px;color:#cfd8d2;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex:1}
.rb .left{font-size:13px;color:#e7b7a4;font-weight:700;white-space:nowrap}
.rb .pg{position:absolute;left:0;bottom:0;height:3px;background:var(--r);width:0}
/* hero */
.hero{display:grid;grid-template-columns:minmax(0,46%) 1fr;min-height:min(92vh,820px);background:var(--g)}
.hero .tx{padding:64px 56px 48px;color:#f3efe6;display:flex;flex-direction:column}
.hero .tx svg{height:34px;width:auto;align-self:flex-start}
.hero h1{font-weight:900;font-size:clamp(2.4rem,4.2vw,4.1rem);line-height:1.04;letter-spacing:-.03em;margin:34px 0 26px}
.hero .sp{font-family:Newsreader,serif;font-size:1.28rem;line-height:1.55;color:#d6ddd8;margin:0}
.hero .mt{margin-top:auto;padding-top:34px;display:flex;gap:22px;flex-wrap:wrap;font-size:14px;color:#aebcb4}
.hero .mt b{color:#fff}
.hero .im{background:#0c1712 url(cover.png) 30% center/cover}
.strip{background:#0c1712;display:grid;grid-template-columns:repeat(8,1fr);border-top:1px solid #2a3b33}
.strip a{color:#aebcb4;text-decoration:none;padding:16px 14px;border-right:1px solid #2a3b33;font-size:12.5px;line-height:1.35}
.strip a b{display:block;color:var(--mint);font-size:20px;font-weight:900;margin-bottom:4px}
.strip a:hover{background:#13241d;color:#fff}
/* column */
.col{max-width:680px;margin:0 auto;padding:0 24px;position:relative}
.sapo{font-family:Newsreader,serif;font-size:1.5rem;line-height:1.55;margin:70px 0 40px;padding-left:22px;border-left:5px solid var(--r)}
.col p,.col li{font-family:Newsreader,serif;font-size:1.27rem;line-height:1.8;color:#232725}
.col p{margin:0 0 1.15em}
.col p.first::first-letter{font-family:"Be Vietnam Pro";font-weight:900;float:left;font-size:5rem;line-height:.8;padding:8px 14px 0 0;color:var(--r2)}
.col p.lead{font-size:1.27rem}
.col h3{font-weight:900;font-size:1.35rem;margin:2.2em 0 .7em;letter-spacing:-.01em;text-transform:uppercase;font-size:1rem;letter-spacing:.12em;color:var(--r2)}
.col h2.plain{font-weight:900;font-size:2rem;letter-spacing:-.02em;margin:2.2em 0 .6em;padding-top:26px;border-top:3px solid var(--ink)}
/* chapter opener */
.op{background:var(--g);color:#f3efe6;margin:90px 0 60px;position:relative;overflow:hidden}
.op::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 15% 50%,rgba(196,85,75,.22),transparent 45%)}
.op-in{position:relative;max-width:1180px;margin:0 auto;padding:80px 32px;display:grid;grid-template-columns:330px 1fr;gap:40px;align-items:center;min-height:52vh}
.op-n{font-weight:900;font-size:260px;line-height:.8;color:transparent;-webkit-text-stroke:2px var(--mint);letter-spacing:-.04em}
.op-k{font-size:13px;font-weight:800;letter-spacing:.24em;color:#e7b7a4}
.op h2{font-weight:900;font-size:clamp(2rem,3.6vw,3.2rem);line-height:1.08;letter-spacing:-.025em;margin:14px 0 20px}
.op p{font-family:Newsreader,serif;font-size:1.35rem;line-height:1.5;color:#cfd8d2;margin:0;max-width:640px}
/* figures break out */
.fig{margin:2.4em -150px;}
.fig img{width:100%;display:block;box-shadow:0 12px 34px rgba(19,36,29,.14)}
.fig figcaption{font-size:14px;color:#6f7772;margin-top:10px;padding:0 4px}
/* sidenote */
.sn{position:absolute;right:-290px;width:250px;font-size:14px;line-height:1.55;color:#4a524e;border-top:3px solid var(--r2);padding-top:10px}
.sn b{display:block;font-size:12px;letter-spacing:.14em;color:var(--r2);margin-bottom:4px}
/* band quote */
.band{margin:80px 0;background:var(--r2);color:#fff;padding:90px 32px}
.band p{max-width:960px;margin:0 auto;font-weight:900;font-size:clamp(1.8rem,3.4vw,3rem);line-height:1.18;letter-spacing:-.02em;text-align:center}
/* end */
.end{background:var(--g);color:#e7ebe8;margin-top:80px;padding:70px 24px 90px}
.end .in{max-width:680px;margin:0 auto}
.end .lg svg{height:34px;width:auto}
.end h4{font-size:12px;letter-spacing:.2em;color:#e7b7a4;margin:40px 0 10px}
.end p{font-family:Newsreader,serif;font-size:1.06rem;line-height:1.65;color:#d6ddd8}
.end details{border-top:1px solid #2f4239;border-bottom:1px solid #2f4239;padding:16px 0;margin-top:30px}
.end summary{font-weight:800;cursor:pointer;color:#fff}
.end li{font-size:.86rem;line-height:1.6;color:#c9d2cd;list-style:none;padding-left:2em;text-indent:-2em;word-break:break-word;margin-bottom:8px}
.end ul{padding:0}.end a{color:var(--mint)}
.mk{position:fixed;right:10px;bottom:10px;background:#000;color:#fff;font:700 12px sans-serif;padding:6px 10px;border-radius:4px;z-index:60}
@media(max-width:1180px){.sn{position:static;width:auto;margin:0 0 1.4em}.fig{margin:2em -24px}}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero .im{order:-1;min-height:260px}.hero .tx{padding:34px 22px}.strip{grid-template-columns:repeat(4,1fr)}.strip a span{display:none}
.op-in{grid-template-columns:1fr;min-height:0;padding:56px 22px;gap:6px}.op-n{font-size:120px}.op p{font-size:1.15rem}
.col p,.col li{font-size:1.13rem}.sapo{font-size:1.25rem;margin-top:40px}.band{padding:56px 22px}.rb .cur{display:none}}
'''
js='''<script>(function(){var rb=document.querySelector('.rb'),pg=rb.querySelector('.pg'),cur=rb.querySelector('.cur'),lf=rb.querySelector('.left'),ops=[].slice.call(document.querySelectorAll('.op')),hero=document.querySelector('.hero'),T=MINS;
function f(){var h=document.documentElement,p=h.scrollTop/(h.scrollHeight-h.clientHeight);pg.style.width=(p*100)+'%';rb.classList.toggle('show',hero.getBoundingClientRect().bottom<0);var c=null;ops.forEach(function(o){if(o.getBoundingClientRect().top<120)c=o});cur.textContent=c?('Chương '+c.querySelector('.op-k').textContent.slice(7,9)+' · '+c.querySelector('h2').textContent):'Mở đầu';lf.textContent='Còn khoảng '+Math.max(1,Math.round(T*(1-p)))+' phút'}
addEventListener('scroll',f,{passive:true});f()})();</script>'''.replace('MINS',str(mins))
teaser=re.sub('<[^>]+>','',sapo).split('. ')[0]+'.'
H=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{fonts}<style>{css}</style></head><body>
<div class="rb"><span>{ICONL}</span><span class="lb">ĐỌC SÂU</span><span class="cur"></span><span class="left"></span><span class="pg"></span></div>
<div class="site"><b>DK</b>Dy Khoa Blog (thanh menu giữ nguyên)</div>
<header class="hero"><div class="tx">{LOGOW}<h1>{title}</h1><p class="sp">{teaser}</p><div class="mt"><span>Dy Khoa</span><span><b>{mins} phút</b> đọc</span><span><b>{len(toc)}</b> chương</span><span><b>6</b> hình</span><span><b>9</b> nguồn</span></div></div><div class="im"></div></header>
<nav class="strip">{strip}</nav>
<div class="col"><div class="sapo">{sapo}</div>{h}</div>
<footer class="end"><div class="in"><div class="lg">{LOGOW}</div><h4>HẾT BÀI ĐỌC SÂU</h4><p>Bạn vừa đọc {len(toc)} chương, {mins} phút, dựa trên 9 nguồn đã được đối chiếu trực tiếp.</p><h4>ĐÔI LỜI GIỚI THIỆU</h4>{intro}<details><summary>Tài liệu tham khảo (9)</summary><ul>{refl}</ul></details></div></footer>
<div class="mk">Phương án C · Đọc Sâu</div>{js}</body></html>'''
H=H.replace('<div class="col"></div>','')
open('C.html','w').write(H);print(words,mins,len(toc),[t for _,t in toc])

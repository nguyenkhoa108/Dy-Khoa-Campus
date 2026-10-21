import re,html,sys
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
out=[];toc=[];ch=0;first_p=True;sapo=None
for b in blocks:
    if b.startswith('## '):
        t=b[3:];ch+=1;slug=f'ch{ch}';toc.append((slug,t))
        out.append(f'<section class="ch" id="{slug}"><div class="chn">{ch:02d}</div><h2>{inl(t)}</h2></section>')
    elif b.startswith('### '): out.append(f'<h3>{inl(b[4:])}</h3>')
    elif re.match(r'^(- |\d\. )',b):
        tag='ol' if b[0].isdigit() else 'ul'
        items=[re.sub(r'^(- |\d\. )','',l) for l in b.split('\n')]
        out.append(f'<{tag}>'+''.join(f'<li>{inl(i)}</li>' for i in items)+f'</{tag}>')
    elif b.startswith('**') and sapo is None:
        sapo=inl(b.strip('*'))
    else:
        if b.startswith('**') and b.count('**')==2 and b.endswith('**'):
            pass
        cls=' class="first"' if first_p else ''
        first_p=False
        out.append(f'<p{cls}>{inl(b)}</p>')
# insert pull quote & data callout
html_body='\n'.join(out)
pq='<blockquote class="pq"><p>Đừng chỉ hỏi "làm sao xóa tin sai", mà hãy hỏi "mắt xích nào trong hệ thống mình có thể làm tốt hơn".</p></blockquote>'
stat='<aside class="stat"><div><b>6,2</b><span>điểm % ở Anh</span></div><div><b>6,4</b><span>điểm % ở Mỹ</span></div><p>Mức giảm tỷ lệ người "chắc chắn tiêm" vắc-xin sau khi xem thông tin sai, so với nhóm đối chứng (Loomba và cộng sự, 2021).</p></aside>'
html_body=html_body.replace('<section class="ch" id="ch1">',stat+'\n<section class="ch" id="ch1">',1)
html_body=html_body.replace('<section class="ch" id="ch7">',pq+'\n<section class="ch" id="ch7">',1)
faq_i=html_body.find('<section class="ch" id="ch9">')
intro=''.join(f'<p>{inl(x.strip())}</p>' for x in intro_txt.strip().split('\n\n') if x.strip() and x.strip()!='---')
refl=''.join(f'<li>{inl(x.strip())}</li>' for x in refs.strip().split('\n\n') if x.strip() and x.strip()!='---')
words=len(re.sub('<[^>]+>',' ',html_body).split()); mins=round(words/230)
tocl=''.join(f'<a href="#{s}"><b>{i+1:02d}</b>{inl(t)}</a>' for i,(s,t) in enumerate(toc))
fonts=''.join(f'<link rel="stylesheet" href="{F}{x}.css">' for x in ['newsreader/400','newsreader/400-italic','newsreader/600','newsreader/700','be-vietnam-pro/400','be-vietnam-pro/600','be-vietnam-pro/700','be-vietnam-pro/800','be-vietnam-pro/900'])
LOGO=open('/tmp/claude-0/logo/out/doc-sau-logo.svg').read(); LOGOD=open('/tmp/claude-0/logo/out/doc-sau-logo-white.svg').read(); ICON=open('/tmp/claude-0/logo/out/doc-sau-icon.svg').read()
common='''
:root{--g:#1f4b3a;--r:#a4504c;--ink:#1b1d1c;--sub:#3d4541;--mut:#6f7772;--line:#e2dcd0;--paper:#faf7f1}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:"Be Vietnam Pro",sans-serif}
a{color:var(--g);text-decoration-thickness:1px;text-underline-offset:3px}
.site{height:58px;background:#fff;border-bottom:1px solid var(--line);display:flex;align-items:center;padding:0 28px;font-size:13px;color:var(--mut)}
.site b{background:var(--g);color:#fff;padding:3px 6px;font-family:Newsreader;margin-right:8px}
.bar{position:fixed;top:0;left:0;height:3px;background:var(--r);width:0;z-index:30}
.badge{display:inline-flex;align-items:center}.badge svg{height:30px;width:auto}
.meta{display:flex;gap:18px;flex-wrap:wrap;font-size:14px;color:var(--mut)}
.meta span+span::before{content:"·";margin-right:18px}
.sapo{font-family:Newsreader,serif;font-size:1.45rem;line-height:1.55;color:var(--ink)}
.sapo strong{font-weight:600}
.art p,.art li{font-family:Newsreader,serif;font-size:1.25rem;line-height:1.78;color:#222624}
.art p{margin:0 0 1.15em}.art li{margin-bottom:.5em}
.art p.first::first-letter{font-family:"Be Vietnam Pro";font-weight:900;float:left;font-size:4.4rem;line-height:.82;padding:8px 12px 0 0;color:var(--g)}
.art h3{font-weight:800;font-size:1.3rem;margin:2em 0 .6em;letter-spacing:-.01em}
.ch{margin:3.4em 0 1.2em}
.chn{font-weight:900;font-size:.8rem;letter-spacing:.2em;color:var(--r)}
.chn::before{content:"CHƯƠNG ";}
.ch h2{font-weight:900;font-size:2.05rem;line-height:1.15;letter-spacing:-.02em;margin:.25em 0 0}
.pq{margin:2.8em 0;padding:0;border:0}
.pq p{font-family:"Be Vietnam Pro"!important;font-weight:800;font-size:1.75rem!important;line-height:1.3!important;letter-spacing:-.015em;color:var(--g)!important}
.pq p::before{content:"";display:block;width:56px;height:5px;background:var(--r);margin-bottom:18px}
.stat{display:grid;grid-template-columns:auto auto 1fr;gap:26px;align-items:center;border-top:2px solid var(--ink);border-bottom:1px solid var(--line);padding:22px 0;margin:2.2em 0}
.stat b{display:block;font-weight:900;font-size:3rem;line-height:1;color:var(--r);letter-spacing:-.03em}
.stat span{font-size:.8rem;font-weight:700;color:var(--mut)}
.stat p{font-family:"Be Vietnam Pro"!important;font-size:.92rem!important;line-height:1.55!important;color:var(--sub)!important;margin:0!important}
.author{margin:3em 0 1em;padding:24px 26px;background:#fff;border-left:4px solid var(--g)}
.author h4{margin:0 0 8px;font-size:.78rem;letter-spacing:.16em;color:var(--mut)}
.author p{font-size:1.02rem!important;line-height:1.65!important}
details.refs{margin:1.6em 0 4em;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:16px 0}
details.refs summary{font-weight:800;cursor:pointer}
details.refs li{font-family:"Be Vietnam Pro"!important;font-size:.86rem!important;line-height:1.6!important;word-break:break-word;list-style:none;padding-left:2em;text-indent:-2em}
details.refs ul{padding:0;margin:14px 0 0}
.mk{position:fixed;right:10px;bottom:10px;background:#000;color:#fff;font:700 12px sans-serif;padding:6px 10px;border-radius:4px;z-index:40}
'''
js='''<script>(function(){var b=document.querySelector('.bar'),L=[].slice.call(document.querySelectorAll('.toc a')),S=L.map(function(a){return document.querySelector(a.getAttribute('href'))});function f(){var h=document.documentElement;b.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+'%';var c=-1;S.forEach(function(s,i){if(s&&s.getBoundingClientRect().top<160)c=i});L.forEach(function(a,i){a.classList.toggle('on',i===c)})}addEventListener('scroll',f,{passive:true});f()})();</script>'''
art=f'<article class="art">{html_body}<div class="author"><h4>ĐÔI LỜI GIỚI THIỆU</h4>{intro}</div><details class="refs"><summary>Tài liệu tham khảo (8)</summary><ul>{refl}</ul></details></article>'
title='Tin giả khoa học lan truyền thế nào, và vì sao gỡ bỏ thôi là chưa đủ?'
meta=f'<div class="meta"><span>Dy Khoa</span><span>Đọc khoảng {mins} phút</span><span>{len(toc)} chương</span><span>8 nguồn tham khảo</span></div>'
A=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{fonts}<style>{common}
.hd{{max-width:900px;margin:0 auto;padding:64px 24px 34px;text-align:center}}
.hd .badge{{justify-content:center;margin-bottom:26px}}
.hd h1{{font-weight:900;font-size:clamp(2.2rem,5vw,3.6rem);line-height:1.08;letter-spacing:-.025em;margin:0 0 22px}}
.hd .meta{{justify-content:center}}
.cover{{max-width:1180px;margin:0 auto;padding:0 24px}}.cover img{{width:100%;display:block;border-radius:4px}}
.cover figcaption{{font-size:13px;color:var(--mut);margin-top:8px}}
.lay{{max-width:1180px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:230px minmax(0,680px) 1fr;gap:56px}}
.toc{{position:sticky;top:24px;align-self:start;margin-top:56px;font-size:.84rem}}
.toc small{{display:block;font-weight:800;font-size:.68rem;letter-spacing:.16em;color:var(--mut);margin-bottom:10px}}
.toc a{{display:grid;grid-template-columns:26px 1fr;gap:6px;padding:7px 0 7px 12px;border-left:2px solid var(--line);color:var(--mut);text-decoration:none;line-height:1.35}}
.toc a b{{color:inherit}}.toc a.on{{border-color:var(--r);color:var(--ink)}}.toc a.on b{{color:var(--r)}}
.sapo{{margin:56px 0 0;padding-bottom:28px;border-bottom:1px solid var(--line)}}
@media(max-width:900px){{.lay{{grid-template-columns:1fr;gap:0}}.toc{{display:none}}.art p,.art li{{font-size:1.12rem}}.sapo{{font-size:1.25rem;margin-top:32px}}.ch h2{{font-size:1.6rem}}.stat{{grid-template-columns:1fr 1fr}}.stat p{{grid-column:1/-1}}.pq p{{font-size:1.4rem!important}}.hd{{padding-top:36px}}}}
</style></head><body><div class="bar"></div><div class="site"><b>DK</b>Dy Khoa Blog (thanh menu giữ nguyên)</div>
<header class="hd"><div class="badge">{LOGO}</div><h1>{title}</h1>{meta}</header>
<figure class="cover"><img src="cover.png" alt=""><figcaption>Tin sai lan qua nhiều nhánh; cắt một liên kết không chặn được cả mạng lưới.</figcaption></figure>
<div class="lay"><nav class="toc"><small>CÁC CHƯƠNG</small>{tocl}</nav><div><div class="sapo">{sapo}</div>{art}</div><div></div></div><div class="mk">Phương án A · Báo dài sáng</div>{js}</body></html>'''
B=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{fonts}<style>{common}
.hero{{position:relative;min-height:min(88vh,760px);display:flex;align-items:flex-end;background:#0c1712 url(cover.png) center/cover;color:#fff}}
.hero::after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,14,11,.15) 0%,rgba(8,14,11,.35) 45%,rgba(8,14,11,.93) 100%)}}
.hero .in{{position:relative;z-index:2;max-width:1000px;margin:0 auto;padding:0 28px 64px;width:100%}}
.hero .badge svg{{height:30px}}
.hero h1{{font-weight:900;font-size:clamp(2.3rem,5.4vw,4.1rem);line-height:1.05;letter-spacing:-.025em;margin:22px 0 22px;max-width:900px}}
.hero .meta{{color:#cfd8d2}}
.wrap{{max-width:740px;margin:0 auto;padding:0 24px}}
.sapo{{margin:56px 0 0;padding:0 0 30px;border-bottom:1px solid var(--line)}}
.toc{{position:fixed;left:22px;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:10px;z-index:20}}
.toc a{{width:30px;height:30px;border-radius:50%;border:1.5px solid var(--line);background:var(--paper);display:grid;place-items:center;font-size:11px;font-weight:800;color:var(--mut);text-decoration:none;overflow:hidden;white-space:nowrap}}
.toc a{{font-size:0}}.toc a b{{font-size:11px}}
.toc a.on{{background:var(--r);border-color:var(--r)}}.toc a.on b{{color:#fff}}
.ch{{margin:4em -9999px 1.4em;padding:54px 9999px 44px;background:#13241d;color:#f3efe6;position:relative}}
.ch .chn{{color:#e7b7a4}}.ch h2{{color:#f3efe6;font-size:2.3rem;max-width:740px}}
.ch::after{{content:attr(data-n);}}
@media(max-width:900px){{.toc{{left:auto;right:10px;top:auto;bottom:56px;transform:none;flex-direction:row}}.toc a:not(.on){{display:none}}.art p,.art li{{font-size:1.12rem}}.sapo{{font-size:1.25rem;margin-top:32px}}.ch h2{{font-size:1.6rem}}.stat{{grid-template-columns:1fr 1fr}}.stat p{{grid-column:1/-1}}.pq p{{font-size:1.4rem!important}}.hero{{min-height:620px}}}}
body{{overflow-x:hidden}}
</style></head><body><div class="bar"></div><div class="site"><b>DK</b>Dy Khoa Blog (thanh menu giữ nguyên)</div>
<header class="hero"><div class="in"><div class="badge">{LOGOD}</div><h1>{title}</h1>{meta}</div></header>
<nav class="toc">{tocl}</nav>
<div class="wrap"><div class="sapo">{sapo}</div>{art}</div><div class="mk">Phương án B · Mở màn tối</div>{js}</body></html>'''
open('A.html','w').write(A);open('B.html','w').write(B);print(words,mins,len(toc))

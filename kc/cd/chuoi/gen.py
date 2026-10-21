import json,re,html,math
B='/home/claude/dy-khoa-campus/bm/'
order=['di-bo-10000-buoc-moi-ngay-co-can-thiet','9-10-nha-si-khuyen-dung-khao-sat-gay-hieu-lam','xa-phong-diet-khuan-99-9-co-tot-hon-xa-phong-thuong','dat-chuan-fda-fda-co-cap-phep-thuc-pham-chuc-nang-khong','da-chung-minh-lam-sang-nghia-la-gi','detox-thai-doc-co-that-khong','sua-chua-tang-mien-dich-vu-activia-ftc','giay-san-chac-co-skechers-reebok-ftc','game-luyen-nao-lumosity-ftc']
P=[]
for s in order:
    d=json.load(open(B+s+'.json'));txt=re.sub('<[^>]+>',' ',d['content']);w=len(txt.split())
    P.append(dict(s=s,t=d['title'],e=d['excerpt'],m=max(1,round(w/220)),date=d['date'][:10]))
tot=sum(p['m'] for p in P)
def short(t):
    t=t.split(':')[0].split('?')[0];return t.replace('"','').strip()
toc=''.join(f'<a href="#bai-{i+1}"><b>{i+1:02d}</b><span>{html.escape(short(p["t"]))}</span></a>' for i,p in enumerate(P))
items=''
for i,p in enumerate(P):
    lay='split' if i%3==2 else 'wide'
    items+=f'''<article class="sx {lay}" id="bai-{i+1}"><div class="sx-n">{i+1:02d}</div>
<a class="sx-img" href="#"><img src="{p["s"]}.webp" alt=""></a>
<div class="sx-tx"><div class="sx-k">Bài {i+1} · {p["m"]} phút đọc</div><h2><a href="#">{html.escape(p["t"])}</a></h2><p>{html.escape(p["e"])}</p><a class="sx-go" href="#">Đọc bài <span>→</span></a></div></article>'''
stack=''.join(f'<img src="{P[k]["s"]}.webp" class="st st{k}" alt="">' for k in range(3))
F='/tmp/claude-0/fonts/node_modules/@fontsource/'
css=open('/tmp/claude-0/lf/style.css').read()
out=f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="{F}newsreader/500.css"><link rel="stylesheet" href="{F}newsreader/700.css"><link rel="stylesheet" href="{F}newsreader/800.css"><link rel="stylesheet" href="{F}newsreader/500-italic.css">
<link rel="stylesheet" href="{F}be-vietnam-pro/400.css"><link rel="stylesheet" href="{F}be-vietnam-pro/700.css"><link rel="stylesheet" href="{F}be-vietnam-pro/800.css">
<style>{css}</style></head><body>
<div class="sitebar"><b>DK</b> Dy Khoa Blog <i>(thanh menu của blog giữ nguyên)</i></div>
<div class="bar" id="bar"></div>
<header class="hx"><div class="hx-in"><div class="hx-tx">
<nav class="crumb"><a href="#">Blog</a> / <a href="#">Chuỗi bài</a></nav>
<div class="kick">Chuỗi bài</div>
<h1>Bóc mác y khoa trong quảng cáo</h1>
<p class="desc">Mỗi bài đặt một thông điệp quảng cáo mang dáng dấp y khoa cạnh nguồn gốc và bằng chứng của nó, kèm nguồn tham khảo mở để bạn tự kiểm tra.</p>
<div class="meta"><span>Đọc trọn chuỗi khoảng {tot} phút</span><span>Cập nhật 20/11/2026</span></div>
<div class="cta"><a class="btn" href="#bai-1">Bắt đầu từ bài 1</a><a class="lnk" href="#">Xem chuyên đề →</a></div>
</div><div class="hx-st">{stack}</div></div></header>
<div class="body"><nav class="toc" aria-label="Các bài trong chuỗi"><small>Thứ tự đọc</small>{toc}</nav>
<main class="main">{items}
<section class="end"><div class="end-k">Hết chuỗi</div><h2>Bạn đã đọc hết {len(P)} bài</h2><p>Muốn xem công cụ tự kiểm tra và các bài liên quan, ghé trang chuyên đề.</p><a class="btn" href="#">Vào chuyên đề Bóc mác y khoa</a>
<div class="others"><small>Chuỗi bài khác</small><a href="#">Kiểm chứng thông tin khoa học</a><a href="#">Tình dục học</a><a href="#">Hiểu đúng về đột quỵ</a></div></section>
</main></div>
<script>(function(){{var b=document.getElementById('bar'),L=[].slice.call(document.querySelectorAll('.toc a')),S=L.map(function(a){{return document.querySelector(a.getAttribute('href'))}});function f(){{var h=document.documentElement;b.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+'%';var c=-1;S.forEach(function(s,i){{if(s.getBoundingClientRect().top<200)c=i}});L.forEach(function(a,i){{a.classList.toggle('on',i===c);a.classList.toggle('done',i<c)}})}}addEventListener('scroll',f,{{passive:true}});f()}})();</script>
</body></html>'''
open('mock.html','w').write(out)

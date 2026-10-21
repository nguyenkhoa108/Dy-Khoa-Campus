F='/tmp/claude-0/fonts/node_modules/@fontsource/'
fonts=''.join(f'<link rel="stylesheet" href="{F}{x}.css">' for x in ['be-vietnam-pro/400','be-vietnam-pro/600','be-vietnam-pro/700','be-vietnam-pro/800','be-vietnam-pro/900','newsreader/400','newsreader/600'])
WM='/tmp/claude-0/logo/out/doc-sau-dau-anh@3x.png'
base=f'''<!doctype html><html><head><meta charset="utf-8">{fonts}<style>
*{{box-sizing:border-box}}body{{margin:0}}
.f{{position:relative;width:1200px;min-height:0;padding-bottom:110px!important;background:#faf7f1;font-family:"Be Vietnam Pro";color:#1b1d1c;padding:54px 64px;overflow:hidden}}
.k{{font-size:15px;font-weight:800;letter-spacing:.18em;color:#a4504c}}
h1{{font-size:38px;font-weight:900;letter-spacing:-.02em;line-height:1.12;margin:10px 0 0;max-width:900px}}
.src{{position:absolute;left:64px;bottom:34px;font-size:15px;color:#6f7772;max-width:760px;line-height:1.4}}
.wm{{position:absolute;right:34px;bottom:26px;height:40px}}
.g{{color:#1f4b3a}}.r{{color:#a4504c}}
</style></head><body><div class="f">BODY<img class="wm" src="{WM}"></div></body></html>'''
figs={}
# 1 Loomba
figs['h1-thi-nghiem-loomba']='''<div class="k">THÍ NGHIỆM, THÁNG 9/2020</div><h1>Sau khi xem tin sai, ý định tiêm vắc-xin giảm</h1>
<div style="display:grid;grid-template-columns:250px 1fr 300px;gap:30px;align-items:center;margin-top:46px">
<div style="background:#1f4b3a;color:#fff;border-radius:8px;padding:28px"><div style="font-size:58px;font-weight:900;line-height:1">8.001</div><div style="font-size:18px;margin-top:8px">người ở Anh và Mỹ</div></div>
<div style="display:flex;flex-direction:column;gap:18px">
<div style="display:flex;align-items:center;gap:14px"><svg width="70" height="20"><path d="M0 10H60" stroke="#a4504c" stroke-width="3"/><path d="M56 3 68 10 56 17" fill="none" stroke="#a4504c" stroke-width="3"/></svg><div style="border:2px solid #a4504c;border-radius:8px;padding:16px 20px;flex:1"><b style="font-size:26px" class="r">6.001 người</b><div style="font-size:17px">xem thông tin sai về vắc-xin Covid-19</div></div></div>
<div style="display:flex;align-items:center;gap:14px"><svg width="70" height="20"><path d="M0 10H60" stroke="#1f4b3a" stroke-width="3"/><path d="M56 3 68 10 56 17" fill="none" stroke="#1f4b3a" stroke-width="3"/></svg><div style="border:2px solid #1f4b3a;border-radius:8px;padding:16px 20px;flex:1"><b style="font-size:26px" class="g">2.000 người</b><div style="font-size:17px">xem thông tin chính xác (nhóm đối chứng)</div></div></div></div>
<div><div style="font-size:16px;font-weight:700;color:#6f7772;margin-bottom:10px">Tỷ lệ "chắc chắn tiêm" giảm so với đối chứng</div>
<div style="display:flex;gap:26px"><div><div style="font-size:72px;font-weight:900;line-height:1" class="r">6,2</div><div style="font-size:17px;font-weight:700">điểm % · Anh</div></div><div><div style="font-size:72px;font-weight:900;line-height:1" class="r">6,4</div><div style="font-size:17px;font-weight:700">điểm % · Mỹ</div></div></div></div></div>
<div class="src">Nguồn: Loomba và cộng sự (2021), Nature Human Behaviour. Anh 3.000 và Mỹ 3.001 người xem tin sai; mỗi nước 1.000 người xem thông tin đúng.</div>'''
# 2 Vosoughi
figs['h2-tin-sai-lan-nhanh-hon']='''<div class="k">TWITTER, 2006-2017</div><h1>Tin sai lan nhanh và xa hơn tin đúng</h1>
<div style="margin-top:40px;display:grid;grid-template-columns:1fr 1fr;gap:56px">
<div><div style="font-size:18px;font-weight:700;margin-bottom:18px">Thời gian để tiếp cận 1.500 người</div>
<div style="display:flex;align-items:center;gap:14px;margin-bottom:16px"><div style="width:80px;font-weight:800" class="r">Tin sai</div><div style="height:38px;width:70px;background:#a4504c;border-radius:4px"></div><b style="font-size:20px">1 phần</b></div>
<div style="display:flex;align-items:center;gap:14px"><div style="width:80px;font-weight:800" class="g">Tin đúng</div><div style="height:38px;width:420px;background:#1f4b3a;border-radius:4px"></div><b style="font-size:20px">khoảng 6 lần</b></div></div>
<div><div style="font-size:18px;font-weight:700;margin-bottom:18px">Khả năng được chia sẻ lại</div>
<div style="display:flex;align-items:baseline;gap:12px"><span style="font-size:96px;font-weight:900;line-height:1" class="r">+70%</span></div><div style="font-size:19px;margin-top:8px">tin sai so với tin đúng</div>
<div style="margin-top:26px;font-size:18px;line-height:1.5;background:#fff;border-left:4px solid #1f4b3a;padding:14px 18px">Tài khoản tự động làm tin đúng và tin sai lan nhanh <b>như nhau</b>. Tin sai đi xa hơn vì <b>con người</b> chia sẻ nó nhiều hơn.</div></div></div>
<div class="src">Nguồn: Vosoughi, Roy và Aral (2018), Science. Khoảng 126.000 câu chuyện, khoảng 3 triệu người, hơn 4,5 triệu lượt tweet.</div>'''
# 3 Royal Society survey
def bar(label,v,col):
    return f'<div style="display:grid;grid-template-columns:420px 1fr 70px;gap:16px;align-items:center;margin-bottom:22px"><div style="font-size:19px;line-height:1.3">{label}</div><div style="height:30px;background:#e8e2d6;border-radius:4px"><div style="height:30px;width:{v}%;background:{col};border-radius:4px"></div></div><b style="font-size:26px;color:{col}">{v}%</b></div>'
figs['h3-khao-sat-hoi-hoang-gia-anh']='<div class="k">KHẢO SÁT 2.019 NGƯỜI DÂN ANH, 7/2021</div><h1>Tin sai xuất hiện nhiều trên mạng, nhưng chỉ một thiểu số tin nó</h1><div style="margin-top:44px">'+bar('Cho rằng internet giúp công chúng hiểu khoa học tốt hơn',61,'#1f4b3a')+bar('Tin rằng công nghệ 5G có hại cho sức khỏe',15,'#a4504c')+bar('Không tin vắc-xin Covid-19 an toàn',5,'#a4504c')+bar('Không tin con người có bất kỳ trách nhiệm nào trong biến đổi khí hậu',5,'#a4504c')+'</div><div class="src">Nguồn: The Royal Society (2022), khảo sát cùng YouGov.</div>'
# 4 NASEM four points
def node(t,d,hl=False):
    bg='#a4504c' if hl else '#fff'; c='#fff' if hl else '#1b1d1c'; b='#a4504c' if hl else '#1f4b3a'
    return f'<div style="background:{bg};color:{c};border:2px solid {b};border-radius:10px;padding:22px 18px;text-align:center"><div style="font-size:26px;font-weight:900">{t}</div><div style="font-size:16px;margin-top:8px;line-height:1.35">{d}</div></div>'
arrow='<svg width="40" height="24"><path d="M2 12H34" stroke="#1f4b3a" stroke-width="3"/><path d="M28 4 38 12 28 20" fill="none" stroke="#1f4b3a" stroke-width="3"/></svg>'
figs['h4-bon-diem-can-thiep']='<div class="k">BỐN ĐIỂM CAN THIỆP</div><h1>Gỡ bỏ nội dung chỉ chạm vào một mắt xích</h1><div style="display:grid;grid-template-columns:1fr 40px 1fr 40px 1fr 40px 1fr;align-items:center;gap:8px;margin-top:56px">'+node('Nguồn cung','Ai tạo ra tin sai')+arrow+node('Nhu cầu','Vì sao người ta tìm đến nó')+arrow+node('Phân phối','Tin sai lan đi thế nào',True)+arrow+node('Tiếp nhận','Người ta tin và dùng nó ra sao')+'</div><div style="display:grid;grid-template-columns:1fr 40px 1fr 40px 1fr 40px 1fr;gap:8px;margin-top:14px"><div></div><div></div><div></div><div></div><div style="text-align:center;font-size:17px;font-weight:800" class="r">↑ gỡ bỏ nội dung</div></div><div style="margin-top:26px;font-size:20px;line-height:1.5;max-width:900px">Chưa có điểm nào được chứng minh là tốt nhất; nhiều cách làm hiệu quả tác động vào nhiều điểm cùng lúc.</div><div class="src">Nguồn: National Academies of Sciences, Engineering, and Medicine (2025), Kết luận 7-1.</div>'
# 5 debunking 4 steps
def step(n,t,d,c):
    return f'<div style="border-top:6px solid {c};background:#fff;border-radius:0 0 10px 10px;padding:22px 20px"><div style="font-size:44px;font-weight:900;color:{c};line-height:1">{n}</div><div style="font-size:24px;font-weight:900;margin-top:10px">{t}</div><div style="font-size:17px;margin-top:8px;line-height:1.4;color:#3d4541">{d}</div></div>'
figs['h5-bon-buoc-dinh-chinh']='<div class="k">CẤU TRÚC ĐÍNH CHÍNH</div><h1>Đặt sự thật ở đầu và ở cuối</h1><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:50px">'+step('1','Sự thật','Mở đầu bằng điều đúng, nếu nó rõ ràng, ngắn gọn, dễ nhớ','#1f4b3a')+step('2','Cảnh báo','Báo trước rằng sắp nhắc tới một thông tin sai','#a4504c')+step('3','Giải thích','Chỉ ra thông tin sai đánh lừa người đọc bằng cách nào','#a4504c')+step('4','Sự thật','Kết thúc bằng việc nhắc lại điều đúng','#1f4b3a')+'</div><div class="src">Nguồn: Lewandowsky và cộng sự (2020), The Debunking Handbook 2020.</div>'
# 6 prebunking funnel
def fl(w,num,lab,c):
    return f'<div style="display:flex;align-items:center;gap:22px;margin-bottom:16px"><div style="width:{w}px;height:64px;background:{c};border-radius:6px;display:flex;align-items:center;padding-left:20px;color:#fff;font-size:30px;font-weight:900">{num}</div><div style="font-size:19px;line-height:1.35;max-width:420px">{lab}</div></div>'
figs['h6-tiem-phong-tam-ly-youtube']='<div class="k">THỬ NGHIỆM TRÊN YOUTUBE, 2022</div><h1>"Tiêm phòng tâm lý" cho hàng triệu người dùng</h1><div style="margin-top:40px">'+fl(600,'khoảng 5,4 triệu','người dùng được hiển thị video quảng cáo trong 15 ngày','#1f4b3a')+fl(420,'967.347','người xem từ 30 giây trở lên','#2f6b54')+fl(260,'22.632','câu trả lời kiểm tra trong vòng 24 giờ (gồm nhóm đối chứng)','#a4504c')+'</div><div style="font-size:19px;margin-top:12px">Người xem video nhận ra kỹ thuật thao túng tốt hơn nhóm đối chứng; chi phí khoảng 0,05 USD mỗi lượt xem.</div><div class="src">Nguồn: Roozenbeek và cộng sự (2022), Science Advances.</div>'
import os
for k,v in figs.items(): open(k+'.html','w').write(base.replace('BODY',v))
print(list(figs))

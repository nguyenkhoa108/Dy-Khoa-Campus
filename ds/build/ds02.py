import re,json,html
exec(open('/home/claude/dy-khoa-campus/bm/bm1.py').read().split('\n',9)[0:9] and '\n'.join(open('/home/claude/dy-khoa-campus/bm/bm1.py').read().split('\n')[:9]))
md=open('/home/claude/dy-khoa-campus/ds/doc-sau-02-truyen-thong-rui-ro.md').read()
body=md.split('# Truyền thông rủi ro khi có dịch: WHO khuyến cáo gì, và vì sao vẫn hay bị làm sai?')[1]
main,rest=body.split('**Đôi lời giới thiệu**')
refs=rest.split('**Tài liệu tham khảo** (khối xổ xuống)')[1].split('**Ghi chú cho người duyệt')[0]
def inl(s):
    s=s.replace('&','&amp;')
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'\*([^*]+)\*',r'<em>\1</em>',s)
    return s
def HTML(x): return f'<!-- wp:html -->\n{x}\n<!-- /wp:html -->\n\n'
def OL(items):
    li=''.join(f'<!-- wp:list-item -->\n<li>{i}</li>\n<!-- /wp:list-item -->' for i in items)
    return f'<!-- wp:list {{"ordered":true}} -->\n<ol class="wp-block-list">{li}</ol>\n<!-- /wp:list -->\n\n'
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'

ALT={'r1-nam-nguyen-tac-who':'Năm nguyên tắc cốt lõi của truyền thông rủi ro theo hướng dẫn WHO 2018: niềm tin, bất định, ngôn ngữ, nhất quán và sớm, cộng đồng',
 'r2-thi-nghiem-covacid':'Biểu đồ thí nghiệm COVACID của Petersen và cộng sự 2021: so với nhóm đối chứng, minh bạch tích cực +7, trung tính +5, nói cả điểm bất lợi -15, mơ hồ -9 điểm phần trăm sẵn sàng tiêm',
 'r3-stay-home':'Được và mất của khẩu hiệu truyền thông rủi ro Stay Home tại Anh theo báo cáo điều tra Covid-19 năm 2025',
 'r4-tong-quan-truyen-thong':'Tổng quan bằng chứng 2023: từ khoảng 11.500 tài liệu chọn 13 nghiên cứu, ba đặc điểm truyền thông giúp người dân làm theo',
 'r5-ky-thi-mpox':'Kỳ thị quanh mpox ở Anh: 68% cho rằng xấu hổ khiến ngại xét nghiệm, 24% khó báo bạn tình, 11 trên 13 người từng mắc bị kỳ thị'}
def FIG(k,cap):
    return HTML(f'<figure class="ds-fig"><picture><source media="(max-width: 700px)" srcset="{{{{M:{k}-doc}}}}"><img src="{{{{M:{k}}}}}" alt="{ALT[k]}" width="1200" loading="lazy" decoding="async"></picture><figcaption>{cap}</figcaption></figure>')
TRIG=[('Hướng dẫn có các nhóm khuyến nghị','r1-nam-nguyen-tac-who','Hình 1. Năm nguyên tắc được phân tích trong bài, theo hướng dẫn của WHO (2018).'),
 ('Nhóm tác giả giải thích rằng sự mơ hồ','r2-thi-nghiem-covacid','Hình 2. Kết quả nghiên cứu thứ hai trong thí nghiệm COVACID (Petersen và cộng sự, 2021).'),
 ('Trở lại với khẩu hiệu','r3-stay-home','Hình 3. Khẩu hiệu "Stay Home" theo đánh giá của báo cáo điều tra Covid-19 tại Anh (UK Covid-19 Inquiry, 2025).'),
 ('Tổng quan này có hạn chế','r4-tong-quan-truyen-thong','Hình 4. Tổng quan bằng chứng về truyền thông và việc tuân thủ biện pháp phòng dịch (Williams và cộng sự, 2023).'),
 ('Với người làm truyền thông, con số 68%','r5-ky-thi-mpox','Hình 5. Kết quả khảo sát về kỳ thị quanh mpox ở Anh (Paterson và cộng sự, 2025).')]
blocks=[b.strip() for b in main.strip().split('\n\n') if b.strip() and b.strip()!='---']
c='';toc=[];ch=0;sapo=None;teaser=False
for b in blocks:
    if b.startswith('# '): continue
    if b.startswith('## '):
        t=b[3:]
        if t.startswith('Kết') or t.startswith('Hỏi nhanh'):
            if t.startswith('Kết'):
                c+=HTML('<blockquote class="ds-band"><p>Khi dịch đã bùng phát, đã quá muộn để bắt đầu xây dựng niềm tin.</p></blockquote>')
            c+=H2(inl(t));teaser=False;continue
        ch+=1;toc.append(t);teaser=True;opener_t=t;continue
    if teaser:
        m=re.match(r'\*\*(.+?)\*\*\s*(.*)',b,re.S)
        c+=HTML(f'<section class="ds-op" id="chuong-{ch}"><div class="ds-op-in"><div class="ds-op-n" aria-hidden="true">{ch:02d}</div><div class="ds-op-t"><div class="ds-op-k">CHƯƠNG {ch:02d} / 0TOTAL</div><h2 class="wp-block-heading">{inl(opener_t)}</h2><p class="ds-op-a">{inl(m.group(1))}</p></div></div></section>')
        teaser=False
        rest_=m.group(2).strip()
        if rest_: c+=P(inl(rest_))
        continue
    if b.startswith('### '): c+=H3(inl(b[4:]));continue
    if re.match(r'^(- |\d\. )',b):
        items=[inl(re.sub(r'^(- |\d\. )','',l)) for l in b.split('\n')]
        c+=OL(items) if b[0].isdigit() else UL(items);continue
    if sapo is None and b.startswith('**'):
        sapo=b.strip('*');c+=HTML(f'<p class="ds-sapo">{inl(sapo)}</p>');continue
    c+=P(inl(b))
    for tr in list(TRIG):
        if b.startswith(tr[0]): c+=FIG(tr[1],tr[2]);TRIG.remove(tr)
assert not TRIG,TRIG
c=c.replace('0TOTAL',f'{ch:02d}')
strip='<nav class="ds-strip" aria-label="Các chương">'+''.join(f'<a href="#chuong-{i+1}"><b>{i+1:02d}</b><span>{inl(t)}</span></a>' for i,t in enumerate(toc))+'</nav>'
c=HTML(strip)+c
refl=[inl(x.strip()) for x in refs.strip().split('\n\n') if x.strip() and x.strip()!='---']
c+='<!-- wp:group {"className":"ds-end"} -->\n<div class="wp-block-group ds-end">'+GEN_END+REFS(refl)+'</div>\n<!-- /wp:group -->'
out=dict(slug='truyen-thong-rui-ro-khi-co-dich',title='Truyền thông rủi ro khi có dịch: WHO khuyến cáo gì, và vì sao vẫn hay bị làm sai?',
 seo_title='Truyền thông rủi ro khi có dịch: WHO khuyến cáo gì?',
 meta_desc='WHO có hướng dẫn rõ về truyền thông rủi ro trong dịch bệnh, nhưng Covid-19 và mpox cho thấy ngay cả Anh vẫn làm sai. Bài phân tích 5 nguyên tắc cốt lõi và bằng chứng từ các tình huống gần đây.',
 focus_kw='truyền thông rủi ro',excerpt='Hướng dẫn của WHO đã chỉ rõ cách truyền thông khi có dịch, nhưng Covid-19 và mpox cho thấy làm đúng khó hơn biết đúng rất nhiều.',
 tags=['truyền thông rủi ro','truyền thông sức khỏe','Covid-19','mpox','WHO','niềm tin'],
 cover_alt='Minh họa truyền thông rủi ro: các sóng thông điệp lan ra từ một nguồn đỏ, có đoạn đứt quãng, tới những chấm tượng trưng cho người dân',
 alts=ALT,content=c)
json.dump(out,open('truyen-thong-rui-ro-khi-co-dich.json','w'),ensure_ascii=False,indent=1)
txt=re.sub('<[^>]+>',' ',c)
for bad in ['dẫn theo','truy cập mở','sinh viên','—','–',' - ']: print(repr(bad),txt.count(bad))
print(len(toc),c.count('ds-fig'),c.count('ds-op"'),len(c),toc)

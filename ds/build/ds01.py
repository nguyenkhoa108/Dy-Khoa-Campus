import re,json,html
exec(open('/home/claude/dy-khoa-campus/bm/bm1.py').read().split('\n',9)[0:9] and '\n'.join(open('/home/claude/dy-khoa-campus/bm/bm1.py').read().split('\n')[:9]))
md=open('/home/claude/dy-khoa-campus/ds/doc-sau-01-tin-gia-khoa-hoc.md').read()
body=md.split('# Tin giả khoa học lan truyền thế nào, và vì sao gỡ bỏ thôi là chưa đủ?')[1]
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
ALT={'h1-thi-nghiem-loomba':'Sơ đồ thí nghiệm Loomba và cộng sự 2021: 8.001 người, tin giả khoa học về vắc-xin làm tỷ lệ chắc chắn tiêm giảm 6,2 điểm phần trăm ở Anh và 6,4 ở Mỹ',
 'h2-tin-sai-lan-nhanh-hon':'Biểu đồ tin sai lan nhanh hơn tin đúng trên Twitter: tin đúng cần khoảng 6 lần thời gian để tới 1.500 người, tin sai được chia sẻ lại nhiều hơn 70%',
 'h3-khao-sat-hoi-hoang-gia-anh':'Biểu đồ khảo sát Hội Hoàng gia Anh 2021 về tin sai khoa học: 61%, 15%, 5% và 5%',
 'h4-bon-diem-can-thiep':'Sơ đồ bốn điểm can thiệp tin giả khoa học theo NASEM: nguồn cung, nhu cầu, phân phối, tiếp nhận; gỡ bỏ nội dung chỉ chạm vào khâu phân phối',
 'h6-tiem-phong-tam-ly-youtube':'Phễu thử nghiệm tiêm phòng tâm lý trên YouTube: khoảng 5,4 triệu người dùng, 967.347 lượt xem trên 30 giây, 22.632 câu trả lời',
 'h5-bon-buoc-dinh-chinh':'Bốn bước đính chính tin sai: sự thật, cảnh báo, giải thích, sự thật'}
def FIG(k,cap):
    return HTML(f'<figure class="ds-fig"><picture><source media="(max-width: 700px)" srcset="{{{{M:{k}-doc}}}}"><img src="{{{{M:{k}}}}}" alt="{ALT[k]}" width="1200" loading="lazy" decoding="async"></picture><figcaption>{cap}</figcaption></figure>')
FIGS={(0,2):('h1-thi-nghiem-loomba','Hình 1. Thiết kế và kết quả chính của thí nghiệm Loomba và cộng sự (2021).'),
 (3,2):('h2-tin-sai-lan-nhanh-hon','Hình 2. Tin sai và tin đúng trên Twitter, theo Vosoughi và cộng sự (2018).'),
 (4,2):('h3-khao-sat-hoi-hoang-gia-anh','Hình 3. Kết quả khảo sát của Hội Hoàng gia Anh và YouGov (The Royal Society, 2022).'),
 (6,4):('h4-bon-diem-can-thiep','Hình 4. Bốn điểm can thiệp theo NASEM (2025).')}
blocks=[b.strip() for b in main.strip().split('\n\n') if b.strip() and b.strip()!='---']
c='';toc=[];ch=0;pin=0;sapo=None;teaser=False;first=True
for b in blocks:
    if b.startswith('## '):
        t=b[3:]
        if t.startswith('Kết') or t.startswith('Hỏi nhanh'):
            if t.startswith('Kết'):
                c+=HTML('<blockquote class="ds-band"><p>Đừng chỉ hỏi "làm sao xóa tin sai", mà hãy hỏi "mắt xích nào trong hệ thống mình có thể làm tốt hơn".</p></blockquote>')
            c+=H2(inl(t));ch_cur=None;teaser=False;continue
        ch+=1;toc.append(t);pin=0;teaser=True;opener_t=t;continue
    if teaser:
        m=re.match(r'\*\*(.+?)\*\*\s*(.*)',b,re.S)
        c+=HTML(f'<section class="ds-op" id="chuong-{ch}"><div class="ds-op-in"><div class="ds-op-n" aria-hidden="true">{ch:02d}</div><div class="ds-op-t"><div class="ds-op-k">CHƯƠNG {ch:02d} / 0TOTAL</div><h2 class="wp-block-heading">{inl(opener_t)}</h2><p class="ds-op-a">{inl(m.group(1))}</p></div></div></section>')
        teaser=False
        rest_=m.group(2).strip()
        if rest_: c+=P(inl(rest_));pin+=1
        continue
    if b.startswith('### '): c+=H3(inl(b[4:]));continue
    if re.match(r'^(- |\d\. )',b):
        items=[inl(re.sub(r'^(- |\d\. )','',l)) for l in b.split('\n')]
        if b[0].isdigit():
            if 'Sự thật' in b: c+=FIG('h5-bon-buoc-dinh-chinh','Hình 6. Cấu trúc bốn bước của <em>Cẩm nang bác bỏ tin sai 2020</em> (Lewandowsky và cộng sự, 2020).')
            c+=OL(items)
        else: c+=UL(items)
        continue
    if sapo is None and b.startswith('**'):
        sapo=b.strip('*');c+=HTML(f'<p class="ds-sapo">{inl(sapo)}</p>');continue
    if 'Đây là định nghĩa của hội đồng chuyên gia' in b:
        c+=HTML('<aside class="ds-note"><b>NASEM</b>Viện Hàn lâm Khoa học, Kỹ thuật và Y học Hoa Kỳ. Báo cáo đồng thuận năm 2025 về tin sai khoa học do một hội đồng chuyên gia biên soạn.</aside>')
    c+=P(inl(b));pin+=1
    if (ch,pin) in FIGS: k,cap=FIGS.pop((ch,pin));c+=FIG(k,cap)
    if 'Theo thông cáo của Đại học Cambridge, mức cải thiện' in b:
        c+=FIG('h6-tiem-phong-tam-ly-youtube','Hình 5. Phễu thử nghiệm thực địa trên YouTube (Roozenbeek và cộng sự, 2022).')
c=c.replace('0TOTAL',f'{ch:02d}')
strip='<nav class="ds-strip" aria-label="Các chương">'+''.join(f'<a href="#chuong-{i+1}"><b>{i+1:02d}</b><span>{inl(t)}</span></a>' for i,t in enumerate(toc))+'</nav>'
c=HTML(strip)+c
refl=[inl(x.strip()) for x in refs.strip().split('\n\n') if x.strip() and x.strip()!='---']
c+='<!-- wp:group {"className":"ds-end"} -->\n<div class="wp-block-group ds-end">'+GEN_END+REFS(refl)+'</div>\n<!-- /wp:group -->'
assert not FIGS, FIGS
out=dict(slug='tin-gia-khoa-hoc-lan-truyen-the-nao',title='Tin giả khoa học lan truyền thế nào, và vì sao gỡ bỏ thôi là chưa đủ?',
 seo_title='Tin giả khoa học lan truyền thế nào và vì sao gỡ bỏ chưa đủ?',
 meta_desc='Tin giả khoa học lan nhanh vì con người, thiết kế nền tảng và động cơ sản xuất nội dung. Báo cáo của Viện Hàn lâm Mỹ và Hội Hoàng gia Anh giải thích vì sao gỡ bỏ thôi là chưa đủ.',
 focus_kw='tin giả khoa học',excerpt='Tin giả khoa học không lan nhanh chỉ vì có người cố tình bịa đặt, và xóa từng bài đăng sai không giải quyết được gốc rễ.',
 tags=['tin giả','thông tin sai lệch','truyền thông khoa học','kiểm chứng thông tin','prebunking'],
 cover_alt='Minh họa mạng lưới tin giả khoa học lan từ một nguồn đỏ qua nhiều nhánh, một liên kết bị cắt nhưng tin sai vẫn lan qua các nhánh khác',
 alts=ALT,content=c)
json.dump(out,open('tin-gia-khoa-hoc-lan-truyen-the-nao.json','w'),ensure_ascii=False,indent=1)
txt=re.sub('<[^>]+>',' ',c)
for bad in ['dẫn theo','truy cập mở','sinh viên','—','–',' - ']: print(repr(bad),txt.count(bad))
print(len(toc),c.count('ds-fig'),c.count('ds-op"'),len(c))

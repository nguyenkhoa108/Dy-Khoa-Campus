import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'


FTC = 'Federal Trade Commission. (2016, ngày 4 tháng 1). <em>Lumosity to pay $2 million to settle FTC deceptive advertising charges for its "brain training" program</em> [Thông cáo báo chí]. https://www.ftc.gov/news-events/news/press-releases/2016/01/lumosity-pay-2-million-settle-ftc-deceptive-advertising-charges-its-brain-training-program'
APS = 'Association for Psychological Science. (2016, ngày 30 tháng 9). <em>Do "brain-training" programs work?</em> https://www.psychologicalscience.org/publications/brain-training.html'
ND87 = 'Chính phủ. (2026). <em>Nghị định số 87/2026/NĐ-CP quy định xử phạt vi phạm hành chính trong lĩnh vực văn hóa và quảng cáo</em>. Công báo điện tử Chính phủ. https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-87-2026-nd-cp-469359.htm'

c = ''
c += P('Game "luyện não" có thể giúp bạn chơi chính trò chơi đó giỏi hơn, nhưng chưa có nhiều bằng chứng cho thấy nó cải thiện trí nhớ, khả năng làm việc hay phòng ngừa sa sút trí tuệ ngoài đời thực. Năm 2016, Ủy ban Thương mại Liên bang Mỹ (FTC) cáo buộc công ty đứng sau ứng dụng Lumosity quảng cáo không có căn cứ rằng game giúp làm việc, học tập tốt hơn và làm chậm suy giảm nhận thức do tuổi tác. Công ty đồng ý trả 2 triệu USD (Federal Trade Commission [FTC], 2016).')
c += P('Đây là bài cuối trong chuyên đề "Bóc mác y khoa trong quảng cáo". Bài trước kể lại ' + A('giay-san-chac-co-skechers-reebok-ftc', 'vụ giày "săn chắc cơ"') + '.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Lumosity quảng cáo game giúp cải thiện học tập, công việc và phòng ngừa sa sút trí tuệ, Alzheimer; FTC cho rằng công ty không có căn cứ khoa học.',
    'Công ty mua hàng trăm từ khóa quảng cáo liên quan đến trí nhớ, sa sút trí tuệ và Alzheimer.',
    'Một số lời chứng thực của khách hàng được thu thập qua cuộc thi có giải thưởng lớn mà không công bố, theo FTC.',
    'Tổng quan khoa học năm 2016: tập luyện cải thiện chính bài tập được luyện, nhưng có rất ít bằng chứng về lợi ích cho nhận thức hằng ngày.',
])

c += H2('Lumosity đã hứa gì?')
c += P('Theo đơn kiện của FTC (2016), Lumosity gồm 40 trò chơi được cho là nhắm vào từng vùng não cụ thể. Công ty quảng cáo rằng luyện tập 10 đến 15 phút, ba hoặc bốn lần mỗi tuần có thể giúp người dùng đạt "toàn bộ tiềm năng trong mọi khía cạnh của cuộc sống". Gói đăng ký có giá từ 14,95 USD mỗi tháng đến 299,95 USD trọn đời.')
c += P('FTC cáo buộc công ty tuyên bố việc luyện tập với Lumosity sẽ (FTC, 2016):')
c += UL([
    'Cải thiện khả năng thực hiện công việc hằng ngày, kết quả học tập, làm việc và thể thao.',
    'Làm chậm suy giảm nhận thức do tuổi tác, bảo vệ khỏi suy giảm nhận thức nhẹ, sa sút trí tuệ và bệnh Alzheimer.',
    'Giảm suy giảm nhận thức liên quan đến đột quỵ, chấn thương sọ não, rối loạn căng thẳng sau sang chấn, rối loạn tăng động giảm chú ý, tác dụng phụ của hóa trị và hội chứng Turner.',
    'Các lợi ích trên đã được nghiên cứu khoa học chứng minh.',
])

c += H2('Quảng cáo đã nhắm vào nỗi sợ thế nào?')
c += P('Giám đốc Văn phòng Bảo vệ Người tiêu dùng của FTC khi đó, Jessica Rich, nhận định Lumosity đã khai thác nỗi sợ của người tiêu dùng về suy giảm nhận thức khi về già, gợi ý rằng game có thể ngăn mất trí nhớ, sa sút trí tuệ và cả bệnh Alzheimer, trong khi công ty "đơn giản là không có khoa học" để chứng minh quảng cáo của mình (FTC, 2016).')
c += P('Theo FTC (2016), Lumosity quảng cáo rộng rãi trên truyền hình, radio, email, blog, mạng xã hội, và mua hàng trăm từ khóa quảng cáo trên Google liên quan đến trí nhớ, nhận thức, sa sút trí tuệ và bệnh Alzheimer.')
c += P('FTC cũng cáo buộc công ty không công bố việc một số lời chứng thực trên website được thu thập qua các cuộc thi có giải thưởng lớn, như iPad, gói Lumosity trọn đời và chuyến đi khứ hồi tới San Francisco (FTC, 2016).')

c += H2('Dàn xếp yêu cầu gì?')
c += UL([
    'Công ty và hai người đồng sáng lập phải có bằng chứng khoa học đáng tin cậy trước khi đưa ra tuyên bố về lợi ích cho hiệu suất ngoài đời thực, suy giảm do tuổi tác hay các tình trạng sức khỏe khác.',
    'Án phạt 50 triệu USD được tạm hoãn do tình hình tài chính của công ty, sau khi công ty trả 2 triệu USD cho FTC.',
    'Công ty phải thông báo cho người đăng ký gói tự gia hạn trong giai đoạn 2009 đến 2014 về vụ việc, và cung cấp cách hủy đăng ký dễ dàng.',
])
c += P('Nguồn: FTC (2016).')

c += H2('Khoa học nói gì về game luyện não?')
c += P('Cùng năm 2016, một nhóm nhà tâm lý học do Daniel Simons dẫn đầu công bố tổng quan trên tạp chí <em>Psychological Science in the Public Interest</em>. Theo bản tóm tắt của Hiệp hội Khoa học Tâm lý (APS), kết quả cho thấy (Association for Psychological Science [APS], 2016):')
c += UL([
    'Luyện tập dường như cải thiện kết quả ở chính các bài tập được luyện.',
    'Có ít bằng chứng hơn về cải thiện ở các bài tập gần giống nhưng không hoàn toàn giống.',
    'Có rất ít bằng chứng về cải thiện ở các bài tập khác xa, hoặc cải thiện khả năng nhận thức hằng ngày.',
    'Nhiều nghiên cứu có vấn đề về phương pháp và không tuân theo thực hành tốt nhất trong nghiên cứu.',
])
c += P('Nhóm tác giả khuyến nghị các nghiên cứu sau này cần đăng ký trước, phân nhóm ngẫu nhiên đúng cách, có cỡ mẫu đủ lớn, hiệu chỉnh khi so sánh nhiều lần và công bố xung đột lợi ích (APS, 2016).')
c += P('Điều này khớp với một ví dụ trong hướng dẫn của FTC đã nêu ở bài ' + A('da-chung-minh-lam-sang-nghia-la-gi', '"đã chứng minh lâm sàng" có đáng tin không') + ': kết quả tốt ở bài tập trí nhớ trong phòng thí nghiệm không đủ để quảng cáo "cải thiện trí nhớ" nói chung.')

c += H2('Ở Việt Nam, quy định thế nào?')
c += P('Quảng cáo không đúng hoặc gây nhầm lẫn về chất lượng, công dụng của sản phẩm so với nội dung đã đăng ký, công bố có thể bị phạt từ 80 đến 100 triệu đồng với cá nhân, gấp đôi với tổ chức (Chính phủ, 2026, Điều 50 khoản 5; Điều 6 khoản 3). Với ứng dụng hay trò chơi hứa hẹn lợi ích sức khỏe, người làm truyền thông nên kiểm tra bằng chứng trước khi đưa các tuyên bố này vào quảng cáo.')

c += H2('Câu hỏi thường gặp')
c += H3('Chơi game luyện não có giúp phòng sa sút trí tuệ không?')
c += P('FTC cho rằng Lumosity không có căn cứ khoa học cho tuyên bố này (FTC, 2016). Tổng quan năm 2016 cũng cho thấy có rất ít bằng chứng về lợi ích cho nhận thức hằng ngày (APS, 2016).')
c += H3('Vậy game luyện não có vô ích không?')
c += P('Không hẳn. Người chơi có thể giỏi hơn ở chính trò chơi được luyện (APS, 2016). Điều cần thận trọng là lời hứa rằng lợi ích sẽ lan sang công việc, học tập hay phòng bệnh.')

c += H2('Điều gì nên nhớ?')
c += P('Khi quảng cáo chạm vào nỗi sợ, như mất trí nhớ khi về già, lời hứa càng dễ được tin. Vụ Lumosity cho thấy cần hỏi: sản phẩm giúp giỏi hơn ở trò chơi, hay giỏi hơn ngoài đời thật? Và bằng chứng nào đứng sau lời hứa đó?')
c += GEN_END + REFS([APS, ND87, FTC])

d = dict(slug='game-luyen-nao-lumosity-ftc', title='Game "luyện não": Lumosity và lời hứa chống lão hóa não',
    seo_title='Game luyện não có tác dụng không? Bài học Lumosity',
    meta_desc='Năm 2016, FTC cáo buộc Lumosity quảng cáo không có căn cứ rằng game giúp học tập, làm việc tốt hơn và phòng sa sút trí tuệ. Khoa học nói gì về game luyện não?',
    focus_kw='game luyện não',
    excerpt='Lumosity hứa game giúp não minh mẫn và chống sa sút trí tuệ. FTC cho rằng công ty không có căn cứ. Khoa học nói gì về lợi ích thật của game luyện não?',
    tags=['game luyện não', 'Lumosity', 'sa sút trí tuệ', 'FTC', 'bóc mác y khoa'], content=c, categories=[3, 11],
    date='2026-11-20T16:00:00', cover_alt='Minh họa mẩu quảng cáo "Game luyện não" bị bút đỏ ghi chú "Chơi giỏi game hay giỏi thật?"')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

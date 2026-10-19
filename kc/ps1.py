import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'

WHO = 'World Health Organization. (2025, ngày 30 tháng 6). <em>Social connection linked to improved health and reduced risk of early death</em> [Thông cáo báo chí]. https://www.who.int/news/item/30-06-2025-social-connection-linked-to-improved-heath-and-reduced-risk-of-early-death'
HL = 'Holt-Lunstad, J., Smith, T. B., &amp; Layton, J. B. (2010). Social relationships and mortality risk: A meta-analytic review. <em>PLoS Medicine, 7</em>(7), e1000316. https://doi.org/10.1371/journal.pmed.1000316'

c = ''
c += P('Cô đơn không phải chuyện riêng của người già. Theo Tổ chức Y tế Thế giới (WHO), khoảng 17% đến 21% người từ 13 đến 29 tuổi cho biết cảm thấy cô đơn, và tỉ lệ cao nhất là ở tuổi thiếu niên (World Health Organization [WHO], 2025). Cô đơn kéo dài không chỉ gây buồn bã mà còn liên quan đến nhiều nguy cơ sức khỏe.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'WHO ước tính khoảng 1 trong 6 người trên thế giới bị ảnh hưởng bởi cô đơn.',
    'Cô đơn là cảm giác, còn cô lập xã hội là tình trạng thiếu kết nối khách quan; hai điều này khác nhau.',
    'Người cô đơn có nguy cơ trầm cảm cao gấp đôi, theo WHO.',
    'Kết nối xã hội mạnh gắn với khả năng sống sót cao hơn khoảng 50% (Holt-Lunstad và cộng sự, 2010).',
])
c += H2('Cô đơn khác cô lập xã hội thế nào?')
c += P('WHO (2025) phân biệt hai khái niệm:')
c += UL([
    '<strong>Cô đơn</strong> là cảm giác đau khổ nảy sinh từ khoảng cách giữa mức kết nối xã hội mình mong muốn và mức mình thực sự có.',
    '<strong>Cô lập xã hội</strong> là tình trạng thiếu kết nối xã hội một cách khách quan.',
])
c += P('Vì vậy, một người có thể sống giữa nhiều người, có hàng trăm bạn bè trên mạng mà vẫn thấy cô đơn; ngược lại, một người ít giao tiếp chưa chắc đã cô đơn. Điều quyết định là khoảng cách giữa mong muốn và thực tế.')
c += H2('Người trẻ cô đơn đến mức nào?')
c += P('Theo thông cáo của WHO về báo cáo của Ủy ban về Kết nối xã hội (WHO, 2025):')
c += UL([
    'Khoảng 1 trong 6 người trên thế giới bị ảnh hưởng bởi cô đơn.',
    'Từ 17% đến 21% người 13 đến 29 tuổi cho biết cảm thấy cô đơn, cao nhất ở tuổi thiếu niên.',
    'Khoảng 24% người ở các nước thu nhập thấp cho biết cảm thấy cô đơn.',
])
c += P('Đồng chủ tịch Ủy ban, bà Chido Mpemba, nhận xét rằng ngay cả trong một thế giới kết nối số, nhiều người trẻ vẫn thấy mình một mình (WHO, 2025).')
c += H2('Cô đơn ảnh hưởng đến sức khỏe ra sao?')
c += P('WHO (2025) cho biết cô đơn và cô lập xã hội làm tăng nguy cơ đột quỵ, bệnh tim, đái tháo đường, suy giảm nhận thức và tử vong sớm. Người cô đơn có khả năng bị trầm cảm cao gấp đôi, và cô đơn cũng có thể dẫn đến lo âu. WHO ước tính cô đơn liên quan đến khoảng 871.000 ca tử vong mỗi năm, tức khoảng 100 ca mỗi giờ.')
c += P('Với người trẻ, ảnh hưởng còn thể hiện ở việc học: thiếu niên cảm thấy cô đơn có khả năng đạt điểm hoặc bằng cấp thấp hơn 22% (WHO, 2025).')
c += P('Ở chiều ngược lại, một phân tích tổng hợp 148 nghiên cứu với hơn 300.000 người tham gia cho thấy người có các mối quan hệ xã hội mạnh có khả năng sống sót cao hơn khoảng 50% (Holt-Lunstad và cộng sự, 2010). Nhóm tác giả đánh giá mức ảnh hưởng này tương đương với các yếu tố nguy cơ tử vong đã được biết rõ.')
c += H2('Điều gì khiến người ta cô đơn?')
c += P('WHO (2025) cho biết cô đơn và cô lập xã hội có nhiều nguyên nhân, bao gồm sức khỏe kém, thu nhập và học vấn thấp, sống một mình, hạ tầng cộng đồng và chính sách công chưa phù hợp, và công nghệ số. Báo cáo nhấn mạnh cần thận trọng với tác động của việc dùng màn hình quá mức.')
c += P('Điều này không có nghĩa mạng xã hội luôn xấu. Câu hỏi là công nghệ đang giúp mình gần người khác hơn hay thay thế những kết nối thật. Các bài ' + A('vi-sao-luot-video-ngan-bien-thanh-vai-tieng', 'vì sao lướt video ngắn biến thành vài tiếng') + ' và ' + A('thong-bao-dien-thoai-anh-huong-tap-trung', 'thông báo điện thoại ảnh hưởng tập trung thế nào') + ' bàn thêm về thói quen dùng điện thoại.')
c += H2('Có thể làm gì để bớt cô đơn?')
c += P('WHO (2025) gợi ý những việc nhỏ mỗi người có thể làm:')
c += UL([
    'Chủ động liên lạc với một người bạn.',
    'Cất điện thoại khi đang trò chuyện với người khác.',
    'Chào hỏi hàng xóm.',
    'Tham gia một nhóm sinh hoạt ở địa phương.',
    'Làm tình nguyện.',
])
c += P('WHO cũng kêu gọi chính phủ và cộng đồng nâng cao nhận thức, điều chỉnh chính sách và đầu tư vào hạ tầng xã hội như công viên, thư viện, để kết nối xã hội trở thành ưu tiên y tế công cộng.')
c += P('Nếu cảm giác cô đơn kéo dài, đi kèm buồn bã, mất hứng thú hay khó ngủ, hãy tìm đến chuyên gia tâm lý. Bài ' + A('vi-sao-nam-gioi-ngai-tim-ho-tro-tam-ly', 'vì sao nam giới ngại tìm hỗ trợ tâm lý') + ' bàn về những rào cản thường gặp.')
c += H2('Câu hỏi thường gặp')
c += H3('Có nhiều bạn trên mạng mà vẫn thấy cô đơn có bình thường không?')
c += P('Có thể xảy ra. Theo WHO (2025), cô đơn là khoảng cách giữa kết nối mình mong muốn và kết nối thực có, nên số lượng bạn bè không quyết định tất cả.')
c += H3('Thích ở một mình có phải là cô đơn không?')
c += P('Không nhất thiết. Nếu bạn ở một mình nhưng không thấy thiếu kết nối, đó không phải cô đơn theo định nghĩa của WHO (2025).')
c += H3('Cô đơn có phải là bệnh không?')
c += P('WHO (2025) định nghĩa cô đơn là một cảm giác, không phải một chẩn đoán bệnh. Tuy vậy, cô đơn kéo dài liên quan đến nhiều nguy cơ sức khỏe, nên đáng được quan tâm như một vấn đề sức khỏe (WHO, 2025).')
c += H2('Điều gì nên nhớ?')
c += P('Cô đơn phổ biến ở người trẻ hơn nhiều người nghĩ, và nó ảnh hưởng thật đến sức khỏe. Tin tốt là kết nối có thể bắt đầu từ những việc nhỏ: một tin nhắn, một lời chào, một buổi gặp mặt không có điện thoại. Nếu thấy khó tự vượt qua, tìm hỗ trợ là một lựa chọn mạnh mẽ, không phải yếu đuối.')
c += P('<em>Bài viết mang tính thông tin, không thay thế tư vấn y khoa hoặc tâm lý cho từng cá nhân.</em>')
c += GEN_END + REFS([HL, WHO])

d = dict(slug='co-don-o-nguoi-tre', title='Cô đơn ở người trẻ: phổ biến đến đâu và ảnh hưởng sức khỏe thế nào?', seo_title='Cô đơn ở người trẻ: phổ biến đến đâu, ảnh hưởng thế nào?',
    meta_desc='Cô đơn ở người trẻ phổ biến hơn ta nghĩ: 17% đến 21% người 13 đến 29 tuổi thấy cô đơn, theo WHO. Cô đơn khác cô lập ra sao, ảnh hưởng sức khỏe và cách giảm.',
    focus_kw='cô đơn ở người trẻ', excerpt='Theo WHO, 17% đến 21% người 13 đến 29 tuổi thấy cô đơn. Cô đơn khác cô lập xã hội thế nào, ảnh hưởng sức khỏe ra sao và những việc nhỏ giúp kết nối lại.',
    tags=['cô đơn', 'sức khỏe tâm thần', 'kết nối xã hội', 'người trẻ', 'mạng xã hội'], content=c, categories=[4, 13],
    date='2026-10-29T11:30:00', cover_alt='Minh họa một người ngồi một mình ở đầu ghế dài trong công viên, cầm điện thoại sáng, bên cột đèn ấm')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']))

import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'

BR = 'Brierley, L., Nanni, F., Polka, J. K., Dey, G., Pálfy, M., Fraser, N., &amp; Coates, J. A. (2022). Tracking changes between preprint posting and journal publication during a pandemic. <em>PLOS Biology, 20</em>(2), e3001285. https://doi.org/10.1371/journal.pbio.3001285'
FR = 'Fraser, N., Brierley, L., Dey, G., Polka, J. K., Pálfy, M., Nanni, F., &amp; Coates, J. A. (2021). The evolving role of preprints in the dissemination of COVID-19 research and their impact on the science communication landscape. <em>PLOS Biology, 19</em>(4), e3000959. https://doi.org/10.1371/journal.pbio.3000959'
MR = 'medRxiv. (n.d.). <em>About medRxiv</em>. https://www.medrxiv.org/content/about-medrxiv'
ZE = 'Zeng, L. (2023). Changes in health communication in the age of COVID-19: A study on the dissemination of preprints to the public. <em>Frontiers in Public Health, 11</em>, 1078115. https://doi.org/10.3389/fpubh.2023.1078115'

c = ''
c += P('Preprint (bản thảo tiền in) là bài báo khoa học được tác giả đăng công khai trước khi qua bình duyệt (peer review). Nói ngắn gọn: đây là kết quả nghiên cứu thật, nhưng chưa được các nhà khoa học độc lập kiểm tra. Chính máy chủ preprint y sinh medRxiv khuyến cáo preprint không nên được dùng để định hướng thực hành lâm sàng hay hành vi sức khỏe, và không nên được báo chí đưa tin như thông tin đã được xác lập (medRxiv, n.d.).')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Preprint giúp chia sẻ kết quả nhanh, nhưng chưa qua bình duyệt (medRxiv, n.d.).',
    'Trong đại dịch COVID-19, preprint chiếm khoảng 25% các công bố khoa học về COVID-19 (Fraser và cộng sự, 2021).',
    'Phần lớn preprint khi được đăng chính thức không thay đổi kết luận về bản chất, nhưng khoảng 17% bản tóm tắt COVID-19 có thay đổi trong kết luận (Brierley và cộng sự, 2022).',
    'Gần một nửa bài báo đưa tin về preprint không cho người đọc biết đó là preprint (Zeng, 2023).',
])

c += H2('Preprint là gì và khác bài báo đã bình duyệt thế nào?')
c += P('Thông thường, một nghiên cứu được gửi đến tạp chí, các chuyên gia cùng lĩnh vực đánh giá, tác giả chỉnh sửa, rồi bài mới được đăng. Quy trình này có thể mất nhiều tháng. Preprint đi tắt: tác giả đăng bản thảo lên các máy chủ như medRxiv, bioRxiv để cộng đồng đọc và góp ý ngay.')
c += P('Máy chủ preprint vẫn có sàng lọc, nhưng chỉ ở mức cơ bản. medRxiv cho biết mọi bài đều qua sàng lọc nội dung xúc phạm hoặc phi khoa học, nội dung có thể gây nguy cơ sức khỏe và kiểm tra đạo văn; việc đăng bài không có nghĩa là máy chủ xác nhận nghiên cứu đó (medRxiv, n.d.). Sàng lọc này khác với bình duyệt, vốn đánh giá phương pháp, dữ liệu và kết luận. Bài ' + '<a href="https://dykhoa.com/blog/thuat-ngu/binh-duyet-mo-open-peer-review/">bình duyệt mở</a>' + ' giới thiệu thêm về các hình thức bình duyệt.')

c += H2('Vì sao preprint trở nên quan trọng?')
c += P('Đại dịch COVID-19 là bước ngoặt. Đến cuối tháng 10/2020, có 30.260 preprint trên tổng số hơn 125.000 công bố về COVID-19, tức khoảng 25% (Fraser và cộng sự, 2021). Preprint COVID-19 được truy cập, trích dẫn và chia sẻ nhiều hơn preprint về chủ đề khác. Đáng chú ý, 28,7% preprint COVID-19 xuất hiện trong ít nhất một bài báo, so với 1,0% preprint không liên quan COVID-19 (Fraser và cộng sự, 2021).')
c += P('Lợi ích là rõ ràng: khi dịch bệnh lan nhanh, chờ nhiều tháng để bình duyệt có thể quá chậm. Nhóm tác giả đánh giá preprint đã đóng vai trò không thể thiếu trong đại dịch (Fraser và cộng sự, 2021).')

c += H2('Preprint có đáng tin không?')
c += P('Câu trả lời ngắn: thường đáng tham khảo, nhưng chưa nên xem là kết luận cuối cùng.')
c += P('Một nghiên cứu so sánh preprint với bản đăng chính thức trên tạp chí cho thấy số hình và bảng thay đổi rất ít. Kết luận trong phần tóm tắt thay đổi ở 7,2% bài không liên quan COVID-19 và 17,2% bài về COVID-19, dù phần lớn thay đổi này không làm đổi kết luận về bản chất (Brierley và cộng sự, 2022).')
c += P('Như vậy, đa số preprint giữ nguyên nội dung chính sau bình duyệt. Nhưng "đa số" không phải "tất cả". Với preprint COVID-19, cứ khoảng 6 bài thì có 1 bài thay đổi kết luận ở phần tóm tắt. Ngoài ra, nghiên cứu này chỉ xét các preprint sau đó đã được đăng chính thức; những bài không bao giờ được đăng không nằm trong phép so sánh.')

c += H2('Vấn đề nằm ở đâu khi preprint đến với công chúng?')
c += P('Rủi ro lớn nhất không nằm ở preprint mà ở cách nó được kể lại. Một nghiên cứu phân tích 468 bài báo đưa tin về preprint trong đại dịch cho thấy (Zeng, 2023):')
c += UL([
    '49% bài báo không có bất kỳ dấu hiệu nào cho biết đây là preprint, nên người đọc dễ hiểu nhầm là nghiên cứu đã được bình duyệt.',
    'Chỉ 15% bài báo nói rõ nghiên cứu chưa qua bình duyệt.',
    'Báo chí truyền thống bỏ qua thông tin này nhiều hơn báo điện tử thuần số (56% so với 41% bài không có dấu hiệu preprint).',
])
c += P('Khi người đọc không biết một kết quả còn sơ bộ, họ có thể ra quyết định sức khỏe dựa trên nó, hoặc mất niềm tin vào khoa học khi kết quả sau đó thay đổi. Bài ' + A('vi-sao-tin-nghien-cuu-moi-hay-bi-thoi-phong', 'vì sao tin nghiên cứu mới hay bị thổi phồng') + ' phân tích thêm vấn đề này.')

c += H2('Làm sao nhận biết và đọc preprint đúng cách?')
c += UL([
    '<strong>Xem nguồn đăng.</strong> Đường dẫn từ medRxiv, bioRxiv, arXiv, SSRN, Research Square hoặc có chữ "preprint" là dấu hiệu bài chưa qua bình duyệt.',
    '<strong>Tìm dòng cảnh báo.</strong> Các máy chủ preprint y sinh thường ghi rõ bài chưa được bình duyệt (medRxiv, n.d.).',
    '<strong>Kiểm tra bài đã được đăng chính thức chưa.</strong> Nhiều máy chủ preprint gắn đường dẫn đến bản đăng trên tạp chí nếu có.',
    '<strong>Xem nó có khớp với các bằng chứng khác không.</strong> Một preprint đi ngược lại nhiều nghiên cứu trước đó cần được xem xét thận trọng hơn.',
    '<strong>Không đổi hành vi sức khỏe chỉ dựa trên một preprint.</strong> Đây cũng là khuyến cáo của chính medRxiv (medRxiv, n.d.).',
])
c += P('Bài trụ cột ' + A('thong-tin-khoa-hoc-tren-mang-co-dang-tin', 'làm sao biết thông tin khoa học trên mạng có đáng tin') + ' tổng hợp các bước kiểm tra chung, và bài ' + A('nghien-cuu-it-nguoi-tham-gia-tin-duoc-den-dau', 'nghiên cứu ít người tham gia tin được đến đâu') + ' giúp đánh giá cỡ mẫu.')

c += H2('Người làm truyền thông nên đưa tin về preprint thế nào?')
c += P('Dựa trên các phát hiện của Zeng (2023) và khuyến cáo của medRxiv (n.d.), người viết có thể:')
c += UL([
    'Ghi rõ ngay trong bài rằng đây là preprint, chưa qua bình duyệt.',
    'Giải thích ngắn gọn bình duyệt là gì và vì sao kết quả có thể thay đổi.',
    'Dùng ngôn ngữ thận trọng như "kết quả sơ bộ", "gợi ý", tránh "chứng minh", "phát hiện đột phá".',
    'Hỏi ý kiến chuyên gia độc lập không tham gia nghiên cứu.',
    'Cập nhật bài khi preprint được đăng chính thức hoặc bị rút.',
])

c += H2('Câu hỏi thường gặp')
c += H3('Preprint có phải là tin giả không?')
c += P('Không. Preprint là kết quả nghiên cứu thật của các nhà khoa học, chỉ là chưa qua bình duyệt. Vấn đề chỉ nảy sinh khi preprint bị trình bày như kết luận đã chắc chắn (Zeng, 2023).')
c += H3('Người học có nên trích dẫn preprint không?')
c += P('Có thể, nếu ghi rõ đây là preprint và ưu tiên bản đã đăng chính thức khi có. Với các quyết định quan trọng, nên dựa vào bằng chứng đã qua bình duyệt và tổng hợp từ nhiều nghiên cứu.')
c += H3('Đã qua bình duyệt thì chắc chắn đúng?')
c += P('Không. Bình duyệt giúp phát hiện nhiều lỗi nhưng không đảm bảo kết quả đúng tuyệt đối. Bài ' + A('mot-nghien-cuu-moi-co-du-de-ket-luan', 'một nghiên cứu mới có đủ để kết luận') + ' giải thích vì sao cần nhìn vào tổng thể bằng chứng.')

c += H2('Điều gì nên nhớ?')
c += P('Preprint giúp khoa học chia sẻ kết quả nhanh hơn, đặc biệt trong khủng hoảng. Đa số giữ được kết luận chính sau bình duyệt, nhưng vẫn có một phần thay đổi. Khi đọc hoặc chia sẻ một preprint, hãy nhớ một câu: kết quả thật, nhưng còn sơ bộ.')
c += GEN_END + REFS([BR, FR, MR, ZE])

d = dict(slug='preprint-la-gi-co-dang-tin-khong', title='Preprint là gì? Có đáng tin không và đọc thế nào cho đúng?',
    seo_title='Preprint là gì? Có đáng tin không, đọc thế nào cho đúng?',
    meta_desc='Preprint là bài báo khoa học chưa qua bình duyệt. Preprint có đáng tin không, vì sao báo chí hay đưa tin sai về preprint và cách đọc, chia sẻ cho đúng.',
    focus_kw='preprint là gì',
    excerpt='Preprint là nghiên cứu thật nhưng chưa qua bình duyệt. Đa số giữ kết luận khi đăng chính thức, nhưng gần một nửa bài báo không cho người đọc biết đó là preprint.',
    tags=['preprint', 'bình duyệt', 'thông tin khoa học', 'truyền thông khoa học', 'kiểm chứng'], content=c, categories=[3, 9],
    date='2026-10-29T16:00:00', cover_alt='Minh họa bản thảo nghiên cứu có con dấu PREPRINT bên cạnh kính lúp và một tạp chí khoa học')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

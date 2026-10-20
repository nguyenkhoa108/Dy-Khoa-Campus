import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'

RA = 'Wellcome Trust. (2026a). <em>Wellcome Global Monitor 2026: Trust in science under pressure</em>. https://doi.org/10.21955/wellcomeopenres.1115455.1'
RB = 'Wellcome Trust. (2026b, ngày 10 tháng 10). <em>Wellcome Global Monitor 2026: Trust in science has declined worldwide, but the picture varies sharply by region</em>. https://wellcome.org/insights/articles/wellcome-global-monitor-2026-trust-science-has-declined-worldwide-picture-varies'
RC = 'Wellcome Trust. (2026c). <em>Wellcome Global Monitor 2026 factsheet: South-eastern Asia</em> [Tờ thông tin]. https://cms.wellcome.org/sites/default/files/2026-10/Wellcome%20Global%20Monitor%202026%20Factsheet%20Region%20South-eastern%20Asia.pdf'

c = ''
c += P('Niềm tin vào khoa học trên thế giới đang giảm. Theo Wellcome Global Monitor 2026, khảo sát toàn cầu về thái độ của công chúng với khoa học và sức khỏe, tỉ lệ người tin tưởng khoa học ở mức "khá" hoặc "rất nhiều" đã giảm từ 80% năm 2020 xuống 72% năm 2025, thấp hơn cả mức 77% của năm 2018 (Wellcome Trust, 2026a). Sự sụt giảm rõ nhất ở nhóm khó khăn về thu nhập và ở những nơi người dân ít tin vào thể chế. Với người làm truyền thông khoa học, đây là tín hiệu cần thay đổi cách tiếp cận.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Khảo sát hơn 140.000 người tại 140 quốc gia năm 2025, do Gallup thực hiện trong khuôn khổ Gallup World Poll (Wellcome Trust, 2026a).',
    'Tỉ lệ tin khoa học giảm từ 80% (2020) xuống 72% (2025); tỉ lệ ít hoặc không tin tăng từ 13% lên 19%.',
    'Tỉ lệ rất tin tưởng các nhà khoa học giảm từ 43% xuống 32%, mức giảm lớn nhất trong các nhóm được hỏi.',
    'Người sống thoải mái rất tin khoa học nhiều gần gấp đôi người gặp khó khăn về thu nhập (39% so với 20%).',
    'Ở khu vực Đông Nam Á, gồm cả Việt Nam, tỉ lệ tin khoa học giảm từ 78% (2020) xuống 70% (2025) (Wellcome Trust, 2026c).',
])

c += H2('Wellcome Global Monitor 2026 là gì?')
c += P('Wellcome Global Monitor là khảo sát định kỳ của quỹ Wellcome (Anh) về cách công chúng toàn cầu nhìn nhận khoa học và sức khỏe. Đợt 2026 được thực hiện năm 2025 tại 140 quốc gia với hơn 140.000 người tham gia, qua phỏng vấn trực tiếp, điện thoại và trực tuyến trên mẫu đại diện quốc gia. Gallup thực hiện khảo sát, còn Ipsos phụ trách phân tích và viết báo cáo (Wellcome Trust, 2026a).')
c += P('Để so sánh theo thời gian, báo cáo chỉ dùng 108 quốc gia có mặt trong cả ba đợt 2018, 2020 và 2025. Báo cáo cũng lưu ý rằng ở Trung Quốc, phương pháp thu thập dữ liệu đã thay đổi qua các đợt, nên cần thận trọng khi đọc xu hướng chung (Wellcome Trust, 2026a).')

c += H2('Niềm tin vào khoa học thay đổi ra sao?')
c += TABLE(['Chỉ số', '2018', '2020', '2025'], [
    ['Tin khoa học "khá" hoặc "rất nhiều" (toàn cầu)', '77%', '80%', '72%'],
    ['Ít hoặc không tin khoa học (toàn cầu)', '13%', '13%', '19%'],
    ['Rất tin tưởng các nhà khoa học (toàn cầu)', '34%', '43%', '32%'],
    ['Tin khoa học "khá" hoặc "rất nhiều" (Đông Nam Á)', '68%', '78%', '70%'],
])
c += P('Nguồn: Wellcome Trust (2026a) cho số liệu toàn cầu; Wellcome Trust (2026c) cho số liệu Đông Nam Á, tính trên 8 quốc gia có mặt trong cả ba đợt.')
c += P('Có thể thấy "hiệu ứng đại dịch": niềm tin tăng mạnh năm 2020, rồi giảm xuống dưới mức trước đại dịch. Tuy nhiên, sự sụt giảm không đồng đều. Niềm tin giảm xuống dưới mức 2018 ở năm khu vực, gồm châu Phi cận Sahara, Trung Á, Tây Á, Đông Á, Úc và New Zealand; trong khi Đông Nam Á thuộc nhóm bảy khu vực có mức niềm tin gần với năm 2018 (Wellcome Trust, 2026a). Dù vậy, tỉ lệ người "rất tin" khoa học giảm ở cả 14 khu vực.')

c += H2('Ai đang mất niềm tin vào khoa học?')
c += H3('Người gặp khó khăn về thu nhập')
c += P('Trong số người đang sống thoải mái, 39% rất tin khoa học; con số này chỉ là 20% ở người đang gặp khó khăn để trang trải cuộc sống. Khoảng cách này đã nới rộng từ 13 lên 19 điểm phần trăm kể từ năm 2018 (Wellcome Trust, 2026a).')
c += H3('Những nơi người dân ít tin vào thể chế')
c += P('Ở những quốc gia có niềm tin vào khoa học thấp hơn, người dân cũng ít tin vào các thể chế quốc gia, ít tin chính phủ hơn và cảm nhận tham nhũng cao hơn. Mức bất bình đẳng kinh tế có tương quan nghịch ở mức vừa phải với niềm tin vào khoa học: nước càng bất bình đẳng, niềm tin vào khoa học càng có xu hướng thấp (Wellcome Trust, 2026a).')
c += P('Cần lưu ý, đây là mối tương quan, không phải quan hệ nhân quả đã được chứng minh. Bài ' + A('tuong-quan-va-nhan-qua-khac-nhau-the-nao', 'tương quan và nhân quả khác nhau thế nào') + ' giải thích vì sao.')
c += H3('Trải nghiệm với hệ thống y tế')
c += P('Trên toàn cầu, 26% người rất tin khoa học. Nhưng trong nhóm rất tin tưởng bệnh viện, phòng khám ở nước mình, tỉ lệ này lên đến 43% (Wellcome Trust, 2026a). Trải nghiệm thực tế với y tế dường như gắn chặt với niềm tin vào khoa học.')

c += H2('Khoa học có mang lại lợi ích cho "người như tôi"?')
c += P('Một phát hiện đáng chú ý: 81% người được hỏi cho rằng công việc của các nhà khoa học mang lại lợi ích cho những người như họ, nhưng chỉ 37% nghĩ khoa học mang lại lợi ích cho phần lớn người dân trong nước, và 20% cho rằng chỉ rất ít người được hưởng lợi (Wellcome Trust, 2026a). Người có ít nhất một mức độ tin tưởng khoa học có khả năng nói khoa học mang lại lợi ích cho phần lớn người dân cao hơn 23 điểm phần trăm.')
c += P('Nói cách khác, nhiều người không nghi ngờ bản thân khoa học, mà nghi ngờ việc lợi ích của khoa học có được chia đều hay không.')

c += H2('Truyền thông khoa học nên làm gì?')
c += P('Báo cáo không đưa ra khuyến nghị chính thức, nhưng phần mở đầu gợi ý các nhà khoa học nên phân biệt rõ điều bằng chứng cho thấy với hành động cần làm, vì hành động luôn gắn với giá trị và sự đánh đổi; đồng thời khoa học cần đáng tin cậy, cởi mở và gắn với đời sống để giành được niềm tin của những người có góc nhìn khác nhau (Wellcome Trust, 2026a).')
c += P('Từ các phát hiện trên, người viết đề xuất một số hướng cho truyền thông khoa học, đặc biệt ở các nước đang phát triển như Việt Nam:')
c += UL([
    '<strong>Gắn khoa học với lợi ích cụ thể</strong> của nhóm thu nhập thấp: y tế cơ sở, nước sạch, nông nghiệp, phòng bệnh, thay vì chỉ nói về thành tựu.',
    '<strong>Làm việc qua những người công chúng đã tin</strong>, như bác sĩ, điều dưỡng, nhân viên y tế cơ sở, vì trải nghiệm tốt với hệ thống y tế đi kèm niềm tin cao hơn vào khoa học.',
    '<strong>Tách bạch bằng chứng và chính sách</strong>: nói rõ khoa học cho thấy gì, và đâu là lựa chọn có đánh đổi.',
    '<strong>Minh bạch về sự không chắc chắn</strong>, để niềm tin không sụp đổ khi kết luận được cập nhật. Bài ' + A('vi-sao-nha-khoa-hoc-hay-noi-chua-chac-chan', 'vì sao nhà khoa học hay nói "chưa chắc chắn"') + ' bàn sâu hơn.',
])
c += P('Bài ' + A('niem-tin-the-che-epistemic-trust-khoa-hoc', 'niềm tin tri thức (epistemic trust) vào khoa học') + ' bàn thêm về nền tảng lý thuyết của niềm tin vào khoa học.')

c += H2('Câu hỏi thường gặp')
c += H3('Có số liệu riêng cho Việt Nam không?')
c += P('Việt Nam có trong mẫu khảo sát khu vực Đông Nam Á năm 2025, nhưng tờ thông tin khu vực chỉ công bố số liệu chung của khu vực, không có số liệu riêng từng nước (Wellcome Trust, 2026c). Bộ dữ liệu công khai của Wellcome có thể cho phép phân tích sâu hơn.')
c += H3('Con số 72% và 70% khác nhau thế nào?')
c += P('Con số 72% là tỉ lệ tin khoa học năm 2025 tính trên 108 quốc gia có mặt trong cả ba đợt khảo sát, dùng để so sánh xu hướng (Wellcome Trust, 2026a). Tờ thông tin khu vực Đông Nam Á ghi mức toàn cầu là 26% "rất tin" và 44% "khá tin", tức 70% (Wellcome Trust, 2026c). Khi trích dẫn, nên ghi rõ con số nào và phạm vi nào.')
c += H3('Niềm tin giảm có phải do đại dịch?')
c += P('Báo cáo cho thấy niềm tin tăng trong đại dịch rồi giảm xuống dưới mức trước đại dịch, nhưng không kết luận nguyên nhân. Các yếu tố đi kèm gồm thu nhập, niềm tin vào thể chế, cảm nhận tham nhũng và bất bình đẳng (Wellcome Trust, 2026a).')

c += H2('Điều gì nên nhớ?')
c += P('Niềm tin vào khoa học vẫn ở mức cao, khoảng 7 trên 10 người, nhưng đang giảm, và giảm nhanh hơn ở những người cảm thấy bị bỏ lại phía sau. Truyền thông khoa học không thể chỉ nói đúng; nó cần cho thấy khoa học mang lại lợi ích cho ai, được chia sẻ công bằng ra sao, và đi qua những kênh mà người dân đã tin.')
c += GEN_END + REFS([RA, RB, RC])

d = dict(slug='wellcome-global-monitor-2026-niem-tin-vao-khoa-hoc', title='Wellcome Global Monitor 2026: niềm tin vào khoa học giảm, truyền thông khoa học cần làm gì?',
    seo_title='Niềm tin vào khoa học giảm: Wellcome Global Monitor 2026',
    meta_desc='Wellcome Global Monitor 2026: tỉ lệ tin khoa học giảm từ 80% xuống 72%, giảm mạnh ở nhóm thu nhập thấp. Số liệu Đông Nam Á và gợi ý cho truyền thông khoa học.',
    focus_kw='niềm tin vào khoa học',
    excerpt='Khảo sát 140.000 người tại 140 nước: niềm tin vào khoa học giảm từ 80% năm 2020 xuống 72% năm 2025. Ai đang mất niềm tin và truyền thông khoa học nên làm gì.',
    tags=['niềm tin vào khoa học', 'Wellcome Global Monitor', 'truyền thông khoa học', 'niềm tin công chúng', 'bất bình đẳng'], content=c, categories=[3, 9],
    date='2026-10-21T13:00:00', cover_alt='Minh họa biểu đồ cột về niềm tin vào khoa học giảm dần, bên cạnh quả địa cầu và kính hiển vi')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

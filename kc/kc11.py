import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'

CK = 'Cook, J., Lewandowsky, S., &amp; Ecker, U. K. H. (2017). Neutralizing misinformation through inoculation: Exposing misleading argumentation techniques reduces their influence. <em>PLOS ONE, 12</em>(5), e0175799. https://doi.org/10.1371/journal.pone.0175799'
PEW = 'Stocking, G., Widjaya, R., Lieb, A., Radde, K., Smith, A., &amp; Yam, E. (2026, ngày 7 tháng 10). <em>Which health and wellness influencers talk about medical topics? Mostly healthcare professionals</em>. Pew Research Center. https://www.pewresearch.org/data-labs/2026/10/07/which-health-and-wellness-influencers-talk-about-medical-topics-mostly-healthcare-professionals/'

c = ''
c += P('Một "chuyên gia" trên mạng đáng tin khi họ có chuyên môn thật, đúng lĩnh vực đang nói, và đưa ra được bằng chứng cho tuyên bố của mình. Thiếu một trong ba điều này, danh xưng "chuyên gia", "bác sĩ" hay "tiến sĩ" chưa đủ để tin. Nghiên cứu về thông tin sai lệch còn chỉ ra một chiến thuật phổ biến: dùng những người trông như có chuyên môn nhưng thực ra không phải chuyên gia trong lĩnh vực đó để gieo nghi ngờ, gọi là chiến thuật "chuyên gia giả" (Cook và cộng sự, 2017).')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Một khảo sát 6.334 người có ảnh hưởng về sức khỏe cho thấy 16% không mô tả bất kỳ chuyên môn nào trong phần giới thiệu (Stocking và cộng sự, 2026).',
    'Chỉ 9% bài đăng của nhóm này dẫn nguồn bên ngoài khi đưa ra tuyên bố sức khỏe (Stocking và cộng sự, 2026).',
    'Có bằng cấp chưa đủ: cần đúng lĩnh vực và có bằng chứng.',
    'Biết trước về chiến thuật "chuyên gia giả" giúp giảm ảnh hưởng của thông tin sai (Cook và cộng sự, 2017).',
])

c += H2('Vì sao cần kiểm tra "chuyên gia" trên mạng?')
c += P('Mạng xã hội cho phép bất kỳ ai tự giới thiệu mình là chuyên gia. Trung tâm Nghiên cứu Pew phân tích 535.512 bài đăng trên Instagram, TikTok và YouTube của 6.334 người có ảnh hưởng về sức khỏe từ tháng 2 đến tháng 4/2026 (Stocking và cộng sự, 2026). Một số kết quả đáng chú ý:')
c += UL([
    'Khoảng 16% không mô tả bất kỳ nền tảng hay chuyên môn nào trong phần giới thiệu.',
    'Chỉ 9% bài đăng dẫn nguồn bên ngoài khi đưa ra tuyên bố về sức khỏe; nhóm nhà nghiên cứu làm điều này nhiều nhất, ở 30% bài đăng.',
    'Với các chủ đề y khoa, người đăng nhiều nhất là nhân viên y tế; nhóm không có chuyên môn chỉ dành khoảng 1/10 bài đăng cho bệnh lý.',
])
c += P('Như vậy, bức tranh không hoàn toàn tiêu cực: phần lớn người nói về bệnh lý có chuyên môn y tế. Nhưng cần lưu ý, chuyên môn trong nghiên cứu này là do người có ảnh hưởng tự mô tả, chưa được kiểm chứng. Và rất ít bài đăng cho người xem cơ hội tự kiểm tra bằng chứng.')

c += H2('Chiến thuật "chuyên gia giả" hoạt động thế nào?')
c += P('Cook và cộng sự (2017) mô tả "chuyên gia giả" là những người trông như có chuyên môn liên quan nhưng thực ra hiếm khi có. Ví dụ trong nghiên cứu là "Kiến nghị Oregon", một danh sách hơn 31.000 người có bằng khoa học ký tên phản đối việc con người gây biến đổi khí hậu. Con số nghe rất lớn, nhưng điều kiện ký chỉ là có bằng cử nhân khoa học, và 31.000 người này chỉ chiếm khoảng 0,3% trong 10,6 triệu người tốt nghiệp ngành khoa học ở Mỹ.')
c += P('Kết quả thí nghiệm cho thấy thông điệp này làm giảm niềm tin rằng giới khoa học đồng thuận. Tuy nhiên, khi người tham gia được giải thích trước về kỹ thuật "chuyên gia giả", tác động tiêu cực đó gần như bị vô hiệu hóa (Cook và cộng sự, 2017). Đây là nền tảng của ' + A('tiem-phong-tam-ly-psychological-inoculation-tin-gia-khoa-hoc', 'tiêm phòng tâm lý') + ' trước tin giả khoa học.')

c += H2('Năm câu hỏi để kiểm tra một "chuyên gia"')
c += P('Các câu hỏi dưới đây do người viết tổng hợp từ các nghiên cứu trên, dùng như một công cụ thực hành:')
c += H3('1. Họ là ai, làm việc ở đâu?')
c += P('Tìm tên đầy đủ, nơi công tác và vị trí hiện tại. Một chuyên gia thật thường có thông tin này rõ ràng và kiểm chứng được qua trang của cơ quan, bệnh viện hoặc trường đại học.')
c += H3('2. Chuyên môn có đúng lĩnh vực đang nói không?')
c += P('Một tiến sĩ vật lý không phải là chuyên gia dinh dưỡng; một bác sĩ da liễu chưa chắc là người phù hợp để nói về vắc xin. Đây chính là điểm mấu chốt của chiến thuật "chuyên gia giả": dùng bằng cấp ở lĩnh vực này để tạo uy tín cho lĩnh vực khác (Cook và cộng sự, 2017).')
c += H3('3. Họ có dẫn nguồn không?')
c += P('Chuyên gia đáng tin thường cho biết tuyên bố của mình dựa trên nghiên cứu hoặc hướng dẫn nào. Thực tế, chỉ 9% bài đăng của người có ảnh hưởng về sức khỏe làm điều này (Stocking và cộng sự, 2026), nên một bài có dẫn nguồn rõ ràng là dấu hiệu tốt.')
c += H3('4. Ý kiến có khớp với đồng thuận khoa học không?')
c += P('Một người đi ngược lại hầu hết các chuyên gia khác cần đưa ra bằng chứng mạnh hơn bình thường. Nếu họ chỉ nói "giới y khoa đang che giấu", đó là dấu hiệu cần thận trọng. Bài ' + A('thong-tin-khoa-hoc-tren-mang-co-dang-tin', 'làm sao biết thông tin khoa học trên mạng có đáng tin') + ' hướng dẫn cách đối chiếu.')
c += H3('5. Họ có lợi ích gì từ lời khuyên này không?')
c += P('Hỏi xem người đó có đang bán sản phẩm, khóa học hay nhận tài trợ liên quan không. Có lợi ích không có nghĩa là sai, nhưng là lý do để kiểm tra kỹ hơn. Bài ' + A('nghien-cuu-do-doanh-nghiep-tai-tro-co-dang-tin', 'nghiên cứu do doanh nghiệp tài trợ có đáng tin') + ' phân tích vấn đề xung đột lợi ích.')

c += H2('Câu hỏi thường gặp')
c += H3('Có danh xưng "bác sĩ" là đủ tin chưa?')
c += P('Chưa đủ. Cần xem họ có đúng chuyên khoa với chủ đề đang nói và có dẫn bằng chứng không. Danh xưng trên mạng xã hội thường do người dùng tự mô tả (Stocking và cộng sự, 2026).')
c += H3('Người không có bằng cấp thì không nên nghe?')
c += P('Không hẳn. Người bệnh chia sẻ trải nghiệm cá nhân có giá trị riêng, miễn là họ nói rõ đó là trải nghiệm, không phải lời khuyên y khoa. Vấn đề là khi trải nghiệm được trình bày như bằng chứng chung cho mọi người.')
c += H3('Nhiều chuyên gia cùng ký tên thì có đáng tin hơn?')
c += P('Không nhất thiết. Ví dụ Kiến nghị Oregon cho thấy một danh sách dài vẫn có thể gây hiểu lầm nếu người ký không thuộc đúng lĩnh vực (Cook và cộng sự, 2017). Điều quan trọng là ai ký và họ đại diện cho bao nhiêu phần giới chuyên môn.')

c += H2('Điều gì nên nhớ?')
c += P('Danh xưng chuyên gia là điểm khởi đầu, không phải điểm kết thúc. Hãy hỏi: họ là ai, có đúng lĩnh vực không, có dẫn nguồn không, có khớp với đồng thuận khoa học không, và họ được lợi gì. Bài ' + A('nguoi-noi-tieng-noi-ve-khoa-hoc-nen-tin-den-dau', 'người nổi tiếng nói về khoa học nên tin đến đâu') + ' bàn thêm về những người có ảnh hưởng không phải chuyên gia.')
c += GEN_END + REFS([CK, PEW])

d = dict(slug='kiem-tra-chuyen-gia-tren-mang', title='Làm sao kiểm tra một "chuyên gia" trên mạng có đáng tin không?',
    seo_title='Kiểm tra "chuyên gia" trên mạng: 5 câu hỏi cần hỏi',
    meta_desc='Làm sao biết một chuyên gia trên mạng có đáng tin? Chiến thuật "chuyên gia giả", số liệu từ Pew Research về người có ảnh hưởng sức khỏe và 5 câu hỏi kiểm tra.',
    focus_kw='chuyên gia trên mạng',
    excerpt='Có danh xưng "bác sĩ", "tiến sĩ" chưa đủ để tin. Chiến thuật "chuyên gia giả" hoạt động thế nào và 5 câu hỏi giúp kiểm tra một chuyên gia trên mạng.',
    tags=['chuyên gia', 'thông tin khoa học', 'người có ảnh hưởng', 'tin giả', 'kiểm chứng'], content=c, categories=[3, 9],
    date='2026-10-31T16:00:00', cover_alt='Minh họa hồ sơ chuyên gia trên điện thoại được soi qua kính lúp, bên cạnh danh sách kiểm tra')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

import json, re, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nhatky.py')).read().split('posts = []')[0])
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
c = ''
c += P('Báo chí khoa học ở Việt Nam đang chịu sức ép từ nhiều phía cùng lúc: số phóng viên chuyên sâu rất ít, tòa soạn ưu tiên tin "dùng được ngay", lương thưởng gắn với lượt xem, chuẩn mực đạo đức chưa chặt, khó tiếp cận thông tin và nhà khoa học còn ngại hợp tác. Đó là bức tranh từ một nghiên cứu phỏng vấn 40 nhà báo khoa học Việt Nam trong gần một thập kỷ (Tran &amp; Nguyen, 2023).')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Nghiên cứu phỏng vấn sâu 40 nhà báo khoa học Việt Nam qua ba đợt, từ năm 2012 đến 2020.',
    'Rào cản nằm ở cả ba tầng: cá nhân người làm báo, tòa soạn và môi trường xã hội.',
    'Những phóng viên được đào tạo và hướng dẫn bài bản cho thấy tư duy nghề nghiệp vững hơn.',
    'Đây là cảm nhận của một nhóm nhỏ, chưa thể khái quát cho toàn bộ báo chí Việt Nam.',
])
c += H2('Nghiên cứu này được thực hiện thế nào?')
c += P('Tran và Nguyen (2023) phỏng vấn sâu 40 nhà báo làm mảng khoa học qua ba đợt: năm 2012 đến 2013, năm 2017 đến 2018 và tháng 7 năm 2020 (đợt cuối tập trung vào đưa tin Covid-19). Khoảng 70% người tham gia làm việc ở báo in, số còn lại ở truyền hình, báo điện tử và các cơ quan kết hợp. Không phải ai cũng được giao chính thức làm phóng viên hay biên tập viên khoa học.')
c += H2('Những rào cản nào được nêu ra?')
c += P('Nhóm tác giả gom các trở ngại thành nhiều nhóm (Tran &amp; Nguyen, 2023):')
c += UL([
    '<strong>Kỳ vọng cao nhưng lực lượng mỏng:</strong> nhà báo xem báo chí khoa học có vai trò "gác cổng", phổ biến và giám sát khoa học, nhưng phóng viên chuyên sâu rất hiếm; một biên tập viên ở TP.HCM cho biết số phóng viên khoa học chuyên sâu chỉ dừng ở "khoảng mười" người trong một thập kỷ.',
    '<strong>Đưa tin nông và dễ thổi phồng:</strong> nhiều bài chỉ dừng ở mức thông báo, ít phân tích; tin Covid-19 nghiêng về số ca, số tử vong hơn là giải thích khoa học.',
    '<strong>Văn hóa tòa soạn chưa thân thiện với khoa học:</strong> khoa học ít được đầu tư, khối lượng việc lớn, và cách trả nhuận bút theo lượt xem khiến người viết khoa học thu nhập thấp hơn, dễ bị đẩy sang nội dung giật gân.',
    '<strong>Chuẩn mực đạo đức lỏng:</strong> có hiện tượng nhận tiền hoặc "hợp đồng truyền thông" để đưa tin tích cực; nghiên cứu nêu một vụ năm 2016, khi một khảo sát về an toàn thực phẩm được hơn 50 cơ quan báo chí lan truyền trước khi bị phát hiện là mẫu không đại diện và có tài trợ.',
    '<strong>Khó tiếp cận thông tin:</strong> cơ quan chức năng thường yêu cầu gửi trước câu hỏi, một số tài liệu như báo cáo đánh giá tác động môi trường khó tiếp cận.',
    '<strong>Nhà khoa học ngại hợp tác:</strong> nhiều nhà khoa học không thấy giá trị của việc truyền thông, sợ bị đưa tin sai, hoặc vướng quy định về người phát ngôn.',
])
c += H2('Vì sao nhà khoa học cũng là một phần của vấn đề?')
c += P('Vì báo chí khoa học cần nguồn tin chuyên môn sẵn sàng giải thích. Ở phía nhà khoa học, một khảo sát 70 nhà nghiên cứu y sinh cho thấy rào cản lớn nhất khi tham gia truyền thông với công chúng là thiếu năng lực (78,6%), thiếu hỗ trợ (70%) và thiếu thời gian (52,9%); 71,4% muốn được tập huấn kỹ năng truyền thông khoa học (Tran Dong Thai và cộng sự, 2023). Nói cách khác, cả nhà báo lẫn nhà khoa học đều cần thêm kỹ năng để gặp nhau ở giữa. Bài ' + A('nha-khoa-hoc-co-can-hoc-truyen-thong', 'Nhà khoa học có cần học truyền thông không?') + ' bàn kỹ hơn về phía nhà khoa học.')
c += H2('Có lối ra nào không?')
c += P('Nghiên cứu ghi nhận những phóng viên được đào tạo và hướng dẫn bài bản trong một dự án quốc tế có tư duy nghề nghiệp vững hơn và có những bài điều tra đáng chú ý (Tran &amp; Nguyen, 2023). Nhóm tác giả đề xuất các tổ chức quốc tế, nhà tài trợ nghiên cứu và hiệp hội nghề nghiệp phối hợp để có giải pháp lâu dài, thay vì các khóa ngắn hạn rời rạc.')
c += P('Với người đọc, bài học thực tế là đọc tin khoa học với một câu hỏi trong đầu: nguồn gốc ở đâu, nghiên cứu làm trên ai, có ai được lợi từ thông tin này không. Các bước cụ thể có trong bài ' + A('thong-tin-khoa-hoc-tren-mang-co-dang-tin', 'Làm sao biết thông tin khoa học trên mạng có đáng tin?') + '.')
c += H2('Câu hỏi thường gặp')
c += '<!-- wp:heading {"level":3} -->\n<h3 class="wp-block-heading">Kết quả nghiên cứu có đại diện cho toàn bộ báo chí Việt Nam không?</h3>\n<!-- /wp:heading -->\n\n'
c += P('Không. Chính nhóm tác giả nói rõ quan điểm của 40 người tham gia không thể khái quát hóa, mẫu nhỏ và không đều giữa các đợt, và kết quả dựa trên cảm nhận của người được phỏng vấn (Tran &amp; Nguyen, 2023).')
c += '<!-- wp:heading {"level":3} -->\n<h3 class="wp-block-heading">Muốn làm báo khoa học thì nên chuẩn bị gì?</h3>\n<!-- /wp:heading -->\n\n'
c += P('Đọc hiểu nghiên cứu, kỹ năng viết cho công chúng và chuẩn mực đạo đức nghề nghiệp. Xem thêm bài ' + A('lam-truyen-thong-khoa-hoc-o-viet-nam', 'Làm truyền thông khoa học ở Việt Nam') + ' và ' + A('viet-khoa-hoc-cho-cong-chung', 'Viết cho công chúng khác viết bài báo khoa học như thế nào?') + '.')
c += H2('Điều gì nên nhớ?')
c += P('Báo chí khoa học ở Việt Nam vừa được kỳ vọng nhiều, vừa thiếu người, thiếu đầu tư và thiếu sự hợp tác từ nhà khoa học. Đào tạo bài bản là một phần lời giải, nhưng cần sự phối hợp của tòa soạn, nhà khoa học và các tổ chức tài trợ. Bài này thuộc ' + HUB + '.')
c += GEN_END + REFS([TN, TDT])
d = dict(slug='bao-chi-khoa-hoc-o-viet-nam-gap-rao-can-gi', title='Báo chí khoa học ở Việt Nam đang gặp những rào cản gì?', seo_title='Báo chí khoa học ở Việt Nam đang gặp những rào cản gì?',
    meta_desc='Báo chí khoa học ở Việt Nam gặp rào cản gì? Nghiên cứu 40 nhà báo: thiếu người chuyên sâu, nhuận bút theo lượt xem, đạo đức, khó tiếp cận nguồn tin.',
    focus_kw='báo chí khoa học Việt Nam', excerpt='Ít phóng viên chuyên sâu, nhuận bút theo lượt xem, chuẩn mực đạo đức lỏng, khó tiếp cận nguồn tin và nhà khoa học ngại hợp tác: bức tranh từ 40 nhà báo khoa học.',
    tags=['báo chí khoa học', 'truyền thông khoa học', 'đạo đức báo chí', 'Việt Nam'], content=c, categories=[3, 9], standard='B',
    cover_alt='Tranh màu nước bàn làm việc tòa soạn với chồng báo, máy ghi âm và một tờ giấy sáng nhẹ, gợi nghề báo khoa học')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print(len(body.split()), [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt']], len(d['meta_desc']), sorted(set(re.findall(r'\(([^()]*?\d{4})\)', body))))
print(re.findall(r'Bài viết này[^.]*', re.sub('<[^>]+>', '', c))[:1])

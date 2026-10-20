import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'

FA = 'Farias, M., Maraldi, E., Wallenkampf, K. C., &amp; Lucchetti, G. (2020). Adverse events in meditation practices and meditation-based therapies: A systematic review. <em>Acta Psychiatrica Scandinavica, 142</em>(5), 374-393. https://doi.org/10.1111/acps.13225'
GO = 'Goyal, M., Singh, S., Sibinga, E. M. S., Gould, N. F., Rowland-Seymour, A., Sharma, R., Berger, Z., Sleicher, D., Maron, D. D., Shihab, H. M., Ranasinghe, P. D., Linn, S., Saha, S., Bass, E. B., &amp; Haythornthwaite, J. A. (2014). Meditation programs for psychological stress and well-being: A systematic review and meta-analysis. <em>JAMA Internal Medicine, 174</em>(3), 357-368. https://doi.org/10.1001/jamainternmed.2013.13018'
JO = 'Johnson, S. B., Park, H. S., Gross, C. P., &amp; Yu, J. B. (2018). Complementary medicine, refusal of conventional cancer therapy, and survival among patients with curable cancers. <em>JAMA Oncology, 4</em>(10), 1375-1381. https://doi.org/10.1001/jamaoncol.2018.2487'
LP = 'Lê Thành Phương. (2026, ngày 23 tháng 6). Hành nghề mê tín dị đoan và các chế tài xử lý. <em>Tạp chí điện tử Luật sư Việt Nam</em>. https://lsvn.vn/hanh-nghe-me-tin-di-doan-va-cac-che-tai-xu-ly-a174659.html'
QC12 = 'Quốc hội. (2012). <em>Luật Quảng cáo số 16/2012/QH13</em>. https://hieuluat.vn/thuong-mai/-luat-quang-cao-2012-11834.html'
QC25 = 'Quốc hội. (2025). <em>Luật sửa đổi, bổ sung một số điều của Luật Quảng cáo số 75/2025/QH15</em>. https://thuvienphapluat.vn/van-ban/Thuong-mai/Luat-Quang-cao-sua-doi-2025-so-75-2025-QH15-555035.aspx'
TN = 'Quốc hội. (2016). <em>Luật Tín ngưỡng, tôn giáo số 02/2016/QH14</em>. https://thuvienphapluat.vn/van-ban/van-hoa-xa-hoi/Luat-tin-nguong-ton-giao-2016-322934.aspx'

c = ''
c += P('Truyền thông dịch vụ tâm linh là cách giới thiệu các hoạt động như lễ hội ở cơ sở thờ tự, phong thủy, xem ngày, tử vi, khóa thiền "chữa lành", tarot hay chiêm tinh đến công chúng. Khác với hầu hết sản phẩm, thứ được "bán" ở đây là niềm tin, và người tìm đến thường đang lo âu hoặc gặp khó khăn. Vì vậy, một thông điệp sai không chỉ là quảng cáo kém mà có thể khiến người khác mất tiền, trì hoãn điều trị hoặc ra quyết định quan trọng dựa trên lời hứa không kiểm chứng được.')
c += P('Bài viết đề xuất một khung truyền thông gồm năm nguyên tắc, dựa trên các quy định pháp luật Việt Nam hiện hành và bằng chứng khoa học liên quan, kèm cách áp dụng cho bốn nhóm dịch vụ.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Luật Tín ngưỡng, tôn giáo cấm lợi dụng hoạt động tín ngưỡng, tôn giáo để trục lợi (Quốc hội, 2016).',
    'Luật Quảng cáo cấm quảng cáo không đúng hoặc gây nhầm lẫn về công dụng, chất lượng, và cấm dùng từ "nhất", "số một" khi không có tài liệu chứng minh (Quốc hội, 2012).',
    'Từ 01/01/2026, người có ảnh hưởng phải kiểm tra tài liệu và không được giới thiệu dịch vụ mình chưa hiểu rõ (Quốc hội, 2025).',
    'Thiền có bằng chứng mức vừa phải giúp giảm lo âu, trầm cảm, đau, nhưng không tốt hơn các điều trị tích cực (Goyal và cộng sự, 2014).',
    'Rủi ro lớn nhất không nằm ở bản thân niềm tin, mà ở việc người dùng từ bỏ hoặc trì hoãn điều trị y khoa (Johnson và cộng sự, 2018).',
])

c += H2('Vì sao dịch vụ tâm linh cần một khung truyền thông riêng?')
c += P('Có ba lý do khiến lĩnh vực này nhạy cảm hơn truyền thông thông thường:')
c += UL([
    '<strong>Sản phẩm vô hình, kết quả khó kiểm chứng.</strong> Một lá số, một buổi giải hạn hay một quẻ tarot không có tiêu chuẩn chất lượng để đối chiếu, nên người dùng phụ thuộc gần như hoàn toàn vào lời giới thiệu.',
    '<strong>Người dùng thường ở trạng thái dễ tổn thương.</strong> Nhiều người tìm đến khi bệnh tật, mất mát, khó khăn tài chính hay bế tắc trong quan hệ. Đây là lúc thông điệp đánh vào nỗi sợ dễ có tác dụng nhất, và cũng dễ gây hại nhất. Bài ' + A('thao-tung-cam-xuc-emotional-manipulation', 'thao túng cảm xúc') + ' phân tích cơ chế này.',
    '<strong>Hậu quả có thể là sức khỏe.</strong> Một nghiên cứu trên dữ liệu ung thư quốc gia Hoa Kỳ cho thấy người dùng liệu pháp bổ sung từ chối hóa trị nhiều hơn rõ rệt (34,1% so với 3,2%) và có nguy cơ tử vong cao hơn; khi tính đến việc từ chối hoặc trì hoãn điều trị chuẩn, mối liên quan này không còn ý nghĩa thống kê (Johnson và cộng sự, 2018). Nói cách khác, tác hại đến chủ yếu từ việc bỏ điều trị.',
])
c += P('Nghiên cứu của Johnson và cộng sự (2018) là nghiên cứu quan sát về liệu pháp bổ sung nói chung, không riêng dịch vụ tâm linh. Tuy vậy, bài học cho người làm truyền thông rất rõ: thông điệp nào khiến người bệnh xa rời điều trị chuẩn đều có thể gây hại thật.')

c += H2('Pháp luật Việt Nam đặt ra những ranh giới nào?')
c += P('Dưới đây là các quy định liên quan trực tiếp đến cách truyền thông. Phần này mang tính tham khảo, không thay thế tư vấn pháp lý cho từng trường hợp.')
c += TABLE(['Văn bản', 'Nội dung liên quan'], [
    ['Luật Tín ngưỡng, tôn giáo 2016, Điều 5', 'Khoản 5 cấm "lợi dụng hoạt động tín ngưỡng, hoạt động tôn giáo để trục lợi" (Quốc hội, 2016).'],
    ['Luật Quảng cáo 2012, Điều 8', 'Khoản 9 cấm quảng cáo không đúng hoặc gây nhầm lẫn về chất lượng, giá, công dụng của dịch vụ. Khoản 11 cấm dùng các từ "nhất", "duy nhất", "tốt nhất", "số một" khi không có tài liệu hợp pháp chứng minh (Quốc hội, 2012).'],
    ['Luật Quảng cáo sửa đổi 2025, Điều 15a', 'Người có ảnh hưởng phải xác minh độ tin cậy của người quảng cáo, kiểm tra tài liệu về dịch vụ, không giới thiệu dịch vụ mình chưa dùng hoặc chưa hiểu rõ, và thông báo việc quảng cáo ngay trước và trong khi thực hiện. Hiệu lực từ 01/01/2026 (Quốc hội, 2025).'],
    ['Bộ luật Hình sự 2015, Điều 320', 'Người dùng bói toán, đồng bóng hoặc hình thức mê tín, dị đoan khác, đã bị xử phạt hành chính hoặc đã bị kết án mà còn vi phạm, có thể bị phạt tiền từ 10 đến 100 triệu đồng hoặc phạt tù đến 3 năm (Lê Thành Phương, 2026).'],
    ['Nghị định 87/2026/NĐ-CP, Điều 20', 'Phạt tiền từ 20 đến 30 triệu đồng với hành vi tổ chức hoạt động mê tín dị đoan (Lê Thành Phương, 2026).'],
])
c += P('Điểm cần lưu ý: pháp luật không cấm hoạt động tín ngưỡng hay việc tìm hiểu văn hóa phong thủy, tử vi. Ranh giới nằm ở trục lợi, gây nhầm lẫn và mê tín dị đoan. Cùng một dịch vụ, cách nói quyết định nó nằm ở phía nào của ranh giới.')

c += H2('Khung truyền thông dịch vụ tâm linh gồm những nguyên tắc nào?')
c += P('Năm nguyên tắc dưới đây do người viết tổng hợp từ các quy định trên và các chuẩn mực ' + A('dao-duc-truyen-thong-communication-ethics', 'đạo đức truyền thông') + '. Đây là đề xuất thực hành, không phải một bộ tiêu chuẩn đã được cơ quan nào ban hành.')
c += H3('1. Gọi đúng tên bản chất dịch vụ')
c += P('Giới thiệu dịch vụ như một trải nghiệm văn hóa, tinh thần hoặc công cụ tự suy ngẫm, không khoác cho nó vẻ "khoa học" hay "y khoa". Tránh các cụm như "được khoa học chứng minh", "liệu pháp", "phác đồ" nếu không có bằng chứng tương ứng.')
c += H3('2. Không hứa hẹn kết quả')
c += P('Không cam kết phát tài, khỏi bệnh, giữ được hôn nhân hay tránh được tai họa. Những lời hứa này không thể chứng minh, và dễ rơi vào hành vi quảng cáo gây nhầm lẫn về công dụng (Quốc hội, 2012).')
c += H3('3. Không khai thác nỗi sợ')
c += P('Không dùng thông điệp kiểu "năm hạn nặng, không giải sẽ gặp họa", "bị phá, bị yểm" để thúc người dùng trả tiền. Thông điệp dọa dẫm vừa gây tổn hại tinh thần, vừa có thể bị xem là trục lợi từ niềm tin (Quốc hội, 2016).')
c += H3('4. Minh bạch giá, người thực hiện và quan hệ thương mại')
c += P('Công khai mức phí trước khi dịch vụ diễn ra, nói rõ người thực hiện là ai và có trình độ gì. Khi hợp tác với người có ảnh hưởng, nội dung phải được ghi rõ là quảng cáo (Quốc hội, 2025).')
c += H3('5. Luôn có lối ra sang chuyên môn phù hợp')
c += P('Với các vấn đề sức khỏe thể chất, sức khỏe tâm thần, pháp lý hay tài chính, thông điệp cần chủ động khuyến khích người dùng gặp bác sĩ, chuyên gia tâm lý, luật sư hoặc chuyên gia tài chính. Dịch vụ tâm linh, nếu có, chỉ nên đi kèm chứ không thay thế.')

c += H2('Áp dụng cho từng nhóm dịch vụ thế nào?')
c += TABLE(['Nhóm dịch vụ', 'Nên truyền thông', 'Cần tránh'], [
    ['Cơ sở tín ngưỡng, tôn giáo', 'Lịch sử, giá trị văn hóa, lịch lễ hội, quy định trang phục và ứng xử, cách đóng góp tự nguyện minh bạch', 'Gắn mức tiền cúng, lễ vật với mức độ "linh ứng"; bán lễ vật, dịch vụ giải hạn kèm cam kết kết quả'],
    ['Phong thủy, xem ngày, tử vi', 'Giới thiệu như tri thức văn hóa dân gian để tham khảo; nói rõ đây là góc nhìn truyền thống', '"Đảm bảo phát tài", "chắc chắn tránh họa", dọa dẫm về năm hạn, ép mua vật phẩm kèm lời hứa'],
    ['Chữa lành, thiền, yoga tâm linh', 'Lợi ích có bằng chứng, nói ở mức vừa phải; trình độ người hướng dẫn; lưu ý ai nên thận trọng', '"Chữa khỏi trầm cảm, ung thư", "thay thế thuốc", khuyên bỏ điều trị; im lặng về tác dụng không mong muốn'],
    ['Tarot, chiêm tinh, bói toán', 'Định vị là giải trí hoặc công cụ tự suy ngẫm; khuyến khích người dùng tự quyết định', 'Phán đoán về bệnh tật, kiện tụng, đầu tư; "giải bùa", "cắt vong" có thu phí; dự đoán như sự thật chắc chắn'],
])
c += P('Riêng nhóm chữa lành, thiền, yoga, có hai bằng chứng nên biết khi viết thông điệp:')
c += UL([
    'Một tổng quan hệ thống và phân tích gộp cho thấy các chương trình thiền chánh niệm có bằng chứng mức vừa phải giúp giảm lo âu, trầm cảm và đau, nhưng không có bằng chứng cho thấy thiền tốt hơn các điều trị tích cực khác (Goyal và cộng sự, 2014).',
    'Một tổng quan hệ thống khác gồm 83 nghiên cứu với 6.703 người tham gia ghi nhận tỉ lệ tác dụng không mong muốn khi thiền là 8,3%, phổ biến nhất là lo âu và trầm cảm, và có thể xảy ra ở cả người chưa từng có vấn đề sức khỏe tâm thần (Farias và cộng sự, 2020).',
])
c += P('Vì vậy, cách nói phù hợp là "có thể hỗ trợ giảm căng thẳng", kèm lưu ý người đang điều trị tâm thần nên hỏi ý kiến bác sĩ. Bài ' + A('hoi-chung-wellness-bay-chua-lanh-thuong-mai-hoa', 'hội chứng wellness và bẫy chữa lành thương mại hóa') + ' bàn sâu hơn về xu hướng này.')

c += H2('Người có ảnh hưởng cần lưu ý gì?')
c += P('Từ 01/01/2026, người có ảnh hưởng nhận quảng cáo dịch vụ tâm linh có thêm nghĩa vụ riêng theo Điều 15a Luật Quảng cáo (Quốc hội, 2025):')
c += UL([
    'Xác minh độ tin cậy của bên thuê quảng cáo và kiểm tra tài liệu về dịch vụ.',
    'Không giới thiệu dịch vụ mình chưa sử dụng hoặc chưa hiểu rõ.',
    'Thông báo rõ đây là quảng cáo ngay trước và trong khi thực hiện.',
])
c += P('Câu chuyện cá nhân kiểu "mình xem xong là đổi vận" có sức thuyết phục cao nhưng không phải bằng chứng. Bài ' + A('nguoi-noi-tieng-noi-ve-khoa-hoc-nen-tin-den-dau', 'người nổi tiếng nói về khoa học, nên tin đến đâu') + ' giải thích vì sao.')

c += H2('Checklist trước khi đăng nội dung')
c += UL([
    'Nội dung có hứa hẹn kết quả cụ thể (tiền, sức khỏe, tình cảm, tránh họa) không?',
    'Có dùng nỗi sợ, sự khẩn cấp hay cảm giác tội lỗi để thúc người dùng trả tiền không?',
    'Có các từ "nhất", "duy nhất", "số một", "100%" mà không có tài liệu chứng minh không?',
    'Có tự gắn mác "khoa học", "y khoa", "trị liệu" mà không có bằng chứng tương ứng không?',
    'Có nội dung nào khiến người bệnh có thể bỏ hoặc trì hoãn điều trị không?',
    'Giá và người thực hiện đã được công khai chưa?',
    'Nếu dùng người có ảnh hưởng, nội dung đã ghi rõ là quảng cáo chưa?',
    'Đã có câu khuyến khích tìm đến chuyên môn phù hợp khi cần chưa?',
])
c += P('Nếu câu trả lời cho bất kỳ câu hỏi nào trong năm câu đầu là "có", nên sửa trước khi đăng. Bài ' + A('quang-cao-thuc-pham-bao-ve-suc-khoe-loi-thuong-gap', 'lỗi thường gặp khi quảng cáo thực phẩm bảo vệ sức khỏe') + ' có nhiều điểm tương đồng về cách tránh tuyên bố công dụng quá mức.')

c += H2('Câu hỏi thường gặp')
c += H3('Quảng bá dịch vụ tarot, tử vi có vi phạm pháp luật không?')
c += P('Các văn bản nêu trong bài không cấm riêng việc giới thiệu tarot hay tử vi như hoạt động văn hóa, giải trí. Rủi ro pháp lý phát sinh khi nội dung gây nhầm lẫn về công dụng, có dấu hiệu trục lợi hoặc mê tín dị đoan (Quốc hội, 2012; Quốc hội, 2016; Lê Thành Phương, 2026). Trường hợp cụ thể nên hỏi ý kiến luật sư.')
c += H3('Có được nói thiền giúp giảm căng thẳng không?')
c += P('Có thể nói ở mức "có thể hỗ trợ", vì đã có bằng chứng mức vừa phải (Goyal và cộng sự, 2014). Không nên nói thiền chữa khỏi bệnh hoặc thay thế điều trị.')
c += H3('Cơ sở thờ tự có nên công khai các khoản đóng góp?')
c += P('Nên. Minh bạch giúp tách bạch đóng góp tự nguyện với hành vi trục lợi từ niềm tin, điều Luật Tín ngưỡng, tôn giáo cấm (Quốc hội, 2016).')

c += H2('Điều gì nên nhớ?')
c += P('Truyền thông dịch vụ tâm linh có trách nhiệm không có nghĩa là phủ nhận niềm tin của người khác. Nó có nghĩa là nói đúng bản chất, không hứa điều không thể chứng minh, không khai thác nỗi sợ, minh bạch về tiền và luôn chừa đường cho người dùng tìm đến chuyên môn khi cần. Khi đó, thương hiệu xây được niềm tin bền vững thay vì niềm tin dựa trên lo âu.')
c += P('<em>Bài viết mang tính thông tin, không thay thế tư vấn pháp lý hoặc y khoa cho từng trường hợp.</em>')
c += GEN_END + REFS([FA, GO, JO, LP, QC12, QC25, TN])

d = dict(slug='khung-truyen-thong-dich-vu-tam-linh', title='Khung truyền thông dịch vụ tâm linh: ranh giới pháp lý và 5 nguyên tắc đạo đức',
    seo_title='Truyền thông dịch vụ tâm linh: ranh giới pháp lý, 5 nguyên tắc',
    meta_desc='Truyền thông dịch vụ tâm linh: quy định pháp luật Việt Nam, 5 nguyên tắc đạo đức, cách áp dụng cho phong thủy, tử vi, chữa lành, tarot và checklist.',
    focus_kw='truyền thông dịch vụ tâm linh',
    excerpt='Phong thủy, tử vi, chữa lành, tarot nên được truyền thông thế nào để không trục lợi niềm tin? Ranh giới pháp lý, 5 nguyên tắc và checklist trước khi đăng.',
    tags=['truyền thông dịch vụ tâm linh', 'đạo đức truyền thông', 'luật quảng cáo', 'chữa lành', 'người có ảnh hưởng'], content=c, categories=[5, 17],
    date='2026-11-12T19:30:00', cover_alt='Minh họa ngọn nến và tấm khiên có dấu tích, tượng trưng cho truyền thông dịch vụ tâm linh minh bạch, có trách nhiệm')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

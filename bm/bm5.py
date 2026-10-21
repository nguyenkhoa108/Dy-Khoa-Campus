import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'


FTC = 'Federal Trade Commission. (2022). <em>Health products compliance guidance</em>. https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance'
ND87 = 'Chính phủ. (2026). <em>Nghị định số 87/2026/NĐ-CP quy định xử phạt vi phạm hành chính trong lĩnh vực văn hóa và quảng cáo</em>. Công báo điện tử Chính phủ. https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-87-2026-nd-cp-469359.htm'

c = ''
c += P('"Đã được chứng minh lâm sàng" là một trong những cụm từ có sức thuyết phục nhất trong quảng cáo sức khỏe, vì nó hứa hẹn rằng sản phẩm đã được thử nghiệm trên người. Nhưng cụm từ này có thể đúng một phần mà vẫn gây hiểu lầm: nghiên cứu có thể làm trên một thành phần chứ không phải sản phẩm, trên một nhóm người khác, đo một kết quả khác, hoặc chỉ là một nghiên cứu nhỏ trong khi các nghiên cứu lớn hơn không cho kết quả tương tự. Hướng dẫn tuân thủ về sản phẩm sức khỏe của Ủy ban Thương mại Liên bang Mỹ (FTC) đưa ra nhiều ví dụ cụ thể cho từng trường hợp (Federal Trade Commission [FTC], 2022).')
c += P('Đây là bài thứ năm trong chuyên đề "Bóc mác y khoa trong quảng cáo". Bài trước bóc ' + A('dat-chuan-fda-fda-co-cap-phep-thuc-pham-chuc-nang-khong', 'mác "đạt chuẩn FDA"') + '.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Theo FTC, nhà quảng cáo phải có ít nhất mức bằng chứng mà họ tuyên bố có.',
    'Với lợi ích sức khỏe, bằng chứng nhìn chung cần là thử nghiệm lâm sàng ngẫu nhiên có đối chứng trên người.',
    'Năm câu hỏi cần đặt ra: thử trên sản phẩm nào, liều nào, trên ai, đo kết quả gì, và các nghiên cứu khác nói gì.',
    'Ở Việt Nam, dùng kết quả nghiên cứu lâm sàng chưa được Bộ Y tế công nhận để quảng cáo thuốc bị xử phạt.',
])

c += H2('FTC yêu cầu gì khi quảng cáo nói "đã chứng minh lâm sàng"?')
c += P('Hướng dẫn của FTC (2022) nêu nguyên tắc khởi điểm: nhà tiếp thị sản phẩm sức khỏe phải có ít nhất mức bằng chứng mà họ tuyên bố có. Ngoài việc mọi tuyên bố về an toàn, hiệu quả đều phải có căn cứ, mọi khẳng định về số lượng, loại hoặc độ mạnh của bằng chứng cũng phải chính xác.')
c += P('FTC (2022) cũng cho biết, nhìn chung, căn cứ cho các lợi ích sức khỏe cần ở dạng thử nghiệm lâm sàng ngẫu nhiên có đối chứng trên người. Khi đánh giá một thử nghiệm, FTC xem xét cỡ mẫu, thời gian và cách đo kết quả, và khuyến khích nhà tiếp thị tham khảo ý kiến chuyên gia độc lập trong lĩnh vực nghiên cứu liên quan.')
c += P('Đáng chú ý, cụm từ không cần xuất hiện trực tiếp. FTC (2022) nêu ví dụ một tờ quảng cáo sản phẩm giảm cân dùng hình bác sĩ mặc áo blouse nhìn kính hiển vi, cấu trúc phân tử và chồng tạp chí y khoa: những hình ảnh này tạo ấn tượng về tính khoa học và nhiều khả năng ngụ ý sản phẩm đã được chứng minh lâm sàng.')

c += H2('Năm cách "chứng minh lâm sàng" có thể gây hiểu lầm')
c += H3('1. Nghiên cứu không làm trên chính sản phẩm')
c += P('FTC (2022) đưa ví dụ một loại đồ uống chứa lợi khuẩn (probiotic) muốn dựa vào hai nghiên cứu tốt ở Nhật Bản. Tuy nhiên, các nghiên cứu dùng một chủng lợi khuẩn khác, ở dạng viên nang phóng thích chậm, trên nhóm người có chế độ ăn có thể rất khác. Nhà quảng cáo cần cân nhắc mức độ liên quan của bằng chứng với sản phẩm và với người dùng mục tiêu trước khi dựa vào chúng.')
c += P('Tương tự, khi một sản phẩm thảo dược dựa vào phê duyệt của cơ quan nước ngoài, FTC (2022) lưu ý nhà tiếp thị cần xem lại nghiên cứu gốc để chắc rằng liều lượng và dạng bào chế tương đương với sản phẩm của mình.')
c += H3('2. Nghiên cứu làm trên một nhóm người khác')
c += P('Một loại trà được chứng minh qua nhiều nghiên cứu là cải thiện sự tỉnh táo ở người bị suy giảm tuần hoàn não nghiêm trọng. Theo FTC (2022), các nghiên cứu này không đủ để quảng cáo rằng trà giúp người trưởng thành khỏe mạnh tỉnh táo hơn.')
c += H3('3. Nghiên cứu đo một kết quả khác')
c += P('Một phần mềm luyện não quảng cáo "đã được chứng minh lâm sàng giúp cải thiện trí nhớ", minh họa bằng cảnh một người quên chỗ để chìa khóa. Nghiên cứu thực tế chỉ dùng ba bài tập trong phòng thí nghiệm để đo trí nhớ làm việc. FTC (2022) cho rằng kết quả này không đủ cho tuyên bố cải thiện trí nhớ nói chung, vì có nhiều loại trí nhớ khác chưa được thử, và quên chỗ để chìa khóa là một kiểu suy giảm trí nhớ khác.')
c += H3('4. Chọn ra một kết quả thuận lợi giữa nhiều phép đo')
c += P('Một thiết bị kích thích não được thử nghiệm ngẫu nhiên, mù đôi, có đối chứng trên người trầm cảm với tám thang đo. Chỉ một trong tám thang đo cho kết quả tốt hơn nhóm đối chứng, và nghiên cứu không hiệu chỉnh thống kê cho việc dùng nhiều phép đo. Theo FTC (2022), kết quả đơn lẻ này có thể do ngẫu nhiên, và không đủ để quảng cáo bất kỳ lợi ích nào cho trầm cảm. Hiện tượng này liên quan đến ' + A('p-hacking-la-gi-vi-sao-nghien-cuu-thong-ke-van-co-the-sai', 'p-hacking') + '.')
c += H3('5. Dựa vào một nghiên cứu nhỏ, bỏ qua các nghiên cứu lớn hơn')
c += P('Một loại nước trái cây quảng cáo "đã được chứng minh có lợi cho tim mạch" dựa trên một nghiên cứu nhỏ có kết quả tốt. Hai nghiên cứu lớn hơn sau đó không tìm thấy khác biệt so với giả dược. Theo FTC (2022), xét toàn bộ bằng chứng, tuyên bố này không có căn cứ, và tiếp tục quảng bá nghiên cứu nhỏ ban đầu là lừa dối.')

c += H2('Bảng kiểm tra nhanh')
c += TABLE(['Câu hỏi', 'Dấu hiệu cần dè chừng'], [
    ['Thử trên sản phẩm nào?', 'Nghiên cứu làm trên một thành phần, một chủng, hoặc dạng bào chế khác'],
    ['Liều bao nhiêu?', 'Liều trong nghiên cứu khác liều trong sản phẩm'],
    ['Thử trên ai?', 'Người bệnh nặng trong nghiên cứu, nhưng quảng cáo cho người khỏe mạnh'],
    ['Đo kết quả gì?', 'Đo một chỉ số trong phòng thí nghiệm, nhưng quảng cáo một lợi ích chung chung'],
    ['Các nghiên cứu khác nói gì?', 'Chỉ dẫn một nghiên cứu nhỏ, không nhắc các nghiên cứu lớn hơn'],
])
c += P('Bảng do người viết tổng hợp từ các ví dụ trong hướng dẫn của FTC (2022). Để đọc kỹ hơn một nghiên cứu được chia sẻ, xem bài ' + A('kiem-tra-nghien-cuu-chia-se-tren-mang', 'làm sao kiểm tra một nghiên cứu được chia sẻ trên mạng') + '.')

c += H2('Ở Việt Nam, quy định thế nào?')
c += P('Nghị định 87/2026/NĐ-CP phạt từ 30 đến 40 triệu đồng đối với hành vi sử dụng kết quả nghiên cứu lâm sàng, nghiên cứu tiền lâm sàng, kết quả kiểm nghiệm, kết quả thử tương đương sinh học chưa được Bộ Y tế công nhận để quảng cáo thuốc (Chính phủ, 2026, Điều 69 khoản 4). Với sản phẩm không phải là thuốc (trừ thiết bị y tế), quảng cáo có nội dung phòng bệnh, chữa bệnh, điều trị bệnh cũng bị phạt ở cùng mức (Chính phủ, 2026, Điều 69 khoản 4).')
c += P('Các mức phạt trên áp dụng với cá nhân; tổ chức bị phạt gấp đôi (Chính phủ, 2026, Điều 6 khoản 3).')

c += H2('Câu hỏi thường gặp')
c += H3('"Đã chứng minh lâm sàng" có nghĩa là sản phẩm hiệu quả?')
c += P('Chưa chắc. Cần biết nghiên cứu làm trên chính sản phẩm hay chỉ một thành phần, trên ai, đo kết quả gì, và các nghiên cứu khác có cho kết quả tương tự không (FTC, 2022).')
c += H3('Một nghiên cứu lâm sàng có đủ không?')
c += P('FTC (2022) đánh giá dựa trên toàn bộ bằng chứng. Một nghiên cứu nhỏ có kết quả tốt không đủ nếu các nghiên cứu lớn hơn không cho kết quả tương tự.')
c += H3('Quảng cáo dùng hình bác sĩ, phòng thí nghiệm có ý nghĩa gì?')
c += P('Theo FTC (2022), những hình ảnh như vậy có thể ngụ ý sản phẩm đã được chứng minh lâm sàng, dù quảng cáo không nói thẳng.')

c += H2('Điều gì nên nhớ?')
c += P('"Đã chứng minh lâm sàng" không phải con dấu bảo đảm. Điều quan trọng là nghiên cứu nào, trên sản phẩm nào, với ai, đo gì, và toàn bộ bằng chứng nói gì. Một quảng cáo không trả lời được những câu hỏi này đang mượn uy tín của khoa học mà chưa chắc có khoa học đứng sau.')
c += GEN_END + REFS([ND87, FTC])

d = dict(slug='da-chung-minh-lam-sang-nghia-la-gi', title='"Đã chứng minh lâm sàng": cụm từ nghe y khoa nhưng có thể gây hiểu lầm',
    seo_title='"Đã chứng minh lâm sàng" có đáng tin không?',
    meta_desc='"Đã chứng minh lâm sàng" có thể đúng một phần mà vẫn gây hiểu lầm: thử trên thành phần khác, nhóm người khác hay đo kết quả khác. 5 câu hỏi để kiểm tra.',
    focus_kw='chứng minh lâm sàng',
    excerpt='Quảng cáo nói sản phẩm "đã chứng minh lâm sàng" có thể dựa trên nghiên cứu không liên quan. Năm cách cụm từ này gây hiểu lầm, theo hướng dẫn của FTC.',
    tags=['chứng minh lâm sàng', 'kiểm nghiệm lâm sàng', 'thử nghiệm lâm sàng', 'quảng cáo sức khỏe', 'bóc mác y khoa'], content=c, categories=[3, 11],
    date='2026-11-16T16:00:00', cover_alt='Minh họa nhãn quảng cáo "Đã kiểm nghiệm lâm sàng" bị bút đỏ ghi chú "Thử trên ai, bao nhiêu người?"')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

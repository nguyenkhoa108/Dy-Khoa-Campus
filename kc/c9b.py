import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'

AZ = 'Azari, A. A., &amp; Barney, N. P. (2013). Conjunctivitis: A systematic review of diagnosis and treatment. <em>JAMA, 310</em>(16), 1721-1729. https://doi.org/10.1001/jama.2013.280318 (bản mở: https://pmc.ncbi.nlm.nih.gov/articles/PMC4049531/)'
CA = 'Centers for Disease Control and Prevention. (2024a, ngày 15 tháng 4). <em>About pink eye</em>. https://www.cdc.gov/conjunctivitis/about/index.html'
CP = 'Centers for Disease Control and Prevention. (2024b, ngày 15 tháng 4). <em>Preventing pink eye</em>. https://www.cdc.gov/conjunctivitis/prevention/index.html'

c = ''
c += P('Đau mắt đỏ (viêm kết mạc) là tình trạng viêm lớp màng mỏng phủ lòng trắng mắt và mặt trong mí mắt. Nguyên nhân thường gặp nhất là virus, sau đó là vi khuẩn và dị ứng; phần lớn trường hợp tự khỏi và không cần kháng sinh (Azari &amp; Barney, 2013). Điều quan trọng nhất là giữ vệ sinh để không lây cho người khác, và nhận biết các dấu hiệu cần đi khám mắt sớm.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Virus gây đến 80% các ca viêm kết mạc cấp (Azari &amp; Barney, 2013).',
    'Đau mắt đỏ do virus không cần kháng sinh; nhỏ kháng sinh không giúp gì mà còn có thể gây hại (Azari &amp; Barney, 2013).',
    'Không tự ý dùng thuốc nhỏ mắt có corticoid.',
    'Rửa tay bằng xà phòng ít nhất 20 giây và không dùng chung khăn, gối, thuốc nhỏ mắt là cách phòng lây chính (Centers for Disease Control and Prevention [CDC], 2024b).',
    'Đi khám mắt ngay nếu nhìn mờ, đau mắt nhiều, sợ ánh sáng hoặc chảy mủ nhiều.',
])

c += H2('Đau mắt đỏ có những dấu hiệu nào?')
c += P('Các triệu chứng thường gặp ở một hoặc cả hai mắt gồm (CDC, 2024a):')
c += UL([
    'Lòng trắng mắt chuyển hồng hoặc đỏ.',
    'Sưng mí mắt.',
    'Chảy nước mắt.',
    'Cảm giác cộm như có vật lạ trong mắt.',
    'Ngứa, rát mắt.',
    'Có ghèn (dịch tiết) ở mắt.',
])

c += H2('Đau mắt đỏ do đâu?')
c += P('Có ba nguyên nhân phổ biến, mỗi loại có đặc điểm và cách xử lý khác nhau (Azari &amp; Barney, 2013):')
c += TABLE(['Nguyên nhân', 'Đặc điểm thường gặp', 'Cách xử lý'], [
    ['Virus (thường gặp nhất)', 'Dịch tiết loãng, trong; có thể kèm sưng hạch. Lây rất mạnh.', 'Không có thuốc đặc hiệu; chườm lạnh, nước mắt nhân tạo giúp đỡ khó chịu. Không cần kháng sinh.'],
    ['Vi khuẩn', 'Ghèn đặc, hai mí dính lại khi ngủ dậy, ít ngứa.', 'Đa số tự khỏi trong 1 đến 2 tuần; bác sĩ có thể kê kháng sinh nhỏ mắt để khỏi nhanh hơn.'],
    ['Dị ứng', 'Ngứa là dấu hiệu nổi bật nhất. Không lây.', 'Thuốc nhỏ kháng dị ứng theo chỉ định.'],
])
c += P('Theo Azari và Barney (2013), độ chính xác khi chẩn đoán đau mắt đỏ do virus chỉ bằng quan sát chưa đến 50% so với xét nghiệm, và nhiều ca do virus bị nhầm là do vi khuẩn. Vì vậy, tự đoán nguyên nhân rồi tự mua thuốc là không đáng tin cậy.')

c += H2('Đau mắt đỏ lây như thế nào và trong bao lâu?')
c += P('Đau mắt đỏ do virus và vi khuẩn đều lây rất dễ từ người sang người (CDC, 2024a). Với virus adeno, tác nhân gây phần lớn các ca do virus, nguy cơ lây được ước tính từ 10% đến 50%. Virus lây qua tiếp xúc trực tiếp với ngón tay bị nhiễm, đồ dùng cá nhân, nước bể bơi; trong một nghiên cứu, 46% người bệnh có virus trên tay (Azari &amp; Barney, 2013).')
c += P('Thời gian ủ bệnh và thời gian có thể lây ước tính (Azari &amp; Barney, 2013):')
c += UL([
    '<strong>Do virus adeno:</strong> ủ bệnh 5 đến 12 ngày, có thể lây trong 10 đến 14 ngày.',
    '<strong>Do vi khuẩn:</strong> ủ bệnh 1 đến 7 ngày, có thể lây trong 2 đến 7 ngày.',
])

c += H2('Có cần nhỏ thuốc kháng sinh không?')
c += P('Với đau mắt đỏ do virus, câu trả lời là không. Kháng sinh nhỏ mắt không có tác dụng, không ngăn được bội nhiễm, có thể gây dị ứng, kích ứng, làm chậm phát hiện các bệnh mắt khác, và lọ thuốc dùng chung có thể làm lây sang mắt còn lại (Azari &amp; Barney, 2013).')
c += P('Với đau mắt đỏ do vi khuẩn, ít nhất 60% trường hợp tự khỏi trong 1 đến 2 tuần. Kháng sinh nhỏ mắt giúp khỏi nhanh hơn và đi học, đi làm lại sớm hơn, nên bác sĩ có thể kê trong một số trường hợp, đặc biệt với người đeo kính áp tròng (Azari &amp; Barney, 2013).')
c += P('<strong>Lưu ý quan trọng:</strong> không tự ý dùng thuốc nhỏ mắt có chứa corticoid hoặc thuốc phối hợp kháng sinh với corticoid. Các tác giả khuyến cáo không dùng thường quy loại thuốc này, vì corticoid có thể làm bệnh kéo dài và làm nặng thêm nhiễm trùng, đặc biệt nguy hiểm nếu là nhiễm virus herpes (Azari &amp; Barney, 2013). Bài ' + A('bi-cam-cum-co-nen-uong-khang-sinh', 'bị cảm cúm có nên uống kháng sinh') + ' giải thích thêm vì sao kháng sinh không có tác dụng với virus.')

c += H2('Khi nào cần đi khám mắt ngay?')
c += P('Theo khuyến cáo của Học viện Nhãn khoa Hoa Kỳ được Azari và Barney (2013) tổng hợp, cần đến bác sĩ chuyên khoa mắt sớm nếu có:')
c += UL([
    'Giảm thị lực, nhìn mờ.',
    'Đau mắt từ vừa đến nhiều.',
    'Chảy mủ nhiều.',
    'Sợ ánh sáng.',
    'Không đỡ sau khoảng 1 tuần, hoặc bị tái đi tái lại.',
    'Đang đeo kính áp tròng.',
    'Từng bị bệnh mắt do virus herpes.',
])
c += P('Trẻ sơ sinh có dấu hiệu đau mắt đỏ cần được bác sĩ khám ngay (CDC, 2024a).')

c += H2('Làm sao để không lây cho người khác?')
c += P('Nếu bạn đang bị đau mắt đỏ (CDC, 2024b):')
c += UL([
    'Rửa tay thường xuyên bằng xà phòng và nước ít nhất 20 giây, nhất là trước và sau khi lau mắt hoặc nhỏ thuốc.',
    'Không dụi mắt bằng tay.',
    'Lau ghèn quanh mắt nhiều lần trong ngày bằng khăn sạch hoặc bông ướt, với tay đã rửa sạch.',
    'Không dùng chung gối, khăn mặt, khăn tắm, thuốc nhỏ mắt, đồ trang điểm mắt.',
    'Ngừng đeo kính áp tròng cho đến khi hết triệu chứng hoặc bác sĩ cho phép.',
    'Giặt vỏ gối, ga giường, khăn thường xuyên bằng nước nóng và xà phòng.',
])
c += P('Nếu bạn sống cùng người bị đau mắt đỏ: rửa tay sau khi tiếp xúc với người bệnh hoặc đồ dùng của họ, không chạm vào mắt khi chưa rửa tay, và không dùng chung bất kỳ vật dụng nào của người bệnh, kể cả kính (CDC, 2024b).')

c += H2('Câu hỏi thường gặp')
c += H3('Nhìn vào mắt người bệnh có bị lây không?')
c += P('Đau mắt đỏ do virus lây chủ yếu qua tiếp xúc trực tiếp với tay bị nhiễm và đồ dùng cá nhân (Azari &amp; Barney, 2013). Vì vậy, rửa tay và không dùng chung đồ quan trọng hơn nhiều so với việc tránh nhìn.')
c += H3('Bị đau mắt đỏ có nên đi học, đi làm?')
c += P('Không nên đi khi còn triệu chứng, nhất là nếu công việc hoặc lớp học cần tiếp xúc gần với người khác. Khi không còn sốt hay triệu chứng khác, có thể quay lại nếu bác sĩ đồng ý (CDC, 2024a).')
c += H3('Đau mắt đỏ bao lâu thì khỏi?')
c += P('Đau mắt đỏ do vi khuẩn thường kéo dài 7 đến 10 ngày, đa số tự khỏi trong 1 đến 2 tuần (Azari &amp; Barney, 2013). Nếu không đỡ sau khoảng 1 tuần, nên đi khám mắt.')

c += H2('Điều gì nên nhớ?')
c += P('Phần lớn đau mắt đỏ do virus và tự khỏi, không cần kháng sinh. Việc cần làm là rửa tay, không dụi mắt, không dùng chung đồ cá nhân, và không tự mua thuốc nhỏ mắt có corticoid. Khi thấy nhìn mờ, đau nhiều, sợ ánh sáng hoặc không đỡ sau một tuần, hãy đi khám mắt.')
c += P('<em>Bài viết mang tính thông tin, không thay thế tư vấn y khoa cho từng cá nhân.</em>')
c += GEN_END + REFS([AZ, CA, CP])

d = dict(slug='dau-mat-do-viem-ket-mac', title='Đau mắt đỏ: nguyên nhân, cách phòng lây và khi nào cần đi khám?',
    seo_title='Đau mắt đỏ: nguyên nhân, cách phòng lây, khi nào đi khám',
    meta_desc='Đau mắt đỏ phần lớn do virus và tự khỏi. Có cần nhỏ kháng sinh không, vì sao không tự dùng thuốc có corticoid, cách phòng lây và khi nào cần đi khám.',
    focus_kw='đau mắt đỏ',
    excerpt='Virus gây đến 80% ca đau mắt đỏ, và kháng sinh không giúp gì trong trường hợp này. Cách phòng lây, thuốc cần tránh và dấu hiệu cần đi khám mắt ngay.',
    tags=['đau mắt đỏ', 'viêm kết mạc', 'kháng sinh', 'phòng bệnh', 'sức khỏe cộng đồng'], content=c, categories=[4, 11],
    date='2026-11-05T08:00:00', cover_alt='Minh họa con mắt đỏ bên cạnh xà phòng rửa tay và khăn mặt riêng, tượng trưng cho phòng lây đau mắt đỏ')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

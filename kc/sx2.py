import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'

APT = 'American Psychological Association. (2024, ngày 8 tháng 7). <em>Answers to your questions about transgender people, gender identity, and gender expression</em>. https://www.apa.org/topics/lgbtq/transgender-people-gender-identity-gender-expression'
APO = 'American Psychological Association. (2008, ngày 29 tháng 10). <em>Understanding sexual orientation and homosexuality</em>. https://www.apa.org/topics/lgbtq/orientation'
WHO = 'World Health Organization. (n.d.). <em>Gender incongruence and transgender health in the ICD</em>. https://www.who.int/standards/classifications/frequently-asked-questions/gender-incongruence-and-transgender-health-in-the-icd'
BYT = 'Bộ Y tế. (2022). <em>Công văn số 4132/BYT-PC về việc chấn chỉnh công tác khám bệnh, chữa bệnh đối với người đồng tính, song tính và chuyển giới</em>. https://luatvietnam.vn/y-te/cong-van-4132-byt-pc-227653-d6.html'

c = ''
c += P('Bản dạng giới là cảm nhận bên trong của một người về việc mình là nam, nữ hay một giới khác. Xu hướng tính dục là việc một người bị hấp dẫn về cảm xúc, lãng mạn hay tình dục với ai. Hai khái niệm này khác nhau: một câu trả lời "mình là ai", một câu trả lời "mình bị thu hút bởi ai" (American Psychological Association [APA], 2024).')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Giới tính sinh học, bản dạng giới, biểu hiện giới và xu hướng tính dục là bốn khái niệm khác nhau.',
    'Người chuyển giới có thể là dị tính, đồng tính, song tính hay vô tính, giống như người không chuyển giới.',
    'Đồng tính, song tính không phải là rối loạn tâm thần (APA, 2008).',
    'Bộ Y tế Việt Nam yêu cầu không coi đồng tính, song tính, chuyển giới là một bệnh (Bộ Y tế, 2022).',
])
c += H2('Bốn khái niệm thường bị nhầm lẫn')
c += P('Theo Hiệp hội Tâm lý học Hoa Kỳ (APA), có thể tách thành bốn khái niệm (APA, 2008, 2024):')
c += TABLE(['Khái niệm', 'Trả lời câu hỏi', 'Giải thích ngắn'], [
    ['Giới tính sinh học', 'Cơ thể được xác định là gì khi sinh ra?', 'Gắn với đặc điểm thể chất như nhiễm sắc thể, hormone, cơ quan sinh dục.'],
    ['Bản dạng giới', 'Mình cảm nhận mình là ai?', 'Cảm nhận bên trong về việc mình là nam, nữ hay một giới khác.'],
    ['Biểu hiện giới', 'Mình thể hiện giới ra bên ngoài thế nào?', 'Qua cách ăn mặc, kiểu tóc, giọng nói, hành vi.'],
    ['Xu hướng tính dục', 'Mình bị hấp dẫn bởi ai?', 'Khuôn mẫu lâu dài về sự hấp dẫn cảm xúc, lãng mạn, tình dục.'],
])
c += P('APA (2024) cũng phân biệt giới tính sinh học với giới: giới là các vai trò, hành vi, hoạt động mà một xã hội cho là phù hợp với nam hay nữ, nên có thể khác nhau giữa các nền văn hóa.')
c += H2('Bản dạng giới là gì?')
c += P('Bản dạng giới là cảm nhận bên trong của một người về việc mình là nam, nữ hay một điều gì khác (APA, 2024). Khi bản dạng giới, biểu hiện giới hay hành vi của một người không khớp với điều thường gắn với giới tính được xác định lúc sinh, người đó có thể được gọi bằng thuật ngữ chung là người chuyển giới (transgender).')
c += P('APA (2024) lưu ý không phải ai có ngoại hình hay hành vi không theo khuôn mẫu giới cũng tự nhận là người chuyển giới. Có người nhận ra bản dạng giới của mình từ rất sớm, có người nhận ra ở tuổi trưởng thành hoặc muộn hơn. Hiện chưa có một lời giải thích duy nhất vì sao một người là người chuyển giới; nhiều chuyên gia cho rằng cả yếu tố sinh học lẫn trải nghiệm sống đều có thể góp phần.')
c += H2('Xu hướng tính dục là gì?')
c += P('Theo APA (2008), xu hướng tính dục là khuôn mẫu lâu dài về sự hấp dẫn cảm xúc, lãng mạn và/hoặc tình dục với nam, nữ hoặc cả hai. Nó cũng gồm cảm nhận bản thân dựa trên sự hấp dẫn đó, các hành vi liên quan và việc thuộc về một cộng đồng có cùng sự hấp dẫn. Ba nhóm thường được nhắc đến là dị tính, đồng tính và song tính, dù nghiên cứu cho thấy xu hướng tính dục trải dài như một dải liên tục.')
c += P('Một vài điểm đáng chú ý từ APA (2008):')
c += UL([
    'Sự hấp dẫn cốt lõi thường hình thành trong khoảng từ giữa thời thơ ấu đến đầu tuổi vị thành niên, và có thể xuất hiện trước khi có bất kỳ trải nghiệm tình dục nào.',
    'Giới khoa học chưa có đồng thuận về nguyên nhân chính xác hình thành một xu hướng tính dục; nhiều người cho rằng cả bẩm sinh lẫn môi trường đều đóng vai trò phức tạp.',
    'Phần lớn mọi người cảm thấy mình có rất ít hoặc không có sự lựa chọn về xu hướng tính dục.',
])
c += H2('Vì sao hai khái niệm này hay bị nhầm?')
c += P('Vì trong đời sống, chúng thường được gộp chung vào một chữ "giới tính". Thực tế, biết bản dạng giới của một người không cho ta biết người đó bị hấp dẫn bởi ai. APA (2024) giải thích người chuyển giới có thể là dị tính, đồng tính, song tính hay vô tính, giống như người không chuyển giới. Họ thường gọi xu hướng tính dục của mình theo bản dạng giới: ví dụ, một người nữ chuyển giới bị hấp dẫn bởi phụ nữ có thể tự nhận là người đồng tính nữ.')
c += P('Tương tự, cách ăn mặc hay biểu hiện giới không nói lên xu hướng tính dục. APA (2024) nêu rõ việc mặc trang phục khác giới là một hình thức biểu hiện giới và không cho biết xu hướng tính dục của người đó.')
c += H2('Đồng tính hay chuyển giới có phải là bệnh?')
c += P('Không. APA (2008) khẳng định đồng tính và song tính không phải là rối loạn, và các tổ chức y tế, sức khỏe tâm thần lớn ở Mỹ đã từ bỏ việc xếp đồng tính vào nhóm rối loạn tâm thần từ lâu. APA cũng cho biết chưa có nghiên cứu khoa học đầy đủ nào chứng minh các liệu pháp nhằm "chuyển đổi" xu hướng tính dục là an toàn hay hiệu quả.')
c += P('Với người chuyển giới, Tổ chức Y tế Thế giới (WHO) đã chuyển "không tương hợp giới" (gender incongruence) trong bảng phân loại bệnh ICD-11 sang chương các tình trạng liên quan đến sức khỏe tình dục. WHO nêu rõ bản dạng chuyển giới và đa dạng giới không phải là tình trạng bệnh lý tâm thần, và việc phân loại như vậy có thể gây kỳ thị rất lớn (World Health Organization [WHO], n.d.).')
c += P('Ở Việt Nam, Công văn số 4132/BYT-PC ngày 3/8/2022 của Bộ Y tế yêu cầu các cơ sở khám chữa bệnh không coi đồng tính, song tính, chuyển giới là một bệnh, và không can thiệp, ép buộc điều trị đối với những người này (Bộ Y tế, 2022).')
c += H2('Kỳ thị ảnh hưởng thế nào?')
c += P('APA (2008) cho biết định kiến và phân biệt đối xử có thể ảnh hưởng tiêu cực đến sức khỏe và hạnh phúc của người đồng tính, song tính, nhất là khi họ phải che giấu bản thân. Với người chuyển giới, APA (2024) giải thích nhiều người không thấy bản dạng giới của mình là điều gây đau khổ; khó khăn lớn thường đến từ việc thiếu chấp nhận của xã hội, phân biệt đối xử hay bạo lực, và những trải nghiệm này có thể dẫn đến lo âu, trầm cảm với tỉ lệ cao hơn.')
c += P('Hiểu đúng các khái niệm là bước đầu để giảm kỳ thị. Bài ' + A('giao-duc-tinh-duc-toan-dien-la-gi-khong-chi-dung-lai-o-tranh-thai', 'giáo dục giới tính toàn diện là gì') + ' giải thích vì sao những chủ đề này nên được dạy một cách khoa học.')
c += H2('Câu hỏi thường gặp')
c += H3('Xu hướng tính dục có tự lựa chọn được không?')
c += P('Theo APA (2008), phần lớn mọi người cảm thấy có rất ít hoặc không có sự lựa chọn về xu hướng tính dục của mình.')
c += H3('Một người có thể biết xu hướng tính dục khi chưa từng quan hệ không?')
c += P('Có. APA (2008) cho biết sự hấp dẫn có thể hình thành mà không cần trải nghiệm tình dục trước đó, và người chưa từng quan hệ vẫn có thể biết xu hướng tính dục của mình.')
c += H3('Nếu băn khoăn về bản dạng giới hay xu hướng tính dục của mình thì nên làm gì?')
c += P('Đó là điều nhiều người trải qua. Trò chuyện với người bạn tin tưởng hoặc tìm đến chuyên gia tâm lý có hiểu biết về giới và tính dục là lựa chọn hợp lý. Theo Bộ Y tế (2022), nếu cần hỗ trợ thì chỉ là hỗ trợ tâm lý, do người có hiểu biết về bản dạng giới thực hiện.')
c += H2('Điều gì nên nhớ?')
c += P('Bản dạng giới là "mình là ai", xu hướng tính dục là "mình bị hấp dẫn bởi ai". Hai điều này độc lập với nhau, và không điều nào là bệnh. Hiểu đúng giúp mỗi người tôn trọng bản thân và người khác hơn. Bài này thuộc chuỗi bài về ' + A('tinh-duc-hoc-la-gi', 'tình dục học') + '.')
c += P('<em>Bài viết mang tính thông tin, không thay thế tư vấn y khoa hoặc tâm lý cho từng cá nhân.</em>')
c += GEN_END + REFS([APO, APT, BYT, WHO])

d = dict(slug='ban-dang-gioi-va-xu-huong-tinh-duc-khac-nhau-the-nao', title='Bản dạng giới và xu hướng tính dục khác nhau thế nào?', seo_title='Bản dạng giới và xu hướng tính dục khác nhau thế nào?',
    meta_desc='Bản dạng giới là "mình là ai", xu hướng tính dục là "mình bị hấp dẫn bởi ai". Phân biệt 4 khái niệm dễ nhầm theo APA, WHO và Bộ Y tế Việt Nam.',
    focus_kw='bản dạng giới và xu hướng tính dục', excerpt='Bản dạng giới và xu hướng tính dục là hai khái niệm khác nhau. Phân biệt cùng giới tính sinh học và biểu hiện giới, và vì sao không điều nào là bệnh.',
    tags=['sức khỏe tình dục', 'bản dạng giới', 'xu hướng tính dục', 'LGBT', 'giáo dục giới tính'], content=c, categories=[4, 11, 13],
    date='2026-10-26T11:30:00', cover_alt='Minh họa hai vòng tròn tách biệt, một vòng mang biểu tượng người và một vòng mang biểu tượng trái tim, gợi hai khái niệm khác nhau')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']))

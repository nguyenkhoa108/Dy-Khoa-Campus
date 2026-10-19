import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'

DO = 'Đỗ, K. (2018, ngày 29 tháng 1). [BSI case study] Neptune: chiến dịch “Hiểu để yêu thương”. <em>Brands Vietnam</em>. https://www.brandsvietnam.com/congdong/topic/8823-BSI-case-study-Neptune-chien-dich-Hieu-De-Yeu-Thuong'
NU = 'Nguyễn, T. D. U. (2019, ngày 20 tháng 9). The Brief #8: Neptune, giọt dầu vàng khởi ngàn tài lộc. <em>Brands Vietnam</em>. https://www.brandsvietnam.com/congdong/topic/20483-The-Brief-8-Neptune-Giot-dau-vang-khoi-ngan-tai-loc'
BV = 'Brands Vietnam. (2019, ngày 26 tháng 2). <em>Không còn lấy nước mắt người tiêu dùng, Neptune Tết năm nay thành công hay thất bại?</em> https://www.brandsvietnam.com/17825-khong-con-lay-nuoc-mat-nguoi-tieu-dung-neptune-tet-nam-nay-thanh-cong-hay-that-bai'
APG = 'Account Planning Group. (2015, ngày 30 tháng 6). <em>What is planning? A view from Vaughan Edmonds</em>. https://www.apg.org.uk/single-post/2015/06/30/what-is-planning'

c = ''
c += P('Insight khách hàng là cách lý giải vì sao khách hàng nghĩ, cảm và hành động như vậy, chứ không chỉ mô tả họ làm gì. Rất nhiều bản đề xuất ghi "Insight: 70% người dùng quan tâm đến giá", nhưng đó mới là một phát hiện từ dữ liệu (finding). Insight bắt đầu khi ta trả lời được câu hỏi "vì sao", và câu trả lời đó mở ra hướng đi cho thông điệp.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Finding trả lời "cái gì đang xảy ra"; insight trả lời "vì sao nó xảy ra" và "điều đó có ý nghĩa gì với thông điệp".',
    'Insight không thay thế dữ liệu; nó được rút ra từ dữ liệu và quan sát.',
    'Với người làm hoạch định chiến lược, insight là bước cần có trước khi bàn đến ý tưởng sáng tạo (Account Planning Group [APG], 2015).',
    'Insight cần được làm mới khi bối cảnh thay đổi, như cách Neptune thay đổi thông điệp Tết qua các năm.',
])
c += H2('Insight khách hàng là gì?')
c += P('Trong bài này, insight khách hàng được hiểu là một cách diễn giải về động cơ, niềm tin hay cảm xúc ẩn sau hành vi của khách hàng, đủ sâu để gợi ra hướng đi cho chiến lược truyền thông. Trong tiếng Anh, khái niệm này thường được gọi là consumer insight hoặc customer insight.')
c += P('Trong nghề hoạch định chiến lược quảng cáo (account planning), insight được xem là điểm khởi đầu. Một bài viết trên trang của Account Planning Group (Anh) cho rằng trước chất lượng sáng tạo và khâu thực thi là nhu cầu có một insight chất lượng, và vai trò của người hoạch định là dẫn dắt sản phẩm của agency, thông qua insight, về hướng có tiềm năng lớn nhất cho khách hàng (APG, 2015).')
c += H2('Insight khác finding thế nào?')
c += P('Có thể phân biệt bằng câu hỏi mỗi loại trả lời:')
c += UL([
    '<strong>Finding</strong> là điều đọc được trực tiếp từ dữ liệu: một con số, một hành vi, một xu hướng. Nó trả lời "cái gì".',
    '<strong>Insight</strong> là phần diễn giải: vì sao con số đó như vậy, khách hàng đang nghĩ và cảm thấy gì. Nó trả lời "vì sao" và gợi ra "nên nói gì".',
])
c += P('Finding không kém giá trị; nó là nguyên liệu. Vấn đề chỉ nảy sinh khi ta dừng ở finding và gọi đó là insight, bỏ qua bước diễn giải.')
c += H2('Ví dụ: Neptune và chiến dịch "Hiểu để yêu thương" (Tết 2018)')
c += P('Phân tích của Brands Vietnam về chiến dịch Tết 2018 của dầu ăn Neptune cho thấy rõ hai lớp này (Đỗ, 2018):')
c += UL([
    '<strong>Finding:</strong> theo khảo sát của ActionAid Việt Nam được bài viết trích, phụ nữ dành trung bình 5 giờ mỗi ngày, tương đương khoảng 2,5 tháng mỗi năm, cho việc nhà.',
    '<strong>Insight:</strong> việc bếp núc được "mặc định" là vai trò của người phụ nữ, và phụ nữ ít khi than phiền vì xem đó là cách thể hiện tình yêu, giữ ấm cho gia đình.',
])
c += P('Nếu dừng ở finding, thông điệp dễ trở thành "sản phẩm giúp nấu nhanh hơn". Insight cho phép chiến dịch nói về cảm xúc phía sau việc bếp núc, thay vì chỉ nói về công dụng của sản phẩm.')
c += H2('Insight có cần thay đổi theo thời gian không?')
c += P('Có. Sang Tết 2019, Neptune rời nền tảng thông điệp đoàn viên quen thuộc (Nguyễn, 2019). Theo Brands Vietnam, thương hiệu không còn "lấy nước mắt" người xem mà chuyển sang thông điệp tươi sáng "Giọt dầu vàng khởi ngàn tài lộc", dựa trên niềm tin rằng hành động đầu năm sẽ quyết định tài vận cả năm (Brands Vietnam, 2019). Bài phỏng vấn trên Brands Vietnam gắn ý tưởng "khai bếp" của chiến dịch với quan niệm "đầu năm bếp ấm, nhà mới an, giàu sang sẽ đến" (Nguyễn, 2019).')
c += P('Bài học ở đây là insight không phải chân lý cố định. Khi một thông điệp đã quá quen, hoặc bối cảnh văn hóa thay đổi, thương hiệu có thể cần một insight mới, kể cả trong cùng một dịp như Tết.')
c += H2('Đi từ dữ liệu đến insight thế nào?')
c += P('Không có công thức duy nhất, nhưng có thể tự đặt các câu hỏi sau khi đọc dữ liệu:')
c += UL([
    '<strong>Con số này nói gì?</strong> Ghi lại finding một cách trung thực, không thêm diễn giải.',
    '<strong>Vì sao lại như vậy?</strong> Hỏi tiếp nhiều lần, đừng dừng ở câu trả lời đầu tiên.',
    '<strong>Khách hàng cảm thấy gì về điều này?</strong> Nhìn từ vị trí của họ, tránh phán xét.',
    '<strong>Có quan sát định tính nào củng cố không?</strong> Phỏng vấn, bình luận, hành vi thực tế.',
    '<strong>Điều này gợi ra thông điệp gì?</strong> Nếu không suy ra được hướng đi nào, có thể ta vẫn đang ở mức finding.',
])
c += P('Bước tiếp theo, từ insight đến ý tưởng lớn, được trình bày trong bài ' + A('tu-insight-khach-hang-den-big-idea', 'Từ insight khách hàng đến big idea') + '. Nếu muốn học bài bản, có thể tham khảo khóa <a href="https://dykhoa.com/blog/courses/chien-luoc-sang-tao-trong-truyen-thong-tu-insight-den-big-idea/">Chiến lược sáng tạo trong truyền thông: từ insight đến big idea</a>.')
c += H2('Checklist: câu insight của bạn đã đạt chưa?')
c += UL([
    'Câu này giải thích "vì sao" hay chỉ mô tả lại "cái gì"?',
    'Nếu bỏ hết số liệu, câu này còn nói được điều gì về con người không?',
    'Đây là cảm nhận thật của khách hàng, hay là phán xét của người viết?',
    'Từ câu này có suy ra được một hướng đi sáng tạo cụ thể không?',
    'Insight này còn mới, hay đã bị nhiều thương hiệu khai thác đến bão hòa?',
])
c += H2('Câu hỏi thường gặp')
c += H3('Insight khách hàng và customer insight có phải là một?')
c += P('Có. "Insight khách hàng" là cách gọi phổ biến trong tiếng Việt của consumer insight hoặc customer insight.')
c += H3('Một chiến dịch có thể có nhiều insight không?')
c += P('Có thể, nhưng thường nên có một insight trung tâm để thông điệp không bị phân tán; các insight khác đóng vai trò bổ trợ.')
c += H3('Không có ngân sách nghiên cứu lớn thì có tìm được insight không?')
c += P('Có. Dữ liệu sẵn có, quan sát và vài cuộc trò chuyện sâu với khách hàng đều có thể là điểm khởi đầu. Quan trọng là đặt câu hỏi "vì sao" đủ sâu và diễn giải trung thực.')
c += H2('Điều gì nên nhớ?')
c += P('Finding là điểm khởi đầu, insight là bước diễn giải giúp thông điệp chạm đến người nhận. Hãy luôn hỏi "vì sao", nhìn từ vị trí của khách hàng, và sẵn sàng làm mới insight khi bối cảnh thay đổi. Cách đưa insight vào kế hoạch truyền thông có trong bài ' + A('lap-ke-hoach-truyen-thong-theo-chuan-oasis', 'lập kế hoạch truyền thông theo chuẩn OASIS') + '.')
c += GEN_END + REFS([APG, BV, DO, NU])

d = dict(id=729, slug='insight-khach-hang-la-gi', title='Insight khách hàng là gì? Cách phân biệt insight và finding trong truyền thông',
    seo_title='Insight khách hàng là gì? Phân biệt insight và finding',
    meta_desc='Insight khách hàng là gì, khác finding thế nào? Ví dụ thật từ chiến dịch Tết của Neptune, cách đi từ dữ liệu đến insight và checklist kiểm tra một câu insight.',
    focus_kw='insight khách hàng là gì', excerpt='Finding cho biết khách hàng làm gì, insight giải thích vì sao. Phân biệt hai khái niệm qua ví dụ chiến dịch Tết của Neptune và checklist kiểm tra insight.', content=c)
json.dump(d, open(os.path.join(H, 'ins.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']))

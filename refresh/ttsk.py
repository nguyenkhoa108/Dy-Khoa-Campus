import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'

GU = 'Guidry, J. P., Carlyle, K. E., LaRose, J. G., Perrin, P., Messner, M., &amp; Ryan, M. (2019). Using the Health Belief Model to analyze Instagram posts about Zika for public health communications. <em>Emerging Infectious Diseases, 25</em>(1), 179-180. https://wwwnc.cdc.gov/eid/article/25/1/18-0824_article'
HP = 'Office of Disease Prevention and Health Promotion. (n.d.). <em>Health communication</em>. Healthy People 2030, U.S. Department of Health and Human Services. https://odphp.health.gov/healthypeople/objectives-and-data/browse-objectives/health-communication'
IK = 'Ishikawa, H., &amp; Kiuchi, T. (2010). Health literacy and health communication. <em>BioPsychoSocial Medicine, 4</em>, 18. https://doi.org/10.1186/1751-0759-4-18'
JO = 'Jones, C. L., Jensen, J. D., Scherr, C. L., Brown, N. R., Christy, K., &amp; Weaver, J. (2015). The Health Belief Model as an explanatory framework in communication research: Exploring parallel, serial, and moderated mediation. <em>Health Communication, 30</em>(6), 566-576. https://doi.org/10.1080/10410236.2013.873363'
NI = 'Niederdeppe, J., Boyd, A. D., King, A. J., &amp; Rimal, R. N. (2025). Strategies for effective public health communication in a complex information environment. <em>Annual Review of Public Health, 46</em>, 411-431. https://doi.org/10.1146/annurev-publhealth-071723-120721'

c = ''
c += P('Truyền thông sức khỏe (health communication) là các hoạt động truyền thông liên cá nhân hoặc truyền thông đại chúng nhằm cải thiện sức khỏe của cá nhân và cộng đồng (Ishikawa &amp; Kiuchi, 2010). Lĩnh vực này bao trùm từ cuộc trò chuyện giữa bác sĩ và bệnh nhân, một tờ thông tin về bệnh, đến một chiến dịch tiêm chủng quốc gia hay một bài đăng trên mạng xã hội. Truyền thông sức khỏe hiệu quả giúp người dân dễ dàng hiểu và hành động dựa trên thông tin sức khỏe (Office of Disease Prevention and Health Promotion [ODPHP], n.d.).')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Truyền thông sức khỏe liên quan đến nhiều lĩnh vực, từ quan hệ bác sĩ, bệnh nhân đến truyền thông rủi ro và y tế từ xa (Ishikawa &amp; Kiuchi, 2010).',
    'Nên xem truyền thông sức khỏe là một quá trình, với sự tương tác giữa nguồn, thông điệp, kênh và công chúng, chứ không chỉ là một sản phẩm như tờ rơi (Niederdeppe và cộng sự, 2025).',
    'Thông điệp cảnh báo hiệu quả hơn khi cho người nhận biết cách hành động và hành động đó có tác dụng (Niederdeppe và cộng sự, 2025).',
    'Thông tin sai lệch là thách thức lớn; ba chiến lược gồm lấp khoảng trống thông tin, đính chính có bằng chứng và tiêm phòng tâm lý.',
])

c += H2('Truyền thông sức khỏe bao gồm những gì?')
c += P('Ishikawa và Kiuchi (2010) cho biết, theo dự án Healthy People 2010 của Hoa Kỳ, truyền thông sức khỏe có thể đóng góp vào mọi khía cạnh của phòng bệnh và nâng cao sức khỏe, và liên quan đến tám lĩnh vực:')
c += UL([
    'Quan hệ giữa nhân viên y tế và bệnh nhân.',
    'Việc người dân tiếp xúc, tìm kiếm và sử dụng thông tin sức khỏe.',
    'Việc tuân thủ khuyến nghị và phác đồ điều trị.',
    'Xây dựng thông điệp và chiến dịch y tế công cộng.',
    'Phổ biến thông tin về rủi ro sức khỏe cá nhân và cộng đồng, tức ' + '<a href="https://dykhoa.com/blog/thuat-ngu/truyen-thong-rui-ro-risk-communication/">truyền thông rủi ro</a>' + '.',
    'Hình ảnh sức khỏe trên truyền thông đại chúng và trong văn hóa.',
    'Hướng dẫn người dân cách tiếp cận hệ thống y tế.',
    'Phát triển các ứng dụng y tế từ xa.',
])
c += P('Các tác giả cũng nhấn mạnh mối liên hệ chặt chẽ giữa truyền thông sức khỏe và ' + 'hiểu biết sức khỏe' + ' (health literacy), tức khả năng tìm, xử lý và hiểu thông tin sức khỏe để ra quyết định phù hợp (Ishikawa &amp; Kiuchi, 2010). Đến Healthy People 2030, trọng tâm là giúp mọi người dễ dàng hiểu và hành động theo thông tin sức khỏe, đặc biệt người có hiểu biết sức khỏe hạn chế hoặc không dùng tiếng Anh là ngôn ngữ chính (ODPHP, n.d.).')

c += H2('Truyền thông sức khỏe là một quá trình')
c += P('Niederdeppe và cộng sự (2025) đề xuất nhìn truyền thông sức khỏe như một quá trình chứ không chỉ là một sản phẩm. Quá trình này có thể được hiểu qua sự tương tác giữa bốn yếu tố:')
c += TABLE(['Yếu tố', 'Ý nghĩa'], [
    ['Nguồn (source)', 'Ai phát đi thông điệp. Mức tin cậy và uy tín của nguồn do chính công chúng cảm nhận.'],
    ['Thông điệp (message)', 'Nội dung, cách diễn đạt và lượng thông tin.'],
    ['Kênh (channel)', 'Phương tiện truyền tải. Có kênh chứa được nhiều nội dung như tờ rơi, có kênh rất ngắn như quảng cáo 30 giây.'],
    ['Công chúng (audience)', 'Mối quan tâm, khả năng và động cơ của người nhận, tương tác với cả ba yếu tố còn lại.'],
])
c += P('Theo các tác giả, đưa thông điệp chiến lược đến đúng công chúng, từ nguồn họ tin, qua kênh họ dùng và tin tưởng, không phải là một công thức cố định. Vì vậy, <strong>phân khúc công chúng</strong> (chia công chúng thành các nhóm nhỏ theo đặc điểm có ý nghĩa) và <strong>cá nhân hóa thông điệp</strong> (tailoring) là các bước quan trọng (Niederdeppe và cộng sự, 2025).')

c += H2('Đo hiệu quả: "tác động" khác "hiệu quả" thế nào?')
c += P('Niederdeppe và cộng sự (2025) phân biệt hai khái niệm:')
c += UL([
    '<strong>Tác động (effects):</strong> thường được kiểm tra trong điều kiện kiểm soát, ví dụ thử nghiệm xem một thông điệp có tạo ra thay đổi hay không.',
    '<strong>Hiệu quả (effectiveness):</strong> liệu các mục tiêu đặt ra có đạt được hay không, và liệu một chiến dịch có hoạt động trong điều kiện thực tế.',
])
c += P('Một thông điệp có tác động trong phòng thí nghiệm chưa chắc đã hiệu quả khi triển khai rộng. Bài ' + '<a href="https://dykhoa.com/blog/thuat-ngu/thu-nghiem-thong-diep-message-testing/">thử nghiệm thông điệp</a>' + ' giải thích cách kiểm tra thông điệp trước khi phát hành.')

c += H2('Các mô hình lý thuyết thường dùng')
c += H3('Mô hình niềm tin sức khỏe (Health Belief Model)')
c += P('Mô hình này cho rằng thông điệp đạt hiệu quả thay đổi hành vi tốt nhất khi tác động được vào nhận thức về rào cản, lợi ích, sự tự tin vào năng lực bản thân và mức độ đe dọa của bệnh (Jones và cộng sự, 2015). Trong nghiên cứu về một chiến dịch tiêm vắc xin cúm, mức độ tiếp xúc với chiến dịch có liên quan tích cực với hành vi tiêm chủng (Jones và cộng sự, 2015).')
c += P('Mô hình này cũng giúp phân tích nội dung truyền thông. Khi phân tích các bài đăng Instagram về dịch Zika, Guidry và cộng sự (2019) thấy nhận thức về mức độ nghiêm trọng (75,8%) và nguy cơ mắc bệnh (59,9%) xuất hiện nhiều nhất, trong khi rào cản (2,8%), lời kêu gọi hành động (10,2%) và yếu tố tự tin vào năng lực (9,6%) rất hiếm. Nói cách khác, các bài đăng chủ yếu cảnh báo, ít hướng dẫn người xem cách hành động.')
c += H3('Mô hình quy trình song song mở rộng (EPPM)')
c += P('Theo mô hình này, con người dễ hành động phòng ngừa hơn khi vừa có động lực, ví dụ nhận thức được nguy cơ, vừa tin rằng mình có khả năng (tự tin vào năng lực) và có cách hiệu quả để hành động (hiệu quả của hành động). Bằng chứng phân tích gộp cho thấy thông điệp gây sợ có tác động mạnh hơn khi kèm thông tin về hiệu quả của hành động được khuyến nghị (Niederdeppe và cộng sự, 2025).')
c += H3('Tiếp cận đa cấp độ')
c += P('Niederdeppe và cộng sự (2025) kêu gọi tích hợp tư duy đa cấp độ: hành vi sức khỏe chịu ảnh hưởng từ yếu tố cá nhân, quan hệ liên cá nhân, cộng đồng và chính sách. Nếu bỏ qua các nguồn bất bình đẳng như khả năng tiếp cận thông tin và rào cản hệ thống, truyền thông sức khỏe có thể vô tình làm khoảng cách sức khỏe rộng thêm.')

c += H2('Thách thức: thông tin sai lệch')
c += P('Niederdeppe và cộng sự (2025) nêu ba hướng xử lý thông tin sai lệch về sức khỏe:')
c += UL([
    '<strong>Lấp khoảng trống thông tin:</strong> thông tin sai lan nhanh hơn khi thiếu thông tin rõ ràng, chính xác về một chủ đề.',
    '<strong>Đính chính có bằng chứng:</strong> khi một thông tin sai lan rộng và có dấu hiệu gây hại, việc đính chính rõ ràng, dựa trên bằng chứng có thể giảm niềm tin sai và xu hướng chia sẻ. Hiệu quả phụ thuộc vào mức chi tiết, sự lặp lại và độ tin cậy của nguồn đính chính.',
    '<strong>Tiêm phòng tâm lý (prebunking):</strong> giúp công chúng tránh, bác bỏ và ít chia sẻ thông tin sai.',
])
c += P('Các tác giả cũng lưu ý không nên đặt toàn bộ trách nhiệm thay đổi lên người tiếp nhận thông tin. Bài ' + A('tiem-phong-tam-ly-psychological-inoculation-tin-gia-khoa-hoc', 'tiêm phòng tâm lý trước tin giả khoa học') + ' phân tích sâu hơn.')

c += H2('Truyền thông sức khỏe khác truyền thông khoa học thế nào?')
c += P('Hai lĩnh vực giao nhau nhiều. Truyền thông sức khỏe thường gắn với mục tiêu cải thiện sức khỏe và hành vi cụ thể, như tiêm chủng, tầm soát, tuân thủ điều trị, trong khi ' + A('truyen-thong-khoa-hoc-la-gi', 'truyền thông khoa học') + ' có phạm vi rộng hơn, bao gồm cả mục tiêu tạo hứng thú và hiểu biết về khoa học. Bài ' + A('truyen-thong-khoa-hoc-va-truyen-thong-y-te-giong-khac-nhau', 'truyền thông khoa học và truyền thông y tế giống, khác nhau thế nào') + ' so sánh chi tiết.')

c += H2('Câu hỏi thường gặp')
c += H3('Truyền thông sức khỏe có phải chỉ là làm tờ rơi, áp phích?')
c += P('Không. Đó chỉ là sản phẩm. Truyền thông sức khỏe là cả một quá trình, gồm xác định vấn đề, hiểu công chúng, chọn nguồn và kênh, thiết kế thông điệp và đánh giá kết quả (Niederdeppe và cộng sự, 2025).')
c += H3('Vì sao thông điệp gây sợ đôi khi không hiệu quả?')
c += P('Theo EPPM, nếu thông điệp chỉ nhấn mạnh nguy cơ mà không cho người nhận biết cách hành động hiệu quả, họ khó thực hiện hành động phòng ngừa. Thông điệp gây sợ mạnh hơn khi kèm thông tin về hiệu quả của hành động (Niederdeppe và cộng sự, 2025).')
c += H3('Ai làm truyền thông sức khỏe?')
c += P('Nhân viên y tế, cơ quan y tế công cộng, nhà báo sức khỏe, người làm truyền thông cho bệnh viện, tổ chức phi chính phủ và người sáng tạo nội dung. Theo Ishikawa và Kiuchi (2010), cả truyền thông liên cá nhân như buổi khám bệnh và truyền thông đại chúng đều thuộc lĩnh vực này.')

c += H2('Điều gì nên nhớ?')
c += P('Truyền thông sức khỏe không chỉ là "nói cho người dân biết điều gì tốt cho họ". Đó là một quá trình chiến lược, dựa trên lý thuyết hành vi, đòi hỏi hiểu đúng công chúng, chọn nguồn và kênh họ tin, thiết kế thông điệp cho thấy cách hành động, và đánh giá hiệu quả trong thực tế. Bài này thuộc ' + HUB + '.')
c += GEN_END + REFS([GU, IK, JO, NI, HP])

d = dict(id=317, slug='truyen-thong-suc-khoe-la-gi', title='Truyền thông sức khỏe là gì?',
    seo_title='Truyền thông sức khỏe là gì? Định nghĩa, quá trình và mô hình',
    meta_desc='Truyền thông sức khỏe là gì? Định nghĩa, 8 lĩnh vực, quá trình nguồn, thông điệp, kênh, công chúng, các mô hình HBM, EPPM và cách xử lý thông tin sai lệch.',
    focus_kw='truyền thông sức khỏe là gì',
    excerpt='Truyền thông sức khỏe là gì? Định nghĩa, các lĩnh vực chính, quá trình truyền thông, mô hình lý thuyết thường dùng và cách ứng phó với thông tin sai lệch.', content=c)
json.dump(d, open(os.path.join(H, 'ttsk.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

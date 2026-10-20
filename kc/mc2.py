import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'

CK = 'Carrette, J., &amp; King, R. (2005). <em>Selling spirituality: The silent takeover of religion</em>. Routledge.'
EI = 'Einstein, M. (2010, ngày 16 tháng 5). Brands of faith: Marketing religion [Phỏng vấn "Ten questions for Mara Einstein"]. <em>Religion Dispatches</em>. https://religiondispatches.org/brands-of-faith-marketing-religion/'
WE = 'Weeks, L. B. (2000, ngày 23 tháng 2). At home in the spiritual market place [Điểm sách <em>Spiritual marketplace</em> của W. C. Roof]. <em>The Christian Century</em>. https://www.religion-online.org/?p=7764'
PW = 'Publishers Weekly. (1999, ngày 4 tháng 10). <em>Spiritual marketplace: Baby boomers and the remaking of American religion</em> [Điểm sách]. https://www.publishersweekly.com/9780691016597'

c = ''
c += P('Thương mại hóa tâm linh là quá trình các hoạt động tâm linh, từ tôn giáo đến thiền, chữa lành, phong thủy, được đóng gói, xây dựng thương hiệu và bán như một sản phẩm. Giới học thuật đã nghiên cứu hiện tượng này từ nhiều thập niên. Ba tác phẩm thường được nhắc đến cho ba góc nhìn khác nhau: <em>Spiritual Marketplace</em> của Wade Clark Roof (xuất bản năm 1999) mô tả "thị trường tâm linh", <em>Brands of Faith</em> của Mara Einstein (năm 2008) phân tích tôn giáo như thương hiệu, và <em>Selling Spirituality</em> của Jeremy Carrette và Richard King (năm 2005) phê phán việc tâm linh bị thị trường chiếm lĩnh.')
c += P('Bài ' + A('khung-truyen-thong-dich-vu-tam-linh', 'khung truyền thông dịch vụ tâm linh') + ' đã đưa ra năm nguyên tắc thực hành. Bài này lùi lại một bước để hỏi: vì sao tâm linh lại vận hành như một thị trường, và người làm truyền thông nên hiểu điều đó thế nào?')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    '<strong>Roof:</strong> người hiện đại không còn chỉ theo tôn giáo của gia đình, mà tự "tìm kiếm" và tự ghép nối bản sắc tâm linh trong một thị trường rộng mở.',
    '<strong>Einstein:</strong> trong môi trường ngập quảng cáo, tôn giáo phải tiếp thị như một thương hiệu để còn hiện diện; bà gọi đó là "điều xấu cần thiết".',
    '<strong>Carrette và King:</strong> "tâm linh" là tôn giáo được đổi thương hiệu để phục vụ thị trường, biến khổ đau xã hội thành vấn đề cá nhân.',
    'Ba góc nhìn bổ sung cho nhau: mô tả, giải thích và phê phán.',
])

c += H2('Roof: "thị trường tâm linh" và người đi tìm')
c += P('Nhà xã hội học tôn giáo Wade Clark Roof nghiên cứu thế hệ bùng nổ dân số (baby boomers) ở Mỹ qua khảo sát và phỏng vấn. Theo các bài điểm sách, cuốn <em>Spiritual Marketplace</em> mô tả cách thế hệ này tái định hình tôn giáo Mỹ thông qua một "văn hóa tìm kiếm" (quest culture), đặt cá nhân lên trên thiết chế (Publishers Weekly, 1999).')
c += P('Weeks (2000) tóm tắt một số ý chính của Roof:')
c += UL([
    'Ranh giới cộng đồng tôn giáo đang được vẽ lại khi con người theo đuổi hành trình tâm linh riêng trong một "thị trường tâm linh mở rộng".',
    'Con người vừa muốn tự do vừa muốn có điểm tựa, nên phần lớn tự "ứng biến" bản sắc tôn giáo của mình.',
    'Khi không còn khuôn khổ được truyền lại, mỗi người tự ghép nối câu trả lời cho nhu cầu tâm linh, điều Roof gọi là "tâm linh phản tư" (reflexive spirituality).',
    'Bên dưới các cuộc tìm kiếm là một "cơn đói sự trọn vẹn" (wholeness hunger).',
])
c += P('Publishers Weekly (1999) cũng lưu ý rằng ẩn dụ "thị trường" có thể đơn giản hóa hiện tượng. Dù vậy, khái niệm này giúp giải thích vì sao ngày nay một người có thể vừa đi chùa, vừa xem tarot, vừa tham gia khóa thiền mà không thấy mâu thuẫn.')
c += P('<strong>Gợi ý cho truyền thông:</strong> người dùng dịch vụ tâm linh thường là người đang tìm kiếm, nhiều khi trong lúc bất an. Đó là lý do khung truyền thông nhấn mạnh việc không khai thác nỗi sợ.')

c += H2('Einstein: khi tôn giáo trở thành thương hiệu')
c += P('Mara Einstein phân tích cách các tổ chức tôn giáo dùng công cụ tiếp thị trong cuốn <em>Brands of Faith: Marketing Religion in a Commercial Age</em> (Routledge, 2008). Trong một cuộc phỏng vấn về cuốn sách, bà giải thích (Einstein, 2010):')
c += UL([
    'Thương hiệu là cách làm một sản phẩm trở nên khác biệt, được tạo nên từ tên gọi, biểu tượng và "huyền thoại" của nó. Tôn giáo ngày nay vận hành tương tự, khi những mục sư nổi tiếng hay nhà thờ lớn thay thế các giáo phái làm "nhận diện" chính.',
    'Mỗi ngày con người tiếp xúc hơn 3.000 thông điệp tiếp thị, nên tiếp thị tôn giáo là "một điều xấu cần thiết" để tôn giáo còn là một phần của đời sống văn hóa.',
    'Người tìm kiếm tâm linh không còn bị ràng buộc vào đức tin của cha mẹ, và truyền thông giúp họ dễ dàng tìm hiểu, thậm chí kết hợp các niềm tin khác nhau.',
    'Tiếp thị không chỉ là quảng cáo, mà gồm cả sản phẩm, giá, phân phối và xúc tiến.',
])
c += P('Góc nhìn của Einstein gắn trực tiếp với mô hình ' + '<a href="https://dykhoa.com/blog/thuat-ngu/phoi-thuc-marketing-marketing-mix-4p/">phối thức marketing 4P</a>' + ': khi một dịch vụ tâm linh có "giá", có "kênh phân phối" và có chiến dịch quảng bá, nó cũng phải chịu các chuẩn mực của hoạt động quảng cáo.')
c += P('<strong>Gợi ý cho truyền thông:</strong> thừa nhận dịch vụ tâm linh đang được tiếp thị là bước đầu để áp dụng các chuẩn mực minh bạch về giá, về người thực hiện và về quan hệ thương mại.')

c += H2('Carrette và King: phê phán "tâm linh tư bản"')
c += P('Trong phần mở đầu cuốn <em>Selling Spirituality</em>, Carrette và King (2005) đưa ra lập luận mạnh nhất trong ba tác phẩm:')
c += UL([
    'Tôn giáo được "đổi thương hiệu" thành "tâm linh" để phục vụ hệ tư tưởng của chủ nghĩa tư bản.',
    'Các hình thức "tâm linh tư bản" xuất hiện cùng sự trỗi dậy của tư bản tài chính toàn cầu, trong bối cảnh nới lỏng quản lý và thu hẹp phúc lợi nhà nước.',
    'Tâm linh bị đóng khung thành chuyện tự hoàn thiện cá nhân, trở thành công cụ của thị trường thay vì hướng tới khuôn khổ đạo đức và xã hội rộng hơn.',
    'Chữ "tâm linh" được dùng để làm sản phẩm và phương pháp quản trị trông có vẻ lành mạnh.',
    'Cách hiểu tâm linh hoàn toàn cá nhân có thể làm tăng sự cô lập mà nó hứa chữa lành, vì che đi nguyên nhân xã hội của khổ đau.',
])
c += P('Lập luận này là nền tảng lý thuyết sát nhất với hiện tượng ' + A('hoi-chung-wellness-bay-chua-lanh-thuong-mai-hoa', '"chữa lành" thương mại hóa') + ' đang phổ biến hiện nay.')
c += P('<strong>Gợi ý cho truyền thông:</strong> khi một thông điệp "chữa lành" hứa giải quyết mọi khó khăn bằng một khóa học hay một buổi trị liệu, nó có thể đang biến những vấn đề cần hỗ trợ y tế, tâm lý hay xã hội thành một món hàng cá nhân.')

c += H2('Ba góc nhìn đặt cạnh nhau')
c += TABLE(['', 'Roof', 'Einstein', 'Carrette và King'], [
    ['Cách tiếp cận', 'Mô tả, xã hội học', 'Giải thích, marketing', 'Phê phán, triết học, chính trị'],
    ['Người dùng được nhìn như', 'Người đi tìm, tự ghép nối niềm tin', 'Người tiêu dùng có nhiều lựa chọn', 'Cá nhân bị thị trường định hình'],
    ['Tiếp thị được nhìn như', 'Hệ quả của thị trường mở', '"Điều xấu cần thiết"', 'Cơ chế chiếm lĩnh tôn giáo'],
    ['Câu hỏi cho người làm truyền thông', 'Người dùng đang tìm điều gì?', 'Thông điệp có minh bạch như một hoạt động tiếp thị?', 'Thông điệp có biến khổ đau xã hội thành món hàng?'],
])
c += P('Bảng do người viết tổng hợp. Ba góc nhìn không loại trừ nhau: có thể vừa thừa nhận tâm linh là một thị trường, vừa dùng công cụ tiếp thị, vừa giữ thái độ phê phán với những thông điệp trục lợi.')

c += H2('Áp dụng vào bối cảnh Việt Nam cần lưu ý gì?')
c += P('Ba tác phẩm chủ yếu dựa trên bối cảnh Mỹ và phương Tây, nơi tôn giáo có tổ chức đóng vai trò lớn. Ở Việt Nam, đời sống tâm linh gắn nhiều với tín ngưỡng dân gian, thờ cúng tổ tiên, lễ hội và các dịch vụ như xem ngày, phong thủy. Vì vậy, các khái niệm này nên được dùng như công cụ gợi mở, không áp dụng nguyên khuôn. Đây cũng là một khoảng trống nghiên cứu đáng quan tâm cho truyền thông và văn hóa học ở Việt Nam.')
c += P('Năm nguyên tắc trong ' + A('khung-truyen-thong-dich-vu-tam-linh', 'khung truyền thông dịch vụ tâm linh') + ' có thể được đọc lại qua ba lăng kính này: không khai thác nỗi sợ của người đi tìm (góc nhìn của Roof), minh bạch như mọi hoạt động tiếp thị (góc nhìn của Einstein), và không biến vấn đề sức khỏe, xã hội thành món hàng tâm linh (góc nhìn của Carrette và King).')

c += H2('Câu hỏi thường gặp')
c += H3('Tiếp thị một dịch vụ tâm linh có sai không?')
c += P('Không nhất thiết. Einstein (2010) xem tiếp thị là điều cần thiết để tôn giáo còn hiện diện trong đời sống văn hóa. Vấn đề nằm ở cách tiếp thị: có minh bạch, có hứa điều không thể chứng minh, có khai thác nỗi sợ hay không.')
c += H3('"Tâm linh" và "tôn giáo" khác nhau thế nào trong các nghiên cứu này?')
c += P('Carrette và King (2005) cho rằng "tâm linh" trong xã hội hiện đại thường là tôn giáo đã được tách khỏi cộng đồng và truyền thống, đóng gói lại cho từng cá nhân. Roof, theo Weeks (2000), mô tả xu hướng con người tự ghép nối niềm tin thay vì theo trọn một truyền thống.')
c += H3('Nên đọc tác phẩm nào trước?')
c += P('Nếu quan tâm đến hành vi người dùng, nên bắt đầu với Roof. Nếu làm marketing, truyền thông, Einstein gần gũi nhất. Nếu muốn phân tích phê phán hiện tượng chữa lành, wellness, hãy đọc Carrette và King.')

c += H2('Điều gì nên nhớ?')
c += P('Tâm linh ngày nay vừa là niềm tin, vừa là một thị trường. Roof giúp hiểu người dùng, Einstein giúp hiểu cơ chế tiếp thị, còn Carrette và King nhắc rằng không phải điều gì bán chạy cũng có lợi cho người mua. Người làm truyền thông có trách nhiệm cần giữ cả ba góc nhìn này cùng lúc.')
c += GEN_END + REFS([CK, EI, PW, WE])

d = dict(slug='thuong-mai-hoa-tam-linh-3-goc-nhin-hoc-thuat', title='Thương mại hóa tâm linh: 3 góc nhìn học thuật cho người làm truyền thông',
    seo_title='Thương mại hóa tâm linh: 3 góc nhìn học thuật',
    meta_desc='Thương mại hóa tâm linh qua 3 tác phẩm: thị trường tâm linh (Roof), tôn giáo như thương hiệu (Einstein) và Selling Spirituality (Carrette và King).',
    focus_kw='thương mại hóa tâm linh',
    excerpt='Vì sao tâm linh vận hành như một thị trường? Ba góc nhìn học thuật từ Roof, Einstein, Carrette và King, cùng gợi ý cho truyền thông dịch vụ tâm linh.',
    tags=['thương mại hóa tâm linh', 'truyền thông dịch vụ tâm linh', 'marketing tôn giáo', 'chữa lành', 'đạo đức truyền thông'], content=c, categories=[5, 17],
    date='2026-11-12T19:30:00', cover_alt='Minh họa ngọn nến đặt trên kệ hàng có thẻ giá, tượng trưng cho thương mại hóa tâm linh')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

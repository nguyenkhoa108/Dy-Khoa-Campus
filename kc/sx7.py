import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'


WI = 'Wirtz, J. G., Sparks, J. V., &amp; Zimbres, T. M. (2018). The effect of exposure to sexual appeals in advertisements on memory, attitude, and purchase intention: A meta-analytic review. <em>International Journal of Advertising, 37</em>(2), 168-198. https://doi.org/10.1080/02650487.2017.1334996'
UI = 'Chamberlain, C. (2017, ngày 22 tháng 6). <em>Research suggests sexual appeals in ads don\'t sell brands, products</em>. University of Illinois News Bureau. https://news.illinois.edu/research-suggests-sexual-appeals-in-ads-dont-sell-brands-products/'
OSU = 'The Ohio State University. (2015, ngày 21 tháng 7). <em>Sex and violence may not really sell products</em>. https://news.osu.edu/sex-and-violence-may-not-really-sell-products/'
ND87 = 'Chính phủ. (2026). <em>Nghị định số 87/2026/NĐ-CP quy định xử phạt vi phạm hành chính trong lĩnh vực văn hóa và quảng cáo</em>. Công báo điện tử Chính phủ. https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-87-2026-nd-cp-469359.htm'

c = ''
c += P('"Sex sells", hình ảnh gợi cảm giúp bán hàng, là một niềm tin lâu đời trong ngành quảng cáo. Hai phân tích tổng hợp (meta-analysis) lớn cho thấy niềm tin này không đứng vững: quảng cáo dùng sex appeal (yếu tố hấp dẫn giới tính) có thể khiến người xem nhớ quảng cáo hơn, nhưng không giúp họ nhớ thương hiệu, không làm tăng ý định mua và có thể làm thái độ với thương hiệu xấu đi.')
c += P('Đây là bài thứ hai trong chuỗi "Tình dục học và truyền thông". Bài trước bàn về ' + A('quang-cao-bao-cao-su-thuoc-sinh-ly-luat-viet-nam', 'quy định quảng cáo bao cao su và thuốc sinh lý') + '. Bài này đi vào câu hỏi hiệu quả: hình ảnh gợi cảm có thật sự giúp bán hàng?')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Quảng cáo có sex appeal được nhớ tốt hơn, nhưng thương hiệu trong quảng cáo thì không (Wirtz và cộng sự, 2018).',
    'Ảnh hưởng đến ý định mua gần như bằng không; thái độ với thương hiệu giảm nhẹ (Wirtz và cộng sự, 2018).',
    'Nam giới có xu hướng thích các quảng cáo này, nữ giới thì ngược lại (Chamberlain, 2017).',
    'Mức độ gợi dục càng cao, thái độ với thương hiệu càng tiêu cực (The Ohio State University, 2015).',
    'Ở Việt Nam, quảng cáo trái đạo đức xã hội hoặc có định kiến về giới có thể bị xử phạt.',
])

c += H2('Nghiên cứu nói gì về hiệu quả của sex appeal?')
c += H3('Phân tích tổng hợp của Wirtz và cộng sự (2018)')
c += P('Nhóm nghiên cứu do John Wirtz (Đại học Illinois, Mỹ) dẫn đầu tổng hợp 78 nghiên cứu đã qua bình duyệt về tác động của quảng cáo có sex appeal (Chamberlain, 2017). Kết quả chính (Wirtz và cộng sự, 2018):')
c += UL([
    '<strong>Ghi nhớ quảng cáo:</strong> tăng có ý nghĩa thống kê. Người xem nhận ra và nhớ lại quảng cáo tốt hơn.',
    '<strong>Ghi nhớ thương hiệu:</strong> không có tác động đáng kể.',
    '<strong>Thái độ với quảng cáo:</strong> tính chung không có tác động đáng kể, nhưng nam giới đánh giá các quảng cáo này tích cực hơn nữ giới.',
    '<strong>Thái độ với thương hiệu:</strong> giảm nhẹ.',
    '<strong>Ý định mua:</strong> không có tác động.',
])
c += P('Wirtz mô tả tác động lên ý định mua là "literally zero" (hoàn toàn bằng không). Ông cũng cho biết nhóm nghiên cứu bất ngờ trước mức độ tiêu cực của phụ nữ đối với các quảng cáo này: thái độ của nam và nữ "đi theo hai hướng hoàn toàn trái ngược" (Chamberlain, 2017).')
c += H3('Phân tích tổng hợp của Lull và Bushman (2015)')
c += P('Một phân tích tổng hợp khác của Robert Lull và Brad Bushman (Đại học bang Ohio, Mỹ), đăng trên tạp chí <em>Psychological Bulletin</em>, tổng hợp 53 thí nghiệm với gần 8.500 người tham gia trong 44 năm. Theo thông cáo của trường (The Ohio State University, 2015):')
c += UL([
    'Quảng cáo đặt trong chương trình có nội dung tình dục: người xem nhớ thương hiệu kém hơn và ít có ý định mua hơn.',
    'Quảng cáo có nội dung tình dục: không làm giảm ghi nhớ thương hiệu, nhưng thái độ với thương hiệu thấp hơn so với quảng cáo trung tính. Nội dung càng gợi dục, thái độ càng tiêu cực, và người xem càng ít muốn mua.',
    'Khi nội dung quảng cáo phù hợp với nội dung chương trình, ghi nhớ và ý định mua được cải thiện.',
    'Các tác động tiêu cực có vẻ giảm dần qua các thập niên, có thể do người xem đã quen với nội dung này.',
])
c += P('Bushman nhận định người xem tập trung vào yếu tố tình dục đến mức ít chú ý hơn đến thông điệp, và nhà quảng cáo "không nên quá chắc chắn" rằng tình dục giúp bán hàng (The Ohio State University, 2015).')

c += H2('Vì sao người xem nhớ quảng cáo mà quên thương hiệu?')
c += P('Hai nghiên cứu cho thấy cùng một mô thức: yếu tố gợi cảm thu hút sự chú ý, nhưng sự chú ý dồn vào hình ảnh chứ không vào sản phẩm. Với người làm marketing, đây là một cái bẫy của chỉ số. Một quảng cáo có thể đạt lượt xem, lượt nhớ và độ lan truyền cao, nhưng không chuyển thành ghi nhớ thương hiệu hay doanh số.')
c += TABLE(['Chỉ số', 'Wirtz và cộng sự (2018)', 'Lull và Bushman (2015)*'], [
    ['Ghi nhớ quảng cáo', 'Tăng', 'Không được nêu trong thông cáo'],
    ['Ghi nhớ thương hiệu', 'Không tác động', 'Không giảm (khi tình dục nằm trong quảng cáo)'],
    ['Thái độ với thương hiệu', 'Giảm nhẹ', 'Thấp hơn quảng cáo trung tính'],
    ['Ý định mua', 'Không tác động', 'Không khác biệt chung; giảm khi nội dung gợi dục cao'],
])
c += P('Bảng do người viết tổng hợp. *Theo thông cáo của The Ohio State University (2015).')

c += H2('Khác biệt giới: ai thích, ai không?')
c += P('Wirtz và cộng sự (2018) ghi nhận nam giới đánh giá quảng cáo có sex appeal tích cực hơn nữ giới. Theo Wirtz, khi gộp chung hai giới, hai chiều thái độ trái ngược này triệt tiêu nhau, nên tác động tổng thể lên thái độ với quảng cáo không có ý nghĩa thống kê (Chamberlain, 2017). Nói cách khác, một quảng cáo gợi cảm "trung tính" trên số liệu tổng có thể đang làm mất lòng một nửa khán giả.')
c += P('Điều này đặc biệt quan trọng khi nhóm khách hàng chính là nữ giới, hoặc khi quyết định mua trong gia đình do phụ nữ đảm nhận. Chủ đề hình ảnh giới trong quảng cáo được bàn thêm trong các bài ' + A('phu-nu-trung-nien-trong-quang-cao', 'phụ nữ trung niên "vô hình" trong quảng cáo') + ' và ' + A('hinh-anh-dan-ong-trong-quang-cao-thay-doi-the-nao', 'hình ảnh đàn ông trong quảng cáo thay đổi thế nào') + '.')

c += H2('Rủi ro pháp lý ở Việt Nam')
c += P('Pháp luật Việt Nam không cấm dùng yếu tố hấp dẫn giới tính trong quảng cáo, nhưng Nghị định 87/2026/NĐ-CP có các mức phạt cho những nội dung mà quảng cáo gợi cảm dễ vướng phải (Chính phủ, 2026):')
c += UL([
    'Quảng cáo có tính chất định kiến về giới: phạt từ 10 đến 20 triệu đồng (Điều 50 khoản 2).',
    'Quảng cáo trái với truyền thống lịch sử, văn hóa, đạo đức xã hội: phạt từ 40 đến 60 triệu đồng (Điều 50 khoản 4).',
    'Quảng cáo có hình ảnh, lời nói tạo cho trẻ em suy nghĩ, hành động trái với đạo đức, thuần phong mỹ tục: phạt từ 40 đến 60 triệu đồng (Điều 50 khoản 4).',
    'Quảng cáo sản phẩm, hàng hóa có tính chất kích dục: phạt từ 70 đến 100 triệu đồng (Điều 49 khoản 2).',
])
c += P('Các mức trên áp dụng với cá nhân; tổ chức bị phạt gấp đôi (Chính phủ, 2026, Điều 6 khoản 3). Ngoài tiền phạt, quảng cáo vi phạm phải bị gỡ bỏ. Rủi ro lớn hơn thường là khủng hoảng truyền thông khi quảng cáo bị cộng đồng mạng phản ứng.')

c += H2('Khi nào có thể cân nhắc yếu tố gợi cảm?')
c += P('Dựa trên các kết quả trên, người viết gợi ý một số câu hỏi trước khi dùng yếu tố gợi cảm trong quảng cáo:')
c += UL([
    '<strong>Có phù hợp với nơi quảng cáo xuất hiện không?</strong> Lull và Bushman ghi nhận ghi nhớ và ý định mua cải thiện khi nội dung quảng cáo phù hợp với nội dung chương trình xung quanh (The Ohio State University, 2015). Một quảng cáo gợi cảm đặt lệch bối cảnh có thể kém hiệu quả hơn.',
    '<strong>Mục tiêu là gì?</strong> Nếu mục tiêu là doanh số hoặc thái độ với thương hiệu, bằng chứng không ủng hộ cách làm này.',
    '<strong>Khán giả là ai?</strong> Khi khách hàng chính là nữ giới, nguy cơ phản tác dụng cao hơn.',
    '<strong>Có vượt ranh giới pháp lý và văn hóa không?</strong> Định kiến giới, nội dung trái đạo đức xã hội hoặc tiếp cận trẻ em đều có thể bị xử phạt.',
    '<strong>Đo đúng chỉ số chưa?</strong> Đo ghi nhớ thương hiệu và ý định mua, không chỉ lượt xem hay mức độ nhớ quảng cáo.',
])

c += H2('Câu hỏi thường gặp')
c += H3('"Sex sells" có đúng không?')
c += P('Theo hai phân tích tổng hợp được dẫn trong bài, nhìn chung là không. Quảng cáo gợi cảm được nhớ tốt hơn, nhưng không làm tăng ý định mua và có thể làm thái độ với thương hiệu xấu đi (Wirtz và cộng sự, 2018; The Ohio State University, 2015).')
c += H3('Quảng cáo đồ lót, mỹ phẩm có dùng hình ảnh gợi cảm được không?')
c += P('Pháp luật không cấm. Các nghiên cứu được dẫn trong bài không phân tích riêng theo từng loại sản phẩm, nên chưa thể kết luận từ đây rằng hình ảnh gợi cảm hiệu quả hơn với các ngành này. Nội dung vẫn phải tránh định kiến giới và không trái đạo đức xã hội.')
c += H3('Các nghiên cứu này có áp dụng được cho Việt Nam?')
c += P('Các nghiên cứu chủ yếu được thực hiện ở nước ngoài, nên cần thận trọng khi áp dụng. Khác biệt văn hóa có thể làm phản ứng của khán giả Việt Nam khác đi. Đây là khoảng trống nghiên cứu đáng quan tâm cho ngành quảng cáo trong nước.')

c += H2('Điều gì nên nhớ?')
c += P('Yếu tố gợi cảm thu hút sự chú ý, nhưng sự chú ý không đồng nghĩa với doanh số. Bằng chứng từ hai phân tích tổng hợp cho thấy quảng cáo gợi cảm giúp người xem nhớ quảng cáo, không giúp họ nhớ thương hiệu, không làm họ muốn mua hơn, và có thể khiến một bộ phận khách hàng, đặc biệt là nữ giới, có thiện cảm kém hơn với thương hiệu.')
c += GEN_END + REFS([ND87, UI, OSU, WI])

d = dict(slug='sex-appeal-trong-quang-cao-co-giup-ban-hang', title='Sex appeal trong quảng cáo: hình ảnh gợi cảm có giúp bán hàng?',
    seo_title='Sex appeal trong quảng cáo có giúp bán hàng?',
    meta_desc='Sex appeal trong quảng cáo giúp người xem nhớ quảng cáo nhưng không nhớ thương hiệu, không tăng ý định mua. Bằng chứng từ 2 phân tích tổng hợp và luật Việt Nam.',
    focus_kw='sex appeal trong quảng cáo',
    excerpt='"Sex sells" có đúng không? Hai phân tích tổng hợp cho thấy quảng cáo gợi cảm được nhớ hơn nhưng không giúp bán hàng, kèm rủi ro pháp lý tại Việt Nam.',
    tags=['sex appeal', 'quảng cáo gợi cảm', 'hiệu quả quảng cáo', 'định kiến giới', 'tình dục học và truyền thông'], content=c, categories=[5, 14],
    date='2026-11-18T19:30:00', cover_alt='Minh họa biển quảng cáo có trái tim nổi bật bên cạnh giỏ hàng trống, tượng trưng cho quảng cáo gợi cảm không giúp bán hàng')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

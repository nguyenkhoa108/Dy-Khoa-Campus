import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'

WSO = 'Feigin, V. L., Brainin, M., Norrving, B., Martins, S. O., Pandian, J., Lindsay, P., Grupper, M. F., &amp; Rautalin, I. (2025). World Stroke Organization: Global stroke fact sheet 2025. <em>International Journal of Stroke</em>. https://doi.org/10.1177/17474930241308142 (bản mở: https://openrepository.aut.ac.nz/bitstreams/0723d262-c131-4d07-884d-ce9f38bca5ee/download)'
CDC = 'Centers for Disease Control and Prevention. (2026, ngày 19 tháng 5). <em>Signs and symptoms of stroke</em>. https://www.cdc.gov/stroke/signs-symptoms/index.html'

c = ''
c += P('Đột quỵ xảy ra khi dòng máu lên một vùng não bị gián đoạn, do mạch máu bị tắc (nhồi máu não) hoặc bị vỡ (xuất huyết não). Đây là bệnh cấp cứu: thấy một trong các dấu hiệu đột ngột như méo mặt, yếu tay, nói khó, mất thăng bằng hay nhìn mờ, hãy ghi lại giờ và gọi cấp cứu 115 ngay (Centers for Disease Control and Prevention [CDC], 2026). Bài này là bản đồ tổng quan về đột quỵ trên Dy Khoa Blog: mỗi phần tóm ý chính và dẫn đến bài viết chi tiết.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Mỗi năm thế giới có gần 12 triệu ca đột quỵ mới và hơn 7 triệu người tử vong vì đột quỵ (Feigin và cộng sự, 2025).',
    'Khoảng 53% ca đột quỵ xảy ra ở người dưới 70 tuổi, 15% ở người 15 đến 49 tuổi.',
    'Khoảng 84% gánh nặng đột quỵ liên quan đến các yếu tố nguy cơ có thể thay đổi; đứng đầu là huyết áp tâm thu cao.',
    'Nhận biết bằng BE FAST, gọi 115 ngay, ghi lại giờ khởi phát triệu chứng.',
])

c += H2('Đột quỵ phổ biến đến đâu?')
c += P('Theo tờ thông tin năm 2025 của Tổ chức Đột quỵ Thế giới, dựa trên dữ liệu Gánh nặng Bệnh tật Toàn cầu năm 2021 (Feigin và cộng sự, 2025):')
c += TABLE(['Chỉ số', 'Số liệu'], [
    ['Ca đột quỵ mới mỗi năm', 'Gần 12 triệu'],
    ['Tử vong mỗi năm', 'Hơn 7 triệu'],
    ['Người đang sống sau đột quỵ', 'Gần 94 triệu'],
    ['Tỉ lệ ca mới ở người dưới 70 tuổi', 'Khoảng 53%'],
    ['Tỉ lệ ca mới ở người 15 đến 49 tuổi', 'Khoảng 15%'],
    ['Tử vong do đột quỵ ở các nước thu nhập thấp và trung bình thấp', '87,2%'],
])
c += P('Đột quỵ không chỉ là bệnh của người già. Bài ' + A('nguoi-tre-co-bi-dot-quy-khong', 'người trẻ có bị đột quỵ không') + ' phân tích các nguyên nhân thường gặp ở người trẻ.')

c += H2('Có những loại đột quỵ nào?')
c += P('Năm 2021, nhồi máu não chiếm 65,3% ca đột quỵ mới, xuất huyết trong não chiếm 28,8% và xuất huyết dưới nhện chiếm 5,8% (Feigin và cộng sự, 2025). Hai nhóm chính được điều trị khác nhau; các bài dưới đây giải thích chi tiết.')
c += UL([
    A('dot-quy-nhoi-mau-nao-va-xuat-huyet-nao', 'Đột quỵ nhồi máu não và xuất huyết não khác nhau thế nào?'),
    A('thieu-mau-nao-thoang-qua-tia', 'Thiếu máu não thoáng qua (TIA): "đột quỵ nhỏ" có nguy hiểm không?'),
])

c += H2('Nhận biết đột quỵ thế nào?')
c += P('CDC (2026) liệt kê các dấu hiệu xuất hiện <strong>đột ngột</strong>: khó đi lại, chóng mặt, mất thăng bằng; khó nhìn; tê hoặc yếu mặt, tay, chân, nhất là một bên cơ thể; lú lẫn, khó nói hoặc khó hiểu lời nói; đau đầu dữ dội không rõ nguyên nhân. Có thể ghi nhớ bằng BE FAST:')
c += TABLE(['Chữ', 'Dấu hiệu', 'Cách kiểm tra'], [
    ['B (Balance)', 'Mất thăng bằng', 'Hỏi người bệnh có thấy chóng mặt, mất thăng bằng không'],
    ['E (Eyes)', 'Thay đổi thị lực', 'Hỏi người bệnh có nhìn khó không'],
    ['F (Face)', 'Méo mặt', 'Bảo người bệnh cười, xem một bên mặt có xệ xuống không'],
    ['A (Arms)', 'Yếu tay', 'Bảo giơ hai tay, xem một tay có rơi xuống không'],
    ['S (Speech)', 'Khó nói', 'Bảo lặp lại một câu đơn giản, nghe có ngọng, lạ không'],
    ['T (Time)', 'Thời gian', 'Thấy một dấu hiệu là gọi cấp cứu ngay'],
])
c += P('Nguồn: CDC (2026). Ở Việt Nam, số cấp cứu là 115. Đọc chi tiết: ' + A('nhan-biet-dot-quy-be-fast', 'nhận biết đột quỵ bằng quy tắc BE FAST') + '.')

c += H2('Cần làm gì khi có người bị đột quỵ?')
c += P('Việc quan trọng nhất là gọi cấp cứu và ghi lại thời điểm triệu chứng bắt đầu, vì thông tin này giúp nhân viên y tế chọn cách điều trị tốt nhất (CDC, 2026). Thời gian quyết định khả năng được điều trị tái thông mạch máu não.')
c += UL([
    A('gio-vang-dot-quy-la-gi', '"Giờ vàng" đột quỵ là gì và vì sao từng phút đều quan trọng?'),
    A('khi-nguoi-than-co-dau-hieu-dot-quy-nen-lam-gi', 'Khi người thân có dấu hiệu đột quỵ: nên làm gì và cần tránh điều gì?'),
    A('tin-don-chua-dot-quy-tren-mang', 'Tin đồn "chữa đột quỵ" trên mạng: vì sao không nên làm theo?'),
])

c += H2('Phòng đột quỵ bằng cách nào?')
c += P('Khoảng 84% gánh nặng đột quỵ năm 2021 liên quan đến 23 yếu tố nguy cơ có thể thay đổi. Ba yếu tố đóng góp nhiều nhất là huyết áp tâm thu cao (56,8%), ô nhiễm bụi mịn ngoài trời (16,6%) và hút thuốc (13,7%) (Feigin và cộng sự, 2025). Vì vậy, kiểm soát huyết áp là việc phòng đột quỵ quan trọng nhất.')
c += UL([
    A('huyet-ap-bao-nhieu-la-cao', 'Huyết áp bao nhiêu là cao và khi nào cần đi khám?'),
    A('cach-do-huyet-ap-tai-nha', 'Đo huyết áp tại nhà thế nào cho đúng?'),
    A('rung-nhi-va-nguy-co-dot-quy', 'Rung nhĩ làm tăng nguy cơ đột quỵ như thế nào?'),
    A('nguoi-viet-an-man-den-muc-nao', 'Người Việt ăn mặn đến mức nào?'),
])

c += H2('Sau đột quỵ: phục hồi thế nào?')
c += P('Gần 94 triệu người trên thế giới đang sống sau đột quỵ (Feigin và cộng sự, 2025). Bài ' + A('phuc-hoi-sau-dot-quy', 'phục hồi sau đột quỵ: những tháng đầu cần biết gì?') + ' tổng hợp khuyến nghị của các hướng dẫn quốc tế về tập phục hồi chức năng, theo dõi tâm trạng và phòng tái phát.')

c += H2('Câu hỏi thường gặp')
c += H3('Triệu chứng tự hết thì có cần đi viện không?')
c += P('Có. Triệu chứng giống đột quỵ rồi tự hết có thể là cơn thiếu máu não thoáng qua, một dấu hiệu cảnh báo. Xem bài ' + A('thieu-mau-nao-thoang-qua-tia', 'thiếu máu não thoáng qua (TIA)') + '.')
c += H3('Người trẻ có cần lo đột quỵ không?')
c += P('Có. Khoảng 15% ca đột quỵ mới xảy ra ở người 15 đến 49 tuổi (Feigin và cộng sự, 2025).')
c += H3('Có cách nào sơ cứu đột quỵ tại nhà không?')
c += P('Không có cách chữa đột quỵ tại nhà. Việc cần làm là gọi cấp cứu và ghi lại giờ triệu chứng bắt đầu (CDC, 2026). Bài ' + A('tin-don-chua-dot-quy-tren-mang', 'tin đồn chữa đột quỵ trên mạng') + ' giải thích vì sao các mẹo như chích máu đầu ngón tay nguy hiểm.')

c += H2('Điều gì nên nhớ?')
c += P('Đột quỵ phổ biến, có thể xảy ra ở cả người trẻ, và phần lớn gánh nặng liên quan đến các yếu tố có thể thay đổi, nhất là huyết áp cao. Hãy nhớ BE FAST, gọi 115 ngay khi thấy dấu hiệu, và kiểm soát huyết áp từ hôm nay. Bài này sẽ được cập nhật khi có thêm bài viết mới trong chủ đề đột quỵ.')
c += P('<em>Bài viết mang tính thông tin, không thay thế tư vấn y khoa cho từng cá nhân.</em>')
c += GEN_END + REFS([CDC, WSO])

d = dict(slug='dot-quy-la-gi', title='Đột quỵ là gì? Dấu hiệu, cấp cứu và phòng ngừa: hướng dẫn tổng quan',
    seo_title='Đột quỵ là gì? Dấu hiệu, cấp cứu, phòng ngừa',
    meta_desc='Đột quỵ là gì, có mấy loại, nhận biết bằng BE FAST thế nào, cần làm gì khi có người bị đột quỵ và cách phòng ngừa. Tổng quan kèm bài chi tiết từng phần.',
    focus_kw='đột quỵ là gì',
    excerpt='Mỗi năm thế giới có gần 12 triệu ca đột quỵ mới. Tổng quan về các loại đột quỵ, dấu hiệu BE FAST, cấp cứu, phòng ngừa và phục hồi, kèm bài chi tiết từng phần.',
    tags=['đột quỵ', 'BE FAST', 'huyết áp', 'cấp cứu', 'sức khỏe tim mạch'], content=c, categories=[4, 11],
    date='2026-10-29T14:00:00', cover_alt='Minh họa bộ não với một vùng mạch máu bị tắc, bên cạnh đồng hồ và biểu tượng điện thoại gọi cấp cứu 115')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

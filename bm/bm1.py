import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'


DING = 'Ding, D., Nguyen, B., Nau, T., Luo, M., del Pozo Cruz, B., Dempsey, P. C., Munn, Z., Jefferis, B. J., Sherrington, C., Calleja, E. A., Chong, K. H., Davis, R., Francois, M. E., Tiedemann, A., Biddle, S. J. H., Okely, A., Bauman, A., Ekelund, U., Clare, P., &amp; Owen, K. (2025). Daily steps and health outcomes in adults: A systematic review and dose-response meta-analysis. <em>The Lancet Public Health, 10</em>(8), e668-e681. https://doi.org/10.1016/S2468-2667(25)00164-1'
USYD = 'The University of Sydney. (2025, ngày 24 tháng 7). <em>Rethink the 10,000 a day step goal, study suggests</em>. https://www.sydney.edu.au/news-opinion/news/2025/07/24/rethink-the-10000-a-day-step-goal-study-suggests.html'
HH = 'Calechman, S. (2019, ngày 11 tháng 7). <em>10,000 steps a day, or fewer?</em> Harvard Health Publishing. https://www.health.harvard.edu/blog/10000-steps-a-day-or-fewer-2019071117305'
HG = 'St. Peter, E. (2019, ngày 4 tháng 6). For older women, just 7,500 steps a day lowers mortality. <em>The Harvard Gazette</em>. https://news.harvard.edu/gazette/story/2019/06/for-older-women-just-7500-steps-a-day-lowers-mortality'
WHO = 'World Health Organization. (2024, ngày 26 tháng 6). <em>Physical activity</em> [Fact sheet]. https://www.who.int/news-room/fact-sheets/detail/physical-activity'

c = ''
c += P('Đi bộ 10.000 bước mỗi ngày không phải là ngưỡng bắt buộc để có lợi cho sức khỏe. Một phân tích tổng hợp năm 2025 trên tạp chí <em>The Lancet Public Health</em> cho thấy so với 2.000 bước, đi khoảng 7.000 bước mỗi ngày gắn với nguy cơ tử vong do mọi nguyên nhân thấp hơn 47% (Ding và cộng sự, 2025). Con số 10.000 vốn có thể bắt nguồn từ tên một chiếc máy đếm bước được bán ở Nhật Bản năm 1965 (St. Peter, 2019).')
c += P('Đây là bài mở đầu chuyên đề "Bóc mác y khoa trong quảng cáo", nơi mỗi bài đặt một thông điệp quảng cáo "nghe như khoa học" cạnh bằng chứng.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Con số 10.000 bước có thể bắt nguồn từ tên một máy đếm bước ở Nhật Bản năm 1965, chứ không từ một nghiên cứu y khoa.',
    'Lợi ích tăng rõ khi đi từ 2.000 lên khoảng 5.000 đến 7.000 bước mỗi ngày (Ding và cộng sự, 2025).',
    'Với một số kết quả sức khỏe, đi nhiều hơn 7.000 bước vẫn có thêm lợi ích, nên 10.000 bước vẫn là mục tiêu tốt cho người đã năng động.',
    'Khuyến nghị của WHO tính theo phút vận động mỗi tuần, không theo số bước.',
])

c += H2('Con số 10.000 bước đến từ đâu?')
c += P('Theo Harvard Health Publishing, nguồn gốc của con số này có thể truy về năm 1965, khi một công ty Nhật Bản bán một thiết bị tên là <em>manpo-kei</em>, nghĩa là "máy đo 10.000 bước" (Calechman, 2019). Nhà dịch tễ học I-Min Lee (Bệnh viện Brigham and Women\'s, Mỹ) nhận xét: "Cái tên ấy là một công cụ tiếp thị" (Calechman, 2019).')
c += P('Cần lưu ý, chính thông cáo của Harvard Gazette viết rằng nguồn gốc của mục tiêu 10.000 bước "chưa rõ ràng", nhưng "có thể" bắt nguồn từ chiếc máy đếm bước này (St. Peter, 2019).')

c += H2('Bằng chứng mới nhất nói gì?')
c += P('Nhóm nghiên cứu do Melody Ding (Đại học Sydney, Úc) dẫn đầu tổng hợp 57 nghiên cứu từ 35 nhóm thuần tập, trong đó 31 nghiên cứu được đưa vào phân tích tổng hợp. Các nghiên cứu đều đo số bước bằng thiết bị, công bố từ năm 2014 đến năm 2025 (Ding và cộng sự, 2025).')
c += P('So với người đi 2.000 bước mỗi ngày, người đi 7.000 bước có nguy cơ thấp hơn ở nhiều kết quả sức khỏe (Ding và cộng sự, 2025):')
c += TABLE(['Kết quả sức khỏe', 'Nguy cơ thấp hơn ở mức 7.000 bước', 'Mức chắc chắn của bằng chứng'], [
    ['Tử vong do mọi nguyên nhân', '47%', 'Trung bình'],
    ['Mắc bệnh tim mạch', '25%', 'Trung bình'],
    ['Tử vong do bệnh tim mạch', '47%', 'Thấp'],
    ['Tử vong do ung thư', '37%', 'Trung bình'],
    ['Đái tháo đường type 2', '14%', 'Trung bình'],
    ['Sa sút trí tuệ', '38%', 'Trung bình'],
    ['Triệu chứng trầm cảm', '22%', 'Trung bình'],
    ['Té ngã', '28%', 'Rất thấp'],
])
c += P('Bảng do người viết tổng hợp từ Ding và cộng sự (2025). Với mắc mới ung thư, mức giảm 6% không có ý nghĩa thống kê. Mức chắc chắn của bằng chứng được nhóm tác giả đánh giá theo hệ thống GRADE.')
c += P('Với tử vong do mọi nguyên nhân, bệnh tim mạch, sa sút trí tuệ và té ngã, lợi ích tăng nhanh rồi chậm lại quanh mức 5.000 đến 7.000 bước. Với một số kết quả khác như đái tháo đường type 2 hay trầm cảm, lợi ích tiếp tục tăng gần như đều khi đi thêm bước (Ding và cộng sự, 2025). Theo thông cáo của Đại học Sydney, nguy cơ tử vong ở mức 7.000 bước gần tương đương mức 10.000 bước, còn với sa sút trí tuệ, đi tới 10.000 bước chỉ giảm thêm khoảng 7% (The University of Sydney, 2025).')

c += H2('Vậy có nên bỏ mục tiêu 10.000 bước?')
c += P('Không hẳn. Chính nhóm tác giả kết luận 10.000 bước vẫn là mục tiêu phù hợp cho người năng động, còn 7.000 bước có thể là mục tiêu thực tế hơn cho một số người (Ding và cộng sự, 2025). Ding nhận định nghiên cứu giúp chuyển trọng tâm "từ sự hoàn hảo sang sự tiến bộ" (The University of Sydney, 2025).')
c += P('Một nghiên cứu trước đó trên 16.741 phụ nữ lớn tuổi (tuổi trung bình 72) cũng ghi nhận xu hướng tương tự: người đi trung bình 4.400 bước mỗi ngày có nguy cơ tử vong thấp hơn 41% so với nhóm đi ít nhất (khoảng 2.700 bước), và lợi ích chững lại ở khoảng 7.500 bước (St. Peter, 2019).')

c += H2('Hạn chế của bằng chứng')
c += UL([
    'Phần lớn là nghiên cứu quan sát, nên chưa thể khẳng định đi bộ nhiều hơn trực tiếp gây ra lợi ích (St. Peter, 2019).',
    'Một số kết quả chỉ có ít nghiên cứu, chưa có phân tích riêng theo độ tuổi, và có thể còn yếu tố gây nhiễu (Ding và cộng sự, 2025).',
    'Nghiên cứu trên phụ nữ lớn tuổi chủ yếu là người da trắng, nên có thể không đại diện cho các nhóm khác (St. Peter, 2019).',
])

c += H2('Thông điệp quảng cáo đã "mượn" khoa học thế nào?')
c += P('Con số 10.000 bước là ví dụ điển hình cho cách một thông điệp tiếp thị trở thành "chuẩn sức khỏe". Một con số tròn, dễ nhớ, gắn với một sản phẩm, được lặp lại đủ lâu sẽ được người nghe xem như kết luận khoa học. Vấn đề không nằm ở việc khuyến khích đi bộ, mà ở chỗ một mốc tiếp thị có thể được hiểu như ngưỡng tối thiểu, trong khi bằng chứng cho thấy lợi ích đã đến từ những mức thấp hơn.')
c += P('Đoạn trên là nhận định của người viết. Khi gặp một con số sức khỏe trong quảng cáo, có thể tự hỏi: con số này đến từ nghiên cứu nào, hay từ chính nhãn hàng? Đây cũng là câu hỏi đầu tiên trong bộ lọc của chuyên đề. Về cách đánh giá các thiết bị đo sức khỏe, xem thêm bài ' + A('dong-ho-thong-minh-do-suc-khoe-tin-duoc-den-dau', 'đồng hồ thông minh đo sức khỏe: tin được đến đâu') + '.')

c += H2('Nên đặt mục tiêu vận động thế nào?')
c += P('Tổ chức Y tế Thế giới (WHO) khuyến nghị người trưởng thành vận động ở cường độ trung bình ít nhất 150 phút mỗi tuần, và không đưa ra một con số bước cụ thể (World Health Organization [WHO], 2024). WHO ước tính khoảng 31% người trưởng thành trên thế giới chưa đạt mức này (WHO, 2024).')
c += P('Với người ít vận động, bằng chứng cho thấy tăng dần từ mức thấp lên khoảng 5.000 đến 7.000 bước đã gắn với lợi ích rõ rệt (Ding và cộng sự, 2025). Người có bệnh lý nên hỏi ý kiến nhân viên y tế trước khi thay đổi mức vận động.')

c += H2('Câu hỏi thường gặp')
c += H3('Đi bộ 10.000 bước mỗi ngày có tốt không?')
c += P('Có, và nhóm nghiên cứu xem đây vẫn là mục tiêu phù hợp cho người năng động. Tuy nhiên, phần lớn lợi ích về tử vong đã đạt được ở khoảng 7.000 bước (Ding và cộng sự, 2025; The University of Sydney, 2025).')
c += H3('Mỗi ngày đi bao nhiêu bước là đủ?')
c += P('Không có một con số đúng cho mọi người. Bằng chứng hiện có cho thấy khoảng 7.000 bước là mục tiêu thực tế, gắn với lợi ích sức khỏe có ý nghĩa lâm sàng (Ding và cộng sự, 2025).')
c += H3('Ai nghĩ ra con số 10.000 bước?')
c += P('Nguồn gốc chưa được xác định chắc chắn, nhưng thường được cho là từ chiếc máy đếm bước <em>manpo-kei</em> bán ở Nhật Bản năm 1965 (St. Peter, 2019; Calechman, 2019).')

c += H2('Điều gì nên nhớ?')
c += P('10.000 bước là một con số dễ nhớ, có thể bắt nguồn từ tên một sản phẩm, chứ không phải một ngưỡng sức khỏe. Bằng chứng mới cho thấy đi khoảng 7.000 bước đã mang lại phần lớn lợi ích, và mỗi bước tăng thêm từ mức thấp đều đáng giá.')
c += GEN_END + REFS([HH, DING, HG, USYD, WHO])

d = dict(slug='di-bo-10000-buoc-moi-ngay-co-can-thiet', title='Đi bộ 10.000 bước mỗi ngày có cần thiết? Con số đến từ một chiếc máy đếm bước',
    seo_title='Đi bộ 10.000 bước mỗi ngày có cần thiết?',
    meta_desc='Đi bộ 10.000 bước mỗi ngày không bắt buộc. Phân tích tổng hợp 2025 cho thấy khoảng 7.000 bước đã gắn với nguy cơ tử vong thấp hơn 47%. Con số 10.000 từ đâu ra?',
    focus_kw='đi bộ 10.000 bước mỗi ngày',
    excerpt='Con số 10.000 bước có thể bắt nguồn từ tên một máy đếm bước ở Nhật Bản năm 1965. Bằng chứng mới nói gì về số bước cần đi mỗi ngày?',
    tags=['đi bộ 10.000 bước', 'số bước mỗi ngày', 'vận động thể chất', 'quảng cáo sức khỏe', 'bóc mác y khoa'], content=c, categories=[3, 11],
    date='2026-11-12T16:00:00', cover_alt='Minh họa mẩu quảng cáo "Mỗi ngày 10.000 bước" bị bút đỏ gạch và ghi chú "Con số này từ đâu ra?"')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

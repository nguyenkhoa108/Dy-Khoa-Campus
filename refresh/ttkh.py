import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'

BU = 'Burns, T. W., O\'Connor, D. J., &amp; Stocklmayer, S. M. (2003). Science communication: A contemporary definition. <em>Public Understanding of Science, 12</em>(2), 183-202. https://doi.org/10.1177/09636625030122004'
DA = 'Davies, S. R. (2019, ngày 3 tháng 12). <em>What is science communication?</em> Public Communication of Science and Technology Network. https://www.pcst.network/what-is-science-communication/'
NA = 'National Academies of Sciences, Engineering, and Medicine. (2017). <em>Communicating science effectively: A research agenda</em>. The National Academies Press. https://www.ncbi.nlm.nih.gov/books/NBK425715/'
SA = 'Sturgis, P., &amp; Allum, N. (2004). Science in society: Re-evaluating the deficit model of public attitudes. <em>Public Understanding of Science, 13</em>(1), 55-74. https://doi.org/10.1177/0963662504042690'
TR = 'Trench, B. (2008). Towards an analytical framework of science communication models. In D. Cheng, M. Claessens, T. Gascoigne, J. Metcalfe, B. Schiele, &amp; S. Shi (Eds.), <em>Communicating science in social contexts: New models, new practices</em> (pp. 119-138). Springer. https://doi.org/10.1007/978-1-4020-8598-7_7 (bản mở: https://doras.dcu.ie/3629/)'
WE = 'Wellcome Trust. (2026). <em>Wellcome Global Monitor 2026: Trust in science under pressure</em>. https://doi.org/10.21955/wellcomeopenres.1115455.1'

c = ''
c += P('Truyền thông khoa học (science communication, viết tắt SciCom) là lĩnh vực nghiên cứu và thực hành về việc trao đổi tri thức, phương pháp và góc nhìn khoa học giữa giới khoa học với các nhóm công chúng. Không có một định nghĩa duy nhất được cả ngành thống nhất, nhưng các định nghĩa có ảnh hưởng đều xoay quanh một ý chung: hoạt động có chủ đích, hướng tới những người ngoài giới chuyên môn, nhằm tạo ra hiểu biết, quan tâm hoặc đối thoại về khoa học (Burns và cộng sự, 2003; Davies, 2019).')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Định nghĩa "AEIOU": truyền thông khoa học nhằm tạo ra nhận biết, hứng thú, quan tâm, hình thành quan điểm và hiểu biết (Burns và cộng sự, 2003).',
    'Viện Hàn lâm Khoa học Hoa Kỳ nêu năm mục tiêu, từ chia sẻ phát hiện đến lắng nghe các góc nhìn đa dạng (National Academies of Sciences, Engineering, and Medicine [NASEM], 2017).',
    'Ba mô hình chính là thiếu hụt, đối thoại và tham gia; chúng cùng tồn tại chứ không thay thế nhau (Trench, 2008).',
    'Báo chí khoa học là một hình thức của truyền thông khoa học, bên cạnh bảo tàng, lễ hội, blog, tư vấn y tế và nhiều hình thức khác (Davies, 2019).',
])

c += H2('Các định nghĩa học thuật về truyền thông khoa học')
c += H3('Định nghĩa AEIOU của Burns, O\'Connor và Stocklmayer')
c += P('Burns và cộng sự (2003) định nghĩa truyền thông khoa học là việc sử dụng các kỹ năng, phương tiện, hoạt động và đối thoại phù hợp để tạo ra một hoặc nhiều phản ứng cá nhân đối với khoa học, gói gọn trong năm nguyên âm AEIOU:')
c += UL([
    '<strong>A</strong>wareness: nhận biết.',
    '<strong>E</strong>njoyment: hứng thú.',
    '<strong>I</strong>nterest: quan tâm.',
    '<strong>O</strong>pinion-forming: hình thành quan điểm.',
    '<strong>U</strong>nderstanding: hiểu biết.',
])
c += P('Điểm mạnh của định nghĩa này là đặt trọng tâm vào tác động lên người nhận, thay vì chỉ vào hoạt động của người truyền đạt.')
c += H3('Định nghĩa theo tính chủ đích')
c += P('Một định nghĩa được dùng rộng rãi khác, do Maja Horst, Sarah R. Davies và Alan Irwin đề xuất năm 2017, xem truyền thông khoa học là những hành động có tổ chức, rõ ràng và có chủ đích nhằm truyền đạt tri thức, phương pháp, quy trình hoặc thực hành khoa học, trong bối cảnh người không thuộc giới khoa học là một phần được thừa nhận của công chúng tiếp nhận (Davies, 2019). Theo cách hiểu này, phạm vi truyền thông khoa học rất rộng: báo chí khoa học, blog, bảo tàng, lễ hội, quán cà phê khoa học, tham vấn công chúng, buổi khám bệnh, thậm chí khoa học viễn tưởng và quảng cáo (Davies, 2019).')
c += H3('Năm mục tiêu theo Viện Hàn lâm Khoa học Hoa Kỳ')
c += P('Thay vì một định nghĩa ngắn, báo cáo của NASEM (2017) xác định truyền thông khoa học qua mục tiêu. Tùy bối cảnh, truyền thông khoa học có thể nhằm:')
c += UL([
    'Chia sẻ phát hiện và sự hứng khởi của khoa học.',
    'Tăng sự trân trọng khoa học như một cách hữu ích để hiểu và xoay xở trong thế giới hiện đại.',
    'Tăng hiểu biết về khoa học liên quan đến một vấn đề cần ra quyết định.',
    'Tác động đến quan điểm, hành vi và lựa chọn chính sách của người dân, khi bằng chứng cho thấy rõ lựa chọn nào có lợi cho sức khỏe, an toàn.',
    'Gắn kết với các nhóm đa dạng để góc nhìn của họ được tính đến khi tìm giải pháp cho các vấn đề chung.',
])

c += H2('Ba mô hình chính trong truyền thông khoa học')
c += P('Trench (2008) đề xuất một khung phân tích dựa trên ba mô hình:')
c += TABLE(['Mô hình', 'Cách hiểu', 'Chiều truyền thông'], [
    ['Thiếu hụt (deficit), một biến thể của mô hình phổ biến', 'Khoa học được chuyên gia truyền đến công chúng, vốn bị xem là thiếu nhận biết và hiểu biết', 'Một chiều'],
    ['Đối thoại (dialogue)', 'Khoa học được trao đổi giữa nhà khoa học và các nhóm khác', 'Hai chiều'],
    ['Tham gia (participation)', 'Truyền thông về khoa học diễn ra giữa các nhóm đa dạng, trên cơ sở mọi người đều có thể đóng góp', 'Đa chiều'],
])
c += P('Mô hình thiếu hụt bị phê phán vì giả định chỉ cần cung cấp thêm kiến thức là thái độ của công chúng sẽ thay đổi. Sturgis và Allum (2004) cho thấy kiến thức đúng là một yếu tố quan trọng quyết định thái độ đối với khoa học, nhưng mối quan hệ giữa kiến thức và thái độ phức tạp và chịu tác động của nhiều yếu tố khác, chứ không đơn giản như mô hình thiếu hụt giả định.')
c += P('Trench (2008) nhấn mạnh ba mô hình không phải là các nấc tiến hóa. Sự chuyển dịch từ thiếu hụt sang đối thoại chưa trọn vẹn và cũng không phải không thể đảo ngược; các mô hình cũ vẫn tồn tại song song, và mỗi mô hình đều có chỗ dùng trong những hoàn cảnh nhất định. Bài ' + A('mo-hinh-tham-hut-den-tham-gia-cong-chung-truyen-thong-khoa-hoc', 'từ mô hình thiếu hụt đến tham gia công chúng') + ' phân tích sâu hơn.')

c += H2('Vì sao truyền thông khoa học quan trọng?')
c += P('Theo NASEM (2017), truyền thông khoa học giúp người dân và nhà hoạch định chính sách ra quyết định dựa trên bằng chứng, đồng thời giúp giới khoa học hiểu được góc nhìn và mối quan tâm của các nhóm công chúng khác nhau.')
c += P('Vai trò này càng rõ khi niềm tin vào khoa học đang chịu áp lực. Khảo sát ' + A('wellcome-global-monitor-2026-niem-tin-vao-khoa-hoc', 'Wellcome Global Monitor 2026') + ' cho thấy tỉ lệ người tin khoa học ở mức "khá" hoặc "rất nhiều" đã giảm từ 80% năm 2020 xuống 72% năm 2025 (Wellcome Trust, 2026).')

c += H2('Truyền thông khoa học có giống báo chí khoa học không?')
c += P('Không hoàn toàn. Báo chí khoa học là một hình thức cụ thể của truyền thông khoa học, tuân theo chuẩn mực nghề báo. Truyền thông khoa học là khái niệm rộng hơn, bao gồm cả báo chí khoa học lẫn bảo tàng, lễ hội, blog, tham vấn công chúng và tương tác giữa bác sĩ với bệnh nhân (Davies, 2019). Bài ' + A('ttkh-khac-gi-bao-chi-giao-duc-pr-khoa-hoc', 'truyền thông khoa học khác gì báo chí, giáo dục và PR khoa học') + ' so sánh chi tiết hơn.')

c += H2('Câu hỏi thường gặp')
c += H3('Truyền thông khoa học có phải chỉ là "phổ biến khoa học"?')
c += P('Không. Phổ biến khoa học gần với mô hình thiếu hụt, tức truyền tri thức một chiều. Truyền thông khoa học hiện đại còn bao gồm đối thoại và tham gia, nơi công chúng góp tiếng nói vào các vấn đề khoa học (Trench, 2008).')
c += H3('Ai làm truyền thông khoa học?')
c += P('Nhà khoa học, nhà báo, người làm bảo tàng, nhân viên truyền thông của viện nghiên cứu, nhân viên y tế, người sáng tạo nội dung và nhiều người khác. Theo Davies (2019), bất kỳ hoạt động nào có chủ đích truyền đạt điều gì đó về khoa học đến công chúng đều thuộc phạm vi này. Xem thêm bài ' + A('ky-nang-cot-loi-truyen-thong-khoa-hoc', 'kỹ năng cốt lõi của truyền thông khoa học') + '.')
c += H3('Truyền thông khoa học và truyền thông y tế khác nhau thế nào?')
c += P('Hai lĩnh vực giao nhau nhưng có trọng tâm khác nhau. Bài ' + A('truyen-thong-khoa-hoc-va-truyen-thong-y-te-giong-khac-nhau', 'truyền thông khoa học và truyền thông y tế giống, khác nhau thế nào') + ' giải thích chi tiết.')

c += H2('Điều gì nên nhớ?')
c += P('Truyền thông khoa học là lĩnh vực rộng, bao gồm mọi hoạt động có chủ đích đưa khoa học đến với công chúng và mở ra đối thoại giữa hai bên. Mục tiêu không chỉ là truyền kiến thức, mà còn tạo hứng thú, xây dựng niềm tin và giúp người dân ra quyết định dựa trên bằng chứng. Bài này là bài nền của ' + HUB + '.')
c += GEN_END + REFS([BU, DA, NA, SA, TR, WE])

d = dict(id=32, slug='truyen-thong-khoa-hoc-la-gi', title='Truyền thông khoa học là gì?',
    seo_title='Truyền thông khoa học là gì? Định nghĩa, mô hình và vai trò',
    meta_desc='Truyền thông khoa học là gì? Các định nghĩa học thuật (AEIOU, NASEM), ba mô hình thiếu hụt, đối thoại, tham gia và khác biệt với báo chí khoa học.',
    focus_kw='truyền thông khoa học là gì',
    excerpt='Truyền thông khoa học là gì? Định nghĩa AEIOU, năm mục tiêu theo Viện Hàn lâm Khoa học Hoa Kỳ, ba mô hình chính và vì sao lĩnh vực này ngày càng quan trọng.', content=c)
json.dump(d, open(os.path.join(H, 'ttkh.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

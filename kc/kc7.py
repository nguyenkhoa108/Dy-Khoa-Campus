import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'

HT = 'Hoffman, S. J., &amp; Tan, C. (2013). Following celebrities’ medical advice: Meta-narrative analysis. <em>BMJ, 347</em>, f7151. https://doi.org/10.1136/bmj.f7151 (bản mở: https://pmc.ncbi.nlm.nih.gov/articles/PMC3898586/)'
BR = 'Brennen, J. S., Simon, F., Howard, P. N., &amp; Nielsen, R. K. (2020, ngày 7 tháng 4). <em>Types, sources, and claims of COVID-19 misinformation</em> [Factsheet]. Reuters Institute for the Study of Journalism. https://reutersinstitute.politics.ox.ac.uk/types-sources-and-claims-covid-19-misinformation'
EV = 'Evans, D. G. R., Barwell, J., Eccles, D. M., Collins, A., Izatt, L., Jacobs, C., Donaldson, A., Brady, A. F., Cuthbert, A., Harrison, R., Thomas, S., Howell, A., Miedzybrodzka, Z., Murray, A., &amp; The FH02 Study Group. (2014). The Angelina Jolie effect: How high celebrity profile can have a major impact on provision of cancer related services. <em>Breast Cancer Research, 16</em>(5), 442. https://doi.org/10.1186/s13058-014-0442-6'

c = ''
c += P('Hãy tin ở mức bạn tin một người bình thường nói về điều họ không chuyên: lắng nghe được, nhưng cần kiểm tra. Người nổi tiếng có sức lan tỏa rất lớn, và chính vì vậy, một lời khuyên sai từ họ có thể đến với rất nhiều người. Trong một mẫu tin sai về Covid-19, nội dung từ chính trị gia, người nổi tiếng và nhân vật công chúng chỉ chiếm 20% số tin nhưng chiếm 69% tổng lượt tương tác trên mạng xã hội (Brennen và cộng sự, 2020).')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Người nổi tiếng thu hút sự chú ý, không phải lúc nào cũng có chuyên môn.',
    'Ta dễ tin người mình yêu mến cả ở những lĩnh vực ngoài chuyên môn của họ, gọi là hiệu ứng hào quang (Hoffman &amp; Tan, 2013).',
    'Ảnh hưởng của người nổi tiếng có thể tích cực, như khi khuyến khích đi khám sàng lọc đúng đối tượng (Evans và cộng sự, 2014).',
    'Cách an toàn là tách thông điệp khỏi người nói: hỏi họ dựa vào nguồn nào và chuyên gia nói gì.',
])
c += H2('Vì sao lời người nổi tiếng có sức nặng đến vậy?')
c += P('Hoffman và Tan (2013) tổng hợp nghiên cứu từ kinh tế học, marketing, tâm lý học và xã hội học để giải thích vì sao người ta làm theo lời khuyên y khoa của người nổi tiếng. Một vài cơ chế chính:')
c += UL([
    '<strong>Hiệu ứng hào quang:</strong> thiện cảm với một người khiến ta tin họ cả ở những lĩnh vực ngoài chuyên môn, có khi còn hơn tin bác sĩ.',
    '<strong>Tâm lý đám đông:</strong> con người có xu hướng quyết định dựa trên việc người khác đã làm gì, và người nổi tiếng kích hoạt xu hướng đó.',
    '<strong>Gắn cảm xúc:</strong> cảm giác tích cực về một người dễ "chuyển" sang lời khuyên hay sản phẩm họ giới thiệu.',
    '<strong>Hình ảnh bản thân:</strong> lời khuyên thuyết phục hơn khi nó khớp với hình mẫu ta muốn trở thành.',
    '<strong>Tự hợp lý hóa:</strong> khi đã làm theo, ta có xu hướng vô thức biện minh cho lựa chọn của mình.',
])
c += P('Những cơ chế này không có nghĩa người theo dõi thiếu hiểu biết. Chúng là cách não bộ tiết kiệm công sức khi phải xử lý quá nhiều thông tin.')
c += H2('Ảnh hưởng của người nổi tiếng luôn xấu sao?')
c += P('Không. Có những trường hợp người nổi tiếng giúp nhiều người quan tâm hơn đến sức khỏe. Hoffman và Tan (2013) nêu các ví dụ:')
c += UL([
    'Sau khi một người dẫn chương trình truyền hình ở Mỹ nội soi đại tràng và phát hình trên truyền hình, số ca nội soi tầm soát ung thư đại trực tràng của 400 bác sĩ nội soi tăng 21% trong tháng tiếp theo.',
    'Ở Anh, số lượt tầm soát ung thư cổ tử cung tháng 3/2009 cao gấp đôi cùng kỳ năm trước, trùng thời điểm một nhân vật truyền hình qua đời vì căn bệnh này.',
])
c += P('Trường hợp được nghiên cứu kỹ là "hiệu ứng Angelina Jolie". Sau khi nữ diễn viên công bố phẫu thuật cắt bỏ tuyến vú phòng ngừa vì mang đột biến gen BRCA năm 2013, số ca được giới thiệu đến 12 phòng khám tư vấn tiền sử gia đình và 9 dịch vụ di truyền khu vực ở Vương quốc Anh tăng gần 2,5 lần trong tháng 6 và 7/2013, từ 1.981 lên 4.847 ca so với cùng kỳ năm 2012 (Evans và cộng sự, 2014). Nhu cầu xét nghiệm BRCA1/2 gần như tăng gấp đôi, và rà soát nội bộ không thấy số ca giới thiệu không phù hợp tăng lên.')
c += P('Dù vậy, Hoffman và Tan (2013) lưu ý đột biến BRCA hiếm gặp, nên xét nghiệm chỉ được khuyến nghị cho người có nguy cơ cao hoặc tiền sử gia đình. Một lời kể cá nhân dù chân thật vẫn có thể khiến người không thuộc nhóm nguy cơ đi tìm xét nghiệm không cần thiết.')
c += H2('Khi nào lời người nổi tiếng đáng lo?')
c += P('Đáng lo nhất khi họ đưa ra khẳng định khoa học ngoài chuyên môn và lời nói đó lan rất nhanh. Báo cáo của Viện Reuters về tin sai Covid-19 phân tích 225 nội dung bị các tổ chức kiểm chứng đánh giá là sai hoặc gây hiểu lầm, xuất hiện từ tháng 1 đến cuối tháng 3/2020 (Brennen và cộng sự, 2020). Nhóm tác giả thấy:')
c += UL([
    'Tin sai từ chính trị gia, người nổi tiếng và nhân vật công chúng chỉ chiếm khoảng 20% mẫu nhưng tạo ra 69% tổng lượt tương tác trên mạng xã hội.',
    'Phần lớn tin sai (59%) được tạo ra bằng cách biến đổi lại thông tin có sẵn; chỉ 38% là hoàn toàn bịa đặt.',
])
c += P('Điểm thứ hai rất quan trọng. Một người nổi tiếng hiếm khi bịa hoàn toàn; thường họ nhắc lại một nghiên cứu có thật nhưng bỏ mất điều kiện, cỡ mẫu hay bối cảnh. Vì thế lời nói "nghe có cơ sở" nhưng kết luận lại sai. Mẫu nghiên cứu chỉ gồm nội dung tiếng Anh trong ba tháng đầu đại dịch, nên con số không áp dụng nguyên cho mọi bối cảnh.')
c += H2('Nên làm gì khi người nổi tiếng nói về khoa học?')
c += P('Hãy tách thông điệp khỏi người nói, rồi hỏi vài câu:')
c += UL([
    '<strong>Đây có phải chuyên môn của họ không?</strong> Một bác sĩ nói về bệnh khác một ca sĩ nói về bệnh.',
    '<strong>Họ đang kể trải nghiệm hay đưa lời khuyên?</strong> Trải nghiệm cá nhân là thật với họ, nhưng chưa chắc phù hợp với bạn.',
    '<strong>Họ dựa vào nguồn nào?</strong> Có nghiên cứu, cơ quan y tế hay chuyên gia cụ thể nào không, và nguồn đó nói gì?',
    '<strong>Họ có được trả tiền không?</strong> Nội dung quảng cáo cần được nhìn khác với chia sẻ cá nhân. Bài ' + A('kol-trach-nhiem-giai-trinh-quang-cao', 'KOL và trách nhiệm giải trình trong quảng cáo') + ' bàn kỹ hơn về khía cạnh này.',
    '<strong>Chuyên gia và cơ quan y tế nói gì?</strong> Với chuyện sức khỏe, hãy hỏi bác sĩ của bạn trước khi làm theo.',
])
c += P('Hoffman và Tan (2013) gợi ý bác sĩ nên xem việc bệnh nhân nhắc đến lời khuyên của người nổi tiếng là cơ hội để trò chuyện và giải thích, thay vì gạt đi. Người đọc cũng có thể làm tương tự: dùng câu chuyện của người nổi tiếng làm điểm khởi đầu để tìm hiểu, không phải điểm kết thúc.')
c += H2('Câu hỏi thường gặp')
c += H3('Người nổi tiếng có bằng cấp y khoa thì có tin được không?')
c += P('Đáng tin hơn ở đúng chuyên môn của họ, nhưng vẫn cần xem họ dựa vào bằng chứng nào. Một bác sĩ da liễu nói về dinh dưỡng cũng đang nói ngoài chuyên môn. Bài ' + A('thong-tin-khoa-hoc-tren-mang-co-dang-tin', 'Làm sao biết thông tin khoa học trên mạng có đáng tin?') + ' có các bước kiểm tra cụ thể.')
c += H3('Người nổi tiếng chia sẻ bệnh của mình có nên không?')
c += P('Chia sẻ có thể giúp giảm kỳ thị và khuyến khích người khác đi khám, như các ví dụ ở trên. Điều quan trọng là người đọc hiểu đó là trải nghiệm của một người, và quyết định của mình cần dựa trên tư vấn y tế phù hợp.')
c += H3('Nhiều người nổi tiếng cùng nói một điều thì có đúng hơn không?')
c += P('Không nhất thiết. Nhiều tiếng nói giống nhau làm thông điệp quen thuộc hơn, nhưng quen thuộc không phải bằng chứng. Bài ' + A('bai-duoc-chia-se-nhieu-co-dang-tin-hon', 'Bài được chia sẻ nhiều có đáng tin hơn không?') + ' giải thích vì sao.')
c += H2('Điều gì nên nhớ?')
c += P('Người nổi tiếng giỏi thu hút sự chú ý, và sự chú ý đó có thể giúp hoặc hại sức khỏe cộng đồng. Hãy trân trọng câu chuyện của họ, nhưng kiểm tra lời khuyên như với bất kỳ ai: họ có chuyên môn không, dựa vào nguồn nào, và chuyên gia nói gì. Bài này thuộc cụm bài về ' + A('thong-tin-khoa-hoc-tren-mang-co-dang-tin', 'kiểm chứng thông tin khoa học trên mạng') + '.')
c += GEN_END + REFS([BR, EV, HT])

d = dict(slug='nguoi-noi-tieng-noi-ve-khoa-hoc-nen-tin-den-dau', title='Khi người nổi tiếng nói về khoa học, nên tin đến đâu?', seo_title='Người nổi tiếng nói về khoa học: nên tin đến đâu?',
    meta_desc='Vì sao ta dễ tin người nổi tiếng nói về sức khỏe, khoa học? Hiệu ứng hào quang, hiệu ứng Angelina Jolie và 5 câu hỏi để kiểm tra lời khuyên của họ.',
    focus_kw='người nổi tiếng nói về khoa học', excerpt='Người nổi tiếng thu hút sự chú ý, không phải lúc nào cũng có chuyên môn. Vì sao ta dễ tin họ, khi nào ảnh hưởng của họ có lợi, và cách kiểm tra lời khuyên.',
    tags=['kiểm chứng thông tin', 'người nổi tiếng', 'hiệu ứng hào quang', 'thông tin sức khỏe', 'tư duy phản biện'], content=c, categories=[3, 9],
    date='2026-10-24T16:00:00', cover_alt='Minh họa chiếc micro dưới ánh đèn sân khấu và kính lúp có dấu hỏi đặt trên cuốn sách mở')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']))
print(sorted(set(re.findall(r'\(([^()]*?\d{4})\)', body))))

import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'

BYT = 'Bộ Y tế. (2024). <em>Quyết định số 292/QĐ-BYT ngày 06/02/2024 về việc ban hành tài liệu chuyên môn "Hướng dẫn chẩn đoán, điều trị bệnh Tay chân miệng"</em>. https://thuvienphapluat.vn/van-ban/The-thao-Y-te/Quyet-dinh-292-QD-BYT-2024-Huong-dan-chan-doan-dieu-tri-benh-Tay-chan-mieng-598415.aspx'
DB = 'Xuân Quý. (2026, ngày 1 tháng 4). Bệnh lây nhiễm tay chân miệng tăng cao, Bộ Y tế chỉ đạo khẩn. <em>Báo Đại biểu Nhân dân</em>. https://daibieunhandan.vn/benh-lay-nhiem-tay-chan-mieng-tang-cao-bo-y-te-chi-dao-khan-10411884.html'
WHO = 'World Health Organization Regional Office for the Western Pacific. (n.d.). <em>Hand, foot and mouth disease</em>. https://www.who.int/westernpacific/emergencies/surveillance/archives/hand-foot-and-mouth-disease'

c = ''
c += P('Phần lớn trẻ mắc tay chân miệng chỉ bị nhẹ, nhưng một số trẻ có thể chuyển nặng rất nhanh, thường từ ngày 2 đến ngày 5 của bệnh. Theo hướng dẫn của Bộ Y tế, trẻ đang theo dõi tại nhà cần được đưa đi khám lại ngay khi có một trong các dấu hiệu như sốt trên 39°C hoặc sốt kéo dài trên 48 giờ, nôn nhiều, lừ đừ, giật mình, thở nhanh (Bộ Y tế, 2024). Nhận ra sớm các dấu hiệu này là điều quan trọng nhất mà cha mẹ có thể làm.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Tay chân miệng thường gặp ở trẻ dưới 5 tuổi, lây chủ yếu qua đường tiêu hóa (Bộ Y tế, 2024).',
    'Biến chứng nặng thường do virus EV71, xuất hiện sớm từ ngày 2 đến ngày 5, có thể đến ngày 7 (Bộ Y tế, 2024).',
    '"Giật mình" là một trong những dấu hiệu cần đưa trẻ đi khám ngay.',
    'Trẻ bệnh nên nghỉ học 7 đến 10 ngày đầu để tránh lây cho trẻ khác (Bộ Y tế, 2024).',
    'Trong gần 3 tháng đầu năm 2026, cả nước ghi nhận 25.094 ca mắc và 4 ca tử vong (Xuân Quý, 2026).',
])

c += H2('Tay chân miệng là bệnh gì?')
c += P('Tay chân miệng là bệnh truyền nhiễm do virus đường ruột, thường gặp nhất là Coxsackie virus A6, A10, A16 và Enterovirus 71 (EV71). Bệnh thường gặp ở trẻ dưới 5 tuổi và lây từ người sang người chủ yếu qua đường tiêu hóa (Bộ Y tế, 2024).')
c += P('Biểu hiện điển hình gồm sốt, loét miệng gây đau và phát ban dạng phỏng nước ở bàn tay, bàn chân, mông (World Health Organization Regional Office for the Western Pacific [WHO WPRO], n.d.). Bệnh có thể gây các biến chứng như viêm màng não, viêm não và liệt giống bại liệt (WHO WPRO, n.d.). Các trường hợp biến chứng nặng thường do EV71 (Bộ Y tế, 2024).')
c += P('Năm 2026, bệnh tăng cao ngay từ đầu năm. Trong gần 3 tháng đầu năm, cả nước ghi nhận 25.094 ca mắc, 4 ca tử vong, trong đó khu vực phía Nam chiếm 18.031 ca (Xuân Quý, 2026).')

c += H2('Khi nào tay chân miệng chuyển nặng?')
c += P('Theo Bộ Y tế (2024), các biến chứng thần kinh, tim mạch, hô hấp thường xuất hiện sớm, từ ngày 2 đến ngày 5 của bệnh, có thể đến ngày 7. Đây là giai đoạn cha mẹ cần theo dõi trẻ sát nhất, kể cả khi ban đầu trẻ chỉ có vài nốt phỏng và sốt nhẹ.')

c += H2('Dấu hiệu nào cần đưa trẻ đi khám ngay?')
c += P('Với trẻ đang được theo dõi tại nhà, Bộ Y tế (2024) hướng dẫn cần đưa trẻ đi khám lại <strong>ngay</strong> nếu có một trong các dấu hiệu sau:')
c += UL([
    'Sốt trên 39°C hoặc sốt kéo dài trên 48 giờ.',
    'Nôn ói nhiều.',
    'Lừ đừ hoặc quấy, kích thích.',
    'Không bú hoặc bú quá ít.',
    '<strong>Giật mình.</strong>',
    'Thở nhanh hoặc khó thở.',
    'Da nổi vân tím.',
    'Co giật hoặc hôn mê.',
    'Trẻ có biểu hiện bất thường khác, hoặc cha mẹ thấy lo lắng.',
])
c += P('Dấu hiệu cuối cùng rất đáng chú ý: hướng dẫn chính thức coi cảm giác lo lắng của cha mẹ là đủ lý do để đưa trẻ đi khám lại. Cha mẹ không cần chờ đến khi chắc chắn.')

c += H2('Chăm sóc trẻ tại nhà thế nào?')
c += P('Với trẻ bệnh nhẹ được theo dõi tại nhà, Bộ Y tế (2024) hướng dẫn:')
c += UL([
    'Tái khám mỗi 1 đến 2 ngày trong 7 đến 10 ngày đầu của bệnh.',
    'Nếu trẻ còn sốt, tái khám mỗi ngày cho đến khi hết sốt ít nhất 48 giờ.',
])
c += P('Không nên chủ quan khi trẻ có vẻ đỡ trong một hai ngày đầu, vì biến chứng có thể xuất hiện đến ngày 7 của bệnh (Bộ Y tế, 2024).')

c += H2('Phòng tay chân miệng thế nào?')
c += P('Các biện pháp phòng bệnh chính theo Bộ Y tế (2024):')
c += UL([
    '<strong>Rửa tay bằng xà phòng</strong>, đặc biệt sau khi thay quần áo, thay tã, hoặc tiếp xúc với phân, nước bọt của trẻ.',
    '<strong>Rửa sạch</strong> đồ chơi, vật dụng và sàn nhà.',
    '<strong>Cho trẻ bệnh nghỉ học</strong>: không đến nhà trẻ, trường học trong 7 đến 10 ngày đầu của bệnh.',
])
c += P('Vì bệnh lây chủ yếu qua đường tiêu hóa, rửa tay của cả người chăm sóc lẫn trẻ là biện pháp then chốt. Bài ' + A('xu-ly-nuoc-sinh-hoat-sau-lu', 'xử lý nước sinh hoạt sau lũ') + ' có thêm lưu ý về vệ sinh nguồn nước, còn bài ' + A('cach-pha-oresol-bu-nuoc-khi-tieu-chay', 'cách pha oresol bù nước') + ' hữu ích khi trẻ nôn hoặc tiêu chảy.')

c += H2('Câu hỏi thường gặp')
c += H3('"Giật mình" trong tay chân miệng là thế nào?')
c += P('Giật mình là một trong các dấu hiệu Bộ Y tế (2024) yêu cầu đưa trẻ đi khám lại ngay. Nếu thấy trẻ giật mình, dù chỉ vài lần, hãy đưa trẻ đến cơ sở y tế và báo cho bác sĩ biết số lần, thời điểm giật mình.')
c += H3('Trẻ bị tay chân miệng bao lâu thì đi học lại được?')
c += P('Theo Bộ Y tế (2024), trẻ có thể đi học lại sau 7 đến 10 ngày kể từ khi phát bệnh.')
c += H3('Người lớn có bị tay chân miệng không?')
c += P('Có thể. Bệnh thường gặp nhất ở trẻ em, nhưng cũng có thể gặp ở thanh thiếu niên và đôi khi ở người lớn (WHO WPRO, n.d.). Người lớn chăm sóc trẻ bệnh cũng cần rửa tay kỹ để không trở thành nguồn lây.')

c += H2('Điều gì nên nhớ?')
c += P('Tay chân miệng thường nhẹ, nhưng có thể chuyển nặng nhanh trong khoảng ngày 2 đến ngày 5. Hãy theo dõi sát trẻ, tái khám đúng hẹn, và đưa trẻ đi khám ngay khi thấy sốt cao, nôn nhiều, lừ đừ, giật mình, thở nhanh hoặc bất kỳ điều gì khiến bạn lo lắng. Rửa tay bằng xà phòng và cho trẻ bệnh nghỉ học là hai cách phòng lây hiệu quả nhất.')
c += P('<em>Bài viết mang tính thông tin, không thay thế tư vấn y khoa cho từng cá nhân.</em>')
c += GEN_END + REFS([BYT, WHO, DB])

d = dict(slug='tay-chan-mieng-dau-hieu-chuyen-nang', title='Tay chân miệng: dấu hiệu chuyển nặng cha mẹ cần biết',
    seo_title='Tay chân miệng: dấu hiệu chuyển nặng cần đưa trẻ đi khám',
    meta_desc='Tay chân miệng có thể chuyển nặng từ ngày 2 đến ngày 5. Những dấu hiệu cần đưa trẻ đi khám ngay theo Bộ Y tế, cách chăm sóc tại nhà và phòng lây.',
    focus_kw='tay chân miệng',
    excerpt='Sốt trên 39°C, nôn nhiều, lừ đừ, giật mình, thở nhanh là những dấu hiệu cần đưa trẻ mắc tay chân miệng đi khám ngay, theo hướng dẫn của Bộ Y tế.',
    tags=['tay chân miệng', 'sức khỏe trẻ em', 'phòng bệnh', 'dấu hiệu nguy hiểm', 'sức khỏe cộng đồng'], content=c, categories=[4, 11],
    date='2026-11-06T08:00:00', cover_alt='Minh họa bàn tay có nốt phỏng nhỏ, nhiệt kế báo sốt 39°C và bánh xà phòng rửa tay')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

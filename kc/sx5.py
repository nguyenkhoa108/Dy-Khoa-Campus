import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'
GL = lambda t: f'<a href="https://dykhoa.com/blog/thuat-ngu/benh-lay-truyen-qua-duong-tinh-duc-sti/">{t}</a>'

WHO = 'World Health Organization. (2025, ngày 10 tháng 9). <em>Sexually transmitted infections (STIs)</em> [Tờ thông tin]. https://www.who.int/news-room/fact-sheets/detail/sexually-transmitted-infections-(stis)'
WHO24 = 'World Health Organization. (2024, ngày 21 tháng 5). <em>New report flags major increase in sexually transmitted infections, amidst challenges in HIV and hepatitis</em> [Thông cáo báo chí]. https://www.who.int/news/item/21-05-2024-new-report-flags-major-increase-in-sexually-transmitted-infections---amidst-challenges-in-hiv-and-hepatitis'
CDC = 'Centers for Disease Control and Prevention. (2026, ngày 17 tháng 3). <em>Getting tested for STIs</em>. https://www.cdc.gov/sti/testing/index.html'

c = ''
c += P('Các bệnh lây truyền qua đường tình dục thường gặp nhất là chlamydia, lậu, giang mai và trichomonas, cùng bốn bệnh do virus là HPV, herpes sinh dục, viêm gan B và HIV. Theo Tổ chức Y tế Thế giới (WHO), mỗi ngày thế giới có hơn 1 triệu ca mắc mới các STI chữa khỏi được, và phần lớn không có triệu chứng (World Health Organization [WHO], 2025). Điều này có nghĩa là "không thấy gì bất thường" chưa chắc là không mắc bệnh.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Bốn STI chữa khỏi được: giang mai, lậu, chlamydia và trichomonas (WHO, 2025).',
    'Herpes và HIV chưa chữa khỏi, nhưng thuốc kháng virus giúp kiểm soát bệnh (WHO, 2025).',
    'STI thường không có triệu chứng; cách duy nhất để biết chắc là xét nghiệm.',
    'Bao cao su là một trong những cách bảo vệ hiệu quả nhất; HPV và viêm gan B đã có vắc xin an toàn, hiệu quả cao (WHO, 2025).',
    'Ca giang mai mới ở người trưởng thành tăng hơn 1 triệu trong năm 2022, lên 8 triệu ca (WHO, 2024).',
])
c += P('Bài ' + GL('bệnh lây truyền qua đường tình dục (STI)') + ' trong thư viện thuật ngữ giải thích khái niệm ngắn gọn. Bài này đi vào các bệnh cụ thể, khi nào nên xét nghiệm và cách phòng ngừa.')

c += H2('Những bệnh lây truyền qua đường tình dục nào thường gặp?')
c += P('Năm 2020, WHO ước tính có 374 triệu ca mắc mới bốn STI chữa khỏi được ở người 15 đến 49 tuổi (WHO, 2025):')
c += TABLE(['Bệnh', 'Tác nhân', 'Ước tính của WHO', 'Chữa khỏi được?'], [
    ['Trichomonas', 'Ký sinh trùng', '156 triệu ca mới (2020)', 'Có'],
    ['Chlamydia', 'Vi khuẩn', '129 triệu ca mới (2020)', 'Có'],
    ['Lậu', 'Vi khuẩn', '82 triệu ca mới (2020)', 'Có, nhưng vi khuẩn đang kháng thuốc'],
    ['Giang mai', 'Vi khuẩn', '7,1 triệu ca mới (2020); 8 triệu ca (2022)', 'Có'],
    ['Herpes sinh dục (HSV)', 'Virus', 'Hơn 520 triệu người đang mắc (2020)', 'Không, nhưng kiểm soát được'],
    ['HPV', 'Virus', 'Khoảng 300 triệu phụ nữ đang nhiễm', 'Phòng được bằng vắc xin'],
    ['Viêm gan B', 'Virus', '254 triệu người mắc mạn tính (2022)', 'Phòng được bằng vắc xin'],
])
c += P('Số liệu từ WHO (2025), riêng giang mai năm 2022 từ WHO (2024). HIV cũng là một STI quan trọng, nhưng có cách phòng và điều trị riêng nên không đưa vào bảng.')

c += H2('Vì sao nhiều người mắc mà không biết?')
c += P('WHO (2025) cho biết STI thường không có triệu chứng, và khi có thì triệu chứng cũng có thể không đặc hiệu. Một người có thể vẫn khỏe mạnh bình thường nhưng đang mang bệnh và lây cho bạn tình.')
c += P('Khi có biểu hiện, các dấu hiệu thường được dùng để nhận biết gồm tiết dịch bất thường từ âm đạo hoặc niệu đạo và vết loét ở vùng sinh dục, hậu môn (WHO, 2025). Nếu thấy những dấu hiệu này, nên đi khám thay vì tự mua thuốc, vì nhiều bệnh có biểu hiện giống nhau nhưng cách điều trị khác nhau.')

c += H2('Không điều trị thì có nguy hiểm không?')
c += P('Có. Theo WHO (2025), STI không được điều trị có thể gây:')
c += UL([
    '<strong>Vô sinh:</strong> lậu và chlamydia là nguyên nhân chính gây viêm vùng chậu và vô sinh ở phụ nữ.',
    '<strong>Biến chứng thai kỳ:</strong> lây từ mẹ sang con có thể gây thai chết lưu, tử vong sơ sinh, sinh non, nhẹ cân. Năm 2022, 1,1 triệu phụ nữ mang thai mắc giang mai, dẫn đến hơn 390.000 kết cục thai kỳ bất lợi.',
    '<strong>Ung thư:</strong> HPV gây ung thư cổ tử cung và một số loại ung thư khác, liên quan đến hơn 311.000 ca tử vong do ung thư cổ tử cung mỗi năm.',
])
c += P('Một vấn đề đáng lo khác là lậu kháng thuốc. Trong 87 quốc gia có giám sát tăng cường, 9 nước ghi nhận mức kháng ceftriaxone, thuốc điều trị cuối cùng cho bệnh lậu, từ 5% đến 40% (WHO, 2024). Đây là lý do không nên tự dùng kháng sinh khi nghi mắc bệnh.')

c += H2('Khi nào nên xét nghiệm?')
c += P('WHO (2025) khuyến nghị tầm soát STI cho các nhóm và bối cảnh ưu tiên. Hướng dẫn của Trung tâm Kiểm soát và Phòng ngừa Dịch bệnh Hoa Kỳ (CDC) cụ thể hơn (Centers for Disease Control and Prevention [CDC], 2026):')
c += UL([
    'Mọi người từ 13 đến 64 tuổi nên xét nghiệm HIV ít nhất một lần.',
    'Phụ nữ dưới 25 tuổi có quan hệ tình dục nên xét nghiệm lậu và chlamydia mỗi năm.',
    'Phụ nữ mang thai nên xét nghiệm giang mai, HIV, viêm gan B và viêm gan C ngay từ đầu thai kỳ.',
    'Nam quan hệ tình dục đồng giới nên xét nghiệm giang mai, chlamydia, lậu và HIV ít nhất mỗi năm; người có nhiều bạn tình có thể cần xét nghiệm 3 đến 6 tháng một lần.',
])
c += P('Đây là khuyến nghị của Hoa Kỳ, dùng để tham khảo. Ở Việt Nam, bạn có thể hỏi bác sĩ tại bệnh viện, phòng khám da liễu hoặc trung tâm kiểm soát bệnh tật địa phương về lịch xét nghiệm phù hợp. Ngoài ra, nên xét nghiệm khi có bạn tình mới, khi có triệu chứng, hoặc khi bạn tình được chẩn đoán mắc STI.')

c += H2('Làm sao để phòng ngừa?')
c += UL([
    '<strong>Dùng bao cao su đúng cách và đều đặn.</strong> Đây là một trong những cách bảo vệ hiệu quả nhất, kể cả với HIV. Tuy vậy, bao cao su không bảo vệ được với các vết loét nằm ngoài vùng được che phủ, như giang mai hoặc herpes (WHO, 2025).',
    '<strong>Tiêm vắc xin.</strong> HPV và viêm gan B đều đã có vắc xin an toàn, hiệu quả cao (WHO, 2025).',
    '<strong>Xét nghiệm định kỳ</strong> theo khuyến nghị cho nhóm của mình.',
    '<strong>Điều trị cho cả bạn tình.</strong> WHO (2025) xem đây là phần quan trọng của điều trị, giúp cắt đường lây và tránh tái nhiễm.',
])
c += P('Nói chuyện thẳng thắn với bạn tình về xét nghiệm và bảo vệ cũng là một phần của ' + A('su-ung-thuan-consent-trong-tinh-duc-la-gi', 'sự ưng thuận trong tình dục') + '. Bài ' + A('vi-sao-trai-thang-ngai-quan-he-hau-mon-voi-nam-gioi', 'vì sao "trai thẳng" ngại quan hệ qua đường hậu môn với nam giới khác') + ' có thêm số liệu về mức giảm nguy cơ HIV khi dùng bao cao su và thuốc dự phòng trước phơi nhiễm (PrEP).')

c += H2('Câu hỏi thường gặp')
c += H3('Bệnh lây truyền qua đường tình dục có chữa khỏi được không?')
c += P('Tùy bệnh. Giang mai, lậu, chlamydia và trichomonas thường chữa khỏi được bằng kháng sinh hoặc thuốc phù hợp. Herpes và HIV chưa chữa khỏi, nhưng thuốc kháng virus giúp kiểm soát bệnh (WHO, 2025).')
c += H3('Đã chữa khỏi thì có bị lại không?')
c += P('Có thể, nếu tiếp tục quan hệ với người đang mắc bệnh. Vì vậy, WHO (2025) xem việc điều trị cho bạn tình là phần quan trọng để tránh tái nhiễm.')
c += H3('Chỉ quan hệ bằng miệng thì có lây không?')
c += P('Có. STI lây qua quan hệ tình dục đường âm đạo, hậu môn và cả đường miệng (WHO, 2025).')
c += H3('Có nên tự mua kháng sinh uống khi nghi mắc bệnh?')
c += P('Không nên. Nhiều STI có biểu hiện giống nhau nhưng cần thuốc khác nhau, và lậu đã kháng nhiều loại kháng sinh (WHO, 2024). WHO (2025) khuyến nghị điều trị dựa trên kết quả xét nghiệm khi có điều kiện.')

c += H2('Điều gì nên nhớ?')
c += P('Bệnh lây truyền qua đường tình dục rất phổ biến, thường không có triệu chứng và phần lớn chữa khỏi hoặc kiểm soát được nếu phát hiện sớm. Bao cao su, vắc xin, xét nghiệm định kỳ và điều trị cho cả bạn tình là bốn việc quan trọng nhất. Xét nghiệm STI là một việc chăm sóc sức khỏe bình thường, không phải điều đáng xấu hổ.')
c += P('<em>Bài viết mang tính thông tin, không thay thế tư vấn y khoa cho từng cá nhân.</em>')
c += GEN_END + REFS([CDC, WHO24, WHO])

d = dict(slug='cac-benh-lay-truyen-qua-duong-tinh-duc-thuong-gap', title='Các bệnh lây truyền qua đường tình dục thường gặp: dấu hiệu, xét nghiệm, phòng ngừa',
    seo_title='Bệnh lây truyền qua đường tình dục thường gặp và cách phòng',
    meta_desc='Các bệnh lây truyền qua đường tình dục thường gặp: chlamydia, lậu, giang mai, HPV, herpes. Vì sao hay không có triệu chứng, khi nào xét nghiệm, cách phòng.',
    focus_kw='bệnh lây truyền qua đường tình dục',
    excerpt='Mỗi ngày có hơn 1 triệu ca mắc mới STI chữa khỏi được, phần lớn không triệu chứng. Bệnh nào thường gặp, khi nào nên xét nghiệm và cách phòng ngừa theo WHO.',
    tags=['bệnh lây truyền qua đường tình dục', 'sức khỏe tình dục', 'giang mai', 'HPV', 'xét nghiệm'], content=c, categories=[4, 11],
    date='2026-10-29T08:00:00', cover_alt='Minh họa tấm khiên y tế, ống xét nghiệm và bao cao su, tượng trưng cho phòng ngừa và xét nghiệm bệnh lây truyền qua đường tình dục')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

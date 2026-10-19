import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'

LIN = 'Lindau, S. T., Schumm, L. P., Laumann, E. O., Levinson, W., O’Muircheartaigh, C. A., &amp; Waite, L. J. (2007). A study of sexuality and health among older adults in the United States. <em>The New England Journal of Medicine, 357</em>(8), 762-774. https://doi.org/10.1056/NEJMoa067423 (bản mở: https://pmc.ncbi.nlm.nih.gov/articles/PMC2426743/)'
MEN = 'World Health Organization. (2024, ngày 16 tháng 10). <em>Menopause</em>. https://www.who.int/vietnam/news/fact-sheets/detail/menopause'
SH = 'World Health Organization. (n.d.). <em>Sexual health</em>. https://www.who.int/health-topics/sexual-health'

c = ''
c += P('Đời sống tình dục không "tắt" khi con người lớn tuổi, nhưng thường thay đổi. Một khảo sát quốc gia tại Mỹ trên hơn 3.000 người từ 57 đến 85 tuổi cho thấy nhiều người cao tuổi vẫn có hoạt động tình dục; tần suất giảm dần theo tuổi, và các vấn đề tình dục khá phổ biến nhưng ít được trao đổi với bác sĩ (Lindau và cộng sự, 2007).')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Tỉ lệ có hoạt động tình dục giảm dần theo tuổi, nhưng nhiều người vẫn duy trì đời sống tình dục đến tuổi 70, 80.',
    'Sức khỏe chung ảnh hưởng rõ đến đời sống tình dục ở tuổi cao.',
    'Ở phụ nữ, mãn kinh có thể kèm khô âm đạo và đau khi quan hệ (World Health Organization [WHO], 2024).',
    'Vấn đề tình dục ở người lớn tuổi phổ biến nhưng ít khi được nói với bác sĩ.',
])
c += H2('Người cao tuổi có còn đời sống tình dục không?')
c += P('Có. Lindau và cộng sự (2007) khảo sát mẫu đại diện quốc gia gồm 3.005 người Mỹ từ 57 đến 85 tuổi. Hoạt động tình dục được định nghĩa rộng: mọi hoạt động tự nguyện với người khác có tiếp xúc tình dục, dù có giao hợp hay cực khoái hay không. Tỉ lệ có hoạt động tình dục trong 12 tháng qua là:')
c += UL([
    '73% ở nhóm 57 đến 64 tuổi.',
    '53% ở nhóm 65 đến 74 tuổi.',
    '26% ở nhóm 75 đến 85 tuổi.',
])
c += P('Ngay cả ở nhóm lớn tuổi nhất, trong số những người còn hoạt động tình dục, 54% cho biết có quan hệ ít nhất hai đến ba lần mỗi tháng và 23% từ một lần mỗi tuần trở lên. Ở mọi độ tuổi, phụ nữ ít báo cáo có hoạt động tình dục hơn nam giới, và phụ nữ cũng ít có bạn đời hay người thân mật hơn (Lindau và cộng sự, 2007).')
c += H2('Những thay đổi nào thường gặp?')
c += P('Trong số người cao tuổi còn hoạt động tình dục, khoảng một nửa cả nam lẫn nữ cho biết có ít nhất một vấn đề tình dục gây phiền lòng (Lindau và cộng sự, 2007):')
c += UL([
    '<strong>Ở phụ nữ:</strong> giảm ham muốn (43%), khó tiết dịch bôi trơn âm đạo (39%), không đạt cực khoái (34%).',
    '<strong>Ở nam giới:</strong> khó cương (37%) là vấn đề phổ biến nhất. 14% nam giới cho biết có dùng thuốc hoặc thực phẩm bổ sung để cải thiện chức năng tình dục.',
])
c += P('Với phụ nữ, mãn kinh thường xảy ra trong khoảng 45 đến 55 tuổi. WHO liệt kê khô âm đạo và đau khi quan hệ trong số các triệu chứng có thể gặp, bên cạnh bốc hỏa, đổ mồ hôi đêm, khó ngủ và thay đổi tâm trạng (WHO, 2024). WHO cho biết có nhiều biện pháp có và không dùng hormone giúp giảm triệu chứng, và khuyên trao đổi với nhân viên y tế để chọn cách phù hợp.')
c += H2('Sức khỏe ảnh hưởng thế nào?')
c += P('Rất rõ. Người tự đánh giá sức khỏe kém ít có hoạt động tình dục hơn, và nếu còn hoạt động thì gặp nhiều vấn đề hơn (Lindau và cộng sự, 2007). Ở những người có bạn đời nhưng không quan hệ từ ba tháng trở lên, lý do được nêu nhiều nhất là sức khỏe thể chất của người chồng hoặc bạn tình nam.')
c += P('Điều này cho thấy đời sống tình dục ở tuổi cao gắn chặt với sức khỏe chung. Chăm sóc các bệnh mạn tính và trao đổi với bác sĩ về tác dụng phụ của thuốc có thể giúp ích. Các nhóm rối loạn và yếu tố góp phần được giải thích trong bài ' + A('roi-loan-chuc-nang-tinh-duc-thuong-gap', 'rối loạn chức năng tình dục thường gặp') + '.')
c += H2('Vì sao ít người cao tuổi nói chuyện này với bác sĩ?')
c += P('Trong khảo sát của Lindau và cộng sự (2007), chỉ 38% nam và 22% nữ cho biết từng trao đổi về tình dục với bác sĩ kể từ năm 50 tuổi. Nhóm tác giả kết luận các vấn đề tình dục ở người cao tuổi khá phổ biến nhưng hiếm khi được thảo luận với bác sĩ.')
c += P('WHO xem sức khỏe tình dục là trạng thái khỏe mạnh về thể chất, cảm xúc, tinh thần và xã hội liên quan đến tình dục (WHO, n.d.). Với người lớn tuổi, việc nêu vấn đề này với bác sĩ cũng bình thường như hỏi về huyết áp hay giấc ngủ.')
c += H2('Giữ đời sống tình dục lành mạnh khi lớn tuổi')
c += UL([
    '<strong>Chăm sóc sức khỏe chung:</strong> vì sức khỏe kém gắn với nhiều vấn đề tình dục hơn (Lindau và cộng sự, 2007).',
    '<strong>Chủ động hỏi bác sĩ:</strong> về triệu chứng mãn kinh, khó cương hay tác dụng phụ của thuốc, thay vì tự mua thuốc.',
    '<strong>Trò chuyện với bạn đời:</strong> nhu cầu và khả năng thay đổi theo tuổi; bài ' + A('lech-pha-ham-muon-trong-moi-quan-he', 'lệch pha ham muốn trong mối quan hệ') + ' có gợi ý cách nói chuyện.',
    '<strong>Hiểu rộng về gần gũi:</strong> theo định nghĩa trong khảo sát, hoạt động tình dục không nhất thiết phải có giao hợp hay cực khoái.',
])
c += H2('Câu hỏi thường gặp')
c += H3('Lớn tuổi mà vẫn có nhu cầu tình dục có bình thường không?')
c += P('Có. Khảo sát quốc gia tại Mỹ cho thấy hơn một nửa người 65 đến 74 tuổi và khoảng một phần tư người 75 đến 85 tuổi vẫn có hoạt động tình dục trong năm qua (Lindau và cộng sự, 2007).')
c += H3('Khô âm đạo sau mãn kinh có cách nào cải thiện không?')
c += P('WHO cho biết có nhiều biện pháp có và không dùng hormone giúp giảm triệu chứng mãn kinh (WHO, 2024). Hãy trao đổi với bác sĩ để chọn cách phù hợp với tình trạng sức khỏe của bạn.')
c += H3('Số liệu này có áp dụng cho người Việt Nam không?')
c += P('Không hoàn toàn. Đây là khảo sát tại Mỹ, công bố năm 2007, nên tỉ lệ có thể khác ở Việt Nam do khác biệt văn hóa, sức khỏe và hoàn cảnh sống. Xu hướng chung, như sức khỏe ảnh hưởng đến đời sống tình dục, vẫn có giá trị tham khảo.')
c += H2('Điều gì nên nhớ?')
c += P('Đời sống tình dục thay đổi theo tuổi nhưng không biến mất. Sức khỏe chung, mãn kinh và các bệnh mạn tính đều có thể ảnh hưởng, và phần lớn có thể được hỗ trợ nếu được nói ra. Đừng ngại hỏi bác sĩ. Bài này thuộc chuỗi bài về ' + A('tinh-duc-hoc-la-gi', 'tình dục học') + ', cùng với bài ' + A('chu-ky-dap-ung-tinh-duc-o-nguoi', 'chu kỳ đáp ứng tình dục ở người') + '.')
c += P('<em>Bài viết mang tính thông tin, không thay thế tư vấn, chẩn đoán và điều trị y khoa cho từng cá nhân.</em>')
c += GEN_END + REFS([LIN, SH, MEN])

d = dict(slug='tinh-duc-va-tuoi-tac-khi-lon-tuoi', title='Tình dục và tuổi tác: đời sống tình dục thay đổi thế nào khi lớn tuổi?', seo_title='Tình dục khi lớn tuổi: thay đổi gì, khi nào cần đi khám?',
    meta_desc='Người lớn tuổi có còn đời sống tình dục? Số liệu từ khảo sát hơn 3.000 người 57 đến 85 tuổi, ảnh hưởng của mãn kinh, sức khỏe và lời khuyên thực tế.',
    focus_kw='tình dục khi lớn tuổi', excerpt='Đời sống tình dục thay đổi theo tuổi nhưng không biến mất. Số liệu từ khảo sát người 57 đến 85 tuổi, ảnh hưởng của mãn kinh, sức khỏe và vì sao nên hỏi bác sĩ.',
    tags=['sức khỏe tình dục', 'người cao tuổi', 'mãn kinh', 'rối loạn cương', 'tình dục học'], content=c, categories=[4, 11, 13],
    date='2026-10-28T11:30:00', cover_alt='Minh họa hai chiếc ghế bành cạnh nhau với hai tách trà và chậu cây, gợi sự gắn bó của một cặp đôi lớn tuổi')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']))

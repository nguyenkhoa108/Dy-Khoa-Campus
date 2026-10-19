import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'

RD = 'Reed, G. M., Drescher, J., Krueger, R. B., Atalla, E., Cochran, S. D., First, M. B., Cohen-Kettenis, P. T., Arango-de Montis, I., Parish, S. J., Cottler, S., Briken, P., &amp; Saxena, S. (2016). Disorders related to sexuality and gender identity in the ICD-11: Revising the ICD-10 classification based on current scientific evidence, best clinical practices, and human rights considerations. <em>World Psychiatry, 15</em>(3), 205-221. https://doi.org/10.1002/wps.20354 (bản mở: https://pmc.ncbi.nlm.nih.gov/articles/PMC5032510/)'
WHO = 'World Health Organization. (n.d.). <em>Gender incongruence and transgender health in the ICD</em>. https://www.who.int/standards/classifications/frequently-asked-questions/gender-incongruence-and-transgender-health-in-the-icd'

c = ''
c += P('Rối loạn chức năng tình dục là những khó khăn khiến một người không có được hoạt động tình dục thỏa mãn với chính họ, kéo dài nhiều tháng, xảy ra thường xuyên và gây phiền muộn đáng kể. Theo cách phân loại mới của Tổ chức Y tế Thế giới (WHO), các rối loạn này không còn bị chia thành "do tâm lý" hay "do thực thể", vì thường cả hai yếu tố cùng tác động (Reed và cộng sự, 2016).')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Các rối loạn được chia thành nhóm về ham muốn và kích thích, cực khoái, xuất tinh, và nhóm đau khi quan hệ.',
    'Để được xem là rối loạn, khó khăn thường phải kéo dài ít nhất vài tháng, xảy ra thường xuyên và gây phiền muộn.',
    'Nguyên nhân có thể đến từ bệnh lý, thuốc, thiếu hiểu biết, tâm lý, mối quan hệ hay văn hóa, và thường đan xen.',
    'Lệch pha ham muốn giữa hai người hay kỳ vọng không thực tế của bạn tình không phải là căn cứ để chẩn đoán rối loạn.',
])
c += H2('Thế nào thì được xem là rối loạn chức năng tình dục?')
c += P('Hầu như ai cũng có lúc gặp trục trặc trong đời sống tình dục, như mệt mỏi không có hứng hay một lần khó cương. Điều đó chưa phải là rối loạn. Theo hướng dẫn chẩn đoán được đề xuất cho bảng phân loại bệnh ICD-11, một vấn đề thường được xem là rối loạn chức năng tình dục khi (Reed và cộng sự, 2016):')
c += UL([
    'Kéo dài hoặc lặp lại trong ít nhất vài tháng.',
    'Xảy ra thường xuyên, dù mức độ có thể lúc nặng lúc nhẹ.',
    'Gây phiền muộn đáng kể cho người đó.',
])
c += P('Có ngoại lệ khi nguyên nhân rõ và cấp tính, chẳng hạn sau phẫu thuật cắt tuyến tiền liệt hay chấn thương tủy sống; khi đó có thể chẩn đoán sớm hơn để bắt đầu điều trị. Ngược lại, nếu một người hài lòng với đời sống tình dục của mình, dù khác với người khác hay với chuẩn mực văn hóa, thì không nên chẩn đoán rối loạn (Reed và cộng sự, 2016).')
c += H2('Có những nhóm rối loạn chức năng tình dục nào?')
c += P('Trong ICD-11, các rối loạn chức năng tình dục được xếp vào chương mới về các tình trạng liên quan đến sức khỏe tình dục (World Health Organization [WHO], n.d.). Hướng dẫn được đề xuất chia thành các nhóm chính (Reed và cộng sự, 2016):')
c += TABLE(['Nhóm', 'Ví dụ'], [
    ['Rối loạn ham muốn và kích thích', 'Giảm ham muốn tình dục; rối loạn kích thích ở nữ; rối loạn cương ở nam'],
    ['Rối loạn cực khoái', 'Khó đạt hoặc không đạt cực khoái'],
    ['Rối loạn xuất tinh', 'Xuất tinh sớm, xuất tinh muộn'],
    ['Rối loạn đau khi quan hệ (nhóm riêng)', 'Rối loạn đau khi xâm nhập, bao gồm co thắt âm đạo'],
])
c += P('Nhiều mục áp dụng cho cả nam và nữ, như giảm ham muốn hay rối loạn cực khoái, để nhấn mạnh điểm chung trong đáp ứng tình dục. Một số mục được tách riêng khi biểu hiện ở hai giới khác nhau rõ, như rối loạn kích thích ở nữ và rối loạn cương ở nam. Quá trình đáp ứng tình dục được mô tả trong bài ' + A('chu-ky-dap-ung-tinh-duc-o-nguoi', 'chu kỳ đáp ứng tình dục ở người') + '.')
c += H2('Vì sao WHO bỏ cách chia "do tâm lý" và "do thực thể"?')
c += P('Trong bảng phân loại cũ ICD-10, rối loạn "không do thực thể" nằm ở chương rối loạn tâm thần, còn rối loạn "do thực thể" nằm rải rác ở chương bệnh tiết niệu sinh dục. Reed và cộng sự (2016) giải thích nhiều bằng chứng cho thấy việc hình thành và duy trì rối loạn chức năng tình dục thường có sự tương tác giữa yếu tố thể chất và tâm lý, nên cách chia tách này không còn phù hợp với thực hành lâm sàng hiện nay.')
c += P('Vì vậy, ICD-11 gộp chúng vào một nhóm thống nhất và dùng các "nhãn nguyên nhân" có thể gắn cùng lúc, thay vì buộc chọn một trong hai.')
c += H2('Những yếu tố nào có thể góp phần?')
c += P('Hướng dẫn được đề xuất liệt kê các nhóm yếu tố, có thể cùng tồn tại ở một người (Reed và cộng sự, 2016):')
c += UL([
    '<strong>Bệnh lý, chấn thương hay phẫu thuật:</strong> ví dụ đái tháo đường, trầm cảm, suy giáp, đa xơ cứng, phẫu thuật cắt tuyến tiền liệt.',
    '<strong>Thuốc hoặc chất:</strong> ví dụ một số thuốc chống trầm cảm nhóm SSRI, rượu, chất dạng thuốc phiện.',
    '<strong>Thiếu hiểu biết:</strong> về cơ thể, chức năng và đáp ứng tình dục của chính mình.',
    '<strong>Yếu tố tâm lý, hành vi:</strong> thái độ tiêu cực về tình dục, trải nghiệm tình dục không tốt trước đây, ngủ kém, làm việc quá sức.',
    '<strong>Yếu tố mối quan hệ:</strong> xung đột, thiếu gắn bó tình cảm.',
    '<strong>Yếu tố văn hóa:</strong> những cấm kỵ về việc thể hiện khoái cảm, hay niềm tin rằng mất tinh dịch sẽ gây suy yếu, bệnh tật.',
])
c += P('Hướng dẫn cũng phân biệt rối loạn "suốt đời" (có từ khi bắt đầu hoạt động tình dục) với "mắc phải" (xuất hiện sau một thời gian bình thường), và rối loạn "toàn bộ" (mọi hoàn cảnh) với "theo tình huống" (chỉ với một số bạn tình hay hoàn cảnh).')
c += H2('Điều gì không phải là rối loạn?')
c += P('Đây là điểm quan trọng để tránh tự gán nhãn. Theo Reed và cộng sự (2016), kỳ vọng không thực tế của bạn tình, sự chênh lệch ham muốn giữa hai người, hay việc kích thích chưa đủ đều không phải là căn cứ để chẩn đoán rối loạn chức năng tình dục. Khi hai người có nhu cầu khác nhau, điều cần trước hết thường là trò chuyện; bài ' + A('lech-pha-ham-muon-trong-moi-quan-he', 'lệch pha ham muốn trong mối quan hệ') + ' bàn kỹ hơn về chuyện này.')
c += H2('Khi nào nên đi khám?')
c += P('Nên tìm đến bác sĩ khi khó khăn kéo dài, xảy ra thường xuyên và khiến bạn hoặc mối quan hệ bị ảnh hưởng. Vì nguyên nhân có thể liên quan đến bệnh lý như đái tháo đường hay trầm cảm, hoặc tác dụng phụ của thuốc (Reed và cộng sự, 2016), việc thăm khám giúp tìm ra yếu tố có thể điều chỉnh. Không nên tự mua thuốc tăng cường sinh lý khi chưa được tư vấn, và không tự ý ngưng thuốc đang dùng; hãy trao đổi với bác sĩ.')
c += H2('Câu hỏi thường gặp')
c += H3('Thỉnh thoảng không cương được có phải là rối loạn cương không?')
c += P('Chưa chắc. Theo hướng dẫn được đề xuất cho ICD-11, khó khăn thường phải kéo dài ít nhất vài tháng, xảy ra thường xuyên và gây phiền muộn đáng kể mới được xem là rối loạn (Reed và cộng sự, 2016).')
c += H3('Rối loạn chức năng tình dục chỉ gặp ở nam giới?')
c += P('Không. Nhiều rối loạn như giảm ham muốn hay rối loạn cực khoái gặp ở cả nam và nữ, và có những rối loạn riêng ở nữ như rối loạn kích thích hay đau khi xâm nhập (Reed và cộng sự, 2016).')
c += H3('Rối loạn chức năng tình dục có phải là bệnh tâm thần?')
c += P('Trong ICD-11, các rối loạn này được xếp vào chương về sức khỏe tình dục, không còn chia thành nhóm tâm thần và nhóm thực thể như trước (WHO, n.d.; Reed và cộng sự, 2016).')
c += H2('Điều gì nên nhớ?')
c += P('Rối loạn chức năng tình dục là vấn đề sức khỏe có thể thăm khám và hỗ trợ, thường do nhiều yếu tố thể chất, tâm lý và quan hệ đan xen. Một lần trục trặc chưa phải là bệnh, và lệch pha ham muốn cũng không phải là rối loạn. Khi khó khăn kéo dài và gây phiền muộn, hãy tìm đến bác sĩ. Bài này thuộc chuỗi bài về ' + A('tinh-duc-hoc-la-gi', 'tình dục học') + '.')
c += P('<em>Bài viết mang tính thông tin, không thay thế tư vấn, chẩn đoán và điều trị y khoa cho từng cá nhân.</em>')
c += GEN_END + REFS([RD, WHO])

d = dict(slug='roi-loan-chuc-nang-tinh-duc-thuong-gap', title='Rối loạn chức năng tình dục thường gặp: thế nào là rối loạn, khi nào nên đi khám?', seo_title='Rối loạn chức năng tình dục: các nhóm thường gặp',
    meta_desc='Rối loạn chức năng tình dục là gì, gồm những nhóm nào, do đâu và khi nào nên đi khám? Giải thích theo cách phân loại ICD-11 của WHO, dễ hiểu cho người đọc.',
    focus_kw='rối loạn chức năng tình dục', excerpt='Một lần trục trặc chưa phải là bệnh. Thế nào là rối loạn chức năng tình dục, gồm những nhóm nào, do yếu tố gì và khi nào nên đi khám, theo cách phân loại ICD-11.',
    tags=['sức khỏe tình dục', 'rối loạn chức năng tình dục', 'rối loạn cương', 'xuất tinh sớm', 'ICD-11'], content=c, categories=[4, 11, 13],
    date='2026-10-27T11:30:00', cover_alt='Minh họa bảng phân loại với bốn ô màu và ống nghe y tế, gợi các nhóm rối loạn chức năng tình dục')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']))

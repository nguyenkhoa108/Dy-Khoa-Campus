import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'

WMJ = 'Willis, M., Murray, K. N., &amp; Jozkowski, K. N. (2021). Sexual consent in committed relationships: A dyadic study. <em>Journal of Sex &amp; Marital Therapy, 47</em>(7), 669-686. https://doi.org/10.1080/0092623X.2021.1937417 (bản mở: https://pmc.ncbi.nlm.nih.gov/articles/PMC9196330/)'
WHO = 'World Health Organization. (n.d.). <em>Sexual health</em>. https://www.who.int/health-topics/sexual-health'
UN = 'UNESCO. (2018). <em>International technical guidance on sexuality education: An evidence-informed approach</em> (Ấn bản sửa đổi). https://unesdoc.unesco.org/ark:/48223/pf0000260770'

c = ''
c += P('Sự ưng thuận (consent) trong quan hệ tình dục là việc mỗi người tự nguyện muốn tham gia một hoạt động tình dục cụ thể, và để người kia biết điều đó. Nó không chỉ là một câu "đồng ý" lúc đầu, mà là một quá trình diễn ra suốt cuộc gần gũi, kể cả giữa vợ chồng hay người yêu lâu năm (Willis và cộng sự, 2021).')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Sự ưng thuận gồm ba mặt: cảm giác muốn ở bên trong, cách thể hiện ra ngoài, và cách người kia hiểu tín hiệu đó.',
    'Nhiều người thể hiện ưng thuận bằng hành động hơn lời nói, nên dễ hiểu nhầm.',
    'Ở bên nhau lâu không có nghĩa là có thể mặc định người kia luôn muốn.',
    'Tổ chức Y tế Thế giới (WHO) xem trải nghiệm tình dục không bị ép buộc là một phần của sức khỏe tình dục.',
])
c += H2('Sự ưng thuận trong tình dục gồm những gì?')
c += P('Theo tổng quan trong nghiên cứu của Willis và cộng sự (2021), sự ưng thuận có ba mặt:')
c += UL([
    '<strong>Cảm giác bên trong:</strong> mình có thật sự muốn, thấy an toàn, thoải mái và sẵn sàng không. Nhóm tác giả mô tả năm cảm giác: đáp ứng cơ thể, an toàn và thoải mái, hưng phấn, mong muốn và sẵn sàng.',
    '<strong>Cách thể hiện:</strong> nói ra bằng lời hay bày tỏ bằng hành động, rõ ràng hay ngầm ý.',
    '<strong>Cách người kia hiểu:</strong> đối phương đọc các tín hiệu đó như sự đồng ý hay từ chối.',
])
c += P('Vì không ai đọc được suy nghĩ của người khác, các cặp đôi luôn phải tìm cách cho nhau biết mình muốn hay không. Nhóm tác giả cho rằng cách tốt nhất là chủ động thể hiện sự ưng thuận, vì các tín hiệu chủ động thường gắn với cảm giác muốn thật sự ở bên trong (Willis và cộng sự, 2021).')
c += H2('Vì sao tín hiệu không lời dễ gây hiểu nhầm?')
c += P('Vì nó phải được đoán. Tổng quan của Willis và cộng sự (2021) ghi nhận người ta dùng tín hiệu không lời, như cử chỉ hay hành động, thường xuyên hơn lời nói. Nhiều người còn thấy hỏi thẳng là "không tự nhiên". Dù vậy, chính họ cũng thừa nhận nói ra bằng lời giúp giảm nhầm lẫn về việc mình hay người kia có muốn hay không.')
c += P('Cũng theo tổng quan này, có khác biệt giữa nam và nữ trong cách đọc tín hiệu: một số nghiên cứu cho thấy nữ dựa nhiều hơn vào lời nói để nhận biết sự ưng thuận, còn nam có xu hướng tìm tín hiệu không lời. Khi hai người "đọc" theo hai cách khác nhau, nguy cơ hiểu sai càng tăng. Bài ' + A('lech-pha-ham-muon-trong-moi-quan-he', 'lệch pha ham muốn trong mối quan hệ') + ' bàn thêm về cách trò chuyện khi hai người có nhu cầu khác nhau.')
c += H2('Đã là người yêu, vợ chồng thì có cần hỏi không?')
c += P('Có. Nhiều người tin rằng trong mối quan hệ gắn bó, sự ưng thuận có thể mặc định. Willis và cộng sự (2021) mô tả niềm tin này, rồi khảo sát 37 cặp đôi đang trong mối quan hệ gắn bó (74 người, phần lớn là người học đại học ở Mỹ). Kết quả đáng chú ý:')
c += UL([
    'Người tham gia cảm thấy ưng thuận rõ hơn khi họ hiểu đúng cách người kia thể hiện, hoặc khi người kia hiểu đúng tín hiệu của họ.',
    'Ở bên nhau càng lâu thì cảm giác ưng thuận bên trong lại có xu hướng thấp hơn. Nhóm tác giả cho rằng một lý do có thể là theo thời gian, các cặp đôi dựa vào bối cảnh để mặc định thay vì hỏi và thể hiện với nhau.',
])
c += P('Nhóm tác giả kết luận việc thể hiện mong muốn vẫn quan trọng ngay cả trong mối quan hệ gắn bó, và sự ưng thuận nên được hiểu là một quá trình liên tục, có qua có lại. Cần lưu ý đây là mẫu nhỏ, chủ yếu là người trẻ ở một trường đại học Mỹ, nên kết quả mang tính gợi mở hơn là kết luận chắc chắn.')
c += H2('Ưng thuận lành mạnh trông như thế nào?')
c += P('WHO định nghĩa sức khỏe tình dục cần một cách tiếp cận tích cực, tôn trọng, với khả năng có trải nghiệm tình dục an toàn và thỏa mãn, "không bị ép buộc, phân biệt đối xử và bạo lực" (World Health Organization [WHO], n.d.). Từ đó, có thể hiểu một vài nguyên tắc thực tế:')
c += UL([
    '<strong>Tự nguyện:</strong> đồng ý vì muốn, không phải vì bị ép, bị đe dọa hay sợ làm người kia giận.',
    '<strong>Gắn với từng hành vi:</strong> sự ưng thuận là phản hồi của một người trước một hành vi tình dục cụ thể được đề nghị (Willis và cộng sự, 2021), nên đồng ý việc này chưa phải là đồng ý việc khác.',
    '<strong>Có thể thay đổi:</strong> muốn lúc đầu không có nghĩa là phải tiếp tục đến cuối. Vì sự ưng thuận là một quá trình (Willis và cộng sự, 2021), mỗi người đều có thể dừng lại.',
    '<strong>Chủ động:</strong> có người coi việc "không thấy từ chối" là đồng ý, nhưng nhóm tác giả khuyến nghị chủ động thể hiện sự ưng thuận (Willis và cộng sự, 2021). Khi không chắc, hãy hỏi.',
])
c += P('UNESCO (2018) liệt kê sự ưng thuận và quyền toàn vẹn thân thể trong các chủ đề mà giáo dục giới tính toàn diện cần bao gồm. Bài ' + A('giao-duc-tinh-duc-toan-dien-la-gi-khong-chi-dung-lai-o-tranh-thai', 'giáo dục giới tính toàn diện là gì') + ' giải thích vì sao chủ đề này không chỉ dừng lại ở chuyện tránh thai.')
c += H2('Làm sao hỏi mà không "mất hứng"?')
c += P('Hỏi không cần cứng nhắc. Một câu như "Em/anh thấy thế này ổn không?", "Mình tiếp tục nhé?" hay để ý phản ứng của người kia và dừng lại khi thấy họ ngập ngừng đều là cách thể hiện sự tôn trọng. Theo Willis và cộng sự (2021), các cặp đôi hiểu đúng tín hiệu của nhau cũng là những người cảm thấy ưng thuận rõ ràng hơn, nên trò chuyện cởi mở có thể khiến trải nghiệm tốt hơn chứ không làm mất đi sự lãng mạn.')
c += H2('Câu hỏi thường gặp')
c += H3('Không nói "không" thì có phải là đồng ý?')
c += P('Chưa chắc. Willis và cộng sự (2021) nhắc đến hiện tượng chiều theo: một người đồng ý quan hệ dù không thật sự muốn, chẳng hạn để làm người kia vui hoặc để người kia thôi nài nỉ, và điều này có thể xảy ra cả trong mối quan hệ gắn bó. Vì vậy, việc không thấy từ chối chưa nói lên người kia có thật sự muốn hay không. WHO nhấn mạnh trải nghiệm tình dục lành mạnh là trải nghiệm không bị ép buộc (WHO, n.d.).')
c += H3('Đã đồng ý rồi có được đổi ý không?')
c += P('Có. Sự ưng thuận là một quá trình diễn ra suốt cuộc gần gũi (Willis và cộng sự, 2021), nên mỗi người đều có quyền dừng lại bất cứ lúc nào, và người kia cần tôn trọng điều đó.')
c += H3('Nếu từng bị ép buộc thì nên làm gì?')
c += P('Đó không phải lỗi của bạn. Hãy tìm đến người bạn tin tưởng, nhân viên y tế hoặc chuyên gia tâm lý để được hỗ trợ. Nếu đang gặp nguy hiểm, hãy liên hệ cơ quan chức năng.')
c += H2('Điều gì nên nhớ?')
c += P('Sự ưng thuận không phải một thủ tục, mà là cách hai người tôn trọng và lắng nghe nhau. Nó cần tự nguyện, cụ thể và có thể thay đổi, kể cả trong mối quan hệ lâu năm. Khi không chắc, hãy hỏi. Bài này thuộc chuỗi bài về ' + A('tinh-duc-hoc-la-gi', 'tình dục học') + ', cùng với bài ' + A('suc-khoe-tinh-duc-la-gi-who', 'sức khỏe tình dục theo định nghĩa của WHO') + '.')
c += P('<em>Bài viết mang tính thông tin, không thay thế tư vấn y khoa hoặc tâm lý cho từng cá nhân.</em>')
c += GEN_END + REFS([UN, WMJ, WHO])

d = dict(slug='su-ung-thuan-consent-trong-tinh-duc-la-gi', title='Sự ưng thuận (consent) trong quan hệ tình dục là gì?', seo_title='Sự ưng thuận (consent) trong tình dục là gì?',
    meta_desc='Sự ưng thuận (consent) trong tình dục là gì, vì sao không từ chối chưa chắc là muốn, và vì sao người yêu lâu năm vẫn cần hỏi nhau. Giải thích từ nghiên cứu.',
    focus_kw='sự ưng thuận trong tình dục', excerpt='Sự ưng thuận là việc tự nguyện muốn tham gia và để người kia biết điều đó, suốt cả cuộc gần gũi. Vì sao tín hiệu không lời dễ hiểu nhầm và vì sao người yêu lâu năm vẫn cần hỏi nhau.',
    tags=['sức khỏe tình dục', 'sự ưng thuận', 'consent', 'mối quan hệ', 'giáo dục giới tính'], content=c, categories=[4, 11, 13],
    date='2026-10-25T11:30:00', cover_alt='Minh họa hai người đối diện nhau với hai bóng thoại có dấu hỏi và dấu tích, gợi cuộc trò chuyện về sự đồng ý')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']))
print(sorted(set(re.findall(r'\(([^()]*?\d{4}|[^()]*n\.d\.)\)', body))))

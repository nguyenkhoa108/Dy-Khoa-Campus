import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'

VOS = 'Vosoughi, S., Roy, D., &amp; Aral, S. (2018). The spread of true and false news online. <em>Science, 359</em>(6380), 1146-1151. https://doi.org/10.1126/science.aap9559 (bản mở: https://politics.media.mit.edu/papers/Vosoughi_Science.pdf)'
AVR = 'Avram, M., Micallef, N., Patil, S., &amp; Menczer, F. (2020). Exposure to social engagement metrics increases vulnerability to misinformation. <em>Harvard Kennedy School (HKS) Misinformation Review, 1</em>(5). https://doi.org/10.37016/mr-2020-033'
PR21 = 'Pennycook, G., &amp; Rand, D. G. (2021). The psychology of fake news. <em>Trends in Cognitive Sciences, 25</em>(5), 388-402. https://doi.org/10.1016/j.tics.2021.02.007'
PCR = 'Pennycook, G., Cannon, T. D., &amp; Rand, D. G. (2018). Prior exposure increases perceived accuracy of fake news. <em>Journal of Experimental Psychology: General, 147</em>(12), 1865-1880. https://doi.org/10.1037/xge0000465 (bản mở: https://papers.ssrn.com/abstract=2958246)'

c = ''
c += P('Không. Lượt chia sẻ cho biết một nội dung lan rộng đến đâu, không cho biết nội dung đó đúng hay sai. Một nghiên cứu lớn trên Twitter còn cho thấy tin sai thường lan xa và nhanh hơn tin đúng (Vosoughi và cộng sự, 2018). Vì vậy, con số "10 nghìn lượt chia sẻ" nên là lý do để kiểm tra kỹ hơn, không phải lý do để tin ngay.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Lượt chia sẻ đo mức độ lan truyền, không đo độ chính xác.',
    'Trên Twitter, tin sai lan đến 1.500 người nhanh gấp khoảng sáu lần tin đúng (Vosoughi và cộng sự, 2018).',
    'Khi thấy lượt tương tác cao, người dùng ít kiểm chứng hơn và dễ bấm thích, chia sẻ nội dung kém tin cậy hơn (Avram và cộng sự, 2020).',
    'Thấy một thông tin nhiều lần khiến ta dễ tin nó hơn, kể cả khi đó là tin giả (Pennycook và cộng sự, 2018).',
])
c += H2('Vì sao lượt chia sẻ không nói lên độ đúng sai?')
c += P('Vì người ta chia sẻ vì nhiều lý do, và độ chính xác thường không phải lý do được nghĩ đến đầu tiên. Pennycook và Rand (2021) tổng hợp các nghiên cứu cho thấy việc một tiêu đề đúng hay sai ảnh hưởng rất ít đến ý định chia sẻ, dù người tham gia vẫn phân biệt được đúng sai khi được hỏi trực tiếp. Theo hai tác giả, nhiều người sẵn sàng chia sẻ cả những nội dung mà họ có thể nhận ra là không chính xác.')
c += P('Hai tác giả cho rằng khoảng cách giữa "tin" và "chia sẻ" chủ yếu đến từ sự thiếu chú ý, hơn là cố ý lan truyền thông tin sai (Pennycook &amp; Rand, 2021). Nói cách khác, nhiều lượt chia sẻ được tạo ra trong vài giây lướt mạng, khi người chia sẻ chưa dừng lại để tự hỏi thông tin này có đúng không.')
c += H2('Tin sai có thật sự lan nhanh hơn tin đúng?')
c += P('Có, ít nhất trong dữ liệu Twitter mà Vosoughi và cộng sự (2018) phân tích. Nhóm nghiên cứu theo dõi khoảng 126.000 chuỗi tin đồn, được khoảng 3 triệu người chia sẻ hơn 4,5 triệu lần, với độ đúng sai do sáu tổ chức kiểm chứng xác định. Kết quả đáng chú ý:')
c += UL([
    '1% chuỗi tin sai lan rộng nhất thường đến được từ 1.000 đến 100.000 người, trong khi tin đúng hiếm khi vượt quá 1.000 người.',
    'Tin đúng cần thời gian lâu gấp khoảng sáu lần tin sai để đến được 1.500 người.',
    'Tin sai thường "mới lạ" hơn tin đúng, và nhóm tác giả cho rằng người dùng có xu hướng chia sẻ thông tin mới lạ.',
    'Tài khoản tự động (bot) làm tăng tốc độ lan truyền của cả tin đúng lẫn tin sai ở mức gần như nhau. Tin sai lan nhanh hơn chủ yếu vì con người chia sẻ nó nhiều hơn.',
])
c += P('Cần lưu ý đây là dữ liệu từ một nền tảng trong một giai đoạn nhất định, nên không thể áp nguyên cho mọi mạng xã hội hiện nay. Dù vậy, kết quả đủ để nhắc rằng độ lan rộng không phải thước đo sự thật.')
c += H2('Con số tương tác cao ảnh hưởng đến người đọc thế nào?')
c += P('Nó khiến ta bớt cảnh giác. Avram và cộng sự (2020) dùng trò chơi Fakey, mô phỏng một bảng tin mạng xã hội, với hơn 8.500 người chơi. Mỗi bài viết hiện kèm một con số lượt thích và chia sẻ được tạo ngẫu nhiên, và người chơi có thể chia sẻ, thích, kiểm chứng hoặc bỏ qua.')
c += P('Kết quả cho thấy khi con số tương tác càng cao, người chơi càng ít kiểm chứng và càng dễ thích, chia sẻ bài viết, đặc biệt với nội dung từ nguồn kém tin cậy (Avram và cộng sự, 2020). Pennycook và Rand (2021) cũng ghi nhận các tín hiệu phản hồi như lượt "thích" làm tăng mức độ tin vào nội dung tin tức.')
c += P('Nhóm tác giả tự nêu giới hạn: đây là trò chơi mô phỏng, con số tương tác là ngẫu nhiên và tập bài viết không đại diện cho bảng tin thật (Avram và cộng sự, 2020). Vì vậy, nên hiểu kết quả là một tín hiệu cảnh báo, chưa phải bằng chứng cuối cùng về hành vi trên mọi nền tảng.')
c += H2('Vì sao thấy nhiều lần lại dễ tin hơn?')
c += P('Vì cảm giác quen thuộc dễ bị nhầm với cảm giác đúng. Pennycook và cộng sự (2018) cho người tham gia xem các tiêu đề tin giả trình bày như trên Facebook. Chỉ một lần xem trước đó đã làm tăng mức độ người tham gia đánh giá tiêu đề là chính xác, cả trong cùng buổi lẫn sau một tuần. Hiệu ứng này vẫn xuất hiện khi tiêu đề được gắn nhãn là đang bị các bên kiểm chứng đặt nghi vấn.')
c += P('Hiệu ứng có giới hạn: việc xem trước không làm người ta tin những câu hoàn toàn phi lý, như "Trái Đất là một hình vuông hoàn hảo" (Pennycook và cộng sự, 2018). Nhưng với các tin nghe có vẻ hợp lý, mỗi lần một nội dung xuất hiện lại trên bảng tin là một lần nó trở nên quen thuộc hơn. Đây là lý do một tin được chia sẻ khắp nơi có thể "nghe rất thật" dù chưa ai kiểm chứng.')
c += H2('Nên làm gì khi thấy một bài có rất nhiều lượt chia sẻ?')
c += P('Hãy xem lượt chia sẻ là tín hiệu để chậm lại. Một vài câu hỏi đơn giản:')
c += UL([
    '<strong>Nguồn gốc là ai?</strong> Bài viết dẫn từ cơ quan, nghiên cứu hay chuyên gia cụ thể nào, và có mở được nguồn đó không?',
    '<strong>Mình đã đọc hết chưa?</strong> Tiêu đề và ảnh chụp màn hình thường bỏ mất bối cảnh.',
    '<strong>Có nơi đáng tin nào khác đưa tin không?</strong> Nếu chỉ có các trang chia sẻ lại nhau, hãy dè chừng.',
    '<strong>Mình thấy nó quen vì đúng, hay vì đã thấy nhiều lần?</strong> Quen thuộc không phải bằng chứng.',
    '<strong>Nếu sai, việc chia sẻ có gây hại không?</strong> Với thông tin sức khỏe, câu trả lời thường là có.',
])
c += P('Theo Pennycook và Rand (2021), các can thiệp nhắc người dùng chú ý đến độ chính xác có thể giúp họ chia sẻ có chọn lọc hơn. Tự hỏi một câu trước khi bấm chia sẻ là phiên bản đơn giản nhất của lời nhắc đó. Cách kiểm tra chi tiết một nghiên cứu được chia sẻ có trong bài ' + A('kiem-tra-nghien-cuu-chia-se-tren-mang', 'Cách kiểm tra một nghiên cứu được chia sẻ trên mạng') + '.')
c += H2('Câu hỏi thường gặp')
c += H3('Bài được báo lớn chia sẻ lại thì có chắc đúng không?')
c += P('Đáng tin hơn một trang vô danh, nhưng chưa chắc đúng. Hãy tìm xem bài báo dẫn nguồn gốc nào và mở nguồn đó nếu có thể. Bài ' + A('thong-tin-khoa-hoc-tren-mang-co-dang-tin', 'Làm sao biết thông tin khoa học trên mạng có đáng tin?') + ' có các bước cụ thể.')
c += H3('Bài ít lượt chia sẻ thì có kém tin cậy hơn không?')
c += P('Không. Nhiều nghiên cứu và thông báo chính thức có rất ít lượt chia sẻ vì chúng khô khan hoặc ít gây bất ngờ. Độ lan rộng và độ chính xác là hai chuyện khác nhau (Vosoughi và cộng sự, 2018).')
c += H3('Lỡ chia sẻ tin sai rồi thì nên làm gì?')
c += P('Gỡ bài hoặc cập nhật kèm thông tin đính chính, và nói rõ vì sao. Bài ' + A('dinh-chinh-tin-sai-khong-hieu-qua', 'Vì sao đính chính tin sai thường không hiệu quả?') + ' giải thích cách đính chính để người đọc dễ tiếp nhận hơn.')
c += H2('Điều gì nên nhớ?')
c += P('Lượt chia sẻ là thước đo sự chú ý, không phải thước đo sự thật. Tin sai có thể lan nhanh hơn tin đúng, con số tương tác cao làm ta bớt cảnh giác, và sự quen thuộc dễ bị nhầm là đúng. Trước khi bấm chia sẻ, hãy dừng lại vài giây và hỏi: thông tin này từ đâu ra? Bài này thuộc cụm bài về ' + A('thong-tin-khoa-hoc-tren-mang-co-dang-tin', 'kiểm chứng thông tin khoa học trên mạng') + '.')
c += GEN_END + REFS([AVR, PR21, PCR, VOS])

d = dict(slug='bai-duoc-chia-se-nhieu-co-dang-tin-hon', title='Bài được chia sẻ nhiều có đáng tin hơn không?', seo_title='Bài được chia sẻ nhiều có đáng tin hơn không?',
    meta_desc='Lượt chia sẻ có nói lên độ tin cậy? Nghiên cứu cho thấy tin sai lan nhanh hơn tin đúng, lượt tương tác cao làm ta bớt kiểm chứng. Cách đọc tỉnh táo.',
    focus_kw='lượt chia sẻ có đáng tin', excerpt='Lượt chia sẻ đo độ lan truyền, không đo sự thật. Tin sai có thể lan nhanh hơn tin đúng, và con số tương tác cao khiến ta bớt kiểm chứng.',
    tags=['kiểm chứng thông tin', 'tin giả', 'mạng xã hội', 'tư duy phản biện', 'thông tin khoa học'], content=c, categories=[3, 9],
    date='2026-10-23T16:00:00', cover_alt='Minh họa kính lúp soi vào con số 12,4K lượt chia sẻ trên màn hình điện thoại')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']))
print(sorted(set(re.findall(r'\(([^()]*?\d{4})\)', body))))

import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'


LBC = 'Quốc hội. (2025). <em>Luật Báo chí số 126/2025/QH15</em>. https://luatvietnam.vn/chinh-sach/luat-bao-chi-2025-so-126-2025-qh15-422610-d1.html'
LTE = 'Quốc hội. (2016). <em>Luật Trẻ em số 102/2016/QH13</em>. https://luatvietnam.vn/lao-dong/luat-tre-em-2016-104818-d1.html'
DART = 'Dart Center for Journalism and Trauma. (n.d.). <em>Reporting on sexual violence</em>. https://dartcenter.org/content/reporting-on-sexual-violence'
INSPQ = 'Institut national de santé publique du Québec. (2024, ngày 24 tháng 9). <em>Sexual violence and the media</em>. https://www.inspq.qc.ca/en/sexual-assault/media'
UNI = 'UNICEF. (n.d.). <em>Ethical reporting guidelines</em>. https://www.unicef.org/media/reporting-guidelines'
FAH = 'Find A Helpline. (n.d.). <em>Tổng đài điện thoại quốc gia bảo vệ trẻ em (National Child Helpline)</em>. https://findahelpline.com/organizations/t-ng-dai-di-n-tho-i-qu-c-gia-b-o-v-tr-em-national-child-helpline'
PL = 'Phaly. (2020, ngày 21 tháng 2). Ngòi bút phải từ tâm. <em>Báo Pháp luật Việt Nam</em>. https://baophapluat.vn/ngoi-but-phai-tu-tam-post332542.html'

c = ''
c += P('Đưa tin về xâm hại tình dục đòi hỏi báo chí cân bằng giữa quyền được biết của công chúng và sự an toàn, phẩm giá của người bị hại. Các hướng dẫn quốc tế thống nhất ở một số nguyên tắc: không để lộ danh tính người bị hại, không mô tả chi tiết giật gân, dùng ngôn ngữ chính xác, đặt vụ việc trong bối cảnh rộng hơn và luôn kèm thông tin hỗ trợ. Ở Việt Nam, Luật Báo chí 2025 cũng cấm miêu tả tỉ mỉ hành động dâm ô và tiết lộ bí mật cá nhân.')
c += P('Đây là bài thứ ba trong chuỗi "Tình dục học và truyền thông", dành cho nhà báo, biên tập viên, người làm nội dung và quản trị fanpage.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Che giấu danh tính, kể cả những chi tiết có thể ghép lại để nhận ra người bị hại như nghề nghiệp, tuổi, nơi ở.',
    'Không gọi hành vi xâm hại là "quan hệ", "chuyện tình cảm"; không đặt câu hỏi hàm ý đổ lỗi.',
    'Không miêu tả tỉ mỉ hành vi; không quy kết tội danh khi chưa có bản án.',
    'Với trẻ em: luôn đổi tên và che hình ảnh, không đăng thông tin có thể khiến trẻ gặp nguy hiểm.',
    'Đặt vụ việc trong bối cảnh và cung cấp nơi người đọc có thể tìm hỗ trợ.',
])

c += H2('Vì sao cách đưa tin lại quan trọng?')
c += P('Một bài báo có thể giúp xã hội nhận diện vấn đề, nhưng cũng có thể gây tổn thương lần nữa cho người bị hại. Báo Pháp luật Việt Nam dẫn cảnh báo của những người làm công tác bảo vệ trẻ em rằng cách đưa tin thiếu cẩn trọng có thể biến trẻ thành "nạn nhân kép": bị xa lánh, chế giễu và chịu tổn thương tâm lý khó chữa lành (Phaly, 2020). Bài báo cũng chỉ ra rằng việc dùng tên viết tắt hay làm mờ khuôn mặt trở nên vô nghĩa nếu bài viết vẫn đăng địa chỉ, hoàn cảnh gia đình hoặc hình ảnh liên quan.')

c += H2('Luật Việt Nam quy định gì?')
c += P('Luật Báo chí số 126/2025/QH15, có hiệu lực từ ngày 1/7/2026, nghiêm cấm một số hành vi liên quan trực tiếp đến tin về xâm hại tình dục (Quốc hội, 2025, Điều 8):')
c += UL([
    'Tiết lộ thông tin thuộc danh mục bí mật cá nhân, bí mật gia đình (khoản 6).',
    'Miêu tả tỉ mỉ những hành động dâm ô, hành vi tội ác (khoản 8).',
    'Xúc phạm danh dự, nhân phẩm của cá nhân; quy kết tội danh khi chưa có bản án của Tòa án (khoản 9).',
    'Thông tin ảnh hưởng đến sự phát triển bình thường của trẻ em (khoản 10).',
])
c += P('Với trẻ em, Luật Trẻ em 2016 nghiêm cấm việc công bố, tiết lộ thông tin về đời sống riêng tư, bí mật cá nhân của trẻ em khi không được sự đồng ý (Quốc hội, 2016, Điều 6 khoản 11). Trẻ em cũng có quyền bất khả xâm phạm về đời sống riêng tư, bí mật cá nhân và bí mật gia đình (Điều 21).')

c += H2('Năm nguyên tắc khi đưa tin')
c += H3('1. Bảo vệ danh tính và sự an toàn')
c += P('Dart Center for Journalism and Trauma, một trung tâm về báo chí và sang chấn, khuyến nghị nhà báo kiểm tra xem các chi tiết như nghề nghiệp, tuổi hay nơi ở có thể ghép lại để nhận ra người bị hại hay không, đồng thời che khuôn mặt và trang phục dễ nhận diện trong ảnh, video (Dart Center for Journalism and Trauma, n.d.). Trước khi liên hệ, nhà báo nên cân nhắc việc tiếp cận có thể ảnh hưởng đến sự an toàn, quyền riêng tư của họ hay không.')
c += H3('2. Phỏng vấn tôn trọng, không gây tổn thương thêm')
c += P('Theo Dart Center (n.d.), nhà báo nên:')
c += UL([
    'Giới thiệu rõ mình là nhà báo và câu chuyện định viết; tôn trọng quyền từ chối.',
    'Để người được phỏng vấn cùng chọn địa điểm, thời gian an toàn; báo trước thời lượng phỏng vấn.',
    'Không ép buộc, lừa dối hay trả tiền để có phỏng vấn.',
    'Lắng nghe, không phán xét; tránh câu hỏi "tại sao" và cách hỏi hàm ý họ có lỗi.',
    'Hiểu rằng lời kể có thể rời rạc, thiếu mạch lạc vì sang chấn có thể ảnh hưởng đến trí nhớ.',
])
c += H3('3. Dùng ngôn ngữ chính xác, trung tính')
c += P('Dart Center (n.d.) khuyến nghị không mô tả hành vi hiếp dâm là "quan hệ tình dục" và không gọi một chuỗi hành vi xâm hại là "chuyện tình cảm". Viện Y tế công cộng quốc gia Quebec (INSPQ, Canada) khuyến nghị dùng từ ngữ "phù hợp, trung tính và chính xác" (Institut national de santé publique du Québec, 2024). Một số ví dụ người viết gợi ý cho tiếng Việt:')
c += TABLE(['Nên tránh', 'Có thể dùng'], [
    ['"Quan hệ", "vụ ân ái", "chuyện tình cảm"', 'Hiếp dâm, xâm hại tình dục, dâm ô (theo đúng hành vi được cơ quan chức năng xác định)'],
    ['"Yêu râu xanh", "con thú"', 'Người bị tố cáo, nghi phạm, bị cáo (theo đúng giai đoạn tố tụng)'],
    ['"Kẻ hiếp dâm" khi chưa có bản án', 'Người bị cáo buộc, nghi phạm'],
    ['"Nữ sinh xinh đẹp", "mặc gợi cảm"', 'Không nêu chi tiết ngoại hình, trang phục không liên quan'],
])
c += P('Bảng do người viết gợi ý dựa trên các nguyên tắc nêu trên và Điều 8 khoản 9 Luật Báo chí 2025. INSPQ (2024) cũng lưu ý mỗi người có thể tự nhận mình là "nạn nhân", "người sống sót", cả hai hoặc không, và có thể dùng từ trung tính "người" để không định danh họ chỉ qua trải nghiệm bị xâm hại.')
c += H3('4. Đặt vụ việc trong bối cảnh')
c += P('INSPQ (2024) khuyến nghị thể hiện được tính phức tạp và quy mô của bạo lực tình dục, cung cấp bối cảnh cho sự việc, và đa dạng góc nhìn bằng cách phỏng vấn chuyên gia. Dart Center (n.d.) cũng khuyên đặt các vụ việc trong bối cảnh rộng hơn, như những vấn đề xã hội kéo dài. Một bài báo chỉ kể diễn biến một vụ án, không nói gì về phòng ngừa hay hỗ trợ, sẽ khó giúp người đọc hiểu vấn đề. Về khái niệm ' + A('su-ung-thuan-consent-trong-tinh-duc-la-gi', 'sự ưng thuận (consent) trong tình dục') + ', có thể tham khảo bài riêng trong blog.')
c += H3('5. Luôn kèm thông tin hỗ trợ')
c += P('INSPQ (2024) khuyến nghị nâng cao nhận thức về các nguồn hỗ trợ và khuyến khích người bị ảnh hưởng tìm sự giúp đỡ. Ở Việt Nam, khi vụ việc liên quan đến trẻ em, bài viết có thể kèm Tổng đài điện thoại quốc gia bảo vệ trẻ em 111, hoạt động 24/7 và miễn phí (Find A Helpline, n.d.).')

c += H2('Khi người bị hại là trẻ em')
c += P('Hướng dẫn đạo đức đưa tin của UNICEF yêu cầu đổi tên và che nhận diện hình ảnh của trẻ là nạn nhân của xâm hại hoặc bóc lột tình dục (UNICEF, n.d.). Các nguyên tắc khác gồm:')
c += UL([
    'Không đăng câu chuyện hay hình ảnh có thể khiến trẻ, anh chị em hoặc bạn bè của trẻ gặp nguy hiểm, kể cả khi đã che danh tính. Nếu không chắc, hãy viết về tình hình chung thay vì về một trẻ cụ thể.',
    'Không đặt câu hỏi làm trẻ sống lại nỗi đau từ sự kiện sang chấn; hạn chế số người phỏng vấn, chụp ảnh.',
    'Xin phép cả trẻ và người giám hộ cho mọi cuộc phỏng vấn, tốt nhất bằng văn bản, và bảo đảm không ai bị ép buộc.',
    'Kiểm chứng lời kể của trẻ với trẻ khác hoặc người lớn, tốt nhất là cả hai.',
])

c += H2('Danh sách kiểm tra trước khi đăng')
c += UL([
    'Bài có chi tiết nào, đơn lẻ hoặc ghép lại, giúp nhận ra người bị hại không?',
    'Ảnh, video đã che mặt, trang phục, nhà cửa, biển số xe chưa?',
    'Có từ ngữ nào giảm nhẹ, lãng mạn hóa hoặc gợi dục hóa hành vi xâm hại không?',
    'Có mô tả chi tiết hành vi vượt quá mức cần thiết để người đọc hiểu sự việc không?',
    'Người bị tố cáo được gọi đúng theo giai đoạn tố tụng chưa?',
    'Tiêu đề và ảnh đại diện có câu view bằng chi tiết gây sốc không?',
    'Đã kèm thông tin về nơi tìm hỗ trợ chưa?',
])
c += P('Danh sách do người viết tổng hợp từ các nguồn trong bài.')

c += H2('Câu hỏi thường gặp')
c += H3('Có nên gọi là "nạn nhân" hay "người sống sót"?')
c += P('Không có một từ đúng cho mọi người. Dart Center (n.d.) khuyên dùng "người sống sót" nếu người đó muốn vậy, còn INSPQ (2024) lưu ý mỗi người có thể chọn cách gọi khác nhau. Khi có thể, hãy hỏi chính người được phỏng vấn.')
c += H3('Viết tên tắt người bị hại đã đủ chưa?')
c += P('Chưa chắc. Nếu bài vẫn nêu địa chỉ, trường học, hoàn cảnh gia đình hoặc hình ảnh liên quan, người quen vẫn có thể nhận ra (Phaly, 2020; Dart Center for Journalism and Trauma, n.d.).')
c += H3('Fanpage, tài khoản cá nhân chia sẻ vụ việc có cần tuân thủ các nguyên tắc này?')
c += P('Có, về mặt đạo đức. Luật Trẻ em 2016 cấm mọi cá nhân tiết lộ bí mật cá nhân của trẻ em khi không được đồng ý, không chỉ riêng báo chí (Quốc hội, 2016, Điều 6 khoản 11).')

c += H2('Điều gì nên nhớ?')
c += P('Đưa tin về xâm hại tình dục không chỉ là kể lại một vụ việc. Mỗi chi tiết, mỗi từ ngữ và mỗi tấm ảnh đều có thể bảo vệ hoặc làm tổn thương người bị hại thêm một lần nữa. Bảo vệ danh tính, dùng ngôn ngữ chính xác, tránh chi tiết giật gân, đặt vụ việc trong bối cảnh và chỉ ra nơi tìm hỗ trợ là năm điều tối thiểu mà người làm báo và người làm nội dung cần nhớ.')
c += GEN_END + REFS([DART, FAH, INSPQ, PL, LBC, LTE, UNI])

d = dict(slug='dua-tin-ve-xam-hai-tinh-duc-bao-chi-nen-viet-the-nao', title='Đưa tin về xâm hại tình dục: báo chí nên viết thế nào?',
    seo_title='Đưa tin về xâm hại tình dục: báo chí nên viết thế nào?',
    meta_desc='Đưa tin về xâm hại tình dục cần bảo vệ danh tính, dùng ngôn ngữ chính xác, tránh chi tiết giật gân. Nguyên tắc từ Dart Center, UNICEF và Luật Báo chí 2025.',
    focus_kw='đưa tin về xâm hại tình dục',
    excerpt='Năm nguyên tắc khi đưa tin về xâm hại tình dục, quy định của Luật Báo chí 2025, Luật Trẻ em và danh sách kiểm tra cho nhà báo, người làm nội dung.',
    tags=['đưa tin xâm hại tình dục', 'đạo đức báo chí', 'Luật Báo chí 2025', 'bảo vệ trẻ em', 'tình dục học và truyền thông'], content=c, categories=[5, 15],
    date='2026-11-20T19:30:00', cover_alt='Minh họa tờ báo có ảnh được làm mờ và cây bút, tượng trưng cho đưa tin có trách nhiệm về xâm hại tình dục')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

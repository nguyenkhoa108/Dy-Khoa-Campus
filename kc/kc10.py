import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'

GR = 'Grudniewicz, A., Moher, D., Cobey, K. D., Bryson, G. L., Cukier, S., Allen, K., Ardern, C., Balcom, L., Barros, T., Berger, M., Buitrago Ciro, J., Cugusi, L., Donaldson, M. R., Egger, M., Graham, I. D., Hodgkinson, M., Khan, K. M., Mabizela, M., Manca, A., . . . Lalu, M. M. (2019). Predatory journals: No definition, no defence. <em>Nature, 576</em>, 210-212. https://doi.org/10.1038/d41586-019-03759-y'
SB = 'Shen, C., &amp; Björk, B. C. (2015). "Predatory" open access: A longitudinal study of article volumes and market characteristics. <em>BMC Medicine, 13</em>, 230. https://doi.org/10.1186/s12916-015-0469-2'
TCS = 'Think. Check. Submit. (n.d.). <em>Journals</em>. https://thinkchecksubmit.org/journals/'

c = ''
c += P('Tạp chí săn mồi (predatory journal) là tạp chí đặt lợi ích riêng, thường là thu phí đăng bài, lên trên chất lượng học thuật. Theo định nghĩa đồng thuận do 43 chuyên gia từ 10 quốc gia xây dựng năm 2019, các tạp chí và nhà xuất bản săn mồi có bốn đặc điểm: thông tin sai hoặc gây hiểu lầm, làm trái các chuẩn mực biên tập và xuất bản, thiếu minh bạch, và/hoặc mời gửi bài ồ ạt, thiếu chọn lọc (Grudniewicz và cộng sự, 2019).')
c += P('Với người đọc phổ thông, điều này có nghĩa là "được đăng trên tạp chí khoa học" chưa chắc đã là bằng chứng đáng tin.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Tạp chí săn mồi thu phí nhưng không bình duyệt nghiêm túc, nên bài kém chất lượng vẫn được đăng.',
    'Năm 2014, khoảng 8.000 tạp chí săn mồi đăng ước tính 420.000 bài, tăng từ 53.000 bài năm 2010 (Shen &amp; Björk, 2015).',
    'Dấu hiệu thường gặp: chỉ số tác động giả, ban biên tập không kiểm chứng được, phí không rõ ràng, email mời gửi bài dồn dập (Grudniewicz và cộng sự, 2019).',
    'Bộ câu hỏi Think. Check. Submit. giúp kiểm tra một tạp chí trước khi gửi bài hoặc tin vào bài đăng.',
])

c += H2('Tạp chí săn mồi hoạt động thế nào?')
c += P('Mô hình xuất bản mở (open access) hợp pháp thường thu phí xử lý bài (article processing charge) từ tác giả để người đọc được đọc miễn phí. Tạp chí săn mồi lợi dụng mô hình này: thu phí nhưng bỏ qua hoặc làm qua loa khâu bình duyệt, nên gần như bài nào trả tiền cũng được đăng.')
c += P('Một nghiên cứu theo dõi thị trường này cho thấy số bài trên tạp chí săn mồi tăng từ 53.000 năm 2010 lên khoảng 420.000 năm 2014, do khoảng 8.000 tạp chí đang hoạt động đăng tải. Tác giả trả trung bình 178 USD mỗi bài, và bài thường được đăng trong vòng 2 đến 3 tháng sau khi gửi (Shen &amp; Björk, 2015). Châu Á và châu Phi chiếm ba phần tư số tác giả trong mẫu nghiên cứu.')

c += H2('Những dấu hiệu nào giúp nhận biết?')
c += P('Grudniewicz và cộng sự (2019) mô tả bốn nhóm dấu hiệu:')
c += UL([
    '<strong>Thông tin sai hoặc gây hiểu lầm:</strong> chỉ số tác động (impact factor) giả, địa chỉ sai, ban biên tập không có thật hoặc không biết mình có tên, tuyên bố sai về việc được lập chỉ mục hay là thành viên các hiệp hội.',
    '<strong>Làm trái chuẩn mực biên tập:</strong> không có chính sách rút bài, không nói rõ giấy phép xuất bản mở, yêu cầu chuyển nhượng bản quyền không phù hợp.',
    '<strong>Thiếu minh bạch:</strong> không có thông tin liên hệ rõ ràng, không công khai phí, khó kiểm chứng biên tập viên.',
    '<strong>Mời gửi bài ồ ạt:</strong> email khen ngợi quá mức, gửi liên tục, mời cả người không cùng chuyên ngành, giục gửi gấp cho "số sắp ra".',
])
c += P('Thêm một dấu hiệu dễ thấy: tạp chí cam kết chấp nhận bài hoặc hứa thời gian bình duyệt ngắn bất thường (Think. Check. Submit., n.d.).')

c += H2('Kiểm tra một tạp chí bằng Think. Check. Submit. thế nào?')
c += P('Think. Check. Submit. là sáng kiến giúp nhà nghiên cứu chọn tạp chí đáng tin. Bộ câu hỏi gồm (Think. Check. Submit., n.d.):')
c += UL([
    'Bạn hoặc đồng nghiệp có biết tạp chí này không?',
    'Có dễ dàng xác định và liên hệ nhà xuất bản không?',
    'Tạp chí có nói rõ hình thức bình duyệt không?',
    'Bài báo có được lập chỉ mục và lưu trữ trong các cơ sở dữ liệu chuyên dụng không?',
    'Các khoản phí có được nêu rõ không?',
    'Trang web có hướng dẫn cho tác giả không?',
    'Nhà xuất bản có là thành viên của các tổ chức uy tín trong ngành, như COPE, DOAJ hay OASPA không?',
])
c += P('Khuyến nghị của sáng kiến này là chỉ gửi bài khi trả lời "có" cho hầu hết hoặc tất cả các câu hỏi (Think. Check. Submit., n.d.). Người đọc cũng có thể dùng chính các câu hỏi này để đánh giá một bài báo được chia sẻ trên mạng.')

c += H2('Vì sao người đọc phổ thông cũng nên quan tâm?')
c += P('Tạp chí săn mồi không chỉ là chuyện của giới học thuật. Khi một bài chưa được bình duyệt nghiêm túc vẫn mang danh "nghiên cứu đăng trên tạp chí quốc tế", nó có thể được dùng để quảng cáo sản phẩm, củng cố tin đồn hoặc tạo vẻ khoa học cho các tuyên bố sai.')
c += P('Vì vậy, khi thấy một bài báo hay quảng cáo dẫn "nghiên cứu khoa học", nên kiểm tra thêm tạp chí đăng bài đó. Bài ' + A('kiem-tra-nghien-cuu-chia-se-tren-mang', 'kiểm tra nghiên cứu được chia sẻ trên mạng') + ' hướng dẫn các bước chung, và bài ' + A('preprint-la-gi-co-dang-tin-khong', 'preprint là gì') + ' giải thích một dạng công bố khác cũng chưa qua bình duyệt nhưng minh bạch về điều đó.')

c += H2('Câu hỏi thường gặp')
c += H3('Tạp chí thu phí đăng bài có phải đều là tạp chí săn mồi?')
c += P('Không. Nhiều tạp chí xuất bản mở uy tín cũng thu phí xử lý bài. Điểm khác biệt là chất lượng bình duyệt và mức độ minh bạch, không phải việc có thu phí hay không (Grudniewicz và cộng sự, 2019).')
c += H3('Có danh sách nào liệt kê tất cả tạp chí săn mồi không?')
c += P('Không có danh sách nào đầy đủ và được công nhận chung. Grudniewicz và cộng sự (2019) cho biết có hơn 90 bộ tiêu chí nhận diện tạp chí săn mồi, nhưng chỉ ba bộ được xây dựng dựa trên bằng chứng nghiên cứu. Vì vậy, nên tự kiểm tra theo các câu hỏi ở trên thay vì chỉ dựa vào một danh sách.')
c += H3('Nhà nghiên cứu có thật sự đăng bài trên tạp chí săn mồi?')
c += P('Có. Một nghiên cứu tại Ý trên khoảng 46.000 nhà nghiên cứu cho thấy khoảng 5% từng đăng bài trên các ấn phẩm săn mồi (Grudniewicz và cộng sự, 2019).')

c += H2('Điều gì nên nhớ?')
c += P('Không phải mọi bài báo mang danh "tạp chí khoa học" đều đáng tin như nhau. Tạp chí săn mồi thu phí nhưng bỏ qua kiểm định chất lượng, và số bài của chúng đã lên đến hàng trăm nghìn mỗi năm. Trước khi tin, chia sẻ hay gửi bài, hãy dành vài phút kiểm tra tạp chí theo bộ câu hỏi Think. Check. Submit.')
c += GEN_END + REFS([GR, SB, TCS])

d = dict(slug='tap-chi-san-moi-predatory-journal-la-gi', title='Tạp chí săn mồi (predatory journal) là gì và nhận biết thế nào?',
    seo_title='Tạp chí săn mồi là gì? Dấu hiệu nhận biết predatory journal',
    meta_desc='Tạp chí săn mồi thu phí nhưng không bình duyệt nghiêm túc. Định nghĩa, 4 nhóm dấu hiệu nhận biết và cách kiểm tra tạp chí bằng Think. Check. Submit.',
    focus_kw='tạp chí săn mồi',
    excerpt='Tạp chí săn mồi thu phí nhưng bỏ qua bình duyệt. Định nghĩa đồng thuận quốc tế, 4 nhóm dấu hiệu và bộ câu hỏi Think. Check. Submit. để kiểm tra một tạp chí.',
    tags=['tạp chí săn mồi', 'predatory journal', 'bình duyệt', 'thông tin khoa học', 'kiểm chứng'], content=c, categories=[3, 9],
    date='2026-10-30T16:00:00', cover_alt='Minh họa lưỡi câu móc vào một cuốn tạp chí khoa học, bên cạnh email cảnh báo và biểu tượng tiền, tượng trưng cho tạp chí săn mồi')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

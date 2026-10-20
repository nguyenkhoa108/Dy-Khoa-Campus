import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'


WHO = 'World Health Organization. (2023, ngày 23 tháng 7). <em>New WHO guidance on HIV viral suppression and scientific updates released at IAS 2023</em>. https://www.who.int/news/item/23-07-2023-new-who-guidance-on-hiv-viral-suppression-and-scientific-updates-released-at-ias-2023'
CDCT = 'Centers for Disease Control and Prevention. (2024b). <em>Treating HIV</em>. https://www.cdc.gov/hiv/treatment/index.html'
CDCP = 'Centers for Disease Control and Prevention. (2024a). <em>Preventing HIV</em>. https://www.cdc.gov/hiv/prevention/index.html'
CAL = 'Calabrese, S. K., Bor, J., Dukashe, M., Kalwicz, D. A., Mupeli, K., Onoya, D., Stackpool-Moore, L., &amp; Richman, B. (2025). A call to action to advance global research priorities related to Undetectable = Untransmittable. <em>Journal of the International AIDS Society, 28</em>(12), Article e70069. https://doi.org/10.1002/jia2.70069'
TAN = 'Tan, R. K. J., Lim, J. M., &amp; Chan, J. K. W. (2021). Is "Undetectable = Untransmissible" good public health messaging? <em>AMA Journal of Ethics, 23</em>(5), E418-422. https://doi.org/10.1001/amajethics.2021.418'
BVH = 'Q. Hoa. (2019, ngày 7 tháng 8). Có thể kiểm soát được dịch HIV/AIDS với chiến dịch K=K. <em>Báo Văn Hóa</em>. https://baovanhoa.vn/y-te/co-the-kiem-soat-duoc-dich-hivaids-voi-chien-dich-kk-50324.html'

c = ''
c += P('K=K là viết tắt của "Không phát hiện = Không lây truyền", phiên bản tiếng Việt của thông điệp quốc tế U=U (Undetectable = Untransmittable). Thông điệp này nói rằng người sống chung với HIV điều trị thuốc kháng virus (ARV) đều đặn và duy trì tải lượng virus ở mức không phát hiện được sẽ không lây truyền HIV cho bạn tình qua quan hệ tình dục (World Health Organization [WHO], 2023; Centers for Disease Control and Prevention [CDC], 2024b).')
c += P('Đây là bài cuối trong chuỗi "Tình dục học và truyền thông". Bài giải thích K=K là gì và vì sao một thông điệp có bằng chứng khoa học rõ ràng vẫn khó đến được với công chúng.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Tải lượng virus không phát hiện được: không lây HIV qua quan hệ tình dục.',
    'Tải lượng virus từ 1.000 bản sao/mL trở xuống: nguy cơ lây truyền không đáng kể, gần như bằng không (WHO, 2023).',
    'K=K chỉ đúng khi người bệnh duy trì điều trị đều đặn; K=K không phòng được các bệnh lây truyền qua đường tình dục khác.',
    'Việt Nam triển khai chiến dịch K=K do Cục Phòng, chống HIV/AIDS (Bộ Y tế) chủ trì, với mục tiêu giảm kỳ thị (Q. Hoa, 2019).',
    'Thông điệp vẫn chưa đến được với nhiều người, một phần vì chính người làm chuyên môn ngại nói "không lây" (Calabrese và cộng sự, 2025).',
])

c += H2('K=K là gì?')
c += P('Tải lượng virus là lượng HIV trong máu. Khi điều trị ARV hiệu quả, tải lượng virus giảm xuống mức xét nghiệm không phát hiện được. CDC (2024b) khẳng định: người có tải lượng virus không phát hiện được sẽ không lây truyền HIV qua quan hệ tình dục. Phần lớn người bệnh có thể kiểm soát HIV trong vòng sáu tháng sau khi bắt đầu điều trị (CDC, 2024b).')
c += P('Năm 2023, Tổ chức Y tế Thế giới (WHO) bổ sung một mốc khác: người có tải lượng virus từ 1.000 bản sao/mL trở xuống, thường được gọi là đã ức chế virus, có nguy cơ lây truyền HIV "không đáng kể, hoặc gần như bằng không" (WHO, 2023).')
c += TABLE(['Mức tải lượng virus', 'Nguy cơ lây HIV qua quan hệ tình dục', 'Nguồn'], [
    ['Không phát hiện được', 'Không lây truyền', 'WHO (2023); CDC (2024b)'],
    ['Từ 1.000 bản sao/mL trở xuống (ức chế virus)', 'Không đáng kể, gần như bằng không', 'WHO (2023)'],
])
c += P('Bảng do người viết tổng hợp từ các nguồn trên.')

c += H2('Những điều K=K không nói')
c += UL([
    '<strong>K=K không phải vĩnh viễn.</strong> Tại buổi giới thiệu chiến dịch ở Việt Nam, Cục trưởng Cục Phòng, chống HIV/AIDS Nguyễn Hoàng Long nhấn mạnh người bệnh phải tiếp tục tuân thủ điều trị, nếu không tải lượng virus sẽ tăng trở lại (Q. Hoa, 2019).',
    '<strong>K=K chỉ nói về HIV.</strong> Bao cao su vẫn có hiệu quả cao trong phòng HIV và các bệnh lây truyền qua đường tình dục khác (CDC, 2024a). Xem thêm bài ' + A('cac-benh-lay-truyen-qua-duong-tinh-duc-thuong-gap', 'các bệnh lây truyền qua đường tình dục thường gặp') + '.',
    '<strong>K=K nói về đường tình dục.</strong> Với việc dùng chung bơm kim tiêm, tải lượng virus không phát hiện được có thể làm giảm nguy cơ, nhưng chưa rõ giảm bao nhiêu (CDC, 2024b).',
])

c += H2('Vì sao K=K quan trọng với truyền thông?')
c += P('K=K không chỉ là thông tin y khoa, mà còn là một thông điệp chống kỳ thị. Tan và cộng sự (2021) cho rằng mục tiêu của thông điệp là giảm kỳ thị và khuyến khích người nhiễm HIV điều trị sớm nhất có thể. Ở Việt Nam, một mục tiêu được nêu của chiến dịch K=K là giảm kỳ thị, giúp xã hội nhìn HIV như một bệnh mạn tính có thể kiểm soát (Q. Hoa, 2019).')
c += P('Calabrese và cộng sự (2025) tổng hợp một số bằng chứng: tại Hồng Kông, việc không biết hoặc hoài nghi về U=U gắn với thái độ kỳ thị HIV cao hơn; tại Mỹ, 82% người tham gia (nam giới đồng tính, song tính và nam giới có quan hệ tình dục đồng giới khác sống chung với HIV) trong một khảo sát cho biết U=U giúp họ cảm thấy tốt hơn về tình trạng HIV của mình.')

c += H2('Vì sao thông điệp vẫn khó đến với công chúng?')
c += P('Theo Calabrese và cộng sự (2025), thông điệp U=U "chưa đến được với nhiều người sống chung với HIV". Các tác giả chỉ ra một số rào cản từ phía người truyền thông:')
c += UL([
    '<strong>Người làm chuyên môn ngần ngại:</strong> một số nhân viên y tế còn nghi ngờ bằng chứng, không thoải mái với cách nói tuyệt đối "không có nguy cơ", hoặc lo ngại trách nhiệm pháp lý, đạo đức.',
    '<strong>Ngôn ngữ mơ hồ:</strong> những cách nói như "gần như không thể" hay "không đáng kể" có thể làm suy yếu thông điệp.',
    '<strong>Hướng dẫn thay đổi:</strong> cách diễn đạt "gần như bằng không" của WHO (2023) cho mức tải lượng virus đã ức chế nhưng vẫn phát hiện được có thể khiến người nghe nhầm lẫn với thông điệp "không lây" ở mức không phát hiện được.',
    '<strong>Kỳ thị:</strong> kỳ thị có thể ảnh hưởng đến cách nhân viên y tế nói về U=U, kể cả khi họ không nhận ra.',
])
c += P('Đây là một tình huống điển hình của ' + '<a href="https://dykhoa.com/blog/thuat-ngu/truyen-thong-rui-ro-risk-communication/">truyền thông rủi ro</a>' + ': khi bằng chứng rõ ràng, việc nói nước đôi để "an toàn" lại có thể khiến công chúng hiểu sai.')

c += H2('Truyền thông K=K: nên và không nên')
c += P('Dựa trên các nguồn trong bài, người viết gợi ý một số nguyên tắc:')
c += TABLE(['Nên', 'Không nên'], [
    ['Nói rõ: tải lượng virus không phát hiện được thì không lây HIV qua quan hệ tình dục', 'Dùng cách nói mơ hồ như "rất khó lây", "gần như không thể" cho mức không phát hiện được'],
    ['Phân biệt mức "không phát hiện được" và mức "đã ức chế" (từ 1.000 bản sao/mL trở xuống)', 'Đánh đồng hai mức này'],
    ['Nhấn mạnh điều kiện: điều trị đều đặn và xét nghiệm tải lượng virus', 'Nói như thể K=K là trạng thái vĩnh viễn'],
    ['Nhắc rằng K=K không phòng các bệnh lây truyền qua đường tình dục khác', 'Gợi ý rằng không cần bao cao su trong mọi trường hợp'],
    ['Dùng K=K để giảm kỳ thị', 'Chia người sống chung với HIV thành nhóm "tốt" (không phát hiện) và "xấu" (chưa ức chế)'],
])
c += P('Nguyên tắc cuối dựa trên cảnh báo của Tan và cộng sự (2021): thông điệp có thể làm sâu thêm khoảng cách giữa người đã và chưa ức chế được virus, và những người khó tiếp cận xét nghiệm, thuốc men có thể cảm thấy bị bỏ lại phía sau. Các tác giả khuyến nghị tiếp tục truyền thông U=U nhưng thiết kế cẩn trọng, tránh đơn giản hóa quá mức, và gắn với cam kết bảo đảm tiếp cận công bằng xét nghiệm, điều trị.')

c += H2('Câu hỏi thường gặp')
c += H3('Người có tải lượng virus không phát hiện được có cần dùng bao cao su không?')
c += P('Với nguy cơ lây HIV qua quan hệ tình dục, câu trả lời theo CDC (2024b) là không lây. Tuy nhiên, bao cao su vẫn giúp phòng các bệnh lây truyền qua đường tình dục khác (CDC, 2024a), nên nhiều người vẫn chọn dùng.')
c += H3('Bao lâu thì đạt mức không phát hiện được?')
c += P('Theo CDC (2024b), phần lớn người bệnh có thể kiểm soát HIV trong vòng sáu tháng điều trị. Cách duy nhất để biết là xét nghiệm tải lượng virus theo chỉ định của bác sĩ.')
c += H3('K=K có áp dụng cho việc lây từ mẹ sang con?')
c += P('WHO (2023) cho biết người có tải lượng virus không phát hiện được có nguy cơ thấp lây truyền HIV sang con. Đây là nguy cơ thấp, không phải bằng không, nên phụ nữ mang thai sống chung với HIV cần được tư vấn riêng bởi nhân viên y tế.')

c += H2('Điều gì nên nhớ?')
c += P('K=K là một trong những thông điệp sức khỏe có bằng chứng rõ ràng nhất: tải lượng virus không phát hiện được thì không lây HIV qua quan hệ tình dục. Thách thức của người làm truyền thông là nói điều đó một cách rõ ràng, kèm đủ điều kiện, và dùng nó để giảm kỳ thị thay vì tạo ra một kiểu kỳ thị mới.')
c += GEN_END + REFS([CAL, CDCP, CDCT, BVH, TAN, WHO])

d = dict(slug='k-k-la-gi-khong-phat-hien-khong-lay-truyen', title='K=K là gì? Truyền thông "Không phát hiện = Không lây truyền" sao cho đúng',
    seo_title='K=K là gì? Không phát hiện = Không lây truyền HIV',
    meta_desc='K=K: người sống chung với HIV có tải lượng virus không phát hiện được sẽ không lây HIV qua tình dục. Bằng chứng từ WHO, CDC và cách truyền thông K=K đúng.',
    focus_kw='K=K là gì',
    excerpt='K=K (Không phát hiện = Không lây truyền) nghĩa là gì, cần điều kiện nào, và vì sao thông điệp có bằng chứng rõ ràng vẫn khó đến với công chúng.',
    tags=['K=K', 'U=U', 'HIV', 'truyền thông sức khỏe', 'tình dục học và truyền thông'], content=c, categories=[5, 14],
    date='2026-12-01T19:30:00', cover_alt='Minh họa ống nghiệm với chỉ số bằng không và dấu bằng, tượng trưng cho thông điệp K=K về HIV')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

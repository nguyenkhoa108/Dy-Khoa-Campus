import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'


SK = 'Federal Trade Commission. (2012, ngày 16 tháng 5). <em>Skechers will pay $40 million to settle FTC charges that it deceived consumers with ads for "toning shoes"</em> [Thông cáo báo chí]. https://www.ftc.gov/news-events/news/press-releases/2012/05/skechers-will-pay-40-million-settle-ftc-charges-it-deceived-consumers-ads-toning-shoes'
RB = 'Federal Trade Commission. (2011, ngày 28 tháng 9). <em>Reebok to pay $25 million in customer refunds to settle FTC charges of deceptive advertising of EasyTone and RunTone shoes</em> [Thông cáo báo chí]. https://www.ftc.gov/news-events/news/press-releases/2011/09/reebok-pay-25-million-customer-refunds-settle-ftc-charges-deceptive-advertising-easytone-runtone'
ND87 = 'Chính phủ. (2026). <em>Nghị định số 87/2026/NĐ-CP quy định xử phạt vi phạm hành chính trong lĩnh vực văn hóa và quảng cáo</em>. Công báo điện tử Chính phủ. https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-87-2026-nd-cp-469359.htm'

c = ''
c += P('"Đi bộ cũng săn chắc mông, đùi, không cần đến phòng tập" là lời hứa của dòng giày "toning" từng bán rất chạy tại Mỹ. Ủy ban Thương mại Liên bang Mỹ (FTC) cáo buộc hai hãng lớn quảng cáo các lời hứa này mà không có đủ căn cứ khoa học: Reebok đồng ý trả 25 triệu USD năm 2011, Skechers đồng ý trả 40 triệu USD năm 2012, và số tiền được dùng để hoàn tiền cho người mua (Federal Trade Commission [FTC], 2011, 2012).')
c += P('Đây là bài thứ tám trong chuyên đề "Bóc mác y khoa trong quảng cáo". Bài trước kể lại ' + A('sua-chua-tang-mien-dich-vu-activia-ftc', 'vụ Activia') + '.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Reebok quảng cáo giày EasyTone giúp cơ mông săn chắc hơn 28% so với giày thường; FTC cho rằng con số này không được chứng minh.',
    'Skechers quảng cáo giày Shape-ups giúp giảm cân, săn chắc cơ; FTC cáo buộc công ty không có căn cứ và chọn lọc kết quả nghiên cứu.',
    'Một "chuyên gia" trong quảng cáo của Skechers được công ty trả tiền làm nghiên cứu và có vợ là giám đốc tiếp thị của hãng, theo FTC.',
    'Dàn xếp không phải là thừa nhận vi phạm, nhưng hai hãng bị cấm đưa ra các tuyên bố sức khỏe không có căn cứ khoa học.',
])

c += H2('Reebok: "săn chắc hơn 28% chỉ bằng cách đi bộ"')
c += P('Theo FTC (2011), từ đầu năm 2009 Reebok quảng cáo giày đi bộ EasyTone và giày chạy RunTone trên báo in, truyền hình, internet, hộp giày và kệ trưng bày. Quảng cáo nói đế giày có các túi khí di chuyển, tạo ra "sự mất ổn định vi mô" giúp săn chắc và tăng sức mạnh cơ khi đi hoặc chạy.')
c += P('FTC cáo buộc Reebok đưa ra các tuyên bố không có căn cứ rằng giày giúp cơ chân, cơ mông săn chắc hơn giày thường, và tuyên bố sai rằng đi giày EasyTone đã được chứng minh giúp cơ mông săn chắc hơn 28%, cơ đùi sau và cơ bắp chân hơn 11% so với giày đi bộ thường. Một quảng cáo truyền hình cho thấy một phụ nữ chỉ vào biểu đồ các nhóm cơ, trong khi máy quay tập trung vào vòng ba của cô (FTC, 2011).')
c += P('Giày EasyTone và RunTone có giá 80 đến 100 USD một đôi. Reebok đồng ý trả 25 triệu USD, dùng để hoàn tiền cho người mua (FTC, 2011).')

c += H2('Skechers: "lấy lại vóc dáng khi đi bộ"')
c += P('Theo FTC (2012), Skechers quảng cáo giày Shape-ups với các khẩu hiệu "Shape Up While You Walk" (lấy lại vóc dáng khi đi bộ) và "Get in Shape without Setting Foot in a Gym" (lấy lại vóc dáng mà không cần đến phòng tập), cho rằng giày giúp giảm cân và săn chắc cơ nhiều hơn giày thể thao thông thường. FTC cũng nêu các dòng Resistance Runner, Toners và Tone-ups.')
c += P('FTC (2012) chỉ ra ba kiểu "mượn khoa học" trong quảng cáo của Skechers:')
c += UL([
    '<strong>Nghiên cứu "độc lập" không độc lập:</strong> quảng cáo có lời khuyên dùng của một bác sĩ nắn chỉnh cột sống, dựa trên một nghiên cứu "độc lập" do chính ông thực hiện. FTC cáo buộc nghiên cứu không cho kết quả như quảng cáo nói, Skechers không công bố việc ông có vợ là một giám đốc tiếp thị của hãng, và hãng đã trả tiền cho ông thực hiện nghiên cứu.',
    '<strong>Chọn lọc kết quả:</strong> quảng cáo giày Resistance Runner nói giày tăng "mức hoạt động cơ" tới 85% với cơ tư thế, 71% với một cơ mông và 68% với cơ bắp chân so với giày chạy thường. FTC cáo buộc Skechers chọn lọc kết quả từ nghiên cứu được dẫn.',
    '<strong>Người nổi tiếng:</strong> quảng cáo có sự xuất hiện của Kim Kardashian và Brooke Burke. Quảng cáo phát trong Super Bowl 2011 cho thấy Kardashian "bỏ" huấn luyện viên cá nhân để chọn giày Shape-ups.',
])
c += P('Giám đốc Văn phòng Bảo vệ Người tiêu dùng của FTC khi đó, David Vladeck, nhận xét các tuyên bố không có căn cứ của Skechers không dừng ở cơ bắp săn chắc, mà còn nói về giảm cân và sức khỏe tim mạch (FTC, 2012).')
c += P('Skechers đồng ý trả 40 triệu USD. Dàn xếp với FTC là một phần của thỏa thuận rộng hơn với tổng chưởng lý của 44 bang và Đặc khu Columbia (FTC, 2012).')

c += H2('Dàn xếp cấm những gì?')
c += P('Hai thỏa thuận có nội dung tương tự. Các hãng bị cấm đưa ra tuyên bố về tăng sức mạnh cơ, mức độ săn chắc tính bằng phần trăm, giảm cân hay bất kỳ lợi ích sức khỏe, thể lực nào khác của giày "toning", trừ khi tuyên bố đúng và có bằng chứng khoa học; đồng thời không được trình bày sai kết quả thử nghiệm, nghiên cứu (FTC, 2011, 2012).')
c += P('FTC ghi chú trong cả hai thông cáo: đơn kiện không phải là kết luận rằng công ty đã vi phạm pháp luật, và thỏa thuận dàn xếp không đồng nghĩa với việc công ty thừa nhận vi phạm (FTC, 2011, 2012).')

c += H2('Bài học cho người đọc quảng cáo')
c += TABLE(['Dấu hiệu trong quảng cáo', 'Ví dụ từ hai vụ việc', 'Câu hỏi nên đặt ra'], [
    ['Con số phần trăm cụ thể', '"Săn chắc hơn 28%", "tăng 85% mức hoạt động cơ"', 'Đo bằng cách nào, trên bao nhiêu người, so với gì?'],
    ['Nghiên cứu "độc lập"', 'Bác sĩ được trả tiền, có quan hệ gia đình với nhãn hàng', 'Ai tài trợ, ai thực hiện, có xung đột lợi ích không?'],
    ['Lời hứa thay thế tập luyện', '"Không cần đến phòng tập"', 'Lợi ích có thật sự nhiều hơn giày thường?'],
    ['Người nổi tiếng', 'Quảng cáo phát trong Super Bowl', 'Họ có dùng thật và có hiểu sản phẩm không?'],
])
c += P('Bảng do người viết tổng hợp từ FTC (2011, 2012). Về cách một kết quả có thể được "chọn lọc" giữa nhiều phép đo, xem thêm bài ' + A('da-chung-minh-lam-sang-nghia-la-gi', '"đã chứng minh lâm sàng" có đáng tin không') + '.')

c += H2('Ở Việt Nam, quy định thế nào?')
c += UL([
    'Quảng cáo không đúng hoặc gây nhầm lẫn về chất lượng, công dụng của sản phẩm so với nội dung đã đăng ký, công bố có thể bị phạt từ 80 đến 100 triệu đồng (Chính phủ, 2026, Điều 50 khoản 5).',
    'Người có ảnh hưởng giới thiệu sản phẩm khi chưa sử dụng hoặc chưa hiểu rõ về sản phẩm bị phạt từ 80 đến 100 triệu đồng (Chính phủ, 2026, Điều 51 khoản 3).',
    'Quảng cáo so sánh sản phẩm của mình với sản phẩm cùng loại của tổ chức, cá nhân khác mà không có tài liệu hợp pháp chứng minh bị phạt từ 40 đến 60 triệu đồng (Chính phủ, 2026, Điều 50 khoản 4).',
])
c += P('Các mức trên áp dụng với cá nhân; tổ chức bị phạt gấp đôi (Chính phủ, 2026, Điều 6 khoản 3).')

c += H2('Câu hỏi thường gặp')
c += H3('Giày "săn chắc cơ" có tác dụng không?')
c += P('FTC cho rằng Reebok và Skechers không có đủ căn cứ khoa học cho các tuyên bố về săn chắc cơ, giảm cân trong quảng cáo của mình (FTC, 2011, 2012). Bài này không đánh giá tác dụng của từng mẫu giày.')
c += H3('Người mua được hoàn tiền thế nào?')
c += P('Số tiền dàn xếp được dùng để hoàn tiền cho người mua, trực tiếp qua FTC hoặc qua một vụ kiện tập thể được tòa án chấp thuận (FTC, 2011, 2012).')

c += H2('Điều gì nên nhớ?')
c += P('Con số phần trăm cụ thể, một "nghiên cứu độc lập" và gương mặt nổi tiếng có thể khiến lời hứa "đi bộ cũng săn chắc" nghe rất khoa học. Hai vụ việc cho thấy cần hỏi ai làm nghiên cứu, ai trả tiền, và kết quả có bị chọn lọc hay không.')
c += GEN_END + REFS([ND87, RB, SK])

d = dict(slug='giay-san-chac-co-skechers-reebok-ftc', title='Giày "săn chắc cơ": khi Skechers và Reebok phải trả tiền vì quảng cáo',
    seo_title='Giày "săn chắc cơ": vụ Skechers, Reebok và FTC',
    meta_desc='Reebok trả 25 triệu USD, Skechers trả 40 triệu USD sau cáo buộc của FTC về quảng cáo giày "săn chắc cơ" thiếu căn cứ. Con số, nghiên cứu và người nổi tiếng.',
    focus_kw='giày săn chắc cơ',
    excerpt='Giày "toning" hứa đi bộ cũng săn chắc cơ. FTC cáo buộc Reebok và Skechers quảng cáo thiếu căn cứ, chọn lọc nghiên cứu và che giấu xung đột lợi ích.',
    tags=['giày săn chắc cơ', 'Skechers', 'Reebok', 'FTC', 'bóc mác y khoa'], content=c, categories=[3, 11],
    date='2026-11-19T16:00:00', cover_alt='Minh họa mẩu quảng cáo "Giày săn chắc cơ" bị bút đỏ ghi chú "Đi giày là đủ?"')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

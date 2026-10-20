import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'

ND87 = 'Chính phủ. (2026). <em>Nghị định số 87/2026/NĐ-CP quy định xử phạt vi phạm hành chính trong lĩnh vực văn hóa và quảng cáo</em>. Công báo điện tử Chính phủ. https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-87-2026-nd-cp-469359.htm'
LQC = 'Quốc hội. (2012). <em>Luật Quảng cáo số 16/2012/QH13</em>. https://thuvienphapluat.vn/van-ban/Thuong-mai/Luat-quang-cao-2012-142541.aspx'
L75 = 'Quốc hội. (2025). <em>Luật số 75/2025/QH15 sửa đổi, bổ sung một số điều của Luật Quảng cáo</em>. https://luatvietnam.vn/thuong-mai/luat-quang-cao-sua-doi-2025-so-75-2025-qh15-404208-d1.html'
LSVN = 'Hồng Hạnh. (2021, ngày 5 tháng 6). Từ 01/6, được quảng cáo bao cao su, băng vệ sinh trong "khung giờ vàng". <em>Luật sư Việt Nam</em>. https://lsvn.vn/tu-016-duoc-quang-cao-bao-cao-su-bang-ve-sinh-trong-khung-gio-vang1622883226-a104802.html'

c = ''
c += P('Theo pháp luật Việt Nam hiện hành, bao cao su được phép quảng cáo, kể cả trên truyền hình vào khung giờ vàng. Ngược lại, thuốc kê đơn và các sản phẩm "có tính chất kích dục" bị cấm quảng cáo. Những sản phẩm thường được gọi chung là "thuốc sinh lý" nằm ở giữa: được quảng cáo hay không, và phải tuân thủ điều gì, phụ thuộc vào việc sản phẩm đó là thuốc kê đơn, thuốc không kê đơn hay thực phẩm bảo vệ sức khỏe.')
c += P('Bài này mở đầu chuỗi bài "Tình dục học và truyền thông", tổng hợp các quy định chính từ Luật Quảng cáo và Nghị định 87/2026/NĐ-CP (có hiệu lực từ 15/5/2026) cho người làm marketing, truyền thông và nhà sáng tạo nội dung.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    '<strong>Bao cao su:</strong> không thuộc danh mục cấm quảng cáo. Quy định phạt khi quảng cáo bao cao su, băng vệ sinh trên truyền hình từ 18 giờ đến 20 giờ đã được bỏ từ ngày 1/6/2021.',
    '<strong>Thuốc kê đơn:</strong> cấm quảng cáo. Mức phạt từ 50 đến 70 triệu đồng với cá nhân.',
    '<strong>Sản phẩm "có tính chất kích dục":</strong> cấm quảng cáo. Mức phạt từ 70 đến 100 triệu đồng với cá nhân.',
    '<strong>Thực phẩm bảo vệ sức khỏe "tăng cường sinh lý":</strong> được quảng cáo nhưng phải có cụm từ, khuyến cáo bắt buộc và không được quảng cáo như thuốc chữa bệnh.',
    'Tổ chức vi phạm bị phạt gấp đôi mức của cá nhân.',
])

c += H2('Luật Quảng cáo cấm quảng cáo những gì?')
c += P('Điều 7 Luật Quảng cáo năm 2012 liệt kê các sản phẩm, hàng hóa, dịch vụ cấm quảng cáo. Hai nhóm liên quan trực tiếp đến chủ đề này là (Quốc hội, 2012):')
c += UL([
    '<strong>Khoản 5:</strong> thuốc kê đơn, và thuốc không kê đơn nhưng được cơ quan có thẩm quyền khuyến cáo hạn chế sử dụng hoặc sử dụng có sự giám sát của thầy thuốc.',
    '<strong>Khoản 6:</strong> các loại sản phẩm, hàng hóa có tính chất kích dục.',
])
c += P('Luật sửa đổi Luật Quảng cáo năm 2025 (Luật số 75/2025/QH15) không thay đổi danh mục này. Luật bổ sung quy định rằng việc quảng cáo thuốc được thực hiện theo pháp luật về dược (Quốc hội, 2025). Bao cao su không nằm trong danh mục cấm, nên được quảng cáo như các sản phẩm thông thường, miễn là nội dung quảng cáo không vi phạm các điều cấm chung.')

c += H2('Quảng cáo bao cao su: từng bị giới hạn khung giờ, nay thì sao?')
c += P('Trước đây, Nghị định 158/2013/NĐ-CP phạt từ 30 đến 50 triệu đồng nếu quảng cáo băng vệ sinh, bao cao su và các sản phẩm tương tự trên truyền thanh, truyền hình từ 18 giờ đến 20 giờ hằng ngày. Nghị định 38/2021/NĐ-CP, có hiệu lực từ ngày 1/6/2021, không còn quy định xử phạt hành vi này (Hồng Hạnh, 2021).')
c += P('Nghị định 87/2026/NĐ-CP thay thế Nghị định 38/2021/NĐ-CP từ ngày 15/5/2026 (Chính phủ, 2026, Điều 93). Khi rà soát toàn văn Nghị định 87/2026/NĐ-CP, người viết không tìm thấy quy định nào riêng về khung giờ quảng cáo bao cao su.')
c += P('Dù vậy, "được quảng cáo" không có nghĩa là quảng cáo kiểu gì cũng được. Nghị định 87/2026/NĐ-CP vẫn phạt từ 40 đến 60 triệu đồng với quảng cáo "trái với truyền thống lịch sử, văn hóa, đạo đức xã hội" hoặc có nội dung tạo cho trẻ em suy nghĩ, hành động trái với đạo đức, thuần phong mỹ tục (Chính phủ, 2026, Điều 50 khoản 4). Một quảng cáo bao cao su dùng hình ảnh, lời lẽ khiêu gợi có thể rơi vào các hành vi này.')

c += H2('"Thuốc sinh lý" được quảng cáo đến đâu?')
c += P('"Thuốc sinh lý" là cách gọi trong đời thường, không phải một nhóm sản phẩm theo pháp luật. Trên thị trường, cách gọi này có thể chỉ thuốc điều trị (cần đơn hoặc không cần đơn) hoặc thực phẩm bảo vệ sức khỏe. Mỗi loại có quy định quảng cáo khác nhau:')
c += TABLE(['Loại sản phẩm', 'Có được quảng cáo?', 'Điểm cần lưu ý'], [
    ['Thuốc kê đơn', 'Không', 'Phạt từ 50 đến 70 triệu đồng (Điều 49 khoản 1)'],
    ['Thuốc không kê đơn', 'Có, nếu không thuộc diện bị khuyến cáo hạn chế sử dụng', 'Phải có giấy xác nhận nội dung quảng cáo còn hiệu lực và quảng cáo đúng nội dung đã được xác nhận (Điều 69 khoản 4)'],
    ['Thực phẩm bảo vệ sức khỏe', 'Có', 'Phải ghi "Thực phẩm bảo vệ sức khỏe" và khuyến cáo "Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh" (Điều 71)'],
    ['Sản phẩm có tính chất kích dục', 'Không', 'Phạt từ 70 đến 100 triệu đồng (Điều 49 khoản 2)'],
])
c += P('Bảng do người viết tổng hợp từ Nghị định 87/2026/NĐ-CP (Chính phủ, 2026). Mức phạt trong bảng áp dụng với cá nhân.')
c += P('Với thực phẩm bảo vệ sức khỏe, rủi ro lớn nhất là quảng cáo như thuốc. Nghị định 87/2026/NĐ-CP phạt từ 30 đến 40 triệu đồng khi quảng cáo một sản phẩm không phải là thuốc (trừ thiết bị y tế) với nội dung dùng để "phòng bệnh, chữa bệnh, chẩn đoán bệnh, điều trị bệnh, giảm nhẹ bệnh, điều chỉnh chức năng sinh lý cơ thể người" (Chính phủ, 2026, Điều 69 khoản 4). Những câu như "chữa dứt điểm yếu sinh lý" trên một sản phẩm không phải thuốc là ví dụ điển hình. Các lỗi khác khi quảng cáo loại sản phẩm này được phân tích trong bài ' + A('quang-cao-thuc-pham-bao-ve-suc-khoe-loi-thuong-gap', 'quảng cáo thực phẩm bảo vệ sức khỏe: lỗi thường gặp') + '.')
c += P('Nếu chưa rõ một sản phẩm thuộc loại nào, người làm truyền thông nên yêu cầu nhãn hàng cung cấp giấy đăng ký lưu hành (với thuốc) hoặc giấy tiếp nhận đăng ký bản công bố sản phẩm (với thực phẩm bảo vệ sức khỏe) trước khi nhận việc.')

c += H2('KOL, người nổi tiếng cũng có thể bị phạt')
c += P('Trách nhiệm không chỉ thuộc về nhãn hàng. Nghị định 87/2026/NĐ-CP có các mức phạt riêng liên quan đến người quảng cáo và nội dung chứng thực (Chính phủ, 2026):')
c += UL([
    'Người có ảnh hưởng giới thiệu sản phẩm khi chưa sử dụng hoặc chưa hiểu rõ về sản phẩm: phạt từ 80 đến 100 triệu đồng (Điều 51 khoản 3).',
    'Người có ảnh hưởng không thông báo về việc quảng cáo ngay trước và trong khi quảng cáo: phạt từ 60 đến 80 triệu đồng (Điều 51 khoản 2).',
    'Quảng cáo thực phẩm có đăng tải, trích dẫn ý kiến người bệnh mô tả thực phẩm có tác dụng điều trị bệnh: phạt từ 20 đến 30 triệu đồng (Điều 71 khoản 4).',
])
c += P('Với nhóm sản phẩm sức khỏe tình dục, những lời "trải nghiệm" của người nổi tiếng hay người dùng thường là phần thuyết phục nhất của quảng cáo. Đây cũng là phần dễ vi phạm nhất. Về cách đánh giá lời khuyên sức khỏe từ người nổi tiếng, xem thêm bài ' + A('nguoi-noi-tieng-noi-ve-khoa-hoc-nen-tin-den-dau', 'người nổi tiếng nói về khoa học nên tin đến đâu') + '.')

c += H2('Danh sách kiểm tra trước khi đăng quảng cáo')
c += UL([
    'Xác định đúng loại sản phẩm: thuốc kê đơn, thuốc không kê đơn, thực phẩm bảo vệ sức khỏe hay sản phẩm thông thường.',
    'Với thuốc và thực phẩm bảo vệ sức khỏe: kiểm tra giấy xác nhận nội dung quảng cáo và chỉ dùng đúng nội dung đã được xác nhận.',
    'Với thực phẩm bảo vệ sức khỏe: có đủ cụm từ "Thực phẩm bảo vệ sức khỏe" và câu khuyến cáo bắt buộc.',
    'Không dùng từ ngữ chữa bệnh, điều trị cho sản phẩm không phải là thuốc.',
    'Không dùng hình ảnh, lời lẽ khiêu gợi; cân nhắc kênh và đối tượng tiếp cận để tránh tiếp cận trẻ em.',
    'Với KOL: dùng thử thật, hiểu sản phẩm và ghi rõ đây là nội dung quảng cáo.',
])
c += P('Danh sách do người viết tổng hợp, không thay thế ý kiến tư vấn pháp lý. Quy định có thể thay đổi, nên kiểm tra văn bản hiện hành trước khi triển khai chiến dịch.')

c += H2('Câu hỏi thường gặp')
c += H3('Có được quảng cáo bao cao su trên truyền hình giờ vàng không?')
c += P('Có. Quy định phạt khi quảng cáo bao cao su trên truyền thanh, truyền hình từ 18 giờ đến 20 giờ đã không còn từ ngày 1/6/2021 (Hồng Hạnh, 2021). Nội dung quảng cáo vẫn phải tuân thủ các điều cấm chung, như không trái với đạo đức xã hội.')
c += H3('Thuốc điều trị rối loạn cương có được quảng cáo không?')
c += P('Nếu là thuốc kê đơn thì không. Nếu là thuốc không kê đơn, thuốc phải không thuộc diện bị khuyến cáo hạn chế sử dụng và phải có giấy xác nhận nội dung quảng cáo. Về các rối loạn chức năng tình dục dưới góc độ sức khỏe, xem bài ' + A('roi-loan-chuc-nang-tinh-duc-thuong-gap', 'rối loạn chức năng tình dục thường gặp') + '.')
c += H3('Nhãn hàng hay agency bị phạt?')
c += P('Nghị định 87/2026/NĐ-CP xử phạt theo hành vi, nên cá nhân, tổ chức thực hiện hành vi vi phạm đều có thể bị xử phạt. Tổ chức bị phạt gấp đôi cá nhân với cùng một hành vi (Chính phủ, 2026, Điều 6 khoản 3). Ngoài tiền phạt, nội dung vi phạm còn bị buộc gỡ bỏ.')

c += H2('Điều gì nên nhớ?')
c += P('Pháp luật Việt Nam không cấm nói về sức khỏe tình dục trong quảng cáo. Bao cao su được quảng cáo rộng rãi, còn thuốc và thực phẩm bảo vệ sức khỏe được quảng cáo trong khuôn khổ. Ranh giới nằm ở hai điểm: không quảng cáo sản phẩm bị cấm (thuốc kê đơn, sản phẩm có tính chất kích dục), và không hứa hẹn chữa bệnh cho sản phẩm không phải là thuốc. Người làm truyền thông có trách nhiệm cần nắm rõ ranh giới này trước khi nhận một chiến dịch về ' + A('tinh-duc-hoc-la-gi', 'sức khỏe tình dục') + '.')
c += GEN_END + REFS([ND87, LSVN, LQC, L75])

d = dict(slug='quang-cao-bao-cao-su-thuoc-sinh-ly-luat-viet-nam', title='Quảng cáo bao cao su, thuốc sinh lý: luật Việt Nam cho phép gì?',
    seo_title='Quảng cáo bao cao su, thuốc sinh lý: luật cho phép gì?',
    meta_desc='Quảng cáo bao cao su được phép, thuốc kê đơn và sản phẩm kích dục bị cấm. Tổng hợp quy định và mức phạt theo Nghị định 87/2026 cho người làm truyền thông.',
    focus_kw='quảng cáo bao cao su',
    excerpt='Bao cao su được quảng cáo, thuốc kê đơn và sản phẩm kích dục bị cấm, còn "thuốc sinh lý" tùy loại. Quy định và mức phạt mới nhất theo Nghị định 87/2026.',
    tags=['quảng cáo bao cao su', 'luật quảng cáo', 'Nghị định 87/2026', 'thực phẩm bảo vệ sức khỏe', 'tình dục học và truyền thông'], content=c, categories=[5, 14],
    date='2026-11-13T19:30:00', cover_alt='Minh họa hộp bao cao su và vỉ thuốc cạnh cuốn sách luật, tượng trưng cho quy định quảng cáo sản phẩm sức khỏe tình dục')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

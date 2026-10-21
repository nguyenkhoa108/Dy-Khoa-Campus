import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'


NCCIH = 'National Center for Complementary and Integrative Health. (2025). <em>"Detoxes" and "cleanses": What you need to know</em>. https://www.nccih.nih.gov/health/detoxes-and-cleanses-what-you-need-to-know'
DBND = 'Hồng Nhung. (2026, ngày 8 tháng 1). Trào lưu "detox": Thải độc hay đánh đổi sức khỏe? <em>Đại biểu Nhân dân</em>. https://daibieunhandan.vn/trao-luu-detox-thai-doc-hay-danh-doi-suc-khoe-10402948.html'
ND87 = 'Chính phủ. (2026). <em>Nghị định số 87/2026/NĐ-CP quy định xử phạt vi phạm hành chính trong lĩnh vực văn hóa và quảng cáo</em>. Công báo điện tử Chính phủ. https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-87-2026-nd-cp-469359.htm'

c = ''
c += P('Chưa có bằng chứng thuyết phục cho thấy các chế độ "detox, thải độc" giúp loại bỏ độc tố khỏi cơ thể hay giảm cân bền vững. Trung tâm Quốc gia về Sức khỏe Bổ sung và Tích hợp Mỹ (NCCIH, thuộc Viện Y tế Quốc gia Mỹ) cho biết số nghiên cứu về các chương trình này còn ít và chất lượng thấp, chưa có nghiên cứu về tác động lâu dài, và một số sản phẩm "detox" từng bị cơ quan quản lý Mỹ xử lý vì chứa thành phần ẩn hoặc quảng cáo sai sự thật (National Center for Complementary and Integrative Health [NCCIH], 2025).')
c += P('Đây là bài thứ sáu trong chuyên đề "Bóc mác y khoa trong quảng cáo". Bài trước bóc cụm từ ' + A('da-chung-minh-lam-sang-nghia-la-gi', '"đã chứng minh lâm sàng"') + '.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Nghiên cứu về detox trên người còn ít, thiết kế yếu, ít người tham gia hoặc chưa qua bình duyệt.',
    'Nước ép, chế độ detox có thể gây giảm cân ban đầu do ăn ít calo, nhưng thường tăng cân trở lại khi ăn uống bình thường.',
    'Một số hình thức detox có rủi ro: thụt tháo đại tràng, thuốc nhuận tràng, nước ép không tiệt trùng, nhịn ăn kéo dài.',
    'Gan, thận là các cơ quan thải độc của cơ thể; liệu trình detox không thay thế được chúng.',
])

c += H2('"Detox" trong quảng cáo gồm những gì?')
c += P('Theo NCCIH (2025), các chương trình "thải độc" có thể gồm nhịn ăn, chỉ uống nước ép, chỉ ăn một số loại thực phẩm, dùng thực phẩm chức năng hoặc sản phẩm thương mại, dùng thảo dược, làm sạch đại tràng bằng thụt tháo, thuốc nhuận tràng hay rửa đại tràng, giảm tiếp xúc với môi trường, hoặc xông hơi. Chúng có thể được quảng cáo thương mại, cung cấp tại các trung tâm sức khỏe hoặc là một phần của liệu pháp tự nhiên.')
c += P('Cần phân biệt với liệu pháp thải kim loại (chelation therapy), một thủ thuật y khoa được Trung tâm Kiểm soát và Phòng ngừa Dịch bệnh Mỹ (CDC) khuyến nghị trong một số trường hợp ngộ độc kim loại nghiêm trọng. Đây không phải loại "detox" được bàn trong bài (NCCIH, 2025).')

c += H2('Nghiên cứu nói gì?')
c += P('NCCIH (2025) tóm tắt bằng chứng như sau:')
c += UL([
    'Chỉ có một số ít nghiên cứu về các chương trình "thải độc" trên người. Một số cho kết quả tích cực về cân nặng, mỡ, kháng insulin và huyết áp, nhưng chất lượng thấp do thiết kế có vấn đề, ít người tham gia hoặc chưa qua bình duyệt.',
    'Một tổng quan năm 2015 kết luận không có nghiên cứu thuyết phục ủng hộ chế độ "detox" để kiểm soát cân nặng hay loại bỏ độc tố.',
    'Một tổng quan năm 2017 cho biết nước ép và chế độ "detox" có thể gây giảm cân ban đầu do ăn ít calo, nhưng thường dẫn đến tăng cân khi ăn uống bình thường trở lại.',
    'Chưa có nghiên cứu nào về tác động lâu dài của các chương trình này.',
])
c += P('Báo Đại biểu Nhân dân dẫn lời Phó Giáo sư Tinsay Woreta, chuyên ngành tiêu hóa, gan mật tại Đại học Johns Hopkins (Mỹ): "Không có bằng chứng cho thấy các liệu trình thải độc bổ sung lợi ích nếu một người vốn đã ăn uống cân bằng" (Hồng Nhung, 2026).')

c += H2('Cơ thể có tự thải độc không?')
c += P('Theo bài viết trên báo Đại biểu Nhân dân, gan giữ vai trò trung tâm khi chuyển hóa các độc tố như rượu thành chất thải, còn thận lọc máu và đào thải chất thải qua nước tiểu. Các liệu trình detox không thể thay thế chức năng của gan, phổi, thận, cũng không đảo ngược được những tổn thương đã xảy ra (Hồng Nhung, 2026).')
c += P('Điều này giải thích vì sao câu hỏi "độc chất nào?" lại quan trọng. Một quảng cáo nói sản phẩm "thải độc" mà không nêu được độc chất cụ thể, cũng không có bằng chứng đo được độc chất đó giảm đi, là một tuyên bố khó kiểm chứng. Đoạn này là nhận định của người viết.')

c += H2('Detox có an toàn không?')
c += P('NCCIH (2025) nêu một số rủi ro:')
c += UL([
    'Cục Quản lý Thực phẩm và Dược phẩm Mỹ (FDA) và Ủy ban Thương mại Liên bang Mỹ (FTC) từng xử lý nhiều công ty bán sản phẩm detox vì chứa thành phần ẩn có thể gây hại, quảng cáo sai rằng chữa được bệnh nặng, hoặc quảng cáo thiết bị làm sạch đại tràng cho mục đích chưa được phê duyệt.',
    'Bằng chứng về rửa đại tràng còn hạn chế, và thủ thuật này có thể gây tác dụng phụ, có khi nghiêm trọng, nhất là ở người có bệnh tiêu hóa, từng phẫu thuật đại tràng, trĩ nặng, bệnh thận hoặc bệnh tim.',
    'Nước ép chưa tiệt trùng có thể gây bệnh, nghiêm trọng hơn ở trẻ em, người già và người suy giảm miễn dịch.',
    'Nước ép từ thực phẩm giàu oxalate như rau lá xanh, củ dền có thể gây hại cho người dễ bị sỏi thận.',
    'Thuốc nhuận tràng có thể gây tiêu chảy, dẫn đến mất nước và kém hấp thu.',
    'Uống nhiều nước, trà thảo mộc và nhịn ăn nhiều ngày liền có thể gây rối loạn điện giải nguy hiểm.',
    'Người bệnh đái tháo đường nên hỏi ý kiến nhân viên y tế trước khi thay đổi lớn chế độ ăn.',
])

c += H2('Ở Việt Nam, quy định thế nào?')
c += P('Nghị định 87/2026/NĐ-CP phạt từ 30 đến 40 triệu đồng đối với hành vi quảng cáo sản phẩm không phải là thuốc (trừ thiết bị y tế) có nội dung dùng để phòng bệnh, chữa bệnh, điều trị bệnh hoặc điều chỉnh chức năng sinh lý cơ thể người (Chính phủ, 2026, Điều 69 khoản 4). Quảng cáo thực phẩm có đăng tải, trích dẫn ý kiến người bệnh mô tả thực phẩm có tác dụng điều trị bệnh bị phạt từ 20 đến 30 triệu đồng (Chính phủ, 2026, Điều 71 khoản 4). Tổ chức bị phạt gấp đôi các mức trên (Chính phủ, 2026, Điều 6 khoản 3).')

c += H2('Câu hỏi thường gặp')
c += H3('Detox có giúp giảm cân không?')
c += P('Có thể giảm cân ban đầu do ăn ít calo, nhưng thường tăng cân trở lại khi ăn uống bình thường (NCCIH, 2025).')
c += H3('Uống nước ép detox mỗi ngày có tốt không?')
c += P('Chưa có bằng chứng thuyết phục về lợi ích thải độc. Nước ép chưa tiệt trùng có thể gây bệnh, và nước ép giàu oxalate có thể gây hại cho người dễ bị sỏi thận (NCCIH, 2025).')
c += H3('Nhịn ăn gián đoạn có phải là detox?')
c += P('Không hẳn. Theo NCCIH (2025), nhịn ăn gián đoạn đang được nghiên cứu cho một số mục tiêu sức khỏe, nhưng chưa có kết luận chắc chắn, và nhịn ăn có thể gây đau đầu, ngất, mệt mỏi, mất nước.')

c += H2('Điều gì nên nhớ?')
c += P('"Detox, thải độc" là một khái niệm tiếp thị hấp dẫn nhưng thiếu bằng chứng. Gan và thận là hệ thống thải độc của cơ thể. Trước khi thử một liệu trình detox, đặc biệt nếu có bệnh nền, hãy trao đổi với nhân viên y tế.')
c += GEN_END + REFS([ND87, DBND, NCCIH])

d = dict(slug='detox-thai-doc-co-that-khong', title='"Detox, thải độc": cơ thể có cần "thải độc" không?',
    seo_title='Detox thải độc có thật không? Bằng chứng nói gì',
    meta_desc='Detox thải độc chưa có bằng chứng thuyết phục giúp loại bỏ độc tố hay giảm cân bền vững, và có thể gây hại. NCCIH và chuyên gia nói gì về các liệu trình detox?',
    focus_kw='detox thải độc',
    excerpt='Nước ép, thụt tháo, nhịn ăn "thải độc" được quảng cáo rầm rộ. Nghiên cứu nói gì về hiệu quả, rủi ro, và cơ thể thực sự thải độc thế nào?',
    tags=['detox thải độc', 'nước ép detox', 'thải độc cơ thể', 'quảng cáo sức khỏe', 'bóc mác y khoa'], content=c, categories=[3, 11],
    date='2026-11-17T16:00:00', cover_alt='Minh họa mẩu quảng cáo "Detox, thải độc" bị bút đỏ ghi chú "Độc chất nào?"')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

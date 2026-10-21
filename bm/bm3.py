import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'


FDA = 'U.S. Food and Drug Administration. (2024, ngày 12 tháng 12). <em>Skip the antibacterial soap; use plain soap and water</em>. https://www.fda.gov/consumers/consumer-updates/skip-antibacterial-soap-use-plain-soap-and-water'
ASA = 'Advertising Standards Authority. (2013, ngày 26 tháng 6). <em>ASA ruling on Jeyes Group Ltd</em> (A13-227107). https://www.asa.org.uk/rulings/jeyes-group-ltd-a13-227107.html'
ND87 = 'Chính phủ. (2026). <em>Nghị định số 87/2026/NĐ-CP quy định xử phạt vi phạm hành chính trong lĩnh vực văn hóa và quảng cáo</em>. Công báo điện tử Chính phủ. https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-87-2026-nd-cp-469359.htm'

c = ''
c += P('Xà phòng diệt khuẩn chưa được chứng minh là tốt hơn xà phòng thường trong việc phòng bệnh. Theo Cục Quản lý Thực phẩm và Dược phẩm Mỹ (FDA), hiện chưa có đủ bằng chứng cho thấy xà phòng diệt khuẩn không kê đơn ngăn ngừa bệnh tốt hơn rửa tay bằng xà phòng thường và nước. Năm 2016, FDA đã cấm 19 hoạt chất, trong đó có triclosan và triclocarban, trong xà phòng và sữa tắm diệt khuẩn tiêu dùng (U.S. Food and Drug Administration [FDA], 2024).')
c += P('Đây là bài thứ ba trong chuyên đề "Bóc mác y khoa trong quảng cáo". Hai bài trước bóc con số ' + A('di-bo-10000-buoc-moi-ngay-co-can-thiet', '10.000 bước') + ' và ' + A('9-10-nha-si-khuyen-dung-khao-sat-gay-hieu-lam', '"9/10 nha sĩ khuyên dùng"') + '.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'FDA: chưa đủ bằng chứng xà phòng diệt khuẩn tiêu dùng phòng bệnh tốt hơn xà phòng thường.',
    'Từ năm 2016, 19 hoạt chất, gồm triclosan và triclocarban, không còn được bán trong xà phòng diệt khuẩn tiêu dùng tại Mỹ.',
    'Con số "99,9%" có thể đến từ thử nghiệm trong phòng thí nghiệm, vốn không cho biết sản phẩm có giúp bạn ít ốm hơn hay không.',
    'Rửa tay bằng xà phòng thường và nước vẫn là cách được FDA khuyến nghị.',
])

c += H2('FDA kết luận gì về xà phòng diệt khuẩn?')
c += P('Theo FDA (2024), quy định cuối cùng ban hành năm 2016 khiến 19 hoạt chất, trong đó có triclosan và triclocarban, không còn được bán trong các sản phẩm rửa sát khuẩn tiêu dùng không kê đơn, gồm xà phòng rửa tay dạng lỏng, bọt, gel, xà phòng bánh và sữa tắm.')
c += P('Lý do được FDA nêu rõ: các nhà sản xuất không cung cấp đủ dữ liệu chứng minh những hoạt chất này vừa an toàn khi dùng hằng ngày trong thời gian dài, vừa hiệu quả hơn xà phòng thường và nước trong việc ngăn ngừa bệnh và sự lây lan của một số bệnh nhiễm trùng (FDA, 2024).')
c += P('Bác sĩ Theresa M. Michele của FDA nhận định không có dữ liệu cho thấy các chất này bảo vệ thêm trước bệnh tật, và việc dùng chúng "có thể tạo cảm giác an toàn giả" cho người dùng (FDA, 2024).')

c += H2('Quy định này không áp dụng cho sản phẩm nào?')
c += UL([
    'Ba hoạt chất benzalkonium chloride, benzethonium chloride và chloroxylenol vẫn được dùng trong khi nhà sản xuất bổ sung dữ liệu mới về an toàn và hiệu quả.',
    'Quy định chỉ áp dụng cho xà phòng và sữa tắm diệt khuẩn tiêu dùng có dùng với nước.',
    'Quy định không áp dụng cho nước rửa tay khô, khăn ướt rửa tay, hoặc xà phòng diệt khuẩn dùng trong cơ sở y tế như bệnh viện, viện dưỡng lão.',
])
c += P('Nguồn: FDA (2024).')

c += H2('Con số "99,9%" thật ra đo điều gì?')
c += P('Các con số như "diệt 99,9% vi khuẩn" có thể dựa trên thử nghiệm trong phòng thí nghiệm. Một phán quyết của Cơ quan Tiêu chuẩn Quảng cáo Anh (ASA) cho thấy rõ giới hạn của kiểu con số này (Advertising Standards Authority [ASA], 2013):')
c += UL([
    'Năm 2013, một nhãn chất tẩy rửa bồn cầu quảng cáo "diệt 100% vi khuẩn bồn cầu".',
    'Nhãn hàng dẫn kết quả thử nghiệm theo tiêu chuẩn châu Âu EN1276, đạt mức giảm 99,999%, và làm tròn lên thành 100%.',
    'ASA lưu ý chính nhãn hàng thừa nhận phép thử EN1276 không thể cho kết quả loại bỏ 100% vi khuẩn, và việc làm tròn như vậy không phải thông lệ được chấp nhận trong ngành.',
    'ASA kết luận người tiêu dùng sẽ hiểu sản phẩm đã loại bỏ hoàn toàn mọi vi khuẩn khi thử nghiệm, nên quảng cáo gây hiểu lầm và thiếu căn cứ.',
])
c += P('Từ hai nguồn trên, người viết rút ra một điểm: con số phần trăm vi khuẩn bị diệt trong ống nghiệm trả lời câu hỏi "sản phẩm diệt được bao nhiêu vi khuẩn trong điều kiện thử nghiệm", chứ không trả lời câu hỏi người tiêu dùng thật sự quan tâm: "dùng sản phẩm này, tôi có ít bị bệnh hơn không?". Với xà phòng diệt khuẩn tiêu dùng, FDA (2024) cho biết câu hỏi thứ hai chưa có đủ bằng chứng.')
c += TABLE(['Quảng cáo nói', 'Câu hỏi nên đặt ra'], [
    ['"Diệt 99,9% vi khuẩn"', 'Thử trên những vi khuẩn nào, trong điều kiện nào, bao lâu?'],
    ['"Kháng khuẩn vượt trội"', 'Vượt trội so với cái gì: xà phòng thường hay không rửa tay?'],
    ['"Bảo vệ cả gia đình"', 'Có nghiên cứu cho thấy người dùng ít bị bệnh hơn không?'],
])
c += P('Bảng do người viết tổng hợp.')

c += H2('Ở Việt Nam, quy định thế nào?')
c += P('Với các sản phẩm thuộc nhóm hóa chất, chế phẩm diệt côn trùng, diệt khuẩn dùng trong gia dụng và y tế, Nghị định 87/2026/NĐ-CP có các mức phạt riêng (Chính phủ, 2026, Điều 72):')
c += UL([
    'Quảng cáo có nội dung không phù hợp với giấy chứng nhận đăng ký lưu hành: phạt từ 5 đến 10 triệu đồng.',
    'Quảng cáo thiếu tên sản phẩm, tên chủ sở hữu số đăng ký, tính năng công dụng, khuyến cáo "Đọc kỹ hướng dẫn sử dụng trước khi dùng" hoặc cảnh báo về hóa chất nguy hiểm: phạt từ 10 đến 20 triệu đồng.',
    'Quảng cáo chế phẩm diệt khuẩn chưa có số đăng ký lưu hành do Bộ Y tế cấp: phạt từ 20 đến 30 triệu đồng.',
])
c += P('Ngoài ra, quảng cáo không đúng hoặc gây nhầm lẫn về chất lượng, công dụng của sản phẩm so với nội dung đã đăng ký, công bố có thể bị phạt từ 80 đến 100 triệu đồng (Chính phủ, 2026, Điều 50 khoản 5). Các mức phạt trên áp dụng với cá nhân; tổ chức bị phạt gấp đôi (Chính phủ, 2026, Điều 6 khoản 3).')

c += H2('Vậy nên rửa tay thế nào?')
c += P('FDA khuyến nghị người tiêu dùng rửa tay bằng xà phòng thường và nước. Theo FDA, đây là một trong những cách hiệu quả nhất để ngăn vi trùng lây lan (FDA, 2024). Để nhận biết sản phẩm diệt khuẩn tại Mỹ, FDA lưu ý nhãn thường có chữ "antibacterial" và có thể chứa benzalkonium chloride, benzethonium chloride hoặc chloroxylenol (FDA, 2024).')

c += H2('Câu hỏi thường gặp')
c += H3('Xà phòng diệt khuẩn có tốt hơn xà phòng thường không?')
c += P('Theo FDA (2024), hiện chưa có đủ bằng chứng cho thấy xà phòng diệt khuẩn tiêu dùng phòng bệnh tốt hơn xà phòng thường và nước.')
c += H3('Triclosan là gì, vì sao bị cấm?')
c += P('Triclosan là một trong 19 hoạt chất bị FDA loại khỏi xà phòng và sữa tắm diệt khuẩn tiêu dùng từ năm 2016, vì nhà sản xuất không chứng minh được nó vừa an toàn khi dùng lâu dài, vừa hiệu quả hơn xà phòng thường (FDA, 2024).')
c += H3('Nước rửa tay khô có bị cấm không?')
c += P('Không. Quy định năm 2016 của FDA chỉ áp dụng cho xà phòng và sữa tắm dùng với nước, không áp dụng cho nước rửa tay khô (FDA, 2024).')

c += H2('Điều gì nên nhớ?')
c += P('"Diệt 99,9% vi khuẩn" là con số đo trong phòng thí nghiệm, không phải bằng chứng rằng bạn sẽ ít bị bệnh hơn. Với xà phòng diệt khuẩn tiêu dùng, FDA cho biết chưa có đủ bằng chứng về lợi ích vượt trội so với xà phòng thường, và rửa tay đúng cách bằng xà phòng thường vẫn là lựa chọn được khuyến nghị.')
c += GEN_END + REFS([ASA, ND87, FDA])

d = dict(slug='xa-phong-diet-khuan-99-9-co-tot-hon-xa-phong-thuong', title='"Diệt 99,9% vi khuẩn": xà phòng diệt khuẩn có tốt hơn xà phòng thường?',
    seo_title='Xà phòng diệt khuẩn có tốt hơn xà phòng thường?',
    meta_desc='FDA cho biết chưa đủ bằng chứng xà phòng diệt khuẩn phòng bệnh tốt hơn xà phòng thường và đã cấm 19 hoạt chất, gồm triclosan. Con số 99,9% thật ra đo điều gì?',
    focus_kw='xà phòng diệt khuẩn',
    excerpt='Con số "diệt 99,9% vi khuẩn" đo trong phòng thí nghiệm. FDA nói gì về xà phòng diệt khuẩn, vì sao triclosan bị cấm, và quy định quảng cáo tại Việt Nam.',
    tags=['xà phòng diệt khuẩn', 'diệt 99,9% vi khuẩn', 'triclosan', 'quảng cáo sức khỏe', 'bóc mác y khoa'], content=c, categories=[3, 11],
    date='2026-11-14T16:00:00', cover_alt='Minh họa nhãn quảng cáo "99,9% diệt khuẩn" bị bút đỏ ghi chú "So với xà phòng thường thì sao?"')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

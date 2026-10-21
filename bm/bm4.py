import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'


FDA1 = 'U.S. Food and Drug Administration. (2026, ngày 4 tháng 5). <em>Is it really "FDA approved"?</em> https://www.fda.gov/consumers/consumer-updates/it-really-fda-approved'
FDA2 = 'U.S. Food and Drug Administration. (2024, ngày 5 tháng 3). <em>Questions regarding whether food facilities are required to pay registration fees and private businesses claiming or suggesting an affiliation with FDA</em>. https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/questions-regarding-whether-food-facilities-are-required-pay-registration-fees-and-private'
ND87 = 'Chính phủ. (2026). <em>Nghị định số 87/2026/NĐ-CP quy định xử phạt vi phạm hành chính trong lĩnh vực văn hóa và quảng cáo</em>. Công báo điện tử Chính phủ. https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-87-2026-nd-cp-469359.htm'
LSVN = 'Huy Vũ. (2026, ngày 29 tháng 5). Chủ tịch UBND tỉnh cấp phép quảng cáo thực phẩm chức năng từ ngày 01/7. <em>Luật sư Việt Nam</em>. https://lsvn.vn/chu-tich-ubnd-tinh-cap-phep-quang-cao-thuc-pham-chuc-nang-tu-ngay-01-7-a172379.html'

c = ''
c += P('Cục Quản lý Thực phẩm và Dược phẩm Mỹ (FDA) không phê duyệt thực phẩm chức năng (dietary supplements) về độ an toàn và hiệu quả. FDA cũng không cấp "giấy chứng nhận đăng ký" cho cơ sở thực phẩm, và không công nhận loại giấy chứng nhận do doanh nghiệp tư nhân phát hành (U.S. Food and Drug Administration [FDA], 2024, 2026). Vì vậy, một sản phẩm thực phẩm chức năng quảng cáo "đạt chuẩn FDA" hay "được FDA chứng nhận" cần được xem xét rất kỹ.')
c += P('Đây là bài thứ tư trong chuyên đề "Bóc mác y khoa trong quảng cáo", và là bài đầu tiên trong nhóm "mác chứng nhận".')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'FDA phê duyệt thuốc mới và sinh phẩm, nhưng không phê duyệt thực phẩm chức năng, mỹ phẩm hay nhãn sản phẩm thực phẩm.',
    'Đăng ký cơ sở với FDA không có nghĩa là cơ sở hay sản phẩm được FDA phê duyệt.',
    'FDA không cấp giấy chứng nhận đăng ký cơ sở thực phẩm; giấy có logo FDA do bên tư nhân phát hành có thể vi phạm luật Mỹ.',
    'Ở Việt Nam, điều cần kiểm tra là giấy phép do cơ quan Việt Nam cấp, không phải "chuẩn FDA".',
])

c += H2('FDA phê duyệt gì, không phê duyệt gì?')
c += P('Theo FDA (2026), không phải mọi sản phẩm thuộc phạm vi quản lý của FDA đều phải được phê duyệt trước khi bán. Một số nhóm chính:')
c += TABLE(['Nhóm sản phẩm', 'FDA có phê duyệt trước khi bán?'], [
    ['Thuốc mới và sinh phẩm (gồm vắc-xin)', 'Có, trừ một số ngoại lệ hiếm'],
    ['Thuốc gốc và thuốc tương tự sinh học', 'Có'],
    ['Thiết bị y tế nguy cơ cao (nhóm III)', 'Thường phải được phê duyệt'],
    ['Thiết bị y tế nguy cơ trung bình (nhóm II)', 'Thường qua thủ tục "510(k) clearance", không phải phê duyệt'],
    ['Phụ gia thực phẩm, phẩm màu', 'Có, trừ một số ngoại lệ'],
    ['Thực phẩm chức năng', 'Không'],
    ['Mỹ phẩm', 'Không (trừ phẩm màu)'],
    ['Thực phẩm nói chung và nhãn sản phẩm', 'Không'],
    ['Cơ sở sản xuất', 'Không phê duyệt độc lập; FDA thanh tra cơ sở'],
])
c += P('Bảng do người viết tổng hợp từ FDA (2026).')

c += H2('Thực phẩm chức năng: FDA nói gì?')
c += P('FDA (2026) viết rõ: theo luật, FDA không phê duyệt thực phẩm chức năng về độ an toàn và hiệu quả, và nhiều sản phẩm có thể được bán mà thậm chí không cần thông báo với FDA. Doanh nghiệp tự chịu trách nhiệm bảo đảm sản phẩm an toàn, tuân thủ yêu cầu về nhãn và thực hành sản xuất tốt. FDA thanh tra cơ sở, theo dõi báo cáo biến cố bất lợi và có quyền hành động khi có lo ngại về an toàn.')
c += P('Với các tuyên bố về cấu trúc, chức năng cơ thể trên nhãn thực phẩm chức năng (ví dụ "canxi giúp xương chắc khỏe"), FDA cũng thường không phê duyệt. Những tuyên bố này phải kèm dòng lưu ý rằng tuyên bố chưa được FDA đánh giá, và sản phẩm không nhằm chẩn đoán, điều trị, chữa khỏi hay phòng ngừa bệnh (FDA, 2026).')

c += H2('"Đăng ký FDA" khác "được FDA phê duyệt"')
c += P('Đây là chỗ dễ gây nhầm lẫn nhất. Theo FDA (2026), việc một cơ sở đăng ký hoặc một sản phẩm được liệt kê với FDA không có nghĩa là cơ sở hay sản phẩm đó được phê duyệt, và cũng không có nghĩa sản phẩm được phép bán hợp pháp.')
c += P('Với cơ sở thực phẩm, FDA còn nói rõ hơn (FDA, 2024):')
c += UL([
    'Đăng ký cơ sở thực phẩm với FDA không mất phí, và không bắt buộc qua bên trung gian.',
    'FDA cấp một số đăng ký, nhưng không cấp giấy chứng nhận đăng ký hay chứng nhận tình trạng sản phẩm.',
    'FDA không công nhận các giấy chứng nhận đăng ký do doanh nghiệp tư nhân phát hành.',
    'Logo FDA chỉ dành cho FDA; dùng trái phép trên tài liệu tư nhân có thể vi phạm luật liên bang Mỹ.',
])
c += P('Nói cách khác, một tấm "giấy chứng nhận FDA" in logo FDA kèm trong quảng cáo thực phẩm chức năng không phải do FDA cấp.')

c += H2('Ở Việt Nam, nên kiểm tra điều gì?')
c += P('Sản phẩm bán và quảng cáo tại Việt Nam chịu sự quản lý của pháp luật Việt Nam. Một số quy định liên quan:')
c += UL([
    'Quảng cáo sản phẩm, hàng hóa, dịch vụ đặc biệt mà không có văn bản chứng nhận được phép lưu hành tại Việt Nam còn hiệu lực có thể bị phạt từ 30 đến 40 triệu đồng (Chính phủ, 2026, Điều 68 khoản 1).',
    'Với thuốc, sử dụng chứng nhận chưa được Bộ Y tế công nhận để quảng cáo bị phạt từ 30 đến 40 triệu đồng (Chính phủ, 2026, Điều 69 khoản 4).',
    'Quảng cáo thực phẩm bảo vệ sức khỏe phải được cơ quan nhà nước có thẩm quyền xác nhận nội dung. Từ ngày 1/7/2026, thẩm quyền này chuyển từ Cục An toàn thực phẩm (Bộ Y tế) sang Chủ tịch UBND cấp tỉnh (Huy Vũ, 2026).',
])
c += P('Các mức phạt trên áp dụng với cá nhân; tổ chức bị phạt gấp đôi (Chính phủ, 2026, Điều 6 khoản 3). Về các lỗi khác khi quảng cáo thực phẩm chức năng, xem bài ' + A('quang-cao-thuc-pham-bao-ve-suc-khoe-loi-thuong-gap', 'quảng cáo thực phẩm bảo vệ sức khỏe: lỗi thường gặp') + '.')

c += H2('Khi thấy "đạt chuẩn FDA", hãy hỏi')
c += UL([
    'FDA phê duyệt cái gì: sản phẩm, một thành phần, hay chỉ là cơ sở đã đăng ký?',
    'Sản phẩm thuộc nhóm nào? Nếu là thực phẩm chức năng hay mỹ phẩm, FDA không phê duyệt nhóm này.',
    '"Giấy chứng nhận" do ai phát hành? FDA không cấp giấy chứng nhận đăng ký cơ sở thực phẩm.',
    'Sản phẩm đã có giấy phép lưu hành và giấy xác nhận nội dung quảng cáo của cơ quan Việt Nam chưa?',
])
c += P('Danh sách do người viết tổng hợp từ các nguồn trong bài.')

c += H2('Câu hỏi thường gặp')
c += H3('FDA có cấp phép thực phẩm chức năng không?')
c += P('Không. Theo luật Mỹ, FDA không phê duyệt thực phẩm chức năng về độ an toàn và hiệu quả (FDA, 2026).')
c += H3('"FDA registered" có nghĩa là gì?')
c += P('Thường chỉ có nghĩa là cơ sở đã đăng ký với FDA. Theo FDA (2026), việc đăng ký không đồng nghĩa với việc cơ sở hay sản phẩm được phê duyệt.')
c += H3('Sản phẩm có "giấy chứng nhận FDA" có đáng tin hơn không?')
c += P('Không nên dựa vào giấy này. FDA không cấp giấy chứng nhận đăng ký cho cơ sở thực phẩm và không công nhận giấy do bên tư nhân phát hành (FDA, 2024).')

c += H2('Điều gì nên nhớ?')
c += P('"Đạt chuẩn FDA" nghe như một con dấu bảo đảm, nhưng với thực phẩm chức năng, FDA không phê duyệt sản phẩm, không cấp giấy chứng nhận đăng ký, và việc đăng ký cơ sở không đồng nghĩa với phê duyệt. Với sản phẩm bán ở Việt Nam, điều đáng kiểm tra là giấy tờ do cơ quan Việt Nam cấp.')
c += GEN_END + REFS([ND87, LSVN, FDA2, FDA1])

d = dict(slug='dat-chuan-fda-fda-co-cap-phep-thuc-pham-chuc-nang-khong', title='"Đạt chuẩn FDA": FDA có cấp phép thực phẩm chức năng không?',
    seo_title='FDA có cấp phép thực phẩm chức năng không?',
    meta_desc='FDA không phê duyệt thực phẩm chức năng và không cấp giấy chứng nhận đăng ký cơ sở thực phẩm. "Đạt chuẩn FDA" nghĩa là gì, và ở Việt Nam nên kiểm tra gì?',
    focus_kw='FDA có cấp phép thực phẩm chức năng',
    excerpt='"Đạt chuẩn FDA", "giấy chứng nhận FDA" xuất hiện nhiều trong quảng cáo thực phẩm chức năng. FDA thực sự phê duyệt gì, và ở Việt Nam nên kiểm tra giấy tờ nào?',
    tags=['đạt chuẩn FDA', 'thực phẩm chức năng', 'giấy chứng nhận FDA', 'quảng cáo sức khỏe', 'bóc mác y khoa'], content=c, categories=[3, 11],
    date='2026-11-15T16:00:00', cover_alt='Minh họa con dấu quảng cáo "Đạt chuẩn FDA" bị bút đỏ gạch chéo, kèm ghi chú "FDA cấp cho điều gì?"')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

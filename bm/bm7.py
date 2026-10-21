import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'


FTC = 'Federal Trade Commission. (2010, ngày 15 tháng 12). <em>Dannon agrees to drop exaggerated health claims for Activia yogurt and DanActive dairy drink</em> [Thông cáo báo chí]. https://www.ftc.gov/news-events/news/press-releases/2010/12/dannon-agrees-drop-exaggerated-health-claims-activia-yogurt-danactive-dairy-drink'
DR = 'Starling, S. (2010, ngày 16 tháng 12). Dannon on FTC settlement: "Our claims remain intact". <em>DairyReporter</em>. https://www.dairyreporter.com/Article/2010/12/16/Dannon-on-FTC-settlement-Our-claims-remain-intact/'
FTCG = 'Federal Trade Commission. (2022). <em>Health products compliance guidance</em>. https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance'
ND87 = 'Chính phủ. (2026). <em>Nghị định số 87/2026/NĐ-CP quy định xử phạt vi phạm hành chính trong lĩnh vực văn hóa và quảng cáo</em>. Công báo điện tử Chính phủ. https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-87-2026-nd-cp-469359.htm'

c = ''
c += P('Năm 2010, Ủy ban Thương mại Liên bang Mỹ (FTC) cáo buộc hãng Dannon quảng cáo phóng đại lợi ích sức khỏe của sữa chua Activia và đồ uống sữa DanActive: Activia "đã được chứng minh lâm sàng" giúp điều hòa tiêu hóa, còn DanActive giúp "tăng cường sức đề kháng", phòng cảm lạnh và cúm. Theo FTC, Dannon không có đủ căn cứ cho các tuyên bố này, và việc nói chúng "đã được chứng minh lâm sàng" là sai. Dannon đồng ý dàn xếp với FTC và trả 21 triệu USD cho 39 bang để kết thúc các cuộc điều tra riêng của bang (Federal Trade Commission [FTC], 2010).')
c += P('Đây là bài thứ bảy trong chuyên đề "Bóc mác y khoa trong quảng cáo", mở đầu nhóm bài "Khi cơ quan quản lý vào cuộc".')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'FTC cáo buộc Dannon không có căn cứ cho tuyên bố Activia điều hòa tiêu hóa và DanActive giúp phòng cảm lạnh, cúm.',
    'FTC cho rằng tuyên bố "đã được chứng minh lâm sàng" của hai sản phẩm là sai.',
    'Theo dàn xếp, Activia chỉ được quảng cáo lợi ích tiêu hóa nếu nói rõ cần ăn ba hộp mỗi ngày, trừ khi có hai nghiên cứu tốt cho liều thấp hơn.',
    'Dàn xếp không phải là thừa nhận vi phạm; theo DairyReporter, Dannon khẳng định chưa từng đưa ra tuyên bố phòng cảm lạnh, cúm.',
])

c += H2('Quảng cáo đã nói gì?')
c += P('Theo thông cáo của FTC (2010), các chiến dịch quảng cáo trên truyền hình, internet, báo in và bao bì của Dannon nói rằng:')
c += UL([
    '<strong>Activia:</strong> mỗi ngày một hộp giúp giảm tình trạng tiêu hóa thất thường tạm thời và hỗ trợ khi "thời gian vận chuyển trong ruột chậm".',
    '<strong>DanActive:</strong> giúp phòng cảm lạnh và cúm.',
    'Có bằng chứng khoa học cho các tuyên bố trên.',
])
c += P('Một quảng cáo truyền hình của Activia kết thúc bằng câu: Activia ăn hằng ngày "đã được chứng minh lâm sàng giúp điều hòa hệ tiêu hóa của bạn trong hai tuần". Quảng cáo DanActive cho thấy hình ảnh lợi khuẩn L. casei Immunitas "bịt lỗ" trên thành ruột, kèm lời thoại sản phẩm "đã được chứng minh lâm sàng giúp tăng cường khả năng phòng vệ của cơ thể" (FTC, 2010).')

c += H2('FTC cáo buộc điều gì?')
c += P('FTC cho rằng quảng cáo của Dannon là lừa dối vì công ty không có căn cứ cho các tuyên bố, và tuyên bố "đã được chứng minh lâm sàng" là sai. Chủ tịch FTC khi đó, Jon Leibowitz, nhận định các công ty như Dannon không nên phóng đại mức độ ủng hộ khoa học cho sản phẩm của mình (FTC, 2010).')
c += P('Cần lưu ý, FTC cũng ghi rõ: việc ban hành cáo buộc không phải là kết luận rằng công ty đã vi phạm pháp luật, và thỏa thuận dàn xếp không đồng nghĩa với việc công ty thừa nhận vi phạm (FTC, 2010).')

c += H2('Dàn xếp yêu cầu những gì?')
c += P('Theo FTC (2010), thỏa thuận dàn xếp quy định:')
c += UL([
    'Dannon không được nói bất kỳ sữa chua, đồ uống sữa hay thực phẩm probiotic nào giúp giảm khả năng mắc cảm lạnh, cúm, trừ khi tuyên bố được Cục Quản lý Thực phẩm và Dược phẩm Mỹ (FDA) chấp thuận.',
    'Dannon chỉ được nói Activia giúp giảm tình trạng tiêu hóa thất thường nếu quảng cáo nêu rõ cần ăn ba hộp mỗi ngày để có lợi ích này. Muốn nói ít hơn ba hộp vẫn có lợi, công ty phải dựa trên hai nghiên cứu lâm sàng được thiết kế tốt trên người.',
    'Với mọi tuyên bố sức khỏe khác, Dannon phải có bằng chứng khoa học đáng tin cậy, và không được trình bày sai kết quả nghiên cứu.',
])
c += P('Song song, 39 tổng chưởng lý bang công bố kết thúc điều tra riêng, và Dannon đồng ý trả cho các bang 21 triệu USD (FTC, 2010).')

c += H2('Phía Dannon nói gì?')
c += P('Theo DairyReporter, người phát ngôn của Dannon cho biết công ty tiếp tục tiếp thị sản phẩm "như bình thường" sau ba lần xem xét. Dannon khẳng định chưa từng đưa ra tuyên bố về phòng cảm lạnh và cúm, và có thể sẽ dùng tuyên bố có kèm điều kiện ba hộp mỗi ngày cho Activia (Starling, 2010).')

c += H2('Bài học cho người đọc quảng cáo')
c += P('Vụ việc minh họa ba điểm mà các bài trước trong chuyên đề đã nêu:')
c += UL([
    '<strong>Liều lượng quan trọng:</strong> lợi ích tiêu hóa gắn với ba hộp mỗi ngày, không phải một hộp như quảng cáo ban đầu ngụ ý (FTC, 2010).',
    '<strong>"Chứng minh lâm sàng" phải đúng với sản phẩm và tuyên bố:</strong> hướng dẫn của FTC yêu cầu nhà quảng cáo có ít nhất mức bằng chứng họ tuyên bố (FTC, 2022). Xem thêm bài ' + A('da-chung-minh-lam-sang-nghia-la-gi', '"đã chứng minh lâm sàng" có đáng tin không') + '.',
    '<strong>Hình ảnh cũng là tuyên bố:</strong> hình lợi khuẩn "bịt lỗ" trên thành ruột hay chiếc khiên bảo vệ quanh đứa trẻ truyền tải thông điệp sức khỏe mà không cần nói thẳng (FTC, 2010).',
])
c += P('Vụ việc không kết luận rằng probiotic vô dụng. Điều FTC xem xét là liệu những tuyên bố cụ thể trong quảng cáo có đủ căn cứ hay không. Đoạn này là nhận định của người viết.')

c += H2('Ở Việt Nam, quy định thế nào?')
c += P('Nghị định 87/2026/NĐ-CP phạt từ 30 đến 40 triệu đồng đối với quảng cáo sản phẩm không phải là thuốc (trừ thiết bị y tế) có nội dung dùng để phòng bệnh, chữa bệnh hoặc điều chỉnh chức năng sinh lý cơ thể người (Chính phủ, 2026, Điều 69 khoản 4). Một tuyên bố như "giúp phòng cảm lạnh, cúm" cho sản phẩm thực phẩm có thể rơi vào hành vi này. Tổ chức bị phạt gấp đôi mức trên (Chính phủ, 2026, Điều 6 khoản 3).')

c += H2('Câu hỏi thường gặp')
c += H3('Activia có bị cấm bán không?')
c += P('Không. Dàn xếp chỉ giới hạn cách Dannon quảng cáo lợi ích sức khỏe (FTC, 2010).')
c += H3('Sữa chua probiotic có tăng miễn dịch không?')
c += P('Bài này không đánh giá tác dụng chung của probiotic. Vụ Activia chỉ cho thấy FTC cho rằng Dannon chưa có đủ căn cứ cho tuyên bố DanActive giúp phòng cảm lạnh, cúm (FTC, 2010).')
c += H3('21 triệu USD được trả cho ai?')
c += P('Cho 39 bang của Mỹ, để kết thúc các cuộc điều tra riêng của bang về quảng cáo DanActive và Activia (FTC, 2010).')

c += H2('Điều gì nên nhớ?')
c += P('Một sản phẩm quen thuộc, một gương mặt nổi tiếng và cụm từ "đã được chứng minh lâm sàng" có thể tạo cảm giác chắc chắn. Vụ Activia cho thấy cần hỏi thêm: chứng minh cho lợi ích nào, với liều bao nhiêu, và bằng chứng có thật sự đủ hay không.')
c += GEN_END + REFS([ND87, FTC, FTCG, DR])

d = dict(slug='sua-chua-tang-mien-dich-vu-activia-ftc', title='Sữa chua "tăng miễn dịch": bài học từ vụ Activia và FTC',
    seo_title='Sữa chua "tăng miễn dịch": bài học từ vụ Activia',
    meta_desc='Năm 2010, FTC cáo buộc Dannon phóng đại lợi ích của Activia và DanActive. Dannon dàn xếp và trả 21 triệu USD cho 39 bang. Bài học về quảng cáo sức khỏe.',
    focus_kw='sữa chua tăng miễn dịch',
    excerpt='Vụ Activia và DanActive: FTC cho rằng tuyên bố "đã chứng minh lâm sàng" là sai. Dàn xếp yêu cầu gì, phía Dannon nói gì, và bài học cho người đọc quảng cáo.',
    tags=['sữa chua tăng miễn dịch', 'Activia', 'probiotic', 'FTC', 'bóc mác y khoa'], content=c, categories=[3, 11],
    date='2026-11-18T16:00:00', cover_alt='Minh họa mẩu quảng cáo "Sữa chua tăng miễn dịch" bị bút đỏ ghi chú "Bằng chứng ở đâu?"')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

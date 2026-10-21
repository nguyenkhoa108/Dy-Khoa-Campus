import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'


OC = 'Osborne Clarke. (2007, ngày 31 tháng 1). <em>Colgate\'s "80% of dentists recommend" claim under fire</em>. Marketing Law. https://marketinglaw.osborneclarke.com/retailing/colgates-80-of-dentists-recommend-claim-under-fire/'
CB = 'Cosmetics Business. (2007, ngày 17 tháng 1). <em>ASA don\'t recommend Colgate</em>. https://www.cosmeticsbusiness.com/asa-don-t-recommend-colgate-47191'
ND87 = 'Chính phủ. (2026). <em>Nghị định số 87/2026/NĐ-CP quy định xử phạt vi phạm hành chính trong lĩnh vực văn hóa và quảng cáo</em>. Công báo điện tử Chính phủ. https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-87-2026-nd-cp-469359.htm'
LSVN = 'Minh Trần. (2025, ngày 20 tháng 4). Bác sĩ, dược sĩ, nhân viên y tế không được tham gia quảng cáo thực phẩm, thực phẩm chức năng. <em>Luật sư Việt Nam</em>. https://lsvn.vn/bac-si-duoc-si-nhan-vien-y-te-khong-duoc-tham-gia-quang-cao-thuc-pham-thuc-pham-chuc-nang-a156624.html'

c = ''
c += P('"9/10 nha sĩ khuyên dùng" nghe như kết quả một nghiên cứu, nhưng con số này có thể đúng về mặt số học mà vẫn gây hiểu lầm. Năm 2007, Cơ quan Tiêu chuẩn Quảng cáo Anh (ASA) kết luận quảng cáo "hơn 80% nha sĩ khuyên dùng Colgate" là gây hiểu lầm: trong khảo sát, nha sĩ được nêu nhiều nhãn hiệu cùng lúc, và một nhãn hiệu đối thủ cũng được khuyên dùng gần như ngang bằng (Osborne Clarke, 2007).')
c += P('Đây là bài thứ hai trong chuyên đề "Bóc mác y khoa trong quảng cáo". Bài trước bóc con số ' + A('di-bo-10000-buoc-moi-ngay-co-can-thiet', '10.000 bước mỗi ngày') + '.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Câu hỏi khảo sát quyết định ý nghĩa của con số: "khuyên dùng" không đồng nghĩa với "chọn nhãn này thay vì nhãn khác".',
    'Trong vụ Colgate, nha sĩ có thể khuyên nhiều nhãn hiệu, nên con số 80% không cho biết họ ưu tiên nhãn nào.',
    'ASA còn kết luận quảng cáo ngụ ý sự chứng thực của giới chuyên môn mà không có sự đồng ý của người được hỏi.',
    'Ở Việt Nam, dùng hình ảnh, danh nghĩa nhân viên y tế để quảng cáo thực phẩm, thuốc bị cấm hoặc bị xử phạt.',
])

c += H2('Vụ Colgate: chuyện gì đã xảy ra?')
c += P('Chiến dịch áp phích của Colgate tại Anh có dòng tiêu đề "Hơn 80% nha sĩ khuyên dùng Colgate". Sau khiếu nại, ASA xem xét khảo sát làm cơ sở cho con số này (Osborne Clarke, 2007):')
c += UL([
    'Khảo sát được thực hiện qua điện thoại.',
    'Nha sĩ được đề nghị khuyên dùng nhiều loại kem đánh răng và nhãn hiệu, không chỉ chọn một.',
    'Một nhãn hiệu đối thủ được nha sĩ khuyên dùng gần như ngang với Colgate.',
])
c += P('ASA kết luận câu quảng cáo khiến người đọc hiểu rằng 80% nha sĩ ưu tiên Colgate hơn các nhãn khác, còn 20% còn lại thích nhãn khác. Đây không phải điều khảo sát đã đo (Cosmetics Business, 2007; Osborne Clarke, 2007). Colgate được yêu cầu không lặp lại tuyên bố này.')

c += H2('Những vấn đề khác ASA chỉ ra')
c += P('Ngoài con số, ASA còn tự nêu thêm một vấn đề: quảng cáo ngụ ý sự chứng thực của giới chuyên môn. Theo Osborne Clarke (2007), kịch bản khảo sát không cho người được hỏi biết Colgate là bên đặt hàng nghiên cứu, hay kết quả có thể được dùng để quảng cáo, và nhãn hàng cũng không có sự cho phép bằng văn bản của họ cho việc chứng thực như vậy.')
c += P('Bốn loại kem đánh răng Colgate có trong khảo sát là thuốc được cấp phép tại Anh, nhóm sản phẩm không được dùng sự chứng thực của nhân viên y tế để quảng cáo. ASA kết luận quảng cáo vi phạm các điều khoản về chứng minh, tính trung thực, lời chứng thực và chứng thực thuốc trong bộ quy tắc quảng cáo của Anh (Osborne Clarke, 2007).')

c += H2('Vì sao "X/10 chuyên gia khuyên dùng" dễ gây hiểu lầm?')
c += P('Từ vụ việc trên, người viết rút ra ba câu hỏi khi gặp một con số kiểu "chuyên gia khuyên dùng":')
c += TABLE(['Câu hỏi', 'Vì sao quan trọng', 'Trong vụ Colgate'], [
    ['Hỏi thế nào?', 'Cho phép chọn nhiều đáp án thì con số không cho biết thứ tự ưu tiên', 'Nha sĩ được nêu nhiều nhãn hiệu'],
    ['So với ai?', 'Một con số không có đối chứng không cho biết sản phẩm nổi bật hơn hay không', 'Đối thủ được khuyên dùng gần như ngang bằng'],
    ['Ai hỏi, người được hỏi có biết không?', 'Người trả lời có thể không biết câu trả lời sẽ thành lời chứng thực', 'Kịch bản không nói rõ nhãn hàng đặt hàng khảo sát'],
])
c += P('Bảng do người viết tổng hợp, dựa trên các vấn đề ASA nêu (Osborne Clarke, 2007).')

c += H2('Ở Việt Nam, quy định thế nào?')
c += P('Một số quy định Việt Nam liên quan trực tiếp đến kiểu thông điệp này:')
c += UL([
    '<strong>Từ ngữ so sánh nhất:</strong> quảng cáo dùng các từ "nhất", "duy nhất", "tốt nhất", "số một" hoặc từ ngữ tương tự mà không có tài liệu hợp pháp chứng minh bị phạt từ 10 đến 20 triệu đồng (Chính phủ, 2026, Điều 50 khoản 2).',
    '<strong>Quảng cáo thuốc:</strong> lợi dụng danh nghĩa, hình ảnh, uy tín của tổ chức, cá nhân hoặc thư cảm ơn của người bệnh để quảng cáo thuốc bị phạt từ 30 đến 40 triệu đồng (Chính phủ, 2026, Điều 69 khoản 4).',
    '<strong>Quảng cáo thực phẩm:</strong> theo Nghị định 15/2018/NĐ-CP, quảng cáo thực phẩm không được dùng hình ảnh, trang phục, tên của cơ sở y tế, bác sĩ, dược sĩ, nhân viên y tế (Minh Trần, 2025).',
])
c += P('Các mức phạt trên áp dụng với cá nhân; tổ chức bị phạt gấp đôi (Chính phủ, 2026, Điều 6 khoản 3). Về các lỗi khác khi quảng cáo thực phẩm chức năng, xem bài ' + A('quang-cao-thuc-pham-bao-ve-suc-khoe-loi-thuong-gap', 'quảng cáo thực phẩm bảo vệ sức khỏe: lỗi thường gặp') + '.')

c += H2('Câu hỏi thường gặp')
c += H3('"Nha sĩ khuyên dùng" có phải là nói dối?')
c += P('Không nhất thiết. Trong vụ Colgate, con số có thể có cơ sở từ khảo sát, nhưng cách trình bày khiến người đọc hiểu sai điều khảo sát đã đo. Đó là lý do ASA kết luận quảng cáo gây hiểu lầm (Osborne Clarke, 2007).')
c += H3('Làm sao kiểm tra một tuyên bố "chuyên gia khuyên dùng"?')
c += P('Hãy tìm xem ai thực hiện khảo sát, hỏi bao nhiêu người, câu hỏi là gì, có được chọn nhiều đáp án không, và các nhãn khác được khuyên dùng bao nhiêu. Nếu quảng cáo không công bố những thông tin này, con số chưa đủ để kết luận.')
c += H3('Ở Việt Nam có được quảng cáo "bác sĩ khuyên dùng" không?')
c += P('Với thực phẩm, quảng cáo không được dùng hình ảnh, tên của bác sĩ, dược sĩ, nhân viên y tế (Minh Trần, 2025). Với thuốc, việc lợi dụng danh nghĩa, uy tín của tổ chức, cá nhân để quảng cáo bị xử phạt (Chính phủ, 2026, Điều 69 khoản 4).')

c += H2('Điều gì nên nhớ?')
c += P('Một con số có thể đúng mà vẫn gây hiểu lầm. Với các tuyên bố "X/10 chuyên gia khuyên dùng", điều cần hỏi không phải là con số lớn đến đâu, mà là ai hỏi, hỏi thế nào, và các lựa chọn khác được khuyên dùng bao nhiêu.')
c += GEN_END + REFS([ND87, CB, LSVN, OC])

d = dict(slug='9-10-nha-si-khuyen-dung-khao-sat-gay-hieu-lam', title='"9/10 nha sĩ khuyên dùng": con số khảo sát bị bẻ cong thế nào?',
    seo_title='"Nha sĩ khuyên dùng": con số khảo sát gây hiểu lầm',
    meta_desc='"80% nha sĩ khuyên dùng" từng bị cơ quan quảng cáo Anh kết luận gây hiểu lầm vì nha sĩ được chọn nhiều nhãn. Cách đọc các tuyên bố "chuyên gia khuyên dùng".',
    focus_kw='nha sĩ khuyên dùng',
    excerpt='Vụ Colgate tại Anh cho thấy con số "chuyên gia khuyên dùng" có thể đúng mà vẫn gây hiểu lầm. Ba câu hỏi để đọc kiểu thông điệp này, và quy định tại Việt Nam.',
    tags=['nha sĩ khuyên dùng', 'chuyên gia khuyên dùng', 'quảng cáo gây hiểu lầm', 'quảng cáo sức khỏe', 'bóc mác y khoa'], content=c, categories=[3, 11],
    date='2026-11-13T16:00:00', cover_alt='Minh họa phiếu quảng cáo "9/10 nha sĩ khuyên dùng" bị bút đỏ khoanh và ghi chú "Hỏi ai? Hỏi thế nào?"')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

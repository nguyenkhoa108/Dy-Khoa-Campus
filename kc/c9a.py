import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'

WHO = 'World Health Organization. (2025, ngày 21 tháng 8). <em>Dengue and severe dengue</em> [Tờ thông tin]. https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue'
AN = 'Andersson, N., Nava-Aguilera, E., Arosteguí, J., Morales-Perez, A., Suazo-Laguna, H., Legorreta-Soberanis, J., Hernandez-Alvarez, C., Fernandez-Salas, I., Paredes-Solís, S., Balmaseda, A., Cortés-Guzmán, A. J., Serrano de los Santos, R., Coloma, J., Ledogar, R. J., &amp; Harris, E. (2015). Evidence based community mobilization for dengue prevention in Nicaragua and Mexico (Camino Verde, the Green Way): Cluster randomized controlled trial. <em>BMJ, 351</em>, h3267. https://doi.org/10.1136/bmj.h3267'
TB = 'Thời báo Tài chính Việt Nam. (2025, ngày 1 tháng 9). <em>Cả nước ghi nhận hơn 21.600 ca mắc sốt xuất huyết trong tháng 8</em>. https://thoibaotaichinhvietnam.vn/ca-nuoc-ghi-nhan-hon-21600-ca-mac-sot-xuat-huyet-trong-thang-8-182434.html'
BD = 'Ủy ban nhân dân xã Ba Dinh. (2026). <em>Về việc tăng cường công tác phòng, chống sốt xuất huyết</em> [Công văn]. https://badinh.quangngai.gov.vn/upload/2007048/20260825/CV%20t%C4%83ng%20c%C6%B0%E1%BB%9Dng%20c%C3%B4ng%20t%C3%A1c%20Ph%C3%B2ng%20ch%E1%BB%91ng%20s%E1%BB%91t%20xu%E1%BA%A5t%20huy%E1%BA%BFt.pdf'

c = ''
c += P('Cách hiệu quả nhất để phòng sốt xuất huyết là không cho muỗi có chỗ đẻ trứng: mỗi tuần đậy kín, đổ bỏ hoặc cọ rửa các dụng cụ chứa nước trong và quanh nhà. Tổ chức Y tế Thế giới (WHO) khẳng định việc phòng và kiểm soát sốt xuất huyết dựa vào kiểm soát muỗi truyền bệnh, và khuyến nghị che đậy, đổ bỏ, làm sạch các dụng cụ chứa nước sinh hoạt hằng tuần (World Health Organization [WHO], 2025).')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Sốt xuất huyết lây qua muỗi vằn <em>Aedes aegypti</em>, loài muỗi đốt vào ban ngày (WHO, 2025).',
    'Thế giới ghi nhận 14,6 triệu ca năm 2024, tăng từ khoảng 505.000 ca năm 2000 (WHO, 2025).',
    'Lăng quăng (bọ gậy) là ấu trùng muỗi, sống trong nước đọng ở các vật chứa nước quanh nhà.',
    'Một thử nghiệm lớn cho thấy cộng đồng cùng diệt lăng quăng giúp giảm 29,5% nguy cơ nhiễm sốt xuất huyết (Andersson và cộng sự, 2015).',
    'Khi bị sốt xuất huyết, chỉ hạ sốt bằng paracetamol, không dùng ibuprofen hay aspirin (WHO, 2025).',
])

c += H2('Vì sao phải diệt lăng quăng?')
c += P('Muỗi truyền sốt xuất huyết chủ yếu là <em>Aedes aegypti</em>. Loài muỗi này hoạt động vào ban ngày, và WHO khuyến nghị ngăn muỗi sinh sản bằng cách loại bỏ các nơi chứa nước nhân tạo quanh nhà (WHO, 2025). Lăng quăng là giai đoạn ấu trùng của muỗi, sống trong nước. Diệt lăng quăng là chặn muỗi từ trước khi chúng trưởng thành và đốt người.')
c += P('Sốt xuất huyết đang tăng mạnh trên thế giới: số ca được báo cáo tăng từ 505.430 ca năm 2000 lên 14,6 triệu ca năm 2024, với hơn 12.000 ca tử vong trong năm 2024 (WHO, 2025). Ở Việt Nam, từ 14/12/2024 đến cuối tháng 8/2025, cả nước ghi nhận 65.101 ca mắc và 11 ca tử vong, số ca mắc cao hơn 20,8% so với cùng kỳ năm trước (Thời báo Tài chính Việt Nam, 2025).')

c += H2('Diệt lăng quăng có thật sự hiệu quả?')
c += P('Có bằng chứng mạnh. Thử nghiệm ngẫu nhiên có đối chứng theo cụm Camino Verde tại Nicaragua và Mexico, với 150 cụm dân cư gồm 85.182 người, so sánh các khu vực có huy động cộng đồng diệt lăng quăng với các khu vực đối chứng. Kết quả ở khu vực can thiệp (Andersson và cộng sự, 2015):')
c += UL([
    'Nguy cơ nhiễm sốt xuất huyết (xác định bằng xét nghiệm máu) giảm 29,5%.',
    'Số người tự báo cáo bị sốt xuất huyết giảm 24,7%.',
    'Tỉ lệ nhà có lăng quăng hoặc bọ gậy giảm 44,1%.',
    'Số nhộng muỗi trên mỗi người giảm 51,7%.',
])
c += P('Nhóm nghiên cứu kết luận việc huy động cộng đồng dựa trên bằng chứng có thể làm tăng hiệu quả kiểm soát muỗi truyền bệnh (Andersson và cộng sự, 2015). Nói cách khác, cả khu dân cư cùng làm sẽ hiệu quả hơn từng hộ làm riêng lẻ.')

c += H2('Lăng quăng thường ở đâu trong nhà?')
c += P('Theo hướng dẫn của địa phương triển khai chỉ đạo ngành y tế, cần chú ý các nơi sau (Ủy ban nhân dân xã Ba Dinh, 2026):')
c += UL([
    'Lu, khạp, bể, thùng chứa nước sinh hoạt không có nắp đậy.',
    'Bình hoa, chậu cây thủy sinh, khay nước dưới chậu cây.',
    'Vật phế thải đọng nước mưa: chai lọ, gáo dừa, chum vỡ, lốp xe cũ, hốc tre.',
    'Các vật chứa nước không sử dụng nhưng để ngửa.',
])

c += H2('Cách diệt lăng quăng tại nhà')
c += P('Các biện pháp dưới đây tổng hợp từ khuyến nghị của WHO (2025) và hướng dẫn của địa phương (Ủy ban nhân dân xã Ba Dinh, 2026). WHO (2025) khuyến nghị làm việc này hằng tuần.')
c += UL([
    '<strong>Đậy kín</strong> tất cả dụng cụ chứa nước để muỗi không vào đẻ trứng.',
    '<strong>Cọ rửa</strong> các dụng cụ chứa nước nhỏ và vừa hằng tuần; lật úp những vật chứa nước không dùng đến.',
    '<strong>Thay nước</strong> bình hoa, chậu cây thủy sinh ít nhất mỗi tuần một lần.',
    '<strong>Thả cá</strong> ăn lăng quăng vào các bể chứa nước lớn.',
    '<strong>Thu gom, loại bỏ</strong> vật phế thải và các hốc đọng nước tự nhiên quanh nhà.',
])
c += P('Sau mưa bão, lượng vật chứa nước đọng thường tăng. Bài ' + A('xu-ly-nuoc-sinh-hoat-sau-lu', 'xử lý nước sinh hoạt sau lũ') + ' có thêm lưu ý về vệ sinh nguồn nước.')

c += H2('Phòng muỗi đốt thế nào?')
c += P('Diệt lăng quăng cần kết hợp với tránh muỗi đốt, nhất là vào ban ngày (WHO, 2025):')
c += UL([
    'Mặc quần áo che kín càng nhiều phần cơ thể càng tốt.',
    'Dùng lưới chống muỗi ở cửa sổ và ngủ màn, kể cả khi ngủ ngày.',
    'Dùng thuốc xua muỗi có chứa DEET, Picaridin hoặc IR3535.',
])

c += H2('Khi nào cần đi khám ngay?')
c += P('Triệu chứng thường xuất hiện 4 đến 10 ngày sau khi bị muỗi đốt và kéo dài 2 đến 7 ngày, gồm sốt cao, đau đầu dữ dội, đau sau hốc mắt, đau cơ khớp, buồn nôn, nôn, nổi hạch, phát ban (WHO, 2025). Khi nghi ngờ sốt xuất huyết, nên đến cơ sở y tế gần nhất, không tự điều trị tại nhà (Ủy ban nhân dân xã Ba Dinh, 2026).')
c += P('Đặc biệt lưu ý: các dấu hiệu nặng thường xuất hiện <strong>sau khi hết sốt</strong>. Cần đi cấp cứu ngay nếu có (WHO, 2025):')
c += UL([
    'Đau bụng dữ dội.',
    'Nôn liên tục.',
    'Thở nhanh.',
    'Chảy máu chân răng hoặc chảy máu mũi.',
    'Nôn ra máu hoặc đi ngoài ra máu.',
])
c += P('Hiện chưa có thuốc điều trị đặc hiệu sốt xuất huyết. Có thể giảm đau, hạ sốt bằng paracetamol; không dùng các thuốc kháng viêm không steroid như ibuprofen và aspirin vì có thể làm tăng nguy cơ chảy máu (WHO, 2025). Bài ' + A('sot-xuat-huyet-lan-2-co-nang-hon-khong', 'sốt xuất huyết lần 2 có nặng hơn không') + ' giải thích thêm về nguy cơ khi mắc lại.')

c += H2('Câu hỏi thường gặp')
c += H3('Phun thuốc diệt muỗi có thay được việc diệt lăng quăng không?')
c += P('Không. Phun thuốc diệt muỗi trưởng thành, còn lăng quăng trong nước vẫn tiếp tục phát triển thành muỗi mới. WHO (2025) xem việc loại bỏ nơi muỗi sinh sản là biện pháp nền tảng.')
c += H3('Đã có vắc xin sốt xuất huyết chưa?')
c += P('Có. Vắc xin QDenga đã được cấp phép ở một số quốc gia. WHO khuyến nghị dùng cho trẻ từ 6 đến 16 tuổi ở những nơi lây truyền cao (WHO, 2025). Hãy hỏi bác sĩ về việc tiêm vắc xin phù hợp.')
c += H3('Muỗi sốt xuất huyết đốt vào lúc nào?')
c += P('Muỗi truyền sốt xuất huyết hoạt động vào ban ngày (WHO, 2025), nên cần ngủ màn cả khi ngủ trưa, nhất là với trẻ nhỏ.')

c += H2('Điều gì nên nhớ?')
c += P('Không có lăng quăng thì không có muỗi truyền bệnh. Mỗi tuần dành một ít thời gian đậy kín, cọ rửa, thay nước và dọn vật đọng nước quanh nhà, đồng thời rủ hàng xóm cùng làm. Khi bị sốt, đi khám sớm, chỉ dùng paracetamol, và theo dõi kỹ các dấu hiệu nặng sau khi hết sốt.')
c += P('<em>Bài viết mang tính thông tin, không thay thế tư vấn y khoa cho từng cá nhân.</em>')
c += GEN_END + REFS([AN, TB, BD, WHO])

d = dict(slug='diet-lang-quang-phong-sot-xuat-huyet', title='Diệt lăng quăng phòng sốt xuất huyết: làm gì mỗi tuần để có hiệu quả?',
    seo_title='Diệt lăng quăng phòng sốt xuất huyết: cách làm hiệu quả',
    meta_desc='Diệt lăng quăng là cách phòng sốt xuất huyết hiệu quả nhất. Lăng quăng ở đâu, cách diệt mỗi tuần, phòng muỗi đốt và dấu hiệu nặng cần đi khám ngay.',
    focus_kw='diệt lăng quăng',
    excerpt='Cộng đồng cùng diệt lăng quăng giúp giảm gần 30% nguy cơ nhiễm sốt xuất huyết. Lăng quăng hay ở đâu, cách diệt mỗi tuần và dấu hiệu nặng cần đi khám.',
    tags=['sốt xuất huyết', 'diệt lăng quăng', 'phòng bệnh', 'muỗi vằn', 'sức khỏe cộng đồng'], content=c, categories=[4, 11],
    date='2026-11-04T08:00:00', cover_alt='Minh họa lu nước được đậy nắp, chậu cây được úp ngược và con muỗi vằn bị gạch chéo, tượng trưng cho diệt lăng quăng phòng sốt xuất huyết')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

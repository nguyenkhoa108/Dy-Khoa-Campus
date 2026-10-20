import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'
GL = lambda s, t: f'<a href="https://dykhoa.com/blog/thuat-ngu/{s}/">{t}</a>'

CF = 'Coleman, E., &amp; Ford, J. V. (2024). A brief history of sexology and lessons learned. <em>The Journal of Sexual Medicine, 21</em>(10), 835-838. https://doi.org/10.1093/jsxmed/qdae081 (bản mở: https://pmc.ncbi.nlm.nih.gov/articles/PMC11442977/)'
KI = 'Kinsey Institute. (n.d.). <em>Learn our history</em>. Indiana University. https://kinseyinstitute.org/about/history/index.php'
IU = 'Schmid, A. (2020, ngày 11 tháng 5). <em>History of medicine book of the week: Psychopathia sexualis</em>. Indiana University School of Medicine Library. https://medicine.iu.edu/blogs/medical-library/2020/History-of-Medicine-Book-of-the-Week-Psychopathia-Sexualis'
WAS = 'World Association for Sexual Health. (n.d.). <em>History</em>. https://worldsexualhealth.net/organization/history/'
WHO = 'World Health Organization. (n.d.). <em>Defining sexual health</em>. https://www.who.int/teams/sexual-and-reproductive-health-and-research/key-areas-of-work/sexual-health/defining-sexual-health'

c = ''
c += P('Tình dục học (sexology) là lĩnh vực nghiên cứu tình dục con người một cách khoa học và liên ngành (Coleman &amp; Ford, 2024). Ngành này kết hợp y học, tâm lý học, xã hội học và nhiều ngành khác để tìm hiểu hành vi, chức năng, các mối quan hệ, sự đa dạng tình dục và sức khỏe tình dục. Tình dục học hình thành ở Đức đầu thế kỷ 20, bị đứt gãy dưới thời Đức Quốc xã, rồi hồi sinh ở Mỹ nhờ các nghiên cứu tiên phong của Alfred Kinsey (Coleman &amp; Ford, 2024).')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Thuật ngữ "Sexualwissenschaft" (tình dục học) do Iwan Bloch đặt ra; viện nghiên cứu tình dục học đầu tiên ra đời tại Berlin năm 1919 (Coleman &amp; Ford, 2024).',
    'Ngay từ đầu, tình dục học khác y học truyền thống ở chỗ tìm hiểu sự bình thường và lành mạnh của các dạng biểu hiện tình dục đa dạng, thay vì chỉ nhìn qua lăng kính bệnh lý.',
    'Viện Kinsey (Mỹ) được thành lập năm 1947; hai báo cáo Kinsey công bố năm 1948 và 1953 (Kinsey Institute, n.d.).',
    'Hiệp hội Tình dục học Thế giới (WAS) ra đời năm 1978 và đổi tên thành Hiệp hội Sức khỏe Tình dục Thế giới năm 2005 (Coleman &amp; Ford, 2024).',
])

c += H2('Tình dục học nghiên cứu những gì?')
c += P('Tình dục học xem xét tình dục con người như một hiện tượng sinh học, tâm lý và xã hội. Có thể hình dung phạm vi của ngành qua ba nhóm câu hỏi:')
c += UL([
    '<strong>Sinh học:</strong> cơ thể đáp ứng tình dục ra sao, các rối loạn chức năng tình dục là gì. Bài ' + A('roi-loan-chuc-nang-tinh-duc-thuong-gap', 'rối loạn chức năng tình dục thường gặp') + ' là một ví dụ.',
    '<strong>Tâm lý:</strong> ham muốn, cảm xúc, bản dạng giới, xu hướng tính dục. Xem thêm bài ' + A('ban-dang-gioi-va-xu-huong-tinh-duc-khac-nhau-the-nao', 'bản dạng giới và xu hướng tính dục khác nhau thế nào') + '.',
    '<strong>Xã hội:</strong> chuẩn mực văn hóa, quan hệ quyền lực, giáo dục giới tính, quyền tình dục, sức khỏe tình dục cộng đồng.',
])
c += P('Theo Coleman và Ford (2024), các nhà tình dục học tiên phong không chỉ nghiên cứu mà còn vận động cho cải cách xã hội, như giáo dục giới tính, tiếp cận chăm sóc sức khỏe và quyền tình dục. Khẩu hiệu của viện tình dục học đầu tiên là "Thông qua khoa học để đến công lý".')

c += H2('Tình dục học ra đời và phát triển như thế nào?')
c += TABLE(['Năm', 'Sự kiện'], [
    ['1886', 'Bác sĩ tâm thần Richard von Krafft-Ebing xuất bản lần đầu cuốn <em>Psychopathia Sexualis</em> (Schmid, 2020).'],
    ['1908', 'Iwan Bloch và Magnus Hirschfeld ra mắt tạp chí tình dục học đầu tiên (Coleman &amp; Ford, 2024).'],
    ['1919', 'Viện Tình dục học đầu tiên được thành lập tại Berlin, sau này gọi là Viện Hirschfeld (Coleman &amp; Ford, 2024).'],
    ['1921', 'Hội nghị tình dục học quốc tế đầu tiên được tổ chức (Coleman &amp; Ford, 2024).'],
    ['1933', 'Đức Quốc xã đột kích và đóng cửa Viện Hirschfeld, gọi tình dục học là "khoa học Do Thái" (Coleman &amp; Ford, 2024).'],
    ['1947', 'Alfred Kinsey và cộng sự thành lập Viện Nghiên cứu Tình dục tại Mỹ, gắn với Đại học Indiana (Kinsey Institute, n.d.).'],
    ['1948, 1953', 'Công bố hai báo cáo về hành vi tình dục của nam giới và nữ giới (Kinsey Institute, n.d.).'],
    ['1958', 'Hội Nghiên cứu Khoa học về Tình dục (SSSS) ra đời, tổ chức khoa học liên ngành đầu tiên về tình dục ở Mỹ (Coleman &amp; Ford, 2024).'],
    ['1966', 'William Masters và Virginia Johnson xuất bản <em>Human Sexual Response</em> (Coleman &amp; Ford, 2024).'],
    ['1975', 'WHO công bố tài liệu kỹ thuật với định nghĩa mới về sức khỏe tình dục (Coleman &amp; Ford, 2024).'],
    ['1978', 'Hiệp hội Tình dục học Thế giới (WAS) được thành lập tại một hội nghị ở Rome (Coleman &amp; Ford, 2024).'],
    ['2002', 'WHO hợp tác với WAS sửa đổi các định nghĩa về tình dục và sức khỏe tình dục (Coleman &amp; Ford, 2024).'],
    ['2005', 'WAS đổi tên thành Hiệp hội Sức khỏe Tình dục Thế giới, vẫn giữ tên viết tắt WAS (Coleman &amp; Ford, 2024).'],
])

c += H2('Vì sao WAS đổi tên từ "tình dục học" sang "sức khỏe tình dục"?')
c += P('Theo Coleman và Ford (2024), năm 2005 WAS đổi tên để phản ánh sứ mệnh rộng hơn việc thúc đẩy tình dục học, đồng thời thừa nhận rằng "tình dục học" chưa được hiểu và chấp nhận đầy đủ như một ngành học trên toàn cầu. Trang lịch sử của WAS xác nhận hiệp hội được thành lập năm 1978 và trước đây mang tên Hiệp hội Tình dục học Thế giới (World Association for Sexual Health, n.d.).')
c += P('Sự thay đổi này cho thấy xu hướng chung của ngành: từ nghiên cứu học thuật sang gắn với sức khỏe cộng đồng và quyền con người. WHO định nghĩa sức khỏe tình dục là trạng thái khỏe mạnh về thể chất, cảm xúc, tinh thần và xã hội liên quan đến tình dục, không chỉ là không có bệnh tật, và đòi hỏi tôn trọng các quyền tình dục. Đây là định nghĩa làm việc từ cuộc tham vấn kỹ thuật năm 2002, công bố năm 2006 (World Health Organization, n.d.). Xem thêm mục ' + GL('suc-khoe-tinh-duc-sexual-health', 'sức khỏe tình dục') + ' trong thư viện thuật ngữ.')

c += H2('Tình dục học khác giáo dục giới tính và trị liệu tình dục thế nào?')
c += TABLE(['', 'Tình dục học', 'Giáo dục giới tính', 'Trị liệu tình dục'], [
    ['Bản chất', 'Lĩnh vực nghiên cứu khoa học', 'Hoạt động truyền đạt kiến thức', 'Hoạt động lâm sàng'],
    ['Mục tiêu', 'Tạo ra hiểu biết mới', 'Giúp người học hiểu và ra quyết định an toàn', 'Hỗ trợ cá nhân, cặp đôi giải quyết khó khăn'],
    ['Ví dụ', 'Khảo sát hành vi, nghiên cứu đáp ứng tình dục', 'Chương trình ' + A('giao-duc-tinh-duc-toan-dien-la-gi-khong-chi-dung-lai-o-tranh-thai', 'giáo dục tình dục toàn diện') + '', 'Tư vấn, trị liệu rối loạn chức năng'],
])
c += P('Bảng do người viết tổng hợp. Ba hoạt động liên quan chặt chẽ: giáo dục và trị liệu dựa trên bằng chứng từ nghiên cứu tình dục học, và một người có thể làm cả ba.')

c += H2('Câu hỏi thường gặp')
c += H3('Tình dục học có phải là ngành y không?')
c += P('Không hoàn toàn. Tình dục học là lĩnh vực liên ngành; ngay từ đầu, nó đã thách thức góc nhìn y khoa vốn chủ yếu xem tình dục qua lăng kính bệnh lý (Coleman &amp; Ford, 2024). Người làm tình dục học có thể xuất thân từ y khoa, tâm lý học, xã hội học, giáo dục hay y tế công cộng.')
c += H3('Ai được xem là "cha đẻ" của tình dục học?')
c += P('Không có một người duy nhất. Iwan Bloch đặt ra thuật ngữ, Magnus Hirschfeld lập viện nghiên cứu đầu tiên, còn Alfred Kinsey và Masters, Johnson đặt nền móng cho nghiên cứu thực nghiệm hiện đại (Coleman &amp; Ford, 2024).')
c += H3('Tình dục học hiện đối mặt với thách thức gì?')
c += P('Coleman và Ford (2024) cho rằng lịch sử ngành cho thấy tình dục học thường bị tấn công về chính trị, từ việc Đức Quốc xã đóng cửa Viện Hirschfeld đến nỗ lực cắt ngân sách Viện Kinsey ở bang Indiana năm 2023.')

c += H2('Điều gì nên nhớ?')
c += P('Tình dục học là lĩnh vực khoa học liên ngành, ra đời từ nỗ lực hiểu tình dục con người một cách khách quan thay vì chỉ qua lăng kính bệnh lý hay đạo đức. Từ Berlin năm 1919 đến Viện Kinsey và các hiệp hội quốc tế, ngành này ngày càng gắn với sức khỏe tình dục và quyền con người. Bài này mở đầu chuỗi bài tình dục học trên Dy Khoa Blog; xem thêm mục ' + GL('tinh-duc-hoc-sexology', 'tình dục học') + ' trong thư viện thuật ngữ.')
c += GEN_END + REFS([CF, KI, IU, WAS, WHO])

d = dict(id=573, slug='tinh-duc-hoc-la-gi', title='Tình dục học là gì? Ngành khoa học nghiên cứu điều gì',
    seo_title='Tình dục học là gì? Lịch sử, phạm vi nghiên cứu',
    meta_desc='Tình dục học (sexology) là gì? Lĩnh vực khoa học liên ngành về tình dục con người: phạm vi nghiên cứu, lịch sử từ Berlin 1919 đến Viện Kinsey và WAS.',
    focus_kw='tình dục học là gì',
    excerpt='Tình dục học là lĩnh vực nghiên cứu khoa học, liên ngành về tình dục con người. Phạm vi, lịch sử hình thành và khác biệt với giáo dục giới tính, trị liệu tình dục.', content=c)
json.dump(d, open(os.path.join(H, 'tdh.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

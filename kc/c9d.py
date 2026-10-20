import json, re, os
exec(open('/home/claude/dy-khoa-campus/ttkh/nhatky.py').read().split('posts = []')[0])
H = os.path.dirname(os.path.abspath(__file__))
GEN_END = END.replace('Bài viết này viết dựa trên quan điểm của người viết, là Nguyễn Hoàng Anh Khoa', 'Bài viết này được tổng hợp bởi Nguyễn Hoàng Anh Khoa')
def H3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def TABLE(head, rows):
    th=''.join(f'<th>{h}</th>' for h in head); tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'

FA = 'Faverio, P., Aliberti, S., Bellelli, G., Suigo, G., Lonni, S., Pesci, A., &amp; Restrepo, M. I. (2014). The management of community-acquired pneumonia in the elderly. <em>European Journal of Internal Medicine, 25</em>(4), 312-319. https://doi.org/10.1016/j.ejim.2013.12.001 (bản mở: https://pmc.ncbi.nlm.nih.gov/articles/PMC4102338/)'
CDC = 'Centers for Disease Control and Prevention. (2026, ngày 25 tháng 2). <em>Pneumococcal vaccine recommendations</em>. https://www.cdc.gov/pneumococcal/hcp/vaccine-recommendations/index.html'
WHO = 'World Health Organization. (2022, ngày 11 tháng 11). <em>Pneumonia in children</em> [Tờ thông tin]. https://www.who.int/news-room/fact-sheets/detail/pneumonia'

c = ''
c += P('Viêm phổi ở người cao tuổi thường không có biểu hiện điển hình như sốt, ho, đau ngực. Thay vào đó, người bệnh có thể chỉ bị lú lẫn đột ngột, té ngã, ăn kém, tiểu không tự chủ hoặc bỗng nhiên yếu đi, không tự sinh hoạt được như trước (Faverio và cộng sự, 2014). Vì vậy, người nhà cần chú ý đến những thay đổi bất thường này, thay vì chỉ chờ đến khi người cao tuổi sốt hay ho.')
c += P('<strong>Tóm tắt nhanh:</strong>')
c += UL([
    'Viêm phổi là một trong những nguyên nhân chính gây bệnh tật và tử vong ở người cao tuổi (Faverio và cộng sự, 2014).',
    'Ở người cao tuổi, lú lẫn, té ngã, ăn kém, suy giảm khả năng tự sinh hoạt thường gặp hơn sốt, ho, khó thở.',
    'Khó nuốt, răng miệng kém vệ sinh, sa sút trí tuệ, bệnh Parkinson làm tăng nguy cơ viêm phổi do hít sặc.',
    'Tiêm vắc xin cúm và phế cầu là biện pháp phòng ngừa được khuyến nghị (Faverio và cộng sự, 2014; Centers for Disease Control and Prevention [CDC], 2026).',
])

c += H2('Vì sao viêm phổi ở người cao tuổi dễ bị bỏ sót?')
c += P('Nhiều nghiên cứu xác nhận viêm phổi ở người cao tuổi thường có biểu hiện không điển hình. Faverio và cộng sự (2014) tổng hợp các biểu hiện như sau:')
c += TABLE(['Thường gặp hơn ở người cao tuổi', 'Ít gặp hơn ở người cao tuổi'], [
    ['Té ngã', 'Đau ngực khi hít thở'],
    ['Thay đổi đột ngột khả năng tự sinh hoạt', 'Ho'],
    ['Ăn uống kém', 'Khó thở'],
    ['Tiểu không tự chủ', 'Sốt'],
    ['Mê sảng, lú lẫn cấp', 'Tăng bạch cầu'],
])
c += P('Các tác giả khuyến nghị nghi ngờ viêm phổi ở người cao tuổi có các biểu hiện không điển hình này. Người cao tuổi cũng có thể không có các phản ứng viêm "kinh điển" như sốt hay nhịp tim nhanh (Faverio và cộng sự, 2014).')
c += P('Với người nhà, điều này có nghĩa là: nếu ông bà, cha mẹ <strong>bỗng nhiên lú lẫn, đi đứng loạng choạng, té ngã, bỏ ăn hoặc không tự làm được những việc thường ngày</strong>, đó có thể là dấu hiệu của một bệnh cấp tính như viêm phổi, không nên nghĩ đơn giản là "do tuổi già".')

c += H2('Ai có nguy cơ cao hơn?')
c += P('Người cao tuổi có nhiều yếu tố nguy cơ viêm phổi do hít sặc, tức là khi thức ăn, nước bọt hoặc dịch từ miệng, họng đi vào phổi. Tuổi tác có thể làm thay đổi phản xạ nuốt, nhưng nguyên nhân chính là các bệnh nền, suy giảm nhận thức và khuyết tật (Faverio và cộng sự, 2014). Các yếu tố liên quan đến tăng nguy cơ hít sặc gồm:')
c += UL([
    'Khó nuốt.',
    'Sa sút trí tuệ nặng, bệnh Parkinson.',
    'Bệnh phổi, đái tháo đường.',
    'Sức khỏe răng miệng kém.',
    'Suy dinh dưỡng.',
    'Một số thuốc như thuốc chống loạn thần, thuốc giảm tiết axit dạ dày nhóm ức chế bơm proton.',
])
c += P('Hít sặc cũng là yếu tố nguy cơ của viêm phổi nặng và có tỉ lệ tử vong cao (Faverio và cộng sự, 2014). Không tự ý ngừng thuốc đang dùng; nếu lo ngại, hãy trao đổi với bác sĩ điều trị.')
c += P('Ngoài ra, các yếu tố như suy giảm khả năng tự sinh hoạt, suy giảm nhận thức và chỉ số khối cơ thể thấp liên quan đến nguy cơ tử vong cao hơn khi nằm viện vì viêm phổi (Faverio và cộng sự, 2014).')

c += H2('Phòng viêm phổi ở người cao tuổi thế nào?')
c += H3('Tiêm vắc xin')
c += UL([
    '<strong>Vắc xin cúm hằng năm:</strong> các nghiên cứu đoàn hệ lớn cho thấy tiêm vắc xin cúm giảm đáng kể nguy cơ nhiễm cúm và tử vong ở người cao tuổi (Faverio và cộng sự, 2014). Bài ' + A('nguoi-lon-co-nen-tiem-vac-xin-cum-moi-nam', 'người lớn có nên tiêm vắc xin cúm mỗi năm') + ' giải thích thêm.',
    '<strong>Vắc xin phế cầu:</strong> phế cầu là tác nhân vi khuẩn thường gặp gây viêm phổi ở người cao tuổi (Faverio và cộng sự, 2014). Tại Hoa Kỳ, CDC khuyến nghị tiêm vắc xin phế cầu cộng hợp cho mọi người từ 50 tuổi trở lên chưa tiêm hoặc không rõ đã tiêm (CDC, 2026). Lịch tiêm và loại vắc xin phù hợp ở Việt Nam nên hỏi bác sĩ hoặc cơ sở tiêm chủng.',
])
c += H3('Chăm sóc hằng ngày')
c += UL([
    '<strong>Giữ vệ sinh răng miệng</strong>, vì sức khỏe răng miệng kém liên quan đến nguy cơ hít sặc (Faverio và cộng sự, 2014).',
    '<strong>Chú ý khi ăn uống</strong> ở người khó nuốt hoặc sa sút trí tuệ; nếu thấy hay sặc, ho khi ăn, nên hỏi bác sĩ.',
    '<strong>Đảm bảo dinh dưỡng</strong>, vì suy dinh dưỡng vừa là yếu tố nguy cơ hít sặc vừa liên quan đến tiên lượng xấu hơn.',
    '<strong>Rửa tay bằng xà phòng</strong>, biện pháp vệ sinh được WHO đưa vào nhóm phòng chống viêm phổi (World Health Organization, 2022).',
])

c += H2('Khi nào cần đưa người cao tuổi đi khám?')
c += P('Nên đưa đi khám sớm khi người cao tuổi có các biểu hiện hô hấp như ho, khó thở, hoặc có những thay đổi đột ngột như lú lẫn, té ngã, bỏ ăn, không tự sinh hoạt được, kể cả khi không sốt (Faverio và cộng sự, 2014).')
c += P('Viêm phổi do vi khuẩn được điều trị bằng kháng sinh theo chỉ định của bác sĩ (World Health Organization, 2022). Không tự mua kháng sinh, vì việc chọn thuốc ở người cao tuổi phụ thuộc vào mức độ nặng, bệnh nền và nguy cơ vi khuẩn kháng thuốc (Faverio và cộng sự, 2014). Bài ' + A('bi-cam-cum-co-nen-uong-khang-sinh', 'bị cảm cúm có nên uống kháng sinh') + ' giải thích khi nào kháng sinh có ích.')

c += H2('Câu hỏi thường gặp')
c += H3('Người cao tuổi không sốt thì có thể bị viêm phổi không?')
c += P('Có. Ở người cao tuổi, sốt thuộc nhóm biểu hiện ít gặp hơn so với lú lẫn, té ngã hay ăn kém (Faverio và cộng sự, 2014).')
c += H3('Đã tiêm vắc xin cúm thì có cần tiêm phế cầu không?')
c += P('Hai vắc xin phòng hai tác nhân khác nhau. Faverio và cộng sự (2014) cho biết có đồng thuận rằng nên khuyến nghị cả hai cho người cao tuổi. Hãy hỏi bác sĩ về lịch tiêm phù hợp.')
c += H3('Ông bà hay bị sặc khi ăn có đáng lo không?')
c += P('Đáng chú ý. Khó nuốt là một yếu tố nguy cơ của viêm phổi do hít sặc (Faverio và cộng sự, 2014). Nên báo bác sĩ để được đánh giá chức năng nuốt.')

c += H2('Điều gì nên nhớ?')
c += P('Viêm phổi ở người cao tuổi thường "giấu mặt": không sốt, không ho, mà chỉ là lú lẫn, té ngã, bỏ ăn hoặc yếu đi đột ngột. Người nhà cần coi những thay đổi này là dấu hiệu cần đi khám. Tiêm vắc xin cúm và phế cầu, giữ vệ sinh răng miệng, chú ý khi ăn uống và đảm bảo dinh dưỡng giúp giảm nguy cơ.')
c += P('<em>Bài viết mang tính thông tin, không thay thế tư vấn y khoa cho từng cá nhân.</em>')
c += GEN_END + REFS([CDC, FA, WHO])

d = dict(slug='viem-phoi-o-nguoi-cao-tuoi', title='Viêm phổi ở người cao tuổi: dấu hiệu dễ bỏ sót và cách phòng',
    seo_title='Viêm phổi ở người cao tuổi: dấu hiệu dễ bỏ sót, cách phòng',
    meta_desc='Viêm phổi ở người cao tuổi thường không sốt, không ho mà chỉ lú lẫn, té ngã, bỏ ăn. Dấu hiệu dễ bỏ sót, ai có nguy cơ cao và cách phòng bằng vắc xin.',
    focus_kw='viêm phổi ở người cao tuổi',
    excerpt='Ở người cao tuổi, viêm phổi thường biểu hiện bằng lú lẫn, té ngã, bỏ ăn hơn là sốt, ho. Dấu hiệu cần chú ý, yếu tố nguy cơ và cách phòng ngừa.',
    tags=['viêm phổi', 'người cao tuổi', 'vắc xin phế cầu', 'vắc xin cúm', 'chăm sóc người cao tuổi'], content=c, categories=[4, 11],
    date='2026-11-07T08:00:00', cover_alt='Minh họa người cao tuổi ngồi ghế với chiếc gậy, bên cạnh hình lá phổi và ống tiêm vắc xin')
json.dump(d, open(os.path.join(H, d['slug'] + '.json'), 'w'), ensure_ascii=False, indent=1)
t = re.sub('<[^>]+>', ' ', c); body = t.split('Đôi lời giới thiệu')[0]
print('words', len(body.split()), 'banned', [b for b in ['dẫn theo', 'truy cập mở', 'sinh viên', '—', '–', ' - '] if b in c + d['meta_desc'] + d['excerpt'] + d['title']], 'meta', len(d['meta_desc']), 'seo', len(d['seo_title']))

import json, os
H = os.path.dirname(os.path.abspath(__file__))
U = 'https://dykhoa.com/blog/'
IMG = '{IMG:%s}'
C = {'a': ('#4f7d62', '#eef4ef', 'Nền tảng'), 'b': ('#b85c45', '#fbefe9', 'Kỹ năng'), 'c': ('#b8862f', '#fbf4e4', 'Học và làm nghề'), 'd': ('#2b5876', '#eaf1f6', 'Ở Việt Nam')}
NEW = {'co-nen-hoc-thac-si-truyen-thong-khoa-hoc', 'nha-khoa-hoc-co-can-hoc-truyen-thong', 'truyen-thong-khoa-hoc-viet-nam-nghi-quyet-57', 'viet-khoa-hoc-cho-cong-chung', 'ai-trong-truyen-thong-khoa-hoc', 'danh-gia-hieu-qua-truyen-thong-khoa-hoc'}
T = '{TITLE:%s}'

def item(s):
    tag = '<em>Bài mới</em>' if s in NEW else ''
    return f'<a class="tth-item" href="{U}{s}/"><img src="{IMG % s}" alt="" loading="lazy" width="1200" height="675"><span><b>{T % s}</b>{tag}</span></a>'

def chang(k, n, lede, lead, lead_txt, items):
    c, bg, name = C[k]
    tag = 'Bài mới' if lead in NEW else 'Đọc trước'
    return (f'<section class="tth-ch" id="chang-{n}" style="--c:{c};--bg:{bg}"><div class="tth-ch__head"><span class="tth-ch__n" aria-hidden="true">{n}</span><div>'
            f'<p class="tth-ch__eb">Chặng {n}</p><h2>{name}</h2><p class="tth-ch__lede">{lede}</p></div></div><div class="tth-ch__body">'
            f'<a class="tth-lead" href="{U}{lead}/"><img src="{IMG % lead}" alt="" loading="lazy" width="1200" height="675"><span class="tth-tag">{tag}</span><h3>{T % lead}</h3><p>{lead_txt}</p></a>'
            f'<div class="tth-list">{"".join(item(s) for s in items)}</div></div></section>')

steps = ''.join(f'<a class="tth-step" style="--c:{C[k][0]}" href="#chang-{i+1}"><i>{i+1}</i><b>{C[k][2]}</b><small>{d}</small></a>' for i, (k, d) in enumerate(zip('abcd', ['Khái niệm, lịch sử, đạo đức', 'Viết, kể chuyện, dùng AI, đo hiệu quả', 'Học ở đâu, làm nghề gì', 'Chính sách và bối cảnh trong nước'])))
course = lambda c, t, url: f'<a class="tth-course" style="--c:{c}" href="{url}"><small>Khóa học</small><b>{t}</b><span>Xem khóa học →</span></a>'
faq = lambda q, a: f'<details><summary>{q}</summary><p>{a}</p></details>'
L = lambda s, t: f'<a href="{U}{s}/">{t}</a>'

html = f'''<!-- wp:html -->
<div class="tth">
<section class="tth-hero" aria-label="Chuyên đề Truyền thông khoa học"><img class="tth-hero__img" src="{IMG % 'banner'}" alt="Tranh màu nước: một nhà khoa học trò chuyện với người dân nhiều thế hệ dưới gốc đa treo đèn lồng bên bờ sông lúc hoàng hôn" width="2400" height="1200" fetchpriority="high">
<div class="tth-hero__card"><p class="tth-hero__eb">Chuyên đề · Dy Khoa Blog</p><h1>Truyền thông khoa học: <em>bắt đầu từ đâu?</em></h1><p class="tth-hero__lede">Lộ trình 4 chặng cho người làm truyền thông, giảng viên, người học và nhà khoa học.</p><a class="tth-btn" href="#lo-trinh">Xem lộ trình</a><a class="tth-btn tth-btn--g" href="#khoa-hoc">Khóa học</a></div></section>
<p class="tth-intro">Truyền thông khoa học là cầu nối giữa nghiên cứu và đời sống. Chuyên đề này gom các bài viết theo bốn chặng, từ hiểu đúng khái niệm đến thực hành và bối cảnh Việt Nam, để bạn đọc theo thứ tự hoặc chọn đúng chặng mình cần.</p>
<nav class="tth-path" id="lo-trinh" aria-label="Lộ trình 4 chặng">{steps}</nav>
{chang('a', 1, 'Truyền thông khoa học là gì, đến từ đâu, khác gì báo chí và PR, và cần giữ những chuẩn mực nào.', 'truyen-thong-khoa-hoc-la-gi', 'Bài nền để hiểu truyền thông khoa học là gì trước khi đi vào các chặng sau.', ['lich-su-truyen-thong-khoa-hoc', 'ttkh-khac-gi-bao-chi-giao-duc-pr-khoa-hoc', 'dao-duc-trong-truyen-thong-khoa-hoc', 'mo-hinh-tham-hut-den-tham-gia-cong-chung-truyen-thong-khoa-hoc'])}
{chang('b', 2, 'Từ viết cho công chúng, kể chuyện đến dùng AI và đo hiệu quả một cách có trách nhiệm.', 'viet-khoa-hoc-cho-cong-chung', 'Cấu trúc, thuật ngữ, con số và sự bất định: những khác biệt khi chuyển từ bài báo khoa học sang bài cho công chúng.', ['ky-nang-cot-loi-truyen-thong-khoa-hoc', 'ke-chuyen-khoa-hoc-storytelling', 'truyen-thong-khoa-hoc-tren-mang-xa-hoi', 'ai-trong-truyen-thong-khoa-hoc', 'danh-gia-hieu-qua-truyen-thong-khoa-hoc'])}
{chang('c', 3, 'Học ở đâu, có nên học thạc sĩ, ra trường làm gì, và vì sao nhà khoa học cũng cần kỹ năng này.', 'co-nen-hoc-thac-si-truyen-thong-khoa-hoc', 'Những điều nên cân nhắc trước khi đăng ký: chương trình, đầu vào và con đường nghề nghiệp sau tốt nghiệp.', ['hoc-truyen-thong-khoa-hoc-o-dau-tren-the-gioi-focus', 'hoc-truyen-thong-khoa-hoc-ra-truong-co-xin-duoc-viec-khong', 'nha-khoa-hoc-co-can-hoc-truyen-thong', 'nha-thuc-hanh-va-nha-nghien-cuu-truyen-thong-khoa-hoc', 'thiet-ke-chuong-trinh-dao-tao-truyen-thong-khoa-hoc'])}
{chang('d', 4, 'Bối cảnh chính sách trong nước và những việc truyền thông khoa học có thể làm ngay.', 'truyen-thong-khoa-hoc-viet-nam-nghi-quyet-57', 'Nghị quyết 57 và các văn bản liên quan nói gì về phổ biến khoa học, và còn những khoảng trống nào.', ['truyen-thong-rui-ro-va-khung-hoang-trong-khoa-hoc', 'thong-tin-khoa-hoc-tren-mang-co-dang-tin'])}
<section class="tth-courses" id="khoa-hoc"><h2>Học cùng Dy Khoa</h2><p class="tth-courses__lede">Khóa học tự học trực tuyến, đi từ nền tảng đến thực hành.</p><div class="tth-cgrid">{course('#4f7d62', 'Truyền thông khoa học cơ bản: Từ nghiên cứu đến công chúng', U + 'courses/truyen-thong-khoa-hoc-co-ban-tu-nghien-cuu-den-cong-chung/')}{course('#b85c45', 'Viết nội dung sức khỏe cho công chúng', U + 'courses/viet-noi-dung-suc-khoe-cho-cong-chung/')}{course('#b8862f', 'Truyền thông kỹ thuật cho công chúng: Từ chuyên môn đến thấu hiểu', U + 'courses/truyen-thong-ky-thuat-cho-cong-chung-tu-chuyen-mon-den-thau-hieu/')}</div></section>
<h2 class="tth-faqh" id="hoi-dap">Hỏi đáp nhanh</h2>
<div class="tth-faq">{faq('Truyền thông khoa học khác gì báo chí khoa học và PR?', 'Ba lĩnh vực giao nhau nhưng khác mục tiêu và chuẩn mực nghề nghiệp. Bài ' + L('ttkh-khac-gi-bao-chi-giao-duc-pr-khoa-hoc', 'Truyền thông khoa học khác gì báo chí, giáo dục và PR khoa học') + ' phân tích chi tiết.')}{faq('Không học chuyên ngành có làm truyền thông khoa học được không?', 'Có nhiều con đường vào nghề. Xem ' + L('hoc-truyen-thong-khoa-hoc-ra-truong-co-xin-duoc-viec-khong', 'cơ hội việc làm') + ' và ' + L('co-nen-hoc-thac-si-truyen-thong-khoa-hoc', 'những điều cần cân nhắc trước khi học thạc sĩ') + '.')}{faq('Nhà khoa học nên bắt đầu từ đâu?', 'Bắt đầu từ mục tiêu và công chúng cụ thể, rồi mới chọn kênh. Bài ' + L('nha-khoa-hoc-co-can-hoc-truyen-thong', 'Nhà khoa học có cần học truyền thông không?') + ' tổng hợp lợi ích, rào cản và bằng chứng về đào tạo.')}{faq('Làm sao biết một hoạt động truyền thông khoa học có hiệu quả?', 'Lượt xem chỉ là đầu ra. Bài ' + L('danh-gia-hieu-qua-truyen-thong-khoa-hoc', 'Đo hiệu quả truyền thông khoa học') + ' giải thích cách phân biệt đầu ra, kết quả và tác động.')}</div>
</div>
<!-- /wp:html -->'''
open(os.path.join(H, 'hub.html'), 'w').write(html)
print(len(html))

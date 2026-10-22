import datetime, html
S={'08':'08:00','11':'11:30','16':'16:00','19':'19:30'}
P=[]
def add(slot,cl,days,titles):
    for d,t in zip(days,titles): P.append((d,slot,cl,t))
add('08','A1',range(12,19),["Tiền đái tháo đường là gì","HbA1c và đường huyết lúc đói: đọc chỉ số thế nào","Ai cần tầm soát đái tháo đường, khi nào? (ADA 35 tuổi, Bộ Y tế 45 tuổi)","Đái tháo đường típ 2 có thuyên giảm được không","Đái tháo đường thai kỳ","Chăm sóc bàn chân người đái tháo đường","Hạ đường huyết: dấu hiệu và xử trí"])
add('08','A2',range(19,25),["Viêm họng: khi nào cần kháng sinh","Nhiễm khuẩn tiết niệu ở phụ nữ","Tự mua kháng sinh, dùng thuốc còn thừa: rủi ro gì","Uống kháng sinh đúng như kê đơn: vì sao liệu trình ngắn là có chủ đích","Trẻ viêm tai giữa có cần kháng sinh ngay","Kháng sinh trong chăn nuôi và thực phẩm"])
add('08','A3',range(25,31),["PrEP là gì, ai nên dùng","PEP: dùng thuốc trong 72 giờ sau phơi nhiễm","Xét nghiệm HIV và thời kỳ cửa sổ","Tự xét nghiệm HIV","Người có HIV điều trị sớm sống được bao lâu","Thuốc tiêm PrEP lenacapavir: WHO khuyến cáo gì"])
add('11','B1',range(12,19),["Mạng xã hội có gây trầm cảm ở tuổi teen? Bằng chứng nói gì","Dùng mạng xã hội “có vấn đề” là gì","Mấy tuổi nên cho trẻ dùng mạng xã hội","Mạng xã hội và hình ảnh cơ thể ở tuổi teen","Điện thoại trong phòng ngủ và giấc ngủ của trẻ","Bắt nạt trên mạng: dấu hiệu và cách hỗ trợ","Cha mẹ nên kiểm soát hay đồng hành"])
add('11','B2',range(19,25),["Thế giới thiếu bao nhiêu giáo viên, vì sao","Ngày Nhà giáo Việt Nam 20/11 có từ đâu","Giáo viên kiệt sức: số liệu quốc tế","Phản hồi thế nào để học sinh tiến bộ","Bài tập về nhà có giúp học tốt hơn","Lớp ít học sinh có học tốt hơn"])
add('11','B3',range(25,31),["Kiểm soát cưỡng ép là gì","Bạo lực tinh thần trong gia đình","Bạo lực trong hẹn hò ở người trẻ","Vì sao người bị bạo hành khó rời đi","Thấy bạo lực gia đình: luật yêu cầu gì và bảo vệ người báo tin thế nào","Phát tán ảnh nhạy cảm và pháp luật Việt Nam"])
add('16','C',range(22,31),["Số ca mắc và tỷ lệ mắc khác nhau thế nào","Trung bình và trung vị: con số nào nói thật hơn","Khoảng tin cậy đọc thế nào","NNT: số người cần điều trị là gì","Giảm tử vong do một bệnh, không giảm tử vong chung","Độ nhạy và độ đặc hiệu của xét nghiệm","Vì sao xét nghiệm dương tính chưa chắc là mắc bệnh","Tầm soát và “sống lâu hơn” ảo","Tỷ lệ tử vong ca bệnh khi dịch mới bùng phát"])
add('19','D1',[14,15,16,17,19,21,22],["Review nhận tiền phải ghi rõ “quảng cáo” thế nào","Luật Quảng cáo sửa đổi 2025: KOL chịu trách nhiệm gì","“Người có ảnh hưởng” và “người chuyển tải quảng cáo”: luật định nghĩa ra sao","Chọn KOL cho thương hiệu sức khỏe: giới hạn pháp lý","Hợp đồng với KOL cần phản ánh nghĩa vụ pháp lý nào","FTC, ASA, ICC: chuẩn influencer quốc tế khác nhau ra sao","Influencer ảo, AI có phải gắn nhãn không"])
add('19','D2',[23,24,27,28,29,30],["Quảng cáo dịch vụ khám chữa bệnh cần điều kiện gì","Dùng hình ảnh bác sĩ, người bệnh trong quảng cáo: luật nói gì","Đăng phản hồi của bệnh nhân lên fanpage","Quảng cáo “chữa khỏi”, “cam kết khỏi bệnh” bị cấm thế nào","Mức phạt khi quảng cáo dịch vụ y tế sai quy định","Bác sĩ livestream tư vấn: ranh giới với quảng cáo"])
assert len(P)==60, len(P)
FLAG={("A1",16):"Chỉ có nguồn ADA, Bộ Y tế chưa có hướng dẫn mở",("A1",18):"Bỏ “quy tắc 15 g” (ADA 2026 không nêu)",("A2",22):"Đổi góc từ “có cần uống hết liều”",("A3",30):"Chưa có trong hướng dẫn Việt Nam",("B2",21):"Số liệu TALIS phải mở PDF đối chiếu tay",("B3",29):"Thay bài “người chứng kiến”",("B3",30):"Kiểm lại NĐ 15/2020 Điều 102 sau sửa đổi",("D1",16):"Thay “KOC và KOL” (không có định nghĩa chính thức)",("D1",19):"Đổi góc: không có nguồn mở về điều khoản hợp đồng",("D1",21):"Thay “đo hiệu quả” (AMEC không riêng influencer)",("D1",22):"Việt Nam chưa có quy định riêng, nói rõ trong bài",("D2",24):"Đổi góc: lệnh cấm chỉ áp dụng mỹ phẩm, thiết bị y tế",("D2",28):"Phải đọc NĐ 87/2026 Điều 53 trước khi viết",("C",23):"CDC chỉ còn bản lưu trữ, dùng làm nguồn phụ",("C",22):"CDC chỉ còn bản lưu trữ, dùng làm nguồn phụ"}
CL={
'A1':("Sức khỏe","Đái tháo đường","Ngày Đái tháo đường thế giới 14/11",["ADA Standards of Care in Diabetes 2026 (mục 2, 6)","Bộ Y tế, QĐ 3087/QĐ-BYT 2020 (tiền đái tháo đường)","Riddle và cộng sự 2021, Diabetes Care (thuyên giảm)","IWGDF 2023 (bàn chân)","WHO fact sheet đái tháo đường"]),
'A2':("Sức khỏe","Dùng kháng sinh đúng","Tuần lễ nhận thức kháng thuốc 18–24/11",["WHO AWaRe antibiotic book 2022","WHO fact sheet kháng thuốc (7/2026)","GBD 2021 AMR Collaborators, Lancet 2024","WHO 2017, hướng dẫn kháng sinh trong chăn nuôi"]),
'A3':("Sức khỏe","Dự phòng HIV","Ngày Thế giới phòng chống AIDS 1/12",["WHO consolidated HIV guidelines 2021 + cập nhật 2025","WHO PEP guidelines 2024; WHO lenacapavir guideline 2025","Bộ Y tế, QĐ 5968/QĐ-BYT 2021","Trickey và cộng sự 2023, Lancet HIV","WHO fact sheet HIV (7/2026)"]),
'B1':("Tâm lý & Đời sống số","Mạng xã hội và tuổi teen","",["US Surgeon General Advisory 2023","APA Health Advisory 2023","WHO/Europe HBSC 2024 (tập 2, tập 6)","Fassi và cộng sự 2024, JAMA Pediatrics","Carter và cộng sự 2016, JAMA Pediatrics","Luật tuổi tối thiểu dùng MXH của Úc 2024"]),
'B2':("Tâm lý & Đời sống số","Giáo viên và việc học","Ngày Nhà giáo Việt Nam 20/11",["UNESCO Global report on teachers 2024","OECD TALIS 2024","EEF Teaching and Learning Toolkit","Luật Nhà giáo 73/2025/QH15, Điều 32"]),
'B3':("Tâm lý & Đời sống số","Bạo lực với phụ nữ","Ngày quốc tế xóa bỏ bạo lực với phụ nữ 25/11",["WHO VAW prevalence estimates 2023 (công bố 11/2025)","UNODC & UN Women, Femicides in 2024","Nghiên cứu quốc gia về bạo lực với phụ nữ VN 2019","WHO RESPECT 2019","Luật Phòng, chống bạo lực gia đình 13/2022/QH15"]),
'C':("Truyền thông khoa học","Đọc đúng con số y tế trên báo","",["Woloshin, Schwartz & Welch 2008, Know Your Chances","Evans và cộng sự 2011, Testing Treatments","Cochrane Handbook v6.5, chương 15","WHO/Europe 2020, Screening programmes: a short guide","WHO 2020, Estimating mortality from COVID-19","CDC Principles of Epidemiology (bản lưu trữ, nguồn phụ)"]),
'D1':("Thực hành Marcom","KOL và influencer theo luật mới","",["Luật Quảng cáo 2012, sửa đổi bởi Luật 75/2025/QH15 (hiệu lực 1/1/2026)","NĐ 342/2025/NĐ-CP (thay NĐ 181/2013)","NĐ 87/2026/NĐ-CP xử phạt (thay NĐ 38/2021)","Luật Bảo vệ quyền lợi người tiêu dùng 2023","FTC 16 CFR 255 và Disclosures 101","ICC Marketing Code 2024; ASA/CAP Influencers' guide"]),
'D2':("Thực hành Marcom","Quảng cáo dịch vụ y tế","",["Luật Khám bệnh, chữa bệnh 15/2023/QH15","Luật Quảng cáo (sửa đổi 2025)","NĐ 342/2025/NĐ-CP, Điều 9","NĐ 87/2026/NĐ-CP, Điều 75","ICC Marketing Code 2024"]),
}
COL={'A':'a','B':'b','C':'c','D':'d'}
existing={'08':set(range(1,12)),'11':set(range(1,12)),'16':set(range(1,22)),'19':{1,2,3,4,5,6,7,8,9,10,11,12,13,18,20}}
wd=['T2','T3','T4','T5','T6','T7','CN']
e=html.escape
rows=[]
for d in range(12,31):
    dt=datetime.date(2026,11,d)
    cells=[]
    for s in ['08','11','16','19']:
        hit=[p for p in P if p[0]==d and p[1]==s]
        if hit:
            _,_,cl,t=hit[0]; f=FLAG.get((cl,d))
            cells.append(f'<td class="k-{COL[cl[0]]}"><span class="tag">{cl}</span><span class="t">{e(t)}</span>'+(f'<span class="fl">{e(f)}</span>' if f else '')+'</td>')
        elif (d,s)==(26,'19'): cells.append('<td class="have">Còn trống</td>')
        else: cells.append('<td class="have">Đã có bài</td>')
    rows.append(f'<tr><th scope="row"><b>{d}/11</b><small>{wd[dt.weekday()]}</small></th>{"".join(cells)}</tr>')
cards=[]
for k,(cat,name,obs,src) in CL.items():
    n=sum(1 for p in P if p[2]==k)
    cards.append(f'<article class="cl k-{COL[k[0]]}"><header><span class="tag">{k}</span><h3>{e(name)}</h3></header><p class="meta">{e(cat)} · {n} bài'+(f' · {e(obs)}' if obs else '')+'</p><ul>'+''.join(f'<li>{e(x)}</li>' for x in src)+'</ul></article>')
nflag=len(FLAG)
page=open('tpl.html').read().replace('{{ROWS}}','\n'.join(rows)).replace('{{CARDS}}','\n'.join(cards)).replace('{{NFLAG}}',str(nflag))
open('/tmp/claude-0/-home-claude/a233cde9-52b8-579d-a3d8-f2ca56bbf0f2/scratchpad/lich-thang-11.html','w').write(page)
print('ok',nflag)

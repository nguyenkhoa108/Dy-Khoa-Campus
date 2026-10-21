(()=>{
const css=`.ds-tl{margin:48px 0 8px;padding:26px 28px 22px;background:#fff;border-top:4px solid #13241d;box-shadow:0 10px 30px rgba(19,36,29,.08);font-family:"Be Vietnam Pro",sans-serif}
.ds-tl h2{font:900 13px "Be Vietnam Pro",sans-serif!important;letter-spacing:.2em;text-transform:uppercase;color:#a4504c!important;margin:0 0 14px!important;border:0!important;padding:0!important}
.ds-tl ul{list-style:none;margin:0!important;padding:0!important}
.ds-tl li{position:relative;padding:12px 0 12px 22px!important;border-top:1px solid #e6e1d6;font-family:"Be Vietnam Pro",sans-serif!important;font-size:1.02rem!important;line-height:1.55!important;color:#1b1d1c!important;margin:0!important}
.ds-tl li:first-child{border-top:0}
.ds-tl li:before{content:"";position:absolute;left:0;top:21px;width:8px;height:8px;background:#c4554b}
.ds-tl li small{display:block;font-size:.8rem;color:#6f7772;margin-top:3px}
.ds-data{margin:10px 4px 0;font-family:"Be Vietnam Pro",sans-serif}
.ds-data summary{cursor:pointer;font-size:13px;font-weight:700;color:#1f4b3a;list-style:none;display:inline-flex;align-items:center;gap:6px}
.ds-data summary::-webkit-details-marker{display:none}
.ds-data summary:before{content:"+";display:inline-grid;place-items:center;width:18px;height:18px;border:1.5px solid #1f4b3a;border-radius:50%;font-size:13px;line-height:1}
.ds-data[open] summary:before{content:"−"}
.ds-data table{width:100%;border-collapse:collapse;margin:12px 0 4px;font-size:14px;background:#fff}
.ds-data th,.ds-data td{border-bottom:1px solid #e6e1d6;padding:9px 12px;text-align:left;vertical-align:top;color:#1b1d1c}
.ds-data th{background:#13241d;color:#f3efe6;font-weight:700}
.ds-data td:last-child{white-space:nowrap;font-weight:700}
.ds-data p{font-size:13px!important;color:#6f7772!important;margin:6px 0 0!important;font-family:"Be Vietnam Pro",sans-serif!important;line-height:1.5!important}
@media(max-width:860px){.ds-tl{padding:20px 18px 16px;margin:34px 0 4px}.ds-data td:last-child{white-space:normal}}`;
const st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
const tl=`<aside class="ds-tl" aria-label="Tóm tắt nhanh"><h2>Tóm tắt nhanh</h2><ul>
<li>Tin sai lan xa hơn, nhanh hơn tin đúng, và động lực chính là con người chia sẻ chứ không phải tài khoản tự động.<small>Vosoughi và cộng sự (2018)</small></li>
<li>Trong một thí nghiệm với 8.001 người, xem tin sai về vắc-xin làm tỷ lệ "chắc chắn tiêm" giảm 6,2 điểm phần trăm ở Anh và 6,4 điểm phần trăm ở Mỹ.<small>Loomba và cộng sự (2021)</small></li>
<li>Thông tin sai vẫn ảnh hưởng tới suy luận kể cả khi đã được đính chính, và lời đính chính thường không đến được những người đã thấy tin sai.<small>Lewandowsky và cộng sự (2020); NASEM (2025)</small></li>
<li>Gỡ bỏ nội dung có ít bằng chứng ủng hộ với tin sai khoa học, và chỉ chạm vào một trong bốn điểm của dòng thông tin: nguồn cung, nhu cầu, phân phối, tiếp nhận.<small>The Royal Society (2022); NASEM (2025)</small></li>
<li>"Tiêm phòng tâm lý" bằng video ngắn giúp người xem nhận ra kỹ thuật thao túng tốt hơn, với chi phí thấp trên quy mô hàng triệu người.<small>Roozenbeek và cộng sự (2022)</small></li></ul></aside>`;
const sapo=document.querySelector('.dkx-body p.ds-sapo');sapo.insertAdjacentHTML('afterend',tl);
const T=(head,rows,note)=>`<details class="ds-data"><summary>Xem số liệu dạng chữ</summary><table><thead><tr>${head.map(h=>`<th>${h}</th>`).join('')}</tr></thead><tbody>${rows.map(r=>`<tr>${r.map(c=>`<td>${c}</td>`).join('')}</tr>`).join('')}</tbody></table>${note?`<p>${note}</p>`:''}</details>`;
const D={
'h1-thi':T(['Chỉ số','Kết quả'],[['Người xem thông tin sai về vắc-xin Covid-19','6.001 (Anh 3.000, Mỹ 3.001)'],['Người xem thông tin chính xác (nhóm đối chứng)','2.000 (mỗi nước 1.000)'],['Tỷ lệ "chắc chắn tiêm" giảm so với đối chứng, Anh','6,2 điểm %'],['Tỷ lệ "chắc chắn tiêm" giảm so với đối chứng, Mỹ','6,4 điểm %']],'Nguồn: Loomba và cộng sự (2021). Thí nghiệm tháng 9/2020.'),
'h2-tin':T(['Chỉ số','Kết quả'],[['Thời gian tin đúng cần để tiếp cận 1.500 người, so với tin sai','Lâu hơn khoảng 6 lần'],['Khả năng được chia sẻ lại của tin sai, so với tin đúng','Cao hơn 70%'],['Tác động của tài khoản tự động','Tăng tốc tin đúng và tin sai gần như ngang nhau']],'Nguồn: Vosoughi và cộng sự (2018). Twitter 2006-2017: khoảng 126.000 câu chuyện, khoảng 3 triệu người, hơn 4,5 triệu lượt đăng lại.'),
'h3-khao':T(['Nhận định','Tỷ lệ'],[['Cho rằng internet giúp công chúng hiểu khoa học tốt hơn','61%'],['Tin rằng công nghệ 5G có hại cho sức khỏe','15%'],['Không tin vắc-xin Covid-19 an toàn','5%'],['Không tin con người có bất kỳ trách nhiệm nào trong biến đổi khí hậu','5%']],'Nguồn: The Royal Society (2022), khảo sát cùng YouGov với 2.019 người dân Anh, tháng 7/2021.'),
'h4-bon':T(['Điểm can thiệp','Câu hỏi'],[['Nguồn cung','Ai tạo ra tin sai'],['Nhu cầu','Vì sao người ta tìm đến nó'],['Phân phối (gỡ bỏ nội dung tác động ở đây)','Tin sai lan đi thế nào'],['Tiếp nhận','Người ta tin và dùng nó ra sao']],'Nguồn: NASEM (2025). Chưa có điểm nào được chứng minh là tốt nhất.'),
'h6-tiem':T(['Giai đoạn','Số lượng'],[['Người dùng được hiển thị video quảng cáo (15 ngày)','Khoảng 5,4 triệu'],['Người xem từ 30 giây trở lên','967.347'],['Câu trả lời kiểm tra trong vòng 24 giờ (gồm nhóm đối chứng)','22.632'],['Chi phí trung bình mỗi lượt xem','Khoảng 0,05 USD']],'Nguồn: Roozenbeek và cộng sự (2022).'),
'h5-bon':T(['Bước','Nội dung'],[['1. Sự thật','Mở đầu bằng điều đúng, nếu nó rõ ràng, ngắn gọn, dễ nhớ'],['2. Cảnh báo','Báo trước rằng sắp nhắc tới một thông tin sai'],['3. Giải thích','Chỉ ra thông tin sai đánh lừa người đọc bằng cách nào'],['4. Sự thật','Kết thúc bằng việc nhắc lại điều đúng']],'Nguồn: Lewandowsky và cộng sự (2020).')};
document.querySelectorAll('.ds-fig').forEach(f=>{const s=f.querySelector('img').getAttribute('src');const k=Object.keys(D).find(k=>s.includes(k));if(k)f.insertAdjacentHTML('beforeend',D[k])});
return [document.querySelectorAll('.ds-data').length,!!document.querySelector('.ds-tl')]})()

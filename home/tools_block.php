            <!-- CÔNG CỤ SỨC KHỎE: TRA HUYẾT ÁP + ĐƯỜNG, MUỐI MỖI NGÀY -->
            <?php
            $dkt_link = function ( $slug ) {
                $p = get_page_by_path( $slug, OBJECT, 'post' );
                return ( $p && 'publish' === $p->post_status ) ? get_permalink( $p ) : '';
            };
            $dkt_bp1 = $dkt_link( 'huyet-ap-bao-nhieu-la-cao' );
            $dkt_bp2 = $dkt_link( 'cach-do-huyet-ap-tai-nha' );
            $dkt_su  = $dkt_link( 'moi-ngay-nap-bao-nhieu-duong-la-qua-nhieu' );
            $dkt_sa  = $dkt_link( 'nguoi-viet-an-man-den-muc-nao' );
            $dkt_lb  = $dkt_link( 'cach-doc-nhan-dinh-duong-tren-bao-bi' );
            ?>
            <style>
            .dkt{margin:4px 0 26px;--dkt-ok:#1f7a45;--dkt-mid:#a86a00;--dkt-hi:#b23a26;--dkt-soft:rgba(15,107,122,.07)}
            html.dk-dark .dkt,html.hm-dark .dkt{--dkt-ok:#6fd39a;--dkt-mid:#f0c060;--dkt-hi:#f0957f;--dkt-soft:rgba(127,207,219,.08)}
            .dkt-head{display:flex;justify-content:space-between;align-items:baseline;gap:10px;border-bottom:2px solid var(--dk-ink);padding-bottom:8px;margin-bottom:14px}
            .dkt-title{font-size:1.3rem;margin:0;color:var(--dk-ink)}
            .dkt-sub{font-size:.8rem;color:var(--dk-muted)}
            .dkt-grid{display:grid;grid-template-columns:1fr;gap:26px}
            @media (min-width:640px){.dkt-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
            .dkt-tool{min-width:0;display:flex;flex-direction:column;gap:10px;color:var(--dk-ink)}
            .dkt-kick{margin:0;font-size:.7rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#0f6b7a}
            html.dk-dark .dkt-kick,html.hm-dark .dkt-kick{color:#7fcfdb}
            .dkt-name{font-family:var(--dk-serif);font-weight:800;font-size:1.15rem;line-height:1.3;margin:0}
            .dkt-row{display:flex;gap:10px;flex-wrap:wrap}
            .dkt-field{flex:1 1 110px;display:flex;flex-direction:column;gap:4px;font-size:.8rem;color:var(--dk-muted)}
            .dkt input[type=number]{width:100%;box-sizing:border-box;padding:9px 10px;border:1px solid var(--dk-line);border-radius:8px;background:transparent;color:var(--dk-ink);font:600 1rem/1.2 var(--dk-sans)}
            .dkt input[type=number]:focus{outline:2px solid #0f6b7a;outline-offset:1px}
            .dkt-radio{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:.85rem}
            .dkt-radio label{display:flex;align-items:center;gap:6px;cursor:pointer}
            .dkt-btn{appearance:none;cursor:pointer;border-radius:999px;padding:8px 16px;font:700 .85rem/1.2 var(--dk-sans);border:1px solid var(--dk-brand);background:var(--dk-brand);color:#fff}
            html.dk-dark .dkt-btn,html.hm-dark .dkt-btn{background:#d8ef6b;border-color:#d8ef6b;color:#012a1a}
            .dkt-btn--ghost{background:transparent!important;color:var(--dk-ink)!important;border-color:var(--dk-line)!important}
            .dkt-chips{display:flex;flex-wrap:wrap;gap:6px}
            .dkt-chip{appearance:none;cursor:pointer;border:1px solid var(--dk-line);background:transparent;color:var(--dk-ink);border-radius:999px;padding:6px 11px;font:600 .8rem/1.2 var(--dk-sans)}
            .dkt-chip:hover{border-color:#0f6b7a}
            .dkt-out{background:var(--dkt-soft);border-radius:8px;padding:12px 14px;display:flex;flex-direction:column;gap:6px;font-size:.9rem;line-height:1.55}
            .dkt-out[hidden]{display:none}
            .dkt-out p{margin:0}
            .dkt-verdict{font-weight:800;font-size:1rem}
            .dkt-verdict.is-ok{color:var(--dkt-ok)}.dkt-verdict.is-mid{color:var(--dkt-mid)}.dkt-verdict.is-hi{color:var(--dkt-hi)}
            .dkt-alert{border-left:3px solid var(--dkt-hi);padding-left:10px;font-weight:600}
            .dkt-tabs{display:flex;gap:6px}
            .dkt-tab{appearance:none;cursor:pointer;border:0;border-bottom:2px solid transparent;background:transparent;color:var(--dk-muted);padding:4px 2px;margin-right:10px;font:800 .85rem/1.2 var(--dk-sans)}
            .dkt-tab[aria-selected=true]{color:var(--dk-ink);border-bottom-color:var(--dk-ink)}
            .dkt-pane[hidden]{display:none}
            .dkt-pane{display:flex;flex-direction:column;gap:10px}
            .dkt-bar{position:relative;height:10px;border-radius:99px;background:var(--dk-line);overflow:hidden}
            .dkt-bar span{position:absolute;inset:0 auto 0 0;width:0;border-radius:99px;background:var(--dkt-ok);transition:width .3s}
            .dkt-list{list-style:none;margin:0;padding:0;font-size:.85rem}
            .dkt-list li{display:flex;justify-content:space-between;gap:8px;padding:4px 0;border-bottom:1px dashed var(--dk-line)}
            .dkt-list button{appearance:none;border:0;background:transparent;color:var(--dk-muted);cursor:pointer;font-size:.9rem;padding:0 4px}
            .dkt-note,.dkt-src{margin:0;font-size:.76rem;line-height:1.5;color:var(--dk-muted)}
            .dkt-src a,.dkt-more a{color:inherit;text-decoration:underline}
            .dkt-more{margin:0;font-size:.82rem;font-weight:700}
            .dkt-more a{color:#0f6b7a;text-decoration:none}
            html.dk-dark .dkt-more a,html.hm-dark .dkt-more a{color:#7fcfdb}
            </style>
            <section class="dkt" aria-label="Công cụ sức khỏe">
                <div class="dkt-head"><h2 class="dkx-h dkt-title">Công cụ sức khỏe</h2><span class="dkt-sub">Tự kiểm tra nhanh, dựa trên hướng dẫn chính thức</span></div>
                <div class="dkt-grid">

                    <div class="dkt-tool" id="dkt-bp">
                        <p class="dkt-kick">Tra huyết áp</p>
                        <h3 class="dkt-name">Huyết áp của bạn ở mức nào?</h3>
                        <div class="dkt-row">
                            <label class="dkt-field">Tâm thu (số trên)<input type="number" inputmode="numeric" min="60" max="260" placeholder="VD: 126" data-sys></label>
                            <label class="dkt-field">Tâm trương (số dưới)<input type="number" inputmode="numeric" min="30" max="160" placeholder="VD: 82" data-dia></label>
                        </div>
                        <div class="dkt-radio" role="radiogroup" aria-label="Nơi đo">
                            <label><input type="radio" name="dkt-where" value="clinic" checked> Đo tại cơ sở y tế</label>
                            <label><input type="radio" name="dkt-where" value="home"> Tự đo tại nhà</label>
                        </div>
                        <div><button type="button" class="dkt-btn" data-go>Xem kết quả</button></div>
                        <div class="dkt-out" aria-live="polite" hidden></div>
                        <p class="dkt-note">Một lần đo chưa đủ để chẩn đoán. Chẩn đoán cần đo nhiều lần, vào các ngày khác nhau. Công cụ không thay thế tư vấn y khoa.</p>
                        <p class="dkt-src">Nguồn: <a href="https://kcb.vn/upload/2005611/20210723//huong_dan_chan_doan_dieu_tri_tha.pdf" target="_blank" rel="noopener">Bộ Y tế (2010)</a>; <a href="https://professional.heart.org/en/science-news/2025-high-blood-pressure-guideline/top-things-to-know" target="_blank" rel="noopener">AHA/ACC (2025)</a>; <a href="https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings" target="_blank" rel="noopener">AHA (2025)</a>.</p>
                        <?php if ( $dkt_bp1 || $dkt_bp2 ) : ?>
                        <p class="dkt-more"><?php if ( $dkt_bp1 ) : ?><a href="<?php echo esc_url( $dkt_bp1 ); ?>">Huyết áp bao nhiêu là cao? →</a><?php endif; ?><?php if ( $dkt_bp1 && $dkt_bp2 ) : ?><br><?php endif; ?><?php if ( $dkt_bp2 ) : ?><a href="<?php echo esc_url( $dkt_bp2 ); ?>">Cách đo huyết áp tại nhà →</a><?php endif; ?></p>
                        <?php endif; ?>
                    </div>

                    <div class="dkt-tool" id="dkt-ss">
                        <p class="dkt-kick">Đường, muối mỗi ngày</p>
                        <h3 class="dkt-name">Hôm nay bạn đã nạp bao nhiêu?</h3>
                        <div class="dkt-tabs" role="tablist">
                            <button type="button" class="dkt-tab" role="tab" aria-selected="true" data-tab="su">Đường</button>
                            <button type="button" class="dkt-tab" role="tab" aria-selected="false" data-tab="sa">Muối</button>
                        </div>

                        <div class="dkt-pane" data-pane="su">
                            <div class="dkt-chips">
                                <button type="button" class="dkt-chip" data-add="40" data-label="Lon nước ngọt có đường (có thể tới 40 g)">+ Lon nước ngọt</button>
                                <button type="button" class="dkt-chip" data-add="47" data-label="Ly trà sữa trân châu cỡ lớn (khoảng 47 g)">+ Ly trà sữa lớn</button>
                                <button type="button" class="dkt-chip" data-add="4" data-label="1 thìa canh tương cà (khoảng 4 g)">+ Thìa tương cà</button>
                            </div>
                            <div class="dkt-row">
                                <label class="dkt-field">Hoặc nhập số gam đường trên nhãn<input type="number" inputmode="decimal" min="0" max="500" step="0.1" placeholder="VD: 12" data-in></label>
                                <div style="align-self:flex-end"><button type="button" class="dkt-btn" data-plus>Thêm</button></div>
                            </div>
                            <ul class="dkt-list" data-list></ul>
                            <div class="dkt-bar" aria-hidden="true"><span></span></div>
                            <div class="dkt-out" aria-live="polite"><p class="dkt-verdict">Tổng: 0 g đường</p><p>Chọn đồ uống, món ăn hoặc nhập số gam trên nhãn.</p></div>
                            <p class="dkt-note">WHO khuyên đường tự do dưới 10% năng lượng, khoảng 50 g/ngày với khẩu phần 2.000 kcal; dưới 25 g có thể có thêm lợi ích. Đường trong trái cây tươi nguyên quả và sữa không tính. Nhãn có thể ghi tổng lượng đường, gồm cả đường có sẵn, nên kết quả chỉ là ước tính. Số liệu trà sữa lấy từ một nghiên cứu nhỏ ở Indonesia, có thể khác ở Việt Nam.</p>
                            <p class="dkt-src">Nguồn: <a href="https://who.int/news/item/04-03-2015-who-calls-on-countries-to-reduce-sugars-intake-among-adults-and-children" target="_blank" rel="noopener">WHO (2015)</a>; <a href="https://www.who.int/news-room/fact-sheets/detail/healthy-diet" target="_blank" rel="noopener">WHO (2026)</a>; <a href="https://doi.org/10.20473/amnt.v6i1SP.2022.171-176" target="_blank" rel="noopener">Veronica và cộng sự (2022)</a>.</p>
                            <?php if ( $dkt_su ) : ?><p class="dkt-more"><a href="<?php echo esc_url( $dkt_su ); ?>">Mỗi ngày nạp bao nhiêu đường là quá nhiều? →</a></p><?php endif; ?>
                        </div>

                        <div class="dkt-pane" data-pane="sa" hidden>
                            <div class="dkt-row">
                                <label class="dkt-field">Nhập lượng natri trên nhãn (mg)<input type="number" inputmode="decimal" min="0" max="20000" step="1" placeholder="VD: 850" data-in></label>
                                <div style="align-self:flex-end"><button type="button" class="dkt-btn" data-plus>Thêm</button></div>
                            </div>
                            <ul class="dkt-list" data-list></ul>
                            <div class="dkt-bar" aria-hidden="true"><span></span></div>
                            <div class="dkt-out" aria-live="polite"><p class="dkt-verdict">Tổng: 0 g muối</p><p>Nhập lượng natri (sodium) ghi trên nhãn từng món đóng gói.</p></div>
                            <p class="dkt-note">WHO khuyên người lớn ăn dưới 5 g muối mỗi ngày, tức dưới 2.000 mg natri; 1 g muối chứa khoảng 400 mg natri. Công cụ chỉ tính món có nhãn. Muối, nước mắm, bột canh, hạt nêm thêm khi nấu và khi ăn, nguồn muối lớn nhất của người Việt, chưa được tính.</p>
                            <p class="dkt-src">Nguồn: <a href="https://www.who.int/news-room/fact-sheets/detail/sodium-reduction" target="_blank" rel="noopener">WHO (2026)</a>; <a href="https://www.who.int/vietnam/vi/news/detail/27-09-2014-world-heart-day-2014-salt-reduction-saves-lives" target="_blank" rel="noopener">WHO Việt Nam (2014)</a>.</p>
                            <?php if ( $dkt_sa || $dkt_lb ) : ?><p class="dkt-more"><?php if ( $dkt_sa ) : ?><a href="<?php echo esc_url( $dkt_sa ); ?>">Người Việt ăn mặn đến mức nào? →</a><?php endif; ?><?php if ( $dkt_sa && $dkt_lb ) : ?><br><?php endif; ?><?php if ( $dkt_lb ) : ?><a href="<?php echo esc_url( $dkt_lb ); ?>">Đọc nhãn dinh dưỡng thế nào cho đúng? →</a><?php endif; ?></p><?php endif; ?>
                        </div>
                        <div><button type="button" class="dkt-btn dkt-btn--ghost" data-reset>Làm lại</button></div>
                    </div>

                </div>
            </section>
            <script>
            (function(){
              function fmt(n,d){return (Math.round(n*Math.pow(10,d))/Math.pow(10,d)).toLocaleString('vi-VN')}
              function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
              /* Tra huyết áp */
              var bp=document.getElementById('dkt-bp');
              if(bp){
                var out=bp.querySelector('.dkt-out');
                bp.querySelector('[data-go]').addEventListener('click',function(){
                  var s=parseFloat(bp.querySelector('[data-sys]').value),d=parseFloat(bp.querySelector('[data-dia]').value);
                  var w=(bp.querySelector('input[name="dkt-where"]:checked')||{}).value||'clinic',h=[];
                  if(!(s>=60&&s<=260&&d>=30&&d<=160)){out.innerHTML='<p>Vui lòng nhập tâm thu từ 60 đến 260 và tâm trương từ 30 đến 160 mmHg.</p>';out.hidden=false;return}
                  if(s<=d){out.innerHTML='<p>Số trên (tâm thu) thường lớn hơn số dưới (tâm trương). Bạn kiểm tra lại giúp nhé.</p>';out.hidden=false;return}
                  if(s>180||d>120){h.push('<p class="dkt-alert">Chỉ số trên 180/120 mmHg. Hãy chờ 1 phút rồi đo lại. Nếu vẫn cao và có đau ngực, khó thở, đau lưng, tê hoặc yếu tay chân, nhìn mờ hay nói khó, gọi 115 ngay. Nếu không có triệu chứng, hãy liên hệ bác sĩ sớm.</p>')}
                  if(w==='home'){
                    if(s>=135||d>=85){h.push('<p class="dkt-verdict is-hi">Từ ngưỡng 135/85 mmHg trở lên khi đo tại nhà</p><p>Theo Bộ Y tế, trung bình nhiều lần tự đo tại nhà từ 135/85 mmHg trở lên là tăng huyết áp. Bạn nên đi khám để được xác nhận và tư vấn.</p>')}
                    else{h.push('<p class="dkt-verdict is-ok">Dưới ngưỡng 135/85 mmHg khi đo tại nhà</p><p>Ngưỡng khi tự đo tại nhà thấp hơn ở cơ sở y tế. Hãy dùng trung bình của nhiều lần đo và tiếp tục theo dõi định kỳ.</p>')}
                  }else{
                    var lv=function(v,c){var t=[[180,110,6],[160,100,5],[140,90,4],[130,85,3],[120,80,2]];for(var i=0;i<t.length;i++){if(v>=t[i][0]||c>=t[i][1])return t[i][2]}return 1}(s,d);
                    var L={1:['Huyết áp tối ưu','is-ok','Dưới 120/80 mmHg. Hãy duy trì lối sống lành mạnh và đo huyết áp định kỳ.'],2:['Huyết áp bình thường','is-ok','Theo Bộ Y tế, tâm thu 120 đến 129 và/hoặc tâm trương 80 đến 84 mmHg là bình thường.'],3:['Tiền tăng huyết áp','is-mid','Chưa tới ngưỡng tăng huyết áp nhưng nên theo dõi thường xuyên và trao đổi với bác sĩ về lối sống, như ăn bớt mặn.'],4:['Tăng huyết áp độ 1','is-hi','Nếu đo nhiều lần, vào các ngày khác nhau vẫn ở mức này, bạn nên đi khám để được chẩn đoán và tư vấn.'],5:['Tăng huyết áp độ 2','is-hi','Nếu đo nhiều lần, vào các ngày khác nhau vẫn ở mức này, bạn nên đi khám để được chẩn đoán và tư vấn.'],6:['Tăng huyết áp độ 3','is-hi','Đây là mức cao nhất trong bảng phân loại. Bạn nên đi khám sớm.']}[lv];
                    h.push('<p class="dkt-verdict '+L[1]+'">'+L[0]+'</p><p>'+L[2]+' Khi hai số rơi vào hai mức khác nhau, Bộ Y tế xếp theo mức cao hơn.</p>');
                    var a=(s>=140||d>=90)?'tăng huyết áp giai đoạn 2':(s>=130||d>=80)?'tăng huyết áp giai đoạn 1':(s>=120)?'huyết áp tăng':'bình thường';
                    h.push('<p>Theo hướng dẫn Hoa Kỳ (AHA/ACC 2025), chỉ số này là <strong>'+a+'</strong>.</p>');
                  }
                  if(s<90||d<60){h.push('<p>Công cụ này không đánh giá huyết áp thấp. Nếu bạn thấy chóng mặt, choáng hoặc mệt nhiều, hãy hỏi ý kiến bác sĩ.</p>')}
                  out.innerHTML=h.join('');out.hidden=false;
                });
              }
              /* Đường, muối */
              var ss=document.getElementById('dkt-ss');
              if(ss){
                var cfg={su:{lim:50,soft:25,unit:'g đường',items:[]},sa:{lim:5,unit:'g muối',items:[]}};
                function render(k){
                  var c=cfg[k],p=ss.querySelector('[data-pane="'+k+'"]'),tot=0;
                  c.items.forEach(function(it){tot+=it.v});
                  p.querySelector('[data-list]').innerHTML=c.items.map(function(it,i){return '<li><span>'+esc(it.l)+'</span><span>'+fmt(it.v,k==='sa'?2:1)+' '+(k==='sa'?'g muối':'g')+' <button type="button" aria-label="Xóa" data-del="'+i+'">×</button></span></li>'}).join('');
                  var pct=Math.min(100,tot/c.lim*100),bar=p.querySelector('.dkt-bar span'),o=p.querySelector('.dkt-out'),v,cls,msg;
                  if(k==='su'){
                    if(!c.items.length){v='Tổng: 0 g đường';cls='';msg='Chọn đồ uống, món ăn hoặc nhập số gam trên nhãn.'}
                    else if(tot<25){cls='is-ok';msg='Dưới 25 g, trong mức WHO cho là có thêm lợi ích.'}
                    else if(tot<50){cls='is-mid';msg='Dưới giới hạn 50 g nhưng đã vượt mức 25 g.'}
                    else{cls='is-hi';msg='Đã chạm hoặc vượt giới hạn 50 g (10% năng lượng với khẩu phần 2.000 kcal).'}
                    if(c.items.length)v='Tổng: '+fmt(tot,1)+' g đường ('+fmt(tot/50*100,0)+'% giới hạn 50 g)';
                  }else{
                    if(!c.items.length){v='Tổng: 0 g muối';cls='';msg='Nhập lượng natri (sodium) ghi trên nhãn từng món đóng gói.'}
                    else{v='Tổng: '+fmt(tot,2)+' g muối ('+fmt(tot*400,0)+' mg natri, '+fmt(tot/5*100,0)+'% giới hạn 5 g)';
                      if(tot<5){cls='is-ok';msg='Chưa tới giới hạn 5 g, nhưng hãy cộng thêm phần gia vị nêm khi nấu và khi ăn.'}
                      else{cls='is-hi';msg='Đã chạm hoặc vượt giới hạn 5 g muối, chưa kể gia vị nêm thêm.'}}
                  }
                  bar.style.width=pct+'%';bar.style.background=cls==='is-hi'?'var(--dkt-hi)':cls==='is-mid'?'var(--dkt-mid)':'var(--dkt-ok)';
                  o.innerHTML='<p class="dkt-verdict '+cls+'">'+v+'</p><p>'+msg+'</p>';
                }
                [].forEach.call(ss.querySelectorAll('.dkt-tab'),function(t){t.addEventListener('click',function(){
                  [].forEach.call(ss.querySelectorAll('.dkt-tab'),function(x){x.setAttribute('aria-selected',x===t?'true':'false')});
                  [].forEach.call(ss.querySelectorAll('.dkt-pane'),function(p){p.hidden=p.getAttribute('data-pane')!==t.getAttribute('data-tab')});
                })});
                [].forEach.call(ss.querySelectorAll('[data-add]'),function(b){b.addEventListener('click',function(){cfg.su.items.push({l:b.getAttribute('data-label'),v:parseFloat(b.getAttribute('data-add'))});render('su')})});
                ['su','sa'].forEach(function(k){
                  var p=ss.querySelector('[data-pane="'+k+'"]'),inp=p.querySelector('[data-in]');
                  function add(){var v=parseFloat(String(inp.value).replace(',','.'));if(!(v>0))return;
                    if(k==='su'){if(v>500)return;cfg.su.items.push({l:'Món từ nhãn',v:v})}else{if(v>20000)return;cfg.sa.items.push({l:'Món từ nhãn ('+fmt(v,0)+' mg natri)',v:v/400})}
                    inp.value='';render(k)}
                  p.querySelector('[data-plus]').addEventListener('click',add);
                  inp.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();add()}});
                  p.querySelector('[data-list]').addEventListener('click',function(e){var i=e.target.getAttribute('data-del');if(i!==null){cfg[k].items.splice(+i,1);render(k)}});
                });
                ss.querySelector('[data-reset]').addEventListener('click',function(){cfg.su.items=[];cfg.sa.items=[];render('su');render('sa')});
              }
            })();
            </script>


    <!-- 1b. GÓC TƯƠNG TÁC: THUẬT NGỮ HÔM NAY + ĐÚNG HAY SAI -->
    <?php
    $dkp_day  = wp_date( 'Ymd' );
    $dkp_pool = get_transient( 'dkp_terms_' . $dkp_day );
    if ( false === $dkp_pool ) {
        $dkp_ids = get_posts( array(
            'post_type'      => 'thuat_ngu',
            'post_status'    => 'publish',
            'posts_per_page' => -1,
            'fields'         => 'ids',
            'no_found_rows'  => true,
            'meta_query'     => array( array( 'key' => '_dktn_reviewed', 'value' => array( '', '0' ), 'compare' => 'NOT IN' ) ),
        ) );
        usort( $dkp_ids, function ( $a, $b ) use ( $dkp_day ) { return strcmp( md5( $a . $dkp_day ), md5( $b . $dkp_day ) ); } );
        $dkp_pool = array();
        foreach ( $dkp_ids as $dkp_id ) {
            $dkp_short = trim( wp_strip_all_tags( (string) get_post_meta( $dkp_id, '_dktn_short', true ) ) );
            if ( '' === $dkp_short ) { continue; }
            $dkp_pool[] = array(
                'n' => preg_replace( '/\s*là gì\??$/u', '', html_entity_decode( get_the_title( $dkp_id ), ENT_QUOTES, 'UTF-8' ) ),
                'd' => $dkp_short,
                'u' => get_permalink( $dkp_id ),
            );
            if ( count( $dkp_pool ) >= 30 ) { break; }
        }
        set_transient( 'dkp_terms_' . $dkp_day, $dkp_pool, DAY_IN_SECONDS );
    }
    $dkp_total = (int) wp_count_posts( 'thuat_ngu' )->publish;

    $dkp_q_raw = array(
        array( 'kem-chong-nang-co-gay-thieu-vitamin-d', 0, 'Bôi kem chống nắng mỗi ngày chắc chắn khiến cơ thể thiếu vitamin D.', 'Một tổng quan hệ thống và một hội đồng chuyên gia quốc tế đều ghi nhận rất ít bằng chứng cho thấy kem chống nắng làm giảm vitamin D trong máu khi dùng trong đời sống thực tế.' ),
        array( 'anh-sang-xanh-co-hai-mat-khong', 0, 'Ánh sáng xanh từ điện thoại, máy tính đã được chứng minh làm tổn thương mắt.', 'Hiện chưa có bằng chứng cho thấy màn hình ở mức dùng bình thường gây hại võng mạc người. Mỏi mắt khi dùng màn hình gắn nhiều với thói quen: chớp mắt ít, nhìn gần lâu, chói sáng.' ),
        array( 'anh-sang-xanh-co-hai-mat-khong', 1, 'Mặt trời là nguồn ánh sáng xanh chính, mạnh hơn nhiều so với màn hình điện thoại.', 'Màn hình cũng phát ánh sáng xanh nhưng độ sáng thấp hơn nhiều so với ánh nắng mặt trời.' ),
        array( 'ngoi-nhieu-co-hai-du-tap-the-duc', 0, 'Đã tập đủ 150 phút mỗi tuần thì ngồi cả ngày cũng không ảnh hưởng đến tim mạch.', 'Một nghiên cứu năm 2024 trên gần 90.000 người cho thấy ngồi hoặc nằm trên khoảng 10,6 giờ mỗi ngày gắn với nguy cơ suy tim và tử vong do tim mạch cao hơn, kể cả ở người đã tập đủ khuyến nghị.' ),
        array( 'sot-xuat-huyet-lan-2-co-nang-hon-khong', 1, 'Sốt xuất huyết lần 2 có thể nặng hơn, nhất là khi nhiễm tuýp virus Dengue khác lần trước.', 'Đúng, nhưng không phải lần tái nhiễm nào cũng nặng. Cần theo dõi sát, đặc biệt khi bắt đầu hạ sốt, và đi khám ngay nếu có dấu hiệu cảnh báo.' ),
        array( 'bam-nut-hoan-bao-thuc-ngu-them-5-phut-co-tot', 0, 'Bấm báo lại (snooze) 30 phút chắc chắn làm hỏng giấc ngủ và khiến đầu óc kém đi.', 'Một thí nghiệm năm 2024 ở người quen báo lại cho thấy báo lại 30 phút chỉ mất khoảng 6 phút ngủ và không làm kết quả kiểm tra nhận thức kém đi. Cách bền vững vẫn là ngủ đủ từ 7 giờ mỗi đêm.' ),
        array( 'mot-nghien-cuu-moi-co-du-de-ket-luan', 0, 'Một nghiên cứu mới được đăng báo là đủ để kết luận một điều là đúng.', 'Một nghiên cứu đơn lẻ chỉ là một mảnh ghép. Kết luận vững chắc thường đến từ nhiều nghiên cứu độc lập cho kết quả nhất quán, được tổng hợp có hệ thống.' ),
        array( 'dinh-chinh-tin-sai-khong-hieu-qua', 0, 'Chỉ cần đính chính, người đọc sẽ thôi tin vào thông tin sai.', 'Đính chính thường có tác dụng nhưng hiếm khi xóa sạch ảnh hưởng. Nhiều người vẫn dựa vào tin sai khi suy luận, gọi là hiệu ứng ảnh hưởng kéo dài.' ),
        array( 'nhin-an-gian-doan-giam-can-hieu-qua', 0, 'Nhịn ăn gián đoạn giúp giảm cân vượt trội so với ăn kiêng giảm calo thông thường.', 'Nhịn ăn gián đoạn có giúp giảm cân, nhưng các tổng quan cho thấy hiệu quả tương đương hoặc chỉ nhỉnh hơn chút ít so với ăn kiêng thông thường.' ),
        array( 'cam-giac-suong-mu-nao-sau-ngay-dai-lam-viec', 0, '"Sương mù não" là một chẩn đoán y khoa.', 'Sương mù não là cách mô tả triệu chứng như đầu óc chậm, khó tập trung, hay quên. Nó xuất hiện trong nhiều tình trạng khác nhau, không phải một bệnh riêng.' ),
        array( 'ngu-bu-cuoi-tuan-co-hieu-qua-khong', 0, 'Nghiên cứu đã chứng minh ngủ bù cuối tuần giúp ngăn ngừa bệnh tật.', 'Bằng chứng hiện còn trái chiều và chủ yếu cho thấy sự liên quan, chưa đủ để nói ngủ bù cuối tuần trực tiếp gây ra hay ngăn ngừa vấn đề sức khỏe.' ),
    );
    $dkp_q = array();
    foreach ( $dkp_q_raw as $dkp_r ) {
        $dkp_p = get_page_by_path( $dkp_r[0], OBJECT, 'post' );
        if ( ! $dkp_p || 'publish' !== $dkp_p->post_status ) { continue; }
        $dkp_q[] = array( 'q' => $dkp_r[2], 'a' => $dkp_r[1], 'w' => $dkp_r[3], 'u' => get_permalink( $dkp_p ) );
    }
    $dkp_doy = (int) floor( time() / DAY_IN_SECONDS );
    $dkp_t0  = $dkp_pool ? $dkp_pool[0] : null;
    $dkp_q0  = $dkp_q ? $dkp_q[ $dkp_doy % count( $dkp_q ) ] : null;
    if ( $dkp_t0 || $dkp_q0 ) :
    ?>
    <style>
    .dkp{margin:22px 0 6px;--dkp-card:#fff;--dkp-line:rgba(1,42,26,.12);--dkp-ink:#13261c;--dkp-mute:#4f6157;--dkp-acc:#0f6b7a;--dkp-btn:#012a1a;--dkp-btn-ink:#fff;--dkp-ok:#1f7a45;--dkp-no:#b23a26;--dkp-soft:rgba(15,107,122,.07)}
    html.dk-dark .dkp{--dkp-card:rgba(255,255,255,.035);--dkp-line:rgba(255,255,255,.09);--dkp-ink:#d6ddd8;--dkp-mute:#9fb0a6;--dkp-acc:#7fcfdb;--dkp-btn:#d8ef6b;--dkp-btn-ink:#012a1a;--dkp-ok:#6fd39a;--dkp-no:#f0957f;--dkp-soft:rgba(127,207,219,.08)}
    .dkp-head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin:0 0 12px}
    .dkp-kick{font-size:.7rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--dkp-acc)}
    .dkp-title{font-family:Newsreader,Georgia,serif;font-weight:800;font-size:1.35rem;margin:0;color:var(--dkp-ink)}
    .dkp-grid{display:grid;grid-template-columns:1fr;gap:14px}
    @media (min-width:760px){.dkp-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
    .dkp-card{background:var(--dkp-card);border:1px solid var(--dkp-line);border-radius:24px;padding:20px 22px;color:var(--dkp-ink);display:flex;flex-direction:column;gap:10px;min-width:0}
    .dkp-label{margin:0;font-size:.72rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--dkp-acc)}
    .dkp-term__name{font-family:Newsreader,Georgia,serif;font-size:1.45rem;line-height:1.25;margin:0}
    .dkp-term__name a{color:inherit;text-decoration:none}
    .dkp-term__name a:hover{text-decoration:underline}
    .dkp-term__def,.dkp-q__text,.dkp-q__why{margin:0;line-height:1.6;color:var(--dkp-ink)}
    .dkp-q__text{font-family:Newsreader,Georgia,serif;font-size:1.2rem;font-weight:700;line-height:1.4}
    .dkp-actions,.dkp-q__btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:auto}
    .dkp-q__btns{margin-top:4px}
    .dkp-btn{appearance:none;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;border-radius:999px;padding:9px 18px;font:700 .88rem/1.2 inherit;font-family:inherit;text-decoration:none;border:1px solid var(--dkp-btn);background:var(--dkp-btn);color:var(--dkp-btn-ink)}
    .dkp-btn--ghost{background:transparent;color:var(--dkp-ink);border-color:var(--dkp-line)}
    .dkp-btn:hover{filter:brightness(1.08)}
    .dkp-btn:focus-visible{outline:2px solid var(--dkp-acc);outline-offset:2px}
    .dkp-q__btns .dkp-btn{min-width:96px}
    .dkp-q__btns .dkp-btn[disabled]{opacity:.5;cursor:default}
    .dkp-q__out{background:var(--dkp-soft);border-radius:16px;padding:12px 14px;display:flex;flex-direction:column;gap:8px}
    .dkp-q__out[hidden]{display:none}
    .dkp-q__verdict{margin:0;font-weight:800}
    .dkp-q__verdict.is-ok{color:var(--dkp-ok)}
    .dkp-q__verdict.is-no{color:var(--dkp-no)}
    .dkp-foot,.dkp-note{margin:0;font-size:.82rem;color:var(--dkp-mute)}
    .dkp-foot a{color:var(--dkp-acc);font-weight:700;text-decoration:none}
    .dkp-foot a:hover{text-decoration:underline}
    </style>
    <section class="dkp" aria-label="Góc tương tác">
        <div class="dkp-head">
            <span class="dkp-kick">Góc tương tác</span>
            <h2 class="dkp-title">Mỗi ngày hiểu thêm một điều</h2>
        </div>
        <div class="dkp-grid">
            <?php if ( $dkp_t0 ) : ?>
            <article class="dkp-card dkp-term" id="dkp-term">
                <p class="dkp-label">Thuật ngữ hôm nay</p>
                <h3 class="dkp-term__name"><a href="<?php echo esc_url( $dkp_t0['u'] ); ?>"><?php echo esc_html( $dkp_t0['n'] ); ?></a></h3>
                <p class="dkp-term__def"><?php echo esc_html( $dkp_t0['d'] ); ?></p>
                <div class="dkp-actions">
                    <a class="dkp-btn dkp-term__link" href="<?php echo esc_url( $dkp_t0['u'] ); ?>">Đọc giải thích</a>
                    <?php if ( count( $dkp_pool ) > 1 ) : ?><button type="button" class="dkp-btn dkp-btn--ghost" data-dkp-next>Thuật ngữ khác</button><?php endif; ?>
                </div>
                <p class="dkp-foot"><a href="<?php echo esc_url( home_url( '/thuat-ngu/' ) ); ?>">Xem toàn bộ <?php echo esc_html( number_format_i18n( $dkp_total ) ); ?> thuật ngữ →</a></p>
                <script type="application/json" class="dkp-data"><?php echo wp_json_encode( $dkp_pool, JSON_UNESCAPED_UNICODE | JSON_HEX_TAG ); ?></script>
            </article>
            <?php endif; ?>
            <?php if ( $dkp_q0 ) : ?>
            <article class="dkp-card dkp-quiz" id="dkp-quiz">
                <p class="dkp-label">Đúng hay sai?</p>
                <p class="dkp-q__text"><?php echo esc_html( $dkp_q0['q'] ); ?></p>
                <div class="dkp-q__btns">
                    <button type="button" class="dkp-btn dkp-btn--ghost" data-dkp-a="1">Đúng</button>
                    <button type="button" class="dkp-btn dkp-btn--ghost" data-dkp-a="0">Sai</button>
                </div>
                <div class="dkp-q__out" aria-live="polite" hidden>
                    <p class="dkp-q__verdict"></p>
                    <p class="dkp-q__why"></p>
                    <div class="dkp-actions">
                        <a class="dkp-btn dkp-q__link" href="<?php echo esc_url( $dkp_q0['u'] ); ?>">Đọc bài đầy đủ</a>
                        <button type="button" class="dkp-btn dkp-btn--ghost" data-dkp-next>Câu tiếp theo</button>
                    </div>
                </div>
                <p class="dkp-foot dkp-q__score" aria-live="polite"></p>
                <p class="dkp-note">Thông tin mang tính tham khảo, không thay thế tư vấn y khoa cho từng cá nhân.</p>
                <script type="application/json" class="dkp-data"><?php echo wp_json_encode( array( 'start' => $dkp_doy % count( $dkp_q ), 'items' => $dkp_q ), JSON_UNESCAPED_UNICODE | JSON_HEX_TAG ); ?></script>
            </article>
            <?php endif; ?>
        </div>
    </section>
    <script>
    (function(){
      function data(el){try{return JSON.parse(el.querySelector('.dkp-data').textContent)}catch(e){return null}}
      var t=document.getElementById('dkp-term');
      if(t){var tp=data(t),ti=0,nb=t.querySelector('[data-dkp-next]');
        if(tp&&tp.length>1&&nb){nb.addEventListener('click',function(){ti=(ti+1)%tp.length;var x=tp[ti];var a=t.querySelector('.dkp-term__name a');a.textContent=x.n;a.href=x.u;t.querySelector('.dkp-term__def').textContent=x.d;t.querySelector('.dkp-term__link').href=x.u;});}
      }
      var q=document.getElementById('dkp-quiz');
      if(q){var qd=data(q);if(!qd||!qd.items||!qd.items.length)return;
        var it=qd.items,qi=qd.start||0,btns=[].slice.call(q.querySelectorAll('[data-dkp-a]')),out=q.querySelector('.dkp-q__out'),ver=q.querySelector('.dkp-q__verdict'),why=q.querySelector('.dkp-q__why'),lnk=q.querySelector('.dkp-q__link'),sc=q.querySelector('.dkp-q__score'),K='dkp_quiz_v1',st={r:0,n:0};
        try{var s=JSON.parse(localStorage.getItem(K)||'null');if(s&&typeof s.r==='number')st=s}catch(e){}
        function score(){sc.textContent=st.n?('Bạn đã trả lời đúng '+st.r+'/'+st.n+' câu.'):'';}
        function show(){var x=it[qi];q.querySelector('.dkp-q__text').textContent=x.q;out.hidden=true;btns.forEach(function(b){b.disabled=false});lnk.href=x.u;}
        btns.forEach(function(b){b.addEventListener('click',function(){var x=it[qi],ok=String(x.a)===b.getAttribute('data-dkp-a');ver.textContent=(ok?'Chính xác! ':'Chưa đúng. ')+'Nhận định này '+(x.a?'ĐÚNG.':'SAI.');ver.className='dkp-q__verdict '+(ok?'is-ok':'is-no');why.textContent=x.w;lnk.href=x.u;out.hidden=false;btns.forEach(function(y){y.disabled=true});st.n++;if(ok)st.r++;try{localStorage.setItem(K,JSON.stringify(st))}catch(e){}score();});});
        q.querySelector('[data-dkp-next]').addEventListener('click',function(){qi=(qi+1)%it.length;show();q.querySelector('.dkp-q__text').focus&&0;});
        score();
      }
    })();
    </script>
    <?php endif; ?>


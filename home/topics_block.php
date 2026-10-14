    <?php
    /* Dải chuyên đề đứng yên: 1 banner chuyên đề gần nhất + thẻ nhỏ các chuyên đề còn lại */
    $dk_topics = array();
    if ( $dk_dq_on ) {
        $dk_topics[] = array( 'end' => '2026-10-29', 'cls' => 'blh-banner--dq', 'url' => home_url( '/ngay-dot-quy-the-gioi/' ), 'img' => content_url( '/uploads/2026/10/ngay-dot-quy-the-gioi-banner.webp' ), 'alt' => 'Minh họa đồng hồ, hình bộ não, điện thoại gọi 115 và giường nghỉ, ảnh bìa chuyên đề Ngày Đột quỵ Thế giới', 'eyebrow' => 'Chuyên đề 29/10 · Ngày Đột quỵ Thế giới', 'title' => 'Nhận ra sớm, <em>gọi 115 ngay</em>', 'plain' => 'Nhận ra sớm, gọi 115 ngay', 'lede' => 'Bài viết và công cụ tương tác giúp bạn nhận biết dấu hiệu đột quỵ, hành động đúng trong những phút đầu và kiểm soát huyết áp mỗi ngày.', 'pos' => '100% 30%' );
    }
    if ( $dk_vvt_on ) {
        $dk_topics[] = array( 'end' => '2026-11-19', 'cls' => 'blh-banner--vvt', 'url' => home_url( '/vung-vang-tu-ben-trong/' ), 'img' => content_url( '/uploads/2026/10/vung-vang-tu-ben-trong-banner-v3.webp' ), 'alt' => 'Tranh người đàn ông chèo thuyền đơn trên sông của Thomas Eakins', 'eyebrow' => 'Chuyên đề 19/11 · Dy Khoa Blog', 'title' => 'Vững vàng <em>từ bên trong</em>', 'plain' => 'Vững vàng từ bên trong', 'lede' => 'Bài viết dựa trên bằng chứng và công cụ tương tác về sức khỏe thể chất, sức khỏe tinh thần và những vai trò đang thay đổi của nam giới.', 'pos' => '70% 40%' );
    }
    if ( $dk_kctt_on ) {
        $dk_topics[] = array( 'end' => '', 'cls' => 'blh-banner--kctt', 'url' => home_url( '/kiem-chung-thong-tin-khoa-hoc/' ), 'img' => content_url( '/uploads/2026/10/kiem-chung-thong-tin-khoa-hoc-banner-v3.webp' ), 'alt' => 'Minh họa bàn làm việc kiểm chứng thông tin: bài báo khoa học, kính lúp, điện thoại có bài đăng bị gắn cảnh báo và sổ ghi các bước kiểm tra', 'eyebrow' => 'Chuyên đề · Đồng hành cùng Lá Chắn Thông Tin', 'title' => 'Kiểm chứng <em>thông tin khoa học</em>', 'plain' => 'Kiểm chứng thông tin khoa học', 'lede' => 'Cách đọc, kiểm chứng và chia sẻ thông tin khoa học, sức khỏe trên mạng: dừng lại, tra nguồn, rồi mới chia sẻ.', 'pos' => '80% 40%' );
    }
    $dk_topics[] = array( 'end' => '2026-10-20', 'cls' => '', 'url' => home_url( '/ban-linh-diu-dang/' ), 'img' => content_url( '/uploads/2026/10/ban-linh-diu-dang-banner.webp' ), 'alt' => 'Tranh minh họa ba thế hệ phụ nữ Việt Nam thong thả đi dạo bên đầm sen lúc bình minh', 'eyebrow' => 'Chuyên đề 20/10 · Dy Khoa Blog', 'title' => 'Bản lĩnh <em>dịu dàng</em>', 'plain' => 'Bản lĩnh dịu dàng', 'lede' => 'Bài viết dựa trên bằng chứng và công cụ tương tác về sức khỏe, tâm trí, khoa học, truyền thông, nghề nghiệp và góc nhìn của phụ nữ.', 'pos' => '72% 30%' );

    /* Thứ tự: chuyên đề có ngày sắp tới (gần nhất trước), rồi chuyên đề thường trực, rồi chuyên đề đã qua (mới nhất trước) */
    $dk_today = wp_date( 'Y-m-d' );
    usort( $dk_topics, function ( $a, $b ) use ( $dk_today ) {
        $ra = '' === $a['end'] ? 1 : ( $a['end'] >= $dk_today ? 0 : 2 );
        $rb = '' === $b['end'] ? 1 : ( $b['end'] >= $dk_today ? 0 : 2 );
        if ( $ra !== $rb ) { return $ra - $rb; }
        if ( 0 === $ra ) { return strcmp( $a['end'], $b['end'] ); }
        if ( 2 === $ra ) { return strcmp( $b['end'], $a['end'] ); }
        return 0;
    } );
    $dk_feat  = array_shift( $dk_topics );
    $dk_cards = array_slice( $dk_topics, 0, 3 );
    ?>
    <style>
    .blh-home .blh-more{margin-top:18px}
    .blh-more__head{margin:0 0 10px;font-size:.72rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--dk-muted)}
    .blh-more__grid{display:grid;grid-template-columns:1fr;gap:12px}
    @media (min-width:721px){.blh-more__grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}}
    .blh-card{display:grid;grid-template-columns:112px minmax(0,1fr);gap:12px;align-items:center;text-decoration:none!important;color:var(--dk-ink)}
    @media (min-width:721px){.blh-card{grid-template-columns:120px minmax(0,1fr)}}
    .blh-card__img{width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:6px;display:block;margin:0;background:#f3f0e9}
    .blh-card__eyebrow{display:block;font-size:.66rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--dk-muted);margin-bottom:3px}
    .blh-card__title{display:block;font-family:var(--dk-serif);font-weight:700;font-size:1.02rem;line-height:1.3;color:var(--dk-ink)}
    .blh-card:hover .blh-card__title{text-decoration:underline}
    </style>
    <div class="blh-home">
      <a class="blh-banner <?php echo esc_attr( $dk_feat['cls'] ); ?>" href="<?php echo esc_url( $dk_feat['url'] ); ?>" aria-label="<?php echo esc_attr( 'Khám phá chuyên đề: ' . $dk_feat['plain'] ); ?>">
        <img class="blh-banner__img" src="<?php echo esc_url( $dk_feat['img'] ); ?>" alt="<?php echo esc_attr( $dk_feat['alt'] ); ?>" width="2400" height="1200" loading="lazy" decoding="async">
        <span class="blh-banner__text">
          <span class="blh-banner__eyebrow"><?php echo esc_html( $dk_feat['eyebrow'] ); ?></span>
          <span class="blh-banner__title"><?php echo wp_kses( $dk_feat['title'], array( 'em' => array() ) ); ?></span>
          <span class="blh-banner__lede"><?php echo esc_html( $dk_feat['lede'] ); ?></span>
          <span class="blh-btn">Khám phá chuyên đề</span>
        </span>
      </a>
      <?php if ( $dk_cards ) : ?>
      <div class="blh-more" aria-label="Các chuyên đề khác">
        <p class="blh-more__head">Các chuyên đề khác</p>
        <div class="blh-more__grid">
          <?php foreach ( $dk_cards as $dk_c ) : ?>
          <a class="blh-card" href="<?php echo esc_url( $dk_c['url'] ); ?>">
            <img class="blh-card__img" src="<?php echo esc_url( $dk_c['img'] ); ?>" alt="" width="240" height="150" loading="lazy" decoding="async" style="object-position:<?php echo esc_attr( $dk_c['pos'] ); ?>">
            <span><span class="blh-card__eyebrow"><?php echo esc_html( $dk_c['eyebrow'] ); ?></span><span class="blh-card__title"><?php echo esc_html( $dk_c['plain'] ); ?></span></span>
          </a>
          <?php endforeach; ?>
        </div>
      </div>
      <?php endif; ?>
    </div>

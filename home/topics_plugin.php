

/* =========================================================
 * Chuyên đề: danh sách dùng chung cho trang chủ và trang /chuyen-de/ (14/10/2026)
 * ========================================================= */
if ( ! function_exists( 'dk_topics_list' ) ) {
    function dk_topics_list( $preview = false ) {
        $all = array(
            array( 'slug' => 'ngay-dot-quy-the-gioi', 'end' => '2026-10-29', 'cls' => 'blh-banner--dq', 'img' => '/uploads/2026/10/ngay-dot-quy-the-gioi-banner.webp', 'alt' => 'Minh họa đồng hồ, hình bộ não, điện thoại gọi 115 và giường nghỉ, ảnh bìa chuyên đề Ngày Đột quỵ Thế giới', 'eyebrow' => 'Chuyên đề 29/10 · Ngày Đột quỵ Thế giới', 'title' => 'Nhận ra sớm, <em>gọi 115 ngay</em>', 'plain' => 'Nhận ra sớm, gọi 115 ngay', 'lede' => 'Bài viết và công cụ tương tác giúp bạn nhận biết dấu hiệu đột quỵ, hành động đúng trong những phút đầu và kiểm soát huyết áp mỗi ngày.', 'pos' => '100% 30%' ),
            array( 'slug' => 'vung-vang-tu-ben-trong', 'end' => '2026-11-19', 'cls' => 'blh-banner--vvt', 'img' => '/uploads/2026/10/vung-vang-tu-ben-trong-banner-v3.webp', 'alt' => 'Tranh người đàn ông chèo thuyền đơn trên sông của Thomas Eakins', 'eyebrow' => 'Chuyên đề 19/11 · Dy Khoa Blog', 'title' => 'Vững vàng <em>từ bên trong</em>', 'plain' => 'Vững vàng từ bên trong', 'lede' => 'Bài viết dựa trên bằng chứng và công cụ tương tác về sức khỏe thể chất, sức khỏe tinh thần và những vai trò đang thay đổi của nam giới.', 'pos' => '70% 40%' ),
            array( 'slug' => 'kiem-chung-thong-tin-khoa-hoc', 'end' => '', 'cls' => 'blh-banner--kctt', 'img' => '/uploads/2026/10/kiem-chung-thong-tin-khoa-hoc-banner-v3.webp', 'alt' => 'Minh họa bàn làm việc kiểm chứng thông tin: bài báo khoa học, kính lúp, điện thoại có bài đăng bị gắn cảnh báo và sổ ghi các bước kiểm tra', 'eyebrow' => 'Chuyên đề · Đồng hành cùng Lá Chắn Thông Tin', 'title' => 'Kiểm chứng <em>thông tin khoa học</em>', 'plain' => 'Kiểm chứng thông tin khoa học', 'lede' => 'Cách đọc, kiểm chứng và chia sẻ thông tin khoa học, sức khỏe trên mạng: dừng lại, tra nguồn, rồi mới chia sẻ.', 'pos' => '80% 40%' ),
            array( 'slug' => 'ban-linh-diu-dang', 'end' => '2026-10-20', 'cls' => '', 'img' => '/uploads/2026/10/ban-linh-diu-dang-banner.webp', 'alt' => 'Tranh minh họa ba thế hệ phụ nữ Việt Nam thong thả đi dạo bên đầm sen lúc bình minh', 'eyebrow' => 'Chuyên đề 20/10 · Dy Khoa Blog', 'title' => 'Bản lĩnh <em>dịu dàng</em>', 'plain' => 'Bản lĩnh dịu dàng', 'lede' => 'Bài viết dựa trên bằng chứng và công cụ tương tác về sức khỏe, tâm trí, khoa học, truyền thông, nghề nghiệp và góc nhìn của phụ nữ.', 'pos' => '72% 30%' ),
        );
        $today = wp_date( 'Y-m-d' );
        $out   = array();
        foreach ( $all as $t ) {
            $p = get_page_by_path( $t['slug'] );
            if ( ! $p || ( 'publish' !== $p->post_status && ! $preview ) ) { continue; }
            $t['url']  = home_url( '/' . $t['slug'] . '/' );
            $t['img']  = content_url( $t['img'] );
            $t['rank'] = '' === $t['end'] ? 1 : ( $t['end'] >= $today ? 0 : 2 );
            $out[]     = $t;
        }
        usort( $out, function ( $a, $b ) {
            if ( $a['rank'] !== $b['rank'] ) { return $a['rank'] - $b['rank']; }
            if ( 0 === $a['rank'] ) { return strcmp( $a['end'], $b['end'] ); }
            if ( 2 === $a['rank'] ) { return strcmp( $b['end'], $a['end'] ); }
            return 0;
        } );
        return $out;
    }
}

if ( ! function_exists( 'dk_topics_shortcode' ) ) {
    function dk_topics_shortcode() {
        $list = dk_topics_list( false );
        if ( ! $list ) { return ''; }
        ob_start();
        ?>
        <style>
        .dkc{display:grid;grid-template-columns:1fr;gap:28px;margin:8px 0 24px}
        @media (min-width:720px){.dkc{grid-template-columns:repeat(2,minmax(0,1fr))}}
        .dkc-item{display:flex;flex-direction:column;gap:8px;text-decoration:none!important;color:inherit}
        .dkc-item img{width:100%;aspect-ratio:2/1;object-fit:cover;border-radius:6px;display:block;margin:0}
        .dkc-status{font-size:.7rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#a4504c}
        .dkc-status.is-past{color:#6b746f}
        .dkc-title{font-family:"Newsreader",Georgia,serif;font-weight:800;font-size:1.4rem;line-height:1.25;margin:0}
        .dkc-item:hover .dkc-title{text-decoration:underline}
        .dkc-lede{margin:0;font-size:.95rem;line-height:1.6;opacity:.85}
        </style>
        <div class="dkc">
        <?php foreach ( $list as $t ) :
            if ( 1 === $t['rank'] ) {
                $st = 'Thường trực';
            } elseif ( 0 === $t['rank'] ) {
                $st = ( wp_date( 'Y-m-d' ) === $t['end'] ? 'Hôm nay · ' : 'Sắp diễn ra · ' ) . wp_date( 'd/m', strtotime( $t['end'] ) );
            } else {
                $st = 'Đã diễn ra · ' . wp_date( 'd/m/Y', strtotime( $t['end'] ) );
            }
            ?>
            <a class="dkc-item" href="<?php echo esc_url( $t['url'] ); ?>">
                <img src="<?php echo esc_url( $t['img'] ); ?>" alt="<?php echo esc_attr( $t['alt'] ); ?>" width="1200" height="600" loading="lazy" decoding="async" style="object-position:<?php echo esc_attr( $t['pos'] ); ?>">
                <span class="dkc-status<?php echo 2 === $t['rank'] ? ' is-past' : ''; ?>"><?php echo esc_html( $st ); ?></span>
                <h2 class="dkc-title"><?php echo esc_html( $t['plain'] ); ?></h2>
                <p class="dkc-lede"><?php echo esc_html( $t['lede'] ); ?></p>
            </a>
        <?php endforeach; ?>
        </div>
        <?php
        return ob_get_clean();
    }
    add_shortcode( 'dk_chuyen_de', 'dk_topics_shortcode' );
}

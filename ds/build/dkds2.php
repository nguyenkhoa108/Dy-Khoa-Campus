
/* ---------------------------------------------------------
 * ĐỌC SÂU: trang mục /category/doc-sau/ + dải trang chủ + nhãn bìa (21/10/2026)
 * --------------------------------------------------------- */
if ( ! function_exists( 'dkds_posts' ) ) {
    function dkds_posts() {
        static $ids = null;
        if ( null === $ids ) {
            $ids = get_posts( array( 'post_type' => 'post', 'category_name' => 'doc-sau', 'posts_per_page' => -1, 'fields' => 'ids', 'orderby' => 'date', 'order' => 'DESC', 'ignore_sticky_posts' => true, 'no_found_rows' => true ) );
            $ids = array_map( 'intval', $ids );
        }
        return $ids;
    }
    function dkds_no( $id ) {
        $ids = array_reverse( dkds_posts() );
        $i   = array_search( (int) $id, $ids, true );
        return false === $i ? '' : sprintf( '%02d', $i + 1 );
    }
    function dkds_meta( $id ) {
        $out = array();
        if ( function_exists( 'dkx_byline' ) && preg_match( '/(?<!\d)(\d{1,3})\s*phút đọc/u', preg_replace( '/<[^>]*>/', ' ', dkx_byline( $id, true ) ), $m ) ) {
            $out[] = $m[1] . ' phút đọc';
        }
        $ch = substr_count( (string) get_post_field( 'post_content', $id ), 'class="ds-op"' );
        if ( $ch ) { $out[] = $ch . ' chương'; }
        return implode( ' · ', $out );
    }
    function dkds_deck( $id ) {
        return function_exists( 'dkx_deck' ) ? dkx_deck( $id ) : get_the_excerpt( $id );
    }
    function dkds_img( $id, $size = 'large' ) {
        $u = get_the_post_thumbnail_url( $id, $size );
        return $u ? '<img src="' . esc_url( $u ) . '" alt="" loading="lazy" decoding="async">' : '';
    }
    function dkds_icon( $s = 15 ) {
        return '<svg viewBox="0 0 24 24" width="' . (int) $s . '" height="' . (int) $s . '" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M12 3 3 8l9 5 9-5-9-5z"/><path d="m3 12.5 9 5 9-5"/><path d="m3 17 9 5 9-5"/></svg>';
    }
    function dkds_url() {
        $t = get_category_by_slug( 'doc-sau' );
        return $t ? get_category_link( $t ) : home_url( '/category/doc-sau/' );
    }
    function dkds_kicker() {
        return '<a class="dsk" href="' . esc_url( dkds_url() ) . '"><i></i>' . dkds_icon( 15 ) . 'Đọc Sâu</a>';
    }
    /* Bài cho dải trang chủ: bài Đọc Sâu mới nhất không trùng bài bìa */
    function dkds_band_id( $cover_id ) {
        foreach ( dkds_posts() as $id ) { if ( $id !== (int) $cover_id ) { return $id; } }
        return 0;
    }
    function dkds_band( $id ) {
        $u = esc_url( get_permalink( $id ) );
        $d = dkds_deck( $id );
        ob_start(); ?>
<section class="dsb" aria-label="Đọc Sâu">
  <div class="dsb-h"><a href="<?php echo esc_url( dkds_url() ); ?>"><img src="https://dykhoa.com/blog/wp-content/uploads/2026/10/doc-sau-logo-trang.png" alt="Đọc Sâu" width="170" height="45"></a><a class="dsb-all" href="<?php echo esc_url( dkds_url() ); ?>">Tất cả bài Đọc Sâu</a></div>
  <div class="dsb-g">
    <a class="dsb-img" href="<?php echo $u; ?>" tabindex="-1" aria-hidden="true"><?php echo dkds_img( $id ); ?></a>
    <div>
      <p class="dsb-no"><?php echo esc_html( dkds_no( $id ) ); ?></p>
      <h3 class="dsb-t"><a href="<?php echo $u; ?>"><?php echo esc_html( get_the_title( $id ) ); ?></a></h3>
      <?php if ( $d ) : ?><p class="dsb-d"><?php echo esc_html( $d ); ?></p><?php endif; ?>
      <p class="dsb-m"><?php echo esc_html( dkds_meta( $id ) ); ?></p>
      <a class="dsb-btn" href="<?php echo $u; ?>">Bắt đầu đọc</a>
    </div>
  </div>
</section>
<?php
        return ob_get_clean();
    }
    function dkds_archive() {
        $ids  = dkds_posts();
        $feat = $ids ? $ids[0] : 0;
        $rest = array_slice( $ids, 1 );
        ob_start(); ?>
<main id="primary" class="site-main dkx-main dsa">
  <header class="dsa-full dsa-mast"><div class="dsa-in">
    <h1 class="dsa-h1"><img src="https://dykhoa.com/blog/wp-content/uploads/2026/10/doc-sau-logo-trang.png" alt="Đọc Sâu" width="360" height="95"></h1>
    <p class="dsa-tag">Những bài viết dài đi đến tận gốc một vấn đề khoa học, có nguồn kiểm chứng cho từng nhận định.</p>
    <ul class="dsa-std"><li>Nguồn gốc cho từng nhận định</li><li>Hình minh hoạ dựng riêng</li><li>Chia chương, đọc theo nhịp</li></ul>
  </div></header>
  <?php if ( $feat ) : $u = esc_url( get_permalink( $feat ) ); $d = dkds_deck( $feat ); ?>
  <section class="dsa-full dsa-feat"><div class="dsa-in dsa-fg">
    <div>
      <p class="dsa-no"><?php echo esc_html( dkds_no( $feat ) ); ?></p>
      <p class="dsa-lab">Mới nhất</p>
      <h2 class="dsa-t"><a href="<?php echo $u; ?>"><?php echo esc_html( get_the_title( $feat ) ); ?></a></h2>
      <?php if ( $d ) : ?><p class="dsa-d"><?php echo esc_html( $d ); ?></p><?php endif; ?>
      <p class="dsa-meta"><?php echo esc_html( trim( get_the_author_meta( 'display_name', get_post_field( 'post_author', $feat ) ) . ' · ' . get_the_date( 'd/m/Y', $feat ) . ' · ' . dkds_meta( $feat ), ' ·' ) ); ?></p>
      <a class="dsa-btn" href="<?php echo $u; ?>">Bắt đầu đọc</a>
    </div>
    <a class="dsa-img" href="<?php echo $u; ?>" tabindex="-1" aria-hidden="true"><?php echo dkds_img( $feat ); ?></a>
  </div></section>
  <?php endif; ?>
  <?php if ( $rest ) : ?>
  <section class="dsa-list"><div class="dsa-in">
    <h2 class="dsa-lh">Các số trước</h2>
    <?php foreach ( $rest as $id ) : $u = esc_url( get_permalink( $id ) ); $d = dkds_deck( $id ); ?>
    <article class="dsa-row">
      <span class="dsa-rn"><?php echo esc_html( dkds_no( $id ) ); ?></span>
      <div><h3><a href="<?php echo $u; ?>"><?php echo esc_html( get_the_title( $id ) ); ?></a></h3><?php if ( $d ) : ?><p><?php echo esc_html( $d ); ?></p><?php endif; ?><small><?php echo esc_html( get_the_date( 'd/m/Y', $id ) . ' · ' . dkds_meta( $id ) ); ?></small></div>
      <a class="dsa-rimg" href="<?php echo $u; ?>" tabindex="-1" aria-hidden="true"><?php echo dkds_img( $id, 'medium_large' ); ?></a>
    </article>
    <?php endforeach; ?>
  </div></section>
  <?php endif; ?>
</main>
<?php
        return ob_get_clean();
    }
    function dkds2_css() {
        return <<<'CSS'
.dsk{display:inline-flex;align-items:center;gap:6px;font:800 12px/1.2 "Be Vietnam Pro",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#1f4b3a;text-decoration:none;margin-bottom:6px}.dsk i{display:inline-block;width:18px;height:2px;background:#c4554b}html.dk-dark .dsk,html.hm-dark .dsk{color:#cfe3d6}
.dsb{width:100vw;margin:10px 0 34px calc(50% - 50vw);background:#0c1712;color:#f4efe4;padding:40px 0 44px;position:relative;overflow:hidden;font-family:"Be Vietnam Pro",sans-serif;box-sizing:border-box}
.dsb:after{content:"";position:absolute;right:-120px;top:-120px;width:420px;height:420px;background:radial-gradient(closest-side,rgba(196,85,75,.25),transparent);pointer-events:none}
.dsb>*{max-width:1180px;margin-left:auto;margin-right:auto;padding:0 24px;box-sizing:border-box;position:relative;z-index:1}
.dsb-h{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:28px}.dsb-h img{height:44px;width:auto;display:block}
.dsb .dsb-all{color:#cfe3d6;font-size:13px;font-weight:700;text-decoration:none;white-space:nowrap}.dsb-all:after{content:" →"}
.dsb-g{display:grid;grid-template-columns:7fr 5fr;gap:40px;align-items:center}.dsb-img img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block}
.dsb .dsb-no{font:900 72px/.85 "Be Vietnam Pro",sans-serif;color:transparent;-webkit-text-stroke:1.2px #cfe3d6;margin:0 0 12px}
.dsb .dsb-t{font-family:Newsreader,Georgia,serif;font-weight:600;font-size:clamp(26px,2.8vw,40px);line-height:1.15;margin:0 0 12px}.dsb .dsb-t a{color:#fff;text-decoration:none}
.dsb .dsb-d{font-family:Newsreader,Georgia,serif;font-size:18px;line-height:1.5;color:#c9d2cd;margin:0 0 12px}.dsb .dsb-m{font-size:12px;color:#aebcb4;margin:0 0 18px}
.dsb .dsb-btn{display:inline-block;background:#c4554b;color:#fff;font-weight:700;font-size:13px;padding:10px 16px;text-decoration:none}
@media(max-width:700px){.dsb{padding:30px 0 34px}.dsb>*{padding:0 20px}.dsb-g{grid-template-columns:1fr;gap:20px}.dsb-h img{height:34px}.dsb .dsb-no{font-size:48px}.dsb .dsb-t{font-size:24px}}
.dkds-arch .dkb-site-content,.dkds-arch .hm-container{padding-top:0!important}
.dsa{font-family:"Be Vietnam Pro",sans-serif;padding-top:0!important}.dsa-full{width:100vw;margin-left:calc(50% - 50vw);box-sizing:border-box}
.dsa-mast{background:#0c1712;color:#f4efe4;position:relative;overflow:hidden;padding:64px 0 56px}
.dsa-mast:before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(180deg,transparent 0 38px,rgba(207,227,214,.05) 38px 39px)}
.dsa-mast:after{content:"";position:absolute;right:-8vw;top:-30%;width:60vw;height:160%;background:radial-gradient(closest-side,rgba(196,85,75,.22),transparent 70%)}
.dsa-in{max-width:1180px;margin:0 auto;padding:0 24px;position:relative;z-index:1;box-sizing:border-box}
.dsa .dsa-h1{margin:0;line-height:0}.dsa-h1 img{width:min(360px,70vw);height:auto;display:block}
.dsa .dsa-tag{font-family:Newsreader,Georgia,serif;font-style:italic;font-size:clamp(20px,2.3vw,28px);line-height:1.4;max-width:720px;margin:26px 0 30px;color:#e9e3d6}
.dsa-std{display:flex;flex-wrap:wrap;gap:10px 28px;margin:0;padding:22px 0 0;border-top:1px solid rgba(207,227,214,.18);list-style:none;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:#aebcb4}
.dsa-std li{margin:0}.dsa-std li:before{content:"";display:inline-block;width:7px;height:7px;background:#c4554b;margin-right:10px;vertical-align:1px}
.dsa-feat{background:#f4efe4;color:#1b1d1c;padding:56px 0 64px}.dsa-fg{display:grid;grid-template-columns:5fr 6fr;gap:48px;align-items:center}
.dsa .dsa-no{font:900 120px/.8 "Be Vietnam Pro",sans-serif;color:transparent;-webkit-text-stroke:1.5px #13241d;letter-spacing:-.04em;margin:0 0 18px}
.dsa .dsa-lab{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#c4554b;margin:0 0 12px}
.dsa .dsa-t{font-family:Newsreader,Georgia,serif;font-weight:600;font-size:clamp(32px,3.6vw,50px);line-height:1.08;margin:0 0 16px;letter-spacing:-.01em}.dsa-t a{color:#1b1d1c;text-decoration:none}
.dsa .dsa-d{font-family:Newsreader,Georgia,serif;font-size:20px;line-height:1.5;color:#2a3b33;margin:0 0 20px}.dsa .dsa-meta{font-size:13px;color:#6f7772;margin:0 0 26px}
.dsa .dsa-btn{display:inline-flex;gap:10px;align-items:center;background:#13241d;color:#fff;padding:13px 22px;font-weight:700;font-size:14px;text-decoration:none;border-radius:2px}.dsa-btn:after{content:"→"}
.dsa-img img{width:100%;aspect-ratio:4/3.2;object-fit:cover;display:block;box-shadow:18px 18px 0 #13241d}
.dsa-list{padding:56px 0 30px}.dsa .dsa-lh{font:900 13px "Be Vietnam Pro",sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#6f7772;margin:0 0 10px}
.dsa-row{display:grid;grid-template-columns:110px 1fr 260px;gap:28px;align-items:center;padding:26px 0;border-top:1px solid var(--dk-line,#d6ddd8)}
.dsa-rn{font:900 64px/.8 "Be Vietnam Pro",sans-serif;color:transparent;-webkit-text-stroke:1.2px currentColor}
.dsa-row h3{font-family:Newsreader,Georgia,serif;font-weight:600;font-size:26px;line-height:1.2;margin:0 0 8px}.dsa-row h3 a{color:inherit;text-decoration:none}
.dsa-row p{font-family:Newsreader,Georgia,serif;font-size:17px;line-height:1.5;margin:0 0 8px;opacity:.85}.dsa-row small{font-size:12px;opacity:.7}.dsa-rimg img{width:100%;aspect-ratio:16/10;object-fit:cover;display:block}
@media(max-width:860px){.dsa-mast{padding:40px 0 36px}.dsa-fg{grid-template-columns:1fr;gap:28px}.dsa-img{order:-1}.dsa-img img{box-shadow:10px 10px 0 #13241d}.dsa .dsa-no{font-size:80px}.dsa-feat{padding:36px 0 44px}.dsa .dsa-d{font-size:18px}.dsa-row{grid-template-columns:64px 1fr;gap:16px}.dsa-rimg{display:none}.dsa-rn{font-size:44px}.dsa-row h3{font-size:21px}}
CSS;
    }
    add_filter( 'body_class', function ( $c ) { if ( is_category( 'doc-sau' ) && ! is_paged() ) { $c[] = 'dkds-arch'; } return $c; } );
    add_action( 'wp_head', function () {
        if ( ! ( is_front_page() || is_home() || is_category( 'doc-sau' ) ) ) { return; }
        if ( is_category( 'doc-sau' ) || is_front_page() || is_home() ) {
            echo '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@900&amp;family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&amp;display=swap">' . "\n";
        }
        echo '<style id="dkds2-css">' . dkds2_css() . '</style>' . "\n";
    }, 30 );
    add_action( 'template_redirect', function () {
        if ( ! is_category( 'doc-sau' ) || is_paged() || is_feed() ) { return; }
        get_header();
        echo dkds_archive();
        get_footer();
        exit;
    }, 20 );
}

if ( ! function_exists( 'dk_topics_shortcode' ) ) {
    /* Trang /chuyen-de/ — mẫu D (21/10/2026): khung lớn = chuyên đề đăng gần nhất, bộ lọc, lưới thẻ có mô tả.
       Nhãn: "Mới ra mắt" trong 14 ngày đầu; ngày kỷ niệm đã qua chỉ ghi dịp + ngày/tháng, không ghi năm. */
    function dk_topics_shortcode() {
        $preview = ! empty( $_GET['dk_preview_slider'] ) && current_user_can( 'edit_pages' );
        $list    = dk_topics_list( $preview );
        if ( ! $list ) { return ''; }
        $occ   = array(
            'ngay-dot-quy-the-gioi'  => 'Ngày Đột quỵ Thế giới',
            'vung-vang-tu-ben-trong' => 'Ngày Quốc tế Nam giới',
            'ban-linh-diu-dang'      => 'Ngày Phụ nữ Việt Nam',
        );
        $today = wp_date( 'Y-m-d' );
        $now   = current_time( 'timestamp' );
        foreach ( $list as $i => $t ) {
            $p          = get_page_by_path( $t['slug'] );
            $pub        = $p ? $p->post_date : '2000-01-01 00:00:00';
            $fresh      = ( $now - strtotime( $pub ) ) <= 14 * DAY_IN_SECONDS;
            $dated      = '' !== $t['end'];
            $dm         = $dated ? wp_date( 'd/m', strtotime( $t['end'] . ' 12:00:00' ) ) : '';
            $o          = isset( $occ[ $t['slug'] ] ) ? $occ[ $t['slug'] ] : '';
            $hot        = $fresh;
            if ( $dated && $t['end'] > $today ) {
                $lab = ( $fresh ? 'Mới ra mắt · ' : '' ) . 'Hướng tới ' . $dm;
                $hot = true;
            } elseif ( $dated && $t['end'] === $today ) {
                $lab = 'Hôm nay · ' . $dm;
                $hot = true;
            } elseif ( $dated ) {
                $lab = ( $o ? $o : 'Ngày kỷ niệm' ) . ' · ' . $dm;
                $hot   = false;
                $fresh = false;
            } else {
                $lab = $fresh ? 'Mới' : 'Thường trực';
            }
            $list[ $i ] += array( 'pub' => $pub, 'fresh' => $fresh, 'dated' => $dated, 'lab' => $lab, 'hot' => $hot, 'occ' => $o );
        }
        usort( $list, function ( $a, $b ) { return strcmp( $b['pub'], $a['pub'] ); } );
        $f    = array_shift( $list );
        $n    = count( $list );
        $cols = ( 2 === $n || 1 === $n % 3 || 1 === $n ) ? 2 : 3;
        $all  = array_merge( array( $f ), $list );
        $cnt  = array(
            'f' => count( array_filter( $all, function ( $x ) { return $x['fresh']; } ) ),
            'p' => count( array_filter( $all, function ( $x ) { return ! $x['dated']; } ) ),
            'd' => count( array_filter( $all, function ( $x ) { return $x['dated']; } ) ),
        );
        $attr = function ( $x ) { return ' data-f="' . ( $x['fresh'] ? 1 : 0 ) . '" data-d="' . ( $x['dated'] ? 1 : 0 ) . '"'; };
        ob_start();
        ?>
<style>
article:has(.dkt) .entry-header,article:has(.dkt) .post-thumbnail{display:none!important}
.dkt{--g:#1f4b3a;--r:#a4504c;--ink:#1b1f1d;--sub:#3c4440;--mut:#6b746f;--line:#e3ded4;--chip:#fff;font-family:var(--dk-sans,"Be Vietnam Pro",sans-serif);color:var(--ink);max-width:1160px;margin:0 auto}
.dkt a{text-decoration:none!important;color:inherit}
.dkt img{display:block;width:100%;object-fit:cover;margin:0!important;max-width:none}
.dkt .dkt-tag{display:block;margin:0!important;font-size:.68rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--r)}
.dkt .dkt-hd{padding:20px 0 0;display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:end}
.dkt .dkt-hd h1{font-family:"Newsreader",Georgia,serif!important;font-size:clamp(2.6rem,6vw,4.4rem)!important;font-weight:800!important;letter-spacing:-.02em;line-height:1!important;margin:4px 0 0!important;color:var(--ink)}
.dkt .dkt-hd p{margin:0!important;font-size:1.02rem;line-height:1.65;color:var(--sub)}
.dkt-tabs{display:flex;gap:8px;padding:26px 0 22px;border-bottom:1px solid var(--line);overflow-x:auto;scrollbar-width:none}
.dkt-tabs::-webkit-scrollbar{display:none}
.dkt-tabs button{flex:none;font:600 .85rem/1 var(--dk-sans,sans-serif);background:var(--chip);color:var(--sub);border:1px solid var(--line);border-radius:999px;padding:10px 15px;cursor:pointer;margin:0}
.dkt-tabs button[aria-pressed="true"]{background:var(--g);color:#fff;border-color:var(--g)}
.dkt-tabs button span{opacity:.55;margin-left:4px}
.dkt-chip{display:inline-block;align-self:flex-start;font-size:.66rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;padding:5px 9px;border-radius:4px;background:#e7b7a4;color:#2a120d;line-height:1.3}
.dkt-chip.perm{background:#fff;color:#1f4b3a}
.dkt-feat{position:relative;display:block;margin:28px 0 8px;border-radius:16px;overflow:hidden;aspect-ratio:2.35/1;background:#14211b}
.dkt-feat img{position:absolute;inset:0;height:100%;transition:transform .6s}
.dkt-feat:hover img,.dkt-card:hover img{transform:scale(1.04)}
.dkt-feat::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,18,14,.88) 0%,rgba(10,18,14,.55) 38%,rgba(10,18,14,0) 65%)}
.dkt-feat .dkt-tx{position:absolute;left:0;top:0;bottom:0;width:46%;padding:40px;display:flex;flex-direction:column;justify-content:center;gap:12px;z-index:2;color:#fff}
.dkt .dkt-occ{margin:0!important;font-family:"Newsreader",Georgia,serif;font-style:italic;color:#e9dcd0;font-size:1.05rem}
.dkt .dkt-feat h2{font-family:"Newsreader",Georgia,serif!important;font-size:2.5rem!important;line-height:1.08!important;color:#fff!important;margin:0!important;font-weight:800}
.dkt .dkt-feat h2 em,.dkt .dkt-card h3 em{font-weight:500}
.dkt .dkt-feat p.dkt-l{margin:0!important;line-height:1.65;color:#e4e7e3;font-size:.98rem}
.dkt-btn{margin-top:6px;align-self:flex-start;background:#fff;color:#1f4b3a;padding:11px 18px;border-radius:999px;font-weight:700;font-size:.9rem}
.dkt-sec{display:flex;align-items:baseline;justify-content:space-between;border-top:2px solid var(--ink);padding-top:12px;margin:46px 0 22px}
.dkt .dkt-sec h2{font-family:"Newsreader",Georgia,serif!important;font-size:1.5rem!important;margin:0!important;font-weight:800;color:var(--ink)}
.dkt-sec span{font-size:.85rem;color:var(--mut)}
.dkt-grid{display:grid;gap:26px;margin-bottom:56px}
.dkt-card .dkt-ph{position:relative;border-radius:12px;overflow:hidden;aspect-ratio:16/9}
.dkt-card .dkt-ph img{height:100%;transition:transform .5s}
.dkt-card .dkt-ph .dkt-chip{position:absolute;left:12px;bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,.15)}
.dkt .dkt-card h3{font-family:"Newsreader",Georgia,serif!important;font-size:1.35rem!important;line-height:1.25!important;margin:14px 0 6px!important;font-weight:800;color:var(--ink)}
.dkt .dkt-card p{margin:0!important;font-size:.92rem;line-height:1.6;color:var(--sub)}
.dkt-card:hover h3{text-decoration:underline}
.dkt-empty{display:none;color:var(--mut);margin:20px 0 50px}
@media (max-width:760px){
.dkt .dkt-hd{grid-template-columns:1fr;gap:12px;padding-top:8px}
.dkt-feat{aspect-ratio:auto;display:flex;flex-direction:column}
.dkt-feat img{position:static;aspect-ratio:16/10;height:auto}
.dkt-feat::after{display:none}
.dkt-feat .dkt-tx{position:static;width:auto;padding:22px 22px 26px}
.dkt .dkt-feat h2{font-size:1.9rem!important}
.dkt-grid{grid-template-columns:1fr!important}
}
html.dk-dark .dkt,html.hm-dark .dkt{--ink:#ecebe6;--sub:#c9cdc8;--mut:#9aa39d;--line:#34403a;--chip:#1c2622}
html.dk-dark .dkt-tabs button[aria-pressed="true"],html.hm-dark .dkt-tabs button[aria-pressed="true"]{background:#cfe3d6;color:#14211b;border-color:#cfe3d6}
</style>
<div class="dkt">
    <div class="dkt-hd">
        <div><span class="dkt-tag">Dy Khoa Blog</span><h1>Chuyên đề</h1></div>
        <p>Mỗi chuyên đề tập hợp các bài viết dựa trên bằng chứng và công cụ tương tác quanh một chủ đề hoặc một ngày kỷ niệm. Chuyên đề mới ra mắt được xếp lên trước.</p>
    </div>
    <div class="dkt-tabs" role="group" aria-label="Lọc chuyên đề">
        <button type="button" data-x="a" aria-pressed="true">Tất cả<span><?php echo (int) count( $all ); ?></span></button>
        <?php if ( $cnt['f'] ) : ?><button type="button" data-x="f" aria-pressed="false">Mới ra mắt<span><?php echo (int) $cnt['f']; ?></span></button><?php endif; ?>
        <?php if ( $cnt['p'] ) : ?><button type="button" data-x="p" aria-pressed="false">Chủ đề thường trực<span><?php echo (int) $cnt['p']; ?></span></button><?php endif; ?>
        <?php if ( $cnt['d'] ) : ?><button type="button" data-x="d" aria-pressed="false">Ngày kỷ niệm<span><?php echo (int) $cnt['d']; ?></span></button><?php endif; ?>
    </div>
    <a class="dkt-feat dkt-it" href="<?php echo esc_url( $f['url'] ); ?>"<?php echo $attr( $f ); ?>>
        <img src="<?php echo esc_url( $f['img'] ); ?>" alt="<?php echo esc_attr( $f['alt'] ); ?>" width="1200" height="600" decoding="async" fetchpriority="high" style="object-position:<?php echo esc_attr( $f['pos'] ); ?>">
        <div class="dkt-tx">
            <span class="dkt-chip<?php echo $f['hot'] ? '' : ' perm'; ?>"><?php echo esc_html( $f['lab'] ); ?></span>
            <?php if ( $f['occ'] ) : ?><p class="dkt-occ"><?php echo esc_html( $f['occ'] ); ?></p><?php endif; ?>
            <h2><?php echo wp_kses( $f['title'], array( 'em' => array() ) ); ?></h2>
            <p class="dkt-l"><?php echo esc_html( $f['lede'] ); ?></p>
            <span class="dkt-btn">Vào chuyên đề →</span>
        </div>
    </a>
    <?php if ( $n ) : ?>
    <div class="dkt-sec dkt-sh"><h2>Đọc bất cứ lúc nào</h2><span><?php echo (int) $n; ?> chuyên đề</span></div>
    <div class="dkt-grid" style="grid-template-columns:repeat(<?php echo (int) $cols; ?>,minmax(0,1fr))">
        <?php foreach ( $list as $t ) : ?>
        <a class="dkt-card dkt-it" href="<?php echo esc_url( $t['url'] ); ?>"<?php echo $attr( $t ); ?>>
            <div class="dkt-ph">
                <img src="<?php echo esc_url( $t['img'] ); ?>" alt="<?php echo esc_attr( $t['alt'] ); ?>" width="1200" height="600" loading="lazy" decoding="async" style="object-position:<?php echo esc_attr( $t['pos'] ); ?>">
                <span class="dkt-chip<?php echo $t['hot'] ? '' : ' perm'; ?>"><?php echo esc_html( $t['lab'] ); ?></span>
            </div>
            <h3><?php echo wp_kses( $t['title'], array( 'em' => array() ) ); ?></h3>
            <p><?php echo esc_html( $t['lede'] ); ?></p>
        </a>
        <?php endforeach; ?>
    </div>
    <?php endif; ?>
</div>
<script>
(function(){var w=document.currentScript.previousElementSibling;if(!w)return;var bs=w.querySelectorAll('.dkt-tabs button'),its=w.querySelectorAll('.dkt-it'),sh=w.querySelector('.dkt-sh');
for(var i=0;i<bs.length;i++){bs[i].addEventListener('click',function(){var x=this.getAttribute('data-x');for(var j=0;j<bs.length;j++)bs[j].setAttribute('aria-pressed',bs[j]===this?'true':'false');var g=0;
for(var k=0;k<its.length;k++){var e=its[k],ok=x==='a'||(x==='f'&&e.getAttribute('data-f')==='1')||(x==='d'&&e.getAttribute('data-d')==='1')||(x==='p'&&e.getAttribute('data-d')==='0');e.style.display=ok?'':'none';if(ok&&e.classList.contains('dkt-card'))g++;}
if(sh)sh.style.display=g?'':'none';});}})();
</script>
        <?php
        return ob_get_clean();
    }
    add_shortcode( 'dk_chuyen_de', 'dk_topics_shortcode' );
}


// DK SERIES: điều hướng "Chuỗi bài" (mẫu A thẻ đầu bài + mẫu B mục lục cuối bài), 20/10/2026
add_action( 'init', function () {
	register_taxonomy( 'dk_series', 'post', array(
		'labels'            => array(
			'name'          => 'Chuỗi bài',
			'singular_name' => 'Chuỗi bài',
			'add_new_item'  => 'Thêm chuỗi bài',
			'edit_item'     => 'Sửa chuỗi bài',
			'all_items'     => 'Tất cả chuỗi bài',
		),
		'hierarchical'      => true,
		'public'            => true,
		'show_ui'           => true,
		'show_admin_column' => true,
		'show_in_rest'      => true,
		'rest_base'         => 'dk_series',
		'rewrite'           => array( 'slug' => 'chuoi-bai', 'with_front' => false ),
	) );
} );

function dk_series_data( $post_id ) {
	$terms = get_the_terms( $post_id, 'dk_series' );
	if ( empty( $terms ) || is_wp_error( $terms ) ) { return null; }
	$term = $terms[0];
	$ids  = get_posts( array(
		'post_type'      => 'post',
		'post_status'    => 'publish',
		'posts_per_page' => 100,
		'orderby'        => 'date',
		'order'          => 'ASC',
		'fields'         => 'ids',
		'no_found_rows'  => true,
		'tax_query'      => array( array( 'taxonomy' => 'dk_series', 'field' => 'term_id', 'terms' => $term->term_id ) ),
	) );
	$pos = array_search( (int) $post_id, array_map( 'intval', $ids ), true );
	if ( false === $pos || count( $ids ) < 2 ) { return null; }
	return array( 'term' => $term, 'ids' => $ids, 'pos' => $pos );
}

add_filter( 'the_content', function ( $content ) {
	if ( is_admin() || ! is_singular( 'post' ) || ! in_the_loop() || ! is_main_query() ) { return $content; }
	$s = dk_series_data( get_the_ID() );
	if ( ! $s ) { return $content; }
	$ids   = $s['ids'];
	$pos   = $s['pos'];
	$total = count( $ids );
	$name  = esc_html( $s['term']->name );
	$prev  = $pos > 0 ? $ids[ $pos - 1 ] : 0;
	$next  = $pos < $total - 1 ? $ids[ $pos + 1 ] : 0;
	$pct   = round( ( $pos + 1 ) / $total * 100 );

	// Mẫu A: thẻ chuỗi đầu bài
	$a  = '<div class="dkser-a"><div class="dkser-t">📚 CHUỖI BÀI</div>';
	$a .= '<div class="dkser-n">' . $name . ' · Bài ' . ( $pos + 1 ) . '/' . $total . '</div>';
	$a .= '<div class="dkser-bar"><i style="width:' . $pct . '%"></i></div><div class="dkser-row">';
	$a .= $prev ? '<a href="' . esc_url( get_permalink( $prev ) ) . '">← Bài trước</a>' : '<span></span>';
	$a .= '<a href="#dk-series">Xem cả chuỗi</a>';
	$a .= $next ? '<a href="' . esc_url( get_permalink( $next ) ) . '">Bài tiếp →</a>' : '<span></span>';
	$a .= '</div></div>';

	// Mẫu B: mục lục chuỗi cuối bài
	$item = function ( $i ) use ( $ids, $pos ) {
		$cls = $i === $pos ? 'cur' : ( $i < $pos ? 'done' : '' );
		$t   = esc_html( get_the_title( $ids[ $i ] ) );
		$in  = $i === $pos ? $t : '<a href="' . esc_url( get_permalink( $ids[ $i ] ) ) . '">' . $t . '</a>';
		return '<li class="' . $cls . '" value="' . ( $i + 1 ) . '">' . $in . '</li>';
	};
	$from = max( 0, min( $pos - 2, $total - 5 ) );
	$to   = min( $total - 1, $from + 4 );
	$b  = '<section class="dkser-b" id="dk-series"><div class="dkser-t">CHUỖI BÀI · ' . $total . ' BÀI</div><div class="dkser-name">' . $name . '</div><ol>';
	for ( $i = $from; $i <= $to; $i++ ) { $b .= $item( $i ); }
	$b .= '</ol>';
	if ( $total > 5 ) {
		$b .= '<details class="dkser-all"><summary>Xem đủ ' . $total . ' bài</summary><ol>';
		for ( $i = 0; $i < $total; $i++ ) { $b .= $item( $i ); }
		$b .= '</ol></details>';
	}
	$b .= '<div class="dkser-pn">';
	$b .= $prev ? '<a href="' . esc_url( get_permalink( $prev ) ) . '"><small>← Bài trước</small>' . esc_html( get_the_title( $prev ) ) . '</a>' : '<span></span>';
	$b .= $next ? '<a class="nx" href="' . esc_url( get_permalink( $next ) ) . '"><small>Bài tiếp →</small>' . esc_html( get_the_title( $next ) ) . '</a>' : '<span></span>';
	$b .= '</div></section>';

	return $a . $content . $b;
}, 20 );

add_action( 'wp_head', function () {
	if ( ! is_singular( 'post' ) || ! dk_series_data( get_queried_object_id() ) ) { return; }
	echo '<style id="dk-series-css">'
		. '.dkser-a{border:1px solid #cfe3d7;background:#f1f8f3;border-radius:10px;padding:12px 14px;margin:0 0 1.4em}'
		. '.dkser-t{font-size:12px;font-weight:700;color:#0e5c3d;letter-spacing:.05em}'
		. '.dkser-n{font-size:15px;font-weight:700;margin:3px 0 8px;color:#0b1712}'
		. '.dkser-bar{height:6px;background:#dcebe2;border-radius:3px;overflow:hidden}.dkser-bar i{display:block;height:100%;background:#0e5c3d}'
		. '.dkser-row{display:flex;justify-content:space-between;gap:8px;font-size:13px;margin-top:8px}'
		. '.dkser-row a{color:#0e5c3d;font-weight:600;text-decoration:none}'
		. '.dkser-b{border:1px solid #e3e0d6;border-top:3px solid #013b25;background:#fff;border-radius:0 0 10px 10px;padding:16px;margin:2em 0}'
		. '.dkser-name{font-size:18px;font-weight:700;margin:2px 0 10px;color:#0b1712}'
		. '.dkser-b ol{margin:0;padding:0;list-style:none}'
		. '.dkser-b li{display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-bottom:1px dashed #e3e0d6;font-size:15px;line-height:1.4;margin:0}'
		. '.dkser-b li:before{content:attr(value);flex:0 0 24px;height:24px;border-radius:50%;background:#eef3ef;color:#0e5c3d;font-weight:700;font-size:12px;display:flex;align-items:center;justify-content:center}'
		. '.dkser-b li.cur{font-weight:700}.dkser-b li.cur:before{background:#0e5c3d;color:#fff}'
		. '.dkser-b li.done a{color:#5b6670}.dkser-b li a{color:#0b1712;text-decoration:none}.dkser-b li a:hover{color:#0e5c3d;text-decoration:underline}'
		. '.dkser-all summary{cursor:pointer;color:#0e5c3d;font-weight:600;font-size:14px;margin:10px 0 4px}'
		. '.dkser-all[open] summary{margin-bottom:8px}.dkser-b>ol:has(+ .dkser-all[open]){display:none}'
		. '.dkser-pn{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}'
		. '.dkser-pn a{display:block;border:1px solid #e3e0d6;border-radius:8px;padding:10px;font-size:14px;line-height:1.35;color:#0b1712;text-decoration:none}'
		. '.dkser-pn a.nx{text-align:right;background:#f1f8f3;border-color:#cfe3d7}'
		. '.dkser-pn small{display:block;color:#5b6670;font-size:12px;margin-bottom:2px}'
		. 'html.dk-dark .dkser-a,html.hm-dark .dkser-a{background:#12251c;border-color:#24473a}html.dk-dark .dkser-b,html.hm-dark .dkser-b{background:#14201a;border-color:#2a3a32}'
		. 'html.dk-dark .dkser-n,html.dk-dark .dkser-name,html.dk-dark .dkser-b li a,html.dk-dark .dkser-pn a,html.hm-dark .dkser-n,html.hm-dark .dkser-name,html.hm-dark .dkser-b li a,html.hm-dark .dkser-pn a{color:#e8efe9}'
		. '@media(max-width:600px){.dkser-pn{grid-template-columns:1fr}.dkser-pn a.nx{text-align:left}}'
		. '</style>' . "\n";
}, 20 );

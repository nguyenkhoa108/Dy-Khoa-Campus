            <!-- CHUYÊN MỤC PHỤ: DU LỊCH + NHẬT KÝ (DẠNG GỌN, CHỈ TIÊU ĐỀ) -->
            <?php
            $dk_minor = array( 'du-lich', 'nhat-ky' );
            $dk_minor_html = '';
            foreach ( $dk_minor as $m_slug ) {
                $m_term = get_category_by_slug( $m_slug );
                if ( ! $m_term ) { continue; }
                $m_posts = get_posts( array(
                    'post_type'           => 'post',
                    'posts_per_page'      => 3,
                    'cat'                 => $m_term->term_id,
                    'fields'              => 'ids',
                    'ignore_sticky_posts' => true,
                    'no_found_rows'       => true,
                ) );
                if ( empty( $m_posts ) ) { continue; }
                $m_color = isset( $cat_colors[ $m_slug ] ) ? $cat_colors[ $m_slug ] : '#013b25';
                $m_url   = get_term_link( $m_term );
                $dk_minor_html .= '<section class="dkx-minor" style="--cat-c:' . esc_attr( $m_color ) . '">';
                $dk_minor_html .= '<div class="dkx-minor-head"><h2 class="dkx-h dkx-minor-title"><a href="' . esc_url( $m_url ) . '">' . esc_html( $m_term->name ) . '</a></h2>';
                $dk_minor_html .= '<a class="dkx-minor-more" href="' . esc_url( $m_url ) . '">Xem tất cả <span>→</span></a></div><ul class="dkx-minor-list">';
                foreach ( $m_posts as $m_id ) {
                    $dk_minor_html .= '<li><a href="' . esc_url( get_permalink( $m_id ) ) . '">' . esc_html( get_the_title( $m_id ) ) . '</a>';
                    $dk_minor_html .= '<span class="dkx-minor-date">' . esc_html( get_the_date( 'd/m/Y', $m_id ) ) . '</span></li>';
                }
                $dk_minor_html .= '</ul></section>';
            }
            if ( $dk_minor_html ) : ?>
            <style>
            .dkx-minor-row{display:grid;grid-template-columns:1fr;gap:22px;margin:6px 0 8px}
            @media (min-width:600px){.dkx-minor-row{grid-template-columns:repeat(2,minmax(0,1fr))}}
            .dkx-minor{min-width:0}
            .dkx-minor-head{display:flex;justify-content:space-between;align-items:baseline;gap:10px;border-bottom:2px solid var(--cat-c);padding-bottom:6px;margin-bottom:2px}
            .dkx-minor-title{font-size:1.1rem;margin:0}
            .dkx-minor-title a{color:var(--cat-c);text-decoration:none}
            .dkx-minor-more{font-size:.8rem;font-weight:700;color:var(--dk-muted);text-decoration:none;white-space:nowrap}
            .dkx-minor-list{list-style:none;margin:0;padding:0}
            .dkx-minor-list li{margin:0;padding:10px 0;border-bottom:1px dashed var(--dk-line)}
            .dkx-minor-list li:last-child{border-bottom:0}
            .dkx-minor-list a{display:block;font-family:var(--dk-serif);font-weight:700;font-size:1rem;line-height:1.35;color:var(--dk-ink);text-decoration:none}
            .dkx-minor-list a:hover{text-decoration:underline}
            .dkx-minor-date{display:block;margin-top:4px;font-size:.78rem;color:var(--dk-muted)}
            </style>
            <div class="dkx-minor-row" aria-label="Chuyên mục khác"><?php echo $dk_minor_html; ?></div>
            <?php endif; ?>

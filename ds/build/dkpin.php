
/* =========================================================
 * GHIM BÀI LÊN BÌA TRANG CHỦ CÓ THỜI HẠN (21/10/2026)
 * Bài được ghim (sticky) và có meta _dk_pin_until (giờ VN, dạng Y-m-d H:i) sẽ tự bỏ ghim khi hết hạn.
 * ========================================================= */
if ( ! function_exists( 'dk_pin_expire' ) ) {
    add_action( 'init', function () {
        register_post_meta( 'post', '_dk_pin_until', array(
            'type'          => 'string',
            'single'        => true,
            'show_in_rest'  => true,
            'auth_callback' => function () { return current_user_can( 'edit_posts' ); },
        ) );
    } );
    function dk_pin_expire( $force = false ) {
        if ( ! $force && get_transient( 'dk_pin_chk' ) ) { return; }
        set_transient( 'dk_pin_chk', 1, 10 * MINUTE_IN_SECONDS );
        $sticky = array_filter( array_map( 'intval', (array) get_option( 'sticky_posts', array() ) ) );
        if ( ! $sticky ) { return; }
        $now     = current_time( 'Y-m-d H:i' );
        $changed = false;
        foreach ( $sticky as $id ) {
            $until = get_post_meta( $id, '_dk_pin_until', true );
            if ( $until && $until <= $now ) {
                unstick_post( $id );
                delete_post_meta( $id, '_dk_pin_until' );
                $changed = true;
            }
        }
        if ( $changed ) { do_action( 'litespeed_purge_all' ); }
    }
    add_action( 'init', 'dk_pin_expire', 20 );
    add_action( 'dk_pin_cron', function () { dk_pin_expire( true ); } );
    add_action( 'init', function () {
        if ( ! wp_next_scheduled( 'dk_pin_cron' ) ) { wp_schedule_event( time() + 300, 'hourly', 'dk_pin_cron' ); }
    }, 30 );
}

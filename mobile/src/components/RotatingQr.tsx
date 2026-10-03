import React, { useCallback, useEffect, useRef, useState } from 'react';
import { ActivityIndicator, StyleSheet, Text, View } from 'react-native';
import QRCode from 'react-native-qrcode-svg';
import { ApiError } from '../api/client';
import { Button, Caption } from './ui';
import { colors, radius, spacing, typography } from '../theme';
import type { QrToken } from '../api/types';

/**
 * Mã QR tự làm mới.
 *
 * Mã do máy chủ ký và chỉ sống vài chục giây, nên màn hình phải xin mã mới
 * trước khi mã cũ hết hạn — `refreshAfterSec` trong phản hồi cho biết nên xin
 * lại sau bao lâu. Nhờ vậy ảnh chụp màn hình gần như vô dụng.
 */
export function RotatingQr({
  fetchToken,
  size = 240,
  caption,
}: {
  fetchToken: () => Promise<QrToken>;
  size?: number;
  caption?: string;
}) {
  const [token, setToken] = useState<QrToken | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [secondsLeft, setSecondsLeft] = useState(0);

  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const mounted = useRef(true);

  const load = useCallback(async () => {
    try {
      const next = await fetchToken();
      if (!mounted.current) return;
      setToken(next);
      setError(null);
      setSecondsLeft(next.ttlSec);

      if (timer.current) clearTimeout(timer.current);
      timer.current = setTimeout(() => {
        if (mounted.current) load();
      }, next.refreshAfterSec * 1000);
    } catch (err) {
      if (!mounted.current) return;
      setError(
        err instanceof ApiError
          ? err.isNetworkError
            ? 'Không lấy được mã mới vì mất kết nối máy chủ.'
            : err.message
          : 'Không lấy được mã QR',
      );
    }
  }, [fetchToken]);

  useEffect(() => {
    mounted.current = true;
    load();
    return () => {
      mounted.current = false;
      if (timer.current) clearTimeout(timer.current);
    };
  }, [load]);

  // Đồng hồ đếm ngược cho người dùng biết mã sắp đổi.
  useEffect(() => {
    if (!token) return;
    const id = setInterval(() => {
      const remaining = Math.max(0, Math.round((new Date(token.expiresAt).getTime() - Date.now()) / 1000));
      setSecondsLeft(remaining);
    }, 500);
    return () => clearInterval(id);
  }, [token]);

  if (error && !token) {
    return (
      <View style={s.center}>
        <Text style={s.error}>{error}</Text>
        <Button label="Thử lại" variant="secondary" onPress={load} />
      </View>
    );
  }

  if (!token) {
    return (
      <View style={s.center}>
        <ActivityIndicator color={colors.primary} size="large" />
        <Caption>Đang tạo mã QR…</Caption>
      </View>
    );
  }

  const expired = secondsLeft <= 0;

  return (
    <View style={s.container}>
      <View style={[s.qrFrame, expired && s.qrExpired]}>
        <QRCode value={token.token} size={size} backgroundColor="white" color={colors.text} />
        {expired ? (
          <View style={s.expiredOverlay}>
            <Text style={s.expiredText}>Đang làm mới…</Text>
          </View>
        ) : null}
      </View>

      <View style={s.countdownRow}>
        <View style={s.track}>
          <View style={[s.fill, { width: `${Math.min(100, (secondsLeft / token.ttlSec) * 100)}%` }]} />
        </View>
        <Text style={s.countdown}>{expired ? '…' : `${secondsLeft}s`}</Text>
      </View>

      {caption ? <Caption>{caption}</Caption> : null}
      {error ? <Text style={s.errorInline}>{error}</Text> : null}
    </View>
  );
}

const s = StyleSheet.create({
  container: { alignItems: 'center', gap: spacing.md },
  center: { alignItems: 'center', justifyContent: 'center', gap: spacing.md, paddingVertical: spacing.xxl },
  qrFrame: {
    backgroundColor: '#FFFFFF',
    padding: spacing.lg,
    borderRadius: radius.lg,
    borderWidth: 1,
    borderColor: colors.border,
  },
  qrExpired: { opacity: 0.4 },
  expiredOverlay: { ...StyleSheet.absoluteFill, alignItems: 'center', justifyContent: 'center' },
  expiredText: { ...typography.subheading, color: colors.text },
  countdownRow: { flexDirection: 'row', alignItems: 'center', gap: spacing.md, alignSelf: 'stretch' },
  track: { flex: 1, height: 6, borderRadius: 3, backgroundColor: colors.border, overflow: 'hidden' },
  fill: { height: 6, borderRadius: 3, backgroundColor: colors.primary },
  countdown: { ...typography.caption, color: colors.textMuted, minWidth: 34, textAlign: 'right' },
  error: { ...typography.body, color: colors.danger, textAlign: 'center' },
  errorInline: { ...typography.caption, color: colors.danger, textAlign: 'center' },
});

import React, { useCallback, useEffect, useRef, useState } from 'react';
import { Platform, Pressable, StyleSheet, Text, View } from 'react-native';
import { CameraView, useCameraPermissions } from 'expo-camera';
import * as Haptics from 'expo-haptics';
import { Button, Caption, EmptyState } from './ui';
import { colors, radius, spacing, typography } from '../theme';

/** Khoảng lặng sau mỗi lần nhận mã, tránh bắn liên tục cùng một mã. */
const RESCAN_DELAY_MS = 2000;

export interface QrScannerProps {
  /** Gọi khi đọc được một mã; trả về Promise để scanner khoá camera trong lúc xử lý. */
  onScan: (data: string) => Promise<void> | void;
  /** Tạm dừng quét (ví dụ khi đang hiện hộp kết quả). */
  paused?: boolean;
  /** Dòng hướng dẫn hiển thị dưới khung ngắm. */
  hint?: string;
}

export function QrScanner({ onScan, paused = false, hint }: QrScannerProps) {
  const [permission, requestPermission] = useCameraPermissions();
  const [busy, setBusy] = useState(false);
  const [torch, setTorch] = useState(false);

  // Chặn trùng: nhớ mã vừa đọc và mốc thời gian, không dựa vào state để khỏi trễ nhịp render.
  const lastScan = useRef<{ data: string; at: number } | null>(null);
  const mounted = useRef(true);

  useEffect(() => {
    mounted.current = true;
    return () => {
      mounted.current = false;
    };
  }, []);

  const handleBarcode = useCallback(
    async ({ data }: { data: string }) => {
      if (paused || busy || !data) return;

      const now = Date.now();
      const prev = lastScan.current;
      if (prev && prev.data === data && now - prev.at < RESCAN_DELAY_MS) return;
      lastScan.current = { data, at: now };

      setBusy(true);
      // Rung nhẹ để người quét biết máy đã bắt được mã, kể cả khi nhìn vào lớp chứ không nhìn màn hình.
      Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium).catch(() => {});
      try {
        await onScan(data);
      } finally {
        if (mounted.current) setBusy(false);
      }
    },
    [busy, paused, onScan],
  );

  if (!permission) {
    return <EmptyState title="Đang kiểm tra quyền camera…" />;
  }

  if (!permission.granted) {
    return (
      <View style={s.permission}>
        <EmptyState
          title="Cần quyền sử dụng camera"
          description={
            permission.canAskAgain
              ? 'Ứng dụng dùng camera chỉ để đọc mã QR điểm danh, không lưu hình ảnh.'
              : 'Bạn đã từ chối quyền camera. Hãy bật lại trong phần Cài đặt của điện thoại.'
          }
        />
        {permission.canAskAgain ? <Button label="Cho phép dùng camera" onPress={requestPermission} /> : null}
      </View>
    );
  }

  return (
    <View style={s.container}>
      <CameraView
        style={StyleSheet.absoluteFill}
        facing="back"
        enableTorch={torch}
        barcodeScannerSettings={{ barcodeTypes: ['qr'] }}
        onBarcodeScanned={paused || busy ? undefined : handleBarcode}
      />

      {/* Khung ngắm: bốn góc sáng, giúp canh mã nhanh trong giảng đường thiếu sáng. */}
      <View style={s.overlay} pointerEvents="box-none">
        <View style={s.reticle}>
          <View style={[s.corner, s.cornerTopLeft]} />
          <View style={[s.corner, s.cornerTopRight]} />
          <View style={[s.corner, s.cornerBottomLeft]} />
          <View style={[s.corner, s.cornerBottomRight]} />
        </View>

        {hint ? (
          <View style={s.hintBox}>
            <Text style={s.hintText}>{hint}</Text>
          </View>
        ) : null}

        {Platform.OS !== 'web' ? (
          <Pressable style={s.torch} onPress={() => setTorch((on) => !on)} accessibilityRole="button">
            <Text style={s.torchText}>{torch ? 'Tắt đèn' : 'Bật đèn pin'}</Text>
          </Pressable>
        ) : null}

        {busy ? (
          <View style={s.busy}>
            <Caption muted={false}>Đang xử lý…</Caption>
          </View>
        ) : null}
      </View>
    </View>
  );
}

const s = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000' },
  permission: { flex: 1, justifyContent: 'center', padding: spacing.xl, gap: spacing.lg },
  overlay: { ...StyleSheet.absoluteFill, alignItems: 'center', justifyContent: 'center' },

  reticle: { width: 240, height: 240 },
  corner: { position: 'absolute', width: 36, height: 36, borderColor: colors.textInverse },
  cornerTopLeft: { top: 0, left: 0, borderTopWidth: 4, borderLeftWidth: 4, borderTopLeftRadius: radius.md },
  cornerTopRight: { top: 0, right: 0, borderTopWidth: 4, borderRightWidth: 4, borderTopRightRadius: radius.md },
  cornerBottomLeft: { bottom: 0, left: 0, borderBottomWidth: 4, borderLeftWidth: 4, borderBottomLeftRadius: radius.md },
  cornerBottomRight: { bottom: 0, right: 0, borderBottomWidth: 4, borderRightWidth: 4, borderBottomRightRadius: radius.md },

  hintBox: {
    position: 'absolute',
    bottom: 120,
    marginHorizontal: spacing.xl,
    backgroundColor: colors.overlay,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
    borderRadius: radius.md,
  },
  hintText: { ...typography.caption, color: colors.textInverse, textAlign: 'center' },

  torch: {
    position: 'absolute',
    bottom: 48,
    backgroundColor: colors.overlay,
    paddingHorizontal: spacing.xl,
    paddingVertical: spacing.md,
    borderRadius: radius.pill,
  },
  torchText: { ...typography.subheading, color: colors.textInverse },

  busy: {
    position: 'absolute',
    top: 48,
    backgroundColor: colors.overlay,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.sm,
    borderRadius: radius.pill,
  },
});

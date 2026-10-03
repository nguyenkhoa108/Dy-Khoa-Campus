import React from 'react';
import { Pressable, StyleSheet, Text, View } from 'react-native';
import { useScanQueue } from '../state/ScanQueueContext';
import { colors, spacing, typography } from '../theme';

/** Dải cảnh báo khi mất mạng hoặc còn lượt quét chưa gửi được. */
export function OfflineBanner() {
  const { isOnline, queue, isSyncing, sync } = useScanQueue();
  if (isOnline && queue.length === 0) return null;

  const offline = !isOnline;
  return (
    <Pressable
      style={[s.banner, offline ? s.offline : s.pending]}
      onPress={() => {
        if (!offline) sync().catch(() => {});
      }}
      disabled={offline || isSyncing}
    >
      <View style={[s.dot, { backgroundColor: offline ? colors.danger : colors.warning }]} />
      <Text style={s.text}>
        {offline
          ? queue.length > 0
            ? `Đang ngoại tuyến · ${queue.length} lượt quét chờ gửi`
            : 'Đang ngoại tuyến · lượt quét sẽ được lưu tạm'
          : isSyncing
            ? `Đang đồng bộ ${queue.length} lượt quét…`
            : `${queue.length} lượt quét chờ gửi · chạm để đồng bộ`}
      </Text>
    </Pressable>
  );
}

const s = StyleSheet.create({
  banner: { flexDirection: 'row', alignItems: 'center', gap: spacing.sm, paddingHorizontal: spacing.lg, paddingVertical: spacing.md },
  offline: { backgroundColor: colors.dangerSoft },
  pending: { backgroundColor: colors.warningSoft },
  dot: { width: 8, height: 8, borderRadius: 4 },
  text: { ...typography.caption, color: colors.text, flex: 1 },
});

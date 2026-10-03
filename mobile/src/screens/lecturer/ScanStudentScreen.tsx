import React, { useCallback, useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { QrScanner } from '../../components/QrScanner';
import { ScanResultSheet } from '../../components/ScanResultSheet';
import { OfflineBanner } from '../../components/OfflineBanner';
import { useCheckIn } from '../../state/useCheckIn';
import { colors, spacing, typography } from '../../theme';

/** Giảng viên quét mã QR cá nhân của từng sinh viên — chiều điểm danh thứ hai. */
export default function ScanStudentScreen({ route }: { route: any }) {
  const sessionId = route.params.sessionId as string;
  const title = route.params.title as string | undefined;

  const { outcome, submit, clear } = useCheckIn(sessionId);
  const [paused, setPaused] = useState(false);
  const [scanned, setScanned] = useState<string[]>([]);

  const handleScan = useCallback(
    async (data: string) => {
      setPaused(true);
      const result = await submit(data, 'Quét mã sinh viên');
      if (result.kind === 'success' && !result.duplicate) {
        setScanned((prev) => [`${result.studentCode} · ${result.studentName}`, ...prev].slice(0, 20));
      }
    },
    [submit],
  );

  const dismiss = useCallback(() => {
    clear();
    setPaused(false);
  }, [clear]);

  return (
    <View style={s.container}>
      <OfflineBanner />
      <View style={s.scanner}>
        <QrScanner
          onScan={handleScan}
          paused={paused}
          hint={title ? `Đang điểm danh: ${title}` : 'Quét mã QR cá nhân của sinh viên'}
        />
      </View>

      <View style={s.log}>
        <Text style={s.logTitle}>Đã quét trong phiên này: {scanned.length}</Text>
        {scanned.slice(0, 4).map((entry) => (
          <Text key={entry} style={s.logItem} numberOfLines={1}>
            ✓ {entry}
          </Text>
        ))}
        {scanned.length === 0 ? <Text style={s.logEmpty}>Chưa quét sinh viên nào.</Text> : null}
      </View>

      <ScanResultSheet outcome={outcome} onDismiss={dismiss} />
    </View>
  );
}

const s = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.background },
  scanner: { flex: 1 },
  log: { padding: spacing.lg, gap: spacing.xs, backgroundColor: colors.surface, borderTopWidth: 1, borderTopColor: colors.border },
  logTitle: { ...typography.subheading, color: colors.text },
  logItem: { ...typography.caption, color: colors.success },
  logEmpty: { ...typography.caption, color: colors.textMuted },
});

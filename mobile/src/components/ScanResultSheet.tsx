import React from 'react';
import { Modal, StyleSheet, Text, View } from 'react-native';
import { Button, Caption } from './ui';
import { attendanceColor, attendanceLabel } from '../utils/labels';
import { colors, radius, spacing, typography } from '../theme';
import type { ScanOutcome } from '../state/useCheckIn';

/** Hộp kết quả sau mỗi lượt quét — to, rõ, đọc được từ xa khi đứng ở bục giảng. */
export function ScanResultSheet({ outcome, onDismiss }: { outcome: ScanOutcome | null; onDismiss: () => void }) {
  if (!outcome) return null;

  const tone =
    outcome.kind === 'success'
      ? attendanceColor[outcome.status]
      : outcome.kind === 'queued'
        ? { fg: colors.warning, bg: colors.warningSoft }
        : { fg: colors.danger, bg: colors.dangerSoft };

  return (
    <Modal transparent animationType="fade" visible onRequestClose={onDismiss}>
      <View style={s.backdrop}>
        <View style={[s.sheet, { borderColor: tone.fg }]}>
          <View style={[s.iconCircle, { backgroundColor: tone.bg }]}>
            <Text style={[s.icon, { color: tone.fg }]}>
              {outcome.kind === 'success' ? '✓' : outcome.kind === 'queued' ? '⏱' : '✕'}
            </Text>
          </View>

          {outcome.kind === 'success' ? (
            <>
              <Text style={s.name}>{outcome.studentName}</Text>
              <Text style={s.code}>{outcome.studentCode}</Text>
              <View style={[s.statusPill, { backgroundColor: tone.bg }]}>
                <Text style={[s.statusText, { color: tone.fg }]}>{attendanceLabel[outcome.status]}</Text>
              </View>
              {outcome.duplicate ? <Caption>Đã điểm danh trước đó, không ghi thêm bản ghi mới.</Caption> : null}
            </>
          ) : outcome.kind === 'queued' ? (
            <>
              <Text style={s.name}>Đã lưu tạm</Text>
              <Text style={s.message}>{outcome.reason}</Text>
            </>
          ) : (
            <>
              <Text style={s.name}>Không ghi nhận được</Text>
              <Text style={s.message}>{outcome.message}</Text>
              <Caption>Mã lỗi: {outcome.code}</Caption>
            </>
          )}

          <Button label="Quét tiếp" onPress={onDismiss} style={{ alignSelf: 'stretch', marginTop: spacing.sm }} />
        </View>
      </View>
    </Modal>
  );
}

const s = StyleSheet.create({
  backdrop: { flex: 1, backgroundColor: colors.overlay, alignItems: 'center', justifyContent: 'center', padding: spacing.xl },
  sheet: {
    backgroundColor: colors.surface,
    borderRadius: radius.lg,
    borderWidth: 2,
    padding: spacing.xl,
    alignItems: 'center',
    gap: spacing.sm,
    width: '100%',
    maxWidth: 420,
  },
  iconCircle: { width: 64, height: 64, borderRadius: 32, alignItems: 'center', justifyContent: 'center' },
  icon: { fontSize: 32, fontWeight: '800' },
  name: { ...typography.title, color: colors.text, textAlign: 'center' },
  code: { ...typography.subheading, color: colors.textMuted },
  message: { ...typography.body, color: colors.text, textAlign: 'center' },
  statusPill: { paddingHorizontal: spacing.lg, paddingVertical: spacing.sm, borderRadius: radius.pill },
  statusText: { ...typography.subheading },
});

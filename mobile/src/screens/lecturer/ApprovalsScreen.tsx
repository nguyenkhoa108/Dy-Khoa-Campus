import React, { useCallback, useState } from 'react';
import { Alert, Modal, RefreshControl, StyleSheet, Text, View } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { api } from '../../api/endpoints';
import { ApiError } from '../../api/client';
import {
  Badge,
  Body,
  Button,
  Caption,
  Card,
  EmptyState,
  ErrorNotice,
  Field,
  Heading,
  Input,
  Loading,
  Row,
  Screen,
} from '../../components/ui';
import { leaveStatusColor, leaveStatusLabel, leaveTypeLabel } from '../../utils/labels';
import { formatDateKey, relativeTime } from '../../utils/datetime';
import { colors, radius, spacing, typography } from '../../theme';
import type { LeaveRequest, LeaveStatus } from '../../api/types';

const FILTERS: Array<{ key: LeaveStatus | 'all'; label: string }> = [
  { key: 'pending', label: 'Chờ duyệt' },
  { key: 'approved', label: 'Đã duyệt' },
  { key: 'rejected', label: 'Từ chối' },
  { key: 'all', label: 'Tất cả' },
];

/** Hộp duyệt đơn xin phép của giảng viên. */
export default function ApprovalsScreen() {
  const [filter, setFilter] = useState<LeaveStatus | 'all'>('pending');
  const [items, setItems] = useState<LeaveRequest[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [refreshing, setRefreshing] = useState(false);
  const [rejecting, setRejecting] = useState<LeaveRequest | null>(null);
  const [busyId, setBusyId] = useState<string | null>(null);

  const load = useCallback(async (status: LeaveStatus | 'all') => {
    try {
      const res = await api.leaveRequests({ status: status === 'all' ? undefined : status, limit: 100 });
      setItems(res.items);
      setError(null);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : 'Không tải được danh sách đơn');
    }
  }, []);

  useFocusEffect(
    useCallback(() => {
      load(filter);
    }, [load, filter]),
  );

  const refresh = useCallback(async () => {
    setRefreshing(true);
    await load(filter);
    setRefreshing(false);
  }, [load, filter]);

  const approve = (leave: LeaveRequest) => {
    Alert.alert(
      'Phê duyệt đơn',
      `Duyệt đơn của ${leave.student.fullName}? Các buổi học trong khoảng ngày sẽ được đánh dấu nghỉ có phép.`,
      [
        { text: 'Huỷ', style: 'cancel' },
        {
          text: 'Duyệt',
          onPress: async () => {
            setBusyId(leave.id);
            try {
              const res = await api.approveLeave(leave.id);
              await load(filter);
              Alert.alert('Đã duyệt', `Đã đánh dấu nghỉ có phép cho ${res.excusedSessions} buổi học.`);
            } catch (err) {
              Alert.alert('Không duyệt được', err instanceof ApiError ? err.message : 'Vui lòng thử lại');
            } finally {
              setBusyId(null);
            }
          },
        },
      ],
    );
  };

  if (!items && error) return <ErrorNotice message={error} onRetry={() => load(filter)} />;

  return (
    <>
      <Screen refreshControl={<RefreshControl refreshing={refreshing} onRefresh={refresh} tintColor={colors.primary} />}>
        <View style={s.filters}>
          {FILTERS.map((f) => (
            <Text
              key={f.key}
              accessibilityRole="button"
              onPress={() => {
                setFilter(f.key);
                setItems(null);
              }}
              style={[s.chip, filter === f.key ? s.chipActive : undefined]}
            >
              {f.label}
            </Text>
          ))}
        </View>

        {!items ? (
          <Loading />
        ) : items.length === 0 ? (
          <Card>
            <EmptyState
              title={filter === 'pending' ? 'Không còn đơn nào chờ duyệt' : 'Không có đơn nào'}
              description={filter === 'pending' ? 'Mọi đơn xin phép đã được xử lý.' : undefined}
            />
          </Card>
        ) : (
          items.map((leave) => {
            const tone = leaveStatusColor[leave.status];
            return (
              <Card key={leave.id}>
                <Row style={s.between}>
                  <View style={s.flex}>
                    <Heading>{leave.student.fullName}</Heading>
                    <Caption>{leave.student.code} · {leave.class?.code ?? 'Tất cả lớp'}</Caption>
                  </View>
                  <Badge label={leaveStatusLabel[leave.status].toUpperCase()} fg={tone.fg} bg={tone.bg} />
                </Row>

                <Row style={s.meta}>
                  <Text style={s.metaChip}>{leaveTypeLabel[leave.type]}</Text>
                  <Text style={s.metaChip}>
                    {leave.startDate === leave.endDate
                      ? formatDateKey(leave.startDate)
                      : `${formatDateKey(leave.startDate)} → ${formatDateKey(leave.endDate)}`}
                  </Text>
                </Row>

                <Body>{leave.reason}</Body>
                <Caption>Nộp {relativeTime(leave.createdAt)}</Caption>

                {leave.reviewNote ? (
                  <View style={s.reviewBox}>
                    <Caption>Ghi chú duyệt:</Caption>
                    <Body>{leave.reviewNote}</Body>
                  </View>
                ) : null}

                {leave.status === 'pending' ? (
                  <Row style={s.actions}>
                    <Button label="Từ chối" variant="ghost" onPress={() => setRejecting(leave)} style={s.flex} />
                    <Button
                      label="Phê duyệt"
                      onPress={() => approve(leave)}
                      loading={busyId === leave.id}
                      style={s.flex}
                    />
                  </Row>
                ) : null}
              </Card>
            );
          })
        )}
      </Screen>

      <RejectDialog
        leave={rejecting}
        onClose={() => setRejecting(null)}
        onDone={async () => {
          setRejecting(null);
          await load(filter);
        }}
      />
    </>
  );
}

function RejectDialog({
  leave,
  onClose,
  onDone,
}: {
  leave: LeaveRequest | null;
  onClose: () => void;
  onDone: () => void | Promise<void>;
}) {
  const [note, setNote] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  if (!leave) return null;

  const submit = async () => {
    if (note.trim().length < 3) {
      setError('Nhập lý do để sinh viên biết cần bổ sung gì.');
      return;
    }
    setBusy(true);
    setError(null);
    try {
      await api.rejectLeave(leave.id, note.trim());
      setNote('');
      await onDone();
    } catch (err) {
      setError(err instanceof ApiError ? err.message : 'Không từ chối được đơn');
    } finally {
      setBusy(false);
    }
  };

  return (
    <Modal transparent animationType="slide" visible onRequestClose={onClose}>
      <View style={s.backdrop}>
        <View style={s.dialog}>
          <Heading>Từ chối đơn của {leave.student.fullName}</Heading>
          <Field label="Lý do từ chối" error={error}>
            <Input
              value={note}
              onChangeText={setNote}
              placeholder="Ví dụ: Em bổ sung giấy khám bệnh rồi nộp lại nhé."
              multiline
              numberOfLines={3}
              style={s.textarea}
            />
          </Field>
          <Row style={s.actions}>
            <Button label="Huỷ" variant="ghost" onPress={onClose} style={s.flex} />
            <Button label="Từ chối đơn" variant="danger" onPress={submit} loading={busy} style={s.flex} />
          </Row>
        </View>
      </View>
    </Modal>
  );
}

const s = StyleSheet.create({
  between: { justifyContent: 'space-between' },
  flex: { flex: 1 },
  actions: { gap: spacing.md, marginTop: spacing.sm },
  filters: { flexDirection: 'row', flexWrap: 'wrap', gap: spacing.sm },
  chip: {
    ...typography.caption,
    color: colors.text,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.sm,
    borderRadius: radius.pill,
    backgroundColor: colors.surface,
    borderWidth: 1,
    borderColor: colors.border,
    overflow: 'hidden',
  },
  chipActive: { backgroundColor: colors.primary, color: colors.textInverse, borderColor: colors.primary },
  meta: { flexWrap: 'wrap', gap: spacing.sm },
  metaChip: {
    ...typography.tiny,
    color: colors.textMuted,
    backgroundColor: colors.background,
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.xs,
    borderRadius: radius.pill,
    overflow: 'hidden',
  },
  reviewBox: { backgroundColor: colors.background, borderRadius: radius.sm, padding: spacing.md, gap: spacing.xs },
  backdrop: { flex: 1, backgroundColor: colors.overlay, justifyContent: 'flex-end' },
  dialog: {
    backgroundColor: colors.surface,
    borderTopLeftRadius: radius.lg,
    borderTopRightRadius: radius.lg,
    padding: spacing.xl,
    gap: spacing.lg,
  },
  textarea: { minHeight: 90, textAlignVertical: 'top', paddingTop: spacing.md },
});

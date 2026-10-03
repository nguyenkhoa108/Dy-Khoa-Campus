import React, { useCallback, useState } from 'react';
import { RefreshControl, StyleSheet, Text, View } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { api } from '../../api/endpoints';
import { ApiError } from '../../api/client';
import { useAuth } from '../../state/AuthContext';
import { Badge, Body, Caption, Card, EmptyState, ErrorNotice, Heading, Loading, Row, Screen } from '../../components/ui';
import { attendanceColor, attendanceLabel } from '../../utils/labels';
import { formatDate, formatRange } from '../../utils/datetime';
import { colors, radius, spacing, typography } from '../../theme';
import type { AttendanceHistory, ClassSummary } from '../../api/types';

export default function AttendanceHistoryScreen() {
  const { classes } = useAuth();
  const [history, setHistory] = useState<AttendanceHistory | null>(null);
  const [classId, setClassId] = useState<string | undefined>(undefined);
  const [error, setError] = useState<string | null>(null);
  const [refreshing, setRefreshing] = useState(false);

  const load = useCallback(
    async (filter?: string) => {
      try {
        setHistory(await api.attendanceHistory({ classId: filter, limit: 100 }));
        setError(null);
      } catch (err) {
        setError(err instanceof ApiError ? err.message : 'Không tải được lịch sử');
      }
    },
    [],
  );

  useFocusEffect(
    useCallback(() => {
      load(classId);
    }, [load, classId]),
  );

  const refresh = useCallback(async () => {
    setRefreshing(true);
    await load(classId);
    setRefreshing(false);
  }, [load, classId]);

  const selectClass = (next?: string) => {
    setClassId(next);
    setHistory(null);
    load(next);
  };

  if (!history && error) return <ErrorNotice message={error} onRetry={() => load(classId)} />;

  return (
    <Screen refreshControl={<RefreshControl refreshing={refreshing} onRefresh={refresh} tintColor={colors.primary} />}>
      <ClassFilter classes={classes} selected={classId} onSelect={selectClass} />

      {!history ? (
        <Loading />
      ) : (
        <>
          <Card>
            <Heading>Tổng kết</Heading>
            <Row style={s.statRow}>
              <Stat label="Có mặt" value={history.summary.present} color={colors.success} />
              <Stat label="Đi muộn" value={history.summary.late} color={colors.warning} />
              <Stat label="Có phép" value={history.summary.excused} color={colors.info} />
              <Stat label="Vắng" value={history.summary.absent} color={colors.danger} />
            </Row>
            <Caption>
              {history.summary.absent > 0
                ? `Bạn đã vắng không phép ${history.summary.absent} buổi. Hãy nộp đơn xin phép trước khi nghỉ để không bị tính vắng.`
                : 'Bạn chưa có buổi vắng không phép nào.'}
            </Caption>
          </Card>

          {history.items.length === 0 ? (
            <Card>
              <EmptyState title="Chưa có bản ghi điểm danh" description="Lịch sử sẽ xuất hiện sau buổi học đầu tiên." />
            </Card>
          ) : (
            history.items.map((item) => {
              const tone = attendanceColor[item.status];
              return (
                <Card key={item.id}>
                  <Row style={s.between}>
                    <Body>{item.session.classCode}</Body>
                    <Badge label={attendanceLabel[item.status].toUpperCase()} fg={tone.fg} bg={tone.bg} />
                  </Row>
                  <Body>{item.session.title}</Body>
                  <Caption>
                    {formatDate(item.session.startsAt)} · {formatRange(item.session.startsAt, item.session.endsAt)}
                    {item.session.room ? ` · ${item.session.room}` : ''}
                  </Caption>
                  {item.note ? <Caption>Ghi chú: {item.note}</Caption> : null}
                </Card>
              );
            })
          )}
        </>
      )}
    </Screen>
  );
}

function ClassFilter({
  classes,
  selected,
  onSelect,
}: {
  classes: ClassSummary[];
  selected?: string;
  onSelect: (id?: string) => void;
}) {
  return (
    <View style={s.filterRow}>
      <Chip label="Tất cả" active={!selected} onPress={() => onSelect(undefined)} />
      {classes.map((c) => (
        <Chip key={c.id} label={c.code} active={selected === c.id} onPress={() => onSelect(c.id)} />
      ))}
    </View>
  );
}

function Chip({ label, active, onPress }: { label: string; active: boolean; onPress: () => void }) {
  return (
    <Text
      accessibilityRole="button"
      onPress={onPress}
      style={[s.chip, active ? s.chipActive : undefined]}
    >
      {label}
    </Text>
  );
}

function Stat({ label, value, color }: { label: string; value: number; color: string }) {
  return (
    <View style={s.stat}>
      <Text style={[s.statValue, { color }]}>{value}</Text>
      <Text style={s.statLabel}>{label}</Text>
    </View>
  );
}

const s = StyleSheet.create({
  between: { justifyContent: 'space-between' },
  filterRow: { flexDirection: 'row', flexWrap: 'wrap', gap: spacing.sm },
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
  statRow: { justifyContent: 'space-between', marginVertical: spacing.sm },
  stat: { flex: 1, alignItems: 'center', backgroundColor: colors.background, borderRadius: radius.sm, paddingVertical: spacing.md },
  statValue: { fontSize: 20, fontWeight: '700' },
  statLabel: { ...typography.tiny, color: colors.textMuted, marginTop: 2 },
});

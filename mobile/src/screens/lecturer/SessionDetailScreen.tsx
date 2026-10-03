import React, { useCallback, useState } from 'react';
import { Alert, RefreshControl, StyleSheet, Text, View } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { api } from '../../api/endpoints';
import { ApiError } from '../../api/client';
import { Badge, Body, Button, Caption, Card, ErrorNotice, Heading, Loading, Row, Screen } from '../../components/ui';
import { attendanceColor, attendanceLabel } from '../../utils/labels';
import { formatDate, formatRange, formatTime } from '../../utils/datetime';
import { colors, radius, spacing, typography } from '../../theme';
import type { AttendanceStatus, RosterEntry, SessionAttendance } from '../../api/types';

/** Danh sách điểm danh của một buổi: theo dõi, sửa tay và đóng buổi. */
export default function SessionDetailScreen({ route, navigation }: { route: any; navigation: any }) {
  const sessionId = route.params.sessionId as string;

  const [data, setData] = useState<SessionAttendance | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [refreshing, setRefreshing] = useState(false);
  const [busyId, setBusyId] = useState<string | null>(null);

  const load = useCallback(async () => {
    try {
      setData(await api.sessionAttendance(sessionId));
      setError(null);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : 'Không tải được danh sách');
    }
  }, [sessionId]);

  useFocusEffect(
    useCallback(() => {
      load();
    }, [load]),
  );

  const refresh = useCallback(async () => {
    setRefreshing(true);
    await load();
    setRefreshing(false);
  }, [load]);

  const mark = async (studentId: string, status: AttendanceStatus) => {
    setBusyId(studentId);
    try {
      await api.markAttendance(sessionId, studentId, status);
      await load();
    } catch (err) {
      Alert.alert('Không ghi nhận được', err instanceof ApiError ? err.message : 'Vui lòng thử lại');
    } finally {
      setBusyId(null);
    }
  };

  const toggleSession = async () => {
    if (!data) return;
    const opening = data.session.checkinState === 'closed';

    if (!opening) {
      Alert.alert('Đóng điểm danh', 'Sinh viên chưa quét sẽ bị tính là vắng. Tiếp tục?', [
        { text: 'Huỷ', style: 'cancel' },
        {
          text: 'Đóng buổi',
          style: 'destructive',
          onPress: async () => {
            try {
              const res = await api.closeSession(sessionId);
              Alert.alert('Đã đóng điểm danh', `${res.markedAbsent} sinh viên bị tính vắng.`);
              await load();
            } catch (err) {
              Alert.alert('Lỗi', err instanceof ApiError ? err.message : 'Không đóng được buổi học');
            }
          },
        },
      ]);
      return;
    }

    try {
      await api.openSession(sessionId);
      await load();
    } catch (err) {
      Alert.alert('Lỗi', err instanceof ApiError ? err.message : 'Không mở được buổi học');
    }
  };

  if (!data && error) return <ErrorNotice message={error} onRetry={load} />;
  if (!data) return <Loading />;

  const { session, summary } = data;
  const roster = data.items as RosterEntry[];
  const isOpen = session.checkinState === 'open';

  return (
    <Screen refreshControl={<RefreshControl refreshing={refreshing} onRefresh={refresh} tintColor={colors.primary} />}>
      <Card>
        <Row style={s.between}>
          <Heading>{session.title}</Heading>
          <Badge
            label={isOpen ? 'ĐANG MỞ' : 'ĐÃ ĐÓNG'}
            fg={isOpen ? colors.success : colors.textMuted}
            bg={isOpen ? colors.successSoft : colors.border}
          />
        </Row>
        <Caption>
          {formatDate(session.startsAt)} · {formatRange(session.startsAt, session.endsAt)}
          {session.room ? ` · Phòng ${session.room}` : ''}
        </Caption>
        <Caption>Quét sau {formatTime(session.startsAt)} + {session.lateAfterMin} phút sẽ tính là đi muộn.</Caption>

        {summary ? (
          <Row style={s.statRow}>
            <Stat label="Có mặt" value={summary.present} color={colors.success} />
            <Stat label="Muộn" value={summary.late} color={colors.warning} />
            <Stat label="Phép" value={summary.excused} color={colors.info} />
            <Stat label="Vắng" value={summary.absent} color={colors.danger} />
            <Stat label="Chưa" value={summary.pending} color={colors.textMuted} />
          </Row>
        ) : null}

        {isOpen ? (
          <>
            <Row style={s.actions}>
              <Button
                label="Chiếu mã QR"
                onPress={() => navigation.navigate('SessionQr', { sessionId, title: session.title })}
                style={s.flex}
              />
              <Button
                label="Quét SV"
                variant="secondary"
                onPress={() => navigation.navigate('ScanStudent', { sessionId, title: session.title })}
                style={s.flex}
              />
            </Row>
            <Button label="Đóng điểm danh" variant="danger" onPress={toggleSession} />
          </>
        ) : (
          <Button label="Mở điểm danh" onPress={toggleSession} />
        )}
      </Card>

      <Heading>Danh sách sinh viên</Heading>
      {roster.map((entry) => {
        const tone = entry.status ? attendanceColor[entry.status] : { fg: colors.textMuted, bg: colors.border };
        return (
          <Card key={entry.studentId}>
            <Row style={s.between}>
              <View style={s.flex}>
                <Body>{entry.fullName}</Body>
                <Caption>{entry.studentCode}</Caption>
              </View>
              <Badge label={entry.status ? attendanceLabel[entry.status].toUpperCase() : 'CHƯA ĐIỂM DANH'} fg={tone.fg} bg={tone.bg} />
            </Row>

            {entry.checkedInAt ? <Caption>Quét lúc {formatTime(entry.checkedInAt)}</Caption> : null}
            {entry.note ? <Caption>{entry.note}</Caption> : null}

            {/* Điểm danh tay: lối thoát khi camera hoặc điện thoại sinh viên có vấn đề. */}
            <Row style={s.markRow}>
              {(['present', 'late', 'excused', 'absent'] as AttendanceStatus[]).map((status) => (
                <Text
                  key={status}
                  accessibilityRole="button"
                  onPress={() => mark(entry.studentId, status)}
                  style={[
                    s.markChip,
                    entry.status === status && { backgroundColor: attendanceColor[status].bg, borderColor: attendanceColor[status].fg },
                    busyId === entry.studentId && s.markDisabled,
                  ]}
                >
                  {attendanceLabel[status]}
                </Text>
              ))}
            </Row>
          </Card>
        );
      })}
    </Screen>
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
  flex: { flex: 1 },
  actions: { gap: spacing.md },
  statRow: { justifyContent: 'space-between', marginVertical: spacing.sm },
  stat: { flex: 1, alignItems: 'center', backgroundColor: colors.background, borderRadius: radius.sm, paddingVertical: spacing.sm },
  statValue: { fontSize: 18, fontWeight: '700' },
  statLabel: { ...typography.tiny, color: colors.textMuted, marginTop: 2 },
  markRow: { flexWrap: 'wrap', gap: spacing.sm, marginTop: spacing.sm },
  markChip: {
    ...typography.tiny,
    color: colors.text,
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
    borderRadius: radius.pill,
    borderWidth: 1,
    borderColor: colors.border,
    backgroundColor: colors.background,
    overflow: 'hidden',
  },
  markDisabled: { opacity: 0.4 },
});

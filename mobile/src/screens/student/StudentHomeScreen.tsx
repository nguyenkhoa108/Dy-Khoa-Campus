import React, { useCallback, useState } from 'react';
import { RefreshControl, StyleSheet, Text, View } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { api } from '../../api/endpoints';
import { ApiError } from '../../api/client';
import { useAuth } from '../../state/AuthContext';
import { OfflineBanner } from '../../components/OfflineBanner';
import { Badge, Body, Button, Caption, Card, EmptyState, ErrorNotice, Heading, Loading, Row, Screen, Title } from '../../components/ui';
import { attendanceColor, attendanceLabel } from '../../utils/labels';
import { formatRange, formatWeekday, isToday, formatDate } from '../../utils/datetime';
import { colors, radius, spacing, typography } from '../../theme';
import type { AttendanceHistory, ClassSession, LeaveRequest } from '../../api/types';

interface Data {
  openSessions: ClassSession[];
  history: AttendanceHistory;
  leaves: LeaveRequest[];
}

export default function StudentHomeScreen({ navigation }: { navigation: any }) {
  const { user } = useAuth();
  const [data, setData] = useState<Data | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [refreshing, setRefreshing] = useState(false);

  const load = useCallback(async () => {
    try {
      const [openSessions, history, leaves] = await Promise.all([
        api.openSessions(),
        api.attendanceHistory({ limit: 5 }),
        api.leaveRequests({ limit: 3 }),
      ]);
      setData({ openSessions: openSessions.items, history, leaves: leaves.items });
      setError(null);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : 'Không tải được dữ liệu');
    }
  }, []);

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

  if (!data && error) return <ErrorNotice message={error} onRetry={load} />;
  if (!data) return <Loading />;

  const { openSessions, history, leaves } = data;
  const attendanceRate = history.summary.total
    ? Math.round(((history.summary.present + history.summary.late) / history.summary.total) * 100)
    : null;

  return (
    <>
      <OfflineBanner />
      <Screen refreshControl={<RefreshControl refreshing={refreshing} onRefresh={refresh} tintColor={colors.primary} />}>
        <View>
          <Caption>Xin chào,</Caption>
          <Title>{user?.fullName}</Title>
          <Caption>{user?.code} · {user?.faculty ?? 'Sinh viên'}</Caption>
        </View>

        {/* Buổi đang mở điểm danh là việc cần làm ngay — đặt trên cùng. */}
        <View style={s.section}>
          <Heading>Đang mở điểm danh</Heading>
          {openSessions.length === 0 ? (
            <Card>
              <EmptyState title="Chưa có buổi nào mở điểm danh" description="Khi giảng viên mở điểm danh, buổi học sẽ hiện ở đây." />
            </Card>
          ) : (
            openSessions.map((session) => (
              <Card key={session.id} style={s.openCard}>
                <Row style={s.between}>
                  <Badge label="ĐANG MỞ" fg={colors.success} bg={colors.successSoft} />
                  <Caption>{isToday(session.startsAt) ? 'Hôm nay' : formatDate(session.startsAt)}</Caption>
                </Row>
                <Heading>{session.classCode} · {session.className}</Heading>
                <Body>{session.title}</Body>
                <Caption>
                  {formatWeekday(session.startsAt)} · {formatRange(session.startsAt, session.endsAt)}
                  {session.room ? ` · Phòng ${session.room}` : ''}
                </Caption>
                <Button label="Quét mã điểm danh" onPress={() => navigation.navigate('Quét QR')} />
              </Card>
            ))
          )}
        </View>

        <View style={s.section}>
          <Heading>Chuyên cần</Heading>
          <Card>
            {attendanceRate === null ? (
              <Caption>Chưa có dữ liệu điểm danh.</Caption>
            ) : (
              <>
                <Row style={s.between}>
                  <Text style={s.rate}>{attendanceRate}%</Text>
                  <Caption>{history.summary.total} buổi đã ghi nhận</Caption>
                </Row>
                <Row style={s.statRow}>
                  <Stat label="Có mặt" value={history.summary.present} color={colors.success} />
                  <Stat label="Đi muộn" value={history.summary.late} color={colors.warning} />
                  <Stat label="Có phép" value={history.summary.excused} color={colors.info} />
                  <Stat label="Vắng" value={history.summary.absent} color={colors.danger} />
                </Row>
              </>
            )}
            <Button label="Xem lịch sử điểm danh" variant="secondary" onPress={() => navigation.navigate('Lịch sử')} />
          </Card>
        </View>

        <View style={s.section}>
          <Row style={s.between}>
            <Heading>Đơn xin phép gần đây</Heading>
          </Row>
          {leaves.length === 0 ? (
            <Card>
              <EmptyState title="Chưa có đơn nào" description="Bạn có thể nộp đơn xin phép từ tab Xin phép." />
            </Card>
          ) : (
            leaves.map((leave) => (
              <Card key={leave.id} onPress={() => navigation.navigate('Xin phép')}>
                <Row style={s.between}>
                  <Body>{leave.class?.code ?? 'Tất cả lớp'}</Body>
                  <Badge
                    label={leave.status === 'pending' ? 'CHỜ DUYỆT' : leave.status === 'approved' ? 'ĐÃ DUYỆT' : leave.status === 'rejected' ? 'TỪ CHỐI' : 'ĐÃ RÚT'}
                    fg={leave.status === 'approved' ? colors.success : leave.status === 'rejected' ? colors.danger : colors.warning}
                    bg={leave.status === 'approved' ? colors.successSoft : leave.status === 'rejected' ? colors.dangerSoft : colors.warningSoft}
                  />
                </Row>
                <Caption>{leave.startDate === leave.endDate ? leave.startDate : `${leave.startDate} → ${leave.endDate}`}</Caption>
              </Card>
            ))
          )}
        </View>

        {history.items.length > 0 ? (
          <View style={s.section}>
            <Heading>Buổi học gần nhất</Heading>
            {history.items.slice(0, 3).map((item) => {
              const tone = attendanceColor[item.status];
              return (
                <Card key={item.id}>
                  <Row style={s.between}>
                    <Body>{item.session.classCode}</Body>
                    <Badge label={attendanceLabel[item.status].toUpperCase()} fg={tone.fg} bg={tone.bg} />
                  </Row>
                  <Caption>{item.session.title}</Caption>
                  <Caption>{formatDate(item.session.startsAt)} · {formatRange(item.session.startsAt, item.session.endsAt)}</Caption>
                </Card>
              );
            })}
          </View>
        ) : null}
      </Screen>
    </>
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
  section: { gap: spacing.md },
  between: { justifyContent: 'space-between' },
  openCard: { borderColor: colors.success, borderWidth: 1.5 },
  rate: { fontSize: 36, fontWeight: '800', color: colors.primary },
  statRow: { justifyContent: 'space-between', marginVertical: spacing.sm },
  stat: { flex: 1, alignItems: 'center', backgroundColor: colors.background, borderRadius: radius.sm, paddingVertical: spacing.md },
  statValue: { fontSize: 20, fontWeight: '700' },
  statLabel: { ...typography.tiny, color: colors.textMuted, marginTop: 2 },
});

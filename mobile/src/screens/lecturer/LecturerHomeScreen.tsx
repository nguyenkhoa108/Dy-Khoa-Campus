import React, { useCallback, useState } from 'react';
import { RefreshControl, StyleSheet, Text, View } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { api } from '../../api/endpoints';
import { ApiError } from '../../api/client';
import { useAuth } from '../../state/AuthContext';
import { OfflineBanner } from '../../components/OfflineBanner';
import { Badge, Body, Button, Caption, Card, EmptyState, ErrorNotice, Heading, Loading, Row, Screen, Title } from '../../components/ui';
import { formatDate, formatRange, formatWeekday, isToday } from '../../utils/datetime';
import { colors, spacing, typography } from '../../theme';
import type { ClassSession, ClassSummary } from '../../api/types';

export default function LecturerHomeScreen({ navigation }: { navigation: any }) {
  const { user } = useAuth();
  const [classes, setClasses] = useState<ClassSummary[] | null>(null);
  const [openSessions, setOpenSessions] = useState<ClassSession[]>([]);
  const [pendingLeaves, setPendingLeaves] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const [refreshing, setRefreshing] = useState(false);

  const load = useCallback(async () => {
    try {
      const [classList, open, pending] = await Promise.all([
        api.classes(),
        api.openSessions(),
        api.pendingLeaveCount(),
      ]);
      setClasses(classList.items);
      setOpenSessions(open.items);
      setPendingLeaves(pending.pending);
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

  if (!classes && error) return <ErrorNotice message={error} onRetry={load} />;
  if (!classes) return <Loading />;

  return (
    <>
      <OfflineBanner />
      <Screen refreshControl={<RefreshControl refreshing={refreshing} onRefresh={refresh} tintColor={colors.primary} />}>
        <View>
          <Caption>Xin chào,</Caption>
          <Title>{user?.fullName}</Title>
          <Caption>{user?.code} · {user?.faculty ?? 'Giảng viên'}</Caption>
        </View>

        {pendingLeaves > 0 ? (
          <Card style={s.alertCard} onPress={() => navigation.navigate('Duyệt phép')}>
            <Row style={s.between}>
              <View style={s.flex}>
                <Heading>{pendingLeaves} đơn xin phép chờ duyệt</Heading>
                <Caption>Chạm để xem và xử lý.</Caption>
              </View>
              <Badge label="CẦN XỬ LÝ" fg={colors.warning} bg={colors.warningSoft} />
            </Row>
          </Card>
        ) : null}

        <View style={s.section}>
          <Heading>Buổi đang mở điểm danh</Heading>
          {openSessions.length === 0 ? (
            <Card>
              <EmptyState
                title="Chưa mở buổi nào"
                description="Chọn một lớp bên dưới, tạo hoặc mở buổi học rồi chiếu mã QR cho sinh viên quét."
              />
            </Card>
          ) : (
            openSessions.map((session) => (
              <Card key={session.id} style={s.openCard}>
                <Row style={s.between}>
                  <Badge label="ĐANG MỞ" fg={colors.success} bg={colors.successSoft} />
                  <Caption>{isToday(session.startsAt) ? 'Hôm nay' : formatDate(session.startsAt)}</Caption>
                </Row>
                <Heading>{session.classCode} · {session.title}</Heading>
                <Caption>
                  {formatWeekday(session.startsAt)} · {formatRange(session.startsAt, session.endsAt)}
                  {session.room ? ` · Phòng ${session.room}` : ''}
                </Caption>
                <Row style={s.actions}>
                  <Button
                    label="Chiếu mã QR"
                    onPress={() => navigation.navigate('SessionQr', { sessionId: session.id, title: session.title })}
                    style={s.flex}
                  />
                  <Button
                    label="Quét SV"
                    variant="secondary"
                    onPress={() => navigation.navigate('ScanStudent', { sessionId: session.id, title: session.title })}
                    style={s.flex}
                  />
                </Row>
                <Button
                  label="Xem danh sách điểm danh"
                  variant="ghost"
                  onPress={() => navigation.navigate('SessionDetail', { sessionId: session.id })}
                />
              </Card>
            ))
          )}
        </View>

        <View style={s.section}>
          <Heading>Lớp học phần phụ trách</Heading>
          {classes.length === 0 ? (
            <Card>
              <EmptyState title="Chưa được phân công lớp nào" />
            </Card>
          ) : (
            classes.map((c) => (
              <Card key={c.id} onPress={() => navigation.navigate('ClassSessions', { classId: c.id, code: c.code })}>
                <Row style={s.between}>
                  <Body>{c.code}</Body>
                  <Caption>{c.studentCount ?? 0} sinh viên</Caption>
                </Row>
                <Text style={s.className}>{c.name}</Text>
                <Caption>Học kỳ {c.term}{c.room ? ` · Phòng ${c.room}` : ''}</Caption>
              </Card>
            ))
          )}
        </View>
      </Screen>
    </>
  );
}

const s = StyleSheet.create({
  section: { gap: spacing.md },
  between: { justifyContent: 'space-between' },
  flex: { flex: 1 },
  actions: { gap: spacing.md },
  openCard: { borderColor: colors.success, borderWidth: 1.5 },
  alertCard: { borderColor: colors.warning, borderWidth: 1.5, backgroundColor: colors.warningSoft },
  className: { ...typography.subheading, color: colors.text },
});

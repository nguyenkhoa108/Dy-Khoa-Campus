import React, { useCallback, useState } from 'react';
import { Alert, RefreshControl, StyleSheet, View } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { api } from '../../api/endpoints';
import { ApiError } from '../../api/client';
import { Badge, Body, Button, Caption, Card, EmptyState, ErrorNotice, Heading, Loading, Row, Screen } from '../../components/ui';
import { formatDate, formatRange, formatWeekday, isToday } from '../../utils/datetime';
import { colors, spacing } from '../../theme';
import type { ClassSession } from '../../api/types';

/** Tất cả buổi học của một lớp, kèm nút tạo nhanh buổi cho hôm nay. */
export default function ClassSessionsScreen({ route, navigation }: { route: any; navigation: any }) {
  const classId = route.params.classId as string;

  const [sessions, setSessions] = useState<ClassSession[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [refreshing, setRefreshing] = useState(false);
  const [creating, setCreating] = useState(false);

  const load = useCallback(async () => {
    try {
      setSessions((await api.classSessions(classId)).items);
      setError(null);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : 'Không tải được danh sách buổi học');
    }
  }, [classId]);

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

  /** Tạo buổi bắt đầu ngay bây giờ — trường hợp hay gặp nhất khi đứng lớp. */
  const createNow = async () => {
    setCreating(true);
    try {
      const startsAt = new Date();
      const endsAt = new Date(startsAt.getTime() + 2 * 60 * 60 * 1000);
      const res = await api.createSession({
        classId,
        title: `Buổi học ngày ${formatDate(startsAt.toISOString())}`,
        startsAt: startsAt.toISOString(),
        endsAt: endsAt.toISOString(),
      });
      await api.openSession(res.session.id);
      await load();
      navigation.navigate('SessionQr', { sessionId: res.session.id, title: res.session.title });
    } catch (err) {
      Alert.alert('Không tạo được buổi học', err instanceof ApiError ? err.message : 'Vui lòng thử lại');
    } finally {
      setCreating(false);
    }
  };

  if (!sessions && error) return <ErrorNotice message={error} onRetry={load} />;

  return (
    <Screen refreshControl={<RefreshControl refreshing={refreshing} onRefresh={refresh} tintColor={colors.primary} />}>
      <Button label="+ Mở buổi điểm danh ngay" onPress={createNow} loading={creating} />

      {!sessions ? (
        <Loading />
      ) : sessions.length === 0 ? (
        <Card>
          <EmptyState title="Lớp chưa có buổi học nào" description="Dùng nút trên để mở buổi điểm danh đầu tiên." />
        </Card>
      ) : (
        sessions.map((session) => {
          const open = session.checkinState === 'open';
          return (
            <Card key={session.id} onPress={() => navigation.navigate('SessionDetail', { sessionId: session.id })}>
              <Row style={s.between}>
                <View style={s.flex}>
                  <Heading>{session.title}</Heading>
                </View>
                {open ? <Badge label="ĐANG MỞ" fg={colors.success} bg={colors.successSoft} /> : null}
              </Row>
              <Caption>
                {isToday(session.startsAt) ? 'Hôm nay' : formatWeekday(session.startsAt)} ·{' '}
                {formatDate(session.startsAt)} · {formatRange(session.startsAt, session.endsAt)}
              </Caption>
              {session.room ? <Body>Phòng {session.room}</Body> : null}
            </Card>
          );
        })
      )}
    </Screen>
  );
}

const s = StyleSheet.create({
  between: { justifyContent: 'space-between' },
  flex: { flex: 1 },
});

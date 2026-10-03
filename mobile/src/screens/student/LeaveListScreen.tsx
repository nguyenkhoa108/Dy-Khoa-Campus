import React, { useCallback, useState } from 'react';
import { Alert, RefreshControl, StyleSheet, View } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { api } from '../../api/endpoints';
import { ApiError } from '../../api/client';
import { Badge, Body, Button, Caption, Card, EmptyState, ErrorNotice, Loading, Row, Screen } from '../../components/ui';
import { leaveStatusColor, leaveStatusLabel, leaveTypeLabel } from '../../utils/labels';
import { formatDateKey } from '../../utils/datetime';
import { colors, spacing } from '../../theme';
import type { LeaveRequest } from '../../api/types';

export default function LeaveListScreen({ navigation }: { navigation: any }) {
  const [items, setItems] = useState<LeaveRequest[] | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [refreshing, setRefreshing] = useState(false);

  const load = useCallback(async () => {
    try {
      setItems((await api.leaveRequests({ limit: 50 })).items);
      setError(null);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : 'Không tải được danh sách đơn');
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

  const cancel = (leave: LeaveRequest) => {
    Alert.alert('Rút đơn xin phép', 'Bạn chắc chắn muốn rút đơn này?', [
      { text: 'Không', style: 'cancel' },
      {
        text: 'Rút đơn',
        style: 'destructive',
        onPress: async () => {
          try {
            await api.cancelLeave(leave.id);
            await load();
          } catch (err) {
            Alert.alert('Không rút được đơn', err instanceof ApiError ? err.message : 'Vui lòng thử lại');
          }
        },
      },
    ]);
  };

  if (!items && error) return <ErrorNotice message={error} onRetry={load} />;

  return (
    <Screen refreshControl={<RefreshControl refreshing={refreshing} onRefresh={refresh} tintColor={colors.primary} />}>
      <Button label="+ Nộp đơn xin phép" onPress={() => navigation.navigate('NewLeave')} />

      {!items ? (
        <Loading />
      ) : items.length === 0 ? (
        <Card>
          <EmptyState
            title="Chưa có đơn xin phép nào"
            description="Nộp đơn trước buổi học để buổi đó được tính là nghỉ có phép thay vì vắng."
          />
        </Card>
      ) : (
        items.map((leave) => {
          const tone = leaveStatusColor[leave.status];
          return (
            <Card key={leave.id}>
              <Row style={s.between}>
                <Body>{leave.class?.code ?? 'Tất cả lớp'}</Body>
                <Badge label={leaveStatusLabel[leave.status].toUpperCase()} fg={tone.fg} bg={tone.bg} />
              </Row>
              <Caption>
                {leaveTypeLabel[leave.type]} ·{' '}
                {leave.startDate === leave.endDate
                  ? formatDateKey(leave.startDate)
                  : `${formatDateKey(leave.startDate)} → ${formatDateKey(leave.endDate)}`}
              </Caption>
              <Body>{leave.reason}</Body>

              {leave.reviewNote ? (
                <View style={s.reviewBox}>
                  <Caption>Phản hồi từ {leave.reviewerName ?? 'người duyệt'}:</Caption>
                  <Body>{leave.reviewNote}</Body>
                </View>
              ) : null}

              {leave.status === 'pending' ? (
                <Button label="Rút đơn" variant="ghost" onPress={() => cancel(leave)} />
              ) : null}
            </Card>
          );
        })
      )}
    </Screen>
  );
}

const s = StyleSheet.create({
  between: { justifyContent: 'space-between' },
  reviewBox: { backgroundColor: colors.background, borderRadius: 8, padding: spacing.md, gap: spacing.xs },
});

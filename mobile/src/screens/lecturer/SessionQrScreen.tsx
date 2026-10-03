import React, { useCallback, useEffect, useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { api } from '../../api/endpoints';
import { ApiError } from '../../api/client';
import { RotatingQr } from '../../components/RotatingQr';
import { Body, Caption, Card, Heading, Row, Screen } from '../../components/ui';
import { colors, radius, spacing, typography } from '../../theme';

/**
 * Màn hình chiếu mã QR cho cả lớp quét.
 * Có đếm sĩ số đã điểm danh cập nhật liên tục để giảng viên biết khi nào nên đóng.
 */
export default function SessionQrScreen({ route }: { route: any }) {
  const sessionId = route.params.sessionId as string;
  const title = route.params.title as string | undefined;

  const [counts, setCounts] = useState<{ checkedIn: number; total: number } | null>(null);
  const [error, setError] = useState<string | null>(null);

  const fetchToken = useCallback(() => api.sessionQr(sessionId), [sessionId]);

  // Theo dõi tiến độ điểm danh trong lúc mã đang chiếu.
  useEffect(() => {
    let active = true;

    const poll = async () => {
      try {
        const res = await api.sessionAttendance(sessionId);
        if (!active || !res.summary) return;
        setCounts({ checkedIn: res.summary.present + res.summary.late, total: res.summary.total });
        setError(null);
      } catch (err) {
        if (active && err instanceof ApiError && !err.isNetworkError) setError(err.message);
      }
    };

    poll();
    const id = setInterval(poll, 5000);
    return () => {
      active = false;
      clearInterval(id);
    };
  }, [sessionId]);

  return (
    <Screen>
      {title ? <Heading>{title}</Heading> : null}

      <Card>
        <RotatingQr
          fetchToken={fetchToken}
          size={260}
          caption="Chiếu màn hình này lên máy chiếu. Mã tự đổi vài giây một lần."
        />
      </Card>

      <Card>
        <Row style={s.between}>
          <Body>Đã điểm danh</Body>
          <Text style={s.counter}>
            {counts ? `${counts.checkedIn}/${counts.total}` : '…'}
          </Text>
        </Row>
        {counts ? (
          <View style={s.track}>
            <View style={[s.fill, { width: `${counts.total ? (counts.checkedIn / counts.total) * 100 : 0}%` }]} />
          </View>
        ) : null}
        <Caption>Số liệu cập nhật mỗi 5 giây.</Caption>
        {error ? <Text style={s.error}>{error}</Text> : null}
      </Card>

      <Caption>
        Sinh viên không quét được (hết pin, hỏng camera) có thể mở mã QR cá nhân để bạn quét, hoặc bạn điểm danh tay
        trong màn hình danh sách.
      </Caption>
    </Screen>
  );
}

const s = StyleSheet.create({
  between: { justifyContent: 'space-between' },
  counter: { fontSize: 28, fontWeight: '800', color: colors.primary },
  track: { height: 10, borderRadius: radius.sm, backgroundColor: colors.border, overflow: 'hidden' },
  fill: { height: 10, borderRadius: radius.sm, backgroundColor: colors.success },
  error: { ...typography.caption, color: colors.danger },
});

import React, { useCallback } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { api } from '../../api/endpoints';
import { useAuth } from '../../state/AuthContext';
import { RotatingQr } from '../../components/RotatingQr';
import { Body, Caption, Card, Screen } from '../../components/ui';
import { colors, spacing, typography } from '../../theme';

/** Mã QR cá nhân để giảng viên quét — chiều điểm danh ngược lại. */
export default function MyQrScreen() {
  const { user } = useAuth();
  const fetchToken = useCallback(() => api.myQr(), []);

  return (
    <Screen>
      <Card style={s.identity}>
        <Text style={s.name}>{user?.fullName}</Text>
        <Text style={s.code}>{user?.code}</Text>
        {user?.faculty ? <Caption>{user.faculty}</Caption> : null}
      </Card>

      <Card>
        <RotatingQr fetchToken={fetchToken} caption="Mã tự đổi liên tục — đưa màn hình này cho giảng viên quét." />
      </Card>

      <View style={s.note}>
        <Body muted>Vì sao mã luôn đổi?</Body>
        <Caption>
          Mỗi mã chỉ có hiệu lực trong ít giây và được máy chủ ký riêng, nên ảnh chụp màn hình gửi cho bạn bè sẽ không
          điểm danh hộ được.
        </Caption>
      </View>
    </Screen>
  );
}

const s = StyleSheet.create({
  identity: { alignItems: 'center' },
  name: { ...typography.title, color: colors.text, textAlign: 'center' },
  code: { ...typography.heading, color: colors.primary, letterSpacing: 1 },
  note: { gap: spacing.xs, paddingHorizontal: spacing.sm },
});

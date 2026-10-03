import React, { useEffect, useState } from 'react';
import { Alert, StyleSheet, Text, View } from 'react-native';
import { getApiBaseUrl, getDefaultApiBaseUrl, setApiBaseUrl } from '../config';
import { useAuth } from '../state/AuthContext';
import { useScanQueue } from '../state/ScanQueueContext';
import { ApiError } from '../api/client';
import { Body, Button, Caption, Card, Divider, Field, Heading, Input, Row, Screen } from '../components/ui';
import { roleLabel } from '../utils/labels';
import { relativeTime } from '../utils/datetime';
import { colors, spacing, typography } from '../theme';

export default function SettingsScreen() {
  const { user, signOut } = useAuth();
  const { queue, isOnline, isSyncing, lastSyncAt, sync, clearFailed } = useScanQueue();

  const [baseUrl, setBaseUrl] = useState('');
  const [saved, setSaved] = useState(false);

  useEffect(() => {
    getApiBaseUrl().then(setBaseUrl);
  }, []);

  const saveBaseUrl = async () => {
    await setApiBaseUrl(baseUrl);
    setSaved(true);
    Alert.alert(
      'Đã lưu địa chỉ máy chủ',
      'Hãy đăng xuất rồi đăng nhập lại để mọi màn hình dùng địa chỉ mới.',
    );
  };

  const syncNow = async () => {
    try {
      const res = await sync();
      Alert.alert(
        'Đồng bộ xong',
        res ? `Đã gửi ${res.accepted} lượt, ${res.rejected} lượt bị từ chối.` : 'Không có lượt nào chờ gửi.',
      );
    } catch (err) {
      Alert.alert('Đồng bộ thất bại', err instanceof ApiError ? err.message : 'Vui lòng thử lại');
    }
  };

  return (
    <Screen>
      {user ? (
        <Card>
          <Heading>{user.fullName}</Heading>
          <Caption>{user.code} · {roleLabel[user.role]}</Caption>
          <Caption>{user.email}</Caption>
          {user.faculty ? <Caption>{user.faculty}</Caption> : null}
        </Card>
      ) : null}

      <Card>
        <Heading>Hàng đợi điểm danh</Heading>
        <Row style={s.between}>
          <Body>Trạng thái mạng</Body>
          <Text style={[s.status, { color: isOnline ? colors.success : colors.danger }]}>
            {isOnline ? 'Trực tuyến' : 'Ngoại tuyến'}
          </Text>
        </Row>
        <Row style={s.between}>
          <Body>Lượt quét chờ gửi</Body>
          <Text style={s.status}>{queue.length}</Text>
        </Row>
        {lastSyncAt ? <Caption>Đồng bộ gần nhất: {relativeTime(lastSyncAt)}</Caption> : null}

        {queue.length > 0 ? (
          <>
            <Divider />
            {queue.slice(0, 5).map((item) => (
              <View key={item.clientUuid} style={s.queueItem}>
                <Body>{item.label}</Body>
                <Caption>
                  {relativeTime(item.queuedAt)}
                  {item.attempts > 0 ? ` · đã thử ${item.attempts} lần` : ''}
                  {item.lastError ? ` · ${item.lastError}` : ''}
                </Caption>
              </View>
            ))}
            <Button label="Đồng bộ ngay" onPress={syncNow} loading={isSyncing} disabled={!isOnline} />
            <Button
              label="Xoá hàng đợi"
              variant="ghost"
              onPress={() =>
                Alert.alert('Xoá hàng đợi', 'Các lượt quét chưa gửi sẽ mất vĩnh viễn. Tiếp tục?', [
                  { text: 'Huỷ', style: 'cancel' },
                  { text: 'Xoá', style: 'destructive', onPress: () => clearFailed() },
                ])
              }
            />
          </>
        ) : (
          <Caption>Không có lượt quét nào đang chờ.</Caption>
        )}
      </Card>

      <Card>
        <Heading>Máy chủ</Heading>
        <Field
          label="Địa chỉ API"
          hint={`Mặc định: ${getDefaultApiBaseUrl()}. Khi chạy thử trên điện thoại thật, nhập IP LAN của máy chạy server, ví dụ http://192.168.1.10:4000/api/v1`}
        >
          <Input
            value={baseUrl}
            onChangeText={(v) => {
              setBaseUrl(v);
              setSaved(false);
            }}
            autoCapitalize="none"
            autoCorrect={false}
            keyboardType="url"
            placeholder="http://192.168.1.10:4000/api/v1"
          />
        </Field>
        <Button label={saved ? 'Đã lưu' : 'Lưu địa chỉ'} variant="secondary" onPress={saveBaseUrl} />
      </Card>

      <Button label="Đăng xuất" variant="danger" onPress={signOut} />
    </Screen>
  );
}

const s = StyleSheet.create({
  between: { justifyContent: 'space-between' },
  status: { ...typography.subheading, color: colors.text },
  queueItem: { paddingVertical: spacing.sm, gap: 2 },
});

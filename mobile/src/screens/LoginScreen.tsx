import React, { useState } from 'react';
import { Image, KeyboardAvoidingView, Platform, ScrollView, StyleSheet, Text, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { ApiError } from '../api/client';
import { useAuth } from '../state/AuthContext';
import { Body, Button, Caption, Field, Input, Title } from '../components/ui';
import { colors, radius, spacing, typography } from '../theme';

export default function LoginScreen({ onOpenSettings }: { onOpenSettings: () => void }) {
  const { signIn } = useAuth();
  const insets = useSafeAreaInsets();

  const [identifier, setIdentifier] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  const submit = async () => {
    if (!identifier.trim() || !password) {
      setError('Nhập đủ mã số / email và mật khẩu');
      return;
    }
    setBusy(true);
    setError(null);
    try {
      await signIn(identifier.trim(), password);
    } catch (err) {
      if (err instanceof ApiError) {
        setError(
          err.isNetworkError
            ? 'Không kết nối được máy chủ. Kiểm tra mạng hoặc địa chỉ API trong Cài đặt.'
            : err.message,
        );
      } else {
        setError('Đăng nhập thất bại, vui lòng thử lại');
      }
    } finally {
      setBusy(false);
    }
  };

  return (
    <KeyboardAvoidingView
      style={s.container}
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      keyboardVerticalOffset={insets.top}
    >
      <ScrollView contentContainerStyle={[s.content, { paddingTop: insets.top + spacing.xxl }]} keyboardShouldPersistTaps="handled">
        <View style={s.brand}>
          <View style={s.logo}>
            <Text style={s.logoText}>DK</Text>
          </View>
          <Title>Dy Khoa Campus</Title>
          <Caption>Điểm danh bằng mã QR và xin phép nghỉ học</Caption>
        </View>

        <View style={s.form}>
          <Field label="Mã số hoặc email">
            <Input
              value={identifier}
              onChangeText={setIdentifier}
              placeholder="2210001 hoặc an.pham@sv.dykhoa.edu.vn"
              autoCapitalize="none"
              autoCorrect={false}
              keyboardType="email-address"
              textContentType="username"
              returnKeyType="next"
            />
          </Field>

          <Field label="Mật khẩu">
            <Input
              value={password}
              onChangeText={setPassword}
              placeholder="••••••••"
              secureTextEntry
              textContentType="password"
              returnKeyType="go"
              onSubmitEditing={submit}
            />
          </Field>

          {error ? <Text style={s.error}>{error}</Text> : null}

          <Button label="Đăng nhập" onPress={submit} loading={busy} />
          <Button label="Cấu hình máy chủ" variant="ghost" onPress={onOpenSettings} />
        </View>

        <View style={s.hintBox}>
          <Body muted>Tài khoản dùng thử (dữ liệu mẫu)</Body>
          <Caption>Sinh viên: 2210001 · Giảng viên: GV001 · Quản trị: AD001</Caption>
          <Caption>Mật khẩu chung: campus123</Caption>
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
}

const s = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.background },
  content: { padding: spacing.xl, gap: spacing.xl, flexGrow: 1, justifyContent: 'center' },
  brand: { alignItems: 'center', gap: spacing.sm },
  logo: {
    width: 72,
    height: 72,
    borderRadius: radius.lg,
    backgroundColor: colors.primary,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: spacing.sm,
  },
  logoText: { color: colors.textInverse, fontSize: 28, fontWeight: '800', letterSpacing: 1 },
  form: { gap: spacing.lg },
  error: { ...typography.caption, color: colors.danger },
  hintBox: {
    backgroundColor: colors.primarySoft,
    borderRadius: radius.md,
    padding: spacing.lg,
    gap: spacing.xs,
  },
});

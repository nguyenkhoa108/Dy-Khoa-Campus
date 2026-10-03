import React from 'react';
import {
  ActivityIndicator,
  Pressable,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  View,
  type StyleProp,
  type RefreshControlProps,
  type TextInputProps,
  type ViewStyle,
} from 'react-native';
import { colors, radius, spacing, typography } from '../theme';

/* ------------------------------------------------------------------ Text -- */

export function Title({ children, style }: { children: React.ReactNode; style?: StyleProp<ViewStyle> }) {
  return <Text style={[s.title, style as never]}>{children}</Text>;
}

export function Heading({ children }: { children: React.ReactNode }) {
  return <Text style={s.heading}>{children}</Text>;
}

export function Body({ children, muted }: { children: React.ReactNode; muted?: boolean }) {
  return <Text style={[s.body, muted && s.muted]}>{children}</Text>;
}

export function Caption({ children, muted = true }: { children: React.ReactNode; muted?: boolean }) {
  return <Text style={[s.caption, muted && s.muted]}>{children}</Text>;
}

/* ----------------------------------------------------------------- Card --- */

export function Card({
  children,
  style,
  onPress,
}: {
  children: React.ReactNode;
  style?: StyleProp<ViewStyle>;
  onPress?: () => void;
}) {
  if (onPress) {
    return (
      <Pressable style={({ pressed }) => [s.card, pressed && s.cardPressed, style]} onPress={onPress}>
        {children}
      </Pressable>
    );
  }
  return <View style={[s.card, style]}>{children}</View>;
}

/* ---------------------------------------------------------------- Badge --- */

export function Badge({ label, fg, bg }: { label: string; fg: string; bg: string }) {
  return (
    <View style={[s.badge, { backgroundColor: bg }]}>
      <Text style={[s.badgeText, { color: fg }]}>{label}</Text>
    </View>
  );
}

/* --------------------------------------------------------------- Button --- */

type ButtonVariant = 'primary' | 'secondary' | 'danger' | 'ghost';

export function Button({
  label,
  onPress,
  variant = 'primary',
  disabled,
  loading,
  style,
}: {
  label: string;
  onPress: () => void;
  variant?: ButtonVariant;
  disabled?: boolean;
  loading?: boolean;
  style?: StyleProp<ViewStyle>;
}) {
  const inactive = disabled || loading;
  return (
    <Pressable
      accessibilityRole="button"
      accessibilityState={{ disabled: Boolean(inactive) }}
      onPress={onPress}
      disabled={inactive}
      style={({ pressed }) => [s.button, btnStyles[variant], inactive && s.buttonDisabled, pressed && s.buttonPressed, style]}
    >
      {loading ? (
        <ActivityIndicator color={variant === 'secondary' || variant === 'ghost' ? colors.primary : colors.textInverse} />
      ) : (
        <Text style={[s.buttonText, btnTextStyles[variant]]}>{label}</Text>
      )}
    </Pressable>
  );
}

/* ---------------------------------------------------------------- Field --- */

export function Field({
  label,
  hint,
  error,
  children,
}: {
  label: string;
  hint?: string;
  error?: string | null;
  children: React.ReactNode;
}) {
  return (
    <View style={s.field}>
      <Text style={s.fieldLabel}>{label}</Text>
      {children}
      {error ? <Text style={s.fieldError}>{error}</Text> : hint ? <Text style={s.fieldHint}>{hint}</Text> : null}
    </View>
  );
}

export function Input(props: TextInputProps) {
  return <TextInput placeholderTextColor={colors.textMuted} {...props} style={[s.input, props.style]} />;
}

/* ----------------------------------------------------------- Containers --- */

export function Screen({
  children,
  scroll = true,
  refreshControl,
  contentStyle,
}: {
  children: React.ReactNode;
  scroll?: boolean;
  refreshControl?: React.ReactElement<RefreshControlProps>;
  contentStyle?: StyleProp<ViewStyle>;
}) {
  if (!scroll) return <View style={[s.screen, contentStyle]}>{children}</View>;
  return (
    <ScrollView
      style={s.screen}
      contentContainerStyle={[s.screenContent, contentStyle]}
      refreshControl={refreshControl}
      keyboardShouldPersistTaps="handled"
    >
      {children}
    </ScrollView>
  );
}

export function Row({ children, style }: { children: React.ReactNode; style?: StyleProp<ViewStyle> }) {
  return <View style={[s.row, style]}>{children}</View>;
}

export function Divider() {
  return <View style={s.divider} />;
}

/* -------------------------------------------------------------- States --- */

export function Loading({ label = 'Đang tải…' }: { label?: string }) {
  return (
    <View style={s.centered}>
      <ActivityIndicator color={colors.primary} size="large" />
      <Text style={[s.caption, s.muted, { marginTop: spacing.md }]}>{label}</Text>
    </View>
  );
}

export function EmptyState({ title, description }: { title: string; description?: string }) {
  return (
    <View style={s.empty}>
      <Text style={s.emptyTitle}>{title}</Text>
      {description ? <Text style={[s.caption, s.muted, { textAlign: 'center' }]}>{description}</Text> : null}
    </View>
  );
}

export function ErrorNotice({ message, onRetry }: { message: string; onRetry?: () => void }) {
  return (
    <View style={s.errorBox}>
      <Text style={s.errorText}>{message}</Text>
      {onRetry ? <Button label="Thử lại" variant="secondary" onPress={onRetry} style={{ marginTop: spacing.md }} /> : null}
    </View>
  );
}

/* --------------------------------------------------------------- Styles --- */

const s = StyleSheet.create({
  title: { ...typography.title, color: colors.text },
  heading: { ...typography.heading, color: colors.text },
  body: { ...typography.body, color: colors.text },
  caption: { ...typography.caption, color: colors.text },
  muted: { color: colors.textMuted },

  screen: { flex: 1, backgroundColor: colors.background },
  screenContent: { padding: spacing.lg, paddingBottom: spacing.xxl, gap: spacing.md },

  card: {
    backgroundColor: colors.surface,
    borderRadius: radius.lg,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: colors.border,
    gap: spacing.sm,
  },
  cardPressed: { opacity: 0.75 },

  badge: { paddingHorizontal: spacing.md, paddingVertical: spacing.xs, borderRadius: radius.pill, alignSelf: 'flex-start' },
  badgeText: { ...typography.tiny, letterSpacing: 0.3 },

  button: {
    minHeight: 50,
    borderRadius: radius.md,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: spacing.lg,
    flexDirection: 'row',
  },
  buttonPressed: { opacity: 0.85 },
  buttonDisabled: { opacity: 0.5 },
  buttonText: { ...typography.subheading },

  field: { gap: spacing.sm },
  fieldLabel: { ...typography.subheading, color: colors.text },
  fieldHint: { ...typography.caption, color: colors.textMuted },
  fieldError: { ...typography.caption, color: colors.danger },
  input: {
    minHeight: 50,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: radius.md,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
    backgroundColor: colors.surface,
    color: colors.text,
    ...typography.body,
  },

  row: { flexDirection: 'row', alignItems: 'center', gap: spacing.sm },
  divider: { height: 1, backgroundColor: colors.border, marginVertical: spacing.sm },

  centered: { flex: 1, alignItems: 'center', justifyContent: 'center', padding: spacing.xl },
  empty: { alignItems: 'center', justifyContent: 'center', padding: spacing.xl, gap: spacing.sm },
  emptyTitle: { ...typography.subheading, color: colors.text, textAlign: 'center' },

  errorBox: {
    backgroundColor: colors.dangerSoft,
    borderRadius: radius.md,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: colors.danger,
  },
  errorText: { ...typography.body, color: colors.danger },
});

const btnStyles = StyleSheet.create({
  primary: { backgroundColor: colors.primary },
  secondary: { backgroundColor: colors.primarySoft },
  danger: { backgroundColor: colors.danger },
  ghost: { backgroundColor: 'transparent', borderWidth: 1, borderColor: colors.border },
});

const btnTextStyles = StyleSheet.create({
  primary: { color: colors.textInverse },
  secondary: { color: colors.primary },
  danger: { color: colors.textInverse },
  ghost: { color: colors.text },
});

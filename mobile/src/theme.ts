/** Bảng màu và khoảng cách dùng chung — giữ giao diện nhất quán giữa các màn hình. */
export const colors = {
  primary: '#0F4C81',
  primaryDark: '#0A3A63',
  primarySoft: '#E7F0F8',
  accent: '#F2994A',

  success: '#1E9E6A',
  successSoft: '#E4F6EE',
  warning: '#E2A33B',
  warningSoft: '#FDF4E3',
  danger: '#D14343',
  dangerSoft: '#FBEAEA',
  info: '#3C7CC4',
  infoSoft: '#EAF1FA',

  text: '#16212E',
  textMuted: '#64748B',
  textInverse: '#FFFFFF',

  background: '#F4F6F9',
  surface: '#FFFFFF',
  border: '#E2E8F0',
  overlay: 'rgba(15, 23, 42, 0.72)',
} as const;

export const spacing = {
  xs: 4,
  sm: 8,
  md: 12,
  lg: 16,
  xl: 24,
  xxl: 32,
} as const;

export const radius = {
  sm: 8,
  md: 12,
  lg: 16,
  pill: 999,
} as const;

export const typography = {
  title: { fontSize: 24, fontWeight: '700' },
  heading: { fontSize: 18, fontWeight: '700' },
  subheading: { fontSize: 15, fontWeight: '600' },
  body: { fontSize: 15, fontWeight: '400' },
  caption: { fontSize: 13, fontWeight: '400' },
  tiny: { fontSize: 11, fontWeight: '600' },
} as const;

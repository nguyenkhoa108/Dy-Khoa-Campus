const WEEKDAYS = ['Chủ nhật', 'Thứ hai', 'Thứ ba', 'Thứ tư', 'Thứ năm', 'Thứ sáu', 'Thứ bảy'];

function pad(n: number): string {
  return n.toString().padStart(2, '0');
}

export function formatTime(iso: string): string {
  const d = new Date(iso);
  return `${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

export function formatDate(iso: string): string {
  const d = new Date(iso);
  return `${pad(d.getDate())}/${pad(d.getMonth() + 1)}/${d.getFullYear()}`;
}

export function formatDateTime(iso: string): string {
  return `${formatTime(iso)} ${formatDate(iso)}`;
}

export function formatWeekday(iso: string): string {
  return WEEKDAYS[new Date(iso).getDay()] ?? '';
}

export function formatRange(startIso: string, endIso: string): string {
  return `${formatTime(startIso)} – ${formatTime(endIso)}`;
}

/** YYYY-MM-DD theo giờ địa phương (tránh lệch ngày do toISOString dùng UTC). */
export function toDateKey(d: Date): string {
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

export function fromDateKey(key: string): Date {
  const [y, m, d] = key.split('-').map(Number);
  return new Date(y ?? 1970, (m ?? 1) - 1, d ?? 1);
}

export function formatDateKey(key: string): string {
  const [y, m, d] = key.split('-');
  return `${d}/${m}/${y}`;
}

export function isToday(iso: string): boolean {
  return toDateKey(new Date(iso)) === toDateKey(new Date());
}

/** "2 phút trước", "vừa xong"… cho nhật ký quét. */
export function relativeTime(iso: string): string {
  const diffSec = Math.floor((Date.now() - new Date(iso).getTime()) / 1000);
  if (diffSec < 10) return 'vừa xong';
  if (diffSec < 60) return `${diffSec} giây trước`;
  const min = Math.floor(diffSec / 60);
  if (min < 60) return `${min} phút trước`;
  const hours = Math.floor(min / 60);
  if (hours < 24) return `${hours} giờ trước`;
  return formatDate(iso);
}

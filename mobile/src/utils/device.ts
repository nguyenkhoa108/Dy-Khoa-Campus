import AsyncStorage from '@react-native-async-storage/async-storage';
import { Platform } from 'react-native';

const KEY = 'dkc.deviceId';
let cached: string | null = null;

function randomId(): string {
  // Đủ dùng để nhận diện thiết bị trong nhật ký điểm danh; không dùng cho bảo mật.
  const rand = () => Math.random().toString(36).slice(2, 10);
  return `${Platform.OS}-${rand()}${rand()}`;
}

/** Mã thiết bị ổn định, gắn kèm mỗi lượt quét để đối soát khi có tranh chấp. */
export async function getDeviceId(): Promise<string> {
  if (cached) return cached;
  const stored = await AsyncStorage.getItem(KEY);
  if (stored) {
    cached = stored;
    return stored;
  }
  const created = randomId();
  await AsyncStorage.setItem(KEY, created);
  cached = created;
  return created;
}

/** UUID v4 cho mỗi lượt quét — khoá chống ghi trùng khi đồng bộ offline. */
export function newClientUuid(): string {
  const hex = '0123456789abcdef';
  let out = '';
  for (let i = 0; i < 36; i += 1) {
    if (i === 8 || i === 13 || i === 18 || i === 23) out += '-';
    else if (i === 14) out += '4';
    else if (i === 19) out += hex[(Math.floor(Math.random() * 16) & 0x3) | 0x8];
    else out += hex[Math.floor(Math.random() * 16)];
  }
  return out;
}

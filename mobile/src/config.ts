import Constants from 'expo-constants';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Platform } from 'react-native';

const STORAGE_KEY = 'dkc.apiBaseUrl';

function fallbackBaseUrl(): string {
  const configured = (Constants.expoConfig?.extra as { apiBaseUrl?: string } | undefined)?.apiBaseUrl;
  if (configured) {
    // Máy ảo Android không tới được "localhost" của máy chủ phát triển — 10.0.2.2 mới đúng.
    if (Platform.OS === 'android') return configured.replace('localhost', '10.0.2.2').replace('127.0.0.1', '10.0.2.2');
    return configured;
  }
  return 'http://localhost:4000/api/v1';
}

let cached: string | null = null;

/**
 * Địa chỉ API đang dùng.
 *
 * Mặc định lấy từ `extra.apiBaseUrl` trong app.json, nhưng người dùng có thể
 * đổi ngay trong màn hình Cài đặt — cần thiết khi chạy thử trên điện thoại
 * thật, lúc đó app phải trỏ tới IP LAN của máy chạy server.
 */
export async function getApiBaseUrl(): Promise<string> {
  if (cached) return cached;
  const stored = await AsyncStorage.getItem(STORAGE_KEY);
  cached = stored?.trim() || fallbackBaseUrl();
  return cached;
}

export async function setApiBaseUrl(url: string): Promise<void> {
  const trimmed = url.trim().replace(/\/+$/, '');
  cached = trimmed || fallbackBaseUrl();
  if (trimmed) await AsyncStorage.setItem(STORAGE_KEY, trimmed);
  else await AsyncStorage.removeItem(STORAGE_KEY);
}

export function getDefaultApiBaseUrl(): string {
  return fallbackBaseUrl();
}

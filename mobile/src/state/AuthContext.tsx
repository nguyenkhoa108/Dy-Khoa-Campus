import React, { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState } from 'react';
import * as SecureStore from 'expo-secure-store';
import { api } from '../api/endpoints';
import { ApiError, configureApiClient, type TokenBundle } from '../api/client';
import { getDeviceId } from '../utils/device';
import type { AuthResponse, ClassSummary, User } from '../api/types';

const ACCESS_KEY = 'dkc.accessToken';
const REFRESH_KEY = 'dkc.refreshToken';
const USER_KEY = 'dkc.user';

interface AuthState {
  status: 'loading' | 'signedOut' | 'signedIn';
  user: User | null;
  classes: ClassSummary[];
  signIn: (identifier: string, password: string) => Promise<void>;
  signOut: () => Promise<void>;
  refreshProfile: () => Promise<void>;
}

const AuthContext = createContext<AuthState | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [status, setStatus] = useState<AuthState['status']>('loading');
  const [user, setUser] = useState<User | null>(null);
  const [classes, setClasses] = useState<ClassSummary[]>([]);

  // Token giữ trong ref để client API đọc đồng bộ, không phụ thuộc vòng render.
  const tokens = useRef<TokenBundle | null>(null);

  const persistTokens = useCallback(async (res: AuthResponse) => {
    tokens.current = { accessToken: res.accessToken, refreshToken: res.refreshToken };
    await Promise.all([
      SecureStore.setItemAsync(ACCESS_KEY, res.accessToken),
      SecureStore.setItemAsync(REFRESH_KEY, res.refreshToken),
      SecureStore.setItemAsync(USER_KEY, JSON.stringify(res.user)),
    ]);
    setUser(res.user);
  }, []);

  const clearSession = useCallback(async () => {
    tokens.current = null;
    await Promise.all([
      SecureStore.deleteItemAsync(ACCESS_KEY),
      SecureStore.deleteItemAsync(REFRESH_KEY),
      SecureStore.deleteItemAsync(USER_KEY),
    ]);
    setUser(null);
    setClasses([]);
    setStatus('signedOut');
  }, []);

  // Nối kho token vào client API đúng một lần.
  useEffect(() => {
    configureApiClient({
      readTokens: () => tokens.current,
      writeTokens: persistTokens,
      onSessionExpired: clearSession,
    });
  }, [persistTokens, clearSession]);

  const refreshProfile = useCallback(async () => {
    const me = await api.me();
    setUser(me.user);
    setClasses(me.classes);
    await SecureStore.setItemAsync(USER_KEY, JSON.stringify(me.user));
  }, []);

  // Khôi phục phiên đã lưu khi mở app.
  useEffect(() => {
    let cancelled = false;

    (async () => {
      const [accessToken, refreshToken, cachedUser] = await Promise.all([
        SecureStore.getItemAsync(ACCESS_KEY),
        SecureStore.getItemAsync(REFRESH_KEY),
        SecureStore.getItemAsync(USER_KEY),
      ]);

      if (cancelled) return;
      if (!accessToken || !refreshToken) {
        setStatus('signedOut');
        return;
      }

      tokens.current = { accessToken, refreshToken };
      // Hiện ngay hồ sơ đã lưu để không phải chờ mạng.
      if (cachedUser) {
        try {
          setUser(JSON.parse(cachedUser) as User);
        } catch {
          /* bộ nhớ đệm hỏng thì bỏ qua, sẽ lấy lại từ máy chủ */
        }
      }
      setStatus('signedIn');

      try {
        await refreshProfile();
      } catch (err) {
        // Mất mạng thì vẫn cho dùng offline; chỉ đăng xuất khi máy chủ từ chối phiên.
        if (err instanceof ApiError && !err.isNetworkError && err.status === 401) await clearSession();
      }
    })();

    return () => {
      cancelled = true;
    };
  }, [refreshProfile, clearSession]);

  const signIn = useCallback(
    async (identifier: string, password: string) => {
      const deviceId = await getDeviceId();
      const res = await api.login(identifier, password, deviceId);
      await persistTokens(res);
      setStatus('signedIn');
      try {
        await refreshProfile();
      } catch {
        /* danh sách lớp sẽ được tải lại ở màn hình chính */
      }
    },
    [persistTokens, refreshProfile],
  );

  const signOut = useCallback(async () => {
    const refreshToken = tokens.current?.refreshToken;
    if (refreshToken) {
      try {
        await api.logout(refreshToken);
      } catch {
        /* thu hồi phía máy chủ thất bại cũng vẫn xoá phiên cục bộ */
      }
    }
    await clearSession();
  }, [clearSession]);

  const value = useMemo<AuthState>(
    () => ({ status, user, classes, signIn, signOut, refreshProfile }),
    [status, user, classes, signIn, signOut, refreshProfile],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth(): AuthState {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth phải nằm trong <AuthProvider>');
  return ctx;
}

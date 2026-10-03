import React, { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import NetInfo from '@react-native-community/netinfo';
import { api, type ScanPayload } from '../api/endpoints';
import { ApiError } from '../api/client';

const QUEUE_KEY = 'dkc.scanQueue';

export interface QueuedScan extends ScanPayload {
  /** Nhãn hiển thị trong danh sách chờ (mã sinh viên hoặc tên buổi học). */
  label: string;
  queuedAt: string;
  attempts: number;
  lastError?: string;
}

interface ScanQueueState {
  queue: QueuedScan[];
  isOnline: boolean;
  isSyncing: boolean;
  lastSyncAt: string | null;
  enqueue: (scan: QueuedScan) => Promise<void>;
  sync: () => Promise<{ accepted: number; rejected: number } | null>;
  clearFailed: () => Promise<void>;
}

const ScanQueueContext = createContext<ScanQueueState | null>(null);

/**
 * Hàng đợi quét offline.
 *
 * Giảng đường thường sóng yếu, nên mỗi lượt quét được ghi xuống máy trước.
 * Khi có mạng trở lại, toàn bộ hàng đợi được gửi theo lô; `clientUuid` bảo đảm
 * gửi lại nhiều lần cũng chỉ sinh một bản ghi điểm danh.
 */
export function ScanQueueProvider({ children }: { children: React.ReactNode }) {
  const [queue, setQueue] = useState<QueuedScan[]>([]);
  const [isOnline, setIsOnline] = useState(true);
  const [isSyncing, setIsSyncing] = useState(false);
  const [lastSyncAt, setLastSyncAt] = useState<string | null>(null);
  const syncing = useRef(false);

  const persist = useCallback(async (next: QueuedScan[]) => {
    setQueue(next);
    await AsyncStorage.setItem(QUEUE_KEY, JSON.stringify(next));
  }, []);

  useEffect(() => {
    AsyncStorage.getItem(QUEUE_KEY).then((raw) => {
      if (!raw) return;
      try {
        setQueue(JSON.parse(raw) as QueuedScan[]);
      } catch {
        AsyncStorage.removeItem(QUEUE_KEY);
      }
    });
  }, []);

  const sync = useCallback(async () => {
    if (syncing.current) return null;

    const pending = JSON.parse((await AsyncStorage.getItem(QUEUE_KEY)) ?? '[]') as QueuedScan[];
    if (pending.length === 0) return null;

    syncing.current = true;
    setIsSyncing(true);
    try {
      const res = await api.syncScans(
        pending.map(({ qr, sessionId, clientUuid, deviceId, scannedAt }) => ({
          qr,
          sessionId,
          clientUuid,
          deviceId,
          scannedAt,
        })),
      );

      const byUuid = new Map(res.results.map((r) => [r.clientUuid, r]));
      // Giữ lại những mục còn có thể thử lại; lỗi 4xx là vĩnh viễn nên bỏ đi.
      const remaining = pending.filter((item) => {
        const result = byUuid.get(item.clientUuid);
        if (!result) return true;
        return !result.ok && result.retryable === true;
      });

      await persist(
        remaining.map((item) => ({
          ...item,
          attempts: item.attempts + 1,
          lastError: byUuid.get(item.clientUuid)?.error?.message,
        })),
      );
      setLastSyncAt(new Date().toISOString());
      return { accepted: res.accepted, rejected: res.rejected };
    } catch (err) {
      // Vẫn mất mạng: giữ nguyên hàng đợi, chỉ ghi lại lý do.
      if (err instanceof ApiError && err.isNetworkError) return null;
      throw err;
    } finally {
      syncing.current = false;
      setIsSyncing(false);
    }
  }, [persist]);

  // Có mạng trở lại thì đẩy hàng đợi đi ngay.
  useEffect(() => {
    const unsubscribe = NetInfo.addEventListener((state) => {
      const online = Boolean(state.isConnected && state.isInternetReachable !== false);
      setIsOnline(online);
      if (online) sync().catch(() => {});
    });
    return unsubscribe;
  }, [sync]);

  const enqueue = useCallback(
    async (scan: QueuedScan) => {
      const current = JSON.parse((await AsyncStorage.getItem(QUEUE_KEY)) ?? '[]') as QueuedScan[];
      if (current.some((s) => s.clientUuid === scan.clientUuid)) return;
      await persist([...current, scan]);
    },
    [persist],
  );

  const clearFailed = useCallback(async () => {
    await persist([]);
  }, [persist]);

  const value = useMemo<ScanQueueState>(
    () => ({ queue, isOnline, isSyncing, lastSyncAt, enqueue, sync, clearFailed }),
    [queue, isOnline, isSyncing, lastSyncAt, enqueue, sync, clearFailed],
  );

  return <ScanQueueContext.Provider value={value}>{children}</ScanQueueContext.Provider>;
}

export function useScanQueue(): ScanQueueState {
  const ctx = useContext(ScanQueueContext);
  if (!ctx) throw new Error('useScanQueue phải nằm trong <ScanQueueProvider>');
  return ctx;
}

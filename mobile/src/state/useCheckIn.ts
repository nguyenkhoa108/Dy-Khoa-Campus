import { useCallback, useState } from 'react';
import * as Haptics from 'expo-haptics';
import { ApiError } from '../api/client';
import { api } from '../api/endpoints';
import { useScanQueue } from './ScanQueueContext';
import { getDeviceId, newClientUuid } from '../utils/device';
import type { AttendanceStatus } from '../api/types';

export type ScanOutcome =
  | {
      kind: 'success';
      studentName: string;
      studentCode: string;
      status: AttendanceStatus;
      duplicate: boolean;
    }
  | { kind: 'queued'; reason: string }
  | { kind: 'error'; code: string; message: string };

/**
 * Logic chung cho mọi màn hình quét.
 *
 * Mất mạng không làm hỏng buổi điểm danh: lượt quét được xếp vào hàng đợi
 * cục bộ và gửi lên khi có sóng trở lại. Mọi kết quả khác được trả về nguyên
 * mã lỗi để màn hình hiển thị đúng thông điệp.
 */
export function useCheckIn(sessionId?: string) {
  const { enqueue } = useScanQueue();
  const [outcome, setOutcome] = useState<ScanOutcome | null>(null);

  const submit = useCallback(
    async (qr: string, label = 'Lượt quét'): Promise<ScanOutcome> => {
      const clientUuid = newClientUuid();
      const deviceId = await getDeviceId();
      const scannedAt = new Date().toISOString();
      const payload = { qr, sessionId, clientUuid, deviceId, scannedAt };

      let result: ScanOutcome;
      try {
        const res = await api.checkIn(payload);
        result = {
          kind: 'success',
          studentName: res.student.fullName,
          studentCode: res.student.code,
          status: res.record.status,
          duplicate: res.duplicate,
        };
        Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success).catch(() => {});
      } catch (err) {
        if (err instanceof ApiError && err.isNetworkError) {
          await enqueue({ ...payload, label, queuedAt: scannedAt, attempts: 0 });
          result = { kind: 'queued', reason: 'Mất kết nối — đã lưu vào hàng đợi và sẽ tự gửi khi có mạng.' };
          Haptics.notificationAsync(Haptics.NotificationFeedbackType.Warning).catch(() => {});
        } else if (err instanceof ApiError) {
          result = { kind: 'error', code: err.code, message: err.message };
          Haptics.notificationAsync(Haptics.NotificationFeedbackType.Error).catch(() => {});
        } else {
          result = { kind: 'error', code: 'UNKNOWN', message: 'Không xử lý được mã QR này' };
          Haptics.notificationAsync(Haptics.NotificationFeedbackType.Error).catch(() => {});
        }
      }

      setOutcome(result);
      return result;
    },
    [enqueue, sessionId],
  );

  return { outcome, submit, clear: useCallback(() => setOutcome(null), []) };
}

import { apiRequest } from './client';
import type {
  AttendanceHistory,
  AttendanceRecord,
  AuthResponse,
  CheckInResponse,
  ClassSession,
  ClassSummary,
  LeaveRequest,
  LeaveStatus,
  LeaveType,
  QrToken,
  SessionAttendance,
  SyncResponse,
  User,
} from './types';

export interface ScanPayload {
  qr: string;
  sessionId?: string;
  clientUuid: string;
  deviceId?: string;
  scannedAt?: string;
}

export const api = {
  // --- Xác thực -------------------------------------------------------------
  login: (identifier: string, password: string, deviceId: string) =>
    apiRequest<AuthResponse>('/auth/login', {
      method: 'POST',
      anonymous: true,
      body: { identifier, password, deviceId },
    }),

  logout: (refreshToken: string) =>
    apiRequest<{ ok: boolean }>('/auth/logout', { method: 'POST', anonymous: true, body: { refreshToken } }),

  me: () => apiRequest<{ user: User; classes: ClassSummary[] }>('/auth/me'),

  changePassword: (currentPassword: string, newPassword: string) =>
    apiRequest<{ ok: boolean }>('/auth/change-password', { method: 'POST', body: { currentPassword, newPassword } }),

  // --- Lớp và buổi học ------------------------------------------------------
  classes: () => apiRequest<{ items: ClassSummary[] }>('/classes'),

  classSessions: (classId: string) => apiRequest<{ items: ClassSession[] }>(`/classes/${classId}/sessions`),

  openSessions: () => apiRequest<{ items: ClassSession[] }>('/sessions/open'),

  openSession: (sessionId: string) =>
    apiRequest<{ session: ClassSession }>(`/sessions/${sessionId}/open`, { method: 'POST' }),

  closeSession: (sessionId: string) =>
    apiRequest<{ session: ClassSession; markedAbsent: number }>(`/sessions/${sessionId}/close`, { method: 'POST' }),

  createSession: (input: {
    classId: string;
    title: string;
    room?: string;
    startsAt: string;
    endsAt: string;
    lateAfterMin?: number;
  }) => apiRequest<{ session: ClassSession }>('/sessions', { method: 'POST', body: input }),

  // --- Mã QR ---------------------------------------------------------------
  sessionQr: (sessionId: string) => apiRequest<QrToken>(`/sessions/${sessionId}/qr`),

  myQr: () => apiRequest<QrToken>('/me/qr'),

  // --- Điểm danh ------------------------------------------------------------
  checkIn: (payload: ScanPayload) => apiRequest<CheckInResponse>('/attendance/check-in', { method: 'POST', body: payload }),

  syncScans: (items: ScanPayload[]) => apiRequest<SyncResponse>('/attendance/sync', { method: 'POST', body: { items } }),

  sessionAttendance: (sessionId: string) => apiRequest<SessionAttendance>(`/sessions/${sessionId}/attendance`),

  markAttendance: (sessionId: string, studentId: string, status: AttendanceRecord['status'], note?: string) =>
    apiRequest<{ record: AttendanceRecord }>(`/sessions/${sessionId}/attendance`, {
      method: 'POST',
      body: { studentId, status, note },
    }),

  attendanceHistory: (params: { studentId?: string; classId?: string; limit?: number; offset?: number } = {}) =>
    apiRequest<AttendanceHistory>('/attendance/history', { query: params }),

  // --- Đơn xin phép ---------------------------------------------------------
  leaveRequests: (params: { status?: LeaveStatus; scope?: 'mine' | 'to-review'; classId?: string; limit?: number } = {}) =>
    apiRequest<{ items: LeaveRequest[]; paging: { limit: number; offset: number; total: number } }>('/leave-requests', {
      query: params,
    }),

  leaveRequest: (id: string) => apiRequest<{ leaveRequest: LeaveRequest }>(`/leave-requests/${id}`),

  pendingLeaveCount: () => apiRequest<{ pending: number }>('/leave-requests/pending-count'),

  createLeaveRequest: (input: {
    classId: string | null;
    type: LeaveType;
    startDate: string;
    endDate: string;
    reason: string;
  }) => apiRequest<{ leaveRequest: LeaveRequest }>('/leave-requests', { method: 'POST', body: input }),

  approveLeave: (id: string, note?: string) =>
    apiRequest<{ leaveRequest: LeaveRequest; excusedSessions: number }>(`/leave-requests/${id}/approve`, {
      method: 'POST',
      body: { note },
    }),

  rejectLeave: (id: string, note: string) =>
    apiRequest<{ leaveRequest: LeaveRequest }>(`/leave-requests/${id}/reject`, { method: 'POST', body: { note } }),

  cancelLeave: (id: string) =>
    apiRequest<{ leaveRequest: LeaveRequest }>(`/leave-requests/${id}/cancel`, { method: 'POST' }),
};

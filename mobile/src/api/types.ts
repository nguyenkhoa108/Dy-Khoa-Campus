export type Role = 'student' | 'lecturer' | 'admin';
export type AttendanceStatus = 'present' | 'late' | 'absent' | 'excused';
export type AttendanceMethod = 'qr_session' | 'qr_student' | 'manual' | 'leave';
export type LeaveType = 'sick' | 'personal' | 'family' | 'other';
export type LeaveStatus = 'pending' | 'approved' | 'rejected' | 'cancelled';

export interface User {
  id: string;
  code: string;
  email: string;
  fullName: string;
  role: Role;
  faculty: string | null;
  avatarUrl: string | null;
}

export interface AuthResponse {
  accessToken: string;
  refreshToken: string;
  tokenType: 'Bearer';
  expiresIn: number;
  refreshExpiresAt: string;
  user: User;
}

export interface ClassSummary {
  id: string;
  code: string;
  name: string;
  term: string;
  room: string | null;
  lecturerId?: string;
  lecturerName: string;
  studentCount?: number;
}

export interface ClassSession {
  id: string;
  classId: string;
  title: string;
  room: string | null;
  startsAt: string;
  endsAt: string;
  lateAfterMin: number;
  checkinState: 'open' | 'closed';
  openedAt: string | null;
  closedAt: string | null;
  classCode?: string;
  className?: string;
  myStatus?: AttendanceStatus | null;
}

export interface AttendanceRecord {
  id: string;
  sessionId: string;
  studentId: string;
  status: AttendanceStatus;
  method: AttendanceMethod;
  checkedInAt: string | null;
  recordedBy: string | null;
  note: string | null;
  clientUuid: string | null;
  updatedAt: string;
}

export interface QrToken {
  token: string;
  expiresAt: string;
  ttlSec: number;
  refreshAfterSec: number;
  studentCode?: string;
  fullName?: string;
}

export interface CheckInResponse {
  duplicate: boolean;
  record: AttendanceRecord;
  student: { id: string; code: string; fullName: string };
  sessionId: string;
}

export interface RosterEntry {
  studentId: string;
  studentCode: string;
  fullName: string;
  recordId: string | null;
  status: AttendanceStatus | null;
  method: AttendanceMethod | null;
  checkedInAt: string | null;
  note: string | null;
}

export interface SessionAttendance {
  session: ClassSession;
  summary: { total: number; present: number; late: number; excused: number; absent: number; pending: number } | null;
  items: RosterEntry[] | AttendanceRecord[];
}

export interface AttendanceHistoryItem extends AttendanceRecord {
  session: {
    id: string;
    title: string;
    startsAt: string;
    endsAt: string;
    room: string | null;
    classCode: string;
    className: string;
  };
}

export interface AttendanceHistory {
  studentId: string;
  summary: { present: number; late: number; absent: number; excused: number; total: number };
  items: AttendanceHistoryItem[];
  paging: { limit: number; offset: number; count: number };
}

export interface LeaveRequest {
  id: string;
  studentId: string;
  classId: string | null;
  type: LeaveType;
  startDate: string;
  endDate: string;
  reason: string;
  attachmentUrl: string | null;
  status: LeaveStatus;
  reviewerId: string | null;
  reviewNote: string | null;
  reviewedAt: string | null;
  createdAt: string;
  updatedAt: string;
  student: { id: string; code: string; fullName: string; avatarUrl: string | null };
  class: { id: string; code: string; name: string } | null;
  reviewerName: string | null;
}

export interface SyncResultItem {
  clientUuid: string;
  ok: boolean;
  duplicate?: boolean;
  record?: AttendanceRecord;
  student?: { id: string; code: string; fullName: string };
  retryable?: boolean;
  error?: { code: string; message: string };
}

export interface SyncResponse {
  accepted: number;
  rejected: number;
  results: SyncResultItem[];
}

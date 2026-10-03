export type Role = 'student' | 'lecturer' | 'admin';
export type AttendanceStatus = 'present' | 'late' | 'absent' | 'excused';
export type AttendanceMethod = 'qr_session' | 'qr_student' | 'manual' | 'leave';
export type LeaveType = 'sick' | 'personal' | 'family' | 'other';
export type LeaveStatus = 'pending' | 'approved' | 'rejected' | 'cancelled';
export type CheckinState = 'closed' | 'open';

export interface UserRow {
  id: string;
  code: string;
  email: string;
  password_hash: string;
  full_name: string;
  role: Role;
  faculty: string | null;
  avatar_url: string | null;
  is_active: number;
  created_at: string;
}

export interface SessionRow {
  id: string;
  class_id: string;
  title: string;
  room: string | null;
  starts_at: string;
  ends_at: string;
  late_after_min: number;
  checkin_state: CheckinState;
  opened_at: string | null;
  closed_at: string | null;
  created_at: string;
}

export interface AttendanceRow {
  id: string;
  session_id: string;
  student_id: string;
  status: AttendanceStatus;
  method: AttendanceMethod;
  checked_in_at: string | null;
  recorded_by: string | null;
  device_id: string | null;
  client_uuid: string | null;
  note: string | null;
  created_at: string;
  updated_at: string;
}

export interface LeaveRow {
  id: string;
  student_id: string;
  class_id: string | null;
  type: LeaveType;
  start_date: string;
  end_date: string;
  reason: string;
  attachment_url: string | null;
  status: LeaveStatus;
  reviewer_id: string | null;
  review_note: string | null;
  reviewed_at: string | null;
  created_at: string;
  updated_at: string;
}

export function publicUser(u: UserRow) {
  return {
    id: u.id,
    code: u.code,
    email: u.email,
    fullName: u.full_name,
    role: u.role,
    faculty: u.faculty,
    avatarUrl: u.avatar_url,
  };
}

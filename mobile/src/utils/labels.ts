import { colors } from '../theme';
import type { AttendanceStatus, LeaveStatus, LeaveType, Role } from '../api/types';

export const attendanceLabel: Record<AttendanceStatus, string> = {
  present: 'Có mặt',
  late: 'Đi muộn',
  absent: 'Vắng',
  excused: 'Nghỉ có phép',
};

export const attendanceColor: Record<AttendanceStatus, { fg: string; bg: string }> = {
  present: { fg: colors.success, bg: colors.successSoft },
  late: { fg: colors.warning, bg: colors.warningSoft },
  absent: { fg: colors.danger, bg: colors.dangerSoft },
  excused: { fg: colors.info, bg: colors.infoSoft },
};

export const leaveStatusLabel: Record<LeaveStatus, string> = {
  pending: 'Chờ duyệt',
  approved: 'Đã duyệt',
  rejected: 'Từ chối',
  cancelled: 'Đã rút',
};

export const leaveStatusColor: Record<LeaveStatus, { fg: string; bg: string }> = {
  pending: { fg: colors.warning, bg: colors.warningSoft },
  approved: { fg: colors.success, bg: colors.successSoft },
  rejected: { fg: colors.danger, bg: colors.dangerSoft },
  cancelled: { fg: colors.textMuted, bg: colors.border },
};

export const leaveTypeLabel: Record<LeaveType, string> = {
  sick: 'Nghỉ ốm',
  personal: 'Việc cá nhân',
  family: 'Việc gia đình',
  other: 'Lý do khác',
};

export const roleLabel: Record<Role, string> = {
  student: 'Sinh viên',
  lecturer: 'Giảng viên',
  admin: 'Quản trị',
};

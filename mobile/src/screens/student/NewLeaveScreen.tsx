import React, { useState } from 'react';
import { Alert, Platform, Pressable, StyleSheet, Text, View } from 'react-native';
import DateTimePicker from '@react-native-community/datetimepicker';
import { api } from '../../api/endpoints';
import { ApiError } from '../../api/client';
import { useAuth } from '../../state/AuthContext';
import { Body, Button, Caption, Card, Field, Input, Row, Screen } from '../../components/ui';
import { leaveTypeLabel } from '../../utils/labels';
import { formatDateKey, fromDateKey, toDateKey } from '../../utils/datetime';
import { colors, radius, spacing, typography } from '../../theme';
import type { LeaveType } from '../../api/types';

const TYPES: LeaveType[] = ['sick', 'personal', 'family', 'other'];

export default function NewLeaveScreen({ navigation }: { navigation: any }) {
  const { classes } = useAuth();

  const [classId, setClassId] = useState<string | null>(classes[0]?.id ?? null);
  const [type, setType] = useState<LeaveType>('sick');
  const [startDate, setStartDate] = useState(toDateKey(new Date()));
  const [endDate, setEndDate] = useState(toDateKey(new Date()));
  const [reason, setReason] = useState('');
  const [picking, setPicking] = useState<'start' | 'end' | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const submit = async () => {
    if (reason.trim().length < 5) {
      setError('Lý do cần ít nhất 5 ký tự để người duyệt hiểu hoàn cảnh của bạn.');
      return;
    }
    if (endDate < startDate) {
      setError('Ngày kết thúc phải sau hoặc bằng ngày bắt đầu.');
      return;
    }

    setBusy(true);
    setError(null);
    try {
      await api.createLeaveRequest({ classId, type, startDate, endDate, reason: reason.trim() });
      Alert.alert('Đã gửi đơn', 'Đơn của bạn đang chờ giảng viên duyệt.', [
        { text: 'Xong', onPress: () => navigation.goBack() },
      ]);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : 'Không gửi được đơn, vui lòng thử lại');
    } finally {
      setBusy(false);
    }
  };

  const onDateChange = (_: unknown, selected?: Date) => {
    const which = picking;
    if (Platform.OS !== 'ios') setPicking(null);
    if (!selected || !which) return;

    const key = toDateKey(selected);
    if (which === 'start') {
      setStartDate(key);
      // Kéo theo ngày kết thúc để không bao giờ rơi vào khoảng ngày không hợp lệ.
      if (endDate < key) setEndDate(key);
    } else {
      setEndDate(key);
    }
  };

  return (
    <Screen>
      <Card>
        <Field label="Lớp học phần" hint="Chọn 'Tất cả lớp' nếu bạn nghỉ toàn bộ các lớp (Phòng Đào tạo sẽ duyệt).">
          <View style={s.chips}>
            {classes.map((c) => (
              <Chip key={c.id} label={c.code} active={classId === c.id} onPress={() => setClassId(c.id)} />
            ))}
            <Chip label="Tất cả lớp" active={classId === null} onPress={() => setClassId(null)} />
          </View>
        </Field>
      </Card>

      <Card>
        <Field label="Lý do nghỉ">
          <View style={s.chips}>
            {TYPES.map((t) => (
              <Chip key={t} label={leaveTypeLabel[t]} active={type === t} onPress={() => setType(t)} />
            ))}
          </View>
        </Field>
      </Card>

      <Card>
        <Field label="Thời gian nghỉ">
          <Row style={s.dateRow}>
            <DateButton label="Từ ngày" value={startDate} onPress={() => setPicking('start')} />
            <DateButton label="Đến ngày" value={endDate} onPress={() => setPicking('end')} />
          </Row>
        </Field>
        {picking ? (
          <DateTimePicker
            value={fromDateKey(picking === 'start' ? startDate : endDate)}
            mode="date"
            display={Platform.OS === 'ios' ? 'inline' : 'default'}
            minimumDate={picking === 'end' ? fromDateKey(startDate) : undefined}
            onChange={onDateChange}
          />
        ) : null}
        {Platform.OS === 'ios' && picking ? (
          <Button label="Xong" variant="secondary" onPress={() => setPicking(null)} />
        ) : null}
      </Card>

      <Card>
        <Field label="Trình bày lý do" hint="Nêu rõ hoàn cảnh để giảng viên có cơ sở duyệt đơn.">
          <Input
            value={reason}
            onChangeText={setReason}
            placeholder="Ví dụ: Em bị sốt cao, có giấy khám của trạm y tế trường."
            multiline
            numberOfLines={4}
            style={s.textarea}
          />
        </Field>
      </Card>

      {error ? <Text style={s.error}>{error}</Text> : null}

      <Button label="Gửi đơn xin phép" onPress={submit} loading={busy} />
      <Caption>
        Đơn được duyệt sẽ tự động đánh dấu "nghỉ có phép" cho các buổi học trong khoảng ngày trên. Buổi nào bạn đã
        điểm danh có mặt thì vẫn giữ nguyên.
      </Caption>
    </Screen>
  );
}

function DateButton({ label, value, onPress }: { label: string; value: string; onPress: () => void }) {
  return (
    <Pressable style={s.dateButton} onPress={onPress} accessibilityRole="button">
      <Caption>{label}</Caption>
      <Body>{formatDateKey(value)}</Body>
    </Pressable>
  );
}

function Chip({ label, active, onPress }: { label: string; active: boolean; onPress: () => void }) {
  return (
    <Text accessibilityRole="button" onPress={onPress} style={[s.chip, active ? s.chipActive : undefined]}>
      {label}
    </Text>
  );
}

const s = StyleSheet.create({
  chips: { flexDirection: 'row', flexWrap: 'wrap', gap: spacing.sm },
  chip: {
    ...typography.caption,
    color: colors.text,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.sm,
    borderRadius: radius.pill,
    backgroundColor: colors.background,
    borderWidth: 1,
    borderColor: colors.border,
    overflow: 'hidden',
  },
  chipActive: { backgroundColor: colors.primary, color: colors.textInverse, borderColor: colors.primary },
  dateRow: { gap: spacing.md },
  dateButton: {
    flex: 1,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: radius.md,
    padding: spacing.md,
    gap: 2,
    backgroundColor: colors.background,
  },
  textarea: { minHeight: 110, textAlignVertical: 'top', paddingTop: spacing.md },
  error: { ...typography.caption, color: colors.danger },
});

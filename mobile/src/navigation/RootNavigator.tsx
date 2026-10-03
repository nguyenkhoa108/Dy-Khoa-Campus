import React, { useCallback, useEffect, useState } from 'react';
import { Text } from 'react-native';
import { NavigationContainer, type Theme } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

import { useAuth } from '../state/AuthContext';
import { api } from '../api/endpoints';
import { Loading } from '../components/ui';
import { colors } from '../theme';

import LoginScreen from '../screens/LoginScreen';
import SettingsScreen from '../screens/SettingsScreen';

import StudentHomeScreen from '../screens/student/StudentHomeScreen';
import StudentScanScreen from '../screens/student/ScanScreen';
import MyQrScreen from '../screens/student/MyQrScreen';
import AttendanceHistoryScreen from '../screens/student/AttendanceHistoryScreen';
import LeaveListScreen from '../screens/student/LeaveListScreen';
import NewLeaveScreen from '../screens/student/NewLeaveScreen';

import LecturerHomeScreen from '../screens/lecturer/LecturerHomeScreen';
import ClassSessionsScreen from '../screens/lecturer/ClassSessionsScreen';
import SessionDetailScreen from '../screens/lecturer/SessionDetailScreen';
import SessionQrScreen from '../screens/lecturer/SessionQrScreen';
import ScanStudentScreen from '../screens/lecturer/ScanStudentScreen';
import ApprovalsScreen from '../screens/lecturer/ApprovalsScreen';

const Tab = createBottomTabNavigator();
const Stack = createNativeStackNavigator();

const navTheme: Theme = {
  dark: false,
  colors: {
    primary: colors.primary,
    background: colors.background,
    card: colors.surface,
    text: colors.text,
    border: colors.border,
    notification: colors.danger,
  },
  fonts: {
    regular: { fontFamily: 'System', fontWeight: '400' },
    medium: { fontFamily: 'System', fontWeight: '500' },
    bold: { fontFamily: 'System', fontWeight: '700' },
    heavy: { fontFamily: 'System', fontWeight: '800' },
  },
};

/** Biểu tượng tab bằng emoji — tránh kéo thêm thư viện icon cho một app nhỏ. */
function tabIcon(glyph: string) {
  return ({ color }: { color: string }) => <Text style={{ fontSize: 20, color }}>{glyph}</Text>;
}

const screenOptions = {
  headerStyle: { backgroundColor: colors.surface },
  headerTintColor: colors.text,
  headerTitleStyle: { fontWeight: '700' as const },
  tabBarActiveTintColor: colors.primary,
  tabBarInactiveTintColor: colors.textMuted,
  tabBarStyle: { backgroundColor: colors.surface, borderTopColor: colors.border },
};

/* ------------------------------------------------------------- Sinh viên -- */

function StudentLeaveStack() {
  return (
    <Stack.Navigator screenOptions={screenOptions}>
      <Stack.Screen name="LeaveList" component={LeaveListScreen} options={{ title: 'Đơn xin phép' }} />
      <Stack.Screen name="NewLeave" component={NewLeaveScreen} options={{ title: 'Nộp đơn xin phép' }} />
    </Stack.Navigator>
  );
}

function StudentTabs() {
  return (
    <Tab.Navigator screenOptions={screenOptions}>
      <Tab.Screen name="Trang chủ" component={StudentHomeScreen} options={{ tabBarIcon: tabIcon('🏠') }} />
      <Tab.Screen
        name="Quét QR"
        component={StudentScanScreen}
        options={{ tabBarIcon: tabIcon('📷'), headerTitle: 'Quét mã điểm danh' }}
      />
      <Tab.Screen name="Mã của tôi" component={MyQrScreen} options={{ tabBarIcon: tabIcon('🪪') }} />
      <Tab.Screen name="Lịch sử" component={AttendanceHistoryScreen} options={{ tabBarIcon: tabIcon('📋') }} />
      <Tab.Screen
        name="Xin phép"
        component={StudentLeaveStack}
        options={{ tabBarIcon: tabIcon('📝'), headerShown: false }}
      />
      <Tab.Screen name="Cài đặt" component={SettingsScreen} options={{ tabBarIcon: tabIcon('⚙️') }} />
    </Tab.Navigator>
  );
}

/* ------------------------------------------------------------ Giảng viên -- */

function LecturerClassStack() {
  return (
    <Stack.Navigator screenOptions={screenOptions}>
      <Stack.Screen name="LecturerHome" component={LecturerHomeScreen} options={{ title: 'Giảng dạy' }} />
      <Stack.Screen
        name="ClassSessions"
        component={ClassSessionsScreen}
        options={({ route }: any) => ({ title: route.params?.code ?? 'Buổi học' })}
      />
      <Stack.Screen name="SessionDetail" component={SessionDetailScreen} options={{ title: 'Danh sách điểm danh' }} />
      <Stack.Screen name="SessionQr" component={SessionQrScreen} options={{ title: 'Mã QR điểm danh' }} />
      <Stack.Screen name="ScanStudent" component={ScanStudentScreen} options={{ title: 'Quét mã sinh viên' }} />
    </Stack.Navigator>
  );
}

function LecturerTabs() {
  const [pending, setPending] = useState(0);

  // Chấm đỏ số đơn chờ duyệt, làm tươi định kỳ để giảng viên không bỏ sót.
  useEffect(() => {
    let active = true;
    const poll = () =>
      api
        .pendingLeaveCount()
        .then((res) => {
          if (active) setPending(res.pending);
        })
        .catch(() => {});
    poll();
    const id = setInterval(poll, 30_000);
    return () => {
      active = false;
      clearInterval(id);
    };
  }, []);

  return (
    <Tab.Navigator screenOptions={screenOptions}>
      <Tab.Screen
        name="Lớp học"
        component={LecturerClassStack}
        options={{ tabBarIcon: tabIcon('🎓'), headerShown: false }}
      />
      <Tab.Screen
        name="Duyệt phép"
        component={ApprovalsScreen}
        options={{ tabBarIcon: tabIcon('📝'), tabBarBadge: pending > 0 ? pending : undefined }}
      />
      <Tab.Screen name="Cài đặt" component={SettingsScreen} options={{ tabBarIcon: tabIcon('⚙️') }} />
    </Tab.Navigator>
  );
}

/* ------------------------------------------------------------------ Root -- */

function ServerSettingsStack() {
  return (
    <Stack.Navigator screenOptions={screenOptions}>
      <Stack.Screen name="ServerSettings" component={SettingsScreen} options={{ title: 'Cấu hình máy chủ' }} />
    </Stack.Navigator>
  );
}

export function RootNavigator() {
  const { status, user } = useAuth();
  const [showServerSettings, setShowServerSettings] = useState(false);

  const openSettings = useCallback(() => setShowServerSettings(true), []);

  if (status === 'loading') return <Loading label="Đang khôi phục phiên đăng nhập…" />;

  return (
    <NavigationContainer theme={navTheme}>
      {status === 'signedOut' ? (
        showServerSettings ? (
          <ServerSettingsStack />
        ) : (
          <LoginScreen onOpenSettings={openSettings} />
        )
      ) : user?.role === 'student' ? (
        <StudentTabs />
      ) : (
        <LecturerTabs />
      )}
    </NavigationContainer>
  );
}

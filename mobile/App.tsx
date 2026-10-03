import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { AuthProvider } from './src/state/AuthContext';
import { ScanQueueProvider } from './src/state/ScanQueueContext';
import { RootNavigator } from './src/navigation/RootNavigator';

export default function App() {
  return (
    <SafeAreaProvider>
      <AuthProvider>
        <ScanQueueProvider>
          <StatusBar style="dark" />
          <RootNavigator />
        </ScanQueueProvider>
      </AuthProvider>
    </SafeAreaProvider>
  );
}

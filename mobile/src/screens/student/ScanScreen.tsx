import React, { useCallback, useState } from 'react';
import { StyleSheet, View } from 'react-native';
import { QrScanner } from '../../components/QrScanner';
import { ScanResultSheet } from '../../components/ScanResultSheet';
import { OfflineBanner } from '../../components/OfflineBanner';
import { useCheckIn } from '../../state/useCheckIn';
import { colors } from '../../theme';

/** Sinh viên quét mã QR giảng viên chiếu trên lớp. */
export default function StudentScanScreen() {
  const { outcome, submit, clear } = useCheckIn();
  const [paused, setPaused] = useState(false);

  const handleScan = useCallback(
    async (data: string) => {
      setPaused(true);
      await submit(data, 'Quét mã buổi học');
    },
    [submit],
  );

  const dismiss = useCallback(() => {
    clear();
    setPaused(false);
  }, [clear]);

  return (
    <View style={s.container}>
      <OfflineBanner />
      <QrScanner
        onScan={handleScan}
        paused={paused}
        hint="Hướng camera vào mã QR giảng viên đang chiếu trên lớp. Mã đổi liên tục nên hãy quét mã mới nhất."
      />
      <ScanResultSheet outcome={outcome} onDismiss={dismiss} />
    </View>
  );
}

const s = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.background },
});

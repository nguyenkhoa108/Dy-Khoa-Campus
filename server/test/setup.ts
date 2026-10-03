process.env.NODE_ENV = 'test';
process.env.JWT_SECRET ??= 'test-secret-test-secret-test-secret-123456';
process.env.QR_SECRET ??= 'test-qr-secret-test-qr-secret-123456789';
process.env.DATABASE_FILE ??= ':memory:';

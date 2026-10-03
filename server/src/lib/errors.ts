/** Lỗi nghiệp vụ có mã ổn định để client (app di động + web app) bắt theo `code`. */
export class ApiError extends Error {
  constructor(
    readonly status: number,
    readonly code: string,
    message: string,
    readonly details?: unknown,
  ) {
    super(message);
    this.name = 'ApiError';
  }

  static badRequest(code: string, message: string, details?: unknown) {
    return new ApiError(400, code, message, details);
  }
  static unauthorized(code: string, message: string) {
    return new ApiError(401, code, message);
  }
  static forbidden(code: string, message: string, details?: unknown) {
    return new ApiError(403, code, message, details);
  }
  static notFound(code: string, message: string, details?: unknown) {
    return new ApiError(404, code, message, details);
  }
  static conflict(code: string, message: string, details?: unknown) {
    return new ApiError(409, code, message, details);
  }
}

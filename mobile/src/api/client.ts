import { getApiBaseUrl } from '../config';
import type { AuthResponse } from './types';

/** Lỗi có mã từ máy chủ, để màn hình hiển thị thông điệp đúng ngữ cảnh. */
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

  /** Mất mạng / máy chủ không trả lời — app xếp vào hàng đợi offline thay vì báo hỏng. */
  get isNetworkError(): boolean {
    return this.status === 0;
  }
}

export interface TokenBundle {
  accessToken: string;
  refreshToken: string;
}

type TokenReader = () => TokenBundle | null;
type TokenWriter = (tokens: AuthResponse) => Promise<void>;
type LogoutHandler = () => Promise<void>;

let readTokens: TokenReader = () => null;
let writeTokens: TokenWriter = async () => {};
let onSessionExpired: LogoutHandler = async () => {};

/** AuthContext gắn kho token vào client khi khởi động. */
export function configureApiClient(opts: {
  readTokens: TokenReader;
  writeTokens: TokenWriter;
  onSessionExpired: LogoutHandler;
}): void {
  readTokens = opts.readTokens;
  writeTokens = opts.writeTokens;
  onSessionExpired = opts.onSessionExpired;
}

const TIMEOUT_MS = 15_000;

async function rawRequest(path: string, init: RequestInit, accessToken?: string): Promise<Response> {
  const base = await getApiBaseUrl();
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);

  try {
    return await fetch(`${base}${path}`, {
      ...init,
      signal: controller.signal,
      headers: {
        Accept: 'application/json',
        ...(init.body ? { 'Content-Type': 'application/json' } : {}),
        ...(accessToken ? { Authorization: `Bearer ${accessToken}` } : {}),
        ...init.headers,
      },
    });
  } catch (err) {
    const aborted = err instanceof Error && err.name === 'AbortError';
    throw new ApiError(
      0,
      aborted ? 'NETWORK_TIMEOUT' : 'NETWORK_UNAVAILABLE',
      aborted ? 'Máy chủ không phản hồi kịp' : 'Không kết nối được máy chủ',
    );
  } finally {
    clearTimeout(timer);
  }
}

async function parseBody(res: Response): Promise<any> {
  const text = await res.text();
  if (!text) return null;
  try {
    return JSON.parse(text);
  } catch {
    return { raw: text };
  }
}

async function toApiError(res: Response): Promise<ApiError> {
  const body = await parseBody(res);
  const err = body?.error;
  return new ApiError(
    res.status,
    err?.code ?? `HTTP_${res.status}`,
    err?.message ?? `Máy chủ trả về lỗi ${res.status}`,
    err?.details,
  );
}

// Nhiều màn hình có thể cùng gặp 401 một lúc; gom chung vào một lượt refresh.
let refreshInFlight: Promise<string> | null = null;

async function refreshAccessToken(): Promise<string> {
  if (refreshInFlight) return refreshInFlight;

  refreshInFlight = (async () => {
    const tokens = readTokens();
    if (!tokens?.refreshToken) throw new ApiError(401, 'AUTH_REQUIRED', 'Phiên đăng nhập đã kết thúc');

    const res = await rawRequest('/auth/refresh', {
      method: 'POST',
      body: JSON.stringify({ refreshToken: tokens.refreshToken }),
    });

    if (!res.ok) {
      await onSessionExpired();
      throw await toApiError(res);
    }

    const next = (await parseBody(res)) as AuthResponse;
    await writeTokens(next);
    return next.accessToken;
  })();

  try {
    return await refreshInFlight;
  } finally {
    refreshInFlight = null;
  }
}

export interface RequestOptions {
  method?: 'GET' | 'POST' | 'PATCH' | 'DELETE';
  body?: unknown;
  /** Bỏ qua Authorization (dùng cho đăng nhập). */
  anonymous?: boolean;
  query?: Record<string, string | number | undefined | null>;
}

/**
 * Gọi API kèm tự động làm mới access token.
 * Khi gặp 401 vì token hết hạn, client refresh một lần rồi thử lại đúng một lần.
 */
export async function apiRequest<T>(path: string, options: RequestOptions = {}): Promise<T> {
  const { method = 'GET', body, anonymous = false, query } = options;

  let url = path;
  if (query) {
    const params = new URLSearchParams();
    for (const [key, value] of Object.entries(query)) {
      if (value !== undefined && value !== null && value !== '') params.append(key, String(value));
    }
    const qs = params.toString();
    if (qs) url += `?${qs}`;
  }

  const init: RequestInit = { method, ...(body === undefined ? {} : { body: JSON.stringify(body) }) };
  const token = anonymous ? undefined : (readTokens()?.accessToken ?? undefined);

  let res = await rawRequest(url, init, token);

  if (res.status === 401 && !anonymous) {
    const parsed = await parseBody(res.clone());
    const code = parsed?.error?.code;
    if (code === 'TOKEN_EXPIRED' || code === 'TOKEN_INVALID' || code === 'AUTH_REQUIRED') {
      const fresh = await refreshAccessToken();
      res = await rawRequest(url, init, fresh);
    }
  }

  if (!res.ok) throw await toApiError(res);
  return (await parseBody(res)) as T;
}

export interface ClientData {
  userId: string,
  hostname: string,
}

export interface ServiceStats {
  createdAt?: string;
}

// User
export interface User {
  userId?: number,
  username: string,
  password: string,
}

// Response interfaces
export interface FileResponse {
  success?: boolean,
  error?: string | null,
}

export interface ExeFileResponse extends FileResponse {
  stats?: ServiceStats,
}

export interface MotdFileResponse extends FileResponse {
  message: string,
}

export interface ResetNFileResponse extends FileResponse {
  started?: number,
}

export interface PflFileResponse extends FileResponse {
  userId?: number,
}

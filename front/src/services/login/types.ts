export interface ClientData {
  userId: string,
  hostname: string,
}

export interface ServiceStats {
  createdAt?: string;
  startedAt?: number;
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

export interface UserResponse {
  userId?: number,
  errors?: { [field: string]: string | null },
  messageOfTheDay?: string,
}

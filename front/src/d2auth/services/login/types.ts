import { Role } from './roles';

export interface ServiceStats {
  createdAt?: string;
  startedAt?: number;
}

export interface AuthData {
  userId: string,
  hostname: string,
}

// User
export interface User {
  userId?: number,
  username: string,
  password?: string,
  messageOfTheDay?: string,
  role?: Role,
}

export interface ChangePassword {
  oldPassword: string,
  newPassword: string,
}

// Response interfaces
export interface BasicResponse {
  success?: boolean,
  error?: string | null,
}

export interface AuthResponse extends BasicResponse{
  user?: User,
  errors?: { [field: string]: string | null },
}

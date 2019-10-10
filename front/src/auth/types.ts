import { Role } from './roles';

export interface ServiceStats {
  createdAt?: string;
  startedAt?: number;
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

// Form data
export interface LoginData {
  username: string,
  password: string,
  rememberMe: boolean,
}

export interface RegistrationData {
  username: string,
  email: string,
  password: string,
  password2: string,
}

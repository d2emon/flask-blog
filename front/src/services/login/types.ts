import { Role } from './roles';

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

export interface UserData {
  userId: number,
  username: string,
  messageOfTheDay?: string,
  role: Role,
}

// Response interfaces
export interface FileResponse {
  success?: boolean,
  error?: string | null,
}

export interface UserResponse extends FileResponse{
  user?: UserData,
  errors?: { [field: string]: string | null },
}

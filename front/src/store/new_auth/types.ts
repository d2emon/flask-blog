import { User } from '@/services/login/types';

export interface NewAuthState {
  error?: string,
  createdAt?: string,
  startedAt?: string,
  username?: string,
  password?: string,
  tries: number,
  user?: User,
  motd?: string,
  isNew: boolean,
}

export interface NewAuthData {
  userId: string,
  hostname: string,
}

import { User } from '@/services/login/types';

export interface NewAuthState {
  error?: string,
  errors: { [field: string]: string | null },
  createdAt?: string,
  startedAt?: string,
  user?: User,
  motd?: string,
  isNew: boolean,
}

export interface NewAuthData {
  userId: string,
  hostname: string,
}

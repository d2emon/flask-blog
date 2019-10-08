import { User } from '@/services/login/types';
import { Role } from '@/services/login/roles';

export interface NewAuthState {
  error?: string,
  errors: { [field: string]: string | null },
  createdAt?: string,
  startedAt?: string,
  role: Role,
  user?: User,
  motd?: string,
  isNew: boolean,
}

export interface NewAuthData {
  userId: string,
  hostname: string,
}

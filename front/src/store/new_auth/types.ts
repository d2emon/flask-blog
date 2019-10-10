import { User } from '@/d2auth/services/login/types';
import { Role } from '@/d2auth/services/login/roles';

export interface NewAuthState {
  error?: string,
  errors: { [field: string]: string | null },
  createdAt?: string,
  startedAt?: string,
  role: Role,
  user?: User,
  viewUser?: User,
  motd?: string,
  isNew: boolean,
}

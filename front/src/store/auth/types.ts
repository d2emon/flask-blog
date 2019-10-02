import {
  User as UserInterface,
} from '@/types';

export default class User implements UserInterface {
  token?: string;

  constructor(token?: string | null) {
    this.token = token || undefined;
  }

  get isAuthorized(): boolean {
    return !!this.token;
  }
}

export interface AuthState {
  user: User,
}

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

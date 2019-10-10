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

  // error?: string,
  errors: { [field: string]: string | null },
  // user?: User,
  // viewUser?: User,
  // isNew: boolean,
}

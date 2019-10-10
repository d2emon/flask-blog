import {
  User as UserInterface,
} from '@/types';
import {
  User as AuthInterface,
} from './types';

export default class User implements UserInterface, AuthInterface {
  token?: string;

  username: string = '';

  constructor(token?: string | null) {
    this.token = token || undefined;
  }

  get isAuthorized(): boolean {
    return !!this.token;
  }
}

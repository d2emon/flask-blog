import {
  AxiosError,
  AxiosInstance,
  AxiosResponse,
} from 'axios';
import {
  AuthData,
  ServiceStats,
  User,
  ChangePassword,
  AuthResponse,
} from './types';

export default class AuthService {
  static defaultErrorMessage: string = 'Unknown error';

  api: AxiosInstance;

  constructor(api: AxiosInstance) {
    this.api = api;
  }

  private static onSuccess(response: AxiosResponse): any {
    const { data } = response;
    if (!data) {
      throw new Error(AuthService.defaultErrorMessage);
    }
    if (data.error) {
      throw new Error(data.error);
    }
    return data;
  }

  private static onError(e: AxiosError): void {
    const message = e.response && e.response.data && e.response.data.error;
    throw new Error(message || e.message);
  }

  /*
  static processResponse(response: AuthResponse, value?: any): any {
    if (!response.success) {
      throw new Error(response.error || AuthService.defaultErrorMessage);
    }
    return (value !== undefined) ? value : response;
  }
   */

  private static fetchRequest = (request: Promise<AxiosResponse>): Promise<any> => request
    .then(AuthService.onSuccess)
    .catch(AuthService.onError);

  check(params: AuthData): Promise<ServiceStats> {
    return AuthService.fetchRequest(
      this.api.get('/check', { params }),
    );
  }

  getUser(username: string): Promise<AuthResponse> {
    return AuthService.fetchRequest(
      this.api.get(`/new-user/${username}`),
    );
  }

  newUser(user: User): Promise<AuthResponse> {
    return AuthService.fetchRequest(
      this.api.post('/new-user/', user),
    );
  }

  updateUser(user: User): Promise<AuthResponse> {
    return AuthService.fetchRequest(
      this.api.put('/new-user/', user),
    );
  }

  newPassword(user: User, passwords: ChangePassword): Promise<AuthResponse> {
    return AuthService.fetchRequest(
      this.api.put(`/new-change-password/${user.username}`, passwords),
    );
  }

  editUser(user: User): Promise<AuthResponse> {
    return AuthService.fetchRequest(
      this.api.put(`/new-user/${user.username}`, user),
    );
  }

  deleteUser(user: User): Promise<AuthResponse> {
    return AuthService.fetchRequest(
      this.api.delete(`/new-user/${user.username}`),
    );
  }
}

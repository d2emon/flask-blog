import {
  AxiosBasicCredentials,
  AxiosError,
  AxiosInstance,
  AxiosResponse,
} from 'axios';
import {
  User,
  ChangePassword,
  AuthResponse,
  RegistrationData,
} from '../types';

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

  // TODO: Auto-check API token on each request
  private static fetchRequest = (request: Promise<AxiosResponse>): Promise<any> => request
    .then(AuthService.onSuccess)
    .catch(AuthService.onError);

  // Tokens
  getToken(credentials: AxiosBasicCredentials): Promise<string> {
    return this.api
      .post('/tokens', null, { auth: credentials })
      .then(({ data }: AxiosResponse) => data.token || Promise.reject(new Error('No token!')))
      .catch(AuthService.onError);
  }

  registerUser(payload: RegistrationData): Promise<any> {
    return this.api
      .post('/register', { ...payload, api: true })
      .then(({ data }: AxiosResponse) => data);
  }

  async logoutUser(token: string | null): Promise<void> {
    if (!token) return;
    await this.api.delete(
      '/tokens',
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      },
    );
  }

  // User
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

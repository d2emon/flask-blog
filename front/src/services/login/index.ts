import {
  AxiosError,
  AxiosResponse,
} from 'axios';
import api from '@/helpers/api';
import {
  ChangePassword,
  NewAuthData,
} from '@/store/new_auth/types';
import {
  User,
  ServiceStats,
  FileResponse,
  UserResponse,
} from './types';
import {
  logFile,
} from './services';

const checkResponse = (response: FileResponse, value?: any): Promise<any> => (
  response.success
    ? (response.success && (value || response))
    : Promise.reject(new Error(response.error || 'Unknown error')));

const apiError = (e: AxiosError): Promise<any> => (
  (e.response && e.response.data && e.response.data.error)
    ? Promise.reject(new Error(e.response.data.error))
    : Promise.reject(new Error(e.message))
);

const apiResponse = ({ data }: AxiosResponse): any => (
  (data && data.error)
    ? Promise.reject(new Error(data.error))
    : data
);

const apiRequest = (promise: Promise<AxiosResponse>): Promise<any> => promise
  .then(apiResponse)
  .catch(apiError);

export const blogService = {
  check: async (params: NewAuthData): Promise<ServiceStats> => apiRequest(
    api.get('/check', { params }),
  ),
  postUser: (user: User): Promise<UserResponse> => apiRequest(
    api.post('/new-user', user),
  ),
  getUser: (username: string): Promise<UserResponse> => apiRequest(
    api.get(`/new-user/${username}`),
  ),
  putUser: (user: User): Promise<UserResponse> => apiRequest(
    api.put('/new-user', user),
  ),
  putPassword: (user: User, passwords: ChangePassword): Promise<UserResponse> => apiRequest(
    api.put(`/new-change-password/${user.username}`, passwords),
  ),
};

export const logService = {
  /**
   * Add to system log
   * @param message {string}
   */
  postLog: (message: string): Promise<boolean> => logFile.postLog(message)
    .then(checkResponse),
};

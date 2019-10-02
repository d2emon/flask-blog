import {
  AxiosBasicCredentials,
  AxiosError,
} from 'axios';
import api, { auth } from '@/helpers/api';
import { RegistrationData } from '@/store/auth/types';

const postAuth = (url: string, payload: {}): Promise<any> => auth
  .post(url, { ...payload, api: true })
  .then(({ data }) => data);

const authError = (e: AxiosError): Promise<any> => (
  (e.response && e.response.data && e.response.data.error)
    ? Promise.reject(new Error(e.response.data.error))
    : Promise.reject(new Error(e.message))
);

export default {
  getToken: (credentials: AxiosBasicCredentials): Promise<string> => api
    .post('/tokens', null, { auth: credentials })
    .then(({ data }) => data.token || Promise.reject(new Error('No token!')))
    .catch(authError),
  registerUser: (payload: RegistrationData) => postAuth('/register', payload),
  logoutUser: (token: string | null): Promise<any> => (
    token
      ? Promise.resolve()
      : api.delete('/tokens', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
  ),
};

import { AxiosBasicCredentials } from 'axios';
import { RegistrationFormData } from '@/forms/types';
import api, { auth } from '@/helpers/api';
import { LoginRequest } from '@/types';

const postAuth = (url: string, payload: {}): Promise<any> => auth
  .post(url, { ...payload, api: true })
  .then(({ data }) => data);

export default {
  getToken: (credentials: AxiosBasicCredentials): Promise<string> => api
    .post('/tokens', null, { auth: credentials })
    .then(({ data }) => data)
    .then(({ token }) => token),
  authUser: (payload: LoginRequest) => postAuth('/login', payload),
  registerUser: (payload: RegistrationFormData) => postAuth('/register', payload),
  logoutUser: (token?: string) => api.delete('/tokens', {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  }),
};

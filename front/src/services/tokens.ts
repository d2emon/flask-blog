import { RegistrationFormData } from '@/forms/types';
import api, { auth } from '@/helpers/api';
import { LoginRequest } from '@/types';

export default {
  getToken: (): Promise<any> => api
    .post('/token')
    .then(({ data }) => data)
    .then(console.log),
  // .then(({ data }) => data),
  authUser: (payload: LoginRequest) => api.post('/login', payload)
    .then(({ data }) => data)
    .then(console.log),
  registerUser: (payload: RegistrationFormData) => auth
    .post('/register', { ...payload, api: true })
    .then(({ data }) => data),
};

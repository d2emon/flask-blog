import api from '@/helpers/api';
import {LoginRequest} from "@/types";

export default {
  getToken: (): Promise<any> => api
    .post('/token')
    .then(console.log),
  // .then(({ data }) => data),
  authUser: (payload: LoginRequest) => api.post('/login', payload)
    .then(console.log),
};

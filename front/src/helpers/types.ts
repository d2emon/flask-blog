import { AxiosRequestConfig } from 'axios';
import { NewAuthData } from '@/store/new_auth/types';

export interface Config {
  api: AxiosRequestConfig,
  auth: AxiosRequestConfig,
  newAuth: {
    userId: string,
    hostname: string,
  },
}

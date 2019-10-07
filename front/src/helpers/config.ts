import { Config } from './types';

const config: Config = {
  api: {
    baseURL: '//127.0.0.1:5000/api',
  },
  auth: {
    baseURL: '//127.0.0.1:5000/auth',
  },
  newAuth: {
    userId: 'userId',
    hostname: 'HOST_MACHINE',
  },
};

export default config;

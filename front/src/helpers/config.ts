import { Config } from './types';

const rootURL = (process.env.NODE_ENV === 'development')
  ? '//127.0.0.1:5000'
  : '';

const config: Config = {
  api: {
    baseURL: `${rootURL}/api`,
  },
  auth: {
    baseURL: `${rootURL}/auth`,
  },
};

export default config;

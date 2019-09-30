import { AxiosRequestConfig } from 'axios';

interface Config {
  api: AxiosRequestConfig,
}

const config: Config = {
  api: {
    baseURL: '//127.0.0.1:5000/api',
  },
};

export default config;

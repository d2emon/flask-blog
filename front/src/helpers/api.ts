import axios from 'axios';
import config from '@/helpers/config';

export const auth = axios.create(config.auth);

export default axios.create(config.api);

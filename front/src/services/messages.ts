import api from '@/helpers/api';

export default {
  getMessages: (): Promise<string[]> => api
    .get('/notifications')
    .then(({ data }) => data),
};

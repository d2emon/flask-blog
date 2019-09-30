import api from '@/helpers/api';
import {
  ArticleQuery,
  CategoryQuery,
  InstagramPost,
  Tag,
} from '@/types';

export default {
  getArticles: (
    start: number = 0,
    count: number = 10,
  ): Promise<ArticleQuery> => api
    .get('/articles', { params: { start, count } })
    .then(({ data }) => data),
  getCategories: (count?: number): Promise<CategoryQuery> => api
    .get('/categories', { params: { count } })
    .then(({ data }) => data),
  getInstagramPosts: (): Promise<InstagramPost[]> => api
    .get('/instagram')
    .then(({ data }) => data),
  getTags: (): Promise<Tag[]> => api
    .get('/tags')
    .then(({ data }) => data),
};

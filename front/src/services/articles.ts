import { Article } from '@/types';

const articles: Article[] = require('@/services/data/articles.json');

export default {
  getArticles: () => Promise.resolve(articles),
};

import {
  Article,
  ArticleQuery,
} from '@/types';

const articlesData: Article[] = require('@/services/data/articles.json');

export default {
  getArticles: (
    start: number = 0,
    count: number = 10,
  ): Promise<ArticleQuery> => Promise.resolve(articlesData.slice(start, start + count))
    .then(articles => ({
      articles,
      total: articlesData.length,
    })),
};

import {
  Article,
  ArticleQuery,
  CategoryQuery,
  Link,
} from '@/types';
import Articles from "@/components/Articles.vue";

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
  getCategories: (count?: number): Promise<CategoryQuery> => Promise.resolve(articlesData.reduce(
    (categories: Link[], article: Article) => {
      if (!article.category) return categories;

      const text: string = article.category;
      if (categories.find(category => category.text === text)) return categories;

      categories.push({
        text,
        to: `/category/${text}`,
      });

      return categories;
    },
    []
  ))
    .then((categories: Link[]): Link[] => categories.sort())
    .then((categories: Link[]): CategoryQuery => ({
      categories: count ? categories.slice(0, count) : categories,
      total: categories.length,
    })),
};

import {
  Article,
  ArticleQuery,
  Category,
  CategoryQuery,
  InstagramPost,
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
  getCategories: (count?: number): Promise<CategoryQuery> => Promise.resolve(articlesData.reduce(
    (categories: Category[], article: Article) => {
      if (!article.category) return categories;

      const text: string = article.category;
      const category = categories.find(category => category.text === text);
      if (category) {
        category.postsCount = category.postsCount ? category.postsCount + 1 : 1;
        return categories;
      }

      categories.push({
        categoryId: categories.length + 1,
        text,
        to: `/category/${text}`,
        postsCount: 1,
      });

      return categories;
    },
    []
  ))
    .then((categories: Category[]): Category[] => categories.sort())
    .then((categories: Category[]): CategoryQuery => ({
      categories: count ? categories.slice(0, count) : categories,
      total: categories.length,
    })),
  getInstagramPosts: (): Promise<InstagramPost[]> => Promise.resolve([
      { src: 'adventurealtitude.jpg' },
      { src: 'garden.jpg' },
      { src: 'pigduck.jpg' },
      { src: 'rain.jpg' },
      { src: 'spices.jpg' },
      { src: 'sunset.jpg' },
  ]),
};

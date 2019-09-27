import {
  Article,
  ArticleQuery,
  Category,
  CategoryQuery,
  InstagramPost,
  Tag,
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
  getTags: (): Promise<Tag[]> => Promise.resolve([
    { tagId: 1, name: 'Tag1' },
    { tagId: 2, name: 'Tag2' },
    { tagId: 3, name: 'Tag3' },
    { tagId: 4, name: 'Tag4' },
    { tagId: 5, name: 'Tag5' },
    { tagId: 6, name: 'Tag6' },
    { tagId: 7, name: 'Tag7' },
    { tagId: 8, name: 'Tag8' },
    { tagId: 9, name: 'Tag9' },
    { tagId: 10, name: 'Tag10' },
    { tagId: 11, name: 'Tag11' },
    { tagId: 12, name: 'Tag12' },
    { tagId: 13, name: 'Tag13' },
    { tagId: 14, name: 'Tag14' },
    { tagId: 15, name: 'Tag15' },
  ]),
};

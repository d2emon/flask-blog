export interface Article {
  title: string,
  author?: string,
  category?: string,
  hero: string,
  prominent?: boolean,
  layout?: number,
}

export interface Category {
  categoryId: number,
  text: string,
  icon?: string,
  to?: string,
  href?: string,
  postsCount: number,
}

export interface Link {
  text: string,
  icon?: string,
  to?: string,
  href?: string,
}

export type MenuLink = Category | Link;

export interface Contact {
  icon: string,
  title: string,
  subtitle?: string,
}

export interface ArticleQuery {
  articles: Article[],
  total: number,
}

export interface CategoryQuery {
  categories: Category[],
  total: number,
}

export interface InstagramPost {
  src: string,
  href?: string,
}

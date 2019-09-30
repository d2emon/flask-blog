export interface Article {
  articleId: string,
  title: string,
  author?: string,
  category?: string,
  img?: string,
  prominent?: boolean,
  createdAt: string,
  layout?: number,
  tags?: [],
  views: number,
  comments?: [],
  commentsCount?: number,
}

export interface ArticleQuery {
  articles: Article[],
  total: number,
}

export interface Category {
  categoryId: number,
  text: string,
  icon?: string,
  to?: string,
  href?: string,
  postsCount: number,
}

export interface CategoryQuery {
  categories: Category[],
  total: number,
}

export interface Comment {
  commentId: number,
  postId: number,
  author: string,
  brief: string,
  body: string,
}

export interface Contact {
  icon: string,
  title: string,
  subtitle?: string,
}

export interface InstagramPost {
  src: string,
  href?: string,
}

export interface Link {
  text: string,
  icon?: string,
  to?: string,
  href?: string,
}

export interface Tag {
  tagId: number,
  name: string,
  fontSize?: string,
  color?: string,
}

export type MenuLink = Category | Link;

export interface LoginRequest {
  username: string,
  password: string,
  remember_me?: boolean,
}

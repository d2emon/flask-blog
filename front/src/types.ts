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

interface BaseLink {
  to?: string,
  href?: string,
}

interface TextLink extends BaseLink {
  text: string,
  icon?: string,
}

interface IconLink extends BaseLink {
  icon: string,
  text?: string,
}

export type Link = TextLink | IconLink;

export interface Tag {
  tagId: number,
  name: string,
  fontSize?: string,
  color?: string,
}

export interface User {
  isAuthorized: boolean,
  token?: string,
}

export type MenuLink = Category | Link;

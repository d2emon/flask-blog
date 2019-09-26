export interface Article {
  title: string,
  author?: string,
  category?: string,
  hero: string,
  prominent?: boolean,
}

export interface Link {
  text?: string,
  icon?: string,
  to?: string,
  href?: string,
}

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
  categories: Link[],
  total: number,
}

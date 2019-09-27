import {
  Article,
  Category,
  Comment,
  InstagramPost,
  Link,
  Tag,
} from '@/types';

export interface RootState {
  articles?: Article[],
  articlesCount: number,
  categories?: Category[],
  comments?: Comment[],
  drawer: boolean,
  instagram?: InstagramPost[],
  items: Link[],
  itemsOnPage: number,
  messages?: string[],
  newest?: Article[],
  page: number,
  tags?: Tag[],
  user?: {},
}

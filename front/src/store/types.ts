import {
  Article,
  Category,
  InstagramPost,
  Link,
} from '@/types';

export interface RootState {
  articles?: Article[],
  articlesCount: number,
  categories?: Category[],
  drawer: boolean,
  instagram?: InstagramPost[],
  items: Link[],
  itemsOnPage: number,
  messages?: string[],
  newest?: Article[],
  page: number,
  user?: {},
}

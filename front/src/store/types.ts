import {
  Article, InstagramPost,
  Link,
} from '@/types';

export interface RootState {
  articles?: Article[],
  articlesCount: number,
  categories?: Link[],
  drawer: boolean,
  instagram?: InstagramPost[],
  items: Link[],
  itemsOnPage: number,
  layout: number[],
  messages?: string[],
  newest?: Article[],
  page: number,
  user?: {},
}

import {
  Article,
  Link,
} from '@/types';

export interface RootState {
  articles?: Article[],
  articlesCount: number,
  categories?: Link[],
  drawer: boolean,
  items: Link[],
  itemsOnPage: number,
  layout: number[],
  newest?: Article[],
  page: number,
}

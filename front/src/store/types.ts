import {
  Article,
  Link,
} from '@/types';

export interface RootState {
  articles?: Article[],
  drawer: boolean,
  items: Link[],
  layout: number[],
  page: number,
  itemsOnPage: 11,
}

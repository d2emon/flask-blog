import { GetterTree } from 'vuex';
import { RootState } from './types';
import {
  Link,
} from '@/types';

const rootGetters: GetterTree<RootState, any> = {
  links: (state): Link[] => state.items.concat(state.categories || []),
  pages: (state): number => state.articles
    ? Math.ceil(state.articlesCount / state.itemsOnPage)
    : 0,
  articleOffset: (state): number => (state.page - 1) * state.itemsOnPage,
};

export default rootGetters;
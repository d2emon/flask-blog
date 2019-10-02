import { GetterTree } from 'vuex';
import { RootState } from './types';
import {
  MenuLink,
} from '@/types';

const getters: GetterTree<RootState, any> = {
  articleOffset: (state): number => (state.page - 1) * state.itemsOnPage,
  links: (state): MenuLink[] => state.items.concat(state.categories || []),
  pages: (state): number => (
    state.articles
      ? Math.ceil(state.articlesCount / state.itemsOnPage)
      : 0
  ),
};

export default getters;

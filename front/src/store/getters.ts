import { GetterTree } from 'vuex';
import { RootState } from './types';
import {
  Link,
  Article,
} from '@/types';

const rootGetters: GetterTree<RootState, any> = {
  categories: (state): Link[] => {
    // TODO: Make async
    const categories: Link[] = [];

    if (!state.articles) return categories;

    for (const article of state.articles) {
      if (!article.category || categories.find(category => category.text === article.category)) continue;

      const text: string = article.category;

      categories.push({
        text,
        to: `/category/${text}`,
      });
    }
    return categories.sort().slice(0, 4);
  },
  links: (state, getters): Link[] => state.items.concat(getters.categories),
  pages: (state): number => state.articles
    ? Math.ceil(state.articlesCount / state.itemsOnPage)
    : 0,
  articleOffset: (state): number => (state.page - 1) * state.itemsOnPage,
};

export default rootGetters;

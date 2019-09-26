import { ActionTree } from 'vuex';
import { RootState } from './types';
import {
  ArticleQuery,
  CategoryQuery,
} from '@/types';
import articlesService from '@/services/articles';

const action: ActionTree<RootState, any> = {
  fetchCategories: ({ commit, getters, state }, count?: number) => articlesService
    .getCategories(count)
    .then((response: CategoryQuery) => commit('setCategories', response)),
  fetchNewest: ({ commit, state }, count: number = 5) => articlesService
    .getArticles(state.articlesCount - count, state.articlesCount)
    .then(({ articles }) => commit('setNewest', articles)),
  fetchPage: ({ commit, getters, state }, page: number = 1) => {
    commit('setPage', page);
    articlesService
      .getArticles(getters.articleOffset, state.itemsOnPage)
      .then((response: ArticleQuery) => commit('setArticles', response));
  },
};

export default action;

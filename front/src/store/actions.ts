import { ActionTree } from 'vuex';
import { RootState } from './types';
import articlesService from '@/services/articles';

const action: ActionTree<RootState, any> = {
  fetchPage: ({ commit, getters, state }, page: number = 1) => {
    commit('setPage', page);
    articlesService
      .getArticles(getters.articleOffset, state.itemsOnPage)
      .then(response => commit('setArticles', response));
  },
  fetchNewest: ({ commit, state }, count: number = 5) => articlesService
    .getArticles(state.articlesCount - count, state.articlesCount)
    .then(({ articles }) => commit('setNewest', articles)),
};

export default action;

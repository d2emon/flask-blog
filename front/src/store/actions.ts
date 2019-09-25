import { ActionTree } from 'vuex';
import { RootState } from './types';
import articlesService from '@/services/articles';

const action: ActionTree<RootState, any> = {
  fetchArticles: ({ commit }) => articlesService
    .getArticles()
    .then(response => commit('setArticles', response)),
};

export default action;

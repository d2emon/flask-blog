import Vue from 'vue';
import { MutationTree } from 'vuex';
import { RootState } from './types';
import {
  Article,
  ArticleQuery,
} from '@/types';

const mutations: MutationTree<RootState> = {
  setDrawer: (state, payload: boolean) => (state.drawer = payload),
  toggleDrawer: state => (state.drawer = !state.drawer),
  setArticles: (state, payload: ArticleQuery) => {
    const {
      articles,
      total,
    } = payload;
    Vue.set(state, 'articles', [...articles]);
    state.articlesCount = total;
  },
  setNewest: (state, payload: Article[]) => Vue.set(state, 'newest', payload),
  setPage: (state, payload: number) => (state.page = payload),
};

export default mutations;

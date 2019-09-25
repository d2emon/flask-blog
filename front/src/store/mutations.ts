import { MutationTree } from 'vuex';
import { RootState } from './types';
import { Article } from '@/types';

const mutations: MutationTree<RootState> = {
  setDrawer: (state, payload: boolean) => (state.drawer = payload),
  toggleDrawer: state => (state.drawer = !state.drawer),
  setArticles: (state, payload: Article[]) => (state.articles = payload),
};

export default mutations;

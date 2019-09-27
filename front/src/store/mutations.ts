import Vue from 'vue';
import { MutationTree } from 'vuex';
import { RootState } from './types';
import {
  Article,
  ArticleQuery,
  CategoryQuery,
  InstagramPost,
  Tag,
} from '@/types';

const mutations: MutationTree<RootState> = {
  setDrawer: (state, payload: boolean) => (state.drawer = payload),
  toggleDrawer: state => (state.drawer = !state.drawer),
  setArticles: (state, payload: ArticleQuery) => {
    const {
      articles,
      total,
    } = payload;
    const layouts = [2, 2, 1, 2, 2, 3, 3, 3, 3, 3, 3];
    Vue.set(state, 'articles', articles.map((article: Article, articleId: number) => ({
      ...article,
      layout: (articleId < layouts.length) ? layouts[articleId] : 3,
    })));
    state.articlesCount = total;
  },
  setCategories: (state, payload: CategoryQuery) => {
    const {
      categories,
      // total,
    } = payload;
    Vue.set(state, 'categories', [...categories]);
    // state.articlesCount = total;
  },
  setInstagram: (state, payload: InstagramPost[]) => Vue.set(state, 'instagram', payload.map(
    (post: InstagramPost) => ({
      ...post,
      src: `/img/instagram/${post.src}`,
    })
  )),
  setMessages: (state, payload: string[]) => Vue.set(state, 'messages', payload),
  setNewest: (state, payload: Article[]) => Vue.set(state, 'newest', payload),
  setPage: (state, payload: number) => (state.page = payload),
  setTags: (state, payload: Tag[]) => Vue.set(state, 'tags', payload),
};

export default mutations;

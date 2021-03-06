import { ActionTree } from 'vuex';
import articlesService from '@/services/articles';
import messagesService from '@/services/messages';
import {
  ArticleQuery,
  CategoryQuery,
  InstagramPost,
  Tag,
} from '@/types';
import { RootState } from './types';

const actions: ActionTree<RootState, any> = {
  fetchCategories: ({ commit, getters, state }, count?: number): Promise<void> => articlesService
    .getCategories(count)
    .then((response: CategoryQuery) => commit('setCategories', response)),
  fetchInstagram: ({ commit, getters, state }): Promise<void> => articlesService
    .getInstagramPosts()
    .then((response: InstagramPost[]) => commit('setInstagram', response)),
  fetchMessages: ({ commit }): Promise<void> => messagesService
    .getMessages()
    .then((messages: string[]) => commit('setMessages', messages)),
  fetchNewest: ({ commit, state }, count: number = 5, force: boolean = false) => (
    force || !state.newest
  ) && articlesService
    .getArticles(state.articlesCount - count, state.articlesCount)
    .then(({ articles }) => commit('setNewest', articles)),
  fetchPage: ({ commit, getters, state }, page: number = 1): Promise<void> => Promise
    .resolve(commit('setPage', page))
    .then(() => articlesService.getArticles(getters.articleOffset, state.itemsOnPage))
    .then((response: ArticleQuery) => commit('setArticles', response)),
  fetchTags: ({ commit, state }, force: boolean = false) => (
    force || !state.tags
  ) && articlesService
    .getTags()
    .then((tags: Tag[]) => commit('setTags', tags)),
};

export default actions;

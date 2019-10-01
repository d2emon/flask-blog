import { ActionTree } from 'vuex';
import { RegistrationFormData } from '@/forms/types';
import articlesService from '@/services/articles';
import messagesService from '@/services/messages';
import tokensService from '@/services/tokens';
import {
  ArticleQuery,
  CategoryQuery, InstagramPost, LoginRequest, Tag,
} from '@/types';
import { RootState } from './types';

const action: ActionTree<RootState, any> = {
  registerUser: ({ commit }, payload: RegistrationFormData) => tokensService
    .registerUser(payload)
    .then((data) => {
      const {
        messages,
      } = data;
      commit('setMessages', messages);
      console.log(data);
      return data;
    }),
  userLogin: (context, payload: LoginRequest) => tokensService
    .authUser(payload),
  fetchToken: () => tokensService
    .getToken(),
  fetchCategories: ({ commit, getters, state }, count?: number) => articlesService
    .getCategories(count)
    .then((response: CategoryQuery) => commit('setCategories', response)),
  fetchInstagram: ({ commit, getters, state }) => articlesService
    .getInstagramPosts()
    .then((response: InstagramPost[]) => commit('setInstagram', response)),
  fetchMessages: ({ commit }) => messagesService
    .getMessages()
    .then((messages: string[]) => commit('setMessages', messages)),
  fetchNewest: ({ commit, state }, count: number = 5, force: boolean = false) => (
    force || !state.newest
  ) && articlesService
    .getArticles(state.articlesCount - count, state.articlesCount)
    .then(({ articles }) => commit('setNewest', articles)),
  fetchPage: ({ commit, getters, state }, page: number = 1) => Promise
    .resolve(commit('setPage', page))
    .then(() => articlesService.getArticles(getters.articleOffset, state.itemsOnPage))
    .then((response: ArticleQuery) => commit('setArticles', response)),
  fetchTags: ({ commit, state }, force: boolean = false) => (
    force || !state.tags
  ) && articlesService
    .getTags()
    .then((tags: Tag[]) => commit('setTags', tags)),
};

export default action;

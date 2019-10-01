import { AxiosBasicCredentials } from 'axios';
import { ActionTree } from 'vuex';
import { RegistrationFormData } from '@/forms/types';
import articlesService from '@/services/articles';
import authService from '@/services/auth';
import messagesService from '@/services/messages';
import {
  ArticleQuery,
  CategoryQuery,
  InstagramPost,
  LoginRequest,
  Tag,
} from '@/types';
import { RootState } from './types';

const action: ActionTree<RootState, any> = {
  processAuthResponse: ({ commit }, payload: {messages: string}) => {
    const {
      messages,
    } = payload;
    commit('setMessages', messages);
    return payload;
  },

  registerUser: ({ dispatch }, payload: RegistrationFormData): Promise<void> => authService
    .registerUser(payload)
    .then(data => dispatch('processAuthResponse', data)),
  loginUser: ({ commit, dispatch }, payload: LoginRequest): Promise<void> => authService
    .authUser(payload)
    .then(data => dispatch('processAuthResponse', data))
    .then((data) => {
      const { token } = data;
      commit('setToken', token);
      return data;
    }),
  logoutUser: ({ commit, getters }): Promise<void> => authService
    .logoutUser(getters.token)
    .then(() => commit('removeToken')),
  fetchToken: ({ commit }, {
    auth,
    rememberMe,
  }): Promise<void> => authService
    .getToken(auth)
    .then((token: string) => {
      if (rememberMe) commit('setToken', token);
      commit('setUser', { token });
    })
    .catch((e: Error) => {
      console.error(e);
      commit('removeToken');
      commit('setMessages', e.message);
    }),
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

export default action;

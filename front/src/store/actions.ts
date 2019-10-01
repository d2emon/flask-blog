import { AxiosBasicCredentials } from 'axios';
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
  processAuthResponse: ({ commit }, payload: {messages: string}) => {
    const {
      messages,
    } = payload;
    commit('setMessages', messages);
    return payload;
  },

  registerUser: ({ dispatch }, payload: RegistrationFormData) => tokensService
    .registerUser(payload)
    .then(data => dispatch('processAuthResponse', data)),
  loginUser: ({ commit, dispatch }, payload: LoginRequest) => tokensService
    .authUser(payload)
    .then(data => dispatch('processAuthResponse', data))
    .then((data) => {
      const { token } = data;
      commit('setToken', token);
      commit('setUser', { token });
      return data;
    }),
  logoutUser: ({ commit, state }) => tokensService
    .logoutUser(state.token)
    .then(() => {
      commit('setToken');
      commit('setUser');
    }),
  fetchToken: ({ commit }, payload: AxiosBasicCredentials) => tokensService
    .getToken(payload)
    .then((token: string) => {
      commit('setToken', token);
      commit('setUser', token);
    }),
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

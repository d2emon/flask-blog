import Vue from 'vue';
import { MutationTree } from 'vuex';
import User, { AuthState } from './types';

const mutations: MutationTree<AuthState> = {
  setToken: (state, payload: string) => {
    localStorage.setItem('token', payload);
    Vue.set(state, 'user', new User(payload));
  },
  removeToken: (state) => {
    localStorage.removeItem('token');
    Vue.set(state, 'user', new User());
  },
  setUser: (state, payload?: User) => Vue.set(state, 'user', payload),
};

export default mutations;

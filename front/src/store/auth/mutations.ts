import Vue from 'vue';
import { MutationTree } from 'vuex';
import { AuthResponse } from '@/auth/types';
import User from '@/auth/user';
import { AuthState } from './types';

const mutations: MutationTree<AuthState> = {
  // Errors
  setError: (state, payload?: string) => Vue.set(state, 'errors', { '': payload }),
  // Token
  setToken: (state, payload: string) => {
    localStorage.setItem('token', payload);
    Vue.set(state, 'user', new User(payload));
  },
  removeToken: (state) => {
    localStorage.removeItem('token');
    Vue.set(state, 'user', new User());
  },
  // User
  setUser: (state, payload?: User) => Vue.set(state, 'user', payload),
  setUserResponse: (state, payload: AuthResponse) => {
    const { user } = payload;
    Vue.set(state, 'errors', payload.errors);
    if (user) Vue.set(state, 'user', user);
  },
  setViewUser: (state, payload: AuthResponse) => {
    Vue.set(state, 'errors', payload.errors);
    Vue.set(state, 'viewUser', payload.user);
  },
};

export default mutations;

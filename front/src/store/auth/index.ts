import { Module } from 'vuex';
import { RootState } from '@/store/types';
import User, { AuthState } from './types';
import getters from './getters';
import mutations from './mutations';
import actions from './actions';

const state: AuthState = {
  user: new User(localStorage.getItem('token')),
};

const namespaced: boolean = true;

const auth: Module<AuthState, RootState> = {
  namespaced,
  state,
  getters,
  mutations,
  actions,
};

export default auth;

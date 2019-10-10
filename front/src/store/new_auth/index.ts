import { Module } from 'vuex';
import * as roles from '@/d2auth/services/login/roles';
import { RootState } from '@/store/types';
import { NewAuthState } from './types';
// import getters from './getters';
import mutations from './mutations';
import actions from './actions';

const state: NewAuthState = {
  errors: {},
  isNew: false,
  role: roles.UNAUTHORIZED,
};

const namespaced: boolean = true;

const auth: Module<NewAuthState, RootState> = {
  namespaced,
  state,
  // getters,
  mutations,
  actions,
};

export default auth;

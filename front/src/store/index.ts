import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './types';
import getters from './getters';
import mutations from './mutations';
import actions from './actions';

Vue.use(Vuex);

const state: RootState = {
  drawer: false,
  items: [
    {
      text: 'Home',
      to: '/',
    },
    {
      text: 'About',
      to: '#about',
    },
  ],
};

const store: StoreOptions<RootState> = {
  state,
  getters,
  mutations,
  actions,
};

export default new Vuex.Store<RootState>(store);

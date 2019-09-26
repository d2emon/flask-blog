import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './types';
import getters from './getters';
import mutations from './mutations';
import actions from './actions';

Vue.use(Vuex);

const state: RootState = {
  articlesCount: 0,
  drawer: false,
  items: [
    {
      text: 'Home',
      to: '/',
    },
    {
      text: 'About',
      href: '#about',
    },
    {
      text: 'Hello',
      to: '/hello',
    },
  ],
  itemsOnPage: 11,
  page: 1,
};

const store: StoreOptions<RootState> = {
  state,
  getters,
  mutations,
  actions,
};

export default new Vuex.Store<RootState>(store);

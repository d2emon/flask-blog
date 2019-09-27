import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './types';
import getters from './getters';
import mutations from './mutations';
import actions from './actions';

Vue.use(Vuex);

const state: RootState = {
  articlesCount: 0,
  comments: [
    {
      commentId: 1,
      postId: 1,
      author: 'author',
      brief: '<h4>Brief</h4>',
      body: '<h4>Brief</h4>\n<div>Body</div>',
    },
    {
      commentId: 2,
      postId: 1,
      author: 'author',
      brief: '<h4>Brief</h4>',
      body: '<h4>Brief</h4>\n<div>Body</div>',
    },
    {
      commentId: 3,
      postId: 2,
      author: 'author',
      brief: '<h4>Brief</h4>',
      body: '<h4>Brief</h4>\n<div>Body</div>',
    },
  ],
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
    {
      text: 'About Page',
      to: '/about',
    },
    {
      text: 'RSS',
      to: '/rss_lastnews',
    },
    {
      text: 'Skip to content',
      href: '#content',
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

import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/Home.vue'),
    },
    // Auth
    {
      path: '/registration',
      name: 'registration',
      component: () => import('@/views/Registration.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/Login.vue'),
    },
    // Other
    {
      path: '/hello',
      name: 'hello',
      component: () => import('@/views/Hello.vue'),
    },
  ],
});

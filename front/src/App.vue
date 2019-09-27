<template>
  <v-app>
    <main-toolbar />

    <main-drawer />

    <main-messages />

    <main-view />

    <main-footer />
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import { mapActions } from 'vuex';

export default Vue.extend({
  components: {
    MainDrawer: () => import('@/components/main/Drawer.vue'),
    MainFooter: () => import('@/components/main/Footer.vue'),
    MainMessages: () => import('@/components/main/Messages.vue'),
    MainToolbar: () => import('@/components/main/Toolbar.vue'),
    MainView: () => import('@/components/main/View.vue'),
  },
  methods: {
    ...mapActions([
      'fetchPage',
      'fetchCategories',
    ]),
  },
  created() {
    this.fetchPage(1);
    this.fetchCategories(10);
  },
});
</script>

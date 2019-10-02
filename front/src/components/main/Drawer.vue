<template>
  <v-navigation-drawer
    v-model="drawerModel"
    app
    dark
    temporary
  >
    <v-list>
      <v-list-item
        v-for="(link, linkId) in links"
        :key="linkId"
        :to="link.to"
        :href="link.href"
        @click.stop="onClick"
      >
        <v-list-item-title
          v-text="link.text"
        ></v-list-item-title>
      </v-list-item>
      <v-list-item
        v-if="user.isAuthorized"
        to="/logout"
      >
        <v-list-item-title>
          Log Out
        </v-list-item-title>
      </v-list-item>
      <template v-else>
        <v-list-item
          to="/login"
        >
          <v-list-item-title>
            Log In
          </v-list-item-title>
        </v-list-item>
        <v-list-item
          to="/registration"
        >
          <v-list-item-title>
            Registration
          </v-list-item-title>
        </v-list-item>
      </template>
    </v-list>
  </v-navigation-drawer>
</template>

<script lang="ts">
import Vue from 'vue';
import {
  mapState,
  mapGetters,
  mapMutations, MutationMethod,
} from 'vuex';
import { Link } from '@/types';

export default Vue.extend({
  computed: {
    ...mapState('auth', ['user']),
    ...mapState({
      drawerState: 'drawer',
    }),
    ...mapGetters(['links']),
    drawerModel: {
      get() { return (this as any).drawerState; },
      set(value: boolean) { (this as any).setDrawer(value); },
    },
  },
  methods: {
    ...mapMutations(['setDrawer']),
    onClick(item: Link) {
      if (item.to === '/') {
        this.$vuetify.goTo(0);
        (this as any).setDrawer(false);
        return;
      }

      if (item.to || !item.href) return;

      this.$vuetify.goTo(item.href);
      (this as any).setDrawer(false);
    },
  },
})
</script>

<style scoped>

</style>

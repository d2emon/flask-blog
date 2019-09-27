<template>
  <v-app-bar
    flat
  >
    <v-app-bar-nav-icon
      class="hidden-md-and-up"
      @click="toggleDrawer"
    ></v-app-bar-nav-icon>
    <v-img
      :src="require('@/assets/logo.png')"
      class="mr-5"
      contain
      height="48"
      width="48"
      max-width="48"
      @click="$vuetify.goTo(0)"
    />
    <v-toolbar-title class="headline text-uppercase mx-5">
      <span>Blog</span>
    </v-toolbar-title>
    <v-btn
      v-for="(link, linkId) in links"
      :key="linkId"
      :to="link.to"
      class="ml-0 hidden-sm-and-down"
      text
      @click.stop="onClick(link)"
    >
      {{ link.text }}
    </v-btn>
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-btn
          class="ml-0 hidden-sm-and-down"
          text
          v-on="on"
        >
          Categories
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="category in categories"
          :key="`category-${category.categoryId}`"
          :to="category.to"
        >
          <v-list-item-title>{{ category.text }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <v-btn
      v-if="user"
      to="/logout"
      class="ml-0 hidden-sm-and-down"
      text
    >
      log out
    </v-btn>
    <v-btn
      v-else
      to="/login"
      class="ml-0 hidden-sm-and-down"
      text
    >
      log in
    </v-btn>
    <v-spacer></v-spacer>
    <v-text-field
      append-icon="mdi-magnify"
      flat
      hide-details
      solo-inverted
      style="max-width: 300px;"
    />
  </v-app-bar>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapGetters,
  mapMutations,
  mapState,
} from 'vuex';
import { Link } from '@/types';

@Component({
  computed: {
    ...mapState([
      'user',
      'categories',
    ]),
    ...mapGetters(['links']),
  },
  methods: {
    ...mapMutations(['toggleDrawer']),
  },
})
export default class MainToolbar extends Vue {
  onClick(item: Link) {
    if (item.to || !item.href) return;

    this.$vuetify.goTo(item.href);
  }
}
</script>

<style scoped>

</style>

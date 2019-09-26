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
    <v-spacer></v-spacer>
    <v-text-field
      append-icon="mdi-magnify"
      flat
      hide-details
      solo-inverted
      style="max-width: 300px;"
    />

    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle colapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Flask-Blog</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li>
              <a href="/">Home</a>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                Categories <span class="caret"></span>
              </a>
              <ul class="dropdown-menu">
                {% for c in g.categories %}
                <li>
                  <a href="/category/{ c.id }">{ c.category_name }</a>
                </li>
                {% endfor %}
              </ul>
            </li>
            <li>
              <a href="/about">About</a>
            </li>
            <li>
              <a href="/rss_lastnews">RSS</a>
            </li>
            {% if not g.user %}
            <li>
              <a href="{ url_for('login') }">log in</a>
            </li>
            {% else %}
            <li>
              <a href="{ url_for('logout') }">log out</a>
            </li>
            {% endif %}
          </ul>
        </div>
      </div>
    </nav>
  </v-app-bar>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapGetters,
  mapMutations,
} from 'vuex';
import { Link } from '@/types';

@Component({
  computed: {
    ...mapGetters(['links']),
  },
  methods: {
    ...mapMutations(['toggleDrawer']),
  },
})
export default class MainToolbar extends Vue {
  // name: 'MainToolbar',

  onClick(item: Link) {
    if (item.to || !item.href) return;

    this.$vuetify.goTo(item.href);
  }
}
</script>

<style scoped>

</style>

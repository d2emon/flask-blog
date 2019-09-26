<template>
  <header id="branding" role="banner">
    <div id="inner-header" class="clearfix">
      <hgroup id="site-heading">
        <h1 id="site-title">
          <a rel="home" title="Home" href="/">Flask-Blog</a>
        </h1>
        <h2 id="site-description">My Flask-based blog.</h2>
      </hgroup>
      <nav id="access" role="navigation">
        <h1 class="assistive-text section-heading">Main menu</h1>
        <div class="skip-link screen-reader-text">
          <a title="Skip to content" href="#content">Skip to content</a>
        </div>

        <slot />

        <!-- head -->
        <div class="menu">
          <div id="menu-icon">
            Menu
            <ul>
              <li
                class="current_page_item"
                id="{% if nav_current=='index' %}current{% endif %}"
              >
                <a class="home" href="/">Home</a>
              </li>
              <li
                v-for="category in categories"
                :key="`category-${category.categoryId}`"
                class="page_item page-item-2"
                id="{% if cat and cat.id==c.id%}current{% endif %}"
              >
                <a :to="category.to">{{ category.text }}</a>
              </li>
              <li class="page_item page-item-2" id="{% if nav_current=='about' %}current{% endif %}">
                <a href="/about">About</a>
              </li>
              <li class="page_item page-item-2" id="{% if nav_current=='rss' %}current{% endif %}">
                <a href="/rss_lastnews">RSS</a>
              </li>
            </ul>
          </div>

          <v-form id="searchform" action="/search" method="get">
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  md="8"
                >
                  <v-text-field
                    id="s"
                    name="s"
                    label="S???："
                  ></v-text-field>
                </v-col>
                <v-col
                  cols="12"
                  md="4"
                >
                  <v-btn id="searchsubmit">
                    Submit
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>

          <!-- form id="quick-search" method="get" action="/search/">
            <fieldset class="search">
              <label for="q">Search:</label>
              <input class="tbox" id="qsearch" type="text" name="q" value="Search..." title="TITLE" onfocus="clS(1);" onblur="clS(0);" />
              <button class="btn" title="Search">Search</button>
            </fieldset>
          </form -->
        </div>
      </nav>
    </div>
  </header>
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
export default class MainHeader extends Vue {
  onClick(item: Link) {
    if (item.to || !item.href) return;

    this.$vuetify.goTo(item.href);
  }
}
</script>

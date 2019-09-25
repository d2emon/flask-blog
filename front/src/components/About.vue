<template>
  <v-container
    id="about"
    tag="section"
  >
    <article-header>About Us</article-header>
    <slot />
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import { Contact } from '@/types';

@Component({
  components: {
    ArticleHeader: () => import('@/components/controls/ArticleHeader.vue'),
  },
})
export default class About extends Vue {}
</script>

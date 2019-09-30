<template>
  <v-card class="mb-2">
    <v-card-title>
      <article-header>{{ title }}</article-header>
    </v-card-title>
    <slot />
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

@Component({
  components: {
    ArticleHeader: () => import('@/components/controls/ArticleHeader.vue'),
  },
  props: {
    title: String,
  },
})
export default class BaseWidget extends Vue {}
</script>

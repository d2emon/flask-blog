<template>
  <v-container pa-0>
    <article-header>Tags</article-header>
    <v-chip
      v-for="(category, categoryId) in categories"
      :key="categoryId"
      label
      small
      color="secondary"
      text-color="white"
      style="margin: 4px"
    >
      {{ category.text }}
    </v-chip>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import { mapState } from 'vuex';

@Component({
  components: {
    ArticleHeader: () => import('@/components/controls/ArticleHeader.vue'),
  },
  computed: {
    ...mapState(['categories']),
  },
})
export default class Tags extends Vue {}
</script>

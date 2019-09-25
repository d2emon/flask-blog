<template>
  <v-container pa-0>
    <article-header>Newest Blog Posts</article-header>
    <v-layout
      v-for="(article, articleId) in articles.slice(11, 14)"
      :key="articleId"
      align-center
      mb-2
    >
      <v-flex
        xs12
        d-flex
      >
        <v-img
          height="36"
          max-width="36"
          :src="require(`@/assets/articles/${article.hero}`)"
          class="mr-3"
        />
        <div>
          <div class="subtitle-1">
            Article Title
          </div>
          <div class="Caption">
            Date
          </div>
        </div>
      </v-flex>
    </v-layout>
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
    ...mapState(['articles']),
  },
})
export default class NewestPosts extends Vue {}
</script>

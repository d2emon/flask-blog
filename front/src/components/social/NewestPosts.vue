<template>
  <v-container pa-0>
    <article-header>Newest Blog Posts</article-header>
    <template v-if="newest">
      <v-layout
        v-for="(article, articleId) in newest.slice(0, 3)"
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
            :src="`/img/articles/${article.img}`"
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
    </template>
    <v-layout v-else>
      <h3>No posts yet!</h3>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapState,
  mapActions,
} from 'vuex';

@Component({
  components: {
    ArticleHeader: () => import('@/components/controls/ArticleHeader.vue'),
  },
  computed: {
    ...mapState(['newest']),
  },
  methods: {
    ...mapActions(['fetchNewest']),
  }
})
export default class NewestPosts extends Vue {
  mounted() {
      (this as any).fetchNewest(3, true);
  }
}
</script>

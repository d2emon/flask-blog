<template>
  <v-container
    grid-list-xl
  >
    <v-layout wrap>
      <v-flex xs12>
        <slot />
      </v-flex>

      <feed-card
        v-for="(article, articleId) in paginated"
        :key="article.title"
        :size="layout[articleId]"
        :value="article"
      ></feed-card>
    </v-layout>

    <v-layout align-center>
      <v-flex xs3>
        <social-button
          v-if="page !== 1"
          class="ml-0"
          title="Previous page"
          square
          @click="page--"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </social-button>
      </v-flex>

      <v-flex
        xs6
        text-center
        subtitle-1
      >
        PAGE {{ page }} OF {{ pages }}
      </v-flex>

      <v-flex
        xs3
        text-right
      >
        <social-button
          v-if="pages > 1 && page < pages"
          class="ml-0"
          title="Next page"
          square
          @click="page++"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </social-button>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { mapState } from 'vuex';

export default Vue.extend({
  components: {
    SocialButton: () => import('@/components/controls/SocialButton.vue'),
    FeedCard: () => import('@/components/FeedCard.vue'),
  },
  data: () => ({
    layout: [2, 2, 1, 2, 2, 3, 3, 3, 3, 3, 3],
    page: 1,
  }),
  computed: {
    ...mapState(['articles']),
    pages() {
      return Math.ceil((this as any).articles.length / 11);
    },
    paginated() {
      const start = (this.page - 1) * 11;
      const stop = this.page * 11;

      return (this as any).articles.slice(start, stop);
    },
  },
  watch: {
    page() {
      window.scrollTo(0, 0);
    },
  },
})
</script>

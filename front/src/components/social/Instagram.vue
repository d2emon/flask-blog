<template>
  <v-container
    pa-0
    grid-list-md
  >
    <article-header>On Instagram</article-header>
    <v-layout
      v-if="instagram"
      wrap
    >
      <v-flex
        v-for="(post, postId) in instagram"
        :key="postId"
        xs4
      >
        <article-card
          tag="a"
          :href="post.href"
          height="88"
          color="grey lighten-2"
        >
          <v-img
            v-if="post.src"
            height="100%"
            :src="post.src"
          />
        </article-card>
      </v-flex>
    </v-layout>
    <v-layout v-else>
      <h3>No instagram yet!</h3>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {mapActions, mapState} from 'vuex';

@Component({
  components: {
    ArticleCard: () => import('@/components/controls/ArticleCard.vue'),
    ArticleHeader: () => import('@/components/controls/ArticleHeader.vue'),
  },
  computed: {
    ...mapState(['instagram']),
  },
  methods: {
    ...mapActions(['fetchInstagram']),
  }
})
export default class Instagram extends Vue {
  created() {
    (this as any).fetchInstagram();
  }
}
</script>

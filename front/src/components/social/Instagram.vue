<template>
  <v-container
    pa-0
    grid-list-md
  >
    <article-header>On Instagram</article-header>
    <v-layout wrap>
      <v-flex
        v-for="(post, postId) in posts"
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
            :src="require(`@/assets/instagram/${post.src}`)"
          />
        </article-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

@Component({
  components: {
    ArticleCard: () => import('@/components/controls/ArticleCard.vue'),
    ArticleHeader: () => import('@/components/controls/ArticleHeader.vue'),
  },
  data: () => ({
    posts: [
      {src: 'adventurealtitude.jpg'},
      {src: 'garden.jpg'},
      {src: 'pigduck.jpg'},
      {src: 'rain.jpg'},
      {src: 'spices.jpg'},
      {src: 'sunset.jpg'},
    ],
  }),
})
export default class Instagram extends Vue {}
</script>

<template>
  <article-card
    dark
  >
    <v-img
      class="grey lighten-2"
      height="400px"
      width="100%"
      :src="image"
    >
      <v-layout
        fill-height
        align-center
        pa-3
      >
        <v-flex
          xs12
          md7
          offset-md5
        >
          <h1 class="display-3 font-weight-light">
            {{ title }}
          </h1>
          <div class="subtitle-1 text-uppercase pl-2 mb-4">
            {{ subtitle }}
          </div>
          <v-btn
            color="primary"
            depressed
            rounded
          >
            Subscribe
          </v-btn>
        </v-flex>
      </v-layout>
    </v-img>
  </article-card>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

@Component({
  components: {
    ArticleCard: () => import('@/components/controls/ArticleCard.vue'),
  },
  props: {
    image: String,
    title: String,
    subtitle: String,
  },
})
export default class Banner extends Vue {}
</script>

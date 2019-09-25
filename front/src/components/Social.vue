<template>
  <v-container
    id="social"
    tag="section"
    grid-list-xl
  >
    <v-layout wrap>
      <v-flex
        xs12
        md4
      >
        <instagram />
      </v-flex>
      <v-flex
        xs12
        md4
      >
        <newest-posts />
      </v-flex>
      <v-flex
        xs12
        md4
      >
        <tags />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

@Component({
  components: {
    Instagram: () => import('@/components/social/Instagram.vue'),
    NewestPosts: () => import('@/components/social/NewestPosts.vue'),
    Tags: () => import('@/components/social/Tags.vue'),
  },
})
export default class About extends Vue {}
</script>

<template>
  <v-container>
    <aside>
      <errors />
    </aside>
    <aside>
      <links />
    </aside>
    <aside>
      <new-posts />
    </aside>
    <aside>
      <hot-posts />
    </aside>
    <aside>
      <tags />
    </aside>
    <aside>
      <categories />
    </aside>
    <aside>
      <comments />
    </aside>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

@Component({
  components: {
    Errors: () => import('@/components/widgets/Errors.vue'),
    Links: () => import('@/components/widgets/Links.vue'),
    NewPosts: () => import('@/components/widgets/NewPosts.vue'),
    HotPosts: () => import('@/components/widgets/HotPosts.vue'),
    Tags: () => import('@/components/widgets/Tags.vue'),
    Categories: () => import('@/components/widgets/Categories.vue'),
    Comments: () => import('@/components/widgets/Comments.vue'),
  },
})
export default class Sidebar extends Vue {}
</script>

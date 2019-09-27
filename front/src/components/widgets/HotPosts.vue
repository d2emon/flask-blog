<template>
  <base-widget
    title="Hot posts"
  >
    <v-list>
      <v-list-item
        v-for="post in hotArticles"
        :key="`hot-${post.postId}`"
        :title="post.title"
        :href="`/article/${post.postId}`"
      >
        <v-list-item-content>
          <v-list-item-title>
            {{post.title}}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </base-widget>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapState,
} from 'vuex';

@Component({
  components: {
    BaseWidget: () => import('@/components/widgets/BaseWidget.vue'),
  },
})
export default class HotPosts extends Vue {
  hotArticles = [
    {
      postId: 1,
      title: 'Title',
    },
  ];
}
</script>

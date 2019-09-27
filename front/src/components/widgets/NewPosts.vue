<template>
  <base-widget
    title="New posts"
  >
    <v-list>
      <v-list-item
        v-for="post in newPosts"
        :key="`new-post-${post.postId}`"
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
export default class NewPosts extends Vue {
  newPosts = [
    {
      postId: 1,
      title: 'Title',
    },
  ];
}
</script>

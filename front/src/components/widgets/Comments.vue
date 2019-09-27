<template>
  <base-widget
    title="Comments"
  >
    <v-list>
      <v-list-item
        three-line
        v-for="comment in comments"
        :key="`comment-${comment.commentId}`"
      >
        <v-list-item-content>
          <v-list-item-title
            :title="comment.postId"
            :to="`/article/${comment.postId}#comments`"
          >
            {{comment.authorName}}
          </v-list-item-title>
          <v-list-item-subtitle>
            {{ comment.brief }}&hellip;
          </v-list-item-subtitle>
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
export default class Comments extends Vue {
  comments = [
    {
      commentId: 1,
      postId: 1,
      authorName: 'author',
      brief: '(comment.content|safe)[:30]',
    },
  ];
}
</script>

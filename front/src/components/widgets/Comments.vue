<template>
  <base-widget
    title="Comments"
  >
    <v-list>
      <v-list-item
        three-line
        v-for="comment in comments"
        :key="`comment-${comment.commentId}`"
        :title="comment.postId"
        :to="`/article/${comment.postId}/comments`"
      >
        <v-list-item-content>
          <v-list-item-title>
            {{comment.author}}
          </v-list-item-title>
          <v-list-item-subtitle>
            <span v-html="comment.brief"></span>&hellip;
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
  computed: {
    ...mapState(['comments'])
  },
})
export default class Comments extends Vue {}
</script>

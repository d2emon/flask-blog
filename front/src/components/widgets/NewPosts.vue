<template>
  <base-widget
    title="New posts"
  >
    <v-list
      two-line
      v-if="newest"
    >
      <v-list-item
        v-for="article in newest.slice(0, 10)"
        :key="`new-post-${article.articleId}`"
        :title="article.title"
        :to="`/article/${article.articleId}`"
      >
        <v-list-item-avatar>
          <v-img
            height="36"
            max-width="36"
            :src="`/img/articles/${article.img}`"
            class="mr-3"
          />
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title
            class="subtitle-1"
          >
            {{ article.title }}
          </v-list-item-title>
          <v-list-item-title
            class="caption"
          >
            {{ article.createdAt }}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-layout v-else>
      <h3>No posts yet!</h3>
    </v-layout>
  </base-widget>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapState,
  mapActions,
} from 'vuex';

@Component({
  components: {
    BaseWidget: () => import('@/components/widgets/BaseWidget.vue'),
  },
  computed: {
    ...mapState(['newest']),
  },
  methods: {
    ...mapActions(['fetchNewest']),
  },
})
export default class NewPosts extends Vue {
  mounted() {
    (this as any).fetchNewest();
  }
}
</script>

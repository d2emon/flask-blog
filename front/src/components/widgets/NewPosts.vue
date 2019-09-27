<template>
  <base-widget
    title="New posts"
  >
    <v-list>
      <v-list-item
        v-for="article in newest"
        :key="`new-post-${article.articleId}`"
        :title="article.title"
        :to="`/article/${article.articleId}`"
      >
        <v-list-item-content>
          <v-list-item-title>
            {{article.title}}
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

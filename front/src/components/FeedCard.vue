<template>
  <v-flex
    xs12
    :class="classes"
  >
    <article-card
      :height="value.prominent ? 450 : 350"
      color="grey lighten-1"
      dark
      href="#!"
    >
      <v-img
        :src="`/img/articles/${value.hero}`"
        height="100%"
        gradient="rgba(0, 0, 0, .42), rgba(0, 0, 0, .42)"
      >
        <v-layout
          v-if="!value.prominent"
          fill-height
          wrap
          text-right
          ma-0
        >
          <v-flex xs12>
            <v-chip
              class="mx-0 mb-2 text-uppercase"
              color="grey darken-3"
              text-color="white"
              label
              small
              @click.stop=""
            >
              {{ value.category }}
            </v-chip>
            <h3 class="title font-weight-bold mb-2">
              {{ value.title }}
            </h3>
            <div class="caption">
              {{ value.author }}<br />
              Date
            </div>
          </v-flex>
          <v-flex align-self-end>
            <v-chip
              class="text-uppercase ma-0"
              color="primary"
              label
              small
              @click.stop=""
            >
              Read More
            </v-chip>
          </v-flex>
        </v-layout>
      </v-img>
    </article-card>
  </v-flex>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import { Article } from '@/types';

@Component({
  components: {
    ArticleCard: () => import('@/components/controls/ArticleCard.vue'),
    // ArticleHeader: () => import('@/components/controls/ArticleHeader.vue'),
  },
  props: {
    size: {
      type: Number,
      default: 3,
    },
    value: Array(
      Object as () => Article,
    ),
  },
})
export default class FeedCard extends Vue {
  get classes() {
    return {
      md6: (this as any).size === 2,
      md4: (this as any).size === 3,
    }
  }
}
</script>

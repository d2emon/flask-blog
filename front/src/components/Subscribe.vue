<template>
  <v-container
    id="subscribe"
    tag="section"
  >
    <article-card
      color="rgb(203, 170, 92, 0.51)"
      class="pa-3"
    >
      <v-container
        grid-list-xl
        pa-0
      >
        <v-layout wrap>
          <v-flex
            xs12
            md5
          >
            <article-header class="mb-3">Subscribe</article-header>
            <slot />

            <v-layout
              wrap
              pa-2
            >
              <v-text-field
                solo
                hide-details
                style="max-width: 400px"
              />
              <v-btn
                :block="$vuetify.breakpoint.xsOnly"
                class="ma-0"
                color="secondary"
                style="height: 48px"
              >
                Subscribe
              </v-btn>
            </v-layout>
          </v-flex>
          <v-flex
            xs12
            md6
            offset-md1
          >
            <article-header>Contact</article-header>
            <v-list>
              <v-list-item
                v-for="(item, itemId) in contacts"
                :key="itemId"
              >
                <v-list-item-avatar
                  color="primary"
                >
                  <v-icon
                    class="elevation-4"
                    dark
                  >
                    {{ item.icon }}
                  </v-icon>
                </v-list-item-avatar>
                <v-list-item-title>
                  {{ item.title }}
                </v-list-item-title>
                <v-list-item-subtitle>
                  {{ item.subtitle }}
                </v-list-item-subtitle>
              </v-list-item>
            </v-list>
          </v-flex>
        </v-layout>
      </v-container>
    </article-card>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import { Contact } from '@/types';

@Component({
  components: {
    ArticleCard: () => import('@/components/controls/ArticleCard.vue'),
    ArticleHeader: () => import('@/components/controls/ArticleHeader.vue'),
  },
  props: {
    contacts: Array as () => Contact[],
  },
})
export default class Subscribe extends Vue {}
</script>

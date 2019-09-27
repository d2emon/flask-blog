<template>
  <base-widget
    title="Categories"
  >
    <v-list>
      <v-list-item
        v-for="category in categories"
        :key="`category-${category.categoryId}`"
        :title="`Category ${category.text}`"
        :to="`/category/${category.categoryId}`"
      >
        <v-list-item-content>
          <v-list-item-title>
            {{ category.text }}({{ category.postsCount || 0 }})
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
  computed: {
    ...mapState(['categories']),
  },
})
export default class Categories extends Vue {}
</script>

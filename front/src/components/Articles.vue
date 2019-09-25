<template>
  <section id="feed">
    <feed>
      <slot />
    </feed>
  </section>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

@Component({
  components: {
    Feed: () => import('@/components/Feed.vue'),
  },
})
export default class Articles extends Vue {}
</script>

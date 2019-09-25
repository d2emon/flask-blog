<template>
  <h2
    class="subtitle-1 text-uppercase font-weight-medium mb-3"
    v-bind="$attrs"
    v-on="$listeners"
  >
    <slot />
  </h2>

</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

@Component({
  inheritAttrs: false,
})
export default class ArticleCard extends Vue {}
</script>

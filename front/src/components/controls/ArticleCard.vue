<template>
  <v-card
    tile
    flat
    v-bind="$attrs"
    v-on="$listeners"
  >
    <slot />
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

@Component({
  inheritAttrs: false,
})
export default class ArticleCard extends Vue {}
</script>

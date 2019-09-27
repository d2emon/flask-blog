<template>
  <v-card class="mb-1">
    <v-card-title>
      <h2>{{ title }}</h2>
    </v-card-title>
    <slot />
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

@Component({
  props: {
    title: String,
  },
})
export default class BaseWidget extends Vue {}
</script>

<template>
  <v-btn
    fab
    small
    color="primary"
    :style="styles"
    v-bind="$attrs"
    v-on="$listeners"
  >
    <slot />
  </v-btn>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

@Component({
  inheritAttrs: false,
  props: {
    square: Boolean,
  },
})
export default class SocialButton extends Vue {
  get styles() {
    return { borderRadius: (this as any).square ? '2px' : undefined }
  }
}
</script>

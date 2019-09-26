<template>
  <v-container id="hello">
    <hello-world />
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import { Contact } from '@/types';

@Component({
  components: {
    HelloWorld: () => import('@/components/HelloWorld.vue'),
  },
})
export default class Hello extends Vue {}
</script>

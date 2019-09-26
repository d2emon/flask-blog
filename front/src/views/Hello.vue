<template>
  <v-container id="hello">
    <hello-world />
    <!-- iframe
      scrolling="no"
      frameborder="0"
      src="http://yibo.iyiyun.com/js/yibo404"
      width="735"
      height="700"
      style="display:block;margin:0 auto;"
    ></iframe -->
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

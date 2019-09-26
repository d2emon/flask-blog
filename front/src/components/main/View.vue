<template>
  <v-content id="content">
    <div
      id="main"
      class="col620 clearfix"
      role="main"
    >
      <router-view />
    </div>

    <sidebar />
  </v-content>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapGetters,
  mapMutations,
} from 'vuex';
import { Link } from '@/types';

@Component({
  components: {
    Sidebar: () => import('@/components/main/Sidebar.vue'),
  },
})
export default class MainView extends Vue {}
</script>

<template>
  <v-content id="content">
    <v-container>
      <v-row>
        <v-flex md2>
          <sidebar />
        </v-flex>
        <v-flex
          id="main"
          role="main"
          md10
        >
          <router-view />
        </v-flex>
      </v-row>
    </v-container>
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

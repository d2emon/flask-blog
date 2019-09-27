<template>
  <base-widget
    title="Errors"
  >
    <v-list>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title>
            Show <a target="_blank" href="/404">404 error</a> page！
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </base-widget>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

@Component({
  components: {
    BaseWidget: () => import('@/components/widgets/BaseWidget.vue'),
  },
})
export default class Errors extends Vue {}
</script>

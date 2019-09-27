<template>
  <base-widget
    title="Links"
  >
    <v-list>
      <v-list-item
        target="_blank"
        href="http://www.pythondoc.com/pythontutorial27/index.html"
      >
        <v-list-item-content>
          <v-list-item-title>
            Python 2.7 tutorial
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item
        target="_blank"
        href="http://www.pythondoc.com/pythontutorial3/index.html"
      >
        <v-list-item-content>
          <v-list-item-title>
            Python 3.3 tutorial
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item
        target="_blank"
        href="http://www.pythondoc.com/sphinx/index.html"
      >
        <v-list-item-content>
          <v-list-item-title>
            sphinx
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
export default class Links extends Vue {}
</script>

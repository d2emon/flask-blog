<template>
  <v-container>
    <v-alert
      v-for="message in messages"
      type="info"
      dismissible
    >
      {{ message }}
    </v-alert>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapActions,
  mapState,
} from 'vuex';

@Component({
  computed: {
    ...mapState(['messages']),
  },
  methods: {
    ...mapActions(['fetchMessages']),
  },
})
export default class Messages extends Vue {
  mounted() {
      (this as any).fetchMessages();
  }
}
</script>

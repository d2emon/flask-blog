<template>
  <v-card>
    <div>{{ motd }}</div>
    <v-btn
      @click="startMain"
    >
      Next
    </v-btn>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapActions,
  mapState,
} from 'vuex';

// !defaultUsername

@Component({
  computed: {
    ...mapState('newAuth', ['motd']),
  },
  methods: {
    ...mapActions('newAuth', [
      'fetchMotd',
      'startMain',
    ]),
  },
})
export default class Motd extends Vue {
  mounted() {
    (this as any).fetchMotd();
  }
}
</script>

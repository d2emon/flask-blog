<template>
  <v-card>
    <div>{{ error }}</div>
    <v-btn
      to="/new-login"
    >
      Hit Return to Continue...
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

@Component({
  computed: {
    ...mapState('newAuth', ['error']),
  },
})
export default class CrapUp extends Vue {}
</script>

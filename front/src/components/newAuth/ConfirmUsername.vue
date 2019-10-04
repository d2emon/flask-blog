<template>
  <v-card>
    <div>Did I get the name right {{username}}?</div>
    <v-btn
      to="/new-login"
    >
      Yes
    </v-btn>
    <v-btn
      to="/ask-password"
    >
      No
    </v-btn>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapState,
} from 'vuex';

@Component({
  computed: {
    ...mapState('newAuth', ['username']),
  },
})
export default class ConfirmUsername extends Vue {}
</script>

<template>
  <v-card flat>
    <v-card-title>Did I get the name right {{username}}?</v-card-title>
    <v-card-actions>
      <v-btn
        @click="submitUsername"
      >
        Yes
      </v-btn>
      <v-btn
        @click="resetUsername"
      >
        No
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapState,
  mapActions,
} from 'vuex';

@Component({
  computed: {
    ...mapState('newAuth', ['username']),
  },
  methods: {
    ...mapActions('newAuth', [
      'submitUsername',
      'resetUsername',
    ]),
  },
})
export default class ConfirmUsername extends Vue {}
</script>

<template>
  <v-card>
    <div>Creating new persona...</div>
    <v-text-field
      type="password"
      label="Give me a password for this persona"
      v-model="password"
      :rules="rules"
      :error-messages="error"
      required
      :size="15"
    />
    <v-btn
      to="/motd"
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
import {
  isRequired,
} from '@/helpers/validators';

@Component({
  computed: {
    ...mapState('newAuth', {
      error: 'error',
      defaultUsername: 'username',
    }),
  },
  methods: {
    ...mapActions('newAuth', ['onUsername']),
  },
})
export default class AskPassword extends Vue {
  password: string = '';

  rules = [
    isRequired('Username is required'),
    (v: string) => !v || v.replace(/[^a-zA-Z]/g, '') === v || 'Wrong username',
  ];
}
</script>

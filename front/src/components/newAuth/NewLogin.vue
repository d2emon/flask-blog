<template>
  <v-card>
    <v-text-field
      label="By what name shall I call you?"
      v-model="username"
      :rules="rules"
      :error-messages="error"
      required
      :size="15"
    />
    <v-btn
      to="/confirm-username"
    >
      New
    </v-btn>
    <v-btn
      to="/ask-password"
    >
      Old
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
export default class NewLogin extends Vue {
  username: string = (this as any).defaultUsername;

  rules = [
    isRequired('Username is required'),
    (v: string) => !v || v.replace(/[^a-zA-Z]/g, '') === v || 'Wrong username',
  ];
}
</script>

<template>
  <v-form
    ref="newLoginForm"
  >
    <v-text-field
      label="By what name shall I call you?"
      v-model="username"
      :rules="rules"
      :error-messages="error"
      required
      :size="15"
    />
    <v-btn
      @click="login"
    >
      Log In
    </v-btn>
  </v-form>
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
  username: string = (this as any).defaultUsername || '';

  rules = [
    isRequired('Username is required'),
    (v: string) => !v || v.replace(/[^a-zA-Z]/g, '') === v || 'Illegal characters in username',
  ];

  login() {
    this.$refs.newLoginForm.validate();
    (this as any).onUsername(this.username);
  }
}
</script>

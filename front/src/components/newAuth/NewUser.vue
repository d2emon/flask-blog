<template>
  <v-form
    ref="newUserForm"
  >
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
      @click="auth"
    >
      Next
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
    ...mapState('newAuth', [
      'error',
      'username',
    ]),
  },
  methods: {
    ...mapActions('newAuth', ['newUser']),
  },
})
export default class AskPassword extends Vue {
  password: string = '';

  rules = [
    isRequired('Password is required'),
    (v: string) => !v || v.indexOf('.') < 0 || 'Illegal characters in password',
  ];

  auth() {
    this.$refs.newUserForm.validate();
    (this as any).newUser({
      username: (this as any).username,
      password: this.password,
    });
  }
}
</script>

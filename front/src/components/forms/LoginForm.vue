<template>
  <v-form
    ref="loginForm"
    v-model="valid"
  >
    <v-text-field
      v-model="username"
      :rules="usernameRules"
      label="Login"
      size="20"
      required
    />
    <v-text-field
      v-model="password"
      :rules="passwordRules"
      label="Password"
      type="Password"
      size="20"
      required
    />
    <v-checkbox
      v-model="rememberMe"
      label="Remember me"
    />
    <v-btn
      :disabled="!valid"
      color="success"
      @click="validate"
    >
      Submit
    </v-btn>
  </v-form>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

type Validator = (v: any) => string | boolean;

@Component
export default class Login extends Vue {
  isRequired: (msg: string) => Validator = (msg: string) => (v: any) => !!v || msg;

  valid: boolean = true;

  username: string = '';

  usernameRules: Validator[] = [
    this.isRequired('Login is required'),
  ];

  password: string = '';

  passwordRules: Validator[] = [
    this.isRequired('Password is required'),
  ];

  rememberMe: boolean = true;

  validate() {
    if (this.$refs.loginForm.validate()) {
      this.$emit('submit', {
        username: this.username,
        password: this.password,
        remember_me: this.rememberMe,
      });
    }
  }
}
</script>

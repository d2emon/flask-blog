<template>
  <v-form
    ref="authForm"
  >
    <confirm-username
      v-model="showConfirm"
      :username="usernameValue"
      :password="password"
      @confirm="save"
    />

    <v-alert
      v-if="error"
      type="error"
    >
      {{ error }}
    </v-alert>

    <v-text-field
      label="By what name shall I call you?"
      v-model="usernameValue"
      :rules="rules.username"
      :error-messages="error"
      required
      :size="15"
    />
    <div v-if="exists">Creating new persona...</div>
    <v-text-field
      type="password"
      :label="passwordLabel"
      v-model="password"
      :rules="rules.password"
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
  components: {
    ConfirmUsername: () => import('@/components/newAuth/ConfirmUsername.vue'),
  },
  computed: {
    ...mapState('newAuth', {
      error: 'error',
    }),
  },
  methods: {
    ...mapActions('newAuth', [
      'findUser',
      'newUser',
      'authUser',
    ]),
  },
  props: {
    username: String,
  },
})
export default class AuthForm extends Vue {
  usernameValue: string = (this as any).username || '';

  password: string = '';

  exists: boolean = false;

  showConfirm: boolean = false;

  rules = {
    username: [
      isRequired('Username is required'),
      (v: string) => !v || v.replace(/[^a-zA-Z]/g, '') === v || 'Illegal characters in username',
    ],
    password: [
      isRequired('Password is required'),
      (v: string) => !v || v.indexOf('.') < 0 || 'Illegal characters in password',
    ],
  };

  get passwordLabel() {
    return this.exists
      ? 'Give me a password for this persona'
      : 'This persona already exists, what is the password?';
  }

  login() {
    if (!this.$refs.authForm.validate()) return;
    (this as any).findUser(this.usernameValue)
      .then((userId: number | null) => {
        this.exists = !!userId;
        this.showConfirm = !userId;
        if (!userId) return;
        (this as any).authUser({
          username: (this as any).usernameValue,
          password: this.password,
        });
        this.$emit('auth');
      });
  }

  save() {
    (this as any).newUser({
      username: (this as any).usernameValue,
      password: this.password,
    });
    this.$emit('auth');
  }
}
</script>

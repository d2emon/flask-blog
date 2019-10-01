<template>
  <v-container id="login">
    <v-row justify="center">
      <v-col md="4">
        <v-card>
          <v-card-title>
            <h1>Sign In</h1>
          </v-card-title>

          <v-container>
            <login-form
              @submit="onSubmit"
            />
            <br />
            <p>
              New User?
              <router-link to="/register">Click to Register!</router-link>
            </p>
            <p>
              Forgot Your Password?
              <router-link to="/reset_password_request">Click to Reset It!</router-link>
            </p>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapActions,
  mapState,
} from 'vuex';
import { LoginFormData } from '@/forms/types';

@Component({
  components: {
    LoginForm: () => import('@/forms/LoginForm.vue'),
  },
  computed: {
    ...mapState(['user']),
  },
  methods: {
    ...mapActions([
      'loginUser',
      'fetchToken',
    ]),
  },
})
export default class Login extends Vue {
  onSubmit(data: LoginFormData) {
    console.log(data);
    const {
      username,
      password,
      rememberMe,
    } = data;
    (this as any).fetchToken({
      auth: {
        username,
        password,
      },
      rememberMe,
    })
      .then(() => {
        if (!(this as any).user) return;
        this.$router.push('/');
      });
  }
}
</script>

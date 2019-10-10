<template>
  <v-card>
    <v-card-title>
      <h1>Blog</h1>
    </v-card-title>
    <v-card-title>
      <h2>By D2emon</h2>
    </v-card-title>
    <v-container>
      <v-alert
        v-if="error"
        type="error"
      >
        {{ error }}
      </v-alert>
      <motd
        v-model="showMessageOfTheDay"
        :message="motd"
      />
      <auth-form
        v-if="!isAuthorized"
        @auth="onAuth"
      />
      <user-menu
        v-else
      />
    </v-container>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapActions,
  mapState,
} from 'vuex';
import * as roles from '@/d2auth/services/login/roles';

@Component({
  components: {
    AuthForm: () => import('@/components/newAuth/AuthForm.vue'),
    NewLoginForm: () => import('@/forms/NewLoginForm.vue'),
    Motd: () => import('@/components/newAuth/Motd.vue'),
    UserMenu: () => import('@/components/newAuth/UserMenu.vue'),
  },
  computed: {
    ...mapState('newAuth', [
      'error',
      'createdAt',
      'startedAt',
      'motd',
      'role',
    ]),
  },
  methods: {
    ...mapActions('newAuth', ['checkNewAuth']),
  },
})
export default class Intro extends Vue {
  showMessageOfTheDay: boolean = false;

  get isAuthorized(): boolean {
    return (this as any).role !== roles.UNAUTHORIZED;
  }

  get isAdmin(): boolean {
    return (this as any).role === roles.ADMIN;
  }

  onAuth() {
    if (!(this as any).error) {
      this.showMessageOfTheDay = true;
    }
  }

  created() {
    (this as any).checkNewAuth();
  }
}
</script>

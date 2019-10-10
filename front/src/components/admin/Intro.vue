<template>
  <v-card>
    <v-card-title>
      <h1>Blog</h1>
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
        :message="user && user.messageOfTheDay"
      />

      <confirm-username
        v-model="showConfirm"
        :message="`Did I get the name right, ${user.username}?`"
        @confirm="save(true)"
      />

      <login-form
        v-if="!isAuthorized"
        :default-username="defaultUsername"
        :errors="errors"
        @submit="login"
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
import * as roles from '@/auth/roles';
import { User } from '@/auth/types';

@Component({
  components: {
    ConfirmUsername: () => import('@/modals/ConfirmUsername.vue'),
    LoginForm: () => import('@/forms/LoginForm.vue'),

    Motd: () => import('@/modals/Motd.vue'),
    UserMenu: () => import('@/components/admin/UserMenu.vue'),
  },
  computed: {
    ...mapState('auth', [
      'errors',
      'user',
    ]),
  },
  methods: {
    ...mapActions('auth', [
      'fetchUser',
      'newUser',
      'authUser',
    ]),
  },
})
export default class Intro extends Vue {
  defaultUsername: string = '';

  user: User = {
    username: '',
    password: '',
  };

  showConfirm: boolean = false;

  showMessageOfTheDay: boolean = false;

  get isAuthorized(): boolean {
    return (this as any).user && ((this as any).user.role !== roles.UNAUTHORIZED);
  }

  get isAdmin(): boolean {
    return (this as any).user && ((this as any).user.role === roles.ADMIN);
  }

  get error(): string | null {
    return ((this as any).errors && (this as any).errors['']) || null;
  }

  async login(user: User) {
    this.user = user;
    const userId: number | null = await (this as any).fetchUser(user.username);
    if ((this as any).errors) return;
    if (!userId) {
      this.showConfirm = true;
      return;
    }
    await this.save(false);
  }

  async save(isNew: boolean = false) {
    if (isNew) {
      await (this as any).newUser((this as any).user);
    } else {
      await (this as any).authUser((this as any).user);
    }
    // On Auth
    if (!(this as any).error) {
      this.showMessageOfTheDay = true;
    }
  }
}
</script>

<template>
  <v-layout row>
    <confirm-username
      v-model="showConfirm"
      :message="`Did I get the name right ${user.username}?`"
      @confirm="save(true)"
    />

    <v-flex xs6>
      <v-container>
        <v-card flat>
          <v-card-text>
            <div>This blog was created: <span>{{ createdAt || '&lt;unknown&gt;' }}</span></div>
            <div v-if="startedAt">Time elapsed: <span>{{ startedAt }}</span></div>
            <div v-else>Blog has yet to ever start!!!</div>
          </v-card-text>
        </v-card>
      </v-container>
    </v-flex>

    <v-flex xs6>
      <v-container>
        <new-login-form
          :default-username="defaultUsername"
          :errors="errors"
          @submit="login"
        />
      </v-container>
    </v-flex>
  </v-layout>
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
import { User } from '@/services/login/types';

@Component({
  components: {
    ConfirmUsername: () => import('@/components/newAuth/ConfirmUsername.vue'),
    NewLoginForm: () => import('@/forms/NewLoginForm.vue'),
  },
  computed: {
    ...mapState('newAuth', [
      'errors',

      'createdAt',
      'startedAt',
    ]),
  },
  methods: {
    ...mapActions('newAuth', [
      'fetchUser',
      'newUser',
      'authUser',
    ]),
  },
  props: {
    defaultUsername: String,
  },
})
export default class AuthForm extends Vue {
  user: User = {
    username: '',
    password: '',
  };

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
      await (this as any).newUser(this.user);
    } else {
      await (this as any).authUser(this.user);
    }
    this.$emit('auth');
  }
}
</script>

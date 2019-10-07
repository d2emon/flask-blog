<template>
  <v-card>
    <v-card-title>
      <h1>New  Auth</h1>
    </v-card-title>
    <v-card-title>
      <h2>By D2emon</h2>
    </v-card-title>
    <v-container>
      <v-card-text>
        <v-alert
          v-if="error"
          type="error"
        >
          {{ error }}
        </v-alert>
        <div>This blog was created: <span>{{ createdAt || '&lt;unknown&gt;' }}</span></div>
        <div v-if="startedAt">Time elapsed: <span>{{ startedAt }}</span></div>
        <div v-else>Blog has yet to ever start!!!</div>
      </v-card-text>

      <template v-if="!user">
        <new-login />
        <confirm-username v-if="isNew" />
        <new-user v-if="isNew" />
        <ask-password v-else />
      </template>
      <motd v-else />
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

@Component({
  components: {
    NewLogin: () => import('@/components/newAuth/NewLogin.vue'),
    ConfirmUsername: () => import('@/components/newAuth/ConfirmUsername.vue'),
    NewUser: () => import('@/components/newAuth/NewUser.vue'),
    AskPassword: () => import('@/components/newAuth/AskPassword.vue'),
    Motd: () => import('@/components/newAuth/Motd.vue'),
  },
  computed: {
    ...mapState('newAuth', [
      'error',
      'createdAt',
      'startedAt',
      'isNew',
      'user',
    ]),
  },
  methods: {
    ...mapActions('newAuth', ['startNewAuth']),
  },
})
export default class Intro extends Vue {
  created() {
    (this as any).startNewAuth();
  }
}
</script>

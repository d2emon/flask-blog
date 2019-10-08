<template>
  <v-card>
    <v-card-title>
      <h1>New  Auth</h1>
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
    AuthForm: () => import('@/components/newAuth/AuthForm.vue'),
    NewLoginForm: () => import('@/forms/NewLoginForm.vue'),
    Motd: () => import('@/components/newAuth/Motd.vue'),
  },
  computed: {
    ...mapState('newAuth', [
      'error',
      'createdAt',
      'startedAt',
      'motd',
    ]),
  },
  methods: {
    ...mapActions('newAuth', ['checkNewAuth']),
  },
})
export default class Intro extends Vue {
  isAuthorized: boolean = false;

  showMessageOfTheDay: boolean = false;

  onAuth() {
    if (!(this as any).error) {
      this.showMessageOfTheDay = true;
      this.isAuthorized = true;
    }
  }

  created() {
    (this as any).checkNewAuth();
  }
}
</script>

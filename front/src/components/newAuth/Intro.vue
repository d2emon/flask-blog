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

      <auth-form
        v-if="!user"
        @auth="onAuth"
      />
      <motd
        v-model="showMotd"
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
    Motd: () => import('@/components/newAuth/Motd.vue'),
  },
  computed: {
    ...mapState('newAuth', [
      'error',
      'createdAt',
      'startedAt',
      'user',
    ]),
  },
  methods: {
    ...mapActions('newAuth', ['startNewAuth']),
  },
})
export default class Intro extends Vue {
  showMotd: boolean = false;

  onAuth() {
    this.showMotd = true;
  }

  created() {
    (this as any).startNewAuth();
  }
}
</script>

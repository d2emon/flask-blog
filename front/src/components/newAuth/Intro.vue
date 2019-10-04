<template>
  <v-card>
    <h1>New  Auth</h1>
    <h2>By D2emon</h2>
    <div>This blog was created:{{ createdAt || '&lt;unknown&gt;' }}</div>
    <div v-if="startedAt">Game time elapsed: {{ startedAt }}</div>
    <div v-else>AberMUD has yet to ever start!!!</div>
    <v-btn
      to="/new-login"
    >
      Next
    </v-btn>
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
    // LoginForm: () => import('@/forms/LoginForm.vue'),
  },
  computed: {
    ...mapState('newAuth', [
      'createdAt',
      'startedAt',
    ]),
  },
  methods: {
    ...mapActions('newAuth', ['startNewAuth']),
  },
})
export default class Intro extends Vue {
  created() {
    (this as any).startNewAuth({
      userId: 'userId',
      hostname: 'hostname',
    });
  }
}
</script>

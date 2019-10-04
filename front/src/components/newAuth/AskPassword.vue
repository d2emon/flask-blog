<template>
  <v-card>
    <v-text-field
      type="password"
      label="This persona already exists, what is the password?"
      v-model="password"
      :rules="rules"
      :error-messages="error"
      required
      :size="15"
    />
    <v-btn
      to="/motd"
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
  computed: {
    ...mapState('newAuth', {
      error: 'error',
      defaultUsername: 'username',
    }),
  },
  methods: {
    ...mapActions('newAuth', ['onUsername']),
  },
})
export default class AskPassword extends Vue {
  password: string = '';

  rules = [
  ];
}
</script>

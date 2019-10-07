<template>
  <v-form>
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
  computed: {
    ...mapState('newAuth', [
      'error',
      'username',
    ]),
  },
  methods: {
    ...mapActions('newAuth', ['authUser']),
  },
})
export default class AskPassword extends Vue {
  password: string = '';

  rules = [
    isRequired('Password is required'),
    (v: string) => !v || v.indexOf('.') < 0 || 'Illegal characters in password',
  ];

  auth() {
    this.$refs.newUserForm.validate();
    (this as any).authUser({
      username: (this as any).username,
      password: this.password,
    });
  }
}
</script>

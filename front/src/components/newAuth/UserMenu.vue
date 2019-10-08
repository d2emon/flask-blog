<template>
  <v-card>
    <v-card-title>
      <h1>Welcome To Blog</h1>
    </v-card-title>
    <v-list
      one-line
      subheader
    >
      <v-subheader>Options</v-subheader>

      <v-list-item>
        <v-list-item-content>
          Enter The Game
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-content>
          Change Password
        </v-list-item-content>
      </v-list-item>
      <v-list-item>
        <v-list-item-content>
          Exit AberMUD
        </v-list-item-content>
      </v-list-item>

      <template v-if="isAdmin">
        <v-divider />

        <v-list-item>
          <v-list-item-content>
            Run TEST game
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            Show persona
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            Edit persona
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            Delete persona
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapState,
} from 'vuex';
import * as roles from '@/services/login/roles';

@Component({
  computed: {
    ...mapState('newAuth', [
      'role',
    ]),
  },
})
export default class UserMenu extends Vue {
  get isAdmin() {
    return (this as any).role === roles.ADMIN;
  }
}
</script>

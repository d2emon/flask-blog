<template>
  <v-container id="login">
    <v-row justify="center">
      <v-col md="6">
        <v-card>
          <v-card-actions>
            <v-btn
              to="/"
            >
              Back
            </v-btn>
          </v-card-actions>
          <v-container>
            <login-form
              @submit="onSubmit"
            />
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapActions,
} from 'vuex';

@Component({
  components: {
    LoginForm: () => import('@/components/forms/LoginForm.vue'),
  },
  methods: {
    ...mapActions(['userLogin']),
  },
})
export default class Login extends Vue {
  onSubmit(credentials: {
    username: string,
    password: string,
  }) {
    console.log('Submit');
    (this as any).userLogin(credentials);
  }
}
</script>

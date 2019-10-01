<template>
  <v-container id="registration">
    <v-row justify="center">
      <v-col md="4">
        <v-card>
          <v-card-title>
            <h1>Register</h1>
          </v-card-title>

          <v-container>
            <registration-form
              :errors="errors"
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
import { RegistrationFormData } from '@/forms/types';

@Component({
  components: {
    RegistrationForm: () => import('@/forms/RegistrationForm.vue'),
  },
  methods: {
    ...mapActions(['registerUser']),
  },
})
export default class Registration extends Vue {
  errors?: {[field: string]: string} = {};

  onSubmit(data: RegistrationFormData) {
    (this as any).registerUser(data)
      .then((response) => {
        this.errors = response.errors;
        console.log(response, this.errors);
      });
  }
}
</script>

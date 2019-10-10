<template>
  <base-form
    :form-name="formName"
    :fields="formData"
    :errors="errors"
    @submit="formSubmit"
  />
</template>

<script lang="ts">
import Vue from 'vue';
import {
  Component,
} from 'vue-property-decorator';
import {
  FormData,
} from './types';
import {
  isEmail,
  isRequired,
} from '@/helpers/validators';

@Component({
  components: {
    BaseForm: () => import('./BaseForm.vue'),
  },
  props: {
    errors: Object,
  },
})
export default class RegistrationForm extends Vue {
  formName: string = 'registrationForm';

  passwordsEqual(v: any) {
    return v === this.formData.password.value || 'Passwords are not equal';
  }

  formData: FormData = {
    username: {
      label: 'Username',
      rules: [
        isRequired('Username is required'),
      ],
      required: true,
      size: 20,
    },
    email: {
      label: 'Email',
      rules: [
        isRequired('Email is required'),
        isEmail(),
      ],
      required: true,
      size: 20,
      type: 'email',
    },
    password: {
      label: 'Password',
      rules: [
        isRequired('Password is required'),
      ],
      required: true,
      size: 20,
      type: 'password',
    },
    password2: {
      label: 'Repeat Password',
      rules: [
        isRequired(),
        this.passwordsEqual,
      ],
      required: true,
      size: 20,
      type: 'password',
    },
  };

  formSubmit(values: {}) {
    this.$emit('submit', values);
  }
}
</script>

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
export default class ChangePassword extends Vue {
  formName: string = 'changePasswordForm';

  formData: FormData = {
    oldPassword: {
      label: 'Old Password',
      rules: [
        isRequired('Password is required'),
      ],
      required: true,
      size: 20,
      type: 'password',
    },
    newPassword: {
      label: 'New Password',
      rules: [
        isRequired('Password is required'),
        (v: string) => v.indexOf('.') < 0 || 'Illegal characters in password',
      ],
      required: true,
      size: 20,
      type: 'password',
    },
    verifyPassword: {
      label: 'Verify Password',
      rules: [
        isRequired('Password is required'),
        (v: string) => v === this.formData.newPassword.value || 'Password not verified',
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

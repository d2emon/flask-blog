<template>
  <!-- div v-if="exists">Creating new persona...</div -->

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
    defaultUsername: String,
    errors: Object,
  },
})
export default class NewLogin extends Vue {
  formName: string = 'newLoginForm';

  formData: FormData = {
    username: {
      label: 'By what name shall I call you?',
      rules: [
        isRequired('Username is required'),
        (v: string) => !v || v.replace(/[^a-zA-Z]/g, '') === v || 'Illegal characters in username',
      ],
      required: true,
      size: 15,
      value: (this as any).defaultUsername,
    },
    password: {
      label: 'Give me a password for this persona',
      // :label="passwordLabel"
      rules: [
        isRequired('Password is required'),
        (v: string) => !v || v.indexOf('.') < 0 || 'Illegal characters in password',
      ],
      required: true,
      size: 20,
      type: 'password',
    },
  };

  /*
  get passwordLabel() {
    return this.exists
      ? 'Give me a password for this persona'
      : 'This persona already exists, what is the password?';
  }
   */

  formSubmit(values: {}) {
    this.$emit('submit', values);
  }
}
</script>

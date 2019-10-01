<template>
  <v-form
    ref="registrationForm"
    v-model="valid"
  >
    <v-text-field
      v-for="field in Object.keys(formData)"
      :key="field"
      :label="formData[field].label"
      v-model="formData[field].value"
      :rules="formData[field].rules"
      :error-messages="formData[field].errors"
      :required="formData[field].required"
      :size="formData[field].size"
      :type="formData[field].type"
      @input="onInput(field)"
    />
    <v-btn
      :disabled="!valid"
      color="success"
      @click="validate"
    >
      Submit
    </v-btn>
  </v-form>
</template>

<script lang="ts">
import Vue from 'vue';
import {Component, Watch} from 'vue-property-decorator';
import {
  RegistrationFormData,
} from './types';
import {
  isEmail,
  isRequired,
} from '@/helpers/validators';

@Component({
  props: {
    errors: Object,
  },
})
export default class RegistrationForm extends Vue {
  valid: boolean = true;

  passwordsEqual(v: any) {
    return v === this.formData.password.value || 'Passwords are not equal';
  }

  formData: RegistrationFormData = {
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

  validate() {
    if (this.$refs.registrationForm.validate()) {
      this.$emit('submit', Object.keys(this.formData).reduce(
        (res, key: string) => ({
          ...res,
          [key]: (this as any).formData[key].value,
        }),
        {},
      ));
    }
  }

  onInput(field: string) {
    (this as any).formData[field].errors = [];
  }

  @Watch('errors')
  watchErrors(errors: {[field: string]: string[]}) {
    if (!errors) return;

    Object.keys(errors).forEach(
      (key: string) => {
        this.$set((this as any).formData, key, {
          ...(this as any).formData[key],
          errors: errors[key],
        });
      },
    );
  }
}
</script>

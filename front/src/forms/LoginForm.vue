<template>
  <v-form
    ref="loginForm"
    v-model="valid"
  >
    <template v-for="field in Object.keys(formData)">
      <v-checkbox
        v-if="formData[field].isCheckBox"
        :key="field"
        :label="formData[field].label"
        v-model="formData[field].value"
        :rules="formData[field].rules"
        :error-messages="formData[field].errors"
        @input="onInput(field)"
      />
      <v-text-field
        v-else
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
    </template>
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
import {
  Component,
  Watch,
} from 'vue-property-decorator';
import {
  LoginFormData,
} from './types';
import {
  isRequired,
} from '@/helpers/validators';

@Component({
  props: {
    errors: Object,
  },
})
export default class Login extends Vue {
  valid: boolean = true;

  formData: LoginFormData = {
    username: {
      label: 'Username',
      rules: [
        isRequired('Username is required'),
      ],
      required: true,
      size: 20,
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
    rememberMe: {
      label: 'Remember Me',
      value: true,
      rules: [],
      isCheckBox: true,
    },
  };

  validate() {
    if (this.$refs.loginForm.validate()) {
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

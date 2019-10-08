<template>
  <v-form
    ref="loginForm"
    v-model="valid"
  >
    <!-- div v-if="exists">Creating new persona...</div -->

    <template v-for="field in Object.keys(formData)">
      <base-field
        :key="field"
        v-model="formData[field]"
        @input="fieldInput(field)"
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
  NewLoginFormData,
} from './types';
import {
  isRequired,
} from '@/helpers/validators';

@Component({
  components: {
    BaseField: () => import('./BaseField.vue'),
  },
  props: {
    defaultUsername: String,
    errors: Object,
  },
})
export default class NewLogin extends Vue {
  valid: boolean = true;

  formData: NewLoginFormData = {
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

  fieldInput(field: string) {
    (this as any).formData[field].errors = [];
  }

  submit() {
    this.$emit('submit', Object.keys(this.formData).reduce(
      (res, key: string) => ({
        ...res,
        [key]: (this as any).formData[key].value,
      }),
      {},
    ));
  }

  validate() {
    if (!this.$refs.loginForm.validate()) return;

    this.submit();
  }
}
</script>

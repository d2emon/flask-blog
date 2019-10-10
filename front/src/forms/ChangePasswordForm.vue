<template>
  <v-form
    ref="changePasswordForm"
    v-model="valid"
  >
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
  FormData,
} from './types';
import {
  isRequired,
} from '@/helpers/validators';

@Component({
  components: {
    BaseField: () => import('./BaseField.vue'),
  },
  props: {
    errors: Object,
  },
})
export default class ChangePassword extends Vue {
  valid: boolean = true;

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
    if (!this.$refs.changePasswordForm.validate()) return;

    this.submit();
  }
}
</script>

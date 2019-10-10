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
    BaseForm: () => import('./BaseForm.vue'),
  },
  props: {
    username: String,
    errors: Object,
  },
})
export default class EditUser extends Vue {
  formName: string = 'editUserForm';

  formData: FormData = {
    username: {
      label: 'Username:',
      rules: [
        isRequired('Username is required'),
      ],
      required: true,
      size: 15,
      value: (this as any).username,
    },
  };

  @Watch('username')
  watchUsername(username:string) {
    this.$set((this as any).formData, 'username', {
      ...(this as any).formData.username,
      value: username,
    });
  }

  formSubmit(values: {}) {
    this.$emit('submit', values);
  }
}
</script>

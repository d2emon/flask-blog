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
export default class AskUser extends Vue {
  formName: string = 'askUserForm';

  formData: FormData = {
    username: {
      label: 'Username:',
      rules: [
        isRequired('Username is required'),
      ],
      required: true,
      size: 15,
    },
  };

  formSubmit(values: {}) {
    this.$emit('submit', values);
  }
}
</script>

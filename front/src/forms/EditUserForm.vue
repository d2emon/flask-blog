<template>
  <v-form
    :ref="formName"
    v-model="valid"
    lazy
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
    username: String,
    errors: Object,
  },
})
export default class EditUser extends Vue {
  formName: string = 'askUserForm';

  valid: boolean = true;

  formData: FormData = {
    username: {
      label: 'Username:',
      rules: [
        isRequired('Username is required'),
      ],
      required: true,
      size: 15,
      value: username,
    },
  };

  @Watch('username')
  watchUsername(username:string) {
    this.$set((this as any).formData, 'username', {
      ...(this as any).formData.username,
      value: username,
    });
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
    (this.$refs[this.formName] as any).reset();
  }

  validate() {
    if (!(this.$refs[this.formName] as any).validate()) return;

    this.submit();
  }
}
</script>

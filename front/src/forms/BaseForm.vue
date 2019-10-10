<template>
  <v-form
    :ref="formName"
    v-model="valid"
    lazy
  >
    <template v-for="field in Object.keys(fields)">
      <base-field
        :key="field"
        v-model="fields[field]"
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

@Component({
  components: {
    BaseField: () => import('./BaseField.vue'),
  },
  props: {
    formName: String,
    fields: Object,
    errors: Object,
  },
})
export default class BaseForm extends Vue {
  valid: boolean = true;

  @Watch('errors')
  watchErrors(errors: {[field: string]: string[]}) {
    if (!errors) return;

    Object.keys(errors).forEach(
      (key: string) => {
        this.$set((this as any).fields, key, {
          ...(this as any).fields[key],
          errors: errors[key],
        });
      },
    );
  }

  fieldInput(field: string) {
    (this as any).fields[field].errors = [];
  }

  submit() {
    this.$emit('submit', Object.keys((this as any).fields).reduce(
      (res, key: string) => ({
        ...res,
        [key]: (this as any).fields[key].value,
      }),
      {},
    ));
    (this.$refs[(this as any).formName] as any).reset();
  }

  validate() {
    if (!(this.$refs[(this as any).formName] as any).validate()) return;

    this.submit();
  }
}
</script>

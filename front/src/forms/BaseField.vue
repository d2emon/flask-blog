<template>
  <v-checkbox
    v-if="value.isCheckBox"
    :label="value.label"
    v-model="fieldValue"
    :rules="value.rules"
    :error-messages="value.errors"
    @input="input"
  />
  <v-text-field
    v-else
    :label="value.label"
    v-model="fieldValue"
    :rules="value.rules"
    :error-messages="value.errors"
    :required="value.required"
    :size="value.size"
    :type="value.type"
    @input="input"
  />
</template>

<script lang="ts">
import Vue from 'vue';
import {
  Component,
  Watch,
} from 'vue-property-decorator';
import { FormField } from './types';

@Component({
  props: {
    value: Object,
  },
})
export default class BaseField extends Vue {
  fieldValue: any = (this as any).value.value || '';

  @Watch('value')
  onNewValue(newValue: FormField<any>) {
    this.fieldValue = newValue.value;
  }

  input() {
    this.$emit('input', {
      ...(this as any).value,
      value: this.fieldValue,
    });
  }
}
</script>

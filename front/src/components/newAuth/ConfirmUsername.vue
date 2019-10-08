<template>
  <v-dialog
    v-model="show"
    max-width="512"
    persistent
  >
    <v-card>
      <v-card-title>{{ message }}</v-card-title>
      <v-card-actions>
        <v-btn
          color="success"
          @click="submitUsername"
        >
          Yes
        </v-btn>
        <v-btn
          color="error"
          @click="resetUsername"
        >
          No
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component, Watch } from 'vue-property-decorator';

@Component({
  props: {
    message: String,
    value: Boolean,
  },
})
export default class ConfirmUsername extends Vue {
  show: boolean = false;

  @Watch('show')
  onShow(newValue: boolean) {
    this.$emit('input', newValue);
  }

  @Watch('value')
  onValue(newValue: boolean) {
    this.show = newValue;
  }

  submitUsername() {
    this.$emit('input', false);
    this.$emit('confirm');
  }

  resetUsername() {
    this.$emit('input', false);
    this.$emit('decline');
  }
}
</script>

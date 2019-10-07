<template>
  <v-dialog
    v-model="show"
    max-width="512"
    persistent
  >
    <v-card>
      <v-card-text>{{ motd }}</v-card-text>
      <v-card-actions>
        <v-btn
          @click="$emit('input', false)"
        >
          Ok
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import Vue from 'vue';
import {
  Component,
  Watch,
} from 'vue-property-decorator';
import {
  mapActions,
  mapState,
} from 'vuex';

// !defaultUsername

@Component({
  computed: {
    ...mapState('newAuth', ['motd']),
  },
  methods: {
    ...mapActions('newAuth', [
      'fetchMotd',
      'startMain',
    ]),
  },
  props: {
    value: Boolean,
  },
})
export default class Motd extends Vue {
  show: boolean = false;

  @Watch('value')
  onValue(newValue: boolean) {
    this.show = newValue;
    if (newValue) {
      (this as any).fetchMotd();
    }
  }
}
</script>

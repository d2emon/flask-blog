<template>
  <v-footer
    class="py-4"
    dark
    height="auto"
  >
    <v-container mx-auto>
      <v-layout wrap>
        <v-flex xs9>
          <social-button
            v-for="(item, itemId) in items"
            :key="itemId"
            :href="item.href"
            class="ml-0 mr-3"
            color="primary"
            square
            target="_blank"
          >
            <v-icon v-text="item.icon"></v-icon>
          </social-button>
        </v-flex>
        <v-spacer></v-spacer>
        <social-button
          class="mr-0"
          square
          title="Go to top"
          @click="$vuetify.goTo(0)"
        >
          <v-icon>mdi-chevron-up</v-icon>
        </social-button>
      </v-layout>
    </v-container>
  </v-footer>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapGetters,
  mapMutations,
} from 'vuex';
import { Link } from '@/types';

@Component({
  components: {
    SocialButton: () => import('@/components/controls/SocialButton.vue'),
  },
  computed: {
    ...mapGetters(['links']),
  },
  methods: {
    ...mapMutations(['toggleDrawer']),
  },
})
export default class MainFooter extends Vue {
  items: Link[] = [
    {
      href: '#!',
      icon: 'mdi-twitter',
    },
    {
      href: '#!',
      icon: 'mdi-instagram',
    },
    {
      href: '#!',
      icon: 'mdi-facebook',
    },
    {
      href: '#!',
      icon: 'mdi-google-plus',
    },
    {
      href: '#!',
      icon: 'mdi-reddit',
    },
    {
      href: '#!',
      icon: 'mdi-discord',
    },
    {
      href: '#!',
      icon: 'mdi-pinterest',
    },
  ];
}
</script>

<style scoped>

</style>

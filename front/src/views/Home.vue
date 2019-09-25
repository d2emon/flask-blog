<template>
  <v-container id="home">
    <articles>
      <banner
        :image="require('@/assets/articles/blurcamera.jpg')"
        title="The Art of Travel"
        subtitle="Finding Beauty, One flight at a time"
      />
    </articles>

    <about>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ut tortor tellus. Donec maximus curs us pulvinar.
        Proin vehicula eros mauris, sit amet rutrum libero vestibulum ac. Morbi ullamcorper eu lacus vulputate consect.
        Etur vivamus sagittis accumsan quam eu malesuada. Proin et ante vel libero ultrices cursus. Donec felis leo, cu
        rsus eget hendrerit at, congue nec enim.
      </p>
    </about>

    <subscribe :contacts="contacts">
      <p>
        Enter your email address to subscribe to this blog
        and receive notifications of new posts by email.
      </p>
    </subscribe>

    <social />

    <hello-world />
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import { Contact } from '@/types';

const contacts: Contact[] = [
  {
    icon: 'mdi-email-outline',
    title: 'EMAIL',
    subtitle: 'THEARTOFTRAVEL@GMAIL.COM',
  },
  {
    icon: 'mdi-map-marker',
    title: 'ADDRESS',
    subtitle: '1234 WORLD DR. HERE, TX 76123',
  },
  {
    icon: 'mdi-phone',
    title: 'PHONE',
    subtitle: '555-789-1234',
  },
];

@Component({
  components: {
    HelloWorld: () => import('@/components/HelloWorld.vue'),
    About: () => import('@/components/About.vue'),
    Articles: () => import('@/components/Articles.vue'),
    Banner: () => import('@/components/Banner.vue'),
    Social: () => import('@/components/Social.vue'),
    Subscribe: () => import('@/components/Subscribe.vue'),
  },
  data: () => ({
    contacts,
  })
})
export default class Home extends Vue {}
</script>
